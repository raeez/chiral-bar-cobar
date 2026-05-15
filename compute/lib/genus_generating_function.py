r"""Finite scalar Faber-Pandharipande generating-function checks.

This module verifies the scalar coefficient lane

    F_g(A) = kappa(A) * lambda_g^FP

where

    lambda_g^FP =
        int_{Mbar_{g,1}} lambda_g psi_1^{2g-2}
      = ((2^{2g-1} - 1) / 2^{2g-1}) * |B_{2g}| / (2g)!.

The finite-window formal identity is

    sum_{g>=1} lambda_g^FP * t^{2g} = (t/2)/sin(t/2) - 1,

and hence

    sum_{g>=1} F_g(A) * hbar^{2g-2}
      = kappa(A)/hbar^2 * ((hbar/2)/sin(hbar/2) - 1).

The usual A-hat series is the alternating companion

    (x/2)/sinh(x/2) = sum_{g>=0} (-1)^g lambda_g^FP x^{2g};

the positive FP series is obtained by the formal substitution x -> i*x.

This engine certifies the scalar coefficient identity. The
Witten-Kontsevich descendant CohFT, KdV hierarchy, analytic tau function,
and all-genus shadow convergence require separate descendant/MC/CohFT or
analytic sewing data. Local anchors: compute/lib/utils.py::lambda_fp,
compute/lib/faber_pandharipande_cross_verification.py, and the
Faber-Pandharipande clauses in higher_genus_modular_koszul.tex.
"""

from __future__ import annotations

from typing import Dict

from sympy import (
    Rational, S, Symbol, series, simplify, sin, sinh,
)

from .utils import lambda_fp


# ═══════════════════════════════════════════════════════════════════════
# Faber-Pandharipande numbers through high genus
# ═══════════════════════════════════════════════════════════════════════

def lambda_fp_table(g_max: int = 15) -> Dict[int, Rational]:
    r"""Compute λ_g^FP = (2^{2g-1}-1)/2^{2g-1} · |B_{2g}|/(2g)! for g=1..g_max.

    These are the Faber-Pandharipande intersection numbers:
      int_{M-bar_{g,1}} λ_g · ψ^{2g-2}
    """
    return {g: lambda_fp(g) for g in range(1, g_max + 1)}


def lambda_fp_extended(g: int) -> Rational:
    r"""Extended λ_g^FP with λ_0^FP := 1 (genus-0 normalization).

    For g ≥ 1: standard FP number.
    For g = 0: convention λ_0^FP = 1.
    """
    if g == 0:
        return Rational(1)
    return lambda_fp(g)


# ═══════════════════════════════════════════════════════════════════════
# The Â-genus generating function
# ═══════════════════════════════════════════════════════════════════════

def A_hat_series(x, g_max: int = 10):
    r"""Compute the Hirzebruch Â-class as a power series:

      Â(x) = (x/2)/sinh(x/2)

    Returns the series expansion through x^{2·g_max}.
    """
    return series(x / 2 / sinh(x / 2), x, 0, 2 * g_max + 1)


def A_hat_coefficients(g_max: int = 15) -> Dict[int, Rational]:
    r"""Extract coefficients of x^{2g} in Â(x) = (x/2)/sinh(x/2).

    Returns {g: coefficient of x^{2g}} for g = 0, 1, ..., g_max.
    """
    x = Symbol('x')
    s = series(x / 2 / sinh(x / 2), x, 0, 2 * g_max + 2)
    result = {}
    for g in range(g_max + 1):
        coeff = s.coeff(x, 2 * g)
        result[g] = Rational(coeff)
    return result


def verify_A_hat_equals_FP(g_max: int = 15) -> Dict[str, object]:
    r"""Verify Â(x) = Σ_{g≥0} (-1)^g λ_g^FP x^{2g}.

    The coefficient of x^{2g} in Â(x) should be (-1)^g · λ_g^FP.
    """
    A_hat_coeffs = A_hat_coefficients(g_max)
    results = {}
    all_match = True

    for g in range(g_max + 1):
        a_coeff = A_hat_coeffs[g]
        fp = lambda_fp_extended(g)
        expected = (-1)**g * fp
        match = simplify(a_coeff - expected) == 0
        all_match = all_match and match
        results[g] = {
            'A_hat_coeff': a_coeff,
            'lambda_fp': fp,
            '(-1)^g * lambda_fp': expected,
            'match': match,
        }

    return {
        'g_max': g_max,
        'all_match': all_match,
        'by_genus': results,
    }


