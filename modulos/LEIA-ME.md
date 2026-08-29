# módulos do deck

As peças de montar. Cada módulo é um arquivo que roda sozinho no navegador e
pode ser soldado num deck sem reescrever nada.

**Sem número de revisão.** O arquivo é o vigente; o anterior está no histórico
do Git. Nunca criar `-R2` ao lado.

| módulo | o que faz | como entra num deck |
|---|---|---|
| `capa-morph.html` | a capa padrão: marca, papel, slogan e site sobre o carrossel morph, em oliva. **Nove peças, engine vigente, 561 KB** | receita de extração em `../marca/MARCA-MICHEL-STEIN-CAPA.md` |
| `divisor-morph.html` | divisor **com assunto**: o carrossel de peças atrás, em terracota. Véu 0.60 | copiar o CSS do véu e a chamada; marcar o divisor com `fundo:true` |
| `divisor-trama.html` | divisor **sem assunto**: nenhuma imagem, só o retículo trocando de grelha. Véu 0.55 | mesma solda; os campos vão junto, são ~40 linhas de JS |
| `fundo-morph-pontilhado.html` | o laboratório do fundo, com todos os controles. **Não é a capa** — serve para calibrar e copiar o preset | não entra; é banco de ensaio |
| `ms-fundo-engine.js` | a engine do morph, ~14 KB | `<script>` no fim do `<body>` + `MSFundo.montar()` |
| `mapa-localizacao.html` | o slide de localização: satélite em sangria, scrim, véu e o rótulo em caixa translúcida | receita em `../sistemas/gabaritos/mapa-localizacao.md` |
| `prancha-referencia.html` | a grade de 2 a 4 imagens sobre um tema, com pilha e slot | receita em `../sistemas/gabaritos/prancha-referencia.md` |
| `render-cheia.html` | o render em tela cheia, com o texto que sai de cena quando o ponteiro para | receita em `../sistemas/gabaritos/render-cheia.md` |
| `ms-voltar.js` | o chip **voltar ao acervo** e a camada de toque, ~12 KB. Vale para toda peça publicada | `<script defer src="../modulos/ms-voltar.js">` no fim do `<body>` — e nada mais |

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

## Véu por contexto — travado em 22/08/2026

| onde | véu | gradiente das pontas |
|---|---|---|
| índice do repositório | 0.18 | 0.30, transparente entre 16% e 84% |
| divisor **com** imagem | **0.60** | 0.50, transparente entre 26% e 74% |
| divisor **só trama** | **0.55** | 0.42, transparente entre 30% e 70% |

O divisor pede o triplo do índice porque carrega o maior tipo do deck
(`--fs-div` chega a 124 px) e a trama compete diretamente com o título. No
índice o texto se apoia nos cards de tinta translúcida, então o fundo pode
ficar solto.

O divisor sem assunto fica pouco abaixo do com imagem: não há foto para abafar,
mas o contraste subiu para 0.62 e a grelha sozinha ainda disputa com o título.

## O divisor sem assunto — por que existe

Decidido em 22/08/2026. O carrossel da abertura é assinatura: mostrar os
projetos ali é o ponto. No meio da apresentação de um cliente, o mesmo carrossel
vira ruído — o cliente está pensando na casa dele e aparece a orla de outro
projeto. O divisor deixou de puxar do acervo pessoal.

Como funciona, em `divisor-trama.html`: quatro **campos de luminância gerados
por código** num canvas 2D, passados à engine como se fossem fotos. Massa à
esquerda, faixas diagonais, clareira central e horizonte. Zero byte de
download; ~0,4 MB de VRAM por campo, contra 1,3 MB de uma peça real.

Calibragem própria, medida e não estimada:

| parâmetro | valor | por quê |
|---|---|---|
| transição | **serigrafia** | a grelha troca dentro do próprio retículo, sem fade e sem borrão |
| cursor | **0, desligado** | o divisor é pausa; a trama reagir ao ponteiro puxa atenção para o lugar errado |
| densidade | 5.2 | mais fina que a capa (4.5): com campo suave a trama fina lê melhor |
| contraste | 0.62 | em 0.46 a troca media 0,7 em 255 entre quadros — invisível |
| gama | 1.28 | |
| velocidade | 0.30 | troca a cada 6,5 s, volta completa em 26 s |
| zoom | 0.038 | deriva contínua, para não ficar parado entre uma troca e outra |
| sangramento | 0.10 | o campo já é massa tonal, quase não precisa sangrar |

*Armadilha paga:* na primeira versão os campos variavam só de 0,24 a 0,94 de
luminância e eram parecidos entre si. Medido em Chromium: a diferença entre
quadros consecutivos ficava em **0,7 de 255** — a troca não existia para o olho,
só aparecia num salto isolado. Abrir os campos para quase 0–1 e subir o
contraste deixou a passagem em `0,8 → 3,8 → 10,3 → 5,0`, ou seja, quatro
segundos de passagem visível dentro do ciclo de 6,5.

## Base64 no deck é decisão, não descuido

As nove peças estão servidas em `../fundo/*.webp` e seria tentador o deck
referenciá-las: tiraria ~424 KB de cada apresentação e o navegador
reaproveitaria as mesmas entre uma peça e outra.

**Não fazer.** Um deck referenciando arquivo externo só abre dentro do Pages.
Deixa de abrir de pen drive, de arquivo baixado do WhatsApp, de rede
corporativa que bloqueia, e de sala de reunião com wifi cativo — que é
exatamente a lista de casos que motivou embutir as fontes em base64, depois de
o DOM travar 12,6 s esperando uma CDN.

A conta: 424 KB num deck de 12 MB são 3,5%. Trocar isso pela garantia de abrir
sem rede é péssimo negócio. E a banda não é problema — o Pages não cobra.

O módulo `capa-morph.html` segue a mesma regra: 561 KB, autossuficiente.
Quem consome o fundo **por link**, como o índice deste repositório, aí sim
referencia `fundo/*.webp` com `?v=`.

## Ao criar um módulo novo

Um módulo entra aqui quando resolve **um** problema de deck de forma
reaproveitável. Três exigências:

1. **Roda sozinho.** Abrir o arquivo no navegador mostra o módulo funcionando,
   sem servidor e sem dependência de CDN.
2. **Tem receita de solda.** O que copiar, onde encaixar, o que ele espera do deck.
3. **Entra nesta tabela**, com uma linha só.

Módulo que precisa de documentação longa ganha um `.md` no `deck/` do
repositório de sistemas.
