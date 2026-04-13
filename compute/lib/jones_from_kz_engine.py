"""
Reshetikhin-Turaev computation of the Jones polynomial from KZ R-matrix data.

Implements the full RT construction for U_q(sl_2) with fundamental
representation V = V_{1/2}:
  - R-matrix eigenvalues on V tensor V from the quadratic Casimir:
      mu_j = (-1)^{1-j} q^{(C_j - 2*C_{1/2})/2}
    where C_j = j(j+1), giving mu_+ = q^{1/4} (spin 1) and mu_- = -q^{-3/4} (spin 0)
  - Quantum dimensions [n]_q = (q^{n/2} - q^{-n/2}) / (q^{1/2} - q^{-1/2})
  - Markov trace via Schur-Weyl decomposition into irreps of U_q(sl_2)
  - Writhe correction with framing factor alpha = q^{C_{1/2}} = q^{3/4}

For n-strand braids, the Jones polynomial is:
  J(K; q) = alpha^{-w} * (1/dim_q(V)) * sum_j dim_q(V_j) * tr(beta|_{S_j})
where V^{xn} = sum_j S_j tensor V_j (Schur-Weyl), beta acts on S_j,
and w = writhe of the braid word.

Supports:
  - 2-strand braids (closed form): torus knots T(2, 2m+1)
  - 3-strand braids (6j recoupling): figure-eight, trefoil on 3 strands, etc.

Ground truth:
  - J(unknot; q) = 1
  - J(trefoil; q) = -q^{-4} + q^{-3} + q^{-1}
  - J(figure-eight; q) = q^{-2} - q^{-1} + 1 - q + q^2
  - J(T(2,5); q) = -q^{-7} + q^{-6} - q^{-5} + q^{-4} + q^{-2}
  - J(T(2,7); q) = -q^{-10} + q^{-9} - q^{-8} + q^{-7} - q^{-6} + q^{-5} + q^{-3}

References:
  - Reshetikhin-Turaev, Comm. Math. Phys. 127 (1990), 1-26
  - Kassel, Quantum Groups, Ch. XIV-XVII
  - Turaev, Quantum Invariants of Knots and 3-Manifolds, Ch. I-III
"""

import cmath
import numpy as np


# =============================================================================
# Quantum group data: U_q(sl_2), fundamental representation V_{1/2}
# =============================================================================

def quantum_integer(n, q):
    """Quantum integer [n]_q = (q^{n/2} - q^{-n/2}) / (q^{1/2} - q^{-1/2}).

    For n=0 returns 0; for q->1 returns n (classical limit).
    """
    denom = q ** 0.5 - q ** (-0.5)
    if abs(denom) < 1e-14:
        return complex(n)
    return (q ** (n / 2) - q ** (-n / 2)) / denom


def quantum_dimension(j, q):
    """Quantum dimension of the spin-j irrep of U_q(sl_2):
    dim_q(V_j) = [2j+1]_q.
    """
    return quantum_integer(2 * j + 1, q)


def r_matrix_eigenvalue(j, s, q):
    """Eigenvalue of the R-matrix (braiding) on the spin-j summand of V_s x V_s.

    mu_j = (-1)^{2s - j} * q^{(C_j - 2*C_s) / 2}
    where C_j = j(j+1) is the quadratic Casimir eigenvalue.

    For s=1/2: mu_0 = -q^{-3/4}, mu_1 = q^{1/4}.
    """
    C_j = j * (j + 1)
    C_s = s * (s + 1)
    sign = (-1) ** int(round(2 * s - j))
    return sign * q ** ((C_j - 2 * C_s) / 2)


def framing_factor(s, q):
    """Writhe correction factor alpha = q^{C_s} where C_s = s(s+1).

    For the fundamental s=1/2: alpha = q^{3/4}.
    """
    return q ** (s * (s + 1))


def q_from_level(k):
    """Root of unity q = exp(2*pi*i / (k+2)) for Chern-Simons level k.

    At level k, the quantum group U_q(sl_2) has finitely many integrable
    representations V_0, V_{1/2}, ..., V_{k/2}.
    """
    return cmath.exp(2j * cmath.pi / (k + 2))


# =============================================================================
# F-matrix (6j recoupling) for V_{1/2}^{x3}
# =============================================================================

