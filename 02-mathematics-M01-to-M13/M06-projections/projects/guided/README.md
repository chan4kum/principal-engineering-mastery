# M06 · Guided numerical worksheet

[Module index](../../README.md)

Build a worksheet comparing an orthogonal projection and a least-squares fit. Compute the constant-fit residual by hand and explain why a zero-length embedding cannot produce a cosine score.

## Worksheet

1. Project (3,1) onto (1,1). Set the direction to zero and identify the division you can no longer perform.
2. Fit a constant to [2,4,6] using a column of three ones. Remove a row of the design and explain why the target no longer matches it.
3. Tabulate squared errors for constants 3, 4, and 5 on [2,4,6]. Replace the last candidate with 6 and compare the result.
4. Compute cosine similarity for (1,0) and (1,1). Replace the query vector with zero and decline to assign a similarity score.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
