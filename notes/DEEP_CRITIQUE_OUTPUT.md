# Deep Mathematical Critique & Horizon Exploration
## Chiral Duality in the Presence of Quantum Corrections

**Date**: 2026-03-05 (F1 update: Session 103)
**Census**: PH 613 / PE 317 / CJ 84 / H 14 = 1028 tagged claims (.tex only)
**Pages**: ~1133, zero LaTeX errors, zero undefined references

**F1 Status (Session 103)**: SUBSTANTIALLY ADDRESSED. Three layers now:
1. chiral_modules.tex comp:bgg-sl2-pipeline — 5-step bar-to-BGG pipeline for sl₂ (Session 102)
2. detailed_computations.tex sec:bgg-sl2-pipeline — explicit matrix-level verification with prop:bar-bgg-sl2 + cor:bgg-koszul-involution (Session 103)
3. chiral_modules.tex prop:vacuum-verma-koszul — vacuum Verma under module Koszul duality (Session 101)
The "no concrete instantiation" gap for BGG/module theory is now closed for sl₂.

---

# PART I: THE CRITIQUE

## F1. The Module Theory Orphanage — RESOLVED (Sessions 98-103)

```
[SEVERITY: CRITICAL]
[LOCATION: chiral_modules.tex:2308, thm:bgg-from-bar]
GAP: The BGG resolution theorem (Bernstein-Gelfand-Gelfand resolution derived
     from bar complex) is proved in full generality but NEVER APPLIED to any
     specific Lie algebra. Not sl_2, not sl_3, not any algebra. The theorem
     says the bar complex geometrically realizes the BGG resolution — but no
     reader sees what this looks like concretely.
IMPACT: A referee will ask: "You prove the BGG resolution comes from the bar
     complex. What does this mean for the BGG resolution of the trivial module
     for sl_2 at level k? Show me." The theorem is powerful precisely because
     it should produce KNOWN resolutions from a NEW mechanism — but the payoff
     is never delivered.
REMEDY: Compute the BGG resolution for sl_2 at generic level via bar complex.
     Show B^n(sl_2_k) -> Verma modules recovers the classical BGG complex
     M(w*0) -> ... -> M(0) -> L(0) -> 0 with the correct Weyl group
     combinatorics. This is a 2-page computation. Then do sl_3 (5 pages).
     [SCALE: ~7 pages total]
```

```
[SEVERITY: CRITICAL]
[LOCATION: chiral_modules.tex:1264, prop:verma-bar-complex;
           also chiral_modules.tex:2308, thm:bgg-from-bar]
GAP: 16 module-theoretic theorems in the three core theory chapters have NO
     concrete instantiation in Part 2. The module Koszul duality functor
     (thm:e1-module-koszul-duality) is defined and its formal properties
     proved, but it is NEVER APPLIED to track a specific module through the
     duality. No Verma module, no Fock module, no evaluation module is
     explicitly sent through the functor with the output computed.
IMPACT: Module Koszul duality is half the book's representation theory. Without
     concrete examples, it reads as abstract machinery without payload. A referee
     at Annals will say: "What does the Koszul dual of the vacuum Verma module
     look like? Of a Whittaker module?"
REMEDY: For sl_2 at generic level k:
     (1) Apply module Koszul duality to M(0) (vacuum Verma). Show the output is
         a specific module over sl_2_{-k-4}. Identify it.
     (2) Apply to Fock module F_lambda. Show it maps to a twisted module over the
         dual algebra.
     (3) For Yangian: track the evaluation module V(a) through the R -> R^{-1}
         duality explicitly (the formal statement is in yangians.tex:297-319 but
         the actual module-level computation is absent).
     [SCALE: ~10 pages across 3 examples]
```

## F2. The Genus >= 2 Wall — RESOLVED (Session 102, genus-2 sl₂ bar differential)

