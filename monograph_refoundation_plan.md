# Refoundation plan for the monograph

## Core diagnosis

The three preprints force upgrades at three *different* levels of the book:

1. **Local algebraic object**: strict chiral algebra must be replaced by **homotopy chiral algebra** (`Ch_∞` / HCA) whenever Čech descent, derived global sections, or nontrivial covers enter.
2. **Deformation/control object**: naive dg Lie deformation complexes must be replaced by **filtered convolution `sL_∞`-algebras** together with Maurer–Cartan `∞`-groupoids and `∞`-morphisms.
3. **Global collision geometry**: ordinary Fulton–MacPherson compactifications on proper smooth targets must be replaced, for punctures and nodal/semistable degenerations, by **logarithmic Fulton–MacPherson spaces**.

If these are not promoted from peripheral remarks to *structural axioms*, the monograph remains formally incomplete.

---

## The replacement dictionary

### Old → New

- sheaf of chiral algebras on a cover
  → Čech totalization carrying an HCA structure

- strict bar/cobar or deformation complex of morphisms
  → convolution `sL_∞`-algebra relative to a twisting morphism

- MC set / gauge equivalence
  → Maurer–Cartan `∞`-groupoid / Deligne–Hinich–Getzler space

- FM compactification on a smooth proper curve
  → log FM compactification on a pair `(X,D)` and its semistable degeneration package

- clutching by abstract sewing alone
  → clutching implemented geometrically by log FM degeneration and rigid combinatorial types

---

## What must become foundational

### A. Homotopy chiral descent

Add a foundational chapter whose theorem is:

> For a sheaf of chiral algebras on a smooth algebraic variety, the Čech complex of any cover admits a homotopy chiral algebra structure; in particular its cohomology is again a chiral algebra.

This chapter should do the following jobs:

- explain pseudo-tensor categories as the natural habitat of chiral algebra up to homotopy;
- define `Ch_∞` as the chiral analogue of a homotopy Lie algebra in the Beilinson–Drinfeld pseudo-tensor sense;
- prove that every local-to-global construction in the book that passes through Čech resolutions should be stated at the `Ch_∞` level first, and only strictified later if possible;
- refound “cohomology carries a PVA/coisson structure” as the *shadow* of a deeper `Ch_∞` structure.

### B. Convolution homotopy Lie algebra as the universal deformation machine

Add a second foundational chapter whose theorem package is:

- `∞`-morphisms of homotopy algebras admit homotopy inverses when they are `∞`-quasi-isomorphisms;
- the deformation complex of an `∞`-morphism is a convolution homotopy Lie algebra;
- Maurer–Cartan `∞`-groupoids of convolution algebras are invariant under the relevant weak equivalences;
- functoriality exists in either slot separately, but **fails in general as a true bifunctor in both slots simultaneously**.

This chapter should be used to replace all naive statements of the form

- “the deformation complex is `Hom(C,A)` with a bracket”

by the correct statement

- “the deformation complex is `hom_α(C,A)` as a filtered convolution `sL_∞`-algebra, and the moduli problem is its MC `∞`-groupoid.”

The failure of two-sided bifunctoriality must be treated as a **serious design constraint** for the whole monograph.

### C. Logarithmic FM geometry as the modular/global completion

The configuration-space engine must be expanded into a three-layer geometry:

1. ordinary FM on smooth proper targets,
2. logarithmic FM on pairs `(X,D)`,
3. logarithmic FM degenerations over semistable families `W → B`.

This should not remain a side remark. It is the correct home for:

- punctured curves,
- insertions at boundary divisors,
- nodal degeneration/clutching,
- modular factorization,
- stable collision combinatorics.

The essential geometric consequences to install are:

- `FM_n(X|D)` compactifies `Conf_n(X\setminus D)` with SNC/log-smooth boundary;
- its tropicalization is controlled by planted-forest combinatorics;
- semistable degenerations produce a log-smooth degeneration of FM spaces;
- each rigid special-fiber component is a birational modification of a product of smaller log FM spaces.

That last point is the missing geometric input for a truly modular factorization package.

---

## Chapter surgery

## Volume I

### 1. Configuration-space chapter

Split the current FM chapter into:

- classical FM compactification,
- logarithmic FM compactification on pairs,
- degeneration of FM spaces and rigid-component product formulas.

New theorem block:

- log FM compactification theorem;
- log FM degeneration theorem;
- degeneration formula for rigid combinatorial types.

### 2. Higher-genus/modular chapters

Every place where modular sewing or degeneration is currently handled abstractly should be recast in log-FM language.

Required upgrades:

- punctured-curve bar complexes are built on `FM_n(X|D)` rather than heuristically on “configuration spaces with marked points removed”;
- clutching of modular operations is expressed through rigid components and planted forests;
- any “nonlinear modular shadow” or “quartic resonance” discussion should be paired with an actual log-degeneration/clutching geometry.

### 3. Bar/cobar and modular convolution algebra

Reformulate the modular convolution algebra at the `∞`-level:

- replace strict convolution Lie constructions by filtered convolution `sL_∞`-algebras;
- define the modular Maurer–Cartan element in the `∞`-sense;
- state modular deformation problems as MC `∞`-groupoids, not naive formal moduli sets.

### 4. New appendix promoted to core text

The current “nonlinear modular shadows” material should probably cease being an appendix and become the final section of the higher-genus foundations. It is where the new log FM degeneration package actually lands.

