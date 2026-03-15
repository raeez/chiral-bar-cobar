I re-cut this from scratch, and my earlier read was too generous.

The upgraded picture is:

The work is stronger than I first said on MC2 existence, and weaker than I first said on universal explicit saturation. The safe core is the existence engine: the manuscript now claims a general cyclic
𝐿
∞
L
∞
	​

 structure on
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

(A), the completed tensor/clutching package, tautological-line support, and from those the existence of a universal Maurer–Cartan class with trace, clutching, and Verdier properties. That is the defensible center of gravity.

Chiral_Bar_Cobar_Duality__Geome…

The place I would attack, hard, is the upgrade from that existence theorem to the claim that for every modular Koszul chiral algebra with simple Lie symmetry, the minimal model is
𝑔
⊕
𝐶
𝜂
g⊕Cη with only the Killing
𝑙
3
l
3
	​

, and hence
Θ
𝐴
Θ
A
	​

 is universally scalar-saturated. That layer is not referee-secure in its present scope. I pulled the decisive source snippets here: source excerpt pack.

The main break is a scope jump.

Theorem 9.18.33 is stated for a general modular Koszul chiral algebra with simple Lie symmetry, and its key part (the minimal-model formula) explicitly cites Corollary 12.5.12 as the source of the structure

𝐻
≅
𝑔
⊕
𝐶
𝜂
,
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
H≅g⊕Cη,l
2
	​

=[−,−],l
3
	​

=ϕ,l
n
	​

=0 (n≥4).

But Corollary 12.5.12 is the Kac–Moody minimal model, and Remark 12.5.13 explicitly says that theorem resolves MC2-1 only for the Kac–Moody family at noncritical generic levels. In other words: the universal theorem is powered by a family-specific input.

That single scope leak contaminates the next layer down.

Corollary 9.18.70 then claims scalar saturation for every Koszul chiral algebra with simple Lie symmetry, and its proof uses exactly that universalized minimal-model picture together with the one-dimensionality of
𝐻
c
y
c
2
(
𝑔
,
𝑔
)
≅
𝐻
3
(
𝑔
)
≅
𝐶
H
cyc
2
	​

(g,g)≅H
3
(g)≅C. Proposition 9.18.77(b) goes even further and says the equivalent rigidity conditions hold “unconditionally for every Koszul chiral algebra with simple
𝑔
g.” Under hostile review, that is where I stop believing the stated generality. The argument is sliding from the cyclic cohomology of the symmetry algebra
𝑔
g to the degree-2 deformation cohomology of the full algebra
𝐴
A, without a family-independent theorem killing all extra “primary” deformation directions.

The manuscript itself contains the counter-pressure to those broad claims.

Theorem 9.18.80 introduces a decomposition

𝐻
c
y
c
2
(
𝐴
,
𝐴
)
=
𝐶
⋅
𝜂
⊕
𝐻
c
y
c
,
p
r
i
m
2
(
𝐴
)
,
H
cyc
2
	​

(A,A)=C⋅η⊕H
cyc,prim
2
	​

(A),

and only kills the primitive part under generic-level semisimplicity hypotheses. Remark 9.18.81 then says admissible levels are precisely where that generic argument does not apply, and Conjecture 9.18.82 explicitly leaves the all-level/all-family scalar-saturation statement conjectural. That is the manuscript’s own admission that the primitive sector is the real unresolved variable. So Corollary 9.18.70 / Proposition 9.18.77(b) and Conjecture 9.18.82 cannot all be taken at face value as written.

That leads to the core adversarial verdict:

MC2 existence looks substantially stronger than open. Universal explicit saturation does not yet look fully proved in the stated generality.

There is also internal status drift.

In the source tree, the extended axioms MK6–MK8 are still labeled conjectured/programmatic; the extracted source lines show exactly that. source excerpt pack In the compiled PDF, Theorem 9.18.68 says MC2 is fully proved. Within Chapter 12, Remark 12.5.13 still says only the Kac–Moody MC2-1 piece is resolved there, while the immediately following remark treats the full construction of
Θ
𝐴
Θ
A
	​

 as established. That is survivable as drafting history, but to a hostile referee it reads like several layers of the project were stacked without one final constitutional cleanup.

