# Modular Factorization Envelope U^mod_X -- Construction Assessment

## Date: 2026-04-05

## Executive Summary

The modular factorization envelope $U^{\mathrm{mod}}_X(L)$ and its adjunction with $\mathrm{Prim}^{\mathrm{mod}}$ exist in the manuscript in **two contradictory incarnations**:

1. **Theorem** (thm:platonic-adjunction, higher_genus_modular_koszul.tex:22563-22694): Tagged `\ClaimStatusProvedHere`, with an explicit proof constructing unit, counit, and bijection. Target category: $\mathsf{Fact}_{\mathrm{cyc}}(X)$ (cyclic factorization algebras).

2. **Conjecture** (conj:universal-modular-factorization-envelope, frontier_modular_holography_platonic.tex:3233-3265): Tagged `\ClaimStatusConjectured`, with an `\begin{evidence}` block. Target category: $\mathrm{ModKoszul}(X)$ (modular Koszul factorization objects).

These are **different claims about different target categories** with **contradictory status tags**. This is an AP40 + AP12 violation. The rest of this document assesses which status is honest.

---

## Finding 1: The Two Target Categories Are Different (CRITICAL)

The conjecture in the frontier chapter targets $\mathrm{ModKoszul}(X)$ -- the category of **modular Koszul** factorization objects, which carry the full six-fold datum $\Pi_X(L)$ including shadow data at all genera. The theorem in the engine chapter targets $\mathsf{Fact}_{\mathrm{cyc}}(X)$ -- the category of cyclic factorization algebras, equipped only with a genus-0 factorization product and a residue pairing.

The theorem proves the adjunction for the WEAKER target category. The conjecture asks for it in the STRONGER target category. The distinction matters: $\mathsf{Fact}_{\mathrm{cyc}}(X)$ does not require its objects to carry genus data, shadow towers, or modular clutching identities. $\mathrm{ModKoszul}(X)$ does.

**Assessment**: The theorem proves a meaningful result -- a "modular envelope" that is a cyclic factorization algebra carrying genus data via the completed tensor product with $\mathbb{G}_{\mathrm{mod}}$. But it does NOT prove that the output lands in the narrower $\mathrm{ModKoszul}(X)$ category carrying all the modular Koszul structure. The two claims are related but distinct, and their simultaneous presence with contradictory status tags is a scope-honesty violation.

---

## Finding 2: Assessment of the Proof of thm:platonic-adjunction

### Part (i): Primitive currents -- SOUND WITH CAVEATS

The proof correctly observes that:
- $\bar{B}(\mathcal{F})$ is cocommutative (from Theorem thm:bar-modular-operad)
- $\ker(\bar{\Delta})$ inherits a Lie conformal bracket from the factorization product
- The Jacobi identity follows from $d_{\bar{B}}^2 = 0$

**Caveat**: The proof invokes "the Milnor-Moore theorem for factorization coalgebras." This is not a standard reference. The classical Milnor-Moore theorem identifies primitives of a cocommutative coalgebra with a Lie algebra, but the factorization algebra setting (D-modules on Ran(X), not vector spaces) requires a version of this theorem in the chiral/factorization context. The manuscript does not cite a specific reference for this generalization. This is a **potential gap** -- the theorem may be folklore or may follow formally from the classical case by working locally, but the lack of a precise citation is a concern at Annals grade.

**Caveat 2**: The claim that cyclic admissibility conditions are inherited (conformal grading from Virasoro action, bounded pole order from locality, etc.) is plausible but each condition should be verified. In particular, bounded pole order for $\mathrm{Prim}^{\mathrm{mod}}(\mathcal{F})$: the primitive elements of a factorization algebra on a curve need not have uniformly bounded pole order in general. The proof asserts this follows "from locality" but does not give the argument.

### Part (ii): Modular envelope construction -- DEFINITION, NOT CONSTRUCTION

The envelope is defined as:
$$U_X^{\mathrm{mod}}(L) := \mathrm{Fact}_X(L) \,\widehat{\otimes}_{\mathrm{cyc}}\, \mathbb{G}_{\mathrm{mod}}$$

This is a completed tensor product of the genus-0 Nishinaka envelope with the stable-graph coefficient algebra. The proof says the modular extension "appends" $\mathbb{G}_{\mathrm{mod}}$ via completed tensor product.

