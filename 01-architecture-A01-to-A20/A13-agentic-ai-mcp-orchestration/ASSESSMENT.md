# A13 · Applied assessment

Attempt these before reviewing the answers. Pass eight of ten, reproduce all labs and both project suites, then demonstrate one fresh failure diagnosis and a delayed re-test.

1. What is the difference between a model proposal and execution?
2. Does a checkpoint imply a durable external effect?
3. Where should an interrupt occur?
4. Is approval valid after changing the payload?
5. Who is responsible for tool scopes?
6. What should replay reuse?
7. Can a tool's returned text change its privileges?
8. How should parallel budget shares relate to the global budget?
9. What verifies success beyond final text?
10. Does stopping a workflow automatically roll back committed effects?

<details>
<summary>Answers</summary>

1. A proposal is data until trusted application code validates, authorizes and executes it.
2. No. The effect needs its own receipt and reconciliation boundary.
3. Before the first action that depends on approval.
4. No. Obtain approval for the new exact payload.
5. The executor and trusted policy layer.
6. The scoped operation identity and verified outcome when available.
7. No, policy comes from a trusted authority.
8. Their allowed sum plus overhead must fit the global cap.
9. Observed trace, durable effects and the task's outcome criteria.
10. No. Inspect and reconcile or compensate each effect under policy.

</details>
