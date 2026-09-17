# módulo `planta-interativa` — a prancha que o cliente percorre

**Ainda não é gabarito do esqueleto.** É o módulo, soldável, com a mecânica
resolvida e medida. Virar tipo de slide do `DECK` é o passo seguinte — a
pendência está no fim deste arquivo.

Módulo que roda sozinho: `../../modulos/planta-interativa.html`.
Abre de `file://`, sem servidor e sem rede.

**Para que serve:** planta grande, com muitos ambientes, que não cabe legível
numa prancha impressa no projetor. Em vez de fatiar o desenho em seis slides, o
cliente percorre **um** desenho: você liga as camadas na ordem em que quer
contar a história, aproxima onde interessa, caminha, abre render e vídeo nos
pontos, e risca por cima enquanto fala.

---

## A decisão que sustenta tudo: vetor, não imagem

O desenho entra como **SVG vetorial**, convertido do PDF do Rayon. Nunca
rasterizado.

| caminho | por que não |
|---|---|
| JPEG de alta resolução | para ler rótulo de ambiente no zoom precisa de ~8.000 px: 4–6 MB, **+33% ao virar base64**. Estoura sozinho o teto de ~8 MB do deck. Safari/iPadOS ainda tem limite de descompressão de imagem — acima dele a imagem não aparece, sem erro: quadro branco no meio da apresentação |
| PDF embutido com pdf.js | vetorial, mas exige a lib (~1 MB), rerenderiza em canvas a cada nível de zoom, o pan fica com atraso perceptível e quebra o arquivo único offline |
| **SVG inline** | zoom infinito sem borrar, sem passar por base64, e — o que decide — **pinos e anotações ficam ancorados em coordenada de desenho, não em pixel** |

### O conversor importa mais que o arquivo

Mesmo PDF de entrada (A1, 554 KB, vetorial puro, sem imagem de fundo):

| conversor | saída | tempo | traços | clipPaths |
|---|---|---|---|---|
| `pdftocairo -svg` | 27,5 MB — e estourou a memória | 100 s | 61.788 | 61.597 |
| **`mutool convert`** | **2,28 MB** (526 KB comprimido) | **0,09 s** | 4.521 | 130 |

Mesma fidelidade visual. O cairo emite **um clipPath por elemento** — é isso que
explode o arquivo, não a complexidade do desenho. Parar no primeiro resultado
levaria a pedir ao Michel para simplificar um projeto que não precisava.

```
apt-get install -y mupdf-tools
mutool convert -o planta.svg planta.pdf      # sai planta1.svg, uma por página
```

**Recorte das margens.** A folha A1 costuma ter muito branco em volta do
desenho, e em tela cheia isso faz a planta nascer pequena. Medir a caixa de
tinta real e ajustar só o `viewBox` — as coordenadas não mudam, então os pinos
continuam válidos:

```
pdftocairo -png -r 100 -singlefile planta.pdf ref
convert ref.png -bordercolor white -border 1 -fuzz 2% -trim -format "%wx%h%O\n" info:
# dividir por 1.38933 (100 dpi / 72 pt) e escrever no viewBox
```

### O que o Rayon entrega bem

Exportação medida em 16/09/2026: A1, 1 página, 4 fontes embutidas, **zero raster
de fundo**. As hachuras e texturas saem como **41 padrões de preenchimento**
(`pattern`) com 6 tiles minúsculos — não como milhares de linhas soltas. É por
isso que o arquivo é leve mesmo com textura em todo ambiente.

Pedir ao Michel: **PDF vetorial, 1:1, só as camadas que vão aparecer, sem imagem
de fundo rasterizada.** Os renders e fotos vêm separados, fora do PDF.

**Limitação:** o texto vira glifo reutilizável (`<use>`), não texto selecionável.
Irrelevante para apresentar; relevante se um dia quiser busca por ambiente.

---

## Camadas — a narrativa, e não só o desenho

