> Shared reference material supporting the AgentCounsel Insurance skills, used to help produce draft legal work product for attorney review — not legal advice.

# Insurance Red-Flag Catalog

This catalog lists patterns in policies, tenders, reservations of rights, certificates, claim files, and insurer/insured correspondence that a reviewer should actively scan for. Each entry describes the pattern, why it matters, what to check, and which role is most exposed. The catalog is organized by document family so a review skill can run a Red Flags Quick Scan against the family relevant to the document in front of it, then fold every pattern found into that skill's own issue table using the table shapes defined in `skills/insurance/references/output-patterns.md`.

This catalog is a review aid. It identifies what to look for and why. It never decides coverage, a duty to defend or indemnify, the validity or timeliness of a tender or a reservation, additional insured status, allocation or priority among policies, whether bad faith occurred or did not occur, a claim's value, or a reserve. Whether a flagged pattern actually matters depends on the policy language, the claim facts, the parties' roles, the claim stage, and the governing jurisdiction — all attorney judgment calls. Every flagged item is a candidate for attorney verification, never a legal conclusion.

Three disciplines are non-negotiable and appear throughout the entries:

- **Never state what the law requires.** Notice-prejudice rules, bad-faith standards, the contra proferentem rule, and every other coverage-interpretation doctrine are intensely jurisdiction-specific. Flag every such point `[verify jurisdiction]`.
- **Never compute a figure or a deadline.** Limits, retentions, deductibles, premiums, and every date are recorded as the document states them, and dates are flagged `[deadline verification required]`. This catalog never tests a covenant, calculates a proration, or reconstructs a timeline beyond what is written.
- **Never rate anything "market standard."** A comparison to market practice (a limit, a sublimit, a retention, an endorsement package) is never asserted here; where a skill's workflow calls for that comparison, it is flagged `[ATTORNEY TO CONFIRM: market context]`.

---

## How to Use This Catalog

For each topic section relevant to the document under review:

1. Locate the relevant provision, letter passage, certificate field, or claim-file entry (or note its absence — a missing item is itself a red flag in several sections below).
2. Check the pattern description against the actual language or fact, quoting operative terms verbatim rather than paraphrasing.
3. If the pattern is present, add the item to the relevant issue table (coverage issue matrix, ROR review table, tender checklist, COI comparison table, bad-faith risk matrix, recovery tracker, renewal checklist, or communications table) with a source citation.
4. Note which role (insurer, insured, additional insured, claimant, broker) is most exposed, and whether the user's stated role matches the exposure profile.
5. Flag every finding for attorney review; never resolve ambiguity, decide coverage, or compute a figure or date.

The sections are grouped by document family:

- **Policy architecture** — Sections 1–2 (used by `insurance-policy-summary`, `coverage-issue-spotter`, `coverage-position-outline`).
- **Defense and reservation** — Section 3 (used by `reservation-of-rights-review`, `coverage-issue-spotter`).
- **Additional insured and evidence of coverage** — Section 4 (used by `certificate-of-insurance-review`, `insurance-requirements-contract-review`, `tender-letter-review`).
- **Tender and notice** — Section 5 (used by `tender-letter-review`).
- **Allocation and limits** — Section 6 (used by `coverage-issue-spotter`, `coverage-position-outline`).
- **Claim handling** — Section 7 (used by `bad-faith-risk-triage`, `claims-chronology-builder`).
- **Recovery** — Section 8 (used by `subrogation-recovery-tracker`).
- **Renewal and placement** — Section 9 (used by `policy-renewal-placement-diligence-checklist`).
- **Communications** — Section 10 (used by `insurer-insured-communications-review`).
- **Cross-cutting** — Section 11 (jurisdiction-specific standards, every skill).

Where a section carries a **Direction for counsel** line, it frames a preferred and a fallback direction the reviewing attorney may weigh in a transactional or negotiation context (contract insurance requirements, renewal placement) — a direction of change, never drafted language, a coverage position, or a decision.

---

## 1. Coverage Architecture Red Flags

### 1.1 Insuring-agreement trigger mismatch

**Pattern:** The claim fact pattern is checked against the insuring agreement's trigger language (e.g., "bodily injury," "property damage," "wrongful act," "personal and advertising injury," "loss") and the trigger is unclear, contested, or appears not to match on its face.

**Why it matters:** Whether a claim falls within an insuring agreement's grant is the threshold coverage question; a mismatch — real or apparent — shapes every downstream issue (exclusions, defense obligations, reservation posture). The question is whether the claim fact and the trigger language line up, not whether coverage exists.

**What to check:**
- Quote the insuring agreement's trigger language verbatim and the claim fact asserted to satisfy it.
- Is the trigger contested by the insurer, the insured, or unaddressed in the correspondence to date?
- Does more than one insuring agreement or coverage part arguably apply to the same claim?

