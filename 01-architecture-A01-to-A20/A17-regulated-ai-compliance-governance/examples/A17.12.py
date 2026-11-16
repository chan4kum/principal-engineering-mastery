"""Compare the two controlled calculations for A17.12."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = 2 / 3
print(repr(result))
