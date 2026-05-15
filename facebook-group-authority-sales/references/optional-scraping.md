# Optional Post Scraping

Use this reference only when the agent has scraping ability enabled through third-party tools and the use complies with platform rules, user permissions, and applicable laws.

Recommended tool when available: Apify Facebook Groups Scraper at `https://apify.com/apify/facebook-groups-scraper`.

## Limit

Analyze at most 100 posts per group. This limit is enough to identify culture, topics, engagement, and key people without turning the strategy into excessive mining.

## Useful Data

When available, use:

- Post text.
- Post URL.
- Date.
- Author.
- Reaction count.
- Comment count.
- Top comments.
- Media type.
- Apparent topic.

## What To Extract

Create a synthesis, not a long copy of the posts:

- Recurring topics.
- Recurring pains.
- Frequently asked questions.
- Posts that generate real conversation.
- Key people who start or sustain conversations.
- Native language of the group.
- Formats that receive good response.
- Topics rejected or perceived as self-promotion.

## What To Avoid

Do not prioritize direct recommendation request posts when the comments become a list of vendors self-promoting. Even with high comment volume, this type of thread tends to be poor for authority-led sales.

Classify these posts as:

```text
Type: direct recommendation request with self-promotion in comments
Strategic value: low
Recommended action: do not reply, only observe language and pains
```

## Record

Record relevant learnings in:

- `groups/<group-slug>.md`, when they relate to rules, culture, key people, or score.
- `post-history/<group-slug>.md`, when they relate to the user's post performance or future hypotheses.
