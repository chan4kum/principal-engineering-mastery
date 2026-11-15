"""Run normal or controlled failure for A03.27."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

rows = [10, 20, 30, 40]
first = rows[:2]
rows.insert(1, 15)
print(rows[2:4] if broken else [key for key in rows if key > first[-1]][:2])
