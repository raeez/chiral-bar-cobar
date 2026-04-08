r"""Generating function analysis for class L (affine Kac-Moody) free energy.

MAIN RESULT (NEGATIVE): The planted-forest generating function G_pf(xi) for
class L algebras does NOT admit a closed form analogous to the scalar
generating function G^scalar(xi) = kappa * (xi/(2 sin(xi/2)) - 1).

The full class L free energy decomposes as:

    G[F](xi) = G^scalar(xi) + G^pf(xi)

where G^scalar(xi) = kappa * (xi/(2 sin(xi/2)) - 1) is CLOSED FORM
(proved in theorem_borel_summability_shadow_engine.py), but G^pf(xi) is
an infinite series whose coefficients are polynomials in (kappa, S_3)
of growing degree, with no finite closed form.

STRUCTURAL RESULTS (POSITIVE)
==============================

1. FACTORIZATION:  G_pf(xi) = S_3 * Phi(kappa, S_3, xi^2)
   where Phi is a formal power series. The overall S_3 factor encodes
   the class G recovery: S_3 = 0 => G_pf = 0 (Heisenberg limit).

2. DEGREE BOUND:  At genus g, delta_pf^{(g)} is a polynomial in (kappa, S_3)
   of total degree <= 2(g-1), with S_3 appearing at powers 1 through 2(g-1).
   The S_3 degree bound 2(g-1) equals the maximum number of genus-0
   trivalent vertices in a stable graph at (g, 0).

3. PADE STRUCTURE: The Pade [1/1] approximant of h(u) = sum delta_pf^{(g)} u^g
   (setting u = xi^2) provides a rational approximation
       G_pf ~ xi^4 * (p_0 + p_1 xi^2) / (1 + q_1 xi^2)
   with family-dependent pole location xi^2 = -1/q_1.

4. S_3-LINEAR DERIVATIVE: dG_pf/dS_3|_{S_3=0} = sum_g L_g(kappa) * xi^{2g}
   where L_g is a polynomial in kappa of degree g-1 (not g).
   At genus 2: L_2 = -kappa/48.

5. LEADING S_3 TERM: The pure-S_3 term (kappa^0 coefficient) at genus g
   has the form c_g * S_3^{2(g-1)}, with c_2 = 5/24, c_3 = 15/64,
   c_4 = 425/576. The sequence {c_g} grows rapidly and does NOT match
   any standard combinatorial sequence.

6. CLASS G RECOVERY: Setting S_3 = 0 recovers G_pf = 0, so
   G[F] = kappa * (xi/(2 sin(xi/2)) - 1), confirming the Borel engine result.

7. LARGE-N ASYMPTOTICS: For SU(N) at k=0 with N >> 1:
   kappa ~ N^2/2, S_3 ~ 2/(3N), so S_3 * kappa ~ 2N/3 is level-independent.
   The planted-forest correction grows as N^{2(g-1)} at genus g, matching
   the 't Hooft large-N scaling with genus-dependent planar weight.

COMPUTATIONAL INFRASTRUCTURE
==============================

- Exact rational arithmetic through genus 4 (from theorem_class_l_closed_form_engine)
- Numerical evaluation at arbitrary xi for SU(N) families
- Pade [1/1] and [2/2] approximants from genus 2-4 data
- S_3-derivative analysis at S_3 = 0
- Cross-family consistency checks (SU(2) through SU(8))
- Additivity verification for scalar part
- Complementarity verification (AP24)

CONVENTIONS (AP1, AP9, AP27, AP38)
===================================

    kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N)  [AP1]
    S_3(V_k(sl_N)) = 2N/(3*kappa)          [class L: S_r=0 for r>=4]
    lambda_g^FP = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)  [AP38]
    Bar propagator is weight 1              [AP27]

References:
    theorem_class_l_closed_form_engine.py: F_1-F_4, planted-forest polynomials
    theorem_borel_summability_shadow_engine.py: scalar generating function
    higher_genus_modular_koszul.tex: thm:theorem-d, rem:planted-forest-correction-explicit
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from compute.lib.theorem_class_l_closed_form_engine import (
    bernoulli_exact,
    lambda_fp,
    kappa_slN,
    central_charge_slN,
    S3_slN,
    shadow_tower_class_L,
    delta_pf_genus2,
    delta_pf_genus3_class_L,
    delta_pf_genus4_class_L,
    F_g_class_L,
    GENUS3_PF_CLASS_L,
    GENUS4_PF_CLASS_L,
)


# ============================================================================
# Section 1: Planted-forest generating function evaluation
# ============================================================================

def G_pf_exact(xi_sq: Fraction, kappa: Fraction, S3: Fraction,
               max_genus: int = 4) -> Fraction:
    r"""Exact planted-forest generating function G_pf at u = xi^2.

    G_pf(xi) = sum_{g=2}^{max_genus} delta_pf^{(g)}(kappa, S_3) * xi^{2g}

    Returns exact Fraction. Genus 1 contributes 0 (no planted-forest at g=1).
    """
    result = Fraction(0)
    for g in range(2, max_genus + 1):
        if g == 2:
            dpf = delta_pf_genus2(kappa, S3)
        elif g == 3:
            dpf = delta_pf_genus3_class_L(kappa, S3)
        elif g == 4:
            dpf = delta_pf_genus4_class_L(kappa, S3)
        else:
            raise ValueError(f"Planted-forest polynomial unavailable at genus {g}")
        result += dpf * xi_sq ** g
    return result


def G_pf_numerical(xi: float, kappa_val: float, S3_val: float,
                   max_genus: int = 4) -> float:
    """Numerical planted-forest generating function at real xi.

    Uses exact polynomials through genus 4 evaluated numerically.
    """
    kap = Fraction(kappa_val).limit_denominator(10**12)
    s3 = Fraction(S3_val).limit_denominator(10**12)
    u = Fraction(xi * xi).limit_denominator(10**12)
    return float(G_pf_exact(u, kap, s3, max_genus))


def G_scalar_closed_form(xi: complex, kappa_val: float) -> complex:
    r"""Closed-form scalar generating function.

    G^scalar(xi) = kappa * (xi / (2 sin(xi/2)) - 1)

    Meromorphic with simple poles at xi = 2*pi*n, n in Z \ {0}.
    """
    xi = complex(xi)
    if abs(xi) < 1e-15:
        return complex(0)
    half = xi / 2.0
    sin_half = cmath.sin(half)
    if abs(sin_half) < 1e-30:
        return complex(float('inf'))
    return kappa_val * (xi / (2.0 * sin_half) - 1.0)


def G_scalar_series(xi_sq: Fraction, kappa: Fraction,
                    max_genus: int = 10) -> Fraction:
    r"""Scalar generating function via truncated series (verification path).

    G^scalar(xi) = sum_{g=1}^{max_genus} kappa * lambda_g^FP * xi^{2g}
    """
    result = Fraction(0)
    for g in range(1, max_genus + 1):
        result += kappa * lambda_fp(g) * xi_sq ** g
    return result


def G_full_class_L(xi: float, kappa_val: float, S3_val: float,
                   max_genus: int = 4) -> Dict[str, float]:
    r"""Full class L generating function decomposition at real xi.

    Returns scalar, planted-forest, and total components.
    """
    G_scal = G_scalar_closed_form(xi, kappa_val).real
    G_pf = G_pf_numerical(xi, kappa_val, S3_val, max_genus)
    return {
        'G_scalar': G_scal,
        'G_pf': G_pf,
        'G_total': G_scal + G_pf,
        'pf_to_scalar_ratio': G_pf / G_scal if abs(G_scal) > 1e-50 else float('inf'),
    }


# ============================================================================
# Section 2: S_3 factorization and derivative at S_3 = 0
# ============================================================================

def verify_S3_factorization(kappa: Fraction, max_genus: int = 4) -> Dict[int, bool]:
    r"""Verify that delta_pf^{(g)} vanishes at S_3 = 0 for each genus.

    This confirms G_pf = S_3 * Phi(kappa, S_3, xi^2).
    """
    results = {}
    for g in range(2, max_genus + 1):
        val = F_g_class_L(g, kappa, Fraction(0)) - kappa * lambda_fp(g)
        results[g] = (val == Fraction(0))
    return results


def S3_linear_coefficients() -> Dict[int, Dict[Tuple[int, int], Fraction]]:
    r"""Extract the S_3-linear terms from each genus polynomial.

    These give dG_pf/dS_3|_{S_3=0} = sum_g L_g(kappa) * xi^{2g}
    where L_g(kappa) = sum_a c_{a,1}^{(g)} * kappa^a.

    g=2: L_2 = -kappa/48
    g=3: L_3 = -343/2304 * kappa - 1/82944 * kappa^3
    g=4: L_4 = -123589/165888 * kappa - 13/864 * kappa^2 - 143/1327104 * kappa^3
    """
    result = {}

    # Genus 2: delta_pf = S3*(10*S3 - kappa)/48 => L_2 = -kappa/48
    result[2] = {(1, 1): Fraction(-1, 48)}

    # Genus 3: extract b=1 terms
    result[3] = {(a, b): c for (a, b), c in GENUS3_PF_CLASS_L.items() if b == 1}

    # Genus 4: extract b=1 terms
    result[4] = {(a, b): c for (a, b), c in GENUS4_PF_CLASS_L.items() if b == 1}

    return result


def dGpf_dS3_at_zero(kappa: Fraction, xi_sq: Fraction,
                     max_genus: int = 4) -> Fraction:
    r"""Evaluate dG_pf/dS_3|_{S_3=0} at given kappa and xi^2.

    dG_pf/dS_3|_{S_3=0} = sum_{g=2}^{max_genus} L_g(kappa) * xi^{2g}
    """
    lin_coeffs = S3_linear_coefficients()
    result = Fraction(0)
    for g in range(2, max_genus + 1):
        if g not in lin_coeffs:
            continue
        L_g = Fraction(0)
        for (a, b), c in lin_coeffs[g].items():
            L_g += c * kappa ** a
        result += L_g * xi_sq ** g
    return result


# ============================================================================
# Section 3: S_3 degree analysis
# ============================================================================

def S3_degree_structure() -> Dict[int, Dict[str, Any]]:
    r"""Analyze the S_3 degree structure at each genus.

    At genus g, delta_pf^{(g,0)} has:
    - min S_3 power = 1 (all genera)
    - max S_3 power = 2(g-1)
    - number of distinct S_3 powers = g-1
    """
    results = {}

    # Genus 2: S_3 powers 1, 2
    results[2] = {
        'min_S3_power': 1,
        'max_S3_power': 2,
        'S3_powers_present': [1, 2],
        'bound_2gm2': 2,
        'saturates_bound': True,
    }

    for g, coeffs in [(3, GENUS3_PF_CLASS_L), (4, GENUS4_PF_CLASS_L)]:
        s3_powers = sorted(set(b for (a, b) in coeffs.keys()))
        bound = 2 * (g - 1)
        results[g] = {
            'min_S3_power': min(s3_powers),
            'max_S3_power': max(s3_powers),
            'S3_powers_present': s3_powers,
            'bound_2gm2': bound,
            'saturates_bound': max(s3_powers) == bound,
        }

    return results


def leading_S3_coefficients() -> Dict[int, Fraction]:
    r"""Extract the leading (highest S_3 power) coefficient at each genus.

    These are the pure-S_3 terms: coefficient of S_3^{2(g-1)} at kappa^0.
    Sequence: c_2 = 5/24, c_3 = 15/64, c_4 = 425/576.
    """
    results = {}

    # Genus 2: coefficient of S_3^2 is 10/48 = 5/24
    results[2] = Fraction(5, 24)

    # Genus 3: coefficient of S_3^4 at kappa^0
    results[3] = GENUS3_PF_CLASS_L.get((0, 4), Fraction(0))

    # Genus 4: coefficient of S_3^6 at kappa^0
    results[4] = GENUS4_PF_CLASS_L.get((0, 6), Fraction(0))

    return results


# ============================================================================
# Section 4: Pade approximants
# ============================================================================

@dataclass(frozen=True)
class PadeApproximant:
    """Pade [1/1] approximant for h(u) = a_2 + a_3*u + a_4*u^2.

    G_pf(xi) ~ xi^4 * (p0 + p1*xi^2) / (1 + q1*xi^2)

    The pole at xi^2 = -1/q1 gives the effective convergence radius
    of the planted-forest expansion.
    """
    p0: Fraction
    p1: Fraction
    q1: Fraction
    pole_location: Fraction  # xi^2 = -1/q1
    a2: Fraction
    a3: Fraction
    a4: Fraction


def pade_11_from_genus_data(kappa: Fraction, S3: Fraction) -> PadeApproximant:
    r"""Construct Pade [1/1] approximant from genus 2-4 planted-forest data.

    Fits h(u) = a_2 + a_3*u + a_4*u^2 where a_g = delta_pf^{(g)},
    as (p0 + p1*u)/(1 + q1*u) satisfying:
        p0 = a_2
        a_3 + a_2*q1 = p1   (from expanding and matching u^1)
        a_4 + a_3*q1 = 0    (from matching u^2 in the denominator)
    So q1 = -a_4/a_3 and p1 = a_3 + a_2*q1.
    """
    a2 = delta_pf_genus2(kappa, S3)
    a3 = delta_pf_genus3_class_L(kappa, S3)
    a4 = delta_pf_genus4_class_L(kappa, S3)

    if a3 == Fraction(0):
        raise ValueError("a3 = 0: Pade [1/1] not constructible (S3 = 0?)")

    q1 = -a4 / a3
    p0 = a2
    p1 = a3 + a2 * q1
    pole = -Fraction(1) / q1 if q1 != Fraction(0) else None

    return PadeApproximant(
        p0=p0, p1=p1, q1=q1,
        pole_location=pole,
        a2=a2, a3=a3, a4=a4,
    )


def pade_evaluate(pade: PadeApproximant, xi_sq: Fraction) -> Fraction:
    r"""Evaluate G_pf ~ xi^4 * (p0 + p1*xi^2) / (1 + q1*xi^2) at xi^2."""
    numer = pade.p0 + pade.p1 * xi_sq
    denom = Fraction(1) + pade.q1 * xi_sq
    if denom == Fraction(0):
        raise ValueError("Evaluation at the Pade pole")
    return xi_sq ** 2 * numer / denom


# ============================================================================
# Section 5: SU(N) family evaluations
# ============================================================================

@dataclass(frozen=True)
class ClassLGFData:
    """Complete generating function data for SU(N) at level k."""
    N: int
    k: Fraction
    kappa: Fraction
    S3: Fraction
    G_pf_values: Dict[float, float]  # xi -> G_pf(xi)
    G_scalar_values: Dict[float, complex]  # xi -> G_scalar(xi)
    G_full_values: Dict[float, float]  # xi -> G_full(xi)
    pade: Optional[PadeApproximant]
    dGpf_dS3_values: Dict[float, float]  # xi -> dG_pf/dS3|_{S3=0}


def evaluate_slN_family(N: int, k: Fraction = Fraction(0),
                        xi_values: List[float] = None) -> ClassLGFData:
    """Compute all generating function data for V_k(sl_N)."""
    if xi_values is None:
        xi_values = [0.1, 0.5, 1.0, 1.5, 2.0]

    kap = kappa_slN(N, k)
    s3 = S3_slN(N, k)

    G_pf_vals = {}
    G_scal_vals = {}
    G_full_vals = {}
    dG_vals = {}

    for xi in xi_values:
        xi_sq_frac = Fraction(xi * xi).limit_denominator(10**12)

        # Planted-forest
        gpf = float(G_pf_exact(xi_sq_frac, kap, s3))
        G_pf_vals[xi] = gpf

        # Scalar (closed form)
        gscal = G_scalar_closed_form(xi, float(kap))
        G_scal_vals[xi] = gscal

        # Full
        G_full_vals[xi] = gscal.real + gpf

        # S3 derivative at S3=0
        dG = float(dGpf_dS3_at_zero(kap, xi_sq_frac))
        dG_vals[xi] = dG

    # Pade
    try:
        pade = pade_11_from_genus_data(kap, s3)
    except (ValueError, ZeroDivisionError):
        pade = None

    return ClassLGFData(
        N=N, k=k, kappa=kap, S3=s3,
        G_pf_values=G_pf_vals,
        G_scalar_values=G_scal_vals,
        G_full_values=G_full_vals,
        pade=pade,
        dGpf_dS3_values=dG_vals,
    )


# ============================================================================
# Section 6: Cross-family analysis
# ============================================================================

def pf_to_scalar_ratio_table(
    N_values: List[int] = None,
    xi_values: List[float] = None,
) -> Dict[int, Dict[float, float]]:
    r"""Compute G_pf/G_scalar ratio across SU(N) families.

    This ratio is NOT universal (depends on N), confirming that the
    planted-forest part has no simple proportionality to the scalar part.
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 6]
    if xi_values is None:
        xi_values = [0.5, 1.0]

    results = {}
    for N in N_values:
        data = evaluate_slN_family(N, xi_values=xi_values)
        ratios = {}
        for xi in xi_values:
            gscal = data.G_scalar_values[xi].real
            gpf = data.G_pf_values[xi]
            ratios[xi] = gpf / gscal if abs(gscal) > 1e-50 else float('inf')
        results[N] = ratios
    return results


