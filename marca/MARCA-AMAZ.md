# marca AMAZ — a camada de marca

Documento de marca, sem dado de cliente, no repositório **público** de
apresentações. Abre por URL raw, sem token.

Companheiro do `../sistemas/DECK-MONTAR.md`, que é o motor e não sabe de que
marca é a peça. **Montar uma apresentação da AMAZ = motor + este arquivo + um
DECK.** O bloco que se cola no esqueleto é o `amaz/bloco.html`, ao lado.

> **A referência da frente é a apresentação institucional.** Decisão do Michel em
> 29/08/2026. Quando este arquivo e a `../amaz-r1/apresentacao.html` divergirem
> sobre o que a marca é, **vale o que está no R1** — e o que se faz é corrigir
> este arquivo, não a peça. Ajustes e arquivos específicos da AMAZ saem de lá.
>
> Como na michel stein_, para todo o resto **o `.md` é o mestre**: divergiu o
> desenho de uma peça nova, o `.md` ganha.

Levantado em 29/08/2026 do `amaz-r1/apresentacao.html` (26/08), do
`amaz-identidade/apresentacao.html` (23/08) e dos documentos de identidade do
Projeto AMAZ. **Nada foi inventado.** As lacunas estão nomeadas no §8.

⚠ **Risco de nome, aberto desde 23/08:** *Amazon* e *Amaze*. INPI (classes 36/37)
e domínio não resolvidos. Vale confirmar antes de investir em aplicação,
papelaria e obra.

---

## 1 · Identidade

| campo | valor |
|---|---|
| nome | `AMAZ` em texto; o wordmark é `amaz`, caixa baixa |
| descritor | `desenvolvimento` / `imobiliário`, duas linhas, Inter 400, +.005em |
| assinatura em slide | o **lockup**: wordmark + descritor + barra Cobre |
| slogan da abertura | **casas que respiram** |
| site | `www.amaz.com.br` |
| o que é | incorporação de vilas de casas em bairros consolidados de São Paulo |
| produto | casa + terreno, madeira engenheirada (MLC) / steel frame, construção modular |

**O dispositivo da marca é a barra de acento do lockup** — é o equivalente
funcional do underscore terracota da michel stein_. Está escrito no código do
R1: *"sem underscore piscante: aquilo é a assinatura do michel stein_. O
dispositivo da AMAZ é a barra de acento do lockup."*

**Símbolo: não existe e está adiado.** A marca é tipográfica. Nenhuma peça
inventa um símbolo.

*O território de slogans em estudo — "pulmão urbano", "um respiro na cidade",
"uma clareira no caos" — é do plano de marketing. Na apresentação, o que está no
ar é "casas que respiram".*

---

## 2 · Cor — os quatro papéis

A AMAZ nomeia os tokens **por papel**, não por cor. É a nomenclatura que o motor
pede, e nisso ela está à frente da michel stein_, que ainda nomeia por cor.

| papel do motor | token | hex | nome |
|---|---|---|---|
| **papel** | `--papel` | `#F4F1EA` | Papel |
| **tinta** | `--tinta` | `#06392F` | Tiber |
| **primária** | `--escura` | `#04251F` | Mata funda |
| **acento** | `--acento` | `#B95118` | Cobre |

Apoio:

| token | hex | papel |
|---|---|---|
| `--apoio` | `#D9C9A3` | Areia — apoio sobre escuro, **e fundo de matéria** |
| `--material` | `#BFA783` | Pinho — a cor medida da MLC clara. **Material, não marca** |
| `--soft` | `#06392F99` | tinta atenuada |
| `--hair` | `#06392F26` | filete |

**Dois fundos claros:** Papel é o fundo de leitura, **Areia é o fundo de
matéria**.

### A regra do acento

**O acento é definido pelo fundo, não pela marca.** Uma função, dois portadores;
nunca os dois na mesma peça.

| fundo | acento do par | o Cobre pode ser |
|---|---|---|
| Papel `#F4F1EA` | **Cobre** (4,38) | texto e grafismo |
| Areia `#D9C9A3` | **Tiber** (7,85) | só título grande e grafismo (3,02) |
| Mata funda `#04251F` | **Areia** (9,95) | só título grande e grafismo (3,30) |
| Tiber `#06392F` | **Areia** (7,85) | só grafismo — **nunca texto** (2,60) |

