# A16 · System Design & Product-Company Interviews

**34 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../A15-security-privacy-global-scale/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [A16.01](lessons/A16.01.md) | requirements discovery | Foundation |
| [A16.02](lessons/A16.02.md) | user stories | Foundation |
| [A16.03](lessons/A16.03.md) | functional vs nonfunctional | Foundation |
| [A16.04](lessons/A16.04.md) | back-of-envelope QPS/storage | Foundation |
| [A16.05](lessons/A16.05.md) | latency budgets | Foundation |
| [A16.06](lessons/A16.06.md) | architectural trade-offs | Foundation |
| [A16.07](lessons/A16.07.md) | SLOs and cost constraints | Foundation |
| [A16.08](lessons/A16.08.md) | API and schema design | Core |
| [A16.09](lessons/A16.09.md) | baseline single-machine design | Core |
| [A16.10](lessons/A16.10.md) | scale bottlenecks | Core |
| [A16.11](lessons/A16.11.md) | URL shortener | Core |
| [A16.12](lessons/A16.12.md) | rate limiter | Core |
| [A16.13](lessons/A16.13.md) | ticket booking | Core |
| [A16.14](lessons/A16.14.md) | payment | Core |
| [A16.15](lessons/A16.15.md) | messaging and notification | Core |
| [A16.16](lessons/A16.16.md) | feed | Core |
| [A16.17](lessons/A16.17.md) | search | Core |
| [A16.18](lessons/A16.18.md) | recommendation | Core |
| [A16.19](lessons/A16.19.md) | nearby search | Core |
| [A16.20](lessons/A16.20.md) | collaborative editor | Core |
| [A16.21](lessons/A16.21.md) | object storage | Core |
| [A16.22](lessons/A16.22.md) | file sync | Core |
| [A16.23](lessons/A16.23.md) | video upload and CDN | Core |
| [A16.24](lessons/A16.24.md) | live streaming and WebRTC | Principal |
| [A16.25](lessons/A16.25.md) | geohash/H3/S2 | Principal |
| [A16.26](lessons/A16.26.md) | analytics sketches HLL/CMS/t-digest | Principal |
| [A16.27](lessons/A16.27.md) | identity and audit | Principal |
| [A16.28](lessons/A16.28.md) | migration design | Principal |
| [A16.29](lessons/A16.29.md) | design failure injections | Principal |
| [A16.30](lessons/A16.30.md) | live interview communication | Principal |
| [A16.31](lessons/A16.31.md) | strong vs eventual consistency | Principal |
| [A16.32](lessons/A16.32.md) | architecture decision records | Principal |
| [A16.33](lessons/A16.33.md) | DSA-to-system-design transfer | Principal |
| [A16.34](lessons/A16.34.md) | principal staff influence | Principal |

## Guided walkthrough

Turn ambiguous requirements into a design that makes capacity, correctness, and failure behavior testable.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Discover requirements and quantify trade-offs (A16.01–A16.07)

1. **[A16.01 · requirements discovery](lessons/A16.01.md).** Identify users, core operations, volumes, constraints and unacceptable outcomes. Confirm assumptions with stakeholder and specify evidence for each. Four assumptions, three confirmed, so one remains.
2. **[A16.02 · user stories](lessons/A16.02.md).** Write actor, need and user outcome, then define observable acceptance criteria. Trace each acceptance criterion to a user journey and test it. Of 4 acceptance cases, 3 are covered.
3. **[A16.03 · functional vs nonfunctional](lessons/A16.03.md).** A functional requirement specifies behavior. A quality requirement constrains how well or under what conditions that behavior must hold. Create and resolve are operations, 100 ms and 99.9% are quality targets. There are two operations.
4. **[A16.04 · back-of-envelope QPS/storage](lessons/A16.04.md).** Divide daily traffic by 86400 s, estimate high-water traffic separately, and budget storage with retention, replicas and indexes. 8,640,000 requests/day is 100/s average. With factor 4 the peak fixture is 400/s.
5. **[A16.05 · latency budgets](lessons/A16.05.md).** For a serial critical path, add component durations at the request level. Percentiles generally do not add. Correlate per-request traces. Gateway 12, storage 28 and network 10 ms total 50 ms.
6. **[A16.06 · architectural trade-offs](lessons/A16.06.md).** Define competing alternatives, record measurable consequences and choose against hard constraints before weighted preferences. Option A costs 5 and takes 80 ms. B costs 9 and takes 70 ms. Under cost cap 7 only A qualifies.
7. **[A16.07 · SLOs and cost constraints](lessons/A16.07.md).** Choose a user-facing SLI numerator and denominator. An allowed failure fraction times eligible events gives the event error budget. SLO 99.9% with 10,000 eligible requests allows 10 failures.

