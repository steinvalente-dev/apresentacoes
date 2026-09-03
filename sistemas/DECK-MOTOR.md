# deck — o motor

Documento de método, **sem dado de cliente**, no repositório público de
apresentações. Abre por URL raw, sem token, em qualquer conversa:
`https://raw.githubusercontent.com/steinvalente-dev/apresentacoes/main/sistemas/DECK-MOTOR.md`

Criado 04/08/2026 · separado do documento único em **29/08/2026** · partido por
ocasião de leitura no mesmo dia.

> **⚑ Este não é mais o arquivo que se lê para montar.** Em 29/08/2026 ele foi
> partido por ocasião de leitura, porque 9.300 tokens eram pagos toda vez que
> alguém ia montar uma peça — e montar usa um terço disto.
>
> | você quer | leia |
> |---|---|
> | **montar uma peça** | `DECK-MONTAR.md` — o arquivo curto |
> | um gabarito com máquina própria | `gabaritos/<nome>.md` |
> | a identidade | `../marca/MARCA-<nome>.md` |
> | **entender por que algo é assim, ou consertar** | este arquivo |
>
> O que sobrou aqui: a história das três arquiteturas, as armadilhas já pagas, a
> validação completa, o desenho do chrome e do fundo. Consulta, não leitura
> corrente.

---

## As três camadas — leia isto primeiro

O sistema de apresentações — o **deck** — tem três camadas, e confundi-las é o que impedia
trocar de marca:

| camada | o que é | onde mora |
|---|---|---|
| **motor** | gabaritos, quadro, revelação, chrome, validação. **Não sabe de que marca é a peça.** | este arquivo |
| **marca** | cor, tipografia, logotipo, assinatura, capa, acervo do fundo | `../marca/MARCA-<nome>.md` — pasta própria, uma por marca |
| **peça** | o array `DECK` de uma apresentação | o HTML da peça |

**Montar uma apresentação = motor + uma marca + um DECK.** Trocar de marca é
trocar o segundo item, e nada mais. Este arquivo nunca cita cor, fonte ou nome
próprio de marca alguma: onde precisaria, cita o **papel** (papel, tinta,
primária, acento) e a marca resolve.

Registros de rodada com nome de cliente ficam no repositório privado, em
`michel-stein-sistemas/deck/rodadas/`.

### Uma palavra, três trabalhos — resolvido em 29/08/2026

O sistema chamava-se **prancha**, e a palavra fazia três trabalhos ao mesmo
tempo: o sistema, um dos gabaritos e a unidade de contagem do acervo.
Confundia, e "prancha" já é palavra carregada em arquitetura.

**O sistema passou a se chamar `deck`** — nome que já era o do array de conteúdo
de toda peça. Os outros dois trabalhos ficaram como estavam, porque ali a
palavra está certa:

| onde aparece | o que significa | mudou? |
|---|---|---|
| o sistema, os documentos, a pasta | **deck** | sim |
| `g:'prancha'` dentro de um `DECK` | o gabarito de grade de imagens | não |
| `pranchas: 29` no acervo | quantas telas a peça tem | não |

Por isso **nenhuma peça publicada precisou ser editada.**

---

## O que é

Apresentação como **HTML único autossuficiente**. Conteúdo num array `DECK`;
gabaritos fixos, nunca canvas livre. Trocar conteúdo = mexer só no `DECK`.
**A engine abaixo dele não se toca.**

As duas faces tipográficas vão **embutidas em base64**, subset latino
`U+0000-00FF` — a peça **roda sem internet**, o que importa em sala de reunião.

> **Esta regra já existiu no papel sem estar cumprida.** Um arquivo entregue em
> 19/08/2026 não tinha `@font-face` nenhum: dependia de a fonte estar instalada
> na máquina, e num notebook de cliente cai no mono do sistema mesmo online.
> Corrigido em 20/08: seis faces em base64, geradas de `@fontsource/*`
> (SIL OFL 1.1) e reduzidas com `pyftsubset` ao latim básico mais o suplemento
> Latin-1, que cobre os acentos do português. 87 KB de woff2 → 104 KB de CSS.
> `src:local('<Face>'), url(data:…)` para quem tem a fonte instalada não
> decodificar o base64. **Conferir isso na validação de todo arquivo novo.**

**Toda apresentação leva uma linha a mais antes do `</body>`** — a do retorno ao
acervo. Não é opcional e não é enfeite: sem ela a peça abre sem saída. Seção
própria abaixo.

---

## Arquitetura — três gerações, e por que cada uma morreu

**v1 · palco fixo com tarja.** Palco de 1600×900 escalado por `transform`, com
tarja preta em tela de outra proporção. Rejeitada: queria-se sangria total.

**v2 · sangria total.** O conteúdo ocupa a tela inteira em qualquer resolução,
sem tarja e sem proporção fixa.

- `#palco` é `position:fixed; inset:0`; cada `.slide` é `position:absolute;
  inset:0` com `overflow-y:auto` — tela baixa rola em vez de cortar.
- **Toda medida sai de token `clamp()` no `:root`**: tipografia (`--fs-*`),
  margem (`--gut`), faixas do chrome (`--top`/`--bot`), setas, pontos, gaps.
  Nenhum px cru dentro de gabarito.
- Referência da escala: 1600×900, onde `1vw = 16px`.
- Chrome único, `position:fixed` sobre o palco, fora dos slides. Gabarito nenhum
  desenha trilha ou rodapé.
- Como `.slide` é posicionado e não tem borda, um filho `position:absolute` com
  `inset:0` cobre o slide **inteiro**, inclusive o padding. É o que faz `cheia`,
  `mapa` e `modelo` sangrarem.

