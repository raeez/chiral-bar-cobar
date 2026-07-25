r"""Koszul conductor table engine: K(A) = kappa(A) + kappa(A^!) for all families.

Computes two complementarity invariants for every family in the standard
chiral algebra landscape:

  K_cc(A) = c(A) + c(A^!)          (central charge sum)
  K_kk(A) = kappa(A) + kappa(A^!)  (Koszul conductor)

The Koszul conductor K_kk is the invariant called K(A) in the monograph
(C18 of the true formula census).  Known values:

  K_kk = 0       for KM, Heisenberg, lattice, free families
  K_kk = 13      for Virasoro
  K_kk = 250/3   for W_3
  K_cc = 50      for the standard Bershadsky--Polyakov central charges
  K_kk = open    for Bershadsky--Polyakov pending genus-one DS curvature

All arithmetic uses fractions.Fraction for exact rational results.

Canonical references:
  C1.  kappa(H_k) = k
  C2.  kappa(Vir_c) = c/2
  C3.  kappa(V_k(g)) = dim(g)*(k+h^v) / (2*h^v)
       on the non-critical affine conductor lane
  C4.  kappa(W_N) = c*(H_N - 1),  H_N = sum_{j=1}^{N} 1/j
  C5.  c_bc(lambda) = 1 - 3*(2*lambda - 1)^2
  C6.  c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)
  C7.  c_bc(lambda) + c_bg(lambda) = 0
  C18. K(A) = kappa(A) + kappa(A^!)
  C20. K_BP = c_BP(k) + c_BP(-k-6) = 50 in the canonical census lane

The secondary shifted formula ``2-24(k+1)^2/(k+3)`` has conductor 196.
It is retained under explicitly shifted names and never enters the canonical
cross-family table.
"""

from fractions import Fraction
from typing import Any, Dict, Tuple

try:
    from compute.lib.bp_koszul_conductor_engine import (
        BP_KAPPA_STATUS,
        K_BP_EXACT,
        K_BP_SHIFTED_EXACT,
        SHIFTED_BP_CONVENTION,
        STANDARD_BP_CONVENTION,
        UnverifiedBPInvariantError,
        K_BP as _canonical_bp_conductor,
        K_BP_shifted as _shifted_bp_conductor,
        c_BP as _canonical_bp_c,
        c_BP_shifted as _shifted_bp_c,
        compute_varrho as _bp_reciprocal_weight_diagnostic,
        dual_level as _bp_dual_level,
        kappa_BP as _canonical_bp_kappa,
    )
except ModuleNotFoundError:  # direct execution from compute/lib
    from bp_koszul_conductor_engine import (
        BP_KAPPA_STATUS,
        K_BP_EXACT,
        K_BP_SHIFTED_EXACT,
        SHIFTED_BP_CONVENTION,
        STANDARD_BP_CONVENTION,
        UnverifiedBPInvariantError,
        K_BP as _canonical_bp_conductor,
        K_BP_shifted as _shifted_bp_conductor,
        c_BP as _canonical_bp_c,
        c_BP_shifted as _shifted_bp_c,
        compute_varrho as _bp_reciprocal_weight_diagnostic,
        dual_level as _bp_dual_level,
        kappa_BP as _canonical_bp_kappa,
    )


AFFINE_CONDUCTOR_HYPOTHESES: Tuple[str, ...] = (
    "noncritical_level_k_plus_h_dual_nonzero",
    "Sugawara_stress_tensor_defined",
    "Feigin_Frenkel_level_shift_stays_in_generic_lane",
    "finite_or_completed_bar_window",
)

AFFINE_CRITICAL_MISSING_HYPOTHESES: Tuple[str, ...] = AFFINE_CONDUCTOR_HYPOTHESES

AFFINE_NONCRITICAL_STATUS = "generic_affine_noncritical_conductor"
AFFINE_CRITICAL_STATUS = (
    "critical_Feigin_Frenkel_center_separate_not_generic_conductor"
)

VIRASORO_DUALITY_HYPOTHESES: Tuple[str, ...] = (
    "Virasoro_Koszul_duality_theorem_applies",
    "class_M_completed_or_finite_window_bar_lane",
    "stress_tensor_normalization_fixed",
)

