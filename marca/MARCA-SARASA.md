# marca Sarasá — a camada de marca

Documento de marca, sem dado de cliente, no repositório **público** de
apresentações. Abre por URL raw, sem token.

Companheiro do `../sistemas/DECK-MONTAR.md`, que é o motor e não sabe de que
marca é a peça. **Montar uma apresentação da Sarasá = motor + este arquivo + um
DECK.** O bloco que se cola no esqueleto é o `sarasa/bloco.html`, ao lado.

> **A frente é o Núcleo de Arquitetura da Sarasá** — conservação, restauro e
> novas edificações. Não é a identidade da Sarasá inteira, que abrange muito
> mais. Decisão do Michel em 29/08/2026, a refinar em rodada própria.
>
> **A peça sai com assinatura Sarasá**, não michel stein_ emprestada. A
> concepção e a coordenação entram como **crédito discreto na contracapa** (§5).
>
> Para todo o resto **o `.md` é o mestre**: divergiu o desenho de uma peça nova,
> o `.md` ganha.

⚠ **Nota de origem — leia antes de usar qualquer número daqui.** A Sarasá **não
tem manual de marca** ao alcance: nada no Drive, nada no Notion, nenhuma peça no
acervo. Este arquivo foi levantado em 29/08/2026 de quatro fontes, e cada valor
carrega a sua:

| origem | confiança | o que deu |
|---|---|---|
| `Sarasa-logotipo-principal.svg` (oficial, servido pelo site) | **AFIRMÁVEL** | os dois fills, e toda a geometria do §4 |
| `Sarasa-logotipo-negativo.svg` (oficial) | **AFIRMÁVEL** | a regra do fundo escuro (§2) |
| **`PORTFOLIO_SARASA_2026.pdf`** (88 pp., PowerPoint 2019, 1440×810) | **AFIRMÁVEL** | a capa em campo Vinho, o grafismo de linha, a serifada, a família (§2, §5, §6, §7) |
| CSS vivo de `estudiosarasa.com.br` (`--e-global-color-*`) | **CONFIRMAR** | paleta de apoio e faces — pode ser default do tema WordPress Vamtam |
| decisões do Michel, 29/08/2026 | **DECISÃO** | papel Cal (§2), crédito (§5), escopo da frente |

**Nada foi inventado.** As lacunas estão nomeadas no §8.

> **Revisão de 29/08, mesma data.** A primeira versão deste arquivo foi escrita
> antes do portfólio e afirmava três coisas que o portfólio derruba: que a
> Sarasá é marca só de fundo claro, que não tem grafismo, e que não existe
> símbolo na casa. As três estão corrigidas abaixo, nos §2, §7 e §4.

---

## 1 · Identidade

| campo | valor |
|---|---|
| nome | `Estúdio Sarasá` em texto; o wordmark é o **lockup de duas partes** |
| lockup | `estúdio` em Ferro, condensada bold, caixa baixa · `Sarasá` em Vinho, grotesca de contraste baixo, corpo 3,76× maior |
| assinatura em slide | o lockup, dois fills sobre claro — **negativo monocromático sobre Vinho ou Ferro** (§2) |
| frase de posicionamento | **O Patrimônio Cultural vivo** |
| site | `estudiosarasa.com.br` |
| a frente | núcleo de arquitetura: conservação, restauro e novas edificações |
| crédito da peça | `CONCEPÇÃO E COORDENAÇÃO · MICHEL STEIN_`, contracapa (§5) |

**O dispositivo da marca é a inversão do acento.** Na michel stein_ o acento é
reserva de 2% — o underscore terracota. Na AMAZ é a barra Cobre, um filete. Na
Sarasá o acento **carrega o nome inteiro**: o Vinho pinta `Sarasá`, o Ferro pinta
`estúdio`. Não é ênfase, é a estrutura.

