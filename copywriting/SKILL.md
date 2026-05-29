---
name: copywriting
description: "Escreve, melhora e critica copy persuasiva para landing pages, headlines, ofertas, CTAs, posts sociais, e-mails de nutrição e criativos de valor para anúncios pagos. Use quando o usuário pedir copy, headlines, hooks, subheads, sales pages, texto de landing page, copy de oferta, roteiro de anúncio, criativo de valor ou reescrita de copy. Não use para cold outreach (cold-email), estrutura de campanha Google Ads ou limites de RSA (google-ads), ou posts em grupos do Facebook (facebook-group-authority-sales)."
---

# Copywriting

## Visão geral

Escreva copy de marketing persuasiva, focada em conversão, clara, específica e orientada à ação. Padrão: **valor primeiro** — ensine ou prove algo real antes de pedir o clique, especialmente em anúncios pagos.

Sempre separe:

- **Copy de promessa** — lidera com o resultado (funciona quando há prova e fit fortes).
- **Copy de valor** — lidera com insight, demo ou prova de expertise; vende pela confiança (ver `references/value-ad-creative.md` para anúncios pagos).

Leia `marketing-context.md` se existir antes de fazer perguntas.

## Regras centrais (sempre aplicar)

1. Uma promessa clara — um resultado principal por peça.
2. Um leitor específico — combine nível de consciência e contexto.
3. Benefícios primeiro; recursos só como suporte.
4. Seja específico — números, prazos e restrições vencem adjetivos.
5. Comprove afirmações — depoimentos, resultados, demos, comparações, garantias (somente se confirmados).
6. Trate objeções antes que surjam — preço, esforço, confiança, fit, troca.
7. Torne escaneável — linhas curtas, bullets, subtítulos claros.
8. Mantenha voz e tom consistentes com a marca.
9. Um call to action claro e específico.
10. Edite sem piedade — corte fluff e clichês; clareza acima de esperteza.

## Primeiros passos

1. Se `marketing-context.md` existir, leia.
2. Identifique o tipo de tarefa: copy nova, reescrita, crítica, só headlines, landing page, oferta/CTA, criativo de valor ou bloco padrão.
3. Se faltar informação-chave, faça até **3 perguntas curtas**. Se o contexto estiver claro ou o usuário tiver pressa, declare premissas e prossiga.
4. Carregue só a referência necessária (tabela abaixo).

## Referências

| Arquivo | Quando usar |
| --- | --- |
| `references/headlines-and-hooks.md` | Headlines, hooks, assuntos, aberturas, scroll-stoppers |
| `references/landing-page-copy.md` | Landing pages, sales pages, hero, estrutura de página |
| `references/offer-and-cta.md` | Ofertas, copy de preço, CTAs, garantias, reversão de risco |
| `references/value-ad-creative.md` | Criativo de anúncio que entrega valor antes do pedido (Meta, YouTube, Google vídeo/PMax, short-form) |

Para **RSA do Google Search** (limites de caracteres, pinagem, pré-qualificação), use a skill `google-ads` — aplique ângulos de valor de `value-ad-creative.md` e adapte ao formato RSA em `google-ads/references/search-ads-copy.md`.

## Fluxo: copy nova

1. **Leitor** — quem, consciência (desconhece → mais consciente), dor principal, resultado desejado.
2. **Ângulo** — promessa vs valor (padrão valor para tráfego frio pago e nichos sensíveis à reputação).
3. **Prova** — só fatos confirmados; marque lacunas como `[PROVA NECESSÁRIA]` se rascunho for permitido.
4. **Rascunho** — siga o formato pedido ou a saída padrão (abaixo).
5. **Corte** — remova linhas genéricas que qualquer concorrente poderia usar.

## Fluxo: crítica ou reescrita

1. Diagnostique os maiores riscos de conversão (promessa vaga, leitor errado, prova fraca, CTA enterrado, tom de anúncio).
2. Entregue a copy revisada.
3. Indique brevemente o que mudou e um teste a rodar em seguida.

Em tarefas de crítica/revisão, inclua diagnóstico. Em entrega pura de copy, siga as regras de saída abaixo.

## Saída padrão (quando o formato não for especificado)

Forneça, nesta ordem:

1. Headline (1–3 opções)
2. Subheadline (1–2 opções)
3. Bullets de benefícios (3–7)
4. Prova / credibilidade (quando aplicável)
5. Tratamento de objeções (FAQ curto ou linhas de redução de risco)
6. CTA primário + CTA secundário

## Regras de saída

**Quando o usuário pedir só a copy final:**

- Entregue **apenas** a copy — sem explicações ou meta comentário.
- Texto simples. Sem tags HTML. Evite tabelas, salvo se o usuário pedir.
- Se o usuário pedir um formato, siga exatamente.

**Quando pedir crítica, estratégia ou opções com rationale:**

- Inclua diagnóstico, copy revisada e teste recomendado.

Escreva entregas no idioma de trabalho do usuário, salvo se ele pedir outro.

## Limites

Nunca:

- Invente depoimentos, resultados, números, garantias ou alegações de compliance.
- Prometa resultados sem prova confirmada.
- Use hype que prejudique reputação (“fique rico da noite pro dia”, curas milagrosas, urgência falsa).
- Copie filler genérico de IA que qualquer concorrente usaria.

Prefira:

- Ângulos valor primeiro em tráfego pago — ensine o caminho, depois convide o próximo passo.
- Especificidade acima de superlativos.
- Um CTA primário por seção.
- Message match entre anúncio/copy e landing page.

## Exemplos

**Usuário:** "Escreve hero copy do meu SaaS de contabilidade para PMEs."

→ Leia `marketing-context.md` se existir → `references/landing-page-copy.md` → bloco de saída padrão.

**Usuário:** "10 opções de headline para campanha local de pet shop."

→ `references/headlines-and-hooks.md` → ângulo de valor (dicas, transparência do processo) se tráfego pago.

**Usuário:** "Roteiro de anúncio de valor de 90s a partir do meu corte de podcast sobre Google Ads."

→ `references/value-ad-creative.md` → hook nos primeiros 5 segundos → CTA suave no final → destino alinhado ao tema.
