# A18 · Microsoft Foundry & Enterprise AI Platforms

**26 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../A17-regulated-ai-compliance-governance/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [A18.01](lessons/A18.01.md) | cloud IAM/networking | Foundation |
| [A18.02](lessons/A18.02.md) | container app vs Kubernetes | Foundation |
| [A18.03](lessons/A18.03.md) | vector retrieval | Foundation |
| [A18.04](lessons/A18.04.md) | agent orchestration | Foundation |
| [A18.05](lessons/A18.05.md) | tenant identity | Foundation |
| [A18.06](lessons/A18.06.md) | pricing units | Foundation |
| [A18.07](lessons/A18.07.md) | Microsoft Foundry model catalog and deployments | Core |
| [A18.08](lessons/A18.08.md) | Azure OpenAI endpoints | Core |
| [A18.09](lessons/A18.09.md) | Foundry Agent Service | Core |
| [A18.10](lessons/A18.10.md) | Microsoft Agent Framework vs LangGraph | Core |
| [A18.11](lessons/A18.11.md) | Azure AI Search | Core |
| [A18.12](lessons/A18.12.md) | Container Apps vs AKS | Core |
| [A18.13](lessons/A18.13.md) | managed identities | Core |
| [A18.14](lessons/A18.14.md) | private endpoints | Core |
| [A18.15](lessons/A18.15.md) | network and secrets | Core |
| [A18.16](lessons/A18.16.md) | tenant-scoped indexes and retrieval | Core |
| [A18.17](lessons/A18.17.md) | managed evaluation and telemetry | Core |
| [A18.18](lessons/A18.18.md) | hosted vs self-hosted build-versus-buy | Principal |
| [A18.19](lessons/A18.19.md) | tenant data planes | Principal |
| [A18.20](lessons/A18.20.md) | isolation tests | Principal |
| [A18.21](lessons/A18.21.md) | key management and residency | Principal |
| [A18.22](lessons/A18.22.md) | cost allocation per tenant | Principal |
| [A18.23](lessons/A18.23.md) | quotas and fairness | Principal |
| [A18.24](lessons/A18.24.md) | managed vs custom lifecycle trade-offs | Principal |
| [A18.25](lessons/A18.25.md) | migration and portability | Principal |
| [A18.26](lessons/A18.26.md) | provider outages and fallback design | Principal |

## Guided walkthrough

Start with tenant, network, and quota boundaries. Use the linked provider lessons for the product names and project assumptions used by this curriculum.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Establish cloud and tenant requirements (A18.01–A18.06)

1. **[A18.01 · cloud IAM/networking](lessons/A18.01.md).** Separate network reachability from identity and authorization. Evaluate management plane and data plane independently. Both allowed network and assigned role are necessary. Reachable with missing role denies.
2. **[A18.02 · container app vs Kubernetes](lessons/A18.02.md).** Compare managed Container Apps and AKS by control-plane ownership, scaling, networking and platform capabilities. A required capability can eliminate a simpler option. Required fixture features are revisions and custom scheduling. App platform has one. Orchestrated platform has both.
3. **[A18.03 · vector retrieval](lessons/A18.03.md).** Filter permitted documents before ranking. Verify behavior for each source and identity flow. Measure judged recall on fixed cases. Tenant A has scores 0.4 and 0.5 while B has 0.9. Eligible maximum A is 0.5.
4. **[A18.04 · agent orchestration](lessons/A18.04.md).** Keep state and effect authorization explicit around tool calls. Evaluate platform runtime, versioning, observability and identity support per agent and deployment type. Four transitions include one approval edge. A route skipping it records zero valid approvals.
5. **[A18.05 · tenant identity](lessons/A18.05.md).** Resolve tenancy from verified identity and map it to a deployment-provisioned scope. Deny unknown tenants and mismatched audience. Authenticated tenant A and request tenant B are inconsistent.
6. **[A18.06 · pricing units](lessons/A18.06.md).** Account for separately billed units by resource, region and SKU. Use one currency and period. Published offers may have different commitment terms. Fixture meter: 2000 tokens at 0.03 units per 1000 gives 0.06 units.

### Assemble the provider components (A18.07–A18.17)

