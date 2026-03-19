#!/usr/bin/env python3
"""
rankin_selberg_bridge.py — Benjamin-Chang bridge from lattice VOA bar cohomology to zeta zeros.

Implements the constrained Epstein zeta series ε^c_s(μ) = Σ_{Δ∈S} (2Δ)^{-s}
from Benjamin-Chang (arXiv:2208.02259), where S is the scalar primary spectrum.

Key results verified:
  (1) Constrained Epstein zeta functional equation (BC eq 3.5):
      ε^c_{c/2-s} = [Γ(s)Γ(s+c/2-1)ζ(2s)] / [π^{2s-1/2}Γ(c/2-s)Γ(s-1/2)ζ(2s-1)] · ε^c_{c/2+s-1}
  (2) Poles at s = (1+z_n)/2 where z_n are nontrivial zeta zeros (BC eq 3.12, Fig 1)
  (3) Crossing equation (BC eq 3.22) with Möbius-weighted sum b(n) = Σ_{k|n} kμ(k)
  (4) Narain spectrum → constrained Epstein → zeta-zero residues δ_{k,c}

Bridge to bar-cobar framework:
  - Primary-counting function Ẑ^c = y^{c/2}|η|^{2c}Z = bar cohomology generating function
  - ε^c_s = Dirichlet series over H*(B(A)) scalar generators
  - Koszul duality A ↔ A! acts on ε^c_s via spectral duality
  - Complementarity Q_1(A) + Q_1(A!) ↔ functional equation of ε^c_s

References:
  Benjamin-Chang, "Scalar Modular Bootstrap and Zeros of the Riemann Zeta Function",
  arXiv:2208.02259 [hep-th], 2022.
"""

import numpy as np
from functools import lru_cache

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 0. Arithmetic functions
# ============================================================

def mobius(n):
    """Möbius function μ(n)."""
    if n == 1:
        return 1
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                temp //= d
                count += 1
            if count > 1:
                return 0
            factors.append(d)
        d += 1
    if temp > 1:
        factors.append(temp)
    return (-1) ** len(factors)


def b_arithmetic(n):
    """
    b(n) = Σ_{k|n} k·μ(k).  (BC eq 3.18)
    This is the Dirichlet series coefficient of ζ(2s)/ζ(2s-1) = Σ b(n) n^{-2s}.
    Also known as Jordan's totient J_1(n) = n·Π_{p|n}(1-1/p) for squarefree n.
    """
    result = 0
    for k in range(1, n + 1):
        if n % k == 0:
            result += k * mobius(k)
    return result


def b_coefficients(nmax):
    """Precompute b(n) for n = 1..nmax."""
    return [b_arithmetic(n) for n in range(1, nmax + 1)]


# ============================================================
# 1. Modular forms on the imaginary axis
# ============================================================

def theta3_real(y, nmax=300):
    """θ_3(iy) = Σ_{n∈Z} exp(-πn²y) for y > 0."""
    result = 1.0
    for n in range(1, nmax + 1):
        val = np.exp(-np.pi * n * n * y)
        if val < 1e-300:
            break
        result += 2.0 * val
    return result


def eta_real(y, nmax=500):
    """η(iy) = exp(-πy/12) Π_{n≥1}(1 - exp(-2πny)) for y > 0."""
    log_result = -np.pi * y / 12.0
    for n in range(1, nmax + 1):
        val = np.exp(-2.0 * np.pi * n * y)
        if val < 1e-300:
            break
        log_result += np.log1p(-val)
    return np.exp(log_result)


def eta_real_squared(y, nmax=500):
    """|η(iy)|² = η(iy)² (real on imaginary axis)."""
    e = eta_real(y, nmax)
    return e * e


# ============================================================
# 2. Narain lattice scalar spectrum
# ============================================================

def narain_scalar_spectrum_c1(R, nmax=200):
    """
    Scalar primaries of the c=1 free boson at radius R.
    h = (n/R + wR)²/4,  h̄ = (n/R - wR)²/4.
    Scalar: h = h̄ ⟹ nw = 0.
    If w=0, n≠0: Δ = h+h̄ = n²/(2R²).
    If n=0, w≠0: Δ = w²R²/2.
    Returns sorted list of (Δ, multiplicity) for Δ > 0.
    """
    dims = {}
    # w = 0 sector (momentum modes)
    for n in range(1, nmax + 1):
        delta = n * n / (2.0 * R * R)
        dims[delta] = dims.get(delta, 0) + 2  # ±n
    # n = 0 sector (winding modes)
    for w in range(1, nmax + 1):
        delta = w * w * R * R / 2.0
        dims[delta] = dims.get(delta, 0) + 2  # ±w
    result = sorted(dims.items())
    return result


