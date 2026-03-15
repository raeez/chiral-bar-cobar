
express the true form of the subject via direct construction of "modular homotopy theory"

I’m treating “modular” in the modular-operad sense and grounding a direct construction in the uploaded operad, chiral, factorization, and deformation references, checking where those structures align via Koszul duality.

The picture is tightening into a single construction: tree-level operadic homotopy is completed to loops and genus by stable graphs and the Feynman transform, with Maurer–Cartan/L∞ deformation data and the chiral upgrade on the Ran space supplying the global gluing layer.

Thought for 22m 10s

By “modular homotopy theory” I would take the phrase in its mathematically sharp sense to mean:

the higher-genus homotopy theory of chiral/factorization objects, obtained by replacing tree-level operadic geometry with the modular operad of stable curves, and replacing ordinary bar–cobar/Koszul duality with its Feynman-transform, factorization-theoretic form. This is the natural synthesis of modular operads and the Feynman transform (Getzler–Kapranov), chiral/factorization Koszul duality on the Ran space (Francis–Gaitsgory), and Poincaré/Koszul duality for factorization homology (Ayala–Francis).

A direct construction is then:

1. Start with factorization data on a curve.
Let
𝑋
X be a smooth curve, and let
F
a
c
t
(
𝑋
)
Fact(X) denote the
∞
∞-category of factorization algebras on
R
a
n
(
𝑋
)
Ran(X). Francis–Gaitsgory show that chiral/factorization structures admit a genuine homotopy theory, analogous to Quillen’s deformation-theoretic framework, and that their relation is a form of Koszul duality.

2. Replace trees by stable graphs.
Let
𝑀
m
o
d
=
{
𝑀
‾
𝑔
,
𝑛
}
2
𝑔
−
2
+
𝑛
>
0
M
mod
	​

={
M
g,n
	​

}
2g−2+n>0
	​

 be the modular operad of stable pointed curves. Getzler–Kapranov’s key point is that modular operads are the “higher-genus” analogue of operads, and their Feynman transform is the higher-genus analogue of both graph complexes and the bar construction.

3. Define the modular bar object.
For a factorization/chiral object
𝐹
F, define

𝐵
𝑋
m
o
d
(
𝐹
)
  
:
=
  
F
T
𝑀
m
o
d
(
𝐹
)
.
B
X
mod
	​

(F):=FT
M
mod
	​

	​

(F).

Concretely, this is a genus-graded object built from stable graphs
Γ
Γ: each vertex is decorated by a local operation of
𝐹
F, and each internal edge is a propagator/homotopy kernel. This is exactly the modular replacement of the ordinary bar complex.

4. Put the differential on it.
The differential is the sum of:

the internal differential of
𝐹
F,

edge-contraction terms,

vertex-splitting / self-gluing terms coming from the boundary stratification of
𝑀
‾
𝑔
,
𝑛
M
g,n
	​

.

The point is that
𝑑
2
=
0
d
2
=0 is now enforced by the modular operad axioms, just as ordinary bar differentials square to zero because operadic boundary-of-boundary vanishes. In other words, genus is no longer decoration; it enters the differential itself.

5. Define the modular cobar object and the homotopy theory.
Form the adjoint cobar functor

Ω
𝑋
m
o
d
.
Ω
X
mod
	​

.

Then the homotopy theory is obtained by localizing curved/factorization objects with respect to the equivalences detected by this bar–cobar pair. On the Koszul locus, this is the higher-genus refinement of ordinary bar–cobar duality; in the topological
𝐸
𝑛
E
n
	​

 direction, it matches the Poincaré/Koszul pattern of factorization homology.

6. Package the genus tower by Maurer–Cartan theory.
The right deformation variable is a universal Maurer–Cartan element

Θ
𝐹
∈
M
C
(
D
e
f
(
𝐹
)
 
⊗
^
 
𝐺
m
o
d
)
,
Θ
F
	​

∈MC(Def(F)
⊗
	​

G
mod
	​

),

