Postscript (March 7, 2026)

This dossier is now historically out of date in one decisive respect.
The former Conjecture 34.9.1 is no longer the live bottleneck: higher-genus
PBW concentration has been proved for generic affine Kac-Moody, generic
Virasoro, and principal finite-type `W`-algebras, including higher `W_N`.
The correct current dependency order is therefore:

1. resolved entry theorem: all-genera PBW concentration for the standard
   finite-type interacting families;
2. Conjecture 34.9.2: cyclic `L_infty` deformation algebra and universal
   `Theta_A`;
3. Conjecture 34.9.3: full factorization-categorical DK/KL extension;
4. Conjecture 34.9.4: completed bar theory for infinite-generator duals;
5. Conjecture 34.9.5: BV/BRST/bar identification.

For the `W`-algebra story this forces a clean split:

- principal finite-type `W_N`: theorem-level and part of Stratum I;
- `W_infinity` / Yangian towers: still blocked by completed bar theory;
- non-principal orbit duality: separate open representation-theoretic
  frontier, not part of the resolved finite-type PBW story.

What follows should be read as the historical proof dossier for the
pre-resolution state of MC1, plus still-relevant guidance for MC2-MC5.

Historical note (pre-resolution snapshot): the source memo treated
Conjecture 34.9.1 as the immediate bottleneck and organized roughly 99
conjectures into five master conjectures. That dependency language is
retained below for archival continuity only; use the postscript above for
current status.

I will take that latest logical order as canonical. The dossier below is therefore organized as a genuine proof programme, not as a bag of isolated suggestions.

Master-conjecture proof dossier
0. Dependency order

The current manuscript itself already points to the correct dependency graph.

Conjecture 34.9.1 (higher-genus PBW degeneration) is the immediate bottleneck for turning the standard interacting families from conditional to unconditional modular Koszul objects.

Conjecture 34.9.2 (cyclic
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

) is the foundational conjecture of the modular programme; it upgrades the scalar/spectral package to the full modular homotopy package.

Conjecture 34.9.3 (full factorization-categorical DK/KL extension) sits one layer above the already-proved chain/evaluation-locus DK statements and explicitly requires additional input: extension beyond evaluation modules, Yangian Koszulness, and factorization-level Kazhdan equivalence.

Conjecture 34.9.4 (completed bar theory for infinite-generator duals) is the infrastructure needed for the
𝑊
∞
W
∞
	​

/Yangian-tower regime and for any serious infinite-generator duality theorem.

Conjecture 34.9.5 (BV/BRST/bar identification) is explicitly downstream of 34.9.1–34.9.4 and should be treated that way; the latest manuscript says this in exactly those terms.

So the mathematically sensible order is:

PBW degeneration
  
→
  
unconditional modular Koszulity
,
PBW degeneration→unconditional modular Koszulity,
cyclic
𝐿
∞
+
Θ
𝐴
  
→
  
full modular package
,
cyclic L
∞
	​

+Θ
A
	​

→full modular package,
completed bar for infinite-generator duals
  
→
  
infinite-generator examples
,
completed bar for infinite-generator duals→infinite-generator examples,
full DK/KL
  
→
  
factorization-categorical quantum side
,
full DK/KL→factorization-categorical quantum side,
BV/BRST/bar
  
→
  
physics completion
.
BV/BRST/bar→physics completion.
1. Conjecture 34.9.1 — Higher-genus PBW degeneration
Conjecture

34.9.1:

For generic affine Kac–Moody
𝑔
^
𝑘
,
 generic Virasoro
V
i
r
𝑐
,
 and generic
𝑊
𝑁
,

𝐸
𝑟
P
B
W
(
𝑔
)
 degenerates at
𝐸
2
 for all
𝑔
≥
1.
Conjecture 34.9.1: For generic affine Kac–Moody
g
	​

k
	​

, generic Virasoro Vir
c
	​

