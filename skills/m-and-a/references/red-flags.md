> Shared reference material supporting the AgentCounsel M&A skills, used to help produce draft legal work product for attorney review — not legal advice.

# M&A Red-Flag Catalog

This catalog lists patterns in acquisition agreements, disclosure schedules,
data rooms, ancillary agreements, and transaction-insurance packages that a
reviewer should actively scan for. Each entry describes the pattern, why it
matters, what to check, and which side of the deal is most exposed. The
catalog is organized by document family so a review skill can run a Red Flags
Quick Scan against the family relevant to the document in front of it, then
fold every pattern found into that skill's own issue table using the table
shapes defined in `skills/m-and-a/references/output-patterns.md`.

This catalog is a review aid. It never decides whether a provision is
enforceable, whether a consent is legally required, whether an escrow or
indemnity structure is adequate, whether a disclosure is complete, or what
tax, antitrust, or securities-law treatment applies. Whether a flagged
pattern matters depends on the deal structure, negotiated leverage, the
client's side, the transaction stage, and the governing jurisdiction — all
attorney judgment calls. Every flagged item is a candidate for attorney
verification, never a legal conclusion.

Three disciplines are non-negotiable throughout:

- **Never state what the law requires.** Enforceability, fraud standards,
  statutory notice or filing requirements, and every legal-treatment question
  are jurisdiction-specific. Flag `[verify jurisdiction]`.
- **Never compute a figure or a deadline.** Price, adjustment amounts, earnout
  metrics, caps, baskets, escrow amounts, and dates are recorded as the
  document states them, and dates are flagged `[deadline verification
  required]`. Never calculate a true-up, test a covenant, or reconstruct a
  timeline.
- **Never rate anything "market standard."** A comparison to market practice
  (a cap, a basket, an escrow percentage, a survival period) is flagged
  `[ATTORNEY TO CONFIRM: market context]`, never asserted.

---

## How to Use This Catalog

For each relevant topic section:

1. Locate the relevant provision, schedule entry, index item, or ancillary
   document (or note its absence — itself a red flag in several sections).
2. Check the pattern against the actual language or fact, quoting operative
   terms verbatim.
3. If present, add the item to the relevant issue table (issue list, risk
   matrix, unresolved-items list, consent tracker, gap matrix, deliverables
   tracker, obligation tracker, exclusions register, or completeness matrix)
   with a source citation.
4. Note which side is most exposed, and whether the user's stated side
   matches the exposure profile.
5. Flag every finding for attorney review; never resolve ambiguity, decide
   enforceability, or compute a figure or date.

Section grouping by document family:

- **Economics** — Section 1 (`purchase-agreement-issue-list`,
  `indemnity-escrow-risk-review`).
- **Reps and disclosure** — Sections 2–3
  (`reps-warranties-disclosure-schedule-review`, `purchase-agreement-issue-list`).
- **Indemnification and insurance** — Section 4 (`indemnity-escrow-risk-review`,
  `rw-insurance-review`).
- **Deal certainty** — Section 5 (`purchase-agreement-issue-list`).
- **Consents and transfer** — Section 6 (`third-party-consents-assignment-review`).
- **Post-closing** — Section 7 (`post-closing-obligations-tracker`,
  `transition-services-agreement-review`, `closing-deliverables-tracker`).
