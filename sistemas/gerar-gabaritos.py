#!/usr/bin/env python3
"""gerar-gabaritos — a tabela de gabaritos do DECK-MONTAR.md, extraída do código.

Uso, na raiz do clone:   python3 sistemas/gerar-gabaritos.py            # reescreve a tabela
                          python3 sistemas/gerar-gabaritos.py --check    # só confere; sai 1 se divergir

Lê o `tpl()` de esqueleto/deck-esqueleto.html: cada ramo `if(s.g==='nome')` é um
gabarito; os campos `s.xxx` lidos dentro do ramo são os campos dele; `EXIGE` diz
quais são obrigatórios; a aridade de `itens`/`cards`/`figs` vem da desestruturação
`([a,b,c])=>`. Escreve o resultado entre `<!-- GABARITOS:INICIO -->` e
`<!-- GABARITOS:FIM -->` no sistemas/DECK-MONTAR.md.

A descrição em uma linha de cada gabarito fica em DESCRICAO, aqui — é a única parte
redigida. Gabarito novo no código sem descrição aparece com "—" e o script avisa.
O código é a fonte; a tabela é a conveniência. Nunca editar a tabela à mão.
"""
import pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ESQ = RAIZ / 'esqueleto' / 'deck-esqueleto.html'
DOC = RAIZ / 'sistemas' / 'DECK-MONTAR.md'

DESCRICAO = {
    'marca':       ('estrutura', 'abertura e contracapa. Vêm do bloco da marca, não se inventam'),
    'capa':        ('estrutura', 'nome do projeto, endereço e três metas'),
    'divisor':     ('estrutura', 'abre seção e ganha um ponto no chrome'),
    'sumario':     ('estrutura', 'o argumento inteiro em blocos, logo depois da capa'),
    'fim':         ('estrutura', 'próximos passos. É o que o cliente leva embora'),
    'frase':       ('texto', 'uma ideia por tela, tipo grande'),
    'lista':       ('texto', 'itens numerados, entram por clique'),
    'trio':        ('texto', 'três blocos curtos lado a lado'),
    'jogadas':     ('texto', 'duas ou três jogadas numeradas, com apoio longo'),
    'duasfrentes': ('texto', 'o pacote se fechando; caixa que cresce a cada item'),
    'tabela':      ('dado', 'comparação'),
    'porte':       ('dado', 'tabela de faixas'),
    'unit':        ('dado', 'números-chave com apoio no ponteiro'),
    'avulso':      ('dado', 'preço por frente, dentro e fora do pacote'),
    'players':     ('dado', 'atores do mesmo mercado, em faixas. `casas`, não `cols`'),
    'plug':        ('dado', 'diagrama de encaixe'),
    'duo':         ('imagem', 'duas imagens lado a lado'),
    'fotos':       ('imagem', 'linha do tempo ilustrada'),
    'prancha':     ('imagem', 'grade de 2 a 4 imagens sobre um tema. Retrato 3–4 colunas, deitada 2. `cols` aqui é NÚMERO — ver `gabaritos/prancha-referencia.md`'),
    'cheia':       ('imagem', 'o render em tela cheia. É o padrão para render — ver `gabaritos/render-cheia.md`'),
    'earth-3d':    ('imagem', 'onde o projeto está: o globo do Google Earth, girando devagar. Só por link — `gabaritos/mapa-earth-3d.md`'),
    'modelo-3d':   ('imagem', 'o que o projeto é: o modelo do SketchUp, vivo. Exige modelo PÚBLICO no 3D Warehouse — `gabaritos/modelo.md`'),
    'mapa':        ('imagem', 'o cadastro desenhado, com hover por lote. Exige o objeto `MAP` — `gabaritos/mapa-lotes.md`'),
}
ORDEM_GRUPO = ['estrutura', 'texto', 'dado', 'imagem']
# campos que valem em qualquer gabarito — não entram na coluna "campos próprios"
# campos calculados no preâmbulo do tpl() (antes dos ramos) e usados por um gabarito específico:
# o parser não os vê dentro do ramo, então entram por aqui
SUPLEMENTO = {'capa': ['metas'], 'tabela': ['cols', 'linhas'], 'porte': ['cols', 'linhas'], 'marca': []}
GERAIS = {'g', 'sec', 'kick', 't', 'sub', 'esc', 'terra', 'trama', 'fundo', 'div', 'cel', 'nota', 'sang',
          'fecho', 'pre', 'largo', 'dois', 'fim_', 'fim', 'capa', 'comecar', 'passos', 'tema'}