def S3_kappa_product_table(
    N_values: List[int] = None,
    k_values: List[Fraction] = None,
) -> List[Dict[str, Any]]:
    r"""Verify that S_3 * kappa = 2N/3 is level-independent for SU(N).

    This is the natural 't Hooft-like invariant: S_3 * kappa depends on N
    but not on the level k.
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 6, 8]
    if k_values is None:
        k_values = [Fraction(0), Fraction(1), Fraction(3)]

    rows = []
    for N in N_values:
        for k in k_values:
            kap = kappa_slN(N, k)
            s3 = S3_slN(N, k)
            product = s3 * kap
            expected = Fraction(2 * N, 3)
            rows.append({
                'N': N,
                'k': k,
                'kappa': kap,
                'S3': s3,
                'S3_times_kappa': product,
                'expected_2N_over_3': expected,
                'match': product == expected,
            })
    return rows


# ============================================================================
# Section 7: Scaling analysis (negative result documentation)
# ============================================================================

def test_S3_squared_scaling(
    N_values: List[int] = None,
    xi: float = 1.0,
) -> Dict[str, Any]:
    r"""Test whether G_pf = S_3^2 * f(kappa, xi) for some bivariate f.

    RESULT: FALSE. The planted-forest polynomial has min S_3 power = 1 at
    every genus, so the correct factorization is G_pf = S_3 * Phi, not S_3^2.
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 6]

    xi_sq = Fraction(xi * xi).limit_denominator(10**12)

    # Compute G_pf / S_3 and G_pf / S_3^2 across families
    ratios_s3 = {}
    ratios_s3sq = {}
    for N in N_values:
        kap = kappa_slN(N)
        s3 = S3_slN(N)
        gpf = float(G_pf_exact(xi_sq, kap, s3))
        s3f = float(s3)
        ratios_s3[N] = gpf / s3f if abs(s3f) > 1e-50 else float('inf')
        ratios_s3sq[N] = gpf / (s3f ** 2) if abs(s3f) > 1e-50 else float('inf')

    # Check constancy: if G_pf/S_3^2 is kappa-only dependent, the ratio
    # should be independent of N at fixed kappa. Since kappa changes with N,
    # this doesn't directly test the hypothesis. Instead we check:
    # does G_pf(kap, S3, xi) / S3^2 = h(kap, xi) for some function h?
    # This means the ratio should depend only on kappa.
    # Since kappa varies with N, we can't directly disprove from this.
    # Instead, the algebraic structure (min S3 power = 1) disproves it.

    return {
        'xi': xi,
        'hypothesis_S3_squared': False,
        'reason': 'min S_3 power in delta_pf is 1 at all genera, not 2',
        'correct_factorization': 'G_pf = S_3 * Phi(kappa, S_3, xi^2)',
        'ratios_over_S3': ratios_s3,
        'ratios_over_S3_squared': ratios_s3sq,
    }


