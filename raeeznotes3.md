The right edit is not “make the proofs more abstract.” It is: choose one semantic level for the whole book, and force every theorem, definition, and conjecture to live there first. The manuscript already points to the correct ambient language: factorization algebras on
R
a
n
(
𝑋
)
Ran(X), bar–cobar as an adjunction there, coderived persistence off the Koszul locus, complementarity as a shifted-symplectic/Lagrangian statement, and a universal Maurer–Cartan class as the missing global control object.

What you need now is a uniform homotopy-native editing policy. That will do three things at once:

eliminate the present drift between cohomology statements, chain models, and conjectural homotopy structures;

make the formalism consistent across genus, curvature, and duality;

shorten many proofs, because the proofs will become instances of a few universal lemmas instead of repeated chain-level manipulations.

The shortest formulation is this:

Master edit: every statement must appear in three synchronized layers

Add a front-matter section called something like:

“Semantic conventions: homotopy objects, dg models, and cohomological shadows”

From that point on, every major object and theorem has three versions:

H-level (homotopy/native): the statement in a stable
∞
∞-category / formal moduli problem / shifted-symplectic language.

M-level (model): an explicit dg /
𝐿
∞
L
∞
	​

 / filtered complex presentation.

S-level (shadow): the cohomology, Ext, numerical, or generating-function consequence.

Then impose these notation rules globally:

≃
≃: equivalence in the homotopy/
∞
∞-categorical sense.

≅
≅: strict isomorphism of chosen models.

=
=: definition or literal equality only.

This is the single most important edit, because the current manuscript already mixes these three levels. Its central object is stated as a modular Koszul chiral algebra on
R
a
n
(
𝑋
)
Ran(X) with a universal Maurer–Cartan class, but the current definition and many proofs are still expressed at the level of chosen complexes, while the scalar theorem is already only the shadow of the conjectural full object.

Once you adopt this H/M/S discipline, the rest becomes systematic.

Edit 1: make the ambient category homotopy-native from the beginning

Right now the manuscript already says the natural home is

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


on
R
a
n
(
𝑋
)
Ran(X), and that off the Koszul locus the correct ambient category is coderived, not ordinary derived.

So the correct edit is:

Replace “the bar complex of
𝐴
A” by two objects

𝐵
𝑋
(
𝐴
)
B
X
	​

(A): the bar object in the stable homotopy category / dg nerve of factorization coalgebras.

𝐵
𝑋
(
𝐴
)
B
X
	​

(A): a chosen explicit dg model.

Do the same for cobar, center, deformation complexes, and genus towers:

𝛺
𝑋
Ω
X
	​

,
Ω
𝑋
Ω
X
	​


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
𝐶
𝑔
(
𝐴
)
C
g
	​

(A)

𝐷
𝑒
𝑓
c
y
c
(
𝐴
)
Def
cyc
	​

(A),
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

(A)

This makes the chain model subordinate to the homotopy object, instead of the reverse.

Why this matters

Then Theorem A is automatically an equivalence of homotopy objects, and every chain-level formula becomes a presentation of that equivalence rather than the theorem itself.

Elementary presentation

Do not force readers into full
∞
∞-categorical abstraction immediately. Present each
𝑋
X by a concrete dg model and state one lemma:

Any two admissible dg presentations of the same factorization object are connected by a contractible space of quasi-isomorphisms.

That gives the constructive version of “beyond chain level.”

Edit 2: rewrite Definition 8.17.7 in homotopy language

The current definition of modular Koszul chiral algebra packages D1–D3 and axioms MK1–MK5, but MK3 is still phrased as a quasi-isomorphism of explicit bar–cobar complexes, MK4 as diagonal Ext vanishing, and MK5 as a decomposition on
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

,Z(A)).

The correct replacement is:

Definition (homotopy form)

A modular Koszul object on
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

(Fact(X)) together with

a bar object
𝐵
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

