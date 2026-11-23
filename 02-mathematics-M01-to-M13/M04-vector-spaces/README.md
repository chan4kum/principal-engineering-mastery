# M04 · Vector spaces

**8 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Describe what a set of vectors can represent, how many coordinates it needs, and which input directions a matrix cannot see.

1. **M04.01 · vectors/norms.** The Euclidean norm is √(Σ xᵢ²), the L1 norm is Σ |xᵢ|, and the maximum norm is max |xᵢ|. For (3, 4) those values are 5, 7, and 4.
2. **M04.02 · dot products.** The dot product sums coordinate products. (1, 2) · (3, 4) = 1×3 + 2×4 = 11. For two nonzero vectors, dividing the dot product by both Euclidean norms gives the cosine of their angle.
3. **M04.03 · spans.** The span consists of all linear combinations of the given vectors. The span of (1, 2) is the line {(t, 2t) | t is real}. Adding (0, 1) expands it to the plane.
4. **M04.04 · independence.** Vectors are independent when a combination equals zero only with all coefficients zero. Vectors u = (1, 2) and v = (2, 4) are dependent because 2u − v = 0.
5. **M04.05 · basis.** A basis is independent and spans the space. The vectors (1, 1) and (1, −1) form a basis for ℝ². The vector (3, 1) has coordinates (2, 1) in this basis.
6. **M04.06 · dimension.** The dimension is the number of vectors in any basis. The plane z = 0 in ℝ³ has dimension 2 because every point uses two independent directions, (1, 0, 0) and (0, 1, 0).
7. **M04.07 · null and column spaces.** The null space is the set of inputs with Ax = 0. The column space is the span of possible outputs. For A = [[1, 2], [2, 4]], the null space is spanned by (−2, 1) and the column space by (1, 2).
8. **M04.08 · orthogonality.** Two vectors are orthogonal if their inner product is zero. In the ordinary dot product, (2, 1) · (1, −2) = 0. Nonzero orthogonal vectors are independent.

### Put it together

Two features with one column exactly twice the other supply one independent feature direction. The coefficient vector can move along (−2, 1) without changing predictions. Verify this on a rank-one matrix, then change one entry and confirm that the null direction and rank change.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

matrix = np.array([[1, 2], [2, 4]])
direction = np.array([-2, 1])
np.testing.assert_array_equal(matrix @ direction, [0, 0])
assert np.linalg.matrix_rank(matrix) == 1
matrix[1, 1] = 5
np.testing.assert_array_equal(matrix @ direction, [0, 1])
assert np.linalg.matrix_rank(matrix) == 2
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

[Previous · M03 Linear systems](../M03-linear-systems/README.md) · [Next · M05 Spectral methods](../M05-spectral-methods/README.md)