where
𝐺
m
o
d
G
mod
	​

 is the modular graph coefficient dg Lie algebra coming from stable graphs / the modular Feynman transform. This is the modular upgrade of the usual statement that chiral duality and deformation theory are governed by Maurer–Cartan data. In the chiral quadratic setting, maps and duality are already controlled by Maurer–Cartan equations, which is exactly the deformation-theoretic template one wants to lift to the modular case.

So the true form of the subject is:

modular homotopy theory
=
homotopy theory of curved factorization/chiral algebras on a curve
with genus controlled by the modular operad
{
𝑀
‾
𝑔
,
𝑛
}
,
 bar by the Feynman transform,
and duality by a modularized Koszul/Verdier bar–cobar adjunction.
modular homotopy theory=homotopy theory of curved factorization/chiral algebras on a curvewith genus controlled by the modular operad {
M
g,n
	​

}, bar by the Feynman transform,and duality by a modularized Koszul/Verdier bar–cobar adjunction.
	​


What is fully standard in the literature is each ingredient separately: modular operads + Feynman transform, chiral/factorization homotopy/Koszul duality, and factorization-homology/Poincaré–Koszul duality. What is not yet a universally standardized named theory is the single packaged subject under the label “modular homotopy theory”; that name is best understood as a synthesis/program built from those ingredients rather than a closed textbook doctrine.

The clean slogan is:

ordinary homotopy theory of operadic algebra is tree-level; modular homotopy theory is what you get when loops/genus are internalized by stable graphs.

A natural next step is to write the stable-graph differential explicitly for one model example, such as a Heisenberg, Kac–Moody, or general factorization algebra on a curve.

execute systematically on exactly this
what is the difference between the homotopy theory of operadic algebra (tree level) vs. full modular homotopy theory. what is accessible mathematically that is not accessible at tree level?
Thought for 20m 58s

Yes. Here is the systematic execution of exactly that construction.

Take as input a smooth curve
𝑋
X and work in the homotopy-theoretic world of chiral/factorization structures on
𝑋
X. Francis–Gaitsgory develop precisely such a homotopy theory and show that, in the chiral setting, the relation between chiral Lie data and factorization coalgebra data is a form of Koszul duality; in pro-nilpotent tensor settings, the Chevalley/primitives adjunction is an equivalence.

Now replace the tree-level operadic geometry by higher-genus geometry. The correct replacement is the modular operad

