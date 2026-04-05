"""
genus1_arithmetic_shadow.py — The genus-1 arithmetic shadow of Θ_A.

SYNTHESIS: Three genus-1 invariants of a chiral algebra A sit in a triangle:

                     ε^c_s(A)
                    /         \
                   /           \
    Koszul duality/             \Rankin-Selberg
                 /               \
    S_A(u) -------- sewing -------- F^conn_A(q)

Left edge: Connected Dirichlet-sewing lift (prime side)
  S_A(u) = Σ a_A(N) N^{-u} = ζ(u+1) Σ_i (ζ(u) - H_{w_i-1}(u))
  Has Euler product iff all weights = 1 (Heisenberg, βγ)

Right edge: Benjamin-Chang constrained Epstein (zero side)
  ε^c_s = Σ_{Δ∈S} (2Δ)^{-s}
  Poles at s = (1+z_n)/2 where z_n are nontrivial zeta zeros
  Functional equation from ζ(2s)/ζ(2s-1) ratio

Bottom edge: Connected sewing free energy (q-expansion)
  F^conn_A(q) = -log det(1 - K_q(A)) = Σ a_A(N) q^N

KEY NEW OBJECTS:

1. TWO-VARIABLE L-OBJECT L_A(s,u):
   Morally: ∫_{X_Γ}^reg ⟨Θ_A^{(1),conn}(τ), E*(τ,s)⟩ y^{u-2} dx dy
   s-slice: Benjamin-Chang ε^c_s (zero side)
   u-slice: Dirichlet-sewing lift S_A(u) (prime side)

2. EULER-KOSZUL CRITERION:
   A is Euler-Koszul iff S_A(u) factors as product of shifted ζ-functions.
   Heisenberg: exact. Vir/W_N: finitely defective. Generic Epstein (h(D)≥2): NOT.
   Defect = 1 - 1/ζ(u) for Virasoro — concentrated in critical strip.

3. PRIME-SIDE Li COEFFICIENTS λ̃_n(A):
   From Ξ_A(u) = (u-1)S_A(u), regularized at u=1.
   Heisenberg: positive for n≤6, negative for n≥7.
   Virasoro/W_N: all negative, exponentially growing.
   NOT the same as zero-side Li coefficients for 4ζ(2s).

4. SHADOW DEPTH ↔ EULER DEFECT:
   G (depth 2): D_A = 1 (exact Euler-Koszul)
   L (depth 3): D_A = 1 - O(1/ζ)
   C (depth 4): D_A = 1 - O(1/ζ²)
   M (depth ∞): infinite defect tower

The weight-level arithmetic shadow captures the free-field / character level.
The quartic resonance class Q^contact is the FIRST interacting correction
beyond the character level — it requires actual OPE data.
"""

from mpmath import (mp, mpf, zeta, diff, log, euler as euler_gamma,
                    power, fac, gamma as mpgamma, pi, stieltjes, exp, matrix as mpmatrix, det as mpdet)
import numpy as np

mp.dps = 40


# =============================================================================
# Core: the three genus-1 invariants
# =============================================================================

def _zeta_reg(u):
    """(u-1)*zeta(u), regularized at u=1."""
    eps = u - 1
    if abs(eps) < mpf('1e-15'):
        return (1 + euler_gamma * eps + stieltjes(1) * eps**2 + stieltjes(2) * eps**3)
    return (u - 1) * zeta(u)


