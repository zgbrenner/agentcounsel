---
name: DSAR Workflow
description: Use when an organization receives a data subject access request (or any data subject rights request) and needs a structured triage, handling record, and response plan for attorney review.
---

# DSAR Workflow

## Purpose

Produce a structured triage record and response plan for a data subject access request (DSAR) or other data subject rights request (deletion, correction, portability, restriction, objection, opt-out, etc.). This skill organizes the operational workflow — logging, identity verification, request classification, system scoping, response structure, and documentation — so that the legal and compliance team has a complete, attorney-ready handling record. It produces draft legal work product for attorney review — not legal advice.

This skill provides workflow discipline only. It does not determine which privacy law applies, whether a particular exemption is available, whether the requester has a legal right to the requested action, or when the response deadline falls. All such determinations are attorney-verification items. Response deadlines in particular must never be computed from model knowledge — they vary by jurisdiction, framework, and request type, and must be confirmed with counsel or by reference to verified current authority.

## Use When

- An individual has submitted a request to access their personal data ("please send me all data you hold about me").
- An individual has requested deletion, erasure, or "right to be forgotten" of their personal data.
- An individual has requested correction or rectification of inaccurate personal data.
- An individual has requested portability of their personal data in a structured, machine-readable format.
- An individual has submitted a request to restrict or object to processing of their personal data.
- An individual has submitted an opt-out of sale, sharing, or targeted advertising request.
- An internal team (legal ops, privacy, compliance) needs a structured intake and handling record for any of the above.
- The organization is building or auditing its DSAR intake and response process and needs a template workflow.
- A regulator has inquired about the organization's handling of a specific data subject request.

## Required Inputs

- **The request itself** — the full text or a faithful summary of what the individual submitted, and the channel through which it was received (email, web form, postal mail, in-product form, verbal, etc.).
- **Date the request was received** — required for deadline tracking. If the date is ambiguous, flag as `[CONFIRM: date received]`.
- **Organization's name and role** — whether the organization is a controller, processor, or acting in another capacity with respect to the data in question. If unclear, flag as `[CONFIRM: client role]`.
- Optional: the identity information already provided by the requester (name, email, account number, etc.), needed for the identity verification step.
- Optional: any prior correspondence with the requester about this or related requests.
- Optional: the applicable privacy framework(s) the organization operates under, as confirmed by counsel (e.g., GDPR, CCPA/CPRA, state law). Do not independently assert which law applies.

If the request text and date received are not provided, stop and request them. Do not fabricate request details.

## Do Not Use When

- The task is to review a privacy policy or notice (use `privacy-policy-gap-review`).
- The task is to review a DPA (use `dpa-review`).
- The incoming communication is a regulatory inquiry, enforcement action, or subpoena — those require separate legal handling, not a DSAR workflow.
- The organization needs to determine whether it is subject to a specific privacy law — that is an attorney-judgment item and is out of scope for this skill.
- The task is to draft data subject rights provisions in a contract or policy — that is a drafting task.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Do not compute, state, or assume any response deadline. Deadlines for data subject requests vary by jurisdiction, regulatory framework, request type, and sometimes the size or nature of the organization. Mark all deadline references as `[CONFIRM: verify response deadline under applicable law with counsel]`.
- Do not determine which privacy law or regulatory framework applies to the requester or the organization. The applicable law is always an attorney-verification item.
- Do not determine whether an exemption applies (e.g., law enforcement exemption, trade secret exemption, third-party privacy exemption). Identify candidate exemptions to flag for attorney review — do not conclude that they apply.
- Do not advise the organization to deny a request without attorney review of the denial basis.
- Do not characterize the requester's legal entitlement. The requester's right to the requested action depends on law and facts that must be assessed by counsel.
- Distinguish clearly: (1) operational steps the organization can take, (2) information that must be gathered, (3) legal determinations that require attorney review.
- Do not place identifying information about the requester into reusable template materials. The handling record for a specific request is a privileged matter record — keep it separate from reusable workflow documentation.
- Use `[CONFIRM: ...]` for every point where the legal consequence, applicable rule, deadline, or exemption is uncertain.
- Flag any request that may involve third-party personal data, law enforcement interests, legal privilege, or trade secrets as requiring immediate attorney consultation before responding.

## Workflow

1. **Log the request.** Record the following at intake: (a) date and time received `[CONFIRM: if ambiguous]`; (b) channel received (email, web form, letter, verbal, etc.); (c) requester's stated identity (name, contact information, account reference if provided); (d) the full text or faithful summary of the request; (e) the type(s) of rights being invoked as best understood from the request. Assign a tracking reference number.

2. **Classify the request type.** Identify which type(s) of data subject rights the request invokes:
   - Access / copy of personal data
   - Deletion / erasure
   - Correction / rectification
   - Portability
   - Restriction of processing
   - Objection to processing
   - Opt-out of sale, sharing, or targeted advertising
   - Withdrawal of consent
   - Other: `[DESCRIBE]`
   
   A single request may invoke multiple rights. If the request is ambiguous, note the ambiguity and flag whether clarification from the requester is appropriate (seek attorney guidance on whether clarifying questions are permitted under applicable law `[CONFIRM]`).

