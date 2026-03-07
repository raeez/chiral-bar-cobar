According to a document from March 2026, I reviewed the latest compiled manuscript together with the uploaded source tree and treated CLAUDE.md as a self-assessment to be checked, not trusted. The current PDF is here:

main

 and the current source archive is bookrepo.zip.

My bottom-line judgment is the same in substance as a harsh referee report would be:

the manuscript now has a substantial real core, but it is still not publishable in its present form because there remain fatal structural mathematical defects in the proof architecture of the main theorems.

The worst defects are no longer “obvious sign errors.” They are subtler and more serious:

Theorem A is still largely built into the definition of “chiral Koszul pair.”

Theorem B is still built into the definition of “modular Koszul chiral algebra,” and the example-verification proposition is circular.

Theorem C still relies on a fiber-cohomology lemma whose written proof does not establish what the theorem needs.

The manuscript still contains a direct cross-chapter contradiction: one chapter says bar–cobar inversion holds only on the Koszul locus, while another still states a bar–cobar resolution theorem “for any chiral algebra.”

The Hochschild duality package is still internally inconsistent across chapters.

That is enough, by itself, to block acceptance.

Part I. Diagnostic — the ills
1. Logical / Mathematical
Finding 1. Main Theorem A is still effectively definitional

Location:

chapters/theory/chiral_koszul_pairs.tex, Definition def:chiral-koszul-pair, lines 65–98.

chapters/theory/higher_genus.tex, Theorem thm:bar-cobar-isomorphism-main, lines 1535–1595.

CLAUDE.md, lines 29–33.

Severity: CRITICAL

Diagnosis:
The definition of a chiral Koszul pair already requires the content of Theorem A.

The definition says that
(
𝐴
1
,
𝐴
2
)
(A
1
	​

,A
2
	​

) is a chiral Koszul pair if:

𝐵
ˉ
c
h
(
𝐴
1
)
≃
𝐴
2
!
,
𝐵
ˉ
c
h
(
𝐴
2
)
≃
𝐴
1
!
,
B
ˉ
ch
(A
1
	​

)≃A
2
!
	​

,
B
ˉ
ch
(A
2
	​

)≃A
1
!
	​

,

and

𝐴
1
≃
Ω
c
h
(
𝐴
2
!
)
,
𝐴
2
≃
Ω
c
h
(
𝐴
1
!
)
.
A
1
	​

≃Ω
ch
(A
2
!
	​

),A
2
	​

≃Ω
ch
(A
1
!
	​

).

Then Theorem A assumes “Let
(
𝐴
1
,
𝐴
2
)
(A
1
	​

,A
2
	​

) be a chiral Koszul pair” and concludes exactly those same bar/cobar quasi-isomorphisms.

This is not a mild redundancy. It means that Theorem A is not an independent theorem in the present source. It is the unpacking of a definition.

Worse, the definition explicitly says the equivalence of Version I and Version II is “immediate,” but the converse direction uses Theorem A itself (“Version I implies acyclicity … by Theorem~\ref{thm:bar-cobar-isomorphism-main}”), so even the claimed equivalence inside the definition is not independent.

Resolution:
Replace Definition def:chiral-koszul-pair by a genuine recognition criterion. For example, define a chiral Koszul pair by antecedent data such as:

a candidate dual chiral coalgebra
𝐶
𝑖
C
i
	​

,

a universal twisting morphism,

acyclicity of the twisted tensor/Koszul complexes,

a PBW / diagonal-Ext condition,

compatibility with Verdier duality on the bar complex.

Then prove bar/cobar duality from those hypotheses.
If you do not do this, Theorem A must be demoted from “main theorem” to “definition unpacking.”

Finding 2. Main Theorem B is still circular through the definition of modular Koszul chiral algebra

Location:

chapters/theory/higher_genus.tex, Definition def:modular-koszul-chiral, lines 7924–7999.

chapters/theory/higher_genus.tex, Theorem thm:higher-genus-inversion, lines 7706–7733.

