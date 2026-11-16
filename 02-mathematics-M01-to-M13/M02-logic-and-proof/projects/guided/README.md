# M02 · Numerical worksheet and NumPy validation

[Phase index](../../README.md)

Write truth tables and evaluate quantified predicates on a finite relation before comparing the NumPy result.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L1](../../labs/L1.md). Name the row where they disagree.
- [L2](../../labs/L2.md). Record both quantifier results or shape error.
- [L3](../../labs/L3.md). Give counterexample and compare the two orders of quantifiers.

Run the verification commands from the linked labs. Inspect the [guided source](guided.py) after predicting the outcome.

Work the [worksheet](WORKSHEET.md), then verify it using the [NumPy notebook](verify.ipynb) in an environment with the math extra.
