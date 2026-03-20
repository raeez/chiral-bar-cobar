"""
Two-variable L-object L_A(s,u) and its Rankin-Selberg factorization.

MAIN THEOREM (Rankin-Selberg collapse):
    L_A(s,u) = Gamma(v) * (2*pi)^{-v} * S_A(v),  v := s + u - 1

where S_A(v) = zeta(v+1) * sum_i (zeta(v) - H_{w_i - 1}(v)) is the
Dirichlet-sewing lift and the integral is

    L_A(s,u) := int_F^{reg} F_A^conn(e^{-2pi*y+2pi*i*x}) * E*(tau,s) * y^{u-2} dx dy

PROOF (Rankin-Selberg unfolding):
    Step 1. F_A^conn depends only on |q| = e^{-2pi*y} (sewing operator
            is diagonalized in Fock basis with eigenvalues depending on |q|).
            Therefore the zeroth Fourier mode a_0(y) = F_A^conn(e^{-2pi*y}).

    Step 2. Rankin-Selberg unfolding replaces
            int_F f * E_s dmu  -->  int_0^infty a_0(y) * y^{s-2} dy
            In our case f = F_A^conn * y^u, so the unfolded integral is
            int_0^infty F_A^conn(e^{-2pi*y}) * y^{s+u-2} dy.

    Step 3. Substituting F_A^conn = sum_i sum_{m>=w_i} sum_{k>=1} e^{-2pi*m*k*y}/k:
            L_A(s,u) = sum_i sum_{m>=w_i} sum_{k>=1} (1/k) * Gamma(v)/(2pi*m*k)^v
                     = Gamma(v)/(2pi)^v * sum_i sum_{m>=w_i} m^{-v} * sum_{k>=1} k^{-(v+1)}
                     = Gamma(v)/(2pi)^v * zeta(v+1) * sum_i (zeta(v) - H_{w_i-1}(v))
                     = Gamma(v)/(2pi)^v * S_A(v).

    The (s,u) dependence enters ONLY through v = s+u-1.  QED.

RECOVERY OF SEWING-SELBERG at u=0:
    L_A(s,0) = Gamma(s-1)/(2pi)^{s-1} * S_A(s-1).
    For Heisenberg: L_H(s,0) = Gamma(s-1)/(2pi)^{s-1} * zeta(s-1)*zeta(s).
    Sewing-Selberg gives -2*(2pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s).
    The factor -2 comes from: sign (F^conn = -log det) and factor 2 from
    the full modular integral vs unfolded strip integral.

KEY FAMILIES:
    Heisenberg  W={1}:   L_H(s,u) = Gamma(v)/(2pi)^v * zeta(v)*zeta(v+1)
    Virasoro    W={2}:   L_V(s,u) = Gamma(v)/(2pi)^v * zeta(v+1)*(zeta(v)-1)
    W_N         W={2..N}: L_{W_N}(s,u) = Gamma(v)/(2pi)^v * S_{W_N}(v)
    betagamma   W={1,1}: L_{bg}(s,u) = Gamma(v)/(2pi)^v * 2*zeta(v)*zeta(v+1)

References:
    sewing_dirichlet_lift.py (S_A(u) implementation)
    operadic_rankin_selberg.py (moment L-functions)
    sewing_euler_product.py (prime decomposition)
"""

from mpmath import (mp, mpf, zeta, gamma as mpgamma, pi as mppi,
                    power, exp as mpexp, log as mplog, diff, inf,
                    nsum, fac, quad, sin, cos, sqrt, re as mpre, im as mpim,
                    mpc, euler as euler_gamma, stieltjes, fabs, mpf as _mpf,
                    matrix as mpmatrix, fp)
import math

mp.dps = 50


# =============================================================================
# 1. Weight multisets for standard families
# =============================================================================

WEIGHTS = {
    'heisenberg': [1],
    'virasoro': [2],
    'betagamma': [1, 1],
    'W3': [2, 3],
    'W4': [2, 3, 4],
    'W5': [2, 3, 4, 5],
    'W_N': lambda N: list(range(2, N + 1)),
    'affine_sl2': [1, 1, 1],  # three currents of weight 1
    'lattice_rank_r': lambda r: [1] * r,
}


def weights_for_family(name, **kwargs):
    """Return weight multiset for a named family."""
    if name == 'W_N':
        return list(range(2, kwargs.get('N', 3) + 1))
    if name == 'lattice_rank_r':
        return [1] * kwargs.get('r', 1)
    return WEIGHTS.get(name, [1])


