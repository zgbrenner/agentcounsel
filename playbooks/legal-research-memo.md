# Playbook: Legal Research Memo

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes how a recurring legal-research task is run; every
> skill it references produces a **draft for attorney review.** It does not
> state the law, predict an outcome, or conclude that any authority is
> currently good law — those are attorney judgments, made only after
> independent verification in a citator or primary source. Use fictional
> examples (e.g., "Contoso," "Client A") only.

## When to Use

A specific legal question needs a structured research memo — scoped, answered
using IRAC discipline, and built on authorities that are synthesized and
checked for negative treatment — before an attorney relies on the analysis.
Use this playbook for recurring research tasks: a question presented by
counsel, a client, or another skill's output.

Do not use it to draft a filing or brief section (route the finished research
to `skills/litigation/brief-section-drafter/SKILL.md`), or when the "research"
is really a rule-change summary from an official source (use
`regulatory-rule-change-summary.md`).

## Required Inputs

| Input | Notes |
|---|---|
| The legal question presented | Framed narrowly enough to scope; broadened later only with attorney sign-off. |
| Known facts | Labeled as user-stated; never assumed. |
| Jurisdiction | `[verify jurisdiction]` if not stated — governs which authorities are even in scope. |
| Any authority already provided | Cases, statutes, or secondary sources the user has in hand. |
| Time and scope constraints | What the attorney has authorized the research to cover. |
| Relevant date | The date "as of" which the analysis is framed. |

If the question, jurisdiction, or relevant date is missing, stop and request
it. Do not scope research on an assumed jurisdiction or date.

## Default Client-Position Questions

- What is the precise Question Presented, and has the attorney approved this
  scope before research begins?
- What facts are known, and which are assumed or still unconfirmed?
- What jurisdiction and relevant date apply, and are they confirmed?
- Has any authority already been supplied, or does the plan need to identify
  leads from scratch?
- What is the intended use of the memo — internal analysis, a brief section,
  or client-facing advice — since that changes the tone and hedging required?
- What time and scope constraints has the attorney set for this research?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Permissive |
|---|---|---|---|
| Rule-statement confidence | State only where multiple authorities agree | State the majority rule, flag the minority | State the best-supported reading with caveats |
| Minority/split authority | Always surface, never resolve | Surface and flag for attorney weighting | Note if directly on point |
| Older or unverified authority | Escalate for citator check before any reliance | Flag with a temporal-confidence caveat | Use with a visible caveat |
| Gaps in the record | Stop and request the missing authority | Flag as an open item | Note and proceed with the caveat recorded |

Record which column the supervising attorney selected. A rule statement, once
flagged as split or unverified, is not silently presented as settled — any
change is an explicit, recorded attorney decision.

## Required Source Materials

- The Question Presented and the known facts, as stated by the requester.
- Any authority already supplied by the user or a prior skill run.
- Jurisdiction- and date-scoping information.
- Shared references in `skills/legal-research/references/`, including
  `citation-type-taxonomy.md`.
- Where available, a citation-verification connector (e.g.,
  `connectors/courtlistener.md`) for federal case law — connectors return
  attributed source data, never a substitute for attorney verification.
- No case, statute, or regulation text is supplied by the library itself; every
  authority is either user-supplied, connector-returned and attributed, or a
  placeholder for attorney verification.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/legal-research/research-plan/SKILL.md` | Scopes the research into leads (statutes, case-law areas, search terms) — no citations, no analysis — for attorney approval before research begins. |
| `skills/legal-research/legal-research-memo/SKILL.md` | Core IRAC-structured memo answering the Question Presented. |
| `skills/legal-research/authority-synthesis/SKILL.md` | When the memo's rule statement must be synthesized from several authorities, with majority/minority and temporal-confidence handling. |
| `skills/legal-research/negative-treatment-check/SKILL.md` | When the cited authorities' current-law status must be organized into a verification plan before reliance. |

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every factual and legal
  claim in the memo traces to a provided document, a labeled user statement,
  or an attributed connector result.
- `skills/legal-methodology/citation-integrity-check/` — classify every
  citation's source status and flag any malformed or unverifiable authority.
- `skills/legal-methodology/assumption-audit/` — surface every assumption
  about facts, jurisdiction, or scope.
- For any memo relying on cited authority (which is nearly all of them), run
  `review-panels/citation-source-red-team-panel.md` before the attorney-review
  gate.
- `skills/legal-methodology/attorney-review-gate/` — checklist ships unchecked.

## Attorney Escalation Triggers

- Any authority whose current-law status is unverified or flagged by the
  negative-treatment check.
- A rule statement built on a genuine circuit or jurisdictional split.
- A gap in the record that the research plan cannot fill from supplied or
  connector-attributed sources.
- Any request to expand scope beyond what the attorney authorized.
- Any instance where the memo would need to predict an outcome rather than
  state the law as the authorities frame it.

## Expected Outputs

- A research-plan roadmap (leads only, no citations) for attorney approval,
  where the task starts from scratch.
- An IRAC-structured legal research memo (Question Presented, Brief Answer,
  Facts, Assumptions, Discussion/Analysis, Conclusion).
- Where multiple authorities are in play, a rule-synthesis worksheet with
  Holding/Relevance/Weight blocks and a majority/minority split.
- A negative-treatment verification plan and status classification for each
  cited authority.
- A citation integrity table and an attorney-verification item list.

## Source and Citation Expectations

Every citation is either user-supplied, drawn from an attributed connector
result, or a placeholder (`[VERIFY: citation]`) — never asserted from model
memory. No authority is presented as good law without a stated verification
status. Follow the source hierarchy in `core/source-and-citation-discipline.md`
and the classification vocabulary used across the quality layer. Any authority
without a stated verification path is flagged, not asserted.

## Common Failure Modes

- Stating a rule as settled when the authorities are split or unverified.
- Treating an older case as current law without a temporal-confidence check.
- Fabricating a citation, pincite, or quotation — the single highest-severity
  failure this playbook exists to prevent.
- Skipping the research-plan step and drafting the memo directly from
  assumed leads.
- Expanding scope beyond the attorney-approved Question Presented.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney review only.** No research memo
is relied upon, cited in a filing, or communicated to a client until a
qualified, licensed attorney has independently verified every authority's
current-law status, resolved every placeholder and assumption, confirmed the
jurisdiction and relevant date, and signed off. The attorney decides what the
law is; the playbook only organizes the research.
