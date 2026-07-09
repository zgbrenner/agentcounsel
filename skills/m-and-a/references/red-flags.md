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

This catalog is a review aid. It identifies what to look for and why. It never
decides whether a provision is enforceable, whether a consent is legally
required, whether an escrow or indemnity structure is adequate, whether a
disclosure is complete, or what tax, antitrust, or securities-law treatment
applies. Whether a flagged pattern actually matters depends on the deal
structure, the negotiated leverage, the client's side, the transaction stage,
and the governing jurisdiction — all attorney judgment calls. Every flagged
item is a candidate for attorney verification, never a legal conclusion.

Three disciplines are non-negotiable and appear throughout the entries:

- **Never state what the law requires.** Enforceability of a liquidated-damages
  or exclusive-remedy clause, the standard for fraud, statutory notice or
  filing requirements, and every other legal-treatment question are
  jurisdiction-specific. Flag every such point `[verify jurisdiction]`.
- **Never compute a figure or a deadline.** Purchase price, adjustment amounts,
  earnout metrics, caps, baskets, escrow amounts, and every date are recorded
  as the document states them, and dates are flagged `[deadline verification
  required]`. This catalog never calculates a true-up, tests a covenant, or
  reconstructs a timeline beyond what is written.
- **Never rate anything "market standard."** A comparison to market practice (a
  cap, a basket, an escrow percentage, a survival period) is never asserted
  here; where a skill's workflow calls for that comparison, it is flagged
  `[ATTORNEY TO CONFIRM: market context]`.

---

## How to Use This Catalog

For each topic section relevant to the document under review:

1. Locate the relevant provision, schedule entry, index item, or ancillary
   document (or note its absence — a missing item is itself a red flag in
   several sections below).
2. Check the pattern description against the actual language or fact, quoting
   operative terms verbatim rather than paraphrasing.
3. If the pattern is present, add the item to the relevant issue table (issue
   list, risk matrix, unresolved-items list, consent tracker, gap matrix,
   deliverables tracker, obligation tracker, exclusions register, or
   completeness matrix) with a source citation.
4. Note which side (buyer, seller, or a specific role such as guarantor,
   escrow agent, or additional insured under an RWI policy) is most exposed,
   and whether the user's stated side matches the exposure profile.
5. Flag every finding for attorney review; never resolve ambiguity, decide
   enforceability, or compute a figure or date.

The sections are grouped by document family:

- **Economics** — Section 1 (used by `purchase-agreement-issue-list`,
  `indemnity-escrow-risk-review`).
- **Reps and disclosure** — Sections 2–3 (used by
  `reps-warranties-disclosure-schedule-review`, `purchase-agreement-issue-list`).
- **Indemnification and insurance** — Section 4 (used by
  `indemnity-escrow-risk-review`, `rw-insurance-review`).
- **Deal certainty** — Section 5 (used by `purchase-agreement-issue-list`).
- **Consents and transfer** — Section 6 (used by
  `third-party-consents-assignment-review`).
- **Post-closing** — Section 7 (used by `post-closing-obligations-tracker`,
  `transition-services-agreement-review`, `closing-deliverables-tracker`).
- **Diligence completeness** — Section 8 (used by `data-room-index-review`).
- **Internal consistency** — Section 9 (every skill in this catalog's scope).
- **Cross-cutting routing** — Section 10 (jurisdiction-specific and
  other-practice-area questions, every skill).
- **Reviewer Notes** — Section 11.

Where a section carries a **Direction for counsel** line, it frames a
preferred and a fallback direction the reviewing attorney may weigh from a
stated side — a direction of change, never drafted language, a negotiating
position, or a decision.

---

## 1. Purchase Price & Adjustment Red Flags

### 1.1 Working-capital target without a clear peg or methodology

**Pattern:** The agreement sets a working-capital target or peg for the
post-closing adjustment, but the peg's derivation (the historical period used,
the accounting principles applied, and any negotiated exclusions) is missing,
inconsistent with the referenced financial statements, or left to a later
schedule.

**Why it matters:** The adjustment mechanism converts directly into cash
between the parties, and an unclear or unsupported peg invites a dispute at
the very moment the parties are trying to close the file. The question is
whether the peg and its derivation are stated and internally consistent — not
what the correct peg should be, which this catalog never computes.

