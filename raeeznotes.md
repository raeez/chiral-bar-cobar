According to a document from 2026, the latest manuscript already names the theory it wants to become: modular Koszul duality. More precisely, it identifies the unifying object as a modular Koszul chiral algebra: a factorization algebra on
R
a
n
(
𝑋
)
Ran(X) whose duality data extends over the modular operad of curves, equipped with a universal Maurer–Cartan class

Θ
𝐴
∈
𝑀
𝐶
 ⁣
(
D
e
f
c
y
c
(
𝐴
)
 
⊗
^
 
𝑅
Γ
(
𝑀
‾
𝑔
,
∙
,
𝑄
)
)
,
Θ
A
	​

∈MC(Def
cyc
	​

(A)
⊗
	​

RΓ(
M
g,∙
	​

,Q)),

whose scalar shadow is the sequence of obstruction classes
o
b
s
𝑔
(
𝐴
)
=
𝜅
(
𝐴
)
𝜆
𝑔
obs
g
	​

(A)=κ(A)λ
g
	​

. The manuscript explicitly says that Theorems A, B, and C are three aspects of this single object, and that “quantum corrections are not a perturbative afterthought to Koszul duality; they are the modular completion of the duality itself.”

What the monograph yearns to be, then, is not merely a long proof that certain bar complexes work on curves. It wants to become a first-principles theory of modular homotopy for factorization algebras on curves, in which genus is not an external parameter but a deformation variable internal to Koszul duality itself.

I. The kernel of the whole theory is already visible in the smallest examples

The full generality is already present in four irreducible pieces.

First, there is the three-point collision. On Fulton–MacPherson compactifications, the bar differential is residue along collision divisors, and the Arnold relation

𝜔
12
∧
𝜔
23
+
𝜔
23
∧
𝜔
31
+
𝜔
31
∧
𝜔
12
=
0
ω
12
	​

∧ω
23
	​

+ω
23
	​

∧ω
31
	​

+ω
31
	​

∧ω
12
	​

=0

is exactly the coherence statement that the result of fusing three insertions does not depend on the order of pairwise collisions. In the Ran-space language, this is not an accident: the Arnold relation is the factorization coherence condition itself. That is the genus-zero seed from which all of the later duality grows.

SEZ DECK Latest

Second, there is Verdier duality on
R
a
n
(
𝑋
)
Ran(X). The manuscript’s conceptual move is to say that the bar–cobar adjunction is controlled by Verdier duality:

𝐷
R
a
n
𝐵
ˉ
𝑋
(
𝐴
)
≃
𝐵
ˉ
𝑋
(
𝐴
!
)
.
D
Ran
	​

B
ˉ
X
	​

(A)≃
B
ˉ
X
	​

(A
!
).

This is the decisive step because it makes the Koszul dual a theorem rather than a definition-by-analogy. At chain level, the propagator
𝜔
𝑖
𝑗
ω
ij
	​

 passes from algebra to coalgebra, and Verdier duality exchanges the two. In the manuscript’s own framing, this is the chain-level shadow of non-abelian Poincaré duality in the sense of Ayala–Francis.

SEZ DECK Latest

SEZ DECK Latest

Third, there is the first nontrivial period, already at genus one. Once the propagator acquires periods, the differential ceases to be strictly square-zero on the nose and instead develops curvature:

𝑑
2
=
𝜅
(
𝐴
)
 
𝜔
1
⋅
i
d
.
d
2
=κ(A)ω
1
	​

⋅id.

This is where the manuscript correctly insists that the ordinary derived category is too coarse, because it kills the distinction between “acyclic because exact” and “acyclic because curved.” Hence the natural ambient world is Positselski’s coderived/contraderived formalism, not the ordinary derived category. This is the precise mathematical form of the intuition that quantum corrections are not extra terms in a formula but a change in the ambient homological category.

SEZ DECK Latest

