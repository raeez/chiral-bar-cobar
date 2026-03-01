0) Panoramic map
0.1 Global structure of main.pdf (832pp)

The manuscript is explicitly organized into at least three large blocks:

Part I: Theory (starts p. 37) with Chapters 1–15: Introduction; algebraic foundations; BD chiral algebras vs factorization algebras; configuration spaces; bar/cobar constructions; Verdier/Koszul duality; completions; and an operadic/NAP layer. This is visible already in the Contents: “I Theory … 1 Introduction … 2 Algebraic Foundations … 3 Chiral Algebras and Factorization Algebras … 4 Configuration Spaces … 5 The Bar Construction …” etc.

main

main

main

Part II: Examples (starts p. 497): “II Examples … 16 E∞-Chiral / Vertex Algebras … 17 Heisenberg Chiral Algebra … 18 Affine Kac–Moody Chiral Algebra … 19 Virasoro Chiral Algebra … 20 W-algebras … 21 Complexes for Chiral Algebras in Practice …” etc.

main

main

main

Part III: Connections and Applications (starts p. 657), explicitly labeled as such in the manuscript’s own summary/structure notes.

main

There is also a substantial Appendix complex (A–G) used for configuration-space geometry, residue identities, sign tables, and physical commentary (e.g. Appendix G for the E1-chiral terminology/definition). The E1-chiral notion is explicitly postponed to Appendix G and Chapter 32.

main

main

0.2 The dependency spine (what the manuscript actually uses)

I will write the spine in “definitions ⇒ lemmas ⇒ theorems ⇒ applications” form, and I will flag where the manuscript’s own status tags indicate missing rigor.

(S0) BD/factorization interface.

Factorization algebra definition: Definition 3.10.5 (FA1–FA5 style axioms on disks).

main

Claimed equivalence direction “chiral ⇒ factorization”: Theorem 3.10.7 ([proved here]).

main

“Factorization homology via configuration spaces”: Theorem 4.1.35 ([proved elsewhere]).

main

(S1) Configuration spaces + residues.

Fulton–MacPherson compactification: Theorem 4.1.4 ([proved here]).

The basic residue apparatus (logarithmic forms on the compactification): Theorem 4.1.26 ([proved here]).

But a basic ingredient is still marked open: Lemma 4.1.25 ([open]) about a “basic logarithmic form” with residue 1.

(S2) Arnold/Orlik–Solomon control of
𝑑
2
d
2
.

Arnold’s relation for
𝜔
𝑖
𝑗
=
𝑑
log
⁡
(
𝑧
𝑖
−
𝑧
𝑗
)
ω
ij
	​

=dlog(z
i
	​

−z
j
	​

): Theorem 4.7.20 ([proved here]).

A global boundary-strata version is only open in Appendix A: Theorem A.12.1 ([open]) “Configuration space boundary relations.”
This is structurally critical: it is precisely the missing bridge between local Arnold relations and the global “residue differential squares to zero” mechanism.

(S3) The geometric bar complex and its differential.

Bar complex definition: Definition 5.1.53 defines
𝐵
‾
c
h
(
𝐴
)
(
𝑈
)
B
ch
	​

(A)(U) as a direct sum over
𝑛
n of
Γ
(
𝐶
𝑛
+
1
(
𝑈
)
,
𝜋
∗
𝐴
⊠
(
𝑛
+
1
)
⊗
𝜔
𝐶
𝑛
+
1
(
𝑈
)
log
⁡
)
[
𝑛
]
Γ(C
n+1
	​

(U),π
∗
	​

A
⊠(n+1)
⊗ω
C
n+1
	​

(U)
log
	​

)[n].

main

Differential decomposition
𝑑
=
𝑑
i
n
t
+
𝑑
d
R
+
𝑑
r
e
s
d=d
int
	​

+d
dR
	​

+d
res
	​

: Definition 5.1.55.

main

Nilpotence claim: Theorem 5.1.20 ([proved here]) states
𝑑
2
=
0
d
2
=0 and sketches a “nine-term cancellation.”

Coalgebra structure: Theorem 5.1.69 ([proved here]) asserts
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) is a chiral coalgebra.

(S4) The geometric cobar and bar–cobar duality.

The introduction advertises a “Geometric Cobar Construction” but marks it open at the level of global statement: Theorem 1.7.3 ([open]).

main

The actual cobar definition is analytic/distributional: Definition 5.2.6 defines
Ω
c
h
𝑝
,
𝑞
(
𝐶
)
Ω
ch
p,q
	​

(C) as distributional sections of
H
o
m
‾
𝐷
(
𝜋
∗
(
𝐶
⊗
(
𝑝
+
1
)
)
,
𝐷
𝐶
𝑝
+
1
(
𝑋
)
)
⊗
Ω
𝐶
𝑝
+
1
𝑞
Hom
	​

D
	​

(π
∗
	​

(C
⊗(p+1)
),D
C
p+1
	​

(X)
	​

)⊗Ω
C
p+1
	​

q
	​

, etc.

main

Bar–cobar quasi-isomorphism is claimed “proved here”: Corollary 5.2.24 “
Ω
c
h
(
𝐵
‾
c
h
(
𝐴
)
)
≃
𝐴
Ω
ch
	​

(
B
ch
	​

(A))≃A.”

(S5) Koszul dual coalgebra + Verdier duality.

Verdier dual comparison: Theorem 6.4.1 ([proved here]) claims
𝐵
‾
c
h
(
𝐴
)
≅
𝐷
(
𝐴
)
B
ch
	​

(A)≅D(A) (bar is Verdier dual).

Completion needed: Theorem 6.6.3 ([proved here]) asserts the completed bar is the right object when you take a full Koszul dual; completion is central throughout.

main

The manuscript itself recognizes a major circularity in defining
𝐴
!
A
!
 and proving
𝐵
(
𝐴
)
≃
𝐴
!
B(A)≃A
!
: “Problem 9.4.1 (Circularity in Koszul Duality)” and “Resolution: three-stage construction.”

The “correct general statement” is still tagged open: Corollary 9.4.9 ([open]).

(S6) “Full genus” and curvature corrections.

The introduction advertises a “full genus bar construction,” tagged open: Theorem 1.7.4 ([open]).

main

A key technical “strict nilpotence” claim is marked proved: Theorem 5.8.4 ([proved here]) asserts
𝑑
2
=
0
d
2
=0 “on the nose” for bar differentials in the presence of “central curvature,” with “verified through genus 5.”

(S7) E1-chiral layer.

“E1-Chiral Algebra” is deferred to Appendix G and explicitly depends on a still-open physical theorem: Definition G.6.13 refers to Theorem 32.3.2, and Theorem 32.3.2 is tagged [open].

main

The flagship E1 example “Yangian as E1-chiral” is explicitly open: Theorem 22.1.4 ([open]).

main

0.3 Done vs open matrix (major [open] items)

I will list “major” [open] items by centrality in the dependency spine above. For each I specify (i) dependencies, (ii) what a proof must deliver, (iii) what is missing in the manuscript as written, and (iv) a repair route.

(O1) Theorem 1.7.1 — Geometric bar construction [open] (PDF p. 46)

Location. Theorem 1.7.1 is tagged [open] and asserts the existence of a geometric bar complex
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) for a chiral algebra
𝐴
A with
𝑑
2
=
0
d
2
=0, whose differential is described “in terms of OPE coefficients and residue maps.”

Depends on: configuration spaces + residues (S1), Arnold/OS relations (S2), and the bar definition (S3).

What a proof must deliver: a precise functor
𝐴
↦
𝐵
‾
c
h
(
𝐴
)
A↦
B
ch
	​

(A) in an appropriate derived category, a well-defined differential, and a rigorous proof
𝑑
2
=
0
d
2
=0 that is independent of coordinate choices.

What is missing: Theorem 5.1.20 is a nine-term cancellation argument but relies on local identities; the global codimension-2 boundary control is only [open] (A.12.1).

Repair route: promote A.12.1 to a proved lemma and rewrite the
𝑑
2
=
0
d
2
=0 argument as “
∂
2
=
0
∂
2
=0” for the boundary operator in a normal-crossings stratification, with explicit orientation/sign bookkeeping.

(O2) Theorem 1.7.3 — Geometric cobar construction [open] (PDF p. 46)

Location. Theorem 1.7.3 is tagged [open] and claims a geometric cobar construction
Ω
c
h
(
𝐶
)
Ω
ch
	​

