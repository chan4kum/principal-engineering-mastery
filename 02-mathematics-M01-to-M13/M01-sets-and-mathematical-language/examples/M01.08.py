"""Compare the two controlled calculations for M01.08."""

import sys

if "--break" in sys.argv[1:]:
    result = sum(x > 5 for x in [2, 5, 8])
else:
    result = sum(x >= 5 for x in [2, 5, 8])
print(repr(result))
