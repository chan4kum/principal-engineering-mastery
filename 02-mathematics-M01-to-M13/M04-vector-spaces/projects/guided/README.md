# M04 · Guided numerical worksheet

[Module index](../../README.md)

Build a worksheet explaining when a candidate coefficient shift is invisible to a model. Derive the shift in L4 and use L1–L3 to distinguish a zero vector, a bad shape, and a genuine null direction.

## Worksheet

1. Compute the Euclidean norm of (3, 4) by hand. Set the second component to zero and recompute it.
2. Multiply (1, 2) by (3, 4) using a dot product. Remove the second component of the right operand and identify the shape error.
3. Sweep the bottom-right entry of [[1, 2], [2, d]] across 4, 5, and 6. Replace the last value with 4 and explain why the last rank drops.
4. Change coefficients from (1, 1) to (−1, 2) on rows (1, 2) and (2, 4). Change only the last feature value to 5 and observe which prediction moves.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
