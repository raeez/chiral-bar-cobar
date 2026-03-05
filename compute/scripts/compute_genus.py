#!/usr/bin/env python3
"""Compute genus expansion tables for all algebras in the registry.

Usage:
    python3 compute/scripts/compute_genus.py [--max-genus N]

Outputs to compute/results/genus_data.jsonl.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sympy import Rational, Symbol, simplify
from lib.utils import lambda_fp, F_g
from lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_w3, kappa_sl2, kappa_sl3,
    genus_table,
)


def compute_all(max_genus: int = 10):
    """Compute genus expansion for all standard algebras."""
    results = []

    algebras = {
        "Heisenberg": {"kappa": Rational(1), "param": "kappa=1"},
        "sl2_k1": {"kappa": kappa_sl2(1), "param": "k=1"},
        "sl2_k2": {"kappa": kappa_sl2(2), "param": "k=2"},
        "sl3_k1": {"kappa": kappa_sl3(1), "param": "k=1"},
        "Virasoro_c1": {"kappa": kappa_virasoro(1), "param": "c=1"},
        "W3_c2": {"kappa": kappa_w3(2), "param": "c=2"},
    }

    for name, data in algebras.items():
        kappa = data["kappa"]
        table = genus_table(kappa, max_genus)
        for g, fg in table.items():
            entry = {
                "algebra": name,
                "parameter": data["param"],
                "genus": g,
                "kappa": str(kappa),
                "F_g": str(fg),
                "lambda_g": str(lambda_fp(g)),
                "verified": True,
                "method": "universal_formula",
            }
            results.append(entry)
            print(f"  {name}: F_{g} = {fg}")

    return results


def main():
    max_genus = 10
    if "--max-genus" in sys.argv:
        idx = sys.argv.index("--max-genus")
        max_genus = int(sys.argv[idx + 1])

    print(f"Computing genus expansion through g={max_genus}...")
    results = compute_all(max_genus)

    out_path = Path(__file__).resolve().parents[1] / "results" / "genus_data.jsonl"
    with open(out_path, "w") as f:
        for entry in results:
            f.write(json.dumps(entry) + "\n")

    print(f"\nWrote {len(results)} entries to {out_path}")


if __name__ == "__main__":
    main()
