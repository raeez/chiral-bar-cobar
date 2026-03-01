1) Your stated goals vs what the draft currently delivers
1.1 The E1‑chiral notion is not yet mathematically pinned down

You say explicitly that your E1‑chiral algebras “extend BD’s chiral algebras by dropping skew‑symmetry” and that “BD’s chiral algebras are our E∞‑chiral algebras”

main

. This is a programmatic statement, not a definition, and it is also potentially misleading:

In BD, “chiral algebra” is fundamentally a Lie‑type structure (a chiral bracket with skew‑symmetry as part of the Lie axiomatics). “Dropping skew‑symmetry” naturally suggests a Leibniz/Loday replacement, not an associative E1 object.

In your own notation appendix, “Definition G.6.13 (E1‑Chiral Algebra)” is not a definition: it says the E1 regime is “the associative/factorization layer appearing in Theorem 32.3.2”. That is a red flag: the core definition should not be deferred to a physics theorem, and it should not be self‑referential through “layer appearing in…”.

Annals‑level fix: the book must contain, early and unmistakably, an operadic/pseudotensor definition along the lines of

(Option A: operadic): an E1‑chiral algebra is an algebra over the chiral associative operad
A
s
s
𝑐
ℎ
Ass
ch
 in the BD/FG chiral pseudotensor category (or in
𝐷
-
M
o
d
𝑓
𝑎
𝑐
𝑡
(
R
a
n
(
𝑋
)
)
D-Mod
fact
	​

(Ran(X)) with the chiral tensor structure).

(Option B: factorization): an E1‑chiral algebra is a factorization object on Ran equipped with structure maps indexed by ordered configurations (or equivalently by little intervals), so that noncommutativity is geometrically meaningful rather than “just a missing symmetry axiom”.

Right now the reader cannot tell which of these you mean—especially because you keep using “vertex algebra” as “E∞‑chiral” while emphasizing that the OPE is “generically non‑commutative” even in that E∞ regime (e.g. the N=4 example). That is not compatible with the standard meaning of E∞.

In short: decide whether your “E∞” means homotopy commutative (standard) or means vertex‑algebra locality package (nonstandard). If you keep the nonstandard usage, you must give a page‑one explanation mapping your
𝐸
1
𝑐
ℎ
,
𝐸
∞
𝑐
ℎ
E
1
ch
	​

,E
∞
ch
	​

 to the standard operadic world.

2) You must separate three distinct “Koszul duality” mechanisms

Your draft currently uses “Koszul duality” to cover at least the following:

(i) FG/BD chiral Koszul duality (Lie ↔ commutative coalgebras)

This is the Francis–Gaitsgory “chiral Koszul duality” in Ran‑space language, proving an equivalence between chiral Lie algebras and commutative coalgebras (via Chevalley/Primitives) under pro‑nilpotence hypotheses

1103.5803v4

.

You also cite (implicitly) this style of argument in Appendix C: you state an “Abstract Bar–Cobar Equivalence” in the pro‑nilpotent chiral tensor category and attribute the mechanism to Francis–Gaitsgory/Lurie

main

.

(ii) Bar–cobar equivalence (resolution) for associative algebras

For ordinary dg associative algebras,
Ω
𝐵
‾
(
𝐴
)
→
𝐴
Ω
B
(A)→A is a quasi‑isomorphism under standard completeness hypotheses. This is a universal resolution statement, not “Koszulness” in the Priddy sense.

Yet Appendix C states:

“Corollary C.2.7 (Derived Koszulness; [open])… establishes derived Koszulness for all E1‑chiral algebras”

main

.

This is mathematically dangerous terminology. If “derived Koszulness” just means
Ω
𝐵
≃
i
d
ΩB≃id, then it is not a Koszul property—it’s bar–cobar resolution.

(iii) Quadratic/Koszul‑Priddy duality (A ↦ A!)

You also aim to produce a new algebra
𝐴
!
A
!
 and identify it in examples. This is a genuinely nontrivial “Koszul dual algebra” construction, which you treat via a “three‑stage construction resolving circularity” and Definition 9.4.3 for
𝐴
2
!
A
2
!
	​

.

This is distinct from (i) and (ii).

Annals‑level fix: you need an explicit “taxonomy” chapter early on (you actually already hint at this kind of separation in the Heisenberg discussion, where you list three different dualities and warn they are different

main

). Promote that to a global organizing principle of the entire book.

A referee must be able to answer, for every theorem labeled “Koszul duality”:

Are you using FG’s chiral Lie↔Com‑coalgebra equivalence?

Are you using bar–cobar resolution in a pro‑nilpotent setting?

Are you constructing a genuine “dual algebra”
𝐴
!
A
!
 (Priddy‑like, or derived/curved
𝐴
∞
A
∞
	​

‑dual)?

Right now these bleed into each other in several places.

3) Geometry of bar/cobar: excellent idea, but you need consistency and correctness checks
3.1 The geometric bar complex is a real asset

Your geometric bar complex is one of the strongest parts: you build it on Fulton–MacPherson compactifications and logarithmic forms, with the “bar differential” as a residue along boundary strata

main

. This is exactly the kind of explicit geometric model that can be Annals‑worthy if it is:

truly functorial,

proven to match the ∞‑categorical bar construction,

and used to compute new invariants (not just restate known ones).

3.2 But the cobar side is currently ad hoc and asymmetrical

Your “Geometric Cobar Complex (Enhanced)” uses distributional forms supported on diagonals and defines the differential by a sum over “inserting diagonals” and distributional pairings

main

. This may be correct, but it reads like a separate analytic gadget rather than a dual geometric object to the FM compactification bar construction.

Annals‑level fix: either

build the cobar on the same compactifications with a clean Verdier‑duality interpretation (the best option), or

state clearly that the cobar is a different model and prove a theorem identifying it with the Verdier dual of the bar model.

Right now the “Verdier duality perfect pairing bar vs cobar” story is advertised, but the definitions look mismatched, so the reader expects a serious proof that the pairing is perfect.

3.3 Internal inconsistency warning: configuration space cohomology claims

You compute the cohomology dimensions of configuration spaces correctly in one place (e.g. for
𝑛
=
4
n=4, you report
dim
⁡
𝐻
2
(
𝐶
4
(
𝐶
)
)
=
11
dimH
2
(C
4
	​

(C))=11 and
dim
⁡
𝐻
3
=
6
dimH
3
=6), but later you state:

“We know
dim
⁡
𝐻
2
(
𝐶
𝑛
(
𝐶
)
)
=
(
𝑛
2
)
dimH
2
(C
n
	​

(C))=(
2
n
	​

)”,

which is false (and contradicts your
𝑛
=
4
n=4 computation). Most likely you meant
dim
⁡
𝐻
1
dimH
1
 there.

