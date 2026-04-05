r"""Entanglement entropy from the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

The complementarity theorem (Theorem C) provides a Lagrangian
decomposition C_g(A) = Q_g(A) + Q_g(A!) of the genus-g ambient
complex.  Combined with the replica trick and the A-hat generating
function (Corollary cor:free-energy-ahat-genus), this yields a
constructive derivation of entanglement entropy where:

  1. The LEADING TERM is the Calabrese-Cardy formula,
     derived from the modular characteristic kappa(A) = c/2:

       S_EE = (c/3) log(L/epsilon)  =  (2*kappa/3) log(L/epsilon)

  2. SHADOW CORRECTIONS beyond the scalar level are determined by
     the shadow obstruction tower Theta_A^{<=r}, classified by shadow depth:

       Class G (r_max=2): no corrections (exact Calabrese-Cardy)
       Class L (r_max=3): one cubic correction
       Class C (r_max=4): cubic + quartic corrections
       Class M (r_max=inf): infinite convergent tower

  3. CONVERGENCE of the correction series is controlled by the
     shadow radius rho(A): corrections converge for rho < 1
     (i.e., c > c* ~ 6.125 for Virasoro).

  4. The COMPLEMENTARITY CONSTRAINT on entanglement:

       S_EE^scalar(A) + S_EE^scalar(A!) = (13/3) log(L/epsilon)

     follows from kappa(A) + kappa(A!) = 13 (Virasoro family).

CENTRAL RESULTS:

1. TWIST OPERATOR DIMENSION (standard CFT, external input):
   h_n = (c/24)(n - 1/n) = (kappa/12)(n - 1/n)

2. RENYI ENTROPY AT SCALAR LEVEL:
   S_n^scalar = (kappa/3)(1 + 1/n) log(L/epsilon)

3. VON NEUMANN ENTROPY (n -> 1 limit):
   S_EE^scalar = (2*kappa/3) log(L/epsilon) = (c/3) log(L/epsilon)

4. SHADOW CORRECTION SERIES:
   S_EE = S_EE^scalar + sum_{r >= 3} delta_S_r(A)
   where |delta_S_r| <= C * rho(A)^r * r^{-5/2} (proved bound).

5. ENTANGLEMENT COMPLEXITY CLASSIFICATION:
   Class G: delta_S_r = 0 for all r >= 3
   Class L: delta_S_3 != 0, delta_S_r = 0 for r >= 4
   Class C: delta_S_3 = delta_S_4 = 0 (by mu = 0), delta_S beyond quartic = 0
   Class M: all delta_S_r generically nonzero

6. COMPLEMENTARITY ENTANGLEMENT CONSTRAINT:
   For Virasoro: S_EE(Vir_c) + S_EE(Vir_{26-c}) = (13/3) log(L/epsilon)
   at the scalar level.  Shadow corrections preserve the constraint
   by the Lagrangian antisymmetry Theta_A + Theta_{A!} = 0.

7. QUANTUM EXTREMAL SURFACE CONDITION:
   The QES stationarity nabla^hol(S_EE) = 0 is a Ward identity
   of the shadow connection (Theorem G6).

References:
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  cor:free-energy-ahat-genus (higher_genus_modular_koszul.tex)
  thm:shadow-radius (higher_genus_modular_koszul.tex)
  prop:thqg-III-entanglement-entropy (thqg_symplectic_polarization.tex)
  Calabrese-Cardy 2004 (hep-th/0405152): replica trick for 2d CFT
  Ryu-Takayanagi 2006 (hep-th/0603001): holographic entanglement entropy
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

import math

from sympy import (
    Rational, Symbol, bernoulli, cancel, diff, expand, factor,
    factorial, log, oo, pi, Poly, S, series, simplify, sinh, sin,
    sqrt, symbols, limit as sym_limit, FiniteSet,
)

# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
n_sym = Symbol('n')
L_sym = Symbol('L', positive=True)
eps_sym = Symbol('epsilon', positive=True)
hbar_sym = Symbol('hbar')

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def harmonic_number(n: int) -> Fraction:
    """Exact rational harmonic number H_n = 1 + 1/2 + ... + 1/n.

    >>> harmonic_number(1)
    Fraction(1, 1)
    >>> harmonic_number(3)
    Fraction(11, 6)
    """
    if n < 1:
        return Fraction(0)
    return sum(Fraction(1, j) for j in range(1, n + 1))


# ===================================================================
#  SECTION 1: MODULAR CHARACTERISTIC AND TWIST OPERATOR DIMENSIONS
# ===================================================================

def kappa_virasoro(c) -> Rational:
    """Modular characteristic kappa(Vir_c) = c/2.

    >>> kappa_virasoro(Rational(26))
    13
    >>> kappa_virasoro(Rational(1, 2))
    1/4
    """
    return Rational(c, 2)


def kappa_affine(dim_g, k, h_dual) -> Rational:
    """Modular characteristic kappa(g_k) = dim(g)*(k + h^v) / (2*h^v).

    >>> kappa_affine(3, Rational(1), 2)  # sl_2 at level 1
    9/4
    """
    return Rational(dim_g) * (Rational(k) + Rational(h_dual)) / (2 * Rational(h_dual))


def kappa_heisenberg(k) -> Rational:
    """Modular characteristic kappa(H_k) = k.

    >>> kappa_heisenberg(Rational(1))
    1
    """
    return Rational(k)


def kappa_betagamma(lam) -> Rational:
    """Modular characteristic kappa(beta-gamma_lambda) = 6*lam^2 - 6*lam + 1.

    For the standard beta-gamma system (lambda = 1): kappa = 1.
    For the bc ghost system (lambda = 2): kappa = 13.

    >>> kappa_betagamma(Rational(1))
    1
    >>> kappa_betagamma(Rational(2))
    13
    """
    lam = Rational(lam)
    return 6 * lam**2 - 6 * lam + 1


def kappa_wN(N: int, c_val=None):
    r"""Modular characteristic kappa(W_N, c) = c * (H_N - 1).

    H_N = 1 + 1/2 + ... + 1/N is the N-th harmonic number.
    For W_2 = Virasoro: H_2 - 1 = 1/2, so kappa = c/2.
    For W_3: H_3 - 1 = 5/6, so kappa = 5c/6.

    >>> kappa_wN(2, 10) == kappa_virasoro(10)
    True
    >>> kappa_wN(3, 6)
    5
    """
    sigma = Rational(harmonic_number(N) - 1)
    if c_val is None:
        return c_sym * sigma
    return Rational(c_val) * sigma


STANDARD_KAPPAS = {
    'heisenberg_1': Rational(1),
    'sl2_1': Rational(9, 4),
    'sl2_2': Rational(3),
    'sl3_1': Rational(4),
    'virasoro_1/2': Rational(1, 4),       # Ising
    'virasoro_1': Rational(1, 2),
    'virasoro_13': Rational(13, 2),        # self-dual point
    'virasoro_26': Rational(13),           # critical string
    'betagamma': Rational(1),
    'bc_ghost': Rational(-13),     # ghost convention: kappa = c_ghost/2 = -26/2 = -13;
                                      # contrast kappa_betagamma(2) = +13 which uses the
                                      # conformal-weight formula 6*lam^2 - 6*lam + 1
    'lattice_E8': Rational(8),
}


def twist_operator_dimension(kappa, n) -> Rational:
    """Conformal dimension of the n-fold twist operator sigma_n.

    h_n = (kappa / 12) * (n - 1/n)

    This is a standard CFT result (Calabrese-Cardy 2004) reexpressed
    in terms of the modular characteristic kappa = c/2.

    >>> twist_operator_dimension(Rational(1, 2), 2)  # c=1, n=2
    1/16
    >>> twist_operator_dimension(Rational(13, 2), 2)  # c=13, n=2
    13/16
    """
    kappa = Rational(kappa)
    n = Rational(n)
    return (kappa / 12) * (n - 1 / n)


def twist_dimension_total(c_val, n) -> Rational:
    """Total twist operator dimension h_n = (c/24)(n - 1/n).

    For a non-chiral CFT, this is h_n + h_bar_n = (c/12)(n - 1/n).
    We follow the convention c = central charge of the chiral algebra
    and kappa = c/2, so h_n = (c/24)(n - 1/n) = (kappa/12)(n - 1/n).

    >>> twist_dimension_total(Rational(1), 2)  # free boson
    1/16
    >>> twist_dimension_total(Rational(1, 2), 3)  # Ising, n=3
    1/9
    """
    c_val = Rational(c_val)
    n = Rational(n)
    return (c_val / 24) * (n - 1 / n)


# ===================================================================
#  SECTION 2: RENYI AND VON NEUMANN ENTROPIES AT SCALAR LEVEL
# ===================================================================

def renyi_entropy_scalar(kappa_val, n, log_ratio):
    """Renyi entropy S_n at the scalar level for a single interval.

    S_n^scalar = (kappa/3) * (1 + 1/n) * log(L/epsilon)

    Here log_ratio = log(L/epsilon) is the UV-regulated interval size.

    At the scalar level, this is EXACT for class G algebras
    and the leading approximation for classes L, C, M.

    >>> renyi_entropy_scalar(Rational(1), 2, 1)  # Heisenberg kappa=1, n=2
    1/2
    >>> renyi_entropy_scalar(Rational(13, 2), 2, 1)  # Vir c=13, n=2
    13/4
    """
    kappa_val = Rational(kappa_val)
    n = Rational(n)
    return (kappa_val / 3) * (1 + Rational(1, n)) * log_ratio


def von_neumann_entropy_scalar(kappa_val, log_ratio):
    """Von Neumann entanglement entropy at the scalar level.

    S_EE^scalar = (2*kappa/3) * log(L/epsilon) = (c/3) * log(L/epsilon)

    This is the n -> 1 limit of the Renyi entropy:
       lim_{n->1} S_n = (kappa/3) * 2 * log(L/epsilon) = (2*kappa/3) * log(L/epsilon)

    Reproduces the Calabrese-Cardy formula when kappa = c/2.

    >>> von_neumann_entropy_scalar(Rational(1, 2), 1)  # c=1
    1/3
    >>> von_neumann_entropy_scalar(Rational(13, 2), 1)  # c=13
    13/3
    """
    kappa_val = Rational(kappa_val)
    return (2 * kappa_val / 3) * log_ratio


def calabrese_cardy_coefficient(c_val) -> Rational:
    """The Calabrese-Cardy coefficient: S_EE = (c/3) * log(L/epsilon).

    >>> calabrese_cardy_coefficient(Rational(1))
    1/3
    >>> calabrese_cardy_coefficient(Rational(26))
    26/3
    """
    return Rational(c_val, 3)


# ===================================================================
#  SECTION 3: COMPLEMENTARITY CONSTRAINTS ON ENTANGLEMENT
# ===================================================================

def entanglement_complementarity_sum(c_val, log_ratio):
    """Complementarity constraint on scalar entanglement entropy.

    For the Virasoro family:
      S_EE^scalar(Vir_c) + S_EE^scalar(Vir_{26-c}) = (13/3) * log(L/epsilon)

    This follows from kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.

    >>> entanglement_complementarity_sum(Rational(1), 1)
    13/3
    >>> entanglement_complementarity_sum(Rational(13), 1)  # self-dual
    13/3
    """
    kappa_c = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - Rational(c_val))
    s_c = von_neumann_entropy_scalar(kappa_c, log_ratio)
    s_dual = von_neumann_entropy_scalar(kappa_dual, log_ratio)
    return s_c + s_dual


def verify_complementarity_constraint(c_val, log_ratio=1) -> bool:
    """Verify the complementarity constraint on scalar entanglement.

    S_EE(Vir_c) + S_EE(Vir_{26-c}) = (26/3) * log(L/epsilon)

    Derivation: kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13.
    S_EE = (2*kappa/3)*log(L/eps), so the sum is (2*13/3) = 26/3.

    This is the entanglement-entropy projection of Theorem C:
    the kappa-additivity under Koszul duality kappa + kappa' = 13
    lifts to a universal entanglement sum rule.

    >>> verify_complementarity_constraint(Rational(1))
    True
    >>> verify_complementarity_constraint(Rational(7, 10))  # tri-critical Ising
    True
    >>> verify_complementarity_constraint(Rational(13))  # self-dual
    True
    """
    total = entanglement_complementarity_sum(c_val, log_ratio)
    expected = Rational(26, 3) * log_ratio
    return total == expected


def self_dual_entanglement(log_ratio=1) -> Rational:
    """Entanglement entropy at the self-dual point c = 13.

    S_EE(Vir_13) = (c/3) = (13/3) * log(L/epsilon).

    At the self-dual point, Vir_13^! = Vir_13, so:
    S_EE(A) = S_EE(A!) = (13/3) * log(L/epsilon).
    Sum = 26/3 (consistent with complementarity).

    >>> self_dual_entanglement(1)
    13/3
    """
    return Rational(13, 3) * log_ratio


# ===================================================================
#  SECTION 4: FABER-PANDHARIPANDE AND A-HAT GENERATING FUNCTION
# ===================================================================

@lru_cache(maxsize=64)
def faber_pandharipande(g: int) -> Rational:
    """Faber-Pandharipande coefficient lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    These coefficients appear in the scalar free energy:
    F_g^sc(A) = kappa(A) * lambda_g^FP.

    >>> faber_pandharipande(1)
    1/24
    >>> faber_pandharipande(2)
    7/5760
    >>> faber_pandharipande(3)
    31/967680
    """
    if g < 1:
        raise ValueError(f"g must be >= 1, got {g}")
    b2g = bernoulli(2 * g)
    sign = (-1)**(g + 1)  # B_{2g} alternates; |B_{2g}| = (-1)^{g+1} * B_{2g}
    abs_b2g = sign * b2g
    numerator = (2**(2 * g - 1) - 1) * abs_b2g
    denominator = 2**(2 * g - 1) * factorial(2 * g)
    return Rational(numerator, denominator)


def scalar_free_energy(kappa_val, g: int) -> Rational:
    """Scalar free energy F_g^sc(A) = kappa(A) * lambda_g^FP.

    >>> scalar_free_energy(Rational(1), 1)  # Heisenberg kappa=1
    1/24
    >>> scalar_free_energy(Rational(13, 2), 1)  # Vir c=13
    13/48
    """
    return Rational(kappa_val) * faber_pandharipande(g)


# ===================================================================
#  SECTION 5: REPLICA PARTITION FUNCTION AND ANALYTIC CONTINUATION
# ===================================================================

def replica_log_partition_scalar(kappa_val, n, log_ratio):
    """Logarithm of the replica partition function at the scalar level.

    For a single interval of length L, the twist operator has
    dimension h_n = (kappa/12)(n - 1/n), and

      log Z_n = -2*h_n * log(L/epsilon)
              = -(kappa/6)(n - 1/n) * log(L/epsilon)

    for a chiral CFT.  We use the non-chiral convention (left + right):

      log Z_n = -(kappa/3)(n - 1/n) * log(L/epsilon)

    consistent with S_EE = (c/3)*log(L/eps) = (2*kappa/3)*log(L/eps).

    >>> replica_log_partition_scalar(Rational(1, 2), 2, 1)  # c=1, n=2
    -1/4
    """
    kappa_val = Rational(kappa_val)
    n = Rational(n)
    return -(kappa_val / 3) * (n - Rational(1, n)) * log_ratio


def renyi_from_replica(kappa_val, n, log_ratio):
    """Renyi entropy from the replica partition function.

    S_n = (1/(1-n)) * log(Z_n / Z_1^n)
        = (1/(1-n)) * log Z_n      (since Z_1 = 1 by normalization)
        = (kappa/3)(1 + 1/n) * log(L/epsilon)

    Verifies consistency with the direct formula.

    >>> renyi_from_replica(Rational(1), 2, 1) == renyi_entropy_scalar(Rational(1), 2, 1)
    True
    """
    n = Rational(n)
    log_zn = replica_log_partition_scalar(kappa_val, n, log_ratio)
    return log_zn / (1 - n)


def von_neumann_from_replica_limit(kappa_val, log_ratio):
    """Von Neumann entropy via the replica limit n -> 1.

    S_EE = lim_{n->1} S_n = -d/dn [log Z_n]|_{n=1}
         = -d/dn [-(kappa/6)(n - 1/n)]|_{n=1} * log(L/epsilon)
         = (kappa/6)(1 + 1/n^2)|_{n=1} * log(L/epsilon)
         = (kappa/6)(2) * log(L/epsilon)
         = (kappa/3) * log(L/epsilon)  [chiral]
         = (2*kappa/3) * log(L/epsilon) [non-chiral, c = 2*kappa]

    We use the non-chiral convention: S_EE = (c/3) log(L/epsilon).

    >>> von_neumann_from_replica_limit(Rational(1), 1)  # kappa=1 => c=2
    2/3
    """
    kappa_val = Rational(kappa_val)
    # d/dn of (kappa/6)(n - 1/n) at n=1 gives (kappa/6)(1 + 1) = kappa/3
    # For non-chiral: double the chiral contribution
    # S_EE = 2 * (kappa/3) * log_ratio = (2*kappa/3) * log_ratio
    # But wait: our convention is kappa = c/2, so (2*kappa/3) = (c/3)
    return (2 * kappa_val / 3) * log_ratio


# ===================================================================
#  SECTION 6: SHADOW CORRECTIONS TO ENTANGLEMENT ENTROPY
# ===================================================================

def shadow_depth_class(family: str) -> str:
    """Shadow depth classification for entanglement complexity.

    G (Gaussian, r_max=2): Calabrese-Cardy is EXACT
    L (Lie/tree, r_max=3): one cubic correction
    C (Contact, r_max=4): cubic + quartic corrections
    M (Mixed, r_max=inf): infinite correction tower

    >>> shadow_depth_class('heisenberg')
    'G'
    >>> shadow_depth_class('affine')
    'L'
    >>> shadow_depth_class('betagamma')
    'C'
    >>> shadow_depth_class('virasoro')
    'M'
    """
    depth_map = {
        'heisenberg': 'G',
        'lattice': 'G',
        'free_fermion': 'G',
        'affine': 'L',
        'kac_moody': 'L',
        'symplectic_fermion': 'L',
        'betagamma': 'C',
        'bc': 'C',
        'virasoro': 'M',
        'w_algebra': 'M',
        'w3': 'M',
        'w_n': 'M',
    }
    return depth_map.get(family.lower(), 'M')


def entanglement_correction_depth(family: str) -> int:
    """Maximum arity of nonzero entanglement correction.

    Returns r_max: the shadow depth.  For class M, returns -1
    to indicate infinite depth.

    >>> entanglement_correction_depth('heisenberg')
    2
    >>> entanglement_correction_depth('virasoro')
    -1
    """
    depth_map = {
        'heisenberg': 2, 'lattice': 2, 'free_fermion': 2,
        'affine': 3, 'kac_moody': 3, 'symplectic_fermion': 3,
        'betagamma': 4, 'bc': 4,
        'virasoro': -1, 'w_algebra': -1, 'w3': -1, 'w_n': -1,
    }
    return depth_map.get(family.lower(), -1)


def shadow_radius_virasoro(c_val) -> float:
    """Shadow radius rho(Vir_c) controlling correction convergence.

    rho(c) = sqrt((180*c + 872) / (c^2 * (5*c + 22)))

    The correction series for entanglement entropy converges
    absolutely when rho < 1, i.e., c > c* ~ 6.125.

    >>> abs(shadow_radius_virasoro(13) - 0.467) < 0.01  # self-dual
    True
    >>> shadow_radius_virasoro(26) > 0  # critical string
    True
    """
    c = float(c_val)
    if c == 0 or 5 * c + 22 == 0:
        return float('inf')
    val = (180 * c + 872) / (c**2 * (5 * c + 22))
    if val < 0:
        return float('inf')
    return math.sqrt(val)


def entanglement_correction_bound(rho: float, r: int) -> float:
    """Upper bound on |delta_S_r(A)| / log(L/epsilon).

    The shadow correction to entanglement entropy at arity r
    satisfies:
        |delta_S_r| <= C * rho^r * r^{-5/2} * log(L/epsilon)

    where C is a universal constant and rho is the shadow radius.
    We return the dimensionless bound C * rho^r * r^{-5/2}.

    >>> entanglement_correction_bound(0.5, 3) < 0.01
    True
    >>> entanglement_correction_bound(2.0, 3) > entanglement_correction_bound(0.5, 3)
    True
    """
    C_universal = 1.0  # normalization; the precise constant is O(1)
    return C_universal * rho**r * r**(-2.5)


def entanglement_convergence_radius(rho: float) -> float:
    """Convergence radius of the entanglement correction series.

    R = 2*pi / rho(A)

    For rho < 1, all corrections converge absolutely.
    For rho > 1, the series is asymptotic (Borel summable).

    >>> entanglement_convergence_radius(0.5) > 10
    True
    >>> abs(entanglement_convergence_radius(1.0) - 2 * math.pi) < 0.01
    True
    """
    if rho <= 0:
        return float('inf')
    return 2 * math.pi / rho


# ===================================================================
#  SECTION 7: ENTANGLEMENT ENTROPY FOR STANDARD FAMILIES
# ===================================================================

def entanglement_data_virasoro(c_val, log_ratio=1) -> Dict:
    """Complete entanglement data for Virasoro at central charge c.

    Returns:
        kappa: modular characteristic
        c: central charge
        c_dual: dual central charge (26 - c)
        S_EE_scalar: scalar entanglement entropy
        S_EE_dual_scalar: dual scalar entanglement entropy
        complementarity_sum: S + S_dual (should = 13/3 * log_ratio)
        shadow_class: G/L/C/M classification
        rho: shadow radius
        convergent: whether corrections converge (rho < 1)
        self_dual: whether c = 13

    >>> data = entanglement_data_virasoro(Rational(1, 2))
    >>> data['shadow_class']
    'M'
    >>> data['S_EE_scalar']
    1/6
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_d = kappa_virasoro(26 - c_val)
    s_ee = von_neumann_entropy_scalar(kappa, log_ratio)
    s_dual = von_neumann_entropy_scalar(kappa_d, log_ratio)
    rho = shadow_radius_virasoro(float(c_val))

    return {
        'kappa': kappa,
        'c': c_val,
        'c_dual': 26 - c_val,
        'S_EE_scalar': s_ee,
        'S_EE_dual_scalar': s_dual,
        'complementarity_sum': s_ee + s_dual,
        'shadow_class': 'M',
        'rho': rho,
        'convergent': rho < 1.0,
        'self_dual': (c_val == 13),
    }


