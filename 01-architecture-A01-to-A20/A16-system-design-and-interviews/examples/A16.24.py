"""Compare the two controlled calculations for A16.24."""

import sys

if "--break" in sys.argv[1:]:
    result = 5
else:
    result = 5 * (5 - 1)
print(repr(result))
