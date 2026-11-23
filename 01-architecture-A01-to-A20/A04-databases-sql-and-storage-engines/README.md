# A04 · Databases, SQL & Storage Engines

**37 lessons · 4 PostgreSQL labs · 2 projects**

Trace a row from application invariants and SQL plans through storage, concurrency and recovery. Lesson IDs and tiers match both curriculum indexes. Examples distinguish arithmetic and simplified models from actual engine observations. The PostgreSQL labs use major version 18.

Prerequisite [A03 exit gate](../A03-python-runtime-and-backend-apis/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A04.01](lessons/A04.01.md) | bytes and pages | Foundation |
| [A04.02](lessons/A04.02.md) | record layouts | Foundation |
| [A04.03](lessons/A04.03.md) | relational tables, keys and constraints | Foundation |
| [A04.04](lessons/A04.04.md) | normalization | Foundation |
| [A04.05](lessons/A04.05.md) | SQL operations | Foundation |
| [A04.06](lessons/A04.06.md) | query plans | Foundation |
| [A04.07](lessons/A04.07.md) | disk seek and random vs sequential I/O | Foundation |
| [A04.08](lessons/A04.08.md) | indexes | Foundation |
| [A04.09](lessons/A04.09.md) | B-tree and B+tree intuition | Foundation |
| [A04.10](lessons/A04.10.md) | ACID and transactions | Core |
| [A04.11](lessons/A04.11.md) | locks | Core |
| [A04.12](lessons/A04.12.md) | isolation levels | Core |
| [A04.13](lessons/A04.13.md) | lost updates/phantoms | Core |
| [A04.14](lessons/A04.14.md) | MVCC | Core |
| [A04.15](lessons/A04.15.md) | WAL/redo/undo concepts | Core |
| [A04.16](lessons/A04.16.md) | checkpoints and crash recovery | Core |
| [A04.17](lessons/A04.17.md) | backup and point-in-time restore | Core |
| [A04.18](lessons/A04.18.md) | schema migration and online indexing | Core |
| [A04.19](lessons/A04.19.md) | keyset vs offset pagination | Core |
| [A04.20](lessons/A04.20.md) | soft deletion and retention | Core |
| [A04.21](lessons/A04.21.md) | document vs key-value vs graph vs columnar stores | Core |
| [A04.22](lessons/A04.22.md) | PostgreSQL query analysis | Core |
| [A04.23](lessons/A04.23.md) | file-backed dictionaries | Principal |
| [A04.24](lessons/A04.24.md) | binary encodings | Principal |
| [A04.25](lessons/A04.25.md) | append-only and log-structured storage | Principal |
| [A04.26](lessons/A04.26.md) | Bitcask | Principal |
| [A04.27](lessons/A04.27.md) | LSM memtable/WAL/SSTable | Principal |
| [A04.28](lessons/A04.28.md) | Bloom/sparse indexes | Principal |
| [A04.29](lessons/A04.29.md) | compaction and write amplification | Principal |
| [A04.30](lessons/A04.30.md) | range and hash partitioning | Principal |
| [A04.31](lessons/A04.31.md) | shard maps | Principal |
| [A04.32](lessons/A04.32.md) | object store metadata | Principal |
| [A04.33](lessons/A04.33.md) | consistency and replication | Principal |
| [A04.34](lessons/A04.34.md) | hot/cold archival | Principal |
| [A04.35](lessons/A04.35.md) | checksums | Principal |
| [A04.36](lessons/A04.36.md) | online evolution | Principal |
| [A04.37](lessons/A04.37.md) | data privacy deletions | Principal |

## Guided walkthrough

Follow an order from its SQL representation to disk, then through concurrent updates, recovery, and distribution. The linked lessons separate simplified storage models from PostgreSQL behavior. Use the labs to measure what the engine actually does.

### Rows, queries, and indexes (A04.01–A04.09)

