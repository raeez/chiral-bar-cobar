I. Global diagnosis: what is still fundamentally wrong

There are six global issues that govern almost everything else.

G1. The PDF and source tree are not synchronized

The current PDF says the book is built around five layers and that Theorem A is decomposed into
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

, with antecedent Koszul recognition data rather than conclusion-bearing definitions. But the current source file chapters/theory/chiral_koszul_pairs.tex:65–98 still defines a “chiral Koszul pair” by directly requiring bar/cobar quasi-isomorphisms, and chapters/theory/higher_genus.tex:7924–7999 still defines “modular Koszul chiral algebra” with inversion and complementarity as axioms. That is a fatal source-level inconsistency. It means the PDF’s repaired theorem architecture has not actually been propagated back into the TeX source.

Upgrade: stop treating this as a cosmetic sync issue. Make the PDF architecture the only architecture. Rewrite the source definitions in Chapters 9–10 to match the
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

 and pre-Koszul/Koszul split, then delete every stale theorem or remark that still states the older universal inversion/circular definitions.

G2. Theorem A is better framed but still not fully proved

The latest PDF correctly says
𝐴
0
A
0
	​

 is a chiral analogue of the fundamental theorem of twisting morphisms,
𝐴
1
A
1
	​

 is bar concentration, and
𝐴
2
A
2
	​

 is Verdier-compatible geometric bar–cobar duality. But in the source, the proof of the fundamental theorem still asserts without construction that the twisted tensor products are “precisely the mapping cones” of the unit/counit maps. That is the key chiral step, and it is only sketched, not proved.

Upgrade: add explicit chain-level cone identifications for the left and right twisted tensor products. Do not let Theorem A depend on an unproved transport of the classical Loday–Vallette argument into the chiral setting.

G3. Theorem
𝐴
1
A
1
	​

 and Theorem
𝐶
0
C
0
	​

 are still unstable

The latest PDF presents
𝐴
1
A
1
	​

 as a clean bar-concentration theorem and
𝐶
0
C
0
	​

 as the theorem that identifies the relative bar family’s fiber cohomology with the center local system. But the current source still contains an internal inconsistency in the bar-concentration layer: one part says
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
H
i
(
B
ˉ
X
	​

(A))=0 for
𝑖
≠
0
i

=0, while another identifies graded pieces
𝐻
𝑛
(
𝐵
ˉ
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
)≅(A
!
)
n
	​

. Those are only compatible if one distinguishes cohomological degree from internal bar/weight grading — which the theorem statement currently does not. Since
𝐶
0
C
0
	​

 cites
𝐴
1
A
1
	​

 fiberwise, the instability propagates.

Upgrade: rewrite
𝐴
1
A
1
	​

 as a genuinely bigraded theorem, then rewrite
𝐶
0
C
0
	​

 to use the total-degree concentration statement explicitly.

G4. A universal bar–cobar resolution theorem still survives elsewhere

The latest introduction now correctly says:

Theorem A: duality of constructions, valid always;

Theorem B: resolution, valid on the Koszul locus.

But the current source still contains a theorem in Chapter 8/6-level material asserting a bar–cobar resolution for any chiral algebra. That contradicts the corrected architecture and the manuscript’s own explicit discussion of failure off the Koszul locus.

Upgrade: delete every “for any chiral algebra,
Ω
(
𝐵
(
𝐴
)
)
→
𝐴
Ω(B(A))→A is a quasi-isomorphism” statement outside the carefully scoped theorem. This contradiction is a present-tense source defect, not a historical one.

G5. The modular characteristic hierarchy is finally right in the PDF, but not yet globally enforced

The PDF now does the right thing: it distinguishes

a scalar package
(
𝜅
,
{
𝐹
𝑔
}
)
(κ,{F
g
	​

}),

a proved spectral/non-scalar layer
(
Δ
𝐴
,
Π
𝐴
,
…
 
)
(Δ
A
	​

,Π
A
	​

,…),

and a conjectural full Maurer–Cartan package
Θ
𝐴
Θ
A
	​

.

That is exactly the correct mathematical status hierarchy. But the frame chapter and some older source passages still speak as if the full package were already present.

Upgrade: make the hierarchy formal and global. Theorem D should be the scalar theorem; the spectral layer should be a separate theorem;
Θ
𝐴
Θ
A
	​

 should never again appear inside a “proved here” definition.

