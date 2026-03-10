#!/usr/bin/env python3
"""Profile scaling of genus-1 sl2 PBW diagnostics across tensor powers.

Usage:
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --max-power 6
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --min-power 7 --max-power 7 --casimir-method modular
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --min-power 7 --max-power 7 --casimir-method exact_sparse
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --min-power 7 --max-power 7 --casimir-method exact
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --skip-casimir
"""

from __future__ import annotations

import argparse
import os
import sys

# Scripts are run standalone (not via pytest); add repository root for compute.* imports.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from compute.lib.genus1_pbw_sl2 import (
    CASIMIR_EXACT_CUTOFF,
    CASIMIR_MODULAR_PRIMES,
    CASIMIR_MODULAR_STRATEGY,
    staged_frontier_diagnostics_on_tensor_power,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-power", type=int, default=2)
    parser.add_argument("--max-power", type=int, default=6)
    parser.add_argument(
        "--casimir-method",
        choices=("auto", "exact", "exact_sparse", "modular", "theory"),
        default="auto",
        help="Casimir multiplicity backend (default: auto).",
    )
    parser.add_argument(
        "--exact-cutoff",
        type=int,
        default=CASIMIR_EXACT_CUTOFF,
        help="Power cutoff used when --casimir-method=auto.",
    )
    parser.add_argument(
        "--modular-prime",
        dest="modular_primes",
        action="append",
        type=int,
        default=None,
        help="Prime used for --casimir-method=modular (repeat flag for multiple primes).",
    )
    parser.add_argument(
        "--modular-strategy",
        choices=("auto", "global", "weight_block"),
        default=CASIMIR_MODULAR_STRATEGY,
        help="Sparse/modular backend strategy used when Casimir mode is modular.",
    )
    parser.add_argument(
        "--skip-casimir",
        action="store_true",
        help="Skip Casimir eigenspace computation (usually the slowest step).",
    )
    parser.add_argument(
        "--skip-equivariance",
        action="store_true",
        help="Skip d1 equivariance checks.",
    )
    parser.add_argument(
        "--skip-commutator",
        action="store_true",
        help="Skip Casimir-commutator checks [C2,d1]=0.",
    )
    args = parser.parse_args()

    if args.min_power < 2:
        raise SystemExit("--min-power must be >= 2")
    if args.max_power < args.min_power:
        raise SystemExit("--max-power must be >= --min-power")

    print("=" * 78)
    print("GENUS-1 sl2 PBW DIAGNOSTICS SCALING PROFILE")
    print("=" * 78)
    modular_primes = tuple(args.modular_primes) if args.modular_primes else CASIMIR_MODULAR_PRIMES
    print(
        f"Casimir mode: {args.casimir_method} (auto cutoff={args.exact_cutoff})"
    )
    print(f"Modular strategy: {args.modular_strategy}")
    print(f"Modular primes: {modular_primes}")
    print(
        "power | rank(d1) | ker(d1) | inv-dim | equivariant | [C2,d1]=0 | timings (s)"
    )
    print("-" * 78)

    for power in range(args.min_power, args.max_power + 1):
        report = staged_frontier_diagnostics_on_tensor_power(
            power=power,
            casimir_method=args.casimir_method,
            exact_cutoff=args.exact_cutoff,
            modular_primes=modular_primes,
            modular_strategy=args.modular_strategy,
            include_casimir=not args.skip_casimir,
            include_equivariance=not args.skip_equivariance,
            include_commutator=not args.skip_commutator,
            include_timings=True,
        )
        timings = report["timings"]
        rank_value = report["rank_d1"]
        ker_value = report["kernel_dim_d1"]
        inv_value = report["invariant_dim"]
        eq_value = report["equivariant"] if not args.skip_equivariance else "skipped"
        comm_value = (
            report["casimir_commutator_zero"] if not args.skip_commutator else "skipped"
        )
        casimir_mode = report["casimir_mode"] if not args.skip_casimir else "skipped"
        casimir_summary = (
            str(report["casimir_eigenspaces"]) if not args.skip_casimir else "skipped"
        )
        timing = (
            f"d1-rank:{timings['d1_rank']:.3f}, inv:{timings['invariant_dim']:.3f}, "
            f"eq:{timings['equivariance']:.3f}, comm:{timings['commutator']:.3f}, "
            f"casimir:{timings['casimir']:.3f}, total:{timings['total']:.3f}"
        )
        print(
            f"{power:>5} | {rank_value:>8} | {ker_value:>7} | {inv_value:>7} | "
            f"{str(eq_value):>10} | {str(comm_value):>9} | {timing}"
        )
        print(f"      Casimir eigenspaces ({casimir_mode}): {casimir_summary}")

    print("-" * 78)
    print("Done.")


if __name__ == "__main__":
    main()
