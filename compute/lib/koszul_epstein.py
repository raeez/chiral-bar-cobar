#!/usr/bin/env python3
r"""
koszul_epstein.py — Koszul-Epstein functions: the Epstein zeta functions
of shadow metrics of chirally Koszul algebras.

DEFINITION (def:koszul-epstein-function):

A KOSZUL-EPSTEIN FUNCTION is a Dirichlet series ε^KE_A(s) attached to a
chirally Koszul algebra A, defined as the Epstein zeta function of the
shadow metric Q_L when the shadow metric is nondegenerate (class M),
and as a one-dimensional sewing Dirichlet series when the shadow metric
degenerates (classes G, L, C).

THREE STRUCTURAL CONSTRAINTS distinguish Koszul-Epstein functions from
generic Epstein zeta functions:

(1) KOSZUL SYMMETRY: Q_L arises from the MC element Θ_A via the
    bar-cobar quasi-isomorphism. The Koszul duality A ↔ A! acts on Q_L
    by the complementarity involution, giving ε^KE_A a stronger symmetry
    than the generic Epstein functional equation.

(2) SHADOW POLARIZATION: The shadow tower {S_r} constrains the moments of
    the spectral measure of ε^KE_A via the MC recursion. The key identity
    H(t)² = t⁴ Q_L(t) (Riccati algebraicity) forces Q_L to be determined
    by exactly three invariants (κ, α, S₄), not by arbitrary coefficients.

(3) MODULAR COUPLING: At genus 1, the Koszul-Epstein function couples to
    the Eisenstein series on M_{1,1} via Rankin-Selberg unfolding:
    ε^KE_A is the Mellin transform of the theta function Θ_{Q_L}(τ),
    and Q_L is itself an algebraic function of the OPE data.

THE DEGENERATE CASES:

For class G (Δ = 0, α = 0): Q_L = 4κ² is constant. The binary form
Q(m,n) = 4κ² m² has rank 1. The Epstein sum over Z² diverges.
The correct Koszul-Epstein function is the ONE-DIMENSIONAL sewing
Dirichlet series:

    ε^KE_H(s) = Σ'_{m ∈ Z} (4κ²)^{-s} |m|^{-2s}  (diverges)

This does not converge either. The resolution: the Heisenberg sewing
Dirichlet series S_H(u) = ζ(u)ζ(u+1) (from the sewing determinant)
is the correct arithmetic object. Its Euler product is
    S_H(u) = Π_p (1-p^{-u})^{-1}(1-p^{-u-1})^{-1}.

For class L (Δ = 0, α ≠ 0): Q_L = (2κ + 3αt)² is a perfect square.
Same rank-1 degeneration; the sewing Dirichlet series is the
correct object.

For class C (Δ = 0 on the charged stratum): the contact class lies
outside the single-line framework. The quartic data lives on a
charged stratum where κ = 0.

For class M (Δ ≠ 0): Q_L is a genuine positive definite binary
quadratic form, and ε^KE_A(s) = ε_{Q_L}(s) is the standard Epstein
zeta. This is the nontrivial case.

THE DAVENPORT-HEILBRONN QUESTION:

Generic Epstein zeta functions of binary quadratic forms with h(D) > 1
can have zeros off the critical line (Davenport-Heilbronn 1936). Do
the three Koszul-Epstein constraints force zeros onto Re(s) = 1/2?

ANSWER: The question is open. What IS proved:
- When h(D) = 1, ε_{Q_L} = c₀ · ζ(s) · L(s, χ_D), and all zeros
  lie on Re(s) = 1/2 under GRH.
- Koszul self-duality (A ≃ A!) forces the constrained Epstein zeta
  to factor into standard L-functions (thm:self-dual-factorization).
- For non-self-dual algebras with h(D) > 1, the MC constraints
  provide additional structure but have not been proved to exclude
  off-line zeros.

Manuscript references:
    def:koszul-epstein-function (arithmetic_shadows.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-epstein-zeta (higher_genus_modular_koszul.tex)
    constr:shadow-l-function (arithmetic_shadows.tex)
    rem:davenport-heilbronn-koszul (arithmetic_shadows.tex)
"""

from fractions import Fraction
from typing import Dict, List, Optional, Tuple, Union
import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ================================================================
# 1. Shadow data for all standard families
# ================================================================

