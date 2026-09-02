#!/usr/bin/env python3
"""guarda-publico — varre o repositório PÚBLICO antes do push.

Uso, na raiz do clone:   python3 sistemas/guarda-publico.py
Sai com código 1 e lista o que achou. Zero achados imprime "guarda: limpo".

O que procura, e por quê (regra em GITHUB-COMO-TRABALHAR.md, "Público quer dizer aberto"):
  - nome de cliente no campo `metas` de uma peça           → peça de cliente mora em /cliente/ do site
  - URL da área de cliente (michel-stein.netlify.app/cliente) → publicar o link anula a proteção
  - endereço com número (Rua/R./Av./Alameda/Travessa … , nnn) → endereço de lote é dado de cliente
  - CNPJ, CPF, telefone                                        → dado pessoal ou societário
  - "R$" seguido de número numa peça                            → honorário, VGV, preço
  - token do GitHub ou chave Google fora do arquivo autorizado → segredo

Exceções deliberadas ficam em sistemas/guarda-publico.allow, uma por linha:
  <caminho>:<trecho literal>    — aceita esse trecho nesse arquivo, e só nele.
Cada exceção precisa de decisão do Michel; escrever o motivo em comentário (#).
"""
import pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ALLOW = RAIZ / 'sistemas' / 'guarda-publico.allow'
IGNORA = ('.git/', 'superado/')          # superado/ é histórico assumido, mas continua público — não pôr cliente lá

PADROES = [
    ('cliente nomeado',  re.compile(r"\[\s*'cliente'\s*,\s*'([^'—-][^']*)'"), ('.html',)),
    ('url área cliente', re.compile(r"michel-stein\.netlify\.app/cliente"), ('.html', '.md', '.js', '.json')),
    ('endereço',         re.compile(r"\b(?:rua|r\.|av\.|avenida|alameda|al\.|travessa|estrada|rodovia|via)\s+[A-Za-zÀ-ú][A-Za-zÀ-ú \.]{2,40},?[ ]*(?:n[ºo°][ ]*)?\d{1,5}\b", re.I), ('.html', '.md')),
    ('cnpj',             re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"), ('.html', '.md')),
    ('cpf',              re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"), ('.html', '.md')),
    ('telefone',         re.compile(r"\(?\b\d{2}\)?\s?9?\d{4}-\d{4}\b"), ('.html', '.md')),
    ('valor em R$',      re.compile(r"R\$\s?\d[\d\.,]*"), ('.html',)),
    ('token github',     re.compile(r"\b(?:github_pat_|gh[pous]_)[A-Za-z0-9_]{20,}"), ('.html', '.md', '.js', '.json', '.py', '.yml')),
    ('chave google',     re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}"), ('.html', '.md', '.js', '.json', '.py', '.yml')),
]

def excecoes():
    ex = set()
    if ALLOW.exists():
        for ln in ALLOW.read_text(encoding='utf-8').splitlines():
            ln = ln.split('#', 1)[0].strip()
            if ln and ':' in ln:
                ex.add(tuple(ln.split(':', 1)))
    return ex

def main():
    ex = excecoes()
    achados = []
    for p in RAIZ.rglob('*'):
        rel = p.relative_to(RAIZ).as_posix()
        if not p.is_file() or rel.startswith(IGNORA) or p.suffix not in ('.html', '.md', '.js', '.json', '.py', '.yml'):
            continue
        if p.stat().st_size > 20_000_000:
            continue
        txt = p.read_text(encoding='utf-8', errors='ignore')
        # base64 embutido gera falsos positivos de "chave google": tirar data-URIs antes de varrer
        txt = re.sub(r"data:[a-z]+/[a-z0-9\.\-\+]+;base64,[A-Za-z0-9+/=]+", "data:…", txt)
        for nome, rx, exts in PADROES:
            if p.suffix not in exts:
                continue
            for m in rx.finditer(txt):
                trecho = m.group(0)
                if (rel, trecho) in ex or (rel, m.group(1) if m.groups() else trecho) in ex:
                    continue
                if nome == 'chave google' and rel == 'modulos/ms-maps-chave.js':
                    continue  # chave de navegador restrita por referrer — exceção documentada no próprio arquivo
                if nome == 'valor em R$' and 'placeholder' in trecho.lower():
                    continue
                linha = txt.count('\n', 0, m.start()) + 1
                achados.append((rel, linha, nome, trecho[:70]))
    if not achados:
        print('guarda: limpo'); return 0
    print(f'guarda: {len(achados)} achado(s) — o push NÃO está liberado\n')
    for rel, ln, nome, tr in achados:
        print(f'  {rel}:{ln}  [{nome}]  {tr}')
    print('\nPeça de cliente vai para michel-stein-site/cliente/<slug-token>/ (registro em michel-stein-sistemas/site/AREA-CLIENTE.md).')
    print('Exceção deliberada, com decisão do Michel: sistemas/guarda-publico.allow')
    return 1

if __name__ == '__main__':
    sys.exit(main())
