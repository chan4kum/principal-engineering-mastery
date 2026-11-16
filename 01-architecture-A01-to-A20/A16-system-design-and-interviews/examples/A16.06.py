"""Compare the two controlled calculations for A16.06."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(c <= 7 for c in [5, 9])
print(repr(result))
