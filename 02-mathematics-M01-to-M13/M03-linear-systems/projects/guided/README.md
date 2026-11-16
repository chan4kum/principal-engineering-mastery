# M03 · Numerical worksheet and NumPy validation

[Phase index](../../README.md)

Derive rank and solve small square systems by Gaussian elimination with partial pivoting. Verify with NumPy using matching shapes.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L1](../../labs/L1.md). Distinguish underdetermined and inconsistent by rank.
- [L2](../../labs/L2.md). Compare pivoted results to NumPy and explain the shape failure.
- [L3](../../labs/L3.md). Tabulate two-norm condition numbers and mark singularity.

Run the verification commands from the linked labs. Inspect the [guided source](guided.py) after predicting the outcome.

Work the [worksheet](WORKSHEET.md), then verify it using the [NumPy notebook](verify.ipynb) in an environment with the math extra.
