# Zhu's Algebra, the Primary Spectrum, and the Constrained Epstein Zeta

## Date: 2026-04-01
## Status: Research audit (independent verification from first principles)
## Sources: Zhu96, BenjaminChang22, virasoro_bar_zhu.py, virasoro_constrained_epstein.py, koszul_epstein/benjamin_chang.md

---

## 0. Summary of Findings

1. Zhu's algebra A(V) captures the full primary spectrum via Zhu's theorem (bijection between irreps of V and simple modules of A(V)), but NOT the quasi-primary multiplicities d(h) within the vacuum module. The constrained Epstein sums over quasi-primaries of the vacuum module, not over primaries of all modules. These are different objects.

2. For A(V) = C[x] (universal Virasoro at generic c): the "zeta function" is NOT 2^{-s} zeta(s). The primaries of the universal Virasoro are labeled by h in C (one irrep V_h for each h), but the constrained Epstein sums over the VACUUM MODULE's internal quasi-primary decomposition, which is a combinatorial invariant d(h) = p_{>=2}(h) - p_{>=2}(h-1).

3. The quasi-primary count d(h) is NOT Ext^0_{A(V)}(C_h, C_0). It is dim ker(L_1: V_h -> V_{h-1}) in the vacuum module, which is a statement about the INTERNAL structure of a single A(V)-module, not about morphisms between modules.

4. The A-infinity structure on the derived Zhu algebra constrains bar cohomology but does NOT directly constrain the constrained Epstein series. The spectral zeta is about representation-theoretic data; the bar complex is about deformation-theoretic data. These are related through the shadow obstruction tower but live at different levels.

---

## 1. Does Zhu's Algebra Capture the Full Primary Spectrum?

### The theorem (Zhu 1996, Theorem 2.2.2)

**Zhu's theorem**: Let V be a vertex operator algebra satisfying standard positivity conditions. There is a bijection

    {isomorphism classes of irreducible positive-energy V-modules}  <--->  {isomorphism classes of simple A(V)-modules}

given by M |-> Omega(M) = M(0) (the weight-0 subspace, a.k.a. the lowest weight space).

**Answer to the headline question**: YES, Zhu's algebra captures the full primary spectrum in the sense that the SET of primary dimensions {Delta_i} bijects with Spec(A(V)) (the spectrum of the algebra A(V), i.e., the set of simple modules).

### Case analysis

**Rational VOAs** (minimal models, WZW at positive integer level, lattice VOAs):

A(V) is finite-dimensional semisimple. The simple modules of a finite-dimensional semisimple algebra over C are exactly the simple summands:

    A(V) = End(M_1^{(0)}) x ... x End(M_N^{(0)})

where M_1, ..., M_N are the finitely many irreducible V-modules and M_i^{(0)} is the lowest weight space. The primary dimensions Delta_1, ..., Delta_N are the eigenvalues of the image of omega in A(V) (where omega is the conformal vector).

For the Ising model c = 1/2: A(L(1/2, 0)) has 3 simple modules corresponding to h = 0, 1/16, 1/2. Dimension 3 as a vector space (each lowest weight space is 1-dimensional).

**Irrational VOAs** (universal Virasoro at generic c):

A(V_c) = C[x] (polynomial ring, x = [omega]). This is NOT semisimple. The simple modules of C[x] are the one-dimensional modules C_h where x acts as h, for each h in C. The irreducible V_c-modules are the Verma modules M(c, h) for each h in C (at generic c, all Verma modules are irreducible). So:

    Spec(A(V_c)) = C

which IS the "primary spectrum" (one module for each conformal weight h in C).

### The critical distinction: spectrum of A(V) vs quasi-primary spectrum of V itself

The constrained Epstein zeta as defined in virasoro_constrained_epstein.py is

    epsilon^c_s(Vir) = sum_{h >= 2} d(h) (2h)^{-s}

where d(h) is the number of quasi-primary states at weight h IN THE VACUUM MODULE V_c. This is the dimension of ker(L_1) in the weight-h subspace of V_c.

This is NOT the same as summing over Spec(A(V)). The spectrum of A(V) = C[x] is the set of all h in C (with multiplicity 1 each). If one were to form a zeta function from Spec(A(V)):

    zeta_{Spec}(s) = sum_{h in Spec, h > 0} (2h)^{-s}

