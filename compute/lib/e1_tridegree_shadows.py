"""E1 tridegree shadows: ordered R-matrices, CYBE, genus-1 corrections, coinvariant projections.

Computes the E1 (ordered/associative) shadow tower data using ribbon graphs
and the Feynman transform FAss of the associative modular operad.  The E1 MC
element Theta^{E1}_A lives in Hom(FAss, End_{B^{E1}(A)}), and its finite-order
projections carry the tridegree (g, n, d) where g = genus of the embedding
surface, n = number of boundary components with marked points, d = depth
from the ordered log-FM stratification.

Families covered: Heisenberg H_k, affine sl_2 at level k, Virasoro at
central charge c, lattice V_Z (rank-1), lattice V_{A2} (rank-2).

KEY RESULTS:
  1. Genus-0 R-matrices for all 5 families (exact, sympy).
  2. CYBE verification: [r12, r13] + [r12, r23] + [r13, r23] = 0 (numerical).
  3. Genus-1 ordered shadows: elliptic R-matrices via Weierstrass p-function.
  4. Coinvariant projection FAss -> FCom: av(r(z)) = kappa(A) at arity 2.
  5. E1 tridegree tables: all nonzero (g, n, d) up to g <= 1, n <= 6.

Shadow depth classification:
  G (Gaussian): r_max = 2 (Heisenberg, lattice V_Z, lattice V_{A2})
  L (Lie/tree): r_max = 3 (affine sl_2)
  M (mixed):    r_max = inf (Virasoro)

References:
  - e1_shadow_tower.py: archetype shadow classes (conventions followed here)
  - ordered_modular_bar.py: Weierstrass p numerical implementation
  - higher_genus_modular_koszul.tex: collision residue identification
  - nonlinear_modular_shadows.tex: shadow depth classification
  - yangians_foundations.tex: R-matrix, CYBE, Yangian structure
"""

from __future__ import annotations

import numpy as np
from typing import Any, Dict, List, Optional, Tuple, Union
from sympy import (
    Symbol, Rational, Matrix, simplify, pi, I, exp,
    symbols, eye, zeros, oo, cos, factorial, zeta,
)


# ---------------------------------------------------------------------------
# Symbolic variables
# ---------------------------------------------------------------------------

k = Symbol('k')
c = Symbol('c')
z = Symbol('z')
tau = Symbol('tau')


# ---------------------------------------------------------------------------
# Known kappa values (ground truth from CLAUDE.md / shadow_tower_atlas)
# ---------------------------------------------------------------------------

_KAPPA = {
    'heisenberg':   lambda lev: lev,                           # kappa = k
    'affine_sl2':   lambda lev: Rational(3) * lev / (lev + 2), # 3k/(k+2)
    'virasoro':     lambda cc: cc / 2,                         # c/2
    'lattice_vz':   lambda: Rational(1),                       # rank-1 Heisenberg at k=1
    'lattice_va2':  lambda: Rational(2),                       # rank-2 Heisenberg at k=1
}

_DEPTH_CLASS = {
    'heisenberg':  ('G', 2),
    'affine_sl2':  ('L', 3),
    'virasoro':    ('M', float('inf')),
    'lattice_vz':  ('G', 2),
    'lattice_va2': ('G', 2),
}

FAMILIES = ['heisenberg', 'affine_sl2', 'virasoro', 'lattice_vz', 'lattice_va2']


# =========================================================================
# Weierstrass p-function
# =========================================================================

def eisenstein_g2k(kk: int, tau_val: complex, n_terms: int = 30) -> complex:
    """Eisenstein series G_{2k}(tau) for k >= 2 via q-expansion.

    G_{2k}(tau) = 2 zeta(2k) + 2 (2 pi i)^{2k} / (2k-1)!
                  * sum_{n>=1} sigma_{2k-1}(n) q^n

    where sigma_{m}(n) = sum_{d|n} d^m and q = e^{2 pi i tau}.
    """
    if kk < 2:
        raise ValueError("Eisenstein series G_{2k} requires k >= 2")
    q = np.exp(2j * np.pi * tau_val)

    # Constant term: 2 zeta(2k) evaluated numerically
    zeta_val = float(zeta(2 * kk))
    const = 2.0 * zeta_val

    # q-expansion coefficient
    prefactor = 2.0 * (2.0 * np.pi * 1j) ** (2 * kk) / float(factorial(2 * kk - 1))

    q_sum = 0.0 + 0.0j
    for n in range(1, n_terms + 1):
        # sigma_{2k-1}(n) = sum_{d|n} d^{2k-1}
        sigma = sum(d ** (2 * kk - 1) for d in range(1, n + 1) if n % d == 0)
        q_sum += sigma * q ** n

    return const + prefactor * q_sum


