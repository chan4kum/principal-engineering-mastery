"""Compare the two controlled calculations for A14.01."""

import sys

if "--break" in sys.argv[1:]:
    result = sum([1, 1, 1]) / 3
else:
    result = sum([1, 1, 1, 0]) / 4
print(repr(result))
