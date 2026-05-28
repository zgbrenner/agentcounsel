# Matter Profile

> **Blank template — contains no client facts.** Once populated this file becomes
> **draft legal work product for attorney review**, potentially privileged. Label
> and access-limit the populated copy. This is not legal advice.
>
> Privilege designation (populated copy): `[CONFIRM: attorney to designate — e.g., Privileged & Confidential — Attorney Work Product]`

## Matter Header

| Field | Value |
|---|---|
| Matter Name | `[CONFIRM: descriptive matter name]` |
| Anonymized Client Label | `[CONFIRM: e.g., "Client A" — keep client-identifying detail out of shared paths]` |
| Client Role | `[CONFIRM: e.g., Buyer, Employer, Disclosing Party, Plaintiff, Respondent]` |
| Opposing Party / Counterparty | `[CONFIRM: name or anonymized label, if applicable — else "N/A"]` |
| Practice Area | `[CONFIRM: e.g., contracts, litigation, privacy, employment, corporate, regulatory]` |
| Jurisdiction(s) | `[CONFIRM: governing law and relevant jurisdictions — verify jurisdiction]` |
| Supervising Attorney | `[CONFIRM: attorney name and bar admission]` |
| User Role | `[CONFIRM: e.g., associate, paralegal, in-house counsel, operations]` |
| Applicable Practice Profile | `[CONFIRM: e.g., practice-profiles/contracts.md]` |
| Selected Matter Pack | `[CONFIRM: e.g., matter-packs/m-and-a.md — or "none"]` |
| Applicable Playbook | `[CONFIRM: e.g., playbooks/nda-review.md — or "none"]` |
| Date Opened | `[CONFIRM: date]` |
| Status | `[CONFIRM: see matter_status.md]` |

## Privilege / Confidentiality Status

| Field | Value |
|---|---|
| Privilege Posture | `[CONFIRM: e.g., Privileged & Confidential — Attorney Work Product]` |
| Confidentiality Constraints | `[CONFIRM: NDA, protective order, ethical wall, or other limits]` |
| Distribution Limits | `[CONFIRM: who may access this matter file]` |

See `core/confidentiality-and-privilege.md` for the operating rules. See
`quality_checks/` for the privilege/confidentiality check record.

## Key Deadlines

> **Gate 2 — Required by `core/jurisdiction-and-deadline-gates.md`.** Every date
> must be independently verified by the supervising attorney. No date is computed
> by any agent or tool.

| # | Date | Event / Deadline | Source | Verification Status |
|---|---|---|---|---|
| 1 | `[CONFIRM: date]` [deadline verification required] | `[CONFIRM: event]` | `[CONFIRM: source]` | `[CONFIRM: attorney to verify]` |
| 2 | | | | |

## Source Documents

> The full documents index lives in `documents/README.md`; list the governing
> source materials here for quick reference.

| # | Document | Provided By | Location |
|---|---|---|---|
| 1 | `[CONFIRM: document name]` | `[CONFIRM]` | `documents/` |
| 2 | | | |

## Known Facts

> Maintained in detail in `facts.md`. Summarize the load-bearing established facts
> here. Each must be traceable to a source — do not record assumptions here.

- `[CONFIRM: established fact — see facts.md for source]`

## Disputed Facts

> Facts the parties dispute or that are not yet established. Detail in `facts.md`.

- `[CONFIRM: disputed fact]`

## Open Questions

> Maintained in `open_questions.md`. List the questions currently blocking or
> shaping the analysis.

- `[CONFIRM: open question]`

## Recommended Quality Checks

> The quality-layer passes recommended for this matter type. Run them and record
> results in `quality_checks/`.

- [ ] `skills/legal-methodology/source-validation/SKILL.md`
- [ ] `skills/legal-methodology/citation-integrity-check/SKILL.md`
- [ ] `skills/legal-methodology/assumption-audit/SKILL.md`
- [ ] `skills/legal-methodology/hallucination-red-team/SKILL.md`
- [ ] `skills/legal-methodology/privilege-confidentiality-check/SKILL.md`
- [ ] `skills/legal-methodology/attorney-review-gate/SKILL.md`
- [ ] `[CONFIRM: add or remove checks for this matter]`

## Attorney Escalation Triggers

> Stop and escalate to the supervising attorney immediately if any of these occur.

- Jurisdiction or governing law is unknown, disputed, or changes.
- Any deadline is uncertain, missed, or close.
- A required source is missing, ambiguous, or contradicted.
- An authority is needed that cannot be verified against an authoritative source.
- A privilege or confidentiality risk arises.
- The matter reaches a point requiring a legal conclusion, filing, signing, or
  external communication.
- `[CONFIRM: matter-specific escalation trigger]`
