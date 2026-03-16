
The emerging spine is a three-level replacement, not an extension: homotopy chiral locality, functorial convolution
𝐿
∞
L
∞
	​

/Maurer–Cartan deformation control, and logarithmic Fulton–MacPherson geometry on Ran/log-Ran.

Thought for 18m 32s

These three papers do not add three side-chapters. They force a three-axis refoundation:

strict chiral algebra must give way to homotopy chiral algebra at the chain/descent level; naive dg Lie “deformation complexes” must give way to filtered convolution
𝑠
𝐿
∞
sL
∞
	​

-algebras and Maurer–Cartan
∞
∞-groupoids; and ordinary Fulton–MacPherson spaces on smooth proper targets must give way, whenever punctures or nodal degenerations enter, to logarithmic Fulton–MacPherson spaces on pairs and semistable families. Malikov–Schechtman define homotopy chiral algebras and prove that the Čech complex of a sheaf of chiral algebras carries such a structure; Robert-Nicoud–Wierstra show convolution homotopy Lie algebras are the correct deformation objects and that their MC simplicial sets are homotopy invariant; Mok constructs
𝐹
𝑀
𝑛
(
𝑋
 ⁣
∣
𝐷
)
FM
n
	​

(X∣D) and its semistable degeneration package.

The shortest accurate slogan is:

strict chiral algebra
  
⇝
  
𝐶
ℎ
∞
,
dg Lie control
  
⇝
  
h
o
m
𝛼
(
−
,
−
)
 as filtered
𝑠
𝐿
∞
,
𝐹
𝑀
𝑛
(
𝑋
)
  
⇝
  
𝐹
𝑀
𝑛
(
𝑋
 ⁣
∣
𝐷
)
,
 
𝐹
𝑀
𝑛
(
𝑊
/
𝐵
)
.
strict chiral algebra⇝Ch
∞
	​

,dg Lie control⇝hom
α
	​

(−,−) as filtered sL
∞
	​

,FM
n
	​

(X)⇝FM
n
	​

(X∣D),FM
n
	​

(W/B).

If the monograph keeps the old objects as fundamental, it will remain brilliant but formally underived. If it promotes these three upgrades to axioms, it becomes the universal theory it wants to be.

What must change
1. The primitive local object is not a strict chiral algebra

Malikov–Schechtman’s point is not merely that “higher homotopies exist,” but that the correct descent object for a sheaf of chiral algebras is a homotopy chiral algebra, obtained by importing homotopy Lie machinery into the Beilinson–Drinfeld pseudo-tensor world. Their theorem says the Čech complex of a sheaf of chiral algebras on a smooth algebraic variety is an HCA, and in particular its cohomology is again a chiral algebra. So every place in the monograph where you pass to covers, Čech resolutions, derived global sections, or sheafified local-to-global arguments should be rewritten at the
𝐶
ℎ
∞
Ch
∞
	​

 level first, with strict chiral algebra appearing only after rectification or on cohomology.

Concretely, this means your current “
𝐴
∞
A
∞
	​

-chiral
→
→ PVA on cohomology” storyline is still not primitive enough. The chain-level story should become

𝐶
ℎ
∞
  
→
  
strict chiral algebra on
𝐻
∙
  
→
  
PVA/coisson shadow
.
Ch
∞
	​

→strict chiral algebra on H
∙
→PVA/coisson shadow.

That upgrade is what makes higher operations intrinsic rather than ornamental.

2. The universal deformation machine is a convolution homotopy Lie algebra

Vallette’s 2014 operadic homotopy theory gives the rectification layer:
∞
∞-morphisms are the correct morphisms between homotopy algebras, and any
∞
∞-quasi-isomorphism admits a homotopy inverse. Robert-Nicoud–Wierstra then identify the deformation complex of such data with a convolution
𝑠
𝐿
∞
sL
∞
	​

-algebra
h
o
m
𝛼
(
𝐷
,
𝐴
)
hom
α
	​