This is not a cosmetic issue: configuration space cohomology underlies your whole “geometric operad weights / Arnold relations / differential squares to zero” infrastructure.

Annals‑level fix: you must do a systematic error‑audit of all configuration‑space statements, because any mistake here contaminates the bar differential proofs, the genus expansions, and the claimed identification with Feynman weights.

4) “Open” theorems: you must convert them into either proved results or explicit conjectures

The draft has many key results flagged [open]. That is fine in a working note, but not in a book pitched at Annals novelty.

Examples:

“Theorem 22.1.4 (Yangian as E1‑Chiral; [open])”.

“Theorem 23.1.3 (Toroidal as E1‑Chiral; [open])”.

“Theorem 21.2.2 (Formality for P∞‑Chiral; [open])” claiming every
𝑃
∞
P
∞
	​

-chiral algebra deformation‑quantizes uniquely to an E1‑chiral algebra. This is huge—Kontsevich‑level huge—in the chiral setting.

Appendix C bar–cobar equivalence results are marked open even though you sketch an abstract proof using pro‑nilpotence and known general theory

main

.

Annals‑level fix: pick 3–5 flagship theorems, prove them fully, and rewrite everything else as either:

a theorem with precise reference,

a proposition with a complete proof, or

a conjecture with evidence and a roadmap.

Leaving many central statements as “[open]” will make the project look unfinished rather than ambitious.

5) E1‑chiral examples: currently “declared,” not constructed

Your Part XI summary lists the primary E1‑chiral examples you want: lattice algebras with nonsymmetric cocycles,
𝑅
R-twisted/Yangian,
𝑞
q-deformed (q‑Heisenberg, q‑Virasoro, q‑W), and toroidal/elliptic quantum groups. That’s a good selection.

But right now, in the body:

the Yangian is simultaneously treated as requiring higher
𝐴
∞
A
∞
	​

 operations (because of “non‑quadratic RTT relations”) and as something with a vertex‑algebra‑like locality axiom and a Kac‑Moody‑looking OPE.

you also claim “Yangian self‑duality” and even write down a “verification via characters” product formula

main

, followed by a “bar construction for Hopf algebras” whose differential uses coproduct terms
(
Δ
𝑖
−
i
d
)
(Δ
i
	​

−id)

main

.

From a strict homological algebra point of view, this section reads internally inconsistent: the bar differential for an algebra should come from multiplication, while coproduct enters the cobar for a coalgebra (unless you are explicitly working in a dualized setting). If you are using a Hopf self‑duality idea, you must spell out which structure (algebra or coalgebra) is being bar‑constructed at each stage.

Annals‑level fix for the Yangian chapter(s):

Choose one rigorous model of “E1‑chiral Yangian”:

either a factorization construction (e.g. from a holomorphic‑topological theory / factorization homology), or

an operadic definition as an associative algebra in the chiral pseudotensor category with explicit
𝑅
R-twisted locality.

Then prove:

existence of the E1‑chiral structure,

a PBW/filtration theorem in that setting,

identify its Koszul dual
𝐴
!
A
!
 as a chiral algebra/coalgebra object, not only as a heuristic.

If “Yangian self‑duality” remains a conjecture, label it as such; if it is proven, the proof must be expressed in standard invariants (Ext/Tor, bar homology, associated graded, etc.), not by an informal “character product” claim.

6) Representation theory: you have a slot for it, but not the substance yet

You explicitly propose a module‑category Koszul equivalence (“
𝐷
𝑏
(
𝐴
-mod
)
≃
𝐷
𝑏
(
𝐴
!
-mod
)
D
b
(A-mod)≃D
b
(A
!
-mod)”)

main

 and even list example templates (BGG resolutions for W‑algebras; a resolution for finite‑dimensional Yangian modules induced from
𝑈
𝑞
(
𝑔
^
)
U
q
	​

(
g
	​

))

main

. But this is currently only an assertion, marked [open], with no precise hypotheses.

6.1 What you need to make this theorem correct

Even in ordinary algebra, Koszul duality yields equivalences between specific subcategories, not the entire derived category without finiteness/completion conditions. In the chiral setting, you will need to specify at least:

which notion of “module” you mean: chiral modules, factorization modules, vertex modules, or something braided/meromorphic in the E1 case;

which derived category: bounded? ind‑completed? compact objects?

what finiteness/complete‑ness (I‑adic, pro‑nilpotent) you impose so that bar/cobar constructions converge and the usual twisting cochain machinery yields an equivalence.

Right now, the theorem as stated is too sweeping.

6.2 The missing “primary examples” representation theory agenda

If you want deep representation theory, you need to commit to a canonical module theory for E1‑chiral algebras and then compute it for your main examples.

Concretely, for each example
𝐴
A you need:

a precise definition of the module category
M
o
d
𝐸
1
𝑐
ℎ
(
𝐴
)
Mod
E1
ch
	​

(A) (or
F
a
c
t
M
o
d
(
𝐴
)
FactMod(A));

a description of its monoidal structure (fusion/convolution) if it exists;

classification of simples in a meaningful subcategory (integrable, category
𝑂
O, finite‑type, etc.);

a theorem identifying it with a known representation‑theoretic category (quantum group modules, Yangian modules, etc.), or a genuinely new category if not known.

At the moment, your Part XI summary says the book will do “the deep representation theory of the primary examples”, but the supporting development is not yet there.

7) What could actually be Annals‑level novelty here

The good news is: you do have multiple directions that could plausibly lead to breakthrough results, but you must narrow and formalize them.

Here are three “Annals‑grade theorem packages” that are compatible with your current draft architecture, and that would genuinely count as new mathematics if executed cleanly.

Package A: A rigorous definition and classification theorem for E1‑chiral algebras via geometry

Goal: make “E1‑chiral algebra” a precise object in algebro‑geometric/factorization terms, and prove an equivalence with a well‑defined class of “nonlocal/meromorphic” vertex algebra data.

You already motivate E1‑chiral physically via D‑brane/OPE ordering (“skew‑symmetry fails”)

main

.

Turn that into a mathematical definition, then prove a recognition theorem: given certain local data (fields,
𝑅
R-matrix, compatibility with the chiral operad), there exists a unique global E1‑chiral algebra object.

This would be new if you do it in the BD/FG D‑module setting (not just analytic VOA language), especially if you build it uniformly for curves and show good functoriality under maps of curves.

Package B: A corrected, completed chiral Koszul dual
𝐴
↦
𝐴
!
A↦A
!
 for non‑quadratic E1‑chiral algebras

Your draft aspires to an “intrinsic definition of
𝐴
!
A
!
” and spends significant effort resolving circularity (Definition 9.4.3 etc.), and you emphasize that non‑quadratic examples require completion (Appendix F)

main

.