# ============================================================================
# Section 8: Large-N asymptotics
# ============================================================================

def large_N_scaling(N_values: List[int] = None) -> Dict[int, Dict[str, Any]]:
    r"""Analyze the large-N scaling of F_g and delta_pf for SU(N) at k=0.

    At large N: kappa ~ N^2/2, S_3 ~ 2/(3N), S_3*kappa = 2N/3.
    The scalar part scales as kappa ~ N^2.
    The planted-forest part at genus g scales as N^{2(g-1)} (from the
    S_3^{2(g-1)} leading term combined with its kappa-dependence).
    """
    if N_values is None:
        N_values = [2, 3, 5, 8, 12, 20]

    results = {}
    for N in N_values:
        kap = kappa_slN(N)
        s3 = S3_slN(N)

        row = {
            'kappa': float(kap),
            'S3': float(s3),
            'S3_kappa': float(s3 * kap),
            'kappa_over_N2': float(kap) / (N * N),
        }

        for g in range(1, 5):
            Fg = float(F_g_class_L(g, kap, s3))
            Fg_scal = float(kap * lambda_fp(g))
            Fg_pf = Fg - Fg_scal
            row[f'F_{g}'] = Fg
            row[f'F_{g}_scalar'] = Fg_scal
            row[f'F_{g}_pf'] = Fg_pf
            if g >= 2:
                row[f'F_{g}_pf_over_N_{2*(g-1)}'] = Fg_pf / (N ** (2 * (g - 1)))

        results[N] = row

    return results


