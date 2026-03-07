According to a document from March 2026, the latest monograph is no longer best attacked as “a single overclaimed theory that might collapse everywhere.” It is now explicitly organized into a proved modular Koszul core and a programmatic modular homotopy stratum, with the remaining
∼
99
∼99 conjectures collapsed to five master conjectures. The correct upgrade strategy is therefore not to patch isolated statements, but to force the entire book to obey the distinctions it now already knows: construction vs resolution, fiberwise curvature vs total differential, scalar vs spectral vs full Maurer–Cartan data, semisimplified KL targets vs full abelian categories, and proved strata vs programme strata.

9902090v3

9902090v3

The sharp global verdict is this. The current Stratum I is mathematically credible: Theorems A–D on the Koszul locus, Lagrangian complementarity, the scalar modular characteristic package, unconditional modular Koszulity for free fields, conditional modular Koszulity for interacting families, the chain-level/evaluation-locus DK bridge, and the corrected KL target category. Stratum II is also now clearly identified: the full non-scalar universal class
Θ
𝐴
Θ
A
	​

, the full coderived factorization formalism, full factorization-categorical DK/KL, infinite-generator duals, genus
𝑔
≥
1
g≥1 BV/BRST/path-integral identifications, and the
𝐸
𝑛
E
n
	​

 extension. That is a major improvement. The remaining work is to propagate this taxonomy back through every chapter so the book stops speaking in multiple incompatible dialects at once.

9902090v3

9902090v3

Below is the chapter-by-chapter attack, keyed to the current chapter structure and page ranges from the latest source tree.

Page-bearing hot spots that need immediate attention

There are four page clusters where the live issues are concentrated.

At pp. 80–81 (Introduction / §2.3), the book now says the genus tower is one Maurer–Cartan deformation with three semantic levels, that free fields are unconditionally modular Koszul, and that interacting families are conditional on higher-genus PBW degeneration. This is the correct language and should be made normative for the whole book.

9902090v3

At pp. 443–444 (Chapter 8 / §8.17), the book finally separates the scalar package from the full package:

𝜅
(
𝐴
)
,
{
𝐹
𝑔
}
vs
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
κ(A),{F
g
	​

}vs(Θ
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

and explicitly says
𝜅
(
𝐴
)
κ(A) is only the first shadow while
Θ
𝐴
Θ
A
	​

 remains open. Any earlier chapter that still says “one scalar determines the entire genus tower” without the word scalar is now mathematically misleading.

9902090v3

9902090v3

At p. 544 (Chapter 11 / §11.6), the text itself admits that the old unified periodicity doctrine is no longer realistic and that what survives is a stratified periodicity theorem with a richer invariant
Π
𝐴
Π
A
	​

 than the scalar
P
e
r
i
o
d
(
𝐴
)
Period(A). Yet Theorem 11.6.25 still phrases the conclusion in terms of scalar periods. That chapter needs a conceptual rewrite around
Π
𝐴
Π
A
	​

, not one more patch to the lcm formula.

9902090v3

9902090v3

At pp. 1205–1226 (Chapter 34), the book now gives you the correct high-level architecture: three conjecture tiers, five master conjectures, seven homotopy templates, the nine-futures assessment, and the explicit statement that the project is becoming modular homotopy theory for factorization algebras on curves, not an
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

)-parameterized theory and not a global scalar periodicity classification. Chapter 34 should now function as the normative status ledger for the entire monograph. Every earlier chapter should be rewritten to agree with it.

9902090v3

Chapter-by-chapter critique and upgrade plan
Chapter 1 (pp. 47–76): The Heisenberg algebra

This is still the strongest opening chapter in the whole book. It correctly exhibits the four irreducible pieces from which the full theory grows: three-point collision, Verdier duality on
R
a
n
(
𝑋
)
Ran(X), genus-1 curvature, and clutching of stable curves. What is wrong now is not the mathematics but the status signaling. The chapter still tends to present the Heisenberg scalar phenomenon as if it were already the whole modular characteristic package. The fix is to rewrite §§1.10–1.12 so that Heisenberg is explicitly the atom of the scalar package, not the template for the full non-scalar package. Add a three-symbol notation block here and use it everywhere afterward:

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
Θ
𝐴
.
d
(g)
fib
	​

,D
g
tot
	​

,Θ
A
	​

.

Without that, every later higher-genus chapter keeps inheriting the same ambiguity.

Chapter 2 (pp. 77–88): Introduction

