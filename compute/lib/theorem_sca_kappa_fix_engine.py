r"""Compatibility surface for superconformal parameter arithmetic.

Earlier versions of this module promoted coset bookkeeping and affine
reflections directly to genus-one modular characteristics.  The canonical
implementation now lives in ``theorem_ap49_superconformal_engine`` and keeps
those layers separate.  This file preserves the historical API while making
every open modular request explicit.
"""

from __future__ import annotations

from fractions import Fraction

from compute.lib.theorem_ap49_superconformal_engine import (
    OpenSuperconformalInvariantError,
    n2_central_charge,
    n2_koszul_dual_c,
    n2_level_from_c,
    n4_central_charge,
    n4_koszul_dual_c,
    superconformal_hierarchy as _typed_hierarchy,
    superconformal_status_packet,
)


F = Fraction


def _open(family: str):
    raise OpenSuperconformalInvariantError(
        superconformal_status_packet(family)["required_input"]
    )


def kappa_n2_from_level(k: Fraction) -> Fraction:
    return _open("N=2")


def kappa_n2_from_c(c: Fraction) -> Fraction:
    return _open("N=2")


def kappa_n2_coset_decomposition(k: Fraction):
    k = F(k)
    return {
        "status": "central-charge coset parameter only",
        "level": k,
        "central_charge": n2_central_charge(k),
        "kappa_total": None,
        "required_input": superconformal_status_packet("N=2")["required_input"],
    }


def n2_complementarity_sum(c: Fraction) -> Fraction:
    return _open("N=2")


def kappa_n4_from_level(k: Fraction) -> Fraction:
    return _open("small N=4")


def kappa_n4_from_c(c: Fraction) -> Fraction:
    return _open("small N=4")


def n4_complementarity_sum_ff(c: Fraction) -> Fraction:
    return _open("small N=4")


def n4_complementarity_sum_cy(k: Fraction) -> Fraction:
    return _open("small N=4")


def kappa_svir(c: Fraction) -> Fraction:
    return _open("N=1")


def superconformal_hierarchy():
    return _typed_hierarchy()


def verify_n2_ap49_discrepancy():
    c = n2_central_charge(F(1))
    return {
        "status": "open modular lane",
        "level": F(1),
        "central_charge": c,
        "inverse_level": n2_level_from_c(c),
        "parameter_reflection": n2_koszul_dual_c(c),
        "kappa": None,
    }


def verify_n4_ap49_discrepancy():
    c = n4_central_charge(F(1))
    return {
        "status": "open modular lane",
        "level": F(1),
        "central_charge": c,
        "parameter_reflection": n4_koszul_dual_c(c),
        "kappa": None,
    }


def n2_kappa_multipath(c: Fraction):
    c = F(c)
    return {
        "status": "open modular lane",
        "central_charge": c,
        "level": n2_level_from_c(c),
        "kappa": None,
        "paths_agree": None,
    }


def n4_kappa_multipath(k: Fraction):
    k = F(k)
    return {
        "status": "open modular lane",
        "level": k,
        "central_charge": n4_central_charge(k),
        "kappa": None,
        "paths_agree": None,
    }