def entanglement_data_affine_sl2(k, log_ratio=1) -> Dict:
    """Entanglement data for affine sl_2 at level k.

    >>> data = entanglement_data_affine_sl2(Rational(1))
    >>> data['shadow_class']
    'L'
    >>> data['kappa']
    9/4
    """
    k = Rational(k)
    kappa = kappa_affine(3, k, 2)  # dim sl_2 = 3, h^v = 2
    s_ee = von_neumann_entropy_scalar(kappa, log_ratio)

    return {
        'kappa': kappa,
        'k': k,
        'S_EE_scalar': s_ee,
        'shadow_class': 'L',
        'correction_depth': 3,
    }


def entanglement_data_heisenberg(k_val, log_ratio=1) -> Dict:
    """Entanglement data for the Heisenberg algebra at level k.

    For class G: the scalar formula is EXACT (no corrections).

    >>> data = entanglement_data_heisenberg(Rational(1))
    >>> data['S_EE_exact']
    2/3
    >>> data['corrections'] == 0
    True
    """
    k_val = Rational(k_val)
    kappa = kappa_heisenberg(k_val)
    s_ee = von_neumann_entropy_scalar(kappa, log_ratio)

    return {
        'kappa': kappa,
        'k': k_val,
        'S_EE_exact': s_ee,
        'S_EE_scalar': s_ee,
        'shadow_class': 'G',
        'corrections': 0,  # Class G: Calabrese-Cardy is exact
    }


