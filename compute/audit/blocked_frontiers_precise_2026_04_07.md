# Blocked Frontiers: Precise Obstruction Analysis

## 2026-04-07

Five frontier directions in the seven-face programme and the broader
modular Koszul duality framework are blocked by specific mathematical
obstructions. This document records what exists, what is missing, and
what minimal input would unblock each direction.

---

## 1. Spectral proof of Theorem B via Bethe completeness

### What exists

Theorem B (bar-cobar inversion: Omega(B(A)) -> A is a quasi-isomorphism
on the Koszul locus) is PROVED by the existing algebraic argument
(PBW filtration + spectral sequence degeneration at E_2). The spectral
proof via Bethe completeness is an independent alternative route that
would give Theorem B a representation-theoretic proof grounded in the
Gaudin model.

The Gaudin model (Feigin-Frenkel-Reshetikhin 1994) attaches commuting
Hamiltonians H_i = sum_{j != i} Omega_{ij}/(z_i - z_j) to n points on
P^1 acting on V_{lambda_1} tensor ... tensor V_{lambda_n}. The Bethe
ansatz produces joint eigenvectors of the H_i parametrized by solutions
of the Bethe equations. Mukhin-Tarasov-Varchenko (MTV) proved Bethe
completeness for finite-dimensional g-modules: the Bethe vectors form
a basis of the tensor product, hence the joint spectrum of the Gaudin
Hamiltonians is simple.

The seven-face programme (standalone/seven_faces.tex, Theorem 3.1)
identifies the collision residue r(z) = Res^coll_{0,2}(Theta_A) with the
Gaudin generating function (Face F7). This gives a spectral interpretation
of bar-cobar inversion: the bar differential, projected to genus 0 and
arity 2, acts on the Bethe eigenbasis as a diagonal operator, and the
cobar reconstruction recovers A from the spectral data.

### What is missing

The MTV Bethe completeness theorem applies to FINITE-DIMENSIONAL
g-modules. The chiral bar complex involves INFINITE-DIMENSIONAL modules:
the bar slots carry copies of A itself (a vertex algebra, infinite-
dimensional in each weight space for W-algebras). Three specific
obstructions block the extension:

(a) Spectral simplicity. MTV proves the Gaudin spectrum is simple for
finite-dimensional modules. For infinite-dimensional modules, the
spectrum can have continuous components and accumulation points. The
spectral simplicity argument (which uses the Shapovalov determinant
and the Wronski map to the space of polynomials) does not directly
generalize.

(b) Bethe vector completeness. The Bethe ansatz produces a discrete
family of eigenvectors parametrized by solutions of algebraic
equations. For infinite-dimensional modules, the Bethe equations become
transcendental (involving q-series), and the solution set may be
uncountable or have convergence issues.

(c) The critical-level wall. The Gaudin model is the critical-level
(k = -h^v) limit of the KZ connection. The bar complex operates at
generic (non-critical) level. The passage from non-critical to critical
is the Feigin-Frenkel center construction, which changes the nature
of the commuting operators from differential to multiplication. The
spectral proof requires understanding this transition at the level of
the bar complex.

### Partial results

The Gaudin-collision engine (standalone/gaudin_from_collision.tex, 177
tests) verifies the F4-F7 identification for all simple types at finite
rank. The genus-0 seven-face chain closes without obstruction on
finite-dimensional evaluation modules. The KZB connection at genus 1
(appendices/ordered_associative_chiral_kd.tex, Theorem at line 7188)
extends the r-matrix to the elliptic setting, providing the genus-1
version of the Gaudin Hamiltonians.

Rybnikov (2006) extended Bethe completeness to certain limits of
evaluation modules. Feigin-Frenkel-Toledano Laredo established a
connection between Gaudin models and opers that could, in principle,
extend to the chiral setting via the Beilinson-Drinfeld opers framework.

### Minimal unblocking input