VIRASORO_SHADOW_TOWER_HYPOTHESES: Tuple[str, ...] = (
    *VIRASORO_DUALITY_HYPOTHESES,
    "c_times_5c_plus_22_nonzero",
    "Zamolodchikov_norm_nonzero",
)

VIRASORO_SHADOW_TOWER_MISSING_AT_SINGULAR: Tuple[str, ...] = (
    "c_times_5c_plus_22_nonzero",
    "Zamolodchikov_norm_nonzero",
)

VIRASORO_EXCEPTIONAL_CHARGES: Dict[Fraction, str] = {
    Fraction(0): "uncurved_kappa_zero_shadow_tower_singular_dual_is_c_26",
    Fraction(-22, 5): "Yang_Lee_Zamolodchikov_norm_zero_shadow_tower_singular",
    Fraction(26): "critical_string_central_charge_dual_is_c_0_not_self_dual",
    Fraction(13): "Koszul_self_dual_fixed_point",
}


# ---------------------------------------------------------------------------
# Harmonic numbers  (C19: H_N = sum_{j=1}^{N} 1/j)
# ---------------------------------------------------------------------------

def harmonic(n: int) -> Fraction:
    """H_n = sum_{j=1}^{n} 1/j.  Exact Fraction."""
    if n < 0:
        raise ValueError(f"harmonic number undefined for n={n}")
    return sum(Fraction(1, j) for j in range(1, n + 1))


# ---------------------------------------------------------------------------
# Heisenberg  (C1, C10)
# ---------------------------------------------------------------------------

def heisenberg_c() -> Fraction:
    """Central charge of rank-1 Heisenberg at any level: c = 1."""
    return Fraction(1)


def heisenberg_kappa(k: Fraction) -> Fraction:
    """kappa(H_k) = k.  (C1)"""
    return Fraction(k)


def heisenberg_dual_kappa(k: Fraction) -> Fraction:
    """kappa(H_k^!) = -k.  Complementarity: kappa + kappa' = 0.  (C18)"""
    return -Fraction(k)


def heisenberg_K_cc() -> Fraction:
    """c + c' = 1 + 1 = 2 for Heisenberg (both sides c=1)."""
    return Fraction(2)


def heisenberg_K_kk(k: Fraction) -> Fraction:
    """K_kk = kappa + kappa' = 0.  (C18: KM/Heis/lattice/free)"""
    return heisenberg_kappa(k) + heisenberg_dual_kappa(k)


# ---------------------------------------------------------------------------
# Virasoro  (C2, C8, C11)
# ---------------------------------------------------------------------------

def virasoro_c(c: Fraction) -> Fraction:
    """Central charge c."""
    return Fraction(c)


def virasoro_dual_c(c: Fraction) -> Fraction:
    """Central charge of the theorem-scoped Koszul partner Vir_{26-c}.  (C8)"""
    return Fraction(26) - Fraction(c)


def virasoro_kappa(c: Fraction) -> Fraction:
    """kappa(Vir_c) = c/2.  (C2)"""
    return Fraction(c) / 2


def virasoro_dual_kappa(c: Fraction) -> Fraction:
    """kappa(Vir_{26-c}) = (26-c)/2."""
    return (Fraction(26) - Fraction(c)) / 2


def virasoro_K_cc(c: Fraction) -> Fraction:
    """c + c' = c + (26-c) = 26."""
    return virasoro_c(c) + virasoro_dual_c(c)


def virasoro_K_kk(c: Fraction) -> Fraction:
    """K_kk = kappa + kappa' = c/2 + (26-c)/2 = 13.  (C18)"""
    return virasoro_kappa(c) + virasoro_dual_kappa(c)


