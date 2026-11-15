# Guided project · Linear and logistic regression from scratch

Start with [the two-objective implementation](regression.py). Derive both gradients as a design transpose multiplied by the appropriate residual: raw prediction minus observed response for squared error, and sigmoid probability minus label for logistic loss.

Run `uv run --locked --extra math pytest -q tests/test_a10_projects.py -k guided`. Verify an analytical gradient with centered finite differences, then fit the supplied synthetic linear and binary datasets. Record loss reduction, coefficients, and decision-threshold behavior. Compare wrong-sign descent with the working update.