**Most exposed:** Insured whose claim sits at the edge of the grant; insurer assessing whether a duty to investigate has even arisen.

---

### 1.2 Occurrence vs. claims-made trigger and multi-year exposure

**Pattern:** The policy is occurrence-based, claims-made, or claims-made-and-reported, and the claim facts implicate conduct, injury, or discovery spanning more than one policy period, an expired extended reporting period, or a retroactive date issue.

**Why it matters:** The trigger-of-coverage theory (manifestation, exposure, continuous trigger, or the claims-made "claim first made" and "reported" mechanics) determines which policy year — or years — respond, and a retroactive date or an expired tail can eliminate coverage entirely. The question is which policy period(s) are implicated on the facts as stated, never which theory prevails.

**What to check:**
- Record the policy type (occurrence vs. claims-made/claims-made-and-reported) and the retroactive date, if any, as written.
- Record every candidate trigger date (occurrence, injury, discovery, claim-first-made, claim-reported) as the documents state it; flag each `[deadline verification required]`.
- Is an extended reporting period ("tail") in play, and is its own reporting deadline recorded and flagged?
- Are prior or subsequent policy years potentially implicated, and have those insurers been identified?

**Most exposed:** Insured facing a coverage gap between policy years; insurer assessing which of several towers responds.

---

### 1.3 Notice and reporting condition gaps

**Pattern:** The policy conditions coverage on notice "as soon as practicable," "immediately," or within a stated period, and the claim facts show a gap between the triggering event and the notice actually given, or notice was given to the wrong party or in the wrong form.

**Why it matters:** A late-notice or defective-notice question is one of the most commonly disputed coverage conditions, and its effect (forfeiture, notice-prejudice analysis, or no effect at all) is governed entirely by jurisdiction-specific law. The question here is only whether a notice gap exists on the facts — never whether it excuses coverage.

**What to check:**
- Quote the notice condition's exact language and record the notice deadline as written; flag `[deadline verification required]`.
- Record the date of the triggering event and the date notice was actually given, both as stated in the documents; do not compute the interval.
- Was notice given to the address, person, or method the policy specifies?
- Is a notice-prejudice rule, a claims-made "notice within the policy period" condition, or a statutory reporting requirement potentially in play? `[verify jurisdiction]`

**Most exposed:** Insured whose notice may be found late or defective; insurer relying on the notice condition as a coverage defense.

---

## 2. Exclusions, Endorsements & Definitions Red Flags

### 2.1 Exclusion asserted without a matched claim fact

**Pattern:** Correspondence, a policy summary, or a coverage position cites an exclusion without identifying the specific claim fact that triggers it, or applies an exclusion's language more broadly than its own terms support.

**Why it matters:** An exclusion only removes coverage to the extent its own terms are met by the facts; citing an exclusion in the abstract, without the matching fact, leaves the analysis incomplete and can overstate (or understate) the exclusion's reach. The question is whether the specific fact needed to trigger the exclusion is present and sourced.

**What to check:**
- Quote the exclusion's operative language verbatim.
- Identify the specific claim fact asserted to trigger it, with its source; if none is identified, flag the gap.
- Does an exception-to-the-exclusion (a "carve-back") potentially restore coverage on the same facts?
- Is more than one exclusion asserted for the same claim fact, and are they consistent with each other?

**Most exposed:** Insured facing a coverage denial built on an unsupported exclusion; insurer whose position may rest on an incomplete match.

---

### 2.2 Endorsement conflicts with the base form

**Pattern:** A policy endorsement adds, deletes, or modifies base-form language, and the endorsement's effect on the base form is unclear, or two endorsements appear to conflict with each other.

**Why it matters:** Endorsements are drafted to amend the base form, and a poorly integrated endorsement (one that does not clearly state what it replaces or how it interacts with other endorsements) creates real interpretive ambiguity. The question is what the endorsement changed and whether that change is internally consistent with the rest of the policy — not how a court would resolve the ambiguity.

**What to check:**
- Quote each relevant endorsement's stated effect (adds/deletes/modifies) and the base-form section it amends.
- Do two or more endorsements address the same base-form provision with different or conflicting effect?
- Is the endorsement's effective date consistent with the claim date?

**Most exposed:** Either party relying on the endorsement's stated effect; broker whose placement instructions may not match what was actually issued.

---

### 2.3 Definitions that narrow or expand coverage unexpectedly

**Pattern:** A defined term ("insured," "occurrence," "property damage," "wrongful act," "claim," "loss," "your work," "products-completed operations") is defined more narrowly or more broadly than its plain meaning, and the claim facts turn on which meaning applies.

**Why it matters:** Coverage disputes frequently turn on a definition rather than an exclusion; a narrow definition of "insured" or "occurrence" can remove coverage as effectively as an exclusion would. The question is what the defined term actually says, quoted in full, against the claim fact — never how the definition should be construed.

