# gabarito `modelo` — visor 3D

Módulo do deck. **Ler só quando um visor 3D entrar na peça.**

## A regra

**Sem título, sem subtítulo, sem legenda: o slide é o visor.** Qualquer texto
rouba área da experiência de girar o modelo.

## A trava de teclado

O iframe rouba as setas e a navegação do deck para. Por isso:

- a ativação é **por clique num `.veu`** que cobre o iframe;
- há um botão `.sair` **fora** do iframe;
- `desativaModelo()` varre `.g-modelo,.g-mapa` e **nunca** usa a classe `ativo`,
  que é o estado do slide visível;
- o `src` só é atribuído ao chegar no slide, a partir de `data-src`. Atribuir na
  carga faz o navegador baixar o modelo inteiro antes da primeira prancha.

## Depende de rede

**Sem internet o slide abre em branco.** Não pôr um visor num slide que carregue
informação crítica sozinho — se a reunião cair da rede, aquele argumento some.

Vale o mesmo para qualquer embed de terceiro.

## Não é validável no sandbox

Os domínios de modelo 3D estão bloqueados no ambiente onde eu rodo. Dá para
verificar composição, véu e rótulo; **a conferência do visor em si depende de o
Michel abrir na máquina dele.** Dizer isso na entrega, não deixar implícito.
