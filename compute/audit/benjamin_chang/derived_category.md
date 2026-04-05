# Can the Derived Category of V-modules Capture the Benjamin-Chang Spectral Zeta?

## Date: 2026-04-01
## Status: Research investigation
## Sources: benjamin_chang.md, arithmetic_shadows.tex, chiral_hochschild_koszul.tex, minimal_model_fusion.tex, thqg_open_closed_realization.tex

---

## 0. Summary of Conclusions

The short answer is: **partially yes for rational VOAs, structurally no for irrational ones, and the manuscript's own ChirHoch* captures something genuinely different from the primary spectrum.**

More precisely:

1. K_0(V-mod) sees the primary spectrum as a SET (with multiplicities) but does NOT naturally produce the Dirichlet series epsilon^c_s. The Dirichlet series requires METRIC data (conformal dimensions) that K_0 does not carry.

2. HH_*(V-mod) is the correct "character ring" in the categorical sense, but for V-mod as a MODULE CATEGORY, not as a bare abelian category. The annulus trace theorem (thm:thqg-annulus-trace) already identifies this: HH_*(M) = integral_{S^1} M. This recovers the character-valued trace, not the spectral zeta.

3. ChirHoch*(V) (Theorem H) sees the DEFORMATION THEORY, not the representation theory. It is concentrated in degrees {0,1,2} with polynomial growth. It does NOT see the primary spectrum directly; it sees the center Z(A) = ChirHoch^0 and the obstruction space ChirHoch^2 = Z(A!)^v. These are algebraic invariants of the algebra itself, not of its module category.

4. For continuous spectra (Virasoro at generic c), K-theory of the naive module category is meaningless (K_0 = 0 or ill-defined). The correct framework is the SPECTRAL DECOMPOSITION on the moduli space M_{1,1} (Roelcke-Selberg), which is a different object entirely.

---

## 1. K_0(V-mod) and the Primary Spectrum

### 1.1 Rational case

For a rational VOA V (C_2-cofinite, with finitely many simple modules L_0, ..., L_{r-1}):

- K_0(V-mod) = Z^r as a free abelian group, with basis [L_i].
- The fusion product gives K_0 a RING structure: [L_i] * [L_j] = sum_k N_{ij}^k [L_k].
- This is the Grothendieck ring, computed explicitly for minimal models in minimal_model_fusion.tex (def:grothendieck-w3, thm:grothendieck-structure).

The Benjamin-Chang spectral zeta is:

  epsilon^c_s = sum_{Delta in S} (2*Delta)^{-s}

where S is the multiset of scalar primary dimensions. In K-theoretic language, this is:

  epsilon^c_s = sum_i m_i * (2*h_i)^{-s}

where h_i is the conformal dimension of L_i and m_i is its multiplicity in the partition function.

**Can K_0 produce this?** Only with ADDITIONAL structure:

(a) K_0 knows the CLASSES [L_i] but not their conformal dimensions h_i. The dimensions h_i are eigenvalues of the L_0 operator, which is extra data beyond K_0.

(b) The multiplicities m_i come from the partition function Z(tau, bar{tau}), which encodes the MODULAR INVARIANT (the choice of how to pair holomorphic and antiholomorphic sectors). K_0 does not know this pairing.

(c) To form epsilon^c_s, one needs: (i) the set of simple objects (from K_0), (ii) their conformal dimensions (from L_0 eigenvalues), (iii) their multiplicities in the physical partition function (from the modular invariant). K_0 provides only (i).

**Enriched K-theory.** If one considers K_0 with the FILTRATION by conformal dimension (the weight grading), then K_0^{fil}(V-mod) = sum_h Z * delta_h recovers the spectrum with multiplicities. This is essentially the CHARACTER: K_0^{fil} = Z[[q]] via [L_i] -> chi_i(q) = tr_{L_i}(q^{L_0 - c/24}). The spectral zeta is then a MELLIN TRANSFORM of the character data. But this requires the weight grading, which is extra structure beyond K_0.

