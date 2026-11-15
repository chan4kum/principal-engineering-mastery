"""Run normal or controlled failure for A03.06."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

keys = list(range(1000))
checks = 0
if broken:
    for key in keys:
        checks += 1
        if key == 999:
            break
else:
    index = dict.fromkeys(keys)
    checks = int(999 in index)
print(checks, "key checks in model")
