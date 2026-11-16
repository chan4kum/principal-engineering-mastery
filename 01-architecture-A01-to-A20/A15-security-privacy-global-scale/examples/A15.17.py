"""Compare the two controlled calculations for A15.17."""

import sys

if "--break" in sys.argv[1:]:
    result = 5 >= 3
else:
    result = 2 >= 3
print(repr(result))
