
Yes. The right word is not “constant” but scalar-saturated.

What your sources are really saying is: the genus-direction of the theory can collapse to one scalar when the relevant deformation sector is rank
1
1, but that does not mean the whole homotopy type is scalar. In the source tree, this is stated very explicitly: the MC element is scalar because it lives in a line, while the full package is non-scalar because the underlying virtual bar family has higher rank. A line bundle has one Chern class; a higher-rank virtual bundle has many. (higher_genus.tex, 15618–15627 and 15741–15752)

So the total object is not the pair
(
𝜅
,
Δ
)
(κ,Δ). It is the full modular characteristic package

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
,
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

),

where
Θ
𝐴
Θ
A
	​

 is the universal Maurer–Cartan class,
Π
𝐴
Π
A
	​

 is the periodicity profile, and
𝐻
𝐴
=
{
𝐶
𝑔
(
𝐴
)
}
𝑔
≥
0
H
A
	​

={C
g
	​

(A)}
g≥0
	​

 is the ambient modular deformation family. In the same source, this package is presented as the total shape, and its components are said to be functorial, dualizable, modular, and non-scalar. (higher_genus.tex, 10103–10170)

The cleanest way to classify the “parts” is to distinguish two hierarchies.

First, there is the homotopy/characteristic hierarchy:

scalar data
  
→
  
spectral data
  
→
  
full MC data
.
scalar data→spectral data→full MC data.

In your source this is spelled out as:

scalar:
𝜅
(
𝐴
)
κ(A), obstruction classes, free energies;

spectral:
Δ
𝐴
(
𝑥
)
Δ
A
	​

(x), bar-cohomology generating functions;

full MC:
Θ
𝐴
Θ
A
	​

,
\Def
c
y
c
(
𝐴
)
\Def
cyc
	​

(A),
𝐻
𝐴
H
A
	​

.
(higher_genus.tex, 10172–10218)

Second, there is the sharper
𝐾
K-theoretic extraction hierarchy from the virtual bar family

𝑉
𝐴
:
=
[
𝑅
𝜋
𝑔
∗
𝐵
ˉ
(
𝑔
)
(
𝐴
)
]
.
V
A
	​

:=[Rπ
g∗
	​

B
ˉ
(g)
(A)].

From this one extracts three different shadow layers:

𝑐
1
(
det
⁡
𝑉
𝐴
)
⇝
𝜅
(
𝐴
)
,
𝑐
∗
(
𝑉
𝐴
)
⇝
Δ
𝐴
(
𝑥
)
,
Hol
⁡
(
𝑉
𝐴
)
⇝
Π
𝐴
.
c
1
	​

(detV
A
	​

)⇝κ(A),c
∗
	​

(V
A
	​

)⇝Δ
A
	​

(x),Hol(V
A
	​

)⇝Π
A
	​

.

The source even tabulates this: level L1 is the first Chern class / trace shadow, level L2 is the full Chern polynomial / determinant shadow, and level L3 is holonomy/eigenvalue structure / periodicity. (higher_genus.tex, 15644–15753)

That also answers the determinant question. There are really two determinant-like objects:

𝐿
𝐴
:
=
det
⁡
𝑅
𝜋
𝑔
∗
𝐵
ˉ
(
𝑔
)
(
𝐴
)
L
A
	​

:=detRπ
g∗
	​

B
ˉ
(g)
(A)

is the determinant line bundle, and its first Chern class is

𝑐
1
(
𝐿
𝐴
)
=
𝜅
(
𝐴
)
⋅
𝜆
.
c
1
	​

(L
A
	​

)=κ(A)⋅λ.

This is still scalar/additive data. But

Δ
𝐴
(
𝑥
)
=
det
⁡
(
1
−
𝑥
𝑇
)
Δ
A
	​

(x)=det(1−xT)

is the spectral determinant or characteristic polynomial of a transport/monodromy operator, so it records all elementary symmetric functions of the eigenvalues, not just the trace. In other words:
𝜅
κ is the trace-class shadow;
Δ
Δ is the determinant-class shadow. They are not the same level of information. (higher_genus.tex, 15577–15615 and 15681–15697; examples_summary.tex, 1239–1265)

So the total picture has the following shape:

(
\Def
c
y
c
(
𝐴
)
,
Θ
𝐴
,
𝐻
𝐴
)
⟶
𝑉
𝐴
⟶
(
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
)
,
(\Def
cyc
	​

(A),Θ
A
	​

,H
A
	​

)⟶V
A
	​

⟶(κ(A),Δ
A
	​

,Π
A
	​

),

and this is realized geometrically in the ambient complex

𝐶
𝑔
=
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
,
C
g
	​

=RΓ(
M
g
	​

,Z
A
	​

),

where
𝑄
𝑔
(
𝐴
)
Q
g
	​

