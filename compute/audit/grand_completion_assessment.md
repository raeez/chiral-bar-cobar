# Grand Completion Conjecture (conj:grand-completion) -- Status Assessment

**Date**: 2026-04-07
**Source**: concordance.tex lines 4749--4758, 9539--9578
**Ranked**: #5 load-bearing in open conjectures survey (2026-04-08)

## Statement

The modular cumulant transform A -> M(A) extends finite-stage chiral Koszul
duality to an equivalence between the completion closure of admissible chiral
A-infinity-algebras on curves and the homotopy theory of complete pronilpotent
modular cumulant coalgebras, with:
- genus-0 truncation = completed bar/cobar,
- ordered-boundary truncation = dg-shifted Yangian jet tower,
- universal deformation theory = graph MC class Theta_A.

The five-component datum M(A) = (Cum_c(A), D_A, tau_A, r_A(z), Theta_A)
packages cumulant coalgebra, coderivation, twisting morphism, r-matrix,
and modular logarithm.

## Two Sub-Conjectures

### 1. Cumulant Recognition (conj:cumulant-recognition, concordance line 4680)

**Statement**: For admissible A satisfying reduced-weight finiteness and
finite-window stabilization, gr_rho(B-hat(A)) = Cum_c(A) as completed
curved dg coalgebras. That is, the resonance-graded associated graded
of the completed bar is the cofree coalgebra on the dual of primitive
cumulants Q(A) = bar(A) / d(bar(A)).

**What proving it requires**:
- A structural comparison between the resonance filtration on B-hat(A)
  (defined by resonance rank rho(A), cf. def:resonance-rank) and the
  cofree filtration on T^c(sQ(A)^v).
- The key difficulty: the completed bar B-hat(A) has a CURVED differential
  D_A. The cofree coalgebra Cum_c(A) has a curved codifferential induced
  from D_A. The recognition asks whether gr_rho intertwines these. For
  non-quadratic algebras (Virasoro, W_N), the resonance filtration has
  nontrivial extensions that may not split at gr_rho.
- Known data: the compute module cumulant_algebra.py computes primitive
  cumulant dimensions q_n via Moebius inversion of bar cohomology
  dimensions. The cumulant data is computed for Heisenberg (polynomial
  growth), affine sl_2 (q_2 = -1 defect), Virasoro (exponential growth),
  W_3 (exponential growth), betagamma (exponential growth). The Euler
  transform roundtrip is verified. But these are DIMENSION counts only --
  the chain-level quasi-isomorphism is untouched.
- The completion entropy h_K(A) = log(rho_A^{-1}) is computed for W_N
  (monotone ladder 0.567 < 0.772 < 0.835 < ... < 0.872). This is
  kinematic data; it constrains M(A) but does not prove the recognition.

### 2. Jet Principle (conj:jet-principle, concordance line 4728)

**Statement**: Reduced-weight-q bar windows K_q(A) determine the
dg-shifted Yangian MC kernel r_A(z) = sum r_m z^{-m-1} through jet
order z^{-q}: the truncation r_A(z) mod z^{-q-1} depends only on
B(A)|_{K_q}.

**What proving it requires**:
- An explicit analysis of how the collision-residue functor
  Res^coll_{0,2} interacts with the weight filtration on B(A).
- For quadratic algebras (class G/L): r_A(z) = Omega/z (single jet),
  and the principle is trivially true since the genus-0 bar complex
  in weight window K_1 already determines the full r-matrix.
- For class C (betagamma): r_A(z) has jets through z^{-3}, and the
  weight-3 window should suffice. Not verified at chain level.
- For class M (Virasoro, W_N): r_A(z) has infinitely many jets, and
  the principle asserts that each finite truncation is determined by a
  finite bar window. This is plausible from the weight-filtration
  spectral sequence but unproved.
- The principle is ultimately about how the collision-residue extraction
  (which is a genus-0 operation on FM_2(X)) interacts with the
  completion tower (which is an arity-filtration operation). These
  two filtrations (weight and arity) are transverse, and the jet
  principle asserts they cooperate.

## What the Grand Completion Itself Requires (Beyond Sub-Conjectures)

Even with both sub-conjectures proved, the grand completion asks for an
EQUIVALENCE OF HOMOTOPY THEORIES. This requires:
1. A model category or infinity-category structure on completed admissible
   chiral A-infinity-algebras.
2. A model category or infinity-category structure on complete pronilpotent
   modular cumulant coalgebras.
3. A Quillen equivalence or infinity-equivalence between them, extending
   the proved genus-0 bar-cobar Quillen equivalence
   (thm:quillen-equivalence-chiral).

The genus-0 truncation is resolved by MC4 (completed bar-cobar). The full
modular extension requires the modular QME in the completed tensor product
(component (5) of M(A)), which is "the principal open structural problem"
per concordance line 4723. The bar-intrinsic MC element Theta_A := D_A - d_0
is proved at all finite orders; the issue is convergence in the completed
modular convolution algebra.

## Theta^oc Reformulation (concordance lines 9549--9578)

The five components of M(A) are projections of the open/closed MC element
Theta^oc_A. The conjecture can be restated as: the functor A -> Theta^oc_A
is an equivalence on the completion closure. This reformulation clarifies
that the grand completion is about whether Theta^oc_A is a COMPLETE INVARIANT
(faithfulness) and whether every admissible cumulant coalgebra arises
(essential surjectivity).

## Does This Session's Work Bring Them Closer?

**No material progress on either sub-conjecture or the grand completion itself.**

The session's main mathematical result is the W_4 full-OPE cross-channel
computation (commit 6e99fc6): delta_F_2(W_4) involves irrational functions
of c (square roots of polynomial discriminants), a qualitative phase
transition from the W_3 case (rational in c). This is relevant to the
MULTI-WEIGHT GENUS EXPANSION (thm:multi-weight-genus-expansion), not to the
grand completion. The cross-channel correction is a projection of Theta_A
at genus 2, arity 0 -- it tests the modular logarithm (component 5) but
does not address the cumulant recognition (component 1) or jet principle
(component 4).

The session also includes fixes to the Bethe MC engine (big-endian bit
convention, BAE shift convention i vs 1). These are correctness fixes to
an existing engine, relevant to MC3/Yangian computations, not to the
grand completion.

**Nearest leverage points for progress**:
- Cumulant recognition: extend cumulant_algebra.py from dimension counts to
  chain-level quasi-isomorphism verification, at least for Heisenberg
  (where the bar complex is explicitly known).
- Jet principle: verify for betagamma (class C) by computing r_A(z) from
  the weight-3 bar window and comparing to the full r-matrix.
- Neither is attempted in this session.

## Overall Assessment

The grand completion is rated VERY HARD in the frontier status document.
The interplay between resonance filtration, completion, and cumulant
functors is the core difficulty. The proved infrastructure (MC4 completion
tower, bar-intrinsic Theta_A, resonance rank finiteness) provides the
necessary foundation, but the actual equivalence-of-homotopy-theories
claim is far from the current proved frontier. No session work advances it.
