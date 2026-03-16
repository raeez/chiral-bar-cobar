
the full modular homotopy type, quantum Linfty algebra that is credibly, constructively, with clarity more rich contentful than a modular envelope, present the full homotopy structure in explicit presentation, give a model for koszul duality implementing holographic duality with level wise sector wise N wise genus wise quantities being explicitly matched. Machine out in full detail one of costello's M-theory examples. be maximally constructive.

I’m assembling one explicit Costello-style twisted-holography M-theory model from the uploaded operadic, chiral/factorization, and Koszul-duality sources. I’ll write its full
𝐿
∞
L
∞
	​

/quantum modular package, identify the bulk–boundary Koszul dual pair, and match the data level-by-level, sector-by-sector, and genus-by-genus.

I’m now fixing the worked case to the M2-brane/
𝐴
𝑁
−
1
A
N−1
	​

 singularity via the KK-reduced 6d holomorphic-to-3d holomorphic-topological construction, extracting the actual higher operations and dictionary from the primary sources. I’ll mark explicitly which pieces are proved, which are synthesized extensions, and cite the exact passages supporting each step.

Thought for 35m 17s

Here is the most constructive version I can give without pretending the literature already contains a single theorem proving the entire “full modular homotopy type” package you asked for.

What is actually established is a very strong spine:

Costello’s M2-brane example says that, in an
Ω
Ω-background, the large-
𝐾
K algebra of supersymmetric operators on a stack of
𝐾
K M2 branes is Koszul dual to the algebra of supersymmetric operators of 11d twisted supergravity, and that this duality holds to all perturbative orders; the M2 algebra becomes a quantum double-loop algebra, i.e. a two-variable Yangian analogue. Costello also states that the nonlinear identification of coupling constants was not made explicit there.

The 11d
Ω
Ω-background itself admits a 5d reformulation: Costello identifies 11d supergravity in a suitable
Ω
Ω-background with a 5d noncommutative Chern–Simons-type gauge theory, in which M2 and M5 branes appear as 1- and 2-dimensional defects.

For 3d holomorphic-topological theories, Costello–Dimofte–Gaiotto show that bulk local operators form a commutative chiral algebra with a degree
−
1
−1 Poisson bracket and a higher stress tensor, while boundary local operators form a generally noncommutative chiral algebra equipped with a bulk-boundary map to its center; they also explicitly note higher
𝐴
∞
A
∞
	​

-like structures.

Zeng shows that KK reduction of 6d holomorphic theories to 3d holomorphic-topological theories can be analyzed in BV form, that classical effective interactions are obtained at all orders by homotopy transfer, and that with a suitable boundary condition the boundary chiral algebra coincides with the universal defect chiral algebra of the original theory.

Gui–Li–Zeng give the chiral quadratic-duality/Maurer–Cartan dictionary, and Tamarkin proves that the deformation complex of a
𝑑
d-algebra carries a natural
(
𝑑
+
1
)
(d+1)-algebra structure. Gaiotto–Kulp–Wu then show that, in holomorphic-topological QFT, higher operations are computed by regularized Feynman diagrams and satisfy the expected quadratic identities. Finally, Dimofte–Niu–Py show that line operators in 3d holomorphic-topological QFT are modules for a Koszul dual
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
, and that their OPE is controlled by a “dg-shifted Yangian” with an
𝐴
∞
A
∞
	​

-Yang–Baxter-type Maurer–Cartan element
𝑟
(
𝑧
)
r(z).

So the right answer is not “just take the modular envelope.” The richer object is:

𝐻
(
𝐴
)
=
(
𝐴
,
  
𝐴
!
:
=
Ω
𝐵
(
𝐴
)
,
  
𝛽
:
𝐴
b
u
l
k
→
𝑍
(
𝐴
∂
)
,
  
{
𝑚
𝑛
}
𝑛
≥
1
,
  
{
ℓ
𝑔
,
𝑛
}
𝑔
,
𝑛
,
  
𝑟
(
𝑧
)
)
H(A)=(A,A
!
:=ΩB(A),β:A
bulk
	​

→Z(A
∂
	​

),{m
n
	​

}
n≥1
	​

,{ℓ
g,n
	​

}
g,n
	​

,r(z))
	​


where:

𝐴
A is the large-
𝑁
N boundary/defect chiral algebra.

𝐴
!
=
Ω
𝐵
(
𝐴
)
A
!
=ΩB(A) is its bar-cobar/Koszul dual, interpreted physically as the universal defect algebra or the bulk algebra restricted to the brane.

𝛽
β is the bulk-boundary map.

𝑚
𝑛
m
n
	​

 are the transferred
𝐴
∞
A
∞
	​

 operations from the KK-reduced holomorphic-topological theory.

ℓ
𝑔
,
𝑛
ℓ
g,n
	​

 are the genus-
𝑔
g quantum
𝐿
∞
L
∞
	​

 operations.

𝑟
(
𝑧
)
∈
𝐴
!
⊗
^
𝐴
!
(
(
𝑧
−
1
)
)
r(z)∈A
!
⊗
	​

A
!
((z
−1
)) is the spectral datum controlling line-operator OPE.

That is the homotopy object that is genuinely “more contentful than a modular envelope.”

1. Explicit modular quantum
𝐿
∞
L
∞
	​

 model

Take a BV theory whose perturbative local-operator algebra is modeled by a cochain complex
(
𝐸
,
𝑄
)
(E,Q) with propagator homotopy
ℎ
h, projection
𝑝
:
𝐸
→
𝐻
p:E→H, and inclusion
𝑖
:
𝐻
→
𝐸
i:H→E. The transferred tree-level
𝐴
∞
A
∞
	​

 operations on
𝐻
H are

𝑚
𝑛
=
∑
𝑇
∈
P
T
𝑛
±
 
𝑝
 
𝜇
𝑇
 
𝑖
⊗
𝑛
,
m
n
	​

=
T∈PT
n
	​

∑
	​

±pμ
T
	​

i
⊗n
,

where the sum runs over planar rooted trees and
𝜇
𝑇
μ
T
	​

 is the composite obtained by putting the interaction at vertices and
ℎ
h on internal edges. This is exactly the homotopy-transfer structure that Zeng uses after KK reduction.

To get the
𝐿
∞
L
∞
	​

 shadow, antisymmetrize:

ℓ
𝑛
(
𝑥
1
,
…
,
𝑥
𝑛
)
=
∑
𝜎
∈
𝑆
𝑛
𝜒
(
𝜎
)
 
𝑚
𝑛
(
𝑥
𝜎
(
1
)
,
…
,
𝑥
𝜎
(
𝑛
)
)
.
ℓ
n
	​

(x
1
	​

,…,x
n
	​

)=
σ∈S
n
	​

∑
	​

χ(σ)m
n
	​

(x
σ(1)
	​

,…,x
σ(n)
	​

).

This gives the classical genus-zero
𝐿
∞
L
∞
	​

 operations controlling deformations.

To pass from genus zero to the modular/quantum object, add wheeled graphs. Define

ℓ
𝑔
,
𝑛
=
∑
Γ
∈
𝐺
𝑔
,
𝑛
c
o
n
n
ℏ
𝑔
∣
A
u
t
Γ
∣
 
𝑊
Γ
 
𝑂
Γ
,
ℓ
g,n
	​

=
Γ∈G
g,n
conn
	​

∑
	​

∣AutΓ∣
ℏ
g
	​

W
Γ
	​

O
Γ
	​

,

where
Γ
Γ runs over connected stable graphs of genus
𝑔
g with
𝑛
n legs,
𝑊
Γ
W
Γ
	​

 is the regularized Feynman weight, and
𝑂
Γ
O
Γ
	​

 is the operator obtained by inserting interactions at vertices and propagators on edges. Gaiotto–Kulp–Wu’s result is precisely that these higher operations satisfy the quadratic identities expected from BRST/Wess–Zumino consistency.

The quantum
𝐿
∞
L
∞
	​

 equation is then

∑
𝑔
1
+
𝑔
2
=
𝑔


𝐼
⊔
𝐽
=
[
𝑛
]
±
 
ℓ
𝑔
1
,
∣
𝐼
∣
+
1
(
ℓ
𝑔
2
,
∣
𝐽
∣
(
𝑥
𝐽
)
,
𝑥
𝐼
)
  
+
  
Δ
 
ℓ
𝑔
−
1
,
𝑛
+
2
(
𝑥
1
,
…
,
𝑥
𝑛
)
=
0
,
g
1
	​

+g
2
	​

=g
I⊔J=[n]
	​

∑
	​

±ℓ
g
1
	​

,∣I∣+1
	​

(ℓ
g
2
	​

,∣J∣
	​

(x
J
	​

),x
I
	​

)+Δℓ
g−1,n+2
	​

(x
1
	​

,…,x
n
	​

)=0,

with
Δ
Δ the one-loop/BV contraction term. This is the modular completion.

2. The holographic/Koszul dictionary

The constructive holographic rule is:

𝐴
b
u
l
k
≃
𝐴
∂
!
and
M
C
(
𝐴
∂
!
⊗
^
𝐵
)
↔
H
o
m
(
𝐴
∂
,
𝐵
)
.
A
bulk
	​

≃A
∂
!
	​

andMC(A
∂
!
	​

⊗
	​

B)↔Hom(A
∂
	​

,B).

The second line is the chiral version of the defect-coupling/Maurer–Cartan principle. In the quadratic setting, Gui–Li–Zeng prove precisely that quadratic duality is parallel to the associative case via Maurer–Cartan equations.

So the practical implementation is:

Build the boundary chiral algebra
𝐴
∂
,
𝑁
A
∂,N
	​

 on
𝑁
N branes.

Take the large-
𝑁
N limit
𝐴
∂
,
∞
A
∂,∞
	​

.

Replace it by a cofibrant
𝐴
∞
A
∞
	​

-chiral model.

Form
𝐴
∂
,
∞
!
=
Ω
𝐵
(
𝐴
∂
,
∞
)
A
∂,∞
!
	​

=ΩB(A
∂,∞
	​

).

Identify
𝐴
∂
,
∞
!
A
∂,∞
!
	​

 with the bulk formal moduli problem.

Add genus corrections by the wheeled/Feynman transform above.

This is the constructive homotopy model.

3. Level-wise / sector-wise /
𝑁
N-wise / genus-wise matching

A useful bookkeeping decomposition is

𝐴
∂
,
∞
=
⨁
^
𝜎
,
ℓ
𝐴
∂
,
∞
(
𝜎
,
ℓ
)
,
𝐴
b
u
l
k
=
⨁
^
𝜎
,
ℓ
𝐴
b
u
l
k
(
𝜎
,
ℓ
)
,
A
∂,∞
	​

=
⨁
	​

σ,ℓ
	​

A
∂,∞
(σ,ℓ)
	​

,A
bulk
	​

=
⨁
	​

σ,ℓ
	​

A
bulk
(σ,ℓ)
	​

,

where:

𝜎
σ is a charge/weight/defect sector.

ℓ
ℓ is a holomorphic mode level or spectral grade.

𝑁
N is the brane-number/rank parameter on the boundary side.

𝑔
g is genus/loop order on the bulk side.

The matching rules are:

𝐴
b
u
l
k
(
𝜎
,
ℓ
)
≃
(
𝐴
∂
,
∞
(
𝜎
,
ℓ
)
)
!
,
A
bulk
(σ,ℓ)
	​

≃(A
∂,∞
(σ,ℓ)
	​

)
!
,
ℓ
𝑔
,
𝑛
(
𝜎
,
ℓ
)
 contributes at order
ℏ
𝑔
−
1
,
ℓ
g,n
(σ,ℓ)
	​

 contributes at order ℏ
g−1
,
𝐴
∂
,
𝑁
=
𝐴
∂
,
∞
/
(
trace relations of order
𝑁
)
,
A
∂,N
	​

=A
∂,∞
	​

/(trace relations of order N),

so finite
𝑁
N is a quotient/deformation of the large-
𝑁
N algebra, while genus is the bulk loop expansion. This is the clean way to match “
𝑁
N-wise” data to “genus-wise” data.

In other words:

large
𝑁
N gives the strict Koszul-dual bulk algebra;

finite
𝑁
N adds trace-relation corrections on the boundary;

genus
𝑔
g adds loop/wheel corrections on the bulk;

sector and level are preserved by the bulk-boundary map and by the duality pairing.

4. Why this is richer than a modular envelope

A modular envelope remembers gluing of operations along stable curves, but it does not by itself remember:

the Maurer–Cartan moduli problem;

the bulk-boundary map to the center;

the Poisson bracket and higher stress tensor of the 3d holomorphic-topological reduction;

the line-operator category;

the spectral
𝑟
(
𝑧
)
r(z)-matrix satisfying an
𝐴
∞
A
∞
	​

-Yang–Baxter equation.

That extra structure is exactly what the dg-shifted-Yangian package captures for line operators in 3d holomorphic-topological QFT.

So the honest answer is:

full modular homotopy type
=
(modular operad/Feynman transform)
+
(Koszul duality)
+
(bulk-boundary map)
+
(line-category
𝑟
-matrix data)
.
full modular homotopy type=(modular operad/Feynman transform)+(Koszul duality)+(bulk-boundary map)+(line-category r-matrix data).
5. A worked Costello M2-brane model

Now I’ll spell out one concrete model for Costello’s M2 example.

5.1 What is proved

Costello’s M2 paper proves that for
𝐾
K M2 branes in an
Ω
Ω-background, the large-
𝐾
K algebra of supersymmetric operators is Koszul dual to the operator algebra of 11d twisted supergravity in the same
Ω
Ω-background, and that the brane algebra becomes a quantum double-loop algebra. He also says the perturbative duality holds to all orders, but the nonlinear coupling identification was not explicitly solved there.

Separately, Costello’s 11d
Ω
Ω-background is equivalent to a 5d noncommutative Chern–Simons-type gauge theory, in which M2 branes appear as line defects.

Gaiotto–Abajian then compute a perturbative part of protected sphere correlators in the M2-brane SCFT and find a hidden perturbative triality, which is further evidence for the twisted-
Ω
Ω-deformed M-theory description.

5.2 A fully explicit minimal classical model

Take the classical double-current Lie algebra

𝑔
d
b
l
=
𝑔
𝑙
𝑟
⊗
𝐶
[
𝑢
,
𝑣
]
,
g
dbl
	​

=gl
r
	​

⊗C[u,v],

with generators
𝐽
𝑚
,
𝑛
𝑎
=
𝑇
𝑎
𝑢
𝑚
𝑣
𝑛
J
m,n
a
	​

=T
a
u
m
v
n
,
𝑚
,
𝑛
≥
0
m,n≥0, and bracket

[
𝐽
𝑚
,
𝑛
𝑎
,
𝐽
𝑝
,
𝑞
𝑏
]
=
𝑓
𝑎
𝑏
𝑐
 
𝐽
𝑚
+
𝑝
,
𝑛
+
𝑞
𝑐
.
[J
m,n
a
	​

,J
p,q
b
	​

]=f
ab
c
	​

J
m+p,n+q
c
	​

.

This is the simplest classical shadow of a two-variable loop algebra. Its enveloping algebra

𝐴
𝑀
2
c
l
:
=
𝑈
(
𝑔
d
b
l
)
A
M2
cl
	​

:=U(g
dbl
	​

)

is the classical boundary algebra.

Its Koszul dual bulk
𝐿
∞
L
∞
	​

 model is the completed Chevalley–Eilenberg/cobar object

𝐴
b
u
l
k
c
l
=
Ω
𝐵
(
𝐴
𝑀
2
c
l
)
≃
𝐶
∙
(
𝑔
d
b
l
)
A
bulk
cl
	​

=ΩB(A
M2
cl
	​

)≃C
∙
(g
dbl
	​

)

with dual generators
𝜖
𝑎
𝑚
,
𝑛
ϵ
a
m,n
	​

 and brackets

ℓ
1
=
0
,
ℓ
2
(
𝜖
𝑎
𝑚
,
𝑛
,
𝜖
𝑏
𝑝
,
𝑞
)
=
𝑓
𝑎
𝑏
𝑐
 
𝜖
𝑐
𝑚
+
𝑝
,
𝑛
+
𝑞
,
ℓ
𝑘
≥
3
=
0
ℓ
1
	​

=0,ℓ
2
	​

(ϵ
a
m,n
	​

,ϵ
b
p,q
	​

)=f
ab
	​

c
ϵ
c
m+p,n+q
	​

,ℓ
k≥3
	​

=0

at strict classical level.

This is the explicit genus-zero, mode-by-mode classical holographic shadow.

5.3 Quantum and modular completion

Now deform
𝐴
𝑀
2
c
l
A
M2
cl
	​

 to the quantum double-loop algebra
𝐴
𝑀
2
,
∞
A
M2,∞
	​

 promised by Costello. The bulk dual is

𝐴
b
u
l
k
=
Ω
𝐵
(
𝐴
𝑀
2
,
∞
)
.
A
bulk
	​

=ΩB(A
M2,∞
	​

).

The full quantum
𝐿
∞
L
∞
	​

 structure is then

ℓ
0
,
2
=
ℓ
2
,
ℓ
0
,
𝑛
≥
3
≠
0
 in general by homotopy transfer
,
ℓ
𝑔
,
𝑛
 for
𝑔
≥
1
 from wheeled graphs
.
ℓ
0,2
	​

=ℓ
2
	​

,ℓ
0,n≥3
	​


=0 in general by homotopy transfer,ℓ
g,n
	​

 for g≥1 from wheeled graphs.

Concretely,