- **Diligence completeness** — Section 8 (`data-room-index-review`).
- **Internal consistency** — Section 9 (every skill in this catalog's scope).
- **Cross-cutting routing** — Section 10 (every skill).

Where a section carries a **Direction for counsel** line, it frames a
preferred and a fallback direction from a stated side — a direction of
change, never drafted language or a decision.

---

## 1. Purchase Price & Adjustment Red Flags

### 1.1 Working-capital target without a clear peg or methodology

**Pattern:** The agreement sets a working-capital target or peg, but its
derivation (historical period, accounting principles, negotiated exclusions)
is missing, inconsistent with the referenced financials, or left to a later
schedule.

**Why it matters:** The adjustment converts directly into cash between the
parties; an unsupported peg invites a dispute at the true-up. The question is
whether the peg and its derivation are stated and internally consistent —
never what the correct peg should be.

**What to check:**
- Quote the working-capital definition, peg amount, and accounting
  principles verbatim, with source.
- Is the peg tied to a stated historical average or balance-sheet date
  consistent with the financial-statements representation?
- Does a schedule meant to show the calculation exist, or read "to be
  provided"?
- Record the true-up review period, objection window, and arbiter-selection
  mechanism as written; flag every date `[deadline verification required]`.

**Most exposed:** Both sides at the true-up; the side whose net proceeds swing
most on an unresolved peg.

---

### 1.2 Earnout metrics under buyer post-closing control with no protective covenants

**Pattern:** Consideration includes an earnout tied to post-closing
performance, the buyer retains full post-closing operating control, and no
covenant requires good-faith operation, resource commitment, or restricts
actions that could suppress the metric.

**Why it matters:** The buyer controls many levers driving the metric
(headcount, budget, cross-selling, accounting allocations); silence leaves
the seller's contingent consideration exposed to decisions it cannot see. The
question is what covenants and audit rights exist — never whether the earnout
will be achieved.

**What to check:**
- Quote the earnout metric verbatim, including adjustment/addback mechanics;
  record measurement periods `[deadline verification required]`.
- Is there an operating covenant (good-faith efforts, standalone-operation,
  a resource-commitment) protecting the metric, or is the buyer unconstrained?
- Is there a seller audit right, a reporting right, and a dispute mechanism
  for the calculation?
- Is there an acceleration trigger if the buyer sells the earned business or
  breaches the operating covenants during the earnout period?

**Most exposed:** Seller relying on the earnout; buyer if covenants are so
restrictive they constrain ordinary integration.

**Direction for counsel:** Preferred (seller) — defined operating covenants,
an audit right, and an acceleration trigger. Fallback — a narrower metric
definition with the audit right preserved. Direction only
`[ATTORNEY TO CONFIRM: market context]`.

---

## 2. Representations & Warranties Red Flags

### 2.1 Thin representations relative to the deal's risk profile

**Pattern:** The representations article omits a representation the deal's
type, size, or industry would typically call for (e.g., no data-privacy
representation for a data-driven target, no environmental representation for
an industrial one), or covers a topic only at a high level of generality.

**Why it matters:** A representation never given is a risk the buyer cannot
recover for through indemnification, however that mechanism is structured.
The question is what is present and conspicuously absent — never whether the
omission is acceptable, which is a negotiated allocation.

**What to check:**
- Inventory the representations given, with citations, against the target's
  business and the diligence workstreams already run.
- Is a representation covering a diligence-flagged risk area present, thin,
  or absent?
- Does a general "compliance with laws" representation stand in for a
  specific one the risk profile calls for?

**Most exposed:** Buyer relying on representations for post-closing recourse;
seller if a broad representation creates exposure beyond what was diligenced.

---

### 2.2 Broad or narrow knowledge qualifier with an undefined knowledge group

**Pattern:** Representations are qualified "to the Company's/Seller's
knowledge," and the definition either names an unreasonably narrow group or
is left undefined, with no stated inquiry standard (actual knowledge vs. a
duty of reasonable inquiry).

**Why it matters:** The qualifier can be the difference between a
representation that protects the buyer and one that protects only insulated
executives. The question is what the definition says and to whom it applies —
never whether the qualifier is fair.

**What to check:**
- Quote the "knowledge" definition in full, including named individuals or
  role-based group and any inquiry standard.
- Is the group limited to individuals unlikely to know the relevant facts
  (e.g., excluding finance on a financial-statements representation)?
- Is "knowledge" defined once and used consistently, or does the agreement
  use more than one knowledge standard without reconciling them (Section 9)?

**Most exposed:** Buyer relying on a knowledge-qualified representation;
individuals named in the knowledge group, whose knowledge now defines the
seller's exposure.

---

### 2.3 Short or asymmetric survival period relative to the risk represented

**Pattern:** General representations survive briefly or not at all, survival
for fundamental representations is undefined or conflicts with a
statute-of-limitations reference elsewhere, and survival periods differ from
the escrow term with no stated reason.

**Why it matters:** A representation that survives only briefly gives the
buyer no practical recourse for a later-discovered breach, and a
survival/escrow mismatch is a structural gap — a claim window can close
before, or reopen after, the funds meant to secure it are released. The
question is whether the periods are stated and consistent — never whether a
period is long enough.

**What to check:**
- Record survival periods for general, fundamental, tax, and any specially
  carved-out representations, each `[deadline verification required]`.
- Does the escrow/holdback release date align with, precede, or follow the
  survival period it secures?
- Does a fundamental-representation survival period reference "the
  applicable statute of limitations plus a tail" without specifying it?
  `[verify jurisdiction]`

**Most exposed:** Buyer whose recourse window may close before a breach is
discovered; seller if survival periods leave an open-ended exposure tail.

---

## 3. Disclosure Schedule Red Flags

### 3.1 Missing or orphan schedule

**Pattern:** A representation cross-references a schedule not in the
delivered package (missing), or a delivered schedule has no representation
pointing to it (orphan).

**Why it matters:** A missing schedule leaves a qualification unverifiable;
an orphan schedule may signal a renumbering error or content disclosed
against the wrong representation. The question is only whether the schedule
and representation match on their face.

**What to check:**
- Cross-reference every representation's schedule citation against the
  delivered package, both directions.
- Record a missing schedule as `Schedule not provided` — never assume nothing
  was meant to be disclosed.
- For an orphan schedule, note which representation it most plausibly
  qualifies and flag the mismatch.

**Most exposed:** Buyer relying on the schedule to define what was disclosed;
seller whose disclosure may not reach the intended representation.

---

### 3.2 Broken cross-reference between representation and schedule

**Pattern:** A representation cites a schedule number that does not match the
delivered package's numbering (e.g., "Schedule 3.10" cited, "Schedule 4.10"
delivered).