a filtered cyclic deformation object
𝐷
𝑒
𝑓
c
y
c
(
𝐴
)
Def
cyc
	​

(A);

a genus-completed deformation datum
Θ
𝐴
Θ
A
	​

 when constructed, or its scalar shadow when only that is proved;

such that:

MK1
∞
∞
	​

: the weight filtration makes
𝐵
𝑋
(
𝐴
)
B
X
	​

(A) Koszul on the associated graded.

MK2
∞
∞
	​

:

𝐷
R
a
n
𝐵
𝑋
(
𝐴
)
≃
𝐵
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
X
	​

(A)≃B
X
	​

(A
!
).

MK3
∞
∞
	​

:

𝛺
𝑋
𝐵
𝑋
(
𝐴
)
≃
𝐴
Ω
X
	​

B
X
	​

(A)≃A

on the Koszul locus.

MK4
∞
∞
	​

: the genus tower comes from a filtered Maurer–Cartan deformation of
𝐵
𝑋
(
𝐴
)
B
X
	​

(A).

MK5
∞
∞
	​

: the complementarity complex is defined before passing to cohomology, and its homotopy eigenspaces are Lagrangian.

Why this is better

It makes MK4 and MK5 genuinely homotopical, instead of shadows of homotopical facts.

Elementary presentation

Immediately after the abstract definition, keep the present D1–D3/MK1–MK5 as a subsection titled:

“Concrete dg model of the above definition.”

That preserves elementary accessibility.

Edit 3: separate the three differentials permanently

This is the most urgent local repair.

You need three symbols, used everywhere:

𝑑
(
𝑔
)
c
u
r
v
(fixed-genus curved differential)
,
d
(g)
curv
	​

(fixed-genus curved differential),
𝐷
t
o
t
(total genus-completed differential)
,
D
tot
(total genus-completed differential),
𝑚
0
(
𝑔
)
(curvature term)
.
m
0
(g)
	​

(curvature term).

Then impose:

(
𝑑
(
𝑔
)
c
u
r
v
)
2
=
𝑚
0
(
𝑔
)
,
(
𝐷
t
o
t
)
2
=
0.
(d
(g)
curv
	​

)
2
=m
0
(g)
	​

,(D
tot
)
2
=0.

This resolves the current instability where one part of the manuscript speaks about genus-
𝑔
g curvature, another about a quantum-corrected
𝑑
𝑔
d
g
	​

 with square zero, and yet another about strict nilpotence in central-curvature examples. The book already has the ingredients to support a homotopy-level resolution: it explicitly treats curvature as the
𝑚
0
(
𝑔
)
m
0
(g)
	​

 term of a modular Maurer–Cartan deformation, while also treating the total structure as a single Maurer–Cartan deformation of genus-zero bar data.

The clean conceptual fix

Define
𝐷
t
o
t
D
tot
 from the full Maurer–Cartan element
Θ
𝐴
Θ
A
	​

. Then the fixed-genus curved differential is the projection of
𝐷
t
o
t
D
tot
 to the genus-
𝑔
g summand. The two square relations then become the same Maurer–Cartan equation seen globally and weightwise.

That one edit will make a large number of current proofs much cleaner.

Edit 4: make complementarity homotopy-first, not cohomology-first

The manuscript already essentially does this in Theorem 8.13.26: it lifts complementarity from cohomology to the cochain complex
𝐶
𝑔
:
=
𝑅
Γ
(
𝑀
𝑔
,
𝑍
(
𝐴
)
)
C
g
	​

:=RΓ(M
g
	​

,Z(A)), defines homotopy eigenspaces, and proves they are Lagrangian subcomplexes whose sum recovers
𝐶
𝑔
C
g
	​

 up to quasi-isomorphism.

So the correct edit is to promote this to the primary definition:

Replace
𝑄
𝑔
(
𝐴
)
=
ker
⁡
(
𝜎
−
i
d
)
⊂
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
Q
g
	​

