# Example: Board Minutes

> **Illustrative example — not legal advice.** This is a sample of what the Board Minutes skill (`skills/corporate/board-minutes/SKILL.md`) produces. Every entity, person, date, resolution, and figure in it is **fictional** and was invented for illustration. It is a *draft* set of minutes — attorney work product to be reviewed, revised, and authorized before it becomes a corporate record — not a finished or adopted minute, and not legal advice. See `examples/README.md`.

## Scenario

Cascade Instruments, Inc. is a fictional privately held maker of laboratory instruments. Its board of directors held a regular quarterly meeting, and the corporate secretary asked for a first-pass minutes draft from the agenda, the board deck, and their notes before outside counsel finalizes it. Seven directors sit on the board; five attended, which the secretary reports met quorum. The agenda had four substantive items: approval of the prior meeting's minutes, appointment of a new Chief Financial Officer, approval of an increase to the equity incentive plan pool, and approval of a supply agreement with a company affiliated with one of the directors — who recused. For one item the notes did not capture the discussion, so the draft keeps a visible placeholder rather than inventing content. This example shows how the skill records **quorum as reported while flagging the threshold itself for attorney verification**, handles a recusal, and preserves attorney-verification framing throughout. Because a quorum was present, the skill proceeds; had it not been, the skill would have stopped and inserted a defect notice instead.

## Illustrative Output

> **Draft legal work product for attorney review. Not legal advice.** These are draft minutes prepared from the materials provided. They are attorney work product and must not be circulated as if adopted. An attorney must review, revise, and authorize finalization before adoption as a corporate record.

---

# Minutes of Meeting of the Board of Directors
## Cascade Instruments, Inc.

**Meeting type:** Board of Directors — Regular Quarterly Meeting
**Date:** `[CONFIRM: date of meeting]`
**Time:** `[CONFIRM: time called to order]` — `[CONFIRM: time adjourned]`
**Location / Platform:** `[CONFIRM: physical address or virtual platform and access method — materials indicate a hybrid meeting]`
**Draft prepared by:** Drafting agent, for the Corporate Secretary and outside counsel
**Draft date:** `[date of this draft]`

---

## Opening

`[CONFIRM: name and title]`, serving as Chair, called the meeting to order. Notice and quorum are addressed below.

**Notice.** Notice of the meeting was duly given to all directors in accordance with the bylaws and applicable law. `[verify jurisdiction]` `[CONFIRM: method and date of notice; confirm notice was timely and proper — the materials reference a notice email but do not state the date.]`

**Quorum.** The Corporate Secretary confirmed that a quorum of directors was present: **five of seven directors** attended. `[CONFIRM: quorum requirement under the certificate of incorporation, bylaws, and applicable law — do not assume a default threshold. The number present is recorded from the attendance list; whether it satisfies the governing quorum requirement is for the attorney to confirm.]` `[verify jurisdiction]`

**Secretary.** `[CONFIRM: name]` served as Secretary of the meeting.

---

## Attendees

### Directors Present

| Name | Capacity |
|------|----------|
| `[CONFIRM: name]` | Director / Chair |
| `[CONFIRM: name]` | Director / Chief Executive Officer |
| `[CONFIRM: name]` | Independent Director |
| `[CONFIRM: name]` | Independent Director |
| `[CONFIRM: name]` | Director |

### Directors Absent

| Name | Capacity |
|------|----------|
| `[CONFIRM: name]` | Independent Director |
| `[CONFIRM: name]` | Director |

### Management and Other Attendees

| Name | Title / Role | Reason for Attendance |
|------|-------------|----------------------|
| `[CONFIRM: name]` | VP Finance | Presented on Agenda Item 2; candidate for CFO appointment |
| `[CONFIRM: name]` | General Counsel & Corporate Secretary | Recorded the meeting |

### Guests

| Name | Firm / Organization | Role |
|------|---------------------|------|
| `[CONFIRM: name]` | `[CONFIRM: firm]` | Outside counsel |

*`[CONFIRM: all attendees and their roles. Note any attendee who joined or departed mid-meeting and the agenda item at which that occurred — the materials indicate the CFO candidate left the room during the Item 2 vote.]`*

---

## Approval of Prior Minutes

The Secretary presented the minutes of the Board of Directors meeting held on `[CONFIRM: prior meeting date]`.

