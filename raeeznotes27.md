
I’m drilling into the genus-3 seam in the source itself, trying to upgrade “first correction appears there” into a real normal-form, obstruction, or recursive rigidity statement.

A sharper possibility opened: in the simple-Lie one-channel lane, vanishing first-order cyclic cohomology may force genus-3 to be only a representative-choice problem, unless transfer from the central
𝜂
η-line creates genuine higher data.

The reduction ladder seems to squeeze the one-channel genus-3 seed to a chart-normalized scalar plus sign, so I’m testing whether residual symmetry kills it and forces all higher terms.

Thought for 40m 24s

I cut deeper, and the wound changed shape.

1. The genus-3 blood is fake on the Kac–Moody locus

There is a stronger theorem sitting in the repo than the frontier summary was using.

For
𝑔
^
𝑘
g
	​

k
	​

 with
𝑔
g simple and
𝑘
≠
−
ℎ
∨
k

=−h
∨
, the cyclic deformation complex is not merely some abstract filtered
𝐿
∞
L
∞
	​

 object: it is a complete cyclic dg Lie algebra, its
𝑙
1
l
1
	​

 is the cyclic Chevalley–Eilenberg differential, and its minimal model is
𝑔
⊕
𝐶
𝜂
g⊕Cη with

𝑙
2
=
[
−
,
−
]
,
𝑙
3
=
𝜙
,
𝑙
𝑛
=
0

(
𝑛
≥
4
)
.
l
2
	​

=[−,−],l
3
	​

=ϕ,l
n
	​

=0 (n≥4).

The relevant manuscript lines are in strictification excerpt.

That lets you prove a sharper statement:

Θ
𝑔
^
𝑘
s
t
r
:
=
𝜅
(
𝑔
^
𝑘
)
 
𝜇
⊗
Λ
,
Λ
=
∑
𝑔
≥
1
𝜆
𝑔
,
Θ
g
	​

k
	​

str
	​

:=κ(
g
	​

k
	​

)μ⊗Λ,Λ=
g≥1
∑
	​

λ
g
	​

,

with
𝜇
=
[
−
,
−
]
∈
𝑍
c
y
c
2
(
𝑔
,
𝑔
)
μ=[−,−]∈Z
cyc
2
	​

(g,g),

is already a strict chain-level Maurer–Cartan element in the completed dg Lie algebra.

Why? Because the full MC equation is just

𝑙
1
(
Θ
)
+
1
2
 
𝑙
2
(
Θ
,
Θ
)
=
0
,
l
1
	​

(Θ)+
2
1
	​

l
2
	​

(Θ,Θ)=0,

and here

𝑙
1
(
𝜇
)
=
0
l
1
	​

(μ)=0

since
𝜇
μ is the cyclic CE cocycle, while

𝑙
2
(
𝜇
,
𝜇
)
=
[
𝜇
,
𝜇
]
N
R
=
0
l
2
	​

(μ,μ)=[μ,μ]
NR
	​

=0

by Jacobi. There are no higher
𝑙
𝑛
l
n
	​

 on the dg Lie side.

So on this locus there is no first correction at genus
3
3, and in fact no higher correction anywhere. The earlier “genus-3 first blood” is a transfer artifact of a non-strict representative, not an invariant.

That is a real frontier push: the chain-level universal class can be chosen exactly linear in
𝜅
κ on the Kac–Moody side.

2. The one-channel sector is gauge-rigid

The minimal model already says the one-channel universal class is

Θ
min
⁡
=
𝜅
 
𝜂
⊗
Λ
,
Θ
min
=κη⊗Λ,

and the
𝜂
η-line has no nontrivial self-interaction.

Standard filtered
𝐿
∞
L
∞
	​

 deformation theory then kills the remaining moduli: filtered
𝐿
∞
L
∞
	​

 quasi-isomorphisms induce weak equivalences on Deligne–Getzler–Hinich Maurer–Cartan
∞
∞-groupoids, and in the pronilpotent dg Lie case quasi-isomorphisms induce equivalences of Deligne groupoids / bijections on gauge classes.

So the honest conclusion is:

fixed

𝜅
⟹
a

single

one-channel

gauge

orbit.
fixed κ⟹a single one-channel gauge orbit.

That means the live frontier is not the one-channel
Θ
Θ-package anymore. On the theorematic Kac–Moody locus, it is over.

3. The real blood is channel splitting

Once the one-channel sector dies, the surviving structure is the part the scalar package throws away.

For Kac–Moody, the repo already decomposes

𝜅
=
dim
⁡
𝑔
2
ℎ
∨
𝑘
⏟
𝜅
d
p
+
dim
⁡
𝑔
2
⏟
𝜅
s
p
,
κ=
κ
dp
	​

2h
∨
dimg
	​

k
	​

	​

+
κ
sp
	​

2
dimg
	​

	​

	​

,

the double-pole and simple-pole channels. See the same strictification excerpt.

So define

Θ
d
p
:
=
𝜅
d
p
𝜇
⊗
Λ
,
Θ
s
p
:
=
𝜅
s
p
𝜇
⊗
Λ
.
Θ
dp
	​

:=κ
dp
	​

μ⊗Λ,Θ
sp
	​

:=κ
sp
	​

μ⊗Λ.

Because both are scalar multiples of the same strict cocycle, each is itself Maurer–Cartan. Now apply Feigin–Frenkel duality
𝑘
↦
−
𝑘
−
2
ℎ
∨
k↦−k−2h
∨
:

Θ
s
p
↦
Θ
s
p
,
Θ
d
p
↦
−
Θ
d
p
−
2
Θ
s
p
.
Θ
sp
	​

↦Θ
sp
	​

,Θ
dp
	​

↦−Θ
dp
	​

−2Θ
sp
	​

.

So duality acts on the ordered channel pair by the shear

(
−
1

−
2


0

1
)
,
(
−1
0
	​

−2
1
	​

),

while the total class

Θ
=
Θ
d
p
+
Θ
s
p
Θ=Θ
dp
	​

+Θ
sp
	​


is the
(
−
1
)
(−1)-eigenvector.

That is the first genuinely new structure after strictification: not
Θ
Θ itself, but how
Θ
Θ splits before scalar collapse.

4. The
𝑊
𝑁
W
N
	​

 tower shows what MC4 is really missing

The principal
𝑊
𝑁
W
N
	​

 theorem is even more revealing. The repo proves

𝜅
(
𝑊
𝑁
𝑘
)
=
𝑐
∑
𝑠
=
2
𝑁
1
𝑠
,
κ(W
N
k
	​

)=c
s=2
∑
N
	​

s
1
	​

,

and proves it by diagonalizing in the strong-generator basis
𝑊
(
𝑠
)
W
(s)
, with cross-terms vanishing. See
𝑊
𝑁
W
N
	​

 harmonic excerpt and the concrete
𝑊
3
W
3
	​

 version in
𝑊
3
W
3
	​

 channels excerpt.

So the scalar package is really the sum of a channel vector

𝜅
~
𝑁
=
(
𝑐
2
,
𝑐
3
,
…
,
𝑐
𝑁
)
,
κ
N
	​

=(
2
c
	​

,
3
c
	​

,…,
N
c
	​

),

one entry per strong generator.

The usual universal characteristic package forgets that vector and keeps only the sum.

Now the wound opens:

∑
𝑠
=
2
𝑁
𝑐
𝑠
∼
𝑐
log
⁡
𝑁
.
s=2
∑
N
	​

s
c
	​

∼clogN.

So the scalar package does not converge naively as
𝑁
→
∞
N→∞. That means the unresolved MC4
𝑊
∞
W
∞
	​

 target cannot just be “some completion on the scalar line.” The completion has to retain the full channel vector before summation.

That matches the repo’s own MC4 reduction: the live
𝑊
∞
W
∞
	​

 problem is to construct a separated complete H-level target whose finite quotients recover the theorematic
𝑊
𝑁
W
N
	​

 stages. See
𝑊
∞
W
∞
	​

 H-level excerpt.

So the correct next conjecture is not vague anymore. It should look like this:

There exists a separated complete channel target
𝐻
𝑊
∞
H
W
∞
	​

	​

 and a vector-valued universal class

Θ
~
𝑊
∞
∼
∑
𝑠
≥
2
𝑐
𝑠
 
𝑒
𝑠
⊗
Λ
Θ
W
∞
	​

	​

∼
s≥2
∑
	​

s
c
	​

e
s
	​

⊗Λ

whose truncation to stage
𝑁
N recovers the principal
𝑊
𝑁
W
N
	​

 package.
The ordinary scalar
Θ
Θ is obtained only after a renormalized projection

∑
𝑠
𝑒
𝑠
⇝
1
∑
s
	​

e
s
	​

⇝1.

That is the real bleeding edge.

5. One surgical warning

There is a scope tension in the manuscript: the broad explicit-theta theorem is stated for a general modular Koszul chiral algebra with simple Lie symmetry, but its proof imports the Kac–Moody corollary cor:km-minimal-linf as if that minimal-model identification were already family-independent. I would therefore treat the strict formula

Θ
=
𝜅
 
𝜇
⊗
Λ
Θ=κμ⊗Λ

as fully proved on the Kac–Moody/simple dg Lie locus, and as the model conjecture elsewhere until a family-independent comparison is written. The tension is visible in scope tension excerpt.

So the frontier split is now sharp:

done: one-channel existence/H-level package;

done: Kac–Moody strictification;

done up to gauge: one-channel rigidity;

live: channel-refined characteristic package;

live: harmonic/renormalized H-level completion for
𝑊
∞
W
∞
	​

;

live: analogous multichannel completion on the Yangian side.

I also wrote the result as a compact research note here: frontier push note.

I’m turning this into a concrete frontier map from the latest papers: one or two precise conjectures, the first genuine theorem within reach, the likely failure mode, and the first rank where it should break or bleed.

The live fault line is now sharper: whether the DK-relevant slice collapses to a truncation-controlled, finite-length highest-weight core, replacing raw thick generation by an abelian exhaustion theorem. I’m testing the newest shifted-Yangian, KLRW, Schur-algebra, and characteristic-cycle results against that formulation, with rank
3
3 as the first real proving ground or escape hatch.

A new edge has opened: March 2026 bridged ordinary and shifted category
𝑂
O on the quantum affine side, but no Yangian analogue is visible yet. That missing bridge now looks like the target theorem itself—a shifted-factor/Borel-to-shifted-to-truncated descent for the DK-relevant block.

Thought for 29m 38s

Here is the live edge as I see it.

