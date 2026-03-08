#!/usr/bin/env python3
"""Profile scaling of genus-1 sl2 PBW diagnostics across tensor powers.

Usage:
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --max-power 6
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --min-power 7 --max-power 7 --casimir-method theory
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --min-power 7 --max-power 7 --casimir-method exact
    python3 compute/scripts/profile_genus1_pbw_sl2_scaling.py --skip-casimir
"""

from __future__ import annotations

import argparse
import os
import sys
from time import perf_counter

# Scripts are run standalone (not via pytest); add repository root for compute.* imports.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from compute.lib.genus1_pbw_sl2 import (
    CASIMIR_EXACT_CUTOFF,
    DIM_SL2,
    bracket_d1_on_tensor_power,
    casimir_method_for_tensor_power,
    casimir_eigenspace_multiplicities_on_tensor_power,
    invariant_subspace_dimension_on_tensor_power,
    d1_is_equivariant_on_tensor_power,
    casimir_d1_commutator_on_tensor_power,
)


def timed(label: str, fn):
    t0 = perf_counter()
    value = fn()
    dt = perf_counter() - t0
    return label, value, dt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-power", type=int, default=2)
    parser.add_argument("--max-power", type=int, default=6)
    parser.add_argument(
        "--casimir-method",
        choices=("auto", "exact", "theory"),
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
    print(
        f"Casimir mode: {args.casimir_method} (auto cutoff={args.exact_cutoff})"
    )
    print(
        "power | rank(d1) | ker(d1) | inv-dim | equivariant | [C2,d1]=0 | timings (s)"
    )
    print("-" * 78)

    for power in range(args.min_power, args.max_power + 1):
        d1_name, d1_matrix, d1_build_t = timed(
            "d1-build", lambda p=power: bracket_d1_on_tensor_power(p)
        )
        rank_name, rank_value, rank_t = timed("rank", lambda m=d1_matrix: m.rank())
        ker_name = "ker"
        ker_value = DIM_SL2 ** power - rank_value
        ker_t = 0.0
        inv_name, inv_value, inv_t = timed(
            "inv", lambda p=power: invariant_subspace_dimension_on_tensor_power(p)
        )
        if args.skip_equivariance:
            eq_name, eq_value, eq_t = "eq", "skipped", 0.0
        else:
            eq_name, eq_value, eq_t = timed(
                "eq", lambda p=power: d1_is_equivariant_on_tensor_power(p)
            )
        if args.skip_commutator:
            comm_name, comm_value, comm_t = "comm", "skipped", 0.0
        else:
            comm_name, comm_value, comm_t = timed(
                "comm", lambda p=power: casimir_d1_commutator_on_tensor_power(p).is_zero_matrix
            )
        if args.skip_casimir:
            casimir_summary = "skipped"
            casimir_t = 0.0
            casimir_mode = "skipped"
        else:
            casimir_name, casimir_value, casimir_t = timed(
                "casimir",
                lambda p=power: casimir_eigenspace_multiplicities_on_tensor_power(
                    p,
                    method=args.casimir_method,
                    exact_cutoff=args.exact_cutoff,
                ),
            )
            casimir_mode = casimir_method_for_tensor_power(
                power=power,
                method=args.casimir_method,
                exact_cutoff=args.exact_cutoff,
            )
            casimir_summary = str(casimir_value)

        total_t = d1_build_t + rank_t + ker_t + inv_t + eq_t + comm_t + casimir_t
        timing = (
            f"{d1_name}:{d1_build_t:.3f}, {rank_name}:{rank_t:.3f}, "
            f"{ker_name}:{ker_t:.3f}, {inv_name}:{inv_t:.3f}, "
            f"{eq_name}:{eq_t:.3f}, {comm_name}:{comm_t:.3f}, casimir:{casimir_t:.3f}, "
            f"total:{total_t:.3f}"
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
