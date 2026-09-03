#!/usr/bin/env python3
"""montar-indice — gera dados.json, o que o index.html lê.

Uso, na raiz do clone:   python3 sistemas/montar-indice.py            # regrava dados.json
                          python3 sistemas/montar-indice.py --check    # só confere; sai 1 se estiver desatualizado

Fontes, nesta ordem:
  <slug>/meta.json          uma peça publicada. Escrito por sistemas/montar.py ao montar a peça.
                            href é sempre <slug>/apresentacao.html — não se escreve no meta.
  registro/<frente>.json    o que cada frente registra à mão: documentos (aba/grupo/nome/desc/
                            arq|href/ver) e peças fora do padrão (href absoluto, oculto, superado/).
                            Ordem das frentes em ORDEM_FRENTES.

Saída: dados.json na raiz, {"projetos":[…], "docs":[…], "gerado":"<ISO>"}.
  projetos  agrupados pelo campo `projeto` (caixa e acento ignorados), em ordem alfabética;
            dentro do projeto, mais recente em cima pela `data` (DD.MM.AAAA); empate por nome.
  docs      concatenados na ordem de ORDEM_FRENTES (dentro da frente, na ordem do arquivo) e
            depois reordenados de forma ESTÁVEL pela sequência de grupos de ORDEM_GRUPOS: o
            index.html mostra os grupos por primeira aparição, e sem isso a aba marca sairia
            na ordem das frentes, não na ordem decidida. Grupo que não está na tabela vai
            para o fim da aba, na ordem das frentes. Grupo novo: acrescentar em ORDEM_GRUPOS.

Guardas, todas param o build (sai 1):
  - meta com `cliente:true` nunca entra — peça de cliente mora na área de cliente do site.
  - órfã: pasta com apresentacao.html sem meta.json e sem href/ver em registro algum.
  - meta sem os campos obrigatórios, data fora de DD.MM.AAAA, registro com JSON inválido.
Aviso, não para: `peso` do meta divergindo > 5% do que está no disco (pasta inteira, em MiB,
sem meta.json e sem anteriores/). O peso do meta é preservado; o aviso é para atualizar o meta.
"""
import json, pathlib, re, sys
from datetime import datetime, timezone

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REGISTRO = RAIZ / 'registro'
SAIDA = RAIZ / 'dados.json'
ORDEM_FRENTES = ['_geral', 'michel-stein', 'sarasa', 'amaz', 'lavro', 'baraka']
FRENTES = set(ORDEM_FRENTES) - {'_geral'}
# sequência dos grupos em cada aba, como o acervo sempre mostrou. aba None = aba sistema
ORDEM_GRUPOS = {
    'deck':  ['montar', 'gabaritos', 'consulta', 'as peças de montar', 'precisa de uma marca', 'rodadas', 'registro'],
    'marca': ['michel stein_', 'AMAZ', 'Lavrō', 'Sarasá', 'a levantar'],
    None:    ['site', 'operação', 'montar', 'publicação', 'contexto', 'proposta', 'notion',
              'sarasá · banco de referência', 'sarasá · mapeamento de danos', 'levantamento 3D'],
}
# pastas que nunca são peça: não entram no índice nem contam como órfã
IGNORA = {'superado', 'sistemas', 'modulos', 'esqueleto', 'ferramentas', 'registro', 'fundo', 'marca', 'entregas', '.git', '.github'}
OBRIGATORIOS = ('projeto', 'nome', 'pranchas', 'peso', 'data', 'frente')
RX_DATA = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')

erros, avisos = [], []


def carrega_json(p):
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:  # JSON quebrado é erro de build, não de leitura
        erros.append(f'{p.relative_to(RAIZ)}: JSON inválido — {e}')
        return None


def data_chave(d):
    """DD.MM.AAAA → AAAA-MM-DD, para ordenar; data ruim vai para o fim."""
    m = RX_DATA.match(d or '')
    return f'{d[6:10]}-{d[3:5]}-{d[0:2]}' if m else ''


def peso_no_disco(pasta):
    """MiB da pasta inteira, sem meta.json e sem anteriores/ — é o que quem manda por e-mail carrega."""
    total = 0
    for p in pasta.rglob('*'):
        rel = p.relative_to(pasta).as_posix()
        if p.is_file() and rel != 'meta.json' and not rel.startswith('anteriores/'):
            total += p.stat().st_size
    return total / 1024 / 1024


def le_metas():
    pecas = []
    for meta in sorted(RAIZ.glob('*/meta.json')):
        slug = meta.parent.name
        if slug in IGNORA or slug.startswith(('_', '.')):
            continue
        m = carrega_json(meta)
        if m is None:
            continue
        rel = meta.relative_to(RAIZ).as_posix()
        if m.get('cliente') is True:
            # guarda extra: o repositório é público; a peça de cliente não pode nem aparecer listada
            erros.append(f'{rel}: cliente:true — peça de cliente NÃO entra no acervo público (mora em /cliente/ do site)')
            continue
        faltam = [k for k in OBRIGATORIOS if k not in m]
        if faltam:
            erros.append(f'{rel}: faltam campos {faltam}')
            continue
        if not RX_DATA.match(str(m['data'])):
            erros.append(f'{rel}: data "{m["data"]}" fora de DD.MM.AAAA')
        if m['frente'] not in FRENTES:
            erros.append(f'{rel}: frente "{m["frente"]}" desconhecida — vale {sorted(FRENTES)}')
        if not (meta.parent / 'apresentacao.html').exists():
            erros.append(f'{rel}: não existe {slug}/apresentacao.html')
        else:
            disco = peso_no_disco(meta.parent)
            try:
                ref = float(m['peso'])
                if ref > 0 and abs(disco - ref) / ref > 0.05:
                    avisos.append(f'{rel}: peso {ref} MB no meta, {disco:.2f} MB no disco — atualizar o meta')
            except (TypeError, ValueError):
                erros.append(f'{rel}: peso "{m["peso"]}" não é número')
        peca = {'nome': m['nome'], 'pranchas': m['pranchas'], 'peso': m['peso'], 'data': m['data'],
                'href': f'{slug}/apresentacao.html', 'frente': m['frente']}
        for k in ('sub', 'tipo', 'unid', 'oculto'):
            if m.get(k) not in (None, False, ''):
                peca[k] = m[k]
        pecas.append((m['projeto'], peca))
    return pecas


