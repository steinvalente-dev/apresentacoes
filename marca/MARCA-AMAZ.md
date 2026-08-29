# marca AMAZ — a camada de marca

Documento de marca, sem dado de cliente, no repositório **público** de
apresentações. Abre por URL raw, sem token.

> ⚠ **Isto é um levantamento, não um manual aprovado.** Tudo o que está aqui foi
> extraído do que já está publicado — `../../amaz-identidade/apresentacao.html` e
> `../../amaz-grafismo/apresentacao.html`, de 23/08/2026 — lendo os tokens do
> `:root` e as fontes embutidas. **Nada foi inventado, e nada foi decidido aqui.**
> As lacunas estão nomeadas no fim. Escrito em 29/08/2026.

Companheiro do `../sistemas/DECK-MOTOR.md`, que é o motor
e não sabe de que marca é a peça. **Montar uma apresentação da AMAZ = motor +
este arquivo + um DECK.**

---

## 1 · Identidade

| campo | valor | de onde saiu |
|---|---|---|
| nome | `AMAZ` | caixa-alta em todo uso observado |
| o que é | desenvolvimento imobiliário — vilas de casas em bairros consolidados | da capa da peça de identidade |
| tagline | **uma clareira no caos** | da peça de identidade |
| produto | constrói com peça serrada e remontada | idem |

⚠ **Risco de nome, já registrado na própria peça:** *"Amazon e Amaze — vale
confirmar antes de investir em aplicação, papelaria e obra."* Continua em aberto.

---

## 2 · Cor — os quatro papéis

A AMAZ já nomeia os tokens **por papel**, não por cor. É a nomenclatura que o
motor pede para a troca de marca funcionar, e neste ponto ela está à frente da
michel stein_, que ainda nomeia por cor (`--creme`, `--oliva`, `--terra`).

| papel do motor | token na peça | hex |
|---|---|---|
| **papel** | `--papel` | `#F4F1EA` |
| **tinta** | `--ink` / `--tiber` | `#06392F` |
| **primária** | `--funda` | `#04251F` |
| **acento** | `--cobre` | `#B95118` |

Apoio, todos observados no `:root`:

| token | hex | papel |
|---|---|---|
| `--areia` | `#D9C9A3` | superfície quente |
| `--pinho` | `#BFA783` | superfície quente, mais fechada |
| `--ink-2` | `#4A6459` | tinta secundária |
| `--ink-3` | `#7C8C84` | tinta terciária, apoio |
| `--rule` | `rgba(6,57,47,.16)` | filete |
| `--rule-soft` | `rgba(6,57,47,.08)` | filete leve |

Três níveis de tinta é mais do que a michel stein_ tem, e resolve texto de apoio
sem recorrer a opacidade.

---

## 3 · Tipografia

| uso | face | pesos observados |
|---|---|---|
| display, títulos | **Bricolage Grotesque** (`--disp`) | 700, 800 |
| texto corrido, interface | **Inter** (`--body`) | 400, 500, 600 |
| rótulo, dado, metadado | **IBM Plex Mono** (`--mono`) | 400, 500 |

Fallbacks declarados: `"Arial Black", system-ui, sans-serif` para a display;
`system-ui, -apple-system, sans-serif` para o corpo; `ui-monospace, Menlo,
monospace` para a mono.

**As faces já vão embutidas** — quatro `@font-face` em base64 na peça publicada.
A peça roda sem internet, que é requisito do motor.

Três famílias contra duas da michel stein_. Custa mais bytes de base64; em
compensação separa dado (mono) de texto (Inter) de título (Bricolage).

---

## 4 · Layout

| token | valor | o que é |
|---|---|---|
| `--col` | `1180px` | largura da coluna de texto |
| `--wmmask` | PNG em base64 no `:root` | máscara da marca d'água, aplicada como `mask-image` |

---

## 5 · O que falta para virar camada de marca de verdade

Comparando com o checklist do `MARCA-MICHEL-STEIN.md`:

| item | estado |
|---|---|
| nome, tagline, o que é | ✅ levantado |
| quatro papéis de cor | ✅ levantados, já nomeados por papel |
| as faces, com peso por uso | ✅ levantadas |
| faces embutidas em base64 | ✅ já embutidas |
| **abertura — que elementos entram e em que ordem** | ❌ não existe |
| **contracapa — o que fecha a peça** | ❌ não existe |
| **acervo do fundo morph, ou a decisão de não usar** | ❌ não existe |
| **regras do logotipo — área de proteção, tamanho mínimo, o que não fazer** | ❌ não existe |
| **o que é intocável** — o ponto em que a identidade ganha do contraste medido | ❌ não existe |

**As cinco lacunas são decisão do Michel e dos sócios, não minha.** A michel
stein_ tem as cinco resolvidas porque foram decididas uma a uma ao longo de
agosto; a AMAZ tem a paleta e a tipografia, que é a metade que se lê no código.

**O grafismo da marchetaria** — `../../amaz-marchetaria/tabuas.html` e
`campo-quadrado.html` — é material de marca e ainda não está descrito aqui.
Provavelmente é ele que responde "o que é intocável".