**Por que a v2 não bastou.** Um deck é uma **prancha**: tem proporção, como
uma folha. Mas a folha de estilo tratava-a como página web — toda a escala em
`clamp(min, N vw, max)`. Num celular `1vw` vale 3,9 px, então **todo o texto
caía no piso do clamp** enquanto o volume de conteúdo continuava o mesmo, e os
breakpoints colapsavam as grades para uma coluna, dobrando a altura. A escala
enxergava a largura e era **cega para a altura**.

**v3 · quadro fixo (letterbox).** Ideia de 25/08/2026. O deck inteiro vive num
`#quadro` de **1600 × 900 fixos, em pixels**, escalado por `transform: scale(k)`
até caber na tela — exatamente o que um vídeo faz em tela cheia.
`k = min(larguraSegura/1600, alturaSegura/900)`.

```
<div id="moldura">      ← mede a ÁREA SEGURA, nunca a tela bruta
  <div id="quadro">     ← 1600 x 900 fixos, escalados por transform
     cortina · canvas · véus · palco · chrome
```

**As unidades de dentro são `cqw`/`cqh`, do contêiner, não da janela.** Com
`container-type:size` no quadro, `1cqw = 16px` e `1cqh = 9px` **sempre** — os
mesmos valores que `1vw`/`1vh` entregavam num 1600 × 900. Por isso nenhuma
clamp precisou ser recalibrada, e as pranchas saíram idênticas pixel a pixel na
medida de projeto.

O que se ganha: a peça é idêntica em qualquer tela; zero transbordo por
construção nas doze telas medidas, de 2560 × 1440 a 390 × 844; o notch e a
Dynamic Island param de comer informação, porque o quadro é medido contra
`env(safe-area-inset-*)`; e **as `@media` de largura viraram código morto** —
dentro de um quadro de 1600 × 900 elas nunca disparam.

O que se paga: no celular **em pé** o quadro cabe pela largura, 390 × 219. A
peça inteira, correta, e pequena. Girar resolve, e quem avisa é o módulo
`ms-voltar.js`, não a peça.

**Estado da adoção** (corrigido 02.09.2026): o esqueleto sai em **tela cheia,
sem tarja**, desde 02/09 — o quadro fixo descrito aqui é a base, e a moldura
deixou de aparecer; regras em `DECK-MONTAR.md`, "O que não é negociável", itens
1, 2 e 7. A peça de referência é `emei-presidente-dutra`. **Peças antigas ficam
como estão, em formato antigo** — decisão do Michel: a última peça é a mais
completa e os módulos se alinham a ela. Não se migra peça publicada.

### Três armadilhas do quadro fixo, já pagas

1. **`getBoundingClientRect` devolve pixel de TELA; `style.left` é pixel de
   LAYOUT.** O popover posicionava-se pela diferença entre os dois e saía do
   lugar em toda tela que não fosse 1600 × 900. Corrigido dividindo cada delta
   por `k`, lido de `--k` no momento de abrir.
2. **O `body` deixou de ser o fundo do deck** — ele agora é a moldura. Se as
   classes de tema continuassem pintando o body, **as tarjas do letterbox
   mudariam de cor a cada slide**. Quem pinta o tema é o `#quadro`; o body pinta
   `--moldura`.
3. **A conversão `vw → cqw` por regex barra decimais que começam com ponto.**
   `.96vw` fica de fora se o lookbehind excluir o próprio ponto do número — 48
   ocorrências sobreviveram e dois slides renderizaram diferente, com diferença
   de 1 a 3 px. **Regex de unidade CSS precisa aceitar `.96` tanto quanto
   `0.96`.**

**Limitação conhecida, não corrigida:** a paralaxe do fundo segue o ponteiro por
`e.clientX` (tela) contra `cv.clientWidth` (1600, layout). Fora de `k = 1` o
movimento satura antes da borda. É cosmético, e a engine não se toca.

**Consequência aceita em todas as gerações:** PDF não é caminho pronto. A
exportação exige fixar viewport e virou passe próprio. **Não prometer PDF sem
fazer o passe.**

---

## Gabaritos

**A lista dos gabaritos é a tabela do `DECK-MONTAR.md`**, gerada do `tpl()` do
esqueleto por `sistemas/gerar-gabaritos.py` — não se repete aqui. (Corrigido
02.09.2026: este trecho listava "os quinze do esqueleto", com `topicos`,
`etapas`, `meio`, `texto`, `desenho`, `planta` e `modelo`; era o vocabulário da
casa ITTB, e esses sete **não existem no esqueleto**. `sumario`, `players`,
`avulso` e `duasfrentes`, dados como "ainda não no esqueleto", estão nele.
Histórico no fim deste arquivo.)

⚠ **`cols` é campo reservado.** O `const tab` compartilhado do `tpl()` dispara
com `s.cols` e exige `s.linhas` logo em seguida. Um gabarito novo que use `cols`
para outra coisa quebra o deck inteiro com `Cannot read properties of undefined
(reading 'map')` — e o sintoma que aparece depois é `cur is not defined`, porque
o corpo do módulo morre antes de `let cur=-1`.

---

## Escala tipográfica

Todo tamanho é `clamp(mínimo, fluido, máximo)`. O terceiro valor é o teto que
impede o texto de explodir em tela grande; o primeiro evita ilegível em
notebook. Calibrada em 19/08/2026 — os tetos e a inclinação `vw` estavam altos
demais.

| token | calibragem vigente | em 1600px |
|---|---|---|
| `--fs-h1` | `clamp(38px, 4.6vw, 92px)` | 74 |
| `--fs-h2` | `clamp(24px, 2.65vw, 52px)` | 42 |
| `--fs-div` | `clamp(42px, 6.0vw, 124px)` | 96 |
| slogan | `clamp(22px, 3.75vw, 82px)` | 60 |

**Corpo, legenda e rótulo não mudaram** — já eram discretos e reduzi-los quebra a
leitura no projetor. Se for recalibrar, mexer só nos tamanhos de display.

