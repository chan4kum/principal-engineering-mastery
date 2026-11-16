# A16 · 18-category system design crosswalk

The roadmap audit organizes system design into 18 categories. Use the linked implementation to ground the case and then answer the transfer question under a new workload. The industry examples are independent references for comparative reasoning.

| Category | Curriculum anchor | Design exercise and evidence |
| --- | --- | --- |
| 01 Foundations | [Sizing](lessons/A16.04.md), [performance](../A05-scalability-caching-performance/README.md) | Choose a single-node baseline. Quantify steady and peak QPS, working-set bytes and recovery before dividing it. |
| 02 APIs, services and protocols | [API design](lessons/A16.08.md), [networking](../A02-networking-and-communication/README.md), [integration](../A07-application-integration-arch/README.md) | Compare HTTP streaming and gRPC paths. Budget queues, idempotent operations and one slow consumer. |
| 03 Data modeling and SQL | [Storage and SQL](../A04-databases-sql-and-storage-engines/README.md) | Design a seat table and indexes. Supply one replay trace and one migration with mixed schema versions. |
| 04 NoSQL, partitions and IDs | [Coordination](../A06-distributed-systems-coordination/README.md) | Partition a write-heavy keyspace. Compute hottest-shard utilization, token space and pagination under concurrent writes. |
| 05 Caching | [Scaling and caching](../A05-scalability-caching-performance/README.md) | Compare TTL and versioned invalidation during a stampede. Measure load on the origin after one cache partition disappears. |
| 06 Coordination | [Coordination](../A06-distributed-systems-coordination/README.md) | Trace a Raft quorum and stale lease holder. Compare fencing with time-based authorization and explain gossip and DHT roles. |
| 07 Storage engines | [Storage and SQL](../A04-databases-sql-and-storage-engines/README.md) | Trace WAL to memtable, sorted table and compaction. Compare Bitcask, LSM and Bloom filters and reproduce one recovery trace. |
| 08 Async work and streams | [Integration](../A07-application-integration-arch/README.md) | Sketch a durable work queue and replayable stream. Compare a database claim loop using SKIP LOCKED with consumer offsets and idempotent effects. |
| 09 Search and retrieval | [Retrieval](../A12-search-rag-and-knowledge-systems/README.md) | Separate inverted-index lexical ranking, approximate nearest neighbor search and permission checks. Rehearse index freshness and a deletion. |
| 10 Analytics and sketches | [Approximation](lessons/A16.26.md) | Estimate distincts with HLL, frequencies with CMS, quantiles with t-digest and top-k with a bounded heap. Compare each sketch to exact results on a skewed dataset and contrast with reservoir sampling. |
| 11 Realtime, social and feed | [Feed](lessons/A16.16.md), [networking](../A02-networking-and-communication/README.md) | Compare push and pull for two follower distributions. Defend SSE or WebSockets, resume point, per-user read state and backpressure. |
| 12 Geo, matching and recommendations | [Nearby search](lessons/A16.19.md), [spatial partitioning](lessons/A16.25.md), [recommendation](lessons/A16.18.md) | Cover a polygon with candidate cells, test geometric false positives, and filter seen results. Compare H3, S2 and geohash boundary behavior. |
| 13 Media, files and CDN | [Media ingestion](lessons/A16.23.md), [realtime media](lessons/A16.24.md), [containers](../A09-cloud-containers-k8s-devsecops/README.md) | Trace a signed multipart upload into an object store, transcode queue and rendition manifest. Test duplicate parts, CDN invalidation and stalled playback. |
| 14 Reliability and operations | [SRE](../A08-reliability-operations-and-sre/README.md), [security](../A15-security-privacy-global-scale/README.md) | Induce a local dependency timeout and record recovery, SLO budget, restore point, authorization state and evidence after a migration. |
| 15 Service and data designs | [URL shortener](lessons/A16.11.md), [object storage](lessons/A16.21.md), [integration](../A07-application-integration-arch/README.md) | Compare URL generation, limiter admission, immutable object IDs and an ordered partitioned log. Identify invariants and partition keys. |
| 16 Product designs | [Tickets](lessons/A16.13.md), [payments](lessons/A16.14.md), [messaging](lessons/A16.15.md), [search](lessons/A16.17.md) | Defend booking capacity and idempotent payment, replay a notification and connect chat, feed, and search contracts. |
| 17 Media and operations designs | [File sync](lessons/A16.22.md), [migration](lessons/A16.28.md), [nearby search](lessons/A16.19.md) | Compare file sync and video backfills to a ride matching workload. Design rollout observations, rollback triggers and data repair. |
| 18 Engineering case studies | [Coordination](../A06-distributed-systems-coordination/README.md), [architecture defense](labs/L4.md) | Compare documented decisions from Dynamo, Stripe idempotency, Discord message storage, Instagram and GitLab. Extract one constraint and evaluate whether it applies to the booking prototype. |

## Quantitative checks

- A Count-Min Sketch with width ⌈e/ε⌉ and depth ⌈ln(1/δ)⌉ provides the standard additive error bound for nonnegative updates under the hashing assumptions in the original analysis. With ε=0.01 and δ=0.05 the dimensions are 272 × 3, or 816 counters. For 10,000 increments, the additive error bound is 100 with probability at least 95%. Verify exact counts beside estimates and report heavy collisions.
- HyperLogLog uses a typical relative standard error of approximately 1.04/√m for register count m under its modeling assumptions. At 4096 registers the estimate is approximately 1.625%. Error is not a deterministic per-query guarantee.
- Six candidate locations with distances 0.8, 1.9, 2.0, 2.1, 2.8 and 4.0 km and radius 2 km yield three exact matches. The cover step alone yields six candidates. Define coordinate reference and treatment of equality.
- A fixed 250 Mbit/s media ingress split into 20% upload retries consumes 50 Mbit/s in retry traffic. Queue latency grows if work arrives faster than transcoding can sustain. Measure output behavior separately at each CDN rendition and during origin failover.

## Primary sources for comparison

- [Count-Min Sketch paper by Cormode and Muthukrishnan](https://moodle2.units.it/pluginfile.php/717089/mod_resource/content/0/4.Count_min_sketchl.pdf)
- [HyperLogLog paper by Flajolet and coauthors](https://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf)
- [H3 documentation](https://h3geo.org/docs/)
- [Stripe API idempotent requests](https://docs.stripe.com/api/idempotent_requests)
- [Discord message storage](https://discord.com/blog/how-discord-stores-trillions-of-messages)
- [Amazon Dynamo paper](https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store)
- [Instagram engineering](https://engineering.fb.com/2025/05/21/production-engineering/journey-to-1000-models-scaling-instagrams-recommendation-system/)
- [GitLab reference architectures](https://docs.gitlab.com/administration/reference_architectures/)
