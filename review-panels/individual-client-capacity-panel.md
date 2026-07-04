# Individual-Client Capacity Panel

A multi-pass review workflow for an individual-client deliverable — a family-law
or trusts-and-estates draft (a client letter, intake summary, factor
organization, memo, or estate-plan overview) prepared for or about an
individual. The draft is run through a defined sequence of review passes, each a
persona with a distinct lens, producing draft findings for the supervising
attorney. See `review-panels/README.md` for what a review panel is.

This panel is process guidance, not legal advice and not legal work product.
Every pass produces draft work product that a qualified, licensed attorney must
review. None of the passes assesses whether a person has capacity, concludes
that conduct was undue influence, coercion, or abuse, predicts a custody,
support, guardianship, best-interests, or heirship outcome, or gives an
individual client advice — those remain attorney (and where relevant, medical)
judgments. It operationalizes `core/capacity-and-vulnerable-parties.md`.

> **The passes below are review lenses, not lawyers and not autonomous agents.**
> Each "reviewer" is a structured pass over the draft. It surfaces issues and
> concerns; it does not act on its own, communicate with anyone, counsel a
> client, or send anything. None of them is a licensed attorney. The panel's
> output is attorney-supervised draft work product.

## When to Use

- A family-law or trusts-and-estates draft prepared for or about an individual
  client needs a structured, multi-lens review before it reaches the client or
  informs the matter.
- The draft touches a potentially vulnerable party — someone elderly, ill,
  grieving, in crisis, subject to possible coercion, or unrepresented.
- The attorney wants capacity, safety, confidentiality, and plain-language
  concerns organized before relying on the draft or sharing it.

Do not use this panel to assess capacity, to decide whether undue influence or
abuse occurred, to predict an outcome about any person, or as a substitute for
the attorney's own reading of the draft.

## Inputs

- The individual-client draft (letter, summary, factor organization, memo, or
  estate-plan overview).
- The practice area, the client represented, and each individual's role in the
  matter (spouse, parent, testator, beneficiary, caregiver, minor).
- The jurisdiction and governing law, or a flag that each is unknown.
- Whether the reader of the draft is the client, and whether the client appears
  to be unrepresented.
- Any user-provided safety, emergency, or hotline resources — never invented.

If the draft or the represented client is missing, stop and request it.

## Review Passes

Each pass below is a review lens, not an autonomous agent and not a lawyer. It
produces draft findings only.

### Capacity & vulnerable-party pass

- **Lens.** Does the draft anywhere assess capacity, conclude that conduct was
  undue influence, coercion, abuse, or neglect, characterize a medical or
  psychological condition beyond a provided document, or predict an outcome
  about a person — contrary to `core/capacity-and-vulnerable-parties.md`?
- **Inputs.** The draft; the individuals' roles; any provided medical or
  condition documents.
- **Produces.** A draft list quoting each statement that assesses capacity,
  labels conduct, or predicts an outcome, each flagged to be recast as
  organized facts and factors for attorney evaluation. It flags the statement;
  it does not itself decide capacity or influence.

### Safety-escalation pass

- **Lens.** Do the facts suggest a risk to anyone's physical safety — domestic
  violence, child or elder abuse or neglect, coercion, self-harm — and, if so,
  is that concern surfaced prominently at the top of the draft and routed to the
  attorney rather than buried in a checklist or narrative?
- **Inputs.** The draft; the factual record; any user-provided emergency or
  hotline resources.
- **Produces.** A draft flag, placed for the top of the output, naming each
  possible safety indicator as a fact requiring immediate attorney attention,
  with any user-provided resources attached. It surfaces the concern; it does
  not evaluate the danger or contact anyone.

### Facts-vs-conclusions pass

- **Lens.** Is everything in the draft organized as facts and questions, with no
  legal conclusion, no valuation, and no best-interests, custody, support, or
  heirship determination?
- **Inputs.** The draft; the capacity pass findings.
- **Produces.** A draft list of any sentence that reads as a conclusion,
  valuation, or determination, each flagged to be recast as a fact, an organized
  statutory or doctrinal factor, or a `[CONFIRM: ...]` question for the attorney.

### Confidentiality & sensitivity pass

- **Lens.** Are details about minors, medical conditions, and finances minimized
  and masked to what the deliverable needs, per
  `core/confidentiality-and-privilege.md`, and are minors treated as matter
  facts rather than as clients of the workflow?
- **Inputs.** The draft; the roles, noting any minors.
- **Produces.** A draft redaction-and-minimization list marking high-sensitivity
  details (minor identifiers, medical facts, account and asset figures) to mask
  or remove, flagged for attorney confirmation. It flags exposure; it does not
  decide what may be disclosed.

### Plain-language-without-advice pass