```
[SEVERITY: CRITICAL]
[LOCATION: chapters/examples/ (all files); higher_genus.tex:2560-2700]
GAP: For non-free algebras, NO bar differential is explicitly computed at
     genus >= 2. The genus universality theorem (thm:genus-universality) gives
     obs_g(A) = kappa(A) * lambda_g for all g, but this is a STRUCTURAL result
     about the curvature class — it does NOT compute the bar differential d^{(g)}
     or the bar cohomology H*(B^{(g)}(A)) for g >= 2.

     Specifically:
     - Heisenberg: genus-2 curvature computed (thm:heisenberg-genus2-obstruction)
       but this is a FREE theory (no quantum corrections)
     - sl_2, Virasoro, W_3: genus-1 pipelines complete; genus-2 absent
     - Yangian: genus-0 only
     - deformation_quantization.tex:117 explicitly says genus >= 2 "remains open"
       for Kontsevich formality

     The book claims "all genera" repeatedly, but the examples stop at g=1.
IMPACT: The genus universality theorem is beautiful but it only governs the
     curvature m_0^{(g)} = kappa * lambda_g. The actual bar cohomology at g >= 2
     involves the FULL bar differential (including d^{(2)}_fact and d^{(2)}_config)
     acting on the bar complex. The F_g values in the genus expansion tables come
     from the universality formula, not independent g >= 2 computation. A referee
     will notice: "Your g >= 2 entries are corollaries of the universality theorem,
     not independent computations."
REMEDY: Compute the genus-2 bar differential for sl_2_k explicitly:
     (1) Write the genus-2 propagator K^{(2)}(z,w) on Sigma_2 (this exists in
         heisenberg_eisenstein.tex for Heisenberg; extend to sl_2)
     (2) Compute d^{(2)} on B^1(sl_2_k) = sl_2 and verify (d^{(2)})^2 = kappa * lambda_2
     (3) Compute the genus-2 partition function F_2 independently and verify it
         matches the universality prediction
     This would be the FIRST non-free genus-2 bar computation in the literature.
     [SCALE: ~15 pages, substantial new mathematics]
```

## F3. The Type-A Monoculture — RESOLVED (Session 98, G2 bar complex)

```
[SEVERITY: MAJOR]
[LOCATION: chapters/examples/ (all files)]
GAP: Every explicit bar complex computation is for type A:
     - sl_2, sl_3 (type A_1, A_2)
     - Virasoro (type A_1 DS reduction)
     - W_3 (type A_2 DS reduction)
     - E_8 appears in tables but only generators (degree 1), no bar differential
     - G_2 appears in W-algebra tables (w_algebras_deep.tex:382,430) but NO
       bar complex computed
     - B_n, C_n: mentioned as orbifold constructions (lattice_foundations.tex:508-518)
       but NO bar complex
     - D_n: D_4 triality mentioned but NO bar complex

     Non-simply-laced algebras (B_n, C_n, F_4, G_2) are particularly important
     because h^dual != h, the Feigin-Frenkel involution k -> -k-2h^dual
     behaves differently, and the KM periodicity period is NOT 2h.
IMPACT: A referee specializing in representation theory will ask: "Does your
     framework handle non-simply-laced algebras? Where is the evidence?" The
     theory chapters prove everything for general g, but the examples only
     exercise type A. The Koszul duality k -> -k-2h^dual has qualitatively
     different behavior for B_n vs C_n (h^dual(B_n) = 2n-1, h^dual(C_n) = n+1).
REMEDY: Compute the bar complex for G_2 (rank 2, simplest non-simply-laced):
     (1) G_2 Kac-Moody at level k: identify generators (14-dim adjoint)
     (2) Bar complex degree 2: quadratic dual relations from the G_2 OPE
     (3) Curvature: kappa(G_2_k) at genus 1, verify h^dual = 4
     (4) Feigin-Frenkel: k -> -k-8 (note: 2h^dual = 8, NOT 2h = 12)
     This would be a 5-page computation with high impact.
     Alternatively: so_5 = B_2 (rank 2, h^dual = 3, h = 4, 2h^dual = 6).
     [SCALE: ~5 pages for one non-simply-laced example]
```

## F4. The A-infinity Mirage — RESOLVED (Session 100, m4 pentagon)

