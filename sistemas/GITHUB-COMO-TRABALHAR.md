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
| binário de trabalho de projeto (PSD, DXF, base de campo) | `michel-stein-sistemas/entregas/<projeto>/` |

Documento **sem** dado de cliente vai para o público de propósito: URL
raw abre sem token, então qualquer conversa lê o arquivo, inclusive as
que não são Cowork. Esse é o ganho. Documento **com** dado de cliente
não tem esse ganho — vai para o privado e abre no GitHub logado.

## ⚑ Duas sessões, um repositório — ler antes de todo push

Frentes diferentes trabalham em Projetos diferentes, e **escrevem no mesmo
repositório**. Em 29/08/2026 isso aconteceu três vezes num dia: o push da Lavrō
apagou o registro da AMAZ, e depois um push apagou a reorganização do acervo.
Nenhum dos dois deu erro — o Git aceita, e o trabalho some em silêncio.

**O arquivo em risco é sempre o mesmo: `index.html`.** É o único que toda frente
edita. O resto — `marca/<nome>/`, `sistemas/gabaritos/`, a pasta da peça — cada
uma mexe no seu canto e não colide.

### O procedimento, sem exceção

```
git fetch origin
git status -sb          # "behind N" = alguém publicou desde o seu clone
git pull --ff-only origin main
# ... só então editar o index.html ...
git fetch origin        # de novo, imediatamente antes de subir
git push origin main
```

**Se o `push` for recusado, NUNCA `--force`.** Recusa quer dizer que existe
trabalho de outra sessão no meio. `git pull --rebase`, conferir que o que o outro
fez continua lá, e só então subir.

### Depois do pull, conferir o que sobreviveu

Puxar não é o bastante: o pull pode trazer uma versão em que a sua mudança
anterior já foi desfeita. Antes de reescrever, procurar o que você espera achar:

```
grep -c 'aba:"marca"' index.html      # as linhas que você acrescentou continuam?
```

Se sumiu, **reaplicar por cima do trabalho do outro** — nunca restaurar a sua
versão inteira, que apagaria a dele.

### E quando o outro fez melhor

Aconteceu no detector de peça órfã: duas sessões resolveram o mesmo problema, uma
ignorando pastas e a outra fazendo o detector contar `docs[].ver`. **A segunda
ataca a causa; a primeira, o sintoma.** Ficou a segunda. Ao encontrar duas
soluções para a mesma coisa, escolher e apagar a outra — deixar as duas é como
nasce a divergência silenciosa.

### O que a cópia local não sabe

Um build que gera o arquivo do zero **apaga edição feita direto no repositório**.
Antes de republicar uma peça:

```
diff <(curl -s <url da peça>) <build local>
```

---
## Subir sem registrar não conta como subir

**Padrão, sem exceção: toda coisa que entra num repositório é registrada no
`index.html` na mesma rodada.** Um commit que acrescenta arquivo e não acrescenta
o registro é uma rodada pela metade — não esperar que o Michel peça.

Arquivo no ar sem registro não dá sintoma nenhum: ele existe, funciona, e ninguém
acha. O detector de peça órfã ajuda, mas só varre `.html` **deste** repositório —
não vê `.md`, não vê binário, e não vê nada que esteja no privado. Ou seja: para
tudo o que este documento manda guardar fora do público, **o detector não cobre e
o registro é manual.**

| o que entrou | onde registrar |
|---|---|
| apresentação, peça de projeto, entrega | array `projetos`, aba Arquivo |
| documento de método, regra, ferramenta | array `docs`, aba Sistema |

Grupo novo na aba Sistema é só escrever um `grupo` que ainda não existe.

### Link que precisa funcionar no iPad, sem login

`github.com/.../raw/...` e `.../blob/...` num repositório **privado** devolvem
**404 sem sessão de navegador** — não aceitam token no header, são rotas de
navegador. Testado em 26.08.2026. Ou seja: link de repositório privado só abre
para quem estiver logado no GitHub naquele navegador, e no iPad em campo isso
não se sustenta.

Quando o arquivo precisa **baixar num toque e abrir em outro app**, o destino é
`michel-stein-site/cliente/<slug>/`, servido pelo Netlify:

- sem login, `robots.txt` com `Disallow: /cliente/` e `X-Robots-Tag: noindex`
- regra no `netlify.toml` para `/cliente/*/*.psd` com
  `Content-Type: application/octet-stream` e `Content-Disposition: attachment` —
  é isso que faz o iOS oferecer "Abrir em..." em vez de tentar exibir
- uma `index.html` na pasta, com um link `download` por arquivo: um endereço só
  para mandar por mensagem
- custo: 15 créditos por deploy e 20 por GB de banda. Um pacote de 22 MB é
  fração de crédito

**O que isso não é:** proteção. Não há senha; quem tem o endereço tem o arquivo.
Serve para base de levantamento e croqui. **Não** serve para laudo, contrato ou
documento com dado pessoal.

O mestre versionado continua no privado, em `entregas/<projeto>/`. A cópia
pública é distribuição, não arquivo.

### Peça que mora fora do repositório público

Entrega em repositório privado — PSD, DXF, binário de trabalho — entra em
`projetos` com **`href` absoluto**, a URL da pasta no GitHub. O `cartao()` já
distingue: `href` começando com `http` vai inteiro para o botão de copiar link;
`href` relativo recebe o `BASE`. Não montar URL à mão no array.

Campos úteis nesse caso: `sub` para dizer o que é e onde mora (`"PSD · repositório
privado"`), `pranchas` com `unid` para a contagem (`6` + `"vistas"`), `peso` em MB
do conjunto. Acima de 8 MB a marca de peça pesada aparece sozinha — e nesse caso
ela é informação verdadeira, não defeito.

### Binário de trabalho: `entregas/`

`michel-stein-sistemas/entregas/<projeto>/` é a exceção deliberada ao "este
repositório é só o método". Existe porque a ferramenta do Google Drive só aceita
texto e binário pequeno: arquivo de alguns megabytes não passa por ela, e passa
pelo Git — lendo do disco com `--data-binary` ou por `git push` normal.

Vale para base de campo, croqui e afins. **Não** vale para entrega final ao
cliente, que continua indo para o Drive, na pasta do projeto.

Cada pasta de projeto leva um `LEIA-ME.md` com o que há, o peso e as ressalvas.
Correção substitui o arquivo na pasta datada; versão nova ganha pasta com data
nova. O Git guarda binário por inteiro em cada versão — o histórico não encolhe
ao substituir arquivo, então repetir rodada pesada tem custo permanente.

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