Isso não é leitura estética, é medição. O Vinho dá **8,64** sobre o papel; o
Cobre da AMAZ dá 4,38 e a terracota da michel stein_ dá 3,66 — aqueles dois são
reserva *porque não aguentam texto*. E o portfólio vai além do que o contraste
já dizia: **a capa inteira é campo Vinho**, medido em `#79232C` sobre 85,5% da
página. O Vinho não é acento com licença de campo. É a superfície da marca.

**O Estúdio não tem símbolo.** O `S` de corpo inteiro é um glifo do lockup.
Nenhuma peça o usa sozinho — e o motivo mudou depois do portfólio: não é que
inventar um símbolo seria arbitrário, é que **o `S` sozinho já é o símbolo do
Instituto Sarasá** (§8). Usar o `S` pelo Estúdio colide com a outra marca da
casa. Mesma proibição, motivo mais forte.

**Sem underscore piscante** — é a assinatura da michel stein_.
**Sem barra de acento fora da caixa** — é a assinatura da AMAZ.

---

## 2 · Cor — os quatro papéis

Tokens nomeados **por papel**, não por cor, que é a nomenclatura que o motor pede.

| papel do motor | token | hex | nome | origem |
|---|---|---|---|---|
| **papel** | `--papel` | `#F3EEE7` | Cal | DECISÃO 29/08 |
| **tinta** | `--tinta` | `#231F20` | Ferro | **AFIRMÁVEL** — fill do logotipo |
| **primária** | `--vinho` | `#79242F` | Vinho | **AFIRMÁVEL** — fill do logotipo e campo da capa |
| **acento** | `--vinho` | `#79242F` | Vinho | **é a mesma cor** — ver abaixo |

**A Sarasá não tem quatro cores, tem três.** Primária e acento são o mesmo
Vinho, e isso é a marca, não uma lacuna: a cor que carrega o nome é a mesma que
pinta o campo da capa, a abertura de seção, o item de menu ativo, o divisor e a
barra de carregamento. Escrever um quarto token seria inventar uma cor que a
marca não tem.

**Sobre o papel Cal.** O site serve `#F9F9F9`, um branco frio, vindo de
`--e-global-color-vamtam_accent_3` — quase certamente default do tema.
Consagrar um default de WordPress como superfície de peça é o acidente que este
arquivo existe para impedir. O Cal `#F3EEE7` é decisão do Michel em 29/08:
quente a 5% de saturação, na família de cal e argamassa que é o assunto da
frente, e mantém o Vinho em 8,64. **Não validado com o os sócios do Estúdio** — §8.

Apoio:

| token | hex | papel |
|---|---|---|
| `--chumbo` | `#4E4E4E` | texto secundário sobre Cal (7,21). CONFIRMAR — Vamtam |
| `--hair` | `#231F2026` | filete sobre Cal, derivado da tinta |
| `--soft` | `#231F2099` | tinta atenuada |

> ⚠ **Dois tokens do site não entram.** `#0A0909` (tarja) dá **1,22** contra a
> tinta `#231F20` — são a mesma cor, indistinguíveis. Um preto só, o do
> logotipo. E `#CCCCCC` (filete) dá **1,53** sobre Cal: some. Filete sobre claro
> é tinta em alfa, não cinza claro.

### As duas superfícies

**Correção.** A primeira versão dizia "a Sarasá é marca de fundo claro". O
portfólio mostra o contrário: a capa é campo Vinho inteiro, e todas as aberturas
de seção — SERVIÇOS, PREMIAÇÕES, CONSULTORIA, SUSTENTABILIDADE, REFERÊNCIAS —
são painel Vinho com título branco. A marca tem **duas superfícies, e cada uma
tem o seu portador**:

| superfície | quando | lockup | o Vinho é |
|---|---|---|---|
| **Cal** `#F3EEE7` | prancha de leitura: texto, tabela, dado, croqui | **positivo**, dois fills | tinta de destaque (8,64) |
| **Vinho** `#79242F` | capa, abertura de seção, contracapa, prancha de respiro | **negativo**, monocromático em Cal | o próprio campo |
| **Ferro** `#231F20` | tarja, rodapé, fundo de fotografia escura | **negativo**, monocromático em Cal | ausente |

A regra que amarra as três: **o Vinho nunca aparece sobre o Vinho, e nunca sobre
o Ferro.** Sobre Vinho ele não tem contraste consigo mesmo; sobre Ferro dá
**1,63** e some. Nos dois casos o portador é o Cal, e o lockup vai monocromático
— que é exatamente o que o `Sarasa-logotipo-negativo.svg` oficial já é:
quatorze elementos, um único fill branco.

**O que não muda:** prancha de trabalho — a que carrega texto corrido, tabela,
mapa de danos, ficha — roda em **Cal**. Campo Vinho é gesto de abertura e de
fechamento, não superfície de leitura longa.

### Contrastes medidos

Ferro sobre Cal **14,12** · Vinho sobre Cal **8,64** · Chumbo sobre Cal **7,21**
· Cal sobre Vinho **8,64** · Cal sobre Ferro **14,12** · Vinho sobre Ferro
**1,63** (inutilizável) · Ferro sobre Vinho 1,63 (inutilizável).

Todo par utilizável passa AA e AAA para texto normal. Não há nesta paleta
nenhum par marginal — são famílias de valor bem separadas, e é por isso que ela
não tolera fundo médio.

### Para a engine do fundo morph

Clara: `{paper:'#F3EEE7', ink:'#231F20', acc:'#79242F'}`
**Vinho:** `{paper:'#79242F', ink:'#F3EEE7', acc:'#F3EEE7'}` — a capa do
portfólio levada ao motor.
Escura: `{paper:'#231F20', ink:'#F3EEE7', acc:'#F3EEE7'}`

Nas duas últimas o acento não tem portador próprio e coincide com a tinta. É a
versão negativa do logotipo levada ao fundo.

---

## 3 · Tipografia

**Duas famílias, quatro faces — e uma divergência aberta.**

| uso | face | pesos | origem |
|---|---|---|---|
| título, texto, dado | **Poppins** (`--sans`) | 400, 500, 600 | CSS vivo — CONFIRMAR |
| rótulo, metadado, crédito | **Archivo** (`--label`) | 600 | CSS vivo — CONFIRMAR |

Do CSS do site: corpo em 14 px, entrelinha 1,7em; rótulo em 12 px, 600, caixa
alta, tracking 0,5–1 px (**+.042 a +.083em**). Ambas são Google Fonts sob SIL
OFL — embutíveis em base64, que é o requisito do motor. Fallback
`system-ui, sans-serif` para as duas.

> ⚠ **A divergência, aberta por decisão.** O portfólio **não usa** Poppins nem
> Archivo em display. Os títulos e as aberturas de seção estão em uma
> **serifada didone de alto contraste** — eixo vertical, serifas em fio,
> caixa-alta generosamente espaçada — e o corpo em uma geométrica monolinear
> compatível com Poppins. A face serifada não foi identificada: o PDF saiu do
> PowerPoint 2019 e não expõe nome utilizável.
>
> **Fica em aberto de propósito.** O Michel vai montar um deck esta semana e
> decidir vendo. **Tendência declarada em 29/08: seguir a sans do site, sem
> serifa** — o argumento é que esta frente é a identidade do *núcleo de
> arquitetura*, não a da Sarasá inteira, e que isso se refina em rodada própria.
>
> Se a serifada entrar, o equivalente OFL mais próximo é **Playfair Display**, e
> o bloco passa de quatro para seis faces.

**A face do logotipo não é nenhuma das duas e não foi identificada.** Duas
consequências práticas:

