"""Compare the two controlled calculations for M03.05."""

import sys

if "--break" in sys.argv[1:]:
    result = 3 * 4
else:
    result = 3 * 4 - 1 * 2
print(repr(result))