**Onde o Cobre entra:** barra vertical do descritor · filete de seção (~180 px em
1600×900) · marcador de item ativo, número de etapa, destaque de um dado.

**Onde não entra:** nunca em texto corrido ou bloco longo · nunca como fundo de
área grande · nunca junto de Pinho em peça pequena (dois quentes brigam) · nunca
dentro da textura da marchetaria.

### Contrastes medidos

Papel sobre Tiber 11,4:1 · Areia sobre Tiber 7,9:1 · Tiber sobre Papel 11,4:1 ·
Cobre sobre Papel 4,4:1 (texto grande apenas) · Cobre sobre Mata funda 3,3:1 ·
Cobre sobre Tiber 2,6:1.

### Para a engine do fundo morph

`{paper:'#F4F1EA', ink:'#06392F', acc:'#B95118'}`.
Versão escura: `{paper:'#04251F', ink:'#D9C9A3', acc:'#B95118'}`.

---

## 3 · Tipografia

**Duas famílias, quatro faces.**

| uso | face | pesos |
|---|---|---|
| display, títulos, slogan | **Bricolage Grotesque** (`--disp`) | 800 |
| texto, rótulo, dado | **Inter** (`--sans`) | 400, 500, 600 |

Fallbacks: `system-ui, sans-serif` para as duas.
Display com tracking negativo: −.042em no slogan, −.03 a −.04em em título grande.
Rótulo em caixa alta: Inter 600, +.15 a +.20em, sempre pequeno.

**As quatro faces vão embutidas em base64** — 83 KB. É o que faz a peça rodar sem
internet, que é requisito do motor. Estão prontas no `amaz/bloco.html`.

> ⚠ **Correção ao levantamento anterior.** A primeira versão deste arquivo dizia
> "três famílias", contando IBM Plex Mono. Errado: o `amaz-identidade` declara um
> token `--mono`, mas **não tem `@font-face` para ele** — cai no mono do sistema.
> A mono não é face de marca. Pelo mesmo motivo, Bricolage **800 só**: o 700 que
> aparecia é peso CSS sem face, sintetizado pelo navegador.
>
> **A receita do `DECK-MONTAR.md` fala em seis `@font-face`. Na AMAZ são quatro.**
> O seis é da michel stein_, que usa reto e itálico.

**Decisão em aberto:** Bricolage em *todos* os títulos pode pesar num deck longo.
A alternativa é Bricolage só na capa e nos divisores, Inter 600 nos títulos
internos. O R1 não fechou isso.

---

## 4 · O lockup

Wordmark `amaz` em Bricolage 800, com **kerning manual por par** — não é tracking
uniforme: `a→m` −.072em · `m→a` −.1255em · `a→z` −.1015em. Proporção de tinta
**4,178 : 1**. O SVG entregue já tem os valores aplicados (IoU 0,99 contra o
original) e está colável no `amaz/bloco.html`, herdando cor por `currentColor`.

Descritor alinhado pela esquerda do wordmark. **A barra Cobre fica fora da caixa,
à esquerda** — é o único elemento que sangra para a margem.

### Quatro níveis de escala

O descritor **não escala junto** com o wordmark. Seja **W** a largura de tinta do
wordmark e **k** o corpo do descritor em fração de W:

| nível | largura do wordmark | k | descritor | quando |
|---|---|---|---|---|
| **Micro** | < 20 mm · < 90 px | — | **sem descritor** | favicon, avatar, marca d'água, carimbo |
| **Compacto** | 20–65 mm · 90–260 px | .105 | duas linhas | cartão, papelaria, placa pequena |
| **Padrão** | 65–250 mm · 260–1000 px | .085 | duas linhas | uso geral, slide, capa de proposta |
| **Herói** | > 250 mm · > 1000 px | .068 | duas linhas | fachada, placa de obra, hero de site |
| *uma linha* | qualquer | .105 | `desenvolvimento imobiliário` | assinatura de e-mail, rodapé estreito |

Piso de leitura: **9,5 px em tela, 6 pt em impresso**. Abaixo disso o descritor
sai — não encolhe.