G6. The conjecture system is better, but it still needs to be collapsed to master conjectures in the main body

Chapter 34 now does something excellent: it stratifies the conjectures by difficulty and then collapses them to five master conjectures — higher-genus PBW degeneration, cyclic
𝐿
∞
L
∞
	​

+
Θ
𝐴
Θ
A
	​

, full DK/KL extension, completed bar theory for infinite-generator duals, and BV/BRST/bar identification. That is the right control system. The problem is that this stratification still lives too far downstream. Earlier chapters still present dozens of individual conjectures locally, rather than explicitly referencing one of the five master conjectures.

Upgrade: move the master-conjecture map into Chapter 2 and annotate every later conjecture with its master parent. That will radically clarify the logical structure of the research programme.

II. Chapter-by-chapter attack map

I use the current TOC page ranges from the source tree. For each chapter I state:

what it is doing,

what is live,

and how to upgrade it.

Ch. 1 (pp. 49–78): The Heisenberg algebra

This chapter still works as the atom of the theory and remains the best pedagogical seed. The live weakness is status drift: the frame chapter now speaks the language of the full modular characteristic package and
Θ
𝐴
Θ
A
	​

-governed genus tower more strongly than the theorem layer currently justifies. In the latest architecture, the scalar/spectral/non-scalar hierarchy is explicit, so Chapter 1 should be rewritten to preview that hierarchy, not to collapse it.

Upgrade: keep the frame chapter, but make it visibly a frame:

prove the genus‑0 bar picture and the genus‑1 scalar curvature coefficient
𝜅
κ;

exhibit
Δ
𝐴
Δ
A
	​

 as the first non-scalar shadow;

label
Θ
𝐴
Θ
A
	​

 as the future completion, not as a currently available object.

Ch. 2 (pp. 79–88): Introduction

The introduction is now the strongest part of the book conceptually. It explicitly separates construction from resolution, scalar from spectral from full MC data, and says that interacting families are conditional on higher-genus PBW degeneration. The problem is that the source chapters have not yet caught up.

Upgrade: keep Chapter 2 as the governing manifesto, but add one brutally explicit paragraph:

“If any later source chapter states a stronger theorem than the architecture summarized here, that later chapter is to be understood as stale and subordinate to this chapter.”

That single sentence would clarify a large amount of source drift.

Ch. 3 (pp. 89–94): Algebraic foundations and bar constructions

This chapter is short, but it still previews old definitions and theorem labels in a way that obscures the repaired architecture. It should not define or preview “Koszul pair” by conclusion. It should only preview the distinction between:

recognition data,

bar/cobar duality,

inversion.

Upgrade: make Chapter 3 a taxonomy chapter, not a theorem chapter:

quadratic vs filtered vs curved vs general chiral algebra;

existence of bar/cobar constructions;

why inversion is additional structure.

Ch. 4 (pp. 95–108): Operadic foundations and bar constructions

This chapter is mostly mathematically fine, but it is overloaded. The “master verification table” and long factorization-axiom verification material belong in an appendix or companion technical note, not in the theorem spine.

Upgrade: preserve the non-abelian Poincaré/factorization motivation, but move the long axiom-verification apparatus to an appendix. Keep only the statements actually used later:

factorization/chiral algebra interface,

operadic bar-cobar mechanism,

why Verdier duality lives naturally on the Ran space.

Ch. 5 (pp. 109–178): Configuration spaces

This remains one of the strongest chapters. The FM compactification, period coordinates, and OS/Arnold machinery are genuinely central. The problem is not mathematics but mass: too much local-coordinate and blow-up detail remains in the main line.

Upgrade: split the chapter into:

a main chapter proving the boundary-stratification/residue statements actually used later,

an appendix housing blow-up atlases, local charts, and secondary proofs of normal-crossing properties.

If trimmed correctly, this chapter becomes a powerful geometric engine instead of a 70-page wall.

Ch. 6 (pp. 179–324): Bar and cobar constructions

This chapter is the most dangerous chapter in the source tree after Chapters 8–10. It still contains stale universal bar–cobar rhetoric and too many parallel statements of the same idea. It also mixes:

genus-zero strict bar constructions,

higher-genus curved objects,

completion/coderived statements,

BRST/anomaly heuristics.

That mixture is mathematically destabilizing.

