According to a document from 2026-02-28, I did two passes on main.pdf:

a mechanical audit of every statement explicitly tagged [open] or [proved elsewhere] (these are, by your own markup, the places that still need proofs or airtight citations), and

a mathematical critique pass focused on correctness, missing hypotheses/definitions, and where the current machinery can plausibly support genuinely new “Annals-grade” theorems—especially around E1‑chiral algebras, chiral Koszul duality, and representation theory.

Deliverable: exhaustive chapter-by-chapter proof/citation checklist

I compiled every [open] and [proved elsewhere] item into a single chapter-indexed spreadsheet (with type, number, title, status, PDF page, and an “action required” column).



chiral_duality_math_audit_open_external.xlsx
Sheet1



This file is the exhaustive list (for the current PDF) of formally-flagged assertions that still need proofs or verified citations/hypotheses.

Five high-impact mathematical issues that need correction (not just “add a proof”)

These are places where the statement as written is very likely false as stated or missing essential hypotheses, and therefore can’t be “fixed” by just appending a proof.

1) Factorization algebras: “cosheaf for open covers” vs “Weiss cosheaf”

In Ch. 3 you state (in multiple spots) that factorization algebras satisfy an ordinary cosheaf/gluing property and even a Mayer–Vietoris type excision statement for general open covers. E.g. the text states a cosheaf theorem for factorization algebras and an excision-style equivalence.

main



In the standard definitions (Ayala–Francis; Costello–Gwilliam; Lurie-style), the cosheaf condition is for Weiss covers / factorizing covers, not arbitrary open covers. Ayala–Francis explicitly frame factorization algebras as (locally constant) Weiss cosheaves on the poset of opens (or disks), and this distinction is not cosmetic—it is foundational.

ayala-francis



What to fix (precise replacement):

Replace “cosheaf for any open cover” with “cosheaf for Weiss covers” (and define Weiss covers).

Replace “excision for opens U,V with pushout” with the correct ⊗‑excision/collar-gluing statement at the level of factorization homology, not the raw functor of opens (unless you’re in an extremely special setting).

2) E∞‑chiral vs vertex algebra vs BD chiral algebra: the equivalences need hypotheses and (likely) reframing

Your definitions currently present E∞‑chiral as “commutative algebra object in the chiral compound tensor ∞‑category,” and then list as “equivalent” (i) vertex algebras, (ii) Beilinson–Drinfeld chiral algebras, (iii) fully commutative factorization algebras.

main



As written, that collapses at least three different layers that normally require extra structure (holomorphicity/translation invariance; D‑module vs chain-complex models; locally constant vs singular support; and “Lie-chiral” vs “commutative factorization coalgebra” conventions).



What to fix (conceptual correction):
You need an explicit, typed dictionary:

(A) “BD chiral algebra” in the D‑module pseudo-tensor sense (typically Lie‑type operations),

(B) “factorization algebra” (typically commutative along disjoint unions, but with singularities/locality encoded in structure maps),

(C) “vertex algebra” as a translation-equivariant holomorphic factorization algebra on
𝐶
C (à la Costello–Gwilliam) or as BD data on
𝐴
1
A
1
 with vacuum/translation.

Right now, the book’s terminology makes it too easy for a reader to infer a literally false statement (“vertex algebras are commutative algebra objects” in a naive monoidal category sense).

3) E1‑chiral: you need an ordered (non‑Σ) factorization framework, otherwise “E1” is ill-posed

The current E1‑chiral definition says “associative but not commutative algebra object” and equates this with “nonlocal vertex algebra” and “factorization algebra with weakened factorization constraints.”

main



This is plausible, but only if you formalize the operadic side correctly: ordinary factorization algebras are inherently symmetric in the labels of points (Σ-actions). An “E1” analogue usually means you pass to ordered configurations (non‑Σ operads) or to “
𝐸
1
E
1
	​

 in a braided/sifted monoidal context,” etc.



What to fix:
Add a precise definition of an ordered Ran space or “non‑Σ factorization algebra,” and define the chiral associative operad
A
s
s
c
h
Ass
ch
	​

 as an actual operad in your target ∞‑category. Without that, “E1‑factorization constraint” is not a mathematically stable phrase.

4) Yangian definition in the Ch. 9 overview is not an RTT presentation

