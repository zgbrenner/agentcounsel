# Example: Red-Team Verifier

> **Illustrative example — not legal advice.** This is a sample of what the Red-Team Verifier skill (`skills/legal-methodology/red-team-verifier/SKILL.md`) produces. Every party, date, and finding in it is **fictional** and was invented for illustration. It is the kind of draft work product a supervising attorney would review — not a finished deliverable, and not legal advice. See `examples/README.md`.

## Scenario

A junior associate used an AI tool to prepare a draft demand letter on behalf of a client, Oakfield Catering Co., addressed to Summit Event Rentals LLC. The draft asserts that Summit breached a written equipment-rental agreement by delivering damaged refrigeration units for a wedding event, and demands payment of lost profits and consequential damages. Before the letter is sent to the opposing party, the supervising attorney asked for an adversarial quality-control pass on the draft.

The draft has several planted weaknesses. It cites a case for the proposition that consequential damages are recoverable, but the cited authority cannot be traced to any provided source. It states as established fact that Summit "knew the units were defective," though the underlying file contains no support for knowledge. It demands payment within a stated number of days and references a limitations period without flagging either for verification. It does not identify the governing jurisdiction or which state's law applies to the contract. And its closing paragraph uses directive, threatening language that overstates the strength of the claim. The verification findings report below is what the Red-Team Verifier skill produces from that draft.

## Illustrative Output

---

**Verification Findings Report**

**Draft legal work product for attorney review. Not legal advice.**

Draft under review: Demand letter from Oakfield Catering Co. to Summit Event Rentals LLC re: alleged breach of equipment-rental agreement
Stated purpose / recipient: Pre-litigation demand to be sent to the opposing party
Date of verification: March 14, 2026
Verified by: Red-Team Verifier (AgentCounsel)

### 1. Executive Risk Summary

**Verdict: REVISE**

Findings: 3 Critical, 3 Material, 2 Minor.

This draft is **not ready for attorney review to be treated as a final pass, and is not ready to send.** It contains a case citation that could not be verified against any provided or independently confirmed source, which means an attorney could not safely rely on the legal proposition it supports. The draft also asserts a contested fact — the opposing party's knowledge of the defect — as if established, which materially affects the strength of the consequential-damages demand. The governing jurisdiction and choice of law are never identified, and a payment deadline and a limitations period are stated without being flagged for verification. The closing language reads as a directive threat rather than as counsel's analysis. Each of these is correctable, but the draft must be revised and re-verified before it is relied upon or sent.

### 2. Major Problems

Ordered by severity. A reviewing attorney should read this section first.

**C-1 — Critical — Source-support audit.** Closing of the damages paragraph. The draft cites an authority for the proposition that consequential damages, including lost profits, are recoverable for breach of an equipment-rental contract. The citation could not be traced to any user-provided document or independently verified source. *Why it matters:* relying on or sending a letter that cites an authority that may not exist, or may not stand for the stated proposition, exposes the client and the firm to serious credibility and professional-responsibility risk.

**C-2 — Critical — Factual claim audit.** Paragraph describing the delivery. The draft states that Summit "knew the units were defective at the time of delivery." Nothing in the provided file supports a finding of knowledge; the file establishes only that the units were later found to be non-functional. *Why it matters:* knowledge or notice is often what separates a routine breach claim from a consequential-damages claim. Asserting it without support overstates the claim and could be contradicted by the opposing party.

**C-3 — Critical — Jurisdiction and timing audit.** Throughout. The draft never identifies the governing jurisdiction or which state's law applies to the rental agreement, yet it makes jurisdiction-specific assertions about damages recoverability and limitations. *Why it matters:* the availability and measure of consequential damages, and the applicable limitations period, vary by jurisdiction; the entire damages theory rests on an unconfirmed premise.

**M-1 — Material — Jurisdiction and timing audit.** Demand paragraph and limitations reference. The draft states a specific payment deadline ("within 14 days") and references a limitations period for the claim. Neither is flagged for verification, and the draft appears to have computed or assumed both. *Why it matters:* an incorrectly stated deadline or limitations period can mislead the client about urgency and waive or appear to waive rights.

**M-2 — Material — Legal-reasoning audit.** Liability paragraph. The draft states the conclusion that Summit breached the agreement but does not state the governing standard for breach, identify the specific contractual obligation allegedly violated, or apply the contract terms to the facts. The analysis is conclusory. *Why it matters:* a demand that does not connect the contract language to the facts is weaker on its merits and easier for the opposing party to rebut.

**M-3 — Material — Professional-responsibility audit.** Closing paragraph. The closing uses directive, threatening language stating that Summit "must pay immediately or face certain liability" and that the claim "will succeed." This overstates certainty on a claim whose damages theory and governing law are unconfirmed, and it presents the analysis as a foregone conclusion. *Why it matters:* overstated threats can undermine the client's negotiating position and raise professional-responsibility concerns about candor and reasonable basis.

### 3. Unsupported Claims Table

