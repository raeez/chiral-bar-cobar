# Multi-Generator Universality at Genus 2 -- Theoretical Frontier Analysis

**Date**: 2026-04-05
**Target**: `op:multi-generator-universality` (higher_genus_foundations.tex:5122)
**Status**: OPEN. New approach identified (Approach F) that resolves genus 2 up to ONE computable residual. All-genera remains open.

## Problem Statement

For multi-weight chiral algebras (generators of conformal weights h_1,...,h_r), does

    obs_g(A) = kappa(A) * lambda_g    in H^{2g}(M-bar_g)

hold at genus g >= 2?

**Known**:
- Uniform-weight algebras: PROVED at all genera (thm:genus-universality)
- All algebras at genus 1: obs_1 = kappa * lambda_1 PROVED unconditionally
- The bar-intrinsic MC element Theta_A = D_A - d_0 satisfies clutching (thm:mc2-bar-intrinsic)
- Algebraic-family rigidity gives Theta^min = eta tensor Gamma_A (one-channel factorization)
- The Kuranishi map vanishes by parity: MC equation does NOT constrain Gamma_A

**Previously failed approaches**:
1. Scalar saturation -- gives line direction only, not coefficient
2. Teleman R=Id -- FALSE (tests prove R != Id for Virasoro)
3. CohFT without flat unit -- insufficient for Teleman reconstruction

---

## Approach A: Direct Genus-2 Computation

**Method**: Compute F_2 explicitly for W_3 (generators T weight 2, W weight 3) via the stable-graph sum over all 6 genus-2 graphs with multi-channel Feynman rules.

**Finding**: The NAIVE (undressed) graph sum gives a nonzero cross-channel correction:

    delta_F2(W_3) = (c + 120) / (16c)

decomposed as:
- Banana (mixed channels): 3/c
- Theta (mixed channels): 9/(2c)
- Lollipop (mixed channels): 1/16

At c = 10: delta_F2 = 13/16 = 0.8125, while F2_scalar = kappa * 7/5760 = 0.0101.
The cross-channel correction DOMINATES the scalar prediction.

**Verdict**: INCONCLUSIVE. The naive graph sum uses undressed (OPE-derived) vertex factors, while the actual bar-complex obstruction obs_g = tr(Theta_A^(g)) involves the full bar differential D_A, which includes R-matrix/Givental dressing effects. The naive cross-channel terms may be cancelled by R-matrix corrections. The computation does NOT falsify the conjecture, but it demonstrates that the conjecture is non-trivial: a precise cancellation between cross-channel OPE contributions and R-matrix corrections must occur.

**What would be needed**: Implement the full Givental-dressed multi-channel graph sum. The R-matrix for the bar-complex CohFT is R(z) = A-hat(iz) * Id (scalar, universal across all channels by AP27). The dressed computation would definitively test whether the cancellation occurs.

---

## Approach B: Tautological Purity

**Method**: If the bar construction always produces tautological classes in R*(M-bar_g), and if lambda_g is the unique tautological class (up to proportionality) in H^{2g}(M-bar_g), then Gamma_A must equal f(kappa) * Lambda.

**Finding**: INSUFFICIENT. For g >= 2, H^{2g}(M-bar_g) has dimension > 1. For g = 2: dim H^4(M-bar_2) = 3 (basis: lambda_1^2, lambda_1*delta_0, lambda_1*delta_1, subject to relations). The Mumford relation gives lambda_2 = lambda_1^2 / 2, so lambda_2 is not independent of other tautological classes. The tautological ring R*(M-bar_g) = H*(M-bar_g) for g = 2 (Faber, proved), so all classes are tautological. But there are 3 independent degree-4 classes, and lambda_2 is just one of them. Tautological purity alone does not force obs_g = kappa * lambda_g.

**Verdict**: FAILS as a standalone approach.

---

## Approach C: Motivic Weight Argument

