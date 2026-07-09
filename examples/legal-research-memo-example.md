# Example: Legal Research Memo

> **Illustrative example — not legal advice.** This is a sample of what the Legal Research Memo skill (`skills/legal-research/legal-research-memo/SKILL.md`) produces. Every party, fact, and date in it is **fictional**. **Critically, this memo contains no real legal authority.** Every case, statute, and rule referenced is a visible placeholder — `[Attorney to insert controlling authority]` — or an obviously fictional stand-in such as *Doe v. Roe*, `[citation to verify]`. **None is a real citation, and none should be read as stating what any law provides.** The example exists to demonstrate the IRAC discipline and the source-flagging, not to report research. It is draft work product a supervising attorney would review — not legal advice. See `examples/README.md`.

## Scenario

Summit Outfitters, LLC is a fictional retailer that ordered store fixtures from Granite Supply Co., another fictional company, under a written purchase order. Summit says the fixtures were defective and wants to sue for breach of contract, but the alleged breach happened a while ago, and the matter partner asked for a first-pass research memo on one discrete question before deciding whether to send a demand letter: **is the contract claim time-barred?** No authorities were provided with the request, and the governing jurisdiction has not been confirmed. This is exactly the situation the skill is built for — and this example shows the skill refusing to invent the one thing that would answer the question (the limitations period and accrual rule), flagging it as unverified authority, and declining to compute any deadline. The memo demonstrates the IRAC structure and the strict separation of facts, assumptions, law, analysis, and open items, with every authority marked for attorney insertion.

## Illustrative Output

> Draft legal work product for attorney review. Not legal advice. **No authority in this memo has been verified; every citation is a placeholder for attorney insertion.** No deadline has been computed.

---

**PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT**

| | |
|---|---|
| **To:** | Supervising Attorney / Matter Team |
| **From:** | Drafting agent (AgentCounsel workflow) |
| **Date:** | `[CONFIRM: date of memo]` |
| **Re:** | Whether Summit's breach-of-contract claim against Granite is time-barred |
| **Matter:** | Summit Outfitters, LLC — potential claim re Purchase Order SG-2210 (no matter number assigned) |
| **Jurisdiction:** | `[CONFIRM: jurisdiction and governing law — not provided; the analysis below cannot be completed without it]` |
| **Relevant Date:** | Alleged breach on or about `[CONFIRM: breach date]`; no complaint filed as of `[CONFIRM: as-of date]` |

---

## Question(s) Presented

1. Under the contract-claims limitations law of `[CONFIRM: jurisdiction]`, is Summit's breach-of-contract claim against Granite time-barred, where the alleged breach occurred on or about `[CONFIRM: breach date]` and no complaint has been filed as of `[CONFIRM: as-of date]`?

*(Sub-issues addressed under Question 1: (1a) the governing limitations period and accrual point; (1b) whether any tolling, discovery-rule, or contractual modification of the period applies.)*

---

## Brief Answer(s)

1. **Uncertain — the question cannot be answered without verified authority.** The answer turns entirely on two things not verified in this session: the limitations period for written-contract claims in the governing jurisdiction, and the rule for when such a claim accrues. Neither the jurisdiction nor any controlling authority has been provided, so no conclusion can be drawn and **no deadline has been computed.** `[CONFIRM: jurisdiction, limitations period, and accrual rule — attorney must supply and verify.]`

---

## Facts

*User-provided facts only. Nothing has been added or inferred without a label.*

- Summit Outfitters, LLC and Granite Supply Co. entered a written purchase order (PO SG-2210) for store fixtures.
- Summit alleges the delivered fixtures were defective.
- The alleged breach occurred on or about `[CONFIRM: breach date]`.
- No complaint has been filed as of `[CONFIRM: as-of date]`.
- **Inference (labeled): none drawn.** The date Summit *discovered* the alleged defect is not in the record and may differ from the breach date. `[CONFIRM: discovery date — legally material if a discovery rule applies.]`
- **`[CONFIRM: factual gap]`** — the full PO text has not been provided; it may contain a clause shortening or lengthening the limitations period. Legally material; obtain before relying on this memo.

---

## Assumptions