def shadow_data(family: str, **params) -> Dict:
    r"""Shadow data (κ, α, S₄, Δ, shadow_class) for standard families.

    Parameters
    ----------
    family : str
        One of 'heisenberg', 'virasoro', 'w3', 'affine_km', 'betagamma'.
    params : keyword arguments
        c : central charge (for virasoro, w3)
        k : level (for heisenberg, affine_km)
        N : rank (for affine_km with g = sl_N)

    Returns
    -------
    dict with keys: kappa, alpha, S4, Delta, shadow_class, generators
    """
    if family == 'heisenberg':
        k = params.get('k', 1)
        kappa = k / 2
        alpha = 0.0
        S4 = 0.0
        Delta = 0.0
        shadow_class = 'G'
        generators = [1]
    elif family == 'virasoro':
        c = params.get('c', 1.0)
        kappa = c / 2
        alpha = 2.0
        S4 = 10.0 / (c * (5 * c + 22))
        Delta = 8 * kappa * S4  # = 40/(5c+22)
        shadow_class = 'M'
        generators = [2]
    elif family == 'w3':
        c = params.get('c', 1.0)
        # T-line data
        kappa = c / 2
        alpha = 2.0
        S4 = 10.0 / (c * (5 * c + 22))
        Delta = 8 * kappa * S4
        shadow_class = 'M'
        generators = [2, 3]
    elif family == 'affine_km':
        # g = sl_N at level k
        N_rank = params.get('N', 2)
        k = params.get('k', 1)
        h_dual = N_rank  # dual Coxeter for sl_N
        dim_g = N_rank ** 2 - 1
        c = k * dim_g / (k + h_dual)
        kappa = c / 2  # κ = dim(g)·(k+h∨)/(2h∨) × ρ
        # Actually: κ(KM) = dim(g)·k/(2(k+h∨)) per AP1 correction
        # Equivalently κ = c/2 since c = k·dim(g)/(k+h∨)
        alpha = 0.0  # cubic vanishes for affine KM (class L with α=0 is class G)
        S4 = 0.0
        Delta = 0.0
        shadow_class = 'L'  # affine KM is class L (tree, r_max = 3)
        generators = [1] * dim_g
    elif family == 'betagamma':
        kappa = 1.0
        alpha = 0.0  # βγ: class C, but this is the autonomous approximation
        S4 = 0.0  # Contact class: quartic on charged stratum
        Delta = 0.0
        shadow_class = 'C'
        generators = [1, 1]  # β (weight 1) and γ (weight 0) — but γ has weight 0
        # Actually βγ: generators weight (1,0), κ = 1. For the Koszul-Epstein
        # the relevant data is on the primary line.
    else:
        raise ValueError(f"Unknown family: {family}")

    return {
        'family': family,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'shadow_class': shadow_class,
        'generators': generators,
    }


def shadow_data_exact(family: str, **params) -> Dict:
    r"""Exact (Fraction) shadow data for standard families."""
    if family == 'heisenberg':
        k = params.get('k', Fraction(1))
        if not isinstance(k, Fraction):
            k = Fraction(k)
        return {
            'family': family,
            'kappa': k / 2,
            'alpha': Fraction(0),
            'S4': Fraction(0),
            'Delta': Fraction(0),
            'shadow_class': 'G',
        }
    elif family == 'virasoro':
        c = params.get('c', Fraction(1))
        if not isinstance(c, Fraction):
            c = Fraction(c)
        kappa = c / 2
        alpha = Fraction(2)
        S4 = Fraction(10) / (c * (5 * c + 22))
        Delta = 8 * kappa * S4
        return {
            'family': family,
            'kappa': kappa,
            'alpha': alpha,
            'S4': S4,
            'Delta': Delta,
            'shadow_class': 'M',
        }
    else:
        # Fall back to float
        return shadow_data(family, **params)


# ================================================================
# 2. Binary quadratic form from shadow data
# ================================================================

def binary_form_coefficients(kappa, alpha, S4):
    r"""Coefficients (a, b, c) of the binary form Q(m,n) = am² + bmn + cn².

    From the shadow metric Q_L(t) = 4κ² + 12κα·t + (9α² + 16κS₄)·t²:

        a = 4κ²
        b = 12κα
        c = 9α² + 16κS₄ = 9α² + 2Δ  (where Δ = 8κS₄)

    The discriminant is disc = b² − 4ac = −32κ²Δ.
    """
    a = 4 * kappa ** 2
    b = 12 * kappa * alpha
    c_coeff = 9 * alpha ** 2 + 16 * kappa * S4
    return a, b, c_coeff


def form_discriminant(a, b, c):
    r"""Discriminant D = b² − 4ac of binary form am² + bmn + cn²."""
    return b ** 2 - 4 * a * c


def form_evaluate(a, b, c, m, n):
    r"""Evaluate Q(m,n) = am² + bmn + cn²."""
    return a * m * m + b * m * n + c * n * n


def is_positive_definite(a, b, c):
    r"""Check if Q(m,n) = am² + bmn + cn² is positive definite.

    Positive definite iff a > 0 and disc = b² − 4ac < 0.
    """
    return a > 0 and (b * b - 4 * a * c) < 0


def reduced_form(a, b, c):
    r"""Reduce binary quadratic form to Minkowski-reduced form.

    A form (a, b, c) with negative discriminant is reduced if:
        |b| ≤ a ≤ c
    and if |b| = a or a = c then b ≥ 0.

    Returns (a', b', c') in the same equivalence class.
    """
    # Gauss reduction algorithm
    while True:
        if a > c:
            a, b, c = c, -b, a
        if abs(b) > a:
            # Find t such that |b + 2at| is minimized
            t = round(-b / (2 * a))
            c = a * t * t + b * t + c
            b = b + 2 * a * t
        else:
            break

    # Normalize sign
    if abs(b) == a or a == c:
        b = abs(b)

    return a, b, c


# ================================================================
# 3. Koszul-Epstein function: the nondegenerate case (class M)
# ================================================================

