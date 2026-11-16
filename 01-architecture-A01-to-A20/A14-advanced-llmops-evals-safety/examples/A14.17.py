"""Compare the two controlled calculations for A14.17."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = sum(b - a for a, b in zip([0, 1, 1, 0], [1, 1, 0, 1])) / 4
print(repr(result))
