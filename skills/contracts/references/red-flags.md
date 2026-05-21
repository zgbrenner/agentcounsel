> Shared reference material supporting the AgentCounsel contracts skills, used to help produce draft legal work product for attorney review — not legal advice.

# Contract Red-Flag Catalog

This catalog lists clause patterns and structural features that a reviewer should actively scan for during a contract review. Each entry describes the pattern, why it matters, what to check, and which client roles are most exposed. The catalog is organized by clause category to support a Red Flags Quick Scan output within the contracts skills.

This catalog is a review aid. It identifies what to look for and why. Whether a flagged pattern is actually problematic depends on the specific contract language, the client's role, the business context, and attorney judgment. Every flagged item is a candidate for attorney verification — not a legal conclusion.

---

## How to Use This Catalog

For each clause category below:

1. Locate the relevant provision in the document under review (or note its absence — a missing provision is itself a red flag in many contexts).
2. Check the pattern description against the actual language.
3. If the pattern is present, add the item to the risk matrix and the issue list.
4. Note which client roles are most exposed and whether the client's role matches the exposure profile.
5. Flag every finding for attorney review; do not resolve ambiguity silently.

---

## 1. Limitation of Liability

### 1.1 Cap tied to a very short period or very low base

**Pattern:** The liability cap is calculated as fees paid in the prior one or two months, or a nominal fixed amount that is small relative to the realistic loss scenario.

**Why it matters:** If the client's realistic harm from a breach (data loss, business interruption, IP misappropriation) greatly exceeds the cap, the clause transfers nearly all downside risk to the client.

**What to check:**
- Quote the cap formula verbatim.
- Compare the cap amount to the client's estimated worst-case exposure and the total contract value.
- Identify whether the cap applies to all claims or only certain types.

**Most exposed:** Customer / buyer / licensee receiving services or data access; any party whose loss would be consequential in nature.

---

### 1.2 Consequential-damages waiver covering the client's primary loss type

**Pattern:** The waiver of indirect, consequential, incidental, or special damages is mutual in form but asymmetric in effect — because the client's realistic losses are almost entirely consequential (lost profits, business interruption, data loss) while the vendor's realistic losses are direct (unpaid fees).

**Why it matters:** A nominally mutual clause can be functionally one-sided if one party's harm is categorically different from the other's.

**What to check:**
- Quote the exclusion language exactly.
- Identify whether lost profits, lost data, or business interruption are expressly included or excluded.
- Check whether any carve-outs restore consequential-damages recovery for specific breach types (data breach, fraud, willful misconduct, IP infringement).

**Most exposed:** Customer / buyer relying on services for business operations; parties with high data or IP exposure.

---

### 1.3 No carve-outs for fraud, willful misconduct, or death/personal injury

**Pattern:** The cap and consequential-damages waiver apply to all claims with no exceptions for egregious conduct.

**Why it matters:** Absence of carve-outs for fraud, willful misconduct, gross negligence, or death/personal injury is non-standard and may be unenforceable in some jurisdictions `[verify jurisdiction]`.

**What to check:**
- List every carve-out that is present.
- Note any carve-out that is one-sided (e.g., data breach carved out for vendor but not for client).

**Most exposed:** Any party relying on the counterparty to handle sensitive data, physical property, or activities with personal-injury risk.

---

### 1.4 IP indemnity subject to liability cap

**Pattern:** The intellectual property indemnity is not carved out from the liability cap, meaning the indemnifying party's maximum exposure for an IP infringement claim is limited to the cap amount.

**Why it matters:** IP infringement claims can generate liability far exceeding typical fee-based caps. If the IP indemnity is capped, the party receiving the indemnity bears the excess risk.

**What to check:**
- Confirm whether the IP indemnity is expressly carved out from the cap.
- Check whether the indemnity is mutual or one-sided.

**Most exposed:** Licensee or customer accepting IP representations from the vendor.

---

## 2. Indemnification

### 2.1 Broad, one-sided indemnification

