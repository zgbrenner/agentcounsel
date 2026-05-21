> Shared reference material supporting the AgentCounsel contracts skills, used to help produce draft legal work product for attorney review — not legal advice.

# Fallback Language Bank

This bank provides sample fallback positions for clauses that commonly need negotiation. For each clause type it gives a **preferred position**, one or more **fallback positions**, and a short **illustrative drafting skeleton**. The bank helps a reviewer articulate the *direction* of a change and gives the supervising attorney a starting point for drafting.

## This material is draft-only

Every sample position and every drafting skeleton in this bank is **illustrative and generic**. None of it is deal-specific, none of it accounts for the governing law, and none of it is final clause language. It is **not legal advice**.

- The skeletons use `[BRACKETS]` for every term that must be set by counsel. They are deliberately incomplete.
- Whether any preferred or fallback position is actually appropriate — or acceptable — depends on the client's role, leverage, risk tolerance, the governing law, and the specific contract. Those are attorney judgments.
- A reviewer must **not** paste illustrative language from this bank into a client-facing deliverable as finished clause text. Substantive drafting of new or replacement clause language is an attorney task — see `skills/contracts/references/redline-output-guidance.md`.
- All fallback positions require attorney confirmation before they are relied on in a negotiation.

## How to use this bank

1. When a review identifies an issue, use the matching entry below to articulate a **Preferred Position** and a **Fallback Position** for the issue list — expressed as the *direction* of the change, following `skills/contracts/references/redline-output-guidance.md`.
2. Treat the illustrative skeleton as a drafting aid handed to the supervising attorney, not as output for the deliverable. When an attorney or user expressly asks for draft language, route the skeleton to the attorney to adapt, complete, and review.
3. Pair each position with a negotiability rating from `skills/contracts/references/negotiability-ratings.md` and, where relevant, a market characterization from `skills/contracts/references/market-benchmark-framework.md`.
4. Flag every open jurisdictional or enforceability question with `[verify jurisdiction]` or `[ATTORNEY TO CONFIRM: ...]`.

---

## 1. Limitation of Liability — Liability Cap

**Preferred position:** Cap is a multiple of total contract value (or annual fees), with a minimum floor, and key risks (IP indemnity, confidentiality breach, data breach, fraud, willful misconduct, death/personal injury) are carved out from the cap entirely.

**Fallback position:** Cap is fees paid in the trailing 12 months, with a supermajority of the high-risk carve-outs preserved — at minimum IP indemnity, data breach, and fraud/willful misconduct sitting outside or at an elevated cap.

**Second fallback:** Cap remains as drafted but a separate, higher "super-cap" applies to the carved-out categories.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Each party's aggregate liability shall not exceed `[CAP — e.g., the greater of (a) total fees paid or payable under this Agreement and (b) [FLOOR AMOUNT]]`, except that the foregoing cap shall not apply to `[CARVE-OUTS — e.g., indemnification obligations, breach of confidentiality, a data breach, or fraud or willful misconduct]`.

---

## 2. Limitation of Liability — Consequential Damages Waiver

**Preferred position:** Mutual waiver of indirect and consequential damages, with mutual carve-outs restoring recovery for the client's most likely loss types — data breach or loss, breach of confidentiality, IP infringement, and fraud or willful misconduct.

**Fallback position:** A carve-out for the client's most likely exposures only (data breach and confidentiality breach), even if not made mutual.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Neither party shall be liable for indirect, incidental, consequential, special, or punitive damages, except that this exclusion shall not apply to `[CARVE-OUTS — e.g., damages arising from a data breach, breach of confidentiality, infringement of intellectual property, or fraud or willful misconduct]`.

---

## 3. Indemnification

**Preferred position:** Mutual indemnities; the counterparty indemnifies the client for third-party claims arising from the counterparty's products, services, IP infringement, and breach; the client's indemnity is limited to claims caused by the client's own breach or misuse. Standard procedural controls (prompt notice, defense control, cooperation, no settlement without consent) apply.

**Fallback position:** Indemnity remains as drafted in scope but procedural controls are added (notice, defense, settlement-consent, cooperation), and the client's IP indemnity is narrowed to claims arising from client modifications or client-supplied materials.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> `[PARTY]` shall defend, indemnify, and hold harmless `[OTHER PARTY]` from third-party claims arising from `[TRIGGER]`, provided that the indemnified party `[gives prompt written notice, allows the indemnifying party to control the defense, and reasonably cooperates]`. The indemnified party shall not settle any claim without the indemnifying party's prior written consent.

