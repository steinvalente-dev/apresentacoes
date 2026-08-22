# módulos da prancha

As peças de montar. Cada módulo é um arquivo que roda sozinho no navegador e
pode ser soldado num deck sem reescrever nada.

**Sem número de revisão.** O arquivo é o vigente; o anterior está no histórico
do Git. Nunca criar `-R2` ao lado.

| módulo | o que faz | como entra num deck |
|---|---|---|
| `capa-morph.html` | a capa padrão: marca, papel, slogan e site sobre o carrossel morph, em oliva | receita de extração em `../PRANCHA-CAPA.md` |
| `fundo-morph-pontilhado.html` | o laboratório do fundo, com todos os controles. **Não é a capa** — serve para calibrar e copiar o preset | não entra; é banco de ensaio |
| `ms-fundo-engine.js` | a engine do morph isolada, ~13 KB | `<script>` no fim do `<body>` + `MSFundo.montar()` |

## Ao criar um módulo novo

Um módulo entra aqui quando resolve **um** problema de prancha de forma
reaproveitável — um mapa, um visor 3D, uma linha do tempo, um comparador
antes/depois. Três exigências:

1. **Roda sozinho.** Abrir o arquivo no navegador tem de mostrar o módulo
   funcionando, sem servidor e sem dependência de CDN.
2. **Tem receita de solda.** Uma seção dizendo o que copiar, onde encaixar e o
   que ele espera do deck — como a que existe no `PRANCHA-CAPA.md`.
3. **Entra nesta tabela**, com uma linha só.

Módulo que precisa de documentação longa ganha um `.md` próprio na pasta acima,
ao lado do `PRANCHA-CAPA.md`.