this would be a sum over a CONTINUOUS set (or over all positive integers, if restricted to the physical spectrum h in Z_{>0}), which is nonsensical without a measure.

The quasi-primary count d(h) is data INTERNAL to a single A(V)-module (the vacuum module M(c,0)), not data about the module category of A(V).

---

## 2. Is epsilon^c_s = 2^{-s} zeta(s) for A(V) = C[x]?

### The claim to test

For A(V) = C[x], the evaluation modules are C_h for h = 0, 1, 2, 3, ... (restricting to non-negative integers for the physical spectrum). The "zeta function" would be

    sum_{h >= 1} (2h)^{-s} = 2^{-s} sum_{h >= 1} h^{-s} = 2^{-s} zeta(s)

### Verdict: FALSE (wrong object)

This sum over h = 1, 2, 3, ... counts the number of MODULES of A(V) with given integer weight, with multiplicity 1 per weight. But the constrained Epstein uses the QUASI-PRIMARY COUNT d(h) as multiplicity:

    epsilon^c_s = sum_{h >= 2} d(h) (2h)^{-s}

where d(h) = p_{>=2}(h) - p_{>=2}(h-1) (a rapidly growing function of h).

The first few values:

| h  | d(h) | p_{>=2}(h) |
|----|------|------------|
| 2  | 1    | 1          |
| 3  | 0    | 1          |
| 4  | 1    | 2          |
| 5  | 0    | 2          |
| 6  | 2    | 4          |
| 7  | 0    | 4          |
| 8  | 3    | 7          |
| 9  | 1    | 8          |
| 10 | 4    | 12         |
| 11 | 2    | 14         |
| 12 | 7    | 21         |

So d(3) = 0, d(5) = 0, d(7) = 0: at odd weights below 9, there are NO quasi-primaries beyond descendants. The vanishing at h = 3, 5, 7 comes from the fact that L_1: V_h -> V_{h-1} is an isomorphism at these weights (the source and target have the same dimension p_{>=2}(h) = p_{>=2}(h-1)).

The "naive" zeta function 2^{-s} zeta(s) would give every positive integer weight multiplicity 1. The actual constrained Epstein has multiplicities growing like exp(pi sqrt(2h/3)) / (2 sqrt(h)), which makes the series DIVERGE for all s.

### The deeper error

Even for A(V) = C[x], asking "what is the zeta function of C[x]?" is ill-posed. Zeta functions of algebras are typically defined for algebras over Z or for orders in number fields (e.g., the Solomon zeta function sum_{I} [A:I]^{-s} over ideals of finite index). For C[x]:

- The ideal zeta function: C[x] has ideals (x - a) for each a in C. These all have "index" 1 (as C-vector spaces, C[x]/(x-a) = C). So the ideal zeta is just the counting function of C, which is not a Dirichlet series.

- The representation zeta function: sum over irreps M_i of dim(M_i)^{-s} = sum_h 1^{-s} = infinity (all irreps are 1-dimensional). Not useful.

Neither of these recovers the constrained Epstein. The constrained Epstein is sui generis: it is a Dirichlet series built from the INTERNAL DECOMPOSITION of a specific module (the vacuum) under a specific operator (L_1).

---

## 3. Is d(h) an Ext functor?

### The claim to test

Is d(h) = dim Ext^0_{A(V)}(C_h, C_0)?

### Computation

For A = C[x], the simple modules are C_a (x acts by a) for a in C.

    Ext^0_{C[x]}(C_h, C_0) = Hom_{C[x]}(C_h, C_0)

A module map f: C_h -> C_0 satisfies f(x . v) = x . f(v), i.e., h f(v) = 0 . f(v) = 0. So:
- If h != 0: f = 0. dim Ext^0 = 0.
- If h = 0: f is any C-linear map C -> C. dim Ext^0 = 1.

So dim Ext^0_{C[x]}(C_h, C_0) = delta_{h,0}, which is NOTHING like d(h).

### Higher Ext

    Ext^n_{C[x]}(C_h, C_0) for the Koszul resolution:

The resolution of C_h over C[x]:
    0 -> C[x] ---(x-h)---> C[x] -> C_h -> 0

Applying Hom(-, C_0):
    0 -> Hom(C[x], C_0) ---(x-h)*---> Hom(C[x], C_0) -> 0

which is
    0 -> C_0 ---(-h)---> C_0 -> 0

