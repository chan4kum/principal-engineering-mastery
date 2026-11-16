"""Compare the two controlled calculations for A17.07."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = len([1, 2, 3])
print(repr(result))
