"""Finite-set operations with an explicit universe."""

import numpy as np


def incidence(universe, selected):
    values = np.asarray(universe)
    if values.ndim != 1 or np.unique(values).size != values.size:
        raise ValueError("universe must be a vector of unique values")
    selected = np.asarray(selected)
    if selected.ndim != 1 or not np.isin(selected, values).all():
        raise ValueError("selection must be inside the universe")
    return np.isin(values, selected)


def partition(universe, left, right):
    a = incidence(universe, left)
    b = incidence(universe, right)
    return (int((a | b).sum()), int((a & b).sum()), int((~(a | b)).sum()))