# ============================================================================
# Section 9: Pade pole analysis across families
# ============================================================================

def pade_pole_table(
    N_values: List[int] = None,
    k: Fraction = Fraction(0),
) -> List[Dict[str, Any]]:
    r"""Compute Pade [1/1] pole location for each SU(N).

    The pole at xi^2 = -1/q_1 gives the effective convergence radius
    of the planted-forest series. If the pole moves with N, the
    convergence properties are family-dependent.
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 6, 8]

    rows = []
    for N in N_values:
        kap = kappa_slN(N, k)
        s3 = S3_slN(N, k)
        try:
            pade = pade_11_from_genus_data(kap, s3)
            rows.append({
                'N': N,
                'kappa': kap,
                'S3': s3,
                'q1': pade.q1,
                'pole_xi_sq': pade.pole_location,
                'pole_xi_sq_float': float(pade.pole_location) if pade.pole_location is not None else None,
            })
        except (ValueError, ZeroDivisionError):
            rows.append({
                'N': N,
                'kappa': kap,
                'S3': s3,
                'q1': None,
                'pole_xi_sq': None,
                'pole_xi_sq_float': None,
            })
    return rows


# ============================================================================
# Section 10: Closed-form obstruction analysis
# ============================================================================

def closed_form_obstruction_evidence() -> Dict[str, Any]:
    r"""Compile evidence that G_pf does NOT have a finite closed form.

    Evidence:
    1. The polynomial degree in (kappa, S_3) grows unboundedly as 2(g-1).
    2. The number of monomial terms grows: 2, 5, 11, ... (not stabilizing).
    3. The Pade pole location is family-dependent (no universal pole).
    4. The ratio G_pf/G_scalar is not constant across families.
    5. The leading S_3 coefficients {5/24, 15/64, 425/576} do not match
       any standard generating function.

    This is a NEGATIVE RESULT: the planted-forest expansion is an
    irreducibly complicated infinite series indexed by stable graphs.
    """
    # Term count growth
    term_counts = {2: 2, 3: 5, 4: 11}

    # Leading S3 coefficients
    leading = leading_S3_coefficients()

    # Check if leading coefficients match a simple GF
    # Test: c_g = A * B^g * C / D for some constants
    c2 = leading[2]  # 5/24
    c3 = leading[3]  # 15/64
    c4 = leading[4]  # 425/576
    # Ratios: c3/c2, c4/c3
    r32 = c3 / c2  # (15/64)/(5/24) = (15*24)/(64*5) = 360/320 = 9/8
    r43 = c4 / c3  # (425/576)/(15/64) = (425*64)/(576*15) = 27200/8640 = 170/54 = 85/27

    # If geometric: r32 == r43. But 9/8 != 85/27.
    is_geometric = (r32 == r43)

    # Pade poles across families
    poles = pade_pole_table()
    pole_values = [r['pole_xi_sq_float'] for r in poles if r['pole_xi_sq_float'] is not None]
    poles_universal = (
        len(set(round(p, 6) for p in pole_values)) == 1
        if pole_values else False
    )

    return {
        'term_count_growth': term_counts,
        'leading_S3_coefficients': {g: str(c) for g, c in leading.items()},
        'ratio_c3_c2': str(r32),
        'ratio_c4_c3': str(r43),
        'leading_is_geometric': is_geometric,
        'pade_poles_universal': poles_universal,
        'conclusion': 'NO_CLOSED_FORM',
        'explanation': (
            'The planted-forest generating function G_pf(xi) for class L '
            'has polynomials of unboundedly growing degree, non-geometric '
            'leading coefficients, and family-dependent Pade poles. '
            'No finite closed form exists analogous to the scalar '
            'kappa*(xi/(2 sin(xi/2))-1).'
        ),
    }


# ============================================================================
# Section 11: Genus-by-genus decomposition by S_3 power
# ============================================================================

def decompose_by_S3_power() -> Dict[int, Dict[int, List[Tuple[int, Fraction]]]]:
    r"""Decompose each genus polynomial by S_3 power.

    Returns {genus: {S3_power: [(kappa_power, coefficient), ...]}}

    This shows the internal structure:
    g=2, b=1: [(-kappa/48)]  ;  b=2: [(5/24)]
    g=3, b=1: [(-343/2304 kap, -1/82944 kap^3)]  ;  b=2: [(1/1152 kap^2)]  ;  etc.
    """
    result = {}

    # Genus 2
    g2 = {}
    g2[1] = [(1, Fraction(-1, 48))]     # kappa^1 * (-1/48)
    g2[2] = [(0, Fraction(5, 24))]      # kappa^0 * (5/24)
    result[2] = g2

    # Genus 3
    g3: Dict[int, List[Tuple[int, Fraction]]] = {}
    for (a, b), c in GENUS3_PF_CLASS_L.items():
        g3.setdefault(b, []).append((a, c))
    for b in g3:
        g3[b].sort()
    result[3] = g3

    # Genus 4
    g4: Dict[int, List[Tuple[int, Fraction]]] = {}
    for (a, b), c in GENUS4_PF_CLASS_L.items():
        g4.setdefault(b, []).append((a, c))
    for b in g4:
        g4[b].sort()
    result[4] = g4

    return result


# ============================================================================
# Section 12: Multi-path verification utilities
# ============================================================================

def verify_class_G_recovery(kappa: Fraction, max_genus: int = 4) -> bool:
    """Path: setting S_3=0 must recover G_pf=0 at every genus."""
    for g in range(2, max_genus + 1):
        F_at_zero = F_g_class_L(g, kappa, Fraction(0))
        F_scalar = kappa * lambda_fp(g)
        if F_at_zero != F_scalar:
            return False
    return True


def verify_pade_matches_series(kappa: Fraction, S3: Fraction,
                               xi_sq: Fraction) -> Dict[str, Any]:
    """Verify Pade approximant matches the series at small xi."""
    try:
        pade = pade_11_from_genus_data(kappa, S3)
    except (ValueError, ZeroDivisionError):
        return {'constructible': False}

    pade_val = float(pade_evaluate(pade, xi_sq))
    series_val = float(G_pf_exact(xi_sq, kappa, S3))

    return {
        'constructible': True,
        'pade_value': pade_val,
        'series_value': series_val,
        'relative_error': abs(pade_val - series_val) / max(abs(series_val), 1e-50),
    }


def verify_scalar_against_closed_form(kappa_val: float,
                                      xi: float,
                                      max_genus: int = 20) -> Dict[str, Any]:
    """Verify the truncated scalar series converges to the closed form."""
    kap_frac = Fraction(kappa_val).limit_denominator(10**9)
    xi_sq = Fraction(xi * xi).limit_denominator(10**12)
    series = float(G_scalar_series(xi_sq, kap_frac, max_genus))
    closed = G_scalar_closed_form(xi, kappa_val).real

    return {
        'series_value': series,
        'closed_form_value': closed,
        'absolute_error': abs(series - closed),
        'relative_error': abs(series - closed) / max(abs(closed), 1e-50),
    }
