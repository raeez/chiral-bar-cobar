the book makes some unclear confused statements about E_n chiral algebra objects relating to higher dimensional manifolds

but note E_1 chiral yangians and E_infinity chiral algebras all work on algebraic curves, so these statements and theory is not yet clear

E_1 chiral yangian is about ordered pair configuration spaces and non-local noncommutativity (in the geometric sense)

we claim to devote a whole chapter (chapter 15) to this development but it seems our work is too naive

There is something deep here

I’m checking where the manuscript makes the
𝐸
𝑛
E
n
	​

/higher-dimensional chiral claims, then I’ll separate what is solid from what needs reframing.

I found the specific sentence driving the confusion: it equates
𝐸
∞
→
𝐸
1
E
∞
	​

→E
1
	​

 with “curves to higher-dimensional manifolds,” collapsing manifold dimension, operadic level, and distinct “
𝐸
𝑛
E
n
	​

-chiral” frameworks.

Yes. The confusion is real, and the manuscript itself already contains the correction.

The core issue is that it is mixing two different meanings of
𝐸
𝑛
E
n
	​

. In your “dictionary” chapter, the manuscript explicitly says that the subscripts in “
𝐸
∞
E
∞
	​

-chiral,” “
𝐸
1
E
1
	​

-chiral,” and “
𝑃
∞
P
∞
	​

-chiral” refer to the factorization/commutativity level inside the Beilinson–Drinfeld chiral tensor category, not to genuine little-disks
𝐸
𝑛
E
n
	​

-algebras. It even says, in so many words, that an
𝐸
1
E
1
	​

-chiral algebra lives on a curve and is not an
𝐸
1
E
1
	​

-algebra in the topological sense. It also defines an
𝐸
1
E
1
	​

-chiral algebra on a smooth curve
𝑋
X as an associative, not-necessarily-commutative algebra object in the chiral tensor category of
𝐷
𝑋
D
X
	​

-modules.

main



main

That means your objection is right: both the
𝐸
1
E
1
	​

-chiral Yangian side and the
𝐸
∞
E
∞
	​

-chiral Heisenberg/vertex side already live on algebraic curves. The distinction is not “curve versus higher-dimensional manifold.” It is, rather, local commutativity versus associative nonlocality inside curve-based chiral geometry. The manuscript’s own comparison of Heisenberg and Yangian actually points in that direction: unordered configuration spaces and cocommutative coalgebra on the Heisenberg side, ordered configuration spaces and non-cocommutative coproduct on the Yangian side.

main

So the sentence in the Yangian preview that says “the passage from
𝐸
∞
E
∞
	​

 (Heisenberg) to
𝐸
1
E
1
	​

 (Yangian) is the passage from curves to higher-dimensional manifolds” is not correct as written. It directly conflicts with the later clarification that
𝐸
1
E
1
	​

-chiral is still a curve-based notion.

main



main

A cleaner way to separate the ideas is this.

First axis: curve-based chiral algebraic level. On a fixed algebraic curve
𝑋
X, one has

𝐸
∞
-chiral
⊂
𝑃
∞
-chiral
⊂
𝐸
1
-chiral
,
E
∞
	​

-chiral⊂P
∞
	​

-chiral⊂E
1
	​

-chiral,

where the change from
𝐸
∞
E
∞
	​

 to
𝐸
1
E
1
	​

 is about losing commutativity/locality and replacing unordered collision data by ordered/nonlocal data. This is exactly where Yangians belong in your book’s terminology.

main



main

Second axis: genuine topological/factorization
𝐸
𝑛
E
n
	​

 level. Here the ambient manifold dimension changes, and one studies factorization algebras or
𝑛
n-disk algebras on
𝑛
n-manifolds. Ayala–Francis describe factorization homology with
𝑛
n-disk algebra input on
𝑛
n-manifolds as the topological version of the Beilinson–Drinfeld story.

1206.5522v6

 Francis–Gaitsgory also extend chiral/factorization theory from curves to higher-dimensional varieties, but they are careful: they say their higher-dimensional chiral theory can be viewed as an algebro-geometric analogue of