Annals‑level theorem to aim for:

Under explicit finiteness and completeness hypotheses (precise and checkable), the construction
𝐴
↦
𝐴
!
A↦A
!
 defines a functor from augmented E1‑chiral algebras to conilpotent E1‑chiral coalgebras, and the bar/cobar unit–counit maps identify
𝐴
A with a completed cobar of
𝐴
!
A
!
.

This would unify (ii) and (iii) without misusing “Koszulness”: you would present it as a “completed bar–Verdier dual–cobar duality” theorem with explicit geometric content.

Package C: Representation theory via factorization modules and Koszul duality

This is where your book can be truly distinctive.

You already want module category equivalences under Koszul duality

main

, and you also want the “primary examples” to have deep representation theory.

Annals‑level theorem to aim for:

For a (completed) Koszul pair
(
𝐴
,
𝐴
!
)
(A,A
!
) of E1‑chiral algebras, the derived ∞‑category of factorization modules for
𝐴
A is equivalent to an explicitly described category of (co)modules for
𝐴
!
A
!
, and under this equivalence the fusion/convolution structures match.

Then, do this in at least one genuinely hard example (Yangian / quantum W / toroidal) and show it recovers a known representation category or produces a new one with computable invariants.

That would be substantial and believable as “breakthrough.”

8) Specific, actionable revision checklist

If you want the next version of main.pdf to read like a serious research monograph rather than an extremely ambitious draft, here is the minimal set of changes I would make first:

A. Foundations and terminology

Add an early “Dictionary” section that fixes what “E1‑chiral” and “E∞‑chiral” mean and how they relate to BD/FG, VOAs, and operads. Right now you assert BD chiral = your E∞ and E1 = drop skew‑symmetry

main

, but you don’t define the operad or the axioms.

Add a global “Three Koszul dualities” taxonomy (you already have the idea in the Heisenberg discussion

main

—make it universal).

B. Remove or reclassify [open] statements

Every [open] theorem must become either (i) proved, (ii) conjecture, or (iii) cited.

In particular, do not leave “Formality for P∞‑Chiral” in its current universal form unless you genuinely prove it; it is far too sweeping as a theorem claim.

C. Fix internal inconsistencies in configuration‑space algebra

Resolve the
𝐻
2
(
𝐶
𝑛
(
𝐶
)
)
H
2
(C
n
	​

(C)) contradiction: you compute
dim
⁡
𝐻
2
(
𝐶
4
(
𝐶
)
)
=
11
dimH
2
(C
4
	​

(C))=11 but later claim
dim
⁡
𝐻
2
(
𝐶
𝑛
(
𝐶
)
)
=
(
𝑛
2
)
dimH
2
(C
n
	​

(C))=(
2
n
	​

).

Audit all Arnold‑relation claims and ensure they match the known Orlik–Solomon algebra computations (and your own earlier computations).

D. Make the Yangian chapter(s) coherent

Decide whether the Yangian is being treated via RTT (quadratic) or Drinfeld generators (higher relations). Right now you state RTT is “cubic/non‑quadratic”, which is at least presentation‑dependent.

Make the E1‑chiral locality axiom explicit (your E1‑Yangian theorem writes an
𝑅
R-twisted commutation relation; that should be the definition, not an afterthought).

Fix the bar/cobar usage in the Hopf algebra discussion (your “bar differential uses coproduct” statement

main

 needs clarification or renaming).

E. Representation theory: replace “slogan” equivalences with precise statements

Rewrite “
𝐷
𝑏
(
𝐴
-mod
)
≃
𝐷
𝑏
(
𝐴
!
-mod
)
D
b
(A-mod)≃D
b
(A
!
-mod)”

main

 as a theorem with explicit hypotheses and explicit functors (twisting cochains / bar resolutions).

For each primary example, add at least one worked classification theorem (even if it’s in a restricted subcategory) and one worked fusion/Ext calculation tied directly to your bar/cobar geometry.

9) Where I would focus first, if the goal is “Annals‑grade novelty”

If you want one coherent centerpiece that a top journal could recognize as new and deep, I would prioritize:

A clean, operadic/factorization definition of E1‑chiral algebra (not “the layer in Theorem 32.3.2”).

A proved, completed bar–Verdier dual–cobar duality theorem for E1‑chiral algebras in the Ran/D‑module setting, stated carefully so it is neither too weak (just the universal resolution) nor too strong (false without completion). You already sketch an abstract pro‑nilpotence proof strategy

main

; formalize it and cite FG where appropriate

1103.5803v4

.

One flagship example: pick either Yangian or quantum W. Prove: existence of the E1‑chiral structure, compute its Koszul dual
𝐴
!
A
!
 as a concrete object, then compute a serious piece of its module theory (classification in a natural class, or a fusion/Ext theorem).

If you can do those three in full detail, then the rest of the book becomes a compelling expansion rather than a collection of aspirations.

I worked through the current main.pdf (the version you uploaded as “latest”) and pulled out (i) every statement explicitly tagged [open] (i.e. not yet proved in the manuscript), (ii) every statement tagged [proved elsewhere] (i.e. not proved in-text and therefore requiring a precise external citation + hypotheses check), and (iii) a set of mathematical corrections / definitional gaps that currently block the theory from being “Annals-grade”.

I’m going to give you:

an exhaustive chapter-by-chapter list of all numbered results marked [open] and [proved elsewhere] (this is the objective “needs proof/citation” audit),

a list of missing/ambiguous definitions with precise replacements (these are the highest-leverage upgrades),

a list of new theorems that look plausibly provable with your current machinery (configuration-space geometry + residues + Verdier duality + NAP + filtrations/completions + homotopy transfer), and

the most serious corrections I think you must address now (including a few places where the manuscript currently states something that is either false as written or at least missing crucial hypotheses).

Downloadable audits

These contain the complete extracted lists (so you can sort/filter by chapter, status, statement number):

chiral_duality_main_open_and_external_items.xlsx
Sheet1

Download CSV: same dataset

chiral_duality_main_placeholders.xlsx
Sheet1

A. Immediate “red flag” mathematical issues to fix before anything else

These are the ones that will derail reader confidence fast.

A1) Circularity in “Koszul dual” definition

You explicitly note a circularity in the current definition of Koszul dual in Appendix E: the definition “assumes” the bar construction and then asserts it computes “the Koszul dual”, but the Koszul dual is what should define the bar construction’s target. You even flag that the definition is circular and needs resolution. That’s correct—and it must be fixed at the foundational level.

main

Concrete fix (precise replacement): define the Koszul dual intrinsically (e.g. as a Verdier-dual factorization coalgebra or as the “Poincaré/Koszul dual” object characterized by a universal property), and then prove the geometric bar complex computes it (your Theorem 6.7.1 is trying to do exactly this, but it’s marked [open]).