**Why it matters:** A broken cross-reference creates the same practical
problem as a missing schedule even though content may exist elsewhere in the
package. The question is whether citation and delivered numbering match —
not what the content says.

**What to check:**
- Build the full cross-reference map (representation section to schedule
  number) and flag every mismatch.
- Is the mismatch a plausible renumbering artifact, or a genuine dead end
  with no corresponding content anywhere?
- Check whether the schedules' general provisions address renumbering, and
  whether that provision is itself consistent.

**Most exposed:** Both sides — the mismatch can be read against either party
`[verify jurisdiction]`.

---

### 3.3 Overbroad general disclosure exception

**Pattern:** The schedules include a qualifier stating any matter disclosed
anywhere in the schedules or data room qualifies every representation to
which it could reasonably apply — sometimes broad enough to sweep in matters
an ordinary reader would not connect to the representation at issue.

**Why it matters:** A broad general-disclosure clause can convert an
unindexed data room into a blanket qualification, substantially narrowing
what the buyer can later claim was not disclosed. The question is the
clause's exact scope and whether the data room is organized enough to make
"reasonable apparency" assessable — never whether the clause is enforceable.

**What to check:**
- Quote the qualifier verbatim, including any "reasonably apparent from the
  face of the disclosure" limiting language.
- Is the data room organized and indexed well enough for that standard to be
  assessable? Cross-check against `data-room-index-review` findings.
- Route enforceability to counsel `[verify jurisdiction]`; never conclude a
  specific document qualifies a specific representation.

**Most exposed:** Buyer whose claims may be narrowed by matters buried in an
unindexed data room; seller relying on the clause to broaden disclosure.

---

### 3.4 Stale schedule date not updated to signing or closing

**Pattern:** A schedule (or the representations bring-down mechanic) is dated
materially earlier than signing, and the agreement does not clearly require
or show an update at signing, closing, or through a supplement mechanism.

**Why it matters:** A schedule gone stale between preparation and signing or
closing can leave a material change undisclosed. The question is only
whether the dates line up and an update mechanism exists — never what a
stale schedule should now say.

**What to check:**
- Record every schedule date and the signing/closing dates, each `[deadline
  verification required]`.
- Does the agreement provide for a schedule supplement between signing and
  closing, and does it interact with closing conditions or indemnification
  (a "sandbagging" question)?
- Is there evidence a supplement was actually delivered, or is the schedule
  silent since its original date?

**Most exposed:** Buyer relying on current information at closing; seller if
an unclear update mechanism creates disclosure risk for the gap period.

---