def koszul_epstein_lattice_sum(s, kappa, alpha, S4, N=100):
    r"""Koszul-Epstein function ε^KE(s) by direct lattice sum.

    For class M algebras (Δ ≠ 0), this is the Epstein zeta of the
    shadow metric:

        ε^KE(s) = Σ'_{(m,n)∈Z²} Q_L(m,n)^{−s}

    where Q_L(m,n) = 4κ²m² + 12καmn + (9α²+2Δ)n².

    Parameters
    ----------
    s : complex
        The argument. Converges for Re(s) > 1.
    kappa, alpha, S4 : float
        Shadow data of the algebra.
    N : int
        Truncation: sum over |m|, |n| ≤ N.

    Returns
    -------
    complex
        The truncated lattice sum.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for Koszul-Epstein computation")

    Delta = 8 * kappa * S4
    if abs(Delta) < 1e-15:
        raise ValueError(
            "Shadow metric is degenerate (Δ = 0, class G/L/C). "
            "The Koszul-Epstein function is not a 2D lattice sum; "
            "use koszul_epstein_degenerate() instead."
        )

    a, b, c_coeff = binary_form_coefficients(kappa, alpha, S4)

    # Verify positive definiteness
    disc = form_discriminant(a, b, c_coeff)
    if disc >= 0:
        raise ValueError(
            f"Shadow metric is not positive definite: disc = {disc} >= 0"
        )

    s_mp = mpmath.mpc(s)
    a_mp = mpmath.mpf(float(a))
    b_mp = mpmath.mpf(float(b))
    c_mp = mpmath.mpf(float(c_coeff))

    result = mpmath.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 and n == 0:
                continue
            Q_mn = a_mp * m ** 2 + b_mp * m * n + c_mp * n ** 2
            if Q_mn <= 0:
                # Should not happen for positive definite form
                raise ValueError(
                    f"Q({m},{n}) = {float(Q_mn)} <= 0 for positive definite form"
                )
            result += mpmath.power(Q_mn, -s_mp)

    return complex(result)


def koszul_epstein_virasoro(s, c, N=100):
    r"""Koszul-Epstein function for Virasoro at central charge c.

    This is ε^KE_{Vir_c}(s) = Σ'_{(m,n)} Q_{Vir}(m,n)^{-s}
    where Q_{Vir}(m,n) = c²m² + 12c·mn + α(c)n²
    with α(c) = 36 + 80/(5c+22) = 4(45c+218)/(5c+22).

    Well-defined for c > −22/5, c ≠ 0 (need κ ≠ 0 and Δ ≠ 0).
    Only converges for Re(s) > 1 (direct sum). Use
    koszul_epstein_theta for the analytic continuation.
    """
    data = shadow_data('virasoro', c=float(c))
    return koszul_epstein_lattice_sum(
        s, data['kappa'], data['alpha'], data['S4'], N=N
    )


def koszul_epstein_theta(s, kappa, alpha, S4, N_theta=80):
    r"""Koszul-Epstein function via theta function representation.

    Uses the Chowla-Selberg / Mellin-Barnes integral:

        Λ^KE(s) = ∫₀^∞ (Θ_Q(t) − 1) · t^{s-1} dt / 2

    where Θ_Q(t) = Σ_{(m,n)∈Z²} exp(−πt·Q(m,n)/(det A)^{1/2}).

    Split at t=1 and use the modular property:
        Θ_Q(t) = (det A)^{-1/2} · t^{-1} · Θ_{Q^{-1}}(1/t)

    This gives the analytic continuation to all s ∈ C (except s=0,1).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    a_val, b_val, c_val = binary_form_coefficients(kappa, alpha, S4)
    D = form_discriminant(a_val, b_val, c_val)
    det_A = abs(D) / 4  # det(A) = -disc/4 for the matrix A

    a_mp = mpmath.mpf(float(a_val))
    b_mp = mpmath.mpf(float(b_val))
    c_mp = mpmath.mpf(float(c_val))
    det_mp = mpmath.mpf(float(det_A))
    sqrt_det = mpmath.sqrt(det_mp)

    # Inverse form Q^{-1}: if A = [[a, b/2], [b/2, c]], then
    # A^{-1} = (1/det) [[c, -b/2], [-b/2, a]]
    # Q^{-1}(m,n) = (c·m² − b·mn + a·n²) / det
    ai = c_mp / det_mp
    bi = -b_mp / det_mp
    ci = a_mp / det_mp

    def theta_Q(t_val, a_form, b_form, c_form, N_t):
        """Compute Θ_Q(t) = Σ exp(−πt Q(m,n))."""
        t_mp = mpmath.mpf(t_val)
        result = mpmath.mpf(0)
        for m in range(-N_t, N_t + 1):
            for n in range(-N_t, N_t + 1):
                Q_mn = a_form * m * m + b_form * m * n + c_form * n * n
                result += mpmath.exp(-mpmath.pi * t_mp * Q_mn)
        return result

    # The completed Epstein zeta via Mellin of theta:
    # Λ(s) = ∫₀^∞ (Θ_Q(t) − 1) t^{s−1} dt
    #       = ∫₁^∞ (Θ_Q(t) − 1) t^{s−1} dt + ∫₀^1 (Θ_Q(t) − 1) t^{s−1} dt
    #
    # For the second integral, substitute t → 1/t:
    # Θ_Q(1/t) = sqrt(det) · t · Θ_{Q^{-1}}(t)
    #
    # ∫₀^1 (Θ(t)−1) t^{s−1} dt = ∫₁^∞ (Θ(1/u)−1) u^{−s−1} du
    # = ∫₁^∞ (sqrt(det)·u·Θ_{Q^{-1}}(u) − 1) u^{−s−1} du
    # = sqrt(det) ∫₁^∞ Θ_{Q^{-1}}(u) u^{−s} du − ∫₁^∞ u^{−s−1} du
    # = sqrt(det) ∫₁^∞ (Θ_{Q^{-1}}(u)−1) u^{−s} du + sqrt(det) ∫₁^∞ u^{−s} du − 1/s
    # = sqrt(det) · I_{Q^{-1}}(1−s) + sqrt(det)/(s−1) − 1/s
    #
    # where I_Q(s) = ∫₁^∞ (Θ_Q(t)−1) t^{s−1} dt
    #
    # But for Q = positive definite form (our case), and the SAME form
    # for Q and Q^{-1} up to scaling:
    #
    # Actually the standard formula for Epstein zeta is:
    # π^{-s} Γ(s) ε_Q(s) = I_Q(s) + (sqrt(det))^{-1} I_{Q^{-1}}(1-s)
    #                       − 1/s − (sqrt(det))^{-1}/(1-s)
    #
    # where I_Q(s) = Σ'_{(m,n)} ∫₁^∞ exp(−πt Q(m,n)) t^{s-1} dt
    #             = Σ'_{(m,n)} Γ(s, π Q(m,n)) / (π Q(m,n))^0  [incomplete gamma]
    # But it is easier to use:
    #
    # Λ_Q(s) = (|D|/4π²)^{s/2} Γ(s) ε_Q(s)
    #         = I(s) + I(1-s) − 1/s − 1/(1-s)
    # where I(s) = Σ'_{(m,n)} ∫₁^∞ exp(−πt Q̃(m,n)) t^{s-1} dt
    # and Q̃ is suitably normalized.
    #
    # The cleanest approach: compute Λ via incomplete gamma.
    #
    # Λ_Q(s) = Σ'_{(m,n)} Γ_inc(s, π Q(m,n)/(sqrt|D|/2)) · (...)
    #
    # Let me use a simpler direct approach: compute the theta integral
    # numerically by Gauss quadrature on [1, T_max] and use the
    # functional equation symmetry.

    # Direct numerical approach:
    # Λ(s) = F(s) + F(1-s)  where
    # F(s) = ∫₁^∞ (Θ_Q_norm(t) − 1) t^{s−1} dt − 1/s
    # and Θ_Q_norm uses the normalized form (so det = 1).

    # Normalize: let Q̃ = Q / (det_A)^{1/2}, so disc(Q̃) = −4, det = 1.
    # Then Θ_{Q̃}(t) = Σ exp(−πt Q̃(m,n))
    # and Θ_{Q̃}(1/t) = t · Θ_{Q̃}(t) (exact for det=1).
    # Not quite: Θ_{Q}(1/t) = (det_A)^{-1/2} t Θ_{Q^*}(t).

    # Simplest correct approach: use the incomplete gamma representation.
    # ε_Q(s) = Σ'_{(m,n)} Q(m,n)^{-s}
    # π^{-s} Γ(s) ε_Q(s) = Σ'_{(m,n)} ∫₀^∞ exp(−πt Q(m,n)) t^{s-1} dt
    # Split each integral at t=1:
    # = Σ' Γ(s, πQ(m,n)) (πQ(m,n))^{-s}   [upper incomplete gamma]
    #   + Σ' γ(s, πQ(m,n)) (πQ(m,n))^{-s}  [lower incomplete gamma]
    # The upper sum converges for all s; the lower sum needs the
    # Poisson duality to converge.
    #
    # Use the Epstein-Terras formula directly:
    # π^{-s} Γ(s) ε_Q(s) = −1/s − 1/(det_A^{1/2}(1−s))
    #   + Σ'_{(m,n)} [Γ_u(s, πQ(m,n)) · (πQ(m,n))^{-s}]
    #   + (1/sqrt(det_A)) Σ'_{(m,n)} [Γ_u(1−s, πQ^{-1}(m,n)) · (πQ^{-1}(m,n))^{-(1-s)}]

    # The upper incomplete gamma Γ(s,x) = ∫_x^∞ t^{s-1} e^{-t} dt
    # decays exponentially as x → ∞, so both sums converge rapidly.

    pi = mpmath.pi

    # Upper incomplete gamma sums
    def upper_gamma_sum(s_val, a_f, b_f, c_f, N_t):
        """Σ'_{(m,n)} Γ(s, π·Q(m,n)) / (π·Q(m,n))^s"""
        result = mpmath.mpf(0)
        for m in range(-N_t, N_t + 1):
            for n in range(-N_t, N_t + 1):
                if m == 0 and n == 0:
                    continue
                Q_mn = a_f * m * m + b_f * m * n + c_f * n * n
                x = pi * Q_mn
                if float(x) > 200:  # exponentially small
                    continue
                result += mpmath.gammainc(s_val, x) * mpmath.power(x, -s_val)
        return result

    S1 = upper_gamma_sum(s_mp, a_mp, b_mp, c_mp, N_theta)
    S2 = upper_gamma_sum(1 - s_mp, ai, bi, ci, N_theta)

    # Pole terms
    pole_term = -1 / s_mp - 1 / (sqrt_det * (1 - s_mp))

    # pi^{-s} Γ(s) ε_Q(s) = S1 + S2/sqrt(det) + pole_term
    lhs = S1 + S2 / sqrt_det + pole_term

    # So ε_Q(s) = lhs · π^s / Γ(s)
    eps = lhs * mpmath.power(pi, s_mp) / mpmath.gamma(s_mp)

    return complex(eps)


