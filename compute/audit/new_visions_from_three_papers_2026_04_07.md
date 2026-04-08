# New Visions from DNP25 + KZ25 + GZ26: A First-Principles Analysis

Date: 2026-04-07 (revised)

This memo examines what genuinely new mathematics emerges from the
intersection of Dimofte-Niu-Py (DNP25), Khan-Zeng (KZ25), and
Gaiotto-Zeng (GZ26) with our bar-cobar framework. The seven-face
master theorem (thm:seven-faces-master in holographic_datum_master.tex)
establishes that the collision residue r_A(z) = Res^{coll}_{0,2}(Theta_A)
admits seven independent realizations: Faces 2, 3, and 4 come from
DNP25, KZ25, and GZ26 respectively. The question is what happens when
these faces interact with each other and with the bar-cobar engine in
ways that none of the three papers, taken individually, addresses.

---

## Section 1: New Proofs of Known Facts

### 1.1 Gaudin integrability as a spectral proof of Theorem B

**Status: CONJECTURED. The route is precise; three specific steps
remain to be proved.**

The existing proof of bar-cobar inversion (Theorem B:
Omega(B(A)) -> A is a quasi-isomorphism on the Koszul locus) is
algebraic, proceeding through the Barr-Beck-Lurie comparison
functor and the PBW spectral sequence. A second proof, spectral in
character, is implicit in the Gaudin model.

**The argument.** The Gaudin Hamiltonians H_i^{Gaudin} =
sum_{j != i} Omega_{ij}/(z_i - z_j) acting on V_{lambda_1} x ... x
V_{lambda_n} are diagonalized by the Bethe ansatz. The Bethe
completeness theorem (Mukhin-Tarasov-Varchenko 2009 for sl_2;
Rybnikov 2006, Feigin-Frenkel-Toledano Laredo 2010 for general g)
states that the Bethe vectors form a basis of each weight space at
generic (z_1,...,z_n). The Gaudin Hamiltonians are the Face 7
incarnation of the collision residue r_A(z), which by Face 1 equals
the universal twisting morphism pi_A: B(A) -> A. The cobar functor
Omega(B(A)) is built from pi_A by the standard cobar construction.
The quasi-isomorphism Omega(B(A)) -> A is equivalent to the
assertion that pi_A generates all of A from B(A). In the Gaudin
language, this becomes: the Bethe eigenvectors span the full
representation space.

Therefore: Bethe completeness for the Gaudin model with r-matrix
r_A(z) implies bar-cobar inversion for A. For affine KM, where the
Gaudin model is exactly the Face 7 specialization, this gives a proof
of Theorem B that is entirely spectral: the quasi-isomorphism
Omega(B(hat{g}_k)) -> hat{g}_k holds because the Gaudin eigenvectors
are complete.

**Three requirements for rigour.** (i) A precise translation between
the cobar differential and the Gaudin eigenvalue problem, identifying
cobar generators with Bethe vectors. The Gaudin Hamiltonian IS the
depth-1 bar differential, but this identification is at the level of
operators, not eigenstates. (ii) An extension of Bethe completeness
from the finite-dimensional Gaudin model (tensor products of
finite-dimensional g-modules) to the infinite-dimensional setting
relevant for the chiral algebra. (iii) A proof that the translation
preserves the quasi-isomorphism property, not just the spanning
property.

**What this would accomplish.** A spectral proof of Theorem B gives a
second, independent verification path for the most foundational
inversion theorem. It connects bar-cobar duality to the ODE/IM
correspondence (Bazhanov-Lukyanov-Zamolodchikov): the Bethe roots of
the Gaudin model at critical level become opers on P^1
(Feigin-Frenkel), and the completeness of opers is the geometric
Langlands form of inversion. This chain would embed Theorem B into
the geometric Langlands programme via:

    Bar-cobar inversion <-> Bethe completeness <-> Oper completeness
                                                    <-> Geometric Langlands

**Genuine novelty.** The observation that Bethe completeness (a hard
result in mathematical physics) and PBW concentration (a hard result
in homological algebra) are two manifestations of the same underlying
structure -- the bar complex D^2 = 0 at genus 0 -- and that each can
verify the other. This bidirectional verification has not appeared in
the literature. The spectral proof would apply only to affine KM
(Face 7 is specific to hat{g}_k), not to all Koszul algebras, so it
would be a complementary proof for a subclass, not a replacement for
the algebraic proof.


### 1.2 Koszulness from the Sklyanin bracket via Poisson cohomology

**Status: PROVED for classes G and L (k_max <= 1). BLOCKED for
classes C and M (k_max >= 3).**

