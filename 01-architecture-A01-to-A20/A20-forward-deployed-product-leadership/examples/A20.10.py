"""Compare the two controlled calculations for A20.10."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = 2 / 4
print(repr(result))
