---
name: meta-ads
description: "Analyzes, plans, and optimizes Meta Ads/Facebook Ads campaigns: C-A-A structures (1-1-3, 1-3-3, 1-3-1, 1-1-1), scale ecosystem, cost cap, channels (Feed/Reels/Stories), SaaS, and value-first creative. Use for Meta Ads, Facebook Ads, Ads Manager, campaign strategy, creative tests, ROAS, CPA, CTR, CPM, scaling, or paid social. Integrates MCP when available."
---

# Meta Ads

## Objective

Analyze, structure, and recommend actions for Meta Ads — via MCP data or user-provided context — covering C-A-A structure, account phase, performance, creatives, hypotheses, and a prioritized plan.

## References

| File | When |
| --- | --- |
| `references/caa-strategy.md` | Account phases, 1-1-1/1-1-3/1-3-1/1-3-3 notation, CBO vs ABO, migrations |
| `references/scale-ecosystem.md` | Campaign ecosystem, daily scaling, creative testing, ticket, multiple offers |
| `references/cost-cap-low-ticket.md` | Ticket < ~$20 USD equivalent, static budget, cost cap / target cost |
| `references/channels-formats-creative.md` | Feed, Reels, Stories, image vs video, WhatsApp vs LP |
| `references/saas-meta-ads.md` | SaaS/digital tool: test→validate→scale, demo, LTV, stack, creatives |

For value-ad scripts and copy: `copywriting` skill → `references/value-ad-creative.md`.

## Before Pulling Data

Confirm or identify:

1. Ad account, campaign, or scope to analyze.
2. Primary period and comparison period.
3. Business goal: leads, sales, acquisition, remarketing, awareness, or other.
4. Primary conversion event and attribution window.
5. Currency, timezone, and CPA, CAC, CPL, or ROAS targets.
6. Account phase: discovery, consolidation, scale, or maintenance.
7. Current or desired C-A-A structure (Campaign-Ad Set-Ad).
8. Offer type: info product, SaaS, e-commerce, local, service.

If information is missing, proceed with clear assumptions or ask focused questions.

## MCP Flow

1. Discover MCP tools for Meta Ads / Ads Manager.
2. Read tool schema before any call.
3. Fetch when available: accounts, campaigns, ad sets, ads, creatives, daily metrics, breakdowns, conversions, ROAS, delivery status, bids.
4. Without MCP: state the blocker and request Ads Manager export or manual data. Never invent numbers.

## Priority Metrics

- Spend, impressions, reach, frequency, CPM.
- Clicks, CTR, CPC, cost per LPV.
- Conversions, CPA, CPL, CAC, ROAS.
- Revenue, AOV/ticket, margin (when provided).
- Daily trends and fatigue signals (frequency, CTR, CPM, CPA).

Separate platform, site/CRM, and inferred metrics. Flag tracking gaps.

## Diagnosis

1. Tracking: pixel/CAPI, event, UTMs.
2. C-A-A structure and phase — `caa-strategy.md`.
3. Funnel: CPM → CTR → CPC → CVR → CPA/ROAS.
4. Creatives: hook, format, fatigue, angles.
5. Scale vs saturation — `scale-ecosystem.md`.
6. Cut: what drains budget without return.

For **SaaS**, cross-check `saas-meta-ads.md` (LTV, churn, demo, stack).

## Report Format

Write deliverables in the user's working language unless they request otherwise:

```markdown
## Executive Summary
[3-6 bullets]

## Analysis Context
- Account/scope:
- Period:
- Goal:
- Offer type:

## Strategy and Structure
- Phase:
- C-A-A mapped:
- Fit:
- Recommended restructure:

## Performance Read
[Budget, bottleneck, trend]

## Campaigns and Creatives
[Winners, watch list, cut candidates]

## Hypotheses
1. [Hypothesis] — evidence — how to validate

## Prioritized Action Plan
1. High / 2. Medium / 3. Low

## Next Tests
- Structure, creative, decision metric, cut/scale criteria
```

## Decision Rules

- C-A-A, CBO/ABO → `caa-strategy.md`
- Ecosystem and daily scaling → `scale-ecosystem.md`
- Low ticket (< ~$20 USD equivalent) → `cost-cap-low-ticket.md`
- Channel/format → `channels-formats-creative.md`
- SaaS / tool → `saas-meta-ads.md`

Performance:

- Scale budget **intraday** only with strong ROAS/CPA **and** campaign volume (>48h, history).
- Stack **1-1-1** campaigns before concentrating budget on few ads.
- **Cost cap** when low ticket + historical CPA + top 3–5 creatives.
- Cut when spend without conversion or clear fatigue.
- Creative test if CTR/CPC is the bottleneck.
- Fix LP/checkout if CTR is ok but CVR/CPA is bad.
- Fix tracking if data diverges.

## Quality

- Cite data and period.
- Measurable actions, review in 3–7 days.
- Hypotheses tied to metrics, not generics.

## Examples

**User:** "AI SaaS, $19/mo, 3 campaigns 1-1-1, CPA $9."

→ `saas-meta-ads.md` + `scale-ecosystem.md` → assess LTV/churn → recommend ecosystem or cost cap.

**User:** "Ticket $7, ROAS 1.7, should I scale?"

→ `cost-cap-low-ticket.md` — likely cost cap, not aggressive daily scaling.
