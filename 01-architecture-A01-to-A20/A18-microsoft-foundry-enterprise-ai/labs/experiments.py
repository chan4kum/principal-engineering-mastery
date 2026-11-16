"""Exercise in-process mock scope, pricing and outage policies."""

from guided import Route, route, search
from independent import Meter, Usage


def observe(lab, broken):
    if lab == 1:
        try:
            return search(
                "a",
                "idx-b" if broken else "idx-a",
                {"a": "idx-a"},
                [("a", "idx-a", 2, "own"), ("b", "idx-b", 9, "foreign")],
            )
        except PermissionError:
            return ()
    if lab == 2:
        meter = Meter({"a": 11}, 20)
        try:
            return meter.charge("a", "r1", Usage("a", 2, 4 if broken else 3))
        except OverflowError:
            return "quota"
    if lab == 3:
        try:
            return route(
                [Route("west", "primary", False), Route("east", "secondary", True)],
                {"west"} if broken else {"east", "west"},
            ).deployment
        except LookupError:
            return "deferred"
    meter = Meter({"a": 10, "b": 10}, 20)
    meter.charge("a", "r1", Usage("a", 4, 2))
    try:
        meter.charge("a", "r1", Usage("b" if broken else "a", 4, 2))
    except PermissionError:
        return ("denied", meter.total("a"), meter.total("b"))
    return ("replay", meter.total("a"), meter.total("b"))


EXPECTED = (
    (("own",), ()),
    (11, "quota"),
    ("secondary", "deferred"),
    (("replay", 10, 0), ("denied", 10, 0)),
)
