r"""Exact N=2 parameter arithmetic and the open genus-one ledger.

The Kazama--Suzuki relation ``c=3k/(k+2)`` and its inverse are exact.
The affine maps ``k -> -k-4`` and ``c -> 6-c`` are likewise elementary
rational identities.  Turning a formal coset subtraction into the modular
characteristic of the N=2 algebra requires a trace-compatible genus-one
coset theorem; this module exposes that obligation explicitly.
"""

from __future__ import annotations

import sympy as sp


k = sp.Symbol("k")
c = sp.Symbol("c")


class OpenN2InvariantError(RuntimeError):
    """Raised when parameter arithmetic is promoted to an open invariant."""


REQUIRED_INPUT = (
    "genus-one Kazama--Suzuki coset curvature with trace-compatible "
    "numerator, fermion, and U(1) subtraction maps"
)


def _sym(value):
    return sp.sympify(value)


def n2_central_charge(k_val=None):
    kval = k if k_val is None else _sym(k_val)
    if kval == -2:
        raise ValueError("k=-2 is the pole of c=3k/(k+2)")
    return sp.simplify(3 * kval / (kval + 2))


def k_from_c(c_val=None):
    cval = c if c_val is None else _sym(c_val)
    if cval == 3:
        raise ValueError("c=3 is the pole of k=2c/(3-c)")
    return sp.simplify(2 * cval / (3 - cval))


def n2_koszul_dual_level(k_val=None):
    """Compatibility name for the affine reflection candidate k -> -k-4."""
    kval = k if k_val is None else _sym(k_val)
    return -kval - 4


def n2_koszul_dual_c(c_val=None):
    """Compatibility name for the induced arithmetic reflection c -> 6-c."""
    cval = c if c_val is None else _sym(c_val)
    return 6 - cval


def parameter_reflection_check(k_val=None):
    kval = k if k_val is None else _sym(k_val)
    c_source = n2_central_charge(kval)
    c_reflected = n2_central_charge(n2_koszul_dual_level(kval))
    return {
        "level": kval,
        "reflected_level": n2_koszul_dual_level(kval),
        "central_charge": c_source,
        "reflected_central_charge": c_reflected,
        "sum": sp.simplify(c_source + c_reflected),
        "involutive": sp.simplify(
            n2_koszul_dual_level(n2_koszul_dual_level(kval)) - kval
        ) == 0,
        "interpretation": "arithmetic reflection candidate",
    }


def n2_modular_status():
    return {
        "status": "open",
        "kappa": None,
        "K_kappa": None,
        "anomaly_ratio": None,
        "required_input": REQUIRED_INPUT,
    }


def _open():
    raise OpenN2InvariantError(REQUIRED_INPUT)


def kappa_n2_correct(c_val=None):
    return _open()


def kappa_n2_from_k(k_val=None):
    return _open()


def kappa_n2_wrong(c_val=None):
    return _open()


def kappa_sl2(k_val=None):
    return _open()


def kappa_fermion_pair():
    return _open()


def kappa_u1_denominator(k_val=None):
    return _open()


def coset_decomposition(k_val):
    kval = _sym(k_val)
    return {
        "status": "open modular comparison",
        "level": kval,
        "central_charge": n2_central_charge(kval),
        "formal_numerator": "V_k(sl_2) plus a complex fermion",
        "formal_denominator": "U(1)",
        "kappa_sl2": None,
        "kappa_fermion": None,
        "kappa_u1": None,
        "kappa_coset": None,
        "required_input": REQUIRED_INPUT,
    }


def complementarity_sum(c_val=None, k_val=None):
    return _open()


def wrong_duality_check(c_val=None, k_val=None):
    cval = c if c_val is None else _sym(c_val)
    return {
        "status": "comparison of parameter maps only",
        "additive_candidate": 6 - cval,
        "multiplicative_candidate": sp.simplify(9 / cval),
        "kappa": None,
    }


def discrepancy(c_val):
    return {
        "central_charge": _sym(c_val),
        "status": "open modular comparison",
        "kappa": None,
        "required_input": REQUIRED_INPUT,
    }


def discrepancy_symbolic():
    return discrepancy(c)


def sl2_naive_vs_correct(k_val):
    return coset_decomposition(k_val)


def F1_values():
    return {
        "status": "open",
        "values": None,
        "required_input": REQUIRED_INPUT,
    }


def sigma_n2(c_val=None):
    return _open()


def verify_resolution():
    checks = {}
    for kval in (sp.Integer(1), sp.Integer(2), sp.Integer(5), sp.Rational(7, 3)):
        cval = n2_central_charge(kval)
        checks[f"inverse@{kval}"] = sp.simplify(k_from_c(cval) - kval) == 0
        packet = parameter_reflection_check(kval)
        checks[f"reflection-sum@{kval}"] = packet["sum"] == 6
        checks[f"involution@{kval}"] = packet["involutive"]
    return {
        "exact_parameter_checks": checks,
        "all_exact_checks_pass": all(checks.values()),
        "modular_status": n2_modular_status(),
    }