### 3.5 "To be provided" or placeholder text left in a schedule

**Pattern:** A schedule entry reads "to be provided," "[TBD]," "[ ]," "draft —
subject to completion," or similar, in a document set otherwise presented as
final.

**Why it matters:** A placeholder at signing or closing means the
representation it qualifies is, in substance, incomplete. The question is
only whether the placeholder exists and where — never what content should
eventually fill it.

**What to check:**
- Scan every schedule for placeholder or draft language and list each
  instance with its citation.
- Is the placeholder in a schedule the closing conditions require to be
  "true, correct, and complete"?
- Flag every instance as an open item requiring resolution before signing or
  closing — never assume the eventual content.

**Most exposed:** Buyer taking the schedules as complete; seller who must
close the gap before delivery.

---

## 4. Indemnification, Caps/Baskets & Escrow Red Flags

### 4.1 Survival-to-escrow-term mismatch

**Pattern:** The representations' survival period and the escrow release
schedule do not align — e.g., escrow releases in full before general-rep
survival expires, with no stated reason for the mismatch.

**Why it matters:** A mismatch between when a claim can still be made and
when the funds meant to satisfy it are released can leave a valid claim
without a ready recovery source. The question is whether the dates line up —
never whether either period, alone, is adequate.

**What to check:**
- Record survival period(s) and escrow release dates exactly as written,
  each `[deadline verification required]`.
- Does escrow release precede survival expiration, and by how much as
  stated — do not compute the interval.
- Does the agreement address a claim pending at the scheduled release date
  (a holdback of the disputed amount, or release regardless)?

**Most exposed:** Buyer whose claim window may outlast the escrow; seller
whose proceeds may be held longer than the risk justifies.

---

### 4.2 Tipping-basket vs. true-deductible ambiguity

**Pattern:** The basket/threshold clause is ambiguous whether, once losses
cross the threshold, the indemnifying party owes losses from the first
dollar (tipping basket) or only the excess (true deductible) — sometimes
because different language elsewhere suggests the other structure.

**Why it matters:** The difference can be a large swing in recovery once the
threshold is crossed. The question is whether the clause's own language
resolves the ambiguity — never which structure a court would apply.

**What to check:**
- Quote the clause verbatim and identify the words signaling a tipping
  basket ("all Losses, including the Basket Amount") vs. a true deductible
  ("Losses in excess of the Basket Amount").
- Does any other reference to the basket elsewhere use inconsistent
  language?
- Is the ambiguity paired with an equally ambiguous mini-basket or per-claim
  threshold?

**Most exposed:** Both sides — whichever party's claims sit near the
threshold bears the greater practical risk.

---

### 4.3 Fraud carve-out breadth or an undefined "fraud" standard

**Pattern:** "Fraud" (or "willful breach," "intentional misrepresentation")
is carved out of the caps, baskets, survival, or exclusive-remedy provision
but is undefined, or defined more broadly or narrowly than common usage.

**Why it matters:** An undefined or inconsistently scoped carve-out can widen
a party's uncapped exposure beyond what was negotiated, or narrow the
carve-out's practical protection — and the governing fraud standard is
intensely jurisdiction-specific. The question is whether the term is defined
and used consistently — never what standard applies.

**What to check:**
- Quote every place "fraud" or its variants appear in the caps, baskets,
  survival, and exclusive-remedy provisions; note whether one definition
  governs all of them.
- Does the carve-out apply symmetrically to both parties' indemnification
  obligations?
- Flag the fraud standard for attorney confirmation `[verify jurisdiction]`;
  never state what conduct would meet it.

**Most exposed:** The side whose recovery depends on the carve-out reaching
the conduct at issue; the side whose cap protection may be undermined by an
overbroad one.

---

### 4.4 Indemnification as exclusive remedy paired with a broad remedy waiver

**Pattern:** Indemnification is the sole and exclusive remedy for breach, and
a broad waiver of other remedies (rescission, other equitable relief, tort or
statutory claims) applies without clearly preserving fraud, willful breach,
or specific performance for pre-closing covenant breaches.

**Why it matters:** Exclusivity paired with a broad waiver can leave a party
with no recourse outside the capped, time-limited indemnity structure, even
for conduct the parties would not expect to be excused. The question is what
exclusivity actually excludes and carves back — never whether it is
enforceable.

