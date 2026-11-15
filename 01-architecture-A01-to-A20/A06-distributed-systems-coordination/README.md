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

## Practice and exit gate

- [L1 · Distributed clocks](labs/L1.md)
- [L2 · Partition and retries](labs/L2.md)
- [L3 · Consensus simulation](labs/L3.md)
- [L4 · Distributed locks](labs/L4.md)
- [Guided · Replicated log and quorum simulator](projects/guided/README.md)
- [Independent · Idempotent distributed coordinator with fencing](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Trace a partition, election and recovery, then demonstrate how a stale lease holder is rejected at the resource.
