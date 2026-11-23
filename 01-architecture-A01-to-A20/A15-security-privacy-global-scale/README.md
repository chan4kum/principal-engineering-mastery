# A15 · Security, Privacy & Global-Scale Architecture

**29 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../A14-advanced-llmops-evals-safety/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [A15.01](lessons/A15.01.md) | security objectives confidentiality/integrity/availability | Foundation |
| [A15.02](lessons/A15.02.md) | identity vs permission | Foundation |
| [A15.03](lessons/A15.03.md) | threat modeling | Foundation |
| [A15.04](lessons/A15.04.md) | encryption at rest/in transit | Foundation |
| [A15.05](lessons/A15.05.md) | secrets and trust boundaries | Foundation |
| [A15.06](lessons/A15.06.md) | OAuth/OIDC and JWT validation | Core |
| [A15.07](lessons/A15.07.md) | RBAC/ABAC/ReBAC | Core |
| [A15.08](lessons/A15.08.md) | row-level security | Core |
| [A15.09](lessons/A15.09.md) | tenant ID propagation | Core |
| [A15.10](lessons/A15.10.md) | document permissions | Core |
| [A15.11](lessons/A15.11.md) | encryption/KMS | Core |
| [A15.12](lessons/A15.12.md) | auditing | Core |
| [A15.13](lessons/A15.13.md) | retention and deletion | Core |
| [A15.14](lessons/A15.14.md) | policy-as-code | Core |
| [A15.15](lessons/A15.15.md) | PII handling | Core |
| [A15.16](lessons/A15.16.md) | network isolation | Core |
| [A15.17](lessons/A15.17.md) | rate limits and abuse protections | Core |
| [A15.18](lessons/A15.18.md) | OWASP application and AI threats | Core |
| [A15.19](lessons/A15.19.md) | data-residency requirements | Principal |
| [A15.20](lessons/A15.20.md) | lawful processing and privacy assessments | Principal |
| [A15.21](lessons/A15.21.md) | disaster recovery regions | Principal |
| [A15.22](lessons/A15.22.md) | key rotation | Principal |
| [A15.23](lessons/A15.23.md) | prompt injection and tool exfiltration | Principal |
| [A15.24](lessons/A15.24.md) | retrieval data poison | Principal |
| [A15.25](lessons/A15.25.md) | supply chain | Principal |
| [A15.26](lessons/A15.26.md) | agent capabilities | Principal |
| [A15.27](lessons/A15.27.md) | SOC2/ISO27001 controls as applicable | Principal |
| [A15.28](lessons/A15.28.md) | cross-region replication | Principal |
| [A15.29](lessons/A15.29.md) | zero-trust architecture and secure migrations | Principal |

## Guided walkthrough

Follow a request through identity, resource authorization, data handling, and regional operations. Make the enforcement point and its evidence explicit.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Identify assets, objectives, and trust boundaries (A15.01–A15.05)

1. **[A15.01 · security objectives confidentiality/integrity/availability](lessons/A15.01.md).** Confidentiality limits disclosure, integrity protects against unauthorized change, and availability measures usable service. Assess each separately. 99/100 requests complete, yet one delivers another tenant's record. Completion rate is 99% and the confidentiality control fails.
2. **[A15.02 · identity vs permission](lessons/A15.02.md).** Authentication establishes a principal. Authorization evaluates action, resource, context and relationships using trusted identity. Deny when no applicable rule grants access. An authenticated reader can list objects but cannot delete them.
3. **[A15.03 · threat modeling](lessons/A15.03.md).** Map assets, actors, data flows and boundaries. For each flow, relate applicable STRIDE categories to evidence and owners. Revisit when paths or privileges change. Three of four boundary crossings have control owners. Coverage is 75%.
4. **[A15.04 · encryption at rest/in transit](lessons/A15.04.md).** Use TLS with verified peers for transport and managed encryption on storage. Decrypted authorized reads, logs, backups and intermediaries require separate controls. Three hops require verified TLS. The middle hop has no peer verification, so the path fails the transport invariant.
5. **[A15.05 · secrets and trust boundaries](lessons/A15.05.md).** Constrain retrieval to the workload identity, keep secret material out of inputs and logs, scope it to the target operation, and rotate versions with bounded overlap. Only version 3 remains accepted after rotation. Version 2 must fail.

