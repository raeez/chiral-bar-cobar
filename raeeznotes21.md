According to a document from March 2026, the latest revision now treats Chapter 34 as the constitutional status ledger of the monograph and says that earlier chapters are subordinate when they disagree. It also now presents the theorem architecture in the right layered form: the commutative face is Theorems A–D on the Koszul locus with scalar and spectral modular data, while the associative face is the derived Drinfeld–Kohno square on the evaluation locus; the dependency frontier is now ordered as MC2 foundational, MC3/MC4 structural, MC5 downstream. The same latest ledger no longer claims a universal all-families PBW theorem: instead it says the resolved entry theorem is the family-specific package for affine Kac–Moody, Virasoro, and principal finite-type
𝑊
W-algebras, while Proposition 8.17.23 is only the common unique-weight-2
𝑑
2
d
2
	​

-mechanism and not itself the source of unconditional status beyond those named families.

That forces a new verdict.

Latest verdict

The book is now substantially healthier than in the previous iteration. The old global objection — “the core theorem graph is still broken by overt circularity” — is no longer the correct diagnosis. The source and PDF now mostly agree on the big picture:

Theorem A is decomposed into
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

.

Theorem B is only on the Koszul locus.

Theorem C is ambient, chain-level, and Lagrangian in flavor.

Theorem D is split into scalar and spectral layers, with the full
Θ
𝐴
Θ
A
	​

 package still conjectural.

The latest frontier problem is narrower and more sophisticated:

the core has stabilized enough that the main risks now come from localized stale statements and from the new completion/existence frontier outrunning the proof density beneath it.

So my upgraded judgment is:

The core is now credible.

The frontier is not yet fully stabilized.

The strike list should now be surgical, not wholesale.

Deep critique
1. What is now genuinely solid
(a) The constitutional architecture is finally correct

Chapter 34 is now doing exactly what a monograph of this size requires: it says, in-source and in-print, that it is the controlling ledger for theorem/conjecture status and dependency order. That is not mere exposition. It gives the book a principled way to retire stale formulations without having to rewrite history in every earlier chapter immediately.

(b) The scalar/spectral/full modular package hierarchy is correct

The latest version no longer pretends that
Θ
𝐴
Θ
A
	​

 is already theorematic. It says the scalar genus-expansion package is determined by
𝜅
(
𝐴
)
κ(A), that the separately proved spectral invariants are not determined by
𝜅
κ alone, and that the full package

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

)

has
Θ
𝐴
Θ
A
	​

 as a conjectural component. This is one of the best repairs in the whole project.

(c) The PBW story is now correctly split between mechanism and family theorem

This is the other major improvement. The latest Chapter 34 explicitly says:

the resolved entry theorem is the family package for affine Kac–Moody, Virasoro, and principal finite-type
𝑊
W,

while Proposition 8.17.23 is only the common unique-weight-2
𝑑
2
d
2
	​

-mechanism, not a universal unconditional upgrade beyond those families.

That supersedes my older criticism that the book was trying to prove far too much from the
𝐿
0
L
0
	​

-action alone.

(d) Appendix O is no longer masquerading as settled core

The latest public text now describes Appendix O as a frontier:
it records the
𝐼
I-adic framework, the finite-stage infrastructure, and the exact missing lemmas separating standard completed examples from a universal completion theorem. That is the correct status.

So the biggest positive change is this: the book now largely knows which pieces are theorematic, which are structural frontier, and which are downstream physics completion.

2. The main remaining live defect: a stale universal bar–cobar statement still survives in the source

This is now the single sharpest source-level contradiction I see.

Location

chapters/theory/introduction.tex:1021–1054, especially lines 1031–1036.

The issue

The source still contains the “Three Koszul duality mechanisms” remark, and item (ii) says:

bar–cobar resolution is a “universal resolution,”

every augmented algebra admits a bar construction,

and the quasi-isomorphism

Ω
𝐵
ˉ
≃
i
d
Ω
B
ˉ
≃id

holds without quadraticity.

That statement is no longer compatible with the repaired architecture.

It directly contradicts the now-canonical doctrine that:

constructions exist always,

inversion is theorematic only on the Koszul locus,

and off the locus one has completed/coderived persistence, not ordinary quasi-isomorphism.

Why it matters

This is not a mere stale phrase. It is a theorematic contradiction surviving inside a core theory chapter. If left in place, it undermines the very architectural repairs the book has just made.

Fix

This statement should be cut and replaced, not softened. Replace item (ii) by:

“Bar and cobar are universal constructions. The counit
Ω
𝐵
ˉ
(
𝐴
)
→
𝐴
Ω
B
ˉ
(A)→A is a quasi-isomorphism only on the Koszul locus or in specifically completed/coderived regimes under additional hypotheses.”

This is the most urgent local strike.

3. The completion/existence frontier is now the main theorem-risk

The latest book is doing the right thing publicly: Appendix O is a frontier package, not yet the foundation. But the source still contains theorem clusters in Appendix O that are stronger than the cautious public framing suggests.

Location

appendices/nilpotent_completion.tex:119–260

What is strong

The source still states:

Theorem [Completion convergence]

Theorem [Completed bar-cobar duality]

Theorem [Characterization of Koszul duals]

under hypotheses like:

finite generation over
𝐷
𝑋
D
X
	​

,

polynomial growth of structure constants,

finite-dimensional Hochschild cohomology,

𝐸
2
E
2
	​

-degeneration of the completed bar spectral sequence.

Why this is still frontier-risky