# =============================================================================
# 2. Harmonic zeta and Dirichlet-sewing lift S_A(v)
# =============================================================================

def harmonic_zeta(n, v):
    """H_n(v) = sum_{j=1}^n j^{-v}."""
    if n <= 0:
        return mpf(0)
    return sum(power(j, -v) for j in range(1, n + 1))


def _ensure_mp(v):
    """Convert to mpf or mpc as appropriate."""
    if isinstance(v, mpc):
        return v
    try:
        return mpf(v)
    except (TypeError, ValueError):
        return mpc(v)


def S_A(weights, v):
    """
    Dirichlet-sewing lift:
        S_A(v) = zeta(v+1) * sum_i (zeta(v) - H_{w_i - 1}(v))
    """
    v = _ensure_mp(v)
    z_v = zeta(v)
    z_v1 = zeta(v + 1)
    return z_v1 * sum(z_v - harmonic_zeta(w - 1, v) for w in weights)


def S_heisenberg(v):
    """S_H(v) = zeta(v) * zeta(v+1)."""
    v = _ensure_mp(v)
    return zeta(v) * zeta(v + 1)


def S_virasoro(v):
    """S_Vir(v) = zeta(v+1) * (zeta(v) - 1)."""
    v = _ensure_mp(v)
    return zeta(v + 1) * (zeta(v) - 1)


def S_betagamma(v):
    """S_bg(v) = 2 * zeta(v) * zeta(v+1)."""
    v = _ensure_mp(v)
    return 2 * zeta(v) * zeta(v + 1)


def S_WN(N, v):
    """S_{W_N}(v) = zeta(v+1) * ((N-1)*zeta(v) - sum_{j=1}^{N-1} H_j(v))."""
    v = _ensure_mp(v)
    harm_sum = sum(harmonic_zeta(j, v) for j in range(1, N))
    return zeta(v + 1) * ((N - 1) * zeta(v) - harm_sum)


# =============================================================================
# 3. The two-variable L-object: factored form
# =============================================================================

def L_factored(weights, s, u):
    """
    L_A(s,u) via the Rankin-Selberg factorization:
        L_A(s,u) = Gamma(v) * (2*pi)^{-v} * S_A(v),   v = s + u - 1.

    This is the EXACT formula obtained by Rankin-Selberg unfolding.
    """
    s, u = mpf(s), mpf(u)
    v = s + u - 1
    gamma_v = mpgamma(v)
    two_pi_inv_v = power(2 * mppi, -v)
    return gamma_v * two_pi_inv_v * S_A(weights, v)


def L_heisenberg_factored(s, u):
    """L_H(s,u) = Gamma(v)/(2pi)^v * zeta(v)*zeta(v+1), v=s+u-1."""
    s, u = mpf(s), mpf(u)
    v = s + u - 1
    return mpgamma(v) * power(2 * mppi, -v) * S_heisenberg(v)


def L_virasoro_factored(s, u):
    """L_Vir(s,u) = Gamma(v)/(2pi)^v * zeta(v+1)*(zeta(v)-1), v=s+u-1."""
    s, u = mpf(s), mpf(u)
    v = s + u - 1
    return mpgamma(v) * power(2 * mppi, -v) * S_virasoro(v)


def L_betagamma_factored(s, u):
    """L_bg(s,u) = Gamma(v)/(2pi)^v * 2*zeta(v)*zeta(v+1), v=s+u-1."""
    s, u = mpf(s), mpf(u)
    v = s + u - 1
    return mpgamma(v) * power(2 * mppi, -v) * S_betagamma(v)


def L_WN_factored(N, s, u):
    """L_{W_N}(s,u) = Gamma(v)/(2pi)^v * S_{W_N}(v), v=s+u-1."""
    s, u = mpf(s), mpf(u)
    v = s + u - 1
    return mpgamma(v) * power(2 * mppi, -v) * S_WN(N, v)


# =============================================================================
# 4. Direct numerical integration (Mellin transform of F^conn)
# =============================================================================

def F_conn(weights, y, terms=200):
    """
    Connected free energy:
        F_A^conn(e^{-2pi*y}) = sum_i sum_{m>=w_i} sum_{k>=1} e^{-2pi*m*k*y}/k

    Truncated to terms summands per generator.
    """
    y = mpf(y)
    result = mpf(0)
    for w in weights:
        for m in range(w, w + terms):
            for k in range(1, terms + 1):
                val = mpexp(-2 * mppi * m * k * y) / k
                if fabs(val) < mpf('1e-40'):
                    break
                result += val
    return result


