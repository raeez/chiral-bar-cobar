# MASTER CATALOGUE — ALL ITEMS IN LIMBO

88 items total: 28 from the Research Log, 35 from Vol I dirty state, 25 from Vol II dirty state.

---

## I. NEW CONSTRUCTIONS FROM THE RESEARCH LOG (RL-1 through RL-28)

These are the genuinely new ideas, constructions, and perspectives developed
in the research log thread on open/closed modular E_1-chiral homotopy theory.
They represent the conceptual reorientation that the rewrite must integrate.

### RL-1. The open sector as primary object

The primitive datum of modular chiral homotopy theory is not a single chiral
algebra but a cyclic factorization dg-category C_op on the real-oriented
blowup of a punctured curve. A boundary algebra A_b = End(b) is a chart on
this categorical object, not the object itself.

**Why this matters:** Currently both volumes treat the chiral algebra A as the
primitive and build everything from it. But A depends on a choice of boundary
vacuum b. The intrinsic object is the Morita class of C_op. This is not mere
abstraction — it is the reason Koszul duality is Morita-invariant, the reason
complementarity holds, and the reason modularity is trace-based.

**Where it must appear:** Vol I introduction, Vol I preface, Vol II preface,
concordance, every chapter that says "let A be a chiral algebra" should
acknowledge that A is a presentation of C_op.

### RL-2. Tangential log curves (X, D, tau)

Let X be a smooth algebraic curve, D = {p_1,...,p_r} a finite reduced divisor,
tau_{p_i} in T_{p_i}X \ {0} a tangential direction at each puncture. The real
oriented blowup X~_D -> X produces boundary circles S^1_{p_i}. Removing the
tangential basepoint yields intervals:

    I_{p_i} := S^1_{p_i} \ {tau_{p_i}} ~ R.

This is the global domain of the open color. On a plain smooth curve there is
no honest boundary, hence no canonical open sector. The puncture structure is
necessary.

**Key geometric point:** The tangential data tau is not decorative. It
linearizes the boundary circle into an interval, which is what makes the
E_1/ordered structure visible. Different choices of tau give Morita-equivalent
but not isomorphic presentations.

### RL-3. Mixed configuration spaces

    Conf^{oc}_{I,m}(X,D,tau) := Conf_I(X \ D) x prod_j Conf^{ord}_{m_j}(I_{p_j})

Interior points: unordered, holomorphic dependence.
Boundary points: ordered, locally constant (topological/E_1).

Their log-Fulton-MacPherson compactification FM^{oc,log}_{I,m}(X,D,tau) has
four types of codimension-one strata:
  (i)   interior cluster collapses (holomorphic)
  (ii)  consecutive boundary points merge (E_1/associative)
  (iii) interior point approaches a boundary circle (mixed/bubbling)
  (iv)  nodal degeneration (clutching)

These four strata are exactly the four terms of the modular MC equation.

### RL-4. Mixed Ran space Ran^{oc}(X,D,tau)

    Ran^{oc}(X,D,tau) := coprod_{I,m} Conf^{oc}_{I,m}(X,D,tau) / Sigma_I

The colored Ran space. The closed color sees Ran(X \ D). The open color sees
ordered configurations on boundary intervals. Factorization is compatible with
the coloring.

### RL-5. Open/closed factorization dg-category

A constructible dg-cosheaf C on Ran^{oc}(X,D,tau) satisfying:
  (i)   Factorization on disjoint unions
  (ii)  Holomorphic locality in the closed direction X \ D
  (iii) Local constancy in each boundary interval I_{p_j}
  (iv)  Local model: W(SC^{ch,top})-algebra in formal collars
  (v)   Weiss descent for mixed configurations

This is the correct globalization of the local Swiss-cheese package.

**IMPORTANT:** This is a DEFINITION, not a theorem. The hard theorem is that
specific theories (Heisenberg, KM, Virasoro, W_N, ...) produce such objects.
Do not conflate defining the framework with populating it.

### RL-6. Boundary algebra as endomorphism chart

Choose a small interval J subset I_{p_j} and a compact generator b in C(J).
Define A_b := RHom_{C(J)}(b,b). Then A_b is naturally an A_infty-chiral
algebra.