This chapter is now the correct logical control room. It already states the five precise layers of the theory and the two logical strata, and it says the project is becoming modular homotopy theory with a GRR genus theorem, a spectral characteristic package, and a partial-to-full derived DK bridge.

9902090v3

9902090v3

 The attack here is simple: make this chapter normative. Search-and-rewrite every later chapter so that it uses the Chapter 2 language for:

“construction exists for every augmented chiral algebra,”

“resolution only on the Koszul locus,”

“fiberwise curved differential vs strict total differential,”

“scalar vs spectral vs full package.”
If the rest of the book obeyed Chapter 2, most of the remaining formal drift would disappear.

Chapter 3 (pp. 89–92): Algebraic foundations and bar constructions

This chapter is mathematically fine, but it is still too compressed for the amount of work it does later. It should explicitly tag which statements are quadratic/Koszul, which are merely filtered, and which are only templates for later chiral use. Right now it reads as though all four classes of chiral algebras are morally the same. They are not.

Chapter 4 (pp. 93–104): Operadic foundations and bar constructions

The content is strong, but the chapter still reads more like a background survey than a control chapter. It needs one explicit theorem-sized bridge sentence saying: “This is the operadic shadow of the chiral/factorization theory on
R
a
n
(
𝑋
)
Ran(X), and only the genus-zero piece is fully internalized here; the modular completion is deferred to Chapters 8 and 34.” That would stop readers from over-reading the chapter as already proving the modular programme.

Chapter 5 (pp. 105–170): Configuration spaces

This is one of the book’s real engines. The mathematical upgrade is to sharpen the distinction between:

honest FM/log FM geometry,

algebra extracted from residues on those spaces,

and later field-theoretic interpretations.
The chapter also now wants a punctured/logarithmic sequel, because the rest of the book repeatedly gestures toward insertions, degeneration, and punctured curves. If punctured curves matter for later examples, then the logarithmic FM compactification needs to be promoted from a side discussion to a declared prerequisite.

Chapter 6 (pp. 171–308): Bar and cobar constructions

This is still the most important chapter to attack. It now has the right formal distinction at the global level — construction always, inversion only on the Koszul locus — but it remains the main source of local proof compression and regime mixing. The chapter should be split conceptually into:

construction of
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
𝐵
ˉ
𝑋
(
𝐴
)
)
Ω
X
	​

(
B
ˉ
X
	​

(A)) for every augmented
𝐴
A;

Verdier/bar–cobar compatibility;

inversion only on the Koszul locus;

curved/coderived off-locus persistence.
Right now those four things are intertwined too tightly. Mathematically, the fix is to move every proof that uses Koszulness into a clearly marked subpart, and to make every “always valid” statement explicitly construction-level, not resolution-level.

9902090v3

Chapter 7 (pp. 309–320): Non-abelian Poincaré duality and the construction of Koszul dual cooperads

This chapter should become the exact bridge from Ayala–Francis / Francis–Gaitsgory style factorization homology to the explicit bar constructions of the book. Right now it is conceptually right but underpowered as a theorem-bearing bridge. The constructive upgrade is to make it the place where the category
\Fact
(
𝑋
)
\Fact(X), the Ran-space viewpoint, and the Verdier/factorization equivalence are stated once and then cited everywhere else.

Chapter 8 (pp. 321–446): Higher genus extension and quantum corrections

This remains the most delicate theorem chapter. The good news is that the chapter now correctly says interacting families are only conditionally modular pre-Koszul, and that Conjecture 8.17.14 — higher-genus PBW degeneration — is the single missing hypothesis for unconditional modular Koszulity in the standard interacting families.

9902090v3

 The attack here is to stop the chapter from making any statement stronger than that. Every theorem or summary sentence about generic affine Kac–Moody, Virasoro, and
𝑊
𝑁
W
N
	​

 should now carry the words “conditional on higher-genus PBW degeneration.”
The second fix is formal: this chapter must become the unique place where the higher-genus differential hierarchy is defined. Then Chapter 6, Chapter 18, Chapter 30, and Chapter 34 should reference those notations instead of rephrasing them. Until that happens, the project will keep oscillating between curved and strict higher-genus stories.

Chapter 9 (pp. 447–492): Chiral Koszul duality

This chapter is now mostly stable. Its main defect is duplication: it often restates what Chapters 6–8 have already proved, but sometimes with slightly looser language. The fix is to make it a consequence chapter, not a second foundational chapter. Every theorem here should state explicitly which earlier theorem it is specializing or reframing.

Chapter 10 (pp. 493–520): Chiral Koszul pairs