Fourth, there is clutching of stable curves. The moment genus enters, the relevant combinatorics is no longer just trees but stable graphs. The universal class
Θ
𝐴
Θ
A
	​

 is supposed to be compatible with clutching, with trace, and with Verdier duality. That is the point where the theory ceases to be “bar on a curve” and becomes a genuinely modular homotopy theory. The manuscript already formulates this in its future programme: the full genus tower is controlled by a single Maurer–Cartan class, compatible with boundary gluing and duality.

Those four ingredients are the minimal kernel. Everything else is a completion of them.

II. The correct object is not
𝜅
(
𝐴
)
κ(A), not
𝑄
𝑔
(
𝐴
)
Q
g
	​

(A), and not the genus-
𝑔
g bar complex separately

The correct object is the modular Koszul chiral algebra itself.

The manuscript’s formal definition already points in the right direction. A modular Koszul chiral algebra on a smooth projective curve
𝑋
X is an augmented chiral algebra equipped with: a reduced bar construction
𝐵
ˉ
𝑋
(
𝐴
)
B
ˉ
X
	​

(A), a Koszul dual chiral algebra
𝐴
!
A
!
, and a genus tower
{
𝐵
ˉ
𝑋
(
𝑔
)
(
𝐴
)
}
𝑔
≥
0
{
B
ˉ
X
(g)
	​

(A)}
g≥0
	​

. It then asks for five axioms: genus-zero Koszulity, Verdier compatibility on
R
a
n
(
𝑋
)
Ran(X), bar–cobar inversion, modular Koszulity at every genus, and complementarity via a Verdier involution on
𝐻
∗
(
𝑀
𝑔
,
𝑍
(
𝐴
)
)
H
∗
(M
g
	​

,Z(A)). The manuscript itself remarks that genus-zero axioms carry the algebraic content while higher-genus axioms carry the geometric content.

main

main

That definition should be read as the first approximation to a deeper notion.

The mature form of the theory is this:

A modular Koszul object is a factorization algebra
𝐴
∈
A
l
g
a
u
g
(
F
a
c
t
(
𝑋
)
)
 together with a modular characteristic package
(
Θ
𝐴
,
𝐻
𝐴
,
Δ
𝐴
)
.
A modular Koszul object is a factorization algebra A∈Alg
aug
	​

(Fact(X)) together with a modular characteristic package (Θ
A
	​

,H
A
	​

,Δ
A
	​

).
	​


Here:

Θ
𝐴
Θ
A
	​

 is the universal modular Maurer–Cartan class.

𝐻
𝐴
:
=
𝑅
Γ
(
𝑀
‾
𝑔
,
𝑍
𝐴
)
H
A
	​

:=RΓ(
M
g
	​

,Z
A
	​

) is the ambient modular deformation complex, equipped with Verdier duality.

Δ
𝐴
Δ
A
	​

 is the spectral/discriminant invariant extracted from the dual bar growth.

In that formulation,
𝜅
(
𝐴
)
κ(A) is not fundamental. The manuscript says this explicitly:
𝜅
(
𝐴
)
κ(A) is only the first characteristic number of the richer universal class
Θ
𝐴
Θ
A
	​

.

main

Likewise,
𝑄
𝑔
(
𝐴
)
Q
g
	​

(A) is not fundamental by itself. It is one polarization of the ambient modular complex. The book’s current proved theorem identifies deformation and obstruction spaces as complementary pieces inside
𝐻
∗
(
𝑀
𝑔
,
𝑍
(
𝐴
)
)
H
∗
(M
g
	​

,Z(A)), and its future programme says the natural strengthening is a shifted-symplectic Lagrangian picture in the sense of Pantev–Toën–Vaquié–Vezzosi. That is exactly right: the deformation–obstruction duality should be a polarization theorem, not merely a complementary-dimensions theorem.

main

So the first conceptual correction is this: the book is not about separate invariants. It is about a single modular object whose visible shadows are