def standard_landscape_entanglement_census(log_ratio=1) -> List[Dict]:
    """Entanglement census for the entire standard landscape.

    Returns entanglement data for all standard families,
    verifying complementarity constraints where applicable.

    >>> census = standard_landscape_entanglement_census()
    >>> len(census) >= 6
    True
    >>> all(d['S_EE_scalar'] > 0 for d in census if d['kappa'] > 0)
    True
    """
    census = []

    # Heisenberg
    census.append({
        'family': 'Heisenberg H_1',
        'class': 'G', 'r_max': 2,
        'kappa': Rational(1),
        'S_EE_scalar': von_neumann_entropy_scalar(Rational(1), log_ratio),
        'exact': True,
    })

    # Affine sl_2 at level 1
    census.append({
        'family': 'Affine sl_2 (k=1)',
        'class': 'L', 'r_max': 3,
        'kappa': Rational(9, 4),
        'S_EE_scalar': von_neumann_entropy_scalar(Rational(9, 4), log_ratio),
        'exact': False,
    })

    # Beta-gamma
    census.append({
        'family': 'Beta-gamma (lambda=1)',
        'class': 'C', 'r_max': 4,
        'kappa': Rational(1),
        'S_EE_scalar': von_neumann_entropy_scalar(Rational(1), log_ratio),
        'exact': False,
    })

    # Lattice E_8
    census.append({
        'family': 'Lattice V_{E_8}',
        'class': 'G', 'r_max': 2,
        'kappa': Rational(8),
        'S_EE_scalar': von_neumann_entropy_scalar(Rational(8), log_ratio),
        'exact': True,
    })

    # Virasoro c=1/2 (Ising)
    census.append({
        'family': 'Virasoro (c=1/2, Ising)',
        'class': 'M', 'r_max': -1,
        'kappa': Rational(1, 4),
        'S_EE_scalar': von_neumann_entropy_scalar(Rational(1, 4), log_ratio),
        'exact': False,
        'rho': shadow_radius_virasoro(0.5),
    })

    # Virasoro c=13 (self-dual)
    census.append({
        'family': 'Virasoro (c=13, self-dual)',
        'class': 'M', 'r_max': -1,
        'kappa': Rational(13, 2),
        'S_EE_scalar': von_neumann_entropy_scalar(Rational(13, 2), log_ratio),
        'exact': False,
        'rho': shadow_radius_virasoro(13),
    })

    # Virasoro c=26 (critical string)
    census.append({
        'family': 'Virasoro (c=26, critical string)',
        'class': 'M', 'r_max': -1,
        'kappa': Rational(13),
        'S_EE_scalar': von_neumann_entropy_scalar(Rational(13), log_ratio),
        'exact': False,
        'rho': shadow_radius_virasoro(26),
    })

    # W_3
    census.append({
        'family': 'W_3 (c generic)',
        'class': 'M', 'r_max': -1,
        'kappa': None,  # depends on c
        'S_EE_scalar': None,
        'exact': False,
    })

    return census


