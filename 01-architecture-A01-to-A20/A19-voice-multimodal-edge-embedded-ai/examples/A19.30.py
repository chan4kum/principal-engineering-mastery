"""Compare the two controlled calculations for A19.30."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = 4 - 3
print(repr(result))
