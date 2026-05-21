---
name: Hiring Review
description: Use when reviewing an employment offer letter (and any restrictive-covenant exhibits) against the candidate's actual work jurisdiction and the employer's standard hiring practices to produce a structured draft review memo with a verdict, for attorney review.
---

# Hiring Review

## Purpose

Produce a structured, attorney-ready review of an employment offer letter and any accompanying restrictive-covenant exhibits. The skill verifies that the proposed terms are internally consistent, flags classification and statutory issues tied to the candidate's actual work jurisdiction, and surfaces enforceability questions on every restrictive covenant — without asserting jurisdiction-specific legal rules. The output is a draft hiring review memo with a verdict. This is draft legal work product for attorney review — not legal advice.

## Use When

- An employer, HR team, or counsel asks for a first-pass review of an offer letter before it is sent to a candidate.
- A candidate or their counsel asks for a structured review of an offer they have received.
- A user asks to "check this offer," "is this offer letter okay to use," or "flag anything I should look at before signing."
- The offer includes restrictive-covenant exhibits (non-compete, non-solicitation, IP assignment, confidentiality) and the team wants an issues list organized by covenant type.
- Counsel needs a jurisdiction and classification flag-list to begin their own analysis.

## Required Inputs

- **The full offer letter text**: uploaded or pasted. Do not review from a summary or description — the actual document text is required.
- **Candidate's actual work location**: the physical location where the candidate will perform work — a specific city and state/province/country, or a confirmed remote home location. This is not the company headquarters unless they are the same. If unknown, stop and request it; the work jurisdiction determines which statutory requirements apply.
- **Role title and proposed compensation**: the title as stated in the offer and the base salary or wage rate as stated.
- **Proposed exempt or non-exempt classification** (where the employer has indicated one, or where the offer structure implies one): identify the stated or implied classification from the offer text.

Optional inputs — provide if available, skip if not:
- **Restrictive-covenant exhibits**: any non-compete, non-solicitation, IP assignment, or confidentiality agreement attached to or referenced in the offer.
- **Employer's standard hiring practices or policy playbook**: if the employer has a standard template or policy the offer is meant to follow, provide it to allow a conformance check.

If the offer letter text is not provided, stop and request it before proceeding. If the candidate's work location is not provided, stop and request it. Do not fabricate, assume, or infer missing required inputs.

## Do Not Use When

