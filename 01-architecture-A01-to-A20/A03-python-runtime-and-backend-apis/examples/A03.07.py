"""Run normal or controlled failure for A03.07."""

import sys as _sys

broken = "--break" in _sys.argv[1:]


def rows():
    for value in range(3):
        print("produce", value)
        yield value


stream = rows()
iterator = iter(list(stream)) if broken else stream
print("first:", next(iterator))
