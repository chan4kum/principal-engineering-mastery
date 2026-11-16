"""Compare the two controlled calculations for A15.23."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = int("write" in {"read"})
print(repr(result))
