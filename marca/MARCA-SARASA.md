# marca Sarasá — a camada de marca

Documento de marca, sem dado de cliente, no repositório **público** de
apresentações. Abre por URL raw, sem token.

Companheiro do `../sistemas/DECK-MONTAR.md`, que é o motor e não sabe de que
marca é a peça. **Montar uma apresentação da Sarasá = motor + este arquivo + um
DECK.** O bloco que se cola no esqueleto é o `sarasa/bloco.html`, ao lado.

> **A peça sai com assinatura Sarasá.** Decisão do Michel em 29/08/2026. Nos
> projetos desta frente a marca da peça é a do Estúdio Sarasá — não a michel
> stein_ emprestada, como se fazia até aqui. A concepção e a coordenação entram
> como **crédito discreto na contracapa** (§5), não como assinatura.
>
> Para todo o resto **o `.md` é o mestre**: divergiu o desenho de uma peça nova,
> o `.md` ganha.

⚠ **Nota de origem — leia antes de usar qualquer número daqui.** A Sarasá **não
tem manual de marca** ao alcance: nada no Drive, nada no Notion, nenhuma peça no
acervo. Este arquivo foi levantado em 29/08/2026 de três fontes, e cada valor
carrega a sua:

| origem | confiança | o que deu |
|---|---|---|
| `Sarasa-logotipo-principal.svg` (oficial, servido pelo site) | **AFIRMÁVEL** | os dois fills, e toda a geometria do §4 |
| `Sarasa-logotipo-negativo.svg` (oficial) | **AFIRMÁVEL** | a regra do fundo escuro (§2) |
| CSS vivo de `estudiosarasa.com.br` (`--e-global-color-*`) | **CONFIRMAR** | paleta de apoio e faces — pode ser default do tema WordPress Vamtam, não escolha de marca |
| decisão do Michel, 29/08/2026 | **DECISÃO** | o papel Cal (§2) e o crédito (§5) |

**Nada foi inventado.** As lacunas estão nomeadas no §8.

---

## 1 · Identidade

| campo | valor |
|---|---|
| nome | `Estúdio Sarasá` em texto; o wordmark é o **lockup de duas partes** |
| lockup | `estúdio` em Ferro, condensada bold, caixa baixa · `Sarasá` em Vinho, grotesca de contraste baixo, corpo 3,76× maior |
| assinatura em slide | o lockup, dois fills — nunca uma palavra sozinha |
| frase de posicionamento | **O Patrimônio Cultural vivo** |
| site | `estudiosarasa.com.br` |
| o que é | núcleo de arquitetura: conservação, restauro e novas edificações |
| crédito da peça | `CONCEPÇÃO E COORDENAÇÃO · MICHEL STEIN_`, contracapa (§5) |

**O dispositivo da marca é a inversão do acento.** Na michel stein_ o acento é
reserva de 2% — o underscore terracota. Na AMAZ é a barra Cobre, um filete. Na
Sarasá o acento **carrega o nome inteiro**: o vinho pinta `Sarasá`, o preto pinta
`estúdio`. Não é ênfase, é a estrutura.

Isso não é leitura estética, é medição: o Vinho dá **8,64** sobre o papel. O
Cobre da AMAZ dá 4,38 e a terracota da michel stein_ dá 3,66 — aqueles dois são
reserva *porque não aguentam texto*. O Vinho aguenta título, corpo, filete e
tarja. É campo por medição, não por escolha.

**Símbolo: não existe.** O `S` de corpo inteiro é um glifo do lockup, não um
símbolo. Nenhuma peça o usa sozinho e nenhuma peça inventa um (§4, Micro).

**Sem underscore piscante** — é a assinatura da michel stein_.
**Sem barra de acento fora da caixa** — é a assinatura da AMAZ.

---

## 2 · Cor — os quatro papéis

Tokens nomeados **por papel**, não por cor, que é a nomenclatura que o motor pede.

| papel do motor | token | hex | nome | origem |
|---|---|---|---|---|
| **papel** | `--papel` | `#F3EEE7` | Cal | DECISÃO 29/08 |
| **tinta** | `--tinta` | `#231F20` | Ferro | **AFIRMÁVEL** — fill do logotipo |
| **primária** | `--vinho` | `#79242F` | Vinho | **AFIRMÁVEL** — fill do logotipo |
| **acento** | `--vinho` | `#79242F` | Vinho | **é a mesma cor** — ver abaixo |

