---
name: NDA Review
description: "Use when reviewing a non-disclosure or confidentiality agreement to produce a triage rating (route, flag, or stop), a structured risk summary, and prioritized redline points for attorney review."
practice_area: contracts
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The full NDA or confidentiality agreement text"
  - "The client's role: disclosing, receiving, or mutual"
  - "The business and transaction context"
  - "Optional: the client's standard NDA positions or playbook"
outputs:
  - "Triage rating (route, flag, or stop)"
  - "Structured risk summary"
  - "Prioritized redline points for attorney review"
related_skills:
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/contracts/redline-summary/SKILL.md
tags:
  - contracts
  - nda
  - confidentiality
  - contract-review
  - risk-triage
---

# NDA Review

## Purpose

Produce a structured, attorney-ready review of a non-disclosure agreement (NDA) or confidentiality agreement. The skill identifies key terms, flags risk-allocation issues, assigns an overall triage rating, and proposes prioritized redline points. It produces draft legal work product for attorney review — not legal advice and not a final negotiating position.

## Use When

- A user asks to "review this NDA," "check this confidentiality agreement," or "tell me what's risky here."
- A counterparty has sent an NDA and the user needs a first-pass risk read.
- The user wants a route / flag / stop call on whether an NDA can move toward signature.
- The user wants a redline priority list before negotiation.
- The user wants a plain-language summary of an NDA's obligations.

## Required Inputs

- The full NDA text (uploaded or pasted). Do not review from a description alone.
- The client's role: disclosing party, receiving party, or mutual.
- The business context: what is being shared and why.
- The transaction context: whether this is a stand-alone commercial NDA, or part of an M&A, employment, or investment deal.
- Optional but recommended: the client's standard NDA positions or playbook — acceptable terms, "never accept" terms, mutuality default, required carve-outs, term and survival caps, and governing-law preferences. The review benchmarks against these where they are provided.

If the NDA text is not provided, stop and request it. Do not reconstruct or assume contract language.

## Do Not Use When

- The document is not an NDA (use `contract-risk-review` for general commercial agreements).
- The user needs a summary of tracked edits between drafts (use `redline-summary`).
- The confidentiality terms are one section of a larger commercial agreement (use `contract-risk-review`).
- The NDA is part of an M&A, employment, or investment transaction — confidentiality terms in those contexts carry deal-specific risk and should be reviewed with specialist counsel rather than triaged as a stand-alone commercial NDA.
- The request is for a statement of legal advice or a final negotiating position — those require an attorney.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Review only the language actually present in the provided document. Quote it accurately.
- Do not invent contract terms, defined terms, section numbers, or quotations.
- Do not invent statutes, regulations, or case law. If legal authority is relevant, mark it as an attorney verification item.
- Do not invent or assume deadlines. Treat any signing or negotiation deadline as user-supplied or unverified.
- A triage rating of GREEN ("clear to route for signature") is a workflow signal, not authorization to sign. Attorney review and sign-off remain required before any NDA is signed.
- Do not draft new clause language or restructure provisions. Propose the direction of a change and route substantive drafting to an attorney.
- Distinguish what the contract says from what you assume and from what the attorney must confirm.
- Preserve confidentiality and privilege: the review is attorney work product. Do not place client-sensitive facts into reusable templates.
- Flag every point of uncertainty rather than resolving it silently.

## Workflow

This skill draws on shared contract-review reference material in `skills/contracts/references/`: `red-flags.md` (red-flag catalogue), `negotiability-ratings.md` (six-rating negotiability rubric), `market-benchmark-framework.md` (benchmarking discipline and market-practice vocabulary), `fallback-language-bank.md` (sample preferred and fallback positions by clause type), `document-type-checklists.md` (per-document-type checklists), and `redline-output-guidance.md` (how to frame redline direction). Consult them at the steps noted below.

