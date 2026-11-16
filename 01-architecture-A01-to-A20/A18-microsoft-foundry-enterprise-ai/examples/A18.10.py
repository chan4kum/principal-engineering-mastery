"""Compare the two controlled calculations for A18.10."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(cp and resume for cp, resume in [(True, True), (True, False)])
print(repr(result))