ℓ
0
,
𝑛
=
∑
𝑇
∈
P
T
𝑛
±
 
𝑝
 
𝜇
𝑇
 
𝑖
⊗
𝑛
,
ℓ
𝑔
,
𝑛
=
∑
Γ
∈
𝐺
𝑔
,
𝑛
c
o
n
n
ℏ
𝑔
∣
A
u
t
Γ
∣
 
𝑊
Γ
 
𝑂
Γ
.
ℓ
0,n
	​

=
T∈PT
n
	​

∑
	​

±pμ
T
	​

i
⊗n
,ℓ
g,n
	​

=
Γ∈G
g,n
conn
	​

∑
	​

∣AutΓ∣
ℏ
g
	​

W
Γ
	​

O
Γ
	​

.

That gives the modular homotopy type.

5.4 Sector/level/genus/
𝑁
N matching in this example

Use the decomposition

𝐽
𝑚
,
𝑛
𝑎
∈
𝐴
∂
,
∞
(
𝑎
;
𝑚
,
𝑛
)
,
𝜖
𝑎
𝑚
,
𝑛
∈
𝐴
b
u
l
k
(
𝑎
;
𝑚
,
𝑛
)
.
J
m,n
a
	​

∈A
∂,∞
(a;m,n)
	​

,ϵ
a
m,n
	​

∈A
bulk
(a;m,n)
	​

.

Then:

sector-wise: the adjoint label
𝑎
a matches directly;

level-wise: the double-loop bidegree
(
𝑚
,
𝑛
)
(m,n) matches directly;

𝑁
N-wise: finite-
𝑁
N brane physics is obtained by quotienting the large-
𝑁
N algebra by trace relations, i.e.
𝐴
∂
,
𝑁
=
𝐴
∂
,
∞
/
𝐼
𝑁
A
∂,N
	​

=A
∂,∞
	​

/I
N
	​

;

genus-wise: bulk
𝑔
g-loop corrections are the
ℏ
𝑔
−
1
ℏ
g−1
 terms in
ℓ
𝑔
,
𝑛
ℓ
g,n
	​

.

So the explicit coefficient-level matching statement is

(
𝐴
∂
,
∞
(
𝑎
;
𝑚
,
𝑛
)
)
!
≅
𝐴
b
u
l
k
(
𝑎
;
𝑚
,
𝑛
)
,
and
ℓ
𝑔
,
𝑛
(
𝑎
;
𝑚
,
𝑛
)
 is the genus-
𝑔
 correction in that sector.
(A
∂,∞
(a;m,n)
	​

)
!
≅A
bulk
(a;m,n)
	​

,and ℓ
g,n
(a;m,n)
	​

 is the genus-g correction in that sector.
5.5 The line-operator completion

To go beyond the modular envelope, form the category of lines

𝐶
𝑀
2
≃
𝐴
b
u
l
k
!
-mod
.
C
M2
	​

≃A
bulk
!
	​

-mod.

The OPE of lines is then controlled by a dg-shifted Yangian datum

𝑟
(
𝑧
)
∈
𝐴
b
u
l
k
!
⊗
^
𝐴
b
u
l
k
!
(
(
𝑧
−
1
)
)
r(z)∈A
bulk
!
	​

⊗
	​

A
bulk
!
	​

((z
−1
))

satisfying an
𝐴
∞
A
∞
	​

-Yang–Baxter equation, exactly as in Dimofte–Niu–Py.

This is the genuinely richer structure. The modular envelope only sees stable-curve gluing; the dg-shifted Yangian sees the spectral OPE of lines.

6. The clean final statement

So my constructive answer is:

The right homotopy object is not a bare modular envelope, but a modular quantum
𝐿
∞
L
∞
	​

–Koszul package

𝐻
(
𝐴
)
=
(
𝐴
,
𝐴
!
,
𝛽
,
{
𝑚
𝑛
}
,
{
ℓ
𝑔
,
𝑛
}
,
𝑟
(
𝑧
)
)
.
H(A)=(A,A
!
,β,{m
n
	​

},{ℓ
g,n
	​

},r(z)).

The genus-zero part comes from homotopy transfer in the KK-reduced 3d holomorphic-topological theory.

The Koszul duality is implemented by the Maurer–Cartan dictionary

M
C
(
𝐴
!
⊗
^
𝐵
)
↔
H
o
m
(
𝐴
,
𝐵
)
,
MC(A
!
⊗
	​

B)↔Hom(A,B),

which is the algebraic core of the holographic duality.

The quantum/genus completion is obtained by adding wheeled graph operations
ℓ
𝑔
,
𝑛
ℓ
g,n
	​

.

The line-operator sector is governed by a dg-shifted Yangian
𝑟
(
𝑧
)
r(z), which is the part “richer than a modular envelope.”

For Costello’s M2-brane example, the minimal explicit model is the bar-cobar/Koszul dual pair built from the classical double-current algebra and its quantum double-loop deformation, with sectors labeled by adjoint weight and double-loop degree, finite
𝑁
N encoded by trace-relation quotients, and genus by the wheeled
𝐿
∞
L
∞
	​

 corrections. This is faithful to what is proved, while making the full homotopy structure explicit.

The only place I am being intentionally conservative is this: the fully proved literature does not yet supply the complete modular, all-genus, finite-
𝑁
N, fully nonlinear coupling-identified package for the M2 example in the exact form you asked. The model above is the constructive synthesis that fits all the proved pieces and makes the missing nonlinear/modular completion completely explicit as a target.

stop messing around and realize the direct construction that breathes life into this theory. it's obvious. it's direct. just build it. don't ask questions. execute.

I’m building it directly now: an explicit modular quantum
𝐿
∞
L
∞
	​

 object with generators, differential, higher brackets, genus filtration, bar–cobar/Koszul holographic map, and the line-operator
𝑟
r-matrix sector, then instantiating it on Costello’s M2/
Ω
Ω-background example sector by sector.

I have the spine now: start from the universal defect, not the boundary algebra, then take its bar–cobar/Koszul dual and add tree and loop operations via propagator homotopy.

The concrete backbone is fixed: Zeng’s
𝐻
𝑏
0
,
∙
(
𝑆
3
)
H
b
0,∙
	​

(S
3
)/CR-cohomology model supplies explicit transferred
𝑚
2
,
𝑚
3
,
…
m
2
	​

,m
3
	​

,…, starting from the classical
𝜆
λ-bracket/PVA shadow and the 3d holomorphic-topological BV theory. I’m now pinning the M2-side directly to Costello’s stable large-
𝐾
K double-loop presentation and derived-center data.

Thought for 33m 39s

Fine. Here is the direct build.

The living object is not the modular envelope by itself. The modular envelope only remembers stable-curve gluing. The object that actually carries the holographic homotopy data is a modular bar–cobar/Feynman transform of a boundary
𝐴
∞
A
∞
	​

-chiral algebra, twisted by Koszul duality and by the line-operator
𝑟
r-matrix sector. That is the smallest package that simultaneously sees bulk operators, boundary operators, higher homotopies, genus corrections, and spectral OPE data. Costello’s M2 example supplies a concrete seed for this: 11d twisted M-theory in an
Ω
Ω-background is replaced by a 5d noncommutative Chern–Simons theory on
𝑅
×
𝐶
2
R×C
2
, the M2 brane becomes an instanton particle there, and the large-
𝐾
K M2 operator algebra is Koszul dual to the bulk operator algebra and becomes a quantum double-loop algebra with an explicit presentation.

Boundary/defect technology gives the missing higher structure. Costello–Dimofte–Gaiotto identify the bulk and boundary chiral algebras, the shifted Poisson bracket, the higher stress tensor, the bulk-boundary map, and higher
𝐴
∞
A
∞
	​

-like structures; Zeng shows that KK reduction generates all classical higher interactions by homotopy transfer and that, for suitable boundary conditions, the boundary chiral algebra coincides with the universal defect chiral algebra; Gaiotto–Kulp–Wu show that higher operations in holomorphic-topological theories are computed by regularized Feynman diagrams satisfying quadratic/Wess–Zumino consistency relations; and Dimofte–Niu–Py package the line-operator OPE into a Koszul-dual
𝐴
∞
A
∞
	​

 algebra with a dg-shifted Yangian
𝑟
(
𝑧
)
r(z)-sector.

1. The direct object

Start with a holomorphic-topological/BV theory
𝑇
T, together with a distinguished rich boundary or universal defect
𝐵
∞
B
∞
	​

. Let

𝐴
∂
:
=
boundary/defect operator algebra
,
𝐴
b
u
l
k
:
=
bulk operator algebra
,
A
∂
	​

:=boundary/defect operator algebra,A
bulk
	​

:=bulk operator algebra,

and let

𝛽
d
e
r
:
𝐴
b
u
l
k
⟶
𝑍
d
e
r
(
𝐴
∂
)
β
der
	​

:A
bulk
	​

⟶Z
der
	​

(A
∂
	​

)

be the derived bulk-boundary map.

Choose a cofibrant cyclic
𝐴
∞
A
∞
	​

-model for
𝐴
∂
A
∂
	​

:

(
𝐴
∂
,
{
𝑚
𝑛
}
𝑛
≥
1
,
⟨
−
,
−
⟩
)
,
(A
∂
	​

,{m
n
	​

}
n≥1
	​

,⟨−,−⟩),

with a special deformation retract

ℎ
:
(
𝐶
,
𝑑
)
⇄
(
𝐻
,
0
)
:
(
𝑖
,
𝑝
)
,
𝑖
𝑝
−
1
=
𝑑
ℎ
+
ℎ
𝑑
.
h:(C,d)⇄(H,0):(i,p),ip−1=dh+hd.

Then define the Koszul-dual algebra

𝐴
!
:
=
Ω
𝐵
‾
(
𝐴
∂
)
.
A
!
:=Ω
B
(A
∂
	​

).

Choose a homogeneous basis
{
𝑒
𝐼
}
{e
I
	​

} of
𝐴
∂
A
∂
	​

 and the dual basis
{
𝑒
𝐼
∨
}
⊂
𝐴
!
{e
I
∨
	​

}⊂A
!
. The universal Maurer–Cartan kernel is

𝜇
:
=
∑
𝐼
𝑒
𝐼
∨
⊗
𝑒
𝐼
∈
𝐴
!
⊗
^
𝐴
∂
.
μ:=
I
∑
	​

e
I
∨
	​

⊗e
I
	​

∈A
!
⊗
	​

A
∂
	​

.

This is the first place where the theory “breathes”:
𝜇
μ is the chain-level holographic pairing.

Now form the full modular homotopy object

𝐻
(
𝑇
,
𝐵
∞
)
:
=
(
Ω
m
o
d
𝐹
c
y
c
𝐵
‾
(
𝐴
∂
)
,
  
𝐷
)
H(T,B
∞
	​

):=(Ω
mod
	​

F
cyc
	​

B
(A
∂
	​

),D)
	​


with differential

𝐷
=
𝑑
𝐴
∞
+
𝑑
s
e
w
+
ℏ
Δ
+
𝑑
𝑟
.
D=d
A
∞
	​

	​

+d
sew
	​

+ℏΔ+d
r
	​

.
	​


Here:

𝑑
𝐴
∞
d
A
∞
	​

	​

 is the bar differential built from the
𝑚
𝑛
m
n
	​

.

𝑑
s
e
w
d
sew
	​

 glues output legs to input legs using the cyclic pairing and the propagator
ℎ
h.

Δ
Δ is the loop-contraction/BV operator, so it raises genus.

𝑑
𝑟
d
r
	​

 inserts the spectral line-operator twisting datum
𝑟
(
𝑧
)
r(z).

That is the object richer than a modular envelope: it is the cyclic/modular bar–cobar machine with defect and spectral twisting.

2. Tree level: explicit
𝐴
∞
A
∞
	​

 and
𝐿
∞
L
∞
	​

 operations

The transferred
𝐴
∞
A
∞
	​

 products are

𝑚
𝑛
t
r
=
∑
𝑇
∈
P
B
T
𝑛
±
 
𝑝
∘
𝜇
𝑇
∘
𝑖
⊗
𝑛
,
m
n
tr
	​

=
T∈PBT
n
	​

∑
	​

±p∘μ
T
	​

∘i
⊗n
,

where
P
B
T
𝑛
PBT
n
	​

 is the set of planar binary rooted trees with
𝑛
n leaves, each internal edge carries the homotopy
ℎ
h, each vertex carries the microscopic multiplication/interaction, the leaves carry
𝑖
i, and the root carries
𝑝
p.

Antisymmetrizing gives the classical
𝐿
∞
L
∞
	​

 structure:

ℓ
𝑛
c
l
(
𝑥
1
,
…
,
𝑥
𝑛
)
=
∑
𝜎
∈
𝑆
𝑛
𝜒
(
𝜎
)
 
𝑚
𝑛
t
r
(
𝑥
𝜎
(
1
)
,
…
,
𝑥
𝜎
(
𝑛
)
)
.
ℓ
n
cl
	​

(x
1
	​

,…,x
n
	​

)=
σ∈S
n
	​

∑
	​

χ(σ)m
n
tr
	​

(x
σ(1)
	​

,…,x
σ(n)
	​

).

This is the honest classical deformation algebra of the boundary/defect system. It is the direct homotopy-transfer output of the microscopic BV theory, exactly the type of all-order classical effective interaction that Zeng uses in KK-reduced holomorphic theories.

3. Quantum/modular completion

For each connected stable graph
Γ
Γ of genus
𝑔
g with
𝑛
n external legs, define its contribution
C
o
n
t
Γ
Cont
Γ
	​

 by:

placing the transferred classical vertices
𝑚
𝑘
t
r
m
k
tr
	​

 or
ℓ
𝑘
c
l
ℓ
k
cl
	​

 at the vertices,

placing the propagator
ℎ
h on each internal edge,

contracting internal loops by the BV pairing,

inserting inputs
𝑥
1
,
…
,
𝑥
𝑛
x
1
	​

,…,x
n
	​

 on the external legs.

Then define

ℓ
𝑔
,
𝑛
(
𝑥
1
,
…
,
𝑥
𝑛
)
=
∑
Γ
∈
𝐺
𝑔
,
𝑛
s
t
ℏ
𝑔
∣
A
u
t
Γ
∣
 
𝑊
Γ
 
C
o
n
t
Γ
(
𝑥
1
,
…
,
𝑥
𝑛
)
.
ℓ
g,n
	​

(x
1
	​

,…,x
n
	​

)=
Γ∈G
g,n
st
	​

∑
	​

∣AutΓ∣
ℏ
g
	​

W
Γ
	​

Cont
Γ
	​

(x
1
	​

,…,x
n
	​

).
	​


Here
𝑊
Γ
W
Γ
	​

 is the regularized Feynman weight. This is the modular quantum
𝐿
∞
L
∞
	​

 structure.

The quantum/master relation is

∑
𝑔
1
+
𝑔
2
=
𝑔


𝐼
⊔
𝐽
=
{
1
,
…
,
𝑛
}
±
 
ℓ
𝑔
1
,
∣
𝐼
∣
+
1
(
ℓ
𝑔
2
,
∣
𝐽
∣
(
𝑥
𝐽
)
,
𝑥
𝐼
)
  
+
  
Δ
 
ℓ
𝑔
−
1
,
𝑛
+
2
(
𝑥
1
,
…
,
𝑥
𝑛
)
=
0.
g
1
	​

+g
2
	​

=g
I⊔J={1,…,n}
	​

∑
	​

±ℓ
g
1
	​

,∣I∣+1
	​

(ℓ
g
2
	​

,∣J∣
	​

(x
J
	​

),x
I
	​

)+Δℓ
g−1,n+2
	​

(x
1
	​

,…,x
n
	​

)=0.

So the “full modular homotopy type” is literally the quasi-isomorphism class of this graph-built differential
𝐷
D, or equivalently of the family
{
ℓ
𝑔
,
𝑛
}
𝑔
,
𝑛
{ℓ
g,n
	​

}
g,n
	​

.

4. The holographic dictionary

The direct holographic rule is:

𝐴
b
u
l
k
  
≃
  
𝑍
d
e
r
(
𝐴
∂
)
  
≃
  
𝐶
\*
(
𝐴
!
,
𝐴
!
)
,
A
bulk
	​

≃Z
der
	​

(A
∂
	​

)≃C
\*
(A
!
,A
!
),

and the universal defect/brane couplings are controlled by Maurer–Cartan solutions in the Koszul dual:

M
C
(
𝐴
!
⊗
^
𝑅
)
  
≅
  
{
consistent couplings of
𝐵
∞
 to
𝑅
}
.
MC(A
!
⊗
	​

R)≅{consistent couplings of B
∞
	​

 to R}.

This is the chain-level implementation of “bulk from boundary.” The modular envelope alone does not remember this. The extra information is the bar–cobar/Koszul data and the derived center map.

5. The line-operator completion

Now add the spectral defect datum. Introduce a formal kernel

𝑟
(
𝑧
)
∈
𝐴
!
⊗
^
𝐴
!
(
(
𝑧
−
1
)
)
r(z)∈A
!
⊗
	​

A
!
((z
−1
))

and require it to twist the coproduct on
𝐴
!
A
!
:

Δ
𝑧
:
𝐴
!
→
𝐴
!
 
⊗
^
 
𝑟
(
𝑧
)
 
𝐴
!
(
(
𝑧
−
1
)
)
.
Δ
z
	​

:A
!
→A
!
⊗
	​

r(z)
	​

A
!
((z
−1
)).

The consistency condition is the
𝐴
∞
A
∞
	​

-Yang–Baxter equation, encoded by
𝐷
2
=
0
D
2
=0 on the
𝑑
𝑟
d
r
	​