---

## 4. Confidentiality — Definition and Exclusions

**Preferred position:** Confidential Information is reasonably scoped, and the definition includes the standard exclusions: information that is public through no fault of the recipient, independently developed, rightfully received from a third party without restriction, or already known to the recipient.

**Fallback position:** Definition stays broad but the standard exclusions are added in full, and a compelled-disclosure provision (law or court order, with notice where permitted) is included.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> "Confidential Information" does not include information that: (a) is or becomes publicly available through no act or omission of the receiving party; (b) was rightfully known to the receiving party without restriction before disclosure; (c) is independently developed without use of the disclosing party's Confidential Information; or (d) is rightfully received from a third party without a duty of confidentiality.

---

## 5. Confidentiality — Term and Survival

**Preferred position:** Confidentiality obligations survive for a defined period after termination appropriate to the sensitivity of the information, with trade secrets protected for as long as they remain trade secrets.

**Fallback position:** A defined survival period for general Confidential Information; an indefinite or longer period for trade secrets only, rather than a perpetual obligation on everything.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> The obligations in this Section survive for `[PERIOD]` after termination or expiration, except that obligations with respect to trade secrets continue for so long as the information remains a trade secret under applicable law. `[verify jurisdiction]`

---

## 6. Intellectual Property Ownership and Assignment

**Preferred position:** Present-tense assignment of all work product to the client ("hereby assigns"), a further-assurances obligation, treatment of moral rights, and a narrow, clearly-defined background-IP carve-out with a license back to the client for any background IP embedded in deliverables.

**Fallback position:** Present-tense assignment plus a further-assurances obligation; if the vendor retains background IP, a perpetual, royalty-free license to the client to use that background IP as embedded in the deliverables, surviving termination.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> `[PARTY]` hereby irrevocably assigns to `[CLIENT]` all right, title, and interest in the Deliverables, and shall execute such further documents as `[CLIENT]` reasonably requests to perfect that assignment. To the extent any `[PARTY]` background materials are embedded in the Deliverables, `[PARTY]` grants `[CLIENT]` a perpetual, irrevocable, royalty-free license to use them as part of the Deliverables. `[Address moral rights — verify jurisdiction.]`

---

## 7. Data Protection — Breach Notification

**Preferred position:** The vendor must notify the client without undue delay and within a short, defined number of hours after becoming aware of a security incident, with enough detail to support the client's own regulatory and customer notifications.

**Fallback position:** Notification tied to a confirmed breach within a defined short period, with a commitment to provide updating information as the investigation develops.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Vendor shall notify Client without undue delay, and in any event within `[NUMBER]` hours, after becoming aware of a Security Incident affecting Client data, and shall provide `[information reasonably necessary for Client to meet its own notification obligations]`. `[ATTORNEY TO CONFIRM: notification period required under applicable law — verify jurisdiction.]`

---

## 8. Data Protection — Vendor Use of Client Data

**Preferred position:** The vendor may use client data only to provide the contracted services; any use for product improvement, analytics, benchmarking, or training AI/ML models is excluded unless separately and expressly agreed.

**Fallback position:** Use beyond providing the services is limited to aggregated and de-identified data that cannot be attributed to the client, with model training expressly excluded.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Vendor shall use Client Data solely to provide the Services and for no other purpose. Vendor shall not use Client Data to `[develop or improve other products, benchmark, or train any machine-learning model]` except `[as expressly agreed in writing / in aggregated, de-identified form that cannot be attributed to Client]`.

---

## 9. Data Protection — Return and Deletion on Termination

**Preferred position:** On termination, the client may export its data in a usable format during a defined retrieval window, after which the vendor deletes the data and certifies deletion, subject only to legal-hold and backup exceptions.

**Fallback position:** A defined post-termination retrieval window and a deletion obligation on request, with deletion certified on the client's request.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> For `[NUMBER]` days after termination, Client may export Client Data in `[FORMAT]`. Thereafter, Vendor shall delete Client Data and, on request, certify deletion, except for copies retained in routine backups or as required by law, which remain subject to the confidentiality obligations of this Agreement.

---

## 10. Payment Terms

