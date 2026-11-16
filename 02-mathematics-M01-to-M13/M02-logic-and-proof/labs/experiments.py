"""Verify truth tables, input shape, empty domains and ML transfer."""

from guided import implication_table, quantifiers
from independent import checked_predictions


def observe(lab, broken):
    if lab == 1:
        return implication_table()[:, 4 if broken else 2].tolist()
    try:
        if lab == 2:
            return quantifiers([True, False] if broken else [[True, False], [False, True]])
        if lab == 3:
            return quantifiers([[True], [False]] if broken else [[True], [True]])
        return checked_predictions([0.25, 1.4 if broken else 0.5, 0.9], 0.5)
    except ValueError:
        return "invalid"


EXPECTED = (
    ([1, 1, 0, 1], [1, 0, 1, 1]),
    ((True, False), "invalid"),
    ((True, True), (False, False)),
    ([0, 1, 2], "invalid"),
)
