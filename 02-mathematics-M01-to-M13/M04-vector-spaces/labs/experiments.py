"""Vector geometry and feature redundancy controls."""

import numpy as np


def norm(broken):
    vector = np.array([3, 0 if broken else 4])
    return float(np.linalg.norm(vector))


def dot(broken):
    left = np.array([1, 2])
    right = np.array([3]) if broken else np.array([3, 4])
    try:
        return int(left @ right)
    except ValueError:
        return "shape mismatch"


def rank_sweep(broken):
    deltas = [0, 1, 2]
    if broken:
        deltas[2] = 0
    return [int(np.linalg.matrix_rank([[1, 2], [2, 4 + delta]])) for delta in deltas]


def feature_predictions(broken):
    inputs = np.array([[1, 2], [2, 5 if broken else 4]])
    original = inputs @ [1, 1]
    changed = inputs @ [-1, 2]
    return (changed - original).tolist()


LABS = {
    "L1": (norm, 5.0, 3.0),
    "L2": (dot, 11, "shape mismatch"),
    "L3": (rank_sweep, [1, 2, 2], [1, 2, 1]),
    "L4": (feature_predictions, [0, 0], [0, 1]),
}
