# VibeMarketing Skills

Skills open source para agentes de IA aplicarem estratégias reais de VibeMarketing, growth hacking e aquisição de clientes com mais contexto, menos spam e melhor adaptação a cada canal.

Este projeto foi criado e disponibilizado pela comunidade [AIEasy](https://aieasy.chat). Para trocar ideias, pedir ajuda e acompanhar novas skills, entre no nosso grupo gratuito do WhatsApp: [Grupo AIEasy no WhatsApp](https://chat.whatsapp.com/IyZeQrXgxuXFfLPjnDtpVj).

## Instalação

A forma mais simples de instalar as skills é usar o CLI de Skills:

```bash
npx skills add lucaseatp/vibemarketing-skills
```

Depois da instalação, invoque uma skill pelo nome na conversa com o agente:

```text
Use $marketing-context para criar um contexto de marketing para minha empresa.
Use $cold-email para montar uma sequência B2B de 3 emails.
Use $facebook-group-authority-sales para vender em grupos do Facebook sem spam.
```

## Instalação manual

Se preferir instalar manualmente, clone o repositório:

```bash
git clone https://github.com/lucaseatp/vibemarketing-skills.git
cd vibemarketing-skills
```

Copie a pasta da skill desejada para o diretório de skills do seu agente. No Codex, por exemplo:

```bash
mkdir -p ~/.codex/skills
cp -R marketing-context ~/.codex/skills/
cp -R cold-email ~/.codex/skills/
cp -R facebook-group-authority-sales ~/.codex/skills/
```

## O que é VibeMarketing

VibeMarketing é marketing feito com contexto: entender a comunidade, o canal, a linguagem, a cultura e o momento certo antes de vender.

A proposta deste repositório é transformar estratégias práticas de crescimento em skills reutilizáveis para agentes de IA. As skills aqui ajudam agentes a:

- criar campanhas mais naturais e menos genéricas;
- adaptar mensagens para nichos, regiões e comunidades específicas;
- montar planos de conteúdo, prospecção e follow-up;
- automatizar partes repetitivas sem virar spam;
- preservar confiança, transparência e reputação de longo prazo.

## Skills disponíveis

### marketing-context

Cria, atualiza ou consolida um arquivo `marketing-context.md` com a base de marketing de uma empresa: oferta, ICP, dores, posicionamento, provas, voz, canais, CTAs, restrições, hipóteses e perguntas em aberto.

Use antes de outras skills quando o agente ainda não tem contexto suficiente sobre o negócio.

```text
Use $marketing-context para criar um contexto de marketing para minha empresa a partir destas anotações.
```

### cold-email

Ajuda a escrever, revisar, planejar e dimensionar campanhas B2B de cold email. Inclui sequências de 3 emails, follow-ups, diagnóstico de copy, planejamento de capacidade, domínios, inboxes, warmup e limites de envio.

```text
Use $cold-email para criar uma sequência de 3 emails para vender minha consultoria para empresas SaaS B2B.
```

### copywriting

Skill (PT) para **escrever, melhorar e criticar copy persuasiva** — landing pages, headlines, ofertas, CTAs e criativos de valor para anúncios pagos. Integra com `marketing-context.md`. Não cobre cold email, estrutura Google Ads ou posts em grupos do Facebook.

Exemplo:

```text
Use $copywriting para escrever a hero copy da minha landing page SaaS. Ângulo de valor, tenho marketing-context.md.
```

### meta-ads

Skill (English) to **analyze, plan, and optimize Meta Ads** — C-A-A structures, scale ecosystem, cost cap, Feed/Reels/Stories, **SaaS strategy** (test→validate→scale, demo, LTV). Integrates MCP when available.

References: `caa-strategy`, `scale-ecosystem`, `cost-cap-low-ticket`, `channels-formats-creative`, `saas-meta-ads`. Copy: `copywriting` skill.

Example:

```text
Use $meta-ads to build Meta strategy for my SaaS. $97/mo ticket, I have a video demo and purchase pixel.
```

### google-ads

Skill (English) to plan, structure, write, audit, and optimize **Google Ads** campaigns (Search, Performance Max, Display, Video, Demand Gen). USD tiers: low (&lt;200/day), medium (~200/day), high (~400/day), very high (≥20k/month). Search → PMax order, CRM-qualified leads (not CPL alone), PMax as scale/complement.

Integrates with `marketing-context.md`. References: structure/bidding, copy/AI Max, Performance Max, tracking/value rules, optimization checklist.

Example:

```text
Use $google-ads to build Search campaigns for my clinic in NYC. Budget US$ 200/day, goal is appointments. I have marketing-context.md.
```

### facebook-group-authority-sales

Aplica a técnica **Community Authority Seeding**, ou **Semeadura de Autoridade Comunitária**: venda em grupos do Facebook baseada em pertencimento real, participação na comunidade, criação de autoridade e CTAs leves.

Em vez de entrar em grupos e postar propaganda direta, a skill orienta o agente a entrevistar o usuário, entender a relevância da oferta para cada comunidade, pesquisar e ranquear grupos de 0 a 10, registrar regras em `groups/`, mapear pessoas-chave e usar `post-history/` para aprender com posts anteriores.

```text
Use $facebook-group-authority-sales para montar uma estratégia para meu negócio local. Quero grupos relevantes, ranking de comunidades, calendário de posts, ideias de comentários e scripts de resposta para leads.
```

## Estrutura do repositório

```text
vibemarketing-skills/
|-- README.md
|-- LICENSE
|-- marketing-context/
|   |-- SKILL.md
|   |-- agents/
|   `-- references/
|-- cold-email/
|   |-- SKILL.md
|   |-- scripts/
|   |-- agents/
|   `-- references/
|-- copywriting/
|   |-- SKILL.md
|   |-- agents/
|   `-- references/
|-- meta-ads/
|   |-- SKILL.md
|   |-- agents/
|   `-- references/
|-- google-ads/
|   |-- SKILL.md
|   `-- references/
|       |-- performance-max.md
|       `-- ...
`-- facebook-group-authority-sales/
    |-- SKILL.md
    |-- agents/
    |-- references/
    |-- groups/
    `-- post-history/
```

## Princípios editoriais

- Sem spam: priorizar relacionamento, timing e relevância.
- Sem falsidade: não inventar identidade, experiência, depoimento ou prova social.
- Sem automação abusiva: evitar mass posting, scraping indevido e mensagens diretas em escala sem consentimento.
- Com adaptação local: nicho, cidade, cultura do grupo e regras da comunidade importam.
- Com foco em resultado: cada skill deve produzir planos, copies, cadências ou critérios que um operador consiga usar na vida real.

## Como contribuir

1. Crie uma nova pasta de skill com nome em `kebab-case`.
2. Inclua um `SKILL.md` com frontmatter `name` e `description`.
3. Mantenha a skill objetiva, prática e reutilizável.
4. Adicione exemplos de prompts reais no corpo da skill quando isso ajudar o agente.
5. Evite documentação extra dentro da pasta da skill; use o README principal para contexto do repositório.
6. Abra um pull request explicando o caso de uso, o público-alvo e o tipo de automação que a skill melhora.

## Comunidade

AIEasy é a comunidade por trás deste repositório. Conheça em [aieasy.chat](https://aieasy.chat) e participe do [grupo gratuito do WhatsApp](https://chat.whatsapp.com/IyZeQrXgxuXFfLPjnDtpVj).