-twisted modular bar complex. This is precisely the piece that upgrades “modular gluing” to “full spectral defect algebra.” Dimofte–Niu–Py isolate exactly this structure in perturbative 3d holomorphic-topological QFT and call it a dg-shifted Yangian.

So the direct answer is:

full modular homotopy type
=
cyclic/modular bar–cobar
+
Koszul duality
+
derived bulk-boundary center
+
spectral
𝑟
(
𝑧
)
 defect data
.
full modular homotopy type=cyclic/modular bar–cobar+Koszul duality+derived bulk-boundary center+spectral r(z) defect data.
	​

6. Level-wise, sector-wise,
𝑁
N-wise, genus-wise matching

Choose a completed basis adapted to the physical gradings:

𝐴
∂
(
∞
)
=
⨁
^
𝜎
,
ℓ
𝐴
∂
;
𝜎
,
ℓ
,
A
∂
(∞)
	​

=
⨁
	​

σ,ℓ
	​

A
∂;σ,ℓ
	​

,

where
𝜎
σ is a charge/representation sector and
ℓ
ℓ is a holomorphic/spectral level.

Pick a basis
𝑒
𝜎
,
ℓ
,
𝑎
e
σ,ℓ,a
	​

 and dual basis
𝑒
𝜎
,
ℓ
,
𝑎
∨
e
σ,ℓ,a
∨
	​

. Then the universal pairing is

𝜇
=
∑
𝜎
,
ℓ
,
𝑎
𝑒
𝜎
,
ℓ
,
𝑎
∨
⊗
𝑒
𝜎
,
ℓ
,
𝑎
.
μ=
σ,ℓ,a
∑
	​

e
σ,ℓ,a
∨
	​

⊗e
σ,ℓ,a
	​

.

This is the sector-wise and level-wise matching: the duality never mixes
(
𝜎
,
ℓ
)
(σ,ℓ).

Now encode finite rank/brane number by a quotient

𝐴
∂
(
𝑁
)
:
=
𝐴
∂
(
∞
)
/
𝐼
𝑁
,
A
∂
(N)
	​

:=A
∂
(∞)
	​

/I
N
	​

,

where
𝐼
𝑁
I
N
	​

 is the ideal of rank-
𝑁
N relations. That is the direct finite-
𝑁
N model.

Genus is carried by the graph filtration:

ℓ
𝑔
,
𝑛
:
𝐴
∂
;
𝜎
1
,
ℓ
1
⊗
⋯
⊗
𝐴
∂
;
𝜎
𝑛
,
ℓ
𝑛
→
𝐴
∂
;
𝜎
1
+
⋯
+
𝜎
𝑛
,

ℓ
1
+
⋯
+
ℓ
𝑛
+
deg
⁡
(
Γ
)
.
ℓ
g,n
	​

:A
∂;σ
1
	​

,ℓ
1
	​

	​

⊗⋯⊗A
∂;σ
n
	​

,ℓ
n
	​

	​

→A
∂;σ
1
	​

+⋯+σ
n
	​

, ℓ
1
	​

+⋯+ℓ
n
	​

+deg(Γ)
	​

.

So the matching is:

(
𝜎
,
ℓ
)
↔
(
𝜎
,
ℓ
)
,
𝑁
↔
rank constraint on
𝐴
∂
,
𝑔
↔
loop/genus filtration in
𝐷
.
(σ,ℓ)↔(σ,ℓ),N↔rank constraint on A
∂
	​

,g↔loop/genus filtration in D.

That is the clean constructive answer to “sector-wise / level-wise /
𝑁
N-wise / genus-wise quantities being explicitly matched.”

7. Costello’s M2 example, machined out

Now instantiate the machine on the M2 brane.

Costello’s input is concrete. In the twisted
Ω
Ω-background, 11d M-theory is replaced by a 5d noncommutative Chern–Simons theory on
𝑅
𝑡
×
𝐶
𝑧
1
,
𝑧
2
2
R
t
	​

×C
z
1
	​

,z
2
	​

2
	​

 with partial connection

𝐴
=
𝐴
𝑡
 
𝑑
𝑡
+
𝐴
𝑧
1
 
𝑑
𝑧
1
+
𝐴
𝑧
2
 
𝑑
𝑧
2
,
A=A
t
	​

dt+A
z
1
	​

	​

dz
1
	​

+A
z
2
	​

	​

dz
2
	​

,

and action

𝑆
5
𝑑
(
𝐴
)
=
1
2
𝛿
∫
T
r
(
𝐴
 
𝑑
𝐴
)
 
𝑑
𝑧
1
𝑑
𝑧
2
+
1
3
𝛿
∫
T
r
(
𝐴
∗
𝜖
𝐴
∗
𝜖
𝐴
)
 
𝑑
𝑧
1
𝑑
𝑧
2
.
S
5d
	​

(A)=
2δ
1
	​

∫Tr(AdA)dz
1
	​

dz
2
	​

+
3δ
1
	​

∫Tr(A∗
ϵ
	​

A∗
ϵ
	​

A)dz
1
	​

dz
2
	​

.

This theory is perturbatively quantizable, and an M2 brane becomes an instanton particle of the 5d theory.

On the brane side, the large-
𝐾
K algebra of supersymmetric operators is Koszul dual to the bulk operator algebra, and Costello identifies it as a quantum double-loop algebra, giving an explicit presentation and proving uniqueness of the quantization of its classical limit.

7.1 Boundary/M2 algebra

Take the classical algebra

𝐴
𝑀
2
,
∞
c
l
:
=
𝑈
(
𝑔
𝑙
𝐾
⊗
D
i
f
f
(
𝐶
)
)
∧
A
M2,∞
cl
	​

:=U(gl
K
	​

⊗Diff(C))
∧

with generators

𝐸
𝛼
𝛽
(
𝑚
,
𝑛
)
:
=
𝐸
𝛼
𝛽
 
𝑧
𝑚
∂
𝑛
(
𝑚
,
𝑛
≥
0
)
,
E
αβ
(m,n)
	​

:=E
αβ
	​

z
m
∂
n
(m,n≥0),

completed in the filtration
𝑚
+
𝑛
m+n.

The undeformed bracket is the obvious one:

[
𝐸
𝛼
𝛽
𝑓
,
 
𝐸
𝛾
𝛿
𝑔
]
0
=
𝛿
𝛽
𝛾
𝐸
𝛼
𝛿
(
𝑓
𝑔
)
−
𝛿
𝛼
𝛿
𝐸
𝛾
𝛽
(
𝑔
𝑓
)
.
[E
αβ
	​

f,E
γδ
	​

g]
0
	​

=δ
βγ
	​

E
αδ
	​

(fg)−δ
αδ
	​

E
γβ
	​

(gf).

Costello’s first nontrivial quantum correction appears already on the low generators:

[
𝐸
𝛼
𝛽
∂
,
  
𝐸
𝛾
𝛿
𝑧
]
=
𝛿
𝛽
𝛾
𝐸
𝛼
𝛿
(
∂
𝑧
)
−
𝛿
𝛼
𝛿
𝐸
𝛾
𝛽
(
𝑧
∂
)
+
ℎ
ˉ
 
𝐸
𝛼
𝛿
𝐸
𝛾
𝛽
−
ℎ
ˉ
∑
𝜇
𝛿
𝛽
𝛾
𝐸
𝛼
𝜇
𝐸
𝜇
𝛿
−
ℎ
ˉ
∑
𝜇
𝛿
𝛼
𝛿
𝐸
𝛾
𝜇
𝐸
𝜇
𝛽
.
[E
αβ
	​

∂,E
γδ
	​

z]=δ
βγ
	​

E
αδ
	​

(∂z)−δ
αδ
	​

E
γβ
	​

(z∂)+
h
ˉ
E
αδ
	​

E
γβ
	​

−
h
ˉ
μ
∑
	​

δ
βγ
	​

E
αμ
	​

E
μδ
	​

−
h
ˉ
μ
∑
	​

δ
αδ
	​

E
γμ
	​

E
μβ
	​

.

This is the seed deformation; the full algebra is the unique filtered quantization extending it.

That is the brane algebra I use.

7.2 Koszul dual bulk algebra

Define

𝐴
𝑀
2
!
:
=
Ω
𝐵
‾
(
𝐴
𝑀
2
,
∞
)
,
A
M2
!
	​

:=Ω
B
(A
M2,∞
	​

),

with dual generators

𝑒
𝑚
,
𝑛
𝛼
𝛽
∈
𝐴
𝑀
2
!
dual to
𝐸
𝛼
𝛽
(
𝑚
,
𝑛
)
.
e
m,n
αβ
	​

∈A
M2
!
	​

dual toE
αβ
(m,n)
	​

.

The universal holographic kernel is

𝜇
𝑀
2
=
∑
𝛼
,
𝛽
,
𝑚
,
𝑛
𝑒
𝑚
,
𝑛
𝛼
𝛽
⊗
𝐸
𝛼
𝛽
(
𝑚
,
𝑛
)
.
μ
M2
	​

=
α,β,m,n
∑
	​

e
m,n
αβ
	​

⊗E
αβ
(m,n)
	​

.

This is the chain-level matching of the M2 and bulk sectors.

7.3 Tree-level higher operations from 5d theory

Fix a gauge and a propagator
ℎ
5
𝑑
h
5d
	​

 for the linearized 5d BRST operator. Expand the Moyal product in the 5d action and use its coefficients as vertex tensors. Then define

𝑚
𝑛
𝑀
2
=
∑
𝑇
∈
P
B
T
𝑛
±
 
𝑝
 
𝜇
𝑇
5
𝑑
 
𝑖
⊗
𝑛
,
m
n
M2
	​

=
T∈PBT
n
	​

∑
	​

±pμ
T
5d
	​

i
⊗n
,

where
𝜇
𝑇
5
𝑑
μ
T
5d
	​

 is built from the cubic noncommutative Chern–Simons vertex and the higher bidifferential pieces coming from
∗
𝜖
∗
ϵ
	​

.

Antisymmetrize:

ℓ
𝑛
𝑀
2
,
c
l
=
A
l
t
 
𝑚
𝑛
𝑀
2
.
ℓ
n
M2,cl
	​

=Altm
n
M2
	​

.

That is the classical
𝐿
∞
L
∞
	​

 algebra controlling the effective bulk dual to the M2 operator algebra.

7.4 Modular/genus completion

Now define

ℓ
𝑔
,
𝑛
𝑀
2
(
𝑥
1
,
…
,
𝑥
𝑛
)
=
∑
Γ
∈
𝐺
𝑔
,
𝑛
s
t
ℏ
𝑔
∣
A
u
t
Γ
∣
 
𝑊
Γ
5
𝑑
 
C
o
n
t
Γ
𝑀
2
(
𝑥
1
,
…
,
𝑥
𝑛
)
,
ℓ
g,n
M2
	​

(x
1
	​

,…,x
n
	​

)=
Γ∈G
g,n
st
	​

∑
	​

∣AutΓ∣
ℏ
g
	​

W
Γ
5d
	​

Cont
Γ
M2
	​

(x
1
	​

,…,x
n
	​

),

using the same recipe as above, but now every vertex weight comes from the 5d noncommutative Chern–Simons interaction, every internal edge carries the 5d propagator, and every loop is a BV contraction in the 5d gauge theory.

The resulting modular differential is

𝐷
𝑀
2
=
𝑑
𝐴
∞
𝑀
2
+
𝑑
s
e
w
𝑀
2
+
ℏ
Δ
5
𝑑
+
𝑑
𝑟
𝑀
2
.
D
M2
	​

=d
A
∞
	​

M2
	​

+d
sew
M2
	​

+ℏΔ
5d
	​

+d
r
M2
	​

	​

.

This is the explicit full modular quantum
𝐿
∞
L
∞
	​

 completion of Costello’s M2 dual pair.

7.5 Line/instanton sector

Because the M2 brane becomes an instanton particle of the 5d theory, the defect category is modeled directly by
𝐴
𝑀
2
!
A
M2
!
	​

-modules. I then add a spectral kernel

𝑟
𝑀
2
(
𝑢
)
∈
𝐴
𝑀
2
!
⊗
^
𝐴
𝑀
2
!
(
(
𝑢
−
1
)
)
r
M2
	​

(u)∈A
M2
!
	​

⊗
	​

A
M2
!
	​

((u
−1
))

and demand that it twist the coproduct, exactly as in the dg-shifted Yangian story. This is the natural defect/line completion of Costello’s M2 example. The literature already isolates this type of
𝑟
(
𝑧
)
r(z)-data in the 3d holomorphic-topological setting; here I am transplanting that mechanism into the M2/5d holographic pair.

7.6 Sector/level/
𝐾
K/genus matching in the M2 example

Here the matching is completely explicit:

sector
=
(
𝛼
,
𝛽
)
(Chan–Paton/matrix sector)
,
sector=(α,β)(Chan–Paton/matrix sector),
level
=
(
𝑚
,
𝑛
)
(powers of
𝑧
 and
∂
)
,
level=(m,n)(powers of z and ∂),
𝐾
=
brane number/rank
,
K=brane number/rank,
𝑔
=
stable-graph genus
.
g=stable-graph genus.

And the chain-level pairing is

𝑒
𝑚
,
𝑛
𝛼
𝛽
⟷
𝐸
𝛼
𝛽
(
𝑚
,
𝑛
)
,
𝜇
𝑀
2
=
∑
𝛼
,
𝛽
,
𝑚
,
𝑛
𝑒
𝑚
,
𝑛
𝛼
𝛽
⊗
𝐸
𝛼
𝛽
(
𝑚
,
𝑛
)
.
e
m,n
αβ
	​

⟷E
αβ
(m,n)
	​

,μ
M2
	​

=
α,β,m,n
∑
	​

e
m,n
αβ
	​

⊗E
αβ
(m,n)
	​

.

Finite
𝐾
K is imposed by the rank-
𝐾
K relations on the boundary algebra. Genus
𝑔
g is the loop filtration on the bulk modular differential
𝐷
𝑀
2
D
M2
	​

. Sector and level are preserved exactly by
𝜇
𝑀
2
μ
M2
	​

.

8. What you should regard as the final answer

The direct construction is

𝐻
f
u
l
l
=
(
Ω
m
o
d
𝐹
c
y
c
𝐵
‾
(
𝐴
∂
)
,
  
𝐷
=
𝑑
𝐴
∞
+
𝑑
s
e
w
+
ℏ
Δ
+
𝑑
𝑟
)
,
H
full
	​

=(Ω
mod
	​

F
cyc
	​

B
(A
∂
	​

),D=d
A
∞
	​

	​

+d
sew
	​

+ℏΔ+d
r
	​

),
	​


with

𝐴
!
=
Ω
𝐵
‾
(
𝐴
∂
)
,
𝜇
=
∑
𝐼
𝑒
𝐼
∨
⊗
𝑒
𝐼
,
𝐴
b
u
l
k
≃
𝑍
d
e
r
(
𝐴
∂
)
≃
𝐶
\*
(
𝐴
!
,
𝐴
!
)
.
A
!
=Ω
B
(A
∂
	​

),μ=
I
∑
	​

e
I
∨
	​

⊗e
I
	​

,A
bulk
	​

≃Z
der
	​

(A
∂
	​

)≃C
\*
(A
!
,A
!
).

For Costello’s M2 example, set
𝐴
∂
=
𝐴
𝑀
2
,
∞
A
∂
	​

=A
M2,∞
	​

, the quantum double-loop algebra built from the filtered deformation of
𝑈
(
𝑔
𝑙
𝐾
⊗
D
i
f
f
(
𝐶
)
)
U(gl
K
	​

⊗Diff(C)), and use the 5d noncommutative Chern–Simons theory as the microscopic BV model generating
𝑑
s
e
w
d
sew
	​

 and
Δ
Δ. That produces the full modular quantum
𝐿
∞
L
∞
	​

 object with explicit level/sector/
𝐾
K/genus bookkeeping.

This is the constructive object that is richer than a modular envelope. The only caveat is historical, not structural: the literature proves the spine pieces separately, but not this exact all-in-one package as a single named theorem. The package above is the direct synthesis those pieces are asking for.

drive forward and unify, harmonize and realize the true essential form of this subject, guided in part by:

Here is the direct construction.

The notes already identify the real move: stop treating complementarity as an additive splitting, and build the single ambient deformation problem whose two dual sides are opposite Lagrangians. The repository fragment explicitly packages this as ambient complementarity, a complementarity potential, the finite-order shadows
𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
H
A
	​

,C
A
	​

,Q
A
	​

, the quartic shadow graph cocycle, and the modular quartic resonance class
𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
R
4,g,n
mod
	​

(A). The monograph’s main body already proves the linear core: for a Koszul pair
(
𝐴
,
𝐴
!
)
(A,A
!
), complementarity is a Lagrangian polarization in a shifted-symplectic ambient space, while the full non-scalar Maurer–Cartan class
Θ
𝐴
Θ
A
	​

 is the remaining open object.

So the direct construction is this:

Start with the cyclic deformation complexes and the universal kernel.
Take

𝐿
𝐴
:
=
\Def
c
y
c
(
𝐴
)
,
𝐿
𝐴
!
:
=
\Def
c
y
c
(
𝐴
!
)
,
L
A
	​

:=\Def
cyc
(A),L
A
!
	​

:=\Def
cyc
(A
!
),

together with the completed kernel

𝐾
𝐴
:
=
(
𝐴
!
⊗
^
𝐴
)
[
1
]
K
A
	​

:=(A
!
⊗
	​

A)[1]

