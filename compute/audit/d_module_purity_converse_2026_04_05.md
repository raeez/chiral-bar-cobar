# D-Module Purity Converse: Analysis of the Missing Direction

## Date: 2026-04-05
## Status: OPEN (theoretical analysis, no proof)

## 1. The Problem

**Theorem** (thm:koszul-equivalences-meta, item (xii)): Each bar component
$\bar{B}_n^{ch}(\mathcal{A})$ is pure of weight $n$ as a mixed Hodge module,
with characteristic variety aligned to FM boundary strata.

**Proved**: (x) => (xii), equivalently: Koszul => D-module pure.
The proof goes through FM boundary acyclicity: Koszulness gives E_2-collapse
of the PBW spectral sequence, which forces boundary restrictions to be
acyclic, which implies purity + alignment.

**Open**: (xii) => (x), equivalently: D-module pure => Koszul.
The question: does purity + characteristic variety alignment of the bar
D-module force FM boundary acyclicity, hence bar concentration, hence
Koszulness?

**Precise formulation** (from concordance.tex, line 9087):
> Does holonomicity of the D-module structure of $\Theta^{oc}_A$ on Ran(X)
> force cohomological concentration of the underlying cochain complex?

**The conjecture** (conj:d-module-purity-koszulness in
bar_cobar_adjunction_inversion.tex, line 2449): $\mathcal{A}$ is chirally
Koszul if and only if:
- (i) Each $\bar{B}_n^{ch}(\mathcal{A})$ is pure of weight $n$ as a mixed
  Hodge module on $\overline{\mathrm{Conf}}_n(X)$.
- (ii) $\mathrm{Ch}(\bar{B}_n^{ch}(\mathcal{A})) \subset \bigcup_S
  T^*_S \overline{\mathrm{Conf}}_n(X)$ (characteristic variety aligned to
  boundary strata).

## 2. What Is Already Known

### 2a. The forward direction: (x) => (xii) (PROVED)

The existing proof (rem:d-module-purity-content, line 2483):
- Purity + alignment => the Leray spectral sequence for $i_S^! \bar{B}_n$
  degenerates at E_1.
- Alignment puts the E_1 terms in degree zero.
- Therefore: FM boundary restrictions are acyclic outside degree 0 = condition (x).
- And (x) <=> (i) (Koszulness) is already proved.

So the logical chain of the FORWARD direction is:
Koszul = (i) <=> (x) => purity + alignment = (xii).

The EXISTING proof of (x) => (xii) is:
FM boundary acyclicity at all strata => the bar D-module has no off-diagonal
cohomological contributions => the weight filtration is concentrated => pure
of the correct weight => alignment follows from the fact that all
singularities of the bar differential are supported on collisions
(FM boundary strata).

### 2b. The classical precedent: BGS96

Beilinson-Ginzburg-Soergel [BGS96] proved, for graded algebras arising from
geometry: Koszulness <=> purity <=> formality <=> derived equivalence.

The key result: $\mathrm{Ext}^i_A(k,k)$ carries a pure Hodge structure of
weight $i$ if and only if $A$ is Koszul.

In the BGS setting, the proof of the converse (purity => Koszul) uses:
1. The algebra A arises from the category of perverse sheaves on a
   stratified space (flag variety G/B).
2. Purity of the Ext groups means the weight filtration on
   $\mathrm{Ext}^i(k,k)$ is concentrated in a single weight.
3. This forces the E_2 page of the weight spectral sequence to be
   concentrated, giving E_2-degeneration.
4. E_2-degeneration of the weight spectral sequence => diagonal Ext-vanishing
   => Koszulness.

**Critical point**: BGS use the GEOMETRIC ORIGIN of the algebra to get a
weight structure on Ext. The algebra A = Ext(IC, IC) for IC sheaves on
Schubert varieties, and purity comes from the decomposition theorem
(BBD + Deligne).

### 2c. Bar complex structure

The bar components $\bar{B}_n^{ch}(\mathcal{A})$ are:
- Regular holonomic D-modules (Lemma lem:bar-holonomicity).
- Supported on $\overline{\mathrm{Conf}}_n(X)$ (Fulton-MacPherson
  compactification).
- The bar differential is a D-module map.
- The PBW spectral sequence is the spectral sequence associated to the
  bar-degree filtration.

## 3. Analysis of Four Approaches

### APPROACH A: Weight Filtration Forces Spectral Sequence Collapse

**Idea**: If $\bar{B}_n^{ch}(\mathcal{A})$ is pure of weight $n$ as a mixed
Hodge module, the weight filtration on its cohomology is concentrated. The PBW
spectral sequence should then degenerate, giving Koszulness.

**Detailed analysis**:

Step 1: Saito's theory gives a weight filtration $W_\bullet$ on any mixed
Hodge module M on a smooth variety. For a pure MHM of weight $w$, we have
$\mathrm{Gr}^W_k(M) = 0$ for $k \neq w$.

Step 2: The bar differential $d: \bar{B}_n \to \bar{B}_{n-1}$ is a morphism
of D-modules. If $\bar{B}_n$ is pure of weight $n$, then $d$ is a morphism
from a pure object of weight $n$ to a pure object of weight $n-1$.

