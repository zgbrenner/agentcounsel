# Matter Workspaces

## What Is a Matter Workspace?

A matter workspace is a single-file structured scaffold for organizing **one specific legal matter**. It is the working file where an agent or team tracks that matter's parties, facts, key documents, deadlines, open action items, and the draft work product produced during the engagement.

A matter workspace is distinct from a skill and distinct from a skill template:

- A **skill** (`skills/<practice-area>/<skill-name>/SKILL.md`) defines a workflow — the steps to produce a specific type of draft legal work product.
- A **skill template** (`skills/.../templates/`) is a fill-in scaffold for the output of a single skill — for example, a risk matrix or a chronology.
- A **matter workspace** is the organizing file for the whole matter. It indexes the parties, facts, documents, deadlines, and every piece of work product produced across all the skills run for that matter.

A blank matter workspace template contains no client facts. Once you populate a copy with matter-specific information, that copy becomes **draft legal work product for attorney review**. It may be protected by the attorney-client privilege and/or the attorney work-product doctrine. Treat it accordingly.

> Matter workspaces do not provide legal advice. All content in a populated workspace is draft legal work product intended for review and adoption by a qualified, licensed legal professional.

---

## Templates in This Directory

| File | Matter Type | Primary Skills Referenced |
|---|---|---|
| `matter-workspaces/litigation-matter.md` | Active or potential litigation / dispute | `skills/litigation/matter-intake/SKILL.md`, `skills/litigation/litigation-chronology/SKILL.md`, `skills/litigation/legal-hold/SKILL.md`, `skills/litigation/demand-letter/SKILL.md`, `skills/litigation/brief-section-drafter/SKILL.md`, `skills/litigation/privilege-log-review/SKILL.md`, `skills/litigation/deposition-prep/SKILL.md`, `skills/litigation/subpoena-triage/SKILL.md` |
| `matter-workspaces/contract-review-matter.md` | Contract review, negotiation, or execution | `skills/contracts/contract-risk-review/SKILL.md`, `skills/contracts/redline-summary/SKILL.md`, `skills/contracts/nda-review/SKILL.md`, `skills/contracts/sow-review/SKILL.md` |
| `matter-workspaces/privacy-matter.md` | Privacy event, data breach, DSAR, DPA review, or processing activity | `skills/privacy/dpa-review/SKILL.md`, `skills/privacy/dsar-workflow/SKILL.md`, `skills/privacy/pia-generation/SKILL.md`, `skills/privacy/privacy-policy-gap-review/SKILL.md` |
| `matter-workspaces/regulatory-matter.md` | Regulatory inquiry, compliance review, or enforcement | `skills/regulatory/compliance-gap-matrix/SKILL.md`, `skills/regulatory/enforcement-risk-memo/SKILL.md`, `skills/regulatory/rule-change-summary/SKILL.md` |

---

## How to Use a Matter Workspace

**Step 1 — Copy the template.**
Copy the appropriate template file to a new, matter-specific location. Name it to identify the matter without embedding client-identifying information in a shared file path if that would be inappropriate. Example:

```
matters/2026-contoso-msa-review/workspace.md
```

Do not edit the blank template file itself. The blank template is a reusable scaffold; the copy you create is the live matter file.

**Step 2 — Populate the matter header.**
Fill in the matter header table: matter name, matter number, client, responsible attorney, practice profile in use, date opened, and status. Confirm that the conflicts check gate (in the litigation template) or the equivalent identification of parties has been completed before substantive work begins.

**Step 3 — Complete Gate 1 (Jurisdiction and Posture) and Gate 2 (Deadlines).**
Every workspace has a dedicated section for jurisdiction, governing law, and posture (Gate 1) and a deadlines table (Gate 2). Both are required by `core/jurisdiction-and-deadline-gates.md` before substantive analysis. Every date in the deadlines table must be independently verified by the responsible attorney. No date is ever computed by an agent or tool.

**Step 4 — Run skills and index the work product.**
Use the AgentCounsel skills appropriate to this matter type. Each skill is defined in `skills/<practice-area>/<skill-name>/SKILL.md`. As drafts are produced, record them in the workspace's Work-Product Index section, noting:
- which skill was run,
- the date,
- where the output is stored, and
- its review status (Draft / Under Review / Adopted / Superseded).

**Step 5 — Maintain the open-items list.**
As the matter progresses, update the Open Items and Action Items section. Every `[ACTION: ...]` placeholder marks a step that must be completed by a person — typically the responsible attorney or an identified team member.

**Step 6 — Attorney sign-off.**
The attorney sign-off checklist at the end of each workspace identifies the verification steps the responsible attorney must complete before the workspace is relied upon or shared. The workspace is not complete until the attorney has reviewed it, resolved all placeholders, and signed off.

---

## Treating a Populated Workspace as Privileged Work Product

A blank template contains no client facts and carries no privilege. Once populated, a workspace may contain:

- confidential client information,
- attorney mental impressions, strategy, and analysis, and
- material prepared in anticipation of litigation or for a regulatory proceeding.

Populated workspaces should be:

- labeled with the privilege designation confirmed by the responsible attorney (for example, "Privileged & Confidential — Attorney Work Product"),
- stored in systems approved for confidential matter files,
- distributed only to persons who need access for the matter, and
- protected from disclosure to third parties who could cause a waiver.

See `core/confidentiality-and-privilege.md` for the full set of operating rules that apply to all matter files.

---

## Relationship to Skills

Skills produce the individual deliverables that get indexed in a workspace. The relationship is:

```
matter workspace
  └── parties, facts, jurisdiction, deadlines, open items
  └── work-product index
        ├── [skill run] → draft risk matrix
        ├── [skill run] → factual chronology
        ├── [skill run] → legal hold notice draft
        └── [skill run] → research memo
```

A workspace does not replace a skill; it organizes the matter and tracks what the skills have produced. You can run a skill without a workspace, but once a matter involves multiple deliverables, multiple deadlines, or multiple team members, a workspace provides the single organizing file.

The `WORKFLOW_ROUTER.md` at the root of the repository maps task descriptions ("review this contract," "open a new dispute matter") to the skill that handles each task. Use it to identify which skills to run for a given matter type.

---

## Relationship to Practice Profiles

Practice profiles under `practice-profiles/` (when present) configure agent behavior for a specific practice area or engagement context. A matter workspace identifies which practice profile is in use in its matter header. The practice profile governs how the agent runs skills; the workspace records the outputs.

---

## No Backend, Runtime, or Vendor Dependency

Matter workspaces are plain Markdown files. They work wherever Markdown is readable — any text editor, any AI assistant, any document system. There is no backend, no database, no login, no script, and no vendor-specific dependency. A workspace can be opened, read, edited, and reviewed by any lawyer on any platform.

This is by design. See `core/legal-work-product.md` and the repository `README.md` for the principles that govern the library.