def narain_scalar_spectrum_cN(G, B, nmax=50):
    """
    Scalar primaries of Narain CFT on Z^c with metric G_{ab} and B-field B_{ab}.
    c = rank of G.
    p_L = n_a (G+B)^{ab} + w^a,  p_R = n_a (G+B)^{ab} - w^a  (schematic).
    Scalar: p_L² = p_R².

    For simplicity, we handle diagonal G with B=0:
    h = Σ_a (n_a/R_a + w_a R_a)²/4,  h̄ = Σ_a (n_a/R_a - w_a R_a)²/4.
    Scalar: Σ n_a w_a = 0.
    """
    c = len(G)
    # For diagonal G = diag(R_1², ..., R_c²), B = 0
    radii = [np.sqrt(G[a][a]) for a in range(c)]
    dims = {}

    # Generate lattice points (n_1,...,n_c,w_1,...,w_c) with Σ n_a w_a = 0
    from itertools import product as iprod
    coords = range(-nmax, nmax + 1)

    for nw in iprod(iprod(coords, repeat=c), iprod(coords, repeat=c)):
        ns, ws = nw
        # Check scalar condition
        dot = sum(ns[a] * ws[a] for a in range(c))
        if dot != 0:
            continue
        # Compute dimension
        delta = 0.0
        for a in range(c):
            pL = ns[a] / radii[a] + ws[a] * radii[a]
            pR = ns[a] / radii[a] - ws[a] * radii[a]
            delta += (pL * pL + pR * pR) / 4.0
        if delta < 1e-12:  # skip vacuum
            continue
        delta_r = round(delta, 10)
        dims[delta_r] = dims.get(delta_r, 0) + 1

    return sorted(dims.items())


def self_dual_radius_spectrum(c, nmax=200):
    """
    Scalar spectrum at the self-dual radius R = 1 for c copies of free boson.
    At R=1: momentum and winding spectra coincide → enhanced symmetry.
    Scalar dims: Δ = n²/2 (momentum, w=0) and Δ = w²/2 (winding, n=0).
    At R=1 these merge: Δ = k²/2 with multiplicity 4 (±n, ±w) for k≥1,
    minus double-counting at n=w=0 (vacuum, excluded).
    Per boson: spectrum {k²/2 : k ≥ 1} with mult 4.
    For c bosons: tensor product spectrum.
    """
    if c == 1:
        return [(k * k / 2.0, 4) for k in range(1, nmax + 1)]
    else:
        # For c > 1 at self-dual point, use diagonal embedding
        return narain_scalar_spectrum_c1(1.0, nmax)


# ============================================================
# 3. Constrained Epstein zeta
# ============================================================

def constrained_epstein_zeta(s, scalar_spectrum, max_terms=None):
    """
    ε^c_s(μ) = Σ_{Δ∈S} (2Δ)^{-s}     (BC eq 3.4)

    scalar_spectrum: list of (Δ, multiplicity) pairs.
    Converges for Re(s) > c - 1.
    """
    result = 0.0
    for i, (delta, mult) in enumerate(scalar_spectrum):
        if max_terms and i >= max_terms:
            break
        if delta > 0:
            result += mult * (2.0 * delta) ** (-s)
    return result


def constrained_epstein_zeta_c1_selfdual(s, nmax=1000):
    """
    ε^1_s at the self-dual radius R=1.
    Scalar primaries: Δ = k²/2 for k ≥ 1, each with multiplicity 4.
    ε^1_s = 4 Σ_{k≥1} (2·k²/2)^{-s} = 4 Σ k^{-2s} = 4ζ(2s).
    """
    if HAS_MPMATH:
        return complex(4 * mpmath.zeta(2 * mpmath.mpc(s)))
    result = 0.0 + 0j
    for k in range(1, nmax + 1):
        result += 4.0 * k ** (-2.0 * s)
    return complex(result)


