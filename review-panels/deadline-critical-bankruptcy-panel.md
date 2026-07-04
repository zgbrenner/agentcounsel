# Deadline-Critical Bankruptcy Panel

A multi-pass review workflow for a deadline-sensitive bankruptcy or
restructuring draft — a filing summary, deadline calendar, proof-of-claim
overview, motion section, plan or objection outline, or diligence note. The
draft is run through a defined sequence of review passes, each a persona with a
distinct lens, producing draft findings for the supervising attorney. See
`review-panels/README.md` for what a review panel is.

This panel is process guidance, not legal advice and not legal work product.
Every pass produces draft work product that a qualified, licensed attorney must
review. None of the passes computes or verifies a date, decides whether the
automatic stay applies or was violated, or concludes that a claim is valid,
priority, avoidable, or confirmable — those remain attorney work. It
operationalizes `core/jurisdiction-and-deadline-gates.md`.

> **The passes below are review lenses, not lawyers and not autonomous agents.**
> Each "reviewer" is a structured pass over the draft. It surfaces issues,
> deadlines, and risks; it does not act on its own, communicate with anyone,
> file, or calendar anything. None of them is a licensed attorney. The panel's
> output is attorney-supervised draft work product.

## When to Use

- A bankruptcy or restructuring draft with time-sensitive content — bar dates,
  objection deadlines, cure periods, stay questions — needs a structured,
  multi-lens review before it is relied upon.
- The attorney wants every date, stay-sensitive action, and legal conclusion
  organized and flagged before the draft informs a filing or a client decision.
- A near-term deadline may be in play and the draft must surface it for
  immediate attorney attention without computing anything.

Do not use this panel to compute or confirm a deadline, to decide whether the
automatic stay applies or was violated, to rule on a claim, or as a substitute
for the attorney's own reading of the draft.

## Inputs

- The bankruptcy or restructuring draft (summary, calendar, claim overview,
  motion section, plan or objection outline, or diligence note).
- The chapter, the client's role (debtor, creditor, trustee, committee), and the
  procedural posture.
- The court and jurisdiction, or a flag that each is unknown.
- Every date the draft references, with its stated source, exactly as supplied.
- The factual record and the authorities the draft relies on.

If the draft or the client's role is missing, stop and request it.

## Review Passes

Each pass below is a review lens, not an autonomous agent and not a lawyer. It
produces draft findings only.

### Deadline-discipline pass

- **Lens.** Is every date in the draft recorded as user-supplied with its source
  and flagged `[deadline verification required]`, with nothing computed,
  counted, or inferred, per `core/jurisdiction-and-deadline-gates.md`? Are
  near-term and bar-date items surfaced for immediate attorney attention?
- **Inputs.** The draft; every referenced date with its stated source.
- **Produces.** A draft date table (date as supplied, stated source,
  `[deadline verification required]`) plus a short list of any date that appears
  computed or inferred — flagged to be stripped back to the user-supplied value
  — and a top-of-output flag for any near-term or bar-date item. It flags dates;
  it never computes or confirms one.

### Automatic-stay pass

- **Lens.** Does the draft avoid concluding that the automatic stay applies,
  does not apply, or was violated, and does it flag stay-sensitive actions
  (collection, setoff, foreclosure, enforcement, filing) for attorney review?
- **Inputs.** The draft; the client's role; the factual record.
- **Produces.** A draft list of any statement that concludes stay applicability
  or violation — flagged to be recast as a question for the attorney — and a
  list of stay-sensitive actions the draft mentions, flagged for attorney
  evaluation. It flags the issue; it does not decide whether the stay applies.

### No-legal-conclusions pass

- **Lens.** Does the draft avoid concluding that a claim is valid, entitled to a
  particular priority, avoidable (as a preference or fraudulent transfer), or
  that a plan is confirmable?
- **Inputs.** The draft; the deadline-discipline and stay pass findings.
- **Produces.** A draft list of any sentence that reads as a claim-validity,
  priority, avoidability, or confirmability conclusion, each flagged to be recast
  as an organized factor set or a `[CONFIRM: ...]` question for the attorney.

### Redaction/PII pass

- **Lens.** Are personal identifiers — full account numbers, Social Security or
  tax IDs, dates of birth, home addresses — flagged for redaction, per
  `core/confidentiality-and-privilege.md`?
- **Inputs.** The draft; the parties and their roles.
- **Produces.** A draft redaction list marking each personal identifier to mask
  or remove before the draft is shared or filed, flagged for attorney
  confirmation. It flags exposure; it does not decide what may be disclosed.

### Source/citation reviewer pass

- **Lens.** Is every authority, code section, and factual assertion in the draft
  supported by a provided source?
- **Inputs.** The draft; the cited authorities; the factual record.
- **Produces.** A draft source-status table marking each item source-supported,
  insufficient, or unsupported, with `[VERIFY: ...]` markers. It flags risk; it
  does not confirm any authority exists.

### Assumption-audit pass

