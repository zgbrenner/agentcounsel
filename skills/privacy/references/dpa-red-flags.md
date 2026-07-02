> Shared reference material supporting the AgentCounsel privacy skills, used to help produce draft legal work product for attorney review — not legal advice.

# DPA Red-Flag Catalog

This catalog lists clause patterns and structural features that a reviewer should actively scan for during a data processing agreement (DPA) review. Each entry describes the pattern, why it matters, what to check, and which client roles are most exposed. The catalog is organized by DPA topic to support a Red Flags Quick Scan output within the privacy skills, principally `skills/privacy/dpa-review/SKILL.md`.

Every pattern in this catalog is a **contract-language pattern** — a description of what the document says, never a statement of what any law requires. Where a legal regime is relevant to why a pattern matters, the regime is described generically and flagged `[Verify current law]` or `[verify jurisdiction]`. Which privacy laws apply, and what they mandate, are always attorney-verification items.

This catalog is a review aid. It identifies what to look for and why. Whether a flagged pattern is actually problematic depends on the specific contract language, the client's role (controller, processor, or sub-processor), the data involved, the business context, and attorney judgment. Every flagged item is a candidate for attorney verification — not a legal conclusion.

Each topic section closes with a **Preferred position / Fallback position** pair in the style of `skills/contracts/references/fallback-language-bank.md`. These are directions for counsel to articulate in an issue list — not clause language, and not positions to adopt without attorney confirmation. They are written from the perspective of a client acting as controller (the customer); where the client is the processor, the directions often invert — confirm the client's role before applying them.

---

## How to Use This Catalog

For each topic section below:

1. Locate the relevant provision in the DPA under review (or note its absence — a missing provision is itself a red flag in many contexts).
2. Check the pattern description against the actual language.
3. If the pattern is present, add the item to the risk table and the prioritized issue list.
4. Note which client roles are most exposed and whether the client's role matches the exposure profile.
5. Flag every finding for attorney review; do not resolve ambiguity silently.

---

## 1. Processing Scope and Instructions

### 1.1 Vague or open-ended processing purposes

**Pattern:** The description of processing purposes is generic ("to provide the services," "for business purposes," "as necessary") with no annex or schedule identifying the data categories, data subjects, and specific processing activities.

**Why it matters:** A vague scope gives the processor room to expand processing without a contract change, and leaves the controller unable to demonstrate that processing is confined to documented purposes — a common expectation under data-protection regimes `[Verify current law]`.

**What to check:**
- Is there a processing-description annex, and is it completed rather than left in template form?
- Are data categories, data subject categories, and purposes specific enough to bound the processing?
- Does the described scope match the commercial relationship as the user describes it?

**Most exposed:** Controller-client whose regulatory accountability depends on documented, bounded processing.

---

### 1.2 Processing beyond documented instructions

**Pattern:** The processor may process personal data for purposes it determines, "as otherwise permitted by the agreement," or wherever it deems processing "reasonably necessary" — rather than only on the controller's documented instructions with narrow carve-outs (such as processing required by law).

**Why it matters:** If the processor can process outside the controller's instructions, the controller loses control over data it remains accountable for, and the processor may in substance be acting as an independent controller for that processing `[Verify current law]`.

**What to check:**
- Quote the instructions clause verbatim.
- List every carve-out from the instructions-only obligation and assess how bounded each is.
- Is the processor obliged to notify the controller if it believes an instruction conflicts with applicable law?

**Most exposed:** Controller-client; sub-processor arrangements where instructions flow through an intermediate processor.

---

### 1.3 Processor discretion over the means of processing

**Pattern:** The DPA gives the processor discretion to determine not just technical implementation details but the essential means of processing — what data is collected, how long it is kept, or who it is disclosed to.

**Why it matters:** Discretion over essential means can blur the controller/processor allocation the DPA is built on; the party determining purposes and essential means may bear controller-level responsibility regardless of the document's labels `[Verify current law]`.

**What to check:**
- Which decisions does the document reserve to the controller, and which does it leave to the processor?
- Does the discretion extend to retention periods, disclosure recipients, or data collection scope?
- Flag the role designations as `[CONFIRM: role allocation under applicable law]`.

**Most exposed:** Controller-client relying on the document's labels; either party if the role allocation is challenged.

**Preferred position:** Processing is confined to the controller's documented instructions, with a completed processing-description annex and only narrow, law-required carve-outs; the controller retains all decisions on purposes and essential means.