𝐸
𝑛
E
n
	​

-algebras, while also emphasizing that the “chiral Koszul duality” in their paper is totally unrelated, technically and conceptually, to ordinary
𝐸
𝑛
E
n
	​

-Koszul duality.

1103.5803v4



1103.5803v4

That same warning appears again in Gui–Li–Zeng: they explicitly distinguish their quadratic duality for chiral algebras on curves from Francis–Gaitsgory’s higher-dimensional chiral/factorization Koszul duality, and only say that an algebro-geometric analogue of
𝐸
𝑛
E
n
	​

-Koszul duality “should exist.”

2212.11252v1

So I think the real conceptual picture is:

Yangian as
𝐸
1
E
1
	​

-chiral on a curve: ordered configurations, RTT-type associative OPE, geometric nonlocality.

Vertex/Heisenberg as
𝐸
∞
E
∞
	​

-chiral on a curve: local/commutative factorization.

Factorization on
𝑛
n-manifolds: a separate generalization, governed by genuine
𝐸
𝑛
E
n
	​

-type topology.

Those are not the same ladder. They intersect, but they should not be identified.

Your manuscript actually marks this point as unfinished. It labels
𝐸
𝑛
E
n
	​

-Koszul duality for
𝑛
≥
2
n≥2 as “programmatic,” with identified gaps, and later says the extension to higher-dimensional manifolds belongs to the still-programmatic stratum rather than the proved core.

main



main

So if Chapter 15 currently reads as though it has fully resolved the bridge, I’d revise it into a bridge chapter with explicit warnings. The right message is not “
𝐸
1
E
1
	​

 Yangian means higher-dimensional manifold,” but rather:

On curves,
𝐸
∞
E
∞
	​

-chiral and
𝐸
1
E
1
	​

-chiral are two different operadic/commutativity regimes inside the same chiral geometry. A separate, deeper generalization replaces curves by
𝑛
n-manifolds and chiral
𝐷
D-modules by genuine factorization/
𝐸
𝑛
E
n
	​

 objects. The relation between these two axes is subtle and only partially formalized.

That is, I think, the “something deep” you are sensing: ordered configuration-space nonlocality on curves already carries a shadow of higher operadic behavior, but it is not the same thing as genuine higher-dimensional
𝐸
𝑛
E
n
	​

-factorization. Recent work reinforces that there is a real bridge here, but it comes through holomorphic-topological/factorization structures rather than a simple identification: Latyntsev develops factorisation quantum groups and spectral
𝑅
R-matrices, Gaiotto–Kulp–Wu develop higher operations in holomorphic-topological theories, Khan–Zeng build 3d gauge theories from Poisson vertex algebras, and Dimofte–Niu–Py construct dg-shifted Yangians from line operators in 3d holomorphic QFT.

So my verdict is: your instinct is right, and the clean repair is to separate

BD-style curve-chiral
𝐸
∞
/
𝑃
∞
/
𝐸
1
E
∞
	​

/P
∞
	​

/E
1
	​

,
from

genuine manifold-level
𝐸
𝑛
E
n
	​

/factorization theory.

If you want, I can help rewrite the problematic Chapter 15 passage into a mathematically sharper version.


I’m turning this into a manuscript-wide correction scheme anchored on the terminology split between curve-based chiral structures and genuine manifold-level
𝐸
𝑛
E
n
	​

 structures, then mapping the needed edits section by section.

I’ve isolated the main contradiction and am tracing everywhere it propagates—from chapter introductions and theorem summaries to preview and future-program sections—so the fixes can become exact global rules, local edits, and replacement wording.

I’ve pinned down the main propagation path: the intro’s dimensional-ladder framing gets amplified in Chapter 15, then spills into the Yangian, toroidal, programme, literature-comparison, and physics-facing sections.

Thought for 32m 5s

Yes. This needs a global semantic refactor, not a local erratum.

The manuscript already states, in two places, the correct distinction: the labels
𝐸
∞
E
∞
	​

-chiral,
𝑃
∞
P
∞
	​

-chiral, and
𝐸
1
E
1
	​