### 1.2 Irrational case (Virasoro at generic c)

For the Virasoro algebra at generic (irrational) c, the representation theory is drastically different:

- There are UNCOUNTABLY many simple highest-weight modules L(c,h), one for each h in C (at generic c, all Verma modules are irreducible).
- The "primary spectrum" is a CONTINUOUS family parametrized by h.
- K_0 of the category of all highest-weight modules is not a finitely generated group; it is an uncountable free abelian group (one generator per h in C), which carries no useful topology.

The Benjamin-Chang spectral zeta in this regime:

  epsilon^c_s = sum_{Delta in S} (2*Delta)^{-s}

where S is the set of scalar primary dimensions appearing in the actual physical partition function. For a physical CFT, this is a discrete (but typically infinite) multiset. However, for the ALGEBRAIC category of Virasoro modules at generic c, there is no canonical partition function and no canonical discrete spectrum.

**The structural gap:** K_0 of a category with continuous simple objects does not produce a Dirichlet series. A Dirichlet series requires a DISCRETE spectrum with a growth condition. The passage from continuous representation theory to a discrete spectrum requires:

(a) choosing a specific theory (a modular invariant), or
(b) passing to the SPECTRAL DECOMPOSITION on the modular curve SL(2,Z) \ H (the Roelcke-Selberg decomposition), which produces a continuous spectral measure plus a discrete cuspidal part.

This is precisely the Benjamin-Chang construction: they do NOT start from K_0. They start from the partition function Z(tau, bar{tau}), strip descendants to get Z-hat^c, and decompose on the modular curve. The spectral parameter s in epsilon^c_s is the EISENSTEIN spectral parameter on SL(2,Z) \ H, not a K-theoretic invariant.

### 1.3 Verdict on Question 1

**epsilon^c_s is NOT naturally a K-theoretic invariant.** It requires:
- for rational VOAs: K_0 + weight grading + modular invariant
- for irrational VOAs: the spectral decomposition on the modular curve, which is a fundamentally analytic (not algebraic) construction

The correct analogy with algebraic geometry is NOT:

  K_0(Coh(X)) -> zeta_X(s)    (WRONG analogy)

but rather:

  H^*(X_et, Q_l) with Frobenius action -> zeta_X(s)    (CORRECT analogy for rational)
  Spectral decomposition on Spec(Z) -> L(s, f)          (CORRECT analogy for irrational)

For rational VOAs, the S-matrix plays the role of Frobenius: its eigenvalues (the quantum dimensions d_i = S_{0i}/S_{00}) control the asymptotic growth of the partition function, just as Frobenius eigenvalues control point counts. The Verlinde formula N_{ij}^k = sum S_{il} S_{jl} S_{kl}*/S_{0l} is analogous to the Lefschetz trace formula.

---

## 2. Hochschild Homology of V-mod

### 2.1 The annulus trace theorem

The manuscript proves (thm:thqg-annulus-trace, in thqg_open_closed_realization.tex):

  integral_{S^1} M  ~=  HH_*(M)

where M is the boundary category (an E_1-category). In a chart M = Perf(A_b):

  HH_*(A_b) = H_*(B^{cyc}(A_b), d_{cyc})

This is the cyclic bar complex of the boundary algebra. The proof uses Ayala-Francis excision: factorization homology over S^1 = Hochschild homology.

### 2.2 What HH_* encodes

For V-mod as a monoidal category (with the fusion tensor product for rational V):

  HH_0(V-mod) = the space of "characters" = the space of traces on the fusion category.

For a semisimple fusion category with simples L_0, ..., L_{r-1}:

  HH_0(V-mod) = C^r (one trace per simple object)

