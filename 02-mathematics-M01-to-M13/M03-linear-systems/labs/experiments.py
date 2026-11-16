"""Verify elimination, conditioning and a regression transfer exercise."""

import numpy as np
from guided import classify, solve_pivot
from independent import fit


def observe(lab, broken):
    if lab == 1:
        return classify([[1, 1], [2, 2]], [3, 7] if broken else [3, 6])
    try:
        if lab == 2:
            a = [[0, 1], [1, 1]]
            b = [2] if broken else [2, 5]
            result = solve_pivot(a, b)
            assert np.allclose(result, np.linalg.solve(a, b))
            return result.tolist()
        if lab == 3:
            scales = [1.0, 0.1, 0.0] if broken else [1.0, 0.1, 0.001]
            return [round(np.linalg.cond(np.diag([1, d]))) if d else "singular" for d in scales]
        weights, residual = fit(
            [[1, 0], [1, 0 if broken else 1], [1, 0 if broken else 2]], [1, 3, 5]
        )
        return weights.round(9).tolist(), round(residual, 9)
    except (ValueError, np.linalg.LinAlgError):
        return "invalid"


EXPECTED = (
    ("underdetermined", "inconsistent"),
    ([3.0, 2.0], "invalid"),
    ([1, 10, 1000], [1, 10, "singular"]),
    (([1.0, 2.0], 0.0), "invalid"),
)
