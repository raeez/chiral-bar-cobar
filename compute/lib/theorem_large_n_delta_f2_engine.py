r"""Large-N expansion of delta_F_2^{grav}(W_N) and 't Hooft limit.

MATHEMATICAL FRAMEWORK
======================

The gravitational cross-channel correction for W_N at genus 2 is:

    delta_F_2(W_N, c) = B(N) + A(N)/c

where:
    B(N) = (N-2)(N+3)/96
    A(N) = (N-2)(3N^3 + 14N^2 + 22N + 33)/24

These are PROVED by the independent graph sum in
rectification_delta_f2_verify_engine.py (7 genus-2 stable graphs,
5+ independent verification paths).

LARGE-N EXPANSION
=================

Full asymptotic expansion:

    B(N) = N^2/96 + N/96 - 1/16

    A(N) = N^4/8 + N^3/3 - N^2/4 - 11N/24 - 11/4
         = (3N^4 + 8N^3 - 6N^2 - 11N - 66)/24

Ratio:
    A(N)/B(N) = 12N^2 + 20N + 28 + O(1/N)

Physical interpretation: the 1/c term (A/c) dominates the constant
term (B) when c << 12N^2. Since c(W_N) ~ N^2 at large N for fixed k,
the ratio delta_F_2 / (kappa * lambda_2) measures cross-channel
importance relative to the scalar sector.

'T HOOFT LIMIT
==============

The Gaberdiel-Gopakumar 't Hooft parameter is:

    lambda = N / (k + N)

so k = N(1 - lambda)/lambda, k + N = N/lambda.

The central charge at large N with fixed lambda:

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
              ~ -N^2(N^2-1)(1-lambda)^2/lambda   (leading term)
              ~ -N^4(1-lambda)^2/lambda            (N -> infinity)

This is the NEGATIVE large-N regime (level k grows with N). For the
POSITIVE large-N regime (c > 0), one needs k > 0, which requires
lambda < 1 and appropriate N.

In the 't Hooft limit with the standard parametrization:

    delta_F_2 ~ B(N) + A(N)/c
             ~ N^2/96 + (N^4/8) / (-N^4(1-lambda)^2/lambda)
             ~ N^2/96 - lambda/(8(1-lambda)^2)

The constant term B(N) grows as N^2, while A(N)/c approaches a
lambda-dependent constant. The 't Hooft limit is SINGULAR for the
cross-channel correction: the constant term B(N) ~ N^2/96 diverges,
reflecting the proliferation of channels.

W_{1+INFINITY} LIMIT
=====================

As N -> infinity with c fixed (the W_{1+infinity} limit):

    delta_F_2(W_N, c) ~ N^2/96 + N^4/(8c) -> infinity

The cross-channel correction diverges. This is EXPECTED: the
W_{1+infinity} algebra has infinitely many generators, so the
multi-weight correction is infinite. The NORMALIZED quantity

    delta_F_2 / kappa = delta_F_2 / (c * (H_N - 1))

also diverges: B/kappa ~ N^2/(96c log N) -> infinity and
A/(c*kappa) ~ N^4/(8c^2 log N) -> infinity.

The W_{1+infinity} limit does NOT have a finite delta_F_2.
The scalar formula F_g = kappa * lambda_g becomes increasingly
inadequate as N grows, with the cross-channel correction
eventually dominating the scalar sector.

MATRIX MODEL PERSPECTIVE
========================

The graph sum computing delta_F_2 is the genus-2 free energy of
the A_{N-2} Frobenius manifold. The Frobenius manifold has:

  - Flat coordinates: t_j for j = 2, ..., N (one per W_N generator)
  - Metric: eta_{jj} = c/j (diagonal)
  - Prepotential: F_0 = (c/6) sum C_{ijk} t_i t_j t_k

The gravitational Frobenius algebra has structure constants
C_{ijk} determined by the W_N OPE (in the gravitational approx:
C_{TTT} = C_{T,W_j,W_j} = c).

The genus expansion F = sum_{g>=0} hbar^{2g} F_g is computed by
topological recursion on the associated spectral curve. The
spectral curve is the DISCRIMINANT of the Frobenius multiplication:

    det(C_i^j(t) - u * delta^j_i) = 0

For the gravitational Frobenius algebra, the T-multiplication has
eigenvalues c/j (j = 2, ..., N), giving N-1 branch points.

The matrix model interpretation: delta_F_2 is the genus-2
contribution to the free energy of an (N-1)-matrix model with
the W_N Frobenius algebra coupling structure.

ABJM N^{3/2} SCALING
=====================

For the ABJM boundary algebra at rank N:
    kappa(A_{ABJM}(N,k)) = -2N^2

This gives N^2 scaling (D-brane), not N^{3/2} (M2-brane). The
M2-brane scaling F ~ N^{3/2} comes from the FULL non-perturbative
partition function (Airy function), not from the perturbative genus
expansion. At genus g >= 1:

    F_g^{ABJM} = kappa * lambda_g = -2N^2 * lambda_g

This is O(N^2) at every genus. The N^{3/2} scaling of the TOTAL
free energy F = sum_g g_s^{2g-2} F_g requires non-perturbative
resummation (the Airy function). The cross-channel correction
delta_F_2 for ABJM would be zero (ABJM boundary VOA is a
single-generator system after BRST reduction at the effective level).

For a HYPOTHETICAL M2-brane boundary algebra with kappa ~ N^{3/2}:
    delta_F_2 ~ B(N) + A(N)/c
with c ~ N^{3/2} / rho (where rho is the anomaly ratio), giving
    delta_F_2 ~ N^2/96 + N^4 / (8 * N^{3/2} / rho) = N^2/96 + rho*N^{5/2}/8
The N^{5/2} scaling would DOMINATE, making the cross-channel
correction even more severe than in the W_N case.

References:
    thm:multi-weight-genus-expansion, thm:theorem-d, AP27
    rectification_delta_f2_verify_engine.py (independent verification)
    wn_central_charge_canonical.py (Fateev-Lukyanov formula)
    matrix_model_cross_channel.py (spectral curve obstruction)
    abjm_holographic_datum.py (ABJM boundary algebra)
    large_n_twisted_holography.py ('t Hooft genus expansion)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial, log
from typing import Dict, List, Optional, Tuple, Union

Num = Union[int, float, Fraction]


# ============================================================================
# 1. Exact closed-form coefficients B(N) and A(N)
# ============================================================================

def B_exact(N: int) -> Fraction:
    r"""Constant term B(N) = (N-2)(N+3)/96.

    This is the c-independent part of delta_F_2^{grav}(W_N).
    Arises entirely from the lollipop graph.

    B(N) = 0 for N = 2 (Virasoro, uniform weight).
    B(3) = 1/16 (W_3).
    B(4) = 7/48 (W_4).
    """
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    return Fraction((N - 2) * (N + 3), 96)


def A_exact(N: int) -> Fraction:
    r"""1/c coefficient A(N) = (N-2)(3N^3 + 14N^2 + 22N + 33)/24.

    This is the coefficient of 1/c in delta_F_2^{grav}(W_N).
    Arises from banana + theta + barbell graphs.

    A(N) = 0 for N = 2 (Virasoro, uniform weight).
    A(3) = 51/4 (W_3, giving (c+204)/(16c) = 1/16 + (51/4)/c).
      Check: 51/4 = (1)(3*27+14*9+22*3+33)/24 = (81+126+66+33)/24 = 306/24 = 51/4. OK.
    """
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    return Fraction((N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33), 24)


def delta_F2_grav_closed(N: int, c: Num) -> Fraction:
    r"""Closed form: delta_F_2^{grav}(W_N, c) = B(N) + A(N)/c.

    Parameters
    ----------
    N : rank of sl_N (N >= 2)
    c : central charge (nonzero)
    """
    c_f = Fraction(c) if not isinstance(c, Fraction) else c
    if c_f == 0:
        raise ValueError("Central charge c must be nonzero")
    return B_exact(N) + A_exact(N) / c_f


# ============================================================================
# 2. Large-N expansion of B(N) and A(N)
# ============================================================================

def B_expansion_coefficients() -> Dict[str, Fraction]:
    r"""Full asymptotic expansion of B(N) in powers of N.

    B(N) = (N^2 + N - 6)/96 = N^2/96 + N/96 - 1/16.

    This is EXACT (a polynomial), not asymptotic.
    """
    return {
        'N^2': Fraction(1, 96),
        'N^1': Fraction(1, 96),
        'N^0': Fraction(-1, 16),
    }


def A_expansion_coefficients() -> Dict[str, Fraction]:
    r"""Full asymptotic expansion of A(N) in powers of N.

    A(N) = (3N^4 + 8N^3 - 6N^2 - 11N - 66)/24

    Derivation:
      (N-2)(3N^3 + 14N^2 + 22N + 33)
      = 3N^4 + 14N^3 + 22N^2 + 33N - 6N^3 - 28N^2 - 44N - 66
      = 3N^4 + 8N^3 - 6N^2 - 11N - 66

    So A(N) = N^4/8 + N^3/3 - N^2/4 - 11N/24 - 11/4.

    This is EXACT (a polynomial), not asymptotic.
    """
    return {
        'N^4': Fraction(1, 8),
        'N^3': Fraction(1, 3),
        'N^2': Fraction(-1, 4),
        'N^1': Fraction(-11, 24),
        'N^0': Fraction(-11, 4),
    }


def verify_A_expansion(N: int) -> bool:
    """Verify the expanded form matches the factored form."""
    factored = A_exact(N)
    expanded = Fraction(3 * N**4 + 8 * N**3 - 6 * N**2 - 11 * N - 66, 24)
    return factored == expanded


def verify_B_expansion(N: int) -> bool:
    """Verify the expanded form matches the factored form."""
    factored = B_exact(N)
    expanded = Fraction(N**2 + N - 6, 96)
    return factored == expanded


def B_leading(N: int) -> float:
    """Leading term: B(N) ~ N^2/96."""
    return N**2 / 96


def A_leading(N: int) -> float:
    """Leading term: A(N) ~ N^4/8."""
    return N**4 / 8


# ============================================================================
# 3. Ratio A(N)/B(N) and its large-N expansion
# ============================================================================

def ratio_A_over_B(N: int) -> Fraction:
    r"""Exact ratio A(N)/B(N).

    A/B = [(N-2)(3N^3+14N^2+22N+33)/24] / [(N-2)(N+3)/96]
        = 4(3N^3+14N^2+22N+33) / (N+3)

    At large N: 12N^2 + ... (leading term).

    For N=2: 0/0, undefined (both vanish). Convention: 0.
    """
    if N <= 2:
        return Fraction(0)
    num = 4 * (3 * N**3 + 14 * N**2 + 22 * N + 33)
    den = N + 3
    return Fraction(num, den)


def ratio_large_N_expansion(N: int) -> Dict[str, Fraction]:
    r"""Polynomial long division of A(N)/B(N).

    A/B = 4(3N^3 + 14N^2 + 22N + 33)/(N + 3)

    Long division:
      3N^3 + 14N^2 + 22N + 33 = (N+3)(3N^2 + 5N + 7) + 12

    So A/B = 4(3N^2 + 5N + 7 + 12/(N+3))
           = 12N^2 + 20N + 28 + 48/(N+3).

    Further expanding 48/(N+3) at large N:
      48/(N+3) = 48/N * 1/(1+3/N) = (48/N)(1 - 3/N + 9/N^2 - ...)
              = 48/N - 144/N^2 + 432/N^3 - ...

    Full expansion:
      A/B = 12N^2 + 20N + 28 + 48/N - 144/N^2 + O(1/N^3)
    """
    if N <= 2:
        return {'N^2': Fraction(0)}
    # Exact polynomial part from long division
    q, r = divmod(3 * N**3 + 14 * N**2 + 22 * N + 33, N + 3)
    # q should be 3N^2 + 5N + 7, r should be 12
    return {
        'N^2': Fraction(12),
        'N^1': Fraction(20),
        'N^0': Fraction(28),
        'remainder': Fraction(48, N + 3),
        'exact': ratio_A_over_B(N),
    }


def verify_long_division(N: int) -> bool:
    """Verify the polynomial long division:
    3N^3+14N^2+22N+33 = (N+3)(3N^2+5N+7) + 12."""
    lhs = 3 * N**3 + 14 * N**2 + 22 * N + 33
    rhs = (N + 3) * (3 * N**2 + 5 * N + 7) + 12
    return lhs == rhs


# ============================================================================
# 4. 't Hooft limit
# ============================================================================

def c_wn_thooft(N: int, lam: Fraction) -> Fraction:
    r"""Central charge c(W_N, lambda) in the 't Hooft parametrization.

    lambda = N/(k+N), so k+N = N/lambda, k = N(1-lambda)/lambda.

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
              = (N-1) - N(N^2-1)(N/lambda - 1)^2 / (N/lambda)
              = (N-1) - (N^2-1)(N/lambda - 1)^2 * lambda

    This is exact for rational lambda.
    """
    if lam == 0:
        raise ValueError("lambda = 0 (k = infinity) not allowed")
    if lam == 1:
        # k = 0, critical-adjacent
        return Fraction(N - 1) - Fraction(N * (N**2 - 1) * (N - 1)**2, N)
    kpN = Fraction(N, 1) / lam  # k + N = N/lambda
    kpNm1 = kpN - 1  # k + N - 1
    c = Fraction(N - 1) - Fraction(N) * Fraction(N**2 - 1) * kpNm1**2 / kpN
    return c


def c_thooft_large_N(N: int, lam: Fraction) -> Dict[str, Fraction]:
    r"""Large-N expansion of c(W_N, lambda) at fixed lambda.

    c = (N-1) - (N^2-1) * lambda * (N/lambda - 1)^2
      = (N-1) - (N^2-1)(N^2/lambda - 2N + lambda)
      = (N-1) - (N^2-1)N^2/lambda + 2N(N^2-1) - lambda(N^2-1)

    Leading: -(N^2-1)N^2/lambda ~ -N^4/lambda.
    """
    c_exact = c_wn_thooft(N, lam)
    c_leading = Fraction(-1) * Fraction(N**4) / lam
    return {
        'exact': c_exact,
        'leading_N4': c_leading,
        'ratio': c_exact / c_leading if c_leading != 0 else None,
    }


def delta_F2_thooft(N: int, lam: Fraction) -> Dict[str, object]:
    r"""delta_F_2 in the 't Hooft limit.

    delta_F_2 = B(N) + A(N)/c(N, lambda)

    At large N:
      B(N) ~ N^2/96
      A(N) ~ N^4/8
      c ~ -N^4/lambda

    So A(N)/c ~ (N^4/8) / (-N^4/lambda) = -lambda/8.

    delta_F_2 ~ N^2/96 - lambda/8   (large N, fixed lambda)

    The constant term B(N) ~ N^2/96 DOMINATES (grows with N^2),
    while the 1/c term approaches a finite lambda-dependent constant.
    """
    c = c_wn_thooft(N, lam)
    if c == 0:
        return {
            'delta_F2': None,
            'B': B_exact(N),
            'A_over_c': None,
            'note': 'c = 0: critical level',
        }
    dF2 = delta_F2_grav_closed(N, c)
    return {
        'delta_F2': dF2,
        'B': B_exact(N),
        'A_over_c': A_exact(N) / c,
        'c': c,
        'lambda': lam,
        'B_leading': Fraction(N**2, 96),
        'A_over_c_leading': Fraction(-1) * lam / 8,
    }


def thooft_limit_A_over_c(lam: Fraction) -> Fraction:
    r"""The finite limit of A(N)/c(N, lambda) as N -> infinity.

    A(N)/c(N, lambda) -> (N^4/8) / (-N^4/lambda) = -lambda/8.

    This is the 't Hooft resummed cross-channel contribution
    from the 1/c sector. It is NEGATIVE (since c < 0 in the
    Gaberdiel-Gopakumar regime) and bounded.
    """
    return -lam / Fraction(8)


# ============================================================================
# 5. W_{1+infinity} limit (N -> infinity, c fixed)
# ============================================================================

def delta_F2_winfty_scaling(N: int, c: Num) -> Dict[str, object]:
    r"""Scaling of delta_F_2(W_N, c) as N -> infinity with c fixed.

    delta_F_2 = B(N) + A(N)/c ~ N^2/96 + N^4/(8c) -> infinity.

    The correction diverges: W_{1+infinity} does NOT have a finite
    cross-channel genus-2 correction. This is a manifestation of
    the infinite number of generators.

    kappa(W_N) = c(H_N - 1) ~ c*log(N) (harmonic number growth).
    delta_F_2 / kappa ~ N^2/(96*c*log(N)) + N^4/(8*c^2*log(N))
    Both diverge.
    """
    c_f = Fraction(c) if not isinstance(c, Fraction) else c
    B = B_exact(N)
    A = A_exact(N)
    dF2 = B + A / c_f
    H_N_minus_1 = sum(Fraction(1, j) for j in range(2, N + 1))
    kappa = c_f * H_N_minus_1
    lam2_fp = Fraction(7, 5760)
    scalar_part = kappa * lam2_fp

    return {
        'N': N,
        'c': c_f,
        'delta_F2': dF2,
        'B': B,
        'A_over_c': A / c_f,
        'kappa': kappa,
        'scalar_F2': scalar_part,
        'ratio_cross_over_scalar': dF2 / scalar_part if scalar_part != 0 else None,
        'B_over_scalar': B / scalar_part if scalar_part != 0 else None,
    }


# ============================================================================
# 6. Matrix model perspective: A_{N-2} Frobenius manifold
# ============================================================================

def frobenius_manifold_dimension(N: int) -> int:
    """Dimension of the W_N Frobenius manifold = N - 1.

    Generators: T, W_3, ..., W_N give N-1 flat coordinates.
    """
    return N - 1


def frobenius_eigenvalues(N: int, c: Num) -> List[Fraction]:
    r"""Eigenvalues of T-multiplication in the gravitational Frobenius algebra.

    The structure constant C_{T,W_j,W_j} = c for each j >= 2,
    and C_{T,T,W_j} = 0 for j >= 3. So T-multiplication on the
    basis {e_2, e_3, ..., e_N} (where e_j represents W_j) gives:

    C_T * e_j = sum_k eta^{kk} C_{T,j,k} e_k

    For the gravitational algebra:
    C_T * e_j = eta^{jj} C_{T,j,j} e_j = (j/c)*c * e_j = j * e_j

    So the eigenvalues are {2, 3, ..., N}.

    The spectral curve is det(C_T - u*I) = prod_{j=2}^N (j - u) = 0,
    with branch points at u = 2, 3, ..., N.
    """
    c_f = Fraction(c) if not isinstance(c, Fraction) else c
    return [Fraction(j) for j in range(2, N + 1)]


def spectral_curve_branch_points(N: int) -> List[int]:
    """Branch points of the A_{N-2} spectral curve: u = 2, 3, ..., N.

    The number of branch points is N-1, matching the Frobenius manifold
    dimension. For N=3 (W_3): 2 branch points at u=2,3 (A_1 curve).
    For N=4 (W_4): 3 branch points (A_2 curve).

    The matrix model obstruction (matrix_model_cross_channel.py) proved
    that no spectral curve with <= 2 branch points reproduces the full
    genus tower for W_3. The correct number is N-1 branch points.
    """
    return list(range(2, N + 1))


def effective_matrix_size(N: int) -> int:
    """Effective matrix size for the multi-matrix model: N - 1.

    The delta_F_2 correction arises from an (N-1)-matrix model
    with coupling structure given by the W_N gravitational Frobenius
    algebra. At genus 2, the free energy receives contributions from
    mixed-channel graph sums.
    """
    return N - 1


# ============================================================================
# 7. ABJM N^{3/2} scaling comparison
# ============================================================================

def kappa_abjm(N: int) -> Fraction:
    r"""kappa(A_{ABJM}(N, k)) = -2N^2.

    Independent of k. The two CS sectors cancel and the
    4N^2 symplectic boson pairs each contribute -1/2.

    This gives N^2 scaling, not N^{3/2}.
    """
    return Fraction(-2 * N**2)


def abjm_genus_g_free_energy(N: int, g: int) -> Fraction:
    r"""F_g^{ABJM} = kappa * lambda_g^FP = -2N^2 * lambda_g.

    The perturbative genus-g free energy scales as N^2 at every genus.
    The N^{3/2} total free energy requires non-perturbative resummation.
    """
    if g < 1:
        raise ValueError(f"Genus g >= 1 required, got {g}")
    # Bernoulli via recurrence
    B2g = _bernoulli_exact(2 * g)
    lam_g = Fraction(2**(2*g-1) - 1, 2**(2*g-1)) * abs(B2g) / Fraction(factorial(2*g))
    return kappa_abjm(N) * lam_g


def abjm_cross_channel_status() -> str:
    r"""ABJM cross-channel correction is ZERO.

    The ABJM boundary VOA (after BRST reduction) is effectively a
    single-generator system at the level relevant for the shadow
    obstruction tower. All generators have the same conformal weight
    after BRST cohomology.

    Therefore delta_F_g^cross(A_{ABJM}) = 0.
    """
    return "ZERO: ABJM boundary VOA is effectively uniform-weight after BRST"


def hypothetical_m2_scaling(N: int, c_coeff: Fraction,
                            rho: Fraction) -> Dict[str, object]:
    r"""Hypothetical M2-brane algebra with kappa ~ N^{3/2}.

    If an M2-brane boundary algebra had:
      c ~ c_coeff * N^{3/2}
      kappa ~ rho * c ~ rho * c_coeff * N^{3/2}

    Then:
      B(N) ~ N^2/96  (independent of c)
      A(N)/c ~ (N^4/8) / (c_coeff * N^{3/2}) = N^{5/2}/(8*c_coeff)

    The N^{5/2} scaling of the 1/c term would DOMINATE over the
    N^2 scaling of the constant term. Cross-channel effects would
    be even more severe than in the W_N case.
    """
    B = B_exact(N)
    A = A_exact(N)
    c_val = c_coeff * Fraction(N)**Fraction(3, 2) if isinstance(c_coeff, Fraction) else float(c_coeff) * N**1.5
    # Use float for non-integer powers
    c_float = float(c_coeff) * N**1.5
    A_over_c_float = float(A) / c_float if c_float != 0 else float('inf')
    B_float = float(B)

    return {
        'N': N,
        'c_approx': c_float,
        'B': B,
        'B_float': B_float,
        'A_over_c_float': A_over_c_float,
        'delta_F2_float': B_float + A_over_c_float,
        'B_scaling': 'N^2',
        'A_over_c_scaling': 'N^{5/2}',
        'dominant': 'A/c (N^{5/2} >> N^2)',
    }


# ============================================================================
# 8. Comprehensive numerical tables
# ============================================================================

def large_N_table(N_values: Optional[List[int]] = None,
                  c_value: Optional[Num] = None) -> List[Dict[str, object]]:
    r"""Table of delta_F_2 data across N values.

    If c_value is given, uses that fixed c. Otherwise uses c = N^2
    (a natural large-N scaling).
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 50]
    rows = []
    for N in N_values:
        B = B_exact(N)
        A = A_exact(N)
        if c_value is not None:
            c_f = Fraction(c_value) if not isinstance(c_value, Fraction) else c_value
        else:
            c_f = Fraction(N**2)
        dF2 = B + A / c_f
        H_Nm1 = sum(Fraction(1, j) for j in range(2, N + 1))
        kappa = c_f * H_Nm1
        lam2 = Fraction(7, 5760)
        scalar = kappa * lam2
        rows.append({
            'N': N,
            'c': c_f,
            'B(N)': B,
            'A(N)': A,
            'delta_F2': dF2,
            'kappa': kappa,
            'scalar_F2': scalar,
            'cross_over_scalar': float(dF2 / scalar) if scalar != 0 else float('inf'),
            'A/B': float(ratio_A_over_B(N)) if N > 2 else 0.0,
        })
    return rows