**What to check:**
- Quote the working-capital definition, the peg amount, and the accounting
  principles (GAAP, a defined "Applicable Accounting Principles," or the
  target's historical practices) verbatim, with source.
- Is the peg tied to a stated historical average or a specific balance sheet
  date, and is that date and methodology internally consistent with the
  financial-statements representation?
- Does a schedule that is supposed to show the peg's calculation exist, or is
  it marked "to be provided" or left blank?

**Most exposed:** Both sides at the true-up; the side whose net proceeds swing
most on an unresolved peg.

---

### 1.2 True-up dispute mechanism ambiguous or missing an arbiter definition

**Pattern:** The post-closing true-up process references an "independent
accountant" or similar arbiter to resolve disputes over the closing statement,
but the identity, selection method, scope of authority (full re-determination
vs. resolving only disputed line items), and cost allocation for that arbiter
are undefined or internally inconsistent with the definitions elsewhere in the
agreement.

**Why it matters:** A true-up dispute without a workable resolution mechanism
can stall final payment indefinitely or push the parties into unplanned
litigation over a process question rather than the substance of the dispute.
The question is whether the mechanism is complete and internally consistent —
never who would prevail in a dispute.

**What to check:**
- Record the review-period length, the objection-notice window, and the
  arbiter-selection mechanism exactly as written; flag every date `[deadline
  verification required]`.
- Is the arbiter's scope limited to line items in dispute, or does it extend
  to a full re-audit? Is that scope consistent throughout the clause?
- How are the arbiter's fees allocated, and is that allocation stated anywhere
  else in the agreement inconsistently?

**Most exposed:** The side likely to dispute the closing statement; both sides
if the mechanism stalls closing of the file.

---

### 1.3 Earnout metrics subject to buyer post-closing control with no protective covenants

**Pattern:** Consideration includes an earnout or other contingent payment
tied to post-closing performance (revenue, EBITDA, a regulatory milestone, a
product launch), and the buyer retains full post-closing operating control
over the earned business with no covenants requiring good-faith operation,
resource commitment, or restrictions on actions that could suppress the
metric.

**Why it matters:** Once the buyer controls the business, it also controls
many of the levers that drive the earnout metric (headcount, budget,
cross-selling, accounting allocations, integration timing); an agreement
silent on operating covenants leaves the seller's contingent consideration
exposed to decisions it cannot see or influence. The question is what
covenants exist and how the metric is defined and audited — not whether the
earnout will actually be achieved.

**What to check:**
- Quote the earnout metric's definition verbatim, including any adjustment or
  addback mechanics, and record the measurement period(s) `[deadline
  verification required]`.
- Does the agreement include any operating covenants (good-faith efforts, a
  standalone-operation requirement, a restriction on diverting business, a
  minimum-resource commitment) protecting the metric, or is the buyer free to
  operate as it sees fit?
- Is there a seller audit right, an information/reporting right during the
  earnout period, and a dispute-resolution mechanism for the earnout
  calculation, each with a source citation?
- Does an acceleration provision exist if the buyer sells the earned business
  or breaches the operating covenants during the earnout period?

**Most exposed:** Seller relying on the earnout as part of the deal
consideration; buyer if operating covenants are so restrictive they constrain
ordinary post-closing integration.

**Direction for counsel:** Preferred (seller) — defined operating covenants, an
audit right, and an acceleration trigger on a covenant breach or a sale of the
earned business. Fallback — a narrower metric definition with an audit right
preserved even without operating covenants. Direction only; adequacy of any
compromise is for the attorney `[ATTORNEY TO CONFIRM: market context]`.

---

## 2. Representations & Warranties Red Flags

### 2.1 Thin representations relative to the deal's risk profile

**Pattern:** The representations article omits representations a deal of this
type, size, or industry would typically address (for example, no data-privacy
representation for a data-driven business, no environmental representation
for an industrial target, no government-contracts representation for a
government-facing business), or covers a topic only at a high level of
generality.

**Why it matters:** A representation the seller never made is a risk the buyer
cannot recover for through the indemnification mechanism, however the
indemnity provisions are otherwise structured; the gap is discoverable by
comparing what is represented against the target's actual business, not by
reading the representations article in isolation. The question is what is
present and what is conspicuously absent — never whether the omission is
acceptable, which depends on the deal's negotiated risk allocation.

**What to check:**
- Build the inventory of representations actually given, with source
  citations, and compare it against the target's stated business, industry,
  and the diligence workstreams already run.
- Is a representation covering a diligence-flagged risk area (from
  `acquisition-diligence-request-list` or `data-room-index-review` findings)
  present, thin, or absent?
- Does a general "compliance with laws" representation stand in for a specific
  representation the deal's risk profile would call for?

**Most exposed:** Buyer relying on the representations for post-closing
recourse; seller if an overly broad representation creates exposure beyond
what was actually diligenced.

---

### 2.2 Broad or narrow knowledge qualifier with an undefined knowledge group

**Pattern:** Representations are qualified "to the Company's knowledge" or "to
Seller's knowledge," and the defined term either names an unreasonably narrow
group of individuals (understating what the seller organization actually
knew) or is left undefined entirely, with no stated inquiry standard
(actual knowledge vs. a duty of reasonable inquiry).

**Why it matters:** The knowledge qualifier can be the difference between a
representation that protects the buyer and one that protects only the
seller's most insulated executives; an undefined or unreasonably narrow
knowledge group can hollow out an otherwise broad representation. The
question is what the definition actually says and to whom it applies — never
whether the qualifier is fair, which depends on negotiating leverage.

**What to check:**
- Quote the "knowledge" definition in full, including the named individuals or
  role-based group and any stated inquiry standard.
- Is the knowledge group limited to individuals unlikely to know the relevant
  facts (for example, excluding the finance or compliance function on a
  representation about financial statements or regulatory compliance)?
- Is "knowledge" defined once and used consistently, or does the agreement use
  more than one knowledge standard without reconciling them (see Section 9)?

**Most exposed:** Buyer relying on a knowledge-qualified representation for
recourse; individuals named in the knowledge group, whose personal knowledge
now defines the seller's exposure.

---

### 2.3 Short or asymmetric survival period relative to the risk represented

**Pattern:** The general representations survive for a short period after
closing (or not at all), survival for fundamental representations is
undefined or conflicts with the statute-of-limitations reference elsewhere in
the agreement, and survival periods differ from the escrow or holdback term
without an explanation for the mismatch.

**Why it matters:** A representation that does not survive, or survives only
briefly, gives the buyer no practical recourse for a breach discovered after
that period — regardless of how the representation itself reads. The
mismatch between survival and the escrow term is a structural gap: a claim
window can close before, or reopen after, the funds meant to secure it are
released. The question is whether the periods are stated, consistent with
each other, and consistent with the escrow release mechanics — never whether
a given period is long enough.

**What to check:**
- Record the survival period for general representations, fundamental
  representations, tax representations, and any specifically carved-out
  representations, each `[deadline verification required]`.
- Does the escrow or holdback release date align with, precede, or follow the
  survival period for the representations it is meant to secure? Flag any
  mismatch.
- Does a fundamental-representations survival period reference "the
  applicable statute of limitations plus a stated tail," and is that
  statute-of-limitations reference itself left unspecified? Flag for attorney
  confirmation `[verify jurisdiction]`.

**Most exposed:** Buyer whose post-closing recourse window may close before a
breach is discovered; seller if survival periods are so long they leave an
open-ended exposure tail.

---

## 3. Disclosure Schedule Red Flags

### 3.1 Missing or orphan schedule

**Pattern:** A representation cross-references a numbered disclosure schedule
that does not appear in the delivered package (missing schedule), or a
delivered schedule exists with no representation pointing to it (orphan
schedule).

**Why it matters:** A missing schedule leaves a representation's qualification
unverifiable — the reviewer cannot confirm what, if anything, was actually
disclosed against it. An orphan schedule may signal a renumbering error, a
representation that was deleted without cleaning up its schedule, or content
disclosed against the wrong representation. The question is only whether the
schedule and the representation match on their face — never what should have
been disclosed.

**What to check:**
- Cross-reference every representation's schedule citation against the
  delivered schedule package, both directions.
- For a missing schedule, record it as `Schedule not provided` rather than
  assuming there is nothing to disclose.
- For an orphan schedule, note which representation it most plausibly
  qualifies and flag the mismatch for attorney and drafter attention.

**Most exposed:** Buyer relying on the schedule to define what was disclosed;
seller whose intended disclosure may not reach the representation it was
meant to qualify.

---

### 3.2 Broken cross-reference between the representation and the schedule

**Pattern:** A representation cites a schedule number or letter that does not
match the numbering used in the delivered schedule package (for example, the
representation cites "Schedule 3.10" but the delivered schedule is numbered
"Schedule 4.10," or a sub-schedule lettering scheme does not match between the
two documents).

**Why it matters:** A broken cross-reference creates the same practical
problem as a missing schedule — the qualification cannot be confirmed as
attaching to the representation it is meant to qualify — even though the
content may in fact exist somewhere in the package. The question is whether
the citation and the delivered numbering actually match, not what the content
says.

**What to check:**
- Build the full cross-reference table (representation section number to
  schedule number) and flag every mismatch.
- Is the mismatch a simple renumbering error (traceable to a plausible
  corresponding schedule) or a genuine gap with no corresponding content
  anywhere in the package?
- Does the disclosure-schedule general provisions section (governing
  cross-references among schedules) address renumbering, and is that
  provision itself internally consistent?

**Most exposed:** Both sides — the mismatch can be read against either party
depending on how a court would treat an unmatched reference `[verify
jurisdiction]`.

---

### 3.3 Overbroad general disclosure exception

**Pattern:** The disclosure schedules include a general qualifier stating that
any matter disclosed anywhere in the schedules, the data room, or a document
made available to the buyer qualifies every representation to which it could
reasonably apply — sometimes phrased broadly enough to sweep in matters an
ordinary reader would not connect to the representation at issue.

**Why it matters:** A broad general-disclosure clause can convert an
extensive, unindexed data room into a blanket qualification of every
representation, which can substantially narrow what the buyer can later claim
was not disclosed. Whether such a clause is given effect, and how broadly, is
a matter of contract interpretation this catalog does not resolve. The
question is whether the clause exists, its exact scope, and whether the data
room is organized in a way that makes "reasonable apparency" plausible to
assess — never whether the clause is enforceable.

**What to check:**
- Quote the general-disclosure qualifier verbatim, including any "reasonably
  apparent from the face of the disclosure" or similar limiting language.
- Is the data room organized and indexed well enough that a "reasonably
  apparent" standard is even assessable, or is it a single undifferentiated
  folder? Cross-check against `data-room-index-review` findings.
- Route the enforceability question to counsel `[verify jurisdiction]`; never
  conclude whether a specific data-room document actually qualifies a specific
  representation.

**Most exposed:** Buyer whose claims may be narrowed by matters buried in an
unindexed data room; seller relying on the clause to broaden its disclosure.

---

### 3.4 Stale schedule date not updated to signing or closing

**Pattern:** A disclosure schedule (or the representations bring-down
mechanic) is dated, or its content is "as of," a date materially earlier than
signing, and the agreement does not clearly require or show a schedule update
at signing, at closing, or through a supplement mechanism.

**Why it matters:** A schedule that has gone stale between its preparation
date and signing or closing can leave a material change undisclosed even
though the schedule was accurate when drafted; whether an update mechanism
exists, and whether it was actually used, determines whether the buyer is
taking the deal on current information. The question is only whether the
dates line up and whether an update mechanism exists — never what a stale
schedule should now say.

**What to check:**
- Record every date stamped on or implied by a schedule entry, and the
  signing and closing dates, each `[deadline verification required]`.
- Does the agreement provide for a schedule supplement between signing and
  closing, and if so, does the supplement mechanism affect the buyer's
  closing conditions or indemnification rights (a "sandbagging" interaction —
  see the purchase-agreement-issue-list workflow)?
- Is there evidence in the document set that a supplement was actually
  delivered, or is the schedule silent since its original date?

**Most exposed:** Buyer relying on current information at closing; seller if
an unclear update mechanism creates disclosure risk for events between signing
and closing.

---

### 3.5 "To be provided" or placeholder text left in a schedule

**Pattern:** A schedule entry reads "to be provided," "[TBD]," "[ ]," "draft
— subject to completion," or similar placeholder language, in a document set
otherwise presented as final or ready for signing or closing.

**Why it matters:** A placeholder left in a disclosure schedule at signing or
closing means the representation it purports to qualify is, in substance,
incomplete — the buyer cannot know what it is agreeing to accept as
disclosed. This is one of the most consequential and most avoidable gaps in
schedule practice, and it is entirely factual to identify. The question is
only whether the placeholder exists and where — never what content should
eventually fill it.

**What to check:**
- Scan every schedule for placeholder or draft language and list each
  instance with its schedule and representation citation.
- Is the placeholder in a schedule the closing conditions require to be
  "true, correct, and complete," creating a closing-condition gap?
- Flag every instance as an open item requiring resolution before signing or
  closing — never assume the content that would fill it.

**Most exposed:** Buyer taking the schedules as complete; seller who must
close the gap before delivery.

---

## 4. Indemnification, Caps/Baskets & Escrow Red Flags

### 4.1 Survival-to-escrow-term mismatch

**Pattern:** The representations' survival period and the escrow release
schedule do not align — for example, the escrow releases in full before the
general representations' survival period expires, or the escrow term
materially outlasts the survival period it is meant to secure with no stated
reason for the extra term.

**Why it matters:** A structural mismatch between when a claim can still be
made and when the funds meant to satisfy that claim are released can leave a
valid claim with no readily available source of recovery, or can tie up
seller proceeds longer than the risk they secure justifies. The question is
whether the dates line up — this catalog never assesses whether either period,
standing alone, is adequate.

**What to check:**
- Record the survival period(s) and every escrow release date exactly as
  written, each `[deadline verification required]`.
- Does the escrow release precede the expiration of the survival period it
  secures? By how much, as stated — do not compute the interval.
- Does the agreement address what happens to a partially escrowed claim
  pending at the scheduled release date (a holdback of the disputed amount, or
  release regardless of a pending claim)?

**Most exposed:** Buyer whose claim window may outlast the escrow; seller
whose proceeds may be held longer than the risk period justifies.

---

### 4.2 Tipping-basket vs. true-deductible ambiguity

**Pattern:** The basket or threshold provision is ambiguous about whether,
once losses cross the stated threshold, the indemnifying party owes the full
amount of losses from the first dollar (a tipping basket) or only the amount
above the threshold (a true deductible) — sometimes because the clause uses
language associated with one structure while a defined term elsewhere
suggests the other.

**Why it matters:** The difference between a tipping basket and a true
deductible can be a large swing in recovery once the threshold is crossed, and
an ambiguous clause invites a dispute over which structure the parties
actually agreed to. The question is whether the clause's own language
resolves the ambiguity — never which structure a court would apply.

**What to check:**
- Quote the basket/threshold clause verbatim and identify the specific words
  that signal a tipping basket ("all Losses, including the Basket Amount") or
  a true deductible ("Losses in excess of the Basket Amount").
- Does any other reference to the basket elsewhere in the agreement (a
  definitions section, a schedule, a side letter) use inconsistent language?
- Is the ambiguity paired with an equally ambiguous mini-basket or per-claim
  threshold, compounding the uncertainty?

**Most exposed:** Both sides — the ambiguity can be argued either way; the
side more likely to have claims near the threshold bears the greater practical
risk.

---

### 4.3 Fraud carve-out breadth or an undefined "fraud" standard

**Pattern:** The agreement carves "fraud" (or "willful breach," "intentional
misrepresentation," or similar) out of the caps, baskets, survival limits, or
exclusive-remedy provision, but does not define the term, or defines it more
broadly or narrowly than common usage (for example, extending the carve-out to
"constructive fraud" or "fraud in the inducement" without specifying which,
or limiting it to a narrow common-law-fraud standard that excludes reckless
misrepresentation).

**Why it matters:** An undefined or inconsistently scoped fraud carve-out can
either substantially widen a party's uncapped exposure beyond what was
negotiated, or narrow the carve-out's practical protection well below what
the negotiating parties assumed — and the fraud standard that actually governs
is intensely jurisdiction-specific. The question is whether the term is
defined and where it is used consistently — never what the applicable fraud
standard is.

**What to check:**
- Quote every place "fraud" (or its variants) appears in the caps, baskets,
  survival, and exclusive-remedy provisions, and note whether a single
  definition governs all of them or the term is left undefined.
- Does the carve-out apply symmetrically to both parties' indemnification
  obligations, or only to one side's?
- Flag the fraud standard itself for attorney confirmation `[verify
  jurisdiction]`; never state what conduct would meet it.

**Most exposed:** The side whose recovery depends on the fraud carve-out
actually reaching the conduct at issue; the side whose cap or basket
protection may be undermined by an overbroad carve-out.

---

### 4.4 Indemnification as exclusive remedy paired with a broad remedy waiver

**Pattern:** The agreement states that indemnification is the sole and
exclusive remedy for a breach of the agreement, and separately includes a
broad waiver of other remedies (rescission, other equitable relief, tort
claims, statutory claims) without clearly preserving fraud, willful breach, or
specific performance for pre-closing covenant breaches as carve-outs.

**Why it matters:** An exclusive-remedy provision paired with a broad waiver
can leave a party with no recourse at all outside the capped and time-limited
indemnification structure, even for conduct the parties would not ordinarily
expect to be excused. The question is what the exclusivity provision actually
excludes and what it carves back — never whether the exclusivity is
enforceable.

**What to check:**
- Quote the exclusive-remedy clause and every carve-out from it (fraud,
  specific performance, injunctive relief for restrictive covenants) verbatim.
- Does the waiver of other remedies extend to statutory or tort claims that
  might otherwise survive independent of the contract, and is that consistent
  with the fraud carve-out (Section 4.3)?
- Is the exclusivity provision itself internally consistent with the
  agreement's specific-performance clause, if any?

**Most exposed:** The side seeking recovery outside the indemnification cap or
after the survival period; the side relying on exclusivity to bound its total
exposure.

---

### 4.5 Setoff rights against escrow, holdback, or earnout asymmetric or unaddressed

**Pattern:** The agreement is silent on whether an indemnification claim may
be set off against an escrow release, a holdback, or an earnout payment, or
grants a setoff right to only one party without a matching right (or a
matching dispute-resolution mechanism) for the other.

**Why it matters:** A setoff right materially changes how an indemnification
claim is actually collected — a party with setoff rights can withhold
otherwise-due consideration unilaterally, while a party without them must
pursue collection through whatever process the agreement provides. The
question is whether the right exists, for whom, and what process governs
disputed setoffs — never whether setoff is the appropriate remedy for a given
claim.

**What to check:**
- Locate every provision addressing setoff against escrow, holdback, or
  earnout payments, and quote it verbatim.
- Is the setoff right one-sided, and does the agreement provide a
  dispute-resolution mechanism for a contested setoff before funds are
  actually withheld?
- Does the setoff provision interact with the recovery waterfall (escrow,
  then RWI, then direct claim) built in the indemnity review, and is that
  interaction stated or left to be inferred?

**Most exposed:** The party without a setoff right, whose deferred
consideration is not protected from a disputed but uncollected claim; the
party exercising setoff, if the right is contested.

---

### 4.6 Representation-and-warranty-insurance interaction inconsistent with the agreement

**Pattern:** The purchase agreement and the RWI policy or binder disagree, or
are silent relative to each other, on the retention layer's relationship to
the escrow or seller indemnity (whether RWI sits excess to a retained
seller-indemnity layer, replaces it, or the two overlap), or on whether the
policy's subrogation waiver against the seller carves out fraud consistent
with the agreement's own fraud carve-out.

**Why it matters:** A mismatch between the agreement's indemnity structure
and the RWI policy's actual terms can leave a gap in coverage the parties
believed was filled, or can create a double recovery or an unintended
overlap; whether the seller's residual indemnity, if any, is intended to be
excess, primary, or eliminated by the RWI needs to be confirmed against both
documents together, not the agreement or the policy alone. The question is
whether the two documents are consistent — this catalog never concludes
coverage exists or is adequate. Deep RWI review routes to
`skills/m-and-a/rw-insurance-review/SKILL.md`.

**What to check:**
- Record the agreement's stated interaction (if any) between the seller
  indemnity/escrow and the RWI policy, and the policy's own retention and
  subrogation-waiver language, each with a source citation.
- Does the policy's subrogation waiver against the seller carve out fraud on
  terms consistent with the agreement's own fraud carve-out (Section 4.3), or
  is there a gap or an inconsistency?
- Is the retention amount in the policy consistent with any residual
  seller-indemnity basket the agreement describes, or does a mismatch leave a
  coverage gap between the two thresholds?

**Most exposed:** Buyer relying on RWI as a recovery source; seller relying on
RWI to eliminate or narrow its residual exposure.

---

## 5. Closing Conditions & Termination Red Flags

### 5.1 Financing condition and MAC/MAE asymmetry

**Pattern:** The buyer's obligation to close is conditioned on obtaining
financing, or on the absence of a material adverse change, while the seller's
corresponding protections (a reverse termination fee, a specific-performance
right, or a financing-cooperation covenant with teeth) are thin, absent, or
one-sided — or the MAC/MAE definition itself carries carve-outs and
exceptions that run only in the buyer's favor.

**Why it matters:** A buyer with a financing out and a broad MAC condition,
but no offsetting reverse fee or specific-performance right for the seller,
can walk away from the deal with comparatively little consequence, leaving
the seller exposed to a failed process. The question is the symmetry of the
conditions and their consequences — not whether any specific MAC/MAE
definition would be triggered on the facts.

**What to check:**
- Quote the financing condition, the MAC/MAE definition (including every
  carve-out — general economic conditions, industry-wide events, changes in
  law, and any specific-to-target exceptions), and any reverse-termination-fee
  or specific-performance provision, verbatim.
- Is the MAC/MAE definition and its carve-out list symmetric between the
  parties, or does it run one direction only?
- Does the seller have a specific-performance right to force the financing to
  be drawn, or only a right to the reverse termination fee?
- Is there a financing-cooperation covenant, and does it obligate the seller
  to take steps that themselves create risk (for example, incurring debt
  before closing)?

**Most exposed:** Seller facing a financing-conditioned buyer with no
offsetting remedy; buyer if the financing condition or MAC definition is so
narrow it cannot actually protect against a real adverse event.

**Direction for counsel:** Preferred (seller) — a specific-performance right
or a reverse termination fee sized to compensate for a failed financing, and a
symmetric MAC/MAE definition. Fallback — a reverse fee without specific
performance. Direction only; adequacy of any fee is `[ATTORNEY TO CONFIRM:
market context]`.

---

### 5.2 Termination-fee asymmetry without a stated rationale

**Pattern:** The agreement sets a termination fee payable by one party on
specified termination events, and the other party's corresponding fee (if any)
is materially smaller, absent, or triggered on a narrower set of events, with
no change in the parties' respective closing conditions or deal risk that
would explain the difference.

**Why it matters:** Termination-fee structure allocates the cost of a failed
deal, and an asymmetric structure can signal — or create — an imbalance in
each side's actual commitment to close. The question is the structure and its
triggers as stated — never whether the fee amount is enforceable as
liquidated damages, which is jurisdiction-specific.

**What to check:**
- Record each party's termination fee amount and every triggering event,
  exactly as written, with a source citation.
- Is one party's fee obligation triggered by a broader set of events (for
  example, any failure to obtain financing) than the other's?
- Does the fee interact with the financing condition and MAC/MAE asymmetry
  (Section 5.1) in a way that compounds the imbalance?
- Flag enforceability of any fee as liquidated damages or an unenforceable
  penalty for attorney assessment `[verify jurisdiction]`.

**Most exposed:** The party whose termination fee is comparatively larger or
more broadly triggered.

---

## 6. Consents, Assignment & Change-of-Control Red Flags

### 6.1 Anti-assignment clause in a material contract not addressed by the deal structure

**Pattern:** A material contract in the target's business contains an
anti-assignment or consent-to-assignment clause, and the deal structure (an
asset purchase requiring assignment, or a merger or stock purchase that may
still trigger a "change of control" deemed-assignment clause) does not
account for the need to obtain that consent before or at closing.

**Why it matters:** An asset deal transfers contracts by assignment, which a
consent clause can block or delay; even a stock deal or merger can trigger a
deemed-assignment or change-of-control clause allowing the counterparty to
terminate or renegotiate. The question is whether each material contract's
transfer mechanics have been checked against the deal structure — never
whether consent, once required, will be granted.

**What to check:**
- For each material contract reviewed, quote the assignment and
  change-of-control language verbatim, and record whether the deal structure
  as stated actually implicates it.
- Is the contract a customer or supplier relationship material enough that a
  termination right, if exercised, would be a closing-condition-level risk
  rather than a post-closing housekeeping item?
- Is the consent required to be obtained as a condition to closing, or left
  as a post-closing best-efforts covenant? Cross-check against the closing
  conditions in `purchase-agreement-issue-list`.

**Most exposed:** Buyer inheriting a contract that may terminate or reprice on
the transfer; seller facing counterparty relationship risk if consent is
sought before closing is assured.

---

### 6.2 Change-of-control definition mismatched to the deal's actual structure

**Pattern:** A material contract's change-of-control clause defines the
triggering event (a specified percentage ownership change, a change in the
identity of a controlling person, a sale of substantially all assets) in a
way that either clearly is, or is ambiguously, triggered by the specific deal
structure at hand — and the review has not confirmed which.

**Why it matters:** Whether a specific transaction structure actually
constitutes a "change of control" under a given contract's own definition is
a fact-and-document-specific question that must be checked contract by
contract; assuming an answer either way risks either an unnecessary consent
request or a missed one. The question is what the definition says relative to
the stated structure — never a conclusion that consent is or is not required.

**What to check:**
- Quote the change-of-control definition verbatim and compare it, clause
  element by clause element, against the deal structure as described by the
  user.
- Does the definition turn on percentage thresholds, a defined list of
  triggering events, or a general "control" standard that is itself
  ambiguous?
- Flag every genuinely ambiguous match as an open question for counsel;
  never conclude that consent is or is not triggered.

**Most exposed:** Both sides — an unaddressed change-of-control trigger risks
termination or renegotiation rights arising after signing or closing.

---

### 6.3 Required consents not made a condition to closing

**Pattern:** A material or governmental consent is identified as necessary,
but the closing conditions do not require it to be obtained before closing —
leaving the parties to close and pursue the consent afterward, without a
stated risk allocation for the period the contract or license is technically
unauthorized.

**Why it matters:** Closing without a required consent in hand can leave a
material relationship, license, or permit vulnerable to termination or
challenge during the gap period, and the parties' agreement about who bears
that risk (indemnification, a post-closing best-efforts covenant, an escrow
holdback tied to the consent) needs to be checked, not assumed. The question
is whether the consent is a closing condition and, if not, what post-closing
protection exists — never whether closing without the consent is advisable.

**What to check:**
- List every consent identified as material, and record whether the closing
  conditions section requires it before closing, treats it as a post-closing
  covenant, or is silent.
- If deferred post-closing, is there a specific covenant, a holdback, or an
  indemnity tied specifically to the consent risk?
- Cross-check the consent list against `closing-deliverables-tracker` and
  `post-closing-obligations-tracker` to confirm the consent appears in the
  right tracker for its actual timing.

**Most exposed:** Buyer operating a business relationship without a required
consent; seller facing a counterparty dispute if consent-seeking before
closing jeopardizes the deal.

---

## 7. Post-Closing Covenants & Integration Red Flags

### 7.1 Transition services agreement scope creep or no defined exit ramp

**Pattern:** The TSA's service schedule does not match the actual separated
business's operational needs (services the business depends on are missing,
unpriced, or vaguely described), or the TSA has no defined outside end date,
migration obligation, or exit-assistance mechanism, risking indefinite
operational entanglement between the parties.

