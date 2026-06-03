# Regulatory Risk Panel

A multi-pass review workflow for a regulatory-facing draft — a filing, a policy,
a compliance memo, or a disclosure. The draft is run through a defined sequence
of review passes, each a persona with a distinct lens, producing draft findings
for the supervising attorney. See `review-panels/README.md` for what a review
panel is.

This panel is process guidance, not legal advice and not legal work product.
Every pass produces draft work product that a qualified, licensed attorney must
review. None of the passes states what a regulation requires, confirms
compliance, computes a filing deadline, or approves a submission — those remain
attorney work.

> **The passes below are review lenses, not lawyers and not autonomous agents.**
> Each "reviewer" is a structured pass over the draft. It surfaces issues and
> risks; it does not act on its own, communicate with a regulator, file, or
> submit. None of them is a licensed attorney. The panel's output is
> attorney-supervised draft work product.

## When to Use

- A regulatory filing, policy, or compliance memo needs a compliance,
  source, and business-risk review before submission or adoption.
- The attorney wants the draft's regulatory touchpoints and exposures organized
  before sign-off.
- A disclosure draft needs a layered check against the applicable regime.

Do not use this panel to opine on whether conduct complies with a regulation, to
approve a filing, or to compute any submission deadline.

## Inputs

- The regulatory draft (filing, policy, compliance memo, or disclosure).
- The applicable regime and regulator, or a flag that each is unknown.
- The jurisdiction and the client's regulated status, if supplied.
- The facts and authorities the draft relies on.
- The client's risk tolerance and business objectives, if supplied.

If the draft or the applicable regime is missing, stop and request it.

## Review Passes

Each pass below is a review lens, not an autonomous agent and not a lawyer. It
produces draft findings only.

### Issue-spotter pass

- **Lens.** What regulatory requirements, triggers, and obligations does the
  draft engage or omit?
- **Inputs.** The draft; the applicable regime; the facts.
- **Produces.** A draft issue list (requirement, trigger, status in the draft)
  flagged for attorney confirmation. It spots issues; it does not confirm
  compliance.

### Source/citation reviewer pass

- **Lens.** Is every regulatory citation and factual assertion supported by a
  provided source?
- **Inputs.** The draft; the cited regulations and guidance; the facts.
- **Produces.** A draft source-status table marking each citation
  source-supported, insufficient, or unsupported, with `[VERIFY: ...]` and
  `[Verify current law]` markers. It flags risk; it does not confirm any
  authority exists or is current.

### Client-position reviewer pass

- **Lens.** Does the draft reflect the client's regulated posture and
  objectives without overcommitting?
- **Inputs.** The client's objectives; the issue list.
- **Produces.** Draft notes on misalignment and overcommitment, marked
  `[CONFIRM: client position]` where the posture is unstated.

### Business-risk reviewer pass

- **Lens.** What enforcement, penalty, operational, and reputational risk does
  the draft's position create?
- **Inputs.** The issue list; the client's risk tolerance.
- **Produces.** A draft risk matrix (issue, exposure, severity flag). Severity
  flags are draft, not conclusions about enforcement likelihood.

### Attorney gatekeeper pass

- **Lens.** Is the consolidated review complete enough for the supervising
  attorney to act on, and what must the attorney confirm?
- **Inputs.** All prior passes' findings.
- **Produces.** A consolidated must-confirm list and a ready / not-ready status.
  This pass organizes issues; it is not the attorney and does not approve any
  filing.

## Sequence

| Order | Pass | Hands off |
|---|---|---|
| 1 | Issue spotter | The issue list orients the source and position passes. |
| 2 | Source/citation reviewer | Source-status findings feed the position and risk passes and the gate. |
| 3 | Client-position reviewer | Misalignment notes feed the risk pass and the gate. |
| 4 | Business-risk reviewer | The risk matrix feeds the gate. |
| 5 | Attorney gatekeeper | Consolidates all findings for the supervising attorney. |

Findings are carried forward by the person running the panel: each pass's draft
output is read, then passed as context into the next.

## Required Quality Checks

Run these quality-layer passes over the draft and the consolidated findings:

- `skills/legal-methodology/source-validation/SKILL.md` — classify every
  regulatory source and confirm it actually supports the statement.
- `skills/legal-methodology/citation-integrity-check/SKILL.md` — check every
  regulatory citation for integrity and currency.
- `skills/legal-methodology/risk-assessment/SKILL.md` — structure the
  enforcement and penalty exposure without converting flags into conclusions.

## Attorney Escalation Triggers

- A regulatory citation cannot be traced to a provided, current source.
- The applicable regime, regulator, or jurisdiction is unknown or disputed.
- The draft turns on whether conduct meets a regulatory standard.
- The draft commits the client beyond its authorized posture.
- A submission or notice deadline is implicated — never compute it; flag
  `[deadline verification required]`.

## Expected Outputs

- A draft issue list of regulatory requirements and triggers (issue spotter).
- A source-status table with verification and currency markers (source/citation
  reviewer).
- Client-position misalignment notes (client-position reviewer).
- A draft business-risk matrix (business-risk reviewer).
- A consolidated must-confirm list and ready / not-ready status (gatekeeper).

All outputs are labeled draft legal work product for attorney review.

## Safety and Supervision Model

Every pass in this panel is a *review lens*, not an autonomous agent and not a
licensed attorney. No pass files, submits, or communicates with a regulator;
each produces draft findings only. The passes run because a person applies them
in order — nothing runs itself or confirms compliance on its own. The attorney
gatekeeper pass organizes issues for the supervising attorney; it does not
replace the attorney's independent judgment or approve any filing. The panel's
entire output is attorney-supervised draft work product, never legal advice and
never a compliance determination.

## Common Failure Modes

- **Compliance conclusion.** A pass stating the draft "complies" instead of
  flagging the requirement for attorney confirmation.
- **Stale authority.** Treating a regulation as current without a
  `[Verify current law]` flag.
- **Authority fabrication.** Citing a regulation number from memory rather than
  marking `[VERIFY: ...]`.
- **Deadline computation.** Calculating a submission date rather than flagging
  `[deadline verification required]`.

## Final Attorney-Review Gate

Run `skills/legal-methodology/attorney-review-gate/SKILL.md` over the
consolidated findings and hand the result to the supervising attorney with the
gate's checklist unchecked. The panel does not check the boxes — the attorney
does. The draft is not to be filed, submitted, or relied upon until the attorney
has reviewed every flagged item and adopted the work as their own.
