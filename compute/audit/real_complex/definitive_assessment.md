# The Real-to-Complex Frontier: Definitive Assessment

## Date: 2026-04-01
## Status: FINAL

## Sources consulted

- compute/audit/descent_chain/ (10 analysis files, 200K+ of rigorous analysis)
- compute/audit/koszul_epstein/ (6 analysis files, 100K+ of rigorous analysis)
- Vol I working_notes.tex (existing Koszul-Epstein and spectral sections)
- Vol II working_notes.tex (existing gravity and spectral sections)
- arithmetic_shadows.tex (the manuscript chapter)
- The full compute test suite (euler_koszul_engine, dirichlet_sewing, shadow tests, koszul_epstein)
- Beilinson Principle and all 32 anti-patterns

---

## The Central Question

Can any real-to-complex extension bridge the gap from the bar complex (real spectral data: shadow coefficients, MC recursions, OPE invariants) to zeta zeros (complex spectral data: the zero set of an entire function of order 1)?

## The Answer

**No.** The gap is fundamental in the single-algebra setting and structurally blocked in the multi-algebra bootstrap setting. The bar complex is inherently limited to real spectral data because it is an algebraic object; zeta zeros are analytic objects. The gap between them is the gap between algebra and analysis.

---

## 1. Eight Candidate Approaches: Classification

### Dead ends (5)

| # | Approach | Why it fails |
|---|----------|-------------|
| 1 | Deligne categories | Interpolates in a categorical variable, not a spectral one. The shadow obstruction tower at non-integer c is already well-defined by rational interpolation; no Deligne category needed. |
| 2 | Wick rotation in c | The sewing Dirichlet series S_A(u) is c-independent. Varying c changes shadow coefficients but not S_A(u). The two variables are orthogonal. |
| 3 | MC4 resonance/completion | Solves a homological algebra problem (bar-cobar for non-quadratic infinite-generator algebras), not a number-theoretic one. Resonance rank classifies algebraic completion difficulty, not L-function analytics. |
| 4 | Borel resummation | The shadow series converges absolutely (Bernoulli decay ~ (2pi)^{-2g}). There is nothing to resummate. The non-perturbative data (D-branes, ZZ instantons) is external to the bar construction. |
| 5 | Spectral curves | Spectral curves encode genus-0 OPE data (the same three parameters kappa, alpha, S_4). The "spectral" in "spectral curve" refers to matrix-model spectrum, not automorphic spectrum. |

### Genuine mathematics, no bridge (2)

| # | Approach | What it produces | Why no bridge |
|---|----------|-----------------|--------------|
| 6 | Analytic continuation of shadow obstruction tower | Quadratic number fields K_L = Q(sqrt(disc(Q_L))) at each rational c. Galois structure, splitting of primes, class numbers. | The number field lives on the arity axis. The Dirichlet L-function L(s, chi_d) is a classical object from algebraic number theory, not produced by the bar construction. |
| 7 | Analytic Langlands | Correct framework for critical-level oper/shadow interpolation. Bar complex at k = -h^v computes opers (local geometric Langlands). | Operates on function fields (curves over C). The number-field Riemann Hypothesis requires arithmetic descent, which is the deepest unsolved problem in the Langlands programme. |

### Most structurally compatible, but no construction exists (1)

| # | Approach | Compatibility | Obstruction |
|---|----------|--------------|-------------|
| 8 | Non-commutative geometry (Connes-Marcolli) | Bost-Connes Hecke algebra compatible with Verdier-Hecke commutation. Verdier self-duality at c=13 provides involution on factorisation coalgebra. | Arithmetic descent: bar complex over C, Bost-Connes over Q. No construction connects them. |

---

## 2. The Structural Theorem (why the gap is fundamental)

Three facts combine to a negative structural result:

**(i)** The shadow obstruction tower on a single primary line is determined by three numbers (kappa, alpha, S_4). These constitute a finite-dimensional algebraic datum.

**(ii)** The zeros of zeta(s) encode infinitely many independent transcendental quantities (the imaginary parts gamma_n are believed algebraically independent).

**(iii)** No finite-dimensional algebraic structure determines the zeros of an entire function of order 1 (by Hadamard factorisation: zeros determine the function, but finitely many algebraic constraints on coefficients cannot determine zeros).

Therefore: **the bar complex of a fixed chiral algebra A produces finitely many algebraic invariants, which cannot determine infinitely many analytic quantities.**

---

## 3. The Bootstrap Escape and Its Three Failures

The single-algebra obstruction suggests using ALL algebras simultaneously. This fails for three independent reasons:

**(a) c-independence of S_A(u).** For all Virasoro algebras at all central charges, S_Vir(u) = zeta(u+1)(zeta(u)-1). Varying c changes shadow coefficients but not the sewing lift. The bootstrap has no leverage on the spectral variable u.

**(b) Rankin-Selberg erasure.** The unfolded integral depends only on Fourier coefficients of the partition function, not on the MC bracket structure. The MC equation constrains the spectral coefficients c_j, but the L-functions L(s, f_j) are properties of the eigenforms f_j, independent of A.

**(c) Flatness vs positivity.** The MC equation D*Theta + (1/2)[Theta,Theta] = 0 is a quadratic integrability (flatness) condition. The Li criterion requires positive definiteness of a specific bilinear form. The chain MC -> Rankin-Selberg -> Li positivity does not close because Rankin-Selberg is not sign-preserving.

---

## 4. The Beilinson Verdict: False Ideas Dismissed