**Fallback position:** The instructions clause stays as drafted but the processing annex is completed with specific data categories, subjects, and purposes, and a notification obligation is added if the processor intends any processing outside the annex.

---

## 2. Vendor Own-Use Rights

### 2.1 Broad rights to use data for product improvement, analytics, or benchmarking

**Pattern:** The vendor may use personal data (or "service data," "usage data," or similar) for its own purposes — improving its products, analytics, benchmarking, research — framed as a permitted use rather than a separately agreed processing purpose.

**Why it matters:** Own-use rights convert the vendor from a processor acting on instructions into a party processing for its own purposes, potentially making it an independent controller for that processing and exposing the client's data to the vendor's competitive benefit `[Verify current law]`.

**What to check:**
- Quote every permitted-use provision verbatim, including any that sit outside the DPA in the main agreement or a policy incorporated by reference.
- Does the own-use right cover personal data, or only genuinely non-personal telemetry?
- Is the own-use right revocable, opt-out, or unconditional?

**Most exposed:** Controller-client with regulatory accountability for the data; any client with competitive sensitivity about usage patterns.

---

### 2.2 Model-training rights

**Pattern:** The vendor may use client data — sometimes framed as "content," "inputs," or "outputs" — to train, fine-tune, or improve machine-learning or AI models, either expressly or through a broad "improve our services" formulation.

**Why it matters:** Training rights can embed the client's personal data and confidential information into models the vendor deploys for other customers, with unclear deletion, extraction, and confidentiality consequences.

**What to check:**
- Is model training expressly addressed — permitted, excluded, or silent?
- If permitted, is it limited to de-identified or aggregated data, and how are those terms defined (see 2.3)?
- If the contract involves AI or machine-learning services, route to or also apply `skills/ai-governance/ai-vendor-terms-review/SKILL.md`.

**Most exposed:** Controller-client; client with proprietary datasets or sensitive personal data categories.

---

### 2.3 "Aggregated / anonymized / de-identified" carve-outs with weak definitions

**Pattern:** The vendor may freely use data once it is "aggregated," "anonymized," or "de-identified," but the DPA does not define those terms, defines them circularly, or sets a standard weaker than irreversibility (e.g., mere removal of direct identifiers).

**Why it matters:** Whether data is genuinely anonymous is a demanding, regime-specific question `[Verify current law]`. A weak definition lets the vendor treat re-identifiable data as outside the DPA's protections entirely, and the carve-out can swallow the own-use restrictions.

**What to check:**
- Quote the definition (or note its absence).
- Does the standard require that data cannot reasonably be re-identified or attributed to the client or any individual?
- Does the carve-out remove the data from confidentiality obligations as well as data-protection obligations?

**Most exposed:** Controller-client; disclosing party whose confidential business data rides along with the personal data.

**Preferred position:** The vendor uses personal data solely to provide the contracted services; product improvement, analytics, benchmarking, and model training are excluded unless separately and expressly agreed, and any aggregation carve-out requires data that cannot reasonably be re-identified or attributed to the client.

**Fallback position:** Own-use is limited to aggregated, de-identified data under a defined irreversibility standard, with model training on personal data expressly excluded.

---

## 3. Sub-Processor Management

### 3.1 Blanket authorization without notice or objection right

**Pattern:** The controller gives general authorization for sub-processors with no obligation on the processor to give advance notice of additions or replacements, and no right for the controller to object.

**Why it matters:** The controller remains accountable for the processing chain but has no visibility into, or control over, who is in it. Some regimes expect a notice-and-objection mechanism where general authorization is used `[Verify current law]`.

**What to check:**
- Is authorization specific (prior written approval per sub-processor) or general?
- If general: is there advance notice of changes, a defined notice period, and an objection right?
- What happens after an objection — a workaround obligation, a termination right for the affected services, or nothing?

**Most exposed:** Controller-client; processor-client whose upstream controller expects flow-through controls.

---

### 3.2 Sub-processor list "subject to change" without a stable reference

**Pattern:** The DPA points to a sub-processor list on a website that the vendor may update at any time, with no notification mechanism, no snapshot at signature, and continued use deemed acceptance of changes.

**Why it matters:** A mutable, un-notified list makes the controller's diligence at signature stale immediately and shifts the burden of monitoring to the client.

