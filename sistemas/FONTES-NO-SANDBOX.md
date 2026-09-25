# Fontes no sandbox — instalar antes de gerar .docx ou PDF

Documento de método, sem dado de cliente, no repositório público. Abre por URL
raw, sem token e sem terminal:
`https://raw.githubusercontent.com/steinvalente-dev/apresentacoes/main/sistemas/FONTES-NO-SANDBOX.md`

**Vale para as quatro frentes.** Todas usam famílias OFL do repositório
`google/fonts`, e todas caem na mesma armadilha.

---

## Quando isto é necessário — e quando não é

| entregável | precisa instalar? |
|---|---|
| **deck / peça HTML** | **não.** As fontes já vivem em base64 dentro de `marca/<nome>/bloco.html`. É requisito do motor: a peça tem de rodar sem internet |
| **`.docx`, `.pdf`, imagem gerada por script** | **sim.** O gerador lê a fonte instalada no sistema, não o base64 do bloco |

Ou seja: proposta, contrato, memorial e qualquer coisa que saia do Word ou do
LibreOffice depende desta receita. Deck, não.

---

## As famílias, por frente

| frente | famílias | arquivo da marca |
|---|---|---|
| **michel stein_** | DM Mono (400/500, reto e itálico) · Inter | `marca/MARCA-MICHEL-STEIN.md` |
| **AMAZ** | Inter · Bricolage Grotesque *(em aberto no R1)* | `marca/MARCA-AMAZ.md` |
| **Lavrō** | Space Grotesk (600/700) · Inter · Fraunces *(variável)* | `marca/MARCA-LAVRO.md` |
| **Sarasá** | Poppins *(marcada CONFIRMAR)* · Playfair Display, se a serifada entrar | `marca/MARCA-SARASA.md` |

**O arquivo da marca é sempre o mestre.** Esta tabela é atalho e pode
envelhecer — na dúvida, reler a marca.

---

## A receita

O `NO_PROXY` não é opcional: o sandbox intercepta a saída e o download volta
vazio ou errado.

```bash
export NO_PROXY='*' HTTPS_PROXY= https_proxy= http_proxy=
mkdir -p ~/.fonts && cd /tmp

# estáticas — uma por face, do diretório ofl/<familia-minuscula>/
for u in DMMono-Medium DMMono-MediumItalic DMMono-Regular DMMono-Italic; do
  curl -sL --noproxy '*' -O \
    "https://github.com/google/fonts/raw/main/ofl/dmmono/$u.ttf"
done

# variáveis — o nome traz os eixos, entre colchetes codificados
curl -sL --noproxy '*' -o Inter.ttf \
  "https://github.com/google/fonts/raw/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf"

cp *.ttf ~/.fonts/ && fc-cache -f
fc-list | grep -iE "dm mono|inter"     # confere que entraram
```

Para outra família, troca-se o diretório `ofl/<familia>` e o nome do arquivo:
`ofl/spacegrotesk/`, `ofl/fraunces/`, `ofl/poppins/`, `ofl/playfairdisplay/`,
`ofl/bricolagegrotesque/`.

---

## As duas armadilhas

**1 · A URL de download do Google Fonts não serve.**
`fonts.google.com/download?family=<nome>` devolve **o mesmo zip para qualquer
família** dentro do sandbox. Silencioso: o arquivo chega, descompacta, e são as
fontes erradas. Usar sempre o repositório `google/fonts`.

**2 · Fonte variável tem o nome com colchetes codificados.**
`Inter[opsz,wght].ttf` vira `Inter%5Bopsz%2Cwght%5D.ttf` na URL. Sem a
codificação, 404. Vale para Fraunces e qualquer outra variável.

---

## Se a fonte não estiver disponível

Não improvisar substituta. O `fc-list` dizendo que a família não entrou é
motivo para parar e avisar — documento saindo com fonte de sistema no lugar da
fonte da marca é pior do que documento atrasado.

Fallback declarado nos blocos, só para tela: `system-ui, sans-serif`.

---

*Levantado em 25/09/2026, do `ACERVO_como-acessar.md` (Drive, hoje em
`00-OBSOLETOS`), ao aposentar aquele arquivo.*
