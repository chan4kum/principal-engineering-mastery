# M02 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Compute the implication truth table and compare it with the converse. Name the row where they disagree.
2. Use a square relation matrix, then flatten it and observe which axis meaning is lost. Record both quantifier results or shape error.
3. Change one row of a two-row one-column relation from true to false. Give counterexample and compare the two orders of quantifiers.
4. Check a running prediction-count invariant, then introduce a score outside the probability domain. Record prefix counts and range validation.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: [1, 1, 0, 1]
L1 failure control: [1, 0, 1, 1]
L2 normal control: (True, False)
L2 failure control: 'invalid'
L3 normal control: (True, True)
L3 failure control: (False, False)
L4 normal control: [0, 1, 2]
L4 failure control: 'invalid'
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. Evaluate P⇒Q with P=false and Q=true, then evaluate the converse.
2. Negate the statement 'every release has at least one reviewed artifact'.
3. The relation x=y is defined over x and y both in {2,3,4}. Does one shared witness y satisfy all x?
4. At the beginning of step i, a counter stores the successes in indices 0 through i−1. How is it preserved?
5. The base case holds at n=2 and induction proves n→n+1 for n≥2. Does this prove n=1?

<details>
<summary>Answers and rationale</summary>

1. True then false.
2. There exists a release for which no artifact is reviewed.
3. No. Individual witnesses exist, but one y cannot equal three distinct elements.
4. Add the success indicator at i and advance i.
5. No. The induction domain starts at 2.

</details>