1. **O logotipo entra como SVG**, não como texto — o oficial, com os valores já
   aplicados. Os dois fills são reetiquetados para `--tinta` e `--vinho` no
   `sarasa/bloco.html`; o negativo é fill único e aceita `currentColor` direto.
2. **Face de trabalho provisória**, só onde o lockup precisar ser reconstruído
   fora do SVG: **Archivo 400/500** para `Sarasá` e **Archivo Narrow 700** para
   `estúdio`. **É empréstimo declarado.** Quando o AI/EPS chegar, troca-se a
   face e a geometria do §4 continua valendo — ela foi medida do desenho, não da
   fonte.

---

## 4 · O lockup

Medido do `Sarasa-logotipo-principal.svg`. `viewBox 0 0 234 77`, catorze
elementos, dois fills. Todos os valores abaixo estão nas unidades do viewBox.

**Estrutura.** `Sarasá` em Vinho ocupa a peça inteira; `estúdio` em Ferro fica
encaixado no ombro do `S`, acima de `arasá`. O `S` é o único glifo de corpo
inteiro: y 0 → 77, largura 51,33 — **22% da largura do lockup**.

| medida | valor |
|---|---|
| altura-x de `Sarasá` | **46,97** (topo y 30,02 · base y 76,99) |
| altura-x de `estúdio` | **12,48** (topo y 11,97 · base y 24,45) |
| **proporção de altura-x** | **3,764 : 1** |
| proporção de largura total | 233,01 : 57,85 = **4,028 : 1** |
| início de `estúdio` | x 54,97 — 3,64 depois do fim do `S`, 2,59 à direita do início do `a` |
| tracking de `estúdio` | vãos 0,67 a 2,39 · média 1,57 sobre altura-x 12,48 ≈ **+0,065em** |
| acento agudo do `á` | 14,19 × 10,25, canto em x 211,96 |

### O alinhamento intocável

**O pé do acento agudo do `á` pousa exatamente na linha de base de `estúdio`.**
Os dois em **y = 24,45**, ao centésimo. Não é coincidência de arquivo: é o que
trava as duas palavras uma na outra e o que faz o lockup ler como um objeto só
em vez de duas linhas empilhadas.

Qualquer reconstrução do lockup — outra face, outro tamanho, variante de uma
linha — **valida por esse alinhamento antes de qualquer outra coisa.** Se ele
quebrar, a reconstrução está errada, ainda que tudo o mais bata.

### Quatro níveis de escala

`estúdio` **não escala junto**: abaixo do piso ele sai, não encolhe. Seja **W** a
largura do lockup; a altura-x de `estúdio` = W × 0,0533.

| nível | largura do lockup | `estúdio` | quando |
|---|---|---|---|
| **Micro** | < 130 px · < 30 mm | **sai** — só `Sarasá` | favicon, avatar, marca d'água, carimbo |
| **Compacto** | 130–300 px · 30–70 mm | presente | cartão, rodapé, papelaria, placa pequena |
| **Padrão** | 300–1000 px · 70–250 mm | presente | slide, capa de proposta, uso geral |
| **Herói** | > 1000 px · > 250 mm | presente | placa de obra, fachada, hero de site |

Piso de leitura: altura-x de `estúdio` **≥ 7 px em tela, ≥ 4,5 pt em impresso**.
É o acento agudo do `ú` que estabelece o piso — ele ocupa 4,70 unidades e é o
primeiro detalhe a fechar.

**No Micro o que fica é `Sarasá`, nunca o `S` sozinho** — o `S` sozinho é o
símbolo do Instituto (§1, §8).

**Área de proteção: não medida.** Valor de trabalho, meu, até haver manual —
folga de **½ altura-x de `Sarasá`** (23,5 unidades ≈ 10% da largura do lockup)
em todos os lados. Sobre fotografia, campo chapado sob a marca.

### Usos proibidos

Rascunhados por mim a partir da geometria, **não validados** — §8.