1. **Bytes and pages.** A database page has space for a header, pointers to records, record bytes, and free space. In a simplified 8 KiB page with 32 bytes of fixed overhead, records that each consume 104 bytes including their slot fit at most `floor((8,192 − 32) ÷ 104) = 78` per page. Actual page occupancy depends on record layout and engine behavior.
2. **Record layouts.** A tuple can include a header, a null bitmap, padding for alignment, and variable-width fields. PostgreSQL can compress large values or store them out of line through TOAST. Estimate storage by inspecting representative rows, including sparse and large values.
3. **Keys and constraints.** A primary key identifies a row, a foreign key enforces a relationship, and a unique constraint restricts duplicate values. A PostgreSQL `CHECK (quantity > 0)` can admit `NULL` because the expression evaluates to unknown. Add `NOT NULL` when quantity is mandatory.
4. **Normalization.** If the customer key determines the current customer name, storing the name on every order creates several copies to update. Store the current name with the customer. An order can separately retain a name captured at purchase time when that historical value is part of the contract.
5. **SQL operations.** Joins build row combinations, filters remove rows, and grouping aggregates the remaining rows. One order with three line items produces three joined rows. Aggregate at the correct grain so that a value stored once per order is not counted three times. Use `ORDER BY` when callers depend on output order.
6. **Query plans.** The planner estimates row counts and operator costs to choose a physical plan. `EXPLAIN` shows those estimates. `EXPLAIN ANALYZE` executes the statement and reports observed work. Use care when analyzing a statement that changes data.
7. **Random and sequential I/O.** HDD seeks add mechanical latency to scattered reads, while SSDs have different latency and throughput characteristics. Request size, locality, queue depth, and cache state can still matter on SSDs. Compare plans under a stated cache state before attributing their difference to the device.
8. **Indexes.** An index can narrow a lookup or support ordering, while inserts and updates may also have to maintain it. In PostgreSQL, having all queried columns in an index can enable an index-only scan, but the engine may still need heap visibility checks.
9. **B-trees and B+tree intuition.** Internal pages use separator keys to select a child. A B+tree-style layout keeps indexed records or references at the leaves, where nearby keys support range scans. High fanout keeps the number of levels small even as the index grows.

### Transactions, recovery, and query analysis (A04.10–A04.22)

10. **ACID.** A transfer commits the debit and credit together or rolls them back together. Constraints and transaction logic enforce invariants. Isolation governs interactions between transactions, and durability depends on commit settings and which failures the deployment is designed to survive.
11. **Locks.** If one transaction holds A and waits for B while another holds B and waits for A, neither can proceed. PostgreSQL detects the cycle and aborts one participant. Acquire the same resources in a consistent order and retry eligible transactions at their full boundary.
12. **Isolation levels.** In PostgreSQL, Read Committed takes a new snapshot for each command. Repeatable Read generally holds one transaction snapshot. Serializable can reject a transaction when concurrent operations cannot safely commit together. The caller must handle serialization failures as part of the contract.
13. **Lost updates and phantoms.** Two workers that read stock `5` and both write the computed value `4` lose one decrement. An in-database conditional decrement can protect this operation. A phantom concerns a change in the set of rows matching a predicate, such as a newly inserted order qualifying on a later read.
14. **MVCC.** An update creates a new row version. Older snapshots can still see a previous version until they end. Vacuum makes eligible space available for reuse, so a long-lived snapshot can delay cleanup even when new writes continue successfully.
15. **WAL, redo, and undo.** Write-ahead logging records changes before the corresponding data pages reach durable storage. PostgreSQL can redo changes after a crash from durable WAL, and transaction visibility hides versions belonging to aborted or uncommitted transactions. Other engines may use explicit undo records.
16. **Checkpoints and crash recovery.** A checkpoint establishes a recovery starting point by making the required dirty state durable. Recovery replays the relevant WAL from that point. More frequent checkpoints can shorten the replay window at the cost of more checkpoint-related writes.
17. **Backups and point-in-time restore.** To restore PostgreSQL to just before a bad transaction, start with a compatible base backup and replay a continuous archived WAL chain to the chosen target. Restore into an isolated instance and verify the expected rows and constraints before relying on it.
18. **Schema migration and online indexes.** Expand the schema, deploy compatible code, backfill, then retire the old shape when it is safe. PostgreSQL `CREATE INDEX CONCURRENTLY` allows ordinary writes during the build, does extra work, runs outside a regular transaction block, and can leave an invalid index after failure.
19. **Keyset and offset pagination.** If a page ends at key `20` and key `15` is inserted, a keyset query for keys greater than `20` continues from the same boundary. An offset query counts positions again and can repeat or skip rows after changes. Use a stable ordering and unique tie-breaker.
20. **Soft deletion and retention.** A deletion marker can hide a row from active queries. A partial unique index can enforce uniqueness only for active rows. Define what happens when a deleted row is restored after a replacement has claimed its unique value.
21. **Storage models.** Key-value access suits lookups by key, document models group related fields, graph models emphasize relationship traversal, and columnar layouts can avoid reading unused columns during scans. Choose using actual query shapes and update patterns, since products can support several models.
22. **PostgreSQL query analysis.** Compare estimates and actual rows near the first divergence in the plan. A repeated node showing `3` actual rows and `100` loops produced roughly `300` rows across those invocations because rows are reported per loop. Use buffer counters to investigate page activity. A shared-buffer hit does not imply a device read.