In Ch. 9’s overview you give a “Yangian – RTT presentation” definition in terms of generators
𝐽
𝑛
𝑎
J
n
a
	​

 and a commutator expansion.

main



That is not the RTT presentation. RTT is a matrix relation
𝑅
(
𝑢
−
𝑣
)
𝑇
(
𝑢
)
𝑇
(
𝑣
)
=
𝑇
(
𝑣
)
𝑇
(
𝑢
)
𝑅
(
𝑢
−
𝑣
)
R(u−v)T(u)T(v)=T(v)T(u)R(u−v), and Drinfeld’s realizations involve additional structure and relations (including Serre-type constraints). You do later discuss RTT-style material in the dedicated Yangian chapter.

main



What to fix:
Either:

rename the Ch. 9 item as “schematic Lie-bialgebraic expansion / heuristic,” or

replace it by an actual RTT definition (and specify which
𝑅
R-matrix; rational/trigonometric;
𝑔
𝑙
𝑛
gl
n
	​

 vs general
𝑔
g).

5) “Chapter [NAP]” placeholder is still present in the manuscript

There’s an explicit placeholder note in the NAP-duality computations chapter indicating it should be “placed as Chapter [NAP].”



That’s a structural break: it signals that the logical dependency graph of the book (where NAP duality is introduced, what it assumes, what it proves) is not yet consistent.

Definition patchset: missing or imprecise definitions that must be made formal

Below are the definitions I’d treat as mandatory to repair logical gaps. I’m writing them as “drop-in replacements” you can paste in (adapt to your notation).

Patch D1: ambient category and dualities

Fix once and for all:

A base field
𝑘
k (likely
𝑘
=
𝐶
k=C).

A symmetric monoidal stable ∞‑category
(
𝑉
,
⊗
,
\mathbbm
1
)
(V,⊗,\mathbbm1) in which your algebras live (e.g.
C
h
(
𝑘
)
Ch(k), or a derived category of
𝐷
D-modules with
⊗
!
⊗
!
, etc.).

Two different dualities must be distinguished:

linear dual
𝑉
∨
=
H
o
m
𝑘
(
𝑉
,
𝑘
)
V
∨
=Hom
k
	​

(V,k) (only works well for dualizable objects),

Verdier dual
𝐷
D (on sheaves/D‑modules), which comes with shifts and orientation twists.

Your notation summary already uses Verdier dual style expressions like
𝐷
(
𝐵
‾
(
𝐴
)
)
⊗
𝜔
−
1
D(
B
(A))⊗ω
−1
. If you use that, you must state which category and which dual.

Patch D2: Weiss cover

A family
{
𝑈
𝑖
}
𝑖
∈
𝐼
{U
i
	​

}
i∈I
	​

 of opens in a manifold
𝑀
M is a Weiss cover if every finite subset
𝑆
⊂
𝑀
S⊂M is contained in some
𝑈
𝑖
U
i
	​

.

Patch D3: factorization algebra (corrected)

A prefactorization algebra
𝐹
F on
𝑀
M valued in
𝑉
V is:

an assignment
𝑈
↦
𝐹
(
𝑈
)
∈
𝑉
U↦F(U)∈V for opens
𝑈
⊂
𝑀
U⊂M,

for every finite disjoint family
𝑈
1
,
…
,
𝑈
𝑛
⊂
𝑉
U
1
	​

,…,U
n
	​

⊂V structure maps

𝐹
(
𝑈
1
)
⊗
⋯
⊗
𝐹
(
𝑈
𝑛
)
→
𝐹
(
𝑉
)
,
F(U
1
	​

)⊗⋯⊗F(U
n
	​

)→F(V),

compatible with refinement and symmetric group actions,

and a unit
\mathbbm
1
→
𝐹
(
𝑈
)
\mathbbm1→F(U) for each
𝑈
U.

A factorization algebra is a prefactorization algebra whose underlying functor
𝑈
↦
𝐹
(
𝑈
)
U↦F(U) is a cosheaf for Weiss covers (i.e. satisfies the cosheaf colimit condition for Weiss covers).



This is the corrected target for your Ch. 3 “cosheaf” results.

main

ayala-francis

Patch D4: E∞‑chiral algebra (make it honest)

Pick one of these two consistent choices, and stick to it:



