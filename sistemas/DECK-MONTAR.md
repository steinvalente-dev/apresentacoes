# deck — o que se lê para montar

Documento de método, sem dado de cliente, no repositório público. Abre por URL
raw, sem token:
`https://raw.githubusercontent.com/steinvalente-dev/apresentacoes/main/sistemas/DECK-MONTAR.md`

**Este é o arquivo curto.** Criado em 29/08/2026, partindo o `DECK-MOTOR.md`, que
misturava três ocasiões de leitura num arquivo só de 9.300 tokens: montar,
consultar um gabarito específico, e entender quando algo quebra. Só a primeira
acontece toda vez.

**A máquina (03/09/2026):** montar uma peça é preencher um `deck.json` e rodar
dois comandos — `python3 sistemas/montar.py <slug> --marca <marca> --deck <deck.json>`
e `node sistemas/validar.mjs <slug>/apresentacao.html`. A ficha curta, com o
formato do JSON e o que fazer em cada falha, é **`DECK-JSON.md`** — para o
dia a dia é o que se lê, não este arquivo. Este arquivo é o método por trás:
o que não é negociável, de onde vêm as imagens, as armadilhas.

| você quer | leia |
|---|---|
| **montar uma peça** | `DECK-JSON.md` (a ficha) + este arquivo quando algo sair do comum |
| um gabarito com máquina própria | `gabaritos/<nome>.md` — só o que entrar na peça |
| um mapa de localização | `gabaritos/mapa-localizacao.md` · módulo em `modulos/mapa-localizacao.html` |
| uma prancha de referência | `gabaritos/prancha-referencia.md` · módulo em `modulos/prancha-referencia.html` |
| um render em tela cheia | `gabaritos/render-cheia.md` · módulo em `modulos/render-cheia.html` |
| entender por que algo é assim, ou consertar | `DECK-MOTOR.md` |
| a identidade | `../marca/MARCA-<nome>.md` |

---

## ⚑ O QUE NÃO É NEGOCIÁVEL — ler antes da receita

Sete coisas que o Michel reconhece de longe, e que **peça nenhuma decide por
conta própria**. Foram escritas aqui em 02/09/2026, depois de a peça EMEI
Presidente Dutra sair errada nas cinco primeiras. O objetivo é literal: *"diminuir a
fricção da construção desses decks, que isso seja o mais automático possível.
Você vai copiar certas informações, sem ter que criar, sem ter que verificar
muito — a verificação já está feita."*

**1 · TELA CHEIA. Sempre.** Sem tarja preta em cima nem embaixo, em monitor
nenhum. O esqueleto já sai assim desde 02/09; se aparecer letterbox, é
regressão, não escolha. A peça de referência pública é
`emei-presidente-dutra` — **abrir antes de montar** e comparar. (Até 02.09 as
referências eram `casa-ittb` e `tokyo-centro`; são peças de cliente e saíram
do público para a área de cliente do site — URLs no privado, em
`site/AREA-CLIENTE.md`. A EMEI é, de qualquer forma, a peça com a engine mais
recente.) Este
arquivo não substitui olhar peça publicada; foi o que a versão anterior
("este arquivo, e mais nada") causou.

**2 · A ÚNICA EXCEÇÃO DA TELA CHEIA É A PRANCHA DE IMAGEM.** O slide preenche
a tela, a imagem não estoura: `object-fit:contain`. Em tela de outra
proporção sobra campo de moldura nas bordas e a imagem entra **inteira**. Em
peça de arquitetura o que o `cover` cortava era desenho.

**3 · A ESCALA DE TEXTO E DE NAVEGAÇÃO É CONSTANTE.** Corpo, margem, faixa de
chrome e botão de seta saem iguais em toda peça, de toda frente. Os valores
estão no `:root` do esqueleto, calibrados na peça de origem (casa ITTB, 08/2026)
e conferidos na EMEI. **Não
recalibrar para caber conteúdo** — se não cabe, corta-se texto, não se
encolhe a tipografia.