(A) and
𝑄
𝑔
(
𝐴
!
)
Q
g
	​

(A
!
) are complementary Lagrangians. The universal class
Θ
𝐴
Θ
A
	​

 is the complete logarithm;
𝜅
,
Δ
,
Π
κ,Δ,Π are its successive shadows. (concordance.tex, 2423–2486 and 3398–3448)

If you want the deepest structural answer: the “parts” are not arbitrary invariants. They are the natural shadow functors out of the universal class. A new part of the homotopy type is something that is:

extracted functorially from
Θ
𝐴
Θ
A
	​

 or
𝑉
𝐴
V
A
	​

,

compatible with clutching and Verdier duality,

not recoverable from a lower extraction level.

In that language:

𝜅
(
𝐴
)
κ(A) is the first trace/Chern-number shadow,

Δ
𝐴
Δ
A
	​

 is the first determinant/Chern-polynomial shadow,

Π
𝐴
Π
A
	​

 is the first holonomy/Galois shadow,

Θ
𝐴
Θ
A
	​

 is the full homotopy datum itself.
(higher_genus.tex, 15668–15752; koszul_pair_structure.tex, 740–790)

And beneath all of this sit the four irreducible geometric seeds: Arnold relation, Verdier duality, genus-1 curvature, and clutching. Those are the generators of the machine;
𝜅
,
Δ
,
Π
,
Θ
κ,Δ,Π,Θ are the outputs of the machine. (heisenberg_frame.tex, 2526–2533)

So the shortest answer is:

Do not classify the homotopy type by a bag of invariants. Classify it by the universal Maurer–Cartan object, and then classify its shadows by level: trace
→
→ determinant
→
→ holonomy.

One caveat: your indexed main.pdf and the extracted bookrepo.zip source tree appear to differ on whether the MC apex is still programmatic or already resolved. The organizational picture above is the same in either case; what changes is only the status of the top layer.

what is the relationship between V
A
	​

:=[Rπ
g∗
	​

B
ˉ
(g)
(A)] and the "complete logarithm" Θ
A
	​

 which is the full homotopy datum itself.

I approximately understand this is the class that defines the algebraic structure in the appropriate full-genus convolution dg modular-algebra structure. Let's connect the two worlds more directly.
Thought for 25m 42s

The clean bridge is not

𝑉
𝐴
=
exp
⁡
(
Θ
𝐴
)
.
V
A
	​

=exp(Θ
A
	​

).

It is

\Theta_A \;\rightsquigarrow\; (\bar B^{(\bullet)}(A),\,d_{\bar}^{\Theta}) \;\xrightarrow{R\pi_*}\; R\pi_{g*}\bar B^{(g)}(A) \;\xrightarrow{[\;]}\; \mathcal V_A\in K_0(\overline{\mathcal M}_g).

So the common object is the genus bar family.

Θ
𝐴
Θ
A
	​

 is the all-genera Maurer–Cartan datum controlling that family as one deformation, while
𝑉
𝐴
V
A
	​

 is the genus-
𝑔
g virtual bundle you get only after derived pushforward and then passing to
𝐾
K-theory. They live at different heights:
Θ
𝐴
Θ
A
	​

 is upstream,
𝑉
𝐴
V
A
	​

 downstream. The source says exactly that
Θ
𝐴
Θ
A
	​

 controls the full genus tower as a single deformation, while
𝑉
𝐴
=
[
𝑅
𝜋
𝑔
∗
𝐵
ˉ
(
𝑔
)
(
𝐴
)
]
V
A
	​

=[Rπ
g∗
	​

B
ˉ
(g)
(A)] is the virtual bar family. (theta_VA_excerpts.txt, concordance 2461–2471, 3432–3440; higher_genus 15644–15651)

The first arrow is the deformation-theoretic one. In standard
𝐿
∞
L
∞
	​

 language, an MC element twists the bare differential into a corrected one; schematically,

d_{\bar}^{\Theta} = l_1+l_2(\Theta,-)+\frac1{2!}l_3(\Theta,\Theta,-)+\cdots.

Here that is not just analogy: the text says the MC equation in

\Def
c
y
c
(
𝐴
)
⊗
^
\Gmod
\Def
cyc
	​

(A)
⊗
	​

\Gmod encodes exactly the nonlinear condition
𝑑
b
a
r
2
=
0
d
bar
2
	​

=0 for the genus-expanded bar differential. Thus
Θ
𝐴
Θ
A
	​

 is the chain-level flatness/integrability law of the genus tower. Its components
𝜃
𝑔
θ
g
	​

 are the successive genus corrections; in the scalar-saturated case,

Θ
𝐴
min
⁡
=
𝜅
(
𝐴
)
 
