# Demo script

A short walkthrough for a **2–4 minute screen recording** of AgentCounsel. It
shows the core loop — pick a pack, run a skill, organize a matter, run a quality
check, hit the attorney-review gate — plus the evals and the site. Use fictional
facts only; never show real client data.

> One framing line to open and close with: *"AgentCounsel produces draft work
> product for attorney review. It is not an AI lawyer and it does not give legal
> advice — a licensed attorney reviews every output."*

Total target: ~3 minutes. Times are guides.

## 0:00 — Hook (15s)

- On camera or voiceover: "This is AgentCounsel — an open-source, Markdown-native
  library of *supervised* legal workflows for AI agents. Not an AI lawyer.
  Everything it produces is draft work product an attorney reviews."
- Show the repo `README.md` or the site home page briefly.

## 0:15 — Pick a platform pack (30s)

- Open the **Packs** page (site `packs/index.html`, or the deployed Pages site).
- Point out: one file per practice area, for ChatGPT, Claude, and Gemini, plus
  repo-agent instructions for Cursor/Codex.
- Expand the **Contracts** pack detail: show included skills, quality checks,
  playbooks, and attorney-review requirements.
- Say: "I'll upload the Contracts pack to a project and apply the safety rules."

## 0:45 — Choose the NDA review workflow (40s)

- In your AI tool (or just open the skill file), go to
  `skills/contracts/nda-review/SKILL.md`.
- Show the eight-section structure: Required Inputs, Legal Safety Rules, Workflow,
  Output Format, Attorney Verification Checklist.
- Provide fictional inputs: "Client is the receiving party; stand-alone commercial
  NDA; [paste a short fictional NDA]."
- Show the structured draft it produces: triage rating, key-terms table, risk
  table, prioritized redline points — with `[CONFIRM: ...]` placeholders where it
  could not be certain.

## 1:25 — Initialize a matter workspace (30s)

- In a terminal:

  ```
  py scripts/init_matter_workspace.py "Contoso NDA Review" --practice-area contracts
  ```

- Open the created folder under `matters/` (git-ignored). Show
  `matter_profile.md`, `source_log.md`, `citation_map.md`, `outputs/`, and
  `attorney_review.md`.
- Say: "For multi-document or multi-step work, the workspace organizes facts,
  sources, deadlines, and outputs — all plain Markdown."

## 1:55 — Run a quality check (30s)

- Open `skills/legal-methodology/citation-integrity-check/SKILL.md` (or
  `source-validation`).
- Run it over the NDA draft. Show it classifying statements (source-supported,
  unsupported, authority-requiring-verification) and flagging anything to verify.
- Say: "The quality layer surfaces issues for verification — it does **not** verify
  the law automatically."

## 2:25 — Attorney-review gate (20s)

- Open the workspace's `attorney_review.md` (or the skill's Attorney Verification
  Checklist).
- Show the unchecked checklist. Say: "The agent never checks these boxes. A
  supervising attorney resolves every placeholder and signs off before anything is
  relied upon, sent, or filed."

## 2:45 — Evals and coverage (15s)

- In a terminal:

  ```
  py scripts/check_evals.py
  py scripts/run_evals.py --strict --quiet
  ```

- Briefly show `reports/eval-coverage.md`. Say: "186 eval files, run with no API
  keys. They check structure and safety signals — not legal correctness."

## 3:00 — Site navigation + close (15s)

- Show the site: Home → How it works → Skills → Packs.
- Close with the framing line: "Markdown-native, portable across AI tools,
  MIT-licensed, and supervised end to end. Draft work product for attorney review —
  not legal advice."

## Recording tips

- Keep terminal font large and the window clean.
- Use only fictional names ("Contoso", "Client A") and fictional NDA text.
- Delete the demo workspace afterward (`matters/` is git-ignored, so it won't be
  committed regardless).
- If you trim to 2 minutes, cut the matter-workspace and evals sections and keep:
  pack → NDA skill → attorney-review gate → close.
