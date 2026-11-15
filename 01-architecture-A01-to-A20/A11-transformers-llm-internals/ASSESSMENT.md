# A11 · Applied assessment

Attempt these before reviewing the answers. Pass eight of ten, reproduce all labs and both project suites, then demonstrate one fresh failure diagnosis and a delayed re-test.

1. What shape follows from two heads of width four?
2. What must earlier logits do after a future-only perturbation?
3. Why subtract the maximum before softmax?
4. What does the factor two represent in KV bytes?
5. Are KV heads necessarily query heads?
6. What does TTFT measure?
7. Which tokens are processed again in this baseline?
8. How many 16-token blocks hold 33 tokens?
9. Does four-bit weight storage determine runtime memory?
10. When can higher throughput lower goodput?

<details>
<summary>Answers</summary>

1. Model width eight before other projections.
2. Remain unchanged under correct causal isolation.
3. It avoids overflow without changing normalized probabilities.
4. Stored keys and values.
5. No. Use the actual cache head count.
6. Time from the declared request start to first token.
7. Every available token in the prefix on each decode step.
8. Three, with fifteen unused slots.
9. No. Cache, scales, activations and execution overhead also count.
10. When increased load causes more requests to miss predefined success or latency thresholds.

</details>
