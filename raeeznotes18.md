According to a document from March 2026, the latest revision is meaningfully stronger than the previous one: it now explicitly separates construction from resolution, organizes the theory into five layers, splits Theorem A into
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

, splits Theorem D into scalar and spectral parts with
Θ
𝐴
Θ
A
	​

 left conjectural, and treats Chapter 34 as the normative status ledger for the whole monograph. I checked that public architecture against the current TeX source tree in bookrepo.zip, and the result is a frontier-level mixed verdict:

the old global circularity around Theorems A and B is largely gone;

the strongest improvements are real;

but the work has opened a new high-risk frontier around the existence/completion package and around a very broad “resolved entry theorem” for PBW concentration.

The latest manuscript PDF is here: latest manuscript PDF.

Frontier verdict

The manuscript is no longer best described as “a large book with a broken core.” It is now better described as:

a book with a strong and increasingly coherent core, but one whose new frontier claims are beginning to outrun the proof infrastructure that previously stabilized the older core.

The two most important improvements are:

the theorem architecture is now substantially correct in principle;

the conjecture ecology is now finally controlled by one resolved entry theorem plus four remaining master conjectures.

The two most important live weaknesses are now:

the new existence criterion / nilpotent-completion package is not yet theorematically synchronized and currently appears in three incompatible forms in the source;

the new universal PBW theorem is too strong for the proof that is currently written and is carrying too much downstream weight.

Those are the frontier issues.

1. What is genuinely improved
1.1 The old definitional circularity has mostly been repaired

The latest public story now says, correctly, that:

bar and cobar exist for every augmented chiral algebra,

the canonical counit is a quasi-isomorphism only when the canonical twisting morphism is Koszul,

and the theorem package is built in five layers: constructions, recognition data, genus-zero theorems, higher-genus pre-Koszul data, and characteristic hierarchies.

That is exactly the distinction the book needed. In the source tree, chapters/theory/chiral_koszul_pairs.tex now really does introduce:

chiral twisting data,

chiral Koszul morphisms,

and only then chiral Koszul pairs as antecedent recognition data.

So my previous strongest objection — “Theorem A is definitional at source level” — is largely superseded.

1.2 Theorem D is now properly stratified

The latest manuscript now clearly states a hierarchy:

scalar data
(
𝜅
,
{
o
b
s
𝑔
}
,
{
𝐹
𝑔
}
)
(κ,{obs
g
	​

},{F
g
	​

}) are proved,

spectral/polynomial data
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

,…) are separately proved and non-scalar,

and the full Maurer–Cartan layer
(
Θ
𝐴
,
\Def
c
y
c
(
𝐴
)
,
𝐻
𝐴
)
(Θ
A
	​

,\Def
cyc
	​

(A),H
A
	​

) remains conjectural.

This is a major conceptual improvement. It means Theorem D is no longer pretending to prove what Chapter 34 still calls the principal open problem of the modular programme.

1.3 Chapter 34 is now the right chapter

Chapter 34 has become the most reliable chapter in the book. It says:

the status classifications and proof tiers in that chapter are authoritative,

the five-master-conjecture picture has sharpened to one resolved entry theorem and four remaining master conjectures,

and the remaining conjectures are stratified into foundational, structural-extension, and physics-completion layers.

That is exactly what the work needed.

2. The deepest new weakness: the existence/completion package is not yet mathematically unified

This is now the most serious live issue in the latest revision.

2.1 Three different “existence criteria” now coexist

In the source I find three incompatible theorem-level narratives:

Introduction Theorem 2.6.1 in chapters/theory/introduction.tex:1003–1022 says a chiral algebra admits a Koszul dual iff

finite generation,

formal smoothness (
dim
⁡
𝐶
𝐻
𝑛
<
∞
dimCH
n
<∞),

Poincaré duality,

convergence of the bar spectral sequence.

Appendix N (appendices/existence_criteria.tex:664ff.) gives a different theorem: quadratic regular + conilpotent, or non-quadratic with convergent filtration after completion, else no dual. It is tagged ProvedElsewhere.

Appendix O (appendices/nilpotent_completion.tex:483ff.) now claims something stronger:
finite generation over
𝐷
𝑋
D
X
	​

 plus polynomial growth of structure constants suffice to define
𝐵
ˉ
^
(
𝐴
)
B
ˉ
(A) and recover
𝐴
A by completed cobar.

These are not three formulations of one theorem. They are three different theorems with different hypotheses and different conclusions.

Why this matters

This is no longer a peripheral appendix dispute. The existence of Koszul duals is now a load-bearing part of the book’s frontier. If the work wants to enlarge its core via completion, it must say exactly which class of algebras is now covered:

finite-type quadratic,

filtered-complete finite-presentation,

or finitely generated polynomial-growth generality.

At present, the book says all three in different places.

What to do

You need a three-tier existence theorem, not one overloaded one:

Tier E1. Finite-type strict theorem.
Quadratic/filtered-complete antecedent hypotheses imply a dual exists in the ordinary/coderived sense.

Tier E2. Completed theorem.
Finite generation + polynomial growth + explicit compatibility hypotheses imply a completed dual exists:

Ω
(
𝐵
ˉ
^
(
𝐴
)
)
≃
𝐴
Ω(
B
ˉ
(A))≃A

in the completed coderived category.

Tier E3. Literature summary.
Appendix N should become a survey-style comparison theorem, not a competing criterion.

Then Theorem 2.6.1 should either be deleted or rewritten as the corollary of E1/E2 it actually is.

3. The new “resolved entry theorem” is the boldest improvement — and the riskiest