def virasoro_scope_report(c: Fraction) -> Dict[str, Any]:
    """Scope report for Virasoro duality and shadow-tower computations.

    The scalar conductor identity is valid as an algebra-level invariant.
    The object-level statement Vir_c^! = Vir_{26-c} is theorem-scoped, and
    the universal shadow-tower formula uses the nonsingular surface
    c(5c+22) != 0.
    """
    c = Fraction(c)
    c_dual = virasoro_dual_c(c)
    nonsingular_shadow = c != 0 and 5 * c + 22 != 0
    return {
        "family": "Virasoro",
        "central_charge": c,
        "dual_central_charge": c_dual,
        "duality_claim": "Vir_c^! = Vir_{26-c}",
        "duality_claim_requires_theorem": True,
        "duality_hypothesis_package": VIRASORO_DUALITY_HYPOTHESES,
        "kappa": virasoro_kappa(c),
        "kappa_dual": virasoro_dual_kappa(c),
        "K_kk": virasoro_K_kk(c),
        "self_dual": c == 13,
        "critical_string_central_charge": c == 26,
        "shadow_tower_formula_applies": nonsingular_shadow,
        "shadow_tower_hypothesis_package": (
            VIRASORO_SHADOW_TOWER_HYPOTHESES if nonsingular_shadow else tuple()
        ),
        "missing_shadow_tower_hypotheses": (
            tuple()
            if nonsingular_shadow
            else VIRASORO_SHADOW_TOWER_MISSING_AT_SINGULAR
        ),
        "S4_formula": "10/[c(5c+22)]" if nonsingular_shadow else None,
        "exceptional_status": VIRASORO_EXCEPTIONAL_CHARGES.get(
            c, "generic_or_nonexceptional_Virasoro_charge"
        ),
    }


# ---------------------------------------------------------------------------
# Affine Kac-Moody  V_k(g)  (C3, C9, C13)
# ---------------------------------------------------------------------------

def _km_is_critical(h_v: int, k: Fraction) -> bool:
    """Whether k is the affine critical level -h^v."""
    return Fraction(k) == -Fraction(h_v)


def _raise_if_km_critical(h_v: int, k: Fraction, formula_name: str) -> None:
    if _km_is_critical(h_v, k):
        raise ValueError(
            f"{formula_name} is a generic affine conductor formula; "
            "critical level k = -h^v belongs to the Feigin-Frenkel "
            "center lane and is not a Sugawara/KZ conductor point"
        )


def _km_scalar_kappa(dim_g: int, h_v: int, k: Fraction) -> Fraction:
    """Scalar kappa expression, including its critical zero."""
    k = Fraction(k)
    return Fraction(dim_g) * (k + Fraction(h_v)) / (2 * Fraction(h_v))


def km_level_scope(dim_g: int, h_v: int, k: Fraction) -> Dict[str, Any]:
    """Scope report for affine KM conductor computations.

    The scalar expression for kappa vanishes at k=-h^v, but that
    critical value is not a generic conductor/Koszul-duality point:
    Sugawara, KZ, and the non-critical bar diagonal package are absent.
    """
    k = Fraction(k)
    h_dual = Fraction(h_v)
    critical = _km_is_critical(h_v, k)
    kappa_scalar = _km_scalar_kappa(dim_g, h_v, k)
    kappa_dual_scalar = _km_scalar_kappa(dim_g, h_v, km_dual_level(k, h_v))
    return {
        "family": "affine_kac_moody",
        "level": k,
        "critical_level": -h_dual,
        "dim_g": dim_g,
        "h_dual": h_dual,
        "is_critical": critical,
        "generic_conductor_formula_applies": not critical,
        "central_charge_defined": not critical,
        "status": AFFINE_CRITICAL_STATUS if critical else AFFINE_NONCRITICAL_STATUS,
        "hypothesis_package": AFFINE_CONDUCTOR_HYPOTHESES if not critical else tuple(),
        "missing_hypotheses": (
            AFFINE_CRITICAL_MISSING_HYPOTHESES if critical else tuple()
        ),
        "kappa_scalar": kappa_scalar,
        "kappa_dual_scalar": kappa_dual_scalar,
        "K_kk_scalar_indicator": kappa_scalar + kappa_dual_scalar,
        "critical_scalar_kappa_vanishes": critical and kappa_scalar == 0,
        "ff_center_lane": critical,
    }


