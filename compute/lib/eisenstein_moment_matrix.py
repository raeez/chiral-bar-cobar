"""
Eisenstein moment matrix for the shadow obstruction tower and genus-1 modular structure.

TWO LAYERS OF STRUCTURE:

Layer 1 (original): Surface-Hankel moment matrix M_{ij} = S_A(i+j+alpha)
where S_A(u) is the two-variable L-object. Rows/columns indexed by integer
arguments of the completed surface zeta function.

Layer 2 (new): Shadow Eisenstein series and Epstein zeta of the shadow obstruction tower.

THE SHADOW EISENSTEIN SERIES:
  E^{shadow}_k(tau, c) = sum_{n>=0} S_{k+n}(c) * q^n

where S_r(c) are the Virasoro shadow coefficients from the shadow obstruction
tower (cf. virasoro_shadow_gf.py). This is a q-deformation of the shadow
tower that incorporates genus-1 modular structure. When q -> 0, recovers S_k(c).

THE EPSTEIN ZETA OF THE SHADOW TOWER:
  Z_shadow(s, c) = sum_{r>=2} |S_r(c)|^2 * r^{-s}

For c = 13 (self-dual point Vir_c = Vir_{26-c}), Z_shadow has a natural
functional equation from the duality symmetry.

THE GENUS-1 MOMENT MATRIX:
For Virasoro, the genus-1 shadow correction is
  delta_H^(1)_Vir = 120/[c^2(5c+22)] * x^2
and the quartic contact invariant is
  Q^contact_Vir = 10/[c(5c+22)]
Both share the Lee-Yang denominator c(5c+22), vanishing at c = -22/5.

The Eisenstein moment matrix E_n(c) is the n x n matrix whose (i,j) entry
captures the genus-1 correction to the (i,j) shadow OPE coefficient:
  (E_n)_{ij} = S_{i+j+2}(c) * F_1(c)
where F_1(c) = c/48 is the genus-1 free energy coefficient.

PARTITION FUNCTION DATA:
  Virasoro vacuum character: q^{-c/24} / prod_{n>=2}(1 - q^n)
  Heisenberg: Z_1 = 1/eta(q) = q^{-1/24} / prod_{n>=1}(1 - q^n)

MOMENT MATRIX EXCLUSION PRINCIPLE:
  det(E^(1)_n(c)) = 0 at specific c-values signals a genus-1 null vector
  relation, giving a spectral characterization of c-values where the
  shadow obstruction tower simplifies.

References:
  thm:virasoro-shadow-generating-function (virasoro_shadow_gf.py)
  thm:w-virasoro-quintic-forced (w_algebras.tex)
  def:modular-cyclic-deformation-complex (chiral_hochschild_koszul.tex)
"""

from mpmath import mp, mpf, zeta, pi, power, fac, gamma as mpgamma, euler as eg
from mpmath import exp as mpexp, log as mplog, matrix as mpmatrix, det as mpdet
from mpmath import sqrt as mpsqrt, mpf as _mpf

mp.dps = 40


# =============================================================================
# Virasoro shadow coefficients (rational functions of c)
# =============================================================================

def shadow_coefficient_exact(r, c_val):
    """Compute S_r(c) for the Virasoro shadow obstruction tower via the closed-form
    generating function H(t,c) = t^2 * sqrt(c^2 + 12ct + alpha(c)*t^2).

    S_r = [t^r] H(t) / r, extracted via series expansion.
    """
    c_val = mpf(c_val)
    if c_val == 0:
        return mpf('inf')
    alpha_val = (180 * c_val + 872) / (5 * c_val + 22)

    # Taylor expand t^2 * sqrt(c^2 + 12c*t + alpha*t^2) to order r
    # Write Q(t) = c^2(1 + 12t/c + alpha*t^2/c^2) = c^2 * (1 + u)
    # where u = 12t/c + alpha*t^2/c^2.
    # sqrt(Q) = |c| * sqrt(1 + u) = |c| * sum_{k>=0} binom(1/2,k) * u^k
    # H(t) = t^2 * |c| * sum binom(1/2,k) * u^k

    # For numerical extraction, evaluate via finite differences or
    # direct polynomial arithmetic. Use the recursive approach.
    return _shadow_coeff_recursive(r, c_val)