- **Assumption 1:** The claim sounds in breach of a written contract, not in tort or under a sale-of-goods regime; the applicable limitations period and accrual rule may differ across those characterizations. `[CONFIRM: claim characterization — attorney to determine, as it may change the governing period.]`
- **Assumption 2:** The relevant triggering event for accrual is the alleged breach date stated above; whether accrual instead runs from discovery, from a demand, or from another event is unverified. `[CONFIRM.]`
- **Assumption 3:** No amendment to any governing limitations statute has been enacted that would change the period between the breach date and today; the attorney must confirm the current version. `[Verify current law.]`
- **Assumption 4:** No prior tolling agreement, standstill, or filing exists between the parties. `[CONFIRM.]`

---

## Discussion / Analysis

*IRAC per sub-issue. **Every "Rule" below is an unfilled placeholder** — no authority has been verified in this session. The structure shows where verified law must go; it does not supply it.*

---

### Issue 1a: What limitations period governs the claim, and when did it accrue?

**Rule**

`[CONFIRM: rule — no verified authority available for this proposition in this session; attorney must supply and verify before relying on this analysis.]`

- The limitations period for a written-contract claim is set by statute in the governing jurisdiction. `[Attorney to insert controlling limitations statute — identify section and confirm current version — verify jurisdiction.]`
- The point at which such a claim accrues (when the period begins to run) is fixed by statute or case law in the governing jurisdiction. `[Attorney to insert controlling authority.]` *Illustrative placeholder only, not a real case:* the accrual rule would be stated by an authority such as *Doe v. Roe*, `[citation to verify]` — **this name is fictional and stands in for the controlling authority the attorney must locate.**

**Application**

- Applying an unverified period to an unverified accrual date cannot yield a reliable result. If accrual ran from the alleged breach date, the period would begin on `[CONFIRM: breach date]`; the outer filing date would then be that date plus the governing period — **which this memo does not compute.** `[deadline verification required.]`
- Whether the elapsed time between `[CONFIRM: breach date]` and `[CONFIRM: as-of date]` exceeds the governing period cannot be assessed until the period is verified.
- The claim characterization (Assumption 1) is dispositive of *which* period applies and is itself unresolved.

**Conclusion on Issue 1a**

Uncertain — turns on the governing period, the accrual rule, and the claim characterization, none of which is verified. No deadline computed.

---

### Issue 1b: Does any tolling, discovery rule, or contractual modification apply?

**Rule**

`[CONFIRM: rule — no verified authority available in this session.]`

- Tolling doctrines and any "discovery rule" that defers accrual until the injury is or should have been discovered are jurisdiction-specific. `[Attorney to insert controlling authority — verify jurisdiction.]`
- Parties may, in some jurisdictions, contractually shorten or lengthen the limitations period; enforceability varies. `[Attorney to insert controlling authority; confirm the PO does or does not contain such a clause.]`

**Application**

- If a discovery rule applies and Summit discovered the defect later than the breach date, accrual could be deferred — but the discovery date is a factual gap (`[CONFIRM: discovery date]`).
- If PO SG-2210 contains a limitations-shortening clause, it could bar the claim earlier than the statutory period; the PO text has not been provided. `[CONFIRM.]`

**Conclusion on Issue 1b**

Uncertain — a discovery rule or a contractual clause could move the deadline in either direction; both depend on unverified law and missing facts.

---

### Adverse Authority and Counterarguments

- **No adverse authority has been identified in this session, because no authority has been researched or verified.** This is not a representation that none exists. `[CONFIRM: attorney must independently search for the controlling limitations statute, the accrual rule, any discovery-rule or tolling authority, and any authority on contractual limitations clauses before relying on this memo.]`

---

## Conclusion

**Question 1:** Uncertain. Whether Summit's claim is time-barred cannot be determined from the information available. The answer depends on (1) the governing jurisdiction, (2) the limitations period for the correctly characterized claim, (3) the accrual rule and the discovery date, and (4) any contractual modification of the period. No authority has been verified and no deadline has been computed. The attorney should treat this as a scoping memo that identifies what must be resolved, not as an answer.

