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

## Guided walkthrough

Start by measuring the workload. Then use those measurements to size caches, queues, and downstream capacity.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Measure traffic, latency, and saturation (A05.01–A05.08)

1. **[A05.01 · time vs throughput](lessons/A05.01.md).** Latency is duration for one observed operation. Throughput is completions per unit time over a defined window. Concurrency can improve throughput without improving individual duration. Five workers taking 0.1 s each can ideally complete 50 requests/s. The 0.1 s individual service time is unchanged.
2. **[A05.02 · QPS/RPS/TPS](lessons/A05.02.md).** A request can fan out into queries or transactions. QPS measures queries, RPS requests, TPS transactions, and each needs an observation point. At 20 requests/s, two transactions per request and three queries per transaction produce 40 TPS and 120 QPS if all work completes.
3. **[A05.03 · mean vs percentiles](lessons/A05.03.md).** An arithmetic mean weights values directly. A percentile is an order statistic or estimate computed under a specified convention. The nearest-rank p95 selects the value at rank ceil(0.95n). Nineteen 10 ms requests and one 210 ms request have a mean of 20 ms. Nearest-rank p99 is 210 ms.
4. **[A05.04 · p95/p99 and tail latency](lessons/A05.04.md).** Request completion can depend on the slowest branch. Independence is an assumption. Common overload or shared infrastructure can correlate tails. If each of ten independent branches meets the threshold 99% of the time, all ten meet it with probability 0.99^10≈90.44%.
5. **[A05.05 · Little law and assumptions](lessons/A05.05.md).** Little's Law relates mean population L, throughput λ, and mean time W in a stable observed system. Use matching boundaries and include queueing time if queue population is counted. 200 completions/s at five seconds mean time imply 1000 requests in flight. CPU allocation requires service demand and headroom separately.
6. **[A05.06 · utilization and queue build-up](lessons/A05.06.md).** High utilization leaves little capacity to absorb arrivals during a busy interval. For an M/M/1 model, arrival and service assumptions yield W=1/(μ−λ) for λ<μ. At service capacity μ=100/s and arrival λ=90/s, ideal M/M/1 W is 0.1 s, ten times the mean service demand of 0.01 s.
7. **[A05.07 · CPU vs I/O bottlenecks](lessons/A05.07.md).** Wall time includes CPU, storage and network waits, pool acquisition and scheduler delays. CPU and waiting can overlap across workers. A serial 200 ms request with 20 ms CPU spends 10% of its wall time on CPU in this simplified trace.
8. **[A05.08 · back-of-envelope resource units](lessons/A05.08.md).** Rates and capacities need dimensions and a decimal or binary convention. Multiply operation rate by bytes per operation before converting to bits/s. 2000 RPS and a 20 kB response give 40 MB/s or 320 Mb/s before protocol overhead.

### Scale and protect shared resources (A05.09–A05.22)