So:
- Ext^0 = ker(-h) = {0 if h != 0, C if h = 0}
- Ext^1 = coker(-h) = {0 if h != 0, C if h = 0}

For h != 0: Ext^n(C_h, C_0) = 0 for all n.
For h = 0: Ext^n(C_0, C_0) = C for n = 0, 1 and 0 for n >= 2.

### Verdict: FALSE

d(h) is NOT any standard Ext functor of modules over Zhu's algebra. The quasi-primary count is a property of the VACUUM MODULE's internal structure (ker L_1), not of the module category of A(V).

### What d(h) actually is

d(h) = dim ker(L_1|_{V_h}) where V_h is the weight-h subspace of the vacuum module V_c. This is the dimension of the kernel of a LINEAR MAP between finite-dimensional vector spaces:

    L_1: (V_c)_h -> (V_c)_{h-1}

where dim(V_c)_h = p_{>=2}(h) (partitions of h into parts >= 2).

By rank-nullity:
    d(h) = dim ker L_1|_h = dim(V_c)_h - rank(L_1|_h) = p_{>=2}(h) - p_{>=2}(h-1)

(at generic c, L_1 is surjective: rank = dim target = p_{>=2}(h-1)). This is verified in virasoro_constrained_epstein.py through h = 14 by explicit matrix computation.

The correct homological interpretation of d(h) is:

    d(h) = dim H^0(n_+, (V_c)_h) = dim ((V_c)_h)^{n_+}

where n_+ = span{L_1, L_2, ...} is the positive-mode subalgebra. A quasi-primary at weight h is an L_1-highest weight state (annihilated by L_1 but not necessarily by higher L_n). For the Virasoro algebra, L_1-annihilation at generic c is sufficient for quasi-primarity because:

    ker(L_1) cap ker(L_2) cap ... = ker(L_1)    (at generic c in the vacuum module)

This is NOT true at special c values or in non-vacuum modules.

---

## 4. Can the A-infinity Structure on the Derived Zhu Algebra Constrain the Spectral Zeta?

### Background

Zhu's algebra A(V) is the zeroth page of a filtration on V. The higher Zhu algebras A_n(V) (Dong-Li-Mason, Miyamoto) control n-th level representation theory. The bar complex B(V) maps to B(A(V)) via the Zhu functor.

The derived Zhu algebra is the object obtained by taking the full derived functor of the Zhu reduction. For the universal Virasoro:

    A(V_c) = C[x]    (Koszul, Ext concentrated in degrees 0-1)

The A-infinity structure on the derived category is trivial (C[x] is formal = its A-infinity structure is quasi-isomorphic to one with m_n = 0 for n >= 3).

### Analysis

The A-infinity structure on the derived Zhu algebra constrains the BAR COHOMOLOGY H*(B(V)), which is the deformation-theoretic object (the Koszul dual coalgebra). The spectral zeta epsilon^c_s is the representation-theoretic object (the primary spectrum).

These live at different levels:

    A-infinity on derived Zhu  ----controls---->  bar cohomology H*(B(V))
                                                         |
                                                    (Koszul duality)
                                                         |
                                                         v
                                                   Koszul dual A^!
                                                         |
                                                    (representation theory)
                                                         |
                                                         v
                                                  primary spectrum of A^!

The A-infinity structure on the derived Zhu algebra constrains the bar cohomology of V, which gives the Koszul dual A^! = V^!. The primary spectrum of A^! is Spec(A(V^!)), which for Virasoro at central charge c is Spec(A(V_{26-c})) = C.

But this is the primary spectrum of the KOSZUL DUAL, not of V itself. The constrained Epstein epsilon^c_s(Vir) uses the quasi-primary spectrum of V (= V_c), not the primary spectrum of V^! (= V_{26-c}).

### What IS constrained

The A-infinity structure constrains the SHADOW TOWER invariants (kappa, alpha, S_4, S_5, ...) through the bar MC element Theta_A. The shadow obstruction tower invariants are the Taylor coefficients of the generating function H(t) = sum S_r t^r where H^2 = t^4 Q_L(t) (Riccati algebraicity, thm:riccati-algebraicity).

The shadow metric Q_L determines the shadow Epstein zeta epsilon_{Q_L}(s), which IS constrained by the A-infinity/bar structure. But this is the SHADOW METRIC Epstein (Object B in benjamin_chang.md), not the constrained Epstein of the primary spectrum (Object A).

