# Matter Packs

A **matter pack** is a workflow bundle: a recommended *sequence* of AgentCounsel
skills for a common, multi-step legal matter, with the starting materials each
sequence needs and the attorney checkpoints along the way.

Matter packs are not legal advice and not legal work product. They are process
guidance. Every skill a matter pack sequences still produces draft work product
that a qualified, licensed attorney must review.

## How a matter pack differs from the rest of the library

- A **skill** (`skills/`) is one workflow — one step.
- `WORKFLOW_ROUTER.md` routes a single task to the one right skill.
- A **matter pack** (this directory) bundles several skills into an ordered
  sequence for a whole matter — "first run this, then this, then this."
- A **matter workspace** (`matter-workspaces/`) is the single file that holds
  one specific matter's parties, facts, deadlines, and the draft work product
  the skills produce.

A typical multi-step matter uses all of these: open a matter workspace, follow
the matter pack's sequence, run each skill, and keep the output in the
workspace.

## How to use a matter pack

1. Read the `core/` operating rules and the relevant practice profile.
2. Open the matter pack and confirm its "When to use" and "Do not use"
   boundaries fit the matter.
3. Gather the pack's required starting materials.
4. Run the skills in the recommended sequence, feeding each step's output into
   the next where the pack says so.
5. Complete each skill's Attorney Verification Checklist, and the pack's
   attorney verification checkpoints, before relying on anything.

A matter pack is a recommended path, not a rule. Skip, reorder, or repeat a
step when the matter calls for it — and route anything the pack does not cover
through `WORKFLOW_ROUTER.md`.

## Layout

```
matter-packs/
  README.md                       - this file
  antitrust-competition.md        - workflow bundles for the Antitrust / Competition practice area
  bankruptcy-restructuring.md     - workflow bundles for the Bankruptcy / Restructuring practice area
  insurance.md                    - workflow bundles for the Insurance practice area
  m-and-a.md                      - workflow bundles for the Mergers & Acquisitions practice area
  real-estate.md                  - workflow bundles for the Real Estate practice area
  securities-capital-markets.md   - workflow bundles for the Securities / Capital Markets practice area
  tax.md                          - workflow bundles for the Tax practice area
  trusts-estates.md               - workflow bundles for the Trusts & Estates practice area
```

To add a matter pack for another practice area, create
`matter-packs/<area>.md` with one section per bundle, each stating: when to use
it, the required starting materials, the recommended skill sequence, the
expected outputs, the attorney verification checkpoints, and the do-not-use
boundaries. Keep every skill reference as a real `skills/<area>/<skill>/SKILL.md`
path.
