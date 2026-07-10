---
name: Data Retention Schedule Review
description: "Use when reviewing a draft or existing data retention schedule to inventory data categories against stated purposes, collect retention-period facts, flag legal-hold interactions, and surface orphaned-data and vendor-coverage gaps for attorney review."
practice_area: privacy
task_type: review
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The draft or existing data retention schedule, policy, or spreadsheet"
  - "The data inventory or record of processing activities, if available"
  - "The organization's stated business, legal, and regulatory purposes for each data category"
  - "Optional: known legal holds or preservation obligations currently in effect"
  - "Optional: vendor and backup system inventory covering the same data categories"
outputs:
  - "Retention-category inventory mapped to stated purposes"
  - "Retention-period fact table, flagged for legal sufficiency review"
  - "Legal-hold override interaction notes"
  - "Deletion and anonymization mechanics summary"
  - "Vendor and backup coverage gap list"
  - "Orphaned-data red-flag list"
related_skills:
  - skills/privacy/pia-generation/SKILL.md
  - skills/privacy/vendor-privacy-diligence/SKILL.md
  - skills/privacy/privacy-policy-gap-review/SKILL.md
  - skills/litigation/legal-hold/SKILL.md
  - skills/privacy/dsar-workflow/SKILL.md
tags:
  - privacy
  - data-retention
  - data-governance
  - legal-hold
  - records-management
  - data-minimization
---

# Data Retention Schedule Review

## Purpose

Organize a review of a draft or existing data retention schedule into an attorney-ready working file. The skill inventories the data categories the schedule covers, maps each to its stated business, legal, or regulatory purpose, collects the retention-period facts as written, and surfaces where the schedule's mechanics — legal-hold overrides, deletion and anonymization steps, vendor and backup coverage — create gaps or contradictions. It produces draft legal work product for attorney review — not legal advice.

This skill never determines whether a stated retention period is legally sufficient, excessive, or compliant with any law. Retention-period adequacy varies by jurisdiction, sector, and data category, and is always an attorney-verification item. The skill also never resolves a legal-hold conflict; it identifies where the schedule and a hold obligation may collide and routes that collision to litigation or legal-hold counsel.

## Use When

- The organization has a draft retention schedule and wants it checked for internal consistency and completeness before adoption.
- An existing retention schedule needs a periodic review against the current data inventory.
- A privacy, records-management, or legal-ops team wants retention periods, legal bases, and deletion mechanics organized for attorney sign-off.
- A DSAR, audit, or regulatory inquiry has surfaced a question about how long a data category is actually kept versus what the schedule says.
- Counsel needs to understand how a proposed litigation hold or preservation notice would interact with the standing retention schedule.

## Required Inputs

- **The retention schedule itself** — the draft or existing document, spreadsheet, or policy text, provided in full. Do not review from a description alone.
- **The data inventory or record of processing activities**, if one exists, so categories in the schedule can be checked against what the organization actually processes. If none is available, note the gap — this review cannot independently verify that the schedule is complete against actual data holdings.
- **The stated purpose for each retention period** — business need, legal/regulatory requirement, or contractual obligation, as the organization or the schedule states it. Do not supply a purpose the skill infers from category name alone.
- Optional: **known legal holds or preservation obligations** currently in effect, so hold-override interactions can be flagged.
- Optional: **vendor and backup system inventory** — third-party processors, backup and archive systems, and disaster-recovery copies that may hold the same data categories outside the primary system.
- Optional: the practice group's `practice-profiles/privacy.md` if populated and loaded alongside this skill. If present, use its Standard Positions and Escalation Thresholds to benchmark the review; if absent, proceed without profile benchmarking.

If the retention schedule text is not provided, stop and request it. Do not reconstruct or assume schedule content, category names, or retention periods.

## Do Not Use When

