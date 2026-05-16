---
name: marketing-context
description: "Create, refresh, audit, or consolidate a shared marketing-context.md file for a company even when source material is incomplete or scattered. Use from business notes, conversations, interviews, websites, app files, pricing facts, existing docs, campaign materials, customer research, or direct discovery questions. Use when Codex needs a reusable source of truth for marketing skills, including business snapshot, offer, ICP, customer pains, positioning, proof, brand voice, channels, CTAs, constraints, assumptions, and open questions."
---

# Marketing Context

## Overview

Use this skill to create and maintain a single `marketing-context.md` file that other marketing skills can read before producing campaigns, copy, outreach, content, landing pages, or sales assets.

The user will often not have organized business foundation docs. That is expected. Create the most useful central context possible from whatever exists: a short conversation, a website, rough notes, product files, an offer description, or a discovery interview.

The goal is not to create a full business documentation folder. The goal is to distill or elicit the business foundation into one practical, human-readable context file that prevents repeated discovery questions and keeps marketing output consistent.

## Default Output

Default to creating or updating `marketing-context.md` at the current workspace root unless the user specifies another path.

The file should be:

- Concise enough to read before doing marketing work.
- Specific enough to guide execution.
- Honest about confidence: separate confirmed facts, assumptions, hypotheses, and open questions.
- Written in the user's working language unless they request another language.
- Useful for downstream skills such as cold email, Facebook group sales, content strategy, landing pages, ads, offers, brand voice, and positioning.

## Workflow

1. Establish the destination.
   - If the user gives a path, use it.
   - If `marketing-context.md` already exists, update it instead of replacing it blindly.
   - If no path exists, create `marketing-context.md` in the current workspace root.

2. Inventory source material before writing.
   - Read existing `marketing-context.md` first.
   - Look for docs such as `briefing-marketing.md`, `briefing-geral.md`, `perfil-cliente-ideal.md`, `proposta-de-valor-posicionamento.md`, `branding-foundation.md`, `plans-pricing.md`, `business-blueprint.md`, and `assumptions-and-open-questions.md` when they exist.
   - Read relevant site, app, pricing, product, README, campaign, sales, or onboarding files when they may contain live facts.
   - Use user-provided notes, transcripts, interviews, and strategy conversations as source material.
   - If little or no source material exists, run a focused discovery interview instead of waiting for perfect documents.

3. Load the right reference.
   - Use `references/marketing-context-blueprint.md` when creating or restructuring the file.
   - Use `references/extraction-and-synthesis.md` when turning messy sources, sparse context, or a discovery interview into clean context.

4. Separate fact from interpretation.
   - Mark facts as confirmed only when the source supports them.
   - Mark uncertain items as assumptions, hypotheses, or questions.
   - Never invent prices, guarantees, results, compliance claims, customer names, or proof points.

5. Synthesize for action.
   - Convert raw business docs into marketing-useful language: audience, problem, trigger, value, proof, offer, voice, channel, CTA, constraints.
   - When evidence is thin, still write a useful best-current version and label it clearly.
   - Keep the file practical. Prefer "how to use this in marketing" over abstract definitions.
   - Avoid turning the file into a generic consulting document.

6. Validate before finishing.
   - Check that `marketing-context.md` exists.
   - Search for stale company names, placeholder text, copied example names, contradictory ICPs, unsupported claims, and uncertain pricing.
   - Ensure every key uncertainty appears in an "Open Questions" or "Assumptions" section.

## Update Rules

When updating an existing `marketing-context.md`:

- Preserve useful sections and naming that downstream skills may already rely on.
- Merge new evidence into the right section instead of appending disconnected notes at the bottom.
- Keep old facts only when they still seem current; otherwise move them to assumptions or open questions.
- Add a short source note when a claim depends on a specific file, page, interview, or user statement.
- Do not erase uncertainty to make the document look more complete.

## Discovery Interview

When the user has no existing docs, ask the smallest set of questions needed to create a useful first version. Prefer one compact batch instead of a long interrogation:

1. What is the company/product and what does it sell?
2. Who is the best-fit customer, and who is not a fit?
3. What painful problem or desired outcome makes them buy?
4. What offer, package, price, or CTA exists today?
5. What proof, results, testimonials, credentials, or examples are safe to mention?
6. What should the brand sound like, and what should it avoid?
7. Which channels or campaigns matter right now?

If the user answers partially, create `marketing-context.md` anyway. Put missing items in `Assumptions And Open Questions`, and make the next questions specific enough to improve the next version.

## Quality Bar

A strong `marketing-context.md` should let another agent answer these questions without asking the user again:

- What does this business sell, to whom, and why now?
- Who is the best-fit customer and who is not a fit?
- What problem, pain, job, or desire drives action?
- What outcome or transformation is promised?
- What proof is safe to use?
- How should the brand sound?
- What offers, pricing, CTAs, and conversion paths exist?
- What channels and campaigns are active or planned?
- What claims, audiences, geographies, or tactics should be avoided?
- What still needs validation?

## Deliverables

For creation or refresh requests, deliver:

- Updated or newly created `marketing-context.md`.
- Brief summary of the strongest confirmed context.
- Open questions or assumptions that matter for future marketing work.
- Source gaps, especially around pricing, proof, compliance, or ICP.

For audit requests, deliver:

- Gaps and contradictions found.
- Recommended edits.
- Optional rewritten `marketing-context.md` when the user asks for implementation.
