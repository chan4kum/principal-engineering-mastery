# A08 · Reliability, Operations & SRE

**30 lessons · 4 labs · 2 projects**

Define user-facing reliability, observe dependencies, rehearse recovery and verify incident mitigations. Lesson IDs and tiers match both curriculum indexes. The labs collect real OpenTelemetry signals and use isolated fault fixtures.

Install the optional SDK with `uv sync --locked --extra api --extra telemetry` before the telemetry lab.

Prerequisite [A07 exit gate](../A07-application-integration-arch/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A08.01](lessons/A08.01.md) | availability vs durability | Foundation |
| [A08.02](lessons/A08.02.md) | SLIs/SLOs/SLAs | Foundation |
| [A08.03](lessons/A08.03.md) | reliability budget | Foundation |
| [A08.04](lessons/A08.04.md) | success and failure definition | Foundation |
| [A08.05](lessons/A08.05.md) | metrics/logs/traces | Foundation |
| [A08.06](lessons/A08.06.md) | structured correlation IDs | Foundation |
| [A08.07](lessons/A08.07.md) | timeout hierarchy | Core |
| [A08.08](lessons/A08.08.md) | retry/backoff/jitter | Core |
| [A08.09](lessons/A08.09.md) | circuit breaker | Core |
| [A08.10](lessons/A08.10.md) | bulkhead | Core |
| [A08.11](lessons/A08.11.md) | fallback | Core |
| [A08.12](lessons/A08.12.md) | backpressure and admission control | Core |
| [A08.13](lessons/A08.13.md) | health checks | Core |
| [A08.14](lessons/A08.14.md) | graceful shutdown | Core |
| [A08.15](lessons/A08.15.md) | error budgets | Core |
| [A08.16](lessons/A08.16.md) | alerts and runbooks | Core |
| [A08.17](lessons/A08.17.md) | on-call triage | Core |
| [A08.18](lessons/A08.18.md) | backups, restore and disaster recovery | Core |
| [A08.19](lessons/A08.19.md) | RPO and RTO | Core |
| [A08.20](lessons/A08.20.md) | fault injection and chaos tests | Principal |
| [A08.21](lessons/A08.21.md) | cascading failures | Principal |
| [A08.22](lessons/A08.22.md) | retry storms | Principal |
| [A08.23](lessons/A08.23.md) | failure domains | Principal |
| [A08.24](lessons/A08.24.md) | single point of failure | Principal |
| [A08.25](lessons/A08.25.md) | multi-region active-passive vs active-active | Principal |
| [A08.26](lessons/A08.26.md) | distributed tracing and sampling | Principal |
| [A08.27](lessons/A08.27.md) | data migration safety | Principal |
| [A08.28](lessons/A08.28.md) | canary, blue-green and shadow traffic | Principal |
| [A08.29](lessons/A08.29.md) | cost/reliability trade-offs | Principal |
| [A08.30](lessons/A08.30.md) | abuse detection | Principal |

## Practice and exit gate

- [L1 · Service telemetry](labs/L1.md)
- [L2 · SLO exercise](labs/L2.md)
- [L3 · Recovery drill](labs/L3.md)
- [L4 · Incident game day](labs/L4.md)
- [Guided · OpenTelemetry service dashboard](projects/guided/README.md)
- [Independent · Incident game-day and recovery automation](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Construct an error budget, incident timeline and mitigation choice using measured evidence.

Continue to [A09 · Cloud, Containers, Kubernetes & Platform Engineering](../A09-cloud-containers-k8s-devsecops/README.md) when the prerequisite stage gates are met.
