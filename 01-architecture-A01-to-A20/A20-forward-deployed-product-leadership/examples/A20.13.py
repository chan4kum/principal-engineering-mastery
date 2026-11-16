"""Compare the two controlled calculations for A20.13."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(x == 4 for x in [3, 4])
print(repr(result))