**What to check:**
- Is the current list attached or referenced with a date or version?
- Is there a subscription or notification mechanism for changes, and does the objection window run from actual notice?
- Does the DPA deem continued use to be consent to new sub-processors?

**Most exposed:** Controller-client subject to vendor-oversight expectations.

---

### 3.3 No flow-down of equivalent obligations

**Pattern:** The DPA does not require the processor to impose data-protection obligations on sub-processors equivalent to those in the DPA, or waters the standard down to "substantially similar," "appropriate," or silence — and does not state that the processor remains liable for its sub-processors.

**Why it matters:** Without equivalent flow-down and retained processor liability, the protections the controller negotiated stop at the first tier while the data travels further.

**What to check:**
- Quote the flow-down standard verbatim ("same," "equivalent," "no less protective," or weaker).
- Does the processor remain fully liable to the controller for sub-processor acts and omissions?
- Do transfer-mechanism obligations (Section 7) also flow down to sub-processors?

**Most exposed:** Controller-client; any client whose data will foreseeably pass through multiple tiers.

**Preferred position:** Specific or general authorization with advance notice of changes, a meaningful objection right with a termination fallback for affected services, a dated sub-processor list, flow-down of obligations no less protective than the DPA, and full processor liability for sub-processors.

**Fallback position:** General authorization stays, but with a defined advance-notice period running from actual notice, an objection right, and an express flow-down and retained-liability clause.

---

## 4. Security Commitments

### 4.1 Undefined "appropriate measures"

**Pattern:** The security clause promises only "appropriate technical and organizational measures" (or "reasonable security") with no annex, no referenced standard or certification, and no description of controls.

**Why it matters:** An undefined standard is difficult to enforce, gives the client no objective baseline to measure against, and leaves the client unable to demonstrate diligence over its processor `[Verify current law]`.

**What to check:**
- Is there a security annex or exhibit, and is it completed rather than left in template form?
- Is any recognized framework or certification referenced (e.g., an information-security management standard or independent audit report), and is conformance a contractual commitment or merely descriptive?
- Are encryption, access control, personnel confidentiality, and testing addressed at all?

**Most exposed:** Controller-client; client processing sensitive data categories.

---

### 4.2 Unilateral right to modify or weaken security measures

**Pattern:** The vendor may update its security measures "from time to time," with the only constraint (if any) being that changes do not "materially degrade" security — as determined by the vendor.

**Why it matters:** A self-judged modification right means the security posture the client diligenced at signature is not the one it is contractually entitled to later.

**What to check:**
- Who judges whether a change degrades security, and by what standard?
- Is there notice of material changes and a client right to object or terminate?
- Does the clause anchor security to a baseline (the annex as of the effective date) or float it entirely?

**Most exposed:** Controller-client that performed security diligence at signature; regulated clients with security-program obligations.

---

### 4.3 No audit right, or audit limited to summaries

**Pattern:** The DPA grants no audit or inspection right, or limits the client to receiving vendor-selected summaries, certifications "upon request," or a right to submit written questions — with no path to an independent audit even after an incident.

**Why it matters:** The client must take the vendor's compliance on trust and may be unable to satisfy its own oversight expectations `[Verify current law]`. Accepting third-party reports as the ordinary course is common; accepting them as the *only* course, with no escalation path, is the red flag.

**What to check:**
- Is there any audit right? What triggers it, how often, on what notice, and at whose cost?
- Are third-party audit reports a substitute for, or a supplement to, a direct audit right?
- Is there an enhanced or expedited audit right following a security incident?

**Most exposed:** Controller-client with regulatory oversight expectations; client in a regulated sector.

---

### 4.4 Certification substitution without a compliance commitment

**Pattern:** The DPA points to the vendor's certifications (security or privacy frameworks) *in place of* substantive security obligations — the vendor promises to "maintain certification" but makes no commitment that the certified controls actually apply to the client's data or that lapses will be notified.

**Why it matters:** A certification describes an audit outcome at a point in time; it is not itself an enforceable control set. If certification lapses or its scope excludes the relevant systems, the client may have no security commitment at all.

**What to check:**
- Does the certified scope cover the services and systems processing the client's data?
- Is there an obligation to notify the client if certification lapses, is suspended, or is narrowed?
- Are there substantive security obligations that survive independently of the certification?

**Most exposed:** Client that relied on the certification during procurement diligence.

