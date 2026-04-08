# D-Module Purity Converse: Frontier Investigation

## Date: 2026-04-07
## Status: OPEN (deep structural analysis; key obstruction identified)

## 1. Problem Statement

**The 13th Koszulness characterization** (item (xii) of thm:koszul-equivalences-meta
in chiral_koszul_pairs.tex, line 1813):

> D-module purity: each bar component B_n^{ch}(A) is pure of weight n as a
> mixed Hodge module on FM_n(X), with characteristic variety aligned to FM
> boundary strata.

**Current status** (chiral_koszul_pairs.tex, line 1822):

> "Condition (xii) implies condition (x); the converse is open."

That is: (xii) => (x) is PROVED (D-module purity + alignment => FM boundary
acyclicity => Koszulness). The open direction is (x) => (xii): does Koszulness
imply D-module purity?

**For affine KM**: BOTH directions proved (prop:d-module-purity-km).

**For Virasoro, W-algebras of rank >= 2**: OPEN.

## 2. The Five-Step Proof Strategy (rem:d-module-purity-content)

The manuscript identifies a five-step reduction for the open direction
(Koszulness => D-module purity):

- **Step 1** (PROVED): The PBW filtration F^{PBW} on B_n(A) is a filtration
  by D-submodules on FM_n(X), with associated graded = FG bar complex.

- **Step 2** (PROVED): On the Koszul locus, gr^F B_n is a direct sum of
  rank-one D-modules on FM boundary strata, each pure of the weight determined
  by stratum codimension.

