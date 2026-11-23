# M09 · Guided numerical worksheet

[Module index](../../README.md)

Build a derivative worksheet tracing the effect of a change through a least-squares loss. State every derivative’s shape, compare the Jacobian action to a directional derivative, and explain why a correct gradient can still produce a worse update.

## Worksheet

1. Expand the forward difference quotient for x² at x=3. Compare h=1/8 with h=1/4 and explain which gives the smaller approximation error.
2. Evaluate the Jacobian of F(x,y)=(x+y²,xy) at (2,3) and apply it to (1,0). Transpose the matrix and identify how the predicted change differs.
3. Find the smallest Hessian eigenvalue of diag(2,c) for c = 1, 0.5, 0.25. Replace the last c with −0.5 and exhibit negative curvature.
4. Use A=[[1],[2]] and b=(1,2) in the quadratic loss ‖Aw−b‖²/2. Take a step from zero with rate 0.2, then compare with rate 1.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