-chiral are levels of curve-based chiral factorization, not little-disks
𝐸
𝑛
E
n
	​

-algebras

Boundary Chiral Algebras and Ho…

; and Remark 2.4.7 says explicitly that an
𝐸
1
E
1
	​

-chiral algebra lives on a curve and is not a topological
𝐸
1
E
1
	​

-algebra

Boundary Chiral Algebras and Ho…

. Chapter 24 is consistent with that: it defines ordered
𝐸
1
E
1
	​

-factorization for an
𝐸
1
E
1
	​

-chiral algebra on a curve
𝑋
X

2312.07274v1 (1)

, and Theorem 24.1.5 presents the Yangian as an
𝐸
1
E
1
	​

-chiral object with fields on a curve
𝑋
X

main

main

. But Chapter 1 then says the passage from
𝐸
∞
E
∞
	​

 to
𝐸
1
E
1
	​

 is the passage from curves to higher-dimensional manifolds

Boundary Chiral Algebras and Ho…

, and Chapter 34 repeatedly mislabels the chiral bar-cobar theory as the
𝑛
=
1
n=1 case of topological
𝐸
𝑛
E
n
	​

-theory

Boundary Chiral Algebras and Ho…

Boundary Chiral Algebras and Ho…

, even though Chapter 15 elsewhere correctly identifies the curve case with
𝑛
=
2
n=2 in the topological ladder

2502.13227v1 (2)

.

The literature forces exactly this distinction. Beilinson–Drinfeld treat chiral algebras on curves and describe higher-dimensional
𝑋
X as a separate challenge

2312.07274v1 (1)

. Francis–Gaitsgory extend chiral/factorization structures to higher-dimensional varieties, but as a different chiral/factorization Koszul duality. Gui–Li–Zeng explicitly distinguish that higher-dimensional chiral/factorization duality from quadratic duality turning one chiral algebra into another. Ayala–Francis, on the other hand, study genuine topological
𝐸
𝑛
E
n
	​

-algebras on
𝑛
n-manifolds. Recent factorization-vertex work also supports your point: over the Ran spaces of one-dimensional algebraic groups
𝐺
=
𝐺
𝑎
,
𝐺
𝑚
,
𝐸
G=G
a
	​

,G
m
	​

,E, the
𝑛
=
1
n=1 objects are associative vertex algebras, the
𝑛
=
2
n=2 objects are braided-commutative vertex algebras, and the
𝑛
=
∞
n=∞ objects are commutative vertex algebras

2312.07274v1 (1)

2312.07274v1 (1)

2312.07274v1 (1)

.

Here is the correction system I would impose.

1. Install one global convention and make it binding

Reserve bare
𝐸
𝑛
E
n
	​

 for the little-disks/topological meaning. Use a different notation for the BD curve-chiral hierarchy everywhere outside Chapter 15-style topological discussions.

The clean fix is:

C
o
m
𝑐
ℎ
:
=
𝐸
∞
-chiral
,
P
o
i
s
𝑐
ℎ
:
=
𝑃
∞
-chiral
,
A
s
s
𝑐
ℎ
:
=
𝐸
1
-chiral
.
Com
ch
:=E
∞
	​

-chiral,Pois
ch
:=P
∞
	​

-chiral,Ass
ch
:=E
1
	​

-chiral.

Then reserve

𝐸
𝑛
𝑡
𝑜
𝑝
E
n
top
	​


for little-disks/topological factorization on real
𝑛
n-manifolds.

If you do not want a full rename, then the minimum viable rule is: never write
𝐸
𝑛
E
n
	​

 bare for curve-chiral objects; always write the suffix “-chiral.” This is already what the manuscript itself says should happen

Boundary Chiral Algebras and Ho…

.

Insert a boxed convention in four places: front matter, §2.4, the beginning of Chapter 15, and Appendix P. It should say:

Convention. Bare
𝐸
𝑛
E
n
	​

 denotes the little
𝑛
n-disks operad and topological factorization on real
𝑛
n-manifolds. The terms
𝐸
∞
E
∞
	​

