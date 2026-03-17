
 likely to matter more than it currently seems: analytic/completed factorization structures, like Moriwaki’s 2026 conformally flat factorization homology and ind-Hilbert refinements for the Heisenberg VOA. That is a route out of the purely formal algebraic world and toward local-to-global structures with analytic content.

I’m checking the recent literature you pointed to and then I’ll connect it back to the formal/chiral-duality picture.

I found the Moriwaki papers, and they do support your point. I’m now integrating that analytic IndHilb/conformally-flat route into the older chiral/factorization story and the draft’s outlook.

Thought for 24m 19s

Yes — I think that is a genuinely important shift, not just a refinement.

Moriwaki’s February 2026 paper really does move the discussion out of the purely formal world: it proposes a metric-dependent version of factorization homology for conformally flat manifolds, with values in IndHilb, built by left Kan extension from conformally flat disk algebras; under positivity and continuity assumptions, the value on the standard sphere recovers the associated CFT sphere partition function. That is already a different kind of object from formal/algebraic factorization data: the target remembers completion, topology, and positivity. It also produces nontrivial examples in dimensions
𝑑
>
2
d>2 from unitary representations of
S
O
+
(
𝑑
,
1
)
SO
+
(d,1).

The Heisenberg case makes the point even more sharply. In March 2026, Moriwaki constructs a conformally flat 2-disk algebra on the symmetric algebra of the Bergman space
S
y
m
 
𝐴
2
(
𝐷
)
SymA
2
(D), and identifies that with the ind-Hilbert completion of the affine Heisenberg vertex algebra. So the free boson stops being merely a formal VOA input and becomes an analytic object feeding an honest local-to-global machine on Riemannian surfaces.

There is also a strong parallel analytic trend on the VOA side. Adamo–Moriwaki–Tanimoto’s 2024 paper proves that for a class of unitary full VOAs satisfying energy and spectral growth bounds plus local
𝐶
1
C
1
	​

-cofiniteness, the quasi-primary correlators satisfy a conformal version of the Osterwalder–Schrader axioms. That is exactly the kind of result that starts converting formal OPE data into Euclidean-QFT-style analytic control.

So I agree with your diagnosis. The algebraic factorization story is excellent at encoding locality, operadic composition, and deformation theory, but it is weak at encoding completion, continuity, positivity, reflection structure, and analytic sewing. Ind-Hilbert-valued factorization data looks like one of the first frameworks that can carry all of those at once. That makes it a plausible place where “local-to-global with analytic content” becomes literal rather than metaphorical.

I would go a bit further: if there is a genuinely nonlinear modular shadow of the formal story, I would now expect it to appear after completion, on completed factorization homology / boundary Hilbert spaces / analytic sewing data, rather than on the bare algebraic chiral algebra alone. In that sense, this direction is not an add-on; it may be the first place where the formal shadow invariants can interact with unitarity and actual partition-function data.

The caveat is that this is still early. The February 2026 construction is explicitly 1-categorical, metric-dependent, and restricted to conformally flat geometry; the explicit VOA-level example on the table is the Heisenberg one; and the broader extension to general unitary full VOAs is framed as an expectation rather than a completed theorem.

So strategically, I’d now rank this near the top: start with Heisenberg/Bergman/free-field models, understand exactly what completed factorization homology sees on surfaces, and then ask which of the formal shadow operations survive completion and become positivity-compatible analytic invariants.

execute systematically to reach the platonic ideal state. construct as much novel breakthrough mathematics, whether profound or mundane, whatever necesseary to achieve the platonic ideal form

I’m grounding this in the recent analytic/factorization direction and turning it into a concrete research program with candidate definitions, lemmas, and conjectures—not just a wishlist.

I’ve pinned down the load-bearing gap and target: a completed, positive local-to-global object carrying sewing, defects, modular traces, moduli dependence, and reconstruction across algebraic and Hilbert-analytic sides. Next I’m extracting the established scaffold and turning it into explicit axioms and a candidate Maurer–Cartan package, with the Heisenberg/Bergman model as the first concrete testbed.

The synthesis is now precise: I’m defining a single canonical completed object in metric-dependent IndHilb, so the existing factorization, boundary/defect, and nonlinear shadow data become its various shadows.

