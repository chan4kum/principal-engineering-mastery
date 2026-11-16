"""Linear-system diagnostics for a local regression transfer exercise."""

import numpy as np


def fit(design, targets, max_condition: float = 1000):
    x = np.asarray(design, dtype=float)
    y = np.asarray(targets, dtype=float)
    if (
        x.ndim != 2
        or not x.size
        or y.shape != (x.shape[0],)
        or not np.isfinite(x).all()
        or not np.isfinite(y).all()
        or max_condition < 1
        or not np.isfinite(max_condition)
    ):
        raise ValueError("invalid regression shapes or numbers")
    weights, _, rank, singular_values = np.linalg.lstsq(x, y, rcond=None)
    if rank != x.shape[1] or singular_values[0] / singular_values[-1] > max_condition:
        raise np.linalg.LinAlgError("design is rank-deficient or ill-conditioned")
    return weights, float(np.linalg.norm(x @ weights - y))