(C) for a chiral coalgebra
𝐶
C, recovering a chiral algebra.

main

Depends on: a rigorous Verdier dual/currents model (S4–S5).

What a proof must deliver: a definition of
Ω
c
h
(
𝐶
)
Ω
ch
	​

(C) internal to D-modules/sheaves (not analytic distributions), and a proof that it is left adjoint to
𝐵
‾
c
h
B
ch
	​

 and computes
𝐴
A under Koszul hypotheses.

What is missing: the actual cobar definition (5.2.6) is distributional/analytic and the manuscript itself flags distribution products failing naively (the “
3
𝛿
123
≠
0
3δ
123
	​


=0” note).

main

main

Repair route: define cobar as a Verdier-dual construction (sheaf-theoretic) rather than distributional, and only after that identify it with distributions by a theorem.

(O3) Theorem 1.7.4 — Full genus bar construction [open] (PDF p. 46)

Location. Theorem 1.7.4 is tagged [open] and asserts existence of “
𝐵
‾
c
h
(
𝑔
)
(
𝐴
)
B
ch
(g)
	​

(A)” for all genera
𝑔
g, with a differential including “quantum corrections,” again squaring to zero.

main

Depends on: compactifications and boundary/residue formalism for moduli of curves with marked points, plus an extension of the Arnold/OS mechanism to genus
𝑔
g.

What is missing: no complete geometric model of genus-
𝑔
g boundary strata and residue identities is provided at the needed level of detail; instead Theorem 5.8.4 claims “verified through genus 5,” which is not a proof.

Repair route: either (i) restrict to genus 0 and declare genus
>
0
>0 conjectural, or (ii) build the genus
𝑔
g complex via standard modular operads (gravity/hypercomm) and prove
𝑑
2
=
0
d
2
=0 by modular operad relations (a different engine than Arnold alone).

(O4) Corollary 9.4.9 — Correct general statement [open] (PDF p. 303)

Location. Corollary 9.4.9 is tagged [open] and is presented as “the correct general statement” after the manuscript’s three-stage attempt to resolve circularity in Koszul duality.

Depends on: the whole bar/cobar formalism + completion (S3–S5).

What a proof must deliver: a dependency-closed definition of
𝐴
!
A
!
 (coalgebra), proof it satisfies coalgebra axioms, and a construction of a quasi-isomorphism
𝐵
(
𝐴
)
≃
𝐴
!
B(A)≃A
!
 without circularity.

What is missing: the document admits “circularity” and proposes stages but does not actually close the loop rigorously in the generality claimed.

Repair route: specify a precise model category/∞-category, declare the correct completion (conilpotent/I-adic) as part of the definition, and reduce to Lurie-style Koszul duality for
𝐸
𝑛
E
n
	​

/factorization algebras by an explicit identification of your operad (NAP/Prism).

(O5) Theorem 32.3.2 — E1-chiral emergence [open] (PDF p. 774)

Location. Theorem 32.3.2 is tagged [open] and is the conceptual basis for the E1-chiral notion (“drop skew-symmetry, keep associativity”).

Depends on: a precise definition of “E1-chiral algebra” (Appendix G), plus compatibility with BD/factorization.

What a proof must deliver: an ∞-categorical definition and a theorem relating it to known braided/quantum VOA formalisms (or proving it’s genuinely new).

What is missing: Definition G.6.13 explicitly points back to this open theorem, creating definitional dependence.

main

Repair route: give an independent axiomatic definition (see §2 below) and then derive Theorem 32.3.2 as a motivational/construction theorem.

(O6) Theorem 22.1.4 — Yangian as E1-chiral algebra [open] (PDF p. 634)

Location. Theorem 22.1.4 is tagged [open] and states the Yangian gives an E1-chiral algebra, with failure of skew-symmetry controlled by an R-matrix/Yang–Baxter mechanism.

main

Depends on: a workable E1-chiral definition and a mechanism to build factorization operations from RTT/YBE.

What is missing: the factorization structure is asserted rather than constructed; the relation to your bar/cobar/Koszul duality is not yet made precise.

Repair route: replace “Yangian gives E1-chiral algebra” by “there is a braided factorization algebra on
𝐴
1
∖
{
∞
}
A
1
∖{∞} determined by RTT data,” and prove associativity/factorization from YBE as a main lemma.

(There are numerous additional [open] items in Introduction §§1.10–1.11 (e.g. deformation theory via chiral Hochschild), but they sit downstream of the above and should not be presented as main results until (O1)–(O4) are settled. )

1) Mathematical correctness audit (hard-nosed)

I separate the audit into (i) what is defined precisely, (ii) hidden hypotheses, and (iii) red flags with repairs.

1.1 Core constructions restated precisely (as the manuscript intends)
1.1.1 Factorization algebra input

The manuscript defines a factorization algebra as an assignment
𝑈
↦
𝐴
(
𝑈
)
U↦A(U) for disks
𝑈
⊂
𝑋
U⊂X, with structure maps for disjoint unions satisfying associativity and locality-type axioms (FA1–FA5) (Definition 3.10.5).

main

It claims a “chiral
⇒
⇒ factorization” theorem (Theorem 3.10.7, [proved here]).

main

Audit note. This theorem is not a harmless lemma: in BD, “chiral algebra” is a D-module object on Ran with factorization and a chiral bracket. A correct statement requires specifying the ambient category (derived category of D-mods? dg D-mods? ind-holonomic?), the Ran topology, and whether “factorization algebra” means the CG definition for cochain models or the BD definition for D-mods. As written, Theorem 3.10.7 is believable only if it is explicitly a rephrasing of BD’s equivalence of chiral/factorization structures (and then it should be a citation, not [proved here]).

1.1.2 Configuration-space residue engine

You build from the Fulton–MacPherson compactification
𝐶
𝑛
(
𝑋
)
C
n
	​

(X) (Theorem 4.1.4) and logarithmic forms
𝜔
log
⁡
ω
log
, together with residue maps along boundary divisors (Theorem 4.1.26).

But a basic local ingredient “
𝜔
ω has residue 1 along the boundary divisor” is only Lemma 4.1.25 and is tagged [open].

1.1.3 Geometric bar complex

For a (augmented) chiral algebra
𝐴
A, the reduced bar complex is defined as

𝐵
‾
c
h
(
𝐴
)
(
𝑈
)
  
=
  
⨁
𝑛
≥
0
Γ
 ⁣
(
𝐶
𝑛
+
1
(
𝑈
)
,
  
𝜋
∗
𝐴
⊠
(
𝑛
+
1
)
⊗
𝜔
𝐶
𝑛
+
1
(
𝑈
)
log
⁡
)
[
𝑛
]
,
B
ch
	​

(A)(U)=
n≥0
⨁
	​

Γ(C
n+1
	​

(U),π
∗
	​

A
⊠(n+1)
⊗ω
C
n+1
	​

(U)
log
	​

)[n],

where
𝜋
:
𝐶
𝑛
+
1
(
𝑈
)
→
𝑈
𝑛
+
1
π:C
n+1
	​

(U)→U
n+1
 is the projection and
𝜔
log
⁡
ω
log
 is the logarithmic canonical sheaf. (Definition 5.1.53).

main

The differential decomposes as

𝑑
=
𝑑
i
n
t
+
𝑑
d
R
+
𝑑
r
e
s
,
d=d
int
	​

+d
dR
	​

+d
res
	​

,

where
𝑑
i
n
t
d
int
	​

 comes from
𝐴
A’s internal differential,
𝑑
d
R
d
dR
	​

 from the de Rham differential on forms, and
𝑑
r
e
s
d
res
	​

 from summing residues along boundary strata (Definition 5.1.55).

main

Nilpotence is asserted in Theorem 5.1.20 ([proved here]) as a “nine-term cancellation.”

Finally,
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) is asserted to be a chiral coalgebra (Theorem 5.1.69, [proved here]).

1.1.4 Geometric cobar complex

For a chiral coalgebra
𝐶
C, the cobar complex is defined using distributional sections and D-module Homs: Definition 5.2.6 defines
Ω
c
h
𝑝
,
𝑞
(
𝐶
)
Ω
ch
p,q
	​

(C) as distributional sections of a sheaf

H
o
m
‾
𝐷
 ⁣
(
𝜋
∗
(
𝐶
⊗
(
𝑝
+
1
)
)
,
𝐷
𝐶
𝑝
+
1
(
𝑋
)
)
⊗
Ω
𝐶
𝑝
+
1
𝑞
,
Hom
	​

