"""Compare the two controlled calculations for A15.29."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"read-old", "write-new", "copy"} - {"read-old", "copy"})
print(repr(result))