def km_c(dim_g: int, h_v: int, k: Fraction) -> Fraction:
    """c(V_k(g)) = k * dim(g) / (k + h^v).

    Sugawara formula.  k is the level (Fraction for exactness).
    Undefined at the critical level k = -h^v.
    """
    k = Fraction(k)
    _raise_if_km_critical(h_v, k, "km_c")
    return k * Fraction(dim_g) / (k + Fraction(h_v))


def km_dual_level(k: Fraction, h_v: int) -> Fraction:
    """Dual level k' = -k - 2*h^v."""
    return -Fraction(k) - 2 * Fraction(h_v)


def km_dual_c(dim_g: int, h_v: int, k: Fraction) -> Fraction:
    """c(V_{k'}(g)) where k' = -k - 2*h^v."""
    k_dual = km_dual_level(k, h_v)
    return km_c(dim_g, h_v, k_dual)


def km_kappa(dim_g: int, h_v: int, k: Fraction) -> Fraction:
    """kappa(V_k(g)) on the non-critical affine conductor lane.  (C3)"""
    k = Fraction(k)
    _raise_if_km_critical(h_v, k, "km_kappa")
    return _km_scalar_kappa(dim_g, h_v, k)


def km_dual_kappa(dim_g: int, h_v: int, k: Fraction) -> Fraction:
    """kappa at dual level k' = -k - 2*h^v."""
    k_dual = km_dual_level(k, h_v)
    return km_kappa(dim_g, h_v, k_dual)


def km_K_cc(dim_g: int, h_v: int, k: Fraction) -> Fraction:
    """c + c' for affine KM."""
    return km_c(dim_g, h_v, k) + km_dual_c(dim_g, h_v, k)


def km_K_kk(dim_g: int, h_v: int, k: Fraction) -> Fraction:
    """K_kk = kappa + kappa' = 0 for affine KM.  (C18)"""
    return km_kappa(dim_g, h_v, k) + km_dual_kappa(dim_g, h_v, k)


# ---------------------------------------------------------------------------
# Principal W_N algebras  (C4, C17, C19)
# ---------------------------------------------------------------------------

def wn_kappa(c: Fraction, n: int) -> Fraction:
    """kappa(W_N) = c * (H_N - 1).  (C4)

    H_N = sum_{j=1}^{N} 1/j.  (C19)
    NOT c * H_{N-1} -- that is B7, the WRONG form (AP136).
    """
    h_n = harmonic(n)
    return Fraction(c) * (h_n - Fraction(1))


def wn_dual_kappa(c: Fraction, c_dual: Fraction, n: int) -> Fraction:
    """kappa(W_N^!) at dual central charge c'."""
    return wn_kappa(c_dual, n)


def wn_K_kk(c: Fraction, c_dual: Fraction, n: int) -> Fraction:
    """K_kk = kappa(W_N, c) + kappa(W_N, c')."""
    return wn_kappa(c, n) + wn_dual_kappa(c, c_dual, n)


# For W_N the dual central charge depends on N.
# K_c(W_N) = c + c' = 4*N^3 - 2*N - 2.
# K_kk(W_N) = (H_N - 1) * K_c(W_N).

def wn_spin_set(n: int) -> Tuple[int, ...]:
    """Principal W_N strong-generator spin set {2, 3, ..., N}."""
    if n < 2:
        raise ValueError("W_N conductor lane requires N >= 2")
    return tuple(range(2, n + 1))


def wn_central_charge_conductor(n: int) -> Fraction:
    """K_c(W_N) = c(W_N) + c(W_N^!) = 4*N^3 - 2*N - 2."""
    if n < 2:
        raise ValueError("W_N conductor lane requires N >= 2")
    return Fraction(4 * n**3 - 2 * n - 2)


def wn_conductor_constant(n: int) -> Fraction:
    """Scalar K_kk(W_N) = kappa(W_N,c) + kappa(W_N,c').

    This is not the central-charge conductor K_c.  The relation is
    K_kk(W_N) = (H_N - 1) * K_c(W_N), with
    K_c(W_N) = 4*N^3 - 2*N - 2.
    """
    h_n = harmonic(n)
    factor = h_n - Fraction(1)
    if factor == 0:
        raise ValueError("W_1 has no Koszul conductor (trivial)")
    return wn_central_charge_conductor(n) * factor


