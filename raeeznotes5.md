I’m going through the source tree as well as the PDF, not just the compiled narrative. I’ll focus first on the four main theorems and the formal fault-lines most likely to survive five audit rounds.

I’ve confirmed the full source bundle, audit notes, and self-assessment are present, and the live pressure points are now source-level propagation drift, higher-genus differential coherence, and theorem-versus-programme leakage.

I’ve now isolated two likely high-severity defects: a deformation theorem still overstates itself beyond the proof’s Koszul scope, and the higher-genus square-zero argument may not be justified operatorially. I’m checking whether those faults propagate into acyclicity, modular-Koszul claims, and any source-versus-PDF mismatch on where genus parameters live.

Thought for 43m 23s

According to a document from March 2026, the manuscript claims that all four main theorems are proved and that the chiral algebras in Part II are instances of a single “modular Koszul chiral algebra” package. I reviewed the current PDF and the uploaded TeX source tree directly: latest PDF, source tree. My conclusion is blunt:

The manuscript now has a real and substantial core, but it is still not in acceptable referee shape for Annals/Astérisque.
The reason is not “too many conjectures” or “over-ambition” by themselves. The reason is that two of the four main theorems are no longer genuinely proved theorems in the present source: they are partially built into the definitions of the objects to which they apply. In addition, Theorem C still contains a serious proof gap, and the book still contains a cross-chapter contradiction in Hochschild duality. Those are not stylistic matters; they are structural mathematical defects.

The good news is that the work is probably salvageable. The defects are concentrated. The bad news is that they are concentrated in exactly the places a serious referee will attack first.

Part I. Diagnostic — the ills
1. Logical / Mathematical
Finding 1. Theorem A is largely tautological in the current source

Location:

chapters/theory/chiral_koszul_pairs.tex, Definition def:chiral-koszul-pair, lines 65–97.

chapters/theory/higher_genus.tex, Theorem thm:bar-cobar-isomorphism-main, lines 1535–1595.

Project self-assessment: CLAUDE.md, lines 119–124.

Severity: CRITICAL

Diagnosis:
The current definition of a chiral Koszul pair already requires the very quasi-isomorphisms that Theorem A later “proves.” In Version I of the definition, a chiral Koszul pair is defined by the conditions

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

together with

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

Then Theorem A assumes “let
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

) be a chiral Koszul pair” and states exactly those same bar/cobar quasi-isomorphisms.

This is not a minor circularity in an example. It is a definition-theorem collapse. As written, Theorem A is not an independent theorem with mathematical content commensurate to its billing as a main theorem. It is, at best, an unpacking of the definition.

This is especially striking because CLAUDE.md correctly identifies and claims to resolve an older circularity about proving Koszulness for standard interacting families. That old issue may indeed be largely repaired. But a new, more serious circularity has been introduced at the level of the definitions themselves.

Resolution:
There are only two honest options.

Make Theorem A a theorem again.
Replace Definition def:chiral-koszul-pair by an independent recognition criterion. For example, define a chiral Koszul pair by:

genus-0 bar complex well-defined;

existence of a candidate dual quadratic/curved coalgebra;

acyclicity of the twisted Koszul complexes;

PBW-flatness / diagonal Ext vanishing for the associated graded.
Then prove the bar/cobar quasi-isomorphisms from those hypotheses.

Admit that Theorem A is definitional.
Keep the current definition, but then relabel Theorem A as something like:

Proposition. Consequences of the definition of chiral Koszul pair.
and remove the ProvedHere / “main theorem” rhetoric.

At present, neither path has been taken, and that is fatal at referee level.

Finding 2. Theorem B is axiomatized by Definition 8.17.7, and the example-verification propositions are circular

Location:

chapters/theory/higher_genus.tex, Definition def:modular-koszul-chiral, lines 7924–7987.

chapters/theory/higher_genus.tex, Theorem thm:higher-genus-inversion, lines 7706–7733.

chapters/theory/higher_genus.tex, Proposition prop:standard-examples-modular-koszul, lines 8005–8030.

