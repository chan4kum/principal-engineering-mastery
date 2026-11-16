"""Compare the two controlled calculations for A16.13."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = min(1, 2)
print(repr(result))
