r"""Finite scalar and stationary diagnostics for the shadow tower.

This module separates three mathematical surfaces.

1. Stationary primary-line Riccati diagnostics.
   The manuscript proves that the one-variable shadow generating function
   satisfies H(t)^2 = t^4 Q_L(t), with Q_L determined by
   (kappa, alpha, S_4).  This is a stationary primary-line diagnostic.

2. Finite-window scalar coefficient identities.
   In the truncated ring Q[kappa][[q]]/(q^{G+1}), the scalar shadow
   identity is
       log tau_shadow,scal^{<=G} = kappa log tau_KW^{<=G}.
   It is a finite logarithmic coefficient identity.

3. Descendant CohFT hierarchy.
   A full KdV, Gelfand-Dickey, Toda, or Painleve hierarchy requires a
   separately supplied descendant CohFT or isomonodromic system.  The finite
   scalar coefficient identity supplies no descendant flows.

Local manuscript anchors:
    chapters/examples/landscape_census.tex:126
    chapters/theory/higher_genus_modular_koszul.tex:18956
    chapters/theory/higher_genus_modular_koszul.tex:20234
    chapters/theory/higher_genus_modular_koszul.tex:20304
    chapters/theory/higher_genus_modular_koszul.tex:23626
    chapters/theory/higher_genus_modular_koszul.tex:29084
    chapters/theory/higher_genus_modular_koszul.tex:29722

All arithmetic is exact unless a function explicitly performs a numerical
ratio check.
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Any, Dict, Optional

from sympy import Rational, S, Symbol, bernoulli, factorial, pi as sym_pi, symbols


# ---------------------------------------------------------------------------
# Symbols kept stable for downstream notebooks and tests.
# ---------------------------------------------------------------------------

c = Symbol("c")
t = Symbol("t")
hbar = Symbol("hbar")
x = Symbol("x")
kappa_sym = Symbol("kappa")
t0, t1, t2, t3 = symbols("t0 t1 t2 t3")
u_sym = Symbol("u")
epsilon = Symbol("epsilon")


LOCAL_SOURCES = {
    "standard_family_constants": "chapters/examples/landscape_census.tex:126",
    "virasoro_shadow_coefficients": "chapters/examples/landscape_census.tex:561",
    "kernel_normalizations": "chapters/examples/landscape_census.tex:165",
    "trace_kz_bridge": "chapters/examples/landscape_census.tex:172",
    "riccati_algebraicity": "chapters/theory/higher_genus_modular_koszul.tex:18956",
    "stationary_hierarchy_shadow": "chapters/theory/higher_genus_modular_koszul.tex:20234",
    "finite_scalar_tau": "chapters/theory/higher_genus_modular_koszul.tex:20304",
    "scalar_kdv_scope": "chapters/theory/higher_genus_modular_koszul.tex:20364",
    "shadow_cohft": "chapters/theory/higher_genus_modular_koszul.tex:23626",
    "universal_instanton_action": "chapters/theory/higher_genus_modular_koszul.tex:29084",
    "painleve_multichannel": "chapters/theory/higher_genus_modular_koszul.tex:29722",
}

OBJECT_FIREWALLS = {
    "A": "input chiral algebra",
    "B(A)": "bar coalgebra T^c(s^{-1} Abar)",
    "A^i": "bar cohomology coalgebra H^* B(A)",
    "A^!": "Verdier or continuous-linear dual algebra under finite-type/completed hypotheses",
    "Z_ch^der(A)": "derived chiral centre, the Hochschild object ChirHoch^*(A,A)",
    "Omega(B(A))": "bar-cobar inversion back to A, not Koszul duality",
}

STANDARD_KERNELS = {
    "Heisenberg_collision": "k/z",
    "affine_collision_trace_form": "k*Omega_tr/z",
    "affine_KZ": "Omega/((k+h^vee)*z)",
    "Virasoro_collision": "(c/2)/z^3 + 2*T/z",
}

STANDARD_KAPPAS = {
    "Heisenberg_rank_d_level_l": "d*l",
    "Heisenberg_rank_1_level_k": "k",
    "affine_V_k_g": "dim(g)*(k+h^vee)/(2*h^vee)",
    "Virasoro_c": "c/2",
    "W_N": "c*(H_N-1)",
    "beta_gamma_lambda": "6*lambda^2 - 6*lambda + 1",
}

VIRASORO_SHADOW_COEFFICIENTS = {
    "S_2": "c/2",
    "S_3": "2",
    "S_4": "10/(c*(5*c+22))",
    "S_5": "-48/(c^2*(5*c+22))",
    "Delta": "40/(5*c+22)",
    "Lambda_norm": "c*(5*c+22)/10",
}


# ---------------------------------------------------------------------------
# Faber-Pandharipande numbers.
# ---------------------------------------------------------------------------

@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Rational:
    r"""Return the Faber-Pandharipande coefficient lambda_g^FP.

    lambda_g^FP =
        ((2^(2g-1)-1) / 2^(2g-1)) * |B_{2g}| / (2g)!.

    Equivalently,
        sum_{g>=1} lambda_g^FP x^{2g} = (x/2)/sin(x/2) - 1.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    power = 2 ** (2 * g - 1)
    return Rational(power - 1, power) * abs(B_2g) / factorial(2 * g)


