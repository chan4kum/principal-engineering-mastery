"""Compare the two controlled calculations for A16.22."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = 3 == 4
print(repr(result))
