"""Compare the two controlled calculations for A18.23."""

import sys

if "--break" in sys.argv[1:]:
    result = 3 <= 3
else:
    result = 3 <= min(3, 2)
print(repr(result))