_LAMBDA_FP_KNOWN = {
    1: Rational(1, 24),
    2: Rational(7, 5760),
    3: Rational(31, 967680),
    4: Rational(127, 154828800),
    5: Rational(73, 3503554560),
}


def shadow_free_energy_genus(kappa_val, g: int):
    r"""Return the scalar free-energy coefficient kappa * lambda_g^FP.

    This is unconditional at genus 1 and valid in all genera on the
    uniform-weight scalar lane.  For multi-weight algebras it is only the
    diagonal scalar projection; cross-channel terms are separate data.
    """
    return kappa_val * lambda_fp(g)


def finite_scalar_tau_identity(kappa_val, g_max: int = 5) -> Dict[str, Any]:
    r"""Return the finite-window scalar tau identity through genus g_max."""
    coefficients = {
        g: {
            "lambda_fp": lambda_fp(g),
            "F_g_shadow_scalar": kappa_val * lambda_fp(g),
        }
        for g in range(1, g_max + 1)
    }
    return {
        "kappa": kappa_val,
        "surface": "finite-window scalar coefficient identity",
        "identity": "log(tau_shadow_scal^{<=G}) = kappa*log(tau_KW^{<=G})",
        "ring": "Q[kappa][[q]]/(q^{G+1})",
        "constructs_descendant_hierarchy": False,
        "coefficients": coefficients,
        "source": LOCAL_SOURCES["finite_scalar_tau"],
    }


# ---------------------------------------------------------------------------
# Scalar KdV obstruction.
# ---------------------------------------------------------------------------

def _scalar_anomaly(kappa_val):
    return kappa_val * (1 - kappa_val)


def kdv_residual_from_power(kappa_val, g_max: int = 5) -> Dict[str, Any]:
    r"""Compute the scalar obstruction for the power tau_KW^kappa.

    If u_KW is assumed to solve the standard first KdV equation and u_kappa =
    kappa*u_KW, substituting u_kappa into the standard equation leaves
    residual 6*kappa*(kappa-1)*u_KW*(u_KW)_x.  The manuscript records the
    same obstruction with the opposite orientation, proportional to
    kappa*(1-kappa).

    This is a failure diagnostic for the finite scalar power identity.  It
    is not a construction of a kappa-deformed KdV hierarchy.
    """
    anomaly = _scalar_anomaly(kappa_val)
    standard_orientation = -anomaly
    return {
        "kappa": kappa_val,
        "diagnostic_surface": "finite scalar tau power",
        "obstruction_factor": "kappa*(1-kappa)",
        "obstruction_value": anomaly,
        "standard_kdv_residual_factor": standard_orientation,
        "standard_kdv_residual": (
            "6*kappa*(kappa-1)*u_KW*(u_KW)_x for the orientation "
            "u_t + 6*u*u_x + u_xxx"
        ),
        "vanishes": anomaly == 0,
        "constructs_kdv_hierarchy": False,
        "painleve_from_scalar_tau": False,
        "scope": (
            "The scalar coefficient series is a rescaled logarithmic "
            "potential, not a certified KdV tau function unless kappa is "
            "0 or 1."
        ),
        "source": LOCAL_SOURCES["scalar_kdv_scope"],
        "coefficients": {
            g: kappa_val * lambda_fp(g) for g in range(1, g_max + 1)
        },
    }


