# M02 · Logic and proof

**8 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../M01-sets-and-mathematical-language/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [M02.01](lessons/M02.01.md) | propositions | Foundation |
| [M02.02](lessons/M02.02.md) | predicates | Foundation |
| [M02.03](lessons/M02.03.md) | truth tables | Foundation |
| [M02.04](lessons/M02.04.md) | conditional/contrapositive | Foundation |
| [M02.05](lessons/M02.05.md) | quantifiers | Foundation |
| [M02.06](lessons/M02.06.md) | Boolean algebra | Foundation |
| [M02.07](lessons/M02.07.md) | proof by contradiction | Foundation |
| [M02.08](lessons/M02.08.md) | induction and invariants | Foundation |

## Guided walkthrough

Turn a condition into a statement you can test, then show why it remains true as the program runs.

1. **[M02.01 · propositions](lessons/M02.01.md).** A proposition has a truth value. “Seven is odd” is true. “x is odd” needs a value for x before it becomes a proposition.
2. **[M02.02 · predicates](lessons/M02.02.md).** A predicate maps inputs in a domain to truth values. The predicate x mod 2 = 0 selects 2 and 4 from {1, 2, 3, 4}.
3. **[M02.03 · truth tables](lessons/M02.03.md).** A truth table enumerates assignments. Two Boolean inputs give four rows. A AND B is true only on the row where both inputs are true.
4. **[M02.04 · conditional/contrapositive](lessons/M02.04.md).** A → B fails only if A is true and B false. Its contrapositive ¬B → ¬A has the same truth table. “Divisible by four implies even” and “odd implies not divisible by four” are equivalent. Reversing the original implication fails at 6.
5. **[M02.05 · quantifiers](lessons/M02.05.md).** Quantifier order controls what can depend on an input. Over the integers, ∀x ∃y (y > x) holds by taking y = x + 1. The reversed order asks for one integer larger than every integer and fails.
6. **[M02.06 · Boolean algebra](lessons/M02.06.md).** De Morgan’s laws distribute negation by swapping AND and OR. For example, ¬(A AND B) = ¬A OR ¬B, so access denied means at least one required condition failed.
7. **[M02.07 · proof by contradiction](lessons/M02.07.md).** To derive a contradiction, assume the claim’s negation and derive an impossibility. If a greatest integer n existed, n + 1 would be an integer greater than n, contradicting maximality.
8. **[M02.08 · induction and invariants](lessons/M02.08.md).** An induction proof establishes a base case and shows how one true case implies the next. For a running sum, the invariant is that after i elements the accumulator equals their sum. The empty prefix starts at zero, and adding the next element establishes the invariant for i + 1.

### Put it together

For a data importer, state the invariant “after processing i records, each accepted record appears exactly once.” Check the base case, test the duplicate branch, and show that the accepted and rejected branches preserve the invariant. A normal input alone cannot establish that the duplicate branch is correct.


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

Continue with [M03 · Linear systems](../M03-linear-systems/README.md) after the applicable gates.
