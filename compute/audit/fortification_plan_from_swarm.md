# Fortification Plan: From Adversarial Swarm to Platonic Ideal

## The Swarm's Verdict (9/10 agents reporting)

### What is STRONG (defend and build on):
1. **Operadic foundations** (Kontsevich: CLEAN): homotopy-Koszulity proof complete and correct, partially modular operad precisely defined, relative Feynman transform original with full signs
2. **The five theorems A-D+H** (Beilinson: CORRECT): 1400pp of proved mathematics, logically sound
3. **∞-categorical framework** (Lurie: SOUND): strict dg-categories correctly used, comparison theorems correctly cited, strict/L∞ comparison handled with care
4. **Swiss-cheese theorem** (Costello: GENUINE PROOF with valid deferred target)
5. **Specific computations**: κ formulas, Q^contact, shadow tower, Verlinde dimensions
6. **Yangian identification** for finite Y(g) at ℏ=1/(k+h∨) (Drinfeld: CORRECT via RTT)

### What must be FIXED (critical/serious findings):

#### CRITICAL (1):
- **Phantom reference** (Costello F8): `prop:mc-homotopy-invariance` cited in thm:e1-factorization-disjoint but does not exist. Must be proved or cited from Seidel/Fukaya/Kontsevich-Soibelman.

#### SERIOUS — Overclaims to correct (6):
1. **"Every object is a projection of Θ^oc"** (Beilinson): FALSE. Correct: "Every algebraic invariant of the genus expansion is a projection of Θ_A."
2. **"Every theorem is a consequence of the MC equation"** (Beilinson): FALSE. Theorem B is independent (PBW + Barr-Beck-Lurie).
3. **"Θ^oc IS the gravitational partition function"** (Witten): SLOGAN. Correct: "Θ^oc computes the perturbative genus-by-genus coefficients F_g around a single saddle."
4. **"Shadow archetypes classify gravitational dynamics"** (Witten): CATEGORY ERROR. Correct: "Shadow archetypes classify boundary A∞ complexity."
5. **N4 at genus ≥ 2** (Beilinson): CONJECTURE presented as PRINCIPLE. Theorem D gives the proved formula.
6. **"MC replaces the sum over topologies"** (Polyakov): OVERSCOPED. Replaces ambiguity within perturbative expansion, not the physical sum over geometries.

#### SERIOUS — Mathematical gaps to close (5):
7. **MCG-equivariance** (Segal F6): rests on a 3-line remark. Needs a theorem.
8. **Comparison with Segal's sewing axioms** (Segal F5): Z_g is DEFINED by clutching, never COMPARED with external notion.
9. **Six categorical underspecifications** (Costello F1-3,9-10,12): tensor products, completions, coherences not specified.
10. **Annulus trace for dg-CATEGORIES** (Segal F4): cites E₁-algebra version, needs Morita reduction step.
11. **Real vs complex gauge group** (Polyakov): passage from SL(2,R) to complex algebraic never acknowledged.

#### SERIOUS — Status inversions to correct (3):
12. **"Bar = coalgebraic shadow"** demotes 1400pp in favor of 35 lines (Beilinson).
13. **Four-stage architecture creates illusion of 75% completion** (Beilinson/Dirac).
14. **Scaffolding ratio**: 21 remarks vs 8 theorems in foundations.tex (Dirac).

#### MODERATE — Naming/terminology (3):
15. **"dg-shifted Yangian"** is a new structure, not Drinfeld Y(g) (Drinfeld F1). Name justified only by associated-graded.
16. **No antipode** in dg-shifted Yangian definition (Drinfeld F2).
17. **"Affine Yangian specialization"** constructs finite Y(g), not affine (Drinfeld F5).

## Fortification Actions

### Tier 1: Fix the critical gap
**Action**: Write prop:mc-homotopy-invariance as a proposition in foundations.tex (or cite Kontsevich-Soibelman, Seidel, or Lyubashenko-Manzyuk). The statement: "For a quasi-isomorphism f: A → A' of A∞ algebras, the induced functor Line(A) → Line(A') is a quasi-equivalence of dg-categories."

