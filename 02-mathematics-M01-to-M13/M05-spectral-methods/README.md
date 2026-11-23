# M05 · Spectral methods

**5 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Find directions that a linear map scales, then use them to reason about repeated applications and stability.

1. **M05.01 · eigenvalues/eigenvectors.** An eigenvector v is nonzero and satisfies Av = λv. For A = diag(2, 3), the first coordinate direction has eigenvalue 2 and the second has eigenvalue 3.
2. **M05.02 · eigendecomposition.** When A has a full eigenbasis, form V with those eigenvectors as columns and Λ with matching eigenvalues. Then AV = VΛ gives A = VΛV⁻¹. Swapping the columns requires swapping the diagonal entries too.
3. **M05.03 · diagonalization.** Diagonalization changes coordinates so that each direction scales independently. If A = VΛV⁻¹, the middle V⁻¹V factors cancel in repeated products and Aᵏ = VΛᵏV⁻¹. A Jordan block [[1, 1], [0, 1]] has only one independent eigenvector, so it lacks such a diagonalization.
4. **M05.04 · spectral radius.** The spectral radius is max |λ|. For A = diag(0.5, −0.8), it is 0.8. For a fixed finite-dimensional linear iteration xₖ₊₁ = Axₖ, a radius below 1 gives decay to zero. A radius above 1 permits growing initial directions.
5. **M05.05 · symmetric matrices.** Real symmetric matrices have real eigenvalues and an orthonormal eigenbasis. For [[2, 1], [1, 2]], (1, 1) has eigenvalue 3 and (1, −1) has eigenvalue 1. Normalize them by dividing by √2.

### Put it together

Start at (1, 1). After three applications of diag(0.5, −0.8), the result is (0.125, −0.512). Change the second eigenvalue to −1.2 and its coordinate instead reaches −1.728. The sign flips in both cases and only the second grows in magnitude.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

start = np.ones(2)
for eigenvalue, expected in [(-0.8, -0.512), (-1.2, -1.728)]:
    matrix = np.diag([0.5, eigenvalue])
    result = np.linalg.matrix_power(matrix, 3) @ start
    np.testing.assert_allclose(result, [0.125, expected])
```

[Previous · M04 Vector spaces](../M04-vector-spaces/README.md) · [Next · M06 Projections](../M06-projections/README.md)