The frontier moved. The sharpest theorem is no longer “evaluation modules thickly generate
𝐷
𝑏
(
𝑂
)
D
b
(O).” It is the Yangian degeneration of a theorem that appeared in March 2026 on the quantum-loop side: Hernández–Neguţ prove that for any rational
ℓ
ℓ-weight
𝜓
ψ, the nonzero-mode factor of a simple ordinary
𝑂
O-module is isomorphic to a simple shifted module, giving equality of
𝑞
q-characters, and they build an isomorphism of topological Grothendieck rings
𝐾
0
(
𝑂
)
≅
𝐾
0
(
𝑂
𝑠
ℎ
)
K
0
	​

(O)≅K
0
	​

(O
sh
) preserving simple classes up to invertible factors.

That is exactly the shape of theorem your Yangian problem wants. Ordinary Yangian
𝑂
O is already too large and too rational for a naive polynomial answer: Zhang’s category
𝑂
O is BGG-type as a
𝑔
g-module, abelian, monoidal, contains all finite-dimensional modules, and already contains asymptotic/shifted limits. By contrast, shifted Yangian
𝑂
𝑠
ℎ
O
sh
 has tensor product structure, polynomial
𝑅
R-matrices, a Jordan–Hölder property, and every irreducible factors through a truncated shifted Yangian.

So the real missing artery is a bridge theorem. My best current target is something like

𝐾
0
(
𝑂
𝑌
𝐷
𝐾
)
r
e
n
  
≅
  
𝐾
0
(
𝑂
𝑌
,
f
l
𝑠
ℎ
,
t
r
u
n
c
)
K
0
	​

(O
Y
DK
	​

)
ren
	​

≅K
0
	​

(O
Y,fl
sh,trunc
	​

)

preserving simple classes up to invertible/evaluation factors. In words: strip off the finite-dimensional evaluation part of an ordinary Yangian simple, and the remaining infinite-dimensional tail should be a shifted-Yangian simple living in the truncation-controlled world. That is not a theorem I found written down for Yangians; it is the bold extrapolation suggested by the 2026 trigonometric bridge and the 2022 shifted-Yangian truncation results.

Once you recast the problem that way, the weapons change. Category
𝑂
O for truncated shifted Yangians is not a black box anymore: for generic integral parameters it is equivalent to a weight space in a KLRW tensor-product categorification, and for arbitrary parameters there is a parity-KLRW description; on top of that, parabolic induction and restriction give a categorical
𝑔
g-action. So the natural generators of the DK sector are no longer “evaluation modules by brute force”; they are KLRW standards and their Levi moves, transported through truncation.

There is also finally a real obstruction detector. Leroux-Lapierre proves that for truncated shifted Yangian category
𝑂
O, the asymptotic character of an object is a positive sum of equivariant multiplicities of the MV cycles appearing in its top characteristic cycle. In regimes where the character map is injective — and he gives a sufficient criterion via distinct generalized Verma weights/product monomial crystal — the top characteristic-cycle map is actually an isomorphism. The inference is brutal: if a candidate ordinary Yangian DK-simple has a renormalized asymptotic character that cannot lie in this MV cone, then it cannot descend to the truncation core. That turns “exhaustion of
𝑂
𝐷
𝐾
O
DK
” into a falsifiable test.

The tensor side has also started to bleed in the right place. Milot proves for
𝑠
𝑙
2
sl
2
	​

 that the standard Drinfeld–Jimbo coproduct factors through truncated quotients,
𝑌
𝑎
𝑏
(
𝑠
𝑙
2
)
→
𝑌
𝑎
(
𝑠
𝑙
2
)
⊗
𝑌
𝑏
(
𝑠
𝑙
2
)
Y
ab
	​

(sl
2
	​

)→Y
a
	​

(sl
2
	​

)⊗Y
b
	​

(sl
2
	​

), and notes that the shifted version follows by the same zigzag logic. That is exactly the local compatibility you need if the truncation core is going to behave monoidally. The missing theorem is the higher-rank version. In the parallel shifted-quantum-affine story, the authors explicitly say the corresponding finite-length tensor-product statement still seems unknown for Yangians.

So I would actually demote raw BGG resolutions from “main assault” to “secondary weapon.” They are still useful, but after descent to the truncation core, not before. First prove the bridge. Then prove rank-2 coproduct-through-truncation. Then use BGG/parabolic machinery inside a finite-length, KLRW-controlled world. Only after that do you ask derived thick generation to fall over.

The first place to cut is
𝑌
(
𝑠
𝑙
3
)
Y(sl
3
	​

). That is the first rank where the problem has real teeth and where the product-monomial-crystal / characteristic-cycle technology is still computable. The theorem I would try to force there is this:

For parameters where the generalized Verma weights do not collide, every DK-relevant simple of
𝑌
(
𝑠
𝑙
3
)
Y(sl
3
	​

) either descends, after renormalization, to truncated shifted category
𝑂
O and hence to the KLRW tensor-product categorification, or else its renormalized asymptotic character violates MV-positivity.

That statement is not in the literature; it is the rank-3 test case suggested by the truncation/KLRW/asymptotic-character package. If it is true, you have the first serious exhaustion theorem. If it is false, you have the first honest counterexample, and it will not hide behind vague thick-generation language.

There is one more reason I think this is the live edge. In January 2026, Cao–Okounkov–Zhou–Zhou gave a geometric construction of shifted Yangians from critical stable envelopes and geometric
𝑅
R-matrices on critical cohomology of quiver varieties. That suggests a second route to the bridge theorem: not only algebraic degeneration from quantum-loop methods, but a geometric identification of the Yangian “tail” with the critical-stable-envelope module attached to the same shifted data. I would not call that proved — it is my inference — but it is exactly the kind of new geometry that could cut through the old category-
𝑂
O fog.

