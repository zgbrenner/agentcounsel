---
name: Compliance Gap Matrix
description: Use when mapping a set of regulatory or framework requirements against an organization's current controls to surface gaps, prioritize remediation, and produce an attorney-ready draft gap analysis.
---

# Compliance Gap Matrix

## Purpose

Produce a structured, attorney-ready draft compliance gap matrix that maps discrete regulatory or framework requirements against the organization's described current controls and practices. The output identifies where controls appear to meet requirements, where coverage is partial or uncertain, and where gaps exist — and proposes initial remediation framing, severity ratings, and ownership suggestions for attorney and management review.

This skill provides workflow discipline and analytical structure. It does not assert legal compliance conclusions. Gap status classifications reflect the workflow assessment and remain subject to attorney verification.

## Use When

- A user says "map our controls to the regulation," "do a gap analysis," or "show me where we're exposed against this framework."
- A compliance or legal team needs a structured first-pass matrix before a formal audit, regulatory examination, or board presentation.
- An organization has received a new regulation or framework (see `rule-change-summary`) and now needs to assess readiness.
- Counsel needs to organize factual information about current controls against a requirement set before advising on remediation priorities.
- A user provides a specific regulation, framework standard, or internal policy and a description of existing controls, and asks for a comparison.

## Required Inputs

- **Requirement source**: the actual regulation, framework, standard, or policy text — uploaded or pasted. If not provided, stop and request it. Do not construct requirements from model background knowledge; every requirement listed in the matrix must trace to this source.
- **Control description**: a description of the organization's current controls, policies, procedures, systems, and practices relevant to the requirement source. This may be a control inventory, a narrative description, policy documents, or process descriptions. The more specific, the more useful the matrix.
- **Organization context**: business type, size, and any relevant regulatory status (e.g., licensed entity, registered filer, covered entity) that affects applicability of specific requirements.
- **Scope boundaries** (optional but recommended): which parts of the organization, business lines, or systems are in scope for this analysis. If not provided, flag as `[SCOPE: CONFIRM with attorney]`.
- **Priority areas** (optional): if the user identifies specific requirements or control areas to focus on, note them and address them first.

If the requirement source is not provided, stop and request it. If control descriptions are too vague to enable meaningful mapping, ask targeted follow-up questions.

## Do Not Use When

- The user needs a summary of what a rule requires (use `rule-change-summary` first, then return here).
- The user needs to assess enforcement exposure for a specific incident or practice (use `enforcement-risk-memo`).
- No requirement source has been provided and cannot be obtained — do not construct a requirements list from model background knowledge alone.
- The user is seeking a certification of compliance or a formal audit opinion — this skill produces a draft gap analysis, not a compliance certification.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Do not assert that any control satisfies a legal requirement as a binding conclusion. "Met" status in the matrix means the described control appears to address the requirement based on the information provided — not that legal compliance has been achieved or that the control would withstand regulatory scrutiny.
- Every requirement listed must trace to the source document provided. Do not add requirements from model background knowledge without clearly marking them `[UNVERIFIED — not from provided source]`.
- Do not assert penalty exposure, enforcement risk, or legal liability based on gap status alone — surface identified gaps as items for attorney assessment.
- Distinguish: (a) requirements as stated in the source, (b) the analyst's mapping of current controls, (c) gap severity as a workflow assessment, (d) attorney-verification items.
- Use `[CONFIRM: ...]` placeholders for any control fact, applicability question, or requirement interpretation that cannot be resolved from provided materials.
- Never fabricate control descriptions, system capabilities, or organizational facts.
- Preserve confidentiality; do not incorporate client-identifying sensitive operational details into reusable templates.
- Flag every area of uncertainty, including requirements whose applicability to the organization is unclear.

## Workflow

1. **Confirm inputs.** Verify that both the requirement source and a control description have been provided. If either is missing, stop and request it. Clarify scope boundaries and priority areas.

2. **Parse the requirement source.** Extract discrete, individually assessable requirements from the source document. Number each requirement for matrix reference. Quote the operative language where precision matters — do not paraphrase in a way that narrows or expands scope. Flag requirements whose applicability to this organization is unclear as `[APPLICABILITY: CONFIRM]`.

3. **Map requirements to controls.** For each requirement, identify which described control, policy, procedure, or system the organization has offered as addressing it. If no control is described, note "No control described."