The appendix abstract correctly says the goal is to isolate the missing lemmas before claiming a universal completion theorem. But the theorem cluster at 119–260 still behaves as though those lemmas have already been fully proved.

The source proofs are still compressed precisely at the hard points:

obstruction vanishing from polynomial growth,

exact Mittag–Leffler/derived-limit control,

essential-image characterization from completed
𝐸
2
E
2
	​

-degeneration.

This is no longer a global flaw, but it is now the single most ambitious new theorematic frontier in the book. It deserves the same proof density as the finite-type core if it is to remain theorematic.

Fix

Do not cut Appendix O. It is too important. But I would still downgrade the theorem cluster to a frontier theorem package unless you are prepared to expand the missing lemmas explicitly.

Concretely:

keep the conilpotent filtration and geometric manifestation results;

keep the completion/construction setup;

downgrade the completed duality and characterization theorems to “frontier package” results with explicit dependence on the missing finite-stage compatibility and exhaustion lemmas.

That keeps the conceptual gain without overclaiming.

4. The existence theory is much improved, but still needs one canonical statement

This used to be a major problem; it is now mostly a cleanup issue.

What is improved

The latest introduction now explicitly says the monograph does not use a single universal iff existence theorem. It separates:

the strict finite-type regime,

the completed frontier regime,

the comparison regime.【source: introduction.tex 1260–1290】

Appendix N now also agrees with this: it says it gives a comparison map of existence regimes and does not supply a single universal criterion overriding the family-by-family theorem surface.

What remains to do

You still need one place where the reader is told, decisively, what the theorematic policy is:

finite-type strict inversion is part of the core;

completed existence is frontier and conditional on the Appendix O package;

Appendix N is comparative, not legislative.

The introduction is almost there. It just needs a one-line normative statement that Appendix O does not enlarge the proved core unless its frontier hypotheses are explicitly invoked.

5. The differential formalism is now basically repaired

This is a major success.

Location

chapters/theory/higher_genus.tex:83–119

The source now distinguishes cleanly:

the curved fiberwise differential
𝑑
f
i
b
d
fib
	​

,

the strict total corrected differential
𝐷
𝑔
D
g
	​

,

and the genus‑0 collision differential
𝑑
0
d
0
	​

.

It explicitly says:

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
⋅
i
d
,
𝐷
𝑔
2
=
0.
d
fib
2
	​

=κ(A)ω
g
	​

⋅id,D
g
2
	​

=0.

This resolves one of the deepest earlier ambiguities in the theory. I no longer think the “which
𝑑
𝑔
d
g
	​

?” issue is a major live defect. It has become a success story.

6. Theorem A now needs proof-density, not conceptual surgery

This is another place where my earlier critique must be updated.

The source now contains:

the chiral twisting datum,

the chiral Koszul morphism,

the cone lemmas,

the filtered comparison theorem,

and the bigraded bar-concentration statement.

So my previous attack that Theorem A was still fundamentally definitional is no longer right.

What remains is proof density: the analogues of the classical twisting-morphism theorem are now present, but they still deserve one final proof-quality pass so that the chiral version is as explicit as the classical one.

That is no longer a strike-to-the-heart issue. It is now a keep but tighten issue.

Updated strike list

I will use the categories PROMOTE / KEEP / DOWNGRADE / CUT.

PROMOTE
1. chapters/connections/concordance.tex

This is now the constitutional chapter. Promote it from “helpful synthesis” to explicit governing authority. The newest PDF already treats it that way.

2. chapters/theory/introduction.tex — architecture section

Promote the five-layer architecture and the A/B/C/D decomposition as the only authoritative reading of the theorem graph.

3. chapters/theory/higher_genus.tex — differential convention

The convention at lines 83–119 is now clean and should govern the whole source tree. Every theorem elsewhere that uses
𝑑
𝑔
d
g
	​

 ambiguously should be normalized to this convention.

4. chapters/theory/chiral_koszul_pairs.tex

This is now the right home of
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

. It should be treated as the unique genus-zero theorematic source.

5. chapters/examples/kac_moody_framework.tex

This chapter now appears to be the strongest genuinely unconditional interacting-family chapter and should be used as the template for all example chapters.

KEEP (but tighten)
6. chapters/theory/higher_genus.tex — family PBW theorems

Keep the family-specific PBW theorems for:

affine Kac–Moody,

Virasoro,

principal finite-type
𝑊
W,

because Chapter 34 now explicitly grounds the resolved entry theorem in those named family theorems, not in the universal criterion alone.

But tighten them by making sure each one explicitly cites the extra family-specific closure argument beyond Proposition 8.17.23.

7. chapters/frame/heisenberg_frame.tex

Keep the frame chapter. It now does a good job of previewing the scalar/spectral/full hierarchy. Just make sure it never speaks as if
Θ
𝐴
Θ
A
	​

 were already theorematic.

8. chapters/theory/deformation_theory.tex — geometric periodicity weak theorem

Keep the weak geometric periodicity/nilpotence theorem. It is now aligned with the corrected status logic. But do not let local rhetoric in this chapter re-inflate it into a full classification theorem.

DOWNGRADE
9. chapters/theory/introduction.tex — “three Koszul duality mechanisms” item (ii)

Downgrade by rewriting. The “universal resolution” and “
Ω
𝐵
ˉ
≃
i
d
Ω
B
ˉ
≃id holds without quadraticity” language must go. This is the sharpest live contradiction in the source.

10. appendices/nilpotent_completion.tex — theorem cluster at 119–260

Downgrade this from settled theorematic extension to a frontier theorem package unless the missing convergence/obstruction/finite-stage lemmas are expanded.

