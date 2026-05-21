> Shared reference material supporting the AgentCounsel contracts skills, used to help produce draft legal work product for attorney review — not legal advice.

# Negotiability Ratings Framework

This framework gives a reviewer a structured way to rate how negotiable a contract term is likely to be in a given deal, and to explain the basis for that rating. It is a reasoning tool — not a fixed list of which clauses are always negotiable or always fixed. Negotiability depends on factors that vary by deal, and the supervising attorney determines final negotiating strategy.

All negotiability ratings are draft assessments for attorney review. The attorney confirms whether a rating is appropriate given the client's actual leverage, the counterparty's behavior, and strategic priorities.

---

## The Rating Scale

The framework uses a four-level ordinal scale. Each level describes a general posture for how likely it is that the counterparty will engage on a given term.

### S — Standard

**Definition:** The term matches widely accepted commercial norms for this contract type. The counterparty is unlikely to engage because the term is genuinely balanced or because deviating from it would require an explanation. Raising the issue may signal inexperience or consume negotiating capital without benefit.

**Use when:**
- The provision reflects a standard allocation that is neutral or marginally favorable to the client.
- Revising it would require the client to argue against an accepted norm.
- The cost of raising it outweighs any realistic gain.

**Note:** "Standard" does not mean "optimal for the client." It means a reasonable market participant would not typically negotiate it. Attorney confirmation of this assessment is required.

---

### N — Negotiable

**Definition:** The term is worth raising and the counterparty is likely to engage, whether by accepting a modification, offering a fallback, or explaining their position. The term represents a real imbalance or risk, and movement is realistically possible given the deal context.

**Use when:**
- The provision is one-sided in a way that the counterparty should recognize.
- The client has leverage (deal value, relationship, alternatives) that makes engagement practical.
- The issue is material enough to justify the negotiating cost.
- A specific fallback or preferred position exists.

---

### D — Difficult

**Definition:** The counterparty will resist meaningful movement on this term. The term may be part of the counterparty's standard form, tied to regulatory requirements, underwritten by insurance, or a policy position they maintain consistently. Movement is possible but will require significant leverage, escalation, or trading against other terms.

**Use when:**
- The term appears in the counterparty's standard form and is rarely changed.
- The counterparty has more leverage or this is a take-it-or-leave-it context.
- Movement on this term would require conceding something elsewhere.
- The term is tied to a regulatory floor or insurance requirement `[verify jurisdiction]`.

**Note:** A Difficult rating does not mean the client should not raise the issue. It means the client should be prepared to trade something, escalate, or accept limited movement. Attorney judgment on strategy is required.

---

### W — Walk-Away

**Definition:** The term, as written, is a potential deal-breaker: it crosses the client's stated limit, creates unacceptable risk, or is one the client's internal policy or playbook identifies as a "never accept" position. The client should not proceed with this term without senior-level review and a conscious decision to accept or reject it.

**Use when:**
- The term hits a defined limit in the client's playbook or practice profile.
- The risk the term creates is disproportionate to the deal value.
- The term is inherently unenforceable or creates regulatory liability `[verify jurisdiction]`.
- The attorney has confirmed that this term cannot be accepted.

**Note:** A Walk-Away rating does not automatically end the deal. It is a signal that the matter must be escalated to a decision-maker or attorney before proceeding. Accepting a Walk-Away term is a conscious business or legal decision, not a default.

---

## Factors That Drive the Rating

The rating is not assigned mechanically. The reviewer considers each of the following factors and their interaction:

### 1. Relative Leverage

Which party needs this deal more? Which party has viable alternatives? The party with more alternatives has more leverage to push on difficult terms. A client who is one of many customers of a large platform vendor has less leverage than a client representing a significant share of the counterparty's revenue. Leverage is deal-specific — the reviewer notes the apparent leverage position and flags it for attorney confirmation.

### 2. Who Drafted the Form

A term appearing in the reviewing party's own form can often be adjusted without counterparty resistance. A term appearing in the counterparty's standard form signals an entrenched position and raises the cost of negotiation. The form's origin affects the starting rating.

