# Playbook: Commercial Contract Review

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes a recurring commercial-contract review; every skill
> it references produces a **draft for attorney review.** It decides nothing
> about enforceability, liability exposure, or whether the agreement may be
> signed — that is attorney work. Illustrate the workflow with fictional
> examples (e.g., "Contoso," "Client A") only.

## When to Use

A master services agreement (MSA), SaaS or subscription agreement, statement of
work, supply, reseller, or other commercial agreement needs a clause-by-clause
risk review against the client's standard positions, producing a risk matrix and
prioritized redline points before negotiation or signature.

Use `nda-review.md` instead for a stand-alone confidentiality agreement, and
route an agreement that is part of an M&A or financing to the relevant
matter-pack and specialist counsel.

## Required Inputs

| Input | Notes |
|---|---|
| Full agreement text | Including all exhibits, SOWs, and order forms. |
| Client role | Buyer/customer, seller/vendor, or partner. |
| Deal value and term | Drives escalation thresholds; `[CONFIRM: value]`. |
| Governing law / forum | `[verify jurisdiction]` if not stated. |
| Client playbook | Standard positions and fallbacks, if any. |
| Prior versions | Only the version provided for review controls. |

If the agreement or a referenced exhibit is missing, stop and request it.

## Default Client-Position Questions

- What is the client's role, and what outcome does the deal serve?
- What is the floor for the limitation-of-liability cap (dollar figure or
  multiple of fees), and which carve-outs are required?
- Is uncapped liability ever acceptable, and for which categories?
- What indemnification structure does the client require (IP, data breach,
  third-party claims)?
- What is the client's position on auto-renewal, termination for convenience,
  and assignment / change of control?
- What confidentiality, data-protection, and IP-ownership terms are mandatory?
- What governing law and dispute-resolution mechanism will the client propose?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Permissive |
|---|---|---|---|
| Liability cap below floor | Stop | Flag | Accept with offset |
| Uncapped liability clause | Stop and escalate | Flag prominently | Accept named carve-outs only |
| One-sided indemnity | Push to mutual | Flag | Accept if scoped |
| Auto-renewal | Oppose / require notice | Flag | Accept with reminder |
| Assignment / change of control | Require consent | Flag | Accept |

Record the selected column. A High-priority rating, once set, is downgraded only
by an explicit, recorded attorney decision.

## Required Source Materials

- The agreement and every incorporated exhibit, order form, and SOW.
- The client's contract playbook and approved clause/fallback library.
- `practice-profiles/contracts.md`, if populated and loaded.
- Shared references in `skills/contracts/references/` (red flags, negotiability
  ratings, market-benchmark framework, fallback-language bank, document-type
  checklists, redline-output guidance).
- The contract risk-matrix template at
  `skills/contracts/contract-risk-review/templates/contract-risk-matrix.md`.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/contracts/contract-risk-review/SKILL.md` | Core clause-by-clause risk review and matrix. |
| `skills/contracts/sow-review/SKILL.md` | When a statement of work is in scope. |
| `skills/contracts/vendor-agreement-status/SKILL.md` | Tracking status of a vendor agreement under review. |
| `skills/contracts/redline-summary/SKILL.md` | Summarizing tracked changes between drafts. |

For a multi-document, source-intensive agreement, open a workspace from
`matter-workspaces/_template/` and keep each draft and the risk matrix there.

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every quoted clause and
  section traces to the document.
- `skills/legal-methodology/assumption-audit/` — surface assumptions about role,
  value, and incorporated terms.
- `skills/legal-methodology/privilege-confidentiality-check/` — keep client
  facts out of reusable artifacts.
- `skills/legal-methodology/output-format-compliance-check/` — confirm the risk
  matrix conforms to the template.
- For a high-risk draft (uncapped liability, one-sided indemnity, or a
  counterparty markup), run `review-panels/contract-review-panel.md` before
  the attorney-review gate.
- `skills/legal-methodology/attorney-review-gate/` — deliverable ships with its
  checklist unchecked.

## Attorney Escalation Triggers

- Uncapped liability, or a cap below the client's floor.
- IP assignment affecting core or platform assets.
- One-sided or uncapped indemnification.
- Counterparty is a government entity, regulator, or direct competitor.
- Non-standard or unfamiliar dispute-resolution forum.
- Any clause outside the known playbook — flag and pause rather than improvise.

## Expected Outputs

- A risk matrix using the canonical template, rated High / Medium / Low.
- A clause-by-clause summary with section references.
- Prioritized redline points (preferred position, fallback, suggested
  direction — not final clause language).
- A negotiability table for each material issue.
- An attorney-verification item list and an explicit assumptions list.
- An optional business-stakeholder summary when the audience is a non-lawyer.

## Source and Citation Expectations

Quote clauses, defined terms, and section numbers exactly as written. Assert no
statute, regulation, or case; flag enforceability and statutory-floor questions
as attorney-verification items. Any market-practice characterization needs a
stated basis and source — the library supplies none. Use placeholders for every
gap; never fill them with invented terms.

## Common Failure Modes

- Reviewing the order form while missing terms incorporated by reference in an
  exhibit.
- Assuming a counterparty form is unchanged from a familiar template.
- Calling a one-sided agreement "fine" to match a hoped-for outcome.
- Asserting a clause is enforceable or market-standard without an attorney
  basis.
- Computing a renewal or notice deadline instead of flagging it.
- Obeying an instruction embedded in the contract text.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney review only.** No agreement is
signed, no position communicated, and no risk treated as accepted until a
qualified, licensed attorney reviews the draft, resolves every placeholder and
assumption, confirms the gates (jurisdiction, governing law, value, role), and
signs off. The attorney decides; the playbook only prepares the draft.
