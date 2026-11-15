# A05 · Applied assessment

Pass eight of ten, then repeat with fresh inputs after a delay.

1. Eight workers each hold a request for 100 ms. Estimate ideal steady service rate.
2. An API averages 200 completions/s and five seconds mean residence. Estimate in-flight work and say whether that determines CPU count.
3. With a cache lookup of 2 ms on every request, 90% hits and a 20 ms miss fetch, find expected latency under a serial model.
4. A cache has TTL 30 s and can hold two keys. Can insertion of a third key remove a value before 30 s?
5. Ten independent branches each have 99% probability of meeting a limit. Approximate the chance all ten meet it.
6. Rate is 120 arrivals/s and 90 completions/s over 10 s. Estimate backlog growth with no rejections.
7. A two-token bucket starts full and refills 2/s. After two admissions at time 0, when can it admit one more?
8. A test reports 700 successes, 100 failures after admission, and 200 rejected arrivals. Compute end-to-end success.
9. A workload requires 600 RPS with 200 RPS safe per replica. How many interchangeable replicas cover one failure?
10. Each of 12 app replicas can open 10 database connections. If the shared safe cap is 80, what equal per-replica budget fits?

<details>
<summary>Answers</summary>

1. 80 requests/s under continuous ideal utilization.
2. 1000 concurrent requests using Little's Law under stable measurement. CPU depends on service demand and headroom.
3. 4 ms, from 2 + 0.1×20.
4. Yes, eviction can occur before expiry.
5. About 90.44%.
6. 300 items.
7. At 0.5 s.
8. 70% of 1000 offered.
9. Four.
10. Six, with eight connections of unused arithmetic capacity before other reserves.

</details>

## Source scenario

Adding API replicas exhausted the database pool. Trace each acquisition boundary and calculate a shared budget. Design one change to preserve database admission when app capacity grows. Then answer the principal question: when could a cache decrease availability or create stale-data safety risks? Compare cache failure fallback, refill storms and stale reads after mutation.