Step 3: In the category of mixed Hodge modules (abelian, with strict
morphisms by Saito's theorem), a morphism between pure objects of DIFFERENT
weights must be either zero or involve a nontrivial extension. More precisely:
Saito's strictness theorem says that any morphism $f: M \to N$ of MHM is
strict with respect to the weight filtration. If M is pure of weight $n$ and
N is pure of weight $m$ with $n \neq m$, then $f$ is either zero (if there is
no weight overlap) or its image has a specific weight structure.

**Gap identified**: This is where the argument requires care. The bar
differential d: bar_n -> bar_{n-1} is a map between pure objects of
ADJACENT weights (n and n-1). In the MHM category, such a map is
automatically strict with respect to the weight filtration, but it need not
be zero. Its image im(d) is a sub-MHM of bar_{n-1} (which is pure of weight
n-1), and its kernel ker(d) is a sub-MHM of bar_n (pure of weight n).

The cohomology H^n(bar) = ker(d_n)/im(d_{n+1}) is a quotient of a sub-MHM
of a pure weight-n object by a sub-MHM coming from a pure weight-(n+1)
object. By strictness, this quotient is itself a mixed Hodge module, and we
need to determine its weight.

**Key question**: If bar_n is pure of weight n for ALL n, does it follow that
H^n(bar) is pure of weight n?

**Answer**: YES, by Saito's strictness. Here is the argument:
- $d_{n+1}: \bar{B}_{n+1} \to \bar{B}_n$ is a morphism of MHM.
- $\bar{B}_{n+1}$ is pure of weight $n+1$, $\bar{B}_n$ is pure of weight $n$.
- im($d_{n+1}$) is a sub-MHM of $\bar{B}_n$, hence has weight $\leq n$.
- But im($d_{n+1}$) is also a quotient of $\bar{B}_{n+1}$ (pure weight $n+1$),
  hence has weight $\geq n+1$.
- **WAIT**: this is a contradiction unless im($d_{n+1}$) = 0.

**THIS IS THE KEY OBSERVATION**: If $\bar{B}_n$ is pure of weight $n$ for all
$n$, and the bar differential $d: \bar{B}_{n+1} \to \bar{B}_n$ is a morphism
of MHM, then Saito's strictness forces im($d$) to be simultaneously a
quotient of a pure weight-$(n+1)$ object and a subobject of a pure weight-$n$
object. A mixed Hodge module that is both of weight $\geq n+1$ (as a
quotient) and weight $\leq n$ (as a subobject) must be zero.

**Therefore: d = 0 on the MHM level.**

But WAIT -- this proves TOO MUCH. If the bar differential is identically
zero as a MHM map, then H^n(bar) = bar_n for all n, which means the bar
cohomology is the entire bar complex. This cannot be right for non-trivial
algebras.

**The error in the above reasoning**: The bar differential d is NOT a morphism
of MHM from the pure weight-n piece to the pure weight-(n-1) piece. The issue
is what "pure of weight n" means here.

Let me reconsider. The conjecture says $\bar{B}_n^{ch}(\mathcal{A})$ is pure
of weight $n$ as a mixed Hodge module. But $\bar{B}_n$ is the n-th bar
component, which lives on $\overline{\mathrm{Conf}}_n(X)$. The bar
differential maps between DIFFERENT configuration spaces:
$d: \bar{B}_n \to \bar{B}_{n-1}$ involves a pushforward from
$\overline{\mathrm{Conf}}_n$ to $\overline{\mathrm{Conf}}_{n-1}$ (by
collapsing two points).

So the bar differential is NOT simply a morphism in the category of MHM on a
fixed space. It involves pushforward/pullback along correspondences on the
FM compactifications. The weight argument above is too naive because it treats
the bar complex as living on a single space.

**Revised assessment of Approach A**:

The purity hypothesis is about each bar component $\bar{B}_n$ individually,
living on its own configuration space $\overline{\mathrm{Conf}}_n(X)$. The
bar differential involves geometric operations (pushforward under collision
maps) that move between different configuration spaces.

The weight-strictness argument fails because:
1. The bar differential d is not an endomorphism of a single MHM.
2. It is a morphism involving functorial operations (pushforward, pullback)
   between MHM categories on DIFFERENT spaces.
3. These functorial operations can shift weights.

Specifically: if $f: Y \to Z$ is a proper map between smooth varieties,
Saito's theory gives:
- $f_*$ preserves the bounded derived category of MHM.
- $f_*$ of a pure MHM of weight $w$ has weights $\leq w$ (by the
  decomposition theorem, it SPLITS as a direct sum of shifted IC sheaves,
  each pure of some weight $\leq w$).
- More precisely, for a proper map, $f_*$ preserves purity by the
  decomposition theorem (BBD).

So the collision pushforward from Conf_n to Conf_{n-1} PRESERVES purity. The
pullback (restriction to boundary strata) also preserves purity for smooth
morphisms. But the bar differential is not purely a pushforward -- it involves
the OPE residue extraction, which is a D-module operation involving
logarithmic poles.

**Bottom line for Approach A**: The weight-filtration approach is structurally
sound in principle, but the multi-space nature of the bar complex and the
non-trivial nature of the bar differential (involving logarithmic residues
along collisions) make a clean weight argument difficult. The key missing
piece is understanding how the weight filtration interacts with the specific
form of the bar differential (d-log extraction of OPE singularities).

**Verdict**: PARTIALLY VIABLE, but requires significant new work to make
rigorous. The naive strictness argument fails because the bar complex lives
on multiple spaces.

### APPROACH B: Saito's Theory on Ran(X)

**Idea**: Apply Saito's mixed Hodge module theory directly on the Ran space.

**Obstacles**:

1. **Ran(X) is an ind-scheme, not a variety.** Saito's theory of mixed Hodge
   modules is defined for algebraic varieties (or complex manifolds). The Ran
   space $\mathrm{Ran}(X) = \coprod_{n \geq 0} X^n / \Sigma_n$ (as a
   topological space) or its algebro-geometric avatar as a presheaf on the
   category of finite sets is NOT a variety.

2. **Factorization structure is not geometric.** The factorization structure
   of the bar complex (the cocomposition maps) involves correspondences
   $\mathrm{Ran}(X) \times_{\mathrm{Ran}(X)} \mathrm{Ran}(X)$
   (partial overlap maps) that are not morphisms of varieties.

3. **No MHM theory on Ran.** There is currently no published extension of
   Saito's MHM theory to ind-schemes or prestacks that would cover the Ran
   space. One would need either:
   (a) A pro-finite stratification of the Ran space compatible with MHM, or
   (b) An ind-limit construction on $\{X^n\}_{n \geq 0}$ with compatible
       weight structures.

4. **Possible workaround**: Work stratum-by-stratum. Each bar component
   $\bar{B}_n$ lives on $\overline{\mathrm{Conf}}_n(X)$, which IS a smooth
   projective variety (the FM compactification). Saito's theory applies to
   each one individually. The difficulty is encoding the GLOBAL structure
   (the bar differential, the factorization coalgebra structure) in terms of
   the individual MHM on each configuration space.

**Verdict**: NOT VIABLE with current technology. Saito's theory does not
extend to ind-schemes in published literature. The stratum-by-stratum
approach reduces to Approach A.

### APPROACH C: Beilinson-Bernstein Localization Analogy

**Idea**: In the classical BGS setting, the algebra arises from perverse
sheaves on G/B, and purity is equivalent to semisimplicity of the
representation category (via BB localization). Can we make a similar
identification for chiral algebras?

**The classical picture** (BGS96):
1. Category O for $\mathfrak{g}$ <=> D-modules on G/B (BB localization).
2. IC sheaves on Schubert varieties correspond to simple objects in O.
3. Ext(IC, IC) is Koszul <=> each IC is pure (decomposition theorem).
4. Koszulness of Ext <=> category O is "Koszul" (homological grading matches
   weight grading).

**The chiral picture** (from the manuscript):
1. Modules for $\hat{\mathfrak{g}}_k$ <=> D-modules on G/B at level k
   (Frenkel-Gaitsgory localization, thm:chiral-localization).
2. The bar complex computes localization (prop:bar-localization):
   $H^i(\bar{B}^{ch}(\hat{\mathfrak{g}}_k, M)) \cong H^i(G/B, \Delta_k(M))$.
3. For dominant generic level, $H^i = 0$ for $i > 0$ and $H^0 = M$.

**Can we use this?** The chiral localization identifies the bar complex with
a geometric object (D-modules on the flag variety). The purity of the bar
complex would then correspond to purity of certain D-modules on G/B, which
by the BGS theory is equivalent to Koszulness.

**Gap**: This argument works only for affine Kac-Moody algebras
$\hat{\mathfrak{g}}_k$, where chiral localization exists. It does NOT
immediately generalize to:
- Virasoro (no flag variety).
- W-algebras (localization via DS reduction, not directly on G/B).
- Free fields (trivially Koszul, so the converse holds vacuously).
- General chiral algebras (no localization theorem available).

**For affine KM specifically**, the argument would be:
1. Bar components are D-modules on $\overline{\mathrm{Conf}}_n(X)$.
2. Via chiral localization, these correspond to D-modules on products
   of copies of the affine flag variety.
3. Purity of these D-modules, by the decomposition theorem and BGS,
   implies Koszulness of the underlying algebra.

**But wait**: the bar complex does NOT directly localize to the flag variety
in the multi-point setting. The bar complex $\bar{B}_n$ lives on
$\overline{\mathrm{Conf}}_n(X)$, while the localization sends a single
module to a D-module on G/B at a single point. The multi-point bar complex
involves n-fold configuration space, not n copies of G/B.

**Revised assessment**: The BB localization provides a bridge for SINGLE-POINT
data (individual bar components restricted to a point), but the multi-point
bar differential (which encodes OPE collisions) does not have a clean
localization interpretation on products of flag varieties.

**Verdict**: PARTIALLY VIABLE for affine KM only, and even there, requires
new work to handle the multi-point bar differential. Not generalizable to
Virasoro, W-algebras, or arbitrary chiral algebras.

### APPROACH D: Contrapositive (NOT Koszul => NOT pure)

**Idea**: If bar cohomology is NOT concentrated (i.e., $\mathcal{A}$ is not
Koszul), exhibit a non-pure weight in the bar D-module.

**Detailed analysis**:

If $\mathcal{A}$ is not Koszul, then by the equivalence (i) <=> (ii), the PBW
spectral sequence does NOT collapse at E_2. This means there exists some
$d_r \neq 0$ for $r \geq 2$.

Step 1: A nontrivial differential $d_r$ on the PBW spectral sequence means
there exists a class in $E_r^{p,q}$ that maps nontrivially to
$E_r^{p+r, q-r+1}$. The bar cohomology has contributions in more than one
bar degree.

Step 2: Need to show this implies $\bar{B}_n$ is NOT pure of weight $n$ for
some $n$, or the characteristic variety is NOT aligned.

**The mechanism**: If $d_r \neq 0$, there is an off-diagonal class in the
bar cohomology. The weight of a bar cohomology class is determined by its
position in the PBW spectral sequence. An off-diagonal class
$H^{p,q}(\bar{B})$ with $p \neq q$ would come from a class that has
contributed through nontrivial extensions in the spectral sequence. In the
MHM framework, these extensions correspond to mixed (non-pure) structures.

**The key point**: If the E_2 page has nontrivial classes both on and off the
diagonal, and these classes are connected by d_r differentials, then the
resulting cohomology has a weight structure that involves EXTENSIONS between
different weights. Such extensions are precisely what it means to be non-pure.

**More precisely**: Consider the total bar complex as a filtered object (by
bar degree). The spectral sequence is the weight spectral sequence of this
filtration. If it does not degenerate at E_2, then the filtration is not
split, which means the bar complex has non-trivial extensions between
different weight pieces. This is exactly the failure of purity.

**But is this rigorous?** The issue is that the PBW filtration on the bar
complex is NOT the same as the weight filtration from Saito's theory. The
PBW filtration is an algebraic filtration (by bar degree / tensor length),
while the weight filtration is a Hodge-theoretic construction.

For the contrapositive to work, we need: the PBW filtration on bar is
COMPATIBLE with the weight filtration from MHM. More precisely, we need:

(**) The PBW grading on $\bar{B}_n$ (which gives bar degree $n$) is the
SAME as the weight grading from Saito's MHM theory (which gives weight $n$
when $\bar{B}_n$ is pure).

