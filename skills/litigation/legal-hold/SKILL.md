---
name: Legal Hold
description: "Use when preparing a litigation hold notice and preservation-scope summary — issuing a new hold, refreshing an existing one, or releasing a closed one — as draft legal work product for attorney review before distribution to custodians."
practice_area: litigation
task_type: drafting
jurisdictions: []
risk_level: critical
requires_attorney_review: true
inputs:
  - "The matter and the attorney-confirmed preservation trigger date"
  - "The preservation scope"
  - "The custodians and data systems involved"
outputs:
  - "Draft litigation hold notice and preservation-scope summary for attorney review"
related_skills:
  - skills/litigation/litigation-chronology/SKILL.md
  - skills/litigation/matter-intake/SKILL.md
tags:
  - litigation
  - legal-hold
  - preservation
  - ediscovery
  - spoliation
---

# Legal Hold

## Purpose

Produce a structured draft litigation hold notice and preservation-scope summary for attorney review. The skill supports three modes: **issue** (a new hold), **refresh** (update scope, custodians, or date range on an existing hold), and **release** (lift a hold when the matter closes). It organizes the preservation scope, identifies custodians and the systems they use, flags departed custodians whose data requires system-level preservation, and drafts a notice that communicates clearly to recipients what they must preserve, how, and why. It does not decide whether a duty to preserve has been triggered — that is a legal determination the attorney must make before this skill is used. The draft notice must not be distributed to custodians without attorney review and approval.

## Use When

- An attorney has determined that a duty to preserve has been triggered and needs a first-draft hold notice to send to custodians.
- A prior hold must be refreshed because the scope has changed, additional custodians have been identified, the date range has expanded, or new systems are in scope.
- A matter has closed and counsel needs a draft hold-release notice confirming that preservation obligations have lifted.
- The attorney wants a preservation-scope summary alongside the notice to document what was covered and why.

## Required Inputs

**For all modes:**

- **Matter identification** — name, number, or brief description sufficient to identify the matter.
- **Trigger event** — the event that prompted the hold (e.g., receipt of a complaint, a threat of litigation, a regulatory inquiry). The attorney must have already determined that this event triggers a preservation duty; this skill does not make that determination.
- **Preservation scope** — the categories of documents, communications, and data to be preserved (e.g., contracts, correspondence, financial records, project files, metadata).
- **Named custodians** — the individuals who may possess responsive information, with their roles or titles. Identify any departed custodians separately.
- **Date range** — the start date and end date (or "ongoing") for responsive material. The attorney must supply these dates; this skill does not compute or assert a trigger date.
- **Systems in scope** — the platforms, applications, and devices from which material must be preserved (e.g., email, chat and messaging tools, file-share and cloud-storage platforms, devices, CRM systems, legacy or archival systems, voicemail).
- **Effective date of the hold** — the date on which the preservation obligation begins. Provided by the attorney; do not compute.

**Additional inputs for Refresh mode:**

- The prior hold notice (or a reference to it) and the date it was issued.
- A description of what has changed: new custodians, expanded scope, updated date range, new systems, or other amendments.

**Additional inputs for Release mode:**

- Confirmation from the attorney that the matter is closed and the preservation duty has lifted.
- Confirmation that no related matter, appeal, cross-claim, or insurance recovery is still live that could independently sustain the preservation obligation.
- The date the release is effective.

If matter identification, trigger event, custodian list, or preservation scope is not provided, stop and request the missing information. Do not draft a hold notice without knowing what is being preserved, from whom, and why. Do not fabricate custodian names, systems, or scope categories.

## Do Not Use When

