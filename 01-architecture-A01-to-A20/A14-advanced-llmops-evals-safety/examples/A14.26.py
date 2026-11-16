"""Compare the two controlled calculations for A14.26."""

import sys

if "--break" in sys.argv[1:]:
    result = 60 / (2 * 20)
else:
    result = 60 / (4 * 20)
print(repr(result))