chapters/theory/higher_genus.tex, Proposition prop:standard-examples-modular-koszul, lines 8005–8030.

chapters/theory/higher_genus.tex, Proposition prop:conditional-modular-koszul, lines 8032–8060.

CLAUDE.md, lines 29–33.

Severity: CRITICAL

Diagnosis:
The definition of “modular Koszul chiral algebra” still includes as axioms:

MK3: bar–cobar inversion,

MK5: complementarity.

Then Theorem B assumes that
𝐴
A is a modular Koszul chiral algebra and proves inversion.
And the proposition “Standard examples are modular Koszul” verifies MK3 by citing Theorem B and MK5 by citing Theorem C.

So the logic is:

define the object by requiring inversion and complementarity,

state inversion and complementarity as theorems about that object,

use those theorems to show examples satisfy the definition.

This is a genuine dependency cycle.

Resolution:
Introduce a weaker notion, e.g. modular pre-Koszul chiral algebra, whose axioms stop before inversion and complementarity. A sensible split is:

MK1: genus-zero Koszulity / recognition criterion;

MK2: Verdier/factorization compatibility;

MK4: higher-genus PBW / filtered modular control.

Then:

Theorem A proves the bar/cobar identification,

Theorem B proves inversion,

Theorem C proves complementarity,

only afterward may one define “modular Koszul chiral algebra” as an object satisfying the conclusions.

As long as the current definition remains in place, Theorem B is not referee-valid.

Finding 3. The written proof of Theorem A still contains a false citation

Location:

chapters/theory/higher_genus.tex, proof of Theorem thm:bar-cobar-isomorphism-main, lines 1627–1636.

Severity: HIGH

Diagnosis:
The proof says that the nontrivial content is established by combining three results, the last being Theorem thm:bar-nilpotency-complete, and then states that this theorem proves that the augmented bar complex has cohomology concentrated in degree
0
0, identifying
𝐻
0
H
0
 with the Koszul dual coalgebra.

But Theorem thm:bar-nilpotency-complete proves
𝑑
b
a
r
2
=
0
d
bar
2
	​

=0. It does not prove bar concentration in degree
0
0, and it does not establish the Koszul property. So the proof of Theorem A still attributes the decisive homological step to the wrong theorem.

