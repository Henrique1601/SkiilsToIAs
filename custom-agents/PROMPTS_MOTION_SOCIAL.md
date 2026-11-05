# 🎬 Catálogo de Prompts de Motion & Vídeo para Redes Sociais

Este catálogo padroniza os **10 estilos de prompts de alto impacto** para geração de vídeos em código (HTML/GSAP/Remotion), teasers de produto, vinhetas e publicações para **LinkedIn** e **Instagram**.

Ambos os agentes **`social-publisher-agent`** e **`video-producer-agent`** operam este catálogo, permitindo que a IA sugira proativamente o melhor formato baseado no tipo do projeto, ou ofereça uma seleção interativa ao usuário via `ask_question`.

---

## 🧭 Matriz de Recomendação Inteligente por Tipo de Projeto

| Tipo de Projeto / Contexto | Prompt Recomendado | Estilo Visual & Duração |
|---|:---:|---|
| **SaaS Web / Ferramentas Digitais** | **Estilo 1 (Apresentação de App)** | 30s, P&B minimalista, headlines dinâmicas, reveal de UI |
| **Biblioteca de Código, UI Kit, Motion System** | **Estilo 2 (Showreel de Motion)** | 15s, educativo, princípios de animação, anotações manuscritas |
| **Aplicativo Mobile (iOS / Android)** | **Estilo 3 (Lançamento de App Store)** | 30s, iPhone 3D flutuando, cards saltando, blur cinemático |
| **Produto Físico, Gadget, Setup ou Hardware** | **Estilo 4 (Produto em Destaque)** | 15s, 3D rotativo como protagonista, duas cores fortes, cards de specs |
| **Portfólio Pessoal, Criador, Freelancer, Bio** | **Estilo 5 (Motion de Apresentação Pessoal)** | 15s, wipes/íris, contadores de métricas, foto em círculo, CTA seguir |
| **Vinheta de Marca, Início de Vídeo, Branding** | **Estilo 6 (Logo Reveal Animado)** | 6s vinheta, partículas convergindo, linhas do logo, flash de luz |
| **Passo a Passo Técnico, Pipeline, Composição Modular** | **Estilo 7 (Montagem Camada por Camada)** | Plano contínuo visto de cima, contadores, spring physics, trilha no beat |
| **Marketplace, Turismo, Serviços, Experiências** | **Estilo 8 (Anúncio de Serviços / Experiências)** | Plano contínuo, elementos metamorfoseiam, travel/service flow |
| **App com Dashboard Denso, FinTech, IA, Editorial** | **Estilo 9 (Apresentação Editorial de App)** | Serifada elegante + itálico colorido, grid 3D, scanner de dados |
| **Lançamento Premium de Alta Linha (Hardware / Luxo)** | **Estilo 10 (Keynote Estilo Apple)** | 27s 60fps a 120 BPM, sem cortes, vidro líquido, plano-sequência fluido |

---

## 📝 Os 10 Prompts de Produção Prontos para Uso

### 1. Apresentação de App (Minimalista P&B)
> **PROMPT:**  
> "CRIE EM HTML (1920X1080, FUNDO PRETO, GSAP) UM MOTION DE 30S ESTILO LANÇAMENTO DE APP: MINIMALISTA P&B, HEADLINES GRANDES COM REVEAL PALAVRA POR PALAVRA, MOCKUPS DE UI, TRANSIÇÕES RÁPIDAS COM ECHO TRAIL E SEM CORTES SECOS. MARCA: [NOME] | LOGO: [LOGO] | TAGLINE: [TAGLINE] CENAS: ABERTURA COM O LOGO → [FRASE 1] → [FRASE 2] → [FRASE 3] → [FRASE 4] → [FRASE 5] → ELEMENTOS FORMAM O LOGO → LOGO + TAGLINE. CRIE A UI DE CADA CENA DE ACORDO COM A FRASE."

---

