# deck — o que se lê para montar

Documento de método, sem dado de cliente, no repositório público. Abre por URL
raw, sem token:
`https://raw.githubusercontent.com/steinvalente-dev/apresentacoes/main/sistemas/DECK-MONTAR.md`

**Este é o arquivo curto.** Criado em 29/08/2026, partindo o `DECK-MOTOR.md`, que
misturava três ocasiões de leitura num arquivo só de 9.300 tokens: montar,
consultar um gabarito específico, e entender quando algo quebra. Só a primeira
acontece toda vez.

| você quer | leia |
|---|---|
| **montar uma peça** | este arquivo, e mais nada |
| um gabarito com máquina própria | `gabaritos/<nome>.md` — só o que entrar na peça |
| um mapa de localização | `gabaritos/mapa-localizacao.md` · módulo em `modulos/mapa-localizacao.html` |
| uma prancha de referência | `gabaritos/prancha-referencia.md` · módulo em `modulos/prancha-referencia.html` |
| um render em tela cheia | `gabaritos/render-cheia.md` · módulo em `modulos/render-cheia.html` |
| entender por que algo é assim, ou consertar | `DECK-MOTOR.md` |
| a identidade | `../marca/MARCA-<nome>.md` |

---

## A receita, em seis passos

1. Abrir `esqueleto/deck-esqueleto.html`. **Não partir do HTML de outra peça** —
   vem com a marca e o conteúdo dela junto.
2. Colar as **seis `@font-face`** do bloco da marca no lugar marcado.
3. Trocar as **quatro cores** do `:root`. As linhas de escala não se tocam.
4. Pôr a **capa e a contracapa** nas pontas do `DECK`.
5. Apontar `CAPA_IMGS` para o acervo da marca; `DIV_IMGS` para as imagens deste
   projeto, ou deixar vazio (o divisor só trama é o padrão).
6. Escrever o miolo do `DECK`.

**A engine abaixo do `DECK` não se toca.** Bloco da michel stein_:
`../marca/michel-stein/bloco.html`.

---

## Os gabaritos do esqueleto

Dezenove, implementados e testados. **Não são "os quinze"** que o documento
antigo listava — aquele conjunto é o da casa ITTB, e cada deck foi criando o seu.
Ver a nota sobre isso no fim.

**Estrutura**

| gabarito | o que é | campos próprios |
|---|---|---|
| `marca` | abertura e contracapa. Vem da marca, não se inventa | `sigla` `papel` `slogan` `site` `comecar` `fim` |
| `capa` | nome do projeto, endereço e três metas | `kick` `t` `sub` `metas` |
| `divisor` | abre seção e ganha um ponto no chrome | `sec` `dn` `dt` `ds` |
| `sumario` | o argumento inteiro em blocos, logo depois da capa | `itens` |
| `fim` | próximos passos. É o que o cliente leva embora | `itens` |

**Texto e listas**

| gabarito | o que é | campos próprios |
|---|---|---|
| `frase` | uma ideia por tela, tipo grande | `t` `sub` |
| `lista` | itens numerados, **entram por clique** | `itens` `pre` `largo` |
| `trio` | três blocos curtos lado a lado | `itens` |
| `jogadas` | duas ou três jogadas numeradas, com apoio longo | `itens` `etapas` |
| `duasfrentes` | o pacote se fechando; caixa que cresce a cada item | `esq` `dir` `fora` |

**Dado**

| gabarito | o que é | campos próprios |
|---|---|---|
| `tabela` | comparação | `cols` **+ `linhas` obrigatório** |
| `porte` | tabela de faixas | `cols` `linhas` |
| `unit` | números-chave com apoio no ponteiro | `dados` `sub` |
| `avulso` | preço por frente, dentro e fora do pacote | `grupos` |
| `players` | atores do mesmo mercado, em faixas | **`casas`, não `cols`** |
| `plug` | diagrama de encaixe | `itens` |

**Imagem**

| gabarito | o que é | campos próprios |
|---|---|---|
| `duo` | duas imagens lado a lado | `figs` **+ `leg` obrigatório** · `ar` |
| `fotos` | linha do tempo ilustrada | `itens` |
| `prancha` | grade de 2 a 4 imagens sobre um tema. **A proporção decide as colunas: retrato 3–4, deitada 2** | `top` `cols` `items` — ver `gabaritos/prancha-referencia.md` |
| **⚠ `cols` no `prancha` é NÚMERO** | em `tabela` e `porte` é array de cabeçalhos | o `tpl()` trata `prancha` antes, por isso |
| `cheia` | **o render em tela cheia. É o padrão para render** | `src` `h2` `cap` — ver `gabaritos/render-cheia.md` |
| `mapa` · localização | onde o terreno está: satélite em sangria, endereço escrito | `src` `kick` `h2` `lead` `cap` `inv` — ver `gabaritos/mapa-localizacao.md` |
| `mapa` · lotes | o cadastro desenhado, com hover por lote | `which` `sang` `leg` — ver `gabaritos/mapa-lotes.md` |