### Design systems around concrete workloads (A16.08–A16.23)

8. **[A16.08 · API and schema design](lessons/A16.08.md).** Define resource identity, constraints, status semantics and version evolution. A scoped idempotency key must bind the request payload and result. Two retries on same tenant/key yield one stored logical request.
9. **[A16.09 · baseline single-machine design](lessons/A16.09.md).** Start with transactional persistence and clear invariants. Measure data size, queue delay and failure modes under representative workload before splitting. Read 200/s with observed capacity 500/s gives load ratio 0.4.
10. **[A16.10 · scale bottlenecks](lessons/A16.10.md).** A pipeline is capped by the narrowest stage. Identify bottlenecks by queue growth, utilization and saturation rather than by component count. Stages support 400,150,300/s. Peak throughput is bounded by 150/s.
11. **[A16.11 · URL shortener](lessons/A16.11.md).** Create an opaque key under uniqueness constraint, verify redirect policy and store lifecycle. HTTP redirect caching has consequences for mutable destinations. An alphabet of size 4 with 3 characters contains 64 distinct tokens. For two characters the count is 16.
12. **[A16.12 · rate limiter](lessons/A16.12.md).** Choose a key, unit, time model and coordination scope. Per-process buckets bound each worker, while a shared bound needs coordination. Four independent buckets of 10 can collectively accept 40. Intended shared cap is 10.
13. **[A16.13 · ticket booking](lessons/A16.13.md).** Use a conditional write within a transaction and a uniqueness rule for the active seat. Define hold expiry and payment transitions. Two requests against one seat leave one successful reservation.
14. **[A16.14 · payment](lessons/A16.14.md).** Record provider event identity, bind idempotency to payload and use integer minor units. Reconcile against the provider ledger. Event p1 is delivered twice and p2 once. Unique ledger effects count two.
15. **[A16.15 · messaging and notification](lessons/A16.15.md).** Use durable enqueue and consumer idempotency. Preserve event identity across retries and decide whether ordering is required per recipient. Events e1,e2,e1 yield two unique effects.
16. **[A16.16 · feed](lessons/A16.16.md).** Write fanout moves work to publishing. Read fanout moves it to readers. Choose hybrid classes based on observed follower distributions and staleness target. Three posts to 200 followers create up to 600 entries versus three stored posts before read-time fanout.
17. **[A16.17 · search](lessons/A16.17.md).** Model ingestion, index refresh and serving eligibility independently. Use tombstones or version filters until the serving index reconciles. Index has two documents, one denied by an updated tombstone set, so one remains.
18. **[A16.18 · recommendation](lessons/A16.18.md).** Separate retrieval, scoring and constraints. Track exposure diversity, eligible inventory and randomized or carefully controlled outcome metrics. A list of four slots contains only two distinct categories. Unique share is 0.5.
19. **[A16.19 · nearby search](lessons/A16.19.md).** Use spatial partitioning to find candidates then compute an exact distance under the selected geometry. Include adjacent cells where the query crosses boundaries. Eligible distance threshold 2 includes distances 1 and 2, and rejects 3.
20. **[A16.20 · collaborative editor](lessons/A16.20.md).** Decide conflict semantics and deterministic ordering. Idempotent delivery and convergent merge require stronger properties than arrival order alone. Set union of observed op IDs {1,2} and {2,3} produces three unique operations.
21. **[A16.21 · object storage](lessons/A16.21.md).** Separate blob data from metadata where useful. Define immutable object identity, checksum verification and safe deletion of unreferenced objects. Three 8 MiB blobs need 24 MiB before replication. Factor two needs 48 MiB.
22. **[A16.22 · file sync](lessons/A16.22.md).** Store version identities and check the expected prior version before accepting writes. For conflicts, retain work and define merge policy. Local expects version 3 and current version is 4. Compare-and-set refuses.
23. **[A16.23 · video upload and CDN](lessons/A16.23.md).** Split ingestion, asynchronous transcoding, manifest generation and edge delivery. Verify each rendition before marking it eligible for playback. A 240 s video at 4 Mbit/s needs 120 MB decimal before overhead.