### 2. Showreel de Motion (Educativo & Princípios)
> **PROMPT:**  
> "CRIE EM HTML (16:9, GSAP) UM SHOWREEL DE MOTION DESIGNER DE 15S QUE ENSINA PRINCÍPIOS DE ANIMAÇÃO. VISUAL: FUNDO ALTERNANDO CINZA CLARO E GRAFITE, FONTE CONDENSADA PESADA, AZUL E VERMELHO DE DESTAQUE, ANOTAÇÕES MANUSCRITAS COM SETINHAS. CENAS: BOLINHA QUICANDO COM RASTRO (SQUASH & STRETCH) → VIRA O PONTO FINAL DE \"[FRASE DE ABERTURA].\" → PALAVRAS ANIMADAS PELO PRÓPRIO SIGNIFICADO: [PALAVRA 1], [PALAVRA 2], [PALAVRA 3], [PALAVRA 4] → GRÁFICO DE EASING (LINEAR X EASE IN-OUT) → COBRINHA DE PONTOS NUM GRID (FOLLOW-THROUGH) → DIAL CARREGANDO ATÉ 100% (ANTICIPATION) → \"[CARGO] / [NOME].\" + NOTA MANUSCRITA \"[CTA]\"."

---

### 3. Lançamento de App (Estilo App Store 3D)
> **PROMPT:**  
> "CRIE EM HTML (1920X1080, GSAP) UM VÍDEO PROMOCIONAL DE APP DE 30S, ESTILO LANÇAMENTO DA APP STORE: FUNDO ESCURO COM BRILHO COLORIDO, IPHONE 3D FLUTUANDO, HEADLINE COM PALAVRA-CHAVE EM [COR], ZOOM NA TELA, CARDS SALTANDO DO CELULAR E TRANSIÇÕES COM BLUR. APP: [NOME] | LOGO: [LOGO] | TAGLINE: [TAGLINE] CENAS: [FRASE 1] → [FRASE 2] → [FRASE 3] → [FRASE 4] → [FRASE 5] → CELULARES EM LEQUE → LOGO + TAGLINE. CRIE A TELA DO APP DE CADA CENA DE ACORDO COM A FRASE."

---

### 4. Produto em Destaque (3D Rotativo & Specs)
> **PROMPT:**  
> "CRIE EM HTML (1920X1080, GSAP) UM COMERCIAL DE 15S PARA [PRODUTO]: DUAS CORES ([COR] E QUASE PRETO), TIPOGRAFIA EXTRA BOLD EM CAIXA ALTA, O PRODUTO EM 3D GIRANDO COMO PROTAGONISTA, TRANSIÇÕES RÁPIDAS COM MOTION BLUR E ECHO TRAIL. MARCA: [NOME] | LOGO: [LOGO] | TAGLINE: [TAGLINE] CENAS: PONTINHO EXPLODE NA TELA → [FRASE 1] → CLOSE NOS DETALHES DO PRODUTO → [FRASE 2] COM O PRODUTO GIRANDO → [BENEFÍCIO 1] E [BENEFÍCIO 2] APARECENDO EM CARDS AO REDOR DO PRODUTO → [FRASE 3] → [PALAVRA 1] [PALAVRA 2] [PALAVRA 3] → LOGO + TAGLINE."

---

### 5. Motion de Apresentação Pessoal & Autoridade
> **PROMPT:**  
> "CRIE EM HTML (1920X1080, GSAP) UM VÍDEO DE APRESENTAÇÃO PESSOAL DE 15S: FUNDO PRETO ALTERNANDO COM [COR], TIPOGRAFIA BOLD COM UMA PALAVRA POR FRASE EM ITÁLICO SERIFADO COLORIDO, TRANSIÇÕES COM WIPES E ÍRIS, NÚMEROS COM COUNT-UP. DADOS: [NOME] | [CARGO] | FOTO: [FOTO] | INSTAGRAM: [@] CENAS: LINHA VIRA PÍLULA QUE FORMA O \"O\" DO NOME → FOTO EM CÍRCULO COM TEXTO GIRANDO + [FRASE DE IMPACTO] → [DESTAQUE 1], [DESTAQUE 2] E [DESTAQUE 3] COM INFOGRÁFICOS ANIMADOS → FOTO + NOME + [CTA] COM BOTÃO \"SEGUIR\" SENDO CLICADO."