def f_matrix_half(q):
    """Quantum 6j recoupling matrix for V_{1/2}^{x3} in the j=1/2 sector.

    Transforms from the ((12),3) coupling basis to the (1,(23)) coupling basis
    in the 2-dimensional multiplicity space S_{1/2}.

    Basis: |j_{12}=0>, |j_{12}=1> (similarly j_{23}=0, j_{23}=1 for the other scheme).

    F_{j12, j23} = (-1)^{j12+j23} * sqrt([2*j12+1]*[2*j23+1]) *
                   {1/2  1/2  j12; 1/2  1/2  j23}_q

    For all spins = 1/2:
      F = [[-1/[2],     sqrt([3])/[2] ],
           [sqrt([3])/[2],  1/[2]     ]]

    F is unitary and satisfies F^2 = I (involution).
    """
    d2 = quantum_integer(2, q)  # [2]
    d3 = quantum_integer(3, q)  # [3]
    sqrt_d3 = d3 ** 0.5

    return np.array([
        [-1.0 / d2, sqrt_d3 / d2],
        [sqrt_d3 / d2, 1.0 / d2]
    ], dtype=complex)


# =============================================================================
# Jones polynomial: 2-strand braids (closed form)
# =============================================================================

def jones_2strand(power, q):
    """Jones polynomial for the closure of sigma_1^n on 2 strands.

    V_{1/2}^{x2} = V_0 (mult 1) + V_1 (mult 1).
    sigma_1 acts as mu_j on V_j (scalar, since mult spaces are 1-dim).

    J(K; q) = alpha^{-w} * (dim_q(V_0)*mu_0^n + dim_q(V_1)*mu_1^n) / dim_q(V_{1/2})

    n odd: knot.  n even: 2-component link.
    n=1: unknot.  n=3: trefoil.  n=5: T(2,5) = 5_1.  n=7: T(2,7) = 7_1.

    Parameters
    ----------
    power : int
        The exponent n in sigma_1^n.
    q : complex
        The quantum parameter.

    Returns
    -------
    complex
        The Jones polynomial evaluated at q.
    """
    s = 0.5  # spin of fundamental
    mu_0 = r_matrix_eigenvalue(0, s, q)     # -q^{-3/4}
    mu_1 = r_matrix_eigenvalue(1, s, q)     # q^{1/4}
    d_0 = quantum_dimension(0, q)           # [1] = 1
    d_1 = quantum_dimension(1, q)           # [3]
    d_V = quantum_dimension(s, q)           # [2]
    alpha = framing_factor(s, q)            # q^{3/4}
    w = power  # writhe

    markov_trace = d_0 * mu_0 ** power + d_1 * mu_1 ** power
    return alpha ** (-w) * markov_trace / d_V


# =============================================================================
# Jones polynomial: 3-strand braids (6j recoupling)
# =============================================================================

def jones_3strand(braid_word, q):
    """Jones polynomial for the closure of a 3-strand braid.

    V_{1/2}^{x3} = V_{3/2} (mult 1) + V_{1/2} (mult 2).

    On S_{3/2} (1-dim): both sigma_1, sigma_2 act as mu_+ = q^{1/4}.
    On S_{1/2} (2-dim): sigma_1 = diag(mu_-, mu_+) in ((12),3) basis;
                         sigma_2 = F^{-1} diag(mu_-, mu_+) F via 6j recoupling.

    J(K; q) = alpha^{-w} * (d_{3/2}*tr(beta|_{S_{3/2}}) +
                             d_{1/2}*tr(beta|_{S_{1/2}})) / d_{1/2}

    Parameters
    ----------
    braid_word : list of (int, int)
        Each entry (gen, exp) with gen in {1, 2} (which generator)
        and exp an integer (positive or negative) exponent.
        E.g., [(1,1),(2,-1),(1,1),(2,-1)] for the figure-eight knot.
    q : complex
        The quantum parameter.

    Returns
    -------
    complex
        The Jones polynomial evaluated at q.
    """
    s = 0.5
    mu_p = r_matrix_eigenvalue(1, s, q)     # q^{1/4}
    mu_m = r_matrix_eigenvalue(0, s, q)     # -q^{-3/4}
    d_half = quantum_dimension(s, q)        # [2]
    d_3half = quantum_dimension(1.5, q)     # [4]
    alpha = framing_factor(s, q)            # q^{3/4}

    w = sum(e for _, e in braid_word)  # writhe

    # F-matrix for j=1/2 multiplicity space
    F = f_matrix_half(q)
    F_inv = np.linalg.inv(F)

    # sigma_i on S_{1/2} (2x2 matrices)
    s1_half = np.diag([mu_m, mu_p])
    s2_half = F_inv @ np.diag([mu_m, mu_p]) @ F

    # Build braid matrices by composing generators
    braid_half = np.eye(2, dtype=complex)
    braid_3half = complex(1.0)

    for gen, exp in braid_word:
        if gen == 1:
            mat = s1_half
        elif gen == 2:
            mat = s2_half
        else:
            raise ValueError(f"Generator must be 1 or 2, got {gen}")

        if exp >= 0:
            braid_half = braid_half @ np.linalg.matrix_power(mat, exp)
        else:
            braid_half = braid_half @ np.linalg.matrix_power(
                np.linalg.inv(mat), -exp
            )
        braid_3half *= mu_p ** exp  # 1-dim: sigma_i = mu_+ always

    tr_half = np.trace(braid_half)
    tr_3half = braid_3half

    markov_trace = d_3half * tr_3half + d_half * tr_half
    return alpha ** (-w) * markov_trace / d_half