A second weakness is proof audibility.

The manuscript’s one-channel reduction chain is extremely long: clutching/trace isolation, Verdier plane, PTVV lift, explicit chain-model sector, finite seed packet, low-arity visible data, transfer law, root-string chart, support-graph rigidity, orbit-count table, parity forcing, normalization. Even if every reduction is correct, the sheer depth makes the result fragile in presentation. A referee will ask for one short theorem that states exactly which interface lemmas are essential and exactly where the Kac–Moody-specific information ends and the family-independent argument begins. Right now that separation is not sharp enough. You can feel that pressure in the text itself.

A third weakness is that the manuscript’s own frontier language is not yet fully synchronized with the theorem statements.

Chapter 35 correctly narrows some claims to the “standard Lie-theoretic landscape” and to generic-level rigidity, while still also advertising universal scalar saturation and effective quadruple reduction. Corollary 9.18.79 is already landscape-restricted; Theorem 9.18.80 is generic-level; Conjecture 9.18.82 is the honest universal statement. That is actually a good stratification, but it means the earlier unconditional formulations should be downgraded to match it.

So my revised understanding of the work is this:

The project has three layers.

First, the infrastructure layer: bar/cobar, graph-complex cyclic
𝐿
∞
L
∞
	​

 structure, completed modular-operadic tensoring, clutching, tautological support. This is the best part of the manuscript and much stronger than I originally credited.

Chiral_Bar_Cobar_Duality__Geome…

Second, the explicit
Θ
Θ-layer: identify the minimal model, write
Θ
min
⁡
=
𝜅
𝜂
⊗
Λ
Θ
min
=κη⊗Λ, and prove scalar saturation. This is the brittle layer. It is solid on Kac–Moody and on the standard Lie-theoretic landscape where extra arguments are supplied; it is not yet referee-proof in full universal generality.

Third, the characteristic-hierarchy / future-stratification layer: reducing the quintuple to an effective quadruple, claiming Future 4 is existence-level solved, isolating the live frontier. This layer is conceptually good, but only if it inherits the corrected scoping from the second layer.

So if I were writing the constitutional rewrite, I would say:

Keep as unconditionally proved: the MC2 existence engine and existence of a universal Maurer–Cartan class with trace/clutching/Verdier properties.

Chiral_Bar_Cobar_Duality__Geome…

Restrict to Kac–Moody / standard-landscape / generic-rigidity regimes: the explicit minimal-model formula, universal scalar saturation, and effective-quadruple reduction.

Leave genuinely conjectural: family-independent vanishing of
𝐻
c
y
c
,
p
r
i
m
2
(
𝐴
)
H
cyc,prim
2
	​

(A), hence universal scalar saturation at all levels and for all modular Koszul chiral algebras with simple Lie symmetry. That is the real unresolved theorem, and the manuscript already names it.

Chiral_Bar_Cobar_Duality__Geome…

This also changes what the real bleeding edge is.

It is not “construct
Θ
𝐴
Θ
A
	​

 somehow.” Theorem 9.18.68 has mostly moved that question into the proved zone. The actual frontier is:

prove a family-independent bridge from the general cyclic
𝐿
∞
L
∞
	​

 existence theorem to the minimal-model identification used in Theorem 9.18.33, or equivalently prove that the primitive deformation sector
𝐻
c
y
c
,
p
r
i
m
2
(
𝐴
)
H
cyc,prim
2
	​

(A) vanishes beyond the current generic/standard-landscape regimes.

One final nuance: the right dichotomy is not merely “generic vs admissible.” The family dependence matters. For example, Arakawa proves rationality for
𝑊
𝑘
(
𝑔
)
W
k
	​

(g) at non-degenerate admissible numbers, so admissible behavior is not uniformly pathological. The true issue is not the word “admissible” by itself; it is whether extra primitive cyclic deformation directions survive in a given family.

So the bottom line is blunt:

My previous analysis over-closed Future 4.
What is really solid is MC2 existence.
What is really vulnerable is the universal explicit/saturation upgrade.
The manuscript already contains the theorem that exposes the gap:
𝐻
c
y
c
,
p
r
i
m
2
(
𝐴
)
H
cyc,prim
2
	​

(A).

That is where the blood is.
