"""Compare the two controlled calculations for A17.08."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = 3 / 4
print(repr(result))