É o que transforma a planta em apresentação: começar com a casa nua, **ligar o
percurso de visitação**, depois **ligar os pontos de mídia**, e só então contar o
que a pessoa vê primeiro e por quê. Cada camada entra com esvanecimento de
0,32 s; ligar e desligar é reversível a qualquer momento.

### Como uma camada existe

```html
<svg id="planta" viewBox="...">
  ...o desenho base...
  <g data-cam="percurso" id="cam-percurso"> ...a polilinha do percurso... </g>
</svg>
```

O grupo mora **dentro** do SVG da planta: anda e escala junto com o desenho,
porque **é desenho**. Aqui a espessura do traço é em unidade de desenho e deve
crescer no zoom — uma linha de percurso de 60 cm continua com 60 cm.

> **É o oposto da anotação ao vivo**, que é recalculada em pixel de tela para
> *não* engordar. Duas camadas, duas naturezas: a camada de projeto pertence ao
> desenho; o rabisco pertence à tela.

A camada `pins` é a exceção: são os pontos de mídia, que já vivem em HTML.

### Declaração

```js
window.__LAYERS__=[
  {id:"base",     nome:"Planta",                fixa:true, on:true},
  {id:"percurso", nome:"Percurso de visitação",            on:false},
  {id:"pins",     nome:"Pontos de mídia",                  on:false}
];
```

`fixa:true` sai do alcance dos botões — a planta não se desliga. A ordem do
array é a ordem do painel e das teclas **1…9**.

### Roteiro — a sequência da fala

```js
window.__ROTEIRO__=[
  {t:"A casa",                  on:[]},
  {t:"O percurso de visitação", on:["percurso"]},
  {t:"O que se vê no caminho",  on:["percurso","pins"]},
  {t:"Parada 2 — o estar",      on:["percurso","pins"], ir:{x:700,y:1500,z:3.2}}
];
```

Cada passo declara **o estado inteiro** das camadas, não um delta: voltar um
passo desfaz sozinho, sem acumular. `ir` é opcional e leva a vista até um ponto
do desenho — `x` e `y` em coordenada de desenho, `z` em múltiplos do
enquadramento da prancha. `ir:{}` sem coordenada volta a ajustar.

**Espaço** e **PageDown** avançam; **shift+espaço** e **PageUp** voltam. É de
propósito: controle remoto de apresentação manda PageDown e PageUp, então o
roteiro anda no clicker, sem voltar ao teclado. As setas continuam servindo para
caminhar pela planta.

### ⚑ O que pedir ao Rayon — uma exportação por camada

**Esta é a parte que decide, e é trabalho de quem desenha, não de quem monta.**

Exportar **um PDF por camada, com o mesmo enquadramento e a mesma escala**: a
planta sem o percurso, o percurso sozinho, e assim por diante. O registro entre
elas sai perfeito de graça, porque as coordenadas são idênticas — nada de
realinhar à mão.

O que **não** pode mudar entre uma exportação e outra: o enquadramento, a
escala, o tamanho da folha. Recortar diferente desalinha tudo, e desalinhamento
de meio metro numa planta de museu aparece no projetor.

**O Rayon passa nesse teste.** Medido em 17/09/2026: as duas exportações saíram
com caixa de página idêntica, `2383,94 × 1683,78 pt`, e o registro ficou exato
sem nenhum ajuste. Confere assim antes de montar:

```
pdfinfo base.pdf | grep "Page size"
pdfinfo camada.pdf | grep "Page size"     # tem de ser igual, dígito a dígito
```

Caixa igual dispensa retângulo de registro. Caixa diferente quer dizer que o
exportador recortou pelo conteúdo — aí sim é preciso um elemento comum em todas
as exportações para alinhar, e removê-lo depois.

Conversão igual à da planta base — `mutool convert` —, e o conteúdo do `<svg>`
convertido entra como `<g data-cam="...">` dentro do SVG da base.

### ⚑ Os ids colidem entre duas exportações — soldar sem prefixo troca os glifos

Confirmado em 17/09/2026 com a planta e o percurso da Fazenda Lageado.