---

### 6. Logo Reveal Animado (Vinheta de Estúdio)
> **PROMPT:**  
> "CRIE UM MOTION (16:9) DE 6S ESTILO VINHETA DE ESTÚDIO: FUNDO [COR], FORMAS GEOMÉTRICAS QUE SE ENCAIXAM COM OVERSHOOT, PARTÍCULAS CONVERGINDO PARA O CENTRO, FLASH DE LUZ E MOTION BLUR. MARCA: [NOME] | LOGO: [LOGO] | TAGLINE: [TAGLINE] CENAS: PONTO DE LUZ → LINHAS DESENHAM O CONTORNO DO LOGO → FORMAS SE ENCAIXAM → BRILHO VARRE O LOGO COMPLETO → TAGLINE SURGE LETRA POR LETRA."

---

### 7. Montagem de Receita / Camada por Camada (Plano Contínuo)
> **PROMPT:**  
> "CRIE UM MOTION GRAPHICS EM HTML DE [DURAÇÃO] MOSTRANDO [PRODUTO] SENDO MONTADO CAMADA POR CAMADA, FORMATO 16:9, 30 FPS, EM PLANO CONTÍNUO, COM ILUSTRAÇÃO VISTA DE CIMA. ESTILO: FUNDO [COR/TEXTURA], BORDAS [EX.: TOALHA XADREZ], CORES [COR], FONTE CONDENSADA BOLD, PRODUTO À ESQUERDA E TEXTO À DIREITA, ANIMAÇÕES COM SPRING. ROTEIRO: BASE + TÍTULO \"[FRASE]\" → CAMADAS ANIMADAS COM CONTADOR (\"[3] COLHERES DE [MOLHO]\", \"[150 G] DE [QUEIJO]\", \"[12] FATIAS DE [PEPPERONI]\") → [TRANSFORMAÇÃO, EX.: FORNO] → PRODUTO PRONTO → FINAL \"[FRASE FINAL]\". TRILHA [ESTILO] COM TRANSIÇÕES NO BEAT."

---

### 8. Anúncio de Viagens & Serviços (Metamorfose Visual)
> **PROMPT:**  
> "CRIE UM MOTION GRAPHICS EM HTML DE [DURAÇÃO] PARA A AGÊNCIA DE VIAGENS [NOME DA AGÊNCIA], FORMATO 16:9, 30 FPS, EM PLANO CONTÍNUO: CADA ELEMENTO SE TRANSFORMA NO PRÓXIMO. ESTILO: FUNDO [COR/TEXTURA], CORES [COR], FONTE [NOME], ANIMAÇÕES COM SPRING, TOM [LEVE | PREMIUM | AVENTUREIRO]. FIO CONDUTOR: [EX.: AVIÃOZINHO COM TRILHA PONTILHADA]. ROTEIRO: BUSCA POR \"[DESTINO]\" → PROMESSA \"[FRASE]\" → SERVIÇOS COM CHECK ([PASSAGENS, HOSPEDAGEM, PASSEIOS]) → 3 DESTINOS EM TELA CHEIA → LOGO + \"[SLOGAN]\" + BOTÃO \"[CTA]\". TRILHA [ESTILO] COM TRANSIÇÕES NO BEAT. USE AS FOTOS E O LOGO ANEXADOS. ENTREGUE O VÍDEO FINAL E UM CONTACT SHEET (1 QUADRO A CADA 0,5 S)."

---

