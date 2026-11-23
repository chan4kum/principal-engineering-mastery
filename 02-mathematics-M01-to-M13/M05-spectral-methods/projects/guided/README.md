# M05 · Guided numerical worksheet

[Module index](../../README.md)

Build a worksheet predicting the stability of a two-coordinate optimizer. Derive each update factor from its Hessian eigenvalue. Use the reconstruction control to show why matching directions and values matters.

## Worksheet

1. For diag(2,3), compute Av−2v with v=(1,0). Add 1 to the second component of v and find the residual.
2. Reconstruct [[2,1],[1,2]] from its symmetric eigenpairs. Reverse the eigenvalues while keeping the eigenvectors in place and measure the Frobenius error.
3. Measure the radii of diag(0.5,−s) for s = 0.5, 0.8, 0.9. Replace 0.9 with 1.2 and identify which matrix can amplify a direction.
4. Apply three gradient steps to a quadratic with Hessian diag(1,3), starting at (1,1). Compare learning rates 0.25 and 1.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