**Preferred position:** A commercially reasonable payment window measured from receipt of a correct invoice, a good-faith dispute mechanism allowing disputed amounts to be withheld without penalty, and any suspension right preceded by notice and a cure period.

**Fallback position:** The payment window stays as drafted, but a good-faith invoice-dispute carve-out is added so disputed amounts do not trigger late fees, interest, or suspension while the dispute is being resolved.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Undisputed amounts are due within `[NUMBER]` days of receipt of a correct invoice. Client may withhold amounts disputed in good faith, and such amounts shall not be subject to late fees, interest, or suspension of Services pending resolution. Vendor may suspend Services for non-payment of undisputed amounts only after `[NUMBER]` days' written notice and an opportunity to cure.

---

## 11. Price Escalation

**Preferred position:** Pricing is fixed for the initial term; any increase at renewal is capped by reference to a published index and the client has the right to terminate without penalty if it rejects an increase.

**Fallback position:** Increases are capped at a fixed percentage per year and require advance notice; the client may terminate at renewal if the increase exceeds the cap.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Fees are fixed during the Initial Term. At each renewal, Vendor may increase fees by no more than `[the lesser of [PERCENT]% or the change in [INDEX]]`, on at least `[NUMBER]` days' notice. If Client rejects an increase, Client may terminate effective at the end of the then-current term without penalty.

---

## 12. Termination for Convenience

**Preferred position:** Mutual termination for convenience on reasonable notice, with no early-termination fee and a defined wind-down and transition period.