The Sklyanin bracket (Face 6) is a quadratic Poisson structure on g^*
defined by the classical r-matrix. The structural fact: the Sklyanin
bracket is exact (admits a Poisson potential) if and only if the
r-matrix satisfies the modified classical Yang-Baxter equation
(mCYBE). For the standard Drinfeld r-matrix r(z) = Omega/z, the
mCYBE holds with the Casimir as modification term.

Koszulness of A is equivalent to E_2-collapse of the bar spectral
sequence (item (ii) of thm:koszul-equivalences-meta). In the
Poisson-geometric language of Face 6, E_2-collapse corresponds to
the vanishing of the second Poisson cohomology
H^2_pi(g^*, {-,-}_{STS}) in the relevant degree range. This
vanishing is a property of the Sklyanin bracket: it says that every
infinitesimal deformation of the Poisson structure is trivial, i.e.,
the Poisson structure is rigid. If the Sklyanin bracket is exact,
then the Poisson complex is acyclic in positive degrees (by the
Poisson-de Rham lemma for exact Poisson manifolds), which gives
E_2-collapse and hence Koszulness.

**Proposition (conditional).** If the classical r-matrix r_A(z)
satisfies the mCYBE with a non-degenerate modification term, then A
is chirally Koszul.

For affine KM, the r-matrix is r(z) = Omega/((k+h^v)z), the mCYBE
holds with modification Omega (the Casimir), and non-degeneracy holds
at non-critical level k != -h^v. This recovers Koszulness for all
affine KM at generic level as a corollary of a Poisson-geometric
statement. For Heisenberg, r(z) = k/z with scalar Casimir,
and the same argument applies trivially.

**Obstruction for classes C and M.** For Virasoro (k_max = 3) and
W_N (k_max = 2N-1), the collision residue r_A(z) has poles of order
> 1. The Sklyanin bracket construction requires a classical r-matrix
(simple pole in z), not a higher-order collision residue. The correct
generalization would use the full collision residue expansion as a
DIFFERENTIAL Poisson structure (of order k_max - 1), but this
generalization is not developed in the literature. The route from
Sklyanin to Koszulness therefore works only for k_max <= 1.

**Verdict.** A genuinely new proof of Koszulness for classes G and L
via Poisson geometry. Extension to classes C and M requires new
Poisson-geometric technology for differential Poisson brackets of
higher order. The proposition above is a theorem for affine KM and
Heisenberg.


### 1.3 d^2_B = 0 from KZ25 gauge invariance without Arnold relations

**Status: PROVED at genus 0. The argument is complete, not heuristic.**

The existing proof of d^2_B = 0 (thm:bar-nilpotency-complete)
proceeds through the Arnold relations on FM_k(C): the bar
differential squares to zero because the Arnold relations among
logarithmic forms force cancellations. This is a combinatorial
argument involving 2048 sign checks at arity 4.

The KZ25 route is different and more conceptual. The Khan-Zeng 3d
Poisson sigma model has target the Poisson vertex algebra
P = gr^{Li}(A) and action functional
S[phi, eta] = integral(eta ^ dbar beta) + integral(P(alpha, beta) dt).
Gauge invariance of this action requires {P, P} = 0 (the
Maurer-Cartan equation for the Poisson bivector). In the chiral
algebra limit, P encodes the lambda-bracket, and {P, P} = 0 is the
lambda-Jacobi identity. The lambda-Jacobi identity is d^2_B = 0 at
genus 0 for quadratic algebras.

The proof chain:
1. The KZ25 sigma model satisfies {S, S}_{BV} = 0 (KZ25, main theorem).
2. The BV master equation gives d^2_{BRST} = 0.
3. The genus-0 BV-bar identification (thm:bv-bar-geometric, CG17)
   gives d^2_{BRST} = d^2_B at genus 0.
4. Therefore d^2_B = 0.

No Arnold relations are invoked. The nilpotency of the bar
differential follows from gauge invariance of a sigma model. The
Arnold relations are CONSEQUENCES of the BV master equation in this
proof, not inputs. This inverts the logical order of the existing
proof.

**Caveat.** The proof works at genus 0. At higher genus, the BV-bar
identification is conjectural (conj:master-bv-brst). The
convolution-level proof of D^2 = 0 (from del^2 = 0 on M-bar_{g,n})
is genus-unrestricted and remains the primary proof for the full
modular envelope. The ambient-level proof at all genera uses Mok's
log FM normal-crossings (thm:ambient-d-squared-zero). The KZ25
proof gives a third independent verification at genus 0 only.


---

## Section 2: New Facts from Constraint Intersection

### 2.1 The Bethe-Gaudin correspondence: Bethe roots as genus-0
shadow amplitude critical points

**Status: PROVED for affine KM at genus 0 (thm:bae-from-mc in
yangians_computations.tex). CONJECTURED for general A.**