This is the SPACE of characters chi_i(tau), not the spectral zeta. To get epsilon^c_s from the characters, one needs:
1. the modular S-matrix (to define the primary-counting function Z-hat^c)
2. the Roelcke-Selberg decomposition on the modular curve (an analytic operation)

**HH_* carries the CHARACTER RING, not the spectral zeta.** The characters chi_i(tau) are the INPUT to the Benjamin-Chang construction; the spectral zeta epsilon^c_s is the OUTPUT. The passage from characters to spectral zeta requires spectral analysis on the modular curve, which is NOT a categorical operation.

### 2.3 Higher Hochschild homology

For a modular tensor category C (which V-mod is for rational V):

  HH_n(C) for n >= 1 encodes the higher-genus modular data.

Specifically, HH_1 carries the Connes B-operator (the "modular derivative") and HH_2 carries the genus-2 data. The FULL HH_* package determines the 3d TQFT Z_C (by the Reshetikhin-Turaev construction, thm:mtc-tqft). But the 3d TQFT is a TOPOLOGICAL invariant, and the spectral zeta is an ANALYTIC invariant (it depends on the conformal structure of the modular curve, not just its topology).

### 2.4 The derived category D^b(V-mod)

For rational V, D^b(V-mod) is the bounded derived category of the (semisimple) fusion category. Since V-mod is semisimple:

  D^b(V-mod) = V-mod (no higher Ext)

So the derived category adds nothing for rational VOAs with semisimple module categories.

For NON-semisimple VOAs (logarithmic CFT, admissible-level quotients, triplet algebras):

  D^b(V-mod) is genuinely richer: Ext^n(L_i, L_j) != 0 for n > 0.

In this case, K_0(D^b(V-mod)) = K_0(V-mod) (Euler characteristic property), but the DERIVED structure (the Ext groups) carries finer information. Whether this finer information connects to the spectral zeta is OPEN and likely involves the relationship between logarithmic characters and mock modular forms.

---

## 3. Chiral Hochschild Cohomology (Theorem H)

### 3.1 What ChirHoch* sees

From chiral_hochschild_koszul.tex, Theorem H has two clauses:

(a) **Koszul duality**: ChirHoch^n(A) = ChirHoch^{2-n}(A!)^v tensor omega_X on the Koszul locus.

(b) **Polynomial growth**: ChirHoch^n(A) = 0 for n not in {0, 1, 2}. The Hochschild-Hilbert series is:

  P_A(t) = dim Z(A) + dim ChirHoch^1(A) * t + dim Z(A!) * t^2

### 3.2 Relationship to the primary spectrum

ChirHoch^0(A) = Z(A), the CENTER of A. For a VOA V:
- Z(V) = the space of SINGULAR VECTORS in V itself (not in the module category)
- For Virasoro at generic c: Z(Vir_c) = C (the vacuum is the only singular vector)
- For rational minimal models: Z(L(c,0)) = C (the simple quotient has trivial center)
- For W-algebras: Z(W^k(g)) may be larger (the Feigin-Frenkel center at critical level is infinite-dimensional)

ChirHoch^2(A) = Z(A!)^v = obstructions to deforming A. This encodes the TANGENT SPACE to the moduli of chiral algebras at A, not the representation theory of A.

ChirHoch^1(A) = the first-order deformations / infinitesimal automorphisms. For Virasoro: ChirHoch^1(Vir_c) = C (the one-parameter family in c).

**ChirHoch* does NOT see the primary spectrum.** It sees the INTRINSIC algebraic structure of A: its center, deformations, and obstructions. The primary spectrum is a property of the MODULE CATEGORY V-mod, which is a different object.

### 3.3 What ChirHoch* DOES connect to

The chiral Hochschild complex IS the tangent complex to the MC moduli MC(g^mod_A)/gauge at the universal class Theta_A (lines 28-31 of chiral_hochschild_koszul.tex). So:

  ChirHoch* controls DEFORMATIONS of Theta_A, not representations of V.