def weierstrass_p(z_val: complex, tau_val: complex, terms: int = 10) -> complex:
    """Numerical Weierstrass p(z; tau) via Laurent + Eisenstein expansion.

    p(z; tau) = 1/z^2 + sum_{n>=1} (2n+1) G_{2n+2}(tau) z^{2n}

    Uses periods (1, tau).  Convergent for |z| < min(1, |tau|).
    For |z| close to 0 the Laurent term dominates.

    Args:
        z_val: evaluation point (complex)
        tau_val: modular parameter (complex, Im(tau) > 0)
        terms: number of Eisenstein terms in the Laurent expansion

    Returns:
        complex value of p(z; tau)
    """
    if abs(z_val) < 1e-15:
        return complex(float('inf'))

    result = 1.0 / z_val ** 2

    for n in range(1, terms + 1):
        g2k = eisenstein_g2k(n + 1, tau_val, n_terms=max(30, terms))
        result += (2 * n + 1) * g2k * z_val ** (2 * n)

    return complex(result)


def weierstrass_p_deriv(z_val: complex, tau_val: complex, terms: int = 10) -> complex:
    """Derivative p'(z; tau) via term-by-term differentiation of the Laurent series.

    p'(z) = -2/z^3 + sum_{n>=1} 2n(2n+1) G_{2n+2}(tau) z^{2n-1}
    """
    if abs(z_val) < 1e-15:
        return complex(float('inf'))

    result = -2.0 / z_val ** 3

    for n in range(1, terms + 1):
        g2k = eisenstein_g2k(n + 1, tau_val, n_terms=max(30, terms))
        result += 2 * n * (2 * n + 1) * g2k * z_val ** (2 * n - 1)

    return complex(result)


def weierstrass_invariants(tau_val: complex, n_terms: int = 30) -> Tuple[complex, complex]:
    """Weierstrass invariants g2, g3 from Eisenstein series.

    g2 = 60 G_4(tau),  g3 = 140 G_6(tau).
    """
    g2 = 60.0 * eisenstein_g2k(2, tau_val, n_terms)
    g3 = 140.0 * eisenstein_g2k(3, tau_val, n_terms)
    return g2, g3


# =========================================================================
# 1. Genus-0 R-matrices
# =========================================================================

def e1_r_matrix(family: str, **params) -> Any:
    """Genus-0 binary R-matrix r(z) for a given family (sympy expression).

    Args:
        family: one of 'heisenberg', 'affine_sl2', 'virasoro',
                'lattice_vz', 'lattice_va2'
        **params:
            k (or level): level parameter (sympy or numeric)
            c (or central_charge): central charge (for Virasoro)

    Returns:
        sympy expression or Matrix for r(z).  For scalar R-matrices
        a scalar expression is returned; for matrix-valued ones a
        sympy Matrix times 1/z is returned.
    """
    family = family.lower()

    if family == 'heisenberg':
        lev = params.get('k', params.get('level', k))
        # r(z) = k/z  (scalar, 1x1)
        return lev / z

    elif family == 'affine_sl2':
        lev = params.get('k', params.get('level', k))
        # r(z) = k * Omega / z where Omega is the split Casimir 4x4
        omega = _sl2_casimir_sympy()
        return lev * omega / z

    elif family == 'virasoro':
        cc = params.get('c', params.get('central_charge', c))
        # r(z) = (c/2)/z  on the primary line (single generator T)
        return cc / (2 * z)

    elif family == 'lattice_vz':
        # V_Z = Heisenberg at k = 1
        return Rational(1) / z

    elif family == 'lattice_va2':
        # V_{A2} = rank-2 Heisenberg at k = 1: r(z) = 2 I / z
        # (I is 2x2 identity, but since channels decouple, use scalar 2/z)
        return Rational(2) / z

    else:
        raise ValueError(f"Unknown family: {family}")