chapters/theory/higher_genus.tex, Proposition prop:conditional-modular-koszul, lines 8032–8068.

Current narrative claim that “the four main theorems are proved” and all Part II examples instantiate the structure.

Severity: CRITICAL

Diagnosis:
Definition def:modular-koszul-chiral contains as axioms:

MK3: bar–cobar inversion;

MK5: complementarity decomposition.

Then Theorem B assumes “let
𝐴
A be a modular Koszul chiral algebra” and proves exactly the inversion statement that is already MK3. The example-verification proposition for standard examples then cites Theorem B to verify MK3. Likewise it cites Theorem C to verify MK5.

So the logic is:

define an object by requiring inversion/complementarity,

state inversion/complementarity as theorems about that object,

use those theorems to verify the definition for examples.

That is textbook circularity.

Resolution:
The definition must be split.

Define instead a weaker object, e.g. modular pre-Koszul chiral algebra, whose axioms are genuinely antecedent:

genus-0 Koszulity / PBW control;

Verdier/factorization setup on
Ran
⁡
(
𝑋
)
Ran(X);

higher-genus bar tower with controlled central curvature;

whatever filtered/homological hypotheses are actually checked in examples.

Then:

Theorem B should prove inversion on the Koszul locus from those hypotheses.

Theorem C should prove complementarity from those hypotheses plus the fiber-cohomology theorem.

The example propositions should verify only the hypotheses, not the conclusions.

Until that is done, the current Theorem B is not referee-grade mathematics.

Finding 3. Even ignoring the circularity, the written proof of Theorem A contains a real proof error

Location:

chapters/theory/higher_genus.tex, proof of thm:bar-cobar-isomorphism-main, lines 1627–1636.

chapters/theory/bar_cobar_construction.tex, Theorem thm:bar-nilpotency-complete, lines 562–597.

Severity: HIGH

Diagnosis:
Theorem A’s proof says that three results imply the bar complex identifies with the Koszul dual coalgebra, and the third cited result is Theorem thm:bar-nilpotency-complete. But that theorem proves only

𝑑
2
=
0
d
2
=0

for the bar differential. It does not prove that the augmented bar complex has cohomology concentrated in degree
0
0, and it certainly does not prove the Koszul property. Yet Theorem A’s proof explicitly says that it does.

This is not a wording problem. It is a false citation inside a main proof.

Resolution:
Insert a genuine theorem, in chiral_koszul_pairs.tex or the appropriate foundation chapter, of the form:

Theorem (Bar concentration for chiral Koszul pairs).
If
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

) satisfies [independent Koszul hypotheses], then the augmented bar complex is acyclic off degree
0
0, and
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
H
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

Then cite that theorem in Theorem A. If such a theorem already exists elsewhere in the source, route the proof explicitly to it and delete the false sentence.

Finding 4. Theorem C still depends on an underproved lemma; Step 4 does not prove total fiber cohomology concentration

Location:

chapters/theory/higher_genus.tex, Lemma lem:fiber-cohomology-center, lines 4982–5067.

chapters/theory/higher_genus.tex, Theorem thm:quantum-complementarity-main / Theorem 8.13.5, especially the use of center-valued fiber cohomology.

Severity: HIGH

Diagnosis:
The complementarity theorem is much improved compared with older versions. The eigenspace/Lagrangian mechanism is now the right one. But the proof still depends on the lemma identifying the fiber cohomology sheaf with the center local system and claiming higher fiber-cohomology vanishing.

The problem is Step 4 of the lemma. It invokes diagonal Ext concentration and then concludes only that higher cohomology vanishes when restricted to the degree-0 bar component. The proof then leaps from that restricted statement to the claim that the entire fiber cohomology sheaf is concentrated in degree
0
0.

That inference is not justified by the written argument.

This matters because Theorem C needs the full ambient object

𝐻
𝑔
(
𝐴
)
=
𝐻
∗
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
H
g
	​

(A)=H
∗
(
M
g
	​

,Z(A))

and its Verdier pairing/Lagrangian splitting, not just the degree-0 bar component.

Resolution:
Replace Step 4 by one of the following:

