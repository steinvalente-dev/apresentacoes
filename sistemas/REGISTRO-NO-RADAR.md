# Registro no Radar

Vale para todo chat e rotina do assistente, em qualquer projeto.

O Radar é o aplicativo do Michel. Ele mostra num lugar só o que os assistentes
fazem. A fonte é UMA base no Notion, "📡 Diário de bordo do Radar". O endereço da
base está na instrução de cada projeto. Não criar base paralela. Não confundir
com o diário de bordo dos projetos, que é a narrativa de cada projeto.

O chat Radar é o assistente principal: sabe de tudo e gerencia o aplicativo. Os
demais chats (notas fiscais, finanças, os que vierem) são assistentes do
assistente — cuidam da minúcia e reportam pelo diário.

## Uma notificação, um lugar

- **Ação para o Michel** → demanda na base Demandas (estação To-do), item
  clicável. Qualquer assistente pode criar.
- **E-mail** → estação Mail. Se gera ação, a ação vai para o To-do; no Mail o
  e-mail aparece só como origem.
- **O que os assistentes fizeram** → Diário de bordo do Radar. Lá ficam Feito,
  Aguardando (esperando terceiro) e Falhou. Tarefa futura do Michel não fica no
  diário: vai para o To-do, com prazo.
- **Exceção: urgente.** O que é urgente e pede ação aparece na caixa laranja
  onde fizer sentido (Mail, To-do, Financ). É o único caso em que a mesma coisa
  aparece em dois lugares.

## Quando registrar

- Ação concluída com efeito fora do chat: e-mail enviado, nota emitida, arquivo
  salvo ou movido, evento criado ou alterado, lista montada, pagamento
  conferido, registro feito no Notion.
- O que ficou esperando alguém: resposta, confirmação, documento.
- Falha que o Michel precise saber: envio que não saiu, rotina que não rodou.
- Conversa, análise e rascunho não enviado **não** viram linha.

## Como registrar

- **Uma entrega, uma linha**: atualizar a mesma linha conforme avança
  (emitida → emitida e enviada). Não abrir linha nova para cada passo.
- **O que** (título): curto e direto. Ex.: "E-mail à contadora com as notas do
  mês".
- **Quando**: data e hora do fato.
- **Frente**: a opção que servir; criar nova se nenhuma servir.
- **Status**: Feito | Aguardando | Falhou.
- **Origem**: o nome do chat (Chat NF, Chat Finanças, Chat Radar, Rotina
  agendada, Checagem de e-mail). Chat novo cria a sua: "Chat <nome>".
- **Detalhe**: uma frase em primeira pessoa — o que foi feito e o que falta.
- **Link**: o e-mail, o arquivo ou a página. Vazio se não houver.

Como o Radar distribui: linha com link de e-mail, ou que espera terceiro ou
falhou, aparece na lista da estação Mail. As demais viram nota na caixinha de
status, que o Michel marca como lida.

## Fato que mexe no financeiro

Cliente que informa data ou valor de pagamento: quem leu o e-mail registra o
fato no diário com Frente = Financeiro e o link. Quem lança no arquivo de
finanças é o chat de finanças, sempre como "a confirmar", com a origem e o link
da linha do diário. O Michel confirma no Radar (estação Financ, caixa
"A confirmar") ou corrige por mensagem. Nunca marcar como recebido sem extrato.

## Regras

- Aguardando que se resolve: atualizar a mesma linha para Feito.
- As colunas **Conferido** e **Arquivado** são do Michel, marcadas no Radar.
  Não tocar — exceto para ler.
- **Nada sensível no texto**: saldo, renda, número de conta ou cartão, senha,
  código, saúde, societário, honorário. Registrar o fato sem o número.
- Antes de agir sobre lista ou demanda, ler o estado atual no Notion, para não
  refazer o que o Michel já resolveu.
- Gravar a linha é o último passo da tarefa. **Sem a linha, a tarefa não está
  entregue.**
