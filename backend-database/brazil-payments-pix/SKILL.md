---
name: brazil-payments-pix
description: "Padrões de integração para pagamentos no Brasil (Pix, Mercado Pago, Asaas, Stripe BR): webhooks idempotentes, HMAC, QR Code Copia e Cola e conciliação."
---

# 💳 Pagamentos Brasil & Pix (`brazil-payments-pix`)

Diretrizes práticas para implementar cobranças via **Pix**, boleto e cartão no Brasil com **idempotência**, **segurança de webhook** e **zero cobrança duplicada**.

## 🎯 Regras Obrigatórias

1. **Idempotência na Criação da Cobrança:**
   - Sempre envie `X-Idempotency-Key` (UUID determinístico do pedido/tentativa) para evitar QR Codes duplicados em retries.
2. **Validação Criptográfica de Webhook:**
   - Nunca confie no payload sem validar a assinatura HMAC/header oficial do gateway (Mercado Pago `x-signature`, Asaas `asaas-access-token`, Stripe `stripe-signature`) usando comparação em tempo constante (`timingSafeEqual`).
3. **Máquina de Estados do Pagamento:**
   - Persista `status` (`pending` → `paid` | `expired` | `refunded`) em transação SQL; ignore eventos repetidos quando o pedido já estiver `paid`.
4. **Expiração & UX de Pix:**
   - Retorne `qr_code` (Copia e Cola) + `qr_code_base64` + `expires_at` (padrão 15–30 min) e atualize a UI via polling curto ou SSE/WebSocket após confirmação do webhook.
5. **TypeSafe AI / Contratos:**
   - Valide payloads de entrada/saída com Zod/Pydantic e nunca exponha `ACCESS_TOKEN` ou chave privada no frontend.