Resolution:
Insert an actual theorem of the form:

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
,
H
i
(
B
ˉ
ch
(A
1
	​

))=0 (i
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

,

under explicit hypotheses independent of the conclusion.

The natural mechanism is a filtration argument:

filter the bar complex by conformal weight / bar length,

identify the associated graded with a classical/operadic Koszul complex,

invoke genuine diagonal concentration there,

lift by spectral sequence.

Until that theorem exists, Theorem A’s proof is not correct as written.

Finding 4. Main Theorem C still rests on an insufficiently proved fiber-cohomology lemma

Location:

chapters/theory/higher_genus.tex, Lemma lem:fiber-cohomology-center, lines 4982–5068.

chapters/theory/higher_genus.tex, Theorem thm:quantum-complementarity-main, especially its use of the ambient center local system.

Severity: HIGH

Diagnosis:
The manuscript’s big improvement is real: complementarity is now proved by a Verdier involution and eigenspace/Lagrangian splitting, not by a bogus dimension count. That part is much better.

The remaining weak point is the lemma identifying the fiber cohomology sheaf with the center. The written argument proves:

𝐻
0
H
0
 of the fiber complex equals the center
𝑍
(
𝐴
)
Z(A),

non-diagonal cohomology vanishes at each bar degree
𝑝
p,

and then concludes the entire fiber cohomology sheaf is concentrated in degree
0
0.

But the final sentence says:

“Therefore
𝐻
f
i
b
e
r
𝑞
=
0
H
fiber
q
	​

=0 for
𝑞
>
0
q>0 when restricted to the degree-0 bar component…”

That is not the same as proving total fiber cohomology concentration. The theorem needs the whole sheaf
𝑅
Γ
(
𝑀
‾
𝑔
,
𝑍
(
𝐴
)
)
RΓ(
M
g
	​

,Z(A)), not just the degree-0 bar component.

So the current proof still stops short of the statement it uses later.

Resolution:
Prove a true total vanishing statement. The clean route is:

Filter the full fiber bar complex by bar degree.

Identify the associated graded with a Koszul/Ext complex whose total cohomology is diagonal.

Show that the spectral sequence for the fiber complex collapses so that only total degree
0
0 survives.

Deduce the full local system is
𝑍
(
𝐴
)
⊗
𝐶
‾
Z(A)⊗
C
	​

, not merely its degree-0 piece.

If this cannot be proved, Theorem C must be weakened to a statement about the scalar/center degree-0 sector only.

Finding 5. A direct contradiction remains: one theory chapter still states bar–cobar resolution for any chiral algebra

Location:

chapters/theory/bar_cobar_construction.tex, Remark rem:fundamental-distinction, lines 4624–4633.

chapters/theory/deformation_theory.tex, Theorem thm:bar-cobar-resolution, lines 1362–1383.

chapters/theory/deformation_theory.tex, Theorem “Hochschild via bar-cobar,” lines 247–253.

By contrast: chapters/theory/bar_cobar_construction.tex, Theorem thm:bar-cobar-inversion-qi, lines 7945–7983; chapters/theory/higher_genus.tex, Theorem thm:higher-genus-inversion, lines 7706–7733.

The manuscript’s own scope remark in the current PDF says the Koszul hypothesis is essential for inversion.

Severity: CRITICAL

Diagnosis:
This is the sharpest remaining internal contradiction.

One place says, explicitly:

“Always True (for any algebra
𝐴
A): …
Ω
(
𝐵
ˉ
(
𝐴
)
)
≃
𝐴
Ω(
B
ˉ
(A))≃A.”

Another chapter states:

“For any chiral algebra
𝐴
A on a curve
𝑋
X, there is a quasi-isomorphism

Ω
g
e
o
m
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
→
∼
𝐴
Ω
geom
(
B
ˉ
geom
(A))
∼
	​

A.”

But the later, more careful theorem and its scope remark say the exact opposite: the counit is a quasi-isomorphism only on the Koszul/pro-nilpotent/completed locus, and explicitly fails at admissible affine levels and minimal-model Virasoro/
𝑊
W-algebras.

So the manuscript still simultaneously contains:

the correct scoped theorem,

the incorrect universal theorem,

and a remark literally saying bar–cobar inversion is always true for any algebra.

That is a direct contradiction in the theorematic layer.

Resolution:
Delete or rewrite all “for any chiral algebra” bar–cobar inversion statements outside the scoped theorem.

Specifically:

Replace the remark at 4624–4633 by:

“Always true: bar and cobar constructions exist.
Only on the Koszul / completed locus: the counit is a quasi-isomorphism.”

Replace Theorem thm:bar-cobar-resolution by a scoped theorem:

Ω
g
e
o
m
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
→
∼
𝐴
Ω
geom
(
B
ˉ
geom
(A))
∼
	​

A

for Koszul chiral algebras (or in the coderived completed sense off the Koszul locus).

Rewrite the Hochschild computation theorem so it uses the scoped version only.

This contradiction is fatal in its current form.

Finding 6. The Hochschild duality package is still inconsistent across chapters

Location:

chapters/theory/higher_genus.tex, Corollary cor:hochschild-duality, lines 1717ff.

chapters/theory/deformation_theory.tex, Theorem thm:main-koszul-hoch, lines 452–505.

chapters/theory/hochschild_cohomology.tex, lines 694–704.

Severity: HIGH

Diagnosis:
The book still contains two inequivalent Hochschild-duality formulations:

one of the form

𝐶
𝐻
𝑛
(
𝐴
1
)
≅
𝐶
𝐻
𝑛
(
𝐴
2
)
∨
⊗
𝜔
𝑋
[
2
]
,
CH
n
(A
1
	​

)≅CH
n
(A
2
	​

)
∨
⊗ω
X
	​

[2],

another of the form

𝐻
𝐻
c
h
i
r
a
l
𝑛
(
𝐴
)
≅
𝐻
𝐻
c
h
i
r
a
l
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
chiral
n
	​

(A)≅HH
chiral
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

These are not the same statement written differently. One preserves degree and shifts the object; the other reflects degree. The later cyclic-homology chapter then cites the second formulation as though it were the unique theorem.

The proof in deformation_theory.tex also remains overcompressed at exactly the nontrivial point: it says the varying Verdier shift
𝑛
+
2
n+2 is “absorbed by Koszul concentration,” but the actual bookkeeping is not written in a stable bigraded form. So even apart from the contradictory formulations, the exposition of the proof still does not meet the standard of the claim.

Resolution:
Pick one definitive object-level statement and derive everything else from it.

For example:

𝑅
𝐻
𝐻
c
h
i
r
a
l
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
i
r
a
l
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
chiral
	​

(A)≃RHom(RHH
chiral
	​

(A
!
),ω
X
	​

[2]).

Then derive the group-level form by taking cohomology with an explicit bigrading convention. This resolves both the contradiction and the current ambiguity in the shift accounting.

Finding 7. The “modular characteristic package” is still stated as proved even though it contains a conjectural component

Location:

chapters/theory/higher_genus.tex, Definition def:modular-characteristic-package, lines 8089–8118.

chapters/theory/higher_genus.tex, Theorem thm:modular-characteristic, lines 8127–8177.

chapters/theory/introduction.tex, lines 147ff.

CLAUDE.md, lines 29–33.

Severity: MEDIUM/HIGH

Diagnosis:
The current definition of the “modular characteristic package” is tagged \ClaimStatusProvedHere, yet it explicitly includes the universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

, and then states that the fourth component is conjectural in its non-scalar form.

So a definition tagged as proved here packages together:

three established invariants,

one conjectural invariant.

Then Theorem D says the modular characteristic package is determined, “as a scalar system,” by
𝜅
(
𝐴
)
κ(A), but also keeps
Δ
𝐴
Δ
A
	​

 and
Θ
𝐴
Θ
A
	​

 in rhetorical proximity. The introduction and CLAUDE.md then present all four main theorems as already proved.

This is a status-control problem with mathematical consequences: it makes it hard to tell exactly what theorem D proves.

Resolution:
Split the package explicitly:

Definition: scalar modular characteristic package

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
,
Δ
𝐴
)
(κ(A),{F
g
	​

(A)},Δ
A
	​

)