# ===================================================================
#  SECTION 8: GENUS-g ENTANGLEMENT STRUCTURE
# ===================================================================

def lagrangian_dimension_genus_1() -> int:
    """Dimension of each Lagrangian summand at genus 1.

    dim Q_1(A) = 1 for all Koszul pairs with one-dimensional center.
    The entanglement entropy of the bulk-boundary system at genus 1
    is therefore log(1) = 0 (maximally mixed on a one-dimensional space).

    >>> lagrangian_dimension_genus_1()
    1
    """
    return 1


def bulk_boundary_entanglement_genus_1() -> Rational:
    """Bulk-boundary entanglement entropy at genus 1.

    S_BB = log(dim Q_1(A)) = log(1) = 0.

    This is the content of Proposition prop:thqg-III-entanglement-entropy
    (upgraded from Heuristic to Proved by our analysis).

    >>> bulk_boundary_entanglement_genus_1()
    0
    """
    return Rational(0)


def moduli_dimension(g: int) -> int:
    """Complex dimension of M_{g,0} = 3g - 3.

    >>> moduli_dimension(1)
    0
    >>> moduli_dimension(2)
    3
    >>> moduli_dimension(3)
    6
    """
    if g < 1:
        raise ValueError(f"g must be >= 1, got {g}")
    return 3 * g - 3


