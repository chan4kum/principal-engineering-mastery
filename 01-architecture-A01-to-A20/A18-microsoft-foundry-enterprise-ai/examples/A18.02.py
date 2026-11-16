"""Compare the two controlled calculations for A18.02."""

import sys

if "--break" in sys.argv[1:]:
    result = len({"revisions", "scheduler"} - {"revisions"})
else:
    result = len({"revisions", "scheduler"} - {"revisions", "scheduler"})
print(repr(result))
