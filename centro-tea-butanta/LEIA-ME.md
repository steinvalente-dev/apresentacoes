# centro-tea-butanta — como remontar

Peça do **Centro de Acolhimento ao Autista (Butantã)**, frente Estúdio Sarasá.

## Remontar

Na raiz do clone de `apresentacoes`:

```
python3 sistemas/montar.py centro-tea-butanta --marca sarasa \
        --deck centro-tea-butanta/deck.json \
        --img  centro-tea-butanta/fonte --sobrescrever
node    sistemas/validar.mjs centro-tea-butanta/apresentacao.html
python3 sistemas/montar-indice.py
python3 sistemas/guarda-publico.py      # tem de imprimir "guarda: limpo"
```

Publicar = push em `main`. O GitHub Pages leva 1–3 min para refletir; conferir
o TAMANHO do arquivo no ar antes de dizer que subiu.

## O que mora aqui

| arquivo | o que é |
|---|---|
| `deck.json` | a fonte da peça — é ele que se edita, nunca o HTML |
| `fonte/` | imagens de origem: carrossel institucional, mapa de atuação e as camadas do `tempo` (`tempo-*.jpg`) |
| `apresentacao.html` | saída do montar; não editar à mão |
| `meta.json` | registro no acervo; escrito pelo montar |

## Duas sessões, uma peça

Esta peça é mantida pela **sessão de produção da apresentação**. A sessão de
projeto/conceito NÃO dá push nela — o token do acervo dá escrita em todas as
peças de todas as frentes, e duas sessões montando o mesmo slug se
sobrescrevem. O estado combinado entre as duas vive no Notion, na entrada
**"Estado da apresentação"** do Diário de bordo — Sarasá.

## Gabaritos próprios desta peça

A abertura institucional usa `meia` com `imgs` + `legs` — pilha de imagens com
legenda, girando a 3,2 s sem reiniciar na troca de slide. Foi acrescentado ao
esqueleto em 30/10/2026; ver os comentários no `deck-esqueleto.html`.

## A linha do tempo (slide 9, gabarito `tempo`)

As camadas vêm do servidor de raster do GeoSampa, **não** da página de
download — aquela está atrás de bloqueio anti-robô e não se automatiza.
Todas no mesmo recorte, para registrarem pixel a pixel:

```
http://raster.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wms
  ?service=WMS&version=1.1.1&request=GetMap&srs=EPSG:31983&styles=
  &bbox=321655,7388660,322295,7389300&width=3000&height=3000
  &format=image/png&layers=<CAMADA>
```

640 × 640 m centrados no polígono oficial do parque (`pde_parque_municipal`,
`Chácara do Jockey`, PQ_BT_17). O servidor recusa pedidos acima de 4096 px.
Camadas usadas: `SaraBrasil_1930`, `Vasp_Cruzeiro`, `Folhas_do_Livro_1988`,
`Orto_MDC` (2004), `Orto_PMD_RGB_2017`, `ORTO_RGB_2020`.

**Três ressalvas que não se perdem:**

1. A `Vasp_Cruzeiro` **não tem data no metadado** — está como `s/d`, e a
   ficha diz que falta confirmar no DPH. Não datar de palpite.
2. A carta de 1988 tem resolução de origem baixa (~0,9 m/px). O que está
   aqui é o máximo que o servidor entrega, com mediana e realce de traço.
   A cópia boa é a folha avulsa, que só sai pela página bloqueada.
3. 1940, 1954, 1994/1996, 2000 e 2001 **existem** no GeoSampa e estão na
   régua como lacuna declarada. Chegando o arquivo, é trocar `vazio` por
   `src` no `deck.json` — a régua já está dimensionada para eles.

**Orçamento de imagem.** O perfil `tempo` está em 1300 px / q78 no
`montar.py` por um motivo: a 1700 px a peça passa de 8 MB em base64 e o
montador quebra em `img/` ao lado, mudando a entrega de arquivo único para
pasta. Subir a resolução é decisão consciente, não ajuste.