- Não recolorir: `Sarasá` é Vinho e `estúdio` é Ferro. Inverter, igualar as duas
  em preto "por contraste", ou pintar `estúdio` de Vinho, descaracteriza.
- Não separar as palavras nem empilhá-las como duas linhas soltas.
- Não usar o `S` sozinho — é a marca do Instituto.
- Não distorcer, condensar ou expandir — a proporção 3,764:1 é fixa.
- Não aplicar o positivo sobre Vinho nem sobre Ferro: sobre campo escuro usa-se
  o negativo monocromático (§2).
- Não pôr o lockup sobre fotografia sem campo chapado sob ele.
- Não acrescentar contorno, sombra ou brilho.
- Não trocar `estúdio` por outra palavra (`escritório`, `arquitetura`).

---

## 5 · A abertura e a contracapa

**Abertura** — gabarito `marca`, **fundo Vinho chapado**, que é o que a capa do
portfólio faz:

1. **Lockup negativo** em Cal, no alto à esquerda, nível Padrão.
2. **Grafismo de linha** (§7) correndo na base, em Cal, sangrando nas laterais.
3. **Frase** `O Patrimônio Cultural vivo`, Poppins 600,
   `clamp(28px, 5.2vw, 96px)`, tracking −0,02em, uma linha, em Cal.
4. **Site** `estudiosarasa.com.br`, Archivo 600, caixa alta,
   `clamp(10px,.78vw,15px)`, +.08em, em Cal a 70%.
5. **Pílula `começar →`** em Cal com texto Vinho. O clique chama `avanca()`.

*Variante clara aprovada:* mesma composição em campo Cal, com o lockup positivo
e a frase em Ferro com `vivo` em Vinho. Usar quando a peça abrir em leitura, não
em gesto. É decisão de peça, não de marca.

**Sem underscore piscante. Sem barra de acento.** São as assinaturas das outras
duas marcas.

**Contracapa** — campo Vinho, `assina:'obrigado'` no lugar da frase, sem pílula:

- **QR** em módulos Cal sobre Vinho, apontando para **`estudiosarasa.com.br`**.
- **Crédito**, linha pequena ao pé: `CONCEPÇÃO E COORDENAÇÃO · MICHEL STEIN_`,
  Archivo 600, caixa alta, +.08em, em Cal a 70%. Não disputa a assinatura;
  registra a autoria na peça que circula.

Os dois objetos do `DECK` estão no `sarasa/bloco.html`.

---

## 6 · Fundo e fotografia — o morph

**A regra do acervo: as imagens são obra da Sarasá.** Nunca portfólio de
terceiros, e — específico desta frente — **nunca obra da michel stein_**. Na
michel stein_ o fundo mostra os projetos dele, e mostrar isso na abertura é o
ponto; aqui a assinatura é outra e o gesto mudaria de sentido.

Formato do sistema, o mesmo das outras frentes: **nove peças, 1024 px, JPEG q68**.
Preset: `{paper:'#F3EEE7', ink:'#231F20', acc:'#79242F'}`.

**Estado: acervo provisório.** As peças montadas hoje usam obra publicada e
fotografada da Sarasá — vitral do Salão do Pregão da Bolsa do Café, casarões da
av. Higienópolis, Castelinho de Poços de Caldas / Pouso Alegre. O portfólio 2026
acrescenta um acervo grande e legendado: Theatro Municipal, Museu do Ipiranga,
Edifício Matarazzo, Estação da Luz, Cine São Luiz, Convento de Itanhaém,
Fortaleza da Barra Grande. O Michel fornece os arquivos em resolução e a
autorização; a substituição é **troca de arquivo, não de regra**.