, and generic W
N
	​

, E
r
PBW
	​

(g) degenerates at E
2
	​

 for all g≥1.

The latest manuscript says this is the single missing hypothesis for unconditional modular Koszulity of the standard interacting families.

Current proved foothold

For the interacting families, the manuscript already proves:

genus-
0
0
𝐸
2
E
2
	​

-collapse,

identification of the associated graded genus-
𝑔
g
𝐸
1
E
1
	​

-page with the genus-
0
0
𝐸
1
E
1
	​

-page,

and therefore conditional modular pre-Koszulity if actual degeneration at generic parameters is supplied.

So the conjecture is not “build a theory from nothing.” It is: upgrade associated-graded control to actual degeneration.

Refined target theorem

Do not try to prove the full three-family statement at once. Replace it by three theorems in order:

PBW-1

For generic affine Kac–Moody
𝑔
^
𝑘
g
	​

k
	​

, the genus-
𝑔
g PBW spectral sequence degenerates at
𝐸
2
E
2
	​

 for all
𝑔
≥
1
g≥1.

PBW-2

For generic Virasoro
V
i
r
𝑐
Vir
c
	​

, the same holds.

PBW-3

For generic
𝑊
𝑁
W
N
	​

-algebras, the same holds.

The Kac–Moody case should be first. It is the one with the strongest existing algebraic control, and once it is done the other two can be attacked by reduction or free-field/screening technology.

Missing lemmas

The missing lemmas are very concrete.

Lemma PBW.1 — Curvature-centrality does not alter the filtered differential

The manuscript already observes that the fiberwise curvature

(
𝑑
f
i
b
(
𝑔
)
)
2
=
𝜅
 
𝜔
𝑔
(d
fib
(g)
	​

)
2
=κω
g
	​


is central and therefore does not alter the PBW-filtered structure of the collision differential at associated graded level.
This needs to be upgraded from a proof remark into a reusable lemma:

If the curvature term is central and filtration-nonnegative, then the PBW associated graded of the genus-
𝑔
g bar differential agrees with the genus-
0
0 associated graded differential.

Lemma PBW.2 — Flatness of the filtered family in the generic parameter

For each family, build the genus-
𝑔
g filtered bar complex as a family over the parameter space (
𝑘
k,
𝑐
c, level, etc.), and prove that the dimensions of the
𝐸
𝑟
E
r
	​

-pages are upper semicontinuous.

Without this, “generic degeneration” is not a meaningful statement.

Lemma PBW.3 — No room for higher differentials

You need a mechanism that kills
𝑑
𝑟
d
r
	​

 for
𝑟
≥
2
r≥2. There are three likely routes:

degree reasons,

character comparison,

semisimplicity/vanishing of certain extension groups in the generic regime.

For affine Kac–Moody, the third route is the strongest.

Proof roadmap
Route A: generic affine Kac–Moody

Put the PBW filtration on the genus-
𝑔
g bar complex by conformal weight, exactly as in the manuscript’s conditional proposition.

Identify the associated graded
𝐸
1
E
1
	​

-page with the genus-
0
0
𝐸
1
E
1
	​

-page as a bigraded complex.

Use the generic BGG/Verma-module control to show that the total cohomology dimensions of the actual genus-
𝑔
g complex match the dimensions predicted by the associated graded.

Conclude that any nonzero higher differential would force a dimension drop, contradiction.

The key idea is: replace “spectral-sequence degeneration is not automatic” by a comparison theorem using generic character exactness.

Route B: generic Virasoro

Use the Feigin–Fuchs free-field realization and screening filtration. The target is to identify the genus-
𝑔
g PBW page with a filtered screening complex whose generic cohomology is already known or can be reduced to the generic Heisenberg/free-field case plus one nontrivial screening operator.

Route C: generic
𝑊
𝑁
W
N
	​