```
[SEVERITY: MAJOR]
[LOCATION: chapters/theory/higher_genus.tex:99-167;
           chapters/connections/feynman_diagrams.tex:698-780]
GAP: The A-infinity operations m_3, m_4, m_5, ... are discussed extensively
     as CONCEPTS but only m_3 is explicitly computed for ONE example:

     - m_3(T tensor T tensor T) = (c/12) partial^3 T + lower order terms
       (Virasoro, feynman_diagrams.tex:746)
     - m_3 for W_3: formula given (w_algebras_framework.tex:1762) but using
       schematic notation, not a closed-form result
     - m_4: described (feynman_diagrams.tex:762-777) but the actual operation
       m_4(T tensor T tensor T tensor T) is NEVER computed
     - m_5: associahedron identity stated (higher_genus.tex:335) but the
       operation itself is NEVER computed
     - Full curved A-infinity structure (m_0, m_1, m_2, m_3, m_4, ...):
       NEVER fully written out for any single example

     The m_3 formula for Virasoro via configuration space integrals is a
     highlight — but it stands alone. The book promises an A-infinity
     framework but delivers only m_0 (curvature), m_2 (OPE), and one m_3.
IMPACT: The A-infinity perspective is a key selling point. Computing m_4 for
     Virasoro would verify the pentagon identity concretely. Computing m_3
     for sl_2_k would show how the level k enters the homotopy.
REMEDY:
     (1) Compute m_4(T,T,T,T) for Virasoro via boundary of K_5 (Stasheff
         associahedron). Verify the A-infinity relation at n=4.
     (2) Compute m_3(J^a, J^b, J^c) for sl_2_k. The answer should involve
         the Killing form and the level k.
     (3) Write out the full table: m_0, m_1, m_2, m_3, m_4 for Virasoro with
         explicit formulas and verify all A-infinity relations through n=4.
     [SCALE: ~8 pages]
```

## F5. The Geometric-Algebraic Bar Comparison Gap — RESOLVED (Session 98)

```
[SEVERITY: MAJOR]
[LOCATION: bar_cobar_construction.tex, thm:geometric-equals-operadic-bar]
GAP: The theorem thm:geometric-equals-operadic-bar states that the geometric
     bar complex (via configuration space integrals on FM compactifications)
     equals the algebraic bar complex (via operadic Koszul theory). This is
     proved abstractly. But NO example verifies this term-by-term:

     The examples use the geometric bar complex (propagators, residues, Arnold
     relations) as their PRIMARY tool, referencing the abstract theorem. But
     they never verify: "The algebraic bar differential d_alg applied to
     [J^a | J^b] gives X, and the geometric bar differential (residue of
     J^a(z_1) J^b(z_2) eta_12 at z_1=z_2) gives the SAME X."

     This comparison is the BRIDGE between Part 1 and Part 2. It is proved
     once abstractly and then assumed everywhere.
IMPACT: For a monograph claiming to connect operadic algebra to geometry,
     the central comparison should be verified explicitly in at least one
     example. Otherwise the geometric language is decoration on algebraic
     computations.
REMEDY: For Heisenberg (simplest case):
     (1) Write the algebraic bar differential on B^2(H_k) = C * J tensor C * J
     (2) Write the geometric bar differential via Res_{z_1=z_2}[J(z_1)J(z_2)eta_12]
     (3) Verify they agree term by term
     Then for sl_2_k at degree 2 (more interesting: structure constants enter).
     [SCALE: ~3 pages]
```

## F6. Lurie's Higher Algebra is Undercited — RESOLVED (Session 101, 17 citations)

```
[SEVERITY: MAJOR]
[LOCATION: introduction.tex (E_1/E_inf dictionary); bar_cobar_construction.tex;
           chiral_koszul_pairs.tex]
GAP: The E_1/E_inf distinction is CENTRAL to the monograph — it drives the
     three Koszul duality mechanisms, the Yangian theory, the entire nonlocal
     VA framework. Yet Lurie's Higher Algebra receives only ~2 explicit
     citations. The E_n-algebra framework (HA Chapter 5), the bar-cobar
     adjunction for E_n-algebras (HA Section 5.3), and the identification
     E_1 = associative, E_inf = commutative (HA Section 5.1-5.2) are all
     used implicitly but rarely cited.

     By contrast, Costello-Gwilliam receives 24+ citations.
IMPACT: A referee from the homotopical algebra community will flag this
     immediately. The E_n-operad framework is Lurie's contribution; using
     it without adequate citation is a gap in attribution.
REMEDY: Add Lurie HA citations in:
     - introduction.tex where E_1/E_inf dictionary is introduced
     - bar_cobar_construction.tex for E_1 bar-cobar adjunction
     - chiral_koszul_pairs.tex for E_1 duality theorem
     - yangians.tex for E_1-chiral definition
     [SCALE: ~1 hour, 10-15 citation additions]
```

## F7. Five Most Damaging Referee Objections — 4/5 RESOLVED (only Objection 2 remains: genus-2 wall)

