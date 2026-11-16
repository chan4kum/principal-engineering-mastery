"""Connect stakeholder outcomes and mandatory controls to MVP scope."""

from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Feature:
    name: str
    team_days: int
    value: int
    covers: frozenset[str]


def scope(backlog: list[Feature], required: set[str], budget: int):
    if budget < 0 or any(f.team_days < 1 or f.value < 0 for f in backlog):
        raise ValueError("invalid planning units")
    eligible = []
    for size in range(len(backlog) + 1):
        for work in combinations(backlog, size):
            cost = sum(f.team_days for f in work)
            covered = frozenset().union(*(f.covers for f in work))
            if cost <= budget and required <= covered:
                eligible.append(
                    (
                        sum(f.value for f in work),
                        -cost,
                        tuple(sorted(f.name for f in work)),
                    )
                )
    if not eligible:
        raise ValueError("mandatory scope exceeds budget")
    return max(eligible)[2]