Sob o quadro fixo (v3) os mesmos clamps valem, com `cqw` no lugar de `vw`.

---

## Regra de imagem

| o que é | gabarito | por quê |
|---|---|---|
| **render horizontal** (ar ≈ 1,7–1,8) | `cheia` | sangria total, impacto máximo, quase sem corte |
| **render quadrado, detalhe ou peça menor** | `duo` ou `prancha` | em sangria total perderia teto ou piso |
| **referência de repertório** (imagem pequena, fundo claro) | `prancha` | a composição em grade é o valor |
| **croqui, planta, corte** | `prancha` de uma coluna | `contain` — desenho técnico nunca se corta. (`planta` e `desenho`, com lupa, não estão no esqueleto — corrigido 02.09.2026) |

`cheia` usa `object-fit:cover`: imagem de proporção diferente de 16:9 **vai**
perder borda. Conferir a proporção antes de mandar para lá.

### `cheia` — o véu esvanece com o ponteiro parado

O gradiente do pé existe para a legenda ser legível, mas come a parte de baixo da
imagem. O véu do pé, o gradiente do topo **e o chrome** esvanecem em 0,55 s
depois de **1,8 s sem movimento**, e voltam ao primeiro gesto: ponteiro, roda,
toque ou tecla. Classe `ocioso` no `body`, mais `em-cheia` para restringir o
efeito a este gabarito. O chrome vai junto de propósito — sem ele a imagem não
fica inteira de verdade, e qualquer gesto o traz de volta. Respeita
`prefers-reduced-motion`.

### Resolução e peso

- render em **`cheia`: 2200 px de largura, JPEG q80** (~500–650 KB). Em sangria
  total 1800 px começa a amolecer.
- render em **`duo`/`prancha`: 1800 px, JPEG q82** (~400–500 KB).
- **croqui e planta: resolução nativa do recorte, JPEG q88** — a lupa amplia até
  600% e compressão baixa vira sujeira no traço.
- Ordem de grandeza: 29 slides com 25 imagens deram **12 MB**. Roda liso, mas
  **passa do limite de anexo de e-mail** — avisar quando cruzar ~8 MB.

### Croqui — recorte comum, nunca individual

Croquis do mesmo app vêm com muita área morta em volta. **Recortar todos com o
mesmo retângulo:**

1. detectar tinta em cada imagem — `lum < 165` **ou** (`saturação > 28` e
   `G < 210`), descontando o verde do canvas (`G > R+6` e `G > B+18` e
   `lum > 170`);
2. `bbox` de cada uma, depois a **união** de todas;
3. margem de ~55 px e aplicar **a mesma caixa** em todas.

Assim as plantas se registram: passar do térreo para o mezanino mostra o bloco
oeste caindo exatamente sobre o bloco oeste. Recorte individual faz cada slide
pular de posição e mata a leitura da sobreposição.

---

## Passo a passo — item numerado entra por clique

**Regra do deck, não opção.** A apresentação é por voz, e o que está na tela na
hora da fala é controlado. Vale para `lista`, `fim` e `duasfrentes` (`lista` é o
nome no esqueleto; `topicos` era o da casa ITTB — corrigido 02.09.2026).

- O item recebe classe `passo`, **não** `rev`. A cascata (`rev`) revela tudo de
  uma vez; aqui o ponto é o oposto.
- `avanca()`/`recua()` substituem `go(cur±1)` em **todos** os pontos de
  navegação: setas, teclado, clique no palco, swipe.
- `↓` e `↑` pulam o slide inteiro, ignorando os passos — atalho de ensaio.
- **Chegar avançando ou por salto começa em zero; voltar mostra tudo.**
- O contador mostra o estado: `21 / 29 · 2/4`.
- Os itens **não** mudam de posição ao aparecer — o grid reserva a altura final.

---

## Mecânicas de slide

### Popover de apoio — o texto sai da tela e volta no ponteiro

Slide com três dados mostra **só número e rótulo**, com um `+` discreto. O texto
de apoio abre numa caixa ao passar o ponteiro.

- **Sem título dentro da caixa.** Ele já está na tela, no elemento que a abriu.
- A caixa usa o **acento** da marca, texto em papel.
- Alinha pela **esquerda do elemento** e nasce logo abaixo da linha dele. Sem
  espaço embaixo, vira para cima em vez de sangrar para fora.
- No hover o elemento inteiro assume o destaque: linha, número e rótulo juntos.
- **Validar sempre:** percorrer todos os alvos e conferir que nenhuma caixa
  ultrapassa a viewport.

### Grifo animado

Faixa que se desenha da esquerda para a direita em 620 ms, com `background-size`
animado e `box-decoration-break: clone` para acompanhar a quebra de linha. **Não
é negrito: é marca de caneta por trás do texto.** Inverte sobre fundo escuro.
Roda uma vez, junto da revelação do slide. Uso: pontos-chave, não todo slide.

### Caixa que cresce — `duasfrentes`

A caixa nasce com altura zero e **cresce para baixo a cada item revelado**,
englobando o que já entrou: é a leitura do pacote se fechando na frente do
cliente. A altura sai do **layout** (`offsetTop + offsetHeight` do último
`li.passo.on`), **nunca** do `getBoundingClientRect` — o item entra com
`translateY`, e medir pelo retângulo pintado faria a borda pular junto com a
animação do texto.

O que **não** entra no pacote fica **fora da caixa**, na segunda linha da grade,
quebrando a caixa de propósito — e como filho direto do contêiner, não das
colunas, para cair alinhado e ser revelado depois dos itens.

### Dois estados no mesmo slide, em vez de dois slides

Quando dois slides compartilham um desenho e um título e só o bloco de texto
muda, **fazer um slide com dois estados**. Como dois, tudo re-anima a cada
passagem e o desenho "pula". Os dois blocos ocupam a mesma célula de grade, então
a caixa cresce pelo mais alto e nada salta. Validar medindo o
`getBoundingClientRect()` do desenho e do título antes e depois da troca: têm de
ser idênticos.

