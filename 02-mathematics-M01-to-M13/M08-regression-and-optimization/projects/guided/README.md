# M08 · Guided numerical worksheet

[Module index](../../README.md)

Build a worksheet comparing baseline and regularized fits. Show the residual convention, derive the update, and compare decrease against the initial objective of 9.

## Worksheet

1. Compute MSE for observations [1,3] and predictions [2,3]. Raise the second prediction to 4 and compare the errors.
2. Predict with rows (1,2),(1,3) and weights (1,2). Remove one weight and verify the dimension error.
3. Take one gradient step from zero on (w−3)²+2w² for rates 0.05, 0.1, and 1/6. Replace the last rate with 1 and compare final losses.
4. Fit a through-origin line to x=[1,2], y=[2,4] with squared-error penalty 5w². Remove the penalty and compare the coefficient.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