**Proof mechanism:** Local constancy along J gives A_infty composition;
holomorphic dependence on nearby interior insertions gives spectral lambda-
dependence; FM compactification strata give Stasheff faces; Stokes gives the
A_infty identities.

### RL-7. Morita invariance of the open sector

If b, b' are two compact generators of C(J), then Perf(A_b) ~ Perf(A_{b'}).
Hence the intrinsic object is the Morita class.

**Consequence:** The derived center Z_ch(C_op) ~ C^bullet_ch(A_b, A_b) is
independent of the choice of generator. This is why bulk is well-defined.

### RL-8. Chiral Hochschild cochains C^bullet_ch(A,A)

Explicit coordinate definition:

    C^n_ch(A,A) := Hom(A^{otimes n}, A((lambda_1))...((lambda_{n-1})))

with differential delta = [m, -]_{brace}, where m = m_1 + m_2 + m_3 + ...

The brace operations are defined by:

    f{g_1,...,g_r} = sum_{1 <= i_1 < ... < i_r <= m} +/- f o_{i_r} g_r o_{i_{r-1}} g_{r-1} ... o_{i_1} g_1

where o_i is partial composition with spectral substitution Lambda_i := lambda_i + ... + lambda_{i+n-1}.

### RL-9. Chiral brace algebra theorem

(C^bullet_ch(A,A), delta, {-}) is a brace dg algebra. Hence the Gerstenhaber
bracket [f,g] := f{g} - (-1)^{...} g{f} makes it a dg Lie algebra, and
cohomology HH^bullet_ch(A) is a Gerstenhaber algebra.

**Proof:** Brace identity follows from associativity of block-substitution of
spectral variables (operadic associativity of o_i). delta^2 = 0 because
A_infty identities are [m,m] = 0. Dg Lie is standard from brace identities.

### RL-10. Chiral Deligne-Tamarkin-Swiss-cheese theorem

For every A_infty-chiral algebra A, the pair

    U(A) := (C^bullet_ch(A,A), A)

is a local chiral Swiss-cheese pair. Moreover it is INITIAL among such pairs
with fixed open color A: if (B,A) is any other such pair, there is a unique
morphism Phi: B -> C^bullet_ch(A,A) compatible with the action on A.

**THIS IS THE KEY THEOREM.** It says: every boundary algebra has a universal
bulk, namely its chiral center. The bulk is not guessed or constructed ad hoc
— it is forced by a universal property.

**Proof:** Define Phi(b)_n(a_1,...,a_n) := mu_{1;n}(b; a_1,...,a_n). This is
a chiral cochain by sesquilinearity of the mixed operations. Compatibility
with braces follows from the Swiss-cheese codimension-one identity. Uniqueness
is tautological: a morphism over A is determined by what a closed element does
to arbitrary strings of open inputs.

### RL-11. Bulk = derived center of the open sector

    Z_ch(C_op) := RHom_{Fun(C_op,C_op)}(Id, Id) ~ C^bullet_ch(A_b, A_b)

for every compact generator b. Independent of choice by Morita equivalence.

**This is the corrected "why 2d+1" answer.** Not "the bar complex has an E_1
direction." Rather: the derived center of a codimension-one boundary algebra
is the universal one-dimension-up acting algebra. The extra dimension is the
normal center direction of the boundary, not the bar ordering direction.

### RL-12. The 2d->3d mechanism: center theorem, not bar ordering

**REFINED after Beilinson pass:** Both perspectives coexist. The bar coalgebra
IS the correct open-sector model in a collar neighborhood (deconcatenation =
factorization along R). But the bar model does not explain the BULK. The bulk
is the center. So:

  - Bar/cobar: represents twisting morphisms and couplings
  - Hochschild cochains/center: IS the acting bulk algebra
  - These are distinct objects with distinct roles

Do NOT set up a false dichotomy. The bar complex remains central to the
theory. But it is the open-sector coalgebra, not the bulk algebra.

### RL-13. Geometric origin: derived self-intersection

DISCARDED AS THEOREM (Beilinson pass). The formula O(L x^h_M L) ~ Bar(A)
requires strong assumptions (smooth, affine, char 0) not developed in the
manuscript. Keep as a motivating remark/analogy. Do not promote to theorem.

