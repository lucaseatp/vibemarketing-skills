---
name: facebook-group-authority-sales
description: "Create ethical authority-led Facebook group sales strategies with a community relevance interview, group research and 0-10 ranking, per-group rules database, optional limited scraping, key people mapping, post history, and content tailored to each community. Use when Codex needs to help local businesses, professionals, service providers, brands, agencies, founders, or operators in any niche sell in groups without spam, using real presence, local authority, phone/website/DM, and compliance with each group's rules."
---

# Facebook Group Authority Sales

## Overview

Use this skill to design Facebook group sales strategies that feel native to a community, not promotional. The core technique is **Community Authority Seeding**: join relevant groups, participate as a real community member, earn familiarity, and only then introduce the business through light, contextual signals.

The focus is fully on **authority-led sales**: the person sells because they become recognized, useful, and trusted in that community. Optimize for trust, usefulness, local relevance, rule compliance, and learning from history.

## Required Workflow

Follow this order before creating content:

1. Run the community relevance interview. Use `references/interview-and-strategy.md`.
2. Research groups that make sense for the user and rank each group from 0 to 10. Use `references/group-research-scoring.md`.
3. If third-party scraping tools are enabled, analyze at most 100 posts per group. Use `references/optional-scraping.md`.
4. Identify key people in each group: admins, influential members, local references, and potential partners. Use `references/key-people-partnerships.md`.
5. Record rules and context for each group in `groups/index.md` and in a group-specific `.md` file inside `groups/`.
6. Check `post-history/index.md` and the group-specific history before suggesting content.
7. Create content specific to each group. Never reuse the same post without contextual adaptation.
8. Plan comment replies, because every comment on the user's posts should be answered. Use `references/content-cadence-comments.md`.
9. After publishing or receiving results, update the group's history in `post-history/`.

## Dynamic Context

Before working on a group, always look for:

- `groups/index.md`: index connecting group name, URL, and the `.md` rules/context file.
- `groups/<group-slug>.md`: rules, score, tone, allowed CTAs, restrictions, and key people for that group.
- `post-history/index.md`: index connecting group name, URL, and history file.
- `post-history/<group-slug>.md`: previous posts, results, comments, learnings, and suggested next content.

If the group does not exist in these files yet, create the entry using `groups/_group-rules-template.md` and `post-history/_post-history-template.md`. If the group rules are unknown, ask the user to paste the rules or produce only conservative general engagement content with no CTA.

## Core Criteria

- Each post must be focused on one specific group.
- The first post is general engagement, with no selling.
- The second post may include belonging and a soft CTA, usually phone, website, or DM, if the rules allow it.
- Publish the second post 1 to 2 weeks after the first; do not publish it the next day, so it does not look like a promotional sequence.
- After the second post, keep at least 3 weeks between new posts in the same group.
- Replying to comments does not count as a new post and should always happen.
- Posts are mostly text. Use images only when they reinforce real experience, local presence, or humanity.
- Avoid scheduling links and forms as the default CTA.
- Avoid replying to direct recommendation request posts when the thread has already become a showcase of vendors self-promoting. That type of post is not the focus of this strategy.
- Never suggest content that violates the group's rules.

## Deliverables

When the user asks for a campaign, deliver:

- Summary of the community relevance interview.
- List of researched groups with 0-10 score and rationale.
- Analysis of up to 100 posts per group when scraping is allowed and a tool is available.
- Key people identified by group and suggestions for content, direct contact, or partnerships.
- Rules files or tables in `groups/`.
- Consultation or update of the history in `post-history/`.
- 3 initial pieces of content per group, respecting rules, key people, history, and user context.
- Reply scripts for comments and objections.
- Next actions: comments to make, people to observe, partnerships to try, next posting dates, and metrics to track.

## Boundaries

Never recommend:

- Fake personal stories, fake local identity, fake visits, fake relationships, fake sponsorships, or invented customer results.
- Mass posting the same content across multiple groups.
- Creating posts before recording the group's rules.
- Reusing the same post without adapting it to the specific group.
- Scraping members from private groups or contacting people without context.
- Scraping more than 100 posts per group for this strategy.
- Ignoring admin rules or evading bans.
- Scheduling links or forms as the default CTA.
- Entering direct recommendation threads just to self-promote.
- Fear-based claims, licensing claims, insurance claims, or guarantees the business cannot support.
- Posting customer photos, addresses, or project details without permission.

Prefer:

- Truthful storytelling, with placeholders for details that are not confirmed yet.
- Native language aligned with the group's culture.
- Helpful comments before new posts.
- Light CTAs through phone, website, or DM that can be removed when group rules require it.
- Personalized content per group based on rules, history, key people, and the user's real context.
