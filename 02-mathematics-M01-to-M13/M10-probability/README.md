# M10 · Probability

**6 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Fix the sample space and the conditioning event before computing uncertainty. Keep the data-generating assumptions visible.

1. **M10.01 · events/conditional independence.** Conditional probability is P(A∩B)/P(B) when P(B)>0. Conditional independence of A and B given C means P(A∩B|C)=P(A|C)P(B|C). Two independent fair flips stay independent given that a separate fair flip came up heads, but become dependent given that their own results match.
2. **M10.02 · Bayes.** Bayes’ rule reverses the conditioning using the prior and the evidence probability. If prevalence is 1%, sensitivity 90%, and false-positive rate 5%, then P(event|positive)=0.009/(0.009+0.0495)=2/13, about 15.4%.
3. **M10.03 · random variables.** A random variable maps outcomes to numbers. If X counts heads in two fair flips, both HT and TH map to 1, giving P(X=1)=1/2.
4. **M10.04 · discrete/continuous distributions.** A discrete distribution sums masses. A continuous distribution integrates a density. For a uniform draw on [0,1], P(X≤0.25)=0.25 but P(X=0.25)=0.
5. **M10.05 · expected value and variance.** Expectation averages values weighted by probability. Variance is E[(X−E[X])²]. Equal probabilities at 0 and 4 yield mean 2 and variance 4.
6. **M10.06 · sampling.** Sampling with replacement restores the population before each draw. With two red items and one blue item, the chance of drawing red twice is (2/3)²=4/9 with replacement and (2/3)(1/2)=1/3 without it.

### Put it together

Imagine 10,000 cases under the Bayes example. Expect 90 true positives among 100 events and 495 false positives among 9,900 non-events. Recompute with prevalence 10% and the same conditional rates. The positive predictive value rises to 2/3.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

prevalence = np.array([0.01, 0.10])
true_positive = 0.90 * prevalence
false_positive = 0.05 * (1 - prevalence)
np.testing.assert_allclose(true_positive / (true_positive + false_positive), [2 / 13, 2 / 3])
```

## Practice and exit gate

- [L1 · Manual calculation](labs/L1.md)
- [L2 · NumPy verification](labs/L2.md)
- [L3 · Parameter sweep](labs/L3.md)
- [L4 · ML transfer](labs/L4.md)
- [Numerical drills](DRILLS.md)
- [Guided numerical worksheet and notebook](projects/guided/README.md)
- [Independent ML transfer project](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Complete the drills, reproduce all four labs, and provide evidence for both projects. Score at least 80% on fresh assessment cases, diagnose an unfamiliar failure, and repeat the assessment after a delay.

[Previous · M09 Calculus and optimization](../M09-calculus-and-optimization/README.md) · [Next · M11 Joint random variables](../M11-joint-random-variables/README.md)
