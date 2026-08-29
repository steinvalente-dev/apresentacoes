# 02 · DESIGN-SYSTEM_Lavrō — documento normativo

> Documento **normativo** do sistema de interface da Lavrō. É a fonte de verdade.
>
> Relação com os outros arquivos:
> - `01_MARCA_Lavro.md` manda em **marca** (wordmark, símbolo, cor da marca, régua, gradiente, tipografia, co-branding). Se houver conflito, ele vence no que é marca.
> - Este arquivo manda em **interface** (tokens, componentes, movimento, navegação, densidade).
> - `03_TELA_Hoje.html` é a **implementação de referência**: styleguide vivo, arquivo único, sobrescrito a cada versão. Não é fonte de verdade — se divergir daqui, ele está velho.
>
> **Versão 1.11 · 06.08.2026** · consolida Lab 01, Lab 02 (v1→v9), o protótipo Hoje (v1→v9),
> o Lab 03 · Arquivos da obra (v1→v10), o Lab 04 · Pessoas (v1→v6) e o Lab 05 ·
> Configuração da empresa (v1→v3)
>
> A v1.6 é uma **mesclagem**: a linha de versões 1.1→1.5 nasceu da implementação (o que o
> repositório provou), e existia em paralelo uma linha de **design** que seguiu do 1.0 e
> especificou o modal de registro e o texto do assessor. As duas foram reunidas aqui. Onde
> divergiram, a regra foi: **decisão de desenho vence pelo lado do design; fato sobre o
> repositório vence pelo lado da implementação.**
>
> **Local canônico: `docs\`, no repositório, versionado no git.** O Google Drive guarda uma
> **cópia de leitura**, para acesso remoto e no celular, atualizada quando uma versão fecha.
> Em caso de divergência, vale o repositório.
>
> A v1.7 acrescenta o que a **navegação** exigiu ao sair do papel: a gaveta de dois
> escopos (**8.4b**) e o retrato da onda A, com o que nasceu dormente e por quê (**8.4c**).
> A v1.8 traz a primeira revisão de uso da gaveta, que virou **régua de bloco**: o que
> vale para todas as obras × o que é daquela obra (**8.4b**). A **v1.9** encurta a gaveta
> pela raiz — telas se unem em "Editar obra" em vez de itens se esconderem — e traz o
> selo **em breve** (**8.4b**).
>
> A seção 13 é o brief de migração da Onda A **dos tokens** (jul/2026) — não confundir com
> a "onda A" da navegação, que é a primeira fatia da §8 e está descrita na 8.4c.

---

## 1. Tokens de cor

### 1.1 Rampa neutra (fria, não tematizável)

```
--n-950 #0E1116   --n-900 #1C222E   --n-800 #262E3C   --n-700 #323B4B
--n-600 #3F4959   --n-500 #5E6779   --n-400 #8790A2   --n-300 #B0B7C4
--n-200 #D3D8E0   --n-100 #E9EBF0   --n-050 #F5F6F9   --n-000 #FFFFFF
```

### 1.2 Azuis (ver manual da marca, seção 4)

| Token | Valor | Papel |
|---|---|---|
| `--azul` | `#0123FF` | marca e **ação** (preenchimento) nos dois modos |
| `--azul-fundo` | `#0016C7` | superfície de marca no modo escuro |
| `--azul-claro` | `#7C8BFF` | **acento de interface** no escuro (obrigação AA) |
| `--marca-escuro` | `#5B6BFF` | wordmark e traço fino sobre fundo escuro |

**A regra que resolve a confusão recorrente:** o que falha no escuro é **traço fino
elétrico sobre grafite** (2,4:1). Branco **sobre** `#0123FF` dá 7,8:1 em qualquer
fundo. Logo: **azul elétrico como preenchimento vale nos dois modos**; como texto,
linha ou ícone fino no escuro, usa-se `#7C8BFF` ou `#5B6BFF`.

Nota: *superfícies de alta ênfase permanentemente escuras (5.19) usam `--azul-claro` para
traço e texto de acento, e `--azul` para preenchimento. É a mesma regra da 1.2, e não a
criação de um segundo azul.*

### 1.3 Semânticos por modo

| Token | Claro | Escuro |
|---|---|---|
| `--bg` | `#F5F6F9` | `#0E1116` |
| `--sup-1` | `#FFFFFF` | `#262E3C` |
| `--sup-2` | `#E9EBF0` | `#323B4B` |
| `--sup-3` | `#D3D8E0` | `#3B4556` |
| `--linha` | `#D3D8E0` | `rgba(255,255,255,.11)` |
| `--linha-forte` | `#B0B7C4` | `rgba(255,255,255,.22)` |
| `--texto` | `#0E1116` | `#EDEFF5` |
| `--texto-2` | `#3F4959` | `#B0B7C4` |
| `--texto-3` | `#8790A2` | `#5E6779` |
| `--acento` | `#0123FF` | `#7C8BFF` |
| `--acao` | `#0123FF` | `#0123FF` |
| `--sobre-acao` | `#FFFFFF` | `#FFFFFF` |
| `--marcador` | `#7C8BFF` | `#0123FF` |
| `--pil-bg` | `#0E1116` | `#FFFFFF` |
| `--pil-texto` | `#FFFFFF` | `#0E1116` |
| `--cap-bg` | `#FFFFFF` | `#262E3C` |
| `--cap-texto` | `#0E1116` | `#EDEFF5` |
| `--cap-borda` | `rgba(14,17,22,.16)` | `rgba(255,255,255,.22)` |
| `--marca-cap` | `#0123FF` | `#5B6BFF` |

`--pil-bg` inverte contra o tema (preta no claro, branca no escuro) porque a
pílula é de **alta ênfase** — ver 4.1. `--cap-*` acompanha o tema, porque a
cápsula é assinatura de produto, não elemento de UI.

### 1.4 Status — **não tematizável**

| Token | Claro | Escuro | Significa |
|---|---|---|---|
| `--ok` | `#1E7F4F` | `#4ADE80` | concluído, no prazo, assinado |
| `--at` | `#B26A00` | `#FFB84D` | prazo próximo, estoque no mínimo, pendente |
| `--er` | `#C62828` | `#FF6B6B` | atrasado, saldo negativo, falha |
| `--neutro` | `#5E6779` | `#8790A2` | não iniciado, paralisado, sem dado |

Verde, âmbar e vermelho carregam significado operacional e de segurança. Nenhum
tema de cliente os altera.

**O par `-c` / `-e` é o valor bruto, e o sufixo diz o FUNDO, não a forma:**

```
--ok-c #1E7F4F   --at-c #B26A00   --er-c #C62828    valor para fundo CLARO  (o mais escuro)
--ok-e #4ADE80   --at-e #FFB84D   --er-e #FF6B6B    valor para fundo ESCURO (o mais claro)
```

`--ok`, `--at` e `--er` são apenas o apontador que o modo vigente resolve: no claro
apontam para `-c`, no escuro para `-e`. **Use sempre o apontador.** O par bruto existe
para os dois casos em que a cor não pode seguir o modo — abaixo, e as superfícies
permanentemente escuras da 5.19.

**Regra do selo sólido, e ela é separada:** o selo **sólido** usa os valores `-c`
**nos dois modos**, porque é sobre eles que o texto branco passa AA — **com uma exceção
medida, e ela é o âmbar**:

| Fundo | Branco sobre ele | AA (4,5:1) |
|---|---|---|
| `--ok-c` `#1E7F4F` | 5,00:1 | passa |
| `--er-c` `#C62828` | 5,62:1 | passa |
| `--at-c` `#B26A00` | **4,24:1** | **reprova** |
| `--at-solido` `#A96500` | 4,62:1 | passa |

```
--at-solido #A96500    fundo do selo SÓLIDO âmbar, nos dois modos
```

A versão 1.1 afirmava que os três `-c` passavam AA. **Estava errada quanto ao âmbar**, e
o valor `--at-solido` existe para cobrir só esse caso. Ele **não** substitui `--at-c`
como cor de fundo claro nem como texto: fora do selo sólido, âmbar continua sendo `--at`.

Isso **não** faz de `-c` "a variante sólida": `-c` é a cor de fundo
claro. Aplicar `--er-c` como texto ou traço sobre fundo escuro reprova em contraste.

### 1.5 O que é tematizável

**Ampliado na v1.3**, por decisão do Michel a partir do Lab 05. Por organização:

| Tematizável | O que é | Onde vive |
|---|---|---|
| `--acento` | a cor da marca do cliente no app | `organizacoes.acento` |
| **`--painel`** | **segunda superfície**: gaveta de navegação (5.9) e assessor de IA (5.7) | `organizacoes.painel` |
| **textura de fundo** | `gradiente` (o do `01` §8) · **`geometrico`** — o Azulejo, `01` §8.1b · `grade` · `nenhum` | `organizacoes.textura_fundo` (+ `azulejo_semente` e `azulejo_tema`) |
| fonte de display | só o display; o corpo nunca muda (`01` §9.1) | `organizacoes.fonte_display` |
| logo e nome | as duas versões do logo, nome e apelido | `organizacoes` + Storage |

**Continua fixo, e isso não se negocia:** status, rampa neutra, espaço, raio e movimento.

**`--painel` entrou porque acento intenso cansa em área grande.** A gaveta e o assessor
são superfícies de permanência, não de ação — pintá-las com o acento do cliente (o amarelo
da Baraka, por exemplo) transforma o app numa parede da cor da marca. Isso **emenda a 5.7
e a 5.9**, que hoje fixam essas superfícies em azul. O par texto/painel é validado no
cadastro: AA obrigatório, sem exceção de marca.

**"Tema" (Lavrō · Papel) é preset da interface, não coluna.** Ele agrupa acento + painel +
fonte + textura no momento da escolha e grava os quatro valores. Guardar o preset
*também* criaria duas verdades — e a hora em que elas divergirem é a hora em que a tela
mostra "Papel" com as cores de outro tema.

~~**Fora, até terem especificação própria:** texturas `geometrico` e `grade`.~~
**Destravado na v1.5.** A `geometrico` ganhou a especificação que faltava — é o
**Azulejo** (`01` §8.1b, aplicação em §7.1), com regras compositivas escritas,
três pares fundo/traço medidos e derivação por semente. A `grade` é o caso
trivial (pontos em malha regular, mesma cor de traço do azulejo) e entra junto.
O princípio continua valendo para o que vier depois: **token de textura sem
especificação vira interpretação de quem implementa.**

**O tema do azulejo não é tematizável pelo acento**, e isso é exceção deliberada
dentro de uma seção sobre o que a organização escolhe: ela escolhe *entre três
pares medidos*, não uma cor livre. Traço sobre fundo de marca arbitrária não tem
contraste garantido, e a textura passaria a competir com a ação.

**Risco conhecido:** cliente com marca amarela produz `--acento` que colide com
`--at`. Exigir separação mínima de matiz no cadastro do tema e manter um
valor reserva de `--at`. Decidir antes do primeiro cliente amarelo. **O mesmo vale para
`--painel`**, com um agravante: ele cobre área grande, então a colisão é mais visível.

### 1.6 Famílias de token de componente

`--pil-*` e `--cap-*` estão na 1.3 porque são semânticas por modo. As quatro famílias
abaixo têm regra própria de modo e ficam aqui. **Nenhuma delas é tematizável** (1.5).

#### `--bar-*` — barra de endereço da janela de arquivos (5.19)

```
--bar-bg      --n-950            SEMPRE, nos dois modos
--bar-txt     #FFFFFF
--bar-txt-2   rgba(255,255,255,.60)
--bar-linha   rgba(255,255,255,.26)
--bar-sup     rgba(255,255,255,.11)
--bar-acento  --azul-claro (#7C8BFF)
--bar-er      #FF6B6B      --bar-at  #FFB84D
```

**Não seguem o modo.** A superfície é permanentemente escura, então os valores são os de
fundo escuro nos dois temas — `--bar-er` e `--bar-at` são `--er-e` e `--at-e`, pela regra
da 1.4. `--bar-acento` não é um segundo azul: é a 1.2 aplicada a traço fino sobre escuro.

#### `--tipo-*` — selo de tipo de arquivo (5.22)

| Tipo | Claro | Escuro |
|---|---|---|
| pdf | `#C0392B` | `#F07167` |
| dwg | `#0E7490` | `#4FC3D9` |
| xls | `#2E7D57` | `#63D9A0` |
| img | `#7A4FBF` | `#B79BEE` |
| doc | `#3A5FA8` | `#8FB0EA` |
| zip | `#8A6A2F` | `#D8B26A` |
| outro | `--n-500` | `--n-400` |

Seguem o modo. **Não pertencem à paleta de status** e existem só dentro do selo — a regra
de contenção está na 5.22.

#### `--papel-*` — marcação de papel da pessoa (Pessoas)

Par explícito **texto/fundo por modo**, um por papel: `admin` · `operador` ·
`almoxarife` · `cliente` · `pendente`.

**Mesmo desenho do `--tipo-*`, e pela mesma razão: papel não é status.** Verde, âmbar,
vermelho e azul elétrico já estão comprometidos com estado e com ação. Pintar papel com
eles faz *cliente* parecer alarme e *admin* parecer prazo vencendo — a marcação mais
repetida da tela roubaria a paleta que sustenta o alarme de verdade.

Seguem o modo. Não são tematizáveis (1.5) e existem **só** dentro da marcação de papel,
pela mesma regra de contenção do selo de tipo (5.22).

**O par é `--papel-X` (tinta) sobre `--papel-X-f` (fundo).** Nunca um sem o outro: o selo
de papel é tinta sobre lavado, e usar a tinta como texto solto fora do selo quebra a
contenção.

**A matiz diz a FAMÍLIA; o tom diz o PAPEL.** São três bandas, e é isso que faz papéis
parentes parecerem parentes sem virarem o mesmo selo:

| Família | Banda (matiz) | Quem ocupa | Reservado para |
|---|---|---|---|
| **Administração** | violeta, 300–318° | `admin` em 309° | níveis futuros (admin júnior) em 300 e 318 |
| **Campo** | petróleo → azul, 218–262° | `operador` 220° · `almoxarife` 260° | o meio da banda |
| **Contratante** | magenta, 336–356° | `cliente` em 348° | cliente de segundo nível em 336 e 356 |

**As bandas são medidas em CIE LCHab**, e o documento diz isso porque em HSL ou OKLCH os
mesmos hex dão outros números — quem for conferir na ferramenta errada vai achar que a
tabela está furada.

| | Claro · tinta / fundo | Escuro · tinta / fundo | Contraste do par |
|---|---|---|---|
| `admin` | `#6D3FBF` / `#E8E0F5` | `#BF92FF` / `#383A53` | 5,27 · 4,62 |
| `operador` | `#106877` / `#D9E7E9` | `#5CB5C7` / `#2C3E4D` | 5,07 · 4,67 |
| `almoxarife` | `#296893` / `#DDE7EE` | `#6CAFE5` / `#2E3D50` | 4,79 · 4,69 |
| `cliente` | `#A03070` / `#F0DEE8` | `#FD7BBF` / `#40374C` | 5,18 · 4,69 |
| `ativo` (`--papel-ok`) | `#1C7549` / `#DBEBE3` | `#51DF85` / `#2F584C` | 4,61 · 4,67 |
| `suspenso` (`--papel-neutro`) | `#5C6577` / `#E5E7EA` | `#B2B8C3` / `#3D4654` | 4,73 · 4,78 |

**Os 12 pares foram medidos e todos passam AA** (mínimo 4,61:1), nos dois modos — e a
separação também: **ΔE ≈ 19 dentro da família** (parecidos, distinguíveis), **≥ 49 entre
famílias** e **≥ 40 de todo status e do azul da marca**. Conferido a partir do
`_historico\04_Pessoas\LAB-04_Pessoas_v6.html` em 01/08/2026.

**No escuro a tinta do fundo é 12%, não 24%.** A 24% os quatro fundos convergiam para
pastéis e a distância entre famílias caía de 49 para 22 de ΔE — as famílias existiam no
token e sumiam na tela.

**Duas delas não são papel, e é deliberado:** `--papel-ok` e `--papel-neutro` marcam a
**situação do vínculo** (ativo · suspenso). Ficam na família porque usam a mesma gramática
visual — selo suave, tinta sobre lavado —, e ficariam erradas em verde de status, que
significa *concluído no prazo*, não *conta em uso*.