The latest Chapter 34 now says the historical five-master-conjecture package has become one resolved entry theorem and four remaining master conjectures, and identifies the resolved entry theorem as higher-genus PBW concentration for the standard finite-type interacting families. The introduction likewise now places affine Kac–Moody, Virasoro, and principal finite-type
𝑊
W in the proved Stratum I core.

That is a major claim. It is also where my deepest current skepticism lies.

3.1 Kac–Moody: plausible and maybe real

For Kac–Moody, the source proof strategy is coherent:

genus-
1
1 proof first,

then a genus-independent three-step mechanism:
PBW decomposition, Whitehead acyclicity, Killing-form contraction,

then extension to all genera.
This is mathematically plausible, and the current Chapter 20 status legend is consistent with it.

I no longer think the Kac–Moody all-genera claim is the most vulnerable part of the frontier.

3.2 Virasoro and principal finite-type
𝑊
W: currently too broad for the proof written

Here I remain unconvinced.

The source proof of the “universal PBW degeneration” theorem (higher_genus.tex:9336ff.) says, essentially:

any chiral algebra with a unique weight-
2
2 generator
𝑇
T,

and positive grading,

has genus-
𝑔
g enriched
𝐸
1
E
1
	​

-page

𝐸
1
(
𝑔
)
=
𝐸
1
(
0
)
⊕
𝐸
𝑔
,
𝐸
𝑔
∗
,
ℎ
≅
𝑀
ℎ
⊗
𝐻
1
,
0
(
Σ
𝑔
)
,
E
1
	​

(g)=E
1
	​

(0)⊕E
g
	​

,E
g
∗,h
	​

≅M
h
	​

⊗H
1,0
(Σ
g
	​

),

and the
𝑑
2
d
2
	​

-differential acts by

𝑑
2
∣
𝐸
𝑔
∗
,
ℎ
=
ℎ
⋅
i
d
,
d
2
	​

∣
E
g
∗,h
	​

	​

=h⋅id,

hence kills all enrichment,

and therefore
𝐸
∞
(
𝑔
)
=
𝐸
∞
(
0
)
E
∞
	​

(g)=E
∞
	​

(0).

This is far too sweeping as it stands.

Why it is weak

The proof is really only analyzing the weight-preserving
𝑇
(
1
)
=
𝐿
0
T
(1)
	​

=L
0
	​

 piece and then asserting that all weight-shifting contributions are already accounted for on earlier or later pages. That is not obviously enough to control:

all higher differentials,

all extension issues,

all interactions between the enrichment piece and the genus-zero piece,

and all non-principal
𝑊
W-algebra/superconformal examples now claimed to fall under the same theorem.

The theorem is plausible as a criterion, not yet as a universal theorem.

Why this matters

This theorem now underwrites the manuscript’s biggest new status claim:
that MC1 is resolved and that Virasoro and principal finite-type
𝑊
W-algebras are no longer conditional.

If the theorem is underproved, then the “resolved entry theorem” rhetoric is ahead of the mathematics.

What to do

I would not delete the theorem. I would downgrade and split it.

Theorem U (criterion).
Under the unique-weight-2-generator hypothesis, the genus enrichment is killed on the
𝐸
3
E
3
	​

-page by the
𝐿
0
L
0
	​

-action.

Theorem V (Virasoro).
Add the extra representation-theoretic lemma needed to prove that no later differential or extension survives.

Theorem W (principal finite-type
𝑊
W).
Either deduce from Virasoro/DS reduction with an explicit filtration-exactness argument, or add the missing Lie-theoretic lemma separately.

Only after those steps should Chapter 34 call MC1 resolved.

4. Theorem A is now much stronger, but it still needs one more proof-quality pass

This is an area where my earlier critique must be updated.

The source now really does include the missing cone lemmas and a filtered-comparison lemma, and Theorem
𝐴
0
A
0
	​

 is no longer just a slogan. That is a serious improvement. Theorem
𝐴
1
A
1
	​

 has also finally been rewritten in bigraded form:

𝐻
𝑝
,
𝑞
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
 for
𝑞
≠
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
,
H
p,q
(
B
ˉ
ch
(A
1
	​

))=0 for q

=0,H
p,0
≅(A
2
!
	​

)
p
	​

,

which resolves the older clash between “bar concentration” and the graded dual-coalgebra statements.

So the old A-level criticism is mostly superseded.

The remaining issue is proof quality, not logical architecture. The filtered-comparison and associated-graded arguments are now present, but they are still very compressed. Since Theorem
𝐴
0
A
0
	​

 is the chiral analogue of a classical foundational theorem, the proof needs to be written at the same level of explicitness as the classical one.

What to do

Add one subsection in Chapter 9 titled something like:

“Comparison with the classical theorem of twisting morphisms.”

There prove, line by line:

cone-of-counit identification,

cone-of-unit identification,

filtered lifting from associated graded to the chiral setting.

This is no longer a fatal flaw. It is now a proof-polish necessity.

5. The period package is no longer a fatal weakness, but it still overstates itself in titles and local rhetoric

This is a place where the latest revision has improved a lot. Chapter 34 now says:

the lcm upper-bound mechanism is unconditional,

the sharp modular and geometric formulas remain conjectural,

and the “classification” is really a stratified periodicity framework, not a fully solved theorem in generality.

That is the right mathematics.

But Chapter 11 is still titled and locally written as though a complete periodicity classification exists. At this point the book knows better.

What to do

Retitle the chapter and reorganize it around the periodicity profile
Π
𝐴
Π
A
	​