(D,A), relative to a twisting morphism
𝛼
α, and prove that the associated Deligne–Hinich–Getzler Maurer–Cartan simplicial sets are invariant under the relevant
∞
𝛼
∞
α
	​

-quasi-isomorphisms.

So every time the manuscript currently says, implicitly or explicitly, “the deformation complex is
H
o
m
(
𝐶
,
𝐴
)
Hom(C,A) with some bracket,” that should be replaced by:

deformation problem
  
=
  
𝑀
𝐶
∙
 ⁣
(
h
o
m
𝛼
(
𝐶
,
𝐴
)
)
.
deformation problem=MC
∙
	​

(hom
α
	​

(C,A)).

This is especially important for bulk–boundary maps, line-operator couplings, Koszul duality, and modular sewing data, where
∞
∞-morphisms are unavoidable.

There is also a crucial warning you should build into the book’s architecture: Robert-Nicoud–Wierstra prove that although convolution is functorial in either slot separately, there is no honest bifunctor taking
∞
∞-morphisms in both slots at once in general. That is a deep structural constraint, not a technical annoyance. It means the monograph must not pretend that all its bulk/boundary/line constructions are strictly two-sided functorial. Where both slots vary, you need a homotopy-coherent correspondence formalism, not a naive bifunctor.

3. The geometry of collisions must become logarithmic

Mok’s 2025 paper answers exactly the geometric question your modular and punctured-curve story needs answered. For a simple normal crossings pair
(
𝑋
,
𝐷
)
(X,D), she constructs
𝐹
𝑀
𝑛
(
𝑋
 ⁣
∣
𝐷
)
FM
n
	​

(X∣D) as an SNC compactification of
𝐶
𝑜
𝑛
𝑓
𝑛
(
𝑋
∖
𝐷
)
Conf
n
	​

(X∖D), built from stable grid expansions; its tropicalization is controlled by planted forests. For a semistable degeneration
𝑊
→
𝐵
W→B, she constructs a proper flat log-smooth degeneration
𝐹
𝑀
𝑛
(
𝑊
/
𝐵
)
→
𝐵
FM
n
	​

(W/B)→B, and proves a degeneration formula: each rigid special-fiber component is a birational modification of a product of smaller log FM spaces.

That means punctures, insertions, and nodal degenerations should no longer be treated as “ordinary FM plus comments.” They need their own geometric engine. In the finished monograph, configuration spaces on punctured curves, clutching of modular operations, and higher-genus degeneration formulas should all be recast on logarithmic FM spaces. This is the missing global support for your nonlinear modular shadows, planted-forest phenomena, and boundary/clutching residues.

4. Bulk–boundary–line needs an
∞
∞-level refoundation

Once you combine the first two papers, the correct local-to-global triangle is no longer:

bulk strict algebra
↔
boundary algebra
↔
line algebra
.
bulk strict algebra↔boundary algebra↔line algebra.

It becomes:

bulk
𝐶
ℎ
∞
  
⇝
  
boundary/defect MC objects in convolution
𝑠
𝐿
∞
  
⇝
  
strict shadows after rectification/cohomology
.
bulk Ch
∞
	​

⇝boundary/defect MC objects in convolution sL
∞
	​

⇝strict shadows after rectification/cohomology.

That changes how the monograph should present universal defects, boundary conditions, line operators, and bar/cobar duality. Their first definition should be via Maurer–Cartan data in filtered convolution algebras, not via already-strict objects. The strict dg-shifted Yangian, PVA, or boundary VOA should appear as the visible shadow.

5. Modular completion must be geometric, not just formal

Your higher-genus and modular chapters can now be made genuinely geometric. Mok’s rigid-type product formula is precisely the kind of clutching law needed to replace abstract sewing by a degeneration theorem on compactified collision spaces. The monograph’s “modular convolution algebra” should therefore be presented as living over a logarithmic degeneration package, with Maurer–Cartan equations interpreted over the rigid product strata. That is the point where the book stops being a genus-zero theory with a modular afterthought, and becomes a true all-genera local-to-global machine.