The connection to the spectral zeta is therefore:
- ChirHoch* controls the LOCAL geometry of the space of chiral algebras near A.
- The spectral zeta epsilon^c_s is a GLOBAL invariant of the representation theory at a single point of that moduli space.
- These are orthogonal: one is tangent (deformation), the other is spectral (representation).

### 3.4 The deeper connection: shadow obstruction tower as mediator

The shadow obstruction tower Theta_A (which ChirHoch* is tangent to) DOES connect to the spectral zeta through the ARITHMETIC SHADOWS chapter:

  Theta_A -> {S_r(A)} (shadow coefficients) -> Q_L (shadow metric) -> epsilon_{Q_L}(s) (shadow-metric Epstein)

and separately:

  V-mod -> {Delta_i} (primary spectrum) -> epsilon^c_s (Benjamin-Chang spectral zeta)

The shadow-spectral correspondence (thm:shadow-spectral-correspondence) relates these two chains for lattice VOAs. But the connection goes through the partition function and modular invariance, not through K-theory or HH_*.

---

## 4. The Correct Analogy with Algebraic Geometry

### 4.1 The Weil conjectures analogy

For a variety X over F_q:

  zeta_X(s) = exp(sum_{n>=1} |X(F_{q^n})| * q^{-ns} / n)
            = prod_i det(1 - q^{-s} * Frob | H^i(X, Q_l))^{(-1)^{i+1}}

The passage is:  point-counting -> etale cohomology -> L-function.

For a VOA V:

  epsilon^c_s = sum_Delta (2*Delta)^{-s}

The proposed analogy would be:

  "primary-counting" -> some cohomology theory -> L-function

### 4.2 What plays the role of Frobenius?

The MODULAR S-MATRIX plays the role of Frobenius:
- Frobenius acts on H^*(X, Q_l) with eigenvalues alpha_i; zeta_X = prod(1 - alpha_i q^{-s})^{+-1}.
- The S-matrix acts on K_0(V-mod) tensor C = C^r; the eigenvalues of S are the QUANTUM DIMENSIONS (up to normalization).

But there is a crucial disanalogy: Frobenius is a SINGLE operator whose iterates produce all point counts |X(F_{q^n})|. The S-matrix is part of the SL(2,Z) representation (S and T together), and the partition function Z(tau) transforms under the FULL modular group, not under iterates of a single operator.

### 4.3 What plays the role of etale cohomology?

Three candidates:

**(a) The modular functor / conformal blocks.** The spaces of conformal blocks V(Sigma_g, p_1, ..., p_n; V_1, ..., V_n) form a vector bundle over the moduli space of pointed curves. These carry a FLAT connection (the KZ/Hitchin connection). The monodromy of this connection around loops in M_g gives the modular representation of the mapping class group. This is the closest analogue to etale cohomology: it is a local system on a moduli space whose monodromy carries arithmetic information.

**(b) The factorization homology.** For a factorization algebra F_A on a curve X:

  integral_X F_A = chiral homology of A on X

This depends on the COMPLEX STRUCTURE of X (unlike etale cohomology, which is topological). Varying X over M_g gives the FACTORIZATION HOMOLOGY SHEAF, a D-module on M_g. The spectral data of this D-module (its characteristic variety, its monodromy) is the correct higher-categorical analogue.

**(c) The bar complex B(A) itself.** The bar complex is a factorization COALGEBRA on Ran(X). Its structure maps encode the collision data. The Verdier dual D_{Ran}(B(A)) = B(A!) intertwines the algebra and its dual. The "cohomology" of B(A) (in the factorization sense) is H*(B(A)) = (A!)^v, the linear dual of the Koszul dual coalgebra. This is FINITE-DIMENSIONAL for Koszul algebras and carries a natural weight grading -- but it does not see the primary spectrum directly.

### 4.4 Proposed framework: the spectral decomposition IS the cohomology

The correct analogy is:

| Algebraic geometry | VOA |
|----|-----|
| X/F_q (variety) | V (vertex algebra) |
| Frobenius | S-matrix |
| H^i(X, Q_l) | Conformal blocks / modular functor |
| zeta_X(s) = det(1 - Frob * q^{-s} \| H^*) | epsilon^c_s = spectral coefficient of Z-hat^c on SL(2,Z)\H |
| Weil conjectures (rationality, FE, Riemann hypothesis) | Benjamin-Chang FE epsilon^c_{c/2-s} = F(s)*epsilon^c_{c/2+s-1} |
| Lefschetz trace formula | Verlinde formula |
| K_0(Coh(X)) | K_0(V-mod) = Grothendieck/fusion ring |
| Chern character K_0 -> H^* | Characters chi_i: K_0 -> C[[q]] |

The analogue of the Riemann hypothesis for zeta_X(s) (the Deligne theorem: |alpha_i| = q^{w_i/2}) is:

  For epsilon^c_s: the nontrivial zeros of zeta(2s-1) in the functional equation lie on Re(s) = 1/2.

This is the actual Riemann hypothesis, appearing as the LOCATION of poles of the functional-equation factor F_c(s) (from zeta(2s)/zeta(2s-1) in the denominator). The Benjamin-Chang construction does NOT prove RH; it shows that RH is EQUIVALENT to certain constraints on the spectral coefficients of every 2d CFT partition function.

---

## 5. The Four Questions Answered

### Q1: Does epsilon^c_s = sum [M] * (dim M)^{-s} in some K-theoretic sense?

**Partially.** For rational VOAs, one can write:

  epsilon^c_s = sum_i m_i * (2*h_i)^{-s}
             = sum_i m_i * (2 * wt([L_i]))^{-s}

where wt: K_0 -> Q is the weight map (from L_0 eigenvalues) and m_i is the multiplicity (from the modular invariant). This is a "K-theoretic zeta function" only if one enriches K_0 with the weight grading AND the modular invariant -- i.e., one needs K_0 together with both the additive and multiplicative structures of the fusion ring, the conformal dimensions, and the physical pairing. At that point, one has essentially the FULL modular data, and K_0 is just the indexing set.

### Q2: Does HH_*(V-mod) encode the spectral data?

**HH_0 encodes the characters, not the spectral zeta.** The characters chi_i(tau) are the INPUT to the Roelcke-Selberg decomposition; the spectral zeta is the OUTPUT. The passage requires the ANALYTIC structure of the modular curve (the Laplacian, the Eisenstein series, the Maass forms). This is not a categorical operation.

For D^b(V-mod): if V is rational and V-mod is semisimple, D^b adds nothing. If V-mod is non-semisimple (logarithmic), the Ext data in D^b is richer and connects to MOCK MODULAR forms (Creutzig-Ridout, Adamovic-Milas). Whether mock modular forms connect to spectral zeta functions is a frontier question.

### Q3: Does ChirHoch*(V) see the primary spectrum?

**No.** ChirHoch* is the tangent complex to the MC moduli at Theta_A. It sees the DEFORMATION THEORY of the chiral algebra, not its representation theory. The primary spectrum is a property of the module category. ChirHoch^0 = center Z(A) is the algebra of endomorphisms of the identity functor on V-mod (this does connect to CENTRAL characters, which label blocks, but not to conformal dimensions within a block).

The indirect connection: ChirHoch* -> MC moduli -> shadow obstruction tower -> shadow-spectral correspondence (for lattice VOAs) -> epsilon^c_s. But this chain passes through the partition function and modular invariance, not through K-theory.

### Q4: How does K-theory handle continuous spectra (Virasoro at generic c)?

**It does not.** K_0 of a category with continuous simple objects is a free abelian group on an uncountable set, which carries no useful structure for forming Dirichlet series.

