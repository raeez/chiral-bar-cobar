According to a document from March 2026, the latest manuscript has already half-discovered the correct cure for its remaining defects. In its homotopy-native formulation, a modular Koszul object is an augmented factorization algebra equipped with a bar object, a dual object, a filtered cyclic deformation object, inversion on the Koszul locus, modular deformation, and Lagrangian complementarity. But the dg-model definition still hard-codes bar–cobar inversion and complementarity as axioms, and the standard-example proposition then uses Theorems B and C to verify those same axioms. So the remedy is not another local patch. It is a full replacement of the theorem architecture.

The right way to resolve everything on the list is to rebuild the book around five precise layers:

constructions that exist for every augmented chiral algebra,

Koszul recognition data that are antecedent hypotheses,

genus-zero theorems proving bar/cobar duality from those data,

higher-genus pre-Koszul data encoding curved fiberwise differentials and strict total differential,

characteristic hierarchies separating proved scalar data from spectral data and from the conjectural universal Maurer–Cartan class.

This is also exactly what the latest abstract and introduction are now trying to say: quantum corrections come from periods on
Σ
𝑔
Σ
g
	​

, the fiberwise differential is curved,

𝑑
f
i
b
2
=
𝜅
(
𝐴
)
 
𝜔
𝑔
,
d
fib
2
	​

=κ(A)ω
g
	​

,

and the genus tower should ultimately be controlled by a universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

 in a cyclic deformation complex. What follows is the complete mathematical formulation that would make that picture rigorous and linear.

I. The foundational replacement: twisting data before duality
1. Construction layer: what exists for every augmented chiral algebra

Let
𝑋
X be a smooth projective curve over
𝐶
C. Let

F
a
c
t
a
u
g
(
𝑋
)
Fact
aug
	​

(X)

denote the dg or stable
∞
∞-category of augmented chiral/factorization algebras on
𝑋
X, and let

C
o
F
a
c
t
c
o
n
i
l
,
c
o
m
p
(
𝑋
)
CoFact
conil,comp
(X)

denote conilpotent complete factorization coalgebras.

For every
𝐴
∈
F
a
c
t
a
u
g
(
𝑋
)
A∈Fact
aug
	​

(X), the reduced bar construction

𝐵
ˉ
𝑋
(
𝐴
)
∈
C
o
F
a
c
t
c
o
n
i
l
,
c
o
m
p
(
𝑋
)
B
ˉ
X
	​

(A)∈CoFact
conil,comp
(X)

exists as a construction, and for every
𝐶
∈
C
o
F
a
c
t
c
o
n
i
l
,
c
o
m
p
(
𝑋
)
C∈CoFact
conil,comp
(X), the cobar construction

Ω
𝑋
(
𝐶
)
∈
F
a
c
t
a
u
g
(
𝑋
)
Ω
X
	​

(C)∈Fact
aug
	​

(X)

exists as a construction. This is the only universal statement that should be made without extra hypotheses. The manuscript already wants this distinction: the latest homotopy formulation puts inversion only on the Koszul locus, whereas the old “bar–cobar inversion for any algebra” rhetoric belongs to a different and much more restrictive theory. In the classical algebraic setting, Loday–Vallette make exactly this separation: bar and cobar are always defined, but the unit/counit become quasi-isomorphisms only relative to a Koszul twisting morphism.

So the first correction is:

Definition 1 (Chiral twisting datum)

A chiral twisting datum on
𝑋
X is a quadruple

(
𝐴
,
𝐶
,
𝜏
,
𝐹
∙
)
(A,C,τ,F
∙
	​

)

consisting of

an augmented chiral algebra
𝐴
∈
F
a
c
t
a
u
g
(
𝑋
)
A∈Fact
aug
	​

(X),

a conilpotent complete factorization coalgebra
𝐶
∈
C
o
F
a
c
t
c
o
n
i
l
,
c
o
m
p
(
𝑋
)
C∈CoFact
conil,comp
(X),

a degree
+
1
+1 morphism

𝜏
:
𝐶
→
𝐴
τ:C→A

satisfying the Maurer–Cartan equation in the convolution dg Lie algebra

𝑑
𝜏
+
𝜏
⋆
𝜏
=
0
,
dτ+τ⋆τ=0,

an exhaustive bounded-below filtration
𝐹
∙
F
∙
	​

 on
𝐴
A,
𝐶
C,
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