7. **[A18.07 · Microsoft Foundry model catalog and deployments](lessons/A18.07.md).** A deployment creates a serving target with its own model version and deployment configuration. Check availability, deployment type, capacity and resource scope in current documentation. Two catalog entries, one provisioned deployment, one routable target.
8. **[A18.08 · Azure OpenAI endpoints](lessons/A18.08.md).** Check endpoint pattern, API surface, authentication scope and deployment name for the service being called. Record version and compatibility in integration tests. Endpoint, audience and named deployment must match. One mismatch fails the fixture.
9. **[A18.09 · Foundry Agent Service](lessons/A18.09.md).** Choose agent type and runtime by tool support, state management, security and versioning. Check feature availability per deployment and service region. Chosen route needs hosting and policy integration. One candidate supplies only hosting and fails requirements.
10. **[A18.10 · Microsoft Agent Framework vs LangGraph](lessons/A18.10.md).** Compare Microsoft Agent Framework and LangGraph using state model, checkpoint recovery, human handoff and test seams. Start with a framework-neutral workflow contract. Two candidate fixtures support checkpointing, only one also supports a verified resume path.
11. **[A18.11 · Azure AI Search](lessons/A18.11.md).** Choose filters or supported permission-aware indexing based on the integration. Confirm enforced behavior for every source, permission update and query path. Three results have explicit ACLs and one grants the requesting identity. Exactly one is eligible.
12. **[A18.12 · Container Apps vs AKS](lessons/A18.12.md).** Compare Container Apps revisions and scale rules with AKS extensibility, Kubernetes API needs and control-plane operations. Evaluate rollout and workload identity together. One modeled support team can sustain 4 hours/week. Plans need 2 and 6. One fits.
13. **[A18.13 · managed identities](lessons/A18.13.md).** Assign a system- or user-assigned identity and grant an appropriate role at target scope. Identity lifecycle and access assignment are separate. Identity exists and token is valid, but missing data role blocks access.
14. **[A18.14 · private endpoints](lessons/A18.14.md).** Private endpoint and private DNS must produce the intended addressing for each network boundary. Restrict public network access when required and verify effective routes. Private endpoint exists but DNS resolves the public path. The private path check is false.
15. **[A18.15 · network and secrets](lessons/A18.15.md).** Use identity-scoped data permissions and network controls. Minimize secret use with managed identity and rotate the remaining credentials. Network, identity and secret-read grant comprise three gates. Two granted is insufficient.
16. **[A18.16 · tenant-scoped indexes and retrieval](lessons/A18.16.md).** Choose shared index, index per tenant or service per tenant after assessing isolation, cost and limits. Enforce identity-to-scope all the way to the candidate set. Tenant allowlist maps A to idx-a. Request for idx-b must fail.
17. **[A18.17 · managed evaluation and telemetry](lessons/A18.17.md).** Record release identity, route, case provenance, trace and evaluation version. Separate score validity from telemetry delivery health. Three expected cases and two observed results give coverage 2/3.

### Test isolation, cost, and portability (A18.18–A18.26)

18. **[A18.18 · hosted vs self-hosted build-versus-buy](lessons/A18.18.md).** Include platform lifecycle, operational staffing, compliance, feature gaps and switching costs at the same quality and traffic targets. Managed fixture totals 6+4=10 units, self-hosted totals 5+7=12.
19. **[A18.19 · tenant data planes](lessons/A18.19.md).** Choose isolation model by blast radius, data controls and resource ceilings. Use deployment stamps where failures or workload need separation. Eight tenants over four equal stamps create a two-tenant blast radius per stamp.
20. **[A18.20 · isolation tests](lessons/A18.20.md).** Use matched fixtures from multiple tenants, rotate scopes and assert foreign content and writes are absent. Cover index, cache and tool boundaries. Allowed=2, denied=2, leakage=0 is a strong fixture. Counting only successes misses denial coverage.
21. **[A18.21 · key management and residency](lessons/A18.21.md).** Map permissions, key rotation and data flows for model, index, telemetry and backup services. Verify functionality and contractual residency for chosen offerings. A configured two-region policy covers retail and backup fixtures but a third telemetry location is outside scope.
22. **[A18.22 · cost allocation per tenant](lessons/A18.22.md).** Choose metered allocations with a stated residual shared-cost rule. Compare cost attribution coverage to the total billed period. Tenant usage 1:3 allocates a 40-unit variable pool as 10 and 30.
23. **[A18.23 · quotas and fairness](lessons/A18.23.md).** Constrain tenant and shared capacity independently and admit within both budgets. Define backpressure, fairness and fallback on capacity errors. Tenant cap 3 and global available 2. Request cost 3 fails.
24. **[A18.24 · managed vs custom lifecycle trade-offs](lessons/A18.24.md).** Track status, deployed model versions, supported interfaces and recovery controls. Build project entry points against current docs and isolate preview behavior. Two lifecycle assumptions confirmed, one assumed only, gives one open migration risk.
25. **[A18.25 · migration and portability](lessons/A18.25.md).** Keep transport and vendor-specific configuration behind an adapter. Preserve normalized release, tenant and evaluation evidence, then run contract tests at migration. Both candidate adapters return status and usage. One loses source version and fails the required fields test.
26. **[A18.26 · provider outages and fallback design](lessons/A18.26.md).** Use a ranked allowlist constrained by region, tenancy and policy. Degrade safely when no eligible route is healthy. Primary unavailable and fallback healthy but forbidden produces zero eligible routes.

### Put it together

Model an outage with a healthy fallback in a destination prohibited by tenant policy. The request remains blocked from that route even if it would improve availability. Test the approved failure behavior and verify that the routing record explains the policy decision.

## Practice and exit gate

- [L1 · Small reproducible experiment](labs/L1.md)
- [L2 · Measured comparison](labs/L2.md)
- [L3 · Failure injection](labs/L3.md)
- [L4 · Independent exercise](labs/L4.md)
- [Multi-tenant Foundry architecture mock](projects/guided/README.md)
- [Enterprise AI SaaS with identity and cost attribution](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Score at least 80% on fresh cases, reproduce four labs, meet both project acceptance criteria, diagnose one unfamiliar failure, and repeat the assessment after a delay.

[Compare AWS, Azure and Google Cloud implementation boundaries](CLOUD_BOUNDARIES.md) for the architecture phases in this batch.

Continue with [A19 · Voice, Multimodal, Edge & Embedded AI](../A19-voice-multimodal-edge-embedded-ai/README.md) after the applicable gates.