If (**) holds, then:
- Purity of weight $n$ means the weight filtration is concentrated, which
  means the PBW filtration is split.
- Split PBW filtration means E_2-collapse (no nontrivial extensions).
- E_2-collapse = Koszulness.
- Conversely, failure of Koszulness = non-split PBW filtration = non-pure.

**The identification (**) is the central missing ingredient.** It says that
the algebraic structure of the bar complex (PBW filtration) is compatible
with the transcendental structure (Hodge filtration / weight filtration).

**Verdict**: MOST PROMISING approach. The contrapositive reduces to proving
the compatibility (**) between the PBW filtration and the Hodge-theoretic
weight filtration. This is a natural statement: the bar complex is built
from algebraic data (OPE coefficients), and its filtration structure should
be compatible with the algebro-geometric weight structure.

## 4. The Decisive Obstruction: PBW = Weight Compatibility

All four approaches converge on the same obstruction: the identification of
the algebraic PBW filtration with the Hodge-theoretic weight filtration.

**What would suffice**: A theorem stating that for a chiral algebra
$\mathcal{A}$ satisfying the standing hypotheses:

> The PBW filtration $F_\bullet$ on $\bar{B}_n^{ch}(\mathcal{A})$ coincides
> with the weight filtration $W_\bullet$ from Saito's theory of mixed Hodge
> modules on $\overline{\mathrm{Conf}}_n(X)$.