def _wn_cc_sum(n: int) -> Fraction:
    """Backward-compatible alias for K_c(W_N) = c + c'."""
    return wn_central_charge_conductor(n)


# Precomputed W_N Koszul conductors K_kk for principal W-algebras.
# Derivation for each from c+c' and H_N-1:
#   K_kk(W_N) = (c + c') * (H_N - 1)

WN_CONDUCTORS: Dict[int, Fraction] = {
    n: wn_conductor_constant(n) for n in range(2, 6)
}

# W_N dual central charge: c'(W_N) = K_cc(W_N) - c
WN_CC_SUMS: Dict[int, Fraction] = {
    n: wn_central_charge_conductor(n) for n in range(2, 6)
}


def wn_dual_c(c: Fraction, n: int) -> Fraction:
    """Dual central charge for W_N family."""
    return wn_central_charge_conductor(n) - Fraction(c)


# ---------------------------------------------------------------------------
# Bershadsky-Polyakov  (C20, C31)
# ---------------------------------------------------------------------------

BP_DUALITY_HYPOTHESES: Tuple[str, ...] = (
    "subregular_sl3_DS_bar_transport",
    "self_transpose_orbit_(2,1)",
    "PBW_Koszul_locus",
    "finite_type_or_completed_Verdier_lane",
)

BP_STRONG_GENERATORS: Tuple[Tuple[str, Fraction, str], ...] = (
    ("J", Fraction(1), "bosonic"),
    ("G+", Fraction(3, 2), "bosonic"),
    ("G-", Fraction(3, 2), "bosonic"),
    ("T", Fraction(2), "bosonic"),
)


def _bp_is_critical(k: Fraction) -> bool:
    """Whether the BP level is the parent sl_3 critical level k=-3."""
    return Fraction(k) == Fraction(-3)


def bp_c(k: Fraction) -> Fraction:
    """Standard Bershadsky--Polyakov central charge.

    ``c_BP(k)=-(2k+3)(3k+1)/(k+3)`` and ``k'=-k-6``.
    """
    return _canonical_bp_c(Fraction(k))


def bp_c_shifted(k: Fraction) -> Fraction:
    """Secondary shifted-conformal-vector formula."""

    return _shifted_bp_c(Fraction(k))


def bp_dual_c(k: Fraction) -> Fraction:
    """c_BP at dual level k' = -k - 6."""
    return bp_c(_bp_dual_level(Fraction(k)))


def bp_K_cc(k: Fraction) -> Fraction:
    """Canonical standard-convention conductor ``K_cc(BP)=50``."""

    return _canonical_bp_conductor(Fraction(k))


def bp_K_cc_shifted(k: Fraction) -> Fraction:
    """Secondary shifted-formula conductor ``196``."""

    return _shifted_bp_conductor(Fraction(k))


def bp_kappa(k: Fraction) -> Fraction:
    """Signal the open BP genus-one curvature computation."""

    return _canonical_bp_kappa(Fraction(k))


def bp_K_kk(k: Fraction = Fraction(0)) -> Fraction:
    """Signal the open BP modular-characteristic companion sum."""

    k = Fraction(k)
    if _bp_is_critical(k):
        bp_c(k)
    raise UnverifiedBPInvariantError(BP_KAPPA_STATUS.resolution_obligation)


def bp_j_line_scalar(k: Fraction) -> Fraction:
    """BP Gaussian J-line scalar S_2^J = (2k+3)/3."""
    k = Fraction(k)
    return (2 * k + 3) / Fraction(3)


def bp_t_line_scalar(k: Fraction) -> Fraction:
    """BP Virasoro T-line scalar S_2^T = c_BP(k)/2."""
    return bp_c(k) / Fraction(2)


def bp_g_mixed_pairing(k: Fraction) -> Fraction:
    """BP even mixed pairing <G+,G-> = (k+1)(2k+3)."""
    k = Fraction(k)
    return (k + 1) * (2 * k + 3)


