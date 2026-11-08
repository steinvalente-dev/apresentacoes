# Mapa de atuação — o módulo, e como alimentá-lo

Peça: `modulos/mapa-atuacao-sarasa.html`. Arquivo único, sem nenhuma
requisição externa — geometria, fotos, fontes e código moram dentro dele.
652 KB no disco, ~358 KB servidos, primeiro pixel em ~100 ms. (Era 531/268 até
08/11/2026; as 13 fotos nacionais a 256 px custaram 133 KB.)

Público:
`steinvalente-dev.github.io/apresentacoes/modulos/mapa-atuacao-sarasa.html`

Marca Sarasá: papel Cal `#F3EEE7`, tinta Ferro `#231F20`, Vinho `#79242F`,
Poppins e Archivo em base64. Ver `../marca/MARCA-SARASA.md` — o `.md` é o
mestre; divergiu, ele ganha.

---

## As três escalas

Uma projeção só para tudo: equirretangular com `k = cos(lat média de São Paulo)`,
origem no canto do bbox do município, `sx = 1000 / ((maxlon-minlon)*k)` ≈ 2368
unidades por grau. Os 27 estados e os 96 distritos estão no **mesmo sistema de
coordenadas**, então o zoom do país até a quadra é um movimento contínuo — não
há dois mapas nem corte entre eles.

| vista | viewBox | o que mostra |
|---|---|---|
| `brasil` | caixa dos 27 estados | nove estados pintados, obras fora da capital, São Paulo como ponto maior |
| `cidade` | o município inteiro | os 96 distritos, os 35 imóveis |
| `centro` | `250 372 330 300` | centro expandido — o recorte do mapa de referência |

A troca de camada é automática: acima de **3.000 unidades** de largura de
viewBox a leitura é de país, abaixo é de cidade (`CORTE`, no script). O tween
interpola o **logaritmo** da largura, não a largura — sem isso o zoom de 273×
sai atropelado no começo e arrastado no fim.

## As duas coleções

- **`ACERVO`** — 35 imóveis da cidade de São Paulo. Campos: `n` (nome),
  `st` (`ativo` | `pos`), `dist` (distrito administrativo, caixa alta sem
  acento), `aferir: true` quando o distrito foi inferido. Opcionais: `end`,
  `tomb`, `escopo`, `vig`, `foto`.
- **`OBRAS_BR`** — 13 obras fora da capital + a capital como porta de entrada
  (`capital: true`). Campos: `n`, `c` (`Cidade/UF`), `uf`, `x`, `y` já
  projetados, `foto`.

Trocar `dist`, tirar um `aferir`, acrescentar `end`/`tomb`/`escopo`/`vig`:
mapa, contadores, lista e ficha se refazem sozinhos. Não há segunda lista.

**`ATUACAO`** guarda a pintura dos estados, lida do "MAPA DE ATUAÇÃO" do
portfólio 2026 (p. 9): `3` = São Paulo, `2` = atuação com obra listada
(RJ, RS, MS, PE, MA, AM), `1` = atuação declarada sem obra aqui (BA, MT).
Estado com `1` fica pintado e sem ponto — é afirmação institucional, não dado.

## De onde vieram as fotos

Nenhuma foto é de terceiros ou da internet.

- **Os 35 da cidade** saíram do próprio mapa de atuação do estúdio, na
  apresentação da Praça Pari (`Apresentação_Projeto de adequação da Praça
  Padre Bento 05_08_2026 R01.pdf`, p. 7, no WorkDrive em
  `00-BIBLIOTECA › PORTFOLIOS`). Os 35 medalhões circulares daquela imagem
  foram detectados por forma, recortados e mascarados em círculo.
  **Limite, medido em 08/11/2026 e fechado:** a imagem dentro do PDF tem
  891 px e os 35 círculos têm raio 31–32 px — **62 px de lado, e não há outra
  cópia.** Varridos os quatro portfólios do acervo (2021, 2023, 2026 e Pari):
  o mapa é imagem já achatada, não existe original maior. Ampliados para 128 px
  por Lanczos. Seguram os 104 px do tooltip em tela 1×; em retina são esticados
  ~1,6×, e é daí que vem a moleza que se vê no iPad.
  **Só há duas saídas, e as duas custam:** upscale de IA, que inventa detalhe
  de fachada (medido numa prova: fidelidade estrutural 0,80 ao voltar a 62 px,
  erro médio 4 %), ou foto nova de cada bem, pedida ao estúdio. Nenhuma das
  duas foi feita — decisão do Michel, em aberto.
