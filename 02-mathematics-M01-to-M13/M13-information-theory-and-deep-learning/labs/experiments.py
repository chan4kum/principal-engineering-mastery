"""Stable losses, gradients, and training controls."""

import numpy as np


def cross_entropy(broken):
    assigned = 0.0 if broken else 0.25
    return float(-np.log2(assigned)) if assigned else "infinite"


def softmax(broken):
    logits = np.array([1000.0, 1000.0])
    if not broken:
        logits -= logits.max()
    with np.errstate(over="ignore", invalid="ignore"):
        values = np.exp(logits)
        probabilities = values / values.sum()
    return probabilities.tolist() if np.all(np.isfinite(probabilities)) else "nonfinite"


def learning_rate_sweep(broken):
    rates = np.array([0.5, 1.0, 2.5 if broken else 1.5])
    # Three updates for L(w) = w²/2 and w initialized at 1.
    return ((1 - rates) ** 3).tolist()


def backprop(broken):
    weight, feature, target = 2.0, 3.0, 1.0
    residual = weight * feature - target
    step = 0.25 if broken else 0.1
    weight -= step * residual * feature
    return (weight * feature - target) ** 2 / 2


LABS = {
    "L1": (cross_entropy, 2.0, "infinite"),
    "L2": (softmax, [0.5, 0.5], "nonfinite"),
    "L3": (learning_rate_sweep, [0.125, 0.0, -0.125], [0.125, 0.0, -3.375]),
    "L4": (backprop, 0.125, 19.53125),
}
