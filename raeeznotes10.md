1.

According to a document from March 2026, the latest version is materially stronger than the one I had been critiquing before. The core theorematic spine is now stated in the right architecture: Theorem A is construction-level and Verdier-intertwined, Theorem B is explicitly restricted to the Koszul locus with curved/coderived persistence off it, Theorem C is now formulated via a Verdier involution and complementary Lagrangians, and Theorem D is split into a scalar theorem
𝐷
s
c
a
l
D
scal
	​

 and a separate spectral theorem
𝐷
Δ
D
Δ
	​

, with the full universal Maurer–Cartan package
Θ
𝐴
Θ
A
	​

 kept conjectural.
Source files inspected: latest PDF, latest source tree ZIP.

Here is the up-to-speed diagnosis.

1. What is genuinely better now

The manuscript now has a real internal hierarchy. The introduction says outright that the project has five layers: constructions for every augmented chiral algebra, Koszul-recognition hypotheses, genus-0 theorems, higher-genus pre-Koszul data, and characteristic hierarchies separating proved scalar data from spectral data and from the conjectural universal class
Θ
𝐴
Θ
A
	​

. It also explicitly says that the free-field families are unconditionally modular Koszul, while affine Kac–Moody, Virasoro, and
𝑊
𝑁
W
N
	​

 are only conditionally modular Koszul, pending higher-genus PBW degeneration. That is a major improvement over earlier drafts, which tended to speak as if one theorem covered every regime.

The project also now knows exactly what Future 7 really is. Chapter 34 says the original “unified periodicity doctrine” is the weakest of the nine futures in its original form, and replaces it with a stratified picture: modular periodicity proved only in special rational cases, quantum periodicity proved, geometric periodicity partly conjectural, and the lcm mechanism treated as the unconditional structural content rather than the whole theorem. Even better, the manuscript now explicitly introduces a richer invariant
Π
(
𝐴
)
=
(
𝑀
𝐴
,
𝑄
𝐴
,
𝐺
𝐴
)
Π(A)=(M
A
	​

,Q
A
	​

,G
A
	​

) and says the scalar
P
e
r
i
o
d
(
𝐴
)
Period(A) is only its shadow.

Finally, Chapter 34 now says clearly that the full modular characteristic package is a quintuple

𝐶
𝐴
=
(
Θ
𝐴
,
𝜅
(
𝐴
)
,
Δ
𝐴
,
Π
𝐴
,
𝐻
𝐴
)
,
C
A
	​

=(Θ
A
	​

,κ(A),Δ
A
	​

,Π
A
	​

,H
A
	​

),

that the scalar part is proved, the spectral discriminant is proved, and the non-scalar class
Θ
𝐴
Θ
A
	​

 remains the principal open problem. That is exactly the right status distinction.

2. What remains live

The deepest remaining issue is no longer “the main theorems are broken.” It is propagation drift: the book now knows the right formal distinctions, but it has not enforced them uniformly across all chapters.

A. The higher-genus differential story is conceptually right but still not uniformly propagated

The latest source has the right formal picture in two places.

First, the introduction now separates:

curved fiberwise differentials
 
𝑑
f
i
b
2
=
𝜅
⋅
𝜔
𝑔
 
d
fib
2
	​

=κ⋅ω
g
	​

,

strict total differentials
 
𝐷
𝑔
2
=
0
 
D
g
2
	​

=0,

and the universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

 as the common H-level object behind them.

Second, Chapter 8.14 now explicitly says the higher-genus parameters come from the curve, not moduli:

𝑡
𝑖
∈
𝐻
1
(
Σ
𝑔
,
𝐶
)
,
𝐷
𝑔
=
𝑑
0
+
∑
𝑡
𝑖
𝑑
𝑖
,
𝐷
𝑔
2
=
0
,
t
i
	​

∈H
1
(Σ
g
	​

,C),D
g
	​

=d
0
	​

+∑t
i
	​

d
i
	​

,D
g
2
	​

=0,

and even inserts the Harer remark explaining why
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

) is not the right source for
𝑔
≥
2
g≥2. (Source: chapters/theory/higher_genus.tex:7152–7205.)

That is the correct formal move.

But the propagation is not complete. The Part I / Heisenberg summary and some older-looking forward-facing passages still speak more loosely about “genus-1 curvature
𝑑
2
=
𝜅
𝜔
1
d
2
=κω
1
	​