**4 · A CAPA VEM DO MÓDULO DA FRENTE, e não se remonta.** Se a frente tem um
módulo de capa, ele é o template: copia-se, troca-se o título, e pronto.
**Ser versão provisória não é motivo para não usar** — decisão do Michel,
02/09. O chrome de laboratório do módulo (painéis de controle, dicas de
protótipo, atalhos de tecla) fica fora: o próprio módulo diz isso.

| frente | módulo de capa |
|---|---|
| Estúdio Sarasá | `modulos/capa-morph-sarasa.html` — dois momentos, ver abaixo |
| michel stein_ | `modulos/capa-morph.html` |

**A capa da Sarasá tem dois momentos, num slide só:** o momento A fica parado
na tela enquanto a sala se acomoda; o clique em `começar` traz o **título da
apresentação** no lugar do bloco institucional; o clique seguinte corre a
cortina diagonal e entra no deck. Implementação: o momento B é um `.passo`, e
a pílula chama `avanca()` em vez de `go(cur+1)`.

**5 · O GIRO DO VISOR 3D É LENTO E INDEFINIDO.** Já vem assim do
`modulos/mapa-earth-3d.html` (`VOLTA` 140 s por volta, `RAMPA` 700 ms). Não é
preferência de peça. ⚠ A rotação é integrada por `requestAnimationFrame` e
**não** por `flyCameraAround`: a API não tem campo de easing, e o `rounds`
dela — deprecated — encaixa N voltas dentro da duração, o que já produziu
4,5 s por volta em peça publicada. Ler a nota no módulo antes de tocar.

**6 · GABARITO NOVO CUJO FUNDO SEJA IMAGEM OU VISOR ENTRA NA LISTA DO
`em-imagem`**, no `go()` do esqueleto. É o que inverte o chrome e lhe dá véu
próprio. Esquecer é falha silenciosa: nada quebra, o chrome só fica
ilegível sobre a imagem. Já custou duas correções no mesmo dia.

**7 · O LOGOTIPO NO CANTO SUPERIOR DIREITO É DECISÃO DA FRENTE, escrita no
arquivo da marca** (decisão do Michel, 02.09.2026). Padrão = **texto**: `michel
stein_`, `AMAZ`, `Lavrō`. **Estúdio Sarasá = logotipo pequeno**, trocando
positivo/negativo pelo tema do slide. A sessão infere a frente pelo Projeto em
que o chat começa e lê `../marca/MARCA-<nome>.md`; a escolha vem configurada
no bloco da marca, na constante `LOGO_CANTO` (`{modo:'texto',html:'…'}` ou
`{modo:'logo',svg:'…'}`). Não decidir por peça.

---

## A receita, em seis passos

O bloco da marca (`marca/<nome>/bloco.html`) entrega **quatro trechos**, cada um
com o lugar marcado no esqueleto: as `@font-face`, o `:root`, as **constantes
da marca** e a abertura/contracapa do `DECK`. Colar os quatro é trocar a marca
inteira — desde 03/09/2026 não há mais hex escrito à mão fora do `:root`.

1. Abrir `esqueleto/deck-esqueleto.html`. **Não partir do HTML de outra
   peça** — vem com a marca e o conteúdo dela junto. Módulo de capa e módulo
   de gabarito são outra coisa: esses **são** para copiar (§4 acima).
2. Colar as `@font-face` do bloco no lugar marcado. **Quantas depende da
   marca:** michel stein_ seis, Sarasá quatro, AMAZ quatro, Lavrō oito.
3. Colar o `:root` do bloco. São **nove tokens, com o mesmo nome nas quatro
   marcas** — `--papel --tinta --primaria --acento --escuro --acento-claro
   --f-display --f-corpo --f-mono`. **As linhas de escala não se tocam** —
   ver o item 3 acima, que diz por quê.
4. Colar as **constantes da marca** (logo abaixo do `DECK`, antes de
   `const palco`): `LOGO_CANTO` (texto ou logotipo no canto — item 7),
   `LOCKUP`, `GRAFISMO`, `QR`, `UNDERSCORE`. O bloco já traz os valores
   certos da frente; não se edita.