**What to check:**
- Quote the exclusive-remedy clause and every carve-out (fraud, specific
  performance, injunctive relief for restrictive covenants) verbatim.
- Does the waiver reach statutory or tort claims otherwise independent of
  the contract, consistent with the fraud carve-out (4.3)?
- Is exclusivity internally consistent with any specific-performance clause?

**Most exposed:** The side seeking recovery outside the cap or survival
period; the side relying on exclusivity to bound total exposure.

---

### 4.5 Setoff rights against escrow, holdback, or earnout asymmetric or unaddressed

**Pattern:** The agreement is silent on whether an indemnification claim may
be set off against an escrow release, holdback, or earnout payment, or grants
setoff to only one party without a matching right or dispute mechanism for
the other.

**Why it matters:** A setoff right changes how a claim is actually
collected — a party with it can unilaterally withhold consideration. The
question is whether the right exists, for whom, and what process governs a
disputed setoff — never whether setoff is the appropriate remedy.

**What to check:**
- Locate every setoff provision and quote it verbatim.
- Is the right one-sided, and is there a dispute-resolution mechanism before
  funds are withheld?
- Does setoff interact with the recovery waterfall (escrow, then RWI, then
  direct claim), and is that interaction stated or left to inference?

**Most exposed:** The party without a setoff right; the party exercising
setoff, if contested.

---

### 4.6 RWI interaction inconsistent with the agreement

**Pattern:** The purchase agreement and the RWI policy/binder disagree, or
are silent relative to each other, on whether RWI sits excess to, replaces,
or overlaps a retained seller-indemnity layer, or on whether the policy's
subrogation waiver against the seller carves out fraud consistent with the
agreement's own carve-out.

**Why it matters:** A mismatch can leave a gap the parties believed was
filled, or create an unintended overlap; this needs both documents checked
together, not either alone. The question is consistency between them — this
catalog never concludes coverage exists or is adequate. Deep RWI review
routes to `skills/m-and-a/rw-insurance-review/SKILL.md`.

**What to check:**
- Record the agreement's stated interaction (if any) with RWI, and the
  policy's retention and subrogation-waiver language, each with source.
- Does the subrogation waiver's fraud carve-out match the agreement's
  (Section 4.3), or is there a gap?
- Is the retention consistent with any residual seller-indemnity basket, or
  does a mismatch leave a coverage gap?

**Most exposed:** Buyer relying on RWI as a recovery source; seller relying
on RWI to narrow residual exposure.

---

## 5. Closing Conditions & Termination Red Flags

### 5.1 Financing condition and MAC/MAE asymmetry

**Pattern:** The buyer's closing obligation is conditioned on financing or the
absence of a material adverse change, while the seller's offsetting
protections (a reverse termination fee, specific performance, a
financing-cooperation covenant with teeth) are thin, absent, or one-sided —
or the MAC/MAE definition's carve-outs run only in the buyer's favor.

**Why it matters:** A buyer with a financing out and a broad MAC condition but
no offsetting remedy can walk with little consequence. The question is the
symmetry of conditions and consequences — not whether a MAC/MAE would be
triggered on the facts.

**What to check:**
- Quote the financing condition, the MAC/MAE definition and every carve-out,
  and any reverse-fee or specific-performance provision verbatim.
- Is the MAC/MAE carve-out list symmetric, or one direction only?
- Does the seller have a specific-performance right, or only the reverse
  fee?
- Does a financing-cooperation covenant itself create risk (e.g., requiring
  pre-closing debt)?

**Most exposed:** Seller facing a financing-conditioned buyer with no
offsetting remedy; buyer if the condition is so narrow it cannot protect
against a real adverse event.

**Direction for counsel:** Preferred (seller) — a specific-performance right
or a fee sized to compensate a failed financing, and a symmetric MAC/MAE
definition. Fallback — a reverse fee without specific performance. Direction
only `[ATTORNEY TO CONFIRM: market context]`.

---

### 5.2 Termination-fee asymmetry without a stated rationale

**Pattern:** One party's termination fee is materially smaller, absent, or
triggered on a narrower set of events than the other's, with no change in
closing conditions or deal risk explaining the difference.

