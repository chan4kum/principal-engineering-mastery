# A04 · Applied assessment

Attempt the questions before revealing the answers. Pass at least eight and repeat with fresh inputs after a delay.

1. A page has 4096 B, a 32 B header, and stored records of 128 B each including slots. How many records fit?
2. Which constraint rejects an order for a nonexistent customer?
3. Why might an indexed Boolean predicate matching 99% of the rows use a sequential scan?
4. Two decrements use a stale input of 5 each. What erroneous quantity can remain?
5. Which PostgreSQL isolation level uses a new snapshot for each ordinary statement?
6. Which wait graph structure indicates a deadlock, and what must a safe retry restart?
7. Which markers survive crash recovery when one transaction committed and one did not, assuming durable settings and intact storage?
8. Why can a replica that replayed an accidental deletion be insufficient for historical recovery?
9. If a storage device writes 480 MiB for 120 MiB of user writes, calculate amplification.
10. Compare B-tree and LSM access for a point read and sustained ingestion.

<details>
<summary>Answers</summary>

1. 31, from floor((4096−32)/128).
2. A foreign key.
3. The index can add scattered heap access to an otherwise almost-complete table scan.
4. 4 instead of 3.
5. Read Committed.
6. A directed cycle. Restart the aborted transaction, including all reads and checks.
7. The committed marker. Uncommitted changes are not visible after recovery.
8. It can mirror the mistake. A compatible base backup and a contiguous archived WAL chain can reconstruct an earlier target.
9. 4×.
10. A B-tree can traverse few pages for a point read and pay for scattered updates. An LSM can batch writes and pay for compaction and multi-run probes. Cache, filters and workload determine the actual outcome.

</details>

## Source scenario

The database commits an order but a search index update fails. Design an outbox row written in the same transaction, an at-least-once publisher and a deduplicating index consumer. Trace publisher failure after delivering the event and before recording its acknowledgment. Check how reconciliation converges on the source of truth.

**Principal interview.** Explain why crash recovery with WAL still requires independently recoverable backups and a separate failure domain when replication is needed.
