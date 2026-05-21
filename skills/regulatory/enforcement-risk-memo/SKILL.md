---
name: Enforcement Risk Memo
description: Use when structuring a memo that assesses potential enforcement exposure for a described practice, conduct, or set of facts, to produce attorney-ready draft analysis for review.
---

# Enforcement Risk Memo

## Purpose

Produce a structured, attorney-ready draft memo assessing potential regulatory enforcement exposure for a described situation, conduct, or practice. The output organizes the facts, identifies the regulatory framework as supplied by the user, applies an analytical structure (elements, mitigating and aggravating factors, plausible regulator responses), and surfaces verification items — without predicting outcomes, inventing enforcement precedent, or asserting what any regulation requires.

This skill provides workflow discipline and output structure. It does not provide legal advice.

## Use When

- A user asks to "assess our enforcement risk," "memo out the exposure here," or "what could a regulator do."
- A client describes a business practice or past conduct and wants to understand how a regulator might view it.
- Counsel needs a structured first-pass risk assessment to organize facts and frame the legal analysis before drafting advice.
- An internal compliance or legal team needs to document a risk assessment for audit, governance, or privilege log purposes.
- The user provides (or references) specific regulatory rules and asks for analysis of whether those rules are implicated.

## Required Inputs

- **Conduct or practice at issue**: a concrete description of what happened or is happening. If vague, ask for specifics — dates, actors, decisions, volumes, systems affected.
- **Regulator(s)**: the agency or agencies the user believes have jurisdiction (e.g., SEC, CFPB, FTC, state AG, FDA). Do not invent or assume regulators.
- **Rule(s) or framework**: the specific rule, statute, or guidance the user believes may be implicated. If the user cannot identify rules, note this as a gap and flag it as an attorney verification item; do not supply rules from model knowledge without clearly marking them `[UNVERIFIED — attorney must confirm]`.
- **Relevant facts**: who, what, when, where, why. Ask follow-up questions if the factual record is incomplete.
- **Client posture**: are we counseling the entity under review, a potential whistleblower, an industry participant, or another role? This affects tone and analytical framing.
- **Jurisdiction and governing law**: state/federal, domestic/cross-border. Flag as `[CONFIRM]` if unclear.

If any required input is missing, stop and request it. Do not fabricate facts, rules, or regulatory history.

## Do Not Use When

- The user needs a full compliance audit or control-mapping exercise (use `compliance-gap-matrix`).
- The user needs a summary of what a rule change requires (use `rule-change-summary`).
- The matter involves active litigation or a filed enforcement action where counsel is already engaged — this skill produces preliminary analytical scaffolding, not litigation strategy.
- The user has not provided any description of the conduct or practice at issue.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Do not predict enforcement outcomes as certainties. Use language such as "potential exposure," "a regulator might argue," "one plausible response," or "this factor could weigh against."
- Do not invent enforcement precedent, settlement statistics, penalty ranges, or agency policy statements. If the user provides documents containing such data, summarize them; otherwise, flag the need to research and verify.
- Do not assert what a regulation requires. Every statement about rule content must trace to text provided by the user or be explicitly marked `[UNVERIFIED — attorney must confirm rule text]`.
- Never invent citations, docket numbers, effective dates, or agency guidance. Use `[CONFIRM: cite]` placeholders.
- Clearly separate: (a) facts as provided, (b) assumptions and inferences, (c) analytical framework, (d) attorney-verification items.
- Do not place client-identifying or sensitive facts into any reusable template.
- Flag every point of uncertainty rather than resolving it silently.
- Identify jurisdiction, governing law, relevant date, regulatory posture, and client posture — or flag each as `[CONFIRM]`.

## Workflow

1. **Confirm inputs.** Review what the user has provided against the Required Inputs list. If anything is missing or ambiguous, ask targeted clarifying questions before proceeding. Do not begin analysis with incomplete facts.

2. **Identify the regulatory framework.** List the regulator(s) and rule(s) as provided by the user. Note the document source for each. If a rule was not provided but identified from model background knowledge, label it `[UNVERIFIED — attorney must confirm rule text and current version]`.

3. **Organize the facts.** Lay out the factual record in chronological or logical order. Distinguish facts stated by the user from assumptions and inferences. Note factual gaps that could affect the analysis.