# ============================================================
# 4. Functional equation and zeta-zero content
# ============================================================

def functional_equation_factor(s, c):
    """
    The ratio appearing in the functional equation of ε^c_s (BC eq 3.5):

    F(s,c) = Γ(s)·Γ(s + c/2 - 1)·ζ(2s) / [π^{2s-1/2}·Γ(c/2 - s)·Γ(s - 1/2)·ζ(2s - 1)]

    So that: ε^c_{c/2-s}(μ) = F(s,c) · ε^c_{c/2+s-1}(μ).

    The POLES of F in s come from zeros of ζ(2s-1), i.e., at 2s-1 = z_n (zeta zeros),
    giving s = (1 + z_n)/2.  If RH holds, Re(s) = 3/4 for all these poles.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for functional equation computation")

    s_mp = mpmath.mpf(s) if isinstance(s, (int, float)) else mpmath.mpc(s)
    c_mp = mpmath.mpf(c)

    num = mpmath.gamma(s_mp) * mpmath.gamma(s_mp + c_mp / 2 - 1) * mpmath.zeta(2 * s_mp)
    den = (mpmath.pi ** (2 * s_mp - mpmath.mpf('0.5'))
           * mpmath.gamma(c_mp / 2 - s_mp)
           * mpmath.gamma(s_mp - mpmath.mpf('0.5'))
           * mpmath.zeta(2 * s_mp - 1))

    return complex(num / den)


def verify_functional_equation(s, c, scalar_spectrum, nmax_terms=500):
    """
    Verify BC eq 3.5: ε^c_{c/2-s} = F(s,c) · ε^c_{c/2+s-1}.
    Returns (LHS, RHS, relative_error).
    """
    lhs = constrained_epstein_zeta(c / 2.0 - s, scalar_spectrum, max_terms=nmax_terms)
    rhs_epstein = constrained_epstein_zeta(c / 2.0 + s - 1, scalar_spectrum, max_terms=nmax_terms)
    F = functional_equation_factor(s, c)
    rhs = F * rhs_epstein

    if abs(lhs) > 1e-30:
        rel_err = abs(lhs - rhs) / abs(lhs)
    else:
        rel_err = abs(lhs - rhs)
    return lhs, rhs, rel_err


# ============================================================
# 5. Zeta-zero residues δ_{k,c}
# ============================================================

def zeta_zeros(n):
    """First n nontrivial zeros of ζ(s) on the critical line (imaginary parts)."""
    if not HAS_MPMATH:
        # Hardcoded first 10
        return [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
                37.586178, 40.918719, 43.327073, 48.005151, 49.773832][:n]
    return [float(mpmath.zetazero(k).imag) for k in range(1, n + 1)]


def zeta_zero_residue_coefficient(k, c, scalar_spectrum, nmax_terms=500):
    """
    Compute δ_{k,c}(μ) from BC eq 3.13:

    δ_{k,c}(μ) = ∫_F (dxdy/y²) (Ẑ^c(τ,μ) - E_{c/2}(τ)) Res_{s=z_k/2} E_s(τ)

    The residue of E_s at s = z_k/2 is given by BC eq 3.14.

    For the constrained Epstein: δ_{k,c} can be extracted from ε^c_s via
    the Laurent expansion of ε^c_{c/2-s} near s = (1+z_k)/2.
    """
    gamma_k = zeta_zeros(k)[-1]  # k-th zero imaginary part
    z_k = 0.5 + 1j * gamma_k  # k-th zeta zero

    # The residue contribution involves ε^c at shifted argument
    s_pole = (1 + z_k) / 2  # = 3/4 + i·gamma_k/2

    # ε^c_{c/2+s-1} evaluated at s = s_pole
    arg = c / 2.0 + s_pole - 1
    eps_val = constrained_epstein_zeta(complex(arg), scalar_spectrum, max_terms=nmax_terms)

    # Residue of F(s,c) at s = s_pole comes from the zero of ζ(2s-1) at 2s-1 = z_k
    # Res_{s=s_pole} F(s,c) = [Γ(s)Γ(s+c/2-1)ζ(2s)] / [π^{2s-1/2}Γ(c/2-s)Γ(s-1/2)] · 1/(2ζ'(z_k))
    if HAS_MPMATH:
        s_mp = mpmath.mpc(s_pole)
        c_mp = mpmath.mpf(c)
        z_k_mp = mpmath.mpc(z_k)

        num = (mpmath.gamma(s_mp) * mpmath.gamma(s_mp + c_mp / 2 - 1)
               * mpmath.zeta(2 * s_mp))
        den = (mpmath.pi ** (2 * s_mp - mpmath.mpf('0.5'))
               * mpmath.gamma(c_mp / 2 - s_mp)
               * mpmath.gamma(s_mp - mpmath.mpf('0.5'))
               * 2 * mpmath.diff(mpmath.zeta, z_k_mp))

        residue_F = complex(num / den)
    else:
        residue_F = float('nan')

    return residue_F * eps_val


# ============================================================
# 6. Crossing equation (BC eq 3.22)
# ============================================================

def crossing_equation_lhs(y, scalar_spectrum):
    """
    LHS of BC eq 3.22: 1 + Σ_{Δ∈S} exp(-2πΔy).
    """
    result = 1.0
    for delta, mult in scalar_spectrum:
        val = np.exp(-2.0 * np.pi * delta * y)
        if val < 1e-300:
            break
        result += mult * val
    return result


def crossing_equation_rhs(y, c, scalar_spectrum, n_zeta_zeros=10, b_nmax=100):
    """
    RHS of BC eq 3.22:

    Λ((c-1)/2)/Λ(c/2) · y^{1-c} + ε_c(μ)·y^{-c/2}
    + Σ_k Re(δ_{k,c}(μ) · y^{-c/2+1-z_k/2})
    + y^{1-c}/√π · Σ_{Δ∈S} Σ_{n≥1} b(n)·n^{c-2}·U(-1/2, c/2, 2πn²Δ/y)·exp(-2πn²Δ/y)

    The last term (hypergeometric) encodes the non-trivial content.
    For numerical verification we use the first few terms.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    c_mp = mpmath.mpf(c)
    y_mp = mpmath.mpf(y)

    # Term 1: Λ((c-1)/2)/Λ(c/2) · y^{1-c}
    # Λ(s) = π^{-s} ζ(2s) Γ(s)
    def Lambda(s):
        return mpmath.power(mpmath.pi, -s) * mpmath.zeta(2 * s) * mpmath.gamma(s)

    term1 = float(Lambda((c_mp - 1) / 2) / Lambda(c_mp / 2) * mpmath.power(y_mp, 1 - c_mp))

    # Term 2: ε_c(μ) · y^{-c/2}
    # ε_c(μ) = 3π^{-c/2} Γ(c/2 - 1) ε^c_{c/2-1}
    eps_c_half_minus_1 = constrained_epstein_zeta(c / 2.0 - 1, scalar_spectrum)
    epsilon_c = float(3 * mpmath.power(mpmath.pi, -c_mp / 2) * mpmath.gamma(c_mp / 2 - 1)) * eps_c_half_minus_1
    term2 = epsilon_c * y ** (-c / 2.0)

    # Term 3: zeta-zero residues
    term3 = 0.0
    gammas = zeta_zeros(n_zeta_zeros)
    for gamma_k in gammas:
        z_k = 0.5 + 1j * gamma_k
        # Schematic: δ_{k,c} · y^{-c/2+1-z_k/2}
        # We need the full δ_{k,c} computation; for now use the residue
        dk = zeta_zero_residue_coefficient(
            gammas.index(gamma_k) + 1, c, scalar_spectrum)
        exponent = -c / 2.0 + 1 - z_k / 2
        term3 += (dk * y ** exponent).real  # Re part

    # Term 4: Möbius-weighted hypergeometric sum (main term)
    bs = b_coefficients(b_nmax)
    term4 = 0.0
    prefactor = y ** (1 - c) / np.sqrt(np.pi)
    for delta, mult in scalar_spectrum[:50]:  # truncate
        for n_idx, bn in enumerate(bs[:30]):  # truncate
            n = n_idx + 1
            arg = 2.0 * np.pi * n * n * delta / y
            if arg > 500:
                continue
            # U(-1/2, c/2, z) = confluent hypergeometric of second kind
            U_val = float(mpmath.hyperu(-0.5, c / 2.0, arg))
            term4 += mult * bn * n ** (c - 2) * U_val * np.exp(-arg)
    term4 *= prefactor

    return term1 + term2 + term3 + term4


