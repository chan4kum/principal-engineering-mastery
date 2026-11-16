# A16 applied assessment

Close the reference solutions. Predict results, then reproduce the changed-input controls with one previously unseen value.

1. Start from create/resolve requirements, then change the requested mapping key to a missing value. Record resolved or missing result and decide an HTTP mapping with a cache policy.
2. Compute 86,400 records/day with 100 B records, two days, and either one or three copies. Compare average requests per second and storage bytes; state omitted index and peak factors.
3. Repeat a seat reservation with identical request identity, then change its payload. Record same-result replay and conflict. Explain edge behavior on lost acknowledgements.
4. Trace two reservation requests against different seats and then against the same seat. Defend unique active-seat state and state what must change for multi-region writes.

<details>
<summary>Fixture answer key</summary>

```text
L1 normal control: 'https://example.test/item'
L1 failure control: None
L2 normal control: (1.0, 51840000)
L2 failure control: (1.0, 17280000)
L3 normal control: 'same result'
L3 failure control: 'idempotency conflict'
L4 normal control: True
L4 failure control: False
```

</details>

## Fresh applied cases

Attempt all five without opening the feedback. Score one point per correct result with reasoning. Four points meet the 80% threshold. Use different values or a different scenario for your delayed retest.

1. 6,912,000 requests arrive per day with peak factor 5.
2. 500,000 records, 250 B each, three copies, without indexes.
3. A repeated request uses the same key with a different seat.
4. Three serial services have isolated throughput of 550, 240 and 700 requests/s.
5. A hot feed publisher has 40,000 followers and produces 3 posts in a minute.

<details>
<summary>Answers and rationale</summary>

1. 80 requests/s average and 400 requests/s peak.
2. 375,000,000 B decimal. List index, allocator and log costs separately.
3. Return a conflict without performing a second booking.
4. Nominal throughput is capped at 240 requests/s, before shared constraints.
5. Write fanout can create 120,000 entries in that minute. Compare deferred or hybrid fanout against read latency.

</details>
