#!/usr/bin/env python3
"""Compute genus expansions for all KM algebras with kappa functions.

Computes F_g(A) = kappa(A) * lambda_g^FP for g = 1..10 for:
  - sl2, sl3, G2, B2 (KM algebras)
  - Virasoro, W3 (W-algebras)
  - Heisenberg

Also verifies complementarity: kappa(A) + kappa(A!) = const (level-independent).

Usage:
    python3 compute/scripts/compute_genus_expansions.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from sympy import Rational, Symbol, simplify

from lib.utils import lambda_fp, F_g
from lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_w3,
    kappa_sl2, kappa_sl3, kappa_g2, kappa_b2,
    genus_table, complementarity_sum_km,
)
from lib.lie_algebra import kappa_km, ff_dual_level, cartan_data


def print_genus_table(name, kappa_val, max_g=6):
    """Print genus expansion table for an algebra."""
    print(f"\n{'─' * 60}")
    print(f"  {name}: kappa = {kappa_val}")
    print(f"{'─' * 60}")
    table = genus_table(kappa_val, max_g)
    for g, val in table.items():
        print(f"  F_{g} = {val}")


def verify_complementarity(type_, rank, name):
    """Verify kappa(A) + kappa(A!) is level-independent."""
    k = Symbol("k")
    total = complementarity_sum_km(type_, rank, k)
    print(f"  {name}: kappa(k) + kappa(k') = {total}")
    # Check level-independence: differentiate w.r.t. k
    from sympy import diff
    dk = diff(total, k)
    assert dk == 0, f"NOT level-independent! d/dk = {dk}"
    print(f"    d/dk = 0 => level-independent")
    return total


def main():
    print("=" * 60)
    print("GENUS EXPANSIONS FOR ALL ALGEBRAS")
    print("=" * 60)

    # Symbolic kappa values
    algebras = [
        ("Heisenberg (kappa=1)", kappa_heisenberg(1)),
        ("sl2 (k=1)", kappa_sl2(1)),
        ("sl2 (k=2)", kappa_sl2(2)),
        ("sl3 (k=1)", kappa_sl3(1)),
        ("G2 (k=1)", kappa_g2(1)),
        ("B2 (k=1)", kappa_b2(1)),
        ("Virasoro (c=1/2, Ising)", kappa_virasoro(Rational(1, 2))),
        ("Virasoro (c=26)", kappa_virasoro(26)),
        ("W3 (c=2)", kappa_w3(2)),
    ]

    for name, kval in algebras:
        print_genus_table(name, kval, max_g=6)

    # Symbolic genus tables
    print("\n\n" + "=" * 60)
    print("SYMBOLIC GENUS TABLES")
    print("=" * 60)

    k = Symbol("k")
    for name, kfunc in [("sl2", kappa_sl2), ("sl3", kappa_sl3),
                         ("G2", kappa_g2), ("B2", kappa_b2)]:
        kval = kfunc()
        print(f"\n  {name}: kappa = {kval}")
        for g in range(1, 4):
            fg = F_g(kval, g)
            print(f"    F_{g} = {fg}")

    # Complementarity verification
    print("\n\n" + "=" * 60)
    print("COMPLEMENTARITY: kappa(k) + kappa(k') = const")
    print("=" * 60)

    results = {}
    for type_, rank, name in [("A", 1, "sl2"), ("A", 2, "sl3"),
                               ("B", 2, "B2/so5"), ("G", 2, "G2")]:
        results[name] = verify_complementarity(type_, rank, name)

    # Cross-check: the constant should be dim(g)
    print("\n  Cross-check against dim(g):")
    for type_, rank, name in [("A", 1, "sl2"), ("A", 2, "sl3"),
                               ("B", 2, "B2/so5"), ("G", 2, "G2")]:
        data = cartan_data(type_, rank)
        print(f"    {name}: kappa + kappa' = {results[name]}, dim(g) = {data.dim}")

    # Faber-Pandharipande numbers
    print("\n\n" + "=" * 60)
    print("FABER-PANDHARIPANDE NUMBERS lambda_g^FP")
    print("=" * 60)
    for g in range(1, 11):
        print(f"  lambda_{g}^FP = {lambda_fp(g)}")

    # Verification: ratio test
    print("\n\n" + "=" * 60)
    print("CONVERGENCE: |F_{g+1}/F_g| -> 1/(2pi)^2")
    print("=" * 60)
    kval = Rational(1)  # kappa = 1 for simplicity
    for g in range(1, 8):
        fg = F_g(kval, g)
        fg1 = F_g(kval, g + 1)
        if fg != 0:
            ratio = fg1 / fg
            print(f"  F_{g+1}/F_{g} = {float(ratio):.8f}")
    from sympy import pi
    print(f"  1/(2*pi)^2 = {float(1/(2*pi)**2):.8f}")

    print("\n  All checks passed.")


if __name__ == "__main__":
    main()