Prove Bethe completeness for the Gaudin model on a category of modules
containing the bar slots of a chirally Koszul algebra. The most
accessible route: extend MTV to highest-weight modules of bounded
conformal weight via the Kac-Kazhdan character formula, then use the
weight-space finiteness of chirally Koszul algebras (each weight space
is finite-dimensional) to reduce to the finite-dimensional case
weight-by-weight. This would require:

1. A Bethe-completeness theorem for weight-graded tensor products of
   Verma modules (extending MTV from irreducibles to Vermas).
2. A comparison between the Gaudin spectral decomposition and the PBW
   spectral sequence (showing the E_2-degeneration of the bar spectral
   sequence corresponds to simplicity of the Gaudin spectrum).
3. A proof that the cobar reconstruction map, expressed in the Bethe
   eigenbasis, is the inverse of the bar projection.

---

## 2. Seven-face categorification as 2-functor

### What exists

The seven-face master theorem (standalone/seven_faces.tex, Theorem 3.1)
proves that seven presentations of the collision residue r(z) determine
the same element of A^! tensor A^![[z^{-1}]]. Each face identification
(F1-F7) is a theorem at the level of 1-morphisms: it identifies two
specific mathematical objects as equal. The chain F1-F2-F3-F4-F7-F5-F6
closes, and the 929-test compute layer verifies coherence.

The individual faces live in different categorical worlds:
- F1 (twisting morphism): factorization coalgebras on Ran(X)
- F2 (line operator R-twist): dg categories of line operators in 3d HT
- F3 (PVA r-matrix): Poisson vertex algebras
- F4 (GZ commuting differentials): D-modules on M_{0,n}
- F5 (Yangian R-matrix): braided monoidal categories (Rep Y_hbar(g))
- F6 (Sklyanin bracket): Poisson geometry on coadjoint orbits
- F7 (Gaudin generator): integrable systems / commuting Hamiltonians

### What is missing

The seven-face identification is proved at the level of OBJECTS (the
r-matrices agree). The categorification asks: do the seven CATEGORIES
assemble into a 2-functor? Specifically:

(a) The 2-categorical structure. Each face defines a category (e.g.,
Rep Y(g) for F5, QCoh(Loc_G) for F6). The face identifications should
lift to equivalences of categories, and the composite equivalences
around any triangle in the seven-face network should satisfy a coherence
condition (the equivalences compose to the identity 2-morphism, not
just to an isomorphic functor).

(b) The target 2-category. The natural target is the (infinity,2)-
category of dg categories (or stable infinity-categories). The seven
source categories live at different categorical levels: some are abelian
(Rep Y(g)), some are triangulated (D-modules on M_{0,n}), some are
dg-enhanced (factorization categories). A unified 2-functorial framework
requires placing all seven in a common (infinity,2)-categorical setting.

(c) The specific gap. Lurie's Higher Algebra provides the foundations
for (infinity,2)-categories of algebra objects. Calaque-Scheimbauer
(2015) construct factorization algebras as functors from a category of
disks to (infinity,1)-categories. Haugseng (2017) develops the
(infinity,2)-category of correspondences needed for dualities. But none
of these frameworks addresses the specific problem of SEVEN functors
between SEVEN different categorical frameworks simultaneously satisfying
hexagonal coherence.

### Partial results

The F5-F6 categorification is classical: the Drinfeld-Jimbo
equivalence between Rep U_q(g) and a category constructed from the
R-matrix is a theorem (Kassel 1995). The F1-F2 categorification is the
content of the DNP identification (Dimofte-Niu-Py 2025), which works
at the level of dg categories of line operators. The F4-F7 link
(GZ-Gaudin) is proved at the operator level but the categorical lift
(D-modules on M_{0,n} equivalent to a category of Gaudin eigensheaves)
is the content of Frenkel's geometric Langlands programme for the Gaudin
model, which is proved for g = sl_2 (Feigin-Frenkel 2006) but open in
general.

### Minimal unblocking input

The minimal input is a proof of 2-functorial coherence for the TRIANGLE
F1-F5-F7. This triangle relates:
- F1: the bar-cobar factorization category
- F5: the Yangian representation category
- F7: the Gaudin eigensheaf category

