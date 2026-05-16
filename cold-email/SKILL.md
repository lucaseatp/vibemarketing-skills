---
name: cold-email
description: "Write, critique, improve, and plan B2B cold email outreach to prospects who have not opted in. Use when the user mentions cold email, cold outreach, prospecting emails, SDR emails, sales emails, first-touch emails, follow-ups, outbound sequences, deliverability, domains, inboxes, monthly sending volume, new contacts per month, or total outreach messages. Distinct from lifecycle or newsletter email: this skill is for unsolicited B2B prospecting, including 3-email campaign planning and capacity math."
---

# Cold Email

## Overview

Use this skill to build B2B cold email campaigns that are concise, relevant, deliverability-aware, and numerically honest. Default to a **3-email campaign** unless the user explicitly gives a different sequence length.

Always separate:

- **New contacts/month**: unique prospects entering the campaign.
- **Total outreach messages/month**: all planned touches sent across the sequence.

For the default 3-email campaign:

```text
total outreach messages/month = new contacts/month * 3
new contacts/month = floor(total outreach messages/month / 3)
```

## First Moves

1. If `marketing-context.md` exists, read it before asking questions.
2. Identify the task type: capacity plan, first email, 3-email sequence, critique, follow-ups, or performance diagnosis.
3. For capacity questions, collect or infer: target new contacts/month, target campaign emails/month, sequence length, domains, inboxes, sending days, daily inbox cap, warmup status, bounce rate, and whether the user is using dedicated cold-email domains.
4. For copy questions, collect: sender, offer, ICP, trigger, problem, proof, CTA, and desired tone.
5. If details are missing but the task can proceed, state assumptions clearly and continue.

## References

Load only what the task needs:

- `references/capacity-planning.md`: use for domains, inboxes, daily inbox caps, warmup consumption, ramp factors, and monthly volume calculations.
- `references/copy-playbook.md`: use for first-touch emails, 3-email sequences, subject lines, CTAs, critiques, and performance rewrites.
- `references/deliverability-checklist.md`: use when setup, domain health, inbox warmup, spam placement, bounces, or compliance are part of the task.

## Capacity Workflow

Use this workflow whenever the user mentions volume, monthly goals, domains, inboxes, deliverability setup, or "how many emails can I send?"

1. Confirm the sequence length. Default: 3 emails.
2. Calculate new contacts/month, campaign outreach messages/month, warmup messages/month, and total inbox sends/month.
3. Calculate required or available domains and inboxes using `references/capacity-planning.md`.
4. Prefer running the calculator for exact numbers:

```bash
python scripts/cold_email_capacity.py --target-new-contacts 5000
python scripts/cold_email_capacity.py --target-total-emails 30000
python scripts/cold_email_capacity.py --domains 15
python scripts/cold_email_capacity.py --domains 15 --ramp 0.5
```

5. Report assumptions, capacity, required infrastructure, daily pace, and whether the plan is under, at, or above recommended limits.

Use this default benchmark unless the user gives better local data:

- 2 inboxes per cold-email domain.
- 25 total sends per inbox/day maximum.
- Warmup is always active.
- With an active campaign, reserve 5 warmup emails per inbox/day. These 5 warmup emails consume the 25/day inbox cap.
- Active campaign budget: 20 campaign outreach messages per inbox/day.
- With no active campaign, warmup can rise to 15 emails per inbox/day.
- With 20 sending days/month: 1 inbox supports 400 campaign outreach messages/month plus 100 warmup emails/month.
- With a 3-email campaign: about 133 new contacts per inbox/month and 266 new contacts per domain/month.

Treat these as planning benchmarks, not guaranteed deliverability promises.

## Deliverability Operations

- Keep bounce rate at or below 3%. If it rises above 3%, stop or slow sending and clean the list.
- Always verify leads before sending and remove invalid, risky, role-based, disposable, or likely-bounce addresses.
- Keep warmup active on every sending inbox.
- Reply to human responses in 5 minutes or less. The ideal response time is 1 minute or less.

## Copy Workflow

Use `references/copy-playbook.md` for detailed guidance, then produce copy that follows these constraints:

- Write like a peer, not a vendor.
- Lead with the prospect's world, trigger, or likely problem.
- Keep one ask per email.
- Keep first emails short: usually 55-125 words.
- Make every follow-up stand alone and add a new angle.
- Use plain text or very light HTML.
- Avoid fake personalization, fake `Re:` or `Fwd:`, inflated claims, and "just checking in."

Default 3-email cadence:

| Email | Day | Job |
| --- | ---: | --- |
| 1 | 1 | Relevant observation, problem, proof, direct question |
| 2 | 4 | New angle: evidence, consequence, insight, or use case |
| 3 | 9 | Close the loop, ask for referral, or make a low-friction final question |

## Deliverables

For a capacity plan, deliver:

- Assumptions.
- New contacts/month.
- Campaign outreach messages/month.
- Warmup messages/month.
- Total inbox sends/month.
- Required or available domains and inboxes.
- Daily sending pace per inbox and per domain.
- Ramp or risk notes.
- Clear recommendation.

For a campaign, deliver:

- 3-email sequence with send days.
- Subject line variants.
- Angle summary for each email.
- Personalization fields or trigger placeholders.
- CTA rationale.
- Optional capacity math if the user mentions volume.

For a critique, deliver:

- Diagnosis of the biggest reply-rate and deliverability risks.
- Revised copy.
- Explanation of the changes.
- One next test to run.

## Boundaries

Never recommend:

- Sending cold outreach from the user's primary company domain.
- Ignoring SPF, DKIM, DMARC, bounce rate, unsubscribe, or opt-out requirements.
- Letting bounce rate exceed 3% without stopping to clean the list.
- Sending unverified leads.
- Turning warmup off on active sending inboxes.
- Buying low-quality unverified lists and blasting them.
- Fake personal details, fake customer results, fake referrals, fake `Re:` or `Fwd:`.
- HTML-heavy templates that look like marketing blasts.
- Scaling volume before inbox placement and reply quality are healthy.

Prefer:

- Dedicated cold-email domains.
- Verified lists and bounce rate at or under 3%.
- Plain text.
- Relevant trigger-based personalization.
- Low-friction CTAs.
- Conservative ramping for new domains and inboxes.
