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

## Guided walkthrough

Start with one business decision in one process. Follow the same decision as it crosses application, data, and deployment boundaries.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Separate decisions, state, and interfaces (A07.01–A07.07)

1. **[A07.01 · separation of concerns](lessons/A07.01.md).** Request parsing, business decisions and persistence have different reasons to change. A pure decision accepts business inputs, while a handler translates request and response contracts. Four pricing cases and three protocol cases need seven focused checks before a small integration suite. Crossing every input with every protocol case would produce twelve combinations.
2. **[A07.02 · coupling/cohesion](lessons/A07.02.md).** Coupling is dependence between units. Cohesion is how closely the responsibilities inside a unit belong together. Dependencies can be about code, data, timing, or deployment. A unit directly referenced by eight callers has up to eight call sites affected by a breaking signature change. One stable adapter can concentrate the translation.
3. **[A07.03 · modules and packages](lessons/A07.03.md).** A module scopes names. A package organizes modules and controls the public interface by convention and documented exports. Python internal naming is not an access control boundary. Ten public exports with two contract cases each require twenty checks. A facade with three exports needs six under the same test model.
4. **[A07.04 · interfaces and contracts](lessons/A07.04.md).** Contracts specify input, result, errors and invariants, not just types. A structural interface helps substitute implementations. Behavior needs executable examples. Two adapters with three required behavior cases need six parameterized checks.
5. **[A07.05 · state boundaries](lessons/A07.05.md).** A state boundary has one owner for mutations and invariants. Other components may maintain derived views with explicit freshness or use an interface to request changes. With an origin committing 20 events/s and a view delayed by two seconds, up to about 40 changes may be unapplied under uniform traffic.
6. **[A07.06 · monolith vs services](lessons/A07.06.md).** A monolith can keep calls and transactions in process. Services add independent deployment and isolation along with network, consistency, and operational obligations. Three serialized 15 ms remote calls add about 45 ms before handler and queue time in a simple example.
7. **[A07.07 · layered architecture](lessons/A07.07.md).** Layers group responsibilities and constrain dependencies. Transport translates requests, application code coordinates use cases, domain code protects invariants and infrastructure handles storage or remote side effects. If six endpoints bypass one shared policy, a rule update can require six edits. Routing each through one rule changes one place.

### Move work across service and event boundaries (A07.08–A07.20)

8. **[A07.08 · hexagonal ports/adapters](lessons/A07.08.md).** A port expresses a boundary needed by the application. An adapter implements it for an external technology, and composition wires the chosen implementation. Two outbound adapters and four common contract scenarios require eight checks independent of domain test cases.
9. **[A07.09 · domain-driven design bounded contexts](lessons/A07.09.md).** A bounded context defines where a domain model and language are internally consistent. Translation across contexts is explicit and does not require a shared persistence schema. Three contexts can produce up to 3×2=6 directed pairwise translations. Document the actual edges instead of assuming all exist.
10. **[A07.10 · modular monolith](lessons/A07.10.md).** A modular monolith keeps one deployment while enforcing module interfaces, owned state and one-way dependencies. Module boundaries still need tests and review. Four modules with three independent interface checks each yield twelve targeted checks, versus treating the entire deployable as one contract.
11. **[A07.11 · microservices trade-offs](lessons/A07.11.md).** Microservices can enable independent releases and scaling. They add remote error semantics, separate lifecycles, data ownership, tracing and operational burden. Four serialized network transitions at 12 ms each contribute about 48 ms under a fixed-delay model.
12. **[A07.12 · API gateway vs service](lessons/A07.12.md).** A gateway handles shared edge policy such as routing and broad credential validation. The service owns resource-level authorization and business policy. At three services behind one gateway, credential verification policy can be centralized, while all three service-level access contracts still need coverage.
13. **[A07.13 · synchronous API vs queue vs stream](lessons/A07.13.md).** A synchronous API couples completion to the request. A queue accepts independent work with an acknowledgment contract. A stream retains ordered records by its partition policy for multiple reader positions. At 20 arrivals/s and 2 s mean residence, a stable stage contains about 40 requests on average. Enqueueing does not eliminate backlog.
14. **[A07.14 · event contracts](lessons/A07.14.md).** An event contract defines identity, type, schema revision, payload and time semantics. Separate event meaning from its envelope and plan for coexistence. Three writer versions and two consumers imply up to six compatibility combinations when their rollout windows overlap.
15. **[A07.15 · CQRS](lessons/A07.15.md).** CQRS separates command and query interfaces. It can use one or multiple stores. A separate projection introduces lag and rebuilding rules. If a projection applies 80 events/s while writes arrive at 100/s, backlog grows at 20/s under fixed rates.
16. **[A07.16 · event sourcing](lessons/A07.16.md).** Event sourcing stores facts as an append-only event history. Current state is folded from the sequence. Snapshots reduce replay work while preserving event interpretation requirements. A snapshot at event 9000 of 10000 reduces replay from 10000 to 1000 events, excluding snapshot loading.
17. **[A07.17 · transactional outbox](lessons/A07.17.md).** Write business state and an outbox record in one database transaction. Publish after commit. A crash after publishing and before recording success may repeat delivery, so use a durable consumer receipt. One event with one retry can produce two broker deliveries and one durable consumer effect with correctly scoped deduplication.
18. **[A07.18 · CDC](lessons/A07.18.md).** Change data capture reads a change feed, often from a transaction log. It needs source positions, startup snapshot policy, retention and restart handling. At 200 changes/s, 30 s of lag represents roughly 6000 changes in a uniform model.
19. **[A07.19 · saga compensation](lessons/A07.19.md).** A saga sequences durable local transitions with compensations. Compensation is a new business action, can itself fail, and may require retries or reconciliation. Three commands with one retried compensation can cause four deliveries while still producing one release effect.
20. **[A07.20 · Kafka event lifecycle](lessons/A07.20.md).** Kafka records are appended to partitions, fetched by consumers and tracked with offsets. Per-partition ordering and group assignments differ from global ordering. Commit positions must align with processing guarantees. With four partitions, at most four group members can actively consume distinct partitions in a conventional consumer group. Extra members can be idle.