The three bilateral equivalences (each proved as a 1-categorical
statement) form a triangle that must commute up to a specified natural
isomorphism. The required tools are:

1. Kazhdan-Lusztig-style equivalence between (a derived version of)
   the bar-cobar category at genus 0 and Rep Y_hbar(g) (this is the
   DK bridge, currently proved on the evaluation core: MC3).
2. The FFR (Feigin-Frenkel-Reshetikhin) identification of Gaudin
   eigensheaves with opers, lifted to a dg-categorical equivalence.
3. A coherence datum (natural isomorphism) for the composite.

The full seven-face 2-functor would then follow by composing triangles.

---

## 3. Shifted-symplectic complementarity via Sklyanin

### What exists

Theorem C (complementarity) is proved in two forms:

(C1) UNCONDITIONAL: the eigenspace decomposition
Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)) as a direct sum splitting. This is
proved for all chirally Koszul pairs at all genera.

(C2) CONDITIONAL: the total complementarity complex C_g(A) carries a
(-(3g-3))-shifted symplectic structure in the PTVV sense, with Q_g(A)
and Q_g(A^!) as complementary Lagrangian subspaces. This is proved
CONDITIONAL on two hypotheses: (H1) perfectness of R pi_{g*} B^(g)(A)
on M_bar_g, and (H2) nondegeneracy of the Verdier pairing.

The PTVV framework (Pantev-Toen-Vaquie-Vezzosi 2013) provides the
foundations: an n-shifted symplectic structure on a derived stack F is a
closed 2-form omega of degree n with omega^sharp : T_F -> L_F[n] a
quasi-isomorphism. A Lagrangian is a morphism L -> F with f*omega = 0
and the induced map T_L -> L_{L/F}[n-1] a quasi-isomorphism.

The BV structure (thm:thqg-III-bv-lagrangian) gives a (-1)-shifted
symplectic structure on MC(B^(g)(A)[1]) that is UNIVERSAL in g. The
Verdier structure gives a (-(3g-3))-shifted structure that DEPENDS on g.
Both make Q_g(A) and Q_g(A^!) complementary Lagrangians.

The Sklyanin bracket (Face F6) provides a classical Poisson structure
on the space of A^!-line-operator configurations. The Yangian quantizes
this Poisson structure.

### What is missing

The connection between the Sklyanin Poisson geometry and the PTVV
shifted-symplectic complementarity has not been established. The
specific gap is:

(a) The convolution dg Lie algebra g^mod_A carries both structures: (i)
the PTVV shifted-symplectic structure from the cyclic pairing (via the
Kontsevich-Pridham correspondence: a dg Lie algebra with invariant
pairing of degree n produces an n-shifted symplectic formal moduli
problem), and (ii) the Sklyanin Poisson structure from the r-matrix
r(z) (the genus-0 binary projection). These two structures should be
COMPATIBLE: the Sklyanin bracket should be the genus-0, arity-2
projection of the shifted symplectic structure.

(b) The cyclic pairing on the convolution algebra is an invariant
pairing of degree -1. By Kontsevich-Pridham (Proposition at line 861 of
thqg_symplectic_polarization.tex), this produces a (-1)-shifted
symplectic structure on MC(g^mod_A). The complementarity Lagrangians
come from the sigma-eigenspace decomposition. The Sklyanin bracket is
the genus-0 classical limit of this structure. But the precise
relationship -- that the Sklyanin bracket is the leading-order term in
a deformation quantization of the shifted symplectic structure -- has
not been proved.

(c) The perfectness and nondegeneracy hypotheses (H1, H2) required for
the CONDITIONAL upgrade (C2) are verified for all standard families at
low genus (the Lagrangian perfectness theorem, prop:lagrangian-
perfectness, proves this for the standard landscape). But the connection
to the Sklyanin geometry could provide an UNCONDITIONAL proof: if the
Sklyanin Poisson structure is nondegenerate (which it is for generic
level, by the non-vanishing of the Casimir), then the shifted symplectic
structure is automatically nondegenerate.