Construção, tudo em função do corpo do descritor **FS** (= k · W): espaço
wordmark→descritor .45·FS · entrelinha 1,05·FS · largura da barra .27·FS · espaço
barra→texto .47·FS · barra sai .72·FS à esquerda · altura da barra = altura de
tinta do bloco de duas linhas.

**Área de proteção sobre textura:** folga **1 H** (H = altura de tinta do
wordmark), módulo da textura **≤ H ÷ 4**; acima disso, campo chapado sob a marca.
Sobre chapado a folga não foi medida — ver §8.

*Leitura minha, a confirmar: no R1 o `.desc` está com `display:none`, ou seja o
deck roda o wordmark sozinho, sem descritor. Se isso foi decisão, vira regra
aqui; se foi acidente, é conserto na peça.*

---

## 5 · A abertura e a contracapa

**Abertura** — gabarito `marca`, fundo Mata funda, vídeo de fundo em sangria:

1. **Lockup** no alto à esquerda, em Papel.
2. **Slogan** `casas que respiram`, Bricolage 800, `clamp(30px,5.6vw,112px)`,
   −.042em, uma linha.
3. **Site** `www.amaz.com.br` em Inter 400, `clamp(10px,.78vw,15px)`, +.14em.
4. **Pílula `começar →`** em Cobre. Convida a entrar; o clique chama `avanca()`.

**Sem underscore piscante.** É a assinatura da outra marca.

**Contracapa** — mesmo bloco, com `assina:'obrigado'` no lugar do slogan e sem a
pílula. **Sem QR** — o QR é da michel stein_, e o destino da AMAZ não está
decidido.

Os dois objetos do `DECK` estão no `amaz/bloco.html`.

**Variante de capa aprovada:** capa em **recorte** — imagem filtrada sangrando na
prancha inteira com o wordmark vazado em Papel. Mais forte, consome a prancha
toda; usar quando a capa não precisar carregar texto.

---

## 6 · Fundo, vídeo e fotografia

**A regra do acervo existe: as peças são empreendimentos da AMAZ, nunca portfólio
de terceiros.** As imagens é que não existem ainda.

O R1 usa **vídeo de fundo**, não carrossel morph: `<video data-v>` com o binário
em base64 na página, WebM VP9 com queda para MP4. **Toca só o vídeo da prancha
ativa** — os três tocando juntos derrubavam a taxa de quadros do deck inteiro
(mediana 134 → 49 ms, medido em 24/08).

**Fotografia:** toda imagem passa por um dos filtros LUT `.cube` 33³ da família —
`amaz-mata` (natureza, material, obra), `amaz-hora-dourada` (gente, convívio),
`amaz-mata-suave` a 45% (imagem que já é da paleta), `amaz-mata-video`. Limite: o
filtro empurra cor que já existe; em imagem sem verde nem laranja vira tingimento
pobre. É direção de arte, não conserto.

**Mecanismo "janela":** o wordmark vira máscara sobre imagem ou vídeo. Só funciona
com desvio padrão de luminância **σ ≤ ~40** — acima disso os contraformas do "a"
fecham. Sobre Tiber a textura precisa contrastar em valor: madeira clara funciona,
folhagem escura desaparece. **Nunca janela sobre textura.**

---

## 7 · Marchetaria — o grafismo

Textura generativa: uma grelha cobre a peça, cada bloco é um pedaço de madeira
serrado com veio próprio, sorteado a partir de uma **semente** — mesma semente,
mesmo desenho, em qualquer máquina. Guarda-se a semente, nunca a imagem. O
mecanismo: **os anéis pertencem ao vértice da grelha, não à célula**, então a
família de anéis atravessa a junta e as figuras emergem do encontro das peças.

**Nenhum matiz novo:** os tons de bloco são a própria paleta em opacidade sobre o
fundo. **Cobre não entra na textura** — só no tipo.

**Entra:** capa e abertura · divisor · fundo de peça institucional · superfície de
apoio.
**Não entra:** atrás de texto corrido, tabela ou gráfico · dentro das letras ·
atrás de fotografia · em peça pequena · animada · impressa em uma cor sem
adaptação.

**Uma peça tem um mecanismo de superfície só:** foto filtrada, *ou* marchetaria,
*ou* cor chapada.

**Movimento é da janela.** A marchetaria é superfície parada, por medição.

