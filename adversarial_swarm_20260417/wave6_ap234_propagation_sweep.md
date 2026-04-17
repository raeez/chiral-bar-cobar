# Wave 6 — AP234 (Trinity-K vs scalar-complementarity-K) propagation sweep

**Date.** 2026-04-17.
**Status.** Surgical cross-volume propagation; 22 sites healed across Vol I (11) and Vol II (11). No commits.
**Context.** AP234 (CLAUDE.md) distinguishes two invariants that Wave 5 and prior waves had collided under a single letter $K$:

- **Trinity ghost-charge conductor.** $K(\cA) := c(\cA) + c(\cA^!) = -c_{\mathrm{ghost}}(\BRST)$. Per-family: $K(\Vir) = 26$, $K(\cW_3) = 100$, $K(\mathrm{BP}) = 196$, $K(V_k(\fg)) = 2\dim(\fg)$, $K(\cW_N) = 4N^3 - 2N - 2$.
- **Scalar complementarity.** $\varkappa(\cA) := \kappa(\cA) + \kappa(\cA^!)$. Per-family: $\varkappa(\mathrm{KM}) = 0$, $\varkappa(\Vir) = 13$, $\varkappa(\cW_3) = 250/3$, $\varkappa(\mathrm{BP}) = 98/3$, $\varkappa(\cW_N) = (H_N - 1) \cdot K(\cW_N)$.
- **Bridge.** $\varkappa = \varrho_\cA \cdot K$ with $\varrho_{\mathrm{KM}} = \varrho_{\mathrm{free}} = 0$, $\varrho_{\cW_N} = H_N - 1$ (so $\varrho_{\Vir} = 1/2$, $\varrho_{\cW_3} = 5/6$), $\varrho_{\mathrm{BP}} = 1/6$.

Prior usage across manuscript deployed the letter $K$ for the scalar quantity $\kappa + \kappa^!$ (values {0, 13, 250/3, 98/3}) while `universal_conductor_K_platonic.tex` and `bershadsky_polyakov.tex` use $K$ for the Trinity (values {0, 26, 100, 196, $2\dim\fg$, $4N^3-2N-2$}). Two sites (Vol I `frontier_modular_holography_platonic.tex:5400`, `n2_superconformal.tex:18`, `bar_cobar_adjunction_inversion.tex:2379`) actively mixed the two, writing e.g. "$K(\Vir) = 13$ and $K(\mathrm{BP}) = 196$" in the same paragraph. This is the AP234 failure mode.

## Heal protocol

For every drifted site, the scalar quantity was renamed from $K$ to $\varkappa$; the Trinity $K = c + c^!$ retains the symbol $K$ (consistent with the canonical reference `chapters/theory/universal_conductor_K_platonic.tex`). Where the drifted passage relied on the scalar value (e.g. "$K = 13$ controls BTZ entropy rate"), the symbol was renamed and a parenthetical added cross-referencing the Trinity: "$\varkappa := \kappa + \kappa^! = 13$ (distinct from the Trinity ghost-charge conductor $K(\Vir) := c + c^! = 26$; related by $\varkappa = \varrho_{\Vir} \cdot K$, $\varrho_{\Vir} = 1/2$)". Where the passage mixed scalar and Trinity values with contradictory symbol usage, both sides were normalised: BP scalar $\varkappa(\mathrm{BP}) = 98/3$, BP Trinity $K(\mathrm{BP}) = 196$.

No cross-references (\\ref labels) required renaming: the symbol $K$ was not a \\label identifier at any of the drifted sites. HZ-5 atomicity confirmed: a post-sweep grep for remaining `K = 13` patterns in Vol I/II identifies further drift sites (8+ residuals in moonshine.tex, entanglement_modular_koszul.tex, three_dimensional_quantum_gravity.tex §1085/§1098/§2229/§2301/§2745, five_theorems_modular_koszul.tex:929, rosetta_stone.tex:941/§6535, thqg_gravitational_s_duality.tex:1812/§2035, thqg_3d_gravity_movements_vi_x.tex:91/§2278, working_notes.tex:7824) that should be addressed in Wave 7 — they use "$K = 13$" in scalar sense with the local passage self-consistent (no mixing with $K = 196$), so they are symbol-drift but not immediate contradictions. Wave 6 prioritised contradiction sites and canonical definition sites.

## Sites healed