- The task is to **draft an offer letter from scratch** rather than review an existing one — drafting an offer from scratch is outside the scope of this skill.
- The document is an **employee handbook or standalone workplace policy** rather than an offer letter (use `employee-policy-review`).
- The core question is **whether a worker should be classified as an employee or an independent contractor** rather than reviewing the terms of an employment offer (use `worker-classification`).
- The user is asking the skill to **decide whether to hire the candidate** — hiring decisions are business and human-resources judgments outside this skill's scope.
- The document is a **collective bargaining agreement or union contract** rather than an individual offer letter.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review only. This is not legal advice. Attorney review and sign-off are required before any party acts on this output.
- Review only the language actually present in the provided documents. Do not infer, supply, or assume terms that are not written.
- Do not assert whether any restrictive covenant is enforceable in any jurisdiction. Enforceability is a jurisdiction-specific legal question that has changed frequently in recent years and must be confirmed by counsel. Flag every enforceability question with `[verify jurisdiction]`.
- Do not assert what the exempt or non-exempt classification threshold is, what duties tests apply, or what the outcome of a classification analysis would be. Flag every classification question with `[verify jurisdiction]` and `[ATTORNEY TO CONFIRM: classification under applicable law]`.
- Do not assert what statutory requirements apply in the work jurisdiction (pay transparency, salary history bans, ban-the-box timing, wage notice obligations, or any other jurisdiction-specific onboarding requirement). Identify each as a question and flag with `[verify jurisdiction]`.
- Do not treat "at-will employment" as a universal rule. If the offer uses at-will language, flag whether at-will employment applies — or is legally meaningful — in the confirmed work jurisdiction as `[verify jurisdiction]`.
- Do not invent facts, citations, quotations, deadlines, or legal authority. Treat model background knowledge as unverified; use `[citation needed]` where a legal proposition is stated without a confirmed source.
- Separate what the document says from what you assume and from what the attorney must verify. Label each category explicitly.
- Preserve confidentiality and privilege. Do not include client-identifying information in reusable template copies of this output.
- Flag every point of uncertainty with a placeholder — `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, `[deadline verification required]` — rather than resolving uncertainty silently.

## Workflow

1. **Confirm inputs.** Verify that the offer letter text and the candidate's actual work location are available. If either is missing, stop and request it before proceeding. Note whether restrictive-covenant exhibits and an employer hiring-practices playbook were provided; if not, record that these are absent and proceed with the information at hand.

2. **Establish the work jurisdiction.** Identify the physical work location from the input. Record it as the controlling jurisdiction for all statutory and enforceability analysis. If the offer states a choice-of-law clause that differs from the work location, note the discrepancy and flag it for attorney assessment — do not conclude which law governs.

3. **Classification sanity check.** Identify the proposed exempt or non-exempt classification from the offer. Identify the role's described duties and compensation level. Flag whether the stated classification appears consistent with the described duties and compensation on its face. Do not state what the applicable salary threshold or duties test is — flag the salary threshold and duties test as `[verify jurisdiction]` and `[ATTORNEY TO CONFIRM: classification under applicable law as of offer date]`. If the offer does not state a classification, flag the omission.

4. **Review restrictive covenants.** For each covenant type present (non-compete, customer non-solicitation, employee non-solicitation, IP assignment, confidentiality/non-disclosure), produce a separate subsection that:
   - Quotes or closely paraphrases the scope (activity restricted, geographic or market scope, duration, parties covered, carve-outs);
   - Notes any remedies, liquidated-damages provisions, or attorneys'-fee provisions stated;
   - Flags enforceability as a jurisdiction-specific question — `[verify jurisdiction]` — without asserting any conclusion;
   - Flags whether the scope appears unusually broad or narrow on its face, for attorney assessment only;
   - Notes any recent legal developments that may affect the covenant type, framed as a prompt to verify: `[VERIFY: recent legal changes affecting [covenant type] in work jurisdiction]`.
   If no restrictive-covenant exhibits were provided, note the absence and flag whether the offer letter itself contains any restrictive language.

5. **Jurisdiction-specific statutory requirements check.** For the confirmed work jurisdiction, identify each of the following as an open question to verify — do not assert what the requirement is or whether it applies:
   - Pay-transparency or salary-range disclosure obligations: `[VERIFY: pay-transparency requirements in work jurisdiction]`;
   - Salary-history inquiry or reliance limits: `[VERIFY: salary-history restrictions in work jurisdiction]`;
   - Ban-the-box or criminal-history inquiry timing rules: `[VERIFY: ban-the-box requirements in work jurisdiction]`;
   - Wage notice or pay-stub obligations at onboarding: `[VERIFY: wage notice obligations in work jurisdiction]`;
   - Any other onboarding-document or timing requirement specific to the work jurisdiction: `[VERIFY: additional onboarding requirements in work jurisdiction]`.
   If the employer's standard hiring-practices playbook was provided, note whether it addresses each of these categories and flag any apparent gaps for attorney confirmation.

6. **Offer-letter content review.** Review the body of the offer letter for the following elements and note whether each is present, absent, or ambiguous:
   - At-will language or equivalent: if present, flag `[verify jurisdiction]` — whether at-will employment applies or is legally meaningful in the work jurisdiction must be confirmed;
   - Offer contingencies (background check, reference check, drug test, work authorization): identify each contingency stated and note any that appear missing given standard practice `[CONFIRM: contingencies are complete]`;
   - Start date;
   - Role title — confirm it matches the title stated in the compensation section and, if applicable, in any equity documents;
   - Base salary or wage rate — confirm internal consistency across the offer and any exhibits;
   - Reporting line or supervisor;
   - Equity or bonus terms — confirm internal consistency with any equity grant documents referenced; flag any equity terms stated in the offer that are not substantiated by an attached grant agreement `[CONFIRM: equity terms match grant documentation]`;
   - Integration or entire-agreement clause — note whether present and whether it supersedes prior representations;
   - Offer expiration or acceptance deadline: note whether stated and flag `[deadline verification required]` if a deadline is present.

7. **Conformance check (if playbook provided).** If the employer's standard hiring-practices playbook was provided, compare the offer against it. Note any deviations — terms that differ from the standard template, provisions that are present in the template but absent from the offer, or non-standard additions. Flag each deviation for attorney assessment.

8. **Identify open items and action items.** Compile a consolidated list of every issue, discrepancy, missing provision, and flagged question identified in Steps 2 through 7. Assign a priority level — High, Medium, or Low — to each item based on its legal significance and likelihood of creating liability or dispute.

9. **Render the verdict.** Select one of the following four verdict options and provide a two-to-four sentence bottom line explaining the basis:
   - **Clear to send / proceed**: no material issues identified; attorney may proceed after confirming verification items.
   - **Changes needed**: specific issues must be resolved before the offer is sent or signed; identified in action items.
   - **Escalate**: issues present that require attorney judgment before proceeding; cannot be resolved through document edits alone.
   - **Hold — research needed**: one or more jurisdiction-specific questions are unresolved and must be researched before the offer can be assessed.

10. **Assemble the output.** Produce the full structured draft hiring review memo labeled as a draft for attorney review, in the format described below.

## Output Format

Deliver the following sections, clearly labeled, in a document headed **DRAFT HIRING REVIEW MEMO — FOR ATTORNEY REVIEW ONLY — NOT LEGAL ADVICE**:

1. **Verdict and Bottom Line** — one of the four verdict options, followed by a two-to-four sentence explanation of the principal basis.

2. **Work Jurisdiction** — the confirmed work location; any choice-of-law discrepancy noted; all jurisdiction flags carried forward from the analysis.

3. **Classification Check** — the proposed classification; the role duties and compensation as stated; the flag-list of classification questions `[verify jurisdiction]`; any apparent inconsistency.

4. **Restrictive Covenants** — one subsection per covenant type present, each covering scope, remedies, enforceability flag `[verify jurisdiction]`, and any breadth observation. If no covenants were provided, note the absence.

5. **Jurisdiction-Specific Statutory Requirements** — the checklist of open verification questions from Step 5, each flagged `[VERIFY: ...]`.

6. **Offer-Letter Content Review** — element-by-element table or list: element, status (present / absent / ambiguous), and any flag or note.

7. **Conformance Check** — deviations from the employer's standard template, if the playbook was provided; otherwise state "Employer hiring-practices playbook not provided."

8. **Action Items** — consolidated, prioritized list of all issues and open questions, with priority (High / Medium / Low) and recommended next step for each.

9. **Assumptions and Limitations** — explicit list of everything assumed or not confirmed, and the boundaries of what this review covered.

Use placeholders throughout: `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, `[deadline verification required]`, `[citation needed]` as appropriate.

