---
name: Privacy Impact Assessment
description: "Use when drafting an internal privacy impact assessment for a new or changed processing activity to document the data involved, design-linked risks, policy consistency, and mitigations for privacy-counsel review."
practice_area: privacy
task_type: drafting
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "A description of the new or changed processing activity"
  - "The data categories involved"
  - "The data flows, recipients, and design details"
outputs:
  - "Draft privacy impact assessment documenting risks and mitigations for privacy-counsel review"
related_skills:
  - skills/privacy/privacy-policy-gap-review/SKILL.md
  - skills/privacy/dpa-review/SKILL.md
  - skills/privacy/dsar-workflow/SKILL.md
  - skills/ai-governance/model-risk-triage/SKILL.md
  - skills/product-legal/ai-feature-review/SKILL.md
tags:
  - privacy
  - pia
  - dpia
  - impact-assessment
  - data-protection
---

# Privacy Impact Assessment

## Purpose

Produce a structured, attorney-ready draft Privacy Impact Assessment (PIA) for a proposed or recently changed processing activity. The PIA documents what personal data is involved, how it flows, where the activity may diverge from the organization's stated privacy commitments, what risks are specific to the design, and what mitigations with assigned owners would reduce those risks. The output is a draft for privacy-counsel review and sign-off — not an approval of the processing activity, not legal advice, and not a determination that any assessment is legally required.

Whether a formal Privacy Impact Assessment or Data Protection Impact Assessment (DPIA) is legally mandated for a given activity — and under which framework — is a legal determination that must be resolved by privacy counsel. This skill supports the internal scoping and drafting process; it does not resolve that determination.

## Use When

- A product, engineering, or business team is launching a new feature, vendor integration, or processing activity that involves personal data, and an internal PIA is needed before sign-off.
- An existing processing activity is being materially changed — expanded data categories, new access paths, new subprocessors, changed retention, or changed purpose — and the PIA must be updated.
- Privacy counsel or a data-protection officer has asked for a PIA draft as an input to their review.
- A procurement or legal-ops team needs a structured first-pass assessment before routing to privacy counsel.
- Internal policy requires a PIA for new processing activities, and a structured draft is needed to initiate that workflow.

## Required Inputs

- **Description of the processing activity**: what the feature, system, vendor use, or change does in functional terms. If not provided, stop and request it.
- **Data categories**: the specific fields or data elements involved — not generic labels like "user data" or "personal information." If only generic labels are provided, request specifics before proceeding.
- **Data subjects**: who the personal data relates to (e.g., customers, employees, job applicants, minors, website visitors). If unknown, flag as `[CONFIRM: data subjects]`.
- **Purpose of processing**: the stated business or functional purpose for which the data is collected or reused.
- **New collection or reuse**: whether this activity involves collecting data for the first time or reusing previously collected data for a new purpose.
- **Access**: who within the organization, and which systems, can access the data; whether access is role-restricted.
- **Storage**: where the data is stored (jurisdiction, cloud region, on-premises) and who controls the infrastructure.
- **Retention period**: how long the data is kept and what triggers deletion or archival. If unknown, flag as `[CONFIRM: retention period — [deadline verification required]]`.
- **Vendors and subprocessors**: any third parties that receive, process, or store the data, or that provide infrastructure used to process it.
- **Failure modes**: known or foreseeable failure scenarios — breach, unauthorized access, data loss, misuse, re-identification.

Optional but recommended:
- The organization's current privacy policy or privacy notice (used to perform the policy-consistency check in Step 5).
- Any prior triage memo, preliminary PIA, or risk log for this activity.
- The organization's PIA house style or template preferences (if the output should conform to an internal format).
- The practice group's `practice-profiles/privacy.md` if it has been populated and is loaded alongside this skill. If present, the skill uses its Standard Positions and Preferred Output Style tables to benchmark the PIA against the group's standing template, risk-rating rubric, and approval routing. If absent, the skill proceeds without practice-profile benchmarking and asks the user to supply standing positions inline if needed.

If the description of the processing activity or the data categories are not provided, stop and request them. Never fabricate processing details, invent data fields, or assume purpose from context.

## Do Not Use When

