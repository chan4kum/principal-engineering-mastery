"""SVD reconstruction, truncation, and PCA controls."""

import numpy as np


def rank(broken):
    matrix = [[1, 2], [2, 5 if broken else 4]]
    return int(np.linalg.matrix_rank(matrix))


def reconstruction(broken):
    matrix = np.diag([4, 2, 1])
    left, values, right = np.linalg.svd(matrix, full_matrices=False)
    if broken:
        values[1] = 0
    return float(np.linalg.norm(matrix - left @ np.diag(values) @ right))


def error_sweep(broken):
    singular_values = np.linalg.svd(np.diag([4, 2, 1]), compute_uv=False)
    ranks = [0, 1, 1 if broken else 2, 3]
    return [float(np.linalg.norm(singular_values[rank:])) for rank in ranks]


def pca_variance(broken):
    samples = np.array([[10, -1], [10, 0], [10, 1]])
    if not broken:
        samples = samples - samples.mean(axis=0)
    singular_values = np.linalg.svd(samples, compute_uv=False)
    return (singular_values ** 2 / (len(samples) - 1)).tolist()


LABS = {
    "L1": (rank, 1, 2),
    "L2": (reconstruction, 0.0, 2.0),
    "L3": (error_sweep, [21 ** 0.5, 5 ** 0.5, 1.0, 0.0], [21 ** 0.5, 5 ** 0.5, 5 ** 0.5, 0.0]),
    "L4": (pca_variance, [1.0, 0.0], [150.0, 1.0]),
}
