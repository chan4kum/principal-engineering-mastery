# M03 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Reduce the system by hand, then change the second right-side entry while keeping dependent rows. Distinguish underdetermined and inconsistent by rank.
2. Use a zero first pivot with a swappable row, then submit an incompatible right-hand side. Compare pivoted results to NumPy and explain the shape failure.
3. Sweep diagonal scale from 1 to 0.001, then replace the smallest scale by zero. Tabulate two-norm condition numbers and mark singularity.
4. Fit an intercept and slope on three labeled points, then zero the feature column. Record residual and coefficients or the rank-deficiency failure.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: 'underdetermined'
L1 failure control: 'inconsistent'
L2 normal control: [3.0, 2.0]
L2 failure control: 'invalid'
L3 normal control: [1, 10, 1000]
L3 failure control: [1, 10, 'singular']
L4 normal control: ([1.0, 2.0], 0.0)
L4 failure control: 'invalid'
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. Solve 2x+y=11 and x−y=1.
2. Compute determinant of [[4,2],[1,5]].
3. Classify x+2y=3 and 2x+4y=7.
4. Compute two-norm condition of diag(2,0.02).
5. Find the result shape for a 4×3 by 3×2 matrix product.

<details>
<summary>Answers and rationale</summary>

1. x=4, y=3 by adding the equations.
2. 18 from 4×5−2×1.
3. Inconsistent because doubling the first equation would require 6 on the second right-hand side.
4. 100. Divide the larger singular value by the smaller.
5. 4×2. The shared dimension 3 is summed over.

</details>
