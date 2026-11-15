"""Run normal or controlled failure for A03.36."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

intervals = [(10, 70), (40, 100)]
child_ms = (
    sum(end - start for start, end in intervals)
    if broken
    else len(set().union(*(range(a, b) for a, b in intervals)))
)
print("outside child ms:", 150 - child_ms)