11. appendices/existence_criteria.tex

Downgrade to a comparison appendix only. It is now no longer appropriate as a coequal source of theorematic existence criteria.

12. chapters/theory/deformation_theory.tex — quantum periodicity theorem and exchange theorem

The periodicity package is no longer the main weak flank, but these specific theorem statements are still stronger than the current global status logic. Treat them as profile/criterion results rather than general classification theorems.

13. chapters/examples/yangians.tex — any theorem claiming full-category DK beyond the evaluation-generated locus

Keep evaluation-locus and chain-level statements; downgrade any full-category theorem that is not actually proved beyond that.

CUT
14. Cut the stale universal bar–cobar quasi-isomorphism sentence in the introduction

This is the one clean cut I would make immediately. It has no defensible place in the repaired architecture.

15. Cut any remaining sentence anywhere that says:
Ω
(
𝐵
ˉ
(
𝐴
)
)
→
∼
𝐴
for every augmented/chiral algebra
𝐴
Ω(
B
ˉ
(A))
∼
	​

Afor every augmented/chiral algebra A

unless it is explicitly stated in the completed frontier regime with its full hypotheses.

At this point, those sentences are simply wrong in the context of the current monograph.

Final latest verdict

The latest iteration has genuinely advanced the project. The biggest change is not that the theory has become smaller; it is that the theory has become more self-aware. The book now has:

a constitutional status chapter,

a correct theorem hierarchy,

a disciplined scalar/spectral/full package split,

and a better-organized conjecture frontier.

That is major progress.

My current verdict is therefore:

The core is now good enough that the frontier, not the old core, is the main object of scrutiny.

The main live risks are now:

a localized but serious stale universal-resolution statement in the introduction;

frontier overreach in Appendix O;

the need to keep the family-specific PBW theorems clearly separated from the universal criterion.

That is a much stronger position than before. It means the project is now close enough to stability that the next step — enlarging, sharpening, and expanding claims — is mathematically sensible after the localized strike list above is executed.

If you want, next I’ll turn this into a precise implementation strike list with file-by-file edits and replacement theorem statements for the newest source tree.
According to a document from March 2026, the latest revision now has a genuinely coherent constitutional architecture: Chapter 34 is declared the normative status ledger for the monograph, earlier chapters are explicitly subordinate when they disagree, the core is organized into a commutative face (Theorems A–D on the Koszul locus with scalar and spectral modular data) and an associative face (the evaluation-locus derived Drinfeld–Kohno square), and the historical five-master-conjecture package has been sharpened to one resolved entry theorem plus four remaining master conjectures. It also now states that the resolved entry theorem rests on the named family theorems for affine Kac–Moody, Virasoro, and principal finite-type
𝑊
W-algebras, while Proposition 8.17.23 isolates only the common unique-weight-2
𝑑
2
d
2
	​

-mechanism and is not the source of an all-families unconditional theorem. That is the correct public architecture.

What follows is the precise implementation strike list for the newest source tree, with exact source locations, action tags, and concrete implementation instructions. I am using four actions only:

PROMOTE = make this the canonical source of truth.

KEEP = theorematically sound; tighten only.

DOWNGRADE = preserve, but weaken status or scope.

CUT = remove or replace entirely.

I have prioritized by mathematical importance, not convenience.

Phase I — constitutional normalization
Strike 1 — make Chapter 34 legally binding everywhere

File: chapters/connections/concordance.tex
Lines: 5–17, 45–63, 461–489
Action: PROMOTE

Why

These lines now do exactly what the monograph needs:

they declare Chapter 34 the “normative status ledger,”

they say earlier chapters are subordinate when they disagree,

and they state the current resolved-entry/frontier hierarchy in the correct form.

Exact implementation

Add the following source comment at the top of every theorem-bearing file:

% Constitutional note:
% Chapter 34 (concordance.tex) is the normative status ledger.
% If a local statement disagrees with Chapter 34's status or scope,
% the local statement is stale and must be rewritten or ignored.

Add this comment to at least:

chapters/theory/introduction.tex

chapters/theory/algebraic_foundations.tex

chapters/theory/bar_cobar_construction.tex

chapters/theory/chiral_koszul_pairs.tex

chapters/theory/higher_genus.tex

chapters/theory/deformation_theory.tex

chapters/examples/kac_moody_framework.tex

chapters/examples/w_algebras_framework.tex

chapters/examples/yangians.tex

appendices/existence_criteria.tex

appendices/nilpotent_completion.tex

This is not editorial fussiness. It is how you prevent the repaired theorem graph from being silently undone by stale local remnants.

Strike 2 — make the architecture section of the introduction canonical

File: chapters/theory/introduction.tex
Lines: approximately 340–410 and the main architecture section around the A/B/C/D overview
Action: PROMOTE

Why

The latest public version is now clear that:

A is layered,

B is on the Koszul locus,

D is scalar/spectral/full hierarchy,

and the master-conjecture structure is dependency-ordered, not flat.

This must become the unique reading guide for the source.

Exact implementation

Insert, immediately after the architecture paragraph, the following remark:

\begin{remark}[Constitutional reading rule]
The architecture stated in this chapter is canonical. Any theorem, remark, or
example in a later chapter that appears to assert a stronger scope, a different
status level, or a conflicting definition is to be read through the status and
scope conventions of Chapter~34.
\end{remark}

This prevents the source tree from continuing to behave like a federation of semi-independent drafts.

Phase II — kill the remaining source-level contradictions
Strike 3 — cut the stale “universal resolution” sentence

