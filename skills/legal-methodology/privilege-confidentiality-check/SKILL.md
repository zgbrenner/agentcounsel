---
name: Privilege and Confidentiality Check
description: "Use when reviewing draft legal work product for confidential client information, privileged communications, work-product labeling, redaction/anonymization needs, external-facing disclosure risk, and safer versions for the intended recipient."
practice_area: legal-methodology
task_type: verification
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The draft output to review for privilege and confidentiality risk"
  - "The intended recipient and distribution plan"
  - "The matter context, client identity, and confidentiality instructions if known"
outputs:
  - "Privilege and confidentiality risk report"
  - "Safer external-facing version or redaction plan"
related_skills:
  - skills/legal-methodology/attorney-review-gate/SKILL.md
  - skills/legal-methodology/assumption-audit/SKILL.md
  - skills/legal-methodology/legal-prose-polish/SKILL.md
tags:
  - legal-methodology
  - privilege
  - confidentiality
  - redaction
  - quality-control
---

# Privilege and Confidentiality Check

## Purpose

Review draft legal work product for privilege and confidentiality risk. The skill identifies unnecessary disclosure of confidential client information, risky inclusion of privileged communications, missing privilege/work-product labels, anonymization needs, sensitive identifiers, and the need for a safer external-facing version.

This skill does not decide privilege law. It flags issues for attorney judgment.

## Use When

- A draft may be sent outside the legal team, to a client, opposing party, regulator, court, vendor, or business stakeholder.
- A draft contains client names, employee names, addresses, account numbers, emails, sensitive facts, privileged communications, or attorney mental impressions.
- A matter workspace or output needs privilege/work-product labeling reviewed.
- The user asks for a redacted, anonymized, or external-facing version.

## Required Inputs

- The draft to review.
- Intended recipient, distribution plan, and whether the output is internal or external.
- Any matter confidentiality instructions, client restrictions, protective order, NDA, or privilege-designation guidance.

If recipient and distribution plan are missing, flag that as a gate before external use.

## Do Not Use When

- The task is to decide as a matter of law whether privilege applies.
- The user wants to disclose confidential information without attorney authorization.
- The draft is a reusable template or example containing real client information; stop and remove the real information.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Follow `core/confidentiality-and-privilege.md`.
- Follow `core/source-and-citation-discipline.md`; do not invent legal authority, citations, quotations, facts, or deadlines.
- Do not decide privilege, waiver, common-interest, work-product, or confidentiality obligations. Flag them for attorney review.
- Do not include unnecessary sensitive details in the check report.
- Do not create reusable examples with real client or matter facts.

## Workflow

1. **Confirm destination.** Identify recipient, audience, system, channel, and whether the draft is internal, client-facing, third-party-facing, court-facing, or regulator-facing.
2. **Scan for sensitive information.** Flag names, addresses, emails, account numbers, personal data, employee facts, medical facts, trade secrets, settlement positions, litigation strategy, and confidential business information.
3. **Scan for privileged material.** Flag attorney-client communications, legal advice summaries, attorney mental impressions, work-product strategy, and internal legal assessments.
4. **Check labels.** Confirm whether a privilege/work-product/confidentiality legend is present and appropriate for attorney review.
5. **Check necessity.** Determine whether each sensitive fact is necessary for the intended recipient and use.
6. **Recommend redaction or anonymization.** Propose neutral labels, summary references, redactions, or a safer external-facing version.
7. **Identify waiver/disclosure risks.** Flag distribution to third parties, mixed business/legal communications, and content that may need protective-order or confidentiality review.
8. **Prepare safer version.** If possible, draft a safer external-facing version that removes or neutralizes sensitive detail without changing substance. If not possible, state what attorney direction is needed.

## Output Format

Deliver:

1. **Draft Label** — "Draft legal work product for attorney review. Not legal advice."
2. **Recipient and Distribution Assumptions**
3. **Risk Table**

   | Location | Sensitive item | Risk type | Why it matters | Recommended treatment |
   |---|---|---|---|---|

4. **Privilege/Work-Product Label Review**
5. **Redaction and Anonymization Plan**
6. **Safer External-Facing Version** — Or a statement that attorney direction is required before a safer version can be drafted.
7. **Attorney Verification Checklist**

## Attorney Verification Checklist

- [ ] Recipient and distribution channel are approved for the matter.
- [ ] Privilege/work-product/confidentiality label is appropriate.
- [ ] No confidential client information is disclosed unnecessarily.
- [ ] Privileged communications and attorney mental impressions are handled appropriately.
- [ ] Sensitive identifiers are redacted or anonymized where appropriate.
- [ ] External-facing version has been reviewed before transmission.
- [ ] Any waiver, protective-order, NDA, or confidentiality obligation has been assessed by counsel.