def bp_total_ds_conformal_shift(k: Fraction) -> Fraction:
    """Exact total shift ``c_BP(k)-c_aff(sl3,k)=-(6k+1)``."""

    k = Fraction(k)
    if _bp_is_critical(k):
        bp_c(k)
    return -(Fraction(6) * k + 1)


def bp_ds_ghost_leg_scalar(k: Fraction) -> Fraction:
    """Signal the open charged/neutral/improvement decomposition."""

    k = Fraction(k)
    if _bp_is_critical(k):
        bp_c(k)
    raise UnverifiedBPInvariantError(
        "decompose the exact BP DS conformal shift into charged ghosts, "
        "neutral fields, and conformal improvement"
    )


def bp_scope_report(k: Fraction) -> Dict[str, Any]:
    """Scope report for the Bershadsky-Polyakov conductor lane.

    BP is the subregular/minimal sl_3 Drinfeld-Sokolov branch
    W^k(sl_3, f_(2,1)), not the principal W_N branch.  The orbit is
    self-transpose.  Same-family Verdier--Koszul duality carries the
    subregular DS/bar transport package.  The fixed level ``k=-3`` is the
    common pole of both conformal-vector formulas, while both conductor
    identities live in the rational-function field.
    """
    k = Fraction(k)
    critical = _bp_is_critical(k)
    report: Dict[str, Any] = {
        "family": "Bershadsky-Polyakov",
        "presentation": "subregular_DS_W3^(2)",
        "parent_lie_algebra": "sl_3",
        "nilpotent_orbit_partition": (2, 1),
        "ds_orbit": "subregular/minimal",
        "is_principal_W_N": False,
        "strong_generators": BP_STRONG_GENERATORS,
        "dual_level": _bp_dual_level(k),
        "level_fixed_by_sigma": k == _bp_dual_level(k),
        "central_charge_defined": not critical,
        "self_transpose_orbit": True,
        "same_family_duality_claim": "BP_k^! ~= BP_{-k-6} under H_DS/bar",
        "duality_claim_requires_theorem": True,
        "duality_hypothesis_package": BP_DUALITY_HYPOTHESES,
        "real_level_self_dual_c_attained": False,
        "standard_convention": STANDARD_BP_CONVENTION.name,
        "standard_convention_status": STANDARD_BP_CONVENTION.status,
        "K_cc": K_BP_EXACT,
        "K_kappa": None,
        "anomaly_ratio": None,
        "kappa_status": BP_KAPPA_STATUS.status,
        "kappa_resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
        "reciprocal_weight_diagnostic": _bp_reciprocal_weight_diagnostic(),
        "shifted_convention": SHIFTED_BP_CONVENTION.name,
        "shifted_convention_status": SHIFTED_BP_CONVENTION.status,
        "shifted_K_cc": K_BP_SHIFTED_EXACT,
        "algebra_level_interpretation": "conditional-H_DS/bar",
        "missing_hypotheses": (
            ("k_plus_3_nonzero",) if critical else tuple()
        ),
    }
    if critical:
        report["shadow_lines"] = {
            "J": {"class": "G", "scalar": None},
            "T": {"class": "M", "scalar": None},
            "G_pairing": {"class": "mixed_even", "scalar": None},
            "full_kappa": {
                "scalar": None,
                "status": BP_KAPPA_STATUS.status,
            },
            "total_DS_conformal_shift": {"scalar": None},
            "DS_ghost_leg": {
                "presentation_dependent": True,
                "scalar": None,
                "status": "open_charged_neutral_improvement_decomposition",
            },
        }
        report["status"] = (
            "fixed_level_is_common_pole; conductors_are_rational_function_identities"
        )
    else:
        report["central_charge"] = bp_c(k)
        report["dual_central_charge"] = bp_dual_c(k)
        report["shifted_central_charge"] = bp_c_shifted(k)
        report["shifted_dual_central_charge"] = bp_c_shifted(
            _bp_dual_level(k)
        )
        report["shadow_lines"] = {
            "J": {
                "class": "G",
                "scalar": bp_j_line_scalar(k),
            },
            "T": {
                "class": "M",
                "scalar": bp_t_line_scalar(k),
                "conformal_convention": STANDARD_BP_CONVENTION.name,
            },
            "G_pairing": {
                "class": "mixed_even",
                "scalar": bp_g_mixed_pairing(k),
                "status": "presentation-dependent OPE scalar",
            },
            "full_kappa": {
                "scalar": None,
                "anomaly_ratio": None,
                "status": BP_KAPPA_STATUS.status,
                "resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
            },
            "total_DS_conformal_shift": {
                "scalar": bp_total_ds_conformal_shift(k),
                "status": "proved_exact_total_shift",
            },
            "DS_ghost_leg": {
                "presentation_dependent": True,
                "scalar": None,
                "status": "open_charged_neutral_improvement_decomposition",
            },
        }
        report["status"] = "standard_subregular_DS_central_lane_with_open_kappa"
    return report


