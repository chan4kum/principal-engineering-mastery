"""Exercise controlled evaluation and release decisions."""

from guided import Case, Response, evaluate
from independent import Promotion, Release


def observe(lab, broken):
    cases = (
        Case("answer", "yes", "alpha", frozenset({"alpha:doc"})),
        Case("refusal", "decline", "alpha", frozenset(), critical=True),
    )
    rows = {
        "answer": Response(
            "no" if broken and lab in {1, 3} else "yes",
            "alpha",
            frozenset({"alpha:doc"}),
            40 if broken and lab == 2 else 20,
            5,
            10,
        ),
        "refusal": Response(
            "decline", "beta" if broken and lab == 4 else "alpha", frozenset(), 10, 2, 0
        ),
    }
    scores = evaluate(cases, rows)
    if lab == 1:
        return sum(row["answer"] for row in scores.values())
    cost = sum(response.cost_units() for response in rows.values())
    if lab == 2:
        return cost
    pipeline = Promotion(Release("m1", "p1", "set1"), frozenset(rows))
    admitted = pipeline.consider(Release("m1", "p2", "set1"), scores, 55, cost)
    active = pipeline.active.prompt
    pipeline.rollback()
    return (admitted, active, pipeline.active.prompt)


EXPECTED = (
    (2, 1),
    (51, 71),
    ((True, "p2", "p1"), (False, "p1", "p1")),
    ((True, "p2", "p1"), (False, "p1", "p1")),
)
