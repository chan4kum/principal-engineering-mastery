"""Compare the two controlled calculations for A17.13."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = 2 == 3
print(repr(result))
