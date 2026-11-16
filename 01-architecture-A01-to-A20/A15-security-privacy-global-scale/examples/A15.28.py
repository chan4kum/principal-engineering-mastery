"""Compare the two controlled calculations for A15.28."""

import sys

if "--break" in sys.argv[1:]:
    result = (120 - 114, 114 > 0)
else:
    result = (120 - 114, 114 >= 118)
print(repr(result))
