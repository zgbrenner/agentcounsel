> Shared reference material supporting the AgentCounsel product-legal skills, used to help produce draft legal work product for attorney review — not legal advice.

# Terms of Service Red-Flag Catalog

This catalog lists drafting patterns and structural features that a reviewer should actively scan for when reviewing a company's own terms of service (ToS) or terms of use for its consumer or business users. Each entry describes the pattern, why it matters, what to check, and who is most exposed. The catalog looks in both directions: risk to the company operating the service (gaps, ambiguity, missing protections) and consumer-fairness or enforceability exposure (provisions a regulator, court, or reasonable user may find one-sided or surprising).

This catalog is a review aid. It identifies drafting and fairness patterns worth flagging — never a conclusion that a clause is unenforceable, unlawful, or in violation of any statute. Whether any flagged pattern is actually a problem depends on the specific language, the jurisdictions where users are located, the business model, and attorney judgment. Every enforceability question is framed as an `[ATTORNEY TO CONFIRM: ...]` item, never asserted.

---

## How to Use This Catalog

For each topic section below:

1. Locate the relevant provision in the ToS under review (or note its absence — a missing provision is itself a red flag in many contexts).
2. Check the pattern description against the actual language, quoting it verbatim where it matters.
3. If the pattern is present, add the item to the Issues Table and the Red Flags Quick Scan.
4. Note whether the exposure runs to the operator, to users, or to both, and whether the context is B2C, B2B, or hybrid — consumer-facing terms carry heightened scrutiny.
5. Frame every enforceability point as an `[ATTORNEY TO CONFIRM: ...]` question. Never state that a clause is or is not enforceable.
6. Use the **Preferred position / Fallback position** lines at the end of each section to state the direction of a recommended change — direction only, not final clause language.

---

## 1. Formation and Assent

### 1.1 Browsewrap-style passive assent

**Pattern:** The terms purport to bind anyone who merely browses or uses the site or app, with no affirmative act of acceptance — no checkbox, no "I agree" click — and notice of the terms appears only in a footer link or similarly inconspicuous location.

**Why it matters:** Contract formation generally depends on notice and manifestation of assent. A passive-assent structure invites the question whether any contract was formed at all — which puts the entire document, including the operator's protective provisions, at risk. `[ATTORNEY TO CONFIRM: whether the assent mechanism supports formation in the relevant jurisdictions]`

**What to check:**
- Describe the actual acceptance flow: clickwrap, sign-in-wrap, browsewrap, or hybrid.
- Where and how conspicuously is the link to the terms presented at the moment of assent?
- Is there a record-keeping mechanism capturing who accepted, which version, and when?

**Most exposed:** The operator — a formation failure can void the provisions the company relies on most (liability limits, dispute resolution).

---

### 1.2 Assent to future or unseen changes

**Pattern:** The acceptance language purports to bind the user not only to the current terms but to "any future versions" or "as amended from time to time," so that the initial click is treated as advance consent to unknown future terms.

**Why it matters:** Advance assent to terms the user has never seen is a fairness pattern regulators and courts scrutinize, and it overlaps with the unilateral-modification patterns in Section 2. `[ATTORNEY TO CONFIRM: whether advance assent to future amendments is given effect in the relevant jurisdictions]`

**What to check:**
- Quote the acceptance clause verbatim; does it reach future versions?
- Is there a separate, adequate modification-and-notice mechanism (see Section 2)?

**Most exposed:** Users bound to terms they never reviewed; the operator, if the structure undermines enforceability of later versions.

---

### 1.3 Terms incorporated by reference but unavailable

**Pattern:** The ToS incorporates other documents — an acceptable use policy, service-level terms, community guidelines, a refund policy — by reference, but the referenced documents are not linked, the links are broken, or the documents cannot be located.

**Why it matters:** Users cannot assent to terms they cannot access, and the operator cannot reliably enforce obligations defined only in a missing document. Incorporation gaps also create version-control risk: which edition of the referenced document applies?

**What to check:**
- List every document incorporated by reference and confirm each is accessible from the point of assent.
- Do the incorporated documents state their own version or effective date?
- Is there an order-of-precedence rule if the documents conflict?

**Most exposed:** Both parties — users face unknowable obligations; the operator faces enforcement and consistency gaps.

