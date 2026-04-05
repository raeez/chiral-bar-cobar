# Pixton Ideal from MC Tower: Complete Investigation

## Date: 2026-04-05

## Conjecture Under Study

**conj:pixton-from-shadows** (concordance.tex, line 3596):
For class-M algebras with r_max = infinity, the infinite family
of MC-descended tautological relations generates the Pixton ideal
in R*(M-bar_{g,n}).

## Executive Summary

The conjecture is **PROVED for all semisimple cases** and **GENUINELY OPEN
for non-semisimple cases only**. The manuscript already correctly states
this in rem:pixton-conjecture-status and thm:planted-forest-structure(vi).
No upgrade of the conjecture statement is warranted because the conjecture
as written covers non-semisimple class-M algebras, which are the residual
open frontier.

## Detailed Findings

### 1. Genus-2 Explicit Verification (CONFIRMED)

The MC equation at (g=2, n=0) decomposes over the 7 stable graphs of
M-bar_2:

| Graph | Codim | Vertex type | Weight | Hodge integral I | Contribution |
|-------|-------|-------------|--------|-----------------|--------------|
| A (smooth) | 0 | (2,0) | 1 | 1 | F_2 (determined) |
| B (lollipop) | 1 | (1,2) | kappa | 1/24 | kappa/48 |
| C (sunset) | 2 | (0,4) | S_4 | 0 | 0 |
| D (dumbbell) | 1 | (1,1)x2 | kappa^2 | -1/576 | -kappa^2/1152 |
| E (bridge-loop) | 2 | (0,3)+(1,1) | S_3*kappa | -1/24 | -S_3*kappa/48 |
| F (theta) | 3 | (0,3)x2 | S_3^2 | 1 | S_3^2/12 |
| G (figure-8) | 3 | (0,3)x2 | S_3^2 | 1 | S_3^2/8 |

**Planted-forest correction** (codim >= 2):
```
delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48
```
Verified algebraically from graph sum. Matches eq:planted-forest-genus2-explicit-bridge.

**Depth-class behavior:**
- Class G (Heisenberg, S_3=0): delta_pf = 0. Only Mumford relations. CONFIRMED.
- Class L (affine sl_2, S_3=2, S_4=0): delta_pf = (40 - 3(k+2)/4)/24. Nonzero.
- Class M (Virasoro, S_3=2, kappa=c/2): delta_pf = (40-c)/48. Nonzero for c != 40.

Note: C (sunset) contributes zero because the Hodge integral I(C) = 0
(self-loop parity vanishing for 2 self-loops at genus 0, since dim M-bar_{0,4} = 1
is odd). So S_4 does NOT enter the genus-2 integrated planted-forest at n=0.
It enters at the class level via descendant pairings (rem:class-vs-integrated-visibility).

### 2. Genus-3 Explicit Verification (CONFIRMED)

The MC equation at (g=3, n=0) involves all 42 stable graphs:
- 4 with 1 vertex, 12 with 2 vertices, 15 with 3 vertices, 11 with 4 vertices
- 35 planted-forest graphs, 7 pure-kappa graphs
- Self-loop parity: triple-loop graph (0,6) has I = 0. CONFIRMED.
- Orbifold Euler characteristic: chi^orb = -12419/90720. CONFIRMED.

**Planted-forest correction** (generic shadow data):
```
delta_pf^{(3,0)} = 15*S_3^4/64 + 15*S_3^3*kappa/512 + 65*S_3^2*S_4/48
                 + S_3^2*kappa^2/1152 - 11*S_3*S_4*kappa/1152
                 + 13*S_3*S_5/16 + S_3*kappa^3/82944 + 115*S_3*kappa/768
                 - 7*S_4^2/12 - S_4*kappa^2/1152 + S_5*kappa/192
```

**Shadow visibility:** S_4 and S_5 both appear with nonzero coefficients.
This is consistent with g_min(S_4) = 3, g_min(S_5) = 3.
The genus-3 MC relation is genuinely NEW (not implied by genus-2 data).

**Virasoro evaluation:** For c in {1,2,10,13,25,26}, the planted-forest
correction is nonzero (values range from ~3.0 to ~11.3).

### 3. Theoretical Framework: MC -> CohFT -> Pixton

**The proof chain (semisimple case):**

1. The shadow obstruction tower Theta_A restricted to genus 0 defines
   a Frobenius algebra on V (the primary lines).

