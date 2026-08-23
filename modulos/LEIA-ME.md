# módulos da prancha

As peças de montar. Cada módulo é um arquivo que roda sozinho no navegador e
pode ser soldado num deck sem reescrever nada.

**Sem número de revisão.** O arquivo é o vigente; o anterior está no histórico
do Git. Nunca criar `-R2` ao lado.

| módulo | o que faz | como entra num deck |
|---|---|---|
| `capa-morph.html` | a capa padrão: marca, papel, slogan e site sobre o carrossel morph, em oliva | receita de extração em `PRANCHA-CAPA.md` |
| `divisor-morph.html` | o divisor de seção com o fundo morph atrás, em terracota. Traz controle de véu para calibrar | copiar o CSS do véu e a chamada; marcar o divisor com `fundo:true` |
| `fundo-morph-pontilhado.html` | o laboratório do fundo, com todos os controles. **Não é a capa** — serve para calibrar e copiar o preset | não entra; é banco de ensaio |
| `ms-fundo-engine.js` | a engine do morph, ~14 KB | `<script>` no fim do `<body>` + `MSFundo.montar()` |

## A engine, hoje

```js
MSFundo.montar(canvas, IMGS, {
  paper:'#6B6A4B',   // cor do papel — oliva na capa, terracota no divisor
  acc:'#B85C38',     // o acento; sobre terracota vira tinta '#211D1A'
  scale:0.85,        // escala de render: o halftone destrói detalhe de qualquer forma
  prep:false,        // pula a auto-exposição em JS; use com imagem já corrigida
  sortear:true       // embaralha a ordem na carga
});
```

Devolve `{entrada(), pausar(v), cor(o), P}`. O `cor()` migra a paleta em rampa,
que é como a troca de contexto acontece sem corte.

**Chamada antiga `MSFundo.montar(cv, IMGS)` continua idêntica** — as três opções
novas têm padrão igual ao comportamento anterior, então deck publicado não muda.

## O acervo do fundo

Nove peças em `../fundo/01.webp` a `09.webp` — **640 px, WebP q72, já
pré-expostas no arquivo**. 317 KB no total, 12,6 MB de VRAM somada.

Por que 640 e não 1024: numa tela de 2560 px, com escala 0,85 e densidade 4,5,
o shader desenha 484 pontos de trama na horizontal. A textura de 1024 entrega o
dobro do que a trama consegue mostrar. Erro de luminância medido contra 1024:
**2,5% RMS**, invisível depois do halftone. Em troca, cabem nove peças onde
cabiam três.

A pré-exposição foi aplicada no arquivo justamente para poder desligar o `prep`:
com nove peças, a passada pixel a pixel em JS seriam nove travadas na carga.
Cinco das nove precisavam de correção de gama (0,44 a 0,84 — as escuras).

A peça `01` está **espelhada de propósito**: a quina do edifício vai para a
direita e libera o lado esquerdo, onde o texto ancora.

Servidas com `?v=N` no `FUNDO_V` de quem consome. O Pages entrega com
`max-age=600`, então trocar uma peça sem subir a versão deixa o navegador no
arquivo velho.

## Ao criar um módulo novo

Um módulo entra aqui quando resolve **um** problema de prancha de forma
reaproveitável. Três exigências:

1. **Roda sozinho.** Abrir o arquivo no navegador mostra o módulo funcionando,
   sem servidor e sem dependência de CDN.
2. **Tem receita de solda.** O que copiar, onde encaixar, o que ele espera do deck.
3. **Entra nesta tabela**, com uma linha só.

Módulo que precisa de documentação longa ganha um `.md` no `prancha/` do
repositório de sistemas.
