r"""Typed arithmetic for the superconformal comparison ledger.

The engine certifies parameter changes and rational identities.  A modular
characteristic is exposed numerically only in the Virasoro lane, where the
repository has a proved genus-one calculation.  The N=1, N=2, small N=4,
and Bershadsky--Polyakov lanes return explicit open status until their
genus-one curvature complexes and comparison maps are constructed.
"""

from __future__ import annotations

from fractions import Fraction


F = Fraction


class OpenSuperconformalInvariantError(RuntimeError):
    """Raised when a rational parameter formula is asked to act as kappa."""


def _fraction(value) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


# ---------------------------------------------------------------------------
# Virasoro: certified scalar lane
# ---------------------------------------------------------------------------


def kappa_vir(c: Fraction) -> Fraction:
    return _fraction(c) / 2


def vir_koszul_dual_c(c: Fraction) -> Fraction:
    """The certified Virasoro reflection c -> 26-c."""
    return 26 - _fraction(c)


def vir_comp_sum(c: Fraction) -> Fraction:
    return kappa_vir(c) + kappa_vir(vir_koszul_dual_c(c))


# ---------------------------------------------------------------------------
# Superconformal parameter maps: exact arithmetic, open modular meaning
# ---------------------------------------------------------------------------


def svir_koszul_dual_c(c: Fraction) -> Fraction:
    """Affine reflection candidate c -> 15-c."""
    return 15 - _fraction(c)


def n2_central_charge(k: Fraction) -> Fraction:
    """Kazama--Suzuki parameter relation c=3k/(k+2)."""
    k = _fraction(k)
    if k == -2:
        raise ValueError("k=-2 is the pole of c=3k/(k+2)")
    return 3 * k / (k + 2)


def n2_level_from_c(c: Fraction) -> Fraction:
    c = _fraction(c)
    if c == 3:
        raise ValueError("c=3 is the pole of k=2c/(3-c)")
    return 2 * c / (3 - c)


def n2_koszul_dual_c(c: Fraction) -> Fraction:
    """Affine reflection candidate c -> 6-c."""
    return 6 - _fraction(c)


def n4_central_charge(k: Fraction) -> Fraction:
    """Small N=4 central-charge parameter relation c=6k."""
    return 6 * _fraction(k)


def n4_koszul_dual_c(c: Fraction) -> Fraction:
    """Affine reflection candidate c -> -c-24."""
    return -_fraction(c) - 24


def superconformal_status_packet(family: str):
    packets = {
        "Virasoro": {
            "status": "proved",
            "kappa_formula": "c/2",
            "reflection": "26-c",
            "K_kappa": F(13),
        },
        "N=1": {
            "status": "open",
            "parameter_reflection": "15-c",
            "required_input": "genus-one super-BRST curvature and determinant-line comparison",
        },
        "N=2": {
            "status": "open",
            "parameter_relation": "c=3k/(k+2)",
            "parameter_reflection": "6-c",
            "required_input": "genus-one Kazama--Suzuki coset curvature with subtraction maps",
        },
        "small N=4": {
            "status": "open",
            "parameter_relation": "c=6k",
            "parameter_reflection": "-c-24",
            "required_input": "genus-one small-N=4 curvature and a typed choice of duality",
        },
        "BP": {
            "status": "open",
            "parameter_reflection": "k -> -k-6",
            "required_input": (
                "complete genus-one minimal-DS curvature with charged ghosts, "
                "neutral fields, improvement term, and mixed channels"
            ),
        },
    }
    try:
        return dict(packets[family])
    except KeyError as exc:
        raise ValueError(f"unknown family: {family}") from exc


def _open_kappa(family: str):
    raise OpenSuperconformalInvariantError(
        superconformal_status_packet(family)["required_input"]
    )


def kappa_svir(c: Fraction) -> Fraction:
    return _open_kappa("N=1")


def svir_comp_sum(c: Fraction) -> Fraction:
    return _open_kappa("N=1")


def svir_kappa_decomposition(c: Fraction):
    return {
        "status": "open",
        "central_charge": _fraction(c),
        "required_input": superconformal_status_packet("N=1")["required_input"],
    }


def kappa_n2_from_c(c: Fraction) -> Fraction:
    return _open_kappa("N=2")


def kappa_n2_from_level(k: Fraction) -> Fraction:
    return _open_kappa("N=2")


def n2_comp_sum(c: Fraction) -> Fraction:
    return _open_kappa("N=2")


def n2_coset_decomposition(k: Fraction):
    k = _fraction(k)
    return {
        "status": "central-charge parameter relation only",
        "level": k,
        "central_charge": n2_central_charge(k),
        "kappa": None,
    }


def kappa_n4_from_level(k: Fraction) -> Fraction:
    return _open_kappa("small N=4")


def kappa_n4_from_c(c: Fraction) -> Fraction:
    return _open_kappa("small N=4")


def n4_comp_sum_ff(c: Fraction) -> Fraction:
    return _open_kappa("small N=4")


def n4_comp_sum_cy(k: Fraction) -> Fraction:
    return _open_kappa("small N=4")