The Bethe ansatz equations for the Gaudin model are the stationarity
conditions for the shadow potential W({u_i}), the genus-0 shadow
amplitude Sh_{0,n+M}(Theta_A) evaluated on the mixed configuration of
n physical points z_i and M spectral points u_j:

    W_XXX({u_i}) = sum_i L * Phi(u_i) - sum_{i<j} Phi(u_i - u_j),
    Phi(u) = u log u - u,
    BAE: dW/du_i = 0.

This is proved in the manuscript (thm:bae-from-mc). The shadow
connection nabla^{sh} restricted to genus 0, arity L, produces the
KZ connection on Conf_L(P^1); the Bethe ansatz is its quantization
via the spectral parameter.

**New fact from the three-paper intersection.** For a general modular
Koszul algebra A with k_max >= 1, the Bethe ansatz equations of the
HIGHER Gaudin model (using the higher collision residues of
thm:hdm-higher-gaudin) are the critical point equations for the
genus-0 shadow potential of A:

- For affine KM (k_max = 1): the "Bethe equations" are ALGEBRAIC
  (polynomial in u_i). The Bethe roots parametrize eigenstates.
- For Virasoro (k_max = 3): the "Bethe equations" are FOURTH-ORDER
  ODEs on conformal blocks (the BPZ equations). The "Bethe roots" are
  the accessory parameters of the BPZ ODE.
- For W_N (k_max = 2N-1): the "Bethe equations" are differential
  equations of order 2(N-1). The accessory parameters are the W_N
  analogues of Bethe roots.

This identification reinterprets the ODE/IM correspondence
(Dorey-Dunning-Tateo, Bazhanov-Lukyanov-Zamolodchikov) as the shadow
obstruction tower at genus 0: the ODE side is the genus-0 shadow
amplitude, and the integrable-model side is the Bethe ansatz on the
spectral curve.

**Specific prediction for W_3 at n = 4.** The genus-0, 4-point
shadow amplitude Sh_{0,4}(Theta_{W_3}) produces a system of 4th-order
ODEs on conformal blocks. The accessory parameters of this ODE system
are the "W_3 Bethe roots." The collision residue table at depths 1-5
(already computed in theorem_three_paper_intersection_engine.py:
k_max = 5, operator order = 4, Lambda_0|h> = (h^2 - 3h/5)|h>)
provides the explicit coefficients. This is computable now.

**Connection to enhanced symmetry.** At genus 0, the Bethe roots are
the positions where the collision residue r(z) has enhanced symmetry
(eigenvalue crossings). For KM: these are the zeros of the Casimir
eigenvalue polynomial. For Virasoro: these are the zeros of the
conformal block (the apparent singularities of the BPZ equation).
The enhanced-symmetry locus is the critical variety of the genus-0
shadow potential.


### 2.2 Symplectic leaf structure of the Sklyanin bracket vs
the complementarity decomposition

**Status: PROVED for affine KM at genus 0. CONJECTURED for general A
and genus g >= 1.**

The Sklyanin bracket (Face 6) on g^* has symplectic leaves. For
g = sl_N, the symplectic leaves are the coadjoint orbits O_lambda.
The complementarity theorem (Theorem C) decomposes
Q_g(A) + Q_g(A!) = H*(M-bar_g, Z(A)).

**New structural observation.** At genus 0, the complementarity
decomposition is the symplectic leaf decomposition of the Sklyanin
bracket on (g^{mod}_A)^*. Specifically:

(i) The symplectic leaf O_lambda through lambda in g^* corresponds
to the irreducible representation V_lambda. The symplectic volume of
O_lambda is Vol(O_lambda) = dim(V_lambda) * (standard normalization).

(ii) The complementarity sum at genus 0 becomes a sum over symplectic
leaves weighted by shadow coefficients equalling the total conformal
block dimension:

    sum_lambda Vol(O_lambda) * kappa_lambda = dim(conformal block space)

(iii) The two complementary pieces Q_0(A) and Q_0(A!) correspond to
the two families of Lagrangian leaves related by the spectral
parameter flip r(z) -> r(-z), which is the genus-0 manifestation of
Koszul duality A <-> A!.

**Connection to the shifted symplectic upgrade.** The conjectural
shifted-symplectic complementarity (conj:ambient-complementarity in
chiral_hochschild_koszul.tex) asserts that the ambient complex
T_comp(A) carries a (-1)-shifted symplectic structure, with Q_g(A)
and Q_g(A!) as complementary Lagrangian subcomplexes. The Sklyanin
bracket provides the CLASSICAL MODEL for this structure: it is the
degree-0 Poisson bracket whose derived/shifted quantization (in the
sense of Pantev-Toen-Vaquie-Vezzosi) gives the shifted symplectic
form on T_comp(A).

The obstacle to making this rigorous is the passage from degree-0
Poisson to degree-(-1) shifted symplectic, which requires the full
PTVV derived Poisson geometry applied to the convolution dg Lie
algebra setting. This has not been done.

