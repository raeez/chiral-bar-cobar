# Theorem Registry

Generated from 587 `\ClaimStatusProvedHere` claims across 49 `.tex` files.
This registry provides detailed entries for the ~120 most important theorems,
plus a summary of the remaining ~470 by category and file.

---

## Part I: Detailed Entries (Core Theory)

### THE THREE MAIN THEOREMS

---

### [mainthm:bar-cobar-complete]
- file: chapters/theory/introduction.tex:597
- statement: For a Koszul chiral algebra A on a smooth projective curve X, bar and cobar functors are mutually quasi-inverse, forming an adjoint pair that extends to all genera with BD compatibility at genus 0.
- hypotheses: A is a Koszul chiral algebra on a smooth projective curve X; for the cobar side, C is a conilpotent dg chiral coalgebra.
- conclusion: (1) Functorial bar B: ChirAlg -> dgCoalg; (2) Quasi-isomorphisms B(A) ~ A^! and Omega(A^!) ~ A; (3) Adjunction Hom_dgCoalg(B(A),C) ~ Hom_ChirAlg(A,Omega(C)); (4) Genus decomposition B(A) = sum hbar^{2g-2} B_g(A); (5) BD compatibility at g=0.
- category: STRUCTURAL
- proof_uses: [cor:bar-functorial, cor:bar-cobar-inverse, thm:bar-cobar-verdier, thm:CC-acyclicity-higher-genus, thm:deformation-obstruction, lem:quantum-preserves-acyclicity]

### [thm:quantum-complementarity-main]
- file: chapters/theory/higher_genus.tex:3740
- statement: For a chiral Koszul pair (A, A^!), the genus-g quantum correction spaces satisfy Q_g(A) + Q_g(A^!) = H*(M-bar_g, Z(A)), with direct sum decomposition, perfect pairing, and functoriality.
- hypotheses: (A, A^!) is a chiral Koszul pair on a smooth projective curve X over C; A is a BD chiral algebra; A^! is its Koszul dual.
- conclusion: Canonical isomorphism Q_g(A) + Q_g(A^!) = H*(M-bar_g, Z(A)) that is (1) a direct sum with trivial intersection, (2) complementary (deformation <-> obstruction), (3) functorial in Koszul pairs, (4) equipped with a perfect pairing Q_g(A) x Q_g(A^!) -> C via integration over M-bar_g, (5) grading-compatible.
- category: GENUS
- proof_uses: [thm:verdier-duality-operations, thm:bar-cobar-verdier, thm:obstruction-general, thm:kodaira-spencer-chiral-complete, lem:obstruction-class, lem:period-integral, lem:deformation-space, lem:obs-def-pairing, lem:center-cohomology]

### [thm:higher-genus-inversion]
- file: chapters/theory/higher_genus.tex:6324
- statement: The bar-cobar inversion quasi-isomorphism holds at each genus g: psi_g: Omega_g(B_g(A)) -> A_g is a quasi-isomorphism.
- hypotheses: A is a chiral algebra on a smooth curve X; the genus-0 bar-cobar inversion (thm:bar-cobar-inversion-qi) is established.
- conclusion: For each genus g >= 0, psi_g is a quasi-isomorphism on M-bar_g.
- category: GENUS
- proof_uses: [thm:bar-cobar-inversion-qi, lem:higher-genus-open-stratum-qi, lem:higher-genus-boundary-qi, lem:extension-across-boundary-qi]

---

### BAR CONSTRUCTION FOUNDATIONS (bar_cobar_construction.tex)

### [thm:bar-nilpotency-complete]
- file: chapters/theory/bar_cobar_construction.tex:563
- statement: The bar differential d = d_internal + d_residue + d_form satisfies d^2 = 0 (strict), with all nine cross-terms cancelling.
- hypotheses: A is a chiral algebra on a smooth curve X; the bar complex is formed from A-sections tensored with logarithmic forms on FM compactifications.
- conclusion: d^2 = 0 strict; three diagonal terms (d_int^2, d_res^2, d_dR^2) and three anticommutators ({d_int,d_res}, {d_int,d_dR}, {d_res,d_dR}) all vanish independently. d_res^2 = 0 by Arnold relations + Borcherds identity.
- category: STRUCTURAL
- proof_uses: [lem:sign-compatibility, thm:arnold-three, thm:normal-crossings]

### [thm:stokes-config]
- file: chapters/theory/bar_cobar_construction.tex:641
- statement: Stokes' theorem holds on compactified configuration spaces for logarithmic forms.
- hypotheses: X smooth curve; FM compactification C-bar_n(X) is a smooth manifold with corners.
- conclusion: Boundary integrals of logarithmic forms reduce to residues at collision divisors.
- category: STRUCTURAL
- proof_uses: [thm:FM, thm:normal-crossings]

### [thm:arnold-three]
- file: chapters/theory/bar_cobar_construction.tex:782
- statement: The Arnold three-term relation dlog(z1-z2) ^ dlog(z2-z3) + cyclic = 0 holds on configuration spaces, encoding d_res^2 = 0.
- hypotheses: Three points z1, z2, z3 on a smooth curve X.
- conclusion: The signed sum of wedge products of logarithmic 1-forms around any triple of points vanishes identically.
- category: STRUCTURAL
- proof_uses: []

