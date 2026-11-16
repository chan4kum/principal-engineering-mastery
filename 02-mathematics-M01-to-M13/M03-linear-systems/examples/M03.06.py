"""Compare the two controlled calculations for M03.06."""

import sys

if "--break" in sys.argv[1:]:
    result = 6 - 2 * 3
else:
    result = 7 - 2 * 3
print(repr(result))