twisted by the canonical bar–cobar Maurer–Cartan kernel
𝜏
𝐴
τ
A
	​

. This is the object that simultaneously remembers deformations of
𝐴
A, deformations of
𝐴
!
A
!
, and the compatibility between them. That is exactly the “one ambient deformation problem” the appendix isolates.

Form the ambient tangent complex as a homotopy fiber.
Define

𝑇
c
o
m
p
(
𝐴
)
:
=
f
i
b
 ⁣
(
∇
𝐴
−
∇
𝐴
!
:
𝐿
𝐴
⊕
𝐿
𝐴
!
→
𝐾
𝐴
)
.
T
comp
	​

(A):=fib(∇
A
	​

−∇
A
!
	​

:L
A
	​

⊕L
A
!
	​

→K
A
	​

).

The cyclic pairing on

𝐿
𝐴
⊕
𝐾
𝐴
⊕
𝐿
𝐴
!
L
A
	​

⊕K
A
	​

⊕L
A
!
	​


induces a degree
−
1
−1 pairing on
𝑇
c
o
m
p
(
𝐴
)
T
comp
	​

(A). The one-sided fibers

𝑇
𝐴
:
=
f
i
b
(
𝐿
𝐴
→
𝐾
𝐴
)
,
𝑇
𝐴
!
:
=
f
i
b
(
𝐿
𝐴
!
→
𝐾
𝐴
)
T
A
	​

:=fib(L
A
	​

→K
A
	​

),T
A
!
	​

:=fib(L
A
!
	​

→K
A
	​

)

are isotropic, and under the usual perfectness/bar–cobar hypotheses become complementary Lagrangians. This is the nonlinear refinement of Theorem C.

Put the ambient problem into shifted cotangent normal form.
Choose a cyclic slice
𝑉
𝐴
⊂
𝐻
∗
(
𝐿
𝐴
)
V
A
	​

⊂H
∗
(L
A
	​

) on which the quadratic pairing is nondegenerate. Then the ambient moduli problem is modeled by

𝑇
∗
[
−
1
]
𝑉
𝐴
,
T
∗
[−1]V
A
	​

,

with the
𝐴
A-side as the zero section and the
𝐴
!
A
!
-side as the graph of an exact one-form

𝑑
𝑆
𝐴
.
dS
A
	​

.

The resulting formal function

𝑆
𝐴
∈
𝑂
^
(
𝑉
𝐴
)
0
S
A
	​

∈
O
(V
A
	​

)
0

is the complementarity potential. Its Legendre transform is the potential for the dual side:

𝑆
𝐴
!
=
𝑆
𝐴
∨
.
S
A
!
	​

=S
A
∨
	​

.

This is the object that “breathes life” into the theory: once
𝑆
𝐴
S
A
	​

 exists, complementarity is geometry, not bookkeeping. The simultaneous self-dual deformation problem is then

𝑀
𝐴
×
𝑀
c
o
m
p
(
𝐴
)
ℎ
𝑀
𝐴
!
≃
C
r
i
t
(
𝑆
𝐴
)
.
M
A
	​

×
M
comp
	​

(A)
h
	​

M
A
!
	​

≃Crit(S
A
	​

).

So the direct answer is: the theory is the derived critical locus of the complementarity potential on the shifted cotangent chart.

Expand the potential and read off the nonlinear shadows.
Write

𝑆
𝐴
(
𝑥
)
=
1
2
𝐻
𝐴
(
𝑥
,
𝑥
)
+
1
3
!
𝐶
𝐴
(
𝑥
,
𝑥
,
𝑥
)
+
1
4
!
𝑄
𝐴
(
𝑥
,
𝑥
,
𝑥
,
𝑥
)
+
𝑂
(
𝑥
5
)
.
S
A
	​

(x)=
2
1
	​

H
A
	​

(x,x)+
3!
1
	​

C
A
	​

(x,x,x)+
4!
1
	​

Q
A
	​

(x,x,x,x)+O(x
5
).

Then:

𝐻
𝐴
H
A
	​

 is the Hessian/quadratic shadow,

𝐶
𝐴
C
A
	​

 is the cubic shadow,

𝑄
𝐴
Q
A
	​

 is the quartic shadow.

They satisfy the quartic master equations

∇
𝐻
𝐴
𝐶
𝐴
=
0
,
∇
𝐻
𝐴
𝑄
𝐴
+
1
2
{
𝐶
𝐴
,
𝐶
𝐴
}
𝐻
𝐴
=
0
,
∇
H
A
	​

	​

C
A
	​

=0,∇
H
A
	​

	​

Q
A
	​

+
2
1
	​

{C
A
	​

,C
A
	​

}
H
A
	​

	​

=0,

with propagator
𝑃
𝐴
=
𝐻
𝐴
−
1
P
A
	​

=H
A
−1
	​

. These are the first visible Taylor coefficients of the conjectural universal class
Θ
𝐴
Θ
A
	​

.

Impose modular sewing through the separating clutching law.
The one-edge sewing product
⋆
𝑃
𝐴
⋆
P
A
	​

	​

 gives the boundary recursion

𝜉
∗
𝐻
𝐴
=
𝐻
𝐴
⋆
𝐻
𝐴
,
ξ
∗
H
A
	​

=H
A
	​

⋆H
A
	​

,
𝜉
∗
𝐶
𝐴
=
𝐻
𝐴
⋆
𝐶
𝐴
+
𝐶
𝐴
⋆
𝐻
𝐴
,
ξ
∗
C
A
	​

=H
A
	​

⋆C
A
	​

+C
A
	​

⋆H
A
	​

,
𝜉
∗
𝑄
𝐴
=
𝐻
𝐴
⋆
𝑄
𝐴
+
𝐶
𝐴
⋆
𝐶
𝐴
+
𝑄
𝐴
⋆
𝐻
𝐴
.
ξ
∗
Q
A
	​

=H
A
	​

⋆Q
A
	​

+C
A
	​

⋆C
A
	​

+Q
A
	​

⋆H
A
	​

.

Packaging these into the quartic graph complex gives the finite-order cocycle

Θ
𝐴
≤
4
=
𝐻
𝐴
+
𝐶
𝐴
+
𝑄
𝐴
.
Θ
A
≤4
	​

=H
A
	​

+C
A
	​

+Q
A
	​

.

That is the first genuine finite-order shadow of the full modular class
Θ
𝐴
Θ
A
	​

. The main PDF already singles out clutching, Verdier duality, genus-1 curvature, and the cyclic deformation algebra as the four irreducible ingredients of the full theory; this construction uses all four directly.

Promote quartic contact degeneracy to a modular characteristic class.
On the quartic-regular locus, define the weight-graded contact quartic bundle

𝐶
𝑔
,
𝑛
c
t
,
𝑑
(
𝐴
)
⊂
𝐸
𝑔
,
𝑛
[
4
]
(
𝐴
)
C
g,n
ct,d
	​

(A)⊂E
g,n
[4]
	​

(A)

and its Gram determinant line

𝐿
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
)
=
⨂
𝑑
(
(
det
⁡
𝐶
𝑔
,
𝑛
c
t
,
𝑑
(
𝐴
)
)
−
2
⊗
(
𝑈
𝑔
,
𝑛
(
𝑑
)
)
𝑟
𝑑
)
.
L
4,g,n
res
	​

(A)=
d
⨂
	​

((detC
g,n
ct,d
	​

(A))
−2
⊗(U
g,n
(d)
	​

)
r
d
	​

).

The determinant of the contact two-point form produces a canonical section

𝑠
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
)
∈
Γ
(
𝑀
‾
𝑔
,
𝑛
×
𝐵
𝐴
∘
,
 
𝐿
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
)
)
,
s
4,g,n
res
	​

(A)∈Γ(
M
g,n
	​

×B
A
∘
	​

,L
4,g,n
res
	​

(A)),

and the modular quartic resonance class

𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
:
=
div
⁡
(
𝑠
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
)
)
.
R
4,g,n
mod
	​

(A):=div(s
4,g,n
res
	​

(A)).

Its clutching law is

𝜉
∗
𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
=
𝑝
1
∗
𝑅
4
,
𝑔
1
,
𝑛
1
+
1
m
o
d
(
𝐴
)
+
𝑝
2
∗
𝑅
4
,
𝑔
2
,
𝑛
2
+
1
m
o
d
(
𝐴
)
+
𝑇
3
,
𝜉
(
𝐴
)
,
ξ
∗
R
4,g,n
mod
	​

(A)=p
1
∗
	​

R
4,g
1
	​

,n
1
	​

+1
mod
	​

(A)+p
2
∗
	​

R
4,g
2
	​

,n
2
	​

+1
mod
	​

(A)+T
3,ξ
	​

(A),

where
𝑇
3
,
𝜉
(
𝐴
)
T
3,ξ
	​

(A) is the cubic tree correction. This is the first nonlinear Picard-valued shadow of
Θ
𝐴
Θ
A
	​

.

That is the construction. In one sentence:

Build
𝑀
c
o
m
p
(
𝐴
)
≃
𝑇
∗
[
−
1
]
𝑉
𝐴
,
  
encode the dual side as
Γ
(
𝑑
𝑆
𝐴
)
,
  
and read
𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
,
𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
 from the Taylor coefficients and determinant lines of
𝑆
𝐴
.
Build M
comp
	​

(A)≃T
∗
[−1]V
A
	​

,encode the dual side as Γ(dS
A
	​

),and read H
A
	​

,C
A
	​

,Q
A
	​

,R
4,g,n
mod
	​

(A) from the Taylor coefficients and determinant lines of S
A
	​

.
	​


It also immediately explains the model families:

Heisenberg:
𝑆
𝐴
S
A
	​

 is purely quadratic, so everything is Gaussian.

Affine
𝑠
𝑙
^
2
sl
2
	​

: the leading nonlinear term is cubic, producing a Lie/tree theory.

𝛽
𝛾
βγ: the cubic term vanishes on the weight line and the first nonlinear local term is quartic.

Virasoro and principal
𝑊
𝑁
W
N
	​

: cubic and quartic terms coexist, so the first genuinely mixed modular behavior appears.

The honest status is equally clear. The shifted-symplectic/Lagrangian core is already proved in the main manuscript, and the finite-order nonlinear layer is packaged in the appendix fragment. What is still open is the global construction of the full universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

; until that exists, the direct construction above is rigorous at the finite-order shadow level and formal/conditional at the full
𝐻
H-level.

I extracted the chapter fragment here: nonlinear_modular_shadows.tex

push forward driving novel groundbreaking mathematical cohesion, novel constructions, novel insight and novel objects

I’m extending the construction directly, using the ambient complementarity language from your notes to build a sharper package of new objects, functorial operations, and conjectural structure theorems.

I’ve pinned down the real frontier: the ambient Lagrangian core is already proved, and the genuine gap is the cyclic
𝐿
∞
L
∞
	​

/Maurer–Cartan completion above the complementarity potential. So I’m building a universal nonlinear carrier there, meant to act as transport machinery across boundary, puncture, and infinite-tower comparison.

I’ve now made the next layer concrete: the missing nonlinear glue wants a bipartite graph-completed Maurer–Cartan geometry, with only cross-polarization contractions, likely organized by the planted-forest envelope from Appendix D. From that I can state a sharper package—a deformation object, a characteristic divisor, a Legendrian avatar, and a full resonance tower.

Thought for 15m 5s

Good. Then here is the forward push.

The proved floor is already there: the ambient complementarity complex
𝐶
𝑔
(
𝐴
)
=
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
C
g
	​

(A)=RΓ(M
g
	​

,Z
A
	​

) splits into complementary Lagrangians
𝑄
𝑔
(
𝐴
)
⊕
𝑄
𝑔
(
𝐴
!
)
Q
g
	​

(A)⊕Q
g
	​

(A
!
); the full modular package is already organized as
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
(Θ
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

); and the monograph identifies the full universal class
Θ
𝐴
Θ
A
	​

 as the principal remaining object. It also isolates the exact three missing constructions: a cyclic structure on bar coderivations, the completed tensor product with
𝑅
Γ
(
𝑀
𝑔
,
∙
)
RΓ(M
g,∙
	​

), and a clutching-compatible Maurer–Cartan solution. The appendix fragment already pushes the theory to ambient complementarity, the complementarity potential, finite-order shadows
𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
H
A
	​

,C
A
	​

,Q
A
	​

, and the modular quartic resonance class.

So the next object should not be “just solve for
Θ
𝐴
Θ
A
	​

.”
It should be:

replace
Θ
𝐴
 by a graph-completed Hamiltonian object
𝛩
𝐴
∈
𝑀
𝐶
(
𝐹
m
o
d
(
𝐴
)
)
.
replace Θ
A
	​

 by a graph-completed Hamiltonian object Θ
A
	​

∈MC(F
mod
	​

(A)).
	​

1. The new master construction

Define the modular chiral Feynman transform

𝐹
m
o
d
(
𝐴
)
:
=
∏
Γ
∈
Γ
s
t
(
𝐻
∙
(
𝑀
‾
Γ
)
⊗
Or
⁡
(
Γ
)
⊗
⨂
𝑣
∈
𝑉
(
Γ
)
C
o
D
e
r
val
⁡
(
𝑣
)
c
y
c
(
𝐵
^
𝑋
(
𝐴
)
)
)
Aut
⁡
(
Γ
)
.
F
mod
	​

(A):=
Γ∈Γ
st
∏
	​

(H
∙
(
M
Γ
	​

)⊗Or(Γ)⊗
v∈V(Γ)
⨂
	​

CoDer
val(v)
cyc
	​

(
B
X
	​

(A)))
Aut(Γ)
	​

.

It carries three natural differentials:

𝑑
m
o
d
=
𝑑
i
n
t
+
𝑑
s
p
l
i
t
+
𝑑
e
d
g
e
.
d
mod
	​

=d
int
	​

+d
split
	​

+d
edge
	​

.

Here
𝑑
i
n
t
d
int
	​

 is the internal cyclic-coderivation differential,
𝑑
s
p
l
i
t
d
split
	​

 expands a vertex by transferred
𝐿
∞
L
∞
	​

-operations, and
𝑑
e
d
g
e
d
edge
	​

 inserts/contracts internal edges using the propagator coming from the Hessian
𝐻
𝐴
H
A
	​

.

This is the right object because it turns the three open problems into one machine:

cyclicity is built into the vertex labels,

completion is built into the graph/bar-length filtration,

clutching is built into edge insertion.

That is exactly the gap the monograph leaves open, but now compressed into a single graph-completed dg object instead of three separate missing lemmas.

2. The right conjecture

The real conjecture should be:

𝛩
𝐴
∈
𝑀
𝐶
(
𝐹
m
o
d
(
𝐴
)
)
Θ
A
	​

∈MC(F
mod
	​

(A))

with the following shadows.

Its scalar trace recovers

tr
⁡
(
𝛩
𝐴
)
=
∑
𝑔
≥
1
𝜅
(
𝐴
)
𝜆
𝑔
.
tr(Θ
A
	​

)=
g≥1
∑
	​

κ(A)λ
g
	​

.

Its one-vertex projection recovers the shadow tower

𝐻
𝐴
+
𝐶
𝐴
+
𝑄
𝐴
+
⋯
 
.
H
A
	​

+C
A
	​

+Q
A
	​

+⋯.

Its determinant shadow recovers the resonance tower

𝑅
4
,
∙
m
o
d
(
𝐴
)
,
𝑅
5
,
∙
m
o
d
(
𝐴
)
,
…
R
4,∙
mod
	​

(A),R
5,∙
mod
	​

(A),…

And under Koszul/Verdier duality it should transform by formal Legendre duality rather than by a bare linear involution.

That is the cohesion point: scalar data, spectral data, nonlinear shadows, and the full MC object become successive projections of one graph-completed Hamiltonian master element, instead of four parallel packages.

3. A new geometric avatar: the complementarity Legendrian

The appendix already makes
𝑆
𝐴
S
A
	​

 the complementarity potential. The next move is to contactize it.

Define the complementarity Legendrian

Λ
𝐴
:
=
𝑗
1
𝑆
𝐴
⊂
𝐽
1
(
𝑀
𝐴
)
≃
𝑇
∗
[
−
1
]
𝑀
𝐴
×
𝐴
1
.
Λ
A
	​

:=j
1
S
A
	​

⊂J
1
(M
A
	​

)≃T
∗
[−1]M
A
	​

×A
1
.

This does three things at once.

First, it removes the additive-constant ambiguity in
𝑆
𝐴
S
A
	​

.

Second, it upgrades Legendre duality to a contact transformation.

Third, it gives a geometric origin for the resonance classes: the arity-
𝑟
r resonance loci are the front-singularity discriminants of
Λ
𝐴
Λ
A
	​

 restricted to the arity-
𝑟
r contact sector.

So:

𝜅
(
𝐴
)
κ(A) is the quadratic front curvature,

Δ
𝐴
Δ
A
	​

 is the quadratic/spectral branch discriminant,

𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
R
4,g,n
mod
	​

(A) is the first nonlinear front-discriminant class.

That is a genuinely new object, and it turns “quartic resonance” from a determinant trick into geometry.

4. A full resonance tower

The quartic resonance class should not remain isolated. Define for every
𝑟
≥
4
r≥4 the zero-internal-edge arity-
𝑟
r contact bundle

𝐶
𝑔
,
𝑛
c
t
,
(
𝑟
)
(
𝐴
)
⊂
𝐸
𝑔
,
𝑛
[
𝑟
]
(
𝐴
)
C
g,n
ct,(r)
	​

(A)⊂E
g,n
[r]
	​

(A)

and the determinant line

