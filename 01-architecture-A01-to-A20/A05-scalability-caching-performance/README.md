# A05 · Scalability, Caching & Performance

**34 lessons · 4 labs · 2 projects**

Estimate capacity, protect downstream dependencies, and measure cache, queue and latency outcomes. Lesson IDs and tiers match both curriculum indexes. Small fixtures isolate mechanisms; the labs combine controlled load and measured outcomes.

Prerequisite [A04 exit gate](../A04-databases-sql-and-storage-engines/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A05.01](lessons/A05.01.md) | time vs throughput | Foundation |
| [A05.02](lessons/A05.02.md) | QPS/RPS/TPS | Foundation |
| [A05.03](lessons/A05.03.md) | mean vs percentiles | Foundation |
| [A05.04](lessons/A05.04.md) | p95/p99 and tail latency | Foundation |
| [A05.05](lessons/A05.05.md) | Little law and assumptions | Foundation |
| [A05.06](lessons/A05.06.md) | utilization and queue build-up | Foundation |
| [A05.07](lessons/A05.07.md) | CPU vs I/O bottlenecks | Foundation |
| [A05.08](lessons/A05.08.md) | back-of-envelope resource units | Foundation |
| [A05.09](lessons/A05.09.md) | horizontal vs vertical scaling | Core |
| [A05.10](lessons/A05.10.md) | load balancers and health checks | Core |
| [A05.11](lessons/A05.11.md) | Redis caching | Core |
| [A05.12](lessons/A05.12.md) | cache-aside/read-through/write-through | Core |
| [A05.13](lessons/A05.13.md) | TTL and eviction | Core |
| [A05.14](lessons/A05.14.md) | LRU/LFU | Core |
| [A05.15](lessons/A05.15.md) | cache invalidation | Core |
| [A05.16](lessons/A05.16.md) | cache stampedes and hot keys | Core |
| [A05.17](lessons/A05.17.md) | connection pools | Core |
| [A05.18](lessons/A05.18.md) | bulkheads | Core |
| [A05.19](lessons/A05.19.md) | batching | Core |
| [A05.20](lessons/A05.20.md) | worker queues | Core |
| [A05.21](lessons/A05.21.md) | rate limiter windows, token bucket/leaky bucket | Core |
| [A05.22](lessons/A05.22.md) | load shedding | Core |
| [A05.23](lessons/A05.23.md) | single-flight request coalescing | Principal |
| [A05.24](lessons/A05.24.md) | split hot keys | Principal |
| [A05.25](lessons/A05.25.md) | consistency under invalidation | Principal |
| [A05.26](lessons/A05.26.md) | sharding and resharding | Principal |
| [A05.27](lessons/A05.27.md) | consistent/rendezvous hashing | Principal |
| [A05.28](lessons/A05.28.md) | probabilistic cache admission | Principal |
| [A05.29](lessons/A05.29.md) | queueing model and contention | Principal |
| [A05.30](lessons/A05.30.md) | cost-aware scaling | Principal |
| [A05.31](lessons/A05.31.md) | latency budgeting | Principal |
| [A05.32](lessons/A05.32.md) | experiments, benchmarks and capacity envelopes | Principal |
| [A05.33](lessons/A05.33.md) | failure headroom | Principal |
| [A05.34](lessons/A05.34.md) | autoscaling interactions | Principal |

## Practice and exit gate

- [L1 · Cache benchmark](labs/L1.md)
- [L2 · Queueing math](labs/L2.md)
- [L3 · Load testing](labs/L3.md)
- [L4 · Rate limiter](labs/L4.md)
- [Guided · Token bucket limiter and cache benchmark](projects/guided/README.md)
- [Independent · Capacity-aware service with SLO and queue telemetry](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Size a 200-RPS service with five seconds mean latency and distinguish in-flight population from the amount of compute to provision.

Continue to [A06 · Distributed Systems & Coordination](../A06-distributed-systems-coordination/README.md) when the prerequisite stage gates are met.
