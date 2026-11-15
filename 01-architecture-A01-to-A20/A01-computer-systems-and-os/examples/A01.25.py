"""Run with --break to select the controlled alternative."""

import sys as _sys
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Lock

broken = "--break" in _sys.argv[1:]

counter = 0
rendezvous, lock = Barrier(2, timeout=2), Lock()


def increment() -> None:
    global counter
    if broken:
        previous = counter
        rendezvous.wait()
        counter = previous + 1
    else:
        with lock:
            counter += 1


with ThreadPoolExecutor(2) as pool:
    list(pool.map(lambda _: increment(), range(2)))
print(counter)