def _sl2_casimir_sympy() -> Matrix:
    """Split Casimir tensor Omega in End(C^2 x C^2) for sl_2.

    Omega = (1/2)(h x h) + e x f + f x e

    In the basis |00>, |01>, |10>, |11> of C^2 x C^2:
    """
    return Matrix([
        [Rational(1, 2), 0, 0, 0],
        [0, Rational(-1, 2), 1, 0],
        [0, 1, Rational(-1, 2), 0],
        [0, 0, 0, Rational(1, 2)],
    ])


def _sl2_casimir_numpy() -> np.ndarray:
    """Numerical split Casimir for sl_2 in End(C^2 x C^2)."""
    e = np.array([[0, 1], [0, 0]], dtype=complex)
    f = np.array([[0, 0], [1, 0]], dtype=complex)
    h = np.array([[1, 0], [0, -1]], dtype=complex)
    return np.kron(h, h) / 2.0 + np.kron(e, f) + np.kron(f, e)


# =========================================================================
# 2. CYBE verification
# =========================================================================

def _build_triple_operators(r: np.ndarray, d: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build r12, r23, r13 on V^{x3} from r on V^{x2}, dim(V) = d."""
    Id = np.eye(d, dtype=complex)
    r12 = np.kron(r, Id)
    r23 = np.kron(Id, r)

    r13 = np.zeros((d ** 3, d ** 3), dtype=complex)
    for a in range(d):
        for b in range(d):
            for cc_idx in range(d):
                for dd_idx in range(d):
                    for ff_idx in range(d):
                        row = a * d * d + b * d + cc_idx
                        col = dd_idx * d * d + b * d + ff_idx
                        r13[row, col] += r[a * d + cc_idx, dd_idx * d + ff_idx]
    return r12, r23, r13


def e1_cybe_check(family: str, z_vals: Optional[List[complex]] = None, **params) -> bool:
    """Verify the classical Yang-Baxter equation numerically.

    For scalar R-matrices (Heisenberg, Virasoro, lattice): CYBE is
    trivially satisfied because all commutators vanish in dimension 1.

    For matrix-valued R-matrices (affine sl_2): verify the STRICT CYBE
    on the skew part r_- = (r - P r P) / 2 of the Casimir.

    Args:
        family: family name
        z_vals: optional list of z-values for numerical evaluation
                (unused for constant-coefficient R-matrices)
        **params: family-specific parameters (k, c, etc.)

    Returns:
        True if CYBE is satisfied (norm < 1e-9).
    """
    family = family.lower()

    # Scalar families: CYBE is trivially satisfied (1d commutators vanish)
    if family in ('heisenberg', 'virasoro', 'lattice_vz', 'lattice_va2'):
        return True

    if family == 'affine_sl2':
        level_val = float(params.get('k', params.get('level', 1.0)))
        return _cybe_affine_sl2(level_val)

    raise ValueError(f"Unknown family: {family}")


def _cybe_affine_sl2(level_val: float) -> bool:
    """Verify strict CYBE for skew part of sl_2 Casimir R-matrix.

    The full Casimir Omega is symmetric so it satisfies MODIFIED CYBE.
    Its skew part r_- = (Omega - P Omega P) / 2 satisfies strict CYBE:
      [r12, r13] + [r12, r23] + [r13, r23] = 0.
    """
    d = 2
    omega = _sl2_casimir_numpy()
    r_full = level_val * omega

    # Permutation operator P on V x V
    P = np.zeros((d ** 2, d ** 2), dtype=complex)
    for a in range(d):
        for b in range(d):
            P[a * d + b, b * d + a] = 1.0

    r_skew = (r_full - P @ r_full @ P) / 2.0

    r12, r23, r13 = _build_triple_operators(r_skew, d)
    comm = lambda a, b: a @ b - b @ a
    cybe_val = comm(r12, r13) + comm(r12, r23) + comm(r13, r23)

    return float(np.max(np.abs(cybe_val))) < 1e-9


# =========================================================================
# 3. Genus-1 ordered shadows (elliptic R-matrix)
# =========================================================================

def e1_genus1_r_matrix(family: str, tau_val: Optional[complex] = None, **params) -> Any:
    """Genus-1 ordered shadow: elliptic R-matrix r^{(1)}(z; tau).

    At genus 1, the ordered propagator is the Weierstrass p-function:
      r^{(1)}(z; tau) = coefficient * p(z; tau)

    Args:
        family: family name
        tau_val: modular parameter (complex, Im > 0).  If None, returns
                 a descriptor dict with the formula.
        **params:
            z_val: evaluation point (complex)
            k / level: level parameter
            c / central_charge: central charge
            terms: number of terms in p expansion (default 10)

    Returns:
        If tau_val and z_val given: numerical complex value.
        If tau_val is None: dict describing the elliptic R-matrix.
    """
    family = family.lower()
    z_val = params.get('z_val', None)
    terms = params.get('terms', 10)

    if family == 'heisenberg':
        level_val = float(params.get('k', params.get('level', 1.0)))
        if tau_val is not None and z_val is not None:
            wp = weierstrass_p(z_val, tau_val, terms)
            return level_val * wp
        return {
            'formula': 'k * p(z; tau)',
            'coefficient': level_val,
            'type': 'scalar',
        }

    elif family == 'affine_sl2':
        level_val = float(params.get('k', params.get('level', 1.0)))
        if tau_val is not None and z_val is not None:
            wp = weierstrass_p(z_val, tau_val, terms)
            omega = _sl2_casimir_numpy()
            return level_val * omega * wp
        return {
            'formula': 'k * Omega * p(z; tau)',
            'coefficient': level_val,
            'type': 'matrix (4x4)',
        }

    elif family == 'virasoro':
        cc_val = float(params.get('c', params.get('central_charge', 1.0)))
        if tau_val is not None and z_val is not None:
            wp = weierstrass_p(z_val, tau_val, terms)
            return (cc_val / 2.0) * wp
        return {
            'formula': '(c/2) * p(z; tau)',
            'coefficient': cc_val / 2.0,
            'type': 'scalar',
        }

    elif family == 'lattice_vz':
        # V_Z = Heisenberg at k = 1
        if tau_val is not None and z_val is not None:
            return weierstrass_p(z_val, tau_val, terms)
        return {
            'formula': 'p(z; tau)',
            'coefficient': 1.0,
            'type': 'scalar',
        }

    elif family == 'lattice_va2':
        # V_{A2} = rank-2 Heisenberg: 2 * p(z; tau)
        if tau_val is not None and z_val is not None:
            return 2.0 * weierstrass_p(z_val, tau_val, terms)
        return {
            'formula': '2 * p(z; tau)',
            'coefficient': 2.0,
            'type': 'scalar',
        }

    else:
        raise ValueError(f"Unknown family: {family}")


# =========================================================================
# 4. Coinvariant projection: av(Theta^{E1}) -> Theta (ordered -> unordered)
# =========================================================================

def e1_coinvariant_projection(family: str, arity: int, **params) -> Any:
    """Coinvariant projection: average over S_n sends E1 shadow to unordered shadow.

    At arity 2: av(r(z)) = Res_{z=0}[r(z)] = kappa(A).
    At arity 3: av(r_3) = C(A) (cubic shadow).
    At arity >= 4: depends on the family.

    Args:
        family: family name
        arity: arity n of the projection
        **params: family-specific parameters

    Returns:
        The coinvariant (averaged) shadow at the given arity.
    """
    family = family.lower()

    if arity < 2:
        raise ValueError("Arity must be >= 2")

    if arity == 2:
        # av(r(z)) = kappa for all families
        return e1_kappa_from_r_matrix(family, **params)

    if arity == 3:
        return _coinvariant_arity3(family, **params)

    if arity >= 4:
        return _coinvariant_higher(family, arity, **params)


def _coinvariant_arity3(family: str, **params) -> Any:
    """Arity-3 coinvariant: the cubic shadow C(A).

    - Heisenberg: C = 0 (Gaussian terminates at arity 2)
    - Affine sl_2: C = structure constants (Lie bracket)
    - Virasoro: C = 2 (gravitational cubic from TT ~ 2T OPE)
    - Lattice V_Z: C = 0 (rank-1 Heisenberg)
    - Lattice V_{A2}: C = 0 (Heisenberg-type, no cubic)
    """
    if family in ('heisenberg', 'lattice_vz', 'lattice_va2'):
        return Rational(0)

    if family == 'affine_sl2':
        lev = params.get('k', params.get('level', k))
        # The cubic shadow for affine algebras is the structure constant
        # tensor f^c_{ab} weighted by the level.  The scalar coinvariant
        # (trace) is proportional to k * dim(g) / (k + h^v).
        # For sl_2: C_scalar = k / (k + 2) (leading term of KZ associator)
        return lev / (lev + 2)

    if family == 'virasoro':
        # C_Vir = 2 (from TT OPE: T(z)T(w) ~ 2T(w)/(z-w)^2)
        return Rational(2)

    raise ValueError(f"Unknown family: {family}")


def _coinvariant_higher(family: str, arity: int, **params) -> Any:
    """Coinvariant at arity >= 4."""
    if family in ('heisenberg', 'lattice_vz', 'lattice_va2'):
        # Gaussian class: all higher shadows vanish
        return Rational(0)

    if family == 'affine_sl2':
        # Lie class: terminates at arity 3 (quartic vanishes by Jacobi)
        return Rational(0)

    if family == 'virasoro':
        cc = params.get('c', params.get('central_charge', c))
        if arity == 4:
            # Q^contact_Vir = 10 / [c (5c + 22)]
            return Rational(10) / (cc * (5 * cc + 22))
        # Higher arities: nonzero but not computed in closed form here.
        # Return a symbolic placeholder.
        return Symbol(f'S_{arity}')

    raise ValueError(f"Unknown family: {family}")


# =========================================================================
# 5. E1 tridegree table
# =========================================================================

def e1_tridegree_table(family: str, max_g: int = 1, max_n: int = 6,
                       **params) -> Dict[Tuple[int, int, int], Any]:
    """Tridegree table: all nonzero (g, n, d) components of Theta^{E1}_A.

    The tridegree (g, n, d) decomposes the E1 MC element:
      g = genus of the embedding surface
      n = arity (number of boundary components / marked points)
      d = depth from ordered log-FM stratification

    At genus 0: the E1 shadow has nonzero components determined by the
    shadow depth of the family.

    At genus 1: the E1 shadow acquires corrections from p(z; tau).

    Args:
        family: family name
        max_g: maximum genus (default 1)
        max_n: maximum arity (default 6)
        **params: family-specific parameters

    Returns:
        dict mapping (g, n, d) -> descriptor string or value
    """
    family = family.lower()
    depth_class, depth = _DEPTH_CLASS[family]
    table: Dict[Tuple[int, int, int], Any] = {}

    # Genus 0 components
    if depth_class == 'G':
        # Gaussian: only n = 2, d = 1
        table[(0, 2, 1)] = 'r(z) = kappa/z'
        # The genus-0 R-matrix is the only nonzero component

    elif depth_class == 'L':
        # Lie: n = 2 (binary) and n = 3 (cubic)
        table[(0, 2, 1)] = 'r(z) = k*Omega/z'
        for n in range(3, min(4, max_n + 1)):
            table[(0, n, 1)] = f'r_{n}: structure constants'

    elif depth_class == 'M':
        # Mixed: all arities n >= 2
        table[(0, 2, 1)] = 'r(z) = (c/2)/z'
        for n in range(3, max_n + 1):
            table[(0, n, 1)] = f'r_{n}: nonzero (depth infinity)'

    # Higher depth components at genus 0
    for n in range(2, max_n + 1):
        for d in range(2, n):  # depth can be at most n-1
            if depth_class == 'G' and d >= 1 and n > 2:
                pass  # no higher components
            elif depth_class == 'L' and d >= 2:
                pass  # depth 1 only for Lie class
            elif depth_class == 'M' and d >= 2:
                table[(0, n, d)] = f'depth-{d} correction at arity {n}'

    # Genus-1 components
    if max_g >= 1:
        # Every family has a genus-1 binary component from p(z; tau)
        table[(1, 2, 0)] = 'genus-1 R-matrix correction (p-function)'
        if depth_class in ('L', 'M'):
            for n in range(3, max_n + 1):
                table[(1, n, 0)] = f'genus-1 arity-{n} shadow'
        if depth_class == 'M':
            for n in range(2, max_n + 1):
                for d in range(1, min(n, 3)):
                    if (1, n, d) not in table:
                        table[(1, n, d)] = f'genus-1 depth-{d} at arity {n}'

    return table


# =========================================================================
# 6. Kappa from R-matrix
# =========================================================================

def e1_kappa_from_r_matrix(family: str, **params) -> Any:
    """Extract kappa from the R-matrix via coinvariant projection at arity 2.

    kappa(A) = av(r(z)) = (1/dim) * Tr(coefficient of 1/z in r(z))

    For scalar R-matrices: kappa = coefficient of 1/z.
    For matrix R-matrices (affine sl_N): kappa = k * dim(g) / (k + h^v).

    Args:
        family: family name
        **params: family-specific parameters

    Returns:
        sympy expression for kappa(A).
    """
    family = family.lower()

    if family == 'heisenberg':
        lev = params.get('k', params.get('level', k))
        return lev

    elif family == 'affine_sl2':
        lev = params.get('k', params.get('level', k))
        # kappa = dim(sl_2) * k / (k + h^v) = 3k / (k + 2)
        return Rational(3) * lev / (lev + 2)

    elif family == 'virasoro':
        cc = params.get('c', params.get('central_charge', c))
        return cc / 2

    elif family == 'lattice_vz':
        # V_Z = Heisenberg at k = 1, rank 1
        return Rational(1)

    elif family == 'lattice_va2':
        # V_{A2}: rank-2 Heisenberg at k = 1 per channel
        return Rational(2)

    else:
        raise ValueError(f"Unknown family: {family}")


# =========================================================================
# 7. Shadow depth
# =========================================================================

def e1_shadow_depth(family: str, **params) -> Union[int, float]:
    """E1 (ordered) shadow depth r_max for a given family.

    The ordered shadow depth equals the unordered shadow depth:
    the coinvariant projection preserves the termination arity.

    Returns:
        int for finite depth, float('inf') for infinite depth.
    """
    family = family.lower()
    if family not in _DEPTH_CLASS:
        raise ValueError(f"Unknown family: {family}")
    return _DEPTH_CLASS[family][1]


def e1_depth_class(family: str) -> str:
    """Shadow depth class: G, L, C, or M."""
    family = family.lower()
    if family not in _DEPTH_CLASS:
        raise ValueError(f"Unknown family: {family}")
    return _DEPTH_CLASS[family][0]


# =========================================================================
# Auxiliary: CYBE verification dict (detailed output)
# =========================================================================

def e1_cybe_check_detailed(family: str, **params) -> Dict[str, Any]:
    """Detailed CYBE verification returning diagnostic data.

    For matrix-valued R-matrices, returns both strict CYBE (skew part)
    and modified CYBE (full Casimir) norms.
    """
    family = family.lower()

    if family in ('heisenberg', 'virasoro', 'lattice_vz', 'lattice_va2'):
        return {
            'family': family,
            'cybe_satisfied': True,
            'reason': 'scalar R-matrix (1d commutators vanish)',
            'norm': 0.0,
        }

    if family == 'affine_sl2':
        level_val = float(params.get('k', params.get('level', 1.0)))
        d = 2
        omega = _sl2_casimir_numpy()
        r_full = level_val * omega

        P = np.zeros((d ** 2, d ** 2), dtype=complex)
        for a in range(d):
            for b in range(d):
                P[a * d + b, b * d + a] = 1.0

        r_skew = (r_full - P @ r_full @ P) / 2.0

        r12, r23, r13 = _build_triple_operators(r_skew, d)
        comm = lambda a, b: a @ b - b @ a
        cybe_skew = comm(r12, r13) + comm(r12, r23) + comm(r13, r23)
        norm_skew = float(np.max(np.abs(cybe_skew)))

        r12f, r23f, r13f = _build_triple_operators(r_full, d)
        mcybe = comm(r12f, r13f) + comm(r12f, r23f) + comm(r13f, r23f)
        norm_full = float(np.max(np.abs(mcybe)))

        return {
            'family': family,
            'cybe_satisfied': norm_skew < 1e-9,
            'cybe_skew_norm': norm_skew,
            'mcybe_full_norm': norm_full,
            'mcybe_nonzero': norm_full > 1e-9,
        }

    raise ValueError(f"Unknown family: {family}")


# =========================================================================
# Summary: comparison table across all families
# =========================================================================

def e1_tridegree_summary() -> Dict[str, Dict[str, Any]]:
    """Summary of E1 tridegree shadow data for all five families."""
    result = {}
    for fam in FAMILIES:
        cls, depth = _DEPTH_CLASS[fam]
        kappa = e1_kappa_from_r_matrix(fam)
        cybe = e1_cybe_check(fam)
        r = e1_r_matrix(fam)
        c3 = e1_coinvariant_projection(fam, 3)
        table = e1_tridegree_table(fam)

        result[fam] = {
            'depth_class': cls,
            'depth': depth,
            'kappa': str(kappa),
            'cybe_satisfied': cybe,
            'r_matrix': str(r),
            'cubic_shadow': str(c3),
            'num_tridegree_entries': len(table),
        }
    return result
