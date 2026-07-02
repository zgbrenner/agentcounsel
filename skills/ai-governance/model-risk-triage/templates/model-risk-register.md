# Model Risk Register

> Draft legal work product for attorney and governance review. Not legal advice.
> Fill-in structure for the Model Risk Triage skill — Workflow step 12 ("Assign risk tier and build the risk register") and Output Format section 3 ("Risk Register").
> Do not paste client-sensitive facts into a reusable copy of this template.

**Model name / version:** [name and version]
**Provider / source:** [vendor API / open-source repository / internally trained]
**Intended use:** [one-line description of intended use]
**Overall risk tier:** [Low / Medium / High — governance triage signal, not a legal conclusion]
**Preparer:** [name]   **Triage date:** [date]

## Risk Register

| Risk Dimension | Finding | Risk Level | Recommended Control | Owner |
|---|---|---|---|---|
| Intended use / foreseeable misuse | [finding from provided materials, or `[CONFIRM: ...]`] | Low / Medium / High | [control or action] | [owner] |
| Affected individuals / harm severity | [finding from provided materials, or `[CONFIRM: ...]`] | Low / Medium / High | [control or action] | [owner] |
| Accuracy and reliability | [finding from provided documentation only — never assumed metrics] | Low / Medium / High | [control or action] | [owner] |
| Bias and fairness | [finding; note need for specialist review where applicable] | Low / Medium / High | [control or action] | [owner] |
| Transparency / explainability | [finding from provided materials, or `[CONFIRM: ...]`] | Low / Medium / High | [control or action] | [owner] |
| Data provenance and rights | [finding from provided materials, or `[CONFIRM: ...]`] | Low / Medium / High | [control or action] | [owner] |
| Security and abuse resistance | [finding from provided materials, or `[CONFIRM: ...]`] | Low / Medium / High | [control or action] | [owner] |
| Human oversight design | [finding from provided materials, or `[CONFIRM: ...]`] | Low / Medium / High | [control or action] | [owner] |
| Monitoring and incident response | [finding; flag if no monitoring plan is in place] | Low / Medium / High | [control or action] | [owner] |

## Row guidance

- **Finding** — what the provided documentation and inputs show for this dimension. Never fabricate benchmark results, accuracy metrics, or technical characteristics; if documentation is unavailable, state that and mark `[CONFIRM: ...]`.
- **Risk Level** — Low / Medium / High per dimension, assigned in Workflow step 12.
- **Recommended Control** — a specific control or action (technical, process, contractual, legal, or governance) for each High and Medium item, per Workflow step 13.
- **Owner** — the function or role responsible for the control.

## Open items for attorney and governance verification

- [ ] Findings trace to provided documentation, not assumed model characteristics.
- [ ] Bias and fairness items escalated to a technical specialist where the use case involves consequential decisions about protected categories.
- [ ] No law or regulation asserted as applying without attorney verification.
- [ ] Any row marked `[CONFIRM: ...]` resolved before deployment.

*Label the full document: DRAFT — For Attorney and Governance Review — Not Legal Advice.*