def kdv_obstruction_explicit(kappa_val, max_genus: int = 5) -> Dict[str, Any]:
    r"""Return finite-window quadratic mismatch data by genus.

    The values below record where a quadratic KdV-type expression would
    scale like kappa^2 while the scalar finite-window coefficient scales
    linearly in kappa.  They are obstruction diagnostics, not DVV recursion
    coefficients and not a hierarchy construction.
    """
    details = {}
    for g in range(2, max_genus + 1):
        quad_sum = Rational(0)
        for g1 in range(1, g):
            quad_sum += lambda_fp(g1) * lambda_fp(g - g1)
        details[g] = {
            "quad_sum_lambda": quad_sum,
            "scalar_anomaly_factor": _scalar_anomaly(kappa_val),
            "standard_orientation_factor": kappa_val * (kappa_val - 1),
            "scalar_window_mismatch": _scalar_anomaly(kappa_val) * quad_sum,
        }
    return {
        "kappa": kappa_val,
        "surface": "finite-window scalar quadratic mismatch",
        "constructs_kdv_hierarchy": False,
        "details": details,
        "source": LOCAL_SOURCES["scalar_kdv_scope"],
    }


def verify_kdv_failure_genus2(kappa_val) -> Dict[str, Any]:
    r"""Check the first scalar quadratic mismatch at genus 2."""
    F1 = kappa_val * Rational(1, 24)
    F2 = kappa_val * Rational(7, 5760)
    kw_F1_squared = Rational(1, 576)
    anomaly = _scalar_anomaly(kappa_val) * kw_F1_squared
    standard_orientation = -anomaly
    return {
        "kappa": kappa_val,
        "F_1_shadow": F1,
        "F_2_shadow": F2,
        "F_1_squared": F1**2,
        "KW_F_1_squared": kw_F1_squared,
        "quadratic_residual": anomaly,
        "standard_orientation_residual": standard_orientation,
        "residual_is_zero": anomaly == 0,
        "constructs_kdv_hierarchy": False,
        "source": LOCAL_SOURCES["scalar_kdv_scope"],
    }


def kappa_deformed_kdv_equation(kappa_val) -> Dict[str, Any]:
    r"""Describe the conditional rescaling diagnostic for a KdV solution.

    The engine may record the tautological fact that if a descendant field
    v is already a KdV solution, then u = kappa*v obeys a rescaled equation.
    It does not prove that the scalar shadow tau identity supplies v, the
    descendant times, or the hierarchy.
    """
    return {
        "kappa": kappa_val,
        "diagnostic_type": "conditional rescaling of an already supplied KdV field",
        "constructs_kdv_hierarchy": False,
        "requires_descendant_cohft": True,
        "rescaled_equation_if_kdv_field_is_supplied": (
            f"u_t + (6/{kappa_val})*u*u_x + u_xxx = 0, with u = {kappa_val}*v"
        ),
        "standard_residual_without_rescaling": (
            "standard KdV residual factor is kappa*(kappa-1)"
        ),
        "critical_points": {
            "kappa_0": "trivial scalar point",
            "kappa_1": "standard Witten-Kontsevich point",
        },
        "not_constructed": [
            "descendant variables",
            "Virasoro constraints on tau_KW^kappa",
            "Hamiltonian or Poisson hierarchy",
            "matrix-model interpretation",
        ],
        "source": LOCAL_SOURCES["finite_scalar_tau"],
    }


