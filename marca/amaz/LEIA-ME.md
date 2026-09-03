# marca AMAZ — a pasta

O que mora aqui, e qual é o mestre de quê.

| arquivo | o que é | papel |
|---|---|---|
| `../MARCA-AMAZ.md` | cor, tipografia, grafismo, o que falta decidir | **o mestre.** É o que as sessões leem e o deck consome |
| `bloco.html` | o que se cola no esqueleto: as quatro fontes, os tokens por papel (`--papel --tinta --primaria --acento --escuro --acento-claro --f-display --f-corpo --f-mono`), as constantes da marca (`LOGO_CANTO LOCKUP GRAFISMO QR UNDERSCORE` — canto em texto, wordmark como `LOCKUP`, sem QR, sem underscore), abertura e contracapa | a forma executável do mestre |

**Se o `.md` e o HTML divergirem, o `.md` ganha.**

**Marcadores para máquina (03/09/2026):** o `bloco.html` traz `/* TRECHO:fontes */`, `/* TRECHO:root */`, `<!-- TRECHO:constantes -->`, `<!-- TRECHO:abertura -->` e `<!-- TRECHO:contracapa -->`, cada um fechado por `/TRECHO` — é o que `sistemas/montar.py` lê para colar nos `COLAR:x` do esqueleto. Invisíveis na página; não mudam o que se copia à mão.

## As peças de marca já publicadas

Material de identidade que existe no acervo desde 23/08/2026, e de onde a marca
foi levantada:

| peça | o que traz |
|---|---|
| `../../amaz-identidade/apresentacao.html` | **a identidade visual — o artefato da linha `marca · amaz`** no acervo |
| `../../amaz-marchetaria/apresentacao.html` | o documento do grafismo — o mestre escrito |
| `../../amaz-marchetaria/laboratorio.html` | o laboratório do gerador, interativo |

**A linha `marca · amaz` abre a identidade visual, não a institucional.** Até
29.08.2026 o `ver artefato` dessa linha apontava para `amaz-r1/apresentacao.html`
— o deck institucional inteiro, que não é peça de marca. Corrigido em 30.08: a
linha passou a abrir `amaz-identidade/apresentacao.html`, e a linha separada
`identidade visual`, que apontava para o mesmo arquivo, foi absorvida. É o mesmo
desenho das outras marcas: uma linha `marca · <nome>`, com o `.md` no **ler** e a
peça da identidade no **ver artefato**. **O R1 é apresentação, e vive só na aba
arquivo.**

**A marchetaria mora inteira em `amaz-marchetaria/`.** Reorganizada em
29.08.2026: eram três peças — o documento em `amaz-grafismo/`, o laboratório e o
campo quadrado. O campo quadrado saiu, porque é o corte **1×1** do laboratório e
o vocabulário das seis peças está na seção 02 do documento. Os três documentos
que viviam no Projeto do Claude foram apagados na mesma rodada: estavam
desatualizados contra este acervo — falavam em cinco regras, e o sistema tem
seis. **Não recriar. Divergiu, o acervo ganha.**

**Convenção de nome: o assunto vem primeiro, a categoria depois.** É
`marchetaria · o documento`, nunca `grafismo · marchetaria` — a AMAZ tem um
grafismo só, e é este.

**São peças de marca, não de projeto** — por isso vivem na aba *marca* do acervo,
e não na aba *arquivo*, que guarda apresentação de cliente. Movidas em
29/08/2026, a pedido do Michel.

Na aba *arquivo* a AMAZ mantém só o que é apresentação: as duas institucionais e
os dois protótipos.

## Ao criar a pasta de outra marca

`marca/<nome>/` com o mesmo desenho: um `bloco.html` que roda sozinho, e o
`MARCA-<NOME>.md` um nível acima como mestre.

**Módulo que só uma marca usa mora aqui**, não em `modulos/`. A regra: mecânica —
como algo se comporta — é compartilhada e vive em `modulos/`; identidade — como
algo se parece nesta marca — vive nesta pasta.