### Storage engine internals (A04.23–A04.29)

23. **File-backed dictionaries.** A persistent map needs a format, a durability boundary, and a multi-writer policy. Reopen the file in a fresh process to test persistence. A successful lookup from the writer’s own in-memory state only verifies that path.
24. **Binary encodings.** In a four-byte big-endian length field, `00 00 01 00` means `256`. Require a complete header, bound the declared length, and verify the payload is present before decoding it. Define how to handle an incomplete trailing record after a crash.
25. **Append-only storage.** An update writes a new record while leaving the previous record in place. Recovery can reconstruct the latest state by reading complete valid records in order. Reclaiming obsolete data and handling a partial tail are explicit engine policies.
26. **Bitcask.** A Bitcask-style key directory points from each key to its newest record’s segment and offset. Reads use that pointer, deletions append tombstones, and merges reclaim old records. The in-memory directory consumes space proportional to the number of indexed keys.
27. **LSM write path.** A write enters the WAL and a mutable sorted memtable. Flushing makes an immutable sorted table on disk. Compaction later merges runs. Reads consult the relevant structures and honor the newest visible version or tombstone.
28. **Bloom filters and sparse indexes.** A Bloom filter can rule out an absent key in a run when the filter says negative. A positive can be a false positive, so verify it in the data. A sparse index narrows the search to the interval between sampled keys.
29. **Compaction and write amplification.** If ingesting 1 GiB leads to 5 GiB written at a consistently defined storage boundary, write amplification is `5×`. Measure under steady load because compaction can lag ingestion. Drop a tombstone only when older values cannot reappear from another run or replica.

### Distribution and lifecycle (A04.30–A04.37)

30. **Range and hash partitioning.** Range boundaries let time-window queries skip unrelated partitions. Hashing can distribute many distinct keys across owners, while an arbitrary range query may need multiple owners. A single heavily accessed key stays hot under ordinary hash partitioning.
31. **Shard maps.** A map assigns a key or range to an owner under a routing epoch. During migration, stale writers must refresh their route or be fenced by the storage protocol. Updating routing alone does not stop requests that were already in flight.
32. **Object store metadata.** An object and its external database pointer are separate writes. One design stores the immutable object revision, then commits the matching pointer. A reconciliation job can identify orphaned objects or broken pointers. Check guarantees per operation and backend.
33. **Consistency and replication.** A primary can acknowledge a write before an asynchronous replica applies it. Reading that replica immediately can return old state. A synchronous acknowledgment policy and a linearizable read policy answer different questions about what was recorded and what a reader may observe.
34. **Hot and cold archival.** Move infrequently accessed records to a storage tier with acceptable retrieval cost and delay. Maintain a catalog that can find the objects, verify restored content, and test that restoration meets the intended recovery time.
35. **Checksums.** A checksum mismatch can reveal accidental corruption. Recomputing the checksum cannot reconstruct the original bytes. Recover from an independently valid copy or redundancy, and use an authentication mechanism if you need protection against deliberate tampering.
36. **Online evolution.** Add the new shape, keep old and new clients compatible, backfill, and compare the results before switching reads. Retire the old shape after the rollback window and any applicable retention obligations permit it. Measure progress so the backfill can resume after interruption.
37. **Privacy deletions.** Propagate authoritative deletion decisions to live stores, replicas, derived indexes, caches, and relevant archive workflows. Track completion by data location. A restore process must reapply outstanding deletion records so a restored snapshot does not reintroduce purged data.

Work through a timed-out order write as a production example. First inspect transaction evidence to establish whether the write committed before the timeout. Then check whether the follow-up read went to a lagging replica. A slow query plan can explain the latency, while a durable transaction record and replica replay position explain the inconsistent observations. Each conclusion requires its own evidence.

## Practice and exit gate

- [L1 · Query plan](labs/L1.md)
- [L2 · Isolation](labs/L2.md)
- [L3 · Crash recovery](labs/L3.md)
- [L4 · Schema change](labs/L4.md)
- [Guided · PostgreSQL indexes, WAL and transaction sandbox](projects/guided/README.md)
- [Independent · Transactional order ledger with migrations and recovery](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Explain crash recovery and compare B-trees with LSM trees for point reads and sustained writes.

Continue to [A05 · Scalability, Caching & Performance](../A05-scalability-caching-performance/README.md) when the prerequisite stage gates are met.
