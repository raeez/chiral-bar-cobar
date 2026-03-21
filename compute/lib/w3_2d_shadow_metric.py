r"""W_3 2D shadow metric: the full quadratic form Q(t,w) on the (T,W) primary plane.

NEW COMPUTATION.  The existing modules compute the W_3 shadow tower on the
T-line (x_W=0) and W-line (x_T=0) separately, or compute the full 2D tower
but do not extract the shadow metric.  This module computes the FULL
2-DIMENSIONAL shadow metric Q(t,w) — the quadratic form on the 2D primary
deformation space — including the off-diagonal mixing channel, the spectral
decomposition, the 2D discriminant surface, and the connection to the
propagator variance theorem.

THE 2D SHADOW METRIC:

On a 1D primary line L, the shadow metric is
    Q_L(t) = (2kappa + alpha*t)^2 + 2*kappa*Delta*t^2

where kappa is the modular characteristic, alpha is the cubic coefficient,
and Delta = 8*kappa*S_4 is the critical discriminant.

For a 2D primary plane with coordinates (t, w) corresponding to the T and W
generators, the shadow metric generalizes to a QUADRATIC FORM:

    Q(t,w) = Q_TT * t^2 + 2 * Q_TW * t * w + Q_WW * w^2

where the 2x2 matrix

    M(t,w) = [[Q_TT, Q_TW],
              [Q_TW, Q_WW]]

encodes the second variation of the shadow potential S along the primary plane.

COMPONENTS OF THE 2D SHADOW METRIC:

Each entry is itself a function of the deformation parameters (t,w) through
the shadow tower.  The quadratic form is extracted from the generating
function:

    G(t, w; x_T, x_W) = sum_{r>=2} Sh_r(t*x_T, w*x_W)

and the shadow metric is the Hessian in (x_T, x_W) at (x_T, x_W) = (t, w):

    M_{ij}(t, w) = d^2 G / d(x_i) d(x_j) evaluated at (x_T, x_W) = (t, w).

More precisely, on the 1D primary line parametrized by x, the shadow GF is
    H(x) = sum_{r>=2} S_r x^r
and the shadow metric is Q(t) = H''(t) * (propagator normalization).

For the 2D case, the generating function is
    H(x_T, x_W) = sum_{r>=2} Sh_r(x_T, x_W)
and the shadow metric MATRIX is the Hessian:
    M_{ij} = d^2 H / d(x_i) d(x_j)

This gives:
    M_TT(x_T, x_W) = sum_{r>=2} d^2/d(x_T)^2 Sh_r(x_T, x_W)
    M_TW(x_T, x_W) = sum_{r>=2} d^2/(d(x_T) d(x_W)) Sh_r(x_T, x_W)
    M_WW(x_T, x_W) = sum_{r>=2} d^2/d(x_W)^2 Sh_r(x_T, x_W)

DISCRIMINANT SURFACE:
    det(M) = M_TT * M_WW - M_TW^2 = 0

defines the SPECTRAL CURVE of the 2D shadow metric in (t, w, c)-space.
The shadow tower terminates iff det(M) = 0 identically (perfect square case).

PROPAGATOR VARIANCE:
    delta_mix = Tr(P * Q) - Tr(P)^{-1} * (Tr(Q))^2 / dim

where P = H^{-1} is the propagator.  The propagator variance measures the
non-autonomy of the diagonal restriction and is computable from arity 2+4.

References:
    w3_full_2d_shadow_tower.py: full 2D tower computation
    w3_multivariable_shadow.py: quartic input data (Lambda-exchange)
    w3_wline_shadow_tower.py: W-line 1D projection
    virasoro_shadow_tower.py: T-line 1D projection
    shadow_connection.py: 1D shadow metric and connection
    propagator_variance.py: propagator variance theorem
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from sympy import (
    Matrix, Poly, Rational, S, Symbol, cancel, collect, diff,
    expand, factor, numer, denom, simplify, sqrt, symbols,
)

c = Symbol('c')
x_T = Symbol('x_T')
x_W = Symbol('x_W')


# =============================================================================
# 1.  Hessian and propagator (curvature matrix)
# =============================================================================

def w3_hessian():
    """The 2x2 curvature (Hessian) matrix H = diag(c/2, c/3).

    H_TT = kappa_T = c/2  (from T_{(3)}T = (c/2) 1)
    H_WW = kappa_W = c/3  (from W_{(5)}W = (c/3) * 5! normalization)
    H_TW = 0               (T and W have different conformal weight parity)

    Total kappa: Tr(H) = c/2 + c/3 = 5c/6.
    """
    return Matrix([
        [c / 2, S.Zero],
        [S.Zero, c / 3],
    ])


def w3_propagator():
    """The 2x2 propagator P = H^{-1} = diag(2/c, 3/c).

    P_TT = 1/kappa_T = 2/c
    P_WW = 1/kappa_W = 3/c
    P_TW = 0
    """
    return Matrix([
        [Rational(2) / c, S.Zero],
        [S.Zero, Rational(3) / c],
    ])


def w3_total_kappa():
    """Total modular characteristic kappa(W_3) = Tr(H) = 5c/6."""
    H = w3_hessian()
    return cancel(H.trace())


# =============================================================================
# 2.  Cubic shadow tensor
# =============================================================================

def w3_cubic_tensor():
    """The cubic shadow tensor C_{ijk} for W_3.

    Sh_3 = 2 x_T^3 + 3 x_T x_W^2

    In tensor notation:
        C_TTT = 2   (from T_{(1)}T = 2T, gravitational cubic)
        C_TWW = 3   (from T_{(1)}W = 3W, weight d_W = 3)
        C_TTW = 0   (by Z_2 parity: W -> -W forces odd x_W count)
        C_WWW = 0   (by Z_2 parity: W -> -W forces odd x_W count)

    The coefficient 3 for C_TWW comes from the gravitational cubic
    C_{T,WW} = d_W = h_W = 3 (weight of W).
    """
    return {
        'TTT': Rational(2),
        'TTW': S.Zero,
        'TWW': Rational(3),
        'WWW': S.Zero,
    }


def w3_cubic_polynomial():
    """The cubic shadow Sh_3 = 2 x_T^3 + 3 x_T x_W^2."""
    return 2 * x_T**3 + 3 * x_T * x_W**2


# =============================================================================
# 3.  Quartic shadow tensor (from Lambda-exchange)
# =============================================================================

def w3_quartic_tensor():
    """The quartic shadow tensor Q_{ijkl} for W_3.

    From Lambda-exchange (the unique weight-4 quasi-primary):
        Q_TTTT = 10/[c(5c+22)]          (Virasoro quartic)
        Q_TTWW = 160/[c(5c+22)^2]       (mixed T-W channel)
        Q_WWWW = 2560/[c(5c+22)^3]      (pure W channel)

    Geometric progression: Q_TTTT : Q_TTWW : Q_WWWW = 1 : alpha : alpha^2
    where alpha = 16/(5c+22) is the Lambda coupling in the WW OPE.

    The quartic shadow polynomial:
        Sh_4 = Q_TTTT x_T^4 + 6 Q_TTWW x_T^2 x_W^2 + Q_WWWW x_W^4

    The factor 6 = C(4,2) is the multinomial coefficient.
    """
    alpha = Rational(16) / (5 * c + 22)
    Q0 = Rational(10) / (c * (5 * c + 22))

    Q_TTTT = Q0
    Q_TTWW = Q0 * alpha
    Q_WWWW = Q0 * alpha**2

    return {
        'Q_TTTT': cancel(Q_TTTT),
        'Q_TTWW': cancel(Q_TTWW),
        'Q_WWWW': cancel(Q_WWWW),
        'alpha': alpha,
    }


def w3_quartic_polynomial():
    """The quartic shadow Sh_4 as a polynomial in (x_T, x_W)."""
    qt = w3_quartic_tensor()
    return expand(
        qt['Q_TTTT'] * x_T**4
        + 6 * qt['Q_TTWW'] * x_T**2 * x_W**2
        + qt['Q_WWWW'] * x_W**4
    )


# =============================================================================
# 4.  2D H-Poisson bracket and shadow tower recursion
# =============================================================================

def h_poisson_2d(f, g):
    """2D H-Poisson bracket: {f, g}_H = sum_ij (df/dx_i) P^{ij} (dg/dx_j).

    For W_3 with diagonal P = diag(2/c, 3/c):
        {f, g}_H = (df/dx_T)(2/c)(dg/dx_T) + (df/dx_W)(3/c)(dg/dx_W)
    """
    P = w3_propagator()
    return expand(
        diff(f, x_T) * P[0, 0] * diff(g, x_T)
        + diff(f, x_W) * P[1, 1] * diff(g, x_W)
    )


def compute_2d_tower(max_arity: int = 10) -> Dict[int, object]:
    """Compute the full 2D W_3 shadow tower through max_arity.

    Input seeds: Sh_2, Sh_3, Sh_4 from OPE data.
    Higher arities: MC recursion nabla_H(Sh_r) + o^(r) = 0
    where o^(r) = sum_{j+k=r+2, 2<=j<=k} {Sh_j, Sh_k}_H
    and nabla_H(Sh_r) = 2r * Sh_r for homogeneous Sh_r of degree r.

    Returns dict {r: Sh_r(x_T, x_W)}.
    """
    H = w3_hessian()

    shadows = {}
    shadows[2] = H[0, 0] * x_T**2 + H[1, 1] * x_W**2
    shadows[3] = w3_cubic_polynomial()
    shadows[4] = w3_quartic_polynomial()

    for r in range(5, max_arity + 1):
        obstruction = S.Zero

        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2 or k not in shadows:
                continue
            if j > k:
                continue

            bracket = h_poisson_2d(shadows[j], shadows[k])

            if j == k:
                obstruction += Rational(1, 2) * bracket
            else:
                obstruction += bracket

        obstruction = expand(obstruction)

        if obstruction == S.Zero:
            shadows[r] = S.Zero
        else:
            Sh_r = cancel(-obstruction / (2 * r))
            shadows[r] = expand(Sh_r)

    return shadows


# =============================================================================
# 5.  Shadow generating function and Hessian (the 2D shadow metric)
# =============================================================================

def shadow_generating_function(max_arity: int = 8) -> object:
    """The shadow generating function H(x_T, x_W) = sum_{r>=2} Sh_r(x_T, x_W).

    This is a formal power series in (x_T, x_W) truncated at max_arity.
    """
    shadows = compute_2d_tower(max_arity)
    return sum(shadows[r] for r in range(2, max_arity + 1))


def shadow_metric_matrix(max_arity: int = 8) -> Matrix:
    """The 2x2 shadow metric matrix M(x_T, x_W).

    M_{ij} = d^2 H / d(x_i) d(x_j)

    where H is the shadow generating function.

    Returns a 2x2 sympy Matrix with entries depending on (c, x_T, x_W).
    """
    H_gf = shadow_generating_function(max_arity)

    M_TT = expand(diff(H_gf, x_T, x_T))
    M_TW = expand(diff(H_gf, x_T, x_W))
    M_WW = expand(diff(H_gf, x_W, x_W))

    return Matrix([
        [M_TT, M_TW],
        [M_TW, M_WW],
    ])


def shadow_metric_contributions(max_arity: int = 8) -> Dict[int, Matrix]:
    """The arity-by-arity contributions to the shadow metric matrix.

    For each arity r, returns the 2x2 matrix of second derivatives
    of Sh_r.  This decomposes the shadow metric into its arity layers.
    """
    shadows = compute_2d_tower(max_arity)
    contributions = {}

    for r in range(2, max_arity + 1):
        Sh_r = shadows[r]
        if Sh_r == S.Zero:
            contributions[r] = Matrix([[S.Zero, S.Zero], [S.Zero, S.Zero]])
        else:
            M_TT = expand(diff(Sh_r, x_T, x_T))
            M_TW = expand(diff(Sh_r, x_T, x_W))
            M_WW = expand(diff(Sh_r, x_W, x_W))
            contributions[r] = Matrix([
                [M_TT, M_TW],
                [M_TW, M_WW],
            ])

    return contributions


# =============================================================================
# 6.  Arity-2 contribution (the curvature kernel)
# =============================================================================

def arity2_contribution():
    """Arity-2 contribution to the shadow metric.

    Sh_2 = (c/2) x_T^2 + (c/3) x_W^2

    Hessian: [[c, 0], [0, 2c/3]]

    This is the CONSTANT part of the shadow metric (independent of x_T, x_W).
    """
    return Matrix([
        [c, S.Zero],
        [S.Zero, 2 * c / 3],
    ])


# =============================================================================
# 7.  Arity-3 contribution (the cubic seed)
# =============================================================================

def arity3_contribution():
    """Arity-3 contribution to the shadow metric.

    Sh_3 = 2 x_T^3 + 3 x_T x_W^2
    d^2 Sh_3 / d(x_T)^2 = 12 x_T
    d^2 Sh_3 / d(x_T) d(x_W) = 6 x_W
    d^2 Sh_3 / d(x_W)^2 = 6 x_T
    """
    return Matrix([
        [12 * x_T, 6 * x_W],
        [6 * x_W, 6 * x_T],
    ])


# =============================================================================
# 8.  Arity-4 contribution (the quartic curvature)
# =============================================================================

def arity4_contribution():
    """Arity-4 contribution to the shadow metric.

    Sh_4 = Q_TT x_T^4 + 6 Q_TW x_T^2 x_W^2 + Q_WW x_W^4
    d^2/d(x_T)^2 = 12 Q_TT x_T^2 + 12 Q_TW x_W^2
    d^2/(d(x_T) d(x_W)) = 24 Q_TW x_T x_W
    d^2/d(x_W)^2 = 12 Q_TW x_T^2 + 12 Q_WW x_W^2
    """
    qt = w3_quartic_tensor()
    Q_TT = qt['Q_TTTT']
    Q_TW = qt['Q_TTWW']
    Q_WW = qt['Q_WWWW']

    M_TT = 12 * Q_TT * x_T**2 + 12 * Q_TW * x_W**2
    M_TW = 24 * Q_TW * x_T * x_W
    M_WW = 12 * Q_TW * x_T**2 + 12 * Q_WW * x_W**2

    return Matrix([
        [expand(M_TT), expand(M_TW)],
        [expand(M_TW), expand(M_WW)],
    ])


# =============================================================================
# 9.  Critical discriminant and spectral curve
# =============================================================================

def shadow_metric_determinant(max_arity: int = 8) -> object:
    """det(M) = M_TT * M_WW - M_TW^2.

    The zero locus det(M) = 0 is the SPECTRAL CURVE of the 2D shadow metric.
    The shadow tower behavior (termination vs infinity) is controlled by
    this determinant.
    """
    M = shadow_metric_matrix(max_arity)
    return expand(M.det())


def shadow_metric_trace(max_arity: int = 8) -> object:
    """Tr(M) = M_TT + M_WW."""
    M = shadow_metric_matrix(max_arity)
    return expand(M.trace())


def shadow_metric_eigenvalues_sum_product(max_arity: int = 8) -> Dict[str, object]:
    """The eigenvalue sum and product of the shadow metric matrix.

    eigenvalue sum = Tr(M)
    eigenvalue product = det(M)

    The eigenvalues are real since M is symmetric.
    """
    M = shadow_metric_matrix(max_arity)
    tr = expand(M.trace())
    det = expand(M.det())
    return {
        'trace': tr,
        'det': det,
        'discriminant': expand(tr**2 - 4 * det),
    }


# =============================================================================
# 10.  1D restrictions and consistency checks
# =============================================================================

def tline_shadow_metric(max_arity: int = 8) -> object:
    """Shadow metric restricted to the T-line (x_W = 0).

    This should match the 1D Virasoro shadow metric:
    Q_Vir(t) = (2kappa + alpha*t)^2 + 2*kappa*Delta*t^2
    with kappa = c/2, alpha = 2, Delta = 8*(c/2)*Q_Vir = 40/(5c+22).
    """
    M = shadow_metric_matrix(max_arity)
    return expand(M[0, 0].subs(x_W, 0))


def wline_shadow_metric(max_arity: int = 8) -> object:
    """Shadow metric restricted to the W-line (x_T = 0).

    Returns the (WW) entry of M evaluated at x_T = 0.
    """
    M = shadow_metric_matrix(max_arity)
    return expand(M[1, 1].subs(x_T, 0))


def tline_virasoro_comparison(max_arity: int = 8) -> Dict[str, object]:
    """Compare the T-line restriction of the 2D metric with the Virasoro metric.

    The 1D Virasoro shadow metric is:
    Q_Vir(t) = c^2 + 12c*t + [(180c + 872)/(5c+22)] * t^2 + ...

    From the Virasoro shadow tower with kappa = c/2, alpha = 2,
    S_4 = 10/[c(5c+22)]:
        Q_Vir(t) = (c + 2t)^2 + (c/2)*[80/(c*(5c+22))]*t^2
                 = c^2 + 4ct + 4t^2 + 40/(5c+22)*t^2 + higher order

    Wait: the shadow metric is NOT just arity 2+3+4.  It is the full
    generating function Hessian H''(t) at all arities.  So we need to
    compare term by term.
    """
    tline_metric = tline_shadow_metric(max_arity)

    # Build the Virasoro GF Hessian for comparison
    from sympy import Poly as SymPoly
    x = Symbol('x_dummy')

    # Virasoro shadow coefficients
    vir_coeffs = {
        2: c / 2,
        3: Rational(2),
        4: Rational(10) / (c * (5 * c + 22)),
        5: Rational(-48) / (c**2 * (5 * c + 22)),
    }

    vir_gf = S.Zero
    for r, coeff in vir_coeffs.items():
        vir_gf += coeff * x_T**r

    vir_metric = expand(diff(vir_gf, x_T, x_T))

    # Compare up to the degree we have Virasoro coefficients for
    diff_val = simplify(expand(tline_metric) - expand(vir_metric))
    # The difference should be zero through the common arities, but may
    # have higher-order terms from arities > 5 that we don't have Virasoro data for.

    return {
        '2d_tline_metric': tline_metric,
        'virasoro_metric': vir_metric,
        'difference': diff_val,
    }


# =============================================================================
# 11.  Propagator variance from the 2D metric
# =============================================================================

def propagator_variance_from_metric() -> object:
    """Compute the propagator variance delta_mix from the 2D shadow metric.

    delta_mix = sum_i f_i^2/kappa_i - (sum_i f_i)^2 / sum_i kappa_i

    where f_i = d(Sh_4)/d(x_i) evaluated on the diagonal x_T = x_W = x,
    extracting the coefficient of x^3.

    This is computable from arity 2 (kappas) and arity 4 (quartic shadow) alone.
    """
    qt = w3_quartic_tensor()
    Q_TT = qt['Q_TTTT']
    Q_TW = qt['Q_TTWW']
    Q_WW = qt['Q_WWWW']

    Sh_4 = w3_quartic_polynomial()

    # Quartic gradients on the diagonal x_T = x_W = x
    x = Symbol('x')
    dSh4_dT = diff(Sh_4, x_T).subs([(x_T, x), (x_W, x)])
    dSh4_dW = diff(Sh_4, x_W).subs([(x_T, x), (x_W, x)])

    # Extract coefficient of x^3
    f_T = cancel(Poly(dSh4_dT, x).nth(3))
    f_W = cancel(Poly(dSh4_dW, x).nth(3))

    kappa_T = c / 2
    kappa_W = c / 3

    delta = cancel(
        f_T**2 / kappa_T + f_W**2 / kappa_W
        - (f_T + f_W)**2 / (kappa_T + kappa_W)
    )

    return {
        'f_T': factor(f_T),
        'f_W': factor(f_W),
        'kappa_T': kappa_T,
        'kappa_W': kappa_W,
        'delta_mix': factor(delta),
    }


def mixing_polynomial() -> object:
    """The mixing polynomial P(c) = 25c^2 + 100c - 428 for W_3.

    P = 0 iff f_T/kappa_T = f_W/kappa_W (curvature-proportional quartic gradient).
    At the roots of P, the diagonal restriction is autonomous.
    """
    return 25 * c**2 + 100 * c - 428


def mixing_polynomial_from_gradients() -> object:
    """Derive P(c) from the curvature-proportionality condition.

    f_T/kappa_T = f_W/kappa_W
    => f_T * kappa_W - f_W * kappa_T = 0

    The numerator of this expression is the mixing polynomial P(c).
    """
    pv = propagator_variance_from_metric()
    f_T = pv['f_T']
    f_W = pv['f_W']
    kappa_T = pv['kappa_T']
    kappa_W = pv['kappa_W']

    # Proportionality test: f_T/kappa_T - f_W/kappa_W = 0
    test_expr = cancel(f_T / kappa_T - f_W / kappa_W)
    num = numer(cancel(test_expr))
    return factor(num)


# =============================================================================
# 12.  Enhanced symmetry loci
# =============================================================================

def enhanced_symmetry_loci() -> List:
    """Central charges where P(c) = 0 (enhanced symmetry).

    P = 25c^2 + 100c - 428 = 0
    c = (-100 +/- sqrt(10000 + 42800)) / 50
      = (-100 +/- sqrt(52800)) / 50
      = (-100 +/- 40*sqrt(33)) / 50
      = (-10 +/- 4*sqrt(33)) / 5
    """
    from sympy import solve
    P = mixing_polynomial()
    return solve(P, c)


# =============================================================================
# 13.  Diagonal restriction of the 2D metric
# =============================================================================

def diagonal_shadow_metric(max_arity: int = 8) -> object:
    """Shadow metric on the diagonal x_T = x_W = x.

    This gives the effective 1D shadow metric for the total deformation
    direction (1, 1) in the primary plane.
    """
    M = shadow_metric_matrix(max_arity)

    # On the diagonal, the effective metric is:
    # Q_diag(x) = (1, 1) M(x, x) (1, 1)^T = M_TT + 2*M_TW + M_WW
    M_diag = M[0, 0] + 2 * M[0, 1] + M[1, 1]
    return expand(M_diag.subs([(x_T, Symbol('x')), (x_W, Symbol('x'))]))


# =============================================================================
# 14.  Critical discriminant matrix (2D generalization)
# =============================================================================

def critical_discriminant_matrix() -> Matrix:
    """The 2D critical discriminant matrix Delta_{ij} = 8 * H_{ij} * Q_{ijkl}.

    For 1D: Delta = 8 * kappa * S_4.
    For 2D: the discriminant is a 2x2 matrix encoding the quartic curvature
    weighted by the Hessian.

    Delta_TT = 8 * kappa_T * Q_TTTT = 8 * (c/2) * 10/[c(5c+22)] = 40/(5c+22)
    Delta_TW = 8 * sqrt(kappa_T * kappa_W) * Q_TTWW
    Delta_WW = 8 * kappa_W * Q_WWWW

    The single-line discriminant on the T-line gives Delta_TT = 40/(5c+22),
    matching the Virasoro critical discriminant.
    """
    H = w3_hessian()
    qt = w3_quartic_tensor()

    Delta_TT = cancel(8 * H[0, 0] * qt['Q_TTTT'])
    Delta_WW = cancel(8 * H[1, 1] * qt['Q_WWWW'])
    # For the off-diagonal: use geometric mean of kappas
    Delta_TW = cancel(8 * sqrt(H[0, 0] * H[1, 1]) * qt['Q_TTWW'])

    return {
        'Delta_TT': Delta_TT,
        'Delta_TW': Delta_TW,
        'Delta_WW': Delta_WW,
    }


def virasoro_discriminant_check() -> Dict[str, object]:
    """Verify Delta_TT = 40/(5c+22) matches the Virasoro discriminant."""
    deltas = critical_discriminant_matrix()
    Delta_TT = deltas['Delta_TT']
    expected = Rational(40) / (5 * c + 22)
    return {
        'Delta_TT': Delta_TT,
        'expected': expected,
        'match': simplify(Delta_TT - expected) == 0,
    }


# =============================================================================
# 15.  Spectral curve analysis
# =============================================================================

def spectral_curve_low_order() -> object:
    """The spectral curve det(M) = 0 from the low-arity truncation.

    Using only arities 2, 3, 4 to build the shadow metric matrix,
    compute det(M) and analyze its zero locus.
    """
    M2 = arity2_contribution()
    M3 = arity3_contribution()
    M4 = arity4_contribution()

    M = M2 + M3 + M4

    det_M = expand(M.det())
    tr_M = expand(M.trace())

    return {
        'metric_matrix': M,
        'determinant': det_M,
        'trace': tr_M,
        'disc': expand(tr_M**2 - 4 * det_M),
    }


def spectral_curve_tline() -> object:
    """Spectral curve restricted to T-line (x_W = 0).

    On the T-line, M reduces to:
    M_TT = c + 12 x_T + 12 Q_TT x_T^2 + ...
    M_TW = 0 (by Z_2 parity: all mixed terms vanish at x_W = 0)
    M_WW = 2c/3 + 6 x_T + 12 Q_TW x_T^2 + ...

    det(M)|_{x_W=0} = M_TT * M_WW (block-diagonal).
    """
    data = spectral_curve_low_order()
    M = data['metric_matrix']

    M_T = M.subs(x_W, 0)
    det_T = expand(M_T.det())

    return {
        'M_TT': expand(M_T[0, 0]),
        'M_TW': expand(M_T[0, 1]),
        'M_WW': expand(M_T[1, 1]),
        'det': det_T,
        'factored': factor(det_T) if det_T != S.Zero else S.Zero,
    }


# =============================================================================
# 16.  W_3 Koszul conductor and duality
# =============================================================================

def w3_koszul_conductor():
    """The W_3 Koszul conductor K_3 = 100.

    W_3 at central charge c is Koszul dual to W_3 at central charge 100 - c.
    Self-dual at c = 50.
    """
    return 100


def koszul_dual_shadow_metric(max_arity: int = 8) -> Matrix:
    """Shadow metric of the Koszul dual W_3 at central charge K - c.

    M^!(x_T, x_W) = M(x_T, x_W)|_{c -> 100 - c}
    """
    M = shadow_metric_matrix(max_arity)
    K = w3_koszul_conductor()
    return M.subs(c, K - c)


def complementarity_trace(max_arity: int = 6) -> object:
    """Tr(M(c)) + Tr(M(100-c)): complementarity sum of traces."""
    M = shadow_metric_matrix(max_arity)
    K = w3_koszul_conductor()
    tr = M.trace()
    tr_dual = tr.subs(c, K - c)
    return cancel(tr + tr_dual)


# =============================================================================
# 17.  Autonomy directions
# =============================================================================

def curvature_proportional_direction() -> Dict[str, object]:
    """Find the direction (a, b) where the quartic gradient is proportional to kappa.

    On this direction: f_T/kappa_T = f_W/kappa_W.
    The shadow tower restricted to this direction is AUTONOMOUS.
    """
    pv = propagator_variance_from_metric()
    f_T = pv['f_T']
    f_W = pv['f_W']
    kappa_T = pv['kappa_T']
    kappa_W = pv['kappa_W']

    # Ratio f/kappa for each generator
    ratio_T = cancel(f_T / kappa_T)
    ratio_W = cancel(f_W / kappa_W)

    # The autonomous direction satisfies f_T(a,b)/kappa_T = f_W(a,b)/kappa_W
    # For the diagonal (a,b) = (1,1), this gives the mixing polynomial.
    # The general autonomous direction is c-dependent.

    return {
        'ratio_T': ratio_T,
        'ratio_W': ratio_W,
        'test': cancel(ratio_T - ratio_W),
    }


# =============================================================================
# 18.  Numerical evaluation
# =============================================================================

def evaluate_metric_at(c_val, xT_val=0, xW_val=0, max_arity: int = 8):
    """Numerically evaluate the shadow metric at specific (c, x_T, x_W)."""
    M = shadow_metric_matrix(max_arity)
    M_num = M.subs([(c, c_val), (x_T, xT_val), (x_W, xW_val)])
    return M_num


def evaluate_determinant_at(c_val, xT_val=0, xW_val=0, max_arity: int = 8):
    """Numerically evaluate det(M) at specific (c, x_T, x_W)."""
    M = evaluate_metric_at(c_val, xT_val, xW_val, max_arity)
    return M.det()


# =============================================================================
# 19.  Summary function
# =============================================================================

def full_2d_shadow_metric_summary(max_arity: int = 8) -> Dict[str, object]:
    """Compute and return a full summary of the 2D shadow metric.

    Includes:
    - Hessian and propagator
    - Cubic and quartic tensors
    - Shadow metric matrix (truncated at max_arity)
    - Arity-by-arity contributions
    - Critical discriminant
    - Propagator variance
    - Mixing polynomial
    - T-line and W-line restrictions
    """
    return {
        'hessian': w3_hessian(),
        'propagator': w3_propagator(),
        'total_kappa': w3_total_kappa(),
        'cubic_tensor': w3_cubic_tensor(),
        'quartic_tensor': w3_quartic_tensor(),
        'metric_matrix': shadow_metric_matrix(max_arity),
        'contributions': shadow_metric_contributions(max_arity),
        'propagator_variance': propagator_variance_from_metric(),
        'mixing_polynomial': mixing_polynomial(),
        'critical_discriminant': critical_discriminant_matrix(),
        'virasoro_check': virasoro_discriminant_check(),
    }


if __name__ == '__main__':
    print("=" * 70)
    print("W_3 2D Shadow Metric Computation")
    print("=" * 70)

    print("\n--- Hessian and propagator ---")
    H = w3_hessian()
    P = w3_propagator()
    print(f"  H = {H}")
    print(f"  P = {P}")
    print(f"  kappa = Tr(H) = {w3_total_kappa()}")

    print("\n--- Cubic shadow ---")
    ct = w3_cubic_tensor()
    print(f"  C_TTT = {ct['TTT']}, C_TWW = {ct['TWW']}")
    print(f"  Sh_3 = {w3_cubic_polynomial()}")

    print("\n--- Quartic shadow ---")
    qt = w3_quartic_tensor()
    for k, v in qt.items():
        print(f"  {k} = {factor(v)}")

    print("\n--- Propagator variance ---")
    pv = propagator_variance_from_metric()
    print(f"  f_T = {pv['f_T']}")
    print(f"  f_W = {pv['f_W']}")
    print(f"  delta_mix = {pv['delta_mix']}")

    print("\n--- Mixing polynomial ---")
    P_mix = mixing_polynomial()
    P_derived = mixing_polynomial_from_gradients()
    print(f"  P(c) = {P_mix}")
    print(f"  P_derived = {P_derived}")

    print("\n--- Critical discriminant ---")
    deltas = critical_discriminant_matrix()
    for k, v in deltas.items():
        print(f"  {k} = {factor(v)}")

    print("\n--- Virasoro check ---")
    vcheck = virasoro_discriminant_check()
    print(f"  Delta_TT = {vcheck['Delta_TT']}, match = {vcheck['match']}")

    print("\n--- Enhanced symmetry loci ---")
    loci = enhanced_symmetry_loci()
    print(f"  Roots of P: {loci}")

    print("\n--- Shadow metric matrix (arity <= 6) ---")
    M = shadow_metric_matrix(6)
    print(f"  M_TT = {collect(M[0, 0], [x_T, x_W])}")
    print(f"  M_TW = {collect(M[0, 1], [x_T, x_W])}")
    print(f"  M_WW = {collect(M[1, 1], [x_T, x_W])}")

    print("\n--- Spectral curve (low order) ---")
    sc = spectral_curve_low_order()
    print(f"  det(M) = {sc['determinant']}")
