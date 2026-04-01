# Adversarial Attack: "Integration over moduli is analytic not algebraic"

## Date: 2026-04-01
## Status: Adjudicated

---

## 0. The Claim Under Attack

The claim (appearing in `compute/audit/benjamin_chang/derived_category.md` and related audit files) is:

> "the spectral decomposition on the modular curve [is] a fundamentally analytic (not algebraic) construction"

> "The passage from characters to spectral zeta requires spectral analysis on the modular curve, which is NOT a categorical operation."

> "No purely algebraic/categorical construction can bridge this gap."

The adversarial challenge says: derived global sections R\Gamma(M_g, F) are purely algebraic. Sheaf cohomology is computed by Cech complexes. The bar complex defines a sheaf. Therefore the "full spectrum" should be algebraic.

---

## 1. What the Manuscript Actually Constructs (Algebraic Side)

The manuscript defines and proves the following chain of algebraic constructions:

### 1.1 The center local system Z(A)

**Definition** (introduction.tex line 1156, higher_genus_complementarity.tex line 165):
The center local system Z_A is the local system on M-bar_g whose fiber over [Sigma_g] is the center Z(A|_{Sigma_g}) -- the commutant of A acting on itself via the chiral bracket.

This is an **algebraic** object: a local system (= locally constant sheaf) on the algebraic stack M-bar_g.

### 1.2 The fiber-center identification

**Theorem C_0** (thm:fiber-center-identification, higher_genus_complementarity.tex line 324):

    R^q pi_{g*} B-bar^{(g)}(A) = 0    for q != 0
    R^0 pi_{g*} B-bar^{(g)}(A) = Z_A

This identifies the derived pushforward of the bar complex along the universal curve pi: C-bar_g -> M-bar_g with the center local system. **Purely algebraic**: derived pushforward of a coherent complex along a morphism of algebraic stacks.

### 1.3 The ambient complex

**Definition** (def:thqg-III-holographic-ambient, thqg_symplectic_polarization.tex line 97):

    C_g(A) := R\Gamma(M-bar_g, Z(A))

Derived global sections of an algebraic local system on an algebraic stack. **Purely algebraic**.

### 1.4 Complementarity (Theorem C)

**Theorem** (thm:quantum-complementarity-main):

    C_g(A) = Q_g(A) + Q_g(A!)

Lagrangian decomposition via Verdier involution. **Purely algebraic**.

### 1.5 The obstruction class

    obs_g(A) = kappa(A) * lambda_g in H^{2g}(M-bar_g, Q)

An algebraic cohomology class. **Purely algebraic**.

### 1.6 The generating function

    sum_{g>=1} obs_g * hbar^{2g} = kappa(A) * (A-hat(i*hbar) - 1)

Computed by GRR on the universal curve. **Purely algebraic**.

**Verdict on the algebraic side: CORRECT.** Everything in the monograph's proved core (Theorems A-D+H, the shadow tower, the obstruction classes, the Lagrangian complementarity) is purely algebraic. R\Gamma(M-bar_g, Z_A) is computed by algebraic methods. The Hodge bundle E = pi_* omega is an algebraic vector bundle. The Chern classes lambda_g are algebraic cycle classes. All of this is correct and purely algebraic.

---

## 2. Where the Analysis Breaks (The Adversary's Error)

The adversarial attack conflates TWO DIFFERENT operations that both involve "integration over moduli":

### Operation A (Algebraic): Derived global sections of Z_A

    C_g(A) = R\Gamma(M-bar_g, Z_A)

This is sheaf cohomology. It produces a finite-dimensional cochain complex (Prop thqg-III-ambient-properties(i): H^n(C_g) finite-dimensional, nonzero only for 0 <= n <= 6g-6). It captures the DEFORMATION-OBSTRUCTION theory of the bar complex. It produces tautological classes (lambda_g, kappa classes, etc.). This is purely algebraic and is what the monograph's proved core computes.

### Operation B (Analytic): Roelcke-Selberg spectral decomposition of Z-hat^c on M_{1,1}

    integral_{SL(2,Z)\H} Z-hat^c(tau, tau-bar) * E_s(tau) d mu(tau)