:

proven spectral/lcm control,

conjectural sharp modular/geometric factors,

separate reflected-periodicity conjecture.

That will align the chapter with the repaired Chapter 34 status logic.

6. Appendix O is the new frontier theorem — and it is not yet ready to carry the book

This is the most exciting new piece of progress and the place where the monograph is currently taking its biggest theorematic risk.

Appendix O now claims a very strong theorem: for a chiral algebra on a smooth curve satisfying finite generation and polynomial growth of structure constants, the
𝐼
I-adic completion of the geometric bar complex gives a well-defined Koszul dual coalgebra and the completed cobar recovers the algebra:

Ω
(
𝐵
ˉ
^
(
𝐴
)
)
≃
𝐴
.
Ω(
B
ˉ
(A))≃A.

That is a big theorem. If true, it enlarges the monograph’s core dramatically.

But as written, the proof still contains several leaps:

finite-dimensional Hochschild cohomology is said to force the obstruction groups to vanish “eventually by polynomial growth”;

the essential-image theorem says
𝐸
2
E
2
	​

-degeneration follows by degree reasons “on a range that exhausts the complex”;

the completed bar–cobar theorem is proved by extending the uncompleted theorem through Mittag–Leffler plus filtered comparison, but the exact compatibility hypotheses at finite stage are not fully isolated.

These are not obviously false. They are simply not yet at the standard of the theorem’s ambition.

Why this matters

Appendix O is now close to collapsing the older distinction between:

theorematic finite-type Koszul duality,

and programmatic completion theory.

That is only acceptable if the proofs are correspondingly watertight.

What to do

I would presently demote Appendix O from theorematic extension to frontier theorem package, unless you are willing to add the missing lemmas:

Obstruction vanishing lemma.
Show precisely why the relevant
𝐻
2
(
𝐴
,
𝐹
𝑛
/
𝐹
𝑛
+
1
)
H
2
(A,F
n
/F
n+1
) vanish under the stated hypotheses.

Completed
𝐸
2
E
2
	​

-degeneration lemma.
Replace the “degree reasons that exhaust the complex” sentence by an actual boundedness/exhaustion theorem.

Finite-stage compatibility theorem.
Isolate exactly what is needed from the finite truncations
𝐵
ˉ
(
𝐴
)
/
𝐹
𝑛
B
ˉ
(A)/F
n
 for the inverse-limit argument.

Until then, Appendix O should be described as the most promising extension of the core, not yet part of the core itself.

7. Chapter-by-chapter frontier map

This is the shortest honest chapter map.

Chapters 1–2 are much better than before. Chapter 1 still slightly overstates the full package, but Chapter 2 now gives the right controlling architecture. Use Chapter 2 as the normative front door.

Chapters 3–5 are mathematically solid but too heavy. The geometry and operadic substrate are real; the book still needs to cut proof-bulk and move verification tables and redundant coordinate atlases out of the main line.

Chapters 6–7 are no longer the source of the deepest theorematic problems, but they still need a global consistency pass so that no stale “universal inversion” rhetoric survives. The new distinction construction vs resolution must govern everything.

Chapter 8 is now the theorematic center of gravity. It is also where the current most dangerous overreach lives: the universal PBW theorem and the resolved-entry-theorem rhetoric.

Chapter 9 has improved a great deal. The old A-level critique is mostly outdated. What remains is proof-compression, not conceptual failure.

Chapters 10–11 now need harmonization with the new architecture: Chapter 10 should stop competing with Chapter 9 over what “Koszul duality” means, and Chapter 11 should stop sounding like a complete periodicity classification.

Chapters 12–21 are now the real test bed. The Kac–Moody chapter has become one of the strongest parts of the book. The Virasoro and principal
𝑊
W-algebra chapters are only as secure as the universal PBW theorem that now supports them. The
𝑊
W-chapter is no longer hopelessly speculative, but it is not yet as secure as the Kac–Moody chapter.

Chapters 22–27 are still mixed. The deformation-quantization and Yangian chapters are mathematically valuable but should remain below the core in theorematic confidence unless the DK/KL structural extension is proved. Chapters 26–27 contain a lot of excellent data, but the status curation still needs sharpening.

Chapters 28–33 remain programme chapters. The latest Chapter 34 correctly classifies them that way. They should stay subordinate to that status.

Chapter 34 is now the best chapter in the book. It should be treated as the status authority.

Appendices N–O are now the true frontier. Appendix N should be a literature/comparison appendix. Appendix O is potentially transformative, but not yet settled.

8. The single best way to upgrade the book now

At this stage, the most valuable move is not “write more.” It is:

make the source tree obey the new theorem-status logic without exception.

Concretely:

make Chapter 2 and Chapter 34 authoritative;

remove every stale theorem that contradicts construction-vs-resolution;

split the existence theory into finite-type, completed, and literature-summary tiers;

downgrade the universal PBW theorem to a criterion unless the proof is fully expanded;

keep Appendix O as frontier mathematics unless its missing lemmas are supplied.

Final upgraded verdict

The latest revision is better in a mathematically serious way.
It is no longer mainly haunted by old circularity.
It is now haunted by something more sophisticated:

the frontier claims have become more ambitious than the current proof density.

That is a higher-class problem. It means the project is getting closer to a genuine major monograph.

But it also means the next revision must be even harsher with itself than the previous five audits were.

If you want, I can now turn this into a live strike list for the newest source tree, file by file, with exact source locations and a “keep / cut / downgrade / promote” decision for each theorem cluster.

