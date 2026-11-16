"""Compare the two controlled calculations for A14.23."""

import sys

if "--break" in sys.argv[1:]:
    result = (0, 2)
else:
    result = (0, 0)
print(repr(result))
