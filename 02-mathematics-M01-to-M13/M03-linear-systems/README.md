# M03 · Linear systems

**7 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../M02-logic-and-proof/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [M03.01](lessons/M03.01.md) | matrices as linear maps | Foundation |
| [M03.02](lessons/M03.02.md) | simultaneous equations | Foundation |
| [M03.03](lessons/M03.03.md) | Gaussian elimination | Foundation |
| [M03.04](lessons/M03.04.md) | row rank | Foundation |
| [M03.05](lessons/M03.05.md) | determinants | Foundation |
| [M03.06](lessons/M03.06.md) | singularity | Foundation |
| [M03.07](lessons/M03.07.md) | inverse and conditioning | Foundation |

## Guided walkthrough

Represent constraints as a matrix equation, then distinguish whether a solution exists from whether a numerical answer is reliable.

1. **[M03.01 · matrices as linear maps](lessons/M03.01.md).** For A = [[2, 1], [0, 3]] and x = (1, 2), the dot products with the rows give Ax = (4, 6). Equivalently, x chooses one copy of the first column and two copies of the second.
2. **[M03.02 · simultaneous equations](lessons/M03.02.md).** The equations x + y = 3 and x − y = 1 meet at (2, 1). Substitution verifies both. Equal left-hand sides with different right-hand sides give incompatible constraints.
3. **[M03.03 · Gaussian elimination](lessons/M03.03.md).** Elimination uses row swaps, nonzero scaling, and row addition to preserve the solution set. Subtract the first row from the second in [[1, 1 | 3], [1, −1 | 1]] to obtain [0, −2 | −2]. Back-substitution gives y = 1 and x = 2.
4. **[M03.04 · row rank](lessons/M03.04.md).** The row rank is the number of independent rows, equivalently the number of pivots. In [[1, 2], [2, 4]], row two is twice row one, so the rank is 1.
5. **[M03.05 · determinants](lessons/M03.05.md).** The determinant of [[a, b], [c, d]] is ad − bc. For [[2, 1], [0, 3]] it is 6, the factor by which this map scales oriented area.
6. **[M03.06 · singularity](lessons/M03.06.md).** A singular square matrix has a nonzero null vector and no inverse. The rows of [[1, 2], [2, 4]] both send (−2, 1) to zero. A compatible right-hand side then gives infinitely many solutions, while an incompatible one gives none.
7. **[M03.07 · inverse and conditioning](lessons/M03.07.md).** Use a linear solve for Ax = b. The condition number κ₂(A) = σmax/σmin measures worst-case relative sensitivity. For diag(1, 0.001), κ₂ = 1000. A 0.001 perturbation to the second coordinate of b changes the second coordinate of x by 1.

### Put it together

With A = diag(1, 0.001), solve once for b = (1, 0) and once for b = (1, 0.001). The solutions are (1, 0) and (1, 1). Both have zero residual in exact arithmetic. Compare the input change with the solution change to see why a small residual alone does not establish that the input was well-conditioned.


## Practice and exit gate

- [L1 · Manual calculation](labs/L1.md)
- [L2 · NumPy verification](labs/L2.md)
- [L3 · Parameter sweep](labs/L3.md)
- [L4 · ML transfer](labs/L4.md)
- [Numerical worksheet and NumPy validation](projects/guided/README.md)
- [Independent calculation and ML transfer](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)
- Use the numerical problem set after each lesson, before opening solution feedback.

Score at least 80% on fresh cases, reproduce four labs, meet both project acceptance criteria, diagnose one unfamiliar failure, and repeat the assessment after a delay.

Continue with [M04 · Vector spaces](../M04-vector-spaces/README.md).