**Preferred position:** A completed security annex with defined controls anchored to a baseline, changes permitted only if they do not reduce protection (judged objectively), audit rights (third-party reports in the ordinary course, direct audit on reasonable notice and after incidents), and notice of any certification lapse.

**Fallback position:** Third-party audit reports as the standard evidence, but with an anchored security baseline, an incident-triggered direct audit right, and lapse notification.

---

## 5. Breach Notification

### 5.1 No outer time bound on notification

**Pattern:** The processor must notify the controller of a personal data breach "without undue delay," "promptly," or "as soon as reasonably practicable" — with no outer bound in hours or days.

**Why it matters:** The controller may face short regulatory and individual notification expectations that run from the controller's awareness `[Verify current law]`. An unbounded processor obligation can consume the controller's entire window before the controller even knows. Do not compute or assert what any regime's window is — mark stated timeframes `[CONFIRM: verify deadline under applicable law]`.

**What to check:**
- Quote the notification timing verbatim; note whether any stated period is measured from discovery, confirmation, or occurrence.
- Is there an obligation to provide updating information as the investigation develops?
- Does the required notification content support the controller's own notifications (nature, categories, approximate numbers, measures taken)?

**Most exposed:** Controller-client bearing downstream notification obligations.

---

### 5.2 Notification triggered only by a "confirmed" breach

**Pattern:** The notification duty is triggered only when the vendor has *confirmed* a breach (or completed its investigation), not on discovery or reasonable suspicion of an incident.

**Why it matters:** Confirmation can take weeks. A confirmed-only trigger lets the vendor's investigation timeline absorb the period in which the controller most needs to act, and gives the vendor an incentive to delay confirmation.

**What to check:**
- What is the trigger: suspected incident, discovery, determination, or confirmation?
- Who decides when a breach is "confirmed," and against what standard?
- Is there any interim-notice obligation while an incident is under investigation?

**Most exposed:** Controller-client; any client whose incident-response plan depends on early warning.

---

### 5.3 Notice conditioned on the vendor's fault determination or scoped to the vendor's systems only

**Pattern:** Notification is required only for breaches "caused by vendor's breach of this DPA," only for the vendor's "own systems" (excluding sub-processors), or is subject to the vendor's determination that the incident is material or notifiable.

**Why it matters:** Fault, system boundaries, and materiality are exactly what is unknown early in an incident. Conditioning notice on the vendor's self-assessment of them means the controller learns late or never — including of sub-processor incidents in its own processing chain.

**What to check:**
- Does the notification duty cover incidents at sub-processors?
- Is notice conditioned on fault, materiality, or a legal-notifiability determination made by the vendor?
- Does the DPA restrict the controller from notifying regulators or individuals without vendor consent (a separate, serious flag)?

**Most exposed:** Controller-client; processor-client passing obligations downstream to sub-processors.

**Preferred position:** Notification of security incidents affecting the client's data (including at sub-processors) without undue delay after discovery and within a short, defined outer bound `[CONFIRM: verify deadline under applicable law]`, with content sufficient to support the controller's own notifications, updating information as the investigation develops, and no vendor veto over the controller's regulatory or individual notifications.

**Fallback position:** A defined outer bound from the vendor's determination that a breach occurred, paired with an interim-notice obligation on discovery of a suspected incident and express coverage of sub-processor incidents.

---

## 6. Data Subject Request Support

### 6.1 No assistance obligation

**Pattern:** The DPA is silent on assisting the controller with data subject requests (access, deletion, correction, portability, objection), or requires only that the processor forward requests it receives.

**Why it matters:** The controller may be unable to fulfill requests without the processor's cooperation, since the processor holds or controls the data. Assistance obligations are a common regulatory expectation for processing arrangements `[Verify current law]`.

**What to check:**
- Is there an affirmative assistance obligation, or only a forwarding duty?
- Does the assistance cover the full range of rights addressed in the applicable framework as stated in the document?
- Are there self-service tools, and does the DPA commit to their continued availability?

**Most exposed:** Controller-client facing request deadlines it cannot meet alone. See `skills/privacy/dsar-workflow/SKILL.md` for handling an actual incoming request.

---

### 6.2 Assistance only for a fee, or at the vendor's discretion

**Pattern:** Assistance with data subject requests is provided "at controller's cost," at "then-current professional services rates," or only as the vendor "may reasonably determine."

