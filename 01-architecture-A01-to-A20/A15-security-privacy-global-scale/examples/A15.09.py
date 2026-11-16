"""Compare the two controlled calculations for A15.09."""

import sys

if "--break" in sys.argv[1:]:
    result = len({7, 7})
else:
    result = len({("a", 7), ("b", 7)})
print(repr(result))