| # | Claim (as stated) | Location | Support state | Recommended action |
|---|-------------------|----------|---------------|--------------------|
| 1 | Consequential damages, including lost profits, are recoverable for this breach | Damages paragraph | unsupported — cites an authority with no verifiable source | Mark `[UNVERIFIED — must be confirmed before reliance]`; attorney to confirm the authority exists and supports the proposition, or remove |
| 2 | Summit knew the units were defective at the time of delivery | Delivery paragraph | unsupported — no source in the file | Remove the knowledge assertion, or replace with what the record supports; flag for attorney |
| 3 | Summit breached the equipment-rental agreement | Liability paragraph | needs citation — no contract section identified, no standard stated | Identify the specific contract provision and the breach standard; attorney to confirm |
| 4 | Oakfield's lost profits total a stated dollar figure | Damages paragraph | needs citation — no source for the calculation | Tie the figure to a client-provided document or invoice; flag the basis |
| 5 | The claim is within the applicable limitations period | Limitations reference | unsupported — no jurisdiction confirmed, period appears assumed | Mark `[deadline verification required]`; attorney to confirm jurisdiction and period |

### 4. Missing Facts

- **Whether Summit received notice of the defect, and when.** If Summit was notified and failed to cure, the breach and damages theory is materially stronger; if no notice was given, a cure-opportunity defense may apply.
- **The governing jurisdiction and choice-of-law provision of the rental agreement.** A different answer changes the damages rules, the limitations period, and possibly the notice requirements.
- **Whether the contract contains a damages-limitation or consequential-damages waiver clause.** If it does, the central demand may be barred regardless of the merits.
- **The basis and documentation for the lost-profits figure.** Without a documented calculation, the demand amount is unsupported and may be challenged.
- **Whether Oakfield mitigated by sourcing replacement equipment.** A failure to mitigate could reduce or eliminate recoverable damages.

### 5. Jurisdiction and Deadline Flags

No date or period below is asserted as correct. Each is flagged for attorney verification.

- **Governing jurisdiction — not stated.** `[verify jurisdiction]` The draft makes jurisdiction-specific damages and limitations assertions without identifying the jurisdiction.
- **Choice of law — not stated.** `[CONFIRM: which state's law governs the rental agreement]`
- **Payment deadline — "within 14 days."** `[deadline verification required]` The draft appears to have set this period; attorney to confirm the intended demand window.
- **Limitations period — referenced but not specified or sourced.** `[deadline verification required]` Attorney to confirm the applicable limitations period for the confirmed jurisdiction and claim type.
- **Time-sensitive legal statement — damages recoverability.** The recoverability of consequential damages should be confirmed as of a stated date against current law in the confirmed jurisdiction.

### 6. Suggested Revisions

Directions for the drafter or attorney. Where a revision requires legal judgment, that is noted.

**Critical**
- Locate and verify the authority cited for consequential damages, or remove the citation and the proposition until a verified source is found. *Requires attorney legal judgment.*
- Remove the assertion that Summit "knew" the units were defective, or replace it with a statement the record supports.
- Identify the governing jurisdiction and choice of law before any jurisdiction-specific assertion is made. *Requires attorney legal judgment.*

**Material**
- Add `[deadline verification required]` markers to the payment deadline and the limitations reference; have the attorney confirm both rather than asserting them.
- Strengthen the liability paragraph by identifying the specific contract provision allegedly breached and applying its terms to the facts. *Requires attorney legal judgment.*
- Revise the closing paragraph to remove the directive threat and the overstated certainty; reframe it as a demand supported by counsel's analysis, not a guarantee of outcome.

**Minor**
- Add the draft label and an attorney verification checklist to the document.
- Separate the factual recitation from the legal conclusions, which are currently blended in the liability paragraph.

### 7. Attorney Verification Checklist

- [ ] All Critical findings (C-1, C-2, C-3) reviewed and resolved, or consciously accepted with documented rationale.
- [ ] All Material findings (M-1, M-2, M-3) reviewed; any accepted without correction documented.
- [ ] The consequential-damages authority independently confirmed to exist and to support the stated proposition, or removed.
- [ ] Every claim in the Unsupported Claims Table given a verified citation or source, or removed.
- [ ] The knowledge assertion confirmed against the record or removed.
- [ ] Governing jurisdiction and choice of law resolved; no jurisdiction-specific analysis relies on an unconfirmed jurisdiction.
- [ ] The payment deadline and limitations period attorney-verified; no date computed by the agent relied upon.
- [ ] Missing facts (notice, choice of law, damages-limitation clause, lost-profits basis, mitigation) obtained or their absence consciously accepted.
- [ ] The liability reasoning checked: contract provision identified, breach standard stated, terms applied to facts.
- [ ] The closing language reviewed; no passage overstates certainty or reads as a guarantee of outcome.
- [ ] Fact, authority, analysis, and demand layers visibly separated in the revised draft.
- [ ] The revised draft carries the required draft label and an attorney verification checklist.
- [ ] Attorney review completed before the letter is sent.

### Scope and Limitations

This report checks the draft demand letter for defects in support, reasoning structure, framing, and completeness. It does not verify that any cited authority says what is claimed, that the damages theory is legally correct, that the demand strategy is sound, or that the letter is complete for its legal purpose. Those remain attorney functions. A REVISE verdict means the draft did not survive this adversarial pass; attorney review is required regardless of any verdict.

---