**`pendente` é a exceção, e usa `--at` de status.** Não é um papel: é uma pessoa esperando
liberação, e **exige ação do admin**. É o único caso da tela em que a paleta de status
está correta, porque ali o significado é mesmo o de status.

**Verde puro está fora da paleta de papel, de propósito.** Ele é de "concluído / no prazo",
e um papel não é uma conclusão.

**Colisão de nome, e ela é conhecida:** o `01` usa `--papel`, `--papel-2` e `--papel-3` no
CSS do próprio documento com o sentido **oposto** (*superfície de papel*), além de
`--creme-papel` como cor. Aqui `papel` é **função da pessoa** — o termo do domínio, o que
o `Gate` lê e o que o schema chama de `role`. A família fica com o nome do domínio; se o
manual um dia exportar os dele, é ele que renomeia. Registrado porque duas variáveis de
mesmo nome e sentido oposto já custaram uma onda inteira (o `C` de `ui.jsx` × `clienteUi.jsx`).

#### `--est-lib` — estado *liberado* (5.30)

```
--est-lib   claro #0123FF   ·   escuro #7C8BFF
```

Segue o modo, pela mesma razão de `--acento`. É o único uso de azul como **estado**, e ele
vale apenas na coluna de estado — ver 5.7.

---

## 2. Espaço, raio, elevação

```
espaço    2 · 4 · 8 · 12 · 16 · 24 · 32 · 48
raio      --r-sm 6px · --r-md 12px · --r-lg 20px · --r-pill 999px
régua     --w-regua 4px
```

### 2.1 Elevação: **sombra é repouso, brilho é significado**

Regra inviolável. Nada brilha por ser azul. Brilho (`filter: drop-shadow`, aura,
halo) é reservado a **estado com significado** — a barra viva do Gantt, o "dados
ao vivo". Um elemento parado usa sombra.

```
--e-1  claro:  0 1px 2px rgba(14,17,22,.07), 0 0 0 1px rgba(14,17,22,.07)
       escuro: 0 0 0 1px rgba(255,255,255,.09), inset 0 1px 0 rgba(255,255,255,.07)
--e-2  claro:  0 1px 2px rgba(14,17,22,.08), 0 8px 22px rgba(14,17,22,.11),
               0 0 0 1px rgba(14,17,22,.075)
       escuro: 0 0 0 1px rgba(255,255,255,.11), inset 0 1px 0 rgba(255,255,255,.10),
               0 10px 28px rgba(0,0,0,.55)
```

No escuro a elevação é **técnica D**: superfície mais clara + borda luminosa +
realce `inset` de 1px no topo + sombra grande. Não é só sombra, porque sombra
sobre preto não aparece.

**Emenda da v1.3 — o claro ganhou duas sombras, e só o claro.** O `--e-2` claro passou de
uma sombra difusa para a gramática de **contato curto + halo largo** da 2.2, com o fio um
pouco mais presente. A queixa que originou isso foi "no claro parece menos tátil", e ela
tinha razão: esta seção justifica o escuro precisar de quatro camadas, mas nunca exigiu
que o claro fosse plano. Aprovado por comparação lado a lado no Lab 04 v4/v5. **O escuro
não foi tocado** — lá a técnica D já resolve, e mexer nele seria consertar o que não
estava quebrado.

### 2.2 Elevação flutuante (pílulas sobre conteúdo)

Sombra em **duas camadas** — contato curto + halo largo:

```
claro:  0 2px 6px rgba(14,17,22,.34), 0 12px 28px rgba(14,17,22,.30)
escuro: 0 2px 8px rgba(0,0,0,.72),    0 14px 34px rgba(0,0,0,.62)
```

### 2.3 Elevação **por papel**

| Papel | Estratégia | Motivo |
|---|---|---|
| Operador | **sombra** | celular fraco, sol, internet ruim |
| Cliente | **blur** (`backdrop-filter`) | desktop, dispositivo mais forte |

Véu claro (scrim) está **descartado**: tinge, e briga com card azul passando por
baixo. O blur dissolve em vez de clarear — visualmente superior, mas
`backdrop-filter` em elemento sticky repinta a cada frame de rolagem. Daí a
divisão por papel.

**Emenda da v1.3 — o véu de modal usa blur nos dois papéis.** A restrição acima é sobre
`backdrop-filter` em elemento **sticky**, que repinta a cada frame porque o conteúdo
atrás rola por baixo dele. Véu de modal é **fixo e o conteúdo atrás não rola** — o custo
que justifica a divisão por papel simplesmente não existe ali. A própria seção já
preferia blur a scrim; o que ela vetava era o caso de rolagem.

**Exige reserva:** `@supports not (backdrop-filter: blur(1px))` cai para o véu opaco. Sem
isso, num navegador sem suporte o modal fica sobre conteúdo legível e a hierarquia some.

### 2.4 Largura de folha

**O limite de folha não é global.** Telas de dados densos usam **1560px**. Texto corrido
mantém o limite anterior. O teto existe porque sem ele, num monitor largo, o olho perde a
linha entre a primeira e a última coluna.

---

## 3. Densidade

Preferência do usuário, persistida por perfil. **Só o vertical muda. `font-size`
nunca muda e nada reflui.**

| Token | Confortável | Compacto |
|---|---|---|
| `--pad-card` | 22px | 14px |
| `--gap-card` | 14px | 9px |
| `--alt-li` | 48px | 44px |
| `--toque` | 48px | 44px |
| `--gap-grade` | 16px | 11px |

Fixos nas duas: etiqueta 11px · corpo 14px · h3 17px · dado 14px.

**A v1.2 ampliou estes valores e a v1.3 desfez isso.** O motivo de desfazer é o motivo
certo: o Michel avaliou o app no ar e a densidade atual está boa nas duas posições. O que
ele queria mais espaçado era **uma tela**, não o sistema — e isso não é densidade.

### 3.1 Porte de superfície — a escala da tela, não a preferência do usuário

**Densidade e porte são eixos diferentes, e confundi-los foi o erro da v1.2.**

- **Densidade** é do usuário, vale para o app inteiro, e alterna confortável ↔ compacto.
- **Porte** é da superfície: uma tela de gestão (linha com subtexto, ficha de detalhe,
  painéis lado a lado) respira diferente de uma lista operacional densa.

O porte amplo é um escopo nomeado que **redefine os mesmos tokens** dentro de si:

```css
.lv-porte-amplo {
  --pad-card: 26px;   /* compacto 14 */
  --gap-card: 18px;   /* compacto  9 */
  --alt-li:   58px;   /* compacto 44 */
  --alt-ficha:54px;   /* compacto 44 */
}
```

Três consequências, e as três são o motivo da forma:

1. **A alternância do usuário continua valendo dentro do porte** (58/44, 26/14, 18/9).
   A §3 não é contrariada: o porte muda a escala, não a preferência.
2. **O CSS da tela não muda de vocabulário** — continua escrevendo `var(--alt-li)`. Quem
   porta um protótipo copia o CSS sem traduzir nada, que é onde os erros de port nascem.
3. **Tela nova de gestão veste o porte** em vez de inventar mais um número solto.

`--alt-ficha` só existe no porte amplo, porque **ficha** (§14) é dele: é a pauta de dados
do detalhe, e é mais baixa que `--alt-li` de propósito — linha de lista é alvo de clique,
linha de ficha é leitura, e leitura não paga o pedágio do toque.

**Quem veste hoje:** Pessoas. **Quem não veste:** Arquivos, e nada do que está no ar muda.

**Piso de toque: 44px, sem exceção.** Discrição visual vem de tamanho de letra e
cor, nunca de alvo pequeno. (Erro cometido e corrigido: itens secundários da
gaveta estavam com 34px.)

**O padrão que concilia as duas coisas:** alvo de 44px com **desenho menor por dentro** —
um invólucro `.alvo44` sem pintura envolvendo um chip de ~34px. É a resposta desta mesma
seção quando o controle precisa *parecer* leve: quem encolhe é o desenho, nunca a área
sensível. Já usado na caixa de seleção (5.16, desenho de 19px em alvo de 44px).

---

## 4. Tipografia e número-âncora

Papéis definidos no manual da marca (seção 9): Space Grotesk display, Inter
corpo, IBM Plex Mono dado. Aqui só o que é de interface.

**A serifa do pacote é a Fraunces** (escolha do Michel, 02/08/2026 — substitui o Georgia
que era espécime provisório no Lab 05). Ela é **opção de display**, nunca corpo: o `01`
§9.1 trava corpo e mono porque é a métrica do corpo que governa quebra de linha e ritmo
vertical. Auto-hospedada em `src/fonts.css`, quatro subsets (latin e latin-ext × romano e
itálico), variável de verdade.

```
--f-serif             "Fraunces", Georgia, serif
--serif-eixos         "opsz" 144, "SOFT" 40, "WONK" 1     display
--serif-eixos-texto   "opsz"  24, "SOFT" 40, "WONK" 0     abaixo de ~16px
```

**Três armadilhas, todas verificadas na tabela `fvar` dos arquivos e todas silenciosas:**

1. **`font-weight: 400` é obrigatório.** O padrão do arquivo é **900** — omitir o peso não
   dá erro, dá Black.
2. **`font-variation-settings` desliga o `font-optical-sizing` automático.** Com `opsz`
   fixo em 144 a fonte fica sempre no desenho de display; em corpo pequeno os traços finos
   somem. É para isso que existe o segundo conjunto de eixos.
3. **Itálico é `font-style`, não eixo.** Sem os arquivos itálicos o navegador inclina o
   romano sozinho, e o resultado é falso.

**Ela fica fora do precache do service worker** (`vite.config.js`): são ~490 KB de uma
serifa opcional, e o operador em obra não deve pagar isso na instalação por um tema que a
organização dele talvez nunca escolha.

### 4.1 Número-âncora — **código × grandeza**

A divisão não é sobre tamanho, é sobre **como o número é lido**.

| Tipo | Como é lido | Fonte | Exemplos |
|---|---|---|---|
| **Código** | caractere por caractere; procurado, conferido, ditado no rádio | IBM Plex Mono 500/600, `tabular-nums`, zero cortado | RDO 0147 · M-12 · +12,40 m · 24.07.26 · NF 8842 |
| **Grandeza** | de relance, como magnitude; comparada | Space Grotesk 700, `tabular-nums` | 68% · 14 · 2,5 h · 1.248,50 m² |

**Caso de fronteira decidido: data-âncora é CÓDIGO.** O "24" grande de um marco
não é quantidade, é o identificador de um dia — vai em mono, e é aí que o zero
cortado paga (`04`, `07`, `10` numa coluna). Já "12 dias de atraso" é grandeza.

**Consequência para movimento (ver 6.4): código não anima. Grandeza pode crescer.**
RDO 0147 contando de 0 a 147 é absurdo.

**Grandeza em tabela: confirmada em Space Grotesk 700.** Testada contra 500 e contra mono
no Lab 03. Aprovado 700.

---

## 5. Componentes

### 5.1 Pílula de navegação — alta ênfase

```
min-height 44px · padding 0 16px · radius 999px · border 0
fundo --pil-bg · texto --pil-texto · Inter 600 13px
:active transform scale(.965)   (press, não hover — no dedo hover não existe)
```

*Era 40px até a v1.2, em divergência com o piso de toque da §3 e da §10. **Resolvido na
v1.3 subindo a pílula** — decisão do Michel, tomada enquanto o custo era só documento: a
navegação Lavrō ainda não foi implementada. O `03` está em 40 e é ele que fica velho.*

**Página atual:** marcada pelo **underscore** — barra de 2,5px em `--marcador`
sob o rótulo, `left/right 4%`, `bottom -4px`. Não se usa inversão de fundo,
porque a pílula já é sólida.

**Badge de pendência:** `top -5px; right -5px`, mínimo 20×20, `--er-c` sólido
(nos dois modos, pela regra do selo sólido em 1.4),
contagem em mono, anel de 2,5px na cor da própria pílula (não na cor do fundo da
página — a pílula flutua sobre conteúdo variável).

### 5.2 Pílula de ação

Mesmo formato, fundo `--acao` (`#0123FF` nos dois modos), texto branco.
**Sombra comum, sem brilho.** É a única pílula preenchida de acento na barra.

### 5.3 Selo de estado — **inerte**

```
min-height 26px · padding 0 11px · radius 999px
IBM Plex Mono 500 10,5px · letter-spacing .1em · CAIXA ALTA
contorno 1,5px currentColor + fundo currentColor a 9%
cursor default · nunca reage ao toque · nunca tem ▾
```

**A distinção contra navegação é de massa e de tipografia:** preenchido e grande
(Inter 600, 40px) = leva a algum lugar; contornado e pequeno (mono caixa alta,
26px) = informa e fica.

**Sólido × contorno:** sólido (cor cheia, texto branco) é **reservado ao estado
que exige ação** — atrasado, saldo negativo, vence hoje. Contorno para a rotina.
Motivo: num painel com doze cards, doze retângulos saturados viram papel de
parede e o alarme perde significado.

**Emenda da v1.2 — e é emenda, não substituição.** A regra acima continua valendo
**para status**. A **marcação de papel** (`--papel-*`, 1.6) tem forma própria: é
**sempre sólida, em tinta de papel, nunca contornada**. Não é contradição, é o
contrário dela — papel usa uma paleta que status não usa, então sólido ali não gasta
o sinal de alarme daqui. O selo de papel permanece **inerte**, como todo selo.

**O selo continua inerte.** O **controle de estado** (5.30) é componente distinto, com
seta, foco, hover e alvo de 44px. Não transformar o selo em botão: o mesmo desenho não
deve fazer dois trabalhos.

### 5.4 Busca retrátil

40×40 fechada (só lupa) → `min(300px, 42vw)` aberta, `width` em 220ms, foco
automático no campo, fecha ao perder foco se vazio. **A lupa carrega o verbo, o
placeholder carrega o escopo:** `RDO, marco, material, pessoa…` — nunca repetir
"pesquisar".

**A busca nunca é pílula sólida**, para não se confundir com navegação.

*Alternativa recomendada para avaliação: paleta central tipo Cmd+K — idêntica no
celular e no desktop, e sem animar largura.*

### 5.5 Cápsula de marca (canto superior direito)

`Lavrō | Minhas obras | avatar` num único invólucro `--cap-bg`, radius 999px.
Acompanha o tema. O mácron usa `--marca-cap`.

### 5.6 Cartões

| Perfil | Forma | Quando |
|---|---|---|
| **Registro** | topo **reto** + régua de 4px, `radius 0 0 12px 12px` | carrega decisão ou registro assinado — RDO, marco, alerta |
| **Apoio** | quatro cantos 12px, sem régua | lista, filtro, formulário, consulta |

**A régua herda a cor do status** quando o cartão tem estado. Topo reto e régua
andam juntos: topo reto sem régua parece corte acidental.

Modal e sheet mantêm os quatro cantos — no celular o topo reto encosta na borda.

### 5.7 Assessor (card de IA)

Superfície de marca **contida** (não full-bleed): `--azul` no claro,
`--azul-fundo` no escuro, radius 20px. Space Grotesk 700 em `clamp(21px,2.7vw,33px)`,
máximo 32ch. Linha mono com os três dados. Botão branco (a ação inverte sobre azul).

**Uma só ação azul por tela.** Azul elétrico preenchido marca a ação principal e a escolha
exclusiva de categoria. Azul como **estado** é permitido **apenas na coluna de estado**
(5.30), onde comunica "autorizado a executar" — nunca em cartão, faixa ou fundo.

Consequência a vigiar: numa obra bem tocada a coluna fica majoritariamente azul.
**Verificar em obra grande se isso lê como sinal ou vira parede.**

**O que é inteligência mora no azul; o que é dado bruto mora fora dele.** Data,
saudação e "dados ao vivo" ficam no hero, acima e descolados.

**Exceção escrita da v1.4 — o selo de plano.** Na lâmina de configuração (5.36) o selo de
plano é **azul elétrico sólido**, ao lado do nome da organização, e convive na mesma tela
com o primário *Salvar alterações*. É decisão do Michel, tomada em 02/08/2026 com o
protótipo aberto e **contra a recomendação de rebaixar o selo para neutro**: ele quer o
plano em destaque.

Fica escrita como exceção, e não corrigida em silêncio, porque a regra continua valendo
para todo o resto — **esta é a única superfície em que dois azuis sólidos coexistem**. O
que a segura de virar precedente: o selo é **inerte** (5.3), não tem alvo de clique e não
compete por gesto; e a lâmina é uma tela de configuração, onde não há fluxo de trabalho
para interromper. Fora dela, azul sólido continua sendo ação e só.