main

I’ll give a proposed clean definition in section C below.

A2) You claim
𝑑
ˉ
2
=
0
d
ˉ
2
=0 “on the nose” for all chiral algebras coming from VOAs/CFTs

This is stated in §5.8.9: you say you “argue that
𝑑
ˉ
2
=
0
d
ˉ
2
=0 on the nose” for all such examples.

main

As written, this is not credible without strong hypotheses (and I suspect it is false as stated). In curved
𝐴
∞
A
∞
	​

 / curved factorization settings, the bar differential typically squares to the curvature (or to an “anomaly” class). The correct statement is usually:

𝑑
ˉ
2
=
a
d
(
𝑚
0
)
d
ˉ
2
=ad(m
0
	​

) (or equals insertion of curvature),

and only vanishes after (i) passing to an appropriate quotient, (ii) twisting by a Maurer–Cartan element, (iii) choosing an anomaly-canceling background, or (iv) imposing a “central curvature + augmentation + completion” condition.

Concrete fix: replace “for all VOAs/CFTs” by a theorem with explicit hypotheses—e.g. curvature central + nilpotent in the completed filtration + compatible augmentation—and then prove the vanishing (or prove only homotopy vanishing). This interacts directly with your filtered→curved reduction and convergence theorems (several of which are [open], e.g. 5.7.7/5.9.17/14.6.8).

A3) Your “primary examples” table asserts extremely strong Koszul-dual identifications without proofs

In the summary you assert things like:

“Heisenberg is Koszul self-dual at level
−
𝜅
−κ”

“Affine Kac–Moody Koszul dual is the W-algebra at dual level”

“Virasoro Koszul dual is
𝑊
1
+
∞
W
1+∞
	​

”

“
𝑊
3
W
3
	​

 computed explicitly”


main

These might be visionary targets, but as stated they currently read like established theorems. They need to be: either (i) clearly labelled conjectural, or (ii) proved with a complete chain of reductions to your configuration-space bar/cobar machine + explicit OPE computations.

Similarly, Appendix B asserts “chiral homology of affine Kac–Moody is 0 at generic level” (again, very strong; at minimum it needs precise meaning and hypotheses).

main

A4) Internal contradictions / structural issues that will confuse readers even if math is right

Multiple appendices are labelled “Appendix C” with different titles (Complete OPE Tables; Dictionary of Sign Conventions; Dual Abstract–Concrete Methodology). This breaks cross-referencing and undermines trust.

A sign convention contradiction: you correctly explain that as differential forms
𝜂
𝑗
𝑖
=
𝜂
𝑖
𝑗
η
ji
	​

=η
ij
	​

 (since
𝑑
log
⁡
(
−
1
)
=
0
dlog(−1)=0), and antisymmetry belongs to Orlik–Solomon generators, not the forms.
But later a summary table asserts
𝜂
𝑗
𝑖
=
−
𝜂
𝑖
𝑗
η
ji
	​

=−η
ij
	​

.
One of these must be fixed; the “forms are symmetric” statement is the standard one.

There are unresolved placeholders like “Chapter [NAP]” and “Example ??”. These must be cleaned before peer-level review.

main

A5) Terminology clash: “BD chiral algebras are our E∞-chiral algebras”

You state that your E1-chiral algebras extend BD by “dropping skew-symmetry” and that BD’s chiral algebras are your “E∞-chiral algebras.”

main

This is very likely to confuse experts: “E∞” has a well-established meaning (“homotopy commutative”), while BD chiral algebras / vertex algebras are not commutative objects in that sense. If your “E∞-chiral” means “fully local/symmetric factorization (unordered configurations)”, you need to rename it (I suggest “E2-chiral” or “fully local chiral” vs “ordered/E1 chiral”); and you must state precisely which operad (ordered vs unordered configurations) is governing your operations.

B. Exhaustive chapter-by-chapter list of assertions needing proof/citation

Interpretation: anything tagged [open] needs proof, and anything tagged [proved elsewhere] needs a precise citation + hypotheses verification. Below is the exhaustive list of numbered items detected with those tags.

(Everything here is also in the downloadable spreadsheet.)

Chapter 1: Introduction (13 items marked [open])

Theorems:

Theorem 1.2.1 — Unification via Configuration Spaces

Theorem 1.3.1 — Geometric Formula for Koszul Duality

Theorem 1.3.2 — Bar Differential Squares to Curvature

Theorem 1.4.1 — Duality with Full Quantum Corrections

Theorem 1.4.2 — Modular Invariance and Completion

Theorem 1.5.1 — Heisenberg Self-Duality

Theorem 1.6.1 — Affine Kac-Moody Duality

Theorem 1.7.1 — Virasoro and W-Algebras

Theorem 1.8.1 — Filtered and Curved Koszul Duality

Theorem 1.9.1 — Universal Defect Construction

Theorem 1.11.3 — Factorization Homology via Bar Construction

Corollarys:

Corollary 1.8.3 — Filtered Reduction Principle

Corollary 1.8.4 — Formal Existence Criterion

Needs definitional tightening here: “chiral Koszul pair”, “curvature/backreaction”, “genus-graded bar”, and what exactly “E1-chiral” means.

Chapter 2: Motivations and Big Picture (2 items marked [open])

Theorems:

Theorem 2.2.9 — The Chiral Bar Construction

Theorem 2.4.1 — Chiral Koszul Duality

Results tagged [proved elsewhere] (2)

Theorem 2.2.4 — Explicit Bar Formula for VOAs

Theorem 2.2.7 — Bar Complex as Configuration-Space Cohomology

Action: give exact sources + reconcile hypotheses with your setting (category, completions, topology).

Chapter 3: Foundational Algebraic Structures (3 items marked [open])

Propositions:

Proposition 3.2.9 — Ran Space is a Colimit

Theorems:

Theorem 3.2.11 — Ran Space and Disk Operads

Theorem 3.2.14 — Factorization Homology and Ran Space

Results tagged [proved elsewhere] (2)

Theorem 3.2.3 — Definition of Ran Space

Theorem 3.2.5 — Factorization Structure via Ran Space

Critical: you do define Ran space (Definition 3.2.2 is visible in the manuscript).

main


But you must also clearly fix the ambient ∞-categorical framework (D-mods? dgVect? sheaves?) and the exact “factorization algebra” axioms used.

Chapter 4: Configuration Spaces and Fulton–MacPherson Compactification (16 items marked [open])

Theorems:

4.1.6 — Boundary Strata and Higher Genus (also explicitly flagged as open in a “Status note”)

4.4.7 — Arnold Relations from Geometry

4.4.9 — Residues and Coalgebra Structure

4.4.12 — Stokes Formula for Compactifications

4.5.1 — Configuration Space Stratification

