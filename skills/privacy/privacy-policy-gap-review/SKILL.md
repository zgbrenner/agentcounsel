---
name: Privacy Policy Gap Review
description: "Use when reviewing a published privacy policy or privacy notice to identify gaps, internal inconsistencies, and discrepancies between what the policy says and the organization's described actual data practices."
practice_area: privacy
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The published privacy policy or notice"
  - "A description of the organization's actual data practices"
  - "The applicable products and processing context"
outputs:
  - "Gap table comparing the policy to actual practice"
  - "Recommendations for attorney review"
related_skills:
  - skills/privacy/dpa-review/SKILL.md
  - skills/privacy/dsar-workflow/SKILL.md
  - skills/privacy/pia-generation/SKILL.md
tags:
  - privacy
  - privacy-policy
  - gap-analysis
  - policy-review
  - disclosures
---

# Privacy Policy Gap Review

## Purpose

Produce a structured, attorney-ready gap review of a published privacy policy or privacy notice. The review identifies: missing standard disclosure topics, vague or boilerplate language that may not reflect actual practice, internal inconsistencies within the policy, and discrepancies between the policy's representations and the organization's actual data practices as described by the user. It produces draft legal work product for attorney review — not legal advice.

This skill provides structural and drafting analysis only. It does not certify compliance with any specific privacy law, regulation, or jurisdiction. Whether any identified gap constitutes a legal violation — and what remediation is legally required — are attorney-verification items. The applicable law, the organization's compliance posture, and the jurisdictional scope of the policy must be determined by counsel.

## Use When

- A user asks to "review our privacy policy," "find gaps in this privacy notice," or "does our policy match what we actually do."
- An organization is updating its privacy policy and wants a first-pass review before attorney review and redrafting.
- A privacy audit or assessment requires a document review of the current privacy notice.
- An organization has changed its data practices (new vendor, new product feature, new data collection) and needs to identify whether the policy needs to be updated.
- Due diligence on a transaction requires review of the target's public-facing privacy representations.
- A regulator or counterparty has raised concerns about the organization's privacy policy and the legal team needs a structured analysis.
- The organization operates in multiple jurisdictions and wants to identify disclosure topics that may need to be addressed for different audiences `[CONFIRM: applicable requirements with counsel]`.

## Required Inputs

- **The privacy policy or privacy notice text** — uploaded, pasted, or linked. If not provided, stop and request it. Do not fabricate or assume policy terms.
- **A description of the organization's actual data practices** — what personal data is collected, from whom, for what purposes, who it is shared with, how it is processed, and how long it is retained. This description must come from the user; do not invent practices. If this description is not provided, the practice-versus-policy comparison step cannot be completed — note the gap and proceed with a structural review only, flagging the comparison as an open item.
- Optional: the organization's industry or sector (e.g., healthcare, financial services, children's services, e-commerce) — relevant for identifying sector-specific disclosure topics to flag, though applicable law is always `[CONFIRM]`.
- Optional: the audience or jurisdictions the policy is intended to serve (e.g., EU residents, California residents, global) — used to identify disclosure topics commonly associated with those audiences, not to assert applicable law.
- Optional: a prior version of the policy, if this is a revision review.

If the policy text is missing, stop and request it. If the description of actual practices is missing, proceed with structural review only and flag the practice comparison as incomplete.

## Do Not Use When