**Pattern:** The client is required to indemnify the vendor broadly (e.g., for any claim arising from client's "use" of the product or service) without a reciprocal indemnity running from vendor to client.

**Why it matters:** A unilateral indemnity can transfer risk for claims the client did not cause, including claims arising from the vendor's own defects or conduct.

**What to check:**
- Is the indemnity mutual or one-sided?
- What triggers the client's indemnity obligation — is "use" or "breach" defined narrowly?
- Is there a carve-out for claims caused by the vendor's own negligence or misconduct?

**Most exposed:** Customer / buyer who does not have leverage to insist on mutuality.

---

### 2.2 No procedural controls on indemnity claims

**Pattern:** The indemnification provision does not require prompt notice of a claim, does not give the indemnifying party control over the defense, and does not require the indemnified party's cooperation.

**Why it matters:** Without procedural controls, the indemnified party can settle a claim at the indemnifying party's expense or prejudice the defense by giving late notice.

**What to check:**
- Is there a notice requirement with a time frame?
- Is there a defense-control right for the indemnifying party?
- Is there a restriction on the indemnified party settling without consent?
- Is there a cooperation obligation?

**Most exposed:** Any party in the indemnifying role.

---

### 2.3 Indemnity triggered by IP claims arising from client modifications

**Pattern:** The client's IP indemnity obligation is triggered by any infringement claim related to the vendor's product, including where the infringement arises from the vendor's base product rather than the client's modifications.

**Why it matters:** The client should bear indemnity risk only for infringement resulting from its own modifications or misuse, not for the vendor's baseline IP risk.

**What to check:**
- Is the IP indemnity limited to claims caused by client modifications or client-provided materials?
- Is the vendor's own IP indemnity obligation clearly stated?

**Most exposed:** Customer / licensee who deploys or integrates vendor technology.

---

## 3. Intellectual Property

### 3.1 Future-tense assignment language

**Pattern:** Work-for-hire or assignment provisions use future-tense language ("will assign," "agrees to assign," "shall vest in") rather than a present-tense grant ("hereby assigns," "is hereby assigned," "vests in").

**Why it matters:** A future promise to assign may require a further act (a subsequent written assignment instrument) to perfect the transfer of ownership `[verify jurisdiction]`. Without that further act, ownership may remain with the assignor.

**What to check:**
- Quote the assignment language verbatim.
- Is it present-tense or future-tense?
- Is there a further-assurances or cooperation clause requiring the assignor to execute additional instruments?
- Is there a power of attorney as backup?

**Most exposed:** Client receiving a work product assignment, acquirer in an M&A diligence context.

---

### 3.2 No further-assurances obligation

**Pattern:** An IP assignment clause contains no obligation on the assignor to execute additional documents or take further steps to perfect the assignment.

**Why it matters:** Without a further-assurances clause, the assignee may be unable to register the IP, record the assignment, or enforce the assignment against third parties if the assignor later becomes uncooperative.

**What to check:**
- Is a further-assurances or cooperation obligation present?
- Is there a provision addressing what happens if the assignor cannot be located or refuses to cooperate?

**Most exposed:** Assignee / buyer / commissioning party.

---

### 3.3 Broad vendor background IP carve-out

**Pattern:** The vendor retains broad rights to background IP, pre-existing tools, platforms, and methodologies used to create the deliverables, with no license back to the client to use those elements embedded in the deliverables.

**Why it matters:** If vendor-retained background IP is embedded in the deliverables, the client owns a deliverable it cannot independently use or modify without an ongoing vendor license.

**What to check:**
- What is included in the definition of background IP?
- Is there a license back to the client for use of background IP embedded in deliverables?
- Can the client's use survive termination of the contract?

**Most exposed:** Client commissioning custom work product (software, creative content, technology).

---

### 3.4 No moral rights treatment

**Pattern:** An assignment of creative works makes no mention of moral rights — no waiver, no confirmation that the jurisdiction does not recognize moral rights, and no express inclusion in the assignment.

**Why it matters:** In jurisdictions that recognize moral rights, an assignment of copyright does not automatically transfer or extinguish moral rights `[verify jurisdiction]`. An unaddressed moral rights position can complicate the assignee's ability to modify or commercialize the work.

**What to check:**
- Does the clause include a waiver of moral rights?
- Is a waiver effective in the governing jurisdiction? `[verify jurisdiction]`

**Most exposed:** Assignee of creative or software works intended for modification or commercialization.

---

### 3.5 Residual rights / residual knowledge clause

**Pattern:** The contract includes a residual rights or residual knowledge clause allowing the vendor to retain and use unaided human memory of confidential information, ideas, concepts, or methods encountered during performance.

**Why it matters:** A residual-knowledge clause can be a significant erosion of confidentiality and IP protection — the vendor's personnel can, in theory, use retained knowledge to benefit competitors.

**What to check:**
- Is the residual clause limited in scope (e.g., to genuinely unaided memory only, excluding written notes or deliberate memorization)?
- Does the residual clause carve out trade secrets or specifically identified confidential categories?
- Does the clause interact with the IP assignment — could retained knowledge be used to recreate assigned work?

**Most exposed:** Disclosing party; client commissioning proprietary development.

---

## 4. Termination

### 4.1 Asymmetric termination for convenience

**Pattern:** One party (typically the vendor) has a termination-for-convenience right with a short notice period, but the other party (typically the client) does not, or must pay a substantial termination fee.

**Why it matters:** The party without a convenience termination right is locked in, while the counterparty retains flexibility.

**What to check:**
- Are termination-for-convenience rights mutual?
- What is the required notice period?
- Are there fees payable on termination (wind-down fees, accelerated payments, break fees)?

**Most exposed:** Client locked into a long-term services or subscription relationship.

---

### 4.2 Short cure period or no cure period for material breach

**Pattern:** Termination for cause is triggered on breach with a very short cure period (or no cure period), meaning a minor operational failure can give rise to immediate termination.

**Why it matters:** A short or absent cure period can be used opportunistically to terminate a relationship that the other party wants to exit for other reasons.

**What to check:**
- Is the cure period reasonable given the nature of the obligations?
- Is the right to terminate limited to material breach, or does it extend to any breach?
- Is the "material breach" standard defined, or is it left open?

**Most exposed:** Party performing services or delivering technology who bears the risk of inadvertent breach.

---

### 4.3 Broad termination triggers beyond breach

**Pattern:** Termination rights are triggered by events beyond breach: insolvency, change of control, regulatory action, or subjective standards ("if [party] determines in its sole discretion that performance is unsatisfactory").

**Why it matters:** Broad termination triggers can be exercised to exit a deal that the counterparty simply no longer wants, regardless of fault.

**What to check:**
- List every termination trigger in the agreement.
- Flag any trigger based on subjective determination without an objective standard.
- Check whether insolvency termination may be unenforceable in the relevant jurisdiction `[verify jurisdiction]`.

**Most exposed:** Party who has invested significantly in relationship setup (data migration, integration, customization).

---

### 4.4 Inadequate wind-down and data return provisions

**Pattern:** The termination section says nothing about transition assistance, data export, data deletion timelines, return of confidential information, or continuity of access during a wind-down period.

**Why it matters:** Without wind-down provisions, a party can be cut off from data, systems, or services immediately on termination with no ability to transition.

**What to check:**
- Is there a transition assistance obligation (and for how long)?
- Is there a data export right before deletion?
- Is there a data deletion obligation and timeline?
- Are there post-termination access rights for retrieval?

**Most exposed:** Customer or client whose operations depend on access to vendor-held data or systems.

---

## 5. Fees, Payment, and Price Escalation

### 5.1 Unilateral price escalation right

**Pattern:** The vendor has the right to increase fees unilaterally on notice (or at renewal), with no cap on the increase percentage and no right for the client to terminate without penalty if the increase is unacceptable.

**Why it matters:** An uncapped unilateral escalation right gives the vendor leverage to impose significant price increases that the client cannot easily exit.

**What to check:**
- Is the escalation right unilateral or subject to mutual agreement?
- Is there a cap on annual increases (e.g., tied to a published index)?
- Does the client have a termination right if it rejects the increase?

**Most exposed:** Client in a multi-year or auto-renewing subscription or services contract.

---

### 5.2 Fees payable on termination or early exit

**Pattern:** The contract requires the client to pay all remaining fees for the unexpired term if the contract is terminated for any reason (including vendor breach), or imposes a substantial early-termination fee.

**Why it matters:** An obligation to pay all remaining fees on termination, even for vendor breach, shifts the financial risk of the relationship to the client.

**What to check:**
- Does the termination-fee obligation apply even on termination for vendor cause?
- Are there any offsets or credits for the vendor's cost savings on early exit?
- Are there acceleration provisions in other parts of the contract (e.g., payment on insolvency)?

**Most exposed:** Client in a long-term, high-value contract.

---

### 5.3 Short payment window with automatic late fees or suspension right

**Pattern:** Payment is due within a very short window (e.g., 5 or 10 days of invoice), with automatic late fees, interest, or the right to suspend services immediately on non-payment.

**Why it matters:** Short payment windows and suspension rights can be used to create leverage, particularly if the client's accounts-payable cycle is longer than the payment window.

**What to check:**
- What is the payment window?
- Is a dispute or good-faith objection sufficient to pause the payment obligation?
- What is the suspension notice period?
- Are late fees or interest rates specified, and are they commercially reasonable?

**Most exposed:** Customer with standard payment cycles; client who relies on continuous service access.

---

### 5.4 Fees due on disputed invoices

**Pattern:** The contract requires payment of all invoiced amounts — including amounts under good-faith dispute — within the payment window, with no mechanism for withholding disputed amounts pending resolution.

**Why it matters:** Requiring payment of disputed amounts removes the client's leverage to dispute invoices without facing late fees, suspension, or default.

**What to check:**
- Is there an invoice dispute mechanism?
- Can the client withhold disputed amounts without triggering late fees or default?
- What is the resolution process for invoice disputes?

**Most exposed:** Client with complex or variable invoicing arrangements.

---

## 6. Confidentiality

### 6.1 Overly broad definition of Confidential Information

**Pattern:** "Confidential Information" is defined to include essentially everything the disclosing party has ever communicated — oral, written, or observed — with no requirement of marking or identification.

**Why it matters:** An over-broad definition creates compliance difficulties and potentially exposes the receiving party to liability for normal business activities (e.g., using generally available information or independently developed knowledge).

**What to check:**
- What are the standard exclusions (publicly available information, independently developed, received from third parties without restriction)?
- Is oral information included? If so, what confirmation steps are required?
- Is there a residual knowledge carve-out (see Section 3.5)?

**Most exposed:** Receiving party who must manage and segregate a very broad confidentiality obligation.

---

### 6.2 Perpetual confidentiality obligation

**Pattern:** Confidentiality obligations survive termination indefinitely, with no sunset period.

**Why it matters:** Perpetual obligations can be overly burdensome, difficult to manage operationally over time, and may be unenforceable in some jurisdictions `[verify jurisdiction]`.

**What to check:**
- Is the confidentiality term defined?
- Are trade secrets carved out for longer or indefinite protection (which may be appropriate)?
- Does the duration align with the sensitivity of the information and market norms for the transaction type?

**Most exposed:** Receiving party with long-term operational compliance obligations.

---

### 6.3 No return-or-destroy obligation

**Pattern:** The confidentiality section contains no obligation to return or destroy confidential information on termination or at the disclosing party's request.

**Why it matters:** Without a return-or-destroy obligation, confidential information may remain with the receiving party indefinitely after the relationship ends.

**What to check:**
- Is there a return-or-destroy obligation?
- Is there a certification requirement?
- Are backup copies and legal hold exceptions addressed?

**Most exposed:** Disclosing party sharing sensitive business, technical, or personal information.

---

## 7. Data, Privacy, and Security

### 7.1 No data processing agreement or data processing terms

**Pattern:** The contract involves the vendor processing personal data on behalf of the client, but contains no data processing agreement, data processing addendum, or data-specific terms addressing processing purposes, data subject rights, security requirements, sub-processing, data return, and deletion.

**Why it matters:** Regulatory frameworks applicable to personal data processing may require a data processing agreement and may impose liability for its absence `[verify jurisdiction]`.

**What to check:**
- Does the contract involve vendor processing of personal data?
- Is there a data processing agreement or addendum?
- If a DPA is referenced but not attached, confirm it exists and is incorporated by reference.

**Most exposed:** Client acting as data controller whose regulatory obligations flow to its processors.

---

### 7.2 No breach notification obligation, or notification period is very long

**Pattern:** The vendor has no obligation to notify the client of a security breach or data incident, or the notification period is so long that it would prevent timely regulatory or customer notification.

**Why it matters:** Failure to receive timely breach notification can cause the client to miss mandatory reporting deadlines under applicable regulatory frameworks `[verify jurisdiction]`.

**What to check:**
- Is there a breach notification obligation?
- What is the notification trigger (confirmed breach vs. suspected incident)?
- Is the notification period consistent with applicable legal requirements? `[verify jurisdiction]`
- Is the notification obligation to the client, or does the vendor notify regulators directly?

**Most exposed:** Client acting as data controller or subject to sector-specific security obligations.

---

### 7.3 Broad data use rights granted to vendor

**Pattern:** The vendor is permitted to use client data for its own purposes — product improvement, analytics, benchmarking, training AI or machine learning models — with broad or unlimited scope.

**Why it matters:** Broad data use rights can expose the client's confidential business data, personal data it controls, or proprietary datasets to use for the vendor's competitive benefit.

**What to check:**
- What are the permitted uses of client data by the vendor?
- Is the scope limited to providing the contracted services?
- Can the vendor use client data to train models or develop competing services?
- If the contract involves AI or machine learning services, route to or also apply the `ai-vendor-terms-review` skill.

**Most exposed:** Client with proprietary data, personal data obligations, or competitive sensitivity about usage patterns.

---

### 7.4 No data deletion or portability right on termination

**Pattern:** The contract does not require the vendor to delete client data on termination, does not specify a deletion timeline, and does not provide a right for the client to export its data in a usable format before deletion.

**Why it matters:** Without a deletion and portability right, client data may persist indefinitely on vendor systems, the client may be unable to migrate to a replacement vendor, and residual data may create ongoing compliance or competitive risk.

**What to check:**
- Is there a data deletion obligation? When does it trigger?
- Is there a data export or portability right? In what format?
- Is there a post-termination access window for retrieval?

**Most exposed:** Client with significant data stored on or processed by vendor systems.

---

## 8. Dispute Resolution

### 8.1 Mandatory arbitration in a forum inconvenient for the client

**Pattern:** The contract requires all disputes to be resolved by arbitration in a specific city or jurisdiction that is the vendor's home forum and is inconvenient or expensive for the client.

**Why it matters:** Inconvenient forum requirements raise the cost and burden of dispute resolution, which can deter a client from pursuing legitimate claims.

**What to check:**
- Is arbitration mandatory or permissive?
- What is the venue?
- Which arbitration rules govern?
- Is there a fee allocation provision?
- Does the clause include a waiver of jury trial? `[verify jurisdiction]`

**Most exposed:** Client who is geographically distant from the vendor, or a smaller party with limited litigation resources.

---

### 8.2 Class action or collective claim waiver

**Pattern:** The dispute resolution clause waives the right to bring or participate in class action or collective proceedings.

**Why it matters:** Class action waivers may limit the client's ability to participate in or benefit from group relief `[verify jurisdiction]`.

**What to check:**
- Is a class action waiver present?
- Is it enforceable in the applicable jurisdiction? `[verify jurisdiction]`
- Does the waiver cover all types of claims or only certain categories?

**Most exposed:** Client exposed to systemic vendor conduct affecting many customers.

---

### 8.3 No carve-out for injunctive relief in court

**Pattern:** A mandatory arbitration clause does not carve out the right to seek emergency or preliminary injunctive relief in a court of competent jurisdiction.

**Why it matters:** Arbitration proceedings typically move more slowly than emergency court applications. Without a court carve-out, a party facing imminent harm (e.g., ongoing misappropriation of trade secrets) may be unable to obtain timely interim relief.

**What to check:**
- Is there a carve-out permitting either party to seek injunctive or other equitable relief in court?
- Is the carve-out mutual?

**Most exposed:** Any party whose potential harm could be irreparable and time-sensitive (IP holder, data owner).

---

## 9. Auto-Renewal

### 9.1 Auto-renewal with short or unclear non-renewal window

**Pattern:** The contract automatically renews for the same term unless a party gives notice within a window that is short, poorly defined, or measured from an unclear trigger date.

**Why it matters:** A client who misses the non-renewal window is committed to another full term, potentially with updated pricing or revised terms.

**What to check:**
- What is the auto-renewal notice window?
- When does the window open and close relative to the renewal date?
- Is the renewal for the same term length and pricing, or does pricing change?
- Does any price-escalation right apply automatically at renewal?

**Most exposed:** Client in a multi-year subscription or services contract who may not actively track renewal dates.

---

### 9.2 Renewal at modified terms

**Pattern:** On auto-renewal, the contract incorporates the vendor's then-current standard terms or pricing rather than the terms in effect at signing.

**Why it matters:** The client may be bound on renewal to materially different terms without receiving notice of specific changes.

**What to check:**
- Does the renewal lock in existing terms or incorporate updated terms?
- Is there a requirement for the vendor to notify the client of material changes before renewal?
- Is there a right to reject updated terms and terminate on shorter notice?

**Most exposed:** Client in a long-term, auto-renewing relationship with a vendor who regularly updates its standard terms.

---

## 10. Assignment and Change of Control

### 10.1 No consent right on vendor assignment or change of control

**Pattern:** The vendor may assign the contract, or undergo a change of control (acquisition, merger), without the client's consent, automatically binding the client to the acquirer or assignee.

**Why it matters:** The client may be bound to a counterparty it would not have chosen — including a competitor — with no ability to exit.

**What to check:**
- Does change of control trigger any client rights (consent right, termination right, step-in right)?
- Is assignment limited to affiliates, or is it fully unrestricted?
- Does the client have a right to terminate if change-of-control consent is not obtained?

**Most exposed:** Client in a relationship where the vendor's identity matters (key-person services, sensitive data sharing, competitive sensitivity).

---

### 10.2 Client's anti-assignment rights inconsistent with its own transaction plans

**Pattern:** The contract restricts the client's ability to assign (e.g., requires vendor consent, prohibits assignment to affiliates) in a way that would require consent for the client's own anticipated corporate transactions.

**Why it matters:** Anti-assignment restrictions can require consent from the counterparty for the client's own M&A, restructuring, or affiliate transfers, potentially complicating or blocking internal transactions.

**What to check:**
- What are the client's assignment rights?
- Is assignment to affiliates permitted?
- Is there a change-of-control trigger for the client as well as the vendor?
- Does the client have any anticipated corporate transactions that would trigger the assignment provision?

**Most exposed:** Client undergoing or anticipating M&A activity, spin-off, or internal restructuring.

---

## 11. One-Sided or Unusual Clauses

### 11.1 Vendor's unilateral right to modify the agreement

**Pattern:** The vendor reserves the right to modify the contract, its terms of service, or incorporated policies unilaterally on notice (or by posting to a website), with continued use constituting acceptance.

**Why it matters:** Unilateral modification rights can change material terms — pricing, functionality, data rights, liability allocation — without requiring the client's affirmative consent.

**What to check:**
- Is the unilateral modification right subject to any limits?
- What notice is required?
- Does the client have a right to reject modifications and terminate without penalty?
- Are any terms expressly locked (e.g., pricing for a fixed term)?

**Most exposed:** Client in a subscription or platform-services relationship governed in part by online terms.

---

### 11.2 "Sole discretion" or subjective standards

**Pattern:** Key rights or obligations are conditioned on a party's "sole discretion," "satisfaction," or "good faith" determination, with no objective standard and no right of appeal or review.

**Why it matters:** Sole-discretion standards can be used to exit obligations, withhold approvals, or exercise rights in ways that are commercially unreasonable with limited recourse for the counterparty.

**What to check:**
- What decisions or determinations are left to sole discretion?
- Is the sole-discretion standard mutual or one-sided?
- Is there a deemed-approval mechanism if a decision is not made within a specified period?

**Most exposed:** Party whose performance, approval rights, or payment depends on a subjective determination by the counterparty.

---

### 11.3 Most-favored-nation or most-favored-customer clause

**Pattern:** One party is guaranteed pricing or terms at least as favorable as those the other party offers to any other customer (or a defined set of customers), without a clear definition of what is being compared or a mechanism to verify compliance.

**Why it matters:** MFN clauses create ongoing obligations that are difficult to monitor, can restrict pricing flexibility, and may interact poorly with regulatory requirements `[verify jurisdiction]`.

**What to check:**
- Is the MFN clause clearly defined as to scope, comparator class, and verification mechanism?
- Are there exceptions for promotional pricing, volume discounts, or bundled offerings?
- Does the clause require proactive disclosure of better pricing?

**Most exposed:** Party obligated to maintain MFN compliance over a long agreement term.

---

### 11.4 Unusual representations or warranties

**Pattern:** A party is required to represent or warrant matters that are inherently forward-looking, beyond its knowledge, or outside its control — for example, that third-party technology will perform in a particular way, or that a regulatory outcome will occur.

**Why it matters:** Representations beyond a party's knowledge or control create strict-liability exposure for breach regardless of the party's reasonable efforts.

**What to check:**
- Are any representations or warranties qualified by knowledge (`"to the best of its knowledge"`) when that qualifier is appropriate?
- Are any representations inherently forward-looking or speculative?
- What is the remedy for breach of a warranty — does it go beyond the limitation-of-liability cap?

**Most exposed:** Party making representations about third-party products, regulatory approvals, or future performance.

---

### 11.5 Standstill, non-solicitation, or non-compete embedded in a commercial agreement

**Pattern:** What appears to be a routine commercial agreement contains a standstill clause, a non-solicitation of employees or customers, or a non-compete restriction buried in the confidentiality, term, or general covenants section rather than labeled as such.

**Why it matters:** Restrictive covenants may have enforceability requirements, geographic or duration limits, and regulatory implications that vary by jurisdiction `[verify jurisdiction]`. Finding them embedded in routine commercial agreements is itself a red flag.

**What to check:**
- Perform a scope check across the entire document for non-compete, non-solicit, and standstill language (see also: `nda-review` scope check).
- Flag any such provision prominently regardless of where it appears in the agreement.
- Note that enforceability of restrictive covenants is jurisdiction-dependent `[verify jurisdiction]`.

**Most exposed:** Client whose operational flexibility could be constrained post-signing or post-termination.

---

## 12. Warranties and Disclaimers

See also Section 11.4 on representations or warranties that are forward-looking or extend beyond a party's knowledge.

### 12.1 Blanket "as is" disclaimer leaving no performance recourse

**Pattern:** The counterparty disclaims all warranties — express and implied, including merchantability, fitness for a particular purpose, and non-infringement — and provides the product or service strictly "as is," with no affirmative warranty that it will perform as described or conform to its documentation.

**Why it matters:** If the counterparty makes no enforceable performance promise, the client may have no contractual remedy when the product or service fails to do what the client is paying for — even if the failure is total.

**What to check:**
- Is there any affirmative warranty (conformance to documentation, conformance to specifications, or performance for a defined period)?
- Quote the disclaimer verbatim and identify exactly which warranties are disclaimed.
- Does the disclaimer's breadth conflict with the order form, statement of work, or materials the client relied on?

**Most exposed:** Customer / buyer / licensee relying on the product or service for a business-critical function.

---

### 12.2 Warranty remedy limited to repair-or-replace as the sole remedy

**Pattern:** The only remedy for breach of warranty is the counterparty's election to repair, replace, or re-perform, with no right to a refund, no right to terminate, and no damages if repair or replacement fails.

**Why it matters:** A sole-and-exclusive repair-or-replace remedy can leave the client with no exit and no compensation if the counterparty cannot actually cure the defect.

**What to check:**
- Is the remedy expressed as "sole and exclusive"?
- Is there a fallback (refund or termination right) if repair or replacement fails or cannot be completed within a reasonable time?
- How does the remedy limitation interact with the liability cap (see Section 1)?

**Most exposed:** Customer / buyer of goods, software, or services with defined performance expectations.

---

### 12.3 Warranty period or survival too short to surface real defects

**Pattern:** The warranty period is very short relative to how long defects would realistically take to appear, or warranties expire on delivery or acceptance with no post-acceptance survival.

**Why it matters:** A warranty that expires before latent defects can reasonably be discovered provides little practical protection.

**What to check:**
- What is the warranty period, and when does it start (delivery, acceptance, go-live)?
- Is the period appropriate for the nature of the goods or services and the way defects would surface?
- Is the survival of warranties on termination addressed?

**Most exposed:** Buyer of goods or deliverables where defects may be latent.

---

## 13. Service Levels and Performance Commitments

### 13.1 No service levels for a service the client depends on

**Pattern:** The agreement is for an ongoing service (hosting, SaaS, managed services, support) but contains no uptime commitment, no response or resolution targets, and no defined performance standard.

**Why it matters:** Without a defined service level, the client has no objective standard to measure performance against and no contractual trigger for a remedy when the service degrades.

**What to check:**
- Is there any uptime, availability, or response-time commitment?
- If service levels appear in a separate SLA or exhibit, confirm it is attached and incorporated.
- Is service availability stated as a warranty, a service-level commitment, or merely aspirational language?

**Most exposed:** Customer relying on continuous service availability for operations.

---

### 13.2 Service credits framed as the sole and exclusive remedy

**Pattern:** When the counterparty misses a service level, the client's only remedy is a service credit — typically a small percentage of fees — and the contract states this is the sole and exclusive remedy for any performance failure.

**Why it matters:** Service credits are often far smaller than the client's actual loss from an outage. As a sole-and-exclusive remedy, they can foreclose any other claim for chronic or severe underperformance.

**What to check:**
- Are service credits expressed as the sole and exclusive remedy?
- Is there a right to terminate for chronic or material SLA failure, separate from the credit mechanism?
- Must the client claim credits within a short window or forfeit them?

**Most exposed:** Customer whose realistic outage losses far exceed a fee-percentage credit.

---

### 13.3 Exclusions that swallow the service-level commitment

**Pattern:** The uptime or availability commitment is subject to broad exclusions — scheduled maintenance, emergency maintenance, third-party failures, "force majeure," anything outside the counterparty's "direct control" — wide enough to exclude most realistic downtime.

**Why it matters:** A high headline availability figure can be meaningless if the definition of measured downtime excludes the events that actually cause outages.

**What to check:**
- List every exclusion from the availability calculation.
- Is scheduled maintenance capped as to frequency, duration, notice, and off-peak windows?
- Does the exclusion for third-party or "outside our control" events swallow the commitment?

**Most exposed:** Customer relying on the headline availability figure without reading the measurement definition.

---

## 14. Insurance

### 14.1 No insurance requirement on the counterparty

**Pattern:** The agreement imposes no obligation on the counterparty to carry insurance, even though the counterparty's performance creates risks (property damage, bodily injury, professional error, data breach) that insurance would ordinarily backstop.

**Why it matters:** Without an insurance requirement, the client's ability to actually recover on an indemnity or damages claim depends entirely on the counterparty's balance sheet. An uninsured or judgment-proof counterparty makes a strong indemnity worth little.

**What to check:**
- Is any insurance required?
- Do the required coverage types match the risks the counterparty's performance creates (commercial general liability, professional liability / errors and omissions, cyber / data-breach, workers' compensation, auto)?
- Are coverage limits specified, and are they meaningful relative to the realistic exposure?

