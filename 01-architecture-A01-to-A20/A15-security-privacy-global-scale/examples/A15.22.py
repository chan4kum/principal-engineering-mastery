"""Compare the two controlled calculations for A15.22."""

import sys

if "--break" in sys.argv[1:]:
    result = len({1, 2} - {2})
else:
    result = len({1, 2} - {1, 2})
print(repr(result))
