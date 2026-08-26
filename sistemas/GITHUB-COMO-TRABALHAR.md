# GitHub — como trabalhar e publicar

Vale para qualquer sessão, de qualquer frente, e para qualquer coisa que
vá para o GitHub: apresentação, documento de regra, ferramenta de
navegador, rotina de automação. Credenciais no documento
`CREDENCIAIS.md`, nos documentos do Projeto — nunca num repositório.

## Pré-requisito que não é negociável

Publicar exige shell, git e rede: uma tarefa **Cowork**, com container.
Teste: se você não tem a ferramenta Bash, você não é Cowork e não vai
conseguir publicar. Nesse caso diga isso em uma linha e oriente — salvar
no Drive e abrir tarefa Cowork neste mesmo Projeto. Não tente e não
deixe o Michel esperando.

## Os três repositórios

| repositório | visibilidade | o que guarda | publica em |
|---|---|---|---|
| `steinvalente-dev/apresentacoes` | **público** | apresentações, módulos, ferramentas de navegador, docs sem dado de cliente | GitHub Pages — grátis |
| `steinvalente-dev/michel-stein-site` | privado | o site de portfólio e a área de cliente | Netlify — 15 créditos por push |
| `steinvalente-dev/michel-stein-sistemas` | privado | as regras de trabalho, com nome de cliente e caminho interno | nada; é só leitura e escrita |

Usuário em todos: `steinvalente-dev`. Branch: `main`. Tokens são
fine-grained, um por repositório, `Contents: read and write`. Push
voltando 403 é token expirado — pedir novo ao Michel.

## Onde cada coisa vai

A pergunta que decide não é "que tipo de arquivo é", é **precisa abrir
por URL** e **contém dado que não pode ser público**.

| o que é | onde vai |
|---|---|
| apresentação de projeto | `apresentacoes/<slug>/apresentacao.html` |
| módulo do sistema visual | `apresentacoes/modulos/` |
| ferramenta que roda no navegador | `apresentacoes/ferramentas/<slug>/index.html` |
| documento de método, sem dado de cliente | `apresentacoes/sistemas/<NOME>.md` |
| regra de trabalho com nome de cliente, endereço, caminho interno | `michel-stein-sistemas/<pasta>/<NOME>.md` |
| script que roda em máquina, não em navegador | `apresentacoes/ferramentas/<slug>/`, junto com o `LEIA-ME.md` |
| peça sensível de cliente | não vai para o público: `michel-stein-site`, em `cliente/` |

Documento **sem** dado de cliente vai para o público de propósito: URL
raw abre sem token, então qualquer conversa lê o arquivo, inclusive as
que não são Cowork. Esse é o ganho. Documento **com** dado de cliente
não tem esse ganho — vai para o privado e abre no GitHub logado.

## Clonar

O `NO_PROXY` não é opcional.

```
export NO_PROXY='*' HTTPS_PROXY= https_proxy= http_proxy=
GH=<token do documento de credenciais>
git -c http.proxy= -c https.proxy= clone --depth 1 \
  "https://x-access-token:${GH}@github.com/steinvalente-dev/<repo>.git" repo
cd repo
```

## A regra de ouro

Editar **sempre no clone fresco, no lugar**. Nunca reescrever o
`index.html` a partir de cópia local ou de memória: várias sessões
publicam no mesmo repositório e a reescrita apaga o registro que outra
acabou de acrescentar. Ler o arquivo vivo, alterar a linha, salvar.

Isso não é hipótese: já aconteceu, e acontece entre um push e o
seguinte na mesma tarde. Clone fresco antes de cada rodada.

Para conferir o estado real da origem independente de cache, query de
cache-busting: `?nc=$RANDOM` na URL raw ou do Pages.

## Ferramenta ou automação nova

Uma pasta por ferramenta, em `ferramentas/<slug>/`, com três coisas:

- `index.html` — a interface, arquivo único, se roda no navegador
- `LEIA-ME.md` — o que faz, como se usa, o que ainda não faz, e as
  decisões de método já tomadas. Este é o arquivo que a próxima sessão
  vai ler; sem ele a ferramenta é ilegível em duas semanas
- os scripts, se houver

Slug em minúsculas, com hífen, sem acento.

