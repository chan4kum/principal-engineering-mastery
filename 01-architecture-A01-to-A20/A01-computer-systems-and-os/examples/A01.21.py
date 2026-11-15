"""Run with --break to select the controlled alternative."""

import sys as _sys
import resource
import time

broken = "--break" in _sys.argv[1:]

start = resource.getrusage(resource.RUSAGE_SELF)
wall = time.perf_counter()
cpu = time.process_time()
if broken:
    sum(range(500_000))
else:
    time.sleep(0.03)
end = resource.getrusage(resource.RUSAGE_SELF)
print(f"wall={time.perf_counter() - wall:.4f}s cpu={time.process_time() - cpu:.4f}s")
print("voluntary:", end.ru_nvcsw - start.ru_nvcsw, "involuntary:", end.ru_nivcsw - start.ru_nivcsw)
