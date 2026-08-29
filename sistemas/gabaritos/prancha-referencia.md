# gabarito `prancha` — a prancha de referência

Módulo do deck. **Ler só quando uma prancha de referência entrar na peça.**
O resto está em `../DECK-MONTAR.md`.

A grade de duas a quatro imagens que expõe **um tema**: repertório que o cliente
mandou, referências que o Michel selecionou, ou um ambiente do projeto. Padrão
adotado da casa ITTB, slides 02 a 06 e 21, de 04/08/2026.

Módulo que roda sozinho: `../../modulos/prancha-referencia.html`.

> **A composição em grade é o valor.** Se a imagem merece a tela inteira, o
> gabarito é `cheia`, não este. Este existe para as imagens serem lidas
> **juntas** — é a comparação que carrega o argumento.

---

## No DECK

```js
{ g:'prancha', num:'02', lbl:'a casa e o gramado',
  top:{ h2:'a casa se deita no terreno',
        lead:'térrea, beiral longo, piscina no mesmo plano do gramado.' },
  cols:4,
  items:[
    { src:REF_01, ar:'0.678' },
    { src:REF_02, ar:'0.561' },
    { src:REF_03, ar:'0.667' },
    { src:REF_04, ar:'0.858' }
  ]},
```

| campo | o que é |
|---|---|
| `top.h2` | **o tema**, à esquerda. É o que amarra as imagens |
| `top.lead` | **a leitura**, à direita. O que elas têm em comum, e por quê |
| `cols` | 2, 3 ou 4. Acima de 4 vira mosaico e ninguém lê |
| `items[].src` | a imagem. Vazio renderiza o slot hachurado |
| `items[].ar` | a proporção da célula. **Ver a armadilha abaixo** |
| `items[].cap` | legenda daquela imagem. Só quando cada uma carrega uma decisão diferente |
| `items[].pilha` | duas imagens empilhadas numa coluna só |

O cabeçalho é **duas pontas**: tema à esquerda, leitura à direita, alinhados pela
base. Não é título com subtítulo embaixo — é uma afirmação e a razão dela.

---

## A pilha

Duas imagens quase quadradas ocupam a coluna de **uma** retrato, sem quebrar a
grade:

```js
{ pilha:[ { src:REF_05 }, { src:REF_06 } ], ar:'0.70',
  cap:'container aberto para deck · estar externo em tela' }
```

Dentro da pilha as imagens usam `object-fit:contain`, não `cover` — são duas num
espaço de uma, e cortar aí perde o assunto. A legenda, quando existe, é **da
pilha inteira**, não de cada uma.

---

## Armadilhas já pagas

**Duas colunas com proporções diferentes transborda.** Duas células largas ficam
altas demais e invadem o cabeçalho e o rodapé. Com duas imagens de proporção
diferente, usar `duo` sem `ar` — ou `prancha` com 3 colunas.

**Sem `ar` a célula estica e o `object-fit:cover` come a imagem.** Declarar a
proporção real de cada uma. Quando qualquer `ar` está declarado, a grade passa a
**centrar** em vez de esticar (`align-content:center`), e é isso que faz uma
prancha de alturas diferentes parecer composta em vez de desalinhada.

**Croqui e planta: recortar todos com o MESMO retângulo.** Recorte individual faz
cada slide pular de posição e mata a leitura da sobreposição. O método está no
`../DECK-MOTOR.md`, seção da regra de imagem.

**Resolução:** 1800 px de largura, JPEG q82, ~400–500 KB por imagem. Referência
de repertório — imagem pequena, fundo claro — pode ir bem abaixo disso.

---

## ⚑ A proporção decide o número de colunas

**É a regra que mais muda o resultado, e a mais fácil de errar.**

| as imagens são | `ar` | colunas |
|---|---|---|
| **em retrato** — o caso normal da referência | ≤ 0.85 | **3 ou 4** |
| quadradas, ou recortadas a 1:1 | 0.85 a 1.2 | **3** |
| **deitadas** | > 1.2 | **2** — ou 3, se recortar em quadrado |

**Por que:** referência de Pinterest chega em retrato, e quatro em pé preenchem a
tela de fora a fora. As da casa ITTB estão entre `0.56` e `0.86`, e é por isso
que aquelas pranchas de quatro funcionam.

**Imagem deitada em quatro colunas fica pequena**, e sobra tarja em cima e
embaixo — o tema perde presença. Deitada pede duas colunas, com legenda por
imagem. Se você precisa de três, **recorte em quadrado**: material deitado a 1:1
volta a preencher a tela.

**Regra prática:** decida a proporção primeiro, o número de colunas depois.
O contrário — escolher quatro colunas e depois enfiar o que tiver — é o que
produz a prancha vazada.

### O gabarito avisa

O render mede a proporção média das células e reclama no console quando ela
briga com o número de colunas:

```
prancha: imagem deitada (ar~1.55) em 4 colunas.
         Deitada pede 2 colunas, ou 3 se recortar em quadrado.
```

Vale no módulo e no esqueleto. É aviso, não bloqueio — há caso legítimo de
quebrar a regra, e aí é decisão sua.

---

## A imagem que falha vira slot

O tratamento é **ouvinte de `error`, não `onerror` inline**:

```js
img.addEventListener('error', function(){
  var ph = img.parentNode;
  ph.innerHTML = '<div class="slot">…</div>';
});
```

⚠ **A versão inline que existe em outra peça está quebrada:**
`onerror="this.remove();this.parentNode.classList.add('semimg')"` remove o
elemento e **depois** tenta ler o pai, que já é nulo. O slot nunca aparecia.
Corrigido no esqueleto em 29/08/2026; nas peças publicadas o bug segue, e só
apareceria se uma imagem 404asse.

**Slot vazio é recurso, não falha.** Permite entregar a prancha montada antes de
a imagem existir, e preencher junto com o Michel — que é como ele trabalha.

---

## Texto de cliente é impessoal

No `lead`, não escrever "o que você escolheu". Escrever **"referências
selecionadas — e a análise das escolhas"**. Vale para toda prancha de repertório
que vá ao cliente.