2. If this Frobenius algebra is semisimple:
   - Givental-Teleman (Givental01, Teleman12) classifies the CohFT as
     the unique semisimple CohFT extending the genus-0 data.
   - The R-matrix is determined (R=1 for rank 1; nontrivial for rank >= 2).

3. PPZ19 Theorem 0.2: For any r >= 2, the r-spin tautological relations
   together with the lambda_g relation generate the Pixton ideal I_g.
   
4. The MC equation at (g,n) produces exactly the CohFT relation Omega_{g,n}.
   For the A_{N-1} CohFT (from W_N), these are (N+1)-spin relations.

5. The MC tower at all (g,n) includes the lambda_g relation from the
   smooth graph: F_g + boundary = 0 is a tautological relation expressing
   kappa*lambda_g^FP in terms of boundary classes.

6. Therefore: MC-descended relations generate I_g for semisimple algebras.

**Scope of the proof:**
- Class G (Heisenberg): PROVED (trivially, delta_pf = 0, Mumford only)
- Class L (affine KM, S_3 != 0): PROVED (semisimple at rank 1)
- Class C (beta-gamma, S_3 != 0): PROVED (semisimple at rank 1)
- Class M (Virasoro, S_3 = 2): PROVED (semisimple at rank 1)
- Class M (W_N, A_{N-1} Frobenius): PROVED (semisimple at generic level)
- All W_k(g, f) whose Slodowy slice gives semisimple singularity: PROVED

This is stated in thm:planted-forest-structure(vi) and rem:pixton-conjecture-status.

### 4. The Precise Gap

The conjecture remains GENUINELY OPEN for:

**(a) Logarithmic/non-rational algebras** (e.g., W(p) triplet algebras)
where the genus-0 Frobenius structure is non-semisimple.
Givental-Teleman does not apply; the CohFT is not determined by genus-0 data.
PPZ19 requires semisimplicity.

**(b) Admissible-level simple quotients** L_k(g) where vacuum null vectors
collapse the Frobenius algebra to a non-semisimple quotient.

**(c) Algebras outside the Koszul locus** where the shadow CohFT
(thm:shadow-cohft) may not exist.

**The mathematical obstruction:** PPZ19 Theorem 0.2 uses the Givental-Teleman
decomposition in an essential way: the R-matrix action preserves the Pixton
ideal, and the trivial CohFT (from which all semisimple CohFTs are obtained
by R-action) generates the Pixton ideal by the r-spin argument.
For non-semisimple CohFTs, there is no such decomposition.

**Possible approaches to the gap:**

1. **Extended PPZ:** Develop a non-semisimple analog of PPZ19.
   This would require understanding how the Pixton ideal behaves
   under the Dubrovin connection at non-semisimple points.
   Progress: Buryak-Clader-Janda (coderived DR cycles) may extend
   to non-semisimple cases, but this is not yet established.

2. **MC-intrinsic argument:** The MC equation has more structure
   than an arbitrary CohFT. The infinite tower (all arities, all genera)
   might force Pixton generation by a mechanism that bypasses the
   CohFT classification. The MC equation's universality (it holds for
   ALL chirally Koszul algebras) gives a parameter family; the
   tautological relations from DIFFERENT algebras in the same family
   might together generate the ideal.

3. **Parameter variation:** For class-M algebras (Virasoro parametrized
   by c), as c varies the MC relations sweep a family of tautological
   classes. For rank-1, this family is 1-dimensional (parametrized by c),
   which is insufficient. For rank-N (W_N), the family is (N-1)-dimensional,
   which could be sufficient at each genus. Taking the UNION over all
   principal W_N (all N) gives an infinite-dimensional family.
   Whether this generates the Pixton ideal is a question about the
   Zariski closure of the image of the MC map in the space of tautological
   relations.

### 5. Assessment of conj:pixton-from-shadows

**Current status:** The conjecture as stated is a PARTIALLY PROVED
conjecture: proved for the semisimple case, open for the non-semisimple case.

**No upgrade is warranted** because:
- The manuscript already states the semisimple case as a theorem
  (thm:planted-forest-structure(vi)).
- The remaining open cases are genuinely hard (require new mathematics).
- The conjecture statement correctly covers all class-M algebras.