A true total vanishing theorem.
Prove directly that the full fiber complex is quasi-isomorphic to
𝑍
(
𝐴
)
Z(A) concentrated in degree
0
0. The natural route is a filtration by bar degree plus a comparison with the Koszul complex or a relative
𝑅
 ⁣
Hom
⁡
RHom computation.

A weaker theorem C.
If only the degree-0 component is currently controlled, then theorem C must be weakened accordingly — for example, to a statement about the scalar or center piece only.

As written, Theorem C is not yet fully secure.

Finding 5. The manuscript contains mutually incompatible Hochschild-duality theorems

Location:

chapters/theory/higher_genus.tex, Corollary cor:hochschild-duality, lines 1717–1743.

chapters/theory/deformation_theory.tex, Theorem thm:main-koszul-hoch, lines 452–505.

Current PDF Chapter 10 statement and proof outline

2212.11252v1

2212.11252v1

.

Severity: HIGH

Diagnosis:
One place states

𝐶
𝐻
𝑛
(
𝐴
1
)
≃
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
.
CH
n
(A
1
	​

)≃CH
n
(A
2
	​

)
∨
⊗ω
X
	​

[2].

Another states

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

These are not equivalent formulations of the same theorem. One preserves cohomological degree and adds a shifted object; the other reflects degree about
1
1. They encode different bookkeeping.

Moreover, the proof in the corollary is not convincing: it attributes the
[
2
]
[2]-shift to “each copy of
𝜔
𝑋
ω
X
	​

” and compresses the bar/configuration-space Verdier bookkeeping into a sentence that does not match the later theorem’s arithmetic.

A single book cannot publish both as definitive statements.

Resolution:
Choose one definitive theorem and prove it once.

The cleanest form is an object-level duality in the derived category, e.g.

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
1
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
i
r
a
l
(
𝐴
2
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

(A
1
	​

)≃RHom(RHH
chiral
	​

(A
2
	​

),ω
X
	​

[2]),

or a fully bigraded theorem with explicit conversion to total degree. Then deduce whichever cohomology-group formula is actually intended as a corollary.

At present this part of the book is mathematically inconsistent.

Finding 6. Theorem D overstates what is proved, and the example/status layer still leaks conjectural content into “established” statements

Location:

chapters/theory/higher_genus.tex, Definition def:modular-characteristic-package, lines 8089–8116.

chapters/theory/higher_genus.tex, Theorem thm:modular-characteristic, lines 8127–8177.

Introduction’s current framing of the four theorems and the package.

Conditional interacting-family statement and Conjecture 8.17.11.

Severity: MEDIUM/HIGH

Diagnosis:
The source is admirably explicit that the modular characteristic package has four components, and that the fourth — the full universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

 — is conjectural beyond its scalar shadow. Yet Theorem D says the modular characteristic package is determined, “as a scalar system,” by
𝜅
(
𝐴
)
κ(A), then immediately includes the spectral discriminant
Δ
𝐴
Δ
A
	​

 as part of that same theorematic package.

So the theorem is mixing:

a proved scalar package,

a separately proved but non-scalar invariant,

and a conjectural non-scalar universal class.

The introduction then amplifies this by speaking of the four main theorems as aspects of one object, which is conceptually fine, but too close to theorematic language when the non-scalar completion is openly conjectural.

Resolution:
Restate Theorem D as exactly what is proved:

Theorem D (Scalar modular characteristic theorem).
The scalar sector
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
)
(κ(A),{F
g
	​

(A)}) is determined by
𝜅
(
𝐴
)
κ(A), with universal genus formula, additivity, and duality law.

Then state
Δ
𝐴
Δ
A
	​

 as a separate theorem/corollary, and
Θ
𝐴
Θ
A
	​

 as a programme-level conjectural completion.

This is not merely rhetorical. Right now the book is over-claiming its fourth main theorem.

2. Structural / Architectural
Finding 7. The dependency graph still contains avoidable cycles and is not linearly trustworthy

Location:
Global, but concretely the cycle runs through:

Definition def:chiral-koszul-pair,

Theorem thm:bar-cobar-isomorphism-main,

Definition def:modular-koszul-chiral,

Theorem thm:higher-genus-inversion,

Theorem thm:quantum-complementarity-main,

Propositions prop:standard-examples-modular-koszul and prop:conditional-modular-koszul.

Severity: HIGH

Diagnosis:
A 1400-page monograph is only as good as its proof graph. The current graph still has cycles:

definitions that already contain theorem content,

theorems that assume those definitions,

example propositions that use the theorems to verify the definitions.

This is a structural defect, not just a local mathematical one. It means the manuscript does not yet have a genuinely linear dependency order.

Resolution:
Rebuild the proof architecture around four layers:

Independent foundations:
configuration spaces, bar/cobar functors, Verdier duality, curved/coderived language.

Genus-0 recognition theorems:
independent criteria for chiral Koszulity.

Higher-genus theorems:
inversion on the Koszul locus, complementarity, scalar modular characteristics.

Examples and programmes.

No theorem in layers 2–3 should assume a definition that already contains its own conclusion.

Finding 8. The frame chapter and the theorem-body chapters duplicate too much mathematics, while appendix-grade material remains in the main line

Location:

The separate Heisenberg frame in the current contents.

Later “Heisenberg Koszul duality from first principles” in the theory part.

Large theorem-body sections such as factorization-axiom verification, master tables, local coordinate atlases, and multiple Arnold proofs in the configuration-space chapters.

Severity: MEDIUM

Diagnosis:
The Heisenberg frame chapter is conceptually good — it does function as an “atom.” But at current length it is too large and too repetitive. It previews the entire thesis, computes the model, and then much of that machinery is reintroduced in the theory chapters. Meanwhile, technical verification material that belongs in appendices remains embedded in the proof line.

This is exactly the wrong trade in a large monograph: too much duplication at the front, too much technical mass in the core.

Resolution:
Two concrete cuts:

Compress the Heisenberg frame to a 15–20 page prologue that does only:

𝑑
2
=
0
d
2
=0,

bar/cobar in the simplest case,

first genus-1 curvature,

one-page preview of A–D.

Move the following to appendices or a companion technical volume:

factorization-axiom “master verification tables,”

long local-coordinate atlases for FM compactifications,

at least two of the three Arnold proofs,

bulked-out complexity-analysis sections.

This would materially improve the book’s readability and proof transparency.

3. Expository / Mathematical Writing
Finding 9. The notation for differentials, curvature, and theorem-status remains too unstable for a work of this scale

Location:
Global, especially Chapters 5–8, 10, 22, and 30.

Severity: MEDIUM

Diagnosis:
This is not a formatting complaint. It is a mathematical-writing problem.

The manuscript now has multiple genuinely different objects:

𝑑
b
a
r
(
0
)
,
𝑑
f
i
b
(
𝑔
)
,
𝐷
t
o
t
(
𝑔
)
,
𝑚
0
(
𝑔
)
,
Θ
𝐴
.
d
bar
(0)
	​

,d
fib
(g)
	​

,D
tot
(g)
	​

,m
0
(g)
	​

,Θ
A
	​

.

Some sections distinguish them; some use
𝑑
𝑔
d
g
	​

 generically; some talk about “the differential” with the distinction recoverable only from context. In a short paper, this would be survivable. In a 1400-page work whose central technical novelty is exactly the passage from strict to curved higher-genus behavior, it is not.

Similarly, the theorem/conjecture boundary is clearer in late chapters than in early ones. Chapter 34 appears to know the correct status distinctions; earlier chapters do not consistently enforce them.

Resolution:
Add, near the beginning, a permanent differential dictionary and enforce it globally:

𝑑
b
a
r
(
0
)
d
bar
(0)
	​

: genus-zero bar differential;

𝑑
f
i
b
(
𝑔
)
d
fib
(g)
	​

: genus-
𝑔
g fiberwise curved differential;

𝐷
t
o
t
(
𝑔
)
D
tot
(g)
	​

: total corrected strict differential;

