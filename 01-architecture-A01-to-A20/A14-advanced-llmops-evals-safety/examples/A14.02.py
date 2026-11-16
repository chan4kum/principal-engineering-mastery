"""Compare the two controlled calculations for A14.02."""

import sys

if "--break" in sys.argv[1:]:
    result = sum([1]) / 1
else:
    result = sum([1, 1, 0, 1]) / 4
print(repr(result))
