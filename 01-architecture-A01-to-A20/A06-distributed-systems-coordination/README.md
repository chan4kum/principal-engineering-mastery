# A06 · Distributed Systems & Coordination

**32 lessons · 4 labs · 2 projects**

Reason about operations when observers disagree, messages arrive late, and leadership changes. Lesson IDs and tiers match both curriculum indexes. Simulations declare their timing and failure assumptions. The partition lab also uses an actual loopback transport.

Prerequisite [A05 exit gate](../A05-scalability-caching-performance/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A06.01](lessons/A06.01.md) | partial failure | Foundation |
| [A06.02](lessons/A06.02.md) | time and clocks | Foundation |
| [A06.03](lessons/A06.03.md) | network partition | Foundation |
| [A06.04](lessons/A06.04.md) | retries and duplicates | Foundation |
| [A06.05](lessons/A06.05.md) | delivery guarantees | Foundation |
| [A06.06](lessons/A06.06.md) | ordering | Foundation |
| [A06.07](lessons/A06.07.md) | monotonic sequence numbers | Foundation |
| [A06.08](lessons/A06.08.md) | safety vs liveness | Foundation |
| [A06.09](lessons/A06.09.md) | failure detection limits | Foundation |
| [A06.10](lessons/A06.10.md) | consistency models | Core |
| [A06.11](lessons/A06.11.md) | linearizability vs serializability | Core |
| [A06.12](lessons/A06.12.md) | eventual consistency | Core |
| [A06.13](lessons/A06.13.md) | leader/follower | Core |
| [A06.14](lessons/A06.14.md) | quorums | Core |
| [A06.15](lessons/A06.15.md) | CAP limits and PACELC | Core |
| [A06.16](lessons/A06.16.md) | Lamport clocks | Core |
| [A06.17](lessons/A06.17.md) | vector clocks | Core |
| [A06.18](lessons/A06.18.md) | consensus/Raft | Core |
| [A06.19](lessons/A06.19.md) | elections, terms and log replication | Core |
| [A06.20](lessons/A06.20.md) | distributed locks, leases and fencing | Core |
| [A06.21](lessons/A06.21.md) | idempotency and deduplication | Core |
| [A06.22](lessons/A06.22.md) | split brain and stale lease holder | Principal |
| [A06.23](lessons/A06.23.md) | transaction coordination and sagas | Principal |
| [A06.24](lessons/A06.24.md) | metadata discovery | Principal |
| [A06.25](lessons/A06.25.md) | gossip and membership | Principal |
| [A06.26](lessons/A06.26.md) | distributed hash tables | Principal |
| [A06.27](lessons/A06.27.md) | consistent/rendezvous hashing | Principal |
| [A06.28](lessons/A06.28.md) | causal consistency | Principal |
| [A06.29](lessons/A06.29.md) | CRDT overview | Principal |
| [A06.30](lessons/A06.30.md) | clock skew | Principal |
| [A06.31](lessons/A06.31.md) | distributed ID/Snowflake | Principal |
| [A06.32](lessons/A06.32.md) | failure injection and linearizability test design | Principal |

## Guided walkthrough

Track what each participant knows when a request crosses a network and the participants can fail independently.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Reason about failure, time, and ordering (A06.01–A06.09)

1. **[A06.01 · partial failure](lessons/A06.01.md).** Partial failure means components have different observations and progress. A client timeout alone cannot distinguish a lost request from a lost reply. Use a durable operation identity or a separate outcome query. With one original attempt and two retries, up to three deliveries can occur. Correct scoped deduplication reduces three equal deliveries to one effect.
2. **[A06.02 · time and clocks](lessons/A06.02.md).** Wall clocks represent calendar time and can jump. Monotonic clocks measure intervals in one observer's time domain. Logical clocks capture ordering constraints without measuring physical duration. When a wall reading moves from 30 s to 25 s, subtraction says −5 s. Monotonic readings of 9 s and 12 s correctly indicate 3 s elapsed on that observer.
3. **[A06.03 · network partition](lessons/A06.03.md).** A partition can be asymmetric and selective. Routing, direction and fault duration affect what each participant can observe. Full membership is not guaranteed by local availability. Three replicas split 2+1. Under majority writes, only the component with two can gather quorum, assuming each replica votes once.
4. **[A06.04 · retries and duplicates](lessons/A06.04.md).** The network can deliver duplicates when callers retry an unknown result. At-least-once delivery and exactly-once business effects require different contracts. Two deliveries of amount 5 create effect 10 if independently applied, versus 5 with transactional deduplication.
5. **[A06.05 · delivery guarantees](lessons/A06.05.md).** At-most-once may lose delivery. At-least-once allows duplicates. Exactly-once effects require atomic state and replay handling at the specified boundary. An ACK can be lost after the side effect. For 100 logical messages and 10 redeliveries, there are 110 deliveries. A correct idempotent sink can retain 100 unique effects.
6. **[A06.06 · ordering](lessons/A06.06.md).** Ordering can be per key, per partition, causal or total. A transport or partition guarantee does not order data across independent channels. With two ordered events in each of two independent partitions, six valid interleavings preserve both within-partition orders.
7. **[A06.07 · monotonic sequence numbers](lessons/A06.07.md).** Sequences compare claims within their scope. Persist the counter or pair it with a fenced term or epoch. Gaps require a policy. Monotonic increase does not imply contiguous data. Lexicographically (6,1) exceeds (5,99) even though the local counter decreased from 99 to 1.
8. **[A06.08 · safety vs liveness](lessons/A06.08.md).** Safety rules exclude bad outcomes. Liveness rules require good outcomes eventually under defined fault and timing assumptions. A safe system can be unavailable during a partition. For N=5, quorum floor(N/2)+1=3. A component with two retains safety by refusing to commit under this rule.
9. **[A06.09 · failure detection limits](lessons/A06.09.md).** In an asynchronous model, delays and crashes can be indistinguishable to an observer. Failure detectors provide suspicion under real timing assumptions, not perfect knowledge. With a three-period threshold and period 2 s, suspicion occurs after about 6 s of silence. A 7 s scheduler pause crosses that threshold without a crash.