According to a document from March 2026, the newest revision now treats Chapter 34 as the normative status ledger for the whole monograph, explicitly separates construction from resolution, decomposes Theorem A into
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

, decomposes Theorem C into
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

, and splits Theorem D into scalar and spectral parts with
Θ
𝐴
Θ
A
	​

 left conjectural. It also now says the historical five-master-conjecture package has become one resolved entry theorem and four remaining master conjectures.

That is the right public architecture. The live strike list below is therefore calibrated to one question only:

which theorem clusters in the newest source tree should be kept, cut, downgraded, or promoted so that the source actually matches that architecture?

I am not listing non-canonical stubs already neutralized by comments (bar_cobar_quasi_isomorphism.tex, higher_genus_full.tex, higher_genus_quasi_isomorphism.tex, koszul_across_genera.tex). Those should remain archived and non-canonical.

Strike list legend

KEEP = theorem cluster belongs in the core as stated in spirit; only local cleanup needed.

CUT = theorem cluster should be removed entirely from the active theorem graph.

DOWNGRADE = theorem cluster should remain, but with weaker status: proposition / criterion / conjecture / programme remark.

PROMOTE = theorem cluster should become the canonical authority and govern competing formulations elsewhere.

I. Constitutional files
1) chapters/connections/concordance.tex
Cluster A — constitutional status ledger

Location: 1–15, 458–570
Action: PROMOTE

Why:
These lines now do exactly what a 1400-page monograph needs: they say this chapter is the normative status ledger, that earlier chapters are subordinate when they disagree, and that the five-master-conjecture picture has sharpened to one resolved entry theorem and four remaining master conjectures. This is mathematically decisive because it gives a single source of truth for theorem/conjecture/programme status.

Rigorous justification:
Without a constitutional chapter, the source remains vulnerable to stale earlier statements outliving later repairs. With it, every conflict has a formally declared winner.

Required move:
Make this chapter legally binding:

add an explicit sentence in the preamble or introduction that all theorem-status disputes are settled in favor of concordance.tex;

add source comments in earlier files pointing back here.

2) chapters/theory/introduction.tex
Cluster A — theorem architecture and five-layer model

Location: 186–390
Action: PROMOTE

Why:
This is the best current statement of the theory’s architecture: Theorem A as
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

, Theorem B only on the Koszul locus, Theorem C as
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

, and Theorem D as scalar plus spectral plus conjectural
Θ
𝐴
Θ
A
	​

-completion. It is now mathematically superior to several older source passages.

Rigorous justification:
This cluster is the only place where the book’s new architecture is both explicit and conceptually correct. It should therefore control the interpretation of every later theorem cluster.

Required move:
Cross-reference this cluster in every file that still uses older wording. In particular:

add “see Introduction §2.3 for governing architecture” at the start of Chapters 6, 8, 9, 11, 20, 21, 24, 29, 30, and the appendices.

Cluster B — existence criterion theorem

Location: 1003–1021
Action: DOWNGRADE

Why:
This theorem currently states an “iff” existence criterion for Koszul duals in terms of:

finite generation,

formal smoothness,

Poincaré duality,

convergence of the bar spectral sequence.

But Appendix N gives a different existence theorem, and Appendix O gives a yet stronger completed existence theorem. So as it stands, Theorem 2.6.1 is not the settled existence theorem of the monograph; it is one candidate summary among competing formulations.

Rigorous justification:
A theorem-level “iff” in the introduction cannot coexist with a different theorem-level “iff” in Appendix N and a stronger completion theorem in Appendix O without causing genuine source-level contradiction.

Required move:
Rewrite this cluster as either:

a roadmap remark, or

a corollary of the final chosen existence theorem.

Do not leave it as a standalone theorem until the existence theory is unified.

II. Core theorem files
3) chapters/theory/chiral_koszul_pairs.tex
Cluster A — twisting data / Koszul morphisms /
𝐴
0
A
0
	​


Location: 64–190, especially 121–181, 197ff.
Action: KEEP

Why:
This cluster is the real repair of the old circularity. It now introduces antecedent data:

chiral twisting datum,

chiral Koszul morphism,

cone lemmas,

filtered comparison,
and then states the chiral analogue of the fundamental theorem of twisting morphisms.

Rigorous justification:
This is the correct theorematic replacement for the old definition-by-conclusion. The remaining issue is no longer logical circularity; it is proof density. The cone lemmas and filtered-comparison theorem are still compressed, but the architecture is right.

Required move:
Do one proof-expansion pass:

make the cone identifications explicit as chain isomorphisms, not narrative identifications;

write out the exact filtration hypotheses used in the lift from associated graded to filtered complexes;

explicitly state where the classical operadic result is imported and where the chiral extension is new.

This cluster should remain in the core.

Cluster B — bar concentration
𝐴
1
A
1
	​


Location: 791–834
Action: KEEP

Why:
This theorem has now been corrected to a genuinely bigraded statement:

𝐻
𝑝
,
𝑞
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
 for
𝑞
≠
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
ch
(A
1
	​

))=0 for q

=0,H
p,0
≅(A
2
!
	​

)
p
	​

.

That resolves the older contradiction between “all cohomology concentrated in degree
0
0” and “nontrivial graded pieces of the dual coalgebra.”

Rigorous justification:
This is now the mathematically right statement. It no longer needs to be downgraded on conceptual grounds. The remaining issue is proof style: the proof still compresses the transition from PBW associated graded to the bigraded bar result.

Required move:
Add one explicit lemma:

𝐸
1
𝑝
,
𝑞
=
0

