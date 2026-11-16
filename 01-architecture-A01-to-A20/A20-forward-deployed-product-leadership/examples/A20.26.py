"""Compare the two controlled calculations for A20.26."""

import sys

if "--break" in sys.argv[1:]:
    result = 150 / 100
else:
    result = (150 - 100) / 100
print(repr(result))
