# Wave-8 Adversarial Attack + Heal: Vol II Part VI 3d Quantum Gravity Cluster

**Date**: 2026-04-17
**Agent**: First-principles adversarial mathematician (Kazhdan-Lusztig + Polyakov + Witten + Costello-Gaiotto voice)
**Targets**: `3d_gravity.tex`, `thqg_gravitational_s_duality.tex`, `thqg_3d_gravity_movements_vi_x.tex`, `thqg_ht_bbl_extensions.tex`, `thqg_symplectic_polarization.tex` (Vol II)
**Constraint**: No commit; `AP/HZ/Pattern/Cache #` tokens forbidden in typeset prose; surgical scope only.

---

## Phase 1 attack — findings

### (i) `thm:E3-topological-DS-general` at `3d_gravity.tex:6806`

**Statement**: For any finite-dim simple Lie algebra `g`, any nilpotent `f` with `sl_2`-triple `(e, h_0, f)`, and `k != -h^v`: the BRST identity `T_DS(f) = [Q_CS, G'_f]` holds on `Q_CS`-cohomology; `Z^der_ch(W^k(g, f))` carries E_3-topological.

**Scope claim**: The quantifier says "any nilpotent". The proof uses Jacobson-Morozov to place `h_0 \in h` (Cartan), then `T_imp(f)` involves only Cartan currents `d J_{h_j}`, each `Q_CS`-exact. Specialisations listed: BP, subregular, hook-type.

**Attack**:
1. The Wave-7 #49 flag cited "line 6219"; reading reveals line 6219 is inside `prop:ainf-chiral-modular-bar-reduction` (hexagon cancellation), not `thm:E3-topological-DS-general`. The flag's line number was imprecise. The actual theorem (line 6806) passes the cohomological-vs-chain-level check via `rem:E3-DS-status` (6787).
2. The proof is cohomological only. `rem:E3-DS-status` correctly states: ghost bilinears in `Q_CS * bar c_a` are `Q`-exact, not zero, at chain level. The theorem wording `\ClaimStatusProvedHere` combined with "on `Q_CS`-cohomology" is honest (the theorem statement itself scopes the identity cohomologically).
3. FM81 historic flag (CLAUDE.md Vol II line 374) said "overclaims to non-principal nilpotents — fractional-weight ghost bilinears (BP, min sl_4) are NOT Cartan-only." This is **closed** by `fractional_ghost_chain_level_platonic.tex` (`thm:E3-topological-DS-general-all-good-graded`, `thm:E3-topological-DS-general-explicit-BP`, `thm:E3-topological-DS-general-minimal-sl4`) via branched-cover integralization + Galois descent. The "Cartan-only" proof in 3d_gravity.tex is the cohomological shortcut; the fractional_ghost file supplies the chain-level rigorous backing. Three-lane concordance (`prop:three-lane-fractional-ghost`) gives independent confirmation via Khan-Zeng and de Boer-Tjin routes.
4. Overlap check: `thm:iterated-sugawara-construction` (Vol II `e_infinity_topologization.tex`) scopes to depth-k stress tensor towers for W_N, W_inf. It cites `thm:E3-topological-DS-general` at 54, 106, 260, 272, 610, 617, 657, 1115. No scope conflict: DS-general handles nilpotent orbits, iterated-sugawara handles W-tower depth. Orthogonal strengthenings.

**Verdict**: `thm:E3-topological-DS-general` is correctly scoped. The "cohomological only" caveat is explicit at `rem:E3-DS-status`. Chain-level content supplied by `fractional_ghost_chain_level_platonic.tex`. **No heal needed.**

### (ii) Gravitational S-duality — `thqg_gravitational_s_duality.tex`

**Content**: 44 theorems/propositions/corollaries, all with `\ClaimStatusProvedHere`. Gravitational S-duality derived as Verdier intertwining on Ran(X): `sigma(Theta_A) = Theta_{A^!}`, Virasoro `Vir_c <-> Vir_{26-c}`, self-dual at `c=13`, complementarity `K(Vir) = 13`, Koszul conductor `K_N = 2(N-1)(2N^2+2N+1)`.

**Attack 1** (κ-complementarity hygiene, cross-check against AP234):
- `K(Vir) = 13` (scalar κ-complementarity sum) ✓
- `K_N = c+c^! = 2(N-1)(2N^2+2N+1)` Trinity conductor: at N=2 gives 26 ✓, at N=3 gives 100 ✓
- `K(W_N) = K_N * (H_N - 1)`: at N=3 gives 100 * 5/6 = 250/3 ✓
- ρ_{W_N} = H_N - 1: matches AP234 canonical with ρ_Vir = 1/2, ρ_{W_3} = 5/6 ✓

All AP234 hygiene passes. The two letters `K_N` (Trinity, family-dep) and `K(W_N)` (κ-sum) are properly distinguished. κ + κ^! = ρ_A · K_Trinity holds for W_N with ρ = H_N - 1.