### Evolve workflows and shared contracts (A07.21–A07.31)

21. **[A07.21 · workflow engines vs event choreography](lessons/A07.21.md).** An orchestrator records state and issues commands. In choreography, participants react to events and infer progress from local facts. Both need step identity and recovery semantics. Six participants with all-to-all directed subscriptions could create 30 relationships. An orchestrator with one command and one reply per participant has 12 such edges in the simplified topology.
22. **[A07.22 · DAG orchestration](lessons/A07.22.md).** A DAG describes dependency relations and has no directed cycles. A scheduler marks tasks ready only after dependencies meet the selected trigger conditions. For upstream stages of 10 ms then parallel branches of 20 and 30 ms, the critical path is 40 ms before the join's own processing.
23. **[A07.23 · job scheduler](lessons/A07.23.md).** Schedulers trigger runs under timing, catch-up and overlap policies. Persist a run identity such as job name and scheduled occurrence, and specify how runs recover. A five-minute cadence over an outage of 20 minutes can miss four intended ticks depending on endpoint convention.
24. **[A07.24 · SKIP LOCKED queues](lessons/A07.24.md).** FOR UPDATE locks eligible rows. PostgreSQL SKIP LOCKED can skip rows already locked by others, useful for competing queue consumers. It intentionally gives an inconsistent selection view. With batch limit 10 and three workers, up to 30 rows may be claimed in one round under disjoint locks.
25. **[A07.25 · rule engines](lessons/A07.25.md).** A rule engine separates rule definitions, evaluation inputs and outcomes. Define precedence, conflict handling, rule version and evidence for a decision. Twenty rules with three explicit edge cases per rule require sixty checks before testing interactions.
26. **[A07.26 · replay and poison messages](lessons/A07.26.md).** Bound attempts, retain failure evidence, and quarantine poison messages. Replaying a queue or stream is safe only with compatible consumers and controlled side effects. With a 3-attempt cap, 20 malformed messages use up to 60 attempts before quarantine rather than indefinite retries.
27. **[A07.27 · schema registry](lessons/A07.27.md).** A schema registry stores versions and checks configured compatibility for supported formats. The compatibility mode and transitive history coverage determine allowed evolution. With four old versions, latest-only comparison checks one predecessor. A transitive policy can check four in a simple example.
28. **[A07.28 · backward compatible events](lessons/A07.28.md).** Backward compatibility allows a new reader to consume older data. Forward compatibility allows older readers to consume newly written data under format-specific rules. Optional fields and defaults depend on the schema format. With two writer versions and two readers, a full rollout matrix contains four pairs. Required directions depend on deployment order.
29. **[A07.29 · change-safe database migrations](lessons/A07.29.md).** Expand first, then deploy compatible reads and writes, backfill, switch authority, and contract after the compatibility and rollback window. Schema lock behavior is engine-specific. Backfilling 4800 rows in batches of 400 takes twelve batches. A single batch holds its relevant locks longer under comparable execution.
30. **[A07.30 · tenancy boundaries](lessons/A07.30.md).** Tenant identity must derive from a trusted authenticated boundary. Qualify state and idempotency keys by tenant, and validate routing and observability data. Caller-provided metadata alone is insufficient. Two tenants with the same external ID occupy two scoped keys. A global key collapses both into one entry.
31. **[A07.31 · architecture decision records and decomposition cost](lessons/A07.31.md).** An ADR records the alternatives, context, choice, consequences and review triggers. Decomposition costs include data migration, coordination and operational ownership. For five components, an all-to-all directed model permits 20 integration edges. Actual decomposition cost depends on the observed edges.

### Put it together

For an order that must trigger fulfillment, commit the order and its outbox entry together. Assume the publisher can deliver the event twice if it crashes after publishing. The consumer needs a durable event identity and a stable side effect on replay. Test old and new readers during a schema rollout before removing the old field.

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