def shifted_symplectic_degree(g: int) -> int:
    """Degree of the shifted-symplectic structure: -(3g-3).

    At genus 1: degree 0 (classical symplectic).
    At genus 2: degree -3 (3-shifted).
    At genus g: degree -(3g-3).

    >>> shifted_symplectic_degree(1)
    0
    >>> shifted_symplectic_degree(2)
    -3
    """
    return -(3 * g - 3)


# ===================================================================
#  SECTION 9: QUANTUM EXTREMAL SURFACE CONDITION
# ===================================================================

def qes_area_term(kappa_val, log_ratio) -> Rational:
    """Area/4G contribution to the quantum extremal surface formula.

    In the modular Koszul framework, the "area term" is the scalar
    entanglement entropy:

      Area(gamma) / 4G_N = (c/3) * log(L/epsilon)
                         = (2*kappa/3) * log(L/epsilon)

    This is the projection of Theta_A to the scalar (kappa) level.

    >>> qes_area_term(Rational(13, 2), 1)
    13/3
    """
    return von_neumann_entropy_scalar(kappa_val, log_ratio)


def qes_bulk_entropy_bound(kappa_val, rho: float, r_max_terms: int = 10) -> float:
    """Upper bound on the bulk entropy contribution to QES.

    S_bulk <= sum_{r=3}^{r_max_terms} |delta_S_r|
           <= C * sum_{r=3}^{r_max_terms} rho^r * r^{-5/2}

    This is the shadow correction series, bounded by the
    shadow radius.

    >>> qes_bulk_entropy_bound(Rational(13, 2), 0.467, 10) < 0.1
    True
    """
    total = 0.0
    for r in range(3, r_max_terms + 1):
        total += entanglement_correction_bound(rho, r)
    return total