𝑀
:
=
{
𝑀
‾
𝑔
,
𝑛
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
M:={
M
g,n
	​

}
2g−2+n>0
	​

,

whose operations are the clutching maps for gluing marked points on stable curves. Getzler–Kapranov’s point is that modular operads are the higher-genus analogue of operads: graphs replace trees, and the basic example is exactly the Deligne–Mumford moduli system
𝑀
‾
𝑔
,
𝑛
M
g,n
	​

. Their Feynman transform is the higher-genus analogue of the usual bar construction.

So the direct construction is:

1. The object

A modular factorization object consists of data

𝐴
=
{
𝐴
(
𝑔
,
𝑛
)
}
2
𝑔
−
2
+
𝑛
>
0
A={A(g,n)}
2g−2+n>0
	​


equipped with
Σ
𝑛
Σ
n
	​

-actions and structure maps along the separating and non-separating gluings

𝐴
(
𝑔
1
,
𝑛
1
+
1
)
⊗
𝐴
(
𝑔
2
,
𝑛
2
+
1
)
→
𝐴
(
𝑔
1
+
𝑔
2
,
𝑛
1
+
𝑛
2
)
,
A(g
1
	​

,n
1
	​

+1)⊗A(g
2
	​

,n
2
	​

+1)→A(g
1
	​

+g
2
	​

,n
1
	​

+n
2
	​

),
𝐴
(
𝑔
,
𝑛
+
2
)
→
𝐴
(
𝑔
+
1
,
𝑛
)
,
A(g,n+2)→A(g+1,n),

satisfying the modular-operadic associativity/equivariance identities. Abstractly, this is just “an algebra over the modular operad of stable curves.”

When only the genus-zero piece is initially given, one should view modular homotopy theory as the problem of constructing a compatible higher-genus lift of that genus-zero factorization/chiral object.

2. The modular bar construction

Define the modular bar object of
𝐴
A by the Feynman transform:

𝐵
m
o
d
(
𝐴
)
:
=
F
T
𝑀
(
𝐴
)
.
B
mod
	​

(A):=FT
M
	​

(A).

Concretely, its
(
𝑔
,
𝑛
)
(g,n)-piece is the stable-graph sum

𝐵
m
o
d
(
𝐴
)
(
𝑔
,
𝑛
)
=
⨁
Γ
∈
𝐺
𝑔
,
𝑛
s
t
(
⨂
𝑣
∈
𝑉
(
Γ
)
𝐴
(
𝑔
𝑣
,
val
⁡
(
𝑣
)
)
)
⊗
or
⁡
(
𝐸
(
Γ
)
)
,
B
mod
	​

(A)(g,n)=
Γ∈G
g,n
st
	​

⨁
	​

	​

v∈V(Γ)
⨂
	​

A(g
v
	​

,val(v))
	​

⊗or(E(Γ)),

where the sum runs over stable graphs with

∑
𝑣
𝑔
𝑣
+
𝑏
1
(
Γ
)
=
𝑔
.
v
∑
	​

g
v
	​

+b
1
	​

(Γ)=g.

This is the exact higher-genus replacement of the ordinary bar complex: vertices carry local operations, internal edges are propagator lines, and loops encode genus. In Getzler–Kapranov, this is the defining role of the Feynman transform.

3. The differential

The modular differential is

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
e
p
+
𝑑
n
o
n
s
e
p
.
d
mod
	​

=d
int
	​

+d
sep
	​

+d
nonsep
	​

.

Here:

𝑑
i
n
t
d
int
	​

 is the internal differential already present on the coefficient object;

𝑑
s
e
p
d
sep
	​

 sums over contractions of separating edges, i.e. ordinary gluing of two components;

𝑑
n
o
n
s
e
p
d
nonsep
	​

 sums over contractions of loops or self-gluings, i.e. the operations that raise genus by one.

The reason this is the right differential is geometric: codimension-one boundary strata of
𝑀
‾
𝑔
,
𝑛
M
g,n
	​

 are exactly separating and non-separating degenerations, and the “boundary of boundary is zero” identity is the modular-operad form of
𝑑
2
=
0
d
2
=0. That is the higher-genus analogue of why the ordinary operadic bar differential squares to zero.

4. The homotopy theory

Declare a morphism

𝑓
:
𝐴
→
𝐵
f:A→B

to be a modular weak equivalence when

𝐵
m
o
d
(
𝑓
)
:
𝐵
m
o
d
(
𝐴
)
→
𝐵
m
o
d
(
𝐵
)
B
mod
	​

(f):B
mod
	​

(A)→B
mod
	​

(B)

is a quasi-isomorphism.

Dually, define a modular cobar functor

Ω
m
o
d
Ω
mod
	​


as the adjoint reconstruction functor from modular coalgebra-type objects back to modular algebra-type objects. On the genus-zero, pro-nilpotent chiral side, this reduces to the Francis–Gaitsgory bar–cobar/Koszul framework. So the modular theory is obtained by replacing “trees + ordinary bar” with “stable graphs + Feynman transform,” while retaining the same homotopy-theoretic logic.

5. Genus filtration

The modular bar object carries the obvious genus filtration

𝐹
≤
𝐺
𝐵
m
o
d
(
𝐴
)
:
=
⨁
𝑔
≤
𝐺
𝐵
m
o
d
(
𝑔
)
(
𝐴
)
.
F
≤G
B
mod
	​

(A):=
g≤G
⨁
	​

B
mod
(g)
	​

(A).

This gives the literal hierarchy:

𝑔
=
0
tree level
,
𝑔
=
1
one-loop
,
𝑔
≥
2
higher loops
.
g=0tree level,g=1one-loop,g≥2higher loops.

So “modular homotopy theory” is not a metaphor: it is the homotopy theory whose fundamental filtration parameter is genus.

6. Deformation theory

The deformation complex of a modular object is the convolution dg Lie algebra

D
e
f
m
o
d
(
𝐴
)
:
=
∏
𝑔
,
𝑛
Hom
⁡
Σ
𝑛
(
𝐶
∗
(
𝑀
‾
𝑔
,
𝑛
)
,
End
⁡
𝐴
(
𝑔
,
𝑛
)
)
,
Def
mod
	​

(A):=
g,n
∏
	​

Hom
Σ
n
	​

	​

(C
∗
	​

(
M
g,n
	​

),End
A
	​

(g,n)),

with bracket induced by graph gluing.

A modular structure on the underlying graded object is then equivalently a Maurer–Cartan element

Θ
∈
M
C
(
D
e
f
m
o
d
(
𝐴
)
)
.
Θ∈MC(Def
mod
	​

(A)).

This is the direct higher-genus upgrade of the standard principle “homotopy algebraic structures = Maurer–Cartan elements in a convolution dg Lie algebra.” Here the new feature is that the coefficients are chains on
𝑀
‾
𝑔
,
𝑛
M
g,n
	​

, hence the stable-graph geometry enters at the level of the governing dg Lie algebra itself.

7. Surface observables

To each modular object one attaches genus-
𝑔
g observables by factorization homology over a surface:

𝐻
Σ
𝑔
(
𝐴
)
:
=
∫
Σ
𝑔
𝐴
.
H
Σ
g
	​

	​

(A):=∫
Σ
g
	​

	​

A.

Ayala–Francis prove Poincaré/Koszul duality for factorization homology, giving a duality between factorization homology with coefficients in an
𝑛
n-disk algebra and factorization cohomology with coefficients in its Koszul dual coalgebra; in the connected/augmented situations covered by their main theorem, this is an equivalence. This supplies the topological shadow of the same modular bar–cobar story.

8. The resulting subject

So, on the nose,

modular homotopy theory
=
the homotopy theory of modular factorization/chiral objects
modular homotopy theory=the homotopy theory of modular factorization/chiral objects
	​


whose

bar construction
=
Feynman transform over
{
𝑀
‾
𝑔
,
𝑛
}
,
bar construction=Feynman transform over {
M
g,n
	​

},
	​


whose

differential
=
internal part + separating gluings + self-gluings
,
differential=internal part + separating gluings + self-gluings,
	​


and whose

weak equivalences are detected by modular bar–cobar/Koszul duality.
weak equivalences are detected by modular bar–cobar/Koszul duality.
	​


The genus-zero truncation recovers ordinary operadic/chiral homotopy theory. The higher-genus layers are exactly what is added when loops are internalized as stable graphs.

9. What is standard and what is synthesis

What is standard in the literature is the triad:

Getzler–Kapranov: modular operads and the Feynman transform.

Francis–Gaitsgory: homotopy theory and Koszul duality for chiral/factorization structures.

Ayala–Francis: Poincaré/Koszul duality for factorization homology.

What is not a standard fixed textbook name is the exact package called “modular homotopy theory.” That phrase is best read as a mathematically natural synthesis of those three ingredients.

In one line:

ordinary homotopy theory of operadic algebra is tree-level;
modular homotopy theory is its stable-graph, all-genus completion.
ordinary homotopy theory of operadic algebra is tree-level;modular homotopy theory is its stable-graph, all-genus completion.
	​


The next clean move is to instantiate this abstract construction for one concrete input
𝐴
A, such as Heisenberg, affine Kac–Moody, or a factorization algebra on a curve, and write the first few genus-
0
,
1
,
2
0,1,2 terms explicitly.

in other instances where we construct cyclic Linfty algebras and special classes, such as kevin costello's koszul duality gives holography setups, there is always a modular homotopy type - true or false?
Thought for 25m 59s

False as stated.

There are really two different claims hiding inside your sentence. At the weak categorical level, it is true that every cyclic operad has a modular envelope: Costello defines
M
o
d
(
𝑃
)
Mod(P) as the universal modular operad receiving a map from a cyclic operad
𝑃
P, and Chuang–Lazarev note that the cyclic operads governing
𝐿
∞
L
∞
	​

 and
𝐴
∞
A
∞
	​

 admit such modular closures. In that formal sense, a cyclic
𝐿
∞
L
∞
	​

 algebra always has a canonical modular avatar.

But in the strong sense relevant to higher genus, BV quantization, and holography, the answer is no. A genuine modular object is what Braun–Maunder call a quantum
𝐿
∞
L
∞
	​

 algebra, or loop homotopy algebra: a solution
𝑚
(
ℏ
)
=
𝑚
0
+
ℏ
𝑚
1
+
⋯
m(ℏ)=m
0
	​

+ℏm
1
	​

+⋯ of the quantum master equation. They explicitly describe this as a higher-genus version of a cyclic
𝐿
∞
L
∞
	​

 algebra, with
𝑚
0
m
0
	​

 as the genus-zero part. Braun–Lazarev then show that lifting a cyclic
𝐿
∞
L
∞
	​

 structure to this quantum/modular level is obstructed: the first obstruction is
Δ
(
𝑚
0
)
Δ(m
0
	​

), a first-order lift exists iff the cyclic
𝐿
∞
L
∞
	​

 algebra is unimodular, and further higher-order obstructions can still appear.

So cyclicity gives you the tree-level symplectic pairing, not automatically the full modular homotopy type. There are important positive classes: for example, harmonic cyclic
𝐿
∞
L
∞
	​

 algebras admit quantum lifts, and Costello’s M2-brane holography paper is exactly a case where the twisted bulk theory is quantized to all orders and the Koszul-duality statement is proved to all orders. But that is a theorem in that example, not a formal consequence of cyclicity alone.

Costello’s own BCOV/open-closed story shows why “always” is too strong. Costello–Li explain that holomorphic Chern–Simons by itself has a one-loop anomaly, while the coupled open-closed BCOV theory has the quantization theorem; and Costello–Gwilliam formulate BV quantization generally as obstruction theory, where the quantum factorization algebra exists only when the anomaly vanishes.

So the clean answer is:

always a modular envelope; not always a genuine modular homotopy type.

For holography, the full modular object is extra structure proved by anomaly cancellation and quantization, not something forced by the mere existence of a cyclic
𝐿
∞
L
∞
	​

 algebra.

so our koszul chiral algebras give full modular homotopy types and that is quite a special thing. Our all-genus structures arising as modular deformations in a cyclic Linfinity structure is than taking place in some quantum Linfty structure?
Thought for 19m 5s

Yes—on the current source tree you uploaded, that is the right reading, with one refinement.

For the class treated there, the claim is now stronger than just “scalar higher-genus shadows.” The source states that Def_cyc(A) is a complete cyclic
𝐿
∞
L
∞
	​

 algebra, that there is a universal Maurer–Cartan class

Θ
𝐴
∈
M
C
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
‾
𝑔
,
∙
,
𝑄
)
)
,
Θ
A
	​

