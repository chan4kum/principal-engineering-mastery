# M07 · Guided numerical worksheet

[Module index](../../README.md)

Build a worksheet comparing rank, storage, and residual error. Show how the largest uncentered singular value can come from a constant feature rather than sample variance.

## Worksheet

1. Find the rank of [[1,2],[2,4]]. Change the bottom-right entry to 5 and verify it by a determinant.
2. Reconstruct diag(4,2,1) from an SVD. Omit the singular value 2 and measure the Frobenius error.
3. Tabulate the tail error for ranks 0, 1, 2, and 3 of diag(4,2,1). Reuse rank 1 in place of rank 2 and identify the repeated error.
4. Find PCA variances for the rows (10,−1),(10,0),(10,1). Omit centering and identify the spurious contribution from the constant feature.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