class ChiralArithmeticShadow:
    """
    Genus-1 arithmetic shadow for a chiral algebra A with bosonic weight multiset W.
    """

    def __init__(self, name, weights, kappa=None, Q_contact=None):
        self.name = name
        self.weights = weights
        self.rank = len(weights)
        self.kappa = kappa
        self.Q_contact = Q_contact

    def S(self, u):
        """Connected Dirichlet-sewing lift S_A(u)."""
        return zeta(u + 1) * sum(zeta(u) - sum(power(j, -u) for j in range(1, w))
                                  for w in self.weights)

    def Xi(self, u):
        """Regularized Xi_A(u) = (u-1)*S_A(u)."""
        harm_sum = sum(sum(power(j, -u) for j in range(1, w)) for w in self.weights)
        return zeta(u + 1) * (self.rank * _zeta_reg(u) - (u - 1) * harm_sum)

    def euler_defect(self, u):
        """D_A(u) = S_A(u) / (rank * ζ(u)ζ(u+1))."""
        if self.rank == 0:
            return mpf(0)
        return self.S(u) / (self.rank * zeta(u) * zeta(u + 1))

    def is_euler_koszul(self):
        """Check if D_A(u) = 1 identically (all weights = 1)."""
        return all(w == 1 for w in self.weights)

    def li_coefficient(self, n):
        """Prime-side Li coefficient λ̃_n(A)."""
        def f(u):
            return power(u, n - 1) * log(self.Xi(u))
        return diff(f, mpf(1), n) / fac(n - 1)

    def sewing_coefficients(self, N_max):
        """Connected free energy coefficients a_A(N)."""
        coeffs = []
        for N in range(1, N_max + 1):
            a_N = mpf(0)
            for d in range(1, N + 1):
                if N % d == 0:
                    m = N // d
                    count = sum(1 for w in self.weights if w <= m)
                    a_N += mpf(count) / d
            coeffs.append(a_N)
        return coeffs

    def surface_moment_matrix(self, size, alpha=2):
        """Surface Hankel matrix M_{ij} = S_A(alpha+i+j)."""
        M = mpmatrix(size, size)
        for i in range(size):
            for j in range(size):
                M[i, j] = self.S(alpha + i + j)
        return M

    def surface_minors(self, max_size=5, alpha=2):
        """Leading principal minors of surface moment matrix."""
        return [mpdet(self.surface_moment_matrix(k, alpha)) for k in range(1, max_size + 1)]


# =============================================================================
# Standard families
# =============================================================================

HEISENBERG = ChiralArithmeticShadow("Heisenberg", [1], kappa=1)
VIRASORO = ChiralArithmeticShadow("Virasoro", [2], kappa=None, Q_contact=None)
BETA_GAMMA = ChiralArithmeticShadow("βγ", [1, 1], kappa=None)

def W_family(N):
    return ChiralArithmeticShadow(f"W_{N}", list(range(2, N + 1)), kappa=None)


# =============================================================================
# The triangle of invariants
# =============================================================================

def triangle_analysis(family, n_li=10, n_sewing=20):
    """Complete triangle analysis for a family."""
    print(f"\n{'='*70}")
    print(f"GENUS-1 ARITHMETIC SHADOW: {family.name}")
    print(f"  Weights: {family.weights}")
    print(f"  Rank: {family.rank}")
    print(f"  Euler-Koszul: {family.is_euler_koszul()}")
    print(f"{'='*70}")

    # Edge 1: Prime side (S_A at integer points)
    print(f"\n--- S_A(u) at integer points ---")
    for u_val in [2, 3, 4, 5, 10]:
        u = mpf(u_val)
        S_val = family.S(u)
        D_val = family.euler_defect(u)
        print(f"  S({u_val}) = {float(S_val):>15.10f},  D({u_val}) = {float(D_val):>12.10f}")

    # Edge 2: q-expansion (connected free energy)
    print(f"\n--- Connected sewing coefficients a_A(N) ---")
    coeffs = family.sewing_coefficients(n_sewing)
    for i in range(min(10, n_sewing)):
        print(f"  a({i+1}) = {float(coeffs[i]):>12.8f}")

    # Edge 3: Li coefficients
    print(f"\n--- Prime-side Li coefficients λ̃_n ---")
    li_vals = []
    for n in range(1, n_li + 1):
        v = family.li_coefficient(n)
        li_vals.append(v)
        sign = "+" if v >= 0 else "-"
        print(f"  λ̃_{n:>2} = {sign} {float(abs(v)):>15.10f}")

    # Surface moments
    print(f"\n--- Surface moment minors (alpha=2) ---")
    minors = family.surface_minors(4, alpha=2)
    for k, m in enumerate(minors):
        print(f"  det(M_{k+1}) = {float(m):>20.12f}")

    return li_vals, coeffs, minors


# =============================================================================
# Benjamin-Chang bridge: connecting S_A to ε^c_s
# =============================================================================