### The chain of constraints

    A-inf on derived Zhu  --->  bar cohomology  --->  Theta_A (MC element)
                                                          |
                                                     (arity projections)
                                                          |
                                                          v
                                                   kappa, alpha, S_4, ...
                                                          |
                                                     (shadow metric)
                                                          |
                                                          v
                                                   epsilon_{Q_L}(s) (Object B)

But:

    primary spectrum {h_i}  --->  epsilon^c_s (Object A)

The two objects are related through the Rankin-Selberg transform on M_{1,1} (the spectral decomposition of the partition function), but this relationship goes through the FULL partition function (not just the vacuum module or the bar complex). The A-infinity structure constrains Object B, not Object A.

### Verdict: INDIRECT constraint only

The A-infinity structure on the derived Zhu algebra constrains the shadow metric Epstein zeta (Object B) through the MC element Theta_A and its shadow projections. It does NOT directly constrain the constrained Epstein of the primary spectrum (Object A). The two are related through Rankin-Selberg on M_{1,1}, but this is a deep analytic relationship, not a direct algebraic one.

For lattice VOAs (where the shadow obstruction tower terminates), the shadow metric Epstein and the constrained Epstein are closely related (both factor through the theta function), and the A-infinity constraints propagate. For Virasoro at generic c (where the shadow obstruction tower is infinite and the constrained Epstein diverges), the constraints are much weaker and the relationship is open.

---

## 5. The Honest Summary Table

| Question | Answer | Reasoning |
|----------|--------|-----------|
| Does Zhu's algebra capture the full primary spectrum? | YES (via Zhu's theorem) | Bijection: irreps of V <-> simple modules of A(V) |
| Is epsilon^c_s the zeta function of A(V) = C[x]? | NO | epsilon^c_s uses quasi-primary multiplicities d(h) in the vacuum module, not the module count of A(V) |
| For A(V) = C[x], is "the zeta function" 2^{-s} zeta(s)? | ILL-POSED | C[x] does not have a natural Dirichlet series attached to its module spectrum over C |
| Is d(h) = Ext^0_{A(V)}(C_h, C_0)? | NO | Ext^0(C_h, C_0) = delta_{h,0}. d(h) = dim ker(L_1\|_h) = p_{>=2}(h) - p_{>=2}(h-1) |
| What is d(h) homologically? | H^0(n_+, V_h) | Zeroth Lie algebra cohomology of the positive-mode subalgebra with coefficients in V_h |
| Can A-inf on derived Zhu constrain epsilon^c_s? | INDIRECTLY | A-inf constrains shadow metric Epstein (Object B) via Theta_A. Relationship to constrained Epstein (Object A) goes through Rankin-Selberg on M_{1,1} |
| Does the c-independence of d(h) have homotopical meaning? | YES | d(h) is c-independent because L_1 has integer entries (no central extension on negative modes). This is the algebraic shadow of PBW degeneration: the E_2 page of the PBW spectral sequence is c-independent |

---

## 6. The Three Objects and Their Correct Homes

### Object A: Constrained Epstein epsilon^c_s(Vir)

- **Definition**: sum_{h >= 2} d(h) (2h)^{-s}
- **Input**: quasi-primary multiplicities d(h) = p_{>=2}(h) - p_{>=2}(h-1) (COMBINATORIAL, c-independent at generic c)
- **Convergence**: DIVERGES for all s (growth exp(C sqrt(h)), C = pi sqrt(2/3))
- **Home**: representation theory of the Virasoro algebra (internal decomposition of the vacuum module under L_1)
- **Zhu connection**: d(h) is NOT an Ext of A(V); it is dim ker(L_1|_h) = H^0(n_+, V_h)
- **Computed in**: virasoro_constrained_epstein.py (truncated partial sums)

### Object B: Shadow metric Epstein epsilon_{Q_L}(s)

- **Definition**: sum'_{(m,n) in Z^2} Q_L(m,n)^{-s}
- **Input**: shadow obstruction tower invariants kappa, alpha, S_4 (c-DEPENDENT, from OPE)
- **Convergence**: CONVERGES for Re(s) > 1 (positive definite binary form for c > 0)
- **Home**: deformation theory / bar-cobar duality (MC element Theta_A projections)
- **Zhu connection**: constrained by A-inf structure through Theta_A
- **Computed in**: koszul_epstein.py, shadow_epstein_zeta.py

