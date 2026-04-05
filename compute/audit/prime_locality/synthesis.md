# Prime-Locality Assessment: Definitive Synthesis

## Status: PARTIALLY PROVED, PARTIALLY OPEN, NOT DEAD

## Executive Summary

Prime-locality is proved for lattice VOAs and rational VOAs. It is open for irrational VOAs (Virasoro at generic c, W_3 at generic c). It is structurally impossible to extract zero-location information from the genus-1 MC equation. The programme is alive but narrower than originally conceived.

## Question 1: Is prime-locality achievable for non-lattice chiral algebras?

**YES for rational non-lattice VOAs. OPEN for irrational non-lattice VOAs.**

For rational VOAs (e.g., Ising c=1/2, tricritical Ising c=7/10, three-state Potts c=4/5): PROVED. The Franc-Mason vector-valued Hecke theory decomposes the character vector into eigencomponents. The theta-bridge (Rocha-Caridi formula) decomposes |chi_{r,s}|^2 into lattice Epstein zeta functions. The non-multiplicativity of the scalar Dirichlet series D(s) = sum a_n n^{-s} (14 coprime failures at c=1/2 with m,n <= 20) is a **projection artefact**: the sum of individually multiplicative L-functions is not multiplicative, but each summand retains its Euler product.

For irrational VOAs (Virasoro at generic c): OPEN. The partition function |eta(tau)|^{2c} for irrational c is not a modular form for any congruence subgroup. The Roelcke-Selberg decomposition involves continuous spectrum (Maass forms), whose Hecke eigenvalues are constrained by the Selberg eigenvalue conjecture (lambda_1 >= 1/4), not by Deligne's theorem.

## Question 2: What is the precise obstruction?

**(e) All of the above, but with different severity at different levels.**

The five obstructions are:

**(a) Lack of Z-form:** For lattice VOAs, representation numbers r_Lambda(n) are integers. For irrational c, the primary-counting function involves non-integral powers. BYPASSED for rational VOAs (characters are VVMF on Gamma(4pq)). OPEN for irrational c.

**(b) Lack of Hecke action on the convolution algebra:** The Hecke operators T_p are analytic objects on M_{1,1}; the convolution algebra g^mod_A is algebraic. For lattice VOAs, the sewing differential factors through Theta_Lambda (a Hecke eigenform), so T_p extends. For non-lattice algebras, the commutator [d_sew, T_p] is the Hecke defect delta_p. NOT COMPUTED for any non-lattice, non-rational algebra.

**(c) Lack of Euler product at character level:** The partition function Dirichlet series is NOT multiplicative for rational CFTs (PROVED, 14 failures for Ising). RESOLVED: this is a projection artefact; individual L-function summands retain Euler products.

**(d) Quasi-modularity of characters:** The genus-1 propagator is E_2*(tau), which is quasi-modular, NOT holomorphic. The Fourier coefficients of (E_2*)^k are NOT multiplicative for k >= 2. This is the DEEPEST structural obstruction. Even if shadow coefficients S_r are tau-independent (hence trivially Hecke-equivariant), the shadow AMPLITUDES Sh_r^(1)(tau) acquire tau-dependence from the propagator, and this tau-dependence is quasi-modular.

**(e) Structural separation at genus 1:** PROVED (thm:structural-separation): the MC equation at genus 1 constrains MOMENTS of the spectral decomposition but cannot access INDIVIDUAL Hecke eigenvalues (which require analytic continuation to complex spectral parameter). This blocks the direct genus-1 approach but not prime-locality itself.

**The deepest obstruction is (d).** Even after resolving (a)-(c), the quasi-modularity of the propagator means that the graph-sum structure of shadow amplitudes is not automatically compatible with the Hecke algebra.

## Question 3: Does Route C actually work?

**PARTIALLY. The counting argument is correct, but the conclusion has a gap.**

