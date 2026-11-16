"""Trace partial pivoting and classify exact small systems by rank."""

import numpy as np


def solve_pivot(matrix, rhs, tolerance: float = 1e-12):
    a = np.asarray(matrix, dtype=float)
    b = np.asarray(rhs, dtype=float)
    if (
        a.ndim != 2
        or a.shape[0] != a.shape[1]
        or a.shape[0] == 0
        or b.shape != (a.shape[0],)
        or not np.isfinite(a).all()
        or not np.isfinite(b).all()
        or not np.isfinite(tolerance)
        or tolerance <= 0
    ):
        raise ValueError("finite square system and matching right-hand side required")
    n = len(b)
    augmented = np.column_stack((a, b))
    for col in range(n):
        pivot = col + int(np.argmax(np.abs(augmented[col:, col])))
        if abs(augmented[pivot, col]) <= tolerance:
            raise np.linalg.LinAlgError("small pivot; check rank and conditioning")
        augmented[[col, pivot]] = augmented[[pivot, col]]
        for row in range(col + 1, n):
            augmented[row, col:] -= (augmented[row, col] / augmented[col, col]) * augmented[
                col, col:
            ]
    x = np.zeros(n)
    for row in range(n - 1, -1, -1):
        x[row] = (augmented[row, -1] - augmented[row, row + 1 : n] @ x[row + 1 : n]) / augmented[
            row, row
        ]
    return x


def classify(matrix, rhs):
    a = np.asarray(matrix, dtype=float)
    b = np.asarray(rhs, dtype=float)
    if a.ndim != 2 or not a.size or b.shape != (a.shape[0],):
        raise ValueError("matching system dimensions required")
    rank = np.linalg.matrix_rank(a)
    augmented_rank = np.linalg.matrix_rank(np.column_stack((a, b)))
    if rank != augmented_rank:
        return "inconsistent"
    return "unique" if rank == a.shape[1] else "underdetermined"