∈MC(Def
cyc
	​

(A)
⊗
	​

RΓ(
M
g,∙
	​

,Q)),

and that MC2 is fully proved. So, in that source, the genus tower is no longer merely encoded by
𝜅
(
𝐴
)
κ(A); it is organized by a full homotopy-algebraic object
Θ
𝐴
Θ
A
	​

. See the uploaded source at introduction.tex lines 319–359, deformation_theory.tex lines 1656–1702, higher_genus.tex lines 10335–10359 and 14239–14295, and concordance.tex lines 3410–3461.

So I would distinguish two levels.

At the formal deformation / tangent level, yes: your all-genus modular deformation is naturally taking place in what the outside literature calls a quantum
𝐿
∞
L
∞
	​

 algebra. In that literature, quantum
𝐿
∞
L
∞
	​

 algebras are exactly the higher-loop or higher-genus generalizations of cyclic
𝐿
∞
L
∞
	​

 algebras.

At the global chiral/factorization level, the object is richer than a bare quantum
𝐿
∞
L
∞
	​

 algebra. Your “full modular homotopy type” also includes the bar–cobar adjunction, functoriality over
𝑀
‾
𝑔
,
𝑛
M
g,n
	​

, Verdier duality, and the shifted-symplectic/Lagrangian package. In your source, the quantum-
𝐿
∞
L
∞
	​

 piece is the deformation algebra
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