**Key question**: What is the factorization algebra structure on this completed tensor product? The factorization product on $\mathrm{Fact}_X(L)$ acts on the first factor; $\mathbb{G}_{\mathrm{mod}}$ carries edge-contraction as its differential. But a factorization algebra structure on the tensor product requires compatibility between these two structures -- specifically, that the genus-g contributions from $\mathbb{G}_{\mathrm{mod}}$ interact correctly with the factorization product from $\mathrm{Fact}_X(L)$.

The proof appeals to Theorem thm:bar-modular-operad for this compatibility. This theorem states that the bar complex $\{B^{(g,n)}(\mathcal{A})\}$ is an algebra over $\mathrm{FCom}$ (Feynman transform of commutative modular operad). If this is sound, then the factorization algebra structure on the modular envelope is indeed inherited from the modular operad structure.

**Assessment**: The construction WORKS as a definition. Whether it produces an object with the right universal property is the content of part (iii).

### Part (iii): Adjunction -- THE CRITICAL GAP

The proof constructs:

**Unit**: $\eta_L: L \to \mathrm{Prim}^{\mathrm{mod}}(U_X^{\mathrm{mod}}(L))$ sends generators to their images. This is straightforward.

**Counit**: Given $\varphi: L \to \mathrm{Prim}^{\mathrm{mod}}(\mathcal{F})$, the proof:
1. Uses the Nishinaka universal property to extend $\varphi$ to $\tilde{\varphi}_0: \mathrm{Fact}_X(L) \to \mathcal{F}$ at genus 0.
2. Claims the extension to all genera is "forced by the modular bar construction" because the bar construction is functorial.

**This is the gap.** The argument says: functoriality of bar gives a map $\bar{B}(\tilde{\varphi}_0): \bar{B}(\mathrm{Fact}_X(L)) \to \bar{B}(\mathcal{F})$, and then "the completed tensor product with $\mathbb{G}_{\mathrm{mod}}$ propagates uniquely."

But propagation to all genera requires MORE than functoriality of bar at genus 0. It requires that:
(a) The genus-g datum of $\mathcal{F}$ is determined by its bar coalgebra structure at all genera.
(b) The map $\tilde{\varphi}_0$ at genus 0 uniquely determines a factorization algebra map at all genera.

Condition (a) is essentially bar-cobar inversion (Theorem B) -- which requires Koszulness. For a general cyclic factorization algebra $\mathcal{F}$ (the target of the adjunction), Koszulness is NOT assumed. The adjunction claims to work for ALL cyclic factorization algebras, not just Koszul ones.

Condition (b) is the claim that a genus-0 factorization algebra map uniquely extends to a modular (all-genera) map. This would follow if $U_X^{\mathrm{mod}}(L)$ were the FREE modular factorization algebra on the genus-0 data modulo the Lie conformal relations. But the proof does not establish this freeness at higher genera -- it only appeals to the Nishinaka freeness at genus 0.

**The sentence "the completed tensor product with $\mathbb{G}_{\mathrm{mod}}$ propagates uniquely" is doing all the work and is not justified.** For the propagation to be unique, one needs that the modular bar construction creates no new relations at higher genera beyond those forced by the genus-0 structure. This is plausible for $U_X^{\mathrm{mod}}(L)$ itself (where the modular data IS defined to be $\mathrm{Fact}_X(L) \widehat{\otimes} \mathbb{G}_{\mathrm{mod}}$), but it requires an argument about the TARGET $\mathcal{F}$: that the map to $\mathcal{F}$ at genus $g \geq 1$ is determined by the genus-0 map plus the stable-graph structure.

**Verdict on the proof**: The construction of $U_X^{\mathrm{mod}}(L)$ as an object is SOUND. The unit is SOUND. The counit construction has a GAP at the genus extension step. The bijection assertion depends on the counit being well-defined. **The theorem as stated (adjunction for all cyclic factorization algebras) is NOT proved.** A restricted version -- adjunction for the subcategory of Koszul cyclic factorization algebras, or factorization algebras whose genus data is determined by the modular bar structure -- may be provable with the existing tools.

---

## Finding 3: The Concordance Is Internally Inconsistent