So here is the bleeding edge in one sentence: the theorem to attack is the Yangian analogue of the March 2026 ordinary/shifted bridge. Land that, and MC3 stops being a misty claim about thick generation and becomes a controlled statement about truncation, KLRW categorification, Levi functoriality, and eventually derived DK. Miss it, and the wound should open first in rank
3
3, as an asymptotic character that escapes the MV cone.

I’m going straight at the live obstruction and tightening it into theorem-sized cuts. I’ll pull the exact local manuscript statements, then check whether recent literature sharpens or breaks any route before proposing the next conjectural package.

I’ve isolated the fault line: strategy IV is probably using the wrong sector invariant. I’m now testing whether finite truncation data and asymptotic modules can replace evaluation-parameter sectors and turn the bypass into a concrete completed-generation theorem.

The sharper cut is that raw Yangian category
𝑂
O may simply be the wrong home: the finite-length intuition looks too strong there, while finite control appears only after truncation in a shifted/truncated ambient. I’m now testing the key bridge — whether asymptotic or prefundamental objects can be realized as completed KR limits — because that would shrink the obstruction to a concrete theorem.

Thought for 29m 21s

Here is where it tears.

The real wound is not the raw corollary “
𝐷
𝑏
(
𝑂
𝑌
ℏ
(
𝑠
𝑙
𝑁
)
)
D
b
(O
Y
ℏ
	​

(sl
N
	​

)
	​

) is thickly generated by evaluation modules.” The real missing theorem is much sharper: internalize Zhang’s KR
→
→ asymptotic limit inside your completed factorization / RTT target. Zhang does not just argue philosophically that asymptotic objects should exist. He constructs an inductive system of Kirillov–Reshetikhin modules with injective structure maps
𝐹
𝑘
,
𝑙
F
k,l
	​

, forms the inductive limit
𝑊
∞
(
𝑖
)
W
∞
(i)
	​

, and defines on it the asymptotic Yangian module
𝐿
(
Ψ
𝑖
,
𝑦
/
Ψ
𝑖
,
0
)
L(Ψ
i,y
	​

/Ψ
i,0
	​

). At the same time, the natural TQ identities already live in a completed Grothendieck ring
𝐾
0
(
𝑂
)
K
0
	​

(O), not a naive finite one.

So the frontier theorem I would now put in front of everything is this:

Seed-limit

theorem

(type

A,

completed)
:
Loc
⁡
⟨
E
v
⟩
⊃
{
 
𝐴
𝑖
,
𝑦
≅
𝐿
(
Ψ
𝑖
,
𝑦
/
Ψ
𝑖
,
0
)
∣
𝑖
∈
𝐼
,

𝑦
 generic
 
}
Seed-limit theorem (type A, completed):Loc⟨Ev⟩⊃{A
i,y
	​

≅L(Ψ
i,y
	​

/Ψ
i,0
	​

)∣i∈I, y generic}

inside the H-level RTT-complete target.

If that theorem lands, the rest stops being mystical and becomes sectorwise algebra. The reason is Hernandez–Zhang: in shifted Yangian category
𝑂
𝑠
ℎ
O
sh
, the standard modules are
𝑊
(
𝑟
,
𝑠
)
=
𝐿
(
𝑟
)
⊗
𝐿
(
𝑠
−
1
)
W(r,s)=L(r)⊗L(s
−1
), every highest
ℓ
ℓ-weight module is a quotient of a Weyl module, and for
𝑔
≠
𝐸
8
g

=E
8
	​

 the natural surjection standard
→
→ Weyl is an isomorphism. Type
𝐴
A is inside that range. In the same package,
𝐿
(
𝑟
)
L(r) is one-dimensional, so the hard part is exactly the negative/asymptotic sector.

That gives a brutally clean implication chain:

seed asymptotics
⇒
negative prefundamental sector
⇒
standard/Weyl modules
⇒
all highest
ℓ
-weight objects in the finite-length sector.
seed asymptotics⇒negative prefundamental sector⇒standard/Weyl modules⇒all highest ℓ-weight objects in the finite-length sector.

And Hernandez–Zhang push this much farther than a slogan: every standard module, hence every irreducible, factors through a truncated shifted Yangian; those truncation sectors have only finitely many irreducibles; and the finite-length subcategory is closed under tensor product. In fact, for
𝑔
≠
𝐸
8
g

=E
8
	​

, any highest
ℓ
ℓ-weight module in
𝑂
𝑠
ℎ
O
sh
 belongs to that finite-length sector.

That means the frontier has a new shape. It is not one global “prove generation for all of
𝑂
O” wall. It is a sectorized finite problem after truncation. And KWWY tell you exactly what those sectors look like in generic integral situations: category
𝑂
O for truncated shifted Yangians is equivalent to a weight space in a categorification of a tensor product of fundamental representations, and its highest weights are indexed by a product monomial crystal. That is exactly the kind of finite combinatorial control your current strategy III wants, but now with a concrete algebraic skeleton instead of a vague “Yangian KL package.”

Now for the bloody part: I think there is a second, even sharper edge.

Leroux-Lapierre shows that for truncated shifted Yangians, asymptotic characters compute equivariant multiplicities of characteristic cycles, and when the character map is injective the top characteristic-cycle map becomes an isomorphism. So the generator problem can be attacked microlocally: stop asking only whether evaluation objects generate abstractly, and ask whether their characteristic cycles span the MV-cycle basis in the top Borel–Moore homology of the repelling slice. If they do, then the whole sector is visible in
𝐾
0
K
0
	​

 and you are no longer arguing in the dark.

