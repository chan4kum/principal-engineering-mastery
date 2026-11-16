"""Compare the two controlled calculations for A20.21."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = 3 - 2
print(repr(result))