def thooft_table(N_values: Optional[List[int]] = None,
                 lambda_values: Optional[List[Fraction]] = None,
                 ) -> List[Dict[str, object]]:
    r"""Table of delta_F_2 in the 't Hooft parametrization."""
    if N_values is None:
        N_values = [3, 5, 10, 20, 50, 100]
    if lambda_values is None:
        lambda_values = [Fraction(1, 4), Fraction(1, 3), Fraction(1, 2),
                         Fraction(2, 3), Fraction(3, 4)]
    rows = []
    for N in N_values:
        for lam in lambda_values:
            try:
                data = delta_F2_thooft(N, lam)
                if data['delta_F2'] is not None:
                    rows.append({
                        'N': N,
                        'lambda': lam,
                        'c': data['c'],
                        'delta_F2': data['delta_F2'],
                        'B': data['B'],
                        'A_over_c': data['A_over_c'],
                        'thooft_limit_A_over_c': thooft_limit_A_over_c(lam),
                    })
            except (ValueError, ZeroDivisionError):
                pass
    return rows


# ============================================================================
# 9. Cross-verification with rectification engine
# ============================================================================

def cross_verify_with_graph_sum(N: int, c: Num) -> Dict[str, object]:
    r"""Cross-verify closed-form against independent graph sum.

    Imports from rectification_delta_f2_verify_engine.py, which
    is built from scratch with zero imports from this module.
    """
    from compute.lib.rectification_delta_f2_verify_engine import (
        delta_F2_grav_graph_sum,
        delta_F2_grav_symbolic,
    )
    c_f = Fraction(c) if not isinstance(c, Fraction) else c
    closed = delta_F2_grav_closed(N, c_f)
    graph_sum = delta_F2_grav_graph_sum(N, c_f)
    symbolic = delta_F2_grav_symbolic(N, c_f)
    return {
        'N': N,
        'c': c_f,
        'closed_form': closed,
        'graph_sum': graph_sum,
        'symbolic': symbolic,
        'all_agree': closed == graph_sum == symbolic,
    }


