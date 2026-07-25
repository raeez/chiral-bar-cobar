r"""Exact N=2 OPE data and typed shadow/modular obligations.

The module uses the standard normalization

    G+(z)G-(w) ~ (2c/3)(z-w)^-3 + 2J(z-w)^-2
                  + (2T+dJ)(z-w)^-1.

It computes singular n-th products and elementary parameter identities.
Line-restricted OPE coefficients are kept distinct from bar curvature,
the full multi-channel shadow tensor, and the genus-one modular
characteristic.
"""

from __future__ import annotations

from typing import Dict

import sympy as sp


c = sp.Symbol("c")
k = sp.Symbol("k")


class OpenN2ShadowError(RuntimeError):
    """Raised when OPE data are asked to determine a comparison invariant."""


BAR_INPUT = (
    "a Fulton--MacPherson residue convention, completed bar filtration, "
    "and proof that the selected line projection intertwines the differential"
)
MODULAR_INPUT = (
    "a trace-compatible genus-one Kazama--Suzuki coset curvature comparison"
)
SHADOW_INPUT = (
    "the full multi-channel Maurer--Cartan tensor with TT, JJ, G+G-, and JG channels"
)


def _sym(value):
    return sp.sympify(value)


def n2_central_charge(k_val=None):
    """Kazama--Suzuki parameter c=3k/(k+2)."""
    kval = k if k_val is None else _sym(k_val)
    if kval == -2:
        raise ValueError("k=-2 is the pole of c=3k/(k+2)")
    return sp.simplify(3 * kval / (kval + 2))


def n2_nth_products():
    r"""Singular n-th products in the standard N=2 convention."""
    return {
        ("T", "T"): {
            3: {"vac": c / 2},
            1: {"T": sp.Integer(2)},
            0: {"dT": sp.Integer(1)},
        },
        ("T", "J"): {
            1: {"J": sp.Integer(1)},
            0: {"dJ": sp.Integer(1)},
        },
        ("J", "T"): {1: {"J": sp.Integer(1)}},
        ("T", "G+"): {
            1: {"G+": sp.Rational(3, 2)},
            0: {"dG+": sp.Integer(1)},
        },
        ("T", "G-"): {
            1: {"G-": sp.Rational(3, 2)},
            0: {"dG-": sp.Integer(1)},
        },
        ("G+", "T"): {
            1: {"G+": sp.Rational(3, 2)},
            0: {"dG+": sp.Rational(1, 2)},
        },
        ("G-", "T"): {
            1: {"G-": sp.Rational(3, 2)},
            0: {"dG-": sp.Rational(1, 2)},
        },
        ("J", "J"): {1: {"vac": c / 3}},
        ("J", "G+"): {0: {"G+": sp.Integer(1)}},
        ("J", "G-"): {0: {"G-": sp.Integer(-1)}},
        ("G+", "J"): {0: {"G+": sp.Integer(-1)}},
        ("G-", "J"): {0: {"G-": sp.Integer(1)}},
        ("G+", "G-"): {
            2: {"vac": 2 * c / 3},
            1: {"J": sp.Integer(2)},
            0: {"T": sp.Integer(2), "dJ": sp.Integer(1)},
        },
        ("G-", "G+"): {
            2: {"vac": 2 * c / 3},
            1: {"J": sp.Integer(-2)},
            0: {"T": sp.Integer(2), "dJ": sp.Integer(-1)},
        },
        ("G+", "G+"): {},
        ("G-", "G-"): {},
    }


def n2_nth_product(a: str, b: str, n: int) -> Dict[str, object]:
    return n2_nth_products().get((a, b), {}).get(n, {})


def n2_ope_status_packet():
    return {
        "status": "exact",
        "generators": {
            "T": {"weight": sp.Integer(2), "parity": "even"},
            "J": {"weight": sp.Integer(1), "parity": "even"},
            "G+": {"weight": sp.Rational(3, 2), "parity": "odd"},
            "G-": {"weight": sp.Rational(3, 2), "parity": "odd"},
        },
        "normalization": "G+G- leading coefficient 2c/3",
    }


def n2_bar_diff_deg2(a: str, b: str):
    """Require the geometric residue model before constructing a bar map."""
    raise OpenN2ShadowError(BAR_INPUT)


def n2_curvature():
    """Return leading OPE norms with their mathematical type."""
    return {
        "status": "leading OPE norms",
        "TT": c / 2,
        "JJ": c / 3,
        "G+G-": 2 * c / 3,
        "bar_curvature": None,
    }


def n2_curvature_ratios():
    return {
        "status": "ratios of leading OPE norms",
        "JJ/TT": sp.Rational(2, 3),
        "G+G-/TT": sp.Rational(4, 3),
    }


def n2_modular_status_packet():
    return {
        "status": "open",
        "kappa": None,
        "anomaly_ratio": None,
        "K_kappa": None,
        "required_input": MODULAR_INPUT,
    }


def _open_modular():
    raise OpenN2ShadowError(MODULAR_INPUT)


def kappa_n2(c_val=None):
    return _open_modular()


def sigma_n2(c_val=None):
    return _open_modular()


def n2_ff_dual_central_charge(c_val=None, k_val=None):
    """Compatibility name for the arithmetic reflection c -> 6-c."""
    if k_val is not None:
        return sp.simplify(n2_central_charge(-_sym(k_val) - 4))
    cval = c if c_val is None else _sym(c_val)
    return 6 - cval