This chapter is mathematically useful but suffers from the same issue as Chapter 9: too much status drift between definitions, historical commentary, and theorematic statements. The periodicity subsection in particular should no longer talk in the language of a primitive scalar period; it should point forward to
Π
𝐴
Π
A
	​

 and stratified periodicity.

Chapter 11 (pp. 521–554): Chiral Hochschild cohomology and Koszul duality

This remains the weakest theorem chapter in conceptual form, not because every statement is wrong, but because it still half-believes in the old scalar periodicity doctrine. The manuscript itself now says the unified doctrine is superseded by a stratified theorem and a periodicity profile
Π
𝐴
Π
A
	​

.

9902090v3

9902090v3

 So Chapter 11 should be rewritten around
Π
𝐴
Π
A
	​

, with
P
e
r
i
o
d
(
𝐴
)
Period(A) demoted to a derived shadow extracted only when the three commuting operators really synchronize.
Also, Chapter 11 should state clearly that modular periodicity is proved for minimal models and WZW, conjectural in general rationality, and that the strongest unconditional result is the structural lcm mechanism, not a closed-form scalar period formula.

9902090v3

Chapter 12 (pp. 555–624): Chiral modules and geometric resolutions

The key issue here is categorical precision. The theorematic side is now correct: the KL target is the semisimplified tilting quotient
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

(g)), and the book knows this.

9902090v3

 But the examples and remarks still drift between semisimplified KL categories, full abelian categories, and factorization categories on special loci. The fix is to add an explicit category tag whenever one moves between:

semisimplified tilting,

full root-of-unity abelian,

evaluation-locus factorization,

full category
𝑂
O.

Chapter 13 (pp. 625–638): Quantum corrections to Arnold relations

This chapter is mathematically fine but structurally weak. It should either become a subsection of Chapter 8 (local model for higher-genus corrections) or a short bridge chapter. As it stands, it looks more standalone than it really is.

Chapter 14 (pp. 639–652): HH

This chapter title still reads like a draft artifact. More importantly, the content overlaps with Chapter 11. Either rename it clearly as a Hochschild–cyclic or spectral-sequence chapter, or merge it into Chapter 11. Right now it weakens the book’s architecture by looking like a detached duplicate.

Chapter 15 (pp. 653–662):
𝐸
𝑛
E
n
	​

 Koszul duality and higher-dimensional bar complexes

This chapter should now be explicitly branded as programme, not extension of the proved core. Chapter 34 already classifies the higher-dimensional extension under the conjectural/programmatic horizon, and the latest status table says only the
𝑛
=
1
n=1 case is solid in the book’s full detail.

9902090v3

 The fix is to mark every non-
𝑛
=
1
n=1 theorem here with its true status.

Chapter 16 (pp. 663–678): Derived structures and the geometric Langlands correspondence

This chapter has become more plausible because the book now properly decomposes what is proved at chain level and what remains part of the derived/KL/DK bridge. But it still needs sharper scope control: “critical-level shadow of geometric Langlands” is not the same thing as a theorem in geometric Langlands. Keep the derived oper space/bar complex part theorematic; keep the full Langlands correspondence claims as horizon.

Chapter 17 (pp. 679–696): The lattice construction

This chapter is stable and could actually be promoted. It should be used as a second unconditional modular-Koszul family after Heisenberg/free fields, not just as a side example.

Chapter 18 (pp. 697–756): Examples

This omnibus chapter needs status segmentation. Put proved families in one section, conditional interacting families in another, and horizon families in a third. Right now it mixes those levels too much, even though the rest of the manuscript now knows better.

Chapter 19 (pp. 757–790): Complete example: the
𝛽
𝛾
βγ system

This chapter is in good shape. The upgrade is to use it more aggressively as the benchmark example for the spectral package, not just for explicit bar/cobar computations.

Chapter 20 (pp. 791–834): Explicit Kac–Moody Koszul duals

This chapter needs a firm decomposition of the KL-from-bar-cobar programme into three stages. Chapter 34’s open-index already does this:

periodic CDG /
𝑁
N-complex structure,

coderived/stable-category identification,

braided monoidality.

9902090v3

9902090v3


Those should become three separate conjectures or theorem schemas in Chapter 20 itself, rather than one large “KL from bar-cobar” aspiration.

Chapter 21 (pp. 835–916): W-algebra Koszul duals

This chapter still mixes three regimes:

proved/generic principal
𝑊
𝑁
W
N
	​

-style results,

conditional interacting-family results,