### [thm:bar-functorial-complete]
- file: chapters/theory/bar_cobar_construction.tex:1051
- statement: The bar construction B(-) is a functor from chiral algebras to DG coalgebras, preserving quasi-isomorphisms.
- hypotheses: Morphism f: A -> A' of chiral algebras on a smooth curve X.
- conclusion: Functorial chain map B(f): B(A) -> B(A'), compatible with coalgebra structure; preserves quasi-isomorphisms; preserves composition.
- category: FUNCTORIAL
- proof_uses: [thm:bar-nilpotency-complete, lem:bar-induced-chain-map, lem:bar-induced-coalgebra]

### [thm:bar-coalgebra]
- file: chapters/theory/bar_cobar_construction.tex:1237
- statement: B(A) carries a natural coalgebra structure with coproduct from deconcatenation and counit from projection.
- hypotheses: A is an augmented chiral algebra.
- conclusion: (B(A), Delta, epsilon, d) is a DG coalgebra.
- category: STRUCTURAL
- proof_uses: [thm:coassociativity-complete, thm:counit-axioms]

### [thm:coassociativity-complete]
- file: chapters/theory/bar_cobar_construction.tex:1265
- statement: The deconcatenation coproduct on the bar complex is strictly coassociative.
- hypotheses: Bar complex B(A) with deconcatenation coproduct.
- conclusion: (Delta x id) o Delta = (id x Delta) o Delta.
- category: STRUCTURAL
- proof_uses: []

### [thm:bar-differential]
- file: chapters/theory/bar_cobar_construction.tex:1536
- statement: Complete formula for the bar differential with three components.
- hypotheses: Chiral algebra A on a smooth curve X with FM compactification.
- conclusion: d = d_internal + d_residue + d_form, with explicit formulas for each component.
- category: STRUCTURAL
- proof_uses: [thm:FM, thm:log-complex]

### [thm:residue-formula]
- file: chapters/theory/bar_cobar_construction.tex:1835
- statement: Explicit residue formula for the bar differential in terms of iterated residues at collision divisors.
- hypotheses: Chiral algebra A with chiral product mu on a smooth curve X.
- conclusion: d_res(phi_0 x ... x phi_n x omega) = sum_{i<j} +/- Res_{D_{ij}}[...].
- category: COMPUTATIONAL
- proof_uses: [thm:bar-differential, lem:orientation, thm:residue-operations]

### [thm:bar-chiral]
- file: chapters/theory/bar_cobar_construction.tex:1989
- statement: The bar complex is a chiral coalgebra, not merely a DG coalgebra.
- hypotheses: A is a chiral algebra on X valued in D-modules.
- conclusion: B(A) carries a chiral coalgebra structure compatible with the D_X-module structure.
- category: STRUCTURAL
- proof_uses: [thm:bar-coalgebra, thm:bar-differential]

### [thm:bar-cobar-verdier]
- file: chapters/theory/bar_cobar_construction.tex:3126
- statement: Perfect pairing between bar and cobar via Verdier duality: <omega_bar, K_cobar> = int_{C-bar_n(X)} omega_bar ^ iota^* K_cobar.
- hypotheses: A is a chiral algebra, C a chiral coalgebra on X; bar elements are log forms on C-bar_n(X), cobar elements are distributions on C_n(X).
- conclusion: Non-degenerate pairing with differential compatibility <d_bar omega, K> = -<omega, d_cobar K>; realizes Omega(C) = D(B(A^!)).
- category: STRUCTURAL
- proof_uses: [thm:verdier-config, thm:stokes-config, thm:dual-differentials]

### [cor:bar-cobar-inverse]
- file: chapters/theory/bar_cobar_construction.tex:3249
- statement: For Koszul chiral algebras, bar and cobar are mutually quasi-inverse.
- hypotheses: A is chiral Koszul (bar complex has cohomology in a single degree); either B(A) is conilpotent or A is I-adically complete.
- conclusion: Omega(B(A)) ~> A and B(Omega(C)) ~> C are quasi-isomorphisms.
- category: STRUCTURAL
- proof_uses: [thm:bar-cobar-verdier]

### [thm:poincare-verdier]
- file: chapters/theory/bar_cobar_construction.tex:3562
- statement: B(A) = D(Omega(A^!)) where D is Verdier duality and A^! is the Koszul dual.
- hypotheses: A is an augmented chiral algebra on a smooth curve X.
- conclusion: Bar-cobar duality is realized as Poincare-Verdier duality on configuration spaces: log forms (bar) are dual to distributions (cobar).
- category: STRUCTURAL
- proof_uses: [thm:bar-cobar-verdier, thm:verdier-config]

### [thm:cobar-cech]
- file: chapters/theory/bar_cobar_construction.tex:3390
- statement: The geometric cobar complex is quasi-isomorphic to a Cech-type complex.
- hypotheses: C is a chiral coalgebra on X; U is a Leray cover of C-bar_n(X).
- conclusion: Omega(C) ~ Check^*(U, F_C) where F_C is the factorization algebra.
- category: STRUCTURAL
- proof_uses: [thm:normal-crossings]

### [thm:cobar-free]
- file: chapters/theory/bar_cobar_construction.tex:3438
- statement: As a graded chiral algebra (forgetting differential), Omega(C) is the free chiral algebra generated by s^{-1}C-bar.
- hypotheses: C is an augmented chiral coalgebra.
- conclusion: Omega(C) = Free_ch(s^{-1}C-bar) with d_Omega the unique derivation extending the reduced comultiplication.
- category: STRUCTURAL
- proof_uses: []

### [thm:geom-unit]
- file: chapters/theory/bar_cobar_construction.tex:3450
- statement: The unit of the bar-cobar adjunction eta: A -> Omega(B(A)) is geometrically realized by configuration space integrals.
- hypotheses: A is a chiral algebra on X; convergence ensured by nilpotency/completeness.
- conclusion: eta(phi)(z) = sum_n int_{C-bar_{n+1}(X)} phi(z) ^ ev_0^*(B_n(A)) ^ omega_n.
- category: STRUCTURAL
- proof_uses: [thm:bar-cobar-verdier, thm:bar-functorial-complete]

### [thm:fermion-boson-koszul]
- file: chapters/theory/bar_cobar_construction.tex:2914
- statement: The beta-gamma system is the Koszul dual of free fermions (chiral lift of Sym(V)^! = Lambda(V^*)).
- hypotheses: Free fermion algebra F = Lambda^ch(V) with exterior chiral product.
- conclusion: F^! = Sym^ch(V^*) = beta-gamma system. Anticommuting fields <-> symplectic bosons; exterior structure <-> polynomial structure; fermionic <-> bosonic statistics.
- category: COMPUTATIONAL
- proof_uses: []

### [thm:curved-mc-cobar]
- file: chapters/theory/bar_cobar_construction.tex:3651
- statement: The curved Maurer-Cartan equation characterizes genus-g deformations.
- hypotheses: Curved A_infinity algebra with curvature mu_0.
- conclusion: MC elements in B^1(A) correspond to quantum deformations with twisted differential d_alpha^2 = 0 iff twisted curvature is central.
- category: STRUCTURAL
- proof_uses: [thm:central-implies-strict]

### [thm:central-charge-cocycle]
- file: chapters/theory/bar_cobar_construction.tex:3841
- statement: The genus-1 cocycle c_1 = Tr(a x a^*) - kappa * 1 satisfies d^(1) c_1 = 0 and generates all genus-1 central phenomena.
- hypotheses: Heisenberg algebra H_kappa at level kappa; genus-1 bar complex.
- conclusion: [c_1] in H_1^(1)(A) is non-trivial, universal, and generates all genus-1 central extensions.
- category: GENUS
- proof_uses: []

### [thm:deformation-obstruction]
- file: chapters/theory/bar_cobar_construction.tex:4396
- statement: Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)) for chiral algebras with central extensions.
- hypotheses: Chiral algebra A on a curve X with genus-g quantum corrections and curved A_infinity structure.
- conclusion: Complementarity decomposition of moduli cohomology into obstruction and deformation spaces.
- category: GENUS
- proof_uses: [lem:obstruction-class, lem:period-integral, lem:deformation-space, lem:obs-def-pairing, lem:center-cohomology]

### [thm:curvature-central]
- file: chapters/theory/bar_cobar_construction.tex:4629
- statement: For a curved A_infinity algebra, the curvature mu_0 is a mu_1-cycle and mu_1^2 = [mu_0, -]_{mu_2}.
- hypotheses: Curved A_infinity algebra (A, mu_0, mu_1, mu_2, ...).
- conclusion: (1) mu_1(mu_0) = 0; (2) mu_1^2(a) = mu_2(mu_0,a) - mu_2(a,mu_0) for all a.
- category: STRUCTURAL
- proof_uses: []

### [thm:central-implies-strict]
- file: chapters/theory/bar_cobar_construction.tex:5097
- statement: If the curvature mu_0 lies in the center Z(A), then d_bar^2 = 0 strictly.
- hypotheses: Curved chiral algebra (A, m_1, mu_0) with mu_0 in Z(A).
- conclusion: d_bar^2 = 0 strict (not merely up to homotopy).
- category: STRUCTURAL
- proof_uses: [thm:arnold-three, thm:bar-nilpotency-complete]

### [thm:mc-deformations]
- file: chapters/theory/bar_cobar_construction.tex:5451
- statement: MC elements in B^1(A) correspond to quantum deformations / flat connections / twisted differentials.
- hypotheses: Chiral algebra A with curved A_infinity structure.
- conclusion: d_alpha^2 = 0 iff mu_0^alpha = 0 is central; MC elements parametrize flat connections on associated bundles.
- category: STRUCTURAL
- proof_uses: [thm:curvature-central]

### [thm:mc-periods]
- file: chapters/theory/bar_cobar_construction.tex:5487
- statement: MC elements arise from period integrals: alpha_g = int_gamma omega_A, and the MC equation equals the flatness condition.
- hypotheses: Chiral algebra A on a curve X of genus g; connection form omega_A in Omega^1(X, A).
- conclusion: MC equation m_1(alpha) + 1/2 m_2(alpha x alpha) + mu_0 = 0 is equivalent to F_omega = d omega + 1/2 [omega, omega] = 0.
- category: GENUS
- proof_uses: [thm:mc-deformations]

### [thm:genus-zero-strict]
- file: chapters/theory/bar_cobar_construction.tex:5546
- statement: At genus 0, the bar differential satisfies d_0^2 = 0 strictly.
- hypotheses: Chiral algebra A with central curvature.
- conclusion: d_0^2 = 0 strict (no quantum corrections at genus 0).
- category: STRUCTURAL
- proof_uses: [thm:arnold-three]

### [thm:genus-induction-strict]
- file: chapters/theory/bar_cobar_construction.tex:5558
- statement: For chiral algebras with central curvature, d_bar^2 = 0 strictly at ALL genera.
- hypotheses: Chiral algebra A with central curvature at all genera.
- conclusion: d_bar^2 = 0 strict at every genus g >= 0.
- category: GENUS
- proof_uses: [thm:genus-zero-strict, thm:central-implies-strict, thm:obstruction-general]

