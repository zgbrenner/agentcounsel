# Citation and Source Red-Team Panel

A focused multi-pass review workflow for any draft that relies on cited
authority. The draft is run through a tight sequence of review passes — each a
persona with a distinct lens — centered on source and citation integrity,
producing draft findings for the supervising attorney. See
`review-panels/README.md` for what a review panel is.

This panel is process guidance, not legal advice and not legal work product.
Every pass produces draft work product that a qualified, licensed attorney must
review. None of the passes confirms that an authority exists, certifies a
citation, states the law, or computes a deadline — those remain attorney work.

> **The passes below are review lenses, not lawyers and not autonomous agents.**
> Each "reviewer" is a structured pass over the draft. It flags citation and
> source risk; it does not act on its own, verify authorities against external
> databases, or certify anything. None of them is a licensed attorney. The
> panel's output is attorney-supervised draft work product.

## When to Use

- A draft cites cases, statutes, regulations, or quotations and must be
  stress-tested for fabricated or unsupported authority before reliance.
- The attorney wants every citation and quoted passage traced to a provided
  source before the draft is filed, sent, or relied upon.
- A model-produced draft arrived without a claim-to-source table.

Do not use this panel to confirm that an authority is good law, to supply
missing authority, or to compute any deadline.

## Inputs

- The complete draft to red-team.
- Every source document, case, statute, and quotation the draft relies on.
- The jurisdiction and governing law, or a flag that each is unknown.
- The intended use and recipient of the draft.

If the draft is missing, stop and request it. If sources are missing, continue
only as a limitation-heavy risk screen and say so.

## Review Passes

Each pass below is a review lens, not an autonomous agent and not a lawyer. It
produces draft findings only.

### Source/citation reviewer pass

- **Lens.** Is every citation, quotation, and pin cite traceable to a provided
  source, and does the source actually support the statement?
- **Inputs.** The draft; every provided source.
- **Produces.** A draft claim-to-source table marking each item
  source-supported, source-mentioned-but-insufficient, unsupported, or
  contradicted, with `[VERIFY: ...]`, `[citation needed]`, and
  `[pin cite needed]` markers. It flags risk; it never asserts an authority is
  fabricated or genuine without a session source to check against.

### Issue-spotter pass

- **Lens.** Where does the draft rest a legal proposition on an authority that
  is risky — invented-looking, jurisdiction-mismatched, outdated, or
  overbroadly characterized?
- **Inputs.** The draft; the claim-to-source table.
- **Produces.** A draft authority-risk list (authority, use in draft, risk type)
  flagged for attorney research. It spots risk; it does not resolve it.

### Attorney gatekeeper pass

- **Lens.** Is the consolidated red-team complete enough for the supervising
  attorney to act on, and what must the attorney verify?
- **Inputs.** Both prior passes' findings.
- **Produces.** A consolidated must-verify list and a ready / not-ready status.
  This pass organizes citation risk; it is not the attorney and does not certify
  any citation.

## Sequence

| Order | Pass | Hands off |
|---|---|---|
| 1 | Source/citation reviewer | The claim-to-source table feeds the issue spotter and the gate. |
| 2 | Issue spotter | The authority-risk list feeds the gate. |
| 3 | Attorney gatekeeper | Consolidates all findings for the supervising attorney. |

Findings are carried forward by the person running the panel: each pass's draft
output is read, then passed as context into the next.

## Required Quality Checks

Run these quality-layer passes over the draft and the consolidated findings:

- `skills/legal-methodology/citation-integrity-check/SKILL.md` — check every
  citation, quotation, and pin cite for integrity.
- `skills/legal-methodology/source-validation/SKILL.md` — classify every source
  against the statement it supports.
- `skills/legal-methodology/hallucination-red-team/SKILL.md` — stress-test for
  invented or unverifiable authority and overclaiming.

## Attorney Escalation Triggers

- An authority cannot be traced to any provided source.
- A citation looks invented or unverifiable in the session materials.
- A quotation does not match the provided source text.
- An authority is from the wrong jurisdiction or may be outdated.
- A legal proposition rests on an authority the draft mischaracterizes.

## Expected Outputs

- A draft claim-to-source table with verification markers (source/citation
  reviewer).
- A draft authority-risk list (issue spotter).
- A consolidated must-verify list and ready / not-ready status (gatekeeper).

All outputs are labeled draft legal work product for attorney review.

## Safety and Supervision Model

Every pass in this panel is a *review lens*, not an autonomous agent and not a
licensed attorney. No pass certifies, files, or sends anything; each produces
draft findings only. The passes run because a person applies them in order —
nothing runs itself or verifies authority against external databases on its own.
A pass never asserts that an authority is fabricated or genuine unless a session
source supports that finding; otherwise it flags the authority for attorney
verification. The attorney gatekeeper pass organizes citation risk for the
supervising attorney; it does not replace the attorney's independent
verification. The panel's entire output is attorney-supervised draft work
product, never legal advice and never a certification that the citations are
correct.

## Common Failure Modes

- **False certification.** A pass declaring a citation "verified" when no session
  source confirms it.
- **Authority fabrication.** Supplying a substitute case or statute from memory
  to fill a gap instead of flagging `[citation needed]`.
- **Quotation drift.** Accepting a paraphrase as a quotation without checking the
  source text.
- **Jurisdiction blindness.** Missing that an otherwise supported authority is
  from the wrong jurisdiction.

## Final Attorney-Review Gate

Run `skills/legal-methodology/attorney-review-gate/SKILL.md` over the
consolidated findings and hand the result to the supervising attorney with the
gate's checklist unchecked. The panel does not check the boxes — the attorney
does. No citation is to be relied upon, and the draft is not to be filed or
sent, until the attorney has independently verified every flagged authority and
adopted the work as their own.
