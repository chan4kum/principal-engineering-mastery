"""Compare the two controlled calculations for M03.07."""

import sys

if "--break" in sys.argv[1:]:
    result = 1 / 0.1
else:
    result = 1 / 0.001
print(repr(result))
