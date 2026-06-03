# Litigation Risk Panel

A multi-pass review workflow for a litigation-bound draft — a memo, demand
letter, brief section, or position paper. The draft is run through a defined
sequence of review passes, each a persona with a distinct lens, producing draft
findings for the supervising attorney. See `review-panels/README.md` for what a
review panel is.

This panel is process guidance, not legal advice and not legal work product.
Every pass produces draft work product that a qualified, licensed attorney must
review. None of the passes states the law, predicts an outcome, computes a
deadline, or decides strategy — those remain attorney work.

> **The passes below are review lenses, not lawyers and not autonomous agents.**
> Each "reviewer" is a structured pass over the draft. It surfaces issues and
> risks; it does not act on its own, communicate with anyone, file, or send.
> None of them is a licensed attorney. The panel's output is attorney-supervised
> draft work product.

## When to Use

- A litigation draft needs an issue-spotting, source, and risk review before it
  is filed, served, or sent.
- The attorney wants the draft's claims, exposures, and weak points organized
  before committing to a position.
- A demand or response draft needs a layered check before it leaves the firm.

Do not use this panel to predict how a court will rule, to decide litigation
strategy, or to compute any filing or limitations deadline.

## Inputs

- The litigation draft (memo, demand, brief section, or position paper).
- The procedural posture and the client's role (plaintiff, defendant, movant).
- The jurisdiction, court, and governing law, or a flag that each is unknown.
- The factual record and the authorities the draft relies on.
- The client's objectives and risk tolerance, if supplied.

If the draft or the posture is missing, stop and request it.

## Review Passes

Each pass below is a review lens, not an autonomous agent and not a lawyer. It
produces draft findings only.

### Issue-spotter pass

- **Lens.** What claims, defenses, elements, and procedural issues does the
  draft raise or omit?
- **Inputs.** The draft; the posture; the factual record.
- **Produces.** A draft issue list (claim or defense, element, status in the
  draft) flagged for attorney confirmation. It spots issues; it does not weigh
  their merits.

### Source/citation reviewer pass

- **Lens.** Is every authority and factual assertion in the draft supported by a
  provided source?
- **Inputs.** The draft; the cited authorities; the factual record.
- **Produces.** A draft source-status table marking each citation
  source-supported, insufficient, or unsupported, with `[VERIFY: ...]` markers.
  It flags risk; it does not confirm any authority exists.

### Client-position reviewer pass

- **Lens.** Does the draft advance the client's objectives without overstating
  or conceding more than authorized?
- **Inputs.** The client's objectives; the issue list.
- **Produces.** Draft notes on misalignment, overclaiming, and unauthorized
  concessions, marked `[CONFIRM: client position]` where the objective is
  unstated.

### Business-risk reviewer pass

- **Lens.** What exposure, cost, reputational, and downstream risk does the
  draft's position create for the client?
- **Inputs.** The issue list; the client's risk tolerance.
- **Produces.** A draft risk matrix (issue, exposure, severity flag). Severity
  flags are draft, not predictions of outcome.

### Attorney gatekeeper pass

- **Lens.** Is the consolidated review complete enough for the supervising
  attorney to act on, and what must the attorney confirm?
- **Inputs.** All prior passes' findings.
- **Produces.** A consolidated must-confirm list and a ready / not-ready status.
  This pass organizes issues; it is not the attorney and does not decide
  strategy or readiness to file.

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

- `skills/legal-methodology/citation-integrity-check/SKILL.md` — check every
  cited authority and quotation for integrity before reliance.
- `skills/legal-methodology/hallucination-red-team/SKILL.md` — stress-test the
  draft for unsupported claims and invented authority.
- `skills/legal-methodology/risk-assessment/SKILL.md` — structure the exposure
  findings without converting flags into outcome predictions.

## Attorney Escalation Triggers

- A cited authority cannot be traced to a provided source.
- The draft turns on a legal standard, element, or limitations period.
- The posture, court, or governing law is unknown or disputed.
- The draft overstates the client's position or makes an unauthorized
  concession.
- A deadline or filing date is implicated — never compute it; flag
  `[deadline verification required]`.

## Expected Outputs

- A draft issue list of claims, defenses, and procedural points (issue spotter).
- A source-status table with verification markers (source/citation reviewer).
- Client-position misalignment notes (client-position reviewer).
- A draft business-risk matrix (business-risk reviewer).
- A consolidated must-confirm list and ready / not-ready status (gatekeeper).

All outputs are labeled draft legal work product for attorney review.

## Safety and Supervision Model

Every pass in this panel is a *review lens*, not an autonomous agent and not a
licensed attorney. No pass files, serves, sends, or certifies the draft; each
produces draft findings only. The passes run because a person applies them in
order — nothing runs itself or predicts an outcome on its own. The attorney
gatekeeper pass organizes issues for the supervising attorney; it does not
replace the attorney's independent judgment or strategic decisions. The panel's
entire output is attorney-supervised draft work product, never legal advice and
never a prediction of how a court will rule.

## Common Failure Modes

- **Outcome prediction.** A pass stating how a court "will" rule instead of
  flagging the issue for attorney judgment.
- **Authority fabrication.** Treating a remembered case as verified instead of
  marking it `[VERIFY: ...]`.
- **Deadline computation.** Calculating a filing or limitations date rather than
  flagging `[deadline verification required]`.
- **Sycophantic softening.** Downplaying a real exposure because it is the
  position the client hoped for.

## Final Attorney-Review Gate

Run `skills/legal-methodology/attorney-review-gate/SKILL.md` over the
consolidated findings and hand the result to the supervising attorney with the
gate's checklist unchecked. The panel does not check the boxes — the attorney
does. The draft is not to be filed, served, sent, or relied upon until the
attorney has reviewed every flagged item and adopted the work as their own.
