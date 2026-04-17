# Wave 11. Vol III Part VI "Seven Faces of r_CY(z)" attack / heal.

Date: 2026-04-17. Target: Vol III `~/calabi-yau-quantum-groups/main.tex` lines 1075-1156 (Part VI frame prose) and the Part-V-to-Part-VI teaser at lines 1047-1060. Four chapters inscribed into Part VI (`modular_koszul_bridge.tex`, `bar_cobar_bridge.tex`, `phi_universal_trace_platonic.tex`, `cy_holographic_datum_master.tex`) are FILE-SKIP (prior-wave targets); audit surface is the frame only.

## Phase 1. Location, inventory, seven-face listing

Vol III `main.tex` lines 1075-1156 inscribe `\part{The Seven Faces of $r_{\mathrm{CY}}(z)$}` with label `part:connections`, spanning four input chapters:
- Ch 22 `connections/modular_koszul_bridge.tex` (1047 lines)
- Ch 23 `connections/bar_cobar_bridge.tex` (1842 lines)
- Ch 23a `theory/phi_universal_trace_platonic.tex` (306 lines)
- Ch 24 `connections/cy_holographic_datum_master.tex` (1117 lines)

The frame lists seven faces:
(i) Yangian coproduct twist `\Delta_u - \Delta_u^op` (home: Hopf/quantum group);
(ii) Drinfeld-centre half-braiding `\sigma_V(Z(Rep^{E_1}(A)))` (home: monoidal category);
(iii) KZ monodromy `Hol(\nabla_KZ)` (home: D-module / holonomy);
(iv) BKM vertex-operator exchange `V_\alpha V_\beta - (\alpha \leftrightarrow \beta)` (home: BKM VOA);
(v) Maulik-Okounkov stable envelope `Stab_C \circ Stab_{C'}^{-1}` (home: equivariant K-theory);
(vi) A_\infty coassociator `\delta^{(3)}` (home: shadow tower);
(vii) Costello 5d hCS tree amplitude `Tree^{hCS}_z[\fgl_1]` (home: BV field theory).

## Phase 2. Adversarial findings

### F1. Conductor identity K-ambiguity (AP234 / B93, CRITICAL).

Line 1097 stated `\kappa_{ch}(A) + \kappa_{ch}(A^!) = K`, followed (lines 1101-1103) by the list `K = 0` (class G/L), `K = 13` (Virasoro), `K = 4N^3 - 2N - 2` (W_N, values `{26, 100, 246, 488}`). This conflates two distinct K's, both routinely written with the same letter:

1. **Scalar complementarity**, `\kappa + \kappa^!`, family-dependent and equal to `{0, 13, 250/3, 98/3, ...}` at `{KM/free, Virasoro, W_3, BP}`.
2. **Trinity invariant**, `K(A) = c(A) + c(A^!) = -c_{ghost}(BRST)`, with canonical values `{-k, 2\dim\fg, 26, 100, 196, ...}` and `K(W_N) = 4N^3 - 2N - 2` (Vol I `chapters/examples/landscape_census.tex:938, 1522`; `chapters/theory/universal_conductor_K_platonic.tex:592`; `chapters/theory/kappa_conductor.tex:231`).

At W_2 = Virasoro the frame stated simultaneously `K = 13` and `K = 26`, which is internally contradictory under the single-letter identification. The correct bridge (Vol I AP234) is `\kappa(A) + \kappa(A^!) = \varrho_A \cdot K(A)` with `\varrho_{W_N} = H_N - 1`, `\varrho_{KM} = \varrho_{free} = 0`, `\varrho_{BP} = 1/6`. Numerical check at W_2: `\varrho_{W_2} = H_2 - 1 = 1/2`, `K(W_2) = 26`, so `\kappa + \kappa^! = 13` \checkmark; at W_3: `\varrho = 5/6`, `K = 100`, `\kappa + \kappa^! = 250/3` \checkmark.

**Heal.** Rewrote the frame to state both identities explicitly, label the prefactor `\varrho_A`, enumerate Trinity values `{V_k(\fg): 2\dim\fg; W_N: 4N^3 - 2N - 2; BP: 196}`, and note that class G (K3 Heisenberg) has `\varrho = 0` so both sides vanish. `main.tex:1095-1108` (new version).

### F2. Bare `\Phi` without dimension subscript (AP247).

Frame prose at lines 1047-1049 and 1081 referenced "the CY output of $\Phi$" without dimension qualifier. Vol III Part II inscribes the stratified family `\{\Phi_d\}_{d \ge 1}` (CY-to-chiral functor varies with complex dimension; E_2-chiral output at d \le 2, E_1-chiral at d \ge 3).

