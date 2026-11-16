# A18 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Query the mock index with a verified tenant and then request the foreign index name. Record result IDs and each denied path.
2. Increase synthetic output usage by one token so the calculated charge crosses its tenant cap. Record integer tariff units and the quota outcome. These are fixture tariff units.
3. Mark the primary unavailable and vary policy eligibility of the healthy backup. Record the route or safe deferral; explain what a live setup must verify.
4. Replay a metered request, then send mismatched tenant evidence under the same request identity. Record replay, denial and both tenant totals.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: ('own',)
L1 failure control: ()
L2 normal control: 11
L2 failure control: 'quota'
L3 normal control: 'secondary'
L3 failure control: 'deferred'
L4 normal control: ('replay', 10, 0)
L4 failure control: ('denied', 10, 0)
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. Tenant X uses 10 input and 5 output tokens at fixture rates 1 and 3. Tenant Y used 10 units and shared budget is 32.
2. Tenant A requests B's index and it exists. Both tenants have the same document identifier.
3. Two regions are healthy, but neither is in the allowed set.
4. A deployment appears in the model catalog but the workload identity lacks inference access on the configured resource.
5. A shared 84-unit pool is attributed by usage weights 5:2.

<details>
<summary>Answers and rationale</summary>

1. X would cost 25 and reach 35 shared units, so defer if Y's charge already committed.
2. Enforce the verified tenant-to-index mapping and scope lookup and cache identity.
3. Defer. Availability does not grant policy eligibility.
4. Verify actual deployment name, data-plane scope and role. Catalog presence alone is insufficient.
5. Allocate 60 and 24 units, with any accounting exceptions specified separately.

</details>