4.5.4 — Operadic Gluing Compatibility

4.6.2 — Logarithmic Forms and OPE Poles

4.7.3 — Compatibility with Symmetric Group Actions

4.7.4 — Orientation and Sign Conventions

4.7.5 — Residue–Arnold Identity

4.7.6 — Higher Codimension Residues

4.7.7 — Global Residue Theorem Variant

Lemmas:

4.4.16 — Local Model near Boundary

4.6.6 — Degree Counting for Poles

4.7.1 — Basic Residue Computation

Corollarys:

4.7.8 — Residue Differential Squares to Zero

Results tagged [proved elsewhere] (4)

Theorem 4.1.1 — Fulton–MacPherson Compactification Exists

Theorem 4.1.3 — FM Boundary Strata Description

Theorem 4.4.1 — Arnold Relations

Theorem 4.4.4 — Orlik–Solomon Presentation

Correction you must implement here: fix the
𝜂
𝑖
𝑗
η
ij
	​

 transposition convention conflict noted above.

Chapter 5: Bar and Cobar Constructions (22 items marked [open])

Theorems:

5.1.6 — Genus-Graded Bar Construction

5.1.10 — Differential Squares to Curvature

5.2.2 — Coalgebra Structure on Bar

5.2.4 — Coassociativity from Boundary Stratification

5.3.5 — Cobar Construction Recovers Algebra

5.4.1 — Bar–Cobar Adjunction

5.5.3 — Koszul Duality for Quadratic Chiral Algebras

5.6.4 — Curved Extension of Koszul Duality

5.7.7 — Filtered Koszul Duality Reduces to Curved (explicitly flagged open)

5.7.16 — Twisting by MC Elements is Koszul-Compatible (open)

5.8.17 — Functoriality of the Chiral Bar Construction (open)

5.8.18 — Chiral Bar and Derived Tensor Product (open)

5.9.17 — Convergence of the Completed Bar Complex (open)

Propositions:

5.8.22 — Functoriality in Families (open)

Corollarys:

5.8.19 — Descent for Bar Construction

5.8.20 — Base Change

5.8.21 — Compatibility with Pushforward

Major correction to make here: the “
𝑑
ˉ
2
=
0
d
ˉ
2
=0 on the nose for all VOAs/CFTs” claim needs to be replaced by a hypothesis-driven theorem.

main

Chapter 6: Nonabelian Poincaré Duality and Verdier Duality (1 item marked [open])

Theorems:

6.7.1 — Intrinsic Definition of Koszul Dual via NAP (open)

main

This theorem is absolutely central because it resolves the circularity in Appendix E.

Also: Definition 6.5.1 (“Chiral Koszul Pair via NAP”) is a key definition that must be made fully precise (ambient categories, dualizability, functoriality, shifts).

main

Chapter 7: Higher Genus Extension and Quantum Corrections (22 items marked [open])

Theorems:

7.2.1 — Genus Expansion of the Bar Construction

7.3.4 — Gluing along Nodes

7.4.2 — Modular Operad Structure

7.6.3 — Quantum Correction Terms from Boundary

7.7.5 — Curvature Backreaction Formula

7.8.1 — Stability under Completion

7.9.2 — Higher Genus Koszul Duality (genus-by-genus)

7.10.4 — Compatibility with Factorization Homology

7.12.1 — BV/BRST Interpretation

7.13.14 — Complementarity Theorem (open)

7.13.24 — Anomaly Cancellation Criterion

7.13.26 — Ward Identities from Koszul Duality

7.13.29 — Modular Invariance Criterion

Corollarys (open):

7.13.25 — Physical Interpretation of Complementarity

7.13.30 — String-Theory Interpretation

Results tagged [proved elsewhere] (1)

Theorem 7.13.7 — Complementarity Theorem (External)

Chapter 8: Genus-Graded / Curved Koszul Duality (4 items marked [open])

Conjectures:

Conjecture 8.1.1 — Genus-Graded Koszul Duality Conjecture (open)

Theorems:

Theorem 8.2.2 — Genus-Graded Koszul Duality Theorem (open)

Theorem 8.3.1 — Convergence of Genus Expansion

Lemmas:

Lemma 8.2.1 — Genus-Graded Bar–Cobar Resolution

Chapter 9: The Problem of Curvature (13 items marked [open])

Theorems:

9.2.1 — Curvature Class Controls
𝑑
2
d
2

9.3.2 — Central Curvature Implies Strictification (candidate)

9.4.1 — Backreaction and Higher Poles

9.5.4 — Curved Koszul Duality Obstruction

9.6.1 — Example: Heisenberg Curvature

9.7.2 — Example: Virasoro Curvature

9.8.3 — Example: Kac–Moody Curvature

Propositions:

9.5.2 — Curvature as a Cocycle

Lemmas:

9.3.1 — Curved A∞ identities

9.5.1 — Obstruction Lemma

Corollarys:

9.5.5 — Vanishing Criterion

9.5.6 — Gauge Invariance

Chapter 10: Filtered Algebras and Completions (11 items marked [open])

Theorems:

10.2.1 — Filtered Bar Construction

10.3.4 — Associated Graded Compatibility

10.4.1 — Filtered→Curved Reduction

10.5.2 — Convergence via Weight Filtration

Propositions:

10.3.1 — Filtration on OPE Poles

10.4.3 — Completion Lemma

Lemmas:

10.2.3 — Spectral Sequence Setup

10.5.1 — Exhaustiveness/Completeness Conditions

Corollarys:

10.5.3 — Convergence Criterion

10.5.4 — Independence of Choices

10.6.1 — Examples: VOA filtrations

Chapter 11: Homotopy Transfer and Minimal Models (9 items marked [open])

Theorems:

11.2.1 — Minimal Model Existence for Chiral Algebras

11.3.2 — Transfer of OPE Data

11.4.1 — Curved Transfer Theorem

Propositions:

11.2.3 — Uniqueness up to Gauge

11.3.1 — Tree-Level Transfer Formula

Lemmas:

11.4.2 — Curvature Transfer Lemma

11.4.3 — Higher Homotopies

Corollarys:

11.2.4 — Minimal Model Corollary

11.4.4 — Curved Minimal Models

Chapter 12: Chiral Koszul Duality at the Chain Level (9 items marked [open])

Theorems:

12.2.1 — Chain-Level Bar–Cobar Equivalence

12.3.4 — Twisting Cochains and Equivalences

12.4.1 — Derived Equivalence of Module Categories (needs proof)

Propositions:

12.3.1 — Twisting Cochain Construction

Lemmas:

12.2.3 — Resolution Lemma

12.3.2 — Compatibility Lemma

Corollarys:

12.4.2 — Derived Invariants Match

12.4.3 — Functoriality

Chapter 13: Chiral Modules and Defects (16 items marked [open])