- The document is a DPA, not a public-facing privacy policy (use `dpa-review`).
- The task is to handle a specific data subject rights request (use `dsar-workflow`).
- The task is to draft a new privacy policy from scratch — this skill reviews an existing document; drafting requires attorney involvement.
- The user needs a legal opinion on compliance with a specific law — that requires an attorney and is beyond this skill's scope.
- The user wants to review privacy terms in a contract or vendor agreement (use `dpa-review` or `contract-risk-review`).

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Do not assert which privacy law, regulation, or framework applies to the organization or its policy. Applicable law is always an attorney-verification item, even where the applicable framework seems obvious.
- Do not conclude that a gap constitutes a legal violation, regulatory breach, or non-compliance. Identify gaps; attorneys determine legal consequences.
- Do not invent or assume data practices not described by the user. The practice comparison must be grounded in user-provided information only.
- Do not quote or characterize the policy text inaccurately. Quote the document directly when characterizing its terms. Note the section or paragraph for each finding.
- Distinguish clearly: (1) what the policy says, (2) what the user describes as actual practice, (3) what you are assuming about industry norms or common disclosure topics, (4) what requires attorney legal determination.
- Do not place client-sensitive business information (undisclosed practices, deal-specific data flows) into reusable template materials.
- Common disclosure topics flagged in this review reflect widely observed practice patterns, not verified legal requirements. Whether any topic is legally required for this organization is `[CONFIRM]`.
- Use `[CONFIRM: ...]` for every point where the legal consequence, applicable requirement, or factual context is uncertain.
- Flag but do not resolve: internal inconsistencies, vague representations, and potential mismatches between policy and practice. Each is an attorney review item.

## Workflow

1. **Confirm inputs.** Verify that the policy text has been provided. Note whether a description of actual practices has been provided; if not, flag the practice-comparison steps as incomplete and proceed with structural review only.

2. **Identify the document.** Note the policy title, version or "last updated" date (if stated), and any stated scope or audience (e.g., "this policy applies to residents of..."). Flag if the document has no version date or if the date appears significantly outdated.

3. **Map the policy structure.** List the sections and topics the policy currently addresses. Identify the overall organization and navigation — whether a reader can quickly find key information such as what data is collected, how it is shared, and how to exercise rights.

4. **Check for standard disclosure topics.** Review the policy against a checklist of commonly addressed disclosure topics. For each, note: present and substantive, present but vague or generic, or absent. Standard topics to check include:
   - Identity and contact information for the organization and any privacy contact or DPO `[CONFIRM if DPO designation is required]`
   - Categories of personal data collected
   - Sources of personal data (direct collection, third parties, inference)
   - Purposes and legal basis for processing `[CONFIRM: legal basis requirements depend on applicable law]`
   - Data retention periods or criteria
   - Data sharing — categories of recipients and purposes
   - Third-party advertising, analytics, or tracking technologies (cookies, pixels, SDKs)
   - Cross-border data transfers and mechanism `[CONFIRM: applicable requirements]`
   - Data subject rights and how to exercise them `[CONFIRM: which rights apply under applicable law]`
   - Right to lodge a complaint with a supervisory authority `[CONFIRM: applicable]`
   - Automated decision-making and profiling `[CONFIRM: applicable]`
   - Children's privacy and age restrictions `[CONFIRM: applicable law and age threshold]`
   - Sensitive or special-category data (if collected) `[CONFIRM: definition and requirements]`
   - Security measures (general description)
   - Policy update and notification procedure
   - Effective date and version history

5. **Assess language quality.** For each section present, assess: (a) whether the language is specific to this organization or is generic boilerplate that may not reflect actual practice; (b) whether the language is internally consistent; (c) whether the language is clear enough for the intended audience. Flag vague formulations such as "we may share your data with partners," "we collect data to improve our services," or "we use industry-standard security measures" — these are common and may be substantively incomplete.

6. **Compare policy to described actual practices (if practices provided).** For each described actual practice, assess whether it is: (a) accurately and fully disclosed in the policy; (b) partially disclosed with gaps; (c) not disclosed. Flag mismatches. Do not infer practices beyond what the user has described. Note: the absence of a practice from the user's description does not confirm the policy is accurate — flag completeness of the practices description as an open item for attorney review.

7. **Identify undisclosed data sharing or third parties.** Based on practices described by the user, flag any categories of third parties (advertising networks, analytics providers, data brokers, service providers, affiliates) that appear in the practices description but are not disclosed in the policy. If no practices description is available, flag common high-risk omission categories for attorney review.

