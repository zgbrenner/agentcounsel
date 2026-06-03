# External Communication Review Panel

A multi-pass review workflow for a draft leaving the firm — a client letter, a
counterparty email, a public statement, or any communication to a third party.
The draft is run through a defined sequence of review passes, each a persona
with a distinct lens, producing draft findings for the supervising attorney. See
`review-panels/README.md` for what a review panel is.

This panel is process guidance, not legal advice and not legal work product.
Every pass produces draft work product that a qualified, licensed attorney must
review. None of the passes decides what may be disclosed, waives privilege,
approves the message, or sends it — those remain attorney work.

> **The passes below are review lenses, not lawyers and not autonomous agents.**
> Each "reviewer" is a structured pass over the draft. It surfaces issues; it
> does not act on its own, communicate with anyone, approve, or send. None of
> them is a licensed attorney. The panel's output is attorney-supervised draft
> work product.

## When to Use

- A communication is about to leave the firm and needs a client-position,
  privilege, business-risk, and tone review before it is sent.
- The attorney wants the message checked for unauthorized commitments,
  privilege exposure, and tone before sign-off.
- A public or counterparty statement needs a layered pre-send review.

Do not use this panel to decide what is privileged, to approve disclosure, or to
send the communication.

## Inputs

- The draft communication and its intended recipient.
- The client's authorized positions and any approved messaging.
- The matter's privilege and confidentiality posture.
- The jurisdiction and governing law, if relevant to the message.
- Any prior communications in the thread the draft must track.

If the draft or the recipient is missing, stop and request it.

## Review Passes

Each pass below is a review lens, not an autonomous agent and not a lawyer. It
produces draft findings only.

### Client-position reviewer pass

- **Lens.** Does the message reflect the client's authorized positions and make
  no unauthorized commitment?
- **Inputs.** The client's authorized positions; the draft.
- **Produces.** Draft notes on unauthorized commitments, overstatements, and
  off-message content, marked `[CONFIRM: client position]` where the position is
  unstated.

### Privilege/confidentiality reviewer pass

- **Lens.** Does the message risk waiving privilege or disclosing confidential
  or sensitive material to this recipient?
- **Inputs.** The matter's privilege posture; the recipient; the draft.
- **Produces.** A draft list of privilege-waiver and confidentiality flags,
  marked for attorney confirmation. It flags risk; it does not decide what is
  privileged.

### Business-risk reviewer pass

- **Lens.** What commercial, reputational, and relationship risk does the
  message create — admissions, commitments, tone that could harm the client?
- **Inputs.** The client-position notes; the draft.
- **Produces.** A draft risk matrix (issue, exposure, severity flag). Severity
  flags are draft, not conclusions.

### Attorney gatekeeper pass

- **Lens.** Is the consolidated review complete enough for the supervising
  attorney to act on, and what must the attorney confirm before the message is
  sent?
- **Inputs.** All prior passes' findings.
- **Produces.** A consolidated must-confirm list and a ready / not-ready status.
  This pass organizes issues; it is not the attorney and does not approve or
  send the message.

## Sequence

| Order | Pass | Hands off |
|---|---|---|
| 1 | Client-position reviewer | Position notes orient the privilege and risk passes. |
| 2 | Privilege/confidentiality reviewer | Privilege flags feed the risk pass and the gate. |
| 3 | Business-risk reviewer | The risk matrix feeds the gate. |
| 4 | Attorney gatekeeper | Consolidates all findings for the supervising attorney. |

Findings are carried forward by the person running the panel: each pass's draft
output is read, then passed as context into the next.

## Required Quality Checks

Run these quality-layer passes over the draft and the consolidated findings:

- `skills/legal-methodology/privilege-confidentiality-check/SKILL.md` — surface
  every privilege-waiver and confidentiality risk for the intended recipient.
- `skills/legal-methodology/legal-prose-polish/SKILL.md` — review tone and
  clarity without changing the substance or the client's positions.
- `skills/legal-methodology/risk-assessment/SKILL.md` — structure the
  reputational and relationship exposure without converting flags into
  conclusions.

## Attorney Escalation Triggers

- The message risks waiving privilege or disclosing confidential material.
- The draft makes a commitment the client has not authorized.
- The recipient or distribution of the message is broader than expected.
- The message contains an admission or a statement of legal position.
- The tone could damage a client relationship or create exposure.

## Expected Outputs

- Client-position notes flagging unauthorized commitments (client-position
  reviewer).
- A privilege-and-confidentiality flag list (privilege/confidentiality
  reviewer).
- A draft business-risk matrix (business-risk reviewer).
- A consolidated must-confirm list and ready / not-ready status (gatekeeper).

All outputs are labeled draft legal work product for attorney review.

## Safety and Supervision Model

Every pass in this panel is a *review lens*, not an autonomous agent and not a
licensed attorney. No pass sends, approves, or discloses the communication; each
produces draft findings only. The passes run because a person applies them in
order — nothing runs itself, sends a message, or decides a privilege question on
its own. The attorney gatekeeper pass organizes issues for the supervising
attorney; it does not replace the attorney's independent judgment about what may
be sent or disclosed. The panel's entire output is attorney-supervised draft
work product, never legal advice and never an approval to send.

## Common Failure Modes

- **Privilege decision.** A pass declaring content "not privileged" instead of
  flagging it for attorney confirmation.
- **Unauthorized commitment.** Letting a commitment stand without a
  `[CONFIRM: client position]` flag.
- **Tone over substance.** Polishing tone while missing an admission or an
  unauthorized statement.
- **Recipient blindness.** Reviewing the message without accounting for who will
  receive or forward it.

## Final Attorney-Review Gate

Run `skills/legal-methodology/attorney-review-gate/SKILL.md` over the
consolidated findings and hand the result to the supervising attorney with the
gate's checklist unchecked. The panel does not check the boxes — the attorney
does. The communication is not to be sent or disclosed until the attorney has
reviewed every flagged item and adopted the message as their own.