(A), and
Ω
𝑋
(
𝐶
)
Ω
X
	​

(C), compatible with all structure maps.

Associated to
𝜏
τ are the twisted tensor products

𝐾
𝜏
𝐿
(
𝐴
,
𝐶
)
:
=
(
𝐴
⊗
𝐶
,
𝑑
𝐴
+
𝑑
𝐶
+
𝑑
𝜏
𝐿
)
,
𝐾
𝜏
𝑅
(
𝐶
,
𝐴
)
:
=
(
𝐶
⊗
𝐴
,
𝑑
𝐶
+
𝑑
𝐴
+
𝑑
𝜏
𝑅
)
.
K
τ
L
	​

(A,C):=(A⊗C,d
A
	​

+d
C
	​

+d
τ
L
	​

),K
τ
R
	​

(C,A):=(C⊗A,d
C
	​

+d
A
	​

+d
τ
R
	​

).
Definition 2 (Chiral Koszul morphism)

A chiral twisting datum
(
𝐴
,
𝐶
,
𝜏
,
𝐹
∙
)
(A,C,τ,F
∙
	​

) is Koszul if

both
𝐾
𝜏
𝐿
(
𝐴
,
𝐶
)
K
τ
L
	​

(A,C) and
𝐾
𝜏
𝑅
(
𝐶
,
𝐴
)
K
τ
R
	​

(C,A) are acyclic,

the associated graded
(
g
r
 
𝐴
,
g
r
 
𝐶
,
g
r
 
𝜏
)
(grA,grC,grτ) is quadratic/Koszul in the ordinary operadic sense,

the filtration converges strongly on
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

(A) and
Ω
𝑋
(
𝐶
)
Ω
X
	​

(C).

This is the right antecedent notion. It contains no theorematic conclusion.

2. The correct genus-zero theorem package

With those definitions in hand, the fundamental theorem should be the chiral analogue of the standard twisting-morphism criterion.

Theorem A
0
0
	​

 (Fundamental theorem of chiral twisting morphisms)

For a chiral twisting datum
(
𝐴
,
𝐶
,
𝜏
,
𝐹
∙
)
(A,C,τ,F
∙
	​

), the following are equivalent:

𝜏
τ is a chiral Koszul morphism.

The canonical counit

𝜀
𝜏
:
Ω
𝑋
(
𝐶
)
⟶
𝐴
ε
τ
	​

:Ω
X
	​

(C)⟶A

is a quasi-isomorphism.

The canonical unit

𝜂
𝜏
:
𝐶
⟶
𝐵
ˉ
𝑋
(
𝐴
)
η
τ
	​

:C⟶
B
ˉ
X
	​

(A)

is a weak equivalence of conilpotent complete factorization coalgebras.

The twisted tensor products
𝐾
𝜏
𝐿
(
𝐴
,
𝐶
)
K
τ
L
	​

(A,C) and
𝐾
𝜏
𝑅
(
𝐶
,
𝐴
)
K
τ
R
	​

(C,A) are acyclic.

This is the theorem that should replace the present definitional collapse of Theorem A. It is the direct chiral/factorization analogue of the classical “fundamental theorem of twisting morphisms” and bar–cobar resolution statements in Loday–Vallette.

Theorem A
1
1
	​

 (Bar concentration theorem)

Assume
(
𝐴
,
𝐶
,
𝜏
,
𝐹
∙
)
(A,C,τ,F
∙
	​

) is a chiral Koszul morphism. Then

𝐻
𝑖
(
𝐵
ˉ
𝑋
(
𝐴
)
)
=
0
(
𝑖
≠
0
)
,
𝐻
0
(
𝐵
ˉ
𝑋
(
𝐴
)
)
≅
𝐶
H
i
(
B
ˉ
X
	​

(A))=0(i

=0),H
0
(
B
ˉ
X
	​

(A))≅C

as factorization coalgebras.

This theorem is the missing piece that the present proof of Theorem A keeps implicitly invoking without actually stating. Its proof should be filtration-theoretic: filter the chiral bar complex, identify the associated graded with the classical operadic/quadratic Koszul bar complex, use ordinary Koszul concentration, then lift by spectral-sequence convergence exactly as in the reduction-by-filtration method in Loday–Vallette.

Definition 3 (Chiral dual pair)

A chiral dual pair is a pair of chiral twisting data