D
	​

(π
∗
	​

(C
⊗(p+1)
),D
C
p+1
	​

(X)
	​

)⊗Ω
C
p+1
	​

q
	​

,

with a cobar differential built from collision distributions (Dirac deltas) and the coalgebra structure.

main

Bar–cobar equivalence is asserted in Corollary 5.2.24 as
Ω
c
h
(
𝐵
‾
c
h
(
𝐴
)
)
≃
𝐴
Ω
ch
	​

(
B
ch
	​

(A))≃A (tagged [proved here]).

1.1.5 Verdier duality and completion

Theorem 6.4.1 ([proved here]) claims
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) identifies with a Verdier dual
𝐷
(
𝐴
)
D(A).

Theorem 6.6.3 ([proved here]) introduces/justifies completion as the correct Koszul dual object.

main

The manuscript explicitly diagnoses circularity in Koszul duality and proposes a three-stage resolution, but ends with an “open” correct general statement (Corollary 9.4.9).

1.1.6 E1-chiral algebra definition

You define E1-chiral algebra in Appendix G, but the definition explicitly depends on an open theorem: Definition G.6.13 points to Theorem 32.3.2 ([open]).

main

In applications you propose Yangians as E1-chiral, with skew-symmetry failure controlled by an R-matrix: Theorem 22.1.4 ([open]) and Construction 22.1.3.

main

main

1.2 Hidden hypotheses and missing foundational choices

The manuscript repeatedly uses constructions that are only valid under specific finiteness/completeness hypotheses, but these hypotheses are not globally fixed early. The minimal set that must be declared (and then checked in all core theorems) is:

Ambient category: Are you working in
𝐷
(
𝐷
−
m
o
d
(
𝑋
)
)
D(D−mod(X)),
𝐷
h
o
l
𝑏
D
hol
b
	​

, Ind-holonomic D-mods, or dg D-mods? This affects (i) existence of
𝑗
!
,
𝑗
∗
j
!
	​

,j
∗
	​

, (ii) Verdier duality, and (iii) pushforward
𝜋
∗
π
∗
	​

.

Holonomicity/constructibility: the use of Verdier duality and “delta distributions” strongly suggests holonomic D-mods. But the bar construction uses
𝜔
log
⁡
ω
log
 on configuration compactifications—these are typically not holonomic unless carefully defined as perverse extensions.

Convergence / completion: Theorem 6.6.3 is about completion, and Problem 9.4.1 diagnoses circularity. You must decide: is the Koszul dual coalgebra defined as a completed cofree coalgebra by default? If not, the cobar/bar equivalence will generally fail.

Augmentation/units: The bar complex is written in “reduced” form
𝐵
‾
B
, but the conditions on units/augmentations are not uniformly stated. (E.g. in Definition 5.1.53 you sum over
𝑛
≥
0
n≥0 and shift by
[
𝑛
]
[n]; this is only canonical if augmentations exist and the
𝑛
=
0
n=0 term is treated correctly.)

main

Sign conventions: You have a dedicated sign-consistency lemma/table (e.g. Lemma 13.9.31; Appendix C.12 “master comparison table”), but the main
𝑑
2
=
0
d
2
=0 argument uses geometric boundary signs and Koszul signs simultaneously; any mismatch destroys correctness.

Coordinate-independence: the residue differential is defined using logarithmic forms and local collision coordinates. If you do not prove invariance under change of coordinates (e.g.
𝑧
↦
𝜙
(
𝑧
)
z↦ϕ(z)), the construction is not intrinsic as a chiral object.

1.3 Red flags (≥10) with repairs

I now list concrete “red flags”: statements or constructions that are too strong, ambiguous, or likely false as written. For each: (i) location, (ii) risk, (iii) minimal correct replacement, (iv) fix plan.

Red flag 1: E1-chiral definition is circular (depends on an open theorem)

Location: Definition G.6.13 points back to Theorem 32.3.2 ([open]).

main

Risk: A definition depending on an open theorem is not acceptable. It prevents any downstream theorem from being checkable.

Minimal replacement (Proposed):
Definition (Proposed). An E1-chiral algebra on a curve
𝑋
X is a factorization algebra
𝐴
A in a monoidal ∞-category
𝐶
C equipped with a braiding/half-braiding along point-collisions so that the factorization product is associative but not required to be symmetric; equivalently, a locally defined “OPE”
𝑚
𝑧
,
𝑤
m
z,w
	​

 satisfying associativity and a controlled commutativity constraint governed by an
𝑅
R-matrix satisfying YBE.
(This is an attempt to formalize the intention of Theorem 22.1.4/Construction 22.1.3.)

Fix plan: Add an “Axioms of E1-chiral algebra” section before any applications: specify disks, disjoint unions, collision maps, associativity, unit, and the braiding datum. Then relegate Theorem 32.3.2 to a motivation theorem (“physics suggests these axioms”).

Red flag 2: Geometric cobar is built from “distributions” without a D-module theorem

Location: Definition 5.2.6 uses distributional sections and
𝐷
D-module Homs, and the text elsewhere flags delta products not behaving naively (the “
3
𝛿
123
≠
0
3δ
123
	​


=0” comment).

main

main

Risk: This is analytically ill-posed: delta-products depend on renormalization/regularization. Without a sheaf-theoretic replacement, the differential and its nilpotence are not intrinsic and may be false.

Minimal replacement (Proposed):
Replace distributional cobar by Verdier-dual cobar: define
Ω
c
h
(
𝐶
)
:
=
𝐷
(
𝐵
‾
c
h
(
𝐷
𝐶
)
)
Ω
ch
	​

(C):=D(
B
ch
	​

(DC)) (or an equivalent internal construction) in the holonomic D-module category.

Fix plan: Prove a theorem identifying the Verdier dual of log-forms with a complex of currents (distributions) as a corollary, not as the definition.

Red flag 3: Bar–cobar quasi-isomorphism stated too broadly / lacks hypotheses

Location: Corollary 5.2.24: “
Ω
c
h
(
𝐵
‾
c
h
(
𝐴
)
)
≃
𝐴
Ω
ch
	​

(
B
ch
	​

(A))≃A” ([proved here]).

Risk: Bar–cobar equivalence is false for general associative/chiral algebras without conilpotence/Koszul hypotheses or completion. Your own Theorem 6.6.3 emphasizes completion; the corollary is missing its dependence on those hypotheses.

Minimal replacement (Proposed):
Corollary (Proposed). If
𝐴
A is (i) augmented, (ii) “chiral-Koszul” (precise definition needed), and (iii) complete with respect to the augmentation ideal filtration so that
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) is conilpotent, then
Ω
c
h
(
𝐵
‾
c
h
(
𝐴
)
)
→
𝐴
Ω
ch
	​

(
B
ch
	​

(A))→A is a quasi-isomorphism.

Fix plan: Make the completion explicit and prove convergence of the standard bar–cobar spectral sequence.

Red flag 4: Theorem 6.4.1 “bar = Verdier dual” is far too strong as written

Location: Theorem 6.4.1 ([proved here])
𝐵
‾
c
h
(
𝐴
)
≅
𝐷
(
𝐴
)
B
ch
	​

(A)≅D(A).

Risk: Verdier duality is a functor on sheaves/D-modules, while
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) is a large configuration-space complex with residues. An isomorphism requires specifying (a) which sheaf on which space is being dualized, and (b) compatibility with Ran/factorization. As written, it reads like a slogan.

Minimal replacement (Proposed):
Theorem (Proposed). There is a natural equivalence between
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) and a model for the Verdier dual of the Ran-space factorization object associated to
𝐴
A, under holonomicity/properness assumptions on the relevant compactifications.

Fix plan: Rewrite with explicit spaces/functors:
𝐴
A is a D-module on Ran,
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) is a D-module (or complex) on Ran; then prove
𝐵
‾
c
h
(
𝐴
)
≃
𝐷
R
a
n
(
𝐴
)
B
ch
	​

(A)≃D
Ran
	​

(A) by reducing to duality on each
𝐶
𝑛
(
𝑋
)
C
n
	​

(X) and checking factorization compatibilities.

Red flag 5: Lemma 4.1.25 [open] is foundational and cannot remain open

Location: Lemma 4.1.25 ([open]) “basic logarithmic form on
𝐶
2
(
𝑋
)
C
2
	​