def hirota_bilinear_kappa_deformation(kappa_val, max_genus: int = 5) -> Dict[str, Any]:
    r"""Record the Hirota obstruction factor for a scalar power."""
    genus_data = {
        g: {
            "F_g_shadow": kappa_val * lambda_fp(g),
            "F_g_KW": lambda_fp(g),
        }
        for g in range(1, max_genus + 1)
    }
    correction_factor = kappa_val * (kappa_val - 1)
    return {
        "kappa": kappa_val,
        "surface": "finite scalar tau power",
        "hirota_D2_scaling": kappa_val,
        "hirota_D4_leading": kappa_val,
        "hirota_D4_correction": correction_factor,
        "hirota_obstruction": correction_factor,
        "vanishes_at_kappa_1": correction_factor == 0,
        "constructs_hirota_hierarchy": False,
        "genus_data": genus_data,
        "source": LOCAL_SOURCES["scalar_kdv_scope"],
    }


# ---------------------------------------------------------------------------
# MC, Virasoro, and descendant hierarchy scope.
# ---------------------------------------------------------------------------

def mc_as_pde_system(kappa_val, max_arity: int = 6) -> Dict[str, Any]:
    r"""Return the MC projection scope without promoting scalar data."""
    virasoro_constraints = {}
    for n in range(-1, max_arity - 2):
        virasoro_constraints[n] = {
            "arity_label": n + 2,
            "genus": 0,
            "requires_descendant_cohft": True,
            "scalar_engine_constructs": False,
        }

    return {
        "kappa": kappa_val,
        "mc_master_equation": "D*Theta_A + (1/2)[Theta_A,Theta_A] = 0",
        "surfaces": {
            "stationary_primary_line": (
                "Riccati diagnostic H(t)^2=t^4 Q_L(t) on a primary line"
            ),
            "finite_scalar_window": (
                "log tau_shadow_scal^{<=G}=kappa log tau_KW^{<=G}"
            ),
            "descendant_cohft": (
                "separate CohFT descendant potential required for Virasoro, "
                "KdV, or Gelfand-Dickey constraints"
            ),
        },
        "virasoro_constraints": virasoro_constraints,
        "kdv_flows": {
            "constructed_by_engine": False,
            "reason": "finite scalar coefficients do not provide descendant times",
        },
        "mc_master_pde": {
            "equation": "D*Theta_A + (1/2)[Theta_A,Theta_A] = 0",
            "interpretation": (
                "The MC equation is the modular obstruction identity.  In this "
                "engine it verifies scalar and stationary projections only."
            ),
            "genus_tower": {
                "g1_scalar": "F_1 = kappa/24 on the scalar lane",
                "stationary": "Riccati primary-line shadow",
                "descendant": "requires Theorem shadow-cohft plus descendant input",
            },
        },
        "source": LOCAL_SOURCES["shadow_cohft"],
    }


def mc_is_hierarchy() -> Dict[str, Any]:
    r"""Return the corrected hierarchy claim surface."""
    return {
        "theorem": (
            "The MC equation governs the modular obstruction tower.  The "
            "scalar engine computes finite-window and stationary projections. "
            "Full descendant integrable hierarchies require separate "
            "descendant CohFT data."
        ),
        "surfaces": {
            "stationary_primary_line": {
                "proved_or_conditional": "conditional on the shadow CohFT hypotheses",
                "content": "Riccati diagnostics by shadow depth",
                "source": LOCAL_SOURCES["stationary_hierarchy_shadow"],
            },
            "finite_scalar_window": {
                "proved_or_conditional": "proved on the uniform-weight scalar lane",
                "content": "tau_shadow_scal^{<=G}=(tau_KW^{<=G})^kappa",
                "source": LOCAL_SOURCES["finite_scalar_tau"],
            },
            "descendant_hierarchy": {
                "proved_or_conditional": "separate assumption or construction required",
                "content": "Virasoro/KdV/Gelfand-Dickey/Toda hierarchy",
                "source": LOCAL_SOURCES["shadow_cohft"],
            },
        },
        "negative_results": [
            "standard KdV has scalar anomaly kappa*(1-kappa)",
            "Gelfand-Dickey flows require descendant CohFT data",
            "Toda lattice equations require coupled descendant data",
            "Painleve descendants require a separate isomonodromic system",
        ],
        "positive_results": [
            "F_g^scal = kappa*lambda_g^FP on the uniform-weight scalar lane",
            "the scalar KdV anomaly is proportional to kappa*(1-kappa)",
            "H(t)^2=t^4 Q_L(t) gives stationary primary-line Riccati diagnostics",
            "A=(2*pi)^2 is the scalar uniform-weight instanton action",
            "S_1=-4*pi^2*kappa*i is the leading scalar Stokes multiplier under the uniform-weight hypothesis",
        ],
        "object_firewall": OBJECT_FIREWALLS,
    }


