# registro — o que cada frente lista no acervo

O `index.html` não tem mais lista nenhuma escrita dentro. Ele lê `dados.json`,
na raiz, que é **GERADO** por `python3 sistemas/montar-indice.py` a partir de
duas fontes:

1. **`<slug>/meta.json`** — uma peça publicada se registra sozinha. O
   `sistemas/montar.py` escreve esse arquivo ao montar a peça. `href` não se
   escreve: é sempre `<slug>/apresentacao.html`.
2. **`registro/<frente>.json`** — o que cada frente registra à mão: documentos
   (abas deck, marca e sistema) e peças fora do padrão (href absoluto, versão
   oculta em `superado/`).

`dados.json` **nunca se edita** — o próximo `montar-indice.py` sobrescreve, e
`publicar.sh` roda ele antes de todo commit. Quem quer mudar o índice mexe em
um `meta.json` ou em um `registro/<frente>.json`. Só.

## Qual arquivo cada frente edita

| arquivo | quem edita | o que vai nele |
|---|---|---|
| `_geral.json` | qualquer frente, com cuidado | o sistema: montar, gabaritos, peças de montar, consulta, registro, publicação, contexto, operação, notion, proposta, levantamento 3D, site — tudo que não é de uma marca |
| `michel-stein.json` | prática própria | marca michel stein_, rodadas do deck |
| `sarasa.json` | Sarasá | marca Sarasá, banco de referência, mapeamento de danos |
| `amaz.json` | AMAZ | marca AMAZ, marchetaria; a versão oculta em `superado/` |
| `lavro.json` | Lavrō | marca Lavrō, Azulejo, relatório de período |
| `baraka.json` | Baraka | identidade "a levantar" |

Cada frente edita o **seu** arquivo. Duas frentes no mesmo arquivo é o problema
que este desenho existe para acabar. Doc de sistema (`_geral.json`) é a exceção:
puxar antes de editar, e o `publicar.sh` já faz `pull --ff-only` no passo 1.

**O `_` do `_geral.json` tem uma armadilha, e ela já disparou.** O `.gitignore`
tem `_*`, para rascunho de sessão nunca subir — e engoliu o `_geral.json` calado
na fase 2: o arquivo existia no disco de quem o escreveu, o build passava, e o
repositório nunca o recebeu. Resultado: de 03 a 04/09/2026 as abas **deck** e
**sistema** ficaram com 2 linhas em vez de 33, sem sintoma nenhum. Hoje o
`.gitignore` tem `!registro/_geral.json` e o `montar-indice.py` para o build se
o arquivo faltar ou estiver ignorado pelo git. Não tirar nenhuma das duas.

## Formato de `registro/<frente>.json`

```json
{
  "projetos": [
    { "nome": "AMAZ", "pecas": [
      { "nome": "apresentação institucional · versão de 23.08", "pranchas": 37, "peso": 6.1,
        "data": "23.08.2026", "oculto": true, "href": "superado/2026-09-02-amaz-apresentacao.html" }
    ] }
  ],
  "docs": [
    { "aba": "marca", "grupo": "AMAZ", "nome": "marca · amaz",
      "desc": "A identidade visual da AMAZ…",
      "arq": "marca/MARCA-AMAZ.md", "ver": "amaz-identidade/apresentacao.html" },
    { "grupo": "notion", "nome": "bancos de consulta · Baraka", "desc": "…",
      "href": "https://github.com/steinvalente-dev/michel-stein-sistemas/blob/main/notion/CONSULTAS-BARAKA.md" }
  ]
}
```

`projetos` quase sempre fica `[]`: peça normal se registra pelo `meta.json` da
pasta. Entra aqui só peça com `href` absoluto (entrega em outro repositório) ou
versão oculta (`oculto: true`) apontando para `superado/` ou `<slug>/anteriores/`.
Peça com nome de cliente não entra em lugar nenhum deste repositório: mora em
`/cliente/` do site e o registro dela é privado.

### Campos de um documento (`docs`)

| campo | obrigatório | efeito |
|---|---|---|
| `nome` | sim | o título da linha, minúsculas |
| `desc` | sim | uma frase: o que é e quando se lê |
| `arq` **ou** `href` | um dos dois | `arq` = caminho neste repositório, abre no leitor da página, marca **público**; `href` = URL absoluta (repositório privado), abre no GitHub, marca **privado** |
| `aba` | não | `"deck"` ou `"marca"`; sem o campo, a linha vai para a aba **sistema** |
| `grupo` | sim | o separador dentro da aba. Grupo novo é só escrever um nome que ainda não existe — e acrescentá-lo em `ORDEM_GRUPOS` do `montar-indice.py`, senão sai no fim da aba |
| `ver` | não | acrescenta "ver artefato" apontando para a coisa funcionando. Peça apontada por `ver` conta como registrada para o detector de órfã |

A ordem dentro do grupo é a ordem do arquivo. A ordem dos grupos em cada aba
está fixada em `ORDEM_GRUPOS`, no `montar-indice.py`.

## Contrato do `meta.json` (para referência — quem escreve é o montar.py)

```json
{ "projeto": "casa X", "nome": "estudo preliminar", "pranchas": 29, "peso": 11.9,
  "data": "19.08.2026", "frente": "michel-stein",
  "sub": "opcional", "tipo": "sistema", "unid": "telas", "oculto": true, "cliente": false }
```

| campo | | |
|---|---|---|
| `projeto` | obrigatório | agrupa: peças com o mesmo `projeto` (caixa e acento ignorados) ficam juntas |
| `nome` | obrigatório | o que é a peça, minúsculas. Nunca com número: 01, 02 saem da ordem, mais recente em cima |
| `pranchas` | obrigatório | quantas pranchas o deck tem |
| `peso` | obrigatório | MB **no disco** (a pasta inteira, com `img/`), não o transferido. O Pages comprime; quem manda por e-mail precisa do número do disco. Acima de 8 MB o índice marca sozinho. O gerador avisa se divergir > 5% do disco |
| `data` | obrigatório | `DD.MM.AAAA`. Define a ordem dentro do projeto |
| `frente` | obrigatório | `michel-stein`, `sarasa`, `amaz`, `lavro` ou `baraka` |
| `sub` | opcional | texto curto que entra antes da contagem ("abre por link", "interativo") |
| `tipo` | opcional | `"sistema"` manda a peça para o bloco de baixo, "sistema visual" |
| `unid` | opcional | troca o rótulo "pranchas" (a Lavrō conta em "telas") |
| `oculto` | opcional | `true` esconde sem apagar o registro |
| `cliente` | opcional | `true` **barra o build**: peça de cliente não entra no acervo público |

## Registrar um documento novo, em três passos

1. abrir o `registro/<sua-frente>.json` e acrescentar um objeto em `docs`
   (grupo existente ou novo)
2. `python3 sistemas/montar-indice.py` — regrava `dados.json`; conferir no
   Chromium local, se quiser
3. `GH=<token> sistemas/publicar.sh "mensagem"` — faz o resto e devolve a URL

Regra completa em `sistemas/GITHUB-COMO-TRABALHAR.md`.