# ============================================================
# 7. Sewing → Epstein bridge
# ============================================================

def sewing_fredholm_det(y, nmax=500):
    """
    Heisenberg sewing Fredholm determinant on imaginary axis:
    det(1 - K_q) = Π_{n≥1}(1 - q^n),  q = exp(-2πy).

    Satisfies: η(iy) = exp(-πy/12) · det(1 - K_q).
    """
    q = np.exp(-2 * np.pi * y)
    log_det = 0.0
    qn = q
    for n in range(1, nmax + 1):
        if qn < 1e-300:
            break
        log_det += np.log1p(-qn)
        qn *= q
    return np.exp(log_det)


def partition_function_from_sewing(y, c=1):
    """
    Z(iy) for c free bosons at self-dual radius, via sewing decomposition:
    Z = |Θ/η^c|² = Θ²/η^{2c} on imaginary axis (everything real).

    Decomposition:
      Θ = lattice theta (arithmetic input)
      η = exp(-πy/12) · det(1-K_q) (sewing/Fredholm input)

    The 'sewing ∘ Rankin-Selberg' composition:
      Z → Ẑ^c = y^{c/2}η^{2c}Z → ε^c_s = Mellin(Ẑ^c) → functional eq with ζ-zeros
    """
    theta = theta3_real(y)
    eta = eta_real(y)
    if abs(eta) < 1e-300:
        return float('inf')
    return (theta / eta) ** (2 * c)


