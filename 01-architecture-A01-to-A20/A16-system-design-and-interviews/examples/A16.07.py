"""Compare the two controlled calculations for A16.07."""

import sys

if "--break" in sys.argv[1:]:
    result = 10000 // 100
else:
    result = 10000 * 1 // 1000
print(repr(result))