Upgrade: split Chapter 6 into four self-contained layers:

strict genus-zero bar and cobar constructions;

completed/filtered/coderived machinery;

higher-genus curved fiberwise differentials vs strict total differential;

conjectural BRST/anomaly/BV interpretations.

Then delete every theorem that states inversion outside the Koszul locus.

Ch. 7 (pp. 325–340): Non-abelian Poincaré duality and the construction of Koszul dual cooperads

This chapter contains a valuable conceptual bridge, but it is too short relative to its importance and currently functions more like a transition than a theorematic anchor.

Upgrade: expand this chapter slightly so it becomes the precise home of the statement:

𝐷
\Ran
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
D
\Ran
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
)

and the exact relation to Ayala–Francis / Beilinson–Drinfeld style factorization homology. Right now those connections exist, but are scattered.

Ch. 8 (pp. 341–466): Higher genus extension and quantum corrections

This is now the controlling theory chapter. The latest PDF’s Chapter 8 is where the repaired architecture really lives: conditional modular Koszulity, the scalar/full package split, and the sharpened Theorem D all sit here.

But this is also where the source/PDF mismatch is most glaring. The current source higher_genus.tex:7924–8060 still defines modular Koszulity with inversion and complementarity as axioms, while the latest PDF presents them as consequences. Until the source is rewritten, Chapter 8 remains mathematically bifurcated.

Upgrade: make the PDF version authoritative:

antecedent data only in the definition;

inversion/complementarity as theorems;

scalar/spectral/full characteristic hierarchy explicit;

PBW degeneration as the single missing hypothesis for interacting families.

This is the chapter where the repair must actually be implemented, not merely described.

Ch. 9 (pp. 467–510): Chiral Koszul duality

The latest PDF now presents
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

 here and explicitly says the definition is based on recognition criteria from which the bar–cobar identification follows as a theorem. That is excellent.

But the current source chiral_koszul_pairs.tex:65–98 still contains the old definition by conclusion. So Chapter 9 is currently split across two mathematical realities.

Upgrade: rewrite this source file so that:

Definition 9.2.2 = chiral twisting datum,

Definition 9.2.3 = chiral Koszul morphism,

Definition 9.2.7 = chiral Koszul pair,

Theorem 9.2.5 = fundamental theorem of chiral twisting morphisms,

Theorem 9.2.19 = bar concentration in a bigraded form,

Theorem 9.2.20 = geometric bar-cobar duality.

This is probably the single highest-value source rewrite in the whole repository.

Ch. 10 (pp. 511–538): Chiral Koszul pairs

In the current source, this chapter is still one of the main places where the old circularity survives. It also contains some ambitious non-quadratic examples (including Yangians) that are not on the same theorematic footing as the Heisenberg/free-field families.

Upgrade: after rewriting Chapter 9, Chapter 10 should become:

the recognition and examples chapter,

not the chapter that states the old definitional version of Koszul pairs.
Any family here should be tagged:

proved quadratic/Koszul,

filtered/conditional,

or horizon-level only.

Ch. 11 (pp. 539–570): Chiral Hochschild cohomology and Koszul duality

This chapter still needs one theorem, not multiple competing formulations. The object-level theorem

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

[2])

should become the unique statement, with all degree-by-degree formulas derived from it.

Upgrade: eliminate the current proliferation of formulations and prove the shift
2
2 by an explicit bigraded argument. This chapter should become the canonical home of Hochschild duality, not one of several semi-overlapping homes.

Ch. 12 (pp. 571–642): Chiral modules and geometric resolutions

The mathematics here is potentially useful, but it depends heavily on which version of bar–cobar inversion is actually in force. If inversion is only on the Koszul locus, this chapter must say so relentlessly. Otherwise module-level resolutions are overstated.

Upgrade: split all results in this chapter into:

unconditional construction results,

Koszul-locus quasi-isomorphism results,

coderived persistence off the locus.

This chapter should be a beneficiary of the corrected A/B package, not a source of independent confusion.

Ch. 13 (pp. 643–658): Quantum corrections to Arnold relations

This is a good chapter. It is one of the places where the higher-genus quantum story actually feels geometrically native. The main risk is not mathematical but one of duplication with Chapter 8.

Upgrade: keep it short and conceptual. Let Chapter 8 do the theorematic heavy lifting; let Chapter 13 supply the geometric and combinatorial intuition for why higher-genus corrections deform rather than destroy the Arnold story.