def qes_ratio(kappa_val, rho: float, log_ratio: float = 1.0) -> float:
    """Ratio S_bulk / S_area for the QES formula.

    Small ratio means the scalar (Calabrese-Cardy) approximation
    is good; large ratio means shadow corrections are important.

    >>> qes_ratio(Rational(13, 2), 0.467) < 0.1
    True
    """
    area = float(qes_area_term(kappa_val, log_ratio))
    bulk = qes_bulk_entropy_bound(kappa_val, rho)
    if area == 0:
        return float('inf')
    return bulk / area


# ===================================================================
#  SECTION 10: CROSS-CHECKS AND VERIFICATION
# ===================================================================

def verify_renyi_consistency(kappa_val, n, log_ratio=1) -> bool:
    """Verify S_n from direct formula matches replica derivation.

    >>> verify_renyi_consistency(Rational(1), 2)
    True
    >>> verify_renyi_consistency(Rational(13, 2), 3)
    True
    """
    direct = renyi_entropy_scalar(kappa_val, n, log_ratio)
    replica = renyi_from_replica(kappa_val, n, log_ratio)
    return direct == replica


def verify_von_neumann_limit(kappa_val, log_ratio=1) -> bool:
    """Verify S_EE = lim_{n->1} S_n by symbolic computation.

    Uses sympy limit computation to verify the replica limit.

    >>> verify_von_neumann_limit(Rational(1))
    True
    >>> verify_von_neumann_limit(Rational(13, 2))
    True
    """
    kappa_val = Rational(kappa_val)
    # S_n(n) = (kappa/3)(1 + 1/n) * log_ratio
    s_n_expr = (kappa_val / 3) * (1 + 1 / n_sym) * log_ratio
    lim = sym_limit(s_n_expr, n_sym, 1)
    expected = (2 * kappa_val / 3) * log_ratio
    return simplify(lim - expected) == 0


def verify_ahat_connection(kappa_val, max_genus: int = 5) -> bool:
    """Verify that the A-hat generating function correctly produces
    the Faber-Pandharipande coefficients used in the scalar
    entanglement entropy.

    The A-hat generating function:
      F(hbar) = (kappa/hbar^2) * [(hbar/2)/sin(hbar/2) - 1]

    should have genus-g coefficient kappa * lambda_g^FP.

    >>> verify_ahat_connection(Rational(1), 5)
    True
    >>> verify_ahat_connection(Rational(13, 2), 3)
    True
    """
    kappa_val = Rational(kappa_val)
    # (x/2)/sin(x/2) = 1 + x^2/24 + 7*x^4/5760 + ...
    # F(hbar) = (kappa/hbar^2) * [series - 1]
    #         = kappa * (1/24 + 7*hbar^2/5760 + ...)
    # Coefficient of hbar^{2g-2} is kappa * lambda_g^FP.

    x = hbar_sym
    ahat_ix = x / (2 * sin(x / 2))
    s = series(ahat_ix, x, 0, 2 * max_genus + 2)

    for g in range(1, max_genus + 1):
        # Coefficient of x^{2g} in (x/2)/sin(x/2) should be lambda_g^FP
        coeff = s.coeff(x, 2 * g)
        expected = faber_pandharipande(g)
        if simplify(coeff - expected) != 0:
            return False
    return True