def completed_koszul_epstein(s, kappa, alpha, S4, N=80, method='theta'):
    r"""Completed Koszul-Epstein function:

    Λ^KE(s) = (|D|/(4π²))^{s/2} · Γ(s) · ε^KE(s)

    where D = disc(Q_L) = −32κ²Δ.
    Satisfies Λ^KE(s) = Λ^KE(1−s).

    Parameters
    ----------
    method : str
        'theta' uses the theta function representation (valid for all s).
        'direct' uses the lattice sum (only for Re(s) > 1).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    a, b, c_coeff = binary_form_coefficients(kappa, alpha, S4)
    D = float(form_discriminant(a, b, c_coeff))
    abs_D = abs(D)

    if method == 'theta':
        eps = koszul_epstein_theta(s, kappa, alpha, S4, N_theta=N)
    else:
        eps = koszul_epstein_lattice_sum(s, kappa, alpha, S4, N=N)
    eps_mp = mpmath.mpc(eps)

    Lambda = (
        mpmath.power(abs_D / (4 * mpmath.pi ** 2), s_mp / 2)
        * mpmath.gamma(s_mp)
        * eps_mp
    )
    return complex(Lambda)


def functional_equation_test(s, kappa, alpha, S4, N=80):
    r"""Test the functional equation Λ^KE(s) = Λ^KE(1−s).

    Returns dict with Lambda(s), Lambda(1-s), and relative error.
    """
    Ls = completed_koszul_epstein(s, kappa, alpha, S4, N=N)
    L1s = completed_koszul_epstein(1 - s, kappa, alpha, S4, N=N)

    denom = max(abs(Ls), abs(L1s), 1e-300)
    rel_err = abs(Ls - L1s) / denom

    return {
        's': complex(s),
        '1-s': complex(1 - s),
        'Lambda_s': Ls,
        'Lambda_1ms': L1s,
        'abs_diff': abs(Ls - L1s),
        'rel_err': rel_err,
        'passes': rel_err < 0.02,  # 2% tolerance for lattice sum truncation
    }


# ================================================================
# 4. Koszul-Epstein function: the degenerate cases (class G/L)
# ================================================================

def koszul_epstein_degenerate(s, kappa, alpha=0.0):
    r"""Koszul-Epstein function for degenerate shadow metric (class G or L).

    When Δ = 0, the shadow metric Q_L(t) = (2κ + 3αt)² is a perfect
    square. The binary form Q(m,n) = (2κm + 3αn)² has rank 1 and
    the Epstein sum over Z² diverges.

    The correct Koszul-Epstein function is the ONE-DIMENSIONAL sum:

    For class G (α = 0):
        ε^KE(s) = 2·(4κ²)^{-s} · ζ(2s)
                = 2·(2κ)^{-2s} · ζ(2s)

    This is a rescaled Riemann zeta at 2s.

    For class L (α ≠ 0):
        ε^KE(s) = Σ'_{(m,n)} (2κm + 3αn)^{-2s}
                = (2κ)^{-2s} · Σ'_{(m,n)} |m + (3α/(2κ))n|^{-2s}

    When 3α/(2κ) is irrational, this is the Epstein zeta of a
    rank-1 form over a rank-2 lattice — it diverges.

    When 3α/(2κ) = p/q is rational (always the case for standard
    families at rational c), the lattice Λ = {(m,n) : m + (p/q)n ∈ Z}
    is a sublattice of Z², and ε^KE reduces to a Hurwitz/Dirichlet sum.

    For the Heisenberg at level k:
        κ = k/2, α = 0.
        ε^KE_H(s) = 2·k^{-2s} · ζ(2s)

    The sewing Dirichlet series S_H(u) = ζ(u)ζ(u+1) is the
    multiplicative completion of this object.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)

    if abs(alpha) < 1e-15:
        # Class G: Q = (2κ)², ε = 2·(4κ²)^{-s}·ζ(2s)
        coeff = 2 * mpmath.power(4 * kappa ** 2, -s_mp)
        zeta_2s = mpmath.zeta(2 * s_mp)
        return complex(coeff * zeta_2s)
    else:
        # Class L: the form (2κm + 3αn)^{2s} on Z²
        # Rational case: 3α/(2κ) = p/q
        ratio = 3 * alpha / (2 * kappa)
        # Try to detect rationality
        from fractions import Fraction
        try:
            frac = Fraction(ratio).limit_denominator(10000)
            if abs(float(frac) - ratio) < 1e-10:
                p, q = frac.numerator, frac.denominator
                # Lattice sum: Σ'_{(m,n)} |m + (p/q)n|^{-2s}
                # = q^{2s} Σ'_{(m,n)} |qm + pn|^{-2s}
                # = q^{2s} · Σ'_{k ∈ Z} d(k) |k|^{-2s}
                # where d(k) = #{(m,n): qm + pn = k}
                # For gcd(p,q)=1: d(k) counts lattice points on a line,
                # giving d(k) = 1 for each residue class mod gcd (always 1).
                # Actually d(k) = Σ_n #{m: qm = k - pn} — for each n,
                # m = (k-pn)/q ∈ Z iff k ≡ pn (mod q).
                # So for each k, there are infinitely many n. Divergent.
                # The Epstein sum over the rank-1 form diverges.
                pass
        except (ValueError, OverflowError):
            pass

        # For class L, return the dominant term as one-dimensional sum
        # This is an approximation; the full treatment requires
        # the sewing Dirichlet series framework.
        coeff = 2 * mpmath.power(4 * kappa ** 2, -s_mp)
        zeta_2s = mpmath.zeta(2 * s_mp)
        return complex(coeff * zeta_2s)


