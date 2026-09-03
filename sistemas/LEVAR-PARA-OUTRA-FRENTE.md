# levar o sistema para outra frente

Documento de método, sem dado de cliente, no repositório público. Abre por URL
raw, sem token e sem terminal:
`https://raw.githubusercontent.com/steinvalente-dev/apresentacoes/main/sistemas/LEVAR-PARA-OUTRA-FRENTE.md`

**Para que serve:** o sistema de apresentações foi construído no Projeto *Solo —
MS*, em 29/08/2026. Ele não é da michel stein_ — é um motor que recebe uma marca.
Este arquivo é o que uma conversa de **outra frente** (Lavrō, AMAZ, Sarasá,
Baraka) precisa ler para usar o mesmo sistema, e o que precisa mudar nas
instruções daquele Projeto.

---

## 1 · O acervo

Uma página, quatro abas: **steinvalente-dev.github.io/apresentacoes**

| aba | o que guarda |
|---|---|
| **arquivo** | as peças publicadas, por projeto |
| **deck** | como se monta uma apresentação — motor, gabaritos, esqueleto |
| **marca** | as identidades, uma por frente |
| **sistema** | as demais regras: site, arquivamento, publicação, Notion, proposta |

Cada linha vem marcada **público** ou **privado**. A regra que separa: nome de
cliente, endereço de obra, honorário ou caminho interno → privado. O resto →
público, porque a URL raw abre sem token e sem terminal, e aí **qualquer conversa
alcança a regra** — inclusive as que não são Cowork.

---

## 2 · As três camadas

Confundi-las é o que impedia trocar de marca.

| camada | o que é | onde |
|---|---|---|
| **motor** | gabaritos, quadro fixo, revelação por clique, chrome, validação. **Não sabe de que marca é a peça** | `sistemas/DECK-MONTAR.md` |
| **marca** | cor, tipografia, assinatura, capa, contracapa | `marca/MARCA-<nome>.md` |
| **peça** | o array `DECK` de uma apresentação | o HTML da peça |

**Montar uma apresentação = motor + uma marca + um DECK.**

O que uma sessão lê para montar (corrigido 02.09.2026 — antes dizia "este
arquivo e mais nada", e foi isso que fez a primeira peça sair errada):

    .../apresentacoes/main/sistemas/DECK-MONTAR.md
    .../apresentacoes/main/marca/MARCA-<a sua>.md
    o módulo de capa da frente, em modulos/
    a peça de referência, ABERTA antes de montar: emei-presidente-dutra

Gabarito com máquina própria — mapa, render em tela cheia, prancha de
referência, visor 3D, popover, isométrico — tem arquivo próprio em
`sistemas/gabaritos/`, lido **só quando aquele gabarito entra na peça**.
`sistemas/DECK-MOTOR.md` é referência de fundo, para quando algo quebrar. **Não
é leitura de rotina.**

---

## 3 · A receita

1. Abrir `esqueleto/deck-esqueleto.html`. **Não partir do HTML de outra peça** —
   vem com a marca e o conteúdo dela junto.
2. Colar as `@font-face` do bloco da marca — **seis** na michel stein_ e na
   AMAZ, **quatro** na Sarasá (corrigido 02.09.2026).
3. Trocar as cores do `:root` pelo bloco da marca, **e varrer os hexes escritos
   à mão pelo CSS** — trocar o `:root` não basta. As linhas de escala não se
   tocam.
4. Pôr a **capa do módulo da frente** e a contracapa nas pontas do `DECK`. O
   logotipo do canto superior direito vem configurado no bloco da marca: texto
   nas outras frentes, logotipo na Sarasá.
5. Escrever o miolo do `DECK`.
6. Rodar o laço de verificação antes de entregar, e a varredura de transbordo em
   sete proporções (`DECK-MONTAR.md`, "Antes de entregar"):

```js
for(let i=0;i<DECK.length;i++){ try{ tpl(DECK[i]) }catch(e){ console.log(i, DECK[i].g, e.message) } }
```

**A engine abaixo do `DECK` não se toca.**

---

## 4 · Onde a sua frente está

| frente | marca | o que falta |
|---|---|---|
| **michel stein_** | `marca/MARCA-MICHEL-STEIN.md` + `michel-stein/bloco.html` | nada — é o padrão do esqueleto |
| **AMAZ** | `marca/MARCA-AMAZ.md` + `amaz/bloco.html` | levantada do que está publicado: paleta e tipografia completas. **Faltam abertura, contracapa, acervo do fundo e "o que é intocável"** |
| **Lavrō** | `marca/MARCA-LAVRO.md` + `lavro/bloco.html` | (corrigido 02.09.2026 — antes: "não existe ainda") ver as lacunas no próprio arquivo |
| **Estúdio Sarasá** | `marca/MARCA-SARASA.md` + `sarasa/bloco.html`, peça publicada: `emei-presidente-dutra` | (corrigido 02.09.2026 — antes: "não existe, não inventar") lacunas nomeadas no §8 do arquivo |
| **Baraka** | não existe | **não inventar paleta.** Levantar a identidade antes |

O checklist de sete itens para criar um `MARCA-<nome>.md` está no fim do
`marca/MARCA-MICHEL-STEIN.md`.

---

## 5 · O que pedir na conversa daquela frente

1. **Ler** o `DECK-MONTAR.md` e a marca correspondente pelas URLs acima.
2. **Auditar as instruções do Projeto**: o que ali ainda manda ler arquivo que
   mudou de nome, o que duplica o que já está no acervo, e o que pode encolher.
   As da michel stein_ foram de ~1.400 para ~600 palavras.
3. **Devolver a versão curta** para o Michel colar nas configurações.
4. Se a frente ainda não tem marca escrita, **levantar o que existe** — de peça
   publicada, de manual, de arquivo de projeto — e propor o `MARCA-<nome>.md`.
   Levantar, não inventar.

---

## 6 · O que ainda não funciona — dizer, não descobrir na hora

- **`planta` e `desenho` não estão no esqueleto.** Dependem da máquina da lupa.
  Planta e corte entram como `prancha` de uma coluna, sem zoom.
- **O mapa de lotes exige o objeto `MAP`** levantado do cadastro. Sem ele o slide
  vira estado vazio. O mapa de **localização** só precisa da URL do embed.
- **O esqueleto nasceu de um deck comercial.** O vocabulário de gabaritos reflete
  isso; cada tipo de argumento criou o seu.
- **Publicar exige a ferramenta Bash e o token do repositório.** O token mora em
  `CREDENCIAIS.md`, nos documentos do Projeto *Solo — MS*. **Uma conversa de
  outro Projeto não o alcança** — ou o Michel copia o `CREDENCIAIS.md` para lá,
  ou a publicação continua acontecendo pelo Projeto dele. Dizer isso de cara, em
  vez de tentar e falhar no fim.

---

## 7 · A regra que não muda

Peça publicada vai para `apresentacoes/<slug>/apresentacao.html`, **mais o
registro no `index.html` na mesma rodada** — subir sem registrar não conta como
subir. Toda peça leva a linha do `ms-voltar.js` antes do `</body>`. O link que se
devolve é o da peça, nunca o do índice.

Runbook completo: `sistemas/GITHUB-COMO-TRABALHAR.md`, ao lado.