## Attorney Verification Checklist

- [ ] The offer letter text reviewed is the final, complete version — not a draft or summary.
- [ ] All restrictive-covenant exhibits are present and reviewed; none are missing or referenced but not provided.
- [ ] The candidate's actual work location is confirmed and is the location used for all statutory and enforceability analysis.
- [ ] The proposed exempt or non-exempt classification has been verified against the applicable duties test and salary threshold under governing law as of the offer date.
- [ ] Each restrictive covenant has been assessed for enforceability under the law of the work jurisdiction, including any recent statutory or regulatory changes.
- [ ] All jurisdiction-specific onboarding and pay-transparency requirements have been confirmed for the work jurisdiction.
- [ ] At-will employment language (if present) is appropriate for the work jurisdiction.
- [ ] All offer contingencies are appropriate and complete for the role.
- [ ] Equity or bonus terms stated in the offer are consistent with grant documentation.
- [ ] Any offer expiration or acceptance deadline is confirmed and compliant with applicable law `[deadline verification required]`.
- [ ] No legal authority, citation, or statutory rule has been asserted in this memo without independent verification by counsel.
- [ ] All assumptions and open items identified in this memo are resolved before the offer is sent or signed.
- [ ] Client-identifying information has been removed from any version of this memo retained as a reusable template.