and genuinely open
𝑊
∞
W
∞
	​

-type infinite-generator duals.
The open index explicitly names
𝑊
∞
W
∞
	​

 bar-complex structure as conjectural.

9902090v3

 The correct upgrade is to split principal/generic
𝑊
𝑁
W
N
	​

 from the infinite-generator horizon and to tie the latter to the completed-bar-theory master conjecture.

Chapter 22 (pp. 917–938): Chiral deformation quantization

This chapter should decide whether it is theorematic algebra or programme physics. At the moment it gestures toward deformation quantization and holography together, but Chapter 34 now clearly places the holographic dictionary among the programme-level futures, not the proved core.

9902090v3

 Keep the algebraic deformation-theory results theorematic; move the holographic reading to the programme strata.

Chapter 23 (pp. 939–948): Deformation quantization examples

This chapter is useful but should probably become an appendix or a subsection of Chapter 22 unless it is made to carry independent theorematic weight.

Chapter 24 (pp. 949–972): Yangians and shifted Yangians

This is one of the best-posed open chapters. The current book already knows exactly what is proved and what remains: braided monoidal bar complexes proved, Verdier
=
=
𝑅
R-matrix inversion proved, chain-level DK square proved, factorization-level statement on evaluation locus proved, extension to full category
𝑂
O still open and dependent on Yangian Koszulness plus factorization-level Kazhdan equivalence.

9902090v3

9902090v3

 The upgrade is to make that decomposition the main structure of Chapter 24 rather than a remark near the end.

Chapter 25 (pp. 973–988): Toroidal and elliptic algebras

This is still a horizon chapter. The right constructive move is to formulate it around what must replace Arnold in the elliptic/toroidal world — Fay identities, theta/Eisenstein structures, and completed propagator formalisms — rather than pretending it is already an extension of the current theorematic machinery.

Chapter 26 (pp. 989–1026): Explicit genus expansions

This chapter is theorematically valuable because it supports the scalar genus theorem and the GRR story. But it should not be allowed to suggest that explicit genus expansions prove the full modular package. They only support the scalar part, unless and until
Θ
𝐴
Θ
A
	​

 is built.

Chapter 27 (pp. 1027–1100): Detailed computations

This chapter has a concrete structural defect: the open-conjecture index still lists the same conjecture label
27.17.25
27.17.25 twice, once for the
𝑠
𝑙
3
sl
3
	​

 bar generating function and once for the
𝑠
𝑙
3
sl
3
	​

 discriminant.

9902090v3

9902090v3

 Fix the labels. More substantively, this chapter is where the book should systematize transfer-matrix, automaton, or recurrence methods if it wants the generating-function/discriminant conjectures to become theorems rather than isolated numerology.

Chapter 28 (pp. 1101–1106): Explicit computations via NAP duality

This is a good bridge chapter, but it should be reframed as a computational method chapter, not as a separate conceptual theory standing parallel to the main one.

Chapter 29 (pp. 1107–1132): Feynman diagram interpretation of bar-cobar duality

This chapter contains fertile mathematics, but it should now be explicitly branded as Stratum II / programme mathematics, except where genus-zero results are actually proved. The later status tables already say the path-integral and higher-genus Feynman dictionary remain conjectural and downstream of the master conjectures.

9902090v3

Chapter 30 (pp. 1133–1154): BV-BRST formalism and Gaiotto’s perspective

Same diagnosis. Genus-zero BRST/bar identifications are now theorematic, higher-genus BV/QME identifications are not. Chapter 34’s status table says exactly this: genus-0 foundation proved, higher genus programmatic.

9902090v3

 The fix is to use Chapter 34’s status taxonomy and stop blurring genus zero and all genera.

Chapter 31 (pp. 1155–1174): Holomorphic-topological boundary conditions and 4d origins

This chapter should become a programme chapter explicitly dependent on the BV/BRST and
𝐸
𝑛
E
n
	​

 master conjectures. Right now it is mathematically rich but logically under-tagged.

Chapter 32 (pp. 1175–1180): Knot invariants and the Kontsevich integral

This chapter should be made conditional on the
𝐸
𝑛
E
n
	​

 / Feynman / BV programme, not presented as if it were on the same proof footing as the chiral core.

Chapter 33 (pp. 1181–1198): Physical origins

This chapter is motivational, not evidentiary. It should say so. The main fix is to prevent readers from treating physical motivation as proof support.

Chapter 34 (pp. 1199–end): Concordance with primary literature

