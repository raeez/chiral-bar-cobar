r"""Shadow radius: the growth-rate invariant of the shadow Postnikov tower.

For a chirally Koszul algebra A of class M (Delta != 0), the shadow
tower coefficients S_r satisfy

    S_r ~ C(A) * rho(A)^r * r^{-5/2} * cos(r*theta + phi)

where rho(A) is the SHADOW GROWTH RATE (or shadow radius), defined as
the reciprocal of the radius of convergence of the weighted shadow
generating function H(t) = sum_{r>=2} r S_r t^r = t^2 sqrt(Q_L(t)).

The branch points of H are the zeros of the shadow metric Q_L(t).
Since Q_L is quadratic in t with discriminant -32 kappa^2 Delta,
the branch points are:

  - Complex conjugate pair when Delta > 0 (generic class M)
  - Real pair when Delta < 0 (rare, requires S_4 < 0)
  - Double root when Delta = 0 (class G or L, tower terminates)

UNIVERSAL FORMULA:
    rho(A) = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)

where kappa = S_2 (curvature), alpha = S_3 (cubic shadow),
Delta = 8*kappa*S_4 (critical discriminant).

For classes G and L: rho = 0 (tower terminates).
For class C: the quartic contact invariant lives on a separate
stratum; the single-line shadow radius is not defined.

CRITICAL CENTRAL CHARGE:
    rho(Vir_c) = 1  iff  5c^3 + 22c^2 - 180c - 872 = 0
    => c* approx 6.1243  (the unique real root > 0)

For c > c*: tower converges (rho < 1). Shadow amplitudes are summable.
For c < c*: tower diverges (rho > 1). Shadow amplitudes grow exponentially.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    rem:shadow-radius (higher_genus_modular_koszul.tex) -> upgraded to thm:shadow-radius
    cor:spectral-curve (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from sympy import (
    Rational, Symbol, cancel, pi, simplify,
    solve, sqrt, Abs,
)

c = Symbol('c')
k = Symbol('k')


# ===========================================================================
# 1. Shadow metric and branch points (general theory)
# ===========================================================================

def shadow_metric_coefficients(kappa, alpha, S4):
    """Coefficients of Q_L(t) = a0^2 + 2*a0*a1*t + (a1^2 + 2*a0*a2)*t^2.

    Returns (q0, q1, q2) such that Q_L(t) = q0 + q1*t + q2*t^2.
    """
    a0 = 2 * kappa
    a1 = 3 * alpha
    a2 = 4 * S4
    q0 = a0 ** 2  # 4*kappa^2
    q1 = 2 * a0 * a1  # 12*kappa*alpha
    q2 = a1 ** 2 + 2 * a0 * a2  # 9*alpha^2 + 16*kappa*S4
    return q0, q1, q2


def critical_discriminant(kappa, S4):
    """Delta = 8*kappa*S4: the critical discriminant."""
    return 8 * kappa * S4


def shadow_metric_discriminant(kappa, alpha, S4):
    """Discriminant of Q_L as polynomial in t.

    disc(Q_L) = q1^2 - 4*q0*q2 = -32*kappa^2 * Delta.

    Sign: negative when Delta > 0 (complex branch points, class M generic).
    """
    Delta = critical_discriminant(kappa, S4)
    return -32 * kappa ** 2 * Delta


def branch_points(kappa, alpha, S4):
    """Zeros of Q_L(t): the branch points of the shadow generating function.

    Returns (t_plus, t_minus) where t_pm = (-q1 +/- sqrt(disc)) / (2*q2).

    For Delta > 0: complex conjugate pair.
    For Delta = 0: double root (class G or L).
    For Delta < 0: two real roots.
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
    disc = q1 ** 2 - 4 * q0 * q2
    sq = sqrt(disc)
    t_plus = (-q1 + sq) / (2 * q2)
    t_minus = (-q1 - sq) / (2 * q2)
    return simplify(t_plus), simplify(t_minus)


