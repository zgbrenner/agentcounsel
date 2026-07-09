# Example: Claim Chart

> **Illustrative example — not legal advice.** This is a sample of what the Claim Chart skill (`skills/litigation/claim-chart/SKILL.md`) produces. Every party, document, bates number, quotation, and record cite in it is **fictional** and was invented for illustration. **No real cause of action, statute, case, or rule is stated** — the elements are treated as attorney-supplied and their source is flagged for verification throughout. This is an internal analytical draft — attorney work product — not a filed contention and not legal advice. See `examples/README.md`.

## Scenario

Harborline Freight LLC is a fictional logistics company that ordered a run of custom shipping pallets from Delta Pallet Co., another fictional company. Harborline alleges the pallets were delivered late and failed a load-rating spec, and it has sued Delta on a written-contract theory. Harborline's counsel, preparing for the close of discovery, wants an element-by-element map of the pleaded claim against the record developed so far, so the team can see what is supported and what still needs evidence before summary-judgment strategy. This is **civil mode, asserting side**. The controlling elements were supplied by the attorney from the operative pleading; consistent with the skill, the elements' governing source is recorded as an attorney-verification item and no statute or case is named. One document was produced under a protective order, so a use-restriction note appears before it is mapped. This example shows the mapping discipline: verbatim record quotes with pin cites, honest mapping states (including "gap" and "needs-evidence"), and a disputed element-definition left open for the court — with **no conclusion on liability**.

## Illustrative Output

> **Privileged & Confidential — Attorney Work Product — Draft for Attorney Review Only.** Every mapping below is an analytical lead the attorney must verify against the source. No conclusion on breach, liability, or non-liability has been drawn. This chart must not be filed, served, or produced without attorney review and authorization.

### 1. Intake Summary

| Field | Value |
|---|---|
| Matter | Harborline Freight LLC v. Delta Pallet Co. (fictional; no docket number assigned) |
| Case theory (one line) | Plaintiff Harborline contends Delta breached the written pallet-supply contract by late, non-conforming delivery; we represent Harborline (asserting). |
| Mode | Civil — Cause of Action |
| Side | Asserting |
| Cause of Action | Breach of written supply contract (as pleaded in the operative complaint) `[ATTORNEY TO CONFIRM: cause of action as stated in the operative pleading]` |
| Evidence Corpus | Executed supply contract; purchase order; two email threads; Delta packing slip and invoice; Harborline incoming-inspection report; deposition excerpts of two witnesses |
| Jurisdiction and Court | `[verify jurisdiction]` — not provided; flagged throughout |
| Phase | Discovery (approaching close) |
| Elements Source | `[ATTORNEY TO CONFIRM: elements source and governing authority — pattern jury instruction, approved charge, or governing statute — verify jurisdiction. The four elements below were supplied by counsel from the operative pleading and are used as provided; no legal authority is asserted by this chart.]` |
| Use-Restriction Check | One document (Delta internal QA log, DELTA-QA-0007) is designated **Confidential — Attorney's Eyes Only** under the protective order. `[VERIFY: confirm permissible use before relying on this document in any filed paper.]` All other documents are unrestricted per the production log. |
| Claim Construction / Element-Definition | The meaning of "conforming" goods and of the delivery "deadline" are contested — see Section 2. Not resolved here. |
| Prepared by | Drafting agent, for the assigned attorney of record |
| Date Prepared | `[CONFIRM: date of preparation]` |
| Status | DRAFT — Attorney Work Product — For Attorney Review Only — DO NOT FILE OR SERVE WITHOUT ATTORNEY AUTHORIZATION |

### 2. Element-by-Element Claim Chart

**Mapping states:** Supported · Partial · Disputed · Gap · Needs-evidence

*The four elements are used exactly as supplied by counsel; their governing source is an attorney-verification item (see Intake). No element below is stated as legal authority.*

| # | Element (as supplied by counsel) | Evidence (verbatim quote + pin cite) | Mapping State | Notes for Attorney | Verified |
|---|---|---|---|---|---|
| 1 | Existence of a valid and enforceable contract between the parties | "Buyer and Seller agree to the purchase and sale of 1,200 custom pallets, Model HL-Grade, per the specifications in Exhibit A." — Supply Contract, § 1 (HARB-000102) | Supported | Executed by both parties per signature block at HARB-000108. Confirm no integration/amendment issue. | `[ ]` |
| 2 | Plaintiff's own performance or a valid excuse for nonperformance | "Payment of the 50% deposit ($ `[CONFIRM: amount]`) was received on `[CONFIRM: date]`." — Delta invoice DEL-INV-3391 (HARB-000140) | Partial | Deposit performance supported; full-performance/tender of remaining obligations not yet documented. `[VERIFY: paraphrase of payment timing — pin cite the wire confirmation.]` | `[ ]` |
| 3 | Defendant's breach — failure to deliver conforming goods by the required date | "Load-rating test result: 1,410 lbs average against a 1,800 lb rated minimum. Result: FAIL." — Harborline Incoming Inspection Report IIR-2207 (HARB-000210, p. 2) | Disputed | Harborline's inspection asserts non-conformity; Delta's QA log (DELTA-QA-0007, **use-restricted**) reportedly records a passing internal test. Conflicting evidence on both sides — do not resolve. Turns partly on the "conforming" definition (Section 2). | `[ ]` |
| 3a | Breach — timeliness of delivery | "Ship date confirmed for the week of `[CONFIRM: date]`; goods received `[CONFIRM: date]`." — Delta packing slip PS-882 (HARB-000155); Okonkwo Dep. 88:4–14 | Disputed | Whether delivery was "late" depends on which date controls — the PO date or a later emailed revised date. See Section 2 element-definition dispute. | `[ ]` |
| 4 | Damages to plaintiff caused by the breach | "We had to re-source 1,200 pallets on 3 days' notice and paid a rush premium." — Email, T. Alvarez (Harborline) to file, DELTA-EM-0455 | Needs-evidence | Damages asserted in correspondence only; no invoices, cover-purchase records, or downstream chargeback documents in the corpus yet. Causation link to the alleged breach not yet documented. | `[ ]` |