𝜂
⊗
Λ
,
[
𝜃
𝑔
]
=
𝜅
(
𝐴
)
[
𝜇
]
⊗
𝜆
𝑔
.
Θ
A
min
	​

=κ(A)η⊗Λ,[θ
g
	​

]=κ(A)[μ]⊗λ
g
	​

.

(theta_VA_excerpts.txt, higher_genus 10424–10523, 15783–15792)

The second arrow is the geometric one. Once the twisted bar differential is in place, you have an actual family of complexes over
𝑀
‾
𝑔
M
g
	​

, and you can push it forward. Under the perfectness hypothesis, the source identifies

𝑅
𝑞
𝜋
𝑔
∗
𝐵
ˉ
(
𝑔
)
(
𝐴
)
=
0
(
𝑞
≠
0
)
,
𝑅
0
𝜋
𝑔
∗
𝐵
ˉ
(
𝑔
)
(
𝐴
)
≅
𝑍
𝐴
,
R
q
π
g∗
	​

B
ˉ
(g)
(A)=0(q

=0),R
0
π
g∗
	​

B
ˉ
(g)
(A)≅Z
A
	​

,

so the immediate bridge object is the center local system
𝑍
𝐴
Z
A
	​

. In that sense,
𝑉
𝐴
V
A
	​

 is the virtual class of the same geometric family that
Θ
𝐴
Θ
A
	​

 governs at chain level. (theta_VA_excerpts.txt, higher_genus 4812–4822)

The third arrow is the decategorifying one: from the derived family to its characteristic shadows. This is where the source’s Chern–Weil dictionary becomes exact. The determinant line

𝐿
𝐴
:
=
det
⁡
𝑉
𝐴
L
A
	​

:=detV
A
	​


has

𝑐
1
(
𝐿
𝐴
)
=
𝜅
(
𝐴
)
𝜆
,
c
1
	​

(L
A
	​

)=κ(A)λ,

and the text explicitly says that
Θ
𝐴
Θ
A
	​

 is a section of a twist of this determinant line. So in rank one,
Θ
𝐴
Θ
A
	​

 is the Chern–Weil representative of the genus-direction seen by
det
⁡
𝑉
𝐴
detV
A
	​

; scalar saturation is precisely the statement that this line carries only one characteristic number, namely
𝜅
(
𝐴
)
κ(A). Beyond that, the higher-rank part of
𝑉
𝐴
V
A
	​

 produces the non-scalar shadows:

𝑐
∗
(
𝑉
𝐴
)
⇝
Δ
𝐴
,
Hol
⁡
(
𝑉
𝐴
)
⇝
Π
𝐴
.
c
∗
	​

(V
A
	​

)⇝Δ
A
	​

,Hol(V
A
	​

)⇝Π
A
	​

.

So
Θ
𝐴
Θ
A
	​

 and
𝑉
𝐴
V
A
	​

 are not two separate invariants; they are two views of the same bar family, before and after characteristic extraction. (theta_VA_excerpts.txt, higher_genus 15545–15627, 15644–15752)

There is also a direct modular-operadic bridge: clutching. The source says the MC equation for
Θ
Θ decomposes along boundary strata as

𝜉
s
e
p
∗
(
Θ
(
𝑔
)
)
=
∑
𝑔
1
+
𝑔
2
=
𝑔
Θ
(
𝑔
1
)
⋆
Θ
(
𝑔
2
)
,
𝜉
n
s
∗
(
Θ
(
𝑔
+
1
)
)
=
Δ
n
s
(
Θ
(
𝑔
)
)
.
ξ
sep
∗
	​

(Θ
(g)
)=
g
1
	​

+g
2
	​

=g
∑
	​

Θ
(g
1
	​

)
⋆Θ
(g
2
	​

)
,ξ
ns
∗
	​

(Θ
(g+1)
)=Δ
ns
	​

(Θ
(g)
).

That means
Θ
𝐴
Θ
A
	​

 is literally the gluing law of the modular bar family. After pushforward, those same gluing laws are what make
𝑉
𝐴
V
A
	​

 into a coherent family over moduli. (theta_VA_excerpts.txt, higher_genus 11627–11752; concordance 2477–2485)

So the sharp relationship is:

Θ
𝐴
=
the derived logarithm / flatness datum of the genus bar tower
,
𝑉
𝐴
=
the
𝐾
-theoretic family-index shadow of that tower
.
Θ
A
	​

=the derived logarithm / flatness datum of the genus bar tower,V
A
	​

=the K-theoretic family-index shadow of that tower.
	​


Or even shorter:

Θ
𝐴
Θ
A
	​

 tells you how the tower is assembled;

𝑉
𝐴
V
A
	​

 tells you what virtual geometric object remains after assembly.

The exact source passages are gathered here: theta_VA_excerpts.txt.