Option A (factorization-first, Costello–Gwilliam style):
An E∞‑chiral algebra on a complex curve
𝑋
X is a holomorphic factorization algebra on
𝑋
X valued in
C
h
(
𝑘
)
Ch(k) satisfying translation-equivariance when
𝑋
=
𝐶
X=C.
Then a theorem (proved elsewhere) gives an equivalence with vertex algebras under standard finiteness/locality hypotheses.



Option B (BD-first):
A BD chiral algebra is (roughly) a
𝐷
𝑋
D
X
	​

-module with chiral operations satisfying Jacobi (Lie‑type), and vertex algebras correspond to certain translation-invariant BD chiral algebras on
𝐴
1
A
1
 with a vacuum/translation operator.
If you use this option, you must not call it “commutative algebra object” unless you’ve defined a monoidal structure in which that is literally correct.



Right now your text asserts these equivalences without the necessary scaffolding.

main

Patch D5: E1‑chiral algebra (ordered factorization)

An E1‑chiral algebra should be defined as an algebra over a non‑Σ (ordered) chiral operad
A
s
s
c
h
Ass
ch
	​

, i.e. structure maps indexed by ordered configurations, satisfying
𝐴
∞
A
∞
	​

/associativity constraints but without Σ‑commutativity.



This is the missing technical backbone behind “factorization algebra with only E1-associativity.”

main

Patch D6: augmented/complete conditions for bar–cobar and Koszul duality

You need a clear definition of:

augmented chiral algebra
𝐴
→
\mathbbm
1
A→\mathbbm1,

augmentation ideal
𝐼
=
ker
⁡
(
𝐴
→
\mathbbm
1
)
I=ker(A→\mathbbm1),

pro-nilpotent /
𝐼
I-adically complete conditions,

dualizability conditions needed to apply
𝐷
D or
(
−
)
∨
(−)
∨
.

Without this, chiral Koszul duality statements are missing hypotheses.

Patch D7: configuration spaces and log forms on curves

When you define complexes like “logarithmic forms on configuration spaces” you must specify:

which compactification
𝐶
𝑛
(
𝑋
)
C
n
	​

(X) you mean (Fulton–MacPherson / wonderful compactification),

the boundary divisor
𝐷
D (“collision divisor”),

Ω
𝐶
𝑛
(
𝑋
)
∙
(
log
⁡
𝐷
)
Ω
C
n
	​

(X)
∙
	​

(logD) and residue maps
R
e
s
𝐷
𝑖
𝑗
Res
D
ij
	​

	​

.

You already cite Arnold–Orlik–Solomon relations as the mechanism making residue differentials square to zero; that needs a clean definition of the residue operators and the relations you impose.

Patch D8: modules (representation theory infrastructure)

You need a definition of:

factorization module over a factorization algebra (the Ran-with-a-marked-point / Swiss-cheese picture),

E1‑chiral module (ordered version),

the derived category
M
o
d
𝐴
Mod
A
	​

 you will study (dg category, stable ∞‑category), and whether you assume presentability/compact-generation.

This is the prerequisite for “deep representation theory.”

Annals-grade theorem targets that look plausibly provable with your current machinery

These are statements that (i) match the book’s existing constructions, and (ii) if proved cleanly, would be legitimately substantial. I’m phrasing them in “paper theorem” form, with a proof strategy sketch.

Target T1: Corrected cosheaf theorem

Theorem (Weiss cosheaf property). Every factorization algebra
𝐹
F on
𝑀
M (in the Ayala–Francis/Costello–Gwilliam sense) is a cosheaf for Weiss covers; conversely, a prefactorization algebra satisfying Weiss cosheaf is a factorization algebra.



Proof strategy: formal; unwind definitions. This replaces the currently over-strong “any open cover” claim.

main

ayala-francis

Target T2: Ordered factorization ⇔ nonlocal vertex algebra

Theorem. Translation-equivariant ordered (non‑Σ) holomorphic factorization algebras on
𝐶
C are equivalent to nonlocal vertex algebras (Li-type) satisfying vacuum/translation/weak associativity.



Proof strategy: adapt the Costello–Gwilliam equivalence “vertex ⇔ factorization” but track the Σ-action; remove commutativity/locality and work with ordered configuration spaces.



