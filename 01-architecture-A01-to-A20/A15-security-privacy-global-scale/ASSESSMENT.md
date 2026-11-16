# A15 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Diagram client → credential boundary → tenant retrieval → protected records. Remove one mapped mitigation. Record the uncovered trust flow and propose its control owner.
2. Stage the new fixture credential, probe both versions, then retire the previous version. Record accepted versions and the consequence of leaving overlap enabled.
3. Compare the pinned digest and inventory to reviewed scan evidence. Mark one finding unresolved. Record the release decision and the evidence required to admit.
4. Make a request with a granted local principal, then set the requested scope to a foreign fixture tenant. Record both result sets and explain why denial occurs before retrieval.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: []
L1 failure control: ['retrieval']
L2 normal control: (False, True)
L2 failure control: (True, True)
L3 normal control: True
L3 failure control: False
L4 normal control: ('local-a',)
L4 failure control: ()
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. A valid issuer-signed token targets billing while requested scope is support.
2. A protected tenant store partitions by tenant and record ID, but the result cache uses record ID only.
3. Replica lag is 7 minutes, observed restoration 22 minutes, RPO 5 minutes and RTO 30 minutes.
4. A correct digest matches while the inventory is missing.
5. Rotation revoked the old writer, but archived records reference the previous key version.

<details>
<summary>Answers and rationale</summary>

1. Deny at the identity boundary because audience does not match.
2. Scope the cache key and verify foreign data never enters either read path.
3. RPO fails and RTO passes. The time to restore and tolerated data loss are separate.
4. Do not release. Identity and inventory cover different security properties.
5. Keep controlled decrypt for still-needed versions until records are migrated or eligible for expiry.

</details>