(A) together with
Θ
𝐴
Θ
A
	​

; the full modular homotopy theory is the larger factorization-theoretic structure around it.

So the clean slogan is:

tree level = cyclic
𝐿
∞
L
∞
	​

;
all genus = quantum
𝐿
∞
L
∞
	​

;
globalized on curves/factorization algebras = modular homotopy type.

And yes, that is a special property. In general, a cyclic
𝐿
∞
L
∞
	​

 algebra does not automatically admit an all-genus quantum lift; existence is typically obstructed and tied to conditions like unimodularity or anomaly cancellation. Costello’s open/closed BCOV–holomorphic Chern–Simons story is a standard example where the all-genus lift exists only after the right anomaly-cancellation mechanism is in place.

So the precise answer is: yes, for the class now covered in your source tree, your modular deformations are living inside a quantum
𝐿
∞
L
∞
	​

 structure; and that quantum
𝐿
∞
L
∞
	​

 structure is the local homotopy-algebraic core of a full modular homotopy type.

what is the "correct definition" of a modular homotopy theory? how does it "obviously" generalized from a correct definition of a "homotopy theory"
Thought for 17m 29s

There is not one universally fixed textbook definition of the phrase “modular homotopy theory.” But there is a clean answer once you separate the abstract notion from the curve/factorization realization.

