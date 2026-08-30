/* ═══════════════════════════════════════════════════════════════════════
   CHAVE DA GOOGLE MAPS PLATFORM — michel stein_
   Um arquivo só. Toda peça que usa mapa 3D carrega este e mais nada.
   Trocar a chave um dia é editar aqui, não vinte decks.

   ── POR QUE ELA ESTÁ EM REPOSITÓRIO PÚBLICO ─────────────────────────
   Decisão do Michel, 30/08/2026, e é exceção consciente à regra geral do
   acervo ("chave de API não entra no público").

   Chave de Maps NÃO é segredo, e não existe arranjo que a esconda: ela
   viaja para o navegador de quem abre a página e está legível no
   código-fonte de qualquer jeito. O que a protege é a RESTRIÇÃO POR
   REFERRER — ela só funciona a partir dos domínios abaixo. Fora deles,
   o Google recusa.

   A regra geral do acervo vale para chave de servidor, que é segredo de
   verdade. Aquela continua valendo. Esta é a única exceção.

   ── DOMÍNIOS CADASTRADOS NA CHAVE ────────────────────────────────────
   https://steinvalente-dev.github.io/*
   https://michel-stein.netlify.app/*
   http://localhost:8765/*          ← ensaio local, via `npx http-server`

   ⚑ DOMÍNIO NOVO EXIGE CADASTRO ANTES DE A PEÇA IR AO AR.
   Um repositório da Sarasá, ou de qualquer frente nova, precisa entrar
   nessa lista no console do Google — senão o slide abre com
   `RefererNotAllowed` na frente do cliente. É o que mais vai ser
   esquecido. Console → Keys & Credentials → a chave → Application
   restrictions → Websites.

   ── LIMITES DA CHAVE ─────────────────────────────────────────────────
   Restrita a UMA api: Maps JavaScript API. Não faz geocoding, não faz
   elevação, não faz rota. Se um gabarito novo precisar de outra, é
   decisão consciente — ampliar isto amplia a superfície.

   TETO DE USO, posto em 30/08/2026: `3D Map loads per day` = 1.000, no
   console em Quotas → Maps JavaScript API. Vinha "Unlimited". Régua para
   julgar o número: uma tarde inteira de testes deu NOVE carregamentos.
   Se um dia a peça bater no teto, o mapa para de abrir — e é para isso
   que o teto serve. Nesse caso, checar Metrics antes de subir o número:
   pode ser sucesso, pode ser vazamento.

   Trocar a chave: gerar nova no console, cadastrar os mesmos domínios e
   a mesma restrição de API, substituir a linha abaixo, publicar, e só
   então apagar a antiga. Nessa ordem — apagar antes derruba as peças no ar.
   ═══════════════════════════════════════════════════════════════════════ */
window.MS_MAPS = {
  chave: 'AIzaSyD4wz67qgTlOGVDOuDxcTPSnHT30UjJXg0',

  /* canal da API. `beta` é obrigatório enquanto o <gmp-map-3d> estiver em
     preview: a biblioteca maps3d não existe no canal estável. Quando sair
     para GA, trocar para 'weekly' — e revisar o gabarito. */
  canal: 'beta'
};
