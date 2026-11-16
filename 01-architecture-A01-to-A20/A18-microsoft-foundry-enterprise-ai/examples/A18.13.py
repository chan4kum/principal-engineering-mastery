"""Compare the two controlled calculations for A18.13."""

import sys

if "--break" in sys.argv[1:]:
    result = all([True, True])
else:
    result = all([True, True, False])
print(repr(result))