(A)=ker(σ−id)⊂H
∗
(M
g
	​

,Z(A))
By
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
−
i
d
:
𝐶
𝑔
→
𝐶
𝑔
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
+
i
d
:
𝐶
𝑔
→
𝐶
𝑔
)
.
Q
g
	​

(A):=fib(σ−id:C
g
	​

→C
g
	​

),Q
g
	​

(A
!
):=fib(σ+id:C
g
	​

→C
g
	​

).

Then define the old objects as shadows:

𝑄
𝑔
(
𝐴
)
:
=
𝐻
∗
(
𝑄
𝑔
(
𝐴
)
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
Q
g
	​

(A):=H
∗
(Q
g
	​

(A)),Q
g
	​

(A
!
):=H
∗
(Q
g
	​

(A
!
)).
Why this matters

Then Theorem C is a theorem in the stable homotopy category:

𝐶
𝑔
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
,
C
g
	​

≃Q
g
	​

(A)⊕Q
g
	​

(A
!
),

with each summand Lagrangian for the relevant shifted symplectic form.

The proof becomes elegant:

build
𝜎
σ on
𝐶
𝑔
C
g
	​

,

take homotopy eigenspaces,

apply the standard lemma that an involution splits a complex into homotopy eigenspaces in characteristic
0
0,

apply the constant-pairing criterion for linear shifted symplectic spaces.

The manuscript is already using exactly this logic in its chain-level and PTVV refinements.

Edit 5: split the modular characteristic package into “proved scalar shadow” and “full homotopy package”

At present the manuscript correctly says that the first three parts of the modular characteristic package are established, while the full non-scalar
Θ
𝐴
Θ
A
	​

 remains conjectural in its full form. It also states in Chapter 34 exactly what is still missing: the cyclic deformation complex as a cyclic
𝐿
∞
L
∞
	​

-algebra and a Maurer–Cartan solution in the completed tensor product with tautological classes.

So the correct edit is:

Introduce two definitions

Scalar modular characteristic package

(
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
)
(κ(A),{F
g
	​

(A)}
g≥1
	​

,Δ
A
	​

)

— proved.

Full modular homotopy package

(
Θ
𝐴
,
𝐶
𝑔
(
𝐴
)
,
Δ
𝐴
,
trace
,
clutching
,
Verdier duality
)
(Θ
A
	​

,C
g
	​

(A),Δ
A
	​

,trace,clutching,Verdier duality)

— partially proved / partially conjectural.

Then rewrite Theorem D

Do not say “Theorem D proves the package.” Say:

Theorem D proves the scalar shadow of the modular package, and identifies it as the first characteristic shadow of the conjectural full Maurer–Cartan class.

That aligns the introduction with the actual state of the book.

Edit 6: construct the cyclic
𝐿
∞
L
∞
	​

 deformation object earlier, even in provisional form

The manuscript already says the full theory wants a universal class

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

and that this is the real object behind curvature, obstruction sheaves, and scalar traces.

So the correct edit is:

Add a Part I subsection:

“Cyclic deformation complex and its elementary models”

In it, do the following.

Define
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

(A) abstractly as the tangent dg Lie /
𝐿
∞
L
∞
	​

 algebra of cyclic deformations of
𝐴
A.

For the concrete examples, build explicit models from:

bar coderivations,

cyclic Hochschild complexes,

stable-graph operations.

Even if the full general construction remains conjectural, you can still make the object part of the book’s formal vocabulary. Then all higher-genus constructions are phrased as “induced by
Θ
𝐴
Θ
A
	​

” rather than as disconnected formulas.

Proof benefit

Many later statements then become tautological consequences of the Maurer–Cartan equation instead of ad hoc induction arguments.

Edit 7: add a constructive coderived model now, not only as future work

The manuscript says clearly that the natural off-Koszul home is coderived and that the full factorization-algebra coderived formalism is not yet developed.

That is fine as a long-range statement, but for the present book you should add a minimal constructive replacement:

New appendix:

“Relative curved models adequate for the present monograph”

Define a relative dg category whose:

objects are filtered curved factorization models appearing in the book,

weak equivalences are filtered morphisms inducing equivalences on the associated graded or on the coacyclic quotient,

homotopy category is the provisional coderived category used in the proofs.

This is not the final theory, but it is enough to make every off-Koszul statement mathematically honest now.

Why this helps

Then Theorem B off the Koszul locus becomes a theorem in an actual relative homotopy category, not a promise of future interpretation.

Edit 8: rewrite Theorems A–D in homotopy-first form

The introduction already presents A–D as the four aspects of one object, and §34.10 already organizes the programme in homotopy-native language.

Now make the theorem statements match that.

Theorem A

Primary statement:

𝐷
R
a
n
𝐵
𝑋
(
𝐴
)
≃
𝐵
𝑋
(
𝐴
!
)
D
Ran
	​

B
X
	​

(A)≃B
X
	​

(A
!
)

in the homotopy category of factorization coalgebras.
Secondary model statement: explicit configuration-space dg models realize this equivalence.

Theorem B

Primary statement:

𝛺
𝑋
𝐵
𝑋
(
𝐴
)
≃
𝐴
Ω
X
	​

B
X
	​

(A)≃A

on the Koszul locus in
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
Alg
aug
	​

(Fact(X)), and in the provisional coderived category off it.
Model statement: counit map of dg models is a quasi-isomorphism/curved equivalence.

Theorem C

Primary statement:

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

with each summand Lagrangian.
Shadow statement: cohomology decomposes accordingly.

Theorem D

Primary statement:
there is a trace map from the deformation object to the tautological ring, and its scalar component is controlled by
𝜅
(
𝐴
)
κ(A).
Shadow statement:
𝜅
κ governs the scalar genus tower.

This will make the proofs far more uniform.

Edit 9: fix the parameter-source problem by adding one diagram

You need one universal diagram that is referenced everywhere higher genus appears:

𝐻
1
(
Σ
𝑔
)
⟶
𝑍
1
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
m
o
d
e
l
)
⟶
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
⟶
t
r
𝑅
Γ
(
𝑀
‾
𝑔
,
𝑄
)
.
H
1
(Σ
g
	​

)⟶Z
1
(Def
cyc
	​

(A)
model
	​

)⟶RΓ(M
g
	​

,Z
A
	​

)
⟶
tr
	​

