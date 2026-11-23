# M08 · Regression and optimization

**6 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Choose an objective that matches the prediction, then examine how residuals, gradient steps, features, and penalties change the fit.

1. **M08.01 · linear/logistic regression.** Linear regression predicts a numeric value with w·x + b. Logistic regression maps the same linear score through σ(z)=1/(1+e⁻ᶻ) to a probability. A score of zero gives probability 0.5.
2. **M08.02 · optimization objectives.** An objective ranks candidate parameters. Squared error penalizes large residuals strongly. For errors 1 and 3, mean squared error is (1²+3²)/2 = 5 and mean absolute error is 2.
3. **M08.03 · residuals.** A residual is observed minus predicted under this convention. For observations [1, 3] and predictions [2, 2], residuals [−1, 1] sum to zero and still produce MSE 1.
4. **M08.04 · gradient descent.** Gradient descent moves by −η∇L. For L(w)=(w−3)² and w=0, the derivative is −6. With η=0.25, one step moves to 1.5.
5. **M08.05 · PCA.** PCA can compress correlated inputs before fitting. Fit the centering and directions on training data and apply the same transformation to held-out data. A discarded direction can contain target signal even if it explains little input variance.
6. **M08.06 · regularization.** L2 regularization adds a squared coefficient penalty. Minimizing (w−3)² + 2w² gives derivative 6w−6 and solution w=1. Without the penalty the optimum is w=3.

### Put it together

For the penalized scalar objective, start at zero and take a step with η = 0.1. The new value is 0.6 and the objective falls from 9 to 6.48. A step with η = 1 instead reaches 6 and raises the objective to 81.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

def objective(weight):
    return (weight - 3) ** 2 + 2 * weight ** 2

gradient_at_zero = -6.0
steps = -np.array([0.1, 1.0]) * gradient_at_zero
np.testing.assert_allclose(steps, [0.6, 6.0])
np.testing.assert_allclose(objective(steps), [6.48, 81.0])
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

[Previous · M07 Matrix decompositions and PCA](../M07-matrix-decompositions-and-pca/README.md) · [Next · M09 Calculus and optimization](../M09-calculus-and-optimization/README.md)
