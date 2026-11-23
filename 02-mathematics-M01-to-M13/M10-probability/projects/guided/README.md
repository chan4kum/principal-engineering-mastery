# M10 · Guided numerical worksheet

[Module index](../../README.md)

Build a probability worksheet that keeps the population and conditioning event explicit at each step. Add a prevalence comparison and identify the dataset assumptions needed before applying it to a classifier.

## Worksheet

1. Out of five eligible observations, two satisfy the event. Compute the conditional probability. Remove all eligible observations and identify the invalid denominator.
2. Find the mean and variance of values 0 and 4 with probabilities 0.5 each. Change the second probability to 0.4 and reject the resulting mass assignment.
3. Use a population of ten with 2, 4, or 8 marked items. Compare the two-marked probability with and without replacement at each population composition.
4. Compute positive predictive value at prevalence 1% and 10%, with sensitivity 0.9 and false-positive rate 0.05. Explain why an unchanged classifier can yield different predictive values.

## Acceptance evidence

- Record the derivation, assumptions, and predicted output for each worksheet case.
- Run the [verification notebook](verify.ipynb) in an environment with the math extra. Its eight controls must agree with the verified fixtures.
- Explain the first changed value, rerun the corresponding normal control, and predict and verify one new input of your own.
