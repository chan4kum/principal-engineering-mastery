# M11 · Guided numerical worksheet

[Module index](../../README.md)

Build a covariance worksheet that distinguishes marginal variability, dependence, and the variance of an aggregate. Include a deliberate invalid covariance so the report explains the rejected result.

## Worksheet

1. For joint masses [[0.3,0.2],[0.2,0.3]], compute P(X=1|Y=1). Move all of the mass to the Y=0 column and explain why the conditional is undefined.
2. Transform covariance [[1,0.5],[0.5,1]] by the row vector (1,1). Pass a column vector instead and explain the shape mismatch.
3. Sweep the correlation in a unit-variance pair across 0, 0.5, and 1. Replace 1 with 1.2 and show why that candidate cannot be a covariance matrix.
4. Average two prediction errors. Compare the average’s variance with independent unit-variance errors and with correlation 0.8.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
