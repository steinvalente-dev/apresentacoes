# deck.json — a ficha

Montar uma peça = preencher um JSON e rodar dois comandos. Marca, escala, chrome e capa vêm do
esqueleto e do bloco da marca — nada se decide aqui. Método inteiro: `DECK-MONTAR.md`.

## Os dois comandos (na raiz do clone)

```
python3 sistemas/montar.py <slug> --marca <michel-stein|sarasa|amaz|lavro> --deck <deck.json> [--img <pasta>] [--cliente]
node sistemas/validar.mjs <slug>/apresentacao.html [--cliente]
```

`<slug>`: minúsculas e hífen (`casa-exemplo`). Saída: `<slug>/apresentacao.html` + `<slug>/meta.json`.
`--img`: pasta das imagens (padrão: a pasta do deck.json). `--cliente`: peça de cliente — sem botão
de voltar, não vai para o acervo público. Peça já existente só é substituída com `--sobrescrever`.
Publicar só com o validar em **passou**.

## O formato

```json
{
  "projeto": "Casa Exemplo",
  "titulo": "casa<br>exemplo",
  "sub": "Uma linha dizendo do que se trata.",
  "kick": "BAIRRO · CIDADE",
  "metas": [["cliente","—"],["etapa","estudo preliminar"],["data","—"]],
  "div_imgs": ["vista-01.jpg"],
  "deck": [
    {"g":"capa"},
    {"g":"sumario","kick":"o argumento","t":"o que esta peça mostra","itens":[["01","o lote","Uma frase."],["02","o projeto","Outra."]]},
    {"g":"divisor","div":1,"terra":1,"fundo":1,"sec":"o lote","dn":"01","dt":"o lote","ds":"A frase que prepara."},
    {"g":"frase","esc":1,"trama":1,"kick":"a ideia","t":"a frase que carrega<br>o argumento"},
    {"g":"lista","largo":1,"kick":"as decisões","t":"três decisões",
     "itens":[["01","<b>primeira.</b> O apoio."],["02","<b>segunda.</b> O apoio."]]},
    {"g":"cheia","src":"render.jpg","h2":"a sala vista do jardim","cap":"O que a imagem mostra."},
    {"g":"duo","kick":"antes e depois","t":"o lote hoje e com a casa","ar":"1.5",
     "figs":[["hoje","antes.jpg","Legenda a.",""],["proposta","depois.jpg","Legenda b.",""]],
     "leg":"A legenda comum às duas."},
    {"g":"prancha","tipo":"desenho","cols":2,"top":{"h2":"plantas"},
     "items":[{"src":"terreo.png","cap":"térreo","ar":"1.5"},{"src":"superior.png","cap":"superior","ar":"1.5"}]},
    {"g":"tabela","kick":"em números","t":"áreas","cols":["","térreo","superior"],"linhas":[["área","180 m²","120 m²"]]},
    {"g":"fim","kick":"encaminhamento","t":"próximos passos","itens":[["primeiro","<b>Aprovar o partido.</b>"],["depois","<b>Anteprojeto.</b>"]]}
  ]
}
```

- **Topo:** `projeto` obrigatório; `titulo`, `sub`, `kick`, `metas` preenchem o slide `{"g":"capa"}`
  quando ele não traz os seus. `metas` com nome de cliente é peça de cliente → `--cliente`.
- **`deck` é o miolo.** Abertura e contracapa vêm do bloco da marca; não se escrevem. (Se o primeiro
  ou o último slide for `g:"marca"`, ele é respeitado.)
- Strings aceitam HTML (`<br>`, `<b>`). `sec` num divisor cria o ponto no chrome.
- **Imagens:** `src`, `figs[][1]`, `items[].src`, `pilha[].src`, `res[].src` e `div_imgs[]` com nome de
  arquivo em `--img` são redimensionadas (cheia 2200 px · duo/prancha 1800 px · `"tipo":"desenho"` no
  slide = resolução nativa) e embutidas em base64. `src:""` = slot hachurado, que é recurso, não erro.
  URL `http…` fica como está. Acima de 8 MB de imagem o montar grava em `<slug>/img/` e avisa: a
  peça passa a exigir a PASTA e se entrega por link.
- `capa_imgs` só se quiser trocar o acervo da marca (raro); `map` só para o gabarito `mapa` de lotes.

## Gabaritos

Tabela completa (campos, obrigatórios, aridade dos itens) em `DECK-MONTAR.md`, entre
`<!-- GABARITOS:INICIO -->` e `<!-- GABARITOS:FIM -->`. Os do dia a dia: `capa sumario(itens 3)
divisor(dt) frase lista(itens 2) trio(itens 2) tabela(cols+linhas) cheia(src) duo(figs 4 + leg)
prancha(cols é NÚMERO) fim(itens 2)`. Com máquina própria, ler `gabaritos/<nome>.md` antes:
`earth-3d modelo-3d mapa prancha`. Gerais: `sec kick t sub esc terra trama fundo div nota fecho pre largo`.

## meta.json

Escrito pelo montar; registra a peça no acervo. `pranchas` conta **todos** os slides, abertura e
contracapa inclusas; `peso` é a pasta inteira (html + img/); `data` é o dia da montagem. Ao
sobrescrever só `pranchas peso data frente cliente` mudam — `nome`/`sub` editados à mão ficam.

## O validador: o que fazer em cada FALHA

| check | quer dizer | o que fazer |
|---|---|---|
| `sintaxe` | um `<script>` não passa no `node --check` | há aspa/HTML quebrado numa string do JSON; corrigir o texto |
| `gabaritos` | slide vazio, `gabarito desconhecido`, `falta <campo>` ou "posição vazia" | trocar o `g` por um da tabela, ou acrescentar o campo obrigatório |
| `undefined` | um slide escreve `undefined`/`NaN` | item com campo de menos (ex.: `duo` sem `leg`, `lista` com item de 1 campo) |
| `console` | `pageerror` ou `console.error` | ler a mensagem; em geral é a causa de `gabaritos`, ou imagem com caminho errado |
| `fontes` | menos de 4 `@font-face` em base64 | o bloco da marca não foi colado — remontar; não editar o HTML à mão |
| `voltar` | falta a linha do `ms-voltar.js` (ou sobra, com `--cliente`) | montar de novo com/sem `--cliente`, conforme a peça |
| `em-imagem` | gabarito com fundo de imagem/visor fora da lista do `go()` | é engine: registrar em `DECK-REGISTRO`; não resolver na peça |
| `hex` | `#RRGGBB` no CSS fora do `:root` | é engine ou bloco: não escrever cor à mão; usar `var(--…)` |
| `proporcoes` | transbordo (`+Npx`) ou letterbox num dos 7 tamanhos | **cortar texto**, nunca encolher tipografia: menos itens, ou dois slides |
| `peso` (aviso) | acima de 8 MB | entregar por link; ou menos imagens |
| `chave-maps` (aviso) | tem `earth-3d` | só por link; o domínio precisa estar na chave da Maps Platform |

O montar já barra `gabarito desconhecido` e `falta <campo>` antes (código 3, peça escrita mesmo assim).