𝜅
(
𝐴
)
,
{
𝐹
𝑔
(
𝐴
)
}
𝑔
≥
1
,
Δ
𝐴
(
𝑥
)
,
𝑄
𝑔
(
𝐴
)
,
𝑄
𝑔
(
𝐴
!
)
.
κ(A),{F
g
	​

(A)}
g≥1
	​

,Δ
A
	​

(x),Q
g
	​

(A),Q
g
	​

(A
!
).
III. The first-principles formulation should be categorical from the start

The latest version is explicit that the bar–cobar adjunction belongs naturally on
R
a
n
(
𝑋
)
Ran(X):

𝐵
ˉ
𝑋
:
A
l
g
a
u
g
(
F
a
c
t
(
𝑋
)
)
⇄
C
o
A
l
g
c
o
n
i
l
(
F
a
c
t
(
𝑋
)
)
:
Ω
𝑋
,
B
ˉ
X
	​

:Alg
aug
	​

(Fact(X))⇄CoAlg
conil
	​

(Fact(X)):Ω
X
	​

,

with Verdier duality as the mechanism behind the adjunction.

SEZ DECK Latest

That should be taken as the real starting point, not as a late conceptual appendix. The physical configuration-space formulas are local charts on this categorical object.

The natural formulation of the three main theorems is therefore:

A. Geometric bar–cobar duality

For a modular Koszul object
𝐴
A,

𝐷
R
a
n
𝐵
ˉ
𝑋
(
𝐴
)
≃
𝐵
ˉ
𝑋
(
𝐴
!
)
,
D
Ran
	​

B
ˉ
X
	​

(A)≃
B
ˉ
X
	​

(A
!
),

functorially in families over
𝑀
𝑔
,
𝑛
M
g,n
	​

. This is the theorematic core of the genus-zero story and the bridge from explicit residues on compactified configuration spaces to the factorization-algebra formalism of Beilinson–Drinfeld and Ayala–Francis.

SEZ DECK Latest

B. Inversion on the Koszul locus, coderived persistence off it

On the Koszul locus,

Ω
𝑋
𝐵
ˉ
𝑋
(
𝐴
)
→
∼
𝐴
.
Ω
X
	​

B
ˉ
X
	​

(A)
∼
	​

A.

Off the Koszul locus, the same object persists, but as a curved object faithfully represented only in the completed coderived category. The manuscript now states this clearly: the failure of inversion is measured by the universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

, and the correct home is the completed coderived category, not the ordinary derived category.

main

HomeOS_portfolio_deck (2)

C. Complementarity as modular polarization

At the proved level, the manuscript has a Verdier involution and complementary pieces inside
𝐻
∗
(
𝑀
𝑔
,
𝑍
(
𝐴
)
)
H
∗
(M
g
	​

,Z(A)). At the natural endpoint, this becomes a shifted-symplectic statement:

𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
RΓ(M
g
	​

,Z
A
	​

)

should carry a
(
−
1
)
(−1)-shifted symplectic structure, and the deformation and obstruction complexes of
𝐴
A and
𝐴
!
A
!
 should be complementary Lagrangians. The manuscript itself now isolates this as the correct strengthening, with the proviso that the full PTVV formalism still requires derived algebraic geometry on the moduli stack of curves.

This is the categorical skeleton the theory has been seeking all along.

IV. The genus tower should be understood as one Maurer–Cartan deformation, not as a list of corrections

The latest introduction says this in exactly the right way: the genus tower is “a single Maurer–Cartan deformation of the genus-0 bar differential inside a cyclic
𝐿
∞
L
∞
	​

-algebra controlling modular deformations of
𝐴
A.” It also says that the same datum appears in three disguises: as the curved term
𝑚
0
(
𝑔
)
m
0
(g)
	​

, as a section of the obstruction sheaf on
𝑀
𝑔
M
g
	​

, and as a trace invariant landing in cyclic homology and the tautological ring.