RΓ(
M
g
	​

,Q).

Interpretation:

the fiber-period parameters live in
𝐻
1
(
Σ
𝑔
)
H
1
(Σ
g
	​

);

the moduli obstruction classes live in
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

the scalar obstruction shadows live in tautological cohomology.

That one diagram prevents the recurring confusion between “parameters from the curve” and “classes on moduli.”

Edit 10: every conjecture should be rewritten into one of seven homotopy templates

This is how you cover “each and every conjecture” without chaos.

Type I: existence of a homotopy object

Example: universal Maurer–Cartan class.

Correct form:

There exists a filtered cyclic
𝐿
∞
L
∞
	​

 algebra
𝐷
𝑒
𝑓
c
y
c
(
𝐴
)
Def
cyc
	​

(A) and an MC element
Θ
𝐴
Θ
A
	​

 with trace, clutching, and Verdier-duality compatibility.

Type II: equivalence of homotopy categories

Examples: full coderived bar–cobar, full DK.

Correct form:

There is an equivalence in a stable/E
1
1
	​

-monoidal
∞
∞-category; current chain models give a presentation on a dense sublocus.

Type III: shifted-symplectic/Lagrangian enhancement

Examples: complementarity upgrades.

Correct form:

A pairing already constructed on the model level upgrades to an
𝑛
n-shifted symplectic structure on the associated linear derived object/formal moduli problem.

