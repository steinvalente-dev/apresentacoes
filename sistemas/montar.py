#!/usr/bin/env python3
"""montar — monta uma peça a partir do esqueleto, de um bloco de marca e de um deck.json.

Uso, na raiz do clone:
  python3 sistemas/montar.py <slug> --marca <michel-stein|sarasa|amaz|lavro> --deck <deck.json>
                             [--img <pasta>] [--cliente] [--sobrescrever]

O que faz, sempre na mesma ordem e sem decidir nada:
  1. abre esqueleto/deck-esqueleto.html e cola, nos lugares marcados `COLAR:x`, os trechos
     `TRECHO:x` do bloco da marca: fontes, :root, constantes, abertura e contracapa do DECK
     (e CAPA_IMGS, quando o bloco traz);
  2. lê o deck.json, completa a `capa` com o topo do arquivo e serializa o miolo no DECK;
  3. redimensiona as imagens que apontam para arquivo em --img (Pillow) e embute em base64 —
     ou, acima de 8 MB, grava em <slug>/img/ e avisa que a peça passa a exigir a PASTA;
  4. escreve <slug>/apresentacao.html e <slug>/meta.json (o que registra a peça no acervo);
  5. confere o script gerado (node --check) e roda `for(const s of DECK) tpl(s)` num Node mínimo.

Formato do deck.json e o que fazer quando algo falha: sistemas/DECK-JSON.md.
Depois de montar, SEMPRE: node sistemas/validar.mjs <slug>/apresentacao.html

Códigos de saída: 0 ok · 1 erro de entrada ou de sintaxe · 2 peça já existe (use --sobrescrever)
                  · 3 peça escrita, mas com slide(s) de aviso — corrigir o deck.json
"""
import argparse, base64, datetime, html, io, json, os, pathlib, re, shutil, subprocess, sys, tempfile

RAIZ = pathlib.Path(__file__).resolve().parent.parent
MARCAS = ('michel-stein', 'sarasa', 'amaz', 'lavro')
LINHA_VOLTAR = '<script defer src="../modulos/ms-voltar.js"></script>\n'
LIMITE_BASE64 = 8 * 1024 * 1024          # medido JÁ EM BASE64 (o que pesa no HTML); acima disto: arquivo ao lado

# tabela do DECK-MONTAR: (largura máxima, qualidade JPEG). None = resolução nativa.
RESIZE = {'cheia': (2200, 80), 'duo': (1800, 82), 'prancha': (1800, 82), 'desenho': (None, 88),
          'fundo': (640, 80), 'padrao': (1800, 82)}


def falha(msg, cod=1):
    print(f'montar: ERRO — {msg}', file=sys.stderr)
    sys.exit(cod)


# ── trechos e marcadores ────────────────────────────────────────────────────
RX_TRECHO = re.compile(r'(?:/\*|<!--)\s*TRECHO:(\w+)\s*(?:\*/|-->)(.*?)(?:/\*|<!--)\s*/TRECHO\s*(?:\*/|-->)', re.S)
EM_PRE = {'constantes', 'abertura', 'contracapa', 'capa_imgs'}   # vivem em <pre>: vêm com &lt; &amp; …


def trechos_do_bloco(txt):
    t = {}
    for nome, corpo in RX_TRECHO.findall(txt):
        corpo = corpo.strip('\n')
        if nome in EM_PRE:
            corpo = html.unescape(corpo)
        t[nome] = corpo
    for obrig in ('fontes', 'root', 'constantes', 'abertura', 'contracapa'):
        if obrig not in t:
            falha(f'bloco da marca sem o trecho TRECHO:{obrig}')
    return t


def colar(esq, nome, conteudo):
    """substitui o que está entre `/* COLAR:nome */` e o `/* /COLAR */` seguinte."""
    ab = f'/* COLAR:{nome} */\n'
    i = esq.find(ab)
    if i < 0:
        falha(f'esqueleto sem o marcador COLAR:{nome}')
    j = esq.find('\n/* /COLAR */', i)
    if j < 0:
        falha(f'esqueleto: COLAR:{nome} sem /COLAR')
    return esq[:i + len(ab)] + conteudo + esq[j:]


def inserir_apos(esq, nome, conteudo):
    """cola logo depois de um marcador sem fechamento (as fontes)."""
    ab = f'/* COLAR:{nome} */\n'
    i = esq.find(ab)
    if i < 0:
        falha(f'esqueleto sem o marcador COLAR:{nome}')
    return esq[:i + len(ab)] + conteudo + '\n' + esq[i + len(ab):]


# ── JSON → literal JS ───────────────────────────────────────────────────────
def js(v):
    s = json.dumps(v, ensure_ascii=False, indent=None, separators=(',', ':'))
    # `</script` dentro de string fecharia o <script>; U+2028/9 quebram string JS
    return s.replace('</', '<\\/').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')


def gabaritos_do_esqueleto(esq):
    """lista de gabaritos e tabela EXIGE, lidas do tpl() — o código é a fonte."""
    m = re.search(r'function tpl\(s\)\{.*?\n\}\n', esq, re.S)
    if not m:
        falha('não achei function tpl(s) no esqueleto')
    conhecidos = set(re.findall(r"s\.g==='([\w-]+)'", m.group(0)))
    ex = re.search(r'const EXIGE=\{(.*?)\};', esq, re.S)
    exige = {}
    if ex:
        for g, campos in re.findall(r"'?([\w-]+)'?:\[([^\]]*)\]", ex.group(1)):
            exige[g] = re.findall(r"'([^']+)'", campos)
    conhecidos |= set(exige)
    return conhecidos, exige, m.group(0)


