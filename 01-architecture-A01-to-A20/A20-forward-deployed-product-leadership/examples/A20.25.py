"""Compare the two controlled calculations for A20.25."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = "restricted" in {"draft", "summarize"}
print(repr(result))
