"""Run discovery, selection and customer environment delivery cases."""

from guided import Feature, scope
from independent import Delivery, Evidence


def observe(lab, broken):
    if lab <= 2:
        backlog = [
            Feature("quick demo", 2, 9, frozenset()),
            Feature("verified integration", 3, 5, frozenset({"workflow"})),
            Feature("failure recovery", 2, 7, frozenset({"recovery"})),
        ]
        required = {"workflow", "recovery"} if lab == 2 else {"workflow"}
        try:
            return scope(
                backlog,
                set() if broken and lab == 1 else required,
                4 if broken and lab == 2 else 5,
            )
        except ValueError:
            return ()
    delivery = Delivery("v1")
    admit = delivery.rollout("v2", Evidence(True, not (broken and lab == 3), True, 99, 100))
    if lab == 3:
        return admit, delivery.active
    final = delivery.monitor(Evidence(True, True, True, 95 if broken else 100, 100))
    return final, len(delivery.log)


EXPECTED = (
    (("quick demo", "verified integration"), ("failure recovery", "quick demo")),
    (("failure recovery", "verified integration"), ()),
    ((True, "v2"), (False, "v1")),
    (("v2", 1), ("v1", 2)),
)
