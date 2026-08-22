# publicar apresentações — runbook

Criado em 22/08/2026. **Este arquivo é a fonte.** Vive no próprio repositório
que ele descreve, então não existe versão obsoleta noutro lugar.

## Onde as coisas moram

| o quê | onde |
|---|---|
| repositório | `steinvalente-dev/apresentacoes` — **público** |
| endereço | `https://steinvalente-dev.github.io/apresentacoes/` |
| hospedagem | GitHub Pages, `main` / `root` |
| índice | `index.html`, com o array `acervo` no fim |
| cada peça | `<slug>/apresentacao.html` |

Não passa pelo Netlify e **não consome crédito nenhum**. O site pessoal
(`michel-stein.netlify.app`) continua separado, e lá cada push custa 15 créditos.

## Publicar uma peça

1. Escrever o HTML em `<slug>/apresentacao.html`. Slug em minúsculas, sem
   acento, com hífen: `casa-ittb`, `toquio-centro`.
2. Acrescentar UM objeto ao array `acervo` do `index.html`:

```js
{
  nome: "casa ITTB",
  desc: "Estudo preliminar · 29 pranchas",
  data: "19.08.2026",
  href: "casa-ittb/apresentacao.html"
}
```

3. **Não escrever número.** O `01`, `02`, `03` sai da ordem do array.
   Mais recente em cima. `oculto: true` esconde a linha sem apagar o registro.
4. Publicar pela API de conteúdos do GitHub (`PUT /repos/.../contents/<caminho>`,
   com `sha` quando o arquivo já existe). O Pages reconstrói em ~1 minuto.
5. Conferir por HTTP antes de devolver o link: código 200 e tamanho igual ao
   do arquivo de origem.

Versão nova de uma peça já publicada **substitui** o arquivo. Não cria linha
nova — só a data muda. O histórico fica no Git.

## Devolver ao Michel

O link da peça, nunca o do índice:

```
https://steinvalente-dev.github.io/apresentacoes/<slug>/apresentacao.html
```

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

## Antes de montar a apresentação

O sistema de pranchas — os quinze gabaritos, a escala tipográfica, as regras de
marca, a lista de validação — **não está aqui**. Ler `PRANCHA-SISTEMA.md` e
`PRANCHA-CAPA.md` antes de mexer em qualquer deck. Trocar só o array `DECK`;
a engine abaixo dele não se toca.

## Histórico

- **22/08/2026** — repositório criado, Pages ligado, índice no ar.
  Publicadas `casa-ittb` (29 pranchas, R2 de 19/08) e `toquio-centro`
  (21 pranchas). A `casa-ittb` foi removida do repositório do site, onde
  existia em duplicata sob `/cliente/`.