### Choose consistency and coordination guarantees (A06.10–A06.21)

10. **[A06.10 · consistency models](lessons/A06.10.md).** Consistency models constrain permitted histories. Read-your-writes, eventual convergence and linearizability describe different properties and boundaries. A replica applying 80 changes/s against 100 writes/s falls behind by 20 per second when load persists, under a simple rate model.
11. **[A06.11 · linearizability vs serializability](lessons/A06.11.md).** Serializability requires a legal serial transaction ordering. Linearizability respects the real-time order of nonoverlapping operations. Strict serializability adds real-time order to transactional serializability. For two overlapping operations there can be two legal real-time orderings. For one completing before another begins, only one respects real time.
12. **[A06.12 · eventual consistency](lessons/A06.12.md).** Eventual consistency promises convergence when updates cease and delivery and merge assumptions hold. It does not establish bounded staleness or read-your-writes on its own. At 1 update/s with an explicit 10 s maximum delivery assumption, up to about 10 versions could be outstanding under a simple model. Eventual consistency itself supplies no such bound.
13. **[A06.13 · leader/follower](lessons/A06.13.md).** Leader/follower replication assigns an ordering role and a replication path. Leadership can change, and follower reads can lag. A leader's name alone does not prove authority. With three replicas and majority acknowledgment, a successful commit requires two copies under the simple model.
14. **[A06.14 · quorums](lessons/A06.14.md).** For N replicas, read/write quorums intersect when R+W>N. Write quorums intersect when 2W>N. Intersection alone does not implement consistency. Membership, version rules and time matter. For N=5, R=2 and W=3 can be disjoint, while R=3 and W=3 intersect by at least one.
15. **[A06.15 · CAP limits and PACELC](lessons/A06.15.md).** Formal CAP constrains availability and atomic consistency under a partition in the defined model. PACELC adds a decision about latency and consistency even when no partition is present. If remote quorum confirmation adds a 50 ms round trip, that cost can enter the ordinary write critical path even without a partition.
16. **[A06.16 · Lamport clocks](lessons/A06.16.md).** Lamport clocks increment on local/send events and set receive to max(local, incoming)+1. If an event happened before another, its Lamport time is lower. The reverse implication does not hold. At receiver counter 4 and message counter 7, max(4,7)+1=8.
17. **[A06.17 · vector clocks](lessons/A06.17.md).** Vector clocks track one component per participant under a fixed membership model. Compare componentwise. If neither vector dominates, events are concurrent in that model. A dense vector with 20 participants and 8 B counters contains 160 B before IDs or framing.
18. **[A06.18 · consensus/Raft](lessons/A06.18.md).** Raft organizes a consensus log into leader election, replication and safety rules. A leader uses majority replication and an eligible current-term entry to advance its commit index. A simulation can illustrate a subset. For 5 nodes, quorum 3. Two acknowledgments including the leader do not commit, three can commit an eligible entry.
19. **[A06.19 · elections, terms and log replication](lessons/A06.19.md).** Raft candidates compare last log term then index. Matching previous index and term is a prerequisite for appending. Committed entries survive valid elections under the protocol. A last term of 4 with index 7 is more up to date than term 3 at index 90 in the candidate comparison.
20. **[A06.20 · distributed locks, leases and fencing](lessons/A06.20.md).** A lease limits ownership under protocol and time assumptions. A fencing token is a monotonically increasing generation accepted or rejected by the actual resource. A resource with highest accepted token 8 rejects token 7. Equal-token policy depends on whether it represents a legitimate retry and on operation identity.
21. **[A06.21 · idempotency and deduplication](lessons/A06.21.md).** Deduplication has scope, retention and conflict rules. Record an operation identity with the effect and outcome so restart and concurrency cannot reopen the same action. Two identical commands adding 3 to 10 produce 16 without dedup and 13 with one effective application.

