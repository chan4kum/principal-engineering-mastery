"""Compare the two controlled calculations for A16.31."""

import sys

if "--break" in sys.argv[1:]:
    result = 8 > 0
else:
    result = 8 >= 9
print(repr(result))