### 9. Apresentação de App (Estilo Editorial & FinTech)
> **PROMPT:**  
> "CRIE UM MOTION GRAPHICS EM HTML DE [DURAÇÃO] PARA O APP [NOME], FORMATO 16:9, 30 FPS, EM PLANO CONTÍNUO: CADA ELEMENTO SE TRANSFORMA NO PRÓXIMO. ESTILO: EDITORIAL, FONTE SERIFADA COM A PALAVRA-CHAVE EM ITÁLICO COLORIDO, CORES [CORES], ÍCONES DE LINHA, CARDS, MOCKUP DE CELULAR, TRANSIÇÕES COM BLUR E SPRING. ROTEIRO: UM ÍCONE SE MULTIPLICA NUMA GRADE DE ÍCONES DE [CATEGORIA DO PRODUTO] QUE SE CURVA EM 3D SOBRE FUNDO ESCURO + \"[FRASE DO PROBLEMA]\"; UM CÍRCULO DE LUZ FILTRA A GRADE, O FUNDO CLAREIA E SOBRAM SÓ [ITENS PRINCIPAIS] + \"[FRASE DE SOLUÇÃO]\"; OS ITENS ENTRAM NUM CELULAR E O APP GERA [RESULTADO DO APP] A PARTIR DE UM PEDIDO DIGITADO + \"[FRASE DE PERSONALIZAÇÃO]\"; UMA FOTO É ESCANEADA E OS ITENS VOAM PARA CARDS DE [CATEGORIAS] + \"[FRASE DE ORGANIZAÇÃO]\"; [AMBIENTE FINAL] ISOMÉTRICO SE MONTA ENQUANTO UM CONTADOR VAI DE 0 A 100% + \"[FRASE DE RESULTADO]\"; TUDO VIRA O LOGO [NOME] + [SLOGAN] + [SITE]."

---

### 10. Vídeo de Lançamento (Estilo Keynote Apple)
> **PROMPT:**  
> "CRIE UM VÍDEO DE LANÇAMENTO DE [PRODUTO] A PARTIR DA FOTO ANEXADA: 16:9, 27 S, 60 FPS, EM LOOP, TEXTOS EM PORTUGUÊS. ESTILO KEYNOTE DA APPLE, SÓ 2D, UM PLANO-SEQUÊNCIA A 120 BPM, SEM CORTES NEM FADES: CADA CENA SE TRANSFORMA NA PRÓXIMA. FUNDO OFF-WHITE, INTERFACE PRETA, VIDRO LÍQUIDO E UM CURSOR FAZENDO CADA CLIQUE. ROTEIRO: TÍTULO \"[PALAVRA].\" → GRADE DE DETALHES → ZOOM EM [DETALHE] NO DROP → CLOSE DA TEXTURA COM CONTROLE DE VIDRO → TELA DE CELULAR → PÁGINA DE PRODUTO COM OPÇÕES → PEDIDO ENTREGUE → PRODUTO EM [AMBIENTE] → VOLTA AO TÍTULO. USE SEMPRE A FOTO REAL DO PRODUTO, SEM DISTORCER E SEM INVENTAR MARCA, PREÇO OU ESPECIFICAÇÕES. GERE MÚSICA E EFEITOS SONOROS SE EU NÃO MANDAR. MOSTRE 4 QUADROS DE PRÉVIA ANTES DO VÍDEO FINAL."

---

## 🤖 Protocolo de Interação com o Usuário

Ao ser solicitado para gerar um post ou vídeo, o agente deve:
1. **Análise Proativa da Stack/Projeto:** Identificar a natureza do projeto (`package.json`, `.exe`, tipo de produto).
2. **Recomendação com Justificativa:**
   *"Analisando o projeto [X], recomendo o **Estilo 1 (Apresentação Minimalista de App)** ou **Estilo 10 (Keynote Apple)** porque valoriza as microinterações e o visual dark do produto."*
3. **Pergunta Interativa:** Utilizar `ask_question` oferecendo a recomendação em primeiro lugar mais as alternativas relevantes, permitindo ao usuário escolher ou pedir customização.
4. **Preenchimento Automático das Variáveis:** Substituir automaticamente `[NOME]`, `[LOGO]`, `[TAGLINE]`, `[FRASE 1..5]` com dados reais extraídos do `README.md` e do repositório.
