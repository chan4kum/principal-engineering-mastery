"""Compare the two controlled calculations for A20.06."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = 4 - 3
print(repr(result))
