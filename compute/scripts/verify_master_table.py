#!/usr/bin/env python3
"""Cross-check all Master Table entries against computed values.

Reads known bar dimensions, kappa values, and genus data from the
computational kernel, and verifies them against each other.

Usage:
    python3 compute/scripts/verify_master_table.py
"""

import json
import sys
from pathlib import Path

# Scripts are run standalone (not via pytest); add compute/ root for lib.* imports.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sympy import Rational, simplify
from lib.bar_complex import (
    KNOWN_BAR_DIMS,
    bar_dim_heisenberg,
    bar_dim_free_fermion,
    verify_bar_dim,
)
from lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_w3, kappa_sl2, kappa_sl3,
)
from lib.lie_algebra import (
    cartan_data, sugawara_c, ff_dual_level, kappa_km,
    sigma_invariant, virasoro_ds_c, w3_ds_c,
)
from lib.utils import lambda_fp, partition_number


def verify_bar_dims():
    """Verify all known bar dimensions."""
    print("\n=== BAR DIMENSIONS ===")
    passes = 0
    fails = 0

    # Heisenberg: dim B-bar^1 = 1, dim B-bar^n = p(n-2) for n >= 2
    # Source: free_fields.tex rem:bar-dims-partitions
    for d in range(1, 6):
        if d == 1:
            expected = 1
        else:
            expected = partition_number(d - 2)
        computed = bar_dim_heisenberg(d)
        ok = computed == expected
        status = "PASS" if ok else "FAIL"
        formula = "1" if d == 1 else f"p({d-2})"
        print(f"  Heisenberg deg {d}: computed={computed}, {formula}={expected} [{status}]")
        if ok:
            passes += 1
        else:
            fails += 1

    # Free fermion: dim B-bar^n = p(n-1)
    for d in range(1, 6):
        expected = partition_number(d - 1)
        computed = bar_dim_free_fermion(d)
        ok = computed == expected
        status = "PASS" if ok else "FAIL"
        print(f"  Free fermion deg {d}: computed={computed}, p({d-1})={expected} [{status}]")
        if ok:
            passes += 1
        else:
            fails += 1

    # Cross-check against KNOWN_BAR_DIMS registry
    for algebra, dims in KNOWN_BAR_DIMS.items():
        for deg, expected in dims.items():
            ok, msg = verify_bar_dim(algebra, deg, expected)
            if ok:
                passes += 1
            else:
                fails += 1
                print(f"  {msg}")

    return passes, fails


def verify_kappa_formulas():
    """Verify kappa values against independent derivations."""
    print("\n=== KAPPA VALUES ===")
    passes = 0
    fails = 0

    # sl_2: kappa = dim * (k + h*) / (2 * h*) = 3*(k+2)/4
    for k_val in [1, 2, 5, 10]:
        from_formula = kappa_sl2(k_val)
        from_general = kappa_km("A", 1, k_val)
        ok = simplify(from_formula - from_general) == 0
        status = "PASS" if ok else "FAIL"
        print(f"  sl2 k={k_val}: formula={from_formula}, general={from_general} [{status}]")
        if ok:
            passes += 1
        else:
            fails += 1

    # sl_3: kappa = 4*(k+3)/3
    for k_val in [1, 2, 5]:
        from_formula = kappa_sl3(k_val)
        from_general = kappa_km("A", 2, k_val)
        ok = simplify(from_formula - from_general) == 0
        status = "PASS" if ok else "FAIL"
        print(f"  sl3 k={k_val}: formula={from_formula}, general={from_general} [{status}]")
        if ok:
            passes += 1
        else:
            fails += 1

    # Virasoro: kappa(Vir_c) = c/2. For DS of sl_2:
    # c(k) = 1 - 6(k+1)^2/(k+2), so kappa = c/2
    for k_val in [0, 1, 2, 5]:
        c_val = virasoro_ds_c(k_val)
        kappa_vir = kappa_virasoro(c_val)
        expected = c_val / 2
        ok = simplify(kappa_vir - expected) == 0
        status = "PASS" if ok else "FAIL"
        print(f"  Vir k={k_val}: c={c_val}, kappa={kappa_vir} [{status}]")
        if ok:
            passes += 1
        else:
            fails += 1

    return passes, fails


def verify_ff_involution():
    """Verify FF involution is an involution: (k')' = k."""
    print("\n=== FF INVOLUTION ===")
    passes = 0
    fails = 0

    for type_, rank in [("A", 1), ("A", 2), ("B", 2), ("G", 2), ("D", 4)]:
        for k_val in [0, 1, 5, 10]:
            k_prime = ff_dual_level(type_, rank, k_val)
            k_double = ff_dual_level(type_, rank, k_prime)
            ok = simplify(k_double - k_val) == 0
            status = "PASS" if ok else "FAIL"
            print(f"  {type_}{rank} k={k_val}: k'={k_prime}, k''={k_double} [{status}]")
            if ok:
                passes += 1
            else:
                fails += 1

    return passes, fails


def verify_complementarity():
    """Verify kappa(k) + kappa(k') is level-independent."""
    print("\n=== COMPLEMENTARITY ===")
    passes = 0
    fails = 0

    for type_, rank in [("A", 1), ("A", 2), ("B", 2), ("G", 2)]:
        sums = []
        for k_val in [0, 1, 2, 5, 10, 100]:
            k_prime = ff_dual_level(type_, rank, k_val)
            kap = kappa_km(type_, rank, k_val)
            kap_prime = kappa_km(type_, rank, k_prime)
            total = simplify(kap + kap_prime)
            sums.append(total)

        # All sums should be equal
        all_equal = all(simplify(s - sums[0]) == 0 for s in sums)
        status = "PASS" if all_equal else "FAIL"
        print(f"  {type_}{rank}: kappa + kappa' = {sums[0]} (constant: {all_equal}) [{status}]")
        if all_equal:
            passes += 1
        else:
            fails += 1

    return passes, fails


def main():
    print("=" * 60)
    print("  MASTER TABLE VERIFICATION")
    print("=" * 60)

    total_passes = 0
    total_fails = 0

    for verify_fn in [verify_bar_dims, verify_kappa_formulas,
                      verify_ff_involution, verify_complementarity]:
        p, f = verify_fn()
        total_passes += p
        total_fails += f

    print("\n" + "=" * 60)
    print(f"  TOTAL: {total_passes} passed, {total_fails} failed")
    print("=" * 60)

    return 0 if total_fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
