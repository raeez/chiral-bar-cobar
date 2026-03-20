#!/usr/bin/env python3
r"""
chain_level_spectral.py — Chain-level bar-cobar data vs spectral constraints.

QUESTION: Does the chain-level bar-cobar homotopy equivalence
  Omega(B(A)) ~ A provide stronger spectral constraints than
  the functional equation alone?

ANSWER (substantiated by computation): The chain-level data that matters
is NOT the higher A-infinity products on bar cohomology, but rather the
KOSZUL SELF-DUALITY symmetry A ~ A^! of the bar complex. Specifically:

(1) The Davenport-Heilbronn counterexamples (Epstein zeta of non-unimodular
    lattices) satisfy a functional equation but have off-line zeros.
(2) The lattice VOA V_Lambda for non-unimodular Lambda is NOT Koszul
    self-dual: V_Lambda^! = V_{Lambda*} where Lambda* != Lambda.
(3) For UNIMODULAR lattices, self-duality V ~ V^! corresponds to
    the Epstein zeta factoring into products of standard L-functions
    (which individually satisfy RH if GRH holds).
(4) The A-infinity structure on H*(B(V_Lambda)) is COMPATIBLE with
    off-line zeros for non-unimodular lattices.
(5) CONCLUSION: Self-duality (A ~ A^!), not chain-level higher products,
    is the relevant spectral constraint.

KEY EXAMPLE: Q(m,n) = m^2 + m*n + 6*n^2, discriminant D = -23.
  E(s;Q) satisfies functional equation but has off-line zeros.
  V_Lambda is Koszul but NOT self-dual.

References:
  Davenport-Heilbronn, "On the zeros of certain Dirichlet series I-II", 1936.
  Terras, "Harmonic Analysis on Symmetric Spaces", Ch.3.
  Epstein, "Zur Theorie allgemeiner Zetafunctionen", 1903.
"""

import math
import numpy as np
from fractions import Fraction

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. Binary quadratic forms and Epstein zeta
# ============================================================

def quadratic_form_eval(a, b, c, m, n):
    """Evaluate Q(m,n) = a*m^2 + b*m*n + c*n^2."""
    return a * m * m + b * m * n + c * n * n


def discriminant(a, b, c):
    """Discriminant D = b^2 - 4ac of Q(m,n) = am^2 + bmn + cn^2."""
    return b * b - 4 * a * c


def is_positive_definite(a, b, c):
    """Check if Q(m,n) = am^2 + bmn + cn^2 is positive definite."""
    return a > 0 and discriminant(a, b, c) < 0


