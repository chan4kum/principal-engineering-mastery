"""Compare the two controlled calculations for A15.13."""

import sys

if "--break" in sys.argv[1:]:
    result = len({"source"} - {"source"})
else:
    result = len({"source", "index", "cache"} - {"source", "cache"})
print(repr(result))