### 3. Deal Value and Strategic Importance

High-value or strategically important deals warrant spending more negotiating capital. A term rated Difficult on a routine small transaction may be worth pushing on in a large or strategic deal, where the client's leverage and incentive to spend effort are both higher.

### 4. Market Norms and Standard Practice

Whether a term deviates from what is typical for this contract type, transaction size, and industry affects whether the counterparty will engage. A genuine deviation from market norms is a more credible basis for negotiation than a request to improve an already-balanced term. Market norm assessments must be verified — see `skills/contracts/references/market-benchmark-framework.md`.

### 5. Regulatory Floor

Some terms cannot be negotiated below a regulatory minimum: required DPA provisions, mandatory breach notification timelines, required disclosures. Terms that hit a regulatory floor are not negotiable below that floor regardless of leverage or deal value `[verify jurisdiction]`. The reviewer notes when a floor may apply and flags for attorney verification.

### 6. Insurance and Underwriting Constraints

Liability caps, indemnification limits, and some insurance-requirement terms may be constrained by the counterparty's insurance underwriting. If the counterparty's insurer requires a particular liability allocation, the counterparty may have limited ability to move on those terms even if it is willing. The reviewer notes this factor when it is apparent from the contract structure.

### 7. The Client's Own Position

If the client has a playbook or practice profile with defined preferred, acceptable, and unacceptable positions, the rating is calibrated against those positions. A term that falls within the client's acceptable range is not automatically Standard — but it affects priority. A term that hits a "never accept" threshold is Walk-Away regardless of other factors.

### 8. Pattern and History

If the client has prior contracts with the same counterparty, or the attorney has experience with this counterparty's negotiation posture, that history informs the rating. Counterparties who have moved on a term before are more likely to move again.

---

## How to Apply the Framework

1. **Identify the term** being rated and note its current posture in the draft (client-favorable, neutral, counterparty-favorable, or missing).

2. **Work through the factors** above. Not all factors will be relevant to every term. Note which factors are present and how they push the rating.

3. **Assign a rating** (S / N / D / W). Where factors point in different directions, flag the tension and note which factors are driving the rating.

4. **Record the basis.** The rating is only as useful as its explanation. A bare rating without reasoning is not actionable.

5. **Note confidence level.** If key factors are unknown (e.g., the client's leverage position has not been confirmed), note the uncertainty. A rating based on incomplete information should be flagged: `[CONFIRM: leverage position before finalizing rating]`.

6. **Flag for attorney review.** All negotiability ratings are draft assessments. The attorney confirms strategy, adjusts for factors the reviewer cannot observe, and decides which issues to raise and in what order.

---

## Recording a Rating

When recording a negotiability rating in an issue list or risk matrix, use the following pattern:

```
Term: [clause name or topic]
Current posture: [counterparty-favorable / neutral / missing]
Rating: [S / N / D / W]
Basis: [one to two sentences identifying the key factors]
Preferred position: [what the client wants]
Fallback position: [what the client would accept]
Attorney note: [CONFIRM: ...] or [ATTORNEY TO CONFIRM: ...]
```

See `skills/contracts/references/redline-output-guidance.md` for guidance on expressing preferred and fallback positions.

---

## Relationship to Priority Ratings

Negotiability (how moveable a term is) is separate from priority (how important it is to push on). A term can be:

- **High priority, Negotiable** — the client should invest effort here; movement is likely.
- **High priority, Difficult** — the client must decide whether to spend capital; movement is possible but costly.
- **High priority, Walk-Away** — escalate immediately; do not proceed without a decision.
- **Low priority, Negotiable** — consider raising but do not invest significant effort.
- **Low priority, Standard** — do not raise; spend capital elsewhere.

The priority rating (High / Medium / Low) reflects the materiality of the risk. The negotiability rating (S / N / D / W) reflects the practical prospect of obtaining improvement. Both are needed to build an effective negotiating strategy.

See `skills/contracts/contract-risk-review/SKILL.md` for the priority rating definitions used in the issue list.
