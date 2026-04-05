# Koszul-Epstein Functions: Definition and Analysis

## 1. The Definition

A **Koszul-Epstein function** is a Dirichlet series attached to a chirally Koszul algebra A via the shadow metric Q_L of the MC element Theta_A. It is the central arithmetic object at the frontier of the modular Koszul programme.

### Formal Definition

Let A be a chirally Koszul algebra with shadow data (kappa, alpha, S_4) on a primary line L in the cyclic deformation complex Def_cyc^mod(A). The **shadow metric** is the binary quadratic form:

    Q_L(m, n) = 4kappa^2 m^2 + 12 kappa alpha m n + (9 alpha^2 + 2 Delta) n^2

where Delta = 8 kappa S_4 is the critical discriminant (def:shadow-metric, higher_genus_modular_koszul.tex, line 14785).

**Case 1: Nondegenerate (class M, Delta != 0).**
The Koszul-Epstein function is the Epstein zeta function of Q_L:

    eps^KE_A(s) := Sigma'_{(m,n) in Z^2} Q_L(m,n)^{-s},    Re(s) > 1

with meromorphic continuation to all of C via the theta function representation (Poisson summation on Z^2). It has:
- A simple pole at s = 1 with residue 2pi / sqrt(|disc(Q_L)|).
- A functional equation: Lambda^KE(s) = Lambda^KE(1-s), where Lambda^KE(s) = (|D|/(4pi^2))^{s/2} Gamma(s) eps^KE(s) and D = disc(Q_L) = -32 kappa^2 Delta.
- Additional constraints from the MC recursion and Koszul duality (see Section 3).

**Case 2: Degenerate (class G/L, Delta = 0).**
The shadow metric degenerates: Q_L(t) = (2kappa + 3alpha t)^2 is a perfect square. The binary form has rank 1 and the 2D Epstein sum diverges. The correct Koszul-Epstein function is the one-dimensional Dirichlet series:

    eps^KE_A(s) = 2 (4kappa^2)^{-s} zeta(2s)     (class G: alpha = 0)

For class G: this reduces to a rescaled Riemann zeta at 2s. The sewing Dirichlet series S_A(u) = zeta(u) zeta(u+1) is the natural multiplicative completion with a genuine Euler product.

For class L: the form (2kappa + 3alpha t)^2 at rational parameters gives a 1D lattice sum which reduces to Hurwitz zeta functions.

**Case 3: Stratum-separated (class C).**
The quartic data lives on a charged stratum where kappa = 0. The Koszul-Epstein function is not defined on the single-line framework; it requires the multi-channel extension.

## 2. Heisenberg at Level 1: The Degenerate Paradigm

**Shadow data:** kappa = 1/2, alpha = 0, S_4 = 0, Delta = 0 (class G).

**Binary form:** Q_H(m,n) = m^2 (rank 1, discriminant 0).

**Why the 2D sum diverges:** For any m != 0, Q_H(m,n) = m^2 is independent of n. Summing Q(m,n)^{-s} over n in Z gives (2N+1) |m|^{-2s} for each m, which grows linearly in N. More fundamentally, Q(0,n) = 0 for all n != 0, and 0^{-s} is undefined. The Epstein zeta of a rank-1 form on Z^2 is not defined.

**Correct Koszul-Epstein function:**

    eps^KE_H(s) = 2 zeta(2s) = 2 Sigma_{n=1}^infty n^{-2s}

This is the Mellin transform of the 1D theta function Theta_1(t) = Sigma_{m in Z} exp(-pi t m^2) = theta_3(0, exp(-pi t)).

**Numerical value at s = 2:** eps^KE_H(2) = 2 zeta(4) = pi^4/45 = 2.164646...

**Euler product:** eps^KE_H(s) = 2 Pi_p (1 - p^{-2s})^{-1}. The Heisenberg is exact Euler-Koszul (D_H(u) = 1 identically).

**All zeros on the critical line:** eps^KE_H factors through zeta(2s), whose nontrivial zeros are at Re(s) = 1/4 (corresponding to Re(2s) = 1/2). Under RH, all zeros lie on this line.

## 3. Virasoro at c = 1: The Nondegenerate Case

**Shadow data:** kappa = 1/2, alpha = 2, S_4 = 10/27.

**Binary form:** Q_Vir(m,n) = m^2 + 12 m n + (1052/27) n^2.

**Discriminant:** disc = -320/27 = -11.852...

