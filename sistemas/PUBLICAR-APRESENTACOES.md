# publicar apresentações — runbook

Criado em 22/08/2026. **Este arquivo é a fonte.** Vive no próprio repositório
que ele descreve, então não existe versão obsoleta noutro lugar.

## Onde as coisas moram

| o quê | onde |
|---|---|
| repositório | `steinvalente-dev/apresentacoes` — **público** |
| quem publica aqui | a prática michel stein_, a **lavrō** e a **AMAZ** — um acervo só |
| endereço | `https://steinvalente-dev.github.io/apresentacoes/` |
| hospedagem | GitHub Pages, `main` / `root` |
| índice | `index.html`, com o array `acervo` no fim |
| cada peça | `<slug>/apresentacao.html` |

Não passa pelo Netlify e **não consome crédito nenhum**. O site pessoal
(`michel-stein.netlify.app`) continua separado, e lá cada push custa 15 créditos.

## Publicar uma peça

1. Escrever o HTML em `<slug>/apresentacao.html`. Slug em minúsculas, sem
   acento, com hífen: `casa-ittb`, `toquio-centro`.
2. Acrescentar UM objeto em `pecas` do projeto certo, no array `projetos`
   do `index.html`. Projeto que ainda não existe ganha um objeto novo:

```js
{
  nome: "casa ITTB",
  pecas: [
    { nome: "estudo preliminar", pranchas: 29, peso: 11.9, data: "19.08.2026",
      href: "casa-ittb/apresentacao.html" }
  ]
}
```

**Os quatro campos da peça são obrigatórios**, e a ficha do índice sai deles na
ordem `pranchas · peso · data`.

### Peça de sistema — o bloco de baixo

Desde 23/08/2026 o `arquivo` tem **dois blocos por projeto**: as apresentações em
cima, na sequência de sempre, e embaixo **`sistema visual`** — os interativos e
demais grafismos do projeto. O separador é o mesmo `.grupo` da aba `sistema`.

Dois campos opcionais governam isso:

| campo | efeito |
|---|---|
| `tipo: "sistema"` | manda a peça para o bloco de baixo |
| `sub: "interativo"` | texto curto no lugar da contagem de pranchas, para peça que não é deck |

```js
{ nome: "marchetaria · laboratório", tipo: "sistema", sub: "interativo",
  peso: 0.050, data: "23.08.2026", href: "amaz-marchetaria/tabuas.html" }
```

A numeração `01, 02` passou a ser **por bloco**. Peça abaixo de 0,1 MB tem o peso
mostrado em **kB** — sem isso um interativo de 50 kB aparecia como `0,0 MB`.

O `peso` é o tamanho **no disco**, em MB, não o transferido. O Pages comprime na
entrega: a casa ITTB são 11,9 MB no disco e 9,3 MB no fio. Quem vai mandar a peça
por e-mail ou WhatsApp precisa do primeiro número — é por isso que ele é o que
aparece.

Medir com `curl -s -I -L <url> | grep -i content-length` **sem** mandar
`Accept-Encoding`, senão vem o comprimido. Acima de 8 MB o índice marca o número
com uma seta: passa do limite de anexo da maioria dos serviços de e-mail.

**Ao substituir uma peça, atualizar o `peso`.** É o campo que envelhece calado.

3. **Não escrever número.** O `01`, `02` sai da ordem das peças **dentro do
   projeto**. Mais recente em cima. `oculto: true` esconde sem apagar.
4. Publicar pela API de conteúdos do GitHub (`PUT /repos/.../contents/<caminho>`,
   com `sha` quando o arquivo já existe). O Pages reconstrói em ~1 minuto.
5. Conferir por HTTP antes de devolver o link: código 200 e tamanho igual ao
   do arquivo de origem.

## Revisão: substituir ou acrescentar

**Não substituir por conta própria. Perguntar sempre.** Regra revista em
22/08/2026: uma revisão nova pode virar linha nova ao lado da anterior, quando
o Michel quiser preservar aquela etapa como registro do que foi apresentado.

Duas saídas, e a escolha é dele:

- **Substituir** — sobrescreve o arquivo no mesmo caminho. Só a data muda no
  índice; a versão anterior fica no histórico do Git.
- **Acrescentar** — a peça nova entra como item novo em `pecas` do mesmo
  projeto, com caminho próprio (`<slug>/<etapa>.html`), e a anterior continua
  visível. A numeração 01, 02 é por projeto e sai da ordem do array.

Na dúvida, **acrescentar**: sobrescrever some da tela, acrescentar não.
`oculto: true` tira do índice sem apagar o registro.

## Devolver ao Michel

O link da peça, nunca o do índice:

```
https://steinvalente-dev.github.io/apresentacoes/<slug>/apresentacao.html
```

