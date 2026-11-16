# A14 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Change one recorded answer while freezing case membership and expected labels. Record answer passes and name the failed case.
2. Increase the input context while holding output and attributed retrieval tokens fixed. Record total metered units and show why the retrieval subset is not billed twice.
3. Compare two immutable prompt releases under the same two case IDs, then restore stable. Record admission, live prompt identity and restored identity.
4. Change the recorded refusal response's scope to a foreign synthetic tenant. Record the scope veto and retained baseline. The fixture uses no live model or privileged tool.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: 2
L1 failure control: 1
L2 normal control: 51
L2 failure control: 71
L3 normal control: (True, 'p2', 'p1')
L3 failure control: (False, 'p1', 'p1')
L4 normal control: (True, 'p2', 'p1')
L4 failure control: (False, 'p1', 'p1')
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. Only 18 of 20 expected cases ran, and all observed cases passed.
2. A request reports 800 input tokens including 330 retrieved tokens plus 60 output. Use rates 1 and 4.
3. A release passes 19 of 20 cases; the failure is a mandatory tenant-isolation veto.
4. First output arrives at 110 ms, then two more at 160 and 230 ms.
5. Of 12 judge-positive cases, 8 are accepted by the human reviewer. Another 3 human positives were missed.

<details>
<summary>Answers and rationale</summary>

1. Hold. The expected-case contract failed despite a perfect observed rate.
2. 1,040 fixture units. The retrieved subset is already included in input.
3. Hold the release even though 95% passes.
4. Time to first token is 110 ms and largest later gap is 70 ms.
5. Precision is 8/12 and recall is 8/11. Choose a threshold using cost of the two error directions.

</details>
