---
name: Subpoena Triage
description: "Use when an incoming subpoena has been received to produce a structured triage summary identifying the compliance deadline, scope, objections, privilege issues, preservation obligations, and internal notification requirements for immediate attorney review."
practice_area: litigation
task_type: triage
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The received subpoena"
  - "The recipient's role and relationship to the matter"
  - "Any related preservation or notification context"
outputs:
  - "Structured subpoena triage summary identifying deadlines, scope, objections, and privilege issues for immediate attorney review"
related_skills:
  - skills/litigation/matter-intake/SKILL.md
  - skills/litigation/legal-hold/SKILL.md
tags:
  - litigation
  - subpoena
  - triage
  - discovery
  - deadlines
---

# Subpoena Triage

## Purpose

Produce a structured triage summary for an incoming subpoena requiring prompt attorney evaluation. The skill identifies the subpoena type, issuing authority, compliance deadline, scope of what is demanded, the recipient's status (party or non-party), potential objections, privilege and preservation obligations, and who must be notified internally. The compliance deadline is flagged as **time-critical** — attorney must verify it immediately. This skill produces draft legal work product for attorney review — not legal advice and not a response or objection to the subpoena.

> **CRITICAL: Subpoena compliance deadlines are strictly enforced and may be very short (sometimes 3–14 days). The attorney must verify the deadline immediately upon receiving this triage summary. Do not rely on any deadline noted here without independent attorney verification.**

## Use When

- A subpoena has been received by the client, the organization, or a custodian of records and triage is needed.
- A user asks to "triage this subpoena," "we got a subpoena, what do we do," or "review this subpoena."
- Counsel needs to quickly identify objection grounds, privilege issues, and internal notification obligations when a subpoena arrives.
- An organization needs a structured process for handling subpoenas received in connection with third-party litigation.
- A non-party has been served and needs to evaluate its obligations before a compliance deadline runs.

## Required Inputs

- The full text of the subpoena (uploaded or pasted). Do not triage from a description alone — the actual subpoena must be reviewed.
- The identity of the recipient: who was served (the individual, entity, or custodian of records).
- Whether the recipient is a party to the underlying litigation or a non-party third party.
- The date of service (to evaluate the compliance deadline — attorney must verify the computation).

If the subpoena text is not provided, stop and request it. Do not complete a triage without reviewing the actual subpoena.

## Do Not Use When

- No subpoena has been provided — do not triage from a description; the actual document must be reviewed.
- The user needs to draft a response or objection to the subpoena — this skill produces a triage summary only; a response or objection requires separate attorney-directed work.
- The document is a **grand-jury subpoena** or is otherwise part of a criminal proceeding — stop immediately and route to criminal-defense counsel. Do not triage a grand-jury subpoena as a civil subpoena; the procedures, risks, and obligations are materially different and this workflow does not apply.
- The document is a **civil investigative demand** issued by an enforcement or regulatory authority — those instruments carry enforcement-specific requirements distinct from ordinary civil subpoenas and must be handled with counsel experienced with the issuing authority. Do not triage a civil investigative demand as a civil subpoena.
- The user has received a regulatory inquiry or government investigation demand — those instruments have distinct requirements and should be handled with specialized counsel.
- The document is a summons and complaint rather than a subpoena (use `matter-intake` for new litigation service).
- The user needs an initial matter intake for the underlying litigation (use `matter-intake` first, then return to this skill).

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- **Consult `connectors/pacer-recap.md` when a verification path is available** to confirm that a referenced federal docket and filing exist and to record the docket number and the filed date as it appears on the docket — for existence and recorded metadata only, never to compute, confirm, or extend the compliance deadline, which stays `[CRITICAL — CONFIRM IMMEDIATELY]`; when no connector is available, the placeholder discipline is unchanged.
- **The compliance deadline is time-critical. Never compute, assert, or represent the compliance deadline as established. Mark it as `[CRITICAL — CONFIRM IMMEDIATELY: attorney must verify the deadline and any available extensions before any other step is taken]`.**
- Do not assert that any objection is valid or will be sustained — identify potential objections for attorney evaluation only.
- Do not assert that any document or communication is privileged — flag categories of potentially privileged material for attorney-directed privilege review.
- Do not instruct the recipient to withhold any documents without attorney authorization. Unauthorized non-compliance with a subpoena can result in contempt.
- Do not assert that a litigation hold is or is not required — flag it as a preservation obligation requiring attorney evaluation.
- Distinguish what the subpoena says from what is assumed or inferred. Quote the subpoena accurately.
- Do not advise on whether to comply, object, negotiate, or seek a protective order — identify the options and flag them for attorney decision.
- Identify who must be notified internally but do not assert that notice is or is not legally required — flag it for attorney confirmation.
- **KILL-SWITCH — Grand-jury subpoena or criminal process:** If at any point the subpoena is identified as a grand-jury subpoena or any other form of criminal process, stop this workflow immediately. Do not complete or deliver a civil triage summary. Flag the matter as criminal process, note that the procedures, risks, and obligations are materially different from those that apply to civil subpoenas, and route immediately to criminal-defense counsel. The same stop-and-route rule applies if, after reviewing the document, it becomes apparent that what was presented as a civil subpoena is in fact criminal process.
- **KILL-SWITCH — Civil investigative demand:** If the document is a civil investigative demand issued by an enforcement or regulatory authority, stop this civil-triage workflow immediately. Flag that the document is a civil investigative demand, note that it carries enforcement-specific requirements distinct from ordinary civil subpoenas, and route to counsel experienced with the issuing authority.
- Preserve confidentiality: the triage summary is attorney work product. Limit distribution.