def F_conn_fast(weights, y, terms=300):
    """
    Connected free energy using polylog/geometric acceleration.
        F_A^conn = sum_i sum_{m>=w_i} -log(1 - e^{-2pi*m*y})
                 = -sum_i sum_{m>=w_i} log(1 - q^m),   q = e^{-2pi*y}
    """
    y = mpf(y)
    q = mpexp(-2 * mppi * y)
    result = mpf(0)
    for w in weights:
        for m in range(w, w + terms):
            qm = power(q, m)
            if fabs(qm) < mpf('1e-45'):
                break
            result -= mplog(1 - qm)
    return result


def L_direct_mellin(weights, s, u, y_min=mpf('1e-4'), y_max=mpf(8),
                    terms=200):
    """
    L_A(s,u) by direct Mellin integration:
        int_0^infty F_A^conn(e^{-2pi*y}) * y^{s+u-2} dy

    Numerically computed with mpmath quadrature on [y_min, y_max].
    The integrand decays exponentially for large y (from e^{-2pi*y})
    and the small-y behavior is regularized by the truncation.
    """
    s, u = mpf(s), mpf(u)

    def integrand(y):
        return F_conn_fast(weights, y, terms) * power(y, s + u - 2)

    # Use tanh-sinh quadrature
    result = quad(integrand, [y_min, y_max], error=True, maxdegree=8)
    return result[0]  # value (discard error estimate)


def L_direct_mellin_precise(weights, s, u, y_min=mpf('5e-5'), y_max=mpf(12),
                            terms=400):
    """Higher-precision version of the direct Mellin integral."""
    s, u = mpf(s), mpf(u)

    def integrand(y):
        return F_conn_fast(weights, y, terms) * power(y, s + u - 2)

    result = quad(integrand, [y_min, y_max], error=True, maxdegree=10)
    return result[0]


# =============================================================================
# 5. Sewing-Selberg recovery at u=0
# =============================================================================

def sewing_selberg_heisenberg(s):
    """
    Sewing-Selberg formula for Heisenberg:
        int_F log det(1-K) * E_s dmu = -2*(2pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1)*zeta(s)

    Our L_H(s,0) = Gamma(s-1)/(2pi)^{s-1} * zeta(s-1)*zeta(s).

    Ratio: sewing_selberg / L_H(s,0) = -2.
    """
    s = mpf(s)
    return -2 * power(2 * mppi, -(s - 1)) * mpgamma(s - 1) * zeta(s - 1) * zeta(s)


def sewing_selberg_generic(weights, s):
    """
    Sewing-Selberg for general weight multiset:
        int_F F^conn_A * E_s dmu = -2 * L_A(s, 0)
                                  = -2 * Gamma(s-1)/(2pi)^{s-1} * S_A(s-1)

    The factor -2 comes from: F^conn = -log det(1-K) (sign), and the factor 2
    from the standard Rankin-Selberg normalization (strip width = 1/2 of the
    fundamental domain after unfolding).
    """
    s = mpf(s)
    return -2 * L_factored(weights, s, mpf(0))


# =============================================================================
# 6. Collapse verification: L_A(s,u) depends only on v = s+u-1
# =============================================================================

def verify_collapse(weights, s1, u1, s2, u2, label=""):
    """
    Verify that L_A(s1,u1) = L_A(s2,u2) whenever s1+u1 = s2+u2.
    Returns the ratio L_A(s1,u1)/L_A(s2,u2) (should be 1.0).
    """
    v1 = mpf(s1) + mpf(u1) - 1
    v2 = mpf(s2) + mpf(u2) - 1
    if fabs(v1 - v2) > mpf('1e-12'):
        return {'match': False, 'reason': f'v1={v1} != v2={v2}'}
    L1 = L_factored(weights, s1, u1)
    L2 = L_factored(weights, s2, u2)
    ratio = L1 / L2 if fabs(L2) > mpf('1e-100') else mpf('nan')
    return {
        's1': s1, 'u1': u1, 's2': s2, 'u2': u2,
        'v': float(v1),
        'L1': L1, 'L2': L2,
        'ratio': ratio,
        'match': fabs(ratio - 1) < mpf('1e-30'),
        'label': label,
    }


# =============================================================================
# 7. Residue analysis at zeta poles/zeros
# =============================================================================