Exploit Miura transform + DS reduction. You do not need a direct genus-
𝑔
g
𝑊
𝑁
W
N
	​

 argument if you can prove:

PBW degeneration for the corresponding affine object,

exact compatibility of genus-
𝑔
g bar complexes with DS reduction,

and filtration-exactness of the reduction functor at generic level.

That converts
𝑊
𝑁
W
N
	​

 from an independent conjecture into a consequence of Kac–Moody plus DS-bar compatibility.

Likely techniques

PBW and conformal-weight filtrations;

Eilenberg–Moore / spectral-sequence comparison theorems;

generic irreducibility of Vermas and absence of singular vectors;

free-field and screening realization for Virasoro/
𝑊
𝑁
W
N
	​

;

Drinfeld–Sokolov filtration compatibility.

Earliest decisive checkpoint

The first decisive result is not the full conjecture. It is:

Checkpoint PBW-KM: prove genus-
𝑔
g
𝐸
2
E
2
	​

-degeneration for generic
𝑠
𝑙
^
2
sl
2
	​

.

If that theorem fails, the whole interacting-family programme needs recalibration. If it succeeds, the rest becomes a scaling problem, not a conceptual one.

2. Conjecture 34.9.2 — Cyclic
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

Conjecture

34.9.2:

Θ
𝐴
∈
𝑀
𝐶
 ⁣
(
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
𝑔
,
∙
,
𝑄
)
)
Conjecture 34.9.2: Θ
A
	​

∈MC(Def
cyc
	​

(A)
⊗
	​

RΓ(M
g,∙
	​

,Q))

with trace
𝜅
(
𝐴
)
𝜆
𝑔
κ(A)λ
g
	​

, clutching compatibility, and Verdier-duality compatibility.

The latest manuscript calls this the genuine foundational conjecture of the modular programme, and the current scalar package chapter says that constructing
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

(A) and solving the MC equation is the principal open problem.

Current proved foothold

The manuscript already has:

the scalar invariant
𝜅
(
𝐴
)
κ(A),

the genus tower
{
𝐹
𝑔
(
𝐴
)
}
{F
g
	​

(A)},

the spectral discriminant
Δ
𝐴
Δ
A
	​

,

and an ambient modular deformation family
𝐻
𝐴
H
A
	​

.

So
Θ
𝐴
Θ
A
	​

 should be viewed as the non-scalar lift of data already visible in shadow form.

Refined target theorem

Do not attempt the full universal MC theorem first. Break it into three stages.

Theta-1 (first Taylor component)

Construct

Θ
𝐴
(
1
)
∈
D
e
f
c
y
c
1
(
𝐴
)
⊗
^
𝐻
∗
(
𝑀
𝑔
,
∙
)
Θ
A
(1)
	​

∈Def
cyc
1
	​

(A)
⊗
	​

H
∗
(M
g,∙
	​

)

whose trace is
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

Theta-2 (quadratic compatibility)

Construct

Θ
𝐴
(
≤
2
)
Θ
A
(≤2)
	​


satisfying the Maurer–Cartan equation modulo cubic terms and prove clutching compatibility to second order.

Theta-3 (full completed MC theorem)

Only after Theta-1 and Theta-2 are in place should one solve the full MC equation.

This staged approach is the only realistic route. Trying to prove the full statement in one shot is too coarse.

Missing lemmas
Lemma Theta.1 — A canonical cyclic deformation complex

You need a precise model for
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

(A). The right candidate is a completed cyclic Hochschild cochain complex of the bar/factorization object, equipped with:

the Gerstenhaber or brace bracket,

a cyclic pairing,

and the topology induced by genus/bar/weight completion.

Without this,
Θ
𝐴
Θ
A
	​

 has no home.

Lemma Theta.2 — Boundary of boundary =
𝐿
∞
L
∞
	​

 relations

