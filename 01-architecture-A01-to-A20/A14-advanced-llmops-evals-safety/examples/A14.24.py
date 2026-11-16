"""Compare the two controlled calculations for A14.24."""

import sys

if "--break" in sys.argv[1:]:
    result = 90 > 90 and 80 < 100
else:
    result = 90 >= 90 and 80 < 100
print(repr(result))