**Why it matters:** Discretionary or fee-gated assistance converts a compliance dependency into a commercial negotiation at the worst moment — when a deadline is already running. Some cost allocation can be commercially reasonable; unbounded rates and discretion are the red flag.

**What to check:**
- Is baseline assistance (or self-service tooling) included, with fees only for extraordinary requests?
- Are fees bounded (rate card, reasonableness standard) or open-ended?
- Can the vendor decline assistance, and on what standard?

**Most exposed:** Controller-client with consumer-scale request volumes.

---

### 6.3 Vendor discretion to respond directly to data subjects

**Pattern:** The vendor reserves the right to respond directly to data subject requests concerning data it processes for the client, or is not required to await the controller's instructions before acting on a request.

**Why it matters:** The controller owns the relationship with, and the response obligations toward, its data subjects. A vendor that responds directly can waive positions, disclose data, or delete data the controller needed to retain.

**What to check:**
- Is the processor required to redirect requests to the controller and act only on instructions?
- Is there a carve-out where the vendor is itself legally compelled to respond `[Verify current law]`?
- Does the DPA address requests the vendor receives about the client's data subjects in its capacity as an independent controller of adjacent data?

**Most exposed:** Controller-client; any client with contested or legally sensitive request scenarios.

**Preferred position:** An affirmative obligation to assist with the full range of data subject rights, requests redirected to the controller and actioned only on its instructions, baseline assistance included in fees, and any charges bounded and limited to extraordinary requests.

**Fallback position:** Assistance delivered primarily through defined self-service tools, with a cooperation obligation and bounded reasonable fees for what the tools cannot do.

---

## 7. Cross-Border Transfers

For any DPA where transfers are material, route the deep analysis to `skills/privacy/cross-border-transfer-review/SKILL.md`. The entries below are quick-scan patterns only.

### 7.1 Transfer mechanism unstated

**Pattern:** The DPA contemplates or permits processing in, or access from, other countries but identifies no transfer mechanism (standard contractual clauses, adequacy reliance, binding corporate rules, or another instrument).

**Why it matters:** Cross-border transfers of personal data commonly require a recognized legal mechanism `[Verify current law]`. A DPA that is silent leaves the lawful basis for the transfer — and the allocation of responsibility for establishing one — unaddressed. Do not assess mechanism validity; flag it for attorney review.

**What to check:**
- Where will data be processed and from where can it be accessed (including support access)?
- Is any mechanism named, incorporated, or attached?
- Who is responsible for putting a mechanism in place if one is needed?

**Most exposed:** Controller-client exporting data; processor-client importing it.

---

### 7.2 Unilateral relocation right

**Pattern:** The vendor may change processing locations, move data to new countries, or relocate hosting regions at its discretion, with no notice, no obligation to maintain a valid transfer mechanism for the new location, and no client objection right.

**Why it matters:** A relocation can invalidate the transfer analysis done at signature and can move data into jurisdictions the client's own customers, regulators, or contracts prohibit.

**What to check:**
- Is there a defined list of processing locations, and is it binding or illustrative?
- Does relocation require notice, an updated transfer mechanism, or consent?
- Do location commitments flow down to sub-processors?

**Most exposed:** Controller-client with data-residency commitments to its own customers or regulators.

---

### 7.3 Missing or template-form annexes to the transfer mechanism

**Pattern:** Standard contractual clauses or an equivalent instrument are incorporated by reference, but the required annexes (parties, data description, security measures) are absent, incomplete, or left in template form — or the mechanism's text has been modified.

**Why it matters:** An incorporated mechanism with empty annexes may not accurately document the transfer, and material modification of standard-mechanism text is generally constrained by the mechanism's own terms `[Verify current law]`. Both are flags for specialist review, alongside the absence of any referenced transfer impact assessment where one is doctrinally expected `[verify jurisdiction]`.

**What to check:**
- Are the annexes present and completed with this deal's actual facts?
- Is the mechanism incorporated as-issued or with modifications?
- Is a transfer impact assessment or supplementary-measures analysis referenced or attached?

**Most exposed:** Both parties — a defectively documented mechanism protects neither.

**Preferred position:** Processing locations are defined and binding, a recognized transfer mechanism is incorporated as-issued with completed annexes, relocations require notice and a maintained mechanism, and location commitments flow down to sub-processors — with mechanism validity routed to counsel via `skills/privacy/cross-border-transfer-review/SKILL.md`.