(X) with residue 1.”

Risk: This lemma is used implicitly in constructing and normalizing residues (Theorem 4.1.26). Leaving it open undermines the residue engine.

Minimal replacement: either prove it or cite a standard construction in log geometry / FM compactification literature.

Fix plan: Add a two-page local coordinate proof: in a normal crossing chart near the boundary divisor, write
𝑑
𝑡
𝑡
t
dt
	​

 and compute residue; check independence.

Red flag 6: The global “OS relations” engine is tagged open (A.12.1)

Location: Theorem A.12.1 ([open]) “Configuration space boundary relations.”

Risk: This is the correct level where
𝑑
r
e
s
2
=
0
d
res
2
	​

=0 should be proved. If it remains open, the nilpotence proof in Theorem 5.1.20 is not globally justified.

Minimal replacement: Move the global nilpotence proof into Appendix A, prove A.12.1, then cite it in §5.1.

Fix plan: Provide the codimension-2 boundary stratification of
𝐶
𝑛
(
𝑋
)
C
n
	​

(X) and show each codim-2 stratum appears with total signed coefficient 0, giving
𝑑
r
e
s
2
=
0
d
res
2
	​

=0.

Red flag 7: “Strict nilpotence for all chiral algebras with central curvature” is not credible as proved

Location: Theorem 5.8.4 ([proved here]) claims
𝑑
2
=
0
d
2
=0 “on the nose,” with “verified through genus 5.”

Risk: A finite-genus check is not a proof. Moreover, the claim “for all chiral algebras with central curvature” is extremely broad and would require a general theorem about all higher boundary strata and all higher correction terms.

Minimal replacement (Proposed):
Theorem (Proposed, weaker). For the genus-0 bar complex
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A), one has
𝑑
2
=
0
d
2
=0. For the “full genus” corrected differential
𝑑
f
u
l
l
d
full
	​

,
𝑑
f
u
l
l
2
d
full
2
	​

 is controlled by explicit boundary strata contributions; if curvature is central, the obstruction class lands in the center and vanishes in the associated graded/completed setting.

Fix plan: Make genus
>
0
>0 a conjecture unless you supply a modular-operad proof.

Red flag 8: Contradictory free-fermion OPE statements

Location A: Example 13.9.16 says free fermion OPE
𝜓
(
𝑧
)
𝜓
(
𝑤
)
∼
1
𝑧
−
𝑤
ψ(z)ψ(w)∼
z−w
1
	​

 and identifies this with a bar differential on configuration space.

Location B: Proposition 17.3.2 states
𝜓
(
𝑧
)
𝜓
(
𝑤
)
=
0
ψ(z)ψ(w)=0 (no pole).

Risk: This is an outright contradiction unless
𝜓
ψ denotes different fields/objects in the two places. It undermines reliability of later computations.

Minimal replacement: Clarify notation: either (i) Proposition 17.3.2 is about the super-commutator or regular part, not the full OPE, or (ii) it is a different algebra (e.g. an exterior algebra toy model, not the free-fermion VOA).

Fix plan: Add a “Notation audit” table at the start of Part II and fix the statement to match the OPE used in Example 13.9.16.

Red flag 9: Theorem 3.10.7 “chiral ⇒ factorization” is marked [proved here] but should be a citation + precise scope

Location: Theorem 3.10.7 ([proved here]).

main

Risk: As written it is not clear whether it is (a) a restatement of BD’s theorem in the D-module setting, or (b) a claim in a different category. “Proved here” with a short sketch is not enough for Annals.

Minimal replacement: State it as: “By BD (precise theorem and section), chiral algebras on a curve are equivalent to factorization algebras of D-modules on Ran.” Then only prove the translation of notation.

Fix plan: Provide exact BD reference and a dictionary of conventions; move any new content to lemmas about compatibility with your
𝜔
log
⁡
ω
log
-bar complex.

Red flag 10: Prism Principle / “Prism as Koszul dual” is open but used as conceptual justification

Location: Remark 5.2.1 “Prism as Koszul dual” is explicitly tagged [open].

main

Risk: You use it as conceptual spine for duality, but it is not proved. Without it, the operadic claims (NAP/Koszul duality) lack their geometric anchor.

Minimal replacement: Recast as conjecture with a precise operadic statement: identify which operad/cooperad (“Prism”) and which Koszul duality (Loday–Vallette) is meant.

Fix plan: Either prove the operadic identification directly, or remove the “Prism” branding until it is established.

Red flag 11: Circularity resolution is incomplete (and admitted)

Location: Problem 9.4.1 and the three-stage plan; Corollary 9.4.9 remains [open].

Risk: This is the core of “chiral Koszul duality.” If it’s open, you cannot present downstream identifications of
𝐴
!
A
!
 with known algebras as theorems.

Minimal replacement: Promote only the stage-1 construction as proved, and mark stages 2–3 as conjectural.

Fix plan: Adopt a standard Koszul duality framework (e.g. Lurie’s
𝐸
𝑛
E
n
	​

-Koszul duality) and prove that your categories satisfy its hypotheses.

Red flag 12: Yangian “self-duality” and other large identifications are labeled [proved here] but are not backed by a completed formalism

Location: Example/summary claims include “Yangian self-duality” (e.g. Theorem 9.3.6, [proved here] appears in the manuscript’s self-summary).

main

Risk: A “Yangian is Koszul self-dual” statement is very strong and sensitive to presentations, completions, and grading conventions. Without a fully closed (O4) duality theorem, such identifications are premature.

Minimal replacement: Recast as a prediction: “If the chiral Koszul duality formalism holds and if the Yangian admits a suitable quadratic Koszul presentation, then it should be (completed) Koszul self-dual.”

Fix plan: Provide a complete quadratic presentation and check Koszulity (PBW + distributivity) or cite the exact known result if it exists (I do not see a precise citation in the manuscript sections retrieved).

2) Proof-gap closure blueprint (engineering mode)

I choose five [open] items of highest centrality and give proof plans with lemma breakdowns. Everything below is Proposed / Needs verification unless the lemma is already proved in your manuscript and cited.

2.1 Close (O1): Theorem 1.7.1 (Geometric bar construction) [open]

Goal. Define
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) intrinsically and prove
𝑑
2
=
0
d
2
=0.

Proposed lemma breakdown.

Lemma 2.1.1 (Functoriality of
𝐵
‾
c
h
B
ch
	​

).
Given a morphism of chiral algebras
𝑓
:
𝐴
→
𝐴
′
f:A→A
′
, the induced maps
𝜋
∗
𝐴
⊠
(
𝑛
+
1
)
→
𝜋
∗
𝐴
′
⊠
(
𝑛
+
1
)
π
∗
	​

A
⊠(n+1)
→π
∗
	​

A
′
⊠(n+1)
 yield a chain map
𝐵
‾
c
h
(
𝐴
)
→
𝐵
‾
c
h
(
𝐴
′
)
B
ch
	​

(A)→
B
ch
	​

(A
′
).

What to check: compatibility with the residue differential and with factorization restriction maps.

Where it’s used: Main Theorem 1.8.1 claims functoriality (citing Corollary 5.1.22).

Lemma 2.1.2 (Residue maps are well-defined in the derived D-module category).
Upgrade Lemma 4.1.25 ([open]) + Theorem 4.1.26 ([proved here]) into a derived statement: residues are morphisms of complexes compatible with de Rham differential.

Lemma 2.1.3 (Boundary orientation/sign convention).
Fix a convention identifying
𝑑
r
e
s
d
res
	​

 with the boundary operator on a normal crossings divisor stratification of
𝐶
𝑛
+
1
(
𝑈
)
C
n+1
	​

(U). This must interface with Koszul signs from tensor permutations (compare Lemma 13.9.31).

Hard lemma 2.1.4 (Global
𝑑
r
e
s
2
=
0
d
res
2
	​

=0 via codimension-2 boundary).
Prove that the sum over codimension-2 strata of iterated residues cancels, yielding
𝑑
r
e
s
2
=
0
d
res
2
	​

=0, and then check cross-terms with
𝑑
d
R
d
dR
	​

 and
𝑑
i
n
t
d
int
	​

.

Key input: Theorem A.12.1 ([open]) must be proved and used here.

Sketch: In a normal crossings compactification,
𝑑
r
e
s
d
res
	​

 is the “Poincaré residue boundary” operator. Then
𝑑
r
e
s
2
=
0
d
res
2
	​

