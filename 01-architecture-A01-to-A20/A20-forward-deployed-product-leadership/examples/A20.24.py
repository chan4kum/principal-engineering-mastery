"""Compare the two controlled calculations for A20.24."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = 4 / 6
print(repr(result))
