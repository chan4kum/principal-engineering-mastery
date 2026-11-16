"""Compare the two controlled calculations for A20.01."""

import sys

if "--break" in sys.argv[1:]:
    result = 7 + 12 + 6
else:
    result = 7 + 5 + 6
print(repr(result))