**Preferred position:** Affirmative clickwrap assent to a clearly presented, versioned set of terms, with every incorporated document linked and archived at the moment of acceptance.
**Fallback position:** Sign-in-wrap with conspicuous notice at account creation and at any material change, plus a maintained archive of accepted versions.

---

## 2. Unilateral Modification

### 2.1 Change without notice

**Pattern:** The operator reserves the right to modify the terms "at any time" simply by posting an updated version, with no obligation to notify users of the change or to identify what changed.

**Why it matters:** Silent modification is a classic fairness pattern: users are held to terms they had no reason to know changed. It also creates enforceability risk for the amended terms themselves. `[ATTORNEY TO CONFIRM: whether posted-only amendments are given effect against existing users in the relevant jurisdictions]`

**What to check:**
- Quote the modification clause verbatim.
- Is any notice required? By what channel, and how far in advance?
- Are material changes distinguished from non-material ones, and is there a version history or changelog users can consult?

**Most exposed:** Users, whose obligations shift silently; the operator, whose amended terms may not bind existing users.

---

### 2.2 Continued-use-as-acceptance with no notice mechanism

**Pattern:** Continued use of the service after a change "constitutes acceptance" of the modified terms, but the terms provide no mechanism ensuring the user actually learns of the change — no email, no in-product banner, no re-acceptance prompt.

**Why it matters:** Continued-use acceptance depends on the user having a meaningful opportunity to learn of the change and to stop using the service. Without a notice mechanism, the acceptance theory is hollow, and for material changes (price, dispute resolution, data rights) the fairness concern is acute.

**What to check:**
- What notice mechanism, if any, backs the continued-use clause?
- Do material changes (pricing, arbitration, data use) require affirmative re-acceptance?
- Do users who reject a change have an exit right without penalty (including a refund of prepaid amounts)?

**Most exposed:** Users in ongoing paid relationships; the operator, if material amendments later prove unenforceable against existing users.

**Preferred position:** Advance notice of material changes through a channel the user actually receives (email or in-product), a stated effective date, and affirmative re-acceptance for changes to dispute resolution, pricing, or data rights.
**Fallback position:** Prominent in-product notice with a reasonable review period before effectiveness and a penalty-free cancellation right for users who decline.

---

## 3. Auto-Renewal and Cancellation

Auto-renewal, negative-option, and cancellation mechanics are consumer-protection-sensitive patterns. Specific disclosure, consent, reminder, and cancellation-method requirements vary widely by jurisdiction `[verify jurisdiction]`. Nothing in this section states what any law requires — flag the pattern and route the legal question to counsel.

### 3.1 Renewal without pre-renewal notice

**Pattern:** A subscription renews automatically for another term with no commitment to send a reminder before the renewal date, or the renewal terms (new price, new term length) are not disclosed at signup.

**Why it matters:** Silent renewal is among the most regulator-scrutinized consumer patterns, and some jurisdictions impose specific pre-renewal reminder and disclosure obligations `[verify jurisdiction]`. It is also a churn and chargeback driver. `[ATTORNEY TO CONFIRM: applicable auto-renewal disclosure and reminder requirements in each market]`

**What to check:**
- Is the auto-renewal disclosed clearly and conspicuously at the point of purchase?
- Is a pre-renewal reminder promised? How far in advance, and by what channel?
- Does the price change at renewal, and is that disclosed?

**Most exposed:** Consumers on annual or long-term plans; the operator, via regulatory and chargeback exposure.

---

### 3.2 Cancellation harder than signup

**Pattern:** Signup is a one-click online flow, but cancellation requires a phone call, a written letter, a retention conversation, or navigation through obstructive steps ("dark patterns").

**Why it matters:** Asymmetric friction between signup and cancellation is a recognized consumer-fairness pattern, and some jurisdictions require cancellation to be available by a mechanism as simple as the signup mechanism `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: click-to-cancel or symmetric-cancellation requirements in each market]`

**What to check:**
- Compare the signup flow to the cancellation flow step by step.
- Can users cancel through the same medium they used to subscribe?
- When does cancellation take effect, and is the user told what happens to the remainder of a paid period?

**Most exposed:** Consumers; the operator, via regulatory scrutiny and reputational risk.

---