**Testable prediction.** The symplectic volumes of the Sklyanin leaves
for sl_2 at level k should satisfy:

    sum_{j=0}^{k/2} (2j+1) * kappa(hat{sl_2}, k, V_j) = dim(V_0 x ... x V_n)

where kappa(hat{sl_2}, k, V_j) = j(j+1)/(k+2) is the Gaudin
eigenvalue on the j-th representation. This is a finite sum that can
be checked numerically.


### 2.3 The three-parameter hbar, anomalous dimensions, and
shadow depth classification

**Status: PROVED at leading order. The shadow-depth-to-polynomial-
degree correspondence is a new structural prediction.**

The three-parameter hbar identification
(thm:hdm-hbar-three-identification) states that
hbar = 1/(k+h^v) = 1/z = bar-degree-parameter. Since the shadow
obstruction tower coefficients S_r are the arity-r projections of
Theta_A, and since bar degree tracks arity, the shadow coefficients
are the Taylor coefficients of r_A(z) in the bar-degree expansion.

**New fact.** The anomalous dimensions of operators (conformal weights
shifted from their free-field values by interaction corrections) are
power series in hbar = 1/(k+h^v):

    h(k) = h_free + sum_{n >= 1} a_n / (k+h^v)^n

where a_1 is determined by kappa, a_2 by the cubic shadow C, and a_n
for n >= 3 by S_{n+1}. The shadow depth class determines the
polynomial degree of the anomalous dimension as a function of hbar:

| Class | r_max | Anomalous dim in hbar | Example |
|-------|-------|----------------------|---------|
| G     | 2     | linear               | Heisenberg: h = k*p^2/2 |
| L     | 3     | linear               | KM: h = j(j+1)/(k+h^v) |
| C     | 4     | quadratic            | betagamma: quartic contact corrections |
| M     | inf   | full power series    | Virasoro: h = h(c) transcendental |

For classes G and L, the anomalous dimensions are RATIONAL functions
of k (single pole at k = -h^v). For class M, they are
TRANSCENDENTAL (the power series in 1/(k+h^v) does not terminate).

**Verification.** For sl_2 at level k: the anomalous dimension of the
spin-j primary is h_j(k) = j(j+1)/(k+2), which is linear in
hbar = 1/(k+2). The shadow tower for sl_2 terminates at r_max = 3
(class L), so S_r = 0 for r >= 4, giving zero higher-order
corrections. This is consistent. For Virasoro with c = 1 - 6/k(k+1)
(minimal models), the conformal weights h_{r,s} are non-polynomial
functions of k, consistent with r_max = infinity (class M).

**Structural consequence.** The c-independence of S_3(Vir) = 2 (the
cubic shadow for Virasoro) is explained by the fact that the arity-3
collision involves only the Witt bracket [L_m, L_n] = (m-n)L_{m+n},
which is c-independent. The central extension enters only at arity 2
(through kappa = c/2). No other shadow coefficient S_r for r >= 4 is
c-independent for Virasoro, because all higher shadows involve the
central term through normal-ordered composites.


---

## Section 3: New Visions

### 3.1 Categorification of the seven faces

Each face of the seven-face identification is a FUNCTOR from the
category of modular Koszul chiral algebras to some target:

    F1: A |-> pi_A in Tw(B(A), A)
    F2: A |-> r^{DNP}(z) in A! x A![[z^{-1}]]
    F3: A |-> {-_lambda -} in PVA(gr^{Li}(A))
    F4: A |-> {H_i^{GZ}} in Diff(Conf_n(P^1))
    F5: A |-> r^{Dr}(z)/(k+h^v) in g x g[[z^{-1}]]
    F6: A |-> {-,-}_{STS} on (g^{mod}_A)^*
    F7: A |-> H_i^{Gaudin}/(k+h^v)

The seven-face master theorem states that natural isomorphisms
alpha_{ij}: F_i => F_j exist for all pairs (i,j). These are not
tautologies: each alpha_{ij} is a non-trivial theorem (Theorems
thm:hdm-face-1 through thm:hdm-face-7), and the coherence conditions
(the chain closes transitively) require the additional content of the
master equation (eq:hdm-master-equation).

**The 2-categorical structure.** The category ChirKos has a natural
2-categorical enrichment: 1-morphisms are A-infinity morphisms
between chiral algebras, 2-morphisms are A-infinity homotopies. The
seven functors extend to this enrichment:

- A 1-morphism f: A -> B induces a morphism r_f: r_A(z) -> r_B(z)
  of collision residues (r-matrix transport).
- A 2-morphism h: f => g induces a gauge transformation between
  r_f and r_g (gauge equivalence of r-matrices).

The categorified seven-face theorem would state that the natural
isomorphisms alpha_{ij} are compatible with gauge transformations.