**Method**: Since the bar propagator d log E(z,w) has weight 1 (AP27), the motivic weight of F_g is independent of field weights. If lambda_g is the UNIQUE class of the correct motivic weight in H^{2g}(M-bar_g), then F_g must be proportional to lambda_g.

**Finding**: FAILS. The cohomology H*(M-bar_g) is of Tate type: H^{p,q}(M-bar_g) = 0 unless p = q. Therefore ALL classes in H^{2g}(M-bar_g) have the same Hodge type (g,g). The motivic weight argument gives no information beyond tautological purity -- it cannot distinguish lambda_g from other degree-2g classes.

**Verdict**: FAILS.

---

## Approach D: Deformation Invariance

**Method**: Deform a multi-weight algebra to a uniform-weight algebra keeping kappa fixed, using the shadow homotopy invariance (thm:shadow-homotopy-invariance).

**Finding**: FAILS. Conformal weights are discrete invariants that determine the algebra type. There is no continuous deformation from W_3 (weights 2, 3) to a uniform-weight algebra. Within a family parametrized by level k, kappa varies but conformal weights are FIXED. Shadow homotopy invariance requires a quasi-isomorphism, not a deformation; but the bar complex is a coalgebra, not an algebra.

**Verdict**: FAILS. No known path from multi-weight to uniform-weight.

---

## Approach E: Index Theory / Anomaly Polynomial

**Method**: The family index theorem (thm:family-index) shows F_g = kappa * lambda_g^FP for uniform-weight algebras via GRR on the K-theory class kappa * [E]. For multi-weight algebras, argue that the K-theory class is still kappa * [E] because the bar propagator is universal (AP27).

**Finding**: PROMISING but INCOMPLETE. The key question: is [B^(g)(A)] = kappa * [E] in K_0(M-bar_g)?

For a DIRECT SUM A = A_1 + A_2 (no mixed OPE): Yes, B^(g)(A) = B^(g)(A_1) + B^(g)(A_2), giving kappa * [E].

For W_3 (NOT a direct sum): The bar complex B^(g)(W_3) involves cross-channel sewing, so it does NOT decompose as a direct sum. The K-theory class depends on both the edge geometry (universal, weight 1) and the vertex algebra (cross-channel structure constants).

The argument that OPE structure constants are "numbers" not "sections of bundles" is suggestive but imprecise. The bar differential at genus g is a map between sheaves on M-bar_g; the OPE coefficients determine the map, but the source and target sheaves are determined by the propagator. Whether the K-theory class depends only on the sheaves (giving kappa * [E]) or also on the map (potentially introducing corrections) is not settled.

**Verdict**: MOST PROMISING among the five original approaches, but has a logical gap at the K-theory level.

---

## Approach F (NEW): Clutching Induction + Harer Vanishing

**Method**: Use the proved clutching axioms of the MC element together with the vanishing of H^{2g}(M_g) (open moduli space) from Harer's virtual cohomological dimension theorem.

### Key Ingredients

1. **MC clutching** (thm:mc2-bar-intrinsic, parts (i)-(iii)):
   - xi_sep^*(Theta^(g)) = sum Theta^(g1) star Theta^(g2)
   - xi_ns^*(Theta^(g+1)) = Delta_ns(Theta^(g))

2. **Genus-1 universality** (proved unconditionally):
   - obs_1 = kappa * lambda_1

3. **Harer's theorem**: vcd(Gamma_g) = 4g - 5, so H^k(M_g, Q) = 0 for k > 4g - 5.

### Analysis at Genus 2

At g = 2: 2g = 4 > 4g - 5 = 3, so **H^4(M_2, Q) = 0**.

The MC clutching axioms give:
- xi_sep^*(obs_2) = kappa^2 * lambda_1 tensor lambda_1 (from obs_1 = kappa * lambda_1)
- xi_ns^*(obs_2) = kappa * Delta_ns(lambda_1)

