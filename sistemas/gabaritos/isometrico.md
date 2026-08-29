# desenho isométrico dentro do slide

Módulo do deck. Vale para qualquer SVG isométrico gerado por código.

## A regra que custou caro

**Não escrever o `viewBox` à mão.** Escrito à mão, ele decepa os últimos volumes
toda vez que o espaçamento muda — e o sintoma aparece só no slide, depois de
pronto.

Calcular de `getBBox()` **depois da inserção**, com 3,5% de folga. A folga cobre
chão, rua, árvores, rótulos e legenda, que ficam fora da caixa dos volumes.

```js
const bb = svg.getBBox(), f = 0.035;
svg.setAttribute('viewBox',
  `${bb.x - bb.width*f} ${bb.y - bb.height*f} ${bb.width*(1+2*f)} ${bb.height*(1+2*f)}`);
```

## Cor pelo fundo

O desenho troca de cor conforme o slide: tinta sobre papel, papel sobre a
primária. **Sem isso ele some no slide de cor chapada** — e some inteiro, sem
erro no console, o que faz perder tempo procurando no lugar errado.