# ---------------------------------------------------------------------------
# Fermionic bc system  (C5, C7)
# ---------------------------------------------------------------------------

def bc_c(lam: Fraction) -> Fraction:
    """c_bc(lambda) = 1 - 3*(2*lambda - 1)^2.  (C5)

    Checks: lambda=1/2 -> 1; lambda=2 -> -26.
    """
    lam = Fraction(lam)
    return 1 - 3 * (2 * lam - 1) ** 2


def bg_c(lam: Fraction) -> Fraction:
    """c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1).  (C6)

    Checks: lambda=1/2 -> -1; lambda=2 -> 26.
    """
    lam = Fraction(lam)
    return 2 * (6 * lam ** 2 - 6 * lam + 1)


def bc_bg_K_cc(lam: Fraction) -> Fraction:
    """c_bc + c_bg = 0.  (C7)"""
    return bc_c(lam) + bg_c(lam)


def bc_kappa(lam: Fraction) -> Fraction:
    """kappa for bc at weight lambda.

    For the bc system, kappa = c_bc/2 only when bc = Virasoro (lambda=2 gives
    c=-26, kappa=-13).  In general, bc is a free-field system, so
    kappa + kappa' = 0 (free family, C18).  And bc^! = bg at the same lambda,
    so kappa_bc + kappa_bg = 0.

    For free fields, kappa = c/2 does NOT hold generically.
    kappa(bc) = c_bc(lam) / 2 would give kappa + kappa' = (c_bc + c_bg)/2 = 0.
    This is consistent with C18 (free family -> K_kk = 0).

    Actually for rank-1 free-field systems, kappa IS c/2:
    Heisenberg: c=1, kappa=k (the LEVEL, not c/2).
    So kappa != c/2 for free fields in general.

    For the bc-bg pair, the monograph treats bc^! = bg (Koszul duality
    exchanges fermionic and bosonic ghosts).  The Koszul conductor is
    K_kk = kappa_bc + kappa_bg = 0 (free/ghost family).

    We store K_kk = 0 without committing to individual kappa values.
    """
    lam = Fraction(lam)
    return bc_c(lam) / 2


def bg_kappa(lam: Fraction) -> Fraction:
    """kappa for betagamma at weight lambda."""
    lam = Fraction(lam)
    return bg_c(lam) / 2


def bc_bg_K_kk(lam: Fraction) -> Fraction:
    """K_kk(bc-bg) = kappa_bc + kappa_bg = 0.  (C18: free family)"""
    return bc_kappa(lam) + bg_kappa(lam)


# ---------------------------------------------------------------------------
# Lattice VOA  V_L  (C18)
# ---------------------------------------------------------------------------

def lattice_c(rank: int) -> Fraction:
    """c(V_L) = rank(L) for an even lattice L."""
    return Fraction(rank)


def lattice_dual_c(rank: int) -> Fraction:
    """c(V_{L^!}) = rank(L) (same rank)."""
    return Fraction(rank)


def lattice_K_cc(rank: int) -> Fraction:
    """c + c' = 2 * rank."""
    return 2 * Fraction(rank)


def lattice_K_kk() -> Fraction:
    """K_kk = kappa + kappa' = 0 for lattice VOAs.  (C18)"""
    return Fraction(0)