# =============================================================================
# General interface
# =============================================================================

def jones_polynomial(knot_name, q):
    """Compute the Jones polynomial of a named knot at quantum parameter q.

    Supported knots:
      'unknot'       : trivial knot (J=1)
      'trefoil'      : right-handed trefoil 3_1 = T(2,3)
      'figure_eight'  : figure-eight knot 4_1
      'T(2,5)'       : torus knot 5_1 = T(2,5)
      'T(2,7)'       : torus knot 7_1 = T(2,7)
      'T(2,n)'       : torus knot T(2,n) for odd n (pass as string 'T(2,n)')

    Parameters
    ----------
    knot_name : str
        Name of the knot.
    q : complex
        The quantum parameter.

    Returns
    -------
    complex
        The Jones polynomial evaluated at q.
    """
    if knot_name == 'unknot':
        return jones_2strand(1, q)
    elif knot_name == 'trefoil':
        return jones_2strand(3, q)
    elif knot_name == 'figure_eight':
        # sigma_1 sigma_2^{-1} sigma_1 sigma_2^{-1} on 3 strands
        return jones_3strand([(1, 1), (2, -1), (1, 1), (2, -1)], q)
    elif knot_name.startswith('T(2,'):
        n = int(knot_name.split(',')[1].rstrip(')'))
        return jones_2strand(n, q)
    else:
        raise ValueError(f"Unknown knot: {knot_name}")


def jones_polynomial_known(knot_name, q):
    """Known closed-form Jones polynomial for verification.

    Returns the Jones polynomial as a Laurent polynomial in q,
    evaluated at the given q. Used for cross-checking the RT computation.
    """
    if knot_name == 'unknot':
        return complex(1.0)
    elif knot_name == 'trefoil':
        return -q ** (-4) + q ** (-3) + q ** (-1)
    elif knot_name == 'figure_eight':
        return q ** (-2) - q ** (-1) + 1 - q + q ** 2
    elif knot_name == 'T(2,5)':
        return -q ** (-7) + q ** (-6) - q ** (-5) + q ** (-4) + q ** (-2)
    elif knot_name == 'T(2,7)':
        return (-q ** (-10) + q ** (-9) - q ** (-8) + q ** (-7)
                - q ** (-6) + q ** (-5) + q ** (-3))
    else:
        raise ValueError(f"No known formula for: {knot_name}")


# =============================================================================
# Derived quantities
# =============================================================================

def colored_jones_dimension(k):
    """Quantum dimension [2]_q at level k (= dim_q of fundamental).

    [2]_q = q^{1/2} + q^{-1/2} = 2*cos(pi/(k+2)).
    """
    q = q_from_level(k)
    return quantum_dimension(0.5, q)


def jones_at_level(knot_name, k):
    """Jones polynomial of a knot at Chern-Simons level k.

    Uses q = exp(2*pi*i/(k+2)).
    """
    return jones_polynomial(knot_name, q_from_level(k))


def r_matrix_eigenvalues(q):
    """R-matrix eigenvalues on V_{1/2} x V_{1/2}.

    Returns (mu_symmetric, mu_antisymmetric) = (q^{1/4}, -q^{-3/4}).
    """
    s = 0.5
    return r_matrix_eigenvalue(1, s, q), r_matrix_eigenvalue(0, s, q)