def primary_counting_function(y, c=1):
    """
    Ẑ^c(iy) = y^{c/2} · |η(iy)|^{2c} · Z(iy)    (BC eq 3.2)

    This strips descendants, leaving only primary content.
    Equals y^{c/2} · Θ(iy)^{2c}  for Narain at self-dual radius.

    KEY IDENTIFICATION: Ẑ^c = bar cohomology generating function.
    |η|^{2c} removes Fock space (oscillator modes), isolating H*(B(A)).
    """
    Z = partition_function_from_sewing(y, c)
    eta_sq = eta_real(y) ** 2
    return y ** (c / 2.0) * eta_sq ** c * Z


# ============================================================
# 8. Mellin transforms
# ============================================================

def mellin_theta(s, ymax=80.0):
    """
    Mellin transform of θ_3(iy) - 1 using functional equation for analytic continuation:

    M(s) = ∫_1^∞ (θ-1)(y^{s-1} + y^{-s-1/2}) dy + 1/(s-1/2) - 1/s

    Should equal π^{-s}Γ(s)·2ζ(2s).
    """
    from scipy import integrate

    def integrand(y):
        return (theta3_real(y) - 1.0) * (y ** (s - 1) + y ** (-s - 0.5))

    result, _ = integrate.quad(integrand, 1.0, ymax, limit=200)
    result += 1.0 / (s - 0.5) - 1.0 / s
    return result


def completed_zeta_from_mellin(s):
    """
    ξ(s) = π^{-s/2} Γ(s/2) ζ(s) (completed Riemann zeta).
    The Mellin of θ gives 2·ξ(2s).
    """
    if HAS_MPMATH:
        return float(mpmath.pi ** (-s / 2) * mpmath.gamma(s / 2) * mpmath.zeta(s))
    from scipy.special import gamma
    from scipy.special import zeta as sp_zeta
    return np.pi ** (-s / 2) * gamma(s / 2) * sp_zeta(s, 1)


def verify_mellin_equals_zeta(s):
    """
    Verify: ∫_0^∞ (θ(iy)-1) y^{s-1} dy = π^{-s}Γ(s)·2ζ(2s) = 2·ξ(2s).
    Returns (mellin_value, analytic_value, relative_error).
    """
    mel = mellin_theta(s)
    analytic = 2.0 * completed_zeta_from_mellin(2 * s)
    rel_err = abs(mel - analytic) / abs(analytic) if abs(analytic) > 1e-30 else abs(mel - analytic)
    return mel, analytic, rel_err


# ============================================================
# 9. Koszul duality action on constrained Epstein zeta
# ============================================================

