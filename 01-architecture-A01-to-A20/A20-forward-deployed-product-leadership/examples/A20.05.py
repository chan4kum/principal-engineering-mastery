"""Compare the two controlled calculations for A20.05."""

import sys

if "--break" in sys.argv[1:]:
    result = 4 + 5 + 3 <= 8
else:
    result = 4 + 3 <= 8
print(repr(result))