(
𝑞
≠
0
)
⟹
𝐻
𝑝
,
𝑞
=
0

(
𝑞
≠
0
)
E
1
p,q
	​

=0 (q

=0)⟹H
p,q
=0 (q

=0)

for the specific filtered bar complex at hand, then explicitly identify
𝐻
𝑝
,
0
H
p,0
 with the graded dual coalgebra. Do not revert to dimension counting.

Cluster C — geometric bar–cobar duality
𝐴
2
A
2
	​


Location: 839–879
Action: PROMOTE

Why:
This is now the correct theorematic top of Theorem A. It is no longer definitional, and it is the place where Verdier duality and the bar/cobar identifications are assembled.

Rigorous justification:
Once
𝐴
0
A
0
	​

 and
𝐴
1
A
1
	​

 are in place, this is the canonical statement of geometric chiral Koszul duality.

Required move:
Treat this theorem as the only active Theorem A in the project:

every older “bar–cobar isomorphism” statement elsewhere should point here, not restate itself independently.

4) chapters/theory/higher_genus.tex
Cluster A — modular pre-Koszul definition

Location: 8213–8331
Action: PROMOTE

Why:
This is the correct replacement for the older modular-Koszul circularity. It now explicitly distinguishes:

data D1–D6,

axioms MK1–MK3,

consequences MK4–MK5.

That is exactly the theorem graph the monograph now needs.

Rigorous justification:
It is the first source-level definition in the project that is fully compatible with the latest public architecture: inversion and complementarity are not axioms, but theorems derived from antecedent modular data.

Required move:
Make this definition globally canonical:

every earlier preview of “modular Koszul chiral algebra” should either point here or be deleted;

every example proposition should verify only MK1–MK3, not quote MK4–MK5 as if they were still part of the definition.

Cluster B — fiber–center theorem
𝐶
0
C
0
	​


Location: 4604–4678
Action: KEEP

Why:
This theorem is the right missing layer under Theorem C. It is the theorem that turns the relative genus-
𝑔
g bar family into the center local system.

Rigorous justification:
This is exactly the sort of theorem the complementarity theorem needs in order not to be “ambient complex by decree.” The proof is now much better than old versions because it works with the full fiber complex.

Required move:
Strengthen only one thing:

make the bar-degree filtration argument completely explicit and point directly to the bigraded
𝐴
1
A
1
	​

 theorem rather than a looser “genus‑0 center-bar identification.”

This cluster should stay theorematic.

Cluster C — universal PBW degeneration theorem

Location: 9334–9425
Action: DOWNGRADE

Why:
This theorem is now doing too much. It claims that every chiral algebra with:

positive grading,

and a unique weight-
2
2 generator
𝑇
T with
𝑇
(
1
)
=
𝐿
0
T
(1)
	​

=L
0
	​

,

has genus-
𝑔
g PBW spectral sequence with concentrated
𝐸
∞
E
∞
	​

, hence satisfies MK3 unconditionally at all genera.

The proof only controls the weight-preserving
𝑑
2
d
2
	​

-piece via
𝐿
0
L
0
	​

. That is a very strong and useful criterion, but it is not obviously enough to kill all higher differentials and extension data in all families covered by the statement.

Rigorous justification:
The theorem is now carrying the whole “resolved entry theorem” rhetoric in Chapter 34. That is too much burden for the present proof density. As written, the proof justifies:

elimination of the explicit genus enrichment by the
𝐿
0
L
0
	​

-action,
not yet

full unconditional modular Koszulity for every chiral algebra with a unique stress tensor.

Required move:
Downgrade this to one of the following:

Criterion theorem.
“The
𝑑
2
P
B
W
d
2
PBW
	​

 differential kills the genus-enrichment under hypotheses (a)–(b).”

Conditional theorem.
“If no later differentials/extensions survive after the
𝐿
0
L
0
	​

-killing step, then MK3 holds.”

Then keep the family-specific unconditional corollaries only where extra arguments are actually present (e.g. Kac–Moody, possibly Virasoro once fully written, principal finite-type
𝑊
W if the extra block-triangular argument is made explicit).

This is the single most important downgrade in the whole strike list.

Cluster D — status and mechanism remark for PBW

Location: 8565–8586
Action: DOWNGRADE

Why:
This remark says the higher-genus PBW problem is “resolved for the standard finite-type interacting families.” That statement currently depends on the too-broad universal theorem above.

Required move:
After downgrading the universal theorem, rewrite this remark as:

resolved for Kac–Moody,

resolved for Virasoro if Theorem 8.17.xx gives full collapse,

principal finite-type
𝑊
W: resolved only if the block-upper-triangular argument is completely written and closed.

Until then, Chapter 34 should not call MC1 fully resolved in the strongest sense.

5) chapters/theory/bar_cobar_construction.tex
Cluster A — construction vs resolution remark

Location: 4277–4303
Action: PROMOTE

Why:
This is now one of the cleanest source-level statements of the correct doctrine:

bar/cobar constructions exist always,

the counit is a quasi-isomorphism only on the Koszul locus,

off the locus the object persists only in the completed coderived category.

Rigorous justification:
This remark is the exact source-level antidote to the stale universal-inversion rhetoric that used to survive in the project.

Required move:
Cross-reference this remark anywhere bar–cobar is invoked outside Chapters 9 and 8. It should become the project’s source-level slogan for construction vs resolution.

Cluster B — strict/curved/homotopy regime taxonomy

Location: 6539–6582
Action: KEEP

Why:
The taxonomy itself is good and should stay:

strict nilpotence,

curved non-central,