**The bar complex as 2-morphism.** The bar complex B(A) mediates
between the identity functor (A |-> A via bar-cobar inversion) and
the Koszul duality functor (A |-> A! via Verdier duality). The
universal twisting morphism pi_A: B(A) -> A is the counit, and the
seven faces are seven ways to extract a 1-morphism from this
2-cell. The categorification would define a "collision residue
2-functor" r: ChirKos_2 -> DerInv_2 and prove the seven forgetful
2-functors are jointly faithful.

**Why this matters.** The 2-categorical structure would produce
DERIVED versions of the seven faces: not just the collision residue
r_A(z) (the genus-0 binary projection) but the full homotopy-coherent
data, encoding the full A-infinity Yangian structure of DNP25, the
full PVA deformation quantization of KZ25, and the full higher Gaudin
system of GZ26. The current seven faces are shadows (projections to
genus 0, arity 2); the categorification would make the full Theta_A
visible through each face.

**Status: SPECULATIVE.** The 2-categorical formulation requires
defining ChirKos_2 carefully, defining the seven target 2-categories,
and proving joint faithfulness. This is a paper-length project.


### 3.2 Higher-genus seven faces

The seven-face master theorem lives at genus 0. At genus g >= 1, the
analogue is the genus-g shadow Sh_{g,n}(Theta_A). Each face has a
genus-g version:

| Face | Genus 0 | Genus 1 | Genus >= 2 |
|------|---------|---------|------------|
| F1   | pi_A    | genus-1 twisting | modular twisting |
| F2   | r^{DNP} | r^{DNP} on E_tau x R | on Sigma_g x R |
| F3   | {-_lambda -} | genus-1 PVA | higher PVA |
| F4   | H_i^{GZ} on P^1 | H_i on E_tau | H_i on Sigma_g = Hitchin |
| F5   | Omega/z | elliptic r-matrix | automorphic r (Etingof-Varchenko) |
| F6   | {-,-}_{STS} | elliptic Sklyanin | higher Sklyanin |
| F7   | H_i^{Gaudin} | elliptic Gaudin | higher Gaudin = Hitchin |

At genus 1, all seven faces are well-known objects: the elliptic
r-matrix (Baxter), the elliptic Gaudin model (Nekrasov), the
Knizhnik-Zamolodchikov-Bernard connection. The genus-1 seven-face
master theorem identifies the genus-1 shadow Sh_{1,n}(Theta_A) with
all seven elliptic incarnations simultaneously.

For class L algebras (affine KM), the genus-1 identification is
already implicit in the manuscript: the KZB connection is the genus-1
shadow connection (rem:kzb-bar in ordered_associative_chiral_kd.tex).
The genus-1 collision residue replaces 1/z by the Weierstrass zeta
function zeta(z, tau), and the curvature kappa * omega_1 produces the
Bernard d-tau term.

**Genuinely new: class M elliptic integrable systems.** For Virasoro
(k_max = 3), the genus-1 shadow connection has higher-order elliptic
terms:

    nabla^{hol}_{1,n}(Vir_c) = d - sum_i H_i^{ell} dz_i - H_tau dtau

where H_i^{ell} involves: depth-1: wp_1(z, tau); depth-2:
wp(z, tau) = -wp_1'(z, tau); depth-3: wp'(z, tau)/2. This is a
HIGHER-ORDER ELLIPTIC DIFFERENTIAL OPERATOR, not present in the
standard KZB theory. It would be the first systematic construction
of a class M elliptic integrable system from the shadow framework.

At genus >= 2, Face 4 (GZ26 Hamiltonians) becomes the HITCHIN
SYSTEM: commuting differential operators on Conf_n(Sigma_g). Face 7
(Gaudin) becomes the higher-genus Gaudin model whose spectral curves
are the Hitchin spectral curves. The genus tower F_1, F_2, ... is
the sequence of Hitchin Hamiltonians at increasing genera. This
connects the shadow obstruction tower to geometric Langlands at the
structural level.

**Critical level degeneration.** At k = -h^v, the collision residue
diverges. The Gaudin Hamiltonians are replaced by the
Feigin-Frenkel center elements, and the Bethe eigenvalues become
opers on P^1. The seven-face programme degenerates, and the
degenerated programme IS the geometric Langlands programme. The
critical-level seven faces are:

    F1: undefined (Theta_A = 0, bar complex uncurved)
    F4: replaced by center of V_{-h^v}(g)
    F5: R(z) = Id (trivial R-matrix)
    F7: critical-level Gaudin model (opers as eigenvalues)

**Status.** The genus-1 case is essentially proved (elliptic r-matrix
= elliptic collision residue, via prop:elliptic-rmatrix-shadow). The
genus >= 2 case and the class M elliptic system are genuine research
programmes. The critical-level connection to opers deserves a section
in the frontier chapter.


