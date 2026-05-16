# Capacity Planning

## Table of Contents

- Planning definitions
- Default benchmark
- Core formulas
- Daily pacing
- Warmup and ramp
- Worked examples
- Output rules

## Planning Definitions

Use these terms consistently:

- **New contacts/month**: unique prospects added to the sequence in a month.
- **Campaign outreach messages/month**: cold outreach touches sent to prospects, including first emails and follow-ups.
- **Warmup messages/month**: warmup emails sent by the inbox to protect reputation. Warmup is not prospect outreach.
- **Total inbox sends/month**: campaign outreach messages plus warmup messages.
- **Sequence length**: number of emails in the campaign. Default to 3.
- **Gross planned sends**: maximum planned campaign sends before replies, bounces, opt-outs, or manual stops.
- **Actual sends**: sends that really go out after replies, bounces, opt-outs, or suppression rules.

For planning, use gross planned campaign sends unless the user gives actual suppression rates.

## Default Benchmark

Use this default benchmark when the user does not provide their own safe sending limits:

| Unit | Value |
| --- | ---: |
| Inboxes per domain | 2 |
| Max total sends per inbox/day | 25 |
| Active-campaign warmup per inbox/day | 5 |
| Active-campaign outreach budget per inbox/day | 20 |
| Inactive-campaign warmup per inbox/day | 15 |
| Sending days/month | 20 |
| Campaign outreach per inbox/month | 400 |
| Warmup per active inbox/month | 100 |
| Total inbox sends per active inbox/month | 500 |
| Campaign outreach per domain/month | 800 |
| Total inbox sends per domain/month | 1,000 |

Warmup is always active. When campaigns are active, the 5 warmup emails per inbox/day consume the 25/day inbox cap, leaving 20/day for campaign outreach. When campaigns are inactive, warmup can rise to 15 emails per inbox/day.

With the default 3-email campaign:

| Unit | Campaign outreach messages/month | New contacts/month |
| --- | ---: | ---: |
| 1 inbox | 400 | 133 |
| 1 domain / 2 inboxes | 800 | 266 |
| 19 domains / 38 inboxes | 15,200 | 5,066 |
| 38 domains / 76 inboxes | 30,400 | 10,133 |

This benchmark is a planning reference, not a guarantee of inbox placement.

## Core Formulas

Default variables:

```text
sequence_length = 3
inboxes_per_domain = 2
max_sends_per_inbox_day = 25
active_warmup_per_inbox_day = 5
inactive_warmup_per_inbox_day = 15
sending_days = 20
campaign_sends_per_inbox_day = max_sends_per_inbox_day - active_warmup_per_inbox_day
campaign_sends_per_inbox_month = campaign_sends_per_inbox_day * sending_days * ramp
warmup_sends_per_inbox_month = active_warmup_per_inbox_day * sending_days
total_inbox_sends_per_inbox_month = campaign_sends_per_inbox_month + warmup_sends_per_inbox_month
```

Capacity from infrastructure:

```text
usable_inboxes = min(inboxes, domains * inboxes_per_domain)
campaign_capacity = floor(usable_inboxes * campaign_sends_per_inbox_month)
warmup_messages = usable_inboxes * active_warmup_per_inbox_day * sending_days
total_inbox_sends = campaign_capacity + warmup_messages
new_contact_capacity = floor(campaign_capacity / sequence_length)
```

Required infrastructure from target contacts:

```text
target_campaign_messages = target_new_contacts * sequence_length
required_inboxes_raw = ceil(target_campaign_messages / campaign_sends_per_inbox_month)
required_domains = ceil(required_inboxes_raw / inboxes_per_domain)
recommended_inboxes = required_domains * inboxes_per_domain
recommended_campaign_capacity = floor(recommended_inboxes * campaign_sends_per_inbox_month)
recommended_warmup_messages = recommended_inboxes * active_warmup_per_inbox_day * sending_days
recommended_total_inbox_sends = recommended_campaign_capacity + recommended_warmup_messages
recommended_new_contact_capacity = floor(recommended_campaign_capacity / sequence_length)
```

Required infrastructure from target campaign emails:

```text
target_new_contacts = floor(target_campaign_messages / sequence_length)
required_inboxes_raw = ceil(target_campaign_messages / campaign_sends_per_inbox_month)
required_domains = ceil(required_inboxes_raw / inboxes_per_domain)
recommended_inboxes = required_domains * inboxes_per_domain
```

If a user gives both domains and inboxes, cap capacity by the lower of the domain and inbox limits. Extra inboxes on too few domains should not increase the recommendation.

## Daily Pacing

Default to 20 sending days/month unless the user provides another number.

With the default benchmark:

- 1 inbox can send up to 25 total emails/day.
- During active campaigns, 5/day are warmup and 20/day are campaign outreach.
- 1 domain with 2 inboxes supports up to 50 total sends/day: 10 warmup and 40 campaign outreach.
- Inactive campaign inboxes can warm up at 15/day.

Report daily pacing as:

```text
campaign_messages_per_inbox_day = campaign_capacity / usable_inboxes / sending_days
warmup_messages_per_inbox_day = active_warmup_per_inbox_day
total_sends_per_inbox_day = campaign_messages_per_inbox_day + warmup_messages_per_inbox_day
new_contacts_per_day = new_contact_capacity / sending_days
```

## Warmup And Ramp

Warmup is always active. Ramp changes campaign outreach volume, not the warmup requirement.

Use a ramp factor when the infrastructure is new or warming:

| Situation | Suggested campaign ramp |
| --- | ---: |
| Brand new domains/inboxes, first active month | 0.25-0.50 |
| Second month with healthy placement | 0.75 |
| Warmed infrastructure with healthy placement | 1.00 |

Health conditions for using 1.00:

- SPF, DKIM, and DMARC pass.
- Bounce rate is at or below 3%.
- Leads are verified before sending.
- Spam placement is not materially increasing.
- Replies and positive replies are stable enough to justify scaling.
- Human replies are answered in 5 minutes or less; ideal is 1 minute or less.
- Domains are dedicated to cold outreach, not the primary company domain.

When uncertain, use the lower ramp and explain that scaling should follow inbox placement, not ambition.

## Worked Examples

Example: user wants 5,000 new contacts/month.

```text
target_campaign_messages = 5,000 * 3 = 15,000
campaign_sends_per_inbox_month = (25 - 5) * 20 = 400
required_inboxes = ceil(15,000 / 400) = 38
required_domains = ceil(38 / 2) = 19
warmup_messages = 38 * 5 * 20 = 3,800
total_inbox_sends = 15,200 campaign capacity + 3,800 warmup = 19,000
```

Answer: 5,000 new contacts/month requires about 19 domains and 38 inboxes. That provides 15,200 campaign outreach messages/month, which covers the 15,000 needed for a 3-email sequence, plus 3,800 warmup messages/month.

Example: user wants 30,000 campaign outreach emails/month.

```text
target_new_contacts = floor(30,000 / 3) = 10,000
campaign_sends_per_inbox_month = 400
required_inboxes = ceil(30,000 / 400) = 75
required_domains = ceil(75 / 2) = 38
recommended_inboxes = 76
```

Answer: 30,000 campaign outreach emails/month supports about 10,000 new contacts/month in a 3-email campaign and requires about 38 domains and 76 inboxes.

Example: user has 12 domains.

```text
inboxes = 12 * 2 = 24
campaign_capacity = 24 * 400 = 9,600 campaign outreach messages/month
warmup_messages = 24 * 5 * 20 = 2,400
total_inbox_sends = 12,000
new_contact_capacity = floor(9,600 / 3) = 3,200 contacts/month
```

Answer: 12 domains support about 3,200 new contacts/month, 9,600 campaign outreach messages/month, and 2,400 warmup messages/month at full campaign ramp.

## Output Rules

Always show these numbers:

- "You can contact about X new prospects/month."
- "That equals about Y campaign outreach messages/month across the 3-email campaign."
- "Warmup uses about Z messages/month."
- "Total inbox sends are about W messages/month."

Never present total inbox sends or campaign outreach messages as new contacts. This is the most common planning mistake.

When the user asks for "how many emails", clarify whether they mean campaign outreach emails or total inbox sends. If they need an immediate answer, calculate both.