=0 is
∂
2
=
0
∂
2
=0 for the boundary complex. The only nontrivial part is verifying that local codim-2 charts match the expected OS relation (Arnold relation in genus 0) with correct signs.

Deliverable: rewrite Theorem 5.1.20 as a corollary of Lemma 2.1.4, rather than a nine-term ad hoc cancellation.

2.2 Close (O2): Theorem 1.7.3 (Geometric cobar) [open]

Goal. Replace distributional cobar by intrinsic Verdier-dual cobar; prove it is adjoint to bar and recovers
𝐴
A under Koszul hypotheses.

Proposed lemma breakdown.

Lemma 2.2.1 (Verdier dual of log-forms is a canonical “current” complex).
Formulate and prove a theorem identifying
𝐷
(
𝜔
𝐶
𝑛
+
1
log
⁡
)
D(ω
C
n+1
	​

log
	​

) with a complex of currents supported on boundary strata. This should explain the appearance of delta distributions.

Motivation: your text explicitly acknowledges delta products are subtle (the “
3
𝛿
123
≠
0
3δ
123
	​


=0” note).

main

Lemma 2.2.2 (Define
Ω
c
h
(
𝐶
)
Ω
ch
	​

(C) as a Verdier dual of bar).
Define
Ω
c
h
(
𝐶
)
Ω
ch
	​

(C) by a universal property (adjunction) in the D-module category. Only after that show it admits the distributional model of Definition 5.2.6.

main

Hard lemma 2.2.3 (Bar–cobar equivalence under completion/Koszulity).
Prove
Ω
c
h
(
𝐵
‾
c
h
(
𝐴
)
)
→
𝐴
Ω
ch
	​

(
B
ch
	​

(A))→A is a quasi-isomorphism assuming (i) conilpotence and (ii) completeness.

Why hard: the naive proof fails in nonconilpotent settings; you already introduce completion as necessary (Theorem 6.6.3).

main

Approach: filtered spectral sequence from the coradical/augmentation filtration; show
𝐸
1
E
1
	​

 is the classical bar–cobar and converges.

2.3 Close (O4): Corollary 9.4.9 [open] (circularity-free Koszul duality)

Goal. Define
𝐴
!
A
!
 without circularity and prove
𝐵
(
𝐴
)
≃
𝐴
!
B(A)≃A
!
.

Proposed lemma breakdown (aligned with your “three-stage” plan).

Stage 1 (intrinsic candidate).
Define
𝐴
≤
2
!
A
≤2
!
	​

 from the quadratic data
(
𝐴
1
,
𝐴
2
,
𝜇
)
(A
1
	​

,A
2
	​

,μ) (your approach in §9.4).

Stage 2 (coalgebra axioms).
Prove the induced comultiplications satisfy coassociativity/counit, using only associativity of OPE and residue boundary identities.

Stage 3 (comparison map).
Construct a map
𝐵
‾
c
h
(
𝐴
)
→
𝐴
!
B
ch
	​

(A)→A
!
 and show it is a quasi-isomorphism by filtration/spectral sequence.

Hard lemma 2.3.1 (noncircular comparison).
Show that the coalgebra axioms and differential squaring to zero can be checked purely at the level of configuration space boundary strata, without invoking bar–cobar duality.

Input needed: a proved version of A.12.1 and an explicit dictionary between “OPE associativity” and boundary-residue identities.

Engineering deliverable: Your manuscript should contain a single dependency-closed diagram:

(Chiral algebra data)
⇒
(Residue operators)
⇒
𝑑
2
=
0
⇒
(Coalgebra)
⇒
(Comparison map)
.
(Chiral algebra data)⇒(Residue operators)⇒d
2
=0⇒(Coalgebra)⇒(Comparison map).

At present, the manuscript itself labels the general end statement open.

2.4 Close (O5): Theorem 32.3.2 [open] (E1-chiral definition/recognition)

Goal. Make “E1-chiral” mathematically precise and independent of physics; relate it to known frameworks.

Proposed lemma breakdown.

Lemma 2.4.1 (Axioms for braided factorization algebra on a curve).
Define a factorization algebra
𝐴
A on
𝑋
X together with a braiding isomorphism along transposition of points in configuration space, satisfying a hexagon/YBE compatibility. This is the correct categorical surrogate for “drop skew-symmetry.”

Lemma 2.4.2 (BD chiral algebras embed as symmetric E1-chiral algebras).
Show that if the braiding is symmetric, you recover BD chiral (i.e. usual locality/skew-symmetry).

Hard lemma 2.4.3 (Equivalence to a known quantum vertex algebra formalism).
Either prove an equivalence with a known notion (e.g. “quantum vertex algebra” of Etingof–Kazhdan type, if that is indeed the intended relation), or explicitly prove that your axioms do not reduce to existing ones.

Deliverable: Rewrite Definition G.6.13 so it does not depend on Theorem 32.3.2.

main

2.5 Close (O6): Theorem 22.1.4 [open] (Yangian as E1-chiral)

Goal. Construct the factorization operations and verify associativity from YBE.

Proposed lemma breakdown.

Lemma 2.5.1 (Local RTT/OPE data).
You propose a skew-symmetry failure controlled by an
𝑅
R-matrix:

𝐽
𝑎
(
𝑧
)
𝐽
𝑏
(
𝑤
)
−
𝑅
𝑎
𝑏
𝑐
𝑑
(
𝑧
−
𝑤
)
 
𝐽
𝑑
(
𝑤
)
𝐽
𝑐
(
𝑧
)
=
0
,
J
a
(z)J
b
(w)−R
ab
cd
	​

(z−w)J
d
(w)J
c
(z)=0,

and claim YBE guarantees associativity. This is stated at the level of Theorem 22.1.4.

main

Lemma 2.5.2 (From RTT to factorization structure).
Define structure maps
𝐴
(
𝑈
1
)
⊗
𝐴
(
𝑈
2
)
→
𝐴
(
𝑈
1
∪
𝑈
2
)
A(U
1
	​

)⊗A(U
2
	​

)→A(U
1
	​

∪U
2
	​

) for disjoint disks, and specify how they degenerate as disks collide.

Hard lemma 2.5.3 (Factorization associativity).
Prove that the compatibility for triple disjoint unions equals the Yang–Baxter equation. Concretely, show that the two ways of multiplying three currents correspond to the two sides of YBE for the braiding operator
𝑅
R.

Deliverable: Provide a complete proof in the simplest case (e.g.
𝑠
𝑙
2
sl
2
	​

) as the first nontrivial test, before stating general
𝑔
g.

3) Novelty audit (Annals bar)

I separate: (i) what is plausibly new in your manuscript, (ii) what looks like repackaging of known frameworks, and (iii) candidate Annals-grade results you could credibly aim for after repairs.

3.1 Novelty claim ledger (responsible version)
Candidate novelty A: “Residue/configuration-space bar complex” as a concrete computational model

What is claimed in the manuscript: a geometric bar complex
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) with explicit residue differential, and a claim it computes the Koszul dual coalgebra and (via cobar) recovers
𝐴
A.

main

What is plausibly new: the explicit “residue differential in terms of OPE data” and its packaging into a chiral coalgebra structure (Theorem 5.1.69).

Referee attack point: the global
𝑑
2
=
0
d
2
=0 mechanism (A.12.1 open), plus the cobar/distributional formalism.

Candidate novelty B: “Prism principle” as the operadic Koszul dual governing bar/cobar

What is claimed: “Prism as Koszul dual” (Remark 5.2.1, [open]).

main

What is plausibly new: if you can precisely identify the operad/cooperad controlling the residue gluing and show it is Koszul dual to NAP (or another known operad), that would be a genuinely new conceptual insight.

Referee attack point: it is explicitly [open]; must be either proved or removed.

Candidate novelty C: E1-chiral algebras as “drop skew-symmetry” and unify quantum groups + vertex ideas

What is claimed: Theorem 32.3.2 [open], Definition G.6.13 referencing it, and the Yangian application (Theorem 22.1.4 [open]).

main

main

What is plausibly new: only if you give a new factorization/D-module realization of “quantum vertex algebra / braided VOA” ideas, with a robust module theory and link to your bar/cobar duality.

Referee attack point: definitional circularity + overlap with existing “quantum vertex algebra” literature (needs a precise comparison, or a clear statement of difference).

3.2 Three candidate Annals-grade results (Proposed)