# ── imagens ─────────────────────────────────────────────────────────────────
def eh_arquivo(v):
    return isinstance(v, str) and v and not v.startswith(('http://', 'https://', 'data:', '../', '/'))


def tem_alfa(caminho):
    """Imagem com transparência não pode virar JPEG: o fundo vira preto.
    Desenho de traço e ortofoto recortada chegam assim de propósito — é o
    slide que põe o campo, não o arquivo (regra do Michel, 10/09/2026)."""
    from PIL import Image
    try:
        with Image.open(caminho) as im:
            return im.mode in ('RGBA', 'LA', 'PA') or 'transparency' in im.info
    except Exception:
        return False
    finally:
        if hasattr(caminho, 'seek'):
            caminho.seek(0)


def redimensiona(caminho, largura, q, fmt='JPEG'):
    from PIL import Image, ImageOps
    im = Image.open(caminho)
    im = ImageOps.exif_transpose(im)
    if fmt == 'JPEG' and im.mode not in ('RGB', 'L'):
        im = im.convert('RGB')
    if fmt == 'WEBP' and im.mode not in ('RGB', 'RGBA'):
        im = im.convert('RGBA' if im.mode in ('LA', 'PA') else 'RGB')
    if largura and im.width > largura:
        im = im.resize((largura, round(im.height * largura / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    if fmt == 'JPEG':
        im.save(b, 'JPEG', quality=q, optimize=True, progressive=True)
    else:
        im.save(b, 'WEBP', quality=q, method=6)
    return b.getvalue()


def coleta_imagens(deck, capa_imgs, div_imgs):
    """devolve a lista de trabalhos: (container, chave, valor, perfil). O valor só é trocado depois,
    quando se sabe o total e portanto o modo (base64 ou arquivo ao lado)."""
    jobs = []

    def add(cont, chave, perfil):
        v = cont[chave] if isinstance(cont, dict) else cont[chave]
        if eh_arquivo(v):
            jobs.append((cont, chave, v, perfil))

    for s in deck:
        g = s.get('g', '')
        perfil = 'desenho' if s.get('tipo') == 'desenho' else (g if g in RESIZE else 'padrao')
        # ⚑ `viva` NAO e imagem: o `src` dele e o arquivo vizinho que o slide
        #   abre num quadro (planta-interativa.html). Passar pelo moinho de
        #   imagem seria erro de leitura de arquivo, e o arquivo nem esta na
        #   pasta de imagens — ele ja mora ao lado da apresentacao.
        if 'src' in s and g != 'viva':
            add(s, 'src', perfil)
        # gabarito `logo`: o lockup preserva alfa (perfil desenho, sem redimensionar
        # para baixo); o fundo parado e' imagem de tela cheia
        # ⚑ `.svg` NAO passa pelo moinho: rasterizar mataria o unico motivo de
        #   ele existir, que e' ter caminho para desenhar. Ver inline_svg().
        if 'marca' in s and not str(s.get('marca','')).lower().endswith('.svg'):
            add(s, 'marca', 'desenho')
        if isinstance(s.get('selo'), str):
            add(s, 'selo', 'desenho')
        if 'fundo' in s and isinstance(s.get('fundo'), str):
            add(s, 'fundo', 'cheia')
        for f in s.get('figs') or []:
            if isinstance(f, list) and len(f) > 1:
                add(f, 1, perfil)
        # `imgs`: lista simples de caminhos. Hoje e o carrossel; qualquer
        # gabarito novo que precise de uma pilha de imagens ganha o campo de graca
        for i in range(len(s.get('imgs') or [])):
            add(s['imgs'], i, perfil)
        for it in s.get('items') or []:
            if isinstance(it, dict):
                if 'src' in it:
                    add(it, 'src', perfil)
                for p in it.get('pilha') or []:
                    if isinstance(p, dict) and 'src' in p:
                        add(p, 'src', perfil)
        for r in s.get('res') or []:
            if isinstance(r, dict) and 'src' in r:
                add(r, 'src', perfil)
        # ⚑ GAVETA: o `src` mora um nivel abaixo, dentro de um objeto proprio
        #   (hoje `tulha`, no earth-3d). Sem esta linha o arquivo nao entra no
        #   moinho NEM na pasta, e o html referencia um nome que nao existe —
        #   404 mudo, que so o validador pega.
        for cx in (s.get('tulha'),):
            if isinstance(cx, dict) and 'src' in cx:
                add(cx, 'src', 'desenho')
        if g == 'fotos':
            for it in s.get('itens') or []:
                if isinstance(it, list) and len(it) > 2:
                    add(it, 2, perfil)
    for lst in (capa_imgs, div_imgs):
        for i in range(len(lst)):
            # a capa vem do módulo já em data-URI: entra no mesmo moinho, para
            # não embutir imagem de tela cheia onde o perfil `fundo` basta
            if isinstance(lst[i], str) and lst[i].startswith('data:image/'):
                jobs.append((lst, i, lst[i], 'fundo'))
            else:
                add(lst, i, 'fundo')
    return jobs


TETO_VIDEO = 3 * 1024 * 1024          # bytes do arquivo, antes do base64

def pesa_videos(deck, pasta):
    """Quanto o `vsrc` pesaria em base64 — so para a decisao de modo.

    Nao abre nem decodifica nada: e' o tamanho do arquivo mais os 33% do
    base64. Roda ANTES de processa_imagens porque e' ela quem escolhe entre
    embutir tudo e escrever ao lado, e video e' peso como qualquer outro.
    """
    tot = 0
    for s in deck:
        v = s.get('vsrc')
        if v is None:
            continue
        for item in ([v] if isinstance(v, str) else list(v)):
            if not eh_arquivo(item):
                continue
            arq = pasta / item
            if arq.is_file():
                tot += (arq.stat().st_size + 2) // 3 * 4
    return tot


def coloca_videos(deck, pasta, modo, saida, avisos):
    """Poe o mp4 do campo `vsrc` na peca — data-URI, ou arquivo ao lado.

    16/09/2026: o video passou a seguir o MODO decidido por processa_imagens.
    Em `arquivo` ele vai para `img/` junto com as imagens: nao infla 33%, nao
    tem teto, e a pasta ja era obrigatoria. Em `base64` tudo segue como era,
    teto incluso.

    Video nao passa pelo moinho de imagem: nao ha o que redimensionar aqui, e
    recomprimir video e trabalho de ffmpeg, fora do montar. O que o montar faz
    e recusar arquivo grande demais - base64 infla ~33%, e uma peca que passa
    dos 8 MB deixa de abrir bem no celular do cliente. Comprimir ANTES:

        ffmpeg -i entrada.mp4 -an -vf scale=1600:-2 -c:v libx264 -crf 28 \
               -preset slow -movflags +faststart -pix_fmt yuv420p saida.mp4

    `-an` nao e detalhe: o gabarito toca mudo de qualquer jeito (autoplay so
    passa mudo), entao a trilha seria peso morto no arquivo.

    DOIS FORMATOS, e nao e excesso de zelo: `vsrc` aceita uma lista, e o certo
    e mandar MP4/H.264 **e** WebM/VP9. H.264 e o unico que o Safari do iPad
    toca; VP9 e o unico que um Chromium sem codec proprietario toca - e e
    exatamente esse o navegador do container, o que significa que so com o
    WebM o slide de video da para CONFERIR aqui antes de ir ao cliente. O
    <video> escolhe sozinho a primeira fonte que sabe tocar.

        ffmpeg -i entrada.mp4 -an -vf scale=1600:-2 -c:v libvpx-vp9 -crf 36 \
               -b:v 0 -row-mt 1 -speed 2 saida.webm
    """
    n = 0
    bytes_tot = 0
    usados = set()
    if modo == 'arquivo':
        (saida / 'img').mkdir(parents=True, exist_ok=True)
    for s in deck:
        v = s.get('vsrc')
        if v is None:
            continue
        # uma string ou uma lista: MP4 primeiro, WebM depois. Os dois formatos
        # existem porque nenhum cobre tudo sozinho — ver o comentario acima.
        lista = [v] if isinstance(v, str) else list(v)
        saiu = []
        for item in lista:
            if not eh_arquivo(item):
                saiu.append(item)        # ja e data-URI ou URL: passa reto
                continue
            arq = pasta / item
            if not arq.is_file():
                avisos.append(f'video nao encontrado em {pasta}: {item} — conferir o nome ou passar --img')
                continue
            dados = arq.read_bytes()
            if modo == 'arquivo':
                nome, k = arq.name, 1
                while nome in usados:
                    k += 1
                    nome = f'{arq.stem}-{k}{arq.suffix}'
                usados.add(nome)
                (saida / 'img' / nome).write_bytes(dados)
                saiu.append('img/' + nome)
                n += 1
                bytes_tot += len(dados)
                continue
            if len(dados) > TETO_VIDEO:
                avisos.append(f'video {item} tem {len(dados)/1048576:.1f} MB — acima do teto de '
                              f'{TETO_VIDEO/1048576:.0f} MB para peca embutida. Comprimir antes '
                              f'(ver coloca_videos no montar.py)')
                continue
            mime = 'video/mp4' if arq.suffix.lower() in ('.mp4', '.m4v') else 'video/webm'
            saiu.append(f'data:{mime};base64,' + base64.b64encode(dados).decode())
            n += 1
            bytes_tot += len(dados)
        if saiu:
            s['vsrc'] = saiu
        else:
            s.pop('vsrc', None)          # sem o campo o gabarito mostra o slot, e nao um 404
    return n, bytes_tot


def inline_svg(deck, pasta, avisos):
    """Poe o conteudo de um `marca: x.svg` dentro da peca, como markup.

    POR QUE (16/09/2026). O Michel pediu a marca DESENHADA e depois
    preenchida, como na AMAZ e na Lavro. Contorno animado exige caminho, e
    caminho exige vetor: um PNG nao tem o que desenhar. Entao quando `marca`
    aponta para `.svg`, o arquivo entra inteiro no HTML — e nao como `<img>`,
    porque dentro de `<img>` o CSS da peca nao alcanca os `<path>`.

    O que sai daqui e' markup confiado: o arquivo e do acervo, gerado por
    nos. Mesmo assim tira-se o cabecalho XML e qualquer `<script>`, que num
    SVG inline executaria de verdade.
    """
    n = 0
    for s in deck:
        v = s.get('marca')
        if not isinstance(v, str) or not v.lower().endswith('.svg'):
            continue
        arq = pasta / v
        if not arq.is_file():
            avisos.append(f'svg de marca nao encontrado em {pasta}: {v}')
            s.pop('marca', None)
            continue
        m = arq.read_text(encoding='utf-8')
        m = re.sub(r'<\?xml[^>]*\?>', '', m)
        m = re.sub(r'<!DOCTYPE[^>]*>', '', m)
        m = re.sub(r'(?is)<script.*?</script>', '', m)
        if '<script' in m.lower() or 'onload' in m.lower():
            falha(f'svg de marca {v} tem script — recusado')
        s['marcasvg'] = m.strip()
        s.pop('marca', None)
        n += 1
    return n


VAR_TEMA = re.compile(r'^--[a-z0-9][a-z0-9-]{0,30}$')
HEX_TEMA = re.compile(r'^#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$')
# 16/09/2026: alem de cor, o tema passa a aceitar NUMERO PURO — `--m-veu: .55`
# regula a carga do veu do gabarito `logo` num valor so. Sem unidade e sem
# funcao: numero entre 0 e 4, que e' o que `calc(90% * var(--m-veu))` espera.
NUM_TEMA = re.compile(r'^(?:[0-3](?:\.[0-9]{1,3})?|4|\.[0-9]{1,3})$')


def bloco_tema(tema, avisos):
    """Escreve o `tema` do deck.json como variaveis CSS no :root da peca.

    POR QUE EXISTE (16/09/2026). O Michel quis uma secao com identidade
    propria - o Museu do Cafe - sem refazer a peca inteira: *"eu nao quero
    fazer um rebranding da apresentacao inteira, mas eu quero ter uma secao
    especial, com uma identidade especial para o museu"*. Sub-marca dentro de
    uma peca e caso recorrente: um projeto tem a marca do escritorio e a marca
    do que se projeta.

    O caminho obvio - cor solta no slide - esbarra no validador, e com razao:
    o check `hex` barra `#RRGGBB` fora do `:root` justamente para ninguem
    pintar cor a mao no meio do deck. Entao a cor entra por onde o sistema ja
    aceita: declarada uma vez, no topo, com nome.

    Chave = nome de variavel CSS (`--m-campo`); valor = hex. Nada alem disso
    passa - o que entra na peca e conferido aqui, nao confiado ao autor.
    """
    if not tema:
        return ''
    linhas = []
    for k, v in tema.items():
        if not VAR_TEMA.match(str(k)):
            avisos.append(f'tema: chave "{k}" ignorada — use nome de variavel CSS, ex. --m-campo')
            continue
        if not (HEX_TEMA.match(str(v)) or NUM_TEMA.match(str(v))):
            avisos.append(f'tema: valor "{v}" de "{k}" ignorado — so hex (#RGB, #RRGGBB, '
                          f'#RRGGBBAA) ou numero puro de 0 a 4')
            continue
        linhas.append(f'  {k}:{v};')
    if not linhas:
        return ''
    return ('<style>\n/* tema da peca — sub-marca declarada no deck.json */\n'
            ':root{\n' + '\n'.join(linhas) + '\n}\n</style>\n')


def capa_do_modulo(raiz, marca):
    """As imagens da capa saem do MÓDULO DE CAPA DA FRENTE — ele é o template.

    Nenhuma peça escolhe imagem de capa, e nenhuma frente precisa declarar
    acervo: `modulos/capa-morph-<marca>.html` (ou `capa-morph.html`, o da
    michel stein_) já traz as imagens embutidas, e é de lá que elas vêm.
    Frente nova = módulo de capa novo, e o resto anda sozinho.
    → (lista de data-URI, nome do módulo)"""
    for nome in (f'capa-morph-{marca}.html', 'capa-morph.html'):
        p = raiz / 'modulos' / nome
        if not p.is_file():
            continue
        txt = p.read_text(encoding='utf-8')
        # duas formas no acervo: `const IMGS = [...]` e o array literal
        # passado direto em `MSFundo.montar(canvas, [...])`
        m = (re.search(r'const\s+IMGS\s*=\s*\[(.*?)\]\s*;', txt, re.S)
             or re.search(r'\.montar\(\s*[^,]+,\s*\[(.*?)\]', txt, re.S))
        if m:
            uris = re.findall(r'''['"](data:image/[^'"]+)['"]''', m.group(1))
            if uris:
                return uris, nome
    return [], None


def copia_anexos(dj, pasta_img, saida, modo, avisos):
    """Copia para `img/` a midia que NENHUM slide usa.

    ⚑ Por que isto existe. A pasta `img/` e' saida do `montar`, que so copia
    o que algum slide referencia. Mas a peca vizinha do gabarito `viva` — a
    planta interativa — tem pinos que apontam para `img/...` por caminho
    relativo, escrito a mao. Enquanto o mesmo render estava num slide E num
    pino, os dois viviam do mesmo arquivo e ninguem reparava. No dia em que o
    slide sai do deck, o arquivo para de ser copiado e o pino vira 404 — sem
    erro em lugar nenhum, porque o validador olha a apresentacao e nao a peca
    ao lado. Pago em 18/09/2026, ao enxugar 16 slides duplicados.

    O campo `anexos` no deck.json resolve declarando a dependencia:

        "anexos": ["adm-porta.png", "sala-jantar.mp4", ...]

    Passam PELO MOINHO quando sao imagem, com o perfil `cheia` — e' o mesmo
    render que o pino abre em tela cheia. Video passa reto, ja vem comprimido.
    So faz sentido em modo `arquivo`; em base64 nao ha pasta para preencher.
    """
    nomes = dj.get('anexos') or []
    if not nomes:
        return 0, 0
    if modo != 'arquivo':
        avisos.append(f'{len(nomes)} anexo(s) declarados, mas a peca saiu em base64 '
                      f'(sem pasta img/) — a peca vizinha nao vai achar a midia')
        return 0, 0
    (saida / 'img').mkdir(parents=True, exist_ok=True)
    n = bytes_tot = 0
    for nome in nomes:
        arq = pasta_img / nome
        if not arq.is_file():
            avisos.append(f'anexo nao encontrado em {pasta_img}: {nome}')
            continue
        ext = arq.suffix.lower()
        if ext in ('.mp4', '.m4v', '.webm'):
            dados, destino = arq.read_bytes(), arq.name
        else:
            larg, q = RESIZE['cheia']
            fmt = 'WEBP' if tem_alfa(arq) else 'JPEG'
            dados = redimensiona(arq, larg, q, fmt)
            destino = arq.stem + ('.webp' if fmt == 'WEBP' else '.jpg')
        (saida / 'img' / destino).write_bytes(dados)
        n += 1; bytes_tot += len(dados)
    return n, bytes_tot


def processa_imagens(jobs, pasta_img, saida, peso_vid=0):
    """→ (bytes em base64, modo, imagens que faltaram)

    `peso_vid` entra SO na escolha do modo: o que decide entre embutir e
    escrever ao lado e' o peso do HTML final, e video pesa nele igual.
    """
    if not jobs:
        return 0, ('arquivo' if peso_vid > LIMITE_BASE64 else 'nenhuma'), []
    try:
        import PIL  # noqa
    except ImportError:
        falha('Pillow não instalado (pip install pillow) — necessário para as imagens')
    cache, total, faltam = {}, 0, []
    for cont, chave, v, perfil in jobs:
        if (v, perfil) in cache:
            continue
        larg, q = RESIZE[perfil]
        if v.startswith('data:image/'):
            arq = io.BytesIO(base64.b64decode(v.split(',', 1)[1]))
        else:
            arq = pasta_img / v
            if not arq.is_file():
                faltam.append(v); cache[(v, perfil)] = None; continue
        # transparência sobrevive: WEBP. Sem ela, JPEG, que é mais leve.
        fmt = 'WEBP' if (perfil == 'fundo' or tem_alfa(arq)) else 'JPEG'
        dados = redimensiona(arq, larg, q, fmt)
        cache[(v, perfil)] = (dados, fmt)
        total += (len(dados) + 2) // 3 * 4      # o que a imagem vai pesar em base64
    modo = 'base64' if total + peso_vid <= LIMITE_BASE64 else 'arquivo'
    nomes, usados = {}, set()
    if modo == 'arquivo':
        (saida / 'img').mkdir(parents=True, exist_ok=True)
    for cont, chave, v, perfil in jobs:
        r = cache.get((v, perfil))
        if r is None:
            continue
        dados, fmt = r
        if modo == 'base64':
            mime = 'image/webp' if fmt == 'WEBP' else 'image/jpeg'
            cont[chave] = f'data:{mime};base64,' + base64.b64encode(dados).decode('ascii')
        else:
            if (v, perfil) not in nomes:
                base = pathlib.Path(v).stem
                ext = '.webp' if fmt == 'WEBP' else '.jpg'
                nome, n = base + ext, 1
                while nome in usados:
                    n += 1; nome = f'{base}-{n}{ext}'
                usados.add(nome); nomes[(v, perfil)] = nome
                (saida / 'img' / nome).write_bytes(dados)
            cont[chave] = 'img/' + nomes[(v, perfil)]
    return total, modo, faltam


# ── deck ────────────────────────────────────────────────────────────────────
def monta_deck(dj, trechos, marca):
    miolo = dj.get('deck')
    if not isinstance(miolo, list) or not miolo:
        falha('deck.json sem o array "deck"')
    for i, s in enumerate(miolo):
        if not isinstance(s, dict) or not s.get('g'):
            falha(f'slide {i} sem campo "g"')
        if s['g'] == 'capa':
            # a capa herda o topo do JSON quando não traz o seu
            s.setdefault('capa', 1); s.setdefault('esc', 1)
            if 't' not in s and dj.get('titulo'): s['t'] = dj['titulo']
            if 'sub' not in s and dj.get('sub'): s['sub'] = dj['sub']
            if 'metas' not in s and dj.get('metas'): s['metas'] = dj['metas']
            if 'kick' not in s and dj.get('kick'): s['kick'] = dj['kick']
    def fecha(texto, virgula):
        """normaliza o fim de um trecho do bloco: `}` ou `},` ou `},  /* nota */` — a vírgula fica
        ANTES do comentário. Vírgula dupla abre um buraco no array, que forEach/map pulam em silêncio."""
        m = re.match(r'(?s)^(.*?)\s*,?\s*(/\*.*?\*/)?\s*$', texto.strip())
        corpo, com = m.group(1), m.group(2) or ''
        return corpo + (',' if virgula else '') + ((' ' + com) if com else '')
    partes = [f'/* ══ ABERTURA ══ do bloco marca/{marca}/bloco.html — não se edita aqui */']
    tem_ab = miolo[0]['g'] == 'marca'
    tem_cc = len(miolo) > 1 and miolo[-1]['g'] == 'marca' and miolo[-1].get('fim_', miolo[-1].get('fim'))
    if not tem_ab:
        partes.append(fecha(trechos['abertura'], True))
    partes.append('/* ══ MIOLO ══ gerado de deck.json por sistemas/montar.py */')
    for s in miolo:
        partes.append(js(s) + ',')
    if not tem_cc:
        partes.append(f'/* ══ CONTRACAPA ══ do bloco marca/{marca}/bloco.html */')
        partes.append(fecha(trechos['contracapa'], False))
    else:
        partes[-1] = partes[-1].rstrip(',')
    total = len(miolo) + (0 if tem_ab else 1) + (0 if tem_cc else 1)
    return 'const DECK=[\n' + '\n'.join(partes) + '\n];', total


# ── verificação em Node ─────────────────────────────────────────────────────
def node_check(html_txt):
    scripts = re.findall(r'<script>(.*?)</script>', html_txt, re.S)
    for i, s in enumerate(scripts):
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(s); nome = f.name
        r = subprocess.run(['node', '--check', nome], capture_output=True, text=True)
        os.unlink(nome)
        if r.returncode:
            falha(f'sintaxe no <script> #{i + 1}:\n{r.stderr.strip()[:1200]}')
    return scripts


STUB = """
const document={getElementById:()=>null,createElement:()=>({style:{},remove(){}}),
  body:{appendChild(){},classList:{toggle(){},add(){},remove(){},contains(){return false}}},
  querySelector:()=>null,querySelectorAll:()=>[]};
const window=globalThis; const location={search:'',hash:''};
const console_={error:()=>{},warn:()=>{},log:console.log};
"""
LACO = """
const _p=[];
for(let i=0;i<DECK.length;i++){const s=DECK[i];
  if(!s||typeof s!=='object'){_p.push(i+' —: posição vazia no array DECK (vírgula dupla?)');continue}
  let h;try{h=tpl(s)}catch(e){_p.push(i+' '+s.g+': quebrou — '+e.message);continue}
  const txt=String(h||'').replace(/<[^>]+>/g,'');
  if(!txt.trim()&&!/<(img|svg|iframe|canvas)/.test(h||''))_p.push(i+' '+s.g+': slide vazio');
  else if(/gabarito desconhecido|: falta |cols(<\\/code>)? sem/.test(txt))_p.push(i+' '+s.g+': '+txt.trim().slice(0,140));
  else if(/(^|[^\\w])(undefined|NaN)([^\\w]|$)/.test(txt))_p.push(i+' '+s.g+': escreve undefined/NaN');}
process.stdout.write('\\n@@'+JSON.stringify(_p));
"""


def laco_tpl(scripts):
    """roda tpl() em cada slide, num Node sem DOM. Devolve a lista de problemas, ou None se não deu para rodar."""
    src = next((s for s in scripts if 'function tpl(s){' in s), None)
    if src is None:
        return None
    corte = src.find('\nDECK.forEach(s=>{if(s.fim&&s.fim_==null)')
    if corte < 0:
        return None
    prog = STUB + src[:corte].replace('console.error(', 'console_.error(').replace('console.warn(', 'console_.warn(') + LACO
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(prog); nome = f.name
    r = subprocess.run(['node', nome], capture_output=True, text=True, timeout=60)
    os.unlink(nome)
    if r.returncode:
        return [f'o laço tpl() não rodou: {r.stderr.strip()[:600]}']
    try:
        return json.loads(r.stdout.rsplit('\n@@', 1)[1])
    except Exception:
        return [f'saída inesperada do laço: {r.stdout[-300:]}']


# ── principal ───────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('slug')
    ap.add_argument('--marca', required=True, choices=MARCAS)
    ap.add_argument('--deck', required=True, help='caminho do deck.json')
    ap.add_argument('--img', help='pasta das imagens (padrão: a pasta do deck.json)')
    ap.add_argument('--cliente', action='store_true', help='peça de cliente: sem ms-voltar.js; vai para o site, não para o acervo público')
    ap.add_argument('--sobrescrever', action='store_true', help='substitui <slug>/apresentacao.html existente')
    ap.add_argument('--raiz', default=str(RAIZ), help='raiz do clone (padrão: a pasta acima de sistemas/)')
    a = ap.parse_args()

    raiz = pathlib.Path(a.raiz)
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', a.slug):
        falha('slug: só minúsculas, dígitos e hífen (ex.: casa-exemplo)')
    saida = raiz / a.slug
    alvo = saida / 'apresentacao.html'
    if alvo.exists() and not a.sobrescrever:
        falha(f'{alvo.relative_to(raiz)} já existe. Versão em desenvolvimento substitui: rode de novo com --sobrescrever', 2)

    deck_path = pathlib.Path(a.deck)
    if not deck_path.is_file():
        falha(f'deck.json não encontrado: {deck_path}')
    try:
        dj = json.loads(deck_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        falha(f'deck.json inválido: {e}')
    if not dj.get('projeto'):
        falha('deck.json sem "projeto"')
    if not isinstance(dj.get('deck'), list) or not dj['deck']:
        falha('deck.json sem o array "deck" (o miolo, sem abertura/contracapa)')
    pasta_img = pathlib.Path(a.img) if a.img else deck_path.parent

    esq_path = raiz / 'esqueleto' / 'deck-esqueleto.html'
    bloco_path = raiz / 'marca' / a.marca / 'bloco.html'
    esq = esq_path.read_text(encoding='utf-8')
    trechos = trechos_do_bloco(bloco_path.read_text(encoding='utf-8'))
    conhecidos, exige, _ = gabaritos_do_esqueleto(esq)

    # ── pré-checagem do deck.json (a mesma que o tpl() faz, só que antes) ──
    avisos, marcados = [], set()
    for i, s in enumerate(dj['deck']):
        if not isinstance(s, dict) or not s.get('g'):
            falha(f'slide {i} não é objeto com campo "g"')
        g = s['g']
        if g not in conhecidos:
            avisos.append(f'slide {i} · gabarito desconhecido: {g}'); marcados.add(i)
        for c in exige.get(g, []):
            if s.get(c) is None:
                avisos.append(f'slide {i} · gabarito {g}: falta {c}'); marcados.add(i)

    # ── imagens: redimensiona e decide o modo ──
    # ── a capa da frente, sem ninguém escolher nada ──
    # Ordem: o deck.json só se quiser TROCAR o acervo (raro); depois o
    # TRECHO:capa_imgs do bloco, que existe para a frente servir as mesmas
    # imagens por caminho relativo em vez de embutir; e, por último e por
    # padrão, o MÓDULO DE CAPA da frente, que é o template.
    capa_imgs, capa_fonte = dj.get('capa_imgs'), 'deck.json'
    if capa_imgs is None:
        ci = trechos.get('capa_imgs') or ''
        m = re.search(r'\[(.*)\]', ci, re.S)
        if m:
            capa_imgs = re.findall(r'''['"]([^'"]+)['"]''', m.group(1))
            capa_fonte = 'bloco da marca'
    if capa_imgs is None:
        capa_imgs, mod = capa_do_modulo(raiz, a.marca)
        capa_fonte = f'modulos/{mod}' if mod else 'nenhuma'
    capa_imgs_js = None
    div_imgs = list(dj.get('div_imgs') or [])
    n_svg = inline_svg(dj['deck'], pasta_img, avisos)
    jobs = coleta_imagens(dj['deck'], capa_imgs, div_imgs)
    saida.mkdir(parents=True, exist_ok=True)
    if a.sobrescrever and (saida / 'img').is_dir():
        shutil.rmtree(saida / 'img')          # img/ é saída do montar: a rodada nova decide o que fica
    # ⚑ a ordem importa: processa_imagens é quem escolhe o modo, e o vídeo
    #   segue esse modo. Por isso o peso do vídeo entra antes, e a gravação
    #   do vídeo vem depois — e depois do rmtree, ou seria apagado.
    total_img, modo, faltam = processa_imagens(jobs, pasta_img, saida,
                                               pesa_videos(dj['deck'], pasta_img))
    n_vid, bytes_vid = coloca_videos(dj['deck'], pasta_img, modo, saida, avisos)
    n_anx, bytes_anx = copia_anexos(dj, pasta_img, saida, modo, avisos)
    if n_anx:
        print(f'montar: anexos — {n_anx} arquivo(s), {bytes_anx/1048576:.2f} MB em img/, '
              f'so para a peca vizinha (nenhum slide usa)')
    if n_svg:
        print(f'montar: marca — {n_svg} svg inline (caminho vivo, para animar)')
    if n_vid:
        onde = 'ao lado, em img/' if modo == 'arquivo' else 'em base64'
        print(f'montar: video — {n_vid} arquivo(s), {bytes_vid/1048576:.2f} MB {onde}')
    for v in faltam:
        avisos.append(f'imagem não encontrada em {pasta_img}: {v} — conferir o nome ou passar --img')
    if capa_imgs_js is None:
        capa_imgs_js = js(capa_imgs)

    # ── monta ──
    deck_js, n_slides = monta_deck(dj, trechos, a.marca)
    esq = inserir_apos(esq, 'fontes', trechos['fontes'])
    esq = colar(esq, 'root', trechos['root'])
    esq = colar(esq, 'constantes', trechos['constantes'])
    esq = colar(esq, 'deck', deck_js)
    esq = colar(esq, 'capa_imgs', f'const CAPA_IMGS={capa_imgs_js};')
    esq = colar(esq, 'div_imgs', f'const DIV_IMGS={js(div_imgs)};')
    if dj.get('map'):
        esq = colar(esq, 'map', f'const MAP = {js(dj["map"])};')
    bt = bloco_tema(dj.get('tema'), avisos)
    if bt:
        if '</head>' not in esq:
            falha('esqueleto sem </head> — nao sei onde por o tema')
        esq = esq.replace('</head>', bt + '</head>', 1)
    titulo = html.escape(re.sub(r'<[^>]+>', ' ', dj.get('titulo') or dj['projeto']).strip())
    esq = re.sub(r'<title>.*?</title>', f'<title>{titulo}</title>', esq, count=1, flags=re.S)
    # ── o rodape de todo slide ──────────────────────────────────────────
    # ⚑ `projeto · cliente` era texto fixo no esqueleto e NUNCA foi trocado:
    #   todo deck desta casa foi ao cliente com o placeholder no pe. Agora
    #   vem do `pe` do deck.json e, na falta dele, do nome do projeto — o
    #   placeholder nao volta a ser publicado por esquecimento.
    pe = (dj.get('pe') or '').strip() \
        or re.sub(r'<[^>]+>', ' ', dj.get('projeto') or '').strip().lower()
    if pe:
        esq = re.sub(r'(<span class="pj">).*?(</span>)',
                     lambda m: m.group(1) + html.escape(pe) + m.group(2),
                     esq, count=1, flags=re.S)
    # ── a chave da Maps: por caminho aqui dentro, EMBUTIDA lá fora ──
    # `../modulos/ms-maps-chave.js` resolve para peça que mora neste
    # repositório, e é assim que tem de ser: trocar a chave um dia é editar um
    # arquivo, não vinte decks. Na área de cliente, no Netlify, o caminho não
    # existe — o slide 3D morria com "sem chave da Maps Platform", mesmo
    # defeito de classe da capa servida por caminho. Só nesse caso a chave vai
    # embutida. Ela é restrita por referrer: embutir não a expõe mais do que
    # servi-la. (Michel, 10/09/2026.)
    #
    # ⚑ Embutir DENTRO do acervo é erro duplo: duplica a chave e faz a
    # guarda do repositório público barrar o push, com razão. Foi o que
    # aconteceu com os dois esqueletos de 09/09, publicados pela API sem
    # passar pela guarda.
    if a.cliente:
        m_chave = re.search(r'[ \t]*<script src="\.\./modulos/ms-maps-chave\.js"></script>\n?', esq)
        if m_chave:
            p_chave = raiz / 'modulos' / 'ms-maps-chave.js'
            if p_chave.is_file():
                esq = esq.replace(m_chave.group(0),
                                  '<script>\n' + p_chave.read_text(encoding='utf-8') + '\n</script>\n')
            else:
                avisos.append('modulos/ms-maps-chave.js não encontrado — slide 3D vai abrir sem chave')

    if a.cliente:
        if LINHA_VOLTAR not in esq:
            falha('esqueleto sem a linha do ms-voltar.js — não sei o que tirar')
        esq = esq.replace(LINHA_VOLTAR, '')
    elif LINHA_VOLTAR not in esq:
        esq = esq.replace('</body>', LINHA_VOLTAR + '</body>')

    # ── confere e grava ──
    scripts = node_check(esq)
    problemas = laco_tpl(scripts)
    alvo.write_text(esq, encoding='utf-8')
    # peso = a PASTA inteira menos meta.json e anteriores/ — a mesma medida do montar-indice.py;
    # em modo arquivo ao lado é o que quem manda a peça carrega
    peso = sum(f.stat().st_size for f in saida.rglob('*')
               if f.is_file() and f.name != 'meta.json' and 'anteriores' not in f.relative_to(saida).parts) / (1024 * 1024)

    meta_path = saida / 'meta.json'
    hoje = datetime.date.today().strftime('%d.%m.%Y')
    if a.sobrescrever and meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding='utf-8'))
        except Exception:
            meta = {}
        # o que é fato do build muda; nome/projeto/sub editados à mão ficam
        meta.update({'pranchas': n_slides, 'peso': round(peso, 2), 'data': hoje, 'frente': a.marca, 'cliente': bool(a.cliente)})
    else:
        meta = {'projeto': dj['projeto'], 'nome': re.sub(r'<[^>]+>', ' ', dj.get('titulo') or dj['projeto']).strip(),
                'pranchas': n_slides, 'peso': round(peso, 2), 'data': hoje,
                'frente': a.marca, 'cliente': bool(a.cliente)}
        if dj.get('sub'):
            meta['sub'] = dj['sub']
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    # ── relatório ──
    rel = alvo.relative_to(raiz)
    print(f'montar: {rel} — {n_slides} slides (abertura e contracapa inclusas), {peso:.2f} MB na pasta, marca {a.marca}'
          + (', peça de CLIENTE (sem ms-voltar.js)' if a.cliente else ''))
    print(f'montar: imagens — {len(jobs)} referência(s), {total_img / 1024 / 1024:.2f} MB em base64, modo {modo}')
    print(f'montar: capa — {len(capa_imgs)} imagem(ns), de {capa_fonte}')
    if modo == 'arquivo':
        print(f'montar: ⚠ ACIMA DE 8 MB DE IMAGEM → arquivo ao lado em {a.slug}/img/. '
              f'A peça EXIGE A PASTA {a.slug}/ inteira; entrega por LINK, não por anexo.')
    if peso > 8:
        print(f'montar: aviso — a pasta pesa {peso:.2f} MB, acima do limite de anexo de e-mail: entrega por link')
    if any(s.get('g') == 'earth-3d' for s in dj['deck']):
        print('montar: aviso — slide earth-3d: entrega por link; o domínio precisa estar na chave da Maps Platform')
    print(f'montar: meta.json gravado em {meta_path.relative_to(raiz)}')
    if problemas is None:
        print('montar: laço tpl() não rodou aqui — o validar.mjs faz isso no navegador')
    else:
        # o laço numera com a abertura (índice 0); o miolo começa em 1 quando ela vem do bloco
        desloc = 0 if dj['deck'][0].get('g') == 'marca' else 1
        for p in problemas:
            m = re.match(r'(\d+) ', p)
            if m and int(m.group(1)) - desloc in marcados:
                continue
            avisos.append('slide ' + p)
    if avisos:
        print(f'montar: {len(avisos)} problema(s) no deck.json — a peça foi escrita, mas o validar vai barrar:', file=sys.stderr)
        for p in avisos:
            print('  · ' + p, file=sys.stderr)
        print('  formato de cada gabarito: sistemas/DECK-JSON.md', file=sys.stderr)
        sys.exit(3)
    print(f'montar: agora rode  node sistemas/validar.mjs {rel}' + (' --cliente' if a.cliente else ''))


if __name__ == '__main__':
    main()