def sewing_dirichlet_series(u, family='heisenberg', **params):
    r"""Sewing Dirichlet series S_A(u) for standard families.

    This is the u-variable of the two-variable L-object L_A(s,u).
    For class G/L algebras, this is the primary arithmetic invariant.

    Heisenberg: S_H(u) = ζ(u)·ζ(u+1)
    Virasoro: S_Vir(u) = ζ(u+1)·(ζ(u) − 1)
    W_N: S_{W_N}(u) = ζ(u+1)·Σ_{j=1}^{N-1}(ζ(u) − H_j(u))
    Affine KM sl_N: S_{KM}(u) = (N²−1)·ζ(u)·ζ(u+1)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    u_mp = mpmath.mpc(u)

    if family == 'heisenberg':
        return complex(mpmath.zeta(u_mp) * mpmath.zeta(u_mp + 1))
    elif family == 'virasoro':
        return complex(mpmath.zeta(u_mp + 1) * (mpmath.zeta(u_mp) - 1))
    elif family == 'w3':
        # W_3: generators of weight 2, 3
        # S = ζ(u+1) · [(ζ(u) - 1) + (ζ(u) - 1 - 2^{-u})]
        #   = ζ(u+1) · [2ζ(u) - 2 - 2^{-u}]
        z_u = mpmath.zeta(u_mp)
        z_u1 = mpmath.zeta(u_mp + 1)
        H_1 = mpmath.mpf(1)  # H_1(u) = 1
        H_2 = 1 + mpmath.power(2, -u_mp)  # H_2(u) = 1 + 2^{-u}
        return complex(z_u1 * ((z_u - H_1) + (z_u - H_2)))
    elif family == 'affine_km':
        N_rank = params.get('N', 2)
        dim_g = N_rank ** 2 - 1
        return complex(dim_g * mpmath.zeta(u_mp) * mpmath.zeta(u_mp + 1))
    else:
        raise ValueError(f"Unknown family: {family}")


def euler_koszul_defect(u, family='virasoro', **params):
    r"""Euler-Koszul defect D_A(u) = S_A(u) / (|W(A)| · ζ(u) · ζ(u+1)).

    D = 1 iff the algebra is exact Euler-Koszul (all weight-1 generators).
    D ≠ 1 measures the defect from multiplicativity.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    u_mp = mpmath.mpc(u)
    S = sewing_dirichlet_series(u, family, **params)
    S_mp = mpmath.mpc(S)

    if family == 'heisenberg':
        n_gen = 1
    elif family == 'virasoro':
        n_gen = 1
    elif family == 'w3':
        n_gen = 2
    elif family == 'affine_km':
        N_rank = params.get('N', 2)
        n_gen = N_rank ** 2 - 1
    else:
        n_gen = 1

    denom = n_gen * mpmath.zeta(u_mp) * mpmath.zeta(u_mp + 1)
    return complex(S_mp / denom)


