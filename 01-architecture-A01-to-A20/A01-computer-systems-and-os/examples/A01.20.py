"""Run with --break to select the controlled alternative."""

import sys as _sys
from threading import Event, Thread

broken = "--break" in _sys.argv[1:]

values: list[int] = []
start = Event()


def worker() -> None:
    start.wait()
    values.append(3)


thread = Thread(target=worker)
thread.start()
if broken:
    print("read early:", values)
start.set()
thread.join()
print("after join:", values)
