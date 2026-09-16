# módulo `planta-interativa` — a prancha que o cliente percorre

**Ainda não é gabarito do esqueleto.** É o módulo, soldável, com a mecânica
resolvida e medida. Virar tipo de slide do `DECK` é o passo seguinte — a
pendência está no fim deste arquivo.

Módulo que roda sozinho: `../../modulos/planta-interativa.html`.
Abre de `file://`, sem servidor e sem rede.

**Para que serve:** planta grande, com muitos ambientes, que não cabe legível
numa prancha impressa no projetor. Em vez de fatiar o desenho em seis slides, o
cliente percorre **um** desenho: aproxima onde interessa, caminha, abre render e
vídeo nos pontos, e você risca por cima enquanto fala.

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

Abrem imagem, carrossel ou vídeo. **Ligam e desligam por botão** — na prancha
cheia as bolinhas se sobrepõem e competem com o desenho.

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

Enquanto isso não existe, a peça pode ser **linkada ao lado do deck** — abre em
aba própria e volta pelo `ms-voltar.js`.

---

## Pendências

- virar tipo de slide do esqueleto (`tpl()`), com `ms-voltar.js` antes do
  `</body>` e `node --check` no script extraído
- decidir a persistência da anotação, se um dia precisar sobreviver ao refresh
- conferência no iPad: pinça, borracha por toque e o custo do véu em aparelho
  real ainda não foram medidos fora do desktop
