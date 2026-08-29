# marca michel stein_ — a capa

Documento de marca, sem dado de cliente, no repositório **público** de
apresentações. Abre por URL raw, sem token.

Companheiro do `MARCA-MICHEL-STEIN.md`, ao lado. Trata de **uma coisa só**: o
slide de abertura de toda apresentação da michel stein_.

É **conteúdo de marca**, não de motor — outra marca tem a sua própria capa, e o
motor não sabe a diferença. Criado em 21/08/2026 com arquivo próprio, para ser
revisado sem mexer no sistema inteiro; movido para a camada de marca em
29/08/2026.

---

## ⚑ A REGRA

**Toda apresentação abre pelo mesmo slide.** Não se inventa capa nova, não se
adapta ao tema do projeto, não se troca a cor. É a marca — nome, papel, slogan,
site — sobre o carrossel morph, em fundo oliva.

O nome do projeto **não** entra aqui. Ele vem no slide seguinte, no gabarito
`capa`.

Quando o Michel pedir "coloca a capa", é **este** slide.

---

## DE ONDE VEM

**Em `../modulos/`, neste mesmo repositório público.** Migrado do Google Drive
em 22/08/2026 — os originais foram para `00-CLAUDE › 00-OBSOLETOS` e não valem
mais como fonte.

| arquivo | o que é |
|---|---|
| `../modulos/capa-morph.html` | **a capa vigente.** 561.350 bytes, nove peças no carrossel. Roda sozinho no navegador. |
| `../modulos/ms-fundo-engine.js` | a engine do morph, isolada. 14.526 bytes. |
| `../modulos/fundo-morph-pontilhado.html` | o laboratório do fundo, com os controles. Não é a capa. |

> **Havia uma segunda cópia destes três arquivos** no repositório privado, em
> `deck/modulos/`, parada na versão de três imagens e 423.077 bytes. Este
> documento chegou a citar aquela como vigente. **Apagada em 29/08/2026** — a de
> cá é a única. Comportamento que precisa mudar em todas as peças ao mesmo
> tempo é servido, não soldado, e por isso mora num lugar só.

> **Acabou o número de revisão.** Não existe mais R6, R7, R8: o arquivo é o
> vigente, e o anterior está no histórico do Git, com data e diferença linha a
> linha. Nunca criar `capa-morph-R2.html` ao lado — editar no lugar.

> **O arquivo não passa pelo texto da conversa.** Ler e escrever é pela API de
> conteúdos do GitHub, em base64, direto do disco. Em 22/08 uma tentativa de
> transportar a engine pelo conector do Drive trocou `uv+pxA` por `uv*pxA` e
> quebraria a paralaxe em silêncio — passava no `node --check`. **Sempre
> conferir o tamanho em bytes contra a origem depois de subir.**

---

## COMO EXTRAIR (receita, para não redescobrir)

O `capa-morph_R<n>.html` é autossuficiente: fontes, engine e imagens em
base64, tudo num arquivo. Para levar a capa para dentro de um deck, tirar
**quatro coisas**:

### 1 · a engine

Do `window.MSFundo=(function(){` até `return {montar:montar};\n})();`.
São ~13 KB. **É byte a byte igual ao `ms-fundo-engine.js` da mesma pasta**,
tirando o comentário de cabeçalho — conferido em 21/08/2026. Dá para usar
qualquer um dos dois.

Preset embutido, chamado **"linha MS"**:

```js
const P={trans:2,cur:3,mode:0,fit:1,dot:4.5,angle:22,angle2:32,bleed:.42,
  contrast:.65,gamma:1.45,amp:.08,edge:1.0,speed:.30,zoom:.01,accent:0,
  grain:0,vig:.86,mforce:.46,mrad:240};
const INK=hex('#0e0f0b'),PAPER=hex('#6B6A4B'),ACC=hex('#B85C38'),SCALE=0.9;
```

### 2 · o carrossel

O array passado a `MSFundo.montar(canvas, IMGS)`. São **nove data-URI JPEG de
1024 px** — renders de projeto do próprio Michel, ~72 KB cada. (A versão de três
imagens é anterior a 22/08/2026 e não vale mais.)
Extração:

```python
i = s.index("MSFundo.montar(document.getElementById('gl')")
arr = s[s.index('[', i) : s.index(']', i) + 1]
imgs = re.findall(r'"(data:image/[^"]+)")', arr)
```