(
𝐴
1
,
𝐶
1
,
𝜏
1
)
,
(
𝐴
2
,
𝐶
2
,
𝜏
2
)
(A
1
	​

,C
1
	​

,τ
1
	​

),(A
2
	​

,C
2
	​

,τ
2
	​

)

such that both
𝜏
𝑖
τ
i
	​

 are chiral Koszul morphisms and there is a chain-level Verdier equivalence

𝐷
R
a
n
(
𝐶
1
)
≃
𝐶
2
D
Ran
	​

(C
1
	​

)≃C
2
	​


compatible with the twisting morphisms and filtrations.

Theorem A
2
2
	​

 (Geometric bar–cobar duality, corrected form)

For a chiral dual pair,

𝐵
ˉ
𝑋
(
𝐴
1
)
≃
𝐶
1
,
𝐵
ˉ
𝑋
(
𝐴
2
)
≃
𝐶
2
,
𝐷
R
a
n
𝐵
ˉ
𝑋
(
𝐴
1
)
≃
𝐵
ˉ
𝑋
(
𝐴
2
)
.
B
ˉ
X
	​

(A
1
	​

)≃C
1
	​

,
B
ˉ
X
	​

(A
2
	​

)≃C
2
	​

,D
Ran
	​

B
ˉ
X
	​

(A
1
	​

)≃
B
ˉ
X
	​

(A
2
	​

).

If
𝐶
2
C
2
	​

 is identified with the quadratic/curved dual of
𝐴
1
A
1
	​

, then