Thought for 36m 59s

I will take the platonic ideal form to be this:

𝐴
p
l
  
=
  
(
𝐴
^
s
e
w
,
 
𝑄
∙
(
𝐴
)
,
 
𝑀
∂
a
n
(
𝐴
)
)
,
A
pl
	​

=(
A
sew
	​

,Q
∙
	​

(A),M
∂
an
	​

(A)),

where
𝐴
A is an algebraic chiral core,
𝐴
^
s
e
w
A
sew
	​

 is its minimal analytic sewing completion,
𝑄
∙
(
𝐴
)
Q
∙
	​

(A) is its curved bar/coderived shadow across genera, and
𝑀
∂
a
n
(
𝐴
)
M
∂
an
	​

(A) is its boundary/defect module theory. The decisive recent fact is that the pieces now exist separately: Moriwaki has built conformally flat factorization homology valued in IndHilb by left Kan extension from conformally flat disk algebras, with sphere values recovering CFT partition functions under positivity/continuity assumptions, and he has also identified a conformally flat 2-disk algebra on
S
y
m
 
𝐴
2
(
𝐷
)
SymA
2
(D) with the ind-Hilbert completion of the affine Heisenberg VOA; meanwhile Adamo–Moriwaki–Tanimoto prove conformal Osterwalder–Schrader axioms for a class of unitary full VOAs. The missing mathematics is the bridge between these pieces.

So here is that bridge.

1. The correct object is not the bare algebra

The bare VOA or chiral algebra should be regarded only as a dense algebraic skeleton. The actual object is the one on which all sewing operations are continuous and all global amplitudes exist as honest analytic operators. This leads to the first new definition.

Definition 1 — Sewing envelope

Let
𝐴
a
l
g
A
alg
	​

 be an algebraic chiral core with algebraic amplitudes

𝐴
Σ
a
l
g
A
Σ
alg
	​


for every finite conformally flat bordism
Σ
Σ with parametrized in/out collars. For every matrix coefficient of every such amplitude, define a seminorm on
𝐴
a
l
g
A
alg
	​

 by

𝑝
Σ
,
𝜉
,
𝜂
(
𝑎
)
=
∣
⟨
𝜂
,
 
𝐴
Σ
a
l
g
(
𝜉
1
⊗
⋯
⊗
𝑎
⊗
⋯
⊗
𝜉
𝑚
)
⟩
∣
.
p
Σ,ξ,η
	​

(a)=
	​

⟨η,A
Σ
alg
	​

(ξ
1
	​

⊗⋯⊗a⊗⋯⊗ξ
m
	​

)⟩
	​

.

The sewing envelope
𝐴
^
s
e
w
A
sew
	​

 is the Hausdorff completion of
𝐴
a
l
g
A
alg
	​

 for the locally convex topology generated by all seminorms
𝑝
Σ
,
𝜉
,
𝜂
p
Σ,ξ,η
	​

.

This is the minimal completion that remembers every local-to-global operation at once.

Proposition 1 — Universal property

If
𝐸
E is any complete locally convex realization of
𝐴
a
l
g
A
alg
	​

 for which every algebraic amplitude extends continuously, then the identity on
𝐴
a
l
g
A
alg
	​

 extends uniquely to a continuous map

𝐴
^
s
e
w
→
𝐸
.
A
sew
	​

→E.

Proof. Every such realization makes each seminorm
𝑝
Σ
,
𝜉
,
𝜂
p
Σ,ξ,η
	​

 continuous. Hence the identity
𝐴
a
l
g
→
𝐸
A
alg
	​

→E is continuous for the sewing topology. By completeness of
𝐸
E, it extends uniquely from the completion. ∎

This is mundane, but it is the right mundane theorem: it says the analytic completion is canonical once one decides which sewing amplitudes must survive.

2. The minimal analytic condition is Hilbert–Schmidt sewing

To get genuine partition functions and not just formal gluing laws, one needs a quantitative condition.

Definition 2 — HS-sewing condition

Let

𝐻
=
⨁
𝑛
≥
0
𝐻
𝑛
H=
n≥0
⨁
	​

H
n
	​


