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

## Guided walkthrough

Define a good user outcome, convert that definition into an operational signal, and test recovery under a controlled fault.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Define and observe reliable outcomes (A08.01–A08.06)

1. **[A08.01 · availability vs durability](lessons/A08.01.md).** Availability is a service-usability property at a defined boundary. Durability is a persistence property under a specified set of faults. You can lose one while preserving the other. If 999 of 1000 requests succeed, measured request availability is 99.9%. That ratio does not describe the probability of losing a stored record.
2. **[A08.02 · SLIs/SLOs/SLAs](lessons/A08.02.md).** An SLI is a quantitative indicator. An SLO sets a target and window for it. An SLA defines an agreement and consequences, often with its own scope and exclusions. At 99.9% with 100000 eligible requests, 100 can miss the target before exhausting the simple request budget.
3. **[A08.03 · reliability budget](lessons/A08.03.md).** A reliability budget allocates tolerable user harm. Multiplying independent availability estimates can approximate mandatory serial dependencies, while correlated failures require a different model. Two mandatory independent components each at 99.9% yield 0.999²≈99.8001% for the path under this model.
4. **[A08.04 · success and failure definition](lessons/A08.04.md).** Success uses product and contract semantics, timing and completeness. An acceptable rejection can be measured separately from an error, with a defined eligible denominator. If 100 eligible responses include four invalid bodies and two different late responses, there are 94 good responses under a combined rule.
5. **[A08.05 · metrics/logs/traces](lessons/A08.05.md).** Metrics aggregate numerical observations, logs record events, and traces connect causal spans for selected operations. A shared measurement boundary supports correlation. 1000 requests with two logs create 2000 records. A 1% uniform trace sample expects ten traces, and cannot replace complete denominator metrics.
6. **[A08.06 · structured correlation IDs](lessons/A08.06.md).** Generate or validate correlation values and propagate them according to interoperability policy. Logs should use allowlisted fields and avoid secrets or high-cardinality metric labels. At 500 requests/s, recording one 48-byte identifier per request adds 24000 bytes/s before encoding and transport overhead.

### Contain failures and prepare recovery (A08.07–A08.19)

7. **[A08.07 · timeout hierarchy](lessons/A08.07.md).** Set a total deadline, then allocate per-hop phase limits and propagate remaining time. Connect, idle read and overall timers measure different events. With budget 300 ms and 60 ms already elapsed, reserving 30 ms for response handling leaves 210 ms for downstream work.
8. **[A08.08 · retry/backoff/jitter](lessons/A08.08.md).** Retries consume backend work, exponential backoff increases waits, and jitter spreads them. Limit retries by attempts, total deadline and safe operation semantics. Three independent layers each allowing three total attempts can produce 27 backend attempts per original request under worst-case nesting.
9. **[A08.09 · circuit breaker](lessons/A08.09.md).** A circuit breaker transitions from closed to open under measured failure, rejects early while open, and allows bounded half-open probes before recovery. If 60 calls/s arrive during a five-second open period, as many as 300 ordinary calls can be rejected early rather than hitting origin. Probes are a separate budget.
10. **[A08.10 · bulkhead](lessons/A08.10.md).** A bulkhead partitions capacity by workload or dependency, limiting failure propagation. Fixed partitions can reduce utilization when one side is idle. A pool with 10 slots split 7/3 leaves three slots for class B while class A saturates its seven.
11. **[A08.11 · fallback](lessons/A08.11.md).** A fallback changes the service contract under failure. It can return a degraded result, stale cache, queued response or clear error according to product constraints. If the last refresh was 120 s ago and the accepted staleness limit is 60 s, serving the cached value violates that limit by 60 s.
12. **[A08.12 · backpressure and admission control](lessons/A08.12.md).** Backpressure communicates capacity upstream. Admission control rejects or delays at a boundary. A bounded queue limits waiters but does not itself bound service duration. If capacity admits 80 of 100 simultaneous jobs and no slots free during arrival, 20 must be delayed upstream or rejected.
13. **[A08.13 · health checks](lessons/A08.13.md).** Liveness estimates whether restart can help. Readiness gates traffic. Startup probes accommodate initialization. Inappropriate dependency coupling can turn a shared outage into restart churn. Three failing probes at 5 s intervals detect a fault roughly 10–15 s after failure under instantaneous checks and fixed scheduling.
14. **[A08.14 · graceful shutdown](lessons/A08.14.md).** Graceful shutdown stops admission, drains or cancels work, then releases resources. A grace deadline bounds the whole sequence. A 30 s grace period with 5 s reserved cleanup and 2 s endpoint-removal delay leaves up to 23 s for draining in the model.
15. **[A08.15 · error budgets](lessons/A08.15.md).** An error budget is the tolerable bad share under the SLO. Burn rate divides observed bad fraction by the allowed one under matching units. At a 99.9% objective, a 1% bad rate burns at 10×. If sustained at stable traffic, it consumes a 30-day budget in three days.
16. **[A08.16 · alerts and runbooks](lessons/A08.16.md).** Actionable alerts focus on user impact or imminent risk. A runbook lists evidence to collect, reversible mitigation, ownership and verification. A 5% budget slice over one hour on a 30-day time-proportional model implies 36× burn, since 0.05×720=36.
17. **[A08.17 · on-call triage](lessons/A08.17.md).** Triage establishes user impact, severity, scope and first reversible mitigation. Assign coordination, communication and operational roles according to incident size. If a failing route receives 200 RPS for 90 seconds, there are up to 18000 affected requests before accounting for successful retries and traffic shifts.
18. **[A08.18 · backups, restore and disaster recovery](lessons/A08.18.md).** A backup is useful when independent restoration is compatible, complete and verified. Use a database-aware snapshot or export, preserve required log chains, and test invariants after restore. Restoring 240 GiB at 120 MiB/s takes about 2048 seconds before verification and warm-up.
19. **[A08.19 · RPO and RTO](lessons/A08.19.md).** RPO bounds acceptable data loss expressed in time. RTO bounds recovery duration. Report observed values against their objectives, including verification and routing time. If records are recoverable through 12:40 and incident begins at 12:45, the observed recovery gap is five minutes. A 12:59 recovery takes 14 minutes from the incident boundary.

