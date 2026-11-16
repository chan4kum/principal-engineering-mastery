# M01 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Compute union, intersection and complement sizes before running the code; then change the second subset. Compare three counts and use inclusion–exclusion to explain changes.
2. Pass a vector universe, then a rank-two array with the same entries. Record the mask-based result and the shape validation failure.
3. Sweep lower-bound thresholds across negative, zero and above-domain values. Tabulate the cohort sizes and identify the empty set.
4. Derive a weighted error from the selected cohort, then exclude every observation. Record the ordinary result and explain why a zero-weight denominator is invalid.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: (3, 1, 1)
L1 failure control: (3, 0, 1)
L2 normal control: (2, 1, 1)
L2 failure control: 'invalid'
L3 normal control: [7, 4, 0]
L3 failure control: [4, 3, 0]
L4 normal control: 0.75
L4 failure control: 'invalid'
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. Universe size 21, |A|=8, |B|=9, |A∩B|=3. Find the count in neither set.
2. There are seven accounts and five days. Count all account-day pairs.
3. With threshold 10 inclusive and values 3,10,12, sum the indicators.
4. Find the excluded real input of f(x)=1/(2x−14).
5. Weighted losses 0,1,0 are eligible with weights 2,2,4.

<details>
<summary>Answers and rationale</summary>

1. 7. Union size is 8+9−3=14.
2. 35 ordered pairs.
3. 2, from 10 and 12.
4. 7 makes the denominator zero.
5. Weighted loss 2/8=0.25.

</details>