Given this identification:
- Purity (weight filtration concentrated) <=> PBW filtration split <=>
  E_2-collapse <=> Koszulness.
- The converse direction follows immediately.

**Evidence for this identification**:

1. **Classical precedent**: For algebras arising from perverse sheaves on
   stratified varieties (BGS setting), the grading filtration IS the weight
   filtration. The analogy extends: the PBW filtration on the bar complex
   plays the role of the grading in the classical setting.

2. **Geometric structure**: The PBW filtration on $\bar{B}_n$ is compatible
   with the FM boundary stratification (the $p$-th filtration step involves
   at most $p$ collision strata). The weight filtration from MHM theory is
   also compatible with the stratification (by Saito's theory, the weight
   filtration is functorial with respect to the stratification).

3. **For quadratic algebras**: When $\mathcal{A}$ is quadratic, the weight
   filtration on $\bar{B}_n^{ch}$ is bounded and the PBW spectral sequence
   collapses at E_2 (rem:comparison-classical, line 3299). In this case, the
   identification (**) holds trivially because both filtrations are
   concentrated.

4. **For the standard landscape**: All standard families (Heisenberg, KM,
   Virasoro, W-algebras) are Koszul (proved by PBW universality). For these,
   purity holds and the identification is automatic (both filtrations are
   concentrated in the Koszul case).

**Obstacles to proving the identification**:

1. The PBW filtration is defined ALGEBRAICALLY (by tensor length in the
   symmetric algebra), while the weight filtration is TRANSCENDENTAL (from
   Hodge theory). Showing they coincide requires a BRIDGE between algebraic
   and transcendental structures. In the BGS setting, this bridge is provided
   by the geometry of Schubert varieties (intersection cohomology = KL
   polynomials = BGG resolution). In the chiral setting, the analogous bridge
   would come from the geometry of FM compactifications and the factorization
   structure.

2. The bar complex on $\overline{\mathrm{Conf}}_n(X)$ is NOT a priori an IC
   sheaf or a standard/costandard object in a weight structure. It is a
   specific D-module constructed from OPE data. Showing it has the
   "right" weight structure requires understanding the MHM structure of
   OPE-derived D-modules.

3. The weight filtration depends on the complex structure of X (through
   Saito's theory), while the PBW filtration is algebraic (depends only on
   the OPE data of $\mathcal{A}$). The identification would imply that
   the weight structure is determined by the OPE, which is a non-trivial
   content.

## 5. A Fifth Approach: Direct FM Analysis

There is a fifth approach that does not require the full PBW = weight
identification. It uses the specific structure of the conjecture: purity +
characteristic variety alignment.

**The conjecture has TWO conditions, not one.** Condition (i) is purity;
condition (ii) is characteristic variety alignment to FM boundary strata.

The alignment condition (ii) is strong: it says
$\mathrm{Ch}(\bar{B}_n) \subset \bigcup_S T^*_S \overline{\mathrm{Conf}}_n(X)$.

For a regular holonomic D-module with characteristic variety supported on
the union of conormal bundles to strata, the following is known:
- The D-module is a SUCCESSIVE EXTENSION of rank-one flat connections along
  boundary strata (rem:d-module-purity-content, line 2480).
- The restriction to each stratum $i_S^! \bar{B}_n$ computes the
  monodromy/residue data of these flat connections.

Combined with purity:
- Purity says the MHM is concentrated in a single weight.
- For a pure MHM with characteristic variety supported on boundary strata,
  the Leray spectral sequence for $i_S^!$ degenerates at E_1 (because
  purity forces all extension data to split).

**This is exactly the argument of rem:d-module-purity-content**: "Together,
(i) and (ii) imply FM boundary acyclicity: purity forces the Leray spectral
sequence for $i_S^! \bar{B}_n$ to degenerate at E_1, and alignment puts the
E_1 terms in degree zero."

So the FORWARD direction (purity + alignment) => FM boundary acyclicity =>
Koszulness is ALREADY PROVED in the manuscript, as stated. Wait -- let me
re-examine the direction carefully.

**Re-reading the theorem**: The theorem states "(x) implies (xii)."
That is: FM boundary acyclicity => D-module purity. And the remark says
"(i) and (ii) imply FM boundary acyclicity" -- this is (xii) => (x), the
CONVERSE.

**CRITICAL FINDING**: Re-reading the source more carefully:

At line 2483-2486 (rem:d-module-purity-content):
"Together, (i) and (ii) imply FM boundary acyclicity
(Theorem thm:fm-boundary-acyclicity): purity forces the Leray spectral
sequence for $i_S^! \bar{B}_n$ to degenerate at E_1, and alignment puts the
E_1 terms in degree zero."

This says (xii) => (x), i.e., purity + alignment => FM boundary acyclicity
=> Koszulness. This IS the converse direction.

But the theorem header says "Condition (x) implies condition (xii)" -- i.e.,
(x) => (xii), the forward direction. And the remark at line 2105 says
"Condition (x) implies condition (xii), but the converse direction is still
open."

**There is a TENSION in the manuscript.** The remark at line 2483 sketches an
argument for (xii) => (x), while the remark at line 2105 says the converse
is still open.

Let me parse this carefully:

1. **Theorem statement** (line 1808): "(x) implies (xii)." Forward only.
2. **Remark (line 2102-2107)**: "(x) implies (xii), but the converse
   direction is still open."
3. **Remark (line 2483-2486)**: "Together, (i) and (ii) imply FM boundary
   acyclicity." This APPEARS to be the converse.
4. **Summary (line 2872)**: "The implication (e)=>(d) is proved; the converse
   is open." Here (e) = Hodge-pure + alignment, (d) = FM boundary acyclicity.
   So (e) => (d) is proved, meaning PURITY => BOUNDARY ACYCLICITY.

Wait -- this is confusing. Let me resolve:

Line 2872 says: (e) => (d) is proved. Here (e) = D-module purity, (d) = FM
boundary acyclicity. So "D-module purity => FM boundary acyclicity" IS proved.
And FM boundary acyclicity <=> Koszul is proved (it's one of the 10
unconditional equivalences).

**So: D-module purity (with alignment) => FM boundary acyclicity => Koszul
IS PROVED.** The converse that is open is (d) => (e), i.e., FM boundary
acyclicity => D-module purity.

**Let me recheck**: The theorem says "(x) implies (xii)." That is:
(x) = FM boundary acyclicity => (xii) = D-module purity. This is the forward
direction. The converse "(xii) => (x)" would be "D-module purity =>
FM boundary acyclicity."

