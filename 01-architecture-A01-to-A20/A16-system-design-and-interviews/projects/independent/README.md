# A16 · Scalable transaction-critical product design and prototype

[Phase index](../../README.md)

Prototype a booking write with an atomic unique-seat invariant and payload-bound idempotency. The prototype makes no payment calls and uses a single SQLite writer. Compare a regional writer with a leader-per-partition design in the exercise.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L3](../../labs/L3.md). Record same-result replay and conflict. Explain edge behavior on lost acknowledgements.
- [L4](../../labs/L4.md). Defend unique active-seat state and state what must change for multi-region writes.

Run the verification commands from the linked labs. Inspect the [independent source](independent.py) after predicting the outcome.

Attempt an independent implementation and preserve normal and failure results before consulting the reference. Repeat with a counterexample from a different input family.
