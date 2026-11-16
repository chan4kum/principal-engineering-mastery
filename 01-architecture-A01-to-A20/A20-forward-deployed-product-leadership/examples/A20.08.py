"""Compare the two controlled calculations for A20.08."""

import sys

if "--break" in sys.argv[1:]:
    result = 0.7 > 0.6
else:
    result = 0.7 - 0.6 >= 0.12
print(repr(result))