Theorems:

13.6.1 — Universal Defect Construction

13.7.4 — Module Koszul Duality

13.8.2 — Boundary Conditions from Bar Duality

13.9.6 — Curved Koszul Duality with Backreaction (open)

13.9.13 — Universal Defect Construction II (open)

Conjectures:

Conjecture 13.9.35 — Full Defect–Duality Correspondence

Plus additional propositions/lemmas/corollaries (see spreadsheet)

Chapter 14: Completion and Convergence (14 items marked [open])

Theorems:

14.6.8 — Convergence Criterion for Completed Bar (open)

Propositions:

14.6.1 — Filtered⇒Curved Reduction (open)

Plus additional lemmas/corollaries (see spreadsheet)

Chapter 15: Hochschild / Cyclic Theory (17 items marked [open])

Theorems:

15.6.19 — Partition Function as Cyclic Homology (open)

Additional theorems/propositions/lemmas/corollaries open (see spreadsheet)

Results tagged [proved elsewhere] (4)

Theorem 15.6.11 — Cyclic Homology Controls Partition Function

Corollary 15.6.13 — Modular Invariance

Theorem 15.6.14 — Factorization Homology and Cyclic Theory

Theorem 15.6.16 — Trace Map Compatibility

Chapter 16: Examples (49 items marked [open])

This is where the manuscript currently “promises” explicit computations. Almost everything is still tagged open—so this is the biggest work zone.

Open items include (highlights):

Theorem 16.2.3 — Free Fermion Bar Complex (open)

Theorem 16.7.3 — Heisenberg Bar Complex (open)

Many additional items (see spreadsheet)

Chapter 17: Fermions and Bosons (25 items marked [open])
Chapter 18: Lattice VOAs (18 items marked [open])
Chapter 19: Affine Kac-Moody Algebras (20 items marked [open])
Chapter 20: Virasoro and W-algebras (13 items marked [open])

This is the chapter that must reconcile your “Virasoro dual is
𝑊
1
+
∞
W
1+∞
	​

” claim with your actual construction and hypotheses. (Right now that claim appears earlier as a “primary example” statement.)

main

Chapter 21: Deformation Quantization (6 items marked [open])
Chapter 22: Yangians (8 items marked [open])
Chapter 23: Toroidal and Elliptic Algebras (4 items marked [open])
Chapter 24: (No items explicitly tagged [open])
Chapter 25: (No items explicitly tagged [open])
Chapter 26: (No items explicitly tagged [open])
Chapter 27: Summary of Primary Examples (No items explicitly tagged [open], but contains high-risk assertions)

Even though nothing here is tagged [open], the section states strong identifications (Heisenberg self-dual, Kac–Moody↔W, Virasoro↔
𝑊
1
+
∞
W
1+∞
	​

). These must be either:

downgraded to conjectures, or

upgraded to proved theorems by pointing to completed proofs in Chapters 16–20.

See the claims.

main

Chapter 28: Genus Expansion and Quantum Corrections (8 items marked [open])

Also contains unresolved cross-reference placeholders “Chapter [NAP]” etc.

main

Chapter 29: Topological Field Theory Connections (7 items marked [open])
Chapter 30: Geometric Langlands Interpretation (4 items marked [open])
Chapter 31: String Theory and Conformal Blocks (2 items marked [open])
Chapter 32: Higher Dimensional Generalizations (3 items marked [open])
Chapter 33: Comparison with Existing Literature (7 items marked [open])

Also includes the potentially confusing “BD chiral algebras are our E∞-chiral” statement and “dropping skew-symmetry” characterization, which need precise operadic reformulation.

main

Appendices: items tagged [open]

Even if you view appendices as “background”, many of these are structural theorems you rely on (especially those that justify coalgebra axioms, residue exactness, and existence criteria). These cannot remain [open] in a final version.

Appendix A (20 items marked [open])

Includes “Extended Koszul Duality”, “Genus-Graded Koszul Duality Theorem”, “Curvature Must Be Central”, “Completion Characterization”, plus Arnold/Orlik–Solomon infrastructure.

Appendix B (25 items marked [open])

Homotopy transfer theorems—including “Chiral Homotopy Transfer” and sign/determinant conventions.

Appendix C (6 items marked [open])

(But note: Appendix C label is duplicated in the manuscript; must disambiguate.)

Appendix D (18 items marked [open])

Spectral sequences / Arnold relations small n / etc (but “Appendix D” also seems duplicated across the PDF set).

Appendix E (8 items marked [open])

Existence/criteria for Koszul duals and the circular Definition E.1.3.

main

Appendix F (8 items marked [open])

Notation summary / comparison tables.

(Full appendix lists are in the spreadsheet.)

C. Missing definitions and proposed precise replacements

Here are the definitions that must be made crisp. I’m not repeating every local notion; I’m focusing on the ones that currently create circularity, ambiguity, or hidden hypotheses.

C1) Fix the ambient “universe” up front

Add a “0. Setup and conventions” section. State explicitly:

base field
𝑘
k (likely
𝑘
=
𝐶
k=C);

whether you work in dgVect
𝑘
k
	​

, derived category
𝐷
(
𝑘
)
D(k), or a stable presentable symmetric monoidal ∞-category
𝑉
V;

whether all tensor products are derived;

whether all colimits are homotopy colimits;

dualizability hypotheses when you use Verdier duality / Poincaré duality.

Without this, statements like “Verdier dual gives the Koszul dual coalgebra” aren’t meaningful.

C2) Definition: (Pre)factorization algebra vs “E1-chiral algebra”

Right now, you use “E1-chiral algebra” in a way that looks like “nonlocal vertex algebra” / “ordered configuration operations” (your own comparison says E1 extends BD by dropping skew-symmetry).

main

Proposed precise replacement definition (operadic):

An E1-chiral algebra on a complex curve
𝑋
X is a prefactorization algebra
𝐴
A valued in
𝑉
V on
𝑋
X whose structure maps are indexed by ordered finite configurations (no symmetric-group invariance required), satisfying associativity/factorization for iterated disjoint unions, and satisfying a holomorphic/locality condition (e.g. dependence only on punctured disks and meromorphic extension across diagonals with prescribed pole orders).

Concretely: use the colored operad of ordered configuration spaces
C
o
n
f
𝑛
o
r
d
(
𝐷
)
Conf
n
ord
	​

(D) (rather than unordered), possibly enhanced by logarithmic forms/residues, as the operad acting on local observables. The “E∞-chiral” / “fully local” version should then be your “unordered +
Σ
𝑛
Σ
n
	​

-equivariant” factorization structure (but please do not call it E∞ unless you explicitly explain why this terminology is not the usual E∞).

Editorial suggestion: rename:

“E∞-chiral” → “fully local chiral” or “vertex/chiral (unordered)”

