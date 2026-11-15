# ☁️ Google Cloud Run MCP Server (`cloudrun`)

Servidor oficial do **Google Cloud Run MCP** (`@google-cloud/cloud-run-mcp`) para listar projetos/serviços, inspecionar logs e publicar containers ou pastas locais no Cloud Run.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Local via `npx`)
- **Pacote:** `@google-cloud/cloud-run-mcp`
- **Autenticação:** Credenciais locais do `gcloud` (`GOOGLE_APPLICATION_CREDENTIALS` ou `gcloud auth application-default login`).

```json
{
  "mcpServers": {
    "cloudrun": {
      "command": "npx",
      "args": ["-y", "@google-cloud/cloud-run-mcp"]
    }
  }
}
```

## 🛠️ Principais Capacidades
- `list_projects` / `create_project`
- `list_services` / `get_service` / `get_service_log`
- `deploy_local_folder` / `deploy_file_contents` / `deploy_container_image`
