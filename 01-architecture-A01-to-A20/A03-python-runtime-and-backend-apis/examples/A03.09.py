"""Run normal or controlled failure for A03.09."""

import sys as _sys
from contextlib import contextmanager

broken = "--break" in _sys.argv[1:]

events = []


@contextmanager
def resource():
    events.append("open")
    try:
        yield
    finally:
        events.append("close")


try:
    if broken:
        events.append("open")
        raise ValueError("write failed")
    with resource():
        raise ValueError("write failed")
except ValueError:
    print(events)