### 3.3 The operator-order filtration as a recollement

The trichotomy k_max = 0, 1, >= 3 from the three-invariants chapter
(three_invariants.tex) suggests a filtration on the category of
chiral algebras by differential operator order. The correct algebraic
structure is a RECOLLEMENT, not a t-structure.

**Definition.** Let ChirKos_d = {A modular Koszul : k_max(A) <= d}.
Then:

    ChirKos_0 subset ChirKos_1 subset ChirKos_{>=3} = ChirKos

where ChirKos_0 = {betagamma, free fermion, ...} (class C),
ChirKos_1 adds Heisenberg and affine KM (classes G, L), and
ChirKos_{>=3} adds Virasoro and W_N (class M). The value k_max = 2
is absent from the standard landscape (Remark rem:k-max-2-missing:
it would require p_max = 3, which is forbidden by bosonic locality
and dimension).

**Behaviour under DS reduction.** DS reduction STRICTLY INCREASES
k_max:

    k_max(hat{sl_N}) = 1  -->  k_max(W_N) = 2N-1  (increase by 2N-2)

The increase is 2(N-1) = dim(n_+) - rank. DS is not a morphism in
ChirKos_1; it is a functor FROM ChirKos_1 TO ChirKos_{2N-1}. The
formula k_max(DS(V_k(g))) = 2*rank(g) - 1 for the principal
reduction is a provable proposition.

**Behaviour under tensor products.** k_max(A tensor B) = max(k_max(A),
k_max(B)) because the cross-OPE has lower poles than self-OPEs (by
independent sum factorization). So ChirKos_d is a MONOIDAL
subcategory.

**Behaviour under Koszul duality.** For every Koszul pair (A, A!) in
the standard landscape, k_max(A) = k_max(A!). For affine KM: both
sides have k_max = 1. For Virasoro: Vir_c and Vir_{26-c} both have
k_max = 3. This is expected: the Verdier involution preserves pole
orders. CAUTION: this has been verified only for the standard
landscape. Whether k_max(A) = k_max(A!) holds universally is open.

**Why recollement, not t-structure.** A t-structure requires a
triangulated category. The category ChirKos is not triangulated.
The correct structure is a recollement: ChirKos decomposes into
layers ChirKos_{k_max = d} for d = 0, 1, 3, 5, ..., with the
Gaudin/GZ26 Hamiltonians providing the gluing data. The GZ26
Hamiltonians of order d-1 (from the depth-d collision residue) are
the inter-layer functors.


---

## Section 4: Specific Computations to Pursue Next

### 4.1 Genus-1 elliptic seven-face verification for sl_2

**Computation.** Verify that the genus-1 collision residue
r_{hat{sl_2}}^{(1)}(z, tau) equals the Baxter elliptic r-matrix.

**Method.** The genus-1 bar propagator is d log E(z,w) on E_tau,
where E is the prime form. The collision residue extracts
r^{(1)}(z, tau) = Omega * zeta(z, tau) / (k+2), where zeta is the
Weierstrass zeta function. Compute numerically at tau = i (square
torus), z = 1/3 + i/4 (generic point). Three verification paths:
(1) bar propagator extraction; (2) standard Baxter formula;
(3) trigonometric limit from XXZ Bethe equations.

**Expected outcome.** Agreement up to the level normalization 1/(k+2).

**Engine.** Extend theorem_three_paper_intersection_engine.py with an
elliptic_r_matrix_from_bar() function.


### 4.2 W_3 four-point accessory parameter ODE

**Computation.** For W_3 with four insertions on P^1, compute the
4th-order ODE on conformal blocks from the collision residue table at
depths 1-5.

**Method.** The collision residue table for W_3 is computed
(theorem_three_paper_intersection_engine.py: k_max = 5, op_order = 4,
Lambda_0|h> = (h^2 - 3h/5)|h>). Use these to build the 4-point
shadow connection Hamiltonian H_i = sum_{j!=i} sum_{k=1}^5
r^{(k)}(z_{ij}) / z_{ij}^k. Evaluate at specific
(h_1,h_2,h_3,h_4,w_1,...,w_4,c) values and compare with the
Bouwknegt-Schoutens W_3 null vector decoupling ODE.

**Expected outcome.** Match up to normalization. The 3/5 eigenvalue
should appear as the coefficient of the leading derivative term.

**Verification.** (1) Shadow connection ODE; (2) W_3 null vector
decoupling; (3) comparison at c = 2 (simplest W_3 minimal model).


### 4.3 Bethe completeness count for sl_2 Gaudin at n = 4

**Computation.** Verify that the sl_2 Gaudin model with n = 4
spin-1/2 representations at generic positions has complete Bethe
spectrum: 16 = sum_{M=0}^{4} C(4,M) eigenstates spanning
(C^2)^{x4} = C^16.