### Test failure domains and release strategies (A08.20–A08.30)

20. **[A08.20 · fault injection and chaos tests](lessons/A08.20.md).** A chaos test declares a hypothesis, observable outcome, target scope, stop condition, and cleanup. Controlled one-variable faults help attribute cause. If the safety cap is 5 of 100 instances, a selected batch of 12 exceeds scope by seven.
21. **[A08.21 · cascading failures](lessons/A08.21.md).** Cascades amplify failure through queues, retries, shared pools and load redistribution. Saturated workers reject or time out, producing additional attempts. At 100 original requests/s and one retry for every failure, offered downstream work can reach 200 attempts/s in the simple model.
22. **[A08.22 · retry storms](lessons/A08.22.md).** A retry storm is amplified offered load from repeated attempts. Synchronized timers and retries at multiple layers can amplify pressure despite static user traffic. With 1000 clients retrying once at the same instant, a 1 s window may get 1000 requests. Uniform jitter over 10 s yields about 100 per 1 s bucket in expectation.
23. **[A08.23 · failure domains](lessons/A08.23.md).** A failure domain groups resources affected by a shared fault. Dependencies can share a host, zone, credential, control plane or operational procedure. If three replicas share a single room and it fails, zero remain. With a 2+1 placement across rooms, loss of the two-replica room leaves one.
24. **[A08.24 · single point of failure](lessons/A08.24.md).** A single point of failure is a component whose loss breaks the required service behavior without a suitable alternate. Redundancy must be operationally independent and tested. With two service replicas and one required unreplicated broker, losing the broker leaves zero complete service paths.
25. **[A08.25 · multi-region active-passive vs active-active](lessons/A08.25.md).** Active-passive usually has one active writer with failover. Active-active may handle requests in several regions and requires explicit state and conflict rules for operations that write. If failover detection takes 40 s, routing change 30 s and verification 20 s, the serial component of recovery is 90 s.
26. **[A08.26 · distributed tracing and sampling](lessons/A08.26.md).** Head sampling selects traces early from available context. Tail sampling uses later evidence and needs buffering and reliable span collection. Sampled traces complement full counters. At 10000 requests and uniform 1% sampling, about 100 traces are expected. If ten requests are slow, expected captured slow traces are only 0.1.
27. **[A08.27 · data migration safety](lessons/A08.27.md).** Data migrations need compatibility across old and new code, backups, staged backfill and data validation. An irreversible transformation may require a forward repair. A backfill of 60000 rows at 2000 rows/min takes at least 30 minutes before retries and verification.
28. **[A08.28 · canary, blue-green and shadow traffic](lessons/A08.28.md).** Canary serves a subset of traffic, blue-green switches between environments, and shadow copies requests without granting authority over user responses. Shadows must isolate side effects. A 5% canary at 2000 RPS receives about 100 RPS with even distribution. The small cohort can need more time to see rare errors.
29. **[A08.29 · cost/reliability trade-offs](lessons/A08.29.md).** Compare marginal cost with a measurable reliability or recovery improvement. Include idle capacity, failover traffic, operational work and cost per successful operation. At 10000 cost units per month and 2 million successful requests, spend is 0.005 units per success. At the same spend and 1 million it is 0.01.
30. **[A08.30 · abuse detection](lessons/A08.30.md).** Abuse detection combines bounded signals such as rate, cost, identity and anomalous behavior. Protect privacy, evaluate false positives, and apply scoped limits and review. If 10 of 1000 legitimate requests are incorrectly blocked, the measured false-positive rate on that legitimate set is 1%.

### Put it together

At a 99.9% successful-request SLO over 100,000 eligible requests, the simple error budget is 100 failures. A canary that consumes 30 failures in a short interval can warrant intervention before the window closes. Trace the failure to the release or dependency, stop additional impact, then use a recovery probe to confirm service behavior.

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
