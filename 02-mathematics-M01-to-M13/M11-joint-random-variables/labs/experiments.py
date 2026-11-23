"""Joint distributions, covariance, and transformation controls."""

import numpy as np


def conditional(broken):
    # Rows index X and columns index Y.
    joint = np.array([[0.2, 0.0], [0.8, 0.0]] if broken else [[0.3, 0.2], [0.2, 0.3]])
    marginal = float(joint[:, 1].sum())
    return float(joint[1, 1] / marginal) if marginal else "undefined"


def transform(broken):
    covariance = np.array([[1.0, 0.5], [0.5, 1.0]])
    matrix = np.array([[1.0, 1.0]])
    if broken:
        matrix = matrix.T
    try:
        return (matrix @ covariance @ matrix.T).tolist()
    except ValueError:
        return "shape mismatch"


def correlation_sweep(broken):
    correlations = [0.0, 0.5, 1.2 if broken else 1.0]
    result = []
    for correlation in correlations:
        covariance = np.array([[1.0, correlation], [correlation, 1.0]])
        smallest = np.linalg.eigvalsh(covariance).min()
        result.append("invalid covariance" if smallest < 0 else float(smallest))
    return result


def ensemble_average(broken):
    off_diagonal = 0.8 if broken else 0.0
    covariance = np.array([[1.0, off_diagonal], [off_diagonal, 1.0]])
    weights = np.full(2, 0.5)
    return float(weights @ covariance @ weights)


LABS = {
    "L1": (conditional, 0.6, "undefined"),
    "L2": (transform, [[3.0]], "shape mismatch"),
    "L3": (correlation_sweep, [1.0, 0.5, 0.0], [1.0, 0.5, "invalid covariance"]),
    "L4": (ensemble_average, 0.5, 0.9),
}
