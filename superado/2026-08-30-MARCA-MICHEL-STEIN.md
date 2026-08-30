# ⚠ SUPERADO — marca michel stein_ (até 30/08/2026)

> **Este arquivo está fora de uso desde 30/08/2026 e é mantido só como registro.**
> O mestre vigente é `marca/MARCA-MICHEL-STEIN.md`, que acrescentou as três
> assinaturas (§1), o grifo (§2) e a escala de números (§3).
> Não ler daqui, não citar daqui.


Documento de método, sem dado de cliente. Mora no repositório **público** de
apresentações para abrir por URL raw, sem token, em qualquer conversa.

Esta é a **camada de marca**: tudo o que uma peça precisa saber para sair com a
cara da michel stein_. O motor — gabaritos, quadro, revelação, chrome,
validação — está em `DECK-MOTOR.md`, ao lado, e não sabe de que marca é a
peça. **Montar uma apresentação = motor + esta marca + um DECK.**

**Este arquivo é o mestre.** O manual em desenho —
`michel-stein/manual.html`, cinco folhas numa página — é a *apresentação* desta
marca, o que se manda para fora. Divergiram, este ganha. A capa do deck tem
arquivo próprio, ao lado: `MARCA-MICHEL-STEIN-CAPA.md`.

---

## 1 · Identidade

| campo | valor |
|---|---|
| nome | `michel stein_` — sempre caixa-baixa, com o underscore |
| papel | **`arquiteto`**, sempre só isto — em slide, cartão, assinatura e manual |
| tagline | `a mão por trás do traço` |
| site | `michelstein.com.br` |
| monograma nível 1 | `ms_` |
| monograma nível 2 | `m_` — favicon, avatar pequeno, selo |

O underscore é **parte do logotipo, não cursor**, e é sempre o acento.

---

## 2 · Cor — os quatro papéis

| papel do motor | token no deck | hex | proporção |
|---|---|---|---|
| **papel** | `--creme` | `#EDE6DA` | 50% |
| **tinta** | `--tinta` | `#211D1A` | 26% |
| **primária** | `--oliva` | `#6B6A4B` | 22% |
| **acento** | `--terra` | `#B85C38` | 2% |

Auxiliares: `--hair: #211D1A22` (filete), `--moldura: #1A1714` (a tarja do
letterbox), `--desk: #CFCBC2` (a mesa, só no manual de marca).

**A terracota nunca é área grande e nunca é fundo.** É o que a mantém contida e
o que a afasta da paleta da identidade antiga. Sobre oliva o destaque clareia
para `#E9A184`; sobre terracota vai a creme.

> **O underscore é sempre terracota**, inclusive sobre oliva e sobre tinta.
> Sobre oliva isso mede 1,2:1 — **decisão consciente do autor**, identidade
> acima de contraste medido. Já foi proposta variante clara, medida em 3,03:1, e
> recusada. **Não reintroduzir "para corrigir".**

Michel cogitou usar **verde como destaque em slide creme** em alguns momentos.
Ficou para depois.

---

## 3 · Tipografia

| uso | face |
|---|---|
| marca, títulos, destaques | **DM Mono** Medium itálico (500), caixa-baixa, tracking −.06em |
| subtítulo de apoio | DM Mono 400 itálico |
| label e metadado | DM Mono 400, caixa-alta, +.20em |
| texto corrido, interface | **Inter** 400 / 500 / 600 |

Num deck as duas vão **embutidas em base64**, subset latino `U+0000-00FF`,
seis faces: DM Mono 400 e 500 (reto e itálico) mais Inter 400 e 500. No manual de
marca elas vêm do Google Fonts, porque ali a rede está pressuposta.

**Minúsculas nos títulos, exceto sigla e nome próprio:** `praça XV`, não
`praça xv`. Por isso o `h1` não força `text-transform`.

`R$` nunca vira `r$` — resolvido no render, não no conteúdo. Ver o motor.

---

## 4 · Regras fixas em slide

- **Capa do projeto:** nome do projeto, endereço logo abaixo, três metas —
  cliente · etapa · data. **Sem `kick` de status** acima do título (redundante
  com etapa) e **sem campo autoria** (a assinatura da marca já está no slide).
- **Na capa o rodapé sai.** `body.na-capa` esconde `.marca` e `.pe`.
- **Texto de cliente é impessoal.** Não "o que você escolheu"; escrever
  "referências selecionadas — e a análise das escolhas".

### Abertura — gabarito `marca` com `frase:true`

Um bloco só, no eixo `--gut-in`, gaps curtos, de cima para baixo:

1. `michel stein_` pequeno (`--fs-marca`), underscore terracota estático, com
   **`arquiteto` ao lado**: DM Mono 400 reto, 0,68em, caixa-baixa,
   `letter-spacing:.02em`, cor `--muted`, 1,1em de respiro. Liga com
   `papel:'arquiteto'`. É **exceção consciente** ao item "label · metadado" da
   folha 04 (que pede caixa-alta e +0,20em): quer-se texto corrido, como no site.
   **Não em terracota** — a terracota fica só no underscore, senão disputa com a
   assinatura.
