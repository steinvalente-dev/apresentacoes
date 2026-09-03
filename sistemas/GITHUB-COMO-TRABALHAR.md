# GitHub — como trabalhar e publicar

Vale para qualquer sessão, de qualquer frente, e para qualquer coisa que
vá para o GitHub: apresentação, documento de regra, ferramenta de
navegador, rotina de automação. Credenciais no documento
`CREDENCIAIS.md`, nos documentos do Projeto — nunca num repositório.

**Este arquivo é o runbook único de publicação.** Em 02.09.2026 absorveu o
`PUBLICAR-APRESENTACOES.md` (hoje em `superado/`). O que era regra lá está
aqui; o que era história está na seção final.

## Pré-requisito que não é negociável

Publicar exige shell, git e rede: uma tarefa **Cowork**, com container.
Teste: se você não tem a ferramenta Bash, você não é Cowork e não vai
conseguir publicar. Nesse caso diga isso em uma linha e oriente — salvar
no Drive e abrir tarefa Cowork neste mesmo Projeto. Não tente e não
deixe o Michel esperando.

## ⚑ Público quer dizer aberto — ler antes de criar qualquer pasta aqui

`steinvalente-dev/apresentacoes` é **público**: qualquer pessoa, sem link do
acervo e sem login, lista as pastas em `github.com`, abre qualquer arquivo e
navega o histórico — inclusive o que já foi apagado. O `noindex` só tira do
Google. O acervo (`index.html`) **não é proteção**: é uma vitrine em cima de
arquivos que já estão abertos. Não existe "arquivo privado dentro de
repositório público" — a visibilidade é do repositório inteiro.

Em 02.09.2026 a auditoria encontrou aqui duas peças com nome de cliente,
endereço do lote e, numa delas, VGV e tese de aquisição — em 190 commits.
Foram movidas e o histórico foi reescrito. Para não repetir:

**A pergunta, antes de criar a pasta da peça:** a peça tem nome de cliente,
endereço, honorário, valor de negócio, planta ou foto de obra de terceiro?

| resposta | destino | registro |
|---|---|---|
| **sim** | `michel-stein-site/cliente/<slug>-<16 hex>/apresentacao.html` (Netlify) | `michel-stein-sistemas/site/AREA-CLIENTE.md` — **privado**. Nunca no `index.html` |
| não | `apresentacoes/<slug>/apresentacao.html` | `index.html`, array `projetos` |

**Como o Michel enxerga as peças de cliente no acervo:** o `index.html` lê um
registro privado (`registro.json`, no site) quando o navegador tem a **chave**
guardada no aparelho dele. Sem a chave, o acervo mostra só o público. A chave
e a URL do registro estão no privado, em `site/AREA-CLIENTE.md`. Peça de
cliente nova entra nesse `registro.json` — nunca no `projetos` daqui.

O slug de cliente leva 16 caracteres hexadecimais aleatórios
(`python3 -c "import secrets;print(secrets.token_hex(8))"`): sem eles a URL é
adivinhável. A URL da área de cliente **nunca** aparece em arquivo do
público — nem como constante, nem em comentário. Entregar o link ao Michel
pelo chat, e registrar no privado.

**Trava mecânica, obrigatória antes de todo push neste repositório:**

```
python3 sistemas/guarda-publico.py      # tem de imprimir "guarda: limpo"
```

Varre cliente nomeado no `metas`, URL de `/cliente/`, endereço com número,
CNPJ, CPF, telefone, `R$` em peça, token e chave. Achado = push não liberado:
mover o arquivo, não contornar. Exceção deliberada só com decisão do Michel,
em `sistemas/guarda-publico.allow`, com o motivo. A mesma guarda está pronta
para rodar no GitHub a cada push, em `sistemas/guarda-workflow.yml` — **ainda
não ativa**: o token de apresentações não tem permissão `Workflows`, então
o arquivo não pôde entrar em `.github/workflows/`. Ativar é um passo do
Michel: dar `Workflows: read and write` ao token (Settings → Developer
settings → Fine-grained tokens) ou mover o arquivo pelo site do GitHub. Ativa,
fica vermelha em achado — é o alarme, não o bloqueio: o Pages publica direto
de `main`.