| # | False claim | Why false | How verified |
|---|------------|-----------|-------------|
| 1 | "Bar-cobar forces Epstein zeros onto Re(s)=1/2" | Davenport-Heilbronn counterexamples for generic Epstein with h(D)>=2 | Computed h(D) for 27 minimal models; 25 have h>=2, EXPOSED to DH |
| 2 | "MC implies Li positivity" | MC is flatness; Li is positivity | Li coefficients for Heisenberg turn negative at n=7 (uncompleted) and n=974 (completed) |
| 3 | "Shadow obstruction tower descends to functional equation of S_A(u)" | Shadow obstruction tower acts on arity variable t; sewing lift on spectral variable u | S_A(u) is c-independent, proved |
| 4 | "c=13 related to Re(s)=1/2" | Different involutions on different spaces (AP9) | Koszul involution depends on Virasoro central charge; zeta FE on Euler product |
| 5 | "Surface positivity converts quartic to Li positivity" | No surface constructed; no polarisation identified | Li coefficients become negative at n=974 for completed Heisenberg, contradicting positive Gram |
| 6 | "Three involutions are the same" | Three distinct order-2 maps on different objects with different fixed points | Verdier: D_Ran on FactCoalg; Galois: sigma on K_L; Koszul: A->A! on families |
| 7 | "Simultaneous-family closure" | Not formulated precisely; bare spectral measures fail by 4-5 orders of magnitude | rn105 quartic Gram test, Liouville/Toda |
| 8 | "Shadow Riemann Hypothesis" | Multiple critical lines are structural features (E_8: two lines; Leech: three); Li sign change at n=7 | Bombieri-Lagarias criterion fails for any function with zeros on two lines |

---

## 5. What Survives (Genuine Mathematics)

### Proved results that stand independently of RH

| # | Result | Status |
|---|--------|--------|
| 1 | MC recursion + Carleman uniqueness: spectral measure uniquely determined by (kappa, alpha, S_4) | PROVED |
| 2 | Route C prime-locality: MC propagates Hecke equivariance from low-arity to all arities | PROVED |
| 3 | Shadow-spectral correspondence for lattice VOAs: depth = #critical_lines - 1 | PROVED |
| 4 | Verdier-Hecke commutation forces L-function factorisation at self-dual points | PROVED |
| 5 | Galois structure of shadow obstruction tower: quadratic extension K_L/F with Koszul sign monodromy | PROVED |
| 6 | Bar = Fourier-Mukai for abelian (Heisenberg on E_tau = Poincare bundle) | PROVED |
| 7 | Bar = non-abelian generalisation with four structural properties | PROVED |
| 8 | Critical-level bar computes opers (local geometric Langlands) | PROVED |
| 9 | Shadow number fields at minimal models with explicit class numbers | VERIFIED |
| 10 | Splitting principle: prime p sees shadow obstruction tower as finite iff p splits in K_L | PROVED |

### Open but meaningful (not false, not proved)

| # | Question | Status |
|---|----------|--------|
| 1 | Crossing-weighted bilinear residue kernel satisfies quartic Gram matching at on-line zeros | UNTESTED (correct formulation, requires DOZZ/Toda structure constants) |
| 2 | Arithmetic comparison conjecture: Theta_A determines nabla^arith_A | OPEN |
| 3 | Prime-locality at subleading order in 1/c for Virasoro | TESTABLE |

---

## 6. The Deepest Structural Question: Fundamental or Contingent?

### For a single algebra: FUNDAMENTAL
Three numbers cannot determine infinitely many zeros. No extension of the bar complex that preserves its algebraic character can bridge this gap.

### For the standard landscape simultaneously: BLOCKED
S_A(u) is c-independent for each family. The bootstrap has nothing to bootstrap. Varying the algebra within a family gives no spectral leverage.

### For a hypothetical construction that accesses the full partition function: CATEGORICAL OBSTRUCTION
The representation category (which determines the primary spectrum and hence the constrained Epstein eps^c_s) cannot be reconstructed from the bar complex. The bar complex determines the Koszul dual A! and the shadow obstruction tower, not the representation category. The primary spectrum is a representation-theoretic invariant; the bar complex is an algebra-theoretic invariant. They live in different categories.

### For the bar complex augmented with external analytic input: MOOT
If one has access to the full partition function Z(tau, tau-bar), then one already has access to the spectral decomposition of Z on M_{1,1}, and the bar complex adds only algebraic constraints on the spectral coefficients (the MC recursion on the shadow obstruction tower). These constraints are finite-dimensional and algebraic; they cannot determine the location of L-function zeros.

---

## 7. The Correct Picture

The descent chain, as a linear sequence from Fourier to L-functions, is broken at Level 2->3. But the bar construction provides something better than a descent chain: a FAN of three independent projections from a single MC element Theta_A:

```
            Theta_A
           /   |   \
    Shadow    Genus   Koszul
     tower    tower    dual
  (arithmetic) (topological) (algebraic)
```

These three outputs are facets of Theta_A, not levels of a chain. The shadow obstruction tower detects arithmetic structure (Hecke eigenforms for lattice VOAs, quadratic fields at rational c). The genus tower computes Mumford classes (tautological ring of M-bar_g). The Koszul dual determines the complementary algebra (A! = boundary of the bulk). All three are proved. None descends to zeta zeros. None needs to.

The bar complex is the algebraic engine of modular Koszul duality. It illuminates the structure of chiral algebras, their shadow obstruction towers, and their modular geometry. The Riemann Hypothesis is not within its scope, and recognising this is progress.

---

## Files Produced

- This definitive assessment: `compute/audit/real_complex/definitive_assessment.md`
- Vol I working notes: new section "The real-to-complex frontier" (sec:real-to-complex-frontier)
- Vol II working notes: new section "Complex parameters in quantum gravity" (sec:complex-parameters-qg)
- Both compile cleanly (65pp and 42pp respectively, 0 LaTeX errors in the new sections).