𝑚
0
(
𝑔
)
m
0
(g)
	​

: curvature term;

Θ
𝐴
Θ
A
	​

: conjectural non-scalar universal MC class.

Then perform a source-wide audit so no theorem statement uses ambiguous
𝑑
𝑔
d
g
	​

 unless it is locally and uniquely defined.

Also propagate the theorem/conjecture/status vocabulary of Chapter 34 backward through the book.

4. Scope and Ambition Calibration
Finding 10. The conjecture / programme apparatus is mathematically fertile but currently weakens the book rather than strengthening it

Location:
Whole manuscript, especially later connections/programme chapters and the current open-problem apparatus.

Severity: MEDIUM/HIGH

Diagnosis:
The problem is not that there are many conjectures. The problem is that they are not stratified by dependency.

At present the book places side by side:

foundational missing pieces (non-scalar
Θ
𝐴
Θ
A
	​

, full coderived factorization formalism),

major but plausibly reachable extensions (full derived Drinfeld–Kohno, one nontrivial higher-genus PBW degeneration),

and long-range physics horizons (BV/bar identity, path-integral interpretation, higher-dimensional
𝐸
𝑛
E
n
	​

 extension, holographic interpretations).

These are not peers. Flattening them into one conjecture ecology blurs the true mathematical core.

Resolution:
Refactor the conjectures into three bands:

Foundational conjectures
whose proof would directly change the theorematic core.

Consequence conjectures
that become accessible once the foundational ones are proved.

Physical / horizon conjectures
which are valuable but should not compete rhetorically with the core monograph.

The leaner, stronger version of this book is already visible: a monograph on geometric bar–cobar duality, higher-genus corrected Koszul duality, complementarity, and a sharply curated example layer. The rest is a research programme and should be labeled as such.

Part II. Constructive — the strike list

Below are the highest-leverage mathematical actions I would recommend now. These are not bug-fixes in the narrow sense; they are the moves that most radically improve the book’s mathematical standing.

Strike 1. Refactor the two key definitions so that Theorems A and B become genuine theorems

The action:
Replace Definition def:chiral-koszul-pair and Definition def:modular-koszul-chiral by antecedent hypotheses that do not already contain bar–cobar inversion or complementarity.

Why it’s high-leverage:
This single change repairs the most serious referee objection in the book: “two main theorems are definitional rather than proved.” It also restores meaning to the ProvedHere tag system.

Feasibility:
1 week. The source already contains most of the ingredients; the problem is how they are organized.

Where it lives:
chapters/theory/chiral_koszul_pairs.tex, chapters/theory/higher_genus.tex, and the introduction.

Mathematical argument sketch:
Define a weaker notion, e.g. a recognition datum:

augmented chiral algebra
𝐴
A,

candidate dual coalgebra
𝐶
C,

twisted Koszul complex
𝐾
𝜏
(
𝐴
,
𝐶
)
K
τ
	​

(A,C),

filtration/PBW hypothesis,

diagonal Ext concentration for the associated graded.

Then prove:

𝐾
𝜏
(
𝐴
,
𝐶
)
 acyclic
  
⟹
  
𝐵
ˉ
c
h
(
𝐴
)
≃
𝐶
,
Ω
c
h
(
𝐶
)
≃
𝐴
.
K
τ
	​

(A,C) acyclic⟹
B
ˉ
ch
(A)≃C,Ω
ch
(C)≃A.

For modular objects, define the higher-genus tower plus central curvature and prove inversion/complementarity rather than requiring them.

Strike 2. Prove a genuine “bar concentration” theorem and use it to repair Theorem A

The action:
Add a theorem showing that, under the actual Koszul hypotheses, the augmented chiral bar complex is acyclic off degree
0
0, with degree-
0
0 cohomology equal to the dual coalgebra.

Why it’s high-leverage:
This kills the false citation in Theorem A’s proof and gives the book a clean genus-0 homological backbone.

Feasibility:
3–7 days if the needed PBW/associated-graded machinery is already present, which it appears to be.