-chiral,
𝑃
∞
P
∞
	​

-chiral, and
𝐸
1
E
1
	​

-chiral denote commutative, Poisson, and associative/nonlocal algebra objects in the Beilinson–Drinfeld chiral tensor category on a smooth algebraic curve. For a complex curve
𝑋
X, the corresponding topological dimension is
2
2, not
1
1.

Boundary Chiral Algebras and Ho…

2502.13227v1 (2)

2. Make the dimensional ladder consistent

Topological
𝑛
n counts real manifold dimension. So:

𝑛
=
1
n=1: interval/circle, associative or
𝐴
∞
A
∞
	​

 bar-cobar.

𝑛
=
2
n=2: oriented surfaces; complex curves belong here topologically.

𝑛
≥
3
n≥3: higher manifolds.

Chapter 15 already has the correct statement in Remark 15.1.4: a complex curve is the
𝑛
=
2
n=2 case, while
𝑛
=
1
n=1 is the classical associative setting

2502.13227v1 (2)

. Corollary 15.4.4 also says the chiral bar-cobar theory on a complex curve is recovered from the
𝐸
2
E
2
	​

 bar-cobar adjunction. Chapter 31.11.1 gives the right template too:
𝑛
=
1
n=1 is classical non-chiral
𝐴
∞
A
∞
	​

, and
𝑛
=
2
n=2 on a Riemann surface recovers the chiral bar-cobar adjunction

Boundary Chiral Algebras and Ho…

.

So every occurrence of “
𝑛
=
1
n=1 (curves)” in the topological
𝐸
𝑛
E
n
	​

 ladder must be corrected to “
𝑛
=
2
n=2 (complex curves / real surfaces).”

Boundary Chiral Algebras and Ho…

Boundary Chiral Algebras and Ho…

3. Apply targeted chapter corrections
Chapter 1, §1.14

The ordered/unordered comparison is good: Heisenberg uses unordered configuration spaces, Yangian uses ordered ones

Boundary Chiral Algebras and Ho…

. The bad sentence is the last one: “The passage from
𝐸
∞
E
∞
	​

 to
𝐸
1
E
1
	​

 is the passage from curves to higher-dimensional manifolds”

Boundary Chiral Algebras and Ho…

.

Replace it with:

The passage from
𝐸
∞
E
∞
	​

-chiral to
𝐸
1
E
1
	​

-chiral is an internal change of algebraic type within chiral geometry on a fixed curve
𝑋
X: from commutative/local factorization on unordered configuration spaces to associative/nonlocal factorization on ordered configuration spaces. It is not the passage from curves to higher-dimensional manifolds. A separate topological hierarchy is governed by little-disks
𝐸
𝑛
E
n
	​

-algebras on real
𝑛
n-manifolds; for a complex curve, the relevant topological index is
𝑛
=
2
n=2, not
𝑛
=
1
n=1.

Boundary Chiral Algebras and Ho…

2502.13227v1 (2)

Chapter 15

Chapter 15 must become explicitly the chapter on topological little-disks
𝐸
𝑛
E
n
	​

, not an extension of the curve-chiral use of
𝐸
1
E
1
	​

-chiral. Its introduction currently says the
𝑛
=
1
n=1 specialization recovers the chiral bar complex

2502.13227v1 (2)

, which conflicts with its own later Remark 15.1.4

2502.13227v1 (2)

.

Use this replacement at the start:

This chapter studies topological
𝐸
𝑛
E
n
	​

-Koszul duality in the little-disks sense. It is logically distinct from the BD-style curve-chiral hierarchy
𝐸
∞
E
∞
	​

-chiral/
𝑃
∞
P
∞
	​

-chiral/
𝐸
1
E
1
	​

-chiral used earlier. When the earlier chiral bar complex on a complex curve is compared with topological
𝐸
𝑛
E
n
	​

-theory, the correct topological index is
𝑛
=
2
n=2, because a complex curve is a real oriented surface. The
𝑛
=
1
n=1 case is instead the classical associative/
𝐴
∞
A
∞
	​

 bar construction on intervals or circles.