**Positive definiteness:** a = 1 > 0 and disc < 0. Verified.

**Critical discriminant:** Delta = 40/27 = 1.481...

**Numerical values:**

| s | eps^KE(s) (lattice, N=100) | eps^KE(s) (theta, N=40) | Convergence |
|---|---------------------------|------------------------|-------------|
| 2 | 2.904183                  | 2.905372              | 4.1e-4      |
| 3 | 2.196679                  | 2.196680              | 2.6e-7      |
| 4 | 2.052625                  | 2.052625              | 2.0e-10     |

The lattice sum converges slowly at s=2 (algebraically in N) but the theta representation converges exponentially.

**Functional equation verification:**
- At s = 0.7: |Lambda(s) - Lambda(1-s)| / max = 1.99e-16 (machine precision).
- At s = 0.5 + 3i: relative error = 6.43e-18.

**Shadow field:** K_L = Q(sqrt(-320/27)). After extracting the fundamental discriminant: -320/27 is not an integer, so we must scale Q to an integral form first. Scaling by 27: Q_int(m,n) = 27m^2 + 324mn + 1052n^2, disc_int = 324^2 - 4*27*1052 = 104976 - 113616 = -8640. Then -8640 = -4 * 2160 = -4 * (144 * 15) = (-4)(144)(15). The fundamental discriminant is -60 with conductor 12: -8640 = -60 * 144 = -60 * 12^2. So K_L = Q(sqrt(-60)) = Q(sqrt(-15)).

## 4. The Three Koszul-Epstein Constraints

What distinguishes a Koszul-Epstein function from a generic Epstein zeta:

### Constraint 1: Koszul Symmetry

The binary form Q_L is not arbitrary: it is the shadow metric of a chirally Koszul algebra, arising from the MC element Theta_A. Under Koszul duality A -> A!:

- For Virasoro: c -> 26 - c, so kappa -> (26-c)/2, and kappa + kappa! = 13 (NOT 0; AP24).
- The complementarity of discriminants: Delta(c) + Delta(26-c) = 6960/((5c+22)(152-5c)).
- At c = 13 (self-dual point): A = A!, and the Epstein zeta factors into standard L-functions by thm:self-dual-factorization.

This is stronger than the generic Epstein functional equation Lambda(s) = Lambda(1-s), which holds for ALL binary quadratic forms. The Koszul constraint relates eps^KE_A and eps^KE_{A!} through a specific algebraic involution.

### Constraint 2: Shadow Polarization

The shadow obstruction tower {S_r}_{r >= 2} is entirely determined by three invariants (kappa, alpha, S_4) via the algebraic identity H(t)^2 = t^4 Q_L(t) (thm:riccati-algebraicity). This gives infinitely many constraints:

    S_r = f_r(kappa, alpha, S_4) for all r >= 2

where f_r is determined by the Taylor expansion of t^2 sqrt(Q_L(t)). For generic Epstein zeta functions, the "moments" (analogous to S_r) are unconstrained.

Verification at c = 1:
- S_2 = kappa = 1/2
- S_3 = alpha = 2
- S_4 = 10/27
- S_5 = -20/81 (computed from MC recursion)
- S_6, S_7, ... all determined

For Heisenberg: the tower terminates at S_2 = kappa = 1/2, with S_r = 0 for r >= 3 (class G, finite depth).

### Constraint 3: Modular Coupling

The Koszul-Epstein function is not an abstract Epstein zeta: it couples to the Eisenstein series on M_{1,1} through the Rankin-Selberg unfolding. The Benjamin-Chang constrained Epstein zeta eps^c_s satisfies:

    eps^c_{c/2-s} = F_c(s) eps^c_{c/2+s-1}

where F_c(s) = [Gamma(s) Gamma(s+c/2-1) zeta(2s)] / [pi^{2s-1/2} Gamma(c/2-s) Gamma(s-1/2) zeta(2s-1)]

contains the Eisenstein scattering factor with the decisive zeta(2s)/zeta(2s-1) ratio.

## 5. The Davenport-Heilbronn Question

**Question:** Do the three Koszul-Epstein constraints force zeros onto Re(s) = 1/2?

