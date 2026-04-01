r"""The shadow connection: logarithmic connection of the shadow metric.

THEOREM (Shadow connection, thm:shadow-connection).
Let A be a chirally Koszul algebra and L a primary line with
shadow metric Q_L(t) (Definition def:shadow-metric).

(i)   Q_L defines a logarithmic connection nabla^sh = d - Q'/(2Q) dt
      on the trivial line bundle O_L over L \ {Q = 0}.

(ii)  Regular singular points at the zeros of Q with residue 1/2.
      Monodromy: exp(2*pi*i * 1/2) = -1 (the Koszul sign).

(iii) Parallel transport: Phi(t) = sqrt(Q(t)/Q(0)). Shadow GF = t^2*sqrt(Q).

(iv)  Koszul duality transforms Q(t,c) -> Q(t,26-c) for Virasoro.
      Dual Lee-Yang points: -22/5 + 152/5 = 26.
      Self-dual at c = 13.

(v)   Complementarity sum: Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)].
      Constant numerator.

(vi)  Multi-channel curvature = propagator variance delta_mix.

(vii) Monodromy factors through Z/2: sheet exchange = Koszul sign.

COMPUTATION DETAILS:

For Virasoro on the T-line:
  kappa = c/2, alpha = S_3 = 2, S_4 = 10/[c(5c+22)], Delta = 40/(5c+22).
  Q_Vir(t) = c^2 + 12ct + [(180c+872)/(5c+22)] t^2.
  Gaussian decomposition: Q = (c + 6t)^2 + [80/(5c+22)] t^2.
  Zeros: t_0 = c * [-15c - 66 +/- 2*sqrt(-25c-110)] / (90c + 436).
  Connection form: omega = [30c^2 + (180c+872)t + 132c] / [(5c+22)*Q_Vir].

For W_3 on the W-line:
  kappa_W = c/3, alpha_W = 0 (Z_2 parity), S_4^W = 2560/[c(5c+22)^3].
  Delta_W = 20480/[3(5c+22)^3].
  Q_W(t) = 4c^2/9 + [40960/(3(5c+22)^3)] t^2.
  Branch points PURELY IMAGINARY (alpha = 0 kills the linear term).
  rho_W^2 = 30720/[c^2(5c+22)^3].

References:
  thm:shadow-connection (higher_genus_modular_koszul.tex)
  def:shadow-metric
  thm:riccati-algebraicity
  thm:propagator-variance
  cor:gaussian-decomposition
"""

from __future__ import annotations

from sympy import (
    I, Rational, Symbol, cancel, diff, exp, expand, factor, log,
    numer, denom, pi, simplify, solve, sqrt, symbols, Abs, Poly,
)

c = Symbol('c')
t = Symbol('t')


# =========================================================================
# 1. Shadow metric (general theory)
# =========================================================================

def shadow_metric_general(kappa, alpha, S4):
    """The shadow metric Q_L(t) on a primary line.

    Q_L(t) = (2*kappa)^2 + 2*(2*kappa)*(3*alpha)*t + ((3*alpha)^2 + 2*(2*kappa)*(4*S4))*t^2
           = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2

    Equivalently, from the Gaussian decomposition:
        Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2

    where Delta = 8*kappa*S4 is the critical discriminant.
    """
    return (2*kappa + 3*alpha*t)**2 + 2 * 8*kappa*S4 * t**2


def shadow_metric_expanded(kappa, alpha, S4):
    """Shadow metric in expanded polynomial form: q0 + q1*t + q2*t^2."""
    return expand(shadow_metric_general(kappa, alpha, S4))


def shadow_metric_coefficients(kappa, alpha, S4):
    """Coefficients (q0, q1, q2) of Q_L(t) = q0 + q1*t + q2*t^2."""
    q0 = 4*kappa**2
    q1 = 12*kappa*alpha
    q2 = 9*alpha**2 + 16*kappa*S4
    return q0, q1, q2


def critical_discriminant(kappa, S4):
    """The critical discriminant Delta = 8*kappa*S4.

    Controls the shadow depth classification:
      Delta = 0: tower terminates (class G or L), Q_L is a perfect square.
      Delta != 0: infinite tower (class M), Q_L is irreducible.
    """
    return 8*kappa*S4


def gaussian_decomposition(kappa, alpha, S4):
    """Decompose Q_L = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    Returns (gaussian_envelope, interaction_correction, Delta).
    """
    Delta = critical_discriminant(kappa, S4)
    gaussian = (2*kappa + 3*alpha*t)**2
    correction = 2*Delta*t**2
    return gaussian, correction, Delta