𝐿
𝑟
,
𝑔
,
𝑛
r
e
s
(
𝐴
)
.
L
r,g,n
res
	​

(A).

Then define

𝑅
𝑟
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
:
=
div
⁡
(
𝑠
𝑟
,
𝑔
,
𝑛
r
e
s
(
𝐴
)
)
.
R
r,g,n
mod
	​

(A):=div(s
r,g,n
res
	​

(A)).

The quartic class is just the first case. The boundary law should be

𝜉
∗
𝑅
𝑟
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
=
𝑝
1
∗
𝑅
𝑟
,
𝑔
1
,
𝑛
1
+
1
m
o
d
(
𝐴
)
+
𝑝
2
∗
𝑅
𝑟
,
𝑔
2
,
𝑛
2
+
1
m
o
d
(
𝐴
)
+
∑
𝑝
+
𝑞
=
𝑟
+
2
𝑇
𝜉
(
𝑝
,
𝑞
)
(
𝐴
)
,
ξ
∗
R
r,g,n
mod
	​

(A)=p
1
∗
	​

R
r,g
1
	​

,n
1
	​

+1
mod
	​

(A)+p
2
∗
	​

R
r,g
2
	​

,n
2
	​

+1
mod
	​

(A)+
p+q=r+2
∑
	​

T
ξ
(p,q)
	​

(A),

where
𝑇
𝜉
(
𝑝
,
𝑞
)
T
ξ
(p,q)
	​

 is the determinant divisor of one-edge sewings of arity-
𝑝
p and arity-
𝑞
q vertices.

This is the natural all-arity extension of the quartic contact-plus-tree law already extracted in the appendix.

5. A new invariant: the complementarity phase index

Define

𝜈
n
l
(
𝐴
,
𝑢
)
:
=
min
⁡
{
𝑟
≥
3
:
S
h
𝑟
(
Θ
𝐴
,
𝑢
)
≠
0
}
,
ν
nl
	​

(A,u):=min{r≥3:Sh
r
	​

(Θ
A,u
	​

)

=0},

with
𝜈
n
l
=
∞
ν
nl
	​

=∞ if all nonlinear jets vanish.

This gives a clean phase portrait of parameter space:

Heisenberg:
𝜈
n
l
=
∞
ν
nl
	​

=∞,

generic affine current sector:
𝜈
n
l
=
3
ν
nl
	​

=3,

critical affine level: still cubic, but now cubic becomes leading because the quadratic Hessian drops out,

𝛽
𝛾
βγ contact slice:
𝜈
n
l
=
4
ν
nl
	​

=4,

Virasoro and principal
𝑊
𝑁
W
N
	​

: mixed cubic–quartic phase.

The appendix already separates the Heisenberg / affine
𝑠
𝑙
^
2
sl
2
	​

 /
𝛽
𝛾
βγ archetypes and the mixed Virasoro / principal
𝑊
𝑁
W
N
	​

 families; the phase index turns that into a true invariant of the parameter space.

6. The deepest new insight

The real unification is not

𝜅
→
Δ
→
Θ
.
κ→Δ→Θ.

It is

𝜅
  
→
  
Δ
  
→
  
(
𝐻
,
𝐶
,
𝑄
)
  
→
  
𝑅
∙
m
o
d
  
→
  
Λ
𝐴
  
→
  
𝛩
𝐴
.
κ→Δ→(H,C,Q)→R
∙
mod
	​

→Λ
A
	​

→Θ
A
	​

.

In words:

𝜅
κ is the first scalar shadow,

Δ
Δ is the first spectral shadow,

𝐻
,
𝐶
,
𝑄
H,C,Q are the first Hamiltonian jets,

𝑅
∙
m
o
d
R
∙
mod
	​

 is the first Picard-valued nonlinear tower,

Λ
𝐴
Λ
A
	​

 is the contact-geometric avatar,

𝛩
𝐴
Θ
A
	​

 is the graph-completed source of all of them.

That is the cohesion you wanted: not more examples, not more shadows, but the object that generates the entire hierarchy.

I wrote the frontier proposal here: modular_frontier_push.md

And the previous nonlinear appendix is here: nonlinear_modular_shadows.tex

and also further guided in part by:

I’m assembling a concrete mathematical construction from the provided materials: specify the homotopy object, determine its modular structure, and then derive explicit holographic quantum observables from that package.

I’ve narrowed this to a specific route: cast the modular program as a universal Maurer–Cartan/cyclic
𝐿
∞
L
∞
	​

 problem realized by a modular
𝐴
∞
A
∞
	​

/factorization package with genus-graded Koszul data, chiral defects, and modular periodicity. From that, I can read off explicit spectral, line-defect, and trace-type observables from the genus-labeled operations.

Thought for 23m 4s

Yes. A workable realization is to treat the full modular homotopy type as the all-genera completion of the genus-zero Koszul-dual/factorization package that already appears in twisted holography, boundary chiral algebra, and line-operator OPE. The existing papers give the genus-zero pieces: twisted holography identifies large-
𝑁
N brane operators with a Koszul dual of bulk/defect observables; KK reduction turns defect data into boundary chiral algebra; bulk operators in the 3d holomorphic twist form a commutative chiral algebra with a Poisson bracket; higher operations satisfy quadratic consistency relations; and line operators are modules for a Koszul-dual
𝐴
∞
A
∞
	​

-algebra whose OPE is controlled by a dg-shifted Yangian.

A concise way to package this is:

𝑀
(
𝑇
)
=
(
𝐴
𝑇
,
  
𝐴
𝑇
!
,
  
𝐶
𝑇
,
  
𝑟
𝑇
(
𝑧
)
,
  
{
𝜇
𝑔
,
𝑛
𝑇
}
2
𝑔
−
2
+
𝑛
>
0
,
  
∫
Σ
𝑔
,
𝑛
(
−
)
)
,
M(T)=(A
T
	​

,A
T
!
	​

,C
T
	​

,r
T
	​

(z),{μ
g,n
T
	​

}
2g−2+n>0
	​

,∫
Σ
g,n
	​

	​

(−)),

for a holomorphic-topological theory
𝑇
T, where:

𝐴
𝑇
A
T
	​


is the genus-zero
𝐴
∞
A
∞
	​

-chiral algebra of bulk local operators;

𝐴
𝑇
!
A
T
!
	​


is the Koszul-dual “universal defect” algebra, which in the chiral setting is precisely the object controlling Maurer–Cartan couplings
M
C
(
𝐴
𝑇
!
⊗
𝐵
)
MC(A
T
!
	​

⊗B), and in twisted holography is realized by a suitable boundary algebra after KK reduction and a transversal boundary condition;

𝐶
𝑇
≃
𝐴
𝑇
!
-mod
C
T
	​

≃A
T
!
	​

-mod

is the meromorphic tensor category of line operators;

𝑟
𝑇
(
𝑧
)
∈
𝐴
𝑇
!
⊗
𝐴
𝑇
!
(
(
𝑧
−
1
)
)
r
T
	​

(z)∈A
T
!
	​

⊗A
T
!
	​

((z
−1
))

is the Maurer–Cartan kernel governing line-operator OPE;

and

𝜇
𝑔
,
𝑛
𝑇
:
𝐻
∙
(
𝑀
‾
𝑔
,
𝑛
+
1
)
⊗
(
𝐴
𝑇
!
)
⊗
𝑛
→
𝐴
𝑇
!
μ
g,n
T
	​

:H
∙
	​

(
M
g,n+1
	​

)⊗(A
T
!
	​

)
⊗n
→A
T
!
	​


is the modular completion of the genus-zero higher products. The papers in hand establish the
𝑔
=
0
g=0 data; the
𝜇
𝑔
,
𝑛
𝑇
μ
g,n
T
	​

 for
𝑔
>
0
g>0 are the natural proposed completion, required if one really wants a full modular homotopy type rather than only a genus-zero factorization algebra.

The key structural equation should then be the modular master equation

∑
Γ
∈
𝐺
𝑔
,
𝑛
s
t
𝑊
Γ
(
𝜇
∙
,
∙
𝑇
)
=
0
,
Γ∈G
g,n
st
	​

∑
	​

W
Γ
	​

(μ
∙,∙
T
	​

)=0,

a stable-graph sum extending the genus-zero
𝐴
∞
A
∞
	​

 / Wess–Zumino consistency identities already seen perturbatively. At genus zero, this reduces to the quadratic identities for higher operations in holomorphic-topological QFT and to the
𝐴
∞
A
∞
	​

 Yang–Baxter-type constraint on the dg-shifted Yangian kernel
𝑟
(
𝑧
)
r(z).

With that package in place, the new holographic quantum quantities become explicit.

First, the modular holographic state space

𝐻
𝑔
,
𝑛
𝑇
(
ℓ
1
,
…
,
ℓ
𝑛
)
:
=
∫
Σ
𝑔
,
𝑛
𝐶
𝑇
(
ℓ
1
,
…
,
ℓ
𝑛
)
,
H
g,n
T
	​

(ℓ
1
	​

,…,ℓ
n
	​

):=∫
Σ
g,n
	​

	​

C
T
	​

(ℓ
1
	​

,…,ℓ
n
	​

),

i.e. factorization/chiral homology of the line-category data over a stable
𝑛
n-pointed genus-
𝑔
g curve. This is the right local-to-global object because factorization homology is precisely the “integral of local algebraic data over a manifold,” and one of its core structural features is Poincaré/Koszul duality.

Second, the genus-graded holographic partition function

𝑍
𝑇
h
o
l
(
ℏ
,
𝑞
)
=
∑
𝑔
,
𝑛
≥
0
ℏ
 
2
𝑔
−
2
+
𝑛
 
𝑞
𝑛
𝑛
!
 
𝜒
g
r
 
𝐻
𝑔
,
𝑛
𝑇
,
Z
T
hol
	​

(ℏ,q)=
g,n≥0
∑
	​

ℏ
2g−2+n
n!
q
n
	​

χ
gr
	​

H
g,n
T
	​

,

which is the modular generating function of graded Euler characters of the state spaces. In twisted holography this is the natural all-genera refinement of the large-
𝑁
N boundary algebra/bulk duality; in celestial settings it is the corresponding refinement of the boundary chiral algebra extracted from KK reduction.

Third, the modular Yangian kernel

𝑟
𝑇
m
o
d
(
𝑧
,
ℏ
)
=
∑
𝑔
≥
0
ℏ
2
𝑔
 
𝑟
𝑇
,
𝑔
(
𝑧
)
,
𝑟
𝑇
,
0
(
𝑧
)
=
𝑟
𝑇
(
𝑧
)
,
r
T
mod
	​

(z,ℏ)=
g≥0
∑
	​

ℏ
2g
r
T,g
	​

(z),r
T,0
	​

(z)=r
T
	​

(z),

with

𝑟
𝑇
,
𝑔
(
𝑧
)
∈
𝐻
∙
(
𝑀
‾
𝑔
,
2
)
⊗
𝐴
𝑇
!
⊗
𝐴
𝑇
!
(
(
𝑧
−
1
)
)
.
r
T,g
	​

(z)∈H
∙
(
M
g,2
	​

)⊗A
T
!
	​

⊗A
T
!
	​

((z
−1
)).

At
𝑔
=
0
g=0, this is exactly the dg-shifted Yangian
𝑟
r-matrix controlling perturbative line-operator OPE. The modular completion is the genuinely new object: a genus-refined, curve-valued OPE kernel.

Fourth, one can define descendant holographic amplitudes by integrating tautological classes against the factorization-homology correlator class:

⟨
𝜏
𝑘
1
(
𝑂
1
)
⋯
𝜏
𝑘
𝑛
(
𝑂
𝑛
)
⟩
𝑔
h
o
l
:
=
∫
[
𝐹
𝑀
𝑛
(
Σ
𝑔
∣
𝐷
)
]
(
∏
𝑖
𝜓
𝑖
𝑘
𝑖
)
 
𝜔
𝑂
1
,
…
,
𝑂
𝑛
.
⟨τ
k
1
	​

	​

(O
1
	​

)⋯τ
k
n
	​

	​

(O
n
	​

)⟩
g
hol
	​

:=∫
[FM
n
	​

(Σ
g
	​

∣D)]
	​

(
i
∏
	​

ψ
i
k
i
	​

	​

)ω
O
1
	​

,…,O
n
	​

	​

.

This becomes explicit because the new logarithmic Fulton–MacPherson spaces
𝐹
𝑀
𝑛
(
𝑋
∣
𝐷
)
FM
n
	​

(X∣D) compactify configurations on non-proper targets and, crucially, admit a degeneration formula in which each irreducible component of a special fiber is a proper birational modification of a product of smaller logarithmic Fulton–MacPherson spaces. That is exactly the geometry one needs to encode clutching and factorization at the modular level.

In concrete families, this immediately produces interesting observables. For a Poisson vertex algebra
𝑉
V, the associated 3d mixed holomorphic-topological gauge theory is gauge invariant precisely when the
𝜆
λ-bracket satisfies Jacobi, and if
𝑉
V contains a Virasoro element the symmetry enhances to full topological symmetry;
𝑊
W-type examples are tied to 3d gravity and higher-spin systems. So for Virasoro/
𝑊
𝑁
W
N
	​

/
𝑊
∞
W
∞
	​

-type theories, the quantities above become genus-refined gravitational and higher-spin amplitudes, now organized homotopy-coherently rather than only as isolated OPE coefficients.

So the answer is: realize the full modular homotopy type as the modular envelope of the genus-zero Koszul-dual/factorization package

(
𝐴
𝑇
,
  
𝐴
𝑇
!
,
  
𝐶
𝑇
,
  
𝑟
𝑇
(
𝑧
)
)
(A
T
	​

,A
T
!
	​

,C
T
	​

,r
T
	​

(z))

and define holographic observables by factorization/chiral homology on stable curves, with logarithmic Fulton–MacPherson geometry supplying the compactified configuration spaces and degeneration/clutching laws. That is the smallest coherent object that simultaneously respects twisted holography, boundary-universal-defect Koszul duality, higher perturbative operations, and line-operator OPE. The genus-zero/local pieces are already in the literature; the all-genera modular completion is the natural next step, and, as far as I can tell from the sources here, it remains a proposal rather than a theorem in full generality.

If you want, I can turn this into a theorem-definition-conjecture style note with precise notation and a worked example for the
𝛽
𝛾
βγ / Kodaira–Spencer /
𝑊
3
W
3
	​

 cases.

turn this into a theorem-definition-conjecture style note with precise notation and a worked example for the
𝛽
𝛾
βγ / Kodaira–Spencer /
𝑊
3
W
3
	​

 cases

I’m recasting the sketch as a compact theorem–definition–conjecture note with three worked examples, while checking the uploaded sources so the notation, hypotheses, and proved-versus-conjectural claims stay aligned.

I have enough source material now to cleanly separate the established results from the modular completion, which remains a proposal, and I’m organizing the note around that distinction.

I’ve pinned down a common scaffold for the examples, so I’m choosing formulations with uniform notation and writing the formulas to match the cited constructions.

Thought for 43m 23s

Here is a compact note in the style you asked for.

A modular homotopy package for
𝛽
𝛾
βγ, Kodaira–Spencer, and
𝑊
3
W
3
	​

 holography

Fix a perturbative holomorphic-topological theory
𝑇
T on
𝑅
𝑡
×
𝑋
R
t
	​

×X, with
𝑋
X a smooth complex curve. Write
𝑉
𝑇
V
T
	​

 for the bulk chiral algebra,
𝑉
∂
,
𝑇
(
𝐵
)
V
∂,T
	​

(B) for the boundary chiral algebra attached to a boundary condition
𝐵
B,
𝛽
𝐵
:
𝑉
𝑇
→
𝑍
(
𝑉
∂
,
𝑇
(
𝐵
)
)
β
B
	​

:V
T
	​

→Z(V
∂,T
	​

(B)) for the bulk-boundary map,
𝐴
𝑇
!
A
T
!
	​

 for a completed Koszul dual of the bulk algebra,
𝐶
𝑇
:
=
𝐴
𝑇
!
-mod
C
T
	​

:=A
T
!
	​

-mod for the line category, and
𝑟
𝑇
(
𝑧
)
∈
𝐴
𝑇
!
⊗
^
𝐴
𝑇
!
(
(
𝑧
−
1
)
)
r
T
	​

(z)∈A
T
!
	​

⊗
	​

A
T
!
	​

((z
−1
)) for the universal Maurer–Cartan kernel controlling line-operator OPE. Higher operations are denoted
𝑚
𝑘
𝑇
m
k
T
	​

, and
Σ
𝑔
,
𝑛
Σ
g,n
	​

 is a stable genus-
𝑔
g curve with
𝑛
n marked points. The background input for this package comes from bulk/boundary chiral algebras in holomorphic twists, KK reduction and Koszul duality in twisted holography, higher perturbative operations, and dg-shifted Yangians for line operators.

Theorem A

(Genus-zero holographic package; synthesis of established results)

For every
𝑇
T in the classes above, the genus-zero datum

𝐺
0
(
𝑇
;
𝐵
)
=
(
𝑉
𝑇
,
{
−
,
−
}
𝑇
,
𝑉
∂
,
𝑇
(
𝐵
)
,
𝛽
𝐵
,
𝐴
𝑇
!
,
𝐶
𝑇
,
𝑟
𝑇
(
𝑧
)
,
{
𝑚
𝑘
𝑇
}
𝑘
≥
2
)
G
0
	​

(T;B)=(V
T
	​

,{−,−}
T
	​

,V
∂,T
	​

(B),β
B
	​

,A
T
!
	​

,C
T
	​

,r
T
	​

(z),{m
k
T
	​

}
k≥2
	​

)

