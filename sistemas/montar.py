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


def redimensiona(caminho, largura, q, fmt='JPEG'):
    from PIL import Image, ImageOps
    im = Image.open(caminho)
    im = ImageOps.exif_transpose(im)
    if fmt == 'JPEG' and im.mode not in ('RGB', 'L'):
        im = im.convert('RGB')
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
        if 'src' in s:
            add(s, 'src', perfil)
        for f in s.get('figs') or []:
            if isinstance(f, list) and len(f) > 1:
                add(f, 1, perfil)
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
        if g == 'fotos':
            for it in s.get('itens') or []:
                if isinstance(it, list) and len(it) > 2:
                    add(it, 2, perfil)
    for lst in (capa_imgs, div_imgs):
        for i in range(len(lst)):
            add(lst, i, 'fundo')
    return jobs


def processa_imagens(jobs, pasta_img, saida):
    """→ (bytes em base64, modo, imagens que faltaram)"""
    if not jobs:
        return 0, 'nenhuma', []
    try:
        import PIL  # noqa
    except ImportError:
        falha('Pillow não instalado (pip install pillow) — necessário para as imagens')
    cache, total, faltam = {}, 0, []
    for cont, chave, v, perfil in jobs:
        if (v, perfil) in cache:
            continue
        arq = pasta_img / v
        if not arq.is_file():
            faltam.append(v); cache[(v, perfil)] = None; continue
        larg, q = RESIZE[perfil]
        fmt = 'WEBP' if perfil == 'fundo' else 'JPEG'
        dados = redimensiona(arq, larg, q, fmt)
        cache[(v, perfil)] = (dados, fmt)
        total += (len(dados) + 2) // 3 * 4      # o que a imagem vai pesar em base64
    modo = 'base64' if total <= LIMITE_BASE64 else 'arquivo'
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
    capa_imgs = dj.get('capa_imgs')
    if capa_imgs is None:
        ci = trechos.get('capa_imgs')
        m = re.search(r'\[.*\]', ci or '', re.S)
        capa_imgs_js = m.group(0) if m else '[]'
        capa_imgs = []
    else:
        capa_imgs_js = None
    div_imgs = list(dj.get('div_imgs') or [])
    jobs = coleta_imagens(dj['deck'], capa_imgs, div_imgs)
    saida.mkdir(parents=True, exist_ok=True)
    if a.sobrescrever and (saida / 'img').is_dir():
        shutil.rmtree(saida / 'img')          # img/ é saída do montar: a rodada nova decide o que fica
    total_img, modo, faltam = processa_imagens(jobs, pasta_img, saida)
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
    titulo = html.escape(re.sub(r'<[^>]+>', ' ', dj.get('titulo') or dj['projeto']).strip())
    esq = re.sub(r'<title>.*?</title>', f'<title>{titulo}</title>', esq, count=1, flags=re.S)
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
