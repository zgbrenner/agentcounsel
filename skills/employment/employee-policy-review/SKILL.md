---
name: Employee Policy Review
description: Use when reviewing an employee handbook or individual workplace policy for clarity, internal consistency, completeness, and legal risk flags requiring attorney and jurisdiction-specific review.
---

# Employee Policy Review

## Purpose

Produce a structured, attorney-ready review of an employee handbook or individual workplace policy. The skill systematically surfaces clarity problems, internal contradictions, coverage gaps, language that may create unintended contractual commitments, outdated or ambiguous procedures, and acknowledgment or disclaimer issues — so that employment counsel can conduct an efficient substantive review. It does NOT certify legal compliance or conclude that any provision is lawful or unlawful. This is draft legal work product — not legal advice.

## Use When

- A user asks to "review our employee handbook" or "check this policy for problems."
- An HR team is preparing to roll out a new or updated handbook and wants a structured gap and issues analysis before counsel review.
- A policy has not been updated in several years and the user needs a systematic review of what may be stale.
- A specific policy (e.g., remote work, leave, social media, progressive discipline) has been flagged as potentially problematic and the user needs an organized issues list.
- Counsel is onboarding a new employer client and needs a first-pass issues inventory of existing policies.
- The user phrases it as: "does our handbook cover everything it should?" or "flag anything that looks like a risk."

## Required Inputs

- **The full policy or handbook text**: uploaded or pasted. Do not review from a description — the actual document text is required.
- **Jurisdiction(s)**: the state, province, or country in which the employer operates, or flag as unknown. Multi-state employers should indicate all relevant jurisdictions.
- **Employer size**: approximate headcount. Certain legal obligations vary by employer size — flag size-dependent topics for attorney confirmation.
- **Industry or workforce type** (if relevant): e.g., healthcare, construction, remote-only workforce. Flag industry-specific requirements for attorney confirmation.

If the document text is not provided, stop and request it. If jurisdiction or employer size is unknown, proceed with the review and flag all size- and jurisdiction-dependent items as `[CONFIRM]`.

## Do Not Use When

- The user is asking whether a specific employment action (termination, demotion, discipline) is lawful — use `termination-risk` or the appropriate action-specific skill.
- The user is asking for a severance or separation agreement review — use `severance-review`.
- The user wants to draft a new handbook from scratch rather than review an existing one (a separate drafting skill applies).
- The user needs advice on whether a specific provision violates a particular statute — that requires legal advice from counsel, not this skill.

## Legal Safety Rules

- Produce draft legal work product for attorney review only. This is not legal advice.
- Do not assert that any provision is or is not legally compliant. Flag provisions for attorney review; do not certify them.
- Do not assert what any jurisdiction requires, prohibits, or mandates in employment policies. Flag topics as jurisdiction-dependent and require attorney confirmation.
- Do not invent legal authority, regulatory citations, or agency guidance. If a policy topic is known to be regulated, note that attorney confirmation is needed — do not state the rule.
- Do not place client-identifying or sensitive factual information into reusable template copies.
- Review only the language actually present in the provided document. Do not infer or supply terms that are not written.
- Separate what the document says from what you assume and from what the attorney must verify. Label each category.
- Use `[CONFIRM: ...]` wherever a legal requirement, enforceability question, or factual basis is uncertain.
- Flag handbook language that may create express or implied contractual commitments as a risk item — do not conclude on enforceability.

## Workflow

1. **Confirm inputs.** Verify that the document text, jurisdiction, and employer size are available. If the text is missing, stop and request it. Flag unknown jurisdiction or employer size as `[CONFIRM]` and proceed.

2. **Identify document structure and scope.** Read through the full document and note: the overall organization, the presence or absence of a table of contents, the types of policies included, and the apparent date of last revision. Flag stale-appearing revision dates for attorney attention.

3. **Review the at-will disclaimer and acknowledgment.** Assess whether: the handbook contains a clear at-will disclaimer; the disclaimer appears in the acknowledgment page signed by employees; language elsewhere in the handbook may contradict or erode the at-will disclaimer (e.g., "employees will be terminated only for cause," progressive discipline language stated as mandatory). Flag all contradictions and the overall disclaimer structure for attorney review.

4. **Identify missing standard policy topics.** Compare the document against a standard set of policy topics to identify what is absent. Common topics include: equal employment opportunity and anti-harassment; anti-retaliation; complaint and investigation procedure; accommodation (disability, religion, pregnancy); leave policies (FMLA-type, state/local leave `[CONFIRM]`); pay practices and timekeeping; remote or hybrid work; social media; confidentiality and trade secrets; progressive discipline; performance review; separation; safety and workers' compensation; technology use and monitoring; and drug and alcohol. Note each missing topic as a gap, and flag size- or jurisdiction-dependent topics for attorney confirmation.