Depois de criar, **acrescentar `'ferramentas/'` já está na lista `IGNORA`
do detector de peça órfã** no `index.html` — então a ferramenta não
aparece como órfã. Em troca, ela também não aparece em lugar nenhum se
você não registrar: registrar sempre no array `docs`.

### Chave de API não vai para o repositório

Página em Pages é arquivo estático servido na internet aberta: qualquer
chave no código vira chave pública, mesmo em repositório privado, mesmo
com `noindex`. Não existe jeito de esconder.

As saídas, em ordem de preferência: a ferramenta pede a chave ao usuário
em campo próprio e guarda só em memória; ou a ferramenta roda como
artefato do claude.ai, onde a chamada é intermediada; ou a parte que
precisa de chave roda em máquina, fora do navegador, e o repositório
guarda só o script e o método. Se a ferramenta depende de chave embutida
para funcionar, ela não vai para o Pages — diga isso ao Michel antes de
montar, não depois.

Vale igual para credencial de banco, token de terceiro e URL de webhook.

### Dado de cliente não vira arquivo de exemplo

Automação de análise costuma nascer com um caso real em cima. Foto de
obra, planta, laudo, endereço e nome de cliente **não sobem** para o
repositório público — nem como exemplo, nem em pasta chamada `teste`.
Exemplo se monta com material anonimizado ou sintético. O caso real fica
no Drive, no projeto dele.

## Registrar apresentação — array `projetos`

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

## Registrar documento ou ferramenta — array `docs`

A aba Sistema agrupa pelo campo `grupo`, na ordem em que os grupos
aparecem no array. Grupo novo é só escrever um `grupo` que ainda não
existe — a aba passa a exibir o separador sozinha.

Três campos decidem o comportamento:

- `href: GH+"pasta/ARQUIVO.md"` — mora no repositório privado, abre no
  GitHub com a conta logada, recebe a marca `••`
- `arq: "sistemas/ARQUIVO.md"` — mora neste repositório, abre no leitor
  de markdown da própria página, recebe a marca `md`
- `ver: "ferramentas/<slug>/index.html"` — acrescenta o link "ver
  artefato", que abre a coisa funcionando

Ferramenta se registra com `arq` apontando para o `LEIA-ME.md` e `ver`
apontando para o `index.html`: um link para entender, outro para usar.

## Validar antes de subir

- `node --check` em cada script inline do `index.html` — um erro de
  sintaxe apaga a lista inteira, e a página quebra sem aviso
- simular o agrupamento fora do navegador: extrair o array e conferir a
  ordem dos grupos e se o `arq` referenciado existe no disco
- abrir a página em Chromium headless e conferir que a linha nova aparece
- abrir a peça ou a ferramenta e conferir console limpo
- `git diff` antes do commit: o diff tem que ser só o que você mexeu

## Publicar

Agrupar a rodada num commit só.

```
git add -A && git commit -m "..."
git -c http.proxy= -c https.proxy= push origin main 2>&1 \
  | sed -E 's/(github_pat_|gh[pous]_)[A-Za-z0-9_]+/***/g'
```

Pages e Netlify reconstroem sozinhos, em cerca de um minuto. Sem passo
manual no painel. Confirmar depois no endereço público, com
cache-busting — push aceito não é o mesmo que no ar.

O `sed` no fim não é enfeite: mensagem de erro de push devolve a URL
inteira, com o token dentro.

## Cuidados

Nome de arquivo e pasta em minúsculas, sem espaço e sem acento — o
servidor é case-sensitive e espaço vira `%20`.

Devolver o link da coisa, nunca o do índice:

```
https://steinvalente-dev.github.io/apresentacoes/<slug>/apresentacao.html
https://steinvalente-dev.github.io/apresentacoes/ferramentas/<slug>/
```

Avisar de refresh forte (Ctrl+Shift+R) se ele acabou de ver a versão
anterior.

Tudo no repositório de apresentações tem `noindex, nofollow, noarchive`,
mas **o repositório é público**: quem chegar nele navega os arquivos,
o histórico e o que já foi apagado. Segredo que entrou no Git continua
lá depois do commit que removeu — se vazou, o certo é rotacionar, não
apagar. Peça ou ferramenta sensível não vai para lá, e isso se avisa
**antes** de subir.
