#!/usr/bin/env python3
"""Calculate cold-email capacity with daily inbox caps and warmup consumption."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass


@dataclass
class Assumptions:
    sequence_length: int
    inboxes_per_domain: int
    max_sends_per_inbox_day: int
    active_warmup_per_inbox_day: int
    inactive_warmup_per_inbox_day: int
    campaign_sends_per_inbox_day: int
    sending_days: int
    ramp: float


@dataclass
class Infrastructure:
    domains: int | None
    inboxes: int | None


@dataclass
class TargetPlan:
    target_new_contacts: int | None
    target_campaign_messages: int
    required_inboxes_raw: int
    recommended_domains: int
    recommended_inboxes: int
    recommended_campaign_capacity: int
    recommended_new_contact_capacity: int
    recommended_warmup_messages: int
    recommended_total_inbox_sends: int
    surplus_campaign_messages: int


@dataclass
class AvailableCapacity:
    domains: int
    inboxes: int
    usable_inboxes: int
    campaign_message_capacity: int
    new_contact_capacity: int
    warmup_messages: int
    total_inbox_sends: int
    campaign_messages_per_inbox_day: float
    warmup_messages_per_inbox_day: float
    total_sends_per_inbox_day: float
    campaign_messages_per_domain_day: float
    total_sends_per_domain_day: float
    new_contacts_per_day: float
    limiting_factor: str


@dataclass
class InactiveWarmupCapacity:
    warmup_messages_per_inbox_day: int
    warmup_messages_per_inbox_month: int


@dataclass
class CapacityResult:
    assumptions: Assumptions
    infrastructure: Infrastructure
    target_plan: TargetPlan | None
    available_capacity: AvailableCapacity | None
    inactive_warmup_capacity: InactiveWarmupCapacity


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def calculate(args: argparse.Namespace) -> CapacityResult:
    campaign_sends_per_inbox_day = (
        args.max_sends_per_inbox_day - args.active_warmup_per_inbox_day
    )
    if campaign_sends_per_inbox_day <= 0:
        raise ValueError(
            "--active-warmup-per-inbox-day must be lower than --max-sends-per-inbox-day"
        )

    campaign_sends_per_inbox_month = (
        campaign_sends_per_inbox_day * args.sending_days * args.ramp
    )
    warmup_sends_per_inbox_month = (
        args.active_warmup_per_inbox_day * args.sending_days
    )

    assumptions = Assumptions(
        sequence_length=args.sequence_length,
        inboxes_per_domain=args.inboxes_per_domain,
        max_sends_per_inbox_day=args.max_sends_per_inbox_day,
        active_warmup_per_inbox_day=args.active_warmup_per_inbox_day,
        inactive_warmup_per_inbox_day=args.inactive_warmup_per_inbox_day,
        campaign_sends_per_inbox_day=campaign_sends_per_inbox_day,
        sending_days=args.sending_days,
        ramp=args.ramp,
    )

    domains = args.domains
    inboxes = args.inboxes

    if domains is not None and inboxes is None:
        inboxes = domains * args.inboxes_per_domain
    if inboxes is not None and domains is None:
        domains = math.ceil(inboxes / args.inboxes_per_domain)

    target_plan = None
    if args.target_new_contacts is not None or args.target_total_emails is not None:
        if args.target_new_contacts is not None:
            target_new_contacts = args.target_new_contacts
            target_campaign_messages = target_new_contacts * args.sequence_length
        else:
            target_campaign_messages = args.target_total_emails
            target_new_contacts = target_campaign_messages // args.sequence_length

        required_inboxes_raw = math.ceil(
            target_campaign_messages / campaign_sends_per_inbox_month
        )
        recommended_domains = math.ceil(required_inboxes_raw / args.inboxes_per_domain)
        recommended_inboxes = recommended_domains * args.inboxes_per_domain
        recommended_campaign_capacity = math.floor(
            recommended_inboxes * campaign_sends_per_inbox_month
        )
        recommended_new_contact_capacity = (
            recommended_campaign_capacity // args.sequence_length
        )
        recommended_warmup_messages = (
            recommended_inboxes * warmup_sends_per_inbox_month
        )
        recommended_total_inbox_sends = (
            recommended_campaign_capacity + recommended_warmup_messages
        )

        target_plan = TargetPlan(
            target_new_contacts=target_new_contacts,
            target_campaign_messages=target_campaign_messages,
            required_inboxes_raw=required_inboxes_raw,
            recommended_domains=recommended_domains,
            recommended_inboxes=recommended_inboxes,
            recommended_campaign_capacity=recommended_campaign_capacity,
            recommended_new_contact_capacity=recommended_new_contact_capacity,
            recommended_warmup_messages=math.floor(recommended_warmup_messages),
            recommended_total_inbox_sends=math.floor(recommended_total_inbox_sends),
            surplus_campaign_messages=(
                recommended_campaign_capacity - target_campaign_messages
            ),
        )

    available_capacity = None
    if domains is not None and inboxes is not None:
        domain_supported_inboxes = domains * args.inboxes_per_domain
        usable_inboxes = min(inboxes, domain_supported_inboxes)
        campaign_message_capacity = math.floor(
            usable_inboxes * campaign_sends_per_inbox_month
        )
        warmup_messages = math.floor(usable_inboxes * warmup_sends_per_inbox_month)
        total_inbox_sends = campaign_message_capacity + warmup_messages

        if domain_supported_inboxes < inboxes:
            limiting_factor = "domains"
        elif inboxes < domain_supported_inboxes:
            limiting_factor = "inboxes"
        else:
            limiting_factor = "balanced"

        campaign_messages_per_inbox_day = (
            campaign_message_capacity / usable_inboxes / args.sending_days
        )
        warmup_messages_per_inbox_day = args.active_warmup_per_inbox_day
        total_sends_per_inbox_day = (
            campaign_messages_per_inbox_day + warmup_messages_per_inbox_day
        )

        available_capacity = AvailableCapacity(
            domains=domains,
            inboxes=inboxes,
            usable_inboxes=usable_inboxes,
            campaign_message_capacity=campaign_message_capacity,
            new_contact_capacity=campaign_message_capacity // args.sequence_length,
            warmup_messages=warmup_messages,
            total_inbox_sends=total_inbox_sends,
            campaign_messages_per_inbox_day=campaign_messages_per_inbox_day,
            warmup_messages_per_inbox_day=warmup_messages_per_inbox_day,
            total_sends_per_inbox_day=total_sends_per_inbox_day,
            campaign_messages_per_domain_day=campaign_message_capacity
            / domains
            / args.sending_days,
            total_sends_per_domain_day=total_inbox_sends
            / domains
            / args.sending_days,
            new_contacts_per_day=(campaign_message_capacity // args.sequence_length)
            / args.sending_days,
            limiting_factor=limiting_factor,
        )

    inactive_warmup_capacity = InactiveWarmupCapacity(
        warmup_messages_per_inbox_day=args.inactive_warmup_per_inbox_day,
        warmup_messages_per_inbox_month=(
            args.inactive_warmup_per_inbox_day * args.sending_days
        ),
    )

    return CapacityResult(
        assumptions=assumptions,
        infrastructure=Infrastructure(domains=domains, inboxes=inboxes),
        target_plan=target_plan,
        available_capacity=available_capacity,
        inactive_warmup_capacity=inactive_warmup_capacity,
    )


def fmt_int(value: int) -> str:
    return f"{value:,}"


def fmt_float(value: float) -> str:
    return f"{value:,.1f}"


def markdown(result: CapacityResult) -> str:
    a = result.assumptions
    inactive = result.inactive_warmup_capacity
    lines = [
        "# Cold Email Capacity",
        "",
        "## Assumptions",
        "",
        "| Input | Value |",
        "| --- | ---: |",
        f"| Sequence length | {a.sequence_length} emails |",
        f"| Inboxes per domain | {a.inboxes_per_domain} |",
        f"| Max total sends/inbox/day | {a.max_sends_per_inbox_day} |",
        f"| Active warmup/inbox/day | {a.active_warmup_per_inbox_day} |",
        f"| Campaign outreach/inbox/day | {a.campaign_sends_per_inbox_day} |",
        f"| Inactive warmup/inbox/day | {a.inactive_warmup_per_inbox_day} |",
        f"| Sending days/month | {a.sending_days} |",
        f"| Campaign ramp factor | {a.ramp:g} |",
        "",
        "Warmup is always active. With active campaigns, warmup consumes the daily inbox cap.",
        f"When campaigns are inactive, warmup can run at {inactive.warmup_messages_per_inbox_day}/day, or {fmt_int(inactive.warmup_messages_per_inbox_month)}/month per inbox.",
        "",
    ]

    if result.target_plan:
        t = result.target_plan
        lines.extend(
            [
                "## Required Plan",
                "",
                "| Metric | Value |",
                "| --- | ---: |",
                f"| Target new contacts/month | {fmt_int(t.target_new_contacts)} |",
                f"| Target campaign outreach messages/month | {fmt_int(t.target_campaign_messages)} |",
                f"| Raw inboxes required | {fmt_int(t.required_inboxes_raw)} |",
                f"| Recommended domains | {fmt_int(t.recommended_domains)} |",
                f"| Recommended inboxes | {fmt_int(t.recommended_inboxes)} |",
                f"| Recommended campaign capacity/month | {fmt_int(t.recommended_campaign_capacity)} |",
                f"| Recommended new contact capacity/month | {fmt_int(t.recommended_new_contact_capacity)} |",
                f"| Active warmup messages/month | {fmt_int(t.recommended_warmup_messages)} |",
                f"| Total inbox sends/month | {fmt_int(t.recommended_total_inbox_sends)} |",
                f"| Surplus campaign messages | {fmt_int(t.surplus_campaign_messages)} |",
                "",
            ]
        )

    if result.available_capacity:
        c = result.available_capacity
        lines.extend(
            [
                "## Available Capacity",
                "",
                "| Metric | Value |",
                "| --- | ---: |",
                f"| Domains | {fmt_int(c.domains)} |",
                f"| Inboxes | {fmt_int(c.inboxes)} |",
                f"| Usable inboxes under domain ratio | {fmt_int(c.usable_inboxes)} |",
                f"| Campaign outreach messages/month | {fmt_int(c.campaign_message_capacity)} |",
                f"| New contacts/month | {fmt_int(c.new_contact_capacity)} |",
                f"| Active warmup messages/month | {fmt_int(c.warmup_messages)} |",
                f"| Total inbox sends/month | {fmt_int(c.total_inbox_sends)} |",
                f"| Campaign outreach/inbox/day | {fmt_float(c.campaign_messages_per_inbox_day)} |",
                f"| Warmup/inbox/day | {fmt_float(c.warmup_messages_per_inbox_day)} |",
                f"| Total sends/inbox/day | {fmt_float(c.total_sends_per_inbox_day)} |",
                f"| Campaign outreach/domain/day | {fmt_float(c.campaign_messages_per_domain_day)} |",
                f"| Total sends/domain/day | {fmt_float(c.total_sends_per_domain_day)} |",
                f"| New contacts/day | {fmt_float(c.new_contacts_per_day)} |",
                f"| Limiting factor | {c.limiting_factor} |",
                "",
            ]
        )

    lines.extend(
        [
            "## Reminder",
            "",
            "New contacts are unique prospects entering the campaign. Campaign outreach messages are prospect touches. Total inbox sends include active warmup.",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate cold-email domains, inboxes, contacts, warmup, and campaign messages."
    )
    parser.add_argument("--domains", type=positive_int, help="Available domains.")
    parser.add_argument("--inboxes", type=positive_int, help="Available inboxes.")
    parser.add_argument(
        "--target-new-contacts",
        type=positive_int,
        help="Desired unique prospects entering the campaign per month.",
    )
    parser.add_argument(
        "--target-total-emails",
        type=positive_int,
        help="Desired campaign outreach messages per month across all touches.",
    )
    parser.add_argument(
        "--sequence-length",
        type=positive_int,
        default=3,
        help="Emails per campaign. Default: 3.",
    )
    parser.add_argument(
        "--inboxes-per-domain",
        type=positive_int,
        default=2,
        help="Recommended inboxes per domain. Default: 2.",
    )
    parser.add_argument(
        "--max-sends-per-inbox-day",
        type=positive_int,
        default=25,
        help="Maximum total sends per inbox per day. Default: 25.",
    )
    parser.add_argument(
        "--active-warmup-per-inbox-day",
        type=positive_int,
        default=5,
        help="Warmup sends per inbox per day while campaigns are active. Default: 5.",
    )
    parser.add_argument(
        "--inactive-warmup-per-inbox-day",
        type=positive_int,
        default=15,
        help="Warmup sends per inbox per day when campaigns are inactive. Default: 15.",
    )
    parser.add_argument(
        "--sending-days",
        type=positive_int,
        default=20,
        help="Sending days per month. Default: 20.",
    )
    parser.add_argument(
        "--ramp",
        type=positive_float,
        default=1.0,
        help="Campaign capacity multiplier during ramp, e.g. 0.5. Default: 1.0.",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format. Default: markdown.",
    )

    args = parser.parse_args()

    if args.target_new_contacts is not None and args.target_total_emails is not None:
        parser.error("Use either --target-new-contacts or --target-total-emails, not both.")

    if args.active_warmup_per_inbox_day >= args.max_sends_per_inbox_day:
        parser.error("--active-warmup-per-inbox-day must be lower than --max-sends-per-inbox-day.")

    if (
        args.domains is None
        and args.inboxes is None
        and args.target_new_contacts is None
        and args.target_total_emails is None
    ):
        parser.error(
            "Provide --domains, --inboxes, --target-new-contacts, or --target-total-emails."
        )

    return args


def main() -> None:
    args = parse_args()
    result = calculate(args)

    if args.format == "json":
        print(json.dumps(asdict(result), indent=2))
    else:
        print(markdown(result))


if __name__ == "__main__":
    main()