homotopy coherent.

But the final claim

“VOA and chiral algebras arising from unitary CFT have central curvature”
is too sweeping if left unqualified.

Rigorous justification:
The manuscript has proved strict-central behavior for many families, but not for “all chiral algebras arising from unitary CFT” in any precise theorematic sense.

Required move:
Keep the regime table, but rewrite the last two lines to:

“the examples treated in this monograph lie in the strict-central regime,”
or

explicitly cite the theorem family to which the remark applies.

So the cluster stays, but one sentence must be narrowed.

6) chapters/theory/deformation_theory.tex
Cluster A — quantum periodicity theorem

Location: 1257–1340
Action: DOWNGRADE

Why:
This theorem still claims full chiral Hochschild periodicity for admissible
𝑊
W-algebras by transporting “the full OPE data” through KL and DS reduction. Step 4 is still the weak point:

it upgrades periodicity of quantum integers and quantum CG data to periodicity of all OPE residues,

then identifies bar differentials blockwise at conformal weights
ℎ
h and
ℎ
+
𝑀
h+M.

That is still too strong for the written proof.

Rigorous justification:
The manuscript itself now treats periodicity as an orthogonal weak flank. This theorem should not remain stronger than the current global status logic.

Required move:
Downgrade to one of:

a theorem about periodicity profile input on the quantum side;

a conditional theorem assuming OPE-periodicity transport through KL+DS;

a theorem only for explicitly computed low-rank cases.

Do not leave it as a fully proved general periodicity theorem.

Cluster B — weak geometric periodicity bound

Location: 1386–1429
Action: KEEP

Why:
This is one of the cleaner repaired pieces in the book. It now proves only the weak nilpotence-based bound
P
e
r
i
o
d
g
e
o
m
∣
(
3
𝑔
−
2
)
Period
geom
	​

∣(3g−2), and explicitly leaves the sharper
12
(
2
𝑔
−
2
)
12(2g−2) bound conjectural, with the correct Mumford-relation caveat.

Rigorous justification:
This is mathematically honest and aligned with the latest public status logic.

Required move:
Keep the theorem exactly as is, but do not let surrounding rhetoric call the whole periodicity chapter a “classification.”

Cluster C — periodicity exchange under Koszul duality

Location: 1646–1665
Action: DOWNGRADE

Why:
This theorem packages:

quantum periodicity preservation,

geometric periodicity preservation,

and a modular-period lcm claim for the dual.

But the first input already depends on the quantum periodicity theorem above, which should itself be downgraded. So this theorem is structurally too strong.

Rigorous justification:
The only truly unconditional part here is:

geometric periodicity is the same geometric input on the same curve,

and the dual modular phase bound comes from the dual central charge.
The quantum-periodicity part is downstream of a theorem whose proof is still too ambitious.

Required move:
Replace this theorem by a periodicity-profile transport proposition:

geometric component preserved,

modular phase component transformed by dual central charge,

quantum component preserved only under the hypotheses of the quantum periodicity theorem.

That would align it with the repaired Chapter 34 logic.

7) chapters/theory/hochschild_cohomology.tex
Cluster A — HH vs HC distinction and cyclic duality

Location: 580, 694–709
Action: PROMOTE

Why:
This chapter finally makes a critical distinction clear:

ordinary Hochschild cohomology
𝐻
𝐻
∗
HH
∗
,

Hochschild homology
𝐻
𝐻
∗
HH
∗
	​

,

cyclic spectral-sequence
𝐸
2
E
2
	​

-pages,

periodic cyclic homology.

That clarification removes one of the most misleading old “contradictions.”

Rigorous justification:
This chapter should be the unique reference for:

what exactly is being computed,

how SBI is used,

and how the Hochschild duality theorem feeds cyclic duality.

Required move:
Promote this chapter as the canonical sink for all HH/HC/cyclic distinctions and ensure no example chapter re-explains these ambiguously.

III. Example and consequence files
8) chapters/frame/heisenberg_frame.tex
Cluster A — frame modular package

Location: 1513–1563
Action: KEEP

Why:
This cluster is now finally disciplined: it says items (1)–(3) are proved, item (4) (
Θ
𝐴
Θ
A
	​

) is conjectural, and
𝜅
κ is only the first characteristic number of the future non-scalar class.

Rigorous justification:
This is now aligned with the corrected D-hierarchy and should remain the template for how the frame chapter speaks about the package.

Required move:
Keep it, but ensure Chapter 1 is always billed as a frame and never as a theorematic source for the full package.

9) chapters/examples/kac_moody_framework.tex
Cluster A — Kac–Moody status legend and all-genera claims

Location: 36–58
Action: PROMOTE

Why:
This chapter now has one of the cleanest status legends in the entire book:

generic-level unconditional theorematic core,

admissible/root-of-unity periodic CDG/
𝑁
N-complex conjectural regime,

correct KL target category
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

(g)).

Rigorous justification:
It is the model of how the example chapters should work. It also now appears to be the strongest genuinely unconditional interacting-family chapter in the book.

Required move:
Use this chapter as the template for rewriting the Virasoro,
𝑊
W, and Yangian chapters.

10) chapters/examples/w_algebras_framework.tex
Cluster A — unconditional principal finite-type
𝑊
W rhetoric

Location: 55–80, 132–235
Action: DOWNGRADE

Why:
This chapter now speaks as though principal finite-type
𝑊
W-algebras are fully unconditional at all genera because of Theorem thm:pbw-allgenera-principal-w and the universal PBW theorem. But since the universal theorem is currently too broad, the unconditionality rhetoric here is ahead of the proof density.