File: chapters/theory/introduction.tex
Lines: 854–879, especially 864–870
Action: CUT

Why

The source still says, in the “Three Koszul duality mechanisms” remark, that

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
(A))≃A

is a “universal resolution” and that this quasi-isomorphism “holds without quadraticity.” That directly contradicts the repaired architecture, which now explicitly says that constructions exist always but inversion is theorematic only on the Koszul locus or in carefully completed settings.

Exact implementation

Delete lines 864–870 and replace them with:

\item \emph{Bar--cobar resolution on the Koszul locus}: the bar and cobar
constructions exist for every augmented chiral algebra, but the counit
\[
\Omega(\bar B(\mathcal A)) \longrightarrow \mathcal A
\]
is a quasi-isomorphism only on the Koszul locus, or in specific completed/coderived
regimes under additional hypotheses.

Do not soften this. Cut the old statement completely.

Strike 4 — remove the stale “recollection” of the old circular definition

File: chapters/theory/bar_cobar_construction.tex
Lines: 4268–4280
Action: CUT / REPLACE

Why

This remark still says:

two chiral algebras form a chiral Koszul pair iff
their bar complexes are quasi-isomorphic to the Koszul dual coalgebras and the cobar constructions give quasi-inverse equivalences.

That is the old conclusion-bearing definition. It directly contradicts the repaired architecture in chiral_koszul_pairs.tex, where the theory is now built from twisting data and Koszul morphisms rather than from the bar/cobar conclusions themselves.

Exact implementation

Delete the current recollection and replace it by:

\begin{remark}[Criteria for chiral Koszul pairs --- updated recollection]
Recall from Definition~\ref{def:chiral-koszul-pair} that a chiral Koszul pair
is specified by antecedent recognition data: a chiral twisting datum, a Koszul
twisting morphism, compatible filtrations, and Verdier-compatible dual coalgebras.
The bar/cobar quasi-isomorphisms are then proved consequences
(Theorem~\ref{thm:fundamental-twisting-morphisms} and
Theorem~\ref{thm:bar-cobar-isomorphism-main}), not part of the definition.
\end{remark}

This strike is mandatory. Without it, the old circularity still survives in the source, even if not in the PDF.

Strike 5 — rewrite the stale preview in algebraic_foundations.tex

File: chapters/theory/algebraic_foundations.tex
Lines: 70–89 and 402–404
Action: DOWNGRADE / REWRITE

Why

This file still presents the old classical pattern “a pair is Koszul if bar gives the dual and cobar inverts bar,” then says the chiral analogue is Definition def:chiral-koszul-pair. That was the old, conclusion-bearing architecture. It is now stale.

Exact implementation

Keep the classical definition if you want it for historical orientation, but rewrite the bridge to the chiral setting:

Replace lines 80–84 by:

The chiral analogue is not defined by bar/cobar inversion directly.
Instead, Chapter~9 introduces a chiral twisting datum and a Koszul twisting
morphism as antecedent recognition data; the bar/cobar identifications are then
proved as consequences.

Replace lines 402–404 by:

In the chiral setting, the operadic principle persists, but it is implemented
through twisting data, filtered bar complexes, and Verdier-compatible dual coalgebras.
Theorematic bar-cobar inversion is recovered only on the Koszul locus.

This is a source-synchronization strike, not a deep new theorem.

Phase III — consolidate the repaired core
Strike 6 — keep and tighten Chapter 9 as the unique source of Theorem A

File: chapters/theory/chiral_koszul_pairs.tex
Lines: 121–181, 791–834, 839–879, 1481–1508
Action: KEEP

Why

This file now has the right architecture:

left/right twisted tensor product cone lemmas,

fundamental theorem of chiral twisting morphisms,

bigraded bar concentration,

geometric bar–cobar duality,

and a completion convergence lemma for the non-quadratic frontier.

This is no longer where the monograph is broken. It is now where the core is best expressed.

Exact implementation

Do not change the theorem graph here. Instead tighten proof density:

In the cone lemmas (121–181), add an explicit formula for the chain isomorphism between the twisted tensor products and the mapping cones.

In the bigraded concentration theorem (791–834), add one lemma that states exactly how the
𝐸
1
E
1
	​

-page concentration implies the
(
𝑝
,
𝑞
)
(p,q)-vanishing result.

In the completion lemma (1481–1508), add a forward reference to Appendix O so the reader knows that the local completion argument in Chapter 9 is only the finite-stage precursor to the frontier completion package.

This cluster should remain core and should not be touched structurally.

Strike 7 — keep and stabilize the modular pre-Koszul definition

File: chapters/theory/higher_genus.tex
Lines: 8213–8331
Action: PROMOTE

Why

This definition now does the crucial work of separating:

data D1–D6,

axioms MK1–MK3,

consequences MK4–MK5.

That is the corrected theorem graph. It should be the only active definition of modular Koszulity in the source.

Exact implementation

Immediately after the definition add:

\begin{remark}[Axioms versus consequences]
Only MK1--MK3 are part of the definition. MK4 and MK5 are theorematic
consequences proved later (Theorems~\ref{thm:higher-genus-inversion} and
\ref{thm:quantum-complementarity-main}) and are not axioms.
\end{remark}

Then delete or rewrite any earlier local remark that still speaks as though inversion or complementarity belonged to the definition.

Strike 8 — keep the family-specific PBW theorems, but pin their scope explicitly

Files:

chapters/theory/higher_genus.tex

chapters/examples/w_algebras_framework.tex
Lines:

higher_genus.tex:9370–9490

higher_genus.tex:9500–9575