**Most exposed:** Client relying on the counterparty's indemnity or damages obligations as a real source of recovery.

---

### 14.2 Insurance mechanics missing (additional insured, certificates, notice)

**Pattern:** The contract requires coverage but omits the operational mechanics: no additional-insured status for the client, no certificate-of-insurance delivery requirement, no advance notice of cancellation or material reduction, no primary-and-noncontributory language.

**Why it matters:** A bare requirement to "carry insurance" without these mechanics gives the client no visibility into whether coverage exists and no direct rights against the policy.

**What to check:**
- Is the client named (or required to be named) as an additional insured where appropriate?
- Must the counterparty deliver certificates of insurance, including on renewal?
- Is there a notice obligation if coverage lapses, is cancelled, or is materially reduced?

**Most exposed:** Client that would need to claim against the counterparty's policy.

---

### 14.3 Insurance offered as a substitute for liability allocation

**Pattern:** The counterparty points to its insurance to justify a low liability cap or broad limitation, but the insurance requirement and the liability cap are not aligned — the cap is below the coverage limit, or the policies exclude the very risks the indemnity covers.

**Why it matters:** Insurance and contractual liability allocation are separate. A policy the client cannot reach, or that excludes the relevant risk, does not cure a deficient liability clause.

**What to check:**
- Does the liability cap align with the insurance limits, or is the cap far lower?
- Do the required policies actually cover the indemnified risks?
- Is the insurance a real backstop, or a negotiating talking point?