That is the heart of the matter. The natural next step is to promote this slogan into the formal object

Θ
𝐴
∈
𝑀
𝐶
 ⁣
(
D
e
f
c
y
c
(
𝐴
)
 
⊗
^
 
𝑅
Γ
(
𝑀
‾
𝑔
,
∙
,
𝑄
)
)
,
Θ
A
	​

∈MC(Def
cyc
	​

(A)
⊗
	​

RΓ(
M
g,∙
	​

,Q)),

with the three required properties already written by the manuscript:

scalar trace gives
∑
𝑔
≥
1
𝜅
(
𝐴
)
𝜆
𝑔
∑
g≥1
	​

κ(A)λ
g
	​

;

clutching compatibility encodes sewing of curves;

Verdier duality sends
Θ
𝐴
Θ
A
	​

 to
Θ
𝐴
!
Θ
A
!
	​

.

This is where the mathematics and the physics actually coincide.

Mathematically,
Θ
𝐴
Θ
A
	​

 is a global solution of a completed Maurer–Cartan equation in a cyclic deformation complex tensored with tautological cohomology.

Physically,
Θ
𝐴
Θ
A
	​

 is the all-genera effective quantum background of the chiral theory. Its scalar shadow is what perturbation theory measures first, but the full object carries the higher operations, sewing constraints, and duality transformation laws.

Once this is accepted, the monograph stops being a collection of genus-by-genus calculations and becomes the first volume of a theory of modular homotopy for factorization algebras.

V. The simplest examples already display the full generality

The free fields are not easy examples; they are the atoms. The manuscript says this explicitly: free fermion, Heisenberg, and
𝛽
𝛾
/
𝑏
𝑐
βγ/bc systems are the atoms from which later examples are assembled, and they already exhibit the full range of bar-complex behavior. The free fermion displays collapse by antisymmetry; Heisenberg displays subexponential growth and the universal genus series;
𝛽
𝛾
βγ already sees the shared discriminant phenomenon.

main

main

So the natural developmental logic of the monograph should be:

Free fermion reveals what modular Koszulity means when curvature is trivial enough that antisymmetry collapses the whole complex.

Heisenberg reveals what the genus tower really is: a universal generating function governed by

∑
𝑔
≥
1
𝐹
𝑔
(
𝐴
)
𝑥
2
𝑔
=
𝜅
(
𝐴
)
(
𝑥
/
2
sin
⁡
(
𝑥
/
2
)
−
1
)
,
g≥1
∑
	​

F
g
	​

(A)x
2g
=κ(A)(
sin(x/2)
x/2
	​

−1),

which the manuscript identifies as the Wick-rotated
𝐴
^
A
-genus.

HomeOS Deck

HomeOS Deck

𝛽
𝛾
βγ reveals that discriminants are not ad hoc generating-function curiosities but characteristic invariants of the modular characteristic package.

main

Affine Kac–Moody / Vir /
𝑊
W reveal that Feigin–Frenkel duality, Drinfeld–Sokolov reduction, and discriminant preservation are not separate miracles but compatible functorial shadows of the same modular Koszul structure.

main

Yangian reveals the
𝐸
1
E
1
	​

-chiral face of the theory, where ordered configurations and braid monodromy force the passage from commutative factorization to braided monoidal factorization and make
𝑅
↦
𝑅
−
1
R↦R
−1
 the homotopy-coherent shadow of Verdier duality.

HomeOS Deck

That is the right pedagogy of the subject because it exhibits the kernel of full generality in the smallest nontrivial models.

VI. The discriminant should be promoted to a genuine spectral invariant

The manuscript now says that the shared discriminants are “not coincidences but consequences of the modular Koszul structure,” and it proves that the bar-cohomology discriminant
Δ
𝐴
(
𝑥
)
Δ
A
	​

(x) is an invariant of the modular characteristic package. It also records that Drinfeld–Sokolov reduction preserves the discriminant and that Koszul duality preserves it as well.