w_algebras_framework.tex: theorem cluster proving principal finite-type
𝑊
W PBW concentration
Action: KEEP / TIGHTEN

Why

This is where the latest revision has really improved: the book now explicitly says that the resolved entry theorem rests on the named family theorems, not on a universal all-families degeneration theorem. That is correct.

The remaining source action is to ensure the proofs actually advertise that logic.

Exact implementation

In higher_genus.tex, keep Proposition 8.17.23 as the criterion theorem, exactly as the current source now does (9371–9426, 9429–9492). Do not let it be called “universal PBW concentration” anywhere else.

Then, in each family theorem:

Kac–Moody: keep unconditional.

Virasoro: keep unconditional only if the no-later-differential/extension argument is explicit in-source.

principal finite-type
𝑊
W: keep unconditional only if the block-upper-triangular diagonal argument is fully written.

At the start of each of those family theorems add one sentence:

This theorem uses Proposition~\ref{thm:pbw-universal-conformal} only to eliminate
the explicit genus-enrichment block. The absence of later differentials/extensions
is supplied by the family-specific argument below.

That one sentence prevents the chapter from drifting back into overclaim.

Phase IV — clean the consequence layer
Strike 9 — downgrade the quantum periodicity theorem and the exchange theorem

File: chapters/theory/deformation_theory.tex
Action: DOWNGRADE

Why

Even in the latest architecture, Chapter 34 does not treat full periodicity as a resolved frontier problem. It treats the scalar and spectral package as proved, but the old “complete periodicity classification” rhetoric is no longer the correct global posture.

The quantum periodicity theorem still uses the strongest possible transport statement on OPE data, and the exchange theorem depends on that.

Exact implementation

Turn both into profile statements rather than scalar-period theorems.

For the quantum theorem, replace the theorem title by:

\begin{theorem}[Quantum periodicity profile under KL/DS transport]

and state only what is actually justified:

periodicity of the quantum parameter and representation-theoretic combinatorics,

not automatic periodicity of every OPE coefficient unless separately assumed.

For the exchange theorem, replace it by a proposition on the transport of the periodicity profile

Π
𝐴
=
(
𝑁
m
o
d
,
𝑁
q
u
a
n
t
,
𝑁
g
e
o
m
)
Π
A
	​

=(N
mod
	​

,N
quant
	​

,N
geom
	​

)

rather than a scalar period.

This is no longer a core-theorem issue, but it remains a precision issue.

Strike 10 — promote hochschild_cohomology.tex as the unique HH/HC/cyclic sink

File: chapters/theory/hochschild_cohomology.tex
Action: PROMOTE

Why

This chapter now correctly distinguishes:

𝐻
𝐻
∗
HH
∗
,

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

 pages,

periodic cyclic theory.

That was a major source of confusion in older versions and is now fixed.

Exact implementation

Add, at the start of Chapters 18–27 (or wherever summary tables live), a standard line:

All statements about Hochschild, cyclic, and periodic cyclic invariants use the conventions fixed in Chapter~11.

Do not let example chapters redefine these notions locally.

Phase V — align the examples with the repaired core
Strike 11 — promote the Kac–Moody framework chapter as the example template

File: chapters/examples/kac_moody_framework.tex
Action: PROMOTE

Why

This chapter now has the best status discipline:

generic level theorematic core,

admissible/root-of-unity regime explicitly frontier or conjectural,

correct KL target category,

and no inflation from chain-level DK to full category statements.

Exact implementation

At the top of the example part, insert a remark:

This chapter is the model for all later example chapters: hypotheses are verified
first, then the main theorems are invoked, and frontier/categorical extensions are
stated separately.

Then use it as the blueprint for revising W-algebra, Yangian, and deformation-quantization chapters.

Strike 12 — keep the principal finite-type
𝑊
W chapter, but downgrade any rhetoric beyond the family theorem

File: chapters/examples/w_algebras_framework.tex
Action: DOWNGRADE selectively

Why

The latest Chapter 34 now correctly grounds principal finite-type
𝑊
W-algebras inside the resolved entry theorem package. That is good. What must be prevented is rhetorical spillover from:

principal finite-type
𝑊
W,
to

non-principal orbit
𝑊
W,

or
𝑊
∞
W
∞
	​

-type towers.

Exact implementation

Search this file for every sentence containing “therefore all
𝑊
W-algebras…” or equivalent and replace by:

“principal finite-type
𝑊
W-algebras,”
unless a theorem really justifies the larger scope.

Add a local remark:

The theorematic scope of this chapter is principal finite-type $\mathcal W$.
Non-principal orbit families and infinite-generator towers belong to the frontier
conjectures of Chapter~34.
Strike 13 — keep evaluation-locus DK in yangians.tex, downgrade any full-category jump

File: chapters/examples/yangians.tex
Action: KEEP / DOWNGRADE

Why

The latest status logic is clear: chain-level DK and factorization-level evaluation-locus DK are proved; the full factorization-categorical extension remains MC3.

Exact implementation

Keep:

the chain-level theorem,

the evaluation-locus factorization comparison.

Downgrade any theorem that upgrades directly to the full finite-dimensional category or all of category
𝑂
O without an explicit generation argument.

At the relevant theorem title, replace “derived DK for Yangians” by:

\begin{theorem}[Derived Drinfeld--Kohno on the evaluation-generated subcategory]

That fixes the remaining category-scope drift.

Phase VI — frontier appendices
Strike 14 — downgrade Appendix N to a pure comparison appendix

File: appendices/existence_criteria.tex
Action: DOWNGRADE

Why