### RL-14. Bar/cobar vs center distinction

  - Bar/cobar represents twisting morphisms:
      Hom(Omega C, A) ~ Tw(C,A) ~ Hom(C, BA)
  - Center/cochains is the acting bulk:
      Z^ch_der(A) = C^bullet_ch(A,A)
  - Modular MC element Theta lives in the convolution algebra, which is
    the home of twisting morphisms, not the center itself.

These three levels must never be conflated.

### RL-15. Modular twisting morphism

    Theta_C: C^{oc,log}_{mod}(X,D,tau) -> End(Z_ch(C_op), C_op)

from the mixed log-modular cooperad into the endomorphism operad of the
universal bulk-boundary pair.

**REFINED after Beilinson pass:** The cooperad C^{oc,log}_{mod} is not yet
defined in the manuscript. This is a DEFINITION TO CONSTRUCT, not a theorem
to cite. The definition requires the mixed configuration spaces (RL-3) and
their log-FM compactifications with all four types of codimension-one strata.

### RL-16. Modular MC equation with clutching

    d Theta + (1/2)[Theta, Theta] + Delta_{clutch}(Theta) = 0

The four codimension-one boundary types give:
  (i)   d Theta: chain boundary on compactified configuration/moduli spaces
  (ii)  [Theta, Theta]: composition of two lower-depth operations
  (iii) Delta_{clutch}: nodal degeneration
  (iv)  Mixed terms from bubbling

Summing all codimension-one boundary components gives zero (Stokes).

### RL-17. Modularity = trace + clutching on the open category

The hierarchy of adjectives:
  - chiral = local holomorphic factorization data in the closed direction
  - open/Swiss-cheese = two-color extension coupling closed to boundary/defect
  - cyclic = existence of traces on open defects
  - traced = open-to-closed map through chiral Hochschild theory
  - ribbon = trace compatible with rotation/Virasoro/framing
  - modular = ribbon-trace data survives log-FM clutching across nodal degenerations

So: modularity is not an axiom on the closed algebra. It is a trace theorem
of the open category.

### RL-18. Cyclic structure as boundary Calabi-Yau

A cyclic open factorization category is C_op with a trace:

    Tr_b: RHom(b,b) -> k[-d]

nondegenerate and compatible with factorization and transport.

### RL-19. Annulus = Hochschild chains

    int_{S^1_p} C_op ~ HH_*(C_op)

by cutting the circle into an interval and applying excision + cyclic bar.
This is the first modular shadow: the annulus is a trace, not a closed-sector
primitive.

### RL-20. Khan-Zeng dimensional constraint

DISCARDED (Beilinson pass). The (d,k) = (1,1) constraint applies only to
freely generated PVA gauge theories, not to all chiral algebras. The general
2d->3d mechanism is the center theorem (RL-10), not a dimensional argument.
Keep as a remark in the PVA/HT chapter, not as a general principle.

### RL-21. Propagator factorization

REFINED (Beilinson pass). The formula P(t,z) ~ Theta(t)/(2pi i z) holds for
abelian theories on C x R. Keep as motivating computation for the Heisenberg
example, not as a general principle. Nonabelian theories have corrections.

### RL-22. Spectral parameter dictionary

    r(z) = sum_{alpha,beta} Phi_alpha tensor Phi_beta int_0^infty d lambda e^{-lambda z} {Phi_alpha}_lambda Phi_beta}

The line-operator spectral kernel is the Laplace transform of the lambda-bracket.

REFINED: This holds for polynomial lambda-brackets. General case needs
distributional treatment. State the polynomial case as a theorem; flag the
general case as requiring completion.

### RL-23. One-step Jacobi coalgebra

Given F = (F_1,...,F_r): (A^n, p) -> (A^r, 0), define:

    J_{F,p} := (S^c(sU + R), b_F)

where U = T_p A^n, R = k^r, and the coderivation b_F is determined by:

    b_F(se_{i_1} ... se_{i_n}) = sum_alpha (1/n!) (d^n F_alpha / dx_{i_1}...dx_{i_n})(p) r_alpha

