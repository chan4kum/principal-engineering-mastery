"""Compare the two controlled calculations for A20.03."""

import sys

if "--break" in sys.argv[1:]:
    result = 20 - 15
else:
    result = (20 - 15) / 20
print(repr(result))