The concordance (concordance.tex:946-957) states: "The modular factorization adjunction is proved in Theorem thm:platonic-adjunction." The concordance (concordance.tex:9350-9391) simultaneously poses the adjunction as a question: "Is $\Theta^{\mathrm{oc}}_{\mathcal{A}}$ the image under $U^{\mathrm{mod}}_X$ of the canonical MC element on $L$? Does the universality of the open sector yield the adjunction?"

These are contradictory: either it is proved or it is an open question. The question formulation in 9350-9391 is the more honest assessment.

**Assessment**: The concordance line 946-957 should be qualified. The question formulation at 9350-9391 correctly identifies what remains open.

---

## Finding 4: Three Construction Strategies -- Comparative Assessment

The manuscript (prop:envelope-construction-strategies, line 22754) correctly identifies three approaches:

### Strategy (i): Bar-Cobar Resolution

$U_X^{\mathrm{mod}}(L) := \Omega(\bar{B}^{\mathrm{ch}}(L) \otimes \mathbb{G}_{\mathrm{mod}})$

**Assessment**: This is the most rigorous approach. It defines $U^{\mathrm{mod}}_X(L)$ as the cobar of the modular bar complex. Non-circular because $\bar{B}^{\mathrm{ch}}(L)$ comes from $L$ alone. **However**: this strategy requires the Koszul hypothesis -- bar-cobar inversion is a quasi-isomorphism only on the Koszul locus. For Koszul algebras, this strategy works and gives a well-defined construction. The adjunction in this setting would be a modular analogue of the bar-cobar Quillen adjunction.

**Scope**: Koszul algebras only. This covers the entire standard landscape (all standard families are Koszul), which is the case of interest.

**What it proves**: For Koszul $L$, $\Omega(\bar{B}(L) \otimes \mathbb{G}_{\mathrm{mod}}) \xrightarrow{\sim} \mathrm{Fact}_X(L) \widehat{\otimes} \mathbb{G}_{\mathrm{mod}}$ by bar-cobar inversion at each genus. The bar-cobar adjunction gives the Hom bijection on the Koszul locus. This is the **actually proved** version of the adjunction.

### Strategy (ii): Genus Tower Induction

Construct $U_X^{(g)}(L)$ inductively. At genus 0: Nishinaka. At genus $g$: adjoin $\Theta_L^{(g)}$ via MC5 sewing.

**Assessment**: Fully constructive for finite shadow depth (classes G, L, C). For class M (infinite tower), requires convergence of the shadow obstruction tower, which is proved (thm:recursive-existence). The MC equation guarantees coherence. This approach builds $U^{\mathrm{mod}}_X(L)$ as a colimit and is the most explicit. However, it does not directly establish the adjunction universal property -- it constructs the object but does not prove that it satisfies the Hom bijection.

**Scope**: All positive-energy chiral algebras with proved tower convergence.

### Strategy (iii): Left Kan Extension

The proof correctly identifies this as circular at genus $g \geq 1$: the colimit requires the very modular data that the envelope is meant to produce.

**Assessment**: Not viable as stated. The circularity is genuine.

---

## Finding 5: What CAN Be Constructed With Current Technology

### The Object $U_X^{\mathrm{mod}}(L)$ -- CONSTRUCTIBLE

The modular factorization envelope $U_X^{\mathrm{mod}}(L) = \mathrm{Fact}_X(L) \widehat{\otimes}_{\mathrm{cyc}} \mathbb{G}_{\mathrm{mod}}$ is well-defined as an object. Its construction depends on:

1. **Nishinaka envelope** at genus 0 (published, [Nish26]): gives $\mathrm{Fact}_X(L)$.
2. **Stable-graph coefficient algebra** $\mathbb{G}_{\mathrm{mod}}$ (combinatorial, Definition def:stable-graph-coefficient-algebra): purely algebraic.
3. **Completed tensor product**: standard.
4. **Modular operad structure** (Theorem thm:bar-modular-operad): proved.
5. **Bar-intrinsic MC element** $\Theta_L = D_L - d_0$ (Theorem thm:mc2-bar-intrinsic): proved.
6. **All-arity convergence** (Theorem thm:recursive-existence): proved.

All six ingredients are proved. The object exists.

### The Primitive-Current Functor $\mathrm{Prim}^{\mathrm{mod}}$ -- CONSTRUCTIBLE ON THE KOSZUL LOCUS