The
𝐿
∞
L
∞
	​

 brackets must come from codimension-1 boundary strata of modular configuration spaces or stable-graph compactifications. Then “boundary of boundary is zero” produces the higher Jacobi relations.

This is the modular extension of the same mechanism by which the Arnold relation gives
𝑑
2
=
0
d
2
=0 at genus
0
0.

Lemma Theta.3 — Trace map compatibility

You need a chain map

tr
⁡
:
D
e
f
c
y
c
(
𝐴
)
→
𝐶
tr:Def
cyc
	​

(A)→C

such that
tr
⁡
(
Θ
𝐴
)
tr(Θ
A
	​

) recovers the scalar package. This is what turns
𝜅
(
𝐴
)
κ(A) into the first characteristic number of
Θ
𝐴
Θ
A
	​

. The manuscript already says this is the right interpretation.

Lemma Theta.4 — Verdier duality on the cyclic deformation complex

The manuscript wants
Θ
𝐴
Θ
A
	​

 and
Θ
𝐴
!
Θ
A
!
	​

 related by Verdier duality. That must be implemented at the chain level on
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

(A), not only on the ambient cohomology package.

Proof roadmap
Phase I: define
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

(A)

Take the completed cyclic Hochschild cochain complex of the bar/factorization model:

D
e
f
c
y
c
(
𝐴
)
:
=
𝐶
𝐶
^
c
y
c
∙
(
𝐴
)
[
1
]
.
Def
cyc
	​

(A):=
CC
cyc
∙
	​

(A)[1].

Show that the brace/Gerstenhaber structure and cyclic pairing survive completion.

Phase II: produce the first operations from stable-graph boundary strata

Use the modular operad of stable curves/configurations:

vertices = local multilinear operations,

edges = propagator contractions,

boundary gluing = composition.

This gives the first few
𝐿
∞
L
∞
	​

 brackets explicitly.

Phase III: define
Θ
𝐴
Θ
A
	​

 perturbatively

Construct
Θ
𝐴
Θ
A
	​

 as a sum over genus and stable-graph types, at first to low order:

Θ
𝐴
=
Θ
𝐴
(
1
)
+
Θ
𝐴
(
2
)
+
⋯
Θ
A
	​

=Θ
A
(1)
	​

+Θ
A
(2)
	​

+⋯

where each coefficient is an integral class/operator extracted from the bar geometry.

Phase IV: verify the three required shadows

trace gives
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

clutching gives sewing,

Verdier duality gives the dual class.

Phase V: solve the completed MC equation

Use filtered pronilpotent deformation theory:

the filtration by genus/weight/number of edges should make the dg Lie/
𝐿
∞
L
∞
	​

 algebra pronilpotent;

solve recursively by obstruction theory.

Likely techniques

cyclic
𝐴
∞
/
𝐿
∞
A
∞
	​

/L
∞
	​

 deformation theory;

Getzler–Kapranov modular operads / modular Feynman transform;

homological perturbation and transferred
𝐿
∞
L
∞
	​

 structures;

Costello-style effective action / graph-sum expansions;

Verdier duality as an involution on graph coefficients.

Earliest decisive checkpoint

The first decisive theorem should be:

Checkpoint Theta-1: construct
Θ
𝐴
(
1
)
Θ
A
(1)
	​

 for free fields and generic affine Kac–Moody, and prove that its trace is exactly
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

That would immediately convert a large amount of current rhetoric into actual mathematics.

3. Conjecture 34.9.3 — Full factorization-categorical DK/KL extension
Conjecture

34.9.3:

the chain-level / evaluation-locus derived DK and KL statements extend to equivalences of full factorization categories.
Conjecture 34.9.3: the chain-level / evaluation-locus derived DK and KL statements extend to equivalences of full factorization categories.

The latest manuscript is very precise about what is already proved and what remains:

chain-level derived DK is proved,

factorization DK on the evaluation locus is proved,