5. Pôr a **abertura e a contracapa do bloco** nas pontas do `DECK` (gabarito
   `marca`; o bloco traz o trecho pronto), e apontar `CAPA_IMGS` para o
   acervo da marca; `DIV_IMGS` para as imagens deste projeto, ou vazio.
6. Escrever o miolo do `DECK`.

⚠ **O que os tokens não trocam:** a postura tipográfica (itálico, caixa-baixa
nos títulos e no slogan) continua sendo a da michel stein_ no CSS do motor. A
EMEI resolveu isso com um bloco de CSS próprio da Sarasá. Enquanto não houver
decisão (tokens de postura ou um quinto trecho "CSS da marca" no bloco), peça
Sarasá/AMAZ/Lavrō copia esse bloco da EMEI. Pendência registrada no
DECK-REGISTRO (privado).

**A engine abaixo do `DECK` não se toca.** Blocos:
`../marca/michel-stein/bloco.html` · `../marca/sarasa/bloco.html` ·
`../marca/amaz/bloco.html` · `../marca/lavro/bloco.html`.

**O que o `tpl()` faz quando algo falta:** gabarito que não existe vira um
slide hachurado "gabarito desconhecido: <nome>"; campo obrigatório ausente vira
"gabarito X: falta Y". Os dois escrevem `console.error`. Nada quebra em
silêncio — se o slide saiu hachurado, a mensagem diz o quê.

---

## Os gabaritos do esqueleto

Implementados e testados no esqueleto. Não existe conjunto fixo: cada tipo de
argumento criou o seu, e a lista é a do código (histórico em `DECK-MOTOR.md`).

Tabela gerada por `sistemas/gerar-gabaritos.py` a partir do `tpl()` do esqueleto — não editar à mão; rodar o script.
<!-- GABARITOS:INICIO -->
Tabela gerada por `sistemas/gerar-gabaritos.py` a partir do `tpl()` do esqueleto — não editar à mão; rodar o script. Campos em **negrito** são obrigatórios (`EXIGE`): sem eles o slide vira aviso. O número entre parênteses é a aridade de cada item (`itens:[[a,b]]` = 2). Campos gerais (`sec kick t sub esc terra trama fundo div cel nota sang fecho pre largo`) valem em todo gabarito e não se repetem aqui.

**Estrutura**

| gabarito | o que é | campos próprios |
|---|---|---|
| `marca` | abertura e contracapa. Vêm do bloco da marca, não se inventam | `assinatura` · `credito` · `descritor` · `lockup` · `papel` · `pe` · `pisca` · `qr` · `sigla` · `site` · `slogan` |
| `capa` | nome do projeto, endereço e três metas | `metas` |
| `divisor` | abre seção e ganha um ponto no chrome | `dn` · `ds` · **`dt`** |
| `fim` | próximos passos. É o que o cliente leva embora | **`itens` (2)** |
| `sumario` | o argumento inteiro em blocos, logo depois da capa | **`itens` (3)** |

**Texto**

| gabarito | o que é | campos próprios |
|---|---|---|
| `frase` | uma ideia por tela, tipo grande | — |
| `jogadas` | duas ou três jogadas numeradas, com apoio longo | **`itens` (3)** |
| `trio` | três blocos curtos lado a lado | **`itens` (2)** |
| `lista` | itens numerados, entram por clique | **`itens` (2)** |
| `duasfrentes` | o pacote se fechando; caixa que cresce a cada item | **`dir`** · `dirfora` · **`esq`** · `esqfora` |

**Dado**

| gabarito | o que é | campos próprios |
|---|---|---|
| `unit` | números-chave com apoio no ponteiro | **`cards` (5)** |
| `porte` | tabela de faixas | `alto` · **`cols`** · `iso` · **`linhas`** · `meia` · `nota2` · `troca` |
| `tabela` | comparação | **`cols`** · **`linhas`** |
| `plug` | diagrama de encaixe | **`ancoras`** · `rodape` |
| `players` | atores do mesmo mercado, em faixas. `casas`, não `cols` | **`casas` (5)** |
| `avulso` | preço por frente, dentro e fora do pacote | **`grupos`** |

**Imagem**

