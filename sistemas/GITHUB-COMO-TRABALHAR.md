# GitHub — como trabalhar e publicar

Vale para qualquer sessão, de qualquer frente. Credenciais no documento
`CREDENCIAIS.md`, nos documentos do Projeto — nunca num repositório.

## Pré-requisito que não é negociável

Publicar exige shell, git e rede: uma tarefa **Cowork**, com container.
Teste: se você não tem a ferramenta Bash, você não é Cowork e não vai
conseguir publicar. Nesse caso diga isso em uma linha e oriente — salvar
no Drive e abrir tarefa Cowork neste mesmo Projeto. Não tente e não
deixe o Michel esperando.

## Os três repositórios

| repositório | visibilidade | publica em |
|---|---|---|
| `steinvalente-dev/apresentacoes` | público | GitHub Pages — grátis |
| `steinvalente-dev/michel-stein-site` | privado | Netlify — 15 créditos por push |
| `steinvalente-dev/michel-stein-sistemas` | privado | nada; só regras |

Usuário em todos: `steinvalente-dev`. Branch: `main`. Tokens são
fine-grained, um por repositório, `Contents: read and write`. Push
voltando 403 é token expirado — pedir novo ao Michel.

## Clonar

O `NO_PROXY` não é opcional.

```
export NO_PROXY='*' HTTPS_PROXY= https_proxy= http_proxy=
GH=<token do documento de credenciais>
git -c http.proxy= -c https.proxy= clone \
  "https://x-access-token:${GH}@github.com/steinvalente-dev/<repo>.git" repo
cd repo
```

## A regra de ouro

Editar **sempre no clone fresco, no lugar**. Nunca reescrever o
`index.html` a partir de cópia local ou de memória: três Projetos
publicam no mesmo repositório e a reescrita apaga o registro que outra
sessão acabou de acrescentar. Ler o arquivo vivo, alterar a linha,
salvar.

Para conferir o estado real da origem independente de cache, query de
cache-busting: `?nc=$RANDOM` na URL raw.

## Registrar a peça — array `projetos`

Cada projeto é `{ nome, pecas: [...] }`. Cada peça:

```
{ nome:"estudo preliminar", pranchas: 29, peso: 11.9, data:"19.08.2026",
  href:"casa-ittb/apresentacao.html" }
```

Mais recente em cima. **Não escrever número** — 01, 02, 03 saem da ordem
do array. `oculto: true` esconde sem apagar o registro.
`tipo:"sistema"` joga a peça para o segundo bloco do projeto, embaixo do
separador "sistema visual". `peso` acima de 8 recebe marca sozinho:
passa do limite de anexo de e-mail.

Versão nova de peça já publicada **substitui** o arquivo e muda só a
data. Não cria linha nova.

## Registrar documento — array `docs`

A aba Sistema agrupa pelo campo `grupo`, na ordem em que os grupos
aparecem. Duas formas:

- `href: GH+"pasta/ARQUIVO.md"` — mora no repositório privado, abre no
  GitHub com a conta logada, recebe a marca `••`
- `arq: "sistemas/ARQUIVO.md"` — mora neste repositório, abre no leitor
  de markdown da própria página, recebe a marca `md`

`ver:` acrescenta o link "ver artefato" para o módulo interativo.

## Validar antes de subir

- `node --check` no script inline — um erro de sintaxe apaga a lista inteira
- abrir a página em Chromium headless e conferir que a linha nova aparece
- abrir a apresentação e conferir console limpo

O detector de peça órfã na própria página compara a árvore do
repositório com o que está listado. Se aparecer aviso, faltou o objeto
em `pecas`.

## Publicar

Agrupar a rodada num commit só.

```
git add -A && git commit -m "..."
git -c http.proxy= -c https.proxy= push origin main 2>&1 \
  | sed -E 's/(github_pat_|gh[pous]_)[A-Za-z0-9_]+/***/g'
```

Pages e Netlify reconstroem sozinhos. Sem passo manual no painel.

## Cuidados

Nome de arquivo e pasta em minúsculas, sem espaço e sem acento — o
servidor é case-sensitive e espaço vira `%20`.

Devolver o link da peça, nunca o do índice:
`https://steinvalente-dev.github.io/apresentacoes/<slug>/apresentacao.html`

Avisar de refresh forte (Ctrl+Shift+R) se ele acabou de ver a versão
anterior.

Tudo no repositório de apresentações tem `noindex, nofollow, noarchive`,
mas **o repositório é público**: quem chegar nele navega os arquivos.
Peça sensível não vai para lá — fica no Netlify, em `/cliente/`, e isso
se avisa **antes** de subir.
