# marca michel stein_ — a camada de marca

Documento de método, sem dado de cliente. Mora no repositório **público** de
apresentações para abrir por URL raw, sem token, em qualquer conversa.

Este arquivo é a **camada de marca**: os valores que uma peça precisa saber
para sair com a cara da michel stein_. Ele não descreve como uma apresentação
funciona — isso é `michel-stein-sistemas/prancha/PRANCHA-SISTEMA.md`, o motor.
Separar os dois é o que torna possível montar a mesma peça com outra marca.

As folhas do manual, em desenho: `../michel-stein-marca/01-capa.html` a
`05-aplicacoes.html`. Este arquivo é o resumo operável delas.

---

## Identidade

| campo | valor |
|---|---|
| nome | `michel stein_` — sempre caixa-baixa, com o underscore |
| papel | `arquiteto · ilustrador` |
| tagline | `a mão por trás do traço` |
| site | `michelstein.com.br` |
| direção | D · Mono Editorial |
| monograma nível 1 | `ms_` |
| monograma nível 2 | `m_` — favicon, avatar pequeno, selo |

O underscore é **parte do logotipo, não cursor**, e é sempre terracota.

## Cor

| token | hex | papel | proporção |
|---|---|---|---|
| `--creme` | `#EDE6DA` | base, fundo | 50% |
| `--tinta` | `#211D1A` | texto, principal | 26% |
| `--oliva` | `#6B6A4B` | secundária ativa: blocos, fundos de seção, avatares | 22% |
| `--terra` | `#B85C38` | destaque, mínimo: o traço ou uma palavra | 2% |

Apoio: `--hair: #211D1A22` (filete), `--desk: #CFCBC2` (mesa, só no manual),
`--moldura: #1A1714` (a tarja do letterbox na prancha).

**A terracota nunca é área grande e nunca é fundo.** É o que a mantém contida.
Sobre oliva o destaque clareia para `#E9A184`.

## Tipografia

| uso | face |
|---|---|
| marca, títulos, destaques | **DM Mono** Medium itálico (500), caixa-baixa, tracking −.06em |
| subtítulo de apoio | DM Mono 400 itálico |
| label e metadado | DM Mono 400, caixa-alta, +.20em |
| texto corrido, interface | **Inter** 400 / 500 / 600 |

Numa prancha as duas vão **embutidas em base64**, subset latino
`U+0000-00FF`, seis faces — a peça roda sem internet. No manual de marca elas
vêm do Google Fonts, porque ali a rede está pressuposta.

`R$` nunca vira `r$`: o título é caixa-baixa por sistema, o símbolo da moeda
não. Resolvido no render, não no conteúdo.

## Regras de uso do logotipo

- Área de proteção: margem livre igual à **altura do "m"** em volta.
- Tamanho mínimo: `ms_` a 24px, `m_` a 18px, favicon 16px.
- Não trocar a cor do traço · não usar a versão reta · não usar caixa-alta ·
  não esticar · não aplicar sombra · não usar sobre fundo de baixo contraste.

## Versão rabisco

`../michel-stein-marca/assets/scribble-ms.png` (mestre, 1679 × 1513),
`scribble-ms-900.png` (uso) e `scribble-ms.gif` (animada, 5 quadros).

**Sem regra escrita.** Não está definido onde entra, tamanho mínimo, nem
comportamento sobre fundo claro — o `ms` é branco e some sobre creme. Até que
a regra exista: só contexto informal, nunca documento formal ou proposta.

---

## Como esta camada é usada — e como se troca de marca

Uma peça de prancha consome desta camada, e só disto:

1. **os quatro tokens de cor**, nos `:root` do deck;
2. **as duas faces**, embutidas;
3. **a assinatura** no chrome, alto à direita;
4. **a capa**, que é a marca sobre o carrossel morph
   (`michel-stein-sistemas/prancha/PRANCHA-CAPA.md`);
5. **o fundo morph**, cujo acervo de imagens é do dono da marca.

Trocar de marca é trocar este arquivo por outro do mesmo formato e refazer os
cinco pontos acima. O motor — gabaritos, quadro fixo, revelação por clique,
chrome, validação — não muda.

**O que ainda não está separado, e é o trabalho pendente:** hoje os quatro
hex e as duas faces estão escritos à mão dentro de cada deck, e a capa é um
HTML de 561 KB com a marca soldada. Enquanto for assim, trocar de marca é
edição manual peça a peça, não substituição de uma camada.