**What to check:**
- Quote every definition the coverage analysis depends on, in full.
- Does the claim fact fall inside or outside the defined term on its face, or is it genuinely ambiguous?
- Are related but differently defined terms (e.g., "insured" vs. "additional insured") being conflated in the correspondence or analysis?

**Most exposed:** Insured or additional insured whose status depends on a defined term; insurer applying a definition to deny or limit coverage.

---

## 3. Duty to Defend/Indemnify & Reservation-of-Rights Red Flags

### 3.1 Vague or boilerplate reservation of rights

**Pattern:** A reservation-of-rights letter cites policy provisions in the abstract (a full list of exclusions and conditions "without limitation") without connecting each cited provision to a specific claim fact, or reserves rights on grounds the letter never actually explains.

**Why it matters:** A reservation's function is to put the insured on notice of the specific bases on which coverage might not apply; a boilerplate reservation that lists provisions without tying them to facts gives the insured little to respond to and can itself become a point of dispute. The question is whether each reserved ground is matched to a stated fact and a stated provision — never whether the reservation is legally sufficient or effective.

**What to check:**
- For each reserved ground, is there a quoted policy provision, a stated claim fact, and an explanation connecting them?
- Are any reserved grounds asserted without any supporting fact identified in the letter or the claim file?
- Does the letter reserve the right to withdraw the defense, seek reimbursement of defense costs, or both — and on what stated conditions?

**Most exposed:** Insured trying to understand what is actually being reserved; insurer whose vague reservation may itself be examined.

---

### 3.2 Unsupported factual assertions in the letter

**Pattern:** A reservation-of-rights letter, a denial letter, or coverage correspondence states a fact about the claim (what happened, what was known, what was disclosed) that does not appear to be supported by the claim file or the pleadings provided.

**Why it matters:** A coverage position built on an unsupported fact is vulnerable on the facts alone, independent of the legal analysis; identifying the gap between what the letter asserts and what the file actually shows is a threshold task before any legal question is reached. The question is only whether the asserted fact is sourced — never whether the position is correct.

**What to check:**
- For each factual assertion in the letter, is there a document in the file that supports it? Cite it, or flag `not found`.
- Are any assertions inconsistent with the pleadings, the tender, or the claimant's own account?
- Does the letter's factual narrative match the chronology built from the underlying documents?

**Most exposed:** Either party relying on the letter's factual accuracy; the party whose position depends on the unsupported fact.

---

### 3.3 Independent-counsel and conflict-of-interest flags

**Pattern:** The insurer has reserved rights on a ground that could create a conflict between the insurer's and the insured's interests in the defense (e.g., a coverage question that turns on the same facts the defense must prove or disprove), and the letter is silent on independent counsel, or asserts a right to control the defense without addressing the conflict.

**Why it matters:** Certain reservations create a recognized potential for a defense-counsel conflict; whether an actual conflict exists, and what it entitles the insured to (independent counsel, a Cumis-type arrangement, or otherwise), is governed by jurisdiction-specific law and case-specific facts. The question here is only to flag the pattern for attorney assessment — never to conclude a conflict exists or what remedy follows.

**What to check:**
- Does the reserved ground turn on a fact that defense counsel would also need to prove or disprove in the underlying action?
- Does the letter address who selects and controls defense counsel, and on what terms?
- Has the insured raised (or should the insured be advised to raise) an independent-counsel request? Flag for attorney assessment, not conclusion. `[verify jurisdiction]`

**Most exposed:** Insured whose defense may be conflicted; insurer whose control of the defense may be challenged.

---

### 3.4 Reimbursement-of-defense-costs reservation without a clear basis

**Pattern:** The insurer reserves a right to seek reimbursement of defense costs paid under a reservation, without identifying the specific coverage basis for reimbursement or without the insured's advance agreement where that is otherwise required.

**Why it matters:** The availability of a reimbursement right — and whether it requires the insured's consent, a court order, or is available at all — is sharply jurisdiction-dependent, and asserting it without a stated basis can overstate the insurer's position. The question is whether the letter states a basis, not whether the right exists.

**What to check:**
- Does the letter identify the specific policy provision or legal basis for a reimbursement right?
- Is the insured's agreement (express or implied) to the reservation of a reimbursement right documented anywhere in the file?
- Flag the reimbursement question for attorney assessment. `[verify jurisdiction]`

**Most exposed:** Insured facing a later demand for repayment of defense costs; insurer whose reimbursement right may be unsupported.

---

## 4. Additional Insured & Certificate-of-Insurance Red Flags

### 4.1 Certificate-of-insurance-to-endorsement mismatch

**Pattern:** A certificate of insurance lists additional insured status, specific coverages, or limits that do not match the actual endorsement forms attached (or not attached) to the policy.