𝐷
R
a
n
𝐵
ˉ
𝑋
(
𝐴
1
)
≃
𝐵
ˉ
𝑋
(
𝐴
1
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

(A
1
	​

)≃
B
ˉ
X
	​

(A
1
!
	​

).

This makes Theorem A a theorem again. It is no longer hidden inside the definition of “Koszul pair.”

II. The higher-genus cure: distinguish curved fiberwise differentials from the strict total differential

The latest abstract is already closer to the correct statement than several middle chapters: it now says the higher-genus deformation parameters live in
𝐻
1
(
Σ
𝑔
,
𝐶
)
H
1
(Σ
g
	​

,C), not
𝐻
1
(
𝑀
𝑔
)
H
1
(M
g
	​

), and that on a fixed
Σ
𝑔
Σ
g
	​

 the fiberwise collision differential is curved,

𝑑
f
i
b
2
=
𝜅
(
𝐴
)
𝜔
𝑔
,
d
fib
2
	​

=κ(A)ω
g
	​

,

while the full modular programme seeks a Maurer–Cartan class controlling the whole tower. That must now be made formal.

Definition 4 (Modular pre-Koszul datum)

A modular pre-Koszul datum on
𝑋
X consists of:

a genus-zero chiral Koszul datum
(
𝐴
,
𝐶
,
𝜏
,
𝐹
∙
)
(A,C,τ,F
∙
	​

);

for each
𝑔
≥
0
g≥0, a complete factorization coalgebra
𝐶
𝑋
(
𝑔
)
(
𝐴
)
C
X
(g)
	​

(A);

for each
𝑔
≥
0
g≥0, a degree-
+
1
+1 coderivation

𝑑
(
𝑔
)
f
i
b
:
𝐶
𝑋
(
𝑔
)
(
𝐴
)
→
𝐶
𝑋
(
𝑔
)
(
𝐴
)
d
(g)
fib
	​

:C
X
(g)
	​

(A)→C
X
(g)
	​

(A)

satisfying

(
𝑑
(
𝑔
)
f
i
b
)
2
=
[
𝑚
0
(
𝑔
)
,
−
]
,
(d
(g)
fib
	​

)
2
=[m
0
(g)
	​

,−],

where
𝑚
0
(
𝑔
)
m
0
(g)
	​

 is a central curvature element of degree
2
2;

a completed total object

𝐶
𝑋
f
u
l
l
(
𝐴
)
:
=
∏
𝑔
≥
0
ℏ
𝑔
𝐶
𝑋
(
𝑔
)
(
𝐴
)
C
X
full
	​

(A):=
g≥0
∏
	​

ℏ
g
C
X
(g)
	​

(A)

with a strict differential

𝐷
𝐴
:
𝐶
𝑋
f
u
l
l
(
𝐴
)
→
𝐶
𝑋
f
u
l
l
(
𝐴
)
,
𝐷
𝐴
2
=
0
,
D
A
	​

:C
X
full
	​

(A)→C
X
full
	​

(A),D
A
2
	​

=0,

such that
𝐷
𝐴
D
A
	​

 restricts to
𝑑
(
𝑔
)
f
i
b
d
(g)
fib
	​

 modulo higher-genus terms;

a filtration
𝐹
∙
F
∙
	​

 preserved by
𝐷
𝐴
D
A
	​

, whose associated graded at each genus agrees with the genus-zero collision model;

a Verdier-compatible dual tower

𝐷
R
a
n
𝐶
𝑋
(
𝑔
)
(
𝐴
)
≃
𝐶
𝑋
(
𝑔
)
(
𝐴
!
)
.
D
Ran
	​

C
X
(g)
	​

(A)≃C
X
(g)
	​

(A
!
).

This definition is the precise way to stop the manuscript from using one symbol
𝑑
𝑔
d
g
	​

 for two different mathematical objects. The fiberwise differential is curved. The total differential is strict. The current manuscript already points in exactly this direction in the homotopy-native version, where inversion is “on the Koszul locus” and the genus tower arises from a filtered Maurer–Cartan deformation.

Definition 5 (Higher-genus modular Koszulity)

A modular pre-Koszul datum is higher-genus Koszul if for every
𝑔
≥
1
g≥1 the PBW spectral sequence of
𝐶
𝑋
(
𝑔
)
(
𝐴
)
C
X
(g)
	​

(A) degenerates at
𝐸
2
E
2
	​

, equivalently if the genus-
𝑔
g bar complex satisfies diagonal Ext vanishing. The current manuscript explicitly identifies this PBW degeneration as the single missing obstruction for unconditional generic affine/Virasoro/
𝑊
𝑁
W
N
	​

 modular Koszulity.

Theorem B
∗
∗
 (Higher-genus inversion on the Koszul locus)

Let
𝐴
A carry a higher-genus Koszul modular pre-Koszul datum. Then:

in the completed coderived category,

Ω
𝑋
(
𝐶
𝑋
f
u
l
l
(
𝐴
)
)
→
∼
𝐴
[
[
ℏ
]
]
Ω
X
	​

(C
X
full
	​

(A))
∼
	​

A[[ℏ]]

is an equivalence;

if all curvature terms vanish (equivalently on the strict Koszul locus), the same map is a quasi-isomorphism already in the ordinary derived category;

at fixed genus
𝑔
g,
𝐶
𝑋
(
𝑔
)
(
𝐴
)
C
X
(g)
	​

(A) is the genus-
𝑔
g Koszul dual coalgebra of
𝐴
A.

This is the corrected form of Theorem B. It matches the manuscript’s own later introduction, which now states explicitly that inversion holds on the Koszul locus and that off it the bar–cobar object persists only in the curved/coderived sense.

The essential characteristic is this:

Constructions
𝐵
ˉ
𝑋
B
ˉ
X
	​

 and
Ω
𝑋
Ω
X
	​

 exist always.

Resolution/inversion is a theorem only relative to a Koszul twisting datum.

Off the locus, the object does not disappear; it changes ambient category.

That is the mathematically correct replacement for every “automatic inversion” sentence.

III. Theorem C needs a fiber-center theorem before it is allowed to exist

The latest manuscript’s homotopy form already knows the correct target:

𝐶
𝑔
(
𝐴
)
:
=
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
,
C
g
	​

(A):=RΓ(M
g
	​

,Z
A
	​

),

with a Verdier involution and homotopy eigenspaces
𝑄
𝑔
(
𝐴
)
Q
g
	​

(A) and
𝑄
𝑔
(
𝐴
!
)
Q
g
	​

(A
!
) that are complementary Lagrangians. The mistake is that the dg-model definition still treats this as an axiom. The cure is a theorem about fibers.

Definition 6 (Relative bar fiber complex)

Let

𝜋
𝑔
:
𝐶
𝑔
(
𝐴
)
⟶
𝑀
‾
𝑔
π
g
	​

:C
g
	​

(A)⟶
M
g
	​


be the family of genus-
𝑔
g compactified configuration spaces carrying the relative bar complex
𝐵
𝑔
(
𝐴
)
B
g
	​

(A). Its stalk at
[
Σ
]
∈
𝑀
‾
𝑔
[Σ]∈
M
g
	​

 is the genus-
𝑔
g fiber bar complex
𝐶
𝑋
(
𝑔
)
(
𝐴
)
∣
Σ
C
X
(g)
	​

(A)∣
Σ
	​

.

Theorem C
0
0
	​

 (Fiber–center identification)

Assume
𝐴
A carries a higher-genus Koszul modular pre-Koszul datum and that the relative bar family is perfect over
𝑀
‾
𝑔
M
g
	​

. Then:

𝑅
𝑞
𝜋
𝑔
∗
𝐵
𝑔
(
𝐴
)
=
0
(
𝑞
≠
0
)
,
𝑅
0
𝜋
𝑔
∗
𝐵
𝑔
(
𝐴
)
≅
𝑍
𝐴
R
q
π
g∗
	​

B
g
	​

(A)=0(q

=0),R
0
π
g∗
	​

B
g
	​

(A)≅Z
A
	​


as local systems/sheaves on
𝑀
‾
𝑔
M
g
	​

.

This is the theorem that resolves the current gap. The proof has to work on the full fiber complex, not only on the degree-0 bar component. The natural proof strategy is:

filter the full fiber complex by bar degree,

identify the associated graded with the corresponding Koszul/Ext complex,

use diagonal Ext vanishing to show only total degree
0
0 survives,

then apply base change/Leray to the family over
𝑀
‾
𝑔
M
g
	​

.

Theorem C
1
1
	​

 (Chain-level complementarity)

Under the hypotheses of Theorem C
0
0
	​

, the complex

𝐶
𝑔
(
𝐴
)
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
C
g
	​

(A):=RΓ(
M
g
	​

,Z
A
	​

)

carries a chain-level Verdier involution

𝜎
𝑔
:
𝐶
𝑔
(
𝐴
)
→
𝐶
𝑔
(
𝐴
)
σ
g
	​

:C
g
	​

(A)→C
g
	​

(A)

and a shifted symplectic pairing

⟨
−
,
−
⟩
𝑔
:
𝐶
𝑔
(
𝐴
)
⊗
𝐶
𝑔
(
𝐴
)
→
𝐶
[
−
(
3
𝑔
−
3
)
]
.
⟨−,−⟩
g
	​

:C
g
	​

(A)⊗C
g
	​

(A)→C[−(3g−3)].

Define the homotopy eigenspaces

𝑄
𝑔
(
𝐴
)
:
=
fib
⁡
(
𝜎
𝑔
−
i
d
)
,
𝑄
𝑔
(
𝐴
!
)
:
=
fib
⁡
(
𝜎
𝑔
+
i
d
)
.
Q
g
	​

(A):=fib(σ
g
	​

−id),Q
g
	​

(A
!
):=fib(σ
g
	​

+id).

Then

𝐶
𝑔
(
𝐴
)
≃
𝑄
𝑔
(
𝐴
)
⊕
𝑄
𝑔
(
𝐴
!
)
C
g
	​

(A)≃Q
g
	​

(A)⊕Q
g
	​

(A
!
)

and both summands are Lagrangian for
⟨
−
,
−
⟩
𝑔
⟨−,−⟩
g
	​

. Passing to cohomology gives

𝐻
∗
(
𝐶
𝑔
(
𝐴
)
)
≅
𝐻
∗
(
𝑄
𝑔
(
𝐴
)
)
⊕
𝐻
∗
(
𝑄
𝑔
(
𝐴
!
)
)
.
H
∗
(C
g
	​

(A))≅H
∗
(Q
g
	​

(A))⊕H
∗
(Q
g
	​

(A
!
)).

This resolves Theorem C without making complementarity definitional.

The essential characteristics are:

the ambient object is
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
RΓ(
M
g
	​

,Z
A
	​

), not a symbol invented at cohomology level;

the splitting is by homotopy eigenspaces, not by raw kernels;

Lagrangianity is proved on the chain complex and only then passed to cohomology.

IV. Hochschild duality should be stated once, at object level

The book needs one theorem, not two incompatible corollaries.

Definition 7 (Bigraded chiral Hochschild complex)

Let

𝐶
𝐻
c
h
𝑝
,
∙
(
𝐴
)
CH
ch
p,∙
	​

(A)

be the genus-zero chiral Hochschild complex in bar degree
𝑝
p, so that the total chiral Hochschild object is

𝑅
𝐻
𝐻
c
h
(
𝐴
)
:
=
Tot
⁡
(
⨁
𝑝
≥
0
𝐶
𝐻
c
h
𝑝
,
∙
(
𝐴
)
[
−
𝑝
]
)
.
RHH
ch
	​

(A):=Tot(
p≥0
⨁
	​

CH
ch
p,∙
	​

(A)[−p]).

The geometry of configuration spaces supplies a Verdier duality shift by
𝑝
+
2
p+2 at bar degree
𝑝
p. Koszul concentration means that only the diagonal
𝑝
=
𝑞
p=q survives. Therefore the variable shift
𝑝
+
2
p+2 collapses to a uniform residual shift by
2
2.

That is the missing bookkeeping sentence the current manuscript keeps compressing.

Theorem H (Definitive Hochschild duality)

For every chiral Koszul datum
𝐴
A with dual
𝐴
!
A
!
,

𝑅
𝐻
𝐻
c
h
(
𝐴
)
≃
𝑅
 ⁣
Hom
⁡
 ⁣
(
𝑅
𝐻
𝐻
c
h
(
𝐴
!
)
,
 
𝜔
𝑋
[
2
]
)
.
RHH
ch
	​

(A)≃RHom(RHH
ch
	​

(A
!
),ω
X
	​

[2]).
Corollary H.1

Taking cohomology yields

𝐻
𝐻
c
h
𝑛
(
𝐴
)
≅
𝐻
𝐻
c
h
2
−
𝑛
(
𝐴
!
)
∨
⊗
𝜔
𝑋
.
HH
ch
n
	​

(A)≅HH
ch
2−n
	​

(A
!
)
∨
⊗ω
X
	​

.
Corollary H.2

If one prefers same-degree notation, this is equivalent to the statement that the Hochschild object of
𝐴
A is the dual of the Hochschild object of
𝐴
!
A
!
 shifted by
[
2
]
[2].

This single theorem resolves the current cross-chapter contradiction.

Its essential characteristics are:

object-level before group-level,

bigraded before totalized,

Verdier shift
𝑝
+
2
p+2 plus diagonal concentration
𝑝
=
𝑞
p=q exactly explains the universal
2
2.

V. The modular characteristic theorem should be split into a hierarchy

The latest manuscript has already moved in the right direction: it now explicitly separates a scalar modular characteristic package from a full modular homotopy package, and says that constructing the cyclic
𝐿
∞
L
∞
	​

 deformation object and solving the MC equation is the principal open problem. It also states Theorem D as a theorem about the scalar package determined by
𝜅
(
𝐴
)
κ(A). That is the correct direction. It should now be made logically precise.

Definition 8 (Scalar modular characteristic system)

The scalar modular characteristic system of
𝐴
A is

𝑆
0
(
𝐴
)
:
=
(
𝜅
(
𝐴
)
,
{
o
b
s
𝑔
(
𝐴
)
}
𝑔
≥
1
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
)
,
S
0
	​

(A):=(κ(A),{obs
g
	​

(A)}
g≥1
	​

,{F
g
	​

(A)}
g≥1
	​

),

with

o
b
s
𝑔
(
𝐴
)
∈
𝐻
2
𝑔
(
𝑀
𝑔
)
,
𝐹
𝑔
(
𝐴
)
∈
𝐶
.
obs
g
	​

(A)∈H
2g
(M
g
	​

),F
g
	​

(A)∈C.
Definition 9 (Spectral characteristic)

The spectral characteristic is the polynomial/discriminant invariant

Δ
𝐴
(
𝑥
)
.
Δ
A
	​

(x).
Definition 10 (Full modular homotopy package)

The full modular homotopy package is

𝑀
(
𝐴
)
:
=
(
𝑆
0
(
𝐴
)
,
Δ
𝐴
(
𝑥
)
,
𝐻
𝐴
,
Θ
𝐴
)
,
M(A):=(S
0
	​

(A),Δ
A
	​

(x),H
A
	​

,Θ
A
	​

),

where

𝐻
𝐴
:
=
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
,
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
𝑔
,
∙
,
𝑄
)
)
H
A
	​

