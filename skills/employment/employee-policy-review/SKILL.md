---
name: Employee Policy Review
description: "Use when reviewing an employee handbook or individual workplace policy — or a proposed change to one — for clarity, internal consistency, completeness, and legal risk flags requiring attorney and jurisdiction-specific review."
practice_area: employment
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The employee handbook or workplace policy text"
  - "Or a proposed change to an existing policy"
  - "The jurisdictions and workforce the policy covers"
outputs:
  - "Gap and issues table"
  - "Prioritized legal-risk flags for attorney and jurisdiction-specific review"
related_skills:
  - skills/employment/termination-risk/SKILL.md
  - skills/employment/severance-review/SKILL.md
tags:
  - employment
  - handbook
  - workplace-policy
  - policy-review
  - gap-analysis
---

# Employee Policy Review

## Purpose

Produce a structured, attorney-ready review of an employee handbook or individual workplace policy, or of a proposed change to an existing handbook or policy. The skill systematically surfaces clarity problems, internal contradictions, coverage gaps, language that may create unintended contractual commitments, outdated or ambiguous procedures, and acknowledgment or disclaimer issues — so that employment counsel can conduct an efficient substantive review. When the input is a proposed change rather than a whole document, the skill additionally checks for ripple effects across the rest of the handbook (cross-references, defined terms, related policies, location supplements) and flags any benefit reductions or altered promises the change would introduce. It does NOT certify legal compliance or conclude that any provision is lawful or unlawful. This is draft legal work product — not legal advice.

## Use When

- A user asks to "review our employee handbook" or "check this policy for problems."
- An HR team is preparing to roll out a new or updated handbook and wants a structured gap and issues analysis before counsel review.
- A policy has not been updated in several years and the user needs a systematic review of what may be stale.
- A specific policy (e.g., remote work, leave, social media, progressive discipline) has been flagged as potentially problematic and the user needs an organized issues list.
- Counsel is onboarding a new employer client and needs a first-pass issues inventory of existing policies.
- The user phrases it as: "does our handbook cover everything it should?" or "flag anything that looks like a risk."
- A user is proposing a change to one or more sections of an existing handbook and wants to know what else in the handbook the change may break, contradict, or affect before the change is published.
- A proposed change reduces or removes an employee benefit or alters a commitment the handbook previously made, and the user needs those implications surfaced for attorney review.

## Required Inputs

- **The full policy or handbook text**: uploaded or pasted. Do not review from a description — the actual document text is required.
- **If the input is a proposed change**: the text of the proposed change AND the text of the current handbook or section(s) being changed. Both are required to perform the ripple-effect and benefit-reduction checks. If the rest of the handbook is not provided, those checks cannot be completed — flag the omission prominently and request the full document.
- **Jurisdiction(s)**: the state, province, or country in which the employer operates, or flag as unknown. Multi-state employers should indicate all relevant jurisdictions.
- **Employer size**: approximate headcount. Certain legal obligations vary by employer size — flag size-dependent topics for attorney confirmation.
- **Industry or workforce type** (if relevant): e.g., healthcare, construction, remote-only workforce. Flag industry-specific requirements for attorney confirmation.
- Optional: the practice group's `practice-profiles/employment.md` if it has been populated and is loaded alongside this skill. If present, the skill uses its Standard Positions and Source-of-Truth Documents tables to benchmark the policy against the group's baseline template and standing positions. If absent, the skill proceeds without practice-profile benchmarking and asks the user to supply standing positions inline if needed.

If the document text is not provided, stop and request it. If jurisdiction or employer size is unknown, proceed with the review and flag all size- and jurisdiction-dependent items as `[CONFIRM]`.

## Do Not Use When