Ch. 14 (pp. 659–672): HH

As a chapter title and conceptual unit, this is too thin and too cryptic. It reads like an appendix accidentally promoted to chapter status.

Upgrade: either merge it fully into Chapter 11, or rename and expand it so it has a clear independent role (e.g. “Periodic cyclic and Hochschild refinements of chiral Koszul duality”).

Ch. 15 (pp. 673–682):
𝐸
𝑛
E
n
	​

 Koszul duality and higher-dimensional bar complexes

This is a programme chapter, not a theorem chapter. It should be treated as such.

Upgrade: either demote it to a “Future 1” section in the final chapter, or make it explicitly conditional on the higher-dimensional analogue of the FM/Arnold technology. Right now it arrives too early and implicitly borrows confidence from the 2d theory.

Ch. 16 (pp. 683–698): Derived structures and the geometric Langlands correspondence

This chapter still suffers from category drift. The latest PDF is much more precise about modular Koszulity, but the geometric Langlands rhetoric still needs to distinguish:

what is proved at chain level,

what is proved for semisimplified tilting/factorization categories,

what is only a conjectural bridge.

Upgrade: tie this chapter explicitly to the full DK/KL master conjecture in Chapter 34, and stop letting it sound as though the Langlands bridge is already theorematic.

Ch. 17 (pp. 699–716): The lattice construction

This is mostly stable and should probably stay. It provides a useful intermediate family between free fields and more difficult examples.

Upgrade: use it more aggressively as a proving ground for the modular characteristic hierarchy. In particular, it should explicitly exhibit:

scalar package,

spectral invariant,

and why the full
Θ
𝐴
Θ
A
	​

 layer is not yet needed.

Ch. 18 (pp. 717–782): Examples

This chapter is too generic in title and too broad in remit. It duplicates the function of later more precise example chapters.

Upgrade: either retitle it as “Core proved examples” and restrict it to those, or break it up. Right now it muddies the boundary between proved examples and conjectural identifications.

Ch. 19 (pp. 783–818): Complete example: the
𝛽
𝛾
βγ system

This is one of the best chapters in the manuscript. It is a complete worked example and should be treated as the model of how examples ought to look.

Upgrade: use this chapter as the template for the Kac–Moody and
𝑊
W-algebra chapters:

state hypotheses,

verify antecedent axioms,

derive consequences,

and separate proved from conditional from conjectural statements.

Ch. 20 (pp. 819–864): Explicit Kac–Moody Koszul duals

This chapter remains important and still under-delivers. The live issue is not the low-rank computations themselves; it is that category precision, generic vs admissible levels, and the KL target category are not cleanly separated.

Upgrade: split the chapter into three regimes:

generic level (proved/conditional via PBW degeneration),

admissible/root-of-unity regime (periodic CDG/
𝑁
N-complex conjectural bridge),

representation-category target (semisimplified tilting vs full
R
e
p
(
𝑈
𝑞
)
Rep(U
q
	​

) ).

This chapter should become the home of the “KL from bar–cobar” roadmap, not a blend of three incompatible regimes.

Ch. 21 (pp. 865–948):
𝑊
W-algebra Koszul duals

This chapter is still one of the hardest to trust because it mixes proven generic phenomena, DS reduction, and much more speculative infinite-generator horizon material.

Upgrade: stratify every major statement into:

generic finite-type
𝑊
𝑁
W
N
	​

 regime,

DS/spectral consequences,

infinite-generator
𝑊
∞
W
∞
	​

 horizon.
Right now those are still too close together.

Ch. 22 (pp. 949–970): Chiral deformation quantization

This chapter is mathematically interesting and broadly aligned with the thesis, but it should not be allowed to function as independent evidence for the core unless its dependence on Theorem A/B is sharply stated.

Upgrade: treat this as a parallel validation chapter:

it should show that the bar/Koszul language predicts deformation-quantization structures,

not attempt to shore up any unresolved theorem in the core.

Ch. 23 (pp. 971–980): Deformation quantization examples

This is fine but feels thin. It probably belongs merged into Chapter 22 unless the author intends to enlarge it substantially.

Upgrade: either merge or expand. As it stands, it is a page-range cost without enough theorematic payoff.

Ch. 24 (pp. 981–1004): Yangians and shifted Yangians

