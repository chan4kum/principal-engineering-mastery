"""Run normal or controlled failure for A03.22."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

row = {"id": 8, "label": "item", "internal_cost": 21}
public = row if broken else {field: row[field] for field in ("id", "label")}
print(sorted(public))