This would put your E1‑chiral definition on a rock-solid operadic foundation.

Target T3: Geometric bar model computes the operadic bar construction

You already advertise a “geometric bar construction” and tie it to operadic bar/cobar. One of your flagship items is exactly this. 【1.7.x style, and Ch. 1 open items】



Theorem. For an augmented E∞‑chiral algebra
𝐴
A on a curve
𝑋
X satisfying mild finiteness/completeness, the operadic bar construction
𝐵
c
h
(
𝐴
)
B
ch
	​

(A) is quasi-isomorphic to the configuration-space model built from
Ω
∙
(
log
⁡
𝐷
)
Ω
∙
(logD) with residue differential.



Proof strategy: show the configuration-space complex is a (co)simplicial resolution of the Ran cosheaf computing factorization homology; identify its totalization with operadic bar via the universal property of the bar construction.

Target T4: Residue differential squares to zero via Arnold–Orlik–Solomon relations (fully rigorous)

You reference Arnold relations as the reason residue terms anticommute / square to zero.



Theorem. In the configuration-space log complex
Ω
∙
(
log
⁡
𝐷
)
Ω
∙
(logD), the total residue operator
𝑑
r
e
s
=
∑
𝑖
<
𝑗
R
e
s
𝐷
𝑖
𝑗
d
res
	​

=∑
i<j
	​

Res
D
ij
	​

	​

 satisfies
𝑑
r
e
s
2
=
0
d
res
2
	​

=0, and
[
𝑑
d
R
,
𝑑
r
e
s
]
=
0
[d
dR
	​

,d
res
	​

]=0 up to the sign conventions used, yielding a genuine differential on the geometric bar complex.



Proof strategy: standard in Orlik–Solomon settings, but you must write it with your exact divisors/signs/degree shifts.

Target T5: Chiral Koszul duality for E1‑chiral algebras

Theorem (Chiral associative Koszul duality). Under suitable completeness/pro-nilpotence hypotheses, augmented E1‑chiral algebras are equivalent (via bar/cobar) to conilpotent E1‑chiral coalgebras, and the double dual map
𝐴
→
(
𝐴
!
)
!
A→(A
!
)
!
 is an equivalence.



Proof strategy: reduce to Koszul duality for
A
s
s
Ass in a stable ∞‑category, then prove compatibility of your chiral operadic model
A
s
s
c
h
Ass
ch
	​

 with the bar/cobar constructions built from configuration spaces.



This is one of the cleanest “new” theorems your framework promises, and it is exactly what would differentiate the book from existing accounts.

Target T6: Koszul duality for module categories

Theorem. If
𝐴
A is augmented and complete (E1‑ or E∞‑chiral) and
𝐴
!
A
!
 is its Koszul dual coalgebra, then the derived ∞‑category of (factorization)
𝐴
A-modules is equivalent to the derived ∞‑category of
𝐴
!
A
!
-comodules (with the expected conilpotence/completion conditions).



Proof strategy: standard bar resolution argument internal to the chiral/factorization module formalism; but you must build the module theory first (Patch D8).

Target T7: Chiral Hochschild = factorization homology on
𝑆
1
S
1
 (and invariance)

Theorem. For a chiral algebra
𝐴
A satisfying your standing hypotheses,

𝐻
𝐻
c
h
(
𝐴
)
  
≃
  
∫
𝑆
1
𝐴
HH
ch
	​

(A)≃∫
S
1
	​

A

and
𝐻
𝐻
c
h
(
𝐴
)
≃
𝐻
𝐻
c
h
(
𝐴
!
)
HH
ch
	​

(A)≃HH
ch
	​

(A
!
) for Koszul dual pairs (up to a canonical twist).



Proof strategy: identify both sides as endomorphisms of the unit in the module ∞‑category; use module Koszul duality.

Target T8: Explicit Koszul dual OPE’s for primary examples

You have several “closed form OPE” theorems (e.g. in W-algebra Koszul dual chapter). The Annals-grade version is:



Theorem. For each primary example (Heisenberg,
𝛽
𝛾
βγ, affine
𝑉
𝑘
(
𝑔
)
V
k
	​

(g),
𝑊
𝑘
(
𝑔
)
W
k
	​

(g), Yangian/Yangian vertex algebra, toroidal/elliptic), the Koszul dual
𝐴
!
A
!
 admits an explicit OPE presentation whose structure constants are obtained by a universal configuration-space integral formula, and these presentations recover known dualities (DS reduction / Feigin–Frenkel-type) as specializations.