**Why it matters:** A TSA that does not match what the business actually
needs to operate can leave the recipient without a critical function at
carve-out, and a TSA with no exit ramp can keep the parties financially and
operationally entangled well past what either side intended. The question is
completeness of the schedule against the deal perimeter and the presence of a
defined exit mechanism — never what the correct price or duration should be.
Full TSA review routes to
`skills/m-and-a/transition-services-agreement-review/SKILL.md`.

**What to check:**
- Compare the TSA's scheduled services against the deal perimeter and any
  diligence functional workstream list; flag every function the business
  depends on that is missing, unpriced, or vaguely described.
- Is there a stated outside end date, a migration or transition-assistance
  obligation, and a knowledge-transfer or documentation requirement?
- Does an extension mechanism renew automatically absent affirmative
  termination, with no outside limit?

**Most exposed:** Recipient facing an operational gap or unbudgeted cost;
provider facing open-ended obligations with no defined exit.

---

### 7.2 Tax cooperation covenant vague on responsibility allocation

**Pattern:** The post-closing tax covenants require "reasonable cooperation"
between the parties for tax matters (return preparation, audits, refund
claims) but do not clearly allocate who prepares which returns, who controls
a tax contest, cost-sharing for cooperation, or the period the cooperation
obligation runs.

**Why it matters:** Tax return preparation and audit control have real cost
and risk consequences, and a vague cooperation covenant can leave both
parties uncertain about who is actually responsible when a pre-closing or
straddle-period tax issue arises after closing. The question is whether the
covenant allocates responsibility clearly — this catalog never states the
tax treatment or the correct allocation, which are for tax counsel.