**Fallback position:** Locations stay flexible, but any relocation requires advance notice, continuation of a valid transfer mechanism as a condition, and an objection or termination right for the affected services.

---

## 8. Retention and Deletion

### 8.1 Deletion at the vendor's discretion or on undefined timelines

**Pattern:** On termination (or on request), the vendor deletes data "in accordance with its policies," "within a reasonable period," or "in the ordinary course," rather than within a defined period at the controller's election of return or deletion.

**Why it matters:** The controller remains accountable for data it can no longer see or control. Discretionary deletion leaves the client unable to state when its data ceased to exist on vendor systems.

**What to check:**
- Who elects between return and deletion — the controller or the vendor?
- Is there a defined deletion period from termination or request?
- Do deletion obligations extend to sub-processors?

**Most exposed:** Controller-client; client with retention commitments to its own customers.

---

### 8.2 Backup carve-outs with no expiry

**Pattern:** Deletion obligations except "data in backup or archival systems," with no commitment to expire backups on a defined cycle, no continued protection for retained copies, and no prohibition on restoring them to active use.

**Why it matters:** An open-ended backup carve-out means "deleted" data persists indefinitely. Some backup latency is operationally normal; the red flag is a carve-out with no cycle, no continuing protections, and no restore restriction.

**What to check:**
- Is there a defined backup-expiry cycle after which the carve-out ends?
- Do the DPA's security and confidentiality obligations expressly continue for retained copies?
- Is the vendor barred from restoring backed-up client data except for disaster recovery?

**Most exposed:** Controller-client; disclosing party under parallel confidentiality return-or-destroy duties.

---

### 8.3 No deletion certification

**Pattern:** The DPA requires deletion but gives the client no right to a written certification (or other evidence) that deletion occurred, including at sub-processors.

**Why it matters:** Without certification, the client has no record to point to when its own regulators, customers, or litigation adversaries ask what happened to the data.

**What to check:**
- Is certification available on request, and does it cover sub-processors?
- Does any legal-retention exception state that retained data remains subject to the DPA's protections and is deleted when the retention basis ends?
- Does the deletion clause interact consistently with the backup carve-out (8.2)?

**Most exposed:** Controller-client with audit-trail or vendor-offboarding obligations.

**Preferred position:** Controller elects return or deletion; deletion completes within a defined period including at sub-processors; backup copies expire on a defined cycle and remain protected and non-restorable meanwhile; deletion is certified on request.

**Fallback position:** Deletion on request within a defined period, a defined backup-expiry cycle with continuing protections, and certification on the client's written request.

---

## 9. Liability and Indemnity Interplay

Read this section together with the main commercial agreement — the DPA's liability posture cannot be assessed from the DPA alone. If the main agreement is not available, flag the gap prominently.

### 9.1 Privacy and security liability disclaimed or folded under a low general cap

**Pattern:** The DPA states that all liability under it is subject to the main agreement's limitation of liability, and the main agreement's general cap (often trailing fees) applies to data-protection breaches with no carve-out or super-cap — or the DPA disclaims the vendor's liability for data incidents outright.

**Why it matters:** Realistic exposure from a data breach — regulatory penalties, individual claims, notification costs, downstream customer claims — can exceed a fee-based cap by orders of magnitude. A cap sized for service-failure risk effectively transfers breach risk to the client.

**What to check:**
- Trace the liability chain: what does the DPA say, what does the main agreement say, and which controls on conflict?
- Is there a carve-out or elevated super-cap for data-protection or security breaches? Compare it to a realistic exposure estimate.
- Are regulatory penalties, notification costs, and third-party claims excluded as "indirect" or "consequential" damages?

**Most exposed:** Controller-client bearing regulatory and customer-facing exposure it cannot pass back.

---

### 9.2 One-way indemnity or allocation untethered from responsibility

