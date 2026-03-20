r"""
minimal_model_l_functions.py — L-functions from minimal model characters.

The spectral continuation programme (Approach B, VVMF Hecke) aims to extend
the shadow-spectral correspondence from lattice VOAs to rational VOAs via
VVMF Rankin-Selberg.  This module extracts concrete L-functions from minimal
model partition functions and tests their arithmetic content.

Given a rational CFT with partition function Z(tau) = sum_i |chi_i(tau)|^2
(diagonal modular invariant), the "constrained Epstein" is

    epsilon^c_s(y) = y^{c/24} |eta(tau)|^2 Z(tau)|_{tau = iy}

and the Dirichlet series D(s) = sum_{n >= 1} a_n n^{-s} is formed from the
Fourier coefficients of this combination.

Supported models (all via Rocha-Caridi characters from vvmf_hecke.py):
  - Ising:             c = 1/2,  M(4,3),  3 primaries
  - Lee-Yang:          c = -22/5, M(5,2), 2 primaries (non-unitary)
  - Tricritical Ising: c = 7/10, M(5,4), 6 primaries
  - 3-state Potts:     c = 4/5,  M(6,5), 10 primaries

For each model we compute:
  1. Partition function Z(tau) at tau = iy for various y
  2. Constrained Epstein epsilon^c_s = y^{c/24} |eta|^2 Z
  3. Dirichlet coefficients a_n from q-expansion of |eta|^2 Z
  4. Multiplicativity test: is a_{mn} = a_m a_n for gcd(m,n)=1?
  5. L-function identification against known zeta/L-functions
  6. Shadow depth prediction from L-function content

CONVENTION: Characters follow the vvmf_hecke.py labeling. The Ising
primaries are (1,1) h=0, (2,1) h=1/16, (1,2) h=1/2 under M(4,3).

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Tuple

import mpmath
from mpmath import mp, mpf, mpc, pi, exp, sin, sqrt, log, fsum, power, floor
from mpmath import matrix as mpmatrix

from compute.lib.vvmf_hecke import (
    MinimalModel,
    MinimalModelLabel,
    character_qseries,
    character_value,
    character_vector,
    s_matrix,
    t_matrix,
    _eta_coeffs,
    _inverse_eta_coeffs,
    ising_model,
    tricritical_ising_model,
    three_state_potts_model,
    DEFAULT_DPS,
)


# ---------------------------------------------------------------------------
# Named models (extending vvmf_hecke)
# ---------------------------------------------------------------------------

def lee_yang_model() -> MinimalModel:
    """Lee-Yang model M(5, 2), c = -22/5, 2 primaries."""
    return MinimalModel(p=5, q=2)


# Alias for convenience
def all_named_models() -> Dict[str, MinimalModel]:
    """Return dict of all named minimal models."""
    return {
        'Ising': ising_model(),
        'Lee-Yang': lee_yang_model(),
        'Tricritical Ising': tricritical_ising_model(),
        '3-state Potts': three_state_potts_model(),
    }


# ---------------------------------------------------------------------------
# Partition function Z(tau) = sum_i |chi_i(tau)|^2  (diagonal invariant)
# ---------------------------------------------------------------------------

def diagonal_partition_function(
    model: MinimalModel,
    tau: mpc,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> mpf:
    """Evaluate Z(tau) = sum_i |chi_i(tau)|^2 at a given tau.

    This is the diagonal modular invariant.
    Returns a real positive value.
    """
    mp.dps = dps
    chi_vec = character_vector(model, tau, num_terms=num_terms, dps=dps)
    return fsum(abs(c) ** 2 for c in chi_vec)


def partition_function_at_imaginary(
    model: MinimalModel,
    y: mpf,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> mpf:
    """Evaluate Z(iy) for real positive y."""
    mp.dps = dps
    tau = mpc(0, y)
    return diagonal_partition_function(model, tau, num_terms=num_terms, dps=dps)


# ---------------------------------------------------------------------------
# |eta(tau)|^2 at tau = iy
# ---------------------------------------------------------------------------

def _eta_value(tau: mpc, num_terms: int = 200, dps: int = DEFAULT_DPS) -> mpc:
    """Evaluate eta(tau) = q^{1/24} prod_{n>=1}(1 - q^n)."""
    mp.dps = dps
    q = exp(2 * pi * mpc(0, 1) * tau)
    # q^{1/24}
    prefactor = power(q, mpf(1) / mpf(24))
    # prod(1 - q^n) from eta coefficients
    prod_val = mpc(1, 0)
    for n in range(1, num_terms):
        prod_val *= (1 - power(q, n))
    return prefactor * prod_val


def eta_norm_squared_at_iy(
    y: mpf,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> mpf:
    """Evaluate |eta(iy)|^2 for real positive y."""
    mp.dps = dps
    tau = mpc(0, y)
    eta_val = _eta_value(tau, num_terms=num_terms, dps=dps)
    return abs(eta_val) ** 2


# ---------------------------------------------------------------------------
# Constrained Epstein: epsilon^c_s(y) = y^{c/24} |eta(iy)|^2 Z(iy)
# ---------------------------------------------------------------------------

def constrained_epstein(
    model: MinimalModel,
    y: mpf,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> mpf:
    """Evaluate the constrained Epstein epsilon^c_s(y) = y^{c/24} |eta|^2 Z.

    At tau = iy, this combines the modular weight of the partition function
    with the eta normalization to produce a quantity amenable to Mellin
    transform / Dirichlet series extraction.
    """
    mp.dps = dps
    c_val = model.central_charge_mpf
    Z_val = partition_function_at_imaginary(model, y, num_terms=num_terms, dps=dps)
    eta_sq = eta_norm_squared_at_iy(y, num_terms=num_terms, dps=dps)
    return power(y, c_val / 24) * eta_sq * Z_val


# ---------------------------------------------------------------------------
# Dirichlet coefficients from q-expansion of |eta|^2 Z
# ---------------------------------------------------------------------------

def _eta_sq_coeffs(num_terms: int) -> List[int]:
    """Coefficients of q^{-1/12} |eta(tau)|^2 at tau = iy (real q = e^{-2 pi y}).

    |eta|^2 = q^{1/12} prod (1 - q^n)^2    (at tau = iy, q is real)

    So q^{-1/12} |eta|^2 = prod(1 - q^n)^2.
    Coefficients of prod(1-q^n)^2 = convolution of eta-pentagonal coefficients
    with themselves.
    """
    eta = _eta_coeffs(num_terms)
    result = [0] * num_terms
    for i in range(num_terms):
        if eta[i] == 0:
            continue
        for j in range(num_terms - i):
            if eta[j] == 0:
                continue
            result[i + j] += eta[i] * eta[j]
    return result


def _norm_sq_character_coeffs(
    model: MinimalModel,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> List[mpf]:
    """Compute coefficients of sum_i |chi_i|^2 in the q-expansion.

    For tau = iy, q = e^{-2 pi y} is real, so |chi_i|^2 = chi_i^2
    (characters are real at imaginary tau).

    chi_i = q^{h_i - c/24} sum_{n>=0} d_n^{(i)} q^n

    |chi_i|^2 = q^{2(h_i - c/24)} (sum d_n q^n)^2

    For the diagonal Z = sum_i |chi_i|^2, we need to combine these.

    The ground state exponent for each primary is e_i = h_i - c/24.
    These are all rational, and Z has the form:
        Z = sum_i q^{2 e_i} (sum_n d_n^(i) q^n)^2

    |eta|^2 = q^{1/12} prod(1-q^n)^2

    So |eta|^2 Z = sum_i q^{1/12 + 2 e_i} prod(1-q^n)^2 (sum d_n q^n)^2

    For the Dirichlet coefficients, we work with:
    prod(1-q^n)^2 * (sum d_n q^n)^2 = (eta-hat * chi-hat)^2
    where hats denote the q^0-normalized parts.

    Return the integer-indexed coefficients a_n of the |eta|^2 Z q-expansion
    (after factoring out the leading q-power).
    """
    mp.dps = dps
    labels = model.primary_labels()

    # For each primary, compute d_n (level degeneracies)
    all_degeneracies = []
    for lab in labels:
        all_degeneracies.append(
            character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        )

    # Compute prod(1-q^n)^2 * (d_n)^2 for each primary, then sum.
    # The eta^2 factor: [prod(1-q^n)]^2 coefficients
    eta_sq = _eta_sq_coeffs(num_terms)

    # For each primary i, form f_i = [prod(1-q^n)] * [sum d_n q^n],
    # then f_i^2 gives the |eta chi_i|^2 contribution (up to q-powers).
    # Actually we want prod(1-q^n)^2 * (sum d_n q^n)^2.
    # This equals [prod(1-q^n) * sum d_n q^n]^2.
    # But note that prod(1-q^n) * sum d_n q^n = theta_{r,s}
    # (the Rocha-Caridi theta function). So the square of the theta
    # function gives the contribution of each primary.

    # More directly: convolve eta_sq with (d * d) for each primary.
    result = [mpf(0)] * num_terms

    for i_lab, lab in enumerate(labels):
        d = all_degeneracies[i_lab]
        # (sum d_n q^n)^2 coefficients
        d_sq = [mpf(0)] * num_terms
        for a in range(num_terms):
            if d[a] == 0:
                continue
            for b in range(num_terms - a):
                if d[b] == 0:
                    continue
                d_sq[a + b] += d[a] * d[b]

        # Convolve with eta_sq
        for m in range(num_terms):
            val = mpf(0)
            for k in range(m + 1):
                if eta_sq[k] == 0:
                    continue
                val += mpf(eta_sq[k]) * d_sq[m - k]
            result[m] += val

    return result


def dirichlet_coefficients(
    model: MinimalModel,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> List[mpf]:
    """Extract the Dirichlet series coefficients a_n for the minimal model.

    These are the coefficients of the q-expansion of |eta|^2 Z
    (the numerator of the constrained Epstein, with leading q-power factored out).

    The Dirichlet series is D(s) = sum_{n >= 1} a_n n^{-s}.
    """
    mp.dps = dps
    return _norm_sq_character_coeffs(model, num_terms=num_terms, dps=dps)


# ---------------------------------------------------------------------------
# Dirichlet series evaluation
# ---------------------------------------------------------------------------

def dirichlet_series(
    model: MinimalModel,
    s_param: mpc,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> mpc:
    """Evaluate D(s) = sum_{n >= 1} a_n n^{-s}."""
    mp.dps = dps
    coeffs = dirichlet_coefficients(model, num_terms=num_terms, dps=dps)
    val = mpc(0)
    for n in range(1, min(num_terms, len(coeffs))):
        if coeffs[n] != 0:
            val += coeffs[n] / power(mpf(n), s_param)
    return val


# ---------------------------------------------------------------------------
# Multiplicativity test
# ---------------------------------------------------------------------------

def check_multiplicativity(
    coeffs: List[mpf],
    max_n: int = 100,
    tol: float = 1e-10,
) -> Tuple[bool, List[Tuple[int, int, mpf]]]:
    """Test if the Dirichlet coefficients a_n are multiplicative.

    A sequence is multiplicative if a_{mn} = a_m a_n whenever gcd(m,n) = 1.

    Returns (is_multiplicative, list_of_failures).
    Each failure is (m, n, |a_{mn} - a_m a_n|).
    """
    failures = []
    N = min(max_n + 1, len(coeffs))
    for m in range(2, N):
        for n in range(2, N):
            if m * n >= N:
                break
            if gcd(m, n) != 1:
                continue
            diff = abs(coeffs[m * n] - coeffs[m] * coeffs[n])
            if diff > tol:
                failures.append((m, n, diff))
    return (len(failures) == 0, failures)


def check_completely_multiplicative(
    coeffs: List[mpf],
    max_n: int = 100,
    tol: float = 1e-10,
) -> Tuple[bool, List[Tuple[int, int, mpf]]]:
    """Test if the Dirichlet coefficients a_n are completely multiplicative.

    A sequence is completely multiplicative if a_{mn} = a_m a_n for ALL m, n.
    """
    failures = []
    N = min(max_n + 1, len(coeffs))
    for m in range(2, N):
        for n in range(2, N):
            if m * n >= N:
                break
            diff = abs(coeffs[m * n] - coeffs[m] * coeffs[n])
            if diff > tol:
                failures.append((m, n, diff))
    return (len(failures) == 0, failures)


# ---------------------------------------------------------------------------
# L-function identification
# ---------------------------------------------------------------------------

def _riemann_zeta_coeffs(num_terms: int) -> List[mpf]:
    """Coefficients of the Riemann zeta Dirichlet series: a_n = 1 for all n."""
    return [mpf(1)] * num_terms


def _dirichlet_character_coeffs(
    d: int,
    num_terms: int,
    dps: int = DEFAULT_DPS,
) -> List[mpf]:
    """Coefficients of L(s, chi_d) for the Kronecker symbol chi_d = (d/.).

    For fundamental discriminant d, chi_d(n) = Kronecker symbol (d|n).
    """
    mp.dps = dps

    def kronecker_symbol(d_val: int, n_val: int) -> int:
        """Kronecker symbol (d|n) via mpmath."""
        if n_val == 0:
            return 1 if abs(d_val) == 1 else 0
        # Use the Jacobi symbol extension
        # For fundamental discriminants, reduce to Legendre for odd primes
        if n_val < 0:
            n_val = -n_val
        result = 1
        # Factor out powers of 2
        n_temp = n_val
        while n_temp % 2 == 0:
            n_temp //= 2
            if d_val % 8 in (3, 5):
                result = -result
        # Now n_temp is odd; use Jacobi symbol
        if n_temp == 1:
            return result
        # Jacobi symbol (d | n_temp) with n_temp odd
        a = d_val % n_temp
        if a < 0:
            a += n_temp
        b = n_temp
        while a != 0:
            while a % 2 == 0:
                a //= 2
                if b % 8 in (3, 5):
                    result = -result
            a, b = b, a
            if a % 4 == 3 and b % 4 == 3:
                result = -result
            a = a % b
        if b == 1:
            return result
        return 0

    coeffs = [mpf(0)] * num_terms
    for n in range(num_terms):
        coeffs[n] = mpf(kronecker_symbol(d, n))
    return coeffs


def identify_l_function(
    coeffs: List[mpf],
    max_n: int = 50,
    tol: float = 1e-6,
    dps: int = DEFAULT_DPS,
) -> List[Dict]:
    """Attempt to identify the Dirichlet series from known L-functions.

    Compares the first max_n coefficients against:
      - Riemann zeta (a_n = 1)
      - L(s, chi_d) for small fundamental discriminants d
      - Scaled versions thereof
      - Products of known L-functions

    Returns a list of matches with quality scores.
    """
    mp.dps = dps
    N = min(max_n, len(coeffs))
    matches = []

    if N < 3:
        return matches

    # Normalize: if a_1 != 0, try a_n / a_1
    a1 = coeffs[1] if len(coeffs) > 1 else mpf(0)
    if abs(a1) < 1e-30:
        return matches

    normalized = [coeffs[n] / a1 for n in range(N)]

    # Test against zeta: a_n = 1 for all n
    zeta_err = max(abs(normalized[n] - 1) for n in range(1, N))
    if zeta_err < tol:
        matches.append({
            'name': 'zeta(s)',
            'scale': a1,
            'error': float(zeta_err),
        })

    # Test against L(s, chi_d) for small discriminants
    for d in [-4, -3, 5, -7, -8, 8, 12, -11, 13, -15, 17, -19, -20, 21, -23, -24]:
        lchi = _dirichlet_character_coeffs(d, N, dps=dps)
        if all(lchi[n] == 0 for n in range(1, min(5, N))):
            continue
        # Check if normalized ~ constant * lchi
        # Find scaling from first nonzero coefficient
        scale = None
        for n in range(1, N):
            if abs(lchi[n]) > 0.5:
                scale = normalized[n] / lchi[n]
                break
        if scale is None:
            continue

        rescaled_err = mpf(0)
        count = 0
        for n in range(1, N):
            if abs(lchi[n]) > 0.5:
                err = abs(normalized[n] - scale * lchi[n])
                if err > rescaled_err:
                    rescaled_err = err
                count += 1
        if count > 3 and rescaled_err < tol:
            matches.append({
                'name': f'L(s, chi_{d})',
                'scale': a1 * scale,
                'error': float(rescaled_err),
            })

    # Test against squared degeneracies (partition function squared)
    # This checks if D(s) has the form sum p(n)^2 n^{-s}
    inv_eta = _inverse_eta_coeffs(N)
    part_sq_err = max(abs(normalized[n] - mpf(inv_eta[n]) ** 2)
                      for n in range(1, N) if inv_eta[n] > 0)
    if part_sq_err < tol * max(1, abs(normalized[N - 1])):
        matches.append({
            'name': 'partition_squared',
            'scale': a1,
            'error': float(part_sq_err),
        })

    return matches


# ---------------------------------------------------------------------------
# S-matrix computation (re-exported for convenience with verification)
# ---------------------------------------------------------------------------

def compute_s_matrix(
    model: MinimalModel,
    dps: int = DEFAULT_DPS,
) -> mpmatrix:
    """Compute and return the modular S-matrix. Wrapper around vvmf_hecke."""
    return s_matrix(model, dps=dps)


def verify_s_matrix(
    model: MinimalModel,
    dps: int = DEFAULT_DPS,
) -> Dict[str, mpf]:
    """Verify S-matrix properties: unitarity, symmetry, S^2 = C."""
    mp.dps = dps
    S = s_matrix(model, dps=dps)
    n = S.rows

    # Unitarity: S^dag S = I
    SdagS = S.T * S  # S is real
    unit_err = mpf(0)
    for i in range(n):
        for j in range(n):
            expected = mpf(1) if i == j else mpf(0)
            err = abs(SdagS[i, j] - expected)
            if err > unit_err:
                unit_err = err

    # Symmetry: S = S^T
    sym_err = mpf(0)
    for i in range(n):
        for j in range(n):
            err = abs(S[i, j] - S[j, i])
            if err > sym_err:
                sym_err = err

    # S^2 should be charge conjugation (permutation matrix)
    S2 = S * S
    s2_diag_err = mpf(0)
    for i in range(n):
        # Check that each row of S^2 has exactly one entry close to +/-1
        max_entry = max(abs(S2[i, j]) for j in range(n))
        s2_diag_err = max(s2_diag_err, abs(max_entry - 1))

    return {
        'unitarity_error': unit_err,
        'symmetry_error': sym_err,
        's_squared_error': s2_diag_err,
    }


# ---------------------------------------------------------------------------
# Shadow depth prediction from L-function content
# ---------------------------------------------------------------------------

# Known shadow depths from the OPE structure (from CLAUDE.md):
# Heisenberg: G class, r_max = 2
# Affine: L class, r_max = 3
# Beta-gamma: C class, r_max = 4
# Virasoro/W_N: M class, r_max = infinity
#
# Minimal models are quotients of Virasoro, so their shadow depth
# depends on the specific model. The shadow-L correspondence predicts:
#   depth d -> d-1 critical lines in the associated L-function(s).
#
# For rational CFTs (minimal models), the characters are VVMFs whose
# component L-functions have finitely many critical lines. This gives
# a FINITE shadow depth prediction.

KNOWN_SHADOW_DEPTHS = {
    'Ising': 'M',        # Virasoro quotient -> infinite tower (as Virasoro)
    'Lee-Yang': 'M',     # non-unitary Virasoro quotient
    'Tricritical Ising': 'M',
    '3-state Potts': 'M',
}

# For minimal models as simple quotient VOAs, the shadow depth is
# potentially FINITE because the null vectors truncate the OPE tower.
# The prediction from L-function content:

def predict_shadow_depth_from_dirichlet(
    model: MinimalModel,
    name: str,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> Dict:
    """Predict shadow depth from the Dirichlet series content.

    The shadow-L correspondence says: depth d implies d-1 critical lines.
    For the minimal model Dirichlet series, we count:
      - Whether D(s) is a single L-function (1 critical line -> depth 2)
      - Whether D(s) factors as product of L-functions (count factors)
      - Whether D(s) has novel analytic structure

    Returns a dict with prediction and evidence.
    """
    mp.dps = dps
    coeffs = dirichlet_coefficients(model, num_terms=num_terms, dps=dps)
    is_mult, failures = check_multiplicativity(coeffs, max_n=min(50, num_terms))
    matches = identify_l_function(coeffs, max_n=min(50, num_terms), dps=dps)

    # Count effective critical lines from identified L-functions
    num_l_factors = len(matches) if matches else 0

    # If multiplicative: single Euler product -> possibly 1 critical line
    # If not multiplicative: multiple L-function components
    if is_mult and num_l_factors <= 1:
        predicted_depth = 2  # Gaussian class
    elif is_mult:
        predicted_depth = num_l_factors + 1
    else:
        # Non-multiplicative -> product of L-functions or novel
        # Count from failure pattern
        predicted_depth = None  # Cannot determine from multiplicativity alone

    return {
        'model_name': name,
        'central_charge': str(model.central_charge),
        'num_primaries': model.num_primaries(),
        'is_multiplicative': is_mult,
        'num_mult_failures': len(failures),
        'identified_l_functions': matches,
        'predicted_depth': predicted_depth,
        'known_virasoro_class': KNOWN_SHADOW_DEPTHS.get(name, 'unknown'),
    }


# ---------------------------------------------------------------------------
# Collected spectral data for a model
# ---------------------------------------------------------------------------

@dataclass
class MinimalModelSpectralData:
    """Full spectral data extracted from a minimal model's partition function."""
    name: str
    model: MinimalModel
    partition_values: Dict[float, mpf]        # y -> Z(iy)
    constrained_epstein_values: Dict[float, mpf]  # y -> epsilon(y)
    dirichlet_coefficients: List[mpf]
    is_multiplicative: bool
    multiplicativity_failures: List[Tuple[int, int, mpf]]
    s_matrix_data: mpmatrix
    s_matrix_checks: Dict[str, mpf]
    l_function_matches: List[Dict]
    shadow_prediction: Dict