- **Lens.** What assumptions about the chapter, the posture, the estate, or the
  parties' positions does the draft rest on that are not stated as such?
- **Inputs.** The draft; all prior passes' findings.
- **Produces.** A draft assumption list, each marked `[CONFIRM: ...]` where the
  premise is unstated, for attorney testing. It surfaces assumptions; it does
  not resolve them.

### Attorney gatekeeper pass

- **Lens.** Is the consolidated review complete enough for the supervising
  attorney to act on, and what must the attorney confirm — starting with any
  near-term deadline and stay flags?
- **Inputs.** All prior passes' findings.
- **Produces.** A consolidated must-confirm list and a ready / not-ready status
  for attorney review, deadline and stay items first. This pass organizes
  issues; it is not the attorney and does not compute a date or decide any stay
  or claim question.

## Sequence

| Order | Pass | Hands off |
|---|---|---|
| 1 | Deadline-discipline | The date table and near-term flags orient every later pass and the gate. |
| 2 | Automatic-stay | Stay flags feed the no-conclusions pass and the gate. |
| 3 | No-legal-conclusions | Conclusion flags feed the source and assumption passes. |
| 4 | Redaction/PII | The redaction list feeds the gate. |
| 5 | Source/citation reviewer | Source-status findings feed the assumption pass and the gate. |
| 6 | Assumption-audit | The assumption list feeds the gate. |
| 7 | Attorney gatekeeper | Consolidates all findings for the supervising attorney. |

Findings are carried forward by the person running the panel: each pass's draft
output is read, then passed as context into the next.

## Required Quality Checks

Run these quality-layer passes over the draft and the consolidated findings
before the gate:

- `skills/legal-methodology/citation-integrity-check/SKILL.md` — check every
  cited authority, code section, and quotation for integrity before reliance.
- `skills/legal-methodology/privilege-confidentiality-check/SKILL.md` — confirm
  personal identifiers are flagged for redaction and no confidential material is
  over-exposed.
- `skills/legal-methodology/assumption-audit/SKILL.md` — surface and test every
  assumption about the chapter, posture, and the parties' positions.
- `skills/legal-methodology/risk-assessment/SKILL.md` — structure the exposure
  and deadline findings without converting flags into conclusions.

## Attorney Escalation Triggers

- Any date appears computed, counted, or inferred — strip it to the user-supplied
  value and flag `[deadline verification required]`; never compute it.
- A near-term deadline or bar date is in play — surface it at the top and route
  it to the attorney immediately.
- The draft concludes that the automatic stay applies, does not apply, or was
  violated, or names a stay-sensitive action.
- The draft concludes a claim is valid, priority, avoidable, or that a plan is
  confirmable.
- The chapter, court, or governing law is unknown or disputed.

## Expected Outputs

- A date table with sources and deadline markers, plus a computed-date flag list
  and a top-of-output near-term flag (deadline-discipline).
- A stay-conclusion flag list and a stay-sensitive-action list (automatic-stay).
- A claim-validity, priority, avoidability, and confirmability flag list
  (no-legal-conclusions).
- A personal-identifier redaction list (redaction/PII).
- A source-status table with verification markers (source/citation reviewer).
- An assumption list marked for confirmation (assumption-audit).
- A consolidated must-confirm list and ready / not-ready status (gatekeeper).

All outputs are labeled draft legal work product for attorney review.

## Safety and Supervision Model

Every pass in this panel is a *review lens*, not an autonomous agent and not a
licensed attorney. No pass computes or confirms a deadline, calendars anything,
decides whether the automatic stay applies, rules on a claim, or files or sends
the draft; each produces draft findings only. The passes run because a person
applies them in order — nothing runs itself or acts on its own. Every date is
treated as user-supplied and unverified, and near-term deadlines are surfaced
for immediate attorney attention, never computed. The attorney gatekeeper pass
organizes issues for the supervising attorney; it does not replace the
attorney's independent judgment. The panel's entire output is
attorney-supervised draft work product, never legal advice.

## Common Failure Modes

- **Deadline computation.** Counting days or inferring a date rather than
  recording the user-supplied value and flagging `[deadline verification
  required]`.
- **Buried bar date.** Leaving a near-term deadline inside a table instead of
  surfacing it at the top for immediate attention.
- **Stay ruling.** Stating the automatic stay "applies" or "was violated"
  instead of flagging the question for the attorney.
- **Claim conclusion.** Calling a claim valid, priority, avoidable, or a plan
  confirmable rather than organizing the factors and flagging them.
- **Authority fabrication.** Treating a remembered code section as verified
  instead of marking it `[VERIFY: ...]`.

## Final Attorney-Review Gate

Run `skills/legal-methodology/attorney-review-gate/SKILL.md` over the
consolidated findings and hand the result to the supervising attorney with the
gate's checklist unchecked. The panel does not check the boxes — the attorney
does. The draft is not to be filed, served, calendared, or relied upon until the
attorney has reviewed every flagged item — near-term deadlines and stay
questions first — and adopted the work as their own.