3. **Identify the response deadline placeholder.** Note the date received and insert a placeholder: "Response deadline: `[CONFIRM: verify deadline for [request type] under applicable law and framework — do not compute]`." Do not calculate or estimate the deadline from model knowledge.

4. **Verify the requester's identity.** Assess whether the requester has provided sufficient information to verify their identity before proceeding. Note: (a) what identifying information was provided; (b) whether additional verification is needed; (c) the proposed verification method. Flag for attorney review if: the verification process could be discriminatory, disproportionate, or if applicable law limits what verification can be required `[CONFIRM]`. Do not collect more personal data than necessary to verify identity.

5. **Confirm the organization's role and scope.** Assess whether the organization is acting as a controller with respect to the personal data at issue, or whether it is a processor holding data on behalf of another controller. If processor, flag that the request may need to be forwarded to the controller `[CONFIRM: confirm whether organization must forward request and within what timeframe]`.

6. **Scope the personal data and systems.** Based on the request type and the organization's data inventory (if available), identify the categories of systems, databases, and records likely to hold personal data relating to the requester. Note: (a) categories of data likely held; (b) systems and teams that need to be queried; (c) any data held by third-party processors that may be in scope. Flag: if data inventory is not available, note the gap as a risk item for attorney and privacy team.

7. **Identify candidate exemptions and third-party considerations.** Without concluding that any exemption applies, flag the following for attorney review if relevant:
   - Data relating to third parties whose rights may be affected by disclosure
   - Legally privileged information
   - Trade secrets or confidential business information
   - Data subject to legal hold, litigation, or regulatory preservation
   - Law enforcement or national security considerations
   - Manifestly unfounded or excessive requests `[CONFIRM: criteria and consequences under applicable law]`

8. **Prepare the response plan.** Draft a structured response plan covering: (a) the action to be taken (fulfill, partially fulfill, deny — each denial basis must be attorney-reviewed before use); (b) the data or information to be provided or withheld; (c) the format and delivery method for any data provided; (d) any fee or extension considerations `[CONFIRM: whether fee or extension is permissible under applicable law]`; (e) the draft response communication (stub only — attorney drafts or reviews before sending).

9. **Document the handling record.** Compile the full handling record including: intake log, identity verification record, request classification, system scope, exemptions flagged, response plan, and any communications sent. The handling record should be retained in accordance with the organization's record-retention policy `[CONFIRM: retention period under applicable law]`.

10. **Flag escalation items.** Identify any factors that warrant immediate attorney consultation before proceeding: large-scale or class-type requests, requests from a known litigant or regulator, requests involving sensitive special-category data, requests that implicate third-party rights, or requests where the response deadline appears imminent `[CONFIRM deadline with counsel immediately]`.

11. **Assemble output** and label it as draft legal work product for attorney review.

## Output Format

Deliver the following, in order:

1. **Intake Log** — reference number, date received, channel, requester identification, request text or faithful summary.
2. **Request Classification** — right(s) invoked; ambiguities noted.
3. **Response Deadline Placeholder** — `[CONFIRM: verify deadline under applicable law]` — do not compute.
4. **Identity Verification Record** — what was provided; verification status; any gaps.
5. **Scope Assessment** — systems and data categories identified; third-party processor considerations.
6. **Candidate Exemptions and Third-Party Flags** — list for attorney review; no conclusions drawn.
7. **Response Plan (draft)** — proposed action, data to provide or withhold, format, delivery method, fee/extension flags.
8. **Escalation Items** — any factors requiring immediate attorney consultation.
9. **Attorney Verification Items** — checkbox list of all open legal determinations.
10. **Assumptions** — explicit list of every assumption made in the handling record.

## Attorney Verification Checklist

- [ ] The applicable privacy law(s) and framework(s) have been confirmed, and the organization is subject to them with respect to this requester and this data.
- [ ] The response deadline has been confirmed under current applicable law — it has not been computed from model knowledge.
- [ ] The organization's role (controller or processor) with respect to the data at issue has been confirmed; if processor, the obligation to forward to the controller has been assessed.
- [ ] The identity verification process is proportionate and compliant with applicable law.
- [ ] The scope of personal data to be provided or addressed is complete and accurate — all relevant systems and processors have been queried.
- [ ] Every candidate exemption has been assessed by counsel; no exemption has been applied without attorney review.
- [ ] The interests of third parties whose personal data may appear in the response have been considered.
- [ ] Any denial of the request is based on a confirmed legal basis reviewed by counsel.
- [ ] Any fee charged or extension claimed is permissible under applicable law.
- [ ] The response communication has been reviewed and approved by counsel before being sent.
- [ ] The handling record is complete and will be retained in accordance with applicable law and organizational policy.
- [ ] All `[CONFIRM: ...]` placeholders in the handling record have been resolved before the response is sent.
- [ ] Escalation items, if any, have been escalated and addressed before the response deadline.