**What to check:**
- Quote the tax cooperation covenant verbatim, including any allocation of
  return-preparation responsibility (pre-closing, straddle-period, and
  post-closing returns), audit and contest control, and cost-sharing.
- Is the cooperation obligation's duration stated, or open-ended? `[deadline
  verification required]` for any stated period.
- Route the substantive tax-allocation and tax-treatment questions to
  `skills/tax/tax-covenants-indemnities-review/SKILL.md`; never conclude on
  tax treatment here.

**Most exposed:** Both parties if a tax contest arises with no clear control
or cost allocation; the party bearing more of the pre-closing tax risk without
a matching cooperation obligation.

---

## 8. Data Room & Diligence Completeness Red Flags

### 8.1 Index entries with no accessible or legible corresponding document

**Pattern:** The data room index lists a file, folder, or category, but the
review is working only from the index (file and folder names), and there is
no way to confirm the underlying document is legible, complete, or actually
matches its listed description.

**Why it matters:** An index entry is not itself evidence of what the
document actually contains; treating an index listing as equivalent to a
reviewed, complete, legible document risks a false sense of diligence
completeness. The question is whether the index shows coverage for a category
— never what the underlying document says, which an index-only review cannot
confirm.

**What to check:**
- For every category assessed, note explicitly that the assessment is based
  on file and folder names only, not document content.
- Are any file names generic, truncated, or otherwise unable to confirm
  content (for example, "Scan001.pdf," "Contract (2).docx")?
- Flag every category where the index shows only a single ambiguous entry as
  a follow-up request rather than a confirmed coverage item.

**Most exposed:** The side relying on the data-room review as a proxy for
document-content review, which it is not.

---

### 8.2 Missing diligence category relative to the standard checklist

**Pattern:** A standard M&A diligence category (corporate, capitalization,
material contracts, IP, employment, litigation, regulatory, real property,
tax, insurance, financial statements, financing/debt, environmental,
data/privacy) has no corresponding entries anywhere in the index.

**Why it matters:** A category with no data-room presence at all is either a
genuine gap in the seller's disclosure or a sign the category was never
requested; either way, it is a diligence gap that should be resolved before
the diligence process is treated as complete. The question is coverage, not
substance — the index review does not assess whether the documents that do
exist are themselves sufficient.

**What to check:**
- Map every index entry to the standard diligence category set and mark each
  category `Present`, `Partial`, or `Absent`.
- Cross-check any `Absent` category against the `acquisition-diligence-request-list`
  to confirm whether the category was actually requested.
- For a target in a regulated or data-intensive industry, confirm the
  industry-specific categories (regulatory licenses, data/privacy, government
  contracts) are not silently missing from an otherwise complete-looking
  index.

**Most exposed:** Buyer relying on data-room completeness before closing;
seller whose data room may later be found incomplete during a dispute.

---

### 8.3 Stale or superseded document versions not flagged as current

**Pattern:** The index shows multiple versions of the same document (a
capitalization table, a set of financial statements, a material contract) with
no clear indication of which is the current, final, or operative version.

**Why it matters:** A schedule review, a representations bring-down, or a
closing-conditions assessment relying on a superseded version of a document
can build on stale information; identifying version ambiguity is a threshold
step before any substantive reliance on the document. The question is only
whether the index resolves which version is current — never which version's
content should govern.

**What to check:**
- Identify every document with more than one apparent version in the index,
  and record the naming pattern (dates, "v1"/"v2"/"final," etc.).
- Does the index or an accompanying cover memo state which version is
  current, or is that left ambiguous?
- Flag every ambiguous-version document as a follow-up request rather than
  assuming the most recently dated file is authoritative.

**Most exposed:** Any skill or downstream reviewer relying on the data room's
documents without confirming the current version first.

---

## 9. Internal Consistency Red Flags

### 9.1 Defined term used inconsistently or left undefined

**Pattern:** A capitalized term used throughout the agreement, a schedule, or
an ancillary document (for example, "Company," "Business," "Affiliate,"
"Knowledge," "Material Adverse Effect") is defined once but used with a
different meaning elsewhere, or is used without ever being defined.

**Why it matters:** A defined-term inconsistency can quietly change the scope
of a representation, a covenant, or an indemnity depending on which meaning
governs a given clause, and it is entirely a factual, checkable matter — not
an interpretive one. The question is whether the term is used consistently
with its definition, or with any other definition of the same term elsewhere
in the document set (for example, a TSA using "Business" differently than the
purchase agreement) — never which meaning should control.

**What to check:**
- Build a defined-terms list from the definitions section and confirm each
  capitalized use elsewhere in the document matches it.
- Compare shared defined terms across the purchase agreement and its
  ancillary documents (the TSA, the escrow agreement, the RWI policy) for
  consistency.
- Flag every used-but-undefined term and every defined-but-unused term.

**Most exposed:** Both sides — an inconsistent defined term can be read to
favor either party depending on the clause.

---

### 9.2 Broken cross-reference to a section, schedule, or exhibit

**Pattern:** A cross-reference within the agreement or an ancillary document
(a reference to "Section 5.2," "Schedule 3.10," or "Exhibit A") does not match
the actual numbering of the referenced provision, schedule, or exhibit,
typically as a result of drafting edits that were not propagated throughout
the document.

**Why it matters:** A broken cross-reference can leave a reader unable to
locate the provision that is supposed to govern a given point, and in some
cases can create genuine interpretive ambiguity about which provision was
actually meant. The question is whether the citation and its target match —
never how to resolve the reference if they do not.

**What to check:**
- Build a cross-reference map of every internal citation and confirm each
  resolves to the correct provision, schedule, or exhibit.
- Is the mismatch a simple renumbering artifact (a plausible intended target
  is identifiable) or a genuine dead-end reference?
- Check cross-references between the purchase agreement and its schedules and
  ancillary documents, not only within the agreement itself.

**Most exposed:** Both sides — resolution of a broken cross-reference is a
drafting-correction and, if disputed, an interpretation question for counsel.

---

### 9.3 Figure inconsistency across the document set

**Pattern:** A dollar figure, percentage, or date that should be identical
across the document set (the purchase price, a cap amount, a basket
threshold, an escrow amount, a survival period) appears differently in two or
more places — for example, the recitals state one purchase price and the
consideration section states another, or the cap is stated one way in the
indemnification article and differently in a related side letter or escrow
agreement.

**Why it matters:** A figure inconsistency is a factual, checkable
discrepancy that can create real disputes about which number governs,
independent of any legal-interpretation question. The question is only
whether the figures match across every place they appear — never which figure
is correct, which the parties themselves must resolve.

**What to check:**
- List every dollar figure, percentage, and date that recurs across the
  agreement, its schedules, and its ancillary documents, and confirm each
  recurrence matches.
- Flag every mismatch with both source citations, without guessing which
  figure is intended to control.
- Check figures across documents prepared by different workstreams (for
  example, the escrow agreement drafted separately from the purchase
  agreement) where inconsistency is most likely to arise unnoticed.

**Most exposed:** Both sides — an unresolved figure inconsistency is a
drafting defect that should be corrected before signing or closing, not left
to later interpretation.

---

## 10. Cross-Cutting Tax/Antitrust/Securities Routing Flags

### 10.1 Tax elections, allocations, or treatment referenced without tax-counsel routing

**Pattern:** The agreement references a tax election (for example, a Section
338(h)(10) or equivalent election), a purchase-price allocation methodology,
or a specific tax treatment for the transaction structure, and the review
being performed is not itself a tax review.

**Why it matters:** Tax elections and allocation methodologies carry
substantive tax consequences that only a tax attorney or tax professional
should assess; identifying that the agreement makes such a reference is the
necessary first step to route the question correctly, not to answer it. The
question is only whether such a reference exists and is flagged for the right
specialist — never what the tax consequence is.

**What to check:**
- Identify every tax-election, tax-allocation, or tax-treatment reference in
  the agreement, with a source citation.
- Route the substantive analysis to `skills/tax/tax-covenants-indemnities-review/SKILL.md`
  and any related tax skill; never state or estimate the tax treatment here.
- Flag the election deadline, if any, `[deadline verification required]` —
  never compute it.

**Most exposed:** Both sides — an unrouted tax question can be missed until
after an election deadline has passed.

---

### 10.2 Antitrust/HSR filing thresholds or approval conditions referenced without antitrust routing

**Pattern:** The agreement conditions closing on the expiration or termination
of a waiting period under a competition or merger-control regime (for example,
Hart-Scott-Rodino or a non-U.S. equivalent), or references a filing threshold,
and the review being performed is not itself an antitrust review.

**Why it matters:** Whether a filing is required, what the waiting period is,
and what conditions or remedies a regulator might impose are questions for
antitrust counsel; identifying that the agreement's closing conditions turn on
regulatory clearance is the routing step, not the analysis. The question is
only whether such a condition exists and is flagged for the right
specialist — never whether clearance will be obtained or on what terms.

**What to check:**
- Identify every regulatory-clearance closing condition, with a source
  citation, and record any stated filing or waiting-period deadline `[deadline
  verification required]`.
- Route the substantive analysis to
  `skills/antitrust-competition/merger-antitrust-issue-spotter/SKILL.md`;
  never state whether a filing is required or estimate clearance timing here.
- Flag any hell-or-high-water or efforts covenant tied to obtaining clearance
  for the antitrust reviewer's attention.

**Most exposed:** Both sides — a missed or mis-scoped antitrust condition can
delay or unwind the transaction.

---

### 10.3 Securities-law issues from stock consideration or resale restrictions

**Pattern:** The consideration includes buyer stock, the agreement references
an exemption from registration, a lock-up, a registration-rights arrangement,
or resale restrictions under securities law, and the review being performed is
not itself a securities review.

**Why it matters:** Whether stock consideration is exempt from registration,
what resale restrictions apply, and what disclosure obligations attach are
securities-law questions outside this catalog's and these skills' scope;
identifying that the agreement raises them is the routing step. The question
is only whether such provisions exist and are flagged for the right
specialist — never whether an exemption is available or a restriction is
enforceable.

**What to check:**
- Identify every provision addressing stock consideration, exemption
  reliance, lock-up periods, or registration rights, with a source citation.
- Record any stated lock-up or holding period `[deadline verification
  required]`; never compute it.
- Route the substantive analysis to
  `skills/securities-capital-markets/` skills relevant to the transaction (see
  `WORKFLOW_ROUTER.md`); never conclude on exemption availability or
  enforceability here.

**Most exposed:** Both sides — an unrouted securities question can create
compliance risk for the party issuing or reselling the stock.

---

## 11. Reviewer Notes

- A red flag is a prompt to look closely and route to attorney attention — not
  a conclusion that a provision is unenforceable, that a consent is required,
  that a disclosure is complete or incomplete, that coverage exists under an
  RWI policy, or that any figure or date is correct.
- Whether a flagged item matters depends on the deal structure, the
  negotiated leverage, the client's side, the transaction stage, and the
  governing jurisdiction — all for the attorney to assess.
- This catalog never rates a cap, basket, escrow percentage, survival period,
  or fee as "market standard" without `[ATTORNEY TO CONFIRM: market context]`,
  never computes a figure or a deadline, and never supplies jurisdiction-
  specific law, tax treatment, antitrust clearance timing, or securities-law
  conclusions.
- This catalog is not exhaustive. Unusual or deal-specific patterns not listed
  here may still warrant a flag in the relevant skill's issue table using the
  table shapes in `skills/m-and-a/references/output-patterns.md`.
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