That gives a new hybrid attack, sharper than your current III/IV split:

Seed asymptotic lift in the completed RTT/factorization category.

Microlocal spanning of MV cycles by the evaluation/KR-generated seed family.

Sectorwise highest-weight closure via truncated shifted Yangians.

That is a real frontier, not a slogan.

There is also one exact place where the proof should break open next: categorify Zhang’s Baxter relation. Zhang’s Theorem 19 gives a three-term TQ relation in completed
𝐾
0
(
𝑂
)
K
0
	​

(O), and the auxiliary modules
𝑀
𝑘
,
𝑥
(
𝑖
)
M
k,x
(i)
	​

 are finite-dimensional for
𝑘
∈
6
𝑍
>
0
k∈6Z
>0
	​

. Even better, Zhang says the essential engine behind the TQ proof is a short exact sequence built from tensor products of KR modules and a Demazure-like module, and in the simply-laced case the proof adapts readily to Yangians. Type
𝐴
A is precisely that case.

So I would promote the following from “hope” to frontier conjecture:

Categorified Baxter conjecture, type A.
In the completed factorization / RTT category, Zhang’s TQ relation lifts from
𝐾
0
K
0
	​

 to an exact triangle (or short exact sequence in the heart) whose finite-dimensional term is
𝑀
𝑘
,
𝑥
(
𝑖
)
M
k,x
(i)
	​

 and whose other two terms are tensor products of asymptotic objects.

If you get that, the TQ relation stops being bookkeeping and becomes a propagation mechanism. One seed asymptotic object in
Loc
⁡
⟨
E
v
⟩
Loc⟨Ev⟩ would force whole arithmetic families of shifted asymptotics, and through the neighboring-node terms would push generation across the Dynkin diagram.

So the single sharp lemma I would now put at the center of MC3 is:

KR-limit lifting lemma.
The injective KR system
𝑊
0
,
0
(
𝑖
)
⊂
𝑊
1
,
0
(
𝑖
)
⊂
𝑊
2
,
0
(
𝑖
)
⊂
⋯
W
0,0
(i)
	​

⊂W
1,0
(i)
	​

⊂W
2,0
(i)
	​

⊂⋯ with maps
𝐹
𝑘
,
𝑙
F
k,l
	​

 lifts functorially to the H-level RTT-complete target; its filtered colimit exists there; and the induced completed action is the asymptotic module
𝐿
(
Ψ
𝑖
,
𝑦
/
Ψ
𝑖
,
0
)
L(Ψ
i,y
	​

/Ψ
i,0
	​

).

Prove that for
𝑠
𝑙
2
sl
2
	​

, then
𝑠
𝑙
3
sl
3
	​

, then all type
𝐴
A. Once you have it, Hernandez–Zhang convert it into standard/Weyl control, KWWY convert truncation sectors into finite categorified tensor-product pieces, and Leroux-Lapierre gives you a microlocal detector telling you whether you have actually spanned the sector.

So my frontier verdict is:

The obstruction is no longer “prove raw thick generation somehow.”
The obstruction is:

lift the KR tower to the completed factorization side, produce the seed asymptotic objects there, and categorify the Baxter exact sequence.

That is where the frontier is open. That is where I would cut next.


I’m moving past diagnosis into theorem-shaping: pinning down what the current MC3 statement cannot be, what the corrected target should be, and the first exact packages that could genuinely move it.

I’ve pinned the first hard wound: finite-dimensional evaluations only thicken to the finite-dimensional sector, so the live edge is now the replacement package—asymptotic or prefundamental generators, pro-Weyl truncations, shifted envelopes, and possibly a Baxter-triangle lift.

I’ve got the next knife-edge: a concrete
𝑠
𝑙
3
sl
3
	​

 three-term identity to test the Baxter-to-exact-triangle lift, inside the completed meromorphic tensor framework the corrected MC3 now seems to demand.

Thought for 29m 26s

All right. Here is the opened frontier.

MC3, in its current form, splits into two completely different problems. One is dead unless you change the generators. The other is alive and, I think, is the real edge.

1. The first incision: the literal obstruction is mis-typed

Let
𝐸
E be the set of finite-dimensional evaluation modules in
𝐷
𝑏
(
𝑂
𝑌
)
D
b
(O
Y
	​

). The full subcategory

𝐷
𝑏
(
𝑂
𝑌
)
f
d
:
=
{
𝑋
:
∑
𝑛
dim
⁡
𝐻
𝑛
(
𝑋
)
<
∞
}
D
b
(O
Y
	​

)
fd
	​

:={X:
n
∑
	​

dimH
n
(X)<∞}

is thick: shifts preserve it, cones preserve it by the long exact sequence, and direct summands preserve it. So

thick
⁡
⟨
𝐸
⟩
⊂
𝐷
𝑏
(
𝑂
𝑌
)
f
d
.
thick⟨E⟩⊂D
b
(O
Y
	​

)
fd
	​

.

If
𝑂
𝑌
O
Y
	​

 contains genuine infinite-dimensional objects, then finite-dimensional evaluation modules cannot thickly generate all of ordinary