Route C (thm:route-c-propagation) is logically sound at the **shadow coefficient level**:
- The MC recursion determines S_r from {S_2, S_3, S_4} (Riccati algebraicity).
- For algebraic families, S_r are tau-independent rational functions of c or k.
- T_p acts as identity on constants, so delta_p^{(r)} = 0 at the coefficient level.
- Corollary cor:route-c-standard-landscape correctly states prime-locality for the standard landscape at the coefficient level.

**The gap is between the coefficient level and the amplitude level:**

Issue 1: The MC recursion on shadow coefficients is a polynomial recursion among constants. The MC recursion on shadow amplitudes is a recursion among quasi-modular forms. These are different operations.

Issue 2: The proof asserts T_p(S_j) * T_p(P) appears in the recursion, but T_p is NOT a ring homomorphism on quasi-modular forms. So T_p(Sh_r^(1)) ≠ the graph sum with T_p applied to each factor.

**The counting argument does NOT break down because the MC recursion fails to give independent equations.** The recursion IS independent at each arity. The problem is that the recursion operates on tau-independent OPE data, while the prime-locality question concerns tau-dependent amplitudes. The overdetermination gives finite determination of the shadow obstruction tower (Riccati), which is algebraic prime-locality, not arithmetic prime-locality.

## Question 4: Is there a modified prime-locality that is true?

**YES: Riccati determinacy (algebraic prime-locality).**

The shadow obstruction tower IS finitely determined: all S_r are polynomials in (kappa, alpha, S_4). This follows from the Riccati algebraicity theorem: H(t) = t^2 sqrt(Q_L(t)) is algebraic of degree 2.

This IS true and IS nontrivial: an infinite tower of invariants is determined by exactly three parameters. It IS a form of prime-locality in the algebraic sense: the data at all arities factors through finitely many algebraic invariants.

It is NOT arithmetic prime-locality: it says nothing about Hecke eigenvalues or Euler products. The distinction is between determining the VERTEX WEIGHTS in the graph sum (which Riccati does) and determining the PROPAGATOR WEIGHTS (which carry the tau-dependence and the arithmetic content).

## Question 5: What is the honest status?

### PROVED:
1. Prime-locality for lattice VOAs (all ranks, all levels)
2. Prime-locality for rational VOAs with diagonal modular invariant
3. Prime-locality at shadow coefficient level for all algebraic families
4. Riccati determinacy (algebraic prime-locality)
5. Ramanujan bound for lattice and rational VOAs
6. Structural separation: genus-1 MC cannot access zeta zeros

### OPEN:
1. Prime-locality for irrational VOAs
2. Amplitude-level Hecke equivariance (graph sums vs Hecke operators)
3. Hecke defect computation for any non-lattice, non-rational algebra
4. Ramanujan for irrational VOAs (conditional on Langlands for Sym^r, r >= 5)

### STRUCTURALLY IMPOSSIBLE:
1. Zero-location from genus-1 MC (proved blocked)
2. Euler product for full partition function of non-lattice rational CFT (proved non-multiplicative)

### VERDICT:
Prime-locality is ALIVE for non-lattice algebras in the proved rational regime. For irrational algebras, the question reduces to a concrete problem in the Hecke theory of quasi-modular forms: does the graph-sum structure on M-bar_{1,r} with universal propagators inherit Hecke equivariance? This connects prime-locality to the Faber-Pandharipande programme. Closing the gap requires one of:
- (A) A vanishing theorem for H^1(g^mod_A, ad_{T_p})
- (B) Explicit computation of [delta_p] for Virasoro at generic c
- (C) A structural argument that tautological classes on M-bar_{1,r} are Hecke-equivariant

Option (C) is the most natural path forward.

## Files Modified

- Vol I: `chapters/connections/arithmetic_shadows.tex` (new section "The prime-locality assessment", ~300 lines)
- Vol II: `chapters/connections/thqg_fredholm_partition_functions.tex` (new subsection "Prime-locality and quantum gravity", ~150 lines)
- This file: `compute/audit/prime_locality/synthesis.md`