```
[SEVERITY: META]
[LOCATION: entire manuscript]

OBJECTION 1 (Representation theory referee):
"The module Koszul duality functor is defined but never applied. Show me what
happens to the vacuum module of sl_2 at level k under your duality. Until you
do, I cannot assess whether this functor produces anything new."
[REQUIRES: F1 remedy]

OBJECTION 2 (Algebraic geometry referee):
"Your three main theorems are proved for all genera, but your examples stop at
genus 1. The genus universality theorem is elegant, but it governs only the
curvature class. What does the actual bar cohomology look like at genus 2 for
a non-free algebra? Without this, the 'all genera' claim is structural, not
computational."
[REQUIRES: F2 remedy]

OBJECTION 3 (Lie theory referee):
"Every computation is for sl_N or its reductions. Non-simply-laced algebras
have qualitatively different Koszul duality behavior (h^dual != h, Feigin-Frenkel
involution differs). Can your framework handle G_2? Show me."
[REQUIRES: F3 remedy]

OBJECTION 4 (Homotopy algebra referee):
"You promise an A-infinity perspective on chiral algebras via configuration
spaces. I see m_2 (the OPE) and m_0 (genus-1 curvature) computed everywhere.
I see one m_3 for Virasoro. Where is m_4? Where is the pentagon identity verified
concretely? The A-infinity story is incomplete."
[REQUIRES: F4 remedy]

OBJECTION 5 (Foundations referee):
"Your E_1/E_inf framework depends on Lurie's Higher Algebra, but you cite
it only twice. The entire E_n-operad hierarchy is fundamental to your claims
about Yangians and nonlocal VAs. Please add proper attribution."
[REQUIRES: F6 remedy]
```

---

# PART II: THE HORIZON

## New Implied Results (NOT in HORIZON.md)

### H1. BGG Resolution via Bar Complex for sl_2

```
[LEVEL: A]
[CONFIDENCE: HIGH]
[SCALE: SECTION]
STATEMENT: For sl_2 at generic level k, the bar complex B^*(sl_2_k)
  geometrically realizes the BGG resolution:
  ... -> B^2(sl_2_k) -> B^1(sl_2_k) -> B^0(sl_2_k) -> L(0) -> 0
  where B^n maps to the direct sum of Verma modules M(w*0) with
  l(w) = n, recovering the classical BGG complex with Weyl group
  W = {1, s} acting on the weight lattice.
FOLLOWS FROM: thm:bgg-from-bar (chiral_modules.tex:2308),
  thm:sl2-koszul-dual (kac_moody_framework.tex),
  prop:verma-bar-complex (chiral_modules.tex:1264)
PROOF SKETCH: The bar complex B^n(sl_2_k) = (sl_2)^{tensor n} tensor
  Omega^n(C-bar_n(P^1))(log D). At degree 1: B^1 = sl_2^* = sl_2
  (self-dual). The bar differential d: B^1 -> B^0 is the augmentation.
  At degree 2: B^2 = sl_2 tensor sl_2 tensor H^0(C-bar_3(P^1), Omega^1(log)).
  The differential extracts the bracket [e, f] = h, [h, e] = 2e, [h, f] = -2f
  via residues. The cohomology at each degree matches dim M(w*0).
BLOCKED BY: Explicit computation of B^n for n >= 2 matching Verma filtration.
REFERENCES: BGS96 Thm 1.1.1; Humphreys "Representations of Semisimple Lie
  Algebras in the BGG Category O", Section 6.
```

### H2. Vacuum Module Under Koszul Duality for sl_2

```
[LEVEL: A]
[CONFIDENCE: HIGH]
[SCALE: COROLLARY]
STATEMENT: The module Koszul duality functor Phi of thm:e1-module-koszul-duality
  sends the vacuum Verma module M(0) of sl_2 at level k to the vacuum Verma
  module M(0) of sl_2 at level -k-4, with Shapovalov form reversal:
  Phi(M(0)_k) = M(0)_{-k-4}, where the singular vectors at level k correspond
  to co-singular vectors at level -k-4.
FOLLOWS FROM: thm:e1-module-koszul-duality (chiral_koszul_pairs.tex:1737),
  thm:sl2-koszul-dual (kac_moody_framework.tex),
  Feigin-Frenkel involution k -> -k-2h^dual = -k-4 for sl_2
PROOF SKETCH: The Koszul dual of sl_2_k is sl_2_{-k-4} (Feigin-Frenkel,
  thm:ff-involution). Module Koszul duality is functorial over this algebra
  duality. The vacuum Verma is the free module on the vacuum vector, hence
  it maps to the free module on the dual vacuum = vacuum Verma at dual level.
  Singular vector structure reverses because the Shapovalov determinant
  det S_n(k) -> det S_n(-k-4) changes sign pattern.
BLOCKED BY: Explicit verification that Shapovalov zeroes match.
REFERENCES: KL93 (tensor structure); Feigin-Frenkel (involution).
```