**Most exposed:** Client persuaded to accept a low cap on the strength of insurance that may not respond.

---

## 15. Audit and Inspection Rights

### 15.1 No audit right where verification matters

**Pattern:** The client has obligations it needs to confirm the counterparty is meeting — security controls, data handling, regulatory compliance, royalty or usage-based fee calculations — but the contract gives the client no right to audit, inspect, or obtain compliance evidence.

**Why it matters:** Without an audit or reporting right, the client must take the counterparty's compliance on trust and may be unable to detect a breach until it causes harm.

**What to check:**
- Does the client have any audit, inspection, or reporting right?
- For security and data obligations, is there a right to obtain third-party audit reports or certifications in place of, or alongside, a direct audit?
- Are there obligations whose breach the client could not otherwise detect?

**Most exposed:** Client with regulatory exposure, usage-based pricing, or sensitive-data obligations flowing to the counterparty.

---

### 15.2 One-sided audit right running against the client

**Pattern:** The counterparty has a broad right to audit the client's use of a product or service (a license "true-up" audit), often including entry to premises, inspection of systems, and back-charges for any underpayment — with no reciprocal right and few limits.

**Why it matters:** A broad vendor audit right can be used to generate surprise back-charges, disrupt operations, and create leverage at renewal.

**What to check:**
- What triggers the audit right, and how often can it be exercised?
- Is there advance-notice, business-hours, scope, and confidentiality protection?
- Who bears audit costs, and what are the consequences of an adverse finding?