def shadow_convergence_radius(kappa, alpha, S4):
    """Radius of convergence R = |nearest branch point| = 2|kappa|/sqrt(9*alpha^2 + 2*Delta).

    This is the distance from t=0 to the nearest zero of Q_L.
    Both branch points have the same modulus when they are complex conjugates
    (Delta > 0); for real branch points (Delta < 0), takes the minimum.
    """
    Delta = critical_discriminant(kappa, S4)
    denom = 9 * alpha ** 2 + 2 * Delta  # = 9*alpha^2 + 16*kappa*S4
    return 2 * Abs(kappa) / sqrt(denom)


def shadow_growth_rate(kappa, alpha, S4):
    """Shadow growth rate rho = 1/R = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|).

    The exponential growth rate of |S_r|.
    rho < 1: shadow tower converges (summable amplitudes).
    rho = 1: marginal (critical central charge).
    rho > 1: shadow tower diverges (exponential growth).
    """
    Delta = critical_discriminant(kappa, S4)
    return sqrt(9 * alpha ** 2 + 2 * Delta) / (2 * Abs(kappa))


def branch_point_argument(kappa, alpha, S4):
    """Argument theta of the nearest branch point t_0 in the complex plane.

    For Delta > 0 (complex conjugate pair), the branch points are at
    t_0 = (-6*kappa*alpha + i*sqrt(32*kappa^2*Delta)) / (2*(9*alpha^2 + 16*kappa*S4))
    and its conjugate.

    The oscillation in the asymptotic formula is cos(r*theta + phi)
    where theta = -arg(t_0).

    Returns (real_part, imag_part) of t_0 normalized by |t_0|,
    i.e., (cos(arg(t_0)), sin(arg(t_0))).
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
    # t_0 = (-q1 + i*sqrt(32*kappa^2*Delta)) / (2*q2)
    # Real part: -q1/(2*q2) = -6*kappa*alpha / (9*alpha^2 + 16*kappa*S4)
    # Imag part: sqrt(32*kappa^2*Delta) / (2*q2)
    real_part = -q1 / (2 * q2)
    Delta = critical_discriminant(kappa, S4)
    imag_part = sqrt(32 * kappa ** 2 * Delta) / (2 * q2)
    return simplify(real_part), simplify(imag_part)


# ===========================================================================
# 2. Virasoro shadow radius
# ===========================================================================

def virasoro_shadow_data():
    """Shadow data for Virasoro: kappa, alpha, S4, Delta as functions of c."""
    kappa = c / 2
    alpha = Rational(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    Delta = critical_discriminant(kappa, S4)
    return kappa, alpha, S4, simplify(Delta)


def virasoro_shadow_radius_formula():
    """Shadow growth rate rho(Vir_c) as a function of c.

    rho = sqrt((180c + 872) / (5c + 22)) / c.

    The expression 9*alpha^2 + 2*Delta:
      = 36 + 80/(5c+22)
      = (180c + 872) / (5c + 22).
    """
    kappa, alpha, S4, Delta = virasoro_shadow_data()
    numer_sq = 9 * alpha ** 2 + 2 * Delta
    numer_sq = cancel(numer_sq)  # (180c + 872)/(5c + 22)
    rho_sq = numer_sq / (4 * kappa ** 2)  # = (180c+872)/((5c+22)*c^2)
    return sqrt(rho_sq), cancel(rho_sq)


def virasoro_shadow_metric():
    """Q_Vir(t) = c^2 + 12c*t + alpha(c)*t^2 where alpha = (180c+872)/(5c+22).

    Gaussian decomposition: Q_Vir = (c + 6t)^2 + 80t^2/(5c+22).
    """
    t = Symbol('t')
    alpha_c = (180 * c + 872) / (5 * c + 22)
    Q = c ** 2 + 12 * c * t + alpha_c * t ** 2
    return Q, alpha_c


def virasoro_critical_central_charge():
    """The critical central charge c* where rho(Vir_{c*}) = 1.

    Solves: (180c + 872)/((5c + 22)*c^2) = 1
    i.e., 5c^3 + 22c^2 - 180c - 872 = 0.

    Returns the unique positive real root (approximately 6.1243).
    """
    poly = 5 * c ** 3 + 22 * c ** 2 - 180 * c - 872
    roots = solve(poly, c)
    # Filter for real positive roots
    real_positive = []
    for r in roots:
        try:
            val = complex(r.evalf())
            if abs(val.imag) < 1e-10 and val.real > 0:
                real_positive.append(r)
        except (TypeError, ValueError):
            continue
    return real_positive[0] if real_positive else None


def virasoro_branch_points_numerical(c_val):
    """Numerical branch points of Q_Vir at a specific central charge value.

    Returns dict with branch point locations, modulus, argument, and growth rate.
    """
    kappa_v = Rational(c_val) / 2
    alpha_v = Rational(2)
    S4_v = Rational(10) / (Rational(c_val) * (5 * Rational(c_val) + 22))

    q0, q1, q2 = shadow_metric_coefficients(kappa_v, alpha_v, S4_v)
    disc = q1 ** 2 - 4 * q0 * q2

    t_plus = (-q1 + sqrt(disc)) / (2 * q2)
    t_minus = (-q1 - sqrt(disc)) / (2 * q2)

    t_plus_c = complex(t_plus.evalf())
    t_minus_c = complex(t_minus.evalf())

    mod_plus = abs(t_plus_c)
    mod_minus = abs(t_minus_c)
    R = min(mod_plus, mod_minus)
    rho = 1.0 / R if R > 0 else float('inf')

    import cmath
    arg_plus = cmath.phase(t_plus_c)
    arg_minus = cmath.phase(t_minus_c)

    return {
        'c': c_val,
        't_plus': t_plus_c,
        't_minus': t_minus_c,
        'mod_plus': mod_plus,
        'mod_minus': mod_minus,
        'arg_plus': arg_plus,
        'arg_minus': arg_minus,
        'R': R,
        'rho': rho,
        'disc_sign': 'complex' if disc < 0 else 'real',
    }


def virasoro_koszul_dual_radius(c_val):
    """Shadow growth rate of Vir_{26-c} (the Koszul dual).

    rho(A!) = sqrt((180(26-c) + 872) / (5(26-c) + 22)) / (26-c)
            = sqrt((5552 - 180c) / (152 - 5c)) / (26 - c).
    """
    c_dual = 26 - Rational(c_val)
    kappa_d = c_dual / 2
    alpha_d = Rational(2)
    S4_d = Rational(10) / (c_dual * (5 * c_dual + 22))
    rho_sq = (9 * alpha_d ** 2 + 2 * critical_discriminant(kappa_d, S4_d)) / (4 * kappa_d ** 2)
    return float(sqrt(rho_sq).evalf()), float(c_dual)


# ===========================================================================
# 3. Shadow radius atlas for all standard families
# ===========================================================================

def shadow_radius_atlas():
    """Complete shadow radius atlas for the standard landscape.

    Returns a dictionary mapping family names to their shadow radius data.

    Classes G and L have rho = 0 (tower terminates, polynomial generating function).
    Class C escapes the single-line framework by stratum separation.
    Class M has rho > 0 (infinite tower, algebraic generating function).
    """
    atlas = {}

    # === CLASS G: Gaussian, depth 2, tower terminates ===

    atlas['Heisenberg'] = {
        'class': 'G',
        'depth': 2,
        'kappa': 'n/2 (rank n)',
        'alpha': 0,
        'S4': 0,
        'Delta': 0,
        'rho': 0,
        'R': float('inf'),
        'description': 'Abelian OPE, no nonlinear shadows',
    }

    atlas['Lattice V_Lambda'] = {
        'class': 'G',
        'depth': 2,
        'kappa': 'rank(Lambda)',
        'alpha': 0,
        'S4': 0,
        'Delta': 0,
        'rho': 0,
        'R': float('inf'),
        'description': 'Abelian OPE, kappa independent of cocycle',
    }

    # === CLASS L: Lie/tree, depth 3, tower terminates ===

    atlas['Affine V_k(g)'] = {
        'class': 'L',
        'depth': 3,
        'kappa': 'dim(g)(k+h^v)/(2h^v)',
        'alpha': '1 (Killing 3-cocycle)',
        'S4': 0,
        'Delta': 0,
        'rho': 0,
        'R': float('inf'),
        'description': 'Jacobi identity kills quartic; Delta=0, Q_L perfect square',
    }

    # === CLASS C: Contact, depth 4, escapes by stratum separation ===

    atlas['Beta-gamma'] = {
        'class': 'C',
        'depth': 4,
        'kappa': '-1 (at c=-2)',
        'alpha': 'nonzero (contact)',
        'S4': '-5/12',
        'Delta': 'N/A (charged stratum)',
        'rho': 'N/A (stratum separation)',
        'R': 'N/A',
        'description': 'Quartic contact invariant on charged stratum; single-line radius undefined',
    }

    # === CLASS M: Mixed, depth infinity, rho > 0 ===

    # Virasoro: parametric in c
    rho_formula, rho_sq = virasoro_shadow_radius_formula()

    c_star_expr = virasoro_critical_central_charge()
    c_star = float(c_star_expr.evalf()) if c_star_expr else None

    # Evaluate at special central charges
    vir_special = {}
    for name, c_val in [('c=1/2 (Ising)', Rational(1, 2)),
                         ('c=1 (free boson)', Rational(1)),
                         ('c=13 (self-dual)', Rational(13)),
                         ('c=25', Rational(25)),
                         ('c=26 (string)', Rational(26))]:
        rho_val = float(sqrt(rho_sq.subs(c, c_val)).evalf())
        R_val = 1.0 / rho_val if rho_val > 0 else float('inf')
        bp = virasoro_branch_points_numerical(c_val)
        vir_special[name] = {
            'rho': rho_val,
            'R': R_val,
            'convergent': rho_val < 1,
            'branch_arg': bp['arg_plus'],
        }

    atlas['Virasoro Vir_c'] = {
        'class': 'M',
        'depth': float('inf'),
        'kappa': 'c/2',
        'alpha': '2',
        'S4': '10/(c(5c+22))',
        'Delta': '40/(5c+22)',
        'rho_formula': 'sqrt((180c+872)/((5c+22)*c^2))',
        'rho_squared': str(rho_sq),
        'critical_c': c_star,
        'special_values': vir_special,
        'description': 'Infinite tower; rho(c) < 1 for c > c* ~ 6.12 (convergent)',
    }

    # W_3: two lines (T-line = Virasoro, W-line = even arities)
    # W-line: kappa_W = c/3, alpha_W = 0 (odd vanish), S4_W = 2560/(c(5c+22)^3)
    kap_W = Rational(1, 3)  # kappa_W / c
    S4_W_expr = Rational(2560) / (c * (5 * c + 22) ** 3)
    Delta_W = 8 * (c / 3) * S4_W_expr
    rho_sq_W = (2 * Delta_W) / (4 * (c / 3) ** 2)  # alpha=0
    rho_sq_W = cancel(rho_sq_W)

    w3_special = {}
    for name, c_val in [('c=2', Rational(2)), ('c=13', Rational(13))]:
        val = float(sqrt(rho_sq_W.subs(c, c_val)).evalf())
        w3_special[name] = {'rho_W': val}

    atlas['W_3'] = {
        'class': 'M',
        'depth': float('inf'),
        'kappa_T': 'c/2 (T-line = Virasoro)',
        'kappa_W': 'c/3',
        'rho_T': '= Virasoro rho',
        'rho_W_formula': str(rho_sq_W),
        'special_values': w3_special,
        'description': 'T-line shadow radius = Virasoro; W-line has separate even-arity radius',
    }

    return atlas


# ===========================================================================
# 4. Asymptotic transfer theorem
# ===========================================================================

def asymptotic_data(kappa_val, alpha_val, S4_val, max_r=32):
    """Compute exact shadow coefficients and compare with asymptotic prediction.

    The transfer theorem (Flajolet-Sedgewick VI.1) gives:
        S_r ~ A * rho^r * r^{-5/2} * cos(r*theta + phi)

    where rho = shadow growth rate, theta = oscillation phase,
    and A, phi are computable from the branch point residue.

    Returns comparison data for validation.
    """
    from .sigma_ring_finite_generation import virasoro_shadow_coefficients

    S = virasoro_shadow_coefficients(max_r)

    # Compute rho
    Delta = critical_discriminant(kappa_val, S4_val)
    denom = 9 * alpha_val ** 2 + 2 * Delta
    rho_exact = sqrt(denom) / (2 * Abs(kappa_val))
    rho_float = float(rho_exact.evalf())

    # Compute branch points
    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, S4_val)
    disc = q1 ** 2 - 4 * q0 * q2
    t0 = (-q1 + sqrt(disc)) / (2 * q2)
    t0_c = complex(t0.evalf())

    import cmath
    theta = -cmath.phase(t0_c)  # oscillation phase

    # Observed ratios |S_{r+1}/S_r|
    ratios = []
    for r in range(3, max_r + 1):
        Sr = float(S[r].subs(c, kappa_val * 2).evalf())  # c = 2*kappa for Vir
        Sr_prev = float(S[r - 1].subs(c, kappa_val * 2).evalf())
        if abs(Sr_prev) > 1e-50:
            ratios.append((r, abs(Sr / Sr_prev)))

    return {
        'rho': rho_float,
        'theta': theta,
        'R': 1.0 / rho_float if rho_float > 0 else float('inf'),
        'branch_point': t0_c,
        'observed_ratios': ratios,
        'predicted_ratio': rho_float,  # limiting ratio |S_{r+1}/S_r| -> rho
        'exponent': -5 / 2,  # r^{-5/2} correction
    }


# ===========================================================================
# 5. DS depth-increase quantification
# ===========================================================================

def ds_shadow_radius_comparison(N_val, c_val=None):
    """Compare shadow radii: sl_N (class L, rho=0) vs W_N (class M, rho>0).

    DS reduction takes rho = 0 -> rho > 0: the GHOST SECTOR creates
    the nonzero shadow radius. This quantifies the depth-increase
    obstruction.

    For W_N at central charge c:
        rho_{W_N,T}(c) = rho_Vir(c)  (T-line = Virasoro shadow radius)
    """
    # sl_N: class L, rho = 0
    sl_data = {
        'class': 'L',
        'depth': 3,
        'rho': 0,
    }

    # W_N on T-line: identical to Virasoro
    if c_val is not None:
        c_v = Rational(c_val)
        rho_sq = (180 * c_v + 872) / ((5 * c_v + 22) * c_v ** 2)
        rho_T = float(sqrt(rho_sq).evalf())
    else:
        rho_T = None

    wn_data = {
        'class': 'M',
        'depth': float('inf'),
        'rho_T_line': rho_T,
        'mechanism': 'Ghost sector creates quartic (and all higher arities) via BRST',
    }

    return {'sl_N': sl_data, f'W_{N_val}': wn_data}


# ===========================================================================
# 6. Koszul duality and shadow radius
# ===========================================================================

def virasoro_koszul_product(c_val):
    """Product rho(Vir_c) * rho(Vir_{26-c}).

    Under Koszul duality Vir_c <-> Vir_{26-c}, the shadow radii are
    related but NOT reciprocal in general.

    At c = 13 (self-dual): rho(A) = rho(A!).
    """
    c_v = Rational(c_val)
    c_dual = 26 - c_v
    rho_sq = (180 * c_v + 872) / ((5 * c_v + 22) * c_v ** 2)
    rho_sq_d = (180 * c_dual + 872) / ((5 * c_dual + 22) * c_dual ** 2)
    rho = float(sqrt(rho_sq).evalf())
    rho_d = float(sqrt(rho_sq_d).evalf())
    return {
        'c': float(c_v),
        'c_dual': float(c_dual),
        'rho': rho,
        'rho_dual': rho_d,
        'product': rho * rho_d,
        'self_dual': abs(rho - rho_d) < 1e-10,
    }


# ===========================================================================
# 7. Shadow radius table (numerical atlas)
# ===========================================================================

def shadow_radius_table():
    """Numerical shadow radius table for the Virasoro family.

    Columns: c, rho(c), R(c) = 1/rho(c), convergent?, arg(t_0)/pi.
    """
    rows = []
    c_values = [
        Rational(1, 2), Rational(7, 10), Rational(4, 5),
        Rational(1), Rational(2), Rational(4),
        Rational(6), Rational(13), Rational(25), Rational(26),
    ]
    for c_v in c_values:
        rho_sq = (180 * c_v + 872) / ((5 * c_v + 22) * c_v ** 2)
        rho = float(sqrt(rho_sq).evalf())
        R = 1.0 / rho if rho > 0 else float('inf')

        # Branch point argument
        bp = virasoro_branch_points_numerical(c_v)

        rows.append({
            'c': str(c_v),
            'c_float': float(c_v),
            'rho': rho,
            'R': R,
            'convergent': rho < 1.0,
            'arg_over_pi': bp['arg_plus'] / float(pi),
        })
    return rows


# ===========================================================================
# 8. Critical central charge analysis
# ===========================================================================

def critical_central_charge_properties():
    """Properties of the critical central charge c* where rho = 1.

    The cubic 5c^3 + 22c^2 - 180c - 872 = 0 has three roots.
    Only one is real and positive: c* ~ 6.1243.

    Physical significance: c* separates summable (c > c*) from
    non-summable (c < c*) shadow towers. All unitary minimal models
    (c < 1) have divergent shadow towers. The string theory value
    c = 26 has a strongly convergent tower (rho ~ 0.23).
    """
    poly = 5 * c ** 3 + 22 * c ** 2 - 180 * c - 872
    all_roots = solve(poly, c)
    result = {'polynomial': '5c^3 + 22c^2 - 180c - 872',
              'roots': []}
    for r in all_roots:
        val = complex(r.evalf())
        result['roots'].append({
            'exact': str(r),
            'numerical': val,
            'is_real': abs(val.imag) < 1e-10,
            'is_positive': val.real > 0 and abs(val.imag) < 1e-10,
        })
    # The critical one
    c_star = [r for r in result['roots'] if r['is_positive']]
    if c_star:
        result['c_star'] = c_star[0]['numerical'].real
    return result


if __name__ == '__main__':
    print("=" * 70)
    print("SHADOW RADIUS ATLAS")
    print("=" * 70)

    # Critical central charge
    cc = critical_central_charge_properties()
    print(f"\nCritical central charge c*: {cc.get('c_star', 'N/A'):.6f}")
    print(f"Polynomial: {cc['polynomial']} = 0")

    # Virasoro table
    print("\nVirasoro shadow radius table:")
    print(f"  {'c':>8s}  {'rho':>10s}  {'R':>10s}  {'conv?':>6s}  {'arg/pi':>8s}")
    print("  " + "-" * 50)
    table = shadow_radius_table()
    for row in table:
        conv = 'YES' if row['convergent'] else 'NO'
        print(f"  {row['c']:>8s}  {row['rho']:10.6f}  {row['R']:10.6f}  {conv:>6s}  {row['arg_over_pi']:8.4f}")

    # Koszul duality
    print("\nKoszul duality rho(c) vs rho(26-c):")
    for c_v in [1, 5, 13, 25]:
        kd = virasoro_koszul_product(c_v)
        sd = "*" if kd['self_dual'] else ""
        print(f"  c={c_v:2d}: rho={kd['rho']:.6f}, rho!={kd['rho_dual']:.6f}, "
              f"product={kd['product']:.6f} {sd}")

    # DS comparison
    print("\nDS depth-increase (sl_3 -> W_3):")
    ds = ds_shadow_radius_comparison(3, 2)
    for key, val in ds.items():
        print(f"  {key}: {val}")