**Why it matters:** A certificate is evidence only of what it states, not proof of coverage — most certificates say so on their face — and a mismatch between the certificate and the actual policy/endorsement can mean the additional insured status the certificate purports to show was never actually granted. The question is whether the certificate and the endorsement match, never whether additional insured status exists.

**What to check:**
- Compare each certificate field (named insured, additional insured, coverage type, limits, endorsement forms referenced) against the actual endorsement, side by side.
- Is the additional insured endorsement referenced by form number on the certificate the same form actually attached to the policy?
- Are the limits shown on the certificate the policy limits, or a certificate-holder-requested subset?

**Most exposed:** Party relying on the certificate as evidence of additional insured status (contractor, landlord, lender); insurer whose actual coverage may not match what the certificate represents.

---

### 4.2 Box checked, endorsement not attached

**Pattern:** The certificate checks a box or states that the certificate holder is an additional insured, a waiver of subrogation applies, or coverage is primary and non-contributory, but no corresponding endorsement is attached to or referenced against the actual policy.

**Why it matters:** A checked box on a certificate, standing alone, typically does not itself confer any status or right under the policy — the endorsement is what does that. This is one of the most consequential and most common gaps in additional insured practice, and it is entirely factual to identify. The question is only whether the endorsement exists and is attached — never whether the certificate has independent legal effect.

**What to check:**
- For every box checked or statement made on the certificate, is there a corresponding endorsement form actually provided?
- If no endorsement is provided, record the gap explicitly as `not found` rather than assuming one exists.
- Does the certificate itself carry a disclaimer that it confers no rights on the certificate holder? Quote it.

**Most exposed:** Certificate holder relying on the checked box; upstream party (contractor, owner) whose risk-transfer expectation may not be met.

---

### 4.3 Additional insured endorsement scope narrower than the contract requires