**Heal.** Both teaser (line 1048) and frame (line 1081) now read "$\{\Phi_d\}_{d \ge 1}$".

### F3. Seven-face distinctness (AP244). ACCEPT.

Home-category audit for the seven faces: Hopf coproduct (i), monoidal centre (ii), holonomy / D-module (iii), BKM VOA (iv), equivariant K-theory stable envelope (v), A_\infty coassociator tower (vi), 5d hCS BV tree amplitude (vii). Seven genuinely distinct categories; no pairwise collapse.

### F4. AP246 (K3 Yangian osp vs gl). No-fire.

Part VI frame does not state a K3 Yangian type; the K3 Yangian content lives in Part IV (`k3_yangian_chapter.tex`, file-skip). No in-frame violation.

### F5. Unification TFAE theorem absent. Accept at current scope.

Vol I Part V seven faces ends with `thm:seven-faces-of-r` (the TFAE unification). Vol III Part VI frame promises "each independent, all agreeing on the CY output of $\Phi_d$" but does not inscribe a `thm:seven-faces-of-r-cy` TFAE in main.tex. The individual equivalences live in the four input chapters (bar_cobar_bridge = shadow-Feynman, phi_universal_trace = face-(i)-(ii) identification, cy_holographic_datum_master = bulk categorical trace synthesising (iii)-(vii)). A consolidated TFAE frame-theorem is a natural next inscription, but none of the four inscribed chapters currently proves the full seven-way unification; scope is correct in the frame prose ("all agreeing").

### F6. Costello "5d" hCS (face vii). Accept.

Engine `compute/lib/costello_5d_verification.py`, appendix `conventions.tex:180`, and notes/theory_coha_e1_sector.tex:1188 (Costello-Li 5d NCCS) confirm the 5d scope. Distinct from Costello 4d mixed holo-topol and from 6d twistor hCS (both of which also appear in Vol III `engine_table_rows.tex` but are not the face-(vii) ingredient).

### F7. DNP25 attribution. Accept.

`FRONTIER.md:332` cites Dimofte-Niu-Py, arXiv:2508.11749 (2025). `cy_holographic_datum_master.tex:695` uses `\hbar^{DNP}` consistently. No miscitation.

### F8. Shadow-Feynman dictionary. Accept as restated.

Lines 1106-1117 state `L`-loop Feynman amplitude = `S_{L+1}` = `\delta^{(L+1)}` coefficient of the `A_\infty`-coproduct correction tower. Class M `E_3` bar = `6^g`. Both consistent with Vol I `shadow_towers_v3.tex` and with the Kunneth computation in Vol III `m3_b2_saga.tex`.

### F9. HZ-7 bare `\kappa` in Part VI frame. Zero hits. Accept.

All `\kappa` occurrences in main.tex frame block carry `_{ch}` subscript.

## Phase 3. Heals (Vol III main.tex only)

Two edits, frame-local:

1. **main.tex:1047-1060** (teaser into Part VI): added `{\Phi_d}_{d \ge 1}` qualifier; replaced bare `\kappa + \kappa^! = K, K=0 at K3` with the scalar-complementarity identity carrying `\varrho_A` prefactor and the explicit class-G rationale for vanishing at K3 Heisenberg.
2. **main.tex:1078-1108** (Part VI header + conductor block): added dimension subscript to `\Phi`; restated the conductor identity as TWO distinct identities (scalar-complementarity with `\varrho_A`, Trinity invariant `K = c + c^!`), with canonical values enumerated for `V_k(\fg)`, `W_N`, BP, and the K3 vanishing noted as a class-G consequence.

No chapter-level edits (file-skip).

## Phase 4. Register

Cache entry #218 (AP234 two-K collision) fires on Vol III main.tex line 1097 and 1058. Heal inscribed. No new AP.

## Cross-volume

AP5 propagation check — grep for `\kappa(A) + \kappa(A^!) = K` (bare, no `\varrho`) across three volumes:

```
grep -rn '\\kappa.*+.*\\kappa.*!.*=.*K[^(]\|kappa + kappa.*= K' chapters/ main.tex
```

Vol I instances (sampled): all carry `\varrho_A` prefactor or are Trinity-K statements under the `c + c^!` letter, not bare `\kappa + \kappa^! = K`. Vol III: main.tex frame was the single outstanding bare-`K` site; now healed.

## Verdict

ACCEPT at healed scope. Part VI frame now honestly distinguishes the two K-invariants, carries the `\{\Phi_d\}` family qualifier, and preserves the seven-face distinctness. Four inscribed chapters deferred (prior-wave file-skip). No commit.