### 3.3 Fee or forfeiture on cancellation

**Pattern:** Cancelling triggers a cancellation fee, forfeits prepaid amounts for the unused remainder of the term with no refund or credit, or accelerates all remaining fees for the committed term.

**Why it matters:** Cancellation penalties in consumer terms attract unconscionability and consumer-protection scrutiny `[verify jurisdiction]`, and prepaid-amount forfeiture overlaps with the termination patterns in Section 8. `[ATTORNEY TO CONFIRM: whether the cancellation fee and refund position are permissible in each consumer market]`

**What to check:**
- Quote the fee and refund language verbatim.
- Does the fee apply even when the user cancels because the operator changed the terms or the service?
- Is the refund position for unused prepaid periods stated, or silent?

**Most exposed:** Consumers on prepaid plans; the operator, via disputes and regulatory complaints.

**Preferred position:** Conspicuous auto-renewal disclosure at purchase, pre-renewal reminders, cancellation as easy as signup, and a stated, fair treatment of unused prepaid amounts.
**Fallback position:** Clear renewal disclosure plus an online cancellation path, with any cancellation fee limited, disclosed at signup, and waived where the operator materially changed the deal.

---

## 4. Dispute Resolution

Enforceability of arbitration clauses, class waivers, limitations-period changes, and forum clauses is highly jurisdiction-specific and is never asserted in a review — every point in this section is an `[ATTORNEY TO CONFIRM: ...]` question `[verify jurisdiction]`.

### 4.1 Mandatory arbitration combined with a class-action waiver

**Pattern:** All disputes must go to individual arbitration, users waive class, collective, and representative proceedings, and there is no opt-out mechanism (or the opt-out window is short and obscure).

**Why it matters:** The arbitration-plus-class-waiver combination is the most litigated and regulated provision in consumer terms. Its treatment varies sharply by jurisdiction and claim type, and design details — opt-out rights, fee allocation, carve-outs (e.g., small-claims court), mass-arbitration protocols — materially affect both fairness and the operator's own exposure. `[ATTORNEY TO CONFIRM: treatment of consumer arbitration clauses and class waivers in each relevant jurisdiction]`

**What to check:**
- Quote the arbitration and class-waiver language verbatim, including any opt-out mechanism and its deadline.
- Which rules and forum administer the arbitration, who pays the fees, and what carve-outs exist (small-claims, injunctive relief, IP claims) — and are the carve-outs mutual or operator-only?
- Is there a severability provision addressing what happens if the class waiver fails, and has the operator considered mass-arbitration exposure (thousands of individual filings)?

**Most exposed:** Consumers losing collective remedies; the operator, via enforceability challenges and mass-arbitration fee exposure.

---

### 4.2 Shortened limitations period

**Pattern:** The terms require any claim to be brought within a contractually shortened period (e.g., one year, or less) after it arises, replacing whatever limitations period would otherwise apply.

**Why it matters:** Contractual shortening of limitations periods is permitted in some places, restricted or ineffective in others, and especially sensitive against consumers `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: whether a contractually shortened claims period is given effect against the relevant user base]`

**What to check:**
- Quote the clause and the period verbatim.
- Is the shortening mutual or does it bind only users?
- When does the period start running — discovery, or occurrence?

**Most exposed:** Users with slow-surfacing claims; the operator, if the clause draws unconscionability scrutiny onto the whole dispute section.

---

### 4.3 One-sided fee shifting

**Pattern:** The user must pay the operator's attorneys' fees and costs if the operator prevails (or merely enforces the terms), with no reciprocal right for a prevailing user.

**Why it matters:** Asymmetric fee shifting deters legitimate user claims and is a recurring fairness flag; some jurisdictions read one-way fee clauses as reciprocal or decline to apply them `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: treatment of one-way fee-shifting clauses in the relevant jurisdictions]`

**What to check:**
- Is fee shifting mutual, one-way, or tied to a "prevailing party" standard?
- Does it interact with the arbitration clause's fee-allocation rules?

**Most exposed:** Users deciding whether to assert a claim; the operator, via fairness scrutiny.

---

### 4.4 Inconvenient exclusive forum

**Pattern:** All disputes must be brought exclusively in the operator's home courts (or an arbitral seat there), regardless of where the user lives — a burden that can be prohibitive for consumer-sized claims.

