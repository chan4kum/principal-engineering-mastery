"""Compare the two controlled calculations for A18.25."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = {"status", "usage", "version"} <= {"status", "usage"}
print(repr(result))