with \ClaimStatusProvedHere.

Conjectural extension: full modular homotopy package

(
𝜅
,
{
𝐹
𝑔
}
,
Δ
,
Θ
𝐴
)
,
(κ,{F
g
	​

},Δ,Θ
A
	​

),

with \ClaimStatusConjectured.

Then restate Theorem D as the scalar modular characteristic theorem. That is mathematically honest and much clearer.

Finding 8. The manuscript’s own claim-status system is no longer internally reliable

Location:

CLAUDE.md, lines 42–52, 85–103.

Current source census by grep in chapters/ and appendices/: 746 ProvedHere, 333 ProvedElsewhere, 95 Conjectured, 23 Heuristic (fresh count from source tree).

Internal source examples where theorem/proposition labels and open-conjecture indexing do not cleanly match status propagation.

Severity: MEDIUM

Diagnosis:
This is not cosmetic. A claim-status system in a monograph of this size is part of its mathematical infrastructure.

CLAUDE.md says “ALL PROVED” for A–D and lists census numbers (731 / 333 / 101 / 21) that do not match the current source-tree counts. More importantly, the source still contains proved-here definitions incorporating conjectural ingredients, and some open conjecture indexing is not synchronized with the actual theorematic boundary.

When the claim-status layer is not fully trustworthy, a referee will trust it not at all.