**Why it matters:** An exclusive distant forum can make user claims economically impossible, and consumer-protection regimes in some jurisdictions restrict forum clauses against local consumers `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: whether the forum and governing-law selections are given effect against consumers in each market]`

**What to check:**
- What forum and governing law are selected, and do they align with each other and with the arbitration clause?
- Is there a carve-out preserving consumers' local mandatory rights or local small-claims access?

**Most exposed:** Users distant from the forum; the operator, via threshold litigation over the clause itself.

**Preferred position:** A dispute clause designed for durability: clear opt-out, mutual carve-outs, mutual fee treatment, small-claims access, and consumer-forum accommodations — reviewed by counsel per market.
**Fallback position:** If aggressive terms are retained as a business decision, document the enforceability risk per market as `[ATTORNEY TO CONFIRM]` items and add severability language, rather than presenting the clause as settled.

---

## 5. Content and Intellectual Property

### 5.1 User-content license broader than the service needs

**Pattern:** Users grant the operator a perpetual, irrevocable, worldwide, royalty-free, sublicensable, transferable license to all content they submit — for any purpose — when the service only needs rights sufficient to host, display, and operate the product.

**Why it matters:** Over-broad content grabs are a recurring public-relations and fairness flashpoint, can conflict with the privacy policy (see Section 6), and can chill adoption by professional users whose content has independent value. Breadth beyond need buys the operator little and costs trust.

**What to check:**
- Quote the license grant verbatim: scope, purpose, duration, revocability, sublicensing, transferability.
- Is the license tied to operating and promoting the service, or is it purpose-unlimited? Does it survive account deletion, and is that disclosed?
- Does the grant cover use for AI training (route to Section 10)?

**Most exposed:** Users with valuable content; the operator, via backlash and privacy-policy conflicts.

---

### 5.2 Feedback assignment rather than license

**Pattern:** All user feedback, suggestions, and ideas are assigned outright to the operator (or licensed with a confidentiality obligation on the user), rather than the conventional unrestricted, non-confidential feedback license.

**Why it matters:** An outright assignment of feedback is broader than the operator typically needs and can be surprising to business users whose employees submit feedback; obligations attached to feedback can also conflict with users' own IP arrangements.

**What to check:**
- Is feedback assigned or licensed? Quote the operative verb.
- Are any obligations imposed on the user regarding their own feedback?

**Most exposed:** Business users with IP hygiene obligations; the operator gains little from the broader form.

---

### 5.3 Moral-rights waiver in consumer terms

**Pattern:** The content license includes a waiver of moral rights (attribution, integrity) — sometimes extending to "all rights of a similar nature anywhere in the world" — in a consumer-facing document.

**Why it matters:** Moral-rights waivers are recognized in some jurisdictions, restricted or ineffective in others `[verify jurisdiction]`, and their presence in consumer terms is a fairness flag when the service does not actually need to modify user works. `[ATTORNEY TO CONFIRM: effect of the moral-rights waiver across the user base's jurisdictions]`

**What to check:**
- Is a moral-rights waiver present, and is it tied to a demonstrated product need (e.g., reformatting, thumbnails)?
- Is the waiver limited to uses within the license purpose?

**Most exposed:** Creator users; the operator, if the waiver draws scrutiny onto the wider license.

**Preferred position:** A content license scoped to what the service needs to operate, promote, and improve the product, terminating on content deletion except for backup and legal-hold copies; a standard non-confidential feedback license.
**Fallback position:** A broader license only where a specific product function requires it, with the function named in the terms and survival after deletion narrowed and disclosed.

---

## 6. Data and Privacy Hooks

This section flags where the ToS intersects data practices. A substantive review of the privacy policy itself is a separate exercise — route it to `skills/privacy/privacy-policy-gap-review/SKILL.md`.

### 6.1 ToS contradicting the privacy policy

**Pattern:** The ToS grants the operator data or content rights (e.g., broad use, sharing, sale, or AI-training rights) that the linked privacy policy does not disclose — or the two documents describe retention, sharing, or deletion differently.

**Why it matters:** Inconsistent statements across the ToS and privacy policy create misrepresentation exposure — the stricter document tends to be the one regulators and plaintiffs quote — and make both documents harder to defend. `[ATTORNEY TO CONFIRM: which document controls and whether the practices described are accurate]`