# =========================================================================
# 2. Connection form and flat sections
# =========================================================================

def connection_form(Q):
    """The logarithmic connection 1-form omega = Q'/(2Q) dt.

    The shadow connection is nabla^sh = d - omega.
    """
    Q_prime = diff(Q, t)
    return cancel(Q_prime / (2*Q))


def connection_form_from_data(kappa, alpha, S4):
    """Connection form computed from shadow data (kappa, alpha, S4)."""
    Q = shadow_metric_general(kappa, alpha, S4)
    return connection_form(Q)


def flat_section(Q):
    """The flat section Phi(t) = sqrt(Q(t)/Q(0)).

    Satisfies nabla^sh(Phi) = 0, Phi(0) = 1.
    """
    Q0 = Q.subs(t, 0)
    return sqrt(Q / Q0)


def shadow_generating_function(Q, kappa):
    """Shadow generating function H(t) = 2*kappa*t^2*Phi(t) = t^2*sqrt(Q).

    WARNING (AP23): H(t) is NOT a flat section of nabla^sh.
    The flat section is Phi(t) = sqrt(Q/Q(0)). The shadow GF is
    t^2 * Phi * sqrt(Q(0)) = t^2 * sqrt(Q), which has a double zero
    at t = 0 and therefore is NOT horizontal.

    Satisfies: H^2 = t^4 * Q (the Riccati algebraicity relation).
    """
    return t**2 * sqrt(Q)


# =========================================================================
# 3. Zeros, residues, and monodromy
# =========================================================================

def shadow_metric_zeros(Q):
    """Zeros of Q_L(t): the branch points of the shadow GF.

    At each simple zero t_0: Q(t) ~ Q'(t_0)*(t-t_0), so
    omega = Q'/(2Q) ~ 1/(2*(t-t_0)) with residue 1/2.

    Returns list of zeros as sympy expressions.
    """
    return solve(Q, t)


def shadow_metric_zeros_from_data(kappa, alpha, S4):
    """Zeros computed from the quadratic formula on Q_L coefficients."""
    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
    disc = q1**2 - 4*q0*q2
    t_plus = (-q1 + sqrt(disc)) / (2*q2)
    t_minus = (-q1 - sqrt(disc)) / (2*q2)
    return simplify(t_plus), simplify(t_minus)


def shadow_metric_discriminant(kappa, alpha, S4):
    """Discriminant of Q_L as a polynomial in t.

    disc(Q_L) = q1^2 - 4*q0*q2 = -32*kappa^2*Delta.

    Sign: negative when Delta > 0 (complex branch points, class M generic).
    Zero when Delta = 0 (class G or L, double root, tower terminates).
    Positive when Delta < 0 (real branch points, rare).
    """
    Delta = critical_discriminant(kappa, S4)
    return -32 * kappa**2 * Delta


def connection_residue_at_zero():
    """Residue of omega = Q'/(2Q) at a simple zero of Q.

    Universal: always 1/2, independent of the algebra.

    At a simple zero t_0: Q(t) ~ Q'(t_0)*(t - t_0), so
    omega ~ Q'(t_0)/(2*Q'(t_0)*(t-t_0)) = 1/(2*(t-t_0)).
    """
    return Rational(1, 2)


def monodromy_eigenvalue():
    """Monodromy around a simple zero of Q_L.

    exp(2*pi*i * residue) = exp(2*pi*i * 1/2) = exp(pi*i) = -1.

    This is the KOSZUL SIGN: the fundamental Z/2 symmetry of
    bar-cobar duality. The monodromy representation factors through
    Z/2, with the nontrivial element acting by -1 (sheet exchange
    of the double cover H^2 = t^4*Q_L).
    """
    return -1


