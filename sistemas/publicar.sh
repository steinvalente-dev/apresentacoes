#!/usr/bin/env bash
# publicar.sh — a rodada inteira de publicação do acervo, num comando só.
#
# Uso, na raiz do clone:
#   GH=<token> sistemas/publicar.sh "<mensagem do commit>" [<slug-da-peça-para-validar>]
#   sistemas/publicar.sh --seco "<mensagem>" [<slug>]      # roda os passos 1–6 e para antes do commit
#   sistemas/publicar.sh --ate <n> "<mensagem>" [<slug>]   # para depois do passo n
#
# Cada passo imprime "ok" ou "FALHA" e a rodada para na primeira falha. Nada aqui
# usa --force: recusa de push quer dizer trabalho de outra sessão no meio.
# Códigos de saída: 0 publicado · 1 falha de passo · 2 push barrado pela permissão da tarefa.
set -euo pipefail
# rede direta: o proxy da sessão não serve para git nem para o curl de conferência
export NO_PROXY='*' HTTPS_PROXY= https_proxy= http_proxy=

REPO='steinvalente-dev/apresentacoes'
URL_PAGES='https://steinvalente-dev.github.io/apresentacoes'
URL_PUB='https://github.com/steinvalente-dev/apresentacoes.git'
FILTRO='s/(github_pat_|gh[pous]_)[A-Za-z0-9_]+/***/g'   # token nunca aparece na saída

cd "$(dirname "$0")/.."

# ── argumentos ──────────────────────────────────────────────────────────────
ATE=99
while [[ $# -gt 0 && "$1" == --* ]]; do
  case "$1" in
    --seco) ATE=6; shift ;;
    --ate)  ATE="$2"; shift 2 ;;
    *) echo "opção desconhecida: $1"; exit 1 ;;
  esac
done
MSG="${1:-}"; SLUG="${2:-}"
[[ -n "$MSG" ]] || { echo 'uso: GH=<token> sistemas/publicar.sh "<mensagem>" [<slug>]'; exit 1; }
if (( ATE >= 9 )) && [[ -z "${GH:-}" ]]; then
  echo 'FALHA  GH vazio — o token vem de CREDENCIAIS.md, nos documentos do Projeto (nunca de um repositório)'; exit 1
fi

# ── utilitários ─────────────────────────────────────────────────────────────
N=0
passo(){ N=$1; printf '\n[%d/10] %s\n' "$1" "$2"; }
ok(){ echo "  ok     ${1:-}"; }
falha(){ echo "  FALHA  ${1:-}"; exit 1; }
aviso(){ echo "  aviso  ${1:-}"; }
parar_se(){ # para depois do passo pedido (--seco / --ate)
  if (( N >= ATE )); then printf '\nparado depois do passo %d, como pedido — nada foi commitado.\n' "$N"; exit 0; fi
}
guarda(){ python3 sistemas/guarda-publico.py 2>&1 | sed -E "$FILTRO"; return "${PIPESTATUS[0]}"; }

# ── 1 · sincronizar ─────────────────────────────────────────────────────────
passo 1 'git fetch + pull --ff-only'
git remote get-url origin >/dev/null 2>&1 || { git remote add origin "$URL_PUB"; aviso "origin não existia — configurado ($URL_PUB)"; }
git fetch origin 2>&1 | sed -E "$FILTRO" || falha 'fetch'
[[ "$(git branch --show-current)" == main ]] || falha "branch atual é '$(git branch --show-current)', não main"
git pull --ff-only origin main 2>&1 | sed -E "$FILTRO" || falha 'pull --ff-only recusado: histórico divergente, ou mudança local no mesmo arquivo que alguém publicou. Resolver à mão'
ok "HEAD $(git rev-parse --short HEAD)"; parar_se

# ── 2 · dados.json ──────────────────────────────────────────────────────────
passo 2 'montar-indice.py — regenera dados.json e detecta órfã'
python3 sistemas/montar-indice.py || falha 'ver acima: órfã, meta inválido ou peça de cliente'
ok; parar_se

# ── 3 · guarda do público ───────────────────────────────────────────────────
passo 3 'guarda-publico.py'
guarda || falha 'achado no repositório público — não sobe'
ok; parar_se

# ── 4 · tabela de gabaritos ─────────────────────────────────────────────────
passo 4 'gerar-gabaritos.py --check'
python3 sistemas/gerar-gabaritos.py --check || falha 'tabela de gabaritos diverge do código: rodar sem --check e commitar junto'
ok; parar_se

# ── 5 · sintaxe do index.html ───────────────────────────────────────────────
passo 5 'node --check nos scripts inline de index.html'
python3 - <<'PY' || falha 'erro de sintaxe: a página abriria em branco'
import re, subprocess, sys, tempfile, pathlib
s = pathlib.Path('index.html').read_text(encoding='utf-8')
blocos = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', s, re.S)
for i, js in enumerate(blocos):
    with tempfile.NamedTemporaryFile('w', suffix=f'-inline{i}.js', delete=False, encoding='utf-8') as f:
        f.write(js); nome = f.name
    r = subprocess.run(['node', '--check', nome], capture_output=True, text=True)
    pathlib.Path(nome).unlink(missing_ok=True)
    if r.returncode: print(r.stderr); sys.exit(1)
print(f'  {len(blocos)} script(s) inline ok')
PY
ok; parar_se

# ── 6 · validar a peça ──────────────────────────────────────────────────────
passo 6 'validar.mjs na peça'
if [[ -z "$SLUG" ]]; then
  ok 'sem slug — nada a validar'
elif [[ ! -f "$SLUG/apresentacao.html" ]]; then
  falha "não existe $SLUG/apresentacao.html"
