# Nuvem de pontos → malha, ortofoto e deck

Método validado em 31.08.2026 num levantamento por drone de sítio rural
tombado: LAZ de 285 MB, 21,4 milhões de pontos, saída de Agisoft Metashape.
Entrada a entrega em uma sessão. Este documento existe para a próxima não
redescobrir nada.

Sem dado de cliente de propósito — o método abre por URL raw, de qualquer
conversa.

---

## A decisão que vem antes de tudo

**Pedir a malha a quem processou.** A empresa que voou já tem as fotos, as
poses de câmera e a malha texturizada. Reconstruir a partir da nuvem é o plano
B, e dá resultado pior: sem as fotos originais a cor vem do ponto, não da
textura. Se eles têm o OBJ, o arquivo já existe e é de graça.

Só malhe a nuvem quando eles não entregarem a malha, ou quando você precisar de
um produto que eles não fizeram — ortofoto em outra resolução, recorte, MDS.

## O que pedir junto com a nuvem

- malha texturizada em OBJ ou FBX (+ `.mtl` e os JPG), e o GLB se houver
- ortomosaico GeoTIFF, com o GSD declarado em cm/pixel
- MDT e MDS, e curvas de nível em DXF
- nuvem em LAS/LAZ, **classificada** se possível
- relatório de processamento: GSD, erro de reprojeção, e sobretudo
  **houve apoio de campo? GCP ou RTK?**
- sistema de coordenadas e datum vertical
- cessão de uso das imagens, se o material vai para deck ou acervo público

**A pergunta do apoio de campo é a que importa.** Sem GCP ou RTK o modelo tem
forma correta e posição absoluta errada — pode flutuar metros em cota. Para
cota de soleira e amarração de divisa isso é decisivo. O LAZ não diz se houve;
tem que perguntar.

---

## O pipeline, sete passos

### 1 · Ler o cabeçalho antes de qualquer coisa

```python
import laspy
f = laspy.open('nuvem.laz'); h = f.header
h.point_count, h.version, h.parse_crs()
h.mins, h.maxs
[d.name for d in h.point_format.dimensions]
```

Quatro coisas decidem o resto: **contagem de pontos** (dimensiona tudo), **CRS**,
**se há normais** e **se há classificação**. Um campo `confidence` denuncia
Metashape.

`laspy` + `lazrs` leem LAZ direto, sem descompactar. `pyproj` é preciso para
`parse_crs()`, e não vem junto.

### 2 · Filtrar por `confidence`, quando existe

O `confidence` do Metashape é o **número de imagens que viram cada ponto**. Ponto
com 1 ou 2 é ruído de baixa redundância fotográfica — quase sempre vegetação
fina, borda de recorte e mosquito no ar.

`confidence >= 3` cortou 28,6% dos pontos e melhorou visivelmente a superfície.
É o filtro mais barato do pipeline. **Rodar sempre que o campo existir.**

### 3 · Rasterizar em grelha, com percentil de Z

Dado aéreo é **campo de altura**: um Z por XY. A superfície que interessa é a
superior — o MDS. Então, por célula de grelha, pegar um Z alto, não a média.

Grelha de **5 cm**, Z no **percentil 92** de cada célula. O percentil, não o
máximo: o máximo captura o outlier no ar que sobrou do filtro.

Implementação que roda em milhões de pontos sem estourar memória — ordenar por
(célula, z) e indexar por deslocamento dentro do grupo:

```python
cell = iy.astype(np.int64)*nx + ix
order = np.lexsort((z, cell)); cell_s = cell[order]
novo   = np.r_[True, cell_s[1:] != cell_s[:-1]]
uniq   = cell_s[novo]
starts = np.searchsorted(cell_s, uniq, 'left')
counts = np.r_[starts[1:], len(cell_s)] - starts
pick   = starts + np.floor(0.92*(counts-1)).astype(np.int64)
sel    = order[pick]        # um índice de ponto por célula
```

Guardar a **origem local** e subtrair de X e Y antes de converter para
`float32`. Coordenada UTM inteira em `float32` perde precisão na casa do
decímetro — erro silencioso, e o modelo chega torto sem ninguém ver.

### 4 · Preencher lacuna pequena, e só ela

`scipy.ndimage.distance_transform_edt(~mask, return_indices=True)` dá, para cada
célula vazia, a distância e o índice do vizinho ocupado mais próximo. Preencher
só onde a distância é de até ~3 células (15 cm na grelha de 5 cm).

Buraco maior é ausência de dado e **tem que continuar buraco**. Fechar sombra de
árvore inventa terreno.

### 5 · Malhar por grelha regular, não por Delaunay nem Poisson

Este é o aprendizado central.