Where it lives:
chapters/theory/chiral_koszul_pairs.tex, immediately before or after the main genus-0 duality theorem.

Mathematical argument sketch:
Use the PBW filtration or weight filtration on the bar complex, identify the associated graded with the classical quadratic/operadic Koszul complex (Loday–Vallette / Ginzburg–Kapranov side), then appeal to classical Koszulity of the associated graded. A standard spectral-sequence comparison then gives concentration of the original chiral bar complex.

Strike 3. Repair Theorem C by proving a total fiber-cohomology theorem

The action:
Prove the missing lemma:

𝐻
f
i
b
e
r
𝑞
(
𝐵
ˉ
Σ
𝑔
(
∙
)
(
𝐴
)
)
=
0
(
𝑞
>
0
)
,
𝐻
f
i
b
e
r
0
≅
𝑍
(
𝐴
)
⊗
𝐶
‾
.
H
fiber
q
	​

(
B
ˉ
Σ
g
	​

(∙)
	​

(A))=0(q>0),H
fiber
0
	​

≅Z(A)⊗
C
	​

.

Why it’s high-leverage:
This is the remaining genuinely dangerous proof gap inside the complementarity theorem. Fixing it stabilizes one of the book’s most distinctive results.

Feasibility:
1 week.

Where it lives:
chapters/theory/higher_genus.tex, in the proof architecture of Theorem 8.13.5.

Mathematical argument sketch:
Do not argue only on the degree-0 bar component. Instead:

build a filtration on the full fiber complex by bar degree;

identify the associated graded fiber complex with a Koszul-type complex computing
Ext
⁡
𝐴
(
𝑘
,
𝑘
)
Ext
A
	​

(k,k);

use diagonal concentration to show only the center survives in total degree
0
0;

pass to the Leray/spectral sequence for the family over
𝑀
𝑔
M
g
	​

.
If this full theorem resists proof, theorem C must be weakened correspondingly.

Strike 4. Consolidate Hochschild duality into one definitive theorem

The action:
Delete the current competing Hochschild-duality formulations and replace them by one object-level theorem, plus clearly derived cohomological corollaries.

Why it’s high-leverage:
It removes a visible contradiction that any expert reader will spot. It also clarifies the deformation-theory chapters and anything using cyclic/Hochschild comparisons.

Feasibility:
1–3 days.

Where it lives:
chapters/theory/deformation_theory.tex, chapters/theory/higher_genus.tex, and any later Hochschild/cyclic chapters.

Mathematical argument sketch:
Prove something of the form

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

[2])

or a bigraded variant. Then derive whichever group-level formulas are intended by taking cohomology with explicit degree conventions. This avoids the current inconsistency between “same degree with
[
2
]
[2]” and “degree
2
−
𝑛
2−n with
𝜔
𝑋
ω
X
	​

.”

Strike 5. Prove one flagship higher-genus PBW degeneration theorem

The action:
Take one nontrivial interacting family — generic affine Kac–Moody is the best candidate — and prove the higher-genus PBW spectral sequence degenerates at
𝐸
2
E
2
	​

.

Why it’s high-leverage:
Right now the interacting families are only conditionally modular-Koszul. Proving the degeneration for one flagship family would dramatically strengthen the book’s mathematical significance and validate the whole programme on non-free examples.

Feasibility:
1 month for a strong result; 1 week if a restricted rank-one or generic
𝑠
𝑙
^
2
sl
2
	​

 theorem is targeted first.

Where it lives:
chapters/theory/higher_genus.tex and the relevant Kac–Moody example chapter.

Mathematical argument sketch:
Use conformal-weight filtration. The central curvature term is filtration-central and does not change the associated graded. Identify the
𝐸
1
E
1
	​

-page with the genus-0 BGG/PBW complex. Then prove absence of higher differentials by a character comparison, irreducibility of generic Vermas, or a Weyl–Kac / BGG exactness argument. Even a proof for generic
𝑠
𝑙
^
2
sl
2
	​

 would be a major gain.

Strike 6. Prove a chain-level bar = semi-infinite/BRST theorem for one family

