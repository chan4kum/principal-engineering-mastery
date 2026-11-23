# M07 · Matrix decompositions and PCA

**6 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Use the singular value decomposition to find independent directions, quantify what compression discards, and connect those directions to PCA.

1. **M07.01 · matrix rank.** The rank is the dimension of a matrix’s column space. In [[1, 2], [2, 4]], the second column is twice the first, so the rank is 1. In numerical work, state the tolerance used to decide whether a small singular value counts.
2. **M07.02 · singular values/vectors.** A right singular vector vᵢ maps to σᵢuᵢ, where uᵢ is the matching left singular vector and σᵢ ≥ 0. For diag(4, −2), the singular values are 4 and 2. The negative sign can appear in the left singular direction.
3. **M07.03 · SVD.** The SVD writes A = UΣVᵀ. For a compact decomposition of an m by n matrix with k = min(m, n), U is m by k, Σ is k by k, and Vᵀ is k by n. Multiplication reconstructs the original shape.
4. **M07.04 · low-rank approximation.** Keeping the largest r singular components gives a best rank-r approximation in Frobenius norm. For diag(4, 2, 1), rank one retains 4 and discards 2 and 1, giving error √(2² + 1²) = √5.
5. **M07.05 · compression.** For a dense m by n matrix, storing compact rank-r factors needs r(m + n + 1) scalar values before metadata. A 100 by 80 matrix uses 8,000 values. Rank 5 uses 905 and trades some reconstruction accuracy for that smaller representation.
6. **M07.06 · PCA connection.** For centered samples arranged as rows, the right singular vectors are PCA directions. With n > 1 samples, component i has sample variance σᵢ²/(n − 1). Center first, since an offset can otherwise dominate the direction with the largest magnitude.

### Put it together

A centered matrix with rows (−2, 0), (0, 0), and (2, 0) has one nonzero singular value √8. Its first principal component accounts for sample variance 8/2 = 4. Increase the middle row’s second feature and recenter. The rank becomes two and one component no longer reconstructs all observations.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

samples = np.array([[-2.0, 0], [0, 0], [2, 0]])
singular = np.linalg.svd(samples, compute_uv=False)
np.testing.assert_allclose(singular ** 2 / 2, [4, 0])
samples[1, 1] = 3
centered = samples - samples.mean(axis=0)
assert np.linalg.matrix_rank(centered) == 2
np.testing.assert_allclose(np.linalg.svd(centered, compute_uv=False) ** 2 / 2, [4, 3])
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

[Previous · M06 Projections](../M06-projections/README.md) · [Next · M08 Regression and optimization](../M08-regression-and-optimization/README.md)