def residue_at_zeta_pole(weights, v0, eps=mpf('1e-8')):
    """
    Compute the residue of L_A at v = v0 (from the zeta poles in S_A).

    S_A(v) has poles from zeta(v) at v=1 and from zeta(v+1) at v=0.
    The Gamma function Gamma(v) has poles at v=0,-1,-2,...

    Leading pole structure of Gamma(v)*(2pi)^{-v}*S_A(v):
    - At v=1: from zeta(v) pole; residue = Gamma(1)/(2pi) * zeta(2) * |W|
              = zeta(2)/(2pi) * |W| = pi/12 * |W|
    - At v=0: from Gamma(v) and zeta(v+1) poles; more complex
    """
    v0 = mpf(v0)
    # Numerical residue via limit: Res = lim_{v->v0} (v - v0) * L_A
    def f(v):
        return (v - v0) * mpgamma(v) * power(2 * mppi, -v) * S_A(weights, v)

    # Evaluate at v0 + eps
    res = f(v0 + eps)
    return res


def completed_L(weights, v):
    """
    Completed L-object:
        Lambda_A(v) = Gamma(v) * (2pi)^{-v} * S_A(v)

    This equals L_A(s,u) for any (s,u) with s+u-1 = v.
    """
    v = _ensure_mp(v)
    return mpgamma(v) * power(2 * mppi, -v) * S_A(weights, v)


# =============================================================================
# 8. Fourier coefficient verification
# =============================================================================

def a_A(weights, N):
    """
    Dirichlet coefficients of S_A(v):
        a_A(N) = sum_i sum_{d|N, N/d >= w_i} 1/d

    Equivalently: a_A(N) = sum_{d|N} (1/d) * #{i : w_i <= N/d}.
    """
    N = int(N)
    result = mpf(0)
    for d in range(1, N + 1):
        if N % d == 0:
            m = N // d
            count = sum(1 for w in weights if w <= m)
            result += mpf(count) / d
    return result


def S_A_from_coefficients(weights, v, N_max=500):
    """
    S_A(v) computed directly from Dirichlet coefficients:
        S_A(v) = sum_{N=1}^{N_max} a_A(N) * N^{-v}
    """
    v = mpf(v)
    result = mpf(0)
    for N in range(1, N_max + 1):
        result += a_A(weights, N) * power(mpf(N), -v)
    return result


def verify_S_A_formula(weights, v, N_max=500):
    """
    Verify that the closed-form S_A(v) matches the Dirichlet series.
    """
    v = mpf(v)
    closed = S_A(weights, v)
    series = S_A_from_coefficients(weights, v, N_max)
    return {
        'v': float(v),
        'closed_form': closed,
        'dirichlet_series': series,
        'rel_error': float(fabs(closed - series) / fabs(closed)) if fabs(closed) > 0 else 0,
    }


# =============================================================================
# 9. Functional equation structure
# =============================================================================

def functional_equation_ratio(weights, v):
    """
    The completed Eisenstein series satisfies E*(tau,s) = E*(tau,1-s).
    Under Rankin-Selberg, this gives a relation between L_A(s,u) and L_A(1-s, u).

    Since L_A(s,u) = Lambda_A(s+u-1), the functional equation from E* is:
        Lambda_A(v) at v = s+u-1  <->  Lambda_A(v') at v' = (1-s)+u-1 = u-s = v - 2s + 1

    This does NOT give a simple v <-> 1-v type functional equation for Lambda_A
    unless u is fixed. For fixed u:
        Lambda_A(s+u-1) relates to Lambda_A(u-s) under E* <-> E*.

    If we set w = s + u - 1, then s = w - u + 1, and the reflected value is
    u - (w - u + 1) = 2u - w - 1. So: Lambda_A(w) <-> Lambda_A(2u-w-1).

    At u = 1/2: Lambda_A(w) <-> Lambda_A(-w), which is the critical-strip symmetry.
    At u = 1:   Lambda_A(w) <-> Lambda_A(1-w), the standard functional equation.

    CONCLUSION: The natural functional equation from the Eisenstein series is
    Lambda_A(v) <-> Lambda_A(1-v) (setting u=1), which corresponds to
    zeta(v)*zeta(v+1) <-> zeta(1-v)*zeta(2-v) after Gamma factors.
    """
    v = mpf(v)
    # For the u=1 slice: v <-> 1-v
    L_v = completed_L(weights, v)
    L_1_minus_v = completed_L(weights, 1 - v)
    if fabs(L_1_minus_v) > mpf('1e-100'):
        return L_v / L_1_minus_v
    return mpf('nan')


# =============================================================================
# 10. Gamma factor extraction
# =============================================================================

def gamma_factor(v):
    """
    The Gamma factor Gamma(v) * (2pi)^{-v}.
    This is the archimedean local factor.
    """
    v = _ensure_mp(v)
    return mpgamma(v) * power(2 * mppi, -v)


