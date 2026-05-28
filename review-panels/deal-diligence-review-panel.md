# Deal Diligence Review Panel

A multi-pass review workflow for a diligence work product — an issue list, a
data-room gap matrix, a diligence summary, or a findings memo. The draft is run
through a defined sequence of review passes, each a persona with a distinct
lens, producing draft findings for the supervising attorney. See
`review-panels/README.md` for what a review panel is.

This panel is process guidance, not legal advice and not legal work product.
Every pass produces draft work product that a qualified, licensed attorney must
review. None of the passes decides whether a finding is material, states the
law, computes a deadline, or approves the deal decision — those remain attorney
work.

> **The passes below are review lenses, not lawyers and not autonomous agents.**
> Each "reviewer" is a structured pass over the draft. It surfaces issues; it
> does not act on its own, communicate with anyone, or approve any deal step.
> None of them is a licensed attorney. The panel's output is attorney-supervised
> draft work product.

## When to Use

- A diligence work product needs a completeness, source, client-position, and
  risk review before it informs a deal decision.
- The attorney wants the diligence findings, gaps, and exposures organized
  before advising the client or the deal team.
- A findings memo or gap matrix needs a layered check before it is relied upon.

Do not use this panel to decide deal materiality, to approve signing or closing,
or to compute any deal deadline.

## Inputs

- The diligence work product (issue list, gap matrix, summary, or memo).
- The deal type, structure, and the side represented.
- The jurisdiction and governing law, or a flag that each is unknown.
- The diligence document set and the sources the findings rely on.
- The client's objectives, risk tolerance, and deal priorities, if supplied.

If the diligence work product or the side is missing, stop and request it.

## Review Passes

Each pass below is a review lens, not an autonomous agent and not a lawyer. It
produces draft findings only.

### Issue-spotter pass

- **Lens.** What diligence issues, gaps, and red flags does the work product
  raise or omit across workstreams?
- **Inputs.** The work product; the deal type; the document set.
- **Produces.** A draft issue list (workstream, issue, gap status) flagged for
  attorney confirmation. It spots issues; it does not weigh materiality.

### Source/citation reviewer pass

- **Lens.** Is every finding traceable to a provided diligence document, and is
  any gap supported by the absence of a document rather than an assumption?
- **Inputs.** The work product; the diligence document set.
- **Produces.** A draft source-status table marking each finding
  source-supported, insufficient, or unsupported, with `[VERIFY: ...]` and
  `[CONFIRM: document]` markers. It flags risk; it does not confirm a document
  exists.

### Client-position reviewer pass

- **Lens.** Does the work product reflect the client's deal objectives and
  priorities, and does it surface what the client needs to decide?
- **Inputs.** The client's objectives; the issue list.
- **Produces.** Draft notes on misalignment and client decision points, marked
  `[CONFIRM: client position]` where the objective is unstated.

### Business-risk reviewer pass

- **Lens.** What deal, financial, and operational risk do the findings create
  for the client — exposure, indemnity implications, post-closing burdens?
- **Inputs.** The issue list; the client's risk tolerance.
- **Produces.** A draft risk matrix (finding, exposure, severity flag). Severity
  flags are draft, not materiality conclusions.

### Attorney gatekeeper pass

- **Lens.** Is the consolidated review complete enough for the supervising
  attorney to act on, and what must the attorney confirm?
- **Inputs.** All prior passes' findings.
- **Produces.** A consolidated must-confirm list and a ready / not-ready status.
  This pass organizes issues; it is not the attorney and does not approve any
  deal step.

## Sequence

| Order | Pass | Hands off |
|---|---|---|
| 1 | Issue spotter | The issue list orients the source, position, and risk passes. |
| 2 | Source/citation reviewer | Source-status findings feed the position and risk passes and the gate. |
| 3 | Client-position reviewer | Misalignment and decision-point notes feed the risk pass and the gate. |
| 4 | Business-risk reviewer | The risk matrix feeds the gate. |
| 5 | Attorney gatekeeper | Consolidates all findings for the supervising attorney. |

Findings are carried forward by the person running the panel: each pass's draft
output is read, then passed as context into the next.

## Required Quality Checks

Run these quality-layer passes over the work product and the consolidated
findings:

- `skills/legal-methodology/source-validation/SKILL.md` — classify every
  diligence source against the finding it supports.
- `skills/legal-methodology/assumption-audit/SKILL.md` — surface and test every
  assumption behind the findings and the gaps.
- `skills/legal-methodology/risk-assessment/SKILL.md` — structure the deal
  exposure without converting flags into materiality conclusions.

## Attorney Escalation Triggers

- A finding cannot be traced to a provided diligence document.
- A gap rests on an assumption rather than a confirmed missing document.
- The deal type, side, or governing law is unknown or disputed.
- A finding implicates the client's authority or deal objectives.
- A finding turns on materiality, a legal standard, or a deal deadline — never
  compute it; flag `[deadline verification required]`.

## Expected Outputs

- A draft issue list across workstreams (issue spotter).
- A source-status table with verification markers (source/citation reviewer).
- Client-position and decision-point notes (client-position reviewer).
- A draft business-risk matrix (business-risk reviewer).
- A consolidated must-confirm list and ready / not-ready status (gatekeeper).

All outputs are labeled draft legal work product for attorney review.

## Safety and Supervision Model

Every pass in this panel is a *review lens*, not an autonomous agent and not a
licensed attorney. No pass approves, signs, or closes anything; each produces
draft findings only. The passes run because a person applies them in order —
nothing runs itself or decides materiality on its own. The attorney gatekeeper
pass organizes issues for the supervising attorney; it does not replace the
attorney's independent judgment or any deal decision. The panel's entire output
is attorney-supervised draft work product, never legal advice and never a
deal-readiness determination.

## Common Failure Modes

- **Materiality conclusion.** A pass declaring a finding "immaterial" instead of
  flagging it for attorney judgment.
- **Phantom gap.** Asserting a gap from an assumption rather than confirming the
  document is absent.
- **Authority fabrication.** Citing a standard from memory rather than marking
  `[VERIFY: ...]`.
- **Deadline computation.** Calculating a deal date rather than flagging
  `[deadline verification required]`.

## Final Attorney-Review Gate

Run `skills/legal-methodology/attorney-review-gate/SKILL.md` over the
consolidated findings and hand the result to the supervising attorney with the
gate's checklist unchecked. The panel does not check the boxes — the attorney
does. The diligence work product is not to inform a deal decision or any signing
or closing step until the attorney has reviewed every flagged item and adopted
the work as their own.