## Workflow

1. **Confirm inputs.** Verify that the full subpoena text has been provided. If not, stop and request it. Do not proceed without the actual subpoena.

2. **Identify the subpoena type — including criminal-process recognition.** Review the face of the document and determine which category applies:

   - **Grand-jury subpoena:** The document commands appearance or production before a grand jury, or is issued in connection with a grand-jury investigation. **STOP — KILL-SWITCH TRIGGERED.** Do not continue this civil-triage workflow. Flag the document as grand-jury/criminal process, note that the procedures, risks, and obligations are materially different from those governing civil subpoenas, and route immediately to criminal-defense counsel. Do not triage it as a civil subpoena.
   - **Civil investigative demand (CID) or enforcement-authority demand:** The document is issued by an enforcement or regulatory authority (rather than a court in civil litigation) and commands production or responses in connection with an investigation or enforcement action. **STOP — KILL-SWITCH TRIGGERED.** Do not continue this civil-triage workflow. Flag the document as a civil investigative demand, note that it carries enforcement-specific requirements, and route to counsel experienced with the issuing authority. Do not triage it as a civil subpoena.
   - **Ordinary civil subpoena — testimony only (deposition subpoena):** The subpoena commands testimony in a civil proceeding. Continue the workflow.
   - **Ordinary civil subpoena — documents/records only (subpoena duces tecum):** The subpoena commands production of documents or records in a civil proceeding. Continue the workflow.
   - **Ordinary civil subpoena — testimony and documents:** The subpoena commands both. Continue the workflow.

   If the category cannot be determined from the face of the document, flag it as `[VERIFY: nature of process — cannot confirm whether this is a civil subpoena, grand-jury subpoena, or civil investigative demand; attorney must confirm before any further action]` and do not continue the workflow without attorney guidance.

3. **Identify the issuing authority.** Record the court or authority that issued the subpoena (federal court, state court, regulatory agency, arbitral body, etc.), the case name and docket number, and the issuing party (the attorney or party who caused the subpoena to issue).

4. **Identify the recipient.** Record who was served: the individual's name, organizational role if applicable, or the entity's name and the specific custodian or records manager served. Confirm whether the recipient is a **party** or **non-party** to the underlying litigation — this affects objection grounds and procedural rules.

5. **Flag the compliance deadline — CRITICAL.** Record the compliance date and time stated on the face of the subpoena. Identify the date of service. Mark the deadline as `[CRITICAL — CONFIRM IMMEDIATELY: attorney must verify the deadline, the method of service, and whether the deadline is valid and has been properly computed. Do not take or forego any action based on this date alone.]` Note that extensions may be available by stipulation or motion, but only if sought promptly.

6. **Identify the scope of the demand.** Summarize what is demanded:
   - For document/records subpoenas: list each category of documents requested, any date ranges, any defined terms, and any limitations stated.
   - For deposition subpoenas: identify the topics or subject matter listed, the date and location of the deposition.
   - Note whether the scope appears targeted and specific or broad and potentially overbroad.

7. **Identify potential objections.** For each category of demand, identify potential grounds for objection, for attorney evaluation only. Common grounds include:
   - **Overbreadth**: the request is unlimited in time, scope, or subject matter.
   - **Undue burden**: compliance would require disproportionate effort or cost relative to the relevance of the information.
   - **Relevance**: the requested material does not appear relevant to the subject matter of the underlying litigation.
   - **Privilege**: the requested material may be protected by attorney-client privilege, attorney work product, trade secret, or another recognized privilege.
   - **Jurisdictional / procedural defect**: the subpoena was not properly issued, served, or does not comply with applicable procedural rules (e.g., geographic limits on subpoena reach).
   - **Confidentiality**: the requested material is subject to a confidentiality agreement, protective order, or privacy law.
   Mark each objection as a potential ground for attorney evaluation — do not assert that any objection is meritorious.

