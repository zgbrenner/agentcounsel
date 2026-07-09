# Playbook: Securities Disclosure Review

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes a recurring securities / capital-markets disclosure
> review; every skill it references produces a **draft for attorney review.** It
> decides nothing about whether a disclosure is adequate, whether an exemption
> applies, or whether a document may be filed or distributed — that is attorney
> work. Use fictional examples (e.g., "Contoso," "Issuer A") only.

## When to Use

An offering document, periodic report, risk-factor set, or other capital-markets
disclosure has been prepared and the client wants a review for internal
consistency, completeness against the relevant disclosure framework, and items
warranting attorney attention — before filing or distribution.

Use this playbook for disclosure-document review. Route a private-placement
process, a Section 16 filing, or a blue-sky tracking task to the specific
securities skills, and route the underlying corporate authorizations to
`corporate-governance-review.md`.

## Required Inputs

| Input | Notes |
|---|---|
| The disclosure document | Offering doc, report, or risk-factor set, complete. |
| Document type and framework | `[CONFIRM: form/framework]`; governs expectations. |
| Issuer and offering profile | Type, stage, prior disclosures. |
| Supporting / backup materials | Sources behind quantitative and factual claims. |
| Prior periodic disclosures | For a consistency comparison. |
| Jurisdiction / regime | `[verify jurisdiction]` if not stated. |

If the document or its supporting materials are missing, stop and request them.
Do not reconstruct disclosure language or figures from memory.

## Default Client-Position Questions

- What document type and disclosure framework apply, and what is the deadline
  posture (treat dates as unverified)?
- What are the issuer's principal risks, and how does the document characterize
  them?
- Which quantitative or forward-looking statements need backup verification?
- Is the disclosure consistent with the issuer's prior periodic filings?
- What is the client's tolerance for additional risk-factor or qualifying
  language?
- Which sections require specialist (accounting, tax, technical) sign-off?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Permissive |
|---|---|---|---|
| Forward-looking statements | Full safe-harbor framing, flagged | Cautionary language, flagged | As drafted |
| Risk-factor breadth | Broad, specific | Material risks covered | Streamlined |
| Inconsistency with prior filings | Stop; reconcile | Flag prominently | Flag |
| Unverified quantitative claim | Require backup | Flag for verification | Flag |

Record the selected column. A High-priority disclosure flag is downgraded only
by an explicit, recorded attorney decision.

## Required Source Materials

- The disclosure document and all incorporated exhibits.
- The backup materials supporting quantitative, factual, and forward-looking
  statements.
- The issuer's prior periodic disclosures for comparison.
- Shared references in `skills/securities-capital-markets/references/`.
- No statute, regulation, rule, or form requirement is supplied by the library;
  framework requirements are flagged for attorney verification.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/securities-capital-markets/offering-document-disclosure-review/SKILL.md` | Core offering-document disclosure review. |
| `skills/securities-capital-markets/risk-factor-review/SKILL.md` | Review and gap-check the risk factors. |
| `skills/securities-capital-markets/sec-filing-consistency-check/SKILL.md` | Consistency across filings and within the document. |
| `skills/securities-capital-markets/comfort-backup-request-tracker/SKILL.md` | Track backup behind numerical/factual claims. |
| `skills/securities-capital-markets/securities-exemption-issue-spotter/SKILL.md` | Spot exemption issues for attorney review. |

Open a workspace from `matter-workspaces/_template/` to track the document,
backup sources, and the consistency comparison.

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every factual and numerical
  statement traces to a backup source.
- `skills/legal-methodology/citation-integrity-check/` — no form requirement,
  rule, or figure is invented; cross-references are exact.
- `skills/legal-methodology/assumption-audit/` — surface assumptions about
  framework, materiality, and scope.
- `skills/legal-methodology/hallucination-red-team/` — challenge any asserted
  requirement or unsupported claim.
- For a high-risk disclosure draft (a new risk factor, a materiality call, or
  pre-filing timing), run `review-panels/regulatory-risk-panel.md` before the
  attorney-review gate.
- `skills/legal-methodology/attorney-review-gate/` — checklist ships unchecked.

## Attorney Escalation Triggers

- A material inconsistency between the document and prior disclosures.
- A quantitative or forward-looking statement without backup.
- A potential omission of a material risk factor.
- An exemption or framework-applicability question.
- A statement that could be read as a guarantee or projection without
  cautionary framing.
- Any section requiring specialist (accounting, tax, technical) sign-off.

## Expected Outputs

- A consistency and completeness review keyed to the document's sections.
- A risk-factor gap note flagging potential omissions for attorney confirmation.
- A backup-tracking list for unverified quantitative and factual claims.
- A list of inconsistencies between the document and prior disclosures.
- An attorney-verification item list and an explicit assumptions list.

## Source and Citation Expectations

Every factual statement, figure, and cross-reference must trace to the document
or its backup and be quoted exactly. No statute, regulation, rule, or form
requirement is cited from memory; framework and adequacy questions are flagged as
attorney-verification items, not answered. Filing dates and windows are stated as
supplied and flagged `[deadline verification required]`; the playbook never
computes them. Use placeholders for gaps; never invent a figure or a requirement.

## Common Failure Modes

- Concluding a disclosure "is adequate" or "complies" — an attorney-only
  judgment.
- Inventing a form requirement, rule citation, or financial figure.
- Asserting an exemption applies rather than flagging it.
- Missing an inconsistency between the document and a prior filing.
- Computing a filing deadline instead of flagging it.
- Treating a forward-looking statement as fact without cautionary framing.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney review only.** No document is
filed or distributed, no exemption treated as available, and no disclosure
treated as adequate until a qualified, licensed attorney reviews the draft,
confirms the gates (framework, jurisdiction, materiality, filing posture),
resolves every placeholder and assumption, and signs off. The attorney decides;
the playbook only prepares the draft.