“E1-chiral” → “ordered chiral” or “associative chiral”

C3) Definition: Chiral algebra (BD) vs vertex algebra vs holomorphic factorization algebra

You need a precise statement of which model you are using:

BD chiral algebra = right D-module on Ran
(
𝑋
)
(X) with factorization product.

VOA = translation-invariant BD chiral algebra on
𝑋
=
𝐴
1
X=A
1
 (under standard equivalence assumptions).

If you are mixing BD and Costello–Gwilliam holomorphic factorization algebras, you need an explicit “dictionary theorem” (even if proved elsewhere) stating equivalences and limitations.

C4) Definition: Genus-graded geometric bar complex

You already have a definition (Definition 5.1.7) but it needs a cleaned version with explicit functoriality and input/output categories (e.g. “outputs a conilpotent chiral coalgebra in
𝑉
V”).

main

Proposed replacement definition:

For an augmented chiral algebra
𝐴
A on
𝑋
X, define
B
a
r
c
h
(
𝐴
)
Bar
ch
(A) as the (co)end over the exit-path ∞-category of the Fulton–MacPherson compactification of configurations, with coefficients given by
𝐴
⊠
𝑛
A
⊠n
 tensored with the logarithmic de Rham complex and pushed forward along the structure map to Ran
(
𝑋
)
(X). The differential is
𝑑
=
𝑑
i
n
t
+
𝑑
d
R
+
𝑑
r
e
s
d=d
int
	​

+d
dR
	​

+d
res
	​

, where
𝑑
r
e
s
d
res
	​

 is the sum of boundary-residue maps along codimension-one diagonals.

Then theorems become meaningful: (i)
𝑑
2
d
2
 equals curvature, (ii) coassociativity from boundary stratification, etc.

C5) Definition: Curvature/backreaction class

You use “curvature”, “backreaction”, “central extension” interchangeably in places (e.g., the
𝑑
ˉ
2
d
ˉ
2
 discussion).

main

Proposed precise definition:

For a curved chiral algebra (or curved
𝐴
∞
A
∞
	​

 object), define curvature
𝑚
0
∈
𝐴
2
m
0
	​

∈A
2
 (or appropriate degree depending on conventions) satisfying the curved
𝐴
∞
A
∞
	​

 identities.

Define the backreaction class as the obstruction in the bar complex: the component of
𝑑
2
d
2
 in the lowest filtration degree, identified with insertion of
𝑚
0
m
0
	​

 (or a central class corresponding to the anomaly).

Then you can prove:
𝑑
2
=
0
d
2
=0 iff this class vanishes (or is gauge-trivial) in the appropriate completed sense.

C6) Definition: Koszul dual without circularity

This is the keystone.

Your Chapter 6 already defines a “Chiral Koszul pair via NAP”.

main


But Appendix E admits circularity.

main


And Theorem 6.7.1 is exactly the missing bridge.

main

Proposed precise replacement definition:

Let
𝐴
A be an augmented chiral algebra on an oriented 1-manifold/curve
𝑋
X in a symmetric monoidal stable ∞-category
𝑉
V, satisfying a pro-nilpotence / completeness hypothesis ensuring dualizability of the associated factorization object on Ran
(
𝑋
)
(X). Define the Koszul dual chiral coalgebra
𝐴
!
A
!
 to be the Verdier dual
𝐷
(
𝐴
)
D(A) of the corresponding factorization D-module (or sheaf) on Ran
(
𝑋
)
(X), twisted by the orientation local system and shifted so that factorization coproducts match boundary stratification maps.
Then define the Koszul pairing
𝐴
⊗
𝐴
!
→
𝜔
𝑋
A⊗A
!
→ω
X
	​

 as the canonical evaluation map.

Then the main theorem is:
B
a
r
c
h
(
𝐴
)
≃
𝐴
!
Bar
ch
(A)≃A
!
 (and similarly cobar recovers
𝐴
A). That removes the circularity.

C7) Definition: Convergence/completion hypotheses

You repeatedly invoke completions and convergence (e.g. Theorem 5.9.17 and Chapter 14).

You need a clean “axiom schema”:

weight/energy grading
𝐴
=
⨁
𝑛
≥
0
𝐴
(
𝑛
)
A=⨁
n≥0
	​

A(n),

filtration
𝐹
𝑝
𝐴
F
p
A exhaustive & complete,

bounded pole order relative to weight,

pro-nilpotence so that infinite configuration sums converge.

State these as “Standing Assumptions (SA1–SA5)”.

D. Specific corrections (mathematical, not stylistic)

Here’s a concrete list of “must change” items that are not just “proof missing”.

Fix transposition for
𝜂
𝑖
𝑗
η
ij
	​

: the differential forms satisfy
𝜂
𝑗
𝑖
=
𝜂
𝑖
𝑗
η
ji
	​

=η
ij
	​

, while antisymmetry belongs to Orlik–Solomon generators; update Table C.3 accordingly.

Resolve circular Koszul-dual definition: replace Appendix E Definition E.1.3 with a non-circular intrinsic definition (Verdier dual / universal property), then make Theorem 6.7.1 the proof that your bar model computes it.

main

main

Correct/qualify
𝑑
ˉ
2
=
0
d
ˉ
2
=0 claim: replace with a theorem “
𝑑
ˉ
2
d
ˉ
2
 equals curvature insertion; vanishes under hypotheses X/Y/Z” rather than “for all VOAs/CFTs”.

main

Downgrade or prove the primary example dualities: Heisenberg self-duality, Kac–Moody↔W at dual level, Virasoro↔
𝑊
1
+
∞
W
1+∞
	​

 must become theorems with proofs or be marked conjectural.

main

Clarify the “generic Kac–Moody chiral homology is 0” assertion: define precisely what “chiral homology” means here (factorization homology of what object on what manifold?), and state hypotheses.

main

Fix appendix labels / cross-references: multiple “Appendix C” etc must be renumbered, and placeholders like “Chapter [NAP]” removed.

main

E. New theorems plausibly provable with the current machinery

These are not random wish-list items; they are theorems that your current pipeline (configuration-space compactifications + residues + bar/cobar + Verdier duality + filtrations/completion + homotopy transfer) is already engineered to prove.

I’m writing them in a way that would read like actual Annals-grade statements (precise hypotheses + meaningful conclusion). You can decide which are the “main theorems” of the book.

E1) Intrinsic chiral Koszul duality theorem (resolves circularity)

Candidate Theorem (upgrade of 6.7.1):
Let
𝐴
A be an augmented chiral algebra on a curve
𝑋
X satisfying (i) locally finite energy grading, (ii) complete descending filtration compatible with OPE pole order, (iii) pro-nilpotence for augmentation ideal. Then:

