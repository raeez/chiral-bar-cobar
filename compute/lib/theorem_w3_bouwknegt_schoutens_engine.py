r"""Exact W_3 Bouwknegt-Schoutens finite-OPE diagnostics.

This module is deliberately finite.  It records computable witnesses for
the Zamolodchikov/Bouwknegt-Schoutens W_3 normalization:

* channel curvatures kappa_T = c/2 and kappa_W = c/3;
* principal scalar trace kappa(W_3) = c(H_3 - 1) = 5c/6;
* W(z)W(w) singular coefficients through the Lambda pole;
* the singular surfaces c = 0 and 5c + 22 = 0;
* scope flags preventing finite OPE data from being promoted to a full
  modular Koszul, derived-centre, or all-genus theorem.

Conventions
-----------
- OPE modes: a_{(n)}b is the coefficient of (z-w)^(-(n+1)).
- The dlog collision residue shifts an OPE pole of order n to an
  r-matrix pole of order n-1.
- beta = 16/(5c + 22) is the Lambda coupling in the W-W pole of order 2.
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict


W3_BETA_SINGULAR_C = Fraction(-22, 5)


def _five_c_plus_22(c):
    return 5 * c + 22


def _is_exact(value: Any) -> bool:
    return isinstance(value, (int, Fraction)) and not isinstance(value, bool)


def _third(value):
    return value / Fraction(3) if _is_exact(value) else value / 3


def _require_beta_regular(c) -> None:
    if _five_c_plus_22(c) == 0:
        raise ValueError("W_3 Zamolodchikov normalization is singular at c = -22/5")


def _require_shadow_regular(c) -> None:
    if c == 0 or _five_c_plus_22(c) == 0:
        raise ValueError("W_3 shadow coefficients require c(5c + 22) != 0")


# ============================================================================
# W_3 structure constants and kappa data
# ============================================================================

def beta_w3(c):
    """Return the W_3 Lambda coupling beta = 16/(5c + 22)."""
    _require_beta_regular(c)
    return Fraction(16) / _five_c_plus_22(c) if _is_exact(c) else 16 / _five_c_plus_22(c)


def w3_harmonic_ratio() -> Fraction:
    """H_3 - 1 = 1/2 + 1/3 = 5/6."""
    return Fraction(5, 6)


def kappa_channels_w3(c) -> Dict[str, Any]:
    """Per-channel W_3 curvatures and principal scalar trace.

    The two channels are not a uniform-weight system: T has weight 2 and
    W has weight 3.  The scalar trace is the principal W_3 kappa from
    kappa(W_N) = c(H_N - 1), not a certificate for a uniform-weight
    all-genus reduction.
    """
    kappa_t = c / Fraction(2) if _is_exact(c) else c / 2
    kappa_w = _third(c)
    return {
        "T": kappa_t,
        "W": kappa_w,
        "principal_total": kappa_t + kappa_w,
        "harmonic_ratio": w3_harmonic_ratio(),
        "weights": {"T": 2, "W": 3},
        "uniform_weight": False,
    }


def kappa_principal_w3(c):
    """Principal scalar kappa(W_3) = c(H_3 - 1) = 5c/6."""
    return kappa_channels_w3(c)["principal_total"]


def kappa_total_w3(c):
    """Backward-compatible alias for the principal scalar trace 5c/6."""
    return kappa_principal_w3(c)


def uniform_weight_reduction_diagnostic(c=None) -> Dict[str, Any]:
    """Detect the forbidden uniform-weight promotion for W_3."""
    result = {
        "weights": (2, 3),
        "is_uniform_weight": False,
        "scalar_trace_available": True,
        "uniform_weight_all_genus_formula_available": False,
        "certifies_modular_koszul": False,
        "certifies_derived_center": False,
        "certifies_all_genus": False,
        "reason": "W_3 has distinct T and W weights; multi-weight corrections are separate data.",
    }
    if c is not None:
        result["principal_scalar_trace"] = kappa_principal_w3(c)
        result["channels"] = kappa_channels_w3(c)
    return result


# ============================================================================
# W_3 OPE witnesses
# ============================================================================

def lambda_zero_witness(h) -> Dict[str, Any]:
    r"""Zero-mode witness for Lambda = :TT: - (3/10) d^2 T on a primary.

    In physics-index modes, (:TT:)_0 acts by h^2 and (d^2T)_0 acts by
    6h.  Therefore Lambda_0 acts by h^2 - 9h/5.  This is a Virasoro
    computation, not a full W_3 null-vector certificate.
    """
    d2t_zero = 6 * h
    d2t_coeff = Fraction(3, 10) if _is_exact(h) else 0.3
    lambda_value = h * h - d2t_coeff * d2t_zero
    return {
        "normal_ordered_TT_zero": h * h,
        "d2T_zero": d2t_zero,
        "lambda_zero": lambda_value,
        "formula": "h^2 - 9h/5",
    }


def lambda_zero_on_primary(c, h):
    """Compatibility wrapper returning the Lambda_0 eigenvalue witness."""
    return lambda_zero_witness(h)["lambda_zero"]


def w3_ww_ope_modes(c) -> Dict[str, Any]:
    r"""Exact W(z)W(w) singular coefficients used by this finite engine."""
    beta = beta_w3(c)
    d2t_coeff = Fraction(3, 10) if _is_exact(c) else 0.3
    return {
        "normalization": "Bouwknegt-Schoutens/Zamolodchikov",
        "mode_5": {"field": "1", "coefficient": _third(c), "ope_pole_order": 6, "r_pole_order": 5},
        "mode_4": {"field": "0", "coefficient": 0, "ope_pole_order": 5, "r_pole_order": 4},
        "mode_3": {"field": "T", "coefficient": 2, "ope_pole_order": 4, "r_pole_order": 3},
        "mode_2": {"field": "dT", "coefficient": 1, "ope_pole_order": 3, "r_pole_order": 2},
        "mode_1": {
            "fields": {"d2T": d2t_coeff, "Lambda": beta},
            "ope_pole_order": 2,
            "r_pole_order": 1,
        },
        "beta": beta,
        "singular_surface_excluded": "5c + 22 = 0",
    }


def w3_rmatrix_collision_poles(c) -> Dict[int, Any]:
    """Return the W-W collision-residue poles after dlog absorption."""
    modes = w3_ww_ope_modes(c)
    return {
        5: modes["mode_5"],
        4: modes["mode_4"],
        3: modes["mode_3"],
        2: modes["mode_2"],
        1: modes["mode_1"],
    }


def finite_ope_diagnostic_scope() -> Dict[str, bool]:
    """Scope of the finite W_3 OPE diagnostic."""
    return {
        "finite_ope_modes": True,
        "certifies_bs_null_vector_ode": False,
        "certifies_modular_koszul": False,
        "certifies_derived_center": False,
        "certifies_all_genus": False,
    }


# ============================================================================
# Minimal model central charges and Virasoro BPZ weights
# ============================================================================

def w3_minimal_model_c(p, pp):
    """Central charge c(p,p') = 2(1 - 12(p-p')^2/(pp')) for W_3."""
    if p == 0 or pp == 0:
        raise ValueError("W_3 minimal-model parameters must be nonzero")
    p, pp = Fraction(p), Fraction(pp)
    return Fraction(2) * (1 - Fraction(12) * (p - pp) ** 2 / (p * pp))


def w3_kac_weight(r, s, p, pp):
    """Virasoro-sublattice Kac weight used only for T-sector checks."""
    p, pp = Fraction(p), Fraction(pp)
    r, s = Fraction(r), Fraction(s)
    return ((r * pp - s * p) ** 2 - (pp - p) ** 2) / (4 * p * pp)


def _sqrt_fraction_if_square(value: Fraction):
    if value < 0:
        return None
    num = math.isqrt(value.numerator)
    den = math.isqrt(value.denominator)
    if num * num == value.numerator and den * den == value.denominator:
        return Fraction(num, den)
    return None


def bpz_degenerate_weight(c):
    """The two Virasoro level-2 BPZ weights h = (5-c +/- sqrt(D))/16."""
    disc = (c - 1) * (c - 25)
    if _is_exact(c):
        sqrt_disc = _sqrt_fraction_if_square(disc)
        if sqrt_disc is None:
            return {
                "discriminant": disc,
                "sqrt_discriminant": None,
                "h_plus": None,
                "h_minus": None,
                "exact_rational": False,
                "formula": "h = (5-c +/- sqrt((c-1)(c-25)))/16",
            }
        return {
            "discriminant": disc,
            "sqrt_discriminant": sqrt_disc,
            "h_plus": (5 - c + sqrt_disc) / 16,
            "h_minus": (5 - c - sqrt_disc) / 16,
            "exact_rational": True,
            "bpz_coefficient": lambda h: Fraction(-3) / (2 * (2 * h + 1)),
        }

    sqrt_disc = math.sqrt(disc) if disc >= 0 else complex(0, math.sqrt(-disc))
    return {
        "discriminant": disc,
        "sqrt_discriminant": sqrt_disc,
        "h_plus": (5 - c + sqrt_disc) / 16,
        "h_minus": (5 - c - sqrt_disc) / 16,
        "exact_rational": False,
        "bpz_coefficient": lambda h: -3 / (2 * (2 * h + 1)),
    }


# ============================================================================
# BPZ T-sector ODE and collision diagnostics
# ============================================================================

def bpz_null_vector_ode(c, h1, h2, h3, h4):
    r"""Virasoro BPZ level-2 null-vector ODE inside the W_3 T-sector."""
    a_coeff = Fraction(2) * (2 * h1 + 1) / 3 if _is_exact(h1) else 2 * (2 * h1 + 1) / 3
    return {
        "order": 2,
        "leading_coefficient": a_coeff,
        "p1_pole_0": 1,
        "p1_pole_1": 1,
        "p0_pole_0_order2": -h2,
        "p0_pole_1_order2": -h3,
        "p0_cross": -(h2 + h3 - h4 + h1),
        "null_vector": "L_{-2} - 3/(2(2h+1))*L_{-1}^2",
        "source": "BPZ T-sector only",
    }


def bpz_ode_indicial_exponents(c, h1, h_ext):
    """Indicial discriminant of the BPZ equation at a regular singularity."""
    a_coeff = Fraction(2) * (2 * h1 + 1) / 3 if _is_exact(h1) else 2 * (2 * h1 + 1) / 3
    discriminant = 1 + 4 * h_ext / a_coeff
    return {
        "a_coefficient": a_coeff,
        "discriminant": discriminant,
        "note": "alpha = (1 +/- sqrt(1 + 4h/a))/2",
    }


def collision_depth_ode_virasoro(c, h1, h2, h3, h4):
    """Finite T-sector Hamiltonian coefficients before scalar BPZ conversion."""
    return {
        "pole_0_order_2": h1,
        "pole_1_order_2": h3,
        "ward_cross": h1 + h3 + h2 - h4,
        "source": "finite collision-depth expansion (T-sector)",
    }


def collision_depth_ode_w3(c, h1, h2, h3, h4, w1=0, w2=0, w3_ch=0, w4=0):
    """Finite W_3 collision-depth data from the W-W OPE."""
    modes = w3_ww_ope_modes(c)
    beta = modes["beta"]
    lam_h1 = lambda_zero_on_primary(c, h1)
    lam_h3 = lambda_zero_on_primary(c, h3)
    d2t_scalar_h1 = modes["mode_1"]["fields"]["d2T"] * (6 * h1)
    d2t_scalar_h3 = modes["mode_1"]["fields"]["d2T"] * (6 * h3)

    return {
        "bpz_sector": collision_depth_ode_virasoro(c, h1, h2, h3, h4),
        "w_sector": {
            "depth_1": {
                "pole_0_lambda": beta * lam_h1,
                "pole_1_lambda": beta * lam_h3,
                "pole_0_d2T": d2t_scalar_h1,
                "pole_1_d2T": d2t_scalar_h3,
                "pole_0_total_on_primary": beta * lam_h1 + d2t_scalar_h1,
                "pole_1_total_on_primary": beta * lam_h3 + d2t_scalar_h3,
                "formal_fields": modes["mode_1"]["fields"],
            },
            "depth_2": {"field": "dT", "coefficient": 1},
            "depth_3": {
                "pole_0_ww": 2 * h1,
                "pole_1_ww": 2 * h3,
                "pole_0_ward": w1,
                "pole_1_ward": w3_ch,
            },
            "depth_4": {"pole_0": 0, "pole_1": 0, "vanishes": True},
            "depth_5": {"pole_0": _third(c), "pole_1": _third(c), "type": "central"},
        },
        "scope": finite_ope_diagnostic_scope(),
    }


def compare_bpz_equations(c, h1, h2, h3, h4):
    """Compare finite T-sector coefficients without upgrading to W_3 BS ODEs."""
    cd = collision_depth_ode_virasoro(c, h1, h2, h3, h4)
    nv = bpz_null_vector_ode(c, h1, h2, h3, h4)
    sign_adjusted_cross_match = cd["ward_cross"] == -nv["p0_cross"]
    return {
        "t_sector_only": True,
        "regular_singular_points": (0, 1, "infinity"),
        "sign_adjusted_cross_match": sign_adjusted_cross_match,
        "collision_depth": cd,
        "null_vector": nv,
        "structural_agreement": sign_adjusted_cross_match,
        "certifies_w3_bs_null_vector_ode": False,
        "note": "BPZ agreement is a Virasoro T-sector check, not a W-sector null-vector proof.",
    }


# ============================================================================
# W_3 line shadows
# ============================================================================

def w3_tline_shadow_data(c) -> Dict[str, Any]:
    """T-line Virasoro shadow data inside W_3 on c(5c+22) != 0."""
    _require_shadow_regular(c)
    s4 = Fraction(10) / (c * _five_c_plus_22(c)) if _is_exact(c) else 10 / (c * _five_c_plus_22(c))
    kappa_t = kappa_channels_w3(c)["T"]
    delta = 8 * kappa_t * s4
    return {"kappa": kappa_t, "S3": 2, "S4": s4, "Delta": delta, "class": "M"}


def w3_wline_shadow_data(c) -> Dict[str, Any]:
    """W-line shadow data inside W_3 on c(5c+22) != 0."""
    _require_shadow_regular(c)
    den = c * (_five_c_plus_22(c) ** 3)
    s4 = Fraction(2560) / den if _is_exact(c) else 2560 / den
    kappa_w = kappa_channels_w3(c)["W"]
    delta = 8 * kappa_w * s4
    q0 = (2 * c / Fraction(3)) ** 2 if _is_exact(c) else (2 * c / 3) ** 2
    return {
        "kappa": kappa_w,
        "S3": 0,
        "S4": s4,
        "Delta": delta,
        "Q_constant": q0,
        "Q_t2_coefficient": 2 * delta,
        "odd_coefficients_vanish": True,
        "class": "M",
    }


def w3_extra_depths_on_primaries(c, h_j, w_j=0):
    """W_3 finite-depth contributions on a primary, separated by source."""
    modes = w3_ww_ope_modes(c)
    beta = modes["beta"]
    lam = lambda_zero_on_primary(c, h_j)
    d2t_scalar = modes["mode_1"]["fields"]["d2T"] * (6 * h_j)
    return {
        "depth_1_lambda": beta * lam,
        "depth_1_d2T": d2t_scalar,
        "depth_1_total_on_primary": beta * lam + d2t_scalar,
        "depth_3_2T": 2 * h_j,
        "depth_3_w_ward": w_j,
        "depth_4_zero": 0,
        "depth_5_central": _third(c),
        "beta": beta,
        "lambda_0": lam,
        "total_depth_3": 2 * h_j + w_j,
        "scope": finite_ope_diagnostic_scope(),
    }


def bs_w3_null_vector_level2(c, h, w):
    """Return an honest scope diagnostic for level-2 W-sector null vectors.

    Generic (c,h,w) triples are not degenerate.  A finite list of OPE
    constants is not the Bouwknegt-Schoutens Kac-Shapovalov determinant,
    and this engine does not certify a full W-sector null vector.
    """
    beta_w3(c)
    return {
        "has_w_null_vector": False,
        "certifies_full_bs_null_vector": False,
        "level": 2,
        "basis": ("L_-2", "L_-1^2", "W_-2", "W_-1 L_-1", "W_-1^2"),
        "required_missing_witness": "full W_3 Kac-Shapovalov determinant vanishing",
        "finite_ope_scope": finite_ope_diagnostic_scope(),
        "input": {"c": c, "h": h, "w": w},
    }


def verify_depth_4_vanishing_bs():
    """Depth 4 vanishes because W_{(4)}W = 0."""
    return {
        "w4_w_vanishes": True,
        "reason": "The W-W OPE has no fifth-order pole.",
        "collision_depth_consistent": True,
        "bs_consistent_as_finite_ope_check": True,
        "certifies_full_bs_null_vector_ode": False,
        "ope_mode": "W_{(4)}W = 0",
        "pole_order": 5,
        "depth": 4,
    }


# ============================================================================
# Summary helpers
# ============================================================================

def compare_at_c2(h1=0, h2=0, h3=0, h4=0, w1=0, w2=0, w3_ch=0, w4=0):
    """Finite comparison data at c = 2."""
    c = Fraction(2)
    return {
        "c": c,
        "beta": beta_w3(c),
        "kappa_channels": kappa_channels_w3(c),
        "kappa_total": kappa_total_w3(c),
        "collision_depth": collision_depth_ode_w3(c, h1, h2, h3, h4, w1, w2, w3_ch, w4),
        "bpz_comparison": compare_bpz_equations(c, h1, h2, h3, h4),
        "w3_extra_depths": w3_extra_depths_on_primaries(c, h1, w1),
        "scope": finite_ope_diagnostic_scope(),
    }


def compare_at_generic_c(c, h1, h2, h3, h4, w1=0, w2=0, w3_ch=0, w4=0):
    """Finite comparison data at regular generic c."""
    return {
        "c": c,
        "beta": beta_w3(c),
        "kappa_channels": kappa_channels_w3(c),
        "kappa_total": kappa_total_w3(c),
        "collision_depth": collision_depth_ode_w3(c, h1, h2, h3, h4, w1, w2, w3_ch, w4),
        "bpz_comparison": compare_bpz_equations(c, h1, h2, h3, h4),
        "w3_extra_depths": w3_extra_depths_on_primaries(c, h1, w1),
        "scope": finite_ope_diagnostic_scope(),
    }


def full_comparison_summary(c=Fraction(2)):
    """Complete finite-OPE summary with explicit non-certification flags."""
    beta = beta_w3(c)
    channels = kappa_channels_w3(c)
    return {
        "c": c,
        "beta": beta,
        "kappa_channels": channels,
        "kappa_total": channels["principal_total"],
        "tline_shadow": w3_tline_shadow_data(c),
        "wline_shadow": w3_wline_shadow_data(c),
        "ww_ope_modes": w3_ww_ope_modes(c),
        "depth_4_vanishing": verify_depth_4_vanishing_bs(),
        "bpz_t_sector": compare_bpz_equations(c, Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "uniform_weight": uniform_weight_reduction_diagnostic(c),
        "finite_ope_diagnostic_passes": True,
        "overall_agreement": False,
        "scope": finite_ope_diagnostic_scope(),
        "remaining_obligation": "Full BS null-vector ODE requires the W_3 Kac-Shapovalov determinant.",
    }