4. **Frame the exposure analysis.** For each rule or provision identified:
   - State what elements or conditions would need to be satisfied for the conduct to fall within the rule's reach.
   - Apply those elements to the facts, noting where the facts are clear, ambiguous, or missing.
   - Do not resolve ambiguities as legal conclusions — surface them as items requiring attorney judgment.

5. **Identify mitigating factors.** What facts, circumstances, or conduct tend to reduce risk (e.g., remediation, lack of intent, disclosure, industry practice, prior guidance relied upon)? Note each as a potential mitigating factor, not a guaranteed defense.

6. **Identify aggravating factors.** What facts, circumstances, or patterns could increase regulator interest or penalty exposure (e.g., recidivism, harm to consumers, failure to remediate, concealment)? Note each candidly.

7. **Map the range of plausible regulator responses.** Without predicting outcomes, describe the spectrum of possible responses from the lowest-severity end (no action, informal inquiry, warning letter) to the highest (formal investigation, enforcement action, referral, penalty). Note which factors would push toward each end.

8. **Draft recommended next steps.** Identify what additional information, legal research, or remedial action the attorney should consider. This section is preliminary scaffolding — the supervising attorney sets actual strategy.

9. **Compile attorney verification items.** List every point in the memo where rule text, precedent, facts, dates, or legal conclusions must be independently confirmed before the memo is relied upon.

10. **Assemble and label the output.** Mark the entire document as a draft for attorney review, confirm the Assumptions section is complete, and ensure every unverified rule, fact, date, or conclusion is flagged with `[CONFIRM]`.

## Output Format

Deliver the following sections in order:

**DRAFT ENFORCEMENT RISK MEMO — FOR ATTORNEY REVIEW ONLY**

1. **Question Presented** — One or two sentences stating the core enforcement risk question.

2. **Summary Assessment** — Two to four sentences summarizing the level and nature of potential exposure, using appropriately qualified language. No outcome predictions.

3. **Facts** — Numbered or bulleted factual summary. Distinguish provided facts from assumptions. Flag gaps as `[FACTUAL GAP — confirm]`.

4. **Assumptions** — Explicit list of assumptions the analysis depends upon.

5. **Applicable Rules [Attorney to Verify]** — Table or list: Rule | Source/Citation | Provided by User or Unverified | Key Provision Summary. Every entry includes a `[CONFIRM]` note if not drawn from user-provided text.

6. **Analysis** — Element-by-element or factor-by-factor application of rules to facts. Use qualified language throughout. Do not assert legal conclusions.

7. **Mitigating Factors** — Bulleted list of facts or circumstances that could reduce exposure.

8. **Aggravating Factors** — Bulleted list of facts or circumstances that could increase exposure.

9. **Range of Plausible Regulator Responses** — Brief description of the spectrum from no action to maximum exposure, tied to specific factors.

10. **Recommended Next Steps** — Bulleted preliminary list for attorney consideration (research, remediation, disclosure analysis, privilege review, etc.).

11. **Attorney Verification Items** — see the Attorney Verification Checklist below.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] All facts in the memo accurately reflect the client's actual situation; no material facts were omitted or misstated.
- [ ] Each rule, statute, regulation, and guidance document cited exists, is in force, and the quoted or summarized text is accurate.
- [ ] No rule content was supplied from model background knowledge without independent verification of current text.
- [ ] No enforcement precedent, penalty range, or agency policy statement was assumed or invented — all such references trace to provided or independently researched sources.
- [ ] Jurisdictional scope, governing law, and applicable regulatory body have been confirmed.
- [ ] The relevant date (date of conduct, date of rule, date of analysis) has been established and is correct.
- [ ] All factual gaps identified in the memo have been resolved or their effect on the analysis has been evaluated.
- [ ] Mitigating and aggravating factors have been assessed against current regulatory guidance and enforcement trends, not assumed.
- [ ] Client posture and privilege status have been reviewed; appropriate markings are applied.
- [ ] Recommended next steps reflect the supervising attorney's actual strategic judgment, not solely this draft.
- [ ] The memo is labeled as draft work product and is not transmitted to any third party without attorney review and approval.