### Verify recovery and concurrent histories (A06.22–A06.32)

22. **[A06.22 · split brain and stale lease holder](lessons/A06.22.md).** Split brain means multiple components act as authority. Majority terms and a resource-enforced fence guard different boundaries. Granting a lock does not stop a paused holder's already-in-flight work. For 3 replicas, a 2+1 partition cannot have two disjoint sets of 2. Stale in-flight messages can still need fencing.
23. **[A06.23 · transaction coordination and sagas](lessons/A06.23.md).** Two-phase commit coordinates a transactional decision and can block in unresolved failure cases. A saga records workflow steps and compensations. Compensation is a business action and can fail or be retried. In a three-step saga failing at step three after the first two succeed, two committed steps may need compensation, depending on workflow semantics.
24. **[A06.24 · metadata discovery](lessons/A06.24.md).** Discovery returns endpoints and metadata under a consistency and freshness contract. Cached records can be outdated. Use generations or fencing where routing changes affect writes. A 30 s poll period plus 10 s local refresh delay can leave a 40 s modeled detection window when the assumptions hold.
25. **[A06.25 · gossip and membership](lessons/A06.25.md).** Gossip spreads observations over repeated contacts. Membership views can be stale and detectors can disagree. Random fanout is probabilistic and repeated contacts overlap. In an idealized no-overlap process where each informed node informs one new node, population can grow from 1 to at most 2^r after r rounds. Four rounds yield at most 16.
26. **[A06.26 · distributed hash tables](lessons/A06.26.md).** A distributed hash table routes via an overlay and limited routing state. The key and node-space mappings the protocol defines determine the next hop. In a model that halves remaining distance each hop, 1024 positions require at most 10 reductions. Real lookup cost depends on topology and churn.
27. **[A06.27 · consistent/rendezvous hashing](lessons/A06.27.md).** Consistent hashing and rendezvous hashing reduce key movement. Rendezvous uses stable key-node scores, and existing keys move only if the new node wins after an addition. Adding one equally weighted node to four makes expected winning share about 1/5 with uniform independent scores.
28. **[A06.28 · causal consistency](lessons/A06.28.md).** Causal consistency preserves visibility of dependent operations. Concurrent independent events may be ordered differently across replicas. Causal context helps know what predecessors are needed. With two dependent writes and one independent write, three of six total orders preserve the one dependency.
29. **[A06.29 · CRDT overview](lessons/A06.29.md).** A state-based CRDT uses a merge with associative, commutative and idempotent semantics. For a grow-only counter, each replica owns a component and merges by componentwise maximum. Merging [3,2] with an identical state preserves total 5. Elementwise addition would incorrectly return 10.
30. **[A06.30 · clock skew](lessons/A06.30.md).** Clock skew is a difference between contemporaneous readings. Drift describes rate differences over time. Time synchronization reduces these effects but does not make clocks identical. A local path lasting 8 ms can appear −7 ms when the downstream wall clock is 15 ms behind. Same-observer monotonic time avoids that subtraction.
31. **[A06.31 · distributed ID/Snowflake](lessons/A06.31.md).** A time-based bit layout commonly combines timestamp, worker identity and per-unit sequence. Unique worker assignment, sequence overflow and clock regression policies are part of correctness. A 12-bit sequence permits 4096 distinct IDs per worker per time unit before advancing or waiting. Capacity alone does not cover regressed timestamps.
32. **[A06.32 · failure injection and linearizability test design](lessons/A06.32.md).** A linearizability test records invocation and response, preserves real-time precedence for nonoverlapping calls, and looks for a legal sequential specification. Fault injection needs a scoped model and observable oracle. For four fully overlapping operations, naive search may inspect 4!=24 orders. Precedence and model pruning reduce the search.

### Put it together

A client times out after sending a transfer. The server may have committed before its reply was lost. Use the original operation ID to query the outcome or retry through durable deduplication. If ownership changed in the meantime, the storage layer must reject the old owner’s fencing token. Check the recorded history for a single committed effect.

## Practice and exit gate

- [L1 · Distributed clocks](labs/L1.md)
- [L2 · Partition and retries](labs/L2.md)
- [L3 · Consensus simulation](labs/L3.md)
- [L4 · Distributed locks](labs/L4.md)
- [Guided · Replicated log and quorum simulator](projects/guided/README.md)
- [Independent · Idempotent distributed coordinator with fencing](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Trace a partition, election and recovery, then demonstrate how a stale lease holder is rejected at the resource.

Continue to [A07 · Application & Integration Architecture](../A07-application-integration-arch/README.md) when the prerequisite stage gates are met.
