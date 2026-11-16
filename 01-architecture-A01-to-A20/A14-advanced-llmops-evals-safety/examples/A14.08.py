"""Compare the two controlled calculations for A14.08."""

import sys

if "--break" in sys.argv[1:]:
    result = 0 / 3
else:
    result = 1 / 3
print(repr(result))
