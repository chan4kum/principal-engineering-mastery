# A16 · URL shortener from one machine

[Phase index](../../README.md)

Persist create/resolve mappings on one machine with SQLite. Evaluate QPS, three-copy storage and the exclusion of index/build overhead.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L1](../../labs/L1.md). Record resolved or missing result and decide an HTTP mapping with a cache policy.
- [L2](../../labs/L2.md). Compare average requests per second and storage bytes; state omitted index and peak factors.

Run the verification commands from the linked labs. Inspect the [guided source](guided.py) after predicting the outcome.
