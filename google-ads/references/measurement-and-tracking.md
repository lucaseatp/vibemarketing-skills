# Measurement and tracking

## Principle

Do not scale without verified primary conversion. Compare **Google Ads vs CRM** weekly — undercounting is common (e.g. half of real leads).

## Primary conversion

- Lead: form with thank-you page or server-side event.
- Sale: purchase with **value**.
- Call: minimum duration.
- Do not bid on micro conversions (scroll, pageview) unless explicit top-of-funnel goal.

## Checklist

- [ ] Google tag or GTM on landing + thank-you
- [ ] Consent mode if using CMP
- [ ] Correct counting (lead: usually one per click)
- [ ] Test conversion within 24–48h
- [ ] GA4 linked
- [ ] Enhanced conversions (forms) if applicable
- [ ] Offline import if sale closes days later in CRM

## Conversion value rules

Use when you know relative value Google **does not** see:

- Leads by country/region with different close rates
- Devices with different refund/chargeback rates
- Segments with higher LTV or repeat purchase

Path: Goals → Conversions → Value rules → apply to campaign.

Lead gen without immediate revenue: optimize CPA/leads; proxy value only with ticket × close rate provided.

## Lead gen + PMax

- Conditional conversion: tag fires only if form passes ICP filter (age, profile, etc.).
- Survey leads from PMax source only before scaling.
- Low CPL with bad quality → fix LP/form/signals, do not celebrate Ads metric.

## Ecommerce

- Dynamic value on purchase; ROAS cap aligned to real margin (consistent tax/shipping treatment).

## Merchant Center

Feed approved before Shopping/PMax retail; fix disapprovals before scaling budget.
