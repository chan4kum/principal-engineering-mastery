"""Run normal or controlled failure for A03.38."""

import sys as _sys
from contextlib import contextmanager

broken = "--break" in _sys.argv[1:]


@contextmanager
def lifespan():
    print("open")
    try:
        yield
    finally:
        print("close")


if broken:
    print("open")
else:
    with lifespan():
        print("serve")
