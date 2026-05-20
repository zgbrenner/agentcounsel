# Workflow Router — Local-Folder Playbook

This is the task-to-skill router for using AgentCounsel as a local-folder legal playbook.

The full router lives at the repository root: [`/WORKFLOW_ROUTER.md`](../../WORKFLOW_ROUTER.md). That is the canonical version — use it for the complete mapping and the "when several skills apply" guidance.

> Read the `core/` operating rules before running any skill. Every skill produces **draft legal work product for attorney review** — never legal advice.

## Quick routes

| The task sounds like... | Open this skill |
|---|---|
| "Review this NDA" | `skills/contracts/nda-review/SKILL.md` |
| "Summarize risks in this contract / vendor agreement" | `skills/contracts/contract-risk-review/SKILL.md` |
| "What changed between these contract drafts?" | `skills/contracts/redline-summary/SKILL.md` |
| "Review this statement of work" | `skills/contracts/sow-review/SKILL.md` |
| "Research this question and write a memo" | `skills/legal-research/legal-research-memo/SKILL.md` |
| "Open a new litigation matter" | `skills/litigation/matter-intake/SKILL.md` |
| "Build a factual timeline from documents" | `skills/litigation/litigation-chronology/SKILL.md` |
| "Draft a demand letter" | `skills/litigation/demand-letter/SKILL.md` |
| "We received a subpoena" | `skills/litigation/subpoena-triage/SKILL.md` |
| "Help assess a termination" | `skills/employment/termination-risk/SKILL.md` |
| "Review this severance agreement" | `skills/employment/severance-review/SKILL.md` |
| "Review our employee handbook / policy" | `skills/employment/employee-policy-review/SKILL.md` |
| "Review a DPA" | `skills/privacy/dpa-review/SKILL.md` |
| "Handle this data subject request" | `skills/privacy/dsar-workflow/SKILL.md` |
| "Check our privacy policy for gaps" | `skills/privacy/privacy-policy-gap-review/SKILL.md` |
| "Legal review before a product launch" | `skills/product-legal/launch-review/SKILL.md` |
| "Review this marketing copy" | `skills/product-legal/marketing-claims-review/SKILL.md` |
| "Review these terms of service" | `skills/product-legal/terms-of-service-review/SKILL.md` |
| "Review the legal risk of this AI feature" | `skills/product-legal/ai-feature-review/SKILL.md` |
| "Assess enforcement exposure" | `skills/regulatory/enforcement-risk-memo/SKILL.md` |
| "Summarize this rule change" | `skills/regulatory/rule-change-summary/SKILL.md` |
| "Map requirements to our controls" | `skills/regulatory/compliance-gap-matrix/SKILL.md` |
| "Triage a proposed AI use case" | `skills/ai-governance/ai-use-case-intake/SKILL.md` |
| "Review this AI vendor's terms" | `skills/ai-governance/ai-vendor-terms-review/SKILL.md` |
| "Triage the risk of this AI model" | `skills/ai-governance/model-risk-triage/SKILL.md` |
| "Review our employee AI policy" | `skills/ai-governance/employee-ai-policy/SKILL.md` |
| "Is this brand name available? (triage)" | `skills/ip/trademark-clearance-triage/SKILL.md` |
| "Prepare / respond to a DMCA takedown" | `skills/ip/dmca-takedown/SKILL.md` |
| "Review open-source licenses" | `skills/ip/open-source-license-review/SKILL.md` |

If no skill fits, say so — do not improvise a legal workflow.
