# A17 · Regulated AI: Compliance, Safety & Governance

**26 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../A16-system-design-and-interviews/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [A17.01](lessons/A17.01.md) | data types and sensitivity | Foundation |
| [A17.02](lessons/A17.02.md) | compliance vs engineering control | Foundation |
| [A17.03](lessons/A17.03.md) | identity and consent | Foundation |
| [A17.04](lessons/A17.04.md) | threat modeling | Foundation |
| [A17.05](lessons/A17.05.md) | clinical risk and human accountability | Foundation |
| [A17.06](lessons/A17.06.md) | GDPR/DSGVO basic obligations | Core |
| [A17.07](lessons/A17.07.md) | GoBD context | Core |
| [A17.08](lessons/A17.08.md) | ISO27001 scope and risk process | Core |
| [A17.09](lessons/A17.09.md) | consent and purpose limitation | Core |
| [A17.10](lessons/A17.10.md) | auditability | Core |
| [A17.11](lessons/A17.11.md) | data retention/deletion | Core |
| [A17.12](lessons/A17.12.md) | explainability, evidence and uncertainty | Core |
| [A17.13](lessons/A17.13.md) | human-in-the-loop gates | Core |
| [A17.14](lessons/A17.14.md) | safe escalation | Core |
| [A17.15](lessons/A17.15.md) | domain review | Core |
| [A17.16](lessons/A17.16.md) | approved data sources | Core |
| [A17.17](lessons/A17.17.md) | policy-as-code | Principal |
| [A17.18](lessons/A17.18.md) | immutable/tamper-evident audit evidence | Principal |
| [A17.19](lessons/A17.19.md) | access logs and key controls | Principal |
| [A17.20](lessons/A17.20.md) | DPIA concept | Principal |
| [A17.21](lessons/A17.21.md) | incident and breach playbooks | Principal |
| [A17.22](lessons/A17.22.md) | decision provenance | Principal |
| [A17.23](lessons/A17.23.md) | stakeholder review | Principal |
| [A17.24](lessons/A17.24.md) | compliance test matrix | Principal |
| [A17.25](lessons/A17.25.md) | safe deployment and continuous monitoring | Principal |
| [A17.26](lessons/A17.26.md) | healthcare risk scenarios | Principal |

## Guided walkthrough

Translate policy and domain risk into observable controls. The lesson examples are fixtures, and operational obligations require the applicable policy and specialist review.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Classify data and accountable decisions (A17.01–A17.05)

1. **[A17.01 · data types and sensitivity](lessons/A17.01.md).** Identify data subjects, data categories, intended use and sensitivity. GDPR special categories include data concerning health. Derived or inferred fields also need assessment. Three fields include two classified sensitive in the fixture. A direct-identifier-only policy captures one.
2. **[A17.02 · compliance vs engineering control](lessons/A17.02.md).** Separate obligation, design control, operating procedure and evidence. Define scope and effectiveness criteria before sampling. Five controls documented and three evidenced imply operating evidence coverage 3/5.
3. **[A17.03 · identity and consent](lessons/A17.03.md).** Verify identity, then resolve a separate, purpose-specific legal basis. Where consent is relied upon it is subject to applicable conditions and withdrawal. A present identity and withdrawn consent deny the consent-only fixture.
4. **[A17.04 · threat modeling](lessons/A17.04.md).** Map actors, sensitive data flows and privileged operations, then check controls and owner at each crossing. Four flows require a named control. Three mapped yields one uncovered.
5. **[A17.05 · clinical risk and human accountability](lessons/A17.05.md).** Determine intended purpose and applicable classification with domain and regulatory review. Preserve accountable human decision authority and a clear escalation path. One required human step and zero approvals imply zero simulated actions.

### Implement policy and human review controls (A17.06–A17.16)

