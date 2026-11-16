"""Compare the two controlled calculations for M02.07."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = ((2 * 1 + 1) + (2 * 2 + 1)) % 2
print(repr(result))