4. **Classify gap status.** For each requirement, apply one of the following statuses based on the mapping:
   - **Met**: The described control appears to address the requirement as stated. Subject to attorney verification.
   - **Partial**: The described control addresses some elements of the requirement but coverage appears incomplete.
   - **Gap**: No described control addresses the requirement, or the described control does not appear to match the requirement.
   - **Unknown**: Insufficient information about controls or requirement applicability to classify. Flag for follow-up.

5. **Assess gap severity.** For Partial and Gap items, assign an initial severity rating — High, Medium, or Low — based on factors such as: centrality to the regulatory scheme, likelihood of regulatory examination, potential for harm, and whether the gap is structural or procedural. These ratings are preliminary and require attorney and management review.

6. **Propose remediation framing.** For each Partial or Gap item, describe in plain language what type of remediation appears warranted (e.g., drafting a written policy, implementing a system control, conducting training, engaging a third party). Do not prescribe specific legal steps — that is attorney judgment.

7. **Suggest ownership areas.** Propose which organizational function (e.g., legal, compliance, IT, HR, operations, finance) is likely the primary owner of remediation. Flag where ownership is unclear as `[OWNER: CONFIRM]`.

8. **Identify attorney-specific verification items.** Flag any gap or mapping where the legal interpretation of the requirement, the legal sufficiency of the control, or the legal consequences of the gap require attorney judgment beyond workflow analysis.

9. **Assemble the matrix and narrative.** Produce the structured output below. Mark the entire document as a draft for attorney review.

## Output Format

Deliver the following sections in order:

**DRAFT COMPLIANCE GAP MATRIX — FOR ATTORNEY REVIEW ONLY**

1. **Scope and Inputs Summary** — Identifies the requirement source (title, version, date from document), organization context, scope boundaries, and any limitations on the analysis (e.g., controls described at a high level only, prior-rule baseline not provided).

2. **Methodology Note** — Brief explanation of status classifications (Met / Partial / Gap / Unknown) and severity ratings (High / Medium / Low), with the caveat that all classifications are workflow assessments subject to attorney verification and do not constitute legal conclusions.

3. **Executive Summary** — Counts of Met / Partial / Gap / Unknown items; count of High/Medium/Low severity gaps; top three to five priority gaps identified for immediate attorney attention.

4. **Compliance Gap Matrix** — Inline table with the following columns:

| # | Requirement | Source ref | Current control | Status | Severity | Remediation (draft) | Owner (proposed) | Attorney note |
|---|---|---|---|---|---|---|---|---|
| 1 | [from source] | [§ or provision] | [from org description] | Met / Partial / Gap / Unknown | H / M / L / — | [type of action] | [function] | [CONFIRM / flag] |

5. **Gap Detail — High Severity Items** — For each High severity item: requirement text, gap description, why severity is rated High, proposed remediation framing, and attorney verification items specific to that gap.

6. **Gap Detail — Medium and Low Severity Items** — Summarized narrative or table for medium and low items; less detailed than High items.

7. **Open Questions** — Bulleted list of requirements whose applicability is unclear, controls whose scope is uncertain, and interpretive questions requiring attorney or subject-matter-expert resolution.

8. **Attorney Verification Items** — see the Attorney Verification Checklist below.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] Every requirement in the matrix has been extracted from the actual source document; none were supplied from model background knowledge without disclosure.
- [ ] The requirement text in each row accurately reflects the source; no paraphrase has narrowed or expanded scope.
- [ ] Applicability of each requirement to this organization has been confirmed by an attorney with subject-matter expertise — no applicability conclusion from the draft is accepted as final.
- [ ] Each "Met" classification has been verified: the described control actually exists as described, is currently operative, and has been assessed by a qualified reviewer as sufficient to address the requirement.
- [ ] Each "Partial" and "Gap" classification reflects a genuine control deficiency, not an artifact of incomplete control descriptions provided as input.
- [ ] Severity ratings have been reviewed and adjusted to reflect the organization's actual regulatory environment, examination history, and risk tolerance.
- [ ] Proposed remediation framing has been reviewed and supplemented by legal and operational judgment before being included in any compliance roadmap.
- [ ] Ownership assignments have been confirmed with management; no function is held responsible for a gap without its knowledge and agreement.
- [ ] The scope of the analysis (which entity, business line, or system) has been confirmed and documented.
- [ ] All open questions have been resolved or escalated before the matrix is presented to regulators, auditors, or the board.
- [ ] The draft is labeled appropriately and has not been transmitted to any third party without attorney review and approval.