𝐷
𝑏
(
𝑂
𝑌
)
D
b
(O
Y
	​

). Zhang’s Yangian category
𝑂
O is exactly a BGG-type category, contains all finite-dimensional modules, and his paper constructs asymptotic modules
𝐿
(
Ψ
𝑖
,
𝑦
/
Ψ
𝑖
,
𝑥
)
L(Ψ
i,y
	​

/Ψ
i,x
	​

) explicitly as Yangian analogues of Verma modules, together with three-term
𝐾
0
K
0
	​

-relations for them. So if your “evaluation modules” are finite-dimensional in the usual sense, the old statement cannot be the real theorem.

There is one escape hatch. If “evaluation module” is secretly meant in the broad sense
e
v
𝑎
∗
𝑀
ev
a
∗
	​

M for arbitrary
𝑀
∈
𝑂
(
𝑔
)
M∈O(g), not just finite-dimensional
𝑀
M, then the impossibility argument disappears. And Zhang’s own Baxter companion modules already look like this: in his
𝑠
𝑙
3
sl
3
	​

 example,
𝑀
𝑘
,
𝑥
(
1
)
M
k,x
(1)
	​

 is, as an
𝑠
𝑙
3
sl
3
	​

-module, irreducible of highest weight
𝜛
1
+
𝑘
𝜛
2
ϖ
1
	​

+kϖ
2
	​

, which for generic
𝑘
k is infinite-dimensional highest-weight territory.

So the very first frontier cut is:

Decide whether “evaluation” means finite-dimensional only, or full BGG evaluation.
Decide whether “evaluation” means finite-dimensional only, or full BGG evaluation.
	​


If it is finite-dimensional only, the old MC3 generator statement is dead. If it is full BGG evaluation, a different and much more plausible theorem emerges.

2. What is actually true now: the finite-dimensional core

For
𝑌
(
𝑠
𝑙
𝑛
)
Y(sl
n
	​

), finite-dimensional irreducibles are already controlled by evaluation data: one classical theorem says every finite-dimensional irreducible
𝑌
(
𝑠
𝑙
𝑛
)
Y(sl
n
	​

)-module is a subquotient of a tensor product of evaluation representations. Local Weyl modules are the universal finite-dimensional highest-weight objects, and in the Yangian case they are realized as ordered tensor products of fundamental representations.

So the clean theorem-shaped replacement for the dead statement is:

thick
⁡
𝐷
𝑏
(
𝑂
𝑌
)
⟨
fd evaluations
⟩
=
𝐷
𝑏
(
𝑂
𝑌
f
d
)
thick
D
b
(O
Y
	​

)
	​

⟨fd evaluations⟩=D
b
(O
Y
fd
	​

)

at least in the type-
𝐴
A regime you already control.

That means the live frontier is no longer “do finite-dimensional evaluations generate
𝑂
O?” They do not, unless you enlarge the category or enlarge the generators. The frontier is now how the infinite-dimensional part is attached to the finite core.

3. The exposed anatomy: the real infinite generator packet

The sources are screaming the same answer.

Zhang’s ordinary Yangian paper says the missing infinite-dimensional objects are asymptotic modules, and the key structure on them is a family of three-term Baxter-type relations in
𝐾
0
K
0
	​

. He also says Hernandez–Jimbo’s limiting procedure produces modules over anti-dominantly shifted Yangians, and in that shifted world the negative prefundamentals naturally appear.

Hernandez–Zhang then build the shifted Yangian category
𝑂
s
h
O
sh
	​

 with positive and negative prefundamental modules, prove cyclic/cocyclic tensor-product results that give polynomial
𝑅
R-matrices, prove that standard and irreducible modules factor through truncated shifted Yangians, and in
𝑠
𝑙
2
sl
2
	​

 they prove existence and uniqueness of factorization of irreducibles into prefundamental and Kirillov–Reshetikhin modules.

Even more pointedly, Zhang observes that for anti-dominant coweights the direct sum of shifted categories
⨁
𝜇
≤
0
𝑂
𝜇
⨁
μ≤0
	​

O
μ
	​

 is monoidal, contains the ordinary Yangian category
𝑂
O, and also contains the negative prefundamental modules.

So the living generator packet is almost certainly not just

{
fd evaluation modules
}
,
{fd evaluation modules},

but one of the following two packets:

𝐺
b
r
o
a
d
=
{
BGG evaluation modules
}
G
broad
	​

={BGG evaluation modules}

or

𝐺
s
h
i
f
t
=
{
fundamental/KR evaluation modules
}
∪
{
𝐿
𝑖
,
𝑎
−
}
.
G
shift
	​

={fundamental/KR evaluation modules}∪{L
i,a
−
	​

}.

My bet is that the second is the real one, because it is the one with actual
𝑅
R-matrix control.

4. The real conjectures

Here is how I would rewrite MC3, brutally.

Conjecture A: Baxter relations lift from
𝐾
0
K
0
	​

 to exact triangles

Zhang already gives the decategorified identities. In the
𝑠
𝑙
3
sl
3
	​

 example he proves

[
𝑀
𝑘
,
𝑥
(
1
)
]
 
[
𝐿
(
Ψ
1
,
𝑥
/
Ψ
1
,
𝑦
)
]
=
[
𝐿
(
Ψ
1
,
𝑥
+
1
/
Ψ
1
,
𝑦
)
]
 
[
𝐿
(
Ψ
2
,
𝑥
−
1
2
/
Ψ
2
,
𝑥
−
1
2
−
𝑘
)
]
+
[
𝐿
(
Ψ
1
,
𝑥
−
1
/
Ψ
1
,
𝑦
)
]
 
