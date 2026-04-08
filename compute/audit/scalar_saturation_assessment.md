# Assessment: conj:scalar-saturation-universality

## Location

higher_genus_modular_koszul.tex line 8771

## What is conjectured

The conjecture has two nested layers:

### Layer 1 (weaker): one-channel line concentration

For any modular Koszul chiral algebra A with maximal reductive current
algebra g = g_1 + ... + g_r (each g_i simple), the minimal-model MC
element factors as:

    Theta^min_A = sum_{i=1}^r eta_i tensor Gamma_i(A)

for tautological coefficients Gamma_i(A) in the completed modular
graph complex. This is the "effective Gamma-quadruple reduction"
(cor:effective-quadruple).

### Layer 2 (stronger): scalar saturation proper

The stronger assertion is that each tautological coefficient is
proportional to the universal Hodge class:

    Theta^min_A = sum_{i=1}^r kappa_i(A) * eta_i tensor Lambda

where Lambda = sum_{g >= 1} lambda_g, and the MC equation decouples
into r independent scalar equations.

### Equivalent formulation (prop:saturation-equivalence)

Both layers are equivalent to a single cohomological condition:

    dim H^2_cyc(A, A) = r = number of simple factors

at every level. This is the testable criterion.

## What is proved

| Regime | Layer 1 | Layer 2 | Method |
|--------|---------|---------|--------|
| KM, simple g, generic level | YES | YES | thm:cyclic-rigidity-generic |
| All algebraic families, rational OPE, non-critical | YES | OPEN | thm:algebraic-family-rigidity |
| Standard Lie-theoretic landscape | YES | YES (uniform-weight) | cor:effective-quadruple |
| Uniform-weight algebras, all genera | YES | YES | thm:genus-universality |
| Multi-weight algebras, genus 1 | YES | YES | thm:multi-weight-genus-expansion(iii) |
| Multi-weight algebras, genus >= 2 | YES | FAILS | thm:multi-weight-genus-expansion(vi) |

## The precise residual gap

thm:algebraic-family-rigidity proves that for algebraic families with
rational OPE coefficients, the primitive cyclic tangent space vanishes:
H^2_{cyc,prim}(A) = 0. This gives Layer 1 (one-channel concentration:
Theta^min = eta tensor Gamma_A). But it does NOT identify
Gamma_A = kappa(A) * Lambda. That additional "tautological purity"
step is open for multi-weight families.

What remains open outside the proved regimes:

1. **Non-algebraic-family VOAs**: vertex algebras not known to belong to
   algebraic families with rational OPE coefficients. The conjecture
   asserts dim H^2_cyc = 1 persists for these.

2. **Tautological purity for multi-weight families**: even when
   dim H^2_cyc = 1 is known, the identification Gamma_A = kappa * Lambda
   requires an additional argument. This is the "tautological purity
   step" (rem:scalar-saturation-scope, line 7775).

## Families that would need checking

From rem:scalar-saturation-scope (line 7727), three candidate classes
for potential non-scalar behavior:

1. **Mixed-factor cosets (non-GKO)**: GKO cosets have rank-1 central
   charge Jacobian, so dim H^2_cyc = 1 automatically. Non-GKO
   embeddings behave identically in all verified cases. But a
   multi-parameter coset with independent level deformations could
   potentially have dim H^2_cyc >= 2.

2. **4D N=2 VOAs (class S and quiver)**: class S VOAs are rigid (fixed
   level). Quiver VOAs with multi-dimensional conformal manifolds depend
   on at most one effective parameter in all computed examples. The
   OPE algebra appears insensitive to exactly marginal couplings. But
   this is empirical, not proved in general.

3. **Admissible-level simple quotients (sl_3 and higher rank)**: L_k(g)
   at admissible levels for rank >= 2. The UNIVERSAL algebra V_k(g) is
   Koszul at ALL levels, but the simple quotient L_k(g) has Koszulness
   open for rank >= 2 (bar-Ext vs ordinary-Ext gap). If L_k(g) is
   Koszul, scalar saturation would need separate verification at
   admissible levels beyond the algebraic-family theorem.

The sharpest potential counterexample identified in the manuscript:
"4D N=2 quiver VOAs with multi-dimensional conformal manifolds" -- but
these have produced only single-parameter dependence in all computed cases.

## Interaction with multi-weight cross-channel work

The multi-weight genus expansion (thm:multi-weight-genus-expansion) is
ORTHOGONAL to scalar saturation, not contradictory. The key distinction:

- **Scalar saturation** (conj:scalar-saturation-universality) concerns
  Layer 1: whether the MC element concentrates on the cyclic direction
  (dim H^2_cyc = 1). This is about the MINIMAL MODEL of the cyclic
  deformation complex.

- **Multi-weight cross-channel correction** (thm:multi-weight-genus-expansion)
  concerns Layer 2 on the uniform-weight lane: whether the tautological
  coefficient Gamma_A equals kappa * Lambda. For multi-weight algebras,
  it does NOT: delta F_g^cross != 0 at g >= 2.

Concretely: W_3 satisfies dim H^2_cyc = 1 (scalar saturation Layer 1
holds). The MC element IS one-channel: Theta^min = eta tensor Gamma_{W_3}.
But Gamma_{W_3} != kappa(W_3) * Lambda at genus >= 2. The cross-channel
correction delta F_2(W_3) = (c + 204)/(16c) measures the FAILURE of
Layer 2 for multi-weight algebras.

So the multi-weight cross-channel work:
- Does NOT contradict scalar saturation Layer 1
- RESOLVES the Layer 2 question NEGATIVELY for multi-weight families
- SHARPENS the conjecture: the residual content is purely Layer 1
  (dim H^2_cyc = 1) for non-algebraic-family algebras
- The tautological purity step (Gamma = kappa * Lambda) now has a
  precise scope: it holds iff the algebra is uniform-weight

## K-theoretic perspective

rem:structural-saturation (line 8888) gives the structural explanation:
the virtual bar family V_A = [R pi_{g*} B^(g)(A)] in K_0(M-bar_g)
has Chern hierarchy L1 (scalar: kappa = c_1(det V)), L2 (spectral:
Delta_A(x) from full Chern polynomial), L3 (periodic: Pi_A from
holonomy). Scalar saturation says the MC element lives in L1. The
non-scalar invariants (Delta, Pi) are level-direction phenomena
(monodromy around the critical level), not primary-direction phenomena.

## Assessment

**Residual content**: The conjecture's residual open content is narrow:
dim H^2_cyc = 1 for non-algebraic-family modular Koszul algebras. No
known counterexample exists among algebras of Lie-theoretic origin.

**Evidence strength**: Very strong. Every tested case satisfies Layer 1.
The three candidate counterexample classes (non-GKO cosets, 4D N=2
quiver VOAs, admissible quotients of higher rank) have all produced
dim H^2_cyc = 1 in computed examples.

**Tractability**: Moderate. The algebraic-family theorem covers the
standard landscape. The gap is for algebras not known to sit in
algebraic families -- a relatively exotic class. A proof would likely
require new technology (motivic methods, or a structural argument that
Koszulness itself forces dim H^2_cyc = 1).

**Risk of falsity**: Low. The uniform structural reason (Koszul algebras
have rigid OPE structure controlled by a single level parameter) suggests
the conjecture is true. But "low risk" is not a proof.