- The user is asking whether a specific employment action (termination, demotion, discipline) is lawful — use `termination-risk` or the appropriate action-specific skill.
- The user is asking for a severance or separation agreement review — use `severance-review`.
- The user wants to draft a new handbook from scratch rather than review an existing one (a separate drafting skill applies).
- The user needs advice on whether a specific provision violates a particular statute — that requires legal advice from counsel, not this skill.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review only. This is not legal advice.
- Do not assert that any provision is or is not legally compliant. Flag provisions for attorney review; do not certify them.
- Do not assert what any jurisdiction requires, prohibits, or mandates in employment policies. Flag topics as jurisdiction-dependent and require attorney confirmation.
- Do not invent legal authority, regulatory citations, or agency guidance. If a policy topic is known to be regulated, note that attorney confirmation is needed — do not state the rule.
- Do not place client-identifying or sensitive factual information into reusable template copies.
- Review only the language actually present in the provided document. Do not infer or supply terms that are not written.
- Separate what the document says from what you assume and from what the attorney must verify. Label each category.
- Use `[CONFIRM: ...]` wherever a legal requirement, enforceability question, or factual basis is uncertain.
- Flag handbook language that may create express or implied contractual commitments as a risk item — do not conclude on enforceability.
- **Ripple-effect rule (change reviews).** When the input is a proposed change to an existing policy or handbook section, do not treat that section in isolation. Identify every other part of the handbook — cross-references to the changed section, defined terms, related policies, and any state or location supplements — that the change may break or contradict, and surface each ripple effect explicitly. Do not assume that only the changed section matters.
- **Benefit-reduction and altered-promise rule (change reviews).** A proposed change that reduces or removes an employee benefit, or that alters a commitment the handbook previously made, can carry contractual or reliance exposure depending on the jurisdiction and how the handbook is framed `[verify jurisdiction]`. Flag every such reduction or altered promise prominently with `[ATTORNEY TO CONFIRM: benefit reduction or altered promise — assess contractual/reliance exposure before publication]`. Do not assert whether the original provision created an enforceable obligation or whether the change is permissible — that determination requires attorney review.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/employment.md` is loaded, its Standard Positions and Source-of-Truth Documents inform the draft but never substitute for attorney judgment. The profile is a configuration record approved by the practice group; it is not legal advice and does not override the skill's normal attorney-verification gates. If the profile's standing positions conflict with the matter facts or with what the supervising attorney concludes, the attorney prevails.

## Workflow

1. **Confirm inputs and review type.** Verify that the document text, jurisdiction, and employer size are available. Determine whether the input is (a) a whole handbook or policy for review or (b) a proposed change to an existing handbook or policy. If the text is missing, stop and request it. If the review is a proposed change and the rest of the handbook has not been provided, flag prominently that the ripple-effect and benefit-reduction checks cannot be completed without the full current document, and request it before proceeding with those checks. Flag unknown jurisdiction or employer size as `[CONFIRM]` and proceed with all other steps.

2. **Identify document structure and scope.** Read through the full document and note: the overall organization, the presence or absence of a table of contents, the types of policies included, and the apparent date of last revision. Flag stale-appearing revision dates for attorney attention.

3. **Review the at-will disclaimer and acknowledgment.** Assess whether: the handbook contains a clear at-will disclaimer; the disclaimer appears in the acknowledgment page signed by employees; language elsewhere in the handbook may contradict or erode the at-will disclaimer (e.g., "employees will be terminated only for cause," progressive discipline language stated as mandatory). Flag all contradictions and the overall disclaimer structure for attorney review.

4. **Identify missing standard policy topics.** Compare the document against a standard set of policy topics to identify what is absent. Common topics include: equal employment opportunity and anti-harassment; anti-retaliation; complaint and investigation procedure; accommodation (disability, religion, pregnancy); leave policies (FMLA-type, state/local leave `[CONFIRM]`); pay practices and timekeeping; remote or hybrid work; social media; confidentiality and trade secrets; progressive discipline; performance review; separation; safety and workers' compensation; technology use and monitoring; and drug and alcohol. Note each missing topic as a gap, and flag size- or jurisdiction-dependent topics for attorney confirmation. Where `practice-profiles/employment.md` is loaded, use its Standard Positions and Source-of-Truth Documents tables as the canonical list of topics the group expects to see covered and the baseline template policy; benchmark the document against that list in addition to the generic standard set above, and flag both group-list omissions and group-template deviations.

5. **Identify internally contradictory provisions.** Read for internal consistency across all policies. Common contradictions include: discipline procedures that are mandatory in one section but discretionary in another; leave policies that conflict with each other in duration or eligibility; inconsistent definitions of "full-time," "part-time," or "regular" employee used to determine benefit eligibility.

6. **Identify language that may create unintended contractual commitments.** Flag: mandatory discipline sequences stated without managerial discretion language; promises of continued employment, job security, or specific treatment; language that removes employer flexibility without intending to. Flag all such language for attorney review — do not conclude on contractual effect.

7. **Assess clarity and procedural specificity.** Identify: procedures that are described without enough specificity to be followed consistently; policies that are aspirational but provide no complaint or enforcement mechanism; vague or undefined terms that employees or managers must interpret. Note each as a clarity gap.

8. **Flag outdated references.** Identify: references to superseded statutes or agencies; outdated job titles, department names, or contact information; COVID-era or other temporary policies that may still appear in the handbook; references to a separate document that does not appear to exist or has not been provided.

9. **Review accommodation and leave coverage.** Note whether disability, religious, and pregnancy accommodation procedures are addressed. Flag whether leave policies appear to address applicable federal, state, and local entitlements — do not assert what those entitlements are; flag for attorney confirmation by jurisdiction.

10. **Review complaint, investigation, and anti-retaliation provisions.** Assess whether: a clear internal complaint procedure is described; the policy identifies who receives complaints; confidentiality and anti-retaliation protections are stated; the investigation process is described at a general level. Flag gaps or overly rigid procedures.

11. **Review technology use, monitoring, and confidentiality policies.** Note whether: the policy addresses employer monitoring of devices and communications; the policy addresses remote work security; confidentiality and trade secret obligations are described; social media use on company time or regarding the employer is addressed. Flag monitoring disclosure language for attorney review — requirements vary by jurisdiction.

12. **[Change reviews only] Ripple-effect and cross-reference check.** If the input is a proposed change to an existing policy or handbook section, systematically check the rest of the handbook for every location that may be broken or contradicted by the change. Specifically look for: (a) cross-references that point to the changed section by name, number, or heading; (b) defined terms that appear in the changed section and are also used elsewhere with an assumed meaning; (c) related policies whose scope, eligibility rules, or procedures interlock with the changed section; and (d) any state, local, or location-specific supplements that mirror or modify the changed section. For each ripple effect found, identify the location in the handbook, describe the conflict or inconsistency the change would create, and flag it for correction before the change is published. If no ripple effects are found, state that explicitly so counsel can confirm.

13. **[Change reviews only] Benefit-reduction and altered-promise flag.** If the input is a proposed change, compare the proposed language side-by-side with the current language it replaces. Identify every instance where the change: (a) reduces or eliminates a benefit employees currently receive under the handbook; (b) removes or narrows a commitment, entitlement, or procedural protection the handbook previously stated; or (c) alters a promise in a way that could disadvantage employees relative to the prior version. For each such instance, produce a prominent flag: `[ATTORNEY TO CONFIRM: benefit reduction or altered promise — assess contractual/reliance exposure before publication] [verify jurisdiction]`. Describe what the prior language said and what the new language says. Do not assert whether the prior provision was enforceable or whether the change is permissible — surface the delta for attorney review.

14. **Build the gap-and-issues table.** Organize all findings by policy area, issue type (gap / contradiction / contractual-risk / clarity / outdated reference / ripple-effect / benefit-reduction / attorney-flag), severity (High / Medium / Low), and recommended action.

15. **Draft prioritized recommendations.** Produce a prioritized list of recommended attorney actions and policy revisions. Label each High, Medium, or Low.

16. **Assemble the output.** Produce the full structured review labeled as a draft for attorney review.

## Output Format

Deliver the following sections, clearly labeled:

1. **Document Overview** — structure, apparent revision date, scope of policies covered, and jurisdiction(s) as stated in or assumed from the document.
2. **At-Will Disclaimer & Acknowledgment Assessment** — location, wording, and any contradictions found.
3. **Gap Analysis** — list of standard policy topics absent from the document, with size- and jurisdiction-dependent items flagged for attorney confirmation.
4. **Gap-and-Issues Table** — structured table: Policy Area | Issue Type | Description | Severity | Recommended Action.
5. **Internal Contradictions** — plain-language description of each identified contradiction and the conflicting provisions.
6. **Contractual-Risk Language** — excerpts or paraphrases of language identified as potentially creating unintended commitments, flagged for attorney review.
7. **Outdated References** — list of stale, broken, or superseded references identified.
8. **[Change reviews] Ripple-Effect Report** — for each part of the handbook broken or contradicted by the proposed change: location, description of the conflict, and recommended correction before publication. State explicitly if no ripple effects were found or if the check could not be completed because the full handbook was not provided.
9. **[Change reviews] Benefit-Reduction and Altered-Promise Flags** — side-by-side comparison of prior and proposed language for each instance where the change reduces a benefit or alters a commitment, each flagged `[ATTORNEY TO CONFIRM: benefit reduction or altered promise — assess contractual/reliance exposure before publication] [verify jurisdiction]`.
10. **Prioritized Recommendations** — numbered list ordered High → Medium → Low, describing each recommended revision or attorney action.
11. **Open Items for Attorney Verification** — numbered list of legal questions that must be resolved before any revision is finalized.
12. **Assumptions** — explicit list of facts assumed in the absence of confirmed information.

Use `[CONFIRM: ...]` throughout for any unverified legal or factual point. Label the complete output: *Draft legal work product for attorney review. Not legal advice.*

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

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
- [ ] **(Change reviews)** All ripple effects identified in the Ripple-Effect Report have been reviewed and corrected, and no cross-references, defined terms, or related policies in the handbook remain inconsistent with the proposed change.
- [ ] **(Change reviews)** Every benefit reduction or altered promise flagged with `[ATTORNEY TO CONFIRM: benefit reduction or altered promise]` has been reviewed by counsel for contractual and reliance exposure before the revised handbook is distributed to employees `[verify jurisdiction]`.
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
