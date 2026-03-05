"""Ground truth formulas loaded from metadata/verified_formulas.jsonl.

Every computed value is checked against this registry before being accepted.
If a computation contradicts ANY entry here, it is REJECTED.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Optional


REGISTRY_PATH = Path(__file__).resolve().parents[2] / "metadata" / "verified_formulas.jsonl"


def load_verified_formulas() -> List[Dict]:
    """Load all verified formulas from the JSONL registry."""
    if not REGISTRY_PATH.exists():
        return []
    formulas = []
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                formulas.append(json.loads(line))
    return formulas


def get_formula(formula_id: str) -> Optional[Dict]:
    """Get a specific verified formula by ID."""
    for f in load_verified_formulas():
        if f.get("id") == formula_id:
            return f
    return None


# Pre-computed lookup for fast access
_KOSZUL_DUALS = {
    "Com": "Lie",           # VF010: Com^! = Lie (NOT coLie)
    "Lie": "Com",
    "Sym": "Lambda",        # VF011: Sym^! = Lambda
    "Lambda": "Sym",
    "Heisenberg": "Sym_ch", # VF013: H^! = Sym^ch(V*)
    "free_fermion": "beta_gamma",  # VF014: F^! = beta-gamma
    "beta_gamma": "free_fermion",
}

_KNOWN_WRONG_DUALS = {
    # These are WRONG but commonly generated
    ("Heisenberg", "Heisenberg"): "VF013: H is NOT self-dual",
    ("free_fermion", "Heisenberg"): "VF014: F^! = beta-gamma, NOT Heisenberg",
    ("Com", "coLie"): "VF010: Com^! = Lie, NOT coLie",
}


def check_koszul_dual(algebra: str, claimed_dual: str) -> tuple[bool, str]:
    """Check if a claimed Koszul dual is correct.

    Returns (is_correct, message).
    """
    pair = (algebra, claimed_dual)
    if pair in _KNOWN_WRONG_DUALS:
        return False, _KNOWN_WRONG_DUALS[pair]

    correct = _KOSZUL_DUALS.get(algebra)
    if correct is not None and correct != claimed_dual:
        return False, f"Correct dual of {algebra} is {correct}, not {claimed_dual}"

    if correct == claimed_dual:
        return True, f"Verified: {algebra}^! = {claimed_dual}"

    return True, f"No ground truth for {algebra}^! (not in registry)"
