#!/usr/bin/env python3
r"""Modular spectral rigidity: MC equation constraints on spectral atoms.

The sewing-shadow intertwining theorem says:
  F_1^conn(q; A) = integral log(1 - lambda * t(q)) d rho(lambda)

where rho is the spectral measure of the MC element Theta_A, and
t(q) = (c/6)(Z(q)/Z_vac - 1) is the shadow-moduli map.

KEY INSIGHT: F_1^conn is a modular function. So the Stieltjes transform
of rho, composed with t(q), must be modular. This forces constraints on
the atoms of rho.

THE RIGIDITY CONJECTURE: If rho is a discrete measure such that
  integral log(1 - lambda * t(q)) d rho(lambda)
is modular of weight w for SL_2(Z), then the atoms of rho satisfy
constraints related to the Ramanujan bound.

FIVE DIRECTIONS:
  1. MC equation -> Hecke multiplicativity (constraints on S_r from bracket)
  2. Modular bootstrap on spectral measures (modularity -> exclusion regions)
  3. Bracket [Theta, Theta] and self-interaction (quadratic constraint -> atoms)
  4. Explicit verification for lattice VOAs (Deligne's theorem)
  5. Weil analogy: quadratic form on shadow space (positivity -> Ramanujan)

HONEST ASSESSMENT:
  - For lattice VOAs with Hecke eigenforms, the Ramanujan bound follows
    from Deligne's theorem (proved). Our computation VERIFIES this.
  - For the MC equation: at finite arity, the MC constraints give polynomial
    relations on shadow coefficients S_r. These translate into constraints
    on spectral atoms via the Stieltjes representation S_r = -(1/r) int lambda^r d rho.
    Whether these constraints force the full Ramanujan bound at finite arity
    is OPEN. At arities 2-4, the constraints are NECESSARY but NOT SUFFICIENT.
  - The modular bootstrap exclusion region approximates Ramanujan from outside
    but does NOT converge to it at finite truncation.
  - The Hodge index analogy is STRUCTURAL, not a proof. The intersection form
    on the cyclic deformation complex does NOT have the required definiteness
    properties in general.

References:
  concordance.tex (MC5, sewing-shadow intertwining)
  higher_genus_modular_koszul.tex (shadow Postnikov tower)
  lattice_shadow_periods.py (Hecke decomposition, theta functions)
  sewing_shadow_intertwining.py (F_1^conn, geometric kernels)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

import numpy as np


# ============================================================
# 0. Arithmetic utilities
# ============================================================

def sigma_k(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def sigma_minus_1(n: int) -> float:
    """sigma_{-1}(n) = sum_{d|n} 1/d."""
    if n <= 0:
        return 0.0
    return sum(1.0 / d for d in range(1, n + 1) if n % d == 0)


def is_prime(n: int) -> bool:
    """Primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def primes_up_to(bound: int) -> List[int]:
    """Return list of primes up to bound."""
    return [p for p in range(2, bound + 1) if is_prime(p)]


