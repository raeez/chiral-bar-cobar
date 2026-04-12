"""
R-matrix character chi_R(u, tau) for Y_hbar(sl_2) at level k=2.

Definition:
    chi_R(u, tau) = Sum_J lambda_J(u) * N_{11}^J * chi_J(tau)

where:
    - J runs over integrable representations at level k
    - lambda_J(u) = R-matrix eigenvalue on the V_J channel
    - N_{11}^J = fusion coefficient for V_{1/2} x V_{1/2} -> V_J
    - chi_J(tau) = affine character of V_J

For sl_2 at k=2:
    - Integrable reps: j = 0, 1/2, 1
    - Fusion: V_{1/2} x V_{1/2} = V_0 + V_1 (at level k=2, both channels open)
    - R-matrix eigenvalues:
        lambda_1(u) = 1          (triplet, J=1)
        lambda_0(u) = (u - hbar)/(u + hbar)  (singlet, J=0)
      where hbar = 1/(k+2) = 1/4
    - Central charge: c = 3k/(k+2) = 3/2
"""

import numpy as np
from mpmath import (mp, mpf, mpc, pi, exp, sqrt, sin, cos, matrix,
                    jtheta, nstr, fabs, im, re, log, power)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mp.dps = 50  # high precision

# ============================================================
# PART 1: Affine sl_2 characters at level k=2
# ============================================================
#
# The specialized character (z=1, i.e. no fugacity) of the integrable
# highest-weight module V_j of hat{sl}_2 at level k is:
#
#   chi_j(tau) = Tr_{V_j}(q^{L_0 - c/24})
#
# Using the Kac-Weyl-Kac character formula with z-specialization,
# the result for hat{sl}_2 is expressible via string functions c^k_j(tau):
#
#   chi_j(tau) = (1/eta(tau)^3) * sum_{m in Z_{2(k+2)}, m = 2j+1 mod 2}
#                  sign(m) * q^{m^2/(4(k+2))}
#
# More explicitly, for the specialized character:
#
#   chi_j(tau) = [Theta_{2j+1,k+2}(0,tau) - Theta_{-(2j+1),k+2}(0,tau)]
#                / [eta(tau)^3]
#
# where the numerator theta function difference, when both are evaluated
# at z=0, requires the derivative form. But the standard approach is:
#
# The SPECIALIZED character formula for hat{sl}_2 at level k gives:
#
#   chi_j(q) = q^{h_j - c/24} * Product_{n>=1}
#              [(1 - q^{n(k+2) + 2j+1})(1 - q^{n(k+2) - (2j+1)})]
#              / [(1-q^n)^2 * (1 - q^{n(k+2)})]    ... [WRONG, too complicated]
#
# The cleanest approach: use the THETA FUNCTION / ETA FUNCTION ratio
# with the non-specialized (z-dependent) character, then take z -> 1
# carefully. But the simplest correct method for numerical computation
# is to directly sum the q-expansion.
#
# For hat{sl}_2 level k, the character is:
#   chi_j(tau) = (1/eta(tau)) * sum_{n in Z} sign_factor * q^{exponent(n)}
#
# Actually, the cleanest route uses the BRANCHING into Virasoro modules.
# For k=2 (the N=1 superconformal / 3-state Potts level), we can
# compute explicitly.
#
# CORRECT FORMULA (Kac-Peterson):
# The specialized character of hat{sl}_2 at level k, highest weight j, is:
#
#   chi_j(tau) = [A_{2j+1,2(k+2)}(tau)] / [eta(tau)^3]
#
# where A_{m,p}(tau) = sum_{n in Z} (p*n + (p-m)/2) * q^{(pn + (p-m)/2)^2 / (2p)}
#                                                         ... [derivative form]
#
# No -- let me use the SIMPLEST correct formula.
#
# For hat{sl}_2 at level k, the FULL character with z-fugacity is:
#   chi_j(z, tau) = [Theta_{2j+1,k+2}(z,tau) - Theta_{-(2j+1),k+2}(z,tau)]
#                   / [Theta_{1,2}(z,tau) - Theta_{-1,2}(z,tau)]
#
# where Theta_{m,K}(z,tau) = sum_n q^{K(n+m/(2K))^2} * y^{K(n+m/(2K))}
# with y = e^{2pi i z}.
#
# The specialized character is the LIMIT as z -> 0. Both numerator and
# denominator vanish at z=0 (odd in z), so we take the ratio of
# derivatives:
#
#   chi_j(tau) = lim_{z->0} chi_j(z,tau)
#              = [d/dz Theta_{2j+1,k+2}(z,tau)|_{z=0}]
#                / [d/dz Theta_{1,2}(z,tau)|_{z=0}]
#
# But actually the correct normalization involves the Weyl denominator.
# For hat{sl}_2, the Weyl-Kac denominator is:
#   R(z,tau) = (y^{1/2} - y^{-1/2}) * prod_{n>=1} (1-q^n y)(1-q^n/y)(1-q^n)
#
# and the character is:
#   chi_j(z,tau) = [sum_{w in W_aff} det(w) * q^{<w(Lambda+rho),alpha_0>} * y^{...}]
#                  / R(z,tau)
#
# This is getting complicated. Let me just use DIRECT q-EXPANSION which is
# completely unambiguous for numerical work.

def eta_function(tau, num_terms=500):
    """Dedekind eta function: eta(tau) = q^{1/24} * prod_{n>=1}(1-q^n)."""
    q = exp(2 * pi * mpc(0, 1) * tau)
    result = power(q, mpf(1)/24)
    for n in range(1, num_terms + 1):
        result *= (1 - power(q, n))
    return result


def theta_function_mk(m, K, z, tau, num_terms=300):
    """
    Theta function with characteristics:
    Theta_{m,K}(z, tau) = sum_{n in Z} q^{K(n + m/(2K))^2} * y^{2K(n + m/(2K))}

    where q = e^{2 pi i tau}, y = e^{2 pi i z}.

    Note: the power of y uses 2K*(...) so that the z-variable
    tracks the weight lattice correctly for sl_2.
    """
    q = exp(2 * pi * mpc(0, 1) * tau)
    y = exp(2 * pi * mpc(0, 1) * z)
    result = mpc(0)
    for n in range(-num_terms, num_terms + 1):
        t = n + mpf(m) / (2 * K)
        q_exp = K * t**2
        y_exp = 2 * K * t
        result += power(q, q_exp) * power(y, y_exp)
    return result


