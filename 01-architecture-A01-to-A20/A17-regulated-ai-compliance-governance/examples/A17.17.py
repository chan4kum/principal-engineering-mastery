"""Compare the two controlled calculations for A17.17."""

import sys

if "--break" in sys.argv[1:]:
    result = None is not False
else:
    result = None is True
print(repr(result))
