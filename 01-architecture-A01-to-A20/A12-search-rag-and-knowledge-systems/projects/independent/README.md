# Tenant-safe hybrid RAG service with evaluations

Implement revision-aware replace and POST /answer. Authenticate an opaque fixture token and derive the tenant from it. Restrict candidate sets before scoring, return source and revision metadata with exact evidence, abstain when there are no hits, and reject stale updates after a tombstone. Demonstrate no cross-tenant leakage and report evaluation results. The reference returns extracts without a model-generated answer.

Run the acceptance suite after the independent attempt where applicable.

```sh
uv run --locked --extra api pytest -q tests/test_a12_projects.py
```

<details>
<summary>Reference implementation after assessment</summary>

[Reference implementation](service.py)

</details>

Record one observed failure, its cause and the first successful recovery. Document the assumptions and one production trade-off.
