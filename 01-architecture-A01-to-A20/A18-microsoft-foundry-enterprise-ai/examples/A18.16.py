"""Compare the two controlled calculations for A18.16."""

import sys

if "--break" in sys.argv[1:]:
    result = bool("idx-b")
else:
    result = {"a": "idx-a"}["a"] == "idx-b"
print(repr(result))
