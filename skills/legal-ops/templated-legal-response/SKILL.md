---
name: Templated Legal Response
description: "Use when drafting a response to a routine, recurring legal inquiry from a configured template, with a built-in escalation gate that stops the templated path when the matter shows characteristics that require individualized counsel review."
practice_area: legal-ops
task_type: drafting
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The recurring legal inquiry and its type"
  - "The team's response template for that inquiry type, if one exists"
  - "Customization facts: names, dates, reference numbers, jurisdiction, receipt date, deadline"
  - "The audience and relationship, so tone can be set"
outputs:
  - "Escalation gate result (pass, or stop and route to counsel)"
  - "Draft templated response for attorney review"
  - "Deadlines and follow-up actions"
related_skills:
  - skills/legal-ops/signature-routing-checklist/SKILL.md
  - skills/privacy/dsar-workflow/SKILL.md
  - skills/litigation/legal-hold/SKILL.md
tags:
  - legal-ops
  - templated-response
  - escalation-gate
  - in-house
  - drafting
---

# Templated Legal Response

## Purpose

Produce a draft response to a routine, recurring legal inquiry using a configured response template, and run an escalation gate before drafting so that matters needing individualized attention do not receive a templated reply. The skill covers common in-house inquiries: data subject requests, litigation hold notices, vendor legal questions, NDA requests from business teams, privacy inquiries, subpoena acknowledgments, and insurance notifications.

This skill provides workflow discipline and structure. It produces draft legal work product for attorney review. This is not legal advice. A templated response is still a legal communication and must be reviewed before it is sent.

## Use When

- A user says "draft a response to this data subject request," "respond to this vendor legal question," "send a litigation hold notice," or names another recurring inquiry type.
- A recurring inquiry arrives that the legal team normally handles with a standard template.
- The team needs a consistent first draft together with a check on whether the matter is routine enough to be templated at all.

## Required Inputs

- **The inquiry** and its type — data subject request, litigation hold, vendor question, NDA request, privacy inquiry, subpoena, insurance notification, or another recurring category. If the type is unclear, ask before drafting.
- **The team's response template** for that inquiry type, if one exists — the actual firm template. If none exists, the skill drafts a default structure and flags clearly that no approved template was used.
- **Customization facts**: names, dates, reference numbers, the applicable jurisdiction and regulation, the date the inquiry was received, and the response deadline if known.
- **The audience and relationship** — internal or external, business or legal, individual or regulator, routine or contentious — so tone can be set.

This skill drafts a response; it does not send anything.

## Do Not Use When

- The inquiry is a subpoena, regulator demand, or other legal process — these require individualized counsel review; the skill may produce only a draft clearly marked for counsel, never a final response.
- An escalation trigger is present (see the Workflow) — the templated path stops and the skill produces a counsel-review draft instead.
- The task is to draft a substantive legal position or argument — that is not a templated response; route it to an attorney.
- No inquiry has been provided and the request is to design templates in the abstract — agree scope first.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice. A templated response is still a legal communication; it must be reviewed before it is sent.
- Run the escalation gate before drafting. If any trigger fires, stop the templated path, alert the user, explain the trigger, recommend an escalation path, and produce a draft marked "DRAFT — FOR COUNSEL REVIEW ONLY."
- Never invent facts, reference numbers, deadlines, regulations, or template language. Use `[CONFIRM: ...]` placeholders for anything not supplied.
- Do not state legal rights or obligations as authoritative; the legal content carried by a template is attorney-verification material.
- Compute a response deadline only from a user-supplied receipt date and the regime the user identifies. Flag every deadline `[CONFIRM: deadline]`. Do not invent or assume deadlines.
- Do not apply a privilege or confidentiality label — such as an attorney-client header on a litigation hold — that the supervising attorney has not authorized.
- Distinguish: the inquiry as received, the escalation-gate result, the draft response, customization assumptions, follow-up actions, verification items.
- Preserve confidentiality; templates and examples use fictional placeholders only.
- Flag every point of uncertainty rather than resolving it silently.

## Workflow