Se mesmo assim algo sensível subir: **tirar o arquivo não basta**. É
`git filter-repo --invert-paths --path <pasta>` mais force-push, e avisar o
Michel — é o único caso em que force-push é permitido aqui.

## Barrado por permissão não é barrado por token

Sintoma: o `GET` da API funciona, o clone funciona, e só a **escrita** —
`git push` ou `PUT` de conteúdo — volta *"Permission for this action was
denied by the Claude Code auto mode classifier"*. Isso **não** é token
expirado, não é credencial faltando, e não se resolve relendo o documento
de credenciais. É o modo de aprovação da tarefa barrando escrita
autenticada na rede.

O que fazer, em ordem:

1. **Parar.** Não trocar de ferramenta para dar a volta: API de conteúdo,
   `git push` e clone com token na URL são a mesma ação, e as três são
   barradas pelo mesmo motivo. Insistir só queima rodada.
2. Deixar o commit local já feito, para o push ser o único passo que
   sobra.
3. Dizer ao Michel em **uma linha**: o que ia subir, em que repositório, e
   que falta liberar. A liberação é por escrita, não por sessão — cada
   push pede a sua.

Token expirado tem outro sintoma, e é fácil de distinguir: **403 do
próprio GitHub**, com corpo JSON. Barrado por permissão nem chega ao
GitHub.

## Ler o acervo de uma conversa que não é deste Projeto

O método sem dado de cliente mora no repositório público de propósito:
abre por URL raw, sem token e sem shell — qualquer conversa lê, inclusive
as que não são Cowork.

O que **não** abre é o repositório privado. O documento de credenciais é
documento *de Projeto*: uma conversa de outro Projeto não tem o token e
não vai ter, por mais que ele exista. Nesse caso, sem rodeio: dizer em uma
linha o que ficou fora de alcance, seguir com o que o público responde, e
oferecer abrir a tarefa no Projeto certo. **Não improvisar sobre o
conteúdo do privado** — regra de honorário e nome de cliente inventados
são pior do que a falta.

O documento chama-se `CREDENCIAIS.md`. Alguns Projetos ainda usam
`CREDENCIAIS-ACERVO.md`, do tempo em que havia um por frente — se o
primeiro nome não estiver na lista de documentos do Projeto, procurar
qualquer documento começando por `CREDENCI` antes de dizer que não há.

## Os três repositórios

| repositório | visibilidade | o que guarda | publica em |
|---|---|---|---|
| `steinvalente-dev/apresentacoes` | **público** | apresentações, módulos, ferramentas de navegador, docs sem dado de cliente | GitHub Pages, `main` / raiz — grátis, sem crédito |
| `steinvalente-dev/michel-stein-site` | privado | o site de portfólio e a área de cliente | Netlify — 15 créditos por push |
| `steinvalente-dev/michel-stein-sistemas` | privado | as regras de trabalho, com nome de cliente e caminho interno | nada; é só leitura e escrita |

Usuário em todos: `steinvalente-dev`. Branch: `main`. Tokens são
fine-grained, um por repositório, `Contents: read and write`. Push
voltando 403 é token expirado — pedir novo ao Michel.

**Um acervo só.** Todas as frentes — michel stein_, Lavrō, AMAZ, Sarasá —
publicam em `apresentacoes`, como projetos do mesmo array `projetos`. Não há
repositório por frente. Consequência: **o token dá escrita em todas as peças,
de todos os projetos** — uma sessão da Lavrō pode sobrescrever a peça de
outra frente. Daí a regra de versão (abaixo) e a de duas sessões. Peça de
outra frente segue a mesma sensibilidade: precificação, estratégia de
produto, análise de concorrente e dado real de obra não vêm para o público.

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
| peça com nome de cliente, endereço ou valor | não vai para o público: `michel-stein-site`, em `cliente/<slug>-<16 hex>/`, registrada no privado em `site/AREA-CLIENTE.md` |
| binário de trabalho de projeto (PSD, DXF, base de campo) | `michel-stein-sistemas/entregas/<projeto>/` |
| arquivo que saiu de uso, guardado só como registro | `apresentacoes/superado/` — ver o `LEIA-ME.md` de lá |
| proposta de substituição, ainda não aprovada | `proposta/`, ao lado do arquivo que ela quer substituir |
| versão anterior de peça que subiu de revisão | `<slug>/anteriores/apresentacao-R<n>.html`, `oculto:true` no índice — ver "Versão nova × revisão nova" |

