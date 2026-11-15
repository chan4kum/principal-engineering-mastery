# Guided project · Replicated log and quorum simulator

```text
fixed leader append → copy to reachable voters → majority threshold → committed prefix
```

```sh
LAB=01-architecture-A01-to-A20/A06-distributed-systems-coordination/labs
uv run python "$LAB/coordination.py" guided
uv run pytest -q tests/test_a06_projects.py -k guided
```

Predict the leader's private length and commit length for an isolated leader, a restored majority, and a later second entry during another outage. Verify the committed prefix never shrinks when reachability changes. Restore one follower and verify both values become visible. Sketch the cost of copying a prefix at every synchronization versus replicating suffixes with index and term checks. The implementation has a fixed leader and membership. It is a quorum exercise with no election, arbitrary log loss or split-brain failover.