def bc_bridge_analysis():
    """
    The key connection between S_A(u) and Benjamin-Chang ε^c_s.

    At the self-dual radius R=1:
      ε^1_s(R=1) = 4ζ(2s)  (scalar primary sum)
      S_H(u) = ζ(u)ζ(u+1)  (connected sewing lift)

    These are related by:
      ε^1_s = 4ζ(2s) = Dirichlet series over SCALAR PRIMARIES
      S_H(u) = ζ(u)ζ(u+1) = Dirichlet series over SEWING AMPLITUDES

    The connecting transform is:
      ε^1_s = 4 Σ k^{-2s}  (sum over lattice points k)
      S_H(u) = Σ σ_{-1}(N) N^{-u}  (sum over levels N)

    The passage from ε to S goes through:
      1. Extract scalar primaries (strip descendants via |η|^{2c})
      2. Take logarithm (connected part)
      3. Mellin transform in the q-variable

    So: S_A = Mellin_q(log(η^{-2c} · Z_A))  vs  ε^c_s = Mellin_y(η^{2c} · Z_A)

    The key structural point: ε^c_s sees SCALAR PRIMARIES (polynomial in Δ).
    S_A sees CONNECTED SEWING AMPLITUDES (polynomial in mode level N).
    These are related by plethysm / Möbius inversion.
    """
    print("\n" + "=" * 70)
    print("BENJAMIN-CHANG ↔ DIRICHLET-SEWING BRIDGE")
    print("=" * 70)

    # At R=1: ε^1_s = 4ζ(2s), S_H = ζ(u)ζ(u+1)
    print("\nAt self-dual radius R=1:")
    for s_val in [1.5, 2, 3, 5]:
        s = mpf(s_val)
        eps = 4 * zeta(2 * s)
        S = zeta(2 * s) * zeta(2 * s + 1)  # S_H at u = 2s
        ratio = eps / S
        print(f"  s={float(s):.1f}: ε^1_s = {float(eps):>12.8f}, "
              f"S_H(2s) = {float(S):>12.8f}, ε/S = {float(ratio):>8.5f}")

    # The ratio is 4/ζ(2s+1), which → 4 as s → ∞
    print("\n  Ratio ε^1_s / S_H(2s) = 4/ζ(2s+1):")
    for s_val in [2, 3, 5, 10]:
        print(f"    4/ζ({2*s_val+1}) = {float(4/zeta(2*s_val+1)):>10.8f}")

    print("\n  STRUCTURAL RELATION:")
    print("    ε^c_s(R=1) = 4ζ(2s)  [scalar primary Dirichlet series]")
    print("    S_H(u) = ζ(u)ζ(u+1)  [connected sewing amplitude series]")
    print("    Connection: ε at u=2s is S_H(2s) * 4/ζ(2s+1)")
    print("    = 4 * ζ(2s), recovering BC's result from sewing data")

    # For Virasoro:
    print("\n  VIRASORO EXTENSION:")
    print("    ε^Vir_s involves scalar primaries at Δ = h_{r,s} (Kac table)")
    print("    S_Vir(u) = ζ(u+1)(ζ(u)-1) [weight-2 sewing series]")
    print("    The defect 1-1/ζ(u) = removed weight-1 mode = DS reduction")
    print("    Zero-side: zeta zeros appear through ζ(2s)/ζ(2s-1) in func eq")
    print("    Prime-side: prime decomposition through Euler product of ζ(u)")


# =============================================================================
# The quartic shadow as first interacting correction
# =============================================================================

def quartic_interacting_analysis():
    """
    The weight-level S_A(u) captures the FREE-FIELD arithmetic shadow.
    The quartic resonance class Q^contact is the FIRST INTERACTING correction.

    Free field: spectrum determined by weights alone → S_A(u)
    Interacting: OPE structure constants modify the sewing operator

    The shadow depth classification:
      G (depth 2): free-field exact (Heisenberg, quadratic OPE)
      L (depth 3): tree-level correction (affine, cubic OPE)
      C (depth 4): contact correction (βγ, quartic OPE)
      M (depth ∞): infinite tower (Virasoro, all-order OPE)

    DEEP POINT: The Euler-Koszul defect order correlates with shadow depth
    but is NOT identical. The Euler defect measures the arithmetic structure
    of the CHARACTER. The shadow depth measures the OPE complexity.
    Both are projections of Θ_A but along different axes.
    """
    print("\n" + "=" * 70)
    print("QUARTIC SHADOW AS INTERACTING CORRECTION")
    print("=" * 70)

    # Compare character-level and OPE-level data
    print("\n  CHARACTER LEVEL (weight multiset):")
    print("    Heisenberg: W = {1}, S = ζ(u)ζ(u+1), Euler-Koszul EXACT")
    print("    Virasoro:   W = {2}, S = ζ(u+1)(ζ(u)-1), defect 1/ζ(u)")
    print("    βγ:         W = {1,1}, S = 2ζ(u)ζ(u+1), Euler-Koszul EXACT")

    print("\n  OPE LEVEL (shadow depth):")
    print("    Heisenberg: r_max = 2 (Gaussian), Q^contact = 0")
    print("    Virasoro:   r_max = ∞ (mixed), Q^contact = 10/[c(5c+22)]")
    print("    βγ:         r_max = 4 (contact), Q^contact = 0 (μ_βγ = 0)")

    print("\n  KEY MISMATCH:")
    print("    βγ is Euler-Koszul EXACT but has shadow depth 4")
    print("    Virasoro has defect but shadow depth ∞")
    print("    → Euler-Koszul ≠ finite shadow depth")
    print("    → They measure DIFFERENT faces of Θ_A:")
    print("       Euler-Koszul = arithmetic face (prime decomposition)")
    print("       Shadow depth = homotopy face (A∞ obstruction tower)")

    # Q^contact_Vir at specific c values
    print("\n  Q^contact_Vir(c) = 10/[c(5c+22)]:")
    for c_val in [1, 2, 13, 25, 26, 50]:
        Q = 10 / (c_val * (5 * c_val + 22))
        print(f"    c = {c_val:>3}: Q = {Q:>15.10f}")

    print("\n  At c=13 (self-dual Virasoro): Q = 10/(13·87) = 10/1131")
    print(f"    = {10/1131:.10f}")
    print("  At c=26 (bosonic string): Q = 10/(26·152) = 10/3952")
    print(f"    = {10/3952:.10f}")