### Isométrico — o viewBox sai do desenho

Escrito à mão, ele decepa os últimos volumes toda vez que o espaçamento muda.
Calcular de `getBBox()` depois da inserção, com 3,5% de folga — cobre chão, rua,
árvores, rótulos e legenda. **Não voltar a escrever viewBox de isométrico à
mão.** O desenho troca de cor conforme o fundo, senão some no slide de primária.

### Símbolo de moeda nunca vira caixa-baixa

Os títulos são caixa-baixa por sistema; `R$` não. Resolvido **no render**,
envolvendo o símbolo em `<span class="ru">` com `text-transform:none` — assim o
`DECK` não precisa carregar marcação.

---

## Chrome — onde fica cada coisa

| posição | o que |
|---|---|
| alto esquerda | nome da seção ativa, com o número pendurado fora do fluxo |
| alto centro | pontos das seções; o nome aparece **acima**, no mouseover |
| alto direita | a assinatura da marca |
| baixo esquerda | projeto · cliente (sai na capa e nos slides de marca) |
| baixo direita | contador, estado dos passos e as duas setas |

O nome da seção é o que orienta quem assiste — "o usuário sempre tem a percepção
de onde ele está". Reanima só quando a seção muda.

**O rótulo do ponto abre para cima** (`bottom:100%`). Para baixo ele nascia
debaixo do cursor que estava fazendo o hover.

Sobre slide `inv` o chrome inverte, via classe `escuro` no `body`. No divisor e
no slide de marca escura há classes próprias (`no-divisor`, `marca-escura`) —
`--soft` tem de entrar nelas, senão assinatura e rodapé ficam tinta sobre tinta.

Setas com `:active scale(.94)` — press, nunca hover: no dedo hover não existe.

### Pastilha da navegação — decidido em 23/08/2026

O contador e as setas **não herdam mais a cor do slide.** Antes eram
`border:1px solid currentColor` sobre fundo nenhum, e isso quebrava sobre imagem
sangrada e em qualquer gabarito cuja cor de texto não combinasse com o que
estava atrás. O `.nav` inteiro passa a viver numa pastilha própria:

```css
.nav{background:rgba(<papel>,.94);
     -webkit-backdrop-filter:blur(7px) saturate(1.1);
     backdrop-filter:blur(7px) saturate(1.1);
     border:1px solid rgba(<tinta>,.22); border-radius:999px;
     box-shadow:0 1px 5px rgba(<tinta>,.16);
     color:var(--tinta)}
.seta{border:1px solid rgba(<tinta>,.34); color:var(--tinta); background:none}
.seta:hover{background:rgba(<tinta>,.08)}
```

**Por que clara e não escura**, medido contra cinco fundos — papel, primária,
superfície escura, foto clara e foto escura:

| tratamento | contraste do glifo | piso |
|---|---|---|
| pastilha escura, glifo claro | 6,2:1 a 14,9:1 | **6,2:1** |
| pastilha clara, glifo escuro | 9,7:1 a 11,4:1 | **9,7:1** |

A clara tem o piso mais alto e a menor variação. A fraqueza dela é sumir como
forma sobre fundo claro (1,0:1 sobre papel), e o **filete de tinta a 22%**
resolve exatamente isso. A escura tem a fraqueza simétrica sobre fundo escuro —
e ali um filete claro não a salvaria sobre foto escura, onde pastilha e borda
somem juntas. **Uma tem antídoto, a outra não.**

`backdrop-filter` é reforço, não requisito: sem suporte, os 94% de opacidade já
entregam o contraste sozinhos.

**Vale para toda marca.** A pastilha é sempre papel-sobre-tinta, independente de
o slide ser claro ou escuro — é justamente o ponto: o chrome de navegação deixa
de depender do tema do deck. Cada marca entra com os seus `--papel` e
`--tinta`; a estrutura não muda.

⚠ **Pendência de desenho, não de implementação.** As bolinhas de seção, o rótulo
da seção e a assinatura, no topo, seguem herdando `currentColor` e têm o mesmo
problema. Não foram tratados junto porque isso colocaria três pastilhas claras
na tela ao mesmo tempo e deixaria a assinatura como único elemento desprotegido.
**Ou os quatro entram, ou nenhum.**

---

## Retorno ao acervo — a linha obrigatória

Última coisa antes do `</body>`, em **toda** peça publicada:

```html
<!-- retorno ao acervo + camada de toque. Comportamento em modulos/ms-voltar.js -->
<script defer src="../modulos/ms-voltar.js"></script>
```

Vale desde 25/08/2026, para os gabaritos, para interativo e para grafismo —
qualquer coisa que vá para `steinvalente-dev/apresentacoes`.

**Por que é obrigatória.** O índice do acervo abre peça com `target="_blank"`.
Aba nova não tem histórico: sem essa linha, quem entrou numa apresentação fica
preso nela.

**O comportamento não mora aqui.** Mora em `modulos/ms-voltar.js`. É deliberado:
mudar o botão em todas as peças de uma vez é editar aquele arquivo, sem reabrir
deck nenhum. **Nunca soldar o chip dentro de um HTML de apresentação.**

| | |
|---|---|
| chip `← acervo` | alto à esquerda, `z-index` acima de todo o chrome do deck. Abre por 2,6 s na carga e recolhe para um disco discreto; no ponteiro fino reabre no hover |
| destino | derivado do `src` do próprio script, não do endereço da peça — não quebra se a pasta mudar de profundidade |
| camada de toque | `viewport-fit=cover`, `touch-action:manipulation`, `overscroll-behavior:none`, `text-size-adjust:100%`, `env(safe-area-*)` respeitada |
| tela cheia | chip `⛶` ao lado, só em `pointer:coarse` e só onde `document.fullscreenEnabled` — iPhone não expõe e o chip não nasce |
| aviso de girar | só em deck de tela fixa, em retrato, **que ainda não tenha o próprio** |