2. o slogan, `clamp(22px, 3.75vw, 82px)`, underscore piscante, em DM Mono.
3. o site em **Inter 400**, `clamp(10px,.78vw,15px)`, `letter-spacing:.14em`. A
   mono fica reservada ao slogan, para não diluir a força dela.
4. **pílula "começar →"** em terracota, pequena, ligada por `comecar:true`.
   Redundante de propósito: convida a mexer o mouse (o fundo reage ao ponteiro) e
   a entrar. O clique chama `go(cur+1)`.

⚠ O espaçamento entre a marca e o `arquiteto` vai como `margin-left` no `<em>`,
**nunca como `gap` de flex** — o `gap` entra também entre o nome e o `<i>_</i>` e
descola o underscore.

Liga com `frase:true` + `sigla` + `slogan` + `site`. **Sem `frase`, o gabarito
cai no arranjo antigo** (`topo` + `sitePe`), que segue válido, só não é o da
abertura.

O slogan continua em `white-space:nowrap`, uma linha de fora a fora, com quebra
só abaixo de 620 px. Com o clamp atual sobra ~40% de largura em 1920. **Se o
slogan mudar de texto, remedir** com `Range.getBoundingClientRect()` contra
`clientWidth - padding`.

### Contracapa — gabarito `marca` com `sigla`

Bloco único centrado na vertical, no eixo `--gut-in`:

1. **QR** — `clamp(64px, 7vw, 128px)`, módulos em tinta sobre placa creme.
   Gerado com `segno` (`error='m'`, `border=2`), SVG inline na constante `QR`.
   **Aponta provisoriamente para michelstein.com.br** — destino final ainda não
   decidido. Trocar o destino = regerar a constante.
2. **`michel stein_`** com o underscore piscante.
3. **Site**, pequeno, colado na sigla (`.assina-marca`, gap ~6 px — o gap do
   `.body` separaria demais).

A contracapa também recebe o fundo morph (`fundo:true`), com esses três
elementos e nada mais.

---

## 5 · Fundo morph — o preset da marca

Preset **"linha MS"**, travado: transição *serigrafia* (duas telas em 22° e 54°,
o calibre de uma fecha enquanto o da outra abre), cursor em *paralaxe*,
densidade 4,5, sangramento 0,42, contraste 0,65, miolo 1,45, vinheta 0,86,
sangria total, **ponto quase preto sobre o oliva da marca**.

Paleta que a engine recebe: `{paper:'#6B6A4B', acc:'#B85C38'}` nos slides de
marca, `{paper:'#B85C38', acc:'#211D1A'}` no divisor. O `cor()` migra em rampa.

**O acervo do fundo é da marca.** Nove peças a 1024 px, JPEG q68, ~1,2 MB de
HTML — em `../fundo/01.webp` a `09.webp` no repositório de apresentações. São os
projetos dele: mostrar isso na abertura é o ponto. **No divisor o padrão é sem
assunto** — ver o motor.

---

## 6 · Versão rabisco

`michel-stein/assets/scribble-ms.png` (mestre, 1679 × 1513),
`scribble-ms-900.png` (uso) e `scribble-ms.gif` (animada, 5 quadros).

**Sem regra escrita.** Não está definido onde entra, tamanho mínimo, nem
comportamento sobre fundo claro — o `ms` é branco e some sobre creme. Até que a
regra exista: só contexto informal, nunca documento formal ou proposta.

---

## 7 · Regras de uso do logotipo

- Área de proteção: margem livre igual à **altura do "m"** em volta.
- Tamanho mínimo: `ms_` a 24 px, `m_` a 18 px, favicon 16 px.
- Não trocar a cor do traço · não usar a versão reta · não usar caixa-alta · não
  esticar · não aplicar sombra · não usar sobre fundo de baixo contraste.

---

## 8 · Checklist para criar `MARCA-<outra>.md`

Uma marca nova é este arquivo preenchido de novo. O mínimo:

1. **Nome, assinatura em slide e site** — o que vai no chrome.
2. **Os quatro papéis de cor**, em hex, com a proporção pretendida.
3. **As duas faces**, com peso e estilo por uso, e as licenças que permitam
   embutir em base64. Sem isso a peça não roda sem internet.
4. **A abertura**: que elementos entram e em que ordem.
5. **A contracapa**: o que fecha a peça.
6. **O acervo do fundo**, ou a decisão de não usar fundo morph.
7. **O que é intocável** — o equivalente ao "o underscore é sempre terracota".
   Toda marca tem um ponto em que a identidade ganha do contraste medido, e ele
   precisa estar escrito para não ser "corrigido" numa rodada futura.

**O que não muda entre marcas:** os gabaritos, o quadro fixo, a revelação por
clique, a estrutura do chrome, a pastilha da navegação, o retorno ao acervo e a
lista de validação. Isso é o motor.

⚠ **O bloqueio prático, hoje:** os hex e as faces estão escritos à mão dentro de
cada deck, com nomes de variável que são desta marca (`--creme`, `--oliva`,
`--terra`), e a capa é um HTML de 561 KB com a marca soldada. **Enquanto for
assim, trocar de marca é edição peça a peça, não substituição de camada.** O
caminho está descrito no fim do `DECK-MOTOR.md`, e passa por o
`deck-esqueleto.html` existir — coisa que ainda não acontece.
