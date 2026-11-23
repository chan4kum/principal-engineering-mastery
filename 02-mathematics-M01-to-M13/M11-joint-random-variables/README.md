# M11 · Joint random variables

**4 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Describe variables together first, then compute what one observation tells you about another.

1. **M11.01 · joint/marginal/conditional distributions.** A joint distribution assigns probabilities to pairs. Summing over one variable gives the other’s marginal. If P(X=1,Y=1)=0.30 and P(Y=1)=0.50, their quotient gives P(X=1|Y=1)=0.60.
2. **M11.02 · covariance/correlation.** Covariance is E[(X−E[X])(Y−E[Y])]. Correlation divides it by both nonzero standard deviations. If X takes −1, 0, and 1 with equal probability and Y=X², their covariance is zero although Y is determined by X.
3. **M11.03 · multivariate Gaussian.** A multivariate Gaussian is specified by a mean vector and covariance matrix. Each linear combination is Gaussian or degenerate. For covariance [[1,0.5],[0.5,1]], the variance of X+Y is 1+1+2×0.5=3.
4. **M11.04 · transformations.** A linear transformation Z=AX+b has mean Aμ+b and covariance AΣAᵀ. For a scalar Y=2X+3 with Var(X)=4, Var(Y)=16 because the shift contributes no variance.

### Put it together

Aggregate two errors with variance 1 each and covariance 0.5. The variance of the sum is 3. Under independence it would be 2, so accounting for covariance changes an uncertainty estimate even when the individual variances stay fixed.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

weights = np.array([1.0, 1.0])
correlated = np.array([[1.0, 0.5], [0.5, 1.0]])
np.testing.assert_allclose(weights @ correlated @ weights, 3.0)
np.testing.assert_allclose(weights @ np.eye(2) @ weights, 2.0)
```

[Previous · M10 Probability](../M10-probability/README.md) · [Next · M12 Statistical inference](../M12-statistical-inference/README.md)