**Most exposed:** Licensee or customer subject to usage-based or seat-based licensing.

---

### 15.3 Audit right with no procedural limits

**Pattern:** An audit right (in either direction) is granted with no limits on notice, frequency, scope, duration, location, who conducts it, the confidentiality of what is reviewed, or who pays.

**Why it matters:** An unbounded audit right is disruptive and can expose the audited party's sensitive information. Procedural limits are what make an audit right workable.

**What to check:**
- Notice period, frequency cap, scope limitation, and business-hours restriction.
- Confidentiality protection for information reviewed during the audit.
- Cost allocation, including any shifting rule if the audit finds a material discrepancy.

**Most exposed:** Whichever party is subject to the audit.

---

## 16. Publicity, Marketing, and Use of Name

### 16.1 Counterparty may use the client's name, marks, or a case study without consent

**Pattern:** The counterparty is permitted to use the client's name, logo, or trademarks, to identify the client as a customer, or to publish a case study or testimonial — without the client's prior written consent for each use.

**Why it matters:** Unconsented use of the client's name and marks can create unwanted public association, implied endorsement, brand-control problems, and trademark-licensing issues.

**What to check:**
- Does the counterparty need the client's prior written consent for each public use?
- Is any permitted use narrowly limited (e.g., to a customer list) and revocable?
- Is the right mutual, and does it survive termination?