The correct tool for continuous spectra is SPECTRAL THEORY on the modular curve:
- The Roelcke-Selberg decomposition provides a continuous spectral measure (the Eisenstein series E_s) and a discrete cuspidal part (the Maass forms u_j).
- The spectral coefficients c(t) of Z-hat^c against E_{1/2+it} form the Eisenstein part of the decomposition.
- The Benjamin-Chang spectral zeta IS these spectral coefficients, evaluated at the Eisenstein spectral parameter.

This is a spectral-theoretic construction (eigenfunction expansion of the Laplacian on L^2(SL(2,Z)\H)), not a categorical construction.

---

## 6. What the Manuscript Already Has

The manuscript's framework already contains the correct pieces, distributed across several chapters:

1. **ChirHoch* (Theorem H, chiral_hochschild_koszul.tex)**: deformation theory of the algebra. Polynomial growth, Koszul duality. Does NOT see the primary spectrum.

2. **Annulus trace (thm:thqg-annulus-trace, thqg_open_closed_realization.tex)**: integral_{S^1} M = HH_*(M). This recovers CHARACTERS (trace of identity on each simple module), which is the input to Benjamin-Chang.

3. **Fusion category / Grothendieck ring (minimal_model_fusion.tex)**: K_0(V-mod) with fusion product. For rational V, this is a finite-rank ring with known structure.

4. **Shadow-spectral correspondence (thm:shadow-spectral-correspondence, arithmetic_shadows.tex)**: relates shadow depth to the number of L-functions in epsilon^c_s. PROVED for lattice VOAs. This is the deepest connection between the algebraic (bar-cobar) and analytic (L-function) sides.

5. **Sewing-Rankin-Selberg bridge (sec:sewing-RS-bridge, arithmetic_shadows.tex)**: the 8-step chain from sewing operator to shadow-spectral correspondence. Each step proved.

The missing piece is a DIRECT categorical construction that produces epsilon^c_s from D^b(V-mod) without passing through the analytic spectral decomposition on the modular curve. Such a construction would be a genuine "motivic" interpretation of the spectral zeta -- analogous to the passage from etale cohomology to the Hasse-Weil zeta function, but in the VOA setting. This is a frontier question.

---

## 7. Structural Obstructions to a Direct Categorical Construction

### 7.1 The modular curve is not algebraic in the right sense

The Roelcke-Selberg decomposition uses the HYPERBOLIC LAPLACIAN on the modular curve SL(2,Z)\H. This is a real-analytic operator, not an algebraic one. The Eisenstein series E_s(tau) is a real-analytic eigenfunction of the Laplacian, not a holomorphic modular form.

A categorical construction of epsilon^c_s would need to "categorify" the spectral decomposition of L^2(SL(2,Z)\H). This is related to the GEOMETRIC Langlands programme (categorification of the spectral decomposition of automorphic forms), which is a major open programme.

### 7.2 The scattering matrix involves zeta zeros

The functional equation of epsilon^c_s involves the ratio zeta(2s)/zeta(2s-1), whose poles are the nontrivial zeros of zeta(s). Any categorical construction that produces epsilon^c_s must therefore "know about" the Riemann zeta function. But the Riemann zeta function is NOT a categorical invariant of any single VOA; it is a UNIVERSAL object that appears in the scattering theory of every automorphic form.

### 7.3 The structural obstruction (from benjamin_chang.md, rem:structural-obstruction)

The shadow obstruction tower and MC equation constrain spectral coefficients c(t) on the REAL spectral line (s = 1/2 + it, t real). The zeta zeros live at COMPLEX spectral parameters. This separation is structural: algebraic constraints on the spectral line cannot reach the scattering poles without analytic continuation of the spectral data off the real axis. No purely algebraic/categorical construction can bridge this gap.

---

## 8. Open Directions

### 8.1 Logarithmic VOAs and mock modular forms

