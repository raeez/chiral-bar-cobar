# Theorem D Attack-and-Heal (Wave 3, 2026-04-18)

**Scope.** Follow-on audit to Wave 1 (`adversarial_swarm_20260417/wave1_theorem_D_attack_heal.md`) and Wave 2 (`adversarial_swarm_20260418/attack_heal_theorem_D_20260418.md`). Wave 1 split scope at genus 1 / 2 / g≥3 and surfaced scalar-diagonality + λ_g-conjecture as the two load-bearing hypotheses; Wave 2 planned three surgical heals (E1 `thm:kac-moody-obs` scope remark, E2 table caption, E3 PTVV genus-stratified Mok25 scope). Wave 3 verifies the current state of the inscription against those plans and closes residual drift.

## Attack ledger

**A1. `thm:kac-moody-obs` scope remark (Wave-2 E1).** INSCRIBED. `rem:kac-moody-obs-scope` at `higher_genus_foundations.tex:5072-5113` honestly records that Step 2–3 of the proof silently uses scalar-diagonality at g≥2, discharged at positive-integer level via Frenkel–Kac lattice realisation and parafermionic cosets, open at generic non-integer level. The theorem header still carries `\ClaimStatusProvedHere`; the scope remark is the right healing pattern (Wave-2 H1 option (a): scope-restrict via a remark rather than downgrading the tag), since g=1 is unconditional and the positive-integer-level g≥2 cases are also unconditional.

**A2. `tab:obstruction-summary` caption (Wave-2 E2).** WAS STILL INACCURATE prior to Wave-3. The pre-edit caption read "For single-generator scalar-diagonal families, obs_g = κ·λ_g..." while the table lists V_k(sl_2), V_k(sl_3), V_k(E_8) — none of which are single-generator (each has dim(g) currents). HEALED Wave-3: caption rewritten to "For scalar-diagonal families (Heisenberg, Virasoro, rank-1 free fields unconditionally; V_k(g) at positive-integer level via the Frenkel–Kac lattice realisation and the parafermionic coset; generic-level V_k(g) with g non-abelian conditional on Definition [def:scalar-diagonal-hypothesis])...".

**A3. `rem:ptvv-aksz-chain-level-scope` genus-stratified Mok25 (Wave-2 E3).** WAS OVERCLAIMED prior to Wave-3. The pre-edit remark invoked Mok25 log-FM sewing uniformly across all g ≥ 2, which overstates the dependency: at g=1 no nodal sewing is needed, and at g=2 classical Knudsen–Mumford stable reduction handles the two boundary divisors of M̄_2 without log-FM machinery. HEALED Wave-3: remark now genus-stratified — g=1 uses direct PTVV pairing on the universal elliptic curve; g=2 uses classical Knudsen–Mumford stable reduction; g≥3 invokes Mok25 + Francis–Gaitsgory base-change as previously. AP149 resolution-propagation: this correctly narrows the conditional scope of `prop:theorem-D-factorization-homology-alt` to g≥3.

**A4. Faber λ_g-conjecture inscription (AP249 base-change / extension).** Faber–Pandharipande λ_g-conjecture is cited at `higher_genus_foundations.tex:5925-5931, 6081-6105` and at `clutching_uniqueness_platonic.tex:303-312, 340-370` as the external input controlling N^g vanishing for g≥3. The citation chain is honest: external reference (FP00), known at low g (Ionel 2002, Graber–Vakil), open in general. The proposition-level scope is correctly tagged Conditional in both places. Nothing to heal.

**A5. PTVV clause (iii) disjointness (Wave-1 F6 residue).** The rewritten proof at `higher_genus_foundations.tex:6194-6239` genuinely does not cite `prop:scalar-obstruction-hodge-euler`: the scalar coefficient is detected on the genus-1 PTVV pairing, and all-g identification is achieved by clutching on the socle. `rem:ptvv-independence` at :6254-6307 honestly labels this as "complementary presentation with distinct scope" rather than "genuinely disjoint". AP243 (HZ-IV decorator non-disjoint dependency) is correctly avoided.

**A6. Scalar-diagonal hypothesis AP259 tautology check.** `rem:scalar-diagonal-honest` at :5490-5517 honestly admits that the K-theoretic Step 1c defines obs_g by projection to ε_p, making obs_g = κ·λ_g tautological under that definition. The substantive content is that the projected class coincides with the physical bar-curvature obstruction — this is the scalar-diagonal hypothesis proper. Honest scope. No heal.