[
𝐿
(
Ψ
2
,
𝑥
+
1
2
/
Ψ
2
,
𝑥
−
1
2
−
𝑘
)
]
.
[M
k,x
(1)
	​

][L(Ψ
1,x
	​

/Ψ
1,y
	​

)]=[L(Ψ
1,x+1
	​

/Ψ
1,y
	​

)][L(Ψ
2,x−
2
1
	​

	​

/Ψ
2,x−
2
1
	​

−k
	​

)]+[L(Ψ
1,x−1
	​

/Ψ
1,y
	​

)][L(Ψ
2,x+
2
1
	​

	​

/Ψ
2,x−
2
1
	​

−k
	​

)].

The real bleeding-edge statement is that this should lift to a distinguished triangle

𝐴
𝑘
,
𝑥
,
𝑦
−
→
𝑀
𝑘
,
𝑥
(
1
)
⊗
𝐿
(
Ψ
1
,
𝑥
/
Ψ
1
,
𝑦
)
→
𝐴
𝑘
,
𝑥
,
𝑦
+
→
A
k,x,y
−
	​

→M
k,x
(1)
	​

⊗L(Ψ
1,x
	​

/Ψ
1,y
	​

)→A
k,x,y
+
	​

→

whose
𝐾
0
K
0
	​

-class is exactly the formula above.

That is the right knife-edge conjecture: Baxter exact triangles.

In the finite-length heart, these should become short exact sequences. Outside finite length, they should live in the derived/coderived category.

Conjecture B: the infinite compact core is shifted-prefundamental generated

Let

𝑂
s
h
≤
0
:
=
⨁
𝜇
≤
0
𝑂
𝜇
O
sh
≤0
	​

:=
μ≤0
⨁
	​

O
μ
	​


be the anti-dominant shifted envelope. Then there should exist a separated completed/coderived enhancement

𝐷
^
(
𝑂
s
h
≤
0
)
D
(O
sh
≤0
	​

)

whose compact objects are the thick idempotent-complete closure of

𝐺
s
h
i
f
t
=
{
fundamental/KR evals
}
∪
{
𝐿
𝑖
,
𝑎
−
}
.
G
shift
	​

={fundamental/KR evals}∪{L
i,a
−
	​

}.

Ordinary Yangian
𝑂
𝑌
O
Y
	​

 should be recovered as a monoidal/localizing subquotient or by restriction from this shifted envelope.

This is the corrected generation theorem.

Conjecture C: every standard is a pro-Weyl limit of finite-dimensional pieces

Take a rational highest
ℓ
ℓ-weight
Ψ
Ψ, truncate it to finite data
Ψ
≤
𝑚
Ψ
≤m
, and let
𝑊
𝑚
:
=
𝑊
(
Ψ
≤
𝑚
)
W
m
	​

:=W(Ψ
≤m
) be the local Weyl module. Local Weyl modules are the universal finite-dimensional highest-weight approximants, and they are built from fundamental modules.

The real theorem should be:

𝑀
(
Ψ
)
≃
𝑅
 ⁣
l
i
m
←
⁡
𝑚
𝑊
𝑚
M(Ψ)≃R
m
lim
	​

	​

W
m
	​


inside a separated completion of
𝑂
O.

That is the only honest way the finite-dimensional evaluation core can generate infinite objects: not by finite thick closure inside ordinary
𝐷
𝑏
D
b
, but by derived completion of a pro-Weyl tower.

Conjecture D: DK/KL extends on compacts, then by completion

Francis–Gaitsgory show exactly where bar/cobar becomes an equivalence: not automatically, but in the pro-nilpotent setting; and they also prove the module-level bar/Chevalley functor is an equivalence for pro-nilpotent modules.

So the DK/KL move should be:

prove the equivalence on the compact shifted-prefundamental core;

identify the completed Yangian side as a pro-nilpotent module category built from pro-Weyl towers;

extend by compact generation / completion.

That is a coherent theorem. The old one is not.

5. How to actually attack it

The proof strategy should be surgical.

Step 1: pick the habitat where exact sequences can exist

Do not try to lift Baxter identities inside the whole ordinary category
𝑂
O first. The shifted category is where the control exists: Hernandez–Zhang give polynomial
𝑅
R-matrices, finite Jordan–Hölder behavior for tensor products in
𝑂
s
h
O
sh
	​

, and factorization through truncated shifted Yangians.

There is also strong external pressure in the neighboring quantum-loop world: Hernandez–Neguț’s 2026 paper says the whole ordinary category
𝑂
O has tensor products of simple modules that are not always of finite length, while shifted
𝑂
s
h
O
sh
	​

 is the more structured environment and the precise relation between the two is the real issue.

So the Baxter exact triangles should first be sought in the anti-dominant shifted envelope.

Step 2: construct the degenerating
𝑅
R-matrix and take its cone

This is where the blood really is.

Take a KR/evaluation object and a negative prefundamental/asymptotic object. The shifted theory gives a normalized polynomial
𝑅
R-matrix between suitable tensor products. At generic spectral parameter it is an isomorphism. At resonance it degenerates. The conjecture is that:

the image is one Baxter branch,

the cokernel is the other Baxter branch,

and no hidden junk survives because the q-character identity already leaves room for exactly two branches.

That is the categorical lift of Zhang’s
𝐾
0
K
0
	​

-formula. Hernandez–Zhang’s cyclic/cocyclic results and polynomial
𝑅
R-matrices are exactly the technology you need to make this precise.