**Key variables (focus verification here first):**
1. Governing jurisdiction and the correct claim characterization.
2. The limitations period and accrual rule under that jurisdiction's current law.
3. The discovery date, if a discovery rule may apply.
4. Whether PO SG-2210 modifies the limitations period.

---

## Authorities Cited

*Every authority below is unverified. Nothing in this table states real law.*

| # | Authority | Type | Citation | Proposition asserted | Source | Verified by attorney |
|---|-----------|------|----------|----------------------|--------|----------------------|
| 1 | `[Attorney to insert controlling limitations statute]` | Statute | `[VERIFY-CITE: section and current version — verify jurisdiction]` | Sets the limitations period for written-contract claims | Not provided — attorney to supply | - [ ] |
| 2 | `[Attorney to insert controlling authority]` | Case or Statute | `[VERIFY-CITE]` | States when a written-contract claim accrues | Not provided — attorney to supply | - [ ] |
| 3 | *Doe v. Roe* *(fictional placeholder — not a real case)* | Case | `[citation to verify]` | Illustrative stand-in for the accrual/discovery-rule authority | Placeholder — attorney to replace | - [ ] |
| 4 | `[Attorney to insert controlling authority]` | Case | `[VERIFY-CITE]` | Enforceability of contractual limitations-period clauses | Not provided — attorney to supply | - [ ] |

**Authority source key:** User-provided · Researched (named source) · Connector-verified (record URL) · `[VERIFY-CITE]` / `[CONFIRM]` — unverified; attorney must locate, review, and confirm. **In this example, every row is unverified.**

---

## Open Items / Attorney Verification

- [ ] Confirm jurisdiction and governing law are correctly identified for this matter.
- [ ] Confirm the relevant date (breach date, and any discovery date) and which event triggers accrual.
- [ ] Supply and verify the controlling limitations statute and confirm its current version.
- [ ] Supply and verify the accrual rule and any discovery-rule or tolling authority.
- [ ] Obtain and review the full PO SG-2210 text for any limitations-modifying clause.
- [ ] Confirm the correct claim characterization (written contract vs. sale-of-goods vs. tort), which governs the applicable period.
- [ ] Independently search for adverse authority not identified in this session.
- [ ] Resolve all `[CONFIRM: ...]` and `[VERIFY-CITE: ...]` placeholders throughout the memo.
- [ ] Compute any filing deadline only as an attorney task; none has been computed here. `[deadline verification required]`
- [ ] Confirm that the privilege and confidentiality designations are appropriate for how this memo will be circulated.

---

## Attorney Verification Checklist

- [ ] The legal question(s) are accurately and completely stated as the client intends them.
- [ ] Jurisdiction and governing law are correctly identified and appropriate for the matter.
- [ ] All facts stated in the memo are accurate and come from the client or verified sources — no facts have been invented or inferred without flagging.
- [ ] All assumptions are identified and their legal materiality has been assessed.
- [ ] Every case cited exists, the citation is accurate, and the holding attributed to it is correct.
- [ ] Every statute and regulation cited is current, in the correct version, and the section referenced says what the memo claims.
- [ ] No authority has been cited that was not in a user-provided document or independently verified in this session (including via a `connectors/` source, where applicable).
- [ ] The rule/holding has not been overstated, paraphrased inaccurately, or taken out of context.
- [ ] Adverse authority has been identified and addressed, not omitted.
- [ ] Any conflict-of-laws or choice-of-law issue has been identified and resolved or flagged.
- [ ] The analysis is presented from a neutral analytical posture, or the advocacy posture is explicitly noted.
- [ ] Confidence levels in the conclusion are appropriate given the state of the law and facts.
- [ ] All open items and `[CONFIRM: ...]` placeholders have been resolved before the memo is relied upon.
- [ ] Privilege and confidentiality designations are appropriate for how the memo will be circulated.

---

*This example is illustrative and built on fictional facts. It deliberately contains **no real legal authority** — every citation is a placeholder for attorney insertion. It demonstrates the IRAC discipline and source-flagging of the Legal Research Memo skill; it is not legal advice and must not be used as a template for a real matter. Run the skill on your own inputs and have a qualified attorney supply and verify every authority before any reliance.*
