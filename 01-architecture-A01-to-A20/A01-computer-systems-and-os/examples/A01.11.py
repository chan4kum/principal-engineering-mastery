"""Run with --break to select the controlled alternative."""

import sys as _sys
import os

broken = "--break" in _sys.argv[1:]

read_fd, write_fd = os.pipe()
try:
    os.write(write_fd, b"K")
    try:
        print(os.read(-1 if broken else read_fd, 1))
    except OSError as error:
        print(f"kernel errno={error.errno}")
finally:
    os.close(read_fd)
    os.close(write_fd)
