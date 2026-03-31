r"""
prime_locality_minimal_model.py — Testing conj:prime-locality-transfer
for non-lattice rational CFTs (Ising, tricritical Ising, 3-state Potts).

Three independent tests of the prime-locality conjecture:

Test A — Stieltjes moment structure:
  Shadow S_r -> moments c_r = -r S_r -> Hankel matrix.
  Universal analytic result: the quadratic form Q(t) = c^2 + 12ct + alpha*t^2
  has COMPLEX branch points for ALL c > -22/5 (disc factor = -80/(5c+22) < 0).
  Hence the Stieltjes spectral measure rho is necessarily SIGNED,
  not positive-discrete as for lattice VOAs.

Test B — Partition function multiplicativity:
  |eta|^2 Z -> Dirichlet coefficients a_n -> test a_{mn} = a_m a_n
  for coprime (m,n).  Necessary condition for prime-locality.

Test C — Shadow-Hecke Newton bridge:
  VVMF Hecke eigenvalues lambda_p^{(i)} -> Newton power sums
  P_r(p) = sum_i (lambda_p^{(i)})^r -> compare ratios with
  shadow moment ratios mu_{r+1}/mu_r.

References:
  - arithmetic_shadows.tex: conj:prime-locality-transfer (line 4825),
    prop:shadow-symmetric-power (line 4309),
    prop:shadow-spectral-measure (line 1527)
  - shadow_automorphic_bridge.py: shadow coefficients S_r
  - minimal_model_l_functions.py: partition function Dirichlet series
  - vvmf_verifications.py: Hecke eigenvalue extraction

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

try:
    import sympy
    from sympy import Rational, cancel, symbols, nsimplify
    _c_sym = symbols('c')
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False

import mpmath
from mpmath import mp, mpf, fabs

from compute.lib.shadow_automorphic_bridge import (
    virasoro_shadow_gf,
    virasoro_shadow_coefficients_exact,
)
from compute.lib.minimal_model_l_functions import (
    dirichlet_coefficients as ml_dirichlet_coefficients,
    check_multiplicativity as ml_check_multiplicativity,
    ising_model,
    lee_yang_model,
    tricritical_ising_model,
    three_state_potts_model,
)
from compute.lib.vvmf_verifications import (
    compute_hecke_proportionality,
)
from compute.lib.vvmf_hecke import MinimalModel


# ===========================================================================
# Exact shadow coefficient computation
# ===========================================================================

def virasoro_shadow_at_c(c_val: Fraction, max_arity: int = 10) -> Dict[int, Fraction]:
    """Compute S_r at a specific rational c value using exact arithmetic.

    Avoids sympy; uses Fraction for full precision.
    Seeds: S_2 = c/2, S_3 = 2, S_4 = 10/(c(5c+22)).
    Recursion for r >= 5 from the MC bracket.
    """
    S: Dict[int, Fraction] = {}
    c = c_val
    S[2] = c / 2
    S[3] = Fraction(2)
    S[4] = Fraction(10) / (c * (5 * c + 22))

    for r in range(5, max_arity + 1):
        target = r + 2
        total = Fraction(0)
        for j in range(3, target):
            k = target - j
            if k < j:
                break
            if k < 3:
                continue
            bracket = 2 * j * k * S[j] * S[k]
            if j == k:
                bracket = bracket / 2
            total += bracket
        S[r] = -total / (2 * r * c)

    return S


def shadow_moments_at_c(c_val: Fraction, max_arity: int = 10) -> Dict[int, Fraction]:
    """Compute Stieltjes moments c_r = -r S_r at rational c.

    These are power sums of the spectral measure rho:
    c_r = integral lambda^r d rho(lambda)  for r >= 2,
    c_1 = 0  (no linear term in G(t)).
    """
    S = virasoro_shadow_at_c(c_val, max_arity)
    moments = {1: Fraction(0)}
    for r, sr in S.items():
        moments[r] = -r * sr
    return moments


# ===========================================================================
# Test A: Stieltjes moment structure — Hankel matrix analysis
# ===========================================================================

def hankel_matrix_from_moments(
    moments: Dict[int, Fraction],
    size: int,
    offset: int = 1,
) -> np.ndarray:
    """Build Hankel matrix H_{ij} = c_{i+j+offset} for i,j = 0,...,size-1.

    Default offset=1 gives H_{ij} = c_{i+j+1}, appropriate for the
    shifted moment sequence (c_1 = 0, c_2, c_3, ...).
    """
    H = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            key = i + j + offset
            if key in moments:
                H[i, j] = float(moments[key])
    return H


def hankel_analysis(c_val: Fraction, max_size: int = 6) -> Dict[str, Any]:
    """Analyze Hankel matrix rank/eigenvalue structure for Virasoro at c.

    For a discrete N-atom spectral measure, rank(H_n) = N for n >= N.
    For an infinite-atom or continuous measure, rank grows with size.

    Returns rank, determinants, eigenvalues, positive-definiteness.
    """
    max_arity = 2 * max_size + 3
    moments = shadow_moments_at_c(c_val, max_arity)

    results: Dict[str, Any] = {
        'c': str(c_val),
        'c_float': float(c_val),
        'ranks': {},
        'determinants': {},
        'eigenvalues': {},
        'is_positive_semidefinite': {},
        'has_negative_even_moment': False,
    }

    # Check sign of even moments (positive measure requires c_{2k} >= 0)
    for r in [2, 4, 6, 8]:
        if r in moments and moments[r] < 0:
            results['has_negative_even_moment'] = True
            break

    for n in range(1, max_size + 1):
        H = hankel_matrix_from_moments(moments, n, offset=1)
        evals = sorted(np.linalg.eigvalsh(H))
        det_val = np.linalg.det(H)
        rank = np.linalg.matrix_rank(H, tol=1e-8)
        results['eigenvalues'][n] = evals
        results['determinants'][n] = det_val
        results['ranks'][n] = rank
        results['is_positive_semidefinite'][n] = all(e > -1e-10 for e in evals)

    # Estimate support size from Hankel rank.
    # Skip n=1: c_1 = 0 makes it trivially rank 0 for ALL Virasoro.
    # For n >= 2: if rank < n, the measure has finite support.
    atoms_est = max_size
    for n in range(2, max_size + 1):
        if results['ranks'][n] < n:
            atoms_est = results['ranks'][n]
            break
    results['spectral_atoms_estimate'] = atoms_est
    results['infinite_support'] = (atoms_est == max_size)

    return results


def stieltjes_discriminant_analysis(c_val: float) -> Dict[str, Any]:
    """Compute Stieltjes discriminant for the quadratic form Q(t).

    Q(t) = c^2 + 12ct + alpha*t^2,  alpha = (180c + 872)/(5c + 22).

    The branch points of H(t) = t^2 sqrt(Q(t)) are roots of Q(t):
    disc(Q) = (12c)^2 - 4*alpha*c^2 = 4c^2(36 - alpha).

    UNIVERSAL: 36 - alpha = -80/(5c+22) < 0 for c > -22/5.
    So Q has COMPLEX roots and rho is SIGNED for ALL Virasoro theories.
    """
    if abs(5 * c_val + 22) < 1e-12:
        return {'c': c_val, 'singular': True, 'reason': 'Lee-Yang pole 5c+22=0'}

    alpha = (180 * c_val + 872) / (5 * c_val + 22)
    disc_factor = 36 - alpha  # = -80/(5c+22)
    disc = 4 * c_val**2 * disc_factor

    # Verify the universal formula
    expected_disc_factor = -80 / (5 * c_val + 22)
    formula_verified = abs(disc_factor - expected_disc_factor) < 1e-10

    return {
        'c': c_val,
        'alpha': alpha,
        'disc_factor': disc_factor,
        'discriminant': disc,
        'branch_points_complex': disc < 0,
        'measure_necessarily_signed': disc < 0,
        'universal_formula_verified': formula_verified,
    }


# ===========================================================================
# Test B: Partition function multiplicativity
# ===========================================================================

def multiplicativity_report(
    model: MinimalModel,
    num_terms: int = 80,
    dps: int = 50,
) -> Dict[str, Any]:
    """Test multiplicativity of |eta|^2 Z Dirichlet coefficients.

    Returns structured report with:
      - is_multiplicative: bool
      - first failures (m, n, defect)
      - a_p for small primes
      - Hecke recursion test: a_{p^2} vs a_p^2 - chi(p) p^{k-1}
    """
    mp.dps = dps
    coeffs = ml_dirichlet_coefficients(model, num_terms=num_terms, dps=dps)

    is_mult, failures = ml_check_multiplicativity(coeffs, max_n=min(num_terms // 3, 30))

    primes = [2, 3, 5, 7, 11, 13]
    a_p = {}
    for p in primes:
        if p < len(coeffs):
            a_p[p] = float(coeffs[p])

    # Hecke recursion at prime-squares: a_{p^2} = a_p^2 - a_1 * chi
    # For weight-0 modular function: chi(p) depends on the model
    hecke_recursion = {}
    a_1 = float(coeffs[1]) if len(coeffs) > 1 else 0.0
    for p in primes:
        if p**2 < len(coeffs) and a_1 != 0:
            actual = float(coeffs[p**2])
            # Simple test: a_{p^2} = a_p^2 - a_1 (weight-0 Hecke relation)
            predicted_w0 = float(coeffs[p])**2 - a_1
            hecke_recursion[p] = {
                'a_p': float(coeffs[p]),
                'a_p2_actual': actual,
                'a_p2_predicted_w0': predicted_w0,
                'defect_w0': abs(actual - predicted_w0),
            }

    # Compute overall multiplicativity defect
    max_defect = 0.0
    if failures:
        max_defect = max(float(f[2]) for f in failures)

    return {
        'model': f"M({model.p},{model.q})",
        'c': float(Fraction(1) - Fraction(6) * Fraction(
            (model.p - model.q)**2, model.p * model.q)),
        'is_multiplicative': is_mult,
        'num_failures': len(failures),
        'max_defect': max_defect,
        'first_failures': [(m, n, float(d)) for m, n, d in failures[:5]],
        'a_p': a_p,
        'a_0': float(coeffs[0]) if coeffs else None,
        'a_1': a_1,
        'hecke_recursion': hecke_recursion,
    }


# ===========================================================================
# Test C: Shadow-Hecke Newton bridge
# ===========================================================================

def hecke_eigenvalue_data(
    model: MinimalModel,
    primes: List[int],
    num_terms: int = 50,
    dps: int = 50,
) -> Dict[int, Dict[str, Any]]:
    """Extract Hecke eigenvalues at each prime from the VVMF.

    For each prime p, tests whether each character chi_{r,s} is an
    eigenform of T_p and extracts eigenvalues.
    """
    mp.dps = dps
    labels = model.primary_labels()

    result = {}
    for p in primes:
        eigenvalues = []
        eigenform_count = 0
        non_eigenform_count = 0

        for lab in labels:
            data = compute_hecke_proportionality(
                model, lab.r, lab.s, p, num_terms=num_terms, dps=dps
            )
            if data['is_eigenform'] and data['eigenvalue'] is not None:
                eigenvalues.append(float(data['eigenvalue']))
                eigenform_count += 1
            else:
                non_eigenform_count += 1

        # Power sums of eigenvalues
        power_sums = {}
        for r in range(1, 9):
            power_sums[r] = sum(lam**r for lam in eigenvalues)

        result[p] = {
            'eigenvalues': eigenvalues,
            'num_eigenforms': eigenform_count,
            'num_non_eigenforms': non_eigenform_count,
            'total_primaries': len(labels),
            'all_eigenforms': non_eigenform_count == 0,
            'power_sums': power_sums,
        }

    return result


def shadow_hecke_bridge(
    model: MinimalModel,
    primes: Optional[List[int]] = None,
    max_arity: int = 8,
    num_terms: int = 50,
    dps: int = 50,
) -> Dict[str, Any]:
    """Compare shadow moments with Hecke power sums.

    For each prime p, computes P_r(p) = sum_i lambda_p^{(i)}^r
    and compares the RATIOS P_{r+1}/P_r with shadow moment ratios
    mu_{r+1}/mu_r.  If prime-locality holds and a single eigenvalue
    dominates at each prime, these ratios should converge to a
    common value related to the dominant eigenvalue.
    """
    if primes is None:
        primes = [2, 3, 5]

    c_frac = Fraction(1) - Fraction(6) * Fraction(
        (model.p - model.q)**2, model.p * model.q
    )
    c_val = float(c_frac)

    # Shadow moments (exact)
    moments = shadow_moments_at_c(c_frac, max_arity)
    moments_float = {r: float(v) for r, v in moments.items()}

    # Shadow moment ratios
    shadow_ratios = {}
    for r in range(2, max_arity):
        if r in moments_float and r + 1 in moments_float:
            if abs(moments_float[r]) > 1e-30:
                shadow_ratios[r] = moments_float[r + 1] / moments_float[r]

    # Hecke data
    hecke = hecke_eigenvalue_data(model, primes, num_terms=num_terms, dps=dps)

    # Hecke power sum ratios
    hecke_ratios = {}
    for p in primes:
        ps = hecke[p]['power_sums']
        ratios_p = {}
        for r in range(1, max_arity):
            if r in ps and r + 1 in ps and abs(ps[r]) > 1e-30:
                ratios_p[r] = ps[r + 1] / ps[r]
        hecke_ratios[p] = ratios_p

    # Check if dominant-eigenvalue ratio from Hecke matches shadow ratio
    # at large r (asymptotic regime)
    convergence_check = {}
    for p in primes:
        if len(hecke[p]['eigenvalues']) >= 1:
            dominant = max(hecke[p]['eigenvalues'], key=abs)
            convergence_check[p] = {
                'dominant_eigenvalue': dominant,
                'shadow_ratio_at_max_r': shadow_ratios.get(max_arity - 1),
            }

    return {
        'model': f"M({model.p},{model.q})",
        'c': c_val,
        'shadow_moments': moments_float,
        'shadow_ratios': shadow_ratios,
        'hecke_data': hecke,
        'hecke_ratios': hecke_ratios,
        'convergence_check': convergence_check,
    }


# ===========================================================================
# Calibration: class G/L lattice tests
# ===========================================================================

def class_g_hankel_calibration(c_int: int = 8) -> Dict[str, Any]:
    """Calibration: class G (lattice, depth 2) Hankel structure.

    S_2 = c/2, S_r = 0 for r >= 3.
    Moments: c_1 = 0, c_2 = -c, c_r = 0 for r >= 3.

    Hankel H_{ij} = c_{i+j+1} has the form:
      [[0, -c, 0, ...], [-c, 0, 0, ...], [0, 0, 0, ...], ...]
    Rank = 2 = shadow depth r_max.
    """
    moments = {1: Fraction(0), 2: Fraction(-c_int)}
    for r in range(3, 14):
        moments[r] = Fraction(0)

    H = hankel_matrix_from_moments(moments, 4, offset=1)
    evals = sorted(np.linalg.eigvalsh(H))
    rank = np.linalg.matrix_rank(H, tol=1e-8)

    return {
        'family': f'lattice_c{c_int}',
        'c': c_int,
        'shadow_depth': 2,
        'archetype': 'G',
        'hankel_rank': rank,
        'expected_rank': 2,  # = shadow depth
        'rank_correct': rank == 2,
        'eigenvalues': evals,
    }


def class_l_hankel_calibration(k_val: Fraction = Fraction(1)) -> Dict[str, Any]:
    """Calibration: class L (affine, depth 3) Hankel structure.

    S_2 = kappa = 3(k+2)/4, S_3 = 2, S_r = 0 for r >= 4.
    Moments: c_1 = 0, c_2 = -2*kappa, c_3 = -6, c_r = 0 for r >= 4.
    Hankel rank = 3 = shadow depth.
    """
    kappa = Fraction(3) * (k_val + 2) / 4
    moments = {
        1: Fraction(0),
        2: -2 * kappa,
        3: Fraction(-6),
    }
    for r in range(4, 14):
        moments[r] = Fraction(0)

    H = hankel_matrix_from_moments(moments, 4, offset=1)
    evals = sorted(np.linalg.eigvalsh(H))
    rank = np.linalg.matrix_rank(H, tol=1e-8)

    return {
        'family': f'affine_sl2_k{k_val}',
        'kappa': float(kappa),
        'shadow_depth': 3,
        'archetype': 'L',
        'hankel_rank': rank,
        'expected_rank': 3,  # = shadow depth
        'rank_correct': rank == 3,
        'eigenvalues': evals,
    }


# ===========================================================================
# Shadow growth rate diagnostic
# ===========================================================================

def shadow_growth_diagnostic(c_val: Fraction, max_arity: int = 12) -> Dict[str, Any]:
    """Compute shadow growth rate and asymptotic structure.

    For class M: S_r ~ A * rho^r * r^{-5/2} * cos(r*theta + phi)
    The oscillation (theta != 0) is equivalent to the signed measure.
    The growth rate rho determines the Borel singularity at xi = 1/rho.

    For large r: |S_{r+1}/S_r| -> rho (shadow radius).
    arg(S_{r+1}/S_r) -> theta (oscillation phase).
    """
    S = virasoro_shadow_at_c(c_val, max_arity)
    S_float = {r: float(v) for r, v in S.items()}

    ratios = {}
    for r in range(2, max_arity):
        if r in S_float and r + 1 in S_float and abs(S_float[r]) > 1e-30:
            ratios[r] = S_float[r + 1] / S_float[r]

    # Estimate rho from last few ratios
    last_ratios = [abs(ratios[r]) for r in sorted(ratios.keys())[-3:]]
    rho_est = np.mean(last_ratios) if last_ratios else None

    # Sign pattern
    signs = {r: (1 if S_float[r] > 0 else -1 if S_float[r] < 0 else 0)
             for r in sorted(S_float.keys())}

    return {
        'c': str(c_val),
        'c_float': float(c_val),
        'S_r': S_float,
        'successive_ratios': ratios,
        'rho_estimate': rho_est,
        'sign_pattern': signs,
    }


# ===========================================================================
# Full bridge report
# ===========================================================================

def full_prime_locality_report(
    model: MinimalModel,
    primes: Optional[List[int]] = None,
    max_arity: int = 8,
    num_terms_mult: int = 80,
    num_terms_hecke: int = 50,
    dps: int = 50,
) -> Dict[str, Any]:
    """Run all three prime-locality tests for a minimal model.

    Returns:
      test_A: Hankel + discriminant analysis
      test_B: multiplicativity of partition function Dirichlet series
      test_C: shadow-Hecke eigenvalue comparison
      diagnosis: summary finding
    """
    if primes is None:
        primes = [2, 3, 5]

    c_frac = Fraction(1) - Fraction(6) * Fraction(
        (model.p - model.q)**2, model.p * model.q
    )
    c_val = float(c_frac)

    report: Dict[str, Any] = {
        'model': f"M({model.p},{model.q})",
        'c': c_val,
        'c_exact': str(c_frac),
    }

    # Test A
    report['test_A_hankel'] = hankel_analysis(c_frac, max_size=min(max_arity - 1, 6))
    report['test_A_discriminant'] = stieltjes_discriminant_analysis(c_val)
    report['test_A_growth'] = shadow_growth_diagnostic(c_frac, max_arity=max_arity + 4)

    # Test B
    report['test_B_multiplicativity'] = multiplicativity_report(
        model, num_terms=num_terms_mult, dps=dps
    )

    # Test C
    report['test_C_bridge'] = shadow_hecke_bridge(
        model, primes=primes, max_arity=max_arity,
        num_terms=num_terms_hecke, dps=dps
    )

    # Diagnosis
    mult_ok = report['test_B_multiplicativity']['is_multiplicative']
    signed = report['test_A_discriminant']['measure_necessarily_signed']
    full_rank = report['test_A_hankel']['infinite_support']

    if not mult_ok:
        diagnosis = 'MULTIPLICATIVITY_FAILS'
        detail = (f"Partition function Dirichlet coefficients are NOT multiplicative. "
                  f"{report['test_B_multiplicativity']['num_failures']} failures found. "
                  f"Prime-locality requires a different mechanism than naive Euler product.")
    elif signed and full_rank:
        diagnosis = 'SIGNED_MEASURE_FULL_RANK'
        detail = ("Stieltjes measure is signed with infinite support "
                  "(Hankel has full rank). Multiplicativity holds. "
                  "Prime-locality is viable but spectral measure differs "
                  "qualitatively from lattice case (positive discrete).")
    else:
        diagnosis = 'PARTIAL_EVIDENCE'
        detail = "Mixed signals; further investigation needed."

    report['diagnosis'] = diagnosis
    report['detail'] = detail

    return report