The action:
Construct a chain map from the reduced bar complex of a flagship family (affine Kac–Moody is again the most natural) to its semi-infinite / BRST complex, and prove it is a filtered quasi-isomorphism.

Why it’s high-leverage:
This would turn a large body of the physics-oriented later chapters from suggestive analogy into rigorous mathematics. It also clarifies the anomaly, complementarity, and W-algebra discussions.

Feasibility:
1 month.

Where it lives:
The Kac–Moody/W-algebra chapters and the later mathematical-physics chapters.

Mathematical argument sketch:
Use the configuration-space realization of the bar differential to define the map on generators via residue kernels/OPE contractions. Filter both sides by conformal weight / ghost number. Show the associated graded comparison is the classical Chevalley–Eilenberg or semi-infinite complex, then upgrade by spectral-sequence comparison.

Strike 7. Replace scalar “Period” by a periodicity profile and salvage the parts that are truly proved

The action:
Rewrite the periodicity package in terms of

Π
(
𝐴
)
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
Π(A)=(N
mod
	​

,N
quant
	​

,N
geom
	​

)

rather than a single scalar
P
e
r
i
o
d
(
𝐴
)
Period(A).

Why it’s high-leverage:
It turns one of the book’s historically weakest flanks into an honest, mathematically coherent subsystem. It also prevents future conditional claims from polluting proved statements.

Feasibility:
1 week.

Where it lives:
The periodicity chapter(s) and any downstream “period exchange” results.

Mathematical argument sketch:
Prove only what is presently supported:

a modular residue-class / phase statement, not chain-level periodicity, unless stronger hypotheses are available;

the quantum/Coxeter periodicity statement independently;

the weak geometric truncation/nilpotence statement;

lcm/gcd statements only after proving synchronization/commutation of the relevant operators.
This would replace an unstable scalar invariant by a stable profile.

Strike 8. Turn
Θ
𝐴
Θ
A
	​

 from a slogan into a first nontrivial theorem

The action:
Do not wait for the full universal Maurer–Cartan class. Prove the existence and compatibility of its first nontrivial Taylor components in the cyclic deformation complex.

Why it’s high-leverage:
This is the single move that would most dramatically raise the conceptual level of the book. Right now
Θ
𝐴
Θ
A
	​

 is the work’s organizing vision, but still conjectural. Even a partial theorem would transform the book from “theory with a grand conjectural capstone” into “theory already exhibiting the capstone in first nontrivial order.”

Feasibility:
1 month.

Where it lives:
chapters/theory/higher_genus.tex and Chapter 34.

Mathematical argument sketch:
Construct

Θ
𝐴
(
1
)
,
Θ
𝐴
(
2
)
∈
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
)
Θ
A
(1)
	​

,Θ
A
(2)
	​

∈Def
cyc
	​

(A)
⊗
	​

RΓ(
M
g,∙
	​

)

from the chain-level genus-one and first clutching operations. Prove:

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

 at first order,

compatibility with clutching at quadratic order,

Verdier duality sends
Θ
𝐴
Θ
A
	​

 to
Θ
𝐴
!
Θ
A
!
	​

 up to the verified order.
This would justify a substantial portion of the modular-characteristic rhetoric.

Final assessment

The book contains serious mathematics and a real theorematic core. But as submitted, it still fails the standard the author is aiming at.

The decisive reasons are:

Theorem A is definitional in the current source.

Theorem B is axiomatized by the current definition of modular Koszul chiral algebra.

Theorem C still contains a serious unproved step.

Hochschild duality is stated inconsistently.

Those are enough, by themselves, to block acceptance.

What is encouraging is that the remaining disease is concentrated. This is no longer a monograph collapsing everywhere. It is a monograph whose hardest work is done, but whose proof architecture and theorem-status discipline are still not rigorous enough for publication at the level it seeks.

That makes the editorial strategy clear:

fix the circular definitions,

repair theorem C,

stabilize Hochschild duality,

stratify the conjectures,

and propagate the honest Chapter 34 status logic backward through the whole book.

If those steps are taken, the manuscript could become a genuinely important monograph.
