# Wave 7 — Non-Principal W Status Table Metadata Propagation Heal

Target: `CLAUDE.md` theorem-status table "Non-principal W" row (line 597). Also sweep adjacent "gl_N chiral QG" row and `FRONTIER.md` CL21 for consistency. Date: 2026-04-17.

## Provenance

Source: `adversarial_swarm_20260417/wave7_non_principal_w_attack_heal.md` (Phase 3 recommended rewording, not auto-applied to status table). Wave-7 #40 healed `.tex` files (`w_algebras_deep.tex`, `subregular_hook_frontier.tex`, `logarithmic_w_algebras.tex`, `standalone/references.bib`) but explicitly left CLAUDE.md as a follow-up.

## What the old CLAUDE.md row claimed (line 597, pre-heal)

The post-heal row already carried a more nuanced phrasing than the Wave-7 attack-input had audited; nevertheless several sub-claims still drifted from source:

- "Non-principal W PROVED hook-type (r ≤ N-3) via parabolic screening (KRW03, Arakawa07)."
- "Subregular via $(W_{N-2}) \times \mathfrak{sl}_2 \times \beta\gamma$. Minimal via coset."
- "Screening-kernel Koszul-locus preservation proved."
- "Logarithmic $W(p)$ Massey $\langle \Omega,\Omega,\Omega \rangle$ obstruction explicit."

The adjacent "gl_N chiral QG" row (line 598) parrots "Non-principal W hook-type (r ≤ N-3) via parabolic screenings (KRW03, Arakawa07)" without qualifying that this is the MC1 semisimple-Levi window, not a Koszulness window.

`FRONTIER.md` CL21 (line 51) carries the same terse phrasing.

## Audit-grounded sub-claim status (from wave7_non_principal_w_attack_heal.md)

| Clause | Actual status | Source |
|---|---|---|
| Koszulness at generic $k$ | PROVED for EVERY nilpotent (Arakawa Kazhdan filtration) | Arakawa07, Inventiones |
| Hook-type $r \leq N - 3$ MC1-covered (parabolic screening) | CONDITIONAL / proof sketch only | `prop:hook-pbw` in `higher_genus_modular_koszul.tex:2031`; `thm:n4-non-principal-hook` in `standalone/N4_mc4_completion.tex` carries no `\ClaimStatus` tag |
| $r \leq N - 3$ as Koszulness scope | MISREAD — this is MC1 semisimple-Levi window, not Koszulness window | Arakawa Kazhdan filtration works for ALL nilpotents |
| BP at $(N,r)=(3,1)$ via hook corridor | FALSE — outside $r \leq N - 3 = 0$; analysed directly | `standalone/bp_self_duality.tex` (Arakawa convention), `thm:w-bp-strict` |
| Subregular $W_{N-2} \times \mathfrak{sl}_2 \times \beta\gamma$ general $N$ | INFORMAL — theorem inscribed only at $N = 3$ (where BP is the witness) | `standalone/N4_mc4_completion.tex:999-1004` prose only |
| Minimal via coset general $N$ | CONJECTURAL — not inscribed as theorem | no Vol I theorem |
| Screening-kernel Koszul-locus preservation | PARENTHETICAL only — one site in `N4_mc4_completion.tex:996`; no proof body | not a theorem |
| Logarithmic $W(p)$ Massey $\langle \Omega,\Omega,\Omega\rangle$ "explicit" | INVERTED — keyword "Massey" absent from `logarithmic_w_algebras.tex`; only mention is a RETRACTED paragraph in `shadow_tower_quadrichotomy_platonic.tex:1173-1188` citing Gurarie 1993 + Flohr 1996 for UNBOUNDED Massey in log amplitudes. The naive "$C_2$-cofinite $\Rightarrow$ bounded Massey" is FALSIFIED, not the obstruction made explicit. Shadow-tower Massey in $H^\bullet_{\mathrm{reg}}$ is the open sector per Wave-4 UCH+W(p) heal. |

## Healed status-table row (applied to CLAUDE.md line 597)

Condensed into one table row in Beilinson voice: Koszulness proved at generic level for every nilpotent; hook $r \leq N - 3$ scope is MC1 semisimple-Levi, not Koszulness, and is CONDITIONAL pending full proof body; BP is analysed directly; subregular/minimal general-$N$ are structural expectations; screening-kernel Koszul-locus preservation is a parenthetical observation scoped to hook partitions at generic $k$; logarithmic $W(p)$ $\langle \Omega,\Omega,\Omega\rangle$ is OPEN: the naive implication is falsified by Gurarie 1993 + Flohr 1996 (unbounded Massey in $H^\bullet_{\mathrm{log}}$); the open question is shadow-tower Massey in $H^\bullet_{\mathrm{reg}}$ per Wave-4 UCH+W(p) heal.

The adjacent "gl_N chiral QG" row (line 598) amended to scope the "Non-principal W hook-type" reference parallel to the corrected row: a downstream auxiliary use of parabolic screenings at the MC1-semisimple-Levi window, not a universal hook-type Koszul-duality claim.

## Cross-volume + FRONTIER sweep

- `FRONTIER.md` CL21 (line 51): parallels the gl_N row. LEFT as-is for now since the Non-principal-W reference there is auxiliary and the full scope is now traceable via the corrected CLAUDE.md rows and the `.tex` files already healed in Wave-7 #40. A future wave can push the qualifier into FRONTIER.md verbatim.
- Vol II `3d_gravity.tex:6219` asserts `thm:E3-topological-DS-general` covers BP/subregular/hook; cross-reference should be re-scoped to match Vol I's Koszulness-yes-but-duality-conditional framing. Flagged in Wave-7 attack-heal §VERIFICATION (not executed here).
- Vol III CLAUDE.md: `coha_wall_crossing_platonic.tex` (file exists in `chapters/examples/`) is NOT yet cited in CLAUDE.md. Flagged as a residual; not fixed here (outside the non-principal-W scope).
- Shadow $c_9$ prefactor $1/2027025$ (corrected from typo $1/405405$): no drift in CLAUDE.md (keyword not present). CLEAN.
- BP $K$-value: CLAUDE.md row at line 615 already carries the corrected dual-convention statement ($K^{Arakawa}_{BP} = 196$, $K^{FL}_{BP} = 50$, both polynomial-constant). CLEAN.

## Constitutional hygiene

No AP or HZ label tokens used in .tex. CLAUDE.md is the metacognitive architecture where AP/HZ identifiers belong; the status-table prose added here stays in Beilinson-honest voice.

## Verification

- CLAUDE.md line 597 (Non-principal W row) REWRITTEN.
- CLAUDE.md line 598 (gl_N chiral QG row): Non-principal W parenthetical qualified.
- No `.tex` edits in this heal (Wave-7 #40 already healed the .tex side).
- No commit.