**Most exposed:** Client sensitive about brand, public association, or confidentiality of the relationship.

---

### 16.2 No mutual control over public statements about the relationship

**Pattern:** The contract is silent on press releases and public announcements, or allows one party to announce the deal unilaterally.

**Why it matters:** A unilateral announcement can disclose a relationship the client wanted kept confidential, or mischaracterize it.

**What to check:**
- Is there a mutual prior-approval requirement for press releases and public statements?
- Are disclosures required by law or stock-exchange rule carved out?

**Most exposed:** Client with confidentiality, competitive, or regulatory sensitivity about the relationship.

---

## 17. Non-Solicitation and Non-Competition

This section expands on Section 11.5, which flags restrictive covenants embedded in routine commercial agreements. Enforceability of restrictive covenants is highly jurisdiction-dependent and, in some jurisdictions, restricted or prohibited `[verify jurisdiction]`.

### 17.1 Non-compete restricting the client's ordinary business

**Pattern:** The client is restricted from competing with the counterparty, from working with the counterparty's competitors, or from offering certain products or services — in a way that reaches the client's ordinary business activity.

**Why it matters:** A non-compete can constrain the client's core operations, future deals, and strategic flexibility, often far beyond the value of the contract.

**What to check:**
- What activity is restricted, for how long, and in what geography or market?
- Does the restriction reach beyond the subject matter of this contract?
- Is the restriction mutual, and is it enforceable in the governing jurisdiction `[verify jurisdiction]`?