def le_registros():
    """→ (lista de (projeto, peça) manuais, docs na ordem das frentes, hrefs/vers registrados)."""
    pecas, docs, registrados = [], [], set()
    for frente in ORDEM_FRENTES:
        p = REGISTRO / f'{frente}.json'
        if not p.exists():
            continue
        r = carrega_json(p)
        if r is None:
            continue
        rel = p.relative_to(RAIZ).as_posix()
        for proj in r.get('projetos', []):
            for x in proj.get('pecas', []):
                if 'href' not in x or 'nome' not in x:
                    erros.append(f'{rel}: peça de "{proj.get("nome")}" sem nome ou href')
                    continue
                if x.get('data') and not RX_DATA.match(str(x['data'])):
                    erros.append(f'{rel}: data "{x["data"]}" fora de DD.MM.AAAA')
                registrados.add(x['href'].split('?')[0])
                pecas.append((proj.get('nome', ''), dict(x)))
        for d in r.get('docs', []):
            if 'nome' not in d or ('arq' not in d and 'href' not in d):
                erros.append(f'{rel}: doc "{d.get("nome")}" precisa de nome e de arq ou href')
                continue
            if d.get('arq') and not (RAIZ / d['arq']).exists():
                avisos.append(f'{rel}: arq "{d["arq"]}" não existe no disco')
            if d.get('ver'):
                registrados.add(d['ver'].split('?')[0])
            docs.append(d)
    # sem nenhum registro/*.json algo está muito errado: o acervo sairia vazio de documentos
    if not any((REGISTRO / f'{f}.json').exists() for f in ORDEM_FRENTES):
        erros.append('registro/: nenhum <frente>.json encontrado')
    return pecas, docs, registrados


def ordena_docs(docs):
    """Ordenação estável pela posição do grupo na aba; grupo desconhecido fica no fim, na ordem de entrada."""
    def chave(d):
        seq = ORDEM_GRUPOS.get(d.get('aba'), [])
        g = d.get('grupo', 'outros')
        return seq.index(g) if g in seq else len(seq)
    return sorted(docs, key=chave)


def agrupa(pecas):
    """[(projeto, peça)] → [{nome, pecas:[…]}], projetos em ordem alfabética, peças por data desc."""
    por_nome = {}
    for projeto, peca in pecas:
        k = projeto.strip().casefold()
        if k not in por_nome:
            por_nome[k] = {'nome': projeto.strip(), 'pecas': []}
        por_nome[k]['pecas'].append(peca)
    for p in por_nome.values():
        p['pecas'].sort(key=lambda x: (data_chave(x.get('data')), x['nome'].casefold()))
        p['pecas'].sort(key=lambda x: data_chave(x.get('data')), reverse=True)
    return sorted(por_nome.values(), key=lambda p: p['nome'].casefold())


def orfas(registrados):
    """Pasta com apresentacao.html, fora das ignoradas, sem meta.json e sem href/ver em registro."""
    achadas = []
    for html in sorted(RAIZ.glob('*/apresentacao.html')):
        pasta = html.parent
        if pasta.name in IGNORA or pasta.name.startswith(('_', '.')):
            continue
        rel = html.relative_to(RAIZ).as_posix()
        if (pasta / 'meta.json').exists() or rel in registrados:
            continue
        achadas.append(rel)
    return achadas


def monta():
    metas = le_metas()
    manuais, docs, registrados = le_registros()
    for slug_html in orfas(registrados):
        erros.append(f'órfã: {slug_html} — sem meta.json e sem href em registro/*.json. Está no ar e ninguém acha')
    return {'projetos': agrupa(metas + manuais), 'docs': ordena_docs(docs)}


def sem_gerado(d):
    return {k: v for k, v in d.items() if k != 'gerado'}


def main():
    check = '--check' in sys.argv
    dados = monta()
    for a in avisos:
        print('aviso:', a)
    if erros:
        for e in erros:
            print('ERRO:', e)
        print(f'montar-indice: {len(erros)} erro(s) — dados.json NÃO foi gravado')
        return 1
    if check:
        atual = carrega_json(SAIDA) if SAIDA.exists() else None
        if atual is None or sem_gerado(atual) != dados:
            print('montar-indice: dados.json DIVERGE das fontes — rodar sem --check')
            return 1
        print('montar-indice: dados.json em dia')
        return 0
    dados['gerado'] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    SAIDA.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    n = sum(len(p['pecas']) for p in dados['projetos'])
    print(f'montar-indice: dados.json gravado — {len(dados["projetos"])} projetos, {n} peças, {len(dados["docs"])} docs')
    return 0


if __name__ == '__main__':
    sys.exit(main())