### H3. G_2 Bar Complex and Non-Simply-Laced Koszul Duality

```
[LEVEL: B]
[CONFIDENCE: MEDIUM]
[SCALE: SECTION]
STATEMENT: For G_2 at level k, the bar complex B^*(G_2_k) in degree 2 is:
  B^2 = Lambda^2(g_2^*) / R^perp
  where R^perp is the orthogonal complement of the G_2 OPE relations.
  The curvature satisfies kappa(G_2_k) = 4(k+4)/3, and the Feigin-Frenkel
  dual is G_2 at level -k-8 (since 2h^dual(G_2) = 8, NOT 2h(G_2) = 12).
FOLLOWS FROM: thm:km-bar-complex (kac_moody_framework.tex),
  prop:km-bar-curvature, thm:genus-universality
PROOF SKETCH: G_2 has dim = 14, h^dual = 4, h = 6. The Killing form
  gives the OPE J^a(z)J^b(w) ~ k*kappa^{ab}/(z-w)^2 + f^{ab}_c J^c(w)/(z-w).
  This is quadratic, so bar degree 2 is R^perp subset g_2^* tensor g_2^*.
  The structure constants f^{ab}_c for G_2 involve the short and long roots
  with ratio |alpha_long|^2/|alpha_short|^2 = 3. The curvature formula
  kappa = dim(g)*c_1/(2h^dual) gives kappa = 14*(k+4)/(2*4)*c_1 — need to
  verify the coefficient via Sugawara c = k*14/(k+4).
BLOCKED BY: Explicit G_2 structure constants; verification of kappa formula
  for non-simply-laced (the Sugawara formula may need long-root normalization).
REFERENCES: G_2 structure constants from Humphreys Table 9.1;
  Feigin-Frenkel for non-simply-laced involution.
```

### H4. Pentagon Identity Verification for Virasoro m_4

```
[LEVEL: A]
[CONFIDENCE: HIGH]
[SCALE: COROLLARY]
STATEMENT: The A-infinity operation m_4(T,T,T,T) for the Virasoro algebra
  is determined by the boundary of the Stasheff associahedron K_5 and
  satisfies:
  m_2(m_3 tensor id) + m_3(m_2 tensor id tensor id) + m_3(id tensor m_2 tensor id)
  + m_3(id tensor id tensor m_2) + m_2(id tensor m_3) + m_4(m_1 tensor ...) = 0
  where m_1 = 0 for Virasoro. The explicit formula involves c^2 and partial^4 T
  terms from double residues on boundary(C-bar_5(P^1)).
FOLLOWS FROM: higher_genus.tex:335 (thm for K_6 associahedron);
  feynman_diagrams.tex:714-746 (m_3 computation);
  the general A-infinity relation at n=4
PROOF SKETCH: At n=4, with m_1=0, the A-infinity relation reduces to:
  m_2(m_3(T,T,T), T) + m_2(T, m_3(T,T,T)) + m_3(m_2(T,T), T, T)
  + m_3(T, m_2(T,T), T) + m_3(T, T, m_2(T,T)) = d(m_4(T,T,T,T))
  Using m_3(T,T,T) = (c/12)partial^3 T + ... and m_2(T,T) = (c/2)partial^3 + 2T*partial + ...
  (the Virasoro OPE), compute each term via residues on boundary(K_5) =
  boundary(C-bar_5(P^1)). The K_5 has 14 vertices and the boundary has
  dimension 2 with faces corresponding to parenthesizations.
BLOCKED BY: Careful residue computation on all faces of K_5.
REFERENCES: Stasheff, "Homotopy associativity of H-spaces";
  Loday-Vallette Section 9.2 for the A-infinity relations.
```

### H5. Genus-2 Bar Differential for sl_2 at Generic Level