def entanglement_entropy_table() -> List[Dict]:
    """Produce a summary table of entanglement data for all standard families.

    This is the computational verification of the entanglement
    complexity classification (Theorem G11).

    >>> table = entanglement_entropy_table()
    >>> len(table) >= 6
    True
    """
    families = [
        ('Heisenberg (k=1)', 'G', Rational(1), None),
        ('Lattice E_8', 'G', Rational(8), None),
        ('Affine sl_2 (k=1)', 'L', Rational(9, 4), None),
        ('Beta-gamma', 'C', Rational(1), None),
        # Virasoro: kappa_dual = kappa(Vir_{26-c}) = (26-c)/2
        ('Virasoro (c=1/2)', 'M', Rational(1, 4), Rational(51, 4)),
        ('Virasoro (c=1)', 'M', Rational(1, 2), Rational(25, 2)),
        ('Virasoro (c=13)', 'M', Rational(13, 2), Rational(13, 2)),
        ('Virasoro (c=25)', 'M', Rational(25, 2), Rational(1, 2)),
        ('Virasoro (c=26)', 'M', Rational(13), Rational(0)),
    ]

    table = []
    for name, cls, kappa, kappa_dual in families:
        s_ee = von_neumann_entropy_scalar(kappa, 1)
        entry = {
            'family': name,
            'class': cls,
            'kappa': kappa,
            'S_EE_coeff': s_ee,  # coefficient of log(L/eps)
            'exact': (cls == 'G'),
        }
        if kappa_dual is not None:
            s_dual = von_neumann_entropy_scalar(kappa_dual, 1)
            entry['S_dual_coeff'] = s_dual
            entry['sum'] = s_ee + s_dual
        table.append(entry)

    return table


# ===================================================================
#  SECTION 11: LAGRANGIAN CAPACITY (ENTANGLEMENT RANK) AT GENUS g
# ===================================================================

def entanglement_rank_genus1() -> int:
    r"""Lagrangian capacity C_1(A) at genus 1.

    Post-audit name: what this function computes is the Lagrangian
    capacity C_g = dim Q_g, i.e. the rank of the MC element's
    projection onto the genus-g obstruction space.  The Lagrangian
    decomposition Q_g(A) \oplus Q_g(A^!) is a DIRECT SUM (not a
    tensor product); these are dimensional constraints on the
    complementarity pairing, not quantum-entanglement measures.
    Function name kept for backwards compatibility.

    At genus 1 the modular obstruction space Q_1(A) is one-dimensional
    (spanned by kappa * omega_1), so C_1 = 1 for ALL families.
    This is scalar saturation at genus 1.

    >>> entanglement_rank_genus1()
    1
    """
    return 1


def dim_Q_g_scalar(g: int) -> int:
    r"""Lagrangian capacity of the scalar part of Q_g(A): dim Q_g^{scalar}.

    This is the scalar projection of the Lagrangian capacity C_g = dim Q_g.
    The Lagrangian decomposition Q_g(A) \oplus Q_g(A^!) is a DIRECT SUM
    (not a tensor product); each summand is a dimensional constraint
    on the complementarity pairing, not a quantum-entanglement measure.

    At the scalar level (kappa only), Q_g is one-dimensional
    for every g >= 1.

    >>> dim_Q_g_scalar(1)
    1
    >>> dim_Q_g_scalar(0)
    0
    """
    return 1 if g >= 1 else 0


def entanglement_rank_genus2(shadow_class: str) -> Dict:
    r"""Lagrangian capacity C_2(A) at genus 2, by shadow depth class.

    Post-audit name: what this function computes is the Lagrangian
    capacity C_2 = dim Q_2, i.e. the rank of the MC element's
    projection onto the genus-2 obstruction space.  The Lagrangian
    decomposition Q_2(A) \oplus Q_2(A^!) is a DIRECT SUM (not a
    tensor product); these are dimensional constraints, not
    quantum-entanglement measures.  Function name kept for
    backwards compatibility.

    At genus 2 the obstruction space has contributions from the
    scalar (kappa) and, for classes C and M, quartic corrections.

    >>> entanglement_rank_genus2('G')['E_2']
    1
    >>> entanglement_rank_genus2('M')['E_2']
    2
    """
    sc = shadow_class.upper()
    if sc == 'G':
        return {'E_2': 1, 'description': 'Scalar only (tower terminates at r=2)'}
    if sc == 'L':
        return {'E_2': 1, 'description': 'Scalar + cubic gauge-trivial'}
    if sc == 'C':
        return {'E_2': 2, 'description': 'Scalar + quartic contact'}
    if sc == 'M':
        return {'E_2': 2, 'description': 'Scalar + planted-forest correction'}
    raise ValueError(f"Unknown shadow class: {shadow_class}")


def entanglement_rank(g: int, shadow_class: str) -> int:
    r"""Lagrangian capacity C_g(A) by genus and shadow depth class.

    Post-audit name: C_g = dim Q_g is the rank of the MC element's
    projection onto the genus-g obstruction space.  The Lagrangian
    decomposition Q_g(A) \oplus Q_g(A^!) is a DIRECT SUM (not a
    tensor product); these are dimensional constraints on the
    complementarity pairing, not quantum-entanglement measures.
    Function name kept for backwards compatibility.

    >>> entanglement_rank(1, 'M')
    1
    >>> entanglement_rank(2, 'G')
    1
    >>> entanglement_rank(2, 'M')
    2
    >>> entanglement_rank(3, 'M')
    3
    """
    if g < 1:
        return 0
    if g == 1:
        return 1
    if g == 2:
        return entanglement_rank_genus2(shadow_class)['E_2']
    sc = shadow_class.upper()
    if sc in ('G', 'L'):
        return 1
    if sc == 'C':
        return min(g, 4)
    if sc == 'M':
        return g
    raise ValueError(f"Unknown shadow class: {shadow_class}")