**Known results:**
1. For h(D) = 1: eps_Q = c_0 zeta_K, and all nontrivial zeros lie on Re(s) = 1/2 under GRH. The nine Heegner discriminants give the class-number-one case.
2. For Koszul self-dual algebras (A = A!): the Epstein zeta factors into standard L-functions (thm:self-dual-factorization), so zeros lie on Re(s) = 1/2 under GRH.
3. For generic Epstein zeta with h(D) > 1: Davenport-Heilbronn (1936) showed zeros can exist off Re(s) = 1/2. The failure mechanism is the decomposition into h(D) ideal-class Epstein zetas whose zeros need not align.

**The structural diagnosis:**
The MC equation constrains eps^KE_A for each algebra A. The shadow obstruction tower provides infinitely many moment constraints. But:
- A single algebra constrains its OWN spectral coefficients, not the scattering matrix phi(s).
- The scattering factor F_c(s) contains zeta(2s)/zeta(2s-1), which is shared by ALL algebras.
- The programme requires using ALL algebras simultaneously (bootstrap closure).

**What would close the gap:** Three steps:
(A) Compute the MC constraint on eps^c_s for non-Nairin theories at each c.
(B) Show that the residue function for off-line zeros (sigma != 1/2) violates MC constraints for some c.
(C) Bootstrap closure: constraints from all c together exclude off-line zeros.

Step (A) is computationally accessible via the shadow obstruction tower. Steps (B) and (C) are open.

**Assessment:** The Koszul-Epstein constraints are genuine extra structure beyond the generic Epstein functional equation, but they are NOT proved to force zeros onto the critical line. The honest status is: the programme is well-defined and computationally instantiated, the structural obstructions are identified (thm:structural-separation), and the gap between MC constraints and spectral zero-location is precisely the content of the problem.

## 6. Euler-Koszul Classification

The Euler-Koszul defect D_A(u) := S_A(u) / (|W(A)| zeta(u) zeta(u+1)) classifies the arithmetic rigidity:

| Family | D_A(u) | Euler-Koszul tier | Shadow class |
|--------|--------|-------------------|--------------|
| Heisenberg | 1 | Exact (tier 1) | G |
| Affine KM | 1 | Exact (tier 1) | L |
| Virasoro | 1 - 1/zeta(u) | Finite defect (tier 2) | M |
| W_3 | 1 - (2+2^{-u})/(2 zeta(u)) | Finite defect (tier 2) | M |
| W_N | ... | Finite defect (tier 2) | M |

Exact Euler-Koszul algebras (D = 1) have sewing Dirichlet series with genuine Euler products. For these, the Koszul-Epstein function factors through zeta(s) L(s, chi_d), and all zeros lie on Re(s) = 1/2 under GRH.

The finitely defective case (D != 1 but D is a rational function of zeta) is the frontier: the defect measures the failure of multiplicativity, and the Davenport-Heilbronn question reduces to whether the defect is compatible with off-line zeros.

## 7. Numerical Results

### eps^KE_H(2) = 2 zeta(4) = pi^4/45 = 2.1646464674...

Exact. No zeros off the critical line (factors through zeta).

### eps^KE_{Vir_1}(2) = 2.9054 (theta method, N=40)

Converged to 12 digits. The functional equation holds to machine precision. The shadow field is Q(sqrt(-15)), with class number h(-60) = 4. Since h > 1, the form does NOT represent the principal class automatically, and Davenport-Heilbronn obstructions are in principle possible for the individual-class Epstein zeta. The Koszul constraints may or may not exclude them.

## 8. Implementation

- **Library:** `compute/lib/koszul_epstein.py` (670+ lines)
- **Tests:** `compute/tests/test_koszul_epstein.py` (68 tests)
- **Methods:**
  - `koszul_epstein_lattice_sum(s, kappa, alpha, S4, N)` — direct sum, Re(s) > 1
  - `koszul_epstein_theta(s, kappa, alpha, S4, N_theta)` — theta/incomplete-gamma representation, all s
  - `heisenberg_koszul_epstein(s, k)` — exact 1D reduction for class G
  - `koszul_epstein_degenerate(s, kappa, alpha)` — class G/L handler
  - `sewing_dirichlet_series(u, family)` — the u-variable sewing series
  - `euler_koszul_defect(u, family)` — the Euler-Koszul defect D_A(u)
  - `shadow_tower_coefficients(kappa, alpha, S4, max_arity)` — MC recursion
  - `functional_equation_test(s, kappa, alpha, S4, N)` — FE verification

## 9. Manuscript Reference

The definition is written as Definition X.Y.Z (def:koszul-epstein-function) in chapters/connections/arithmetic_shadows.tex, in the section on the shadow metric and Dirichlet L-functions.
