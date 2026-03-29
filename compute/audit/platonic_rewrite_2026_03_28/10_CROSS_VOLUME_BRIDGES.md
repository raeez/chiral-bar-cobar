# CROSS-VOLUME BRIDGES — HARMONIZATION PLAN

Seven bridges connect the two volumes. Five are proved, two are conjectural.
The rewrite adds an eighth bridge (the center bridge) and upgrades one
conjectural bridge to proved.

---

## BRIDGE 1: BAR-COBAR BRIDGE (PROVED)

**Vol I side:** Theorem A (adjunction) + Theorem B (inversion) on Ran(X).
**Vol II side:** SC^{ch,top} bar-cobar Quillen equivalence recovers chiral
bar-cobar for boundary operators.

**Current status:** Solid. The Vol II recognition theorem (F4/F5) identifies
SC-algebra structure with A_infty-chiral structure, and the bar-cobar
adjunction on the open color reduces to Vol I's bar-cobar adjunction.

**Action:** Add explicit cross-reference from Vol I Chapter 8 (open sector)
to Vol II equivalence theorem. State: "the local Swiss-cheese bar-cobar
restricted to the closed color recovers the chiral bar-cobar of Vol I."

---

## BRIDGE 2: HOCHSCHILD BRIDGE (UPGRADE: CONJECTURAL -> PROVED)

**Vol I side:** Chiral Hochschild cohomology ChirHoch*(A) (Theorem H).
**Vol II side:** Bulk = HH^bullet_ch(A^!) (bulk-boundary-line triangle).

**Current status:** Stated as conjectural in Vol II. The identification of
bulk local operators with chiral Hochschild cochains was conditional on
the HT theory setup.

**After rewrite:** The center theorem (RL-10) makes this UNIVERSAL:
  A_bulk ~ Z_der(C_op) ~ C^bullet_ch(A_b, A_b) ~ HH^bullet_ch(A)

for ANY A_infty-chiral algebra A, not just HT boundary algebras. The proof
is the initiality of U(A) (Theorem 8.5.3 in Vol I).

**Action:** Upgrade from conjectural to consequence of the center theorem.
Remove conditional language. State as a theorem with proof.

---

## BRIDGE 3: DK-YBE BRIDGE (PROVED)

**Vol I side:** Drinfeld-Kohno comparison. Five-stage DK ladder (DK-0
through DK-5). Chain-level equivalence reversing braiding.
**Vol II side:** Spectral braiding r(z) = Laplace transform of lambda-bracket.

**Current status:** DK-0/1 proved. DK-2/3 proved on evaluation-generated core.
DK-4/5 conditional on MC3 (type A proved; arbitrary type open).

**Action:** Add the Laplace transform dictionary as a bridging formula:

    r(z) = sum_{alpha,beta} Phi_alpha tensor Phi_beta int_0^infty d lambda e^{-lambda z} {Phi_alpha}_lambda Phi_beta}

This connects the Vol I spectral parameter z to the Vol II lambda-bracket.
State as a proposition for polynomial lambda-brackets.

---

## BRIDGE 4: W-ALGEBRA BRIDGE (PROVED)

**Vol I side:** W-algebra Koszul duals. DS reduction as Koszul functor.
Shadow tower for W_N.
**Vol II side:** Feynman m_k from 3d HT theory match bar differential at
genus 0. Genus >= 1 proved algebraically.

**Current status:** Solid at genus 0. Genus >= 1 via inductive genus
determination + HS-sewing.

**Action:** Add the composite-nonlinearity observation (RL-27): the W_3
bracket {W_lambda W} forces composite Lambda into the open category. This
is a CATEGORICAL phenomenon, not just a formula accident. Connect to Vol II
Chapter 20 (W_3 example).

---

## BRIDGE 5: RELATIVE HOLOGRAPHIC BRIDGE (PROVED)

**Vol I side:** Holographic modular Koszul datum H(T) = (A, A^!, C, r(z), Theta_A, nabla^{hol}).
**Vol II side:** Forgetful p: g^{SC}_T -> g^{mod}_A[A] has fiber whose MC
elements lift boundary datum Theta_A to full 3d data.

**Current status:** Proved. The fiber MC elements parametrize extensions of
the boundary shadow tower to the full bulk/boundary system.

**Action:** Reframe using the center theorem: the holographic datum H(T) is
the universal thickening U(A) equipped with the modular twisting morphism.
The six components of H(T) are projections of (Z_ch(C_op), C_op, Theta_C).

---

