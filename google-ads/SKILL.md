---
name: google-ads
description: "Plans, structures, writes, audits, and optimizes Google Ads campaigns (Search, Performance Max, Display, Video, Demand Gen). USD budget tiers: low (<200/day), medium (~200/day), high (~400/day), very high (≥20k/month). Use for Google Ads, PMax, RSA, keywords, AI Max, CPA, ROAS, remarketing, GA4, Merchant Center, or performance diagnosis."
---

# Google Ads

## Overview

Campaigns aligned to **business goals**, landing pages, and verified measurement — not a generic checklist.

**Default:** Search for high-intent leads/sales. **PMax last** for lead gen; ecommerce may test PMax earlier with CPA/ROAS caps.

Always separate: business outcome (lead/sale) · platform metrics (CPC, CTR) · economics (CPA, ROAS, margin).

## Budget tiers (USD)

Use these tiers as the default when planning (convert to local currency only in ad copy/reports):

| Tier | Reference | Posture |
| --- | --- | --- |
| **Low** | &lt; US$ 200/day | 1 Search campaign, 1 offer, tight geo, exact+phrase, ~10 clicks/day in plan, cut losers **early**, pre-qualify in ads |
| **Medium** | ~**US$ 200/day** (~US$ 6k/month) | Solid Search + 2nd campaign only with data; weekly search-term review; tCPA/tROAS when stable |
| **High** | ~**US$ 400/day** (~US$ 12k/month) | Multiple groups/campaigns ok; test search partners, Demand Gen, AI Max (final URL expansion off); PMax if gates met |
| **Very high** | ≥ **US$ 20k/month** | Full stack, PMax for scale, value rules, new customer acquisition; budget jumps with CRM checks |

**Account maturity** (independent of budget): new account or &lt;30 conversions/30 days → Search first, no PMax/AI Max/Display on Search. With stable Search + tracking → Demand Gen → remarketing → PMax (`references/performance-max.md`).

## Marketing context

Read `marketing-context.md` if it exists. Ask only what changes structure, keywords, copy, bidding, or compliance.

## First moves

1. Task: plan, build Search, PMax, copy, keywords, audit, tracking, diagnosis.
2. Confirm: goal, geo (**presence**, not “interest”), budget, URL, sales cycle, verified conversion (Ads vs CRM).
3. Broken tracking → fix before scaling (`references/measurement-and-tracking.md`).

## References

| File | When |
| --- | --- |
| `references/campaign-structure.md` | Structure, campaign order, bidding, networks |
| `references/search-ads-copy.md` | Keywords, RSA, extensions, AI Max, pre-qualification |
| `references/performance-max.md` | PMax: when, signals, lead vs sale, scale |
| `references/measurement-and-tracking.md` | Conversions, value rules, CRM |
| `references/optimization-checklist.md` | Audit, cuts, scale |

## Workflow: new Search campaign

1. **Economics** — primary conversion, acceptable CPA/ROAS, budget for ~10 clicks/day (Keyword Planner: avg low/high CPC).
2. **One offer** — best historical performer; else higher ticket/margin.
3. **Structure** — brand separate; non-brand by theme; turn off search partners and Display on Search; audiences in **observation**; tablet −100% at start (see checklist).
4. **Keywords** — transactional; **exact + phrase** at start; negatives (jobs, free, wrong product).
5. **RSA** — distinct angles + **unique** copy (no generic AI clone); pre-qualify in headlines on **low** tier (price, geo, profile) — pin only if needed.
6. **Tracking + launch** — checklist in `campaign-structure.md`.

## Workflow: PMax

Only after gates in `references/performance-max.md`. Summary:

- **Direct sale:** CPA/ROAS cap, feed ok.
- **Lead:** qualifying LP/form, conditional conversion for ICP, hot signals (list ≥100), search terms (up to 25), validate in CRM — **do not** scale on low CPL alone.

## Workflow: diagnosis

1. Period, spend, conversion definition.
2. Ads vs CRM (missing half of real conversions is common without checks).
3. Segment: campaign → terms → device → geo → channel (PMax).
4. Fix: tracking → relevance → LP → bids → creative.

## Deliverables

- **Plan:** goal, budget, activation order (Search → … → PMax), gates, tracking.
- **Search:** keywords by group, negatives, RSA, extensions, LP notes.
- **PMax:** signals, assets, bid (CPA/ROAS), LP/form qualification, how to measure quality in CRM.
- **Audit:** top 5 by impact + 30-day plan.

Write deliverables in the user's working language unless they request otherwise.

## Boundaries

Never: promise ROAS/CPA without evidence; broken LP; scale without tags; PMax lead gen on open “maximize conversions”; multiple campaign types on **low** tier; presence+interest for local business; AI Max with **final URL expansion** on at launch; native lead forms before the site converts; ignore lead quality because CPL dropped.

Prefer: geographic presence targeting; one offer until profitable; value rules when Google lacks relative value (geo, device, LTV); weekly search-term review (Search); combine Google automation + advertiser direction (value rules, new customer acquisition, PMax signals).

## Example prompts

```text
Use $google-ads — US$ 200/day, dental clinic NYC, appointments. First Search campaign.
```

```text
Use $google-ads — PMax ecommerce, ROAS 3, Merchant feed ok, 40 sales/month.
```

```text
Use $google-ads — PMax launch: cheap leads but no closes. How to qualify?
```
