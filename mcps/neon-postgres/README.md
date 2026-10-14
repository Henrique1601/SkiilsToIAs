# 🐘 Neon Postgres — Servidor MCP

Servidor de **Model Context Protocol (MCP)** para integração com o **Neon**, a plataforma de banco de dados PostgreSQL serverless com escalonamento automático e branching instantâneo.

---

## 📌 Metadados Técnicos

* **Nome do Servidor:** `mcp-server-neon`
* **Transporte:** Remote SSE via proxy `mcp-remote` ou Streamable HTTP
* **Endpoint Remoto:** `https://mcp.neon.tech/sse`
* **Comando Stdio (Bridge):** `npx -y mcp-remote https://mcp.neon.tech/sse`
* **Principais Recursos:**
  * Criação e deleção de branches de desenvolvimento e teste isoladas a partir do branch principal.
  * Execução de queries SQL de leitura e escrita com segurança transacional.
  * Inspeção completa de schemas, tabelas, índices e tipos de dados.
  * Comparação de diferenças de schema (*schema diff*) entre branches.
  * Monitoramento de queries lentas e recomendações de tuning de performance.

---

## 🛠️ Principais Ferramentas Expostas (*Tools*)

* `run_sql`: Executa comandos SQL no banco de dados ativo.
* `run_sql_transaction`: Executa múltiplos comandos SQL em uma única transação atômica.
* `describe_table_schema`: Retorna a estrutura detalhada de colunas, chaves primárias e estrangeiras de uma tabela.
* `get_database_tables`: Lista todas as tabelas e views presentes no banco.
* `list_branches`: Lista os branches de banco existentes no projeto.
* `create_branch`: Cria um novo branch de banco de dados instantâneo (útil para testes isolados de agentes e PRs).
* `compare_database_schema`: Compara as alterações de DDL entre dois branches.
* `explain_sql_statement`: Gera o plano de execução (`EXPLAIN ANALYZE`) de uma query para otimização de performance.

---

## 🚀 Como Configurar

### No Google Antigravity / Gemini CLI (`mcp_config.json`):
```json
{
  "mcpServers": {
    "mcp-server-neon": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.neon.tech/sse"
      ]
    }
  }
}
```

### No Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "mcp-server-neon": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.neon.tech/sse"
      ]
    }
  }
}
```