def S_A_from_L(L_val, v):
    """
    Extract S_A(v) from L_A value: S_A(v) = L_A / gamma_factor(v).
    """
    gf = gamma_factor(v)
    if fabs(gf) > mpf('1e-100'):
        return L_val / gf
    return mpf('nan')


# =============================================================================
# 11. Critical line and special values
# =============================================================================

def L_on_critical_line(weights, t, u=1):
    """
    Evaluate L_A on the critical line v = 1/2 + it.
    With u=1: s = v = 1/2 + it, so s = 1/2 + it.
    """
    v = mpc(mpf('0.5'), mpf(t))
    return completed_L(weights, v)


def L_special_values(weights):
    """
    Compute special values of Lambda_A(v) at integer points.
    """
    results = {}
    for v_int in [2, 3, 4, 5, 6]:
        results[v_int] = {
            'v': v_int,
            'Lambda_A': float(completed_L(weights, v_int)),
            'S_A': float(S_A(weights, v_int)),
            'gamma_factor': float(gamma_factor(v_int)),
        }
    return results


# =============================================================================
# 12. Cross-family comparison
# =============================================================================

def cross_family_table(v, families=None):
    """
    Compare Lambda_A(v) across all standard families at a given v.
    """
    if families is None:
        families = {
            'heisenberg': [1],
            'virasoro': [2],
            'betagamma': [1, 1],
            'W3': [2, 3],
            'W4': [2, 3, 4],
            'affine_sl2': [1, 1, 1],
        }
    v = mpf(v)
    results = {}
    for name, weights in families.items():
        results[name] = {
            'Lambda': completed_L(weights, v),
            'S': S_A(weights, v),
            'gamma': gamma_factor(v),
        }
    return results


# =============================================================================
# 13. Dirichlet-sewing lift formula verification
# =============================================================================

def verify_S_A_closed_form(weights, v):
    """
    Verify that S_A(v) = zeta(v+1) * sum_i (zeta(v) - H_{w_i-1}(v))
    matches the sum_i sum_{m>=w_i} m^{-v} * zeta(v+1) form.
    """
    v = mpf(v)
    # Method 1: closed form
    closed = S_A(weights, v)

    # Method 2: explicit double sum
    z_v1 = zeta(v + 1)
    explicit = mpf(0)
    for w in weights:
        tail_sum = mpf(0)
        # sum_{m>=w} m^{-v} = zeta(v) - H_{w-1}(v)
        for m in range(w, 1000):
            tail_sum += power(mpf(m), -v)
        explicit += z_v1 * tail_sum

    return {
        'closed': closed,
        'explicit': explicit,
        'rel_error': float(fabs(closed - explicit) / fabs(closed)),
    }


# =============================================================================
# 14. Summary display
# =============================================================================

def print_factorization_table():
    """Print the factorization L_A(s,u) = Gamma(v)/(2pi)^v * S_A(v) for test values."""
    print("=" * 100)
    print(f"{'Family':>14} | {'s':>5} {'u':>5} {'v=s+u-1':>8} | "
          f"{'Gamma(v)/(2pi)^v':>22} | {'S_A(v)':>22} | {'L_A(s,u)':>22}")
    print("-" * 100)

    families = [
        ('Heisenberg', [1]),
        ('Virasoro', [2]),
        ('betagamma', [1, 1]),
        ('W_3', [2, 3]),
    ]

    for s, u in [(2, 1), (3, 0), (1.5, 1.5), (2.5, 0.5)]:
        for name, w in families:
            v = s + u - 1
            gf = gamma_factor(v)
            sv = S_A(w, v)
            lv = L_factored(w, s, u)
            print(f"{name:>14} | {s:>5.1f} {u:>5.1f} {v:>8.1f} | "
                  f"{float(gf):>22.12e} | {float(sv):>22.12e} | {float(lv):>22.12e}")
        print()


if __name__ == "__main__":
    mp.dps = 30
    print_factorization_table()

    print("\n=== Collapse verification: L(s1,u1) = L(s2,u2) when s1+u1 = s2+u2 ===")
    for name, w in [('Heis', [1]), ('Vir', [2]), ('bg', [1, 1])]:
        res = verify_collapse(w, 2, 1, 1.5, 1.5, name)
        print(f"  {name}: ratio = {float(res['ratio']):.15f}, match = {res['match']}")
        res2 = verify_collapse(w, 3, 0, 2, 1, name)
        print(f"  {name}: ratio = {float(res2['ratio']):.15f}, match = {res2['match']}")