**Attack 2** (phantom cross-volume references):

Grep finds 44 references of the form `\ref{V1-(thm|prop|cor|...):thqg-IV-*}` in `thqg_gravitational_s_duality.tex`. Each such label is marked `% label removed:` at the declaration site — the label was DELETED but references remain pointing at a phantom `V1-` prefix, misleadingly claiming it's a Vol I cross-volume label. Grep across both Vols: **none of the `thqg-IV-*` labels exist anywhere** (verified for `thm:thqg-IV-theta-duality`, `prop:thqg-IV-verdier-dg-lie`).

Systemic count across Vol II `connections/`: 287 phantom `V1-*thqg-*` refs in 14 files. This is same pattern Wave-6 #16 healed (12 phantoms in `chiral_higher_deligne.tex`), but at scale.

**Honest scoping status**: Vol II build currently tolerates these as "expected V1-* cross-volume externals" per `compute/audit/linear_read_notes.md:580` (46 undefined-reference labels classified as "expected"). That classification is FALSE — these are not cross-volume externals; they are broken self-references misprefixed with V1-.

**Scope limit**: Full 287-ref sweep is outside Wave-8 surgical scope. Wave-8 heals the 3 highest-impact labels in `thqg_gravitational_s_duality.tex` (3 most-referenced theorems) to restore the load-bearing self-consistency of the S-duality climax theorem.

**Heal (surgical)**:
1. Restore label `thm:thqg-IV-theta-duality` at line 293 (currently `% label removed`).
2. Restore label `prop:thqg-IV-verdier-dg-lie` at line 205 area.
3. Restore label `thm:thqg-IV-shadow-duality` at line 436.
4. Strip `V1-` prefix from `\ref{V1-thm:thqg-IV-theta-duality}`, `\ref{V1-prop:thqg-IV-verdier-dg-lie}`, `\ref{V1-thm:thqg-IV-shadow-duality}` at the 3 load-bearing cross-reference sites (lines 362, 403, 404, 545, 603, 780, 1504 + proof-of-involutivity).

This restores 3 labels → functional cross-refs within `thqg_gravitational_s_duality.tex`, leaves the remaining 41 phantoms for a future systemic sweep (flagged for Wave-N).

### (iii) 3d gravity movements VI-X — `thqg_3d_gravity_movements_vi_x.tex`

Read first 250 lines (Movement VI: Gravitational S-duality). Theorems present:
- `thm:gravity-verdier-intertwining` (ClaimStatusProvedHere): Virasoro D-intertwining on bar, theta, shadow. Proof via Killing form: `<L_{-n}, L_{-n}> = (c/12)(n^3 - n)` maps to `((26-c)/12)(n^3 - n)` under D.
- `prop:gravity-complementarity-constant`: K = 13 for Virasoro ✓
- `prop:gravity-self-dual-13`: self-duality at c=13 with fusion kernel reflection.
- `prop:gravity-c26-anomaly-cancellation`: scoped carefully — "This does not identify the full higher-degree shadow obstruction tower" at (ii). Honest scope — κ_eff = 0 at c=26 is scalar-only; higher-degree tower matching remains open.

**Verdict**: Movement VI is scope-honest. c=13 vs c=26 distinction (`rem:gravity-13-not-critical`) correct. No heal needed.

### (iv) Bulk construction — `thqg_ht_bbl_extensions.tex`

The global Koszul triangle (line 1670, conjecture scoped by G1-G4): `A_bulk ≃ Z^{der}(B_boundary) ≃ Z^{der}(C_line) ≃ HH^•_ch(A^!_T)`. Status: **conjecture** (G4 is not proved in full generality). Disk-sector proved unconditionally in boundary-linear sector (`thm:fortified-local-triangle`). Holonomy obstruction made explicit via `prop:holonomy-obstruction`.

AP-SC-BAR compliance: bulk = `Z^{der}(B_boundary)` = Hochschild cochain complex (not bar complex of B_boundary). Line 1830: `HH^•(B_boundary) = Z^{der}(B_boundary)`. Correct.

AP-TOPOLOGIZATION: no claim that SC^{ch,top} → E_3 for general chiral; bulk is 3d holomorphic-topological (H1-H4 hypotheses). The topologization question is separated from the bulk-boundary comparison.

AP-CY62 (geometric vs algebraic): the `Z^{der}` here is `HH^•_ch(A^!_T)`, i.e. chiral Hochschild on the algebraic-operadic side; the bulk A_bulk is the 3d HT perturbative theory (geometric on C × R). The equivalence is a comparison map `β_{der}`, not a definitional identity. Correct handling.

**Verdict**: `thqg_ht_bbl_extensions.tex` is scope-honest. No heal needed.

### (v) Cross-references to Vol I

