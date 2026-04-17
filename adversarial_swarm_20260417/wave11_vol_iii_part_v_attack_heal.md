# Wave-11 Vol III Part V CY Landscape — Adversarial Audit + Heal

Date: 2026-04-17
Scope: Vol III (`~/calabi-yau-quantum-groups`) Part V `\part{The CY Landscape}` (main.tex:983-1070 and chapters `matrix_factorizations.tex`, `fukaya_categories.tex`, `super_riccati_shadow_tower_platonic.tex`, `quantum_group_reps.tex`, `modular_trace.tex`). Skipped per prior-wave FILE SKIP list: `cy_d_kappa_stratification.tex`, `toric_cy3_coha.tex`, `coha_wall_crossing_platonic.tex`, `k3_yangian_chapter.tex`, `k3e_bkm_chapter.tex`, `k3e_cy3_programme.tex`, `k3_chiral_algebra.tex`, `k3_quantum_toroidal_chapter.tex`, `toroidal_elliptic.tex`, `derived_categories_cy.tex`, `cy_c_*`.

## Phase 1 findings

### F1 (CRITICAL; HEALED). κ_cat vs κ_ch conflation in `quantum_group_reps.tex:498-576`.
The proposition `prop:kappa-cat-quantum-groups` assigned the formula
`κ_cat(C(g,q)) = dim(g)(k+h^v)/(2h^v)` (Sugawara-shift affine KM). That
is the Vol I CHIRAL modular characteristic `κ_ch(V_k(g))`, not the
CATEGORICAL Euler characteristic `κ_cat = χ(O_X)`. The inconsistency
surfaced in the same chapter at line 549, which correctly states
`κ_cat(K3×E) = χ(O_{K3×E}) = 0` (multiplicative Künneth, Wave-4). The
two statements cannot both hold: the Sugawara formula has no `χ(O_X)`
factor, and `sl_2` at generic k gives `3(k+2)/4 ≠ 0`.

### F2 (CRITICAL; HEALED). Downstream `prop:kappa-cat-complementarity` inherited F1's conflation.
Its "proof" manipulates `dim(g)(k+h^v)/(2h^v)` (a κ_ch quantity) under
`k → -k-2h^v` and calls the result κ_cat complementarity. That is the
bosonic KM κ_ch complementarity (Vol I Thm C), not a κ_cat statement.

### F3 (HEALED). `super_riccati_shadow_tower_platonic.tex:91-92` stated `κ_ch(V_k(g)) + κ_ch(V_{-k-2h^v}(g)) = dim(g)/2` — false at both endpoints: at k = -h^v both summands equal 0; in general the sum is 0 (Feigin-Frenkel) or 13 for Virasoro (AP234 K≠κ+κ'). The super-rank offset `max(m,n)` is correct for the super-Yangian Koszul pair (Wave-3 Wave-16); the bosonic KM comparison was the drifted clause.

### F4 (OPEN; not healed in this pass). AP247 Φ_d indexing drift.
`main.tex` uses bare `\Phi` throughout lines 387, 398-405, 438, 467, 481, 488, 517, 644, 668, 721, 756. Prior-wave policy `\Phi_d` with dimension index is not enforced in the Part V front-matter. Healing this requires a coordinated sweep across the five listed chapters plus the front-matter; deferred to a dedicated pass.

### F5 (OPEN; not healed). Per-d family enumeration missing in Part V front-matter.
`main.tex:983-1070` gives the CY-D tri-stratum table and the toric CY_3 benchmark table, but does NOT enumerate the Wave-4 canonical families per d: d=1 (E), d=2 (K3, abelian surface, bielliptic, Enriques), d=3 (quintic, K3×E, E^3, local P^2, conifold), d=4 (sextic, K3×K3, T^8), d=5 (CY_5 generic). Front-matter defers to Ch 23 `cy_d_kappa_stratification.tex` (FILE SKIP) where the values do live, but a reader of Part V only sees the toric CY_3 table. Action queued for next wave: add enumeration paragraph pointing to the relevant subchapters.