For a **Koszul** cyclic factorization algebra $\mathcal{F}$, the bar coalgebra $\bar{B}(\mathcal{F})$ has the right formal properties (cocommutative, cofree on cogenerators), and the primitive elements $\ker(\bar{\Delta})$ inherit the Lie conformal algebra structure. The Milnor-Moore argument goes through when $\bar{B}(\mathcal{F})$ has the expected cofreeness (which follows from Koszulness).

For a general (non-Koszul) cyclic factorization algebra, the primitive-current extraction may not produce a cyclically admissible Lie conformal algebra: the bounded pole-order condition and the conformal grading need not be inherited.

### The Adjunction -- PROVED ON THE KOSZUL LOCUS, OPEN IN GENERAL

On the Koszul locus, Strategy (i) (bar-cobar resolution) provides:
- $U_X^{\mathrm{mod}}(L)$ via cobar construction
- $\mathrm{Prim}^{\mathrm{mod}}$ via primitives of bar coalgebra
- The adjunction via the bar-cobar twisting morphism correspondence

The bar-cobar adjunction (Theorem A, at genus 0) extends to all genera via the modular operad structure. The Hom bijection follows from:
$$\mathrm{Hom}_{\mathsf{Fact}}(U^{\mathrm{mod}}(L), \mathcal{F}) \cong \mathrm{Tw}(\bar{B}(L) \otimes \mathbb{G}_{\mathrm{mod}}, \mathcal{F}) \cong \mathrm{Hom}_{\mathrm{LCA}}(L, \mathrm{Prim}(\mathcal{F}))$$
where $\mathrm{Tw}$ denotes twisting morphisms.

**Status**: On the Koszul locus with $\mathsf{Fact}_{\mathrm{cyc}}(X)$ as target, the adjunction is proved using Strategy (i) + the existing bar-cobar machinery. For the full adjunction (non-Koszul targets, or the stronger ModKoszul target category), the proof has gaps.

### The Shadow Invariants -- COMPUTABLE

Given $U_X^{\mathrm{mod}}(L)$, all shadow invariants ($\kappa$, $\Delta$, $\mathfrak{R}_4^{\mathrm{mod}}$, branch operator, full $\Theta_L$) are extractable by the shadow extraction corollary (cor:shadow-extraction) applied to the bar-intrinsic MC element. The genus tower formula $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ holds on the uniform-weight lane.

---

## Finding 6: The Frontier Conjecture vs the Engine Theorem -- What Each Actually Claims

| Feature | Frontier Conjecture | Engine Theorem |
|---------|-------------------|----------------|
| Label | conj:universal-modular-factorization-envelope | thm:platonic-adjunction |
| Status | Conjectured | ProvedHere |
| Target category | ModKoszul(X) | Fact_cyc(X) |
| Input | cyclically admissible L | cyclically admissible L |
| Output carries | full Theta, kappa, Delta, T^br, R^mod_4 | genus-0 + modular graph extension |
| Universal property | left adjoint to Prim_mod | left adjoint to Prim^mod |
| Proof | evidence block only | explicit unit/counit |

The two claims overlap but are not identical. The engine theorem is weaker (smaller target category) and claims a proof. The frontier conjecture is stronger (richer target category with ModKoszul structure) and is honest about being conjectural.

---

## Recommendations

### 1. DOWNGRADE thm:platonic-adjunction (SERIOUS)

The proof has a gap in the counit construction at genus $g \geq 1$. Options:

(a) **Restrict the theorem to the Koszul locus**: Replace $\mathsf{Fact}_{\mathrm{cyc}}(X)$ with the subcategory of Koszul cyclic factorization algebras. The proof via Strategy (i) is then complete.

(b) **Add a hypothesis**: Require the target $\mathcal{F}$ to satisfy the bar-determines-algebra condition (that the bar coalgebra structure at all genera determines the factorization algebra uniquely). This is satisfied by all Koszul algebras and is the actual hypothesis used in the proof.

(c) **Flag the counit step as needing additional input**: Add a `% RECTIFICATION-FLAG: counit extension from genus 0 to all genera requires bar-determines-algebra for the target` comment.

### 2. RECONCILE the two incarnations

The frontier conjecture should reference the engine theorem as proving the genus-0 base case and the Koszul restriction. The engine theorem should note that the full ModKoszul target version remains conjectural. Currently, the concordance (line 946-957) and all cross-references cite thm:platonic-adjunction as if the full adjunction is proved, while the concordance (line 9350-9391) simultaneously treats it as an open question.

