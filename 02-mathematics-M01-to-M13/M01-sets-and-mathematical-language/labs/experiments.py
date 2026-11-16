"""Test finite sets and transfer indicator weighting to model evaluation."""

from guided import partition
from independent import weighted_error


def observe(lab, broken):
    try:
        if lab == 1:
            return partition([0, 1, 2, 3], [0, 1], [2] if broken else [1, 2])
        if lab == 2:
            return partition([[0, 1, 2]] if broken else [0, 1, 2], [0, 1], [1])
        if lab == 3:
            universe = [-3, -2, -1, 0, 1, 2, 3]
            return [
                partition(universe, [x for x in universe if x >= bound], [])[0]
                for bound in ([0, 1, 4] if broken else [-4, 0, 4])
            ]
        return weighted_error(
            [0, 1, 0],
            [False, False, False] if broken else [True, True, False],
            [1, 3, 1],
        )
    except ValueError:
        return "invalid"


EXPECTED = (
    ((3, 1, 1), (3, 0, 1)),
    ((2, 1, 1), "invalid"),
    ([7, 4, 0], [4, 3, 0]),
    (0.75, "invalid"),
)