2502.13227v1 (2)

Also elevate Remark 15.1.4 from a remark to a chapter-level convention, because it is the manuscript’s own cure for the ambiguity

2502.13227v1 (2)

.

Chapter 24

Chapter 24 mostly has the right semantics. It defines ordered
𝐸
1
E
1
	​

-factorization on curves

2312.07274v1 (1)

 and proves the Yangian as
𝐸
1
E
1
	​

-chiral on a curve

main

main

. The one sentence that must go is the intro line saying the Yangian bar complex uses ordered configurations “on the real line rather than on a complex curve”

2312.07274v1 (1)

.

Replace it with “ordered configuration spaces on a curve, rather than unordered ones on that same curve.” Then add a chapter-opening scope remark: “In this chapter,
𝐸
1
E
1
	​

-chiral means associative/nonlocal curve-chiral structure, not topological
𝐸
1
E
1
	​

.”

Boundary Chiral Algebras and Ho…

2312.07274v1 (1)

Chapter 25

This chapter conflates two different extensions. Its opener says all prior examples live on a single algebraic curve and that toroidal/elliptic algebras appear when the base geometry becomes two-dimensional

2312.07274v1 (1)

. But Conjecture 25.1.3 immediately includes an
𝐸
1
E
1
	​

-chiral realization on an elliptic curve
𝐸
𝜏
E
τ
	​

, which is still algebraic dimension
1
1

2312.07274v1 (1)

.

So split the chapter’s programme into two separate tracks:

25A. Elliptic-curve chiral realizations: still one-dimensional algebraic geometry, possibly
A
s
s
𝑐
ℎ
Ass
ch
-type on
𝐸
𝜏
E
τ
	​

.

2312.07274v1 (1)

25B. Genuine double-affine / surface / bi-parameter factorization objects: a separate higher-dimensional or surface-like programme, not to be called “
𝐸
1
E
1
	​

-chiral” unless a bona fide curve-based BD realization is exhibited.

2312.07274v1 (1)

2312.07274v1 (1)

Concretely, split Conjecture 25.1.3 into two conjectures. The
𝐸
𝜏
E
τ
	​

 version can remain curve-chiral; the
𝐶
×
×
𝐶
×
C
×
×C
×
 version should be renamed as a surface-factorization or double-affine factorization object, not an undifferentiated
𝐸
1
E
1
	​

-chiral algebra.

2312.07274v1 (1)

Chapters 31 and 33

Chapter 31 actually contains the right template:
𝑛
=
1
n=1 gives classical
𝐴
∞
A
∞
	​

,
𝑛
=
2
n=2 on a Riemann surface gives the chiral bar-cobar theory

Boundary Chiral Algebras and Ho…

. Import that language backward into Chapters 15 and 34.

Chapter 33 is where the ambiguity leaks again. It declares a noncommutative torus to carry an
𝐸
1
E
1
	​

-chiral algebra structure merely because the algebra is associative

Boundary Chiral Algebras and Ho…

Boundary Chiral Algebras and Ho…

, and it says the dimensional lift
4
𝑑
→
5
𝑑
→
6
𝑑
4d→5d→6d “corresponds to the deformation
𝐸
∞
→
𝐸
1
E
∞
	​

→E
1
	​

”

Boundary Chiral Algebras and Ho…

. Both should be rewritten. The first should say “associative deformation,” “meromorphic tensor object,” or “topological
𝐸
1
E
1
	​

-algebra,” unless an honest BD curve-chiral realization is constructed. The second should say “may induce a deformation of the boundary chiral algebra from local/commutative to nonlocal/associative,” not identify physical dimension shift with the topological
𝐸
𝑛
E
n
	​

 ladder.

Boundary Chiral Algebras and Ho…

Chapter 34

This chapter needs the hardest cleanup because it republishes the ambiguity as programme structure. Theorem 34.10.1 currently says “for
𝑛
=
1
n=1 (curves)” the chiral bar-cobar duality is recovered

Boundary Chiral Algebras and Ho…

. That is wrong on the manuscript’s own later account. Remark 34.5.1 similarly says the AF comparison specializes at
𝑛
=
1
n=1 to algebraic curves