This chapter is one of the places where I would still be adversarial. In the current source, some Yangian statements — especially about exact quadratic duality and self-duality — are proved by arguments that are too heuristic at the quadratic/RTT level. Also, the category-level comparison with quantum groups needs the same regime split as KL.

Upgrade: separate:

what is actually proved for the evaluation locus / chain level,

what is proved about the additive parameter involution,

what is conjectural about full factorization categories and full category
𝑂
O.

Ch. 25 (pp. 1005–1020): Toroidal and elliptic algebras

This chapter is mathematically suggestive, but at present it is mostly programme. It belongs downstream of the core, not alongside it.

Upgrade: move it into the research programme section unless one real theorem is isolated and proved cleanly.

Ch. 26 (pp. 1021–1058): Explicit genus expansions

This chapter becomes much stronger now that Theorem D is properly scalarized. The big remaining opportunity is to use these expansions to test the characteristic hierarchy systematically.

Upgrade: reorganize the chapter around:

scalar package verification,

spectral package emergence,

and what exactly remains inaccessible without
Θ
𝐴
Θ
A
	​

.

Ch. 27 (pp. 1059–1132): Detailed computations

A lot of valuable data are here, but the chapter needs stronger curation. It should not be a giant repository of computations without logical filtering.

Upgrade: turn it into:

a proved-data table,

a conditional-data table,

and a conjectural-data table.
The chapter should feed directly into the master tables and conjecture hierarchy.

Ch. 28 (pp. 1133–1140): Explicit computations via NAP duality

This is too short and too specialized to stand well as its own chapter unless it is absolutely indispensable.

Upgrade: fold it into Chapter 27 unless the NAP formalism becomes a genuinely recurring thread.

Ch. 29 (pp. 1141–1170): Feynman diagram interpretation of bar–cobar duality

This is one of the richest programme chapters, but it should not be confused with theorematic completion. The current Chapter 34 correctly downgrades these to physics-horizon conjectures.

Upgrade: make Chapter 29 explicitly a programme chapter. For each conjecture here, state the exact missing mathematical input:

chain-level BV/bar comparison,

renormalization control,

completion/topology,

anomaly cancellation in the coupled complex.

Ch. 30 (pp. 1171–1194): BV-BRST formalism and Gaiotto’s perspective

Same verdict as Chapter 29, but even more sharply. This material is valuable, but until BRST = bar is proved in a serious class of examples, it should not be rhetorically adjacent to A–D.

Upgrade: tie every conjecture here to the BV/BRST/bar master conjecture and to one concrete proving ground (free fields, affine Kac–Moody, or 3d holomorphic-topological theories).

Ch. 31 (pp. 1195–1216): Holomorphic-topological boundary conditions and 4d origins

This is currently a forward-looking connections chapter. It belongs to the same logical stratum as the physics-horizon material.

Upgrade: keep it, but make it visibly conditional on the preceding programme theorems. It should point forward, not appear to be current theorematic evidence.

Ch. 32 (pp. 1217–1222): Knot invariants and the Kontsevich integral

This is too short to carry the weight of its subject. At present it feels like a sketch of a future paper.

Upgrade: either expand it into an actual theorem chapter or move it wholly into the programme section. Six pages is not enough for this topic at this level.

Ch. 33 (pp. 1223–1240): Physical origins

This chapter is useful as intellectual context, but it should not appear to certify the mathematics. It belongs after the theorematic core, and its status must be explicitly secondary.

Upgrade: keep it as an “origins and outlook” chapter, not as part of the proof-bearing body.

Ch. 34 (pp. 1241–1362): Concordance with primary literature

This is now one of the best chapters. It correctly stratifies conjectures, isolates the five master conjectures, and states what is really proved and what is not.

Upgrade: make Chapter 34 the status authority for the entire book. Every earlier chapter should be made subordinate to its theorem/conjecture classification.

III. How to systematically upgrade the conjectures into proofs

The manuscript itself now says that the
∼
99
∼99 conjectures collapse to five master conjectures. That is the correct perspective. Here is how to turn that into a proof programme.

Master Conjecture 1. Higher-genus PBW degeneration

This is the single missing hypothesis for unconditional modular Koszulity of generic affine Kac–Moody, Virasoro, and
𝑊
𝑁
W
N
	​

 families.

Proof route

