# M01 · Numerical worksheet and NumPy validation

[Phase index](../../README.md)

Derive inclusion–exclusion and finite-set operations by hand, then validate finite universes and masks with NumPy.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L1](../../labs/L1.md). Compare three counts and use inclusion–exclusion to explain changes.
- [L2](../../labs/L2.md). Record the mask-based result and the shape validation failure.
- [L3](../../labs/L3.md). Tabulate the cohort sizes and identify the empty set.

Run the verification commands from the linked labs. Inspect the [guided source](guided.py) after predicting the outcome.

Work the [worksheet](WORKSHEET.md), then verify it using the [NumPy notebook](verify.ipynb) in an environment with the math extra.
