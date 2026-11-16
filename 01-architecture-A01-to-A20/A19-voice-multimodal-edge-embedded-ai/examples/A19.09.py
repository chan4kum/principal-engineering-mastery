"""Compare the two controlled calculations for A19.09."""

import sys

if "--break" in sys.argv[1:]:
    result = len(["hel", "hello", "hello"])
else:
    result = len(["hello"])
print(repr(result))
