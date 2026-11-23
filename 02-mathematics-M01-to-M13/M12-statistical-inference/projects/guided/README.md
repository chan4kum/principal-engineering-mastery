# M12 · Guided numerical worksheet

[Module index](../../README.md)

Build a worksheet that separates estimation, interval assumptions, and held-out calibration. Label each denominator and show how changing it affects the reported quantity.

## Worksheet

1. For two successes and one failure in an ordered Bernoulli sequence, evaluate the likelihood at p=0.5. Set p=0 and explain the zero likelihood.
2. Compute sample variance for [2,4,6] using n−1. Use n in its place and explain why the resulting quantity answers a different question.
3. For population standard deviation 5, sweep the 95% normal-interval half-width across sample sizes 25, 100, and 400. Replace 400 with zero and reject the interval.
4. Evaluate calibration for a bin of 100 forecasts with probability 0.8. Change the number of positive outcomes from 80 to 60 and measure the absolute gap.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
