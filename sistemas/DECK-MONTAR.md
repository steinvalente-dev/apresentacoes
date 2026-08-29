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
| `mapa` | mapa de lotes ou de cluster | `which` `sang` `leg` — ver `gabaritos/mapa.md` |

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

**O que isso significa na prática:** este esqueleto entrega o vocabulário
comercial. Para uma apresentação de arquitetura vão faltar `cheia`, `planta`,
`prancha` e `desenho` — que estão na casa ITTB e ainda não foram trazidos para
cá. É a pendência mais visível deste arquivo.