be a graded pre-Hilbert core, and write the pair-of-pants multiplication as sector maps

𝑚
𝑎
,
𝑏
𝑐
:
𝐻
𝑎
⊗
^
𝐻
𝑏
→
𝐻
𝑐
.
m
a,b
c
	​

:H
a
	​

⊗
^
	​

H
b
	​

→H
c
	​

.

Say
𝐴
A satisfies HS-sewing if there exists
0
<
𝑞
<
1
0<q<1 such that

∑
𝑎
,
𝑏
,
𝑐
≥
0
𝑞
𝑎
+
𝑏
+
𝑐
 
∥
𝑚
𝑎
,
𝑏
𝑐
∥
𝐻
𝑆
2
<
∞
.
a,b,c≥0
∑
	​

q
a+b+c
∥m
a,b
c
	​

∥
HS
2
	​

<∞.

Define the weighted completion

𝐻
𝑞
:
=
⨁
^
𝑛
≥
0
𝑞
𝑛
𝐻
𝑛
.
H
q
	​

:=
⨁
	​

n≥0
	​

q
n
H
n
	​

.
Proposition 2 — Closed amplitudes become trace class

Under HS-sewing, the weighted pair-of-pants map

𝑚
𝑞
:
𝐻
𝑞
⊗
^
𝐻
𝑞
→
𝐻
𝑞
m
q
	​

:H
q
	​

⊗
^
	​

H
q
	​

→H
q
	​


is Hilbert–Schmidt. Consequently, every closed amplitude obtained from finitely many pairs of pants, cups, and caps is trace class on the relevant weighted state space.

Proof. The square Hilbert–Schmidt norm of
𝑚
𝑞
m
q
	​

 is exactly the defining sum. A closed sewing diagram factors as a finite composition of bounded collar-identification maps and pair-of-pants maps. Any composition containing two Hilbert–Schmidt factors is trace class. ∎

This is the point where “formal factorization” becomes “analytic local-to-global.” It also gives the right habitat for partition functions, shadow traces, and spectral invariants.

3. The second completion is bar/coderived, not merely topological

The first completion makes sewing continuous. The second completion makes duality survive curvature.

Definition 3 — Analytic bar coalgebra

For an
𝐸
1
E
1
	​

-type chiral core
𝐴
a
l
g
A
alg
	​

, define the
𝑛
n-th completed bar piece by closing the algebraic bar sector inside the sewing envelope:

𝐵
ˉ
𝑛
a
n
(
𝐴
)
=
𝐴
a
l
g
⊗
𝑛
⊗
Ω
log
⁡
∗
(
𝐶
𝑛
(
𝑋
)
)
‾
 
g
r
a
p
h
(
𝑑
b
a
r
)
.
B
ˉ
n
an
	​

(A)=
A
alg
⊗n
	​

⊗Ω
log
∗
	​

(C
n
	​

(X))
	​

graph(d
bar
	​

)
.

Here

𝑑
b
a
r
=
∑
𝑖
<
𝑗
Res
⁡
𝑧
𝑖
=
𝑧
𝑗
∘
𝑌
𝑖
𝑗
,
d
bar
	​

=
i<j
∑
	​

Res
z
i
	​

=z
j
	​

	​

∘Y
ij
	​

,

and the closure is taken in the graph norm of the closable residue operator
𝑑
b
a
r
d
bar
	​

.

This is the analytic closure of the algebraic bar construction, not a different construction.

Proposition 3 — Positive grading implies conilpotency

Let

𝐶
=
⨁
^
𝑛
≥
0
𝐶
𝑛
C=
⨁
	​

n≥0
	​

C
n
	​


be a coaugmented completed coalgebra with
𝐶
0
=
𝐶
C
0
	​

=C, and suppose the reduced coproduct preserves total degree:

Δ
ˉ
(
𝐶
𝑛
)
⊂
⨁
^
𝑖
+
𝑗
=
𝑛
,
  
𝑖
,
𝑗
>
0
𝐶
𝑖
⊗
^
𝐶
𝑗
.
Δ
ˉ
(C
n
	​

)⊂
⨁
	​

i+j=n,i,j>0
	​

C
i
	​

⊗
^
	​