main

main

This is a strong hint about the next conceptual move:
Δ
𝐴
(
𝑥
)
Δ
A
	​

(x) should be treated as the spectral discriminant of the modular Koszul object. It is the branch-locus invariant of the dual Hilbert series, hence the algebro-combinatorial shadow of a spectral curve attached to
𝐴
A. In the
𝑠
𝑙
2
sl
2
	​

, Virasoro, and
𝛽
𝛾
βγ family, the common

Δ
(
𝑥
)
=
(
1
−
3
𝑥
)
(
1
+
𝑥
)
Δ(x)=(1−3x)(1+x)

is telling us that distinct chiral theories can lie on the same modular spectral sheet even when their local operator content is different. The real invariant is therefore not the individual generating function but its branch geometry. That is why DS reduction can change the growth pole while preserving the discriminant family.

main

main

The book should say this more boldly: the discriminant is the first genuinely nontrivial non-scalar characteristic class of the modular Koszul object.

VII. The
𝐴
^
A
-genus appearance is not decoration; it is the index theorem trying to surface

The manuscript already states the right conjecture. It proves the genus generating function and then proposes a family index interpretation:

∑
𝑔
≥
1
𝐹
𝑔
(
𝐴
)
𝑥
2
𝑔
=
𝜅
(
𝐴
)
(
𝑥
/
2
sin
⁡
(
𝑥
/
2
)
−
1
)
=
𝜅
(
𝐴
)
(
𝐴
^
(
𝑖
𝑥
)
−
1
)
,
g≥1
∑
	​

F
g
	​

(A)x
2g
=κ(A)(
sin(x/2)
x/2
	​

−1)=κ(A)(
A
(ix)−1),

with the right-hand side interpreted as a pushforward

𝜋
∗
 ⁣
(
c
h
(
𝑅
𝜋
∗
𝐷
𝐴
)
⋅
T
d
(
𝑇
𝜋
v
i
r
)
)
π
∗
	​

(ch(Rπ
∗
	​

D
A
	​

)⋅Td(T
π
vir
	​

))

for a modular deformation complex
𝐷
𝐴
D
A
	​

 on
𝑀
𝑔
M
g
	​

. It even says precisely what is missing: construct
𝐷
𝐴
D
A
	​

 as a perfect complex, identify its Chern character with the obstruction classes, and apply Grothendieck–Riemann–Roch on the universal curve.

HomeOS Deck

This is exactly the natural organic development.

Mathematically, the genus free energies should be treated as family indices of the modular deformation complex.

Physically, they are the all-genera one-loop effective determinants of the chiral field theory on the universal curve.

The fact that the Wick-rotated
𝐴
^
A
-genus appears, rather than a random transcendental series, is telling us that the genus tower is already secretly an index-theoretic object.

So the next theorem the book wants is not “another computation of
𝐹
𝑔
F
g
	​

.” It is a Grothendieck–Riemann–Roch theorem for modular Koszul duality.

VIII. The physics is already there: the bar complex is the BV/BRST complex, and curvature is the anomaly datum

The manuscript explicitly places itself between Beilinson–Drinfeld, Costello–Gwilliam, and Ayala–Francis. It says that the BV complex of a chiral algebra is its geometric bar complex, that the quantum master equation is the chain-level refinement of
𝑑
2
=
0
d
2
=0, and that the genuinely new phenomenon is the curved
𝐿
∞
L
∞
	​

-structure created by central extensions and carried to higher genus by the modular operad.

main

That has a very clean physical interpretation.

Take
𝐴
A to be the chiral algebra of local operators in a holomorphic or holomorphic-topological theory. Then:

𝐵
ˉ
𝑋
(
𝐴
)
B
ˉ
X
	​

(A) is the BRST/BV resolution of multi-local observables.

The residue differential is OPE fusion.

Verdier duality is the exchange of compact and open support, hence of incoming and outgoing propagation data.