These are Proposed (not yet proved in your manuscript); I state them in a way that could become defensible after repairs.

Theorem (Proposed A): Intrinsic geometric bar complex computes factorization homology for augmented chiral algebras

Hypotheses.
𝐴
A is an augmented BD chiral algebra on a smooth complex curve
𝑋
X, valued in holonomic D-modules, satisfying a finiteness condition ensuring all configuration-space pushforwards used in Definition 5.1.53 are defined and compatible with Verdier duality.

main

Conclusion. The geometric bar complex
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) (Definition 5.1.53) is a functorial model for the reduced factorization homology
∫
𝑋
𝐴
∫
X
	​

A (or its Koszul dual coalgebra object), and its differential
𝑑
=
𝑑
i
n
t
+
𝑑
d
R
+
𝑑
r
e
s
d=d
int
	​

+d
dR
	​

+d
res
	​

 squares to zero intrinsically.

Proof strategy.

Prove a global residue boundary identity (upgrade A.12.1 from [open] to proved).

Identify
𝑑
r
e
s
d
res
	​

 with the boundary operator in a “log de Rham” model on
𝐶
𝑛
+
1
(
𝑋
)
C
n+1
	​

(X).

Apply a factorization-homology comparison theorem (your Theorem 4.1.35 is the natural anchor) to identify this configuration-space model with
∫
𝑋
𝐴
∫
X
	​

A.

main

Comparison. This would strengthen the manuscript’s current “
𝑑
2
=
0
d
2
=0 by nine-term cancellation” (Theorem 5.1.20) into an intrinsic global boundary proof.

Theorem (Proposed B): Chiral Koszul duality for conilpotent/completed chiral algebras

Hypotheses.
𝐴
A is augmented and complete w.r.t. the augmentation ideal, and the reduced bar coalgebra
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) is conilpotent; define
𝐴
!
A
!
 as the completed chiral coalgebra extracted from
𝐵
‾
c
h
(
𝐴
)
B
ch
	​

(A) (align with Theorem 6.6.3).

main

Conclusion. There is an equivalence
Ω
c
h
(
𝐵
‾
c
h
(
𝐴
)
)
≃
𝐴
Ω
ch
	​

(
B
ch
	​

(A))≃A, and the bar–cobar adjunction restricts to an equivalence between suitable Koszul subcategories.

Proof strategy.

Replace distributional cobar by a Verdier-dual cobar (repair §1.3, Red flag 2).

Prove convergence of the coradical filtration spectral sequence (requires explicit completeness hypotheses).

Use the three-stage anti-circular construction (Problem 9.4.1) but complete Stage 2–3 rigorously, thereby closing Corollary 9.4.9.

Comparison. This is the mathematical version of what Corollary 5.2.24 currently asserts without sufficient hypotheses.

Theorem (Proposed C): Braided factorization algebras from RTT data (Yangian case)

Hypotheses. Fix a rational R-matrix
𝑅
(
𝑧
)
R(z) satisfying Yang–Baxter and unitarity; assume the RTT relations define an algebra of currents
𝐽
𝑎
(
𝑧
)
J
a
(z) with the braided locality relation stated in Theorem 22.1.4.

main

Conclusion. There exists a braided factorization algebra
𝑌
Y on
𝐴
1
A
1
 (an “E1-chiral algebra”) whose local sections reproduce the Yangian algebra, and whose associativity/factorization axioms are equivalent to YBE for
𝑅
R.

Proof strategy.

Build
𝑌
(
𝑈
)
Y(U) for disks by generators/relations and define factorization maps via “ordered product” + braiding.

Prove the factorization associativity diagram for triple unions equals YBE.

Show that when
𝑅
R is trivial/symmetric you recover the BD chiral structure (compatibility check with Theorem 3.10.7).

main

Comparison. Theorem 22.1.4 is currently tagged [open] and presented as a statement. This would turn it into a genuine construction theorem.

main

4) Representation theory program (primary E1 examples; deep, explicit)

Everything in this section is a program: it is Proposed / Needs verification unless explicitly cited as already defined/claimed in main.pdf. The manuscript itself marks the core E1 statements as [open], so the program must be built around repairing the definition first.

main

4.0 A workable definition of “module” for E1-chiral algebras (Proposed)

To make module theory checkable, you need a notion that interacts with factorization:

Definition (Proposed). Let
𝐴
A be an E1-chiral (braided factorization) algebra on a curve
𝑋
X. An E1-chiral module supported at a point
𝑥
∈
𝑋
x∈X is a factorization module
𝑀
M on the pointed Ran space
R
a
n
(
𝑋
;
𝑥
)
Ran(X;x) such that:

On disjoint disks away from
𝑥
x,
𝑀
M factorizes as
𝐴
⊗
𝑛
⊗
𝑀
A
⊗n
⊗M.

As disks collide with the marked point, the action is governed by the same braiding/OPE data as
𝐴
A.

Verification route.

Implement this first for locally constant factorization algebras (where it reduces to ordinary modules over an
𝐸
1
E
1
	​

-algebra).

Then extend to the “non-locally constant” chiral case by local-to-global gluing along configuration spaces.

This aligns conceptually with your factorization-algebra framework (Definition 3.10.5).

main

4.1 Yangian / shifted Yangian / affine Yangian / Coulomb branch algebras / CoHA
A) Definition of E1-chiral structure (from manuscript + proposed repairs)

The manuscript’s Yangian E1-chiral claim is:

Construction 22.1.3 gives “Yangian currents and OPE data” in the E1-chiral direction.

main

Theorem 22.1.4 ([open]) asserts skew-symmetry failure is controlled by an R-matrix relation
𝐽
𝑎
(
𝑧
)
𝐽
𝑏
(
𝑤
)
−
𝑅
𝑎
𝑏
𝑐
𝑑
(
𝑧
−
𝑤
)
𝐽
𝑑
(
𝑤
)
𝐽
𝑐
(
𝑧
)
=
0
J
a
(z)J
b
(w)−R
ab
cd
	​

(z−w)J
d
(w)J
c
(z)=0, and associativity is ensured by Yang–Baxter.

main

Audit-based repair (Proposed).
Define the E1-chiral Yangian
𝑌
ℏ
(
𝑔
)
Y
ℏ
	​

(g) as a braided factorization algebra on
𝐴
1
A
1
 whose 2-point collision law is given by RTT/OPE with R-matrix, and whose 3-point coherence is YBE. This is exactly what your Theorem 22.1.4 intends but does not yet construct.

B) Module theory program (Proposed; verify against Yangian literature)

Once the braided factorization algebra exists, module theory should recover known families:

Evaluation modules (finite-dimensional): modules obtained by pulling back along
𝑧
↦
𝑧
−
𝑎
z↦z−a and using an underlying
𝑔
g-module.

Checkable goal: show the factorization-module axiom reduces to RTT evaluation representation.

Highest-weight modules (Drinfeld polynomials): define “highest weight” in E1-chiral language as a module
𝑀
M with a cyclic vector annihilated by positive-current modes and with specified eigenvalues for Cartan-current generating series.

Checkable goal: reproduce the classification by Drinfeld polynomials (external standard result; needs precise citation and adaptation).

Tensor/fusion: the factorization tensor product on the Ran space should produce a monoidal structure on modules; the braiding should give an
𝑅
R-matrix braided tensor category.

Concrete computational target (toy Yangian check).
Take
𝑠
𝑙
2
sl
2
	​

. Implement:

the RTT algebra with
𝑅
(
𝑢
)
=
1
−
ℏ
𝑃
/
𝑢
R(u)=1−ℏP/u (external),

show the module supported at a point reproduces the usual
2
2-dim evaluation module, and

compute the braiding on
𝑉
(
𝑎
)
⊗
𝑉
(
𝑏
)
V(a)⊗V(b) from factorization.

This is not proved in the manuscript (it is precisely what Theorem 22.1.4 should become).

main

C) Duality action (Proposed)

Your manuscript aims to apply “chiral Koszul duality” to examples like Yangians (and even claims “Yangian self-duality” in its summary notes).

main

Proposed prediction (needs verification).
If the Yangian E1-chiral algebra is Koszul (in your completed sense), then Koszul duality should induce a derived equivalence between:

a derived category of
𝑌
Y-modules (factorization modules) and

a derived category of comodules over
𝑌
!
Y
!
 (the Koszul dual coalgebra).

