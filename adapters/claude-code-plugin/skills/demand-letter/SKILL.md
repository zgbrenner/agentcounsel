---
name: Demand Letter
description: Use when drafting a demand letter (outline and draft text) for attorney review, with the factual background, claimed basis, specific demand, damages figures, and response deadline all flagged for attorney confirmation before sending.
---

# Demand Letter

## Purpose

Produce a structured draft demand letter — outline and draft text — for attorney review, revision, and sending. The skill organizes the factual narrative, identifies the claimed basis for relief, articulates a specific demand, and flags every legal conclusion, damages figure, response deadline, and consequence of non-response as items requiring attorney confirmation before the letter is finalized. The draft is not a final negotiating position and must not be sent without attorney review and approval.

## Use When

- A user asks to "draft a demand letter," "write a demand," or "send a letter before filing suit."
- Counsel wants a structured first draft before editing and sending a pre-litigation demand.
- A client has suffered a harm and counsel needs to frame and communicate a pre-suit demand.
- A breach of contract, tort claim, employment dispute, property damage, or similar matter requires a formal written demand as a precursor to litigation or negotiation.
- A statutory or contractual pre-suit notice requirement must be met (attorney must confirm applicability and form).

## Required Inputs

- The client's identity and role (the party making the demand).
- The recipient's identity and, if known, address and counsel information.
- A description of the dispute, the alleged harm, and the factual background (from documents or a client summary).
- The nature of the claim or legal theory to be asserted (e.g., breach of contract, negligence, fraud) — attorney will confirm.
- The relief or remedy being demanded (e.g., payment of a specific amount, return of property, specific performance).

If the client identity, recipient identity, or nature of the demand is not provided, stop and request it. Do not draft a demand letter without knowing who is demanding what from whom.

## Do Not Use When

- The user wants to file a complaint or pleading rather than a pre-litigation demand (use a pleading drafting skill instead).
- The matter requires a statutory notice of claim with specific form requirements (attorney must confirm applicability; this skill produces a general demand draft only).
- A settlement agreement is needed rather than a demand (use a settlement drafting skill).
- The user needs a chronology of events to support the demand (use `litigation-chronology` first, then return to this skill).
- The user needs to respond to a demand letter received from an opposing party (use a demand response skill).

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- The draft demand letter must not be sent to any party without attorney review, revision, and authorization.
- Do not assert legal conclusions as established facts (e.g., do not state "you breached the contract" as a fact — state "we contend" or "it is our position that" and flag for attorney to confirm the framing).
- Do not invent, fabricate, or assume damages figures. Use only client-supplied or document-supported figures. Mark all damages as `[CONFIRM: attorney to verify calculation and supporting evidence]`.
- Do not assert a response deadline without attorney instruction. Use `[CONFIRM: attorney to specify response deadline]` — never compute or assert a deadline independently.
- Do not assert legal authority (statutes, regulations, case law) without attorney direction. If legal authority is included, mark it as `[CONFIRM: attorney to verify citation and current law]`.
- Do not assert consequences of non-response (e.g., "we will file suit") without attorney authorization — use `[CONFIRM: attorney to confirm and authorize]`.
- Where a statutory pre-suit notice requirement may apply, flag it explicitly as `[ACTION: attorney must confirm whether statutory notice requirements apply and whether this letter satisfies them]`.
- Clearly distinguish facts (from documents or client) from contentions and from attorney judgment calls.
- Preserve confidentiality and privilege: the draft and outline are attorney work product. Do not circulate outside the legal team without authorization.

## Workflow

1. **Confirm inputs.** Verify that the client identity, recipient identity, nature of the claim, and the relief sought have been provided. If any of these are missing, stop and request them before proceeding.

2. **Identify the parties.** Record the sending party (client) with full legal name and, if applicable, entity type. Record the recipient with full legal name, address, and counsel if known. Note any aliases or related entities.

3. **Identify the legal theory.** Identify the claim(s) or legal theory asserted: breach of contract, negligence, fraud, employment discrimination, property damage, etc. Label these as "claimed basis" and mark for attorney confirmation. Note any contractual or statutory provision that is the basis for the demand if provided.

4. **Organize the factual background.** Using provided documents or client summary, organize the relevant facts in chronological order: the relationship of the parties, the relevant agreement or obligation if any, the events giving rise to the claim, and the harm suffered. Label the factual background as "based on information provided" and identify the sources.

5. **Identify and quantify the harm.** List the specific harms or damages claimed: monetary damages, consequential damages, attorneys' fees if applicable, non-monetary relief. Use only client-supplied or document-supported figures. Mark each figure as `[CONFIRM: attorney to verify]`. If damages are not yet quantifiable, note that they will be provided or calculated at a later stage.

6. **Identify the specific demand.** State the specific relief demanded: payment of a sum certain `[CONFIRM]`, return of property, specific performance of a contractual obligation, cessation of a course of conduct, or other. The demand must be specific.

7. **Identify the response deadline.** Do not compute or assert a deadline. Insert `[CONFIRM: attorney to specify the response deadline and confirm it is reasonable and consistent with any applicable rule or agreement]`.

8. **Identify consequences of non-response.** Draft a placeholder for consequences (e.g., further legal action) but mark as `[CONFIRM: attorney to authorize specific language regarding consequences]`. Do not threaten specific legal action without attorney direction.

9. **Check for privilege or settlement communication designation.** Note that some demand letters are designated as privileged settlement communications (Federal Rule of Evidence 408 or state equivalent). Flag this as `[ACTION: attorney to confirm whether to include a settlement privilege designation and whether it is appropriate in this jurisdiction]`.

10. **Draft the letter using the outline template.** Populate the template at `templates/demand-letter-outline.md`. Every section that requires an attorney determination must retain its `[CONFIRM]` or `[ACTION]` placeholder in the draft.

11. **Compile the attorney verification checklist.** List all items requiring attorney confirmation before the letter is sent.

12. **Label the output.** Mark the draft as "DRAFT — Attorney Work Product — For Attorney Review Only — Do Not Send Without Authorization."

## Output Format

Deliver:

1. **Draft Demand Letter** — A full draft of the letter, populated using the template at `templates/demand-letter-outline.md`, with all `[CONFIRM]` and `[ACTION]` placeholders retained where attorney input is required.
2. **Drafting Notes** — A brief separate section explaining the choices made in the draft, flagging areas of uncertainty, and listing alternative formulations for attorney consideration.
3. **Attorney Verification Checklist** — All items requiring attorney review before the letter is finalized and sent.

## Attorney Verification Checklist

- [ ] Client identity, authority to make the demand, and engagement scope confirmed.
- [ ] Recipient identity and address verified; letter will reach the correct party.
- [ ] Legal theory and claimed basis reviewed and confirmed by attorney.
- [ ] All factual statements verified against the documentary record; no misstatements of fact.
- [ ] All quotations from documents are accurate and in context.
- [ ] Damages figures verified and supported by evidence; calculation confirmed.
- [ ] Response deadline confirmed as reasonable and consistent with any applicable rule, contract, or statute.
- [ ] Whether a statutory pre-suit notice requirement applies — and whether this letter satisfies it — confirmed by attorney.
- [ ] Consequences of non-response language reviewed and authorized by attorney.
- [ ] Settlement privilege / FRE 408 designation decision made by attorney.
- [ ] Tone and framing reviewed: no misstatements of fact or law presented as established conclusions.
- [ ] Letter authorized for sending by the responsible attorney of record.
- [ ] Proof of delivery method confirmed (certified mail, email with read receipt, hand delivery, etc.).