8. **Flag privilege and confidentiality issues.** Identify categories of documents or communications that may be privileged or protected: attorney-client communications, attorney work product, trade secrets, personally identifiable information, healthcare records, financial records, or material subject to a protective order. Flag these for attorney-directed privilege review before any production. Note that a privilege log may be required.

9. **Flag litigation hold / preservation obligation.** Note that receipt of a subpoena may trigger or reinforce a duty to preserve relevant documents and ESI. Flag for attorney evaluation: whether a hold is already in place, whether a new or supplemental hold notice is required, and who the relevant custodians are. Do not assert that a hold is or is not required. When a hold notice is required, use `legal-hold` to prepare it.

10. **Identify internal notification requirements.** Based on the subpoena's scope and the recipient's organizational role, identify who within the organization should be notified: legal department, HR, IT (for ESI preservation), records management, the specific custodians named or implicated, and senior leadership if appropriate. Mark as `[CONFIRM: attorney to confirm required internal notifications and any applicable corporate policy]`.

11. **Identify external notification requirements.** Note whether other parties to the underlying litigation must be notified (e.g., the party whose case is the subject of the subpoena), and whether any contractual or court-order notification obligation applies. Mark as `[CONFIRM: attorney to evaluate]`.

12. **Compile immediate action items.** Prioritize actions required within the next 24–48 hours and within the compliance window: attorney notification, deadline verification, litigation hold evaluation, internal custodian notification, IT hold, and evaluation of whether to comply, object, negotiate, or move for a protective order.

13. **Assemble the triage summary.** Organize all of the above into a structured triage summary using the output format below. Label as draft attorney work product. Prominently display the unverified deadline and the critical action items at the top.

## Output Format

Deliver a Subpoena Triage Summary with the following sections:

1. **Critical Action Items (TOP)** — Prominently listed before all other content: unverified compliance deadline, attorney notification, litigation hold flag, and immediate steps required.
2. **Subpoena Identification** — Type, issuing court/authority, case name and docket number, issuing party/counsel.
3. **Recipient Identification** — Who was served, organizational role, party or non-party status.
4. **Compliance Deadline** — Date stated on the subpoena, date of service, marked `[CRITICAL — CONFIRM IMMEDIATELY]`.
5. **Scope of Demand** — Table of each category demanded: Category | Date Range | Description | Initial Assessment.
6. **Potential Objections** — Table: Objection Ground | Applicable to Which Request(s) | Initial Notes | Attorney Evaluation Required.
7. **Privilege and Confidentiality Flag** — Categories of potentially protected material; privilege review required.
8. **Litigation Hold / Preservation Flag** — Relevant custodians; attorney evaluation required.
9. **Internal Notification Required** — Persons and departments to notify; `[CONFIRM]`.
10. **External Notification Required** — Other parties or third parties to notify; `[CONFIRM]`.
11. **Options for Attorney Consideration** — Comply in full, partial compliance with objections, negotiated scope reduction, motion to quash or modify, motion for protective order.
12. **Open Items for Attorney Verification** — All `[CONFIRM]`, `[CRITICAL]`, and unresolved items.

## Attorney Verification Checklist

- [ ] **CRITICAL:** Compliance deadline independently verified — do not rely on the triage summary deadline alone.
- [ ] Method and date of service verified; deadline computation confirmed.
- [ ] Extension request evaluated — if more time is needed, it must be sought immediately.
- [ ] Subpoena procedurally valid: issued by proper court or authority, properly served, within geographic limits.
- [ ] Recipient's status as party or non-party confirmed; applicable procedural rules identified.
- [ ] Scope of each demand category evaluated for relevance, overbreadth, and undue burden.
- [ ] All potential objection grounds evaluated; decision made on whether to object, comply, or negotiate.
- [ ] Privilege review initiated for all potentially protected categories; privilege log evaluated.
- [ ] Litigation hold / preservation evaluation completed; hold notice issued if required.
- [ ] Internal notifications sent to all required personnel (legal, HR, IT, custodians, leadership as appropriate).
- [ ] External notification obligation (if any) evaluated and fulfilled.
- [ ] Response strategy determined: comply, object, negotiate, move to quash, or move for protective order.
- [ ] Client (or organizational leadership) informed of the subpoena and the chosen response strategy.
- [ ] Triage summary labeled as attorney work product and distribution appropriately limited.
