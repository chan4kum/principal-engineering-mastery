"""Cohort counting and weighted error estimates with set indicators."""

import numpy as np


def weighted_error(errors, eligible, weights):
    errors = np.asarray(errors, dtype=float)
    eligible = np.asarray(eligible)
    weights = np.asarray(weights, dtype=float)
    if errors.ndim != 1 or errors.shape != eligible.shape or errors.shape != weights.shape:
        raise ValueError("aligned vectors required")
    if (
        eligible.dtype != np.dtype(bool)
        or np.any(~np.isfinite(errors))
        or np.any(~np.isfinite(weights))
        or np.any(weights < 0)
    ):
        raise ValueError("invalid cohort weights or indicators")
    used = weights[eligible]
    total = float(used.sum())
    if not np.isfinite(total) or total <= 0:
        raise ValueError("cohort requires positive finite weight")
    return float(np.dot(errors[eligible], used) / total)