# =============================================================================
# The two-variable L-object
# =============================================================================

def two_variable_L_analysis():
    """
    The conjectural two-variable L-object L_A(s,u) unifies:
      s-variable: zero-side (Rankin-Selberg / Eisenstein)
      u-variable: prime-side (Mellin / Dirichlet sewing)

    For Heisenberg at self-dual radius:
      L_H(s,u) should have:
        s-slice at u=2s: proportional to ε^1_s = 4ζ(2s)
        u-slice at s=0: S_H(u) = ζ(u)ζ(u+1)
        Functional equation in BOTH variables

    The shadows should be:
      (s,u) = (scalar, scalar): κ(A) = c/2
      (s,u) = (scalar, prime):  Euler defect D_A
      (s,u) = (spectral, scalar): Δ_A (spectral discriminant)
      (s,u) = (spectral, prime):  S_A(u) full series
      (s,u) = (quartic, ...):     R_4^mod (quartic resonance class)
    """
    print("\n" + "=" * 70)
    print("TWO-VARIABLE L-OBJECT L_A(s,u)")
    print("=" * 70)

    print("\n  The unified object L_A(s,u) should satisfy:")
    print("    L_A(s, 2s) ~ ε^c_s(A)  [zero-side slice]")
    print("    L_A(0, u)  ~ S_A(u)     [prime-side slice]")
    print()
    print("  Functional equations:")
    print("    In s: from ζ(2s)/ζ(2s-1) factor (Benjamin-Chang)")
    print("    In u: from (u-1)ζ(u) regularization")
    print()
    print("  Shadow decomposition of L_A:")
    print("    Level 0: κ(A)·ζ·ζ  [scalar amplitude × Euler product]")
    print("    Level 1: Δ_A correction [spectral discriminant]")
    print("    Level 2: S_A defect [Euler-Koszul failure]")
    print("    Level 3: R_4^mod correction [quartic resonance class]")
    print("    Level ∞: full Θ_A [modular MC element]")

    # Heisenberg: exact factorization
    print("\n  HEISENBERG (exact Euler-Koszul):")
    print("    L_H(s,u) = 4·ζ(2s)·ζ(u)·ζ(u+1) / [normalization]")
    print("    All shadows determined by κ=1 and the Euler product")
    print("    No interacting correction needed")

    # Virasoro: the defect creates mixed (s,u) dependence
    print("\n  VIRASORO (Euler-defective):")
    print("    L_Vir(s,u) = L_H(s,u) · (1 - 1/ζ(u)) + interacting corrections")
    print("    The defect 1/ζ(u) creates s,u mixing")
    print("    Q^contact = first interacting correction at arity 4")
    print("    The FULL tower of corrections = shadow obstruction tower of Θ_Vir")


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    triangle_analysis(HEISENBERG, n_li=8)
    triangle_analysis(VIRASORO, n_li=8)
    triangle_analysis(W_family(3), n_li=5)

    bc_bridge_analysis()
    quartic_interacting_analysis()
    two_variable_L_analysis()
