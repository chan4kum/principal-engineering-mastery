"""Compare the two controlled calculations for A16.18."""

import sys

if "--break" in sys.argv[1:]:
    result = 1
else:
    result = len({"a", "b"}) / 4
print(repr(result))