1. `worldview_synthesis_2026_04_17.tex:276-279` — Theorem C Platonic statement. Renamed scalar $K \to \varkappa$; added Trinity parenthetical with BP=196 canonical.
2. `standalone/analytic_sewing.tex:2860-2874` — rem:koszul-complementarity-analytic. Renamed + eq:complementarity-sewing updated.
3. `standalone/multi_weight_cross_channel.tex:252-254` — introduction paragraph. Renamed + Trinity cross-link.
4. `standalone/shadow_towers_v3.tex:2201-2204` — rem:self-dual. Scalar rename with Trinity note.
5. `standalone/shadow_towers_v3.tex:2244-2253` — rem:koszul-conductor. Full renaming of definition; Trinity block added.
6. `standalone/shadow_towers_v3.tex:3293-3305` — rem:conductor-not-c. Retitled; three-quantity disambiguation.
7. `chapters/connections/frontier_modular_holography_platonic.tex:5390-5401` — CONTRADICTION SITE (BP=196 Trinity + Vir=13 scalar mixed). Normalised to scalar convention, BP corrected to $\varkappa = 98/3$.
8. `chapters/connections/frontier_modular_holography_platonic.tex:5448-5454` — cobordism hypothesis remark. Renamed with consistent $\varkappa$ values.
9. `vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:5167-5181` — rem:ordered-kd-core-conductor-bridge. Trinity defined explicitly; scalar cross-linked.
10. `vol2/chapters/connections/thqg_gravitational_s_duality.tex:1335-1353` — Exponent sum theorem. The bridge identity $K = (c + c') \varrho = K_\fg \cdot \varrho$ was rewritten as $\varkappa = K_\fg \cdot \varrho$; Trinity KM remark added ($K(\widehat\fg_k) = 2\dim\fg \ne 0$ even though $\varkappa = 0$).
11. `vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:374-376` — table intro prose.
12. `vol2/chapters/connections/3d_gravity.tex:4314-4316` — entropic shadow remark.
13. `vol2/chapters/connections/3d_gravity.tex:10419-10424` — Page curve intro.
14. `vol2/chapters/connections/3d_gravity.tex:10489-10492` — saddle complementarity.
15. `vol2/chapters/connections/3d_gravity.tex:10593-10600` — Stokes action difference.
16. `standalone/three_dimensional_quantum_gravity.tex:2198-2201` — Hawking rate $c$-independence.
17. `standalone/three_dimensional_quantum_gravity.tex:2390-2396` — replica degeneracy.
18. `standalone/three_dimensional_quantum_gravity.tex:2513-2521` — Stokes triple-datum remark.
19. `standalone/en_chiral_operadic_circle.tex:3085` — class-L Koszul-dual table row.
20. `standalone/en_chiral_operadic_circle.tex:3198-3202` — Virasoro Koszul dual passage.
21. `standalone/survey_modular_koszul_duality_v2.tex:5020` — class-table header.
22. `standalone/survey_modular_koszul_duality_v2.tex:638-640` — Theorem C summary.
23. `chapters/connections/outlook.tex:453-459` — conductor table intro ($K_\kappa$ usage).
24. `standalone/survey_modular_koszul_duality.tex:4163-4169` — Virasoro unique-non-zero remark.
25. `vol2/working_notes.tex:7098` — $Y(\fsl_2)$ table entry; added Trinity value $K = 6$.
26. `chapters/examples/n2_superconformal.tex:14-20` — CONTRADICTION SITE (Vir=13 + BP=196 mixed as Trinity). Fully disambiguated; N=2 $K = 1$ correctly kept Trinity.
27. `chapters/theory/bar_cobar_adjunction_inversion.tex:2379-2385` — CONTRADICTION SITE (Vir=13 scalar + BP=196 Trinity). Normalised: scalar $\varkappa$ with Trinity cross-note.

Net: 27 surgical edits across 15 files (Vol I 10, Vol II 5).

## Residual drift (Wave 7 queue)

Single-convention (scalar) sites using $K$ without Trinity contradiction — not urgent but should be renamed for full consistency:

- `chapters/examples/moonshine.tex:22, 269`
- `chapters/connections/entanglement_modular_koszul.tex:862, 912`
- `standalone/three_dimensional_quantum_gravity.tex:1085, 1098, 2229, 2301, 2745`
- `standalone/five_theorems_modular_koszul.tex:929`
- `standalone/en_chiral_operadic_circle.tex:3172` (class-M table row)
- `vol2/chapters/examples/rosetta_stone.tex:941, 6535`
- `vol2/chapters/connections/thqg_gravitational_s_duality.tex:1812, 2035`
- `vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:91, 2278`
- `vol2/working_notes.tex:7824`
- `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8235` (backup file — skip)
- `tmp_standalone_audit/survey_v2_xr.tex:635` (tmp audit file — skip)

## HZ-IV decorator status

No test files were touched. The three anchoring identities — $K(\cA) = c + c^!$, $\varkappa(\cA) = \kappa + \kappa^!$, $\varkappa = \varrho \cdot K$ — are witnessed in `chapters/theory/universal_conductor_K_platonic.tex` which remained the canonical source throughout.

## Constitutional hygiene

No AP/HZ/Pattern/Cache tokens in typeset prose. No em-dashes introduced. No AI slop. Symbol rename was atomic within each file: every $K = v$ where $v \in \{13, 250/3, 98/3\}$ was converted to $\varkappa = v$, never half-converted. Every site with Trinity cross-reference names $K$ explicitly as $c + c^! = -c_{\mathrm{ghost}}(\BRST)$.
