# gabarito `earth-3d` · visor fotorrealista — ⚠ EM PROVA, NÃO VIGENTE

**Status mudou em 10/09/2026.** Até então era protótipo de gaveta, com a nota
"não usar em peça de cliente". Foi usado numa peça de cliente pela primeira
vez nessa data, por decisão do Michel, e **ainda não voltou conferido por
ele** — enquanto não voltar, não é vigente e não se propõe sozinho: quem
quiser usar pergunta antes. O vigente para localização continua sendo
`mapa-localizacao.md`, ao lado.

Duas coisas quebraram nessa primeira vez, e as duas estão resolvidas no
sistema. Quem for repetir precisa das duas — detalhe na seção "A chave",
adiante:

1. **a chave tem de ficar embutida na peça.** O `<script src="../modulos/
   ms-maps-chave.js">` do esqueleto não resolve fora do acervo; o `montar.py`
   passou a inserir o conteúdo do módulo no lugar da tag. Sem isso o slide
   abre com "Sem chave da Maps Platform"
2. **a varredura de segredos do Netlify barra o build.** Ela reconhece o
   padrão `AIza…` no que vai ao ar e sai com código 2, sem publicar. É falso
   positivo — chave de Maps é pública por natureza —, e a isenção está posta
   no `netlify.toml` do site

Módulo que roda sozinho: `../../modulos/mapa-earth-3d.html`.

---

## O que é

O mesmo slide de localização — sangria total, scrim, véu, rótulo em caixa
translúcida —, mas com a malha fotorrealista do Google Earth no lugar do
satélite chapado. Tilt, heading e órbita em torno do lote. É a mesma base de
dados do Earth, servida pela Maps JavaScript API como `<gmp-map-3d>`.

Vale onde o entorno construído é o argumento: gabarito de vizinhos, insolação
aparente, a leitura da esquina. Não vale como base de implantação — a malha é
fotogrametria, não levantamento.

## Por que não é vigente — três motivos, nesta ordem

1. **Está em preview, no canal `v=beta`.** Sem SLA, com API que pode mudar sem
   aviso. Peça de cliente não se apoia em beta de terceiro. Um deck que abriu
   ontem pode não abrir na reunião.
2. **Exige chave da Maps Platform com billing ativo.** Resolvido pela decisão
   de 30/08 — ver *A chave*, abaixo —, mas segue sendo uma dependência de
   conta que a peça 2D não tem.
3. **Depende de rede boa.** O satélite 2D degrada mal; a malha 3D degrada pior,
   porque carrega em blocos e a sala assiste. Sem rede, tela de estado — que é
   o comportamento correto, e o motivo de o endereço continuar escrito no
   `lead`.

---

## ⚑ PEÇA DE LINK, NUNCA PEÇA DE ARQUIVO

**A Maps JavaScript API recusa página aberta do disco (`file://`).** Um deck
com este gabarito, mandado como `.html` por e-mail ou WhatsApp, abre com o
slide de localização morto — na máquina do cliente e na do Michel. Não há
contorno: não é restrição de chave, é a origem da página.

Decidido em 30/08/2026: **apresentação se entrega por link**, publicada no
acervo. É como o Michel já trabalha, então o gabarito é utilizável. Mas a
regra tem de ser dita a cada peça nova que use 3D:

- **serve:** link do acervo, do Netlify, ou de qualquer domínio cadastrado
- **não serve:** arquivo enviado ao cliente, pen drive, pasta compartilhada,
  duplo clique no `.html`
- **reunião sem rede:** este gabarito não entra. Fica o `mapa-localizacao`,
  que roda do disco, ou um vídeo de órbita do Earth Studio

Quem abre o link **não precisa de nada** — nem chave, nem conta, nem
permissão. Qualquer pessoa, em qualquer computador, navega no 3D. A
restrição vale para o *endereço da página*, não para quem está na frente dela.

---

