"""Connect universal checks and loop invariants to thresholded predictions."""

import numpy as np


def checked_predictions(scores, threshold: float):
    scores = np.asarray(scores, dtype=float)
    if scores.ndim != 1 or not np.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError("threshold and input shape")
    if not np.isfinite(scores).all() or not ((0 <= scores) & (scores <= 1)).all():
        raise ValueError("invalid score")
    running = 0
    counts = []
    for value in scores:
        running += int(value >= threshold)
        counts.append(running)
    return counts
