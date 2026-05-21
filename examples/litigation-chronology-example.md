# Example: Litigation Chronology

> **Illustrative example — not legal advice.** This is a sample of what the Litigation Chronology skill (`skills/litigation/litigation-chronology/SKILL.md`) produces. Every party, date, document, and event in it is **fictional** and was invented for illustration. It is the kind of draft work product a supervising attorney would review — not a finished deliverable, and not legal advice. See `examples/README.md`.

## Scenario

Meridian Fabrication LLC ("Meridian"), a fictional metal-parts manufacturer, retained counsel after a contract dispute with its supplier, Brightline Components Co. ("Brightline"). Meridian alleges that Brightline delivered nonconforming aluminum housings under Purchase Order 4471 and that the late, defective shipment caused Meridian to miss a downstream delivery to its own customer. Brightline contends the housings conformed to spec and that Meridian's own revised drawings caused the problem. Meridian is the prospective plaintiff. To build this draft chronology, counsel was provided a small set of source documents: the executed purchase order, an email thread between Sam Delgado (Meridian) and Priya Okafor (Brightline), Brightline's packing slip and invoice, Meridian's incoming-inspection report, and a single text-message screenshot. The chronology organizes those documents by event date so a supervising attorney can assess the breach timeline before any demand letter is drafted.

## Illustrative Output

> Draft legal work product for attorney review. Not legal advice. This document is matter-specific and should be kept in the client file.

---

# Litigation Chronology

**Matter:** Meridian Fabrication LLC — Potential Claim re Purchase Order 4471 (no matter number assigned)
**Client / Role:** Meridian Fabrication LLC — Prospective Plaintiff
**Prepared by:** Drafting agent, for review by assigned attorney
**Date prepared:** [CONFIRM: date of preparation]
**Status:** DRAFT — Attorney Work Product — For Attorney Review Only
**Privilege posture of source documents:** Mixed or potentially privileged — `[ATTORNEY TO CONFIRM: privilege status of source documents before distribution of this chronology]`

---

## Sources Reviewed

No event appears in the table below unless it is supported by a document on this list.

| # | Document Name / Description | Bates Range or Identifier | Date of Document | Document Type | Custodian / Produced By |
|---|---|---|---|---|---|
| 1 | Purchase Order 4471 (executed) | MERID-00001–00003 | 02-March (fictional yr) | Contract / PO | Meridian — S. Delgado |
| 2 | Email thread, Delgado–Okafor ("PO 4471 — drawings & lead time") | MERID-00010–00017 | 04-March–19-March | Email chain | Meridian — S. Delgado |
| 3 | Brightline packing slip, Shipment SL-882 | MERID-00021 | 21-March | Packing slip | Meridian — receiving dept. |
| 4 | Brightline Invoice 7730 | MERID-00022 | 23-March | Invoice | Meridian — accounts payable |
| 5 | Meridian Incoming Inspection Report IIR-0445 | MERID-00030–00031 | 24-March | Inspection record | Meridian — QA |
| 6 | Text-message screenshot (Delgado / Okafor) | MERID-00040 | undated on its face | Text message | Meridian — S. Delgado |

---

## Severity / Priority Key

| Label | Meaning |
|---|---|
| **High** | Directly relevant to a central claim, defense, or damages element; likely contested at trial |
| **Medium** | Relevant background or corroborating fact; provides context |
| **Low** | Potentially relevant but peripheral; included for completeness |
| **[DISPUTED]** | Two or more documents conflict on this event; do not treat as established |
| **[CONFIRM]** | Date, actor, or fact is uncertain or approximate; verify before reliance |
| **[GAP]** | Expected event or document is absent from the record |

---

## Chronology Table

