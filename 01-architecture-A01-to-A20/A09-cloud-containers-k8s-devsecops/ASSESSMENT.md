# A09 · Applied assessment

1. Why can a container see eight CPU IDs with a quota of 0.25 CPU?
2. Does restarting a container automatically retain files in its writable layer across replacement?
3. How does a digest differ from a tag?
4. What makes a Service reachable when Pods are ready?
5. Which layer enforces NetworkPolicy?
6. What does a PDB protect, and which failures can bypass it?
7. Why can HPA increase Pods without restoring throughput?
8. Distinguish admission, scheduling, startup and readiness evidence.
9. At 4 replicas and utilization 80% with target 50%, calculate the modeled HPA target.
10. Which permissions belong in a short-lived workload identity instead of a node-wide credential?

<details>
<summary>Answers</summary>

1. Namespace and CPU visibility are separate from cgroup quota.
2. No. Use storage with a separate lifecycle where persistence is required.
3. A digest identifies immutable content; a tag can be reassigned.
4. Correct selectors and eligible endpoints, DNS, and an allowed data plane.
5. A supporting network plugin.
6. Some voluntary evictions. Node failures and direct deletion are separate cases.
7. A downstream resource or node placement limits the path.
8. Admission accepts the object; scheduling assigns a node; startup launches the process; readiness controls traffic eligibility.
9. Seven before stabilization and policy.
10. Only resource actions required by the workload, scoped to its identity.

</details>

Pass eight of ten on fresh inputs, reproduce all four labs and both projects, and explain one unfamiliar failed rollout or connectivity path.
