"""Derivatives, Jacobians, Hessians, and parameter updates."""

import numpy as np


def quotient(broken):
    x, step = 3.0, 0.25 if broken else 0.125
    return ((x + step)**2 - x**2) / step


def jacobian(broken):
    x, y = 2, 3
    matrix = np.array([[1, 2 * y], [y, x]])
    return ((matrix.T if broken else matrix) @ [1, 0]).tolist()


def curvature_sweep(broken):
    values = [1, 0.5, -0.5 if broken else 0.25]
    return [float(np.min(np.linalg.eigvalsh(np.diag([2, value])))) for value in values]


def update(broken):
    design = np.array([[1.0], [2.0]])
    target = np.array([1.0, 2.0])
    weight = np.zeros(1)
    gradient = design.T @ (design @ weight - target)
    weight = weight - (1.0 if broken else 0.2) * gradient
    residual = design @ weight - target
    return float(0.5 * (residual @ residual))


LABS = {
    "L1": (quotient, 6.125, 6.25),
    "L2": (jacobian, [1, 3], [1, 6]),
    "L3": (curvature_sweep, [1.0, 0.5, 0.25], [1.0, 0.5, -0.5]),
    "L4": (update, 0.0, 40.0),
}
