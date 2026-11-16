# A17 · Auditable human-approved healthcare/energy copilot

[Phase index](../../README.md)

Bind a fictional administrative effect to the intended evidence, a distinct authorized reviewer and an unexpired exact digest. Use a local hash chain with a trusted head to detect changed audit rows. Unanchored histories can be rewritten.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L2](../../labs/L2.md). Record decision and effect count.
- [L3](../../labs/L3.md). Record denial and propose a fresh-review procedure.
- [L4](../../labs/L4.md). Record whether the chain verifies and how many effects were committed.

Run the verification commands from the linked labs. Inspect the [independent source](independent.py) after predicting the outcome.

Attempt an independent implementation and preserve normal and failure results before consulting the reference. Repeat with a counterexample from a different input family.