## De onde saem `lat` e `lng` — a ordem, e ela não se pula

Decisão do Michel, 10/09/2026. **A sessão não inventa coordenada e não pede o
que já está registrado.** Antes de escrever o slide, nesta ordem:

1. **Procurar no Notion.** Na página do projeto, base *Projetos — <frente>*, e
   **nesta ordem**: o campo **`Coordenada`**, que o Michel preenche com o ponto
   que a peça deve mostrar (`lat, lng` em texto), e só depois o campo de
   endereço (`place:Endereço:latitude` / `longitude`), que é a localização
   postal. Uma consulta, e normalmente acaba aqui.
2. **Não achou? Perguntar ao Michel.** Uma linha, direta, dizendo que a página
   do projeto no Notion não tem o endereço preenchido.
3. **Ele não respondeu? Deduzir do material que existe** — KML do levantamento,
   GeoTIFF georreferenciado, matrícula, endereço escrito em documento do
   projeto — e **dizer de onde veio e com que precisão**. Coordenada deduzida
   entra marcada, nunca como fato confirmado.
4. Achando a coordenada fora do Notion, **gravar no Notion**: da próxima vez o
   passo 1 resolve.

⚑ **A coordenada do endereço não é a coordenada do slide.** O campo de endereço
do Notion costuma cair na portaria, no acesso ou no centro do CEP — e o visor
3D tem de abrir sobre o que está sendo apresentado. Na Fazenda Lageado a
diferença medida foi de ~1,6 km: o endereço registrado é
−22,8587 / −48,4351 (portaria do câmpus) e o núcleo histórico, pelo KML da
ortofoto, está em −22,8441 / −48,4271.

**A regra que resolve isso:** `lat`/`lng` recebem o **centroide do que a peça
mostra** — quando houver levantamento georreferenciado, o dele; o `lead` recebe
o **endereço por extenso do Notion**. Os dois campos, as duas fontes, cada uma
no seu lugar. Sem levantamento, a coordenada do Notion serve, e o orbital é
conferido antes de publicar.

## Coordenada de CADA edificação — a prancha planialtimétrica resolve

Para o pino de um lote só, a coordenada do Notion basta. Para **um pino por
edificação** — o que o gabarito permite pelo campo `anot` — é preciso uma
coordenada por prédio, e ninguém tem isso digitado em lugar nenhum.

A rota que funcionou em 11/09/2026, e leva minutos:

1. **Pegar a prancha planialtimétrica cadastral em PDF vetorial.** Todo
   levantamento topográfico entrega uma. Ela traz **malha de coordenadas
   rotulada** nas bordas (`E=…`, `N=…`) e a nota do sistema — tipicamente
   *SIRGAS 2000 / UTM*.
2. **Rasterizar** (`pdftoppm -r 100` para achar as linhas, `-r 400` para ler os
   rótulos) e **detectar a malha**: linhas que atravessam a folha inteira.
   `numpy`: fração de tinta por coluna e por linha acima de ~0,75.
3. **Ler dois rótulos por eixo** — recorte ampliado, o texto é vertical
   (`rotate(-90)`). Dois, não um: o segundo confere o espaçamento. Numa folha
   A1 a 1:500 a célula costuma dar 50 m.
4. **Montar a transformação** pixel → E,N e converter com `pyproj`.
5. **Marcar e conferir por iteração**: desenhar uma cruz na coordenada
   estimada sobre a própria prancha, olhar, corrigir. Duas rodadas bastam para
   cravar cada prédio dentro da sua pegada.

⚑ **A zona UTM é onde se erra, e o erro é silencioso.** Trocar 22S por 23S
desloca 6° em longitude — a latitude continua certinha, o que dá uma falsa
sensação de acerto. **A prova é cruzada:** o centroide dos pontos convertidos
tem de bater com a coordenada que o Michel gravou no Notion. Bateu na sexta
casa de latitude e a longitude ficou 6° fora: era a zona.