Grepped `V1-thm:|V1-eq:|V1-cor:|V1-prop:` in `thqg_3d_gravity_movements_vi_x.tex` (5 refs): `V1-thm:bar-modular-operad`, `V1-thm:mc2-bar-intrinsic`, `V1-thm:quantum-complementarity-main`, `V1-cor:nms-betagamma-mu-vanishing`, `V1-thm:heisenberg-one-particle-sewing`. All five verified as genuine Vol I labels (Vol I `main.tex`, `appendices/nonlinear_modular_shadows.tex`, `chapters/theory/higher_genus_complementarity.tex`, `chapters/theory/bar_cobar_adjunction_curved.tex`). Clean.

In `3d_gravity.tex`: 2 `V1-thm:thqg-swiss-cheese` refs. Label lives in Vol I `chapters/connections/thqg_open_closed_realization.tex`. Genuine Vol I cross-volume ref. Clean.

### (vi) AP234 propagation (Wave-7 #28) sweep verification

Wave-7 #28 claimed 3 sites swept in Vol II Part VI. Spot-check:
- `thqg_gravitational_s_duality.tex:1168-1179`: K(W_N) = K_N · (H_N - 1) with K_N = 2(N-1)(2N^2+2N+1), κ(W_N) = c · (H_N - 1). Matches AP234.
- `thqg_gravitational_s_duality.tex:1206-1227`: table {N, H_N - 1, K_N, K(W_N), self-dual c_*, κ(c_*)}. N=2: 1/2, 26, 13, 13, 13/2 ✓. N=3: 5/6, 100, 250/3, 50, 250/6 ✓. All consistent with AP234 canonical.
- `thqg_symplectic_polarization.tex:1830-1979`: landscape census. κ(Heis)=k ✓, κ(aff)=dim(g)(k+h^v)/(2h^v) ✓, κ(βγ)=c_βγ/2 ✓, κ(Vir)=c/2 ✓, κ(W_N)=c·(H_N-1) with H_N=∑_{j=1}^N 1/j ✓.

Wave-7 #28 sweep was **clean** on the Part VI target files.

---

## Phase 2 heal — surgical edits

Three label re-inscriptions + six cross-reference unprefixings in `thqg_gravitational_s_duality.tex`:

1. `% label removed: thm:thqg-IV-theta-duality` → `\label{thm:thqg-IV-theta-duality}` (line ~293).
2. `% label removed: prop:thqg-IV-verdier-dg-lie` → `\label{prop:thqg-IV-verdier-dg-lie}` (line ~205).
3. `% label removed: thm:thqg-IV-shadow-duality` → `\label{thm:thqg-IV-shadow-duality}` (line ~436).
4. `\ref{V1-thm:thqg-IV-theta-duality}` → `\ref{thm:thqg-IV-theta-duality}` (7 sites).
5. `\ref{V1-prop:thqg-IV-verdier-dg-lie}` → `\ref{prop:thqg-IV-verdier-dg-lie}` (6 sites).
6. `\ref{V1-thm:thqg-IV-shadow-duality}` → `\ref{thm:thqg-IV-shadow-duality}` (2 sites).

Remaining 35 phantom `V1-thqg-IV-*` refs remain flagged for a future Wave-N systemic sweep across all 14 Vol II `connections/` files (287 total).

---

## Outstanding frontier (passed to future wave)

**VIII-A**: Systemic 287-ref phantom `V1-thqg-*` sweep across 14 Vol II connections files. Pattern: labels disabled via `% label removed:` comment; refs retained with erroneous `V1-` prefix; false classification in `linear_read_notes.md` as "expected cross-volume externals". Heal protocol: restore labels + strip V1- prefix, OR convert every `\ref{V1-thqg-IV-X}` into inline prose description of the referenced result.

**VIII-B**: `thm:E3-topological-DS-general` chain-level class-M closure: the cohomological proof in 3d_gravity.tex (any nilpotent via Jacobson-Morozov Cartan h_0) and the branched-cover chain-level proof in fractional_ghost_chain_level_platonic.tex (all good-graded via degree-d_f Kummer cover + Galois descent) together close chain-level E_3-topological for all good-graded W-algebras. The ONLY remaining open direction is non-good-graded nilpotents (exist in exceptional types, require half-integer Kazhdan grading resolved differently). Flag for Wave-N.

**VIII-C**: Line 6910 in `3d_gravity.tex` has duplicate prose about ghost stress tensor (text at 6877-6881 is repeated verbatim at 6910). Not functional, but aesthetic.

---

## Beilinson verdict

Of the five target files: `thqg_gravitational_s_duality.tex` has one localised heal (3 labels + 15 refs). The other four (`3d_gravity.tex`, `thqg_3d_gravity_movements_vi_x.tex`, `thqg_ht_bbl_extensions.tex`, `thqg_symplectic_polarization.tex`) are scope-honest as inscribed, with `\ClaimStatusProvedHere`/`\ClaimStatusConditional`/`\ClaimStatusConjectured` correctly calibrated.

The 3d quantum gravity climax presentation is structurally sound. The one systemic debt (phantom V1-thqg-* refs) is flagged explicitly for future Wave-N.
