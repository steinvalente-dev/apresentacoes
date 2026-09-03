# exemplos — um deck.json mínimo por marca

Quatro arquivos, um por frente: `michel-stein.json`, `sarasa.json`, `amaz.json`, `lavro.json`.
Cada um é um deck real de arquitetura, curto e neutro — sem cliente, sem endereço com número,
sem R$ (a guarda pública barra isso). Os gabaritos: `capa sumario divisor frase lista cheia duo tabela fim`;
`cheia` e `duo` com `src` vazio, de propósito: o slot hachurado é o estado "estrutura antes da imagem".

Para montar um: `python3 sistemas/montar.py teste-sarasa --marca sarasa --deck esqueleto/exemplos/sarasa.json`,
depois `node sistemas/validar.mjs teste-sarasa/apresentacao.html`. Os quatro passam no validador inteiro.
**Pasta `teste-*` não fica no repositório** — apagar depois de olhar.

Para uma peça de verdade: copiar o JSON da frente, trocar os textos, apontar as imagens. Formato: `sistemas/DECK-JSON.md`.
