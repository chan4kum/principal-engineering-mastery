"""Compare the two controlled calculations for A16.15."""

import sys

if "--break" in sys.argv[1:]:
    result = 3
else:
    result = len(set(["e1", "e2", "e1"]))
print(repr(result))