### Object C: Benjamin-Chang spectral function E^c_s

- **Definition**: Eisenstein spectral coefficient of the Roelcke-Selberg decomposition of the full partition function Z(tau, tau_bar) on M_{1,1}
- **Input**: FULL partition function of a specific 2d CFT at central charge c
- **Convergence**: well-defined as a spectral measure (tempered distribution)
- **Home**: spectral theory on the modular surface SL(2,Z)\H
- **Zhu connection**: the primary spectrum that enters is Spec(A(V)) (via Zhu's theorem), but the multiplicities come from the full modular-invariant partition function, not from a single module
- **Computed in**: benjamin_chang.md (analytic description only)

### The chain of projections (from benjamin_chang.md, verified)

    Full CFT data  ---(primary spectrum)--->  E^c_s (Object C)
                                                 |
                                            (low moments)
                                                 |
                                                 v
                                           epsilon_{Q_L}(s) (Object B)
                                                 |
                                            (Taylor coefficients)
                                                 |
                                                 v
                                           Z_{sh}(s, c) (shadow obstruction tower zeta)

Object A (constrained Epstein of the vacuum module) sits OUTSIDE this chain: it uses the vacuum module's internal structure (d(h)), not the primary spectrum across all modules.

---

## 7. What the Bar Complex DOES Constrain

The bar complex B(V) and its cohomology H*(B(V)) = V^! (the Koszul dual) constrain:

1. **The Koszul dual algebra**: V^! = Vir_{26-c} for the Virasoro. Its primary spectrum is the same continuous set C, but with DIFFERENT OPE coefficients (c -> 26-c).

2. **The shadow obstruction tower**: The MC element Theta_A = D_A - d_0 in the modular convolution algebra determines all shadow invariants kappa(A), alpha(A), S_r(A) for r >= 4. These are the TAYLOR COEFFICIENTS of the algebraic shadow generating function H(t)^2 = t^4 Q_L(t).

3. **The shadow metric Epstein**: Through the shadow invariants, the bar complex determines epsilon_{Q_L}(s) (Object B), which has a genuine functional equation (Epstein 1903) and arithmetic content (factoring through Dirichlet L-functions when the discriminant is fundamental).

4. **The genus expansion**: F_g(A) = kappa(A) * lambda_g^{FP} at all genera on the uniform-weight lane (Theorem D). This is a SINGLE SCALAR (kappa) determining the entire genus tower.

The bar complex does NOT directly constrain:
- The quasi-primary multiplicities d(h) (these are representation-theoretic, not deformation-theoretic)
- The convergence properties of the constrained Epstein (Object A)
- The spectral decomposition on M_{1,1} (this requires the full partition function, not just the bar complex)

---

## 8. Verification Against Existing Code

### Cross-check 1: d(h) values (virasoro_constrained_epstein.py)

The quasi_primary_count(h) function computes d(h) = p_{>=2}(h) - p_{>=2}(h-1). Verified:

    d(2) = 1, d(4) = 1, d(6) = 2, d(8) = 3, d(10) = 4, d(12) = 7

These match the documented values and are c-independent (integer matrix rank argument).

### Cross-check 2: Zhu Ext (virasoro_bar_zhu.py)

The ZhuAlgebra class computes:
- Universal A(V_c) = C[x]: Ext^0 = 1, Ext^1 = 1, Ext^n = 0 for n >= 2 (Koszul)
- Simple A(L(c,0)): Ext^0 = 1, Ext^n = 0 for n >= 1 (semisimple)

Verified: these are correct for C[x] and for finite-dimensional semisimple algebras.

### Cross-check 3: Convergence (virasoro_constrained_epstein.py)

The convergence_analysis() function correctly identifies:
- Abscissa of convergence = +infinity (series diverges for all s)
- Growth rate C = pi sqrt(2/3) approx 2.565
- d(h) grows as exp(C sqrt(h)) / (2 sqrt(h))

This is mathematically correct: the Dirichlet series with coefficients growing as exp(C sqrt(h)) has infinite abscissa.

### Cross-check 4: Benjamin-Chang comparison (benjamin_chang.md)

The audit document correctly distinguishes Objects A, B, C and identifies:
- The pole at s = c/2 in the BC functional equation coincides with kappa only for Virasoro (not for general algebras) -- AP1 awareness
- The shadow metric Epstein and the constrained Epstein are fundamentally different objects
- Five false ideas correctly dismissed

---

## 9. Open Questions (refined)

1. **Regularization of Object A**: The constrained Epstein diverges for all s. What is the correct regularization? The partial sums are well-defined finite Dirichlet polynomials. Borel summation, zeta regularization, or spectral regularization (treating d(h) as a spectral density and using the Rankin-Selberg transform) are candidates. The c-independence of d(h) at generic c suggests a topological/combinatorial regularization may exist.

2. **Higher Zhu algebras and the constrained Epstein**: The higher Zhu algebras A_n(V) (Dong-Li-Mason) control the representation theory at higher levels. Do the Ext groups of A_n(V) constrain d(h) at weight h = n + 2? Specifically:

       d(h) =? dim H^0(n_+, V_h) =? some derived functor of higher Zhu data

   This is a genuine open question. The answer would connect the combinatorial d(h) to the algebraic Zhu hierarchy.

3. **Homotopy-theoretic meaning of c-independence**: The c-independence of d(h) at generic c follows from the integrality of the L_1 matrix. Homotopy-theoretically, this means the E_2 page of the PBW spectral sequence (which computes bar cohomology) is c-independent. But the constrained Epstein uses d(h) (quasi-primary counts), not dim H^n(B(V)) (bar Betti numbers). Is there a spectral sequence connecting d(h) to bar cohomology?

   The answer is partially affirmative: the bar complex at bar degree 1 has H^1(B(V)) = V^!_1 (the weight-1 part of the Koszul dual), and dim(V^!_h) = d(h) by the Koszul duality V^! = H*(B(V)). So d(h) IS a bar cohomology dimension -- it is the bar degree 1, weight h piece. The full bar cohomology has higher bar degrees as well.

   Correction: This identification requires care. H^1(B(V))_h = ker(d: B^1_h -> B^0_h) / im(d: B^2_h -> B^1_h). The kernel of d on B^1 consists of elements that are cocycles under the bar differential. For the Virasoro, the bar differential on B^1 extracts OPE poles (weight-lowering). The quasi-primaries (ker L_1) are related but not identical to bar 1-cocycles.

   STATUS: The precise relationship between d(h) and H^1(B(V))_h is a subtle question that depends on the filtration conventions. At the E_2 level of the PBW spectral sequence, they coincide. At the full cohomology level, corrections from higher filtration stages may enter. This is verified in virasoro_bar_zhu.py's discussion of the weight filtration (lines 1096-1133).

4. **Non-vacuum modules**: The constrained Epstein as defined uses only the vacuum module. For a FULL CFT, one would sum over primaries of ALL modules (as in the Benjamin-Chang construction). Can the bar complex of V constrain the primary content of non-vacuum modules? This is related to the Swiss-cheese structure (Vol II) and the open/closed MC element Theta^{oc}.

---

## 10. The Structural Answer

The constrained Epstein zeta epsilon^c_s is the spectral zeta function of the VACUUM MODULE's quasi-primary decomposition. Zhu's algebra A(V) captures the primary spectrum (set of modules), not the quasi-primary multiplicities (internal decomposition of a single module). The A-infinity structure on the derived Zhu algebra constrains the bar complex and hence the shadow metric Epstein (Object B), but not directly the constrained Epstein (Object A).

The correct chain of mathematical relationships is:

    Zhu's algebra A(V)
         |
         |--- (simple modules) ---> primary spectrum {h_i} ---> (sum) ---> Object C (BC)
         |
         |--- (Koszulity of A(V)) ---> bar cohomology H*(B(V)) = V^!
         |                                    |
         |                                    |--- (MC element) ---> Theta_A ---> shadow invariants
         |                                    |                                        |
         |                                    |                                   Object B (shadow Epstein)
         |                                    |
         |                                    |--- (bar degree 1) ---> H^1(B) ~ quasi-primaries (at E_2)
         |
         |--- (ker L_1 in vacuum module) ---> d(h) ---> Object A (constrained Epstein)

The key insight: d(h) appears BOTH as a representation-theoretic invariant (ker L_1) AND as a deformation-theoretic invariant (bar degree 1 cohomology at the E_2 level). But these are related by the PBW degeneration, not by Zhu's algebra directly. The A-infinity structure enters through the bar complex, not through the module category.