### 5.8 Cursor da IA

Marca de **procedência**, não de progresso: sinaliza "isto foi escrito por IA",
e **permanece depois de o texto terminar**.

```
display inline-block · width .62em · height .115em · min-height 2px
vertical-align -.16em
animation lv-caret 1060ms step-end infinite
@keyframes lv-caret { 0%{opacity:1} 50%{opacity:0} 100%{opacity:1} }
```

**Pisca seco**, como caret de linha de comando — `step-end`, sem transição.
`-0.16em` põe a base da barra 0,16em abaixo da linha de base e o topo a 0,048em:
a mesma posição que a Space Grotesk reserva ao glifo `_`.

**Frase de IA não leva ponto final — o underscore é o ponto.**

Exigências: respeitar `prefers-reduced-motion`; ter como desligar (a WCAG pede
mecanismo de parada para o que pisca por mais de 5s, e aqui pisca por projeto);
e o bloco leva **barra vertical de acento à esquerda**, para a procedência seguir
legível com movimento desligado.

### 5.9 Gaveta e popup

| Superfície | Borda | Gatilho |
|---|---|---|
| Navegação da obra | **esquerda**, `--azul` / `--azul-fundo` | pílula da obra |
| Perfil | **popup central**, `--sup-1` neutro | avatar |

**Gatilho e gaveta sempre na mesma borda, sem exceção.** Isso vale igual no
celular e no desktop — não existe hambúrguer separado.

O perfil é popup e não gaveta para a gaveta azul não perder força por repetição.

Gaveta: largura `min(370px, 88vw)`, itens de 52px (pai) e 42px (filho),
**sombra só quando aberta** (erro cometido: projetava sombra recolhida).

### 5.10 Modal de registro (+ Novo)

Disparado pela pílula `+ Novo`. É o **ato central do sistema** — montar o
documento que depois será lavrado —, e por isso é modal centralizado, não
submenu: submenu trataria o ato principal como item de navegação.

**Forma:** centralizado, `min(560px, 92vw)`, radius 20px, azul cheio
(`--azul` no claro, `--azul-fundo` no escuro). Título em
`clamp(24px,4vw,32px)`. Opções em Space Grotesk 700 26px, com `+` a 55% de
opacidade antes de cada nome, descrição em mono 10px. **Sobre azul, nenhuma
ação é azul** — os itens são texto branco, sem botão de acento.

**O título É a frase rotativa da seção 9.** Não é texto fixo.

**Escopo — as quatro opções:**

| Opção | Descrição (mono, sob o nome) |
|---|---|
| **Nova RDO** | relatório diário · efetivo, clima, serviços, fotos |
| **Registro** | ocorrência avulsa · foto, nota, evento da obra |
| **Pergunta** | questão formal à equipe ou ao cliente · fica no histórico |
| **Ata de reunião** | decisões e presentes · entra no acervo da obra |

Ordem fixa: Nova RDO primeiro, porque é o caminho de todo dia.

**Por que "+ Novo" e não "+ Nova RDO":** quando Pergunta e Ata existirem, um
botão "Nova RDO" fixo estaria errado metade do tempo. O guarda-chuva certo
agora evita renomear depois. Custo: um toque a mais para a RDO diária. Se a
telemetria mostrar que a maioria absoluta dos usos é RDO, cabe atalho (toque =
modal, toque longo = RDO direto) — otimização para depois, não agora.

**Armadilha de tipografia:** a palavra marcada pelo underscore precisa de
invólucro `white-space:nowrap` junto da pontuação — a palavra é `inline-block`
e o navegador quebra depois dela, deixando o "?" órfão.

**Estado no repositório, e as quatro entram na lista mesmo dormentes.** O modal
não existe no app: não há pílula `+ Novo` (a navegação da 8 é a onda seguinte).
Das quatro opções, **Nova RDO** tem tela própria (`Rdo.jsx`) e as outras três
correspondem a tipos que a tabela `registros` já grava —
`tipo in ('pedido','registro','ata','aviso','resposta')`, migration `v14`:

| Opção da interface | `registros.tipo` | Situação |
|---|---|---|
| Nova RDO | — (tabela `rdos`) | existe |
| Registro | `registro` | tipo existe; **criação pela interface, não** |
| Pergunta | `pedido` | o cliente já cria pelo "Fale com a Baraka"; o lado da obra, não |
| Ata de reunião | `ata` | tipo existe; **criação pela interface, não** |

**O nome na interface é o desta seção, não o do banco** — `pedido` é a coluna,
"Pergunta" é a palavra que o usuário lê. Opção dormente aparece no modal quando
existir a tela que ela abre; até lá a lista aqui é o alvo, não o retrato.

**Delimitação da v1.3: a superfície de marca é do modal de ESCOLHA, não de tudo que o
"+ Novo" abre.** Escolher entre quatro caminhos em azul cheio funciona; **preencher
formulário sobre azul cheio, não** — o desenho de campo da 5.14 pressupõe superfície
neutra, e campo claro sobre azul saturado vira caixa flutuando sem pertencer a nada.

Regra: **o modal de escolha é azul; a folha que ele abre é `--sup-1`.** A folha de convite
(5.35) é o primeiro caso — ela é formulário, então é neutra, mesmo tendo sido aberta pelo
"+ Novo".

### 5.11 Gráficos

| Componente | Regra |
|---|---|
| Donut | `stroke-dashoffset` em 900ms; é o **gesto principal** da tela |
| Barras verticais | `transform: scaleY` de origem inferior; grandeza pode crescer |
| Barra de Gantt | `scaleX`; a barra **ativa fica sólida** e emana **aura** (nunca pisca para o branco) |
| Rail de meses | bolinha 8px em botão de 30px; acima de ~10 meses agrupar por trimestre |

### 5.12 Carrossel

5s por item, crossfade de 600ms **só em opacity**, pontos indicadores, pausa em
hover/foco, setas de teclado, estático em movimento reduzido.

**Regra dobrada, e assumida:** avanço automático não é revelação nem estado —
seria decoração. Justifica-se porque aqui **o conteúdo em movimento é a
informação** (a obra recente). As guardas acima são o preço da exceção.

### 5.13 Botão

```
min-height --toque (48 / 44 compacto) · padding 0 20px · radius 999px
Inter 600 13px · borda 1,5px solid transparent
:active transform scale(.97) em --t-toque
```

| Nível | Fundo | Texto | Quando |
|---|---|---|---|
| **Primário** | `--acao` | `--sobre-acao` | a ação que a tela existe para fazer. Um por superfície |
| **Secundário** | transparente, borda `--linha-forte` | `--texto` | alternativa, cancelar, navegar |
| **Positivo vazado** | transparente, borda e texto `--ok` | `--ok` | confirmar liberação |
| **Destrutivo sólido** | `--er-c` nos dois modos | branco | dentro de confirmação (5.25) |
| **Destrutivo vazado** | transparente, borda e texto `--er` | `--er` | dentro de painel ou lista de detalhes |
| **Sobre azul** | branco | `--azul-fundo` | herda de 5.10 |

**`:disabled` = `opacity .45` + `cursor:not-allowed`. Nunca esconder o botão para indicar indisponibilidade** — desabilitar comunica que a ação existe e que agora não dá; esconder faz procurar. A mesma regra vale para **item de menu**: opção impossível aparece desabilitada **com o motivo escrito**, não sumida.

Abaixo de 720px o primário de uma barra de ferramentas ocupa largura cheia.

### 5.14 Campo de texto e campo de seleção

```
rótulo    IBM Plex Mono 500 10px · .12em · CAIXA ALTA · --texto-3
campo     min-height --toque · padding 12px 15px · radius --r-md
          fundo --sup-2 · borda 1,5px --linha-forte
:focus    borda --acento
dica      Inter 12px --texto-3 à esquerda · contador à direita
erro      Inter 12,5px --er — SUBSTITUI a dica, não empilha
.err      borda do campo em --er
.mono     variante para código: IBM Plex Mono, letter-spacing .04em
```

1. **Rótulo sempre visível.** Placeholder não é rótulo: some quando mais se precisa dele.
2. **Dica e erro na mesma linha**, alternando. Empilhar faz o formulário pular de altura ao validar.
3. **O erro descreve o que fazer**, não o que a máquina sentiu.

**Campo de seleção** é a mesma caixa em `radius 999px`, `appearance:none`, seta em CSS. `<select>` nativo é permitido — a proibição de diálogo nativo vale para **confirmação**.

**Campo com autocompletar** usa o menu flutuante (5.20) como lista de sugestões, nunca um contêiner absoluto dentro do modal — seria cortado pelo `overflow` da folha.

### 5.15 Campo de busca de escopo local

```
min-height --toque · radius 999px · fundo --sup-2 · borda 1,5px transparente
lupa 15px --texto-3 · botão limpar (30px) só quando há texto
:focus-within borda --acento
```

**Não é a busca 5.4.** A 5.4 é global, mora no cabeçalho, é pílula sólida retrátil. Esta filtra conteúdo já carregado, mora **dentro** do contêiner e é vazada.

**Posição — a regra é relativa, não fixa (emenda v1.2): a busca acompanha o lado da coluna que ela filtra.** Ela é acessório da lista, não cabeçalho da página, e o que se encurta é o caminho do olho entre o que se digita e o que se lê:

| Tela | Lado | Porque a coluna filtrada é |
|---|---|---|
| Janela de arquivos (5.19) | **direita**, ~52% da largura, ao lado da ordenação e do alternador de vista | número e data, que ficam à direita |
| Pessoas | **esquerda** | o nome, que é a primeira coluna |

A v1.1 escrevia "encostada à direita" como regra geral — era **um caso generalizado cedo demais**. Abaixo de 900px ocupa a largura toda, dos dois lados.

**O placeholder declara o escopo:** `Filtrar nesta pasta`. Filtra nome **e código do documento**, em memória, **só no nível atual** — e o estado vazio correspondente precisa dizer isso (5.27).

### 5.16 Caixa de seleção e seleção múltipla

```
desenho   19px · radius 5px · borda 1,7px --linha-forte
alvo      44px × 44px SEMPRE
marcada   fundo e borda --acao · marca em --sobre-acao
parcial   propriedade nativa `indeterminate`, não uma terceira arte
:focus-visible outline 2px --acento offset 2px
```

Primeira coluna da tabela, 52px. A do cabeçalho seleciona tudo do nível.

**Na vista em grade não há cabeçalho**, então o mesmo trabalho é feito por um **botão "Tudo"** ao lado do alternador de vista, que alterna para *Limpar (N)* quando há seleção. Ele existe **apenas em grade** — na lista, dois controles para a mesma coisa confundiriam.

**Linha selecionada** `color-mix(--acao 10%)`. **Linha ativa** (a que está nos detalhes) `color-mix(--acao 16%)` + `inset 3px 0 0 --acento`. São estados diferentes: marcar para agir em lote não é o mesmo que olhar um item.

**Ações em massa vivem na barra de endereço**, não numa barra flutuante nova: contagem e limpar à esquerda, ações à direita. Barra flutuante foi rejeitada — cobre conteúdo e cria uma segunda gramática de ação.

### 5.17 Categoria de visibilidade

Toda pasta e todo arquivo pertencem a **uma** categoria, e é ela que decide quem vê:

| Categoria | Organização | Contratante | Campo |
|---|---|---|---|
| **Aberta** | vê | vê | vê |
| **Contratante** | vê | vê | — |
| **Campo** | vê | — | vê |
| **Só a organização** | vê | — | — |

**Não é escada de sigilo.** Contratante e Campo são irmãos que se excluem.

**A visibilidade mora na categoria, nunca no arquivo.** Razão técnica: RLS filtra linha, não coluna — categoria são quatro ramos de policy, enquanto etiqueta por arquivo é uma chance nova de errar em cada upload.

**Não é gabarito fixo.** A mesma pasta de notas fiscais é Aberta numa obra por administração e Contratante numa empreitada a preço fechado. Depende do contrato.

#### Frentes contratadas decidem quais categorias existem

| Frente | Categorias |
|---|---|
| **Projetos** | Aberta · Contratante |
| **Obra** | Aberta · Contratante · Campo · Só a organização |

*Campo* não faz sentido sem o módulo de obra. *Só a organização* também não: documento pessoal só entra quando há operário cadastrado para uma obra.

**Consequência de esquema, e ela é grave se ignorada:** categoria **não pode ser enum fixo**. Precisa ser tabela por organização, ou habilitar e desabilitar frente vira migration com dado vivo. Pastas espelho também carregam a frente — *Fotos dos RDOs* só existe na frente de obra.

#### Seletor

```
pílula SÓLIDA em --azul (#0123FF), texto branco, NOS DOIS MODOS
min-height 40px · radius 999px · Inter 700 14px · seta 7px em CSS
```

Primeiro item da barra de endereço. **Lista apenas categorias.** Listar também as pastas raiz foi tentado e removido: era mostrar filhos num lugar onde a lista principal já mostra filhos.

**Sólido contra vazado** distingue *escolhida* de *disponível* num grupo que se exclui. A 5.1 diz que a pílula de navegação não usa inversão porque já é sólida; aqui a inversão faz outro trabalho. Variante, não contradição.

**O seletor existe para todos os papéis**, mostrando só as categorias que aquele papel alcança. Esconder o mecanismo faria o operador subir arquivo sem saber quem lê.

#### Declaração de público

Segunda linha da barra: risco de 3px + rótulo mono + texto. Risco em `--bar-acento` quando Aberta, em `--bar-at` quando restrita — **a restrição é o que precisa ser notado**. Reaparece na folha de envio, **antes** de o arquivo ser aceito.

### 5.18 Pasta espelho

Pasta `tipo = espelho` é **vista de outro módulo**, não armazenamento próprio.

- Sem envio, sem excluir. Faixa (5.26) dizendo **onde se edita de verdade**.
- Estado vazio próprio, sem convite para agir.
- **Espelho e trava são hereditários**: valem para a pasta e tudo abaixo.

**Somente leitura vale para o conteúdo, não para o estado.** Nada entra nem sai de uma pasta espelho, mas **o estado de uma revisão continua editável a partir dela** — o estado pertence à revisão, não à pasta. Sem essa distinção, o caminho de recuperação de 5.30 não existe.

**Marcador `espelho`** tem classe própria (`tag-esp`): contorno neutro, mono 9px, **fora da paleta de status**. Ele descreve a *origem* do dado, não a situação dele — usar um selo de estado ali vestiria "espelho" de "superada".

**Motivo do espelho, e é de LGPD:** duplicar documento pessoal duplica a superfície de exposição *e* a obrigação de eliminação. Um pedido do titular passaria a ter dois lugares para varrer, e o segundo é o que se esquece.

**Limite conhecido:** *"a organização mais a subempreiteira dela"* não é expressável enquanto `profiles.role` souber apenas `operador`, sem saber de qual empresa. Por isso a pasta de pessoas fica **Só a organização** até existir a dimensão de subempreiteira.

### 5.19 Janela de arquivos

**Barra de endereço e lista são um corpo só.** Nenhuma folga, raio apenas nas pontas externas, uma sombra `--e-2` no conjunto.

```
.janela   radius --r-md · sombra --e-2 · fundo --sup-1
.end      radius --r-md --r-md 0 0 · fundo --bar-bg
corpo     grade: lista (1fr) + detalhes (344px) · min-height --alt-janela
```

Não é cartão de apoio (5.6) nem pilha deles: é uma **janela**. É a colagem que faz a tela ser lida como navegador de arquivos, e essa leitura dispensa explicação para quem já usou Finder ou Explorer.

#### Tokens próprios `--bar-*`

Valores na 1.6.

**A barra é sempre escura, independente do tema.** Nenhum outro componente do `02` tem essa liberdade. Aqui a superfície é o que identifica a tela, e identidade não deve oscilar com preferência de tema.

**`--bar-acento` não é um segundo azul.** É a 1.2 aplicada: elétrico como preenchimento vale nos dois modos; como traço fino sobre escuro, reprova. A categoria sólida permanece `#0123FF`; só o contorno se ajusta.

#### Conteúdo

```
linha 1   [voltar] [categoria ▾] / segmento ▾ / segmento ▾ … [ações]
linha 2   | QUEM PODE VER: …
ações     [N selecionados ✕] [Mudar estado N ▾] [Excluir N] [Nova pasta] [Baixar N] [Enviar]
```

Abaixo de 960px a linha 1 quebra: caminho em cima, ações embaixo com rolagem horizontal e o vazado de acento primeiro.