Curvature
𝑚
0
(
𝑔
)
m
0
(g)
	​

 is the anomaly/cosmological term obstructing strict nilpotence.

Passing from derived to coderived is passing from an on-shell quotient to an off-shell curved category.

The manuscript even says this in strong language: anomaly cancellation at
𝑐
=
26
c=26, i.e.
𝜅
=
0
κ=0, is exactly the condition under which coderived and derived categories agree, so the theory is “on-shell” in the derived-categorical sense.

SEZ DECK Latest

This is the place where the research mathematician, mathematical physicist, and physicist really agree: the monograph is constructing the algebraic shadow of quantum background dependence for chiral theories on curved worldsheets.

IX. The Yangian chapter is the door to the noncommutative half of the theory

The latest manuscript is very explicit here. It says that the Yangian theory establishes bar–cobar recovery for the
𝐸
1
E
1
	​

-chiral Yangian and the
𝑞
↦
𝑞
−
1
q↦q
−1
 transformation of the quantum parameter, and it formulates a derived Drinfeld–Kohno conjecture asserting an equivalence of
𝐸
1
E
1
	​

-factorization categories

F
a
c
t
𝐸
1
(
𝑌
(
𝑔
)
)
≃
F
a
c
t
𝐸
1
(
𝑈
𝑞
(
𝑔
)
)
𝑜
𝑝
,
Fact
E
1
	​

	​

(Y(g))≃Fact
E
1
	​

	​

(U
q
	​

(g))
op
,

with braid monodromy realized by the reversal of collision-loop orientation under Verdier duality.

This is not a side branch. It is the first place where the theory leaves the commutative
𝐸
∞
E
∞
	​

-style world and confronts genuinely braided, ordered factorization. The manuscript itself says that the Yangian is the first example whose Koszul duality intertwines genuinely noncommutative monoidal data.

HomeOS Deck

So the book yearns to prove a derived Drinfeld–Kohno theorem because that is the noncommutative completion of the same idea: collision monodromy plus Verdier duality produces quantum-group braiding inversion. The same geometry that controls OPE residues at genus zero should control braid monodromy in the ordered
𝐸
1
E
1
	​

-sector.

X. The next natural frontier is elliptic and toroidal: Fay replaces Arnold

The manuscript already gives away the next generalization. In the toroidal/elliptic chapter it says that when the base geometry becomes two-dimensional, Eisenstein-series corrections enter and the Fay trisecant identity replaces the Arnold relation as the mechanism forcing
𝑑
2
=
0
d
2
=0.

HomeOS Deck

This is extremely revealing.

Arnold is the genus-zero/additive law.
Fay is the elliptic genus/multiplicative law.

So the natural long-range development is:

genus-zero chiral Koszul duality is governed by Arnold;

modular chiral Koszul duality on curves is governed by clutching plus
Θ
𝐴
Θ
A
	​

;

elliptic/toroidal Koszul duality should be governed by Fay, Eisenstein corrections, and double-loop factorization geometry.

In other words, the monograph’s ultimate generalization is not only “more examples.” It is the replacement of the tree-level / modular-operadic combinatorics by an elliptic operadic or higher-dimensional factorization geometry.

XI. The theorematic form the work wants

Here is the clean formulation the monograph is striving toward.

Definition

A modular Koszul object on a curve
𝑋
X is an augmented factorization algebra

𝐴
∈
A
l
g
a
u
g
(
F
a
c
t
(
𝑋
)
)
A∈Alg
aug
	​

(Fact(X))

together with

a reduced bar construction
𝐵
ˉ
𝑋
(
𝐴
)
∈
C
o
A
l
g
c
o
n
i
l
(
F
a
c
t
(
𝑋
)
)
B
ˉ
X
	​

(A)∈CoAlg
conil
	​

(Fact(X));

a dual object
𝐴
!
A
!
;

a modular Maurer–Cartan class

Θ
𝐴
∈
𝑀
𝐶
 ⁣