Proof strategy: develop a uniform operadic/graphical “integral formula” for OPE coefficients in the dual, then evaluate it in each example using your configuration-space calculus + known free-field realizations.

Representation theory: what you need to add to make Part II “deep” (and actually new)

Right now the manuscript builds lots of algebras and dualities, but “representation theory” needs a consistent “category-of-modules” lens and computations that are not just re-statements of known facts.



Here are concrete additions that would make it feel like a breakthrough program:

(R1) Define the universal module categories

For each chiral algebra type you study, define:

factorization modules on
𝑋
X with one marked point (the standard replacement for “vertex modules”),

in the E1 setting, define ordered factorization modules (non‑Σ “Swiss-cheese” / “little interval with boundary” structure),

specify finiteness: e.g. presentable stable ∞‑category, compact objects, t‑structure if used.

Then prove comparison with classical notions in your examples:

vertex modules for E∞,

nonlocal/quantum vertex modules for E1,

Wakimoto/Fock modules via free-field constructions.

(R2) Compute something invariant and nontrivial

For each primary family, compute at least one of:

Ext-algebras between standard modules,

block decomposition / linkage,

fusion rules (even in a restricted subcategory),

characters / graded dimensions (and modular transformation properties when relevant),

factorization homology with coefficients in a module.

(R3) Use Koszul duality to produce representation equivalences

This is where “Annals-grade novelty” can happen:

Show Koszul duality induces a derived Morita-type equivalence between module categories (Target T6).

In examples, identify this equivalence with known dualities (DS reduction, Koszul duality for Lie algebras, BGG-type dualities), but derived from your configuration-space model.

(R4) Primary examples: very concrete “what to prove”

Heisenberg / lattice: classify irreducible factorization modules, compute fusion with Fock modules, recover discriminant group story.

𝛽
𝛾
βγ: identify the module category with
𝐷
D-modules on the underlying vector space (or loop space truncation) in a precise sense; compute HH
c
h
ch
	​

.

Affine
𝑉
𝑘
(
𝑔
)
V
k
	​

(g): define the factorization module category and compare with
𝑔
^
g
	​

-modules in category
𝑂
O; then prove how Koszul duality interacts with DS reduction.

W‑algebras: compute the dual side’s standard modules and their Ext’s (Arakawa-type results are the gold standard, but your framework could produce new proofs or new generalizations).

Yangians / shifted Yangians: define the E1‑chiral module category; relate to known Yangian category
𝑂
O and quiver variety constructions; then state and prove your Koszul dual predictions.

Chapter-by-chapter audit summary

Below is the chapter-by-chapter actionable view: (i) how many items are tagged [open]/[proved elsewhere], (ii) the top proof obligations, (iii) what definitions are missing/fragile, and (iv) “new theorem targets” that are plausible given what the chapter already sets up.



For the full exhaustive list of all tagged assertions by chapter, use the spreadsheet.

Chapter 1 — Introduction

Tagged items: 13 open / 0 external



Top proof obligations (from your own tags):

Thm 1.2.1 Unification via configuration spaces (OPEN, p.40)

Thm 1.7.1 Geometric Bar Construction, Theorem 3.2 (OPEN, p.43)

Thm 1.7.3 Geometric Cobar Construction, Theorem 3.5 (OPEN, p.44)

Thm 1.7.4 Full Genus Bar Complex, Theorem 5.1 (OPEN, p.44)

Thm 1.9.1 Arnold–Orlik–Solomon relations (OPEN, p.47)

Corrections / missing definitions:

Fix the E∞/E1 equivalence claims (Patch D4–D5). The current “equivalently … vertex algebra … BD chiral algebra … commutative factorization algebra” needs hypotheses and probably a rewording.

main

State the exact duality functor used in
𝐴
!
A
!
 (Verdier vs linear) and the required dualizability/compactness.

Plausible new theorem targets:

“Ordered factorization ⇔ nonlocal vertex algebra” (Target T2).

“Module Koszul duality” specialized to curve factorization modules (Target T6).

Chapter 2 — Algebraic Foundations and Bar Constructions

