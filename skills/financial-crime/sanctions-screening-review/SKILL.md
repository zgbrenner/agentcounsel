---
name: Sanctions Screening Review
description: "Use when reviewing sanctions, PEP, or adverse-media screening results for named parties to compare identifiers, classify each potential match by confidence, separate likely false positives from genuine hits, and recommend a disposition for compliance and attorney review."
practice_area: financial-crime
task_type: review
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The screening results: the alert list or hit report with screened name, list source, matched entry, and match score"
  - "Identifying data for the screened party (date of birth or formation date, nationality or jurisdiction, addresses, identifiers)"
  - "The firm's screening or alert-disposition policy, including match thresholds and false-positive criteria"
  - "The screening context: lists screened against, as-of date, and whether onboarding or ongoing monitoring"
outputs:
  - "Alert inventory and identifier-comparison match analysis"
  - "Confidence classification of each potential match"
  - "Recommended dispositions, escalations, and verification items"
related_skills:
  - skills/financial-crime/kyc-onboarding-review/SKILL.md
  - skills/financial-crime/transaction-monitoring-alert-triage/SKILL.md
  - skills/financial-crime/edd-file-review/SKILL.md
  - skills/regulatory/compliance-gap-matrix/SKILL.md
  - skills/regulatory/enforcement-risk-memo/SKILL.md
tags:
  - financial-crime
  - sanctions
  - screening
  - pep
  - adverse-media
  - alert-adjudication
---

# Sanctions Screening Review

## Purpose

Produce a structured, review-ready draft adjudication of sanctions, politically exposed person (PEP), and adverse-media screening results. The skill compares the screened party's identifiers against each matched list entry, classifies every potential match by confidence, separates likely false positives from genuine hits, and proposes a disposition for each alert.

This skill provides workflow discipline and analytical structure. It produces draft work product for review by the firm's compliance function and a supervising attorney. This is not legal advice and not an alert-clearing decision. A potential match is not a confirmed match, and a confirmed match is not by itself a finding of wrongdoing.

## Use When

- A user says "review these screening hits," "adjudicate these PEP matches," or "help me work through these sanctions alerts."
- A screening run — at onboarding or as part of ongoing monitoring — has generated potential matches that need first-pass review.
- A firm needs a structured comparison and confidence classification before a compliance officer dispositions alerts.

## Required Inputs

- **The screening results**: the actual alert list or hit report — the screened name, the list source for each hit, the matched list entry, and the match score where one is given. If no screening results are provided, stop and request them.
- **Identifying data for the screened party**: date of birth or formation date, nationality or jurisdiction, addresses, and any identifiers — so the screened party can be compared against the matched entry.
- **The firm's screening or alert-disposition policy**: the firm document setting out match thresholds, false-positive criteria, and escalation rules. If not provided, stop and request it. Do not apply thresholds from model background knowledge.
- **Screening context**: the lists screened against, the as-of date of the screening run, and whether this is onboarding or ongoing monitoring.

If the screening results or the disposition policy is missing, stop and request it.

## Do Not Use When

- Live screening is requested — this skill does not access sanctions, PEP, or adverse-media databases; it reviews results that are provided to it.
- No screening results are available — there is nothing to adjudicate.
- The user wants a final alert-clearing decision treated as authoritative — this skill produces a draft for the compliance function and counsel.
- The task is a full onboarding file rather than match adjudication — use `kyc-onboarding-review`, which incorporates a screening-review step.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft work product for review by the firm's compliance function and a supervising attorney. This is not legal advice and not an alert-clearing decision.
- Review only the screening results actually provided. Never fabricate hits, list entries, match scores, or list sources.
- Do not state that a party "is sanctioned," "is a PEP," or "is clear" as a conclusion. Classify match confidence and route the alert.
- A potential match is not a confirmed match; a confirmed match is not by itself a violation or a finding of wrongdoing. Flag matches for human disposition and counsel review.
- Cite the firm's disposition policy for any threshold or false-positive criterion applied.
- Distinguish: (a) the screened identity, (b) the matched list entry, (c) the identifier comparison, (d) the confidence classification, (e) the recommended disposition, (f) verification items.
- Use `[CONFIRM: ...]` placeholders for any identifier or list detail that cannot be resolved from the materials provided.
- Preserve confidentiality; do not place party-identifying data into reusable templates.
- Flag every uncertain match and every party that has not yet been screened.