(
D
e
f
c
y
c
(
𝐴
)
 
⊗
^
 
𝑅
Γ
(
𝑀
‾
𝑔
,
∙
,
𝑄
)
)
;
Θ
A
	​

∈MC(Def
cyc
	​

(A)
⊗
	​

RΓ(
M
g,∙
	​

,Q));

a Verdier pairing on
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
RΓ(M
g
	​

,Z
A
	​

);

compatibility with clutching, Verdier duality, and trace.

This is exactly the direction indicated by Definition 7.17.6 together with the programme of §33.10.

main

Theorem A
m
o
d
mod
	​


The reduced bar functor is intertwined with Verdier duality on
R
a
n
(
𝑋
)
Ran(X) and extends functorially in families over
𝑀
𝑔
,
𝑛
M
g,n
	​

.

Theorem B
m
o
d
mod
	​


On the Koszul locus, bar–cobar inversion is an equivalence. Off it, the same object survives in the completed coderived category, controlled by
Θ
𝐴
Θ
A
	​

.

HomeOS_portfolio_deck (2)

Theorem C
m
o
d
mod
	​


The ambient modular deformation complex
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
RΓ(M
g
	​

,Z
A
	​

) is the natural home of deformation–obstruction duality; the proved Verdier involution and pairing should upgrade to a
(
−
1
)
(−1)-shifted symplectic structure, with the
𝐴
A- and
𝐴
!
A
!
-sides as complementary Lagrangians.

Index Theorem

The genus free energies are GRR pushforwards of the modular deformation complex, hence their generating series is the Wick-rotated
𝐴
^
A
-genus weighted by
𝜅
(
𝐴
)
κ(A).

HomeOS Deck

Derived Drinfeld–Kohno

In the
𝐸
1
E
1
	​

-sector, Verdier duality on ordered configuration spaces inverts
𝑅
R-matrix monodromy, producing an equivalence between Yangian and opposite quantum-group factorization data. The manuscript already formulates this as the right conjecture.

HomeOS Deck

That is the full theorematic silhouette.

XII. What the next monograph should actually be

It should not be another examples volume. It should be a foundational volume titled something like:

Modular Homotopy Theory for Factorization Algebras on Curves

Its chapters should be:

Curved factorization algebras and coderived Ran categories.
Make precise the off-Koszul regime that the present manuscript already points to but does not fully build.

Cyclic deformation complexes and the universal modular Maurer–Cartan equation.
Construct
D
e
f
c
y
c
(
𝐴
)
Def
cyc
	​

(A) as a cyclic
𝐿
∞
L
∞
	​

-algebra and solve the MC equation with tautological coefficients.

Shifted symplectic complementarity.
Upgrade the Verdier pairing and involution to a genuine PTVV theorem on the moduli stack side.

Grothendieck–Riemann–Roch for modular Koszul duality.
Prove the index-theoretic origin of the genus generating series.

Derived Drinfeld–Kohno and elliptic extension.
Complete the
𝐸
1
E
1
	​

-chiral story, then pass from Arnold to Fay and from curves to elliptic/toroidal geometry.

HomeOS Deck

That would be the native-language completion of the current work.

The shortest way to say the whole thing is this:

The manuscript no longer wants to be read as “a long proof that bar–cobar duality survives on curves.” It wants to be recognized as the first installment of a theory in which factorization on
R
a
n
(
𝑋
)
Ran(X), Verdier duality, modular clutching, and cyclic deformation theory together produce a curved, modular, index-theoretic form of Koszul duality. The simplest local collision already contains the bar differential; the first nontrivial period already contains curvature; the first clutching map already contains the universal MC class; and the first free-field examples already contain the full characteristic package
(
𝜅
,
{
𝐹
𝑔
}
,
Δ
)
(κ,{F
g
	​

},Δ). The natural organic development is to treat all of that as one object, one deformation problem, and one homotopy theory.