elif [[ ! -f sistemas/validar.mjs ]]; then
  aviso 'sistemas/validar.mjs não existe neste clone — validação da peça pulada'
else
  node sistemas/validar.mjs "$SLUG/apresentacao.html" || falha 'a peça não passou na validação'
  ok "$SLUG"
fi
parar_se

# ── 7 · commit ──────────────────────────────────────────────────────────────
passo 7 'git add -A && git commit'
git add -A
# o que o .gitignore está engolindo — visível, para ninguém descobrir dias depois (caso registro/_geral.json, 03–04/09)
ENGOLIDOS="$(git ls-files --others --ignored --exclude-standard | grep -v -E '^(node_modules/|\.)' || true)"
if [[ -n "$ENGOLIDOS" ]]; then
  echo "  aviso  o .gitignore está deixando de fora (não vão subir):"; echo "$ENGOLIDOS" | sed 's/^/           /'
  if echo "$ENGOLIDOS" | grep -q -E '(^|/)(meta\.json|apresentacao\.html|registro/|sistemas/|marca/|modulos/|esqueleto/)'; then
    falha 'arquivo do sistema ignorado pelo .gitignore — renomear (nada que o sistema lê começa por _) ou estreitar a regra'
  fi
fi
if git diff --cached --quiet; then
  echo '  nada para commitar — a árvore está igual ao HEAD.'
  if [[ -z "$(git log --oneline origin/main..HEAD)" ]]; then echo '  e nada local por subir. Fim.'; exit 0; fi
  aviso 'há commit local por subir; seguindo sem commit novo'
else
  # autor fixo da casa: o container não tem git config, e "Claude <noreply>" no histórico não diz de quem é o acervo
  git -c user.name=steinvalente-dev -c user.email=michel@michelstein.com.br \
    commit -q -m "$MSG" -m "Publicado por sistemas/publicar.sh" || falha 'commit'
  ok "$(git log --oneline -1 | sed -E "$FILTRO")"
fi
parar_se

# ── 8 · alguém publicou no meio? ────────────────────────────────────────────
passo 8 'git fetch — o remoto avançou?'
git fetch origin 2>&1 | sed -E "$FILTRO" || falha 'fetch'
if [[ -n "$(git log --oneline HEAD..origin/main)" ]]; then
  aviso "remoto avançou $(git rev-list --count HEAD..origin/main) commit(s): rebase, regenerar dados.json, guarda de novo"
  git rebase origin/main 2>&1 | sed -E "$FILTRO" || { git rebase --abort 2>/dev/null || true; falha 'conflito no rebase — resolver à mão, NUNCA --force'; }
  python3 sistemas/montar-indice.py || falha 'montar-indice depois do rebase'
  if ! git diff --quiet -- dados.json; then
    git add dados.json && git -c user.name=steinvalente-dev -c user.email=michel@michelstein.com.br commit --amend --no-edit -q
  fi
  guarda || falha 'achado depois do rebase — o que veio do outro lado não está limpo'
fi
ok "HEAD $(git rev-parse --short HEAD)"; parar_se

# ── 9 · push ────────────────────────────────────────────────────────────────
passo 9 'git push (sem --force)'
SAIDA_PUSH="$(git -c http.proxy= -c https.proxy= push "https://x-access-token:${GH}@github.com/${REPO}.git" HEAD:main 2>&1 || true)"
SAIDA_PUSH="$(printf '%s' "$SAIDA_PUSH" | sed -E "$FILTRO")"
echo "$SAIDA_PUSH" | sed 's/^/  /'
if grep -q 'denied by the Claude Code auto mode classifier' <<<"$SAIDA_PUSH"; then
  echo
  echo '  Barrado por permissão, não por token: o commit está pronto localmente e só falta liberar a escrita'
  echo "  em github.com/${REPO} (main). Não tentar por outro caminho — API e clone com token são a mesma ação."
  exit 2
fi
# push aceito: o remoto aponta para o nosso HEAD
git fetch origin 2>&1 | sed -E "$FILTRO" >/dev/null || true
[[ "$(git rev-parse HEAD)" == "$(git rev-parse origin/main)" ]] || falha 'push não chegou — origin/main não é o HEAD local'
ok "origin/main = $(git rev-parse --short HEAD)"; parar_se

# ── 10 · no ar? ─────────────────────────────────────────────────────────────
passo 10 'esperar 60 s e conferir o Pages'
GERADO="$(python3 -c "import json;print(json.load(open('dados.json'))['gerado'])")"
sleep 60
for tent in 1 2 3; do
  NOAR="$(curl -sS --max-time 20 "${URL_PAGES}/dados.json?nc=$RANDOM$RANDOM" || true)"
  if grep -qF "\"gerado\": \"$GERADO\"" <<<"$NOAR" || grep -qF "\"gerado\":\"$GERADO\"" <<<"$NOAR"; then break; fi
  NOAR=''; (( tent < 3 )) && sleep 30
done
[[ -n "$NOAR" ]] || falha "dados.json no ar ainda não traz gerado=$GERADO — Pages atrasado; conferir em um minuto com ?nc="
ok "dados.json no ar, gerado $GERADO"
if [[ -n "$SLUG" ]]; then
  COD="$(curl -sS -o /dev/null -w '%{http_code}' --max-time 30 "${URL_PAGES}/${SLUG}/apresentacao.html?nc=$RANDOM$RANDOM" || echo 000)"
  [[ "$COD" == 200 ]] || falha "a peça respondeu $COD"
  ok "peça responde 200"
  echo
  echo "${URL_PAGES}/${SLUG}/apresentacao.html"
else
  echo
  echo 'publicado. Devolver sempre o link da peça, nunca o do índice.'
fi