- The attorney has not yet determined whether a duty to preserve has been triggered. Deciding whether and when the duty arose is a legal determination outside the scope of this skill; the attorney must resolve it before using this skill.
- The attorney needs to determine the trigger date for the preservation duty. This skill accepts a trigger date as an input; it does not calculate one.
- The matter involves spoliation that has already occurred and the attorney needs to assess remediation options or disclosure obligations — that is a separate remediation workflow.
- The user needs a litigation chronology to identify potentially responsive events and date ranges (use `litigation-chronology` to build the chronology first, then return to this skill with dates confirmed by the attorney).
- The user needs to draft a discovery response, a request for production, or a privilege log — those are separate skills.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- The hold notice must not be distributed to any custodian without attorney review, revision, and sign-off. Premature distribution — or distribution of an unreviewed notice — can waive privilege, create obligations the attorney has not intended, or lead to inconsistent preservation efforts.
- Do not decide whether a duty to preserve has been triggered, when it was triggered, or what the governing standard is. The existence and timing of the preservation duty vary by jurisdiction, the nature of the matter, and the procedural posture — treat all such determinations as `[verify jurisdiction]` until the attorney confirms them.
- Do not compute, assert, or assume any preservation trigger date or hold effective date. Use only attorney-supplied dates and mark any date the attorney has not confirmed with `[deadline verification required]`.
- Scope is an attorney judgment call. An over-broad scope creates disproportionate burden and cost; an under-broad scope risks losing evidence and, in the worst case, sanctions. Flag scope questions explicitly rather than resolving them silently.
- Departed custodians require special attention. Their data cannot be preserved through a personal-acknowledgment workflow alone; system-level preservation must be arranged with IT or a records custodian. Flag every departed custodian with `[ACTION: attorney to arrange system-level preservation with IT for departed custodian — personal acknowledgment is insufficient]`.
- For Release mode, confirm — and flag for attorney confirmation — that no related matter, appeal, cross-claim, or insurance recovery is live that could independently sustain the obligation. Releasing a hold prematurely can trigger the same consequences as failing to issue one.
- Do not invent legal authority. The duty to preserve, the consequences of non-preservation (including potential sanctions), and the legal standards that govern scope all vary by jurisdiction and forum — treat all such references as `[verify jurisdiction]` and `[citation needed]` unless the attorney has supplied specific authority for inclusion.
- Distinguish what the attorney has confirmed from what has been assumed. Every assumption must be flagged with `[CONFIRM: ...]` or `[ATTORNEY TO CONFIRM: ...]`.
- Preserve confidentiality and privilege. The hold notice is an internal communication. Keep client-sensitive facts out of reusable copies of the template.

## Workflow

1. **Confirm the mode.** Determine whether the request is to issue a new hold, refresh an existing hold, or release a closed hold. If the mode is ambiguous, ask before proceeding.

2. **Confirm inputs.** Verify that all required inputs for the selected mode have been provided. If matter identification, trigger event, custodian list, or preservation scope is missing, stop and request it. Do not proceed on assumed information.

3. **Conflicts and privilege check.** Note that before issuing any hold notice, the attorney should have confirmed that the representation is cleared, conflicts have been checked, and the attorney-client relationship with the client is established. Flag as `[ATTORNEY TO CONFIRM: conflicts cleared and representation authorized]` if not confirmed.

4. **Note the jurisdiction-specific preservation standard.** The duty to preserve and the consequences of non-preservation vary by jurisdiction and forum. Record: "The governing preservation standard for this matter is `[verify jurisdiction]` — attorney to confirm." Do not state a jurisdiction-specific rule.

5. **Scope the preservation.** Using the provided inputs, set out:
   - The document and data categories to be preserved.
   - The systems in scope.
   - The date range (attorney-supplied; do not compute).
   - Any categories or systems the attorney has affirmatively excluded from scope, with a note that exclusions are the attorney's judgment.
   Flag any scope gaps or ambiguities identified during drafting as `[CONFIRM: attorney to evaluate whether [category/system] is within scope]`.

6. **Review the custodian list.** For each named custodian:
   - Record their name and role.
   - Identify whether they are a current employee or a **departed custodian**.
   - For every departed custodian, insert: `[ACTION: attorney to arrange system-level preservation with IT for [name] — departed custodian; personal acknowledgment is insufficient]`.
   - Note any custodians the attorney should consider adding based on the scope, flagged as `[CONFIRM: attorney to evaluate whether [role/name] should be added as a custodian]`.

7. **Draft the hold notice.** Populate `templates/legal-hold-notice.md` for the selected mode:
   - **Issue:** Complete all sections of the template. Use the attorney-supplied effective date. Retain every `[CONFIRM]` placeholder. The notice must include the "LEGAL HOLD — PRESERVE DOCUMENTS AND COMMUNICATIONS" heading, the reason the recipient is receiving it, what to preserve, the date range, systems in scope, explicit dos and don'ts, and an acknowledgment section.
   - **Refresh:** Begin with a clear "AMENDED LEGAL HOLD — UPDATE TO PRIOR NOTICE DATED [date]" heading. State what has changed and confirm that unchanged obligations from the prior notice remain in effect. Retain all `[CONFIRM]` placeholders.
   - **Release:** Begin with "LEGAL HOLD RELEASE — [MATTER NAME]." Confirm the matter is closed and state the effective release date. Include the attorney-required confirmation that no related matter, appeal, or other obligation independently sustains the preservation duty. Retain all `[CONFIRM]` placeholders.

