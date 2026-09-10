# servir.ps1 -- servidor estatico local, para ensaiar peca com slide 3D.
#
# POR QUE EXISTE
# A Maps JavaScript API recusa pagina aberta do disco (file://): o visor 3D
# so desenha se a pagina vier de um endereco http. A porta 8765 e' a que esta
# cadastrada na chave (ver modulos/ms-maps-chave.js) e localhost nao exige
# privilegio de administrador.
#
# A maquina do Michel NAO TEM Node nem Python -- `npx http-server` e
# `python -m http.server` nao rodam la. PowerShell vem com o Windows, e o
# System.Net.HttpListener resolve sem instalar nada. Foi por isso que este
# arquivo nasceu, em 10/09/2026.
#
# COMO USAR, na pasta da peca:
#     powershell -ExecutionPolicy Bypass -File servir.ps1
# Depois abrir:  http://localhost:8765/apresentacao.html
# Para parar:    Ctrl+C
#
# Serve a pasta corrente e nada acima dela. Nao e' servidor de producao:
# escuta so em localhost, um pedido por vez, sem cache e sem range.

$porta = 8765
$raiz   = (Get-Location).Path

$tipos = @{
  '.html'='text/html; charset=utf-8'; '.htm'='text/html; charset=utf-8'
  '.js'='text/javascript; charset=utf-8'; '.mjs'='text/javascript; charset=utf-8'
  '.css'='text/css; charset=utf-8';   '.json'='application/json; charset=utf-8'
  '.png'='image/png'; '.jpg'='image/jpeg'; '.jpeg'='image/jpeg'
  '.webp'='image/webp'; '.svg'='image/svg+xml'; '.gif'='image/gif'
  '.woff2'='font/woff2'; '.woff'='font/woff'; '.pdf'='application/pdf'
}

$ouvinte = New-Object System.Net.HttpListener
$ouvinte.Prefixes.Add("http://localhost:$porta/")
try { $ouvinte.Start() }
catch {
  Write-Host "Nao consegui abrir a porta $porta." -ForegroundColor Red
  Write-Host "Se outro programa estiver usando a porta, feche-o e rode de novo."
  exit 1
}

Write-Host ""
Write-Host "  servindo $raiz" -ForegroundColor DarkGray
Write-Host "  http://localhost:$porta/apresentacao.html" -ForegroundColor Green
Write-Host "  Ctrl+C para parar" -ForegroundColor DarkGray
Write-Host ""

try {
  while ($ouvinte.IsListening) {
    $ctx = $ouvinte.GetContext()
    $rel = [System.Uri]::UnescapeDataString($ctx.Request.Url.AbsolutePath).TrimStart('/')
    if ([string]::IsNullOrWhiteSpace($rel)) { $rel = 'apresentacao.html' }
    $alvo = Join-Path $raiz $rel

    # nao sair da pasta servida
    $ok = $false
    try { $ok = (Resolve-Path -LiteralPath $alvo -ErrorAction Stop).Path.StartsWith($raiz) } catch { $ok = $false }

    if ($ok -and (Test-Path -LiteralPath $alvo -PathType Leaf)) {
      $ext = [System.IO.Path]::GetExtension($alvo).ToLower()
      $ctx.Response.ContentType = $(if ($tipos.ContainsKey($ext)) { $tipos[$ext] } else { 'application/octet-stream' })
      $bytes = [System.IO.File]::ReadAllBytes($alvo)
      $ctx.Response.ContentLength64 = $bytes.Length
      $ctx.Response.OutputStream.Write($bytes, 0, $bytes.Length)
      Write-Host ("  200  " + $rel) -ForegroundColor DarkGray
    } else {
      $ctx.Response.StatusCode = 404
      $msg = [System.Text.Encoding]::UTF8.GetBytes("nao encontrado: $rel")
      $ctx.Response.OutputStream.Write($msg, 0, $msg.Length)
      Write-Host ("  404  " + $rel) -ForegroundColor DarkYellow
    }
    $ctx.Response.OutputStream.Close()
  }
} finally {
  $ouvinte.Stop(); $ouvinte.Close()
  Write-Host "  parado." -ForegroundColor DarkGray
}
