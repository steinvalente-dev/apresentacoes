# Pacote `sarasa-sobre` — três slides de abertura, prontos

Os três slides institucionais do Estúdio Sarasá, para entrar **em bloco** no
começo de qualquer peça da frente. Não se remonta nada: o pacote traz o JSON e
as imagens-fonte.

```
pacotes/sarasa-sobre/
  sobre.json     os 3 slides, no formato do array `deck`
  img/           as 33 imagens-fonte (13 MB) — mosaico + faixa de obras
  LEIA-ME.md     este arquivo
```

## Os três

| # | gabarito | o que é |
|---|----------|---------|
| 1 | `meia` + `mosaico` + `inst` | **setenta anos de ofício** — linha do tempo 1939→2022 sobre um mosaico de 23 obras em movimento. Traz o botão "visite o nosso site". |
| 2 | `meia` + `espelho` | **serviços** — as cinco frentes, com faixa de 10 obras legendadas. |
| 3 | `viva` | **onde atuamos** — o mapa de atuação interativo, por `<iframe>` (`modulos/mapa-atuacao-sarasa.html`). |

O slide 1 leva `"atalho": "sobre a Sarasá"`, que é o que põe a primeira bolinha
da navegação como link permanente para o institucional. Mantenha.

## Como inserir

1. Copiar o array `deck` de `sobre.json` para o **começo** do array `deck` da
   peça. A ordem importa: o mapa fecha o bloco.
2. Nada mais. Os caminhos de imagem já apontam para este pacote
   (`pacotes/sarasa-sobre/img/…`) e o `montar` resolve sozinho.
3. `montar` → `validar` → `montar-indice` → `guarda-publico.py` → push, como
   sempre.

**Caminho que começa por `pacotes/` resolve da raiz do clone**, não da pasta de
fontes da peça — é a única exceção do `montar`, feita para isto (`acha()` em
`sistemas/montar.py`). Vale qualquer que seja o `--img` da peça, e o arquivo
gerado em `img/` continua com o mesmo nome de sempre.

## O que muda de peça para peça

- **Nada é obrigatório mudar.** O bloco é institucional, não fala do projeto.
- O botão do slide 1 aponta para `estudiosarasa.com.br`. Peça de cliente que
  não deva sair do deck: tirar o `botao`.
- O slide 3 depende do módulo publicado. Em ensaio local, servir a raiz do
  clone (`python3 -m http.server`) — caminho relativo, não `file://`.

## Marca

A Sarasá ainda não tem marca escrita. As peças saem com `--marca sarasa`, que
hoje é empréstimo de `michel stein_` com a assinatura trocada. Ver
`marca/MARCA-SARASA.md`.

## Primeiro consumidor

`centro-tea-butanta/deck.json` — os índices 0, 1 e 2 são exatamente este
pacote. Serve de referência viva: divergiu, o `sobre.json` é o mestre.