## Workflow

1. **Confirm inputs.** Verify that screening results, identifying data for the screened party, and the firm's disposition policy are present. If any is missing, stop and request it.

2. **Inventory the alerts.** List every potential match as one row: screened name, list source, matched entry, match score if given.

3. **Compare identifiers.** For each alert, compare the screened party against the matched list entry attribute by attribute — name, date of birth or formation date, nationality or jurisdiction, identifiers, addresses. Record which attributes match, which do not, and which cannot be compared for lack of data.

4. **Classify match confidence.** For each alert, assign one classification, with the basis stated:
   - **Likely false positive**: identifiers materially diverge (for example, a name match but a clear date-of-birth or nationality mismatch).
   - **Possible match**: some identifiers align and others cannot be compared or are ambiguous.
   - **Likely true match**: identifiers align across the available attributes.
   - **Insufficient data**: too little identifying information to compare meaningfully.

5. **Note list context.** For each alert, record whether the hit is a sanctions listing, a PEP designation, or adverse media; the list source; and the severity implied by the list.

6. **Apply the disposition policy.** Apply the firm's thresholds and false-positive criteria, citing the policy provision.

7. **Recommend a disposition.** For each alert, recommend one of: discount as a false positive, escalate for compliance review, escalate as a likely true match, or hold pending more identifying data. Sanctions hits classified as possible or likely true matches always escalate to compliance and counsel.

8. **Identify escalation and verification items.** Flag every possible and likely true match, every insufficient-data alert, and any point requiring compliance or attorney judgment.

9. **Assemble the output.** Produce the structured output below and label it a draft.

## Output Format

Deliver the following sections in order:

**DRAFT SANCTIONS / PEP / ADVERSE-MEDIA SCREENING REVIEW — FOR COMPLIANCE AND ATTORNEY REVIEW ONLY**

1. **Inputs and Scope Summary** — the screening results reviewed, the lists and as-of date, the disposition policy applied (title, version, date), and any limitations on the analysis.

2. **Methodology Note** — a brief explanation of the confidence classifications and the disposition options, with the caveat that all classifications are workflow assessments subject to compliance and attorney verification and are not decisions.

3. **Alert Inventory** — table: alert id, screened name, list source, matched entry, match score.

4. **Match Analysis** — for each alert, an identifier-comparison table: attribute, screened value, matched-entry value, match / mismatch / not comparable.

5. **Confidence Classification Summary** — counts by classification; the alerts in each class.

6. **Recommended Dispositions** — table: alert id, classification, list context, recommended disposition, reason.

7. **Escalations** — alerts escalating to compliance and counsel, and why.

8. **Open Questions** — alerts with insufficient data, parties not yet screened, and identifiers to confirm.

9. **Attorney Verification Items** — see the Attorney Verification Checklist below.

## Attorney Verification Checklist

- [ ] Every alert in the review traces to the actual screening results provided; no hit, list entry, or match score was supplied from model background knowledge.
- [ ] The identifier comparison for each alert has been verified against the underlying records.
- [ ] Each confidence classification has been reviewed against the firm's screening and disposition policy.
- [ ] Every disposition labeled "discount as false positive" has been independently confirmed; identifier divergence is genuine and not an artifact of incomplete data.
- [ ] Every possible match and likely true match has been escalated to compliance and counsel; no sanctions match has been cleared without that review.
- [ ] Insufficient-data alerts have been resolved by obtaining the missing identifying information, not by default clearing.
- [ ] The list sources and the as-of date of the screening run are current enough for the decision being made.
- [ ] Every named party in scope has been screened; no party remains screening-pending.
- [ ] The disposition policy thresholds applied are the firm's current thresholds.
- [ ] All escalation items and open questions have been resolved before any alert is closed.
- [ ] The draft is labeled appropriately and has not been transmitted to any third party without compliance and attorney review.
