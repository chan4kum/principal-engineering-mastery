"""Verify a mathematics lab or check a learner's independent project."""

import argparse
import json
from pathlib import Path
from runpy import run_path

import numpy as np


ROOT = Path(__file__).resolve().parent
MODULES = tuple(f"M{number:02}" for number in range(4, 14))


def module_path(module):
    (path,) = sorted(ROOT.glob(f"{module}-*"))
    return path


def matches(actual, expected):
    """Match JSON structure exactly and compare floating-point results with tolerance."""
    if isinstance(expected, dict):
        return isinstance(actual, dict) and actual.keys() == expected.keys() and all(
            matches(actual[key], value) for key, value in expected.items()
        )
    if isinstance(expected, list):
        return isinstance(actual, (list, tuple)) and len(actual) == len(expected) and all(
            matches(item, reference) for item, reference in zip(actual, expected, strict=True)
        )
    if isinstance(expected, float):
        return (
            isinstance(actual, (int, float, np.integer, np.floating))
            and not isinstance(actual, (bool, np.bool_))
            and bool(np.isclose(actual, expected, rtol=1e-7, atol=1e-9))
        )
    if isinstance(expected, bool):
        return isinstance(actual, (bool, np.bool_)) and actual == expected
    if isinstance(expected, int):
        return (
            isinstance(actual, (int, np.integer))
            and not isinstance(actual, (bool, np.bool_))
            and actual == expected
        )
    return isinstance(actual, type(expected)) and actual == expected


def verify_lab(module, lab, broken=False):
    source = module_path(module) / "labs" / "experiments.py"
    experiments = run_path(str(source))["LABS"]
    experiment, normal, changed = experiments[lab]
    result = experiment(broken)
    expected = changed if broken else normal
    if not matches(result, expected):
        raise SystemExit(f"{module} {lab}: expected {expected!r}, observed {result!r}")
    label = "failure control" if broken else "normal control"
    return f"{module} {lab} {label}: {result!r}"


def verify_project(module, solution):
    source = module_path(module) / "projects" / "independent" / "cases.json"
    cases = json.loads(source.read_text())
    solve = run_path(str(solution)).get("solve")
    if not callable(solve):
        raise SystemExit("Define a callable solve(case) in your solution file.")
    for case in cases:
        result = solve(case["input"])
        if not matches(result, case["expected"]):
            raise SystemExit(f"{case['name']}: expected {case['expected']!r}, observed {result!r}")
    return f"{module}: {len(cases)} independent project cases passed"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("module", choices=MODULES)
    commands = parser.add_subparsers(dest="command", required=True)
    lab = commands.add_parser("lab")
    lab.add_argument("lab", choices=("L1", "L2", "L3", "L4"))
    lab.add_argument("--break", dest="broken", action="store_true")
    project = commands.add_parser("project")
    project.add_argument("solution", type=Path)
    args = parser.parse_args()

    if args.command == "lab":
        print(verify_lab(args.module, args.lab, args.broken))
    else:
        print(verify_project(args.module, args.solution))


if __name__ == "__main__":
    main()