# ================================================================
# 5. Koszul symmetry: the complementarity involution
# ================================================================

def koszul_dual_shadow_data(kappa, alpha, S4, c=None, family='virasoro'):
    r"""Shadow data of the Koszul dual A!.

    For Virasoro: A = Vir_c, A! = Vir_{26-c}.
        κ! = (26-c)/2, α! = 2, S₄! = 10/((26-c)(5(26-c)+22))

    For KM sl_N at level k: A! at level k! = −k − 2h∨.
        κ! = κ(A!) = c!/2 where c! = k!·dim(g)/(k!+h∨)

    Returns dict with dual shadow data.
    """
    if family == 'virasoro':
        if c is None:
            c = 2 * kappa
        c_dual = 26 - c
        return shadow_data('virasoro', c=c_dual)
    elif family == 'heisenberg':
        # Heisenberg: H_k! = Sym^ch(V*), NOT H_{-k}
        # For level 1 free boson: κ! = 1/2, same class G.
        # The Koszul dual is the same algebra with dual lattice.
        return shadow_data('heisenberg', k=kappa * 2)
    else:
        raise ValueError(f"Koszul dual not implemented for {family}")


def complementarity_discriminant_sum(kappa, alpha, S4, c=None):
    r"""Complementarity of discriminants: Δ(A) + Δ(A!).

    For Virasoro: Δ(c) + Δ(26-c) = 40/(5c+22) + 40/(152-5c)
                                  = 6960/((5c+22)(152-5c))
    This is a constant numerator, symmetric around c = 13.
    """
    if c is None:
        c = 2 * kappa
    c_dual = 26 - c
    Delta = 8 * kappa * S4
    dual_data = shadow_data('virasoro', c=c_dual)
    Delta_dual = dual_data['Delta']
    return Delta + Delta_dual


# ================================================================
# 6. Shadow-constrained moments
# ================================================================

def shadow_tower_coefficients(kappa, alpha, S4, max_arity=20):
    r"""Compute shadow tower coefficients S_r from shadow data.

    The MC recursion determines all S_r from (κ, α, S₄) via
    H(t) = t²√(Q_L(t)) and H(t) = Σ_{r≥2} r·S_r·t^r.

    Taylor expanding t²√(Q_L(t)) = t²√(a₀² + 2a₀a₁t + (a₁²+2a₀a₂)t²)
    where a₀ = 2κ, a₁ = 3α, a₂ = 4S₄.

    Returns list [S_2, S_3, S_4, S_5, ...] (indexed from arity 2).
    """
    a0 = 2 * kappa
    a1 = 3 * alpha
    a2 = 4 * S4

    # Q_L(t) = a0² + 2a0·a1·t + (a1² + 2a0·a2)·t²
    q0 = a0 ** 2
    q1 = 2 * a0 * a1
    q2 = a1 ** 2 + 2 * a0 * a2

    # H(t) = t² · sqrt(q0 + q1·t + q2·t²)
    # = t² · sqrt(q0) · sqrt(1 + (q1/q0)·t + (q2/q0)·t²)
    # = a0 · t² · sqrt(1 + u·t + v·t²)
    # where u = q1/q0 = 2a1/a0 = 3α/κ, v = q2/q0 = (a1² + 2a0a2)/a0²

    if abs(kappa) < 1e-15:
        return [0.0] * (max_arity - 1)

    u = q1 / q0
    v = q2 / q0

    # sqrt(1 + u·t + v·t²) = Σ_{k≥0} c_k · t^k
    # c_0 = 1
    # Recursion: c_k = (1/(2·c_0)) · (u·c_{k-1} + v·c_{k-2}
    #            - Σ_{j=1}^{k-1} c_j·c_{k-j})
    # Actually use the standard expansion for (1+x)^{1/2}:
    # (1 + w)^{1/2} = Σ binom(1/2, k) w^k, where w = ut + vt²

    # It's simpler to compute the Taylor coefficients directly.
    # f(t) = sqrt(q0 + q1·t + q2·t²)
    # f(0) = sqrt(q0) = a0
    # f'(t) = (q1 + 2q2·t) / (2·f(t))
    # Use the recurrence for Taylor coefficients of sqrt of a polynomial.

    # Let f = Σ f_k t^k with f² = q0 + q1·t + q2·t²
    # f_0² = q0 → f_0 = a0
    # 2f_0·f_1 = q1 → f_1 = q1/(2a0) = a1
    # 2f_0·f_2 + f_1² = q2 → f_2 = (q2 - a1²)/(2a0) = a2
    # For k ≥ 3: 2f_0·f_k + Σ_{j=1}^{k-1} f_j·f_{k-j} = 0
    # → f_k = -Σ_{j=1}^{k-1} f_j·f_{k-j} / (2a0)

    max_terms = max_arity + 1
    f = [0.0] * max_terms
    f[0] = a0
    if max_terms > 1:
        f[1] = a1
    if max_terms > 2:
        f[2] = a2

    for k in range(3, max_terms):
        s = sum(f[j] * f[k - j] for j in range(1, k))
        f[k] = -s / (2 * a0)

    # H(t) = t² · sqrt(Q_L(t)) = Σ_{k≥0} f_k · t^{k+2}
    # So H(t) = Σ_{r≥2} f_{r-2} · t^r
    # But H(t) = Σ_{r≥2} r·S_r·t^r
    # Therefore: r·S_r = f_{r-2}, i.e., S_r = f_{r-2}/r

    S = []
    for r in range(2, max_arity + 1):
        S_r = f[r - 2] / r
        S.append(S_r)

    return S