the remaining gap is the extension from evaluation modules to the full Yangian category
𝑂
O, which requires Yangian Koszulness and factorization-level Kazhdan equivalence.

Current proved foothold

The latest manuscript already has:

braided monoidal structure on bar complexes of
𝐸
1
E
1
	​

-chiral algebras,

Verdier duality
⇒
𝑅
⇒R-matrix inversion,

chain-level DK square for evaluation modules,

factorization DK on the evaluation locus.

This is a strong foothold. The full conjecture is no longer a foggy dream; it has a sharply isolated missing step.

Refined target theorem

Again, split it.

DK-1

Factorization-level Kazhdan equivalence on the evaluation-generated subcategory.

DK-2

Extension of the evaluation-locus equivalence to the idempotent-complete triangulated/derived subcategory generated by evaluation objects.

DK-3

Full extension to category
𝑂
O and full
𝐸
1
E
1
	​

-factorization category.

Do not attempt DK-3 before DK-1 is proved.

Missing lemmas
Lemma DK.1 — Evaluation modules generate the relevant factorization subcategory

One needs a precise generation statement: every object in the target category is built from evaluation objects by extensions, filtered colimits, or a specified closure operation.

Without generation, “extend from evaluation modules” is empty.

Lemma DK.2 — Exactness and continuity of the bar-cobar functor on the completed
𝐸
1
E
1
	​

 side

The extension beyond the evaluation locus requires the functor to preserve the operations used to generate category
𝑂
O.

Lemma DK.3 — Factorization-level Kazhdan equivalence

This is already singled out by the manuscript as the “critical remaining step”. It should be isolated as the central intermediate theorem:

F
a
c
t
𝐸
1
o
r
d
(
𝑋
;
𝑌
(
𝑔
)
)
  
≃
  
F
a
c
t
𝐸
1
o
r
d
(
𝑋
;
𝑈
𝑞
(
𝑔
)
)
Fact
E
1
	​

ord
	​

(X;Y(g))≃Fact
E
1
	​

ord
	​

(X;U
q
	​

(g))

on the correct factorization/Kazhdan side.

Lemma DK.4 — Yangian Koszulness for general
𝑔
g

The manuscript itself says this is a remaining requirement for the full extension. This should probably be attacked first for
𝑠
𝑙
𝑁
sl
N
	​

, not all
𝑔
g.

Proof roadmap
Phase I: stabilize the evaluation-locus theorem categorically

Take Theorem 24.9.5 and recast it as an equivalence of compactly generated dg/
∞
∞-categories, not merely as a statement about objects and braiding on a handpicked subcategory.

Phase II: prove factorization-level Kazhdan on the same subcategory

Show that the Kazhdan functor intertwines:

ordered-collision factorization,

the
𝑅
R-matrix local system,

and Verdier duality/bar-cobar inversion.

This is the actual categorical bridge.

Phase III: prove generation of category
𝑂
O

Show that the full category
𝑂
O is generated by:

evaluation modules,

standard modules,

or another explicit family stable under the factorization tensor structure.

Phase IV: extend by exactness/continuity

Use compact generation and exactness of the functors to extend the equivalence from generators to the full category.

Likely techniques

compact generation in stable
∞
∞-categories;

monadic or Tannakian reconstruction of factorization categories;

factorization homology on ordered configuration spaces;

Kazhdan–Lusztig/Finkelberg equivalence at the correct categorical level;

spectral
𝑅
R-matrix control and braid-group local systems;

pro-nilpotent completion for the
𝐸
1
E
1
	​

-bar side.

Earliest decisive checkpoint

The crucial checkpoint is not the whole theorem. It is:

Checkpoint DK-1: prove the factorization-level Kazhdan equivalence on the evaluation-generated subcategory.

If that theorem is proved, the remaining step is categorical extension. If not, the conjecture remains blocked at its real bottleneck.

4. Conjecture 34.9.4 — Completed bar theory for infinite-generator duals
Conjecture