### Tier 2: Correct the six overclaims
For each, the fix is a SINGLE EDIT to the specific passage:
1. platonic_ideal_reconception.md line 5: "Every algebraic invariant..." not "Every object..."
2. Same document line 162: "Theorems A, C, D, H are consequences... Theorem B is independent..."
3. Vol I preface §10 opening: "the perturbative genus-by-genus coefficients" not "the gravitational partition function"
4. Same: "boundary A∞ complexity" not "gravitational dynamics"
5. Concordance N4: "At genus ≥ 2, this is conjectural" appended
6. Vol I preface line 1872: qualify "within the perturbative expansion"

### Tier 3: Close the five mathematical gaps
7. Write thm:mcg-equivariance as a theorem with proof (the argument is: bar-intrinsic construction is built from D²=0 on M̄_{g,n}, which is MCG-invariant, so Θ^(g) is MCG-equivariant).
8. State the comparison question as a precise conjecture: "Do the genus-g amplitudes Z_g(C) produced by g-fold clutching agree with those produced by Segal's sewing axioms?"
9. Specify the six categorical items: (a) Lurie tensor product for ⊠, (b) pronilpotent completion for ⊗̂, (c) state compatibilities between axioms, etc.
10. Add the Morita reduction step to the annulus trace proof. Cite BZFN.
11. Add a remark acknowledging the real-vs-complex passage for 3d gravity.

### Tier 4: Restore proved-to-conjectural hierarchy
12. Rewrite rem:corrected-big-picture to say: "The bar complex is the object with 1400pp of proofs. The open category is the natural categorical context in which those proofs live. Both descriptions are correct; neither is subordinate."
13. Add honest scope markers to the four-stage architecture: "Stage 1: theorem. Stage 2: theorem. Stage 3: theorem (local) + programme (global). Stage 4: theorem (annulus) + programme (genus ≥ 2)."
14. Cut the weakest scaffolding per Dirac's count (rem:single-phenomenon, vestigial subsection "Configuration spaces and higher operations", duplicate Steinberg analogy).

### Tier 5: Fix terminology
15. Add a remark: "The 'dg-shifted Yangian' is a strictly more general algebraic structure than Drinfeld's Yangian Y(g). The name is justified by the fact that on the affine Kac-Moody locus, the associated-graded reduction recovers Y(g) with its RTT presentation."
16. Add: "The dg-shifted Yangian is an A∞ bialgebra; the existence of an antipode in the A∞ setting is an open question."
17. Rename constr:dg-shifted-yangian-from-bar to "finite Yangian specialization" or clarify the title.

### Tier 6: First-principles computational verification (from Feynman)
The programme has ZERO first-principles verification at genus ≥ 1. Three computations needed:
18. **Compute κ from d² on the torus**: genus-1 bar differential with Weierstrass propagator, extract coefficient of Arnold defect, verify = c/2
19. **Compute R-matrix from collision residue**: Construct Θ_A at genus 0 arity 2, take Res^coll_{0,2}, verify = Ω/z for sl_2
20. **Compute F_2 from stable graph sum**: enumerate 6 genus-2 graphs, compute amplitudes from shadow data, verify = κ · 7/5760

## What the programme SHOULD claim (honest scope)

"Volume I constructs the bar-cobar machine for chiral algebras on curves and proves five theorems about it. The bar complex classifies twisting morphisms; the modular MC element Θ_A encodes the genus expansion; the shadow tower extracts algebraic invariants; and the five theorems give adjunction, inversion, complementarity, the leading coefficient, and the Hochschild ring.

Volume II identifies a natural categorical context for these theorems: the open factorization dg-category C on a tangential log curve. In this context, the bar complex is the coalgebraic encoding of the twisting data of C, the derived center is the universal bulk, and the Koszul dual governs line operators. The Swiss-cheese operad SC^{ch,top} is the operadic governance, proved to be homotopy-Koszul.

Modularity at genus 1 (the annulus trace) is a theorem. Modularity at genus ≥ 2 (full clutching verification) is a well-posed programme.

The genus expansion of Θ_A computes the perturbative genus-by-genus coefficients F_g of the gravitational partition function around a single saddle. The non-perturbative completion (sum over geometries, BTZ saddles, phase transitions) is outside the current scope."
