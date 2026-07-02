# Configuring AgentCounsel for a practice group

AgentCounsel can run out-of-the-box with no configuration — every skill works the first time you load it into your AI workspace and provide its Required Inputs. The configuration described here is **optional** and improves the output quality of certain skills by giving them access to the practice group's standing positions, escalation thresholds, and output preferences.

## What configuration does

A populated `practice-profiles/<area>.md` file gives ~20 of AgentCounsel's skills access to:

- **Standard Positions** — the group's default negotiating positions, severance grids, standing policies, etc.
- **Escalation Thresholds** — when an AI-assisted draft must stop and route to a human reviewer (deal size, liability cap floor, jurisdiction outside scope, etc.).
- **Preferred Output Style** — deliverable format, risk-rating scheme, tone, length conventions.
- **Source-of-Truth Documents** — where the group's authoritative playbooks, templates, control libraries, and registers live.
- **Attorney Review Requirements** — which deliverables require which level of reviewer.
- **Prohibited Assumptions** — what the agent must never assume and must always confirm.

Skills that consume the profile are listed in `practice-profiles/README.md`. The other ~170 skills are unaffected by the profile's presence.

## How to configure

### Option 1: Run the cold-start interview (recommended for full practice-group adoption)

Each practice area has a cold-start interview skill at `skills/setup/<area>-cold-start-interview/SKILL.md`. The interview walks a supervising attorney through every section of the profile and produces a populated draft for attorney review and approval. Plan for 30-60 minutes per practice area.

### Option 2: Edit the profile directly

Open `practice-profiles/<area>.md` and replace every `[CONFIRM: ...]` placeholder with the group's actual answer. Have a supervising attorney review and approve before use.

### Option 3: Configure incrementally

Start with no profile and run skills as needed. When you notice a skill repeatedly asking for the same standing positions, populate just that section of the profile. The profile sections are independent — a partially-populated profile still works, with the unpopulated sections treated as silent.

## How skills use the profile

Skills that consume the profile expect it to be loaded into the same AI workspace as the skill. The skill reads the profile's tables when running, benchmarks the matter facts against the standing positions, and flags deviations or profile-silent items for attorney review.

Profile is reference-only — every conclusion is still routed for attorney verification per the skill's normal gates. The profile informs the draft; the attorney owns the decision.

## What configuration does NOT do

- It does not modify any skill file or any `core/` operating rule.
- It does not change escalation behavior for skills not listed in `practice-profiles/README.md`.
- It does not substitute for attorney review. Profile is a configuration record approved by the practice group; it is not legal advice.
- It does not persist across AI sessions automatically — each session loads whatever files you provide. Platform packs and Claude Code plugin bundles can include the profile if you build them with the populated profile present.

## Where to go next

- `practice-profiles/README.md` — list of skills that consume profile data.
- `skills/setup/` — cold-start interviews per practice area.
- `QUICKSTART.md` — running skills without any configuration.
- `README.md` — the rest of AgentCounsel.
