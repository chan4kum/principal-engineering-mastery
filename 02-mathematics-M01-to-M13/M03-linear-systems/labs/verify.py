"""Run a phase lab and verify its observed control."""

import argparse
from pathlib import Path
import sys

_PROJECTS = Path(__file__).resolve().parents[1] / "projects"
sys.path[0:0] = [str(_PROJECTS / "guided"), str(_PROJECTS / "independent")]

from experiments import EXPECTED, observe  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("lab", choices=["L1", "L2", "L3", "L4"])
    parser.add_argument("--break", dest="broken", action="store_true")
    args = parser.parse_args()
    lab = int(args.lab[1])
    result = observe(lab, args.broken)
    expected = EXPECTED[lab - 1][int(args.broken)]
    if result != expected:
        raise SystemExit(f"{args.lab}: expected {expected!r}, observed {result!r}")
    print(f"{args.lab} {'failure control' if args.broken else 'normal control'}: {result!r}")


if __name__ == "__main__":
    main()