This is an L^2 inner product on the hyperbolic surface SL(2,Z)\H, decomposing the function Z-hat^c into eigenfunctions of the hyperbolic Laplacian Delta = -y^2(d^2/dx^2 + d^2/dy^2). The Eisenstein series E_s(tau) is a **real-analytic** eigenfunction of the Laplacian, NOT a holomorphic section of any algebraic line bundle.

### THE CRITICAL DISTINCTION

These are genuinely different mathematical operations, even though they both involve M_{1,1}:

**Operation A** works with the CENTER LOCAL SYSTEM Z_A, which is an algebraic (in fact locally constant) sheaf on M-bar_{g}. Its derived global sections capture algebraic invariants: tautological classes, Chern classes of the Hodge bundle, Verdier duality eigenspaces.

**Operation B** works with the PARTITION FUNCTION Z(tau, tau-bar) as a function on the complex upper half-plane, viewed as a real-analytic function on the Riemannian manifold SL(2,Z)\H. Its spectral decomposition uses the Riemannian Laplacian, which is NOT an algebraic operator.

The partition function Z(tau, tau-bar) and the center local system Z_A are RELATED but NOT THE SAME OBJECT:

- Z_A captures the algebraic/chiral center -- what the bar complex sees.
- Z(tau, tau-bar) = tr_{V} q^{L_0 - c/24} q-bar^{L-bar_0 - c/24} involves the TRACE over the entire representation theory, computed using the ANALYTIC sewing operator. This produces a function of (tau, tau-bar), not a section of an algebraic sheaf.

### Why Z(tau, tau-bar) is not a section of Z_A

The center local system Z_A has fiber Z(A|_{Sigma_g}), the commutant of A acting on itself. For genus 1, the center Z(A|_{E_tau}) consists of degree-0 Hochschild cocycles -- the "zeroth chiral Hochschild cohomology." This is a finite-dimensional algebraic object at each fiber.

The partition function Z(tau, tau-bar) = sum_n dim(V_n) q^{n - c/24} is computed by TRACING over the FULL STATE SPACE V = bigoplus V_n, which is infinite-dimensional. It involves:
1. The sewing operator K_q (the propagator acting on the Hilbert space), which requires ANALYTIC completion
2. The anti-holomorphic variable tau-bar (the partition function is a real-analytic function on H, not a holomorphic section)
3. The Fredholm determinant det(1-K_q), which requires the HS-sewing condition (a convergence/analytic condition)

The sewing-Selberg formula (thm:sewing-selberg-formula) makes this explicit:

    integral_{M_{1,1}} log det(1-K(tau)) * E_s(tau) d mu(tau) = -2(2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s)

The left side is an integral of the Fredholm determinant (an analytic object) against the Eisenstein series (a real-analytic eigenfunction of the Laplacian), with the hyperbolic measure d mu(tau) = y^{-2} dx dy. None of these ingredients are algebraic:
- det(1-K_q) requires Hilbert-space completion
- E_s(tau) is a real-analytic automorphic form, not algebraic
- d mu(tau) = y^{-2} dx dy is the Riemannian volume form, not an algebraic measure

---

## 3. The Adversary's Specific Sub-Claims Evaluated

### Claim: "R\Gamma(M_g, F) is purely algebraic"

**TRUE but IRRELEVANT.** R\Gamma(M-bar_g, Z_A) is purely algebraic and the monograph computes it. But this operation produces tautological/Hodge classes (lambda_g, etc.), NOT the spectral zeta epsilon^c_s. The spectral zeta comes from a DIFFERENT operation on a DIFFERENT object (the partition function Z(tau,tau-bar), not the center local system Z_A).

### Claim: "Sheaf cohomology H*(M_g, F) is computed by Cech complexes"

**TRUE but IRRELEVANT.** The sheaf cohomology H*(M-bar_g, Z_A) is what Theorem C computes. It decomposes into Q_g(A) + Q_g(A!). This is NOT the spectral zeta.

### Claim: "The Hodge bundle E is algebraic, lambda_g is algebraic"

