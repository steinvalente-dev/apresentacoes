# superado — o que saiu de uso, guardado só como registro

**Nada aqui está em uso.** Esta pasta existe para que um arquivo tirado de
circulação não precise ser apagado: fica a cópia, datada e marcada, e o
vigente segue sozinho no lugar dele.

A regra que a justifica é a de sempre — **um arquivo vivo por assunto**. Duas
versões do mesmo manual em duas pastas, ambas parecendo válidas, é como se
perde meia hora descobrindo qual é a boa. Aqui a resposta é imediata: se está
em `superado/`, não vale.

## Como um arquivo entra

1. Copiar para `superado/AAAA-MM-DD-<nome-original>.<ext>` — a data é a de
   saída de uso, não a de criação.
2. **Marcar o arquivo por dentro.** Um `.md` recebe o aviso no topo; um
   `.html` recebe a faixa (o trecho está abaixo) e o `noindex`.
3. Registrar a linha na tabela deste arquivo.
4. Só então substituir o vigente.

Copiar **antes** de substituir, sempre na mesma rodada. Um push que troca o
vigente e esquece a cópia não tem volta barata.

## A faixa, para arquivo HTML

No `<head>`:

```html
<meta name="robots" content="noindex, nofollow, noarchive">
```

Primeiro elemento do `<body>`:

```html
<div style="position:sticky;top:0;z-index:9999;background:#B85C38;color:#EDE6DA;
  font:500 12px/1.5 'Inter',system-ui,sans-serif;letter-spacing:.06em;
  padding:11px 16px;text-align:center">
  ⚠ ARQUIVO SUPERADO — fora de uso desde AAAA-MM-DD. Mantido só como registro.
  O vigente é <b>CAMINHO/DO/VIGENTE</b>.
</div>
```

Terracota de fundo cheio é o único lugar do sistema onde ela cobre área grande.
É deliberado: a faixa tem de brigar com o desenho da peça, senão não cumpre a
função.

## O que **não** vem para cá

- **Versão intermediária de trabalho.** Isso é histórico de commit, e o Git já
  guarda. Aqui entra o que já esteve publicado e valendo.
- **Peça de cliente.** Vai para o repositório do site, em `cliente/`, com as
  regras de lá.
- **Arquivo com nome de cliente, endereço ou honorário.** Este repositório é
  público. Vai para `michel-stein-sistemas`.
- **Rascunho e proposta.** Proposta ainda não foi vigente; mora ao lado do
  arquivo que pretende substituir, numa pasta `proposta/`, e some quando a
  troca acontece — aprovada ou recusada.

## O que está guardado

| arquivo | o que era | saiu de uso | substituído por |
|---|---|---|---|
| _(vazio)_ | | | |
