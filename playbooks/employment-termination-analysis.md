# Playbook: Employment Termination Analysis

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes a recurring termination-risk analysis; every skill it
> references produces a **draft for attorney review.** It decides nothing about
> whether a termination is lawful, whether a claim would succeed, or whether the
> separation may proceed — that is attorney work. Use fictional examples
> (e.g., "Contoso," "Employee A") only; never real personnel facts.

## When to Use

A client is considering separating or terminating an employee and wants a
structured risk read before any decision is finalized or communicated — covering
the stated reason, the employee's protected characteristics and activity, recent
performance and complaint history, and any contractual or policy constraints.

Use this playbook for individual separations. Route a reduction-in-force, a
discrimination charge already filed, or an active litigation matter to
specialist counsel and the litigation playbooks.

## Required Inputs

| Input | Notes |
|---|---|
| Jurisdiction(s) of employment | `[verify jurisdiction]`; drives applicable regimes. |
| Employee status | Exempt/non-exempt, at-will, contract, union — confirmed. |
| Stated reason for separation | As articulated by the client. |
| Performance and disciplinary record | Documents, dates, reviewers. |
| Protected status / activity (known) | Leave, complaints, accommodation requests. |
| Governing documents | Offer letter, agreement, handbook, policies, any CBA. |

If the stated reason or the relevant documents are missing, stop and request
them. Treat all personnel facts as confidential.

## Default Client-Position Questions

- What outcome does the client want, and on what timeline (treat dates as
  unverified)?
- Is the separation framed as performance, conduct, restructuring, or mutual?
- What documented performance or disciplinary history supports the stated
  reason?
- Has the employee recently taken protected leave, raised a complaint, or
  requested an accommodation?
- Is the employee subject to an employment agreement, severance plan, or CBA?
- Is the client offering severance, and on what conditions (e.g., a release)?
- What is the client's risk tolerance for a claim versus the cost of severance?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Aggressive |
|---|---|---|---|
| Recent protected activity | Pause; escalate | Flag and document basis | Proceed with documentation |
| Thin documentation of reason | Build record first | Flag gap | Proceed |
| Severance / release offered | Offer with full release | Case-by-case | Minimal / none |
| Communication timing | Hold for review | Coordinate with counsel | Proceed on client timeline |

Record the selected column. A High-risk flag is downgraded only by an explicit,
recorded attorney decision.

## Required Source Materials

- The employee's offer letter, any employment or arbitration agreement, and the
  applicable handbook and policies.
- The performance and disciplinary record, with dates and authors.
- Any severance plan or template release.
- Shared references in `skills/employment/references/`.
- No statute or regulation text is supplied by the library; applicable-law
  questions are flagged for attorney verification, never answered.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/employment/termination-risk/SKILL.md` | Core termination-risk read. |
| `skills/employment/severance-review/SKILL.md` | When a separation/release package is in scope. |
| `skills/employment/protected-leave-review/SKILL.md` | When recent leave is a factor. |
| `skills/employment/worker-classification/SKILL.md` | If status (employee vs. contractor) is in question. |
| `skills/employment/internal-investigation/SKILL.md` | When the reason follows a complaint or investigation. |

Open a workspace from `matter-workspaces/_template/` to track facts, the
chronology, and drafts when the history is complex.

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every fact traces to a
  provided document or a labeled user statement.
- `skills/legal-methodology/assumption-audit/` — surface assumptions about
  status, timeline, and protected activity.
- `skills/legal-methodology/privilege-confidentiality-check/` — treat the
  analysis as privileged; keep personnel facts out of templates.
- `skills/legal-methodology/hallucination-red-team/` — challenge any asserted
  legal conclusion or invented authority.
- For a high-risk termination (a protected-characteristic or recent-complaint
  fact pattern), run `review-panels/litigation-risk-panel.md` before the
  attorney-review gate.
- `skills/legal-methodology/attorney-review-gate/` — checklist ships unchecked.

## Attorney Escalation Triggers

- Recent protected leave, complaint, accommodation request, or whistleblowing.
- A stated reason unsupported by contemporaneous documentation.
- An employee subject to a contract, CBA, or for-cause standard.
- A prior settlement, charge, or pending claim involving the employee.
- Cross-border or multi-state employment.
- Any signal the separation could be perceived as retaliatory.

## Expected Outputs

- A structured risk read identifying potential exposure areas (flagged, not
  adjudicated).
- A timeline of relevant events, with each date treated as user-supplied.
- A documentation-gap list — what the record does and does not support.
- A draft severance/release outline for attorney review, if requested.
- An attorney-verification item list and an explicit assumptions list.

## Source and Citation Expectations

No statute, regulation, or case is cited; applicable-law and enforceability
questions are flagged as attorney-verification items. Dates are never computed —
notice periods, leave windows, and limitations periods are flagged
`[deadline verification required]`. Every fact is labeled by source. Use
placeholders for gaps; never infer a protected status or a fact not in the
record.

## Common Failure Modes

- Concluding a termination "is lawful" or "is fine" — a legal conclusion that is
  attorney-only.
- Missing recent protected activity because the record was read too quickly.
- Computing a leave or limitations deadline instead of flagging it.
- Treating the client's framing of the reason as established fact.
- Letting a hoped-for outcome soften a real retaliation or discrimination risk.
- Placing identifiable personnel facts into a reusable artifact.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney review only.** No separation
decision is finalized, and nothing is communicated to the employee, until a
qualified, licensed attorney reviews the draft, resolves every placeholder and
assumption, confirms the gates (jurisdiction, status, governing documents,
relevant dates), and signs off. The attorney decides; the playbook only prepares
the draft.
