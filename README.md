# VibeMarketing Skills

Repositório open source de skills para agentes de IA focadas em estratégias reais de VibeMarketing, growth hacking e aquisição de clientes que podem ser sistematizadas, adaptadas e executadas com ajuda de IA.

Este projeto foi criado e disponibilizado pela comunidade [AIEasy](https://aieasy.chat). Para trocar ideias, pedir ajuda e acompanhar novas skills, entre no nosso grupo gratuito do WhatsApp: [Grupo AIEasy no WhatsApp](https://chat.whatsapp.com/IyZeQrXgxuXFfLPjnDtpVj).

## O que é VibeMarketing

VibeMarketing é marketing feito com contexto: entender a comunidade, o canal, a linguagem, a cultura e o momento certo antes de vender. A proposta deste repositório é transformar estratégias práticas de crescimento em skills reutilizáveis para agentes de IA.

As skills aqui devem ajudar agentes a:

- criar campanhas mais naturais e menos genéricas;
- adaptar mensagens para nichos, regiões e comunidades específicas;
- montar planos de conteúdo, prospecção e follow-up;
- automatizar partes repetitivas sem virar spam;
- preservar confiança, transparência e reputação de longo prazo.

## Como usar

Clone o repositório:

```bash
git clone https://github.com/lucaseatp/vibemarketing-skills.git
cd vibemarketing-skills
```

Instale uma skill copiando ou criando um link simbólico da pasta desejada para o diretório de skills do seu agente. No Codex, por exemplo:

```bash
mkdir -p ~/.codex/skills
cp -R facebook-group-authority-sales ~/.codex/skills/
```

Depois, invoque a skill pelo nome em uma conversa com o agente:

```text
Use $facebook-group-authority-sales para criar um plano de 30 dias para um negócio local vender de forma natural em comunidades do Facebook.
```

Você também pode usar as skills como referência para criar seus próprios agentes, playbooks internos, automações de conteúdo ou workflows de growth.

## Skills disponíveis

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

Skill para aplicar a técnica **Community Authority Seeding**, ou **Semeadura de Autoridade Comunitária**: uma abordagem de venda em grupos do Facebook baseada em pertencimento real, participação na comunidade, criação de autoridade e chamadas comerciais leves.

Em vez de entrar em grupos e postar propaganda direta, a estratégia orienta o agente a entrevistar o usuário, entender sua relevância para cada comunidade, pesquisar e ranquear grupos de 0 a 10, registrar regras em `groups/`, mapear pessoas-chave e usar `post-history/` para aprender com posts anteriores. O foco é venda por autoridade, com soft CTA, resposta natural a todos os comentários e cadência respeitosa.

Exemplo de uso:

```text
Use $facebook-group-authority-sales para montar uma estratégia para meu negócio local. Quero grupos relevantes, ranking de comunidades, calendário de posts, ideias de comentários e scripts de resposta para leads.
```

## Estrutura do repositório

```text
vibemarketing-skills/
|-- README.md
|-- LICENSE
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
    |   `-- openai.yaml
    |-- references/
    |-- groups/
    `-- post-history/
```

## Princípios editoriais

- Sem spam: a skill deve priorizar relacionamento, timing e relevância.
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