Documento **sem** dado de cliente vai para o público de propósito: URL
raw abre sem token, então qualquer conversa lê o arquivo, inclusive as
que não são Cowork. Esse é o ganho. Documento **com** dado de cliente
não tem esse ganho — vai para o privado e abre no GitHub logado.

## ⚑ Duas sessões, um repositório — ler antes de todo push

Frentes diferentes trabalham em Projetos diferentes, e **escrevem no mesmo
repositório**. O Git aceita um push que apaga o trabalho do outro, sem erro —
já aconteceu mais de uma vez no mesmo dia (ver Histórico).

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

### Duas soluções para o mesmo problema: fica uma

Ao encontrar duas soluções para a mesma coisa (aconteceu no detector de peça
órfã), escolher a que ataca a causa e apagar a outra. Deixar as duas é como
nasce a divergência silenciosa.

### O que a cópia local não sabe

Um build que gera o arquivo do zero **apaga edição feita direto no repositório**.
Antes de republicar uma peça:

```
diff <(curl -s <url da peça>) <build local>
```

### A regra de ouro

Editar **sempre no clone fresco, no lugar**. Nunca reescrever o
`index.html` a partir de cópia local ou de memória: a reescrita apaga o
registro que outra sessão acabou de acrescentar, e acontece entre um push
e o seguinte na mesma tarde. Ler o arquivo vivo, alterar a linha, salvar.
Clone fresco antes de cada rodada.

Para conferir o estado real da origem independente de cache, query de
cache-busting: `?nc=$RANDOM` na URL raw ou do Pages.

---
## Subir sem registrar não conta como subir

**Padrão, sem exceção: toda coisa que entra num repositório é registrada no
`index.html` na mesma rodada.** Um commit que acrescenta arquivo e não acrescenta
o registro é uma rodada pela metade — não esperar que o Michel peça.

Arquivo no ar sem registro não dá sintoma nenhum: ele existe, funciona, e ninguém
acha. O detector de peça órfã ajuda, mas só varre `.html` **deste** repositório —
não vê `.md`, não vê binário, e não vê nada que esteja no privado. Ou seja: para
tudo o que este documento manda guardar fora do público, **o detector não cobre e
o registro é manual.** E o detector da página usa a API pública do GitHub, 60
chamadas por hora por IP — estourou, silencia. Rede de segurança, não registro.

| o que entrou | onde registrar |
|---|---|
| apresentação, peça de projeto, entrega | array `projetos`, aba Arquivo |
| documento de método, regra, ferramenta | array `docs`, aba Sistema |
| proposta, protótipo, revisão de peça — qualquer `.html` que não seja nem uma coisa nem outra | array `docs`, com `ver:` apontando para ele. **Este é o caso que escapa**: a sessão pensa "não é peça nem documento" e não registra nada |

Grupo novo na aba Sistema é só escrever um `grupo` que ainda não existe.

### Link que precisa funcionar no iPad, sem login

`github.com/.../raw/...` e `.../blob/...` num repositório **privado** devolvem
**404 sem sessão de navegador** — não aceitam token no header, são rotas de
navegador. Link de repositório privado só abre para quem estiver logado no
GitHub naquele navegador, e no iPad em campo isso não se sustenta.

Quando o arquivo precisa **baixar num toque e abrir em outro app**, o destino é
`michel-stein-site/cliente/<slug>-<16 hex>/`, servido pelo Netlify:

- sem login; `X-Robots-Tag: noindex` pelo `netlify.toml`. O `robots.txt` **não**
  lista `/cliente/` — listar anunciaria o caminho
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

**Não se registra no `index.html`.** Registrar com `href` absoluto publicava a
URL da área de cliente para qualquer visitante e anulava a proteção. O registro
dessas peças e entregas é o `michel-stein-sistemas/site/AREA-CLIENTE.md`,
privado. O `cartao()` continua aceitando `href` absoluto para link que possa
ser público (repositório de terceiro, página institucional) — nunca para
`/cliente/`.

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

Publicar é por `git push`. A API de conteúdos (`PUT .../contents/<caminho>`,
com `sha`) funciona e vale para um arquivo avulso, mas não é o caminho
principal: não dá `diff`, não dá `git status -sb`, e é onde o `index.html`
já foi sobrescrito por cópia local.