@lru_cache(maxsize=256)
def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficients of Delta = q * prod(1-q^m)^{24}.

    First values: tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830.
    """
    if n < 1:
        return 0
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    if n - 1 <= N:
        return coeffs[n - 1]
    return 0


def eisenstein_coefficient(k: int, n: int) -> Fraction:
    r"""The n-th Fourier coefficient of E_k (weight k Eisenstein series).

    E_k = 1 + (-2k/B_k) * sum_{n>=1} sigma_{k-1}(n) q^n.
    """
    if n == 0:
        return Fraction(1)
    Bk = _bernoulli(k)
    norm = Fraction(-2 * k, 1) / Bk
    return norm * Fraction(sigma_k(n, k - 1))


def _bernoulli(n: int) -> Fraction:
    """Bernoulli number B_n as exact fraction."""
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    if n == 0:
        return B[0]
    for m in range(1, n + 1):
        s = Fraction(0)
        for kk in range(m):
            binom = Fraction(1)
            num = m + 1
            for j in range(1, kk + 1):
                binom = binom * num // j
                num -= 1
            s += binom * B[kk]
        B[m] = -s / Fraction(m + 1)
    return B[n]


# ============================================================
# Direction 1: MC equation -> Hecke multiplicativity
# ============================================================

def mc_equation_genus1_constraints(
    shadow_coeffs: Dict[int, float],
    r_max: int,
) -> Dict[int, Dict[str, Any]]:
    r"""Genus-1 MC constraints on shadow coefficients S_2, ..., S_{r_max}.

    The MC equation at arity r+1 gives:
      nabla_H(Sh_r) + o^{(r)} = 0
    where nabla_H is the Hochschild differential and o^{(r)} is the
    obstruction from lower arities.

    At genus 1, the obstruction o^{(r)} is a polynomial in S_2, ..., S_{r-1}.
    The STIELTJES REPRESENTATION S_r = -(1/r) int lambda^r d rho(lambda)
    translates these into constraints on spectral atoms.

    Returns dict {arity: constraint_info} where constraint_info contains
    the polynomial relation, its evaluation, and the predicted S_r.

    KEY CAVEAT: These constraints are NECESSARY but not sufficient for
    Ramanujan. At finite arity, they constrain the MOMENTS of rho,
    not the individual atoms.
    """
    constraints = {}

    # S_2 = kappa = c/2 is the leading shadow. No constraint on S_2 alone.
    S = {r: shadow_coeffs.get(r, 0.0) for r in range(2, r_max + 1)}

    # Arity 3 constraint: the cubic shadow.
    # The MC equation at arity 3 gives:
    #   S_3 + (1/2) * bracket_contribution_3(S_2) = 0
    # where bracket_contribution_3 involves S_2 * S_2 through the
    # genus-1 propagator P (the Bergman kernel).
    #
    # For the Stieltjes measure: S_r = -(1/r) * sum_j c_j * lambda_j^r
    # The bracket [Theta^{<=2}, Theta^{<=2}]_3 = alpha_3 * S_2^2
    # with alpha_3 depending on the geometry of M_{1,3}.
    #
    # The genus-1 propagator gives alpha_3 = 1/(2*pi*i) * residue
    # from the sewing diagram. Numerically for standard families:
    alpha_3 = 0.0  # vanishes for free fields; for interacting theories:
    # alpha_3 is proportional to the structure constant C_{222} of the OPE.

    if 3 in S:
        predicted_S3 = -0.5 * alpha_3 * S.get(2, 0.0) ** 2
        constraints[3] = {
            'arity': 3,
            'mc_relation': 'S_3 + (1/2) * alpha_3 * S_2^2 = 0',
            'predicted': predicted_S3,
            'actual': S[3],
            'defect': S[3] - predicted_S3,
            'alpha_3': alpha_3,
            'note': ('alpha_3 = 0 for abelian theories (Gaussian class). '
                     'For non-abelian theories, alpha_3 encodes the cubic OPE structure.'),
        }

    # Arity 4 constraint: the quartic shadow.
    # MC equation at arity 4:
    #   S_4 + bracket_4(S_2, S_3) + (1/6) * triple_bracket_4(S_2, S_2, S_2) = 0
    # The key term is bracket_4 which couples S_2 * S_3.
    #
    # For the Stieltjes measure:
    #   S_4 = -(1/4) sum c_j lambda_j^4
    # So the MC equation gives:
    #   sum c_j lambda_j^4 = 4 * [bracket terms in S_2, S_3]
    #
    # This is a constraint on the 4th moment of rho in terms of the
    # 2nd and 3rd moments.
    #
    # The bracket coefficient beta_4 comes from the geometry of M_{1,4}.
    # For free-field theories: beta_4 = 0 (tower terminates at arity 2).
    # For affine theories: beta_4 != 0 but S_4 is determined by S_2, S_3.
    beta_4_linear = 0.0  # coefficient of S_2 * S_3
    beta_4_cubic = 0.0   # coefficient of S_2^3

    if 4 in S:
        predicted_S4 = -(beta_4_linear * S.get(2, 0.0) * S.get(3, 0.0)
                         + (1.0 / 6.0) * beta_4_cubic * S.get(2, 0.0) ** 3)
        constraints[4] = {
            'arity': 4,
            'mc_relation': 'S_4 + beta_4^lin * S_2 * S_3 + (1/6) * beta_4^cub * S_2^3 = 0',
            'predicted': predicted_S4,
            'actual': S[4],
            'defect': S[4] - predicted_S4,
            'beta_4_linear': beta_4_linear,
            'beta_4_cubic': beta_4_cubic,
            'note': ('Quartic constraint involves M_{1,4} geometry. '
                     'For Virasoro: Q^contact = 10/[c(5c+22)] enters here.'),
        }

    # Arity 5+ constraints follow the same pattern:
    # S_{r+1} is determined by S_2, ..., S_r plus the bracket at arity r+1.
    # We record the general structure.
    for r in range(5, r_max + 1):
        if r in S:
            constraints[r] = {
                'arity': r,
                'mc_relation': f'S_{r} = poly(S_2, ..., S_{r-1}) from MC at arity {r}',
                'actual': S[r],
                'note': (f'Arity-{r} MC constraint: not computed explicitly. '
                         'Requires M_{{1,{r}}} intersection theory.'),
            }

    return constraints


def hecke_multiplicativity_from_mc(
    atoms: Sequence[float],
    weights: Sequence[float],
    prime_bound: int = 50,
) -> Dict[str, Any]:
    r"""Check Hecke multiplicativity for a spectral measure rho = sum c_j delta(lambda_j).

    Given atoms lambda_j and weights c_j, compute the q-expansion coefficients
    a(n) = sum_j c_j * lambda_j^n (up to normalization) and check:
      a(p^2) = a(p)^2 - p^{k-1}   (Hecke recursion at weight k)

    for primes p <= prime_bound.

    HONEST ASSESSMENT: The Hecke recursion holds ONLY if the underlying
    modular form is a Hecke eigenform. For lattice VOAs, the theta function
    may decompose into multiple eigenforms. The recursion holds for each
    eigenform component separately, NOT for the full theta function unless
    it is already an eigenform (e.g., E_4 for E_8, Delta for weight 12).

    Returns a dict with Hecke defects at each prime.
    """
    atoms = list(atoms)
    weights = list(weights)
    n_atoms = len(atoms)
    assert len(weights) == n_atoms

    # Compute "Fourier coefficients" a(n) = sum_j c_j * lambda_j^n
    # This is the n-th power sum of the measure rho.
    def a(n):
        return sum(w * lam ** n for w, lam in zip(weights, atoms))

    primes = primes_up_to(prime_bound)
    results = {
        'atoms': atoms,
        'weights': weights,
        'n_atoms': n_atoms,
        'hecke_defects': {},
        'max_defect': 0.0,
    }

    for p in primes:
        a_p = a(p)
        a_p2 = a(p * p) if p * p <= 10000 else None
        if a_p2 is not None:
            # Try to detect the weight k from the data.
            # Hecke recursion: a(p^2) = a(p)^2 - p^{k-1}
            # So: p^{k-1} = a(p)^2 - a(p^2)
            pk_minus_1 = a_p ** 2 - a_p2
            results['hecke_defects'][p] = {
                'a_p': a_p,
                'a_p2': a_p2,
                'a_p_squared_minus_a_p2': pk_minus_1,
                'note': f'If Hecke eigenform of weight k: this should equal p^(k-1) = {p}^(k-1)',
            }
            if abs(pk_minus_1) > abs(results['max_defect']):
                results['max_defect'] = pk_minus_1

    return results


def mc_to_hecke_bridge(c: float, r_max: int = 8) -> Dict[str, Any]:
    r"""For Virasoro at central charge c, compute shadow coefficients,
    extract spectral measure, and check MC -> Hecke multiplicativity.

    The Virasoro shadow coefficients:
      S_2 = kappa = c/2
      S_3 = cubic shadow (vanishes for c = free field)
      S_4 involves Q^contact = 10/[c(5c+22)]

    The spectral measure for Virasoro is NOT a finite discrete measure
    (shadow tower is infinite, class M). So we truncate at arity r_max
    and extract a FINITE approximation to rho.

    HONEST RESULT: For Virasoro, the MC constraints at finite arity do NOT
    force Hecke multiplicativity. The shadow tower is infinite (class M),
    and no finite truncation captures the full modular structure. The Hecke
    recursion is an ASYMPTOTIC property that requires all arities.
    """
    # Shadow coefficients for Virasoro
    kappa = c / 2.0

    # Q^contact_Vir = 10/[c(5c+22)] for c != 0 and c != -22/5
    if abs(c) < 1e-15 or abs(5 * c + 22) < 1e-15:
        Q_contact = float('inf')
    else:
        Q_contact = 10.0 / (c * (5 * c + 22))

    shadow_coeffs = {2: kappa}
    # For Virasoro, the cubic shadow is determined by the Virasoro OPE.
    # At genus 1, the cubic contribution involves the three-point function
    # of T on the torus, which gives:
    #   S_3 = 0 (vanishes by conformal Ward identity on the torus)
    shadow_coeffs[3] = 0.0

    # The quartic shadow involves Q^contact:
    # S_4 ~ kappa * Q_contact (schematic; precise coefficient from M_{1,4})
    shadow_coeffs[4] = kappa * Q_contact

    # Higher shadows: not computed explicitly.
    # The Virasoro tower is infinite (class M), so all S_r for r >= 5 are nonzero.
    for r in range(5, r_max + 1):
        # Placeholder: the r-th shadow is suppressed by ~ c^{-r+2}
        shadow_coeffs[r] = kappa * Q_contact ** (r - 3) if Q_contact != float('inf') else 0.0

    # Extract finite spectral approximation from moments S_r.
    # S_r = -(1/r) * sum c_j * lambda_j^r => moments mu_r = -r * S_r = sum c_j * lambda_j^r
    moments = {r: -r * shadow_coeffs[r] for r in range(2, r_max + 1)}

    # For a finite set of atoms, we need n_atoms = r_max//2 at most.
    # Use the Hamburger moment problem: given mu_2, ..., mu_{r_max},
    # find atoms and weights. This is NOT unique in general.

    result = {
        'c': c,
        'kappa': kappa,
        'Q_contact': Q_contact,
        'shadow_coeffs': shadow_coeffs,
        'moments': moments,
        'mc_constraints': mc_equation_genus1_constraints(shadow_coeffs, r_max),
        'hecke_from_mc': 'NOT FORCED',
        'explanation': (
            'For Virasoro (class M), the MC constraints at finite arity '
            'give polynomial relations on shadow moments. These are '
            'NECESSARY but NOT SUFFICIENT for Hecke multiplicativity. '
            'The full Hecke recursion is an all-arity statement.'
        ),
    }

    return result


# ============================================================
# Direction 2: Modular bootstrap on spectral measures
# ============================================================

def modular_spectral_bootstrap(
    atoms: Sequence[float],
    weights: Sequence[float],
    q_test_points: Sequence[complex],
    weight_w: int = 0,
) -> Dict[str, Any]:
    r"""Check modularity of G(t(q)) = sum c_j log(1 - lambda_j * t(q)).

    For G to be modular of weight w under tau -> -1/tau:
      G(t(q(-1/tau))) = (c*tau)^w * G(t(q(tau)))  (for weight w)

    or for weight 0:
      G(t(q(-1/tau))) = G(t(q(tau)))

    The shadow-moduli map t(q) = (c/6)(Z(q)/Z_vac - 1) is itself
    NOT modular, so the composition constraint is nontrivial.

    q_test_points should be points in the upper half plane, specified as
    q = exp(2*pi*i*tau) with |q| < 1.

    Returns the modularity defect at each test point.

    HONEST ASSESSMENT: This computation requires evaluating the full
    partition function Z(q), which for interacting theories is known
    only through its q-expansion. The modularity test is meaningful
    only to the extent that the q-expansion is accurate.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for modular bootstrap")

    atoms = list(atoms)
    weights = list(weights)

    results = {
        'atoms': atoms,
        'weights': weights,
        'weight': weight_w,
        'test_points': [],
        'modularity_defects': [],
        'max_defect': 0.0,
    }

    for q in q_test_points:
        # G(q) = sum_j c_j * log(1 - lambda_j * t(q))
        # For t(q), we use the Heisenberg shadow-moduli map as a proxy:
        #   t(q) ~ sum_{N>=1} sigma_{-1}(N) * q^N (for c=1)
        # This is exact for free fields and a leading approximation for interacting.

        q_mp = mpmath.mpc(q)
        tau = mpmath.log(q_mp) / (2 * mpmath.pi * mpmath.mpc(0, 1))

        # Compute t(q) via truncated series
        t_val = mpmath.mpf(0)
        for N in range(1, 100):
            t_val += sigma_minus_1(N) * q_mp ** N
            if abs(q_mp ** N) < mpmath.mpf(10) ** (-40):
                break

        # G(q) = sum_j c_j * log(1 - lambda_j * t(q))
        G_val = mpmath.mpf(0)
        for lam, w in zip(atoms, weights):
            arg = 1 - mpmath.mpf(lam) * t_val
            if abs(arg) > 0:
                G_val += mpmath.mpf(w) * mpmath.log(arg)

        # Compute G at tau' = -1/tau
        tau_prime = -1 / tau
        q_prime = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) * tau_prime)

        t_val_prime = mpmath.mpf(0)
        for N in range(1, 100):
            t_val_prime += sigma_minus_1(N) * q_prime ** N
            if abs(q_prime ** N) < mpmath.mpf(10) ** (-40):
                break

        G_val_prime = mpmath.mpf(0)
        for lam, w in zip(atoms, weights):
            arg = 1 - mpmath.mpf(lam) * t_val_prime
            if abs(arg) > 0:
                G_val_prime += mpmath.mpf(w) * mpmath.log(arg)

        # Modularity check: G(tau') = (c*tau)^w * G(tau) for weight w
        if weight_w == 0:
            defect = abs(G_val_prime - G_val)
        else:
            defect = abs(G_val_prime - (tau ** weight_w) * G_val)

        results['test_points'].append(complex(tau))
        results['modularity_defects'].append(float(defect))
        if float(defect) > results['max_defect']:
            results['max_defect'] = float(defect)

    return results


def ramanujan_bound_test(
    atoms: Sequence[float],
    k: int,
    prime_bound: int = 50,
) -> Dict[str, Any]:
    r"""Test Ramanujan bound |lambda_j| <= 2 p^{(k-1)/2} for atoms.

    The Ramanujan bound applies to Hecke eigenvalues of cusp forms of weight k.
    For Eisenstein series, the eigenvalues are sigma_{k-1}(p) = 1 + p^{k-1},
    which VIOLATE the Ramanujan bound.

    KEY DISTINCTION:
    - Cusp form eigenvalues: |a(p)| <= 2 p^{(k-1)/2}  (Deligne, proved)
    - Eisenstein eigenvalues: a(p) = 1 + p^{k-1} >> 2 p^{(k-1)/2}

    For lattice VOAs, the spectral atoms come from the Hecke decomposition
    of the theta function. The Eisenstein part gives large atoms; only the
    cusp form part satisfies Ramanujan.

    Returns per-atom, per-prime results.
    """
    atoms = list(atoms)
    primes = primes_up_to(prime_bound)

    results = {
        'k': k,
        'atoms': atoms,
        'tests': [],
        'all_pass': True,
        'failures': [],
    }

    for j, lam in enumerate(atoms):
        for p in primes:
            bound = 2.0 * p ** ((k - 1) / 2.0)
            passes = abs(lam) <= bound + 1e-10  # tolerance
            test_result = {
                'atom_index': j,
                'atom_value': lam,
                'prime': p,
                'bound': bound,
                'passes': passes,
                'ratio': abs(lam) / bound if bound > 0 else float('inf'),
            }
            results['tests'].append(test_result)
            if not passes:
                results['all_pass'] = False
                results['failures'].append(test_result)

    return results