def _shadow_coeff_recursive(r, c_val):
    """Compute S_r via the H-Poisson bracket recursion."""
    c_val = mpf(c_val)
    if r < 2:
        return mpf(0)

    S = {}
    S[2] = c_val / 2
    S[3] = mpf(2)
    h = 5 * c_val + 22
    if abs(h) < mpf('1e-30'):
        return mpf('inf')
    S[4] = mpf(10) / (c_val * h)

    if r <= 4:
        return S[r]

    # Propagator P = 2/c
    P = mpf(2) / c_val

    for rr in range(5, r + 1):
        obs = mpf(0)
        for j in range(3, rr):
            k = rr + 2 - j
            if k < 2 or k >= rr or k not in S:
                continue
            if j > k:
                continue
            # {S_j x^j, S_k x^k}_H = j*k * S_j * S_k * P * x^{j+k-2}
            # The x-power of the bracket is j+k-2 = rr (since j+k = rr+2).
            bracket_coeff = j * k * S[j] * S[k] * P
            if j == k:
                obs += bracket_coeff / 2
            else:
                obs += bracket_coeff

        S[rr] = -obs / (2 * rr)

    return S[r]


def shadow_coefficients(max_r, c_val):
    """Return dict {r: S_r(c)} for r = 2, ..., max_r."""
    c_val = mpf(c_val)
    if c_val == 0:
        return {r: mpf('inf') for r in range(2, max_r + 1)}

    h = 5 * c_val + 22
    P = mpf(2) / c_val

    S = {}
    S[2] = c_val / 2
    S[3] = mpf(2)
    if abs(h) < mpf('1e-30'):
        S[4] = mpf('inf')
    else:
        S[4] = mpf(10) / (c_val * h)

    for rr in range(5, max_r + 1):
        obs = mpf(0)
        for j in range(3, rr):
            k = rr + 2 - j
            if k < 2 or k >= rr or k not in S:
                continue
            if j > k:
                continue
            bracket_coeff = j * k * S[j] * S[k] * P
            if j == k:
                obs += bracket_coeff / 2
            else:
                obs += bracket_coeff
        S[rr] = -obs / (2 * rr)

    return S


# =============================================================================
# Genus-1 data
# =============================================================================

def genus1_free_energy(c_val):
    """F_1(c) = c/48, the genus-1 free energy from kappa * lambda_1^FP.

    kappa = c/2, lambda_1^{FP} = 1/24 (first Faber-Pandharipande coefficient).
    """
    return mpf(c_val) / 48


def delta_H_genus1(c_val):
    """Genus-1 Hessian correction: delta_H^(1)_Vir = 120/[c^2(5c+22)].

    This is the coefficient of x^2 in the genus-1 shadow correction.
    """
    c_val = mpf(c_val)
    h = 5 * c_val + 22
    return mpf(120) / (c_val ** 2 * h)


def quartic_contact(c_val):
    """Quartic contact invariant: Q^contact_Vir = 10/[c(5c+22)]."""
    c_val = mpf(c_val)
    h = 5 * c_val + 22
    return mpf(10) / (c_val * h)


def rho_genus1(c_val):
    """Genus-1 density correction: rho^(1)_Vir = 240/[c^3(5c+22)]."""
    c_val = mpf(c_val)
    h = 5 * c_val + 22
    return mpf(240) / (c_val ** 3 * h)


# =============================================================================
# Surface moment matrix (original Layer 1)
# =============================================================================

def S_heisenberg(u):
    if abs(u - 1) < 1e-20:
        return mpf('inf')  # pole
    return zeta(u) * zeta(u + 1)


def S_virasoro(u):
    if abs(u - 1) < 1e-20:
        return mpf('inf')
    return zeta(u + 1) * (zeta(u) - 1)