C
j
	​

.

Then
𝐶
C is conilpotent.

Proof. Every application of
Δ
ˉ
Δ
ˉ
 splits positive degree into a sum of positive degrees. Hence
Δ
ˉ
(
𝑁
)
(
𝐶
𝑛
)
=
0
Δ
ˉ
(N)
(C
n
	​

)=0 for
𝑁
>
𝑛
N>n. ∎

So once the analytic bar object is graded by tensor length or positive conformal weight, conilpotency is built in.

4. Analytic Koszulity is the right duality notion

Now we package the genus-zero and higher-genus stories together.

Definition 4 — Analytic Koszul pair

An analytic Koszul pair
(
𝐴
,
𝐴
!
)
(A,A
!
) consists of:

a sewing envelope
𝐴
^
s
e
w
A
sew
	​

,

an analytic bar coalgebra
𝐵
ˉ
a
n
(
𝐴
)
B
ˉ
an
(A),

a genus-zero equivalence

𝐷
c
o
m
p
l
a
n
(
𝐴
-mod
)
≃
𝐷
c
o
n
i
l
a
n
(
𝐵
ˉ
a
n
(
𝐴
)
-comod
)
,
D
compl
an
	​

(A-mod)≃D
conil
an
	​

(
B
ˉ
an
(A)-comod),

under finite-type dualizability, an identification of conilpotent analytic comodules with complete
𝐴
!
A
!
-modules.

This is the analytic lift of bar/cobar duality.

Principle 5 — Curvature forces coderived passage

At genus
𝑔
g, if the completed bar object carries a curvature term
𝑚
0
(
𝑔
)
≠
0
m
0
(g)
	​


=0, then ordinary cohomology is not the right invariant because the differential satisfies

𝑑
2
=
𝑚
0
(
𝑔
)
⋅
(
−
)
,
d
2
=m
0
(g)
	​

⋅(−),

so honest cohomology stops being functorial under sewing. The correct receptacle is therefore the coderived/contraderived analytic category, not an ordinary derived category.

This is not cosmetic. It is the mechanism by which higher-genus local-to-global data remain nontrivial after completion.

Proposition 4 — Centers survive analytic Koszul duality

Assume an analytic Koszul equivalence

Φ
:
𝐷
c
o
m
p
l
a
n
(
𝐴
)
→
∼
𝐷
c
o
m
p
l
a
n
(
𝐴
!
)
Φ:D
compl
an
	​

(A)
∼
	​

D
compl
an
	​

(A
!
)

sending vacuum to vacuum. Then

𝑍
a
n
(
𝐴
)
≅
𝑍
a
n
(
𝐴
!
)
,
𝑍
a
n
(
𝐴
)
:
=
End
⁡
(
1
𝐴
)
.
Z
an
	​

(A)≅Z
an
	​

(A
!
),Z
an
	​

(A):=End(1
A
	​

).

Proof. Equivalences preserve endomorphism algebras of distinguished objects. ∎

This is the first hint that any genuine “shadow” or complementarity invariant belongs on the completed/global side, not on the bare presentation.

5. The shadow should be a global analytic object
Definition 5 — Analytic shadow

For each genus
𝑔
g, define the analytic shadow

𝑄
𝑔
(
𝐴
)
:
=
𝐷
c
o
 ⁣
(
𝐵
ˉ
𝑔
a
n
(
𝐴
)
-comod
)
.
Q
g
	​

(A):=D
co
	​

(
B
ˉ
g
an
	​

(A)-comod).

When
𝑚
0
(
𝑔
)
=
0
m
0
(g)
	​

=0, this reduces to an honest cohomological object

S
h
𝑔
(
𝐴
)
=
𝐻
∗
Γ
(
𝐵
ˉ
𝑔
a
n
(
𝐴
)
)
.
Sh
g
	​

(A)=H
∗
Γ(
B
ˉ
g
an
	​

(A)).

A complementarity operator is an involution

𝜎
𝑔
:
𝑄
𝑔
(
𝐴
)
→
𝑄
𝑔
(
𝐴
)
σ
g
	​

:Q
g
	​

(A)→Q
g
	​

(A)

induced by duality plus sewing reversal.