**What to check:**
- Compare data-use, sharing, retention, and deletion statements across both documents side by side.
- Is there an order-of-precedence clause, and does it resolve the specific conflict?
- Does either document promise practices the product does not actually implement?

**Most exposed:** The operator — inconsistency is exposure regardless of which version is "right"; users, whose expectations are set by the more protective document.

---

### 6.2 Data consent buried in the terms

**Pattern:** Consent to specific data practices (marketing communications, sharing with partners, tracking, AI training on personal data) is embedded as a clause inside the ToS, obtained only through the general "I agree" to the terms as a whole.

**Why it matters:** Regimes that require consent for a data practice often require it to be specific, informed, and separately given; a buried clause is a fairness flag and may not function as valid consent `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: whether the consent mechanisms satisfy the applicable data-protection regimes]`

**What to check:**
- List every data-practice consent the ToS purports to capture.
- Is each consent separable (its own checkbox or setting), or bundled into general acceptance?
- Route the substantive adequacy review to `skills/privacy/privacy-policy-gap-review/SKILL.md`.

**Most exposed:** Users, whose data is used beyond expectations; the operator, via consent-validity exposure.

**Preferred position:** The ToS defers to the privacy policy for data practices, the two documents are reconciled, and any practice requiring consent is captured through a separate, specific mechanism.
**Fallback position:** At minimum, an accurate cross-reference with an order-of-precedence rule and removal of any ToS data clause the privacy policy does not support.

---

## 7. Disclaimers and Liability

### 7.1 Blanket warranty disclaimer against consumers

**Pattern:** The service is provided strictly "AS IS," disclaiming all warranties, express and implied, with no affirmative service commitment — applied without distinction to consumer users.

**Why it matters:** Some jurisdictions restrict how far implied warranties or statutory guarantees can be disclaimed against consumers, and some require specific savings language `[Verify current law]`. A blanket disclaimer with no consumer savings clause is a fairness flag and can put the whole disclaimer at risk. `[ATTORNEY TO CONFIRM: permissible scope of warranty disclaimers against the consumer user base]`

**What to check:**
- Quote the disclaimer verbatim; is it conspicuous (all-caps or equivalent)?
- Is there a savings clause ("to the maximum extent permitted by law" / "some jurisdictions do not allow...") preserving non-waivable rights?
- Does the disclaimer contradict marketing claims or an SLA elsewhere?

**Most exposed:** Consumers relying on the service; the operator, if an overbroad disclaimer fails wholesale rather than being trimmed.

---

### 7.2 Liability cap below refund value or purely nominal

**Pattern:** Liability is capped at a nominal fixed sum (e.g., $50 or $100) or at fees paid in a short trailing window — an amount below what the user paid, or effectively zero for free-tier users — combined with a full consequential-damages waiver.

**Why it matters:** A cap that denies even a refund-level remedy is a strong unconscionability and fairness flag in consumer contexts, and courts in some jurisdictions scrutinize remedy structures that leave users with no meaningful recourse `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: whether the cap structure withstands scrutiny in consumer markets]`

**What to check:**
- Quote the cap formula and compare it to what a typical user pays over the relationship.
- Are there carve-outs (e.g., for the operator's willful misconduct, or for the operator's indemnity obligations, if any)?
- Is the structure mutual in form, and asymmetric in effect?

**Most exposed:** Paying users; the operator, via unconscionability challenges to the remedy structure.

---

### 7.3 Disclaiming rights some jurisdictions do not permit waiving

**Pattern:** The terms purport to exclude or waive categories of user rights or remedies that some jurisdictions do not permit waiving — statutory consumer guarantees, certain personal-injury liability, or liability for the operator's own intentional misconduct — with no jurisdiction-specific savings or tailoring `[Verify current law]`.

**Why it matters:** Purporting to waive non-waivable rights does not merely fail — in some places it can itself be a prohibited practice or can taint adjacent provisions `[verify jurisdiction]`. Described generically here: the flag is the absence of any accommodation for rights some jurisdictions do not permit waiving. `[ATTORNEY TO CONFIRM: which user rights are non-waivable in each market and whether the savings language is adequate]`

