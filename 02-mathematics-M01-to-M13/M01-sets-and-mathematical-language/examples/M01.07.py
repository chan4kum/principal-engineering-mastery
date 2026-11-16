"""Compare the two controlled calculations for M01.07."""

import sys

if "--break" in sys.argv[1:]:
    result = [-0.5, 0, 0.5]
else:
    result = [1 / x for x in [-2, 0, 2] if x != 0]
print(repr(result))