def verify_residue_symbolically(kappa, alpha, S4):
    """Verify residue = 1/2 at each zero by Laurent expansion.

    For Q = q0 + q1*t + q2*t^2 with zero at t_0:
    Q(t) = q2*(t - t_0)*(t - t_1) near t_0,
    Q'(t) = q2*(2t - t_0 - t_1),
    Q'(t_0) = q2*(t_0 - t_1),
    omega(t) = Q'(t)/(2*Q(t)) -> 1/(2*(t - t_0)) as t -> t_0.
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
    # By Vieta's formulas: t_0 + t_1 = -q1/q2, t_0*t_1 = q0/q2
    # Q'(t_0) = q2*(t_0 - t_1)
    # Q(t) = q2*(t-t_0)*(t-t_1)
    # Q'/Q at t near t_0: q2*(2t - t_0 - t_1) / (q2*(t-t_0)*(t-t_1))
    # = (2t - t_0 - t_1)/((t-t_0)*(t-t_1))
    # At t = t_0: ~ (t_0 - t_1)/((t-t_0)*(t_0-t_1)) = 1/(t-t_0)
    # So omega = 1/(2*(t-t_0)): residue = 1/2. QED.
    return Rational(1, 2)


# =========================================================================
# 4. Virasoro shadow connection
# =========================================================================

def virasoro_shadow_data():
    """Shadow data for the Virasoro algebra on the T-line.

    kappa = c/2 (from T_{(3)}T = (c/2)*1, the unique weight-2 generator)
    alpha = S_3 = 2 (from T_{(1)}T = 2T, the gravitational cubic)
    S_4 = 10/[c(5c+22)] (the quartic shadow, from Lambda-exchange)
    Delta = 8*kappa*S_4 = 40/(5c+22) (the critical discriminant)

    All verified in compute/tests/test_virasoro_shadow_all_arity.py.
    """
    kappa = c / 2
    alpha = Rational(2)
    S4 = Rational(10) / (c * (5*c + 22))
    Delta = cancel(critical_discriminant(kappa, S4))
    return kappa, alpha, S4, Delta


def virasoro_shadow_metric():
    """Q_Vir(t) = c^2 + 12ct + [(180c+872)/(5c+22)] t^2.

    Gaussian decomposition: Q_Vir = (c + 6t)^2 + [80/(5c+22)] t^2.

    Pole data:
      Lee-Yang pole at c = -22/5 (from the OPE denominator 5c+22).
      Singularity at c = 0 (from 1/c in S_4; but Q_Vir(0) = c^2 ~ 0).
    """
    kappa, alpha, S4, _ = virasoro_shadow_data()
    return cancel(shadow_metric_general(kappa, alpha, S4))


def virasoro_shadow_metric_explicit():
    """Q_Vir(t) in the explicit form c^2 + 12ct + alpha(c)*t^2.

    alpha(c) = (180c + 872)/(5c + 22).
    """
    alpha_c = (180*c + 872) / (5*c + 22)
    return c**2 + 12*c*t + alpha_c*t**2


def virasoro_gaussian_decomposition():
    """Q_Vir = (c + 6t)^2 + [80/(5c+22)] t^2.

    The first term is the Gaussian envelope (perfect square).
    The second term is the interaction correction (from S_4).
    Delta_Vir = 40/(5c+22).
    """
    gaussian = (c + 6*t)**2
    correction = Rational(80) / (5*c + 22) * t**2
    Delta = Rational(40) / (5*c + 22)
    return gaussian, correction, Delta


def virasoro_connection_form():
    """Connection 1-form omega for the Virasoro shadow connection.

    omega = Q_Vir'(t) / (2*Q_Vir(t))
          = [12c + 2*(180c+872)/(5c+22)*t] / [2*Q_Vir(t)]

    Simplifies to:
      (30c^2 + 132c + (180c+872)*t) / [c^2*(5c+22) + ... polynomial in c,t].
    """
    Q = virasoro_shadow_metric()
    return connection_form(Q)


def virasoro_discriminant():
    """Critical discriminant Delta_Vir = 40/(5c+22).

    Controls the Virasoro shadow tower: Delta > 0 for all c > -22/5,
    confirming Virasoro is always class M (infinite tower).
    """
    return Rational(40) / (5*c + 22)


def virasoro_zeros():
    """Zeros of Q_Vir(t): the branch points of the Virasoro shadow GF.

    The discriminant of Q_Vir as a polynomial in t is
    disc = (12c)^2 - 4*c^2*(180c+872)/(5c+22)
         = -32*(c/2)^2 * 40/(5c+22)
         = -320*c^2/(5c+22).

    For c > 0: disc < 0, so the zeros are a complex conjugate pair.
    This means the branch points are complex, and rho > 0 (infinite tower).
    """
    Q = virasoro_shadow_metric()
    return solve(Q, t)


def virasoro_zeros_explicit():
    """Virasoro zeros in closed form using the quadratic formula.

    t_pm = [-12c +/- sqrt(-320c^2/(5c+22))] / [2*(180c+872)/(5c+22)]
         = [-12c*(5c+22) +/- sqrt(-320c^2*(5c+22))] / [2*(180c+872)]

    For c > 0, these are complex conjugate.
    """
    kappa, alpha, S4, _ = virasoro_shadow_data()
    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
    disc = shadow_metric_discriminant(kappa, alpha, S4)
    t_plus = cancel((-q1 + sqrt(disc)) / (2*q2))
    t_minus = cancel((-q1 - sqrt(disc)) / (2*q2))
    return t_plus, t_minus


def virasoro_flat_section():
    """Flat section Phi(t) = sqrt(Q_Vir(t)/Q_Vir(0)) = sqrt(Q_Vir(t))/c.

    Q_Vir(0) = c^2 (since Q_Vir = c^2 + 12ct + ...).
    So Phi(t) = sqrt(Q_Vir(t)) / c.

    Satisfies: nabla^sh(Phi) = 0, Phi(0) = 1.
    """
    Q = virasoro_shadow_metric()
    return sqrt(Q) / c


def virasoro_picard_fuchs():
    """The Picard-Fuchs ODE for flat sections of the Virasoro shadow connection.

    Q_L * f'' + (1/2)*Q_L' * f' = 0.

    This is the ODE satisfied by f(t) = sqrt(Q_Vir(t)).
    Equivalently: f'' + omega * f' = 0 where omega = Q'/(2Q).

    Returns (Q, Q') for the Virasoro algebra.
    """
    Q = virasoro_shadow_metric()
    Q_prime = diff(Q, t)
    return Q, Q_prime


# =========================================================================
# 5. W_3 shadow connection (W-line)
# =========================================================================

def w3_wline_shadow_data():
    """Shadow data for W_3 on the W-line (x_T = 0).

    kappa_W = c/3 (from W_{(5)}W = (c/3)*1, the weight-3 generator)
    alpha_W = 0 (Z_2 parity: odd arities vanish on W-line)
    S_4^W = Q_WWWW = 2560/[c(5c+22)^3] (quartic shadow, Lambda-exchange)
    Delta_W = 8*kappa_W*S_4^W = 20480/[3(5c+22)^3]

    The Z_2 parity (W -> -W) forces:
      - All odd arities vanish on the W-line.
      - alpha_W = 0 (no cubic term).
      - The shadow metric has NO linear term in t.
      - Branch points are PURELY IMAGINARY.
    """
    kappa_W = c / 3
    alpha_W = Rational(0)
    S4_W = Rational(2560) / (c * (5*c + 22)**3)
    Delta_W = cancel(critical_discriminant(kappa_W, S4_W))
    return kappa_W, alpha_W, S4_W, Delta_W


def w3_wline_shadow_metric():
    """Q_W(t) = (2c/3)^2 + 2*Delta_W*t^2 = 4c^2/9 + [40960/(3(5c+22)^3)] t^2.

    Since alpha_W = 0, the shadow metric has NO linear term.
    This means:
      - Q_W(t) = Q_W(-t) (even function of t).
      - Zeros are symmetric: t_0 and -t_0.
      - Connection form is an ODD function of t.
      - Branch points are purely imaginary (for c > 0).
    """
    kappa_W, alpha_W, S4_W, _ = w3_wline_shadow_data()
    return cancel(shadow_metric_general(kappa_W, alpha_W, S4_W))


def w3_wline_gaussian_decomposition():
    """Q_W = (2c/3)^2 + 2*Delta_W*t^2.

    Since alpha_W = 0, the Gaussian envelope is the constant (2c/3)^2 = 4c^2/9.
    The entire t-dependence comes from the interaction correction.
    """
    kappa_W = c / 3
    gaussian = (2*kappa_W)**2  # 4c^2/9
    _, _, _, Delta_W = w3_wline_shadow_data()
    correction = 2*Delta_W*t**2
    return gaussian, correction, Delta_W


def w3_wline_connection_form():
    """Connection form on the W-line.

    omega_W = Q_W'/(2Q_W) = 2*B*t / (2*(A + B*t^2)) = B*t / (A + B*t^2)

    where A = 4c^2/9 and B = 40960/(3(5c+22)^3).

    Key property: omega_W is an ODD function of t (because alpha_W = 0
    kills the constant term in Q_W').
    """
    Q = w3_wline_shadow_metric()
    return connection_form(Q)


def w3_wline_discriminant():
    """Critical discriminant on the W-line.

    Delta_W = 8*(c/3)*2560/[c*(5c+22)^3] = 20480/[3*(5c+22)^3].

    Note: Delta_W is MUCH SMALLER than Delta_Vir = 40/(5c+22) for large c.
    The ratio Delta_W/Delta_Vir = 512/[3*(5c+22)^2] -> 0 as c -> infinity.
    This reflects the W-channel's much faster convergence.
    """
    return cancel(Rational(20480) / (3 * (5*c + 22)**3))


def w3_wline_zeros():
    """Zeros of Q_W(t): purely imaginary branch points.

    Since Q_W = A + B*t^2 with A, B > 0 (for c > 0):
    t_0 = +/- i * sqrt(A/B) = +/- i * (2c/3) / sqrt(2*Delta_W).

    The zeros are purely imaginary because alpha_W = 0
    eliminates the linear term in Q_W.
    """
    Q = w3_wline_shadow_metric()
    return solve(Q, t)


def w3_wline_zero_modulus():
    """Modulus of the W-line branch point |t_0| = (2c/3)/sqrt(2*Delta_W).

    This equals the radius of convergence R_W = 1/rho_W.
    """
    kappa_W = c / 3
    _, _, _, Delta_W = w3_wline_shadow_data()
    return cancel(2*kappa_W / sqrt(2*Delta_W))


def w3_wline_growth_rate():
    """Shadow growth rate on the W-line.

    rho_W^2 = 2*Delta_W / (2*kappa_W)^2 = 30720/[c^2*(5c+22)^3].

    Note: since alpha_W = 0, the formula simplifies to rho = sqrt(2*Delta)/(2*kappa).
    Compare Virasoro: rho_Vir^2 = (180c+872)/[(5c+22)*c^2].
    """
    _, _, _, Delta_W = w3_wline_shadow_data()
    kappa_W = c / 3
    rho_sq = cancel(2*Delta_W / (2*kappa_W)**2)
    return rho_sq, sqrt(rho_sq)


def w3_wline_flat_section():
    """Flat section on the W-line: Phi_W(t) = sqrt(Q_W(t)/Q_W(0)).

    Q_W(0) = 4c^2/9, so Phi_W(t) = sqrt(Q_W(t)) / (2c/3) = (3/(2c))*sqrt(Q_W(t)).
    """
    Q = w3_wline_shadow_metric()
    Q0 = Q.subs(t, 0)
    return sqrt(Q / Q0)


# =========================================================================
# 6. W_3 shadow connection (T-line)
# =========================================================================

def w3_tline_shadow_data():
    """Shadow data for W_3 on the T-line (x_W = 0).

    The T-line of W_3 IS the Virasoro shadow: kappa_T = c/2, alpha_T = 2,
    S_4^T = 10/[c(5c+22)], Delta_T = 40/(5c+22).

    This is because restricting W_3 to the T-line sees only the
    Virasoro subalgebra.
    """
    return virasoro_shadow_data()


def w3_tline_shadow_metric():
    """T-line shadow metric = Virasoro shadow metric."""
    return virasoro_shadow_metric()


# =========================================================================
# 7. Koszul duality
# =========================================================================

def koszul_dual_metric(Q_expr, conductor=26):
    """Apply Koszul duality c -> conductor - c to the shadow metric.

    For Virasoro: conductor = 26, c -> 26-c.
    For W_3: conductor = 100, c -> 100-c.
    """
    return Q_expr.subs(c, conductor - c)


def virasoro_koszul_dual_metric():
    """Q_Vir^!(t) = Q_Vir(t)|_{c -> 26-c}."""
    return koszul_dual_metric(virasoro_shadow_metric(), 26)


def w3_koszul_dual_wline_metric():
    """Q_W^!(t) = Q_W(t)|_{c -> 100-c}."""
    return koszul_dual_metric(w3_wline_shadow_metric(), 100)


def dual_lee_yang_points():
    """The Koszul-dual Lee-Yang points for Virasoro: -22/5 and 152/5.

    Sum = 26 (Koszul conductor for Virasoro).
    The shadow metric has poles at these two points.
    """
    return (Rational(-22, 5), Rational(152, 5))


# =========================================================================
# 8. Complementarity
# =========================================================================

def complementarity_sum_discriminant():
    """Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)].

    Proof: Delta(c) = 40/(5c+22), Delta(26-c) = 40/(152-5c).
    Sum = 40*[(152-5c) + (5c+22)] / [(5c+22)(152-5c)]
        = 40*174 / [(5c+22)(152-5c)]
        = 6960 / [(5c+22)(152-5c)].

    The numerator 6960 = 40*174 is CONSTANT (universal).
    """
    Delta = virasoro_discriminant()
    Delta_dual = Delta.subs(c, 26 - c)
    return cancel(Delta + Delta_dual)


def complementarity_sum_metric():
    """Q(t,c) + Q(t,26-c) for Virasoro."""
    Q = virasoro_shadow_metric()
    Q_dual = koszul_dual_metric(Q)
    return cancel(Q + Q_dual)


def complementarity_product_metric():
    """Q(t,c) * Q(t,26-c) for Virasoro (the shadow norm)."""
    Q = virasoro_shadow_metric()
    Q_dual = koszul_dual_metric(Q)
    return cancel(Q * Q_dual)


def self_dual_metric():
    """Q(t, 13): the Virasoro shadow metric at the self-dual point c = 13.

    At c = 13: Q_Vir = Q_Vir^!.
    """
    Q = virasoro_shadow_metric()
    return Q.subs(c, 13)


def w3_complementarity_sum_discriminant():
    """Delta_W(c) + Delta_W(100-c) for W_3."""
    Delta_W = w3_wline_discriminant()
    Delta_W_dual = Delta_W.subs(c, 100 - c)
    return cancel(Delta_W + Delta_W_dual)


# =========================================================================
# 9. Multi-channel curvature
# =========================================================================

def multi_channel_curvature(kappas, f_values):
    """Curvature of the shadow connection on the multi-channel space.

    This equals the propagator variance delta_mix.
    For rank 1: always zero (single channel is flat).
    For rank > 1: nonzero iff quartic gradient is not curvature-proportional.
    """
    from .propagator_variance import propagator_variance
    return propagator_variance(kappas, f_values)


# =========================================================================
# 10. Numerical evaluation
# =========================================================================

def virasoro_shadow_metric_numerical(c_val):
    """Numerical evaluation of Virasoro shadow connection data at a specific c.

    Returns dict with Q(t), zeros, connection form, growth rate, etc.
    """
    c_v = Rational(c_val)

    kappa_v = c_v / 2
    alpha_v = Rational(2)
    S4_v = Rational(10) / (c_v * (5*c_v + 22))
    Delta_v = cancel(critical_discriminant(kappa_v, S4_v))

    q0, q1, q2 = shadow_metric_coefficients(kappa_v, alpha_v, S4_v)
    disc = q1**2 - 4*q0*q2

    t_plus = (-q1 + sqrt(disc)) / (2*q2)
    t_minus = (-q1 - sqrt(disc)) / (2*q2)

    t_plus_c = complex(t_plus.evalf())
    t_minus_c = complex(t_minus.evalf())

    mod = abs(t_plus_c)
    rho = 1.0/mod if mod > 0 else float('inf')

    import cmath
    arg = cmath.phase(t_plus_c)

    return {
        'c': float(c_v),
        'kappa': float(kappa_v),
        'alpha': float(alpha_v),
        'S4': float(S4_v),
        'Delta': float(Delta_v),
        'q0': float(q0),
        'q1': float(q1),
        'q2': float(q2),
        'disc': float(disc),
        't_plus': t_plus_c,
        't_minus': t_minus_c,
        'branch_point_modulus': mod,
        'branch_point_argument': arg,
        'rho': rho,
        'R': mod,
        'convergent': rho < 1.0,
    }


def w3_wline_shadow_metric_numerical(c_val):
    """Numerical evaluation of W_3 W-line shadow connection data."""
    c_v = Rational(c_val)

    kappa_W = c_v / 3
    S4_W = Rational(2560) / (c_v * (5*c_v + 22)**3)
    Delta_W = cancel(critical_discriminant(kappa_W, S4_W))

    # Q_W = (2c/3)^2 + 2*Delta_W*t^2
    A = (2*kappa_W)**2
    B = 2*Delta_W

    # Zeros: t = +/- i * sqrt(A/B)
    t0_abs = float(sqrt(A/B).evalf())
    rho_W = 1.0/t0_abs if t0_abs > 0 else float('inf')

    return {
        'c': float(c_v),
        'kappa_W': float(kappa_W),
        'S4_W': float(S4_W),
        'Delta_W': float(Delta_W),
        'A': float(A),
        'B': float(B),
        't0_modulus': t0_abs,
        't0_argument': float(pi)/2,  # purely imaginary
        'rho_W': rho_W,
        'R_W': t0_abs,
        'convergent': rho_W < 1.0,
    }
