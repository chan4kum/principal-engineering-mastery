"""Compare the two controlled calculations for A17.22."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"source", "policy", "model"} - {"source", "model"})
print(repr(result))