O `mutool` numera os ids do zero em **cada** arquivo: `font_0_7`, `clip_1`… Duas
exportações da mesma folha saem com o **mesmo esquema**, e na base de Lageado
**49 dos 114 ids do percurso colidiam com os da planta**. Soldar sem tratar isso
não dá erro: o navegador fica com a última definição e os glifos de uma camada
aparecem no lugar dos da outra.

Antes de injetar, prefixar os ids da camada e as referências a eles —
`id="x"`, `href="#x"` e `url(#x)`:

```python
for i in sorted(ids, key=len, reverse=True):
    txt = txt.replace('id="%s"'%i,      'id="rt_%s"'%i)
    txt = txt.replace('href="#%s"'%i,   'href="#rt_%s"'%i)
    txt = txt.replace('url(#%s)'%i,     'url(#rt_%s)'%i)
```

Ordenar por tamanho decrescente importa: sem isso `clip_1` come o começo de
`clip_12`.

### A moldura da folha vem repetida, e tudo bem

Cada exportação traz o norte, as marcas de elevação e o carimbo. Como são
idênticos e caem na mesma coordenada, **se sobrepõem exatamente e leem como um
só** — não há o que suprimir. O custo é peso: no caso de Lageado, o percurso
sozinho pesou 822 KB, dos quais 278 KB são as fontes repetidas da base. Vale
limpar só se o teto de 8 MB apertar.

**Quando só existe um PDF com tudo junto:** dá para isolar a camada no SVG
convertido filtrando por cor ou por grupo, **se** ela tiver cor própria no
desenho. É frágil e depende do arquivo — tentar só quando reexportar não for
possível, e conferir olhando.

---

## A mecânica

### Zoom e pan

`transform` CSS no palco — `translate()` + `scale()`, origem `0 0`. Sem
biblioteca. Medido: **60–70 ms por quadro repintado a 4× e 8×** de escala, com
zoom até 720% sem borrar.

- **clique** percorre três paradas: prancha → ambiente (3,4×) → detalhe (7,2×)
- **arrastar** caminha · **scroll e pinça** dão zoom contínuo · **slider** lateral
- **esc** ou **0** volta à prancha

### ⚑ Clique contra arrasto — a armadilha real

Um clique é um arrasto de 2 px. Sem limiar, **todo pan vira zoom** e o módulo
fica inutilizável. O limiar em uso: **6 px de deslocamento, 450 ms**. Abaixo
disso é clique; acima é arrasto, e o clique não dispara no `pointerup`.

### Pinos de mídia

Posição em **coordenada de desenho**, tamanho **fixo em pixel de tela**: a
posição é recalculada a cada quadro por `(x - VBX) * escala + tx`. Se o pino
escalasse junto com o desenho, a 700% ele viraria uma bola cobrindo dois
ambientes.

Abrem imagem, carrossel ou vídeo. **São uma camada** — na prancha cheia as bolinhas se
sobrepõem e competem com o desenho, então entram quando a fala chega neles.

**Como se posiciona um pino, sem adivinhação:** a ferramenta *marcar ponto*
captura a coordenada do clique e copia para a área de transferência, já no
formato do array `PINS`. O Michel marca, cola, e os pinos nascem certos.

### Anotação ao vivo

Traço livre, linha reta, seta, ponto e borracha; três canetas (vermelho,
grafite, marca-texto); desfazer e limpar.

**A arquitetura que barateia tudo:** os pontos ficam em coordenada de desenho e
o traço é **recalculado em pixel de tela a cada quadro**. É o que faz o rabisco
andar colado na planta sem engordar no zoom — espessura, raio do ponto e ponta
da seta ficam constantes.

> Desenhar dentro do próprio SVG com `vector-effect="non-scaling-stroke"`
> resolveria a espessura, **mas não a ponta da seta nem o raio do ponto**: eles
> inchariam junto com o desenho. Por isso a camada de tinta é um `<svg>` por
> cima do palco, não dentro dele.

- borracha por **distância em pixel do clique ao segmento** (limiar 18 px), sem
  elemento de hit-test no DOM
