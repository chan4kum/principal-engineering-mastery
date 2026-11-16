"""Compare the two controlled calculations for A19.15."""

import sys

if "--break" in sys.argv[1:]:
    result = (1000 * 4, 1000 * 4)
else:
    result = (1000 * 4, 1000)
print(repr(result))
