"""Compare the two controlled calculations for A18.20."""

import sys

if "--break" in sys.argv[1:]:
    result = (2, 0, 0)
else:
    result = (2, 2, 0)
print(repr(result))