:=RΓ(M
g
	​

,Z
A
	​

),Θ
A
	​

∈MC(Def
cyc
	​

(A)
⊗
	​

RΓ(M
g,∙
	​

,Q))

is conjectural at present.

Theorem D
s
c
a
l
a
r
scalar
	​


For every modular Koszul object in the theorematic sense,

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
,
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
obs
g
	​

(A)=κ(A)λ
g
	​

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

and
𝜅
κ is additive under tensor product and anti-symmetric under Koszul duality.

Theorem D
Δ
Δ
	​


The spectral discriminant
Δ
𝐴
(
𝑥
)
Δ
A
	​

(x) is invariant under the explicitly proved duality operations (for example, Koszul duality / DS reduction in the regimes where the manuscript proves this).

Conjecture
Θ
Θ

There exists a cyclic
𝐿
∞
L
∞
	​

-algebra
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

(A) and a universal Maurer–Cartan element
Θ
𝐴
Θ
A
	​

 whose:

trace recovers
𝜅
(
𝐴
)
𝜆
𝑔
κ(A)λ
g
	​

,

clutching compatibility recovers sewing,

Verdier duality recovers complementarity.

The essential characteristic of this hierarchy is:

scalar data are proved,

spectral/polynomial data are proved but not scalar,

full MC data are conjectural.