def compute_full_spectral_data(
    model: MinimalModel,
    name: str,
    y_values: Optional[List[float]] = None,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> MinimalModelSpectralData:
    """Compute all spectral data for a minimal model."""
    mp.dps = dps

    if y_values is None:
        y_values = [0.5, 1.0, 2.0, 5.0]

    # Partition function values
    pf_vals = {}
    ce_vals = {}
    for y in y_values:
        y_mpf = mpf(y)
        pf_vals[y] = partition_function_at_imaginary(
            model, y_mpf, num_terms=num_terms, dps=dps
        )
        ce_vals[y] = constrained_epstein(
            model, y_mpf, num_terms=num_terms, dps=dps
        )

    # Dirichlet coefficients
    d_coeffs = dirichlet_coefficients(model, num_terms=num_terms, dps=dps)

    # Multiplicativity
    is_mult, failures = check_multiplicativity(d_coeffs, max_n=min(100, num_terms))

    # S-matrix
    S = compute_s_matrix(model, dps=dps)
    s_checks = verify_s_matrix(model, dps=dps)

    # L-function identification
    matches = identify_l_function(d_coeffs, max_n=min(50, num_terms), dps=dps)

    # Shadow prediction
    prediction = predict_shadow_depth_from_dirichlet(
        model, name, num_terms=num_terms, dps=dps
    )

    return MinimalModelSpectralData(
        name=name,
        model=model,
        partition_values=pf_vals,
        constrained_epstein_values=ce_vals,
        dirichlet_coefficients=d_coeffs,
        is_multiplicative=is_mult,
        multiplicativity_failures=failures,
        s_matrix_data=S,
        s_matrix_checks=s_checks,
        l_function_matches=matches,
        shadow_prediction=prediction,
    )


# ---------------------------------------------------------------------------
# Cross-model comparison
# ---------------------------------------------------------------------------

def compare_dirichlet_series(
    models: Dict[str, MinimalModel],
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> Dict[str, Dict]:
    """Compare Dirichlet series across multiple models.

    Returns a dict keyed by model name with summary statistics.
    """
    mp.dps = dps
    results = {}
    for name, model in models.items():
        coeffs = dirichlet_coefficients(model, num_terms=num_terms, dps=dps)
        is_mult, failures = check_multiplicativity(coeffs, max_n=min(50, num_terms))
        matches = identify_l_function(coeffs, max_n=min(30, num_terms), dps=dps)

        # Growth rate: log(a_n) / log(n) for large n
        growth_rates = []
        for n in [10, 20, 50]:
            if n < len(coeffs) and coeffs[n] > 0:
                growth_rates.append(
                    (n, float(log(coeffs[n]) / log(mpf(n))))
                )

        results[name] = {
            'central_charge': float(model.central_charge),
            'num_primaries': model.num_primaries(),
            'is_multiplicative': is_mult,
            'num_failures': len(failures),
            'first_10_coeffs': [float(coeffs[n]) for n in range(min(10, len(coeffs)))],
            'growth_rates': growth_rates,
            'l_matches': matches,
        }
    return results


# ---------------------------------------------------------------------------
# Theta-function expressions for Ising characters (cross-validation)
# ---------------------------------------------------------------------------

def _jacobi_theta3(q: mpc, num_terms: int = 200) -> mpc:
    """theta_3(0|tau) = 1 + 2 sum_{n>=1} q^{n^2/2}.

    Here q = e^{2 pi i tau} (the standard nome).
    The exponents are n^2/2, following the Jacobi convention
    theta_3(0|tau) = sum_{n in Z} e^{i pi n^2 tau}.
    """
    val = mpc(1, 0)
    for n in range(1, num_terms):
        qn2 = power(q, mpf(n * n) / 2)
        if abs(qn2) < mpf(10) ** (-mp.dps + 5):
            break
        val += 2 * qn2
    return val


def _jacobi_theta4(q: mpc, num_terms: int = 200) -> mpc:
    """theta_4(0|tau) = 1 + 2 sum_{n>=1} (-1)^n q^{n^2/2}.

    Here q = e^{2 pi i tau}.
    """
    val = mpc(1, 0)
    for n in range(1, num_terms):
        qn2 = power(q, mpf(n * n) / 2)
        if abs(qn2) < mpf(10) ** (-mp.dps + 5):
            break
        val += 2 * ((-1) ** n) * qn2
    return val


def _jacobi_theta2(q: mpc, num_terms: int = 200) -> mpc:
    """theta_2(0|tau) = 2 sum_{n>=0} q^{(n+1/2)^2/2}.

    Here q = e^{2 pi i tau}. The exponents are (n+1/2)^2/2.
    """
    val = mpc(0, 0)
    for n in range(num_terms):
        exp_val = mpf((2 * n + 1) ** 2) / 8  # (n+1/2)^2 / 2
        qe = power(q, exp_val)
        if abs(qe) < mpf(10) ** (-mp.dps + 5):
            break
        val += qe
    return 2 * val


def ising_characters_theta(
    tau: mpc,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> Tuple[mpc, mpc, mpc]:
    """Compute Ising characters using theta/eta expressions.

    The Ising model = free fermion has three sectors (NS+, NS-, R).
    The NS+/- partition functions are sqrt(theta_3/eta) and sqrt(theta_4/eta).
    The Virasoro characters are their symmetric/antisymmetric combinations:

        chi_0    = (sqrt(theta_3/eta) + sqrt(theta_4/eta)) / 2    [h = 0]
        chi_1/2  = (sqrt(theta_3/eta) - sqrt(theta_4/eta)) / 2    [h = 1/2]
        chi_1/16 = sqrt(theta_2 / (2 eta))                         [h = 1/16]

    Here theta_j = theta_j(0|tau) are the standard Jacobi theta functions
    and eta = eta(tau) is the Dedekind eta, all with nome q = e^{2 pi i tau}.

    In the vvmf_hecke.py M(4,3) convention:
    (1,1) -> h=0, (2,1) -> h=1/16, (1,2) -> h=1/2.
    Returns (chi_{(1,1)}, chi_{(2,1)}, chi_{(1,2)}) ordered by conformal weight.
    """
    mp.dps = dps
    q = exp(2 * pi * mpc(0, 1) * tau)
    eta_val = _eta_value(tau, num_terms=num_terms, dps=dps)

    th3 = _jacobi_theta3(q, num_terms=num_terms)
    th4 = _jacobi_theta4(q, num_terms=num_terms)
    th2 = _jacobi_theta2(q, num_terms=num_terms)

    sqrt_th3_eta = sqrt(th3 / eta_val)
    sqrt_th4_eta = sqrt(th4 / eta_val)

    chi_11 = (sqrt_th3_eta + sqrt_th4_eta) / 2       # h = 0
    chi_12 = (sqrt_th3_eta - sqrt_th4_eta) / 2       # h = 1/2
    chi_21 = sqrt(th2 / (2 * eta_val))                # h = 1/16

    return chi_11, chi_21, chi_12  # ordered by conformal weight


def verify_ising_theta_vs_rocha_caridi(
    tau: mpc,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> Dict[str, mpf]:
    """Cross-validate the two Ising character computations.

    Returns the absolute differences between theta/eta and Rocha-Caridi
    for each of the three characters.
    """
    mp.dps = dps
    model = ising_model()
    labels = model.primary_labels()  # (1,1), (2,1), (1,2) sorted by h

    # Rocha-Caridi
    rc_values = [
        character_value(model, lab.r, lab.s, tau, num_terms=num_terms, dps=dps)
        for lab in labels
    ]

    # Theta/eta
    theta_values = list(ising_characters_theta(tau, num_terms=num_terms, dps=dps))

    result = {}
    for i, lab in enumerate(labels):
        key = f'chi_({lab.r},{lab.s})'
        result[key] = abs(rc_values[i] - theta_values[i])

    return result