### Partial results

The CPTVV (Calaque-Pantev-Toen-Vaquie-Vezzosi 2017) paper on shifted
Poisson structures and deformation quantization provides the framework
for connecting shifted symplectic and Poisson structures. The
complementarity potential S_A (Definition at line 591 of
nonlinear_modular_shadows.tex) is the generating function of the
Lagrangian, and its Legendre dual S_{A^!} encodes the dual Lagrangian.
The Legendre duality of S_A and S_{A^!} (Proposition at line 606) is
proved.

### Minimal unblocking input

1. Show that the Sklyanin Poisson bracket on the formal neighborhood of
   r(z) in A^! tensor A^![[z^{-1}]] is the genus-0 arity-2 reduction
   of the (-1)-shifted symplectic structure on MC(g^mod_A). This is a
   computation in the CPTVV framework: the shifted Poisson structure
   associated to the cyclic pairing, evaluated on the twisting morphism
   locus, should reproduce the Sklyanin bracket.

2. Prove that nondegeneracy of the Sklyanin bracket at generic level
   implies nondegeneracy of the shifted symplectic pairing (hypothesis
   H2). This would make (C2) unconditional for all standard families at
   generic level.

3. Identify the complementarity potential S_A with the generating
   function of the Gaudin eigensheaf category (connecting to frontier 2).

---

## 4. Higher-genus seven faces beyond genus 1

### What exists

The seven-face programme is proved at genus 0: all seven presentations
of r(z) are identified, the chain F1-F7 closes, and 929 tests verify
coherence.

At genus 1, the KZB connection (appendices/ordered_associative_chiral_kd
.tex, Definition at line 4864) replaces the KZ connection. The elliptic
r-matrix (eq:elliptic-r-matrix at line 7188) replaces the rational
r-matrix:

  r^{E_tau}(z) = c_0 zeta(z|tau) + c_1 wp(z|tau) + ...

where zeta and wp are Weierstrass functions. The Drinfeld-Kohno theorem
at genus 1 (proved by Etingof-Schiffmann and Calaque-Enriquez-Etingof)
identifies the KZB monodromy with the quantum group U_q(g). This gives
the genus-1 seven-face identification for the AFFINE LINEAGE (simple g,
generic level, finite-dimensional evaluation modules).

The genus-1 Swiss-cheese structure exhibits a Cartan/Yangian dichotomy
(Theorem at line 7188): when c_0 = 0 (Cartan type), the elliptic
r-matrix is doubly periodic and the braiding decouples from the Hodge
curvature; when c_0 != 0 (Yangian type), the B-cycle monodromy
2 eta_tau c_0 entangles braiding and curvature.

### What is missing

At genus g >= 2, three specific obstructions block the seven-face
programme:

(a) Automorphic r-matrices. The genus-0 r-matrix is rational (poles at
z = 0). The genus-1 r-matrix is elliptic (Weierstrass functions). At
genus g >= 2, the r-matrix should involve automorphic functions on the
Jacobian Jac(Sigma_g) -- specifically, sections of line bundles on the
universal curve over M_g pulled back to the configuration space. The
theory of automorphic r-matrices at genus >= 2 does not exist in the
literature. Etingof-Varchenko (1998) studied dynamical r-matrices with
spectral parameter on higher-genus curves, but only for specific
representations and without the full Bethe/Gaudin framework.

(b) The propagator problem. At genus 0, the bar propagator is
d log(z-w) = dz/(z-w). At genus 1, it is the Weierstrass zeta function
zeta(z-w|tau) dz. At genus g >= 2, the propagator is the Szego kernel
S(z,w) on Sigma_g: a (1,0)-form in z with a simple pole at z = w and
prescribed normalization along the g independent A-cycles. The Szego
kernel depends on a spin structure (choice of theta characteristic).
The bar complex uses the canonical propagator d log E(z,w) where E is
the prime form, which is independent of spin structure but acquires
monodromy along B-cycles. Controlling this monodromy at genus >= 2
requires the full Schottky uniformization or algebraic-geometric methods
on the Jacobian.