**Não colide com a engine.** O script não toca em variável, classe nem listener
do deck. O chip é irmão do `#palco`, então clique nele não sobe para o
`avanca()`; `Enter` e espaço são barrados na captura.

**Degrada em silêncio.** Arquivo aberto do disco ou mandado por e-mail não acha o
script: nenhum chip, e a peça abre exatamente como antes.

**Caminho relativo.** `../modulos/` vale porque toda peça mora a exatamente um
nível da raiz (`<slug>/arquivo.html`). Peça mais funda ajusta o `../`.

**Cache.** O Pages entrega o módulo com `max-age=600` — ajuste no chip demora até
10 min para chegar em quem já abriu.

⚠ **Achado aberto:** em retrato estreito (390 px) o chip de voltar e o chip de
tela cheia se sobrepõem no canto superior esquerdo. É do módulo e vale para
todas as peças.

Runbook e tabela de campos: `GITHUB-COMO-TRABALHAR.md`, ao lado deste arquivo.

---

## Seções, transição e entrada

Um slide com `sec:'nome'` abre seção e ganha **um** ponto; os seguintes sem `sec`
pertencem a ela. Faixa boa: **cinco a nove seções**.

Saída rápida, entrada calma: `.slide` sai em 150 ms, `.slide.ativo` entra em
440 ms com `translateY` de 14 px. Dentro do slide, cada bloco leva `rev` e sobe
em cascata; o `--i` é atribuído em JS na ordem do documento, com **teto de 10
passos** (≈420 ms).

**A cascata reinicia a cada chegada:** remove `revelado`, força reflow com
`void sl.offsetWidth`, recoloca. Remover a classe **só do slide que entra** — se
remover também do que sai, ele pisca.

---

## Aviso de orientação

Celular no retrato recebe um cartão sugerindo o horizontal. **Sugestão, nunca
barreira.**

- **Só em celular:** exige `pointer:coarse` **ou** menor dimensão ≤ 820 px.
  Janela de desktop redimensionada não dispara.
- **Um toque dispensa**, e esse toque não avança slide (`stopPropagation` no
  overlay, em `z-index:90`, acima da lupa).
- **Volta toda vez que o aparelho retorna ao retrato.** O estado é a transição,
  não um flag de "já viu": `avaliaGiro()` guarda `eraRetrato` e só age quando o
  valor muda.
- O swipe é bloqueado enquanto o cartão está na tela, senão o gesto de dispensar
  trocaria de slide.
- `orientationchange` só é confiável com `setTimeout` de ~260 ms — o viewport
  ainda não atualizou no instante do evento.

Desde 25/08 o `ms-voltar.js` cobre a lacuna em deck que não tenha aviso próprio.
O módulo detecta o `#giro` do deck e não duplica. **O do esqueleto é mais bem
resolvido — o módulo é rede de segurança, não substituto.**

---

## Conteúdo embutido que depende de rede

Dois gabaritos furam a autossuficiência, e isso está declarado no próprio slide.

**`mapa`** — embed de mapa em sangria total: `padding:0`, iframe
`position:absolute; inset:0`. Entra com `inv:true`. Dois cuidados de leitura: o
`scrim` é **denso nas pontas**, não degradê suave (~92% de opacidade nos
primeiros 7% e nos últimos 12% da altura, transparente no meio); e o rótulo tem
**caixa translúcida própria**, com `backdrop-filter:blur(6px)` e filete de 1px.

**`modelo`** — visor 3D. **Sem título, sem subtítulo, sem legenda: o slide é o
visor.** Qualquer texto rouba área da experiência de girar.

Os dois compartilham a **trava de teclado explícita**: o iframe rouba as setas,
então a ativação é por clique num `.veu` e há um botão `.sair` **fora** do
iframe. `desativaModelo()` varre `.g-modelo,.g-mapa` e nunca usa a classe `ativo`
(que é o estado do slide visível). O `src` só é atribuído ao chegar no slide, a
partir de `data-src`.

**Sem internet os dois abrem em branco.** Não colocar mapa ou visor num slide que
carregue informação crítica sozinho.

---

## Encerramento — `fim`

Título e ações **próximos e centrados como par**, não jogados nos cantos:
`grid-template-columns:auto minmax(0,1fr)`, `max-width:min(100%,1240px)` com
`margin:0 auto`. O item de ação vai em `--fs-item` (não `--fs-body`) e
`max-width:52ch` — é o que o cliente leva embora.

---

## Fundo morph pontilhado — o que o motor precisa saber

Shader WebGL2 de ~13 KB (`modulos/ms-fundo-engine.js`, núcleo compartilhado) que
faz transição entre imagens e converte tudo em trama de pontos. **Quais imagens,
qual paleta e qual preset é decisão da marca** — está em `../marca/MARCA-<nome>.md`. O
registro técnico do shader está em `FUNDO-MORPH-PONTILHADO.md`.

**Onde vive:** só nos slides marcados com `fundo:true`. Fora deles o canvas é
pausado e apagado.

**Cinco pontos de solda**, para repetir em qualquer deck:

1. CSS: `#msfundo` e `#msveu` fixos em `z-index:0`, `#palco` em `z-index:1`, e
   `body.com-fundo .slide.ativo{background:transparent;background-image:none}` —
   a especificidade tem de ganhar da regra de cor do gabarito `marca`.
2. DOM: `<canvas id="msfundo">` e `<div id="msveu">` imediatamente antes de
   `<div id="palco">`. **Nunca dentro do `#palco`** — a engine indexa slides por
   `palco.children[i]` e um filho extra quebra a navegação inteira.