34.9.4:

the bar–cobar framework extends to chiral algebras whose Koszul duals have infinitely many generators (
𝑊
∞
,
 Yangian towers, etc.).
Conjecture 34.9.4: the bar–cobar framework extends to chiral algebras whose Koszul duals have infinitely many generators (W
∞
	​

, Yangian towers, etc.).

The latest manuscript explicitly says this requires “new analytic/topological completion techniques beyond the present finite-type setting” and also lists the full coderived factorization-algebra formalism and infinite-generator duals in Stratum II.

Current proved foothold

The manuscript already has:

finite-type filtered-complete bar complexes,

the coderived intuition,

and concrete finite-generator examples.

What is missing is a completed functional-analytic / pro-object theory strong enough to handle infinitely many generators.

Refined target theorem

Break the conjecture into infrastructure and application.

INF-1

Define the completed bar construction

𝐵
ˉ
^
𝑋
(
𝐴
)
=
𝑇
𝑐
^
(
𝑠
−
1
𝐴
ˉ
)
B
ˉ
X
	​

(A)=
T
c
(s
−1
A
ˉ
)

for a class of pronilpotent graded-complete chiral algebras.

INF-2

Prove the completed bar differential converges and the construction is functorial.

INF-3

Prove a completed/coderived bar–cobar adjunction.

INF-4

Apply it to one infinite-generator family, e.g. a controlled
𝑊
∞
W
∞
	​

-type truncation or Yangian tower.

Only after INF-1–INF-3 are secure should one speak about actual infinite-generator duality theorems.

Missing lemmas
Lemma INF.1 — Topological tensor-coalgebra convergence

You need a precise class of topological vector spaces (or Ind-Pro objects) in which

𝑇
𝑐
^
(
𝑠
−
1
𝐴
ˉ
)
=
∏
𝑛
≥
0
(
𝑠
−
1
𝐴
ˉ
)
⊗
^
𝑛
T
c
(s
−1
A
ˉ
)=
n≥0
∏
	​

(s
−1
A
ˉ
)
⊗
	​

n

makes sense and the deconcatenation coproduct is continuous.

Lemma INF.2 — Continuity of the bar differential

The OPE/residue/collision differential must be continuous for the chosen topology, and the infinite sum of higher terms must converge.

Lemma INF.3 — Completed twisting morphisms and coderived acyclicity

The analogue of the fundamental theorem of twisting morphisms must be re-proved in the completed setting.

Lemma INF.4 — Verdier duality is continuous on the completed coalgebraic side

Without this, the infinite-generator version of the duality theorem will have no chain-level meaning.

Proof roadmap
Phase I: choose the right ambient category

The cleanest starting point is not Banach or Fréchet spaces per se; it is a filtered-complete pronilpotent dg category, or an Ind-Pro category of finite-weight pieces. The category should satisfy:

completed tensor products exist,

filtered inverse limits are exact enough,

continuous duals behave predictably.

Phase II: rebuild bar/cobar in that ambient category

Define completed bar and completed cobar, prove functoriality, and formulate the completed twisting-morphism criterion.

Phase III: prove a completed comparison theorem

Approximate the infinite-generator object by finite-type truncations
𝐴
≤
𝑁
A
≤N
	​

. Prove:

𝐵
ˉ
^
(
𝐴
)
≃
l
i
m
←
⁡
𝑁
𝐵
ˉ
(
𝐴
≤
𝑁
)
,
B
ˉ
(A)≃
N
lim
	​

	​

B
ˉ
(A
≤N
	​

),

and that the inverse system is Mittag–Leffler or otherwise convergence-safe.

Phase IV: test on one infinite-generator example

Do not start with the full
𝑊
∞
W
∞
	​

 mythology. Start with a filtered tower whose associated graded is under control. If the infrastructure works there, then proceed.

Likely techniques

filtered-complete dg categories and derived completion;

