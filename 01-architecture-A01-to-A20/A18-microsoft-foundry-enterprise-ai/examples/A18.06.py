"""Compare the two controlled calculations for A18.06."""

import sys

if "--break" in sys.argv[1:]:
    result = 2000 * 0.03
else:
    result = 2000 * 0.03 / 1000
print(repr(result))