1. **Identify the inquiry type.** Confirm the category. If it is ambiguous, show the categories and ask before drafting.

2. **Load the template.** Use the team's configured template for the type. If none exists, note that no approved template was found and use a default structure for the type, flagged as not firm-approved.

3. **Run the escalation gate.** Before drafting, check for triggers that mean the matter should not receive a templated reply:
   - **Universal triggers**: potential litigation or regulatory investigation; the inquiry originates from a regulator, government agency, or law enforcement; the response could create a binding commitment or waiver; potential criminal liability; media attention is involved or likely; the situation is unprecedented for the team; multiple jurisdictions with conflicting requirements; executive leadership or board members are involved.
   - **Category-specific triggers**: for data subject requests — a minor's data, a request from a regulator rather than an individual, data under a litigation hold, a requester with an active employment dispute, an unusually broad scope, or special-category data; for litigation holds — potential criminal liability, unclear or disputed scope, or a custodian objection; for vendor questions — a dispute, a breach, a litigation threat, or a regulatory-compliance question; for NDA requests — a competitor counterparty, classified information, or an M&A context; for subpoenas and legal process — always requires counsel review.
   - If any trigger fires: stop the templated path, alert the user, explain which trigger fired and why it matters, recommend an escalation path, and produce a draft marked "DRAFT — FOR COUNSEL REVIEW ONLY" rather than a final response.

4. **Gather customization details.** If the gate passes, collect the facts the response needs: names, dates, reference numbers, jurisdiction and regulation, receipt date, and deadline.

5. **Draft the response.** Populate the template. Adjust tone for the audience, the relationship, the sensitivity of the matter, and the urgency. Keep business-facing language plain.

6. **Verify required elements.** Confirm the response contains the elements the inquiry type requires (for a data subject request: the applicable regime, the timeline, identity-verification requirements, the data subject's rights, a contact; for a litigation hold: the matter reference, the preservation scope, the no-spoliation instruction, an acknowledgment request, a contact).

7. **List follow-up actions and deadlines.** Note post-send actions, calendar reminders, and any logging or tracking the inquiry type requires. Flag every deadline `[CONFIRM]`.

8. **Assemble the output** and label it a draft.

## Output Format

Deliver the following sections in order:

**DRAFT TEMPLATED LEGAL RESPONSE — FOR ATTORNEY REVIEW**

1. **Inquiry Summary** — inquiry type, origin, date received, applicable jurisdiction and regulation, and the template used (or a note that no approved template was found).

2. **Escalation Gate Result** — **PASS** (no triggers detected) or **STOP** (the triggers detected, why each matters, and the recommended escalation path). On STOP, the draft below is marked for counsel review only.

3. **Draft Response** — recipient, subject line, and body, with `[CONFIRM: ...]` placeholders for any missing fact.

4. **Customization and Assumptions** — every fact used to customize the response and every assumption made.

5. **Deadlines** — each response or acknowledgment deadline, flagged `[CONFIRM: deadline]`.

6. **Follow-Up Actions** — post-send actions, reminders, and tracking or logging requirements.

7. **Attorney Verification Items** — see the Attorney Verification Checklist below.

## Attorney Verification Checklist

- [ ] The inquiry type has been correctly identified.
- [ ] The escalation gate has been run; if any trigger fired, the templated path was stopped and the matter routed to counsel.
- [ ] The template used is the team's current, approved template for this inquiry type — or the absence of an approved template has been noted and accepted.
- [ ] Every name, date, reference number, jurisdiction, and regulation in the response has been verified; none was invented.
- [ ] Every response or acknowledgment deadline has been verified against the applicable regime and the actual receipt date.
- [ ] The response contains every legally required element for its inquiry type.
- [ ] Any privilege or confidentiality label on the response has been authorized by the supervising attorney.
- [ ] The tone is appropriate for the audience, the relationship, and the sensitivity of the matter.
- [ ] For any subpoena or legal-process matter, individualized counsel review has been completed; no templated response was sent as a final reply.
- [ ] All assumptions and open items are resolved, and the response has been approved, before it is sent.