**What to check:**
- Identify each absolute exclusion ("in no event," "under no circumstances") and whether a savings clause qualifies it.
- Is there any jurisdiction-specific rider or "if you are a consumer in [region]" section?

**Most exposed:** The operator — this pattern is primarily operator-side legal exposure dressed as protection.

**Preferred position:** Disclaimers and caps calibrated to the user base, with savings clauses preserving non-waivable rights, refund-level remedies preserved for consumers, and jurisdiction riders where markets diverge.
**Fallback position:** A global savings clause plus attorney-confirmed treatment of the largest consumer markets, with remaining markets flagged as open items.

---

## 8. Termination and Account Suspension

### 8.1 Suspension or termination without notice or appeal

**Pattern:** The operator may suspend or terminate any account "at any time, for any reason or no reason, in its sole discretion," with no notice, no statement of reasons, and no appeal or reinstatement path.

**Why it matters:** Unqualified sole-discretion termination is a fairness flag in consumer terms — especially where users lose access to purchased content, data, or an income stream — and some regimes impose notice or statement-of-reasons obligations on certain platforms `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: any platform-specific notice, reasons, or appeal obligations applicable to the service]`

**What to check:**
- What triggers suspension versus termination, and is any notice or cure period provided for non-egregious violations?
- Can users export their data or content after termination, and for how long?
- Is there an appeal or review mechanism, even an informal one?

**Most exposed:** Users dependent on the account (data, purchases, income); the operator, via disputes and platform-regulation exposure.

---

### 8.2 Forfeiture of prepaid amounts or virtual items on termination

**Pattern:** On termination — including operator-initiated termination without cause — the user forfeits prepaid subscription fees, account credits, gift-card balances, or virtual items and currency, which the terms declare have "no cash value" and are "not the user's property."

**Why it matters:** Forfeiture of paid-for value on operator-initiated termination is a strong unconscionability and consumer-protection flag, and prepaid instruments and stored value are specifically regulated in some jurisdictions `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: treatment of prepaid amounts, credits, and virtual items on termination in each market]`

**What to check:**
- Distinguish the refund position by termination cause: user breach, user convenience, operator convenience, service shutdown.
- Quote the virtual-items and credits language verbatim.
- Is there any wind-down or refund commitment if the operator discontinues the service?

**Most exposed:** Consumers holding prepaid value; the operator, via regulatory complaints and chargebacks.

**Preferred position:** Graduated enforcement (warn, suspend, terminate) with notice and appeal for non-egregious cases, a post-termination data-export window, and pro-rata refunds of prepaid amounts on operator-initiated termination without cause.
**Fallback position:** Immediate action reserved for defined egregious conduct, with the refund and export position for all other cases stated explicitly rather than left to discretion.

---

## 9. Accessibility of Key Terms

### 9.1 Material terms hidden in cross-referenced documents

**Pattern:** Terms with real economic or legal weight — pricing changes, arbitration details, data rights, service-level exclusions — live not in the ToS itself but in secondary documents reached by chains of links, where a user reading the main terms would not find them.

**Why it matters:** Burying material terms undercuts the notice on which enforceability rests and is itself a fairness pattern reviewers and regulators look for. The more surprising the term, the more conspicuous its presentation needs to be. `[ATTORNEY TO CONFIRM: whether the presentation of the buried material terms supports enforcement]`

**What to check:**
- Map every incorporated document and identify which contains material terms not summarized in the ToS.
- How many clicks from the point of assent is each material term?
- Were the secondary documents available and versioned at the time of assent (see Section 1.3)?

**Most exposed:** Users, who miss the material terms; the operator, whose buried terms may not bind.

---

### 9.2 Inconsistent definitions between the ToS and order forms

**Pattern:** The ToS and the order form, checkout page, subscription screen, or enterprise order documents use the same defined terms differently ("Services," "Fees," "Term," "User"), or describe the deal differently (price, renewal, seat counts), with no order-of-precedence clause.

**Why it matters:** Definitional drift between the standing terms and the transactional documents creates ambiguity over the actual deal — and ambiguity in operator-drafted standard terms is commonly resolved against the drafter. This is primarily operator-side risk.

**What to check:**
- Cross-check every defined term used in both the ToS and the ordering documents.
- Is there an order-of-precedence clause, and does it point in the direction the operator intends?
- Do checkout-screen statements (price, renewal, cancellation) match the ToS?