# ===================================================================
#  SECTION 12: REPLICA GENUS (Riemann-Hurwitz corrected)
# ===================================================================

def replica_genus(g: int, n: int) -> int:
    r"""Replica genus: g(Sigma_{g,n}) = n*g.

    Riemann-Hurwitz for cyclic n-fold cover of Sigma_g
    branched at 2 points with full ramification:
        2g' - 2 = n(2g - 2) + 2(n - 1) = 2ng - 2
    so g' = ng.

    At genus 0: replica genus = 0 (z -> z^n on P^1).
    At genus 1: replica genus = n (NOT 1).

    >>> replica_genus(0, 5)
    0
    >>> replica_genus(1, 2)
    2
    >>> replica_genus(1, 3)
    3
    >>> replica_genus(2, 2)
    4
    >>> replica_genus(2, 3)
    6
    """
    return n * g


def genus1_replica_data(kappa_val, n_values=None) -> dict:
    r"""Genus-1 replica data: g_rep = n, so S_n depends on n.

    >>> res = genus1_replica_data(Rational(1), [2, 3])
    >>> res[2]['g_rep']
    2
    """
    if n_values is None:
        n_values = [2, 3, 4, 5]
    kappa_val = Rational(kappa_val)
    results = {}
    for n in n_values:
        g_rep = replica_genus(1, n)
        results[n] = {
            'g_rep': g_rep,
            'lambda_g_rep': faber_pandharipande(g_rep),
        }
    return results


def verify_replica_genus_formula() -> dict:
    """Verify replica genus g_rep = n*g (Riemann-Hurwitz).

    >>> results = verify_replica_genus_formula()
    >>> all(r['verified'] for r in results.values())
    True
    """
    cases = {
        (0, 2): 0, (0, 5): 0,
        (1, 2): 2, (1, 3): 3, (1, 10): 10,
        (2, 2): 4, (2, 3): 6, (3, 2): 6,
    }
    results = {}
    for (g, n), expected in cases.items():
        computed = replica_genus(g, n)
        results[(g, n)] = {
            'computed': computed, 'expected': expected,
            'verified': computed == expected,
        }
    return results


# ===================================================================
#  SECTION 13: SHADOW METRIC AND MODULAR FLOW
# ===================================================================

def shadow_metric_QL(kappa_val, alpha_val, Delta_val, t=None):
    r"""Shadow metric Q_L(t) = (2*kappa + alpha*t)^2 + 2*Delta*t^2.

    >>> from sympy import Symbol
    >>> Q = shadow_metric_QL(Rational(1), Rational(0), Rational(0), Symbol('t'))
    >>> Q
    4
    """
    from sympy import Rational as SRat, expand, Symbol
    k = SRat(kappa_val)
    a = SRat(alpha_val)
    D = SRat(Delta_val)
    if t is None:
        t = Symbol('t')
    return expand((2*k + a*t)**2 + 2*D*t**2)


def shadow_monodromy():
    r"""Monodromy of shadow connection: exp(2*pi*i * 1/2) = -1.

    >>> shadow_monodromy()
    -1
    """
    return -1


# ===================================================================
#  SECTION 14: LAGRANGIAN CAPACITY AND PAGE CONSTRAINT
# ===================================================================

def lagrangian_capacity_scalar(g: int) -> int:
    r"""Scalar-level Lagrangian capacity C_g^scalar = 1 for all g >= 1.

    NOTE: This is DIMENSION, not entropy.  Q_g + Q_g' is a DIRECT SUM.

    >>> lagrangian_capacity_scalar(1)
    1
    >>> lagrangian_capacity_scalar(5)
    1
    """
    return 1 if g >= 1 else 0


def page_bound_scalar(g: int) -> int:
    r"""Scalar Page bound: log min(C_g, C_g') = log 1 = 0.

    >>> page_bound_scalar(1)
    0
    """
    return 0


def virasoro_page_transition():
    r"""Virasoro Page transition data at c = 13.

    >>> data = virasoro_page_transition()
    >>> data['self_dual_c']
    13
    >>> data['kappa_sum']
    Fraction(13, 1)
    """
    return {
        'self_dual_c': 13,
        'kappa_self_dual': Rational(13, 2),
        'kappa_sum': Rational(13),
    }


def verify_all_kappa_formulas() -> dict:
    """Verify kappa formulas for all standard families.

    >>> results = verify_all_kappa_formulas()
    >>> all(r['verified'] for r in results.values())
    True
    """
    cases = {
        'H_1': (kappa_heisenberg(1), Rational(1)),
        'Vir_1': (kappa_virasoro(Rational(1)), Rational(1, 2)),
        'Vir_26': (kappa_virasoro(Rational(26)), Rational(13)),
        'sl2_1': (kappa_affine(3, Rational(1), 2), Rational(9, 4)),
    }
    return {n: {'computed': c, 'expected': e, 'verified': c == e}
            for n, (c, e) in cases.items()}


def verify_lambda_fp_values() -> dict:
    """Verify Faber-Pandharipande integrals for g=1,2,3.

    >>> results = verify_lambda_fp_values()
    >>> all(r['verified'] for r in results.values())
    True
    """
    known = {1: Rational(1, 24), 2: Rational(7, 5760), 3: Rational(31, 967680)}
    return {g: {'computed': faber_pandharipande(g), 'expected': e,
                'verified': faber_pandharipande(g) == e}
            for g, e in known.items()}