---

## O formato de cada campo composto

Os nomes não bastam: **`itens` tem formato diferente em cada gabarito**, e errar a
aridade escreve `undefined` na tela. Extraído do código, não de memória.

| gabarito | campo | formato |
|---|---|---|
| `sumario` | `itens` | `[['01','título','o apoio']]` — **três** |
| `jogadas` | `itens` | `[['01','título com <br>','o apoio']]` — **três** |
| `lista` | `itens` | `[['rótulo','o texto']]` — **dois** |
| `trio` | `itens` | `[['o número','o texto']]` — **dois** |
| `fotos` | `itens` | `[['quando','o texto, aceita HTML']]` — **dois** |
| `fim` | `itens` | `[['quando','<b>a ação.</b> O detalhe.']]` — **dois** |
| `capa` | `metas` | `[['cliente','—'],['etapa','—'],['data','—']]` |
| `tabela`, `porte` | `cols` + `linhas` | `cols:['','a','b']` · `linhas:[['rótulo','—','—']]` |
| `players` | `casas` | uma faixa por ator. **`cols` aqui quebra o deck** |
| `avulso` | `grupos` | `[['título','subtítulo',[['item','valor']]]]` |
| `duo` | `figs` + `leg` | `figs:[['rótulo','src','legenda','classe']]` · **`leg` obrigatório** |
| `prancha` | `items` | `[{src,ar,cap}]` ou `[{pilha:[{src}],ar,cap}]` |
| `duasfrentes` | `esq` `dir` | mais `esqfora` e `dirfora`, o que **não** entra no pacote |
| `unit` | `dados` | os números-chave, com `<mark class="pop">` para o apoio |
| `plug` | `ancoras` `rodape` | |
| `mapa` · lotes | `which` `sang` `leg` | mais `chave` e `hint` |

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

1. `node --check` no script extraído. Erro de sintaxe derruba o arquivo em silêncio.
2. Percorrer todos os slides e conferir que nenhum escreve `undefined`.
3. Percorrer os passos por teclado num `lista` e num `fim`.
4. Conferir que as seis faces em base64 estão no arquivo.
5. Conferir a linha do `ms-voltar.js`.

Sob o quadro fixo, transbordo não acontece por construção — a varredura de nove
tamanhos que existia virou desnecessária. A lista completa de validação, para
quando algo quebrar, está no `DECK-MOTOR.md`.

---

## ⚠ Sobre "os quinze gabaritos"

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

**Estado em 29/08/2026, depois do teste de montagem:**

| gabarito de arquitetura | no esqueleto? |
|---|---|
| `prancha` — grade de referência | ✅ portado |
| `cheia` — render em tela cheia | ✅ portado |
| `planta` — com lupa de 100 a 600% | ❌ falta a máquina da lupa |
| `desenho` — planta com dados ao lado | ❌ idem |

Enquanto `planta` e `desenho` não entram, planta e corte vão como `prancha` de
uma coluna, **sem zoom**. É a limitação mais concreta hoje.

---

## O que o teste de montagem mostrou

Em 29/08/2026 montei um deck de dezesseis slides a partir de um briefing real,
usando **só este arquivo** — sem abrir os decks publicados. Resultado:

**Quebrou em dois pontos, e os dois eram erro de documentação, não de código.**

1. **`prancha` estava listado aqui e não existia no esqueleto.** O `s.cols` caía
   no `const tab` compartilhado, que espera array, e derrubava **o deck inteiro**
   com `s.cols.map is not a function`. É a armadilha do campo reservado,
   registrada em 23/08 e paga de novo. Corrigido: `prancha` foi portado, e o
   `tpl()` o trata **antes** do `tab`.
2. **`mapa` com o andaime vazio derrubava o deck.** Corrigido: vira estado vazio.

**O que funcionou de primeira:** capa, divisor, lista, tabela com `fecho` e
`nota`, fim, abertura e contracapa da marca, os passos por clique, o quadro
fixo, a cortina e o retorno ao acervo. Zero transbordo, zero `undefined`.

**A lição para quem montar:** rodar o laço de verificação **antes de entregar**,
não depois —

```js
for(let i=0;i<DECK.length;i++){ try{ tpl(DECK[i]) }catch(e){ console.log(i, DECK[i].g, e.message) } }
```

Um gabarito quebrado não quebra só o próprio slide: **derruba o deck inteiro**, e
o sintoma que aparece no console é `cur is not defined`, que não diz nada sobre a
causa.