- `shift` trava o ângulo da reta e da seta em múltiplos de 45°
- dois dedos durante um traço **cancelam o traço** e viram navegação
- toque sem arrasto não vira traço
- atalhos `V D L A P E`, `ctrl+z` desfaz, `esc` volta a navegar
- **não persiste**: recarregou, perdeu. É anotação de apresentação, não de
  projeto. Para sobreviver, serializar `strokes` — já é um array de pontos em
  coordenada de desenho, pronto para virar JSON

### A transição da mídia — a regra de custo

Véu com desfoque do fundo (`backdrop-filter`) e fade. Medido em rasterização por
software, pior caso:

| estado | quadros/s |
|---|---|
| véu parado, com desfoque | **61–62** |
| repintando a cada quadro, blur 18px | 19 |
| repintando a cada quadro, blur 6px | 22 |
| repintando a cada quadro, sem blur | 55 |

**O custo do desfoque não depende do raio** — depende de reler o fundo. Daí as
três regras:

1. o raio do blur **nunca anima**; anima só a opacidade do véu, composta na GPU
2. **nada anima atrás do véu**: o halo dos pinos congela e o chrome some. O
   fundo vira quadro parado e o custo cai a zero
3. `prefers-reduced-motion` desliga tudo

**Plano B de uma linha** se algum aparelho engasgar: trocar `backdrop-filter`
por véu escuro sólido — vira opacidade pura. O `@supports` já faz isso onde o
recurso não existe.

A mídia é **emoldurada**, não ocupa a tela toda: se ocupar, o desfoque existe e
ninguém vê.

---

## Vídeo

| | tamanho |
|---|---|
| original de sala (20 s, 1442×1080, 9,9 Mbps) | 24,9 MB |
| H.264 1280, sem áudio, CRF 31 | **1,83 MB** → 2,4 MB em base64 |
| VP9/WebM CRF 36, testado como alternativa | 2,84 MB — **pior**, descartado |

```
ffmpeg -i in.mp4 -an -vf scale=1280:-2 -c:v libx264 -crf 31 \
       -preset slow -movflags +faststart out.mp4
```

Um clipe de 20 s consome **~30% do teto de 8 MB** do deck.

> **A regra:** no máximo um vídeo curto por deck embutido. A partir do segundo,
> ou o vídeo sai do arquivo único, ou aquele deck deixa de ser um arquivo e vira
> pasta.

Reprodução automática: `autoplay muted loop playsinline`, mais um `play()` no
evento `canplay` para o caso de a primeira chamada chegar antes do arquivo.
**`muted` é obrigatório** — nenhum navegador toca sozinho com som. Ao fechar,
pausa e zera. Se o navegador recusar, sobra o pôster com controles.

---

## Armadilhas já pagas

- **Acentuação.** Peça gravada em UTF-8 sem `<meta charset>` abre do disco
  mostrando `RecepÃ§Ã£o`. Este módulo declara o charset; a versão que sai do
  acervo e viaja por e-mail deve, além disso, gravar os acentos como entidades.
- **O Chromium de desenvolvimento não tem H.264.** Validar vídeo em sandbox
  exige uma cópia em WebM; o MP4 toca normalmente em Chrome, Safari e Edge.
- **`max-height:100%` dentro de linha `1fr` de grid estoura o contêiner** — a
  mídia cresce e empurra a legenda para fora da tela. Resolvido com
  `position:absolute; inset:0; margin:auto`.
- **`navigator.clipboard.writeText` rejeita uma Promise, não lança.** `try/catch`
  sozinho não segura; precisa de `.catch()`, senão vira erro de página.

---

## Pesos, para dimensionar a peça

Medido na planta real de 16/09/2026 (A1, 26 ambientes de programa museológico):

| parte | peso |
|---|---|
| SVG vetorial da planta | 2,2 MB |
| um vídeo de 20 s recomprimido | 2,4 MB em base64 |
| um render 1800 px, JPEG q82 | 0,33 MB |
| **peça inteira** | **~5,0 MB** |

