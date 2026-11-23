"""Regression residuals, regularization, and optimization controls."""

import numpy as np


def mse(broken):
    observed = np.array([1, 3])
    predicted = np.array([2, 4 if broken else 3])
    return float(np.mean((observed - predicted) ** 2))


def prediction(broken):
    design = np.array([[1, 2], [1, 3]])
    weights = np.array([2]) if broken else np.array([1, 2])
    try:
        return (design @ weights).tolist()
    except ValueError:
        return "shape mismatch"


def step_sweep(broken):
    rates = np.array([0.05, 0.1, 1.0 if broken else 1 / 6])
    weights = 6 * rates
    return ((weights - 3) ** 2 + 2 * weights ** 2).tolist()


def ridge_fit(broken):
    design = np.array([[1.0], [2.0]])
    target = np.array([2.0, 4.0])
    penalty = 0 if broken else 5
    matrix = design.T @ design + penalty * np.eye(1)
    return np.linalg.solve(matrix, design.T @ target).tolist()


LABS = {
    "L1": (mse, 0.5, 1.0),
    "L2": (prediction, [5, 7], "shape mismatch"),
    "L3": (step_sweep, [7.47, 6.48, 6.0], [7.47, 6.48, 81.0]),
    "L4": (ridge_fit, [1.0], [2.0]),
}
