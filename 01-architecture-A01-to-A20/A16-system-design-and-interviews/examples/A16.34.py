"""Compare the two controlled calculations for A16.34."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = 4 - 3
print(repr(result))