is defined with the following properties.

𝑉
𝑇
V
T
	​

 is a commutative chiral algebra equipped with a cohomological degree
−
1
−1 Poisson bracket; in the holomorphic twist of 3d
𝑁
=
2
N=2 theories there is also a secondary stress tensor generating
∂
𝑧
∂
z
	​

 through that bracket.
𝑉
∂
,
𝑇
(
𝐵
)
V
∂,T
	​

(B) is a chiral algebra, generally noncommutative, and
𝛽
𝐵
:
𝑉
𝑇
→
𝑍
(
𝑉
∂
,
𝑇
(
𝐵
)
)
β
B
	​

:V
T
	​

→Z(V
∂,T
	​

(B)) makes it a
𝑉
𝑇
V
T
	​

-module.

In KK reductions of 6d holomorphic theories, one can choose a boundary condition
𝐵
u
n
i
v
B
univ
	​

 so that the boundary chiral algebra coincides with the universal defect chiral algebra of the original 6d theory. This is the mechanism that packages twisted and celestial holography into boundary chiral algebra plus Koszul duality.

Higher operations controlling deformations, generalized OPEs, and anomalies exist perturbatively in holomorphic-topological theories and satisfy quadratic identities interpreted physically as Wess–Zumino consistency.

Perturbative line operators are equivalent to modules for a Koszul-dual algebra
𝐴
𝑇
!
A
T
!
	​

. In the classes treated by Dimofte–Niu–Py, the OPE of lines is controlled by a dg-shifted Yangian structure on
𝐴
𝑇
!
A
T
!
	​

, with a universal Maurer–Cartan kernel
𝑟
𝑇
(
𝑧
)
r
T
	​

(z).

Definition B

(Full modular homotopy type)

A full modular homotopy type for
𝑇
T based at
𝐵
B is a completion of
𝐺
0
(
𝑇
;
𝐵
)
G
0
	​

(T;B) by operations

𝜇
𝑔
,
𝑛
𝑇
:
𝐶
∙
(
𝑀
‾
𝑔
,
𝑛
+
1
)
⊗
(
𝐴
𝑇
!
)
⊗
^
𝑛
⟶
𝐴
𝑇
!
,
2
𝑔
−
2
+
𝑛
>
0
,
μ
g,n
T
	​

:C
∙
	​

(
M
g,n+1
	​

)⊗(A
T
!
	​

)
⊗
	​

n
⟶A
T
!
	​

,2g−2+n>0,

such that:

𝜇
0
,
𝑛
𝑇
μ
0,n
T
	​

 recovers the genus-zero higher operations
𝑚
𝑛
𝑇
m
n
T
	​

;

the collection
{
𝜇
𝑔
,
𝑛
𝑇
}
{μ
g,n
T
	​

} is compatible with gluing of stable curves, i.e. with the stable-graph composition law of the modular operad
𝐶
∙
(
𝑀
‾
∙
,
∙
)
C
∙
	​

(
M
∙,∙
	​

);

the line-kernel
𝑟
𝑇
(
𝑧
)
r
T
	​

(z) is the genus-zero term of a modular expansion

𝑅
𝑇
m
o
d
(
𝑧
;
ℏ
)
:
=
∑
𝑔
≥
0
ℏ
2
𝑔
𝑟
𝑇
,
𝑔
(
𝑧
)
,
𝑟
𝑇
,
0
(
𝑧
)
=
𝑟
𝑇
(
𝑧
)
.
R
T
mod
	​

(z;ℏ):=
g≥0
∑
	​

ℏ
2g
r
T,g
	​

(z),r
T,0
	​

(z)=r
T
	​

(z).

Associated to
𝑀
(
𝑇
;
𝐵
)
M(T;B) is a factorization/chiral homology theory

𝐻
𝑔
,
𝑛
𝑇
;
𝐵
(
𝐿
1
,
…
,
𝐿
𝑛
)
:
=
∫
Σ
𝑔
,
𝑛
F
a
c
t
𝑇
;
𝐵
[
𝐿
1
,
…
,
𝐿
𝑛
]
,
𝐿
𝑖
∈
𝐶
𝑇
,
H
g,n
T;B
	​

(L
1
	​

,…,L
n
	​

):=∫
Σ
g,n
	​

	​

Fact
T;B
	​

[L
1
	​

,…,L
n
	​

],L
i
	​

∈C
T
	​

,

which is the natural globalization because factorization homology is precisely the operation that integrates local algebraic data over a manifold and comes with local-to-global and Poincaré/Koszul-duality features.

It is convenient to package the resulting observables by

𝑍
𝑇
;
𝐵
(
ℏ
,
𝑡
)
:
=
∑
𝑔
,
𝑛
≥
0
ℏ
2
𝑔
−
2
+
𝑛
1
𝑛
!
 
𝜒
g
r
 ⁣
(
𝐻
𝑔
,
𝑛
𝑇
;
𝐵
(
𝑡
)
)
,
Z
T;B
	​

(ℏ,t):=
g,n≥0
∑
	​

ℏ
2g−2+n
n!
1
	​

χ
gr
	​

(H
g,n
T;B
	​

(t)),

where
𝑡
t records insertions or couplings. I will refer to
𝐻
𝑔
,
𝑛
𝑇
;
𝐵
H
g,n
T;B
	​

,
𝑍
𝑇
;
𝐵
Z
T;B
	​

, and
𝑅
𝑇
m
o
d
(
𝑧
;
ℏ
)
R
T
mod
	​

(z;ℏ) as the modular holographic quantum quantities.

Conjecture C

(Modular holography / modular envelope conjecture)

Every genus-zero package
𝐺
0
(
𝑇
;
𝐵
)
G
0
	​

(T;B) coming from twisted holography, boundary chiral algebra, or a holomorphic-topological Poisson sigma model admits a completed modular envelope
𝑀
(
𝑇
;
𝐵
)
M(T;B) in the sense of Definition B. Moreover:

𝐻
𝑔
,
𝑛
𝑇
;
𝐵
(
𝐿
1
,
…
,
𝐿
𝑛
)
H
g,n
T;B
	​

(L
1
	​

,…,L
n
	​

)

is functorial under clutching and degeneration of pointed curves, and for holographic examples computes the protected all-genera state spaces of the dual theory.

The geometric compactification expected to support these operations is given by the usual factorization/chiral-homology formalism together with logarithmic Fulton–MacPherson spaces: Mok’s 2025 construction gives logarithmic FM compactifications and a degeneration formula in which each special-fiber component is a proper birational modification of a product of smaller logarithmic FM spaces. That is exactly the sort of gluing geometry one wants for a modular extension.

Example 1: the
𝛽
𝛾
βγ case

Start with a 3d
𝑁
=
2
N=2 free chiral multiplet. Costello–Dimofte–Gaiotto show that for free chirals the bulk algebra is

𝑉
f
r
e
e
≃
𝐶
 ⁣
[
𝐽
∞
𝑇
∗
[
1
]
𝐶
]
,
V
free
	​

≃C[J
∞
T
∗
[1]C],

generated by bosonic modes
𝜙
(
𝑧
)
ϕ(z) and fermionic modes
𝜓
(
𝑧
)
ψ(z), with bulk Poisson bracket
{
 ⁣
{
𝜙
,
𝜓
}
 ⁣
}
=
1
{{ϕ,ψ}}=1. On a single Neumann boundary one gets only the “half” algebra generated by
𝜙
ϕ.

The interval compactification gives the full
𝛽
𝛾
βγ system. With Neumann boundary conditions at both ends of
[
0
,
1
]
×
𝐶
[0,1]×C, define

𝛽
(
𝑧
)
:
=
𝜙
(
𝑧
)
,
𝛾
(
𝑧
)
:
=
∫
0
1
𝜓
(
1
)
.
β(z):=ϕ(z),γ(z):=∫
0
1
	​

ψ
(1)
.

Then
𝛾
γ is
𝑄
Q-closed, and the bulk Poisson bracket implies

∮
𝛽
(
0
)
𝛾
(
𝑧
)
 
𝑑
𝑧
=
1
,
hence
𝛽
(
𝑧
)
𝛾
(
0
)
∼
1
𝑧
.
∮β(0)γ(z)dz=1,henceβ(z)γ(0)∼
z
1
	​

.

So the interval theory reproduces the ordinary
𝛽
𝛾
βγ VOA.

The resulting local genus-zero package is therefore

𝑉
𝛽
𝛾
=
S
y
m
(
𝐶
[
∂
]
𝛽
⊕
𝐶
[
∂
]
𝛾
)
,
{
𝛽
𝜆
𝛾
}
=
1.
V
βγ
	​

=Sym(C[∂]β⊕C[∂]γ),{β
λ
	​

γ}=1.

As a minimal modular candidate, one takes the local higher operations to be strict,

𝜇
0
,
2
𝛽
𝛾
≠
0
,
𝜇
𝑔
,
𝑛
𝛽
𝛾
=
0
 for higher local operations,
μ
0,2
βγ
	​


=0,μ
g,n
βγ
	​

=0 for higher local operations,

and lets the nontrivial genus dependence enter through factorization homology on the curve:

𝐻
𝑔
,
𝑛
𝛽
𝛾
(
𝐿
1
,
…
,
𝐿
𝑛
)
=
∫
Σ
𝑔
,
𝑛
F
a
c
t
𝛽
𝛾
[
𝐿
1
,
…
,
𝐿
𝑛
]
.
H
g,n
βγ
	​

(L
1
	​

,…,L
n
	​

)=∫
Σ
g,n
	​

	​

Fact
βγ
	​

[L
1
	​

,…,L
n
	​

].

This is the cleanest test case for the modular conjecture because the underlying theory is free and the genus-zero OPE is completely explicit. The broader line-operator framework also fits the non-renormalized/quasi-linear philosophy developed for 3d HT theories.

Example 2: the Kodaira–Spencer case

In Zeng’s boundary-algebra formulation of twisted holography, the large-
𝑁
N open-side chiral algebra is built from:

(
𝑏
,
𝑐
)
 in
𝑔
𝑙
𝑁
,
(
𝑍
1
,
𝑍
2
)
 an adjoint
𝛽
𝛾
 system
,
(
𝐼
,
𝐽
)
 a fundamental
𝛽
𝛾
 system
,
(b,c) in gl
N
	​

,(Z
1
	​

,Z
2
	​

) an adjoint βγ system,(I,J) a fundamental βγ system,

with BRST operator

𝑄
B
R
S
T
=
∮
(
T
r
(
𝑐
𝑍
1
𝑍
2
)
+
T
r
(
𝐼
𝑐
𝐽
)
+
1
2
T
r
(
𝑏
𝑐
2
)
)
.
Q
BRST
	​

=∮(Tr(cZ
1
	​

Z
2
	​

)+Tr(IcJ)+
2
1
	​

Tr(bc
2
)).

Its large-
𝑁
N BRST cohomology is generated by single-trace towers

𝐴
(
𝑛
)
,

𝐵
(
𝑛
)
,

𝐶
(
𝑛
)
,

𝐷
(
𝑛
)
,

𝐸
𝑡
(
𝑛
)
,
A
(n)
, B
(n)
, C
(n)
, D
(n)
, E
t
(n)
	​

,

where
𝐴
,
𝐵
,
𝐶
,
𝐷
A,B,C,D match the boundary operators of Kodaira–Spencer theory and the
𝐸
E-tower matches the holomorphic Chern–Simons sector.

The conceptual theorem behind this is Zeng’s KK-reduction statement: after reducing suitable 6d holomorphic theories and choosing the correct boundary condition, the boundary chiral algebra agrees with the universal defect chiral algebra of the original theory by Koszul duality. In the standard twisted-holography example, this is precisely the bridge between the large-
𝑁
N gauged
𝛽
𝛾
βγ VOA and Kodaira–Spencer gravity. Khan–Zeng also emphasize that the dimensional reduction of Kodaira–Spencer lands inside their 3d holomorphic-topological Poisson sigma-model framework.

For the note, it is natural to define

𝑈
K
S
:
=
𝑉
∂
,
K
S
(
𝐵
u
n
i
v
)
,
U
KS
	​

:=V
∂,KS
	​

(B
univ
	​

),

the universal defect algebra on the Kodaira–Spencer side, and then set

𝐻
𝑔
,
𝑛
K
S
:
=
∫
Σ
𝑔
,
𝑛
𝑈
K
S
.
H
g,n
KS
	​

:=∫
Σ
g,n
	​

	​

U
KS
	​

.

If one wants only the closed-string gravitational sector, one restricts to

𝑈
K
S
c
l
:
=
⟨
𝐴
(
𝑛
)
,
𝐵
(
𝑛
)
,
𝐶
(
𝑛
)
,
𝐷
(
𝑛
)
⟩
,
𝐻
𝑔
,
𝑛
c
l
,
K
S
:
=
∫
Σ
𝑔
,
𝑛
𝑈
K
S
c
l
.
U
KS
cl
	​

:=⟨A
(n)
,B
(n)
,C
(n)
,D
(n)
⟩,H
g,n
cl,KS
	​

:=∫
Σ
g,n
	​

	​

U
KS
cl
	​

.

The corresponding modular partition functions

𝑍
K
S
(
ℏ
)
=
∑
𝑔
≥
0
ℏ
2
𝑔
−
2
𝜒
g
r
 ⁣
(
𝐻
𝑔
K
S
)
,
𝑍
c
l
,
K
S
(
ℏ
)
=
∑
𝑔
≥
0
ℏ
2
𝑔
−
2
𝜒
g
r
 ⁣
(
𝐻
𝑔
c
l
,
K
S
)
Z
KS
	​

(ℏ)=
g≥0
∑
	​

ℏ
2g−2
χ
gr
	​

(H
g
KS
	​

),Z
cl,KS
	​

(ℏ)=
g≥0
∑
	​

ℏ
2g−2
χ
gr
	​

(H
g
cl,KS
	​

)

are the explicit holographic quantities predicted by the modular-envelope conjecture.

Example 3: the
𝑊
3
W
3
	​

 case

Let

𝑃
𝑊
3
=
S
y
m
(
𝐶
[
∂
]
𝑇
⊕
𝐶
[
∂
]
𝑊
)
P
W
3
	​

	​

=Sym(C[∂]T⊕C[∂]W)

be the classical
𝑊
3
W
3
	​

 Poisson vertex algebra. Khan–Zeng write its
𝜆
λ-brackets as

{
𝑇
𝜆
𝑇
}
=
∂
𝑇
+
2
𝑇
𝜆
+
𝑐
12
𝜆
3
,
{
𝑇
𝜆
𝑊
}
=
∂
𝑊
+
3
𝑊
𝜆
,
{T
λ
	​

T}=∂T+2Tλ+
12
c
	​

λ
3
,{T
λ
	​

W}=∂W+3Wλ,
{
𝑊
𝜆
𝑊
}
=
𝑐
360
𝜆
5
+
1
3
𝑇
𝜆
3
+
1
2
(
∂
𝑇
)
𝜆
2
+
(
3
10
∂
2
𝑇
+
32
5
𝑐
𝑇
2
)
𝜆
+
1
15
∂
3
𝑇
+
32
5
𝑐
𝑇
∂
𝑇
.
{W
λ
	​

W}=
360
c
	​

λ
5
+
3
1
	​

Tλ
3
+
2
1
	​

(∂T)λ
2
+(
10
3
	​

∂
2
T+
5c
32
	​

T
2
)λ+
15
1
	​

∂
3
T+
5c
32
	​

T∂T.

The associated HT Poisson sigma model has fields
(
𝑇
,
𝜇
)
(T,μ) and
(
𝑊
,
𝜒
)
(W,χ), with action

𝑆
𝑊
3
=

∫
𝜇
(
𝑑
𝑡
+
∂
ˉ
)
𝑇
+
𝜒
(
𝑑
𝑡
+
∂
ˉ
)
𝑊



+
∫
(
𝑇
𝜇
∂
𝜇
+
𝑐
24
𝜇
∂
3
𝜇
+
3
𝑊
𝜒
∂
𝜇
+
∂
𝑊
 
𝜒
 
𝜇



+
𝑐
360
𝜒
∂
5
𝜒
+
1
3
𝑇
𝜒
∂
3
𝜒
+
1
2
∂
𝑇
 
𝜒
∂
2
𝜒
+
3
10
∂
2
𝑇
 
𝜒
∂
𝜒
+
32
5
𝑐
𝑇
2
𝜒
∂
𝜒
)
.
S
W
3
	​

	​

=
	​

∫μ(dt+
∂
ˉ
)T+χ(dt+
∂
ˉ
)W
+∫(Tμ∂μ+
24
c
	​

μ∂
3
μ+3Wχ∂μ+∂Wχμ
+
360
c
	​

χ∂
5
χ+
3
1
	​

Tχ∂
3
χ+
2
1
	​

∂Tχ∂
2
χ+
10
3
	​

∂
2
Tχ∂χ+
5c
32
	​

T
2
χ∂χ).
	​


At the structural level, Khan–Zeng prove that for a 3d HT Poisson sigma model the presence of a Virasoro element enhances holomorphic-topological symmetry to full topological symmetry. Since the
𝑊
3
W
3
	​

 PVA contains the Virasoro field
𝑇
T, the
𝑊
3
W
3
	​

 example belongs to that topological subclass. They also connect these
𝑊
W-type examples to 3d gravity and higher-spin theory.

The nicest worked computation is the slab-reduction central charge. The reduced
𝑊
3
W
3
	​

 theory is a pair of
