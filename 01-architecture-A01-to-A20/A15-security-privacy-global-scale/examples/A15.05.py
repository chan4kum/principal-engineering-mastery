"""Compare the two controlled calculations for A15.05."""

import sys

if "--break" in sys.argv[1:]:
    result = 2 in {2, 3}
else:
    result = 2 in {3}
print(repr(result))