**Fallback position:** A client-side termination-for-convenience right on reasonable notice; if a fee applies, it is limited to unrecovered, pre-approved costs rather than all remaining contract value.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Either party may terminate this Agreement for convenience on `[NUMBER]` days' prior written notice. `[If a fee applies: Client's sole payment obligation on such termination is for Services performed through the termination date and [non-cancelable, pre-approved commitments].]`

---

## 13. Termination for Cause and Cure Period

**Preferred position:** Termination for cause requires a *material* breach and a reasonable cure period; immediate termination is reserved for breaches incapable of cure.

**Fallback position:** The cure period stays as drafted but the trigger is narrowed from "any breach" to "material breach," and the right is made mutual.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Either party may terminate this Agreement if the other party materially breaches it and fails to cure the breach within `[NUMBER]` days after written notice describing the breach.

---

## 14. Assignment and Change of Control

**Preferred position:** Neither party may assign without consent, except that either party may assign to an affiliate or in connection with a merger or sale of substantially all assets; a change of control of the vendor gives the client a consent or termination right.

**Fallback position:** Vendor assignment and change of control require notice to the client and give the client a right to terminate if the assignee or acquirer is a competitor of the client.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Neither party may assign this Agreement without the other's prior written consent, except to an affiliate or in connection with a merger or sale of substantially all assets. `[If Vendor undergoes a change of control, Client may terminate on [NUMBER] days' notice if the acquirer is a competitor of Client.]`

---

## 15. Governing Law and Forum

**Preferred position:** Governing law and forum bear a reasonable connection to the parties or the transaction, or sit in a neutral jurisdiction; the dispute provisions (governing law, forum, and any arbitration clause) are internally consistent.

**Fallback position:** A neutral, mutually acceptable jurisdiction, or each party brings suit in the other's home forum; any arbitration clause preserves a court carve-out for injunctive relief.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> This Agreement is governed by the laws of `[JURISDICTION]`. The parties submit to the `[exclusive / non-exclusive]` jurisdiction of the courts of `[FORUM]`. `[verify jurisdiction]`

---

## 16. Audit Rights

**Preferred position:** The client has a right to audit, or to obtain third-party audit reports, for the counterparty's compliance with security, data, and material obligations; any audit right running against the client is reciprocal and procedurally limited.

**Fallback position:** In place of an on-site audit, the counterparty provides recognized third-party audit reports or certifications on request; any vendor audit of the client is limited as to notice, frequency, scope, and cost.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> On reasonable prior notice and no more than `[FREQUENCY]`, `[PARTY]` may audit `[OTHER PARTY]`'s compliance with `[OBLIGATIONS]`, or `[OTHER PARTY]` may instead provide `[a current third-party audit report / certification]`. Audits shall occur during business hours, minimize disruption, and be subject to confidentiality. Each party bears its own audit costs unless the audit reveals a material discrepancy.

---

## 17. Warranties

**Preferred position:** The counterparty warrants that the product or service will conform to its documentation and specifications for a defined period, that services will be performed in a professional and workmanlike manner, and that the deliverables do not infringe third-party rights.

**Fallback position:** A conformance-to-documentation warranty for a defined period, with a remedy that includes a refund or termination right if repair or replacement fails.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Vendor warrants that, for `[PERIOD]`, the `[product / service]` will conform in all material respects to `[the Documentation / the specifications]`. If it does not, Vendor shall `[repair or replace it; and if Vendor cannot do so within [NUMBER] days, Client may terminate and receive a refund of [fees for the non-conforming portion]]`.

---

## 18. Service Levels

**Preferred position:** A defined availability commitment with meaningful service credits, narrowly scoped exclusions, capped scheduled-maintenance windows, and a right to terminate for chronic or material SLA failure separate from the credit mechanism.

**Fallback position:** Service credits stay as drafted, but a termination right is added for chronic SLA failure (for example, a defined number of breaches in a rolling window), and credits are not the sole remedy for that chronic-failure scenario.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Vendor commits to `[PERCENT]%` availability per `[period]`, measured as set out in `[Exhibit]`. Service credits are described in `[Exhibit]`. If Vendor fails to meet the availability commitment in `[NUMBER]` `[periods]` within any rolling `[window]`, Client may terminate without penalty; service credits are not Client's sole remedy for such chronic failure.

---

## 19. Insurance

**Preferred position:** The counterparty must carry coverage types and limits that match the risks its performance creates (commercial general liability, professional liability / errors and omissions, cyber, workers' compensation as applicable), name the client as an additional insured where appropriate, and deliver certificates and notice of cancellation or material reduction.

**Fallback position:** Coverage types and limits stay as drafted but the operational mechanics are added — certificates of insurance, additional-insured status where appropriate, and notice of cancellation or material reduction.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> During the Term, `[PARTY]` shall maintain `[COVERAGE TYPES]` with limits of at least `[AMOUNTS]`, shall name `[CLIENT]` as an additional insured under `[POLICIES]` where applicable, and shall on request deliver certificates of insurance and provide `[NUMBER]` days' notice of cancellation or material reduction in coverage.

---

## 20. Publicity and Use of Name

**Preferred position:** Neither party may use the other's name, logo, or marks, or publish a case study or testimonial, without the other's prior written consent for each use; press releases require mutual approval.

**Fallback position:** A limited, revocable right to identify the client on a customer list only, with all other publicity — case studies, testimonials, press releases — requiring the client's prior written consent.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> Neither party shall use the other's name, logos, or trademarks, or publish any case study, testimonial, or press release referring to the other, without that party's prior written consent. `[Optional: Vendor may include Client's name and logo in a factual customer list, subject to Client's brand guidelines and revocable on Client's request.]`

---

## 21. Non-Solicitation and Non-Competition

**Preferred position:** No non-compete; any employee non-solicit is narrowly scoped to personnel connected to the engagement, carves out general advertising and unsolicited applicants, and is limited in duration. Restrictive covenants are confined to what the transaction genuinely requires.

**Fallback position:** A narrowly tailored, mutual employee non-solicit with the general-advertising and unsolicited-applicant carve-outs and a defined, limited duration; no customer non-solicit or non-compete.

**Illustrative drafting skeleton (counsel must draft and adapt):**
> During the Term and for `[PERIOD]` after, neither party shall knowingly solicit for employment any employee of the other who was directly involved in the engagement, except that general advertising not targeted at such employees, and the hiring of any person who responds to it or otherwise applies without solicitation, are not restricted. `[ATTORNEY TO CONFIRM: enforceability and permissible scope — verify jurisdiction.]`

---

## Reviewer Notes

- This bank covers commonly negotiated clauses. It is not exhaustive; deal-specific provisions may have no entry here and still need a fallback position.
- The preferred and fallback positions are written from the perspective of a client that is generally the customer, buyer, licensee, or disclosing party. Where the client is the vendor or receiving party, the directions often invert — confirm the client's role before applying an entry.
- Always pair a fallback position with the reason the preferred position may not be achievable (leverage, counterparty form, regulatory floor) — see `skills/contracts/references/negotiability-ratings.md`.
- See `skills/contracts/references/redline-output-guidance.md` for how to express these positions in a deliverable as the direction of a change rather than as final drafted language.