### Enforce and verify access and data controls (A15.06–A15.18)

6. **[A15.06 · OAuth/OIDC and JWT validation](lessons/A15.06.md).** Validate the allowed algorithm, issuer, audience and time bounds with keys from trusted issuer metadata. OIDC authenticates a user. Resource APIs enforce authorization on appropriate access tokens. Audience is billing and the endpoint requires catalog. The authorization decision is false despite a valid modeled signature.
7. **[A15.07 · RBAC/ABAC/ReBAC](lessons/A15.07.md).** RBAC grants role permissions, ABAC evaluates attributes and ReBAC evaluates relationships. A decision can compose them with precedence and auditability. A reader with a verified same-team relationship passes. Another-team reader fails despite sharing the role.
8. **[A15.08 · row-level security](lessons/A15.08.md).** PostgreSQL RLS can restrict visible rows and proposed writes. Test with a regular application role. Superusers, BYPASSRLS roles and normally table owners are exceptions. Two same-tenant rows among five produce two results under policy.
9. **[A15.09 · tenant ID propagation](lessons/A15.09.md).** Derive tenant from authenticated context, preserve it through async boundaries, and scope database keys, cache keys and logs as appropriate. Reject conflicting asserted scope. Requests A and B share ID 7 yet occupy two keyed values when tenant is included.
10. **[A15.10 · document permissions](lessons/A15.10.md).** Use current caller permissions to scope eligible documents before ranking and reauthorize after a scope change. Include scope in cached results. Tenant A owns score 3. Tenant B owns score 9. A's eligible maximum is 3.
11. **[A15.11 · encryption/KMS](lessons/A15.11.md).** Envelope encryption uses a data encryption key for data and a managed key to wrap it. Track version and integrity context and restrict decrypt operations. Two independent data keys wrapped by one key give two data-key identities. Direct reuse gives one.
12. **[A15.12 · auditing](lessons/A15.12.md).** Capture principal, action, resource, decision, timestamp and correlation ID with appropriate redaction. Protect integrity and restrict access to logs. Three records with decisions allow, deny, deny yield two denied events regardless of HTTP class.
13. **[A15.13 · retention and deletion](lessons/A15.13.md).** Model retention and deletion across derived indexes, caches, replicas and backup restore. Legal grounds or holds may constrain deletion. Reconcile on restore. One deletion must reach source, index and cache. With two receipts, one remains unresolved.
14. **[A15.14 · policy-as-code](lessons/A15.14.md).** Version policy as data, unit-test permit and deny cases, validate bundle provenance and record the policy version per decision. One release has both allow and deny evidence. Accept-only tests cover one of two required outcomes.
15. **[A15.15 · PII handling](lessons/A15.15.md).** Pseudonymised records can remain personal data when attribution is possible using additional information. Limit access and evaluate linkability and attribute inference. Three records with token T1 permit linkage across three entries even after direct names are removed.
16. **[A15.16 · network isolation](lessons/A15.16.md).** Segment ingress and egress by workload identity and service need. Keep application authorization and observe denied paths in isolated fixtures. Only application-to-database is allowed. Worker-to-database is denied.
17. **[A15.17 · rate limits and abuse protections](lessons/A15.17.md).** Apply scoped rate and concurrency limits with explicit cost units, bounded queues and fair allocation. A distributed limiter must define behavior during store failure. A capacity-5 bucket has 2 tokens left. A cost-3 request is denied.
18. **[A15.18 · OWASP application and AI threats](lessons/A15.18.md).** Identify affected assets and invariants. Access-control and prompt-mediated failures require authority and effect checks after input parsing. Use synthetic records to verify protections. A syntactically valid request lacks the required capability and is denied.

### Maintain controls across regions and migrations (A15.19–A15.29)