| método | por que não |
|---|---|
| **Poisson** | supõe superfície fechada, exige normais e **infla o terreno** — cria volume onde não há. Errado para dado aéreo |
| **Delaunay 2.5D** | correto em geometria, mas o qhull em milhões de pontos consome memória de forma imprevisível e pode não voltar |
| **grelha regular** | ✔ dois triângulos por quadrado, memória previsível, malha limpa e regular, custo zero de biblioteca |

Se você já rasterizou em grelha (passo 3), a triangulação é determinística e não
precisa de algoritmo nenhum:

```python
a = idx[:-1,:-1]; b = idx[:-1,1:]; c = idx[1:,1:]; d = idx[1:,:-1]
ok = M[:-1,:-1] & M[:-1,1:] & M[1:,1:] & M[1:,:-1]   # os 4 nós existem
F  = np.vstack([np.c_[a[ok],b[ok],c[ok]], np.c_[a[ok],c[ok],d[ok]]])
```

**Descartar quad com salto vertical acima de ~8 m.** É o que evita parede falsa
na borda do recorte e no contorno de árvore alta. Limite generoso de propósito:
apertar demais abre buraco em fachada e em muro real.

Resolução: **20 cm** para a malha, com **textura de 5 cm** por cima. É o padrão
dos produtos tipo Google Earth — geometria média, textura fina. A textura carrega
o detalhe; adensar a malha só engorda o arquivo.

### 6 · Texturizar por projeção planar

Em 2,5D a UV é exata e trivial: `u = X/Xmax`, `v = 1 - Y/Ymax`. Sem pose de
câmera, sem atlas, sem unwrap.

A ortofoto sai do mesmo raster do passo 3 — a cor do ponto escolhido por célula.
**Isso significa que a ortofoto é subproduto gratuito da malha**, e costuma ser o
entregável mais útil de todos: base de implantação em CAD, em escala, com
georreferência.

Atenção ao **sentido de V**: raster com linha 0 no Y mínimo precisa de
`FLIP_TOP_BOTTOM` na imagem, ou `1-v` na UV. Errar isso espelha a textura, e o
sintoma é sutil — o modelo parece certo até alguém ler uma placa.

### 7 · Exportar em três pesos

| formato | quando | limite |
|---|---|---|
| **GLB** | SketchUp, web, deck, celular | arquivo único, textura embutida — **preferir sempre** |
| **DAE** | plano B do GLB | ~2,6× o tamanho do GLB |
| **PLY** | CloudCompare, MeshLab | cor por vértice, malha cheia |
| **OBJ** | só se pedirem | três arquivos que se perdem, e ASCII pesado |

Decimação por colapso de aresta com `fast_simplification.simplify` — rápido e
preserva silhueta. **Recalcular a UV depois de decimar** a partir do XY novo; a
UV antiga não sobrevive ao remapeamento de vértice.

Alvos: **~450 k triângulos** para SketchUp, **~300 k** e textura 4096 para deck
web (dá GLB de 9 a 17 MB).

---

## SketchUp — o que se aprendeu na prática

**A lista de importação varia por versão e por licença. Perguntar qual ela é
antes de gerar o arquivo.** Numa instalação real de 2026 a lista **não tinha
OBJ**, e tinha glTF binário, COLLADA, 3DS, STL, KMZ, DEM — e as quatro linhas
do **Scan Essentials** (Las, Laz, Ply, e57).

Três consequências:

1. **GLB é o alvo padrão**, não OBJ. Arquivo único, textura dentro, nada de MTL
   para se perder ao mover de pasta.
2. **Scan Essentials na lista = SketchUp Studio.** Aí a nuvem `.laz` original
   importa direto, sem malha no meio, e o Scan Essentials decima a exibição
   sozinho. Para **medir cota e alinhar geometria nova**, ponto real bate malha
   interpolada. Vale importar os dois e comparar.
3. A malha entra **travada, em Tag própria**, como contexto. 450 k faces é o teto
   prático; navegar pede sombras desligadas.

Dizer sempre as constantes de volta ao absoluto no arquivo de leia-me, porque a
malha sai em coordenada local:

```
E = X_local + <origem E>
N = Y_local + <origem N>
Z = Z_local + <Z mínimo>
```

## Deck interativo

**GLB + `<model-viewer>`.** Uma tag, roda no celular, sem plugin, arquivo
hospedado no próprio repositório. Orçamento: **10 a 25 MB**; acima disso o
celular sofre.

**Não usar Sketchfab.** A Epic vem desativando o serviço desde 2024, fundindo no
Fab, loja fechada e download removido. Peça de cliente em cima disso é dívida.

Duas ressalvas: o `model-viewer` vem de CDN — para deck autossuficiente, baixar
o `.min.js` e servir local. E o GLB fica ao lado do HTML, não em base64 dentro
dele, o que rompe a auto-suficiência dos decks. É o preço, e é conhecido.

Resolução cheia e navegável de verdade pede **3D Tiles + CesiumJS** — que é a
tecnologia do Google Earth. Muito mais trabalho.

## Se o objetivo é só o *aspecto*