Positselski-style coderived/CDG techniques;

pro-objects / Ind-Pro limits;

continuous Hochschild/cyclic theory;

nuclearity or finite-weight hypotheses to guarantee tensor convergence;

truncation/inverse-limit comparison.

Earliest decisive checkpoint

The first serious checkpoint is:

Checkpoint INF-1: define
𝐵
ˉ
^
𝑋
(
𝐴
)
B
ˉ
X
	​

(A) and prove convergence of
𝑑
b
a
r
d
bar
	​

 for one honest infinite-generator class.

Without that, every infinite-generator duality conjecture remains rhetoric.

5. Conjecture 34.9.5 — BV/BRST/bar identification
Conjecture

34.9.5:

For a holomorphic field theory on a Riemann surface, the BV/BRST complex coincides with the bar complex of the associated chiral algebra, at all genera.
Conjecture 34.9.5: For a holomorphic field theory on a Riemann surface, the BV/BRST complex coincides with the bar complex of the associated chiral algebra, at all genera.

The latest manuscript is very clear on the current footholds:

genus-0 BRST-bar quasi-isomorphism is proved for
𝑐
=
26
c=26 on
𝑃
1
P
1
;

stronger holomorphic/semi-infinite identifications are proved for Kac–Moody and
𝑊
W-algebras at genus
0
0;

the higher-genus extension explicitly requires path-integral measure and Costello renormalization input;

and the manuscript itself says this whole conjecture is downstream of the first four master conjectures.

Current proved foothold

There are already three nontrivial footholds:

genus-0 BRST-bar quasi-isomorphism at
𝑐
=
26
c=26 for the string-type coupled system;

holomorphic BRST = bar for Kac–Moody and
𝑊
W-algebras at genus 0 / semi-infinite level;

anomaly cancellation dictionary
𝜅
t
o
t
=
0
↔
𝑐
m
a
t
t
e
r
+
𝑐
g
h
o
s
t
=
0
κ
tot
	​

=0↔c
matter
	​

+c
ghost
	​

=0 at genus 0.

That is more substantial than the older versions had.

Refined target theorem

Again, split the target.

BV-1

Holomorphic all-genera BRST/bar identification for one family with no diffeomorphism ghosts.

BV-2

Genus-graded extension of the genus-0 string BRST-bar quasi-isomorphism for the coupled matter
⊗
𝑏
𝑐
⊗bc system.

BV-3

Topological BRST/bar identification including
D
i
f
f
(
𝑋
)
Diff(X) ghosts.

BV-4

QME/bar-cobar equivalence:

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
⟺
𝐷
𝑔
2
=
0
ℏΔS+
2
1
	​

{S,S}=0⟺D
g
2
	​

=0

at chain level.

The current manuscript already says the topological BRST conjecture is stronger than the holomorphic/semi-infinite one and that
D
i
f
f
(
𝑋
)
Diff(X) is the real new difficulty. So BV-1 must come first.

Missing lemmas
Lemma BV.1 — A genus-
𝑔
g chain map
Φ
𝑔
Φ
g
	​


You need an explicit chain map

Φ
𝑔
:
𝐶
B
R
S
T
(
𝑔
)
(
𝐴
)
→
𝐵
ˉ
𝑋
(
𝑔
)
(
𝐴
)
Φ
g
	​

:C
BRST
(g)
	​

(A)→
B
ˉ
X
(g)
	​

(A)

extending the genus-0 map
Φ
Φ. The manuscript already says this is what should exist, with the genus-
𝑔
g component involving Costello’s counterterm expansion.

Lemma BV.2 — Compatibility with renormalization/counterterms

The map
Φ
𝑔
Φ
g
	​

 must intertwine the renormalized BV differential with the total corrected bar differential
𝐷
𝑔
D
g
	​

, not merely with the naive fiberwise bar differential.

Lemma BV.3 — Ghost anomaly = curvature anomaly