19. **[A15.19 · data-residency requirements](lessons/A15.19.md).** Inventory where data is processed, stored, replicated and accessible. Map legal or contractual requirements to actual data flows, processors and transfer mechanisms. Primary EU and backup EU with telemetry elsewhere yields two of three locations in the required fixture set.
20. **[A15.20 · lawful processing and privacy assessments](lessons/A15.20.md).** Assign and document a lawful basis per purpose. Special-category data can require an additional condition. Assess necessity, proportionality and whether a DPIA is required. Model two stated purposes and an approval for one. The other is unresolved.
21. **[A15.21 · disaster recovery regions](lessons/A15.21.md).** Define recovery time and recovery point objectives independently. Qualify target dependencies and enforce fencing before allowing writes. A replicated snapshot is 5 minutes old, restoration takes 18, and targets are 10 and 15. RPO passes and RTO fails.
22. **[A15.22 · key rotation](lessons/A15.22.md).** Track key version, phase out old write privileges, retain necessary read rights and verify migration before destruction according to policy. Reads initially need versions 1 and 2. Writes use 2. Destroying 1 leaves one missing read version.
23. **[A15.23 · prompt injection and tool exfiltration](lessons/A15.23.md).** Keep tool output untrusted, validate provenance, and authorize every proposed effect against the caller and destination outside the model. Use a mock data sink for evaluation. A mock requested write has no grant and must produce zero effects even if its text suggests otherwise.
24. **[A15.24 · retrieval data poison](lessons/A15.24.md).** Gate publication on provenance and review, enforce access, version indexes and rehearse revocation on synthetic fixtures. Among candidate scores 8,6,4, the unreviewed 8 is excluded. Highest eligible is 6.
25. **[A15.25 · supply chain](lessons/A15.25.md).** Resolve an immutable digest and verify provenance against an expected builder and source. SBOM inventories components. Vulnerability triage and artifact policy provide separate evidence. Trusted provenance must match signature, builder and revision. Two matches and one mismatch deny release.
26. **[A15.26 · agent capabilities](lessons/A15.26.md).** Issue narrow, short-lived capabilities for resource and action. Re-check authoritative context at the effect boundary and log denials. Capability permits read on resource 7. Write on the same resource has no grant.
27. **[A15.27 · SOC2/ISO27001 controls as applicable](lessons/A15.27.md).** Map actual scope, requirement, control owner and operating evidence. ISO/IEC 27001 specifies an information security management system. SOC 2 is an examination against applicable criteria. Three controls have named owners, but one of three has current evidence. Evidence coverage is one third.
28. **[A15.28 · cross-region replication](lessons/A15.28.md).** Measure replica freshness and decide which operations tolerate it. Use version, tombstone and reconciliation semantics at failover. Primary offset 120 and replica 114 imply six entries of lag. A read requiring offset 118 must fail or route elsewhere.
29. **[A15.29 · zero-trust architecture and secure migrations](lessons/A15.29.md).** Apply explicit per-request access, least privilege and bounded dual operation. Validate identities for old and new data paths and remove temporary permissions after verification. Three temporary grants are issued and only two are revoked, so one remains.

### Put it together

Test a document search with two tenants and a query that would rank the other tenant’s document first. Enforce eligibility before the document can enter the results or model context. Compare response and audit evidence to verify the decision without exposing document contents in telemetry.

## Practice and exit gate

- [L1 · Threat model](labs/L1.md)
- [L2 · Secrets lifecycle](labs/L2.md)
- [L3 · Software supply chain](labs/L3.md)
- [L4 · Access isolation](labs/L4.md)
- [Threat model and local policy checks](projects/guided/README.md)
- [DevSecOps secured multi-tenant AI service](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Score at least 80% on fresh cases, reproduce four labs, meet both project acceptance criteria, diagnose one unfamiliar failure, and repeat the assessment after a delay.

Continue with [A16 · System Design & Product-Company Interviews](../A16-system-design-and-interviews/README.md) after the applicable gates.