1. **Confirm inputs.** Verify you have the full NDA text, the client's role, and the transaction context. If anything is missing, request it before proceeding.
2. **Transaction-context check.** If the NDA is part of an M&A, employment, or investment transaction, stop and route the matter to specialist counsel (see Do Not Use When). Continue only for stand-alone commercial NDAs.
3. **Identify the structure.** Locate and label the core provisions: parties, definition of Confidential Information, permitted use, standard exclusions, term and survival, return/destruction, remedies, and governing law. Use the NDA checklist in `skills/contracts/references/document-type-checklists.md` to confirm nothing is overlooked.
4. **Red flags quick scan.** Run a fast first pass against the red-flag catalogue in `skills/contracts/references/red-flags.md`. Record each red-flag pattern present, or note that none surfaced in the scan. This scan orients the deeper review; it does not replace it.
5. **Scope check.** Scan for obligations that go beyond confidentiality — for example a standstill, exclusivity, non-solicitation, non-competition, IP assignment, a licensing grant, a right of first refusal, a most-favored-nation clause, broad arbitration, or a governing-law clause reaching beyond confidentiality disputes. Any such term means the document is more than an NDA: flag it prominently and raise the triage rating accordingly.
6. **Summarize each key term** in plain language, citing the section number as written.
7. **Assess risk allocation from the client's role.** A receiving party and a disclosing party care about opposite asymmetries; analyze from the client's actual position.
8. **Benchmark against the client's standard positions.** If a playbook was provided, note where the NDA matches it, where it deviates, and where any term hits a "never accept" position. Record any market comparison using the discipline in `skills/contracts/references/market-benchmark-framework.md`: characterize each relevant term with the controlled vocabulary (Common, Aggressive, Unusual, Depends on Leverage, Needs Attorney Confirmation), state the basis and supporting source, and flag every characterization not backed by a playbook, comparable, counterparty prior form, or attorney-supplied norm as an attorney-verification item. AgentCounsel does not supply market data.
9. **Flag missing or one-sided terms** — for example, no standard exclusions, a perpetual term on all information, broad injunctive-relief language, or unilateral obligations in a document labeled "mutual."
10. **Build the risk table** using `templates/nda-risk-table.md`.
11. **Rate negotiability.** For each material issue, assign one of the six negotiability ratings from `skills/contracts/references/negotiability-ratings.md` — Must Push, Strong Push, Business Call, Acceptable if Balanced, Low Priority, or Do Not Spend Leverage — with a one-line rationale drawn from leverage, who drafted the form, the deal value, and any regulatory floor.
12. **Draft prioritized redline points.** Rank issues High / Medium / Low. For each, following `skills/contracts/references/redline-output-guidance.md`, state: the issue, why it matters, a **Preferred Position**, a **Fallback Position**, and a **Suggested Redline Direction** — the direction of the change, not final clause language unless the user asks for it. Use `skills/contracts/references/fallback-language-bank.md` to help articulate preferred and fallback positions. Route substantive drafting to an attorney.
13. **Internal consistency check.** Confirm that defined terms, party names, cross-references, and section numbers are used consistently throughout the NDA. Flag any defined-but-unused term, used-but-undefined term, broken cross-reference, mismatched party label, or numbering gap.
14. **Assign an overall triage rating:**
    - **GREEN — clear to route for signature.** Terms are consistent with the client's role and standard positions; no obligations beyond confidentiality; no missing protection that matters for the client's role. Attorney sign-off is still required.
    - **YELLOW — flag for negotiation or approver review.** One or more terms deviate from the client's standard positions or are one-sided but not dealbreakers; or a playbook is silent on a material term; or the scope check found a non-confidentiality term that needs review.
    - **RED — stop and escalate.** A term hits a "never accept" position; there is a structural mismatch (such as unilateral obligations in a "mutual" NDA, or a perpetual term on all information); or the document carries significant non-confidentiality obligations or arises in an M&A, employment, or investment context.
15. **List attorney verification items** — governing-law implications, enforceability questions, every unverified benchmark, and anything requiring legal judgment.
16. **Draft a business-friendly summary.** Produce a short, plain-language summary for non-lawyer stakeholders: the overall posture, the few terms that matter most, what to push on and why, and what — if anything — would stop signature. Use the stakeholder-communication language patterns in `skills/contracts/references/negotiability-ratings.md`. Avoid legal jargon.
17. **Assemble the output** and label it as a draft for attorney review.