Resolution:
Do one global pass whose sole purpose is claim-status normalization:

Every \ClaimStatusProvedHere item must be theorematically independent and have a complete proof in-source.

Definitions that contain conjectural data must not be tagged as proved.

Recompute the census mechanically at build time and print it automatically.

Separate “foundational conjectures,” “conditional theorems,” and “physics horizon conjectures.”

This is a medium issue by itself, but it amplifies every other issue.

2. Structural / Architectural
Finding 9. The dependency graph still has unnecessary cycles, and this is now an architectural defect, not just a local one

Location:
Global; concretely:

def:chiral-koszul-pair ↔ Theorem A,

def:modular-koszul-chiral ↔ Theorem B/C,

example-verification propositions ↔ those same theorems.

Severity: HIGH

Diagnosis:
A long monograph stands or falls by whether its proof graph is acyclic and trustworthy. Right now it is not.

The manuscript has done a lot of hard work to fix local mathematics, but it still has an architectural pattern of:

introducing a definition that already contains the conclusion of a later theorem,

then proving the theorem from the definition,

then using the theorem to verify examples satisfy the definition.

That is not just a local error repeated twice; it is a book-level design problem.

Resolution:
Reorganize the proof graph into four layers:

Foundations: configuration spaces, bar/cobar, Verdier duality, filtered/curved/coderived frameworks.

Recognition criteria: independent criteria for chiral Koszulity / modular pre-Koszulity.

Main theorems: A, B, C, D proved from the criteria.

Examples and programmes: verify hypotheses for examples; then apply A–D.

Until that reorganization is done, the manuscript is mathematically harder to trust than it needs to be.

Finding 10. The current three-part decomposition still mixes proved mathematics and programme mathematics too tightly

Location:
Overall architecture, especially the transition from theory chapters into the long examples / connections sections; see contents of the current PDF, Parts I–III.

main

Severity: MEDIUM

Diagnosis:
The three-part split (Theory / Examples / Connections) is broadly right, but the present execution does not sufficiently separate:

theorematic core,

example verification,

programme-level mathematical physics.

The consequence is that the reader has to keep checking whether a given later statement is:

a proved theorem,

a conditional theorem,

a tested example,

or a research programme claim.

This burden is too high.

Resolution:
I would strongly recommend splitting the book conceptually into:

Core Monograph: Foundations + A–D + verified examples.

Research Programme Volume / Part IV: BV-BRST, holography, path-integral, higher-dimensional and boundary/defect programmes.

If the author wants one volume, then a minimum fix is to make the “programme” chapters typographically and theorematically distinct, with their own claim-status conventions.

3. Expository / Mathematical Writing
Finding 11. The notation is still too unstable exactly where the mathematics is most delicate

Location:
Global, especially Chapters 6, 8, 11, and the introduction.

Severity: MEDIUM

Diagnosis:
This is not a formatting complaint. It is a serious mathematical-writing complaint.

The manuscript’s main novelty concerns:

curved vs strict differentials,

scalar shadow vs full
Θ
𝐴
Θ
A
	​

,

bar/cobar existence vs inversion,

Koszul pair vs modular Koszul object.

Those distinctions must be legible instantly. They still are not. The current notation and theorem statements force the reader to infer from context which exact object is being discussed.

This contributed directly to the cross-chapter contradictions above.

Resolution:
Add and enforce a global mathematical dictionary near the beginning:

𝐵
ˉ
B
ˉ
,
Ω
Ω: constructions only,

𝜓
ψ: counit map,

𝜅
κ: scalar genus-1 curvature coefficient,

Θ
𝐴
Θ
A
	​

: conjectural non-scalar universal class,

“Koszul pair”: recognition hypothesis,

“modular pre-Koszul”: higher-genus hypothesis,

“modular Koszul”: theorematic conclusion, if that term is retained at all.