```
[LEVEL: B]
[CONFIDENCE: MEDIUM]
[SCALE: SECTION]
STATEMENT: For sl_2 at generic level k on a genus-2 surface Sigma_2 with
  period matrix Omega in H_2, the genus-2 bar differential d^{(2)} on
  B^1(sl_2_k) = sl_2 acts by:
  d^{(2)}(J^a) = kappa * sum_{i,j=1}^{2} omega_i wedge omega_j * kappa^{ab} * ...
  where kappa = 3(k+2)/4 (the sl_2 obstruction parameter).
  The curvature (d^{(2)})^2 = kappa * lambda_2, where
  lambda_2 = c_2(E) in H^4(M-bar_2), confirming universality at g=2.
FOLLOWS FROM: thm:genus-universality, thm:sl2-genus1-curvature,
  thm:heisenberg-genus2-obstruction (for the genus-2 propagator structure),
  def:period-matrix-g2, def:prime-form-g2
PROOF SKETCH: Replace the genus-1 propagator (Weierstrass zeta + E_2 correction)
  with the genus-2 propagator K^{(2)}(z,w) = partial_z log theta[delta](z-w|Omega)
  (from heisenberg_eisenstein.tex). The B-cycle monodromies give TWO independent
  shifts: K(z + delta_{B_j}, w) = K(z,w) - 2*pi*i * omega_j(w) for j=1,2.
  The curvature (d^{(2)})^2 arises from the product of these two monodromies:
  kappa * (omega_1 wedge omega_2) = kappa * c_2(E). The Shapovalov form
  remains non-degenerate at generic k, so the spectral sequence collapses at E_2.
BLOCKED BY: Explicit action of d^{(2)} on generators of sl_2 (need the
  genus-2 Sugawara construction and the two A-cycle integrations).
REFERENCES: Fay "Theta Functions on Riemann Surfaces" for genus-2 propagator;
  Mumford "Tata Lectures on Theta II" for Siegel modular forms.
```

### H6. Kazhdan-Lusztig Equivalence via Bar-Cobar

```
[LEVEL: B]
[CONFIDENCE: MEDIUM]
[SCALE: SECTION]
STATEMENT: The Kazhdan-Lusztig equivalence O_kappa(g-hat) ≃ Rep^fd(U_q(g))
  (for q = exp(i*pi/kappa)) can be recovered from the bar-cobar framework
  by composing: (a) chiral module Koszul duality with (b) the identification
  of the Koszul dual module category with quantum group representations.
  Specifically, the bar complex of the affine KM algebra produces a coalgebra
  whose comodule category is equivalent to U_q(g)-modules.
FOLLOWS FROM: thm:e1-module-koszul-duality, KL93 (tensor structure),
  thm:km-bar-complex, BGS96 Thm 1.2.6 (Koszul duality functor on D^b)
PROOF SKETCH: The bar complex B(g-hat_k) is a DG-coalgebra. Its comodule
  category D^co(B(g-hat_k)-comod) is equivalent (by bar-cobar adjunction)
  to D^b(g-hat_k-mod). The Koszul dual algebra g-hat_k^! = g-hat_{-k-2h^dual}
  has module category equivalent (by Feigin-Frenkel) to the same category
  with quantum parameter q <-> q^{-1}. The KL equivalence identifies this
  with Rep(U_q(g)). The composition gives the KL equivalence as a
  "bar-cobar transport."
BLOCKED BY: Proving that the bar-cobar transport preserves the tensor structure
  (not just the abelian category structure). This requires showing the
  coalgebra structure on B(g-hat_k) is compatible with the KL tensor product.
REFERENCES: KL93 Parts I-IV; BGS96; Finkelberg "An equivalence of fusion
  categories" (for the tensor structure identification).
```

### H7. Positselski Acyclicity and Exotic Derived Categories at Higher Genus

```
[LEVEL: B]
[CONFIDENCE: HIGH]
[SCALE: COROLLARY]
STATEMENT: At genus g >= 1, the bar complex B^{(g)}(A) is acyclic as an
  ordinary DG-coalgebra (because the curvature m_0 != 0 makes the naive
  cohomology trivial). The correct framework is Positselski's coderived
  category D^co(B^{(g)}(A)-comod). This explains why the genus-g bar-cobar
  adjunction must use exotic derived categories, not the standard derived
  category.
FOLLOWS FROM: Positselski "Two Kinds", Section 6.1 (Bar_v(B) acyclic when
  h != 0); thm:curved-bar-cobar (bar_cobar_construction.tex);
  prop:km-bar-curvature (m_0 = kappa * lambda_1 != 0 at g=1)
PROOF SKETCH: At genus 0, m_0 = 0 and B(A) is a DG-coalgebra with meaningful
  cohomology. At genus 1, m_0 = kappa * omega_1 != 0, so B^{(1)}(A) is a
  CURVED DG-coalgebra. Positselski's Remark (p.68) shows that Bar_v of a
  CDG-algebra with h != 0 has acyclic underlying complex. Therefore the
  ordinary derived category D(B^{(1)}(A)-comod) = 0, and one MUST use
  D^co(B^{(1)}(A)-comod). This is already implicit in the manuscript's use
  of completed bar complexes, but making it explicit strengthens the
  conceptual architecture.
BLOCKED BY: Nothing — this is a conceptual clarification, ~1 page.
REFERENCES: Positselski "Two Kinds", Section 6.1, p.68.
```