**Most exposed:** The operator, as drafter; business customers, in enterprise ordering flows.

**Preferred position:** Material terms stated or summarized in the main ToS, a single defined-terms source used consistently across ToS and ordering documents, and an explicit order-of-precedence clause.
**Fallback position:** A reconciliation pass fixing the specific conflicts found, plus a precedence clause covering the rest.

---

## 10. AI-Feature Terms

Apply this section when the service includes AI features (generative outputs, model-backed functionality, AI assistants). These entries cover the ToS-level flags only — route any deep review of an AI feature to `skills/product-legal/ai-feature-review/SKILL.md`.

### 10.1 Training-on-user-content defaults

**Pattern:** The terms grant the operator the right to use user content, prompts, or usage data to train or improve AI models — by default, with no opt-out, or with the grant buried in a general content license rather than stated plainly.

**Why it matters:** Default AI-training rights are among the most scrutinized modern ToS patterns: they raise fairness and surprise concerns, frequently conflict with the privacy policy (see Section 6.1), can conflict with business users' own confidentiality obligations, and may implicate consent requirements for personal data `[verify jurisdiction]`. `[ATTORNEY TO CONFIRM: adequacy of disclosure and any required consent for AI training on user content]`

**What to check:**
- Quote the training-rights language verbatim and note where it sits (its own clause, or buried in the content license).
- Is training opt-in, opt-out, or unavoidable — and does the tier matter (consumer vs. enterprise)?
- Does the privacy policy disclose the same practice in the same scope? Route a deep review to `skills/product-legal/ai-feature-review/SKILL.md`.

**Most exposed:** Users with confidential or valuable content; the operator, via backlash, consent exposure, and enterprise deal friction.

---

### 10.2 Output ownership ambiguity

**Pattern:** The terms are silent or internally inconsistent on who owns AI-generated outputs — e.g., the user "owns" outputs while the operator retains a broad license to them, identical outputs may be generated for other users, and the terms disclaim any warranty that outputs do not infringe third-party rights.

**Why it matters:** Users make commercial decisions based on assumed output ownership. Ambiguity here creates disputes, and the underlying question of protectability of AI-generated content is unsettled and jurisdiction-dependent `[Verify current law]`. `[ATTORNEY TO CONFIRM: the output-ownership and IP-risk allocation position the company intends, and how current law treats it]`

**What to check:**
- Quote every clause touching output ownership, licensing back to the operator, and non-uniqueness of outputs.
- Is the user told what they may and may not do commercially with outputs?
- Who bears third-party IP infringement risk in outputs — and is any indemnity offered or excluded?

**Most exposed:** Users commercializing outputs; the operator, via inconsistent promises across terms, marketing, and enterprise contracts.

**Preferred position:** A plainly stated AI section: what is trained on what data and under what control, a clear output-rights allocation, and consistent treatment across ToS, privacy policy, and marketing.
**Fallback position:** At minimum, training rights surfaced as their own labeled clause with an opt-out for identifiable content, and output ownership stated even if qualified.

---

## Reviewer Notes

- A red flag is a prompt to look closely and flag for attorney attention — not a conclusion that a clause is unenforceable, unconscionable, or unlawful. Enforceability is always an `[ATTORNEY TO CONFIRM: ...]` question, jurisdiction by jurisdiction `[verify jurisdiction]`.
- This catalog runs in both directions. Some patterns expose users to unfair terms; others expose the operating company to enforceability failure, regulatory scrutiny, or drafting ambiguity. Record which direction each finding runs.
- Whether a flagged pattern is a problem depends on the user base (consumer, business, or hybrid), the markets served, the product's actual behavior, and attorney judgment.
- This catalog is not exhaustive. Unusual provisions not listed here may still warrant a flag in the Issues Table.
- Preferred and Fallback position lines state the direction of a change only — never final clause language. Substantive drafting is an attorney task.
- See `skills/product-legal/terms-of-service-review/SKILL.md` for the full ToS review workflow.
- See `skills/privacy/privacy-policy-gap-review/SKILL.md` for substantive privacy-policy review, and `skills/product-legal/ai-feature-review/SKILL.md` for deep review of AI features.