Then source-audit all later chapters so every theorem uses the canonical dictionary.

4. Scope and ambition calibration
Finding 12. The 94/95+ conjecture apparatus is not the main problem, but it is currently organized in a way that weakens the core

Location:
Whole manuscript; especially CLAUDE.md and the horizon/programme chapters.

Severity: MEDIUM

Diagnosis:
The problem is not “too many conjectures.” The problem is that the conjectures are not stratified by dependency.

Some conjectures are:

one theorem away from the current core,

some are serious but plausible extensions,

some are long-range mathematical physics horizons.

Putting them in one rhetorical layer makes the book feel less secure than it really is.

Resolution:
Create three conjecture classes:

Foundational next-step conjectures
(e.g. full
Θ
𝐴
Θ
A
	​

, one flagship higher-genus PBW degeneration, full DK extension);

Consequence conjectures
that depend on the foundational ones;

Physics horizon conjectures
(BV/bar identity, holographic dictionary, path-integral realization, etc.).

This would make the book feel leaner and stronger without reducing ambition.

Part II. Constructive — the strike list

These are the highest-leverage mathematical moves I would recommend now.

Strike 1. Refactor the definitions so Theorems A and B become actual theorems

The action:
Replace the current definitions of “chiral Koszul pair” and “modular Koszul chiral algebra” by antecedent recognition criteria that do not already include the content of Theorems A/B/C.

Why it’s high-leverage:
This repairs the two most serious referee-level defects in one move and restores integrity to the entire theorem graph.

Feasibility:
1 week

Where it lives:
chapters/theory/chiral_koszul_pairs.tex, chapters/theory/higher_genus.tex, introduction.

Mathematical argument sketch:
Use a twisting-morphism/Koszul-complex recognition criterion modeled on Loday–Vallette’s “twisting morphism fundamental theorem,” where acyclicity of a twisted composite/tensor product implies both the bar identification and the cobar quasi-isomorphism. The chiral version should take:

a candidate dual coalgebra,

a canonical twisting morphism,

acyclic twisted tensor product,

and PBW/diagonal-Ext concentration,
and then conclude A/B.

Strike 2. Prove a genuine bar concentration theorem for chiral Koszul pairs

The action:
Add an explicit theorem that the augmented geometric bar complex is acyclic off degree
0
0, with
𝐻
0
H
0
 identified with the dual coalgebra.

Why it’s high-leverage:
It fixes the false citation in Theorem A and gives the book a proper genus-zero homological backbone.

Feasibility:
3–7 days

Where it lives:
Immediately before or inside the proof package for Theorem A.

Mathematical argument sketch:
Filter the chiral bar complex by pole order / conformal weight, identify the associated graded with the operadic or classical quadratic Koszul complex, invoke diagonal concentration there, and lift by spectral sequence. This is exactly the sort of step the current proof gestures at but does not supply.

Strike 3. Repair Theorem C by proving total fiber-cohomology concentration

The action:
Strengthen Lemma lem:fiber-cohomology-center to a theorem about the full fiber complex, not just the degree-0 bar component.

Why it’s high-leverage:
It stabilizes the strongest genuinely distinctive theorem in the book.

Feasibility:
1 week

Where it lives:
chapters/theory/higher_genus.tex, Step II/III of complementarity.

Mathematical argument sketch:
Use a bar-degree filtration and compare to a Koszul/Ext complex. Show that only total degree
0
0 survives, not merely degree
0
0 in one bar component. Then the center local system is truly the full fiber cohomology sheaf.

Strike 4. Unify the Hochschild-duality story into one object-level theorem

The action:
Delete the competing corollary/theorem formulations and replace them with one object-level duality theorem plus explicit corollaries.

Why it’s high-leverage:
It removes an obvious contradiction and clarifies all later deformation/cyclic material.

Feasibility:
1–3 days

Where it lives:
deformation_theory.tex, higher_genus.tex, hochschild_cohomology.tex.