def cross_verify_BN_AN(N: int) -> Dict[str, object]:
    """Cross-verify B(N) and A(N) against graph-based extraction."""
    from compute.lib.rectification_delta_f2_verify_engine import (
        extract_A_N_from_graphs,
        extract_B_N_from_large_c,
    )
    B_here = B_exact(N)
    A_here = A_exact(N)
    B_graph = extract_B_N_from_large_c(N)
    A_graph = extract_A_N_from_graphs(N)
    return {
        'N': N,
        'B_exact': B_here,
        'B_graph': B_graph,
        'B_match': B_here == B_graph,
        'A_exact': A_here,
        'A_graph': A_graph,
        'A_match': A_here == A_graph,
    }


# ============================================================================
# 10. Normalized quantities for scaling analysis
# ============================================================================

def normalized_delta_F2(N: int, c: Num) -> Dict[str, object]:
    r"""Normalized cross-channel correction.

    Normalizations:
      1. delta_F_2 / lambda_2^FP = B(N)/lambda_2 + A(N)/(c*lambda_2)
      2. delta_F_2 / kappa = B(N)/kappa + A(N)/(c*kappa)
      3. delta_F_2 / F_2^scalar = (B + A/c) / (kappa * lambda_2)
      4. delta_F_2 * c = B*c + A  (polynomial in c)
    """
    c_f = Fraction(c) if not isinstance(c, Fraction) else c
    B = B_exact(N)
    A = A_exact(N)
    dF2 = B + A / c_f
    lam2 = Fraction(7, 5760)
    H = sum(Fraction(1, j) for j in range(2, N + 1))
    kappa = c_f * H
    scalar = kappa * lam2

    return {
        'delta_F2': dF2,
        'over_lambda2': dF2 / lam2,
        'over_kappa': dF2 / kappa if kappa != 0 else None,
        'over_scalar': dF2 / scalar if scalar != 0 else None,
        'times_c': B * c_f + A,
    }