**Most exposed:** Client whose business overlaps with the counterparty's market.

---

### 17.2 Overbroad non-solicitation of employees

**Pattern:** A non-solicit of employees has no carve-out for general advertising, job postings, or unsolicited inbound applications, and/or covers all employees rather than those connected to the engagement.

**Why it matters:** An overbroad non-solicit can be triggered by ordinary recruiting and restrict the client's hiring well beyond the people connected to the deal.

**What to check:**
- Is there a carve-out for general solicitations not targeted at the counterparty's staff, and for unsolicited applicants?
- Is the covered population limited to employees connected to the engagement?
- What is the duration, and does it run from termination?

**Most exposed:** Client that recruits in the same talent market as the counterparty.

---

### 17.3 Customer non-solicitation or exclusivity embedded in the deal

**Pattern:** The agreement restricts the client from soliciting, serving, or contracting with certain customers or categories of customers, or grants the counterparty exclusivity.

**Why it matters:** Customer non-solicits and exclusivity provisions can foreclose revenue opportunities and lock the client out of markets.

**What to check:**
- What customers or segments are covered, and for how long?
- Is exclusivity reciprocal, and is it tied to minimum commitments?
- Flag the provision prominently regardless of where it appears.

**Most exposed:** Client whose growth depends on access to the restricted customers or markets.