3. `G.marca`, ramo `frase`: os campos da abertura vêm da marca.
4. Em `go()`: `body.com-fundo` por `s.fundo`, `body.em-cheia` por
   `s.g==='cheia'`, e o fundo pausa fora dos slides com fundo.
5. Um `<script>` no fim do `<body>` com o núcleo, `MSFundo.montar()` e a
   delegação de clique da pílula. Ele roda **depois** do `go()` de inicialização,
   então confere a classe no `body` para saber em que estado começar.

**Cortina diagonal — é a saída da abertura, não a entrada.** Nada de efeito na
carga: a diagonal acontece ao sair da capa para o primeiro slide. Painel
inclinado 14° com fio de acento de 3 px nas duas bordas; varre para a direita em
0,60 s, **a troca de slide acontece a 0,58 s escondida atrás do painel**, e o
painel sai em 0,64 s. Como o painel tem a cor do slide que entra, o olho lê uma
varredura só. Intercepta a saída da abertura venha de onde vier — pílula, seta,
teclado ou miniatura — reatribuindo `window.go`, o que funciona porque `go` é
função global de `<script>` clássico. Só dispara com `cur===0` e `i>cur`, e
respeita `prefers-reduced-motion`.

**Peso e desempenho.** Três imagens a 1024 px em base64 custam ~0,4 MB. Carga
progressiva: começa a animar com duas texturas prontas. Auto-pausa por
`visibilitychange` e `IntersectionObserver` — só o slide visível gasta GPU.
Escala de render em 0,9: o halftone destrói detalhe de qualquer forma. **Três a
cinco imagens por deck, não dez** — cada uma de 1024 px custa ~3,7 MB de VRAM.

---

## O divisor de seção com fundo

O divisor pode receber o fundo morph, e **o custo é praticamente zero**: o canvas
é único e fixo atrás do palco, então ligar o fundo num divisor não carrega imagem
nova nem ocupa VRAM adicional. O gasto é só o `requestAnimationFrame` enquanto
aquele slide está visível.

**Com assunto** — `modulos/divisor-morph.html`. O carrossel de peças atrás do
título. Serve quando as imagens têm a ver com o projeto apresentado.

**Sem assunto** — `modulos/divisor-trama.html`. **É o padrão.** Nenhuma imagem:
quatro campos de luminância gerados por código, e a grelha trocando entre eles.

> **Por que o padrão é sem assunto.** O carrossel da abertura é assinatura —
> mostrar os projetos ali é o ponto. No meio da apresentação de um cliente o
> mesmo carrossel vira ruído: o cliente está pensando na casa dele e aparece a
> orla de outro projeto. Pior ainda com render do próprio projeto, que chega
> gasto no slide que devia apresentá-lo. O divisor é pausa de respiro, e pausa
> não precisa de assunto.

**Como ligar:** `fundo:true` no divisor; paleta do divisor por `F.cor({paper, acc})`
na entrada e de volta à paleta da marca nos slides de marca — o `cor()` migra em
rampa, a troca não é corte; canvas e véu **imediatamente antes de `<div id="palco">`**.

**Véu, por contexto — travado, não recalibrar.**

| onde | véu | gradiente das pontas |
|---|---|---|
| abertura | 0.18–0.30 | conforme o gabarito `marca` |
| divisor **com** imagem | **0.60** | 0.50, transparente entre 26% e 74% |
| divisor **só trama** | **0.55** | 0.42, transparente entre 30% e 70% |

O divisor pede o triplo da abertura porque carrega o maior tipo do deck
(`--fs-div` chega a 124 px) e a trama compete diretamente com o título.

**Preset do divisor sem assunto:** transição serigrafia (a grelha troca dentro do
próprio retículo, sem fade e sem borrão), **cursor desligado** (`cur:0` — o
divisor é pausa; a trama reagir ao ponteiro puxa atenção para o lugar errado),
densidade 5.2, contraste 0.62, gama 1.28, velocidade 0.30 (troca a cada 6,5 s,
volta em 26 s), zoom 0.038, sangramento 0.10.

*Armadilha paga:* na primeira versão os campos variavam só de 0,24 a 0,94 de
luminância e eram parecidos entre si. Medido em Chromium, a diferença entre
quadros consecutivos ficava em **0,7 de 255** — a troca não existia para o olho.
Abrir os campos para quase 0–1 e subir o contraste de 0,46 para 0,62 deixou a
passagem em `0,8 → 3,8 → 10,3 → 5,0`.

*Aberto:* com seis divisores o fundo liga e desliga seis vezes. Tecnicamente
barato, mas muda o ritmo — o que era momento da abertura vira presença
recorrente.

---

## Multimarca — como o motor recebe uma marca

Um único bloco de tema no topo do `<style>` — as `@font-face` e o `:root` —
mais os objetos de abertura e contracapa no `DECK` e o `CAPA_IMGS`. Tudo isso
vem do **bloco da marca**, `../marca/<nome>/bloco.html`, que se cola no
esqueleto. (Corrigido 02.09.2026: não há constante `MARCA` no `<script>`.)
Trocar marca não reescreve gabarito.

O bloco de tema declara quatro papéis:

| papel | onde aparece |
|---|---|
| **papel** | fundo da maioria dos slides, pastilha da navegação |
| **tinta** | texto, glifos do chrome, filetes |
| **primária** | blocos, fundos de seção, slides invertidos |
| **acento** | destaque mínimo: um traço, uma palavra, o popover |

Mais dois auxiliares: **filete** (tinta a ~13%) e **moldura** (a tarja do
letterbox, na v3).

**Marcas registradas** (corrigido 02.09.2026 — a tabela anterior dizia que
Lavrō e Sarasá não tinham arquivo de marca; têm):