6. **[A17.06 · GDPR/DSGVO basic obligations](lessons/A17.06.md).** Map applicable GDPR principles and legal basis, special-category conditions where relevant, rights procedures and accountability evidence. Assess applicability and local law with the responsible team. Two purposes recorded, only one with legal-basis evidence, leaves one review item.
7. **[A17.07 · GoBD context](lessons/A17.07.md).** German GoBD guidance applies to applicable books, records and documents with tax relevance. Design documented processes, accessible evidence and change history according to the applicable requirement. Three modeled revisions kept as append-only events preserve three records. Overwriting a single row retains one revision.
8. **[A17.08 · ISO27001 scope and risk process](lessons/A17.08.md).** Define information security management system scope, context, risk assessment and treatment. Scope and applicable controls need evidence and continuous improvement. Of four systems, three have reviewed risks. Risk review coverage equals 0.75.
9. **[A17.09 · consent and purpose limitation](lessons/A17.09.md).** Record purposes and applicable lawful bases. Evaluate compatibility or identify another lawful route before changing processing. Fixture uses a strict purpose allowlist. Consent covers support only. Proposed analytics is denied by the allowlist.
10. **[A17.10 · auditability](lessons/A17.10.md).** Record timestamp, actor, source versions, policy, decision, and response status. Restrict audit readers and apply minimization and retention. Five required evidence fields, four present, gives one missing.
11. **[A17.11 · data retention/deletion](lessons/A17.11.md).** Plan deletion through derivatives and restore workflows. Verify actual control behavior including legal exceptions, schedules and failures. Primary and vector stores are required. Deleting only primary leaves one unresolved target.
12. **[A17.12 · explainability, evidence and uncertainty](lessons/A17.12.md).** Show source and version, surface uncertainty and preserve conditions under which the explanation was produced. Test whether evidence supports the displayed claim. Two supported claims among three yields supported share 2/3.
13. **[A17.13 · human-in-the-loop gates](lessons/A17.13.md).** Place approval before effects, bind it to exact artifact identity, constrain reviewer role and enforce expiry. Keep approvals observable and revocable as policy requires. Approved version 2 does not authorize proposed version 3.
14. **[A17.14 · safe escalation](lessons/A17.14.md).** Route uncertain, out-of-scope and severe cases to an accountable workflow. Measure queue delay and provide a safe failure state while waiting. Two escalations with a capacity of one leave one pending.
15. **[A17.15 · domain review](lessons/A17.15.md).** Use qualified review to define unacceptable errors, representative fixtures and acceptance gates. Record disagreements and amendments to the rubric. One required reviewer and zero approved reviews must block release.
16. **[A17.16 · approved data sources](lessons/A17.16.md).** Maintain approved source versions, usage permissions and ingestion evidence. Quarantine unapproved sources and reconcile dependent artifacts on revocation. Of three sources, two carry approval. Exactly two may enter the fixture.

### Verify evidence, escalation, and deployment (A17.17–A17.26)

17. **[A17.17 · policy-as-code](lessons/A17.17.md).** Encode explicit decision inputs and outcomes, keep policy versioned and review tests across permit, denial and missing-input paths. Missing consent is represented by None. A policy requiring exact True denies.
18. **[A17.18 · immutable/tamper-evident audit evidence](lessons/A17.18.md).** Hash-linked audit entries detect changes relative to a trusted checkpoint. External anchoring or protected storage addresses full-chain rewriting and deletion. An intact sequence of two expected hashes matches. Removing one breaks the anchored count.
19. **[A17.19 · access logs and key controls](lessons/A17.19.md).** Correlate access context and key use, log allowed and denied administrative actions and restrict log access. Retain relevant version identifiers without secret material. One decrypt record has no correlated request ID among three. Evidence coverage is 2/3.
20. **[A17.20 · DPIA concept](lessons/A17.20.md).** GDPR Article 35 describes DPIAs for processing likely to result in high risk, with examples and roles. Document findings, safeguards and residual risk through the responsible stakeholders. Three fixture risks have owners, mitigations exist for two, leaving one unresolved.
21. **[A17.21 · incident and breach playbooks](lessons/A17.21.md).** Record when the organization became aware of the incident, assign a decision owner, and document the applicable notification assessment and its evidence. In the fictional exercise, a 72-hour reference window makes hour 60 timely and hour 75 late. The exercise measures the playbook’s timing logic.
22. **[A17.22 · decision provenance](lessons/A17.22.md).** Capture stable version identifiers, evidence references and reviewer decision. Restrict audit disclosure and reconstruct the chain from a trace ID. Reconstruction requires source, policy and model. Source and model alone leave one missing.
23. **[A17.23 · stakeholder review](lessons/A17.23.md).** Identify accountable owners for domain, privacy, operations and security. Define decision, exceptions, residual risk and escalation timeline. Required roles are privacy, lead and operations. Two responses leave one pending.
24. **[A17.24 · compliance test matrix](lessons/A17.24.md).** Map control IDs to test cases, environments, owner and failure handling. Cover negative and unknown states alongside successful paths. Controls C1,C2,C3 and coverage C1,C3 leave one gap.
25. **[A17.25 · safe deployment and continuous monitoring](lessons/A17.25.md).** Predefine a safe degraded mode, telemetry, canary gates and rollback criteria, then exercise failure in isolation. Three canary checks have one critical failure. An all-pass rule declines promotion.
26. **[A17.26 · healthcare risk scenarios](lessons/A17.26.md).** Separate administrative assistance from high-stakes advice and decisions according to intended use. Require evidence and qualified review. Route unresolved cases to a synthetic review queue. A proposed effect with reviewer approval but no evidence stays blocked.

### Put it together

For a clinical decision-support scenario, record source versions, policy decision, uncertainty, and reviewer outcome. If evidence is missing, keep the proposed action blocked and route it for review. Verify that access controls and audit records preserve both the decision history and patient privacy.

## Practice and exit gate

- [L1 · Small reproducible experiment](labs/L1.md)
- [L2 · Measured comparison](labs/L2.md)
- [L3 · Failure injection](labs/L3.md)
- [L4 · Independent exercise](labs/L4.md)
- [Regulated AI requirements simulator](projects/guided/README.md)
- [Auditable human-approved healthcare/energy copilot](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Score at least 80% on fresh cases, reproduce four labs, meet both project acceptance criteria, diagnose one unfamiliar failure, and repeat the assessment after a delay.

Continue with [A18 · Microsoft Foundry & Enterprise AI Platforms](../A18-microsoft-foundry-enterprise-ai/README.md) after the applicable gates.