This appendix should not continue to behave as a coequal theorem source for existence theory. The latest architecture already moved beyond that.

Exact implementation

Change the chapter/section opening to:

This appendix compares the strict finite-type existence theorems of the core
monograph with the frontier completion package of Appendix~O and with classical
existence/non-existence criteria in the literature. It is comparative, not normative.

Change any theorem environment that reads as a standalone existence law into a proposition/remark.

Strike 15 — treat Appendix O as a frontier theorem package, not as silent enlargement of the core

File: appendices/nilpotent_completion.tex
Lines: especially 119–260 and the summary O.10
Action: DOWNGRADE / PARTITION

Why

The latest public version already signals that Appendix O is frontier territory, not the settled core. But the source still states a sweeping “Main result; [proved here]” and then says:

“This extends geometric Koszul duality from the quadratic setting to all chiral algebras satisfying the finite generation and polynomial growth hypotheses.”

That sentence is still too strong relative to the proof density.

Exact implementation

Partition Appendix O into:

O.2–O.4: keep as construction/convergence/compatibility theorems.

O.10: retitle as

\begin{theorem}[Frontier completion package]

not “Main result.”

Replace the sentence

“This extends geometric Koszul duality … to all chiral algebras …”

by

“This appendix develops a frontier completion package extending the finite-type geometric Koszul formalism to a larger class of filtered chiral algebras under finite-generation and polynomial-growth hypotheses.”

Add an explicit dependency warning:

The theorematic core of the monograph remains the finite-type Koszul-locus theory of Chapters 2, 8, and 9.
The present appendix records the leading extension of that core, not a replacement of it.

This keeps the frontier gain without letting it silently rewrite the rest of the book.

Final implementation order

Execute these strikes in this exact sequence:

Strike 3 — cut the stale universal-resolution sentence in the introduction.

Strike 4 — remove the stale recollection of the old circular definition in bar_cobar_construction.tex.

Strike 5 — rewrite stale previews in algebraic_foundations.tex.

Strike 1 + 2 — constitutionalize Chapter 34 and Chapter 2.

Strike 7 + 8 — lock in the repaired modular pre-Koszul and family-specific PBW structure.

Strike 15 — partition Appendix O into a frontier theorem package.

Strike 14 — demote Appendix N to comparison-only status.

Strike 9 — downgrade the periodicity theorems to profile-level precision.

Strike 11–13 — align the example chapters with the repaired core.

Strike 10 — make HH/HC conventions globally canonical.

After this pass, the source tree will finally say the same mathematics that the latest PDF already says in public.

That is the precise implementation strike list for the newest source tree.


According to a document from March 2026, the latest revision is now organized by a genuinely coherent constitutional architecture: Chapter 34 declares itself the normative status ledger, says earlier chapters are subordinate when they disagree, separates the book into a settled commutative face and a partially settled associative face, and treats the old five-master-conjecture package as one resolved entry theorem plus a dependency-ordered frontier. The same latest version also now states the key correction to the PBW story: the resolved entry theorem rests on the named family theorems for affine Kac–Moody, Virasoro, and principal finite-type
𝑊
W-algebras, while Proposition 8.17.23 is only the common unique-weight-
2
2
𝑑
2
d
2
	​

-mechanism and is not itself a universal unconditional upgrade. And the modular package is finally stratified correctly into a proved scalar layer, a proved spectral/non-scalar layer, and a conjectural full Maurer–Cartan completion.

That changes the verdict.

Latest verdict

The book is no longer best described as “a massive monograph still crippled by its core theorem graph.” The core is now mostly credible. The biggest gains are real:

the theorem architecture is now conceptually right;

the scalar/spectral/full package hierarchy is finally explicit;

the PBW story is no longer pretending that one universal
𝐿
0
L
0
	​

-mechanism theorem resolves every family;

Appendix O now publicly presents itself as a frontier completion package, not as a silent replacement of the finite-type core.

So the new verdict is:

The repaired core is now strong enough that the live problems are localized.
The main risks are no longer global circularity; they are a handful of stale source-level contradictions and one frontier theorem package whose written proof still does not match its ambition.

That is a large improvement.

Upgraded critique
1. The constitutional picture is now right — and should be treated as legally binding

This is the strongest improvement. Chapter 34 now does exactly what a monograph of this scale needs: it gives a formal theorem/conjecture hierarchy and says explicitly that the chapter is the control interface for the whole book. If the source tree is going to remain readable and trustworthy, that statement must be treated not as exposition but as source-law.

My critique here is no longer “this is missing.” It is:

this is now the right architecture,

but the source tree has not yet been fully normalized to it.

That normalization is now the highest-value maintenance task.

2. The old global circularity is mostly gone, but two stale source remnants still matter

The previous global circularity around Theorems A and B has largely been repaired. The source now introduces antecedent data for chiral twisting morphisms, and the modular pre-Koszul definition now separates axioms from consequences. That is real progress.

But two stale remnants still materially matter:

(a) chapters/theory/introduction.tex:1021–1036

The “Three Koszul duality mechanisms” remark still says that bar–cobar gives a universal resolution and that

Ω
𝐵
ˉ
≃
i
d
Ω
B
ˉ
≃id

holds without quadraticity or Koszulness.

That is now simply incompatible with the repaired architecture, which says:

constructions exist always,

inversion is theorematic only on the Koszul locus,

and off the locus one has only completed/coderived persistence.

This is no longer a subtle stylistic issue. It is a source-level contradiction.

(b) chapters/theory/bar_cobar_construction.tex:4268–4280