- The task is to determine whether a PIA or DPIA is legally required for a specific activity under any applicable law or regulation — that is a legal determination; escalate to privacy counsel with the activity description and inputs gathered here.
- The task is to approve or reject a processing activity — the draft recommendation in this PIA is a draft for privacy-counsel sign-off, not a binding decision.
- The task is to prepare a regulator-specific filing or submit a DPIA to a supervisory authority — regulatory filing requirements vary by jurisdiction and require attorney preparation.
- The task is to review a published privacy policy for gaps or compliance issues (use `privacy-policy-gap-review`).
- The task is to review a data processing agreement with a vendor (use `dpa-review`).
- The task is to handle a data subject access or deletion request (use `dsar-workflow`).

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice. Privacy-counsel review and sign-off are required before any processing activity is approved or any PIA is treated as final.
- Do not assert which privacy law, regulation, or framework applies to this activity, or whether a formal assessment is legally required. Those are attorney-verification items. Flag them as `[verify jurisdiction]` and route to privacy counsel.
- Do not invent, infer, or assume data categories, purposes, access paths, or retention periods. Assess only the facts actually provided. If a material input is missing, flag it as `[CONFIRM: ...]` and note how the gap affects the analysis.
- Treat the agent's background knowledge of legal rules, regulatory standards, and enforcement positions as unverified. Do not cite statutes, regulations, or regulatory guidance as governing authority.
- Separate facts (what was provided), assumptions (what has been inferred and flagged), analysis (the assessment of risk and policy consistency), and open items (what the attorney must resolve).
- Risks must be design-specific. Do not include generic risks such as "there could be a data breach" or "the organization could face non-compliance." Each risk must be grounded in a specific design feature, access pattern, disclosed purpose, sharing arrangement, or rights gap identified in the inputs.
- The recommendation section — approve, approve with conditions, changes required, or not approved — is a draft recommendation for privacy-counsel sign-off. It is not a decision. Do not frame it as a decision.
- Preserve confidentiality and privilege. Keep client-sensitive facts and deal-specific details out of any reusable copy of the template.
- Flag all uncertainty with `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, `[deadline verification required]`, or `[citation needed]` as appropriate. Never resolve uncertainty silently.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/privacy.md` is loaded, its Standard Positions and Preferred Output Style inform the draft but never substitute for attorney judgment. The profile is a configuration record approved by the practice group; it is not legal advice and does not override the skill's normal attorney-verification gates. If the profile's standing positions conflict with the matter facts or with what the supervising attorney concludes, the attorney prevails.

## Workflow

1. **Confirm inputs.** Verify that the processing activity description and specific data categories have been provided. Confirm that data subjects, purpose, and new-collection-or-reuse status are known or have been flagged. Note which optional inputs are present. If the activity description or data categories are missing, stop and request them before proceeding.

2. **Assess whether a PIA is warranted.** Evaluate whether the activity meets the organization's internal triggers for a PIA (if internal triggers have been provided). Separately flag — as `[ATTORNEY TO CONFIRM: whether a formal DPIA or equivalent is legally required for this activity — [verify jurisdiction]]` — the legal-requirement question. If neither an internal trigger nor a plausible legal trigger applies, note that a short file note may be sufficient; do not dismiss the question. Proceed with the full PIA draft unless the user confirms otherwise.

3. **Run the intake.** Organize the provided inputs into the seven structural sections of the PIA: (1) description of processing; (2) legal basis and disclosure; (3) data flow — collection, storage, sharing, retention; (4) policy-consistency check; (5) risks and mitigations; (6) data-subject-rights readiness; (7) recommendation. Note gaps in the inputs as `[CONFIRM: ...]` items against the relevant section.

4. **Perform the policy-consistency check.** If the organization's privacy policy or privacy notice has been provided, cross-reference each finding — particularly the data categories collected, the stated purposes, the sharing with third parties, the retention period, and the rights offered to data subjects — against the policy's commitments. Flag any divergence as a policy-consistency issue with a plain-language description of the gap. If the policy is not available, note the gap and flag the entire policy-consistency section as `[VERIFY: cross-check against current privacy policy before finalizing]`.

5. **Identify design-specific risks.** For each identified risk, ground it in a specific design element: a data category that is broader than the stated purpose requires; an access path that is not role-restricted; a retention period longer than the stated purpose supports; a sharing arrangement with a subprocessor not disclosed in the privacy policy; a rights fulfillment gap for a specific data subject category; a failure mode tied to a specific system or integration. Reject generic risks. Produce two to five risks, each with likelihood, impact, proposed mitigation, owner, and status. Mark risks that depend on unverified facts as `[CONFIRM: ...]`.