But line 2872 says "(e) => (d) is proved" where (e) = purity + alignment and
(d) = FM boundary acyclicity. So (xii) => (x) IS proved!

**RESOLUTION**: There is an INCONSISTENCY in the manuscript. The summary at
line 2872 says "(e)=>(d) is proved" (purity => boundary acyclicity), which
combined with (d)<=>(a) (boundary acyclicity <=> Koszul) would give
(e)=>(a) (purity => Koszul), closing the gap. But the theorem statement
at line 1808 says only "(x) implies (xii)" (the other direction), and
line 2105 says "the converse direction is still open."

**Let me re-read line 2872 one more time**: "The implication (e)=>(d) is
proved; the converse is open."

OK so (e) = "Hodge-theoretic" = D-module purity + alignment. (d) =
"Geometric" = FM boundary acyclicity. "(e)=>(d) is proved" means
purity+alignment => boundary acyclicity. "The converse is open" means
boundary acyclicity does NOT necessarily imply purity+alignment.

So the situation is:
- PROVED: Koszul <=> FM boundary acyclicity <=> ... (10 equivalences)
- PROVED: D-module purity + alignment => FM boundary acyclicity => Koszul
- OPEN: Koszul => D-module purity + alignment (i.e., (x)=>(xii))

WAIT. That contradicts line 1808 which says "(x) implies (xii)."

**Let me re-read one more time.**

Line 1808: "Condition (x) implies condition (xii)."
This means FM boundary acyclicity => D-module purity.

Line 2872: "(e)=>(d) is proved; the converse is open."
(e) = purity+alignment, (d) = boundary acyclicity.
"(e)=>(d) proved" = purity => boundary acyclicity.
"converse open" = boundary acyclicity does not necessarily => purity.

These are CONSISTENT: both directions use the same two conditions but in
different letters. The situation is:

**BOTH DIRECTIONS ARE CLAIMED PROVED:**
- (x) => (xii): FM boundary acyclicity => D-module purity. CLAIMED in
  theorem statement (line 1808).
- (xii) => (x): D-module purity + alignment => FM boundary acyclicity.
  CLAIMED in remark (line 2483) and summary (line 2872: "(e)=>(d) is proved").

But the remark at line 2105 says "the converse direction is still open."

**This is a genuine inconsistency.** The theorem proves (x) => (xii). The
remark proves (xii) => (x). Yet the status remark says the converse is open.

**Resolution**: The most likely reading is:
- In the meta-theorem (thm:koszul-equivalences-meta), condition (xii) is
  listed as a ONE-DIRECTIONAL consequence: (x) => (xii).
- The remark at line 2483 sketches the argument for (xii) => (x), but this
  argument is taken as HEURISTIC rather than fully rigorous (it relies on
  the Leray degeneration claim which may require verification).
- The summary at line 2872 may be using a different convention.

**Let me check what exactly the Leray degeneration claim requires:**

"Purity forces the Leray spectral sequence for $i_S^! \bar{B}_n$ to
degenerate at E_1."

This is standard for PROPER maps of algebraic varieties with pure source:
the Leray spectral sequence degenerates by the decomposition theorem (BBD).

But here $i_S: S \hookrightarrow \overline{\mathrm{Conf}}_n(X)$ is a CLOSED
INCLUSION (of a boundary stratum), not a proper map. The functor $i_S^!$ is
the exceptional pullback (right adjoint of $i_{S,!}$), which for a closed
inclusion in a smooth ambient space equals $i_S^* \otimes \omega_{S/X}[\dim]$
(shifted Verdier dual of ordinary pullback).

For a CLOSED inclusion $i: Z \hookrightarrow X$, the functor $i^!$ on
D-modules corresponds to restriction to the formal neighborhood of Z,
followed by taking nearby cycles / specialization. For regular holonomic
D-modules, $i^!$ preserves the MHM structure.