This resolves the status drift without weakening the vision.

VI. The conjectures collapse to a small number of master conjectures

To “resolve everything” one should not try to treat 90+ conjectures separately. The manuscript itself already says that the single obstruction to unconditional modular Koszulity of the standard interacting families is higher-genus PBW degeneration, and that the principal open problem of the modular programme is the construction of the cyclic
𝐿
∞
L
∞
	​

 deformation object and universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

. That means the conjectural layer should be rewritten as five master conjectures.

Master Conjecture 1 (Higher-genus PBW degeneration)

For generic affine Kac–Moody, generic Virasoro, and generic
𝑊
𝑁
W
N
	​

, the genus-
𝑔
g PBW spectral sequence degenerates at
𝐸
2
E
2
	​

 for all
𝑔
≥
1
g≥1.

This is exactly the missing hypothesis needed to pass from modular pre-Koszulity to actual modular Koszulity for the standard interacting families.

Master Conjecture 2 (Cyclic
𝐿
∞
L
∞
	​

 deformation algebra and universal
Θ
𝐴
Θ
A
	​

)

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

-algebra and solve the completed Maurer–Cartan equation to obtain
Θ
𝐴
Θ
A
	​

.

This is the genuine foundational conjecture of the modular programme.

Master Conjecture 3 (Full factorization-categorical DK/KL extension)