The class kappa * lambda_2 satisfies the SAME clutching constraints.

The difference alpha := obs_2 - kappa * lambda_2 satisfies:
- xi_sep^*(alpha) = 0
- xi_ns^*(alpha) = 0

By the localization exact sequence and H^4(M_2) = 0 (Harer), the class alpha is constrained. Specifically:

H^4(M-bar_2) has dimension 3, with Poincare duality pairing H^2 x H^4 -> Q nondegenerate.
H^2(M-bar_2) = span{lambda_1, delta_0, delta_1}.

The clutching constraints determine int(alpha * delta_0) = 0 and int(alpha * delta_1) = 0 (by the projection formula: xi_i^*(alpha) = 0 implies the intersection of alpha with the corresponding boundary class vanishes).

**Remaining gap**: The intersection int(alpha * lambda_1) is NOT determined by the clutching axioms alone. This leaves a ONE-DIMENSIONAL ambiguity: alpha could be a multiple of the class in H^4(M-bar_2) that pairs trivially with delta_0 and delta_1 but nontrivially with lambda_1.

### Corrected Analysis: Boundary Restriction Is NOT Injective

**Critical correction** (Beilinson self-audit):

The boundary restriction map i^*: H^4(M-bar_2) -> H^4(delta_0) + H^4(delta_1) maps a 3-dimensional space to a space of dimension at most 2:
- delta_0 has complex dimension 2, so H^4(delta_0) ~ Q (1-dim)
- delta_1 ~ (M-bar_{1,1} x M-bar_{1,1})/S_2 has complex dimension 2, so H^4(delta_1) ~ Q (1-dim)
- Target dimension: at most 2

Therefore ker(i^*) has dimension >= 1. The clutching axioms determine obs_2 up to the kernel of the boundary restriction -- a ONE-DIMENSIONAL ambiguity.

This means Approach F **does not quite close** the genus-2 gap. It reduces the problem to fixing ONE free parameter: the coefficient of the class in ker(i^*: H^4(M-bar_2) -> H^4(boundary)).

### What Would Close the Genus-2 Gap

Any ONE of the following would fix the remaining free parameter and complete the proof at genus 2:

**(F.i)** A direct computation showing int(obs_2 * lambda_1) = kappa * int(lambda_2 * lambda_1) = kappa/480. This is a specific numerical check involving the bar-complex trace at genus 2 paired with the Hodge class. Combined with the clutching constraints, this would pin down obs_2 completely.

**(F.ii)** A structural argument that obs_2 lies in the Hodge-supported subspace span{lambda_1^2} of ker(i^*). If the bar complex produces only Hodge-type classes (no boundary-type classes in the unconstrained direction), this pins down the coefficient.

**(F.iii)** The index theory argument (Approach E) at genus 2: if [B^(2)(A)] = kappa * [E] in K_0(M-bar_2), then GRR gives obs_2 = kappa * lambda_2 directly, bypassing the clutching argument entirely.

**(F.iv)** An independent trace calculation: the "dressed" genus-2 graph sum with the universal scalar R-matrix R(z) = A-hat(iz). If the dressed sum gives F_2 = kappa * lambda_2^FP for W_3 at specific central charges, this provides numerical evidence and (if exact) a proof.

### Genus Range

The Harer vanishing argument works for g = 1 and g = 2 only:

| g | 2g | vcd = 4g-5 | H^{2g}(M_g) = 0? |
|---|-----|------------|-------------------|
| 1 | 2   | -1         | YES               |
| 2 | 4   | 3          | YES               |
| 3 | 6   | 7          | NO                |
| 4 | 8   | 11         | NO                |

At g >= 3, H^{2g}(M_g) is generally nonzero, so the boundary restriction does not determine the class. A different argument would be needed for g >= 3.

---

## Summary and Recommendations

### Current Status of Each Approach