6. **Assess data-subject-rights readiness.** For each relevant rights category (access, correction, deletion, portability, objection, restriction — as applicable to the activity), assess whether the design supports fulfillment. Note gaps. Flag the rights that apply as `[verify jurisdiction]` — which rights are legally required depends on the applicable framework.

7. **Draft the recommendation.** Based on the risk analysis, draft one of: approve; approve with conditions; changes required; not approved. List any conditions as specific, actionable items with assigned sign-off roles. Label the recommendation prominently as a draft for privacy-counsel review and sign-off.

8. **Compile the open items list.** Collect all `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` flags into a consolidated open-items section at the end of the document.

9. **Assemble and label the output.** Use `templates/privacy-impact-assessment.md` — or, where the organization's PIA house style or template preferences were provided (either inline by the user or via the loaded `practice-profiles/privacy.md` Preferred Output Style section), conform the output to that format and flag any departures from `templates/privacy-impact-assessment.md` for attorney review. Where the profile is loaded but is silent on a specific format element, treat that element as not addressed by the playbook. Label the output clearly as a draft for privacy-counsel review. Do not represent it as a final, approved, or regulator-ready document.

## Output Format

Deliver a completed draft PIA using `templates/privacy-impact-assessment.md`. The document must be labeled **DRAFT — FOR PRIVACY-COUNSEL REVIEW**. It includes:

- **Header block**: activity name, prepared by, date, version, status (DRAFT).
- **Executive summary**: one paragraph describing the activity, the data involved, and an overall risk rating (Low / Medium / High / `[CONFIRM]`).
- **Section 1 — Description of processing**: activity, purpose, data subjects, data categories, new collection or reuse.
- **Section 2 — Legal basis and disclosure**: how the processing is authorized and what is disclosed to data subjects; all legal-basis assertions flagged `[verify jurisdiction]`.
- **Section 3 — Data flow**: collection, storage (location and controller), sharing and subprocessors, retention period and deletion trigger.
- **Section 4 — Policy-consistency check**: a table mapping each key finding against the privacy policy commitment, with a consistency status and any gap noted.
- **Section 5 — Risks and mitigations**: a table of two to five design-specific risks, each with likelihood, impact, mitigation, owner, and status.
- **Section 6 — Data-subject-rights readiness**: a table of applicable rights, readiness assessment, and gaps.
- **Section 7 — Recommendation**: the draft recommendation with any conditions and sign-off roles.
- **Open items for attorney verification**: consolidated list of all flagged items.

Use `[CONFIRM: ...]` wherever inputs were not provided or are uncertain. Do not leave any section blank without a flag.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The processing activity description is complete, accurate, and reflects the system as built or proposed — not a summary or approximation.
- [ ] All data categories listed are accurate; no categories present in the system are omitted.
- [ ] The stated purpose of processing is the actual operational purpose, not a post-hoc rationalization.
- [ ] Whether a formal DPIA or equivalent assessment is legally required for this activity has been confirmed by privacy counsel `[verify jurisdiction]`.
- [ ] The legal basis for processing identified in Section 2 has been verified under applicable law `[verify jurisdiction]`.
- [ ] The privacy-policy commitments reviewed in Section 4 reflect the current, published version of the policy.
- [ ] Every divergence flagged in the policy-consistency check has been assessed and either resolved or accepted with documented rationale.
- [ ] Each risk in Section 5 has been reviewed; likelihood and impact ratings have been confirmed by a person with operational knowledge of the system.
- [ ] Each proposed mitigation is technically and operationally feasible; owners have confirmed their acceptance of the mitigation task.
- [ ] The data-subject-rights assessment in Section 6 reflects the rights applicable under the governing framework `[verify jurisdiction]`.
- [ ] All subprocessors and third-party recipients listed in Section 3 have current, executed data processing agreements `[ATTORNEY TO CONFIRM]`.
- [ ] Retention periods have been verified against any applicable legal retention requirements `[verify jurisdiction]` `[deadline verification required]`.
- [ ] Cross-border transfer mechanisms, if applicable, are in place and have been confirmed by privacy counsel `[verify jurisdiction]`.
- [ ] The draft recommendation in Section 7 has been reviewed and a final determination made by privacy counsel.
- [ ] All open items flagged in the consolidated list have been resolved or documented as accepted risks before the PIA is treated as final.
- [ ] No agent-generated content has been relied upon as legal authority, citation, or regulatory quotation without independent verification.
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