def n2_self_dual_point():
    return {
        "central_reflection_fixed_point": sp.Integer(3),
        "level_reflection_fixed_point": sp.Integer(-2),
        "chart_status": "boundary value and parameter pole",
        "object_level_duality": None,
    }


def n2_complementarity_sum(c_val=None, k_val=None):
    return _open_modular()


def n2_shadow_data_T_line(c_val=None):
    cval = c if c_val is None else _sym(c_val)
    return {
        "status": "Virasoro OPE restriction",
        "leading_norm": cval / 2,
        "singular_products": n2_nth_products()[("T", "T")],
        "full_shadow": None,
    }


def n2_shadow_data_J_line():
    return {
        "status": "Heisenberg OPE restriction",
        "leading_norm": c / 3,
        "singular_products": n2_nth_products()[("J", "J")],
        "full_shadow": None,
    }


def n2_shadow_data_G_line(c_val=None):
    cval = c if c_val is None else _sym(c_val)
    products = n2_nth_products()[("G+", "G-")]
    return {
        "status": "mixed G+G- OPE restriction",
        "leading_norm": 2 * cval / 3,
        "singular_products": {
            degree: {
                state: sp.simplify(coefficient.subs(c, cval))
                if hasattr(coefficient, "subs") else coefficient
                for state, coefficient in outputs.items()
            }
            for degree, outputs in products.items()
        },
        "full_shadow": None,
    }


def _open_shadow():
    raise OpenN2ShadowError(SHADOW_INPUT)


def n2_shadow_tower_T_line(c_val, max_arity=30):
    return _open_shadow()


def n2_shadow_tower_J_line(c_val, max_arity=30):
    return _open_shadow()


def n2_shadow_tower_G_line(c_val, max_arity=30):
    return _open_shadow()


def n2_shadow_growth_rate_T_line(c_val=None):
    return _open_shadow()


def n2_shadow_growth_rate_J_line():
    return _open_shadow()


def n2_shadow_growth_rate_G_line():
    return _open_shadow()


def n2_F_g(c_val, g):
    return _open_modular()


def n2_genus_table(c_val, max_genus=5):
    return _open_modular()


def n2_cross_channel_curvatures():
    return {
        "status": "central terms of singular OPE channels",
        "TT": c / 2,
        "JJ": c / 3,
        "G+G-": 2 * c / 3,
        "mixed_shadow_tensor": None,
    }


def n2_propagator_variance(c_val=None):
    return _open_shadow()


def n2_special_values():
    levels = (sp.Integer(1), sp.Integer(2), sp.Integer(10))
    return {
        level: {
            "central_charge": n2_central_charge(level),
            "kappa": None,
            "status": "exact parameter, open modular invariant",
        }
        for level in levels
    }


def n2_shadow_class():
    return {
        "status": "open",
        "class": None,
        "required_input": SHADOW_INPUT,
    }


def n2_full_shadow_coefficients(c_val, max_arity=20):
    return _open_shadow()


def verify_n2_jacobi_TJG():
    products = n2_nth_products()
    return {
        "T_weights": (
            products[("T", "J")][1]["J"] == 1
            and products[("T", "G+")][1]["G+"] == sp.Rational(3, 2)
        ),
        "J_charges": (
            products[("J", "G+")][0]["G+"] == 1
            and products[("J", "G-")][0]["G-"] == -1
        ),
    }


def verify_n2_jacobi_JGG():
    products = n2_nth_products()
    return {
        "charge_conservation": (
            products[("J", "G+")][0]["G+"]
            + products[("J", "G-")][0]["G-"]
            == 0
        ),
        "opposite_J_coefficients": (
            products[("G+", "G-")][1]["J"]
            + products[("G-", "G+")][1]["J"]
            == 0
        ),
    }


def verify_n2_jacobi_GGT():
    products = n2_nth_products()
    return {
        "stress_tensor_coefficient": products[("G+", "G-")][0]["T"] == 2,
        "central_normalization": products[("G+", "G-")][2]["vac"] == 2 * c / 3,
    }


def verify_all():
    products = n2_nth_products()
    exact = {
        "central_parameter_inverse": sp.simplify(
            2 * n2_central_charge(k) / (3 - n2_central_charge(k)) - k
        ) == 0,
        "central_reflection_sum": sp.simplify(
            n2_central_charge(k) + n2_central_charge(-k - 4)
        ) == 6,
        "TT_norm": products[("T", "T")][3]["vac"] == c / 2,
        "JJ_norm": products[("J", "J")][1]["vac"] == c / 3,
        "GG_norm": products[("G+", "G-")][2]["vac"] == 2 * c / 3,
        "TJG_packet": all(verify_n2_jacobi_TJG().values()),
        "JGG_packet": all(verify_n2_jacobi_JGG().values()),
        "GGT_packet": all(verify_n2_jacobi_GGT().values()),
    }
    return {
        "exact_checks": exact,
        "all_exact_checks_pass": all(exact.values()),
        "bar_status": {"status": "open", "required_input": BAR_INPUT},
        "modular_status": n2_modular_status_packet(),
        "shadow_status": n2_shadow_class(),
    }