## Um acervo só — decidido em 22/08/2026

Lavrō e AMAZ publicam **neste mesmo repositório**, como projetos do array
`projetos`. Não há repositório por frente. Desmembrar fica para quando o volume
pedir; até lá, um lugar só é mais fácil de manter que três.

Consequência que precisa estar clara para quem publica de outro Projeto:
**o token deste repositório dá escrita em todas as peças, de todos os projetos.**
Uma sessão da Lavrō pode sobrescrever a apresentação da casa ITTB. Por isso a
regra de revisão vale em dobro aqui: **não substituir por conta própria.**

Peça de frente que não é a prática de arquitetura segue as mesmas regras de
sensibilidade: o repositório é público, então precificação, estratégia de
produto, análise de concorrente e dado real de obra não vêm para cá.

## ⚑ Publicar é DOIS passos, nunca um

Subir o arquivo **e** registrar no índice. Peça publicada sem registro fica no
ar e ninguém acha — não dá erro, não dá sintoma, some.

E o índice é **o único arquivo que os três Projetos disputam**. Daí a regra que
não se quebra:

> **Nunca reescrever o `index.html` a partir de cópia local.** Buscar o que está
> no repositório, alterar só o trecho necessário, e subir com o `sha` daquele
> `GET`. Subir uma cópia inteira apaga em silêncio o que outro Projeto acabou de
> registrar.

*Armadilha paga em 23/08/2026:* às 13h05 a Lavrō registrou a peça dela, às 13h16
a AMAZ registrou a sua, e às 13h31 uma sessão da prática subiu o índice inteiro
de uma cópia local para aplicar um ajuste de layout. As duas peças sumiram do
índice — os arquivos continuaram no ar. No mesmo movimento, o Tóquio voltou de
33 para 21 pranchas, valor que a cópia local trazia de horas antes. Recuperado
pelo histórico do Git.

**O índice avisa.** Desde 23/08 ele compara a árvore do repositório com o array
`projetos` e mostra um aviso quando encontra `.html` de peça que não está
listado. Usa a API pública do GitHub, que limita a 60 chamadas por hora por IP —
se estourar, o aviso silencia. É rede de segurança, não substituto do registro.

## Regras que valem sempre

- **`noindex, nofollow, noarchive`** no índice e em toda apresentação. Decisão
  de 22/08: nada disso aparece em buscador. O compartilhamento é por link.
- **`robots.txt` não funciona aqui.** Em Pages de projeto o buscador só lê o
  `robots.txt` da raiz do domínio (`steinvalente-dev.github.io`), que não é
  deste repositório. A proteção é a meta tag, e só.
- **O repositório é público.** Quem chegar em `github.com/steinvalente-dev/apresentacoes`
  navega a lista de pastas e baixa qualquer arquivo. Serve contra buscador,
  não contra curioso. **Peça sensível não vem para cá.**
- **Peso.** Pages publica no máximo 1 GB, e o histórico do Git conta. Com
  apresentação de 12 MB em base64 e revisões acumulando, isso aperta lá pela
  quadragésima. Quando incomodar: tirar as imagens do base64 e servir como
  `.webp` ao lado — o HTML cai para ~200 KB e as imagens passam a ser
  reaproveitadas entre revisões.
- **Nome de arquivo e pasta em minúsculas, sem espaço e sem acento.**
- **O índice tem duas abas.** `arquivo` lista as peças por projeto; `sistema`
  lista os documentos de método. A aba `sistema` troca o fundo da página para
  terracota — é exceção deliberada à regra de marca, pedida em 22/08 para que a
  troca de contexto seja inconfundível.

## Antes de montar a apresentação

O sistema de pranchas — os quinze gabaritos, a escala tipográfica, as regras de
marca, a lista de validação — **não está aqui**. Ler `PRANCHA-SISTEMA.md` e
`PRANCHA-CAPA.md` antes de mexer em qualquer deck. Trocar só o array `DECK`;
a engine abaixo dele não se toca.

## Histórico

- **23/08/2026** — o `arquivo` ganhou o bloco `sistema visual` por projeto, com
  os campos `tipo` e `sub`. Publicadas as duas peças interativas da marchetaria
  da AMAZ em `amaz-marchetaria/`.
- **22/08/2026, noite** — índice refeito: fundo oliva, abas arquivo/sistema
  com fundo terracota no sistema, e o arquivo passa a ser **agrupado por
  projeto**, com copiar link e abrir em cada peça. A área do cliente do site
  Netlify foi removida.
- **22/08/2026** — repositório criado, Pages ligado, índice no ar.
  Publicadas `casa-ittb` (29 pranchas, R2 de 19/08) e `toquio-centro`
  (21 pranchas). A `casa-ittb` foi removida do repositório do site, onde
  existia em duplicata sob `/cliente/`.
