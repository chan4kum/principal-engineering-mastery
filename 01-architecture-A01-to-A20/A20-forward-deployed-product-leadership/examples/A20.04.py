"""Compare the two controlled calculations for A20.04."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = 18 - 14
print(repr(result))