⚑ **Nome de edificação vem do Notion, não da prancha** — base *Lista de
desenhos* da página do projeto, que tem a numeração e o nome. Os croquis de
nomenclatura do levantamento (quando existem, no acervo da topografia) mostram
a subdivisão sobre satélite e são o que amarra número a prédio.

## A chave

**Decisão de 30/08/2026, tomada pelo Michel, que muda a regra do acervo.**

Uma chave de Maps é sempre legível por quem abre a página — é assim que a
API funciona, e nenhum arranjo esconde isso. O que a protege não é sigilo, é
**restrição por referrer**: a chave só roda a partir dos domínios cadastrados.
A regra geral do acervo (`chave de API não entra no repositório público`) foi
escrita para chave de servidor, que é segredo de verdade. **Para chave de Maps
restrita por domínio, abre-se exceção** — e esta é a única.

A chave mora em **um arquivo só**, `modulos/ms-maps-chave.js`, e as peças o
carregam. Trocar a chave é editar um arquivo, não vinte decks.

Domínios cadastrados na chave:

```
https://steinvalente-dev.github.io/*
https://michel-stein.netlify.app/*
http://localhost:*/*
```

**Domínio novo, chave nova de configuração.** Um repositório da Sarasá, ou de
qualquer outra frente que venha a existir, precisa entrar nessa lista *antes*
de a peça ir ao ar — senão o slide abre com `RefererNotAllowed` na frente do
cliente. É o item que mais vai ser esquecido.

A chave em uso é a `Maps API Key`, criada em 15/05/2024 e restrita por domínio
em 30/08/2026. Restrição de API: só `Maps JavaScript API` — verificada por
dentro, a `ElevationService` responde `REQUEST_DENIED` com ela.

**Teto de uso, posto em 30/08/2026:** `3D Map loads per day` = **1.000**, em
Quotas → Maps JavaScript API. Vinha `Unlimited`. É o que torna a chave em
página pública tranquila: se vazar, para sozinho no dia seguinte em vez de
rodar o mês na conta do Michel.

Régua para julgar o número: uma tarde inteira de testes e verificação deu
**nove** carregamentos. Mil por dia é folga de duas ordens de grandeza.

Se a peça bater no teto, o mapa simplesmente não abre. Antes de subir o
número, olhar **Metrics**: pode ser sucesso legítimo, pode ser vazamento.

**Ensaio local roda na porta 8765**, que é a cadastrada. Outra porta exige
cadastrar outra porta no console.

Aqui, no contêiner, `npx --yes http-server -p 8765 -c-1` na pasta da peça.

**Na máquina do Michel, não.** Ela não tem Node *nem* Python — confirmado em
10/09/2026, quando `npx` voltou "não é reconhecido". Lá o ensaio é
`ferramentas/servir-local/servir.ps1`, PowerShell puro, copiado para a pasta
da peça:

```
powershell -ExecutionPolicy Bypass -File servir.ps1
```

**A localização continua fora do repositório de método.** Coordenada de
projeto entra na peça do projeto, não no módulo nem no gabarito.

## `compacto` — quando o endereço sai da tela

Campo booleano do slide, 11/09/2026, pedido do Michel: *"elimine o endereço.
Vamos deixar onde a fazenda está. Embaixo você pode deixar aquele texto
pequeno… essa caixa toda fica um pouco mais compacta no canto esquerdo
inferior"*.

Duas coisas, e são independentes: **tirar o `lead` do deck.json** apaga o
endereço; **`compacto:true`** aperta largura, respiro e corpo do `h2`, e a
caixa vira etiqueta. Com anotação dentro da malha o endereço na caixa vira
repetição — os nomes já estão sobre os telhados.

Vale também no `modelo-3d`, que divide o CSS do rótulo.

## No DECK, se um dia virar vigente

