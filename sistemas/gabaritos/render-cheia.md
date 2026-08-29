# gabarito `cheia` — o render em tela cheia

Módulo do deck. **Ler quando entrar render na peça** — e numa apresentação de
arquitetura isso é quase sempre.

Módulo que roda sozinho: `../../modulos/render-cheia.html`.

> **A regra, dada pelo Michel:** *"eu prefiro mil vezes mostrar esses renders bem
> grandão, pra que eles fiquem impactantes."*
>
> **Render vai em `cheia` por padrão.** Um ou dois menores, em `duo` ou
> `prancha`, quando fizer sentido comparar — mas a exceção é a imagem pequena,
> não a grande. **Uma sequência de quatro, seis renders em tela cheia é o uso
> normal do gabarito.**

---

## No DECK

```js
{ g:'cheia', num:'07', lbl:'gazebo',
  src:REND_01,
  h2:'o gazebo visto do gramado',
  cap:'A decisão que a imagem mostra — não a descrição do que já se vê.' },
```

| campo | o que é |
|---|---|
| `src` | o render. Vazio renderiza o slot hachurado |
| `h2` | o título, sobre a imagem, no pé |
| `cap` | a legenda. **Explica a decisão, não descreve a foto** |
| `lbl` | o nome do slot, quando a imagem ainda não existe |

Sem `h2` e sem `cap` o slide é só a imagem — e isso é legítimo no meio de uma
sequência, para não repetir o mesmo rótulo quatro vezes seguidas.

---

## ⚑ O texto sai de cena quando o ponteiro para

É a mecânica que define este gabarito.

Depois de **1,8 s sem movimento**, o véu do pé, o gradiente do topo **e o
chrome** esvanecem em 0,55 s. A imagem fica inteira. Qualquer gesto — ponteiro,
roda, toque ou tecla — traz tudo de volta.

**Por que existe:** o gradiente do pé é necessário para a legenda ser legível,
mas come justamente a parte de baixo do render. No render do banheiro da casa
ITTB ele escondia o piso, que era o elemento a apresentar.

**O chrome vai junto de propósito.** Sem ele a imagem não fica inteira de
verdade; e como qualquer gesto o traz de volta, não há perda de navegação.

Duas classes fazem isso:

```css
#chrome,.g-cheia .ov,.g-cheia .full:after{transition:opacity .55s var(--e-ui)}
body.em-cheia.ocioso #chrome,
body.em-cheia.ocioso .slide.ativo .ov,
body.em-cheia.ocioso .slide.ativo .full:after{opacity:0}
```

- `ocioso` é **genérico**, no `body`, ligado por um temporizador de 1,8 s;
- `em-cheia` é ligada no `go()` por `s.g === 'cheia'`, e é ela que **restringe o
  efeito a este gabarito**.

Sem a segunda, o texto sumiria em todo slide da apresentação.

**Respeita `prefers-reduced-motion`:** com a preferência ligada, nada esvanece.

---

## As duas camadas de contraste

**Gradiente do topo** — `linear-gradient(#211D1Ab8 0, #211D1A00 22%)` sobre a
imagem. Dá contraste ao chrome claro quando o render é claro no alto.

**Véu do pé** — `linear-gradient(transparent, #211D1AE6 62%)`, e o texto vive
**dentro** dele. O respiro à direita é `var(--gut) + var(--seta) * 4.4`: é o que
impede a legenda de correr por baixo das setas de navegação.

---

## Armadilhas

**`object-fit:cover` corta.** Imagem de proporção diferente de 16:9 **vai** perder
borda. **Conferir a proporção antes de mandar para `cheia`** — render quadrado ou
retrato perde teto ou piso, e aí o gabarito certo é `duo` ou `prancha`.

**Resolução: 2200 px de largura, JPEG q80** (~500–650 KB). Em sangria total a
imagem é ampliada, e 1800 px começa a amolecer.

**Imagem exportada do SketchUp com fundo transparente renderiza preto.** Já
aconteceu depois de documentado. Compor opaco em RGB antes de embutir.

**Peso.** Seis renders em `cheia` são ~4 MB só de imagem. Acima de ~8 MB no total
avisar o Michel: passa do limite de anexo de e-mail.

---

## O que ainda não está no esqueleto

`cheia` entrou em 29/08/2026. **`planta` e `desenho` continuam fora** — os dois
dependem da máquina da lupa (visor de zoom de 100 a 600%), que não foi portada.
Enquanto isso, planta e corte entram como `prancha` de uma coluna, sem zoom.