---

## 18. Governing Law and Choice of Forum

See also Section 8 (Dispute Resolution) for arbitration-specific patterns.

### 18.1 Governing law or forum with no connection to the parties or transaction

**Pattern:** The agreement selects a governing law or an exclusive forum that has no relationship to either party, the place of performance, or the subject matter.

**Why it matters:** An unrelated governing law can introduce unfamiliar legal rules; an unrelated or distant forum raises the cost and burden of any dispute and can deter the client from enforcing its rights. A choice with no reasonable connection may also face enforceability questions `[verify jurisdiction]`.

**What to check:**
- What law governs, and what is the exclusive forum or venue?
- Is there a reasonable connection between the chosen law or forum and the deal?
- Is the forum the counterparty's home turf and inconvenient for the client?

**Most exposed:** Client distant from the chosen forum, or a smaller party with limited litigation resources.

---

### 18.2 Inconsistent or split governing-law, forum, and arbitration provisions

**Pattern:** Different provisions point in different directions — a governing-law clause naming one jurisdiction, a forum-selection clause naming another, an arbitration clause naming a third seat — or incorporated documents (online terms, exhibits) carry their own conflicting clauses.

**Why it matters:** Inconsistent dispute provisions create uncertainty about where and under what law a dispute would proceed, and can trigger expensive threshold litigation about the dispute clause itself.

**What to check:**
- Do the governing-law, forum-selection, and arbitration clauses align?
- Do incorporated or online terms contain their own, conflicting clauses?
- Is there a clear order-of-precedence rule?

**Most exposed:** Either party, if a dispute arises.

---

### 18.3 Jury-trial waiver

**Pattern:** The agreement waives the right to a jury trial for any dispute.

**Why it matters:** A jury-trial waiver changes who decides the facts in any litigation. Its enforceability and effect vary by jurisdiction `[verify jurisdiction]`.

**What to check:**
- Is a jury-trial waiver present, and is it mutual?
- Is it enforceable under the governing law `[verify jurisdiction]`?

**Most exposed:** Either party; the effect depends on the dispute and the jurisdiction.

---

## Reviewer Notes

- A red flag is a prompt to look closely and flag for attorney attention — not a conclusion that a clause is unenforceable or unacceptable.
- Whether a flagged clause is a problem depends on the client's role, leverage, business context, and risk tolerance — all of which are for the attorney to assess.
- This catalog is not exhaustive. Unusual or deal-specific provisions not listed here may still warrant a flag in the "Unusual or One-Sided Clauses" category of the risk matrix.
- See `skills/contracts/contract-risk-review/SKILL.md` for the full clause-by-clause review workflow.
- See `skills/contracts/nda-review/SKILL.md` for the NDA-specific scope check and risk table workflow.
