"""Compare the two controlled calculations for A18.07."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = 1
print(repr(result))
