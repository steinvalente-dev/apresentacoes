# gabarito `mapa`

Módulo do deck. **Ler só quando um mapa entrar na peça.** O resto está em
`../DECK-MONTAR.md`.

Dois desenhos no mesmo gabarito: `which:'rua'` (os lotes de uma via, sobre o
cadastro) e `which:'cluster'` (pontos espalhados num perímetro).

## O que ele exige

Um objeto `MAP` no topo do script. **O esqueleto vem com o andaime vazio** — o
contrato à vista, sem dado.

```js
const MAP = {
  base: {
    rua:     {img:"data:image/jpeg;base64,…", w:1200, h:1500, tex:""},
    cluster: {img:"…", w:1024, h:768, tex:""}
  },
  lotes: [ {n:"rótulo", end:"Endereço, 000", lat:-23.55, lon:-46.63,
            d:[[x,y],…], r:0, t:0, offset:[0,0]} ],
  pts:   [ {n:"nome", lat:…, lon:…, k:1, pt:10, viz:[[dist,"endereço"]]} ],
  rotulo: "nome da via"
};
```

- `base.<qual>.img` é a **imagem do cadastro** em base64, e `w`/`h` são as dela.
- `lotes[].d` é o contorno em coordenadas da imagem, não em lat/lon.
- `offset` desloca o rótulo quando dois lotes vizinhos colidem.
- `rotulo` é o texto que aparece sobre a via. Vazio, não desenha nada.

## No DECK

```js
{g:'mapa', which:'rua', sang:1, foto:1,
  kick:'olho', t:'a quadra',
  sub:'Os lotes reais, sobre o cadastro municipal.',
  hint:'Passe o cursor sobre cada lote.',
  leg:[['#B85C38','uma categoria'],['#211D1A','outra']]},
```

`sang:1` sangra o mapa; `foto:1` liga a foto no hover do lote, via `FOTO_LOTE`.

## Armadilhas já pagas

**O texto de descrição do lote vaza sem avisar.** Ele só aparece no hover, então
passa despercebido numa revisão visual. Conferir com `grep` no arquivo publicado
antes de subir — foi assim que uma grafia errada de marca sobreviveu a três
revisões.

**O `MAP` de um projeto real é grande.** O do estudo de posicionamento tinha
107 KB só de lotes, com endereço e nome de operador. **Isso é dado de cliente** —
não vai para o repositório público dentro do esqueleto, e não é o tipo de coisa
que se copia de um projeto para outro por preguiça.

**O mapa depende de rede quando usa embed de terceiro.** Neste gabarito não:
o desenho é SVG gerado do `MAP`, e roda offline. O que não roda offline é o
gabarito `modelo` — ver `modelo.md`.

**A trava de teclado.** Se o mapa virar iframe algum dia, ele rouba as setas e a
navegação do deck para. A ativação passa a ser por clique num `.veu`, com um
botão `.sair` fora do iframe.