A homotopy theory, in the precise modern sense, is best taken to be an
∞
∞-category (or any equivalent presentation, such as a model category or relative category). Francis–Gaitsgory say exactly this: the homotopy category is too coarse, a model category is a presentation with extra choices, and the right intermediate notion is an
∞
∞-category carrying objects, maps, homotopies, higher homotopies, and so on. (1103.5803v4.txt, lines 287–309)

A modular operad is the higher-genus replacement of a cyclic operad: instead of compositions indexed only by trees, one allows stable graphs, including self-gluings and loops. Loday–Vallette phrase this exactly as “a higher genus extension of the notion of cyclic operads.” (algebraic_operads_lv.txt, lines 28968–28975)

So the minimal abstract definition is:

modular homotopy theory
=
(
∞
-category
𝐻
)
+
(
homotopy-coherent stable-graph / modular-operadic structure
)
modular homotopy theory=(∞-category H)+(homotopy-coherent stable-graph / modular-operadic structure)
	​


In other words, the underlying notion of “homotopy theory” does not change: it is still an
∞
∞-category. What changes is the indexing geometry of operations. Tree-level operadic homotopy theory has compositions parameterized by trees; modular homotopy theory has compositions parameterized by stable graphs, equivalently by the modular operad
{
𝑀
‾
𝑔
,
𝑛
}
{
M
g,n
	​

}. So “modular” is extra structure on a homotopy theory, not a replacement for the meaning of homotopy theory itself. (1103.5803v4.txt, lines 287–309; algebraic_operads_lv.txt, lines 28968–28975)

In your current source tree, the native definition is explicitly H-level, not dg-model level. The manuscript’s H/M/S convention says the H-level is the homotopy-native statement in the stable
∞
∞-category, the M-level is an explicit dg or
𝐿
∞
L
∞
	​

 presentation, and the S-level is the numerical/cohomological shadow. So the “correct definition” is the H-level one; bar complexes and formulas are presentations of it, not its essence. (introduction.tex, lines 810–846)