```js
{ g:'earth-3d', num:'01', lbl:'localização', inv:true,
  lat:-23.5505, lng:-46.6333,
  kick:'cidade, uf · o olho do slide',
  h2:'onde o terreno está',
  lead:'rua, número · bairro.',
  cap:'Clique para navegar no 3d · o botão devolve o teclado ao slide.' },
```

A chave **não** é campo do DECK: vem de `modulos/ms-maps-chave.js`, carregado
uma vez pela peça.

| campo | o que é |
|---|---|
| `lat` `lng` | o ponto. Botão direito no Google Maps copia os dois |
| `kick` `h2` `lead` `cap` | idênticos ao `mapa-localizacao` |
| `inv:true` | inverte o chrome; a malha 3D é escura como o satélite |

## O enquadramento da casa

Travado no módulo, em `CAM`, para os slides de localização não parecerem cada
um de um projeto:

```js
var CAM = { alt:760, range:600, tilt:58, heading:30, tiltEntrada:45 };
var DEGRAUS = [6000, 2500, 1200];   // a aproximação, ~13 s no total
```

Calibrado sobre a Vila Madalena em 30/08/2026. `range` abaixo de ~250 entra na
malha e mostra a costura da fotogrametria; `tilt` acima de ~72 deita o
horizonte e o scrim perde a função.

**A câmera não nasce no enquadramento final — ela chega nele.** Ver a próxima
seção: não é enfeite, é o que faz o slide desenhar alguma coisa.

## A aproximação — a armadilha que custou a tarde

**Criar o visor já com o `range` final devolve tela azul lisa, sem erro
nenhum.** O motor ainda não tem a malha daquele pedaço e a câmera nasce dentro
do chão. Os tiles chegam — todos `200` na aba de rede —, mas não há o que
desenhar na frente da lente.

A cura é chegar de longe: entrar **muito** largo — 6 km, não 2 —, onde a malha
grossa já existe, e fechar em degraus de 3 s. Cada degrau dá ao motor tempo de puxar o nível
seguinte e reconciliar a altitude do terreno — dá para ver ele reescrevendo
`center.altitude` sozinho no caminho.

Isso também explica por que o ensaio de manhã funcionou: eu tinha mexido no
`range` na mão, de 900 para 700 para 320, sem perceber que a sequência *era* a
solução. Publicado direto no enquadramento final, o mesmo código não desenhava
nada.

De quebra, a peça abre com um mergulho, que é melhor do que aparecer pronta.

**Não há evento de "terminei".** `gmp-steadychange` não dispara nesta versão do
preview — testado em 30/08, zero eventos em sete segundos. Por isso a espera é
por relógio, e é generosa: declarar pronto cedo demais mostra a geometria bruta,
aqueles prismas cinza que parecem erro de render e são só nível de detalhe baixo.

**O tempo de montagem é o calcanhar deste gabarito.** Em máquina boa e rede de
escritório, a malha fina de um bairro levou de dez segundos a alguns minutos,
sem padrão claro e sem nada no console. É instabilidade de produto em preview, e
é o argumento mais forte para ele continuar fora de peça de cliente.

**O modo é `SATELLITE`, não `HYBRID`.** O híbrido cobre a cidade de pinos de
restaurante e rótulos de rua — numa peça de arquitetura, só atrapalham.

## A copy da tela de carga

O `<b>` diz **`carregando localização`**, não `carregando a malha 3d` — regra
de motor desde 04/09/2026, em `DECK-MOTOR.md`, e a mesma na variante 2D. A
espera é longa neste gabarito; a frase que a acompanha tem de ser da língua da
sala. O rótulo de passo abaixo (`aproximando · 2 de 4`, `assentando a malha`)
descreve o degrau real e fica como está.

---

## A trava de teclado

Mesma mecânica do mapa vigente e do visor 3D: o visor rouba as setas e a
navegação do deck para. Ativação por clique no `.veu`, botão `.sair` **fora**
do visor. Ao soldar num deck, acrescentar `.g-earth` aos três pontos da engine:

