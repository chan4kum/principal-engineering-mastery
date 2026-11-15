# Numerical attention and tiny GPT

Implement a single-head causal attention function, show the mask order, and derive both one-token and two-token outputs by hand. Train the model on the fixed next-token sequence and record the loss reduction. Use the future-token perturbation test to demonstrate causality.

Run the acceptance suite after the independent attempt where applicable.

```sh
uv run --locked --extra transformer --extra api pytest -q tests/test_a11_projects.py
```

[Reference implementation](tiny.py)

Record one observed failure, its cause and the first successful recovery. Document the assumptions and one production trade-off.