**Drafting notes:**
- Every entry ties to a specific record cite; thin or correspondence-only support is recorded as "needs-evidence," not "supported."
- Element 3 is recorded as **Disputed** because conflicting evidence exists on both sides; the chart does not resolve it.
- Bracketed `[CONFIRM]` items mark quotes/dates that must be pinned to native records before reliance.

### 3. Disputed Constructions and Element-Definition Questions

*Listed, not resolved. Preserved for attorney and, where applicable, court determination.*

| Term or Element | Dispute or Ambiguity | Impact on Mapping | Attorney Action Required |
|---|---|---|---|
| "Conforming" goods | Contract § 3 references Exhibit A specs; the parties dispute whether the 1,800 lb load rating is a binding spec or a target. | Determines whether Element 3 maps as Supported or remains Disputed. | `[VERIFY: disputed element definition — attorney to advise; may require construction of Exhibit A.]` |
| Delivery "deadline" | The PO states one ship date; a later email thread references a revised date. Which controls is contested. | Governs Element 3a (timeliness). | `[VERIFY: disputed element definition — attorney to determine which instrument controls; verify jurisdiction on contract-modification standard.]` |

### 4. Patent-Specific Flags

**N/A — this is a civil-mode chart.** Doctrine-of-equivalents, indirect/divided infringement, and invalidity-burden sections do not apply.

### 5. Gap List

| Element # | Element (abbreviated) | Mapping State | What Is Needed | Priority |
|---|---|---|---|---|
| 2 | Plaintiff's full performance | Partial | Wire-transfer confirmation; any documentation of remaining contractual obligations tendered | Medium — attorney to assign |
| 3 | Non-conformity | Disputed / Construction-dependent | Resolution of the "conforming" definition; possible expert on load-rating methodology; access decision on use-restricted DELTA-QA-0007 | High — attorney to assign |
| 3a | Timeliness | Disputed / Construction-dependent | Determination of controlling delivery date; native email metadata for the revised-date thread | High — attorney to assign |
| 4 | Damages / causation | Needs-evidence | Cover-purchase invoices; rush-premium documentation; any downstream chargeback records; causation testimony | High — attorney to assign |

### 6. Open Items for Attorney Verification

- [ ] `[VERIFY: jurisdiction, court, governing law, and phase confirmed]`
- [ ] `[ATTORNEY TO CONFIRM: controlling elements source confirmed — verify jurisdiction]`
- [ ] `[VERIFY: use-restriction check completed; DELTA-QA-0007 not relied upon in any filed paper without clearance under the protective order]`
- [ ] `[VERIFY: both element-definition disputes flagged in Section 3; neither resolved without attorney direction]`
- [ ] `[VERIFY: all verbatim quotes confirmed accurate against source documents; all paraphrases pin-cited]`
- [ ] `[VERIFY: all bracketed dates and amounts confirmed against native records]`
- [ ] `[VERIFY: no mapping state overstated — Element 4 recorded as "needs-evidence," not "supported"]`
- [ ] `[ATTORNEY TO CONFIRM: gap list reviewed; discovery and expert plan established before close of discovery]`
- [ ] `[VERIFY: no legal conclusion on breach, liability, or non-liability appears in this chart]`
- [ ] `[VERIFY: no statute-section number, case name, or named doctrine has been asserted as authority]`
- [ ] `[ATTORNEY TO CONFIRM: chart authorized for any use beyond internal attorney review — do not file, serve, or produce without authorization]`

---

## Attorney Verification Checklist

- [ ] Jurisdiction, court, governing law, and phase confirmed.
- [ ] The controlling elements (civil mode) or the asserted claim limitations (patent mode) have been confirmed by attorney against the authoritative source.
- [ ] Use-restriction check completed; no use-restricted materials have been incorporated without attorney clearance.
- [ ] All disputed claim terms or element definitions have been flagged and none have been silently resolved.
- [ ] Every mapping entry has been verified against the source document; no entry is based on model background knowledge or extrapolation.
- [ ] All verbatim quotes are accurate; all paraphrases are flagged `[VERIFY]`.
- [ ] Pinpoint cites are complete and accurate for every mapping entry.
- [ ] No mapping state has been overstated; thin or ambiguous evidence is recorded as "needs-evidence," not "supported."
- [ ] The gap list is complete; attorney has reviewed what additional discovery, expert input, or construction resolution is needed.
- [ ] Doctrine-of-equivalents leads (patent mode) have been reviewed by attorney; no equivalents conclusion has been drawn by the agent.
- [ ] Indirect and divided infringement flags (patent mode) have been reviewed by attorney.
- [ ] Invalidity burden note (patent mode, invalidity) confirmed as accurate for the applicable jurisdiction.
- [ ] No legal conclusion on infringement, non-infringement, validity, invalidity, liability, or non-liability appears in the chart.
- [ ] No statute-section number, case name, court-rule number, or named doctrine has been asserted as authority.
- [ ] The chart is labeled as a draft for attorney review and has not been filed, served, or produced.
- [ ] Any portion of the chart to be incorporated into a filed document has been reviewed, revised as needed, and authorized by the responsible attorney of record.

---

*This example is illustrative and built on fictional facts. It demonstrates the structure and discipline of the Claim Chart skill; it is not legal advice and must not be used as a template for a real matter. Run the skill on your own inputs and have the responsible attorney verify every mapping against the source before any reliance.*
