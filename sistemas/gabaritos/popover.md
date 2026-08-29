# mecânica `popover` — o apoio que sai da tela

Módulo do deck. Vale para `unit`, `avulso` e qualquer slide com números.

## A ideia

Slide com três dados mostra **só número e rótulo**, com um `+` discreto. O texto
de apoio abre numa caixa ao passar o ponteiro. Tira texto da tela sem tirar
informação da apresentação.

## As regras

- **Sem título dentro da caixa.** Ele já está na tela, no elemento que a abriu.
- A caixa usa o **acento** da marca, texto em papel.
- Alinha pela **esquerda do elemento** e nasce logo abaixo da linha dele. Sem
  espaço embaixo, vira para cima em vez de sangrar para fora.
- No hover o elemento inteiro assume o destaque: linha, número e rótulo juntos.

## No DECK

```html
<mark class="pop" data-pop="custo">R$ 6.655/m²</mark>
```

com o texto de apoio no dicionário de popovers do deck, na chave `custo`.

## ⚠ A armadilha do quadro fixo

`getBoundingClientRect` devolve pixel de **tela**; `style.left` é pixel de
**layout**. O popover se posiciona pela diferença entre os dois, e sob o
`transform: scale(k)` do quadro fixo ele sai do lugar — quanto mais longe de
1600×900, mais longe ele vai.

**Cada delta tem de ser dividido por `k`**, lido de `--k` no momento de abrir.
Está corrigido no esqueleto; se você escrever um popover novo, herde o cálculo em
vez de reescrever.

## Validação

**Percorrer todos os alvos e conferir que nenhuma caixa ultrapassa a viewport.**
É a única forma de pegar o caso da borda direita, que só aparece no último dado
da última coluna.