This is now the controlling chapter. It gives the status table, the five master conjectures, the homotopy templates, the nine-futures assessment, and the open-conjecture index. It should become the single source of truth for theorem/conjecture status. Every earlier chapter should be rewritten until it agrees with Chapter 34’s language and hierarchy.

How to upgrade the conjectures into theorems

The book itself now tells you the right meta-strategy: the
∼
99
∼99 conjectures collapse to five master conjectures, and those five are the right theoremization targets. So do not try to prove 99 conjectures one at a time. Prove the five structural ones.

Master Conjecture 1: Higher-genus PBW degeneration

This is the single missing hypothesis for unconditional modular Koszulity in generic affine Kac–Moody, generic Virasoro, and generic
𝑊
𝑁
W
N
	​

 families. To upgrade it to a theorem, you need:

a filtered genus-
𝑔
g bar complex whose associated graded is explicitly genus-zero-like,

a no-hidden-extensions argument beyond associated-graded degeneration,

a semicontinuity/generic-flatness theorem in the parameter,

and low-genus compute verification as a control mechanism.

This one theorem would immediately discharge a large swath of interacting-family “conditional” statements.

Master Conjecture 2: Cyclic
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


This is the foundational target of the modular programme and the real missing non-scalar completion of Theorem D.

9902090v3

 To prove it, you need:

a concrete construction of
\Def
c
y
c
(
𝐴
)
\Def
cyc
	​

(A),

a cyclic pairing compatible with both bracket and trace,

a completed modular graph/coefficient algebra,

and a convergent Maurer–Cartan equation in the completed tensor product.
Once this exists, the full package
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

) becomes genuinely theorematic rather than partly conjectural.

9902090v3

Master Conjecture 3: Full factorization-categorical DK/KL extension

The latest version already decomposes this correctly: chain-level/evaluation-locus pieces are proved, the full factorization-level extension is not.

9902090v3

 To make it a theorem, you need:

Yangian Koszulness beyond evaluation modules,

factorization-level Kazhdan equivalence,

and full braided monoidal compatibility.
This should absorb all the separate DK and KL conjectures currently scattered across Chapters 20 and 24.

Master Conjecture 4: Completed bar theory for infinite-generator duals

This is the right home for
𝑊
∞
W
∞
	​

, Yangian towers, and similar infinite-generator duals. To prove it, you need:

completed/pronilpotent bar and cobar constructions in the chiral/factorization setting,

convergence and continuity theorems,

and a robust notion of completion/pro-object duality compatible with the rest of the modular package.
This one theorem would clear much of the current horizon around
𝑊
∞
W
∞
	​

, large-
𝑁
N, and tower-type examples.

Master Conjecture 5: BV/BRST/bar identification

The book itself says this is downstream of the first four and should not be placed on the same logical level. That is exactly right. Once the modular/coderived/bar machinery is complete, then and only then should one try to prove the full all-genera BV/BRST/bar comparison using Costello-style renormalization and formal moduli comparison.

What to do with the remaining non-master conjectures

Chapter 34’s open index already groups the remaining conjectures by theme: algebraic structure, representation theory/Langlands, generating functions/combinatorics, physics/BV-BRST, and holomorphic-topological dualities.

9902090v3

9902090v3

9902090v3

 The constructive move is:

treat algebraic-structure conjectures such as 6.4.11, 6.4.15, 6.2.26 as consequences of Master 5;

treat 20.14.2–20.14.4 and 24.9.6 as consequences of Master 3;

treat 21.19.17, 26.3.3, 26.3.5, 26.3.7, 27.17.20, 27.17.25 as consequences of Master 4 plus a transfer-matrix/combinatorics programme;

treat 30.9.5, 30.9.3, 29.11.4, 29.4.1, 18.30.2, 18.30.7, 18.31.3 as consequences of Master 5;

treat 31.11.1, 10.10.4, 11.7.3, 22.10.1, 25.1.5 as genuine programme-level horizons that should stay conjectural until the core master conjectures are settled.

Bottom line

The latest version should be upgraded in one decisive way: make Chapter 34 the constitution of the book. The five-layer architecture, the two-strata split, the scalar/spectral/full package distinction, the periodicity-profile replacement of scalar period, the conditional/unconditional modular Koszul boundary, and the five-master-conjecture hierarchy should all be propagated backward through Chapters 1–33. The mathematics is now good enough for that to work. What remains is a global status-and-formalism synchronization pass, followed by concentrated work on the five master conjectures the manuscript itself has now correctly identified.

9902090v3

9902090v3