### F6 (OK, verified). Fukaya κ_cat values match Wave-4 Hodge supertrace.
- K3 Fukaya (line 171, 176): κ_cat = χ(O_K3) = 2 ✓ (Wave-4 K3 = 2)
- abelian A (line 216-220): κ_cat = 0 ✓ (Wave-4 abelian = 0)
- quintic X_5 (line 325): κ_cat = χ(O_{X_5}) = 0 ✓ (Wave-4 quintic = 0)
- conifold (line 344): κ_ch = 1 ✓ (AP-CY34 NOT local surface, direct McKay)

### F7 (OK, verified). Matrix factorisations κ values coherent.
- MF(W) CY_2: κ_ch(Φ(MF(W))) = χ(HH_*(MF(W))) = μ(W) Milnor number (line 76, 81).
- Fermat K3: κ_cat=2, κ_fiber=24, κ_ch=2, κ_ch^MF=81 (line 261-266) — self-consistent table.
- Quintic LG: κ_ch = 1024 = 4^5 Jacobi-ring dimension (line 356-362) ✓.

### F8 (OK). HZ-7 bare κ compliance.
`grep \\kappa(?!_\{?(ch|cat|BKM|fiber))` on all five in-scope Part V chapters returned zero matches (subscripts κ_ell, κ_T, κ_psi for section-local dummy indices are fine per HZ-7 local-definition clause).

### F9 (OK). Conifold scope.
`fukaya_categories.tex:344` and the main.tex toric CY_3 table at 1008 treat conifold correctly: κ_ch = 1 via direct McKay, NOT via local-surface χ(S)/2. `cor:conifold-non-local-surface` respected.

### F10 (OK). AP246.
No bare `Y(gl(4|20))` or `Y(gl(4|20))^ch` misnaming in Part V chapters. K3-Yangian references route to `k3_yangian_chapter.tex` (FILE SKIP) which already uses Y_osp(4|20).

## Phase 2 edits (surgical, in-scope only)

1. `chapters/examples/super_riccati_shadow_tower_platonic.tex:86-97` — replace the falsified `κ+κ' = dim(g)/2` clause with the correct `κ+κ' = 0` bosonic KM Feigin-Frenkel complementarity, contrasting to Virasoro=13 and to super-rank offset max(m,n).
2. `chapters/examples/quantum_group_reps.tex:498-528` — rename Proposition `κ_cat for quantum groups` to `κ_ch on the chiral-algebra side`, relabel table column header from κ_cat to κ_ch(V_k(g)), reword prose to distinguish chiral vs categorical invariants.
3. `chapters/examples/quantum_group_reps.tex:552-580` — rewrite complementarity proposition in κ_ch (not κ_cat), with Feigin-Frenkel proof in κ_ch.

Label `prop:kappa-cat-quantum-groups` kept for cross-reference continuity (only internal self-reference at line 16 inside the same chapter; no external refs across Vol III via grep).

## Deferred (next wave)

- F4 Φ_d indexing sweep across Part V and Part VI.
- F5 per-d family enumeration in Part V front-matter.
- AP5 cross-volume propagation: grep Vol II and Vol I for any
  `κ_cat = dim(g)(k+h^v)/(2h^v)` variant. Preliminary grep found the
  pattern only in Vol III and only in the two propositions healed
  above.

## Voice

Beauville CY_2 classification (Enriques/bielliptic/abelian/K3) framing
present in `cy_d_kappa_stratification.tex` (FILE SKIP). Bondal-Orlov
derived equivalence invoked via Fukaya/derived mirror pairs. Bridgeland
CY_3 stability-manifold framing in `coha_wall_crossing_platonic.tex`
(FILE SKIP). Nakamura conifold via AP-CY34 citation in
`cy_d_kappa_stratification.tex`.

## Closing

Two CRITICAL conflations (F1, F2) healed at the source. One HIGH (F3)
healed. Two OPEN findings (F4 Φ_d, F5 per-d enumeration) queued. No
AP5 propagation required beyond the edited chapter.