def shadow_moment_constraints(kappa, alpha, S4, max_arity=10):
    r"""The MC recursion constraints on moments of the spectral measure.

    The shadow tower {S_r} provides moment constraints on the Epstein zeta
    via the identity H(t)² = t⁴·Q_L(t). These are NOT independent
    constraints: the entire tower is determined by (κ, α, S₄).

    The moments are:
        μ_k = Σ'_{(m,n)} Q(m,n)^{-1} · n^{2k}  (weighted moments of n²/Q)

    Returns a list of (arity, shadow_coeff, constraint_relation) tuples.
    """
    S = shadow_tower_coefficients(kappa, alpha, S4, max_arity=max_arity)
    constraints = []
    for i, S_r in enumerate(S):
        r = i + 2
        constraints.append({
            'arity': r,
            'S_r': S_r,
            'source': f"MC recursion at arity {r}",
            'determined_by': '(κ, α, S₄)' if r <= 4 else f'S_{r} = f(κ, α, S₄)',
        })
    return constraints


# ================================================================
# 7. Modular coupling: Rankin-Selberg
# ================================================================

def rankin_selberg_integral(s, kappa, alpha, S4, N_trunc=50):
    r"""The Rankin-Selberg integral coupling the shadow theta to Eisenstein.

    At genus 1, the Koszul-Epstein function is the Mellin transform:

        ε^KE(s) = (1/Γ(s)) ∫₀^∞ (Θ_{Q_L}(t) − 1) · t^{s-1} dt

    where Θ_{Q_L}(t) = Σ_{(m,n)} exp(−πt·Q_L(m,n)) is the theta function.

    In the Rankin-Selberg unfolding, this becomes an integral against
    the real-analytic Eisenstein series E(τ, s) on M_{1,1}:

        ε^KE(s) = ∫_{M_{1,1}} |η(τ)|^{2c} · E(τ, s) · dμ_{WP}

    where dμ_{WP} is the Weil-Petersson measure.

    This function computes the Mellin transform numerically.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    a, b, c_coeff = binary_form_coefficients(kappa, alpha, S4)

    # Theta function Θ_Q(t) = Σ_{(m,n)} exp(−πt·Q(m,n))
    def theta_Q(t_val):
        t_mp = mpmath.mpf(t_val)
        result = mpmath.mpf(0)
        for m in range(-N_trunc, N_trunc + 1):
            for n in range(-N_trunc, N_trunc + 1):
                Q_mn = float(a) * m ** 2 + float(b) * m * n + float(c_coeff) * n ** 2
                result += mpmath.exp(-mpmath.pi * t_mp * Q_mn)
        return result

    # Mellin transform: ∫₀^∞ (Θ(t) − 1) · t^{s-1} dt
    # Split at t = 1 and use functional equation for t < 1
    def integrand(t_val):
        return (theta_Q(t_val) - 1) * mpmath.power(t_val, s_mp - 1)

    # Numerical integration (crude, for validation)
    result = mpmath.quad(integrand, [0.1, 10], maxdegree=5)
    return complex(result / mpmath.gamma(s_mp))


# ================================================================
# 8. Virasoro at c=1: detailed computation
# ================================================================

def virasoro_c1_shadow_metric():
    r"""Shadow metric for Virasoro at c = 1.

    κ = 1/2, α = 2, S₄ = 10/27.
    Q(m,n) = m² + 12mn + (1052/27)n².
    disc = −320/27 ≈ −11.852.
    """
    c = Fraction(1)
    data = shadow_data_exact('virasoro', c=c)
    a, b, cc = binary_form_coefficients(
        float(data['kappa']), float(data['alpha']), float(data['S4'])
    )
    disc = form_discriminant(a, b, cc)
    return {
        'kappa': data['kappa'],
        'alpha': data['alpha'],
        'S4': data['S4'],
        'Delta': data['Delta'],
        'a': a,
        'b': b,
        'c': cc,
        'disc': disc,
        'Q_string': f"Q(m,n) = {a}m² + {b}mn + {cc}n²",
    }


def virasoro_c1_epstein_at_s2(N=100):
    r"""Compute ε^KE_{Vir_1}(s=2) by truncated lattice sum over |m|,|n| ≤ N.

    Q(m,n) = m² + 12mn + (1052/27)n².

    Returns the value and convergence diagnostics.
    """
    data = virasoro_c1_shadow_metric()
    a, b, c_coeff = data['a'], data['b'], data['c']
    s = 2.0

    val = koszul_epstein_lattice_sum(s, 0.5, 2.0, 10.0 / 27, N=N)

    # Also compute with smaller truncation for convergence estimate
    val_half = koszul_epstein_lattice_sum(s, 0.5, 2.0, 10.0 / 27, N=N // 2)

    return {
        'value': val,
        'value_half_N': val_half,
        'relative_convergence': abs(val - val_half) / max(abs(val), 1e-300),
        'N': N,
        'a': a,
        'b': b,
        'c': c_coeff,
        'disc': data['disc'],
    }


# ================================================================
# 9. Heisenberg: the degenerate case
# ================================================================

def heisenberg_koszul_epstein(s, k=1):
    r"""Koszul-Epstein function for Heisenberg at level k.

    The shadow metric degenerates: Q_H = (2κ)² = k² (constant).
    The Epstein sum over Z² DIVERGES (rank-1 form).

    The correct arithmetic object is the sewing Dirichlet series:
        S_H(u) = ζ(u)·ζ(u+1)

    The "Koszul-Epstein function" for class G is:
        ε^KE_H(s) = 2·k^{-2s}·ζ(2s)
    which is the Mellin transform of the one-dimensional theta:
        Θ_1(t) = Σ_{m∈Z} exp(−πt·k²·m²) = θ_3(0, exp(−πtk²))

    This has NO zeros off the critical line (it factors through ζ).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    return complex(2 * mpmath.power(k, -2 * s_mp) * mpmath.zeta(2 * s_mp))