# ═══════════════════════════════════════════════════════════════════════
# Free energy generating function
# ═══════════════════════════════════════════════════════════════════════

def scalar_free_energy_series(kappa, hbar, g_max: int = 10):
    r"""Scalar free energy F(ℏ) = Σ_{g≥1} κ · λ_g^FP · ℏ^{2g-2}.

    Returns the series as a sympy expression.
    """
    result = S.Zero
    for g in range(1, g_max + 1):
        result += kappa * lambda_fp(g) * hbar**(2*g - 2)
    return result


def scalar_free_energy_closed_form(kappa, hbar):
    r"""Closed scalar formal series:
      F(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1].

    Equivalently, with genus-0 term:
      F^total(ℏ) = κ/ℏ² · (ℏ/2)/sin(ℏ/2)

    Without genus-0:
      F(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1]
    """
    positive_fp_generator = (hbar / 2) / sin(hbar / 2)
    return kappa / hbar**2 * (positive_fp_generator - 1)


def verify_closed_form(g_max: int = 10) -> Dict[str, object]:
    r"""Verify the scalar sin-branch closed form through a finite window.

    Expands the closed form as a series and compares term by term.
    """
    hbar = Symbol('hbar')

    closed = (hbar / 2) / sin(hbar / 2) - 1
    closed_series = series(closed, hbar, 0, 2 * g_max + 2)

    results = {}
    all_match = True

    for g in range(1, g_max + 1):
        F_g_from_closed = Rational(closed_series.coeff(hbar, 2 * g))
        F_g_from_series = lambda_fp(g)
        match = simplify(F_g_from_closed - F_g_from_series) == 0
        all_match = all_match and match

        results[g] = {
            'closed_form_coeff': F_g_from_closed,
            'lambda_fp': F_g_from_series,
            'match': match,
        }

    return {
        'g_max': g_max,
        'all_match': all_match,
        'scope': f'finite exact rational window 1 <= g <= {g_max}',
        'by_genus': results,
        'identity': "F(ℏ) = κ/ℏ² · ((ℏ/2)/sin(ℏ/2) - 1)",
    }


def free_energy_sign_resolution() -> Dict[str, object]:
    r"""Resolve the sinh/sin sign convention for FP coefficients.

    The issue: λ_g^FP > 0 for all g, but Â(x) has alternating signs.

    Resolution: the scalar FP generator is (x/2)/sin(x/2), while the
    usual A-hat generator (x/2)/sinh(x/2) is its alternating companion.

    (x/2)/sin(x/2) = 1 + x²/24 + 7x⁴/5760 + 31x⁶/967680 + ...

    Relationship:
      (x/2)/sin(x/2) = Ahat(i*x), where Ahat(x) = (x/2)/sinh(x/2).

    The scalar free energy is:
      F(ℏ) = κ/ℏ² · [Â_R(ℏ) - 1]
            = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1]

    and with the genus-0 normalization:
      F^total(ℏ) = κ/ℏ² · (ℏ/2)/sin(ℏ/2)
    """
    x = Symbol('x')

    # (x/2)/sin(x/2) — all-positive generating function
    A_hat_real = series(x / 2 / sin(x / 2), x, 0, 22)

    # (x/2)/sinh(x/2) — alternating-sign Â-genus
    A_hat_standard = series(x / 2 / sinh(x / 2), x, 0, 22)

    coeffs_real = {}
    coeffs_standard = {}
    for g in range(11):
        coeffs_real[g] = Rational(A_hat_real.coeff(x, 2*g))
        coeffs_standard[g] = Rational(A_hat_standard.coeff(x, 2*g))

    # Verify: coeffs_real[g] = λ_g^FP (positive) for all g
    fp_match = all(
        coeffs_real[g] == lambda_fp_extended(g) for g in range(11)
    )

    # Verify: coeffs_standard[g] = (-1)^g · λ_g^FP for all g
    A_hat_match = all(
        coeffs_standard[g] == (-1)**g * lambda_fp_extended(g)
        for g in range(11)
    )

    return {
        'A_hat_real_coeffs': coeffs_real,
        'A_hat_standard_coeffs': coeffs_standard,
        'real_equals_FP': fp_match,
        'standard_equals_(-1)^g_FP': A_hat_match,
        'free_energy_formula': (
            "F(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1]"
        ),
        'total_free_energy': (
            "F^total(ℏ) = κ/ℏ² · (ℏ/2)/sin(ℏ/2)"
        ),
        'generating_function': "(x/2)/sin(x/2)",
        'A_hat_relation': "formal substitution x -> i*x in Ahat(x)",
    }