**A Sarasá não tem quatro cores, tem três.** Primária e acento são o mesmo
Vinho, e isso é a marca, não uma lacuna: a cor que carrega o nome é a mesma que
marca o item ativo, o divisor, o ícone e a barra de carregamento no site vivo.
Escrever um quarto token seria inventar uma cor que a marca não tem.

**Sobre o papel Cal.** O site serve `#F9F9F9`, um branco frio, vindo da variável
`--e-global-color-vamtam_accent_3` — quase certamente default do tema, não
escolha de marca. Consagrar um default de WordPress como a superfície dominante
de toda peça é o tipo de acidente que este arquivo existe para impedir. O Cal
`#F3EEE7` é decisão do Michel em 29/08: quente a 5% de saturação, na família de
cal e argamassa que é o assunto da frente, e mantém o Vinho em 8,64. **Não
validado com o os sócios do Estúdio** — §8.

Apoio:

| token | hex | papel |
|---|---|---|
| `--chumbo` | `#4E4E4E` | texto secundário sobre Cal (7,90). CONFIRMAR — Vamtam |
| `--hair` | `#231F2026` | filete sobre Cal, derivado da tinta |
| `--soft` | `#231F2099` | tinta atenuada |

> ⚠ **Dois tokens do site não entram.** `#0A0909` (tarja/header) dá **1,22**
> contra a tinta `#231F20` — são a mesma cor, indistinguíveis. Um preto só, o do
> logotipo. E `#CCCCCC` (filete) dá **1,53** sobre Cal: some. Filete sobre claro
> é tinta em alfa, não cinza claro.

### A regra do acento

**O acento é definido pelo fundo** — e nesta marca a regra não é proposta minha,
está no artefato oficial.

| fundo | portador do acento | o Vinho pode ser |
|---|---|---|
| **Cal** `#F3EEE7` | **Vinho** (8,64) | tudo: nome, título, corpo, filete, tarja, pílula |
| **Ferro** `#231F20` | **Cal** (14,12) | **nada** — Vinho sobre Ferro = 1,63 |

O `Sarasa-logotipo-negativo.svg` é **monocromático**: quatorze elementos, um
único fill branco. A marca já decidiu que no escuro o Vinho sai e o lockup vira
uma cor só.

**Consequência dura: a Sarasá é uma marca de fundo claro.** A prancha roda em
Cal. Ferro é tarja, cabeçalho, rodapé e prancha de respiro — nunca superfície
que carregue o nome vivo, porque no escuro o nome perde exatamente aquilo que o
torna reconhecível.

### Contrastes medidos

Ferro sobre Cal **14,12** · Vinho sobre Cal **8,64** · Chumbo sobre Cal **7,21**
· Cal sobre Ferro **14,12** · Vinho sobre Ferro **1,63** (inutilizável) · Cal
sobre Vinho **8,64** · Ferro sobre Vinho 1,63 (inutilizável).

Todos os pares utilizáveis passam AA e AAA para texto normal. Não há nesta
paleta nenhum par de contraste marginal — é uma paleta de duas famílias de valor
bem separadas, e é por isso que ela não tolera fundo médio.

### Para a engine do fundo morph

`{paper:'#F3EEE7', ink:'#231F20', acc:'#79242F'}`.
Versão escura: `{paper:'#231F20', ink:'#F3EEE7', acc:'#F3EEE7'}` — no escuro o
acento não tem portador próprio, e coincide com a tinta. É a versão negativa do
logotipo levada ao fundo.

---

## 3 · Tipografia

**Duas famílias, mais o logotipo em SVG.**

| uso | face | pesos | origem |
|---|---|---|---|
| título, texto, dado | **Poppins** (`--sans`) | 400, 500, 600 | CSS vivo — CONFIRMAR |
| rótulo, metadado, crédito | **Archivo** (`--label`) | 600 | CSS vivo — CONFIRMAR |

Do CSS do site: corpo em 14 px, entrelinha 1,7em; rótulo em 12 px, 600, caixa
alta, tracking 0,5–1 px (**+.042 a +.083em**). Ambas são Google Fonts sob SIL
OFL — **embutíveis em base64**, que é o requisito do motor. Fallback
`system-ui, sans-serif` para as duas.

> ⚠ **CONFIRMAR.** Poppins e Archivo podem ser default do tema Vamtam. Se forem,
> não são escolha de marca e não deveriam ter virado regra. Estão aqui porque
> são o que está no ar, não porque alguém as escolheu — §8.