### [thm:bar-cobar-inversion-qi]
- file: chapters/theory/bar_cobar_construction.tex:6557
- statement: The bar-cobar adjunction counit psi: Omega(B(A)) -> A is a quasi-isomorphism of chiral algebras (not merely chain complexes), with spectral sequence and genus convergence.
- hypotheses: A is a chiral algebra on a Riemann surface X.
- conclusion: (1) psi respects all chiral algebra structure; (2) psi_g is a QI at each genus; (3) the full genus-graded sum converges; (4) spectral sequence with E_1 = bar-cobar complex.
- category: STRUCTURAL
- proof_uses: [thm:bar-cobar-adjunction, thm:bar-functorial-complete, thm:genus-graded-convergence, thm:higher-genus-inversion, thm:bar-cobar-spectral-sequence, thm:spectral-sequence-collapse]

### [thm:bar-cobar-spectral-sequence]
- file: chapters/theory/bar_cobar_construction.tex:6692
- statement: The bar-cobar filtration induces a spectral sequence E_0^{p,q} => H^{p+q}(Omega(B(A))) with explicit page descriptions.
- hypotheses: Bar-cobar filtration on Omega(B(A)) by cobar arity.
- conclusion: E_0 = associated graded, E_1 = internal cohomology, E_2 = bar cohomology, converges to H*(Omega(B(A))).
- category: SPECTRAL
- proof_uses: []

### [thm:spectral-sequence-collapse]
- file: chapters/theory/bar_cobar_construction.tex:6748
- statement: For a Koszul chiral algebra A, the bar-cobar spectral sequence collapses at E_2.
- hypotheses: A is Koszul (bar complex has cohomology concentrated in single degree).
- conclusion: E_2 = E_infinity; all higher differentials d_r = 0 for r >= 2.
- category: SPECTRAL
- proof_uses: [thm:bar-cobar-spectral-sequence]

### [thm:genus-graded-convergence]
- file: chapters/theory/bar_cobar_construction.tex:6766
- statement: Bar-cobar inversion converges at each genus g and converges formally in the hbar-adic completion.
- hypotheses: A is a chiral algebra; genus series psi = sum hbar^{2g-2} psi_g.
- conclusion: (1) psi_0 is a QI (BD); (2) each psi_g is a QI; (3) psi converges in hbar-adic completion.
- category: SPECTRAL
- proof_uses: [thm:BD-genus-zero, lem:pushforward-preserves-qi]