# ═══════════════════════════════════════════════════════════════════════
# Universal ratio table
# ═══════════════════════════════════════════════════════════════════════

def universal_ratios(g_max: int = 10) -> Dict[str, Rational]:
    r"""Compute universal ratios F_{g+1}/F_g = λ_{g+1}^FP / λ_g^FP.

    These finite-window scalar ratios are independent of the algebra A
    after the common factor kappa(A) is fixed. They are not descendant
    CohFT reconstruction data.
    """
    ratios = {}
    for g in range(1, g_max):
        r = lambda_fp(g + 1) / lambda_fp(g)
        ratios[f"F_{g+1}/F_{g}"] = Rational(r)
    return ratios


# ═══════════════════════════════════════════════════════════════════════
# Shadow corrections to the free energy
# ═══════════════════════════════════════════════════════════════════════

def virasoro_Q_contact(c=None):
    r"""Virasoro quartic contact invariant Q^contact_Vir = 10/[c(5c+22)].

    This is the first shadow correction beyond the scalar level.
    It contributes to the genus-2 free energy at the chain level.
    """
    if c is None:
        c = Symbol('c')
    return Rational(10, 1) / (c * (5 * c + 22))


def genus2_shadow_correction_virasoro(c=None):
    r"""Conditional genus-2 Virasoro contact pairing.

    The unconditional scalar term is

        F_2^{scalar}(Vir_c) = kappa(Vir_c) * lambda_2^FP
                             = (c/2) * 7/5760.

    The exact local shadow constant is

        Q^contact_Vir = 10/[c(5c+22)].

    The boundary Witten-Kontsevich pairing 1/1152 is locally recorded in
    concordance.tex as <tau_4>_2^{boundary}. Multiplying it by
    Q^contact gives a conditional contribution only after a separate
    descendant/MC graph pairing identifies that boundary class with the
    Virasoro quartic contact insertion. This function therefore does not
    assert an unconditional corrected genus-2 Virasoro free energy.
    """
    if c is None:
        c = Symbol('c')

    kappa_vir = c / 2
    F2_scalar = kappa_vir * lambda_fp(2)  # c/2 · 7/5760 = 7c/11520
    Q_contact = virasoro_Q_contact(c)
    boundary_wk_pairing = Rational(1, 1152)
    conditional_delta_F2 = Q_contact * boundary_wk_pairing

    return {
        'c': c,
        'kappa': kappa_vir,
        'F_2_scalar': F2_scalar,
        'Q_contact': Q_contact,
        'boundary_wk_pairing': boundary_wk_pairing,
        'conditional_delta_F_2': simplify(conditional_delta_F2),
        'conditional_F_2_if_pairing_applies': simplify(
            F2_scalar + conditional_delta_F2
        ),
        'conditional_ratio_if_pairing_applies': simplify(
            conditional_delta_F2 / F2_scalar
        ),
        'unconditional_full_genus2_correction': None,
        'claim_scope': (
            "conditional: Q_contact and 1/1152 are exact local constants; "
            "a full Virasoro genus-2 correction requires separate "
            "descendant/MC graph pairing data"
        ),
    }


# ═══════════════════════════════════════════════════════════════════════
# Descendant CohFT firewall
# ═══════════════════════════════════════════════════════════════════════

def free_energy_tau_function_check(g_max: int = 8) -> Dict[str, object]:
    r"""Classify the scalar FP window relative to KdV data.

    Witten-Kontsevich concerns the full descendant potential in times
    t_0, t_1, ... . The scalar Hodge numbers
    int_{Mbar_{g,1}} lambda_g psi_1^{2g-2} form one formal coefficient
    lane. They do not by themselves construct a KdV tau function, the
    hierarchy flows, or descendant reconstruction.

    A rank-1 primary or stationary line becomes a KdV comparison only
    after the corresponding CohFT supplies the full descendant correlators.
    This function records that firewall explicitly.
    """
    u = Symbol('u', positive=True)
    fp_series = sum(lambda_fp_extended(g) * u**g for g in range(g_max + 1))

    return {
        'scalar_free_energy': "F(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1]",
        'total_free_energy': "F^total(ℏ) = κ/ℏ² · (ℏ/2)/sin(ℏ/2)",
        'infinite_product': "(ℏ/2)/sin(ℏ/2) = Π_{n≥1} (1 - ℏ²/(2nπ)²)^{-1}",
        'coefficient_scope': f'finite formal scalar window 0 <= g <= {g_max}',
        'constructs_full_kdv_hierarchy': False,
        'constructs_analytic_tau_function': False,
        'claims_all_genus_shadow_convergence': False,
        'requires_witten_kontsevich_descendants': True,
        'requires_descendant_cohft_data': True,
        'kdv_relation': (
            "Scalar FP coefficients alone do not define KdV flows; "
            "Witten-Kontsevich input is the full descendant potential."
        ),
        'stationary_primary_line': (
            "A one-dimensional primary/stationary line is a specialization "
            "only after the CohFT descendant data are supplied."
        ),
        'analytic_scope': (
            "The sin closed form is meromorphic with first pole at |hbar|=2*pi; "
            "all-genus shadow convergence requires separate analytic input."
        ),
        'shadow_correction_structure': (
            "Shadow corrections δF(ℏ) satisfy the Maurer-Cartan equation "
            "D·Θ + ½[Θ,Θ] = 0 projected to each genus. "
            "They require algebra-dependent descendant/graph data."
        ),
        'finite_scalar_series': fp_series,
    }