Its cobar algebra Omega(J_{F,p}) is the exact pointed line algebra.

The explicit A_infty model on K^{gr}_{F,p} = k[c_alpha] tensor Lambda(lambda_i):

    m_n(lambda_{i_1},...,lambda_{i_n}) = sum_alpha c_alpha (1/n!) (d^n F_alpha / dx_{i_1}...dx_{i_n})(p)

extended as multiderivations. Three immediate subexamples:
  - F = 0: free case, m_n = 0 for n >= 3
  - F = x^2: quadratic, m_2(lambda,lambda) = 2c, rest zero
  - F = x^3: cubic, m_3(lambda,lambda,lambda) = 6c, rest zero

This is a beautiful concrete construction that makes the staircase visible at
the level of Taylor coefficients.

### RL-24. Boundary-linear LG theorem

For W(x,y) = <y, F(x)>, the boundary algebra is the Koszul dg algebra:

    A_F = (k[[x_1,...,x_n]] tensor Lambda(eta_1,...,eta_r), d eta_alpha = F_alpha(x))

By dg HKR:

    Z^ch_der(A_F) ~ HH^bullet(A_F) ~ O(T*[-1] Z^der_F) ~ O(dCrit(W))

So: bulk = functions on the derived critical locus of the superpotential.
This is the exact interacting model of "bulk = derived center of open sector."

### RL-25. Complementarity as duality witness

    kappa(A) + kappa(A^vee) = constant
    F_1(A) + F_1(A^vee) = constant/24

Explicit values:
  - Heisenberg: kappa + kappa' = 0
  - affine sl_2: kappa + kappa' = 0 (under k -> -k-4)
  - Virasoro: kappa + kappa' = 13 (under c -> 26-c)
  - W_3: kappa + kappa' = 250/3 (under c -> 100-c)

Genus-one modularity is the first observable shadow of duality.

### RL-26. Chiral Cartan formula

For Virasoro: [T, f] = partial f + delta(iota_T f), so [partial] = 0 in
H^bullet(C^bullet_ch). An inner Virasoro element upgrades HT to topological.

This is the chain-level universal-bulk version of Khan-Zeng's theorem.

### RL-27. W_3 composite nonlinearity as structural necessity

{W_lambda W} forces composite Lambda = :TT: - (3/10) partial^2 T into the
bracket. This cannot close in the linear span of T, W. The theory ceases to
be even approximately quadratic.

Consequence: the open category for W_3 is genuinely beyond modules over a
single linear algebra. Composite fields are categorical necessity.

### RL-28. The staircase of examples

    Free (strict) -> Heisenberg (spectral) -> cubic LG (first m_3)
      -> affine sl_2 (nonabelian + complementarity)
      -> Virasoro (wheel + infinite tower + Cartan)
      -> W_3 (composite nonlinearity + quartic resonance)

This is not a list. It is a staircase: each example reveals a new structural
layer of the theory. The staircase should be a chapter in its own right.

---

## II. DIRTY WORKING STATE IN VOL I (V1-1 through V1-35)

### V1-1. Preface editorial overhaul
+510 lines modified. Heisenberg MC element, generating function,
complementarity formula, multi-generator W-algebra patterns all refined.
Not yet in final form. Missing the open-sector thread entirely.

### V1-2. Introduction scope narrowing
"Standard examples" -> "Free-field examples"; multi-generator universality
now OPEN for W_N at g >= 2. Propagation to all downstream uses incomplete.
AP7 (scope inflation) partially addressed but not fully checked.

### V1-3. Higher-genus propagator formula
Expanded from vague "(period corrections)" to explicit formula:

    eta^{(g)}_{12} = d log E(z_1,z_2) + sum (Im Omega)^{-1}_{alpha beta} omega_alpha(z_1) bar{omega}_beta(z_2)

Not yet cross-checked against all downstream uses in examples chapters.

### V1-4. Concordance expansion (+445 lines)
Constitution tracks full proof-chain dependencies, AP11 flags, genus/level
qualifications. Does NOT yet incorporate the open-sector/center perspective.
Does not yet have a section on the center theorem.