The chain/evaluation-locus theorems should extend to the full factorization-categorical regime.

Master Conjecture 4 (Completed bar theory for infinite-generator duals)

Needed for
𝑊
∞
W
∞
	​

, Yangian towers, and other infinite-generator cases.

Master Conjecture 5 (BV/BRST/bar identification)

This is the mathematical-physics bridge. It should be downstream of 1–4, not placed on the same logical level.

Once these five are isolated, the rest of the conjectural zoo becomes tractable.

VII. Essential characteristics of the corrected theory

The repaired theory has the following essential features.

1. Antecedent hypotheses, not conclusion-bearing definitions

No definition should contain:

bar–cobar inversion,

complementarity,

or the existence of the universal MC class,
unless those are already proved in the relevant category.

2. Construction vs resolution

For every augmented chiral algebra:

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

(A) exists,

Ω
𝑋
(
𝐶
)
Ω
X
	​

(C) exists.
But resolution is equivalent to the Koszulity of a twisting morphism, not automatic.

3. Chain level before cohomology level

Verdier duality, complementarity, and Hochschild duality should first be stated at the level of complexes/derived objects. Cohomology-level formulas are corollaries.

4. Curved fiberwise differential vs strict total differential

The curved equation

(
𝑑
(
𝑔
)
f
i
b
)
2
=
𝑚
0
(
𝑔
)
(d
(g)
fib
	​

)
2
=m
0
(g)
	​


and the strict equation

𝐷
𝐴
2
=
0
D
A
2
	​

=0

must coexist and must never again be denoted by the same symbol. The latest abstract already suggests exactly this split.

5. Scalar/spectral/full characteristic hierarchy

𝜅
κ is the first characteristic number,
Δ
𝐴
Δ
A
	​

 is the first genuinely non-scalar characteristic class, and
Θ
𝐴
Θ
A
	​

 is the conjectural universal object.

6. The homotopy form is the correct foundational layer

The latest manuscript’s homotopy-native definition is already much closer to the correct mathematics than the current dg-model axiomatization. The cure is to make that homotopy layer foundational and make the dg model an explicit presentation of it, not the other way around.