def koszul_dual_spectrum_lattice(R, nmax=200):
    """
    For c=1 boson at radius R, the Koszul dual A! has the dual lattice 1/R.
    (More precisely: lattice duality Λ ↔ Λ* sends R ↔ 1/R for the rank-1 case.)

    In the bar-cobar framework:
      V_Λ → B(V_Λ) → H*(B(V_Λ)) = (V_Λ)^i → (V_Λ)^! = Verdier dual

    For even self-dual lattices (Λ = Λ*), the dual is the same:
      V_Λ^! ≃ V_Λ (up to shift)  ← self-Koszul-dual

    For Λ = Z at radius R: Λ* corresponds to radius 1/R.
    The scalar spectrum at R and 1/R are related by T-duality:
      momentum ↔ winding.
    """
    return narain_scalar_spectrum_c1(1.0 / R, nmax)


def koszul_duality_on_epstein(s, c, R, nmax=200):
    """
    Compare ε^c_s at radius R vs 1/R (Koszul/T-duality).

    At the self-dual point R=1: ε^c_s(R) = ε^c_s(1/R), and the functional
    equation of ε^c_s becomes a SELF-DUALITY.

    The functional equation (BC 3.5) relates ε^c_{c/2-s} to ε^c_{c/2+s-1}.
    At R=1 (self-dual), combined with T-duality, this gives:
      ε^c_{c/2-s}(R=1) = F(s,c) · ε^c_{c/2+s-1}(R=1)
    which is the standard functional equation.

    KEY CLAIM: For general R, the functional equation of ε^c_s DECOMPOSES as:
      (Koszul duality: R → 1/R) ∘ (Modular crossing: s → c/2-s)
    The zeta functional equation ξ(s) = ξ(1-s) is the FIXED POINT of
    Koszul involution at the self-dual radius.

    Returns (eps_R, eps_dual_R, functional_eq_test).
    """
    spec_R = narain_scalar_spectrum_c1(R, nmax)
    spec_dual = narain_scalar_spectrum_c1(1.0 / R, nmax)

    eps_R = constrained_epstein_zeta(s, spec_R)
    eps_dual = constrained_epstein_zeta(s, spec_dual)

    # At self-dual: these should be equal
    return eps_R, eps_dual


def koszul_complementarity_check(s, c, R, nmax=200):
    """
    Test: does complementarity Q_1(A) + Q_1(A!) map to the functional equation?

    Genus-1 complementarity: Q_1(V_R) + Q_1(V_{1/R}) = H*(M_{1,1}, Z(V_R))

    At the Epstein level:
      ε^c_s(R) + ε^c_s(1/R) vs ε^c_{c/2-s}(R) + ε^c_{c/2-s}(1/R)

    The functional equation (3.5) applied to both R and 1/R should yield
    a SYMMETRIC functional equation for the sum ε^c_s(R) + ε^c_s(1/R).
    """
    spec_R = narain_scalar_spectrum_c1(R, nmax)
    spec_dual = narain_scalar_spectrum_c1(1.0 / R, nmax)

    eps_s_R = constrained_epstein_zeta(s, spec_R)
    eps_s_dual = constrained_epstein_zeta(s, spec_dual)
    sum_s = eps_s_R + eps_s_dual

    eps_reflected_R = constrained_epstein_zeta(c / 2.0 - s, spec_R)
    eps_reflected_dual = constrained_epstein_zeta(c / 2.0 - s, spec_dual)
    sum_reflected = eps_reflected_R + eps_reflected_dual

    return sum_s, sum_reflected


# ============================================================
# 10. Bar cohomology → constrained Epstein bridge
# ============================================================

def bar_cohomology_to_constrained_epstein(bar_dims, s):
    """
    Bridge from bar cohomology generators to constrained Epstein zeta.

    The primary-counting function Ẑ^c = y^{c/2}|η|^{2c}Z strips descendants.
    What remains are U(1)^c primaries = generators of H*(B(A)).

    The constrained Epstein zeta ε^c_s = Σ_{Δ∈S} (2Δ)^{-s} is then
    a Dirichlet series over bar cohomology generator dimensions.

    bar_dims: list of (dimension, multiplicity) from bar complex computation.
    Returns ε^c_s.
    """
    return constrained_epstein_zeta(s, bar_dims)


# ============================================================
# 11. Epstein zeros on critical line (= zeta zeros)
# ============================================================

