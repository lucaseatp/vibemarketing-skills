# Campaign structure

## Activation order (conversion / lead)

```text
Search → Demand Gen → Remarketing → Performance Max
```

Ecommerce with a mature feed may test Shopping/PMax earlier. Meta/TikTok are outside this skill but compete for total budget.

## Budget tiers (USD — VibeMarketing default)

| Tier | Reference | Structure |
| --- | --- | --- |
| Low | &lt; US$ 200/day | 1 campaign type, 1 offer, tight geo; see rules below |
| Medium | ~US$ 200/day | Search as core; expand only with stable CPA/ROAS |
| High | ~US$ 400/day | Multiple campaigns/themes; controlled tests (Demand Gen, AI Max) |
| Very high | ≥ US$ 20k/month | PMax scale + advanced bidding; validate quality in CRM |

Click plan (all tiers): daily budget ≈ avg CPC × **10 clicks** (Keyword Planner: average of bid low/high).

### Golden rule — low tier (&lt; US$ 200/day)

- **One** campaign type (almost always Search).
- **One** offer (best historical ROAS/CPA or higher ticket).
- **Geo** as narrow as possible; city in keyword + copy + extensions.
- Cut weak keywords/geo/devices **early** — profit &gt; statistical significance.

## Campaign types

| Type | Use |
| --- | --- |
| Search | Intent, local leads, services, account start |
| Shopping | Ecommerce with feed; fallback if Search fails for small stores |
| Demand Gen | Visual prospecting; more control than PMax |
| PMax | Scale + complement — see `performance-max.md` |
| Display / Video | Awareness/remarketing; do not mix Display **inside** Search |

## Search — settings that prevent waste

- **Networks:** turn off Display network on Search; defer search partners until the campaign converts.
- **Geo:** `Presence: people in location` — **not** “presence or interest” (critical for local: NYC, London, etc.).
- **Audiences:** add relevant segments in **Observation** (not “Targeting” that over-narrows at start).
- **Bidding (start):** maximize conversions **without** target CPA until volume exists; if no impressions, test max clicks with CPC cap or manual CPC.
- **AI Max:** not at launch; if testing later, see `search-ads-copy.md`.
- **Post-launch:** tablet device −100% until validated; negatives for wrong product (e.g. equipment brand vs service).

## Bidding — progression

| Stage | Bid strategy |
| --- | --- |
| Zero data | Max clicks + CPC cap or manual CPC |
| 15–30 conversions / 30 days | Maximize conversions |
| Ecommerce with varied values | Maximize conversion value |
| Stable history | tCPA / tROAS |
| Need more new vs heavy remarketing | New customer acquisition / high-value (list uploads) |

**Value rules:** when Google lacks relative value (US lead &gt; UK, iOS fewer refunds, sector that converts more) — adjust conversion value by condition.

## PMax — minimum gate

- Verified sale or lead tracking
- ~30–50 recent primary conversions **or** accept long learning with CPA/ROAS cap
- Assets + signals (hot list, search terms)
- Lead gen: qualification plan (not CPL only)

## Naming

```text
{Geo} | {Objective} | {Theme} | {Type}
US-NYC | Leads | Implants | Search
```
