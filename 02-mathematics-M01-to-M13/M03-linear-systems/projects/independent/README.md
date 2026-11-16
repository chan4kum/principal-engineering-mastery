# M03 · Independent calculation and ML transfer

[Phase index](../../README.md)

Transfer conditioning and rank checks to a fitted line using least squares. Measure residual and reject an ill-defined or ill-conditioned design.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L4](../../labs/L4.md). Record residual and coefficients or the rank-deficiency failure.

Run the verification commands from the linked labs. Inspect the [independent source](independent.py) after predicting the outcome.

Attempt an independent implementation and preserve normal and failure results before consulting the reference. Repeat with a counterexample from a different input family.

Work the [worksheet](WORKSHEET.md), then verify it using the [NumPy notebook](verify.ipynb) in an environment with the math extra.