5. **Identify internally contradictory provisions.** Read for internal consistency across all policies. Common contradictions include: discipline procedures that are mandatory in one section but discretionary in another; leave policies that conflict with each other in duration or eligibility; inconsistent definitions of "full-time," "part-time," or "regular" employee used to determine benefit eligibility.

6. **Identify language that may create unintended contractual commitments.** Flag: mandatory discipline sequences stated without managerial discretion language; promises of continued employment, job security, or specific treatment; language that removes employer flexibility without intending to. Flag all such language for attorney review — do not conclude on contractual effect.

7. **Assess clarity and procedural specificity.** Identify: procedures that are described without enough specificity to be followed consistently; policies that are aspirational but provide no complaint or enforcement mechanism; vague or undefined terms that employees or managers must interpret. Note each as a clarity gap.

8. **Flag outdated references.** Identify: references to superseded statutes or agencies; outdated job titles, department names, or contact information; COVID-era or other temporary policies that may still appear in the handbook; references to a separate document that does not appear to exist or has not been provided.

9. **Review accommodation and leave coverage.** Note whether disability, religious, and pregnancy accommodation procedures are addressed. Flag whether leave policies appear to address applicable federal, state, and local entitlements — do not assert what those entitlements are; flag for attorney confirmation by jurisdiction.

10. **Review complaint, investigation, and anti-retaliation provisions.** Assess whether: a clear internal complaint procedure is described; the policy identifies who receives complaints; confidentiality and anti-retaliation protections are stated; the investigation process is described at a general level. Flag gaps or overly rigid procedures.

11. **Review technology use, monitoring, and confidentiality policies.** Note whether: the policy addresses employer monitoring of devices and communications; the policy addresses remote work security; confidentiality and trade secret obligations are described; social media use on company time or regarding the employer is addressed. Flag monitoring disclosure language for attorney review — requirements vary by jurisdiction.

12. **Build the gap-and-issues table.** Organize all findings by policy area, issue type (gap / contradiction / contractual-risk / clarity / outdated reference / attorney-flag), severity (High / Medium / Low), and recommended action.

13. **Draft prioritized recommendations.** Produce a prioritized list of recommended attorney actions and policy revisions. Label each High, Medium, or Low.

14. **Assemble the output.** Produce the full structured review labeled as a draft for attorney review.

## Output Format

Deliver the following sections, clearly labeled:

1. **Document Overview** — structure, apparent revision date, scope of policies covered, and jurisdiction(s) as stated in or assumed from the document.
2. **At-Will Disclaimer & Acknowledgment Assessment** — location, wording, and any contradictions found.
3. **Gap Analysis** — list of standard policy topics absent from the document, with size- and jurisdiction-dependent items flagged for attorney confirmation.
4. **Gap-and-Issues Table** — structured table: Policy Area | Issue Type | Description | Severity | Recommended Action.
5. **Internal Contradictions** — plain-language description of each identified contradiction and the conflicting provisions.
6. **Contractual-Risk Language** — excerpts or paraphrases of language identified as potentially creating unintended commitments, flagged for attorney review.
7. **Outdated References** — list of stale, broken, or superseded references identified.
8. **Prioritized Recommendations** — numbered list ordered High → Medium → Low, describing each recommended revision or attorney action.
9. **Open Items for Attorney Verification** — numbered list of legal questions that must be resolved before any revision is finalized.
10. **Assumptions** — explicit list of facts assumed in the absence of confirmed information.

Use `[CONFIRM: ...]` throughout for any unverified legal or factual point. Label the complete output: *Draft legal work product for attorney review. Not legal advice.*

## Attorney Verification Checklist

- [ ] The complete, current handbook or policy text was reviewed; no sections, appendices, or exhibits are missing.
- [ ] The at-will disclaimer and its interaction with all other provisions has been reviewed by counsel.
- [ ] All gaps identified have been assessed for jurisdiction-specific mandates applicable to this employer's size and location(s).
- [ ] Each flagged contradiction has been resolved and the handbook revised to be internally consistent.
- [ ] All language identified as creating potential contractual commitments has been reviewed and revised or intentionally retained.
- [ ] Leave and accommodation policies have been confirmed as addressing applicable federal, state, and local requirements for all operating jurisdictions.
- [ ] Monitoring, technology, and confidentiality provisions have been reviewed for compliance with applicable jurisdiction-specific requirements.
- [ ] The complaint and investigation procedure has been reviewed for adequacy and practicability.
- [ ] All outdated references have been updated or removed.
- [ ] The employee acknowledgment form captures what is legally necessary for the employer's purposes in each operating jurisdiction.
- [ ] All `[CONFIRM]` placeholders have been resolved by counsel before the handbook is distributed or relied upon.
- [ ] No legal conclusions in this document have been relied upon without attorney review.