- **Step 3** (PROVED): Purity of the associated graded implies purity of
  the filtered module iff the PBW filtration = Saito weight filtration.
  (Formal consequence of Saito's strictness theorem.)

- **Step 4** (THE GAP): **F^{PBW} = W^{Saito} on B_n(A) for FM_n(X).**
  Proved for affine KM via chiral localization (Frenkel-Gaitsgory) + Hitchin
  connection (provides variation of Hodge structure). OPEN for Virasoro and
  W-algebras: the BPZ equations do not carry a known variation of Hodge
  structure.

- **Step 5** (PROVED): Given Steps 1-4, purity follows by strictness of
  the weight filtration. (Formal.)

**The single gap is Step 4: PBW = Saito weight filtration.**

## 3. Does the Three-Bar-Complex Picture Help?

**The three bar complexes** (thm:three-bar-complexes, bar_construction.tex:1741):

```
Lie^c(s^{-1}A)  -->  Sym^c(s^{-1}A)  -->  T^c(s^{-1}A)
   (Harrison)         (coshuffle)         (tensor)
```

The Eulerian idempotent decomposition (eq:eulerian-bar-decomposition):

    Sym^c(s^{-1}A) = bigoplus_{r >= 1} (Lie^c)^{odot r}

gives a canonical weight grading on the coshuffle bar complex. Weight 1 is
the Harrison (Lie coalgebra) part; weight r is the r-th symmetric power.

**Key observation**: This Eulerian weight decomposition is ALGEBRAIC -- it is
defined by the action of Eulerian idempotents in the group algebra Q[S_n].
The PBW filtration on B_n(A) is the filtration by Eulerian weight:
F^{PBW}_p = bigoplus_{r <= p} (Lie^c)^{odot r}.

The Saito weight filtration is TRANSCENDENTAL -- it comes from mixed Hodge
module theory on FM_n(X).

**The three-bar-complex picture helps in the following way**: The Eulerian
decomposition provides a CANONICAL splitting of the PBW filtration (not just
a filtration but an actual grading). If this grading coincides with the Saito
weight grading on B_n(A), then Step 4 is proved. The advantage of having a
grading (rather than just a filtration) is that the comparison becomes a
question about individual graded pieces, not about a filtration as a whole.

**For affine KM**: The Hitchin connection provides the variation of Hodge
structure, and the monodromy of this connection respects the Lie-theoretic
grading. The Eulerian weight grading and the Saito weight grading coincide
because both are controlled by the same Lie-theoretic data (root space
decomposition of g, KZ/Gaudin connection).

**For Virasoro**: The analogous structure would be a variation of Hodge
structure on FM_n(X) controlled by the Virasoro OPE. The BPZ differential
equations are the Virasoro analogue of the KZ equations, but they do NOT
arise from a flat connection with regular singularities in the classical
sense (they are higher-order differential equations, not first-order).
This is the fundamental obstruction.

## 4. What Specifically Fails for Virasoro/W?

The obstruction has three layers:

### 4a. No geometric localization target

For affine KM V_k(g): chiral localization (Frenkel-Gaitsgory) identifies
B_n(V_k(g)) with a D-module on the affine Grassmannian Gr_G. The
Grassmannian is an ind-scheme with a stratification by Schubert cells, and
D-modules on this stratification carry natural mixed Hodge structures
(geometric Satake, BBD decomposition theorem).

For Virasoro: there is NO analogous geometric space. The Virasoro algebra
is not the affinization of a finite-dimensional Lie algebra. There is no
"Virasoro Grassmannian" or "Virasoro flag variety" to localize onto. The
closest analogue is the moduli of curves M_g itself, but the Virasoro action
on M_g is infinitesimal (vector fields on M_g), not geometric in the
requisite sense.

For W-algebras W_k(g, f): the DS reduction W_k(g, f) = H^0_{DS}(V_k(g), f)
inherits SOME structure from V_k(g), but the BRST cohomology functor does
not obviously preserve the MHM structure needed for the PBW = Saito
identification.

### 4b. BPZ equations are higher-order

The KZ equations for V_k(g) are FIRST-ORDER systems of linear ODEs:

    d_i Phi = Omega_{ij} / (z_i - z_j) * Phi

These are a flat connection on a vector bundle over Conf_n(X). The monodromy
of this connection is a representation of pi_1(Conf_n(X)) = pure braid group.
The regularity of the connection (regular singular along FM boundary) gives
the MHM structure.

The BPZ equations for Virasoro are SECOND-ORDER (and higher) differential
equations:

    (L_{-2} + sum_j (Delta_j/(z-z_j)^2 + (1/(z-z_j))d_j)) Phi = 0

These are NOT a flat connection. They define a D-module on Conf_n(X), but
the D-module is not of "connection type" -- it has irregular singularities
and is not just a local system. The mixed Hodge theory of such D-modules is
less well-understood than for flat connections.

### 4c. No Hitchin connection analogue

For affine KM: the Hitchin connection on the conformal blocks bundle
provides a projectively flat connection with respect to the moduli of curves.
This connection is the geometric ingredient that forces the PBW filtration
to coincide with the Saito weight filtration: the Hitchin connection
PRESERVES the PBW filtration (it commutes with the KZ connection), and
its flatness forces the weight filtration to agree.

For Virasoro: conformal blocks exist (they are the partition functions), but
there is no known projectively flat connection on them that preserves the
PBW filtration. The Virasoro uniformization gives a DIFFERENT connection
(the connection on the Teichmuller space), but this connection does not
have the requisite regularity properties.

## 5. Is There a Counterexample or Hard Obstruction?

**No counterexample is known.** The existing compute engines
(pbw_saito_comparison.py, dmod_filtration_ss_engine.py,
dmod_counterexample_search_engine.py) have tested all standard families
with zero counterexamples found. Specifically:

- For every tested algebra A, null vectors simultaneously create
  off-diagonal bar cohomology AND mixed Hodge extensions
  (rem:d-module-purity-content, line 2198).

- The PBW spectral sequence dimensions match the predicted Saito weight
  filtration dimensions at every tested bidegree.

**Assessment**: The absence of counterexamples is strong evidence that
the converse holds. The obstruction is not the existence of a
counterexample but the lack of a proof technique that works outside the
localization regime.

## 6. Promising Approaches for the Converse

### Approach 1: Direct FM analysis via the alignment condition

The argument for (xii) => (x) (already proved) uses:

    purity + alignment => Leray degeneration => boundary acyclicity

For the converse, one could try:

    Koszulness => bar concentration => [show purity + alignment]

Bar concentration gives the associated graded structure (Step 2). If one
can show that the bar D-module with concentrated cohomology automatically
has aligned characteristic variety (a "Borho-Brylinski theorem for FM
compactifications"), then purity would follow from Step 2 + Step 3 without
needing Step 4 in full generality.

**Key question**: Is characteristic variety alignment automatic for bar
D-modules? This amounts to: are ALL singularities of the bar differential
supported on FM boundary strata? The answer is YES by construction (the
bar differential involves d-log residue extraction along collisions, which
are precisely the FM boundary strata). So alignment is automatic.

If alignment is automatic, then the converse reduces to: bar concentration
implies purity. This is a weaker statement than Step 4 (PBW = Saito), and
may be provable by an inductive argument on n.

### Approach 2: Contrapositive via spectral sequence non-degeneration

If A is NOT Koszul, the PBW spectral sequence has nontrivial d_r
differentials for some r >= 2. These differentials connect different PBW
weight pieces. If PBW = Saito (even partially), these connections
produce non-pure MHM extensions, proving non-purity.

The advantage: one does not need PBW = Saito in full generality; one only
needs that the PBW filtration is COMPATIBLE with the MHM weight filtration
(i.e., each F^{PBW}_p is contained in W_{something}). This is a weaker
statement and may be provable from the D-module structure alone.

### Approach 3: Categorical abstraction (potential new idea)

The bar complex on FM_n(X) has two structures: it is a D-module (geometric)
and it carries the PBW filtration (algebraic). Rather than identifying PBW
with Saito, one could try to prove purity directly from the factorization
structure.

The bar complex B_n(A) has a factorization coalgebra structure: the
coproduct B_n -> B_p tensor B_q (for p + q = n) is compatible with the
partial diagonal maps FM_n -> FM_p x FM_q. If each factorization factor is
pure, the tensor product is pure (purity is preserved by external tensor
product of MHM). So purity of B_n could be proved by induction on n, using
the factorization coproduct.

The base case B_1(A) = s^{-1}A is a D-module on X, which is pure of
weight 1 (a shifted local system). The inductive step would use the
factorization coproduct to show B_n is a successive extension of pure
objects, hence pure.

**Gap in this approach**: the factorization coproduct gives B_n as an
extension of tensor products B_p tensor B_q, but the EXTENSION DATA
(encoded in the bar differential restricted to the diagonal stratum)
could produce non-pure extensions. For Koszul algebras, bar concentration
forces these extensions to split (the spectral sequence degenerates), which
should give purity. Making this rigorous requires understanding the
extension group in the MHM category.

## 7. Relationship to the Eulerian Weight Decomposition

The Eulerian weight decomposition

    Sym^c(s^{-1}A) = bigoplus_r (Lie^c)^{odot r}

provides the algebraic counterpart of the MHM weight grading. In the KM
case where PBW = Saito is proved, the Eulerian weight r piece IS the pure
weight-r piece of the MHM.

For Virasoro: the derivative tower {partial^k T}_{k >= 0} generates the
full bar complex. The desuspended degrees alternate: |s^{-1}(partial^k T)|
= k + 1. The Eulerian idempotents decompose the arity-n bar space into
weight components whose dimensions depend on the representation theory
of S_n acting on tensor products of fields with mixed parities.

**Connection to purity**: If purity of B_n is equivalent to purity of each
Eulerian weight component, then the problem reduces to understanding the
MHM structure of each weight-r piece (Lie^c)^{odot r} separately. For
weight 1 (Harrison), this is the Lie coalgebra part, which for Virasoro
involves the derivative tower. For weight >= 2, these are symmetric
decomposables.

The Eulerian weight decomposition may provide the "algebraic coordinates"
on which to test the Saito weight filtration, even when a geometric
localization target is unavailable.

## 8. Summary

### What is proved:
- (xii) => (x): D-module purity + alignment => Koszulness (via Leray
  degeneration). Standard from Saito's MHM theory.
- For affine KM: full equivalence (x) <=> (xii), via Frenkel-Gaitsgory
  chiral localization + Hitchin connection.

### What is open:
- (x) => (xii): Koszulness => D-module purity, for Virasoro and W-algebras
  of rank >= 2.
- Reduces to Step 4: PBW filtration = Saito weight filtration on B_n(A).

### Why it is hard:
- No geometric localization target for Virasoro (no "Virasoro Grassmannian").
- BPZ equations are higher-order, not a flat connection.
- No Hitchin connection analogue for the Virasoro conformal blocks.

### Most promising paths:
1. Prove alignment is automatic (likely, since bar singularities are on FM
   boundary by construction), then prove bar concentration => purity via
   factorization induction on n.
2. Prove a partial compatibility statement (PBW filtration refines Saito
   weight filtration), then use the contrapositive.
3. Use the Eulerian weight decomposition as algebraic coordinates for
   testing purity component-by-component.

### No counterexample:
Zero counterexamples across all tested families. Strong computational
evidence that the converse holds universally.

### Manuscript consistency:
The meta-theorem header (line 1822) correctly states "(xii) implies (x);
the converse is open." The five-step remark (rem:d-module-purity-content)
correctly identifies Step 4 as the single gap. The prop:d-module-purity-km
correctly marks the KM case as proved. No inconsistencies found in the
current source.
