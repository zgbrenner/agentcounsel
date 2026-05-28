# Playbook: Privacy DPA Review

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes a recurring data-processing-agreement review; every
> skill it references produces a **draft for attorney review.** It decides
> nothing about whether the DPA satisfies a privacy regime, whether a transfer
> is permitted, or whether it may be signed — that is attorney work. Use
> fictional examples (e.g., "Contoso," "Client A") only.

## When to Use

A data processing agreement (DPA) or data-protection addendum has been received
and the client wants a review against its data-protection positions — covering
roles (controller/processor), processing scope, sub-processing, security
measures, breach notification, data-subject rights, audit, and cross-border
transfers — producing a risk read and prioritized redline points.

Use `commercial-contract-review.md` for the broader commercial terms of the
underlying agreement; this playbook focuses on the data-protection terms. Route a
full privacy-impact assessment to the relevant specialist skill.

## Required Inputs

| Input | Notes |
|---|---|
| Full DPA / addendum text | Including any incorporated security schedule. |
| Client role | Controller, processor, or sub-processor — confirmed. |
| Processing description | Categories of data and data subjects, purposes. |
| Applicable regimes | `[verify jurisdiction]`; named by the client. |
| Transfer mechanism in use | SCCs, adequacy, or other — as stated. |
| Client data-protection positions | Standard DPA playbook, if any. |

If the DPA text or its security schedule is missing, stop and request it.

## Default Client-Position Questions

- Is the client the controller, the processor, or a sub-processor?
- What categories of personal data and data subjects are in scope?
- Which privacy regimes does the client treat as applicable to this processing?
- What are the client's required security, breach-notification, and audit
  terms?
- What is the client's position on sub-processing (consent, notice, flow-down)?
- What cross-border transfer mechanism does the client require, and to which
  countries?
- What are the client's deletion / return and retention requirements?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Permissive |
|---|---|---|---|
| Sub-processing | Prior consent required | Notice with objection right | General authorization |
| Breach-notification window | Short, fixed | Reasonable, stated | As proposed |
| Audit rights | Full on-site rights | Reports plus limited audit | Reports only |
| Transfer to non-adequate country | Stop / require safeguards | Flag and require mechanism | Accept stated mechanism |
| Liability for data breach | Carve out from cap | Flag | Accept within cap |

Record the selected column. A High-priority flag is downgraded only by an
explicit, recorded attorney decision.

## Required Source Materials

- The DPA / addendum and any security schedule or transfer annex.
- The client's DPA playbook and standard data-protection positions.
- The processing description and data-flow information.
- `practice-profiles/contracts.md`, if populated and loaded.
- No privacy statute or regulation text is supplied by the library; regime-
  specific requirements are flagged for attorney verification.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/privacy/dpa-review/SKILL.md` | Core DPA clause-by-clause review. |
| `skills/privacy/privacy-policy-gap-review/SKILL.md` | When the DPA is checked against the client's published policy. |
| `skills/privacy/pia-generation/SKILL.md` | When a privacy-impact assessment follows. |
| `skills/privacy/dsar-workflow/SKILL.md` | When data-subject-rights handling is in scope. |

Open a workspace from `matter-workspaces/_template/` when the DPA, schedule, and
transfer annex together justify multi-file tracking.

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every quoted clause traces to
  the DPA text.
- `skills/legal-methodology/assumption-audit/` — surface assumptions about role,
  scope, and applicable regime.
- `skills/legal-methodology/privilege-confidentiality-check/` — keep data-flow
  and client facts out of reusable artifacts.
- `skills/legal-methodology/output-format-compliance-check/` — risk output
  conforms to the expected format.
- `skills/legal-methodology/attorney-review-gate/` — checklist ships unchecked.

## Attorney Escalation Triggers

- A cross-border transfer to a country without an adequacy finding or a stated
  safeguard.
- A role characterization (controller vs. processor) that the processing
  description contradicts.
- A breach-notification term that appears inadequate for the applicable regime.
- Sub-processing without notice, objection, or flow-down obligations.
- Special-category or children's data in scope.
- A data-breach liability carve-out missing where required.

## Expected Outputs

- A clause-by-clause review against the client's data-protection positions.
- A risk table rated High / Medium / Low with section references.
- Prioritized redline points (preferred position, fallback, suggested
  direction — not final clause language).
- A roles-and-transfers note flagging characterizations for attorney
  confirmation.
- An attorney-verification item list and an explicit assumptions list.

## Source and Citation Expectations

Quote DPA clauses, defined terms, and section numbers exactly. No privacy
statute, regulation, or guidance is cited; regime-specific adequacy and
sufficiency questions are flagged as attorney-verification items, not answered.
Transfer-mechanism validity is flagged, never concluded. Use placeholders for
gaps; never infer an applicable regime or a data category not described.

## Common Failure Modes

- Accepting the DPA's role label without testing it against the processing
  description.
- Concluding the DPA "complies with" a named regime — an attorney-only judgment.
- Inventing a regulatory requirement or notification window not in the document.
- Computing a breach-notification or retention deadline instead of flagging it.
- Missing a transfer to a non-adequate jurisdiction buried in an annex.
- Placing client data-flow facts into a reusable template.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney review only.** No DPA is signed,
no transfer treated as permitted, and no compliance conclusion relied upon until
a qualified, licensed attorney reviews the draft, confirms the gates (role,
regime, transfer mechanism, jurisdiction), resolves every placeholder and
assumption, and signs off. The attorney decides; the playbook only prepares the
draft.