Sobra pouco do teto de 8 MB. Planta com vídeo é peça cheia: o resto do deck
precisa ser magro, ou a planta vira peça separada.

---

## Solda num deck

Hoje o módulo é **página de tela cheia com chrome próprio**: barra de
ferramentas à esquerda, controle de zoom à direita, rodapé de ajuda. Copiar para
dentro de um slide pede três coisas:

1. **o slide assume a tela inteira** e devolve a navegação ao sair — o scroll do
   zoom disputa com a navegação de slide da engine, e tem de ser capturado
   enquanto a planta estiver aproximada
2. **o chrome vira o do deck** — cor, tipografia e cantos do `MARCA-<frente>.md`;
   o módulo usa neutros próprios de propósito, para não fingir marca
3. **a planta e a mídia entram como campos do `DECK`**, não como HTML colado: o
   SVG inline, o array `PINS` em coordenada de desenho e a lista de mídia

**Resolvido em 17/09/2026, e por um caminho mais barato que os três: o
quadro.** O gabarito `viva` (ver `viva.md`) roda a peça DENTRO do slide, num
quadro de sangria total, com `src` relativo. Os três pontos acima caem:

1. o slide assume a tela inteira e **o teclado fica da peça enquanto o slide é
   dela** — evento dentro do quadro não chega ao motor. O `trava`, que já
   existia, tira o toque e o arrasto; as setas do deck seguem;
2. **o chrome do deck é que aparece** — logotipo nos dois cantos de cima,
   bolinhas de seção, setas no pé. A peça esconde o dela no modo `embutida`,
   abaixo;
3. a planta e a mídia **não precisaram virar campos do `DECK`**: a peça
   continua um arquivo só, que abre sozinho. É o que evita as colisões de id
   registradas aqui — colar duas exportações no mesmo documento é o problema
   que este módulo já pagou uma vez.

### o modo `embutida`

Liga sozinho quando a peça está num quadro (`self!==top`), ou por `?embutida`
para conferir abrindo sozinha. Nele:

- **saem** `#topleft`, `#topright` e `#hint` — o deck cobre os mesmos cantos, e
  o indicador "Pontos ligados" é redundante com o menu de camadas;
- **o roteiro desce e camadas/marcas sobem**, por `--deck-topo` e `--deck-pe`,
  que chegam MEDIDOS do deck. Estimar a proporção por fora não fechou: ver a
  armadilha em `viva.md`;
- o rótulo do zoom (`Prancha / Ambiente / Detalhe`) **vira o botão de voltar à
  prancha** — a função do "Ajustar", que saiu junto com o canto;
- **o roteiro devolve o clicker ao deck na ponta.** Ele é um conjunto de passos
  dentro do slide, como os `.passo` do motor: andou até o fim, o próximo avanço
  sai do slide, senão o clicker morre na mão de quem apresenta.

⚑ Quem regenerar esta peça tem de repor o modo `embutida` — são quatro pontos,
todos marcados no arquivo com o comentário `EMBUTIDA`.

O caminho anterior, de **linkar ao lado** (`abre`, no `cheia` — ver
`render-cheia.md`), continua no motor e continua válido para peça vizinha que
não caiba dentro do slide. Só não é mais o que este deck usa.

---

## Pendências

- ~~virar tipo de slide do esqueleto~~ — **feito de outro jeito em 17/09/2026**:
  o gabarito `viva` roda a peça num quadro, sem colá-la no esqueleto. Colar o
  SVG e os pins como campos do `DECK` continua possível, mas deixou de ser
  necessário
- o percurso **deste módulo** continua sintético, porque a planta real é de
  cliente e não entra no repositório público. O registro entre duas exportações
  já foi provado com arquivo real — ver "o Rayon passa nesse teste"
- decidir a persistência da anotação, se um dia precisar sobreviver ao refresh
- conferência no iPad: pinça, borracha por toque e o custo do véu em aparelho
  real ainda não foram medidos fora do desktop