### 5.20 Menu flutuante e migalha suspensa

```
menu      position:fixed em CAMADA PRÓPRIA, nunca dentro do contêiner que rola
          --sup-1 · radius --r-md · padding 6px · sombra 0 26px 70px + 1px --linha
item      min-height --toque · marca de escolhido em --acento à esquerda
          rótulo Inter 600 14px + descrição mono 10,5px --texto-3
          desabilitado: opacity .5, cursor not-allowed, motivo na descrição
grupos    rótulo mono 9px .14em CAIXA ALTA, separados por hr
```

**Camada própria é requisito:** a migalha rola horizontalmente e um menu dentro dela seria cortado pelo `overflow`. Um nó único, reposicionado por `getBoundingClientRect`, fechando em clique fora, `Escape`, rolagem e redimensionamento.

#### Modo de escolha múltipla (v1.2)

O mesmo menu atende **escolha múltipla** — filtrar por vários papéis, vincular várias obras — com quatro diferenças:

```
marca      caixa QUADRADA (5.16), não a marca de escolhido à esquerda
busca      campo interno a partir de SETE itens
rodapé     Marcar todas · Limpar, separado por hr
fechamento NÃO fecha a cada marcação — só em clique fora, Escape ou no gatilho
```

**Por que menu e não grade de caixas na própria tela:** a grade cresce com o cadastro — vinte obras viram vinte linhas empurrando o resto —, o menu não. O menu tem tamanho fixo e a busca interna absorve o crescimento.

**Fechar a cada marcação é o defeito clássico** deste componente: quem escolhe três papéis abre o menu três vezes. Aqui a confirmação é implícita — sai fechando.

#### Migalha: irmãos, não filhos

**Cada segmento abre as pastas do MESMO nível**, com a atual marcada. Em `Projetos aprovados`, oferece *Relatórios aprovados* e *Fotos dos RDOs*; dentro de `Arquitetura`, oferece *Instalações, Estrutura, Interiores, Catálogos*.

Filhos já estão na lista principal — mostrá-los no menu era redundância. **Navegação lateral não estava em lugar nenhum**, e é o que a migalha passa a resolver. É o comportamento da barra de caminho do Finder.

Segmento sem irmãos não recebe seta e navega direto.

**Isto substitui a árvore fixa à esquerda, rejeitada** por três razões: duplica a navegação existente; ocupa a borda que a 8.1 reserva ao gatilho da obra; e não tem para onde ir no celular, criando dois modelos de navegação por largura.

### 5.21 Tabela de dados com ordenação

```
th        mono 10px .12em CAIXA ALTA --texto-3 · botão de 32px
          seta 5px --acento, invisível quando aria-sort="none"
td        height --alt-li (48 / 44) · border-top 1px --linha
:hover    linha em --sup-2 (só onde existe ponteiro)
```

**Ordem das colunas:** seleção · **estado** · nome · revisão · tamanho · enviado · por · ações.

**Estado é a primeira coluna de conteúdo**, antes do nome. Foi testado com o selo ao lado do nome e a informação aparecia duas vezes; à esquerda e em coluna própria, o nome recupera largura e a leitura respira.

- Estado de ordenação em **`aria-sort`**, não em classe.
- Primeiro clique em número ou data ordena **decrescente**; em texto, crescente.
- **Data é CÓDIGO** (4.1): mono, tabular, nunca animada. **Tamanho é GRANDEZA:** Space Grotesk 700, tabular, à direita.
- Ordenação também como campo de seleção — no celular não há cabeçalho para clicar.
- **Não existe coluna de tipo.** O tipo virou selo colorido no nome (5.22).
- O cabeçalho é renderizado dinamicamente e **cada coluna carrega a chave de tradução junto do rótulo**. Cabeçalho montado em JS sem `data-t` fica fora do i18n e nunca traduz — sem sintoma visível.

#### Pasta é linha, não pílula

Pastas e arquivos convivem na mesma lista, **pastas sempre primeiro**, independente da ordenação. A pasta mostra contagem recursiva na coluna de tamanho, em mono `--texto-3` (é contagem, não grandeza), e uma seta à direita.

Disciplina passa de dez com facilidade, e dez pílulas em rolagem horizontal não se leem. **Cada componente com um trabalho: pílula escolhe público, linha navega.**

#### Forma da linha abaixo de 720px

Cabeçalho oculto; a linha vira **dois andares** em `grid 44px 1fr 44px`:

```
andar 1   selo de tipo + nome
andar 2   faixa mono 10,5px --texto-3: estado · tamanho · data · autor
pontas    seleção (44px) à esquerda, ação (44px) à direita · mínimo 58px
```

Mesmo dado, mesma ordenação, outro arranjo. Ver 8.3.

### 5.22 Selo de tipo de arquivo

```
32px · radius 8px · fundo color-mix(cor 16%) · texto na cor
sigla mono 700 9px: PDF · DWG · XLS · IMG · DOC · ZIP · ARQ
distintivo "+N" no canto quando a revisão tem mais de um arquivo
```

Tokens **`--tipo-*`**, valores na 1.6.

**Regra inviolável de contenção:** cor de tipo existe **só dentro do selo**, e **status nunca entra no selo**. Sem isso o vermelho de PDF conversa com o vermelho de atrasado e os dois perdem significado.

**DWG é ciano, não azul.** Azul de DWG ficaria a um passo do azul da marca, e um selo azul ao lado de um botão azul ensina que os dois são a mesma coisa.

Estas cores **não são tematizáveis pelo cliente** e não pertencem à paleta de status.

#### O selo vira botão quando o arquivo pré-visualiza

**Pré-visualizam: PDF e imagem.** DWG precisa de visualizador próprio; planilha e texto precisariam de conversão no servidor; ZIP nunca.

Quando pré-visualiza, o selo é `<button>` com contorno no hover e `title` de pré-visualizar. Quando não, continua `<span>` inerte. **A affordance não mente:** o vermelho do PDF convida, o ciano do DWG não.

### 5.23 Detalhes do item — um renderizador, dois recipientes

| Largura | Recipiente |
|---|---|
| **≥ 1180px** | coluna de 344px dentro da janela |
| **< 1180px** | modal central `min(520px, 92vw)` |

```
coluna    border-left 1px --linha · fundo color-mix(--sup-2 45%)
conteúdo  selo grande + código + título + pílula de estado
          prévia (botão quando pré-visualiza) · dados · arquivos da revisão
          histórico (avançado) · blocos reservados · ações
dados     linha de 38px: chave mono CAIXA ALTA | valor à direita
```

**Sem redundância:** código e estado aparecem **só no topo**. Repeti-los na tabelinha de dados era a mesma informação duas vezes.

**A coluna não encolhe: abaixo do corte ela deixa de existir.** Coluna estreita demais não informa, e componente duplicado divergiria na primeira alteração.

**Nunca gaveta.** A 8.1 reserva a borda direita à cápsula de perfil.

#### Altura estável — regra nova

```
--alt-janela: clamp(430px, 58vh, 640px)
.corpo-janela { align-items:start; min-height: var(--alt-janela) }
.painel { position:sticky; top:76px; height: var(--alt-janela); overflow:hidden }
.painel .corpo-p { overflow-y:auto; flex:1 1 auto; min-height:0 }
```

**O painel auxiliar não empurra o layout.** Ele tem altura própria e rola por dentro; a janela reserva o mesmo mínimo. Consequência: **selecionar um item nunca muda a altura da página**, e em lista longa o painel acompanha a rolagem.

A área vazia abaixo de uma lista curta continua existindo — mas já está lá antes do clique. **Era o salto que incomodava, não o espaço.**

#### Dois cuidados de implementação, ambos custaram bug no laboratório

1. **A regra que esconde a coluna precisa de especificidade maior que a regra base:** `.corpo-janela > .painel` (0,2,0), não `.painel` (0,1,0). Com especificidade igual, a base — que vem depois na folha — ganha, a coluna nunca se esconde e **cai numa segunda linha implícita da grade, embaixo da lista**: nem coluna, nem modal, um terceiro comportamento que ninguém desenhou.
2. **A verificação em JS deve testar largura ocupada**, não só visibilidade. Confiar em `offsetParent` deixa o modal sem abrir no estreito.

#### Onde o botão de ações da linha (*kebab*) leva

Acima do corte, menu curto de ações. **Abaixo, ele abre o modal de detalhes** — sem painel, os dois seriam caminhos concorrentes, e o modal informa mais: mostra o público e o aviso antes de a pessoa agir.

### 5.24 Zona de envio e progresso

```
zona      borda 1,5px TRACEJADA --linha-forte · radius --r-md
:sobre    borda --acento + fundo --sup-2      (arrastando)
:erro     borda --er
progresso pista 5px --sup-3 · barra --acento em scaleX, origem à esquerda
```

1. **A zona não é permanente.** No desktop vive na folha de envio e reage ao arraste; no dedo **não existe arrastar**, então o caminho é o botão.
2. **A zona não é azul cheia.** Colidiria com 5.2 e 5.7. O acento entra no **contorno**.
3. **Progresso é por arquivo.** Uma barra só, para dois arquivos de 40 MB, não diz qual falhou.
4. **Progresso é `scaleX`, determinado.** Roda indeterminada é proibida.
5. **Falha não perde a seleção.**

#### Envio em pasta com controle de revisão

Ganha dois campos antes da zona: **Documento** (código, mono, com autocompletar) e **Revisão**. Um terceiro campo, **Título**, aparece só quando o código é novo — depois ele é herdado.

**A comparação de código é normalizada:** maiúsculas, sem espaço, hífen, ponto ou sublinhado. É isso que faz `spk mar prj 001` e `SPK-MAR-PRJ-001` caírem no **mesmo** documento em vez de criarem dois — e o erro de digitação silencioso é o que mataria o controle de revisão inteiro.

**Revisão repetida no mesmo documento é erro nomeado**, não silêncio.

**A revisão nova entra sempre em `em análise`.** Uma faixa avisa que ela **não substitui a vigente** e que o campo continua vendo a anterior.

### 5.25 Confirmação destrutiva

```
modal central min(500px,92vw) · superfície --sup-1 NEUTRA
título: pergunta direta · etiqueta mono com o ALCANCE da ação
alvo:   nome exato, mono sobre --sup-2, com word-break
        em lote: até 12 nomes + "mais N", com rolagem
ações:  Cancelar (secundário) · Excluir (destrutivo sólido)
≤560px  empilhados, ordem invertida: o destrutivo em baixo
```

**Nunca a superfície de marca do 5.10.** Usar a mesma superfície para criar e para destruir ensina o gesto errado.

**O nome do objeto é obrigatório na tela.** Em lote, diz quantas pastas há na seleção e que o conteúdo delas sai junto.

**Diz o alcance real:** *"a ação vale para todos que veem esta categoria"*.

Nunca `confirm()` nativo.

### 5.26 Faixa de aviso em linha

```
radius 0 --r-md --r-md 0 · borda-esquerda 3px · fundo --sup-2
rótulo mono 10px .12em CAIXA ALTA --texto-3 · corpo Inter 13px --texto-2
```

| Variante | Borda | Usos |
|---|---|---|
| **atenção** | `--at` | categoria restrita · revisão entrando em análise |
| **informativa** | `--acento` | pasta espelho · quem vai ver o arquivo |

Distinta do `.nota` do `03`, que é anotação de laboratório. Nenhuma animação.

**Não usar faixa para explicar encanamento.** O aviso de "link temporário de 60 minutos" foi removido: descrevia o funcionamento interno do armazenamento privado, não algo que o usuário decide ou controla. Detalhe de implementação não vira interface.

### 5.27 Estado vazio — são cinco, não um

```
marca 52px, borda 1,5px tracejada --linha-forte, radius --r-md
título Space Grotesk 600 18px · texto Inter 13,5px --texto-2, máx 46ch
ação primária centralizada apenas quando houver o que fazer
```

| Caso | Diz | Ação |
|---|---|---|
| **Categoria sem pastas** | que se começa pelas pastas de primeiro nível | Nova pasta |
| **Pasta vazia** | o que enviar, e quem verá quando subir | Nova pasta · Enviar |
| **Filtro sem resultado** | **o escopo do filtro** — nome e código, só neste nível | Limpar filtro |
| **Espelho vazio** | onde o registro nasce | nenhuma |
| **Nada liberado** | que existe documento, mas nenhuma revisão liberada | nenhuma |

**O último caso é o mais importante e o menos óbvio.** Uma pasta com documentos só em análise aparece **vazia** para o operador. Sem um texto próprio, ele conclui que a pasta está errada ou que perdeu arquivo.

**A diferença entre pasta vazia e filtro sem resultado** é a segunda mais importante: mesmo texto nos dois casos faz o usuário concluir que perdeu o arquivo.

### 5.28 Esqueleto de carregamento

```
blocos --sup-3 · altura 11px (32px no selo de tipo) · radius --r-sm
pulso em OPACITY: lv-pulso --t-pulso · atraso 120ms por linha, teto 400ms
```

Fecha a exigência da 6.5, que pedia esqueleto sem ter componente.

**Pulso em `opacity`, jamais `background-position`.** O brilho varrendo do *shimmer* animaria posição de fundo e exigiria exceção à 6.1/6.3. Sob movimento reduzido, blocos cinza estáticos continuam sendo a informação certa.

**O esqueleto imita a grade real**, incluindo a coluna de seleção.

### 5.29 Faixa de conexão

```
position:fixed no topo · acima de tudo · min-height 46px
fundo --at-solido SÓLIDO nos dois modos · texto branco
ponto de 10px pulsando em opacity · rótulo mono 600 CAIXA ALTA
empurra o cabeçalho e o topo do painel sticky
```

**Não é descartável.** Sem botão de fechar, e desabilita enviar, criar pasta, baixar e mudar estado — não esconde: **desabilita** (5.13).

**Âmbar, não vermelho.** Vermelho significa **dado com problema**: atrasado, saldo negativo, falha de regra. Perda de conexão não é falha do dado, e gastar vermelho nela dilui o vermelho onde ele importa.

> **Mudou na v1.2, e o código está atrás.** Esta faixa era `--at-c` — branco sobre
> `#B26A00` dá **4,24:1** e reprova AA (1.4). É o **único lugar do sistema onde âmbar
> aparece sólido com texto branco**, e por isso o único afetado pela correção. No
> repositório: `src/lavro.css:360` (`.lv-conexao`) segue em `var(--at-c)` e o
> `src/tokens.css:120` ainda descreve `--at-c` como "faixa de conexão sólida". Trocar é
> duas linhas — **não feito aqui**, porque muda pixel no módulo que está no ar.

### 5.30 Estado de revisão — selo e controle

#### O modelo tem quatro níveis, não dois

| Nível | O que é | Exemplo |
|---|---|---|
| **documento** | identidade estável, emitida por quem projeta | `SPK-MAR-PRJ-001` |
| **revisão** | identidade emitida pelo projetista, com estado | `R04`, liberada |
| **versão** | evento de upload, automático, sequencial | `v2` daquela revisão |
| **arquivo** | o binário | `.pdf` e `.dwg` |

**Uma revisão carrega N arquivos.** PDF para ler, DWG para trabalhar, ambos da R04. Se arquivo e revisão forem a mesma coisa, a R04 existe duas vezes e a lógica de superar não sabe qual superar. É o erro que obriga a refazer o módulo.

#### Os quatro estados

| Estado | Cor | Significado |
|---|---|---|
| **em análise** | `--at` âmbar | rascunho — o campo não vê |
| **aprovado** | `--ok` verde | conferido, mas ainda não autorizado a executar |
| **liberado** | `--est-lib` **azul elétrico** | autorizado a executar em obra |
| **superada** | `--texto-3` cinza **riscado** | deixou de ser vigente |

Valores de `--est-lib` na 1.6.

**Aprovado ≠ liberado.** Aprovado é ato técnico: alguém conferiu e aceitou. Liberado é ato de gestão: está autorizado a executar. A folga existe quando a aprovação acontece mas a liberação espera a frente de serviço chegar. Nesse intervalo o projeto está certo e **ninguém deve executá-lo ainda**.

**Superada é cinza, não vermelho.** Vermelho é dado com problema; revisão arquivada não é problema. O problema é o papel na mão de alguém — e é lá, no QR da cópia impressa, que o vermelho deve morar.

#### Selo × controle de estado

O **selo** continua sendo o que a 5.3 define: inerte. O **controle de estado** é componente novo:

```
min-height 34px · radius 999px · borda 1,5px transparente
fundo color-mix(--sc 14%) · texto --sc · seta de 7px
:hover  borda --sc      ·  alvo de 44px garantido pelo invólucro
```

Renderiza como controle quando o papel pode e a rede está de pé; como selo inerte quando não.

#### As regras de transição

**O menu mostra SEMPRE os quatro estados.** As transições impossíveis aparecem **desabilitadas com o motivo escrito** — menu com uma opção só parece quebrado, e opção sumida faz procurar.

| De | Para | Permitido |
|---|---|---|
| qualquer | **superada** | **nunca manualmente** — ver abaixo |
| qualquer | o próprio estado | não ("já está neste estado") |
| **superada** | liberado | **sim** — é o caminho de recuperação |
| liberado | análise, aprovado | sim, com confirmação |

**Superada é consequência, não escolha.** Marcar à mão deixaria o documento **sem vigente** e o campo sem prancha, em silêncio. Ela é produzida pelo gatilho.

**O gatilho dispara ao LIBERAR, jamais ao subir.** Se a R05 entra em análise e obsoleta a R04 imediatamente, o montador fica sem prancha válida enquanto a nova ainda está em conferência. Numa obra de combate a incêndio isso não é detalhe.

**De superada dá para voltar a liberado.** Se a R05 der problema, reativa-se a R04 e ela supera a R05. Isso exige que o estado seja editável também de dentro da pasta espelho de superadas (5.18).

#### Confirmação em dois sentidos

- **Vira liberado:** nomeia qual revisão passa a superada e avisa que as cópias impressas dela ficam inválidas.
- **Sai de liberado:** avisa que o documento **deixa de ter revisão vigente** e some da lista do campo, e que quem já imprimiu continua com o papel na mão.

As demais transições aplicam direto.

#### Superadas é pasta espelho automática

Uma por pasta controlada, filha dela, herdando a categoria, **gerada por consulta**. Nada é movido de lugar.

Movimentação física quebraria três coisas: a categoria da pasta de destino brigaria com a de origem e a visibilidade vazaria; o histórico se desprenderia do documento; e "mover" é justamente o que está fora de escopo por ser perigoso.

**Aparece apenas no modo avançado** (5.33). A lista principal mostra **uma linha por documento**, a vigente — poluição zero.

### 5.31 Vista em grade

```
grade   repeat(auto-fill, minmax(152px,1fr)) · gap 12px
bloco   min-height 158px · radius --r-md · ícone de 66px
        código mono 9,5px · nome 12,5px em 2 linhas com clamp
        contagem ou tamanho · controle de estado no pé
seleção caixa no canto superior esquerdo, sempre visível
```

Alternador de vista à direita, na barra de ferramentas.

**Na grade, um clique na pasta abre.** É navegação de principiante: duplo clique não se ensina, e no dedo ele não existe.

O botão **Tudo** (5.16) aparece só nesta vista.

### 5.32 Barra de consumo de armazenamento

```
grandeza em Space Grotesk 700 · limite em mono CAIXA ALTA
pista 6px · radius 3px · fundo --sup-3
        box-shadow: inset 0 0 0 1px var(--linha-forte)
preenchimento --neutro · --at acima de 80% · --er acima de 95%
```

**O fio é sombra interna, não borda:** não altera a altura da pista e é **coberto pelo preenchimento**, sobrando apenas no trecho vazio — que é onde o contraste faltava. Sem ele, a pista em `--sup-3` fica quase do mesmo tom do gradiente de fundo, **nos dois temas**.

**Aqui o vermelho é legítimo:** acabar o espaço é problema do dado.

Mora no alto da tela, ao lado do título. A versão completa — histórico, quanto cada obra ocupa — mora na tela de Configurações.

### 5.33 Escalonamento de interface

O esquema é **sempre completo**. O que escalona é a interface, em dois eixos independentes:

| Eixo | Decide | Onde vive |
|---|---|---|
| **Plano da organização** | se o recurso **existe** para aquele cliente | `organizacao.recursos` |
| **Preferência do usuário** | se a superfície avançada **aparece** | perfil |

Aplicado ao controle de revisão, isso produz três níveis da **mesma tela**:

| Nível | O que se vê |
|---|---|
| **Recurso desligado** | lista chapada dos **arquivos vigentes**. Nem coluna de revisão, nem estado, nem Superadas. A palavra "revisão" não aparece em lugar nenhum |
| **Simples** | uma linha por documento, coluna de estado, sem coluna de revisão, Superadas escondida |
| **Avançado** | coluna de revisão com número de versão, Superadas, histórico no painel, ação de liberar |

**O nível acessível é seguro por construção:** o que não é vigente simplesmente não é listado.

Há um terceiro eixo, mais grosso, que decide o que existe antes de tudo: as **frentes contratadas** (5.17).

#### Três travas

1. **Plano e preferência não se misturam.** Plano é comercial; preferência é do usuário. Um interruptor que leva a uma parede de venda é o pior resultado possível — o interruptor só deve existir se o plano já inclui.
2. **O escalonamento é do servidor, não do navegador.** Esconder campo enquanto a API aceita o valor produz dado inconsistente, que é pior que recurso vazado. O bloqueio vive na policy e no RPC.
3. **Não se vende o aviso de risco.** Pode-se vender a *capacidade de controlar revisão*. Não se pode vender o *aviso de que uma prancha está obsoleta*: se o dado existe, o selo aparece, em qualquer plano e para qualquer papel. Senão um rebaixamento de plano vira alguém executando por planta superada.

---

### 5.34 Referência de papéis — modal, não legenda

O que cada papel faz, aberto por um link no **subtítulo** da tela de Pessoas.

```
recipiente  modal grande sobre o fundo desfocado (2.3), saída explícita
grade       auto-fit, mínimo 266px, gap --gap-card
caixa       radius --r-md, padding --gap-card, tingida com a matiz --papel-* do papel
faz         Inter 600 14px, texto cheio          <- a informação principal
não faz     12,5px normal --texto-3, após filete <- ressalva, e parece ressalva
```

**A cor da caixa é a mesma matiz do selo da linha, e é ela que dispensa legenda.** Quem
vê um selo violeta na lista e abre a referência encontra a caixa violeta: a ligação é
visual e imediata, sem um mapa "esta cor significa aquilo".

**Por que modal e não seção no pé** (que foi o desenho da v5): o pé não se acha — quem
tem a dúvida está no meio da lista, não no fim da página. **E por que não rota própria:**
seria mais uma tela para manter, com navegação de ida e volta, para um conteúdo que se lê
em vinte segundos.

**Hierarquia é o ponto todo.** O que o papel **faz** é a resposta; o que ele **não faz** é
ressalva. Igualar os dois pesos transforma referência em contrato, e o leitor sai com a
impressão de que o papel é mais restrito do que é.

### 5.35 Folha de convite — dois passos

Formulário → link gerado. Superfície **neutra** (`--sup-1`), pela delimitação da 5.10.

**Passo 1 — o formulário.** Abre com uma **faixa informativa** (5.26) *antes* dos campos:

> O convite é um link. Nada sai por e-mail daqui.

**Essa faixa vem primeiro porque sem ela a pessoa preenche o e-mail achando que apertou
"enviar".** É o mal-entendido que o desenho inteiro existe para evitar.

| Campo | Regra |
|---|---|
| Obra | obrigatório; único da organização já vem escolhido |
| E-mail | **opcional** — anota de quem é o link e permite conferir no aceite |
| Mensagem | **opcional**, ≤180 caracteres, aparece na tela de aceite |

**Passo 2 — o link.** Recapitulação em **ficha** (obra, papel, destinatário) + o link + *Copiar link* como ação primária e *Criar outro* como secundária.

**Reenviar, sem e-mail, aparece desabilitado com o motivo escrito** — nunca sumido (5.13). Some é o que não se pode explicar; desabilitado com motivo ensina.

**Nada aqui depende de servidor de e-mail.** A mensagem viaja no próprio convite e aparece no aceite, então o recurso existe inteiro sem infraestrutura de envio.

### 5.36 Lâmina de configuração

A tela de configuração da organização **não é uma página, é uma lâmina sobre o app** — e
essa escolha carrega o argumento inteiro: o que se muda ali vale para tudo o que está por
baixo. Ver o app desfocado atrás é o que diz isso sem uma frase de ajuda.

```
camadas   conteúdo real → blur estático → véu → piso/teto de luminosidade → folha
z-index   fundo 0 · lâmina e piso 1 · folha 2      (estrutural, não cosmético)
véu       claro rgba(245,246,249,.16) · escuro rgba(14,17,22,.34)
blur      blur(17px) saturate(.95)
colunas   identidade 300–400px (sticky) + opções (teto 880px)
margem    clamp(48px, 9vw, 190px), ancoradas à ESQUERDA — não centradas
empilha   abaixo de 960px, identidade primeiro
```

**O blur aqui é estático, e por isso é barato.** A restrição da 2.3 vale para
`backdrop-filter` em elemento que rola, que repinta a cada frame; atrás da lâmina nada
rola. É o mesmo raciocínio que liberou o véu de modal na v1.3.

**O piso de luminosidade é o que torna a lâmina legível sobre qualquer conteúdo.** Sem ele
o texto atravessa um fundo que muda de claridade conforme a tela por baixo — e o contraste
deixa de ser uma propriedade do componente para virar sorte.

```
piso (claro)   mix-blend-mode: lighten com --n-300   só levanta o que é mais escuro
teto (escuro)  mix-blend-mode: darken  com --n-700
```

Medido no pior caso (painel grafite atrás): **`--texto` 9,4:1 · `--texto-2` 4,5:1** no
claro, e **12,9:1** no escuro. Passa AA.

**Limite conhecido, e ele vira regra:** `--texto-3` cai para ~1,6:1 sobre o piso. Então
**sobre a lâmina nada abaixo de `--texto-2` carrega informação** — dica em `--texto-3` só
na metade inferior, onde a textura do fundo já dissolveu.

**Ordem de pintura é estrutura.** `mix-blend-mode` mistura com tudo o que foi pintado
abaixo no mesmo contexto de empilhamento: trocar o z-index das três camadas não "muda um
detalhe", desmonta o piso.

**A coluna de identidade é sticky e a de opções rola.** Nome, selo de plano, consumo e
logo são o *sujeito* da tela — sair de vista enquanto se mexe nas opções faz perder de
vista o que está sendo configurado.

---

## 6. Movimento

### 6.1 As três regras

**1. Todo movimento é um gesto, e todo gesto tem um sujeito.** Antes de animar,
é preciso nomear o sujeito. **Um gesto principal por chegada de tela.** A cascata
não é o gesto — é a ordem de leitura.

**2. Só existem revelação e estado. O resto é decoração e sai.**

| | Revelação | Estado |
|---|---|---|
| Duração | tem fim | permanece |
| Repete no mesmo conteúdo? | **nunca** | sempre |
| Diz | "aqui está, nesta ordem" | "isto está vivo / pendente / sendo gerado" |
| Pode desligar? | não precisa | **tem de poder** |

Revelação que reexecuta a cada re-render é o erro clássico.

**3. A informação nunca espera o movimento.** Legível no frame 0; teto de atraso;
só `transform` e `opacity`; **código não anima, grandeza pode crescer**.

### 6.2 Tokens

```
--t-toque   120ms   press, feedback imediato
--t-ui      220ms   dropdown, selo, foco, busca — e a ENTRADA de superfície flutuante
--t-sai     140ms   a SAÍDA de superfície flutuante (6.8)
--t-entra   420ms   revelação de um elemento
--t-gesto   900ms   gesto principal (donut, barras)
--t-varre   820ms   varredura de tela cheia, total
--t-pulso  1500ms   estado (aura, dados ao vivo)
--t-caret  1060ms   caret da IA, step-end
--stagger    38ms   cascata

--e-saida  cubic-bezier(.25,.7,.3,1)   revelação
--e-ui     cubic-bezier(.3,.8,.3,1)    interface
```

### 6.3 Teto de atraso: **400ms**

Com dez elementos e 38ms de passo, o último entra a 380ms. **Acima de dez
elementos, entram em grupos, não em fila** — vinte cards em fila fariam o último
esperar 1,2s.

### 6.4 Reconciliação com o código atual

O `clienteUi.jsx` tem movimento com valores escolhidos a esmo. O que fica:

| Hoje no código | Vira | Por quê |
|---|---|---|
| `baraka-up .55s`, stagger `.06s` | 420ms, stagger 38ms, teto de 10 passos | a fila era infinita |
| donut `stroke-dasharray 1s` | 900ms, `stroke-dashoffset` | único valor folgado justificado: é o gesto |
| `baraka-live-ring/dot 1.6s` | 1500ms | unificado — eram 1,6s e 0,9s sem motivo |
| `baraka-caret .9s step-end` | 1060ms `step-end` | mantida a natureza seca; só o valor tokenizado |
| FotoTile hover `-3px .15s` | 120ms em `:active` | hover não existe no dedo |
| `GlitchType` com scramble | **removido** | o texto simplesmente surge, caractere a caractere |

### 6.5 Varredura de tela cheia

Marca **mudança de lugar, não de vista**. Login, troca de obra, primeira chegada
ao Hoje na sessão. **Não** em navegação de rotina.

```
@keyframes lv-varre {
  0%   translateX(-101%)
  22%  translateX(0)      /* 180ms cobrindo   */
  73%  translateX(0)      /* 420ms PARADO     */
  100% translateX(101%)   /* 220ms revelando  */
}
```

A pausa de 420ms existe para dar leitura ao wordmark, que entra e sai por
opacidade dentro dela. O conteúdo reexecuta a revelação a ~560ms, ainda coberto.

**Nunca esconder carregamento:** se o dado não chegou, a cortina revela
esqueleto, não vazio. Senão a varredura vira disfarce de lentidão.

### 6.6 Movimento reduzido

Um único ponto de controle:

```css
[data-mov="reduzido"] *, @media (prefers-reduced-motion:reduce) * {
  animation:none !important; transition:none !important }
.rev { opacity:1 !important; transform:none !important }
```

Valores finais aparecem imediatamente: contadores no número final, texto de IA
completo, carrossel estático.

### 6.7 Exceções documentadas à regra "só transform/opacity"

1. **`stroke-dashoffset`** — desenho do anel do donut. Repaint, não reflow, num
   elemento pequeno. O alternativo composto (girar semidisco com clip) não paga.
2. **`width`** — busca retrátil. Layout, mas num elemento pequeno do cabeçalho.
   Evitável adotando a paleta central.
3. **`backdrop-filter`** — elevação por blur no modo cliente. Repinta na rolagem;
   por isso restrito a esse papel.

Qualquer exceção nova exige registro aqui, com o motivo.

### 6.8 Superfície flutuante: entra e sai em tempos diferentes (v1.2)

Vale para menu (5.20), popup de perfil (8.5) e qualquer painel que apareça sobre o
conteúdo:

```
entra   --t-ui   220ms
sai     --t-sai  140ms
origem  transform-origin no GATILHO que a abriu
o quê   só transform (scale + translate) e opacity
```

**Aparecer e sumir não são o mesmo gesto invertido.** Aparecer é revelação: precisa de
tempo para o olho encontrar a superfície nova e entender de onde ela saiu. Sumir é
liberar o caminho — quem fechou já decidiu, e o que ele quer ver é o que estava atrás.
Saída com a mesma duração da entrada lê como travamento.

**A origem no gatilho é o que torna a saída legível:** a superfície volta para o botão
que a abriu, em vez de desaparecer no lugar. É o mesmo princípio da 6.1 — todo gesto tem
um sujeito, e aqui o sujeito é o gatilho.

---

## 7. Fundo de tela

Conceito reaproveitável em todas as telas: a densidade fica na **metade
superior** e dissolve para baixo, deixando limpa a faixa dos dados.

```css
position:fixed; left:0; right:0; top:0; height:56vh; z-index:0;
mask-image:linear-gradient(to bottom,
  rgba(0,0,0,1) 0%, rgba(0,0,0,.88) 30%, rgba(0,0,0,.40) 66%, rgba(0,0,0,0) 100%);
filter:blur(46px) saturate(.85);
transform:scale(1.18); transform-origin:50% 0%;
```

| Opacidade | Claro | Escuro |
|---|---|---|
| Capa/foto | .30 | .48 |
| Gradiente da obra | .24 | .42 |

Medido: pico entre 10% e 22% da altura, zero em 61%. **Elemento fixo e estático
— pintado uma vez, não custa rolagem.** Quando houver foto de capa real, ela
entra nesta mesma camada, com o mesmo blur, máscara e altura.