- **Lens.** Is the draft readable for an individual client — plain language over
  jargon — without ever crossing into advice ("the draft flags X for your
  attorney," never "you should do X"), and without dramatizing or softening a
  real problem?
- **Inputs.** The draft; whether the reader is the client; whether the client is
  unrepresented.
- **Produces.** Draft notes on jargon to simplify and on any sentence that reads
  as advice, urgency, or reassurance, each flagged to recast neutrally, plus a
  flag to state plainly that the material is a draft for attorney review where
  the reader appears unrepresented.

### Source/citation reviewer pass

- **Lens.** Is every authority, statutory factor, and factual assertion in the
  draft supported by a provided source, with dates left unverified?
- **Inputs.** The draft; the cited authorities; the factual record.
- **Produces.** A draft source-status table marking each item source-supported,
  insufficient, or unsupported, with `[VERIFY: ...]` markers and
  `[deadline verification required]` on any date. It flags risk; it does not
  confirm any authority or date exists.

### Assumption-audit pass

- **Lens.** What assumptions about the facts, the relationships, the
  jurisdiction, or the client's wishes does the draft rest on that are not
  stated as such?
- **Inputs.** The draft; all prior passes' findings.
- **Produces.** A draft assumption list, each marked `[CONFIRM: ...]` where the
  premise is unstated, for attorney testing. It surfaces assumptions; it does
  not resolve them.

### Attorney gatekeeper pass

- **Lens.** Is the consolidated review complete enough for the supervising
  attorney to act on, and what must the attorney confirm — starting with any
  safety and capacity flags?
- **Inputs.** All prior passes' findings.
- **Produces.** A consolidated must-confirm list and a ready / not-ready status
  for attorney review, safety and capacity items first. This pass organizes
  issues; it is not the attorney and does not decide capacity, safety, or any
  outcome.

## Sequence

| Order | Pass | Hands off |
|---|---|---|
| 1 | Capacity & vulnerable-party | Flagged capacity and influence statements orient every later pass. |
| 2 | Safety-escalation | Safety flags go to the top and feed the gate for immediate attention. |
| 3 | Facts-vs-conclusions | Conclusion flags feed the confidentiality and plain-language passes. |
| 4 | Confidentiality & sensitivity | The minimization list feeds the plain-language pass and the gate. |
| 5 | Plain-language-without-advice | Advice and readability notes feed the gate. |
| 6 | Source/citation reviewer | Source-status findings feed the assumption pass and the gate. |
| 7 | Assumption-audit | The assumption list feeds the gate. |
| 8 | Attorney gatekeeper | Consolidates all findings for the supervising attorney. |

Findings are carried forward by the person running the panel: each pass's draft
output is read, then passed as context into the next.

## Required Quality Checks

Run these quality-layer passes over the draft and the consolidated findings
before the gate:

- `skills/legal-methodology/privilege-confidentiality-check/SKILL.md` — confirm
  minors, medical, and financial details are minimized and masked, and no
  confidential material is over-exposed.
- `skills/legal-methodology/source-validation/SKILL.md` — classify whether every
  factual and legal claim, factor, and date is supported by a provided source.
- `skills/legal-methodology/assumption-audit/SKILL.md` — surface and test every
  assumption about the facts, relationships, and the client's wishes.
- `skills/legal-methodology/legal-prose-polish/SKILL.md` — keep the draft plain
  and neutral without letting readability slide into advice, urgency, or
  reassurance.

## Attorney Escalation Triggers

- The facts suggest a risk to anyone's physical safety — surface it at the top
  and route it to the attorney immediately; never evaluate the danger.
- The draft assesses capacity, or labels conduct as undue influence, coercion,
  abuse, or neglect.
- The draft predicts a custody, support, guardianship, best-interests, or
  heirship outcome, or scores or ranks a parent, spouse, heir, or beneficiary.
- The reader appears to be an unrepresented individual who could mistake the
  draft for legal advice.
- A date or filing period is implicated — never compute it; flag
  `[deadline verification required]`.

## Expected Outputs

- A list of flagged capacity, influence, and outcome statements to recast
  (capacity & vulnerable-party).
- A prominent, top-of-output safety flag with any provided resources
  (safety-escalation).
- A conclusion-and-valuation flag list to recast as facts and factors
  (facts-vs-conclusions).
- A redaction-and-minimization list for high-sensitivity details
  (confidentiality & sensitivity).
- Plain-language and advice-crossing notes (plain-language-without-advice).
- A source-status table with verification and deadline markers (source/citation
  reviewer).
- An assumption list marked for confirmation (assumption-audit).
- A consolidated must-confirm list and ready / not-ready status (gatekeeper).

All outputs are labeled draft legal work product for attorney review.

## Safety and Supervision Model

Every pass in this panel is a *review lens*, not an autonomous agent and not a
licensed attorney. No pass assesses capacity, decides whether undue influence or
abuse occurred, predicts an outcome about a person, counsels a client, or sends
anything; each produces draft findings only. The passes run because a person
applies them in order — nothing runs itself or acts on its own. Safety concerns
are surfaced prominently and routed to the attorney, never buried and never
evaluated by a pass. The attorney gatekeeper pass organizes issues for the
supervising attorney; it does not replace the attorney's independent judgment.
The panel's entire output is attorney-supervised draft work product, never legal
advice and never an assessment of any person.

## Common Failure Modes

- **Capacity conclusion.** A pass stating a person "has" or "lacks" capacity
  instead of organizing the facts and flagging them for the attorney.
- **Labeling conduct.** Calling behavior "undue influence," "coercion," or
  "abuse" as a conclusion rather than flagging the facts for attorney
  evaluation.
- **Buried safety concern.** Leaving a domestic-violence, child-safety, or
  elder-safety indicator inside a checklist instead of at the top for immediate
  attention.
- **Outcome prediction.** Predicting a custody, support, or heirship result, or
  ranking a parent, spouse, or heir.
- **Readability into advice.** Simplifying language until it tells the client
  what to do, or dramatizing or softening a real problem.

## Final Attorney-Review Gate

Run `skills/legal-methodology/attorney-review-gate/SKILL.md` over the
consolidated findings and hand the result to the supervising attorney with the
gate's checklist unchecked. The panel does not check the boxes — the attorney
does. The draft is not to be sent to the client, acted on, or relied upon until
the attorney has reviewed every flagged item — safety and capacity flags first —
and adopted the work as their own.
