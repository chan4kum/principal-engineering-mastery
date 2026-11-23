# M12 · Statistical inference

**7 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Use observed data to estimate a population property. State the sampling model, uncertainty method, and decision rule separately.

1. **M12.01 · likelihood.** Likelihood treats the observed data as fixed and compares parameter values. For two successes and one failure in an ordered sequence of independent Bernoulli trials, L(p)=p²(1−p). It is a function of p and need not integrate to one over p.
2. **M12.02 · maximum likelihood.** The maximum likelihood estimate maximizes that function. For 0<p<1, differentiating 2 log p + log(1−p) gives 2/p−1/(1−p), which vanishes at p=2/3. Since the likelihood is zero at the endpoints and positive inside, this is the maximum.
3. **M12.03 · sample mean and variance.** For [2,4,6] the sample mean is 4. The sum of squared deviations is 8. Dividing by n−1 gives sample variance 4, while dividing by n gives the variance of the empirical distribution, 8/3.
4. **M12.04 · confidence intervals.** A frequentist confidence interval procedure has coverage over repeated samples under its assumptions. For 25 independent normal observations with a sample mean of 10 and a known population standard deviation of 5, a 95% z interval is 10±1.96×5/√25 = [8.04,11.96].
5. **M12.05 · hypothesis tests.** A p-value is the null-model probability of a statistic at least as extreme as observed. A valid p-value of 0.03 falls below a preselected threshold of 0.05. It does not quantify the probability that the null hypothesis is true.
6. **M12.06 · bootstrap.** The ordinary bootstrap resamples observations with replacement and recomputes a statistic. For [2,4,6], resample [2,2,6] to get mean 10/3. Repeat many times for an empirical sampling distribution, or resample blocks or clusters when justified by dependence.
7. **M12.07 · calibration.** A calibrated probabilistic model has observed event frequencies close to the probabilities it assigns among comparable predictions. If 100 cases assigned probability 0.8 yield 60 events, the bin’s observed frequency is 0.6 and its estimated calibration gap is 0.2.

### Put it together

For eight recorded successes in ten independent Bernoulli trials, the likelihood is maximized at p=0.8. That estimate describes the fitted sample. In a separate cohort where 60 of 100 predictions near 0.8 are positive, the 0.2 gap supplies different evidence about calibration.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

probabilities = np.linspace(0, 1, 101)
likelihood = probabilities ** 8 * (1 - probabilities) ** 2
estimate = probabilities[np.argmax(likelihood)]
np.testing.assert_allclose(estimate, 0.8)
np.testing.assert_allclose(abs(estimate - 60 / 100), 0.2)
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

[Previous · M11 Joint random variables](../M11-joint-random-variables/README.md) · [Next · M13 Information theory and deep learning](../M13-information-theory-and-deep-learning/README.md)
