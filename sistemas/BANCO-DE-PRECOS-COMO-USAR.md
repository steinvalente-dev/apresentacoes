# Banco de preços de obra — como usar

Método. Sem dado de cliente, sem honorário, sem endereço. Abre por URL raw, sem token
e sem terminal, de qualquer frente.

O que tem nome de cliente, valor de proposta ou achado comercial mora no repositório
privado `michel-stein-sistemas`, em `notion/BANCO-DE-PRECOS.md` — e exige Bash e token.

---

## A regra que não se quebra

**Existe UMA base de preços de obra**, no Dashboard pessoal do Michel, no Notion.
Ela não é de projeto nenhum: todas as frentes consultam e alimentam a mesma.

**Nunca criar base paralela "para este projeto".** O que separa os mundos é o campo
`Natureza da obra`, nunca uma tabela nova. Base fragmentada é banco morto — o valor
está em poder comparar o unitário de restauro com o de obra comum.

Há uma base irmã, de **propostas comerciais**, com grão diferente: lá uma linha é uma
proposta inteira; aqui uma linha é um serviço. As duas se ligam por relation.

Os IDs das duas bases estão nas instruções do Projeto, não aqui.

---

## Schema da base de obras

| campo | tipo | observação |
|---|---|---|
| `Código` | título | código da tabela pública como veio; código local recebe prefixo do projeto |
| `Descrição` | texto | |
| `Unidade` | select | cj · h · kg · m · m² · m³ · mês · un · vb · L · cento · viagem · mxmês · unxmês · mêsxm² · m³xkm · kgxmês · un/mês · cjxmês · CHI · CHP |
| `Preço` | número | **custo direto, sem BDI** |
| `Categoria` | select | 23 opções, de Acessibilidade a Vidros e vitrais |
| `Fonte` | select | SINAPI · CPOS · CDHU · EDIF · EMOP · SIURB · SBC · ORSE · FDE · Mercado · Fornecedor · Construtora · Projetista · Composição própria |
| `Origem do preço` | select | Tabela referencial · Composição própria · Preço informado · Verba estimada · Cotação formal |
| `Natureza da obra` | multi-select | Restauro e patrimônio · Retrofit · Obra comum · Instalações · Museografia · Restauro de bem móvel |
| `Data-base` | data | mês de referência do preço |
| `Fator p/ hoje` | número | INCC-DI acumulado até a referência corrente |
| `Preço atualizado` | fórmula | **é esta coluna que se lê, nunca o preço cru** |
| `Projeto de origem` | select | de onde a linha veio |
| `Observações` | texto | ressalvas, divergências, o que é leitura e não fato |

---

## Atualização pelo INCC-DI

Série **192** do SGS do BACEN, aberta, sem token:

    https://api.bcb.gov.br/dados/serie/bcdata.sgs.192/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2026

Devolve a variação mensal em %. O fator de um preço de mês M até a referência
corrente é o produto de `(1 + variação)` de **todos os meses posteriores a M**.
Referência corrente da base: **agosto de 2026** — meses iguais ou posteriores têm
fator 1,0.

A leitura correta é sempre `Preço atualizado`. Comparar preço cru de anos diferentes
não diz nada.

---

## Regras de carga

1. **Ler o manual privado antes de carregar.** Ele tem as armadilhas já encontradas
   nos arquivos de origem; sem ele, repete-se erro já pago.
2. **Data-base vem de dentro do documento, nunca do nome do arquivo.** Sem data-base
   declarada, a linha não sobe — salvo autorização explícita do Michel, caso a caso,
   e então a presunção vai **escrita na própria linha**, com a palavra PRESUMIDA.
3. **Perguntar a natureza da obra por fonte.** Não deduzir do nome do arquivo.
4. **Nunca carregar coluna de preço com BDI embutido.** A base é custo direto. Planilha
   que traz `PREÇO UNITÁRIO = custo × (1 + BDI)` tem que ser desfeita antes, ou a
   linha entra inflada e contamina toda comparação futura.
5. **Idempotência.** Chave `(Código, Descrição[:160], Preço)`. Ler a base inteira antes
   de criar qualquer linha; recarga é rotina, duplicata não.
6. **Código local recebe prefixo do projeto.** Código de tabela pública fica como veio,
   para cruzar com a tabela de origem depois.
7. **Antes de inventar área, abrir o cabeçalho da planilha orçamentária.** O
   quantitativo costuma estar lá, no canto superior direito da aba principal, ou numa
   aba `QUANT-*` / `MEMÓRIA DE CÁLCULO`. Medido vale mais que estimado.
8. **Mostrar o resultado agrupado antes de carregar**, com o que ficou sem data-base
   separado à parte.

Carga em lote usa a API REST do Notion e exige o token de integração, que mora no
documento de credenciais do Projeto. Leitura e escrita pontual funcionam pelo conector
do Notion, sem token. Uma base só responde ao token depois de ser conectada à
integração: abrir a base → `•••` → Conexões.

---

## Dois testes de qualidade, antes de confiar num unitário

### ① Redondo ou quebrado

Numa planilha fechada por valor-alvo, o orçamentista calibra uma variável até o total
bater. Os unitários que ele **digitou** continuam redondos; os que o cálculo
**devolveu** vêm com centavo quebrado.

> **valor redondo = entrada real · centavo quebrado = resíduo de retro-cálculo**

Carregar os redondos e deixar os quebrados de fora preserva o que é levantamento e
descarta o que é aritmética reversa. É o teste mais barato que existe.

### ② Total suspeito de teto

Se o custo direto ou o total com BDI cair exatamente sobre um número redondo —
R$ 1,0 milhão, R$ 4,0 milhões, R$ 5,0 milhões — ou se o BDI tiver muitas casas
decimais quebradas, a planilha foi ajustada a um teto. **Unitário de planilha ajustada
a teto não é levantamento de preço.** Pode entrar na base, mas com a ressalva escrita
na linha, e nunca como referência isolada.

### ③ E uma terceira verificação, de origem

Aba de memória de cálculo copiada entre planilhas é comum. Antes de usar uma memória
para medir, conferir se os ambientes e os códigos descritos são **daquele** imóvel —
template reaproveitado carrega a medição do imóvel anterior, e ninguém percebe.

---

## O que a base ainda não responde

Está no manual privado, na seção de pendências, e muda a cada rodada. Consultar lá
antes de afirmar que a base cobre alguma coisa.
