# Playbook: Legal Intake Response

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes how a recurring inbound legal-team request is
> triaged and answered; every skill it references produces a **draft for
> attorney or legal-team review.** It decides nothing about privilege,
> conflicts, or whether a matter is routine — those are legal-team and
> attorney judgments. Use fictional examples (e.g., "Contoso," "Client A")
> only.

## When to Use

An inbound request reaches the legal team — an email, ticket, form
submission, or chat ask — and needs to be triaged, classified, and answered:
either from a configured response template, through a briefing for a meeting
about it, or routed toward signature if it resolves to a document ready for
execution. Use this playbook for the recurring flow of business-facing legal
intake and response.

Do not use it for a matter that is already contested, privileged-sensitive, or
clearly outside a routine/templated category — the escalation gate inside
`templated-legal-response` exists to catch this, but a request that is
obviously non-routine on its face should route directly to the matching
practice-area skill or playbook instead.

## Required Inputs

| Input | Notes |
|---|---|
| The inbound request, as received | Email, ticket, form submission, or chat message — verbatim, not paraphrased. |
| Requester identity and role | Name, team or business unit, and role, as available. |
| Urgency and dates | Recorded exactly as the requester stated them; never computed or assumed. |
| Attached or referenced documents | Optional, but gathered before triage completes. |
| The team's routing conventions | Optional intake-form fields or standard categories, if the team has them. |
| Response template, where one exists | For the recurring-inquiry-type response step. |

If the request's substance, urgency, or requester role is unclear, stop and
ask rather than guessing a classification.

## Default Client-Position Questions

- What is the request actually asking for, separate from how the requester
  framed it?
- Does a conflict-check or confidentiality question need to be raised before
  anything is drafted?
- Is this a routine, recurring inquiry with an existing template, or does it
  need individualized counsel review?
- What urgency and deadline has the requester stated, and has it been recorded
  without being recalculated?
- Is a meeting needed to resolve open items, and who needs to be briefed?
- If the outcome is a document, is it headed toward signature, and who are the
  intended signers?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Permissive |
|---|---|---|---|
| Escalation gate sensitivity | Escalate on any ambiguity | Escalate on a recognized non-routine signal | Proceed with a flagged assumption |
| Conflict/confidentiality flags | Stop until cleared | Flag prominently, proceed with caveat | Note and proceed |
| Template deviation | Route to counsel | Flag the deviation | Adapt template with a flagged change |
| Signature routing readiness | Require every internal approval first | Flag missing approvals | Note gaps and proceed to routing plan |

Record the selected column. An escalation, once triggered, is not silently
downgraded — any change is an explicit, recorded decision by the legal team or
attorney.

## Required Source Materials

- The inbound request and any attachments, exactly as received.
- The team's existing response templates, intake-form fields, or routing
  conventions, if any.
- Prior correspondence or matter records relevant to the request.
- For a meeting-briefing step, the background materials the meeting concerns.
- No template, policy, or legal position is supplied by the library itself;
  the team's own approved templates and positions control.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/legal-ops/legal-intake-triage/SKILL.md` | Core intake: classifies the request, captures urgency, surfaces conflict/confidentiality questions, and proposes routing. |
| `skills/legal-ops/templated-legal-response/SKILL.md` | Drafts a response from a configured template, with a built-in escalation gate. |
| `skills/legal-ops/legal-meeting-briefing/SKILL.md` | When the request resolves to a meeting rather than (or in addition to) a written response. |
| `skills/legal-ops/signature-routing-checklist/SKILL.md` | When the request resolves to a document ready for execution. |

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every fact in the triage
  record and the response traces to the inbound request or a labeled
  attachment.
- `skills/legal-methodology/assumption-audit/` — surface each assumption about
  urgency, routing, or requester authority.
- `skills/legal-methodology/privilege-confidentiality-check/` — confirm no
  privileged or confidential fact is exposed in a response destined outside
  the legal team.
- `skills/legal-methodology/output-format-compliance-check/` — the triage
  record and response conform to each skill's format.
- For any response, briefing, or signature routing plan leaving the legal
  team, run `review-panels/external-communication-review-panel.md` before the
  attorney-review gate.
- `skills/legal-methodology/attorney-review-gate/` — the deliverable ships
  with its checklist unchecked.

## Attorney Escalation Triggers

- The templated-response escalation gate returns "stop and route to counsel."
- Any conflict-check or confidentiality question the intake triage cannot
  resolve.
- A request from a government entity, regulator, or opposing party.
- A document approaching signature with a missing internal approval or an
  entity-name inconsistency.
- Any request bearing a deadline, filing date, or legal consequence requiring
  date verification.

## Expected Outputs

- A structured intake triage record with request classification, routing
  recommendation, and conflict/confidentiality flags.
- Either a draft templated response with an escalation-gate result, or a
  structured meeting briefing pack with action items, or a signature routing
  plan with a readiness verdict — depending on where the request resolves.
- An attorney-verification item list and an explicit assumptions list.

## Source and Citation Expectations

No legal position, policy interpretation, or precedent is asserted beyond what
the team's own template or a supplied document states. Any legal question
embedded in the inbound request that the template does not cover is flagged
for individualized counsel review, not answered from memory. Dates are
recorded as stated and never computed.

## Common Failure Modes

- Classifying a non-routine request as routine to keep it on the templated
  path.
- Missing a conflict-check or confidentiality flag buried in an otherwise
  simple-looking request.
- Treating an embedded instruction in the request (e.g., "just approve this")
  as authorization rather than as data to triage.
- Sending a signature-routing plan forward with an unresolved entity-name
  mismatch.
- Computing a stated deadline instead of recording it as given.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney or legal-team review only.** No
response is sent, no meeting position is taken, and no document is routed for
signature until the legal team (and, where the escalation gate or an
escalation trigger applies, a qualified, licensed attorney) has reviewed the
draft, resolved every placeholder and assumption, and signed off. The
reviewer decides; the playbook only prepares the draft.