8. **Compile the preservation-scope summary.** Separately from the notice, produce a brief internal summary documenting:
   - The matter and trigger event.
   - The custodians covered and the mode of preservation for each (personal acknowledgment; IT/system-level for departed custodians).
   - The document and data categories in scope.
   - The systems in scope.
   - The date range.
   - Any scope exclusions and the basis for them.
   - Any open scope questions flagged for the attorney.
   Label this summary "Privileged & Confidential — Attorney Work Product."

9. **Compile the attorney verification checklist.** Assemble all `[CONFIRM]`, `[ACTION]`, and `[ATTORNEY TO CONFIRM]` items into the checklist at the end of the output. These are the items that must be resolved before the notice is distributed.

10. **Label the output.** Mark the hold notice and preservation-scope summary as drafts for attorney review. Ensure the hold notice itself carries the "DRAFT FOR ATTORNEY REVIEW — DO NOT DISTRIBUTE UNREVIEWED" banner until the attorney has reviewed and authorized it.

## Output Format

Deliver:

1. **Draft Hold Notice** — populated from `templates/legal-hold-notice.md`, with all `[CONFIRM]`, `[ACTION]`, and `[ATTORNEY TO CONFIRM]` placeholders retained. Labeled "DRAFT FOR ATTORNEY REVIEW — DO NOT DISTRIBUTE UNREVIEWED."
2. **Preservation-Scope Summary** — internal work product: the matter, trigger event, custodians, scope categories, systems, date range, exclusions, and open scope questions. Labeled "Privileged & Confidential — Attorney Work Product."
3. **Departed-Custodian Flag** — if any departed custodians were identified, a separate callout listing each one and the required IT/system-level preservation action. Labeled "Privileged & Confidential — Attorney Work Product."
4. **Attorney Verification Checklist** — all items from the draft requiring attorney review before the notice is distributed, consolidated in one place.

## Attorney Verification Checklist

- [ ] Attorney has determined that a duty to preserve has been triggered and has authorized issuance of this hold.
- [ ] The trigger event and trigger date have been confirmed by the attorney; no date in this notice was computed by the drafting agent.
- [ ] Conflicts check completed and the representation is authorized.
- [ ] The governing preservation standard for this jurisdiction and forum has been confirmed by the attorney — `[verify jurisdiction]`.
- [ ] The custodian list is complete; no relevant custodian has been omitted.
- [ ] For every departed custodian identified, system-level preservation has been arranged with IT or a records custodian.
- [ ] Preservation scope — document categories, data types, and systems — reviewed and approved as appropriate in breadth (neither over-broad nor under-broad).
- [ ] Date range reviewed and confirmed by attorney; start date reflects the attorney-determined trigger date.
- [ ] Systems in scope are complete and accurate for this matter.
- [ ] Any scope exclusions have been reviewed and affirmatively authorized by the attorney.
- [ ] For Refresh: the prior hold is accurately identified and described; the notice clearly states what has changed.
- [ ] For Release: the attorney has confirmed the matter is closed and that no related matter, appeal, cross-claim, or insurance recovery independently sustains the preservation obligation; the release effective date is confirmed.
- [ ] The hold notice language is clear and plain enough that a non-lawyer custodian can understand what they must do.
- [ ] The acknowledgment section is complete and the attorney has determined how acknowledgments will be collected and tracked.
- [ ] No jurisdiction-specific legal authority has been asserted in the notice without attorney verification — `[verify jurisdiction]`.
- [ ] The notice carries the "DRAFT FOR ATTORNEY REVIEW — DO NOT DISTRIBUTE UNREVIEWED" banner and has been reviewed and authorized before any distribution to custodians.
- [ ] All `[CONFIRM]`, `[ACTION]`, and `[ATTORNEY TO CONFIRM]` placeholders resolved before distribution.