### V1-5. Koszulness meta-theorem count
10 unconditional + 1 conditional + 1 one-directional. K-numbering (K1-K12 in
preface) vs meta-theorem items (i)-(xii) still not perfectly aligned. Prior
audit found 6/12 items differed. This mismatch is editorial debt.

### V1-6. MC frontier status
MC1,2,4,5 proved; MC3 type A proved; arbitrary type open. Reflected in
concordance but the treatment tells the MC story as five separate problems
rather than as projections of the single universal twisting morphism Theta_A.
The rewrite should unify the MC narrative.

### V1-7. Shadow Postnikov tower as finite-order projections
Theta_A^{<=r} machinery fully developed in higher_genus_modular_koszul.tex
(172 ProvedHere claims). Not yet reframed through the open-sector lens.
The shadow obstruction tower should be presented as the Taylor expansion of the modular
twisting morphism Theta_C (RL-15).

### V1-8. Three-pillar integration
11 identification theorems stated. Mok25 dependency (single-source, ambient
D^2=0) still not cleanly isolable in the exposition. The concordance has
fallback clauses but they are buried. AP11 (single external dependency)
applies. Must be frontlit.

### V1-9. Arithmetic shadows programme
Shadow depth = 1 + d_arith + d_alg. L-function content. Hecke eigenforms.
+184 lines but needs the spectral-parameter / Laplace-transform dictionary
(RL-22) to connect to open-sector spectral data. Also needs Beilinson pass
on the Kummer motive / motivic decomposition claims.

### V1-10. Shadow growth rate rho(A)
Convergence radius, critical cubic, Vieta structure. Proved but not yet
connected to open-sector categorical invariants. Should be framed as a
property of the modular twisting morphism's Taylor radius.

### V1-11. Yangians: Coulomb branch + CoHA sections
New conjectures on CoHA/E_1-chiral duality. Not yet connected to the
open-sector / line-category picture. The Yangian IS the E_1-chiral Koszul
dual, so the open-sector picture should illuminate its role.

### V1-12. Non-principal W-duality frontier
Hook-type corridor proved in type A; transport propagation. The open-sector
perspective should reframe this: Koszul duality for W-algebras is Morita
equivalence of boundary categories under DS reduction.

### V1-13. Analytic sewing programme
HS-sewing proved; Heisenberg sewing proved; sewing envelope A^{sew}. But
analytic completion not yet formulated in terms of the open-sector
categorical trace. The sewing envelope should be the Hausdorff completion
of the boundary algebra in the trace topology induced by the cyclic structure.

### V1-14. Modular Koszul datum Pi_X(L)
Six-fold datum from cyclically admissible Lie conformal algebra. REFINE:
the modular Koszul datum should be the initial data for the open/closed
factorization category, not a standalone six-fold datum. Reframe as:
Pi_X(L) encodes the data needed to construct C_op on (X, D, tau).

### V1-15. Factorization envelope technology
U^{mod}_X as left adjoint of Prim^{mod}. DISCARD AS THEOREM: this is
conjectural at the modular level. Keep as a clearly marked conjecture.

### V1-16. Cubic gauge triviality + independent sum factorization
Proved but not connected to the categorical trace perspective. Should be
connected: gauge triviality at arity 3 is the statement that the cyclic
trace kills certain deformations.

### V1-17. Shadow metric Q_L, shadow connection nabla^{sh}, propagator variance delta_mix
Proved Ring 2 results. Need integration with open-sector spectral data.
The shadow metric should be presented as the quadratic form on the modular
tangent complex, not as a standalone invariant.

### V1-18. Arithmetic packet connection nabla^{arith}_A
DISCARD FROM MAIN DEVELOPMENT (Beilinson pass). Conflates L-functions with
shadow obstruction tower in ways not yet falsification-tested. Move to clearly marked
frontier appendix.

### V1-19. 24 new ProvedHere claims
Scattered across theory/examples/connections. Need propagation verification
(AP5: local fix, global neglect). Run beilinson_auditor.py after rewrites.

### V1-20. Beilinson auditor framework
compute/lib/beilinson_auditor.py (44KB) untracked. Computational
falsification engine implementing upstream-first DAG verification. Needs
integration into the build system.