**A face do logotipo não é nenhuma das duas e não foi identificada.** Não vou
chutar. Duas consequências práticas:

1. **O logotipo entra como SVG**, não como texto — o oficial, com os valores já
   aplicados. Os dois fills são reetiquetados para `--tinta` e `--vinho` no
   `sarasa/bloco.html`; o negativo é fill único e aceita `currentColor` direto.
2. **Face de trabalho provisória**, só onde o lockup precisar ser reconstruído
   fora do SVG (variante de uma linha, marca d'água, teste de escala):
   **Archivo 400/500** para `Sarasá` e **Archivo Narrow 700** para `estúdio` —
   medidas compatíveis com a geometria do §4, e nenhuma família nova no bloco.
   **É empréstimo declarado.** Quando o AI/EPS chegar, troca-se a face e a
   geometria do §4 continua valendo — ela foi medida do desenho, não da fonte.

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
| **Micro** | < 130 px · < 30 mm | **sai** — só `Sarasá`, em Vinho | favicon, avatar, marca d'água, carimbo |
| **Compacto** | 130–300 px · 30–70 mm | presente | cartão, rodapé, papelaria, placa pequena |
| **Padrão** | 300–1000 px · 70–250 mm | presente | slide, capa de proposta, uso geral |
| **Herói** | > 1000 px · > 250 mm | presente | placa de obra, fachada, hero de site |

Piso de leitura: altura-x de `estúdio` **≥ 7 px em tela, ≥ 4,5 pt em impresso**.
É o acento agudo do `ú` que estabelece o piso — ele ocupa 4,70 unidades e é o
primeiro detalhe a fechar.

**No Micro o que fica é `Sarasá`, nunca o `S` sozinho.** O `S` sozinho seria um
símbolo, e a marca não tem símbolo (§1).

**Área de proteção: não medida.** Valor de trabalho, meu, até haver manual —
folga de **½ altura-x de `Sarasá`** (23,5 unidades ≈ 10% da largura do lockup)
em todos os lados. Sobre fotografia, campo chapado de Cal sob a marca. §8.

### Usos proibidos

Rascunhados por mim a partir da geometria, **não validados** — §8.

- Não recolorir: `Sarasá` é Vinho e `estúdio` é Ferro. Inverter, igualar as duas
  em preto "por contraste", ou pintar `estúdio` de Vinho, descaracteriza.
- Não separar as palavras nem empilhá-las como duas linhas soltas.
- Não usar o `S` sozinho como símbolo.
- Não distorcer, condensar ou expandir — a proporção 3,764:1 é fixa.
- Não aplicar o positivo sobre fundo escuro: sobre Ferro usa-se o negativo
  monocromático (§2).
- Não pôr o lockup sobre fotografia sem campo chapado sob ele.
- Não acrescentar contorno, sombra ou brilho.
- Não trocar `estúdio` por outra palavra (`escritório`, `arquitetura`).

---

## 5 · A abertura e a contracapa

**Abertura** — gabarito `marca`, **fundo Cal** (a regra do §2 tira o fundo
escuro da abertura):

1. **Lockup** no alto à esquerda, nível Padrão, dois fills.
2. **Frase** `O Patrimônio Cultural vivo`, Poppins 600,
   `clamp(28px, 5.2vw, 96px)`, tracking −0,02em, uma linha, em Ferro.
   *Sugestão minha, não levantada: a palavra `vivo` em Vinho, repetindo a lógica
   do próprio logotipo — o Vinho carrega a palavra que importa. Desligar é
   trocar uma cor.*
3. **Site** `estudiosarasa.com.br`, Archivo 600, caixa alta, `clamp(10px,.78vw,15px)`,
   +.08em, em Chumbo.
4. **Pílula `começar →`** em Vinho, texto Cal (8,64). O clique chama `avanca()`.

**Sem underscore piscante. Sem barra de acento.** São as assinaturas das outras
duas marcas.

**Contracapa** — mesmo bloco, com `assina:'obrigado'` no lugar da frase e sem a
pílula:

- **QR** em módulos Ferro sobre Cal, apontando para **`estudiosarasa.com.br`**.
  Decisão do Michel em 29/08: a peça é da Sarasá, o QR também.
- **Crédito**, linha pequena ao pé: `CONCEPÇÃO E COORDENAÇÃO · MICHEL STEIN_`,
  Archivo 600, caixa alta, +.08em, em Chumbo sobre Cal (7,21). Não disputa a
  assinatura; registra a autoria na peça que circula.

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
av. Higienópolis, Castelinho de Poços de Caldas / Pouso Alegre. O Michel vai
fornecer os arquivos em resolução e a autorização de uso, e a substituição é
**troca de arquivo, não de regra**: o preset, o formato e a contagem continuam.

> **Nenhum LUT nesta frente.** A AMAZ tinge toda fotografia com filtro `.cube` da
> família, e para incorporação isso é direção de arte. Aqui a cor do material é
> **dado técnico** — argamassa, pátina, pigmento, oxidação. Um filtro que empurra
> matiz transforma leitura de estado de conservação em decoração. Fotografia de
> patrimônio entra com correção de exposição e nada mais.

---

## 7 · Grafismo

**A Sarasá não tem grafismo, e não deve ganhar um por invenção.** A AMAZ tem a
marchetaria, a Lavrō tem o Azulejo; aqui não há nada levantado e nada a portar.
Enquanto não houver, a superfície da prancha é **Cal chapado ou fotografia — uma
coisa só por prancha**.

> ⚠ **O candidato óbvio é o que não pode entrar.** O sistema de mapeamento de
> danos (`sarasa/MAPEAMENTO-DANOS.md`, 25 patologias × 11 substratos) tem malha
> e paleta prontas, e é tentador transformá-lo em textura de marca. **Não.** Cor
> de patologia tem de ser discriminável em croqui de campo por quem está no
> andaime; cor de marca tem de ser reconhecível em slide. Uma legenda técnica que
> vira ornamento perde a função de legenda, e uma marca que empresta cor de
> legenda deixa de ser reconhecível. Quebra os dois sistemas de uma vez.

---

## 8 · O que falta — e não deve ser inventado

Contra o checklist do `MARCA-MICHEL-STEIN.md`:

| item | estado |
|---|---|
| 1 · nome, assinatura, site | ✅ |
| 2 · os quatro papéis de cor | ✅ com contrastes medidos — ⚠ dois tokens de tema descartados, um decidido |
| 3 · as faces, com peso por uso | ⚠ duas famílias levantadas; **face do logotipo não identificada** |
| 4 · a abertura | ✅ §5 |
| 5 · a contracapa | ✅ §5, QR e crédito decididos |
| 6 · o acervo do fundo | ⚠ a regra existe, os arquivos são provisórios |
| 7 · o que é intocável | ✅ **o Vinho carrega o nome, o Ferro carrega `estúdio`; no escuro o lockup é monocromático** |

Aberto, e é decisão do Michel com o os sócios do Estúdio:

1. **Face do logotipo** — pedir o pacote de marca: manual, ou o AI/EPS com as
   fontes. Fecha o §3 e libera a variante de uma linha.
2. **Papel Cal `#F3EEE7`** — decisão do Michel, não validada com os sócios. É a
   superfície dominante de toda peça; vale confirmar antes de imprimir.
3. **Poppins e Archivo** — confirmar se são escolha de marca ou default do tema
   Vamtam. Se forem default, a tipografia inteira volta a ser lacuna.
4. **Portador do acento em fundo escuro** — não existe. Hoje a resposta é o
   logotipo monocromático, que é o que a marca já faz. Se um dia a frente quiser
   prancha escura com o nome vivo, precisa de uma segunda cor de marca — e essa
   é decisão deles, não derivação minha.
5. **Área de proteção** — não medida. §4 traz valor de trabalho.
6. **Lista de usos proibidos** — rascunhada no §4 a partir da geometria, não
   validada.
7. **Acervo do morph** — arquivos em resolução e autorização de uso.
8. **Grafismo** — ter ou não ter. Hoje não tem, e isso está escrito como decisão,
   não como esquecimento.
9. **INPI e domínio** — não verificados nesta rodada.

---

## 9 · O vocabulário de gabaritos da Sarasá

**Não há peça Sarasá publicada no acervo.** Este parágrafo é previsão de
necessidade, não levantamento — a lista real sai da primeira peça montada.

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

Enquanto não forem portados, montar peça Sarasá pelo esqueleto entrega bem
capa, divisor, texto e tabela, e **não entrega mapa de danos** — que é justamente
o que diferencia a frente.
