# M01 · Sets and mathematical language

**8 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../../00-stage-0-diagnostic/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [M01.01](lessons/M01.01.md) | number systems | Foundation |
| [M01.02](lessons/M01.02.md) | notation and operators | Foundation |
| [M01.03](lessons/M01.03.md) | membership | Foundation |
| [M01.04](lessons/M01.04.md) | set builder | Foundation |
| [M01.05](lessons/M01.05.md) | union/intersection/complement | Foundation |
| [M01.06](lessons/M01.06.md) | Cartesian products | Foundation |
| [M01.07](lessons/M01.07.md) | functions/domains | Foundation |
| [M01.08](lessons/M01.08.md) | indicator functions | Foundation |

## Guided walkthrough

Start by naming the values an operation accepts. Then use that domain to define sets, construct combinations, and count events without changing the population halfway through a calculation.

### Values, notation, and membership (M01.01–M01.04)

1. **Number systems.** Integers `ℤ` include negative whole numbers, zero, and positive whole numbers. Rationals `ℚ` include ratios of integers with a nonzero denominator. Reals `ℝ` also include irrationals such as `√2`. Complex numbers `ℂ` extend the reals with `i² = −1`. A set is closed under an operation when every allowed pair of inputs gives a result in that set. For example, `3 ÷ 2 = 3/2` shows that division by a nonzero integer can leave `ℤ`.
2. **Notation and operators.** Parentheses specify what an operator acts on. In `−(3²)`, square `3` and then negate to get `−9`. In `(−3)²`, square the negative value to get `9`. Write the grouping explicitly when translating a formula to code, then verify that the language operator has the intended meaning.
3. **Membership and subsets.** `x ∈ A` says `x` is one element of `A`. `B ⊆ A` says every element of `B` belongs to `A`. For `A = {1, 2}`, `1 ∈ A` and `{1} ⊆ A`, while `{1} ∉ A`. The empty set is a subset of every set because it has no element that could violate the condition.
4. **Set-builder notation.** Read `{x ∈ U | P(x)}` as “the elements `x` of `U` for which `P(x)` is true.” With `U = {−3, −2, −1, 0, 1, 2, 3}` and `P(x)` meaning “`x` is even,” the result is `{−2, 0, 2}`. Restricting `U` to the positive candidates changes the answer to `{2}` with the same predicate.

### Set operations, functions, and counts (M01.05–M01.08)

5. **Union, intersection, and complement.** With `U = {0, 1, 2, 3}`, `A = {0, 1}`, and `B = {1, 2}`, the union is `{0, 1, 2}` and the intersection is `{1}`. The complement of the union is `{3}` relative to `U`. De Morgan’s law gives the same result by intersecting the two complements, `{2, 3} ∩ {0, 3} = {3}`.
6. **Cartesian products.** `A × B` contains every ordered pair `(a, b)` with `a ∈ A` and `b ∈ B`. Two model versions and three datasets give `2 × 3 = 6` version–dataset pairs. Pairing by position yields only two pairs and leaves four experiment combinations untested.
7. **Functions and domains.** A function assigns exactly one output to each input in its domain. For `f(x) = 1/x` over nonzero reals, `f(−2) = −0.5` and `f(2) = 0.5`. Zero lies outside the domain. For a composition `g(f(x))`, first check that `x` belongs to the domain of `f`, then that `f(x)` belongs to the domain of `g`.
8. **Indicator functions.** The indicator of a predicate is `1` when it holds and `0` otherwise. For scores `[2, 5, 8]` and an inclusive threshold of `5`, the indicators are `[0, 1, 1]`. Their sum is `2`, the passing count. Divide by `3` for the overall pass rate, or divide `0×2 + 1×5 + 1×8` by `2` for the mean among passing scores. The conditional mean is undefined when there are no passing scores.

### Put it together

Suppose four evaluated records have unique IDs `U = {a, b, c, d}`. The target cohort is `C = {a, b, d}` and the records that pass a model check are `P = {b, c, d}`. The intersection `C ∩ P = {b, d}` gives two passing records in the cohort. The overall rate is `3/4 = 75%`. The cohort rate uses the same outcomes but divides by the size of the cohort, giving `2/3 ≈ 66.7%`. If the cohort is empty, report that its rate is undefined. This keeps the population, predicate, and denominator visible in evaluation code.

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

Continue with [M02 · Logic and proof](../M02-logic-and-proof/README.md) after the applicable gates.
