# Contract Review Panel

A multi-pass review workflow for a drafted or marked-up contract. The draft is
run through a defined sequence of review passes — each a persona with a distinct
lens — that produce draft findings for the supervising attorney. See
`review-panels/README.md` for what a review panel is.

This panel is process guidance, not legal advice and not legal work product.
Every pass produces draft work product that a qualified, licensed attorney must
review. None of the passes decides whether a provision is enforceable, states
governing law, computes a deadline, or approves signing — those remain attorney
work.

> **The passes below are review lenses, not lawyers and not autonomous agents.**
> Each "reviewer" is a structured pass over the draft. It surfaces issues; it
> does not act on its own, communicate with anyone, sign, or send. None of them
> is a licensed attorney. The panel's output is attorney-supervised draft work
> product.

## When to Use

- A contract has been drafted or redlined and needs a structured, multi-lens
  review before it goes back to the client or counterparty.
- The reviewing attorney wants issue-spotting, client-position alignment, and
  business-risk perspectives organized before sign-off.
- A counterparty markup has come back and the deltas need a layered review.

Do not use this panel to decide enforceability, to approve execution, or as a
substitute for the attorney's own reading of the contract.

## Inputs

- The contract draft or markup (with redlines, if any).
- The side represented (which party) and the deal posture.
- The jurisdiction and governing-law clause, or a flag that it is unknown.
- The client's known positions, priorities, and risk tolerance, if supplied.
- Any prior term sheet, LOI, or playbook the contract should track.

If the draft or the represented side is missing, stop and request it.

## Review Passes

Each pass below is a review lens, not an autonomous agent and not a lawyer. It
produces draft findings only.

### Primary drafter pass

- **Lens.** Does the draft say what it intends to say, clearly and internally
  consistently?
- **Inputs.** The contract draft; the term sheet or playbook it should track.
- **Produces.** A list of ambiguities, undefined terms, cross-reference errors,
  and gaps between the draft and the intended deal terms — as draft findings.

### Issue-spotter pass

- **Lens.** What legal and structural issues does the draft raise — missing
  protections, one-sided terms, problematic carve-outs?
- **Inputs.** The contract draft; the side represented.
- **Produces.** A draft issue list with each issue tied to a clause, flagged for
  attorney confirmation. It spots issues; it does not resolve them.

### Client-position reviewer pass

- **Lens.** Does the draft reflect the client's stated positions, priorities,
  and risk tolerance?
- **Inputs.** The client's known positions; the issue list.
- **Produces.** Draft notes on where the contract diverges from the client's
  positions, marked `[CONFIRM: client position]` where the position is unstated.

### Business-risk reviewer pass

- **Lens.** What commercial and operational risks do the terms create for the
  client — exposure, obligations, dependencies?
- **Inputs.** The issue list; the client's risk tolerance.
- **Produces.** A draft risk matrix (issue, exposure description, severity flag)
  for attorney and client review. Severity flags are draft, not conclusions.

### Attorney gatekeeper pass

- **Lens.** Is the consolidated review complete enough for the supervising
  attorney to act on, and what must the attorney confirm?
- **Inputs.** All prior passes' findings.
- **Produces.** A consolidated must-confirm list and a ready / not-ready status
  for attorney review. This pass organizes issues; it is not the attorney and
  does not approve the contract.

## Sequence

| Order | Pass | Hands off |
|---|---|---|
| 1 | Primary drafter | Clarity and consistency findings orient the issue spotter. |
| 2 | Issue spotter | The issue list feeds the client-position and business-risk passes. |
| 3 | Client-position reviewer | Divergence notes feed the business-risk pass and the gate. |
| 4 | Business-risk reviewer | The risk matrix feeds the gate. |
| 5 | Attorney gatekeeper | Consolidates all findings for the supervising attorney. |

Findings are carried forward by the person running the panel: each pass's draft
output is read, then passed as context into the next.

## Required Quality Checks

Run these quality-layer passes over the consolidated findings before the gate:

- `skills/legal-methodology/assumption-audit/SKILL.md` — surface and test every
  assumption about the deal terms and the client's positions.
- `skills/legal-methodology/privilege-confidentiality-check/SKILL.md` — confirm
  no privileged or confidential material is exposed if the markup is shared.
- `skills/legal-methodology/risk-assessment/SKILL.md` — structure the
  business-risk findings without converting flags into conclusions.

## Attorney Escalation Triggers

- A provision appears to allocate risk in a way the client did not authorize.
- The governing law or jurisdiction is unknown or disputed.
- The draft conflicts with the term sheet or the client's stated positions.
- An issue turns on enforceability, a legal standard, or a deadline.
- The counterparty markup introduces terms outside the playbook.

## Expected Outputs

- A clarity-and-consistency findings list (primary drafter).
- A draft issue list keyed to clauses (issue spotter).
- Client-position divergence notes (client-position reviewer).
- A draft business-risk matrix (business-risk reviewer).
- A consolidated must-confirm list and ready / not-ready status (gatekeeper).

All outputs are labeled draft legal work product for attorney review.

## Safety and Supervision Model

Every pass in this panel is a *review lens*, not an autonomous agent and not a
licensed attorney. No pass approves, signs, sends, or files the contract; each
produces draft findings only. The passes run because a person applies them in
order — nothing runs itself or acts on its own. The attorney gatekeeper pass
organizes issues for the supervising attorney; it does not replace the
attorney's independent judgment. The panel's entire output is
attorney-supervised draft work product, never legal advice.

## Common Failure Modes

- **Drift to a verdict.** A pass calling a clause "fine" or "enforceable"
  instead of flagging it for attorney confirmation.
- **Position invention.** Filling in the client's position where it is unstated
  rather than writing `[CONFIRM: client position]`.
- **Lens collapse.** Passes blurring together so issues are missed; keep each
  pass to its own lens.
- **Authority fabrication.** Citing a case or statute for an enforceability
  point instead of flagging `[VERIFY: ...]` for attorney research.

## Final Attorney-Review Gate

Run `skills/legal-methodology/attorney-review-gate/SKILL.md` over the
consolidated findings and hand the result to the supervising attorney with the
gate's checklist unchecked. The panel does not check the boxes — the attorney
does. The contract is not to be sent, signed, or relied upon until the attorney
has reviewed every flagged item and adopted the work as their own.