Type IV: trace/index statements

Examples: genus generating series, GRR,
𝐴
^
A
-genus.

Correct form:

The scalar invariant is the image of the universal deformation object under a trace/pushforward functor.

Type V: periodicity statements

Do not formulate these first as statements about scalar periods.
Formulate them as:

existence of a finite homotopy action / graded autoequivalence / periodic filtration operator on a homotopy object.
Only then take numerical shadows.

Type VI: infinite-generator/completed dualities

Correct form:

the duality lives in a pro-/completed category; finite-stage truncations converge to the desired object.

Type VII: physics-dictionary conjectures

Examples: BRST/bar, BV/bar-cobar, BPHZ/
𝐴
∞
A
∞
	​

, path integral.

Correct form:

the relevant dg Lie or
𝐿
∞
L
∞
	​

 algebras controlling the two deformation problems are quasi-isomorphic.

This single rewrite policy will clean up the conjecture ecosystem dramatically.

Edit 11: present every proof by the same three-step method

To make proofs elegant, enforce this proof architecture everywhere:

Step A: abstract homotopy lemma

Prove the result in the stable
∞
∞-category / formal moduli problem.

Step B: explicit dg model

Choose the configuration-space, bar-complex, BRST, or deformation-complex model.

Step C: shadow corollary

Extract the cohomology, spectral sequence, or generating-function statement.

The manuscript already has the ingredients for this pattern:

Theorem A is naturally an adjunction/equivalence on
R
a
n
(
𝑋
)
Ran(X).

Theorem B is already phrased as derived vs coderived depending on the locus.

Theorem C is already lifted to chain level and to shifted symplectic geometry.

Theorem D already distinguishes scalar theorem from full MC object.

So the book is ready for this uniform proof architecture.

Edit 12: add an “elementary model presentation” after every major theorem

Because you want constructive, elementary access, do not leave the homotopy version alone. After each theorem, add a fixed-format subsection:

“Elementary model presentation”

chosen dg model;

explicit formula for the differential or pairing;

one-page proof in that model;

explanation of which homotopy object it presents.

For example:

after Theorem C, show

𝑄
𝑔
(
𝐴
)
=
f
i
b
(
𝜎
−
i
d
)
Q
g
	​

(A)=fib(σ−id)

is modeled by the cone of
𝜎
−
i
d
σ−id shifted by
−
1
−1;

after the shifted symplectic theorem, show the constant pairing on a cochain complex gives a linear derived affine scheme with the required shifted form;

after the universal MC conjecture, show what the stable-graph formulas would be in the Heisenberg and free-field cases.

That will make the book both more rigorous and more readable.

If you want elegant proofs of all existing statements, make these five edits first

Semantic conventions chapter: H/M/S levels, notation, equivalence conventions.

Differential split:
𝑑
(
𝑔
)
c
u
r
v
d
(g)
curv
	​

,
𝐷
t
o
t
D
tot
,
𝑚
0
(
𝑔
)
m
0
(g)
	​

.

Homotopy-first complementarity: define deformation/obstruction complexes as homotopy eigenspaces, cohomology spaces as shadows.

Scalar vs full modular package: separate Theorem D from Conjecture
Θ
𝐴
Θ
A
	​

.

Minimal coderived appendix: enough relative homotopy theory to make off-Koszul statements mathematically honest now.

If you make those five edits, the whole project will start reading as one coherent homotopy theory instead of a mixture of chain calculations, cohomological shadows, and horizon statements.

The deepest reason this is the right path is that the manuscript itself already says the true object is a modular Koszul chiral algebra on
R
a
n
(
𝑋
)
Ran(X), controlled by a universal Maurer–Cartan deformation, with bar–cobar, coderived persistence, and shifted-symplectic complementarity as its natural manifestations. The correct edits are the ones that force the text to actually live where its best mathematics already lives.