Mathematical argument sketch:
State

𝑅
𝐻
𝐻
c
h
i
r
a
l
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
i
r
a
l
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
,
RHH
chiral
	​

(A)≃RHom(RHH
chiral
	​

(A
!
),ω
X
	​

[2]),

then deduce the degree-level formulas after fixing the bigrading convention once and for all.

Strike 5. Prove one flagship higher-genus PBW degeneration theorem

The action:
Choose one nontrivial interacting family — generic affine Kac–Moody is the best target — and prove the genus-
𝑔
g PBW spectral sequence degenerates at
𝐸
2
E
2
	​

.

Why it’s high-leverage:
It would convert a large conditional swath of the monograph into unconditional mathematics.

Feasibility:
1 month for a robust result; 1 week for a serious first case such as generic
𝑠
𝑙
^
2
sl
2
	​

.

Where it lives:
higher_genus.tex plus the Kac–Moody example chapter.

Mathematical argument sketch:
Use conformal-weight filtration, identify the associated graded with the genus-0 PBW/Verma/BGG complex, and kill higher differentials by generic irreducibility / character comparison. Even a good rank-one theorem would materially upgrade the book.

Strike 6. Split Theorem D into scalar theorem + non-scalar programme

The action:
Rewrite Theorem D as the scalar modular characteristic theorem and move the full
Θ
𝐴
Θ
A
	​

 story into a clearly labeled conjectural extension.

Why it’s high-leverage:
It makes the book mathematically honest without sacrificing ambition.

Feasibility:
1–2 days

Where it lives:
Introduction, Chapter 8/34, master tables.

Mathematical argument sketch:
The scalar sector is already there:

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
.
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

−1).

Package that as the theorem. Present
Θ
𝐴
Θ
A
	​

 as the conjectural enhancement controlling clutching, trace, and Verdier compatibility.

Strike 7. Do a global “claim-status propagation” pass

The action:
Normalize the entire source so the theorem/conjecture/proved-elsewhere/proved-here layer is globally consistent.

Why it’s high-leverage:
Right now the book’s own internal status-control system is not fully trustworthy. Fixing this will significantly increase referee confidence.

Feasibility:
3–5 days

Where it lives:
Whole source, but especially introduction, summary theorems, master tables, example chapters.

Mathematical argument sketch:
This is editorial-mathematical rather than creative mathematics, but it is high leverage: every theorem or definition involving conjectural data must be retagged; every example proposition must verify hypotheses, not conclusions; the census should be generated mechanically.

Strike 8. Prove one low-order piece of the universal Maurer–Cartan class

The action:
Construct and prove compatibility of the first nontrivial components of
Θ
𝐴
Θ
A
	​

, rather than leaving the entire object conjectural.

Why it’s high-leverage:
This would transform the book’s conceptual capstone from slogan to mathematics.

Feasibility:
1 month

Where it lives:
Chapter 34 / higher-genus theory.

Mathematical argument sketch:
Build the first Taylor components of
Θ
𝐴
Θ
A
	​

 from the already-constructed genus-one curvature, clutching maps, and cyclic deformation complex. Prove:

scalar trace recovers
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

first compatibility with clutching,

first compatibility with Verdier duality.
That would already justify a large fraction of the rhetoric around the modular package.

Final verdict

The updated manuscript is better than earlier versions. The complementarity theorem is much stronger than it was; the author has clearly done serious and difficult repair work. But the current source still contains defects that a top-tier referee will treat as fatal:

Theorem A is still definitional.

Theorem B is still definitional/circular through the modular-Koszul definition.

Theorem C still depends on an underproved fiber-cohomology lemma.

The manuscript still contradicts itself about whether bar–cobar inversion holds for any chiral algebra.

The Hochschild-duality package is still inconsistent.

Those are not “could be better.” They are “must be fixed.”

If those are repaired, I think the book could become a genuinely important monograph. If they are not, the current claim that “all four main theorems are proved” is not mathematically defensible.