**The Leray spectral sequence for $i_S^!$ on a pure MHM**: If M is pure of
weight w on X and $i: Z \hookrightarrow X$ is a closed inclusion with Z
smooth of codimension d, then $i^!(M)$ is a mixed Hodge module on Z with
weights in $[w-d, w]$ (by Saito's theory). Purity of the INPUT does NOT
automatically give purity of $i^!(M)$ -- it gives a BOUNDED weight range.

Degeneration of the Leray spectral sequence at E_1 follows from purity of
M TOGETHER with the alignment condition (ii). Alignment says the
characteristic variety is contained in the union of conormal bundles to
strata. For a D-module with characteristic variety supported on $T^*_Z X$
(the conormal to Z), the restriction $i_Z^!$ is concentrated in a single
degree (the codimension shift). This is what the remark means by "alignment
puts the E_1 terms in degree zero."

**So the argument IS rigorous**, assuming:
(a) The bar components are regular holonomic D-modules (PROVED:
    lem:bar-holonomicity).
(b) The MHM structure exists (NEED: the bar components live on smooth
    projective FM compactifications, so Saito's theory applies).
(c) Purity + alignment => Leray degeneration (STANDARD from Saito's theory
    + the explicit alignment hypothesis).

**Updated conclusion**: The argument (xii) => (x) outlined in
rem:d-module-purity-content IS rigorous, given the hypothesis that the bar
components carry MHM structure. The remark at line 2105 ("converse still
open") appears to be stale or to refer to a WEAKER version of (xii) (perhaps
purity alone, without alignment).

**The actual open direction** may be: FM boundary acyclicity => D-module
purity (with alignment). That is: given that bar cohomology is concentrated,
prove that the bar D-modules are pure and have aligned characteristic
variety. This is the forward direction (x) => (xii), which IS stated in the
theorem but whose proof within the theorem block is not explicitly written
out (the proof block only covers the 10 unconditional equivalences and the
Lagrangian criterion).

## 6. Precise Status Assessment

After careful reading of all sources, the situation is:

### CRITICAL FINDING: Directional inconsistency between two files

**In chiral_koszul_pairs.tex** (thm:koszul-equivalences-meta, line 1808):
"Condition (x) implies condition (xii)."
Items: (x) = FM boundary acyclicity, (xii) = D-module purity + alignment.
Claimed direction: (x) => (xii), i.e., Koszul => pure.

**In bar_cobar_adjunction_inversion.tex** (summary remark, line 2872):
"The implication (e)=>(d) is proved; the converse is open."
Items: (e) = D-module purity + alignment, (d) = FM boundary acyclicity.
Claimed direction: (e) => (d), i.e., pure => Koszul.
Open direction: (d) => (e), i.e., Koszul => pure.

The label mapping between the two files:
(x) in chiral_koszul_pairs = (d) in bar_cobar_adjunction_inversion
(xii) in chiral_koszul_pairs = (e) in bar_cobar_adjunction_inversion

**The meta-theorem claims (x)=>(xii), i.e., (d)=>(e).**
**The summary remark says (d)=>(e) is OPEN.**

These are CONTRADICTORY. The meta-theorem claims a direction that the
summary remark says is open.

### Resolution of the inconsistency

The proof block of thm:koszul-equivalences-meta does NOT contain a proof of
(x) => (xii). The proof covers only the 10 unconditional equivalences
(i)-(x) and the Lagrangian criterion (xi). The D-module purity item (xii) is
mentioned only in the theorem header, with no proof written.

**Assessment**: The summary remark in bar_cobar_adjunction_inversion.tex is
MORE LIKELY CORRECT. The situation is:

- **PROVED: (xii) => (x)**, i.e., D-module purity + alignment => FM boundary
  acyclicity => Koszulness. The argument (rem:d-module-purity-content, line
  2483): purity forces Leray spectral sequence degeneration; alignment puts
  the E_1 terms in degree 0; together they give boundary acyclicity.
  This argument is standard from Saito's MHM theory.

- **OPEN: (x) => (xii)**, i.e., Koszulness => D-module purity + alignment.
  The theorem header at line 1808 claims this, but no proof appears in the
  proof block. The implicit argument (E_2-collapse => bar concentration =>
  the bar D-module is pure) requires establishing that bar concentration
  implies purity of the bar D-module, which is a non-trivial claim about the
  Hodge theory of configuration space D-modules. This argument is NOT written.

**The meta-theorem header at line 1808 should either be corrected to
"Condition (xii) implies condition (x)" (the proved direction) or the
corresponding proof should be supplied.**

### Corrected status:

1. **10 unconditional equivalences (i)-(x)**: FULLY PROVED with explicit
   proof chains in the theorem block.

2. **(xii) => (x)** (D-module purity + alignment => Koszulness): PROVED
   by the Leray degeneration argument (rem:d-module-purity-content, line
   2483). This argument uses Saito's MHM theory applied to the closed
   inclusion of FM boundary strata.

3. **(x) => (xii)** (Koszulness => D-module purity + alignment): OPEN.
   Stated in the theorem header (line 1808) but no proof is given. The
   implicit argument requires showing that bar concentration implies purity
   of the bar D-module, which is not established.

### What is genuinely OPEN:

The forward direction (x) => (xii): does Koszulness (bar concentration)
imply D-module purity of the bar complex? This requires showing that the
bar D-module, which is constructed from algebraic OPE data and lives on FM
compactifications, acquires a pure Hodge structure when bar cohomology is
concentrated. The manuscript does not contain this argument.

The separate question of whether alignment is automatic (does purity alone
imply alignment?) is also open.

## 7. Recommendations

### 7a. Immediate manuscript corrections needed

**FINDING (SERIOUS)**: The meta-theorem header (chiral_koszul_pairs.tex, line
1808) claims "(x) implies (xii)" (Koszul => D-module pure), but:
1. No proof appears in the proof block.
2. The summary remark (bar_cobar_adjunction_inversion.tex, line 2872) says
   the opposite direction "(e)=>(d)" is proved and "(d)=>(e)" is open,
   which (under the label mapping) means (xii)=>(x) is proved and
   (x)=>(xii) is open.

**Correction needed**: The theorem header at line 1808 should read either:
(a) "Condition (xii) implies conditions (i)-(x)" (the proved direction), or
(b) "Conditions (i)-(x) are equivalent to condition (xii)" if a proof of
    the forward direction can be supplied.

The remark at line 2105 ("the converse direction is still open") is
CONSISTENT with the summary remark and should remain as-is. It correctly
describes the open problem: Koszulness => D-module purity is unproved.

**Severity**: SERIOUS (AP40-type: theorem claims a direction whose proof is
absent). The LaTeX environment is a theorem, and the header claims an
implication that is not proved in the proof block. This is an instance of
AP4 (status tag as ground truth) combined with AP40 (environment contradicts
content).

### 7b. Theoretical path forward

The cleanest path to a full resolution has three steps:

**Step 1** (verifiable with current tools): Verify that the argument of
rem:d-module-purity-content is fully rigorous. This requires checking that
Saito's Leray degeneration theorem applies to the specific closed inclusion
$i_S: S \hookrightarrow \overline{\mathrm{Conf}}_n(X)$ for FM boundary
strata, with the MHM structure on bar components from lem:bar-holonomicity.

**Step 2** (requires new work): Prove the forward direction (x) => (xii)
properly. Show that Koszulness (bar concentration) implies purity of the
bar D-module. The argument: bar concentration means the bar complex has
cohomology only in degree 1. The PBW spectral sequence degenerates. The
resulting D-module $H^1(\bar{B}_n)$ inherits a pure Hodge structure from
the PBW splitting. The characteristic variety alignment comes from the
factorization structure (all singularities are on FM boundary strata by
construction).

**Step 3** (the deepest question): Determine whether alignment is a
CONSEQUENCE of purity (making condition (ii) redundant) or an independent
condition. In the BGS setting, alignment is automatic for category O
representations (the characteristic variety of a D-module on G/B is
contained in the union of conormal bundles to Schubert varieties by the
Borho-Brylinski theorem). In the chiral setting, this would require a
structural theorem about D-modules on FM compactifications arising from
chiral algebras.

### 7c. Strategy ranking

1. **APPROACH D + E (contrapositive + FM analysis)**: Most promising.
   The argument (xii) => (x) via Leray degeneration appears sound and may
   already close the gap if Step 1 above succeeds. Priority: HIGH.

2. **APPROACH A (weight filtration)**: Sound in principle but blocked by
   the multi-space nature of the bar complex. Priority: MEDIUM.

3. **APPROACH C (BB localization)**: Works for affine KM only, not general.
   Priority: LOW (not generalizable).

4. **APPROACH B (Saito on Ran)**: Blocked by lack of MHM theory on
   ind-schemes. Priority: VERY LOW.

## 8. Summary

### The actual open problem

The D-module purity item (xii) has a CLEAR directional structure that was
partially misrecorded in the manuscript:

- **PROVED: (xii) => (i)-(x)**: D-module purity + alignment implies
  Koszulness. The argument via Leray degeneration (rem:d-module-purity-content)
  is standard from Saito's MHM theory.

- **OPEN: (i)-(x) => (xii)**: Koszulness implies D-module purity + alignment.
  The meta-theorem header claims this direction but provides no proof.

The open direction is therefore "Koszul => D-module pure," not the converse.
This is a DIFFERENT open problem than what CLAUDE.md and the concordance
describe as "the converse direction."

### Manuscript inconsistency (SERIOUS)

The meta-theorem header (line 1808 of chiral_koszul_pairs.tex) claims
"(x) implies (xii)" -- i.e., Koszul => D-module pure. But the summary
(line 2872 of bar_cobar_adjunction_inversion.tex) says this direction is
OPEN. The proof block contains no proof of this claim. This inconsistency
should be corrected.

### What would close the gap

The open direction (Koszul => D-module pure) requires showing that bar
concentration implies purity of the bar D-module. The key obstacle is
the identification of the algebraic PBW filtration with the Hodge-theoretic
weight filtration on the bar complex.

**Approach A (weight filtration)**: Sound in principle but requires
understanding how the bar differential (involving d-log residue extraction
across multiple configuration spaces) interacts with the MHM weight
structure. The naive strictness argument fails because the bar complex
lives on multiple spaces.

**Approach C (BB localization)**: Works for affine KM via Frenkel-Gaitsgory,
but cannot generalize to Virasoro or W-algebras. Could serve as evidence
for the general claim.

**Approach D (contrapositive)**: If bar cohomology is NOT concentrated, the
PBW spectral sequence has nontrivial d_r differentials. These differentials
connect different weight pieces, producing non-pure extensions. Making this
rigorous requires the PBW = weight identification.

**No approach can FULLY close the gap with existing published technology.**
The deepest ingredient needed is a theory connecting the algebraic structure
of the bar complex (PBW filtration, OPE singularity data) to the
transcendental structure (Saito's MHM weight filtration on FM
compactifications). In the classical BGS setting, this connection comes
from the geometry of Schubert varieties and the decomposition theorem.
The chiral analogue -- a "decomposition theorem for bar D-modules on FM
compactifications" -- does not yet exist.

### Secondary question

Whether alignment (condition (ii) of the conjecture) is automatic or an
independent condition. In the BGS setting, characteristic variety alignment
is automatic (Borho-Brylinski). In the chiral setting, the analogous
statement would be that all singularities of the bar D-module are supported
on FM boundary strata by construction (since the bar differential involves
only OPE collisions, which are FM boundary phenomena). This is plausible
and may follow from the explicit construction of bar components, but has
not been verified.