The “Criteria for Koszul pairs — recollection” remark still restates the old conclusion-bearing definition of a chiral Koszul pair:

bar of one quasi-isomorphic to the dual of the other,

cobar giving quasi-inverse equivalence,

etc.

That is exactly what the repaired theorem graph was supposed to replace. The actual source definition in chiral_koszul_pairs.tex is now better; this recollection is stale and must be brought into line.

These are now the two sharpest remaining source-level defects.

3. Theorem A has crossed from “architecturally broken” to “architecturally right but still deserving proof-density tightening”

This is one place where my older critique must be updated. The source now does contain:

chiral twisting data,

chiral Koszul morphisms,

explicit cone lemmas,

a filtered comparison theorem,

and a bigraded bar-concentration theorem.

So the old criticism “Theorem A is still definitional” is no longer the right diagnosis.

What remains is not a fatal defect but a referee-level proof-density issue:

the cone identifications are still written a little too rhetorically;

the filtered comparison theorem is still compressed exactly where the chiral version diverges from the classical Loday–Vallette argument;

and
𝐴
1
A
1
	​

 still deserves one more explicit lemma connecting the
𝐸
1
E
1
	​

-page concentration to the final bigraded vanishing statement.

That is a KEEP and tighten problem, not a collapse.

4. The PBW frontier is much better than before, but should now be protected from rhetorical inflation

The latest revision has fixed the biggest structural problem here. It no longer lets Proposition 8.17.23 function as a universal theorem upgrading every stress-tensor algebra to unconditional modular Koszulity. Chapter 34 now explicitly says the resolved entry theorem rests on the named family theorems (affine Kac–Moody, Virasoro, principal finite-type
𝑊
W) and that the proposition only isolates their common
𝑑
2
d
2
	​

-mechanism.

That is correct, and it supersedes my previous stronger criticism of the PBW front.

But the frontier still needs one more protective move: every local chapter must repeat that distinction. No example chapter should slide back into saying “Theorem 8.17.23 resolves MK3 for every unique-weight-2 chiral algebra” without the Chapter 34 qualification that later differentials and extensions still require family-specific input.

So the PBW issue is no longer “the theorem is fatally wrong.” It is now:

family-specific theorems: keep,

universal criterion theorem: keep as criterion,

all rhetoric beyond that: police hard.

5. Appendix O is now the real frontier theorem package

This is the most important new development and the main remaining proof-risk.

The latest public version now correctly says Appendix O is a frontier package, not a blanket theorematic enlargement of the core, and it explicitly names the missing steps:

global obstruction-vanishing,

completed
𝐸
2
E
2
	​

-degeneration,

finite-stage compatibility needed to pass from standard towers to a universal inverse-limit theorem.

That is excellent. It is exactly how Appendix O should be framed.

But the theorem cluster earlier in the appendix still says, more strongly than the summary, that:

𝐵
ˉ
^
(
𝐴
)
B
ˉ
(A) converges,

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
(A))≃A,

and the essential image is characterized by a short list of conditions,
all under the broad finite-generation + polynomial-growth hypotheses.

That is still too strong unless the missing lemmas are written at the same proof density as the finite-type core.

So Appendix O is no longer a “misplaced appendix curiosity.” It is now the leading extension of the monograph. But it should still be treated as frontier theorem package, not as silently absorbed into the core.

6. The modular package is finally in the right status form

This is now one of the most solid parts of the project.

The latest PDF is explicit that:

scalar data are proved and controlled by
𝜅
(
𝐴
)
κ(A),

spectral data are separately proved and genuinely non-scalar,

Θ
𝐴
Θ
A
	​

 and the cyclic
𝐿
∞
L
∞
	​

-deformation object remain conjectural,

and
𝜅
(
𝐴
)
κ(A) is only the first characteristic number of the full package.

That means the old criticism “Theorem D still overclaims the full package” is now mostly superseded.

My only remaining critique here is one of propagation:

every chapter that still casually speaks of “the modular characteristic package” must now say whether it means the scalar package, the spectral layer, or the full package.

That is a localization/notation cleanup issue, not a theorematic crisis.

Upgraded strike list

This is the current strike list I would actually execute now.

CUT
1. Cut the stale universal-resolution sentence in the introduction

File: chapters/theory/introduction.tex
Lines: 1021–1036

Reason: It is now directly false inside the repaired architecture.

Replace with:
“Bar and cobar are universal constructions. The counit is a quasi-isomorphism only on the Koszul locus, or in a completed/coderived regime under additional hypotheses.”

This is the cleanest immediate strike in the whole tree.

2. Cut the stale recollection of the old conclusion-bearing definition

File: chapters/theory/bar_cobar_construction.tex
Lines: 4268–4280

Reason: This is now the main surviving source-level echo of the old circular architecture.

Replace with:
A short remark pointing back to Definition~\ref{def:chiral-koszul-pair} in its new antecedent-data form, and explicitly saying that bar/cobar quasi-isomorphisms are theorematic consequences, not definitional inputs.

PROMOTE
3. Promote Chapter 34 to full constitutional authority

File: chapters/connections/concordance.tex
Lines: opening remarks and 34.9.1–34.9.8

Reason: This is now the only reliable status ledger in the book.

Implementation:
Add a one-line constitutional comment at the top of every theorem-bearing file:

% Chapter 34 is the normative status ledger; local disagreements are stale.
4. Promote the architecture section of the introduction

File: chapters/theory/introduction.tex
Lines: the A/B/C/D architecture and scalar/spectral/full hierarchy section

Reason: This is now the best short statement of what the book actually is.