# ---------------------------------------------------------------------------
# Bershadsky--Polyakov: FKR convention
# ---------------------------------------------------------------------------


def bp_central_charge(k: Fraction) -> Fraction:
    """Standard FKR central charge -(2k+3)(3k+1)/(k+3)."""
    k = _fraction(k)
    if k == -3:
        raise ValueError("k=-3 is the critical pole")
    return -((2 * k + 3) * (3 * k + 1)) / (k + 3)


def bp_shifted_secondary_central_charge(k: Fraction) -> Fraction:
    """Separate shifted expression 2-24(k+1)^2/(k+3)."""
    k = _fraction(k)
    if k == -3:
        raise ValueError("k=-3 is the critical pole")
    return 2 - 24 * (k + 1) ** 2 / (k + 3)


def bp_ff_dual_level(k: Fraction) -> Fraction:
    """Level reflection k -> -k-6."""
    return -_fraction(k) - 6


def bp_koszul_conductor(k: Fraction) -> Fraction:
    """Compatibility name for the exact central-charge reflection sum 50."""
    k = _fraction(k)
    return bp_central_charge(k) + bp_central_charge(bp_ff_dual_level(k))


def bp_shifted_secondary_sum(k: Fraction) -> Fraction:
    k = _fraction(k)
    return bp_shifted_secondary_central_charge(k) + bp_shifted_secondary_central_charge(
        bp_ff_dual_level(k)
    )


def bp_generator_parities():
    return {"J": "even", "T": "even", "G+": "even", "G-": "even"}


def bp_reciprocal_weight_diagnostic() -> Fraction:
    return F(1) + F(2, 3) + F(2, 3) + F(1, 2)


def bp_varrho() -> Fraction:
    return _open_kappa("BP")


def bp_varrho_unsigned() -> Fraction:
    """Compatibility API returning the reciprocal-weight diagnostic."""
    return bp_reciprocal_weight_diagnostic()


def kappa_bp(k: Fraction) -> Fraction:
    return _open_kappa("BP")


def bp_comp_sum(k: Fraction) -> Fraction:
    return _open_kappa("BP")


def kappa_bp_t_line(k: Fraction) -> Fraction:
    """Virasoro T-line projection, kept separate from full BP kappa."""
    return bp_central_charge(k) / 2


def bp_comp_sum_t_line(k: Fraction) -> Fraction:
    k = _fraction(k)
    return kappa_bp_t_line(k) + kappa_bp_t_line(bp_ff_dual_level(k))


def check_bp_anomaly_ratio():
    return {
        "parities": bp_generator_parities(),
        "reciprocal_weight_diagnostic": bp_reciprocal_weight_diagnostic(),
        "rho": None,
        "status": "open",
    }


def check_bp_collapsing_level():
    return {
        "level": F(-1),
        "standard_c": bp_central_charge(F(-1)),
        "shifted_secondary": bp_shifted_secondary_central_charge(F(-1)),
    }


def check_bp_intra_file_contradiction():
    return {
        "standard_reflection_sum": bp_koszul_conductor(F(0)),
        "shifted_secondary_sum": bp_shifted_secondary_sum(F(0)),
        "status": "resolved by separating the two conformal-vector conventions",
    }


def multipath_bp(k: Fraction):
    k = _fraction(k)
    direct = bp_koszul_conductor(k)
    reflected = bp_central_charge(k) + bp_central_charge(-k - 6)
    return {
        "standard_central_sum_direct": direct,
        "standard_central_sum_reflected": reflected,
        "central_paths_agree": direct == reflected == 50,
        "shifted_secondary_sum": bp_shifted_secondary_sum(k),
        "kappa": None,
        "K_kappa": None,
        "status": "open modular lane",
    }


# ---------------------------------------------------------------------------
# Typed cross-family reports
# ---------------------------------------------------------------------------


def superconformal_hierarchy():
    return {
        family: superconformal_status_packet(family)
        for family in ("Virasoro", "N=1", "N=2", "small N=4", "BP")
    }


def hierarchy_comp_sums_decreasing():
    raise OpenSuperconformalInvariantError(
        "cross-family ordering requires the four open genus-one modular characteristics"
    )


def check_n2_cross_volume():
    return {
        "status": "open modular lane",
        "level": F(1),
        "central_charge": n2_central_charge(F(1)),
        "inverse_level": n2_level_from_c(n2_central_charge(F(1))),
        "kappa": None,
    }


def check_n4_cross_volume():
    return {
        "status": "open modular lane",
        "level": F(1),
        "central_charge": n4_central_charge(F(1)),
        "affine_reflection": n4_koszul_dual_c(n4_central_charge(F(1))),
        "kappa": None,
    }


def ap48_kappa_not_c_over_2():
    raise OpenSuperconformalInvariantError(
        "the requested comparison requires the open superconformal kappa values"
    )


def multipath_svir(c: Fraction):
    return {
        "central_charge": _fraction(c),
        "reflected_central_charge": svir_koszul_dual_c(c),
        "kappa": None,
        "status": "open modular lane",
    }