- **As 13 nacionais** saíram do `PORTFOLIO_SARASA_2026.pdf`, uma por página
  legendada, **recortadas no centro** — conferido em 08/11/2026: as 13 são
  recorte quadrado centrado, sem exceção. Quatro delas mostram trabalho de
  conservação em curso em vez do bem — foi o que a página tinha. A fonte vai de
  634 a 2 400 px, bem acima do que o medalhão pede: **regeradas a 256 px**, que
  é o que a retina consome (104 CSS px × 2).

Formato: webp com máscara circular em alpha, embutido em base64.
35 da cidade a 128 px q80–82 ≈ 203 KB · 13 nacionais a **256 px q76** ≈ 221 KB.
A qualidade caiu de 82 para 76 nas nacionais porque a 104 px de exibição o
artefato não aparece e a diferença eram 56 KB.

**Para trocar uma foto:** gerar o webp com máscara circular — 256 px quando a
origem permitir, 128 px quando não — e substituir o valor de `foto` daquele
item. Nada mais muda.

**Páginas de origem das 13**, para quem precisar refazer: Château d'Eau p. 11 ·
Ponte Torta p. 12 · Fazenda Campos Novos p. 17 · Igreja de São Benedito p. 18 ·
Cine São Luiz p. 19 · MiBIO p. 22 · Convento da Conceição p. 26 · Museu da
Energia de Itu p. 29 · Casa do Artesão p. 31 · Assoc. Comercial de PE p. 67 ·
Secretaria da Fazenda RS p. 68 · Bolsa do Café p. 73 · Museu Regional de
Olinda p. 83.

## O panorama

Botão **ver as fotos** (ou tecla V): troca os pontos pelas fotos e revela uma a
uma, **da esquerda para a direita**, ~95 ms entre cada, ~2,9 s no total. Serve à
abertura de apresentação — mostra o tamanho da carteira sem exigir que alguém
mergulhe em nada.

Os medalhões não ficam exatamente sobre o ponto: uma relaxação afasta só o
necessário para não se sobreporem, puxando cada um de volta na direção do ponto
verdadeiro, e um fio liga o medalhão ao ponto real. Sem isso, Sé e Consolação
viram uma pilha. No nível país os medalhões são menores, porque ali deslocar
pouco importa mais do que impressionar.

**Qualquer gesto** — clique, tecla, scroll, toque — encerra o panorama e
devolve o mapa interativo. Clicar num medalhão sai do panorama e abre a ficha
daquele imóvel.

## A abertura

Roda sozinha ao carregar: Brasil (2 s) → São Paulo (2,4 s) → centro expandido
(2 s) → varredura (2,9 s). ~9,5 s do começo ao fim. `prefers-reduced-motion`
desliga a sequência inteira e abre direto no centro expandido.

## Embutir numa apresentação

`<iframe>` apontando para a URL pública, nunca o arquivo colado dentro de outro
HTML — colar duplicaria ids, CSS e as fontes em base64.

```html
<iframe src="https://steinvalente-dev.github.io/apresentacoes/modulos/mapa-atuacao-sarasa.html"
        style="width:100%;height:100%;border:0;display:block" loading="lazy"
        title="Mapa de atuação do Estúdio Sarasá"></iframe>
```

No motor do deck isso é o gabarito `viva` (ver `DECK-MOTOR.md`), que é como a
planta interativa entrou no deck sem ser colada no esqueleto.

**Na prática não se escreve esse iframe à mão.** O mapa é o terceiro slide do
pacote `pacotes/sarasa-sobre/` — o bloco institucional da frente, três slides
que entram juntos. Ver `pacotes/sarasa-sobre/LEIA-ME.md`.

## O que está pendente, e não deve ser inventado

1. **15 dos 35 imóveis** estão com distrito inferido, endereço não confirmado
   com o estúdio. O chip "endereço a confirmar" isola exatamente essa lista.
2. **"Casa Museu Furio Pennacchi"** é provavelmente **Fulvio**. Mantida a grafia
   da fonte — não se corrige nome de bem tombado sem confirmação.
3. **BA, MT, AM e MA** aparecem pintados sem nenhuma obra registrada. Falta
   obra e cidade de cada um.
4. **Coordenadas das obras nacionais** são centroides de cidade, aproximados.
   Boas para mapa de apresentação, erradas para qualquer outra coisa.
5. **Tombamento, escopo e vigência** estão vazios em todos os 35.
6. **Interior de São Paulo** não tem escala própria. Jundiaí, Itu, Itanhaém e
   Santos já estão na base com coordenada — metade do caminho para um quarto
   enquadramento.
