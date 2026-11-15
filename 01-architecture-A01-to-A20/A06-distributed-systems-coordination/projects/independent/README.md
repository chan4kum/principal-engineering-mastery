# Independent project · Idempotent distributed coordinator with fencing

Simulate a resource and several contending workers with one persistent authority. Use a SQLite file for durable state. The reference accepts deterministic time from a trusted simulator.

```text
claim → new monotonic fence → delayed worker attempts effect → transaction checks current fence
                                         → one effect and durable receipt or denial
```

Implement `Coordinator(path)`, `claim(name, owner, now, ttl)`, `apply(name, fence, operation, delta, now)`, and `value(name)`. Each new lease generates a larger positive fence. Active leases deny replacement. Expired and superseded fences deny effects. A valid repeated operation with the same delta returns its original outcome while a different delta causes `Conflict`. Denials use `Denied`. Persist receipt and effect in one transaction. Lease times, effects and IDs are scoped by resource. Keep trusted time monotonically increasing per resource in the exercise.

```sh
P=01-architecture-A01-to-A20/A06-distributed-systems-coordination/projects/independent
A06_COORDINATOR="$P/coordinator.py" uv run pytest -q tests/test_a06_projects.py -k coordinator
```

Show a paused holder rejected after a new claim, valid concurrent replay, and restart that preserves the fence and receipt. Explain what would change if several independent hosts could write the lease database. The exerciser supplies the clock and trusted callers. A production system needs a shared authority, unforgeable client authority, and a storage system that enforces fencing at the effect boundary.

<details>
<summary>Reference implementation for review after the independent gate</summary>

[SQLite reference coordinator](reference_coordinator.py)

</details>