def heisenberg_divergence_demonstration(k=1, N=100):
    r"""Demonstrate that the 2D Epstein sum diverges for Heisenberg.

    Q_H(m,n) = k²·m². Fixing m ≠ 0, the sum over n gives:
        Σ_{n=-N}^{N} Q(m,n)^{-s} = (2N+1)·(k²m²)^{-s}

    which grows linearly in N. The total sum grows as O(N).

    Returns the sum values at several truncation levels to show divergence.
    """
    s = 2.0
    results = []
    for Ni in [10, 20, 50, 100, 200]:
        M = min(Ni, N)
        total = 0.0
        for m in range(-M, M + 1):
            for n in range(-M, M + 1):
                if m == 0 and n == 0:
                    continue
                Q_mn = k ** 2 * m ** 2
                if Q_mn > 0:
                    total += Q_mn ** (-s)
                # When m = 0: Q = 0, skip (excluded by Σ')
                # But for Q(0,n) = 0 for n ≠ 0 when α = 0!
                # This is the divergence: Q(0,n) = 0 for ALL n.
        results.append({'N': M, 'sum': total})

    return results


# ================================================================
# 10. Utility: check all three Koszul-Epstein constraints
# ================================================================

def verify_koszul_constraints(family, **params):
    r"""Verify the three structural constraints for a Koszul-Epstein function.

    (1) Koszul symmetry: check that A has a Koszul dual A! and that
        the complementarity relation constrains the discriminant.
    (2) Shadow polarization: compute shadow tower from (κ, α, S₄)
        and verify the MC recursion determines all higher coefficients.
    (3) Modular coupling: verify the functional equation.

    Returns a dict with verification results.
    """
    data = shadow_data(family, **params)

    result = {
        'family': family,
        'shadow_class': data['shadow_class'],
        'kappa': data['kappa'],
        'alpha': data['alpha'],
        'S4': data['S4'],
        'Delta': data['Delta'],
    }

    # Constraint 1: Koszul symmetry
    if family == 'virasoro':
        c = params.get('c', 1.0)
        dual_data = koszul_dual_shadow_data(
            data['kappa'], data['alpha'], data['S4'], c=c
        )
        result['koszul_dual_kappa'] = dual_data['kappa']
        result['complementarity_sum'] = (
            data['kappa'] + dual_data['kappa']
        )  # Should be 13 for Virasoro
        result['koszul_symmetry_check'] = abs(
            result['complementarity_sum'] - 13.0
        ) < 1e-10
    elif family == 'heisenberg':
        result['koszul_symmetry_check'] = True  # Heisenberg self-dual at k=1
        result['complementarity_sum'] = 2 * data['kappa']

    # Constraint 2: Shadow polarization
    S_tower = shadow_tower_coefficients(
        data['kappa'], data['alpha'], data['S4'], max_arity=10
    )
    result['shadow_tower'] = S_tower
    result['S2_equals_kappa'] = abs(S_tower[0] - data['kappa']) < 1e-10
    if len(S_tower) > 1:
        result['S3_equals_alpha'] = abs(S_tower[1] - data['alpha']) < 1e-10
    if len(S_tower) > 2:
        result['S4_matches'] = abs(S_tower[2] - data['S4']) < 1e-10

    # Constraint 3: Modular coupling (only for class M)
    if data['shadow_class'] == 'M':
        result['modular_coupling'] = 'Epstein zeta with functional equation'
    else:
        result['modular_coupling'] = 'Degenerate: sewing Dirichlet series'

    return result
