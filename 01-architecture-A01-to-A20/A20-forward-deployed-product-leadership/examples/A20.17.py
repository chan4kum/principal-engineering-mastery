"""Compare the two controlled calculations for A20.17."""

import sys

if "--break" in sys.argv[1:]:
    result = 3
else:
    result = max(0, 3 - 2)
print(repr(result))
