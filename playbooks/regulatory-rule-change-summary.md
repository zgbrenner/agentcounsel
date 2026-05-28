# Playbook: Regulatory Rule-Change Summary

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes how a recurring rule-change summarization task is
> run; the skill it references produces a **draft for attorney review.** It
> decides nothing about whether the client is in compliance, whether the rule
> applies, or what action is required — that is attorney work. Use fictional
> examples (e.g., "Contoso," "Client A") only.

## When to Use

A new or proposed rule, regulation, agency guidance, or enforcement policy has
issued, and the client wants a structured, plain-language summary of what
changed, who it appears to affect, and what areas may warrant follow-up — drawn
from the source text the client provides.

Use this playbook for summarizing a discrete rule or guidance document. Route a
full compliance-gap assessment, an enforcement-defense matter, or a comment-
letter drafting task to the relevant specialist skills and counsel.

## Required Inputs

| Input | Notes |
|---|---|
| The rule / guidance text | The actual document or its official citation. |
| Issuing body and status | Proposed, final, or guidance; `[CONFIRM: status]`. |
| Effective / comment dates | As stated in the source; never computed. |
| Client's sector and footprint | Which operations might be touched. |
| Prior rule or version | For a change comparison, if applicable. |
| Jurisdiction(s) | `[verify jurisdiction]` if not stated. |

If the rule text is not provided, stop and request it. Do not summarize from
memory of a regulation.

## Default Client-Position Questions

- Which of the client's products, services, or operations could fall within the
  rule's scope?
- Is the client seeking a neutral summary, a change comparison, or an
  impact-flagging read?
- Does the client intend to submit a comment (for a proposed rule)?
- What is the client's tolerance for early action versus waiting for a final
  rule?
- Which internal owners need to be briefed, and at what level of detail?
- Are there related rules or guidance the summary should cross-reference (by
  source only)?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Permissive |
|---|---|---|---|
| Scope interpretation | Assume in-scope, flag | Flag ambiguity | Note narrowly |
| Effective-date treatment | Flag for verification | State as written, flag | State as written |
| Impact characterization | Flag everything material | Prioritize | Highlight only top items |
| Action signal | Recommend attorney review of each item | Flag key items | Summarize only |

Record the selected column. A High-impact flag is downgraded only by an
explicit, recorded attorney decision.

## Required Source Materials

- The rule or guidance text itself (and the prior version, for a comparison).
- The issuing body's stated effective and comment dates, as written.
- The client's description of its sector and operations.
- Shared references in the `skills/regulatory/` skills.
- No regulation, statute, or guidance is quoted from memory; every quotation
  traces to the provided source or is a flagged placeholder.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/regulatory/rule-change-summary/SKILL.md` | Core plain-language change summary. |
| `skills/regulatory/compliance-gap-matrix/SKILL.md` | When a gap assessment follows the summary. |
| `skills/regulatory/enforcement-risk-memo/SKILL.md` | When enforcement exposure is in scope. |
| `skills/regulatory/compliance-program-tracker/SKILL.md` | To track follow-up obligations over time. |

Open a workspace from `matter-workspaces/_template/` when the rule is long or
the change comparison spans many provisions.

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every characterization traces
  to the provided rule text.
- `skills/legal-methodology/citation-integrity-check/` — the rule is cited
  exactly as provided; no section or number is invented.
- `skills/legal-methodology/assumption-audit/` — surface assumptions about scope
  and applicability.
- `skills/legal-methodology/hallucination-red-team/` — challenge any asserted
  requirement not in the source.
- `skills/legal-methodology/attorney-review-gate/` — checklist ships unchecked.

## Attorney Escalation Triggers

- Ambiguity about whether the client falls within the rule's scope.
- A short comment window or effective date requiring verification.
- A change that appears to impose a new substantive obligation.
- Conflict between the new rule and an existing obligation.
- Cross-jurisdictional or extraterritorial application.

## Expected Outputs

- A plain-language summary of what changed and what it requires (as written).
- A side-by-side change comparison, where a prior version exists.
- An applicability flag — operations that may be in scope, flagged for attorney
  confirmation.
- A follow-up list of items warranting attorney or compliance review.
- An attorney-verification item list and an explicit assumptions list.

## Source and Citation Expectations

Every requirement, threshold, and quotation must trace to the provided rule
text and be cited exactly as it appears there. No statute, regulation, or
guidance is summarized from memory. Effective dates and comment deadlines are
stated as written and flagged `[deadline verification required]`; the playbook
never computes a date. Use placeholders for anything not in the source.

## Common Failure Modes

- Summarizing a regulation from recollection rather than the provided text.
- Stating the client "is in scope" or "must comply" — a legal conclusion that is
  attorney-only.
- Inventing a section number, threshold, or deadline.
- Computing a comment or effective-date deadline rather than flagging it.
- Overstating or understating the significance of a change to match
  expectations.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney review only.** No applicability
conclusion is relied upon, and no compliance action is taken, until a qualified,
licensed attorney reviews the draft, verifies the rule text and every date,
resolves every placeholder and assumption, and signs off. The attorney decides
how the rule applies; the playbook only prepares the draft summary.