**A7. Step 3d AP237/AP258 splitting-principle degree accounting.** The 2026-04-17 Wave-1 rewrite of Step 3 as "Chern–Weil corroboration, not an independent proof path" (:5863-5911) correctly identifies Step 1c's K-theoretic class as the load-bearing derivation and Step 3's BGS/Arakelov apparatus as a differential-geometric presentation of the same class. No AP237 residue.

## Surviving core

Theorem D at its honest scope: (S1) obs_1 = κ·λ_1 unconditional for every uniform-weight family (H^2(M̄_{1,1}) = Q·λ_1 is 1-dim). (S2) obs_g = κ·λ_g on the nose in H^{2g}(M̄_g, Q) for g ∈ {1, 2} on scalar-diagonal families (rank-1 strong-generator unconditionally; V_k(g) at positive-integer level via Frenkel–Kac + parafermionic coset). (S3) obs_g = κ·λ_g on the socle R^g/N^g for all g ≥ 1 via two complementary routes: Arakelov–BGS (needs scalar-diagonality) and PTVV + socle clutching (needs λ_g-conjecture at g≥3 for on-the-nose lift, but NOT scalar-diagonality). The two routes agree on their intersection (scalar-diagonal uniform-weight at g ∈ {1,2}) and jointly cover complementary remainders at g ≥ 3. (S4) Multi-weight δF_g^cross: unconditional closed form (c+204)/(16c) at g=2 for W_3; named via graph-sum at g≥3, closed form open.

## Heal plan

Three surgical edits inscribed in this wave:

- **H-A2.** Table caption at `higher_genus_foundations.tex:6314` rewritten to list the scalar-diagonal families explicitly (Heisenberg, Virasoro, rank-1 free fields unconditionally; V_k(g) at positive-integer level; generic-level conditional). Closes Wave-2 E2.
- **H-A3.** `rem:ptvv-aksz-chain-level-scope` at `:6241` rewritten to genus-stratify the Mok25 dependency: g=1 none; g=2 classical Knudsen–Mumford; g≥3 Mok25 + Francis–Gaitsgory. Closes Wave-2 E3.
- **H-A1 (already inscribed).** `rem:kac-moody-obs-scope` at `:5072-5113` (Wave-2 E1 healing, present prior to Wave 3). Verified correct and left intact.

No status-tag changes needed: the inscription already correctly carries `\ClaimStatusProvedHere` on the load-bearing lemmas and `\ClaimStatusConditional` on the PTVV alternative per Wave-1 and Wave-2 heals. CLAUDE.md Theorem D row matches the healed manuscript post-Wave-3 (see AP288 reverse-drift audit below).

## Commit plan

No commits in this wave. The two surgical edits (table caption, PTVV scope remark) are inscribed in the working tree; they belong with the next omnibus manuscript-hygiene commit. The linter's AP24 warnings on lines 244/6411/6423 are pre-existing (κ+κ' = 0 qualified to affine KM / Heisenberg respectively, and κ+κ' = 250/3 for W_3) and are NOT introduced by this edit. AP5 cross-volume sweep: the table caption and PTVV scope remark are local to Vol I; no cross-volume consumer references the exact caption wording or the Mok25 scope phrasing, so no Vol II / Vol III propagation is required.

## AP288 reverse-drift audit (CLAUDE.md vs manuscript)

CLAUDE.md Theorem D row reads: "PROVED unconditional at g=1 (all families via 1-dim H²(M̄_{1,1}) = Q·λ_1); PROVED unconditional at g=2 for single-generator scalar-diagonal families; at g ≥ 3 conditional on (a) scalar-diagonal hypothesis for multi-generator uniform-weight and (b) Faber's λ_g-conjecture for on-the-nose lift from the socle." This is ALMOST accurate post-Wave-3 but carries one residual wording drift: "single-generator scalar-diagonal families" at g=2 overstates, since V_k(g) at positive-integer level is multi-generator AND scalar-diagonal (via Frenkel–Kac). The correct wording per Wave-2 revision is "PROVED unconditional at g=2 for scalar-diagonal families (rank-1 strong-generator unconditionally; V_k(g) at positive-integer level via the Frenkel–Kac lattice realisation; generic-level V_k(g) with g non-abelian conditional)". Pending cleanup in the next CLAUDE.md hygiene pass; a single-word fix ("single-generator" → "rank-1 or lattice-realised") suffices.

No AI attribution. All commits when made will be authored by Raeez Lorgat.