**Cuidado de implementação:** não colocar a camada de fundo com uma regra
`.app > *{position:relative}`, porque isso sobrescreve o `position:sticky` do
cabeçalho. Posicionar só os invólucros de conteúdo.

### 7.1 Azulejo — a textura escolhida pela organização (v1.5)

A padronagem do `01` §8.1b, aplicada como fundo. **Ela é a especificação que
faltava à textura `geometrico`** — que a 1.5 mantinha fora justamente por não
ter uma. Com ela escrita, `geometrico` entra; no banco o valor continua com esse
nome, e **"Azulejo" é como ele se chama na tela**, do mesmo jeito que `grotesk`
aparece como "Montserrat".

```
persistência   semente (inteiro) + tema (texto). NUNCA a imagem
pintura        background-image com data: URI
atrás de texto traço a 50% (OPACIDADE_ATRAS_DE_TEXTO)
célula         largura / 8, piso de 140px — escala com a tela
custo          ~1,4 ms por sorteio, ~6,5 KB; estático depois de pintado
```

**`background-image`, nunca SVG no DOM.** Como imagem de fundo a textura vira
uma pintura do compositor: zero nós, não participa do layout e não entra em
nenhuma varredura de acessibilidade. Injetada como markup, ela acrescenta
centenas de nós a uma tela que pode ter lista longa — e passa a custar em cada
recálculo de layout.

**Gerar uma vez por montagem**, amarrado a `[semente, tema]`. No corpo do render,
cada tecla digitada num campo qualquer redesenharia a textura inteira.

**O traço cai à metade atrás de texto.** Em área de leitura o desenho compete com
a letra; a 50% ele continua presente e para de disputar.

**Não é tematizável pelo acento** (1.5): os três pares fundo/traço são fechados e
medidos. Ver o porquê no `01` §8.1b.

---

## 8. Navegação

### 8.1 Arquitetura: um gatilho por borda

```
esquerda  pílula da obra (☰ + nome + badge)  →  gaveta de navegação (esquerda)
          + Novo                              →  modal de registro
          lupa                                →  busca
direita   cápsula: Lavrō | Minhas obras | avatar  →  popup de perfil
```

Idêntico no celular e no desktop. **Não existe hambúrguer separado nem barra de
pílulas de seção** — "Hoje" mora dentro da gaveta.

**Custo assumido:** Hoje e Evolução deixam de ser um clique. Mitigado por o app
abrir no Hoje e por "+ Novo" seguir exposto.

**Confirmada e reforçada:** a coluna de detalhes (5.23) **não é gaveta** e não disputa a
borda direita. A árvore de pastas à esquerda foi **rejeitada** por disputar a borda
esquerda com o gatilho da obra.

**Configuração de módulo não vira subitem na gaveta.** Destino único *Configurações da
obra*, com seções. Subitem por módulo transformaria a gaveta em árvore de dois níveis —
cada módulo novo acrescentaria um ramo.

### 8.2 Cabeçalho transparente

Sem fundo, sem scrim. **Só é possível porque tudo nele é pílula ou cápsula** —
texto solto não sobrevive passando por cima de um card. A alta ênfase (preta no
claro, branca no escuro) garante legibilidade sobre qualquer conteúdo.

### 8.3 Degradação responsiva — por prioridade, nunca por quebra de linha

Barra sticky que muda de altura ao rolar é pior que truncar.

| Largura | O que sai |
|---|---|
| ≤1180px | nome da obra limitado a 20ch |
| ≤1024px | wordmark e divisor da cápsula |
| ≤860px | rótulo "Minhas obras" vira ícone de grade |
| ≤640px | nome da obra a 11ch, gaps reduzidos |
| ≤420px | nome a 7ch, `--pad-tela` 12px |
| ≤365px | nome a 5ch |

Verificado de 360 a 1340px: sem transbordo, sem sobreposição, sempre uma linha.

**Linha de dados abaixo de 720px muda de forma, não de componente.** Dois andares, com
seleção e ação de 44px nas pontas. Nenhum dado sai, a ordenação é a mesma.

**Componente auxiliar pode deixar de existir em vez de encolher.** A coluna de detalhes
desaparece abaixo de 1180px e migra para modal. Encolher um painel abaixo do que ele
precisa para informar é pior do que removê-lo.

**Painel auxiliar não empurra o layout** (5.23): altura própria, rolagem interna, e altura
mínima na janela.

### 8.4 Estrutura da gaveta

```
Lavrō                                    ✕
SPK MARTINELLI
[ Hoje                              3 ]   ← pílula vazada, destino principal

CONTROLES DE ADMIN  (só renderiza para admin)
  Editar obra        dados, checklists, alertas e prazos
  Usuários e acessos quem entra e o que pode fazer

CONTROLE
  RDOs 147 · Marcos 40 · Materiais · Cargos e pessoas

EVOLUÇÃO · mesma página
  Linha do tempo · Gantt · Físico-financeiro

────── rodapé ancorado, 12,5px, discreto ──────
  Novidades do app · Sobre a Lavrō · Sobre a Baraka
```

**Separador de bloco é rótulo mono + filete, e só.** Barra vertical + horizontal
juntas eram ruído concorrente (erro corrigido).

**Dica de subitem é texto pequeno fixo em mono, não tooltip** — a gaveta é o
componente mais tocado no celular, e `hover` não existe no dedo.

**Nomes não podem colidir.** Casos resolvidos: `Marcos` só em Controle;
`Usuários e acessos` (admin) × `Cargos e pessoas` (controle).

### 8.4b A gaveta tem DOIS ESCOPOS, não um (decisão de 04.08.2026)

A 8.4 desenha a gaveta como gaveta **da obra**. Ela não pode ser só isso, e o
motivo é estrutural: `/admin/pessoas`, `/admin/checklists`, `/admin/organizacao`
e o dashboard são da **organização**, não de nenhuma obra — e a 8.1 proíbe
hambúrguer separado. Sem um segundo bloco, dessas telas não haveria como sair.

```
Lavrō                                    ✕
ED FICTÍCIO            ← escopo: nome da OBRA, ou da ORGANIZAÇÃO quando não há obra
[ Hoje ]                 destino principal do escopo

ADMINISTRAÇÃO          (só admin, SEMPRE — vale para todas as obras)
  Pessoas · Modelos de checklist · Configurações da empresa

NESTA OBRA             (só com obra aberta)
  RDOs · Marcos · Materiais · Funcionários · Cargos · Arquivos ·
  Galeria · Câmeras · Solicitações · Relatório do período
  e, só para admin: Checklists da obra · Alertas e prazos · Painel do cliente

────── rodapé ancorado ──────
  Plataforma (só admin de plataforma) · Novidades do app · Sobre a <empresa>
```

**A RÉGUA DOS DOIS BLOCOS** (revisão do Michel, 04.08.2026): **o que vale para todas
as obras é Administração; o que é daquela obra fica em Nesta obra, inclusive os
controles de admin dela.** Administração vem primeiro. Coberto por teste — regra sem
teste volta na próxima vez que alguém acrescentar um item.

**REVISÃO DA MESMA NOITE — os blocos passam a ser os do protótipo, e a gaveta encurta
de verdade** (04.08.2026, noite):

```
ED FICTÍCIO
[ Hoje ]

CONTROLES DE ADMIN            (só admin)
  Editar obra                 dados, checklists, alertas e prazos
  Usuários e acessos          quem entra e o que pode fazer
  Configurações da empresa    identidade, marca e navegação

CONTROLE
  RDOs · Marcos · Materiais · Funcionários · Cargos · Arquivos ·
  Solicitações · Câmeras (em breve) · Relatório do período

EVOLUÇÃO · mesma página
  Linha do tempo · Gantt (em breve) · Físico-financeiro (em breve)

────── rodapé ──────
  Plataforma · Novidades do app · Sobre a <empresa>
```

**O bloco "Administração" deixou de existir**, e não por gosto: com Pessoas virando
**Usuários e acessos**, os **modelos de checklist** entrando dentro de *Editar obra* e
as **configurações da empresa** subindo para Controles de admin, não sobrou item para
ele. Três dos cinco rótulos de bloco desapareceram e nenhum destino se perdeu.

**"Editar obra" é uma página com quatro seções** (`/obra/:id/editar`): dados da obra ·
checklists desta obra · alertas e prazos · **modelos de checklist**. As rotas antigas
continuam de pé — a página as **reusa** em modo `embutido` (elas só deixam de desenhar
o cabeçalho próprio), então um favorito guardado não morre numa mudança de menu.

**A mistura de escopo ali é deliberada e está MARCADA na tela:** as três primeiras
seções são da obra; modelos de checklist é da **organização** e vale para todas. Editar
um modelo aqui altera o que as outras obras oferecem, e o que contém isso é uma faixa
de aviso acima da seção — não uma nota miúda. Templates fazem **snapshot** no RDO
(regra inviolável do projeto), então nada disso reescreve histórico.

**O formulário de dados da obra virou componente** (`pages/obra/FormDadosObra.jsx`),
usado pela página nova **e** pelo dashboard da obra: duas cópias de um formulário de
obra é como as duas divergem, e divergência ali é dado de documento saindo errado. **A
zona de perigo** (apagar a obra, zerar RDOs) **não foi movida** — é código destrutivo,
com limpeza de Storage antes do delete, e mudar código que apaga pede onda própria.

**Selo "em breve", e ele distingue dois casos que parecem um:** *Gantt* e
*físico-financeiro* não têm rota (são a onda da timeline), então entram **inertes** —
sem `href`, porque um link para lugar nenhum cai no `Navigate to="/"` e o menu parece
quebrado. *Câmeras* é o oposto: a tela **existe e funciona**, e o selo ali é decisão de
produto (não expor ainda), então o item continua clicável.

**Na lista de obras a pílula é só o gatilho** — círculo com as três barras, sem o nome
da empresa: ali a resposta para "onde estou" é *em nenhuma obra*, e o nome da
organização confundia. Ele segue dentro da gaveta, onde é contexto. Alvo em 44px: a
discrição vem de não haver rótulo, nunca de alvo menor.

**Defeito de acessibilidade encontrado de raspão, e ainda aberto:** o `Field` de
`ui.jsx` renderiza `<label>` sem `for` e o input sem `id` — **nenhum campo do app tem
rótulo acessível associado**. Apareceu porque `getByLabel` não achava nada no teste.
Conserto mexe em todos os formulários: onda própria.

### 8.1b A RÉGUA DAS DUAS BORDAS (05.08.2026) — a regra que decide onde um item mora

> **A borda esquerda é a OBRA — onde estou e para onde vou.
> A borda direita é a EMPRESA e EU.**

A 8.1 já dizia "um gatilho por borda". Esta é a camada de cima: **de quem é o
assunto de cada lado.** Sem ela, cada item novo virava discussão.

| Esquerda (obra) | Direita (empresa e eu) |
|---|---|
| pílula do escopo → gaveta | wordmark **Lavrō** (a plataforma) |
| "‹ Minhas obras" (primeiro item da gaveta — sobe um nível) | **nome da empresa** → popup com *Usuários e acessos* e *Configurações da empresa* |
| atalho de **Arquivos** · lupa · **+ Novo** | **avatar** → popup de perfil |

**Nada aparece nos dois lados.** Duplicação foi o critério que tirou **Obras**
(a cápsula e a pílula já eram isso), **Arquivos** (ganhou pílula própria),
**Usuários e acessos** e **Configurações da empresa** (mudaram de borda). O
custo assumido: **sem obra aberta a gaveta fica mínima** — escopo, destino
principal e rodapé —, porque na lista de obras a administração se alcança
pela direita.

**Os dois popups são o mesmo gesto na mesma borda**, e por isso o da empresa
espelha o de perfil em vez de virar outra gaveta: duas gavetas ensinariam que
a borda direita também navega.

**Quem não administra lê o nome da empresa como TEXTO**, sem botão.
Identidade é contexto para todo mundo; configuração, não.

### 8.2b A PÍLULA DIZ ONDE VOCÊ ESTÁ, em dois níveis (05.08.2026)

`Ed Fictício · Marcos` — nome da obra em branco, página em cinza, ponto entre
as duas. Dentro de um RDO: `Ed Fictício · RDO 149`.

**O rótulo vem de um MAPA DE ROTA, nunca do `<h1>` da tela.** O cabeçalho
monta antes do conteúdo; ler o título renderizado faria a pílula piscar a cada
navegação. Rotas antigas entram no mapa mesmo tendo saído da gaveta — elas
seguem alcançáveis por URL, e chegar numa delas com a pílula muda seria pior
que não ter o recurso.

**Na raiz da obra não há segundo nível:** o lugar é a obra, e repetir "RDOs"
ali seria dizer duas vezes a mesma coisa. **Abaixo de 640px a página sai antes
do nome da obra** — entre *onde* e *o quê*, o onde vem primeiro (§8.3).

**Defeito que originou isto:** dentro de `/rdo/:id` o cabeçalho lia só
`/obra/:id`, então a pílula ficava nua e **a gaveta perdia os itens da obra** —
o sintoma visível era só o nome sumindo. O RDO conhece a obra dele, e a mesma
consulta devolve o número que vira o segundo nível.

### 8.4d A gaveta do OPERADOR — quatro itens (05.08.2026)

```
SPK MARTINELLI
[ Hoje ]

CONTROLE
  RDOs · Marcos · Materiais · Cargos e pessoas
```

Sem controles de admin, sem Evolução, sem Arquivos, Solicitações ou Câmeras. **Ele
registra o dia:** escolher entre onze destinos não ajuda quem está de bota no canteiro.
O que saiu da gaveta dele continua acessível pelo bloco "Controles de obra" da própria
página da obra — **a gaveta encurtou, o app não**.

**"Cargos e pessoas"** (`/obra/:id/equipe`) é a junção de Funcionários e Cargos, mesmo
método de *Editar obra*: reuso em modo `embutido`, rotas antigas de pé. A separação
nunca ajudou — cadastrar alguém exige um cargo, e criar cargo só serve para cadastrar
alguém.

**Relatório do período saiu da gaveta:** ele nasce do filtro de datas **dentro** da
lista de RDOs (`ObraPage.jsx:326`). Item de menu levaria a uma tela sem filtro — atalho
para o vazio.

**Selo "em breve" — a regra final, com os dois casos que ela cobre:**

| Caso | Forma | Exemplos |
|---|---|---|
| não tem rota | **inerte**: sem `href`, sem hover, sem foco | Gantt · Físico-financeiro |
| tem tela, mas não se quer expor | **inerte também** (decisão do Michel, 05.08) | Câmeras |

A distinção some da tela e permanece no código: se um dia a decisão de produto mudar,
**Câmeras volta a ser link sem que o Gantt possa**.

### 8.4e O "+ Novo" entrou (05.08.2026) — e como ele cria sem duplicar lógica

Pílula de ação no cabeçalho, **só dentro de uma obra**: as quatro coisas que o modal
cria pertencem a uma obra, e na lista de obras ele não teria onde escrever.

O modal é o da **5.10**, com o título vindo do **baralho da 9.1** — 20 frases
embaralhadas, uma por abertura, índice persistido no dispositivo. **Só "Nova RDO"
está viva;** Registro, Pergunta e Ata aparecem desligadas com "em breve", no mesmo
tratamento inerte da gaveta.

**O modal PEDE, a página da obra FAZ.** Criar RDO é `novoRdo()` no `ObraPage` — herda
equipamentos do último, monta o checklist ativo, deixa o número para o banco.
Reimplementar isso no cabeçalho seriam duas verdades sobre como nasce um RDO, e a
errada estaria no cabeçalho, em obra ativa. Então o cabeçalho navega para a obra com
`state.novaRdo` e quem sabe fazer, faz. **Três guardas**, cada uma evitando um RDO
indevido: ref contra a montagem dupla do StrictMode (que criaria dois), limpeza do
`state` antes de criar (senão voltar no histórico repete o pedido) e disparo só com a
obra carregada (`novoRdo` lê a coordenada para a previsão).

**Correção normativa da 9.4 — `{}` para dado, `[[ ]]` para a palavra marcada.** O texto
antigo usava `{}` para as duas coisas e argumentava que "é ordem, não conflito", porque
o `t()` só troca o que recebe. Isso vale em runtime, **mas não para o
`npm run verificar:locales`**, que compara os `{}` entre idiomas para achar tradução com
placeholder faltando: a palavra marcada é traduzida (`{lavrar}` × `{record}`), então ela
gerava **18 falsos positivos** e cegava a verificação real. Com delimitadores separados
morre também a armadilha que a própria 9.4 avisa — passar em `vars` um nome igual à
palavra marcada não pode mais apagar o underscore em silêncio.

