"""Compare the two controlled calculations for A20.12."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = len({1, 2} - {1})
print(repr(result))
