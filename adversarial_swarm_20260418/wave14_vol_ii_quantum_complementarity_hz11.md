# Wave-14 Vol II `V1-thm:quantum-complementarity-main` AP287 HZ-11 sharpening

Date: 2026-04-18
Target: Vol II consumers of Vol I `thm:quantum-complementarity-main` (canonical: Vol I `higher_genus_complementarity.tex:540-609`, ClaimStatusProvedHere, Lagrangian polarization).
Prior: Wave-10 (commit ad057aad) retargeted 15 Vol II `\ref{thm:quantum-complementarity-main}` consumers to `\ref{V1-thm:quantum-complementarity-main}` via phantomsection alias (main.tex:809) + blanket Remark[Attribution] at `vol2/bv_brst.tex:794-811` (`rem:quantum-complementarity-vol1-attribution`).
This wave: site-by-site AP287 classification + targeted HZ-11 sharpening for genuine violations.

## Site-by-site classification (15 consumer sites)

| # | File | Line | Context | AP287? | Heal |
|---|------|------|---------|--------|------|
| 1 | `thqg_symplectic_polarization.tex` | 32 | Section opener motivational prose (not inside ProvedHere proof) | No | Option A: "Volume~I," prefix added |
| 2 | `holomorphic_topological.tex` | 1123 | Comparison table cell (Costello vs monograph scoreboard) | No | Option A: "Vol~I" in cell |
| 3 | `holomorphic_topological.tex` | 1221 | Inside `\begin{remark}[...]` listing Costello gaps | No | Option A: "Volume~I," prefix |
| 4 | `holomorphic_topological.tex` | 1429 | Inside `\begin{remark}[...]` (structure list) | No | Option A: "Volume~I," prefix |
| 5 | `thqg_3d_gravity_movements_vi_x.tex` | 121 | Free prose AFTER `prop:gravity-complementarity-constant` proof closes | No | Option A: "Volume~I," prefix |
| 6 | **`thqg_gravitational_s_duality.tex` | 1679** | **Inside ProvedHere `thm:thqg-IV-four-facets` clause (IV); proof body at :1705-1714 load-bearing on Vol~I result** | **YES** | **Option B: `rem:thqg-IV-four-facets-attribution` inserted immediately after theorem env** |
| 7 | `twisted_holography_quantum_gravity.tex` | 511 | Inside gravitational-phase-space definition; already "Volume~I, Theorem~..." | No | Already healed |
| 8 | `twisted_holography_quantum_gravity.tex` | 747 | Inside `[Proof sketch]` of thm; already "Volume~I, Theorem~..." | No | Already healed |
| 9-15 | `bv_brst.tex` | 824, 880, 1197, 1221, 1239, 1245, 1346 | All inside same chapter as Wave-10 blanket `rem:quantum-complementarity-vol1-attribution` at :794-811 (semantic, not tactical: covers "all invocations of Theorem~\ref{V1-thm:quantum-complementarity-main} in this chapter") | No (AP286-compliant blanket heal already in place) | Already healed |

Summary: 1 AP287 canonical violation healed (Option B Remark[Attribution]); 5 prose sites sharpened with "Volume~I" prefix (Option A); 9 sites already healed by prior passes (Wave-10 blanket + earlier "Volume~I" prefixes in twisted_holography chapter).

## Incidental AP124 duplicate phantomsection healed

`main.tex` carried TWO `\phantomsection\label{V1-thm:quantum-complementarity-main}` declarations (line 809 Wave-10 insertion with annotation; line 978 legacy batch). Duplicate at :978 replaced with a comment pointing at the canonical one at :809. Label uniqueness (AP124/125) restored.

## Heals applied (files touched)

1. `/Users/raeez/chiral-bar-cobar-vol2/main.tex`: AP124 duplicate phantom removed at :978.
2. `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:32`: "Volume~I," prefix.
3. `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1123,1221,1429`: "Vol~I,"/"Volume~I," prefixes (three sites).
4. `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:121`: "Volume~I," prefix.
5. `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1679`: "Volume~I," prefix in clause IV of theorem statement + `rem:thqg-IV-four-facets-attribution` inserted immediately after `\end{theorem}` at line ~1682. The new remark explicitly declares the theorem imports Vol~I input and does not reprove the Lagrangian statement.

## PE-7 / PE-8 template fills

### PE-7 label creation (new remark)

- environment: remark
- label: `\label{rem:thqg-IV-four-facets-attribution}` in `thqg_gravitational_s_duality.tex`
- prefix match (AP125): `rem:` -> remark: Y
- grep across three volumes for `rem:thqg-IV-four-facets-attribution`:
  Vol I: 0, Vol II: 0 (before edit), Vol III: 0; after edit: Vol II: 1. delta = 1: Y.
- verdict: ACCEPT

### PE-8 cross-volume formula (V1-thm:quantum-complementarity-main consumer)

- formula: the Lagrangian polarization `C_g(A) ≃ Q_g(A) ⊕ Q_g(A^!)` with complementarity sum.
- Vol I canonical: `higher_genus_complementarity.tex:540-609`, `\label{thm:quantum-complementarity-main}`, ClaimStatusProvedHere.
- Vol II phantomsection alias at `main.tex:809` (post-AP124 heal: singular, duplicate at :978 retired).
- Vol III: no direct consumers (checked).
- convention consistent: Y.
- AP5 propagation: Vol I canonical and Vol II consumers now carry explicit "Volume~I" attribution or blanket Remark[Attribution]; no Vol III consumers.
- verdict: ACCEPT

## AP287 post-conditions

- ProvedHere consumer `thm:thqg-IV-four-facets` now carries explicit Attribution Remark adjacent to the theorem environment, satisfying AP287 discipline (HZ-11 cross-volume attribution for cited lemma/theorem whose label lives only in Vol~I).
- All other consumer sites are either (a) prose motivational / definitional (no AP287 trigger), (b) inside blanket `rem:quantum-complementarity-vol1-attribution` chapter-level attribution at `bv_brst.tex:794-811`, or (c) already carried "Volume~I" prose prefix pre-heal.

## Commit plan (NOT executed per instructions)

Single logical commit, Vol II only:
- `main.tex` (AP124 duplicate phantom cleanup)
- 4 `chapters/connections/*.tex` files (Option A "Volume~I" prefix hygiene across 5 consumer sites)
- `thqg_gravitational_s_duality.tex` (Option B Attribution Remark for the one AP287 violation)
- this notes file at `adversarial_swarm_20260418/wave14_vol_ii_quantum_complementarity_hz11.md`

Commit message draft:
```
Vol II AP287 HZ-11 sharpening: quantum-complementarity consumer attribution
+ AP124 duplicate phantomsection cleanup
```

No Vol I edits. No compute/test changes. Hook warnings observed during edit passes (AP24, AP8, AP7/AP32, V2-AP26) are pre-existing in unrelated file regions and not introduced by this wave.

## Residuals / frontier

- One Vol~II cross-volume `\ref{V1-lem:involution-splitting}(c)` inside the Facet~IV proof body (line 1711): lemma label presumably inscribed in Vol~I higher_genus_complementarity.tex. Out of scope for this wave (V1-lem:involution-splitting is a separate HZ-11 slug).
- `V1-thm:shifted-symplectic-complementarity` (cited in `thqg_symplectic_polarization.tex:37`, `twisted_holography_quantum_gravity.tex:513,750`) is a distinct Vol~I theorem; AP287 audit for it is a separate wave.