**Resolution:**

> RESOLVED, that the minutes of the regular meeting of the Board of Directors held on `[CONFIRM: prior meeting date]` are hereby approved as presented. `[CONFIRM: conform resolution language to the organization's governing documents and house style]`

**Vote:** Approved unanimously by the directors present. `[CONFIRM: vote count]`

---

## Agenda Item 1: Appointment of Chief Financial Officer

**Materials presented:** Board deck, "CFO Appointment" section, and a candidate summary `[CONFIRM: exhibit designation].`

**Discussion:**

Management presented the recommendation to appoint the current VP Finance as Chief Financial Officer, reviewing the candidate's background and proposed terms as reflected in the board deck. The candidate left the room for the deliberation and vote. `[CONFIRM: confirm this discussion summary against the materials; expand only from what the deck and notes support — do not add content that was not presented.]`

**Resolution:**

> RESOLVED, that `[CONFIRM: name]` is hereby appointed as Chief Financial Officer of the Corporation, effective `[CONFIRM: effective date]`, with the authority and responsibilities set forth in the Corporation's bylaws and as determined by the Board. `[CONFIRM: conform resolution language to the organization's governing documents and house style; confirm officer-appointment authority and any compensation approvals required.]`

**Vote:** Approved unanimously by the directors present. `[CONFIRM: vote count]`

---

## Agenda Item 2: Increase to Equity Incentive Plan Pool

**Materials presented:** Board deck, "Equity Pool" section; proposed form of resolution `[CONFIRM: exhibit designation].`

**Discussion:**

[PLACEHOLDER — Summarize discussion based on materials provided. The notes provided do not describe the board's discussion of this item beyond the proposed resolution. This placeholder is retained rather than filled, and is flagged in the Open Items List.]

**Resolution:**

> RESOLVED, that the number of shares reserved for issuance under the Corporation's `[CONFIRM: plan name]` Equity Incentive Plan is hereby increased by `[CONFIRM: number of shares]` shares, subject to `[CONFIRM: any required stockholder approval — verify jurisdiction and governing documents]`. `[CONFIRM: conform resolution language to the organization's governing documents and house style]`

**Vote:** `[CONFIRM: vote count — materials do not state whether unanimous or a tally]`

---

## Agenda Item 3: Approval of Supply Agreement with Affiliated Party (Related-Party Transaction)

**Materials presented:** Board deck, "Supply Agreement" section; draft agreement `[CONFIRM: exhibit designation].`

**Discussion:**

Management presented a proposed supply agreement with `[CONFIRM: counterparty name]`, a company affiliated with a member of the Board. `[CONFIRM: name]` disclosed a conflict of interest with respect to this item — `[CONFIRM: describe the nature of the conflict — the materials indicate the director holds an ownership interest in the counterparty]` — and recused, leaving the meeting for the deliberation and vote on this item. `[verify jurisdiction]` `[ATTORNEY TO CONFIRM: adequacy of disclosure and recusal procedure under the governing documents and applicable law, including any disinterested-director or independent-committee approval requirements for a related-party transaction.]`

**Resolution:**

> RESOLVED, that the Corporation is hereby authorized to enter into the supply agreement with `[CONFIRM: counterparty name]` on the terms presented, and the officers of the Corporation are authorized to execute and deliver the agreement and to take such further actions as they deem necessary or advisable to carry out the intent of this resolution. `[CONFIRM: conform resolution language to the organization's governing documents and house style]`

**Vote:** Approved by the disinterested directors present, with `[CONFIRM: name]` having recused. `[CONFIRM: vote count of disinterested directors]`

---

## Other Business

`[CONFIRM: note any other business raised, or state "There was no other business." — the materials do not reflect additional business.]`

---

## Adjournment

There being no further business to come before the Board, the Chair declared the meeting adjourned at `[CONFIRM: time of adjournment]`.

---

## Signatures

These minutes are certified as a true and accurate record of the proceedings of the Board of Directors of Cascade Instruments, Inc. held on `[CONFIRM: date]`.

`[ATTORNEY TO CONFIRM: signature and attestation requirements under the governing documents and applicable law]` `[verify jurisdiction]`

**Chair:** Signature: ___________________________  Name: `[CONFIRM]`  Date: ___________________________

**Secretary:** Signature: ___________________________  Name: `[CONFIRM]`  Date: ___________________________

---

### Open Items List

- Meeting date, time called to order, and time of adjournment — not stated in the materials `[CONFIRM].`
- Meeting location / platform — hybrid indicated, details unconfirmed `[CONFIRM].`
- Method and date of notice `[CONFIRM]`; whether notice was proper or waived `[verify jurisdiction].`
- **Quorum requirement (threshold) under the governing documents and applicable law** `[verify jurisdiction]` — five of seven directors is recorded as present; the governing threshold is unverified.
- All director, management, and guest names `[CONFIRM].`
- Mid-meeting departures — CFO candidate (Item 1) and recused director (Item 3) `[CONFIRM].`
- Prior meeting date for the minutes approved `[CONFIRM].`
- Agenda Item 2 discussion summary — `[PLACEHOLDER]` retained; notes did not describe the discussion.
- Vote counts for Items 2 and 3 `[CONFIRM].`
- Effective date and any required compensation approval for the CFO appointment `[CONFIRM].`
- Equity pool share number and any required stockholder approval `[CONFIRM] [verify jurisdiction].`
- Related-party transaction: adequacy of disclosure, recusal procedure, and disinterested-approval requirements `[ATTORNEY TO CONFIRM] [verify jurisdiction].`
- Resolution language for every item — conform to house style and governing documents `[CONFIRM].`
- Exhibit designations for all referenced materials `[CONFIRM].`
- Signature and attestation requirements `[ATTORNEY TO CONFIRM] [verify jurisdiction].`

### Assumptions

- Assumed this was a regular quarterly meeting of the full Board (not a committee meeting), per the agenda provided.
- Assumed the attendance count (five of seven directors present) as reported by the Corporate Secretary; the identities and the governing quorum threshold are unverified.
- Assumed a neutral standard resolution form for each item because no house-style precedent or populated `practice-profiles/corporate.md` was supplied; each resolution is flagged to be conformed.
- Assumed the CFO candidate and the recused director each left the room for the relevant vote, per the notes; the exact points of departure and return are flagged.
- Assumed the supply-agreement counterparty is an affiliate of a director, giving rise to the recusal, per the materials; the nature of the conflict is flagged for confirmation.
- No assumption was made about notice validity, quorum sufficiency, voting standards, related-party-approval requirements, or signature requirements; each is an attorney-verification item.

---

## Attorney Verification Checklist

- [ ] The meeting actually took place on the date, at the time, and at the location stated.
- [ ] Notice was proper under the governing documents and applicable law, or was effectively waived by all required parties. `[verify jurisdiction]`
- [ ] Attendance is accurate and complete, including any directors who joined or left during the meeting.
- [ ] A quorum was present throughout the portions of the meeting at which action was taken, as required by the governing documents and applicable law. `[verify jurisdiction]`
- [ ] Each resolution accurately states the action approved and the vote (or unanimous approval without objection).
- [ ] Resolution language conforms to the organization's governing documents, any applicable shareholder or board approval requirements, and house style.
- [ ] All exhibits referenced in the minutes are identified correctly and are attached or on file.
- [ ] Prior minutes were properly presented and approved.
- [ ] No action taken at the meeting exceeded the authority granted to the board or committee by the governing documents or applicable law. `[verify jurisdiction]`
- [ ] Any conflicted director or member was identified, disclosed, and handled appropriately. `[verify jurisdiction]`
- [ ] Discussion summaries accurately reflect what occurred and do not include content that was not discussed.
- [ ] The minutes do not contain privileged communications that should be withheld from the formal corporate record.
- [ ] The chair and secretary have signed or will sign the minutes before they are adopted and filed.
- [ ] No legal authority, statute, or case law has been asserted in the draft without verification.
- [ ] All placeholders and open items are resolved before the minutes are adopted as a corporate record.
- [ ] The finalized minutes are filed in the corporate record book or equivalent repository as required by the governing documents and applicable law. `[verify jurisdiction]`
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.

---

*This example is illustrative and built on fictional facts. It demonstrates the structure and discipline of the Board Minutes skill; it is not legal advice and must not be used as a template for a real matter. Run the skill on your own inputs and have a qualified attorney review, revise, and authorize the minutes before adoption.*
