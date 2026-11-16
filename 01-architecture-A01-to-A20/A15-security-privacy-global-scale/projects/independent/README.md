# A15 · DevSecOps secured multi-tenant AI service

[Phase index](../../README.md)

Guard tenant-specific reads and exercise digest-pinned artifact approval using a local inventory and review fixture. The examples represent policy controls for a local service, with no externally reachable endpoint.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L3](../../labs/L3.md). Record the release decision and the evidence required to admit.
- [L4](../../labs/L4.md). Record both result sets and explain why denial occurs before retrieval.

Run the verification commands from the linked labs. Inspect the [independent source](independent.py) after predicting the outcome.

Attempt an independent implementation and preserve normal and failure results before consulting the reference. Repeat with a counterexample from a different input family.
