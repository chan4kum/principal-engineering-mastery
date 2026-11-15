"""Run normal or controlled failure for A03.08."""

import sys as _sys

broken = "--break" in _sys.argv[1:]


def square(value: int):
    if not broken and type(value) is not int:
        return "rejected"
    return value * 2


print(square("7"))