| gabarito | o que é | campos próprios |
|---|---|---|
| `cheia` | o render em tela cheia. É o padrão para render — ver `gabaritos/render-cheia.md` | `cap` · `h2` · `lbl` · `src` |
| `duo` | duas imagens lado a lado | **`figs` (4)** · **`leg`** |
| `fotos` | linha do tempo ilustrada | `cols` · **`itens`** |
| `prancha` | grade de 2 a 4 imagens sobre um tema. Retrato 3–4 colunas, deitada 2. `cols` aqui é NÚMERO — ver `gabaritos/prancha-referencia.md` | `ar` · `cols` · `items` · `top` |
| `modelo-3d` | o que o projeto é: o modelo do SketchUp, vivo. Exige modelo PÚBLICO no 3D Warehouse — `gabaritos/modelo.md` | `cap` · `h2` · `lead` · **`modelo`** · `res` |
| `earth-3d` | onde o projeto está: o globo do Google Earth, girando devagar. Só por link — `gabaritos/mapa-earth-3d.md` | `alt` · `cap` · `h2` · **`lat`** · `lead` · **`lng`** |
| `mapa` | o cadastro desenhado, com hover por lote. Exige o objeto `MAP` — `gabaritos/mapa-lotes.md` | `chave` · `hint` · `leg` (2) · `which` |
<!-- GABARITOS:FIM -->

**Campos de fecho e nota:** `sumario`, `tabela`, `players` e `porte` aceitam
`fecho` — a linha que fecha o slide, abaixo do conteúdo. `avulso`, `tabela` e
`porte` aceitam `nota`, o rodapé pequeno.

**Na dúvida, ler o gabarito no esqueleto** — `esqueleto/deck-esqueleto.html`, no
`tpl()`. O código é a fonte; esta tabela é a conveniência.

---

## De onde vêm as imagens

Três caminhos, e **a pergunta se faz antes de montar**, não depois:

1. **Michel manda pelo chat.** Chegam anexadas; ficam disponíveis na sessão.
2. **Buscar no Drive dele.** Cada projeto tem a árvore padrão; as referências
   ficam em `<projeto> › 02_Apresentação e conceito`, subdivididas em
   `00 - Fotos referência`, `01 - Croquis` e `02 - Imagens`. Render de projeto
   costuma estar em `<projeto> › 04_Imagens`.
3. **Michel cola o caminho.** Quando ele já sabe qual pasta.

**Confirmar antes de embutir.** Uma pasta de referência costuma ter mais imagens
do que entram na peça, e a seleção é dele. O certo é listar o que se achou,
propor a seleção e o agrupamento por tema, e só então montar.

**O que fazer com elas:**

| destino | largura | qualidade | peso típico |
|---|---|---|---|
| `cheia` | 2200 px | JPEG q80 | 500–650 KB |
| `duo`, `prancha` | 1800 px | JPEG q82 | 400–500 KB |
| croqui e planta | resolução nativa do recorte | JPEG q88 | — |

Vão **embutidas em base64** dentro do HTML — é o que faz a peça rodar sem
internet. Acima de ~8 MB no total, avisar: passa do limite de anexo de e-mail.

**A exceção, e quando ela vale:** peça com mais de ~15 renders passa dos 8 MB
só de imagem, e aí o base64 deixa de ser vantagem — a primeira prancha espera
por todas. Nesse caso os renders vão como **arquivo ao lado**, numa pasta
`img/` da própria peça, com `data-src` trocado no `go()` (o slide atual e o
seguinte). **Consequência que precisa ser dita ao Michel:** a peça passa a
precisar da PASTA, não só do `.html`, e se entrega por link. Feito assim na
EMEI Presidente Dutra: 24 renders, 7 MB de imagem, HTML em 266 KB.
Peça com slide `earth-3d` já se entrega por link de qualquer forma — a Maps
API recusa `file://`. Nesse caso a escolha é livre.

**Croqui: recortar todos com o mesmo retângulo**, nunca cada um no seu limite —
senão as plantas não se registram de um slide para o outro. Método no
`DECK-MOTOR.md`.

---

## Campos que valem em qualquer gabarito