**TRUE and ALREADY USED.** The monograph fully exploits this: obs_g = kappa * lambda_g is an algebraic class. The A-hat generating function is algebraic. This is the proved core.

### Claim: "Factorization homology integral_{Sigma_g} A is computed algebraically (Ayala-Francis)"

**TRUE but REQUIRES CARE.** Factorization homology for a FIXED Sigma_g is algebraic (it is chiral homology in the sense of Beilinson-Drinfeld). As Sigma_g varies over M_g, one gets a sheaf on M_g whose derived global sections are algebraic. This is what the monograph does. But this does NOT produce the partition function Z(tau, tau-bar): factorization homology integral_{Sigma_g} A = H^*(A, d) on P^1, and HH^*(A) on E_tau. The partition function is the GRADED TRACE of the sewing operator, not the Hochschild homology.

### Claim: "E(tau,s) is a section of a line bundle (the Eisenstein sheaf)"

**FALSE.** The real-analytic Eisenstein series E_s(tau) = sum_{(m,n)!=0} y^s / |m tau + n|^{2s} is NOT a section of an algebraic line bundle. It is:
- Real-analytic (depends on tau and tau-bar)
- An eigenfunction of the hyperbolic Laplacian Delta (with eigenvalue s(1-s))
- For Re(s) > 1, defined by an absolutely convergent sum; for other s, by meromorphic continuation

There IS a notion of "Eisenstein sheaf" in the geometric Langlands programme (Beilinson-Bernstein, Drinfeld), but this is a D-MODULE on the modular curve, not a line bundle, and its relationship to the real-analytic E_s(tau) goes through the Riemann-Hilbert correspondence -- which is itself a transcendental (non-algebraic) construction.

### Claim: "The Rankin-Selberg integral is a sheaf-cohomology pairing"

**FALSE.** The Rankin-Selberg integral integral_{M_{1,1}} Z-hat^c * E_s d mu is an L^2 inner product on the Riemannian manifold SL(2,Z)\H. While the underlying space M_{1,1} is algebraic, the inner product uses:
- The hyperbolic metric (Riemannian, not algebraic)
- The Eisenstein series E_s (real-analytic, not algebraic)
- The L^2 pairing (functional-analytic, not sheaf-theoretic)

The Rankin-Selberg method is a tool of ANALYTIC number theory, not algebraic geometry. Its algebraicization is one of the major open problems of the Langlands programme.

---

## 4. The Precise Location of the Algebraic/Analytic Boundary

The monograph's architecture has a clean boundary:

### ALGEBRAIC (proved, the monograph's core):

1. The bar complex B(A) on Ran(X) -- algebraic factorization coalgebra
2. The center local system Z_A on M-bar_g -- algebraic local system
3. R\Gamma(M-bar_g, Z_A) = Q_g(A) + Q_g(A!) -- derived global sections (Theorem C)
4. obs_g = kappa * lambda_g -- algebraic cohomology class (Theorem D)
5. The shadow tower Theta_A -- MC element in algebraic deformation complex
6. The Hodge bundle E, lambda_g, psi classes -- algebraic tautological ring
7. The A-hat generating function -- algebraic (GRR)

### ANALYTIC (the arithmetic frontier, arithmetic_shadows.tex):

1. The partition function Z(tau, tau-bar) = tr_V q^{L_0-c/24} q-bar^{L-bar_0-c/24} -- requires analytic completion (sewing envelope)
2. The primary-counting function Z-hat^c = y^{c/2} |eta|^{2c} Z -- real-analytic function on H
3. The Roelcke-Selberg decomposition of Z-hat^c -- spectral theory of the Laplacian on H
4. The Eisenstein series E_s(tau) -- real-analytic eigenfunction
5. The Rankin-Selberg integral -- L^2 inner product
6. The constrained Epstein zeta epsilon^c_s -- Dirichlet series from spectral decomposition
7. The scattering matrix phi(s) = Lambda(1-s)/Lambda(s) -- involves zeta zeros

### THE BRIDGE (partially proved, the sewing programme):

The bridge between algebraic and analytic is the SEWING construction:
- The sewing envelope A^{sew} = Hausdorff completion (MC5, analytic)
- The HS-sewing criterion (thm:general-hs-sewing, proved for standard landscape)
- The Fredholm determinant det(1-K_q) (analytic)

