# centro-tea-butanta — como remontar

Peça do **Centro de Acolhimento ao Autista (Butantã)**, frente Estúdio Sarasá.

## Remontar

Na raiz do clone de `apresentacoes`:

```
python3 sistemas/montar.py centro-tea-butanta --marca sarasa \
        --deck centro-tea-butanta/deck.json \
        --img  centro-tea-butanta/fonte --sobrescrever
node    sistemas/validar.mjs centro-tea-butanta/apresentacao.html
python3 sistemas/montar-indice.py
python3 sistemas/guarda-publico.py      # tem de imprimir "guarda: limpo"
```

Publicar = push em `main`. O GitHub Pages leva 1–3 min para refletir; conferir
o TAMANHO do arquivo no ar antes de dizer que subiu.

## O que mora aqui

| arquivo | o que é |
|---|---|
| `deck.json` | a fonte da peça — é ele que se edita, nunca o HTML |
| `fonte/` | imagens de origem: carrossel institucional e mapa de atuação |
| `apresentacao.html` | saída do montar; não editar à mão |
| `meta.json` | registro no acervo; escrito pelo montar |

## Duas sessões, uma peça

Esta peça é mantida pela **sessão de produção da apresentação**. A sessão de
projeto/conceito NÃO dá push nela — o token do acervo dá escrita em todas as
peças de todas as frentes, e duas sessões montando o mesmo slug se
sobrescrevem. O estado combinado entre as duas vive no Notion, na entrada
**"Estado da apresentação"** do Diário de bordo — Sarasá.

## Gabaritos próprios desta peça

A abertura institucional usa `meia` com `imgs` + `legs` — pilha de imagens com
legenda, girando a 3,2 s sem reiniciar na troca de slide. Foi acrescentado ao
esqueleto em 30/10/2026; ver os comentários no `deck-esqueleto.html`.
