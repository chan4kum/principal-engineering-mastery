# M09 · Calculus and optimization

**9 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Move from one-variable derivatives to vectors, matrices, and constraints. Check the shapes of derivatives before using them in an update.

1. **M09.01 · derivatives.** A derivative is the local rate of change. For f(x)=x², the difference quotient is ((x+h)²−x²)/h = 2x+h, so the derivative at x=3 is 6.
2. **M09.02 · chain rule.** The chain rule multiplies derivatives along a composition. For f(x)=(x²+1)³, the inner derivative is 2x and the outer derivative at u=x²+1 is 3u². At x=1 their product is 24.
3. **M09.03 · partials.** A partial derivative varies one coordinate while holding the others fixed. For f(x,y)=x²y, the partial with respect to x is 2xy and the partial with respect to y is x². At (2,3) they are 12 and 4.
4. **M09.04 · gradients.** The gradient collects the partials of a scalar function. For f(x,y)=x²+2y², the gradient is (2x,4y). At (1,1) the first-order change in direction (1,0) per unit distance is 2.
5. **M09.05 · Jacobians.** A Jacobian stacks the derivatives of vector-valued outputs. For F(x,y)=(x+y²,xy), rows are (1,2y) and (y,x). At (2,3) the 2 by 2 Jacobian has rows (1,6) and (3,2).
6. **M09.06 · matrix calculus.** For L(w)=‖Aw−b‖₂²/2, let r=Aw−b. A small change dw gives dr=A·dw and dL=rᵀA·dw, so ∇L=Aᵀr. If A is m by n, the gradient has n entries.
7. **M09.07 · Hessian.** The Hessian collects second partials. For f(x,y)=x²+2xy+3y² it is [[2,2],[2,6]]. The mixed terms couple changes in x and y.
8. **M09.08 · convexity.** A convex function lies below or on the chord between two points. For twice differentiable functions on an open convex domain, a positive semidefinite Hessian characterizes convexity. The Hessian of x²−y² has a negative direction, so this function is not convex on ℝ².
9. **M09.09 · constrained optimization.** For minimizing x²+y² subject to x+y=4, substitute y=4−x. The derivative of x²+(4−x)² is 4x−8, giving x=y=2 and objective 8. Check feasibility as well as the stationary condition.

### Put it together

For a one-feature least-squares model with A = [[1],[2]], b = (1,2), and w = 0, the gradient is −5. A step of size 0.2 reaches w = 1 and zero loss. A step of size 1 jumps to w = 5 and raises loss from 2.5 to 40.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

design = np.array([[1.0], [2.0]])
target = np.array([1.0, 2.0])
start = np.array([0.0])
gradient = design.T @ (design @ start - target)
np.testing.assert_allclose(gradient, [-5.0])
for step_size, expected_loss in [(0.2, 0.0), (1.0, 40.0)]:
    weight = start - step_size * gradient
    residual = design @ weight - target
    np.testing.assert_allclose(0.5 * (residual @ residual), expected_loss)
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

[Previous · M08 Regression and optimization](../M08-regression-and-optimization/README.md) · [Next · M10 Probability](../M10-probability/README.md)