### H8. Mixed Geometry Interpretation of Koszulity via FM Compactifications

```
[LEVEL: C]
[CONFIDENCE: LOW]
[SCALE: PAPER]
STATEMENT: The diagonal purity condition for Koszulity (Ext^{i,j}(C,C) = 0
  for i != j) should have a geometric interpretation in terms of purity of
  mixed Hodge structures on the cohomology of FM compactifications, parallel
  to BGS96's mixed geometry proof of Koszulity for category O via flag
  varieties.
FOLLOWS FROM: BGS96 Thm 1.4.2 (parity vanishing + mixed geometry -> Koszul);
  thm:geometric-equals-operadic-bar (bar complex = FM cohomology);
  the fact that FM compactifications are smooth projective varieties
  (hence carry pure Hodge structures)
PROOF SKETCH: H^k(C-bar_n(X)) carries a mixed Hodge structure. The bar
  complex filtration induces a weight filtration. Purity (weight = degree)
  would imply diagonal Ext vanishing. For X = P^1 (genus 0), the cohomology
  of C-bar_n(P^1) is known to be pure (Totaro). For X = E (genus 1), the
  mixed Hodge structure on H^*(C-bar_n(E)) has been studied by Dupont.
  Purity in the genus-0 case gives a GEOMETRIC explanation of Koszulity.
BLOCKED BY: Full MHS computation for FM compactifications on higher-genus
  curves. This is a research problem, not a computation.
REFERENCES: BGS96 Section 3; Totaro "Configuration spaces of algebraic
  varieties"; Dupont "The purity of the cohomology of configuration spaces."
```

---

# PART III: THE VISION

## The 3 Most Impactful New Results

### 1. BGG Resolution via Bar Complex (H1 + F1)
**Why**: This is the canonical application that connects bar-cobar machinery to
classical representation theory. Computing the BGG resolution of the trivial sl_2
module from the bar complex, then sl_3, would be the definitive "payoff" theorem
that shows configuration space integrals produce KNOWN representation-theoretic
objects from the NEW geometric mechanism. Every algebraist reading the book will
look for this.

### 2. Non-Simply-Laced Example: G_2 Bar Complex (H3 + F3)
**Why**: Breaking the type-A monoculture is essential for credibility. G_2 is the
simplest non-simply-laced example and would demonstrate that the framework handles
the subtleties of h^dual != h, different root lengths, and the modified
Feigin-Frenkel involution. A 5-page computation with outsized impact.

### 3. Genus-2 Bar Differential for sl_2 (H5 + F2)
**Why**: This would be the first non-free genus-2 bar computation in the literature.
It would validate the genus universality theorem independently, show what genus-2
quantum corrections look like concretely, and move the "genus wall" from g=1 to g=2.
This is substantial new mathematics (~15 pages) but would transform the book's
credibility at higher genus.

## The Missing Chapter: "E_1-Chiral Representation Theory"

### Chapter Outline: Representation Theory of Yangians and Quantum Groups via E_1-Chiral Koszul Duality

**Section 1: The E_1-Chiral Module Category** (~5 pages)
- Definition of E_1-chiral modules (R-matrix-twisted locality)
- Evaluation modules, tensor products, braiding via R-matrix
- Module Koszul duality: V(a) -> V(-a) with R -> R^{-1}
- Theorem: KL equivalence O_kappa ≃ Rep(U_q(g)) via bar-cobar transport

**Section 2: Yangian Category O** (~8 pages)
- Definition of Yangian highest-weight modules (Drinfeld polynomials)
- Bar complex of Y(sl_2) through degree 3 at the module level
- Koszul dual modules: explicit computation for fundamental and adjoint
- Spectral sequence: E_2-collapse and Yangian BGG resolution

**Section 3: Genus-1 Yangian Bar Complex** (~10 pages)
- Construction of d^{(1)} for Y(sl_2) using rational R-matrix propagator
- Curvature: m_0^{(1)} and the Yangian obstruction parameter
- Comparison with quantum group central element (Casimir at q)
- Conjecture: Yangian periodicity vs quantum group periodicity

**Section 4: Coulomb Branches and Geometric Realizations** (~5 pages)
- COHA (cohomological Hall algebra) as factorization algebra
- Bar complex of COHA and the Coulomb branch algebra
- Latyntsev's factorisation quantum groups as alternative framework
- Open problems: genus-g Yangian duality, spectral R-matrix at higher genus