The sewing-Selberg formula (thm:sewing-selberg-formula) is the explicit bridge: it connects the algebraic Fredholm determinant to the analytic Rankin-Selberg integral. But the bridge itself is analytic.

---

## 5. What a Purely Algebraic Construction COULD Produce

The adversary's instinct has a valid core: one SHOULD ask what sheaf on M_g the bar complex defines, and whether its derived global sections capture the spectral data.

The answer is: the bar complex defines the center local system Z_A, and its derived global sections R\Gamma(M-bar_g, Z_A) capture the DEFORMATION-OBSTRUCTION data (Theorem C). This is algebraic and is fully exploited.

What it does NOT capture:
- The partition function (requires trace over infinite-dimensional Hilbert space)
- The spectral zeta (requires Roelcke-Selberg decomposition)
- The scattering matrix (requires zeta zeros)

Could there be a DIFFERENT algebraic construction that captures the spectral data? This is the "motivic spectral zeta" question (derived_category.md section 8.4). It would require:
1. A categorical version of the Roelcke-Selberg decomposition
2. A categorical functional equation (from the modular tensor category structure)
3. A "motivic Mellin transform"

This is related to the geometric Langlands programme's goal of categorifying automorphic spectral decompositions. No such construction exists.

---

## 6. Verdict

The claim "integration over moduli is analytic not algebraic" is **imprecise but substantively correct** when applied to the spectral zeta / Roelcke-Selberg / Rankin-Selberg operations. The adversary is correct that:

1. R\Gamma(M-bar_g, Z_A) is purely algebraic -- and the monograph already computes this.
2. The Hodge bundle and its Chern classes are algebraic -- and the monograph uses this.
3. Factorization homology is algebraic -- and the monograph exploits this.

But the adversary is wrong that these algebraic operations produce the spectral zeta epsilon^c_s. The spectral zeta requires:
- The partition function Z(tau, tau-bar), which is a TRACE (analytic)
- The hyperbolic Laplacian on M_{1,1}, which is Riemannian (non-algebraic)
- The Eisenstein series E_s, which is real-analytic (non-algebraic)
- The Rankin-Selberg integral, which is L^2 (analytic number theory)

The precise statement should be:

> **The bar complex defines an algebraic local system Z_A on M-bar_g whose derived global sections R\Gamma(M-bar_g, Z_A) capture the deformation-obstruction theory (Theorem C). The spectral zeta epsilon^c_s requires a DIFFERENT operation: the Roelcke-Selberg spectral decomposition of the partition function Z(tau,tau-bar) on SL(2,Z)\H, which uses the Riemannian Laplacian and is genuinely analytic. The bridge between the algebraic (bar/center) and analytic (spectral zeta) sides is the sewing construction.**

### Summary of errors in the original claim

The phrase "the full spectrum requires integration over moduli space, which is analytic not algebraic" is misleading because:
- "Integration over moduli space" is ambiguous: R\Gamma is algebraic, the RS integral is analytic
- The issue is not that integration is analytic, but that the OBJECT BEING INTEGRATED (the partition function) and the DECOMPOSITION METHOD (Roelcke-Selberg) are analytic
- The correct locus of non-algebraicity is the passage from the center local system Z_A (algebraic) to the partition function Z(tau,tau-bar) (analytic) via the sewing construction

### Summary of errors in the adversarial attack

1. E_s(tau) is NOT a section of an algebraic line bundle (it is real-analytic)
2. The RS integral is NOT a sheaf-cohomology pairing (it is an L^2 inner product)
3. Z(tau,tau-bar) is NOT a section of Z_A (it is a trace over the full Hilbert space, not a commutant element)
4. The operation that produces epsilon^c_s is genuinely non-algebraic (Riemannian spectral theory)

---

## 7. A Subtlety: Free Energy F_g vs Partition Function Z(tau, tau-bar)

The compute engine identifies factorization homology with the partition function:
    integral_{Sigma_g} A = F_g(A)

This needs disambiguation:

- F_g(A) = kappa(A) * lambda_g^{FP} = kappa * int_{M-bar_{g,1}} psi^{2g-2} lambda_g
  is a NUMBER, computed by integrating an algebraic class over an algebraic cycle.
  This is ALGEBRAIC. The free energy numbers F_1 = kappa/24, F_2 = 7 kappa/5760, ...
  are rational multiples of kappa, computed by GRR. No analysis needed.

- Z(tau, tau-bar) = sum_{n,m} d(n,m) q^n q-bar^m is a FUNCTION of the modular
  parameter tau, computed by tracing the sewing operator over the full Hilbert space.
  This requires ANALYTIC completion (sewing envelope, HS condition).

- The spectral zeta epsilon^c_s comes from decomposing Z-hat^c(tau, tau-bar) via the
  hyperbolic Laplacian. This requires REAL-ANALYTIC spectral theory.

The free energies F_g are the genus-g CONTRIBUTIONS to the full partition function.
They capture the algebraic part. The full Z(tau, tau-bar) packages all genera together
with the tau-dependence, which is analytic. The spectral zeta decomposes this
tau-dependent object using Riemannian geometry on H.

So the precise boundary is:
- The individual numbers F_g: ALGEBRAIC (tautological intersection numbers)
- The partition function Z(tau, tau-bar) as a modular function: ANALYTIC (requires sewing)
- The spectral zeta epsilon^c_s: ANALYTIC (requires Roelcke-Selberg)

## 8. Four Questions the Adversary Raised, Answered (renumbered from Q1-Q4)

### Q1: What SHEAF on M_g does the bar complex define?

**Answer**: The center local system Z_A, whose fiber over [Sigma_g] is Z(A|_{Sigma_g}) = the commutant of A in itself. This is proved by the fiber-center identification (thm:fiber-center-identification): R^0 pi_{g*} B-bar^{(g)}(A) = Z_A, with higher R^q vanishing (Koszulness concentration).

### Q2: The shadow curvature kappa * lambda_g is algebraic. Are the higher shadow coefficients S_r higher Chern classes or derived push-forwards?

**Answer**: The higher shadows S_r are NOT Chern classes of the Hodge bundle. They are Taylor coefficients of the MC element Theta_A in the cyclic deformation complex Def_cyc^mod(A). They live in the cohomology of the modular operad's Feynman transform, not in the tautological ring R*(M-bar_g). The single-line dichotomy (thm:single-line-dichotomy) shows that S_r satisfy an algebraic recurrence (the shadow metric Q_L = (2kappa + 3 alpha t)^2 + 2 Delta t^2), so they are algebraic invariants of A, but they are NOT Chern classes of any specific bundle on M-bar_g. At genus g, the arity-r shadow S_r contributes to obs_{g,n} for n = r (pointed moduli), not to obs_g (unpointed).

### Q3: For varying Sigma_g over M_g, the "universal factorization homology" integral_{univ} A is a sheaf on M_g. Do its derived global sections give the spectral data?

**Answer**: The derived global sections R\Gamma(M-bar_g, integral_{univ} A) give exactly C_g(A) = R\Gamma(M-bar_g, Z_A) by the fiber-center identification. This is Theorem C, and it gives the Lagrangian complementarity Q_g(A) + Q_g(A!), NOT the spectral zeta. The spectral zeta requires a different input (the partition function, computed via sewing) and a different operation (Roelcke-Selberg, computed via the Riemannian Laplacian).

### Q4: Is the Rankin-Selberg integral "computable as sheaf cohomology"?

**Answer**: No. The RS integral integral_{M_{1,1}} Z-hat^c * E_s d mu pairs a real-analytic function (Z-hat^c) with a real-analytic eigenfunction (E_s) using the Riemannian L^2 inner product (d mu). This is analytic number theory, not sheaf cohomology. Algebraicizing this operation is one of the central problems of the geometric Langlands programme (categorifying the spectral decomposition of automorphic forms). The manuscript's structural-obstruction remark (rem:structural-obstruction) makes the precise statement: the spectral parameter t is real on the spectral line but the zeta zeros live at complex t, and algebraic constraints on the real line cannot reach the complex poles without analytic continuation.