Volume-by-volume surgery
Volume I

First, split the configuration-space foundation into three layers: classical FM, logarithmic FM on pairs, and semistable degeneration of FM spaces. The log layer is not optional if punctures and modular degeneration are part of the narrative.

Second, in the higher-genus/modular sections, replace abstract sewing whenever possible by a log-degeneration/clutching argument. The rigid combinatorial types and planted-forest stratifications are the geometric incarnation of the modular decomposition you have been trying to express algebraically.

Third, recast every “modular deformation complex” as a filtered convolution
𝑠
𝐿
∞
sL
∞
	​

-algebra with MC
∞
∞-groupoid, not as a naive dg Lie algebra. The modular Maurer–Cartan element is then literally the object being glued across degeneration strata.

Fourth, promote “nonlinear modular shadows” from appendix-status to core text. It is where the logarithmic degeneration package actually lands.

Volume II

Insert, very early, a chapter called something like Homotopy chiral algebras and derived descent. Its main theorem should be the Malikov–Schechtman Čech/HCA theorem, plus the pseudo-tensor technology needed to use it.

Then insert a chapter called Convolution homotopy Lie algebras and deformation
∞
∞-groupoids. This is where Vallette + Robert-Nicoud–Wierstra become part of the book’s basic language:
∞
∞-morphisms, homotopy inverses, convolution
𝑠
𝐿
∞
sL
∞
	​

, one-sided functoriality, failure of naive bifunctoriality, and homotopy invariance of MC spaces.

After that, rewrite the PVA-descent chapter so the logic is:
chain-level
𝐶
ℎ
∞
Ch
∞
	​

 object → strict chiral algebra on cohomology → PVA/coisson shadow.
That is the correct direction of explanatory priority.

Finally, whenever the volume discusses HT perturbation theory, boundary transfer, celestial/bulk-boundary-line structures, or modular quantization, enlarge the configuration-space geometry from ordinary FM/raviolo spaces to logarithmic FM as soon as punctures, degeneration, or modularity appear.

The theorem packages the final book should contain

These should be presented in three tiers.

The proved-from-literature tier:

homotopy chiral descent for Čech complexes of sheaves of chiral algebras;

rectification and homotopy inversion for
∞
∞-morphisms of homotopy algebras;

convolution
𝑠
𝐿
∞
sL
∞
	​

-control of deformations and homotopy invariance of MC spaces;

logarithmic FM compactification, log-smooth degeneration, and rigid-component product formula.

The new synthesis theorems the monograph should prove:

logarithmic chiral/factorization descent on punctured and nodal curves;

logarithmic bar/cobar and logarithmic factorization homology packages;

modular Maurer–Cartan/clutching theorems over rigid degeneration strata;

bulk–boundary–line Koszul duality reformulated at the
𝐶
ℎ
∞
Ch
∞
	​

/convolution level.

The clearly marked conjectural frontier:

strictification criteria turning the relevant
𝐶
ℎ
∞
Ch
∞
	​

 objects back into strict chiral algebras in your modular/HT setting;

a full logarithmic chiral Koszul duality theorem;

a global correspondence formalism that resolves the no-bifunctor obstruction without cheating.

The deep philosophical change

The platonic ideal of the subject is not:

“strict chiral algebras on smooth curves, plus some higher operations, plus some FM geometry.”

It is:

“homotopy-coherent chiral/factorization objects on logarithmic pairs and degenerations, whose formal moduli are Maurer–Cartan
∞
∞-groupoids of convolution
𝐿
∞
L
∞
	​

-algebras, and whose global modular behavior is governed by logarithmic FM clutching geometry.”

That is the version in which the local algebra, the deformation theory, and the collision geometry finally line up.

I also put this into a repo-ready memo:

monograph_refoundation_plan.md