Check in toy case: do this for the locally constant “RTT truncation” (see toy model below) where Koszul duality reduces to ordinary algebraic Koszul duality.

4.2
𝑞
q-Heisenberg,
𝑞
q-Virasoro, quantum
𝑊
W-algebras

main.pdf contains extensive discussion of Heisenberg/Virasoro/
𝑊
W-algebras in Part II (Ch.17–20) but the E1-chiral
𝑞
q-deformed versions are not (in the chunks retrieved) given as complete constructions with proofs. The correct program is:

A) Definition of E1-chiral structure (Proposed)

Model
𝑞
q-Heisenberg currents
𝑎
(
𝑧
)
a(z) with a
𝑞
q-difference OPE (or braided commutator) encoded by a trigonometric R-matrix.

Impose braided locality:

𝑎
(
𝑧
)
𝑎
(
𝑤
)
=
𝜑
(
𝑧
/
𝑤
)
 
𝑎
(
𝑤
)
𝑎
(
𝑧
)
+
(singular/central terms)
,
a(z)a(w)=φ(z/w)a(w)a(z)+(singular/central terms),

where
𝜑
φ satisfies a multiplicative cocycle condition ensuring associativity (a
𝑞
q-YBE type identity).

B) Module theory: explicit families (Proposed)

Fock modules: generated by a vacuum vector with annihilation conditions for positive modes; compute graded character (often
∏
𝑛
≥
1
(
1
−
𝑞
𝑛
)
−
1
∏
n≥1
	​

(1−q
n
)
−1
-type) depending on conventions.

Screening-operator constructions: modules built by BRST-type complexes; compatibility with factorization should manifest as higher residue conditions.

C) Duality action (Proposed)

Koszul duality should relate
𝑞
q-Heisenberg to a “
𝑞
q-commutative coalgebra” (quantum exterior) and potentially connect
𝑞
q-Virasoro/
𝑞
q-
𝑊
W to dual-level
𝑊
W-algebras (your manuscript suggests many Langlands-style dualities in Part III summary, but these are not yet dependency-closed).

main

4.3 Toroidal and elliptic algebras (genus 1 structure)

Your manuscript advertises “full genus” bar constructions (Theorem 1.7.4 [open]) and higher-genus corrections (Theorem 5.8.4 claims strict nilpotence, but with only partial verification).

main

Program consequence: elliptic/toroidal examples are blocked until the genus-1 bar/cobar is made rigorous.

A) Definition of E1-chiral structure (Proposed)

Replace rational/trigonometric R-matrices by elliptic R-matrices with theta-function dependence.

Define collision rules using elliptic functions; associativity should follow from the elliptic Yang–Baxter equation.

B) Module theory (Proposed)

Fock-like modules graded by energy/charge.

Evaluation modules along elliptic curve points, with monodromy data around cycles.

C) Duality action (Proposed)

Koszul duality should interact with modularity (S-transform) if your genus-1 construction is compatible with mapping class group action. This is a major new direction but must be postponed until (O3) is proved.

4.4 R-twisted / Yang–Baxter vertex algebras and lattice cocycle examples

Your own manuscript summary explicitly highlights “lattice algebras with non-symmetric cocycles” as first strictly E1 examples (this appears in the summary material in Part III/Connections).

main

A) Definition (Proposed)

Take a lattice
Γ
Γ and a (possibly non-symmetric) 2-cocycle
𝜖
(
𝛼
,
𝛽
)
ϵ(α,β). Define vertex operators
𝑉
𝛼
(
𝑧
)
V
α
	​

(z) with multiplication twisted by
𝜖
ϵ, producing a braided locality rather than skew-symmetry.

B) Modules (Proposed)

Twisted group-algebra modules: induced modules from characters of
Γ
Γ.

Fock modules: built from a Heisenberg part tensored with twisted lattice part.

C) Duality (Proposed)

You predict that Koszul duality inverts the cocycle (or exchanges
𝜖
ϵ with
𝜖
−
1
ϵ
−1
), consistent with “braiding inversion” heuristics. This needs a fully closed (O4) Koszul duality theorem to be meaningful.

4.5 Fully worked toy model (end-to-end)

Because the manuscript’s E1-chiral definition is not yet dependency-closed (Red flag 1), I provide an E1 toy model in the locally constant case, where factorization algebras on a 1-manifold reduce to ordinary
𝐸
1
E
1
	​

-algebras. This is consistent with the manuscript’s “drop skew-symmetry” philosophy (Theorem 32.3.2 [open]) but is Proposed as the cleanest sanity check.

Toy model: the quantum plane
𝐴
𝑞
A
q
	​

 as a locally constant E1-chiral algebra
Step 1. Define the algebra as E1-chiral (locally constant factorization)

Let
𝑘
k be a field and
𝑞
∈
𝑘
×
q∈k
×
. Define the graded algebra

𝐴
𝑞
:
=
𝑘
⟨
𝑥
,
𝑦
⟩
/
(
𝑦
𝑥
−
𝑞
𝑥
𝑦
)
,
deg
⁡
𝑥
=
deg
⁡
𝑦
=
1
,
A
q
	​

:=k⟨x,y⟩/(yx−qxy),degx=degy=1,

augmented by
𝜀
(
𝑥
)
=
𝜀
(
𝑦
)
=
0
ε(x)=ε(y)=0.

Claim (Proposed, but verifiable directly). The assignment
𝑈
↦
𝐴
𝑞
U↦A
q
	​

 with factorization product given by multiplication defines a locally constant factorization algebra on
𝑅
R, hence an
𝐸
1
E
1
	​

-algebra object (“E1-chiral in the locally constant sense”).

Verification route. Use the standard equivalence: locally constant factorization algebras on
𝑅
R
↔
↔
𝐸
1
E
1
	​

-algebras (external theorem; cite Ayala–Francis or Lurie once you choose a reference).

Step 2. Compute a piece of the bar complex

Use the reduced algebraic bar complex
𝐵
∙
(
𝐴
𝑞
)
B
∙
	​

(A
q
	​

) with

𝐵
𝑛
(
𝐴
𝑞
)
=
𝐴
𝑞
‾
⊗
𝑛
,
𝑑
(
𝑎
1
∣
⋯
∣
𝑎
𝑛
)
=
∑
𝑖
=
1
𝑛
−
1
(
−
1
)
𝑖
−
1
(
𝑎
1
∣
⋯
∣
𝑎
𝑖
𝑎
𝑖
+
1
∣
⋯
∣
𝑎
𝑛
)
.
B
n
	​

(A
q
	​

)=
A
q
	​

	​

⊗n
,d(a
1
	​

∣⋯∣a
n
	​

)=
i=1
∑
n−1
	​

(−1)
i−1
(a
1
	​

∣⋯∣a
i
	​

a
i+1
	​

∣⋯∣a
n
	​

).

(Here
𝐴
𝑞
‾
=
ker
⁡
𝜀
A
q
	​

	​

=kerε.)

Compute:

In degree 1:
𝐵
1
=
𝐴
𝑞
‾
B
1
	​

=
A
q
	​

	​

 and
𝑑
=
0
d=0. So
𝑥
,
𝑦
x,y are cycles.

In degree 2:
𝐵
2
=
𝐴
𝑞
‾
⊗
𝐴
𝑞
‾
B
2
	​

=
A
q
	​

	​

⊗
A
q
	​

	​

, and

𝑑
(
𝑦
∣
𝑥
−
𝑞
 
𝑥
∣
𝑦
)
=
𝑦
𝑥
−
𝑞
𝑥
𝑦
=
0
in
𝐴
𝑞
.
d(y∣x−qx∣y)=yx−qxy=0in A
q
	​

.

So
𝜉
:
=
𝑦
∣
𝑥
−
𝑞
𝑥
∣
𝑦
ξ:=y∣x−qx∣y is a 2-cycle.

A standard graded argument shows that in the minimal resolution this class survives to homology, yielding
dim
⁡
T
o
r
2
𝐴
𝑞
(
𝑘
,
𝑘
)
=
1
dimTor
2
A
q
	​

	​

(k,k)=1. (I give a self-contained resolution below.)

Step 3. Identify the Koszul dual object

The quadratic dual of
𝐴
𝑞
A
q
	​

 is

𝐴
𝑞
!
:
=
𝑘
⟨
𝑥
\*
,
𝑦
\*
⟩
/
(
𝑥
\*
2
,
 
𝑦
\*
2
,
 
𝑥
\*
𝑦
\*
+
𝑞
 
𝑦
\*
𝑥
\*
)
.
A
q
!
	​