With that understood, the correct definition in your project is the one in Definition 34.11.15: a modular homotopy theory on a smooth curve
𝑋
X is a package consisting of

(
𝑖
)
(i) an
∞
∞-categorical bar–cobar adjunction on the coderived category of curved factorization algebras on
Ran
⁡
(
𝑋
)
Ran(X),

(
𝑖
𝑖
)
(ii) functoriality over
{
𝑀
‾
𝑔
,
𝑛
}
{
M
g,n
	​

} intertwined with Verdier duality,

(
𝑖
𝑖
𝑖
)
(iii) a universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

 controlling the full genus tower as one deformation, and

(
𝑖
𝑣
)
(iv) a shifted-symplectic pairing for which deformation and obstruction complexes are complementary Lagrangians. (concordance.tex, lines 3410–3461)

That definition is not floating in the air: the basic objects that live inside it are your modular Koszul objects. Their homotopy-form definition requires a bar object, a dual object, a cyclic deformation object
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

(A), a center local system on
𝑀
‾
𝑔
,
∙
M
g,∙
	​

, and further spectral/periodicity data; the antecedent axioms are exactly Koszulity, Verdier intertwining, and modular deformation, with bar-cobar inversion and Lagrangian complementarity following as consequences. (higher_genus.tex, lines 8658–8749)

So the “obvious generalization” works like this:

ordinary homotopy theory
  
⇝
  
∞
-category
ordinary homotopy theory⇝∞-category
operadic homotopy theory
  
⇝
  
∞
-category with tree-indexed operations
operadic homotopy theory⇝∞-category with tree-indexed operations
modular homotopy theory
  
⇝
  
∞
-category with stable-graph-indexed operations
modular homotopy theory⇝∞-category with stable-graph-indexed operations

and in the chiral/factorization setting this becomes:

Fact
⁡
(
𝑋
)
+
bar-cobar/Verdier/Koszul duality
+
{
𝑀
‾
𝑔
,
𝑛
}
-functoriality
+
Θ
𝐴
+
Lagrangian branch structure
.
Fact(X)+bar-cobar/Verdier/Koszul duality+{
M
g,n
	​

}-functoriality+Θ
A
	​

+Lagrangian branch structure.

This is why the manuscript says the subject is built from the genus-0 seed (Arnold/factorization coherence), Verdier duality, genus-1 curvature, and clutching of stable curves. The crucial transition is from trees to stable graphs: that is where the theory becomes genuinely modular. (introduction.tex, lines 491–525)

So the sharp answer is:

A modular homotopy theory is a homotopy theory whose higher operations are governed by modular geometry.
A modular homotopy theory is a homotopy theory whose higher operations are governed by modular geometry.
	​


For your project, that means: the coderived homotopy theory of curved factorization algebras on a curve, equipped with bar–cobar duality, Verdier-compatible functoriality over
𝑀
‾
𝑔
,
𝑛
M
g,n
	​

, a universal genus-completed Maurer–Cartan deformation, and a shifted-symplectic/Lagrangian obstruction theory. (concordance.tex, lines 3410–3461)

One more important point: “obvious” here means formal at the level of definition, not automatic at the level of existence. Replacing trees by stable graphs is conceptually straightforward. Proving that a given theory actually carries that structure is hard. Your current extracted concordance reflects that sharpened status: it says the universal Maurer–Cartan class is now treated as proved, and the remaining gap is the full coderived Ran-space formalism. (concordance.tex, lines 3388–3394; concordance.tex, lines 3452–3461)

The shortest slogan is:

homotopy theory
=
∞
-category
,
modular homotopy theory
=
∞
-category
+
stable-graph/moduli-of-curves structure
.
homotopy theory=∞-category,modular homotopy theory=∞-category+stable-graph/moduli-of-curves structure.
	​