> **Nenhum LUT nesta frente — e agora sei que estou proibindo uma prática, não
> prevenindo uma hipótese.** No portfólio, **85 das 88 páginas** carregam
> veladura de cor sobre fotografia. Vinho e ocre se defendem, são as cores da
> casa. Mas seis páginas estão em matizes que não pertencem a marca nenhuma —
> azul (p. 3), verde (p. 17), ciano (p. 18 e 55), amarelo (p. 29), roxo (p. 75)
> — e o organograma da p. 2 tem bolhas em rosa, azul, amarelo e verde sem regra.
> A matiz é escolhida por página, não por sistema.
>
> Numa frente de patrimônio isso não é direção de arte: a cor do material é
> **dado técnico** — argamassa, pátina, pigmento, oxidação. Filtro que empurra
> matiz transforma leitura de estado de conservação em decoração. Fotografia de
> patrimônio entra com correção de exposição e nada mais. Escurecimento neutro
> para assentar texto é permitido; deslocamento de matiz não.

---

## 7 · Grafismo — o contorno

**Correção: a Sarasá tem grafismo.** A primeira versão deste arquivo dizia que
não tinha. Tem, está na capa do portfólio e reaparece na abertura de SERVIÇOS:

**Um desenho de contorno em linha única, em Cal, de patrimônio edificado** —
fortaleza, casario, perfil de terreno — correndo rente à base da peça e
sangrando nas duas laterais. Sem preenchimento, sem hachura, espessura
constante. É o equivalente da marchetaria da AMAZ e do Azulejo da Lavrō, e é
mais pertinente que os dois: é o próprio bem tombado, traçado a linha.

**Onde entra:** capa · abertura de seção · contracapa · rodapé de prancha de
respiro. Sempre na base, sempre sangrando, sempre em uma cor só.
**Onde não entra:** atrás de texto corrido, tabela, croqui ou mapa de danos ·
dentro das letras · sobre fotografia · em peça pequena · animado.

**Uma peça tem um mecanismo de superfície só:** fotografia, *ou* contorno, *ou*
campo chapado.

**Arquivo: `sarasa/grafismo-linha.svg`.** ⚠ **Derivado, não oficial.** No
portfólio o desenho é **raster** de 960 px, colado no PowerPoint. O SVG ao lado
é vetorização minha desse raster — serve para montar peça agora e escala sem
perda, mas o traço não é o original. **Pedir o vetor** junto com o pacote de
marca (§8). Herda cor por `currentColor`; `viewBox 0 0 2880 429`.

> **O candidato óbvio continua sendo o que não pode entrar.** O sistema de
> mapeamento de danos (`sarasa/MAPEAMENTO-DANOS.md`, 25 patologias × 11
> substratos) tem malha e paleta prontas, e é tentador transformá-lo em textura.
> **Não.** Cor de patologia tem de ser discriminável em croqui de campo por quem
> está no andaime; cor de marca tem de ser reconhecível em slide. Uma legenda que
> vira ornamento perde a função de legenda, e uma marca que empresta cor de
> legenda deixa de ser reconhecível. Quebra os dois sistemas de uma vez.

---

## 8 · O que falta — e não deve ser inventado

Contra o checklist do `MARCA-MICHEL-STEIN.md`:

| item | estado |
|---|---|
| 1 · nome, assinatura, site | ✅ |
| 2 · os quatro papéis de cor | ✅ com contrastes medidos e as duas superfícies |
| 3 · as faces, com peso por uso | ⚠️ **divergência aberta** entre a serifada do portfólio e a sans do site |
| 4 · a abertura | ✅ §5, campo Vinho |
| 5 · a contracapa | ✅ §5, QR e crédito decididos |
| 6 · o acervo do fundo | ⚠️ a regra existe, os arquivos são provisórios |
| 7 · o que é intocável | ✅ **o Vinho carrega o nome, o Ferro carrega `estúdio`; sobre campo escuro o lockup é monocromático** |

### O Instituto Sarasá — fora de escopo, registrado para ninguém inventar