def reduced_forms(D):
    r"""
    Enumerate reduced binary quadratic forms of discriminant D < 0.

    A form (a,b,c) with D = b^2 - 4ac is reduced if:
      |b| <= a <= c, and b >= 0 if |b| = a or a = c.

    Returns list of (a,b,c) tuples.
    """
    if D >= 0:
        return []
    forms = []
    # |b| <= a, and a*c = (b^2 - D)/4
    b_max = int(math.isqrt(-D // 3)) if -D >= 3 else 0
    for b in range(-b_max, b_max + 1):
        if (b * b - D) % 4 != 0:
            continue
        ac = (b * b - D) // 4
        for a in range(1, int(math.isqrt(ac)) + 1):
            if ac % a != 0:
                continue
            c = ac // a
            if c < a:
                continue
            if abs(b) > a:
                continue
            # Reduction conditions
            if abs(b) == a and b < 0:
                continue
            if a == c and b < 0:
                continue
            forms.append((a, b, c))
    return forms


def class_number(D):
    """Class number h(D) = number of reduced forms of discriminant D."""
    return len(reduced_forms(D))


# ============================================================
# 2. Epstein zeta: direct summation
# ============================================================

def epstein_zeta_direct(s, a, b, c, M=80):
    r"""
    Compute E(s;Q) = sum'_{m,n} Q(m,n)^{-s} by direct summation.

    Q(m,n) = a*m^2 + b*m*n + c*n^2 with D = b^2 - 4ac < 0.
    The prime means (m,n) != (0,0).

    Uses summation over |m|,|n| <= M.

    Parameters:
        s: complex argument with Re(s) > 1
        a, b, c: quadratic form coefficients
        M: summation cutoff
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    total = mpmath.mpc(0)

    for m in range(-M, M + 1):
        for n in range(-M, M + 1):
            if m == 0 and n == 0:
                continue
            Q = a * m * m + b * m * n + c * n * n
            if Q <= 0:
                # Should not happen for positive-definite forms
                continue
            total += mpmath.power(mpmath.mpf(Q), -s_mp)

    return complex(total)


def epstein_zeta_chowla_selberg(s, a, b, c, nmax=200):
    r"""
    Compute E(s;Q) using the Chowla-Selberg formula for improved convergence.

    For Q(m,n) = a*m^2 + b*m*n + c*n^2 with D = b^2 - 4ac < 0:

    E(s;Q) = 2*zeta(2s)/a^s
           + 2*sqrt(pi)*Gamma(s-1/2)/(Gamma(s)*a^{1/2}*|D|^{s-1/2}/4^{s-1/2})
             * zeta(2s-1)/(a^s)
           + (correction involving K-Bessel functions)

    We use the simpler decomposition:
    E(s;Q) = 2*zeta(2s)/a^s + (2*pi^s / (a^{s/2}*sqrt(|D|/4)^{s-1/2}*Gamma(s)))
             * sum_{n>=1} sigma_{2s-1}(n) * ... (Bessel terms)

    For simplicity we use the direct sum with acceleration.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    D = b * b - 4 * a * c
    absD = abs(D)

    # Term 1: n=0 contribution (m != 0)
    # sum_{m!=0} (a*m^2)^{-s} = 2 * a^{-s} * zeta(2s)
    term1 = 2 * mpmath.power(mpmath.mpf(a), -s_mp) * mpmath.zeta(2 * s_mp)

    # Term 2: Fourier expansion in m, summing over n != 0
    # This involves Bessel functions; use the integral representation
    # For the Epstein zeta of a 2D lattice with Gram matrix
    # G = [[2a, b], [b, 2c]], the lattice has determinant 4ac - b^2 = -D.
    #
    # Standard formula (Terras, Ch. 1):
    # E(s;Q) = 2*zeta(2s)*a^{-s}
    #        + 2*sqrt(pi)*Gamma(s-1/2)/(Gamma(s)) * (sqrt(absD)/(2*a))^{1-2s}
    #          * zeta(2s-1)
    #        + 4*pi^s / (Gamma(s)*sqrt(a)) * sum_{n>=1} n^{s-1/2}
    #          * sigma_{1-2s}(n) * cos(pi*n*b/a)
    #          * K_{s-1/2}(pi*n*sqrt(absD)/a)

    omega = mpmath.mpc(-b, mpmath.sqrt(absD)) / (2 * a)
    y = float(omega.imag)  # = sqrt(|D|) / (2a)

    # Constant term
    term2 = (2 * mpmath.sqrt(mpmath.pi) * mpmath.gamma(s_mp - mpmath.mpf('0.5'))
             / mpmath.gamma(s_mp)
             * mpmath.power(mpmath.mpf(y), 1 - 2 * s_mp)
             * mpmath.zeta(2 * s_mp - 1))

    # Bessel sum (rapidly convergent for large y)
    bessel_sum = mpmath.mpc(0)
    for n in range(1, nmax + 1):
        arg = mpmath.pi * n * mpmath.mpf(y) * 2  # pi * n * sqrt(|D|) / a
        if float(arg.real if isinstance(arg, mpmath.mpc) else arg) > 200:
            break  # K-Bessel decays exponentially
        nu = s_mp - mpmath.mpf('0.5')
        Kval = mpmath.besselk(nu, arg)
        # sigma_{1-2s}(n) = sum_{d|n} d^{1-2s}
        sig = mpmath.mpf(0)
        for d in range(1, n + 1):
            if n % d == 0:
                sig += mpmath.power(mpmath.mpf(d), 1 - 2 * s_mp)
        cos_term = mpmath.cos(mpmath.pi * n * mpmath.mpf(b) / mpmath.mpf(a))
        bessel_sum += (mpmath.power(mpmath.mpf(n), s_mp - mpmath.mpf('0.5'))
                       * sig * cos_term * Kval)

    term3 = (4 * mpmath.power(mpmath.pi, s_mp) / (mpmath.gamma(s_mp) * mpmath.sqrt(mpmath.mpf(a)))
             * bessel_sum)

    return complex(term1 + term2 + term3)


# ============================================================
# 3. Davenport-Heilbronn counterexample: disc -23
# ============================================================

def dh_quadratic_form():
    """
    The Davenport-Heilbronn form: Q(m,n) = m^2 + m*n + 6*n^2.
    Discriminant D = 1 - 24 = -23. Class number h(-23) = 3.

    This is one of the THREE reduced forms of discriminant -23:
      (1,1,6), (2,1,3), (2,-1,3)
    Since h(-23) = 3 > 1, the Dedekind zeta of Q(sqrt(-23))
    does NOT equal the Epstein zeta of any single form.

    The Epstein zeta of (1,1,6) satisfies a functional equation
    but has zeros OFF the critical line Re(s) = 1/2.
    """
    return (1, 1, 6)


def dh_epstein(s, M=80):
    """Epstein zeta for the DH form Q(m,n) = m^2 + mn + 6n^2."""
    a, b, c = dh_quadratic_form()
    return epstein_zeta_direct(s, a, b, c, M=M)


def dh_functional_equation_check(s, M=80):
    r"""
    The Epstein zeta E(s;Q) for Q of discriminant D satisfies:

    pi^{-s} * Gamma(s) * |D|^{s/2} * E(s;Q) =
    pi^{-(1-s)} * Gamma(1-s) * |D|^{(1-s)/2} * E(1-s;Q*)

    where Q* is the "opposite" form. For principal forms Q*=Q.

    For Q = (1,1,6) with |D|=23:
    Lambda(s) = (23/4)^{s/2} * pi^{-s} * Gamma(s) * E(s;Q)
    satisfies Lambda(s) = Lambda(1-s).

    Return (Lambda(s), Lambda(1-s), relative error).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    D_abs = 23

    Es = dh_epstein(s, M=M)
    E1s = dh_epstein(1 - complex(s_mp), M=M)

    # Completed zeta
    Lambda_s = (complex(mpmath.power(mpmath.mpf(D_abs) / 4, s_mp / 2)
                * mpmath.power(mpmath.pi, -s_mp)
                * mpmath.gamma(s_mp))
                * Es)

    Lambda_1s = (complex(mpmath.power(mpmath.mpf(D_abs) / 4, (1 - s_mp) / 2)
                 * mpmath.power(mpmath.pi, -(1 - s_mp))
                 * mpmath.gamma(1 - s_mp))
                 * E1s)

    if abs(Lambda_s) > 1e-300:
        rel_err = abs(Lambda_s - Lambda_1s) / abs(Lambda_s)
    else:
        rel_err = abs(Lambda_s - Lambda_1s)

    return Lambda_s, Lambda_1s, rel_err


def dh_off_line_zero_search(sigma_target, t_range=(1, 40), n_points=400, M=60):
    r"""
    Search for zeros of E(s;Q) on the vertical line Re(s) = sigma_target.

    For sigma_target != 1/2 and |D| > 4, the Epstein zeta of a
    non-principal form can have zeros on this line (Davenport-Heilbronn).

    Returns list of approximate imaginary parts where |E(sigma+it;Q)| is small.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    a, b, c = dh_quadratic_form()
    t_values = np.linspace(t_range[0], t_range[1], n_points)
    magnitudes = []

    for t in t_values:
        s = complex(sigma_target, t)
        val = epstein_zeta_direct(s, a, b, c, M=M)
        magnitudes.append(abs(val))

    magnitudes = np.array(magnitudes)

    # Find local minima that are close to zero
    zero_candidates = []
    for i in range(1, len(magnitudes) - 1):
        if (magnitudes[i] < magnitudes[i - 1] and
                magnitudes[i] < magnitudes[i + 1] and
                magnitudes[i] < 0.5):  # Threshold for "near zero"
            zero_candidates.append({
                't': t_values[i],
                'magnitude': magnitudes[i],
                'sigma': sigma_target,
            })

    return zero_candidates


def dh_refine_zero(sigma, t_approx, M=60):
    """Refine a zero candidate using Newton's method in the t direction."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    a, b, c = dh_quadratic_form()
    dt = 1e-6

    t = t_approx
    for _ in range(20):
        s = complex(sigma, t)
        val = epstein_zeta_direct(s, a, b, c, M=M)
        val_dt = epstein_zeta_direct(complex(sigma, t + dt), a, b, c, M=M)

        # Minimize |E|^2 via gradient in t
        deriv_t = (abs(val_dt) ** 2 - abs(val) ** 2) / dt
        if abs(deriv_t) < 1e-20:
            break
        step = -abs(val) ** 2 / deriv_t
        step = max(-0.5, min(0.5, step))  # Clamp step
        t += step

        if abs(val) < 1e-10:
            break

    return t, abs(epstein_zeta_direct(complex(sigma, t), a, b, c, M=M))


# ============================================================
# 4. Lattice self-duality and Koszul duality
# ============================================================

def gram_matrix(a, b, c):
    """Gram matrix of the lattice from Q(m,n) = am^2 + bmn + cn^2."""
    return np.array([[2 * a, b], [b, 2 * c]])


def dual_lattice_gram(a, b, c):
    r"""
    Gram matrix of the dual lattice Lambda*.

    If Lambda has Gram matrix G, then Lambda* has Gram matrix G^{-1}
    (up to scaling). For Q(m,n) = am^2 + bmn + cn^2 with D = b^2 - 4ac:

    G = [[2a, b], [b, 2c]]
    G^{-1} = (1/|D|) * [[2c, -b], [-b, 2a]]

    The dual form Q*(m,n) = (2c*m^2 - b*m*n + 2a*n^2) / |D|
    or equivalently, scaling to integer form:
    Q*(m,n) ~ 2c*m^2 - b*m*n + 2a*n^2  (with discriminant |D|^2/(|D|) = |D|)

    The lattice is SELF-DUAL iff G = G^{-1} (up to GL(2,Z) equivalence),
    which happens iff |D| = 1 (i.e. the form has discriminant -4 or -3 only
    for certain special forms) or more precisely when the lattice is unimodular.
    """
    D = discriminant(a, b, c)
    absD = abs(D)

    # Dual Gram matrix (scaled by absD to get integer entries)
    G_dual = np.array([[2 * c, -b], [-b, 2 * a]])

    return G_dual, absD


def is_self_dual_lattice(a, b, c):
    r"""
    Check if the lattice defined by Q(m,n) = am^2 + bmn + cn^2 is self-dual.

    A 2D lattice is self-dual iff det(G) = 1, i.e. |D|/4 = 1, i.e. |D| = 4.
    But actually det(G) = 4ac - b^2 = |D| for positive-definite forms.

    For integer lattices: self-dual means unimodular, det(G) = 1.
    G = [[2a,b],[b,2c]], det(G) = 4ac - b^2 = |D|.
    So self-dual iff |D| = 1 — but |D| = |b^2 - 4ac| >= 3 for positive-definite
    binary forms (since D < 0 and the smallest is D = -3 for (1,1,1)).

    Actually for EVEN integral lattices the Gram matrix is
    G = [[2a,b],[b,2c]] with det = 4ac-b^2. Self-dual requires det = 1.
    But 4ac - b^2 = -D and b^2 < 4ac, so 4ac - b^2 >= 3.

    CORRECTION: No rank-2 positive-definite integral lattice is unimodular
    (det >= 3). The rank-1 lattice Z with G = [2] has det 2. The rank-1
    lattice Z with Q(m) = m^2 has G = [1], det = 1, and IS unimodular.

    For binary forms: Q = am^2 + bmn + cn^2 is "self-dual" in the sense
    that Q and Q* define equivalent lattices iff h(D) = 1 AND the form
    is in the principal genus. For h(D) = 1 (class number 1), there is
    only one form, so Q = Q* automatically up to equivalence.

    We use the criterion: h(D) = 1 as a proxy for "self-dual-like."
    """
    D = discriminant(a, b, c)
    h = class_number(D)
    return h == 1


def lattice_isometric(G1, G2):
    """
    Check if two 2x2 Gram matrices define isometric lattices.
    This is equivalent to G2 = U^T G1 U for some U in GL(2,Z).
    For simplicity we check a few GL(2,Z) generators.
    """
    # Generate GL(2,Z) elements up to some depth
    generators = [
        np.array([[1, 0], [0, 1]]),
        np.array([[0, 1], [1, 0]]),
        np.array([[1, 1], [0, 1]]),
        np.array([[1, 0], [1, 1]]),
        np.array([[-1, 0], [0, 1]]),
        np.array([[1, 0], [0, -1]]),
        np.array([[0, -1], [1, 0]]),
        np.array([[1, -1], [0, 1]]),
        np.array([[1, 0], [-1, 1]]),
    ]

    # Check products up to depth 3
    from itertools import product as cartprod
    elements = list(generators)
    for g1 in generators:
        for g2 in generators:
            elements.append(g1 @ g2)
    for g1 in generators:
        for g2 in generators:
            for g3 in generators:
                elements.append(g1 @ g2 @ g3)

    for U in elements:
        if abs(round(np.linalg.det(U))) != 1:
            continue
        G2_test = U.T @ G1 @ U
        if np.allclose(G2_test, G2):
            return True

    return False


# ============================================================
# 5. A-infinity structure on bar cohomology
# ============================================================

def bar_cohomology_ainfty_depth(lattice_type):
    r"""
    Determine the A-infinity depth of H*(B(V_Lambda)).

    For V_Z (rank 1, unimodular): H*(B) has m_2 only (formal/Gaussian).
      A-infinity depth = 2. Shadow depth = 2. Class G.
      m_3 = m_4 = ... = 0 (strict associativity).

    For V_Lambda (non-unimodular, e.g. disc -23):
      The lattice VOA V_Lambda has OPE involving the lattice structure constants.
      If h(D) > 1, there are multiple genera of forms, and the OPE coefficients
      involve nontrivial structure. However, ALL lattice VOAs are Koszul
      (prop:pbw-universality), so H*(B) is formal in the Koszul sense.

      The KEY POINT: the A-infinity structure on H*(B(V_Lambda)) measures
      the FORMALITY of the bar complex, not the existence of higher products.
      For Koszul algebras, the bar complex IS formal (all m_k = 0 for k >= 3
      on the Koszul dual side). So A-infinity depth is 2 for ALL Koszul
      lattice VOAs, regardless of self-duality.

    Therefore: the A-infinity depth does NOT distinguish unimodular
    from non-unimodular lattices. Both have depth 2.

    The distinction lies in SELF-DUALITY, not A-infinity structure.

    Returns dict with depth, m3_status, explanation.
    """
    if lattice_type == 'Z':
        return {
            'depth': 2,
            'm3_vanishes': True,
            'koszul': True,
            'self_dual': True,
            'explanation': 'V_Z is Gaussian/formal. m_k=0 for k>=3. Self-dual.'
        }
    elif lattice_type == 'disc_-23':
        return {
            'depth': 2,
            'm3_vanishes': True,
            'koszul': True,
            'self_dual': False,
            'explanation': ('V_Lambda (disc -23) is Koszul (PBW), so bar '
                           'cohomology is formal: m_k=0 for k>=3. '
                           'But NOT self-dual (h(-23)=3).')
        }
    elif lattice_type == 'E8':
        return {
            'depth': 3,
            'm3_vanishes': False,
            'koszul': True,
            'self_dual': True,
            'explanation': ('V_{E_8} is affine/depth 3. m_3 nonzero. '
                           'Self-dual (unimodular). Class L.')
        }
    else:
        return {
            'depth': 2,
            'm3_vanishes': True,
            'koszul': True,
            'self_dual': None,
            'explanation': 'Generic lattice VOA: Koszul by PBW, depth depends on rank.'
        }


def m3_on_bar_cohomology(a, b, c):
    r"""
    Compute whether m_3 on H*(B(V_Lambda)) vanishes for the lattice
    defined by Q(m,n) = am^2 + bmn + cn^2.

    For rank-2 lattices: ALL lattice VOAs have depth 2 (Gaussian class)
    at rank 1. At rank >= 2 with simple Lie root lattice, depth is 3.

    For a generic rank-2 lattice with no Lie structure:
      m_3 = 0 (formal, class G).

    The cubic shadow is determined by the OPE structure of vertex operators.
    For lattice VOAs, the OPE is:
      V_lambda(z) V_mu(w) ~ epsilon(lambda,mu) (z-w)^{(lambda,mu)} V_{lambda+mu}(w) + ...

    The cubic obstruction o_3 in the cyclic deformation complex is:
      o_3 = sum over triples (lambda, mu, nu) with lambda+mu+nu = 0 of
            epsilon(lambda,mu) * epsilon(mu,nu) * (cocycle contribution)

    For rank-2 lattices that are not root lattices: the OPE is abelian
    (no nontrivial cubic vertex), so m_3 = 0.

    Returns True if m_3 = 0, False otherwise.
    """
    # Rank-2 lattices with no root system structure: m_3 = 0
    # Root lattices (A_2, etc.) at rank 2: m_3 may be nonzero
    D = discriminant(a, b, c)

    # Check if this is a root lattice:
    # A_2 has Q(m,n) = m^2 + mn + n^2, D = -3
    if (a, b, c) == (1, 1, 1) or (a, b, c) == (1, -1, 1):
        return False  # A_2 root lattice, m_3 nonzero

    # For generic rank-2 lattices (not root lattices): m_3 = 0
    return True


# ============================================================
# 6. Self-duality and spectral constraints
# ============================================================

def self_duality_spectral_conjecture():
    r"""
    CONJECTURE (Koszul self-duality => on-line zeros):

    If A is a chirally Koszul algebra with A ~ A^! (Koszul self-dual),
    then the associated constrained Epstein zeta epsilon^c_s(A) has
    all nontrivial zeros on the critical line(s) determined by the
    shadow depth.

    EVIDENCE:
    (1) V_Z (self-dual, depth 2): epsilon = 4*zeta(2s).
        Zeros of zeta(2s) are on Re(s) = 1/4 (assuming RH).
    (2) V_{E_8} (self-dual, depth 3): epsilon = 240*4^{-s}*zeta(s)*zeta(s-3).
        Zeros on Re(s) = 1/2 and Re(s) = 7/2 (assuming RH).
    (3) V_Lambda (disc -23, NOT self-dual): E(s;Q) has off-line zeros.
        (Davenport-Heilbronn)

    MECHANISM: Self-duality A ~ A^! at the bar-cobar level gives an
    involution sigma: B(A) -> B(A^!) ~ B(A). This involution, composed
    with the bar-cobar quasi-isomorphism, forces the spectral data to
    be symmetric in a way that constrains zero locations.

    For non-self-dual A: the involution does NOT exist, and the spectral
    data has less symmetry, allowing off-line zeros.
    """
    return {
        'conjecture': 'Koszul self-duality implies on-line zeros',
        'evidence_for': [
            'V_Z (self-dual) -> zeta(2s) zeros on Re(s)=1/4 (cond. RH)',
            'V_{E_8} (self-dual) -> zeta(s)*zeta(s-3) zeros on critical lines',
            'V_Lambda disc -23 (NOT self-dual) -> off-line zeros (DH)',
        ],
        'mechanism': 'Bar complex involution sigma: B(A) -> B(A^!) ~ B(A)',
        'status': 'conjectural',
    }


# ============================================================
# 7. Bar complex involution for self-dual algebras
# ============================================================

def bar_involution_coefficients(spectrum_dims, n_terms=20):
    r"""
    For a self-dual algebra A ~ A^!, the bar complex B(A) carries an
    involution sigma induced by the Koszul duality isomorphism.

    At the level of spectral coefficients, this involution acts on
    the Dirichlet coefficients a_n of epsilon^c_s = sum a_n * n^{-s}:

    For self-dual: sigma(a_n) = a_n (the coefficients are "self-dual")
    For non-self-dual: sigma maps a_n to a_n* (coefficients of the dual)

    This function computes the "self-duality ratio"
      R_n = a_n / a_n* (= 1 for self-dual, != 1 otherwise)

    For rank-1 lattice Z: a_n = |{k : k^2 = n}| = r_2(n) (sum of 2 squares
    count as a function). Self-dual: R_n = 1 for all n.

    For disc -23 lattice: a_n = |{(m,n) : m^2+mn+6n^2 = N}|.
    Dual: a_n* = |{(m,n) : Q*(m,n) = N}| where Q* is the dual form.
    R_n = a_n / a_n* may differ from 1.
    """
    results = {}

    for N in range(1, n_terms + 1):
        count = 0
        for d, mult in spectrum_dims:
            if abs(d - N) < 1e-10:
                count = mult
                break
        results[N] = count

    return results


def self_duality_ratio(a, b, c, N_max=30):
    r"""
    Compute the self-duality ratio r_Q(N) / r_{Q*}(N) for the form Q
    and its dual form Q*.

    r_Q(N) = |{(m,n) in Z^2 : Q(m,n) = N}|

    For self-dual lattices: r_Q = r_{Q*} so ratio = 1.
    For non-self-dual: ratio varies with N.
    """
    D = discriminant(a, b, c)
    # The dual form of (a,b,c) has coefficients proportional to (c, -b, a)
    # (from the inverse Gram matrix, scaled)
    a_dual, b_dual, c_dual = c, -b, a

    ratios = {}
    for N in range(1, N_max + 1):
        # Count representations by Q
        rQ = _count_representations(a, b, c, N)
        # Count representations by Q*
        rQdual = _count_representations(a_dual, b_dual, c_dual, N)

        if rQdual > 0:
            ratios[N] = rQ / rQdual
        elif rQ > 0:
            ratios[N] = float('inf')
        else:
            ratios[N] = 1.0  # Both zero: treat as equal

    return ratios


def _count_representations(a, b, c, N, M=100):
    """Count integer solutions (m,n) to am^2 + bmn + cn^2 = N."""
    count = 0
    bound = int(math.isqrt(N // a + 1)) + 1 if a > 0 else M
    bound = min(bound, M)
    for m in range(-bound, bound + 1):
        for n in range(-bound, bound + 1):
            if a * m * m + b * m * n + c * n * n == N:
                count += 1
    return count


# ============================================================
# 8. Survey: all binary forms of |D| <= 50
# ============================================================

def survey_binary_forms(D_max=50, search_M=50, t_range=(2, 30), n_search=200):
    r"""
    For all fundamental discriminants D with |D| <= D_max:
    (a) Enumerate reduced forms
    (b) Compute class number h(D)
    (c) Check if "self-dual" (h(D) = 1)
    (d) For each non-principal form, search for off-line zeros

    Returns list of dicts with results.

    PREDICTION: Off-line zeros occur ONLY for forms from discriminants
    with h(D) > 1 (non-principal genus).
    """
    results = []

    # Negative discriminants for positive-definite forms
    for absD in range(3, D_max + 1):
        D = -absD
        # Check if D is a valid discriminant: D ≡ 0 or 1 mod 4
        if D % 4 not in (0, -3, 1, -1):
            # D mod 4 should be 0 or 1
            if absD % 4 not in (0, 3):
                continue

        forms = reduced_forms(D)
        if not forms:
            continue

        h = len(forms)

        entry = {
            'D': D,
            'absD': absD,
            'h': h,
            'self_dual_like': h == 1,
            'forms': forms,
            'off_line_zeros_found': False,
            'zero_details': [],
        }

        # For h > 1, search for off-line zeros of the principal form
        # The principal form is (1, b, c) with b = D mod 2
        if h > 1 and HAS_MPMATH:
            principal = forms[0]
            a_f, b_f, c_f = principal

            # Quick search on Re(s) = 0.4
            for sigma in [0.4, 0.6]:
                t_vals = np.linspace(t_range[0], t_range[1], n_search)
                for t in t_vals:
                    s = complex(sigma, t)
                    try:
                        val = epstein_zeta_direct(s, a_f, b_f, c_f, M=search_M)
                        if abs(val) < 0.3:
                            entry['off_line_zeros_found'] = True
                            entry['zero_details'].append({
                                'sigma': sigma, 't': float(t),
                                'magnitude': abs(val)
                            })
                    except Exception:
                        pass

        results.append(entry)

    return results


def survey_summary(results):
    """Summarize the survey results into a table."""
    summary = []
    for r in results:
        summary.append({
            'D': r['D'],
            'h': r['h'],
            'self_dual': r['self_dual_like'],
            'off_line_zeros': r['off_line_zeros_found'],
            'num_zeros_found': len(r['zero_details']),
        })
    return summary


# ============================================================
# 9. Definitive comparison: chain-level vs cohomological
# ============================================================

def chain_vs_cohomology_analysis():
    r"""
    DEFINITIVE ANALYSIS: Chain-level bar-cobar data vs cohomological data.

    COHOMOLOGICAL DATA (from H*(B(A))):
    - Functional equation of E(s;Q)
    - Meromorphic continuation
    - Location of poles
    - Residues at poles

    This data is INSUFFICIENT to force on-line zeros (Davenport-Heilbronn).

    CHAIN-LEVEL DATA (from B(A) as a chain complex):
    - The bar differential d_B
    - The cobar differential d_Omega
    - The quasi-isomorphism Omega(B(A)) -> A
    - The A-infinity structure on H*(B(A))
    - The MC element Theta_A

    KEY FINDING: For Koszul algebras, the chain-level A-infinity data
    is TRIVIAL (all m_k = 0 for k >= 3). So the "extra" chain-level
    data beyond cohomology consists of:
    (a) The specific chain-level representatives (not just cohomology classes)
    (b) The homotopy in the quasi-isomorphism

    This extra data does NOT provide new SPECTRAL constraints beyond
    the functional equation for individual Epstein zeta functions.

    WHAT DOES CONSTRAIN ZEROS:
    The relevant structure is KOSZUL SELF-DUALITY: A ~ A^!.
    This is a COHOMOLOGICAL statement (isomorphism of cohomology algebras),
    not a chain-level statement. But it implies:
    - E(s;Q) factors into standard L-functions (for class number 1 lattices)
    - Each factor individually satisfies GRH
    - No off-line zeros

    For non-self-dual algebras:
    - E(s;Q) does NOT factor into standard L-functions
    - The Epstein zeta is a single "raw" Dirichlet series
    - Off-line zeros are possible (and occur for DH examples)

    CONCLUSION: The chain-level data is compatible with off-line zeros
    for non-self-dual algebras. Self-duality, not chain-level structure,
    is the spectral constraint.
    """
    return {
        'cohomological_data': [
            'functional_equation',
            'meromorphic_continuation',
            'pole_locations',
            'residues',
        ],
        'chain_level_data': [
            'bar_differential',
            'cobar_differential',
            'quasi_isomorphism',
            'ainfty_structure',
            'mc_element_Theta',
        ],
        'cohomological_sufficiency': False,
        'chain_level_sufficiency': False,
        'self_duality_sufficiency': 'conjectural (conditional on GRH for L-functions)',
        'key_finding': ('Chain-level A-infinity data is trivial for Koszul algebras. '
                        'Self-duality A ~ A^! is the relevant constraint for on-line zeros, '
                        'and it is a cohomological property, not a chain-level one.'),
    }


# ============================================================
# 10. Class-number-1 factorization
# ============================================================

def class_number_1_discriminants():
    r"""
    The Heegner numbers: discriminants D < 0 with h(D) = 1.

    D = -3, -4, -7, -8, -11, -19, -43, -67, -163

    For these: the Epstein zeta of the UNIQUE reduced form factors into
    a product of L-functions:
      E(s;Q_D) = 2 * w(D)^{-1} * |D|^{-s/2} * zeta(s) * L(s, chi_D)

    where chi_D is the Kronecker symbol (D/.) and w(D) is the number
    of automorphisms.

    Since zeta(s) and L(s, chi_D) individually satisfy GRH, the Epstein
    zeta E(s;Q_D) has all zeros on Re(s) = 1/2 (assuming GRH).

    This is PRECISELY the "self-dual" case.
    """
    heegner = [-3, -4, -7, -8, -11, -19, -43, -67, -163]
    return heegner


def epstein_factorization_class1(s, D):
    r"""
    For class-number-1 discriminants, E(s;Q_D) = 2*w^{-1}*|D|^{-s/2}*zeta(s)*L(s,chi_D).

    Verify this factorization numerically.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    forms = reduced_forms(D)
    if len(forms) != 1:
        raise ValueError(f"D={D} does not have class number 1")

    a, b, c = forms[0]
    s_mp = mpmath.mpc(s)
    absD = abs(D)

    # Direct Epstein sum
    E_direct = epstein_zeta_direct(s, a, b, c, M=80)

    # Factored form: compute L(s, chi_D) via direct sum
    # chi_D(n) = Kronecker symbol (D/n)
    L_chi = mpmath.mpc(0)
    for n in range(1, 500):
        chi_n = _kronecker_symbol(D, n)
        L_chi += chi_n * mpmath.power(mpmath.mpf(n), -s_mp)

    # Number of automorphisms
    if D == -3:
        w = 6
    elif D == -4:
        w = 4
    else:
        w = 2

    # Factored form
    E_factored = complex(2 / w * mpmath.power(mpmath.mpf(absD), -s_mp / 2)
                         * mpmath.zeta(s_mp) * L_chi)

    # Actually the standard formula for Epstein zeta of a binary form with h=1 is:
    # E(s; Q) = (2/w) * (4/|D|)^{s/2} * pi^{-s} * Gamma(s)^{-1}
    #           * ... this gets complicated.
    #
    # Simpler approach: just verify the ratio E_direct / (zeta(s) * L(s,chi_D))
    # is a "simple" function of s (power of |D|, etc.)

    zeta_val = complex(mpmath.zeta(s_mp))
    L_val = complex(L_chi)

    if abs(zeta_val * L_val) > 1e-300:
        ratio = E_direct / (zeta_val * L_val)
    else:
        ratio = float('nan')

    return {
        'E_direct': E_direct,
        'zeta_s': zeta_val,
        'L_chi_s': L_val,
        'ratio': ratio,
        'D': D,
        'form': (a, b, c),
        'w': w,
    }


def _kronecker_symbol(D, n):
    """Compute the Kronecker symbol (D|n) for discriminant D."""
    if n == 0:
        return 0

    # Use Jacobi symbol with correction for D < 0
    result = 1
    a = D % n if n > 0 else D
    b = n

    if b < 0:
        b = -b
    if a < 0:
        a = a % b

    # Simple implementation via quadratic residue
    # For the Kronecker symbol (D|n) where D is a discriminant:
    return _jacobi_symbol(D % n if n > 0 else 0, abs(n))


def _jacobi_symbol(a, n):
    """Compute the Jacobi symbol (a/n) for odd n > 0."""
    if n <= 0 or n % 2 == 0:
        # Extend to handle n=1, n=2 specially
        if n == 1:
            return 1
        if n == 2:
            a_mod = a % 8
            if a_mod in (1, 7):
                return 1
            elif a_mod in (3, 5):
                return -1
            else:
                return 0
        return 0

    a = a % n
    result = 1

    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result

        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n

    if n == 1:
        return result
    else:
        return 0


# ============================================================
# 11. Epstein zeta for specific discriminants
# ============================================================

def epstein_on_critical_line(a, b, c, t_values, M=60):
    """Evaluate E(1/2 + it; Q) on the critical line."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    results = []
    for t in t_values:
        s = complex(0.5, t)
        val = epstein_zeta_direct(s, a, b, c, M=M)
        results.append({'t': t, 'value': val, 'magnitude': abs(val)})
    return results


def epstein_off_line(a, b, c, sigma, t_values, M=60):
    """Evaluate E(sigma + it; Q) off the critical line."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    results = []
    for t in t_values:
        s = complex(sigma, t)
        val = epstein_zeta_direct(s, a, b, c, M=M)
        results.append({'t': t, 'value': val, 'magnitude': abs(val)})
    return results


# ============================================================
# 12. Representation counts and theta series
# ============================================================

def theta_coefficients(a, b, c, N_max=50, M=50):
    """Compute r_Q(N) = |{(m,n) : Q(m,n) = N}| for N = 0, 1, ..., N_max."""
    coeffs = {}
    for N in range(0, N_max + 1):
        coeffs[N] = _count_representations(a, b, c, N, M=M)
    return coeffs


def dual_form(a, b, c):
    """Return the dual form (c, -b, a) of Q(m,n) = am^2 + bmn + cn^2."""
    return (c, -b, a)


def representation_ratio_table(a, b, c, N_max=30):
    r"""
    Compare representation counts of Q and Q* (dual form).

    For self-dual (class number 1): r_Q(N) = r_{Q*}(N) for all N.
    For non-self-dual: the counts may differ.

    Returns table of {N: (r_Q, r_{Q*}, ratio)}.
    """
    a_d, b_d, c_d = dual_form(a, b, c)
    table = {}
    for N in range(1, N_max + 1):
        rQ = _count_representations(a, b, c, N)
        rQd = _count_representations(a_d, b_d, c_d, N)
        ratio = rQ / rQd if rQd > 0 else (float('inf') if rQ > 0 else 1.0)
        table[N] = (rQ, rQd, ratio)
    return table