9. **[A05.09 · horizontal vs vertical scaling](lessons/A05.09.md).** Vertical scaling adds resources per instance. Horizontal scaling adds independent instances and can increase coordination, downstream fan-out, and connection count. Six 100 RPS app replicas have nominal 600 RPS capacity, but a shared database capped at 400 RPS limits the complete path.
10. **[A05.10 · load balancers and health checks](lessons/A05.10.md).** A health check defines an observation boundary. Readiness gates admission. A TCP listener check cannot establish application correctness. For three probes with a 5 s interval, detection is roughly 10–15 s with instantaneous failures depending on schedule alignment.
11. **[A05.11 · Redis caching](lessons/A05.11.md).** A remote cache adds a lookup on every request. Its benefit depends on hit ratio, lookup cost and backend load. Verify key namespacing, TTL and fallback behavior. With lookup c=2 ms, backend b=20 ms and hit fraction h=0.9, average path cost is c+(1−h)b=4 ms.
12. **[A05.12 · cache-aside/read-through/write-through](lessons/A05.12.md).** Cache-aside fills a cache on a miss. Read-through delegates loading to a cache layer. Write-through synchronously forwards writes under that design's contract. Partial failure still matters. With 100 requests and a 95% hit rate, five are expected to invoke origin under the simple one-fill model.
13. **[A05.13 · TTL and eviction](lessons/A05.13.md).** TTL bounds expiry, while eviction can remove eligible entries earlier due to memory policy. Redis eviction behavior depends on the configured policy and memory accounting. If a 200-entry cache receives 250 distinct live keys, at least 50 cannot reside simultaneously under the model.
14. **[A05.14 · LRU/LFU](lessons/A05.14.md).** LRU favors recent references. LFU favors frequent references, often using approximations or aging. A sequential scan may displace a hot set under pure recency. For capacity two, access hot, hot, cold, scan. LRU removes hot. An LFU model preferentially evicts the single-use cold key.
15. **[A05.15 · cache invalidation](lessons/A05.15.md).** An invalidation event does not automatically order concurrent cache fills. A generation or version check can refuse a value older than the invalidation floor. If a stale fill arrives 100 ms after invalidation and remains for 5 s, a naive cache can serve it until roughly 5.1 s after invalidation.
16. **[A05.16 · cache stampedes and hot keys](lessons/A05.16.md).** Stampedes occur when many clients miss at once and refill independently. Hot keys skew load even when aggregate capacity looks healthy. For 400 concurrent misses on one key, a per-process single-flight with four independent processes can reduce origin fills toward four instead of 400.
17. **[A05.17 · connection pools](lessons/A05.17.md).** Pool acquisition has an independent queue and timeout. Per-replica pool caps multiply and must fit the database budget after reserved capacity. Eight replicas with 15 connections permit 120 concurrent leases. If the database allows 80 after reserves, the cap exceeds budget by 40.
18. **[A05.18 · bulkheads](lessons/A05.18.md).** Separate resource partitions can contain failure propagation. A bulkhead should bound queue and execution resources and have a deliberate failure policy. With ten workers and an eight/two partition, A cannot occupy more than eight and B retains two. B cannot borrow idle A capacity in the fixed model.
19. **[A05.19 · batching](lessons/A05.19.md).** Batching amortizes fixed overhead but adds collection delay and may amplify retries. Use both size and timer thresholds. With fixed overhead 8 ms plus 1 ms per item, eight unbatched calls cost 72 ms versus 16 ms as one batch, excluding fill wait.
20. **[A05.20 · worker queues](lessons/A05.20.md).** Queues decouple arrivals and service. A sustained positive difference accumulates backlog. Retry, visibility lease and deduplication policies govern redelivery. At 120 arrivals/s and 90 completions/s over 10 s, a simple backlog grows by 300 items absent rejection.
21. **[A05.21 · rate limiter windows, token bucket/leaky bucket](lessons/A05.21.md).** Fixed windows reset together. Sliding windows count usage in a trailing interval. Token buckets permit a burst and refill. Leaky-bucket terminology can mean shaping departure or metering arrivals depending on context. A 10-per-second fixed window can admit 20 at t=0.999 and t=1.001 across two windows. A trailing one-second cap of 10 rejects the second group.
22. **[A05.22 · load shedding](lessons/A05.22.md).** Load shedding intentionally drops work before it consumes scarce resources. A bounded queue and retry hints can protect admitted work while rejecting excess. If 70 jobs arrive during a window that can admit 50, reject 20 under a fixed simple budget.

### Validate capacity and failure headroom (A05.23–A05.34)