## Volume II

### 1. Foundations / locality / equivalence

Insert a new chapter near the beginning:

**Homotopy chiral algebras and derived descent**

with the following role:

- strict chiral algebras are the 0-truncated visible part;
- the actual chain-level object is a `Ch_∞`-algebra;
- Čech descent, restriction to covers, and derived global sections must be performed in `Ch_∞`.

### 2. PVA descent chapter

Upgrade the logic from

`A_∞-chiral on chains  →  PVA on cohomology`

to

`Ch_∞ on Čech/factorization chains  →  strict chiral algebra on cohomology  →  PVA/coisson shadow`.

This removes the current feeling that the chain-level higher operations are an added embellishment. They become structurally necessary.

### 3. Boundary / line / holography chapters

Add a deformation-theoretic interlude:

**Convolution `L_∞` control of bulk–boundary–line data**

with the following consequences:

- boundary conditions, line operators, and bulk-boundary maps are governed by MC elements in suitable convolution algebras;
- the line-operator category and bulk-boundary transfer are only homotopy-functorial in a controlled one-sided sense unless one builds a higher correspondence formalism;
- any naive two-sided functoriality claim should be replaced by a homotopy-coherent or derived-correspondence statement.

### 4. FM calculus / raviolo / modular quantization

The geometry here should be enlarged from ordinary FM/raviolo spaces to log FM whenever punctures, singular boundaries, degeneration, or modularity appear.

This is especially important if the monograph wants to unify:

- HT perturbation theory,
- factorization homology,
- celestial or boundary transfer,
- modular quantization packages.

---

## The theorem packages the finished monograph should contain

### Proven-from-literature packages

1. **Homotopy chiral descent theorem**
   - Čech complex of a sheaf of chiral algebras is a homotopy chiral algebra.

2. **Homotopy-theoretic rectification package**
   - `∞`-quasi-isomorphisms admit homotopy inverses.
   - Bar–cobar provides rectification of homotopy algebras under suitable operadic hypotheses.

3. **Convolution deformation package**
   - deformation of `∞`-morphisms is controlled by convolution homotopy Lie algebras;
   - MC `∞`-groupoids are homotopy invariant;
   - two-sided strict bifunctoriality fails in general.

4. **Log FM compactification and degeneration package**
   - compactification on pairs,
   - log-smooth degeneration,
   - rigid-component product formula.

### New synthesis packages the book should prove or clearly label as conjectural

1. **Logarithmic chiral/factorization descent**
   - `Ch_∞` structures on punctured/nodal/logarithmic curves.

2. **Logarithmic bar/cobar package**
   - bar complexes built on log FM spaces;
   - comparison with ordinary FM in the smooth proper case.

3. **Modular MC formalism**
   - genus-completed deformation problems stated as MC `∞`-groupoids of modular convolution algebras.

4. **Clutching via log degeneration**
   - modular sewing identities proved geometrically using rigid combinatorial types and log FM product decompositions.

5. **Bulk–boundary–line Koszul triangle, homotopy-refounded**
   - every arrow lives at the `∞`-level first;
   - strict algebraic shadows arise only after cohomology/rectification.

---

## Deep consequences for the philosophy of the book

### 1. “Strict chiral algebra” is not the primitive notion.

The primitive notion is the homotopy-coherent chiral object. Strict chiral algebra is the visible shadow after descent/rectification.

### 2. “The deformation complex” is not a dg Lie algebra by fiat.

It is a filtered convolution `sL_∞`-algebra relative to a twisting morphism. The deformation space is not an MC set modulo gauge, but an MC `∞`-groupoid.

### 3. “Configuration space geometry” is not only ordinary FM blowups.

The natural global geometry of punctures, boundaries, and nodal degenerations is logarithmic FM geometry.

### 4. The correct global picture is triadic.

- **Algebraic level**: `Ch_∞` / operads / Koszul duality
- **Deformation level**: convolution `sL_∞` / MC `∞`-groupoids / rectification
- **Geometric level**: log FM compactifications / degeneration formulas / planted-forest clutching

The monograph reaches its “platonic” form only when these three levels are visibly locked together.

---

## What should be demoted, what should be promoted

### Demote

- any claim that sounds strict when only homotopy coherence is actually available;
- any modular/clutching argument that uses abstract sewing without pairing it to log FM geometry;
- any deformation discussion phrased solely in terms of ordinary dg Lie algebras if `∞`-morphisms are present.

### Promote

- HCA/`Ch_∞` descent,
- convolution `L_∞` deformation theory,
- log FM geometry,
- the status ledger distinguishing “proved from literature”, “proved here”, and “conjectural synthesis”.

---

## Minimal viable refoundation

If you want the smallest set of changes that makes the monograph mathematically honest and structurally complete, do these five things:

1. Add a full chapter on homotopy chiral algebras and Čech descent.
2. Add a full chapter on convolution homotopy Lie algebras and MC `∞`-groupoids.
3. Replace all punctured/nodal configuration-space discussions by log FM constructions.
4. Recast modular sewing/clutching via Mok-style degeneration formulas.
5. Rewrite the bulk–boundary–line deformation story so every universal object is first defined at the `∞`-level, and only then strictified.

That is the point where the manuscript stops being a brilliant but partially strictified synthesis and becomes the actual universal theory it is trying to be.
