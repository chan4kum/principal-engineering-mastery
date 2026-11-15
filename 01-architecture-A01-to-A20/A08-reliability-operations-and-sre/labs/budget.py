"""Request-based error budget with exact parts-per-million arithmetic."""

import argparse
from fractions import Fraction


def budget(eligible: int, bad: int, target_ppm: int) -> dict[str, int | float]:
    if eligible < 1 or not 0 <= bad <= eligible or not 0 < target_ppm < 1_000_000:
        raise ValueError("invalid counts or objective")
    allowed_fraction = Fraction(1_000_000 - target_ppm, 1_000_000)
    return {
        "eligible": eligible,
        "bad": bad,
        "allowed_bad": int(eligible * allowed_fraction),
        "remaining": int(eligible * allowed_fraction) - bad,
        "burn": float(Fraction(bad, eligible) / allowed_fraction),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--break", dest="burst", action="store_true")
    args = parser.parse_args()
    print(
        "30-day request window:",
        budget(1_000_000, 1500 if args.burst else 500, 999_000),
    )