def S_WN(N, u):
    if abs(u - 1) < 1e-20:
        return mpf('inf')
    harm_sum = sum(power(j, -u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * zeta(u) - harm_sum)


def surface_moment_matrix(S_func, size, alpha=2):
    """M_{ij} = S_A(alpha + i + j) for i,j = 0,...,size-1.

    Hankel matrix in the surface zeta function at integer points.
    """
    M = mpmatrix(size, size)
    for i in range(size):
        for j in range(size):
            u = alpha + i + j
            M[i, j] = S_func(u)
    return M


def surface_moment_minors(S_func, max_size=5, alpha=2):
    """Leading principal minors of the surface moment matrix."""
    minors = []
    for k in range(1, max_size + 1):
        M = surface_moment_matrix(S_func, k, alpha)
        minors.append(mpdet(M))
    return minors


# =============================================================================
# Shadow Eisenstein series (new Layer 2)
# =============================================================================

def shadow_eisenstein_series(k, c_val, q_val, max_terms=20):
    r"""Shadow Eisenstein series E^{shadow}_k(q, c) = sum_{n=0}^{N} S_{k+n}(c) * q^n.

    Parameters
    ----------
    k : int
        Starting arity (>= 2).
    c_val : float or mpf
        Central charge.
    q_val : float or mpf
        Nome q = exp(2*pi*i*tau), real and |q| < 1.
    max_terms : int
        Truncation order.

    Returns
    -------
    mpf
        Truncated value of the shadow Eisenstein series.
    """
    c_val = mpf(c_val)
    q_val = mpf(q_val)
    S = shadow_coefficients(k + max_terms, c_val)
    result = mpf(0)
    q_power = mpf(1)
    for n in range(max_terms + 1):
        r = k + n
        if r in S:
            result += S[r] * q_power
        q_power *= q_val
    return result


def shadow_eisenstein_array(c_val, q_val, k_range=range(2, 8), max_terms=20):
    """Compute E^{shadow}_k for a range of starting arities k.

    Returns dict {k: E^{shadow}_k(q, c)}.
    """
    c_val = mpf(c_val)
    q_val = mpf(q_val)
    max_r = max(k_range) + max_terms
    S = shadow_coefficients(max_r, c_val)

    results = {}
    for k in k_range:
        val = mpf(0)
        q_power = mpf(1)
        for n in range(max_terms + 1):
            r = k + n
            if r in S:
                val += S[r] * q_power
            q_power *= q_val
        results[k] = val
    return results


# =============================================================================
# Epstein zeta of the shadow obstruction tower
# =============================================================================

def shadow_epstein_zeta(s_val, c_val, max_r=30):
    r"""Epstein zeta function of the shadow obstruction tower:
        Z_shadow(s, c) = sum_{r>=2} |S_r(c)|^2 * r^{-s}

    Parameters
    ----------
    s_val : float or mpf
        Complex frequency (real part > 1 for convergence).
    c_val : float or mpf
        Central charge.
    max_r : int
        Truncation.

    Returns
    -------
    mpf
        Truncated Epstein zeta value.
    """
    c_val = mpf(c_val)
    s_val = mpf(s_val)
    S = shadow_coefficients(max_r, c_val)
    result = mpf(0)
    for r in range(2, max_r + 1):
        if r in S:
            result += S[r] ** 2 * power(r, -s_val)
    return result


def shadow_epstein_zeta_complex(s_real, s_imag, c_val, max_r=30):
    """Epstein zeta at complex s = s_real + i*s_imag."""
    from mpmath import mpc
    c_val = mpf(c_val)
    s = mpc(s_real, s_imag)
    S = shadow_coefficients(max_r, c_val)
    result = mpc(0)
    for r in range(2, max_r + 1):
        if r in S:
            sr = S[r]
            result += sr * sr * power(r, -s)
    return result


def shadow_epstein_functional_equation_test(s_val, c_val=13, max_r=30):
    """Test the functional equation at the self-dual point c = 13.

    At c = 13, Vir_c^! = Vir_{26-c} = Vir_13 = self-dual.
    The shadow coefficients satisfy S_r(13) = S_r(13) trivially,
    so Z_shadow(s, 13) is self-consistent. The question is whether
    Z_shadow has a nontrivial functional equation relating s to some s'.

    For the surface Hankel matrix, functional equations come from the
    Riemann zeta. Here we test numerically whether
    Z_shadow(s, 13) / Z_shadow(A-s, 13) is approximately constant
    for some reflection point A.
    """
    c_val = mpf(c_val)
    Z_s = shadow_epstein_zeta(s_val, c_val, max_r)

    # Try several reflection points
    results = {}
    for A in [2, 3, 4, 5]:
        Z_ref = shadow_epstein_zeta(A - s_val, c_val, max_r)
        if abs(Z_ref) > mpf('1e-30'):
            results[A] = float(Z_s / Z_ref)
        else:
            results[A] = None
    return results


# =============================================================================
# Duality structure: S_r(c) vs S_r(26-c)
# =============================================================================

def shadow_duality_ratio(r, c_val):
    """Compute S_r(c) / S_r(26-c), the Virasoro duality ratio.

    At c = 13 (self-dual), this is 1.
    """
    S_c = shadow_coefficient_exact(r, c_val)
    S_dual = shadow_coefficient_exact(r, 26 - c_val)
    if abs(S_dual) < mpf('1e-30'):
        return mpf('inf')
    return S_c / S_dual


def shadow_duality_epstein_ratio(s_val, c_val, max_r=30):
    """Z_shadow(s, c) / Z_shadow(s, 26-c)."""
    Z_c = shadow_epstein_zeta(s_val, c_val, max_r)
    Z_dual = shadow_epstein_zeta(s_val, 26 - c_val, max_r)
    if abs(Z_dual) < mpf('1e-30'):
        return mpf('inf')
    return Z_c / Z_dual


# =============================================================================
# Eisenstein moment matrix E_n(c) (genus-1 shadow OPE correction)
# =============================================================================

def eisenstein_moment_matrix_genus1(n, c_val):
    """The n x n Eisenstein moment matrix for genus-1 shadow corrections.

    (E_n)_{ij} = S_{i+j+2}(c) * F_1(c)

    where S_r are shadow coefficients and F_1 = c/48.
    This captures how genus-1 corrections mix different conformal families.
    """
    c_val = mpf(c_val)
    F1 = genus1_free_energy(c_val)
    max_r = 2 * n + 2
    S = shadow_coefficients(max_r, c_val)

    M = mpmatrix(n, n)
    for i in range(n):
        for j in range(n):
            r = (i + 1) + (j + 1) + 2  # 1-indexed: i+j+4 for i,j from 0
            # Actually: (i+j+2) with 0-indexed, so r = i + j + 2
            r = i + j + 2
            if r in S:
                M[i, j] = S[r] * F1
            else:
                M[i, j] = mpf(0)
    return M


def eisenstein_moment_matrix_pure(n, c_val):
    """Pure shadow Hankel matrix: (M_n)_{ij} = S_{i+j+2}(c).

    Without the F_1 prefactor. This is a Hankel matrix in the shadow
    tower coefficients, analogous to the surface Hankel matrix but
    using the Virasoro shadow obstruction tower directly.
    """
    c_val = mpf(c_val)
    max_r = 2 * n + 2
    S = shadow_coefficients(max_r, c_val)

    M = mpmatrix(n, n)
    for i in range(n):
        for j in range(n):
            r = i + j + 2
            if r in S:
                M[i, j] = S[r]
            else:
                M[i, j] = mpf(0)
    return M


def eisenstein_moment_minors(n_max, c_val, pure=True):
    """Leading principal minors of the Eisenstein moment matrix.

    Returns list [det(E_1), det(E_2), ..., det(E_{n_max})].

    When det(E_k) = 0 at some c, there is a genus-1 null vector relation.
    """
    minors = []
    for k in range(1, n_max + 1):
        if pure:
            M = eisenstein_moment_matrix_pure(k, c_val)
        else:
            M = eisenstein_moment_matrix_genus1(k, c_val)
        minors.append(mpdet(M))
    return minors


# =============================================================================
# Partition function data
# =============================================================================

def eta_function(q_val, max_terms=100):
    """Dedekind eta: eta(q) = q^{1/24} * prod_{n>=1}(1 - q^n), truncated."""
    q_val = mpf(q_val)
    prod = mpf(1)
    q_power = q_val
    for n in range(1, max_terms + 1):
        prod *= (1 - q_power)
        q_power *= q_val
    return q_val ** (mpf(1) / 24) * prod


def heisenberg_partition(q_val, max_terms=100):
    """Z_1^{Heis}(q) = 1/eta(q) for the c=1 Heisenberg algebra."""
    eta = eta_function(q_val, max_terms)
    if abs(eta) < mpf('1e-30'):
        return mpf('inf')
    return 1 / eta


def virasoro_vacuum_character(c_val, q_val, max_terms=50):
    """Virasoro vacuum character: q^{-c/24} / prod_{n>=2}(1 - q^n).

    This is the genus-1 partition function for a single Virasoro primary
    at weight h = 0.
    """
    c_val = mpf(c_val)
    q_val = mpf(q_val)
    prod = mpf(1)
    q_power = q_val * q_val  # start at q^2
    for n in range(2, max_terms + 1):
        prod *= (1 - q_power)
        q_power *= q_val
    return q_val ** (-c_val / 24) / prod


def eisenstein_E2(q_val, max_terms=50):
    """Quasi-modular Eisenstein series E_2(q) = 1 - 24*sum_{n>=1} sigma_1(n)*q^n."""
    q_val = mpf(q_val)
    result = mpf(1)
    for n in range(1, max_terms + 1):
        # sigma_1(n) = sum of divisors of n
        sigma1 = sum(d for d in range(1, n + 1) if n % d == 0)
        result -= 24 * sigma1 * q_val ** n
    return result


def eisenstein_E4(q_val, max_terms=50):
    """Eisenstein series E_4(q) = 1 + 240*sum_{n>=1} sigma_3(n)*q^n."""
    q_val = mpf(q_val)
    result = mpf(1)
    for n in range(1, max_terms + 1):
        sigma3 = sum(d ** 3 for d in range(1, n + 1) if n % d == 0)
        result += 240 * sigma3 * q_val ** n
    return result


def eisenstein_E6(q_val, max_terms=50):
    """Eisenstein series E_6(q) = 1 - 504*sum_{n>=1} sigma_5(n)*q^n."""
    q_val = mpf(q_val)
    result = mpf(1)
    for n in range(1, max_terms + 1):
        sigma5 = sum(d ** 5 for d in range(1, n + 1) if n % d == 0)
        result -= 504 * sigma5 * q_val ** n
    return result


# =============================================================================
# Shadow-modular connection
# =============================================================================

def shadow_modular_ratio(k, c_val, q_val, max_terms=20):
    """Ratio E^{shadow}_k(q, c) / E_k^{Eisenstein}(q) at integer weight k.

    When this ratio is approximately constant (independent of q), the
    shadow Eisenstein series is proportional to the classical Eisenstein
    series, which would mean the shadow obstruction tower IS modular.

    For Heisenberg (Gaussian, shadow depth 2): only S_2 = 1/2 is nonzero,
    so E^{shadow}_2 = 1/2 (constant, trivially modular).

    For Virasoro: the ratio varies with q, measuring the deviation from
    modularity. The leading correction is O(q) with coefficient S_3/S_2.
    """
    E_shadow = shadow_eisenstein_series(k, c_val, q_val, max_terms)

    if k == 2:
        E_classical = eisenstein_E2(q_val, max_terms)
    elif k == 4:
        E_classical = eisenstein_E4(q_val, max_terms)
    elif k == 6:
        E_classical = eisenstein_E6(q_val, max_terms)
    else:
        return None  # only E_2, E_4, E_6 implemented

    if abs(E_classical) < mpf('1e-30'):
        return mpf('inf')
    return E_shadow / E_classical


# =============================================================================
# Lee-Yang singularity analysis
# =============================================================================

def lee_yang_approach(c_val):
    """Behavior of shadow invariants as c -> -22/5 (Lee-Yang edge).

    At c = -22/5 = -4.4, the factor (5c+22) vanishes. This is M(2,5),
    the simplest non-unitary minimal model. All shadow invariants involving
    (5c+22) in the denominator diverge:
      - Q^contact = 10/[c(5c+22)] -> infinity
      - delta_H^(1) = 120/[c^2(5c+22)] -> infinity
      - S_5 = -48/[c^2(5c+22)] -> infinity

    The physical interpretation: the Lee-Yang model has decoupled Lambda
    (no quartic contact interaction), and the formal shadow formulas
    detect this via pole singularity.
    """
    c_val = mpf(c_val)
    h = 5 * c_val + 22
    return {
        '5c+22': float(h),
        'Q_contact': float(quartic_contact(c_val)) if abs(h) > 1e-10 else float('inf'),
        'delta_H': float(delta_H_genus1(c_val)) if abs(h) > 1e-10 else float('inf'),
        'S_4': float(shadow_coefficient_exact(4, c_val)) if abs(h) > 1e-10 else float('inf'),
        'S_5': float(shadow_coefficient_exact(5, c_val)) if abs(h) > 1e-10 else float('inf'),
    }


# =============================================================================
# Moment matrix exclusion principle
# =============================================================================

def exclusion_scan(n_max=4, c_range=None, pure=True):
    """Scan for c-values where det(E_n) = 0 (genus-1 null vectors).

    The moment matrix exclusion principle: vanishing of det(E_n) signals
    a linear dependence among shadow coefficients that corresponds to a
    null vector at genus 1.

    Returns dict {n: [(c_val, det_val), ...]} for near-vanishing minors.
    """
    if c_range is None:
        c_range = [mpf(c) / 10 for c in range(1, 300) if c != -44]  # avoid 5c+22=0

    results = {}
    for n in range(1, n_max + 1):
        near_zeros = []
        for c_val in c_range:
            try:
                if pure:
                    M = eisenstein_moment_matrix_pure(n, c_val)
                else:
                    M = eisenstein_moment_matrix_genus1(n, c_val)
                d = mpdet(M)
                if abs(d) < mpf('1e-10'):
                    near_zeros.append((float(c_val), float(d)))
            except Exception:
                continue
        results[n] = near_zeros
    return results


# =============================================================================
# Analysis runner
# =============================================================================

def analyze_surface_structure():
    """Compute surface moment matrices and their determinants."""
    print("=" * 80)
    print("SURFACE MOMENT MATRIX ANALYSIS")
    print("=" * 80)

    for alpha in [2, 3, 4]:
        print(f"\n--- Offset alpha = {alpha} ---")

        minors_H = surface_moment_minors(S_heisenberg, 5, alpha)
        print(f"\nHeisenberg surface minors (alpha={alpha}):")
        for k, m in enumerate(minors_H):
            print(f"  det(M_{k+1}) = {float(m):>25.15f}")

        minors_V = surface_moment_minors(S_virasoro, 5, alpha)
        print(f"\nVirasoro surface minors (alpha={alpha}):")
        for k, m in enumerate(minors_V):
            print(f"  det(M_{k+1}) = {float(m):>25.15f}")

        print(f"\nVirasoro/Heisenberg minor ratios:")
        for k in range(len(minors_H)):
            if abs(minors_H[k]) > 1e-30:
                print(f"  det(M_{k+1})_Vir / det(M_{k+1})_H = "
                      f"{float(minors_V[k] / minors_H[k]):>20.15f}")


def analyze_shadow_eisenstein():
    """Analyze the shadow Eisenstein series at various c and q."""
    print("\n" + "=" * 80)
    print("SHADOW EISENSTEIN SERIES")
    print("=" * 80)

    for c_val in [1, 13, 25, 26]:
        print(f"\n--- c = {c_val} ---")
        for q_val in [0.01, 0.1, 0.3]:
            vals = shadow_eisenstein_array(c_val, q_val, range(2, 7), 15)
            print(f"  q = {q_val}:")
            for k, v in sorted(vals.items()):
                print(f"    E^shadow_{k} = {float(v):>20.12f}")


def analyze_epstein_zeta():
    """Analyze the Epstein zeta of the shadow obstruction tower."""
    print("\n" + "=" * 80)
    print("SHADOW EPSTEIN ZETA")
    print("=" * 80)

    for c_val in [1, 13, 25, 26]:
        print(f"\n--- c = {c_val} ---")
        for s_val in [2, 3, 4, 5]:
            Z = shadow_epstein_zeta(s_val, c_val, 25)
            print(f"  Z_shadow(s={s_val}) = {float(Z):>20.12f}")

    print(f"\n--- Self-dual c=13: duality ratio ---")
    for s_val in [2, 3, 4, 5]:
        ratio = shadow_duality_epstein_ratio(s_val, 13, 25)
        print(f"  Z(s={s_val}, c=13) / Z(s={s_val}, c=13) = {float(ratio):>15.10f}")

    print(f"\n--- c=1 vs c=25: duality check ---")
    for s_val in [2, 3, 4, 5]:
        ratio = shadow_duality_epstein_ratio(s_val, 1, 25)
        print(f"  Z(s={s_val}, c=1) / Z(s={s_val}, c=25) = {float(ratio):>15.10f}")


if __name__ == "__main__":
    analyze_surface_structure()
    analyze_shadow_eisenstein()
    analyze_epstein_zeta()
