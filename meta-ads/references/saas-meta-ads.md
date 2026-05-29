# SaaS and Digital Tools on Meta Ads

Playbook derived from high-growth SaaS case study: test → validate → scale, demo-led creatives, LTV-aware decisions.

## Contents

- Funnel fit
- Phases: test, validate, scale
- Creative strategy for SaaS
- Metrics beyond CPA
- Campaign structure
- Stack and offers
- Common SaaS errors

## Funnel Fit

Meta works for SaaS when:

- **Clear problem** and **demo-able product** (screen recording, before/after workflow).
- **Free trial**, freemium, or low-friction signup with **tracked** complete registration / subscribe event.
- **LTV > CAC** with payback window you can afford (often 3–6 months for self-serve).

Harder when:

- Long enterprise sales cycle with no pixel event.
- Product needs heavy education with no video/demo capacity.
- Churn erases LTV before payback — fix product/pricing before scaling spend.

## Phases: Test → Validate → Scale

| Phase | Budget | Structure | Goal |
| --- | --- | --- | --- |
| **Test** | Low (~$10–30/day total) | 1-1-3 or 1-3-1, ABO | Find creative + audience with acceptable signup/trial CPA |
| **Validate** | Moderate | 1-1-1 winners, 5–7 days stable | Confirm CPA holds with volume; check trial→paid if data exists |
| **Scale** | Increase | Multiple 1-1-1 + optional cost cap | Volume while CPA ≤ target; refresh creatives |

Do **not** scale to $100+/day on one ad before **validate** phase completes.

## Creative Strategy for SaaS

Winning patterns:

1. **Screen demo** — show the exact workflow solved (not generic "AI tool" b-roll).
2. **Problem agitation** — "You're still doing X manually" in first 3 seconds.
3. **Specific outcome** — numbers, time saved, revenue (if defensible).
4. **UGC / founder** — trust for early-stage products.
5. **Before/after** — spreadsheet vs dashboard, old process vs new.

Test matrix (controlled):

- Same demo, **3 hooks** (1-1-3).
- Winning hook, **3 audiences** (1-3-1): broad Advantage+, LAL purchasers/signups, interest stack.

Avoid:

- Generic stock footage with no product UI.
- Feature lists without outcome.
- Same creative for cold and remarketing without adaptation.

Cross-reference: `copywriting` → `value-ad-creative.md` for script structure.

## Metrics Beyond CPA

| Metric | Why |
| --- | --- |
| **CPA (signup/trial)** | Primary optimization at top of funnel |
| **Trial → paid %** | Validates creative attracts right users |
| **LTV / MRR per cohort** | Justifies higher CPA than e-commerce |
| **Churn (30/90 day)** | Kills scale if ignored |
| **Payback period** | Max affordable CPA = f(LTV, margin, churn) |

Example logic:

- $19/mo plan, 5% monthly churn → rough LTV ~$380 (simplified) → CPA $15–40 may be viable vs $7 ebook.

Always state assumptions when LTV is estimated.

## Campaign Structure

Recommended stack:

1. **Cold prospecting** — 1-1-1 or 1-1-3, conversion objective (complete registration / subscribe).
2. **Advantage+** duplicate of winning creative — often expands reach.
3. **Remarketing** — trial started, visited pricing, engaged 30d — separate 1-1-1, tighter message (urgency, social proof).
4. **Optional cost cap** — after 3–5 validated creatives and known CPA (`cost-cap-low-ticket.md` applies to low MRR tiers too).

For **low MRR** ($5–15/mo): treat like low ticket — static budgets, ecosystem, cost cap; don't chase ROAS on first month revenue alone.

## Stack and Offers

- Multiple **plans or entry offers** (annual vs monthly, lite vs pro) → separate campaigns or clear LP paths; don't blend CPAs.
- **Lead magnet → trial** vs **direct trial** — test both; different CPAs, same LTV check at paid conversion.
- Content/SEO + Meta: attribute with UTMs; don't double-count organic signups as ad ROAS.

## Common SaaS Errors

- Optimizing for **link clicks** or **landing page views** instead of signup/purchase.
- Scaling one **UGC winner** without demo variants → audience exhaustion.
- Ignoring **onboarding/trial experience** — ads fix traffic, not product activation.
- CPA target from **first-month revenue** only on subscription.
- Pausing remarketing while scaling cold — trial abandoners need separate budget.
- 1-3-3 matrix without budget → inconclusive tests, premature cuts.

## Decision Rules

- New SaaS account → start **1-1-3** demo creatives, ABO, $10–20/day.
- Winner with 10+ signups at target CPA → **1-1-1** + begin second creative test (duplicate campaign).
- 3+ stable 1-1-1 + historical CPA → add **cost cap** layer for volume.
- CPA up but trial→paid stable → likely **creative fatigue** or audience saturation — refresh creative, not only bid.
- CPA up and trial→paid down → **wrong message/audience** or product mismatch — revisit offer and LP.

## Related References

- `caa-strategy.md` — C-A-A phases and migrations.
- `scale-ecosystem.md` — ecosystem before budget, day rule.
- `cost-cap-low-ticket.md` — low price point tiers.
- `channels-formats-creative.md` — Reels demo, Feed static.
