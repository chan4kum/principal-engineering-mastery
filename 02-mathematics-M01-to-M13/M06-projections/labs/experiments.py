"""Projection, least-squares, and cosine controls."""

import numpy as np


def project(broken):
    point = np.array([3, 1])
    basis = np.array([0, 0] if broken else [1, 1])
    length_squared = basis @ basis
    if length_squared == 0:
        return "zero direction"
    return (point @ basis / length_squared * basis).tolist()


def residual(broken):
    observed = np.array([2.0, 4.0, 6.0])
    design = np.ones((3, 1))
    if broken:
        design = design[:2]
    try:
        weights, *_ = np.linalg.lstsq(design, observed, rcond=None)
    except np.linalg.LinAlgError:
        return "row mismatch"
    return float(np.linalg.norm(design.T @ (observed - design @ weights)))


def error_sweep(broken):
    observed = np.array([2, 4, 6])
    candidates = [3, 4, 5 if not broken else 6]
    return [int(np.sum((observed - candidate) ** 2)) for candidate in candidates]


def cosine(broken):
    query = np.array([0, 0] if broken else [1, 0])
    candidate = np.array([1, 1])
    denominator = np.linalg.norm(query) * np.linalg.norm(candidate)
    return float(query @ candidate / denominator) if denominator else "undefined"


LABS = {
    "L1": (project, [2.0, 2.0], "zero direction"),
    "L2": (residual, 0.0, "row mismatch"),
    "L3": (error_sweep, [11, 8, 11], [11, 8, 20]),
    "L4": (cosine, 2 ** -0.5, "undefined"),
}
