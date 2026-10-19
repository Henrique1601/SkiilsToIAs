<#
.SYNOPSIS
    Instalador Automatico de Skills, Agentes e Servidores MCP para Ambientes de IA.
    Compativel com Antigravity / Gemini CLI, Claude Code e Claude Desktop.

.DESCRIPTION
    Script PowerShell oficial para instalacao com 1-clique em novos computadores.
    Desenvolvido por Henrique Bezerra Dos Santos (@Henrique1601)

.PARAMETER Target
    Define o alvo da instalacao: "all" (padrao), "gemini", "claude"

.PARAMETER SkipMcp
    Pula a configuracao de servidores MCP se especificado.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\install.ps1
    powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target gemini
    powershell -ExecutionPolicy Bypass -File .\install.ps1 -Target claude -SkipMcp
#>

[CmdletBinding()]
param(
    [ValidateSet("all", "gemini", "claude")]
    [string]$Target = "all",
    [switch]$SkipMcp
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RepoRoot = $PSScriptRoot
if (-not $RepoRoot) {
    $RepoRoot = (Get-Location).Path
}

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "SkiilsToIAs - Instalador Automatico de Skills, Agentes e MCPs" -ForegroundColor Cyan
Write-Host "Repositorio: Henrique1601/SkiilsToIAs" -ForegroundColor DarkCyan
Write-Host "Origem: $RepoRoot" -ForegroundColor DarkGray
Write-Host "Alvo: $Target | Configurar MCP: $(!$SkipMcp)" -ForegroundColor DarkGray
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host ""

$Categories = @(
    "ai-agents",
    "backend-database",
    "business-management",
    "career",
    "design",
    "development",
    "devops-cloud",
    "documents-productivity",
    "marketing",
    "seo",
    "utilities"
)

function Install-Gemini {
    Write-Host "[1/3] Instalando Skills e Agentes para Gemini / Antigravity..." -ForegroundColor Yellow
    
    $GeminiSkillsDir = Join-Path $HOME ".gemini\config\skills"
    $GeminiAgentsDir = Join-Path $HOME ".gemini\config\agents"

    if (-not (Test-Path $GeminiSkillsDir)) {
        New-Item -ItemType Directory -Path $GeminiSkillsDir -Force | Out-Null
    }
    if (-not (Test-Path $GeminiAgentsDir)) {
        New-Item -ItemType Directory -Path $GeminiAgentsDir -Force | Out-Null
    }

    $installedSkills = 0
    foreach ($cat in $Categories) {
        $srcCat = Join-Path $RepoRoot $cat
        if (Test-Path $srcCat) {
            $destCat = Join-Path $GeminiSkillsDir $cat
            if (-not (Test-Path $destCat)) {
                New-Item -ItemType Directory -Path $destCat -Force | Out-Null
            }

            Get-ChildItem -Path $srcCat -Directory | ForEach-Object {
                $skillSrc = $_.FullName
                $skillDest = Join-Path $destCat $_.Name
                Copy-Item -Path $skillSrc -Destination $skillDest -Recurse -Force
                $installedSkills++
            }
        }
    }

    $srcAgents = Join-Path $RepoRoot "custom-agents"
    $installedAgents = 0
    if (Test-Path $srcAgents) {
        Get-ChildItem -Path $srcAgents -Filter "*.md" | ForEach-Object {
            Copy-Item -Path $_.FullName -Destination $GeminiAgentsDir -Force
            $installedAgents++
        }
    }

    Write-Host "  Gemini: $installedSkills skills e $installedAgents agentes instalados com sucesso!" -ForegroundColor Green
    Write-Host "     Destino Skills: $GeminiSkillsDir" -ForegroundColor DarkGray
    Write-Host "     Destino Agentes: $GeminiAgentsDir" -ForegroundColor DarkGray
}

function Install-Claude {
    Write-Host "[2/3] Instalando Skills para Claude Code..." -ForegroundColor Yellow
    
    $ClaudeSkillsDir = Join-Path $HOME ".claude\skills"
    if (-not (Test-Path $ClaudeSkillsDir)) {
        New-Item -ItemType Directory -Path $ClaudeSkillsDir -Force | Out-Null
    }

    $installedSkills = 0
    foreach ($cat in $Categories) {
        $srcCat = Join-Path $RepoRoot $cat
        if (Test-Path $srcCat) {
            Get-ChildItem -Path $srcCat -Directory | ForEach-Object {
                $skillSrc = $_.FullName
                $skillDest = Join-Path $ClaudeSkillsDir $_.Name
                Copy-Item -Path $skillSrc -Destination $skillDest -Recurse -Force
                $installedSkills++
            }
        }
    }

    Write-Host "  Claude Code: $installedSkills skills instaladas com sucesso!" -ForegroundColor Green
    Write-Host "     Destino Skills: $ClaudeSkillsDir" -ForegroundColor DarkGray
}

function Install-McpServers {
    Write-Host "[3/3] Configurando Servidores MCP..." -ForegroundColor Yellow

    $mcpTemplatePath = Join-Path $RepoRoot "mcps\mcp_template.json"
    if (-not (Test-Path $mcpTemplatePath)) {
        Write-Warning "Arquivo mcps/mcp_template.json nao encontrado em $RepoRoot."
        return
    }

    $templateRaw = Get-Content -Path $mcpTemplatePath -Raw -Encoding UTF8
    $templateJson = $templateRaw | ConvertFrom-Json

    $targetConfigs = @()
    $targetConfigs += (Join-Path $HOME ".gemini\config\mcp_config.json")
    if ($env:APPDATA) {
        $targetConfigs += (Join-Path $env:APPDATA "Claude\claude_desktop_config.json")
    }

    foreach ($cfgPath in $targetConfigs) {
        $cfgDir = Split-Path -Path $cfgPath -Parent
        if (-not (Test-Path $cfgDir)) {
            New-Item -ItemType Directory -Path $cfgDir -Force | Out-Null
        }

        $existing = [ordered]@{}
        if (Test-Path $cfgPath) {
            try {
                $content = Get-Content -Path $cfgPath -Raw -Encoding UTF8
                if ($content.Trim()) {
                    $existing = $content | ConvertFrom-Json -AsHashtable
                }
            } catch {
                $existing = [ordered]@{}
            }
        }

        if (-not $existing.ContainsKey("mcpServers")) {
            $existing["mcpServers"] = [ordered]@{}
        }

        $addedCount = 0
        foreach ($prop in $templateJson.mcpServers.PSObject.Properties) {
            $serverName = $prop.Name
            if (-not $existing["mcpServers"].ContainsKey($serverName)) {
                $existing["mcpServers"][$serverName] = $prop.Value
                $addedCount++
            }
        }

        $outputJson = $existing | ConvertTo-Json -Depth 10
        Set-Content -Path $cfgPath -Value $outputJson -Encoding UTF8
        Write-Host "  MCP atualizado em: $cfgPath (Novos adicionados: $addedCount)" -ForegroundColor Green
    }
}

try {
    if ($Target -eq "all" -or $Target -eq "gemini") {
        Install-Gemini
        Write-Host ""
    }
    if ($Target -eq "all" -or $Target -eq "claude") {
        Install-Claude
        Write-Host ""
    }
    if (-not $SkipMcp) {
        Install-McpServers
        Write-Host ""
    }

    Write-Host "=================================================================" -ForegroundColor Cyan
    Write-Host "Instalacao concluida com sucesso em seu ambiente!" -ForegroundColor Green
    Write-Host "Lembre-se de configurar suas credenciais (ex: Prospector CRM / Notion)" -ForegroundColor Yellow
    Write-Host "em ~/.gemini/config/mcp_config.json ou Claude Desktop." -ForegroundColor Yellow
    Write-Host "=================================================================" -ForegroundColor Cyan
} catch {
    Write-Error $_.Exception.Message
    exit 1
}