**Why it matters:** Fee structure allocates the cost of a failed deal; an
asymmetric structure can signal or create an imbalance in each side's actual
commitment to close. The question is the structure and triggers as stated —
never whether the amount is enforceable as liquidated damages.

**What to check:**
- Record each party's fee and every triggering event exactly as written.
- Is one party's obligation triggered by a broader set of events than the
  other's?
- Does the fee interact with the financing/MAC asymmetry (5.1) to compound
  imbalance?
- Flag enforceability as liquidated damages/penalty for attorney assessment
  `[verify jurisdiction]`.

**Most exposed:** The party whose fee is comparatively larger or more broadly
triggered.

---

## 6. Consents, Assignment & Change-of-Control Red Flags

### 6.1 Anti-assignment or change-of-control clause not addressed by the deal structure

**Pattern:** A material contract contains an anti-assignment,
consent-to-assignment, or change-of-control (including deemed-assignment)
clause, and the deal structure's transfer mechanics have not been checked
against it — or the clause's triggering definition is ambiguous relative to
the specific structure.

**Why it matters:** An asset deal transfers contracts by assignment, which a
consent clause can block or delay; even a stock deal or merger can trigger a
deemed-assignment clause allowing termination or renegotiation. Whether a
given structure actually triggers a given clause is fact- and
document-specific. The question is whether each material contract's
mechanics have been checked — never whether consent, once required, will be
granted.

**What to check:**
- For each material contract, quote the assignment/change-of-control
  language verbatim and record whether the stated structure implicates it.
- Is the counterparty relationship material enough that a termination right
  is a closing-condition-level risk, not a post-closing housekeeping item?
- Flag genuinely ambiguous matches as open questions for counsel; never
  conclude consent is or is not triggered.

**Most exposed:** Buyer inheriting a contract that may terminate or reprice;
seller facing relationship risk if consent-seeking jeopardizes the deal.

---

### 6.2 Required consent not made a condition to closing

**Pattern:** A material or governmental consent is identified as necessary,
but the closing conditions do not require it before closing, leaving the
parties to close and pursue it afterward with no stated risk allocation for
the gap period.

**Why it matters:** Closing without a required consent can leave a material
relationship, license, or permit vulnerable during the gap. The question is
whether the consent is a closing condition and, if not, what post-closing
protection exists — never whether closing without it is advisable.

**What to check:**
- List every consent identified as material, and record whether it is a
  closing condition, a post-closing covenant, or unaddressed.
- If deferred, is there a covenant, holdback, or indemnity tied specifically
  to that consent risk?
- Cross-check against `closing-deliverables-tracker` and
  `post-closing-obligations-tracker` for the right tracker and timing.

**Most exposed:** Buyer operating without a required consent; seller facing a
counterparty dispute if consent-seeking before closing jeopardizes the deal.

---

## 7. Post-Closing Covenants & Integration Red Flags

### 7.1 Transition services agreement scope creep or no defined exit ramp

**Pattern:** The TSA's service schedule does not match the separated
business's actual operational needs (missing, unpriced, or vaguely described
services), or the TSA has no outside end date, migration obligation, or
exit-assistance mechanism.

**Why it matters:** A mismatched schedule can leave the recipient without a
critical function at carve-out; no exit ramp can keep the parties
entangled indefinitely. The question is schedule completeness against the
deal perimeter and the presence of a defined exit mechanism — never the
correct price or duration. Full review routes to
`skills/m-and-a/transition-services-agreement-review/SKILL.md`.

**What to check:**
- Compare scheduled services against the deal perimeter and any diligence
  functional workstream list; flag every missing, unpriced, or vague
  function the business depends on.
- Is there a stated outside end date, migration/transition-assistance
  obligation, and documentation requirement?
- Does an extension mechanism renew automatically with no outside limit?

**Most exposed:** Recipient facing an operational gap or unbudgeted cost;
provider facing open-ended obligations with no defined exit.

---

### 7.2 Tax cooperation covenant vague on responsibility allocation

**Pattern:** Post-closing tax covenants require "reasonable cooperation" for
return preparation, audits, and refund claims, but do not allocate who
prepares which returns, who controls a contest, cost-sharing, or the period
the obligation runs.