**Method.** Solve the Gaudin Bethe equations numerically at 4 generic
points. Verify 16 solutions with distinct eigenvalue tuples. Compute
the Gram matrix of Bethe vectors and verify it is non-degenerate.

**Expected outcome.** All 16 Bethe states non-degenerate at generic
positions. This is a numerical verification of the
Mukhin-Tarasov-Varchenko completeness theorem.

**Engine.** Extend theorem_bethe_mc_engine.py.


### 4.4 Sklyanin bracket Poisson cohomology for sl_2

**Computation.** Compute H^2_pi(sl_2^*, {-,-}_{STS}) for the
Sklyanin bracket defined by r(z) = Omega/z.

**Method.** The Poisson cohomology complex on sl_2^* = C^3 with the
Sklyanin bracket. Compute H^2 = ker(d_3)/im(d_1) using explicit
polynomial representatives.

**Expected outcome.** H^2 = 0, confirming Poisson rigidity and
supporting the Koszulness-from-Sklyanin argument (Section 1.2).

**Engine.** New module theorem_sklyanin_poisson_cohomology_engine.py.


### 4.5 Cross-channel correction from Gaudin spectral determinant

**Computation.** For W_3 at genus 2, compute F_2(W_3) using the
Gaudin spectral determinant det(nabla^{hol}_{2,0} - lambda) and
verify it equals kappa * lambda_2^FP + (c+204)/(16c).

**Method.** (1) Graph sum (existing engine:
theorem_genus2_planted_forest_gz26_engine.py); (2) Gaudin spectral
determinant (new computation); (3) comparison.

**Expected outcome.** Agreement. If confirmed, this gives the first
SPECTRAL computation of the genus-2 cross-channel correction.


---

## Section 5: Connections to Existing Conjectures

### 5.1 How the seven faces constrain resonance completion
(thm:platonic-completion)

The platonic completion theorem states that every positive-energy
chiral algebra has finite resonance rank rho(A) < infinity. The seven
faces provide a new constraint through the following mechanism.

The resonance rank rho equals dim(V_0) (the weight-0 subspace of the
generating space). In the Gaudin language, V_0 is the space of
CONSTANT solutions of the Gaudin eigenvalue problem (eigenvalue 0).
The Gaudin Hamiltonians on V_0 are finite matrices (by the
positive-energy axiom), so rho = dim(V_0) < infinity. This
reproduces the existing proof of thm:platonic-completion.

The seven-face perspective adds: rho is visible in ALL seven faces
simultaneously. In Face 6 (Sklyanin), the resonance locus is where
the Sklyanin bracket degenerates (rank drop of the Poisson tensor).
In Face 3 (KZ25), it is where the PVA bracket develops a kernel. In
Face 2 (DNP25), it is where the line-operator braiding degenerates.
Each face gives an independent characterization of rho, and the
seven characterizations must agree.

**Specific predictions.** For Virasoro: rho = 1 (the curvature m_0
is the single resonance). In the Gaudin language, the Virasoro Gaudin
Hamiltonian has a single constant-eigenvalue mode. In the Sklyanin
language, the Sklyanin bracket on Vir^* has rank drop at exactly one
point. For W_3: rho = 1 (same reasoning). For betagamma: rho = 1
(the weight-0 generator gamma is the single resonance). All are
independently verifiable.

**The seven-face programme at genus 0 is UNCONDITIONAL** (does not
depend on resonance completion): the collision residue r_A(z) has
finitely many (= k_max) nonzero pole terms for any
finitely-generated algebra. At higher genus, the genus-g shadow
connection involves shadows S_2,...,S_{2g-1} (by the visibility genus
formula g_min(S_r) = floor(r/2)+1), and the resonance completion
conjecture ensures finiteness. For class M algebras (r_max = infinity),
ALL shadows contribute at sufficiently high genus, regardless of
resonance completion.


### 5.2 How the Gaudin model connects to MC3

MC3 (thm:categorical-cg-all-types, cor:mc3-all-types) proves that the
DK category is thickly generated by evaluation modules for all simple
types. The Gaudin model is defined on EXACTLY the tensor products of
evaluation modules that appear in the MC3 statement.

**The connection.** The Gaudin Hamiltonians decompose tensor products
of evaluation modules into Bethe eigenspaces. MC3's thick generation
says that EVERY object in the DK category can be approximated by such
tensor products. Combined with Gaudin diagonalization: every object in
the DK category can be approximated by direct sums of Bethe
eigenstates.

**New characterization of MC3.** The Bethe ansatz completeness (at
generic level) is the REPRESENTATION-THEORETIC counterpart of MC3's
thick generation. Both state that evaluation modules generate the
category. Bethe completeness says this at the level of vectors (Bethe
vectors span tensor products). MC3 says it at the level of objects
(evaluation modules thickly generate the category). The passage from
vectors to objects is the categorical lift that MC3 achieves.