**O que NÃO está na gaveta, e a ausência é decisão:**

| Fora | Onde vive | Por quê |
|---|---|---|
| **Obras** | cápsula ("Minhas obras") e, sem obra aberta, a própria pílula do topo | seria a terceira cópia do mesmo destino |
| **Requisições** (RCM) | dentro de Materiais, que já tem dois botões para ela | requisição é consequência do estoque, não vizinha dele. A dica de Materiais diz "estoque e requisições" — sem ela, quem procurava a RCM concluiria que a tela morreu |
| **Operadores · Almoxarifes** | "Controles de obra", na página da obra | pedido do Michel. **Atenção ao que elas são:** vínculo POR OBRA (`obra_operadores`, `obra_almoxarifes`), quem tem acesso àquela obra. A tela Pessoas é da ORGANIZAÇÃO e define **papel**, não obra — ela ainda **não** substitui essas duas. No dia em que absorver o vínculo por obra, aí sim elas deixam de existir |
| **Plataforma** | primeira linha do rodapé, no corpo discreto | uma conta só a enxerga; destaque grande seria peso de menu para uma pessoa |

**A pílula do cabeçalho segue o mesmo escopo:** nome da obra quando há obra,
nome da organização quando não há. Guardar "última obra visitada" foi
**rejeitado** — inventa estado, e a pílula passaria a mentir sobre onde você
está. Sem obra aberta, "nesta obra" simplesmente não existe; é a ausência que
informa.

**O bloco de admin vem ANTES do da obra**, e não misturado nele: são as telas
que mudam a configuração da obra, não as que a operam.

### 8.4c O que a onda A entregou, e o que nasceu dormente

Publicado em 04.08.2026, atrás da chave `organizacoes.nav_nova` (NV-01) — dois
cabeçalhos coexistem no código até a virada, e **todo link novo entra nos dois**.
Implementação em `src/nav.css` (classes `lvn-`) e `src/pages/nav/`.

| Peça | Estado |
|---|---|
| pílula do escopo → gaveta pela esquerda | **no ar** |
| gaveta de dois blocos (8.4b) | **no ar** |
| cápsula Lavrō \| Minhas obras \| avatar | **no ar** |
| lupa retrátil | **no ar** — embrulha o `BuscaGlobal` que já existia (166 linhas fazendo a busca de verdade); a lupa não reconstruiu busca nenhuma |
| popup de perfil (8.5) | **no ar**, com Aparência e Reportar erro **desabilitados** |
| **+ Novo** (modal 5.10) | **fora da onda A.** Criar RDO hoje é `novoRdo()` dentro do `ObraPage` — herda equipamentos do último RDO e numera pelo banco. Replicar isso num cabeçalho, em obra ativa com equipe em campo, seria a pior forma de estrear o botão |
| badge de pendências na pílula | **fora**: nenhum número é inventado. O desenho existe no CSS, esperando fonte de verdade |
| "Hoje" | aponta para `/obra/:id` até a tela Hoje existir |

**Dormente com o motivo escrito, e não escondido:** Aparência precisa de modo
escuro (o app não tem — os tokens `--esc-*` não são a mesma coisa) e de troca de
densidade; "Reportar erro" precisa das **duas rotas** da 8.5, e nenhuma existe.
Botão desabilitado com a razão à vista é melhor que controle que não faz nada — e
melhor que sumir e a norma passar a mentir.

**Divergência que ficou em aberto, e é decisão de desenho:** o `01` §10 diz que o
cabeçalho é o espaço da marca do **cliente**, e o cabeçalho antigo cumpre isso com
o lockup (símbolo + duas linhas). Aqui a cápsula da direita é da **Lavrō** e a
organização aparece como **nome**, dentro da pílula — onde divide lugar com o nome
da obra. Os dois não podem estar certos ao mesmo tempo. O lockup impresso, onde o
assunto é documento, não mudou.

**Divergências de base, todas por falta no app e nenhuma por escolha:**
tipografia (Space Grotesk e Inter estão na branch `onda-identidade`, pausada — até
lá herda-se Montserrat), modo escuro (não existe: as regras
`[data-modo="escuro"]` do protótipo não foram portadas) e elevação do cabeçalho
(só a estratégia SOMBRA; o BLUR não é padrão nem no protótipo).

**Um defeito que a medição pegou e a leitura não pegaria:** a gaveta é
flex-column com rolagem, e um filho flex encolhe pela altura quando o conteúdo
não cabe. O rótulo do escopo tem `overflow: hidden` (é o truncamento do nome), o
que zera seu `min-height` implícito — ele saiu **com altura zero**, presente no
DOM, com o texto certo, invisível na tela. Conserto: `flex: 0 0 auto` em todos os
filhos diretos. Está coberto por teste que mede altura, não texto.

### 8.5 Popup de perfil

Nome + cargo · **Aparência** (Claro/Escuro + Compacto/Confortável) ·
Configurações do perfil · Reportar erro · Sair.

**"Reportar erro" precisa de duas rotas:** erro do aplicativo vai para a **Lavrō**;
problema no registro da obra vai para o **contratante**. Num produto
multi-tenant, mandar tudo para o cliente entrega bug de software a quem não pode
resolver.

---

## 9. Frases do assessor

São o **título do modal de registro** (5.10), sorteadas a cada abertura.

### 9.1 Baralho, não sorteio

20 frases embaralhadas, consumidas uma por abertura, reembaralhadas só quando a
última sai — **20 aberturas sem repetição**, cerca de um mês de dias úteis.
Sorteio puro com 20 frases repetiria em ~6 aberturas (`√(πN/2)`).

O índice do baralho é persistido na preferência do usuário. Cada frase marca
**uma palavra** que recebe o underscore.

### 9.2 Frases contextuais

Sobrepõem o baralho. Prioridade: **contratante › primeira vez › lacuna › marco
vencendo › chuva › sexta › segunda.**

Estado real dispara **sempre**. Dia da semana dispara com **50%** de chance —
segunda e sexta cobrem 40% da semana, e contexto que dispara sempre deixa de ser
contexto.

### 9.3 Aviso do contratante (a implementar)

Requer campo **`apelido`** no contratante, no tenant e não na obra, com **teto de
14 caracteres** validado no cadastro. Fallback: primeira palavra da razão social;
se genérica ("Construtora"), as duas primeiras.

> {apelido} comentou no RDO 0147. Vale **responder** →

**Prioridade máxima**, acima de "primeira vez": as outras condições descrevem
estados; esta tem **uma pessoa esperando**.

**A frase termina em seta e leva ao card de pendências do Hoje.** E o canal
primário é o **badge do Hoje**, não a frase — frase é reforço. Requer estado de
leitura por usuário no comentário (única coisa desta lista que exige migração).

*Nota de implementação (v1.6):* o padrão "apelido com teto de 14 validado no
cadastro" já existe no banco — `organizacoes.apelido`, migration `og01`, com o
teto imposto pela RPC e coberto por teste de isolamento. Não é a mesma coluna
(aquele é o apelido do **tenant**, este é o do **contratante**), mas é o molde a
copiar, incluindo validar no banco e não só na tela.

### 9.4 O texto — apêndice temporário

> **Este apêndice é provisório.** Na onda de externalização de textos, ele migra
> para `src/locales/pt.json` sob a chave `assessor.frases` e
> `assessor.frases_contexto`, e este documento passa a guardar **só as regras**.
> Está aqui porque o conteúdo não pode viver apenas num arquivo de `_estudos/`.

**Convenção:** a palavra entre `{}` recebe o underscore da marca. **Uma por
frase, nunca duas.**

**As chaves de dado usam as mesmas chaves `{}`, e isso não é conflito — é ordem.**
O `t()` do app (`src/lib/i18n.js`) substitui **apenas os nomes que recebe** em
`vars`; o que sobra passa intacto para o marcador de underscore. Então
`{marco} {vence} em {dias} dias` resolve em duas etapas: `t()` troca `marco` e
`dias` pelo dado real, e `vence` — que ninguém passou — é a palavra marcada. A
contagem "uma por frase" vale **depois** do `t()`.

> **Armadilha:** passar em `vars` um nome igual à palavra marcada apaga o
> underscore **sem erro nenhum**. Nome de variável nunca deve ser verbo.

**Baralho — 20 frases:**

```
 1. O que vamos {lavrar}?
 2. O que merece {atenção} hoje?
 3. O que vale {registrar} hoje?
 4. Trabalho bem feito merece {foto}.
 5. Como anda o {trabalho} hoje?
 6. O que {aconteceu} na obra hoje?
 7. O que precisa ficar {documentado}?
 8. Alguma coisa para deixar {por escrito}?
 9. O que {avançou} hoje?
10. O que a obra tem para {contar}?
11. Serviço concluído? Vale uma {foto}.
12. O que não pode ser {esquecido} amanhã?
13. O que {mudou} desde ontem?
14. Que parte do trabalho merece ficar {guardada}?
15. Alguma pendência para {formalizar}?
16. O que vale {mostrar} ao cliente?
17. Como foi o {dia} na obra?
18. O que a equipe {entregou} hoje?
19. Hoje é fácil {lembrar}. Amanhã, não.
20. Vamos deixar isso {registrado}.
```

**Contextuais — 6 frases.** `sempre` = dispara toda vez que a condição vale;
`50%` = dispara com metade de chance, para o baralho continuar aparecendo.

| Condição | Disparo | Frase |
|---|---|---|
| `contratante` | sempre | *(a implementar — ver 9.3)* |
| `primeiro` | sempre | Primeiro registro desta obra. Vamos {começar}. |
| `lacuna` | sempre | Sem registro há {dias} dias. Vamos {pôr em dia}? |
| `marco` | sempre | {marco} {vence} em {dias} dias. Tem evidência para anexar? |
| `chuva` | sempre | Choveu hoje. Vale registrar a {parada}. |
| `sexta` | 50% | Sexta-feira. O que {fechamos} esta semana? |
| `segunda` | 50% | Segunda-feira. Como a obra {amanheceu}? |

**Frase contextual não pode conter dado fixo.** "M-12 vence em 3 dias" precisa
vir do marco real e do prazo real — frase contextual que erra o dado é pior que
frase aleatória. Por isso as duas frases acima trocaram `M-12` e `3` por `{marco}`
e `{dias}`: era exemplo renderizado escrito como se fosse a frase.

*Pendência que isso abre:* `{dias} dias` sai errado no singular ("há 1 dias").
Enquanto `lacuna` dispara só a partir de 2 dias o caso não aparece; se um dia
disparar com 1, precisa de chave própria — **não de plural automático**, que o
`t()` não tem.

**Frase de IA não leva ponto final** quando termina em pergunta ou quando o
cursor a segue: o underscore é o ponto.

---

## 10. Acessibilidade

- **Piso de toque 44px**, sem exceção — e desde a v1.3 isso é literal em todo o
  documento: a pílula de navegação, que era o único desvio, subiu para 44 (5.1).
- Contraste: marcas são isentas; **`--acento`, texto e componentes não são**. É a
  razão de `--acento` ser `#7C8BFF` no escuro. Fundo de selo sólido também não é
  isento — foi assim que o âmbar reprovado apareceu (1.4).
- `prefers-reduced-motion` num único ponto de controle (6.6).
- Qualquer coisa que pisque por mais de 5s precisa de mecanismo de parada.
- Procedência de IA legível **sem** movimento (barra vertical de acento).
- `:focus-visible` com contorno de 2px em `--acento`, offset 2px.
- Estado ativo nunca comunicado só por cor — o underscore é forma.

---

## 11. Regras invioláveis herdadas do projeto

- Alertas são **calculados, não persistidos**.
- Saldo de material é recalculado pelo banco (trigger). Nunca escrever direto.
- Paginação é só de exibição; o dataset completo fica em memória.
- Templates de checklist fazem **snapshot** no RDO.
- Toda tabela nova precisa de policy RLS SELECT explícita.
- Documento sensível (LGPD) só em bucket privado com signed URL.
- Nunca expor chave de API no bundle do Vite.
- Nunca usar dialog nativo do browser para confirmação.

---

## 12. Pendências

### 12.1 Deixaram de ser inexistentes na v1.1

Campo com rótulo e erro, tabela com ordenação, zona de upload, estado vazio,
confirmação destrutiva — todos nas seções 5.13 a 5.33.

**Correção de fato:** estado vazio e carregamento **existiam no código** (`ui.jsx` exporta
`Empty` e `Loading`). Estavam não especificados, não ausentes. **Botão** faltava na lista e
agora é 5.13.

### 12.2 Em aberto

| Item | Situação |
|---|---|
| **Vetor do símbolo** | Geometria definida no manual; desenho vetorial não feito. Bloqueia favicon. |
| **Modal de registro — as três opções inertes** | ~~"não existe no app"~~ — **corrigido em 22/08/2026:** o modal e a pílula `+ Novo` estão no ar desde 04–05/08 (`src/pages/nav/ModalNovo.jsx`), com o título vindo do baralho da 9.1. O que segue pendente é só **ativar as três opções desligadas** (Registro · Pergunta · Ata): elas correspondem a tipos que `registros` já grava, mas nenhuma tem tela de criação pelo lado da obra, e o selo "em breve" é decisão do Michel, não omissão. |
| **Configurações do Hoje** | Usuário escolhe quais cards aparecem. Exige persistência por usuário e por obra. |
| **Paleta de busca (Cmd+K)** | Alternativa recomendada à busca retrátil. |
| **Blur no modo cliente** | Aprovado para experimentação. |
| **Grafismo modular** | Referências Athos/Lurca levantadas; decidir se substitui ou convive com o gradiente. |
| **Acento âmbar de tenant** | Colisão com `--at`. Decidir antes do primeiro cliente amarelo. |
| **Coreografia entre telas** | Só a varredura está definida. Transição de seção e relação da gaveta com o conteúdo atrás ficam para depois do protótipo. |
| **Selo de plano em azul sólido** | Fica ao lado do nome da organização (Lab 05) e tensiona o "uma só ação azul por tela" da 5.7. Ou vira exceção escrita, ou rebaixa para contornado. **Decisão do Michel, com o protótipo aberto.** |
| **Alcance do tema "Papel + serifas"** | App inteiro ou só superfícies de leitura? O `01` §6.1 trava creme como superfície institucional. A serifa do pacote também não existe: Georgia é espécime provisório. |
| **Texturas `geometrico` e `grade`** | Aprovadas como opção na tela, **sem especificação escrita**. Ficam fora da 1.5 até terem derivação própria, como o gradiente tem no `01` §8. |
| **Papel no convite** | ~~O Lab 04 v6 pede "papel no aceite"; `convites` não tem essa coluna.~~ **Resolvido em 02/08/2026:** a migration `pe02` criou `convites.papel` (opcional) e `usar_convite` o aplica só sobre quem estava `pendente`. |
| **Largura de folha padrão** | Hoje são 1000px no app, 1180px no protótipo e 1560px nas telas de dados densos (2.4). O Michel testou Pessoas em 1000 e **aprovou a leitura** — a dúvida que fica é de padrão, não desta tela: ou 1000 continua sendo o padrão e algumas telas declaram largura própria, ou o padrão sobe para 1180 (mais próximo do uso atual de monitor) e 1560 segue como exceção de dados densos. **Decisão do Michel, fora da onda 9.** |

### 12.3 Ainda inexistente

- **Mover** item entre pastas e entre categorias. Entre categorias é *mudar quem vê* e exige confirmação própria.
- **Filtro por facetas** (tipo, autor, período).
- **Download em lote como arquivo único** — depende de compactação no servidor.
- **Protocolo de distribuição** e **QR da cópia impressa** — reservados no painel, onda 2.
- **Log de eventos** com interface de consulta.
- **Tela de Configurações da obra.**
- **Anotação sobre imagem** — comentário em cima de planta ou foto.
- **Visualizador de DWG.**
- **Abas** — não foram necessárias: a escolha exclusiva virou pílula (5.17) e a navegação de pasta virou linha (5.21).

---

## 13. Onda A — brief de migração

**Objetivo: introduzir os tokens semânticos deixando o app visualmente
IDÊNTICO ao que é hoje.** Nenhuma mudança de aparência nesta onda.

**Ordem:**