8. **Identify outdated or stale references.** Flag: law or regulation references that may be outdated; links or contact details that appear broken or stale; references to products, features, or entities that no longer exist or have been renamed.

9. **Check for internal inconsistencies.** Identify provisions within the policy that contradict each other (e.g., "we do not sell personal data" in one section and "we may share your data with advertising partners for their own use" in another). Note section references for each inconsistency.

10. **Build the gap table.** Organize findings into a structured gap table (see Output Format) with: Topic, Policy Status (present/vague/absent), Practice Match (if practices provided), Risk/Priority (High/Med/Low), and Recommended Action.

11. **Draft prioritized recommendations.** Organize recommendations: (1) High priority — absent disclosures relating to actual practices, significant internal inconsistencies, or topics commonly subject to regulatory scrutiny; (2) Medium priority — vague language, incomplete disclosures, or topics that may be required under one or more applicable frameworks; (3) Low priority — drafting improvements, clarity enhancements, and housekeeping items.

12. **List attorney verification items.** Enumerate every open legal question — applicable law, required disclosures, legal basis requirements, DPO designation, children's law thresholds, cross-border transfer requirements — that requires attorney judgment.

13. **Assemble output** and label it as draft legal work product for attorney review.

## Output Format

Deliver the following, in order:

1. **Summary** — one paragraph identifying the policy reviewed, its stated date and scope, the nature of the review (structural only, or structural plus practice comparison), and the top three to five findings.

2. **Document Overview** — policy version/date, stated audience or scope, overall structure assessment (navigability, completeness at a glance).

3. **Gap Table** — a structured table with the following columns:

   | # | Topic | Policy Status | Practice Match | Priority | Recommended Action | Attorney Note |
   |---|---|---|---|---|---|---|

   Policy Status: Present and specific / Present but vague / Absent.
   Practice Match (if practices provided): Matches / Partial / Undisclosed / Unknown.
   Priority: High / Med / Low.

4. **Vague Language Flags** — a list of specific policy provisions identified as generic boilerplate or insufficiently specific, with the quoted text and recommended improvement direction.

5. **Internal Inconsistencies** — a list of any provisions that contradict each other within the policy, with section references.

6. **Prioritized Recommendations** — organized as High / Medium / Low, with plain-language description of each issue and recommended action direction.

7. **Attorney Verification Items** — see the Attorney Verification Checklist below.

8. **Assumptions** — explicit list of every assumption made in the review (about practices, audience, industry norms, etc.).

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The applicable privacy law(s) and regulatory framework(s) have been confirmed; the gap review has been assessed against their specific requirements.
- [ ] Every "absent" or "vague" disclosure topic has been assessed by counsel to determine whether it is legally required for this organization, its audience, and its data practices.
- [ ] The legal basis for each processing purpose has been confirmed and, where required to be disclosed, is accurately stated in the policy.
- [ ] Whether a Data Protection Officer or privacy contact must be designated and disclosed has been confirmed under applicable law.
- [ ] Children's privacy requirements, including age thresholds for consent, have been confirmed and are accurately reflected.
- [ ] Applicable data subject rights — including which rights apply, how they may be exercised, and any applicable timeframes — have been confirmed and are accurately and completely disclosed.
- [ ] Cross-border transfer disclosures and mechanisms have been confirmed as current and legally valid.
- [ ] Automated decision-making and profiling disclosures, if required, have been confirmed.
- [ ] The practice-versus-policy comparison is based on a complete and accurate description of actual data practices — the user's description has been verified as current and exhaustive.
- [ ] All identified mismatches between policy and practice have been assessed for legal and regulatory risk.
- [ ] Internal inconsistencies have been resolved, not just flagged.
- [ ] The policy update and notification procedure complies with applicable requirements.
- [ ] All `[CONFIRM: ...]` placeholders in the gap table and recommendations have been resolved before remediation work begins.
- [ ] Privilege and confidentiality designations are appropriate for the matter, particularly where undisclosed practices are discussed.