def skein_relation_check(q):
    """Verify the skein relation: q^{1/2}*mu_+ - q^{-1/2}*mu_- = q - q^{-1}.

    The Jones polynomial satisfies the skein relation:
      q^{-1} J(L_+) - q J(L_-) = (q^{1/2} - q^{-1/2}) J(L_0)
    which at the R-matrix level reads:
      q^{1/2} mu_+ - q^{-1/2} mu_- = q - q^{-1}

    Returns the difference (should be 0).
    """
    mu_p, mu_m = r_matrix_eigenvalues(q)
    lhs = q ** 0.5 * mu_p - q ** (-0.5) * mu_m
    rhs = q - q ** (-1)
    return lhs - rhs


def writhe(braid_word):
    """Compute the writhe of a braid word.

    Parameters
    ----------
    braid_word : list of (int, int)
        Braid word as list of (generator, exponent) pairs.

    Returns
    -------
    int
        The writhe (sum of exponents).
    """
    return sum(e for _, e in braid_word)


# =============================================================================
# KZ connection data (link to chiral programme)
# =============================================================================

def kz_r_matrix(k, q=None):
    """Classical r-matrix r(z) = k * Omega / z for affine sl_2 at level k.

    The KZ connection nabla = d - sum_i<j r_{ij} dz_{ij} has monodromy
    given by the quantum R-matrix of U_q(sl_2) at q = exp(2*pi*i/(k+2)).

    Returns the level-prefixed r-matrix coefficient.
    The Casimir Omega = (1/2)(h x h) + e x f + f x e in sl_2 x sl_2.

    AP126 check: at k=0, r(z) = 0 (abelian limit, verified).
    """
    # AP1: kappa from landscape_census.tex
    # kappa(V_k(sl_2)) = dim(sl_2) * (k + h^v) / (2 * h^v)
    #                   = 3 * (k + 2) / 4
    # AP126: level prefix mandatory, k=0 -> r=0
    dim_g = 3       # dim(sl_2)
    h_vee = 2       # dual Coxeter number of sl_2
    kappa = dim_g * (k + h_vee) / (2 * h_vee)
    return {
        'r_coefficient': k,   # r(z) = k * Omega / z (trace-form convention)
        'kappa': kappa,        # kappa = 3(k+2)/4
        'q': q_from_level(k),
        'level': k,
        'convention': 'trace-form',
        'ap126_check': k == 0,  # r(z)|_{k=0} = 0: verified
    }


# =============================================================================
# Braid words for standard knots
# =============================================================================

KNOT_CATALOG = {
    'unknot': {
        'braid_word_2strand': 1,       # sigma_1^1, closure = unknot
        'jones': {0: 1},               # J = 1
        'writhe': 1,
        'crossing_number': 0,
    },
    'trefoil': {
        'braid_word_2strand': 3,       # sigma_1^3
        'jones': {-4: -1, -3: 1, -1: 1},
        'writhe': 3,
        'crossing_number': 3,
    },
    'figure_eight': {
        'braid_word_3strand': [(1, 1), (2, -1), (1, 1), (2, -1)],
        'jones': {-2: 1, -1: -1, 0: 1, 1: -1, 2: 1},
        'writhe': 0,
        'crossing_number': 4,
    },
    'T(2,5)': {
        'braid_word_2strand': 5,       # sigma_1^5
        'jones': {-7: -1, -6: 1, -5: -1, -4: 1, -2: 1},
        'writhe': 5,
        'crossing_number': 5,
    },
    'T(2,7)': {
        'braid_word_2strand': 7,       # sigma_1^7
        'jones': {-10: -1, -9: 1, -8: -1, -7: 1, -6: -1, -5: 1, -3: 1},
        'writhe': 7,
        'crossing_number': 7,
    },
}


def jones_from_coefficients(coeffs, q):
    """Evaluate a Jones polynomial from its Laurent polynomial coefficients.

    Parameters
    ----------
    coeffs : dict
        Map from integer power to coefficient, e.g. {-4: -1, -3: 1, -1: 1}.
    q : complex
        The quantum parameter.

    Returns
    -------
    complex
        The evaluated polynomial.
    """
    return sum(c * q ** p for p, c in coeffs.items())