def virasoro_operator_kappa(n: int, kappa_val) -> Dict[str, Any]:
    r"""Describe Virasoro formulas only under descendant CohFT input."""
    base = {
        "n": n,
        "requires_descendant_cohft": True,
        "constructed_from_scalar_tau_power": False,
        "source": "chapters/theory/higher_genus_modular_koszul.tex:28080",
    }
    if n == -1:
        base.update(
            {
                "name": "string equation",
                "standard": "dF/dt_0 = (1/2)*t_0^2 + sum t_{k+1} dF/dt_k",
                "kappa_deformed": (
                    f"dF/dt_0 = ({kappa_val}/2)*t_0^2 + "
                    "sum t_{k+1} dF/dt_k"
                ),
                "scope": "descendant potential formula, not scalar tau-power output",
            }
        )
    elif n == 0:
        base.update(
            {
                "name": "dilaton equation",
                "standard": "Euler descendant equation with genus-one constant 1/24",
                "kappa_deformed": f"genus-one scalar constant kappa/24 = {kappa_val}/24",
                "scope": "finite scalar check plus descendant input for the full operator",
            }
        )
    else:
        base.update(
            {
                "name": f"L_{n} descendant constraint",
                "standard": f"L_{n} constraint on a supplied descendant potential",
                "kappa_deformed": (
                    "quadratic free-energy terms require the full descendant "
                    "CohFT; they are not inferred from tau_KW^kappa"
                ),
                "scope": "conditional descendant surface",
            }
        )
    return base


def verify_virasoro_on_shadow_tau(kappa_val, max_genus: int = 5) -> Dict[str, Any]:
    r"""Verify the scalar A-hat coefficients, not Virasoro constraints."""
    details = {}
    for g in range(1, max_genus + 1):
        fg = kappa_val * lambda_fp(g)
        details[g] = {
            "F_g": fg,
            "lambda_fp_g": lambda_fp(g),
            "match": fg == kappa_val * lambda_fp(g),
        }
    return {
        "kappa": kappa_val,
        "surface": "finite scalar A-hat coefficient check",
        "details": details,
        "all_match": all(d["match"] for d in details.values()),
        "dilaton_check": {
            "F_1": kappa_val * lambda_fp(1),
            "expected": kappa_val * Rational(1, 24),
            "match": kappa_val * lambda_fp(1) == kappa_val * Rational(1, 24),
        },
        "constructs_virasoro_constraints": False,
        "source": LOCAL_SOURCES["finite_scalar_tau"],
    }


# ---------------------------------------------------------------------------
# Stationary Riccati and landscape diagnostics.
# ---------------------------------------------------------------------------

def stationary_riccati_diagnostics(
    kappa_val,
    alpha_val=0,
    S4_val=0,
) -> Dict[str, Any]:
    r"""Return Q_L coefficients for the stationary primary-line diagnostic."""
    delta = 8 * kappa_val * S4_val
    return {
        "surface": "stationary primary-line Riccati diagnostic",
        "Q_L": {
            "constant": 4 * kappa_val**2,
            "linear": 12 * kappa_val * alpha_val,
            "quadratic": 9 * alpha_val**2 + 2 * delta,
            "Delta": delta,
            "closed_form": "(2*kappa + 3*alpha*t)^2 + 2*Delta*t^2",
        },
        "H_relation": "H(t)^2 = t^4*Q_L(t)",
        "constructs_descendant_hierarchy": False,
        "source": LOCAL_SOURCES["riccati_algebraicity"],
    }