| marca | estado | onde |
|---|---|---|
| michel stein_ | implementada, é o padrão. Logotipo do canto: texto | `../marca/MARCA-MICHEL-STEIN.md` · `michel-stein/bloco.html` |
| AMAZ | levantada de peça publicada. Logotipo do canto: texto | `../marca/MARCA-AMAZ.md` · `amaz/bloco.html` |
| Lavrō | arquivo de marca e bloco prontos. Logotipo do canto: texto | `../marca/MARCA-LAVRO.md` · `lavro/bloco.html` |
| Estúdio Sarasá | arquivo de marca e bloco prontos; peça publicada (`emei-presidente-dutra`). Logotipo do canto: **o logotipo**, positivo/negativo pelo tema | `../marca/MARCA-SARASA.md` · `sarasa/bloco.html` |
| Baraka | sem sistema visual documentado | **não inventar paleta** — levantar antes e escrever o `MARCA-<nome>.md` |

A escolha texto × logotipo no canto superior direito é **por frente, escrita no
arquivo da marca** e configurada no bloco da marca — decisão do Michel,
02.09.2026. Regra em `DECK-MONTAR.md`, item 7.

### O que ainda não está separado

O `deck-esqueleto.html` **existe** desde 29/08/2026, em
`esqueleto/deck-esqueleto.html`, e cada marca tem o seu `bloco.html` — a
afirmação anterior deste trecho, de que o esqueleto "não existe em repositório
nenhum", está corrigida (02.09.2026). Em 03/09/2026 o `:root` foi renomeado
para os papéis — `--papel --tinta --primaria --acento --escuro --acento-claro
--f-display --f-corpo --f-mono`, iguais nos quatro blocos — e todo hex escrito à
mão no CSS e nos scripts virou `var()`/derivado. Os nomes antigos (`--creme`,
`--oliva`, `--terra`, `--mono`, `--sans`…) sobrevivem como aliases no bloco
DERIVADOS, para peça antiga. Vale a partir do esqueleto; peça publicada não se
reabre para isso.

---

## Validação — rodar antes de entregar

1. `node --check` no script extraído. Erro de sintaxe no `DECK` derruba o arquivo
   em silêncio.
2. **Varredura de tamanhos.** Playwright em 2560×1440, 1920×1080, 1440×900,
   1366×768, 1280×720, um 4:3 e um retrato; para cada slide medir
   `scrollHeight - clientHeight`. **Acima de 2 px é transbordo** e pede correção
   de composição, não scroll. *Sob o quadro fixo (v3) esta varredura passa por
   construção — rodar mesmo assim, é ela que prova.*
3. **Medir o slogan da abertura** com `Range`, em todos os tamanhos.
4. **Percorrer todos os alvos de popover** e conferir que nenhuma caixa
   ultrapassa a viewport.
5. **Aviso de orientação** em contexto móvel (`is_mobile`, `has_touch`): abre no
   retrato → toque dispensa sem trocar slide → navega normal → paisagem esconde →
   voltar ao retrato mostra de novo → desktop não dispara.
6. **Percorrer os passos por teclado** num `lista` e num `fim`.
7. Capturar `pageerror` e **olhar as imagens** num tamanho grande e num pequeno.
8. **Conferir que as faces em base64 estão no arquivo** — seis (michel stein_,
   AMAZ) ou quatro (Sarasá), conforme a marca.
9. **Gabarito de rede não é validável no sandbox** — os domínios de mapa estão
   bloqueados. Verificar só composição, véu e rótulo, e pedir a conferência na
   máquina dele.
10. **A linha do `ms-voltar.js` está antes do `</body>`?** Conferir no arquivo e,
    depois de publicar, no ar: `#msVoltar` existe, o `href` aponta para o índice
    do acervo, e `Enter` com foco no chip não avança o deck.

**Cuidado ao testar:** forçar `cur=-1` antes de `go(n)` deixa o slide anterior
com a classe `ativo` e a captura sai errada. Navegar sempre por `go()`, `#hash`
ou teclado.

---

## Convenções que sustentam o fluxo

**Slot de imagem vazio é recurso, não falha.** `src:''` renderiza retângulo
hachurado com nome do slot e proporção esperada; `src` quebrado cai no mesmo
slot. Permite entregar a estrutura antes de qualquer imagem existir.

**Marcação de pendência.** Parágrafo começando com `ESCREVER`, `CONFIRMAR`,
`PREENCHER` ou `VERIFICAR` renderiza em acento com barra tracejada. Separa o que
exige confirmação oficial (BDT, GeoSampa, certidão, levantamento) do que pode ser
afirmado como fato.

**Toda apresentação a cliente abre com slide "pontos a discutir"**, gabarito
`sumario` ou `lista` (`topicos`, o nome antigo, não existe no esqueleto), depois
da capa.

**Lupa em desenho técnico.** `.ph[data-lupa]` abre a imagem num visor de zoom
próprio (100–600%, arraste, esc fecha). Nunca `<embed>` de PDF: o visor do
navegador rouba o foco e as setas param de trocar slide. A máquina da lupa é da
casa ITTB e **não está no esqueleto** — `planta` e `desenho` dependem dela
(corrigido 02.09.2026).

**Proporção no `duo`.** Sem `ar`, a coluna estica e o `object-fit:cover` come o
desenho. Declarar `ar:'1.705'` (ou o que for). Sem `ar` só quando as duas imagens
têm proporções diferentes e o corte é aceitável.

**Ordem de argumento comercial: o preço vem depois do escopo, nunca antes.**

---

## Armadilhas já pagas

- **`.dot` colide** com a trilha do gabarito `etapas`. O ponto de seção é `.sdot`.
  Sem isso a trilha infla de 11 para 21 px.
- **`prancha` com 2 colunas e proporções diferentes transborda.** Duas células
  largas ficam altas demais e invadem cabeçalho e rodapé. Usar `duo` sem `ar` —
  ou `prancha` com 3 colunas.
- **`justify-content:space-between` na lista de tópicos** deixa o filete órfão.
  Correto é `li{flex:1}`.
