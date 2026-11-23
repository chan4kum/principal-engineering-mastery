# M06 · Projections

**6 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Break a vector into a component within a space and an orthogonal remainder. That same operation finds a least-squares fit.

1. **M06.01 · inner products.** A real inner product is symmetric, bilinear, and positive definite. A weighted example is ⟨x, y⟩ = 2x₁y₁ + x₂y₂. It gives ⟨(1, 2), (3, 4)⟩ = 14, so geometry depends on the inner product used.
2. **M06.02 · projection.** Project x onto a nonzero vector v by multiplying v by (x·v)/(v·v). For x = (3, 1) and v = (1, 1), the projection is (2, 2), leaving residual (1, −1) orthogonal to v.
3. **M06.03 · least squares.** Least squares minimizes ‖Ax − b‖₂². At a minimum the residual b − Ax is orthogonal to the columns of A. To fit one constant to [2, 4, 6], solve 3c = 12 and obtain c = 4.
4. **M06.04 · orthonormal bases.** An orthonormal basis has unit vectors with pairwise zero inner products. With columns assembled into Q, the coordinates of x along those vectors are Qᵀx and the projection is QQᵀx.
5. **M06.05 · Gram-Schmidt.** Gram–Schmidt subtracts the existing projections before normalizing. Starting with (1, 0) and (1, 1), subtract (1, 0) from the second vector to obtain (0, 1). A zero remainder signals dependence. For numerical work, QR routines can handle round-off more reliably than a naive implementation.
6. **M06.06 · cosine similarity.** Cosine similarity divides the dot product by both norms. (1, 0) and (1, 1) give 1/√2. The value is undefined when either vector is zero.

### Put it together

Fit a constant to [2, 4, 6]. Its residuals are [−2, 0, 2], sum to zero, and have squared error 8. Force the constant to 3 and the squared error rises to 11.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

observations = np.array([2.0, 4.0, 6.0])
design = np.ones((3, 1))
coefficients, *_ = np.linalg.lstsq(design, observations, rcond=None)
np.testing.assert_allclose(coefficients, [4.0])
residual = observations - design @ coefficients
np.testing.assert_allclose(design.T @ residual, [0], atol=1e-12)
np.testing.assert_allclose(residual @ residual, 8.0)
assert np.sum((observations - 3) ** 2) == 11
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

[Previous · M05 Spectral methods](../M05-spectral-methods/README.md) · [Next · M07 Matrix decompositions and PCA](../M07-matrix-decompositions-and-pca/README.md)
