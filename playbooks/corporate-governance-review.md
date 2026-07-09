# Playbook: Corporate Governance Review

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes a recurring board-action / governance review; every
> skill it references produces a **draft for attorney review.** It decides
> nothing about whether an action is duly authorized, whether a quorum was met,
> or whether the action is valid — that is attorney work. Use fictional examples
> (e.g., "Contoso," "Director A") only.

## When to Use

A company is taking a board or shareholder action — approving a transaction,
appointing officers, authorizing a financing, adopting a plan, or ratifying a
prior act — and wants draft consents or minutes plus a governance-authority
check against the charter, bylaws, and any agreements before the action is
finalized.

Use this playbook for discrete governance actions. Route a full closing process
to the relevant matter-pack and the corporate closing skills, and a securities
disclosure question to `securities-disclosure-review.md`.

## Required Inputs

| Input | Notes |
|---|---|
| The proposed action | What the board or shareholders are being asked to approve. |
| Charter and bylaws | The governing documents controlling authority. |
| Stockholder / voting agreements | Any consent, voting, or approval-rights terms. |
| Board/committee composition | Members, independence, interested parties. |
| Jurisdiction of incorporation | `[verify jurisdiction]`; governs requirements. |
| Meeting / consent details | Notice, quorum, votes — as stated, never computed. |

If the charter, bylaws, or relevant agreements are missing, stop and request
them. Do not assume governance terms from a typical form.

## Default Client-Position Questions

- What is the precise action being authorized, and by which body?
- Does the charter, bylaws, or an agreement require a special vote, class vote,
  or independent-committee approval?
- Are any directors or stockholders interested in the action (recusal,
  disclosure)?
- Will the action proceed by meeting or by written consent?
- What approvals, consents, or conditions must precede the action?
- Is the action a ratification of a prior act, and on what basis?
- What filing or notice obligations follow (flagged, not computed)?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Permissive |
|---|---|---|---|
| Special / class vote uncertainty | Stop; require confirmation | Flag prominently | Note |
| Interested-party participation | Require recusal and committee | Flag and document | Flag |
| Written consent vs. meeting | Prefer documented meeting | Either, documented | Consent acceptable |
| Authority ambiguity in charter | Escalate | Flag for confirmation | Proceed with note |

Record the selected column. A High-risk authority flag is downgraded only by an
explicit, recorded attorney decision.

## Required Source Materials

- The certificate of incorporation / charter and current bylaws.
- Any stockholder, voting, or investor-rights agreement bearing on approval.
- The board and committee composition and independence information.
- The proposed resolutions or term sheet for the action.
- Shared references in `skills/corporate/references/`.
- No statute is supplied by the library; statutory voting and approval
  requirements are flagged for attorney verification.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/corporate/written-consent/SKILL.md` | Draft board/stockholder written consents. |
| `skills/corporate/board-minutes/SKILL.md` | Draft minutes for a meeting action. |
| `skills/corporate/entity-compliance/SKILL.md` | Check standing and governance prerequisites. |
| `skills/corporate/material-contract-schedule/SKILL.md` | When the action turns on a material contract. |
| `skills/corporate/closing-checklist/SKILL.md` | When the governance action feeds a closing. |

Open a workspace from `matter-workspaces/_template/` when the action spans
multiple consents, approvals, and conditions.

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every authority statement
  traces to the charter, bylaws, or an agreement.
- `skills/legal-methodology/assumption-audit/` — surface assumptions about
  quorum, votes, and independence.
- `skills/legal-methodology/citation-integrity-check/` — charter and bylaw
  sections are cited exactly; none invented.
- `skills/legal-methodology/privilege-confidentiality-check/` — treat drafts as
  privileged board materials.
- For a high-risk governance action (a financing, a related-party
  transaction, or a ratification of a prior act), run
  `review-panels/contract-review-panel.md` before the attorney-review gate.
- `skills/legal-methodology/attorney-review-gate/` — checklist ships unchecked.

## Attorney Escalation Triggers

- Uncertainty about whether a special, class, or supermajority vote is required.
- An interested director or controlling stockholder in the transaction.
- A conflict between the charter/bylaws and a stockholder agreement.
- A proposed ratification of a potentially defective prior act.
- An action implicating fiduciary-duty or disclosure obligations.
- A required regulatory or securities filing flowing from the action.

## Expected Outputs

- Draft resolutions, written consents, or minutes for attorney review.
- A governance-authority note mapping the action to the charter/bylaw/agreement
  provisions that govern it (flagged for attorney confirmation).
- A conditions-and-approvals list — what must precede or follow the action.
- An attorney-verification item list and an explicit assumptions list.

## Source and Citation Expectations

Quote charter, bylaw, and agreement provisions exactly, with their section
references. No statute or case is cited; statutory vote thresholds and validity
questions are flagged as attorney-verification items, not answered. Meeting
dates, notice periods, and consent dates are stated as supplied and flagged
`[deadline verification required]`; the playbook never computes them. Use
placeholders for gaps; never assume a governance term.

## Common Failure Modes

- Concluding an action "is duly authorized" or "is valid" — an attorney-only
  judgment.
- Assuming default governance terms instead of reading the actual charter and
  bylaws.
- Missing a special or class vote required by a stockholder agreement.
- Overlooking an interested-party recusal or disclosure requirement.
- Computing a notice or record-date deadline instead of flagging it.
- Inventing a charter section number or vote threshold.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney review only.** No consent or
minutes are executed, and no action is treated as authorized, until a qualified,
licensed attorney reviews the draft, confirms the gates (jurisdiction of
incorporation, governing documents, required votes, interested parties),
resolves every placeholder and assumption, and signs off. The attorney decides;
the playbook only prepares the draft.