Malha de varredura **terrestre** não se parece com Google Earth: varredura de
solo não tem dado de telhado, e a cor vem do ponto. Para o aspecto, os caminhos
são fotogrametria de drone (RealityCapture ficou gratuito abaixo de US$ 1 M/ano
de faturamento) ou **gaussian splatting** (Luma AI, SuperSplat e Nerfstudio
gratuitos; Postshot roda offline). Splat impressiona e **não mede** — não corta
seção, não vira DXF.

Para navegar varredura terrestre no browser, o produto é **Cintoo**: converte a
nuvem em malha, uma por estação, e exige **E57 estruturado com panoramas** —
nuvem unificada não sobe, e isso se pede ao topógrafo antes da entrega, porque
depois não tem conserto.

---

## Enviar arquivo grande para a sessão

Anexo de chat não passa de dezenas de MB, e `.laz` não é tipo aceito. O caminho
é **link do Drive com "qualquer pessoa com o link"**, e download por terminal:

```bash
export NO_PROXY='*' HTTPS_PROXY= https_proxy= http_proxy=
pip install --break-system-packages -q gdown
gdown "<ID do arquivo>" -O nuvem.laz      # --fuzzy não existe nesta versão
```

O `gdown` trata a tela de aviso de antivírus que o Drive impõe em arquivo grande.
Passar o **ID**, não a URL.

**Não usar o conector do Drive para binário grande** — ele devolve base64 dentro
da conversa e estoura o contexto. Tem que ser terminal.

**WeTransfer não funciona** (a página exige JavaScript).

## Devolver arquivo que o celular não abre

`.obj` e `.mtl` não têm app no iOS: o botão de download não vai a lugar nenhum.
**Zipar** resolve — o app Arquivos descompacta nativamente. Bônus: OBJ é ASCII e
comprime ~70%.

Melhor ainda é não precisar: **GLB é um arquivo só**, e o problema não aparece.

## Orçamento de máquina

3 GB de RAM no container. Referência medida:

| etapa | 21,4 M pontos |
|---|---|
| leitura do LAZ completo | ~1,2 GB de pico |
| grelha de 5 cm (6070 × 3929) | Z `float32` 96 MB + RGB 72 MB |
| malha de 20 cm | 1,9 M triângulos, 994 k vértices |
| pipeline inteiro | poucos minutos |

Acima de ~50 M pontos: ler em chunk com `laspy.open().chunk_iterator()`,
rasterizar por ladrilho e costurar. A malha sai em resolução de grelha, não de
ponto bruto — e isso se diz ao Michel, não se esconde.

Salvar arrays intermediários em `.npy` entre etapas. O passo caro é a leitura do
LAZ; não repetir.

## Bibliotecas

```bash
pip install --break-system-packages laspy "laspy[lazrs]" pyproj \
    trimesh pygltflib fast-simplification pycollada
```

`open3d` e `pye57` são instaláveis, mas **não foram necessários**: grelha regular
dispensa o open3d, e E57 estruturado vai para o Cintoo, não para cá.

## Conferir antes de entregar

Três renders, sempre, e olhar os três:

1. **ortofoto reduzida** — a textura está certa e no sentido certo?
2. **hillshade do MDS** (`matplotlib.colors.LightSource`) — a geometria está
   certa? É aqui que se vê água de telhado, e é a melhor peça para leitura de
   caimento e infiltração
3. **render em perspectiva** — comparar com a imagem que o fornecedor mandou. Se
   reproduz, o pipeline está correto

Render por z-buffer de vértices em numpy puro é suficiente e não precisa de GPU.
**Cuidado com o sinal do eixo Z da câmera** — errar dá tela vazia, e a tela vazia
parece falha de dado quando é só sinal trocado.

## O que a malha não serve

- **Fachada e elevação.** 2,5D é um Z por XY: face vertical estica, parede borra.
  Vale para implantação, terreno e telhado. Para fachada, o produto é a
  ortoimagem plana de varredura terrestre.
- **Leitura de estado de conservação.** A malha **interpola**: onde não havia
  ponto, o algoritmo fechou superfície, e ela não se distingue visualmente da
  medida. Fissura fechada por interpolação desaparece sem deixar rastro. A base
  do mapeamento de danos continua sendo nuvem e ortoimagem.
- **MDT.** Sem classificação, árvore é volume opaco e não há terreno nu. Pedir a
  nuvem classificada, ou é etapa nova.

## Pendências de sistema

- **Falta código de tipo para modelo 3D e ortofoto** na nomenclatura. Sugerido:
  **`MOD`** e **`ORT`**. Enquanto não estiver registrado, arquivo de malha sai com
  nome descritivo — e não se inventa código no meio de uma entrega.
- **`.RCP` continua fora de alcance:** contêiner proprietário Autodesk, sem
  biblioteca aberta. Só ReCap e Civil 3D falam. Pedir `.las`/`.laz`/`.e57`.
