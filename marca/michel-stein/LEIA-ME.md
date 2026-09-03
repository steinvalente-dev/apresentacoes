# marca michel stein_ — a pasta

O que mora aqui, e qual é o mestre de quê.

| arquivo | o que é | papel |
|---|---|---|
| `../MARCA-MICHEL-STEIN.md` | cor, tipografia, assinatura, abertura, contracapa, preset do fundo | **o mestre.** É o que as sessões leem e o deck consome |
| `../MARCA-MICHEL-STEIN-CAPA.md` | o slide de abertura: regra, receita de extração, especificação, armadilhas | mestre da capa |
| `manual.html` | as cinco folhas em desenho, numa página | **a apresentação** — o que se manda para fora |
| `bloco.html` | as cinco coisas que se colam no esqueleto: as seis fontes, os tokens por papel (`--papel --tinta --primaria --acento --escuro --acento-claro --f-display --f-corpo --f-mono`), as constantes da marca (`LOGO_CANTO LOCKUP GRAFISMO QR UNDERSCORE`), capa e contracapa | a forma executável do mestre |
| `assets/` | a versão rabisco do monograma — mestre em resolução plena, cópia de uso e o GIF | |

**Se o `.md` e o HTML divergirem, o `.md` ganha.** O manual é desenho da regra,
não a regra.

## O bloco, em uma frase

Montar uma peça michel stein_ = abrir `../../esqueleto/deck-esqueleto.html`,
colar o que está no `bloco.html`, escrever o `DECK`. A ordem completa está no
fim do próprio `bloco.html`.

Desde 03/09/2026 os nomes de token são **por papel**, iguais nos quatro blocos
(`--papel`, `--primaria`… em vez de `--creme`, `--oliva`…), e o QR da
contracapa saiu do esqueleto: mora aqui, na constante `QR`, porque aponta para
o site desta marca. `UNDERSCORE=true` é só desta marca — as outras desligam.

## Ao criar a pasta de outra marca

`marca/<nome>/` com o mesmo desenho: um `bloco.html` que roda sozinho, e o
`MARCA-<NOME>.md` um nível acima como mestre. Manual em desenho é opcional —
existe aqui porque existia antes do sistema.

**Módulo que só uma marca usa mora aqui**, não em `modulos/`. A regra: mecânica
— como algo se comporta — é compartilhada e vive em `modulos/`; identidade —
como algo se parece nesta marca — vive nesta pasta.