## Ferramenta ou automação nova

Uma pasta por ferramenta, em `ferramentas/<slug>/`, com três coisas:

- `index.html` — a interface, arquivo único, se roda no navegador
- `LEIA-ME.md` — o que faz, como se usa, o que ainda não faz, e as
  decisões de método já tomadas. Este é o arquivo que a próxima sessão
  vai ler; sem ele a ferramenta é ilegível em duas semanas
- os scripts, se houver

Slug em minúsculas, com hífen, sem acento.

`'ferramentas/'` já está na lista `IGNORA` do detector de peça órfã no
`index.html` — a ferramenta não aparece como órfã. Em troca, ela também não
aparece em lugar nenhum se você não registrar: registrar sempre no array `docs`.

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

## Antes de montar a apresentação

O sistema do deck — gabaritos, escala, marca, validação — **não está aqui**.
Ler `DECK-MONTAR.md` e `../marca/MARCA-<nome>.md`, e abrir a peça de
referência `emei-presidente-dutra` antes de montar. Trocar só o array `DECK`;
a engine abaixo dele não se toca.

## Registrar apresentação — array `projetos`

Cada projeto é `{ nome, pecas: [...] }`. Projeto que ainda não existe ganha um
objeto novo. Cada peça:

```
{ nome:"estudo preliminar", pranchas: 29, peso: 11.9, data:"19.08.2026",
  href:"<slug>/apresentacao.html" }
```

**Os quatro campos são obrigatórios**; a ficha do índice sai deles na ordem
`pranchas · peso · data`. Slug em minúsculas, sem acento, com hífen:
`emei-presidente-dutra`, `lavro-grafismo`.

Mais recente em cima. **Não escrever número** — 01, 02, 03 saem da ordem
do array, por bloco. `oculto: true` esconde sem apagar o registro.

**Peça de sistema — o bloco de baixo.** Cada projeto tem dois blocos: as
apresentações em cima e, embaixo do separador "sistema visual", os interativos
e demais grafismos. Dois campos opcionais:

| campo | efeito |
|---|---|
| `tipo: "sistema"` | manda a peça para o bloco de baixo |
| `sub: "interativo"` | texto curto no lugar da contagem de pranchas, para peça que não é deck |

**`peso` é o tamanho no disco, em MB**, não o transferido — o Pages comprime
na entrega, e quem manda a peça por e-mail ou WhatsApp precisa do número do
disco. Medir com `curl -s -I -L <url> | grep -i content-length` **sem**
`Accept-Encoding`. Acima de 8 MB o índice marca sozinho: passa do limite de
anexo de e-mail. Abaixo de 0,1 MB o índice mostra em kB. **Ao substituir uma
peça, atualizar o `peso`** — é o campo que envelhece calado.

## Versão nova × revisão nova

Decisão do Michel, 02.09.2026. Substitui as duas regras que conviviam até
aqui ("substitui" num arquivo, "nunca substitua, acrescente" no outro).

- **Ideia em desenvolvimento → versão nova.** A peça nova **substitui** o
  arquivo no mesmo caminho. No `index.html` mudam só `data` e `peso`. O Git
  guarda o histórico; a interface mostra uma peça.
- **Revisão nova (R2, R3…) só quando o Michel disser.** Aí sim é linha nova em
  `pecas`. A versão anterior vai para `<slug>/anteriores/apresentacao-R<n>.html`
  e entra no índice com `oculto:true` — estocada no GitHub, fora da interface.
  Registrada, o detector de órfã não a acusa.
- **A sessão pergunta.** Peça publicada há um ou dois dias, antes de
  sobrescrever: *"esta peça já foi apresentada ao cliente? sobe de revisão?"*
  Peça de horas não precisa da pergunta; peça de dias não se decide sozinha.

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

- **`python3 sistemas/guarda-publico.py` → `guarda: limpo`.** Primeiro de
  todos; achado = não sobe (seção "Público quer dizer aberto")
- **toda peça leva, antes do `</body>`,**
  `<script defer src="../modulos/ms-voltar.js"></script>` — sem ela a peça
  abre sem saída (o índice abre em aba nova). O caminho é relativo e vale
  porque toda peça mora a um nível da raiz; peça mais funda ajusta o `../`.
  Comportamento e detalhes em `DECK-MOTOR.md`
