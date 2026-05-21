---
name: Matter Intake
description: Use when opening a new litigation or dispute matter to produce a structured intake summary capturing parties, claims, jurisdiction, key dates, and immediate action flags for attorney review.
---

# Matter Intake

## Purpose

Produce a structured, attorney-ready intake summary for a new litigation or dispute matter. The skill guides systematic collection of the information needed to open a file, identify conflicts, trigger preservation obligations, and surface immediate action items. It produces draft legal work product for attorney review — not legal advice and not a final case assessment.

## Use When

- A new dispute, claim, or litigation matter is being opened and a structured intake record is needed.
- A user asks to "open a new matter," "intake this dispute," or "set up a file for this case."
- A client has received a complaint, demand letter, or threat of litigation and initial triage is required.
- A conflict check, litigation hold, or insurance notice obligation needs to be flagged at the outset.
- A lawyer or paralegal needs a repeatable checklist-driven intake process.

## Required Inputs

- Identity of the client: name, entity type, and role in the dispute (plaintiff, defendant, third party, etc.).
- Names and roles of all known opposing parties and other significant parties.
- A plain-language description of the dispute or claims (summary, complaint, demand letter, or similar).
- The relevant jurisdiction(s) and forum (court, arbitral body, regulatory agency, or unknown).
- Any known key dates: date of incident, date of filing, service date, response deadline, statute of limitations dates.

If the client identity or a basic description of the dispute is not provided, stop and request them. Do not assume the client's role or fabricate party names, claims, or dates.

## Do Not Use When

- The matter is transactional rather than a dispute or litigation (use a contract or deal intake skill instead).
- A subpoena has been received and the primary task is subpoena triage (use `subpoena-triage`).
- The user needs a full factual chronology built from documents (use `litigation-chronology`).
- The user needs a demand letter drafted (use `demand-letter`).
- The matter is already open and the goal is case status review rather than initial intake.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Do not invent, compute, or assert any procedural deadline, statute of limitations period, or response date. Mark every deadline as `[CONFIRM: attorney must verify]`.
- Do not resolve conflicts-check results — flag that a conflicts check must be run and confirmed by the responsible attorney.
- Do not assert that a litigation hold is or is not required — flag it as a preservation obligation that must be evaluated by an attorney.
- Do not assert insurance coverage or indemnity rights — flag them as items requiring attorney and client verification.
- Separate confirmed facts (from documents) from client representations from assumptions. Label each category clearly.
- Do not place client-sensitive facts into reusable templates. Every intake summary is a matter-specific work product.
- If any required input is missing, record a `[CONFIRM: ...]` placeholder; never fabricate the missing information.
- Privilege and confidentiality: the intake summary itself may be attorney-client privileged or attorney work product — label it accordingly and note that distribution should be limited.

## Workflow

1. **Confirm inputs.** Verify that client identity, client role, and a dispute description have been provided. If not, stop and request the missing information before proceeding.

2. **Identify the client and client role.** Record the client's full legal name, entity type (individual, corporation, LLC, partnership, trust, government body, etc.), and role in the dispute. Note aliases, trade names, or related entities if known.

3. **Identify all parties.** List every known party: plaintiff(s), defendant(s), third-party defendants, cross-claimants, intervenors, and any unnamed or "Doe" parties. Record entity type and role for each. Note aliases and related entities where provided.

4. **Summarize the dispute.** Provide a plain-language summary of the nature of the dispute, the underlying facts as described or alleged, and the harm or injury at issue. Clearly label this summary as based on provided information only.

5. **Identify claims and causes of action.** List all claims or causes of action that have been asserted or that appear likely to be asserted, noting who is asserting them and against whom. Label each as "asserted" (present in a filed pleading or demand) or "anticipated" (not yet formally asserted). Do not characterize the legal merit of any claim.

6. **Identify procedural posture.** Record whether litigation has been filed, at what stage (pre-litigation, demand stage, complaint filed, answer due, discovery, motions pending, trial scheduled, appellate, etc.), and in what forum. Note the case number or docket identifier if available.

7. **Identify jurisdiction and venue.** Record the jurisdiction(s) (federal, state, foreign, arbitral), the specific court or forum, the governing-law provision if known (e.g., from a contract), and any venue or jurisdictional issues flagged by the user. Mark unresolved jurisdiction or venue questions as `[CONFIRM]`.

8. **Record key dates.** List all dates provided: incident date, filing date, service date, answer or response deadline, statute of limitations expiration, arbitration demand deadline, and any other deadlines or milestones. Mark every deadline as `[CONFIRM: attorney must verify deadline and method of calculation]`. Never compute, extend, or assert a deadline.

9. **Flag conflicts check — gate.** Record all party names and aliases for conflicts screening. This step is a gate: the matter must not proceed past intake — no work may be performed and no engagement confirmed — while a potential conflict remains unresolved, unless the responsible attorney has documented in writing their authorization to proceed notwithstanding the identified conflict (e.g., informed consent, waiver, or screen). Record the gate status as one of: (a) `[ACTION: conflicts check not yet run — matter gated; do not proceed]`, (b) `[ACTION: potential conflict identified — matter gated pending documented attorney authorization]`, or (c) `[CONFIRM: conflicts check cleared — attorney to confirm before matter proceeds]`. Do not characterize whether a conflict is waivable or consentable; that determination is for the responsible attorney `[verify jurisdiction]`.

