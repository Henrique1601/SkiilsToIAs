---
name: n8n-whatsapp-automation
description: "Padrões de automação com n8n e WhatsApp (Cloud API oficial ou Evolution API): webhooks seguros, fila com retry, dedupe de mensagens e limites anti-ban."
---

# 🤖 Automação n8n & WhatsApp (`n8n-whatsapp-automation`)

Padrões confiáveis para fluxos de atendimento, notificações e agentes via **n8n** e **WhatsApp** sem loops infinitos ou bloqueio de número.

## 🎯 Boas Práticas Obrigatórias

1. **Deduplicação & Anti-Loop:**
   - Ignore mensagens `fromMe === true` e armazene `message_id` com TTL (Redis/SQLite) antes de processar o webhook para evitar reprocessamento em retries.
2. **Webhook Rápido (200 OK Imediato):**
   - Responda `200 OK` ao webhook antes de chamar LLMs ou APIs lentas; enfileire o processamento assíncrono para evitar timeouts e reenvios em cascata.
3. **Respeito a Rate Limits & Janela de 24h:**
   - Na WhatsApp Cloud API oficial, use templates aprovados fora da janela de 24h; em envios em lote, aplique jitter/delay e opt-out explícito.
4. **Segurança & Credenciais:**
   - Valide token secreto no header do webhook, nunca versionar credenciais de instância nos JSONs exportados do n8n (`workflows/*.json`).
5. **Fallback Humano:**
   - Sempre preveja palavra-chave ou erro crítico que encaminha a conversa para atendimento humano e registra o evento em log.