# ═══════════════════════════════════════════════════════════════════════
# Shadow-corrected generating function structure
# ═══════════════════════════════════════════════════════════════════════

def shadow_corrected_structure() -> Dict[str, object]:
    r"""Scope of shadow-corrected free-energy data.

    F^{corr}(ℏ) = F^{scalar}(ℏ) + δF^{shadow}(ℏ)

    where:
      F^{scalar}(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1]   (pure Â, universal)
      δF^{shadow}(ℏ) = Σ_{g≥2} δF_g^{shadow} · ℏ^{2g-2}   (algebra-dependent)

    The shadow corrections start at genus 2 (genus 1 has no shadow correction
    because the quartic contact only contributes through genus-2 moduli).

    For each shadow archetype:
      G (Gaussian, r_max=2): δF^{shadow} = 0 (Heisenberg, lattice VOAs)
      L (Lie, r_max=3): δF^{shadow} starts at genus 3 (cubic correction)
      C (Contact, r_max=4): δF^{shadow} starts at genus 2 (quartic correction)
      M (Mixed, r_max=∞): no finite shadow-depth truncation at generic level

    Structural input:
      The coefficients δF_g^{shadow}, when defined, are controlled by
      the Maurer-Cartan element Θ_A and stable-graph amplitudes

        δF_g = Σ_{r≥3} Σ_{Γ ∈ G_{g,0}^{(r)}} (1/|Aut Γ|) · A_Γ(Θ_A^{≤r})

    This module does not assert a closed multiplicative shadow generating
    function or a KdV recursion for those corrections.
    """
    c = Symbol('c')

    F2_data = genus2_shadow_correction_virasoro(c)

    return {
        'gaussian_correction': "δF = 0 (Heisenberg, lattice)",
        'lie_correction': "δF starts at genus 3",
        'contact_correction': "δF starts at genus 2 (quartic Q^contact)",
        'mixed_correction': "no finite shadow-depth truncation at generic level",
        'virasoro_genus2': F2_data,
        'closed_shadow_generating_function': None,
        'constructs_full_kdv_hierarchy': False,
        'requires_descendant_cohft_data': True,
        'mc_equation_controls_corrections': True,
    }


# ═══════════════════════════════════════════════════════════════════════
# Numerical verification
# ═══════════════════════════════════════════════════════════════════════

def numerical_verification(g_max: int = 15) -> Dict[str, object]:
    r"""Finite exact verification of the positive FP generating function.

    Computes λ_g^FP and (x/2)/sin(x/2) coefficients through genus g_max
    and verifies exact agreement.
    """
    from sympy import sin

    x = Symbol('x')
    s = series(x / 2 / sin(x / 2), x, 0, 2 * g_max + 2)

    table = []
    all_match = True
    for g in range(g_max + 1):
        fp = lambda_fp_extended(g)
        coeff = Rational(s.coeff(x, 2 * g))
        match = (fp == coeff)
        all_match = all_match and match
        table.append({
            'genus': g,
            'lambda_fp': fp,
            '(x/2)/sin(x/2) coeff': coeff,
            'match': match,
        })

    return {
        'g_max': g_max,
        'all_match': all_match,
        'table': table,
        'scope': f'finite exact rational window 0 <= g <= {g_max}',
        'generating_function_identity': (
            "(x/2)/sin(x/2) = Σ_{g≥0} λ_g^FP x^{2g}, checked through "
            f"genus {g_max}"
        ),
        'free_energy_identity': (
            f"F(ℏ) = κ/ℏ² · [(ℏ/2)/sin(ℏ/2) - 1], checked through "
            f"genus {g_max}"
        ),
    }