When
𝑞
𝐿
0
𝜎
𝑔
q
L
0
	​

σ
g
	​

 is trace class, define the shadow partition function

𝑍
𝑔
s
h
(
𝐴
;
𝜏
)
=
Str
⁡
𝑄
𝑔
(
𝐴
)
 ⁣
(
𝜎
𝑔
 
𝑞
𝐿
0
−
𝑐
/
24
)
.
Z
g
sh
	​

(A;τ)=Str
Q
g
	​

(A)
	​

(σ
g
	​

q
L
0
	​

−c/24
).

By Proposition 2, HS-sewing is exactly the sort of hypothesis that should make this analytic trace converge on a right half-plane. That gives a concrete home for complementarity/modular shadows: they become traces on completed global state spaces, not formal decorations on local OPE coefficients.

6. The Heisenberg theory is the first full laboratory

Here the recent work is especially decisive. Moriwaki constructs a conformally flat 2-disk algebra on
S
y
m
 
𝐴
2
(
𝐷
)
SymA
2
(D), identifies it with the ind-Hilbert completion of the affine Heisenberg vertex algebra, and uses left Kan extension to produce metric-dependent invariants of 2d Riemannian manifolds; he also explicitly points toward Hilbert-analytic analogues of conformal blocks over Teichmüller space for broader unitary VOA inputs.

This suggests an explicit local dictionary.

Definition 6 — Mode–Bergman correspondence

On the algebraic Heisenberg core, define

Θ
(
𝑎
−
𝑛
−
1
1
)
=
𝑛
+
1
 
𝑧
𝑛
∈
𝐴
2
(
𝐷
)
,
Θ(a
−n−1
	​

1)=
n+1
	​

z
n
∈A
2
(D),

and extend multiplicatively by symmetrization:

Θ
(
𝑎
−
𝑛
1
−
1
⋯
𝑎
−
𝑛
𝑘
−
1
1
)
=
Sym
⁡
(
Θ
(
𝑎
−
𝑛
1
−
1
1
)
⊗
⋯
⊗
Θ
(
𝑎
−
𝑛
𝑘
−
1
1
)
)
.
Θ(a
−n
1
	​

−1
	​

⋯a
−n
k
	​

−1
	​

1)=Sym(Θ(a
−n
1
	​

−1
	​

1)⊗⋯⊗Θ(a
−n
k
	​

−1
	​

1)).

This gives a dense algebraic map

Θ
:
Heisenberg Fock core
→
S
y
m
 
𝐴
2
(
𝐷
)
.
Θ:Heisenberg Fock core→SymA
2
(D).
Proposed Theorem A — Heisenberg sewing theorem

Under
Θ
Θ,

the sewing envelope of the algebraic Heisenberg VOA is exactly
S
y
m
 
𝐴
2
(
𝐷
)
SymA
2
(D);

the completed bar differential is the closure of the Gaussian collision operator on Bergman tensors;

pair-of-pants sewing is the second quantization of a one-particle Bergman restriction/composition operator;

every closed amplitude is therefore a Fredholm determinant on the one-particle Bergman space.

The first clause is strongly suggested by Moriwaki’s identification; the rest is the new bridge.

This is the first theorem I would force through. Once it exists, the analytic chiral package is real in rank one, not aspirational.

7. The next extension is lattice data with norms

The right extension of free bosons is not “add more algebra.” It is “add charge sectors with compatible Hilbert control.”

Definition 7 — Analytic theta-datum

An analytic theta-datum is

Θ
a
n
=
(
𝜅
,
{
𝐿
𝛾
}
𝛾
∈
Γ
,
𝑐
,
∥
⋅
∥
)
,
Θ
an
=(κ,{L
γ
	​

}
γ∈Γ
	​

,c,∥⋅∥),

where

(
𝜅
,
𝐿
,
𝑐
)
(κ,L,c) is a theta-type charge datum,

each local section space
Γ
(
𝑈
,
𝐿
𝛾
)
Γ(U,L
γ
	​

) carries a Hilbert norm,

the disjoint-union multiplication maps are bounded,

the collar-sewing maps are Hilbert–Schmidt after weight damping.

Proposed Theorem B — Lattice sewing envelope

