"""Compare the two controlled calculations for A15.27."""

import sys

if "--break" in sys.argv[1:]:
    result = 3 / 3
else:
    result = 1 / 3
print(repr(result))
