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

## Practice and exit gate

- [L1 · Query plan](labs/L1.md)
- [L2 · Isolation](labs/L2.md)
- [L3 · Crash recovery](labs/L3.md)
- [L4 · Schema change](labs/L4.md)
- [Guided · PostgreSQL indexes, WAL and transaction sandbox](projects/guided/README.md)
- [Independent · Transactional order ledger with migrations and recovery](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Explain crash recovery and compare B-trees with LSM trees for point reads and sustained writes.