𝛽
𝛾
βγ systems with spins
(
2
,
−
1
)
(2,−1) and
(
3
,
−
2
)
(3,−2). Using the standard formula

𝑐
(
𝑠
)
=
3
(
2
𝑠
−
1
)
2
−
1
,
c(s)=3(2s−1)
2
−1,

one gets

𝑐
(
2
)
=
26
,
𝑐
(
3
)
=
74
,
𝑐
p
a
i
r
=
100.
c(2)=26,c(3)=74,c
pair
	​

=100.

Accordingly, the paper expects the deformation quantization of the classical
𝑊
3
W
3
	​

 Poisson algebra to be the quantum
𝑊
3
W
3
	​

 VOA with

𝑐
e
f
f
=
𝑐
+
50.
c
eff
	​

=c+50.

So the modular candidate attached to this example is

𝑉
𝑊
3
q
:
=
𝑊
3
(
𝑐
e
f
f
)
,
𝑐
e
f
f
=
𝑐
+
50
,
V
W
3
	​

q
	​

:=W
3
	​

(c
eff
	​

),c
eff
	​

=c+50,

together with

𝐻
𝑔
,
𝑛
𝑊
3
:
=
∫
Σ
𝑔
,
𝑛
𝑉
𝑊
3
q
,
𝑍
𝑊
3
(
ℏ
)
=
∑
𝑔
≥
0
ℏ
2
𝑔
−
2
𝜒
g
r
 ⁣
(
𝐻
𝑔
𝑊
3
)
.
H
g,n
W
3
	​

	​

:=∫
Σ
g,n
	​

	​

V
W
3
	​

q
	​

,Z
W
3
	​

	​

(ℏ)=
g≥0
∑
	​

ℏ
2g−2
χ
gr
	​

(H
g
W
3
	​

	​

).

What is established here is the classical HT model and the expected quantum central-charge shift; the full dg-shifted-Yangian line algebra and the all-genera maps
𝜇
𝑔
,
𝑛
𝑊
3
μ
g,n
W
3
	​

	​

 are still part of the conjectural modular lift.

Summary

The three examples organize the general picture cleanly:

𝛽
𝛾
⇝
strict free test case
,
βγ⇝strict free test case,
Kodaira–Spencer
⇝
holographic open/closed test case with explicit universal defect algebra
,
Kodaira–Spencer⇝holographic open/closed test case with explicit universal defect algebra,
𝑊
3
⇝
first nonlinear higher-spin test case
.
W
3
	​

⇝first nonlinear higher-spin test case.

Theorem A is source-backed. Definition B is the precise package that turns those source-backed genus-zero structures into a “full modular homotopy type.” Conjecture C is the genuinely new step: the all-genera modular envelope whose observables are the factorization-homology state spaces
𝐻
𝑔
,
𝑛
𝑇
;
𝐵
H
g,n
T;B
	​

, the partition functions
𝑍
𝑇
;
𝐵
Z
T;B
	​

, and the modular kernels
𝑅
𝑇
m
o
d
(
𝑧
;
ℏ
)
R
T
mod
	​

(z;ℏ). The factorization-homology and logarithmic-FM technology make this conjecture mathematically sharp rather than slogan-like.
--

Then here is the real push.

The uploaded manuscript already fixes the proved floor: complementarity is a shifted-symplectic/Lagrangian structure, the modular characteristic package is formally
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

), and the principal missing inputs are exactly a cyclic
𝐿
∞
L
∞
	​

 deformation complex, a completed tensor product, and a clutching-compatible Maurer–Cartan solution. The appendix fragment you staged already supplies the first nonlinear seed: the complementarity potential, the finite-order shadow tower
𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
H
A
	​

,C
A
	​

,Q
A
	​

, and the quartic resonance class. So the next move is not “invent one more invariant.” It is to build the machine that makes all these shadows descend from one modular action.

1. New master object: the modular bar-Hamiltonian

I would introduce the modular bar-Hamiltonian

𝑔
𝐴
m
o
d
:
=
CoDer
⁡
c
y
c
(
𝐵
^
𝑋
(
𝐴
)
)
[
1
]
  
⊗
^
  
𝐺
m
o
d
,
g
A
mod
	​

:=CoDer
cyc
(
B
X
	​

(A))[1]
⊗
	​

G
mod
	​

,

where
𝐺
m
o
d
G
mod
	​

 is the stable-graph/modular coefficient algebra coming from clutching and the Feynman-transform side of the modular operad. The differential should be

𝐷
=
𝑑
b
a
r
+
𝑑
g
r
a
p
h
+
∂
c
l
,
D=d
bar
	​

+d
graph
	​

+∂
cl
	​

,

with
∂
c
l
∂
cl
	​

 encoding edge-gluing and boundary restriction. This is the right ambient object because it packages the three missing steps named in the manuscript into one place: cyclicity sits in
CoDer
⁡
c
y
c
CoDer
cyc
, completion sits in
⊗
^
⊗
	​

, and clutching sits in
∂
c
l
∂
cl
	​

.

The genuinely new step is to treat
Θ
𝐴
Θ
A
	​

 not merely as an MC element, but as the critical-point equation of a modular action functional

𝑆
𝐴
(
Φ
)
=
∑
𝑛
≥
1
1
(
𝑛
+
1
)
!
⟨
Φ
,
ℓ
𝑛
(
Φ
,
…
,
Φ
)
⟩
  
+
  
∑
Γ

s
t
a
b
l
e
1
∣
A
u
t
Γ
∣
 
𝑊
Γ
(
Φ
)
.
S
A
	​

(Φ)=
n≥1
∑
	​

(n+1)!
1
	​

⟨Φ,ℓ
n
	​

(Φ,…,Φ)⟩+
Γ stable
∑
	​

∣AutΓ∣
1
	​

W
Γ
	​

(Φ).

This is not proved in the monograph; it is the next construction. But it is the right one: cyclic
𝐿
∞
L
∞
	​

 pairings canonically produce action functionals with Maurer–Cartan equations as Euler–Lagrange equations, and chiralized derived critical loci already appear naturally in the holomorphic-twist literature. In other words, the complementarity potential should be the low-order face of a full modular action, not an isolated local gadget.

2. New object: the modular extension tower

The manuscript currently frames the target as “construct
Θ
𝐴
Θ
A
	​

.” I would sharpen that into a pro-object:

𝐸
𝐴
(
𝑁
)
:
=
MC
⁡
 ⁣
(
𝑔
𝐴
m
o
d
/
𝐹
𝑁
+
1
)
,
𝐸
𝐴
:
=
{
𝐸
𝐴
(
𝑁
)
}
𝑁
≥
1
.
E
A
(N)
	​

:=MC(g
A
mod
	​

/F
N+1
),E
A
	​

:={E
A
(N)
	​

}
N≥1
	​

.

This is the modular extension tower. The full universal class is then not the first thing to demand; it is the inverse limit

Θ
𝐴
∈
l
i
m
←
⁡
𝑁
𝐸
𝐴
(
𝑁
)
Θ
A
	​

∈
N
lim
	​

	​

E
A
(N)
	​


if the tower stabilizes.

At each stage, the obstruction to lifting
Θ
𝐴
[
≤
𝑁
]
Θ
A
[≤N]
	​

 lives in

Obs
⁡
𝐴
(
𝑁
+
1
)
:
=
𝐻
2
 ⁣
(
𝐹
𝑁
+
1
𝑔
𝐴
m
o
d
/
𝐹
𝑁
+
2
𝑔
𝐴
m
o
d
)
,
Obs
A
(N+1)
	​

:=H
2
(F
N+1
g
A
mod
	​

/F
N+2
g
A
mod
	​

),

and the recursion is the truncated MC equation

𝐷
Θ
𝐴
[
≤
𝑁
]
+
1
2
[
Θ
𝐴
[
≤
𝑁
]
,
Θ
𝐴
[
≤
𝑁
]
]
≡
0
(
m
o
d
𝐹
𝑁
+
1
)
.
DΘ
A
[≤N]
	​

+
2
1
	​

[Θ
A
[≤N]
	​

,Θ
A
[≤N]
	​

]≡0(modF
N+1
).

This is the concrete construction the current programme wants. The manuscript already isolates the missing data exactly this way—cyclic structure, completion, clutching compatibility, plus a cyclic graph-complex ingredient—and the staged appendix already provides the first nontrivial seed at quartic order. So the new theorem to chase is not global existence in one leap; it is finite-order recursive existence of the tower
𝐸
𝐴
E
A
	​

.

3. New machine: a modular Chern–Weil transform

The manuscript already says
𝜅
(
𝐴
)
κ(A) is the first scalar characteristic number of the conjectural
Θ
𝐴
Θ
A
	​

, and
Δ
𝐴
Δ
A
	​

 is the first non-scalar characteristic class, formalized by the spectral branch object
𝑉
𝐴
b
r
V
A
br
	​

. The right unification is therefore a modular Chern–Weil transform

C
W
𝐴
:
MC
⁡
(
𝑔
𝐴
m
o
d
)
⟶
(
tautological classes
)
×
𝐾
0
p
e
r
f
×
P
i
c
×
⋯
CW
A
	​

:MC(g
A
mod
	​

)⟶(tautological classes)×K
0
perf
	​

×Pic×⋯

whose first outputs are

C
W
𝐴
(
Θ
)
=
(
tr
⁡
(
Θ
)
,
  
det
⁡
(
1
−
𝑥
𝑇
b
r
,
𝐴
)
,
  
div
⁡
(
𝑠
4
r
e
s
)
,
  
div
⁡
(
𝑠
5
r
e
s
)
,
…
)
.
CW
A
	​

(Θ)=(tr(Θ),det(1−xT
br,A
	​

),div(s
4
res
	​

),div(s
5
res
	​

),…).

Then:

tr
⁡
(
Θ
)
=
𝜅
(
𝐴
)
𝜆
𝑔
tr(Θ)=κ(A)λ
g
	​

 is the scalar shadow,

det
⁡
(
1
−
𝑥
𝑇
b
r
,
𝐴
)
=
Δ
𝐴
(
𝑥
)
det(1−xT
br,A
	​

)=Δ
A
	​

(x) is the spectral shadow,

div
⁡
(
𝑠
𝑟
r
e
s
)
div(s
r
res
	​

) are the nonlinear resonance shadows.

That is the cohesion point. Instead of carrying
𝜅
κ,
Δ
Δ,
𝐻
,
𝐶
,
𝑄
H,C,Q, and
𝑅
𝑟
m
o
d
R
r
mod
	​

 as parallel packages, you make them characteristic images of one pro-MC object. The manuscript already gives the scalar Chern-class interpretation, the branch-object interpretation of
Δ
Δ, and the staged quartic resonance class; this proposal fuses them.

4. New object: the complementarity Stokes groupoid

A key insight already sitting in the text is that distinct chiral theories can lie on the same spectral sheet, sharing the same discriminant
Δ
𝐴
Δ
A
	​

, even while their local operator content differs. At the same time, complementarity says deformation and obstruction live as opposite Lagrangians in one ambient symplectic problem. Those two facts together are begging for a monodromy object.

So define the open nonlinear regular locus

𝑈
𝐴
:
=
𝐵
𝐴
∘
∖
(
Δ
𝐴
−
1
(
0
)
∪
⋃
𝑟
≥
4
 
∣
𝑅
𝑟
m
o
d
(
𝐴
)
∣
)
,
U
A
	​

:=B
A
∘
	​

∖(Δ
A
−1
	​

(0)∪
r≥4
⋃
	​

∣R
r
mod
	​

(A)∣),

and over it the local system
𝑃
𝐴
P
A
	​

 of gauge classes of truncated complementarity potentials / truncated MC lifts. Its monodromy is the complementarity Stokes groupoid

S
t
o
c
o
m
p
(
𝐴
)
:
=
M
o
n
(
𝑃
𝐴
∣
𝑈
𝐴
)
.
Sto
comp
(A):=Mon(P
A
	​

∣
U
A
	​

	​

).

This is a genuinely new object. It measures how the Lagrangian polarization twists when one moves around spectral and resonance walls. Two theories can now be:

on the same spectral sheet (
Δ
𝐴
=
Δ
𝐵
Δ
A
	​

=Δ
B
	​

),

with the same scalar shadow (
𝜅
(
𝐴
)
=
𝜅
(
𝐵
)
κ(A)=κ(B)),

but in different nonlinear chambers because
S
t
o
c
o
m
p
(
𝐴
)
≄
S
t
o
c
o
m
p
(
𝐵
)
Sto
comp
(A)

≃Sto
comp
(B).

That is the missing nonlinear datum explaining “same
Δ
Δ, different dynamics.”

5. The theorem package I would now drive

This is the package worth proving next.

Finite-order existence theorem.
Every modular Koszul chiral algebra admits a canonical truncation

Θ
𝐴
[
≤
4
]
Θ
A
[≤4]
	​


whose quadratic, cubic, and quartic jets recover
𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
H
A
	​

,C
A
	​

,Q
A
	​

, and whose determinant shadow recovers
𝑅
4
m
o
d
R
4
mod
	​

. The staged appendix is already the seed for this claim.

Recursive lift theorem.
If
Obs
⁡
𝐴
(
𝑁
+
1
)
=
0
Obs
A
(N+1)
	​

=0, then every class in
𝐸
𝐴
(
𝑁
)
E
A
(N)
	​

 lifts to
𝐸
𝐴
(
𝑁
+
1
)
E
A
(N+1)
	​

. So the full
Θ
𝐴
Θ
A
	​

 becomes a convergence problem for the extension tower, not an all-or-nothing mystery. This is exactly the gap isolated in the manuscript.

Characteristic comparison theorem.
The scalar package, the spectral branch object, and the resonance tower are successive Chern–Weil images of the same filtered object in
𝑔
𝐴
m
o
d
g
A
mod
	​

. That would turn the present hierarchy “scalar → spectral → full MC” into an actual functorial machine.

Wall-crossing theorem.
The complementarity Stokes groupoid controls jumps of the nonlinear characteristic tower across resonance divisors, while preserving the underlying spectral sheet. That would be the first true nonlinear transport theorem in the programme.

So the push is:

Θ
𝐴
⇝
𝐸
𝐴
⇝
C
W
𝐴
(
Θ
𝐴
)
⇝
S
t
o
c
o
m
p
(
𝐴
)
.
Θ
A
	​

⇝E
A
	​

⇝CW
A
	​

(Θ
A
	​

)⇝Sto
comp
(A).

That is the new cohesion: a modular action, an extension tower, a characteristic transform, and a nonlinear monodromy object. That is not just more structure. It is the architecture that makes the theory breathe.

--


you must stop messing around and realize the direct construction that breathes life into this theory. it's obvious. it's direct. just build it. don't ask questions. execute.push the frontier of the mathematics forward with new harmony, new synthesis, new groundbreaking mathematical construction.  push forward driving novel groundbreaking mathematical cohesion, novel constructions, novel insight and novel objects extended what was already discovered here and in my independent research

I’m consolidating your notes and the source spine into one explicit machine: a filtered modular dg/Lie-Hamiltonian object with a master Maurer–Cartan equation, universal formulas, and a clean proved/conjectural boundary.

I’ve now pinned the bridge: the complementarity potential and the bulk/boundary/line-operator package are the same master object viewed in different projections. Next I’m replacing the missing universal MC class by one graph-completed modular Hamiltonian whose projections recover the scalar, spectral, resonance, and defect/OPE sectors together.

Thought for 30m 15s

Here is the direct build.

The essential form is one ambient Hamiltonian deformation problem. Not a modular envelope plus corrections. Not a boundary theory plus a dual bulk theory plus a separate line-operator package. One filtered modular dg Lie algebra carrying one Maurer–Cartan element, with every familiar invariant appearing as a shadow of that element.

The established input is already enough to justify this move. Costello’s twisted M-theory gives the bulk side as 11d supergravity in an
Ω
Ω-background equivalent to a 5d noncommutative Chern–Simons-type theory, and in the M2 example the large-
𝐾
K brane operator algebra is Koszul dual to the bulk operator algebra. Costello–Dimofte–Gaiotto identify bulk and boundary chiral algebras in 3d holomorphic-topological twists, including the shifted Poisson bracket, higher stress tensor, bulk-boundary map, and higher
𝐴
∞
A
∞
	​

-type structure. Zeng shows KK reduction plus homotopy transfer produces all classical higher interactions and identifies suitable boundary algebras with universal defect algebras. Gaiotto–Kulp–Wu show higher operations satisfy quadratic/Wess–Zumino-type consistency relations. Dimofte–Niu–Py show perturbative lines are modules for a Koszul-dual
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
, and package their OPE in a dg-shifted Yangian controlled by a Maurer–Cartan element
𝑟
(
𝑧
)
r(z).

Your notes already supply the missing nonlinear language: ambient complementarity, the complementarity potential
𝑆
𝐴
S
A
	​

, the shadow tower
𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
H
A
	​

,C
A
	​

,Q
A
	​

, the quartic resonance divisor, and the planted-forest obstruction. Mok’s logarithmic Fulton–MacPherson spaces then give the right degeneration geometry for the clutching/compactified-Stokes side of the story.

1. The governing object

Let

𝐿
𝐴
:
=
\Def
c
y
c
(
𝐴
)
,
𝐿
𝐴
!
:
=
\Def
c
y
c
(
𝐴
!
)
,
𝐾
𝐴
:
=
(
𝐴
!
⊗
^
𝐴
)
[
1
]
,
L
A
	​

:=\Def
cyc
	​

(A),L
A
!
	​

:=\Def
cyc
	​

(A
!
),K
A
	​