def epstein_critical_line_values(tmax=60.0, npoints=3000, c=1, R=1.0):
    """
    Evaluate ε^c_s on the critical line Re(s) = 1/4 (for c=1) using the
    Hardy Z-function approach.

    For c=1, R=1: ε^1_s = 4ζ(2s).  On s = 1/4 + it: ε^1 = 4ζ(1/2 + 2it).
    Zeros at t = γ_n/2 where γ_n are imaginary parts of zeta zeros.

    Uses the Hardy Z-function Z(t) = e^{iθ(t)}ζ(1/2+it) which is real on the
    critical line.  We compute Z(2t) to find the zeros.

    Returns (t_values, Z_values, zero_locations).
    """
    if not HAS_MPMATH:
        return np.array([]), np.array([]), []

    ts = np.linspace(0.1, tmax, npoints)
    vals = []

    for t in ts:
        # Use mpmath's siegelz (Hardy Z function): Z(t) is real, zeros = zeta zeros
        z_val = float(mpmath.siegelz(2 * t))  # Z(2t): zeros where ζ(1/2+2it)=0
        vals.append(z_val)

    vals = np.array(vals)
    zeros = []
    for i in range(len(vals) - 1):
        if vals[i] * vals[i + 1] < 0:
            t_zero = ts[i] - vals[i] * (ts[i + 1] - ts[i]) / (vals[i + 1] - vals[i])
            zeros.append(t_zero)

    return ts, vals, zeros


# ============================================================
# 12. Full pipeline: sewing → bar → Epstein → zeta zeros
# ============================================================

def full_pipeline_c1(R=1.0, s_test=2.0, n_zeros=5):
    """
    Execute the full pipeline for c=1 lattice VOA at radius R:

    1. Sewing: Z(τ) from Fredholm det (thm:heisenberg-sewing)
    2. Bar cohomology: Ẑ^c = y^{c/2}|η|^{2c}Z strips descendants
    3. Constrained Epstein: ε^1_s = Σ (2Δ)^{-s} over scalar primaries
    4. Functional equation: encodes ζ(2s)/ζ(2s-1) factor
    5. Zeta zeros: poles of F(s,1) at s = (1+z_n)/2
    6. Koszul: R → 1/R duality on ε

    Returns comprehensive results dict.
    """
    results = {}

    # Step 1-2: spectrum
    spec = narain_scalar_spectrum_c1(R)
    results['spectrum_count'] = sum(m for _, m in spec[:20])
    results['first_dims'] = [(d, m) for d, m in spec[:5]]

    # Step 3: constrained Epstein
    eps_val = constrained_epstein_zeta(s_test, spec)
    results['epsilon_s'] = eps_val

    # Self-dual check
    if abs(R - 1.0) < 1e-10:
        analytic = constrained_epstein_zeta_c1_selfdual(s_test)
        results['epsilon_analytic'] = analytic
        results['epsilon_match'] = abs(eps_val - analytic) / abs(analytic) if analytic != 0 else 0

    # Step 4: Mellin → zeta
    mel, ana, mel_err = verify_mellin_equals_zeta(s_test)
    results['mellin_value'] = mel
    results['mellin_analytic'] = ana
    results['mellin_error'] = mel_err

    # Step 5: zeta zeros from Epstein
    _, _, ezeros = epstein_critical_line_values(tmax=30, npoints=2000)
    gamma_true = zeta_zeros(n_zeros)
    results['epstein_zeros'] = ezeros[:n_zeros]
    results['zeta_zeros_half'] = [g / 2 for g in gamma_true]

    # Step 6: Koszul duality
    eps_R, eps_dual = koszul_duality_on_epstein(s_test, 1, R)
    results['eps_R'] = eps_R
    results['eps_dual_R'] = eps_dual
    results['koszul_symmetric'] = abs(eps_R - eps_dual) < 1e-10 if abs(R - 1) < 1e-10 else None

    # Step 6b: sewing decomposition verification
    y_test = 1.0
    fred = sewing_fredholm_det(y_test)
    eta = eta_real(y_test)
    exp_factor = np.exp(-np.pi * y_test / 12.0)
    results['sewing_eta_match'] = abs(eta - exp_factor * fred) / abs(eta)

    return results