- **`noindex, nofollow, noarchive`** no índice e em toda peça. `robots.txt`
  não funciona em Pages de projeto — o buscador só lê o da raiz do domínio,
  que não é deste repositório. A meta tag é a única proteção contra buscador
- `node --check` em cada script inline do `index.html` — um erro de
  sintaxe apaga a lista inteira, e a página quebra sem aviso
- simular o agrupamento fora do navegador: extrair o array e conferir a
  ordem dos grupos e se o `arq` referenciado existe no disco
- abrir a página em Chromium headless e conferir que a linha nova aparece
- abrir a peça ou a ferramenta e conferir console limpo
- `git diff` antes do commit: o diff tem que ser só o que você mexeu
- **rodar o detector de órfã no disco, antes do push** — o da página só
  avisa depois que o arquivo já está no ar, e quem vê é o Michel:

```
python3 - <<'EOF'
import re, pathlib
s = open('index.html', encoding='utf-8').read()
reg = set(re.findall(r'(?:href|ver)\s*:\s*"([^"?]+)"', s))
IGN = ('index.html','sistemas/','modulos/','fundo/','ferramentas/','superado/','.git')
orfas = sorted(str(p) for p in pathlib.Path('.').rglob('*.html')
               if not str(p).startswith(IGN) and str(p) not in reg)
print('\n'.join(orfas) if orfas else 'nenhuma órfã')
EOF
```

  Tem de imprimir `nenhuma órfã`. Se imprimir caminho, a rodada não está
  fechada — registrar e só então subir.

## Publicar

Agrupar a rodada num commit só.

```
git add -A && git commit -m "..."
git -c http.proxy= -c https.proxy= push origin main 2>&1 \
  | sed -E 's/(github_pat_|gh[pous]_)[A-Za-z0-9_]+/***/g'
```

Pages e Netlify reconstroem sozinhos, em cerca de um minuto. Sem passo
manual no painel. Confirmar depois no endereço público, com
cache-busting — push aceito não é o mesmo que no ar: **código 200 e tamanho
igual ao do arquivo de origem**, antes de devolver o link.

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

**Peso do repositório.** Pages publica no máximo 1 GB, e o histórico do Git
conta. Com peça de 12 MB em base64 e versões acumulando, isso aperta lá pela
quadragésima. Quando incomodar: tirar as imagens do base64 e servir como
`.webp` ao lado — o HTML cai para ~200 KB e as imagens passam a ser
reaproveitadas entre versões.

Tudo no repositório de apresentações tem `noindex, nofollow, noarchive`,
mas **o repositório é público**: quem chegar nele navega os arquivos,
o histórico e o que já foi apagado. Segredo que entrou no Git continua
lá depois do commit que removeu — se vazou, o certo é rotacionar, não
apagar. Peça ou ferramenta sensível não vai para lá, e isso se avisa
**antes** de subir.

## Histórico

- **22/08/2026** — repositório criado, Pages ligado, índice no ar. Decidido: um acervo só para todas as frentes; `noindex` em tudo.
- **23/08/2026** — três sessões colidiram no `index.html`: um push de cópia local apagou dois registros e regrediu uma contagem de pranchas. Recuperado pelo Git. Nasceram a regra "nunca reescrever de cópia local" e o detector de órfã na página. O arquivo ganhou o bloco "sistema visual" (`tipo`, `sub`).
- **25/08/2026** — todas as peças ganharam `modulos/ms-voltar.js`.
- **26/08/2026** — testado: `raw`/`blob` de repositório privado devolvem 404 sem sessão de navegador.
- **29/08/2026** — duas frentes sobrescreveram trabalho uma da outra três vezes num dia. Nasceu "Duas sessões, um repositório".
- **02/09/2026** — auditoria: `casa-ittb`, `tokyo-centro` e `casa-tavares` eram peças de cliente em repositório público; foram para `/cliente/` do site, histórico reescrito, guarda `guarda-publico.py` criada. `robots.txt` do site deixou de listar `/cliente/`. Peça fora do público deixou de ser registrada no `index.html`. Runbook `PUBLICAR-APRESENTACOES.md` fundido neste; regra de versão × revisão decidida.