1. **Desarmar a mina.** `ui.jsx` e `clienteUi.jsx` exportam ambos uma variável
   `C` com o mesmo nome e valores opostos (claro × escuro). Separar antes de
   qualquer outra coisa.
2. **Criar a camada de tokens** com os nomes das seções 1, 2, 3 e 6, mantendo
   **os valores atuais** — amarelo `#F5C400` como `--acento`, Montserrat como
   display, cinzas atuais nas superfícies.
3. **Substituir literais por tokens.** Inclui os ~30 `rgba(245,196,0,…)`
   espalhados e o `C.yellowRGB`.
4. **Remover o `alert()` nativo** em `Rcm.jsx:272`.
5. **Remover `LogoMarkCurva`** (zero renders).
6. **Auto-hospedar as fontes** (woff2, subset latino).

**O que NÃO entra na Onda A:** trocar valores de token, aplicar a identidade
Lavrō, mexer em navegação, criar componente novo. Cada um é onda própria.

**Critério de aceite:** captura de tela antes e depois, por rota, sem diferença
perceptível. Se algo mudou de aparência, a onda falhou.

---

## 14. Vocabulário

| Jargão | Nome no manual |
|---|---|
| kebab | **botão de ações da linha** — três pontos verticais |
| hambúrguer | **gatilho da obra** — três barras, abre a gaveta |
| chip | **selo de tipo** (5.22) |
| dropzone | **zona de envio** (5.24) |
| breadcrumb | **migalha** (5.20) |
| skeleton | **esqueleto** (5.28) |
| inline edit / *click to edit* | **campo quieto** — campo que se parece com texto e só revela que é editável quando o ponteiro chega |
| filter pill / tag | **chip de filtro** — filtro aplicado e removível. Não confundir com o **selo de tipo**, que informa e não sai |
| detail pane / *property list* | **ficha** — a pauta de rótulo e valor do detalhe, altura de linha `--alt-ficha` (§3) |

---

## 15. Chaves de tradução

Famílias: `arquivos.*` · `cat.*` · `publico.*` · `col.*` · `acao.*` · `filtro.*` · `envio.*` · `pasta.*` · `excluir.*` · `liberar.*` · `ver.*` · `painel.*` · `vazio.*` · `espelho.*` · `tag.*` · `rede.*` · `rodape.*` · `nav.*`

Duas armadilhas que este módulo pisa:

- **Tamanho de arquivo passa por `Intl.NumberFormat`** (`12,4 MB` → `12.4 MB`). É grandeza.
- **Data NÃO passa.** É código: formatada como número perde o preenchimento com zero e deixa de ser conferível.

**Todo texto renderizado em JS precisa carregar a chave junto**, incluindo cabeçalhos de tabela montados dinamicamente. Um cabeçalho sem `data-t` não dá erro, não tem sintoma, e simplesmente nunca traduz.

O laboratório tem um alternador **Chaves t()** que troca o texto pela chave. O que continuar em português com ele ligado é texto solto.

**Convenção `data-dado` (v1.2) — o que NÃO traduz.** Nome de pessoa, e-mail, nome de obra
e nome de empresa são **dado**, não texto de interface: não têm chave e nunca deveriam
ter. Marcá-los com `data-dado` transforma o alternador em verificador de verdade — com
ele ligado, **o que continua em português sem ser `data-dado` é texto solto**, e a
varredura passa a ser visual em vez de conferência linha a linha.

Sem essa marca o alternador tem um ponto cego, e ele já cobrou: cinco opções de filtro
ficaram sem chave na v1 do Lab 04, indistinguíveis dos nomes próprios ao redor.

---

## 16. Histórico de versões

| Versão | Data | O que entrou |
|---|---|---|
| **1.11** | 06.08.2026 | **A navegação ganha a regra que faltava, e ela é de borda.** Nova **8.1b**: a esquerda é a OBRA (onde estou e para onde vou), a direita é a EMPRESA e EU. É a camada acima do "um gatilho por borda" da 8.1 — sem ela, cada item novo virava discussão. Dela saem, sem caso a caso: "Minhas obras" como primeiro item da gaveta, o nome da empresa na cápsula abrindo as configurações do admin, e a proibição de um item existir nas duas bordas (foi o critério que moveu Obras, Arquivos, Usuários e acessos e Configurações da empresa). Fica registrado o custo assumido: **sem obra aberta a gaveta é mínima**. Nova **8.2b**: a pílula em **dois níveis** — obra em branco, página em cinza —, com o rótulo vindo de um MAPA DE ROTA e nunca do `<h1>` da tela, porque o cabeçalho monta antes do conteúdo e ler o título renderizado faria a pílula piscar. Na raiz da obra não há segundo nível; abaixo de 640px a página sai antes do nome da obra. Ela nasceu de um defeito: dentro de `/rdo/:id` o cabeçalho lia só `/obra/:id`, a pílula ficava nua e **a gaveta perdia os itens da obra** — o nome sumindo era só o sintoma visível. |
| **1.10** | 05.08.2026 | **A gaveta do operador cabe em quatro itens, e o "+ Novo" entra de verdade.** Nova **8.4d**: o operador vê RDOs · Marcos · Materiais · **Cargos e pessoas** — nada mais. Ele registra o dia, e escolher entre onze destinos não ajuda quem está de bota no canteiro; o que saiu segue nos "Controles de obra" da página da obra. **Cargos e pessoas** () junta Funcionários e Cargos pelo mesmo método de *Editar obra*. **Relatório do período sai da gaveta** — ele nasce de um filtro dentro da lista de RDOs, e item de menu levaria a uma tela sem filtro. O selo **em breve** ganha regra final: sem rota **ou** decisão de não expor, o item fica **inerte** (Câmeras entra aqui por decisão de produto, e a distinção permanece escrita no código). Nova **8.4e**, o **+ Novo**: pílula de ação só dentro de uma obra, modal da 5.10 com título do baralho da 9.1, só *Nova RDO* viva. **O modal pede, a página da obra faz** —  em vez de reimplementar , com três guardas contra RDO indevido. E a **9.4 é corrigida**:  para dado,  para a palavra marcada, porque o mesmo delimitador para as duas coisas cegava o verificador de traduções com 18 falsos positivos. |
| **1.9** | 04.08.2026 (noite, 2ª revisão) | **A gaveta encurta pela raiz: telas se unem em vez de itens se esconderem.** Os blocos passam a ser os do protótipo (Controles de admin · Controle · Evolução) e **"Administração" deixa de existir** — Pessoas vira **Usuários e acessos**, os **modelos de checklist** entram dentro de *Editar obra* e as **configurações da empresa** sobem para Controles de admin. Nova página **`/obra/:id/editar`**, quatro seções, reusando as telas antigas em modo `embutido` — as rotas velhas continuam de pé, porque favorito não pode morrer numa mudança de menu. A **mistura de escopo** ali (modelos são da organização) é deliberada e vive marcada por faixa de aviso, não por nota miúda. O **formulário de dados da obra vira componente** compartilhado com o dashboard; a **zona de perigo NÃO foi movida**, porque mudar código que apaga pede onda própria. Novo selo **"em breve"**, com a distinção que importa: sem rota → item **inerte** (Gantt, físico-financeiro); tela que existe e não vai expor ainda → item **clicável com selo** (Câmeras). Na lista de obras a **pílula é só o gatilho**, sem o nome da empresa. E fica registrado um defeito aberto que o teste encontrou de raspão: o `Field` de `ui.jsx` **não associa label a input** — nenhum campo do app tem rótulo acessível. |
| **1.8** | 04.08.2026 (noite) | **A gaveta passa pela primeira revisão de uso, e ela vira régua.** A 8.4b troca "Controles de admin / Nesta obra / Na organização" por **dois blocos**: **Administração** é o que vale para TODAS as obras (Pessoas, modelos de checklist, configurações da empresa), **Nesta obra** é o que é daquela obra — inclusive os controles de admin dela. Saem quatro itens, e cada ausência tem destino escrito: **Obras** (a cápsula e a pílula do topo já são isso), **Requisições** (mora dentro de Materiais, que tem dois botões para ela — e a dica "estoque e requisições" existe para ninguém concluir que a tela morreu), **Operadores e Almoxarifes** (seguem nos "Controles de obra" da página da obra) e **Plataforma**, que desce para a primeira linha do rodapé porque uma conta só a enxerga. Fica registrado o que o pedido supunha e o código não confirma: Pessoas é da ORGANIZAÇÃO e define **papel**; Operadores/Almoxarifes são vínculo **por obra** — ela ainda não substitui as duas, e enquanto não substituir elas não podem simplesmente deixar de existir. |
| **1.7** | 04.08.2026 | **A navegação sai do papel, e a §8 ganha o que faltava para caber no app.** Nova **8.4b**: a gaveta tem **dois escopos**, não um — "nesta obra" só com obra aberta, "na organização" sempre. Não é exceção de código: o §8.1 proíbe hambúrguer separado e metade das telas de admin é da ORGANIZAÇÃO, então sem o segundo bloco não haveria como sair delas. A pílula segue o mesmo escopo, e guardar "última obra visitada" fica **rejeitado** — inventa estado e a pílula passaria a mentir sobre onde você está. Nova **8.4c**, o retrato da onda A: o que está no ar, o que nasceu **dormente com o motivo à vista** (Aparência precisa de modo escuro, "Reportar erro" precisa das duas rotas da 8.5), e o que ficou de fora — o **`+ Novo`**, porque criar RDO hoje mora dentro do `ObraPage` e replicar aquilo num cabeçalho, em obra ativa, seria a pior forma de estrear o botão. Fica registrada a **divergência entre o `01` §10 e esta seção**: o cabeçalho antigo dá o lugar ao lockup do cliente, o novo dá a cápsula à Lavrō e a organização vira nome na pílula — os dois não podem estar certos, e decidir é desenho, não implementação. E fica o defeito que só a medição pega: em flex-column com rolagem, filho com `overflow: hidden` encolhe **abaixo do min-content** — o rótulo do escopo saiu com altura zero, no DOM, com o texto certo e invisível. |
| **1.6** | 02.08.2026 (mesclagem) | **Reúne a linha de design com a linha de implementação.** Do lado do **design**: a **5.10** deixa de ser "modal de superfície de marca" e passa a ser **modal de registro**, com o motivo de ser modal e não submenu (é o ato central do sistema, não item de navegação), as **quatro opções** com descrição, a ordem fixa, o raciocínio do "+ Novo" contra "+ Nova RDO", e a regra de que **o título É a frase rotativa da 9**; nova **9.4**, o texto do assessor — 20 frases do baralho e 6 contextuais — trazido para cá porque conteúdo não pode viver só num arquivo de `_estudos/`. Do lado da **implementação**: a delimitação da v1.3 sobrevive dentro da 5.10 (o modal de escolha é azul, a folha que ele abre é `--sup-1`), e a 5.10 ganha o retrato do que existe hoje — o modal **não existe no app**, e das quatro opções três correspondem a tipos que `registros` já grava, com **o nome da interface prevalecendo sobre o nome da coluna** (`pedido` é a coluna, "Pergunta" é o que se lê). **Duas correções de texto:** as frases contextuais tinham `M-12` e `3 dias` cravados — exemplo renderizado escrito como se fosse a frase, contra a regra que o próprio apêndice enuncia; viraram `{marco}` e `{dias}`. E fica documentado por que a mesma chave `{}` serve para dado e para underscore: **é ordem, não conflito** — `t()` troca só o que recebe, o resto vira palavra marcada, e a contagem "uma por frase" vale depois disso. |
| **1.0** | 26.07.2026 | Consolidação inicial: Lab 01, Lab 02 (v1→v9) e o protótipo Hoje (v1→v9). Tokens, espaço e elevação, densidade, tipografia, componentes 5.1–5.12, movimento, fundo de tela, navegação, frases do assessor, acessibilidade, pendências e o brief da Onda A. |
| **1.5** | 02.08.2026 (noite) | **O Azulejo destrava a textura `geometrico`.** Nova **7.1**: a padronagem do `01` §8.1b aplicada como fundo — persistência de **semente + tema, nunca a imagem**; **`background-image` com data: URI, jamais SVG no DOM** (como markup são centenas de nós numa tela que pode ter lista longa, e passam a custar em cada recálculo de layout); geração uma vez por montagem, amarrada a `[semente, tema]`; e o traço a **50% atrás de texto**, onde o desenho competiria com a letra. A **1.5** perde o "fora até terem especificação": `geometrico` ganhou a dela e `grade` é o caso trivial. Fica registrado que o tema do azulejo **não é tematizável pelo acento** — a organização escolhe entre três pares medidos, e não uma cor livre, porque traço sobre fundo de marca arbitrária não tem contraste garantido. |
| **1.4** | 02.08.2026 (tarde) | **Onda 9 (b) destravada — as decisões que faltavam viraram texto.** Nova **5.36 · lâmina de configuração**: camadas, blur estático (a restrição da 2.3 é sobre elemento que rola), piso/teto de luminosidade com as medições, e a regra derivada **"sobre a lâmina, nada abaixo de `--texto-2`"** — porque `--texto-3` cai para 1,6:1 ali. **5.7 ganha exceção escrita:** o selo de plano é azul sólido e convive com o primário na mesma tela — decisão do Michel, contra a recomendação, e registrada como exceção em vez de corrigida em silêncio; o que a contém é o selo ser inerte e a lâmina não ter fluxo de trabalho. **§4:** a serifa do pacote passa a ser a **Fraunces**, auto-hospedada e variável, com os dois conjuntos de eixos (display e texto) e as três armadilhas verificadas na tabela `fvar` — o padrão de `wght` do arquivo é **900**, então omitir o peso dá Black. Ela fica **fora do precache**: 490 KB de serifa opcional não podem cair no operador em obra. |
| **1.3** | 02.08.2026 | **Lab 04 v6 e Lab 05 v3.** `--papel-*` **reorganizada em três famílias** — a matiz diz a família, o tom diz o papel; bandas em **CIE LCHab** (Administração 300–318°, Campo 218–262°, Contratante 336–356°), com posição reservada para níveis futuros. Os valores da v1.2 eram da v3 do protótipo e estavam **errados**: almoxarife e cliente haviam trocado de família. **§1.5 ampliada** (decisão do Michel): entram `--painel`, textura e fonte de display; "tema" é preset sem coluna; geométrico e grade ficam fora até terem especificação. **§3 corrigida** — a ampliação de densidade da v1.2 **foi desfeita**, e no lugar entra o **porte de superfície** (§3.1, `.lv-porte-amplo`): densidade é do usuário, porte é da tela. **§2.1** ganha duas sombras no claro (só no claro). **§2.3** libera blur no véu de modal. **§5.1** sobe para 44px e a divergência com a §10 morre. **§5.10** delimita a superfície de marca ao modal de escolha. Componentes novos: **5.34** referência de papéis e **5.35** folha de convite. |
| **1.2** | 01.08.2026 | Lab 04 · Pessoas (v1→v3), pela `_historico/PASSAGEM_Lab04-Pessoas.md`. **Correção de fato na 1.4:** `--at-c` reprova AA com branco (4,24:1) — nasce `--at-solido` `#A96500`. Família **`--papel-*`** na 1.6 — 12 pares tinta/fundo, todos medidos e AA nos dois modos. **§3: delta de densidade ampliado** (`--alt-li` 58/44, `--pad-card` 26/14, `--gap-card` 18/9, `--gap-grade` 20/11) e token novo `--alt-ficha`; padrão `.alvo44`. Emendas em **5.3** (papel é sempre sólido), **5.15** (a busca acompanha o lado da coluna que filtra) e **5.20** (modo de escolha múltipla). **6.2 / 6.8:** token `--t-sai` e a regra de saída de superfície flutuante. Convenção **`data-dado`** na 15. Vocabulário (14): campo quieto, chip de filtro, ficha. Divergência 40px × 44px **registrada, não resolvida** (5.1, 10, 12.2). |
| **1.1** | 28.07.2026 | Adendo v1.2 (Lab 03 · Arquivos da obra, v1→v10): componentes **5.13 a 5.33** — formulário, dados, navegação de arquivos e controle de revisão. Famílias `--bar-*`, `--tipo-*` e `--est-lib` na **1.6**. Renome dos tokens de status para `--at` / `--er` e documentação do par `-c` / `-e` na **1.4**. Nova **2.4** (largura de folha). Emendas em 1.2, 4.1, 5.3, 5.7, 8.1, 8.3 e 12. Vocabulário (**14**) e chaves de tradução (**15**). Convenção de local canônico movida para `docs\`. |