## BRIDGE 6: LOOP-CONNES BRIDGE (CONJECTURAL)

**Vol I side:** Closed genus creation via Lambda_P (non-separating clutching).
**Vol II side:** BV/Connes operator on the open sector.

**Current status:** Conjectural. The identification of Lambda_P with the
image of the open BV/Connes operator under the derived-center map is
expected but not proved.

**Action:** Keep conjectural. State as a conjecture with the precise
identification: the non-separating clutching map Lambda_P on the closed
shadow tower should be the derived-center image of the cyclic operator B
on HH_*(C_op).

---

## BRIDGE 7: BV FUNCTOR BRIDGE (CONJECTURAL)

**Vol I side:** BV/BRST formalism.
**Vol II side:** Hypotheses (H1)-(H4) define a physics-to-algebra functor
realizing BV = bar at higher genus.

**Current status:** Conjectural. Depends on physical axioms (H1)-(H4).

**Action:** Keep conjectural. Mark clearly as conditional on (H1)-(H4).
State the precise expectation: for an HT theory satisfying (H1)-(H4), the
BV complex at genus g is quasi-isomorphic to the bar complex with curvature
kappa * omega_g.

---

## BRIDGE 8: CENTER BRIDGE (NEW, PROVED)

**Vol I side:** Theorem 8.5.3 (chiral Deligne-Tamarkin): U(A) = (C^bullet_ch(A,A), A)
is the initial Swiss-cheese pair.
**Vol II side:** Theorem 5.X (center theorem): bulk = Z_der(C_op) = C^bullet_ch(A_b, A_b).

**Status:** PROVED. This is the same theorem stated in two ways:
  - Vol I: algebraically, as a universal property of Hochschild cochains
  - Vol II: categorically, as a derived-center computation

**Action:** State explicitly as a cross-volume bridge. The center bridge
is the single theorem that fuses the two volumes into one story:

    Vol I proves the algebraic engine (bar-cobar, Koszul, shadow tower).
    Vol II proves the categorical depth (open sector, center, modularity).
    The center theorem bridges them: bulk = center = cochains.

---

## BRIDGE TABLE (SUMMARY)

| # | Name | Vol I | Vol II | Status |
|---|------|-------|--------|--------|
| 1 | Bar-cobar | Thm A+B | SC Quillen equiv | PROVED |
| 2 | Hochschild | Thm H | Bulk = HH | UPGRADED: PROVED |
| 3 | DK-YBE | DK ladder | Spectral braiding | PROVED (type A) |
| 4 | W-algebra | Shadow tower | Feynman = bar | PROVED |
| 5 | Holographic | H(T) datum | Fiber MC lift | PROVED |
| 6 | Loop-Connes | Lambda_P | BV/Connes | CONJECTURAL |
| 7 | BV functor | BV/BRST | (H1)-(H4) functor | CONDITIONAL |
| 8 | Center | Thm 8.5.3 | Thm 5.X | **NEW, PROVED** |

---

## HARMONIZATION DIRECTIVES

1. Every cross-volume reference must cite both the Vol I and Vol II
   theorem numbers. Use the format "Vol I Theorem X.Y.Z / Vol II Theorem X.Y.Z".

2. The center bridge (Bridge 8) must be stated in BOTH introductions:
   Vol I introduction says "the algebraic center theorem is proved in
   Chapter 8; its categorical and geometric depth is developed in Vol II."
   Vol II introduction says "the center theorem was stated algebraically
   in Vol I Chapter 8; this volume develops its full implications."

3. The Hochschild bridge upgrade (Bridge 2) must be propagated:
   - Vol II concordance: change "conjectural" to "proved"
   - Vol I concordance: add center theorem as the proof mechanism
   - Vol II ht_bulk_boundary_line_core.tex: remove conditional language

4. The DK-YBE bridge (Bridge 3) gains the Laplace transform formula.
   This should appear in:
   - Vol I Yangians chapters (as a remark)
   - Vol II spectral braiding chapter (as a proposition)

5. The W-algebra bridge (Bridge 4) gains the composite-nonlinearity
   observation. This should appear in:
   - Vol I W-algebra chapter (as a remark)
   - Vol II W_3 example chapter (as a theorem about categorical necessity)

6. The holographic bridge (Bridge 5) should be reframed using the center
   theorem. The holographic datum H(T) = (A, A^!, C, r(z), Theta_A, nabla^{hol})
   is the universal thickening U(A) + modular twisting morphism Theta_C
   projected to the six classical components.