| campo | efeito |
|---|---|
| `sec:'nome'` | abre seção e cria um ponto no chrome. Cinco a nove por deck |
| `kick` | o olho, acima do título |
| `t` | o título. Aceita `<br>` e `<mark>` |
| `sub` | a linha de apoio |
| `esc` | tema escuro neste slide |
| `terra` | tema acento neste slide |
| `trama` | trama de fundo |
| `fundo:true` | liga o morph neste slide |
| `div:1` | usa o canvas do divisor, não o da marca |
| `cel:1` | ajuste de composição para tela pequena |
| `nota` | rodapé pequeno do slide |
| `sang` | sangria total |

---

## Três armadilhas que mordem na hora de montar

**`cols` é campo reservado.** Quem usa `cols` tem de trazer `linhas` logo em
seguida. Um gabarito novo que use `cols` para outra coisa quebra o deck inteiro
com `Cannot read properties of undefined (reading 'map')`, e o sintoma que
aparece depois é `cur is not defined`. Foi o que aconteceu com o `players`, que
por isso usa `casas`.

**`duo` sem `leg` escreve "undefined" na tela.** E sem `ar` a coluna estica e o
`object-fit:cover` come o desenho.

**O `mapa` de lotes exige o objeto `MAP` do projeto.** Sem ele o slide vira
estado vazio — hachurado, com o título e a nota do que falta. Não derruba o deck,
mas também não desenha nada. Montar o `MAP` é levantamento, não redação.

**`mapa` é dois gabaritos com o mesmo nome.** O de localização é um embed de
satélite, sem dado e dependente de internet; o de lotes é SVG gerado de um objeto
`MAP`, roda offline e exige levantamento. Herdaram o nome em decks diferentes.
Ao pedir "um mapa", dizer qual.

**Slot de imagem vazio é recurso, não falha.** `src:''` renderiza retângulo
hachurado com o nome do slot. Dá para entregar a estrutura antes de a imagem
existir — que é como o Michel trabalha.

---

## A linha obrigatória

Última coisa antes do `</body>`, em **toda** peça publicada:

```html
<script defer src="../modulos/ms-voltar.js"></script>
```

Sem ela a peça abre sem saída: o índice abre em aba nova, e aba nova não tem
histórico. Já vem no esqueleto.

---

## Antes de entregar

```
node sistemas/validar.mjs <slug>/apresentacao.html        # tem de imprimir tudo "ok"
```

O validador faz, em ~7 segundos, o que esta lista pedia à mão: `sintaxe`
(node --check), `gabaritos` (laço do `tpl()`, nenhum aviso de gabarito
desconhecido ou campo faltando), `undefined`, `console` (zero erro),
`fontes` (≥ 4 faces em base64), `voltar` (linha do `ms-voltar.js`; ausente
com `--cliente`), `em-imagem`, `hex` (nenhuma cor à mão fora do `:root`),
`proporcoes` (uma página redimensionada em sete tamanhos — 21:9, 16:9 ×2,
16:10, 3:2, 4:3 ×2 — todos os passos revelados, transbordo e letterbox
medidos), `peso` (aviso acima de 8 MB) e `chave-maps` (aviso: peça com
`earth-3d` se entrega por link). FALHA em qualquer um = não publica. O que
fazer em cada falha está na tabela do `DECK-JSON.md`.

Peça antiga (anterior a 03/09) não passa no `hex` — tem cor à mão. Não se
reabre peça publicada para isso; o validador é para peça nova.

## A lição do teste de montagem

Em 29/08/2026 um deck de dezesseis slides montado só por este arquivo quebrou
em dois pontos — os dois eram erro de documentação, não de código (relato em
`DECK-MOTOR.md`, "Histórico do método"). O que fica:

**Rodar o laço de verificação antes de entregar**, não depois —

```js
for(let i=0;i<DECK.length;i++){ try{ tpl(DECK[i]) }catch(e){ console.log(i, DECK[i].g, e.message) } }
```

Um gabarito quebrado não quebra só o próprio slide: **derruba o deck inteiro**, e
o sintoma que aparece no console é `cur is not defined`, que não diz nada sobre a
causa.
