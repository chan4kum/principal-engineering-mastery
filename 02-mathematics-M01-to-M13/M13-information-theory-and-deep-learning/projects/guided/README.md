# M13 · Guided numerical worksheet

[Module index](../../README.md)

Build a worksheet tracing values from logits to loss and from loss to a parameter update. Verify a stable softmax calculation and show a case where a correct gradient with too large a step increases the loss.

## Worksheet

1. Calculate cross entropy in bits when the true class has assigned probability 0.25. Change that probability to zero and characterize the loss.
2. Calculate softmax for logits (1000,1000) after subtracting the maximum. Omit the shift and observe how exponential overflow affects the result.
3. Starting at w=1, apply three gradient updates to w²/2 for rates 0.5, 1, and 1.5. Replace 1.5 with 2.5 and compare the magnitude after three steps.
4. Backpropagate through y=wx for initial w=2, x=3, and target 1. Compare one step at rates 0.1 and 0.25 by measuring the new half-squared loss.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