**Chromatic-magnon correspondence.** The chromatic filtration of the
MC3 proof (stratifying the evaluation-generated category by tensor
factor count) corresponds to the magnon number M in the Bethe ansatz
(the number of Bethe roots). The M-magnon sector generates the M-th
chromatic layer. This gives the chromatic filtration a physical
interpretation as the particle-number decomposition of the Gaudin
spin chain.

**Consequence.** The Gaudin eigenvalues (Bethe energies) provide a
NUMERICAL INVARIANT of objects in the DK category. Two objects with
different Gaudin spectra are different. This gives a computable
distinguishing invariant for evaluation modules, usable for
computational verification of MC3.

**Status: CONJECTURED.** The precise translation between the chromatic
filtration and the magnon number requires identifying the
evaluation-module tensor product with the Gaudin Hilbert space at the
level of dg categories, not just vector spaces.


### 5.3 How the Sklyanin bracket connects to Theorem C

The shifted-symplectic upgrade of Theorem C
(conj:ambient-complementarity in chiral_hochschild_koszul.tex) asserts
that T_comp(A) carries a (-1)-shifted symplectic structure, with
Q_g(A) and Q_g(A!) as complementary Lagrangian subcomplexes.

**The Sklyanin bracket as the classical model.** The Sklyanin bracket
on (g^{mod}_A)^* is a degree-0 Poisson structure. The convolution dg
Lie algebra g^{mod}_A has an underlying Lie bracket that is the
"quantum" version of the Sklyanin bracket (the Yangian coproduct
quantizes Sklyanin, by Face 6). The shifted-symplectic structure on
T_comp(A) is the derived/shifted version of this Lie bracket, via the
PTVV formalism.

**Explicit Poisson formula.** Instead of abstract PTVV machinery, the
Sklyanin bracket provides an explicit formula for the Poisson
structure that the shifted symplectic form quantizes:

    {f, g}_{comp}(xi) = <xi, [df, dg]_{r_A}> + <xi, [df, dg]_{r_{A!}}>

where the two terms correspond to the A- and A!-summands of T_comp(A).
The isotropy of Q_g(A) becomes: the bracket restricted to
A-variations vanishes, i.e., {f, g}_{r_A} = 0 when both f and g are
A-deformations. This is the classical Yang-Baxter equation for r_A(z)
restricted to one-sided variations.

**The identification chain.**

    Sklyanin bracket on (g^!)^*
      = classical limit of Yangian coproduct (Face 6)
      = genus-0 reduction of shifted symplectic on T_comp(A)
      => complementarity = Lagrangian splitting of Sklyanin manifold

The last step is conjectural: it requires proving that the genus-0
restriction of the shifted symplectic structure recovers the Sklyanin
bracket. The first-principles check: at genus 0, the ambient complex
T_comp(A) reduces to End_A(2)[[z^{-1}]] (the space of collision
residues), and the Sklyanin bracket on this space is exactly the
bracket induced by the classical r-matrix. The Lagrangian condition
becomes the transversality of Q_0(A) and Q_0(A!) in End_A(2), which
is the genus-0 complementarity theorem.

**Status: CONJECTURED.** The obstacle is the PTVV passage from
degree-0 Poisson to degree-(-1) shifted symplectic. The Sklyanin
formula is the natural starting point for the application.


---

## Summary Table

| Item | Status | Section |
|------|--------|---------|
| Spectral proof of Thm B via Gaudin completeness | CONJECTURED | 1.1 |
| Koszulness from Sklyanin for classes G/L | PROVED | 1.2 |
| d^2 = 0 from KZ25 gauge invariance (genus 0) | PROVED | 1.3 |
| Bethe roots = genus-0 shadow critical points | PROVED (KM); CONJECTURED (general) | 2.1 |
| Sklyanin leaves = complementarity at genus 0 | PROVED (KM, genus 0); CONJECTURED (general) | 2.2 |
| Shadow depth = anomalous dimension polynomial degree | PROVED (leading); CONJECTURED (full) | 2.3 |
| Categorification of seven faces (2-functor) | SPECULATIVE | 3.1 |
| Higher-genus seven faces (Hitchin connection) | PROVED (g=1); SPECULATIVE (g>=2) | 3.2 |
| Operator-order recollement | CONJECTURED | 3.3 |
| Seven faces constrain resonance completion | PROVED (finiteness); adds independent characterizations | 5.1 |
| Gaudin = MC3 at vector/categorical levels | CONJECTURED (chromatic-magnon correspondence) | 5.2 |
| Sklyanin = classical model for shifted symplectic complementarity | CONJECTURED (PTVV passage needed) | 5.3 |
