"""Compare the two controlled calculations for A19.13."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = 1 == 2
print(repr(result))