O portfólio é assinado por **duas** entidades, lado a lado na capa e na
contracapa: **Estúdio Sarasá Conservação e Restauração S/S Ltda** (CNPJ
[cnpj removido], [cau removido], [endereço removido]) e **Instituto Sarasá de
Arte, Cultura e Cidadania — ISACC** (CNPJ [cnpj removido], [endereço removido]
1.099). Decisão do Michel em 29/08: **este arquivo cobre só o Estúdio.**

O que foi medido do Instituto, para que nenhuma peça o invente:

- **Cor própria: ocre `#E5A11A`.** Não é cor do Estúdio e não entra em peça
  desta frente.
- **Símbolo: o `S` vazado em branco sobre bloco ocre**, rompendo a borda do
  bloco em cima e embaixo. É o mesmo `S` do wordmark, ampliado.
- **Mesma estrutura de lockup** — palavra pequena em cima, nome grande embaixo —
  diferenciada por peso e caixa: o Instituto usa `sarasá` **bold, caixa baixa**;
  o Estúdio usa `Sarasá` leve com `S` capitular.

Levantar de verdade quando houver peça do Instituto. Até lá, **nada do Instituto
entra em peça do Estúdio**, e vice-versa.

### Aberto, e é decisão do Michel com o os sócios do Estúdio

1. **Face do logotipo** — pedir o pacote de marca: manual, ou o AI/EPS com as
   fontes. Fecha o §3 e libera a variante de uma linha.
2. **Serifada × sans (§3)** — decidir vendo o primeiro deck montado. Tendência
   declarada: sans do site.
3. **Papel Cal `#F3EEE7`** — decisão do Michel, não validada com os sócios. É a
   superfície de metade de toda peça de leitura.
4. **Poppins e Archivo** — confirmar se são escolha de marca ou default do tema
   Vamtam. Se forem default, a tipografia de corpo volta a ser lacuna.
5. **Vetor do grafismo** — hoje só existe raster de 960 px; o SVG do acervo é
   vetorização derivada (§7).
6. **Área de proteção** — não medida. §4 traz valor de trabalho.
7. **Lista de usos proibidos** — rascunhada no §4, não validada.
8. **Acervo do morph** — arquivos em resolução e autorização de uso.
9. **A veladura de cor (§6)** — a proibição de LUT contraria a prática atual do
   portfólio. Conversa a ter, com as palavras do §6.
10. **INPI e domínio** — não verificados nesta rodada.
11. **O escopo da frente** — a identidade do núcleo de arquitetura, distinta da
    identidade da Sarasá inteira, se refina em rodada própria.

---

## 9 · O vocabulário de gabaritos da Sarasá

**Não há peça Sarasá publicada no acervo.** Este parágrafo é previsão de
necessidade — a lista real sai da primeira peça montada, esta semana.

Do esqueleto servem desde já: `marca`, `divisor`, `frase`, `lista`, `cheia`,
`tabela`, `fim`.

Os que a frente vai pedir e **não existem**:

- `mapa-de-danos` — croqui com legenda ligada ao catálogo mestre de patologias.
  É o gabarito próprio desta frente e o que carrega argumento técnico. Depende
  da máquina da lupa, como `planta` e `desenho`, que faltam para todo mundo.
- `ficha` — ficha de patologia: substrato, diagnóstico, foto, prescrição.
- `antes-depois` — par de imagens com corte, a prancha que vende restauro.
- `fases` — linha de tempo de intervenção, com instância de aprovação marcada
  (municipal, CONDEPHAAT ou IPHAN — nunca assumida).

O portfólio 2026 sugere mais dois, já testados por eles em 88 páginas:
`mapa-brasil` (estados de atuação em Vinho chapado) e `premiacoes` (lista curta
em campo Vinho, com a peça premiada ao lado).

Enquanto não forem portados, montar peça Sarasá pelo esqueleto entrega bem
capa, divisor, texto e tabela, e **não entrega mapa de danos** — que é
justamente o que diferencia a frente.
