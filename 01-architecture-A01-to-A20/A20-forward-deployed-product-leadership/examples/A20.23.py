"""Compare the two controlled calculations for A20.23."""

import sys

if "--break" in sys.argv[1:]:
    result = any([True, True, False])
else:
    result = all([True, True, False])
print(repr(result))