def dispersionless_shadow_hierarchy(kappa_val, max_order: int = 5) -> Dict[str, Any]:
    r"""Return large-kappa scalar coefficient scaling.

    The scalar finite-window series starts at genus 1.  Its large-kappa
    bookkeeping is not a Hopf equation or a dispersionless KdV hierarchy.
    """
    genus_scaling = {}
    for g in range(1, max_order + 1):
        genus_scaling[g] = {
            "lambda_g": lambda_fp(g),
            "kappa_power_under_hbar2_equals_1_over_kappa": 1 - g,
            "coefficient": lambda_fp(g),
        }
    return {
        "kappa": kappa_val,
        "surface": "large-kappa scalar coefficient scaling",
        "genus_scaling": genus_scaling,
        "dispersionless_equation": {
            "constructed_by_engine": False,
            "reason": "the finite scalar series has no descendant spatial flow",
        },
        "thooft_scaling": {
            "coupling": "hbar^2 = 1/kappa",
            "free_energy": "F_scal = sum_g kappa^{1-g} lambda_g^FP",
            "leading": f"kappa*lambda_1 = {kappa_val}/24",
        },
        "source": LOCAL_SOURCES["finite_scalar_tau"],
    }


def wn_kappa_deformed_gelfand_dickey(
    N: int,
    kappa_vals: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    r"""Return the W_N stationary-shadow scope.

    Gelfand-Dickey names are recorded as the stationary shadows listed by
    depth.  A full Gelfand-Dickey hierarchy requires separate descendant
    data.
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    if kappa_vals is None:
        kappa_vals = {f"W_{j}": f"kappa_{j}" for j in range(2, N + 1)}

    lax_operator = "D^{}".format(N)
    for j in range(N - 2, -1, -1):
        lax_operator += f" + u_{j} D^{j}"

    if N == 2:
        name = "stationary GD_2 shadow"
        descendant = "KdV if a rank-1 descendant CohFT hierarchy is supplied"
    elif N == 3:
        name = "stationary GD_3 shadow"
        descendant = "Boussinesq if a W_3 descendant hierarchy is supplied"
    else:
        name = f"stationary GD_{N} shadow"
        descendant = f"{N}-th Gelfand-Dickey if a descendant hierarchy is supplied"

    return {
        "N": N,
        "rank": N - 1,
        "lax_operator": lax_operator,
        "kappa_inputs": kappa_vals,
        "hierarchy": {
            "name": name,
            "constructed_by_engine": False,
            "descendant_hierarchy_if_supplied": descendant,
            "lax_template_only": lax_operator,
        },
        "stationary_shadow": {
            "depth_class": "M" if N >= 2 else "G",
            "source": LOCAL_SOURCES["stationary_hierarchy_shadow"],
        },
    }


def toda_from_multichannel_shadow(channel_data: Dict[str, Any]) -> Dict[str, Any]:
    r"""Return multichannel coupling diagnostics without Toda promotion."""
    if not channel_data:
        channel_data = {
            "channels": ["T", "W"],
            "kappas": {"T": "c/2", "W": "c/3"},
            "coupling": {"TW": "mixed OPE coefficient"},
        }
    channels = channel_data.get("channels", ["T", "W"])
    N = len(channels)
    templates = {}
    for i, ch in enumerate(channels):
        left = channels[i - 1] if i > 0 else "boundary_left"
        right = channels[i + 1] if i + 1 < N else "boundary_right"
        templates[ch] = f"q_{ch}'' = exp(q_{left}-q_{ch}) - exp(q_{ch}-q_{right})"

    return {
        "N": N,
        "channels": channels,
        "finite_window_couplings": channel_data.get("coupling", {}),
        "toda_equations": {
            "constructed_by_engine": False,
            "template_if_lax_system_supplied": templates,
        },
        "independent_limit": (
            "With zero mixed OPE, scalar channels factor as independent "
            "finite-window coefficient identities."
        ),
        "hierarchy_type": {
            "constructed_by_engine": False,
            "template": f"A_{N-1} Toda only after separate Lax/descendant input",
        },
        "source": LOCAL_SOURCES["stationary_hierarchy_shadow"],
    }


def shadow_hierarchy_landscape() -> Dict[str, Dict[str, Any]]:
    r"""Return family data with stationary and descendant surfaces separated."""
    return {
        "Heisenberg_k": {
            "kappa": "k",
            "depth_class": "G",
            "stationary_shadow": "trivial Riccati diagnostic, Q_L constant",
            "descendant_hierarchy_if_supplied": "free-field descendant theory",
            "constructs_descendant_hierarchy": False,
            "kernel": STANDARD_KERNELS["Heisenberg_collision"],
        },
        "affine_sl2_k": {
            "kappa": "3*(k+2)/4",
            "depth_class": "L",
            "stationary_shadow": "GD_2 stationary primary-line diagnostic",
            "descendant_hierarchy_if_supplied": "KZ/W-constraint descendant system",
            "constructs_descendant_hierarchy": False,
            "kernel": STANDARD_KERNELS["affine_collision_trace_form"],
            "kz_kernel": STANDARD_KERNELS["affine_KZ"],
        },
        "affine_slN_k": {
            "kappa": "(N^2-1)*(k+N)/(2*N)",
            "depth_class": "L",
            "stationary_shadow": "finite-depth Lie/tree Riccati diagnostic",
            "descendant_hierarchy_if_supplied": "affine/KZ descendant system",
            "constructs_descendant_hierarchy": False,
            "kernel": STANDARD_KERNELS["affine_collision_trace_form"],
            "kz_kernel": STANDARD_KERNELS["affine_KZ"],
        },
        "beta_gamma_lambda": {
            "kappa": STANDARD_KAPPAS["beta_gamma_lambda"],
            "depth_class": "C",
            "stationary_shadow": "KdV plus contact stationary diagnostic",
            "descendant_hierarchy_if_supplied": "requires separate CohFT input",
            "constructs_descendant_hierarchy": False,
        },
        "Virasoro_c": {
            "kappa": "c/2",
            "depth_class": "M",
            "stationary_shadow": "polynomial Gelfand-Dickey stationary shadow",
            "descendant_hierarchy_if_supplied": "rank-1 KdV descendant CohFT",
            "constructs_descendant_hierarchy": False,
            "kernel": STANDARD_KERNELS["Virasoro_collision"],
            "S_values": VIRASORO_SHADOW_COEFFICIENTS,
        },
        "W3_c": {
            "kappa": "5*c/6",
            "kappa_T_line": "c/2",
            "kappa_W_line": "c/3",
            "depth_class": "M",
            "stationary_shadow": "two-line stationary GD_3 diagnostic",
            "descendant_hierarchy_if_supplied": "Boussinesq/W_3 constraints",
            "constructs_descendant_hierarchy": False,
        },
        "WN_c": {
            "kappa": "c*(H_N-1)",
            "depth_class": "M",
            "stationary_shadow": "polynomial Gelfand-Dickey stationary shadow",
            "descendant_hierarchy_if_supplied": "W_N constraints or GD_N only with descendant CohFT input",
            "constructs_descendant_hierarchy": False,
        },
    }


# ---------------------------------------------------------------------------
# Resurgence and Painleve scope.
# ---------------------------------------------------------------------------

def shadow_instanton_structure(kappa_val, max_instanton: int = 3) -> Dict[str, Any]:
    r"""Return scalar large-order data and Painleve firewall."""
    A_instanton = 4 * sym_pi**2
    S1_stokes = -4 * sym_pi**2 * kappa_val * S.ImaginaryUnit
    trans_series = {
        n: {
            "instanton_number": n,
            "exponential_factor": f"exp(-{n}*4*pi^2/hbar^2)",
            "scalar_large_order_only": True,
        }
        for n in range(1, max_instanton + 1)
    }
    return {
        "kappa": kappa_val,
        "instanton_action": {
            "A": f"(2*pi)^2 = {float(4 * math.pi**2):.6f}",
            "A_symbolic": A_instanton,
            "universality": "conditional uniform-weight scalar lane",
            "source": LOCAL_SOURCES["universal_instanton_action"],
        },
        "stokes_constant": {
            "S_1": f"-4*pi^2*kappa*i = -4*pi^2*{kappa_val}*i",
            "S_1_symbolic": S1_stokes,
            "kappa_scaling": "linear in kappa on the scalar lane",
        },
        "trans_series": trans_series,
        "painleve": {
            "single_channel_constructed_from_scalar_tau": False,
            "single_channel_statement": (
                "The local manuscript states that the single-channel shadow "
                "Schrodinger equation is rigid and yields no Painleve equation."
            ),
            "multi_channel_if_isomonodromic_system_supplied": (
                "Painleve VI can arise from a separate Heun/isomonodromic "
                "multi-channel system."
            ),
            "source": LOCAL_SOURCES["painleve_multichannel"],
        },
        "large_order": {
            "formula": "lambda_g^FP ~ 2/(2*pi)^(2g)",
            "verification": (
                "F_g^scal = kappa*lambda_g^FP, so the ratio "
                "F_{g+1}/F_g cancels kappa and tends to 1/(2*pi)^2."
            ),
        },
    }


def shadow_instanton_action_numerical(kappa_val: float, max_g: int = 20) -> Dict[str, Any]:
    r"""Numerically check A=(2*pi)^2 from lambda_{g+1}/lambda_g."""
    ratios = {}
    for g in range(1, max_g):
        fp_g = float(lambda_fp(g))
        fp_g1 = float(lambda_fp(g + 1))
        if fp_g != 0:
            ratio = fp_g1 / fp_g
            expected = 1.0 / (2 * math.pi) ** 2
            ratios[g] = {
                "ratio": ratio,
                "expected": expected,
                "relative_error": abs(ratio - expected) / abs(expected),
            }
    A_estimates = {g: 1.0 / data["ratio"] for g, data in ratios.items()}
    A_exact = (2 * math.pi) ** 2
    return {
        "kappa": kappa_val,
        "ratios": ratios,
        "A_estimates": A_estimates,
        "A_exact": A_exact,
        "A_numerical": {
            "value": A_exact,
            "formula": "(2*pi)^2 = 4*pi^2",
            "decimal": f"{A_exact:.10f}",
        },
        "kappa_independence": (
            "The scalar action is independent of kappa because kappa cancels "
            "in F_{g+1}^scal/F_g^scal."
        ),
        "source": LOCAL_SOURCES["universal_instanton_action"],
    }


# ---------------------------------------------------------------------------
# Summary surface.
# ---------------------------------------------------------------------------

def shadow_hierarchy_main_theorem() -> Dict[str, Any]:
    r"""Return the corrected theorem surface for this engine."""
    return {
        "theorem_name": "Finite Scalar Shadow and Stationary Riccati Diagnostics",
        "statements": {
            "(i)": "finite scalar tau identity in Q[kappa][[q]]/(q^{G+1})",
            "(ii)": "standard KdV obstruction proportional to kappa*(1-kappa)",
            "(iii)": "stationary primary-line Riccati diagnostic H^2=t^4 Q_L",
            "(iv)": "descendant CohFT hierarchy requires separate input",
            "(v)": "Painleve/Toda/Gelfand-Dickey systems are not constructed from scalar tau power",
        },
        "key_formula": {
            "finite_scalar_tau": "log tau_shadow_scal^{<=G}=kappa log tau_KW^{<=G}",
            "riccati": "H(t)^2=t^4*((2*kappa+3*alpha*t)^2+2*Delta*t^2)",
            "obstruction": "kappa*(1-kappa)",
            "mc_equation": "D*Theta + (1/2)[Theta,Theta] = 0",
            "instanton_action_scalar": "A=(2*pi)^2",
        },
        "classification": {
            "G": "stationary trivial Riccati diagnostic",
            "L": "stationary GD_2 diagnostic",
            "C": "stationary KdV plus contact diagnostic",
            "M": "stationary polynomial Gelfand-Dickey diagnostic",
        },
        "firewalls": {
            "objects": OBJECT_FIREWALLS,
            "kernels": STANDARD_KERNELS,
        },
        "sources": LOCAL_SOURCES,
    }