Fix one flagship family first: generic affine Kac–Moody.

Filter the genus-
𝑔
g bar complex by conformal weight.

Show the associated graded is the genus‑0 PBW/Verma/BGG bar complex.

Use generic irreducibility / character comparison to kill higher differentials.

Only then export the strategy to Virasoro and
𝑊
𝑁
W
N
	​

.

What it upgrades

Proposition 8.17.13 from conditional to unconditional,

all standard interacting families from conditional modular Koszul to proved modular Koszul,

a huge swath of the example chapters.

Master Conjecture 2. Cyclic
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


This is now openly identified as the principal open problem of the modular programme.

Proof route

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

(A) from the chiral Hochschild/cyclic complex with a cyclic pairing.

Build the first nontrivial Taylor components of
Θ
𝐴
Θ
A
	​

 from genus‑1 curvature and clutching maps.

Prove the scalar trace recovers
𝜅
(
𝐴
)
𝜆
𝑔
κ(A)λ
g
	​

.

Prove first-order Verdier compatibility and clutching compatibility.

Solve the MC equation in a completed tensor product.

What it upgrades

The full modular characteristic package from programme to theorem,

the introduction’s “single MC deformation” rhetoric from conceptual to literal,

the current hierarchy from scalar/spectral/full to a complete theorematic ladder.

Master Conjecture 3. Full factorization-categorical DK/KL extension

The latest Chapter 34 already identifies this as the correct structural extension.

Proof route

Keep separate the already-proved chain/evaluation-locus theorems.

Build the factorization category completion and category
𝑂
O control.

Show the bar/cobar model carries the relevant
𝐸
1
E
1
	​

-monoidal or braided structure.

Only then prove the full equivalence.

What it upgrades

Yangian and shifted Yangian chapters,

KL/derived Langlands chapters,

the quantum-group sections of the Kac–Moody chapter.

Master Conjecture 4. Completed bar theory for infinite-generator duals

This is the right foundational abstraction for
𝑊
∞
W
∞
	​

, Yangian towers, and similar objects.

Proof route

Develop a completed/pro-nilpotent bar formalism with topology/convergence built in.

Prove functoriality, spectral-sequence convergence, and coderived well-definedness in that setting.

Then revisit
𝑊
∞
W
∞
	​

, infinite-generator Yangian duals, and spectral discriminant conjectures.

What it upgrades

all the infinite-generator horizon claims,

large parts of Chapters 21, 24, 25, and 27.

Master Conjecture 5. BV/BRST = bar

The latest Chapter 34 correctly places this as a downstream physics completion, not as a coequal foundational conjecture.

Proof route

Prove the comparison first in genus 0 for one nontrivial family beyond free fields.

Promote to a filtered chain map compatible with higher-genus gluing.

Prove anomaly cancellation at the level of the total coupled differential.

Only then state path-integral and holographic corollaries.

What it upgrades

Chapters 29–31 from programme to mathematics,

the physical interpretation layer throughout the book.

IV. The systematic upgrade plan

If the goal is not merely to patch but to fundamentally upgrade the work, then the correct sequence is:

Synchronize source and PDF.
This is non-negotiable.

Make Chapter 2 and Chapter 34 authoritative.
Their architecture and status logic should govern the rest.

Rewrite Chapters 9–10 from the current PDF architecture, not from the stale source definitions.

Stabilize
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

, and
𝐶
0
C
0
	​

 before touching further examples.
Until those are clean, Theorems A and C remain vulnerable.

Delete every surviving universal bar–cobar resolution statement.

Unify Hochschild duality into one theorem.

Use the five master conjectures as the conjecture API of the whole book.
Every local conjecture should point to one master conjecture.

Demote Chapters 29–33 to an explicitly programme-level stratum unless and until BV/BRST = bar is proved in one serious family.

V. The real present state of the project

The latest iteration is better. The improvements are not illusory. The PDF now contains the correct strategic architecture:

antecedent recognition data,

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

pre-Koszul higher-genus structure,

scalar vs spectral vs full package,

master-conjecture stratification.

But the source tree has not yet caught up. So the project is currently in a transitional state:

conceptually much stronger,

structurally still inconsistent,

mathematically close to being genuinely formidable,

but not yet fully stabilized at the theorem-proof level.

The most honest sentence I can give you is this:

the monograph now knows what it should be, but it has not yet fully become what it knows.