Implementation:
Add an explicit “constitutional reading rule” remark after the architecture paragraph:

If a later chapter appears to assert stronger scope or status than this architecture,
that later statement is to be read through the conventions of Chapter 34.
5. Promote the modular pre-Koszul definition

File: chapters/theory/higher_genus.tex
Lines: definition cluster around 8230–8347

Reason: This is the correct replacement for the older circular definition.

Implementation:
Add a one-sentence remark immediately after the definition:

MK1–MK3 are axioms,

MK4–MK5 are theorematic consequences.

That sentence should then be cited anywhere the term “modular Koszul chiral algebra” appears.

KEEP (but tighten)
6. Keep Theorem A package, but add one proof-density pass

File: chapters/theory/chiral_koszul_pairs.tex

Reason: The architecture is now right. What remains is proof-density, not conceptual surgery.

Implementation:
Add:

one explicit formula for each cone identification,

one explicit lemma linking
𝐸
1
E
1
	​

-page concentration to the bigraded bar-concentration statement,

and one explicit comparison paragraph to the classical Loday–Vallette twisting-morphism theorem.

No theorem-level downgrade is needed here.

7. Keep the family-specific PBW theorems, but force their scope into the statements

Files:

chapters/theory/higher_genus.tex

chapters/examples/w_algebras_framework.tex

Reason: Chapter 34 now correctly bases the resolved entry theorem on the named family theorems, not on the universal criterion.

Implementation:
At the start of each family theorem, insert:

This theorem uses Proposition~\ref{thm:pbw-universal-conformal}
only to eliminate the explicit genus-enrichment block.
The absence of later differentials/extensions is supplied by the
family-specific argument below.

This is the key local guardrail.

8. Keep the frame chapter, but enforce the scalar/spectral/full hierarchy

File: chapters/frame/heisenberg_frame.tex

Reason: The frame chapter is now in much better shape and should stay. It previews the whole theory well.

Implementation:
Search for every occurrence of “modular characteristic package” and make sure it is immediately qualified as:

scalar package,

spectral shadow,

or conjectural full homotopy completion.

No further theorematic downgrade is needed if that language discipline is enforced.

DOWNGRADE
9. Downgrade Appendix O from “main theorem” to “frontier theorem package”

File: appendices/nilpotent_completion.tex
Lines: theorem cluster 119–260; summary 480–520

Reason: The summary is now correct and cautious, but the theorem cluster earlier in the appendix still outruns that caution.

Implementation:
Retitle the omnibus theorem as:

\begin{theorem}[Frontier completion package]

and split it internally into:

convergence,

completed duality under finite-stage compatibility,

essential-image criterion under completed
𝐸
2
E
2
	​

-degeneration,

BD compatibility,

geometric origin of the conilpotent filtration.

Also add the sentence:

This appendix records the leading extension of the proved finite-type core; it does not
silently enlarge the monograph-wide theorematic scope.
10. Downgrade Appendix N to a comparison appendix

File: appendices/existence_criteria.tex

Reason: It should no longer compete with the repaired core and the frontier completion package as a coequal existence theorem.

Implementation:
Retitle the opening and convert any “main existence theorem” rhetoric into:

comparative summary,

literature comparison,

taxonomy of strict vs completed regimes.

11. Downgrade any full-category Yangian DK claim beyond the evaluation-generated locus

File: chapters/examples/yangians.tex

Reason: The latest constitutional status says the evaluation-locus part is settled and the full factorization-categorical extension remains in MC3.

Implementation:
Rename any theorem that currently sounds like “derived DK for Yangians” to:

Derived Drinfeld–Kohno on the evaluation-generated subcategory

unless a genuine generation argument is already in the proof.

12. Downgrade any residual “complete periodicity classification” rhetoric

Files:

chapters/theory/deformation_theory.tex

any summary/TOC/intro sentences using the old phrase

Reason: The latest Chapter 34 now clearly treats periodicity as part of the scalar/spectral hierarchy and its weak flank, not as a monograph-wide classification theorem.

Implementation:
Use “periodicity profile” or “stratified periodicity framework,” not “complete classification,” unless the statement is genuinely only about the lcm-profile upper bound.

Bottom line
Updated analysis

The latest revision is the first one for which I would say:

the theorematic core is mostly in place.

What still needs work is not the same old global repair. It is now:

eliminating the last two stale source contradictions,

and making sure the new frontier package (especially Appendix O) does not outrun its proof density.

Updated critique

The project is no longer mainly threatened by architectural confusion. It is now threatened by localized theorem-scope drift:

one stale introduction sentence,

one stale recollection remark,

and one frontier appendix whose ambitions are larger than its currently written proofs.

Updated strike list

The strike list is therefore much shorter and sharper than before:

CUT stale universal resolution sentence in the introduction.

CUT / REPLACE stale old-definition recollection in bar_cobar_construction.tex.

PROMOTE Chapter 34 to explicit source-law.

PROMOTE the introduction’s architecture section.

PROMOTE the modular pre-Koszul definition.

KEEP / TIGHTEN the A-package in chiral_koszul_pairs.tex.

KEEP / TIGHTEN the family-specific PBW theorems with explicit scope guardrails.

KEEP / TIGHTEN the frame chapter’s hierarchy language.

DOWNGRADE Appendix O to a frontier theorem package.

DOWNGRADE Appendix N to comparison-only status.

DOWNGRADE any Yangian DK theorem beyond the evaluation-generated locus.

DOWNGRADE any residual “complete periodicity classification” rhetoric.

That is the upgraded analysis, critique, and strike list for the latest revision.