Tagged items: 2 open / 1 external



Top proof obligations:

Thm 2.2.2 Heisenberg Koszul Duality – definitive statement (OPEN, p.57)

Thm 2.2.8 Comparison: your approach vs GLZ (OPEN, p.60)

Thm 2.1.7 Classical Koszul pairs (EXT, p.54)

Corrections / missing definitions:

Define “complete / pronilpotent” hypotheses explicitly before invoking bar–cobar equivalences (Patch D6).

If “GLZ” is used as a reference anchor, give full bibliographic identification and state exactly what theorem is being imported.

Plausible new theorem targets:

A clean “Ass
c
h
ch
	​

 is Koszul” statement (in the chiral category you use) plus a complete proof.

Chapter 3 — Operadic Foundations and Bar Constructions

Tagged items: 3 open / 1 external



Top proof obligations:

Thm 3.5.2 Operadic bar complex (OPEN, p.69)

Thm 3.10.9 Factorization algebras are cosheaves (OPEN, p.76)

Prop 3.9.1 Quadratic presentations (OPEN, p.71)

Thm 3.2.3 Chiral algebras on Ran space (EXT, p.64)

Corrections / missing definitions:

Correct the “cosheaf” theorem to Weiss covers (Patch D2–D3). As stated it’s too strong.

main

Add a definition of Weiss cover and cite the correct source statement (Ayala–Francis).

ayala-francis

Plausible new theorem targets:

A theorem identifying your “operadic bar complex” with configuration-space totalizations (bridge to Ch. 5).

Chapter 4 — Configuration Spaces and Logarithmic Forms

Tagged items: 16 open / 7 external



Top proof obligations (sample):

Thm 4.1.34 Logarithmic forms and residues (OPEN, p.91)

Thm 4.2.1 Configuration space compactifications (OPEN, p.104)

Thm 4.4.7 Chiral algebras as factorization algebras (OPEN, p.115)

plus several external theorems you cite but haven’t localized to your setup.

Corrections / missing definitions:

You must define
𝐶
𝑛
(
𝑋
)
C
n
	​

(X) and
Ω
∙
(
log
⁡
𝐷
)
Ω
∙
(logD) precisely (Patch D7) before residues appear in differentials.

If you use Orlik–Solomon/Arnold relations in the curve setting, specify the curve hypotheses (genus, punctures) and which arrangement model you’re using.

Plausible new theorem targets:

A genus‑
𝑔
g Orlik–Solomon theorem for your specific compactification, tuned to the residues you need for the bar differential.

Chapter 5 — The Bar Construction

Tagged items: 19 open / 8 external



Top proof obligations (sample):

Thm 5.1.1 Geometric bar construction (OPEN, p.132)

Thm 5.4.1 Geometric cobar construction (OPEN, p.142)

Thm 5.9.2 E1‑chiral algebra via bar (OPEN, p.150)

Corrections / missing definitions:

This chapter needs a completely explicit sign/degree convention for the three differentials (internal, residue, de Rham) and a proof of
𝑑
2
=
0
d
2
=0. You explicitly appeal to Arnold/Orlik–Solomon relations as the reason residue squares to zero.

Plausible new theorem targets:

The rigorous equivalence “geometric bar model ≃ operadic bar” (Target T3–T4).

Chapter 6 — Non-Abelian Poincaré Duality and Construction of Koszul Dual Cooperads

Tagged items: 20 open / 7 external



Top proof obligations (sample):

Thm 6.1.8 NAP duality (OPEN, p.166)

Thm 6.2.1 Construction of Koszul dual cooperads (OPEN, p.171)

Corrections / missing definitions:

State the exact hypotheses (locally constant? augmented? dualizable?) needed for NAP duality in your context.

Separate “factorization algebra duality” from “factorization homology duality.”

Plausible new theorem targets:

A clean chiral version of ⊗‑excision / collar gluing that is actually used later (so you can remove the open-cover confusion from Ch. 3).

Chapter 7 — Higher Genus Bar Construction

Tagged items: 15 open / 8 external



Corrections / missing definitions:

Define the modular operad / genus‑graded operad structure you’re using, including gluing maps and orientation lines.

Specify how central charge/anomaly enters as curvature (if that’s your mechanism).

Plausible new theorem targets:

A “quantum master equation” style theorem guaranteeing
𝑑
2
=
0
d
2
=0 in the higher-genus bar complex.

Chapter 8 — Across Genera

Tagged items: 18 open / 7 external



Corrections / missing definitions:

Clarify what is meant by “across genera”: is there a spectral sequence, a filtered colimit over genus, or a modular envelope construction?

Plausible new theorem targets:

A comparison theorem: genus‑graded bar complex filtered by genus has
𝐸
1
E
1
	​

 page = genus 0 bar complex and converges under explicit finiteness hypotheses.

Chapter 9 — Chiral Koszul Duality

Tagged items: 32 open / 10 external



High priority correction:

The Yangian overview definition labelled “RTT” is not RTT (see above).

main

Plausible new theorem targets:

The book’s central “chiral Koszul duality equivalence” with full hypotheses and proof (Target T5), plus module-level version (Target T6).

Chapters 10–15 (Machinery: classical origins, chiral Hochschild, modules, quantum corrections, Hochschild theory)

These chapters collectively have ~75 tagged items in the audit spreadsheet and will determine whether the book is logically watertight.



The single biggest addition needed here is Patch D8 (modules): without a formal factorization-module theory, the “representation theory” promise in Part II can’t be discharged.

Chapters 16–23 (Examples: lattice/fermions/βγ, Kac–Moody, W, deformation quantization, Yangians, toroidal/elliptic)

These chapters are where you can win “breakthrough” status—but only if you add the representation layer and make the Koszul duality computations truly structural.



Two concrete examples of “must-fix” issues:

Ch. 22 Yangians: You have an explicit claim that Yangian vertex algebras should be E1‑chiral, with “R‑twisted commutativity” and an open proof obligation.

main


This needs:

a precise definition of “R‑twisted commutativity” in your operadic setting, and

a proof via ordered/ braided factorization algebra technology.

Ch. 16 Examples: this chapter has 75 open items—too many for a reader to know what is “example sketch” vs “theorem.” You should either (a) split it into multiple chapters, or (b) explicitly label which statements are expository vs new vs claimed.

Chapters 24–27 (explicit genus expansions / modular forms / spectral sequences / detailed computations)

Tagged items: 0 (no [open]/[proved elsewhere] tags detected)



That’s good news: it likely means this portion is already written as “complete computations.”
The main critique here is integration: make sure every computational tool used has been defined earlier (especially if it relies on modular operads, anomalies, or spectral sequence convergence assumptions).

Chapter 28 — Explicit Computations via NAP Duality

Tagged items: 3 open / 0 external



Also contains the “Chapter [NAP]” placeholder remark.



You should remove the placeholder and ensure that the NAP theorem is introduced before the computations that use it.

Chapters 29–33 (Feynman diagrams, BV–BRST, boundary conditions/holomorphic twists, physical origins, concordance)

These are high-value narrative chapters. The most important thing to ensure is that:

they are logically downstream of the precise theorems, and

they do not introduce new undefined structures (BV operator, boundary factorization algebra, etc.) without a definition block.

Appendices A–G

Appendices A–F have many tagged items in the audit, meaning even your “background appendix” contains unproved results. That’s dangerous: appendices should be the most stable part.



Appendix G is notation/summary; it appears untagged.

What I recommend you do next (highest leverage)

Fix Ch. 3 terminology (Weiss vs ordinary covers) and propagate the correction everywhere. This is a “single bug” that can silently invalidate many downstream claims.

main

ayala-francis

Stabilize the E∞/E1 dictionary with an explicit ordered-factorization operad definition of E1-chiral (Patch D5). Then rewrite Defs 1.4.2–1.4.3 accordingly.

main

Prove the geometric bar/cobar equivalence (Targets T3–T4). This is the core new mathematics that will carry the book.

Build the module theory once (Patch D8), then apply it to each example systematically (R1–R4).

Repair the Yangian overview definition and enforce “RTT = RTT” throughout.

main

main

If you want, I can take the audit spreadsheet and (still chapter-by-chapter) add a second “Notes” column that proposes, for each open theorem/proposition, the minimal missing hypothesis and a likely proof route (configuration-space Stokes argument, operadic Koszulity reduction, reference to a specific known theorem, etc.). That would turn the checklist into a step-by-step proof-writing plan.
