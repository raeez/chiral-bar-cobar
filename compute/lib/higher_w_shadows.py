r"""Shadow tower data for W_4 and W_5 algebras as functions of central charge c.

W_N (principal DS reduction of sl_N-hat) has N-1 generators of weights 2, 3, ..., N.
The shadow Postnikov tower lives on the (N-1)-dimensional deformation space
with coordinates (x_2, x_3, ..., x_N) corresponding to each generator.

W_4 (generators T, W_3, W_4 of weights 2, 3, 4):
  kappa = diag(c/2, c/3, c/4), total kappa = 13c/12
  H_4 = 1 + 1/2 + 1/3 + 1/4 = 25/12, so kappa = c * (H_4 - 1) = 13c/12
  Shadow archetype: class M (infinite tower on every primary line)

W_5 (generators T, W_3, W_4, W_5 of weights 2, 3, 4, 5):
  kappa = diag(c/2, c/3, c/4, c/5), total kappa = 77c/60
  H_5 = 1 + 1/2 + 1/3 + 1/4 + 1/5 = 137/60, so kappa = c * (H_5 - 1) = 77c/60
  Shadow archetype: class M

KEY STRUCTURAL FEATURES:

1. CHANNEL-REFINED KAPPA. Each generator W_j contributes kappa_j = c/j.
   The total kappa(W_N) = c * (H_N - 1) grows as c * log(N).

2. PRIMARY-LINE SHADOW DATA. On each primary line (restricting to a single
   generator W_j with all others set to zero):
     kappa_j = c/j
     alpha_j = gravitational cubic coefficient on that line
     S4_j = quartic contact on that line (from quasi-primary exchange)
     Delta_j = 8 * kappa_j * S4_j (critical discriminant)

3. T-LINE IS UNIVERSAL. On the T-line (x_j = 0 for j >= 3), the shadow data
   is identical to the Virasoro algebra at the same central charge:
     kappa_T = c/2, alpha_T = 2, S4_T = 10/[c(5c+22)]
   This is because the T-line sees only the Virasoro subalgebra.

4. GRAVITATIONAL CUBIC. The gravitational part of the cubic shadow is
   determined by conformal weights alone:
     C^grav(T, T, T) = 2, C^grav(T, W_j, W_j) = j
   In polynomial form: Sh_3^grav = 2 x_T^3 + sum_{j=3}^N j x_T x_j^2

5. MULTI-CHANNEL QUARTIC. The quartic shadow on each line involves exchange
   of weight-4 quasi-primaries. The quasi-primary spectrum at weight 4 is:
     Lambda = :TT: - (3/10) d^2 T (norm N_Lambda = c(5c+22)/10)
     W_4 itself (if present as a generator, norm N_{W_4} = c/4)

   For W_3: only Lambda mediates (1 channel at weight 4).
   For W_4 and W_5: both Lambda AND W_4 mediate (2 channels at weight 4).
   This is the key structural upgrade at rank >= 3.

6. PROPAGATOR VARIANCE. The multi-channel non-autonomy invariant
     delta_mix = sum_j f_j^2/kappa_j - (sum_j f_j)^2 / (sum_j kappa_j)
   measures deviation from a single effective 1D tower on the diagonal.
   Non-negative by Cauchy-Schwarz; vanishes iff curvature-proportional.

PARITY CONSTRAINTS. The W_3 generator has Z_2 parity (W_3 -> -W_3) that
forces odd powers of x_3 to vanish in the shadow tower. The W_4 and W_5
generators do NOT have such a simple parity, so their self-cubics (c_444,
c_555) are generically nonzero.

Manuscript references:
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
  thm:propagator-variance (higher_genus_modular_koszul.tex)
  thm:w-universal-gravitational-cubic (w_algebras.tex)
  comp:w4-kappa (w_algebras.tex)

Dependencies:
  w3_shadow_tower_engine.py: W_3 data for comparison
  w4_multivariable_shadow.py: W_4 quasi-primary spectrum
  propagator_variance.py: mixing polynomial computation
  shadow_radius.py: growth rate theory
  wn_channel_refined.py: harmonic number kappa
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Matrix,
    Rational,
    S,
    Symbol,
    cancel,
    diff,
    expand,
    factor,
    simplify,
    sqrt,
    symbols,
)


c = Symbol('c')


# ============================================================================
# 1. Harmonic numbers and total kappa
# ============================================================================

def harmonic_number(n: int) -> Rational:
    """H_n = sum_{j=1}^n 1/j (exact rational)."""
    return sum(Rational(1, j) for j in range(1, n + 1))


def anomaly_ratio(N: int) -> Rational:
    r"""rho(W_N) = H_N - 1 = sum_{j=2}^N 1/j.

    kappa(W_N) = rho(W_N) * c.
    """
    return harmonic_number(N) - 1


def total_kappa(N: int, c_val=None):
    r"""Total modular characteristic kappa(W_N) = c * (H_N - 1).

    W_2 = Virasoro: kappa = c/2
    W_3: kappa = 5c/6
    W_4: kappa = 13c/12
    W_5: kappa = 77c/60
    """
    cc = c_val if c_val is not None else c
    return anomaly_ratio(N) * cc


def channel_kappa(j: int, c_val=None):
    """Channel contribution kappa_j = c/j from the W_j self-coupling."""
    cc = c_val if c_val is not None else c
    return cc / j


def kappa_matrix(N: int, c_val=None) -> Matrix:
    """Diagonal kappa matrix diag(c/2, c/3, ..., c/N)."""
    cc = c_val if c_val is not None else c
    entries = [cc / j for j in range(2, N + 1)]
    return Matrix.diag(*entries)


def propagator_matrix(N: int, c_val=None) -> Matrix:
    """Inverse kappa matrix diag(2/c, 3/c, ..., N/c)."""
    cc = c_val if c_val is not None else c
    entries = [j / cc for j in range(2, N + 1)]
    return Matrix.diag(*entries)


# ============================================================================
# 2. Koszul duality data
# ============================================================================

def koszul_dual_c(N: int) -> Any:
    r"""Koszul dual central charge c' such that c + c' = K_N.

    For W_N from sl_N: Feigin-Frenkel duality k <-> -k - 2N gives
    c + c' = (N-1)(N+1)^2/N * 2  [the complementarity sum].

    Explicit values:
      W_2 (Virasoro): c + c' = 26
      W_3: c + c' = 100
      W_4: c + c' = ???

    Actually the formula for principal W_N is:
      c(k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
    and c(k) + c(k') = 2(N-1) where k' = -k-2N? No...

    For W_2: c(k) = 1 - 6/(k+2), c' = c(-k-4) = 1 - 6/(-k-2), c+c' = 26. Hmm:
      c(-k-4) = 1 - 6/(-k-4+2) = 1 - 6/(-k-2) = 1 + 6/(k+2)
      c + c' = 2 - 6/(k+2) + 6/(k+2) = 2? No, that's wrong.
      Actually c(Vir, k) = 1 - 6(k+1)^2/(k+2).
      c' = c(-k-4) = 1 - 6(-k-3)^2/(-k-2) = 1 + 6(k+3)^2/(k+2)
      c + c' = 2 + 6[(k+3)^2 - (k+1)^2]/(k+2) = 2 + 6(4k+8)/(k+2) = 2 + 24 = 26. ✓

    For general W_N, under k -> k' = -k - 2N:
      c(k) + c(k') = (N-1)[2 - N(N+1)/(k+N) - N(N+1)/(-k-N)]
      = (N-1)[2 - N(N+1)/(k+N) + N(N+1)/(k+N)]
      Hmm, that gives (N-1)*2. That's not right either.

    Let me use the correct Fateev-Lukyanov:
      c(W_N, k) = (N-1)[1 - N(N+1)/(k+N)]
    Under k' = -k-2N: k'+N = -k-N, so 1/(k'+N) = -1/(k+N).
      c(k') = (N-1)[1 + N(N+1)/(k+N)]
      c(k) + c(k') = 2(N-1)

    So K_N = 2(N-1):
      W_2: K = 2     ... but Virasoro has c + c' = 26!

    There's a discrepancy. The issue is which formula is being used.
    The "simple" Fateev-Lukyanov c = (N-1)[1 - N(N+1)/(k+N)] is NOT
    the standard formula. The standard is:
      c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
    Let me not go down this rabbit hole. Return the known values.
    """
    known = {
        2: 26,        # Virasoro: c + c' = 26
        3: 100,       # W_3: c + c' = 100
    }
    if N in known:
        return known[N]
    # General formula not implemented; return symbolic
    return None


def complementarity_kappa_sum(N: int) -> Any:
    r"""kappa(c) + kappa(c') where c + c' = K_N.

    kappa + kappa' = rho * (c + c') = (H_N - 1) * K_N.

    W_2: (1/2) * 26 = 13
    W_3: (5/6) * 100 = 250/3
    """
    K = koszul_dual_c(N)
    if K is None:
        return None
    rho = anomaly_ratio(N)
    return rho * K


# ============================================================================
# 3. Weight-4 quasi-primary exchange data (universal)
# ============================================================================

def lambda_norm(c_val=None):
    r"""BPZ norm of Lambda = :TT: - (3/10) d^2 T.

    N_Lambda = c(5c + 22)/10.
    This is universal (depends only on the Virasoro sector).
    """
    cc = c_val if c_val is not None else c
    return cc * (5 * cc + 22) / 10


def coupling_to_lambda(j: int, c_val=None):
    r"""Coupling C(W_j, W_j, Lambda) from the W_j x W_j OPE.

    For j = 2 (T): C(T,T,Lambda) = 1.
      (From T_{(-1)}T = :TT: = Lambda + (3/10)d^2T, coefficient of Lambda is 1.)

    For j = 3 (W_3): C(W_3,W_3,Lambda) = alpha_33 = 16/(5c+22).
      (From W_3_{(1)}W_3 at pole order h+h-4 = 2, the Lambda coefficient.)

    For j >= 4: the coupling C(W_j, W_j, Lambda) involves the W_j x W_j OPE
    at pole order 2j-4. The extraction requires the full Gram matrix at
    weight 4, but the Lambda coefficient alpha_jj can be computed from the
    L_{-2}^2 coefficient in the OPE.

    For j = 4: C(W_4, W_4, Lambda) involves the W_4_{(3)}W_4 product.
      The W_4 x W_4 OPE at (z-w)^{-4} gives weight-4 output. The
      quasi-primary projection onto Lambda is computable from the
      mode algebra.

    UNIVERSAL FORMULA for the gravitational contribution to the Lambda
    coupling (from the stress tensor sector):
      C(W_j, W_j, Lambda) = j(2j-1) / (5c+22) * (some normalization)

    Actually, the simplest approach: from conformal Ward identities,
      <W_j W_j Lambda> = beta_j(c)
    where beta_j is determined by the W_j conformal weight h_j = j.

    For concrete computations: the T-sector contribution to C(W_j,W_j,Lambda)
    comes from the singular terms in the T(z)W_j(w) OPE that contribute to
    the :TT: composite. By dimensional analysis and conformal invariance:

      C(W_j, W_j, Lambda) = 2j(2j-1) / ((2j-2)(2j-3)) * (some factor)

    This is getting involved. Let me use the known values and leave higher
    ones as inputs.
    """
    cc = c_val if c_val is not None else c
    if j == 2:
        return S.One
    elif j == 3:
        return Rational(16) / (5 * cc + 22)
    else:
        # For j >= 4, need the full OPE computation.
        # Return symbolic placeholder.
        return Symbol(f'alpha_{j}{j}')


# ============================================================================
# 4. Primary-line shadow data
# ============================================================================

def t_line_data(c_val=None) -> Dict[str, Any]:
    r"""Shadow data on the T-line (all x_j = 0 for j >= 3).

    UNIVERSAL for all W_N: identical to Virasoro.
      kappa_T = c/2
      alpha_T = 2 (from T_(1)T = 2T)
      S4_T = 10/[c(5c+22)] (from Lambda exchange)
      Delta_T = 40/(5c+22)
    """
    cc = c_val if c_val is not None else c
    kappa = cc / 2
    alpha = Rational(2)
    S4 = Rational(10) / (cc * (5 * cc + 22))
    Delta = 8 * kappa * S4
    return {
        'kappa': kappa,
        'alpha': alpha,
        'S4': cancel(S4),
        'Delta': cancel(Delta),
        'depth_class': 'M',
        'rho_sq': cancel((9 * alpha**2 + 2 * Delta) / (4 * kappa**2)),
    }


def w3_line_data_in_w4(c_val=None) -> Dict[str, Any]:
    r"""Shadow data on the W_3-line of W_4 (x_T = x_4 = 0).

    kappa = c/3
    alpha = 0 (Z_2 parity: W_3 -> -W_3 kills odd arities)

    S4 has TWO exchange channels (unlike the W_3 algebra's W-line):
      (a) Lambda exchange: C(W_3,W_3,Lambda)^2 / N_Lambda
          = [16/(5c+22)]^2 / [c(5c+22)/10] = 2560/[c(5c+22)^3]
      (b) W_4 exchange: C(W_3,W_3,W_4)^2 / N_{W_4}
          = c_334^2 / (c/4) = 4 c_334^2 / c

    The W_4 exchange channel is ABSENT in the W_3 algebra (which has no
    weight-4 primary), making this a genuine structural upgrade.

    For the W_3 x W_3 OPE: the structure constant c_334 = C(W_3, W_3, W_4)
    is known from the Zamolodchikov recursion for principal W_4. The full
    formula involves c and the W_4 normalization.

    For the GRAVITATIONAL part only (ignoring c_334):
      S4^grav = 2560/[c(5c+22)^3] (same as W_3 algebra's W-line)
    """
    cc = c_val if c_val is not None else c
    kappa = cc / 3
    alpha = Rational(0)

    # Lambda-exchange contribution (gravitational)
    alpha_33 = Rational(16) / (5 * cc + 22)
    N_Lambda = cc * (5 * cc + 22) / 10
    S4_Lambda = alpha_33**2 / N_Lambda

    # W_4-exchange contribution (non-gravitational, symbolic)
    c_334 = Symbol('c_334')
    N_W4 = cc / 4
    S4_W4 = c_334**2 / N_W4

    S4_total = cancel(S4_Lambda) + cancel(S4_W4)
    S4_grav = cancel(S4_Lambda)

    Delta_grav = 8 * kappa * S4_grav

    return {
        'kappa': kappa,
        'alpha': alpha,
        'S4_Lambda': cancel(S4_Lambda),
        'S4_W4': cancel(S4_W4),
        'S4_total': S4_total,
        'S4_gravitational': cancel(S4_grav),
        'Delta_gravitational': cancel(Delta_grav),
        'depth_class': 'M',
        'note': 'W_4 exchange channel present (absent in W_3 algebra)',
        'c_334': c_334,
    }


def w4_line_data_in_w4(c_val=None) -> Dict[str, Any]:
    r"""Shadow data on the W_4-line of W_4 (x_T = x_3 = 0).

    kappa = c/4
    alpha = c_444 (the W_4 self-coupling: W_4_{(3)}W_4 -> c_444 * W_4)
      No Z_2 parity constraint: W_4 has even weight, so self-cubic is
      generically nonzero for the principal W_4 algebra.

    S4 has TWO exchange channels:
      (a) Lambda exchange: C(W_4,W_4,Lambda)^2 / N_Lambda
          = alpha_44^2 / [c(5c+22)/10] = 10 alpha_44^2 / [c(5c+22)]
      (b) W_4 self-exchange: C(W_4,W_4,W_4)^2 / N_{W_4}
          = c_444^2 / (c/4) = 4 c_444^2 / c
    """
    cc = c_val if c_val is not None else c
    kappa = cc / 4
    c_444 = Symbol('c_444')
    alpha_44 = Symbol('alpha_44')

    alpha = c_444  # self-cubic (symbolic)

    N_Lambda = cc * (5 * cc + 22) / 10
    N_W4 = cc / 4

    S4_Lambda = alpha_44**2 / N_Lambda
    S4_W4 = c_444**2 / N_W4

    S4_total = cancel(S4_Lambda) + cancel(S4_W4)

    return {
        'kappa': kappa,
        'alpha': alpha,
        'S4_Lambda': cancel(S4_Lambda),
        'S4_W4': cancel(S4_W4),
        'S4_total': S4_total,
        'depth_class': 'M',
        'alpha_44': alpha_44,
        'c_444': c_444,
    }


def w3_line_data_in_w5(c_val=None) -> Dict[str, Any]:
    r"""Shadow data on the W_3-line of W_5 (x_T = x_4 = x_5 = 0).

    kappa = c/3
    alpha = 0 (Z_2 parity)

    S4 has TWO exchange channels:
      (a) Lambda exchange: 2560/[c(5c+22)^3]
      (b) W_4 exchange (if C(W_3,W_3,W_4) != 0): 4 c_334^2 / c

    Note: W_5 does NOT appear at weight 4, so it adds no new exchange
    channel at the quartic level compared to W_4.
    """
    cc = c_val if c_val is not None else c
    kappa = cc / 3
    alpha = Rational(0)

    alpha_33 = Rational(16) / (5 * cc + 22)
    N_Lambda = cc * (5 * cc + 22) / 10
    S4_Lambda = alpha_33**2 / N_Lambda

    c_334 = Symbol('c_334')
    N_W4 = cc / 4
    S4_W4 = c_334**2 / N_W4

    return {
        'kappa': kappa,
        'alpha': alpha,
        'S4_Lambda': cancel(S4_Lambda),
        'S4_W4': cancel(S4_W4),
        'S4_total': cancel(S4_Lambda) + cancel(S4_W4),
        'S4_gravitational': cancel(S4_Lambda),
        'depth_class': 'M',
        'c_334': c_334,
    }


def w4_line_data_in_w5(c_val=None) -> Dict[str, Any]:
    r"""Shadow data on the W_4-line of W_5 (x_T = x_3 = x_5 = 0).

    kappa = c/4. Same exchange channels as W_4-line in W_4:
    Lambda and W_4 (self-exchange). W_5 has weight 5, not weight 4,
    so does not contribute a new exchange channel at the quartic level.
    """
    return w4_line_data_in_w4(c_val)


def w5_line_data_in_w5(c_val=None) -> Dict[str, Any]:
    r"""Shadow data on the W_5-line of W_5 (x_T = x_3 = x_4 = 0).

    kappa = c/5
    alpha = c_555 (W_5 self-cubic, generically nonzero for odd weight)

    Actually: W_5 has weight 5 (odd), so it has a Z_2 symmetry W_5 -> -W_5
    analogous to W_3. On the W_5-line, odd powers of x_5 vanish.
    Therefore alpha_{W_5} = 0 (cubic vanishes).

    S4 exchange channels:
      (a) Lambda exchange: C(W_5,W_5,Lambda)^2 / N_Lambda
      (b) W_4 exchange: C(W_5,W_5,W_4)^2 / N_{W_4}
          (from W_5 x W_5 OPE at pole order 5+5-4 = 6: W_5_{(5)}W_5)
    """
    cc = c_val if c_val is not None else c
    kappa = cc / 5
    alpha = Rational(0)  # Z_2 parity kills odd arities

    N_Lambda = cc * (5 * cc + 22) / 10
    N_W4 = cc / 4

    alpha_55 = Symbol('alpha_55')  # C(W_5, W_5, Lambda)
    c_554 = Symbol('c_554')        # C(W_5, W_5, W_4)

    S4_Lambda = alpha_55**2 / N_Lambda
    S4_W4 = c_554**2 / N_W4

    return {
        'kappa': kappa,
        'alpha': alpha,
        'S4_Lambda': cancel(S4_Lambda),
        'S4_W4': cancel(S4_W4),
        'S4_total': cancel(S4_Lambda) + cancel(S4_W4),
        'depth_class': 'M',
        'alpha_55': alpha_55,
        'c_554': c_554,
    }


# ============================================================================
# 5. Gravitational cubic shadow (universal part)
# ============================================================================

def gravitational_cubic(N: int, c_val=None):
    r"""Gravitational cubic shadow Sh_3^grav for W_N.

    From thm:w-universal-gravitational-cubic:
      C^grav(T, T, T) = 2
      C^grav(T, W_j, W_j) = j  (conformal weight eigenvalue from T_(1)W_j = j W_j)

    The gravitational cubic in polynomial form:
      Sh_3^grav = 2 x_2^3 + sum_{j=3}^N j * x_2 * x_j^2

    This is the part of the cubic shadow determined purely by conformal weights.
    The full cubic may also include non-gravitational terms from W_j x W_k OPEs.
    """
    x = [Symbol(f'x_{j}') for j in range(2, N + 1)]

    # TT->T gravitational cubic
    result = 2 * x[0]**3

    # T-W_j-W_j gravitational couplings
    for idx, j in enumerate(range(3, N + 1)):
        result += j * x[0] * x[idx + 1]**2

    return expand(result)


def gravitational_cubic_w4():
    """Gravitational cubic for W_4: 2 x_T^3 + 3 x_T x_3^2 + 4 x_T x_4^2."""
    x_T, x_3, x_4 = symbols('x_T x_3 x_4')
    return 2 * x_T**3 + 3 * x_T * x_3**2 + 4 * x_T * x_4**2


def gravitational_cubic_w5():
    """Gravitational cubic for W_5: 2x_T^3 + 3x_T x_3^2 + 4x_T x_4^2 + 5x_T x_5^2."""
    x_T, x_3, x_4, x_5 = symbols('x_T x_3 x_4 x_5')
    return 2 * x_T**3 + 3 * x_T * x_3**2 + 4 * x_T * x_4**2 + 5 * x_T * x_5**2


# ============================================================================
# 6. Quartic contact on each primary line
# ============================================================================

def Q_contact_T_line(c_val=None):
    r"""Quartic contact on the T-line = Virasoro quartic contact.

    Q^contact_T = S4 = 10/[c(5c+22)].
    Universal for all W_N.
    """
    cc = c_val if c_val is not None else c
    return Rational(10) / (cc * (5 * cc + 22))


def Q_contact_w3_line_gravitational(c_val=None):
    r"""Gravitational part of quartic contact on the W_3-line.

    From pure Lambda exchange:
      Q^contact_{W_3-line}^{grav} = alpha_33^2 / N_Lambda
      = [16/(5c+22)]^2 / [c(5c+22)/10]
      = 2560 / [c(5c+22)^3]

    This is the same for the W_3-line in W_3, W_4, and W_5 (the Lambda
    exchange is independent of the ambient algebra).
    """
    cc = c_val if c_val is not None else c
    return Rational(2560) / (cc * (5 * cc + 22)**3)


def Q_contact_w4_line_Lambda(c_val=None):
    r"""Lambda-exchange contribution to quartic contact on the W_4-line.

    Q^{Lambda}_{W_4-line} = alpha_44^2 / N_Lambda
                          = 10 alpha_44^2 / [c(5c+22)]

    The coupling alpha_44 = C(W_4, W_4, Lambda) requires the full W_4 OPE.
    Returns symbolic expression in alpha_44.
    """
    cc = c_val if c_val is not None else c
    a44 = Symbol('alpha_44')
    N_L = cc * (5 * cc + 22) / 10
    return cancel(a44**2 / N_L)


# ============================================================================
# 7. Propagator variance
# ============================================================================

def w4_quartic_gradients_gravitational(c_val=None) -> List:
    r"""Quartic gradient f_j on the diagonal for W_4, gravitational part only.

    The quartic shadow on the 3d space has monomials x_T^a x_3^b x_4^c.
    The quartic gradient f_j = (d/dx_j) Sh_4 evaluated on the diagonal
    x_T = x_3 = x_4 = x.

    For the gravitational part (Lambda-exchange only), the quartic tensor is:
      Q_{ijkl}^grav = C_{ij,Lambda} * C_{kl,Lambda} / N_Lambda

    where C_{TT,Lambda} = 1, C_{33,Lambda} = 16/(5c+22), C_{44,Lambda} = alpha_44,
    and all mixed couplings C_{T3,Lambda} = C_{T4,Lambda} = C_{34,Lambda} = 0.

    The quartic polynomial (gravitational part):
      Sh_4^grav = Q_TT x_T^4 + 6 Q_{TT,33} x_T^2 x_3^2 + 6 Q_{TT,44} x_T^2 x_4^2
                + Q_{33} x_3^4 + 6 Q_{33,44} x_3^2 x_4^2 + Q_{44} x_4^4

    where Q_{ij} = C_{ii,Lambda}*C_{jj,Lambda}/N_Lambda.

    On the diagonal x_T = x_3 = x_4 = x:
      f_T^grav = 4*Q_TT + 12*Q_{TT,33} + 12*Q_{TT,44}   (times x^3)
      f_3^grav = 12*Q_{TT,33} + 4*Q_{33} + 12*Q_{33,44}  (times x^3)
      f_4^grav = 12*Q_{TT,44} + 12*Q_{33,44} + 4*Q_{44}  (times x^3)

    Note: these are the LAMBDA-ONLY contributions. The full quartic also
    includes W_4-exchange contributions.
    """
    cc = c_val if c_val is not None else c
    a33 = Rational(16) / (5 * cc + 22)
    a44 = Symbol('alpha_44')
    N_L = cc * (5 * cc + 22) / 10

    Q_TT = 1 / N_L
    Q_TT_33 = a33 / N_L
    Q_TT_44 = a44 / N_L
    Q_33 = a33**2 / N_L
    Q_33_44 = a33 * a44 / N_L
    Q_44 = a44**2 / N_L

    f_T = cancel(4 * Q_TT + 12 * Q_TT_33 + 12 * Q_TT_44)
    f_3 = cancel(12 * Q_TT_33 + 4 * Q_33 + 12 * Q_33_44)
    f_4 = cancel(12 * Q_TT_44 + 12 * Q_33_44 + 4 * Q_44)

    return [f_T, f_3, f_4]


def propagator_variance_general(kappas: List, f_values: List):
    r"""Propagator variance delta_mix.

    delta = sum_j f_j^2/kappa_j - (sum_j f_j)^2 / (sum_j kappa_j)

    Non-negative by Cauchy-Schwarz. Vanishes iff f_j/kappa_j is constant.
    """
    term1 = sum(f**2 / k for f, k in zip(f_values, kappas))
    term2 = sum(f_values)**2 / sum(kappas)
    return cancel(term1 - term2)


def w4_propagator_variance_gravitational(c_val=None):
    r"""Propagator variance for W_4 using gravitational quartic only.

    This uses only the Lambda-exchange contributions to the quartic.
    The full variance also includes W_4-exchange terms.
    """
    cc = c_val if c_val is not None else c
    kappas = [cc / 2, cc / 3, cc / 4]
    f_vals = w4_quartic_gradients_gravitational(cc)
    return propagator_variance_general(kappas, f_vals)


def w3_propagator_variance(c_val=None):
    r"""Propagator variance for W_3 (for comparison).

    W_3 has rank 2 with channels T and W:
      kappa_T = c/2, kappa_W = c/3
      f_T, f_W from Lambda-exchange quartic.

    The mixing polynomial is P(W_3) = 25c^2 + 100c - 428.
    """
    cc = c_val if c_val is not None else c
    alpha = Rational(16) / (5 * cc + 22)
    N_L = cc * (5 * cc + 22) / 10

    Q_TT = 1 / N_L
    Q_TW = alpha / N_L
    Q_WW = alpha**2 / N_L

    # On diagonal x_T = x_W = x:
    # Sh_4 = Q_TT x^4 + 6 Q_TW x^4 + Q_WW x^4
    # f_T = 4*Q_TT + 12*Q_TW (derivative of x_T^4 + 6 x_T^2 x_W^2 w.r.t. x_T at diag)
    # f_W = 12*Q_TW + 4*Q_WW
    f_T = cancel(4 * Q_TT + 12 * Q_TW)
    f_W = cancel(12 * Q_TW + 4 * Q_WW)

    kappas = [cc / 2, cc / 3]
    return propagator_variance_general(kappas, [f_T, f_W])


def w3_mixing_polynomial():
    r"""Mixing polynomial P(W_3) = 25c^2 + 100c - 428."""
    return 25 * c**2 + 100 * c - 428


# ============================================================================
# 8. Shadow metric and growth rate on primary lines
# ============================================================================

def shadow_metric_on_line(kappa_val, alpha_val, S4_val, c_val=None):
    r"""Shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    where Delta = 8*kappa*S4 is the critical discriminant.

    Returns coefficients (q0, q1, q2) of Q_L(t) = q0 + q1*t + q2*t^2.
    """
    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 16 * kappa_val * S4_val
    return cancel(q0), cancel(q1), cancel(q2)


def growth_rate_squared(kappa_val, alpha_val, S4_val):
    r"""Squared shadow growth rate rho^2 on a primary line.

    rho^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2)
          = (9*alpha^2 + 16*kappa*S4) / (4*kappa^2)
          = q2 / q0

    For class G/L: rho = 0 (Delta = 0, tower terminates).
    For class M: rho > 0 (tower infinite).
    """
    numer = 9 * alpha_val**2 + 16 * kappa_val * S4_val
    denom = 4 * kappa_val**2
    return cancel(numer / denom)


def t_line_growth_rate_squared(c_val=None):
    """rho_T^2 = (180c + 872) / [c^2(5c+22)]. Same as Virasoro."""
    cc = c_val if c_val is not None else c
    data = t_line_data(cc)
    return growth_rate_squared(data['kappa'], data['alpha'], data['S4'])


def w3_line_growth_rate_squared_gravitational(c_val=None):
    r"""rho_{W_3}^2 on the W_3-line (gravitational part only).

    alpha = 0, so rho^2 = 2*Delta / (4*kappa^2) = Delta / (2*kappa^2).

    Delta_grav = 8*(c/3)*2560/[c(5c+22)^3] = 20480/[3(5c+22)^3]

    rho^2 = 20480/[3(5c+22)^3] / (2*c^2/9) = 30720/[c^2(5c+22)^3]
    """
    cc = c_val if c_val is not None else c
    S4_grav = Rational(2560) / (cc * (5 * cc + 22)**3)
    kappa = cc / 3
    alpha = Rational(0)
    return growth_rate_squared(kappa, alpha, S4_grav)


# ============================================================================
# 9. Comprehensive W_4 shadow package
# ============================================================================

def w4_shadow_package(c_val=None) -> Dict[str, Any]:
    r"""Complete shadow tower data for W_4 as a function of c.

    Returns all computable quantities:
    - Kappa data (exact)
    - T-line data (exact, matches Virasoro)
    - W_3-line data (gravitational part exact, W_4-exchange symbolic)
    - W_4-line data (fully symbolic in alpha_44, c_444)
    - Gravitational cubic (exact)
    - Propagator variance (gravitational part)
    - Growth rates (gravitational part)
    """
    cc = c_val if c_val is not None else c

    return {
        'N': 4,
        'generators': {2: 'T', 3: 'W_3', 4: 'W_4'},
        'kappa_total': total_kappa(4, cc),
        'kappa_channels': {j: channel_kappa(j, cc) for j in range(2, 5)},
        'kappa_matrix': kappa_matrix(4, cc),
        'H_4': harmonic_number(4),
        'rho_4': anomaly_ratio(4),
        'gravitational_cubic': gravitational_cubic_w4(),
        'T_line': t_line_data(cc),
        'W3_line': w3_line_data_in_w4(cc),
        'W4_line': w4_line_data_in_w4(cc),
        'weight_4_quasi_primaries': {
            'dim': 2,
            'basis': ['Lambda', 'W_4'],
            'Lambda_norm': lambda_norm(cc),
            'W4_norm': cc / 4,
        },
        'depth_class': 'M',
        'shadow_archetype': 'mixed (infinite tower)',
    }


# ============================================================================
# 10. Comprehensive W_5 shadow package
# ============================================================================

def w5_shadow_package(c_val=None) -> Dict[str, Any]:
    r"""Complete shadow tower data for W_5 as a function of c.

    W_5 has 4 generators: T, W_3, W_4, W_5 of weights 2, 3, 4, 5.

    Key differences from W_4:
    1. One additional channel (kappa_5 = c/5)
    2. W_5 has Z_2 parity (odd weight -> W_5 -> -W_5 is a symmetry)
       so the W_5-line has alpha = 0 and only even arities
    3. At weight 4, still only Lambda and W_4 mediate the quartic exchange
       (W_5 has weight 5, not 4)
    4. At weight 5, there could be new quasi-primary exchanges for the
       quintic shadow, but that's arity 5, not 4
    """
    cc = c_val if c_val is not None else c

    return {
        'N': 5,
        'generators': {2: 'T', 3: 'W_3', 4: 'W_4', 5: 'W_5'},
        'kappa_total': total_kappa(5, cc),
        'kappa_channels': {j: channel_kappa(j, cc) for j in range(2, 6)},
        'kappa_matrix': kappa_matrix(5, cc),
        'H_5': harmonic_number(5),
        'rho_5': anomaly_ratio(5),
        'gravitational_cubic': gravitational_cubic_w5(),
        'T_line': t_line_data(cc),
        'W3_line': w3_line_data_in_w5(cc),
        'W4_line': w4_line_data_in_w5(cc),
        'W5_line': w5_line_data_in_w5(cc),
        'weight_4_quasi_primaries': {
            'dim': 2,
            'basis': ['Lambda', 'W_4'],
            'Lambda_norm': lambda_norm(cc),
            'W4_norm': cc / 4,
        },
        'depth_class': 'M',
        'shadow_archetype': 'mixed (infinite tower)',
    }


# ============================================================================
# 11. Structural comparison between W_3, W_4, W_5
# ============================================================================

def compare_algebras() -> Dict[str, Any]:
    r"""Structural comparison of shadow tower data across W_3, W_4, W_5.

    KEY DIFFERENCES:
    1. Kappa: W_3 = 5c/6, W_4 = 13c/12, W_5 = 77c/60
    2. Rank: W_3 = 2, W_4 = 3, W_5 = 4
    3. Weight-4 exchange channels: W_3 has 1 (Lambda only), W_4 and W_5 have 2
    4. Parity: W_3 has Z_2 on x_3-line, W_5 has Z_2 on x_5-line,
       W_4 has NO parity on x_4-line (even weight generator)
    5. Non-gravitational cubic: appears in W_4 (c_334 x_4 x_3^2 term),
       in W_5 additional terms (c_334 x_4 x_3^2, c_345..., c_355...)
    """
    rho_3 = anomaly_ratio(3)
    rho_4 = anomaly_ratio(4)
    rho_5 = anomaly_ratio(5)

    return {
        'kappa': {
            'W_3': Rational(5, 6) * c,
            'W_4': Rational(13, 12) * c,
            'W_5': Rational(77, 60) * c,
        },
        'rho': {
            'W_3': rho_3,
            'W_4': rho_4,
            'W_5': rho_5,
        },
        'rank': {'W_3': 2, 'W_4': 3, 'W_5': 4},
        'weight_4_exchange_dim': {
            'W_3': 1,   # Lambda only
            'W_4': 2,   # Lambda + W_4
            'W_5': 2,   # Lambda + W_4 (W_5 has weight 5, not 4)
        },
        'parity_lines': {
            'W_3': ['x_3 (Z_2)'],
            'W_4': ['x_3 (Z_2)'],
            'W_5': ['x_3 (Z_2)', 'x_5 (Z_2)'],
        },
        'depth_class': 'M (all)',
        'T_line_universal': True,
    }


# ============================================================================
# 12. Convolution recursion on a primary line
# ============================================================================

def tower_on_line_exact(kappa_val, alpha_val, S4_val, max_r: int = 10,
                        c_sym=None) -> Dict[int, Any]:
    r"""Exact shadow tower S_2, ..., S_{max_r} on a primary line.

    Uses the convolution recursion from H(t) = t^2 sqrt(Q_L(t)):
      f(t) = sqrt(Q_L(t)) = sum_{n>=0} a_n t^n
      S_r = a_{r-2} / r

    Works for positive c (uses sqrt(c^2) = c).
    """
    q0, q1, q2 = shadow_metric_on_line(kappa_val, alpha_val, S4_val)
    a0 = sqrt(q0)
    coeffs = [a0]

    if max_r >= 3:
        a1 = q1 / (2 * a0)
        coeffs.append(a1)
    if max_r >= 4:
        a2 = (q2 - coeffs[1]**2) / (2 * a0)
        coeffs.append(a2)
    for n in range(3, max_r - 1):
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(cancel(-conv_sum / (2 * a0)))

    result = {}
    for r_idx in range(len(coeffs)):
        r = r_idx + 2
        result[r] = cancel(coeffs[r_idx] / r)

    return result


def tower_on_line_numerical(kappa_val: float, alpha_val: float,
                            S4_val: float, max_r: int = 30) -> Dict[int, float]:
    """Numerical shadow tower on a primary line."""
    import math
    q0 = 4.0 * kappa_val**2
    q1 = 12.0 * kappa_val * alpha_val
    q2 = 9.0 * alpha_val**2 + 16.0 * kappa_val * S4_val

    a0 = math.sqrt(q0)
    coeffs = [a0]
    if max_r >= 3:
        coeffs.append(q1 / (2.0 * a0))
    if max_r >= 4:
        coeffs.append((q2 - coeffs[1]**2) / (2.0 * a0))
    for n in range(3, max_r - 1):
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(-conv_sum / (2.0 * a0))

    return {r_idx + 2: coeffs[r_idx] / (r_idx + 2) for r_idx in range(len(coeffs))}


def t_line_tower_w4_numerical(c_val: float, max_r: int = 30) -> Dict[int, float]:
    """T-line tower for W_4 at specific c (= Virasoro tower)."""
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    return tower_on_line_numerical(kappa, alpha, S4, max_r)


def w3_line_tower_w4_numerical(c_val: float, max_r: int = 30) -> Dict[int, float]:
    """W_3-line tower for W_4 at specific c (gravitational part only)."""
    kappa = c_val / 3.0
    alpha = 0.0
    S4 = 2560.0 / (c_val * (5.0 * c_val + 22.0)**3)
    return tower_on_line_numerical(kappa, alpha, S4, max_r)


# ============================================================================
# 13. Main
# ============================================================================

if __name__ == '__main__':
    from sympy import N as Neval

    print("=" * 70)
    print("HIGHER W-ALGEBRA SHADOW TOWER DATA")
    print("=" * 70)

    print("\n--- Harmonic numbers and kappa ---")
    for N in [2, 3, 4, 5]:
        H = harmonic_number(N)
        rho = anomaly_ratio(N)
        kap = total_kappa(N)
        print(f"  W_{N}: H_{N} = {H}, rho = {rho}, kappa = {kap}")

    print("\n--- W_4 shadow package ---")
    pkg4 = w4_shadow_package()
    print(f"  kappa_total = {pkg4['kappa_total']}")
    print(f"  kappa_channels = {pkg4['kappa_channels']}")
    print(f"  gravitational cubic = {pkg4['gravitational_cubic']}")
    print(f"  T-line S4 = {pkg4['T_line']['S4']}")
    print(f"  W_3-line S4 (grav) = {pkg4['W3_line']['S4_gravitational']}")
    print(f"  weight-4 QP dim = {pkg4['weight_4_quasi_primaries']['dim']}")

    print("\n--- W_5 shadow package ---")
    pkg5 = w5_shadow_package()
    print(f"  kappa_total = {pkg5['kappa_total']}")
    print(f"  kappa_channels = {pkg5['kappa_channels']}")
    print(f"  gravitational cubic = {pkg5['gravitational_cubic']}")

    print("\n--- Structural comparison ---")
    comp = compare_algebras()
    print(f"  Kappa: {comp['kappa']}")
    print(f"  Anomaly ratio: {comp['rho']}")
    print(f"  Weight-4 exchange dim: {comp['weight_4_exchange_dim']}")
    print(f"  Parity lines: {comp['parity_lines']}")

    print("\n--- T-line numerical tower at c = 30 ---")
    tower = t_line_tower_w4_numerical(30.0, max_r=10)
    for r in sorted(tower.keys()):
        print(f"  S_{r} = {tower[r]:.8e}")

    print("\n--- W_3-line numerical tower at c = 30 (grav) ---")
    tower = w3_line_tower_w4_numerical(30.0, max_r=10)
    for r in sorted(tower.keys()):
        print(f"  S_{r} = {tower[r]:.8e}")

    print("\n--- Propagator variance (W_3 comparison) ---")
    pv = w3_propagator_variance()
    print(f"  delta_mix(W_3) = {factor(pv)}")
    print(f"  P(W_3) = {w3_mixing_polynomial()}")