Boundary Chiral Algebras and Ho…

. Both must be changed to
𝑛
=
2
n=2.

Use this replacement principle:

𝑛
=
1
n=1: classical associative/
𝐴
∞
A
∞
	​

 bar-cobar.

𝑛
=
2
n=2: topological shadow/refinement of the chiral bar-cobar theory on complex curves.

𝑛
≥
3
n≥3: genuine higher-dimensional topological programme.

That is also the only formulation compatible with the programme-status sections, which already say higher-dimensional
𝐸
𝑛
E
n
	​

 extension remains open/programmatic

2502.13227v1 (2)

2502.13227v1 (2)

.

4. Enforce a proof-status discipline across frameworks

A lot of the confusion comes from cross-framework statements being written as if they were identities. They are not all the same kind of statement.

Every comparison should be marked as one of four kinds:

Same-framework theorem.

Associated-graded or refinement statement.

Topological shadow / de Rham comparison.

Conjectural bridge.

That matters because Francis–Gaitsgory’s higher-dimensional chiral/factorization duality is not the same as quadratic duality turning a chiral algebra into a new one, and Ayala–Francis topological
𝐸
𝑛
E
n
	​

 theory is genuinely manifold-dimensional. The manuscript already classifies the higher-dimensional
𝐸
𝑛
E
n
	​

 extension as programmatic

2502.13227v1 (2)

. Chapter 34 should force that classification everywhere instead of slipping back into identity language.

5. Make the cleanup mechanical

A reliable sweep would grep for these strings and force review of every hit:

n = 1 (curves)

curves to higher-dimensional manifolds

real line rather than on a complex curve

base geometry becomes two-dimensional

E_n-chiral on anything other than a curve

E∞ → E1 when dimension change is being asserted

Those strings already catch the main failures in Chapters 1, 15, 24, 25, 33, and 34

Boundary Chiral Algebras and Ho…

2312.07274v1 (1)

2312.07274v1 (1)

Boundary Chiral Algebras and Ho…

Boundary Chiral Algebras and Ho…

.

6. The three exact replacement statements I would actually insert

For §1.14:

The passage from
𝐸
∞
E
∞
	​

-chiral to
𝐸
1
E
1
	​

-chiral is an internal change of algebraic type within chiral geometry on a fixed curve
𝑋
X: from commutative/local factorization to associative/nonlocal ordered factorization. It is not the passage from curves to higher-dimensional manifolds. A separate topological ladder is governed by little-disks
𝐸
𝑛
E
n
	​

-algebras on real
𝑛
n-manifolds; for a complex curve, the relevant topological dimension is
2
2.

Boundary Chiral Algebras and Ho…

2502.13227v1 (2)

For the beginning of Chapter 15:

This chapter studies topological
𝐸
𝑛
E
n
	​

-Koszul duality in the little-disks sense. It is distinct from the earlier BD-style hierarchy
𝐸
∞
E
∞
	​

-chiral/
𝑃
∞
P
∞
	​

-chiral/
𝐸
1
E
1
	​

-chiral on curves. The earlier chiral bar complex on a complex curve corresponds topologically to the
𝑛
=
2
n=2 case, since a complex curve is a real oriented surface. The
𝑛
=
1
n=1 case is the classical associative/
𝐴
∞
A
∞
	​

 bar-cobar theory on intervals or circles.

2502.13227v1 (2)

For Theorem 34.10.1(ii):

For
𝑛
=
2
n=2, one recovers the topological shadow of the chiral bar-cobar duality of Theorem 9.2.23 on complex curves. The
𝑛
=
1
n=1 case is the classical non-chiral associative/
𝐴
∞
A
∞
	​

 bar-cobar adjunction.

Boundary Chiral Algebras and Ho…

That is the coherent repair. Once you impose that two-axis convention—curve-chiral commutativity level versus topological manifold dimension—the manuscript stops contradicting itself, Yangians stay where they belong, Chapter 15 becomes mathematically honest, and the higher-dimensional programme becomes deep rather than confused.
