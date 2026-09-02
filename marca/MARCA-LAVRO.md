# marca Lavrō — a camada de marca

Documento de método, sem dado de cliente. Mora no repositório **público** de
apresentações para abrir por URL raw, sem token, em qualquer conversa.

Esta é a **camada de marca**: tudo o que uma peça precisa saber para sair com a
cara da Lavrō. O motor — gabaritos, quadro, revelação, chrome, validação — está
em `../sistemas/DECK-MONTAR.md`, e não sabe de que marca é a peça.
**Montar uma apresentação = motor + esta marca + um DECK.**

**Este arquivo não é o mestre.** O mestre é o
`lavro/01-MARCA-normativo.md`, ao lado — o documento normativo da marca, v1.6
de 02/08/2026, canônico no repositório da Lavrō (`01_MARCA_Lavro.md`) e
versionado no git. Este aqui é o **recorte de deck** dele: o que o motor
precisa, na ordem em que o motor pergunta. Divergiram, **o normativo ganha**.

| ao lado | o que é |
|---|---|
| `lavro/01-MARCA-normativo.md` | o mestre. Conceito, wordmark, símbolo, cor, régua, gradiente, azulejo, proibições |
| `lavro/02-DESIGN-SYSTEM.md` | a camada de interface: tokens, componentes, densidade, movimento |
| `lavro/03-styleguide.html` | o styleguide vivo. **Nunca vence** — se divergir do design system, está velho |
| `lavro/manual.html` | o manual visual, derivado do normativo. Datado de 01/08, um dia antes da v1.6 |
| `lavro/bloco.html` | **o que se cola no esqueleto.** Abre sozinho, sem internet |
| `lavro/wordmark.svg` | o wordmark em contorno, 2 KB |

---

## 0 · O que a Lavrō é

Lavrō é o **livro de registro do empreendimento** — da decisão de projeto ao dia
de obra. Plataforma SaaS multi-tenant; o Baraka RDO é o primeiro cliente.

**Lavrar** é o verbo próprio da marca: registrar de boa-fé, com autor e data.
Não é anotar, não é salvar. Quem lavra assina embaixo.

**A palavra vetada é *risco*** — em obra ela carrega perigo. Vale inclusive no
sentido de desenho: usar *traço* ou *rabisco*. E **empreendimento** é o termo
guarda-chuva; *projeto* e *obra* são as duas fases, nunca sinônimos do todo.

---

## 1 · Identidade

| campo | valor |
|---|---|
| nome | **Lavrō** — title case, com o mácron. Nunca caixa alta no logo |
| assinatura em slide | **`da decisão à prova`** — a tagline |
| em inglês | from decision to proof |
| descritor de uma linha | o livro de registro do empreendimento, do projeto à obra |
| posicionamento | prova, não versão. **Só em conversa de venda** — ver abaixo |
| site | **⚠ não decidido.** Ver §7 |
| símbolo | `L_` — **provisório**. Só onde a palavra não cabe |

A grafia muda com o contexto, e a regra é **técnica, não estilística**:

| contexto | grafia |
|---|---|
| o que nós desenhamos — slide, manual, site, copy | **Lavrō** |
| domínio, e-mail, nome de arquivo, chave de banco | `lavro` |
| registro de marca | `LAVRO` |
| título de SEO, listagem de loja | `Lavro` |

**"Prova, não versão" não serve como assinatura de slide.** Em projeto, *versão*
é revisão de prancha — legítima e obrigatória. A frase pode ser lida como "aqui
não tem versionamento", o oposto do que o módulo de projeto faz.

---

## 2 · Cor — os papéis

| papel do motor | token | hex | proporção |
|---|---|---|---|
| **papel** | `--creme` | `#F1EBDD` | institucional e acervo |
| papel, alternativo | `--bg-frio` | `#F5F6F9` | superfície clara de sistema |
| **tinta** | `--grafite` | `#0E1116` | também o fundo do modo escuro |
| **primária e acento** | `--marca` | `#0123FF` | o mesmo azul nos dois papéis |

**A Lavrō não tem quarta cor, e isso é decisão, não lacuna.** Onde a michel
stein_ tem oliva e terracota em papéis distintos, a Lavrō tem um azul só que
faz os dois. O motor pede quatro; a marca entrega três e repete o azul.

Os vizinhos, que **não são cor de marca**:

| token | hex | papel |
|---|---|---|
| `--marca-escuro` | `#5B6BFF` | o mesmo azul, sobre escuro, **quando a leitura se prejudicar** |
| `--azul-fundo` | `#0016C7` | superfície de marca em tela cheia, no escuro |
| `--azul-claro` | `#7C8BFF` | **acento de interface** no escuro. Nunca marca |

> **Não usar `#7C8BFF` na marca.** É o acento de interface no modo escuro, e
> faz a marca parecer um botão.