**Why it matters:** Return preparation and audit control carry real cost and
risk; a vague covenant can leave both parties uncertain who is responsible
when a pre-closing or straddle-period issue arises. The question is whether
responsibility is allocated clearly — this catalog never states tax
treatment or the correct allocation.

**What to check:**
- Quote the covenant verbatim, including any allocation of return
  responsibility (pre-closing, straddle, post-closing), contest control, and
  cost-sharing.
- Is the cooperation obligation's duration stated `[deadline verification
  required]`, or open-ended?
- Route substantive tax-allocation questions to
  `skills/tax/tax-covenants-indemnities-review/SKILL.md`; never conclude on
  tax treatment here.

**Most exposed:** Both parties if a contest arises with no clear control or
cost allocation.

---

## 8. Data Room & Diligence Completeness Red Flags

### 8.1 Index entries with no way to confirm the underlying document's content

**Pattern:** The data room index lists a file or category, and the review is
working only from the index (file and folder names), with no way to confirm
the document is legible, complete, or matches its listed description.

**Why it matters:** An index entry is not evidence of what the document
contains; treating a listing as equivalent to a reviewed document risks a
false sense of completeness. The question is whether the index shows
coverage — never what the underlying document says, which an index-only
review cannot confirm.

**What to check:**
- State explicitly that the assessment is based on file/folder names only.
- Are any file names generic, truncated, or otherwise uninformative (e.g.,
  "Scan001.pdf")?
- Flag any category with only one ambiguous entry as a follow-up request,
  not a confirmed coverage item.

**Most exposed:** Anyone relying on the data-room review as a proxy for
document-content review, which it is not.

---

### 8.2 Missing diligence category or unresolved document-version ambiguity

**Pattern:** A standard diligence category (corporate, capitalization,
material contracts, IP, employment, litigation, regulatory, real property,
tax, insurance, financials, financing/debt, environmental, data/privacy) has
no index entries, or the index shows multiple versions of the same document
with no indication which is current.

**Why it matters:** A category with no presence at all is either a genuine
disclosure gap or a sign it was never requested; a stale or superseded
version relied upon can build a later review on outdated information. The
question is coverage and version clarity, not document substance.

**What to check:**
- Map index entries to the standard category set; mark each `Present`,
  `Partial`, or `Absent`, and cross-check `Absent` categories against
  `acquisition-diligence-request-list`.
- For a regulated or data-intensive target, confirm industry-specific
  categories are not silently missing.
- Identify every document with more than one apparent version and whether
  the index states which is current.

**Most exposed:** Buyer relying on data-room completeness before closing;
seller whose data room may later be found incomplete.

---

## 9. Internal Consistency Red Flags

### 9.1 Defined term used inconsistently or left undefined

**Pattern:** A capitalized term ("Company," "Business," "Affiliate,"
"Knowledge," "Material Adverse Effect") is defined once but used with a
different meaning elsewhere, or used without ever being defined — including
across the purchase agreement and its ancillary documents (a TSA using
"Business" differently than the agreement).

**Why it matters:** An inconsistency can quietly change the scope of a
representation, covenant, or indemnity, and it is entirely a checkable
matter, not an interpretive one. The question is whether usage matches the
definition — never which meaning should control.

**What to check:**
- Build a defined-terms list and confirm each capitalized use matches it.
- Compare shared defined terms across the agreement and its ancillary
  documents (TSA, escrow agreement, RWI policy) for consistency.
- Flag every used-but-undefined and defined-but-unused term.

**Most exposed:** Both sides — an inconsistent term can be read to favor
either party depending on the clause.

---

### 9.2 Broken cross-reference or figure inconsistency across the document set

**Pattern:** An internal citation ("Section 5.2," "Schedule 3.10," "Exhibit
A") does not match the actual numbering of its target, or a figure that
should be identical across the document set (purchase price, cap, basket,
escrow amount, survival period) appears differently in two or more places.

**Why it matters:** A broken reference can leave a reader unable to locate
the governing provision; a figure mismatch is a factual discrepancy that can
create disputes about which number governs — both independent of any
legal-interpretation question. The question is only whether citations and
figures match everywhere they appear — never which one is correct.

**What to check:**
- Build a cross-reference map of every internal citation and confirm each
  resolves correctly, including references to schedules and ancillary
  documents.
- List every recurring dollar figure, percentage, and date, and confirm each
  recurrence matches; flag every mismatch with both source citations without
  guessing which controls.
- Check figures across documents drafted by different workstreams (e.g., an
  escrow agreement drafted separately from the purchase agreement).

**Most exposed:** Both sides — an unresolved mismatch is a drafting defect
that should be corrected before signing or closing.

---

## 10. Cross-Cutting Tax/Antitrust/Securities Routing Flags

### 10.1 Tax elections or allocations referenced without tax-counsel routing

**Pattern:** The agreement references a tax election (e.g., a Section
338(h)(10) or equivalent), a purchase-price allocation methodology, or a
specific tax treatment, and the review being performed is not itself a tax
review.

**Why it matters:** Tax elections and allocations carry substantive
consequences only a tax professional should assess; identifying the
reference is the routing step, not the analysis.

**What to check:**
- Identify every tax-election, allocation, or treatment reference, with
  source; record any election deadline `[deadline verification required]`.
- Route substantive analysis to
  `skills/tax/tax-covenants-indemnities-review/SKILL.md`; never state or
  estimate tax treatment here.

**Most exposed:** Both sides — an unrouted tax question can be missed until
after an election deadline has passed.

---

### 10.2 Antitrust or securities-law provisions referenced without specialist routing

**Pattern:** Closing is conditioned on expiration of a competition/merger-
control waiting period (e.g., Hart-Scott-Rodino or a non-U.S. equivalent), or
the consideration includes buyer stock with an exemption, lock-up, or
registration-rights reference — and the review being performed is not itself
an antitrust or securities review.

**Why it matters:** Whether a filing is required, what the waiting period is,
whether an exemption is available, and what resale restrictions apply are
questions for antitrust or securities counsel; identifying that the
agreement raises them is the routing step, not the analysis.

**What to check:**
- Identify every regulatory-clearance condition and every stock-consideration
  or resale-restriction provision, with source; record any stated deadline
  or lock-up period `[deadline verification required]`.
- Route antitrust questions to
  `skills/antitrust-competition/merger-antitrust-issue-spotter/SKILL.md` and
  securities questions to the relevant `skills/securities-capital-markets/`
  skill (see `WORKFLOW_ROUTER.md`); never conclude on clearance, exemption
  availability, or enforceability here.

**Most exposed:** Both sides — an unrouted regulatory question can delay or
unwind the transaction or create compliance risk.

---

## Reviewer Notes

- A red flag is a prompt to look closely and route to attorney attention —
  not a conclusion that a provision is unenforceable, a consent is required,
  a disclosure is complete, coverage exists under an RWI policy, or any
  figure or date is correct.
- Whether a flagged item matters depends on the deal structure, negotiated
  leverage, the client's side, the transaction stage, and the governing
  jurisdiction — all for the attorney to assess.
- This catalog never rates a cap, basket, escrow percentage, survival period,
  or fee as "market standard" without `[ATTORNEY TO CONFIRM: market context]`,
  never computes a figure or a deadline, and never supplies jurisdiction-
  specific law, tax treatment, antitrust clearance timing, or securities-law
  conclusions.
- This catalog is not exhaustive. Unusual or deal-specific patterns not
  listed here may still warrant a flag in the relevant skill's issue table
  using the table shapes in `skills/m-and-a/references/output-patterns.md`.
- See `skills/m-and-a/purchase-agreement-issue-list/SKILL.md`,
  `skills/m-and-a/indemnity-escrow-risk-review/SKILL.md`,
  `skills/m-and-a/reps-warranties-disclosure-schedule-review/SKILL.md`,
  `skills/m-and-a/third-party-consents-assignment-review/SKILL.md`,
  `skills/m-and-a/data-room-index-review/SKILL.md`,
  `skills/m-and-a/closing-deliverables-tracker/SKILL.md`,
  `skills/m-and-a/post-closing-obligations-tracker/SKILL.md`,
  `skills/m-and-a/rw-insurance-review/SKILL.md`, and
  `skills/m-and-a/transition-services-agreement-review/SKILL.md` for the full
  review workflows this catalog supports.
