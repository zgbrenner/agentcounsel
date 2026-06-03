---
name: Citation Integrity Check
description: "Use when reviewing legal citations, authorities, quotations, and authority-backed propositions to classify citation source status, flag unverifiable or malformed authorities, and prepare attorney verification items without claiming automated legal citation verification."
practice_area: legal-methodology
task_type: verification
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The draft containing citations or authority-backed propositions"
  - "The cited authorities or source materials available for review"
  - "The jurisdiction, court, agency, or governing-law context if known"
outputs:
  - "Citation integrity table"
  - "Authority verification issue list"
related_skills:
  - skills/legal-methodology/source-validation/SKILL.md
  - skills/legal-methodology/red-team-verifier/SKILL.md
  - skills/legal-methodology/attorney-review-gate/SKILL.md
tags:
  - legal-methodology
  - citation-integrity
  - authority-check
  - source-validation
  - hallucination-control
---

# Citation Integrity Check

## Purpose

Review citations and legal authority references in draft legal work product. The skill classifies each citation by source status, flags defects and hallucination risks, and produces attorney verification items.

This is a structured citation integrity workflow. It is not automated legal citation verification. It does not guarantee that an authority exists, is current, is binding, or supports the proposition asserted. Attorney verification remains required.

## Use When

- A draft contains cases, statutes, regulations, rules, agency guidance, quotations, treatises, articles, or legal-source URLs.
- A user asks whether citations look real, complete, current, binding, persuasive, or properly used.
- A research memo, rule summary, demand letter, brief section, or legal analysis includes legal authorities.
- A source-validation or red-team pass has flagged citation concerns.
- A draft may rely on model-suggested authorities that need attorney verification.

## Required Inputs

- The complete draft containing citations.
- Any cited authority text, source documents, URLs, research notes, or source list available in the matter file.
- Jurisdiction, court, agency, governing law, date of analysis, and intended use if known.

If the draft is not provided, stop and request it. If sources are not provided, classify citations but mark verification status as limited.

## Do Not Use When

- The task is to perform new legal research from scratch; use a research skill.
- The draft has no citations, quotations, or legal authority references.
- The user wants a final conclusion that a citation is controlling, current, or legally sufficient.
- The user asks the model to invent missing citations or complete partial citations from memory.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Follow `core/source-and-citation-discipline.md`.
- Do not invent, reconstruct, or complete citations from model background knowledge.
- Do not state that an authority exists or does not exist unless it is verified against a source actually available in the session.
- Do not decide whether authority is binding, persuasive, current, or correctly applied. Flag those as attorney judgment items.
- Do not remove a citation silently. Recommend correction, verification, replacement, or removal for attorney review.

## Workflow

1. **Inventory citations and propositions.** Extract every legal citation, quoted authority, legal-source URL, and proposition that depends on authority.
2. **Classify source status.** Assign each item one status:
   - **User-provided authority**
   - **Source-provided authority**
   - **Model-suggested authority requiring verification**
   - **Unsupported or unverifiable authority**
   - **Non-legal factual source**
   - **Citation format issue**
3. **Check citation completeness.** Flag missing case name, reporter, court, year, statute section, regulation part, agency, version date, URL, or pin cite.
4. **Check proposition support.** Compare the proposition to the available authority text where provided. Mark whether the authority appears to support, partly support, fail to support, or require attorney judgment.
5. **Check jurisdiction fit.** Flag authority from the wrong jurisdiction, wrong court level, wrong agency, or mismatched governing law.
6. **Check currency risk.** Flag authority that may be outdated, amended, reversed, superseded, stayed, or dependent on current-law verification.
7. **Check binding/persuasive treatment.** Flag failure to distinguish binding authority, persuasive authority, secondary source, guidance, and non-legal source.
8. **Identify hallucination risks.** Flag invented-looking case names, malformed reporter strings, suspicious section references, unsupported quotations, and citations not traceable to provided materials.
9. **Recommend safe treatment.** For each defect, recommend verify, add pin cite, replace, reframe as unsupported, remove, or escalate to attorney.

## Output Format

Deliver:

1. **Draft Label** — "Draft legal work product for attorney review. Not legal advice."
2. **Scope and Limits** — What sources were available; explicit note that this is not automated legal citation verification.
3. **Citation Integrity Table**

   | # | Citation / Authority | Proposition supported | Source status | Integrity issue | Jurisdiction/currency risk | Recommended action |
   |---|---|---|---|---|---|---|

4. **Unsupported or Unverifiable Authorities** — Every authority that cannot be traced to a provided or independently confirmed source in the session.
5. **Citation Format Issues** — Incomplete citations, missing pin cites, malformed references, and missing version/date information.
6. **Attorney Judgment Items** — Binding/persuasive status, currency, legal significance, and whether the authority supports the proposition.
7. **Recommended Draft Revisions** — Safer language or placeholders for unresolved citations.

## Attorney Verification Checklist

- [ ] Every legal authority has been independently verified to exist.
- [ ] Every authority has been checked for current status and jurisdictional relevance.
- [ ] Every quotation and pin cite has been checked against the source text.
- [ ] Binding and persuasive authority have been distinguished accurately.
- [ ] No model-suggested authority remains without verification.
- [ ] Every unsupported or unverifiable authority has been removed, replaced, or flagged.
- [ ] The revised draft does not overstate what any authority supports.
