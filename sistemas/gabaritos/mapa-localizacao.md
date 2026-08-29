# gabarito `mapa` · localização — onde o terreno está

Módulo do deck. **Ler só quando um mapa de localização entrar na peça.**
O resto está em `../DECK-MONTAR.md`.

Padrão adotado da casa ITTB, slide `01 · localização`, de 04/08/2026. É o mapa
que abre a seção de localização de uma apresentação de arquitetura: satélite em
sangria total, endereço por escrito, e o slide inteiro é o mapa.

Módulo que roda sozinho: `../../modulos/mapa-localizacao.html`.

> **Não confundir com `mapa-lotes.md`, ao lado.** Aquele é o cadastro desenhado,
> com hover por lote, gerado de um objeto `MAP`. Este é um embed: sem dado, sem
> levantamento, e depende de internet.

---

## No DECK

```js
{ g:'mapa', num:'01', lbl:'localização', inv:true,
  src:'https://www.google.com/maps/embed?pb=…&5e1&…',
  kick:'cidade, uf · distância da capital',
  h2:'onde o terreno está',
  lead:'rua, número · lote, quadra · condomínio ou bairro.',
  cap:'Clique no mapa para navegar · o botão devolve o teclado ao slide · precisa de internet.' },
```

| campo | o que é |
|---|---|
| `src` | a URL do embed. **`5e1` no `pb=` é o que liga o satélite** — sem isso vem o mapa de ruas |
| `kick` | o olho: cidade e a distância que dá escala |
| `h2` | o título, dentro da caixa translúcida |
| `lead` | o endereço por escrito. **Escrever, não deixar só no pino** |
| `cap` | a instrução de uso. Não é enfeite: sem ela ninguém descobre que o mapa navega |
| `inv:true` | inverte o chrome, porque o satélite é escuro |

**Como pegar o `src`:** Google Maps → Compartilhar → Incorporar um mapa → copiar
o `src` do iframe. Depois trocar `!5e0` por `!5e1` para satélite.

---

## As quatro camadas do slide

1. **iframe** em sangria total, `pointer-events:none` até o clique, com
   `filter:saturate(.82) contrast(1.04)` — o satélite cru é saturado demais e
   briga com a paleta.
2. **scrim**, gradiente denso nas pontas: ~92% de opacidade nos primeiros 7% e
   nos últimos 12% da altura, transparente no meio. **Não é degradê suave** — é
   o que faz o chrome continuar legível sobre qualquer trecho da imagem.
3. **véu** com "clique para navegar no mapa", que some ao entrar no modo de
   navegação.
4. **rótulo** no canto baixo esquerdo, em caixa translúcida própria
   (`#211D1A73` com `backdrop-filter:blur(6px)` e filete de 1px). A caixa
   garante a leitura sem apagar a imagem embaixo.

---

## A trava de teclado

**O iframe rouba as setas e a navegação do deck para.** Mesma mecânica do visor
3D:

- ativação **por clique no `.veu`**, que põe `girando` no slide e libera o
  `pointer-events` do iframe;
- botão `.sair` **fora** do iframe, que devolve o teclado;
- `desativaModelo()` varre `.g-modelo,.g-mapa` e **nunca** usa a classe `ativo`,
  que é o estado do slide visível;
- o clique do palco ignora `.g-mapa .visor`, senão navegar no mapa avançaria o
  slide.

**O `src` só é atribuído ao chegar no slide**, a partir de `data-src`. Atribuir
na carga faz o navegador baixar o mapa antes da primeira prancha.

---

## Armadilhas

**Depende de internet.** Sem rede o slide abre em branco. **Não pôr num slide
que carregue informação crítica sozinho** — se a reunião cair da rede, a
localização some. O endereço no `lead` é a rede de segurança: escrito, ele
sobrevive à falta de conexão.

**Não é validável no sandbox.** `google.com` está bloqueado no ambiente onde eu
rodo. Dá para verificar composição, scrim, véu e rótulo; **a conferência do mapa
em si depende de o Michel abrir na máquina dele.** Dizer isso na entrega.

**O `src` carrega o endereço do cliente.** A URL do embed traz o endereço por
extenso e as coordenadas. Isso é dado de cliente: não vai para o esqueleto, não
vai para o módulo, e não se copia de um projeto para outro.
