# 🔬 REA (Reverse Engineering Agent) — Servidor MCP

Servidor especializado de **Model Context Protocol (MCP)** para engenharia reversa de software, desmontagem e análise de segurança de binários nativos, aplicativos compilados e artefatos de sistema.

---

## 📌 Metadados Técnicos

* **Nome do Servidor:** `rea`
* **Transporte:** Stdio (Local Node/npx)
* **Pacote npm:** `rea-agents@6.0.0`
* **Comando:** `npx -y rea-agents@6.0.0 mcp`
* **Formatos Suportados:** Executáveis PE (Windows .exe/.dll), Mach-O (macOS/iOS), ELF (Linux), APK/DEX (Android) e Web Bundles.

---

## 🛠️ Principais Ferramentas Expostas (*Tools*)

* `binary_overview`: Extrai arquitetura, seções, símbolos exportados e metadados de cabeçalho do executável.
* `procedure_assembly` & `procedure_pseudo_code`: Desmonta instruções assembly e decompila funções para pseudocódigo C-like legível.
* `procedure_callees` & `procedure_callers`: Mapeia o grafo de chamadas de funções.
* `search_strings`: Localiza strings embutidas no binário (URLs, endpoints, chaves, mensagens de erro).
* `inspect_signature`: Valida assinaturas digitais, certificados e integridade de código.
* `inspect_native_api`: Analisa chamadas a APIs nativas do sistema operacional para detecção de comportamento de risco.

---

## 🚀 Como Configurar

### No Google Antigravity / Gemini CLI (`mcp_config.json`):
```json
{
  "mcpServers": {
    "rea": {
      "command": "npx",
      "args": [
        "-y",
        "rea-agents@6.0.0",
        "mcp"
      ]
    }
  }
}
```

### No Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "rea": {
      "command": "npx",
      "args": [
        "-y",
        "rea-agents@6.0.0",
        "mcp"
      ]
    }
  }
}
```