### V1-21. Planted forest amplitude engine
compute/lib/planted_forest_amplitude_engine.py (30KB) untracked. Log-FM
amplitude computation. Implements the combinatorial heart of the modular
cooperad.

### V1-22. 12 new bottleneck test files
Untracked in compute/tests/. Theorem-dependency verification. Need to be
added to the test suite.

### V1-23. E_1 modular Koszul duality chapter
Standalone chapter exists but does not yet make the connection to the chiral
Deligne-Tamarkin theorem explicit. This chapter should be the place where
the ribbon/'t Hooft bridge (V2-24) lands in Vol I.

### V1-24. Holographic modular Koszul datum H(T)
Six-component packaging (A, A^!, C, r(z), Theta_A, nabla^{hol}). But the
"why 2d+1" explanation in the holomorphic_topological chapter is still the
old bar-ordering story. Must be rewritten using the center theorem.

### V1-25. THQG chapters (14 files)
G1-G10 all marked ProvedHere. REFINE: several (G4 S-duality, G8
reconstruction) rest on conditional physics inputs. Downgrade to Conditional
where physical axioms (H1)-(H4) are assumed.

### V1-26. Chriss-Ginzburg tautological programme
Shadow CohFT, MC tautological descent, WDVV from MC, Givental R-matrix. In
higher_genus_modular_koszul.tex. Needs open-sector categorical interpretation:
the CohFT should be the trace of the open sector's modular MC element.

### V1-27. W_3 composite field chapter
All coefficients explicit. Not yet connected to the chiral Hochschild / brace
perspective. Should state: the composite Lambda is forced because the brace
operations on C^bullet_ch do not close in the linear span.

### V1-28. Bar complex tables
Machine-verified entries. Complete but static. No changes needed beyond
cross-references.

### V1-29. Configuration spaces chapter
Arnold relations, FM compactification, log forms. Does NOT include log-FM on
bordered curves (RL-3). This is the most critical gap in the foundations.

### V1-30. Chiral Hochschild chapter
Currently only the closed-sector Hochschild. Does not contain braces, does
not contain the center theorem. Must be expanded per Cluster A.

### V1-31. PBW propagation theorem
MK3 follows from MK1 for all CFT-type algebras. Five main theorems from
genus-0 + D^2=0. This is a powerful simplification that should be promoted:
it means the entire Ring 1 core follows from just two inputs.

### V1-32. Convolution algebra: strict vs homotopy
Conv_str vs Conv_infty. Distinguished in CLAUDE.md but the manuscript still
occasionally blurs them. Systematic check needed.

### V1-33. Depth filtration and tridegree
(g,n,d) = (loop genus, arity, log boundary depth) from Mok's stratification.
Not yet in the introduction. Should be stated early as a fundamental grading.

### V1-34. Genus spectral sequence
E_1 page isolates tree/one-loop/genus-2 data. Distinct from PBW spectral
sequence. Underexploited in the current exposition.

### V1-35. Modular tangent complex
L_infty twisted differential d_{Theta_A}(x) = sum (hbar^g/n!) l^{(g)}_{n+1}(Theta_A^{tensor n}, x).
Stated but not connected to derived deformation theory of the open sector.
Should be: the modular tangent complex is the tangent complex of the MC
moduli space of the modular twisting morphism.

---

## III. DIRTY WORKING STATE IN VOL II (V2-1 through V2-25)

### V2-1. A_infty-chiral algebra axioms
Defined in axioms.tex with sesquilinearity, unitality, spectral A_infty
identities. THIS IS the correct local definition. Already precise.
Needs consistency check with Vol I conventions (desuspension, sign).

### V2-2. Swiss-cheese operad SC^{ch,top}
Two-colored operad defined in locality.tex/foundations.tex:
  SC(ch^k; ch) = FM_k(D)
  SC(ch^k, top^m; top) = FM_k(D) x E_1(m)
No open-to-closed operations. Local recognition theorem proved.
Homotopy-Koszulity proved (via Kontsevich formality + classical SC transfer).

### V2-3. Operad => axioms (F4) and axioms => operad (F5)
Both PROVED. Local equivalence established under tameness/logarithmic hypotheses.

