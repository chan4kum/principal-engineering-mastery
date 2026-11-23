"""Eigenvector, reconstruction, and iteration controls."""

import numpy as np


def eigenvector(broken):
    matrix = np.diag([2, 3])
    vector = np.array([1, int(broken)])
    return (matrix @ vector - 2 * vector).tolist()


def reconstruct(broken):
    matrix = np.array([[2, 1], [1, 2]])
    eigenvalues, vectors = np.linalg.eigh(matrix)
    if broken:
        eigenvalues = eigenvalues[::-1]
    return float(np.linalg.norm(matrix - vectors @ np.diag(eigenvalues) @ vectors.T))


def radius_sweep(broken):
    scales = [0.5, 0.8, 0.9]
    if broken:
        scales[-1] = 1.2
    return [float(max(abs(np.linalg.eigvals(np.diag([0.5, -scale]))))) for scale in scales]


def iteration(broken):
    # Linearized update x_next = (I - step * H) x for a diagonal quadratic Hessian.
    step = 1.0 if broken else 0.25
    transition = np.eye(2) - step * np.diag([1, 3])
    return (np.linalg.matrix_power(transition, 3) @ np.ones(2)).tolist()


LABS = {
    "L1": (eigenvector, [0, 0], [0, 1]),
    "L2": (reconstruct, 0.0, 8 ** 0.5),
    "L3": (radius_sweep, [0.5, 0.8, 0.9], [0.5, 0.8, 1.2]),
    "L4": (iteration, [0.421875, 0.015625], [0.0, -8.0]),
}