def affine_sl2_character(j, tau, k=2, num_terms=300):
    """
    Compute the specialized affine sl_2 character chi_j(tau).

    Method: evaluate the full z-dependent character at a small z and
    take the limit numerically. Both numerator and denominator of the
    Kac-Weyl formula vanish at z=0 (they are odd functions of z),
    so we evaluate at z = epsilon and verify stability.

    Alternatively, we use L'Hopital:
    chi_j(tau) = [d/dz num(z,tau)]_{z=0} / [d/dz den(z,tau)]_{z=0}

    For the theta functions Theta_{m,K}(z,tau):
    d/dz Theta_{m,K}(z,tau)|_{z=0} = 2pi i * sum_n 2K(n+m/(2K)) * q^{K(n+m/(2K))^2}

    This is a convergent sum we can compute directly.
    """
    q = exp(2 * pi * mpc(0, 1) * tau)

    def d_theta_dz_at_0(m, K):
        """d/dz Theta_{m,K}(z,tau) at z=0."""
        result = mpc(0)
        for n in range(-num_terms, num_terms + 1):
            t = n + mpf(m) / (2 * K)
            coeff = 2 * K * t  # coefficient from y-exponent
            q_exp = K * t**2
            result += coeff * power(q, q_exp)
        return 2 * pi * mpc(0, 1) * result

    # Numerator derivative: d/dz [Theta_{2j+1,k+2} - Theta_{-(2j+1),k+2}] at z=0
    m_val = int(2 * j + 1)
    K_val = k + 2
    d_num = d_theta_dz_at_0(m_val, K_val) - d_theta_dz_at_0(-m_val, K_val)

    # Denominator derivative: d/dz [Theta_{1,2} - Theta_{-1,2}] at z=0
    d_den = d_theta_dz_at_0(1, 2) - d_theta_dz_at_0(-1, 2)

    return d_num / d_den


def affine_sl2_character_direct(j, tau, k=2, num_terms=500):
    """
    Direct q-expansion of the affine sl_2 character at level k.

    For hat{sl}_2 at level k, the specialized character is:

    chi_j(tau) = (1/eta(tau)^3) * sum_{n in Z} (2(k+2)n + 2j+1) * q^{(2(k+2)n + 2j+1)^2 / (4(k+2))}

    This is the derivative (L'Hopital) form of the Kac-Weyl ratio.
    The sum converges rapidly for Im(tau) > 0.

    Proof: Theta_{m,K}(z,tau) - Theta_{-m,K}(z,tau) is odd in z,
    so its z-derivative at z=0 gives a factor of 2*i*pi*(...).
    The denominator d/dz[Theta_{1,2} - Theta_{-1,2}]|_{z=0} = i*eta(tau)^3
    (Jacobi triple product derivative identity).

    Hence chi_j(tau) = A_{2j+1,2(k+2)}(tau) / eta(tau)^3
    where A_{m,p}(tau) = sum_{n in Z} m_n * q^{m_n^2/(2p)}
    with m_n = p*n + m (running over the coset m + p*Z) ... no wait.

    Let me just compute via the derivative approach directly.
    """
    q = exp(2 * pi * mpc(0, 1) * tau)

    # Numerator: sum_n (2*K*n + m) * q^{K*(n + m/(2K))^2} where K=k+2, m=2j+1
    # minus the same with m -> -m
    # = sum_n [(2Kn+m) * q^{(2Kn+m)^2/(4K)} - (2Kn-m) * q^{(2Kn-m)^2/(4K)}]
    # Setting r = 2Kn+m and r' = 2Kn-m:
    # = sum_{r = m mod 2K} r * q^{r^2/(4K)} - sum_{r' = -m mod 2K} r' * q^{r'^2/(4K)}

    # More simply: both the m and -m theta functions contribute.
    # d/dz Theta_{m,K}|_{z=0} = 2*pi*i * sum_n 2K*(n+m/(2K)) * q^{K*(n+m/(2K))^2}
    #                          = 2*pi*i * sum_n (2Kn+m) * q^{(2Kn+m)^2/(4K)}

    K = k + 2
    m = int(2 * j + 1)

    num = mpc(0)
    for n in range(-num_terms, num_terms + 1):
        r_plus = 2 * K * n + m
        r_minus = 2 * K * n - m
        num += r_plus * power(q, mpf(r_plus**2) / (4 * K))
        num -= r_minus * power(q, mpf(r_minus**2) / (4 * K))

    # Denominator: same with K=2, m=1 gives i*eta(tau)^3 (up to normalization)
    # d/dz [Theta_{1,2} - Theta_{-1,2}]|_{z=0}
    # = 2*pi*i * sum_n [(4n+1)*q^{(4n+1)^2/8} - (4n-1)*q^{(4n-1)^2/8}]
    # This equals 2*pi*i * eta(tau)^3 by the Jacobi triple product derivative.

    den = mpc(0)
    for n in range(-num_terms, num_terms + 1):
        s_plus = 4 * n + 1
        s_minus = 4 * n - 1
        den += s_plus * power(q, mpf(s_plus**2) / 8)
        den -= s_minus * power(q, mpf(s_minus**2) / 8)

    # The common 2*pi*i factor cancels in the ratio.
    return num / den


# ============================================================
# PART 2: R-matrix eigenvalues for Y_hbar(sl_2)
# ============================================================

