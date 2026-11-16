"""Compare the two controlled calculations for A20.02."""

import sys

if "--break" in sys.argv[1:]:
    result = max([0, 1, 2])
else:
    result = sum([0, 1, 2])
print(repr(result))
