# servir-local · ensaiar a peça num endereço, não no disco

Servidor estático de uma linha, para abrir uma apresentação em
`http://localhost:8765/` na máquina do Michel.

## O problema que ele resolve

**A Maps JavaScript API recusa página aberta do disco.** Peça com o gabarito
`earth-3d` abre em `file://` com o slide 3D vazio e um erro de origem no
console. Só desenha se a página vier de um endereço `http`, e só das origens
cadastradas na chave — a porta **8765** é uma delas. Outra porta exige
cadastrar outra porta no console do Google.

O mesmo vale, em menor grau, para qualquer coisa que dependa de `fetch`,
módulo ES ou `canvas` com imagem externa: `file://` é origem opaca e o
navegador barra.

## Por que PowerShell, e não `npx http-server`

**A máquina do Michel não tem Node nem Python.** Descoberto em 10/09/2026,
quando `npx` voltou *"não é reconhecido como um comando interno ou externo"* —
a ausência de Python já estava registrada, a de Node não.

Isso derruba as duas receitas habituais (`npx --yes http-server -p 8765 -c-1`
e `python -m http.server 8765`). PowerShell vem com o Windows e o
`System.Net.HttpListener` faz o serviço sem instalar nada — nem privilégio de
administrador, porque `localhost` é exceção na reserva de URL do Windows.

⚑ **Consequência mais ampla:** nada que se peça ao Michel rodar na máquina
dele pode pressupor Node, Python, `npm`, `pip` ou gerenciador de pacote. Ou é
PowerShell puro, ou roda aqui e vai pronto para ele.

## Usar

Copiar o `servir.ps1` para a pasta da peça e, de dentro dela:

```
powershell -ExecutionPolicy Bypass -File servir.ps1
```

Depois abrir `http://localhost:8765/apresentacao.html`. `Ctrl+C` para parar.

O `-ExecutionPolicy Bypass` é necessário porque a política padrão do Windows
recusa script não assinado; a forma acima vale só para aquela execução e não
muda a configuração da máquina.

## O que ele faz e o que não faz

Serve a pasta corrente e nada acima dela — caminho que escape da raiz volta
404. Tem tabela de MIME para o que uma peça usa (`html`, `js`, `mjs`, `css`,
`json`, `png`, `jpg`, `webp`, `svg`, `gif`, `woff2`, `woff`, `pdf`); o resto
sai como `application/octet-stream`. Imprime cada pedido, com o código.

Não é servidor de produção: escuta só em `localhost`, atende um pedido por
vez, não faz cache, não faz `Range` e não trata compressão. Peça de 6 MB em
base64 abre em instantes assim mesmo, porque é tudo memória local.

Se a porta estiver ocupada ele avisa e sai — não tenta outra, porque outra
porta não está cadastrada na chave e o 3D não abriria de qualquer jeito.

## Histórico

- **10/09/2026** — nasceu. O ensaio local da peça com `earth-3d` estava
  travado: `file://` não serve, `npx` não existe na máquina, `python` também
  não. Registrado aqui para não se redescobrir a limitação na próxima frente.