def r_matrix_eigenvalue(J, u, hbar=mpf(1)/4):
    """
    R-matrix eigenvalue on the spin-J channel of V_{1/2} x V_{1/2}.

    For the Yangian Y_hbar(sl_2), the R-matrix acting on V_{1/2} x V_{1/2}
    decomposes as:

        R(u) = lambda_0(u) * P_0 + lambda_1(u) * P_1

    where P_J is the projector onto the spin-J component and:

        lambda_1(u) = 1                    (triplet, normalized)
        lambda_0(u) = (u - hbar)/(u + hbar)  (singlet)

    This is the standard rational R-matrix for sl_2 in the fundamental
    representation, with the normalization R(infinity) = id.

    Here hbar = 1/(k+2) = 1/4 for level k=2.
    """
    if J == 1:
        return mpf(1)
    elif J == 0:
        return (u - hbar) / (u + hbar)
    else:
        raise ValueError(f"Invalid J={J} for V_{{1/2}} x V_{{1/2}} decomposition")


# ============================================================
# PART 3: Fusion coefficients
# ============================================================

# For sl_2 at level k=2:
# V_{1/2} x V_{1/2} = V_0 + V_1
# So N_{1/2, 1/2}^0 = 1, N_{1/2, 1/2}^1 = 1

FUSION_COEFFS = {0: 1, 1: 1}  # N_{1/2,1/2}^J for J=0 and J=1


# ============================================================
# PART 4: The R-matrix character
# ============================================================

def chi_R(u, tau, k=2, hbar=None, num_terms=500):
    """
    R-matrix character:
        chi_R(u, tau) = Sum_J lambda_J(u) * N_{1/2,1/2}^J * chi_J(tau)

    For k=2:
        chi_R(u, tau) = lambda_0(u) * chi_0(tau) + lambda_1(u) * chi_1(tau)
                      = [(u-hbar)/(u+hbar)] * chi_0(tau) + 1 * chi_1(tau)
    """
    if hbar is None:
        hbar = mpf(1) / (k + 2)

    result = mpc(0)
    for J, N_J in FUSION_COEFFS.items():
        lam = r_matrix_eigenvalue(J, u, hbar)
        chi = affine_sl2_character_direct(mpf(J), tau, k, num_terms)
        result += lam * N_J * chi
    return result


def chi_R_verlinde(tau, k=2, num_terms=500):
    """
    Verlinde limit: chi_R(infinity, tau) = Sum_J N_{1/2,1/2}^J * chi_J(tau)
                                         = chi_0(tau) + chi_1(tau)
    """
    result = mpc(0)
    for J, N_J in FUSION_COEFFS.items():
        chi = affine_sl2_character_direct(mpf(J), tau, k, num_terms)
        result += N_J * chi
    return result


# ============================================================
# PART 5: S-matrix
# ============================================================

def s_matrix_sl2(k):
    """
    Modular S-matrix for sl_2 at level k.

    S_{jj'} = sqrt(2/(k+2)) * sin(pi*(2j+1)*(2j'+1)/(k+2))

    For k=2 (K=k+2=4):
    Representations: j = 0, 1/2, 1
    """
    K = k + 2
    spins = [mpf(j) / 2 for j in range(k + 1)]  # j = 0, 1/2, 1 for k=2

    S = matrix(len(spins), len(spins))
    prefactor = sqrt(mpf(2) / K)

    for i, j in enumerate(spins):
        for ip, jp in enumerate(spins):
            S[i, ip] = prefactor * sin(pi * (2*j + 1) * (2*jp + 1) / K)

    return S, spins


# ============================================================
# MAIN COMPUTATION
# ============================================================

