"""Run normal or controlled failure for A03.31."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

items, outcomes = [], {}
for key in ("same", "same"):
    if broken or key not in outcomes:
        items.append("new resource")
        outcomes[key] = len(items)
print("commits:", len(items))
