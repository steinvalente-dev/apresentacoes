# `viva` — a peça vizinha, dentro do slide

17/09/2026. Um slide de sangria total que roda **outro arquivo HTML, da mesma
pasta da apresentação**, num quadro. Hoje é a planta interativa da Fazenda
Lageado; serve para qualquer módulo que ainda não seja gabarito do esqueleto.

```json
{ "g": "viva",
  "src": "planta-interativa.html",
  "alt": "Planta do museu, interativa: camadas, percurso, pontos de mídia",
  "lbl": "planta interativa · percurso e pontos de mídia",
  "h2":  "a planta, viva",
  "cap": "abrindo o desenho" }
```

`h2` e `cap` aqui **não são legenda de slide**: são o campo de espera, que
aparece enquanto o arquivo abre e some quando ele entra.

---

## Por que quadro, e não colado dentro do esqueleto

- a planta interativa tem **6 MB**, com CSS e ids próprios. Colada, disputa
  nome com o motor — e a receita do módulo já registrou **49 colisões de id
  entre duas exportações da mesma planta**. O quadro isola de graça.
- ela continua **um arquivo só**, que abre sozinho e se conserta sozinho.
- **o teclado fica dela enquanto o slide é dela**: evento dentro do quadro não
  chega ao motor. É isso que faz `espaço` andar no roteiro da planta em vez de
  trocar de slide.

---

## O `src` é RELATIVO. Sempre.

As duas peças moram na mesma pasta da área de cliente, então o nome do arquivo
basta — e assim o caminho da área de cliente **não é escrito em lugar nenhum**.
URL de área de cliente dentro de arquivo é o que o `guarda-publico` existe para
barrar.

⚑ `montar.py` **não passa o `src` do `viva` pelo moinho de imagem** — ele não é
imagem, e nem está na pasta de imagens: já mora ao lado da apresentação.

⚑ O publicador da pasta tem de **preservar** o arquivo vizinho. Ele não sai do
`montar`, então a limpeza de "o que saiu" o apagaria e o slide viraria campo
vazio no primeiro publish seguinte.

---

## O que o motor faz, e o que a peça faz

**O motor:**

- monta o `src` **na chegada**, não na carga — 6 MB parados atrás de trinta
  slides é memória que ninguém está usando;
- **não desmonta na saída.** Oposto do `modelo-3d`, que desmonta: lá são 40 MB
  de WebGL de outro domínio, aqui é um SVG local, e desmontar jogaria fora o
  zoom, as camadas ligadas e a anotação feita na frente do cliente;
- **foca o quadro ao chegar e devolve o foco ao sair** — é o que faz o clicker
  andar dentro da planta, e voltar a trocar de slide depois;
- `viva` está na lista **`em-imagem`** do `go()` (o fundo é visor, o chrome
  inverte) e na **`G_TRAVA`** (sem toque para avançar, sem arrasto: dentro do
  slide o dedo desenha e arrasta a planta). As setinhas seguem, porque param o
  evento antes;
- **mede o próprio chrome e manda para a peça** (`postMessage`
  `{ms:'viva-chrome',topo,pe}`), na chegada e a cada resize.

**A peça** (ver `planta-interativa.md`) liga o modo `embutida` quando está num
quadro: esconde o chrome próprio que o deck já cobre, desvia do topo e do pé
pela medida que recebeu, e **devolve o clicker ao deck quando o roteiro chega
na ponta** (`postMessage` `{ms:'viva',vai:±1}`).

---

## Armadilhas

**Proporção adivinhada por fora não fecha.** A primeira versão desviava do
chrome do deck com `clamp(96px,9vh,132px)`. Passou em 2560×1440 e em 1440×900 e
**falhou em 2560×1080**: o chrome do deck mistura largura e altura nos `clamp`,
então em tela larga e baixa ele continua alto enquanto o `9vh` já encolheu.
Por isso a medida vai medida, e não estimada.

**`file://` não serve.** Quadro de arquivo local abre com origem `null` no
Chromium — a peça fica em branco e o `postMessage` não passa. Entrega por link,
que é como esta peça já é entregue (pasta de 36 MB).

**Os dois `postMessage` conferem `location.origin`** dos dois lados. Mesma
pasta, mesma origem; qualquer outra coisa é ignorada.

---

## Pendências

- conferência no iPad: o foco do quadro em toque, e a pinça dentro do slide
  travado, ainda não foram medidos fora do desktop
- o roteiro devolve o clicker na ponta, mas **não avisa** que vai sair; se em
  apresentação isso surpreender, cabe um sinal no último passo
