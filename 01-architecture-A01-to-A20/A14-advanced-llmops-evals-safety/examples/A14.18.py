"""Compare the two controlled calculations for A14.18."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = sum(a == b for a, b in [(1, 1), (1, 0), (0, 0), (1, 1)]) / 4
print(repr(result))