def ramos(js):
    """devolve {gabarito: trecho de código do ramo} a partir do tpl()"""
    ini = js.index('function tpl(s)')
    fim = js.index('\n}', ini)
    corpo = js[ini:fim]
    pos = [(m.start(), m.group(1)) for m in re.finditer(r"if\(s\.g==='([a-z0-9\-]+)'(?:\|\|s\.g==='([a-z0-9\-]+)')?", corpo)]
    out = {}
    for i, (p, g) in enumerate(pos):
        q = pos[i + 1][0] if i + 1 < len(pos) else len(corpo)
        trecho = corpo[p:q]
        # o ramo acaba onde começa um `const` compartilhado de nível superior (ex.: o `tab`)
        c = re.search(r"\n  const ", trecho)
        if c:
            trecho = trecho[:c.start()]
        m = re.match(r"if\(s\.g==='([a-z0-9\-]+)'\|\|s\.g==='([a-z0-9\-]+)'\)", trecho)
        nomes = [g] + ([m.group(2)] if m else [])
        for n in nomes:
            out[n] = out.get(n, '') + trecho
    # o preâmbulo do tpl (antes do primeiro ramo) lê campos gerais — não conta
    return out


def campos(trecho, g=''):
    cs = set(re.findall(r"\bs\.([a-zA-Z_][a-zA-Z0-9_]*)", trecho)) | set(SUPLEMENTO.get(g, []))
    if g == 'marca':
        cs.discard('metas')
    return sorted(c for c in cs if c not in GERAIS and c != 'g')


def aridade(trecho, campo):
    m = re.search(r"s\." + re.escape(campo) + r"\.map\(\(\[([^\]]*)\]\)", trecho)
    if not m:
        return ''
    n = len([x for x in m.group(1).split(',') if x.strip()])
    return f'{n}'


def exige(js):
    m = re.search(r"const EXIGE=\{(.*?)\};", js, re.S)
    out = {}
    if m:
        for g, lst in re.findall(r"'?([a-z0-9\-]+)'?\s*:\s*\[([^\]]*)\]", m.group(1)):
            out[g] = [x.strip().strip("'") for x in lst.split(',') if x.strip()]
    return out


def gerar():
    html = ESQ.read_text(encoding='utf-8')
    js = '\n'.join(re.findall(r'<script(?![^>]*src)[^>]*>(.*?)</script>', html, re.S))
    rs = ramos(js)
    ex = exige(js)
    faltam_desc = [g for g in rs if g not in DESCRICAO]
    linhas = ['Tabela gerada por `sistemas/gerar-gabaritos.py` a partir do `tpl()` do esqueleto — '
              'não editar à mão; rodar o script. Campos em **negrito** são obrigatórios (`EXIGE`): '
              'sem eles o slide vira aviso. O número entre parênteses é a aridade de cada item '
              '(`itens:[[a,b]]` = 2). Campos gerais (`sec kick t sub esc terra trama fundo div cel nota sang fecho pre largo`) '
              'valem em todo gabarito e não se repetem aqui.', '']
    for grupo in ORDEM_GRUPO:
        gs = [g for g in rs if DESCRICAO.get(g, ('?',))[0] == grupo]
        if grupo == ORDEM_GRUPO[-1]:
            gs += [g for g in rs if g not in DESCRICAO]
        if not gs:
            continue
        linhas += [f'**{grupo.capitalize()}**', '', '| gabarito | o que é | campos próprios |', '|---|---|---|']
        for g in gs:
            desc = DESCRICAO.get(g, ('', '—'))[1]
            cs = []
            for c in campos(rs[g], g):
                a = aridade(rs[g], c)
                cel = f'`{c}`' + (f' ({a})' if a else '')
                if c in ex.get(g, []):
                    cel = f'**{cel}**'
                cs.append(cel)
            linhas.append(f'| `{g}` | {desc} | {" · ".join(cs) or "—"} |')
        linhas.append('')
    return '\n'.join(linhas).rstrip() + '\n', faltam_desc, len(rs)


def main():
    novo, faltam, n = gerar()
    doc = DOC.read_text(encoding='utf-8')
    a, b = '<!-- GABARITOS:INICIO -->', '<!-- GABARITOS:FIM -->'
    if a not in doc or b not in doc:
        print('marcadores GABARITOS não encontrados no DECK-MONTAR.md'); return 2
    i, j = doc.index(a) + len(a), doc.index(b)
    atual = doc[i:j].strip('\n')
    if faltam:
        print('AVISO — gabarito(s) sem descrição em DESCRICAO:', ', '.join(faltam))
    if '--check' in sys.argv:
        if atual == novo.strip('\n'):
            print(f'gabaritos: tabela em dia ({n} gabaritos)'); return 0
        print('gabaritos: tabela DIVERGE do código — rodar sem --check'); return 1
    DOC.write_text(doc[:i] + '\n' + novo + doc[j:], encoding='utf-8')
    print(f'gabaritos: tabela reescrita ({n} gabaritos)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