def main():
    print("=" * 72)
    print("R-MATRIX CHARACTER chi_R(u, tau) FOR Y_hbar(sl_2) AT LEVEL k=2")
    print("=" * 72)

    k = 2
    hbar = mpf(1) / (k + 2)  # = 1/4
    tau = mpc(0, 1)  # tau = i
    c = mpf(3 * k) / (k + 2)  # c = 3/2

    print(f"\nParameters:")
    print(f"  k = {k}")
    print(f"  hbar = 1/(k+2) = {hbar}")
    print(f"  c = 3k/(k+2) = {nstr(c, 6)}")
    print(f"  tau = i")

    q = exp(2 * pi * mpc(0, 1) * tau)
    print(f"  q = e^{{2 pi i tau}} = e^{{-2 pi}} = {nstr(re(q), 15)}")

    # Conformal weights
    print(f"\nConformal weights h_j = j(j+1)/(k+2):")
    for j_val in [mpf(0), mpf(1)/2, mpf(1)]:
        h = j_val * (j_val + 1) / (k + 2)
        print(f"  h_{{{nstr(j_val, 3)}}} = {nstr(h, 6)}")

    # ────────────────────────────────────────────────────────────
    # Compute individual characters
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("INDIVIDUAL AFFINE CHARACTERS chi_j(tau = i)")
    print(f"{'='*72}")

    # First verify the two methods agree
    print("\n  Cross-checking derivative vs direct methods:")
    for j_val in [mpf(0), mpf(1)/2, mpf(1)]:
        chi_deriv = affine_sl2_character(j_val, tau, k, num_terms=300)
        chi_direct = affine_sl2_character_direct(j_val, tau, k, num_terms=300)
        diff = fabs(chi_deriv - chi_direct)
        print(f"    j={nstr(j_val,3)}: deriv={nstr(re(chi_deriv), 15):>20s}  "
              f"direct={nstr(re(chi_direct), 15):>20s}  diff={nstr(diff, 5)}")

    chars = {}
    for j_val in [mpf(0), mpf(1)/2, mpf(1)]:
        chi = affine_sl2_character_direct(j_val, tau, k)
        chars[j_val] = chi
        print(f"\n  chi_{{{nstr(j_val, 3)}}}(i) = {nstr(re(chi), 25)}")
        print(f"       Im part  = {nstr(im(chi), 10)}  (should be ~0)")
        print(f"       |chi|    = {nstr(fabs(chi), 25)}")

    chi_0 = chars[mpf(0)]
    chi_half = chars[mpf(1)/2]
    chi_1 = chars[mpf(1)]

    # Sanity checks
    print(f"\n  Sanity checks:")
    # At q -> 0 (tau -> i*infinity), chi_j -> q^{h_j - c/24} * (1 + ...)
    # h_0 = 0, c/24 = 1/16. So chi_0 ~ q^{-1/16}
    # h_{1/2} = 3/16, c/24 = 1/16. So chi_{1/2} ~ q^{3/16 - 1/16} = q^{1/8}
    # h_1 = 1/2, c/24 = 1/16. So chi_1 ~ q^{1/2 - 1/16} = q^{7/16}
    q_val = exp(-2 * pi)  # |q| for tau = i
    print(f"  q = e^{{-2pi}} = {nstr(q_val, 15)}")
    print(f"  Expected leading behavior:")
    print(f"    chi_0 ~ q^{{-1/16}} = {nstr(power(q_val, mpf(-1)/16), 15)}")
    print(f"    chi_{{1/2}} ~ q^{{1/8}} = {nstr(power(q_val, mpf(1)/8), 15)}")
    print(f"    chi_1 ~ q^{{7/16}} = {nstr(power(q_val, mpf(7)/16), 15)}")

    # ────────────────────────────────────────────────────────────
    # R-matrix eigenvalues
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("R-MATRIX EIGENVALUES lambda_J(u)")
    print(f"{'='*72}")
    print(f"  lambda_1(u) = 1  (triplet channel, all u)")
    print(f"  lambda_0(u) = (u - 1/4)/(u + 1/4)  (singlet channel)")
    print(f"  hbar = {hbar}")

    u_values = [mpf(0), hbar/2, hbar, 2*hbar, 4*hbar, 10*hbar, 100*hbar]
    u_labels = ["0", "hbar/2", "hbar", "2*hbar", "4*hbar", "10*hbar", "100*hbar"]

    print(f"\n  {'u':>12s}  {'lambda_0(u)':>20s}  {'lambda_1(u)':>12s}")
    print(f"  {'---':>12s}  {'---':>20s}  {'---':>12s}")
    for u_val, u_lab in zip(u_values, u_labels):
        l0 = r_matrix_eigenvalue(0, u_val, hbar)
        l1 = r_matrix_eigenvalue(1, u_val, hbar)
        print(f"  {u_lab:>12s}  {nstr(l0, 15):>20s}  {nstr(l1, 12):>12s}")

    print(f"\n  Key values:")
    print(f"    lambda_0(0) = -1     (singlet fully reflected)")
    print(f"    lambda_0(hbar) = 0   (singlet channel CLOSED)")
    print(f"    lambda_0(inf) = 1    (Verlinde / E_inf limit)")

    # ────────────────────────────────────────────────────────────
    # chi_R(u, tau) for several u
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("R-MATRIX CHARACTER chi_R(u, tau = i)")
    print(f"{'='*72}")
    print(f"  chi_R(u, tau) = lambda_0(u) * chi_0(tau) + lambda_1(u) * chi_1(tau)")
    print(f"               = [(u-1/4)/(u+1/4)] * chi_0(i) + chi_1(i)")

    print(f"\n  Components:")
    print(f"    chi_0(i) = {nstr(re(chi_0), 25)}")
    print(f"    chi_1(i) = {nstr(re(chi_1), 25)}")

    chi_verlinde = re(chi_0) + re(chi_1)
    print(f"\n  Verlinde limit: chi_R(inf, i) = chi_0(i) + chi_1(i) = {nstr(chi_verlinde, 25)}")

    u_compute = [mpf(0), hbar/4, hbar/2, 3*hbar/4, hbar, 3*hbar/2,
                 2*hbar, 3*hbar, 4*hbar, 6*hbar, 10*hbar, 20*hbar,
                 50*hbar, 100*hbar, 1000*hbar]
    u_comp_labels = ["0", "hbar/4", "hbar/2", "3hbar/4", "hbar", "3hbar/2",
                     "2hbar", "3hbar", "4hbar", "6hbar", "10hbar", "20hbar",
                     "50hbar", "100hbar", "1000hbar"]

    print(f"\n  {'u':>12s}  {'chi_R(u,i)':>25s}  {'Delta_chi(u,i)':>25s}  {'ratio':>12s}")
    print(f"  {'---':>12s}  {'---':>25s}  {'---':>25s}  {'---':>12s}")

    chi_R_data = []
    for u_val, u_lab in zip(u_compute, u_comp_labels):
        l0 = r_matrix_eigenvalue(0, u_val, hbar)
        l1 = r_matrix_eigenvalue(1, u_val, hbar)
        chi_r = l0 * re(chi_0) + l1 * re(chi_1)
        delta = chi_r - chi_verlinde
        ratio = chi_r / chi_verlinde if chi_verlinde != 0 else mpf(0)

        chi_R_data.append((u_val, chi_r, delta, ratio))
        print(f"  {u_lab:>12s}  {nstr(chi_r, 20):>25s}  {nstr(delta, 20):>25s}  {nstr(ratio, 8):>12s}")

    # ────────────────────────────────────────────────────────────
    # E_1 correction analysis
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("E_1 CORRECTION: Delta_chi(u, tau) = chi_R(u,tau) - chi_R(inf,tau)")
    print(f"{'='*72}")

    print(f"\n  Analytic form: Delta_chi(u, tau) = -2*hbar/(u+hbar) * chi_0(tau)")
    print(f"               = -(1/2)/(u + 1/4) * chi_0(i)")
    print(f"\n  Verification (analytic vs direct):")

    for u_val, u_lab in zip(u_compute[:8], u_comp_labels[:8]):
        delta_analytic = -2 * hbar / (u_val + hbar) * re(chi_0)
        l0 = r_matrix_eigenvalue(0, u_val, hbar)
        delta_direct = (l0 - 1) * re(chi_0)
        diff = fabs(delta_analytic - delta_direct)
        print(f"    u={u_lab:>12s}: analytic={nstr(delta_analytic, 15):>20s}  "
              f"direct={nstr(delta_direct, 15):>20s}  diff={nstr(diff, 5)}")

    # ────────────────────────────────────────────────────────────
    # Key structural features
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("KEY STRUCTURAL FEATURES")
    print(f"{'='*72}")

    chi_at_hbar = re(chi_1)  # lambda_0(hbar) = 0
    chi_at_0 = -re(chi_0) + re(chi_1)  # lambda_0(0) = -1

    print(f"\n  1. SINGLET SUPPRESSION (u = hbar = 1/4):")
    print(f"     chi_R(hbar, i) = 0*chi_0(i) + 1*chi_1(i) = chi_1(i)")
    print(f"     = {nstr(chi_at_hbar, 25)}")
    print(f"     Pure triplet character: the singlet channel is COMPLETELY CLOSED.")

    print(f"\n  2. SINGLET REFLECTION (u = 0):")
    print(f"     chi_R(0, i) = (-1)*chi_0(i) + 1*chi_1(i) = chi_1(i) - chi_0(i)")
    print(f"     = {nstr(chi_at_0, 25)}")
    print(f"     The singlet has NEGATIVE weight: maximally non-Verlinde.")

    print(f"\n  3. VERLINDE LIMIT (u -> infinity):")
    print(f"     chi_R(inf, i) = chi_0(i) + chi_1(i)")
    print(f"     = {nstr(chi_verlinde, 25)}")

    print(f"\n  4. INTERPOLATION RATIOS:")
    print(f"     chi_R(0, i)/chi_R(inf, i)     = {nstr(chi_at_0 / chi_verlinde, 15)}")
    print(f"     chi_R(hbar, i)/chi_R(inf, i)  = {nstr(chi_at_hbar / chi_verlinde, 15)}")

    print(f"\n  5. CRITICAL STRUCTURE:")
    print(f"     chi_0(i) / chi_1(i) = {nstr(re(chi_0) / re(chi_1), 15)}")
    print(f"     chi_0(i) / chi_verlinde = {nstr(re(chi_0) / chi_verlinde, 15)}")
    print(f"     chi_1(i) / chi_verlinde = {nstr(re(chi_1) / chi_verlinde, 15)}")

    # ────────────────────────────────────────────────────────────
    # S-matrix and modular transformation
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("MODULAR S-MATRIX FOR sl_2 AT LEVEL k=2")
    print(f"{'='*72}")

    S, spins = s_matrix_sl2(k)
    print(f"\n  Integrable representations: j = {[nstr(s, 3) for s in spins]}")
    print(f"  S_{{jj'}} = sqrt(2/(k+2)) * sin(pi*(2j+1)*(2j'+1)/(k+2))")
    print(f"\n  S-matrix (numerical):")

    for i in range(len(spins)):
        row = "  ["
        for ip in range(len(spins)):
            row += f" {nstr(S[i, ip], 10):>14s}"
        row += " ]"
        lbl = f"j={nstr(spins[i], 3)}"
        print(f"  {lbl:>8s} {row}")

    print(f"\n  Exact values:")
    print(f"    S_{{0,0}}   = 1/2")
    print(f"    S_{{0,1/2}} = 1/sqrt(2)")
    print(f"    S_{{0,1}}   = 1/2")
    print(f"    S_{{1/2,1/2}} = 0")
    print(f"    S_{{1/2,1}} = -1/sqrt(2)")
    print(f"    S_{{1,1}}   = 1/2")

    # Verify S^2 = C (charge conjugation = identity for sl_2)
    SS = S * S.T
    print(f"\n  S * S^T (should be identity):")
    for i in range(len(spins)):
        row = "  ["
        for ip in range(len(spins)):
            row += f" {nstr(SS[i, ip], 8):>12s}"
        row += " ]"
        print(f"    {row}")

    # Verify character transformation at tau = i (self-dual point)
    print(f"\n  Character transformation at tau = i (self-dual: -1/tau = i):")
    print(f"  chi_j(-1/tau) should equal Sum_{{j'}} S_{{jj'}} * chi_{{j'}}(tau)")
    for idx_j, j_val in enumerate(spins):
        chi_s_transform = mpc(0)
        for idx_jp, jp_val in enumerate(spins):
            chi_s_transform += S[idx_j, idx_jp] * chars[jp_val]
        diff = fabs(chars[j_val] - chi_s_transform)
        print(f"    j={nstr(j_val, 3)}: chi_j(i) = {nstr(re(chars[j_val]), 15):>20s}  "
              f"Sum S chi = {nstr(re(chi_s_transform), 15):>20s}  diff={nstr(diff, 5)}")

    # ────────────────────────────────────────────────────────────
    # Modular transformation of chi_R
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("MODULAR TRANSFORMATION OF chi_R(u, tau)")
    print(f"{'='*72}")

    print(f"""
  Under tau -> -1/tau, the affine characters transform as:
      chi_j(-1/tau) = Sum_{{j'}} S_{{jj'}} * chi_{{j'}}(tau)

  For chi_R(u, tau) = lambda_0(u)*chi_0(tau) + chi_1(tau):

      chi_R(u, -1/tau) = lambda_0(u) * chi_0(-1/tau) + chi_1(-1/tau)
                       = lambda_0(u) * [S_00*chi_0 + S_01*chi_{{1/2}} + S_02*chi_1]
                       +               [S_10*chi_0 + S_11*chi_{{1/2}} + S_12*chi_1]

  With S-matrix entries for k=2:
      = lambda_0(u) * [(1/2)*chi_0 + (1/sqrt2)*chi_{{1/2}} + (1/2)*chi_1]
      +               [(1/2)*chi_0 + 0*chi_{{1/2}} + (1/2)*chi_1]

  Collecting by character:
      chi_R(u, -1/tau) = [(1/2)*lambda_0(u) + 1/2]*chi_0(tau)
                       + [(1/sqrt2)*lambda_0(u)]*chi_{{1/2}}(tau)
                       + [(1/2)*lambda_0(u) + 1/2]*chi_1(tau)

  Substituting lambda_0(u) = (u-hbar)/(u+hbar):

      coeff of chi_0:     (1/2)*[(u-hbar)/(u+hbar) + 1] = u/(u+hbar)
      coeff of chi_{{1/2}}: (1/sqrt2)*(u-hbar)/(u+hbar)
      coeff of chi_1:      (1/2)*[(u-hbar)/(u+hbar) + 1] = u/(u+hbar)

  Therefore:
      chi_R(u, -1/tau) = [u/(u+hbar)] * [chi_0(tau) + chi_1(tau)]
                       + [(u-hbar)/((u+hbar)*sqrt(2))] * chi_{{1/2}}(tau)

  CRITICAL: The j=1/2 character chi_{{1/2}} appears in the S-transform
  even though it is ABSENT from chi_R(u,tau) itself!
  This is the hallmark of the E_1 structure: the S-transform does not
  close on the fusion subalgebra of V_{{1/2}} x V_{{1/2}}.""")

    # Numerical verification of the S-transform formula
    print(f"\n  Numerical verification at tau = i (-1/tau = i, self-dual):")
    for u_val, u_lab in zip([hbar, 2*hbar, 10*hbar], ["hbar", "2*hbar", "10*hbar"]):
        l0 = r_matrix_eigenvalue(0, u_val, hbar)
        chi_r_direct = l0 * re(chi_0) + re(chi_1)

        # S-transform formula
        coeff_0 = u_val / (u_val + hbar)
        coeff_half = (u_val - hbar) / ((u_val + hbar) * sqrt(2))
        coeff_1 = u_val / (u_val + hbar)

        chi_r_stransform = coeff_0 * re(chi_0) + coeff_half * re(chi_half) + coeff_1 * re(chi_1)

        diff = fabs(chi_r_direct - chi_r_stransform)
        print(f"    u={u_lab:>8s}: direct={nstr(chi_r_direct, 15):>20s}  "
              f"S-transf={nstr(chi_r_stransform, 15):>20s}  diff={nstr(diff, 5)}")

    # ────────────────────────────────────────────────────────────
    # Jacobi form analysis
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("JACOBI FORM / MODULAR FORM CLASSIFICATION")
    print(f"{'='*72}")

    print(f"""
  QUESTION: Is chi_R(u, tau) a Jacobi form? A modular form?

  ANALYSIS:

  1. chi_R(u, tau) = [(u-hbar)/(u+hbar)] * chi_0(tau) + chi_1(tau)

     The u-dependence is RATIONAL (Mobius transformation).
     Standard Jacobi forms have u-dependence through e^{{2*pi*i*u}}
     (theta-function type), with quasi-periodicity under u -> u+1, u -> u+tau.

     The rational u-dependence reflects the YANGIAN (rational) R-matrix.
     For the ELLIPTIC quantum group, lambda_0 would involve theta_1(u|tau)/theta_1(...),
     giving the proper Jacobi-type structure.

  2. Under tau -> -1/tau, chi_R mixes in chi_{{1/2}} (the j=1/2 character
     absent from the original fusion). This means chi_R is NOT closed under
     modular transformations at fixed u.

  3. The correct mathematical framework:

     chi_R(u, tau) is an element of

         Rat_1(u)  tensor  VVMF(SL_2(Z), rho_k)

     where:
       - Rat_1(u) = rational functions of u with a simple pole at u = -hbar
       - VVMF = vector-valued modular forms
       - rho_k = the (k+1)-dimensional representation of SL_2(Z)
                 given by the affine sl_2 S-matrix at level k

     More precisely, writing f(u) = (u-hbar)/(u+hbar) = 1 - 2*hbar/(u+hbar):

         chi_R(u, tau) = chi_Verlinde(tau) - [2*hbar/(u+hbar)] * chi_0(tau)

     where chi_Verlinde = chi_0 + chi_1 is one specific component of the
     VVMF, and chi_0 is another.

  4. chi_R is NOT:
     - A modular form (mixes under S-transform)
     - A Jacobi form (wrong u-dependence, no quasi-periodicity)
     - A quasi-modular form (those are polynomials in E_2)
     - A mock modular form (those have shadow integrals)

     chi_R IS:
     - A rational-in-u, vector-valued-modular-in-tau object
     - Specifically: an element of Hom(V_{{1/2}} tensor V_{{1/2}}, VVMF_k)
       where the Hom is R-matrix-weighted

  5. WEIGHT AND INDEX (if we force the question):
     The individual characters chi_j(tau) transform under tau -> -1/tau
     with a matrix (the S-matrix), not a power of tau. So there is no
     single "weight" for chi_R.

     However, at the level of the VECTOR (chi_0, chi_{{1/2}}, chi_1),
     this is a weight-0 vector-valued modular form for SL_2(Z)
     (the characters carry weight 0 in the usual CFT normalization
     where L_0 - c/24 gives the exponent).

  ELLIPTIC UPLIFT:

  If we replace the rational eigenvalue with the elliptic one:

      lambda_0^ell(u, tau) = theta_1(u - hbar | tau) / theta_1(u + hbar | tau)

  then chi_R^ell(u, tau) has the u-periodicity of a MEROMORPHIC Jacobi form
  (simple pole at u = -hbar mod Z + Z*tau), but the S-transform still
  mixes in chi_{{1/2}}, so it lives in

      MeroJac(tau) tensor VVMF(SL_2(Z), rho_k)
""")

    # ────────────────────────────────────────────────────────────
    # Elliptic R-matrix comparison
    # ────────────────────────────────────────────────────────────
    print(f"{'='*72}")
    print("ELLIPTIC VS RATIONAL R-MATRIX CHARACTER")
    print(f"{'='*72}")

    q_nome = exp(mpc(0, 1) * pi * tau)  # nome q_J = e^{i*pi*tau}

    print(f"\n  lambda_0^ell(u, tau) = theta_1(u - hbar | tau) / theta_1(u + hbar | tau)")
    print(f"  nome for theta: q_J = e^{{i*pi*tau}} = e^{{-pi}} = {nstr(re(exp(-pi)), 10)}")

    print(f"\n  {'u':>12s}  {'lam_0^rat':>15s}  {'lam_0^ell':>18s}  {'chi_R^rat':>22s}  {'chi_R^ell':>22s}")
    print(f"  {'---':>12s}  {'---':>15s}  {'---':>18s}  {'---':>22s}  {'---':>22s}")

    ell_chi_data = []
    for u_val, u_lab in zip(u_compute[:12], u_comp_labels[:12]):
        lam_rat = r_matrix_eigenvalue(0, u_val, hbar)

        z_minus = pi * (u_val - hbar)
        z_plus = pi * (u_val + hbar)
        th_minus = jtheta(1, z_minus, q_nome)
        th_plus = jtheta(1, z_plus, q_nome)
        lam_ell = th_minus / th_plus

        chi_r_rat = lam_rat * re(chi_0) + re(chi_1)
        chi_r_ell = re(lam_ell) * re(chi_0) + re(chi_1)

        ell_chi_data.append((float(u_val), float(re(lam_ell)), float(chi_r_ell)))

        print(f"  {u_lab:>12s}  {nstr(lam_rat, 12):>15s}  "
              f"{nstr(re(lam_ell), 14):>18s}  {nstr(chi_r_rat, 18):>22s}  {nstr(chi_r_ell, 18):>22s}")

    # ────────────────────────────────────────────────────────────
    # Plot
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("GENERATING PLOT")
    print(f"{'='*72}")

    hbar_f = 0.25
    chi_0_f = float(re(chi_0))
    chi_1_f = float(re(chi_1))
    chi_half_f = float(re(chi_half))
    chi_verl_f = chi_0_f + chi_1_f

    # --- Rational R-matrix character (main plot: u in [0, 5]) ---
    u_plot = np.linspace(0.001, 5.0, 500)
    lam_0_rat = (u_plot - hbar_f) / (u_plot + hbar_f)
    chi_R_rat = lam_0_rat * chi_0_f + chi_1_f
    delta_rat = chi_R_rat - chi_verl_f

    # --- Elliptic: restrict to ONE fundamental period u in [0, 0.5)
    #     to avoid poles at u = -hbar + n, i.e. u = 0.75, 1.75, ... ---
    u_plot_ell = np.linspace(0.001, 0.70, 300)  # stay within first period, before pole
    lam_0_ell_arr = np.zeros_like(u_plot_ell)
    chi_R_ell_fund = np.zeros_like(u_plot_ell)
    for idx, u_f in enumerate(u_plot_ell):
        u_mp = mpf(u_f)
        z_m = pi * (u_mp - hbar)
        z_p = pi * (u_mp + hbar)
        th_m = jtheta(1, z_m, q_nome)
        th_p = jtheta(1, z_p, q_nome)
        lam_e = float(re(th_m / th_p))
        lam_0_ell_arr[idx] = lam_e
        chi_R_ell_fund[idx] = lam_e * chi_0_f + chi_1_f

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: chi_R(u, tau=i) -- RATIONAL, clean monotone interpolation
    ax = axes[0, 0]
    ax.plot(u_plot, chi_R_rat, 'b-', linewidth=2.5, label=r'$\chi_R(u, i)$')
    ax.axhline(y=chi_verl_f, color='gray', linestyle=':', linewidth=1.2,
               label=r'Verlinde $\chi_R(\infty)={:.4f}$'.format(chi_verl_f))
    ax.axhline(y=chi_1_f, color='green', linestyle=':', linewidth=1.2,
               label=r'$\chi_1(i)={:.4f}$ (singlet closed)'.format(chi_1_f))
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.3)
    ax.axvline(x=hbar_f, color='orange', linestyle='--', linewidth=1.2, alpha=0.8,
               label=r'$u = \hbar = 1/4$')
    # Mark the three regimes
    ax.plot(0, chi_1_f - chi_0_f, 'rv', markersize=10, zorder=5)
    ax.annotate(r'$u\!=\!0$: $\chi_1\!-\!\chi_0$', xy=(0, chi_1_f - chi_0_f),
                xytext=(0.5, -0.8), fontsize=9,
                arrowprops=dict(arrowstyle='->', color='red'))
    ax.plot(hbar_f, chi_1_f, 'o', color='orange', markersize=8, zorder=5)
    ax.annotate(r'$u\!=\!\hbar$: $\chi_1$', xy=(hbar_f, chi_1_f),
                xytext=(0.7, 0.0), fontsize=9,
                arrowprops=dict(arrowstyle='->', color='orange'))
    ax.set_xlabel(r'Spectral parameter $u$', fontsize=12)
    ax.set_ylabel(r'$\chi_R(u, \tau\!=\!i)$', fontsize=12)
    ax.set_title(r'R-matrix character (rational Yangian)', fontsize=11)
    ax.legend(fontsize=8, loc='lower right')
    ax.set_ylim(-1.8, 2.0)
    ax.grid(True, alpha=0.3)

    # Panel 2: E_1 correction Delta_chi
    ax = axes[0, 1]
    ax.plot(u_plot, delta_rat, 'b-', linewidth=2.5,
            label=r'$\Delta\chi(u) = -\frac{1/2}{u+1/4}\,\chi_0(i)$')
    ax.axhline(y=0, color='gray', linestyle=':', linewidth=1)
    ax.axvline(x=hbar_f, color='orange', linestyle='--', linewidth=1, alpha=0.7)
    # Shade the E_1 correction region
    ax.fill_between(u_plot, delta_rat, 0, alpha=0.15, color='blue')
    ax.set_xlabel(r'Spectral parameter $u$', fontsize=12)
    ax.set_ylabel(r'$\Delta\chi(u, \tau\!=\!i)$', fontsize=12)
    ax.set_title(r'$E_1$ correction (departure from Verlinde limit)', fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 3: Eigenvalue comparison (rational vs elliptic, one period)
    ax = axes[1, 0]
    # Rational on same domain
    lam_rat_fund = (u_plot_ell - hbar_f) / (u_plot_ell + hbar_f)
    ax.plot(u_plot_ell, lam_rat_fund, 'b-', linewidth=2,
            label=r'Rational: $\frac{u-\hbar}{u+\hbar}$')
    ax.plot(u_plot_ell, lam_0_ell_arr, 'r--', linewidth=2,
            label=r'Elliptic: $\frac{\theta_1(u\!-\!\hbar|\tau)}{\theta_1(u\!+\!\hbar|\tau)}$')
    ax.axhline(y=0, color='gray', linestyle=':', linewidth=1)
    ax.axhline(y=1, color='gray', linestyle=':', linewidth=0.5)
    ax.axhline(y=-1, color='gray', linestyle=':', linewidth=0.5)
    ax.axvline(x=hbar_f, color='orange', linestyle='--', linewidth=1, alpha=0.7,
               label=r'$u=\hbar$')
    ax.set_xlabel(r'$u$ (one fundamental period)', fontsize=12)
    ax.set_ylabel(r'$\lambda_0(u)$', fontsize=12)
    ax.set_title(r'Singlet eigenvalue: rational vs elliptic ($\tau=i$)', fontsize=11)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: interpolation ratio chi_R / chi_Verlinde
    ax = axes[1, 1]
    ratio_rat = chi_R_rat / chi_verl_f
    ax.plot(u_plot, ratio_rat, 'b-', linewidth=2.5, label='Rational')
    ax.axhline(y=1, color='gray', linestyle=':', linewidth=1.2, label='Verlinde (=1)')
    singlet_closed_ratio = chi_1_f / chi_verl_f
    ax.axhline(y=singlet_closed_ratio, color='green', linestyle=':', linewidth=1.2,
               label=f'Singlet closed (={singlet_closed_ratio:.4f})')
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.3)
    ax.axvline(x=hbar_f, color='orange', linestyle='--', linewidth=1, alpha=0.7)
    # Shade interpolation
    ax.fill_between(u_plot, ratio_rat, 1.0, alpha=0.1, color='blue')
    ax.set_xlabel(r'Spectral parameter $u$', fontsize=12)
    ax.set_ylabel(r'$\chi_R(u, i)\, /\, \chi_R(\infty, i)$', fontsize=12)
    ax.set_title(r'Interpolation ratio (1 = Verlinde limit)', fontsize=11)
    ax.legend(fontsize=9, loc='lower right')
    ax.set_ylim(-1.0, 1.3)
    ax.grid(True, alpha=0.3)

    fig.suptitle(r'R-matrix character $\chi_R(u, \tau)$ for $Y_\hbar(\mathfrak{sl}_2)$, level $k\!=\!2$, $\hbar\!=\!1/4$',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/Users/raeez/chiral-bar-cobar/standalone/chi_R_plot.png', dpi=150, bbox_inches='tight')
    print(f"  Plot saved to chi_R_plot.png")

    # ────────────────────────────────────────────────────────────
    # Additional tau variation
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("TAU VARIATION: chi_R at u = hbar for several tau")
    print(f"{'='*72}")
    print(f"  At u = hbar, chi_R = chi_1(tau) (pure triplet).")
    print(f"  At u = inf,  chi_R = chi_0(tau) + chi_1(tau) (Verlinde).")
    print(f"\n  {'Im(tau)':>10s}  {'chi_0':>18s}  {'chi_1':>18s}  {'chi_Verl':>18s}  {'chi_R(hbar)':>18s}")
    print(f"  {'---':>10s}  {'---':>18s}  {'---':>18s}  {'---':>18s}  {'---':>18s}")

    for im_tau in [mpf(1)/2, mpf(3)/4, mpf(1), mpf(3)/2, mpf(2), mpf(3)]:
        tau_val = mpc(0, im_tau)
        c0 = re(affine_sl2_character_direct(mpf(0), tau_val, k, 300))
        c1 = re(affine_sl2_character_direct(mpf(1), tau_val, k, 300))
        verl = c0 + c1
        print(f"  {nstr(im_tau, 5):>10s}  {nstr(c0, 14):>18s}  {nstr(c1, 14):>18s}  "
              f"{nstr(verl, 14):>18s}  {nstr(c1, 14):>18s}")

    # ────────────────────────────────────────────────────────────
    # Summary
    # ────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("SUMMARY")
    print(f"{'='*72}")

    print(f"""
  DEFINITION (sl_2, level k=2, fundamental x fundamental):

      chi_R(u, tau) = Sum_J lambda_J(u) * N_{{1/2,1/2}}^J * chi_J(tau)

  EXPLICIT FORMULA:

      chi_R(u, tau) = [(u - 1/4)/(u + 1/4)] * chi_0(tau) + chi_1(tau)

  DECOMPOSITION:

      chi_R(u, tau) = chi_Verlinde(tau) - [1/(2(u + 1/4))] * chi_0(tau)
                    = [E_inf part]       + [E_1 correction]

  NUMERICAL VALUES AT tau = i:

      chi_0(i)         = {nstr(re(chi_0), 20)}
      chi_{{1/2}}(i)     = {nstr(re(chi_half), 20)}
      chi_1(i)         = {nstr(re(chi_1), 20)}
      chi_Verlinde(i)  = {nstr(chi_verlinde, 20)}

  THREE REGIMES:

      u = 0     :  chi_R = chi_1 - chi_0 = {nstr(chi_at_0, 15)}   (singlet reflected)
      u = hbar  :  chi_R = chi_1         = {nstr(chi_at_hbar, 15)}   (singlet closed)
      u = inf   :  chi_R = chi_0 + chi_1 = {nstr(chi_verlinde, 15)}   (Verlinde)

  MODULAR PROPERTIES:

      NOT a modular form (S-transform mixes in chi_{{1/2}}).
      NOT a Jacobi form (rational u-dependence, not theta-type).

      chi_R in Rat_1(u) tensor VVMF(SL_2(Z), rho_{{k=2}})

      Under S: tau -> -1/tau:
          chi_R(u, -1/tau) = [u/(u+hbar)] * (chi_0 + chi_1)
                           + [(u-hbar)/((u+hbar)*sqrt(2))] * chi_{{1/2}}

  ELLIPTIC UPLIFT:

      lambda_0^ell(u, tau) = theta_1(u - hbar | tau) / theta_1(u + hbar | tau)

      Recovers the rational version as tau -> i*infinity (q -> 0).
      The elliptic chi_R^ell is meromorphic Jacobi-type in u,
      but still not a standard Jacobi form due to the S-matrix mixing.
""")

    return chars


if __name__ == "__main__":
    chars = main()