” or “a single scalar
𝜅
(
𝐴
)
κ(A) determines the entire genus tower,” without always making clear whether the differential in question is the fiberwise curved differential or the total corrected one. In the source tree, chapters/connections/genus_complete.tex, chapters/connections/holomorphic_topological.tex, and appendices/coderived_models.tex still use overlapping notations and mixed explanatory layers. The right fix is now obvious:

keep three permanent symbols:

𝑑
(
𝑔
)
f
i
b
,
𝐷
𝑔
t
o
t
,
𝑚
0
(
𝑔
)
,
d
(g)
fib
	​

,D
g
tot
	​

,m
0
(g)
	​

,

and add one cross-reference block at the start of every higher-genus or physics chapter saying which one is in use.

Until that happens, the formalism is much better than before, but still not perfectly stable.

B. Theorem D is now mostly correct, but the manuscript still oscillates between the scalar theorem and the full package

The refined introduction is correct:

𝐷
s
c
a
l
D
scal
	​

: one scalar
𝜅
(
𝐴
)
κ(A) determines the scalar modular package;

𝐷
Δ
D
Δ
	​

: the discriminant is a separately proved non-scalar invariant;

Θ
𝐴
Θ
A
	​

: conjectural non-scalar completion.

Chapter 34 is also correct: it says the full package is the quintuple
𝐶
𝐴
=
(
Θ
𝐴
,
𝜅
,
Δ
𝐴
,
Π
𝐴
,
𝐻
𝐴
)
C
A
	​

=(Θ
A
	​

,κ,Δ
A
	​

,Π
A
	​

,H
A
	​

), that
Θ
𝐴
Θ
A
	​

 is still open, and that
𝜅
κ is only the first characteristic number.

But the earlier “Part II opening” language and parts of the Heisenberg frame still compress this back to “Theorem D says a single scalar
𝜅
(
𝐴
)
κ(A) determines the entire genus tower,” which is only true for the scalar tower, not for the full package, because
Δ
𝐴
Δ
A
	​

 and
Π
𝐴
Π
A
	​

 are explicitly not determined by
𝜅
κ alone. The book itself now says that the genus expansion is only an “almost-complete” invariant and that different algebras can share the same
𝜅
κ.

So the right up-to-date reading is:

the scalar genus-obstruction tower is controlled by
𝜅
κ;

the full modular characteristic package is not.

That distinction should now replace every surviving informal phrase like “single scalar determines the entire genus tower” unless it is immediately qualified by “scalar package.”

C. The periodicity chapter is much more honest, but its final object is still not quite the right one

This is the strongest remaining conceptual weakness.

What is fixed:

modular periodicity is now split into proved minimal/WZW cases and conjectural general rational cases;

the weak geometric bound
3
𝑔
−
2
3g−2 is proved, the sharp
12
(
2
𝑔
−
2
)
12(2g−2) bound is conjectural with the correct Mumford relation cited;

the lcm combination mechanism is now treated as the unconditional structural content, not as a fully proved classification theorem.

What remains conceptually unstable:

the book still states a scalar “complete periodicity classification” theorem/conjecture in terms of
P
e
r
i
o
d
(
𝐴
)
Period(A), even after introducing the more refined periodicity triple
Π
(
𝐴
)
Π(A).

In other words, the manuscript has already discovered the correct object and then partly retreats back to the old scalar language.

The true current form is:

Π
(
𝐴
)
Π(A) is the primary invariant;

P
e
r
i
o
d
(
𝐴
)
Period(A) is a shadow extracted when the three commuting periodicity operators actually synchronize on a common graded object.

I would not call this a theorem-breaking error anymore. It is a theory-shaping issue: the book should stop treating scalar period as primitive.

D. KL target-category precision is fixed in theorem chapters but still drifts in example chapters

The theorematic side is now correct. The book says the KL target is the semisimplified tilting quotient
𝐶
(
𝑈
𝑞
(
𝑔
)
)
C(U
q
	​

(g)), not the full root-of-unity category.

But in the source tree, chapters/examples/kac_moody_framework.tex:1098–1178 still contains a mixed discussion:

one paragraph deliberately switches back to the full
R
e
p
f
d
(
𝑈
𝑞
(
𝑔
)
)
Rep
fd
(U
q
	​

(g)) because it wants BGG reciprocity in the non-semisimple setting,

the theorem immediately afterward reverts to the semisimplified tilting category.

This is not necessarily mathematically false, but it is categorically slippery. The reader is being asked to move between:

KL on semisimplified tilting categories,