# ============================================================================
# 11. Dominance crossover: where does A/c overtake B?
# ============================================================================

def dominance_crossover(N: int) -> Dict[str, object]:
    r"""Find the central charge c_* where |A(N)/c| = |B(N)|.

    A(N)/c_* = B(N) => c_* = A(N)/B(N) = ratio_A_over_B(N).

    For c < c_*: the 1/c term dominates (instanton regime).
    For c > c_*: the constant term dominates (perturbative regime).

    At large N: c_* ~ 12N^2.
    """
    if N <= 2:
        return {'N': N, 'note': 'N=2: both terms vanish'}
    r = ratio_A_over_B(N)
    return {
        'N': N,
        'c_star': r,
        'c_star_float': float(r),
        'c_star_leading': 12 * N**2,
        'B': B_exact(N),
        'A': A_exact(N),
        'interpretation': (
            f'For c < {float(r):.1f}: 1/c term dominates (instanton). '
            f'For c > {float(r):.1f}: constant term dominates (perturbative).'
        ),
    }


# ============================================================================
# 12. Internal helpers
# ============================================================================

@lru_cache(maxsize=64)
def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n via Akiyama-Tanigawa."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    a = [Fraction(0)] * (n + 1)
    for m in range(n + 1):
        a[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return a[0]


# ============================================================================
# Self-tests on import
# ============================================================================

# B(N) checks
assert B_exact(2) == Fraction(0), f"B(2) should be 0, got {B_exact(2)}"
assert B_exact(3) == Fraction(1, 16), f"B(3) should be 1/16, got {B_exact(3)}"
assert B_exact(4) == Fraction(7, 48), f"B(4) should be 7/48, got {B_exact(4)}"

# A(N) checks
assert A_exact(2) == Fraction(0), f"A(2) should be 0, got {A_exact(2)}"
# A(3) = (1)(3*27+14*9+22*3+33)/24 = (81+126+66+33)/24 = 306/24 = 51/4
assert A_exact(3) == Fraction(51, 4), f"A(3) should be 51/4, got {A_exact(3)}"

# W_3 consistency: delta_F_2(W_3, c) = (c+204)/(16c)
# B(3) + A(3)/c = 1/16 + 51/(4c) = (c + 204)/(16c). Check: 51/4 * 16 = 204. OK.
_test_c = Fraction(100)
_w3_ours = B_exact(3) + A_exact(3) / _test_c
_w3_known = (_test_c + 204) / (16 * _test_c)
assert _w3_ours == _w3_known, f"W_3 consistency failed: {_w3_ours} != {_w3_known}"

# Expansion verification
assert verify_A_expansion(3), "A expansion verification failed at N=3"
assert verify_A_expansion(10), "A expansion verification failed at N=10"
assert verify_B_expansion(5), "B expansion verification failed at N=5"

# Long division verification
assert verify_long_division(7), "Long division verification failed at N=7"
assert verify_long_division(100), "Long division verification failed at N=100"
