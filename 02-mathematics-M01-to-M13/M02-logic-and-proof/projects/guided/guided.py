"""Truth tables and quantifier order over finite sets."""

from itertools import product

import numpy as np


def implication_table():
    pairs = list(product((False, True), repeat=2))
    p, q = np.asarray(pairs).T
    return np.column_stack((p, q, ~p | q, q | ~p, p | ~q)).astype(int)


def quantifiers(matrix):
    matrix = np.asarray(matrix)
    if matrix.ndim != 2 or matrix.dtype != np.dtype(bool):
        raise ValueError("two-axis predicate relation required")
    return (bool(matrix.any(axis=1).all()), bool(matrix.all(axis=0).any()))