BGG reciprocity in the full abelian category,

and
𝑞
↦
𝑞
−
1
q↦q
−1
 transport under Koszul duality,

without a sharp regime change marker.

The fix is straightforward: every such discussion needs an explicit tag saying which category is being used and why. Right now the theorematic chapters know the answer, but the examples still drift.

E. The conditional status of interacting families is now identified, but not fully respected everywhere

The introduction and Chapter 8 now say very clearly that free fields are unconditional, while affine Kac–Moody, Virasoro, and
𝑊
𝑁
W
N
	​

 need higher-genus PBW spectral-sequence degeneration and remain conditional in that sense.

That is the correct status.

The remaining problem is that some example chapters and summary rhetoric still talk as if “all standard interacting examples are modular Koszul” rather than “modular Koszul modulo PBW degeneration.” The introduction has already solved the logical issue. The rest of the manuscript now needs to inherit that exact phrasing.

3. The project’s shape, now

Up to speed, I would describe the manuscript like this:

It is no longer best understood as “a monograph proving all of modular Koszul duality.” It is better understood as a two-stratum work.

The first stratum is now solid:

geometric bar–cobar duality;

inversion on the Koszul locus with coderived persistence off it;

complementarity via Verdier involution and Lagrangian polarization;

scalar modular characteristic theorem;

spectral discriminant as a separate proved non-scalar invariant;

evaluation-locus / chain-level derived Drinfeld–Kohno bridge.

The second stratum is now clearly identified rather than blurred:

full universal
Θ
𝐴
Θ
A
	​

;

full coderived Ran-space formalism;

full factorization-categorical DK;

full synchronization of periodicity data;

higher-dimensional and BV/BRST/holographic completions.

That is progress. The book is now much closer to being a core theorem monograph with an explicit research programme than a single text oscillating between theorem and aspiration.

4. What I would now prioritize

If the goal is to stabilize the latest version, my priority order is:

Propagate the differential notation split everywhere.
This is the single highest-value cleanup because it affects Chapters 6, 8, 18, 20, 21, 29, 30, 31, and 34.

Normalize Theorem D language everywhere to the scalar/non-scalar split.
The current best wording is already in Chapter 2 and Chapter 34. Copy it backward.

Promote
Π
(
𝐴
)
Π(A) over
P
e
r
i
o
d
(
𝐴
)
Period(A) as the primary invariant.
Keep scalar period only as a derived corollary when synchronization is proved.

Tag category regimes explicitly in KL/quantum-group chapters.
“Semisimplified tilting,” “full abelian root-of-unity category,” and “evaluation-locus factorization category” should never be allowed to slide into one another without a local warning.

Enforce the conditional/unconditional boundary for modular Koszulity.
The introduction already does this correctly. The examples need to follow it.

Bottom line

The latest version is substantially better. The core A/B/C/D spine is now structurally credible in a way earlier versions were not. The project’s real weakness is no longer broken central theorems. It is that the manuscript has finally found its correct formal distinctions — scalar vs full package, fiberwise curvature vs total strict differential, stratified periodicity vs unified doctrine, semisimplified vs full quantum categories — and now needs one more pass to make every chapter obey them.


2.

I checked the latest PDF

main

 against the unpacked source tree bookrepo.zip, and the analysis does need to be updated.

The short version is:

the manuscript is materially stronger than the previous iteration.
The old fatal circularities around Theorems A and B are no longer present in their main definitions, and Theorem D has now been correctly split into a proved scalar theorem plus a separate proved spectral theorem plus a conjectural
Θ
𝐴
Θ
A
	​

-completion.

But the book is not yet fully clean. The main remaining pressure points are now narrower and subtler:

Theorem A’s new foundation theorem is still too sketchy to carry the full weight of A.

Theorem
𝐴
1
A
1
	​

 (“bar concentration”) is internally inconsistent with the corollary immediately before it.

Theorem C’s new fiber–center theorem inherits that instability.

A direct contradiction still survives elsewhere in the book: one theorem still says bar–cobar resolution exists for any chiral algebra.

The frame chapter and an early foundations chapter still propagate stale pre-rewrite formulations, especially around
Θ
𝐴
Θ
A
	​

.

So the state of the book is now:

B and D are mostly stabilized.

A and C are much better organized but not yet referee-secure.

The remaining defects are structural proof-quality issues and stale propagation, not raw conceptual collapse.

What is genuinely fixed in the latest iteration
1. Theorem A is no longer definitional at the level of the main definition