- `desativaModelo()` varre `.g-modelo,.g-mapa` → acrescentar `.g-earth`
- o clique do palco ignora `.g-mapa .visor` → acrescentar `.g-earth .visor`
- o `go()` monta o visor ao **chegar** no slide. Montar na carga baixa dezenas
  de MB de malha antes da primeira prancha

## Armadilhas

**Quatro coisas diferentes dão a MESMA tela azul lisa, sem erro:** altitude
errada, `range` final sem aproximação, câmera sob a superfície e — de longe —
o globo visto do espaço. Diante de tela azul, checar nesta ordem: a altitude,
depois a aproximação. O console não ajuda em nenhuma das duas.

**A altitude é acima do NÍVEL DO MAR, não altura de voo.** É a pior das
armadilhas, porque falha em silêncio. São Paulo está a ~760 m: pôr `alt:180`
— que parece um valor razoável de altura de câmera — nasce a câmera seiscentos
metros abaixo do solo, e a tela fica **azul lisa, sem um erro sequer no
console**. Confirmado no ensaio de 30/08. Litoral ~10, planalto gaúcho ~800.
A Elevation API resolveria sozinha, mas está — corretamente — fora da
restrição da chave, e ativá-la só para isso amplia a superfície à toa. Por
isso a altitude é campo, não constante.

**O loader do Google só pode entrar uma vez na página.** Injetar o script
duas vezes — clicar CARREGAR enquanto a primeira carga está no ar — quebra por
dentro com `Cannot read properties of undefined (reading 'keys')`, um erro que
não diz uma palavra sobre a causa. A promessa do loader é memoizada e o botão
trava durante a carga. Encontrado no uso real, 30/08.

**O menu do Google Maps oferece Plus Code antes da coordenada.** `C8R5+77
Pinheiros` não é lat,lng, e converter exigiria a Geocoding API — fora da
restrição da chave, de propósito. O módulo reconhece o formato e diz onde
achar a coordenada de verdade, em vez de cair no ponto padrão em silêncio.

**Chave ruim não rejeita: ela desenha o erro e grita no console.** A promise da
API resolve normalmente. Sem uma janela de verificação do console, chave
inválida vira tela preta muda no meio da reunião. O módulo espia
`console.error` e traduz `BillingNotEnabled`, `ApiNotActivated`,
`RefererNotAllowed` e `InvalidKey` em texto na tela.

**Billing ativo é obrigatório mesmo estando em preview e sem cobrança.** É o
erro mais comum e o menos óbvio.

**Restringir a chave por referrer antes de publicar qualquer coisa.** Chave
solta em HTML público é cota de terceiro rodando na conta do Michel.

**`flyCameraAround` é do beta.** Se sumir, o fallback empurra o `heading` num
`setInterval` — mais duro, mas não quebra a peça.

**A biblioteca é `MapMode`, não `Map3DMode`.** A documentação de terceiros
erra isso com frequência. Confirmado na `importLibrary('maps3d')`, que devolve
`Map3DElement`, `MapMode`, `AltitudeMode`, os marcadores e polígonos 3D.
`flyCameraAround`, `flyCameraTo` e `stopCameraAnimation` existem e funcionam.

**Validado em navegador em 30/08/2026**, na Vila Madalena, com chave restrita
por API à `Maps JavaScript API`. A restrição foi verificada por dentro: a
`ElevationService` responde `REQUEST_DENIED` com a mesma chave, que é a prova
de que a restrição faz o que promete.

---

## Se for promovido a vigente

O que tem de acontecer antes, nesta ordem: `gmp-map-3d` sair de preview para
GA · uma chave restrita por referrer criada e documentada em `CREDENCIAIS.md` ·
um teste em rede de cliente, não de escritório · e a decisão de o que aparece
quando a rede cai.