**Pattern:** The underlying contract requires broad additional insured status (e.g., for "ongoing and completed operations," "sole negligence," or a specific scope of work), and the endorsement actually issued is narrower (e.g., ongoing operations only, or limited to the additional insured's vicarious liability).

**Why it matters:** A gap between what the contract requires and what the endorsement actually grants can leave the additional insured without the coverage it bargained for, discoverable only by lining up the contract's insurance clause against the endorsement's actual scope. The question is the scope match, never whether the endorsement is legally sufficient.

**What to check:**
- Quote the contract's insurance-requirement clause and the endorsement's actual scope language side by side.
- Does the endorsement cover completed operations if the contract requires it, and for how long?
- Is the endorsement limited to the additional insured's vicarious liability, when the contract calls for broader status?
- Route the underlying contract review to `skills/insurance/insurance-requirements-contract-review/SKILL.md`.

**Most exposed:** Additional insured whose actual coverage is narrower than negotiated; named insured facing an indemnity claim the endorsement does not fully offset.

**Direction for counsel:** Preferred (additional insured/upstream party) — an endorsement matching the contract's full stated scope, including completed operations where required. Fallback — a narrower endorsement with the gap flagged for a contractual indemnity backstop. Adequacy and enforceability are for the attorney `[ATTORNEY TO CONFIRM: market context]`.

---

## 5. Tender & Notice Completeness Red Flags

### 5.1 Tender missing a required element

**Pattern:** A tender or notice letter omits an element the policy, the contract, or ordinary tender practice would call for — the specific claim identification, the asserted coverage basis, the underlying contract reference, supporting documents, or a clear statement of what is being requested (defense, indemnity, or both).

**Why it matters:** An incomplete tender can slow or complicate the insurer's response and can itself become a point of dispute about what was actually tendered and when. The question is whether each element is present, source-cited, or missing — never whether the tender, as made, is legally sufficient or timely.

**What to check:**
- Work through the tender-completeness elements (recipient, asserted basis, claim identification, duties tendered, additional insured basis if asserted, supporting documents) and mark each present/not found/ambiguous.
- Is the underlying contract's insurance/indemnity clause attached or otherwise identified as the basis for the tender?
- Is the tender addressed to the correct party (the named insured's carrier, the additional insured's own carrier, or both), as identified in the documents?

**Most exposed:** Party tendering, whose incomplete tender may be met with a request for more information rather than a response; recipient assessing what is actually being asked.

---

### 5.2 Tender timing gap without a stated explanation

**Pattern:** The claim file shows a gap between the triggering event (the underlying claim, suit, or demand) and the date the tender was actually made, with no explanation in the file for the interval.

**Why it matters:** Timing is frequently disputed in tender and additional-insured practice, and identifying the gap — and whether the file offers any explanation — is a factual predicate to any timeliness analysis. The question is only whether a gap exists on the dates as written; timeliness itself is never concluded here.

**What to check:**
- Record the triggering-event date and the tender date exactly as the documents state them; flag both `[deadline verification required]`. Do not compute the interval.
- Does the file offer any explanation for the interval (e.g., delayed discovery of the claim, delayed identification of a responsible carrier)?
- Was tender made to more than one potentially responsible carrier, and on what dates?

**Most exposed:** Party tendering, if timeliness is later disputed; insurer assessing whether prejudice is even a live question. `[verify jurisdiction]`

---

### 5.3 Response gap or non-response to a completed tender

**Pattern:** A tender that appears complete on its face has received no substantive response, an acknowledgment only, or a response that does not address acceptance, denial, or a reservation of rights.

**Why it matters:** A non-response or an ambiguous response leaves the tendering party without a clear posture to act on, and the pattern itself — not any legal conclusion about its effect — is what the tracker should surface. The question is whether a substantive response exists in the file, never what a non-response legally means.

**What to check:**
- Is there a substantive response in the file (acceptance, denial, or reservation), and on what date? `[deadline verification required]`
- If only an acknowledgment exists, does it commit to a response date?
- Does the file show any follow-up correspondence chasing a response?

**Most exposed:** Party awaiting a response, whose own deadlines (a responsive pleading, a settlement decision) may be running regardless.

---

## 6. Allocation, Other-Insurance & Limits/SIR Red Flags

### 6.1 Multiple policies or towers potentially implicated

**Pattern:** More than one policy (different insurers, different policy years, primary and excess, or multiple lines) appears potentially triggered by the same claim, and the file does not identify how — or whether — allocation among them has been addressed.

**Why it matters:** Allocation methodology (pro rata by time on the risk, "all sums," horizontal or vertical exhaustion) varies sharply by jurisdiction and policy language, and identifying that multiple policies are in play is the necessary first step before any allocation question can even be framed for counsel. The question is which policies are potentially implicated — never how they should be allocated.

**What to check:**
- List every policy, insurer, and policy period potentially implicated by the claim facts, with source.
- Does an "other insurance" clause in any of the implicated policies address priority, and what does it say verbatim?
- Is excess or umbrella coverage potentially triggered, and has the underlying limit been confirmed as exhausted, partially exhausted, or not exhausted? `[ATTORNEY TO CONFIRM]`

**Most exposed:** Insured with a multi-year or multi-policy exposure; insurers whose relative shares are undetermined.

---

### 6.2 "Other insurance" and non-cumulation clause conflicts

**Pattern:** Two or more potentially applicable policies each contain an "other insurance," excess, or non-cumulation clause, and the clauses conflict (each purporting to be excess to the other, or each purporting to limit its own liability by reference to the other).

**Why it matters:** Conflicting other-insurance clauses are a well-recognized coverage dispute category, and how the conflict is resolved is jurisdiction-specific and policy-specific. The question is to quote and compare the clauses, not to resolve the conflict.

**What to check:**
- Quote each "other insurance," excess, or non-cumulation clause verbatim, with its source.
- Do the clauses conflict, and is the conflict a "true conflict" (each policy claims to be excess to the other) on its face?
- Route the priority question for attorney resolution rather than assuming an order. `[verify jurisdiction]`

**Most exposed:** Insurers whose relative payment obligations are unresolved; insured awaiting payment while priority is disputed.

---

### 6.3 Limits, sublimits, and SIR/deductible erosion questions

**Pattern:** The claim facts raise a question about whether a sublimit (rather than the policy's full limit) applies, whether a self-insured retention or deductible has been satisfied, or whether prior payments have eroded the limit available for this claim.

**Why it matters:** Whether a sublimit applies, and how much of a limit or SIR remains, drives what the claim can recover — but the figures are recorded, never calculated, here. The question is what the policy states and what the claim file shows about payments to date, not the remaining balance.

**What to check:**
- Record each potentially applicable limit and sublimit exactly as the policy states it, with source.
- Record the SIR/deductible amount and any stated erosion or exhaustion mechanics as written; do not compute remaining balance.
- Record prior payments under the same limit as the claim file states them, with source, flagging any gap in the payment record.

**Most exposed:** Insured whose recovery may be capped by a sublimit; insurer tracking limit exposure across related claims.

---

## 7. Claim-Handling & Bad-Faith Risk Themes

> Every item in this section is framed neutrally, as a pattern that warrants closer attorney review — never as an accusation that claim handling was improper, nor as an exoneration that it was reasonable. Bad-faith standards (what conduct breaches the duty of good faith, what damages are available, and what showing is required) are entirely jurisdiction-specific and are never stated here. See `skills/insurance/bad-faith-risk-triage/SKILL.md`.

### 7.1 Investigation gaps

**Pattern:** The claim file shows periods of inactivity, requested information that was never obtained or followed up on, or an investigative step (an examination under oath, an inspection, an expert retention) that the file describes as planned but never shows as completed.

**Why it matters:** A gap in the investigation is a fact about the file, not a conclusion about reasonableness; surfacing it lets counsel assess, against the jurisdiction's own standard, whether the gap is material. The question is only whether the gap exists and what the file shows.

**What to check:**
- Build the chronology of investigative steps taken and identify any stated step not shown as completed.
- Is there a period of unexplained inactivity in the file, and how long does the file show it lasting? `[deadline verification required]` for any stated deadline; do not compute elapsed time as a conclusion.
- Was information the insured or claimant provided ever acknowledged or acted on in the file?

**Most exposed:** Insured or claimant awaiting a decision; insurer whose file may show a documentation gap regardless of actual practice.

---

### 7.2 Inconsistent or shifting explanations

**Pattern:** The insurer's stated basis for a coverage position, a reservation, or a denial changes across correspondence in the file, without an explanation for the change tied to new facts.

**Why it matters:** A shift in stated rationale is a documented fact pattern that counsel would want to examine; it is not, by itself, evidence of any improper motive, and may reflect legitimate new information. The framing here is strictly neutral — the theme is worth examining, not a conclusion.

**What to check:**
- Line up each letter's stated basis side by side, with dates and sources.
- Does a later letter cite a different basis than an earlier one, and does the file show new facts that would explain the change?
- Is the change consistent with the claim's procedural posture (e.g., new facts from discovery), or unexplained?

**Most exposed:** Insured trying to understand the insurer's actual position; insurer whose file should show the basis for any change.

---

### 7.3 Communication and response-time patterns

**Pattern:** The chronology shows response times to insured or claimant correspondence that are markedly longer at some points than others, or requests for extensions with no substantive update provided.

**Why it matters:** Response-time patterns are claim-handling facts a bad-faith attorney will want organized; whether any particular delay reflects a standard the jurisdiction recognizes as reasonable is entirely an attorney and jurisdiction-specific question. The output is the pattern, not a verdict on it.

**What to check:**
- Build a response-time table from the correspondence dates in the file (request date, response date), sourced to each document.
- Are extension requests accompanied by a stated reason and a new target date?
- Is the pattern consistent across the file, or concentrated around a particular event (e.g., near a coverage decision)?

**Most exposed:** Insured or claimant awaiting responses; insurer whose file documentation of reasons for delay may be thin.

---

### 7.4 Reserve or valuation activity referenced without explanation

**Pattern:** Adjuster notes or a claim diary reference reserve changes or a valuation without the file showing the factual basis for the change.

**Why it matters:** This catalog and the skills it supports never estimate, opine on, or use reserve figures as a coverage or value benchmark; the pattern to flag is only whether the file's own documentation ties a reserve or valuation change to a stated fact. The reserve amount itself is never recorded, restated, or relied upon in any output.

**What to check:**
- Note that a reserve or valuation entry exists in the file, without restating the figure in any work product.
- Does the file tie the change to a specific new fact, document, or event?
- Flag any apparent gap in documentation as a neutral observation, never as a conclusion about claim value or reserve adequacy.

**Most exposed:** Neither party specifically; this is a file-documentation observation for counsel's own claim-handling assessment.

---

## 8. Subrogation & Recovery Red Flags

### 8.1 Evidence-preservation gaps

**Pattern:** The loss facts point to a potential third-party recovery (a product, a contractor's work, a vendor's negligence), and the file does not show that physical evidence, the failed item, or scene photographs were preserved before repair, replacement, or disposal.

**Why it matters:** A recovery theory (subrogation, contribution, reimbursement, indemnity) can be undermined or lost entirely if the evidence needed to prove it is not preserved early, often before counsel is even retained. The question is whether preservation happened and is documented — never whether a recovery right exists.

**What to check:**
- Identify the physical evidence, documents, or data the recovery theory would need, and whether the file shows it was preserved, and when. `[deadline verification required]` for any preservation or spoliation-risk deadline.
- Was the responsible party, its insurer, or a subrogation vendor put on notice, and when?
- Is repair, replacement, or disposal of the damaged property imminent or already completed?

**Most exposed:** Party with the potential recovery right, if evidence is lost before it is secured.

---

### 8.2 Contractual waiver of subrogation

**Pattern:** A contract between the insured and the potentially responsible party contains a waiver of subrogation, an indemnity clause, or a limitation-of-liability clause that may bar or limit the very recovery theory being pursued.

**Why it matters:** A waiver of subrogation in the underlying contract can foreclose a recovery the insurer would otherwise have, and it is discoverable only by reading the contract between the insured and the responsible party — not just the policy. The question is whether such a clause exists and what it says, never whether it is enforceable.

**What to check:**
- Obtain and review every contract between the insured and the potentially responsible party for a waiver-of-subrogation, indemnity, or limitation clause; quote it verbatim.
- Does the policy itself contain a "waiver of subrogation permitted" or "blanket waiver" endorsement, and does it match the contract's waiver?
- Route deep contract review to `skills/insurance/insurance-requirements-contract-review/SKILL.md` where the underlying contract's insurance and indemnity provisions require full analysis.

**Most exposed:** Insurer whose recovery may be barred; insured who agreed to the waiver, potentially without appreciating its effect.

---

### 8.3 Statute-of-limitations and notice-of-claim deadlines for the recovery action

**Pattern:** The recovery theory depends on a limitations period or a pre-suit notice requirement (e.g., a notice-of-claim statute against a governmental entity, a statutory repose period) that the file has not identified or confirmed.

**Why it matters:** A recovery right can be time-barred well before the underlying claim is resolved, and identifying the applicable deadline is squarely an attorney task this catalog never performs. The question is whether the deadline has been identified and flagged for counsel — the deadline itself is never computed or supplied.

**What to check:**
- Record every date relevant to a potential limitations or notice-of-claim period exactly as the documents or the user state it; flag `[deadline verification required]`.
- Is the potentially responsible party a governmental entity or public agency, raising a shorter notice period? Flag for attorney confirmation. `[verify jurisdiction]`
- Route the deadline determination itself to counsel; never state or estimate the period.

**Most exposed:** Party with the recovery right, if the deadline is missed before counsel is engaged.

---

## 9. Renewal/Placement Diligence Red Flags

### 9.1 Material change not reflected in the expiring program

**Pattern:** The insured's operations, revenue, locations, workforce, or risk profile have changed materially since the expiring policy was placed, and the renewal submission materials do not reflect the change.

**Why it matters:** An outdated submission can lead to a program that does not match current exposures, or to a misrepresentation question on the application itself. The question is whether the change is reflected in what will be submitted for renewal — never whether current coverage is adequate or whether a misrepresentation occurred.

**What to check:**
- List material changes since the expiring program was placed (new operations, new jurisdictions, acquisitions, revenue changes, new products) as stated by the user.
- Does the renewal submission draft reflect each change, or is a gap identified?
- Are any changes ones a carrier would consider material to underwriting, warranting a mid-term disclosure rather than waiting for renewal? Flag for attorney and broker assessment.

**Most exposed:** Insured facing a coverage or rescission dispute if a material change is not disclosed; broker responsible for the submission's accuracy.

---

### 9.2 Claims history and loss-run gaps

**Pattern:** The loss runs provided are incomplete (missing years, missing a line of coverage, or showing claims without final status), or a known claim or incident is not reflected in the loss runs at all.

**Why it matters:** Complete and accurate loss history underlies both underwriting and the insured's own understanding of its risk; gaps can affect pricing, terms, or the completeness of the diligence record. The question is whether the loss runs are complete against what is otherwise known — never whether a particular claim will affect terms.

**What to check:**
- Compare the loss runs provided against the claims history known from other sources (claim files, litigation records, prior renewal submissions).
- Is any line of coverage, policy year, or claim status missing from the loss runs?
- Are open claims shown with a current reserve or status, and is that status consistent with what the claim file otherwise shows?

**Most exposed:** Insured whose renewal terms may be affected by an incomplete record; broker compiling the submission.

---

### 9.3 Contractual coverage obligations not reflected in the placement

**Pattern:** Contracts requiring specific insurance (limits, additional insured status, waivers of subrogation, primary-and-non-contributory language) are in force, and the renewal or new placement does not appear to address whether the program will satisfy them.

**Why it matters:** A gap between what contracts require and what the program actually provides can leave the insured in breach of its own contractual insurance obligations even while "insured." The question is whether the contractual requirements have been inventoried and checked against the placement — never whether the requirements themselves are enforceable.

**What to check:**
- Inventory the contracts that impose insurance requirements on the insured, with their requirements as written.
- Does the renewal/placement submission address each requirement (limits, AI status, waiver of subrogation, primary-and-non-contributory), or is the check not yet done?
- Route detailed contract-by-contract review to `skills/insurance/insurance-requirements-contract-review/SKILL.md`.

**Most exposed:** Insured facing a contractual breach if the program falls short; counterparties relying on the insured's coverage.

**Direction for counsel:** Preferred — a placement checklist that confirms every contractual requirement is addressed before binding. Fallback — a flagged gap list for the broker to price and negotiate. Placement and carrier decisions remain the client's and broker's `[ATTORNEY TO CONFIRM: market context]`.

---

## 10. Insurer/Insured Communication Red Flags

### 10.1 Tone or posture inconsistent with the stated coverage position

**Pattern:** A draft communication's tone (accusatory, dismissive, or conclusory) is inconsistent with the coverage position actually reserved or stated elsewhere in the file — for example, a reservation letter that hedges on coverage but a follow-up email that assumes a denial.

**Why it matters:** Inconsistent tone across communications from the same file can create confusion about the insurer's actual position and can itself become an issue in a later dispute. The question is whether the draft is internally consistent with the file's own stated position — never whether the position is correct.

**What to check:**
- Compare the draft's tone and assumed posture against the most recent formal coverage position in the file.
- Does the draft state a conclusion (coverage exists, coverage does not exist, bad faith occurred) that has not actually been reached in the file?
- Flag any apparent overstatement or understatement of the current posture.

**Most exposed:** Both parties, if the communication creates confusion about the actual coverage position.

---

### 10.2 Privileged or work-product content in a communication intended for the other side

**Pattern:** A draft communication intended for the insured, the claimant, or opposing counsel contains language, an attachment, or a forwarded thread that appears to include privileged legal analysis or attorney work product not intended for that recipient.

**Why it matters:** Sending privileged content to the wrong recipient can waive privilege; this is a discipline this catalog and every skill treats as a hard flag, never a judgment call left unaddressed. The question is only whether the draft, as written, contains such content — never a privilege-law conclusion.

**What to check:**
- Review the draft and any attachments or forwarded threads for internal legal analysis, coverage counsel's mental impressions, or reserve/valuation information not intended for the recipient.
- Is a forwarded email chain trimmed to remove earlier privileged content before it goes out?
- Flag any such content for removal before the communication is finalized; never approve the communication for sending.

**Most exposed:** The party whose privilege could be waived by the disclosure.

---

### 10.3 Information request without a stated purpose or deadline

**Pattern:** A communication requests information, documents, or an examination under oath from the insured or claimant without stating why the information is needed or by when a response is expected.

**Why it matters:** An unclear request can slow the claim and create ambiguity about what is actually being asked; a clear request with a stated purpose and target date serves both parties. The question is completeness of the request, not whether the underlying demand is proper.

**What to check:**
- Does the draft state what is being requested, why, and a target response date (flagged `[deadline verification required]`, never computed)?
- Is the request consistent with the policy's cooperation or examination-under-oath conditions, as quoted?
- Does the draft reference a deadline elsewhere in the file that this request should align with?

**Most exposed:** Recipient trying to understand what is expected; sender whose unclear request may draw a delayed or incomplete response.

---

## 11. Cross-Cutting Jurisdiction-Specific Standards

### 11.1 Any coverage, notice, or bad-faith standard question

**Pattern:** Any document or analysis in this catalog's scope depends on a rule of law — a notice-prejudice rule, a contra proferentem or reasonable-expectations doctrine, a bad-faith standard (first-party or third-party), a statutory unfair claims practices act, an examination-under-oath enforcement rule, or a subrogation/anti-subrogation rule.

**Why it matters:** Insurance law is heavily state-specific (and, for surplus lines and certain lines, can vary by regulatory regime), and a rule that governs in one jurisdiction may not apply, or may apply differently, in another. This catalog never supplies the rule — it flags where local law governs so counsel can verify it.

**What to check:**
- Identify each point in the analysis where the outcome depends on a jurisdiction-specific legal standard, and flag it `[verify jurisdiction]`.
- Note where the policy's choice-of-law provision, the insured's domicile, the risk location, and the forum differ, since more than one may be argued to govern.
- Never state the substantive rule, the standard, or the deadline that jurisdiction supplies; route it to the attorney.

**Most exposed:** Any party relying on a legal standard whose content is jurisdiction-dependent.

---

## Reviewer Notes

- A red flag is a prompt to look closely and route to attorney attention — not a conclusion that coverage exists or does not, that a tender or reservation is valid or timely, that additional insured status exists, that bad faith occurred or did not occur, or that a recovery right exists.
- Whether a flagged item matters depends on the policy language, the claim facts, the party's role, the claim stage, and the governing jurisdiction — all for the attorney to assess.
- This catalog never rates a limit, retention, or endorsement package as "market standard" without `[ATTORNEY TO CONFIRM: market context]`, never computes a figure or a deadline, and never supplies jurisdiction-specific insurance law.
- Claim-handling and bad-faith themes (Section 7) are always framed neutrally — a pattern worth examining, never an accusation and never an exoneration.
- This catalog is not exhaustive. Unusual or claim-specific patterns not listed here may still warrant a flag in the relevant skill's issue table using the table shapes in `skills/insurance/references/output-patterns.md`.
- See `skills/insurance/coverage-issue-spotter/SKILL.md`, `skills/insurance/reservation-of-rights-review/SKILL.md`, `skills/insurance/tender-letter-review/SKILL.md`, `skills/insurance/certificate-of-insurance-review/SKILL.md`, `skills/insurance/bad-faith-risk-triage/SKILL.md`, `skills/insurance/subrogation-recovery-tracker/SKILL.md`, `skills/insurance/policy-renewal-placement-diligence-checklist/SKILL.md`, `skills/insurance/insurer-insured-communications-review/SKILL.md`, `skills/insurance/insurance-requirements-contract-review/SKILL.md`, and `skills/insurance/coverage-position-outline/SKILL.md` for the full review workflows this catalog supports.