**Pattern:** The client indemnifies the vendor for data-protection claims (including claims arising from the vendor's own processing failures), with no reciprocal indemnity — or the DPA is silent on how liability for regulatory penalties and data subject claims is allocated between the parties.

**Why it matters:** Some regimes allocate liability between controller and processor based on responsibility, and permit recovery between the parties `[Verify current law]`. A contractual allocation that runs only one way, or silence, can leave the client holding losses caused by the vendor.

**What to check:**
- Is there any indemnity for data-protection claims, and is it mutual or one-way?
- Does each party bear liability corresponding to its own non-compliance, with a recovery mechanism between the parties?
- Do the DPA's indemnities conflict with the main agreement's indemnity framework?

**Most exposed:** Whichever party accepts allocation untethered from its actual responsibility — most often the controller-client signing the vendor's form.

---

### 9.3 DPA/main-agreement conflict left unresolved

**Pattern:** The DPA and the main agreement each contain liability, indemnity, or order-of-precedence language, and they point in different directions — with no clear rule stating which controls for data-protection matters.

**Why it matters:** An unresolved conflict invites threshold disputes about which cap and which allocation applies, precisely when a large claim is on the table.

**What to check:**
- Quote each order-of-precedence clause; do they agree?
- Does the DPA amend the main agreement, supplement it, or stand alone?
- Are there duplicated obligations (e.g., two breach-notice clauses, two security standards) that differ in substance?

**Most exposed:** Both parties; in practice, the party that needs to enforce quickly after an incident.

**Preferred position:** Data-protection and security liability is carved out from the general cap or subject to a defined super-cap proportionate to realistic breach exposure; liability between the parties follows responsibility, with a mutual recovery mechanism; a single order-of-precedence rule makes the DPA control for data-protection matters.

**Fallback position:** The general cap stands, but a super-cap applies to security and data-protection breaches, and the order-of-precedence conflict is resolved expressly in the DPA's favor for data matters.

---

## 10. Termination and Return

### 10.1 Data return format and fees undefined or vendor-controlled

**Pattern:** The client's right to get its data back on termination is silent on format, is limited to a proprietary or unusable format, or is conditioned on payment of unspecified retrieval or "professional services" fees.

**Why it matters:** A return right the client cannot practically exercise — because the export is unusable or priced prohibitively — is lock-in dressed as a right, and can strand personal data the client is obligated to retrieve or migrate.

**What to check:**
- Is a machine-readable, commonly used export format specified?
- Are retrieval fees defined, capped, or excluded — and do they apply even on termination for vendor breach?
- Does the return right cover all client personal data, including data held by sub-processors?

**Most exposed:** Controller-client migrating to a successor vendor; any client with portability commitments to its own customers.

---

### 10.2 Short or absent retrieval window

**Pattern:** Data is deleted immediately on termination, or the post-termination retrieval window is very short relative to a realistic migration, with no right to extend and no continued access for retrieval purposes.

**Why it matters:** A window too short to complete migration forces the client to choose between losing data and staying in a contract it wants to exit — and interacts dangerously with the deletion obligations in Section 8 if deletion runs before retrieval completes.

**What to check:**
- How long is the retrieval window, and does it run from termination notice or effective termination?
- Is access during wind-down preserved (and on what fee basis)?
- Is deletion sequenced to occur only after the retrieval window closes or the client confirms export?

**Most exposed:** Controller-client with large data volumes or complex integrations; client exiting on short notice after vendor breach.

**Preferred position:** A defined retrieval window adequate for migration, export in a machine-readable common format covering data held by sub-processors, retrieval free or at defined bounded cost (and free where the client terminates for vendor breach), with deletion sequenced after retrieval completes.

**Fallback position:** A shorter defined window with a right to extend for a bounded fee, a specified export format, and deletion deferred until the window closes.

---

## Reviewer Notes

- A red flag is a prompt to look closely and flag for attorney attention — not a conclusion that a clause is unenforceable, non-compliant, or unacceptable.
- Whether a flagged clause is a problem depends on the client's role (controller, processor, or sub-processor), the data involved, leverage, business context, and risk tolerance — all of which are for the attorney to assess.
- Nothing in this catalog states what any law requires. Applicable frameworks, mandatory terms, and all deadlines are attorney-verification items — `[Verify current law]` `[verify jurisdiction]`.
- The Preferred/Fallback pairs are directions for counsel to refine, written from a controller-client perspective; confirm the client's role before applying them, and pair each with a negotiability rating from `skills/contracts/references/negotiability-ratings.md`.
- This catalog is not exhaustive. Unusual or deal-specific provisions not listed here may still warrant a flag in the risk table.
- See `skills/privacy/dpa-review/SKILL.md` for the full DPA review workflow, `skills/privacy/cross-border-transfer-review/SKILL.md` for transfer-mechanism analysis, and `skills/contracts/references/red-flags.md` for general commercial-contract patterns (liability, indemnity, audit, termination) that also apply to the main agreement.