| Date | Time (if known) | Event Description | Source Document / Bates | Actor(s) | Significance | Disputed? | Attorney Note |
|---|---|---|---|---|---|---|---|
| 02-March | — | Meridian issues and Brightline countersigns Purchase Order 4471 for 600 aluminum housings, part no. AH-12, at agreed unit price; PO states delivery "on or before 20-March." | PO 4471 (MERID-00001–00003) | S. Delgado (Meridian); P. Okafor (Brightline) | High | No | Contract-formation event; confirm PO terms control over any later email terms. |
| 04-March | 9:12 a.m. | Delgado emails Okafor attaching drawing AH-12 Rev. B and asks Brightline to "confirm you are building to Rev. B." | Email thread (MERID-00010) | S. Delgado | High | No | Establishes the governing drawing revision per Meridian. |
| 07-March | — | Okafor replies confirming Brightline "received Rev. B" and stating lead time "remains comfortable." | Email thread (MERID-00012) | P. Okafor | Medium | No | — |
| 11-March (per email) / 12-March (per text) | — | Delgado sends a further drawing change. Email thread shows a "Rev. C" attachment dated 11-March; the text-message screenshot refers to "the new drawing I sent yesterday" in a message Okafor answers, implying a 12-March send date. | Email thread (MERID-00014); Text screenshot (MERID-00040) | S. Delgado | High | **[DISPUTED]** | **[DISPUTED]** — Two sources conflict on the date the Rev. C change was transmitted. Do not treat either date as established. Pin down via email metadata and native text-message export. |
| circa 13-March | — | Okafor responds (text screenshot) that the late drawing change "may push the ship date." | Text screenshot (MERID-00040) | P. Okafor | High | No | **[CONFIRM]** — Screenshot is undated on its face; 13-March is inferred from its position relative to the 12-March message it answers. Inference flagged for attorney verification against native text data. |
| 20-March | — | Contractual delivery deadline under PO 4471 passes. No shipment received by Meridian as of this date. | PO 4471 (MERID-00001–00003); Packing slip (MERID-00021) | — | High | No | Apparent missed delivery date. **[CONFIRM]** whether any extension was agreed — see disputed Rev. C timing above. |
| 21-March | — | Brightline ships housings; packing slip SL-882 lists 600 units of part AH-12 and references "Rev. B." | Packing slip (MERID-00021) | Brightline (shipper) | High | No | Packing slip cites Rev. B, not Rev. C — relevant to the conformity dispute. |
| 22-March | — | Shipment SL-882 received at Meridian dock. | Inspection report (MERID-00030) | Meridian receiving | Medium | No | Receipt date taken from inspection report intake line. |
| 23-March | — | Brightline issues Invoice 7730 for the full PO 4471 quantity. | Invoice 7730 (MERID-00022) | Brightline (A/R) | Low | No | Invoice unpaid as of last source document; payment status not in record. |
| 24-March | — | Meridian QA completes Incoming Inspection Report IIR-0445; report records 142 of 600 housings as out of tolerance on a mounting-hole dimension and notes units "appear built to Rev. B." | Inspection report (MERID-00030–00031) | Meridian QA | High | **[DISPUTED]** | **[DISPUTED]** — Whether the housings are nonconforming turns on which drawing revision governs; Brightline's position not yet documented in the record. Record both: Meridian asserts nonconformity vs. Rev. C; Brightline shipped to Rev. B per packing slip. |
| 26-March | 2:40 p.m. | Delgado emails Okafor rejecting the 142 units and demanding rework or replacement; email asserts Brightline "ignored Rev. C." | Email thread (MERID-00016) | S. Delgado | High | No | Notice-of-breach / rejection communication per Meridian. Confirm whether email satisfies any contractual notice clause. |
| 27-March | — | Okafor replies stating Brightline "built exactly to the print in our file" and disputing that Rev. C was ever received. | Email thread (MERID-00017) | P. Okafor | High | **[DISPUTED]** | **[DISPUTED]** — Brightline denies receipt of Rev. C; conflicts with Meridian's 11/12-March transmittal entry above. |
| circa late March | — | Meridian states it missed a delivery to its own downstream customer as a result of the housing defects (referenced in Delgado email). | Email thread (MERID-00016) | S. Delgado | Medium | No | **[CONFIRM]** — Downstream delay and any resulting damages are asserted in correspondence only; no underlying customer documents in the record. |

---

## Gaps and Missing Periods

- **[GAP]** 07-March to 11-March: No correspondence produced covering the period between Brightline's lead-time confirmation and the disputed Rev. C transmittal. Any emails or calls in this window should be requested.
- **[GAP]** Native electronic data: The Rev. C transmittal and the text-message thread exist only as a PDF email chain and a screenshot. Native files with metadata (email headers, message timestamps) have not been obtained and are needed to resolve the date conflict.
- **[GAP]** Brightline-side documents: No Brightline internal records (production travelers, the drawing in Brightline's file, internal emails) have been produced. These are anticipated in discovery and are central to the conformity dispute.
- **[GAP]** Downstream customer materials: No documents from Meridian's own customer (purchase order, delay notice, chargeback) have been produced to support the asserted consequential damages.

## Open Items for Attorney Verification

- [ ] **[DISPUTED]** Date the Rev. C drawing change was transmitted (11-March per email vs. 12-March per text). Attorney to evaluate against native metadata before relying on either date.
- [ ] **[DISPUTED]** Whether the housings are nonconforming, which turns on the governing drawing revision (Rev. B per packing slip vs. Rev. C per Meridian). Do not resolve; both versions recorded.
- [ ] **[DISPUTED]** Brightline's denial that it ever received Rev. C. Conflicts with Meridian's transmittal entry; resolution depends on Brightline-side discovery.
- [ ] **[CONFIRM]** Date of preparation of this chronology.
- [ ] **[CONFIRM]** The circa 13-March text-message date is an inference from message sequence — verify against native text-message export.
- [ ] **[CONFIRM]** Whether the parties agreed any extension of the 20-March delivery deadline.
- [ ] **[CONFIRM]** Asserted downstream-customer delay and resulting damages — currently supported only by Meridian correspondence.
- [ ] **[ATTORNEY TO CONFIRM]** Privilege status of all source documents before this chronology is distributed; posture is currently mixed/unconfirmed.
- [ ] Confirm whether the 26-March rejection email satisfies any contractual notice-of-defect requirement [verify jurisdiction] [deadline verification required].
- [ ] Confirm any applicable limitations period and acceptance/rejection deadlines [verify jurisdiction] — no authority cited here; [CONFIRM: governing law and any controlling rule].

## Assumptions

- Documents were assumed authentic and unaltered as produced. Authenticity has not been independently verified.
- The text-message screenshot (MERID-00040) is undated on its face; its position in the chronology was inferred from the content of the messages it references. The placement is approximate and flagged above.
- "March" dates use a fictional year; year and exact calendar dates must be confirmed against the native documents.
- The PO 4471 terms were assumed to control over later email exchanges. Whether the emails modified the contract is a legal question reserved for the attorney; [CONFIRM: governing contract terms].
- This chronology reflects only the six documents in the Sources Reviewed list and is not a complete record of all events in the matter.

---

*This chronology reflects only the documents listed in the Sources Reviewed section above. It does not constitute a complete record of all events in this matter. It is a draft for attorney review and must not be used or distributed as a final work product without attorney verification.*