At genus 0 this is proved:
𝜅
t
o
t
=
0
κ
tot
	​

=0 matches BRST anomaly cancellation. At higher genus, you need the analogue after renormalization and measure insertion.

Lemma BV.4 — Inclusion of diffeomorphism ghosts

The manuscript explicitly says that topological BRST requires infinite-dimensional
D
i
f
f
(
𝑋
)
Diff(X) ghosts and that neither the genus-0 PBW filtration argument nor the semi-infinite approach directly applies. This is the real obstruction to BV-3.

Proof roadmap
Phase I: holomorphic all-genera first

Do not start with full topological BRST. Start with the holomorphic/semi-infinite model.

Take a family where the holomorphic BRST complex is already understood at genus 0 — affine Kac–Moody is the best target — and define a genus-graded chain map
Φ
𝑔
Φ
g
	​

 using the same propagator data that define the bar differential on
Σ
𝑔
Σ
g
	​

.

Phase II: compare filtrations

Put conformal-weight/ghost-number filtrations on both sides. The genus-0 proof already uses a PBW filtration to reduce to the classical comparison. The all-genera version should use:

conformal weight,

genus filtration,

and counterterm order.

The goal is to reduce the comparison to the already-proved genus-0 or semi-infinite model plus controlled higher-genus corrections.

Phase III: add anomaly cancellation

Use the already-proved genus-0 anomaly dictionary as the base case and prove that the same scalar curvature class controls both sides in genus
𝑔
g. This is where the scalar package and conjecture 34.9.2 start to interact.

Phase IV: only then add
D
i
f
f
(
𝑋
)
Diff(X)

Once holomorphic BV/bar is working, extend the local symmetry algebra from gauge/vertex-algebra symmetry to the semidirect product with diffeomorphisms. This is where the topological BRST conjecture actually begins.

Likely techniques

Costello renormalization and effective-action counterterms;

semi-infinite cohomology;

homological perturbation / transferred differentials;

Eilenberg–Moore spectral-sequence comparisons (already used at genus 0);

BRST descent and anomaly-cancellation identities;

configuration-space boundary formulas realizing the BV bracket.

Earliest decisive checkpoint

The decisive checkpoint is:

Checkpoint BV-1: prove a genus-
1
1 holomorphic BRST/bar quasi-isomorphism for one nontrivial family (preferably affine Kac–Moody).

If that theorem is achieved, the conjecture changes nature: the all-genera theorem becomes an induction/renormalization problem rather than a conceptual leap.

VI. Recommended execution order

If the goal is to maximize theorematic return rather than scatter effort, the order should be:

PBW degeneration for one flagship interacting family.
This upgrades the core immediately.

First-order
Θ
𝐴
Θ
A
	​

: construct
Θ
𝐴
(
1
)
Θ
A
(1)
	​

 and its trace.
This upgrades the package conceptually.

Completed bar infrastructure for infinite-generator objects.
This is required before the big infinite-generator duals are anything more than slogans.

Factorization-level Kazhdan equivalence on the evaluation-generated subcategory.
This is the critical bottleneck in full DK/KL.

Genus-1 holomorphic BRST/bar comparison.
This is the right gateway theorem for the BV/BRST programme.

That order respects the manuscript’s own logical stratification and avoids spending months on downstream physics structure before the algebraic heart is fully stabilized.

VII. Final assessment

The latest manuscript now gives the right abstract control system for its open problems. That is a major advance. The five master conjectures are not peers; they form a dependency ladder, and the book finally says so. The proof dossier above is therefore not a speculative redesign; it is the natural rigorous completion of the structure the manuscript now explicitly advertises.

The single most important tactical point is this:

Conjecture 34.9.1 is the fastest route to hard new theorems; Conjecture 34.9.2 is the deepest route to conceptual completion; Conjecture 34.9.5 must remain downstream until the first four are materially advanced.
