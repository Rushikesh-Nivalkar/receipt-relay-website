<#
.SYNOPSIS
  Build the ReceiptRelay website on the NAS, mirror dist/ to D:\dev\receipt-relay-website, serve it from D:\dev.
.DESCRIPTION
  1. node scripts/build.mjs on the NAS copy (src -> dist).
  2. robocopy /MIR dist -> D:\dev\receipt-relay-website\dist (incremental), plus serve.mjs + site.config.json.
  3. node scripts/serve.mjs from D:\dev on http://localhost:<port> (foreground; run in background).
  If the port is already in use, the running server already serves the new files (it reads from disk
  per request), so serving is skipped. -NoServe = build + sync only. Local preview only: no deploy.
.EXAMPLE
  powershell -ExecutionPolicy Bypass -File start-local.ps1
  powershell -ExecutionPolicy Bypass -File start-local.ps1 -NoServe
#>
[CmdletBinding()]
param(
    [string]$Dest = 'D:\dev\receipt-relay-website',
    [switch]$NoServe
)
$ErrorActionPreference = 'Stop'

$site = Split-Path -Parent $PSScriptRoot
$dst  = [IO.Path]::GetFullPath($Dest).TrimEnd('\')
if (-not (Test-Path -LiteralPath (Join-Path $site 'site.config.json'))) { throw "Not the website folder: $site" }
if ($dst -notlike 'D:\dev\?*') { throw "Local copies live only under D:\dev\<slug>, not $dst" }
if ($site.TrimEnd('\') -ieq $dst) { throw 'Run this from the NAS copy, not from D:\dev.' }
if (-not (Get-Command node -ErrorAction SilentlyContinue)) { throw 'node not on PATH (Node 22+ needed).' }

# 1. Build on the NAS.
& node (Join-Path $site 'scripts\build.mjs')
if ($LASTEXITCODE -ne 0) { throw 'Build failed.' }

# 2. Incremental mirror to D:\dev.
function Invoke-Robo([string[]]$RoboArgs) {
    & robocopy @RoboArgs /R:2 /W:2 /NP /NDL /NJH /NJS | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "robocopy failed (exit $LASTEXITCODE): $($RoboArgs -join ' ')" }
}
Invoke-Robo @((Join-Path $site 'dist'), (Join-Path $dst 'dist'), '/MIR')
Invoke-Robo @((Join-Path $site 'scripts'), (Join-Path $dst 'scripts'), 'serve.mjs')
Invoke-Robo @($site, $dst, 'site.config.json')
Write-Host "Synced dist -> $dst\dist"

if ($NoServe) { exit 0 }

# 3. Serve from D:\dev.
$port = (Get-Content -LiteralPath (Join-Path $dst 'site.config.json') -Raw | ConvertFrom-Json).port
$busy = $null
try { $busy = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction Stop } catch {}
if ($busy) {
    Write-Host "Port $port already in use - existing server now serves the new build: http://localhost:$port"
    exit 0
}
Push-Location $dst
try { & node 'scripts\serve.mjs' } finally { Pop-Location }
