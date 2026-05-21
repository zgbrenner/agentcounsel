---
name: Employee AI Policy
description: Use when reviewing a draft internal employee AI-use policy — or drafting review criteria when no policy exists — to identify gaps, inconsistencies, and priority issues for attorney and HR review.
---

# Employee AI Policy

## Purpose

Produce a structured review of an organization's internal employee AI-use policy (or, if no policy exists, a structured gap analysis based on the topics a policy should address). The output is a gap-and-issues table with prioritized recommendations for attorney and HR review.

This skill does not certify legal compliance, render an opinion on what any law requires, or produce a final policy. It identifies what is missing, inconsistent, or ambiguous and routes open questions to the right specialists.

## Use When

- An organization has a draft AI-use policy for employees and wants it reviewed before publication.
- Legal, HR, or compliance has been asked "do we have what we need in our AI policy?" or "what should our AI policy cover?"
- An existing AI policy needs to be updated because new AI tools have been adopted or applicable law has changed.
- An incident (data leak, confidentiality breach via AI tool, IP dispute) has prompted a policy review.
- A user asks "what should employees be allowed to do with AI tools?" or "how do we handle employees using generative AI tools for work?"

## Required Inputs

- **Policy text (if one exists)**: The full text of the current or draft employee AI-use policy, uploaded or pasted.
- **Organization context**: A brief description of the organization's industry, approximate size, and the types of AI tools employees are currently using or are likely to use.
- **Jurisdictions**: The countries and states or provinces where employees are located — employment law is jurisdiction-specific and the review will flag where jurisdiction-specific legal input is needed.

If no policy text is provided, the skill will produce a gap analysis based on the topics a policy should address. Note clearly that this is a gap analysis and not a policy review.

If the organization context and jurisdictions are not provided, stop and request them. Employment law varies materially by jurisdiction and industry; do not assume.

## Do Not Use When

- The question is about reviewing an AI vendor's terms of service — use `ai-vendor-terms-review`.
- The question is about assessing a specific AI use case for a product or service — use `ai-use-case-intake`.
- The primary question is about employment law compliance in a specific jurisdiction (discrimination, monitoring, works council rights) — route directly to an employment law specialist after completing this review.
- The policy in question governs AI use by contractors, customers, or third parties rather than employees — this skill covers employee-facing policies only.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Do not assert what any law or regulation requires of an employee AI policy. Employment law, privacy law, and AI regulation are jurisdiction-specific and fast-moving — flag regulatory considerations for attorney verification.
- Do not assert that a policy is legally compliant or sufficient.
- Review only the text actually provided. Do not fabricate policy provisions, assume terms that are not stated, or invent regulatory requirements.
- Distinguish what the policy says, what is missing or ambiguous, and what requires attorney or specialist verification.
- Use `[CONFIRM: ...]` placeholders wherever jurisdiction-specific legal input is required or a provision is ambiguous.
- Employee monitoring and consent topics are legally sensitive and jurisdiction-specific — always flag for employment law specialist review.
- Confidentiality and privilege implications of employee AI use are a significant risk area — ensure these are flagged prominently.

## Workflow

1. **Confirm inputs.** Verify that policy text (or a clear statement that none exists), organization context, and jurisdictions are present. If policy text is absent, note that the output will be a gap analysis, not a policy review.

2. **Identify the policy scope and structure.** If a policy exists, summarize its stated scope (which employees, which tools, which uses), effective date, and owner. Note any definitions of "AI tool" or "generative AI" and assess whether they are broad enough to cover the tools employees actually use.

3. **Review approved and prohibited tools.** Assess whether the policy clearly identifies approved AI tools and prohibited or unapproved tools. Flag if the policy is silent on tool approval or if the approval process is unclear. Note whether the policy covers both employer-provided tools and personal/consumer AI tools used for work purposes.

4. **Review handling of confidential and sensitive data.** Assess whether the policy prohibits employees from entering confidential business information, trade secrets, non-public financial information, or other sensitive organizational data into unapproved AI systems. Flag if confidential data categories are undefined or underinclusive.

5. **Review handling of personal data.** Assess whether the policy addresses the prohibition on entering personal data (employee data, customer data, patient data, etc.) into AI tools, and whether it addresses applicable privacy law requirements. Flag for privacy specialist review if personal data is in scope.

6. **Review prohibition on privileged and client-sensitive material.** Assess whether the policy explicitly prohibits employees from entering attorney-client privileged communications, work product, or client-sensitive information into unapproved AI systems. This is a high-priority gap in legal, professional services, and regulated industries — flag prominently if absent or insufficient.

7. **Review IP and ownership of AI-assisted work.** Assess whether the policy addresses who owns work created with the assistance of AI tools. Flag if the policy is silent on: (a) the employee's obligation to disclose AI assistance; (b) the organization's IP rights in AI-assisted work product; (c) restrictions on using AI-generated content that may be subject to third-party claims.