This is a real improvement.

The source now introduces:

a chiral twisting datum in chapters/theory/chiral_koszul_pairs.tex:53–75,

a chiral Koszul morphism in chapters/theory/chiral_koszul_pairs.tex:77–89,

and only then a chiral Koszul pair as a pair of such data with Verdier-compatible dual coalgebras in chapters/theory/chiral_koszul_pairs.tex:209–248.

Crucially, the definition now says these are antecedent hypotheses, and that Theorem A proves the bar-cobar identification as a consequence (chiral_koszul_pairs.tex:229–235).

That directly fixes the earlier fatal defect where Theorem A had been folded into the definition.

2. Theorem B is no longer built into the definition of modular Koszulity

This is also a real repair.

The current def:modular-koszul-chiral is now a definition of a modular pre-Koszul chiral algebra with:

data D1–D6,

axioms MK1–MK3,

and then consequences MK4–MK5, explicitly marked as consequences of Theorems B and C, not axioms.

See chapters/theory/higher_genus.tex:8204–8301.

That resolves the previous direct circularity in which inversion and complementarity had been encoded as axioms and then “proved.”

3. Theorem C has been re-architected correctly

This is one of the strongest improvements.

The complementarity package is now explicitly split into:

C
0
0
	​

: the fiber–center identification (higher_genus.tex:4596–4633),

C
1
1
	​

: the chain-level/homotopy Lagrangian polarization (higher_genus.tex:4673ff.).

The theorem itself now works with:

𝐶
𝑔
(
𝐴
)
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
,
𝑄
𝑔
(
𝐴
)
=
fib
⁡
(
𝜎
−
i
d
)
,
C
g
	​

(A)=RΓ(
M
g
	​

,Z
A
	​

),Q
g
	​

(A)=fib(σ−id),

and gives the splitting via homotopy eigenspaces rather than the old dimension-count rhetoric. That is the correct conceptual form.

4. Theorem D is now correctly stratified

This is a major improvement.

The source now distinguishes:

the scalar modular characteristic package (higher_genus.tex:8448–8475),

the full modular characteristic package as conjectural (higher_genus.tex:8477–8533),

the scalar modular characteristic theorem (higher_genus.tex:8575–8628),

the separate spectral characteristic theorem (higher_genus.tex:8668–8679),

and the conjectural universal modular Maurer–Cartan class (higher_genus.tex:8688ff.).

This resolves the previous overstatement in which Theorem D appeared to prove the whole package, including
Θ
𝐴
Θ
A
	​

.

5. The introduction is now much better aligned with the intended architecture

The introduction now explicitly says:

A decomposes as
𝐴
0
/
𝐴
1
/
𝐴
2
A
0
	​

/A
1
	​

/A
2
	​

,

C decomposes as
𝐶
0
/
𝐶
1
C
0
	​

/C
1
	​

,

D is split into
𝐷
s
c
a
l
D
scal
	​

,
𝐷
Δ
D
Δ
	​

, and conjectural
Θ
𝐴
Θ
A
	​

,

and inversion is only on the Koszul locus (chapters/theory/introduction.tex:145–225).

This is much closer to a publishable architecture.

What still remains live
1. The new “fundamental theorem of chiral twisting morphisms” is still not proved at referee level

Location: chapters/theory/chiral_koszul_pairs.tex:107–179
Severity: HIGH

Diagnosis

The theorem statement is exactly the right one. The problem is the proof.

The two key steps:

𝐾
𝜏
𝐿
K
τ
L
	​

 is “precisely the mapping cone” of the counit (lines 146–154),

𝐾
𝜏
𝑅
K
τ
R
	​

 is “the mapping cone” of the unit (lines 156–159),

are simply asserted.

That is acceptable in a classical algebra text if one has already built the twisting-morphism formalism carefully. Here, it is new chiral/factorization machinery. The theorem is supposed to be the chiral analogue of the Loday–Vallette fundamental theorem, and the proof never actually constructs the mapping-cone identifications in the chiral setting.

The converse direction is also too compressed:

filter
Ω
𝑋
(
𝐶
)
Ω
X
	​

(C),

deduce
𝐸
2
E
2
	​

-collapse,

recover acyclicity of the twisted tensor products.

That is plausible, but as written it is still a sketch, not a theorem-proof worthy of carrying Main Theorem A.

Why it matters

Theorem A now depends on this theorem as its real foundation. So although the old circularity is gone, A is still not fully secure until this proof is made rigorous.