For non-rational VOAs with non-semisimple module categories (W(p) triplet algebras, admissible-level quotients), the characters are MOCK MODULAR FORMS (Zwegers, Creutzig-Ridout). The derived category D^b(V-mod) is genuinely richer (Ext != 0). Whether the Ext data produces a different spectral zeta (one that sees the "shadow" of the mock modular form, in Zwegers' sense -- a coincidence of terminology with the shadow obstruction tower worth investigating) is unexplored.

### 8.2 Categorical trace and the Witten-Kontsevich index

The CATEGORICAL TRACE of the identity functor on D^b(V-mod) (in the sense of Ben-Zvi-Francis-Nadler) is:

  Tr(Id_{D^b(V-mod)}) = integral_{S^1} D^b(V-mod) = HH_*(D^b(V-mod))

For a smooth proper dg-category C:

  HH_*(C) = "the space of self-dual bulk local operators"

This is the CATEGORICAL analogue of the partition function. The passage from this to the spectral zeta requires the spectral decomposition, which is the analytic step.

### 8.3 The derived center as universal bulk

The chiral derived center Z^{der}_{ch}(A) = H*(C^bullet_{ch}(A,A), delta) is defined in the manuscript (def:thqg-chiral-derived-center). For the open/closed MC element Theta^{oc} = Theta_A + sum mu^{M_j}, the closed projection is the bar-intrinsic Theta_A and the mixed projection is the bulk-to-boundary coupling. The derived center is the UNIVERSAL BULK -- it classifies bulk operators, not boundary representations. Its HH_* does NOT directly produce the spectral zeta.

### 8.4 The motivic spectral zeta (speculative)

A genuinely new construction would be:

  zeta_V^{mot}(s) := sum_i [L_i] * (L_0|_{L_i})^{-s}    in    K_0(V-mod) tensor C

where [L_i] is the K-theory class and (L_0|_{L_i})^{-s} is the "motivic weight." This lives in a completed K-theory ring and would need:
(a) a topology on K_0 (from the weight grading),
(b) a "motivic" version of the Mellin transform,
(c) a categorical functional equation (from the modular tensor category structure).

For rational V, this reduces to a finite sum and the functional equation comes from the S-matrix. For irrational V, this requires a continuous K-theory (probably KK-theory or some form of spectral K-theory) and the functional equation would need to come from a categorical version of the Roelcke-Selberg decomposition. This is entirely speculative and no construction exists.

---

## 9. Key Distinctions (Summary Table)

| Object | What it encodes | Sees primary spectrum? | Sees epsilon^c_s? |
|--------|----------------|----------------------|-------------------|
| K_0(V-mod) | Simple modules as abstract classes | Yes (as a set) | No (no metric) |
| K_0^{fil}(V-mod) | Simple modules with weight grading | Yes (with dimensions) | Partially (need modular invariant + Mellin) |
| HH_0(V-mod) | Characters / traces | Yes (via characters) | No (characters are input, not output) |
| HH_*(V-mod) | Full categorical trace | Yes (all-genus data) | No (topological, not analytic) |
| D^b(V-mod) | Ext groups | Only for non-semisimple | Open (mock modular?) |
| ChirHoch*(A) | Deformation theory of A | No | No |
| Z^{der}_{ch}(A) | Bulk operators | No | No |
| Shadow obstruction tower Theta_A | OPE invariants (kappa, C, Q, ...) | Indirectly (via shadow-spectral) | Indirectly (via epsilon_{Q_L}) |
| Roelcke-Selberg decomposition | Spectral data on M_{1,1} | Yes | Yes (by definition) |

The spectral zeta epsilon^c_s lives at the ANALYTIC level (spectral decomposition on the modular curve). All categorical constructions (K-theory, HH_*, ChirHoch*, D^b) live at the ALGEBRAIC level. The bridge between them is the MODULAR INVARIANCE of the partition function, which is a datum of the PHYSICAL theory (not of the algebra or its module category alone).