**O carrossel é dele, não é decoração intercambiável.** Não substituir por
fotos do projeto que está sendo apresentado.

### 3 · a marcação

```html
<div class="frase">
  <div class="sigla-mini">michel stein<i>_</i><em>arquiteto</em></div>
  <div class="slogan">a mão por trás do traço<i class="pisca">_</i></div>
  <div class="site">www.michelstein.com.br</div>
  <button class="start">começar <span class="seta">→</span></button>
</div>
```

### 4 · a cortina

`#cortina` — painel creme, fio terracota nas duas bordas, `skewX(-14deg)`.
Varre na **saída** da capa, nunca na entrada. Sequência: `on` aos 0 ms,
troca escondida aos 580 ms, `sai` aos 660 ms, reset aos 1340 ms.

---

## A ESPECIFICAÇÃO

Fundo oliva `#6B6A4B`, texto creme `#EDE6DA`, underscore terracota `#B85C38`.
Bloco encostado à esquerda em `--gut-in: clamp(38px,8vw,190px)`, centrado na
vertical. Quatro linhas no mesmo eixo, `gap: clamp(9px,1.35vh,20px)`.

| linha | tipografia |
|---|---|
| `michel stein` + `_` | DM Mono **500 itálico**, `clamp(11px,1.0vw,20px)`, caixa-baixa, `letter-spacing:-.01em` |
| `arquiteto`, ao lado | DM Mono **400 reto**, `.68em`, `letter-spacing:.02em`, **caixa-baixa**, cor `--muted` |
| **a mão por trás do traço** + `_` | DM Mono **500 itálico**, `clamp(22px,3.75vw,82px)`, `letter-spacing:-.028em`, `line-height:1.04`, `white-space:nowrap` |
| `www.michelstein.com.br` | **Inter 400**, `clamp(10px,.78vw,15px)`, `letter-spacing:.14em` |

Pílula: terracota, `border-radius:999px`, `font-size:var(--fs-cap)`,
`letter-spacing:.16em`, padding `clamp(7px,.85vh,11px) clamp(14px,1.35vw,22px)`.
Texto **"começar"** e a seta. No hover, `translateY(-1px)` e o gap abre de
`.6em` para `.95em`.

Underscore do slogan pisca em `1060ms step-end infinite`.

Entrada do texto escalonada: `.06s`, `.16s`, `.28s`, `.42s`.

Abaixo de 620 px o slogan solta o `nowrap` e quebra em `max-width:20ch`.

---

## ARMADILHAS JÁ PAGAS

**O respiro entre `michel stein_` e `arquiteto` vem de `margin-left:1.1em` no
`<em>` — NUNCA de `gap` no flex.** O gap descola o underscore do nome. Custou
duas rodadas.

**"A mão por trás do traço" é a tagline, texto puro.** Não é uma imagem de
mão. Já se perdeu tempo procurando um desenho que não existe.

**Nem DM Mono nem Inter trazem a seta `→` (U+2192).** Com glifo de texto ela
cai para fonte de sistema e destoa. Usar SVG inline:

```html
<svg class="seta" viewBox="0 0 16 10"><path d="M0 5h13.4M9.6 1l4 4-4 4"
  fill="none" stroke="currentColor" stroke-width="1.4"
  stroke-linecap="round" stroke-linejoin="round"/></svg>
```

**A capa não mostra chrome.** Nem seção, nem bolinhas, nem contador.
`body.na-marca .chrome{opacity:0;pointer-events:none}`.

**O morph trava o Playwright headless na configuração padrão.** Para testar,
ou rodar com `?semfundo`, ou lançar o Chromium com
`--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`.
Com SwiftShader ele renderiza — verificado em 21/08/2026.

**Subir a engine fora do caminho crítico**, em `requestIdleCallback` com
`timeout:1200`, dentro de `try/catch`. Sem WebGL2 a capa continua em oliva
chapado, que é um estado aceitável.

---

## O FECHAMENTO

Mesmo gabarito `marca`, variante de fim: **QR acima**, marca, a palavra
**obrigado** no lugar do slogan, site embaixo. Sem pílula. Fundo oliva.
QR de 29×29 módulos, `width: clamp(64px,7vw,128px)`, apontando para
`www.michelstein.com.br`.

---
