"""Compare the two controlled calculations for A18.05."""

import sys

if "--break" in sys.argv[1:]:
    result = bool("b")
else:
    result = "a" == "b"
print(repr(result))
