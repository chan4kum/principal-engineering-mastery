# A06 · Applied assessment

Pass at least eight of ten, reproduce the four labs and both projects, diagnose a new failure, and re-check with changed inputs after a delay.

1. A writer times out after sending. Name two possible outcomes at the server.
2. Five nodes split into groups of two and three. Which can form an ordinary majority?
3. What does safety require during a minority partition?
4. A receiver has Lamport counter 5 and sees timestamp 9. Calculate its receive timestamp.
5. Are vectors [2,1] and [1,2] comparable?
6. For N=5, can R=2 and W=3 avoid overlapping?
7. A Raft candidate has last term 5/index 10 and a voter has last term 4/index 90. Which is more up to date under the comparison?
8. A resource saw fence 15 and now receives a delayed write at fence 14. What should it do?
9. A client repeats an operation under the same identity after losing a reply. What records should be committed atomically?
10. A completed write of 1 precedes an ordinary read returning the register's initial value 0 with no intervening write. Is that history linearizable?

<details>
<summary>Answers</summary>

1. It may never commit, or it may commit and lose the response.
2. The three-node component.
3. It must prevent invalid commits, even if doing so suspends progress.
4. 10.
5. No. Each exceeds the other in one dimension.
6. Yes. Two and three can be disjoint in five. They do not guarantee intersection.
7. The candidate with last term 5.
8. Reject it at the effect boundary.
9. The effect, scoped operation identity and original outcome.
10. No. Nonoverlap forces the read after the write.

</details>

Draw replicas before, during and after a partition. Mark unknown client outcomes, which side may commit, and where stale writes are rejected. Explain whether the system preserves safety during the fault and what assumptions let it make progress after the fault clears.

**Principal interview.** Why can a Redis lock without fencing be insufficient for correctness-critical operations? Trace a task paused beyond expiry, its replacement writing, and the first task resuming. The resource can reject a stale request only if it enforces successor authority or an equivalent invariant.

**Exit trace.** Draw one Raft term before and after a leader crash. Label the log entries that have quorum replication and satisfy the current-term rule. Compare candidate freshness in the next term and state why a correct leader cannot discard a committed entry.