:=k⟨x
\*
,y
\*
⟩/(x
\*2
,y
\*2
,x
\*
y
\*
+qy
\*
x
\*
).

(This is computed by
𝑅
⊥
R
⊥
 for
𝑅
=
⟨
𝑦
⊗
𝑥
−
𝑞
 
𝑥
⊗
𝑦
⟩
R=⟨y⊗x−qx⊗y⟩.)

Claim (Proposed, but checkable directly).
𝐴
𝑞
A
q
	​

 is Koszul and
E
x
t
𝐴
𝑞
∙
(
𝑘
,
𝑘
)
≅
𝐴
𝑞
!
Ext
A
q
	​

∙
	​

(k,k)≅A
q
!
	​

, with
T
o
r
∙
𝐴
𝑞
(
𝑘
,
𝑘
)
Tor
∙
A
q
	​

	​

(k,k) dual to
𝐴
𝑞
!
A
q
!
	​

 as a coalgebra.

Verification (explicit minimal resolution).
Define a graded free resolution:

0
→
𝐴
𝑞
(
−
2
)
→
𝑑
2
𝐴
𝑞
(
−
1
)
⊕
2
→
𝑑
1
𝐴
𝑞
→
𝑘
→
0
0→A
q
	​

(−2)
d
2
	​

	​

A
q
	​

(−1)
⊕2
d
1
	​

	​

A
q
	​

→k→0

by

𝑑
1
(
𝑎
,
𝑏
)
=
𝑎
𝑥
+
𝑏
𝑦
,
𝑑
2
(
𝑐
)
=
(
𝑐
 
𝑦
,
 
−
𝑐
 
𝑞
 
𝑥
)
.
d
1
	​

(a,b)=ax+by,d
2
	​

(c)=(cy,−cqx).

Then

𝑑
1
𝑑
2
(
𝑐
)
=
(
𝑐
𝑦
)
𝑥
+
(
−
𝑐
𝑞
𝑥
)
𝑦
=
𝑐
(
𝑦
𝑥
−
𝑞
𝑥
𝑦
)
=
0.
d
1
	​

d
2
	​

(c)=(cy)x+(−cqx)y=c(yx−qxy)=0.

Tensoring with
𝑘
k over
𝐴
𝑞
A
q
	​

 kills
𝑥
,
𝑦
x,y, so the differentials become zero and

T
o
r
0
(
𝑘
,
𝑘
)
≅
𝑘
,
T
o
r
1
(
𝑘
,
𝑘
)
≅
𝑘
⊕
2
,
T
o
r
2
(
𝑘
,
𝑘
)
≅
𝑘
,
Tor
0
	​

(k,k)≅k,Tor
1
	​

(k,k)≅k
⊕2
,Tor
2
	​

(k,k)≅k,

matching the graded dimensions of
𝐴
𝑞
!
A
q
!
	​

 (degrees 0,1,2).

This gives the toy-model identification: the bar homology is concentrated in degrees
≤
2
≤2 and matches the quantum exterior dual.

Step 4. Build a concrete module and compute an invariant

Define an
𝐴
𝑞
A
q
	​

-module
𝑀
M on the graded vector space
𝑘
[
𝑡
]
k[t] by

𝑥
⋅
𝑡
𝑛
:
=
𝑡
𝑛
+
1
,
𝑦
⋅
𝑡
𝑛
:
=
𝑞
𝑛
 
𝑡
𝑛
.
x⋅t
n
:=t
n+1
,y⋅t
n
:=q
n
t
n
.

Check:
𝑦
(
𝑥
𝑡
𝑛
)
=
𝑦
𝑡
𝑛
+
1
=
𝑞
𝑛
+
1
𝑡
𝑛
+
1
y(xt
n
)=yt
n+1
=q
n+1
t
n+1
, while
𝑞
𝑥
(
𝑦
𝑡
𝑛
)
=
𝑞
𝑥
(
𝑞
𝑛
𝑡
𝑛
)
=
𝑞
𝑛
+
1
𝑡
𝑛
+
1
qx(yt
n
)=qx(q
n
t
n
)=q
n+1
t
n+1
, so
𝑦
𝑥
=
𝑞
𝑥
𝑦
yx=qxy holds.

Invariant (explicit). The graded character of
𝑀
M (with
deg
⁡
𝑡
=
1
degt=1) is

𝜒
𝑀
(
𝑢
)
=
∑
𝑛
≥
0
𝑢
𝑛
=
1
1
−
𝑢
.
χ
M
	​

(u)=
n≥0
∑
	​

u
n
=
1−u
1
	​

.
Step 5. How this interfaces with your chiral bar complex (Proposed)

In the locally constant case, your geometric bar complex should reduce to the ordinary bar complex (configuration-space forms contribute a contractible factor). This is the sanity-check that your E1 theory should pass once Definition G.6.13 is repaired.

main

main

5) Actionable edit plan (author-facing; dependency-ordered)

I group tasks into 1 week / 1 month / 3 months / 1 year, and I insist each item is dependency-closed.

5.1 One week: stabilize the foundations and remove contradictions

Fix the free-fermion contradiction (Example 13.9.16 vs Proposition 17.3.2). Either rename objects or correct the proposition.

Remove definitional circularity: rewrite Definition G.6.13 so it does not depend on Theorem 32.3.2.

main

State global hypotheses once: category of D-modules (holonomic? derived?), augmentation/completion conventions, and the meaning of factorization algebra used. Anchor Definition 3.10.5 and Theorem 3.10.7 with a precise scope statement.

main

main

Resolve typos that signal conceptual confusion: e.g. Definition 5.1.53’s “
𝑗
:
𝐶
𝑛
+
1
(
𝑋
)
↪
𝐶
𝑛
+
1
(
𝑋
)
j:C
n+1
	​

(X)↪C
n+1
	​

(X)” should be corrected (it must be the open inclusion of the complement of diagonals).

main

5.2 One month: close the residue engine and make
𝑑
2
=
0
d
2
=0 intrinsic

Prove Lemma 4.1.25 and remove [open]. It is too foundational.

Prove Theorem A.12.1 and remove [open]. Then rewrite Theorem 5.1.20 to cite it as the main mechanism.

Rewrite the nilpotence proof as a boundary-strata argument, not a nine-term cancellation; incorporate Lemma 13.9.31 sign conventions explicitly.

5.3 Three months: repair cobar and close Koszul duality circularity

Replace distributional cobar definition by a Verdier-dual construction; move distributions to a corollary theorem (requires tackling the “
3
𝛿
123
≠
0
3δ
123
	​


=0” issue head-on).

main

main

Restate Corollary 5.2.24 with hypotheses (conilpotence + completion + Koszulity). Then prove it with a filtered spectral sequence.

main

Finish the three-stage circularity resolution and remove [open] from Corollary 9.4.9 by writing a complete proof in a fixed model/∞-category.

5.4 One year: E1-chiral + primary examples (Yangian/CoHA) as real theorems

Axiomatize E1-chiral algebras (braided factorization algebras) and prove a clean recognition theorem; then treat Theorem 32.3.2 as motivation/physics.

Prove Theorem 22.1.4 in a rigorous form for
𝑠
𝑙
2
sl
2
	​

 first (full construction of factorization operations from RTT/YBE), then generalize.

main

Develop module categories as factorization modules; compute at least one nontrivial character/fusion rule in a worked example (evaluation module or Fock module). This is essential for representation-theoretic credibility.

Genus-1/elliptic extension: either prove Theorem 1.7.4 in a modular-operad framework or explicitly declare genus
>
0
>0 as conjectural and remove Theorem 5.8.4’s “proved” status unless a proof replaces the “verified through genus 5” claim.

main

Final referee-style verdict (tight)

The genus-0 configuration-space bar complex is a plausible and potentially valuable contribution, but it is not yet Annals-grade because the global boundary/residue nilpotence mechanism is not dependency-closed (A.12.1 is [open]) and because cobar is defined via distributions without a Verdier-dual theorem.

The E1-chiral part is currently conceptual scaffolding, not a definition-driven theory; it must be rebuilt from axioms upward before Yangian/quantum group claims become checkable.

The manuscript already contains its own diagnosis of the hardest issue (Koszul duality circularity). That diagnosis is correct; the resolution is incomplete and must be finished before downstream identifications are publishable as theorems.