**The genus-2 and genus-3 verifications** confirm that:
- The MC relations produce the correct tautological classes.
- New shadow data (S_4, S_5) enters at genus 3 as predicted.
- The planted-forest correction is exactly eq:delta-pf-genus2-explicit.
- The computational infrastructure (286 tests, all passing) is sound.

### 6. Relation to Other Open Problems

The Pixton conjecture connects to:
- **op:multi-generator-universality**: Whether obs_g = kappa*lambda_g at
  all genera for multi-weight algebras. This affects the smooth graph
  contribution at each genus. If the scalar formula holds, the lambda_g
  relation in the MC tower is exactly kappa*lambda_g^FP for all families.

- **Modular cooperad completion**: The full modular cooperad structure
  on the open factorization category C_op would give a rigorous
  framework for the MC equation at all (g,n) simultaneously,
  potentially providing a structural argument for Pixton generation
  that bypasses PPZ.

- **Pixton's conjecture (R* = tautological ring modulo Pixton relations)**:
  This is now a theorem (proved by PPZ-Clader-Janda). Our question is
  the CONVERSE direction: whether MC relations generate the ideal.

## Files Read

- `/Users/raeez/chiral-bar-cobar/compute/lib/pixton_shadow_bridge.py` (all parts)
- `/Users/raeez/chiral-bar-cobar/compute/lib/pixton_mc_relations.py` (all parts)
- `/Users/raeez/chiral-bar-cobar/compute/lib/pixton_genus3_engine.py` (all)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex` (lines 20090-20190)
- `/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex` (lines 3596-3693)

## Tests Run

286 existing tests pass (pixton_shadow_bridge, pixton_mc_relations,
pixton_genus3_engine, pixton_planted_forest).

## Computations Performed

1. Genus-2 MC relation decomposition for generic, Virasoro, Heisenberg, affine shadow data
2. Genus-3 planted-forest correction with generic shadow data
3. Shadow visibility verification (S_4, S_5 appear at genus 3)
4. Self-loop parity vanishing at genus 3
5. Orbifold Euler characteristic verification at genus 3
6. Virasoro planted-forest numerical evaluation at genus 3

## Error Analysis (Beilinson)

### Finding 1: Class-M restriction is too narrow (MODERATE)

The conjecture restricts to "class-M algebras with r_max = infinity."
However, the PPZ argument works for ALL chirally Koszul algebras with
semisimple genus-0 Frobenius (S_3 != 0 at rank 1). This includes:
- Class L (affine KM, S_3 = 2, S_4 = 0): shadow CohFT = WK CohFT
  (by Givental-Teleman, since R=1 at rank 1). PPZ gives Pixton generation.
- Class C (beta-gamma, S_3 != 0): same argument.

The class-M restriction is UNNECESSARY for the proved semisimple case.
The shadow depth r_max is irrelevant: even if the planted-forest terminates
at finite arity, the full MC tower at all (g,n) produces the COMPLETE
set of CohFT relations, which generate the Pixton ideal by PPZ.

The manuscript's rem:pixton-conjecture-status correctly states the
broader claim ("all chirally Koszul algebras whose genus-0 shadow data
defines a semisimple Frobenius algebra"). The conjecture statement itself
(conj:pixton-from-shadows) could be broadened, or the remark could
explicitly note that the proved result is STRONGER than the conjecture.

This is not a mathematical error: the conjecture is TRUE for class M
(as a consequence of the stronger semisimple result). The issue is
that the conjecture is stated more narrowly than what is proved.

### Finding 2: "Expected" qualifier in proof of (vi) (MINOR)

The proof of thm:planted-forest-structure(vi) says the identification
of W_N genus-0 data with A_{N-1} prepotential is "expected for general N
from the free-field realization." This should be strengthened to
"follows from the Feigin-Frenkel theorem [FF92, Arakawa15] and
standard Saito Frobenius manifold theory [Saito83, Dubrovin96]."
The identification IS a theorem, not a heuristic.

### Finding 3: Conjecture environment is correct (CONFIRMATION)

**The conjecture label conj:pixton-from-shadows is in a
\\begin{conjecture} environment** (concordance.tex line 3596),
which is appropriate because the general statement (including
non-semisimple cases) IS genuinely conjectural.
The proved semisimple case is stated as part of thm:planted-forest-structure(vi),
which is in a \\begin{theorem} environment. This avoids the AP40 anti-pattern
(environment/tag mismatch).