(c) The moduli problem. At genus 0, the configuration space is M_{0,n}
(algebraic, rational). At genus 1, it is Conf_n(E_tau) parametrized by
tau in H (the upper half-plane). At genus >= 2, the configuration space
Conf_n(Sigma_g) fibers over M_g, and the seven-face identification must
be compatible with the variation over M_g. The GZ commuting Hamiltonians
(Face F4) generalize to operators on M_{g,n}, but the curvature
kappa * omega_g introduces a genuinely new term: the connection
nabla^GZ acquires curvature proportional to the Hodge class, and the
commutativity [H_i, H_j] = 0 holds only modulo this curvature.

### Partial results

Genus 2 is partially accessible. The genus-2 planted-forest engine
(14 three-vertex, 11 four-vertex graphs among 42 total stable graphs of
M_bar_{3,0}) computes the planted-forest correction at genus 2:
delta_pf^{(2,0)} = S_3(10S_3 - kappa)/48. The seven-face identification
at genus 2 would require:
- The genus-2 analogue of the KZB connection (involving period matrices
  of hyperelliptic curves)
- The genus-2 Gaudin Hamiltonians (involving the Szego kernel on
  hyperelliptic curves)
- A genus-2 Drinfeld-Kohno-type theorem identifying the monodromy with
  a quantum algebraic structure

None of these exist in the literature for general g, though
Enriquez (2010) constructed genus-g analogues of the KZB connection
using the universal unipotent connection on the universal curve.

### Minimal unblocking input

For GENUS 2 specifically:

1. Construct the genus-2 KZB-type connection on Conf_n(Sigma_2) using
   Enriquez's framework and the period matrix of Sigma_2.

2. Identify the genus-2 Gaudin Hamiltonians as the genus-2 projection
   of the MC equation Theta_A restricted to the genus-2 stratum of the
   bar complex.

3. Prove a genus-2 Drinfeld-Kohno theorem: the monodromy of the
   genus-2 KZB connection factors through a quantum algebraic structure
   (likely a quotient of the completed Yangian by the genus-2 ideal
   generated by the Hodge curvature).

For ARBITRARY GENUS: the minimal input is a theory of automorphic
r-matrices parametrized by the Torelli space of Sigma_g, compatible with
degeneration (the r-matrix at a nodal curve is the sewing of lower-genus
r-matrices). This would require foundational work in higher-genus
quantum groups that does not currently exist.

---

## 5. Koszulness-from-Sklyanin for classes C and M

### What exists

The Sklyanin bracket (Face F6) is a Poisson bracket on the space of
A^!-line-operator configurations, generated by the classical r-matrix
r(z). For class G (Gaussian) and class L (Lie/tree), the Sklyanin
bracket is a standard linear or quadratic Poisson bracket: the r-matrix
has at most a simple pole (k_max = 1), and the Poisson bracket is of
order 1. For these classes, the Koszulness characterization is
well-understood: PBW degeneration, A_infinity formality, and all 10
unconditional equivalences of the meta-theorem (thm:koszul-equivalences-
meta) apply directly.

The seven-face classification (standalone/seven_faces.tex, Theorem 4.1)
shows that classes C and M have qualitatively different Sklyanin
structures:

- Class C (betagamma, k_max = 0): the collision residue VANISHES, so
  the Sklyanin bracket is identically zero. The GZ Hamiltonians are
  trivial. Koszulness holds (betagamma is chirally Koszul) but is not
  witnessed by the Sklyanin bracket.

- Class M (Virasoro, W_N, k_max >= 3): the collision residue has poles
  of order >= 3, making the Sklyanin bracket a DIFFERENTIAL Poisson
  bracket. The GZ Hamiltonians are genuine differential operators of
  order k_max - 1 >= 2. Koszulness holds (Virasoro and W_N are chirally
  Koszul) but the relationship between the differential Poisson structure
  and the Koszulness characterization is not understood.