Every positive-definite even lattice equipped with an analytic theta-datum admits a canonical sewing envelope, and its completed simple sectors are indexed by discriminant charge exactly as in the algebraic theory, but now realized as honest Hilbert sectors.

The free boson is the
Γ
=
0
Γ=0 case. The novelty is not the combinatorics of charges; it is the existence of a charge-refined analytic sewing completion.

8. The true realization criterion for general unitary full VOAs

Adamo–Moriwaki–Tanimoto prove OS-type analytic control for quasi-primary correlators of a class of unitary full VOAs under energy/spectral growth and local
𝐶
1
C
1
	​

-cofiniteness assumptions. Combined with Moriwaki’s Heisenberg prototype, that points to the next theorem.

Main Conjecture C — Analytic realization criterion

Let
𝑉
V be a unitary full VOA such that:

its quasi-primary correlators satisfy conformal OS axioms,

its graded pieces have polynomial spectral growth,

its intertwining/screening OPE maps satisfy HS-sewing after exponential weight damping.

Then
𝑉
V admits:

𝑉
a
l
g
⟶
𝑉
^
s
e
w
∈
I
n
d
H
i
l
b
,
V
alg
	​

⟶
V
sew
	​

∈IndHilb,

a conformally flat 2-disk algebra
𝐹
𝑉
F
V
	​

, a genus-zero analytic Koszul duality package, and a higher-genus coderived shadow
𝑄
∙
(
𝑉
)
Q
∙
	​

(V).

This is the theorem that would turn “unitary full VOA” into “analytic local-to-global field theory.”

9. Boundary data must be built in from the start

The platonic object is incomplete without boundaries.

Definition 8 — Analytic boundary condition

An analytic boundary condition for
𝐴
A is a complete module
𝑀
M equipped with continuous half-disk actions

𝐴
(
𝑈
)
⊗
^
𝑀
(
𝐼
)
→
𝑀
(
𝐼
′
)
A(U)
⊗
^
	​

M(I)→M(I
′
)

compatible with collar sewing and reflection.

Proposed Theorem D — Boundary bar duality

For an analytically Koszul
𝐴
A,

genus
0
0: completed boundary modules are equivalent to analytic comodules over
𝐵
ˉ
a
n
(
𝐴
)
B
ˉ
an
(A),

curved genus: the correct objects are analytic contramodules over the curved dual.

This is where branes, open strings, and boundary chiral algebras should actually live.

10. The systematic execution order

To make this real, the order matters.

First, prove Theorem A for Heisenberg. That locks the local completion, the sewing analysis, and the analytic bar package to one explicit Gaussian model.

Second, prove the HS-sewing criterion in the Heisenberg model with explicit one-particle estimates. That turns determinants and partition functions into theorems rather than slogans.

Third, extend from Heisenberg to lattice theories via analytic theta-data. This imports charge sectors without changing the basic analytic mechanism.

Fourth, formulate and prove a local realization theorem for the class of unitary full VOAs covered by the OS result. That is the jump from prototype to structure theorem.

Fifth, build the higher-genus coderived shadow and its complementarity involution. Only here do modular and duality shadows become the right kind of invariant.

11. The platonic ideal state, stated plainly

The platonic ideal form is not a bare chiral algebra.

It is:

a dense algebraic core
𝐴
a
l
g
A
alg
	​

,

its canonical sewing envelope
𝐴
^
s
e
w
A
sew
	​

,

an IndHilb-valued factorization/local-to-global theory on conformally flat surfaces,

a reflection-positive boundary module theory,

and a curved bar/coderived shadow
𝑄
∙
(
𝐴
)
Q
∙
	​

(A) where higher-genus dualities actually survive.

In one line:

formal OPE data
  
⊂
  
sewing envelope
  
⇝
  
Hilbert factorization theory
  
⇝
  
coderived shadow invariants
formal OPE data⊂sewing envelope⇝Hilbert factorization theory⇝coderived shadow invariants
	​


That is the organism. The algebra alone is only its skeleton.

The first proof to force next is the Heisenberg sewing theorem. Once that is in hand, the rest stops being mystical and becomes deformation theory around a solved analytic core.