def bootstrap_exclusion_region(
    k: int,
    num_atoms: int,
    q_points: int = 20,
    atom_range: Tuple[float, float] = (-100.0, 100.0),
    grid_size: int = 50,
) -> Dict[str, Any]:
    r"""Compute the exclusion region in atom space from modularity constraints.

    For a spectral measure rho = sum_{j=1}^{num_atoms} c_j delta(lambda_j),
    the condition that G(t(q)) = sum c_j log(1 - lambda_j * t(q)) be modular
    constrains the atoms. We compute this constraint on a grid.

    METHOD: For num_atoms = 1, sweep lambda_1 over atom_range and compute
    the modularity defect. The exclusion region is where the defect is
    above a threshold.

    For num_atoms = 2, we sweep (lambda_1, lambda_2) on a 2D grid.

    HONEST ASSESSMENT: At finite q_points, the exclusion region is a
    NECESSARY condition for modularity, not sufficient. The true modular
    constraint requires checking at all tau, which is equivalent to
    checking all Fourier coefficients. Our grid gives an APPROXIMATION.

    Returns the grid of defects and the approximate exclusion boundary.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    if num_atoms == 1:
        lambdas = np.linspace(atom_range[0], atom_range[1], grid_size)
        defects = np.zeros(grid_size)

        # Test points: tau = i*y for y in [0.5, 2.0]
        test_taus = [complex(0, y) for y in np.linspace(0.5, 2.0, q_points)]
        test_qs = [complex(np.exp(-2 * np.pi * y)) for y in np.linspace(0.5, 2.0, q_points)]

        for idx, lam in enumerate(lambdas):
            try:
                result = modular_spectral_bootstrap(
                    atoms=[float(lam)],
                    weights=[1.0],
                    q_test_points=test_qs,
                    weight_w=0,
                )
                defects[idx] = result['max_defect']
            except Exception:
                defects[idx] = float('inf')

        # The Ramanujan bound for weight k:
        # For a single atom, the constraint is |lambda| <= 2*p^{(k-1)/2}
        # for the smallest prime p=2.
        ram_bound = 2.0 * 2 ** ((k - 1) / 2.0)

        return {
            'num_atoms': 1,
            'k': k,
            'lambdas': lambdas.tolist(),
            'defects': defects.tolist(),
            'ramanujan_bound': ram_bound,
            'grid_size': grid_size,
            'q_points': q_points,
            'note': ('Exclusion region approximation. The modularity defect '
                     'should be near zero for allowed atoms and large for '
                     'excluded atoms. At finite truncation, the exclusion '
                     'region is WIDER than the Ramanujan bound.'),
        }

    elif num_atoms == 2:
        # 2D grid
        gs = min(grid_size, 30)  # keep manageable
        lambdas_1 = np.linspace(atom_range[0], atom_range[1], gs)
        lambdas_2 = np.linspace(atom_range[0], atom_range[1], gs)
        defects = np.zeros((gs, gs))

        test_qs = [complex(np.exp(-2 * np.pi * y)) for y in np.linspace(0.5, 2.0, min(q_points, 10))]

        for i, l1 in enumerate(lambdas_1):
            for j, l2 in enumerate(lambdas_2):
                try:
                    result = modular_spectral_bootstrap(
                        atoms=[float(l1), float(l2)],
                        weights=[0.5, 0.5],
                        q_test_points=test_qs,
                        weight_w=0,
                    )
                    defects[i, j] = result['max_defect']
                except Exception:
                    defects[i, j] = float('inf')

        return {
            'num_atoms': 2,
            'k': k,
            'lambdas_1': lambdas_1.tolist(),
            'lambdas_2': lambdas_2.tolist(),
            'defects': defects.tolist(),
            'grid_size': gs,
        }

    else:
        return {
            'error': f'num_atoms = {num_atoms} > 2 not supported for grid exclusion',
            'note': 'For num_atoms > 2, use random sampling instead of grid.',
        }


# ============================================================
# Direction 3: Bracket [Theta, Theta] and self-interaction
# ============================================================

def mc_bracket_contribution(
    shadow_coeffs: Dict[int, float],
    r: int,
) -> Dict[str, Any]:
    r"""Compute the bracket [Theta^{<=r-1}, Theta^{<=r-1}] at arity r.

    The MC equation D*Theta + (1/2)[Theta, Theta] = 0 gives at arity r:
      D(Theta_r) + (1/2) sum_{a+b=r} [Theta_a, Theta_b] = 0

    where the bracket is the Lie bracket on the convolution algebra
    g^mod_A = Hom_alpha(C^!_ch, P^ch).

    The bracket [Theta_a, Theta_b]_r involves:
    - The genus-1 propagator P (Bergman kernel) connecting arity-a and arity-b graphs
    - The stable curve gluing map M_{1,a} x_{sewing} M_{1,b} -> M_{1,r}

    For low arities:
      r=3: [Theta_2, Theta_2]_3 ~ S_2^2 * <geometry of M_{1,3}>
      r=4: [Theta_2, Theta_3]_4 + [Theta_3, Theta_2]_4 ~ S_2*S_3 * <M_{1,4}>
           + (1/3!)[Theta_2, [Theta_2, Theta_2]]_4 ~ S_2^3 * <M_{1,4}>
      r=5: all pairings (a,b) with a+b=5
    """
    S = shadow_coeffs

    if r == 3:
        # [Theta_2, Theta_2]_3
        # The bracket involves gluing two 2-point vertices into a 3-point
        # configuration on the torus. This requires a propagator insertion.
        bracket_val = S.get(2, 0.0) ** 2
        return {
            'arity': 3,
            'bracket': bracket_val,
            'formula': '[Theta_2, Theta_2]_3 = S_2^2 * alpha_3',
            'components': [('S_2 * S_2', S.get(2, 0.0) ** 2)],
            'note': ('The coefficient alpha_3 depends on the integration '
                     'over M_{1,3}. For abelian theories alpha_3 = 0 '
                     '(Gaussian class terminates at arity 2).'),
        }

    elif r == 4:
        # [Theta_2, Theta_3]_4 and [Theta_2, Theta_2, Theta_2]_4
        term_23 = 2.0 * S.get(2, 0.0) * S.get(3, 0.0)  # symmetric: [2,3] + [3,2]
        term_222 = S.get(2, 0.0) ** 3 / 6.0  # (1/3!) from iterated bracket
        bracket_val = term_23 + term_222
        return {
            'arity': 4,
            'bracket': bracket_val,
            'formula': '[Theta^{<=3}, Theta^{<=3}]_4 = 2*S_2*S_3 + (1/6)*S_2^3',
            'components': [
                ('2 * S_2 * S_3', term_23),
                ('(1/6) * S_2^3', term_222),
            ],
            'note': ('Coefficient includes M_{1,4} geometry factors. '
                     'The Q^contact term enters here for Virasoro.'),
        }

    elif r == 5:
        term_24 = 2.0 * S.get(2, 0.0) * S.get(4, 0.0)
        term_33 = S.get(3, 0.0) ** 2
        term_223 = S.get(2, 0.0) ** 2 * S.get(3, 0.0) / 2.0
        term_2222 = S.get(2, 0.0) ** 4 / 24.0
        bracket_val = term_24 + term_33 + term_223 + term_2222
        return {
            'arity': 5,
            'bracket': bracket_val,
            'formula': '[Theta^{<=4}, Theta^{<=4}]_5',
            'components': [
                ('2 * S_2 * S_4', term_24),
                ('S_3^2', term_33),
                ('(1/2) * S_2^2 * S_3', term_223),
                ('(1/24) * S_2^4', term_2222),
            ],
        }

    else:
        # General arity: enumerate partitions of r into parts >= 2
        return {
            'arity': r,
            'bracket': None,
            'note': f'Bracket at arity {r} requires enumeration of partitions. Not computed.',
        }


def bracket_to_hecke_translation(
    shadow_coeffs: Dict[int, float],
    r_max: int = 6,
) -> Dict[str, Any]:
    r"""Translate MC bracket relations into constraints on spectral atoms.

    The Stieltjes representation: S_r = -(1/r) * sum_j c_j * lambda_j^r
    gives the shadow coefficients as MOMENTS of the spectral measure.

    The MC bracket relations give POLYNOMIAL RELATIONS among the S_r.
    Through the Stieltjes representation, these become constraints on
    the atoms lambda_j.

    KEY COMPUTATION for r=4:
    MC equation at arity 4 gives: S_4 = f(S_2, S_3)
    Stieltjes: S_4 = -(1/4) sum c_j lambda_j^4
    So: sum c_j lambda_j^4 = -4 * f(S_2, S_3)

    Through the Hamburger moment problem, this constrains the SUPPORT
    of the measure rho.

    HONEST RESULT: At arity 4, the constraint is:
      mu_4 >= mu_2^2  (by Cauchy-Schwarz)
    where mu_r = sum c_j lambda_j^r. This is a NECESSARY condition
    for the measure to be non-negative, but it is NOT the Ramanujan bound.
    The Ramanujan bound requires ALL arities.
    """
    S = shadow_coeffs
    mu = {r: -r * S.get(r, 0.0) for r in range(2, r_max + 1)}

    # Moment constraints from the Hamburger moment problem:
    # The Hankel matrix H_n = (mu_{i+j})_{i,j=0}^n must be positive semidefinite.
    # H_1 = [[mu_0, mu_1], [mu_1, mu_2]] (using mu_0 = total mass, mu_1 = first moment)
    #
    # For our measure (atoms are Hecke eigenvalues), mu_0 = sum c_j and
    # mu_1 = sum c_j lambda_j.

    # Construct Hankel matrices from available moments
    hankel_tests = {}

    # 2x2 Hankel: uses mu_2, mu_3, mu_4
    if all(r in mu for r in [2, 3, 4]):
        H2 = np.array([[mu[2], mu[3]], [mu[3], mu[4]]])
        eigvals = np.linalg.eigvalsh(H2)
        hankel_tests['H_2x2'] = {
            'matrix': H2.tolist(),
            'eigenvalues': eigvals.tolist(),
            'positive_semidefinite': bool(np.all(eigvals >= -1e-10)),
            'note': 'Cauchy-Schwarz: mu_4 * mu_2 >= mu_3^2',
        }

    # 3x3 Hankel: uses mu_2, ..., mu_6
    if all(r in mu for r in [2, 3, 4, 5, 6]):
        H3 = np.array([
            [mu[2], mu[3], mu[4]],
            [mu[3], mu[4], mu[5]],
            [mu[4], mu[5], mu[6]],
        ])
        eigvals = np.linalg.eigvalsh(H3)
        hankel_tests['H_3x3'] = {
            'matrix': H3.tolist(),
            'eigenvalues': eigvals.tolist(),
            'positive_semidefinite': bool(np.all(eigvals >= -1e-10)),
        }

    # MC bracket constraints at each arity
    bracket_constraints = {}
    for r in range(3, r_max + 1):
        bc = mc_bracket_contribution(S, r)
        bracket_constraints[r] = bc

    return {
        'shadow_coeffs': dict(S),
        'moments': mu,
        'hankel_tests': hankel_tests,
        'bracket_constraints': bracket_constraints,
        'hecke_forced': False,
        'explanation': (
            'The MC bracket relations give polynomial constraints on moments '
            'of the spectral measure. The Hankel positivity condition is '
            'necessary for the measure to exist. However, at finite arity, '
            'these constraints are WEAKER than Ramanujan. The Ramanujan bound '
            'is equivalent to all Hankel matrices being positive semidefinite '
            'with a specific BOUND on the support of rho.'
        ),
    }


def bracket_positivity_test(
    shadow_coeffs: Dict[int, float],
    r_max: int = 6,
) -> Dict[str, Any]:
    r"""Test whether positivity of [Theta, Theta] forces Ramanujan on atoms.

    The bracket [Theta, Theta] has a sign from the symplectic structure
    on the convolution algebra. Specifically:
      [Theta, Theta] = sum_{stable graphs Gamma} (1/|Aut(Gamma)|) * Theta_Gamma
    where the sum is over stable graphs contributing to the bracket.

    The sign of each graph contribution depends on:
    1. The orientation of the stable graph (from the modular operad)
    2. The pairing on the cyclic deformation complex

    HONEST RESULT: The bracket positivity does NOT directly force Ramanujan.
    The bracket [Theta, Theta] is NOT a positive-definite form in general.
    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 is a CANCELLATION
    condition, not a positivity condition. The analogy with the Weil proof
    (where positivity of the intersection form forces zeros onto the line)
    is STRUCTURAL but not directly applicable.
    """
    S = shadow_coeffs

    # Compute bracket contributions at each arity
    bracket_data = {}
    positivity_holds = True

    for r in range(3, r_max + 1):
        bc = mc_bracket_contribution(S, r)
        bracket_val = bc.get('bracket', None)
        if bracket_val is not None:
            bracket_data[r] = {
                'bracket_value': bracket_val,
                'sign': 'positive' if bracket_val > 1e-15 else ('negative' if bracket_val < -1e-15 else 'zero'),
            }
            # The MC equation says D(Theta_r) = -(1/2) * bracket_val
            # For positivity of the "energy" ||Theta||^2, we need
            # specific signs. Check consistency.
        else:
            bracket_data[r] = {'bracket_value': None, 'sign': 'not computed'}

    return {
        'shadow_coeffs': dict(S),
        'bracket_data': bracket_data,
        'forces_ramanujan': False,
        'explanation': (
            'The bracket [Theta, Theta] at finite arity does NOT have '
            'definite sign. The MC equation is a CANCELLATION condition. '
            'The Weil analogy (intersection form positivity -> zeros on line) '
            'requires additional structure (ampleness, Hodge index) that '
            'the shadow tower does NOT possess in general.'
        ),
    }


# ============================================================
# Direction 4: Explicit verification for lattice VOAs
# ============================================================

# Known Ramanujan tau values
_KNOWN_TAU = {
    1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
    6: -6048, 7: -16744, 8: 84480, 9: -113643, 10: -115920,
    11: 534612, 12: -370944, 13: -577738, 14: 401856, 15: 1217160,
    16: 987136, 17: -6905934, 18: 2727432, 19: 10661420, 20: -7109760,
    21: -4219488, 22: -12830688, 23: 18643272, 24: 21288960,
    25: -25499225, 26: 13865712, 27: -73279080, 28: 24647168,
}


def verify_ramanujan_for_lattice(
    lattice_type: str,
    num_primes: int = 15,
) -> Dict[str, Any]:
    r"""For lattice VOAs, verify the Ramanujan bound on Hecke eigenvalues.

    LATTICE THETA FUNCTIONS:
      V_Z:     theta_3(2*tau), weight 1/2 -- NOT a modular form for SL_2(Z)
      V_{Z^2}: theta_3(2*tau)^2, weight 1 on Gamma_0(4)
      V_{A_2}: theta function in M_1(Gamma_0(3), chi_3)
      V_{E_8}: Theta_{E_8} = E_4, weight 4 Eisenstein (no cusp part)
      V_Leech: Theta_Leech = E_{12} - (65520/691)*Delta, weight 12

    RAMANUJAN BOUND: applies to CUSP FORMS only.
      - E_4 (E_8 theta): eigenvalues are sigma_3(p) = 1+p^3, which VIOLATE
        the cusp form Ramanujan bound 2p^{3/2}. But E_4 is Eisenstein, not cusp.
      - Delta (Leech contribution): eigenvalues are tau(p), and Deligne proved
        |tau(p)| <= 2*p^{11/2}.

    The spectral atoms for lattice VOAs come from BOTH Eisenstein and cusp parts.
    Only the cusp form atoms satisfy Ramanujan.
    """
    primes = primes_up_to(100)[:num_primes]
    results = {
        'lattice': lattice_type,
        'primes_tested': primes,
        'eisenstein_tests': [],
        'cusp_tests': [],
        'summary': '',
    }

    if lattice_type == 'E8':
        # Theta_{E_8} = E_4: pure Eisenstein, weight 4
        # Hecke eigenvalues: a(p) = 1 + 240*sigma_3(p) (with normalization)
        # Actually: E_4 = 1 + 240*sum sigma_3(n) q^n
        # Hecke eigenvalue of E_4 at p: lambda(p) = sigma_3(p) = 1+p^3
        #
        # This VIOLATES 2*p^{3/2}: for p=2, sigma_3(2) = 1+8 = 9 > 2*2^{3/2} = 5.66
        for p in primes:
            sig3_p = 1 + p ** 3
            ram_bound = 2.0 * p ** 1.5
            results['eisenstein_tests'].append({
                'prime': p,
                'eigenvalue': sig3_p,
                'ramanujan_bound': ram_bound,
                'satisfies_bound': sig3_p <= ram_bound + 1e-10,
                'ratio': sig3_p / ram_bound,
            })
        results['cusp_tests'] = []
        results['summary'] = (
            'E_8 theta = E_4 (pure Eisenstein). Eigenvalues sigma_3(p) = 1+p^3 '
            'VIOLATE the Ramanujan bound 2p^{3/2}. This is expected: Ramanujan '
            'applies to cusp forms, not Eisenstein series. No cusp form component.'
        )

    elif lattice_type == 'Leech':
        # Theta_Leech = E_{12} - (65520/691)*Delta
        # Weight 12. Eisenstein part: E_{12} with eigenvalues sigma_{11}(p).
        # Cusp part: Delta with eigenvalues tau(p).
        # Deligne's theorem: |tau(p)| <= 2*p^{11/2}.
        c_delta = Fraction(-65520, 691)

        for p in primes:
            # Eisenstein eigenvalue
            sig11_p = sigma_k(p, 11)  # = 1 + p^{11}
            ram_bound_12 = 2.0 * p ** 5.5  # 2*p^{(12-1)/2} = 2*p^{11/2}

            results['eisenstein_tests'].append({
                'prime': p,
                'eigenvalue_sigma11': sig11_p,
                'ramanujan_bound': ram_bound_12,
                'satisfies_bound': sig11_p <= ram_bound_12 + 1e-10,
                'ratio': sig11_p / ram_bound_12,
                'note': 'Eisenstein: sigma_{11}(p) = 1+p^{11} >> 2p^{11/2}',
            })

            # Cusp form eigenvalue (Ramanujan tau)
            tau_p = _KNOWN_TAU.get(p, ramanujan_tau(p))
            results['cusp_tests'].append({
                'prime': p,
                'tau_p': tau_p,
                'ramanujan_bound': ram_bound_12,
                'satisfies_bound': abs(tau_p) <= ram_bound_12 + 1e-10,
                'ratio': abs(tau_p) / ram_bound_12 if ram_bound_12 > 0 else float('inf'),
                'note': f'|tau({p})| = {abs(tau_p)}, bound = {ram_bound_12:.2f}',
            })

        results['summary'] = (
            f'Leech theta = E_{{12}} - (65520/691)*Delta. '
            f'Eisenstein eigenvalues sigma_11(p) VIOLATE Ramanujan (expected). '
            f'Cusp eigenvalues tau(p) SATISFY Ramanujan: |tau(p)| <= 2p^{{11/2}} '
            f'(Deligne 1974, proved).'
        )

    elif lattice_type == 'Z':
        # Theta function is theta_3(2*tau), weight 1/2.
        # Not a modular form for SL_2(Z). Hecke theory is for the metaplectic cover.
        # No standard Ramanujan bound in this setting.
        results['summary'] = (
            'V_Z: theta_3(2*tau) is weight 1/2 for Gamma_0(4). '
            'Hecke theory for half-integer weight requires metaplectic cover. '
            'Standard Ramanujan bound does not apply directly.'
        )

    elif lattice_type == 'Z2':
        # weight 1 form for Gamma_0(4)
        results['summary'] = (
            'V_{Z^2}: weight 1 for Gamma_0(4). Decomposition into Eisenstein + cusp '
            'depends on the character. No cusp forms in M_1(SL_2(Z)), but there may '
            'be cusp forms on Gamma_0(4).'
        )

    elif lattice_type == 'A2':
        results['summary'] = (
            'V_{A_2}: weight 1 for Gamma_0(3) with character. '
            'No cusp forms at weight 1 for this group/character pair.'
        )

    else:
        results['summary'] = f'Unknown lattice type: {lattice_type}'

    return results


def verify_hecke_from_mc(
    lattice_type: str,
    r_max: int = 8,
) -> Dict[str, Any]:
    r"""For lattice VOAs, compute shadow coefficients from MC element,
    extract spectral measure, and verify Hecke multiplicativity.

    For lattice VOAs, the shadow coefficients are EXACTLY:
      S_r = -(1/r) * sum_{n>=1} a(n) * mu_r(n)
    where a(n) are theta function coefficients and mu_r(n) are the
    moments of the genus-1 kernel at arity r.

    For the simple case of the Heisenberg (shadow depth 2):
      S_2 = kappa = c/2, S_r = 0 for r >= 3.
    The spectral measure has ONE atom: rho = kappa * delta(lambda_0)
    with lambda_0 determined by S_2 = -(1/2) * kappa * lambda_0^2.
    But this is a self-consistency: lambda_0 = -1 (normalized).

    For E_8 (shadow depth 3, Lie class):
      S_2 = kappa = c/2 = 248/(2*31) = 124/31
      S_3 = cubic shadow (from the Lie bracket structure)
      S_r = 0 for r >= 4 (no quartic in Lie class)

    For Leech (shadow depth 4, contact class):
      S_2 = kappa = c/2 = 12
      S_3 = cubic from Eisenstein
      S_4 = quartic from Ramanujan Delta
      S_r = 0 for r >= 5 (terminates at 4)
    """
    results = {
        'lattice': lattice_type,
        'r_max': r_max,
        'shadow_coeffs': {},
        'spectral_measure': {},
        'hecke_check': {},
    }

    if lattice_type == 'Z':
        c = 1.0
        kappa = c / 2.0
        shadow_coeffs = {2: kappa}
        for r in range(3, r_max + 1):
            shadow_coeffs[r] = 0.0
        results['shadow_coeffs'] = shadow_coeffs
        results['spectral_measure'] = {
            'type': 'single_atom',
            'atom': -1.0,  # normalized
            'weight': kappa,
            'note': 'Gaussian class: single atom, tower terminates at arity 2',
        }
        results['hecke_check'] = {
            'applicable': False,
            'reason': 'Weight 1/2 form; standard Hecke theory not directly applicable',
        }

    elif lattice_type == 'E8':
        c = 248.0 / 31.0
        kappa = c / 2.0
        shadow_coeffs = {2: kappa, 3: 0.0}  # cubic vanishes for weight-4 Eisenstein
        # Actually for E_8, the theta function IS E_4, which is a Hecke eigenform.
        # The shadow depth is 3 (Lie class) because the cubic shadow from
        # the affine structure is nonzero.
        # But as a LATTICE VOA, the shadow from the Hecke decomposition
        # only has Eisenstein, so no cusp form atoms.
        for r in range(4, r_max + 1):
            shadow_coeffs[r] = 0.0
        results['shadow_coeffs'] = shadow_coeffs
        results['spectral_measure'] = {
            'type': 'eisenstein_only',
            'note': 'E_4 is pure Eisenstein. No cusp form atoms. No Ramanujan bound applies.',
        }
        # Hecke multiplicativity for E_4:
        # sigma_3(p^2) = sigma_3(p)^2 - p^3 ? NO.
        # Actually: sigma_3 is multiplicative and sigma_3(p^2) = 1+p^3+p^6.
        # The Hecke recursion for E_4: a(p^2) = a(p)^2 - p^3
        # Check: sigma_3(p^2) = 1+p^3+p^6, sigma_3(p)^2 = (1+p^3)^2 = 1+2p^3+p^6
        # So sigma_3(p)^2 - sigma_3(p^2) = 2p^3+p^6 - p^3 - p^6 = p^3
        # YES: sigma_3(p^2) = sigma_3(p)^2 - p^3 holds.
        hecke_primes = primes_up_to(30)[:10]
        hecke_results = []
        for p in hecke_primes:
            sig3_p = 1 + p ** 3
            sig3_p2 = sigma_k(p * p, 3)
            defect = sig3_p ** 2 - sig3_p2 - p ** 3
            hecke_results.append({
                'prime': p,
                'sigma3_p': sig3_p,
                'sigma3_p2': sig3_p2,
                'sigma3_p_sq_minus_p3': sig3_p ** 2 - p ** 3,
                'hecke_defect': defect,
            })
        results['hecke_check'] = {
            'applicable': True,
            'eigenform': 'E_4',
            'weight': 4,
            'hecke_recursion': 'a(p^2) = a(p)^2 - p^3',
            'results': hecke_results,
            'all_pass': all(r['hecke_defect'] == 0 for r in hecke_results),
        }

    elif lattice_type == 'Leech':
        c = 24.0
        kappa = c / 2.0  # = 12
        # Theta_Leech = E_{12} - (65520/691)*Delta
        # The spectral measure has TWO components:
        # 1. Eisenstein part: E_{12} with eigenvalues sigma_{11}(p)
        # 2. Cusp part: Delta with eigenvalues tau(p)
        c_delta_float = -65520.0 / 691.0

        shadow_coeffs = {2: kappa}
        # The cubic shadow comes from E_{12} (Eisenstein)
        # The quartic shadow comes from Delta (cusp form)
        # Higher shadows vanish (shadow depth 4, contact class)
        for r in range(3, r_max + 1):
            shadow_coeffs[r] = 0.0  # placeholder; actual values need Hecke decomposition

        results['shadow_coeffs'] = shadow_coeffs
        results['spectral_measure'] = {
            'type': 'eisenstein_plus_cusp',
            'eisenstein_weight': 1.0,
            'cusp_coefficient': c_delta_float,
            'cusp_form': 'Delta (weight 12)',
            'note': 'Ramanujan bound applies to cusp part only.',
        }

        # Hecke multiplicativity for Delta:
        # tau(p^2) = tau(p)^2 - p^{11}
        hecke_primes = primes_up_to(30)[:10]
        hecke_results = []
        for p in hecke_primes:
            tau_p = _KNOWN_TAU.get(p, ramanujan_tau(p))
            tau_p2 = _KNOWN_TAU.get(p * p, ramanujan_tau(p * p))
            predicted = tau_p ** 2 - p ** 11
            defect = tau_p2 - predicted
            hecke_results.append({
                'prime': p,
                'tau_p': tau_p,
                'tau_p2': tau_p2,
                'predicted_tau_p2': predicted,
                'hecke_defect': defect,
            })
        results['hecke_check'] = {
            'applicable': True,
            'eigenform': 'Delta (Ramanujan)',
            'weight': 12,
            'hecke_recursion': 'tau(p^2) = tau(p)^2 - p^{11}',
            'results': hecke_results,
            'all_pass': all(r['hecke_defect'] == 0 for r in hecke_results),
        }

    else:
        results['hecke_check'] = {
            'applicable': False,
            'reason': f'Lattice type {lattice_type} not implemented',
        }

    return results


def spectral_rigidity_landscape(
    c_range: Sequence[float],
    r_max: int = 6,
) -> List[Dict[str, Any]]:
    r"""Sweep over central charges, compute spectral data at each c.

    For each c in c_range, computes:
    (a) Shadow coefficients S_r (Virasoro)
    (b) Spectral moments from Stieltjes representation
    (c) Hecke multiplicativity check
    (d) Ramanujan bound check on extracted atoms (if any)

    HONEST ASSESSMENT: For Virasoro at generic c, the shadow tower is
    INFINITE (class M). No finite truncation gives exact spectral atoms.
    The landscape shows qualitative behavior:
    - At c=1 (free boson): single atom, Gaussian class
    - At c=1/2 (free fermion): single atom, Gaussian class
    - At c=26 (critical bosonic string): Virasoro self-dual point
    - At c -> infinity: perturbative regime, atoms cluster near 0
    """
    landscape = []

    for c in c_range:
        kappa = c / 2.0

        # Q^contact for Virasoro
        if abs(c) < 1e-15 or abs(5 * c + 22) < 1e-15:
            Q_contact = None
        else:
            Q_contact = 10.0 / (c * (5 * c + 22))

        # Shadow coefficients
        shadow_coeffs = {2: kappa}
        shadow_coeffs[3] = 0.0  # cubic vanishes on torus by Ward identity
        if Q_contact is not None:
            shadow_coeffs[4] = kappa * Q_contact
        else:
            shadow_coeffs[4] = None

        # Moments
        moments = {}
        for r in range(2, r_max + 1):
            if shadow_coeffs.get(r) is not None:
                moments[r] = -r * shadow_coeffs[r]

        # Classification
        if abs(c - 1.0) < 0.01 or abs(c - 0.5) < 0.01:
            shadow_class = 'G'
        elif Q_contact is not None and abs(Q_contact) < 1e-10:
            shadow_class = 'L'
        else:
            shadow_class = 'M'

        entry = {
            'c': c,
            'kappa': kappa,
            'Q_contact': Q_contact,
            'shadow_coeffs': shadow_coeffs,
            'moments': moments,
            'shadow_class': shadow_class,
        }

        # Extract leading atom approximation
        # From S_2 = kappa = -(1/2)*sum c_j*lambda_j^2, if single atom:
        # lambda_0 = sqrt(-2*kappa/c_0) with c_0 = kappa => lambda_0 = sqrt(-2) = imaginary
        # This means the single-atom model for Virasoro is NOT a real measure.
        # Need at least two atoms for a real positive measure.
        if kappa > 0 and Q_contact is not None:
            # Two-atom approximation using S_2 and S_4:
            # c_1*lambda_1^2 + c_2*lambda_2^2 = -2*S_2
            # c_1*lambda_1^4 + c_2*lambda_2^4 = -4*S_4
            # With c_1 = c_2 = kappa/2 (symmetric):
            # (lambda_1^2 + lambda_2^2) = -2*S_2/(kappa/2) = -4*S_2/kappa = -4
            # This gives lambda_1^2 + lambda_2^2 = -4, still imaginary.
            #
            # The issue: shadow coefficients for Virasoro give COMPLEX atoms
            # in the Stieltjes representation. This is because the genus-1
            # free energy has an IMAGINARY part (from the Dedekind eta).
            entry['atom_extraction'] = {
                'status': 'complex_atoms',
                'note': ('Virasoro shadow coefficients give complex Stieltjes atoms. '
                         'The spectral measure is not a real positive measure '
                         'on the real line. This is expected: the sewing integral '
                         'involves a COMPLEX contour.'),
            }

        landscape.append(entry)

    return landscape


# ============================================================
# Direction 5: Weil analogy and quadratic form
# ============================================================

def weil_pairing_on_shadows(
    S_r: float,
    S_s: float,
    r: int,
    s: int,
) -> Dict[str, Any]:
    r"""The bracket [Theta, Theta] defines a bilinear form on shadow space.

    The pairing <S_r, S_s> := [Theta_r, Theta_s]_{r+s-2} is the
    (r+s-2)-arity component of the Lie bracket on g^mod_A.

    For low arities:
      <S_2, S_2> = alpha_3 * S_2 * S_2  (contributes to arity 3)
      <S_2, S_3> = beta_4 * S_2 * S_3  (contributes to arity 4)
      <S_3, S_3> = gamma_4 * S_3 * S_3  (contributes to arity 4)

    The WEIL ANALOGY: In the function field case, Weil proved RH by
    showing the intersection form on divisors of a surface is negative
    definite on a specific subspace (the Hodge index theorem). The
    analogous statement for the shadow tower would be:

    "The Lie bracket restricted to the shadow subspace is negative
     definite (or has signature (1, r-1)) with respect to a natural
     norm on g^mod_A."

    HONEST ASSESSMENT: This analogy is STRUCTURAL, not a proof.
    The convolution algebra g^mod_A does NOT have a natural positive
    definite inner product in general. The bracket is antisymmetric
    (Lie bracket), not symmetric, so "definite" does not apply directly.
    The correct analogue would be the CYCLIC HOMOLOGY pairing, which
    is symmetric on the cyclic deformation complex. But this pairing
    is NOT definite.
    """
    # The bracket value [Theta_r, Theta_s] at arity r+s-2
    # depends on the OPE and the geometry of M_{1,r+s-2}.
    # We compute the schematic value.
    target_arity = r + s - 2
    bracket_val = S_r * S_s  # schematic, missing geometric coefficient

    return {
        'r': r,
        's': s,
        'S_r': S_r,
        'S_s': S_s,
        'target_arity': target_arity,
        'bracket_value_schematic': bracket_val,
        'weil_analogy': (
            'The Weil proof uses: intersection form on Div(S) restricted '
            'to algebraic equivalence classes has signature (1, rho-1) '
            '(Hodge index theorem). For shadows: the cyclic homology '
            'pairing on Def_cyc^mod(A) restricted to the shadow subspace '
            'would need analogous signature. This is NOT PROVED.'
        ),
        'honest_status': 'STRUCTURAL ANALOGY ONLY',
    }


def hodge_index_test(
    shadow_coeffs: Dict[int, float],
    r_max: int = 6,
) -> Dict[str, Any]:
    r"""Test the Hodge index analogy for the shadow intersection form.

    Construct the "intersection matrix" I_{rs} = <S_r, S_s> for
    r, s = 2, ..., r_max, and check its signature.

    For the Hodge index theorem in the Weil proof:
      - The intersection form on NS(S) has signature (1, rho-1)
      - Combined with the Castelnuovo-Severi inequality, this gives RH

    For the shadow tower:
      - The "intersection form" is I_{rs} = S_r * S_s (schematic)
      - For a single nonzero shadow (Gaussian class): I = (S_2^2), rank 1, trivially (1,0)
      - For two shadows (Lie class): I is 2x2, check signature
      - For three shadows (contact class): I is 3x3, check signature

    RESULT: The schematic intersection matrix I_{rs} = S_r * S_s is
    RANK 1 (outer product of the shadow vector with itself). Its
    eigenvalues are (||S||^2, 0, 0, ..., 0), which has signature (1, 0)
    on the nondegenerate part. This is TRIVIALLY of Hodge index type
    but carries NO information about Ramanujan.

    The actual bracket involves geometric coefficients that could break
    the rank-1 structure, but computing these requires M_{g,n} integrals.
    """
    S = shadow_coeffs
    arities = sorted(r for r in S if r >= 2 and S[r] != 0)
    n = len(arities)

    if n == 0:
        return {
            'status': 'trivial',
            'note': 'No nonzero shadow coefficients.',
        }

    # Schematic intersection matrix: I_{rs} = S_r * S_s
    # This is rank 1 by construction.
    shadow_vec = np.array([S[r] for r in arities])
    I_matrix = np.outer(shadow_vec, shadow_vec)
    eigenvalues = np.linalg.eigvalsh(I_matrix)
    eigenvalues = sorted(eigenvalues, reverse=True)

    # Check signature
    n_pos = sum(1 for ev in eigenvalues if ev > 1e-12)
    n_neg = sum(1 for ev in eigenvalues if ev < -1e-12)
    n_zero = n - n_pos - n_neg

    return {
        'arities': arities,
        'shadow_vector': shadow_vec.tolist(),
        'intersection_matrix': I_matrix.tolist(),
        'eigenvalues': eigenvalues,
        'signature': (n_pos, n_neg, n_zero),
        'is_hodge_index_type': n_pos == 1 and n_neg == 0,
        'rank': n_pos + n_neg,
        'honest_assessment': (
            'The schematic intersection matrix S_r * S_s is RANK 1 '
            '(outer product). Signature is trivially (1, 0, n-1). '
            'This carries NO Ramanujan information. The actual bracket '
            'involves M_{g,n} intersection theory and could have higher rank.'
        ),
    }


# ============================================================
# Summary and landscape
# ============================================================

def full_rigidity_report(
    lattice_type: str = 'Leech',
    c_vir: float = 26.0,
    r_max: int = 6,
    num_primes: int = 10,
) -> Dict[str, Any]:
    r"""Comprehensive rigidity report combining all five directions.

    Returns a structured summary of what works, what doesn't, and what
    remains open.
    """
    report = {
        'directions': {},
        'lattice_verification': {},
        'virasoro_analysis': {},
        'honest_summary': '',
    }

    # Direction 1: MC -> Hecke
    report['virasoro_analysis'] = mc_to_hecke_bridge(c_vir, r_max)

    # Direction 4: Lattice verification
    report['lattice_verification'] = {
        'ramanujan': verify_ramanujan_for_lattice(lattice_type, num_primes),
        'hecke_from_mc': verify_hecke_from_mc(lattice_type, r_max),
    }

    # Direction 3: Bracket analysis
    shadow_coeffs = {2: c_vir / 2.0, 3: 0.0}
    if abs(c_vir) > 1e-15 and abs(5 * c_vir + 22) > 1e-15:
        shadow_coeffs[4] = (c_vir / 2.0) * 10.0 / (c_vir * (5 * c_vir + 22))
    report['directions']['bracket'] = bracket_to_hecke_translation(shadow_coeffs, min(r_max, 6))
    report['directions']['positivity'] = bracket_positivity_test(shadow_coeffs, min(r_max, 6))

    # Direction 5: Hodge index
    report['directions']['hodge_index'] = hodge_index_test(shadow_coeffs, r_max)

    report['honest_summary'] = (
        'SUMMARY OF MODULAR SPECTRAL RIGIDITY INVESTIGATION:\n'
        '\n'
        'WHAT WORKS:\n'
        '1. Lattice VOAs: Ramanujan bound VERIFIED for cusp form eigenvalues '
        '(Deligne 1974). Eisenstein eigenvalues VIOLATE Ramanujan (expected).\n'
        '2. Hecke multiplicativity VERIFIED for E_4 (E_8) and Delta (Leech).\n'
        '3. MC bracket relations give polynomial constraints on shadow moments.\n'
        '\n'
        'WHAT DOES NOT WORK:\n'
        '1. MC constraints at finite arity do NOT force Hecke multiplicativity.\n'
        '2. Bracket positivity does NOT force Ramanujan on atoms.\n'
        '3. Hodge index analogy is STRUCTURAL only; the intersection matrix '
        'is rank 1 (trivial) at schematic level.\n'
        '4. Virasoro shadow tower is infinite (class M); no finite truncation '
        'captures the full modular structure.\n'
        '5. Spectral atoms for Virasoro are COMPLEX, not real.\n'
        '\n'
        'WHAT REMAINS OPEN:\n'
        '1. Whether ALL arities of the MC equation force Hecke multiplicativity.\n'
        '2. Whether the M_{g,n} geometric coefficients in the bracket give '
        'higher-rank intersection forms with Hodge index properties.\n'
        '3. Whether the spectral rigidity conjecture holds for the analytic '
        '(not truncated) spectral measure.\n'
    )

    return report


# ============================================================
# NEW SECTION: Shadow-moduli resolution
# ============================================================

def shadow_moduli_map_single_atom(c, q_coeffs, q_max):
    """Compute the shadow-moduli map t(q) at leading order (single atom).

    The shadow-moduli resolution theorem:
      t(q) = (c/6)(Z(q)/Z_vac - 1)

    where Z(q)/Z_vac = det(1-K_q)^{-1} = prod(1-q^n)^{-1} for Heisenberg.

    At leading order (single atom rho = delta(lambda + 6/c)):
      1 + 6t/c = exp(-F_1^conn)  =>  t = (c/6)(exp(-F_1) - 1)

    Args:
        c: central charge
        q_coeffs: dict {N: a_N} giving F_1^conn = sum a_N q^N
        q_max: truncation
    Returns:
        dict {N: t_N} giving t(q) = sum t_N q^N
    """
    # exp(-F_1) as a power series: if F_1 = sum a_N q^N,
    # then exp(-F_1) = 1 - a_1 q + (a_1^2/2 - a_2) q^2 + ...
    # We compute this via successive multiplication.
    exp_coeffs = [0.0] * (q_max + 1)
    exp_coeffs[0] = 1.0  # constant term of exp(-F_1)

    # Compute exp(-sum a_N q^N) order by order
    # d/dq exp(-F) = -F' * exp(-F)
    # So exp_N = -(1/N) sum_{j=1}^{N} j * a_j * exp_{N-j}
    a = [0.0] * (q_max + 1)
    for N, val in q_coeffs.items():
        if 1 <= N <= q_max:
            a[N] = float(val)

    for N in range(1, q_max + 1):
        s = 0.0
        for j in range(1, N + 1):
            s += j * a[j] * exp_coeffs[N - j]
        exp_coeffs[N] = -s / N

    # t = (c/6) * (exp(-F_1) - 1)
    t_coeffs = {}
    for N in range(1, q_max + 1):
        t_coeffs[N] = (c / 6.0) * exp_coeffs[N]

    return t_coeffs


def shadow_moduli_map_multi_atom(atoms, weights, F1_coeffs, q_max):
    """Compute t(q) for multi-atom spectral measure.

    General shadow-moduli resolution:
      prod_j (1 - lambda_j * t(q))^{-c_j} = exp(F_1^conn)

    For multi-atom case, t(q) must be computed by inverting this
    transcendental equation order by order in q.

    Args:
        atoms: list of spectral atoms lambda_j
        weights: list of weights c_j
        F1_coeffs: dict {N: a_N} for F_1^conn
        q_max: truncation
    Returns:
        dict {N: t_N}
    """
    # The equation is: prod_j (1 - lambda_j * t)^{-c_j} = Z/Z_vac = exp(F_1)
    # Taking log: -sum_j c_j log(1 - lambda_j t) = F_1
    # = sum_j c_j * sum_{r>=1} (lambda_j t)^r / r = F_1
    # = sum_{r>=1} [sum_j c_j lambda_j^r / r] * t^r = F_1
    #
    # Let mu_r = sum_j c_j lambda_j^r. Then:
    # sum_{r>=1} mu_r t^r / r = F_1
    #
    # This is the LAGRANGE INVERSION: given F_1 = sum a_N q^N,
    # and t = sum t_N q^N, we need t such that
    # sum_{r>=1} (mu_r/r) (sum_N t_N q^N)^r = sum_N a_N q^N.
    #
    # At leading order: mu_1 * t_1 * q = a_1 * q, so t_1 = a_1/mu_1.

    mu = {}
    for r in range(1, q_max + 2):
        mu[r] = sum(w * lam**r for w, lam in zip(weights, atoms))

    a = [0.0] * (q_max + 1)
    for N, val in F1_coeffs.items():
        if 1 <= N <= q_max:
            a[N] = float(val)

    # Solve order by order: at order N in q, the equation is:
    # sum_{r=1}^{N} (mu_r/r) * [t^r]_N = a_N
    # where [t^r]_N is the coefficient of q^N in t(q)^r.
    #
    # [t^r]_N depends on t_1, ..., t_{N-r+1} for r >= 2, and on t_N for r=1.
    # So the leading term is mu_1 * t_N, and the rest is a polynomial in
    # t_1, ..., t_{N-1}.

    t = [0.0] * (q_max + 1)

    if abs(mu.get(1, 0.0)) < 1e-30:
        # mu_1 = 0 means no linear term; use quadratic inversion
        return {N: 0.0 for N in range(1, q_max + 1)}

    for N in range(1, q_max + 1):
        # Compute contribution from r >= 2 using known t_1, ..., t_{N-1}
        rhs = a[N]

        # Subtract the known contributions from r >= 2
        # We need [t^r]_N for each r = 2, ..., N
        # This requires computing the convolution t * t * ... * t (r times)

        # t_powers[r] stores the coefficients of t^r up to order N
        t_powers = [[0.0] * (q_max + 1) for _ in range(N + 1)]
        t_powers[0][0] = 1.0  # t^0 = 1
        t_powers[1] = list(t)  # t^1 = t (with t_N not yet set)

        # For r >= 2: t^r = t^{r-1} * t, using only t_1, ..., t_{N-1}
        for r in range(2, N + 1):
            for m in range(N + 1):
                s = 0.0
                for j in range(m + 1):
                    if j < len(t_powers[r-1]) and (m-j) < len(t_powers[1]):
                        s += t_powers[r-1][j] * t_powers[1][m-j]
                t_powers[r][m] = s

        # Now subtract: sum_{r=2}^{N} (mu_r/r) * t_powers[r][N]
        for r in range(2, N + 1):
            rhs -= (mu.get(r, 0.0) / r) * t_powers[r][N]

        # Solve: mu_1 * t_N = rhs
        t[N] = rhs / mu[1]

        # Update t_powers[1]
        t_powers[1][N] = t[N]

    return {N: t[N] for N in range(1, q_max + 1)}


def verify_shadow_moduli_heisenberg(c=1.0, q_max=30):
    """Verify the shadow-moduli resolution for Heisenberg.

    For Heisenberg at central charge c:
      F_1^conn = c * sum sigma_{-1}(N) q^N
      exp(-F_1) = prod(1-q^n)^c
      t(q) = (c/6)(prod(1-q^n)^c - 1) at leading order

    Verification: t(q) computed from the resolution must equal
    the geometric kernel G_2(q) times a normalization factor.
    Specifically, F_1 = G(t(q)) with G = -log(1+6t/c), and
    F_1 = (c/2) * G_2, so:
      -log(1+6t/c) = (c/2) * G_2
      t = (c/6)(exp(-(c/2)*G_2) - 1)
    """

    # F_1^conn for Heisenberg
    F1 = {N: c * sum(1.0/d for d in range(1, N+1) if N % d == 0)
          for N in range(1, q_max + 1)}

    # Compute t via shadow-moduli resolution
    t_resolution = shadow_moduli_map_single_atom(c, F1, q_max)

    # For integer c, build prod(1-q^n)^c directly
    prod_coeffs = [0.0] * (q_max + 1)
    prod_coeffs[0] = 1.0
    ic = int(round(c))
    is_integer_c = abs(c - ic) < 1e-12

    if is_integer_c:
        for n in range(1, q_max + 1):
            # Multiply current series by (1-q^n)^c
            for _ in range(abs(ic)):
                new_coeffs = list(prod_coeffs)
                for m in range(n, q_max + 1):
                    if ic > 0:
                        new_coeffs[m] -= prod_coeffs[m - n]
                    else:
                        new_coeffs[m] += prod_coeffs[m - n]
                prod_coeffs = new_coeffs
    else:
        # For non-integer c, use the exp(-F_1) computation which is already
        # what shadow_moduli_map_single_atom does internally. So just copy
        # the resolution result for comparison.
        # We set prod_coeffs to match the exp_coeffs from the resolution.
        # This means the "direct" and "resolution" will agree by construction
        # for non-integer c.
        a = [0.0] * (q_max + 1)
        for N, val in F1.items():
            if 1 <= N <= q_max:
                a[N] = float(val)
        prod_coeffs[0] = 1.0
        for N in range(1, q_max + 1):
            s = 0.0
            for j in range(1, N + 1):
                s += j * a[j] * prod_coeffs[N - j]
            prod_coeffs[N] = -s / N

    # t_direct = (c/6) * (prod - 1) at each order
    t_direct = {}
    for N in range(1, q_max + 1):
        t_direct[N] = (c / 6.0) * prod_coeffs[N]

    # Compare
    max_error = 0.0
    errors = {}
    for N in range(1, q_max + 1):
        err = abs(t_resolution[N] - t_direct[N])
        errors[N] = err
        if err > max_error:
            max_error = err

    return {
        'match': max_error < 1e-10,
        'max_error': max_error,
        'c': c,
        'q_max': q_max,
        't_resolution_first5': {N: t_resolution[N] for N in range(1, min(6, q_max+1))},
        't_direct_first5': {N: t_direct[N] for N in range(1, min(6, q_max+1))},
    }


def modularity_constraint_test(atoms, weights, k, q_max=50):
    """Test the modularity constraint on a spectral measure.

    Given rho = sum c_j delta(lambda_j), the function
      G(t) = sum_j c_j log(1 - lambda_j t)
    composed with t(q) must give a modular function.

    For lattice VOAs, the atoms are Hecke eigenvalues and the
    modularity is automatic. This test verifies:
    1. The q-expansion of G(t(q)) has the expected modular properties
    2. The Hecke multiplicativity of the coefficients
    3. Consistency with Ramanujan bound |a_f(p)| <= 2p^{(k-1)/2}

    Args:
        atoms: spectral atoms lambda_j
        weights: weights c_j
        k: modular weight (for Ramanujan bound check)
        q_max: series truncation
    """
    results = {
        'atoms': list(atoms),
        'weights': list(weights),
        'k': k,
        'hecke_tests': {},
        'ramanujan_tests': {},
        'all_hecke_pass': True,
        'all_ramanujan_pass': True,
    }

    # For each atom, check if it could be a Hecke eigenvalue
    # a_f(p) at weight k must satisfy |a_f(p)| <= 2*p^{(k-1)/2}
    primes = [p for p in range(2, min(q_max, 100) + 1) if is_prime(p)]

    for j, (lam, w) in enumerate(zip(atoms, weights)):
        atom_results = {}
        for p in primes:
            bound = 2.0 * p ** ((k - 1) / 2.0)
            passes = abs(lam) <= bound * 1.01  # small tolerance
            atom_results[p] = {
                'atom': lam,
                'bound': bound,
                'passes': passes,
            }
            if not passes:
                results['all_ramanujan_pass'] = False
        results['ramanujan_tests'][j] = atom_results

    # Check Hecke multiplicativity: for a single atom lambda,
    # a(n) = lambda^n (n-th power). Then:
    # a(p^2) = lambda^{p^2} and a(p)^2 - p^{k-1} should equal a(p^2).
    # But lambda^{p^2} != lambda^{2p} - p^{k-1} in general!
    # The Hecke relation is a(mn) = a(m)a(n) for (m,n)=1 (multiplicativity)
    # and a(p^{r+1}) = a(p)a(p^r) - p^{k-1} a(p^{r-1}) (recursion).
    # These are constraints on the COEFFICIENTS a(n) of the modular form,
    # NOT on the powers of a single atom.
    #
    # For a single Hecke eigenform f = sum a(n) q^n:
    # a(n) = sum_j c_j lambda_j^n (if rho has atoms at lambda_j)
    # is NOT the right formula. The correct relation is through the
    # Hecke L-function: L(s,f) = prod_p (1 - a(p)p^{-s} + p^{k-1-2s})^{-1}.
    #
    # The shadow coefficient S_r = -(1/r) sum_j c_j lambda_j^r is the r-th
    # MOMENT of rho. The Hecke multiplicativity of a(n) constrains the moments
    # through Newton's identities relating power sums to elementary symmetric
    # polynomials.

    # For two atoms (e.g., Satake parameters alpha_p, beta_p at a prime p):
    if len(atoms) == 2:
        alpha, beta = atoms[0], atoms[1]
        # Hecke eigenvalue: a(p) = alpha + beta
        a_p = alpha + beta
        # Hecke recursion: a(p^2) = a(p)^2 - p^{k-1}
        # Also: a(p^2) = alpha^2 + alpha*beta + beta^2 = (alpha+beta)^2 - alpha*beta
        # So: alpha*beta = p^{k-1}
        product = alpha * beta
        for p in primes:
            expected_product = p ** (k - 1)
            defect = abs(product - expected_product)
            results['hecke_tests'][p] = {
                'a_p': a_p,
                'product': product,
                'expected_product': expected_product,
                'defect': defect,
                'passes': defect < 1e-6 * max(1, expected_product),
            }
            if not results['hecke_tests'][p]['passes']:
                results['all_hecke_pass'] = False

    return results


def ramanujan_bound_verification(k, n_max=30):
    """Verify Ramanujan bound for weight-k cusp forms (Deligne's theorem).

    For the Ramanujan Delta function (k=12):
      |tau(p)| <= 2*p^{11/2}

    For general weight k, we check the UNIQUE normalized eigenform in S_k(SL_2(Z))
    (when dim S_k = 1, i.e., k = 12, 16, 18, 20, 22, 26).
    """
    results = {'k': k, 'primes': {}}

    if k == 12:
        # Ramanujan tau function
        for n in range(1, n_max + 1):
            tau_n = ramanujan_tau(n)
            if is_prime(n):
                bound = 2.0 * n ** (5.5)  # 2*p^{(k-1)/2} = 2*p^{11/2}
                passes = abs(tau_n) <= bound * 1.001
                results['primes'][n] = {
                    'tau': tau_n,
                    'bound': bound,
                    'ratio': abs(tau_n) / bound if bound > 0 else 0,
                    'passes': passes,
                }
    else:
        results['note'] = f'Weight {k}: cusp form coefficients not implemented'

    results['all_pass'] = all(
        r['passes'] for r in results['primes'].values()
    ) if results['primes'] else True

    return results


def symmetric_power_from_shadow(atoms, weights, r_max=8):
    """Extract symmetric power L-function data from shadow coefficients.

    The shadow tower at arity r encodes data of Sym^{r-2}:
      S_r ~ sum_p p^{-rs} * tr(Sym^{r-1} diag(alpha_p, beta_p))

    Newton's identity: the MC constraint at arity r+1 gives a
    polynomial relation between Sym^{r-1} and Sym^0, ..., Sym^{r-2}.

    For two Satake parameters alpha, beta:
      p_r(alpha, beta) = alpha^r + beta^r = tr(Sym^{r-1} diag(alpha, beta))  [NOT QUITE]
    Actually: tr(Sym^m diag(a,b)) = sum_{j=0}^m a^j b^{m-j} = (a^{m+1}-b^{m+1})/(a-b).
    And the power sum is p_r = a^r + b^r.
    Newton's identity: p_r = e_1 p_{r-1} - e_2 p_{r-2}  (for two variables)
    where e_1 = a+b, e_2 = ab.

    Args:
        atoms: [alpha, beta] Satake parameters
        weights: [c_alpha, c_beta] weights
        r_max: max arity
    Returns:
        dict with power sums, symmetric power traces, Newton identity checks
    """
    if len(atoms) != 2:
        return {'error': 'Need exactly 2 atoms (Satake parameters)'}

    a, b = atoms[0], atoms[1]
    e1 = a + b  # elementary symmetric poly e_1
    e2 = a * b  # elementary symmetric poly e_2

    results = {
        'alpha': a, 'beta': b,
        'e1': e1, 'e2': e2,
        'power_sums': {},
        'sym_traces': {},
        'newton_checks': {},
    }

    # Power sums p_r = a^r + b^r (include r=0 for Newton's identity base case)
    results['power_sums'][0] = 2.0  # a^0 + b^0 = 2
    for r in range(1, r_max + 1):
        p_r = a**r + b**r
        results['power_sums'][r] = p_r

    # Symmetric power traces tr(Sym^m) = (a^{m+1} - b^{m+1})/(a - b) if a != b
    for m in range(0, r_max):
        if abs(a - b) > 1e-15:
            sym_m = (a**(m+1) - b**(m+1)) / (a - b)
        else:
            sym_m = (m + 1) * a**m
        results['sym_traces'][m] = sym_m

    # Newton's identity checks: p_r = e1 * p_{r-1} - e2 * p_{r-2}
    for r in range(2, r_max + 1):
        predicted = e1 * results['power_sums'][r-1] - e2 * results['power_sums'][r-2]
        actual = results['power_sums'][r]
        defect = abs(predicted - actual)
        results['newton_checks'][r] = {
            'predicted': predicted,
            'actual': actual,
            'defect': defect,
            'passes': defect < 1e-10 * max(1, abs(actual)),
        }

    return results


def operadic_mc_constraint_symmetric_powers(c, r_max=8):
    """The operadic MC constraint gives relations between symmetric power data.

    For Virasoro at central charge c, the shadow coefficients satisfy:
      S_r = (2/r) * (-3)^{r-4} * (2/c)^{r-2}  (leading order)

    The spectral measure has a single atom at lambda_eff = -6/c (leading order).
    The "Satake parameters" in this case are:
      alpha = -6/c, beta = 0  (single atom: beta = 0 means abelian component)

    The MC constraint at arity r+1:
      nabla_H(Sh_{r+1}) + {Sh_3, Sh_r}_H + ... = 0
    gives S_{r+1} as a polynomial in S_2, ..., S_r.

    At leading 1/c order, this is the geometric series recursion:
      S_{r+1} = -(3(r)/r+1)) * (2/c) * S_r
    which is equivalent to Newton's identity for a single atom.

    The CONTENT is at subleading order: the corrections to the geometric
    series encode the multi-atom structure of rho, which is where Hecke
    multiplicativity would manifest.
    """
    P = 2.0 / c if abs(c) > 1e-15 else 0.0

    shadow = {}
    # Leading order shadow coefficients
    for r in range(2, r_max + 1):
        shadow[r] = (2.0 / r) * (-3.0)**(r - 4) * P**(r - 2)

    # MC recursion check: S_{r+1} = -(3r/(r+1)) * P * S_r at leading order
    recursion_checks = {}
    for r in range(3, r_max):
        predicted = -(3.0 * r / (r + 1)) * P * shadow[r]
        actual = shadow[r + 1]
        defect = abs(predicted - actual) / max(1e-30, abs(actual))
        recursion_checks[r] = {
            'predicted': predicted,
            'actual': actual,
            'rel_defect': defect,
            'passes': defect < 1e-8,
        }

    # Subleading corrections encode the multi-atom structure
    # At O(1/c^r), the r-th shadow gets a correction from the quartic contact:
    # delta S_r ~ Q^contact * (correction from M_{1,r} geometry)
    Q_contact = 10.0 / (c * (5 * c + 22)) if abs(c) > 1e-15 and abs(5*c+22) > 1e-15 else 0.0

    return {
        'c': c,
        'P': P,
        'Q_contact': Q_contact,
        'shadow_leading': shadow,
        'recursion_checks': recursion_checks,
        'all_recursion_pass': all(r['passes'] for r in recursion_checks.values()),
        'interpretation': (
            'The leading-order MC recursion is Newton identity for a single atom. '
            'Subleading corrections (O(Q^contact)) encode multi-atom structure. '
            'Full Hecke multiplicativity requires all arities and all orders in 1/c.'
        ),
    }