> ⚠ **Estado real: desligada.** Foi retirada do R1 em 24/08 — *"o porte não
> reproduziu o campo do documento e o Michel vai investigar a fonte"*. O gerador
> (`marchetaria()`) e o CSS (`canvas.march`) continuam no arquivo; religar é
> devolver o canvas àquela linha. **Enquanto isso, a marchetaria é identidade
> escrita e não é peça no ar.**

Especificação técnica — gramática, as **seis** regras de sorteio, escala absoluta,
receita de cor dos quatro pares, custo medido: `amaz-grafismo/apresentacao.html`,
e os geradores em `amaz-marchetaria/tabuas.html` e `campo-quadrado.html`.
Receita do par Areia: fundo `#D9C9A3` · madeira A Mata funda 8,5% · B 2% · veio
40% · junta 17%. Juntas dos outros pares: Mata funda 13% · Papel 16% · Tiber 14%.

---

## 8 · O que falta — e não deve ser inventado

Contra o checklist do `MARCA-MICHEL-STEIN.md`:

| item | estado |
|---|---|
| 1 · nome, assinatura, site | ✅ |
| 2 · os quatro papéis de cor | ✅ com contrastes medidos |
| 3 · as faces, com peso por uso | ✅ duas famílias, quatro faces, embutidas |
| 4 · a abertura | ✅ §5 |
| 5 · a contracapa | ✅ §5 |
| 6 · o acervo do fundo | ⚠️ a regra existe, as imagens não |
| 7 · o que é intocável | ✅ **o acento é definido pelo fundo, não pela marca** |

Aberto, e é decisão do Michel e dos sócios:

1. **Área de proteção sobre fundo chapado** — não medida. Sobre textura já existe.
2. **Lista de usos proibidos** do logotipo — não existe (não distorcer, não
   recolorir a barra, não trocar o descritor, não inventar símbolo…).
3. **Acervo de fundo** — imagens e vídeos dos empreendimentos da AMAZ. Hoje as
   referências disponíveis são preview de Pinterest em baixa e uma foto com marca
   d'água Unsplash+. **Não licenciadas.**
4. **Descritor no deck** — ligado ou desligado (§4).
5. **Bricolage em todos os títulos** vs. só capa e divisores (§3).
6. **Escala tipográfica** — o R1 tem a sua (`--fs-mega/big/h/item/body/cap/num`),
   o esqueleto tem a dele. Não foram conciliadas. Como o R1 é a referência da
   frente, o provável é a escala dele subir para o esqueleto — mas isso é rodada
   própria, não se resolve de passagem.
7. **Marchetaria** — reproduzir o campo do documento e religar, ou aposentar.
8. **Validação com Eduardo Eid e Adriano Carvalho** — a paleta é escolha do
   Michel, ainda não do grupo.
9. **INPI e domínio** — o `www.amaz.com.br` está escrito na peça e não está
   confirmado como registrado.

---

## 9 · O vocabulário de gabaritos da AMAZ

O esqueleto tem dezenove gabaritos, vindos do deck comercial da tokyo. **O R1 usa
vinte, e só `marca`, `divisor`, `frase`, `lista`, `cheia`, `tabela` e `fim` são
comuns aos dois.**

Do R1, em 56 pranchas: `frase` ×18 · `divisor` ×8 · `dado` ×6 · `meio` ×3 ·
`socio` ×3 · `marca` ×2 · `mosaico` ×2 · `casos` ×2 · e um de cada:
`pergunta`, `planilha`, `camadas`, `logo`, `janela`, `cheia`, `donut`, `grelha`,
`tabela`, `duas`, `lista`, `fim`.

Os nove que **não existem no esqueleto** — `dado`, `meio`, `socio`, `mosaico`,
`casos`, `pergunta`, `planilha`, `camadas`, `logo`, `janela`, `donut`, `grelha`,
`duas` — são o vocabulário institucional da AMAZ, e é onde está o trabalho de
portar. `donut` (dois anéis do ACV, desenhados por código, valores vindo do
`DECK`) e `janela` (o wordmark como máscara sobre vídeo) são os dois que carregam
argumento próprio da incorporadora.

**Enquanto não forem portados, montar peça AMAZ pelo esqueleto perde esses
gabaritos.** É a limitação mais concreta hoje — junto com `planta` e `desenho`,
que dependem da máquina da lupa e faltam para todo mundo.