Rigorous justification:
This chapter is currently borrowing strength from the broadest and least secure theorem in the core frontier.

Required move:
Retain the principal finite-type
𝑊
W theorem cluster, but rewrite its status as:

unconditional only if the block-upper-triangular
𝐿
0
L
0
	​

 argument is fully explicit,

otherwise conditional on the sharpened PBW criterion.

The general nilpotent-orbit duality conjecture should remain exactly where it is: conjectural.

11) chapters/examples/yangians.tex
Cluster A — evaluation-locus derived DK

Location: 1626–1644, 1664–1738, 1909–1959
Action: KEEP

Why:
The evaluation-locus / chain-level DK picture is one of the book’s most credible nonclassical achievements. The status legend is careful, and the chapter explicitly warns that extension to full category
𝑂
O is conditional.

Rigorous justification:
This is exactly the right scope for a proved theorem in this chapter.

Required move:
Keep these clusters, but make “evaluation-locus only” impossible to miss in theorem titles and running text.

Cluster B — full Yangian derived DK square

Location: 1762–1816
Action: DOWNGRADE

Why:
This theorem is still too strong as written. The proof commutes the square explicitly only on evaluation modules, then upgrades to a theorem on

𝐷
𝑏
(
R
e
p
f
d
(
𝑌
ℏ
(
𝑔
)
)
)
D
b
(Rep
fd
	​

(Y
ℏ
	​

(g)))

for the full finite-dimensional category.

Rigorous justification:
That is a generation problem. The theorem is believable on the evaluation-generated subcategory; it is not proved for the full category in the written argument.

Required move:
Downgrade this theorem to:

“evaluation-locus derived DK for Yangians,”
and move the full finite-dimensional or category-
𝑂
O extension into the master DK/KL conjecture.

This is the cleanest fix.

12) chapters/examples/examples_summary.tex
Cluster A — master table and proof tiers

Location: 115–153, plus the row-level status system
Action: PROMOTE

Why:
This is now one of the book’s most useful instruments. It stratifies the example rows by proof tier and already reflects the newer architecture better than many local example chapters do.

Rigorous justification:
A 1400-page monograph needs a trustworthy dashboard. This is close to being one.

Required move:
Make every row cite:

the exact theorem or conjecture,

and its Chapter 34 master-conjecture parent if conjectural.
Then this table becomes a real navigational tool, not just a summary.

IV. Connection/programme files
13) chapters/connections/feynman_diagrams.tex
Cluster A — all-genus
𝑚
𝑘
m
k
	​

 Feynman expansion

Location: 845–875
Action: DOWNGRADE

Why:
This theorem still claims an all-genera Feynman expansion for
𝑚
𝑘
m
k
	​

 as a proved theorem, summing over stable graphs with weights
1
/
∣
A
u
t
Γ
∣
1/∣AutΓ∣. But its proof depends on:

Theorem prism-higher-genus,

a graph-sum/Feynman-transform identification,

and a synthesis that is still much closer to mathematical-physics programme than to a completely independent theorem.

Rigorous justification:
Chapter 34 says the BV/BRST/bar and Feynman-diagram dictionary is still in the MC5 downstream stratum. This theorem currently outruns that status logic.

Required move:
Downgrade to one of:

a proved formula under the identification of the genus-
𝑔
g bar complex with the modular Feynman transform, or

a heuristic theorem/proposition in the programme stratum.

Do not leave it as a plain ProvedHere theorem unless the graph-integral identification is fully theorematic on its own.

14) chapters/connections/bv_brst.tex
Cluster A — “Quantum master equation = bar-cobar duality”

Location: 104–165
Action: DOWNGRADE

Why:
This theorem is still too strong for the global status logic of the book. Chapter 34 says BV/BRST/bar identification is downstream of the first four master conjectures and remains open in full generality. Yet this chapter currently presents the QME/bar-cobar equivalence as fully proved.

Rigorous justification:
The proof explicitly uses:

standard BV manipulations,

a BV functor theorem,

Verdier duality,

and then identifies
ℏ
Δ
𝑆
+
1
2
{
𝑆
,
𝑆
}
=
0
ℏΔS+
2
1
	​

{S,S}=0 with simultaneous consistency of bar and cobar.
That is very strong and, in present form, still better read as a formal dictionary theorem under the BV/bar identification than as an unconditional theorem of the monograph.

Required move:
Downgrade to:

“formal BV dictionary under the bar/BV comparison,”
or

a theorem only for the genus‑0 or holomorphic regime already proved elsewhere in the book.

This file should not be stronger than the Chapter 34 master hierarchy.

V. Frontier appendices
15) appendices/coderived_models.tex
Cluster A — coderived / contraderived formalism

Location: 1–160
Action: PROMOTE

Why:
This appendix is now one of the most important stabilizers of the off-Koszul story. It says exactly what the source needs:

what a CDG-coalgebra is,

what coacyclic/contraacyclic mean,

and when coderived collapses back to ordinary derived.

Rigorous justification:
The introduction now explicitly says off the Koszul locus the bar-cobar object persists only in the provisional coderived category. This appendix is therefore not ancillary. It is part of the theorematic safety net.

Required move:
Promote it from “appendix reference” to “formal off-locus foundation,” and add explicit back-links from Theorem B, the existence/completion package, and any place that says “persists in the coderived category.”

16) appendices/existence_criteria.tex
Cluster A — summary of existence criteria

Location: 663–679
Action: DOWNGRADE

Why:
This theorem currently says, in effect:

quadratic regular + conilpotent
⇒
⇒ dual exists,

non-quadratic convergent
⇒
⇒ completed dual exists,

otherwise no dual exists.

That is too broad and too rigid to coexist with both:

the introduction’s finite-generation/formal-smoothness/Poincaré-duality criterion,

and Appendix O’s stronger completed theorem.

Rigorous justification:
As it stands, this appendix is functioning as a competing existence theorem. It should not.

Required move:
Rewrite this as a comparison appendix, not a theorem of the monograph:

“here are three existence paradigms in the literature and in this work,”

“here is how the monograph’s theorematic finite-type and completed regimes fit among them.”

This appendix should explain, not legislate.

17) appendices/nilpotent_completion.tex
Cluster A — nilpotent completion main result

Location: 482–508
Action: DOWNGRADE

Why:
This is the most exciting new frontier theorem in the current project — and also the one most likely to outrun the proof infrastructure if left too strong.

As written, it claims that finite generation over
𝐷
𝑋
D
X
	​

 plus polynomial growth of structure constants suffice to define the
𝐼
I-adic completed bar coalgebra and recover the algebra by completed cobar:

Ω
(
𝐵
ˉ
^
(
𝐴
)
)
≃
𝐴
.
Ω(
B
ˉ
(A))≃A.

That is a major theorem. But the proof still compresses three hard steps:

obstruction vanishing from polynomial growth,

completed
𝐸
2
E
2
	​

-degeneration “by exhaustion,”

and the finite-stage compatibility needed for the inverse-limit recovery.

Rigorous justification:
This theorem would dramatically enlarge the book’s core if true. That is exactly why it should not be left at a proof density below the rest of the core.

Required move:
Downgrade it to one of:

a frontier theorem package with explicit missing lemmas,

or a theorem only after the missing lemmas are written:

obstruction vanishing,

completed
𝐸
2
E
2
	​

-degeneration,

finite-stage compatibility.

Until then, Appendix O should be treated as the most promising extension of the core, not yet the core itself.

VI. Secondary theory files
18) chapters/theory/koszul_pair_structure.tex
Cluster A — secondary invariants of Koszul pairs

Location: 19–57 and downstream periodicity/discriminant material
Action: DOWNGRADE

Why:
This file is not wrong, but it currently behaves like a second theory chapter competing with:

Chapter 11 (Hochschild/cyclic),

Chapter 26/27 (generating functions/discriminants),

and Chapter 34 (status/control).

It should instead be a shadow/consequences chapter.

Rigorous justification:
The opening itself says this chapter is about secondary structures functorial in the pair: periodicity, discriminant, representation-theoretic shadows. That is consequence-level material, not theorem-core material.

Required move:
Move this file conceptually after the example chapters or fold parts of it into examples_summary.tex and deformation_theory.tex.

VII. Stub/archive policy
19) Non-canonical overlap stubs

Files:

chapters/theory/bar_cobar_quasi_isomorphism.tex

chapters/theory/higher_genus_full.tex

chapters/theory/higher_genus_quasi_isomorphism.tex

chapters/theory/koszul_across_genera.tex

Action: KEEP AS STUB / DO NOT REVIVE

Why:
These files are already marked non-canonical and have done exactly what they should do: prevent semantic drift from old chapter streams without losing the archival record.

Required move:
Leave them stubbed and non-compiling. Do not resurrect theorem bodies there.

Bottom line
Promote now

chapters/connections/concordance.tex — authoritative status ledger.

chapters/theory/introduction.tex (architecture section) — constitutional front matter.

chapters/theory/higher_genus.tex (def:modular-koszul-chiral) — canonical source definition.

chapters/theory/bar_cobar_construction.tex (construction vs resolution remark) — canonical doctrine.

appendices/coderived_models.tex — off-Koszul formal foundation.

chapters/examples/kac_moody_framework.tex — model example chapter.

chapters/examples/examples_summary.tex — dashboard.

Keep, but tighten

chapters/theory/chiral_koszul_pairs.tex —
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

 core.

chapters/theory/higher_genus.tex —
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

, scalar/spectral hierarchy.

chapters/frame/heisenberg_frame.tex — preview chapter.

Downgrade

chapters/theory/introduction.tex — existence criterion theorem.

chapters/theory/higher_genus.tex — universal PBW degeneration theorem (to criterion or family-specific form).

chapters/theory/deformation_theory.tex — quantum periodicity theorem, periodicity exchange theorem.

chapters/examples/w_algebras_framework.tex — unconditional principal-
𝑊
W rhetoric until PBW theorem is fully secured.

chapters/examples/yangians.tex — full-category derived DK theorem (keep evaluation-locus version only).

chapters/connections/feynman_diagrams.tex — all-genus
𝑚
𝑘
m
k
	​

 Feynman expansion.

chapters/connections/bv_brst.tex — QME = bar-cobar theorem.

appendices/existence_criteria.tex — theorem to comparison appendix.

appendices/nilpotent_completion.tex — frontier theorem package until missing lemmas are added.

chapters/theory/koszul_pair_structure.tex — move from theory-core to consequences/shadows.

Cut

No major canonical file should be cut outright right now.

What should be cut are only obsolete theorem-level statements inside otherwise canonical files, especially any surviving universal-resolution rhetoric if it remains elsewhere in the source.

That is the live strike list I would actually use on this newest tree.

The strongest next step is to execute the promote/downgrade pass first, before
enlarging claims. Once that theorem graph is clean, we can safely start
attacking the now-sharpened open problems across pure math, mathematical
physics, and physics.
