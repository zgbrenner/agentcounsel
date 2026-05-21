---
name: Signature Routing Checklist
description: "Use when a document is believed final and ready to sign — to run a pre-signature completeness checklist, identify signers and signing order, flag blockers, and produce a routing plan for attorney review before the document is sent for execution."
practice_area: legal-ops
task_type: verification
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The document to be signed, uploaded, pasted, or precisely described"
  - "The intended signers: names, titles, and the entity each signer binds"
  - "The required internal approvals and whether they have been obtained"
  - "The signing preferences: sequential or parallel order and any CC recipients"
outputs:
  - "Pre-signature completeness checklist with pass or issues result"
  - "Issues-and-blockers list and entity-name consistency check"
  - "Signing configuration, routing plan, and readiness verdict"
related_skills:
  - skills/legal-ops/legal-meeting-briefing/SKILL.md
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/contracts/redline-summary/SKILL.md
  - skills/corporate/written-consent/SKILL.md
tags:
  - legal-ops
  - signature
  - execution-readiness
  - routing
  - pre-signature-checklist
---

# Signature Routing Checklist

## Purpose

Produce a draft pre-signature readiness review and signing-routing plan for a document that is believed to be in final form. The skill runs a completeness checklist, identifies the signers and the signing order, checks entity names for consistency, flags anything that must be resolved before the document is sent for execution, and assembles a routing plan.

This skill provides workflow discipline and structure. It produces draft work product for attorney review. This is not legal advice. A passing checklist is not authorization to execute; the skill never sends, transmits, or executes a document.

## Use When

- A user says "is this ready to sign?", "set up signing for this contract," or "prepare this for signature."
- A document is believed final and needs a pre-execution completeness check and a routing plan.
- The user is verifying entity names, exhibits, and signature blocks before a document goes out for signature.

## Required Inputs

- **The document to be signed** — uploaded, pasted, or precisely described.
- **The intended signers** — names, titles, the entity each signer binds, and whether each signer is understood to be internally authorized.
- **Required internal approvals** — which approvals the document needs and whether they have been obtained.
- **Signing preferences** — sequential or parallel signing order, and any CC recipients for the executed copy.

If the document is not provided, stop and request it. If signer information is incomplete, ask before producing the routing plan.

## Do Not Use When

- The document is not in final form or has open redlines — resolve those first (use `redline-summary` or `contract-risk-review`).
- The user wants the agent to actually send the document for e-signature — this skill produces a routing plan and a checklist, not an execution action.
- Signing authority is genuinely in question — whether a person or entity can bind is a corporate-authority question; route it to `written-consent` or to counsel.
- The task is to review the document's terms for risk — use `contract-risk-review` or the relevant contract-review skill.

## Legal Safety Rules

- Produce draft work product for attorney review. This is not legal advice. A passing checklist is not authorization to execute; counsel sign-off remains required before a document is sent for signature.
- Check only what is present in the document. Never invent entity names, signature blocks, exhibits, dates, or approvals.
- Do not confirm that a signer is authorized to bind an entity — flag signing authority as a verification item.
- Do not represent the document as "final"; only the responsible attorney or business owner confirms final form.
- Flag every missing exhibit, mismatched entity name, and unobtained approval as a blocker, not as a minor note.
- The skill never sends, transmits, executes, or routes the document to an external party — it produces a plan for a person to act on.
- Distinguish: what the checklist confirms, the blockers it finds, the routing plan, and the verification items.
- Use `[CONFIRM: ...]` placeholders for anything that cannot be resolved from the materials provided.
- Preserve confidentiality.

## Workflow

1. **Accept the document.** Take the document in whatever form it is provided and confirm what it is — the document type and the parties.

2. **Run the pre-signature checklist.** Check each item and record the result:
   - The document appears to be in final, agreed form with no open redlines.
   - All exhibits, schedules, and attachments referenced in the document are present.
   - The legal entity names on the signature blocks are correct and complete.
   - Dates are correct, or left blank for the execution date as intended.
   - The signature blocks match the intended authorized signers.
   - Any required internal approvals have been obtained.
   - The document has been reviewed by the appropriate counsel.

3. **Identify issues and blockers.** From the checklist, list every item that did not pass. Mark as a blocker anything that must be resolved before the document can be sent: a missing exhibit, a mismatched or incomplete entity name, an unobtained approval, an unresolved redline.

4. **Configure signing.** Identify the signers, the signing order (sequential or parallel), any internal approval step that must precede counterparty signature, and the CC recipients for the executed copy.

5. **Check entity-name consistency.** Compare the entity names in the signature blocks against the names used in the document's preamble and defined terms. Flag any inconsistency — the most common signing error.

6. **Produce the routing plan.** Lay out the signing sequence step by step. If no e-signature tool is in use, produce manual signing instructions and the full signer contact list instead.

7. **Determine overall readiness.** State a verdict: **READY TO ROUTE** (the checklist passes and no blockers remain) or **ISSUES TO RESOLVE FIRST** (one or more blockers remain).

8. **List next steps and verification items.** Note what happens after routing, the expected turnaround, the follow-up point if the document is not signed, and the items an attorney must verify.

9. **Assemble the output** and label it a draft.

## Output Format

Deliver the following sections in order:

**DRAFT SIGNATURE READINESS REVIEW — FOR ATTORNEY REVIEW**

1. **Document Details** — document type, parties, and length or scope.

2. **Pre-Signature Checklist** — each checklist item with its result (pass / issue), and an overall **PASS** or **ISSUES FOUND**.

3. **Issues and Blockers** — every item that did not pass, with each blocker marked as such.

4. **Signing Configuration** — table: order, signer, role and the entity bound, contact, internal-approval dependency.

5. **Entity-Name Consistency Check** — whether the signature-block entity names match the document's preamble and defined terms, with any inconsistency flagged.

6. **Routing Plan** — the step-by-step signing sequence, or manual signing instructions if no e-signature tool is in use.

7. **Readiness Verdict** — **READY TO ROUTE** or **ISSUES TO RESOLVE FIRST**, with a one-line rationale.

8. **Next Steps** — what to expect after routing, turnaround, and the follow-up point.

9. **Attorney Verification Items** — see the Attorney Verification Checklist below.

## Attorney Verification Checklist

- [ ] The document is confirmed to be in final, agreed form with no open redlines.
- [ ] All exhibits, schedules, and attachments referenced in the document are present and correct.
- [ ] The legal entity names on every signature block are correct, complete, and consistent with the document's preamble and defined terms.
- [ ] Each signer is authorized to bind the entity for which they are signing.
- [ ] All required internal approvals have been obtained and documented.
- [ ] The document has had the appropriate counsel review before being sent for signature.
- [ ] The signing order and any internal-approval dependency are correct for this transaction.
- [ ] The CC list for the executed copy is correct and complete.
- [ ] A **READY TO ROUTE** verdict has counsel sign-off before the document is sent for signature.
- [ ] A plan to file the executed copy in the appropriate system after execution is in place.
