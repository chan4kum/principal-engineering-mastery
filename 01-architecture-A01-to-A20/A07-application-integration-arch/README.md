# A07 · Application & Integration Architecture

**31 lessons · 4 labs · 2 projects**

Build integration boundaries that remain understandable under retries, mixed-version deployment, and failure after a business commit. Lesson IDs and tiers match both curriculum indexes. Fixtures isolate mechanisms, while the labs exercise Redis delivery and durable local workflows.

Prerequisite [A06 exit gate](../A06-distributed-systems-coordination/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A07.01](lessons/A07.01.md) | separation of concerns | Foundation |
| [A07.02](lessons/A07.02.md) | coupling/cohesion | Foundation |
| [A07.03](lessons/A07.03.md) | modules and packages | Foundation |
| [A07.04](lessons/A07.04.md) | interfaces and contracts | Foundation |
| [A07.05](lessons/A07.05.md) | state boundaries | Foundation |
| [A07.06](lessons/A07.06.md) | monolith vs services | Foundation |
| [A07.07](lessons/A07.07.md) | layered architecture | Foundation |
| [A07.08](lessons/A07.08.md) | hexagonal ports/adapters | Core |
| [A07.09](lessons/A07.09.md) | domain-driven design bounded contexts | Core |
| [A07.10](lessons/A07.10.md) | modular monolith | Core |
| [A07.11](lessons/A07.11.md) | microservices trade-offs | Core |
| [A07.12](lessons/A07.12.md) | API gateway vs service | Core |
| [A07.13](lessons/A07.13.md) | synchronous API vs queue vs stream | Core |
| [A07.14](lessons/A07.14.md) | event contracts | Core |
| [A07.15](lessons/A07.15.md) | CQRS | Core |
| [A07.16](lessons/A07.16.md) | event sourcing | Core |
| [A07.17](lessons/A07.17.md) | transactional outbox | Core |
| [A07.18](lessons/A07.18.md) | CDC | Core |
| [A07.19](lessons/A07.19.md) | saga compensation | Core |
| [A07.20](lessons/A07.20.md) | Kafka event lifecycle | Core |
| [A07.21](lessons/A07.21.md) | workflow engines vs event choreography | Principal |
| [A07.22](lessons/A07.22.md) | DAG orchestration | Principal |
| [A07.23](lessons/A07.23.md) | job scheduler | Principal |
| [A07.24](lessons/A07.24.md) | SKIP LOCKED queues | Principal |
| [A07.25](lessons/A07.25.md) | rule engines | Principal |
| [A07.26](lessons/A07.26.md) | replay and poison messages | Principal |
| [A07.27](lessons/A07.27.md) | schema registry | Principal |
| [A07.28](lessons/A07.28.md) | backward compatible events | Principal |
| [A07.29](lessons/A07.29.md) | change-safe database migrations | Principal |
| [A07.30](lessons/A07.30.md) | tenancy boundaries | Principal |
| [A07.31](lessons/A07.31.md) | architecture decision records and decomposition cost | Principal |

## Practice and exit gate

- [L1 · Synchronous vs async](labs/L1.md)
- [L2 · Messaging semantics](labs/L2.md)
- [L3 · Saga](labs/L3.md)
- [L4 · Contracts](labs/L4.md)
- [Guided · Queue-backed order workflow](projects/guided/README.md)
- [Independent · Saga and transactional-outbox business pipeline](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Defend an integration boundary and its failure recovery with a sequence diagram, including both publication replay and consumer deduplication.

Continue to [A08 · Reliability, Operations & SRE](../A08-reliability-operations-and-sre/README.md) when the prerequisite stage gates are met.