### V2-4. PVA descent D2-D6
ALL PROVED via exchange cylinder + three-face Stokes on FM_3(C).
Repaired versions in pva-descent-repaired.tex.

### V2-5. Raviolo vertex algebras
SC -> raviolo restriction via time-slices. Defined in raviolo.tex.
Raviolo as derived pushout: pt coprod^h_{[0,1]} pt ~ S^0.

### V2-6. Bulk-boundary-line triangle
A_bulk ~ Z_der(B_partial) ~ Z_der(C_line) ~ HH^bullet(A^!), C_line ~ A^!-mod.
Stated in ht_bulk_boundary_line_core.tex (+1075 lines). PROBLEM: framed as
specific to HT theories, not as the universal center theorem.
THE REWRITE: promote this to a universal theorem (consequence of RL-10).

### V2-7. Chiral Hochschild cochains as brace algebra
brace.tex defines braces on FM(C) x Conf(R). KEY FILE. Not yet connected to
the chiral Deligne-Tamarkin theorem. Must be upgraded with the initiality
proof (RL-10).

### V2-8. Bar-cobar review / GLZ extension
bar-cobar-review.tex (+988 lines). Reviews GLZ quadratic duality and
non-quadratic extensions. Solid background material.

### V2-9. Spectral braiding
spectral-braiding-core.tex (+159 lines). r(z) and coproduct Delta_z on A^!.
Needs connection to Laplace transform dictionary (RL-22).

### V2-10. Modular PVA quantization
modular_pva_quantization_core.tex (+138 lines). Quantization of coisson to
vertex. Should be connected to the modular completion framework (RL-15 through RL-17).

### V2-11. Line operators chapter
Chiral structures on line operators. Connects to Dimofte-Niu-Py 2025. Should
be framed as: line operators are objects of C_op, with A^!-module structure
as a presentation via a chosen generator.

### V2-12. Log HT monodromy
Logarithmic HT monodromy from log-FM compactification. Connects to RL-3.

### V2-13. Anomaly-completed structures
REFINE: physics-motivated; keep but qualify as conditional on (H1)-(H4).

### V2-14. 3D gravity from E_1-chiral Koszul duality
Direct link to the "why 2d+1" question. Should be grounded in the center
theorem after the rewrite.

### V2-15. Celestial boundary transfer
REFINE: Ring 3 frontier. Mark explicitly as conditional.

### V2-16. YM synthesis
Yang-Mills boundary algebra computation. Connects to Vol I YM chapters.

### V2-17. Affine half-space BV
BV theorem transport to Virasoro/W_3 via Drinfeld-Sokolov reduction.

### V2-18. Rosetta stone + examples
Cross-framework dictionary. Explicit computations for Virasoro, W_3, W_infty.

### V2-19. FM calculus chapter
Proves A_infty relations from Stokes on FM compactifications. Foundational.

### V2-20. THQG extension files (37 files)
Massive physics-facing extension. REFINE: do not let Ring 3 extensions inflate
the proved core's appearance. Status varies; audit needed.

### V2-21. Appendices: brace signs, FM proofs, orientations, PVA expanded
Technical detail. Needs consistency check against Vol I sign conventions
(appendices/signs_and_shifts.tex is AUTHORITATIVE for Vol I).

### V2-22. Preface/introduction
Motivates holomorphic x topological; bar complex as unified structure. Does
NOT yet present the open-sector-primary perspective. Critical rewrite needed.

### V2-23. Concordance Vol II
Cross-reference to Vol I. Needs the open-sector reframing.

### V2-24. Ribbon/'t Hooft bridge
PROVED: cyclic trace + matrix realization -> 't Hooft sums with N^{chi(Sigma_Gamma)}.
Important result. Not yet connected to RL-17 (modularity = trace + clutching).
The 't Hooft expansion IS the open-sector trace on the ribbon modular operad.

### V2-25. Seven cross-volume bridges
Bar-cobar, Hochschild, DK-YBE, W-algebra, relative holographic, Loop-Connes,
BV functor. Five proved, two conjectural. The Hochschild bridge should be
upgraded from conjectural to a consequence of the center theorem.
