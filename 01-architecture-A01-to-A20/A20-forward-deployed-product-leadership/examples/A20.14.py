"""Compare the two controlled calculations for A20.14."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"a", "b"} - {"a", "c"})
print(repr(result))