A neighboring trigonometric sign that this is not fantasy: in late 2025, higher Dorey/T-system work for quantum affine algebras produced generalized T-systems of short exact sequences, not just decategorified identities. The Yangian Baxter triangles are the rational cousin of that story.

Step 3: do
𝑠
𝑙
2
sl
2
	​

 until it cracks

This is the first real target.

Zhang frames everything against the prototype

[
𝐶
2
]
[
𝑀
𝑥
]
=
[
𝑀
𝑥
+
1
]
+
[
𝑀
𝑥
−
1
]
[C
2
][M
x
	​

]=[M
x+1
	​

]+[M
x−1
	​

]

in BGG for
𝑠
𝑙
2
sl
2
	​

, and then proves Yangian analogues with asymptotic modules. Hernandez–Zhang then prove that in shifted
𝑠
𝑙
2
sl
2
	​

, every irreducible factors uniquely into prefundamental and KR modules.

So the first honest frontier theorem is:

In anti-dominant shifted
𝑌
(
𝑠
𝑙
2
)
Y(sl
2
	​

), the Baxter
𝐾
0
K
0
	​

-relation lifts to a short exact sequence or distinguished triangle.

Once you have that, you can bootstrap to longer products and then to type
𝐴
A by rank-one slices.

Step 4: turn local Weyl towers into completed standards

The pro-Weyl move is the bridge from finite to infinite. Each finite truncation sits in the evaluation-generated core. The missing theorem is not algebraic generation in a bounded derived category; it is separated recovery of a highest-
ℓ
ℓ-weight standard as a derived inverse limit. That is exactly the sort of move Francis–Gaitsgory’s pro-nilpotent formalism was built to tolerate.

If this step fails on the nose, the failure mode is informative: it will tell you whether the completion must be coderived, ind-completed,
𝑡
t-adically completed, or shifted-envelope completed.

6. What this does to the KL side

There is another hidden wound: you are probably asking for a braided monoidal structure too early.

Latyntsev proves that in factorization quantum groups, representation categories are controlled by spectral
𝑅
R-matrices, and a factorization braiding on
𝐴
A-FactMod is equivalent to the existence of a spectral
𝑅
R-matrix.

Then the 2025 dg-shifted Yangian line-operator paper goes even further: line operators are modeled by modules for a Koszul-dual
𝐴
∞
A
∞
	​

-algebra
𝐴
!
A
!
,
𝐴
!
A
!
 is conjecturally a dg-shifted Yangian with Maurer–Cartan element
𝑟
(
𝑧
)
r(z), associativity yields an
𝐴
∞
A
∞
	​

 Yang–Baxter equation, and the authors say flatly that there is no actual braiding in the category
𝐶
C.

So I would rewrite the KL side of MC3 as:

not “first produce a braided monoidal upgrade,”

but “first produce a periodic/CDG/
𝐴
∞
A
∞
	​

 factorization object with spectral
𝑟
(
𝑧
)
r(z)-data.”

That is the primitive structure. Braiding, if it exists, is a later shadow.

7. The two coherent ways forward

There are exactly two mathematically coherent futures now.

Future A: keep finite-dimensional evaluations, enlarge the world

Then MC3 becomes:

finite-dimensional core is already the evaluation core;

add asymptotic/prefundamental generators in the anti-dominant shifted envelope;

lift Baxter identities to exact triangles;

recover ordinary standards by pro-Weyl completion;

apply FG/Latyntsev to move to factorization.

This is the route I believe.

Future B: keep ordinary
𝐷
𝑏
(
𝑂
)
D
b
(O), enlarge “evaluation”

Redefine the generator family to include evaluation pullbacks of the full BGG category
𝑂
(
𝑔
)
O(g). Then the Baxter modules
𝑀
𝑘
,
𝑥
(
𝑖
)
M
k,x
(i)
	​

 are no longer alien; they become the natural bridge objects. The frontier theorem becomes:

𝐷
𝑏
(
𝑂
𝑌
)
=
?
thick
⁡
⟨
e
v
𝑎
∗
(
𝐷
𝑏
(
𝑂
(
𝑔
)
)
)
⟩
.
D
b
(O
Y
	​

)
=
?
thick⟨ev
a
∗
	​

(D
b
(O(g)))⟩.

That is also plausible, but it is a different theorem from the old finite-dimensional evaluation claim.

8. My hard recommendation

If you want the frontier pushed, not described, I would replace the old MC3 obstruction by these four new targets:

Baxter exact triangles in anti-dominant shifted
𝑂
O.

Compact generation of a completed shifted Yangian category by KR + negative prefundamentals.

Pro-Weyl recovery of ordinary highest-
ℓ
ℓ-weight standards.

Derived DK/KL on compacts, extended by pro-nilpotent completion.

And I would attack them in this order:

𝑠
𝑙
2
sl
2
	​

 Baxter exact sequence,

𝑠
𝑙
3
sl
3
	​

 exact triangle realizing Zhang’s displayed three-term identity,

pro-Weyl completion for one rational highest-
ℓ
ℓ-weight family,

compact-generation theorem,

then factorization/KL extension.

That is the live frontier.

The old sentence “is
𝐷
𝑏
(
𝑂
𝑌
ℏ
(
𝑠
𝑙
𝑁
)
)
D
b
(O
Y
ℏ
	​

(sl
N
	​

)
	​

) thickly generated by evaluation modules?” is no longer the frontier. It is the scar tissue around the real wound.

