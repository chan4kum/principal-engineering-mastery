"""Compare the two controlled calculations for A15.11."""

import sys

if "--break" in sys.argv[1:]:
    result = len({"shared"})
else:
    result = len({"data-a", "data-b"})
print(repr(result))
