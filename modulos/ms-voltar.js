
/* ─── ms-voltar · retorno ao acervo + camada de toque ────────────────────────
   Uma linha por peça, no fim do <body>:

       <script defer src="../modulos/ms-voltar.js"></script>

   O comportamento inteiro mora AQUI. Mudar o botão em todas as apresentações
   de uma vez = editar este arquivo. Nenhuma peça precisa ser reaberta.

   O que faz, em ordem:
     1. desenha o chip "voltar ao acervo" no alto à esquerda, acima de tudo;
     2. aplica os ajustes de toque que valem para qualquer peça
        (sem zoom de duplo-toque, sem puxar-para-recarregar, sem inflar
        tipografia no iOS, área segura respeitada);
     3. em tablet/celular com suporte, oferece o chip de tela cheia;
     4. em deck de tela fixa aberto em retrato, avisa uma vez para girar —
        e só se a peça já não tiver aviso próprio.

   Degrada em silêncio: arquivo aberto do disco ou mandado por e-mail não
   acha o script, não mostra chip, e a apresentação abre exatamente como
   antes. É deliberado — fora do acervo não há acervo para onde voltar.

   Autonomia: não depende de CDN, de fonte externa nem de nada do deck.
   Não toca em variável, classe ou listener da engine da prancha.
─────────────────────────────────────────────────────────────────────────────*/
(function () {
  'use strict';

  if (window.__msVoltar) return;            /* dupla inclusão não duplica chip */
  window.__msVoltar = true;

  /* ─── onde fica o acervo ────────────────────────────────────────────────
     Deriva do src DESTE script, não do endereço da peça. Assim funciona em
     qualquer profundidade de pasta e não quebra se o repositório mudar de
     nome ou de domínio.                                                    */
  var eu = document.currentScript ||
           (function () {
             var s = document.querySelectorAll('script[src*="ms-voltar"]');
             return s[s.length - 1];
           })();
  var ACERVO = eu ? new URL('../index.html', eu.src).href
                  : new URL('../index.html', location.href).href;

  var toque = matchMedia('(pointer:coarse)').matches;

  /* ─── 1. viewport: cobrir o entalhe ─────────────────────────────────────
     Sem viewport-fit=cover o iPhone deitado deixa duas tarjas pretas e a
     sangria total deixa de ser total. env(safe-area-*) só passa a valer
     depois disto.                                                          */
  var vp = document.querySelector('meta[name="viewport"]');
  if (!vp) {
    vp = document.createElement('meta');
    vp.name = 'viewport';
    vp.content = 'width=device-width,initial-scale=1';
    document.head.appendChild(vp);
  }
  if (!/viewport-fit/.test(vp.content)) vp.content += ',viewport-fit=cover';

  /* ─── 2. estilo ─────────────────────────────────────────────────────────
     Véu escuro com fio claro: é o único par que lê tanto sobre prancha
     creme quanto sobre divisor oliva ou tinta. Não usa cor da marca de
     propósito — o chrome do navegador não deve competir com a peça.        */
  var CSS = [
    'html{-webkit-text-size-adjust:100%;text-size-adjust:100%}',
    'html,body{overscroll-behavior:none}',
    'body{touch-action:manipulation}',

    '#msVoltar{position:fixed;z-index:2147483000;',
    '  top:calc(env(safe-area-inset-top,0px) + 10px);',
    '  left:calc(env(safe-area-inset-left,0px) + 10px);',
    '  display:flex;align-items:center;gap:.5em;',
    '  height:' + (toque ? '44px' : '36px') + ';padding:0 ' + (toque ? '13px' : '11px') + ';',
    '  border:1px solid rgba(237,230,218,.30);border-radius:999px;',
    '  background:rgba(20,17,15,.46);color:#EDE6DA;',
    '  -webkit-backdrop-filter:blur(9px) saturate(1.15);',
    '  backdrop-filter:blur(9px) saturate(1.15);',
    '  font:500 11px/1 ui-monospace,"DM Mono",SFMono-Regular,Menlo,monospace;',
    '  letter-spacing:.16em;text-transform:lowercase;text-decoration:none;',
    '  cursor:pointer;opacity:' + (toque ? '.52' : '.34') + ';',
    '  transition:opacity .28s ease,background-color .28s ease,transform .28s ease;',
    '  -webkit-tap-highlight-color:transparent;appearance:none;outline:none}',
    '#msVoltar .g{font-size:14px;line-height:1;transform:translateY(-.5px)}',
    '#msVoltar .r{max-width:0;overflow:hidden;white-space:nowrap;opacity:0;',
    '  transition:max-width .30s cubic-bezier(.4,0,.2,1),opacity .22s ease}',
    '#msVoltar.aberto{opacity:1;background:rgba(20,17,15,.72)}',
    '#msVoltar.aberto .r{max-width:8em;opacity:1}',
    '#msVoltar:focus-visible{opacity:1;box-shadow:0 0 0 2px rgba(237,230,218,.55)}',
    '#msVoltar:active{transform:scale(.94)}',
    '@media (hover:hover){#msVoltar:hover{opacity:1;background:rgba(20,17,15,.72)}',
    '  #msVoltar:hover .r{max-width:8em;opacity:1}}',
    '@media print{#msVoltar,#msTela,#msGiro{display:none!important}}',

    '#msTela{position:fixed;z-index:2147483000;',
    '  top:calc(env(safe-area-inset-top,0px) + 10px);',
    '  left:calc(env(safe-area-inset-left,0px) + 64px);',
    '  width:44px;height:44px;display:grid;place-items:center;',
    '  border:1px solid rgba(237,230,218,.30);border-radius:999px;',
    '  background:rgba(20,17,15,.46);color:#EDE6DA;font-size:15px;line-height:1;',
    '  -webkit-backdrop-filter:blur(9px);backdrop-filter:blur(9px);',
    '  cursor:pointer;opacity:.52;appearance:none;outline:none;',
    '  -webkit-tap-highlight-color:transparent;transition:opacity .28s,transform .28s}',
    '#msTela:active{transform:scale(.94)}',

    '#msGiro{position:fixed;z-index:2147482900;left:50%;transform:translateX(-50%);',
    '  bottom:calc(env(safe-area-inset-bottom,0px) + 22px);',
    '  max-width:min(84vw,340px);padding:12px 18px;border-radius:14px;',
    '  border:1px solid rgba(237,230,218,.26);background:rgba(20,17,15,.80);',
    '  -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);',
    '  color:#EDE6DA;font:400 12.5px/1.45 ui-monospace,"DM Mono",Menlo,monospace;',
    '  text-align:center;opacity:0;pointer-events:none;transition:opacity .34s ease}',
    '#msGiro.on{opacity:1;pointer-events:auto}',
    '#msGiro b{display:block;font-weight:500;letter-spacing:.04em;margin-bottom:3px}',
    '#msGiro s{display:block;margin-top:6px;text-decoration:none;font-size:10.5px;',
    '  letter-spacing:.14em;text-transform:uppercase;color:rgba(237,230,218,.56)}',

    '@media (prefers-reduced-motion:reduce){#msVoltar,#msVoltar .r,#msTela,#msGiro',
    '  {transition-duration:.01ms}}'
  ].join('\n');

  var st = document.createElement('style');
  st.id = 'msVoltarCSS';
  st.textContent = CSS;
  document.head.appendChild(st);

  /* ─── 3. o chip ─────────────────────────────────────────────────────────
     <a> de verdade, com href: o botão do meio abre em aba nova e o menu de
     contexto oferece "copiar endereço". Um <button> perderia as duas coisas. */
  var chip = document.createElement('a');
  chip.id = 'msVoltar';
  chip.href = ACERVO;
  chip.title = 'voltar ao acervo de apresentações';
  chip.setAttribute('aria-label', 'voltar ao acervo de apresentações');
  chip.innerHTML = '<span class="g" aria-hidden="true">←</span><span class="r">acervo</span>';

  /* O deck escuta clique e tecla no document inteiro. O chip é irmão do
     palco, então clique nele não sobe até lá — mas Enter com foco no chip
     subiria e avançaria a prancha junto. Barrado na captura.               */
  chip.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') e.stopPropagation();
  }, true);
  chip.addEventListener('click', function (e) { e.stopPropagation(); });
  chip.addEventListener('pointerdown', function (e) { e.stopPropagation(); });
  chip.addEventListener('touchstart', function (e) { e.stopPropagation(); }, { passive: true });
  chip.addEventListener('touchend', function (e) { e.stopPropagation(); }, { passive: true });

  document.body.appendChild(chip);

  /* Aparece aberto por 2,6 s — é o que o torna descoberto — e depois recolhe
     para o disco discreto. Quem já sabe que ele existe acha na quina.      */
  requestAnimationFrame(function () {
    chip.classList.add('aberto');
    setTimeout(function () { chip.classList.remove('aberto'); }, 2600);
  });

  /* ─── 4. tela cheia, só onde existe ─────────────────────────────────────
     iPhone não expõe a API: o chip simplesmente não nasce. iPad e Android
     ganham o ganho real, que é sumir com a barra do navegador.             */
  if (toque && document.fullscreenEnabled) {
    var tela = document.createElement('button');
    tela.id = 'msTela';
    tela.type = 'button';
    tela.title = 'tela cheia';
    tela.setAttribute('aria-label', 'tela cheia');
    tela.textContent = '⛶';
    tela.addEventListener('click', function (e) {
      e.stopPropagation();
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen().catch(function () {});
    });
    tela.addEventListener('pointerdown', function (e) { e.stopPropagation(); });
    tela.addEventListener('touchstart', function (e) { e.stopPropagation(); }, { passive: true });
    tela.addEventListener('touchend', function (e) { e.stopPropagation(); }, { passive: true });
    document.body.appendChild(tela);
  }

  /* ─── 5. aviso de girar ─────────────────────────────────────────────────
     Sugestão, nunca barreira. Três condições, todas necessárias:
       · é dedo;
       · a peça é deck de tela fixa — página que rola já funciona em retrato
         e não deve receber aviso nenhum;
       · a peça ainda não tem aviso próprio (a casa ITTB tem: #giro).
     Uma vez por sessão, some sozinho em 5,5 s.                             */
  var jaTem = document.getElementById('giro') || document.getElementById('rotate');
  if (toque && !jaTem) {
    var giro = null, visto = false;

    function ehDeckFixo() {
      var d = document.documentElement;
      return d.scrollHeight <= innerHeight * 1.25;
    }
    function retrato() {
      return innerHeight > innerWidth;
    }
    function some() {
      if (!giro) return;
      giro.classList.remove('on');
      setTimeout(function () { if (giro) { giro.remove(); giro = null; } }, 380);
    }
    function avalia() {
      if (visto || giro || !retrato() || !ehDeckFixo()) return;
      visto = true;
      giro = document.createElement('div');
      giro.id = 'msGiro';
      giro.setAttribute('role', 'status');
      giro.innerHTML = '<b>melhor na horizontal</b>' +
                       'gire o aparelho para ver em tela cheia.' +
                       '<s>toque para dispensar</s>';
      giro.addEventListener('click', function (e) { e.stopPropagation(); some(); });
      giro.addEventListener('touchstart', function (e) { e.stopPropagation(); }, { passive: true });
      document.body.appendChild(giro);
      requestAnimationFrame(function () { giro.classList.add('on'); });
      setTimeout(some, 5500);
    }

    /* espera o deck montar antes de medir a altura */
    setTimeout(avalia, 900);
    addEventListener('orientationchange', function () { setTimeout(avalia, 400); });
  }
})();