If you want, I can next compress this into a single formal definition in the style of a paper: “Definition. A modular homotopy theory is …” with no motivational language.

execute that
Thought for 13m 23s

Here is the paper-style formulation compatible with the current manuscript.

Definition 1 (homotopy theory).
A homotopy theory is an
∞
∞-category
𝐻
H.
(1103.5803v4.txt, lines 287–301)

Definition 2 (tree-level operadic homotopy theory).
Let
𝑃
P be an operad. A tree-level operadic homotopy theory is an
∞
∞-category
𝐻
H equipped with a homotopy-coherent
𝑃
P-action; equivalently,
𝐻
H carries higher composition operations indexed by rooted trees, compatible with grafting, contraction, and symmetric-group actions.

Definition 3 (modular homotopy theory, abstract).
Let
𝑀
M be a modular operad. A modular homotopy theory is an
∞
∞-category
𝐻
H equipped with a homotopy-coherent
𝑀
M-action; equivalently,
𝐻
H carries higher operations indexed by stable graphs, compatible with separating and nonseparating gluing, internal-edge contraction, and automorphisms of graphs.
This is the formal generalization of Definition 2 obtained by replacing trees with stable graphs.
(algebraic_operads_lv.txt, lines 28968–28975; introduction.tex, lines 513–519)

Definition 4 (modular homotopy theory on a smooth curve).
A modular homotopy theory on a smooth curve
𝑋
X is the data of:

an
∞
∞-categorical bar–cobar adjunction

𝐵
ˉ
𝑋
⊣
Ω
𝑋
B
ˉ
X
	​

⊣Ω
X
	​


on the coderived category

𝐷
c
o
(
Fact
⁡
(
𝑋
)
)
D
co
(Fact(X))

of curved factorization algebras on
Ran
⁡
(
𝑋
)
Ran(X);

functoriality of this adjunction over the modular operad

{
𝑀
‾
𝑔
,
𝑛
}
𝑔
,
𝑛
,
{
M
g,n
	​

}
g,n
	​

,

intertwined with Verdier duality, in the sense that

𝐷
Ran
⁡
 
𝐵
ˉ
𝑋
(
𝐴
)
≃
𝐵
ˉ
𝑋
(
𝐴
!
)
;
D
Ran
	​

B
ˉ
X
	​

(A)≃
B
ˉ
X
	​

(A
!
);

a universal Maurer–Cartan class

Θ
𝐴
∈
MC
⁡
 ⁣
(
Def
⁡
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
,
𝑄
)
)
Θ
A
	​

∈MC(Def
cyc
	​

(A)
⊗
	​

RΓ(
M
g,∙
	​

,Q))

controlling the full genus tower as a single deformation;

a shifted-symplectic pairing on

𝑅
Γ
(
𝑀
‾
𝑔
,
𝑍
𝐴
)
RΓ(
M
g
	​

,Z
A
	​

)

for which the deformation and obstruction complexes

𝑄
𝑔
(
𝐴
)
,
𝑄
𝑔
(
𝐴
!
)
Q
g
	​

(A),Q
g
	​

(A
!
)

are complementary Lagrangians.
(concordance.tex, lines 3410–3461)

Remark.
Definition 1 is the correct abstract meaning of “homotopy theory.” Definition 3 is the obvious modular generalization: the ambient notion remains an
∞
∞-category, and only the indexing geometry of higher operations changes, from trees to stable graphs. In the manuscript’s H/M/S convention, these are H-level definitions; dg,
𝐿
∞
L
∞
	​

, or bar-complex realizations are M-level presentations, and numerical/cohomological invariants are S-level shadows.
(1103.5803v4.txt, lines 287–301; introduction.tex, lines 810–846)

In one sentence:

modular homotopy theory
=
homotopy theory
+
stable-graph/modular-operadic higher composition
.
modular homotopy theory=homotopy theory+stable-graph/modular-operadic higher composition.
