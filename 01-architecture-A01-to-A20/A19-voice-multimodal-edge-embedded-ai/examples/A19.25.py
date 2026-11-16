"""Compare the two controlled calculations for A19.25."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"latency", "route", "pcm", "text"} - {"latency", "route"})
print(repr(result))