10. **Flag litigation hold / preservation obligation.** Based on the parties and claims described, note that an attorney must immediately evaluate whether a litigation hold notice is required and to whom it must be sent. Record known or likely custodians of relevant documents and ESI. Do not assert that a hold is or is not required. When an attorney has determined a hold is warranted, use `legal-hold` to prepare the notice.

11. **Flag insurance and indemnity.** Note whether any insurance policy, indemnity agreement, or tender obligation may be implicated. Record policy information if provided. Flag as `[ACTION: verify coverage and notice requirements with client and coverage counsel]`. Never assert coverage.

12. **List immediate action items.** Compile a prioritized list of actions that must be taken promptly: conflict check, litigation hold evaluation, insurance notice, answer or response deadline verification, client communication, document preservation, and any other time-sensitive items flagged in the intake.

13. **Preliminary risk and materiality assessment.** Based solely on the information provided in this intake — without access to discovery, full facts, or legal analysis — record a preliminary triage signal for portfolio-management purposes only. These are not legal conclusions and are explicitly labeled `[ATTORNEY TO CONFIRM]`.

    - **Risk band:** Assign a preliminary band of Low, Medium, or High with a one-sentence rationale drawn only from the intake facts (e.g., nature of claims, scale of alleged harm, procedural posture). Do not predict outcome or assess legal merit.
    - **Materiality posture:** Assign a preliminary materiality posture relevant to the organization's financial reporting or risk-management obligations, selecting from: None (no current reporting or reserve signal), Monitor (track but no current action), Reserve (potential financial reserve may be warranted — attorney/finance to assess), or Disclose (potential disclosure obligation — attorney to assess). This signal does not constitute accounting, auditing, or securities advice.

    Both signals must carry the tag `[ATTORNEY TO CONFIRM: preliminary triage only — not a legal conclusion]` and a note that they may change materially as facts develop. If insufficient information was provided to form even a preliminary signal, record `[CONFIRM: insufficient information to assess — attorney to triage]` for each item.

14. **Assemble the intake summary.** Organize all of the above into a structured document using the output format below. Label every section, mark all placeholders and confirmation items, and append the attorney verification checklist.

## Output Format

Deliver a structured Matter Intake Summary with the following sections:

1. **Matter Header** — Client name, matter name/description, date of intake, attorney/preparer.
2. **Client and Client Role** — Full name, entity type, role in dispute, aliases.
3. **Parties** — Table of all parties: Name | Entity Type | Role | Aliases/Related Entities | Counsel (if known).
4. **Dispute Summary** — Plain-language narrative of the dispute and alleged harm. Labeled as based on provided information.
5. **Claims and Causes of Action** — Bulleted list: Claim | Asserted by | Against | Status (asserted/anticipated).
6. **Procedural Posture** — Forum, stage, case number if known.
7. **Jurisdiction and Venue** — Jurisdiction, court/forum, governing law, open issues.
8. **Key Dates and Deadlines** — Table: Date | Event/Deadline | Source | `[CONFIRM]` flag.
9. **Conflicts Check Gate** — Party list for conflicts screening; gate status (not yet run / potential conflict gated / cleared); documented attorney authorization if applicable.
10. **Litigation Hold / Preservation Flag** — Known custodians; attorney evaluation required.
11. **Insurance and Indemnity Flag** — Known policies or agreements; notice obligation flag.
12. **Immediate Action Items** — Prioritized checklist.
13. **Preliminary Risk and Materiality Assessment** — Risk band (Low / Medium / High) with one-sentence rationale; materiality posture (None / Monitor / Reserve / Disclose); both tagged `[ATTORNEY TO CONFIRM: preliminary triage only — not a legal conclusion]`.
14. **Assumptions and Open Items** — All `[CONFIRM: ...]` placeholders and unresolved items.

Use `[CONFIRM: ...]` for every unverified or missing item. Use `[ACTION: ...]` for every required attorney or client step.

## Attorney Verification Checklist

- [ ] Client identity and role confirmed with client.
- [ ] All party names and aliases captured for conflicts screening.
- [ ] Conflicts check run; gate status confirmed: if a potential conflict was identified, documented attorney authorization to proceed is on file before any work is performed.
- [ ] All deadlines independently verified — none computed or relied upon from this intake alone.
- [ ] Statute of limitations and any tolling issues evaluated by attorney.
- [ ] Litigation hold / document preservation obligation evaluated and, if required, hold notice issued.
- [ ] Insurance and indemnity notice obligations evaluated; timely notice given if required.
- [ ] Jurisdiction and venue confirmed; no waiver issues.
- [ ] Governing law identified and confirmed.
- [ ] Privilege and confidentiality of intake summary protected; distribution limited.
- [ ] Preliminary risk band and materiality posture reviewed and confirmed or revised by responsible attorney; triage signals updated as facts develop.
- [ ] Assumptions and open items resolved before intake summary is relied upon.
- [ ] Client has been advised of attorney-client relationship scope and engagement terms.
