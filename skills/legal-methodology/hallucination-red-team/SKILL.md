---
name: Hallucination Red-Team
description: "Use when stress-testing draft legal work product for hallucination risk by separating factual claims, legal claims, cited authorities, user-provided information, model-generated information, unsupported claims, uncertainty, and safer revisions."
practice_area: legal-methodology
task_type: verification
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The complete draft legal output to red-team"
  - "The user-provided facts, source documents, and cited authorities"
  - "The intended use and audience of the output"
outputs:
  - "Hallucination risk report"
  - "Safer revised version or not-ready finding"
related_skills:
  - skills/legal-methodology/red-team-verifier/SKILL.md
  - skills/legal-methodology/citation-integrity-check/SKILL.md
  - skills/legal-methodology/source-validation/SKILL.md
tags:
  - legal-methodology
  - hallucination-check
  - red-team
  - unsupported-claims
  - verification
---

# Hallucination Red-Team

## Purpose

Force a draft legal output to account for every factual claim, legal claim, cited authority, user-provided fact, model-generated statement, unsupported claim, and uncertainty marker. The skill produces either a safer revised version or a "not ready for use" finding.

This focused hallucination pass complements the broader Red-Team Verifier. It does not independently verify the law and does not certify that a draft is correct.

## Use When

- A draft contains legal claims, factual claims, citations, quotations, or confident conclusions that may be unsupported.
- A user asks for a hallucination check, unsupported-claim audit, or safer revised version.
- A draft will be sent externally, filed, used in a client communication, or relied on for a high-risk decision.
- A model produced the draft without a clear claim/source table.

## Required Inputs

- The complete draft to red-team.
- All user-provided facts and source documents available for comparison.
- Any cited authorities, research notes, or source lists.
- The intended use and recipient.

If the draft is missing, stop and request it. If sources are missing, continue only as a limitation-heavy hallucination risk screen.

## Do Not Use When

- The user wants new legal analysis instead of a verification pass.
- The output has no claims to audit.
- The user asks for a final certification that no hallucinations exist.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Do not claim the absence of hallucinations. State only what was checked and what remains unresolved.
- Do not invent sources, facts, citations, or safer substitute law.
- Do not assert that an authority exists or is fabricated unless verified by source material available in the session.
- Preserve privilege and confidentiality.

## Workflow

1. **Segment the draft.** Break the draft into discrete factual claims, legal claims, citations, quotations, assumptions, recommendations, and conclusions.
2. **Classify information origin.** For each item, mark whether it is user-provided, source-provided, model-generated, inferred, or unclear.
3. **Inventory authorities.** List every authority, citation, quotation, source URL, statute, rule, case, regulation, or guidance reference.
4. **Flag unsupported claims.** Mark claims with no source, insufficient source support, contradicted source support, unclear origin, or overbroad phrasing.
5. **Flag authority risks.** Mark invented-looking or unverifiable authorities, missing pin cites, jurisdiction mismatch, outdated authority risk, and unsupported legal propositions.
6. **Mark uncertainty.** Add or recommend `[CONFIRM: ...]`, `[VERIFY: ...]`, `[citation needed]`, `[pin cite needed]`, `[verify jurisdiction]`, and `[deadline verification required]` markers where needed.
7. **Decide readiness.** If material unsupported claims, authority risks, or missing gates remain, mark "not ready for use." Otherwise mark "ready for attorney review," not final use.
8. **Revise safely.** Produce a safer revised version only where the revision removes overclaiming, labels uncertainty, or narrows to supported facts. Do not supply missing law.

## Output Format

Deliver:

1. **Draft Label** — "Draft legal work product for attorney review. Not legal advice."
2. **Readiness Finding** — Ready for attorney review / Not ready for use, with reasons.
3. **Claim-Origin Table**

   | # | Claim | Type | Origin | Support status | Risk | Required action |
   |---|---|---|---|---|---|---|

4. **Authority Risk Table**

   | Authority | Use in draft | Verification status | Hallucination risk | Required action |
   |---|---|---|---|---|

5. **Unsupported Claims List**
6. **Uncertainty Markers To Add**
7. **Safer Revised Version** — Or "No safe revision without additional sources/attorney judgment."
8. **Attorney Verification Checklist**

## Attorney Verification Checklist

- [ ] Every factual claim is traced to user-provided or source-provided material, or is marked as unsupported.
- [ ] Every legal claim is supported by verified authority or flagged for attorney research.
- [ ] Every cited authority and quotation has been independently checked.
- [ ] Model-generated claims have been removed, sourced, or marked for verification.
- [ ] Jurisdiction and deadline gaps are resolved or visibly flagged.
- [ ] The revised draft does not present unsupported analysis as settled law.
- [ ] The output is ready for attorney review only; it has not been treated as final.