23. **[A05.23 · single-flight request coalescing](lessons/A05.23.md).** Single-flight lets concurrent requests for a key share an in-progress result. Cancellation of one waiter should be considered separately from ownership of shared work. Ten simultaneous asks for one key can share one origin request. Ten distinct keys still need ten calls.
24. **[A05.24 · split hot keys](lessons/A05.24.md).** Split a commutative counter over several independently addressed subkeys and aggregate on reads. Extra keys increase query cost and alter snapshot semantics. At 800 updates/s across eight evenly selected subkeys, each gets an expected 100/s. Skew can push a shard above its mean.
25. **[A05.25 · consistency under invalidation](lessons/A05.25.md).** Failures can delay or reorder invalidation. Versions, tombstones, durable outbox events or read bypass can constrain stale reads under defined assumptions. Two-hour invalidation lag and a ten-minute TTL do not guarantee ten minutes of staleness if old readers continually refill. A monotonic generation fence rejects older candidates.
26. **[A05.26 · sharding and resharding](lessons/A05.26.md).** Naive modulo routing changes many assignments when the denominator changes. Resharding needs source and target ownership, copy, catch-up, cutover and rollback. For keys 0 through 11, changing modulo three to four moves nine keys. Data migration cost also depends on bytes per moved key.
27. **[A05.27 · consistent/rendezvous hashing](lessons/A05.27.md).** Consistent hashing and rendezvous hashing seek stable placement under membership changes. Rendezvous picks the highest stable key-node score. Adding a node can only move a key to the added node. With three existing equal nodes and one added node, the new node wins about one-quarter of keys under uniform independent scores.
28. **[A05.28 · probabilistic cache admission](lessons/A05.28.md).** Frequency-aware admission can refuse cold items instead of admitting everything. TinyLFU-style approaches approximate recent access frequency, with counters and aging. If eight of ten scanned keys are one-off and are rejected, two enter the cache rather than ten under the simplified trace.
29. **[A05.29 · queueing model and contention](lessons/A05.29.md).** Queue models make assumptions about arrival, service and resource sharing. Use interarrival and service distributions, correlations and observed throughput before applying formulas. An M/M/1 model at λ=80 and μ=100 requests/s predicts mean residence 50 ms. The prediction does not cover arbitrary burst or service distributions.
30. **[A05.30 · cost-aware scaling](lessons/A05.30.md).** Unit cost includes compute, storage, network, downstream and idle capacity over a common window. Compare successful work and reliability outcomes. At 12 currency units/hour and 60000 successes/hour, cost is 0.0002 per success. At 30000 successes/hour with the same spend it doubles.
31. **[A05.31 · latency budgeting](lessons/A05.31.md).** Allocate an end-to-end budget across serial dependencies and admission, transport and retry work. Parallel branches contribute along the critical path, with joint tail behavior captured experimentally. A 300 ms budget minus 60 ms ingress and 150 ms backend leaves 90 ms for other serial work.
32. **[A05.32 · experiments, benchmarks and capacity envelopes](lessons/A05.32.md).** Include offered, accepted, successful, failed, rejected and timed-out rates. Open-loop load maintains arrivals independently of completions. Closed-loop often slows offered load during stalls. If 1000 requests are offered, 800 accepted and 700 successful, the end-to-end success rate is 70%, versus 87.5% among accepted work.
33. **[A05.33 · failure headroom](lessons/A05.33.md).** Failure headroom is capacity held against degraded operation and recovery. Verify dependencies and shared failure domains before counting interchangeable replicas. At 600 RPS required and 200 RPS safe capacity per replica, three cover normal load. Four cover the same load after one fails in this ideal model.
34. **[A05.34 · autoscaling interactions](lessons/A05.34.md).** Autoscaling is a feedback loop with measurement, stabilization, actuator delay and shared constraints. Per-tier scaling can multiply connection or queue pressure. Increasing from 6 to 12 replicas with 10 connections each doubles the maximum to 120. For a shared cap of 80, budget must be at most floor(80/12)=6 each under equal division.

### Put it together

For an API handling 240 requests/s at an average end-to-end latency of 250 ms, Little’s Law gives about 60 requests in the system under stable conditions. If a rollout doubles the worker count, recompute the combined database connection ceiling. Check that p99 stays within budget when a worker is lost and that extra concurrency does not move the bottleneck to the database.

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