### What is missing

(a) Differential Poisson brackets of order >= 2. A standard (linear)
Poisson bracket on a polynomial algebra is of order 1: {f, g} involves
at most first derivatives of f and g. The Sklyanin bracket for class M
is of order k_max - 1 >= 2: it involves higher derivatives. The theory
of DIFFERENTIAL Poisson algebras (Poisson brackets involving
differential operators of order >= 2) exists in a limited form
(Krasil'shchik-Verbovetsky, jet-space Poisson structures) but has not
been connected to Koszulness theory. Specifically:

- Does every differential Poisson bracket of finite order admit a
  deformation quantization? (For order 1, this is Kontsevich's formality
  theorem. For order >= 2, the question is open in general.)

- Does the existence of such a quantization imply Koszulness of the
  associated chiral algebra? (For order 1, this is the content of the
  K3 characterization: PVA quantization implies Koszulness.)

(b) Class C: Koszulness without Sklyanin. For betagamma, the Sklyanin
bracket vanishes, yet the algebra is chirally Koszul. The Koszulness is
witnessed by the QUARTIC contact invariant Q^contact (which lives on a
charged stratum, not on the primary line where the Sklyanin bracket is
defined). The stratum-separation mechanism (Remark 5.6 in
seven_faces.tex) explains why the shadow obstruction tower terminates at
arity 4 despite the vanishing collision residue, but does not provide a
Sklyanin-type explanation of Koszulness. A "generalized Sklyanin
bracket" that includes contributions from charged strata would be needed.

(c) Class M: infinite tower and Koszulness. For Virasoro and W_N, the
shadow obstruction tower is infinite (r_max = infinity), yet the algebra
is chirally Koszul (bar cohomology concentrated in bar degree 1). The
infinite tower provides an infinite sequence of obstructions (kappa, C,
Q, ...) all of which are controlled by the MC equation. The question is:
does the MC equation, interpreted as a differential Poisson master
equation of infinite order, CHARACTERIZE Koszulness?

### Partial results

The shadow-formality identification (thm:shadow-formality-identification)
proves that the shadow obstruction tower IS the L_infinity formality
obstruction tower at all arities. This means the MC equation on the
shadow side is equivalent to L_infinity formality on the bar side. But
the translation to the Sklyanin framework has not been done: the
L_infinity formality obstruction tower is defined on the bar complex,
not on the Sklyanin configuration space.

For class M, the A_infinity non-formality engine
(theorem_ainfty_nonformality_class_m_engine, 77 tests) verifies that
the higher A_infinity operations m_k (k >= 3) are nonzero, confirming
that class M is NOT Swiss-cheese formal (AP14: Koszulness !=
formality). The K3 Poisson vertex algebra lambda-bracket for Virasoro
has all coefficients nonzero (the T_{(3)}T = c/2 mode generates a
cubic pole in the collision residue), and the resulting differential
Poisson bracket is of order 2.

### Minimal unblocking input

1. For class C: construct a "charged Sklyanin bracket" on the full
   cyclic deformation complex (not just the primary line) that
   witnesses the quartic contact invariant Q^contact. This requires
   extending the Sklyanin construction from the genus-0 arity-2
   collision residue to the genus-0 arity-4 sector, where the
   contact term lives on a charged stratum.

2. For class M: prove that the differential Poisson bracket of order
   k_max - 1 admits a deformation quantization (extending Kontsevich
   formality to differential Poisson brackets), and that this
   quantization is the Yangian Y_hbar(A^!) with its full higher-
   order R-matrix.

3. For both: establish a "generalized Koszulness-from-Sklyanin"
   theorem stating that the existence of a (possibly differential,
   possibly higher-arity) classical r-matrix satisfying the CYBE
   (or its higher-order generalization) implies chirally Koszulness.
   The key insight would be that the CYBE is the shadow of D^2 = 0,
   and D^2 = 0 is the source of Koszulness.
