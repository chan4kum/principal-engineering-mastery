# A20 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Identify the workflow requirement in the discovery fixture, then remove it from feature selection. Record the two chosen slices and which one lacks the necessary workflow.
2. Compare complete workflow-plus-recovery scope under five days and four days. Record eligible scope or the budget hold; distinguish work estimates from elapsed time.
3. Remove integration evidence while keeping the release version and outcome observations fixed. Record hold or promotion, and preserve the stable deployment.
4. Monitor a promoted pilot, then introduce enough failed requests to violate the fixture's 99% target. Record baseline restoration and attach the event to the delivery decision.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: ('quick demo', 'verified integration')
L1 failure control: ('failure recovery', 'quick demo')
L2 normal control: ('failure recovery', 'verified integration')
L2 failure control: ()
L3 normal control: (True, 'v2')
L3 failure control: (False, 'v1')
L4 normal control: ('v2', 1)
L4 failure control: ('v1', 2)
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. A pilot reduces time to resolution from 18 to 12 minutes under matching conditions.
2. Two workstreams take 4 and 8 days in parallel, followed by 5 days of integration.
3. A candidate reaches 100 eligible requests with two failures; pilot target is 99% good.
4. A proposed integration reduces setup effort, but nobody owns restoration in the customer environment.
5. Benefit is 240 units, implementation 70 and operations 80.

<details>
<summary>Answers and rationale</summary>

1. 6 minutes absolute and one third relative reduction.
2. 13 days on the critical path if capacity and dependency assumptions hold.
3. 98% good violates the candidate gate.
4. Hold readiness and name accountable restoration owner before promotion.
5. Net benefit 90 units. Simple ROI is 90/150 = 60%.

</details>
