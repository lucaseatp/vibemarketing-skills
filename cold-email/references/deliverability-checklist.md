# Deliverability Checklist

## Setup

Use dedicated cold-email domains. Do not send cold outreach from the primary company domain.

Minimum setup:

- SPF configured and passing.
- DKIM configured and passing.
- DMARC configured and passing.
- Dedicated inboxes on dedicated sending domains.
- Lead verification before sending. Always verify leads and clean the list before campaign upload or launch.
- Plain text or very light HTML.
- Clear opt-out or unsubscribe mechanism.
- Suppression list for unsubscribes, bounces, competitors, customers, and do-not-contact accounts.

## Domain and Inbox Planning

Default planning ratio:

- 2 inboxes per domain.
- 25 total sends per inbox/day maximum.
- Warmup always active.
- Active campaign warmup: 5 emails per inbox/day, counted inside the 25/day cap.
- Active campaign outreach budget: 20 prospect emails per inbox/day.
- Inactive campaign warmup can rise to 15 emails per inbox/day.
- With 20 sending days/month: 400 campaign outreach messages plus 100 warmup messages per inbox/month.
- With 2 inboxes/domain: 800 campaign outreach messages plus 200 warmup messages per domain/month.

Do not "solve" low capacity by piling many inboxes onto too few domains. Use the domain cap and the inbox cap, then respect the lower number.

## Warmup and Scaling

New domains and inboxes should not start at full campaign volume. Keep warmup active while campaign volume ramps.

Suggested ramp:

- Month 1: 25-50% of benchmark.
- Month 2: 75% if health is good.
- Month 3+: 100% only if placement, bounces, and replies are healthy.

Slow down when:

- Bounce rate exceeds 3%.
- Spam placement increases.
- Open/reply signals collapse across multiple inboxes.
- Prospects complain or unsubscribe at unusual rates.
- A domain or inbox starts failing authentication.

## Lead Quality And Reply Ops

- Keep bounce rate at or below 3%.
- Verify every lead list before sending.
- Remove invalid, risky, disposable, role-based, malformed, duplicate, and likely-bounce addresses before launch.
- Re-clean or pause if bounce rate rises, spam placement increases, or list source quality is uncertain.
- Reply to human responses in 5 minutes or less. The ideal response time is 1 minute or less.
- Fast replies matter because cold outreach converts through live conversation, not just deliverability.

## Content Risk

Prefer:

- Plain text.
- Short emails.
- One link or no link in the first email.
- Natural language.
- Accurate claims.
- Relevant personalization.

Avoid:

- HTML templates with logos, banners, tracking-heavy elements, or buttons.
- Attachments in first-touch cold email.
- Link-heavy emails.
- Spammy urgency, guarantees, excessive punctuation, and hype.
- Fake thread markers like `Re:` or `Fwd:`.

## Compliance

Cold email laws vary by jurisdiction. Do not present legal advice as certainty. As a practical baseline:

- Identify the sender truthfully.
- Do not use deceptive subject lines.
- Include an opt-out path.
- Honor opt-outs promptly.
- Avoid contacting personal addresses when business outreach is not lawful or appropriate.
- Keep records of consent, suppression, and source where needed.