Resolution

Add a separate lemma package before Theorem A
0
0
	​

:

Lemma (Twisted tensor product = cone of counit).
Construct an explicit quasi-isomorphism

𝐾
𝜏
𝐿
(
𝐴
,
𝐶
)
≃
Cone
⁡
(
𝜀
𝜏
)
[
−
1
]
.
K
τ
L
	​

(A,C)≃Cone(ε
τ
	​

)[−1].

Lemma (Twisted tensor product = cone of unit).
Construct

𝐾
𝜏
𝑅
(
𝐶
,
𝐴
)
≃
Cone
⁡
(
𝜂
𝜏
)
[
−
1
]
.
K
τ
R
	​

(C,A)≃Cone(η
τ
	​

)[−1].

Lemma (Filtered comparison).
State the exact filtration hypotheses under which quasi-isomorphism of
𝜀
𝜏
ε
τ
	​

 implies acyclicity of the twisted tensor products.

Right now the source has the correct theorem, but not yet the proof quality.

2. Theorem
𝐴
1
A
1
	​

 (“bar concentration”) is internally inconsistent with the preceding corollary

Location: chapters/theory/chiral_koszul_pairs.tex:699–738
Severity: HIGH

Diagnosis

The source states:

𝐻
𝑖
(
𝐵
ˉ
c
h
(
𝐴
1
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
c
h
(
𝐴
1
)
)
≅
𝐴
2
!
.
H
i
(
B
ˉ
ch
(A
1
	​

))=0(i

=0),H
0
(
B
ˉ
ch
(A
1
	​

))≅A
2
!
	​

.

But in the immediately preceding corollary/proof chain, the source has already concluded

𝐻
𝑛
(
𝐵
ˉ
g
e
o
m
(
𝐴
)
)
≅
(
𝐴
!
)
𝑛
H
n
(
B
ˉ
geom
	​

(A))≅(A
!
)
n
	​


via the PBW/spectral-sequence computation (chiral_koszul_pairs.tex:672–680, and cited again at 726–727).

Those two statements are not compatible unless
(
𝐴
2
!
)
𝑛
=
0
(A
2
!
	​

)
n
	​

=0 for
𝑛
>
0
n>0, which is false in the standard graded Koszul situation.

So either:

the theorem statement is wrong,

or the proof is using cohomological degree and internal degree inconsistently,

or the corollary is mis-stated.

At the moment, the text says all three things at once.

Why it matters

This is no longer a cosmetic mismatch. Theorem
𝐴
1
A
1
	​

 is part of the newly advertised
𝐴
0
/
𝐴
1
/
𝐴
2
A
0
	​

/A
1
	​

/A
2
	​

 architecture, and later theorems — especially
𝐶
0
C
0
	​

 — cite it.

Resolution

Choose one of the following formulations and use it everywhere:

Object-level form.

𝐵
ˉ
𝑋
(
𝐴
1
)
≃
𝐴
2
!
B
ˉ
X
	​

(A
1
	​

)≃A
2
!
	​


in the derived category of graded coalgebras, where
𝐴
2
!
A
2
!
	​

 carries internal grading but sits in cohomological degree
0
0.

Bigraded form.
State explicitly that

𝐻
𝑝
,
𝑞
(
𝐵
ˉ
𝑋
(
𝐴
1
)
)
=
0
unless
𝑞
=
0
,
𝐻
𝑝
,
0
≅
(
𝐴
2
!
)
𝑝
.
H
p,q
(
B
ˉ
X
	​

(A
1
	​

))=0unless q=0,H
p,0
≅(A
2
!
	​

)
p
	​

.

Totalized form.
If total degree is intended, then the theorem must be rewritten to match the actual totalization convention.

As written,
𝐴
1
A
1
	​

 is mathematically unstable.

3. Theorem
𝐶
0
C
0
	​

 is improved, but still inherits the instability of
𝐴
1
A
1
	​


Location: chapters/theory/higher_genus.tex:4596–4633
Severity: HIGH

Diagnosis

The new fiber–center theorem is a serious improvement. But its proof still has two compressed steps:

Step 3 says diagonal Ext vanishing implies only total degree
0
0 survives “by spectral sequence comparison.”

Step 4 identifies the surviving
𝑅
0
𝜋
𝑔
∗
R
0
π
g∗
	​

 with the center local system by applying Theorem~\ref{thm:bar-concentration} fiberwise.

The first step is still schematic. The second step is now a problem because thm:bar-concentration is itself unstable for the reasons above.

So Theorem
𝐶
0
C
0
	​

 is now conceptually in the right place, but it is not yet fully stabilized.

Why it matters

Theorem C
1
1
	​

 depends on C
0
0
	​

. So the complementarity theorem is much improved, but it still depends on a layer that is not yet fully rigorous.

Resolution

Do not cite
𝐴
1
A
1
	​

 here until
𝐴
1
A
1
	​

 is fixed.

Instead prove
𝐶
0
C
0
	​

 directly by:

filtering the full fiber complex by bar degree,

identifying the associated graded with the Koszul/Ext complex of the associated graded algebra,

proving total cohomology concentration in degree
0
0,

then using proper base change / Leray to identify the local system.

That proof would make Theorem C genuinely referee-stable.

4. A contradiction still survives: one theorem still says the cobar of the bar resolves any chiral algebra

Location: chapters/theory/higher_genus.tex:1033–1039
Severity: CRITICAL

Diagnosis

This is still a live contradiction.

The source states:

Theorem [Cobar resolution; ProvedElsewhere]
“For any chiral algebra
𝐴
A, the cobar of the bar provides a free resolution…”

and then writes a full resolution complex.

But the same manuscript now correctly says elsewhere:

the counit is a quasi-isomorphism only on the Koszul locus,

off the locus one only has a curved/coderived object,

and admissible/minimal-model cases are explicit failures.

So the manuscript still simultaneously contains:

the correct scoped theorem B,

and an incorrect universal resolution theorem.

Why it matters

This is not just stale exposition. It is a theorem-level contradiction in the core theory part.

Resolution

Delete or rewrite higher_genus.tex:1033–1039 immediately.

The replacement should say:

For every augmented chiral algebra, the bar and cobar constructions exist.
For a chiral Koszul algebra, the counit
Ω
(
𝐵
ˉ
(
𝐴
)
)
→
𝐴
Ω(
B
ˉ
(A))→A is a quasi-isomorphism.
Off the Koszul locus, the resulting object persists only in the completed coderived category.

Until this is removed, the theorematic layer is inconsistent.

5. The frame chapter still presents the full modular characteristic package as if
Θ
𝐴
Θ
A
	​

 were already available

Location: chapters/frame/heisenberg_frame.tex:1510–1566
Severity: MEDIUM/HIGH

Diagnosis

The frame chapter now says:

the modular characteristic package of
𝐻
𝑘
H
k
	​

 includes the universal Maurer–Cartan class
Θ
𝐻
𝑘
Θ
H
k
	​

	​

,

the package is “fully determined” by
𝜅
=
𝑘
κ=k,

and
Θ
𝐴
Θ
A
	​

 is the fundamental object.

But later, the theory chapters correctly distinguish:

scalar package (proved),

spectral package (proved),

full
Θ
𝐴
Θ
A
	​

-completion (conjectural).

So Chapter 1 is still written in the language of the future theory, not the current theorematic status.

Why it matters

The frame chapter is the reader’s model of the whole book. If it overstates the status of
Θ
𝐴
Θ
A
	​

, it poisons the epistemic clarity of the entire monograph.

Resolution

Rewrite the frame chapter’s package section as follows:

keep
𝜅
κ,
{
𝐹
𝑔
}
{F
g
	​

}, and
Δ
Δ as established;

call
Θ
𝐻
𝑘
Θ
H
k
	​

	​

 the conjectural non-scalar completion;

state explicitly that the frame chapter is previewing the shape of the full package, not claiming its full construction.

6. Chapter 3 still contains a stale preview-definition of chiral Koszul pair

Location: chapters/theory/algebraic_foundations.tex:97–106
Severity: MEDIUM

Diagnosis

This section still says, in effect:

two chiral algebras form a chiral Koszul pair if

𝐵
ˉ
(
𝐴
1
)
≃
𝐴
2
!
B
ˉ
(A
1
	​

)≃A
2
!
	​

,
𝐵
ˉ
(
𝐴
2
)
≃
𝐴
1
!
B
ˉ
(A
2
	​

)≃A
1
!
	​

, and
Ω
(
𝐴
𝑖
!
)
≃
𝐴
𝑖
Ω(A
i
!
	​

)≃A
i
	​

.

That is precisely the older, conclusion-bearing form of the definition which the actual Chapter 9 definition has now corrected.

So Chapter 9 has been fixed, but Chapter 3 still contains the stale earlier form.

Why it matters

It creates an avoidable impression that the circularity remains, even though the actual definition is now better.

Resolution

Rewrite algebraic_foundations.tex:97–106 so it previews the new architecture:

construction layer: bar/cobar always exist,

recognition layer: chiral twisting datum + Koszul morphism,

theorem layer: bar/cobar identification for a chiral Koszul pair.

This is a propagation fix, not a new mathematical theorem.

7. Theorem D is now mostly correct, but the introduction still speaks too confidently about the full package

Location:

chapters/theory/introduction.tex:186–207

chapters/theory/introduction.tex:245–314

Severity: MEDIUM

Diagnosis

The theorem statements themselves are now well split. That is good.

But the introduction still says that the genus tower is “a single Maurer–Cartan deformation” and that all three semantic levels are realizations of the (conjectural) universal class
Θ
𝐴
Θ
A
	​

. That is conceptually right, but theorematically stronger than what the book actually constructs.

Why it matters

This is not wrong, but it still lets the reader drift too easily from:

a proved scalar theorem,
to

a proved spectral theorem,
to

a conjectural full MC package.

Resolution

Keep the vision, but add one explicit sentence after introduction.tex:245–314:

In this monograph, only the scalar and spectral shadows are fully constructed; the universal non-scalar Maurer–Cartan object remains a programme-level conjecture.

That would fully harmonize the introduction with the repaired theorem package.

Updated verdict

Here is the genuinely up-to-date state.

What is now solid

The old direct circularities in A and B have been substantially repaired.

The complementarity theorem is now in the right conceptual form.

The scalar/spectral split of D is a real improvement.

The introduction’s architecture is far better than before.

What is still broken

A
0
0
	​

 is still underproved.

A
1
1
	​

 is still internally inconsistent.

C
0
0
	​

 therefore remains unstable.

A generic universal bar–cobar resolution theorem still survives elsewhere and directly contradicts the corrected scoped theory.

So the current mathematical picture is:

Theorem B: mostly stabilized.

Theorem D: mostly stabilized.

Theorem A: architecturally fixed, but not yet fully proved at referee level.

Theorem C: structurally much improved, but still dependent on an unstable auxiliary theorem.

If you want, I can now produce a new referee-grade replacement package for only the still-live defects — i.e. a minimal patch set for:

𝐴
0
A
0
	​

,

𝐴
1
A
1
	​

,

𝐶
0
C
0
	​

,

the surviving universal-resolution contradiction,

and the frame/introduction propagation fixes.


3.

According to a document from March 2026, the latest iteration is materially stronger than the version I last assessed. The manuscript now explicitly separates the curved fiberwise differential
𝑑
f
i
b
d
fib
	​

 from the strict total corrected differential
𝐷
𝑔
D
g
	​

, and it also separates the proved scalar modular package from the conjectural full Maurer–Cartan package. The introduction now says the higher-genus data should be read on three semantic levels—H-level, M-level, and S-level—and it states plainly that the scalar package is proved while the full universal class
Θ
𝐴
Θ
A
	​

 remains conjectural.

That means my updated global judgment is this: the core theorematic spine is now mostly stable. The old attacks on complementarity, on the need to distinguish fiberwise curvature from strict total nilpotence, on conditional modular Koszulity for interacting families, and on the Kazhdan–Lusztig target category have largely been answered in the current text. In particular, the manuscript now treats interacting families only conditionally through higher-genus PBW degeneration, and it now states the KL target as the semisimplified tilting category
𝐶
(
𝑈
𝑞
(
𝑔
)
)
C(U
q
	​

(g)), not the full root-of-unity representation category.

The place where the project is still genuinely vulnerable is the periodicity package. The manuscript has become more honest in its prose about stratified periodicity and the periodicity triple
Π
(
𝐴
)
Π(A), but one major theorem in that chapter still looks overproved. Theorem 11.6.1 still claims proved modular periodicity for Virasoro minimal models, and the surrounding discussion still says the key input is that theta-over-eta characters give “exact periodicity of Fourier coefficients” and that this lifts to bar-cohomology periodicity.

That proof is not sound as written. The step from
𝑇
𝑁
=
I
d
T
N
=Id to eventual periodicity of weight-space data is exactly the dangerous step, and the claim that theta/eta characters have exact periodic Fourier coefficients is false in the naive sense needed there. I checked the Rocha–Caridi series directly for the Ising vacuum
𝑀
(
3
,
4
)
M(3,4): the relative graded coefficients at offsets
0
,
48
,
96
0,48,96 are
1
,
2048
,
223561
1,2048,223561, so the weight-space dimensions themselves are not periodic with period
48
48. That does not by itself disprove periodicity of bar cohomology, but it does show that the proof’s Step 2 mechanism is invalid. So the right current assessment is: Theorem 11.6.1 and the parallel WZW theorem should be treated as unsupported by their present proofs unless a different argument is supplied. Because Chapter 34 still uses those theorems as part of the “unconditional stratum,” this flaw propagates into the status accounting of Future 7.

A second live issue sits immediately downstream. Theorem 11.6.25 is labeled proved here and states that under Koszul duality the quantum period is preserved, the geometric period is unchanged, and the dual modular period is
24
𝑞
′
/
gcd
⁡
(
𝑝
′
,
24
)
24q
′
/gcd(p
′
,24), yielding an lcm bound for the dual. But the same periodicity section also says that the structural lcm mechanism is unconditional while the specific modular and geometric values remain conjectural. So part (3) of Theorem 11.6.25 is still too strong in its current status label: it imports the conjectural modular-period formula while presenting the full theorem as proved. The clean fix is to split 11.6.25 into a proved theorem for the quantum part and a conditional/conjectural addendum for the modular-period transport statement.

There is also still a genuine status drift between Chapter 1 and the later theory chapters. In the Heisenberg frame, Definition 1.12.1 still presents the “modular characteristic package for Heisenberg” as consisting of the universal Maurer–Cartan class
Θ
𝐻
𝑘
Θ
H
k
	​

	​

, the ambient deformation complex, the spectral discriminant, and
𝜅
(
𝐻
𝑘
)
κ(H
k
	​

), and then says the package is fully determined by
𝜅
=
𝑘
κ=k. But later, the theory chapter now cleanly distinguishes the scalar package as proved from the full package
(
Θ
𝐴
,
𝜅
(
𝐴
)
,
Δ
𝐴
,
Π
𝐴
,
𝐻
𝐴
)
(Θ
A
	​

,κ(A),Δ
A
	​

,Π
A
	​

,H
A
	​

) as conjectural in its non-scalar part. Those two presentations are no longer aligned. If
Θ
𝐴
Θ
A
	​

 is still conjectural in general, then Chapter 1 should not present
Θ
𝐻
𝑘
Θ
H
k
	​

	​

 as if it already belongs to a fully established package without either proving the Heisenberg case separately or explicitly labeling it as the anticipated full refinement of the scalar package.

A smaller but still real bookkeeping problem remains in the conjecture/concordance machinery. In the source tree, the
𝑠
𝑙
^
3
sl
3
	​

 generating-function conjecture currently carries two labels—conj:sl3-bar-gf and conj:sl3-discriminant—on the same conjecture block, while the concordance chapter lists them as if they were two separate open items. That does not damage a theorem, but it does corrupt the project’s conjecture census and makes cross-references unreliable. This one does not show up cleanly in the rendered PDF citations, but it is present in the TeX source and should be fixed before the conjecture index is treated as authoritative.

So the up-to-date picture is:

The manuscript has successfully repaired the homological core: semantic levels, fiberwise-vs-total differentials, scalar-vs-full characteristic packages, conditional modular Koszulity, and the KL target category are now much better organized.
The manuscript’s remaining weak flank is periodicity, not complementarity or bar–cobar duality. The periodicity chapter is now conceptually better than before, but its flagship “proved” minimal-model/WZW periodicity results still need either a new proof or a status downgrade, and Theorem 11.6.25 needs to be split into proved and conditional pieces.
The only other substantial issue is status propagation: Chapter 1 still talks as though the full modular characteristic package is already available, while the later theory correctly says the full non-scalar Maurer–Cartan package is conjectural.

The highest-leverage edits now are very clear. First, downgrade Theorems 11.6.1 and 11.6.7 unless you can replace the theta/eta periodicity argument by a real theorem about bar-complex periodicity. Second, split Theorem 11.6.25 into a proved structural/profile statement and a conjectural modular-period transport statement. Third, rewrite Definition 1.12.1 so that the Heisenberg chapter presents the scalar package as theorematic and the full
Θ
𝐻
𝑘
Θ
H
k
	​

	​

-package as a preview of the conjectural full theory. Fourth, clean the conjecture registry so one conjecture is one item. If you want, I can turn this into a precise patch list against the source tree, file by file.
