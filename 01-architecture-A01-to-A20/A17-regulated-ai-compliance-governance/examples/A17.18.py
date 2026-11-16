"""Compare the two controlled calculations for A17.18."""

import sys

if "--break" in sys.argv[1:]:
    result = len(["h1"]) == 2
else:
    result = len(["h1", "h2"]) == 2
print(repr(result))