### 3. The Seven-Stage Execution Programme Is Correct

The seven-stage programme in rem:envelope-execution-programme (concordance.tex:959-996) is well-designed. Steps (1)-(2) use published input. Steps (3)-(5) are the proved core. Steps (6)-(7) are the constructive layer. The assessment that "steps (1)-(5) are supplied by the current literature and the proved core" is accurate.

---

## Summary Assessment

| Component | Status | Confidence |
|-----------|--------|------------|
| The object $U_X^{\mathrm{mod}}(L)$ | CONSTRUCTIBLE | HIGH |
| The MC element $\Theta_L$ on it | PROVED | HIGH |
| The shadow invariants | COMPUTABLE | HIGH |
| The adjunction on the Koszul locus | PROVED (via Strategy i) | HIGH |
| The adjunction for general $\mathsf{Fact}_{\mathrm{cyc}}(X)$ | GAP in counit | MEDIUM |
| The adjunction for $\mathrm{ModKoszul}(X)$ | OPEN | LOW |
| The frontier conjecture (conj:universal-modular-factorization-envelope) | OPEN | matches honest assessment |

**Bottom line**: $U_X^{\mathrm{mod}}(L)$ can be constructed with current technology. It carries $\Theta_L$ and all shadow invariants. The adjunction is proved on the Koszul locus (which covers the entire standard landscape). The full adjunction for arbitrary cyclic factorization algebras has a gap in the counit at genus $\geq 1$. The strongest form (landing in ModKoszul) is genuinely open.

The manuscript should be corrected to reflect this: thm:platonic-adjunction is honest as a theorem if restricted to the Koszul locus or if the gap in the counit is acknowledged. The simultaneous existence of a theorem and a conjecture for the same object with contradictory status is a clear AP40/AP12 violation that must be resolved.

---

## Three Approaches -- Detailed Verdict

### Approach A: Genus-by-Genus Induction (Strategy ii)

- **Does the construction produce a well-defined object?** YES. At genus 0, Nishinaka gives $\mathrm{Fact}_X(L)$. At genus $g$, the MC element $\Theta_L^{(g)}$ is determined by the MC equation projected to genus $g$, which involves only lower-genus data and the genus-$g$ curvature $\kappa \cdot \omega_g$. The HS-sewing criterion (thm:general-hs-sewing) guarantees convergence.
- **Does it have the right universal property?** NOT DIRECTLY. The inductive construction builds the object but does not establish the Hom bijection. Additional input (freeness at each genus, or bar-cobar) is needed for the adjunction.
- **Is it computable?** YES, fully constructive for classes G, L, C (finite shadow depth). For class M, requires truncation.

### Approach B: Bar-Cobar on Modular Operads (Strategy i)

- **Does the construction produce a well-defined object?** YES, on the Koszul locus. $\Omega(\bar{B}^{\mathrm{ch}}(L) \otimes \mathbb{G}_{\mathrm{mod}})$ is well-defined by the modular operad structure (thm:bar-modular-operad).
- **Does it have the right universal property?** YES, on the Koszul locus. The bar-cobar adjunction at the modular operad level gives the Hom bijection via twisting morphisms.
- **Is it computable?** YES, but less explicitly than Approach A. The cobar construction requires inverting the bar quasi-isomorphism, which is homotopy-theoretic rather than algebraic.

### Approach C: Derived Algebraic Geometry

- **Does the construction produce a well-defined object?** IN PRINCIPLE. The MC moduli $\mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_A)$ is a derived stack by general Lurie machinery (DAG-X, Formal Moduli Problems). Global sections of the universal family would give $U_X^{\mathrm{mod}}$.
- **Does it have the right universal property?** WOULD FOLLOW from the DAG formalism, but requires setting up the correct derived functor framework for modular factorization algebras, which has not been done.
- **Is it computable?** POORLY. The DAG approach gives existence and universal property but is non-constructive. Extracting $F_g$, $\kappa$, or shadow invariants from a derived stack requires additional technology.
- **Assessment**: This approach is the most powerful in principle but the most distant from the manuscript's actual machinery. It would require importing substantial DAG infrastructure that is not currently present.