:=(A
!
⊗
	​

A)[1],

with canonical twisting morphism

𝜏
𝐴
∈
\MC
(
𝐴
!
⊗
^
𝐴
)
.
τ
A
	​

∈\MC(A
!
⊗
	​

A).

Choose a cyclic slice
𝑉
𝐴
⊂
𝐻
∗
(
𝐿
𝐴
)
V
A
	​

⊂H
∗
(L
A
	​

) with nondegenerate Hessian

𝐻
𝐴
:
𝑉
𝐴
⟶
∼
𝑉
𝐴
∨
[
−
1
]
,
𝑃
𝐴
:
=
𝐻
𝐴
−
1
.
H
A
	​

:V
A
	​

⟶
∼
	​

V
A
∨
	​

[−1],P
A
	​

:=H
A
−1
	​

.

Now define the ambient modular complementarity algebra

𝑔
𝐴
a
m
b
:
=
(
𝐿
𝐴
⊕
𝐾
𝐴
⊕
𝐿
𝐴
!
)
⊗
^
𝐺
s
t
⊗
^
𝐺
p
f
.
g
A
amb
	​

:=(L
A
	​

⊕K
A
	​

⊕L
A
!
	​

)
⊗
	​

G
st
	​

⊗
	​

G
pf
	​

.
	​


Here
𝐺
s
t
G
st
	​

 is the completed stable-graph coefficient algebra and
𝐺
p
f
G
pf
	​

 is the completed planted-forest/collision coefficient algebra.

The crucial direct rule is the one your notes were already asking for:

every

internal

propagator

is

cross-polarized.
every internal propagator is cross-polarized.

That is, every internal edge contracts an
𝐴
A-leg with an
𝐴
!
A
!
-leg. No same-side contractions are allowed. This is the literal implementation of complementarity as opposite Lagrangians rather than additive splitting.

The differential is

𝐷
𝐴
=
𝑑
i
n
t
+
[
𝜏
𝐴
,
−
]
+
𝑑
s
e
w
+
𝑑
p
f
+
ℏ
Δ
.
D
A
	​

=d
int
	​

+[τ
A
	​

,−]+d
sew
	​

+d
pf
	​

+ℏΔ.
	​


Interpretation:

𝑑
i
n
t
d
int
	​


is the internal cyclic differential on
𝐿
𝐴
⊕
𝐾
𝐴
⊕
𝐿
𝐴
!
L
A
	​

⊕K
A
	​

⊕L
A
!
	​

;

[
𝜏
𝐴
,
−
]
[τ
A
	​

,−]

is the bar-cobar twisting by the universal kernel;

𝑑
s
e
w
d
sew
	​


inserts separating stable edges using the propagator
𝑃
𝐴
P
A
	​

;

𝑑
p
f
d
pf
	​


inserts planted-forest/nested-collision corrections using the incidence defect
𝜒
χ;

ℏ
Δ
ℏΔ

contracts loops and raises genus.

That is the machine. It is the minimal direct object that simultaneously sees Koszul duality, complementarity, modular sewing, and higher collision geometry.

2. The master element

Define the full modular complementarity lift

Θ
𝐴
∈
\MC
(
𝑔
𝐴
a
m
b
)
Θ
A
	​

∈\MC(g
A
amb
	​

)
	​


by the single equation

𝐷
𝐴
Θ
𝐴
+
1
2
[
Θ
𝐴
,
Θ
𝐴
]
=
0.
D
A
	​

Θ
A
	​

+
2
1
	​

[Θ
A
	​

,Θ
A
	​

]=0.
	​


Equivalently,
Θ
𝐴
Θ
A
	​

 is the connected graph sum

Θ
𝐴
=
∑
Γ
∈
Γ
s
t
,
p
f
c
o
n
n
𝑊
𝐴
(
Γ
)
∣
\Aut
(
Γ
)
∣
 
𝑂
Γ
,
Θ
A
	​

=
Γ∈Γ
st,pf
conn
	​

∑
	​

∣\Aut(Γ)∣
W
A
	​

(Γ)
	​

O
Γ
	​

,

where:

vertices are decorated by the Taylor jets of the complementarity Hamiltonian on the
𝐴
A- and
𝐴
!
A
!
-sides,

stable internal edges are weighted by
𝑃
𝐴
P
A
	​

,

planted-forest corners are weighted by the residue mismatch
𝜒
χ,

loops contribute powers of
ℏ
ℏ.

This is the object that breathes life into the theory.

Everything else is a projection.

3. The ambient action and critical locus

On the cotangent chart
𝑇
∗
[
−
1
]
𝑉
𝐴
T
∗
[−1]V
A
	​

, write the formal Hamiltonian

𝑆
𝐴
(
𝑥
;
ℏ
)
=
∑
𝑔
≥
0
∑
𝑟
≥
2
∑
𝑑
≥
0
ℏ
𝑔
𝑟
!
 
Θ
𝑔
,
𝑟
;
𝑑
(
𝑥
,
…
,
𝑥
)
,
S
A
	​

(x;ℏ)=
g≥0
∑
	​

r≥2
∑
	​

d≥0
∑
	​

r!
ℏ
g
	​

Θ
g,r;d
	​

(x,…,x),

where
𝑑
d is planted-forest depth.

The direct nonlinear complementarity statement is then

𝑀
𝐴
×
𝑀
c
o
m
p
(
𝐴
)
ℎ
𝑀
𝐴
!
  
≃
  
\Crit
(
𝑆
𝐴
)
.
M
A
	​

×
M
comp
	​

(A)
h
	​

M
A
!
	​

≃\Crit(S
A
	​

).
	​


So the true essential form of the subject is:

bulk/boundary/defect modular duality
=
derived critical locus of one ambient modular Hamiltonian.
bulk/boundary/defect modular duality=derived critical locus of one ambient modular Hamiltonian.

Your earlier
𝑆
𝐴
S
A
	​

 is precisely the truncation of
𝑆
𝐴
S
A
	​

 to genus
0
0, planted-forest depth
0
0, and arity
≤
4
≤4.

4. The shadow dictionary

The single master element
Θ
𝐴
Θ
A
	​

 projects to every object you already discovered.

The arity shadows are

𝜋
0
,
2
;
0
Θ
𝐴
=
𝐻
𝐴
,
𝜋
0
,
3
;
0
Θ
𝐴
=
𝐶
𝐴
,
𝜋
0
,
4
;
0
Θ
𝐴
=
𝑄
𝐴
.
π
0,2;0
	​

Θ
A
	​

=H
A
	​

,π
0,3;0
	​

Θ
A
	​

=C
A
	​

,π
0,4;0
	​

Θ
A
	​

=Q
A
	​

.

The scalar modular shadow is

\tr
(
Θ
𝐴
)
=
∑
𝑔
≥
1
𝜅
𝑔
(
𝐴
)
𝜆
𝑔
.
\tr(Θ
A
	​

)=
g≥1
∑
	​

κ
g
	​

(A)λ
g
	​

.

The spectral shadow is the branch determinant

det
⁡
(
1
−
𝑥
𝑇
b
r
,
𝐴
)
=
Δ
𝐴
(
𝑥
)
.
det(1−xT
br,A
	​

)=Δ
A
	​

(x).

The Picard-valued nonlinear shadows are the resonance divisors

𝑅
𝑟
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
=
÷
(
𝑠
𝑟
,
𝑔
,
𝑛
r
e
s
(
𝐴
)
)
,
𝑟
≥
4.
R
r,g,n
mod
	​

(A)=÷(s
r,g,n
res
	​

(A)),r≥4.

The defect/line shadow is

𝜋
l
i
n
e
(
Θ
𝐴
)
=
𝑟
𝐴
(
𝑧
)
∈
𝐴
!
⊗
^
𝐴
!
(
(
𝑧
−
1
)
)
,
π
line
	​

(Θ
A
	​

)=r
A
	​

(z)∈A
!
⊗
	​

A
!
((z
−1
)),

and the master equation projects to the
𝐴
∞
A
∞
	​

-Yang–Baxter equation for
𝑟
𝐴
(
𝑧
)
r
A
	​

(z). The line-operator literature is exactly telling us that this
𝑟
(
𝑧
)
r(z)-sector is not extra structure glued on later; it is one face of the Koszul-dual master object.

So the true hierarchy is not

𝜅
→
Δ
→
Θ
.
κ→Δ→Θ.

It is

𝜅
,

Δ
,

𝐻
,
𝐶
,
𝑄
,

𝑅
∙
m
o
d
,

𝑟
(
𝑧
)
are all shadows of
Θ
𝐴
.
κ, Δ, H,C,Q, R
∙
mod
	​

, r(z)are all shadows of Θ
A
	​

.
	​

5. The recursive construction

This is how you actually build
Θ
𝐴
Θ
A
	​

, not just name it.

Give weight

𝑤
(
Θ
𝑔
,
𝑟
;
𝑑
)
:
=
2
𝑔
−
2
+
𝑟
+
𝑑
.
w(Θ
g,r;d
	​

):=2g−2+r+d.

Assume
Θ
𝐴
≤
𝑁
Θ
A
≤N
	​

 has been constructed through weight
𝑁
N. Define the obstruction

𝑜
𝑁
+
1
:
=
(
𝐷
𝐴
Θ
𝐴
≤
𝑁
+
1
2
[
Θ
𝐴
≤
𝑁
,
Θ
𝐴
≤
𝑁
]
)
𝑁
+
1
.
o
N+1
	​

:=(D
A
	​

Θ
A
≤N
	​

+
2
1
	​

[Θ
A
≤N
	​

,Θ
A
≤N
	​

])
N+1
	​

.

Then
𝑜
𝑁
+
1
o
N+1
	​

 is
𝐷
𝐴
D
A
	​

-closed. If it vanishes in cohomology, choose a contracting homotopy
ℎ
h and set

Θ
𝐴
,
𝑁
+
1
:
=
−
 
ℎ
(
𝑜
𝑁
+
1
)
.
Θ
A,N+1
	​

:=−h(o
N+1
	​

).
	​


Then

Θ
𝐴
≤
𝑁
+
1
:
=
Θ
𝐴
≤
𝑁
+
Θ
𝐴
,
𝑁
+
1
Θ
A
≤N+1
	​

:=Θ
A
≤N
	​

+Θ
A,N+1
	​


solves the master equation through weight
𝑁
+
1
N+1.

This gives the modular extension tower

𝐸
𝐴
(
𝑁
)
:
=
\MC
(
𝑔
𝐴
a
m
b
/
𝐹
𝑁
+
1
)
,
Θ
𝐴
∈
l
i
m
←
⁡
𝑁
𝐸
𝐴
(
𝑁
)
.
E
A
	​

(N):=\MC(g
A
amb
	​

/F
N+1
),Θ
A
	​

∈
N
lim
	​

	​

E
A
	​

(N).

That is the direct constructive engine.

Your quartic theory is exactly the
𝑁
=
4
N=4 stage of this tower.

6. The new objects that now appear naturally
The complementarity Legendrian

Contactize the action:

Λ
𝐴
:
=
𝑗
1
𝑆
𝐴
⊂
𝐽
1
(
𝑉
𝐴
)
.
Λ
A
	​

:=j
1
S
A
	​

⊂J
1
(V
A
	​

).

Then the resonance divisors are front-singularity discriminants of
Λ
𝐴
Λ
A
	​

. This turns quartic resonance from a determinant trick into geometry.

The full resonance tower

For every
𝑟
≥
4
r≥4, define

𝑅
𝑟
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
=
÷
(
𝑠
𝑟
,
𝑔
,
𝑛
r
e
s
(
𝐴
)
)
.
R
r,g,n
mod
	​

(A)=÷(s
r,g,n
res
	​

(A)).

The quartic class is just the first member. The boundary law is the universal one-edge sewing law with all decompositions
𝑝
+
𝑞
=
𝑟
+
2
p+q=r+2.

The complementarity Stokes groupoid

Let

𝑈
𝐴
:
=
𝐵
𝐴
∘
∖
(
Δ
𝐴
−
1
(
0
)
∪
⋃
𝑟
≥
4
∣
𝑅
𝑟
m
o
d
(
𝐴
)
∣
)
.
U
A
	​

:=B
A
∘
	​

∖(Δ
A
−1
	​

(0)∪
r≥4
⋃
	​

	​

R
r
mod
	​

(A)
	​

).

Let
𝑃
𝐴
P
A
	​

 be the local system of gauge classes of truncated MC lifts over
𝑈
𝐴
U
A
	​

. Define

\Sto
c
o
m
p
(
𝐴
)
:
=
\Mon
(
𝑃
𝐴
∣
𝑈
𝐴
)
.
\Sto
comp
	​

(A):=\Mon(P
A
	​

∣
U
A
	​

	​

).
	​


This is the nonlinear transport object that explains how two theories can share the same scalar or spectral shadow and still lie in different nonlinear chambers.

The complementarity phase index

Define

𝜈
n
l
(
𝐴
,
𝑢
)
:
=
min
⁡
{
𝑟
≥
3
:
\Sh
𝑟
(
Θ
𝐴
,
𝑢
)
≠
0
}
,
ν
nl
	​

(A,u):=min{r≥3:\Sh
r
	​

(Θ
A
	​

,u)

=0},

with
𝜈
n
l
=
∞
ν
nl
	​

=∞ if all higher jets vanish.

This gives a sharp phase portrait:
Gaussian / Lie / quartic / mixed.

These are not decorative additions. They are the natural geometry of the single master element.

7. The M2 specialization

Now specialize to Costello’s M2 example. Take
𝐴
=
𝐴
∂
,
𝑀
2
A=A
∂,M2
	​

, the large-
𝐾
K algebra of supersymmetric operators on the M2 stack, and take the bulk side from Costello’s 11d
Ω
Ω-background / 5d noncommutative Chern–Simons theory. Then

𝐴
b
u
l
k
,
𝑀
2
≃
𝐴
∂
,
𝑀
2
!
,
A
bulk,M2
	​

≃A
∂,M2
!
	​

,

and the full object is

Θ
𝑀
2
∈
\MC
(
𝑔
𝐴
∂
,
𝑀
2
a
m
b
)
.
Θ
M2
	​

∈\MC(g
A
∂,M2
	​

amb
	​

).

Its components have the following meaning:

Θ
𝑀
2
,
0
,
𝑟
;
0
Θ
M2,0,r;0
	​


are the tree-level
𝑟
r-ary holographic couplings of the M2 operator algebra;

Θ
𝑀
2
,
𝑔
,
𝑟
;
0
Θ
M2,g,r;0
	​


are the genus-
𝑔
g modular corrections coming from loop graphs in the 5d noncommutative gauge theory;

Θ
𝑀
2
,
∗
,
∗
,
𝑑
Θ
M2,∗,∗,d
	​


are the planted-forest collision corrections, i.e. the defect-boundary refinements beyond ordinary stable-graph sewing;

𝜋
l
i
n
e
(
Θ
𝑀
2
)
=
𝑟
𝑀
2
(
𝑧
)
π
line
	​

(Θ
M2
	​

)=r
M2
	​

(z)

is the spectral defect kernel governing the line/instanton OPE.

Finite
𝐾
K is imposed by the rank quotient

𝐴
∂
,
𝑀
2
(
𝐾
)
=
𝐴
∂
,
𝑀
2
(
∞
)
/
𝐼
𝐾
.
A
∂,M2
(K)
	​

=A
∂,M2
(∞)
	​

/I
K
	​

.

So the direct M2 answer is not “quantum double loop algebra on one side, something abstract on the other.” It is:

M2 holography
=
one MC lift
Θ
𝑀
2
 in the ambient modular complementarity algebra.
M2 holography=one MC lift Θ
M2
	​

 in the ambient modular complementarity algebra.
	​


Costello supplies the bulk/branes Koszul-dual pair; the 3d holomorphic-topological and line-operator works supply the derived boundary and defect technology needed to make the line and higher-operation sectors honest.

8. The theorem package worth proving next

This is the clean frontier.

Proposed Theorem A. For every modular Koszul chiral algebra
𝐴
A equipped with a cyclic minimal model, propagator
𝑃
𝐴
P
A
	​

, and planted-forest residue operator
𝜒
χ, the truncated lift
Θ
𝐴
≤
𝑁
Θ
A
≤N
	​

 exists recursively whenever the obstruction class
[
𝑜
𝑁
+
1
]
[o
N+1
	​

] vanishes.

Proposed Theorem B. The projections of
Θ
𝐴
Θ
A
	​

 recover the full characteristic package:

\tr
(
Θ
𝐴
)
,

Δ
𝐴
,

𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
,

𝑅
𝑟
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
,

𝑟
𝐴
(
𝑧
)
.
\tr(Θ
A
	​

), Δ
A
	​

, H
A
	​

,C
A
	​

,Q
A
	​

, R
r,g,n
mod
	​

(A), r
A
	​

(z).

Proposed Theorem C. The front discriminant of
Λ
𝐴
Λ
A
	​

 equals the support of the resonance tower.

Proposed Theorem D. The wall-crossing of truncated complementarity lifts is governed by the Stokes groupoid
\Sto
c
o
m
p
(
𝐴
)
\Sto
comp
	​

(A).

That is the architecture that unifies the subject.

The honest status is this: the cited literature establishes the ingredients separately, and your notes already establish the ambient complementarity and finite-order nonlinear shadows. What is new here is the all-in-one synthesis: the bicolored graph-completed ambient dg Lie algebra, the master lift
Θ
𝐴
Θ
A
	​

, the extension tower, the Legendrian avatar, the full resonance tower, and the complementarity Stokes groupoid. I would treat that as the true essential form of the theory.