## Output Format

Deliver:

1. **Triage Rating** — GREEN / YELLOW / RED, with a one-line rationale.
2. **Summary** — 3-5 sentences: document type, client role, overall risk posture.
3. **Red Flags Quick Scan** — each red-flag pattern from `skills/contracts/references/red-flags.md` found in the NDA, or a note that none surfaced in the scan.
4. **Key Terms Table** — plain-language summary with section references.
5. **Scope Check** — whether the document contains obligations beyond confidentiality, and which.
6. **Risk Table** — from `templates/nda-risk-table.md`.
7. **Negotiability Table** — a table covering each material issue, with columns: Issue | Negotiability Rating | Basis | Recommended Lawyer Action. The Negotiability Rating is one of the six ratings defined in `skills/contracts/references/negotiability-ratings.md` (Must Push, Strong Push, Business Call, Acceptable if Balanced, Low Priority, Do Not Spend Leverage); the Basis is a one-line rationale.
8. **Market Practice Notes** — any market comparison, recorded using `skills/contracts/references/market-benchmark-framework.md`. Characterize each relevant term with the controlled vocabulary (Common, Aggressive, Unusual, Depends on Leverage, Needs Attorney Confirmation), state the basis and supporting source, and flag every characterization not backed by a playbook, comparable, counterparty prior form, or attorney-supplied norm for attorney verification. AgentCounsel does not supply market data.
9. **Prioritized Redline Points** — High / Medium / Low. Each point states the issue and why it matters, a **Preferred Position**, a **Fallback Position**, and a **Suggested Redline Direction** (direction of change, not final language), following `skills/contracts/references/redline-output-guidance.md`. Use `skills/contracts/references/fallback-language-bank.md` to help articulate preferred and fallback positions.
10. **Business-Friendly Summary** — a short, plain-language summary for non-lawyer stakeholders: the overall posture, the few terms that matter most, what to push on and why, and what — if anything — would stop signature. Avoid legal jargon.
11. **Internal Consistency Check** — whether defined terms, party names, cross-references, and section numbers are used consistently, with any inconsistency flagged.
12. **Attorney Verification Items** — open questions and items requiring legal judgment.
13. **Assumptions** — every assumption made, listed explicitly.

Use placeholders like `[CONFIRM: governing law]` wherever information is missing. Do not fill gaps with invented content.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The NDA text reviewed is complete and final.
- [ ] The client's role (disclosing / receiving / mutual) is correctly identified.
- [ ] The transaction context is confirmed; if the NDA arises in an M&A, employment, or investment deal, specialist counsel has been involved.
- [ ] The scope check is complete; if the document contains obligations beyond confidentiality, it has been reviewed as more than an NDA.
- [ ] All section references and quotations match the source document.
- [ ] No legal authority, statute, or case law has been asserted without verification.
- [ ] Enforceability of remedies and any restrictive covenants has been assessed under the governing law.
- [ ] Governing law and jurisdiction are appropriate for the client.
- [ ] Term and survival periods are acceptable for the type of information being shared.
- [ ] The triage rating and risk ratings reflect the client's standard positions, role, and leverage.
- [ ] The red-flag quick scan and the negotiability table have been reviewed; each of the six-scale negotiability ratings reflects the client's actual leverage and standard positions.
- [ ] Every market-practice characterization has a stated basis and supporting source; no market benchmark has been relied on without independent verification.
- [ ] Preferred and fallback positions reflect the client's actual leverage and standard positions.
- [ ] The business-friendly summary accurately reflects the review and neither overstates nor understates any risk.
- [ ] The internal consistency check is complete; defined terms and cross-references are sound.
- [ ] A GREEN rating has attorney sign-off before the NDA is signed.
- [ ] All assumptions and open items are resolved before the review is relied upon.
