# A17 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Triage a synthetic administrative request with a known source and then without that source. Record the state and why review and evidence are distinct.
2. Compare exact digest-bound review with approval of a different revision. Record decision and effect count.
3. Advance the fixture clock past approval validity while keeping all other inputs fixed. Record denial and propose a fresh-review procedure.
4. Run the authorized request twice, then modify one local audit event and check against the prior anchor. Record whether the chain verifies and how many effects were committed.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: 'needs review'
L1 failure control: 'needs evidence'
L2 normal control: (True, 1)
L2 failure control: (False, 0)
L3 normal control: (True, 1)
L3 failure control: (False, 0)
L4 normal control: (True, 1)
L4 failure control: (False, 1)
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. A synthetic administrative proposal changes its source version after a reviewer authorizes the previous version.
2. One audit row is removed, then the remaining hashes are recomputed.
3. Three required recipients received a deletion event, but one has no confirmation.
4. A user tested the system successfully, but the applicable downstream use is unclassified.
5. A reviewer owner approves their own request within the duration window.

<details>
<summary>Answers and rationale</summary>

1. Revalidate source and require fresh exact-digest approval.
2. An independent trusted head or comparable external evidence still fails; self-validation alone cannot establish history.
3. Keep one unresolved target and verify after recovery or restore.
4. Escalate intended use and classification review. A successful task test cannot establish applicability.
5. Deny per the exercise's separation rule and record evidence of the decision.

</details>