8. **Review accuracy and verification expectations.** Assess whether the policy sets expectations that employees must verify AI-generated outputs before relying on or sharing them. Flag if the policy implies that AI outputs can be used without human review.

9. **Review disclosure and transparency requirements.** Assess whether the policy addresses when employees must disclose AI assistance to internal stakeholders, clients, or counterparties. Flag if the policy is silent on customer-facing or counterparty-facing disclosure.

10. **Review customer-facing use.** Assess whether the policy separately addresses AI use in customer communications, customer service, or client deliverables — where accuracy, disclosure, and regulatory requirements may be heightened. Flag if customer-facing use is not separately addressed.

11. **Review security requirements.** Assess whether the policy addresses security requirements for AI tool use: approved device and network requirements, prohibition on sharing credentials, logging and audit requirements for AI tool use. Flag if security requirements are absent.

12. **Review enforcement and training.** Assess whether the policy explains the consequences of non-compliance and whether training is required. Flag if the policy lacks an enforcement mechanism or if no training obligation is stated.

13. **Flag jurisdiction-specific considerations.** For each jurisdiction provided, flag topics that require jurisdiction-specific legal review: employee monitoring and consent, data protection (GDPR, CCPA, and others), works council or union consultation rights, and any jurisdiction-specific AI transparency or automated-decision requirements. Do not assert what the law requires — flag the topics for attorney verification.

14. **Prioritize gaps and issues.** Categorize all findings as High (significant risk, requires immediate attention), Medium (should be addressed before the policy is finalized), or Low (minor gap, flag for awareness).

15. **Assemble the output.** Compile all sections, label the document as a draft for attorney and HR review, and include all assumptions and open items.

## Output Format

Deliver the following sections in order:

**1. Review Summary**
Two to four sentences: policy scope (or absence of a policy), overall coverage assessment, and the two or three highest-priority gaps or risks.

**2. Policy Scope Assessment**
If a policy exists: stated scope, covered tools, effective date, policy owner, and assessment of whether the definition of "AI tool" is sufficiently broad. If no policy exists: confirm this is a gap analysis and note the tools employees are known to use.

**3. Gap-and-Issues Table**

| Coverage Area | Policy Position (or Gap) | Issue / Risk | Priority |
|---|---|---|---|
| Approved / prohibited tools | | | |
| Confidential and sensitive data | | | |
| Personal data | | | |
| Privileged / client-sensitive material | | | |
| IP ownership of AI-assisted work | | | |
| Accuracy and verification | | | |
| Disclosure and transparency | | | |
| Customer-facing use | | | |
| Security requirements | | | |
| Enforcement and training | | | |

**4. Jurisdiction-Specific Flags**
For each jurisdiction provided, a bullet list of topics requiring jurisdiction-specific legal review, with a `[CONFIRM: ...]` tag for each. Do not assert what the law requires.

**5. Prioritized Recommendations**
Numbered list of recommended policy changes or additions, sorted High / Medium / Low, each with a brief rationale and suggested owner (legal, HR, IT security, compliance).

**6. Routing Recommendations**
- Employment law specialist — for jurisdiction-specific compliance review (monitoring consent, data protection, works council rights, AI-specific transparency obligations).
- Privacy specialist — if the policy addresses or should address employee or customer personal data.
- IT security — for security requirements and approved tool lists.
- `ai-use-case-intake` — if the policy review reveals specific AI use cases that have not been assessed.
- `ai-vendor-terms-review` — if terms for specific AI tools used by employees have not been reviewed.

**7. Open Items and Assumptions**
Bullet list of every `[CONFIRM: ...]` item, jurisdiction-specific gap, and assumption made during the review.

*Label the full document: DRAFT — For Attorney and HR Review — Not Legal Advice.*

## Attorney Verification Checklist

- [ ] The policy text reviewed is the current or most recent draft; no prior version has been substituted.
- [ ] The definition of "AI tool" covers all tools employees are currently using, including consumer-facing tools used for work purposes.
- [ ] Confidential data categories are defined and cover all relevant categories for the organization's industry.
- [ ] The prohibition on entering privileged or client-sensitive material is explicit and has been reviewed by legal.
- [ ] IP ownership provisions have been reviewed against the organization's standard employment agreements and applicable law.
- [ ] Jurisdiction-specific flags have been reviewed by an employment law specialist in each relevant jurisdiction.
- [ ] Employee monitoring provisions (if any) have been reviewed for consent and notice requirements in each jurisdiction.
- [ ] Personal data handling provisions have been reviewed by a privacy specialist.
- [ ] Customer-facing AI use provisions are consistent with applicable client contracts, professional conduct rules, and sector-specific regulations.
- [ ] Enforcement and training provisions are consistent with the organization's disciplinary framework.
- [ ] No legal conclusion about compliance with any law or regulation has been asserted without attorney verification.
- [ ] All open items and `[CONFIRM: ...]` placeholders have been resolved before the policy is published.