**Section 5: Worked Example: Y(sl_2) Complete Pipeline** (~7 pages)
- Full computation: algebra, dual, bar complex, modules, genus-1 curvature
- The "three theorems in action" for E_1 (parallel to genus_expansions.tex)
- Comparison table: E_inf (Kac-Moody) vs E_1 (Yangian) Koszul duality

**Total: ~35 pages**

## The Narrative Arc

The book's story is:

> **Phenomenon**: Chiral algebras on curves carry Koszul duals, just as
> associative algebras do.
>
> **Surprise**: The duality is not algebraic — it is mediated by the GEOMETRY
> of configuration spaces. The Fulton-MacPherson compactification provides
> the propagator; Verdier duality exchanges bar and cobar; Arnold relations
> ensure d^2 = 0. This is operadic Koszul duality made geometric.
>
> **Deepening**: On higher-genus curves, the geometry produces quantum
> corrections. These corrections are controlled by the cohomology of moduli
> spaces M_g and manifest as curvature m_0, curved A-infinity structures,
> and the complementarity principle: what one algebra sees as deformation,
> its Koszul dual sees as obstruction.
>
> **Payoff**: The framework EXPLAINS three things that were previously mysterious:
> (X) Why central charges appear in pairs c + c' = 26 (for Virasoro),
>     c + c' = dim(g) (for KM) — it's Koszul complementarity applied to
>     the Kodaira-Spencer class.
> (Y) Why the Feigin-Frenkel involution k -> -k-2h^dual governs so much of
>     affine Lie algebra theory — it's the MANIFESTATION of bar-cobar duality
>     at the level of representations.
> (Z) Why vertex algebras and quantum groups are related (KL equivalence) —
>     bar-cobar TRANSPORTS the tensor structure from chiral to quantum, via
>     the coalgebra structure of the bar complex.

---

# PART IV: SUMMARY TABLE

| # | Result | Level | Confidence | Scale | Blocked by |
|---|--------|-------|------------|-------|------------|
| H1 | BGG resolution via bar complex (sl_2) | A | HIGH | SECTION | Degree 2+ Verma matching |
| H2 | Vacuum module under Koszul duality (sl_2) | A | HIGH | COROLLARY | Shapovalov zero matching |
| H3 | G_2 bar complex + non-simply-laced Koszul | B | MEDIUM | SECTION | G_2 structure constants |
| H4 | Pentagon identity via m_4 for Virasoro | A | HIGH | COROLLARY | K_5 residue computation |
| H5 | Genus-2 bar differential for sl_2 | B | MEDIUM | SECTION | Genus-2 Sugawara |
| H6 | KL equivalence via bar-cobar transport | B | MEDIUM | SECTION | Tensor structure compatibility |
| H7 | Positselski acyclicity at higher genus | B | HIGH | COROLLARY | Nothing (clarification) |
| H8 | Mixed geometry Koszulity via FM purity | C | LOW | PAPER | MHS for FM on higher-genus curves |

### Findings Summary

| # | Finding | Severity | Remedy Scale |
|---|---------|----------|-------------|
| F1 | Module theory orphanage (16 uninstantiated theorems) | CRITICAL | ~10 pages |
| F2 | Genus >= 2 wall (no non-free bar differential at g >= 2) | CRITICAL | ~15 pages |
| F3 | Type-A monoculture (no non-simply-laced bar complex) | MAJOR | ~5 pages |
| F4 | A-infinity mirage (only m_3 for Virasoro computed) | MAJOR | ~8 pages |
| F5 | Geometric-algebraic bar comparison gap | MAJOR | ~3 pages |
| F6 | Lurie HA undercited | MAJOR | ~1 hour |
| F7 | Five referee objections (meta) | — | Addressed by F1-F6 |

### Cross-Reference to HORIZON.md

Items H1-H8 are ALL NEW — none appear in the existing HORIZON.md (which has
29 items at Levels A-D, 10 completed). The closest overlap:
- H5 (genus-2 sl_2) is related to but distinct from HORIZON A2 (genus tables)
- H6 (KL via bar-cobar) is related to but distinct from HORIZON B3 (module equivalences)
- H3 (G_2) has no antecedent in HORIZON.md
- H1 (BGG via bar) has no antecedent in HORIZON.md
- H4 (m_4 pentagon) has no antecedent in HORIZON.md
