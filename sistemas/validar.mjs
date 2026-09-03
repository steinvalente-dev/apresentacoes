#!/usr/bin/env node
/* validar — abre a peça no Chromium e barra o que o DECK-MONTAR manda barrar.

   Uso, na raiz do clone:
     node sistemas/validar.mjs <slug>/apresentacao.html [--cliente] [--rapido]

   --cliente  peça de cliente: a linha do ms-voltar.js tem de estar AUSENTE
   --rapido   pula a varredura de proporções (sete tamanhos de tela)

   Precisa do Playwright (npm i playwright@1 em /tmp → NODE_PATH=/tmp/node_modules) e de um
   Chromium; o caminho do binário vem de PW_CHROME ou do padrão abaixo. Serve a raiz do clone
   com `python3 -m http.server` numa porta livre e abre a peça com `?semfundo` (desliga os
   dois canvas do morph — não muda layout e é o que faz a varredura caber em segundos).

   Saída: uma linha por check — ok / FALHA / aviso — e código 1 se houver FALHA.
   O que fazer em cada falha: sistemas/DECK-JSON.md. */
import fs from 'node:fs';
import path from 'node:path';
import net from 'node:net';
import os from 'node:os';
import { spawn, spawnSync } from 'node:child_process';
import { createRequire } from 'node:module';

const t0 = Date.now();
const args = process.argv.slice(2);
const cliente = args.includes('--cliente');
const rapido = args.includes('--rapido');
const alvo = args.find(a => !a.startsWith('--'));
if (!alvo) { console.error('uso: node sistemas/validar.mjs <slug>/apresentacao.html [--cliente] [--rapido]'); process.exit(1); }
const arq = path.resolve(alvo);
if (!fs.existsSync(arq)) { console.error('validar: arquivo não existe: ' + arq); process.exit(1); }

/* a raiz do clone é a pasta que tem esqueleto/deck-esqueleto.html — a peça mora um nível abaixo */
let raiz = path.dirname(arq);
while (!fs.existsSync(path.join(raiz, 'esqueleto', 'deck-esqueleto.html'))) {
  const up = path.dirname(raiz);
  if (up === raiz) { console.error('validar: não achei a raiz do clone (esqueleto/deck-esqueleto.html) acima de ' + arq); process.exit(1); }
  raiz = up;
}
const rel = path.relative(raiz, arq).split(path.sep).join('/');
const html = fs.readFileSync(arq, 'utf8');

const VIEWPORTS = [[2560, 1080], [1920, 1080], [1366, 768], [1920, 1200], [1620, 1080], [1024, 768], [1440, 1080]];
const LINHA_VOLTAR = '<script defer src="../modulos/ms-voltar.js"></script>';
const IGNORA_CONSOLE = /favicon|ERR_CONNECTION|ERR_NAME|ERR_FAILED|ERR_BLOCKED|ERR_INTERNET|ERR_ABORTED|googleapis|gstatic|sketchup/i;

const resultados = [];   // {nome, estado:'ok'|'FALHA'|'aviso', detalhe}
const marca = (nome, estado, detalhe = '') => resultados.push({ nome, estado, detalhe });
const falhaOuOk = (nome, problemas, okTxt) =>
  problemas.length ? marca(nome, 'FALHA', problemas.join(' · ')) : marca(nome, 'ok', okTxt);

