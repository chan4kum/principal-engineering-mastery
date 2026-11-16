"""Compare the two controlled calculations for A14.13."""

import sys

if "--break" in sys.argv[1:]:
    result = min([(1, 512), (4, 1024)])
else:
    result = min((cost, limit) for cost, limit in [(1, 512), (4, 1024)] if limit >= 900)
print(repr(result))