Sobre fundo claro o `#0123FF` atende em qualquer tamanho — 7,8:1 contra branco.
Sobre grafite ele dá 2,4:1: não fica ilegível em display grande, fica
**encardido**, e aos 15px fica ilegível de fato. Daí o valor alternativo.
O que falha no escuro é **traço fino e texto**, não preenchimento: branco sobre
`#0123FF` dá 7,8:1 em qualquer fundo.

**Limite do creme:** sobre ele o tint de `--atencao` quase desaparece — mesma
família de matiz. Tolerável num acervo de documentos, **grave numa tela de
obra**. Creme não é superfície de trabalho com muito status.

---

## 3 · Tipografia

| uso | face |
|---|---|
| marca e títulos | **Space Grotesk** 700 / 600 |
| corpo e interface | **Inter** 400 / 500 / 600 |
| dado e etiqueta | **IBM Plex Mono** 500 |
| serifa do pacote | **Fraunces** 400, romano e itálico — variável, eixos `opsz 144 · SOFT 40 · WONK 1` |

**São oito faces, não seis.** A Lavrō tem quatro famílias, e a Fraunces sozinha
responde por 171 KB dos 287 KB do bloco. **Deck que não usar serifa deixa as
duas Fraunces de fora.** Todas SIL OFL — embutir em base64 é permitido.

**Só o display troca** no tier pago: é a métrica do corpo que governa quebra de
linha e ritmo vertical, e trocá-la desmonta o layout. A Fraunces é display,
nunca corpo. **Montserrat não é fonte da Lavrō** — é uma das opções de display
do tier pago, para o cliente que quiser a cara mais próxima da Baraka.

Auto-hospedagem é obrigatória. Depender da fonte instalada no dispositivo é
risco de identidade.

---

## 4 · Abertura — gabarito `marca` com `frase:true`

**⚠ Proposta, não decidida.** O normativo não especifica slide de abertura de
deck — ele norma a marca, não a peça. O que está abaixo é o que se deduz das
regras que existem. Michel confirma ou corrige, e então isto vira regra.

Um bloco só, no eixo `--gut-in`, de cima para baixo:

1. **O wordmark `Lavrō`** pequeno, Space Grotesk 700, com a barra construída —
   nunca o glifo `ō`. O "o" **e** a barra em `#0123FF`; as demais letras na cor
   do texto.
2. **A tagline** `da decisão à prova`, Space Grotesk 700, `clamp` de uma linha
   de fora a fora.
3. **O site** em Inter 400, pequeno, com tracking. ⚠ Depende de §7.
4. **Pílula "começar →"** em `--marca`, ligada por `comecar:true`.

**O símbolo `L_` não entra na abertura.** Regra dura do normativo §3.5:
**símbolo e wordmark nunca aparecem juntos**, e o símbolo só existe onde a
palavra não cabe. Numa capa de deck a palavra cabe.

Liga com `frase:true` + `sigla` + `slogan` + `site`.

---

## 5 · Contracapa — gabarito `marca` com `sigla`

**⚠ Proposta, não decidida**, e **bloqueada** por §7: a contracapa da michel
stein_ leva QR, e QR precisa de destino.

Bloco único centrado na vertical: o wordmark, o site pequeno colado nele, e —
quando houver destino — o QR em módulos grafite sobre placa creme.

---

## 6 · Fundo — a Lavrō não usa o morph

O preset "linha MS" é da michel stein_: o acervo dele são os projetos de
arquitetura dele, e mostrar isso na abertura é o ponto. **Para a Lavrō não
significa nada.**

A Lavrō tem duas texturas próprias, ambas homologadas no normativo, e as duas
são regidas pela mesma lei: **o desenho varia, a matéria não**.

**O gradiente de marca** (normativo §8) — elemento gráfico e fallback de capa
quando a obra não tem foto. Quatro camadas radiais mais uma linear, com
derivação **determinística** por obra: mesma obra, mesmo gradiente, sempre.
Variante clara especificada.

**O Azulejo** (normativo §8.1b, aprovado em 02/08/2026) — padronagem generativa
com referência aos azulejos de **Athos Bulcão**. Grelha onde cada célula liga
dois cantos opostos, por diagonal reta ou por quarto de círculo. **Só linha,
sem preenchimento: é textura, não figura.** Cinco regras compositivas com
precedência, três pares fundo/traço homologados, semente determinística.

**Recomendação:** o Azulejo. É o que a Lavrō tem de mais autoral, roda offline
como SVG gerado, e o morph não sabe fazer.

**Nenhum dos dois está portado para o motor.** Hoje o esqueleto só conhece o
morph. Portar é trabalho, e é o que separa esta marca de estar pronta para
montar uma peça de ponta a ponta.

---

## 7 · O que falta decidir

Três coisas, e duas delas bloqueiam a peça:

| # | o quê | bloqueia |
|---|---|---|
| 1 | **O site.** O normativo norma a grafia do domínio e nunca diz qual é | abertura e contracapa |
| 2 | **O destino do QR** da contracapa | contracapa |
| 3 | **Portar gradiente ou Azulejo** para o motor | o fundo de qualquer peça |

E duas pendências que vêm do normativo §12, que **não bloqueiam este arquivo**
mas precisam estar escritas para ninguém tropeçar:

- **O vetor do símbolo não existe.** A geometria está definida (§3.1), o desenho
  com cotas não foi feito. Bloqueia favicon e ícone de aplicativo. O
  `wordmark.svg` ao lado é o **wordmark**, não o símbolo — e a barra dele veio
  da peça publicada, onde é animada, então está mais larga e mais alta que a
  construção em CSS. Conferir contra §2.2 antes de aplicação final.
- **O `L_` é provisório**, por não ser distintivo — há muitas empresas com um
  "L" sobre azul em tonalidade próxima. Fica cravado para desbloquear favicon,
  com a intenção declarada de buscar algo mais marcante se houver necessidade
  real. **Não investir em aplicação cara sobre ele:** fachada, relevo, brinde,
  bordado, sinalização física.

---

## 8 · O que é intocável

O equivalente ao "o underscore é sempre terracota" da michel stein_.

> **Sobre creme, o mácron vai em azul.** Sem ele, a marca em creme e preto
> parece de outra empresa.

É o ponto em que a identidade ganha da conveniência, e é o que alguém
"corrigiria" numa rodada futura. **Não corrigir.**

Junto com ele, quatro regras que não se negociam:

1. **O azul não aponta para si mesmo.** Quando ele é o fundo, o acento inverte
   para branco. E superfície de marca só em tela de permanência curta — login,
   splash, assessor de IA, confirmação, onboarding. **Nunca em tela de
   trabalho**: azul saturado é substrato ruim para leitura longa e compete com
   verde, âmbar e vermelho de status, que num app de obra carregam significado
   operacional.
2. **Sombra é repouso, brilho é significado.** Nada brilha por ser azul. Brilho
   — `filter`, aura, halo — é reservado a estado com significado: a barra em
   execução, o indicador de dado ao vivo. Elemento parado usa sombra.
3. **Topo reto e régua andam juntos.** São um componente, não dois tokens. Topo
   reto sem régua parece corte acidental. E a régua só marca superfície que
   carrega decisão ou registro assinado — RDO, ata, marco, alerta. Não todo
   card; sem esse critério, vira listra.
4. **Círculo completo nunca**, no Azulejo. O círculo fechado é o símbolo, e
   deixá-lo aparecer no fundo por acaso gasta o único lugar em que ele
   significa algo.

---

## 9 · Proibições

Do normativo §11, o que morde numa peça:

- **No logo**, não substituir a barra construída pelo glifo `ō`. Em texto
  corrido, ao contrário, o glifo `ō` é o correto.
- Não deixar a barra encostar no "o". Não usar caixa alta no logo.
- Não aplicar o azul da marca sobre superfície de marca.
- Não colorir só a barra, deixando o "o" na cor do texto — falha na redução.
- Não usar o símbolo abaixo de 24px sem engrossar a barra para 0,14em.
- **Não usar o símbolo ao lado do wordmark.**
- Não usar gradiente aleatório ou variável entre carregamentos.
- Não usar creme como superfície de trabalho com muito status.

---

## 10 · Nota de contexto — coincidência de mercado

**nōvi** (`novi.cc`), estúdio brasileiro de cultura de aprendizagem
corporativa, usa **mácron sobre o "o"**, fundo creme, azul elétrico como
acento, botão em pílula e painel modular geométrico — cinco pontos de encontro
com a Lavrō.

**Avaliação registrada no normativo §13: aceitável.** Setor distinto, nomes
diferentes, e os elementos coincidentes são idioma corrente de design, não
propriedade deles. Não é conflito de marca, é repertório compartilhado. Antes
de depositar, vale busca de anterioridade com advogado, olhando elemento
figurativo além do nominativo.

**O que de fato diferencia a Lavrō** não é afastamento cosmético do mácron — é
o **registro instrumental**: mono no dado, notação de cota, tabular-nums,
régua, folha de especificação. Essa é a camada a proteger.

---

## 11 · Estado

**A peça `lavro/apresentacao.html` que está no acervo é de outra geração.**
Publicada em 23/08/2026, 15 telas, ela **não foi montada no motor** — não tem
`DECK`, não tem gabaritos, tem engine própria. É anterior ao
`deck-esqueleto.html`, que nasceu em 29/08. Ela serviu como levantamento dos
tokens desta marca e serve como referência visual; **não serve como ponto de
partida para a próxima peça**. A receita continua valendo: partir do esqueleto,
nunca do HTML de outra peça.

**A identidade Lavrō está decidida e não está implementada no app.** O app no ar
não se parece com o `03-styleguide.html`. A ordem de execução prevista está na
seção 14 do normativo.
