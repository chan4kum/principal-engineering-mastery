"""Compare the two controlled calculations for A20.09."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = 3 / 5
print(repr(result))