- **Concatenação de string, não template literal**, na engine. Já se quebrou
  arquivo inserindo código dentro de crase aberta.
- **Imagem exportada do SketchUp com fundo transparente renderiza preto.** Voltou
  a acontecer depois de documentado. Compor opaco em RGB antes de embutir.
- **Fontes só no subset latino** (`U+0000-00FF`). Latin-ext leva a 848 KB de
  base64 sem ganho.
- Escrever em `stage.innerHTML` apagava o chrome na v1. Da v2 em diante o chrome
  é irmão do palco, não filho.
- **O clique do palco avança slide** — qualquer área interativa nova precisa
  entrar na lista de exceções (`.ph[data-lupa]`, `.g-modelo .visor`,
  `.g-mapa .visor`, `#giro`).
- **`segno.save()` em `StringIO` estoura** — o writer escreve bytes. Usar
  `BytesIO` e decodificar.
- **`will-change:transform` em painel de tela cheia inclinado** trava a
  renderização por CPU. Numa transição de 0,6 s não traz ganho nenhum.
- **`gap` de flex na linha da assinatura descola o underscore** do nome — o `gap`
  vale entre todos os filhos. Espaçamento vai como `margin-left`.
- **Canvas ou qualquer elemento novo dentro do `#palco` quebra a navegação** — os
  slides são indexados por `palco.children[i]`.
- **Chrome solto dentro do HTML da peça vira dívida de manutenção.** Botão, aviso
  ou HUD que valha para todas as peças vai para `modulos/`, nunca soldado no deck.
- **Colapsar coluna em tela baixa piora, não melhora.** Um `@media(max-width)`
  que empilhava doze linhas estourou 291 px em 1024. Na v2 a quebra tem de ir
  para largura bem menor; na v3 o problema deixa de existir.
- **Um build que gera o arquivo do zero apaga edição feita direto no
  repositório.** Antes de republicar uma peça:
  `diff <(curl -s <url da peça>) <build local>`.

---

## Histórico do método

Movido do `DECK-MONTAR.md` em 02/09/2026 — lá fica só a lição prática (o laço
de verificação). Aqui, o relato.

### Sobre "os quinze gabaritos" — 29/08/2026

O documento antigo falava em quinze, fixos. **A varredura de 29/08/2026 nas peças
publicadas mostrou outra coisa:**

| peça | gabaritos | quais |
|---|---|---|
| casa ITTB | 8 | capa, cheia, divisor, duo, mapa, marca, planta, prancha |
| AMAZ R1 | 20 | camadas, casos, cheia, dado, divisor, donut, duas, fim, frase, grelha, janela, lista, logo, marca, meio, mosaico, pergunta, planilha, socio, tabela |
| tokyo · centro | 19 | os deste esqueleto |

**Só `marca` e `divisor` aparecem nas três.** Cada deck criou o vocabulário do
seu tipo de argumento: a casa ITTB é arquitetura, a AMAZ é institucional, a tokyo
é comercial. Não existe um conjunto único, e fingir que existe é o que fazia o
documento antigo descrever um sistema que já não era o que estava no ar.

**Estado em 29/08/2026, depois do teste de montagem (ainda válido em 02/09):**

| gabarito de arquitetura | no esqueleto? |
|---|---|
| `prancha` — grade de referência | ✅ portado |
| `cheia` — render em tela cheia | ✅ portado |
| `planta` — com lupa de 100 a 600% | ❌ falta a máquina da lupa |
| `desenho` — planta com dados ao lado | ❌ idem |

Enquanto `planta` e `desenho` não entram, planta e corte vão como `prancha` de
uma coluna, **sem zoom**. É a limitação mais concreta hoje.

### O que o teste de montagem mostrou — 29/08/2026

Em 29/08/2026 uma sessão montou um deck de dezesseis slides a partir de um briefing real,
usando **só o `DECK-MONTAR.md`** — sem abrir os decks publicados. Resultado:

**Quebrou em dois pontos, e os dois eram erro de documentação, não de código.**

1. **`prancha` estava listado no `DECK-MONTAR.md` e não existia no esqueleto.** O `s.cols` caía
   no `const tab` compartilhado, que espera array, e derrubava **o deck inteiro**
   com `s.cols.map is not a function`. É a armadilha do campo reservado,
   registrada em 23/08 e paga de novo. Corrigido: `prancha` foi portado, e o
   `tpl()` o trata **antes** do `tab`.
2. **`mapa` com o andaime vazio derrubava o deck.** Corrigido: vira estado vazio.

**O que funcionou de primeira:** capa, divisor, lista, tabela com `fecho` e
`nota`, fim, abertura e contracapa da marca, os passos por clique, o quadro
fixo, a cortina e o retorno ao acervo. Zero transbordo, zero `undefined`.

### 02/09/2026 — auditoria

A EMEI Presidente Dutra passa a ser a peça de referência; `casa-ittb` e
`tokyo-centro` saíram do público (peças de cliente, na área de cliente do site).
Peças antigas ficam como estão. O esqueleto sai em tela cheia, sem tarja. Lavrō e
Sarasá têm arquivo de marca e bloco. Logotipo do canto decidido por frente.
Regra de versão × revisão em `GITHUB-COMO-TRABALHAR.md`.

---

## O que este arquivo não cobre

| assunto | onde |
|---|---|
| cor, tipografia, logotipo, capa, acervo do fundo | `../marca/MARCA-<nome>.md` |
| o shader do fundo, preset a preset | `michel-stein-sistemas/deck/FUNDO-MORPH-PONTILHADO.md` |
| a capa padrão da michel stein_, receita de extração | `../marca/MARCA-MICHEL-STEIN-CAPA.md` |
| como publicar, registrar e validar no ar | `GITHUB-COMO-TRABALHAR.md`, ao lado |
| rodadas com nome de cliente, histórico por projeto | `michel-stein-sistemas/deck/` |