### [thm:bar-cobar-inversion-functorial]
- file: chapters/theory/bar_cobar_construction.tex:6893
- statement: The QI psi: Omega(B(A)) -> A is functorial in A.
- hypotheses: Morphism f: A -> A' of chiral algebras.
- conclusion: The diagram Omega(B(A)) -> A and Omega(B(A')) -> A' commutes with the induced maps.
- category: FUNCTORIAL
- proof_uses: [thm:bar-functorial-complete, thm:bar-cobar-adjunction]

### [cor:derived-equivalence-bar-cobar]
- file: chapters/theory/bar_cobar_construction.tex:6928
- statement: Bar and cobar induce an equivalence of derived categories D^b(Mod(A)) ~ D^b(Comod(A^!)).
- hypotheses: A is Koszul chiral algebra on X, augmented over O_X, locally finitely generated as D_X-module; modules are BD chiral modules; comodules are conilpotent A^!-comodules.
- conclusion: Equivalence of triangulated categories via bar extension of scalars and cobar restriction.
- category: FUNCTORIAL
- proof_uses: [thm:bar-cobar-inversion-qi, thm:spectral-sequence-collapse, prop:counit-qi]

### [thm:bar-functorial-grothendieck]
- file: chapters/theory/bar_cobar_construction.tex:5846
- statement: Functoriality of bar construction in the Grothendieck sense.
- hypotheses: Chiral algebra A on a smooth curve X.
- conclusion: Bar construction is a functor compatible with the six-functor formalism on D-modules.
- category: FUNCTORIAL
- proof_uses: [thm:bar-functorial-complete]

### [cor:genus-expansion-converges]
- file: chapters/theory/bar_cobar_construction.tex:5779
- statement: The genus expansion of the bar complex converges in the hbar-adic completion.
- hypotheses: Chiral algebra A with central curvature at all genera.
- conclusion: The formal series B(A) = sum hbar^{2g-2} B_g(A) converges in the I-adic completion.
- category: GENUS
- proof_uses: [thm:genus-induction-strict, thm:central-implies-strict]

---

### CONFIGURATION SPACES (configuration_spaces.tex)

### [thm:FM]
- file: chapters/theory/configuration_spaces.tex:65
- statement: The FM compactification C-bar_n(X) of C_n(X) exists as a smooth variety with normal crossings boundary, functorial in X, for curves of any genus g.
- hypotheses: X is a smooth curve (or more generally n-dimensional manifold); n >= 2 points.
- conclusion: C-bar_n(X) is a smooth variety with corners; boundary divisors D_S (indexed by subsets |S| >= 2) have normal crossings; functorial in X.
- category: STRUCTURAL
- proof_uses: []

### [thm:normal-crossings]
- file: chapters/theory/configuration_spaces.tex:390
- statement: Boundary divisors of the FM compactification have normal crossings.
- hypotheses: FM compactification C-bar_n(X) of a smooth curve X.
- conclusion: The boundary divisors D_S intersect transversally; local coordinates are products of radial and angular parts.
- category: STRUCTURAL
- proof_uses: [thm:FM, thm:local-coords-boundary]

### [thm:log-complex]
- file: chapters/theory/configuration_spaces.tex:588
- statement: The logarithmic complex Omega^*_log(C-bar_n(X)) computes the cohomology of C_n(X).
- hypotheses: FM compactification with normal crossings boundary.
- conclusion: H*(C_n(X)) = H*(C-bar_n(X), Omega^*_log).
- category: STRUCTURAL
- proof_uses: [thm:normal-crossings]

### [thm:arnold-relations]
- file: chapters/theory/configuration_spaces.tex:627
- statement: Arnold relations: dlog(z_i - z_j) ^ dlog(z_j - z_k) + cyclic = 0.
- hypotheses: Three distinct points on a smooth curve X.
- conclusion: The three 2-forms sum to zero; this generates all relations in H^*(C_n(X)).
- category: STRUCTURAL
- proof_uses: []

### [thm:residue-operations]
- file: chapters/theory/configuration_spaces.tex:732
- statement: Residue operations on logarithmic forms are well-defined and compatible with the boundary stratification.
- hypotheses: Log forms on FM compactification; normal crossings boundary.
- conclusion: Res_D: Omega^k_log -> Omega^{k-1}_log|_D is well-defined; compatible with iterated residues.
- category: STRUCTURAL
- proof_uses: [thm:log-complex, thm:normal-crossings]

### [thm:residue-sequence]
- file: chapters/theory/configuration_spaces.tex:836
- statement: The residue exact sequence for logarithmic forms on FM compactifications.
- hypotheses: Normal crossings boundary D = union D_S in C-bar_n(X).
- conclusion: 0 -> Omega^k -> Omega^k(log D) -> direct-sum Omega^{k-1}_{D_S}(log D') -> 0.
- category: STRUCTURAL
- proof_uses: [thm:normal-crossings]

### [thm:arnold-jacobi]
- file: chapters/theory/configuration_spaces.tex:2699
- statement: Arnold relations = Jacobi identity: the three-term Arnold relation for logarithmic forms is equivalent to the Jacobi identity for the chiral Lie bracket.
- hypotheses: Configuration space C_3(X) on a smooth curve X.
- conclusion: Arnold 3-term relation encodes the Jacobi identity [a,[b,c]] + cyclic = 0.
- category: STRUCTURAL
- proof_uses: [thm:arnold-relations]

### [thm:normal-crossings-preservation]
- file: chapters/theory/configuration_spaces.tex:2847
- statement: Normal crossings are preserved under fiber products and blowups relevant to the bar construction.
- hypotheses: FM compactifications of configuration spaces on smooth curves.
- conclusion: All intersection patterns in the bar complex boundary are normal crossing.
- category: STRUCTURAL
- proof_uses: [thm:normal-crossings, lem:fiber-product-NC]

---

### HIGHER GENUS (higher_genus.tex)

### [thm:bar-ainfty-complete]
- file: chapters/theory/higher_genus.tex:120
- statement: The geometric bar complex carries a natural A_infinity structure with m_k given by sums over planar binary trees of residues at boundary strata.
- hypotheses: Chiral algebra A on a smooth curve X; FM compactification C-bar_k(X) with boundary stratification.
- conclusion: Operations m_k from residues at codimension-(k-1) strata; m_1 = 0, m_2 = chiral product, m_3 = associativity obstruction; A_infinity relations from d^2 = 0 on boundaries.
- category: STRUCTURAL
- proof_uses: [thm:FM, thm:normal-crossings, thm:stokes-config]

### [thm:ainfty-moduli]
- file: chapters/theory/higher_genus.tex:185
- statement: Bar complex A_infinity operations are given by integration over M-bar_{0,k+1} boundaries.
- hypotheses: Bar complex of a chiral algebra; DM compactification M-bar_{0,k+1}.
- conclusion: m_k(omega_1,...,omega_k) = int_{partial M-bar_{0,k+1}} pi^*(omega_1 ^...^ omega_k) ^ Omega_{0,k+1}.
- category: STRUCTURAL
- proof_uses: [thm:bar-ainfty-complete]

### [thm:verdier-duality-operations]
- file: chapters/theory/higher_genus.tex:572
- statement: Verdier duality exchanges the bar A_infinity operations with the cobar A_infinity operations.
- hypotheses: Chiral Koszul pair (A, A^!) on X.
- conclusion: m_k^bar and m_k^cobar are Verdier dual under the configuration space pairing.
- category: STRUCTURAL
- proof_uses: [thm:bar-ainfty-complete, thm:bar-cobar-verdier]

### [thm:obstruction-general]
- file: chapters/theory/higher_genus.tex:3031
- statement: The genus-g obstruction is obs_g = sum_{g1+g2=g, g1,g2>=1} d_{g1} o d_{g2}, with [obs_g] in H^2(B_0(A), Z(A)).
- hypotheses: Chiral algebra A with genus decomposition of the bar differential d_total = sum hbar^{2g-2} d_g.
- conclusion: The obstruction class [obs_g] is well-defined, independent of choices, and lands in the center Z(A). d_g exists iff obs_g is a d_0-coboundary.
- category: GENUS
- proof_uses: [thm:arnold-three]

### [thm:heisenberg-obs]
- file: chapters/theory/higher_genus.tex:3081
- statement: For Heisenberg H_kappa, obs_g = kappa * lambda_g in H^{2g}(M-bar_g).
- hypotheses: Heisenberg vertex algebra H_kappa at level kappa; genus g >= 1.
- conclusion: obs_g = kappa * c_g(E) where E is the Hodge bundle. Vanishes iff kappa = 0.
- category: COMPUTATIONAL
- proof_uses: [thm:obstruction-general]

### [thm:kac-moody-obs]
- file: chapters/theory/higher_genus.tex:3164
- statement: For affine KM g-hat_k, obs_g = (k+h^v)*dim(g)/(2h^v) * lambda_g.
- hypotheses: Affine KM vertex algebra g-hat_k at level k != -h^v.
- conclusion: Explicit formula for obstruction at each genus; vanishes at critical level k = -h^v.
- category: COMPUTATIONAL
- proof_uses: [thm:obstruction-general, thm:heisenberg-obs]

### [thm:w3-obstruction]
- file: chapters/theory/higher_genus.tex:3281
- statement: W_3 obstruction at genus g with explicit central charge dependence.
- hypotheses: W_3 algebra at central charge c.
- conclusion: obs_g depends on c through the T and W generators with specific coefficients.
- category: COMPUTATIONAL
- proof_uses: [thm:obstruction-general]

### [thm:genus-universality]
- file: chapters/theory/higher_genus.tex:3436
- statement: For every Koszul chiral algebra A, obs_g(A) = kappa(A) * lambda_g with kappa genus-independent.
- hypotheses: A is a Koszul chiral algebra.
- conclusion: (i) Explicit values: kappa(H_kappa) = kappa, kappa(g-hat_k) = (k+h^v)dim(g)/(2h^v), kappa(Vir_c) = c/2; (ii) kappa(A^!) = -kappa(A); (iii) F_g = kappa * (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!.
- category: GENUS
- proof_uses: [thm:heisenberg-obs, thm:kac-moody-obs, thm:quantum-complementarity-main]

### [cor:kappa-additivity]
- file: chapters/theory/higher_genus.tex:3481
- statement: kappa(A tensor B) = kappa(A) + kappa(B) for Koszul chiral algebras.
- hypotheses: A, B Koszul chiral algebras with A tensor B Koszul.
- conclusion: Obstruction coefficient is additive under tensor product.
- category: GENUS
- proof_uses: [thm:genus-universality]

### [cor:critical-level-universality]
- file: chapters/theory/higher_genus.tex:3498
- statement: Critical level (kappa(A) = 0) characterized: obs_g = 0 for all g iff kappa = 0.
- hypotheses: Koszul chiral algebra A.
- conclusion: A is at critical level iff all genus obstructions vanish.
- category: GENUS
- proof_uses: [thm:genus-universality]

### [thm:self-dual-halving]
- file: chapters/theory/higher_genus.tex:4935
- statement: If A = A^! (self-dual), then dim Q_g(A) = 1/2 dim H*(M-bar_g, Z(A)).
- hypotheses: (A, A^!) is a Koszul chiral pair with A = A^! as chiral algebras.
- conclusion: dim Q_g(A) = dim Q_g(A^!) = 1/2 dim H*(M-bar_g, Z(A)); in particular dim H*(M-bar_g, Z(A)) is even.
- category: GENUS
- proof_uses: [thm:quantum-complementarity-main]

### [thm:kodaira-spencer-chiral-complete]
- file: chapters/theory/higher_genus.tex:4290
- statement: There exists a Kodaira-Spencer map for chiral algebras: rho: Z(A) -> End(H*(M-bar_g, Z(A))) from the Gauss-Manin connection, anti-commuting with Verdier duality.
- hypotheses: (A, A^!) is a chiral Koszul pair; pi: C_g -> M-bar_g is the universal curve.
- conclusion: Center Z(A) acts on H*(M-bar_g, Z(A)) via the Gauss-Manin connection on chiral homology; this action anti-commutes with Verdier duality: D o nabla^z = -nabla^z o D.
- category: GENUS
- proof_uses: [thm:quantum-complementarity-main]

### [thm:ss-genus-stratification]
- file: chapters/theory/higher_genus.tex:4705
- statement: The bar-cobar spectral sequence stratifies by genus.
- hypotheses: Chiral Koszul pair (A, A^!) with genus decomposition.
- conclusion: Spectral sequence with E_1 = genus-graded pieces, converging to total quantum corrections.
- category: SPECTRAL
- proof_uses: [thm:bar-cobar-spectral-sequence]

### [thm:BD-genus-zero]
- file: chapters/theory/higher_genus.tex:5419
- statement: BD 3.4.12: Chevalley-Cousin complex is acyclic at genus 0.
- hypotheses: Smooth projective curve X; chiral algebra A.
- conclusion: H^i(R(X), C(A)) = A for i=0, 0 otherwise.
- category: STRUCTURAL
- proof_uses: []

### [thm:CC-acyclicity-higher-genus]
- file: chapters/theory/higher_genus.tex:5524
- statement: Chevalley-Cousin acyclicity extends to higher genus.
- hypotheses: Chiral algebra A on a smooth curve X of genus g; quantum-corrected differential d_g.
- conclusion: H^i(R(Sigma_g), C(A)) = A for i=0, 0 otherwise; quantum corrections preserve acyclicity.
- category: GENUS
- proof_uses: [thm:BD-genus-zero, thm:quantum-diff-squares-zero, lem:quantum-preserves-acyclicity, thm:normal-crossings-persist, prop:factorization-over-moduli]

### [thm:quantum-diff-squares-zero]
- file: chapters/theory/higher_genus.tex:5717
- statement: The quantum-corrected differential d_g = d_0 + sum t_k d_k satisfies d_g^2 = 0.
- hypotheses: Chiral algebra A on a genus-g curve; d_k correction operators from A-cycle period integrals.
- conclusion: d_g^2 = 0; vanishing follows from d_0^2 = 0, Fubini theorem for mixed terms, and A-cycle Lagrangian property for quantum terms.
- category: GENUS
- proof_uses: [thm:bar-nilpotency-complete]

### [thm:verdier-AF-compat]
- file: chapters/theory/higher_genus.tex:5927
- statement: Geometric-topological duality compatibility: geometric Verdier duality specializes to topological (AF) duality.
- hypotheses: Chiral algebra A valued in holonomic D-modules on X.
- conclusion: The Verdier duality of D-modules specializes via de Rham to the Ayala-Francis non-abelian Poincare duality.
- category: STRUCTURAL
- proof_uses: [thm:bar-computes-dual, lem:DR-verdier-compat, lem:ran-duality-AF, lem:bar-as-fact-hom-AF, lem:coalgebra-verdier-AF, lem:diagram-commutes-AF]

### [cor:bar-is-fh]
- file: chapters/theory/higher_genus.tex:6074
- statement: The bar complex computes factorization homology: B(A) ~ int_X A.
- hypotheses: Chiral algebra A on a smooth curve X valued in holonomic D-modules.
- conclusion: The bar complex is quasi-isomorphic to Ayala-Francis factorization homology.
- category: STRUCTURAL
- proof_uses: [thm:verdier-AF-compat, lem:bar-as-fact-hom-AF]

### [thm:genus-graded-koszul]
- file: chapters/theory/higher_genus.tex:6411
- statement: Genus-graded Koszul duality: the genus tower is a compatible system of Koszul dualities.
- hypotheses: (A, A^!) is a genus-0 Koszul pair with central curvature at all genera; modular Koszulity (diagonal Ext vanishing at each genus); convergence in hbar-adic topology.
- conclusion: A^! is genus-graded Koszul, (A^!)^! = A in C[[hbar]]-modules, and the genus tower is a compatible system.
- category: GENUS
- proof_uses: [thm:higher-genus-inversion, thm:genus-universality]

---

### POINCARE DUALITY (poincare_duality.tex)

### [thm:dual-differentials]
- file: chapters/theory/poincare_duality.tex:159
- statement: Under Verdier duality, Res_{D_ij} (bar) is dual to delta_{ij} (cobar), collapse is dual to split, and composition product is dual to coproduct.
- hypotheses: Configuration spaces C_k(X) with FM compactification.
- conclusion: <Res_D(omega), K> = <omega, delta_D(K)> for all bar elements omega and cobar elements K.
- category: STRUCTURAL
- proof_uses: [thm:verdier-config]

### [thm:coalgebra-via-NAP]
- file: chapters/theory/poincare_duality.tex:269
- statement: The Verdier dual construction of A^! yields a well-defined conilpotent chiral coalgebra.
- hypotheses: A is an augmented chiral algebra on X with conformal weight grading.
- conclusion: (A^!, Delta, epsilon, d) satisfies coassociativity, counit, coderivation, and conilpotency axioms.
- category: STRUCTURAL
- proof_uses: [thm:verdier-config]

### [thm:bar-computes-dual]
- file: chapters/theory/poincare_duality.tex:338
- statement: B(A) ~ A^! where A^! is the Verdier dual chiral coalgebra (NAP construction).
- hypotheses: A is an augmented chiral algebra on X valued in holonomic D-modules; configuration-space pushforwards well-defined in derived category.
- conclusion: Canonical QI of chiral coalgebras Phi: B(A) -> A^!; Phi respects all coalgebra structures and is functorial.
- category: STRUCTURAL
- proof_uses: [thm:dual-differentials, thm:coalgebra-via-NAP, thm:verdier-config]

---

### CHIRAL KOSZUL PAIRS (chiral_koszul_pairs.tex)

### [thm:yangian-self-dual]
- file: chapters/theory/chiral_koszul_pairs.tex:271
- statement: Y(g)^! = Y_{R^{-1}}(g) = Y(g)^{hbar -> -hbar}; for simply-laced g, the Yangian is Koszul self-dual.
- hypotheses: Yangian Y(g) in RTT presentation; Yang R-matrix.
- conclusion: Koszul dual is the RTT algebra with R^{-1}; for simply-laced g, Y(g)^! = Y(g).
- category: STRUCTURAL
- proof_uses: []

### [thm:bar-computes-koszul-dual-complete]
- file: chapters/theory/chiral_koszul_pairs.tex:615
- statement: For a chiral Koszul pair (A_1, A_2), completed bar complex of A_1 is QI to A_2^! as chiral coalgebras.
- hypotheses: (A_1, A_2) is a chiral Koszul pair.
- conclusion: Phi: hat{B(A_1)} ~> A_2^! respects all coalgebra structures; functorial; reduces to classical for quadratic; completion essential for non-quadratic.
- category: STRUCTURAL
- proof_uses: [thm:bar-cobar-verdier]

### [thm:feynman-bar-cobar]
- file: chapters/theory/chiral_koszul_pairs.tex:1393
- statement: Feynman diagrams of genus g / symmetries = C_*(g)(A): the bar complex computes the Feynman diagram expansion.
- hypotheses: Chiral algebra A; modular operad {M-bar_{g,n}}.
- conclusion: Feynman integrals <-> bar complex operations; loop momenta <-> config space integration; renormalization <-> homological perturbation; g-loop divergences <-> H_*^(g)(A).
- category: GENUS
- proof_uses: [thm:prism-higher-genus]

### [thm:e1-chiral-koszul-duality]
- file: chapters/theory/chiral_koszul_pairs.tex:1491
- statement: E_1-chiral Koszul duality: bar-cobar adjunction is an equivalence of infinity-categories between augmented pro-nilpotent chirAss-algebras and coaugmented conilpotent chirAss-coalgebras.
- hypotheses: chirAss is the associative chiral operad; V = D-mod(X) with chiral tensor product; Ass is Koszul.
- conclusion: B: chirAss-Alg^{aug,pronil} <-> chirAss-CoAlg^{coaug,conil} :Omega with unit and counit QIs.
- category: FUNCTORIAL
- proof_uses: [prop:chirAss-self-dual]

### [thm:module-category-equivalence]
- file: chapters/theory/chiral_koszul_pairs.tex:1677
- statement: For a Koszul pair (A_1, A_2): derived equivalence D^b(A_1-mod) ~ D^b(A_2-mod)^op; Ext-Tor duality; simple-projective correspondence; Hochschild cohomology duality.
- hypotheses: (A_1, A_2) form a Koszul pair of chiral algebras.
- conclusion: (1) RHom_{A_1}(A_2,-) is a derived equivalence; (2) Ext^i_{A_1} = Tor_i^{A_2}*; (3) simples <-> projectives; (4) HH*(A_1,M) = HH_{d-*}(A_2, RHom(A_2,M)).
- category: FUNCTORIAL
- proof_uses: [cor:derived-equivalence-bar-cobar, thm:bar-cobar-inversion-qi]

### [thm:e1-module-koszul-duality]
- file: chapters/theory/chiral_koszul_pairs.tex:1737
- statement: E_1-module Koszul duality: D(Mod^{E1,compl}_A) ~ D(CoMod^{E1,conil}_{A^!}).
- hypotheses: A is a Koszul E_1-chiral algebra with Koszul dual A^! = B(A).
- conclusion: Derived equivalence; simples <-> injective comodules; Ext exchange; character computation via Koszul resolution.
- category: FUNCTORIAL
- proof_uses: [thm:e1-chiral-koszul-duality]

### [thm:structure-exchange]
- file: chapters/theory/chiral_koszul_pairs.tex:1862
- statement: Koszul duality exchanges generators with relations, products with coproducts, and syzygies with cosyzygies.
- hypotheses: Koszul pair (A_1, A_2) of chiral algebras.
- conclusion: Gen(A_1) <-> Rel(A_2)^perp; Rel(A_1) <-> Gen(A_2)^perp; multiplication <-> comultiplication; Syz^n(A_1) <-> CoSyz^{n+1}(B(A_2)).
- category: STRUCTURAL
- proof_uses: []

### [thm:ainfty-duality-exchange]
- file: chapters/theory/chiral_koszul_pairs.tex:1903
- statement: A_infinity structures interchange under Koszul duality: trivial A_inf (Com) <-> maximal A_inf (Lie); Massey products <-> coMassey products.
- hypotheses: Koszul dual pair (A_1, A_2).
- conclusion: Com^! = Lie duality; m_k^(1) detected by m_k^(2) via config space pairing.
- category: STRUCTURAL
- proof_uses: [thm:verdier-duality-operations, thm:bar-cobar-verdier]

### [thm:curved-koszul-pairs]
- file: chapters/theory/chiral_koszul_pairs.tex:1959
- statement: Curved Koszul pair theory: curvature on one side corresponds to curved A_infinity structure on the dual.
- hypotheses: Curved chiral algebra A with curvature mu_0 in Z(A).
- conclusion: Bar-cobar correspondence extends to curved setting; curvature encodes higher-genus quantum corrections.
- category: STRUCTURAL
- proof_uses: [thm:central-implies-strict, thm:curvature-central]

---

### POINCARE DUALITY QUANTUM (poincare_duality_quantum.tex)

### [thm:prism-operadic]
- file: (referenced throughout; definitions in poincare_duality_quantum.tex)
- statement: Genus-0 chiral operad is QI to HyCom, whose Koszul dual cooperad is Grav^c. The bar complex decomposes A into its operadic spectrum with respect to Grav^c.
- hypotheses: Chiral operad at genus 0.
- conclusion: Operadic Koszul duality via HyCom-Grav duality (Getzler).
- category: STRUCTURAL
- proof_uses: []

### [thm:prism-higher-genus]
- file: (referenced throughout; poincare_duality_quantum.tex)
- statement: At higher genus, bar-cobar extends to the Feynman transform of the modular operad {M-bar_{g,n}}.
- hypotheses: Modular operad structure on {M-bar_{g,n}} (Getzler-Kapranov).
- conclusion: Bar complex at genus g is computed by Feynman transform; MCG-equivariant.
- category: GENUS
- proof_uses: []

---

### INTRODUCTION (introduction.tex)

### [mainthm:curved-complete]
- file: chapters/theory/introduction.tex:648
- statement: Curved Koszul duality for chiral algebras: obstruction theory, deformation-obstruction duality, and completion.
- hypotheses: Chiral algebras with central extensions (curved A_infinity structures).
- conclusion: Q_g in H^2(B_g, Z(A)); Q_g(A) + Q_g(A^!) = H*(M-bar_g, Z(A)); hat{A^!} via nilpotent completion.
- category: GENUS
- proof_uses: [lem:obstruction-class, thm:deformation-obstruction]

### [mainthm:NAP-complete]
- file: chapters/theory/introduction.tex:721
- statement: Bar-cobar duality is mediated by Verdier duality on configuration spaces: B(A) ~ int_X A (factorization homology), Omega(C) ~ D(int_{-X} C).
- hypotheses: Chiral algebra A valued in holonomic D-modules.
- conclusion: Bar = factorization homology; cobar = Verdier dual; geometric and topological dualities are compatible.
- category: STRUCTURAL
- proof_uses: [lem:bar-as-fact-hom-AF, thm:bar-cobar-verdier, thm:verdier-AF-compat]

### [cor:explicit-pairs-intro]
- file: chapters/theory/introduction.tex:760
- statement: Explicit Koszul pairs: free fermion <-> beta-gamma; Heisenberg <-> curved DG Sym^ch; g-hat_k <-> CE_ch^*(g); W_N <-> Wakimoto.
- hypotheses: Each of the named algebras.
- conclusion: Four families of Koszul dual pairs.
- category: COMPUTATIONAL
- proof_uses: [thm:fermion-boson-koszul, thm:heisenberg-koszul-dual-early, thm:sl2-koszul-dual, thm:universal-kac-moody-koszul, thm:w-algebra-koszul]

### [thm:central-charge-complementarity]
- file: chapters/theory/introduction.tex:785
- statement: For Koszul dual pairs related by Feigin-Frenkel involution k -> k' = -k - 2h^v, the sum of central charges is independent of level.
- hypotheses: Koszul dual pair related by FF involution.
- conclusion: c(A) + c(A^!) = c_crit (independent of level).
- category: COMPUTATIONAL
- proof_uses: [thm:quantum-complementarity-main, thm:genus-universality]

### [thm:existence-koszul]
- file: chapters/theory/introduction.tex:1033
- statement: Existence criterion for chiral Koszul duality.
- hypotheses: Chiral algebra A satisfying finiteness and generation conditions.
- conclusion: Koszul dual exists and bar complex computes it.
- category: STRUCTURAL
- proof_uses: []

---

### DEFORMATION THEORY (deformation_theory.tex)

### [thm:hochschild-chain-complex]
- file: chapters/theory/deformation_theory.tex:65
- statement: The chiral Hochschild differential d = d_int + d_fact + d_config satisfies d^2 = 0.
- hypotheses: Chiral algebra A on a smooth curve X; cochains defined via FM compactification with log forms.
- conclusion: d^2 = 0 from d_int^2 = 0 (D-module), d_config^2 = 0 (de Rham), d_fact^2 = 0 (chiral associativity), and mixed terms cancel by Arnold-OS relations.
- category: STRUCTURAL
- proof_uses: [thm:arnold-relations]

### [cor:def-obs-exchange-genus0]
- file: chapters/theory/deformation_theory.tex:411
- statement: Deformation-obstruction exchange at genus 0 via Koszul duality.
- hypotheses: Koszul pair (A, A^!) at genus 0.
- conclusion: Def(A) = Obs(A^!), Obs(A) = Def(A^!).
- category: STRUCTURAL
- proof_uses: [thm:quantum-complementarity-main]

---

### CHIRAL MODULES (chiral_modules.tex)

### [thm:BGG-bar]
- file: chapters/theory/chiral_modules.tex:2308
- statement: BGG resolution arises from the bar complex.
- hypotheses: Koszul chiral algebra A with simple module L.
- conclusion: BGG resolution of L by Verma modules is the bar resolution.
- category: FUNCTORIAL
- proof_uses: [thm:module-category-equivalence]

### [thm:ds-koszul-intertwine]
- file: chapters/theory/chiral_modules.tex:3378
- statement: Drinfeld-Sokolov reduction intertwines with Koszul duality.
- hypotheses: Affine KM g-hat_k; DS reduction functor.
- conclusion: DS(B(g-hat_k)) = B(W(g,k)); DS commutes with bar construction.
- category: FUNCTORIAL
- proof_uses: [thm:universal-kac-moody-koszul, thm:w-algebra-koszul]

---

## Part II: Detailed Entries (Examples)

### FREE FIELDS (free_fields.tex)

### [thm:heisenberg-koszul-dual-early]
- file: chapters/examples/free_fields.tex:742
- statement: Heisenberg Koszul dual: H_k^! = Sym^ch(V^*) with curved structure.
- hypotheses: Heisenberg vertex algebra H_k at level k.
- conclusion: H_k^! is the commutative chiral algebra Sym^ch(V^*); the bar complex is curved with curvature proportional to k.
- category: COMPUTATIONAL
- proof_uses: [thm:fermion-boson-koszul]

### [thm:betagamma-bc-koszul]
- file: chapters/examples/free_fields.tex:243
- statement: beta-gamma and bc systems are Koszul dual (2-generator duality).
- hypotheses: beta-gamma system (bosonic) and bc ghost system (fermionic) with dim V = 2.
- conclusion: bc^! = beta-gamma; this is the 2-generator version of the Lie-Com duality.
- category: COMPUTATIONAL
- proof_uses: [thm:fermion-boson-koszul, prop:bc-betagamma-orthogonality]

### [thm:heisenberg-genus-g]
- file: chapters/examples/free_fields.tex:2560
- statement: Quantum complementarity for Heisenberg at all genera.
- hypotheses: Heisenberg H_kappa at level kappa; all genera g >= 1.
- conclusion: Q_g(H_kappa) + Q_g(H_kappa^!) = H*(M-bar_g, C); obstruction = kappa * lambda_g.
- category: COMPUTATIONAL
- proof_uses: [thm:quantum-complementarity-main, thm:heisenberg-obs]

### [thm:heisenberg-bar-complete]
- file: chapters/examples/free_fields.tex:2697
- statement: Complete calculation of Heisenberg bar complex at all genera.
- hypotheses: Heisenberg H_kappa at level kappa.
- conclusion: Explicit formulas for B_g(H_kappa) including Eisenstein series contributions at genus 1.
- category: COMPUTATIONAL
- proof_uses: [thm:heisenberg-obs, thm:genus-universality]

### [thm:heisenberg-level-inversion]
- file: chapters/examples/free_fields.tex:2778
- statement: Heisenberg level inversion via curved duality.
- hypotheses: Heisenberg H_k and its dual H_k^! = Sym^ch(V^*).
- conclusion: Level inversion k <-> -k manifests as curvature exchange in the bar-cobar duality.
- category: COMPUTATIONAL
- proof_uses: [thm:heisenberg-koszul-dual-early, thm:deformation-obstruction]

### [thm:virasoro-moduli]
- file: chapters/examples/free_fields.tex:1410
- statement: Virasoro-moduli correspondence: Virasoro algebra controls deformations of M_g.
- hypotheses: Virasoro algebra Vir_c at central charge c.
- conclusion: Virasoro bar complex computes H*(M-bar_g) with Virasoro action.
- category: GENUS
- proof_uses: [thm:genus-universality]

### [thm:modular-invariance]
- file: chapters/examples/free_fields.tex:3138
- statement: Modular invariance of the bar complex.
- hypotheses: Chiral algebra A with well-defined genus-g bar complex.
- conclusion: Bar complex B_g(A) carries an action of MCG(Sigma_g) compatible with the chiral structure.
- category: GENUS
- proof_uses: [thm:prism-higher-genus]

---

### KAC-MOODY (kac_moody_framework.tex)

### [thm:level-shifting-abstract]
- file: chapters/examples/kac_moody_framework.tex:223
- statement: Level-shifting duality: g-hat_k^! = g-hat_{-k-2h^v} (abstract form).
- hypotheses: Affine KM algebra g-hat_k at level k != -h^v.
- conclusion: Koszul dual is the same affine algebra at dual level k' = -k - 2h^v.
- category: COMPUTATIONAL
- proof_uses: [thm:universal-kac-moody-koszul]

### [thm:sl2-koszul-dual]
- file: chapters/examples/kac_moody_framework.tex:339
- statement: Explicit Koszul dual of sl2-hat at level k.
- hypotheses: Affine sl2-hat at level k.
- conclusion: sl2-hat_k^! = sl2-hat_{-k-4} with explicit bar complex.
- category: COMPUTATIONAL
- proof_uses: [thm:level-shifting-abstract]

### [thm:universal-kac-moody-koszul]
- file: chapters/examples/kac_moody_framework.tex:498
- statement: Universal Koszul duality for affine KM: g-hat_k^! = CE_ch^*(g) at the Koszul dual level.
- hypotheses: Affine KM g-hat_k at level k for any simple Lie algebra g.
- conclusion: The Koszul dual is the chiral Chevalley-Eilenberg algebra at dual level.
- category: COMPUTATIONAL
- proof_uses: [thm:sl2-koszul-dual, thm:sl3-koszul-dual]

### [thm:screening-bar]
- file: chapters/examples/kac_moody_framework.tex:594
- statement: Screening charges implement the bar differential.
- hypotheses: Affine KM g-hat_k with Wakimoto realization.
- conclusion: d_bar = sum Q_i (screening operators); bar cohomology = kernel of screening charges.
- category: COMPUTATIONAL
- proof_uses: [thm:wakimoto-koszul]

### [thm:w-algebra-koszul]
- file: chapters/examples/kac_moody_framework.tex:645
- statement: W-algebra Koszul duality at critical level.
- hypotheses: W-algebra W(g) at critical level from DS reduction of g-hat at critical level.
- conclusion: W(g)^! is computed by the bar complex of the DS reduction.
- category: COMPUTATIONAL
- proof_uses: [thm:universal-kac-moody-koszul]

---

### W-ALGEBRAS (w_algebras_framework.tex)

### [thm:w-algebra-koszul-main]
- file: chapters/examples/w_algebras_framework.tex:38
- statement: W-algebra Koszul duality for principal nilpotent: W^k(g)^! = W^{k'}(g^L) where k' = -k - 2h^v.
- hypotheses: W^k(g) at level k for principal nilpotent; g^L is Langlands dual.
- conclusion: Koszul dual is W-algebra of Langlands dual at shifted level.
- category: COMPUTATIONAL
- proof_uses: [thm:universal-kac-moody-koszul]

### [thm:w-koszul-precise]
- file: chapters/examples/w_algebras_framework.tex:578
- statement: Precise Koszul duality for W-algebras with explicit bar complex.
- hypotheses: W(g,k) at non-critical level.
- conclusion: Bar complex with generators, differential, and coalgebra structure fully specified.
- category: COMPUTATIONAL
- proof_uses: [thm:w-algebra-koszul-main, thm:w-bar-curvature]

### [thm:w3-koszul-dual]
- file: chapters/examples/w_algebras_framework.tex:1167
- statement: Koszul dual of W_3 algebra: explicit computation.
- hypotheses: W_3 algebra at central charge c.
- conclusion: W_3^! with explicit generators, relations, and central charge shift.
- category: COMPUTATIONAL
- proof_uses: [thm:w-koszul-precise]

---

### GENUS EXPANSIONS (genus_expansions.tex)

### [thm:heisenberg-all-genera]
- file: chapters/examples/genus_expansions.tex:8
- statement: Complete Heisenberg genus expansion at all genera.
- hypotheses: Heisenberg H_kappa.
- conclusion: F_g = kappa * (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!.
- category: COMPUTATIONAL
- proof_uses: [thm:genus-universality, thm:heisenberg-obs]

### [thm:sl2-all-genera]
- file: chapters/examples/genus_expansions.tex:289
- statement: sl2-hat free energy at all genera.
- hypotheses: sl2-hat at level k.
- conclusion: F_g^{sl2} = 3(k+2)/4 * Bernoulli formula.
- category: COMPUTATIONAL
- proof_uses: [thm:genus-universality, thm:kac-moody-obs]

### [thm:bernoulli-universality]
- file: chapters/examples/genus_expansions.tex:411
- statement: Bernoulli universality: all genus expansions involve Bernoulli numbers through the same formula.
- hypotheses: Any Koszul chiral algebra with obstruction coefficient kappa.
- conclusion: F_g involves |B_{2g}|/(2g)! universally.
- category: GENUS
- proof_uses: [thm:genus-universality]

### [thm:universal-generating-function]
- file: chapters/examples/genus_expansions.tex:454
- statement: Universal generating function for genus expansions of Koszul chiral algebras.
- hypotheses: Koszul chiral algebra A with obstruction coefficient kappa.
- conclusion: Explicit generating function encoding all genera.
- category: GENUS
- proof_uses: [thm:bernoulli-universality]

---

## Part III: Detailed Entries (Connections)

### [thm:feynman-bar-cobar] (duplicate from chiral_koszul_pairs)
See above.

### [thm:a-infinity-constraint]
- file: chapters/connections/feynman_diagrams.tex:384
- statement: A_infinity constraint formula from Feynman diagrams.
- hypotheses: Chiral algebra A with A_infinity structure.
- conclusion: A_infinity relations are equivalent to cancellation of Feynman diagram anomalies.
- category: STRUCTURAL
- proof_uses: [thm:bar-ainfty-complete]

---

## Part IV: Summary of Remaining Claims (~470)

### By File (remaining claims not individually listed above)

| File | Total PH | Detailed Above | Remaining | Primary Category |
|------|----------|----------------|-----------|-----------------|
| bar_cobar_construction.tex | 76 | 30 | 46 | STRUCTURAL |
| higher_genus.tex | 86 | 25 | 61 | GENUS |
| configuration_spaces.tex | 40 | 8 | 32 | STRUCTURAL |
| chiral_koszul_pairs.tex | 13 | 10 | 3 | STRUCTURAL/FUNCTORIAL |
| introduction.tex | 17 | 7 | 10 | STRUCTURAL |
| chiral_modules.tex | 33 | 2 | 31 | FUNCTORIAL |
| deformation_theory.tex | 16 | 2 | 14 | STRUCTURAL |
| koszul_pair_structure.tex | 12 | 0 | 12 | STRUCTURAL |
| free_fields.tex | 43 | 7 | 36 | COMPUTATIONAL |
| kac_moody_framework.tex | 26 | 6 | 20 | COMPUTATIONAL |
| w_algebras_framework.tex | 17 | 3 | 14 | COMPUTATIONAL |
| genus_expansions.tex | 15 | 4 | 11 | COMPUTATIONAL/GENUS |
| poincare_duality.tex | 7 | 3 | 4 | STRUCTURAL |
| poincare_duality_quantum.tex | 6 | 2 | 4 | GENUS |
| lattice_foundations.tex | 17 | 0 | 17 | COMPUTATIONAL |
| beta_gamma.tex | 15 | 0 | 15 | COMPUTATIONAL |
| w3_composite_fields.tex | 13 | 0 | 13 | COMPUTATIONAL |
| minimal_model_fusion.tex | 12 | 0 | 12 | COMPUTATIONAL |
| detailed_computations.tex | 10 | 0 | 10 | COMPUTATIONAL |
| yangians.tex | 9 | 0 | 9 | COMPUTATIONAL |
| heisenberg_eisenstein.tex | 7 | 0 | 7 | COMPUTATIONAL |
| algebraic_foundations.tex | 5 | 0 | 5 | STRUCTURAL |
| hochschild_cohomology.tex | 5 | 0 | 5 | STRUCTURAL |
| classical_to_chiral.tex | 6 | 0 | 6 | STRUCTURAL |
| feynman_diagrams.tex | 6 | 1 | 5 | STRUCTURAL |
| holomorphic_topological.tex | 6 | 0 | 6 | STRUCTURAL |
| bv_brst.tex | 5 | 0 | 5 | STRUCTURAL |
| toroidal_elliptic.tex | 5 | 0 | 5 | COMPUTATIONAL |
| deformation_quantization.tex | 4 | 0 | 4 | STRUCTURAL |
| koszul_across_genera.tex | 4 | 0 | 4 | GENUS |
| w_algebras_deep.tex | 3 | 0 | 3 | COMPUTATIONAL |
| genus_complete.tex | 3 | 0 | 3 | GENUS |
| Appendices (14 files) | 34 | 0 | 34 | STRUCTURAL/COMPUTATIONAL |
| Other connections | 4 | 0 | 4 | STRUCTURAL |

### By Category (all 587 claims)

| Category | Count | Description |
|----------|-------|-------------|
| STRUCTURAL | ~210 | Bar-cobar adjunction, d^2=0, Verdier exchange, coalgebra axioms, Arnold relations, normal crossings |
| COMPUTATIONAL | ~200 | Free field computations, KM/W-algebra bar complexes, explicit formulas, dimension counts, character formulas |
| GENUS | ~90 | Higher genus inversion, quantum corrections, obstruction classes, Hodge bundle, modular operad |
| FUNCTORIAL | ~50 | Derived equivalences, module category Koszul duality, DS reduction intertwining, character correspondences |
| SPECTRAL | ~37 | Spectral sequence results, E_2 collapse, convergence, genus stratification |

### Remaining Claims: Typical Content

**bar_cobar_construction.tex (46 remaining):** Lemmas on sign compatibility, orientation conventions, residue properties, well-definedness of residues, bar coalgebra axiom verifications, cobar differential explicit formulas, cobar d^2 = 0 verifications, cobar sign consistency, cobar A_infinity explicit formulas (n_1 through n_5), weak topology on bar complex, complete essential image characterization, recognition principle, curved differential formulas, I-adic completion necessity/convergence, filtered-to-curved reduction, conilpotency convergence.

**higher_genus.tex (61 remaining):** Pentagon identity, cobar A_infinity structure, chain-level vs homology-level structure, geometric enhancement of Com-Lie, convergence for filtered algebras, deforming Heisenberg/beta-gamma, Jacobiator, Bianchi identity, higher associahedron, bar-cobar isomorphism for Koszul pairs, Hochschild duality, genus-1 Arnold relation, nilpotency at genus 1, E_1/E_2 page structure, W_3 obstruction explicit values, obstruction nilpotence, obstruction-deformation pairing, spectral sequence for quantum corrections, Verdier duality for compactified config spaces, duality for bar complexes, spectral sequence duality, modular properties, vanishing results, Virasoro quantum corrections, critical level uncurving, factorization over moduli, normal crossings persist, gluing at nodes, boundary compatibility, relative diagonal, DR preserves duality, Verdier dual of chiral algebra, AF duality for chiral algebras, key compatibility, de Rham-Verdier compatibility, Ran space duality, bar as factorization homology, coalgebra from Verdier dual, diagram commutes, open-stratum QI, boundary-stratum QI, extension across boundary, genus-graded Koszul resolution.

**chiral_modules.tex (31 remaining):** Fusion product, monoidal module Koszul duality, conformal blocks via bar, KZB connection from bar, conformal block duality, t-structures, tilting modules, Verma module bar complex, Zhu algebra under Koszul duality, orbit duality, free module structure, bar resolution acyclicity, geometric bar complex for modules, character via acyclic resolution, Koszul pairs simplify resolutions, character formula, Weyl-Kac character formula, character from bar resolution, Ext groups, characters under level-shifting, character with homological corrections, deformation of acyclicity, explicit vacuum module calculations (boson, fermion, W-algebra), bar complex as localization, singular support, DS-KD intertwining, characters under DS reduction, W-algebra cobar from KM bar.

**free_fields.tex (36 remaining):** Free fermion bar complex at genus 0, fermion bar coalgebra, beta-gamma bar complex, bc-betagamma orthogonality, single-generator fermion-boson duality, Heisenberg bar at genus 0, orientation consistency, convergence in curved structure, monodromy finiteness, Heisenberg curved structure, module-comodule equivalence, Fock module bar resolution, Koszul dual module, Fock module character, Ext groups between Fock modules, twisted module Koszul duality for fermions, spectral flow under Koszul duality, lattice VOA bar complex, A_2 lattice computation, geometric interpretation, elliptic free fermion bar complex, higher genus Heisenberg, filtered bar complex, Virasoro-string duality, W-algebra bar complex, Wakimoto bar complex, graphical interpretation, Heisenberg is not self-dual, modular invariance and anomaly cancellation.

---

## Index of Labels

For quick lookup, the most important labels and their categories:

**Main Theorems:**
- `mainthm:bar-cobar-complete` (STRUCTURAL)
- `mainthm:curved-complete` (GENUS)
- `mainthm:NAP-complete` (STRUCTURAL)
- `thm:quantum-complementarity-main` (GENUS)
- `thm:higher-genus-inversion` (GENUS)
- `thm:bar-cobar-inversion-qi` (STRUCTURAL)

**Core Structural:**
- `thm:bar-nilpotency-complete` (d^2=0)
- `thm:bar-cobar-verdier` (Verdier duality)
- `cor:bar-cobar-inverse` (mutual inverse)
- `thm:poincare-verdier` (PV duality)
- `thm:bar-computes-dual` (NAP)
- `thm:central-implies-strict` (centrality => strict)
- `thm:genus-induction-strict` (strict at all genera)

**Spectral:**
- `thm:bar-cobar-spectral-sequence`
- `thm:spectral-sequence-collapse`
- `thm:ss-genus-stratification`
- `thm:genus-graded-convergence`

**Functorial:**
- `cor:derived-equivalence-bar-cobar`
- `thm:e1-chiral-koszul-duality`
- `thm:module-category-equivalence`
- `thm:e1-module-koszul-duality`
- `thm:bar-cobar-inversion-functorial`

**Genus:**
- `thm:genus-universality`
- `thm:obstruction-general`
- `thm:heisenberg-obs`
- `thm:kac-moody-obs`
- `thm:self-dual-halving`
- `thm:kodaira-spencer-chiral-complete`
- `thm:CC-acyclicity-higher-genus`
- `thm:quantum-diff-squares-zero`
- `thm:feynman-bar-cobar`
- `thm:bernoulli-universality`

**Computational:**
- `thm:fermion-boson-koszul`
- `thm:heisenberg-koszul-dual-early`
- `thm:betagamma-bc-koszul`
- `thm:sl2-koszul-dual`
- `thm:universal-kac-moody-koszul`
- `thm:w-algebra-koszul-main`
- `thm:yangian-self-dual`
- `thm:heisenberg-all-genera`
- `thm:central-charge-complementarity`