| Approach | Status | Genus Range | Key Gap |
|----------|--------|-------------|---------|
| A (Direct computation) | INCONCLUSIVE | g = 2 | Naive sum != obs_g; need dressed sum |
| B (Tautological purity) | FAILS | -- | dim H^{2g} > 1 for g >= 2 |
| C (Motivic weight) | FAILS | -- | All classes have same Hodge type |
| D (Deformation) | FAILS | -- | No path from multi to uniform weight |
| E (Index theory) | PROMISING | All g | Gap: K-theory class of bar complex |
| F (Clutching + Harer) | REDUCES g=2 to 1 parameter | g = 1, 2 only | One intersection number (ker of bdry restriction) |

### Highest-Leverage Next Steps

1. **Close genus 2 via Approach F**: Compute int(obs_2 * lambda_1) from the bar complex. This is a specific, well-defined computation. If it equals kappa/480, genus 2 is settled for ALL modular Koszul algebras.

2. **Implement dressed genus-2 graph sum** (Approach A + scalar R-matrix): The universal R-matrix R(z) = A-hat(iz) acts componentwise on the diagonal metric. Implementing the Givental action at genus 2 would give a direct numerical test.

3. **Investigate the K-theory class** (Approach E): If [B^(g)(A)] = kappa * [E] can be proved using AP27 and the structure of the bar differential, this closes all genera at once. The argument that vertex data (OPE coefficients) does not modify the K-theory class (because OPE coefficients are scalars, not sections) deserves careful scrutiny.

4. **For g >= 3**: Neither Approach F nor the direct computation extends. Approach E (index theory) remains the only viable path to an all-genera proof. Alternatively, a completely new approach using the modular operad structure of the bar complex might be needed.

### Files Consulted

- `chapters/theory/higher_genus_foundations.tex` (op:multi-generator-universality at line 5122, thm:genus-universality at line 4991, prop:multi-generator-obstruction at line 5248)
- `chapters/theory/higher_genus_modular_koszul.tex` (thm:mc2-bar-intrinsic at line 2975, thm:multi-generator-universality at line 19164, thm:algebraic-family-rigidity)
- `chapters/connections/concordance.tex` (thm:family-index at line 5338)
- `compute/lib/genus2_multichannel.py` (multi-channel graph sum engine)
- `compute/lib/multichannel_genus2.py` (W_3-specific computation)
- `compute/tests/test_genus2_multichannel.py` (249 tests, all passing)

### Honest Assessment

None of the six approaches closes the problem. The strongest finding is the combination of Approach E (index theory) and Approach F (clutching + Harer):

- **Approach F** reduces the genus-2 problem from 3 unknowns to 1 unknown: the coefficient in the kernel of the boundary restriction map.
- **Approach E** suggests the residual unknown is zero (because the K-theory class of the bar complex should be kappa * [E], from AP27), but this has a logical gap at the K-theory level.
- **The combination** provides a clear path to a genus-2 proof: prove [B^(2)(A)] = kappa * [E] in K_0(M-bar_2) for multi-weight A, OR compute int(obs_2 * lambda_1) directly.

For g >= 3: no viable approach exists among those examined. The Harer vanishing fails, the direct computation is intractable, and the index theory argument has the same K-theory gap. A genuinely new idea is needed.

The problem remains OPEN at all genera g >= 2 for multi-weight algebras. The genus-2 case is within reach; g >= 3 requires new tools.

### Key Mathematical Facts Used

- **AP27**: Bar propagator d log E(z,w) has weight 1 for all channels
- **Harer (1986)**: vcd(Gamma_g) = 4g - 5, so H^k(M_g) = 0 for k > 4g-5
- **Mumford relation**: lambda_2 = lambda_1^2 / 2 on M-bar_g for g >= 2
- **Faber**: R*(M-bar_2) = H*(M-bar_2), dim H^4(M-bar_2) = 3
- **MC clutching**: Proved unconditionally by thm:mc2-bar-intrinsic
