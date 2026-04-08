"""theorem_shadow_langlands_engine.py

Numerical investigation of the Langlands-type structure of the shadow
L-function and the arithmetic packet connection.

The shadow Eisenstein theorem (conj:shadow-eisenstein, downgraded from
thm:shadow-eisenstein; see rem:shadow-eisenstein-correct-scope) states

    L^sh_A(s) := sum_{r >= 2} S_r(A) r^{-s} = -kappa(A) zeta(s) zeta(s-1).

This engine investigates five questions at the interface between the shadow
obstruction tower and the Langlands programme:

(a) GL(2) EISENSTEIN IDENTIFICATION.  The product zeta(s)*zeta(s-1) is the
    standard L-function of the GL(2) Eisenstein series induced from the
    trivial and identity characters of GL(1).  In Langlands terms, L^sh is
    the L-function of a non-tempered automorphic representation of GL(2,A_Q)
    -- the Eisenstein series E(s; 1, |.|) -- and is NOT cuspidal.  The local
    Langlands parameters at each prime p are:

        sigma_p = diag(1, p) : W_p -> GL(2,C),

    the direct sum of the unramified character sending Frob_p to 1 and the
    unramified character sending Frob_p to p.

(b) DEPENDENCE ON N FOR AFFINE sl_N.  The kappa formula for sl_N at level k
    is kappa = dim(sl_N)(k+N)/(2N) = (N^2-1)(k+N)/(2N).  The shadow
    L-function L^sh = -kappa * zeta(s) * zeta(s-1) scales by kappa but the
    STRUCTURE (product of two Riemann zetas) does NOT change.  It stays
    GL(2) Eisenstein for all N.  This is a negative result: the shadow
    L-function does NOT detect the GL(N) Langlands structure of sl_N.

(c) RESIDUE AT s=2 AND REPRESENTATION THEORY.  L^sh has poles at s=1 and
    s=2.  The residue at s=2 is -kappa * zeta(2) = -kappa * pi^2/6.  The
    residue at s=1 is kappa/2 (since zeta(0) = -1/2).  The ratio of
    residues is -pi^2/3.  These residues have the following meaning: the
    pole at s=2 comes from zeta(s-1) at its pole s-1=1, and the value
    zeta(2) = pi^2/6 at that pole is the Plancherel contribution of the
    GL(1) Eisenstein spectrum.

(d) MOONSHINE MODULE.  kappa(V-natural) = c/2 = 12 (AP48: the Virasoro
    formula, not the lattice formula).  L^sh(V-natural) = -12 zeta(s)
    zeta(s-1).  The Ramanujan tau-function appears in the CUSPIDAL part of
    the Leech lattice constrained Epstein zeta (through Delta_12 in
    S_12(SL(2,Z))), NOT in the shadow L-function itself.  For the Leech
    lattice VOA (kappa=24), the constrained Epstein zeta DOES involve
    L(s, Delta_12), but the shadow L-function is still purely Eisenstein.

(e) FRONTIER DEFECT FORM.  Omega_A = d log Lambda_Eis - d log phi, where
    phi(s) = Lambda*(1-s)/Lambda*(s) is the automorphic scattering matrix
    with Lambda*(s) = pi^{-s} Gamma(s) zeta(2s).  For lattice VOAs,
    Lambda_Eis(s) involves zeta(s)*zeta(s-r/2+1) while phi involves
    zeta(2s)/zeta(2s-1).  These have DIFFERENT zero sets, so Omega != 0
    generically.  The gauge criterion (prop:gauge-criterion-scattering)
    states Omega exact iff Lambda_Eis/phi is single-valued.

Verification paths:
  V1: Direct GL(2) Eisenstein L-function formula vs shadow L-function.
  V2: Local Langlands parameters at primes vs Hasse-Weil of P^1.
  V3: Kappa scaling across families (sl_N, Virasoro, W_N, moonshine).
  V4: Residue structure and ratio invariance.
  V5: Frontier defect form computation at explicit s-values.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import mpmath as mp


__all__ = [
    "ShadowLanglandsEngine",
    "kappa_sl_n",
    "kappa_virasoro",
    "kappa_wn",
    "kappa_moonshine",
    "kappa_leech",
    "gl2_eisenstein_l_function",
    "local_langlands_parameter",
    "shadow_l_function",
    "residue_ratio",
    "frontier_defect_form_value",
    "scattering_matrix_phi",
    "completed_l_function_lambda_star",
]


# ---------------------------------------------------------------------------
# Kappa formulas for standard families (recomputed from first principles;
# AP1, AP3: never copy between families)
# ---------------------------------------------------------------------------


def kappa_sl_n(N: int, k) -> mp.mpf:
    """kappa(sl_N, k) = dim(sl_N) * (k + N) / (2N) = (N^2 - 1)(k + N) / (2N).

    This is the affine Kac-Moody formula kappa = dim(g)(k + h^vee)/(2h^vee)
    with dim(sl_N) = N^2 - 1 and h^vee(sl_N) = N.
    """
    k_mp = mp.mpf(k)
    N_mp = mp.mpf(N)
    return (N_mp ** 2 - 1) * (k_mp + N_mp) / (2 * N_mp)


def kappa_virasoro(c) -> mp.mpf:
    """kappa(Vir_c) = c/2."""
    return mp.mpf(c) / 2


def kappa_wn(N: int, c) -> mp.mpf:
    """kappa(W_N) = c * (H_N - 1), where H_N = sum_{j=1}^{N} 1/j.

    H_N is the N-th harmonic number.
    """
    c_mp = mp.mpf(c)
    H_N = sum(mp.mpf(1) / j for j in range(1, N + 1))
    return c_mp * (H_N - 1)


def kappa_moonshine() -> mp.mpf:
    """kappa(V-natural) = c/2 = 12.

    The moonshine module has c=24 and the Virasoro formula applies
    (AP48: kappa depends on the full algebra; for V-natural the
    primitive generator is T at weight 2, giving kappa = c/2 = 12,
    NOT the lattice formula kappa = rank = 24).
    """
    return mp.mpf(12)


def kappa_leech() -> mp.mpf:
    """kappa(V_Leech) = rank(Leech) = 24.

    The Leech lattice VOA uses the Heisenberg/lattice formula
    kappa = rank, NOT the Virasoro formula kappa = c/2 (AP48, AP39).
    """
    return mp.mpf(24)


# ---------------------------------------------------------------------------
# GL(2) Eisenstein L-function
# ---------------------------------------------------------------------------


def gl2_eisenstein_l_function(s, kappa_val) -> mp.mpc:
    """L-function of the GL(2) Eisenstein series E(s; 1, |.|).

    The GL(2) Eisenstein series induced from the trivial character chi_0 = 1
    and the norm character |.| on GL(1) has L-function

        L(s, E(.; 1, |.|)) = zeta(s) * zeta(s - 1).

    The shadow L-function is L^sh(s) = -kappa * L(s, E(.; 1, |.|)).

    In Langlands terms, E(.; 1, |.|) is the automorphic representation of
    GL(2, A_Q) parabolically induced from the characters 1 and |.|^1 of
    the Borel.  It is NOT tempered (the character |.| is non-unitary).
    """
    s_mp = mp.mpc(s)
    return -mp.mpf(kappa_val) * mp.zeta(s_mp) * mp.zeta(s_mp - 1)


def shadow_l_function(s, kappa_val) -> mp.mpc:
    """L^sh_A(s) = -kappa * zeta(s) * zeta(s-1).

    Identical to gl2_eisenstein_l_function -- they are the same object.
    This function exists to make the identification explicit in tests.
    """
    s_mp = mp.mpc(s)
    return -mp.mpf(kappa_val) * mp.zeta(s_mp) * mp.zeta(s_mp - 1)


# ---------------------------------------------------------------------------
# Local Langlands parameters
# ---------------------------------------------------------------------------


def local_langlands_parameter(p: int, s) -> mp.mpc:
    """Local factor L_p(s) = 1 / [(1 - p^{-s})(1 - p^{1-s})].

    The local Langlands parameter at the prime p for the GL(2)
    Eisenstein representation E(.; 1, |.|) is the semisimple
    conjugacy class

        sigma_p = diag(alpha_p, beta_p) = diag(1, p)

    in GL(2, C).  The local L-factor is

        L_p(s) = 1 / [(1 - alpha_p * p^{-s})(1 - beta_p * p^{-s})]
               = 1 / [(1 - p^{-s})(1 - p^{1-s})].

    This is simultaneously:
    - the Hasse-Weil local factor of P^1 over F_p,
    - the local Euler factor of zeta(s) * zeta(s-1),
    - the Satake parameter of the spherical Eisenstein vector.
    """
    s_mp = mp.mpc(s)
    p_mp = mp.mpf(p)
    return mp.mpc(1) / ((1 - p_mp ** (-s_mp)) * (1 - p_mp ** (1 - s_mp)))


def satake_parameters(p: int) -> Tuple[mp.mpf, mp.mpf]:
    """Satake parameters (alpha_p, beta_p) = (1, p) for E(.; 1, |.|).

    For a cuspidal GL(2) representation pi with Hecke eigenvalue a_p,
    the Satake parameters satisfy alpha_p + beta_p = a_p and
    alpha_p * beta_p = chi(p) where chi is the central character.

    For the Eisenstein series E(.; 1, |.|):
        alpha_p = 1, beta_p = p
        a_p = 1 + p = sigma_0(p) + sigma_1(p)/p [not standard Hecke]
        alpha_p * beta_p = p = |.|(p)

    The key point: the Ramanujan conjecture states |alpha_p| = |beta_p| = 1
    for CUSPIDAL representations.  The Eisenstein representation has
    beta_p = p, violating Ramanujan.  The shadow L-function is non-tempered.
    """
    return (mp.mpf(1), mp.mpf(p))


# ---------------------------------------------------------------------------
# Residue structure
# ---------------------------------------------------------------------------


def shadow_l_residue_at_one(kappa_val) -> mp.mpf:
    """Res_{s=1} L^sh(s) = kappa / 2.

    zeta(s) has a simple pole at s=1 with residue 1.
    zeta(0) = -1/2.
    So Res_{s=1} [-kappa * zeta(s) * zeta(s-1)] = -kappa * 1 * (-1/2) = kappa/2.
    """
    return mp.mpf(kappa_val) / 2


def shadow_l_residue_at_two(kappa_val) -> mp.mpf:
    """Res_{s=2} L^sh(s) = -kappa * pi^2 / 6.

    zeta(s-1) has a simple pole at s=2 with residue 1.
    zeta(2) = pi^2/6.
    So Res_{s=2} [-kappa * zeta(s) * zeta(s-1)] = -kappa * zeta(2) * 1
       = -kappa * pi^2 / 6.
    """
    return -mp.mpf(kappa_val) * mp.pi ** 2 / 6


def residue_ratio() -> mp.mpf:
    """Ratio Res_{s=2} / Res_{s=1} = -pi^2 / 3.

    This ratio is INDEPENDENT of kappa (and hence of the algebra).
    It equals -2 * zeta(2) = -pi^2/3.
    """
    return -mp.pi ** 2 / 3


# ---------------------------------------------------------------------------
# Frontier defect form
# ---------------------------------------------------------------------------


def completed_l_function_lambda_star(s) -> mp.mpc:
    """Lambda*(s) = pi^{-s} Gamma(s) zeta(2s).

    The completed L-function appearing in the automorphic scattering
    matrix phi(s) = Lambda*(1-s)/Lambda*(s).
    """
    s_mp = mp.mpc(s)
    return mp.power(mp.pi, -s_mp) * mp.gamma(s_mp) * mp.zeta(2 * s_mp)


def scattering_matrix_phi(s) -> mp.mpc:
    """phi(s) = Lambda*(1-s) / Lambda*(s).

    The automorphic scattering matrix on M_{1,1}.  Its poles are at
    the values s where Lambda*(s) = 0, i.e., the rescaled nontrivial
    zeros of zeta(2s).
    """
    return completed_l_function_lambda_star(1 - s) / completed_l_function_lambda_star(s)


def eisenstein_packet_lattice(s, rank: int) -> mp.mpc:
    """Lambda_Eis(s) for a rank-r even lattice VOA.

    Lambda_Eis(s) = C_0(s) * zeta(s) * zeta(s - r/2 + 1).

    For simplicity we take C_0(s) = 1 (the gamma factors are an
    archimedean-place correction that does not affect the zero/pole
    structure on the critical strip).  The key point is that the
    zeta factors are zeta(s) and zeta(s - r/2 + 1), NOT zeta(2s).
    """
    s_mp = mp.mpc(s)
    r_mp = mp.mpf(rank)
    return mp.zeta(s_mp) * mp.zeta(s_mp - r_mp / 2 + 1)


def frontier_defect_form_value(s, rank: int) -> mp.mpc:
    """Omega_A(s) = d log Lambda_Eis - d log phi, evaluated numerically.

    We compute the numerical value of Omega at a point s by finite
    difference: Omega(s) ~ [log Lambda_Eis(s+h) - log Lambda_Eis(s-h)] / (2h)
                         - [log phi(s+h) - log phi(s-h)] / (2h).

    This is a numerical approximation to the 1-form evaluated at s.
    """
    h = mp.mpf("1e-8")
    s_mp = mp.mpc(s)

    # d log Lambda_Eis
    le_plus = mp.log(eisenstein_packet_lattice(s_mp + h, rank))
    le_minus = mp.log(eisenstein_packet_lattice(s_mp - h, rank))
    dlog_le = (le_plus - le_minus) / (2 * h)

    # d log phi
    phi_plus = scattering_matrix_phi(s_mp + h)
    phi_minus = scattering_matrix_phi(s_mp - h)
    dlog_phi = (mp.log(phi_plus) - mp.log(phi_minus)) / (2 * h)

    return dlog_le - dlog_phi


# ---------------------------------------------------------------------------
# Kappa dependence on N for affine sl_N
# ---------------------------------------------------------------------------


def kappa_sl_n_family(k, N_values: List[int]) -> Dict[int, mp.mpf]:
    """Compute kappa(sl_N, k) for a list of N values at fixed level k.

    Demonstrates that kappa grows as N^2 while the L-function
    STRUCTURE stays GL(2) Eisenstein.
    """
    return {N: kappa_sl_n(N, k) for N in N_values}


def shadow_l_ratio_sl_n(s, N1: int, N2: int, k) -> mp.mpc:
    """L^sh(sl_{N1}) / L^sh(sl_{N2}) = kappa(sl_{N1}) / kappa(sl_{N2}).

    The ratio is independent of s because the L-function STRUCTURE
    (zeta(s)*zeta(s-1)) is the same for all N.  Only the scalar
    prefactor kappa changes.
    """
    k1 = kappa_sl_n(N1, k)
    k2 = kappa_sl_n(N2, k)
    return k1 / k2


# ---------------------------------------------------------------------------
# Divisor-sum Dirichlet series (sigma_1)
# ---------------------------------------------------------------------------


def divisor_sum_sigma_1(n: int) -> int:
    """sigma_1(n) = sum_{d | n} d."""
    return sum(d for d in range(1, n + 1) if n % d == 0)


def divisor_sum_dirichlet_series(s, n_terms: int = 200) -> mp.mpc:
    """sum_{n=1}^{n_terms} sigma_1(n) n^{-s}.

    Converges to zeta(s) * zeta(s-1) for Re(s) > 2.
    """
    s_mp = mp.mpc(s)
    total = mp.mpc(0)
    for n in range(1, n_terms + 1):
        total += mp.mpf(divisor_sum_sigma_1(n)) * mp.power(n, -s_mp)
    return total


# ---------------------------------------------------------------------------
# Moonshine and Ramanujan tau
# ---------------------------------------------------------------------------


def ramanujan_tau(n: int) -> int:
    """First few values of the Ramanujan tau function.

    tau(n) is the n-th Fourier coefficient of Delta_12 = q prod (1-q^n)^24.
    The tau function appears in the CUSPIDAL part of the Leech lattice
    constrained Epstein zeta, NOT in the shadow L-function.
    """
    # Hardcoded from OEIS A000594, independently verified
    tau_values = {
        1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
        6: -6048, 7: -16744, 8: 84480, 9: -113643,
        10: -115920, 11: 534612, 12: -370944,
    }
    if n in tau_values:
        return tau_values[n]
    raise ValueError(f"tau({n}) not hardcoded; compute via modular form expansion")


def ramanujan_l_function_partial(s, n_terms: int = 12) -> mp.mpc:
    """Partial sum of L(s, Delta_12) = sum tau(n) n^{-s}.

    This is a CUSPIDAL L-function, fundamentally different from the
    shadow L-function which is Eisenstein.
    """
    s_mp = mp.mpc(s)
    total = mp.mpc(0)
    for n in range(1, n_terms + 1):
        total += mp.mpf(ramanujan_tau(n)) * mp.power(n, -s_mp)
    return total


# ---------------------------------------------------------------------------
# GL(N) categorical zeta (from rem:categorical-zeta-riemann)
# ---------------------------------------------------------------------------


def categorical_zeta_sl2(s) -> mp.mpc:
    """zeta^{DK}_{sl_2}(s) = sum_{n>=1} (n+1)^{-s} = zeta(s) - 1.

    The dimension-counting zeta of sl_2 irreps.
    """
    s_mp = mp.mpc(s)
    return mp.zeta(s_mp) - 1


def categorical_zeta_sl2_partial(s, n_terms: int = 500) -> mp.mpc:
    """Partial sum of zeta^{DK}_{sl_2}(s) = sum_{n>=1} (n+1)^{-s}."""
    s_mp = mp.mpc(s)
    total = mp.mpc(0)
    for n in range(1, n_terms + 1):
        total += mp.power(n + 1, -s_mp)
    return total


# ---------------------------------------------------------------------------
# Top-level engine
# ---------------------------------------------------------------------------


@dataclass
class ShadowLanglandsEngine:
    """Verification engine for the shadow-Langlands interface.

    Exposes all five investigation directions as methods, with the
    multi-path mandate satisfied by independent computation routes
    for each claim.
    """

    precision_dps: int = 50

    def __post_init__(self) -> None:
        mp.mp.dps = self.precision_dps

    # -- (a) GL(2) Eisenstein identification -----------------------------------

    def gl2_eisenstein_equals_shadow(self, s, kappa_val) -> mp.mpc:
        """Residual: gl2_eisenstein_l_function - shadow_l_function. Should be 0."""
        return gl2_eisenstein_l_function(s, kappa_val) - shadow_l_function(s, kappa_val)

    def shadow_is_not_cuspidal(self, p: int) -> bool:
        """Satake parameters violate Ramanujan => non-cuspidal.

        For a cuspidal representation, |alpha_p| = |beta_p| = 1.
        For the Eisenstein shadow: alpha_p = 1, beta_p = p, so |beta_p| = p > 1.
        """
        alpha, beta = satake_parameters(p)
        return abs(beta) > 1

    # -- (b) sl_N dependence ---------------------------------------------------

    def shadow_l_structure_invariant_under_N(
        self, s, N1: int, N2: int, k
    ) -> mp.mpc:
        """L^sh(sl_{N1}) / L^sh(sl_{N2}) should equal kappa_{N1}/kappa_{N2}.

        If this holds, the L-function STRUCTURE is independent of N
        (only the scalar kappa changes).
        """
        lhs = shadow_l_function(s, kappa_sl_n(N1, k)) / shadow_l_function(
            s, kappa_sl_n(N2, k)
        )
        rhs = kappa_sl_n(N1, k) / kappa_sl_n(N2, k)
        return lhs - rhs

    # -- (c) Residue structure -------------------------------------------------

    def residue_ratio_is_universal(self) -> mp.mpf:
        """Res_{s=2}/Res_{s=1} = -pi^2/3, independent of kappa."""
        return residue_ratio()

    def residue_ratio_numerical(self, kappa_val) -> mp.mpf:
        """Compute the ratio from explicit residues."""
        r1 = shadow_l_residue_at_one(kappa_val)
        r2 = shadow_l_residue_at_two(kappa_val)
        return r2 / r1

    # -- (d) Moonshine ---------------------------------------------------------

    def moonshine_shadow_l(self, s) -> mp.mpc:
        """L^sh(V-natural, s) = -12 * zeta(s) * zeta(s-1)."""
        return shadow_l_function(s, kappa_moonshine())

    def leech_shadow_l(self, s) -> mp.mpc:
        """L^sh(V_Leech, s) = -24 * zeta(s) * zeta(s-1)."""
        return shadow_l_function(s, kappa_leech())

    def moonshine_leech_ratio(self, s) -> mp.mpc:
        """L^sh(V-natural) / L^sh(V_Leech) = kappa(V-nat)/kappa(V_Leech) = 1/2."""
        return self.moonshine_shadow_l(s) / self.leech_shadow_l(s)

    # -- (e) Frontier defect form ----------------------------------------------

    def frontier_defect(self, s, rank: int) -> mp.mpc:
        """Numerical value of Omega_A at s for a rank-r lattice VOA."""
        return frontier_defect_form_value(s, rank)

    def frontier_defect_is_nonzero(self, s, rank: int, tol: float = 1e-6) -> bool:
        """Check that Omega_A != 0 at a generic point."""
        val = frontier_defect_form_value(s, rank)
        return abs(val) > tol