/* ── checks estáticos ─────────────────────────────────────────────────────── */
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
{
  const erros = [];
  scripts.forEach((s, i) => {
    const tmp = path.join(os.tmpdir(), `validar-${process.pid}-${i}.js`);
    fs.writeFileSync(tmp, s);
    const r = spawnSync('node', ['--check', tmp], { encoding: 'utf8' });
    fs.unlinkSync(tmp);
    if (r.status !== 0) erros.push(`<script> #${i + 1}: ${r.stderr.trim().split('\n').slice(0, 3).join(' ')}`);
  });
  falhaOuOk('sintaxe', erros, `${scripts.length} <script> inline passam no node --check`);
}
{
  const n = (html.match(/@font-face\{[^}]*base64,/g) || []).length;
  n >= 4 ? marca('fontes', 'ok', `${n} @font-face em base64`) : marca('fontes', 'FALHA', `${n} @font-face em base64 (mínimo 4) — as fontes do bloco da marca não foram coladas`);
}
{
  const tem = html.includes(LINHA_VOLTAR);
  if (cliente) tem ? marca('voltar', 'FALHA', 'peça de cliente com a linha do ms-voltar.js — montar com --cliente') : marca('voltar', 'ok', 'sem ms-voltar.js (peça de cliente)');
  else tem ? marca('voltar', 'ok', 'linha do ms-voltar.js presente') : marca('voltar', 'FALHA', 'falta a última linha antes de </body>: ' + LINHA_VOLTAR);
}
{
  /* hex fora do :root. Tira os blocos :root{…} (tokens + DERIVADOS + escala) e as linhas
     marcadas — convenção do esqueleto hoje: `/* #fff: motivo *\/`; aceita também `/* fixo: *\/`. */
  let css = [...html.matchAll(/<style>([\s\S]*?)<\/style>/g)].map(m => m[1]).join('\n');
  css = css.replace(/:root\s*\{[^{}]*\}/g, '');
  const achados = [];
  css.split('\n').forEach((linha, i) => {
    if (/\/\*\s*(fixo:|#[0-9a-f]{3,8}\s*:)/i.test(linha)) return;
    const semCom = linha.replace(/\/\*[\s\S]*?\*\//g, '');
    /* só dentro de declaração (depois de `:`), para não confundir com #id de seletor */
    for (const m of semCom.matchAll(/:[^;{}]*?(#[0-9A-Fa-f]{3,8})\b/g)) achados.push(`${m[1]} (linha ${i + 1} do CSS)`);
  });
  falhaOuOk('hex', achados, 'nenhum #RRGGBB fora do :root e dos marcados');
}
const peso = fs.statSync(arq).size / 1048576;
peso > 8 ? marca('peso', 'aviso', `${peso.toFixed(2)} MB — acima do limite de anexo de e-mail; entregar por link`) : marca('peso', 'ok', `${peso.toFixed(2)} MB`);

/* a lista `em-imagem` do go(), lida do código */
const emImagem = (() => {
  const m = html.match(/toggle\('em-imagem',([\s\S]*?)\);/);
  return m ? [...m[1].matchAll(/'([\w-]+)'/g)].map(x => x[1]) : null;
})();

/* ── navegador ───────────────────────────────────────────────────────────── */
let playwright;
try {
  playwright = createRequire(import.meta.url)('playwright');
} catch {
  try { playwright = createRequire(path.join(os.tmpdir(), 'x'))('playwright'); }
  catch { console.error('validar: playwright não encontrado. Em /tmp: npm i playwright@1 e rode com NODE_PATH=/tmp/node_modules'); process.exit(1); }
}
const CHROME = process.env.PW_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const porta = await new Promise(res => { const s = net.createServer(); s.listen(0, '127.0.0.1', () => { const p = s.address().port; s.close(() => res(p)); }); });
const servidor = spawn('python3', ['-m', 'http.server', String(porta), '--bind', '127.0.0.1', '-d', raiz], { stdio: 'ignore' });
const base = `http://127.0.0.1:${porta}/`;
for (let i = 0; i < 50; i++) { try { await fetch(base); break; } catch { await new Promise(r => setTimeout(r, 100)); } }

const browser = await playwright.chromium.launch({
  headless: true, executablePath: fs.existsSync(CHROME) ? CHROME : undefined,
  args: ['--no-sandbox', '--disable-dev-shm-usage'],
});
const consoleErros = [];
try {
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 }, reducedMotion: 'reduce' });
  /* sem rede: qualquer coisa fora do servidor local é cortada na hora, em vez de esperar o timeout */
  await page.route(u => !(u.href.startsWith(base) || u.protocol === 'data:' || u.protocol === 'blob:'), r => r.abort());
  page.on('pageerror', e => consoleErros.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !IGNORA_CONSOLE.test(m.text())) consoleErros.push('console.error: ' + m.text().slice(0, 200)); });

  await page.goto(base + rel + '?semfundo', { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(400);

  /* gabaritos: o laço do tpl() e os slides renderizados */
  const gab = await page.evaluate(() => {
    const p = [];
    if (typeof DECK === 'undefined' || typeof tpl !== 'function') return ['DECK ou tpl() não existem na página'];
    for (let i = 0; i < DECK.length; i++) {
      const s = DECK[i];
      if (!s || typeof s !== 'object') { p.push(`slide ${i}: posição vazia no array DECK (vírgula dupla?)`); continue; }
      try { tpl(s); } catch (e) { p.push(`slide ${i} (${s.g}) lança ${e.message}`); }
    }
    const sl = [...document.querySelectorAll('#palco .slide')];
    if (sl.length !== DECK.length) p.push(`${sl.length} slides renderizados para ${DECK.length} no DECK`);
    sl.forEach((el, i) => {
      const g = DECK[i] && DECK[i].g, tx = el.textContent || '';
      if (/gabarito desconhecido/.test(tx)) p.push(`slide ${i}: gabarito desconhecido "${g}"`);
      else if (/gabarito [\w-]+: falta/.test(tx)) p.push(`slide ${i} (${g}): ${(el.querySelector('.aviso h2') || el).textContent.trim().slice(0, 80)}`);
      else if (/gabarito [\w-]+ quebrou/.test(tx)) p.push(`slide ${i} (${g}): quebrou`);
      else if (/<code>cols<\/code> sem/.test(el.innerHTML)) p.push(`slide ${i} (${g}): cols sem linhas`);
      if (!el.innerHTML.trim() || (!tx.trim() && !el.querySelector('img,svg,iframe,canvas,.slot'))) p.push(`slide ${i} (${g}): vazio`);
    });
    return p;
  });
  falhaOuOk('gabaritos', gab, `${await page.evaluate(() => DECK.length)} slides, tpl() sem exceção, nenhum aviso`);

  /* percorre todos os slides, com todos os passos, no tamanho padrão */
  const percorre = async (vw, vh) => {
    return page.evaluate(async ([vw, vh, emImagem]) => {
      const dorme = ms => new Promise(r => setTimeout(r, ms));
      const sl = [...document.querySelectorAll('#palco .slide')];
      const out = { undef: [], transb: [], quadro: null, imagem: [] };
      const q = document.getElementById('quadro') || document.getElementById('palco');
      const r = q.getBoundingClientRect();
      if (Math.abs(r.width - innerWidth) > 1 || Math.abs(r.height - innerHeight) > 1)
        out.quadro = `#quadro ${Math.round(r.width)}×${Math.round(r.height)} numa tela ${innerWidth}×${innerHeight} (letterbox)`;
      for (let i = 0; i < sl.length; i++) {
        go(i, true);
        sl[i].querySelectorAll('.passo').forEach(p => p.classList.add('on'));
        await dorme(40);
        const el = sl[i], g = DECK[i].g;
        const tx = (el.textContent || '');
        if (/(^|[^\w])(undefined|NaN)([^\w]|$)/.test(tx)) out.undef.push(`slide ${i} (${g})`);
        const d = el.scrollHeight - el.clientHeight;
        if (d > 2) out.transb.push(`slide ${i} (${g}) +${d}px`);
        /* fundo em imagem ou visor: iframe, ou imagem/quadro que cobre a tela */
        let cheio = !!el.querySelector('iframe');
        if (!cheio) for (const im of el.querySelectorAll('img,.full,[style*="background-image"]')) {
          const b = im.getBoundingClientRect();
          if (b.width >= innerWidth * 0.9 && b.height >= innerHeight * 0.9) { cheio = true; break; }
        }
        if (cheio && emImagem && !emImagem.includes(g) && !out.imagem.includes(g)) out.imagem.push(g);
      }
      return out;
    }, [vw, vh, emImagem]);
  };

  const r0 = await percorre(1600, 900);
  falhaOuOk('undefined', r0.undef, 'nenhum slide escreve undefined/NaN');
  if (!emImagem) marca('em-imagem', 'FALHA', 'não achei a lista em-imagem no go() do esqueleto');
  else falhaOuOk('em-imagem', r0.imagem.map(g => `gabarito "${g}" tem fundo de imagem/visor e não está na lista em-imagem do go()`),
    `lista: ${emImagem.join(', ')}`);

  /* proporções: UMA página, redimensionada — abrir sete derruba o Chromium */
  if (rapido) marca('proporcoes', 'aviso', 'pulado (--rapido)');
  else {
    const probs = [];
    for (const [w, h] of VIEWPORTS) {
      await page.setViewportSize({ width: w, height: h });
      await page.waitForTimeout(120);
      const r = await percorre(w, h);
      if (r.quadro) probs.push(`${w}×${h}: ${r.quadro}`);
      r.transb.forEach(x => probs.push(`${w}×${h}: ${x}`));
    }
    falhaOuOk('proporcoes', probs, `${VIEWPORTS.length} tamanhos, todos os slides e passos, sem transbordo nem letterbox`);
  }

  const temEarth = await page.evaluate(() => DECK.some(s => s.g === 'earth-3d'));
  if (temEarth) marca('chave-maps', 'aviso', 'slide earth-3d: entrega por link; o domínio precisa estar na chave da Maps Platform (modulos/ms-maps-chave.js)');
  else marca('chave-maps', 'ok', 'sem earth-3d');

  await page.waitForTimeout(300);
  falhaOuOk('console', [...new Set(consoleErros)].slice(0, 12), 'zero pageerror, zero console.error');
} catch (e) {
  marca('navegador', 'FALHA', 'o Chromium não completou a varredura: ' + e.message.split('\n')[0]);
} finally {
  await browser.close().catch(() => {});
  servidor.kill();
}

/* ── relatório ───────────────────────────────────────────────────────────── */
const ordem = ['sintaxe', 'gabaritos', 'undefined', 'console', 'fontes', 'voltar', 'em-imagem', 'hex', 'proporcoes', 'peso', 'chave-maps', 'navegador'];
resultados.sort((a, b) => ordem.indexOf(a.nome) - ordem.indexOf(b.nome));
for (const r of resultados) console.log(`${r.estado.padEnd(6)} ${r.nome.padEnd(11)} ${r.detalhe}`);
const falhas = resultados.filter(r => r.estado === 'FALHA');
console.log(`\nvalidar: ${rel} — ${falhas.length ? falhas.length + ' FALHA(S): ' + falhas.map(f => f.nome).join(', ') : 'passou'} · ${((Date.now() - t0) / 1000).toFixed(1)} s`);
process.exit(falhas.length ? 1 : 0);
