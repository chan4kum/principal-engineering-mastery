# Independent project · Reproducible feature-to-model ML pipeline

Implement `train(rows, split, file)` and `predict(file, features)`. Rows are time-ordered [feature, target] pairs. Fit preprocessing and model only on the prefix before the split. Serialize format version, split, training-data digest, transform statistics and coefficients. Reopening the artifact must yield the same predictions. Reject invalid input. Holdout changes must not alter the training artifact.

```text
versioned rows → temporal split → train-only scaler + model → JSON artifact → predict
```

Run `A10_PIPELINE=path/to/your/pipeline.py uv run --locked --extra math pytest -q tests/test_a10_projects.py -k pipeline`. Include split rationale, data identity, one intentionally leaking control and an offline quality result. Set a promotion gate and a rollback action.

<details>
<summary>Reference for after assessment</summary>

[Pipeline and serialization](pipeline.py)

</details>