# ---------------------------------------------------------------------------
# Master table
# ---------------------------------------------------------------------------

# Lie algebra data: (name, dim, h^v)
LIE_DATA: Dict[str, Tuple[int, int]] = {
    "sl2": (3, 2),
    "sl3": (8, 3),
    "so8": (28, 6),
    "g2": (14, 4),
    "f4": (52, 9),
    "e6": (78, 12),
    "e7": (133, 18),
    "e8": (248, 30),
}


def full_conductor_table(k_km: Fraction = Fraction(1),
                         c_vir: Fraction = Fraction(1),
                         c_w3: Fraction = Fraction(1),
                         lam_bc: Fraction = Fraction(2),
                         k_bp: Fraction = Fraction(1),
                         lattice_rank: int = 8,
                         ) -> Dict[str, Dict[str, Any]]:
    """Build the full Koszul conductor table for all families.

    Returns typed family packets.  Open numerical invariants appear as
    ``None`` together with a status and resolution obligation.
    """
    table = {}

    # Heisenberg
    k_heis = k_km  # use same level for convenience
    table["Heisenberg"] = {
        "c": heisenberg_c(),
        "c_dual": heisenberg_c(),
        "K_cc": heisenberg_K_cc(),
        "K_kk": heisenberg_K_kk(k_heis),
    }

    # Virasoro
    table["Virasoro"] = {
        "c": virasoro_c(c_vir),
        "c_dual": virasoro_dual_c(c_vir),
        "K_cc": virasoro_K_cc(c_vir),
        "kappa": virasoro_kappa(c_vir),
        "kappa_dual": virasoro_dual_kappa(c_vir),
        "K_kk": virasoro_K_kk(c_vir),
    }

    # Affine KM for each Lie algebra
    for name, (dim_g, h_v) in LIE_DATA.items():
        table[f"KM_{name}"] = {
            "c": km_c(dim_g, h_v, k_km),
            "c_dual": km_dual_c(dim_g, h_v, k_km),
            "K_cc": km_K_cc(dim_g, h_v, k_km),
            "kappa": km_kappa(dim_g, h_v, k_km),
            "kappa_dual": km_dual_kappa(dim_g, h_v, k_km),
            "K_kk": km_K_kk(dim_g, h_v, k_km),
        }

    # W_N for N=2,3
    for n in [2, 3]:
        if n in WN_CC_SUMS:
            cc = c_w3 if n == 3 else c_vir
            table[f"W_{n}"] = {
                "K_kk": WN_CONDUCTORS[n],
                "kappa": wn_kappa(cc, n),
                "kappa_dual": wn_kappa(wn_dual_c(cc, n), n),
                "K_cc": WN_CC_SUMS[n],
            }

    # Bershadsky-Polyakov
    table["BP"] = {
        "c": bp_c(k_bp),
        "c_dual": bp_dual_c(k_bp),
        "K_cc": bp_K_cc(k_bp),
        "kappa": None,
        "kappa_dual": None,
        "K_kk": None,
        "kappa_status": BP_KAPPA_STATUS.status,
        "kappa_resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
        "reciprocal_weight_diagnostic": _bp_reciprocal_weight_diagnostic(),
        "total_DS_conformal_shift": bp_total_ds_conformal_shift(k_bp),
    }

    # bc-betagamma
    table["bc"] = {
        "c": bc_c(lam_bc),
        "c_dual": bg_c(lam_bc),
        "K_cc": bc_bg_K_cc(lam_bc),
        "K_kk": bc_bg_K_kk(lam_bc),
    }
    table["betagamma"] = {
        "c": bg_c(lam_bc),
        "c_dual": bc_c(lam_bc),
        "K_cc": bc_bg_K_cc(lam_bc),
        "K_kk": bc_bg_K_kk(lam_bc),
    }

    # Lattice
    table["Lattice"] = {
        "c": lattice_c(lattice_rank),
        "c_dual": lattice_dual_c(lattice_rank),
        "K_cc": lattice_K_cc(lattice_rank),
        "K_kk": lattice_K_kk(),
    }

    return table