### Defend the design under change and failure (A16.24–A16.34)

24. **[A16.24 · live streaming and WebRTC](lessons/A16.24.md).** WebRTC handles interactive real-time media and negotiates network paths and media parameters. Track forwarding and congestion separately from playback delivery. Five peers in a full mesh give each peer four outgoing streams and 20 directed streams.
25. **[A16.25 · geohash/H3/S2](lessons/A16.25.md).** H3, S2 and geohash approximate locations at discrete resolutions with different cells and neighbor semantics. Use exact geometry for final selection. Three cells have candidate counts 2,1,3. A one-cell query checks two while all three check six.
26. **[A16.26 · analytics sketches HLL/CMS/t-digest](lessons/A16.26.md).** HLL approximates distinct counts, Count-Min Sketch estimates nonnegative frequency and t-digest aggregates quantile summaries. Select according to error behavior and merge constraints. A Count-Min query sees counters [4,7,5], so its estimate is min=4.
27. **[A16.27 · identity and audit](lessons/A16.27.md).** Derive identity from the authentication boundary, check permissions at operation time, and preserve decision and trace identifiers under minimization rules. Three writes, two correlated identities. One write violates the provenance requirement.
28. **[A16.28 · migration design](lessons/A16.28.md).** Use a migration contract with backfill, reconciliation, shadow reads, compatibility and rollback bounds. Agree on the source of truth during each state. Out of 100 paired reads, 98 match. Two discrepancies block a zero-difference gate.
29. **[A16.29 · design failure injections](lessons/A16.29.md).** Define deadlines, bounded retries and fallback behavior per dependency. Measure the expected evidence during controlled isolated failure. Three layers each permit two attempts, so one original call can cause eight downstream attempts.
30. **[A16.30 · live interview communication](lessons/A16.30.md).** State the user journey, scale and invariants. Draw one complete path and compare concrete alternatives using visible trade-offs. Two hard constraints are latency ≤80 and cost ≤5. Only (75,4) passes among (75,4),(70,6),(85,3).
31. **[A16.31 · strong vs eventual consistency](lessons/A16.31.md).** Define the exact consistency promise per operation: latest under linearizability, session guarantees or convergence under eventual consistency. Trace reads relative to successful writes. Write response observed at version 9 and subsequent read at 8 violates read-your-writes in this model.
32. **[A16.32 · architecture decision records](lessons/A16.32.md).** Record context, decision, alternatives, consequences and status. Supersede a changed decision and retain its history. Two ADRs in one chain, with v1 superseded by v2, leave one current decision.
33. **[A16.33 · DSA-to-system-design transfer](lessons/A16.33.md).** Translate data-structure complexity to memory and throughput bounds. Compare approximate structures only when the product tolerates their error. A million 16-byte entries need at least 16 MB decimal before overhead.
34. **[A16.34 · principal staff influence](lessons/A16.34.md).** Build shared evidence, clarify ownership and define a review mechanism. Influence across teams requires feedback and measurable adoption. Four teams agree, but only three emit comparable verification evidence, leaving one unresolved.

### Put it together

For ticket booking, start with the invariant that one seat has at most one successful reservation for a performance. Build a baseline that makes the reservation atomic. Test two simultaneous attempts and a retry after a lost reply. Add scaling only after measuring where the baseline saturates.

## Practice and exit gate

- [L1 · Requirements modeling](labs/L1.md)
- [L2 · Quantitative sizing](labs/L2.md)
- [L3 · Failure review](labs/L3.md)
- [L4 · Architecture defense](labs/L4.md)
- [URL shortener from one machine](projects/guided/README.md)
- [Scalable transaction-critical product design and prototype](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)
- [18-category system design crosswalk](SYSTEM_DESIGN_MATRIX.md)

Score at least 80% on fresh cases, reproduce four labs, meet both project acceptance criteria, diagnose one unfamiliar failure, and repeat the assessment after a delay.

Continue with [A17 · Regulated AI: Compliance, Safety & Governance](../A17-regulated-ai-compliance-governance/README.md) after the applicable gates.
