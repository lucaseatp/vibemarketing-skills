# C-A-A Strategy and Structure

**C-A-A** notation = **Campaigns - Ad Sets - Ads**. Every analysis should map current structure, identify strategic phase, and recommend the right structure — not only tune isolated metrics.

## Account Phases

| Phase | Goal | Typical structure | Signal you're in this phase |
|------|----------|-------------------|---------------------------|
| Discovery | Find winning audience, creative, or offer | 1-3-3, 1-1-3, 1-3-1 | Unstable CPA/ROAS, few clear winners, high test volume |
| Consolidation | Isolate and validate winners | 1-1-3 → 1-1-1, 1-3-1 with winners | 1-2 consistent combos, learning stabilizing |
| Scale | Increase volume while keeping efficiency | 1-1-1, CBO, Advantage+ | CPA/ROAS on target 7+ days with volume |
| Maintenance | Protect margin and refresh creatives | 1-1-1 + pipeline of 1-1-3 | Fatigue, high frequency, gradual CTR/CVR drop |

## C-A-A Structures and When to Use

### 1-1-1 — 1 campaign, 1 ad set, 1 ad

- **Use**: scale validated winner, focused remarketing, bottom-of-funnel with clear offer.
- **Advantage**: concentrates learning, less fragmentation, cleaner reads.
- **Risk**: single creative/audience dependency; fast fatigue without test pipeline.
- **Recommend when**: winner has volume and stability; goal is scale or maintenance.

### 1-1-3 — 1 campaign, 1 ad set, 3 ads

- **Use**: creative test on same audience (hooks, formats, angles, proof).
- **Advantage**: compares creatives with controlled variable (fixed audience).
- **Rule**: keep audience, placement, budget, offer equal; vary creative/copy only.
- **Limit**: **max 3 ads** per ad set in test — more splinters budget.
- **Recommend when**: CTR/CPC is bottleneck; audience works but creatives saturated.
- **Exit criteria**: identify 1 winner → move to 1-1-1 or replace losers.
- **How to launch tests**: **duplicate campaign**, keep winning audience, swap creative — **never** add new ad to campaign already selling (see `scale-ecosystem.md`).

### 1-3-1 — 1 campaign, 3 ad sets, 1 ad

- **Use**: audience test with fixed creative (interests, LAL, broad, remarketing).
- **Advantage**: isolates which audience responds best to same message.
- **Rule**: same creative/copy in all ad sets; vary segmentation only.
- **Recommend when**: creative works but CPA/ROAS varies widely by audience.
- **Exit criteria**: 1 winning ad set → close losers and scale winner.

### 1-3-3 — 1 campaign, 3 ad sets, 3 ads

- **Use**: test matrix (audience × creative) in discovery.
- **Advantage**: explores combinations quickly.
- **Risk**: splinters budget, prolongs learning, muddy causal read.
- **Recommend when**: new account, new product, or strategic reset; min budget per cell ≥ 1-2× target CPA in 3-5 days.
- **Exit criteria**: winners found → simplify to 1-1-3 or 1-3-1 before scaling.

### 1-1-5 / 1-1-10 — high-volume creative testing

- **Use**: mature accounts with continuous creative pipeline.
- **Recommend when**: active scale needs constant refresh; CBO distributes to winners.

### 1-N-1 with CBO — horizontal scale

- **Use**: multiple ad sets (countries, budget tiers, LALs) with winning creative under CBO.
- **Recommend when**: validated winner and room to expand reach without losing efficiency.

## CBO vs ABO

- **ABO**: prefer in tests (1-1-3, 1-3-1, 1-3-3) for minimum spend per cell and fair reads.
- **CBO**: prefer in scale (1-1-1, 1-N-1) for platform to optimize across mature ad sets.
- **Error signal**: CBO on test campaign with small cells → Meta concentrates budget before statistical significance.
- **Error signal**: ABO at scale with many ad sets → unbalanced budgets and under-funded winners.

## Structural Diagnosis

When analyzing the account, answer explicitly:

1. **What is current C-A-A structure?** Map active campaigns to notation.
2. **Does structure match phase?** E.g. 1-3-3 on account that should scale = fragmentation; 1-1-1 without winner = premature.
3. **Fragmentation?** Many campaigns/ad sets with low spend (< 1× target CPA) and no learning.
4. **Audience overlap?** Ad sets competing (auction overlap).
5. **Ads per ad set?** Ideal: 3-5 in test; 1-2 in scale. More than 6 dilutes learning.
6. **Budget per cell sufficient?** Rule of thumb: ≥ 1-2 conversions/day per ad set at scale; in test, spend ≥ 1× target CPA before cutting.
7. **Test pipeline exists?** Scale account without parallel 1-1-3 = fatigue risk.

## Strategic Migrations

| From | To | When |
|----|------|--------|
| 1-3-3 | 1-1-3 | Creative winner identified on 1 audience |
| 1-3-3 | 1-3-1 | Creative winner identified, test audiences |
| 1-1-3 | 1-1-1 | Creative winner validated 5-7 days |
| 1-3-1 | 1-1-1 | Audience + creative validated |
| 1-1-1 | 1-1-1 + 1-1-3 | Stable scale, start creative pipeline |
| Any | Reset 1-3-3 | Offer changed, broken tracking, CPA > 2× target 7+ days |

## Common Structural Errors

- Scaling before validation (1-1-1 without clear winner).
- Testing audience and creative together without budget (under-funded 1-3-3).
- Duplicating winning campaigns without changing a variable (cannibalization).
- Mixing top/mid/bottom funnel in same campaign.
- Dead ads consuming impressions in CBO.
- Budget increases > 20-30% every 2-3 days on ad set in learning.
- Killing new campaign before **48h** (unless stricter internal rule).
- Aggressive daily scaling on ticket **< ~$20 USD equivalent** — use `cost-cap-low-ticket.md`.

## Related References

- `scale-ecosystem.md` — campaign volume, day rule, multiple offers, Advantage+.
- `cost-cap-low-ticket.md` — cost cap, static budget ~$8–12/day equivalent.
- `channels-formats-creative.md` — Feed, Reels, Stories, image vs video, WhatsApp vs LP.
- `saas-meta-ads.md` — full SaaS and digital tool playbook.

## Strategic Decision Rules

- Recommend **1-1-3** when bottleneck is creative (bad CTR/CPC, audience ok).
- Recommend **1-3-1** when bottleneck is audience (creative ok, CPA varies by segment).
- Recommend **1-3-3** only with budget for ≥ 1× target CPA per test cell.
- Recommend **1-1-1** only after winner validated 5-7 days with volume.
- Recommend **ABO** in tests; **CBO** at scale with mature ad sets.
- Recommend **restructure** (not just bid/budget tweak) when structure and phase are misaligned.