the Verdier dual
𝐴
!
:
=
𝐷
(
𝐴
)
⊗
o
r
𝑋
[
dim
⁡
𝑋
]
A
!
:=D(A)⊗or
X
	​

[dimX] carries a canonical structure of conilpotent chiral coalgebra, and

the geometric bar construction
B
a
r
c
h
(
𝐴
)
Bar
ch
(A) is canonically quasi-isomorphic to
𝐴
!
A
!
 as chiral coalgebras, and

the cobar construction recovers
𝐴
A up to filtered quasi-isomorphism.

This is exactly what your narrative is building to; it just needs to be made sharp and proved. (You already frame this goal around NAP/Verdier duality.)

main

main

E2) Curvature-square theorem (correct replacement for “
𝑑
ˉ
2
=
0
d
ˉ
2
=0”)

Candidate Theorem:
For an augmented chiral algebra
𝐴
A whose OPE has at most second-order poles and whose “anomaly” class
𝑚
0
m
0
	​

 is central (in the precise sense of acting trivially on all factorization modules), the bar differential satisfies

𝑑
ˉ
2
=
𝜄
(
𝑚
0
)
d
ˉ
2
=ι(m
0
	​

)

(insertion of curvature). In particular,
𝑑
ˉ
2
=
0
d
ˉ
2
=0 iff
𝑚
0
m
0
	​

 vanishes (or is gauge-trivial) in the completed filtration.

This formalizes what you are gesturing at in §5.8.9 but without the overreach.

main

E3) Functoriality theorem for bar under étale maps / pushforward

Upgrade your open functoriality results (5.8.17/5.8.18/5.8.22) to a single cohesive statement:

Candidate Theorem:
The chiral bar construction defines a symmetric monoidal functor

B
a
r
c
h
:
A
l
g
c
h
a
u
g
(
𝑋
)
→
C
o
a
l
g
c
h
c
o
n
i
l
(
𝑋
)
Bar
ch
:Alg
ch
aug
	​

(X)→Coalg
ch
conil
	​

(X)

compatible with pullback along étale maps
𝑓
:
𝑌
→
𝑋
f:Y→X, and with proper pushforward in the D-module setting, under standard finiteness hypotheses.

E4) Convergence theorem via positive-energy filtration

Candidate Theorem (upgrade of 5.9.17 / 14.6.8):
If
𝐴
A is graded by conformal weight
𝐴
=
⨁
𝑛
≥
0
𝐴
(
𝑛
)
A=⨁
n≥0
	​

A(n) and OPE pole order between weight
𝑛
n and
𝑚
m is bounded by a linear function
𝑃
(
𝑛
,
𝑚
)
P(n,m) with
𝑃
(
𝑛
,
𝑚
)
≤
𝑛
+
𝑚
−
𝐶
P(n,m)≤n+m−C for some
𝐶
>
0
C>0, then the completed genus-graded bar complex converges and the associated spectral sequence is strongly convergent.

This is exactly the kind of technical result Annals referees will demand to justify “completed bar complex”.

E5) Module-category Koszul duality theorem

This is the missing “representation theory engine” theorem.

Candidate Theorem:
Under the same hypotheses as E1, the ∞-category of factorization (chiral) modules over
𝐴
A is equivalent to the ∞-category of comodules over
𝐴
!
A
!
, via twisting cochains induced by the universal bar–cobar adjunction.

This would turn your example computations into actual representation theory consequences.

E6) Heisenberg self-duality with explicit coalgebra model

You explicitly note that Heisenberg is not quadratic in the standard sense because the double pole behaves like curvature.

main

Candidate Theorem:
Let
𝐻
𝜅
H
κ
	​

 be the Heisenberg chiral algebra at level
𝜅
κ. Then
B
a
r
c
h
(
𝐻
𝜅
)
Bar
ch
(H
κ
	​

) is quasi-isomorphic to a cofree conilpotent coalgebra on one generator with curvature determined by
𝜅
κ, and after the canonical completion, the Koszul dual is equivalent to
𝐻
−
𝜅
H
−κ
	​

.

This matches the “primary examples” claim but now it is properly conditioned.

E7) Lattice E1-chiral duality via cocycle inversion

Your “E1-chiral lattice algebra with non-symmetric cocycle” claim can become a clean theorem:

Candidate Theorem:
Let
𝑉
𝐿
,
𝜖
V
L,ϵ
	​

 be a lattice-type E1-chiral algebra determined by a 2-cocycle
𝜖
ϵ on
𝐿
L. Under standard finiteness hypotheses (e.g.
𝐿
L finitely generated,
𝜖
ϵ unitary), the Koszul dual satisfies

𝑉
𝐿
,
𝜖
!
≃
𝑉
𝐿
,
𝜖
−
1
V
L,ϵ
!
	​

≃V
L,ϵ
−1
	​


in the completed E1-chiral category, and the duality identifies module categories by cocycle-twisted Fourier transform.

E8) Kac–Moody ↔ W-algebra as Koszul duality (careful formulation)

Your manuscript asserts this strongly.

main


To make it plausibly provable, formulate it as:

Candidate Theorem (restricted):
For
𝑔
^
𝑘
g
	​

k
	​

 at noncritical level, the Koszul dual of the BRST-reduced chiral algebra (or of a precisely specified extension with curvature) is equivalent to the corresponding
𝑊
W-algebra
𝑊
𝑔
,
𝑘
′
W
g,k
′
	​

 at dual level
𝑘
′
k
′
, provided the bar differential’s curvature class matches the BRST anomaly class.

This is believable if your machinery already encodes BRST reduction as a bar/cobar construction (many of your chapters suggest you’re setting that up).

E9) Virasoro ↔
𝑊
1
+
∞
W
1+∞
	​

: downgrade to conjecture unless you can prove

Given current state, this should be explicitly framed as conjectural until you have a chain-level construction and convergence proof. The claim appears in your “primary examples” list.

main

F. What to do next (so the book becomes “Annals-grade” rather than “ambitious notes”)

If you want the manuscript to read like breakthrough mathematics rather than a program:

Make Theorem 6.7.1 your Main Theorem (intrinsic Koszul dual, non-circular), and prove it completely. Right now it’s [open].

main

Fix curvature properly: replace §5.8.9’s universal
𝑑
ˉ
2
=
0
d
ˉ
2
=0 claim by a curvature-insertion theorem + precise vanishing criterion.

main

Choose 2–3 flagship examples and actually finish them:

Heisenberg (complete and explicit)

Free fermion / βγ (complete and explicit)

One nontrivial W-algebra (e.g.
𝑊
3
W
3
	​

)
These should have fully worked bar complexes, explicit coalgebra structures, and a real module-category corollary.

Clean the internal logic (appendix labels, sign convention contradictions, placeholders). These are easy but essential.