- The task is to determine whether a specific retention period is legally required, permitted, or excessive under a named law — that is an attorney-judgment item this skill flags but never resolves.
- A litigation hold must be issued, scoped, or lifted (use `skills/litigation/legal-hold/SKILL.md`; this skill's legal-hold interaction notes are an input to that workflow, not a substitute).
- The task is a general data-inventory or processing-activity mapping exercise with no retention-schedule artifact in view (use `skills/privacy/pia-generation/SKILL.md` for a new processing activity).
- The task is to review a privacy policy's public-facing retention statements against practice (use `skills/privacy/privacy-policy-gap-review/SKILL.md`).
- The task is vendor diligence on a specific processor's own retention practices in isolation (use `skills/privacy/vendor-privacy-diligence/SKILL.md`).

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- **Never conclude that a retention period is legally sufficient, excessive, or compliant.** Retention-period requirements vary by jurisdiction, sector, and data category — some are set by statute (a floor), some by regulation, and some are purely a business judgment with no legal floor or ceiling. Record every stated period as a fact and flag it `[verify jurisdiction]` and `[ATTORNEY TO CONFIRM: legal sufficiency of stated retention period]`. Do not state that a period is "too long," "too short," or "compliant."
- **Never resolve a legal-hold conflict.** If the schedule calls for deletion of a category that may be, or is, subject to a legal hold or preservation obligation, do not decide which controls. Flag the collision and route it to litigation/legal-hold counsel: `[ATTORNEY TO CONFIRM: legal-hold override — do not permit scheduled deletion of held data until counsel confirms]`.
- Record deletion, destruction, and anonymization mechanics **as facts described in the schedule** — what the schedule says happens (secure deletion, overwrite, anonymization method, archive-then-purge) — never as an endorsement that the described mechanism is legally or technically adequate. Flag adequacy as an attorney/technical-verification item.
- Do not assume the retention schedule is complete. If a category appears in the data inventory but not the schedule, or a system is not addressed by any schedule entry, flag it as an orphaned-data gap rather than assuming a default rule applies.
- Do not assume vendor or backup systems mirror the primary system's retention schedule. Absent vendor-specific confirmation, flag vendor and backup coverage as unverified.
- **Do not compute a deadline.** Any date derived from a retention period (a calculated purge date, an anniversary date) is `[deadline verification required]` — never compute it from the stated period and a start date.
- Preserve confidentiality: keep organization-specific data categories and vendor names out of reusable templates; the review is a matter record.
- Flag every gap with a placeholder rather than resolving it silently.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/privacy.md` is loaded, its Standard Positions and Escalation Thresholds inform the draft but never substitute for attorney judgment; if the profile conflicts with the matter facts or the supervising attorney's conclusions, the attorney prevails.

## Workflow

1. **Confirm inputs.** Verify the retention schedule text is provided. Note whether a data inventory, legal-hold list, and vendor/backup inventory are available; record their absence as a scoping limitation rather than assuming completeness.

2. **Build the retention-category inventory.** List each data category named in the schedule, with: the schedule's stated description, the system(s) or record type(s) it covers, and the stated retention period as written. Quote or cite the schedule section for each entry.

3. **Map each category to its stated purpose.** For each category, record the purpose the schedule or the organization states (business need, legal/regulatory requirement, contractual obligation). Where no purpose is stated, flag it: `[CONFIRM: purpose for retaining this category]`. Do not infer a purpose from the category name.

4. **Collect retention-period facts without validating them.** For each category, record the stated period as a fact. Do not characterize it as sufficient, excessive, or typical for the sector. Flag every entry `[verify jurisdiction]` (periods vary by jurisdiction and sector) and `[ATTORNEY TO CONFIRM: legal sufficiency of stated retention period]`.

5. **Screen for legal-hold interactions.** Compare the schedule's scheduled-deletion categories against any known legal holds or preservation obligations provided. For any category that overlaps a hold, flag: `[ATTORNEY TO CONFIRM: legal-hold override — do not permit scheduled deletion of held data until counsel confirms]`, and note that the interaction should be routed to `skills/litigation/legal-hold/SKILL.md`. If no legal-hold information was provided, state that as a gap, not as confirmation that no hold exists.

6. **Record deletion and anonymization mechanics as facts.** For each category, note what the schedule says happens at end of retention (deletion method, anonymization or pseudonymization approach, archival before purge, or no described mechanism). Flag any category with no described end-of-life mechanism. Do not assess technical or legal adequacy — flag it `[ATTORNEY TO CONFIRM: adequacy of described deletion/anonymization mechanism]`.

7. **Check vendor and backup coverage.** For each category, note whether the schedule (or the provided vendor/backup inventory) addresses copies held by third-party processors, backup systems, archives, and disaster-recovery environments. Flag any category where the primary system's retention period is addressed but vendor/backup coverage is silent: `[CONFIRM: vendor/backup retention alignment for this category]`.

8. **Identify orphaned-data red flags.** Cross-reference the data inventory (if provided) against the schedule. Flag as an orphaned-data red flag: (a) any data category present in the inventory but absent from the schedule; (b) any system named in the inventory with no corresponding schedule entry; (c) any schedule entry referencing a category or system not found in the inventory (a possible stale entry). If no data inventory was provided, state that this cross-reference could not be performed and flag it as a scoping gap.

9. **Assess internal consistency.** Check for contradictory entries (the same category listed twice with different periods), undefined terms, and any category whose stated period is open-ended or silent ("retained as needed," "indefinitely") — flag open-ended periods prominently, as they carry elevated legal and minimization risk `[ATTORNEY TO CONFIRM]`.

10. **Compile escalation items.** Flag prominently: any legal-hold overlap, any category with no stated period or an open-ended period, any category present in the data inventory but orphaned from the schedule, and any sensitive-data category (special-category, children's, financial, health) with a notably long or unclear retention rationale.

11. **Assemble the output** using `templates/data-retention-schedule-review-table.md`, and label it as draft legal work product for attorney review.

## Output Format

Deliver the following, in order:

1. **Summary** — 3-5 sentences: what schedule was reviewed, its scope, and the overall posture (complete, partial, or significant gaps).
2. **Retention-Category Inventory** — table: Category | Description | System(s)/Record Type | Stated Purpose | Source (section/page cited).
3. **Retention-Period Fact Table** — using `templates/data-retention-schedule-review-table.md`: Category | Stated Period (as written) | `[verify jurisdiction]` | `[ATTORNEY TO CONFIRM: legal sufficiency]`.
4. **Legal-Hold Interaction Notes** — any overlap between scheduled deletion and known holds, each flagged `[ATTORNEY TO CONFIRM: legal-hold override]` and routed to `skills/litigation/legal-hold/SKILL.md`; or a statement that no hold information was provided.
5. **Deletion and Anonymization Mechanics** — per category, the described end-of-life mechanism as a fact, with adequacy flagged for attorney/technical review.
6. **Vendor and Backup Coverage Gaps** — categories where third-party, backup, or archival coverage is unaddressed or unverified.
7. **Orphaned-Data Red Flags** — categories or systems in the data inventory absent from the schedule, and schedule entries with no corresponding inventory match.
8. **Internal Consistency Issues** — contradictions, undefined terms, and open-ended or silent retention periods.
9. **Escalation Items** — factors requiring immediate attorney or legal-hold-counsel attention.
10. **Attorney Verification Items and Assumptions** — every placeholder gathered in one list, followed by every assumption made.

### Optional: Business Stakeholder Summary

When the output will brief a non-lawyer stakeholder (a records-management lead, IT owner, or executive sponsor), add a **Business Stakeholder Summary** as a clearly separated section following `core/business-stakeholder-communication.md` — Business Summary, Decision Needed, Recommended Ask, Fallback Position, and Escalation Needed? — produced only on request or for a plainly business audience, always in addition to the deliverable above and never a substitute for attorney review.

## Attorney Verification Checklist

- [ ] The retention schedule reviewed is the current, complete version.
- [ ] Every stated retention period has been checked for legal sufficiency under applicable law by counsel; none was validated by this draft. `[verify jurisdiction]`
- [ ] Every legal-hold interaction has been reviewed and resolved by litigation/legal-hold counsel before any scheduled deletion proceeds.
- [ ] Every category's stated purpose has been confirmed as accurate and current.
- [ ] The described deletion and anonymization mechanisms have been assessed for legal and technical adequacy.
- [ ] Vendor and backup system retention practices have been confirmed to align with (or intentionally diverge from) the primary schedule.
- [ ] Every orphaned-data red flag has been investigated and resolved or explained.
- [ ] Open-ended or silent retention periods have been reviewed and either bounded or justified by counsel.
- [ ] All `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` placeholders have been resolved before the schedule is adopted or relied upon.
- [ ] If a practice profile was loaded: every applicable Standard Position and Escalation Threshold has been surfaced and deviations flagged; if none was loaded, no standing-position framing was assumed.
