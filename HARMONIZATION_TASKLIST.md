# HARMONIZATION TASKLIST — Full Manuscript Audit
# Generated: 2026-03-17
# Volumes: I (~/chiral-bar-cobar) + II (~/chiral-bar-cobar-vol2) + MD (control plane)
# Oracle: concordance.tex + editorial_constitution.tex + CLAUDE.md + MEMORY.md

## Oracle Digest — Canonical Status (from concordance.tex as of 2026-03-17)

### Five Main Theorems: ALL PROVED (A/B/C/D/H)
### MC Frontier:
- MC1: PROVED (PBW concentration, all standard families)
- MC2: PROVED (bar-intrinsic, thm:mc2-bar-intrinsic; thm:recursive-existence)
- MC3: PROVED in type A (thm:mc3-type-a-resolution); arbitrary type CONJECTURAL (conj:mc3-arbitrary-type)
- MC4: PROVED (strong completion towers, thm:completed-bar-cobar-strong; MC4+ unconditional, MC4^0 reduced to finite-dim)
- MC5: Genus ≤1 PROVED; genus ≥2 requires Costello renormalization

### Shadow Tower:
- Finite-order Θ_A^{≤r}: PROVED for all r (bar-intrinsic)
- Full Θ_A: PROVED at convolution level (thm:mc2-bar-intrinsic)
- D²=0 at convolution level: PROVED (thm:convolution-d-squared-zero)
- D²=0 at ambient level: PROVED (thm:ambient-d-squared-zero, via Mok log FM)

### Identification Theorems: 11 total (upgraded from 7 in CLAUDE.md)
- (1)-(6): proved; (7): structural obstruction (RNW19); (8)-(11): proved via three pillars

### Critical CLAUDE.md Drift Found During Oracle Build:
- CLAUDE.md:55 says "Seven identification theorems (all 7 proved)" → concordance says 11 (6 proved + obstruction + 4 new from pillars)
- CLAUDE.md:120 ambient D²=0 — ALREADY CORRECTED to PROVED ✓
- CLAUDE.md:41 Ring 1 says MC4 proved via "W_N rigidity" only → should also cite strong completion towers (thm:completed-bar-cobar-strong)
- CLAUDE.md:7 appendix structure says "3 clusters" → now 4 clusters (A-D) per main.tex
- CLAUDE.md:5 says "finite-order nonlinear shadow calculus" → full Θ_A now proved, not just finite-order

---

## PHASE 1: Delta Propagation Sweep

### Δ1 — MC2 Closure Propagation (10 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0001 | 1 | STALE-PROSE | I | main.tex:632-633 | Change "whose conjectural all-arity limit is a universal element" → "whose all-arity limit, proved by Theorem thm:mc2-bar-intrinsic, is the universal element" | thm:mc2-bar-intrinsic |
| H0002 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:73 | Delete "the unrestricted all-genera modular envelope that the tower conjecturally converges to is not yet established in general"; replace with ref to thm:mc2-bar-intrinsic | thm:mc2-bar-intrinsic |
| H0003 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:2178 | Change "if the full universal class Θ_A exists" → "since Θ_A exists (Theorem thm:mc2-bar-intrinsic)" | thm:mc2-bar-intrinsic |
| H0004 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:2191 | Change "The full foundational task remains: construct Θ_A globally" → "Θ_A is constructed (thm:mc2-bar-intrinsic); what remains is clutching/Verdier compatibilities" | thm:mc2-bar-intrinsic |
| H0005 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:3019 | Change "if the full universal class Θ_A exists" → "since Θ_A exists (Theorem thm:mc2-bar-intrinsic)" | thm:mc2-bar-intrinsic |
| H0006 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:3067-3068 | Change "The full foundational task remains: construct Θ_A globally" → "Θ_A is constructed; remaining task is clutching/Verdier compatibilities" | thm:mc2-bar-intrinsic |
| H0007 | 1 | DEF-DRIFT | I | chapters/connections/editorial_constitution.tex:262-263 | Remove "and simple Lie symmetry" from hypothesis; MC2 holds for all modular Koszul algebras without Lie symmetry restriction | thm:mc2-bar-intrinsic |
| H0008 | 1 | DEF-DRIFT | I | chapters/connections/editorial_constitution.tex:2376-2380 | Remove "If, in addition, A has simple Lie symmetry and non-degenerate invariant form" condition; Θ_A exists for all modular Koszul A | thm:mc2-bar-intrinsic |
| H0009 | 1 | STALE-PROSE | I | chapters/connections/genus_complete.tex:1131-1132 | Change "proved constructively, conjectural as r→∞" → "proved constructively; all-arity limit exists by thm:mc2-bar-intrinsic" | thm:mc2-bar-intrinsic |
| H0010 | 1 | STALE-PROSE | I | chapters/theory/introduction.tex:2054 | Change "MC1 and MC2 proved at finite order" → "MC1 and MC2 proved" (MC2 is fully proved, not just finite order) | thm:mc2-bar-intrinsic |

### Δ2 — MC3 Type A Propagation (11 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0011 | 1 | STALE-PROSE | I | main.tex:1161 | Change "conjectural stratification MC3/MC4/MC5" → "partially resolved stratification" noting MC3 type A proved, MC4 proved | thm:mc3-type-a-resolution |
| H0012 | 1 | STALE-PROSE | I | appendices/nilpotent_completion.tex:995 | Add "(MC3 proved in type A; MC4 proved)" after "MC3 ⇒ MC4 ⇒ MC5 remains inviolable" | thm:mc3-type-a-resolution |
| H0013 | 1 | STALE-PROSE | I | chapters/connections/concordance.tex:1190-1195 | MC3 bullet says "categorical splitting awaits"; add "MC3 proved in type A (thm:mc3-type-a-resolution); beyond type A awaits..." | thm:mc3-type-a-resolution |
| H0014 | 1 | STALE-PROSE | I | chapters/theory/chiral_modules.tex:49 | Add "(proved in type A; conjectural beyond)" after "MC3 extension problem" | thm:mc3-type-a-resolution |
| H0015 | 1 | STALE-PROSE | I | chapters/examples/yangians_computations.tex:1397 | Change bare "(MC3)" → "(MC3, proved in type A)" in both DK-4 and DK-5 references | thm:mc3-type-a-resolution |
| H0016 | 1 | STALE-PROSE | I | chapters/examples/yangians_computations.tex:2964 | Add "beyond type A" after "remaining MC3 open problem" | thm:mc3-type-a-resolution |
| H0017 | 1 | STALE-PROSE | I | chapters/connections/editorial_constitution.tex:2430 | Add "(proved in type A; open beyond)" after "MC3 beyond the evaluation-generated core" | thm:mc3-type-a-resolution |
| H0018 | 1 | XVOL-SYNC | II | concordance.tex:132 | Change "MC3 (DK extension)" → "MC3 (DK extension; type A proved)" | thm:mc3-type-a-resolution |
| H0019 | 1 | XVOL-SYNC | II | concordance.tex:441 | Change "Would advance MC3. Status: Open." → add "(proved in type A; open beyond)" | thm:mc3-type-a-resolution |
| H0020 | 1 | XVOL-SYNC | II | conclusion.tex:86 | Add "(proved in type A; open beyond)" after "MC3 programme" | thm:mc3-type-a-resolution |
| H0021 | 1 | XVOL-SYNC | II | spectral-braiding.tex:1044 | Add "(proved in type A)" after "full DK ladder (MC3)" | thm:mc3-type-a-resolution |

### Δ4 — Shadow Tower Level Boundary (15 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0022 | 1 | STALE-PROSE | I | main.tex:632 | Change "conjectural all-arity limit" → "proved all-arity limit" (duplicate of H0001, keep most specific) | thm:mc2-bar-intrinsic |
| H0023 | 1 | STATUS-UP | I | chapters/connections/editorial_constitution.tex:102-109 | Remove ambient D²=0 from "remaining conjectural items" list; it is now PROVED (thm:ambient-d-squared-zero via Mok) | thm:ambient-d-squared-zero |
| H0024 | 1 | STATUS-LEVEL | I | chapters/connections/genus_complete.tex:198 | Add "(now proved)" to parenthetical about ambient D²=0; currently reads as uncertain | thm:ambient-d-squared-zero |
| H0025 | 1 | STALE-PROSE | I | chapters/theory/higher_genus_modular_koszul.tex:7946 | Change "The conjecture that D²=0 at ambient level" → "The theorem that D²=0 at ambient level" | thm:ambient-d-squared-zero |
| H0026 | 1 | STATUS-UP | I | chapters/connections/concordance.tex:1072 | Change "conjectural at all arities" → "proved at all arities" for master MC equation | thm:mc2-bar-intrinsic |
| H0027 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:569 | Change "should globalize...Before that globalization is completed" → "globalizes (thm:mc2-bar-intrinsic)" | thm:mc2-bar-intrinsic |
| H0028 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:2197 | Rewrite to acknowledge proved existence of Θ_A; remaining task is enhanced carrier identification | thm:mc2-bar-intrinsic |
| H0029 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:2257 | Change "raw conjecture 'construct Θ_A'" → "raw question 'characterize Θ_A'" (existence no longer conjectural) | thm:mc2-bar-intrinsic |
| H0030 | 1 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:598 | Add note that full MC class exists by thm:mc2-bar-intrinsic (not just "visible arity-≤4 face") | thm:mc2-bar-intrinsic |
| H0031 | 1 | XVOL-SYNC | II | fm3_planted_forest_synthesis.tex:75 | Rewrite "D²=0 (at convolution level; at ambient level, Theorem...)" → "D²=0 at both levels (both proved)" | thm:ambient-d-squared-zero |


### Direct Oracle Findings — CLAUDE.md Drift (5 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0032 | 5 | SCAFFOLD | MD | CLAUDE.md:55 | Change "Seven identification theorems (all 7 proved)" → "Eleven identification theorems (6 proved + structural obstruction + 4 pillar-derived)" with items (8)-(11) | concordance:rem:three-pillar-identifications |
| H0033 | 5 | SCAFFOLD | MD | CLAUDE.md:55-62 | Add identification theorems (8)-(11): Borcherds=shadow, quartic clutching via Mok, log clutching PROVED, ambient D²=0 PROVED | concordance:rem:three-pillar-identifications |
| H0034 | 5 | SCAFFOLD | MD | CLAUDE.md:41 | Ring 1: add "strong completion towers (thm:completed-bar-cobar-strong)" alongside W_N rigidity for MC4 proof | concordance:editorial_constitution:MC4 |
| H0035 | 5 | SCAFFOLD | MD | CLAUDE.md:7 | Change "3 clusters: Foundations, Nonlinear Technical, Physics Reference" → "4 clusters: A-Foundations, B-Nonlinear, C-Extended Families, D-Physics+Reference" | main.tex appendix structure |
| H0036 | 5 | SCAFFOLD | MD | CLAUDE.md:5 | Change "finite-order nonlinear shadow calculus developed through arity 4" → "nonlinear shadow calculus with full Θ_A proved (bar-intrinsic) and finite-order engine through arity 4" | thm:mc2-bar-intrinsic |


### Δ3 — MC4 Closure Propagation (29 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0037 | 1 | STALE-PROSE | I | main.tex:1161 | Change "conjectural stratification MC3/MC4/MC5" → "dependency-ordered stratification; MC1-MC4 proved" | editorial_constitution:MC-table |
| H0038 | 1 | STATUS-UP | I | chapters/examples/free_fields.tex:1614 | Virasoro/W∞ row: change ClaimStatusConjectured → ProvedElsewhere (MC4 closed) | thm:completed-bar-cobar-strong |
| H0039 | 1 | STATUS-UP | I | chapters/examples/free_fields.tex:1615 | W_N/Yangian row: change ClaimStatusConjectured → ProvedElsewhere (MC4 closed) | thm:completed-bar-cobar-strong |
| H0040 | 1 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_curved.tex:229-230 | Change "W∞ marks the locus where completed duality is still missing" → "handled by strong completion-tower theorem" | thm:completed-bar-cobar-strong |
| H0041 | 1 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_curved.tex:498 | Change "MC4 completion target" → "MC4 completion (proved)" | thm:completed-bar-cobar-strong |
| H0042 | 1 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_curved.tex:501-511 | Change "remaining MC4 problem...three obstructions remain" → structural theorem proved; H-level identification residual | thm:completed-bar-cobar-strong |
| H0043 | 1 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_curved.tex:81 | Change "MC4 completion target (W∞)" → "MC4 completion (proved)" | thm:completed-bar-cobar-strong |
| H0044 | 1 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_inversion.tex:99 | Change "MC4 completion target" → "MC4 proved" | thm:completed-bar-cobar-strong |
| H0045 | 1 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_inversion.tex:694 | Change "exact MC4 package remains open" → "MC4 proved; H-level identification is example-specific" | thm:completed-bar-cobar-strong |
| H0046 | 1 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_inversion.tex:710 | Change "treat as MC4 completion target" → "handled by MC4 completion theorem" | thm:completed-bar-cobar-strong |
| H0047 | 1 | STATUS-LEVEL | I | chapters/connections/editorial_constitution.tex:106 | conj:master-infinite-generator listed as "remaining conjectural"; MC4 structural is proved, only H-level residual | thm:completed-bar-cobar-strong |
| H0048 | 1 | STATUS-LEVEL | I | chapters/connections/editorial_constitution.tex:345-346 | Relabel conj:master-infinite-generator: MC4 proved, this is residual H-level comparison only | thm:completed-bar-cobar-strong |
| H0049 | 1 | STALE-PROSE | I | appendices/coderived_models.tex:338 | Change "(MC4: completed bar for infinite generators)" → "(MC4: proved; residual H-level comparison)" | thm:completed-bar-cobar-strong |
| H0050 | 1 | STALE-PROSE | I | chapters/theory/higher_genus_modular_koszul.tex:689 | Add "MC4 structural framework proved; H-level identification remaining" to conj:master-infinite-generator ref | thm:completed-bar-cobar-strong |
| H0051 | 1 | STALE-PROSE | I | chapters/theory/chiral_modules.tex:1976-1979 | Update MC4 ref from "delegated to W∞ MC4 package" → "MC4 proved; H-level identification residual" | thm:completed-bar-cobar-strong |
| H0052 | 1 | STALE-PROSE | I | chapters/theory/chiral_modules.tex:3792 | Change "MC4 open problem" → "MC4 proved; H-level identification is example-specific" | thm:completed-bar-cobar-strong |
| H0053 | 1 | STALE-PROSE | I | chapters/examples/landscape_census.tex:508-509 | Change "H-level remains part of MC4" → "MC4 proved; H-level target identification residual" | thm:completed-bar-cobar-strong |
| H0054 | 1 | STALE-PROSE | I | chapters/examples/landscape_census.tex:971-972 | Change "MC4 completion problem" → "MC4 proved; H-level identification residual" | thm:completed-bar-cobar-strong |
| H0055 | 1 | STALE-PROSE | I | chapters/examples/genus_expansions.tex:1845 | Add "(proved; thm:completed-bar-cobar-strong)" after "W∞ MC4 package" | thm:completed-bar-cobar-strong |
| H0056 | 1 | STALE-PROSE | I | chapters/examples/w_algebras_deep.tex:1080 | Change "live MC4 open problem" → "proved by strong completion-tower theorem" | thm:completed-bar-cobar-strong |
| H0057 | 1 | STALE-PROSE | I | chapters/examples/yangians_drinfeld_kohno.tex:556 | Change "DK-4/5: conjectural" → "DK-4: proved (MC4 closed); DK-5: conjectural" | thm:completed-bar-cobar-strong |
| H0058 | 1 | STALE-PROSE | I | chapters/examples/yangians_drinfeld_kohno.tex:987 | Change "Yangian MC4 open problem" → "MC4 residual H-level (structural proved)" | thm:completed-bar-cobar-strong |
| H0059 | 1 | STALE-PROSE | I | appendices/existence_criteria.tex:421-423 | Update: W∞ IS completed Koszul via strong completion-tower theorem | thm:completed-bar-cobar-strong |
| H0060 | 1 | XVOL-SYNC | II | holomorphic_topological.tex:117 | Change "Coefficient identities belong to MC4" → "resolved (MC4 closed)" | thm:completed-bar-cobar-strong |
| H0061 | 1 | XVOL-SYNC | II | holomorphic_topological.tex:378 | Change "MC4/MC5" → "MC4 proved; closed-string belongs to MC5" | thm:completed-bar-cobar-strong |
| H0062 | 1 | XVOL-SYNC | II | holomorphic_topological.tex:781 | Change "Remaining coefficient identities belong to MC4" → "MC4 resolved" | thm:completed-bar-cobar-strong |

### Δ5 — Three-Pillar Integration (14 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0063 | 1 | STALE-PROSE | I | chapters/theory/introduction.tex:1420 | Change "Seven identification theorems" → "Eleven identification theorems" | concordance:rem:three-pillar-identifications |
| H0064 | 1 | XREF-STALE | I | chapters/theory/introduction.tex:1421 | Rename label subsec:seven-identifications → subsec:eleven-identifications | concordance:1092 |
| H0065 | 1 | STALE-PROSE | I | chapters/theory/introduction.tex:1424 | Change "seven identification theorems, five proved and two structural" → "eleven identification theorems" | concordance:1092 |
| H0066 | 1 | STALE-PROSE | I | chapters/theory/introduction.tex:1425-1433 | Add items (8)-(11): Borcherds=shadow, quartic clutching via Mok, log clutching proved, ambient D²=0 proved | concordance:1117-1143 |
| H0067 | 1 | STALE-PROSE | I | chapters/theory/higher_genus_modular_koszul.tex:7946 | Change "The conjecture that D²=0" → "The theorem that D²=0" (line 7950 already says "now proved") | thm:ambient-d-squared-zero |
| H0068 | 1 | XREF-BROKEN | I | chapters/theory/chiral_modules.tex:4479 | Add \cite{Mok25} after "logarithmic FM compactification" | Mok25:Pillar-C |
| H0069 | 1 | STATUS-LEVEL | I | chapters/connections/genus_complete.tex:198 | Add "(now proved)" to parenthetical about ambient D²=0 at conj:differential-square-zero ref | thm:ambient-d-squared-zero |
| H0070 | 1 | XREF-BROKEN | II | affine_half_space_bv.tex:632 | Add \cite{Mok25} after "logarithmic FM compactification" | Mok25:Pillar-C |
| H0071 | 1 | XREF-BROKEN | II | fm3_planted_forest_synthesis.tex:307 | Add \cite{Mok25} — file uses planted forests throughout without citing Mok25 | Mok25:Pillar-C |
| H0072 | 1 | XREF-STALE | II | conclusion.tex:196 | Change informal "(cf. Mok)" → proper \cite{Mok25} | Mok25:Pillar-C |
| H0073 | 1 | XREF-BROKEN | II | log_ht_monodromy.tex:1148 | Add \cite{Mok25} after "logarithmic FM spaces" | Mok25:Pillar-C |
| H0074 | 1 | XREF-BROKEN | II | log_ht_monodromy.tex:1220 | Add \cite{Mok25} after "logarithmic FM spaces" | Mok25:Pillar-C |
| H0075 | 1 | XREF-STALE | II | hochschild.tex:815-819 | Add cross-ref to identification (8): F_n = o_n (shadow tower obstruction) | concordance:1117 |
| H0076 | 1 | XREF-STALE | II | pva-descent.tex:788-803 | Add cross-ref to identification (8): F_n = o_n | concordance:1117 |

### Δ6 — Homotopy Refoundation (12 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0077 | 1 | DEF-DRIFT | I | chapters/examples/yangians_drinfeld_kohno.tex:5468 | Add "(strict model; Convention rem:two-level-convention)" after "dg Lie algebra" in def:modular-yangian-pro | rem:two-level-convention |
| H0078 | 1 | DEF-DRIFT | I | appendices/koszul_reference.tex:158 | Add "in the L∞ MC ∞-groupoid" after "gauge equivalence" for MC moduli | rem:two-level-convention |
| H0079 | 1 | DEF-DRIFT | I | chapters/examples/deformation_quantization.tex:133 | Add "(gauge equivalence in Conv_∞)" after "canonical up to gauge equivalence" | rem:two-level-convention |
| H0080 | 1 | DEF-DRIFT | I | chapters/examples/deformation_quantization_examples.tex:123 | Add "(in L∞ MC groupoid)" after "unique up to gauge equivalence" | rem:two-level-convention |
| H0081 | 1 | DEF-DRIFT | I | chapters/theory/bar_cobar_adjunction_inversion.tex:4092-4102 | Add "Both are strict models; comparison Φ_* is L∞ morphism" to rem:cech-modular-parallel | rem:two-level-convention |
| H0082 | 1 | DEF-DRIFT | I | chapters/theory/cobar_construction.tex:1918 | Add "(gauge equivalence in L∞ sense)" for curved deformation gauge equivalence | rem:two-level-convention |
| H0083 | 1 | DEF-DRIFT | I | chapters/theory/bar_cobar_adjunction_inversion.tex:3128 | Add "(L∞ gauge equivalence)" for flat-connection gauge on contractible base | rem:two-level-convention |
| H0084 | 1 | DEF-DRIFT | II | examples-worked.tex:409-417 | Add "(strict model; gauge equivalence in Conv_∞)" for MC gauge in g^amb | conv:vol2-strict-models |
| H0085 | 1 | DEF-DRIFT | II | examples-complete.tex:927-930 | Add strict-model/L∞ annotation for Seiberg duality MC gauge equivalence | conv:vol2-strict-models |
| H0086 | 1 | DEF-DRIFT | I | chapters/theory/higher_genus_modular_koszul.tex:9179 | Rewrite "HTT for the dg Lie algebra" → "HTT applied to strict model (producing transferred L∞ on shadow algebra)" | rem:two-level-convention |
| H0087 | 1 | DEF-DRIFT | II | fm3_planted_forest_synthesis.tex:212-216 | Add "(strict model)" after "dg Lie algebra" in semicosimplicial residue passage | conv:vol2-strict-models |
| H0088 | 1 | DEF-DRIFT | I | appendices/homotopy_transfer.tex:461 | Add "bar-cobar as quantum L∞ functor (Remark rem:full-homotopy-why)" to prop:transfer-bar proof | rem:two-level-convention |

### Δ7 — W∞ Scalar Saturation (12 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0089 | 1 | STALE-PROSE | I | chapters/examples/yangians_computations.tex:1397 | Change "MC4 closed via W_N rigidity" → "MC4 closed; strong completion towers + W_N coefficient identification" | thm:completed-bar-cobar-strong |
| H0090 | 1 | STALE-PROSE | I | chapters/connections/editorial_constitution.tex:516-519 | Add "within the strong completion-tower framework (thm:completed-bar-cobar-strong)" to W_N rigidity passage | thm:completed-bar-cobar-strong |
| H0091 | 1 | STALE-PROSE | I | chapters/connections/editorial_constitution.tex:828-836 | Note thm:c334 gives explicit c₃₃₄² and prop:gram-wt4 gives weight-4 Gram matrix | thm:c334, prop:gram-wt4 |
| H0092 | 1 | STALE-PROSE | I | chapters/examples/w_algebras_deep.tex:33-34 | Add citation to strong completion-tower theorem alongside W_N rigidity | thm:completed-bar-cobar-strong |
| H0093 | 1 | STALE-PROSE | I | chapters/examples/yangians_drinfeld_kohno.tex:4306-4309 | Add strong completion towers citation alongside W_N rigidity | thm:completed-bar-cobar-strong |
| H0094 | 1 | STALE-PROSE | I | chapters/examples/yangians_drinfeld_kohno.tex:1158 | Add "(strong completion towers)" to "Proved (MC4 closed)" in DK table | thm:completed-bar-cobar-strong |
| H0095 | 1 | STALE-PROSE | I | chapters/examples/free_fields.tex:1654 | Distinguish coefficient identification (W_N rigidity) from structural proof (completion towers) | thm:completed-bar-cobar-strong |
| H0096 | 1 | STALE-PROSE | I | chapters/examples/genus_expansions.tex:2272-2277 | Stage-4 is fully resolved; cite thm:c334 and prop:gram-wt4 for explicit formulas | thm:c334 |
| H0097 | 1 | STALE-PROSE | I | chapters/examples/landscape_census.tex:255-262 | Add structural MC4 proof citation alongside W_N rigidity | thm:completed-bar-cobar-strong |
| H0098 | 1 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_curved.tex:2930-2935 | Add "within strong completion-tower framework" to W_N rigidity passage | thm:completed-bar-cobar-strong |
| H0099 | 1 | STATUS-LEVEL | I | chapters/theory/higher_genus_modular_koszul.tex:2589-2591 | Note W∞ scalar saturation proved (thm:winfty-scalar); conditional scope narrowed to non-Lie-theoretic VOAs | thm:winfty-scalar |
| H0100 | 1 | XVOL-SYNC | II | w-algebras.tex:965 | Cite explicit c₃₃₄² formula from Vol I (thm:c334) for structure constant reference | thm:c334 |

### Δ8 — Frontier File Restoration (15 items, excluding OK)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0101 | 1 | STATUS-LEVEL | I | chapters/connections/frontier_modular_holography_platonic.tex:1022 | Split conj: Θ_A existence is PROVED (thm:mc2-bar-intrinsic); only bulk realization is conjectural | thm:mc2-bar-intrinsic |
| H0102 | 1 | STALE-PROSE | I | chapters/connections/frontier_modular_holography_platonic.tex:1039 | Add "(already proved, thm:mc2-bar-intrinsic)" after "universal MC element Θ_A" | thm:mc2-bar-intrinsic |
| H0103 | 1 | STATUS-LEVEL | I | chapters/connections/frontier_modular_holography_platonic.tex:1089 | Note in def:holographic-modular-koszul-datum that Θ_A is proved; only HT realization is conjectural | thm:mc2-bar-intrinsic |
| H0104 | 1 | STATUS-DOWN | I | chapters/connections/frontier_modular_holography_platonic.tex:1155 | Split def:modular-shadow-connection: genus-0 version is proved, only higher-genus conjectural | frontier_modular_holography:1155 |
| H0105 | 1 | STALE-PROSE | I | chapters/connections/frontier_modular_holography_platonic.tex:1301 | Note bar-intrinsic construction bypasses constructive tower approach; update conj:quartic-resonance-obstruction | thm:mc2-bar-intrinsic |
| H0106 | 1 | STATUS-DOWN | I | chapters/connections/frontier_modular_holography_platonic.tex:1902 | Narrow ClaimStatusConjectured on def:envelope-shadow-functor: genus-0 is well-defined, conjectural part is modular extension | thm:mc2-bar-intrinsic |
| H0107 | 1 | STALE-PROSE | I | chapters/connections/frontier_modular_holography_platonic.tex:1420 | Note Θ_A (all orders) already proved; constructive approach is computational, not foundational | thm:mc2-bar-intrinsic |
| H0108 | 1 | STALE-PROSE | I | chapters/connections/semistrict_modular_higher_spin_w3.tex:49 | Change "does not claim full H-level construction of Θ_A" → Θ_A IS proved (thm:mc2-bar-intrinsic); reframe scope | thm:mc2-bar-intrinsic |
| H0109 | 1 | STALE-PROSE | I | appendices/typeA_baxter_rees_theta.tex:5-7 | Change "sharpens MC4 and DK frontier" → "records weightwise formalism used in MC4 proof and DK frontier" | MC4:proved |
| H0110 | 1 | STALE-PROSE | I | appendices/typeA_baxter_rees_theta.tex:10 | Add note that "weightwise MC4" is now part of the proved MC4 closure | MC4:proved |
| H0111 | 1 | STALE-PROSE | I | appendices/typeA_baxter_rees_theta.tex:23 | Change "should be posed" → "was posed and is now proved" | MC4:proved |
| H0112 | 1 | STALE-PROSE | I | appendices/typeA_baxter_rees_theta.tex:442 | Add note that MC4 is resolved via this weightwise approach | MC4:proved |
| H0113 | 1 | STALE-PROSE | I | appendices/typeA_baxter_rees_theta.tex:468-469 | Update rem:correct-form-of-MC4 to past tense: insight is part of proved MC4 | MC4:proved |


---

## PHASE 5: Control Plane Audit (73 items)

### CLAUDE.md (5 items — see H0032-H0036 above)

### README.md (20 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0114 | 5 | SCAFFOLD | MD | README.md:16 | Update badge "pages-1767" → ~2,200 | MEMORY.md:13 |
| H0115 | 5 | SCAFFOLD | MD | README.md:17 | Update badge "theorems proved-1217" → current census count | generate_metadata.py |
| H0116 | 5 | SCAFFOLD | MD | README.md:18 | Update badge "tests-8071" → ~8,100+ | MEMORY.md |
| H0117 | 5 | SCAFFOLD | MD | README.md:23-26 | Update claim counts (PH/PE/CJ/HE) to current census | generate_metadata.py |
| H0118 | 5 | SCAFFOLD | MD | README.md:42 | Change "MC4 fully closed via W_N rigidity" → "MC4 PROVED via strong completion towers" | thm:completed-bar-cobar-strong |
| H0119 | 5 | SCAFFOLD | MD | README.md:113 | Update "1,513 proved claims" to current count | generate_metadata.py |
| H0120 | 5 | SCAFFOLD | MD | README.md:117 | Update "128 precisely scoped conjectures" to current count | generate_metadata.py |
| H0121 | 5 | SCAFFOLD | MD | README.md:130 | Change MC4 "M-level proved; algebraic identification open" → "MC4 PROVED" | thm:completed-bar-cobar-strong |
| H0122 | 5 | SCAFFOLD | MD | README.md:224 | Update "1,698 pages" → ~2,200 | manuscript build |
| H0123 | 5 | SCAFFOLD | MD | README.md:253-254 | Update "102 library modules" → 130+; "110 test files" → 151+; "7,785 tests" → 8,000+ | compute_modules.md |
| H0124 | 5 | SCAFFOLD | MD | README.md:306-318 | Update file table: old names (kac_moody_framework, w_algebras_framework, detailed_computations, examples_summary, deformation_examples, yangians) → new names per CLAUDE.md rename table | CLAUDE.md:rename-table |
| H0125 | 5 | SCAFFOLD | MD | README.md:387-388 | Update "7,785 tests" → 8,000+ | make test |
| H0126 | 5 | SCAFFOLD | MD | README.md:597-603 | Update claim status count table to current census | generate_metadata.py |
| H0127 | 5 | SCAFFOLD | MD | README.md:624 | Update footer "1,698 pages...7,785 tests" → current | manuscript build |

### Memory Files (25 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0128 | 5 | SCAFFOLD | MD | memory/raeeznotes76_reorientation.md:17 | Change "ambient D²=0 CONJECTURAL" → "PROVED (thm:ambient-d-squared-zero)" | concordance:1136-1143 |
| H0129 | 5 | SCAFFOLD | MD | memory/raeeznotes76_reorientation.md:21 | Change "MC2 PROVED AT FINITE ORDER" → "MC2 PROVED (full Θ_A, thm:mc2-bar-intrinsic)" | thm:mc2-bar-intrinsic |
| H0130 | 5 | SCAFFOLD | MD | memory/raeeznotes76_reorientation.md:24 | Change "full Θ_A explicitly conjectural" → "full Θ_A PROVED" | thm:mc2-bar-intrinsic |
| H0131 | 5 | SCAFFOLD | MD | memory/raeeznotes76_reorientation.md:28-33 | Update "How to apply" section: Θ_A is proved, not "the target" | thm:mc2-bar-intrinsic |
| H0132 | 5 | SCAFFOLD | MD | memory/master_conjecture_roadmap.md:73 | Change MC2 difficulty "VERY HIGH" → "RESOLVED" | thm:mc2-bar-intrinsic |
| H0133 | 5 | SCAFFOLD | MD | memory/master_conjecture_roadmap.md:106-121 | Add strong completion towers (thm:completed-bar-cobar-strong) to MC4 body; change "CLOSED" → "PROVED" | thm:completed-bar-cobar-strong |
| H0134 | 5 | SCAFFOLD | MD | memory/master_conjecture_roadmap.md:155 | Change "MC4 CLOSED" → "MC4 PROVED" | thm:completed-bar-cobar-strong |
| H0135 | 5 | SCAFFOLD | MD | memory/mathematical_audit_2026_03_17.md:29-30 | Change "ambient D²=0 must use conjectural language" → "ambient D²=0 PROVED" | thm:ambient-d-squared-zero |
| H0136 | 5 | SCAFFOLD | MD | memory/feedback_audit_patterns.md:14-15 | Change Rule 2 "ambient D²=0 CONJECTURAL" → "PROVED (thm:ambient-d-squared-zero)" | thm:ambient-d-squared-zero |
| H0137 | 5 | SCAFFOLD | MD | memory/feedback_audit_patterns.md:18-19 | Change Rule 3 "undecorated Θ_A is all-arity limit (conjectural)" → "PROVED" | thm:mc2-bar-intrinsic |
| H0138 | 5 | SCAFFOLD | MD | memory/mc2_closure.md:14 | Add ambient D²=0 proved (thm:ambient-d-squared-zero) alongside convolution D²=0 | thm:ambient-d-squared-zero |
| H0139 | 5 | SCAFFOLD | MD | memory/three_pillars_integration.md | Change "Seven identification theorems" → "Eleven" | concordance:1092 |
| H0140 | 5 | SCAFFOLD | MD | memory/nilpotence_log_periodicity.md:147-157 | Update old file names: bar_cobar_construction→split, higher_genus→split, deformation_theory→renamed, yangians→split | CLAUDE.md:rename-table |
| H0141 | 5 | SCAFFOLD | MD | memory/raeeznotes81_campaign.md:11 | Change "Principal open target: Θ_A" → Θ_A is PROVED; reframe target | thm:mc2-bar-intrinsic |
| H0142 | 5 | SCAFFOLD | MD | memory/raeeznotes81_campaign.md:29-30 | Change "Central bottleneck: Construct Θ_A" → Θ_A is PROVED | thm:mc2-bar-intrinsic |
| H0143 | 5 | SCAFFOLD | MD | MEMORY.md:154 | Change "MC4 closed" → "MC4 proved" | thm:completed-bar-cobar-strong |
| H0144 | 5 | SCAFFOLD | MD | MEMORY.md:177 | Change "superseded by MC4 closure via W_N rigidity" → "MC4 proved via strong completion towers" | thm:completed-bar-cobar-strong |

### Notes Files (15 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0145 | 5 | SCAFFOLD | MD | notes/autonomous_state.md:10-82 | Entire file severely stale (census, page count, test count, MC frontier table all outdated); archive or regenerate | MEMORY.md |
| H0146 | 5 | SCAFFOLD | MD | notes/SESSION_PROMPT_v36.md:11 | Stale page/claim counts; archive (completed session prompt) | MEMORY.md |
| H0147 | 5 | SCAFFOLD | MD | notes/VISION.md:93-100 | MC4 described as active frontier → MC4 PROVED; remaining is example-specific | thm:completed-bar-cobar-strong |
| H0148 | 5 | SCAFFOLD | MD | notes/MASTER_PROPAGATION_TASKLIST_v44.md | 58 tasks reference old file names throughout; archive or update | CLAUDE.md:rename-table |
| H0149 | 5 | SCAFFOLD | MD | notes/STRIKE_LIST_250.md:16,58-64 | References old file names throughout; update or archive | CLAUDE.md:rename-table |
| H0150 | 5 | SCAFFOLD | MD | notes/REFORGE_MANIFEST.md | 387 findings reference old file names; update file paths | CLAUDE.md:rename-table |
| H0151 | 5 | SCAFFOLD | MD | notes/MASTER_TASK_LIST_COMPREHENSIVE.md:130,150-158 | MC4 "open frontier" → PROVED; task items D2.1-D2.10 superseded | thm:completed-bar-cobar-strong |
| H0152 | 5 | SCAFFOLD | MD | notes/RAEEZNOTES_INDEX.md | Many files marked ACTIVE that are superseded (e.g., r29 says MC2 "weaker") | mc2_closure.md |

### Metadata Files (3 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0153 | 5 | SCAFFOLD | MD | metadata/frontier_and_gaps.md:8,22-25 | MC3/MC4 framing is pre-completion-tower; update to reflect MC3 type A proved, MC4 proved | oracle |
| H0154 | 5 | SCAFFOLD | MD | metadata/reference_theorems.md:5-8 | Lists only 3 main theorems (A,B,C) → should include all 5 (A,B,C,D,H) | concordance:15-49 |
| H0155 | 5 | SCAFFOLD | MD | memory/strategic_edge_assessment.md:11,30 | MC4 "CENTRAL FRONTIER" / "MAIN BOTTLENECK" → PROVED; archive or update | thm:completed-bar-cobar-strong |

### Redundancy Items (8 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0156 | 5 | SCAFFOLD | MD | notes/MASTER_TASK_LIST_COMPREHENSIVE.md | Duplicates STRIKE_LIST + PROGRAMMES + REFORGE + PROPAGATION; archive | redundancy |
| H0157 | 5 | SCAFFOLD | MD | notes/MASTER_PROPAGATION_TASKLIST_v44.md | 58 tasks superseded by three_pillars_integration + mc2_closure + raeeznotes85; archive | redundancy |
| H0158 | 5 | SCAFFOLD | MD | notes/SESSION_PROMPT_v36.md | Completed session prompt; archive | redundancy |
| H0159 | 5 | SCAFFOLD | MD | notes/autonomous_state.md | All numbers stale; redundant with MEMORY.md; archive | redundancy |
| H0160 | 5 | SCAFFOLD | MD | memory/strategic_edge_assessment.md | MC4 "frontier" superseded by raeeznotes85_completion_closure; archive | redundancy |
| H0161 | 5 | SCAFFOLD | MD | memory/raeeznotes76_reorientation.md | Θ_A conjectural framing superseded by mc2_closure.md; archive or heavy update | redundancy |
| H0162 | 5 | SCAFFOLD | MD | notes/REFORGE_MANIFEST.md | File paths all stale (old names); needs path update if kept | redundancy |
| H0163 | 5 | SCAFFOLD | MD | notes/STRIKE_LIST_250.md | File paths partially stale; needs path update if kept | redundancy |


---

## PHASE 2: File-by-File Audit (partial — agents still returning)

### Step2-E: Connections Chapters (30 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0164 | 2 | XREF-STALE | I | chapters/connections/genus_complete.tex:198 | Update stale label conj:differential-square-zero → thm:ambient-d-squared-zero (ambient D²=0 proved) | thm:ambient-d-squared-zero |
| H0165 | 2 | STALE-PROSE | I | chapters/connections/genus_complete.tex:1131-1132 | Remove "conjectural as r→∞"; full Θ_A proved via bar-intrinsic | thm:mc2-bar-intrinsic |
| H0166 | 2 | STALE-PROSE | I | chapters/connections/genus_complete.tex:605 | Remove misleading MC2 cross-reference on non-Koszul EO recursion | thm:mc2-bar-intrinsic |
| H0167 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:773 | Remove ClaimStatusConjectured from definition env (definitions don't carry status) | style:definitions |
| H0168 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:789 | Same: remove ClaimStatusConjectured from definition | style:definitions |
| H0169 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:810 | Same: definition of modular r-matrix | style:definitions |
| H0170 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:831 | Same: definition of descendant holographic amplitudes | style:definitions |
| H0171 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:1198 | Same: sewing envelope definition | style:definitions |
| H0172 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:1244 | Same: HS-sewing condition definition | style:definitions |
| H0173 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:1286 | Same: analytic bar coalgebra definition | style:definitions |
| H0174 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:1324 | Same: analytic Koszul pair definition | style:definitions |
| H0175 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:1361 | Same: analytic shadow definition | style:definitions |
| H0176 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:1377 | Same: shadow partition function definition | style:definitions |
| H0177 | 2 | STATUS-DOWN | I | chapters/connections/genus_complete.tex:1498 | Same: analytic boundary condition definition | style:definitions |
| H0178 | 2 | STATUS-DOWN | I | chapters/connections/frontier_modular_holography_platonic.tex:1089 | Same: holographic modular Koszul datum definition | style:definitions |
| H0179 | 2 | STATUS-DOWN | I | chapters/connections/frontier_modular_holography_platonic.tex:1155 | Same: modular shadow connection definition | style:definitions |
| H0180 | 2 | STATUS-DOWN | I | chapters/connections/frontier_modular_holography_platonic.tex:1902 | Same: envelope-shadow functor definition | style:definitions |
| H0181 | 2 | STALE-PROSE | I | chapters/connections/bv_brst.tex:1075 | Add "(MC4 closed)" after "belongs to MC4" | thm:completed-bar-cobar-strong |
| H0182 | 2 | STALE-PROSE | I | chapters/connections/feynman_connection.tex:2 | Change "remains conjectural" → "proved for KM/W-algebras at genus 0; beyond that locus conjectural" | MC5:genus≤1-proved |
| H0183 | 2 | STALE-PROSE | I | chapters/connections/feynman_connection.tex:34-37 | Change "only conjecturally" → "proved at genus 0 for standard families; conjectural beyond" | MC5:genus≤1-proved |
| H0184 | 2 | STATUS-LEVEL | I | chapters/connections/kontsevich_integral.tex:397-400 | Clarify: algebraic bar-complex structure extends to all genera (proved); HT propagator comparison is the conjectural step | clarity |
| H0185 | 2 | STATUS-LEVEL | I | chapters/connections/frontier_modular_holography_platonic.tex:1022 | Clarify: Θ_A existence PROVED; bulk HT realization is what's conjectural | thm:mc2-bar-intrinsic |
| H0186 | 2 | STATUS-LEVEL | I | chapters/connections/frontier_modular_holography_platonic.tex:1301 | Quartic resonance/clutching law PROVED; isolate what remains conjectural (HT-specific) | thm:mc2-bar-intrinsic |

### Step2-B: Theory Medium+Small Files (9 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0187 | 2 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_inversion.tex:33 | Change "MC4 completion programme still under construction" → MC4 proved | thm:completed-bar-cobar-strong |
| H0188 | 2 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_inversion.tex:315 | Change "open problem is to construct filtered H-level dual" → MC4 framework proved | thm:completed-bar-cobar-strong |
| H0189 | 2 | FORMULA-FIX | I | chapters/theory/higher_genus_modular_koszul.tex:2227-2228 | κ(A)+κ(A^!)=0 cites "Theorem D(iv)" → should be "(iii)" (Duality, not Additivity) | thm-D-numbering |
| H0190 | 2 | FORMULA-FIX | I | chapters/theory/higher_genus_modular_koszul.tex:2680-2681 | Same misnumbering: "Theorem D(iv)" → "(iii)" for duality formula | thm-D-numbering |

### Step 3: Existing Audit Absorption (503 items — written to separate file)

The audit absorption agent translated 3 prior audits into 503 items:
- **248 REFORGE items** from notes/REFORGE_MANIFEST.md (387 findings → 248 rows after grouping)
- **250 STRIKE_LIST items** from notes/STRIKE_LIST_250.md (all open, none marked done)
- **5 FORMULA-FIX items** from mathematical_audit propagation check

These are written to `notes/HARMONIZED_TASKLIST.md` by the agent. Key unpropagated formula fixes:

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0191 | 3 | FORMULA-FIX | I | chapters/theory/introduction.tex:1257 | Wrong KM κ formula dim(g)/(k+h^v) → (k+h^v)·dim(g)/(2h^v) | mathematical_audit:A7 |
| H0192 | 3 | FORMULA-FIX | I | chapters/theory/koszul_pair_structure.tex:1400 | Wrong KM κ formula k·dim(g)/(2(k+h^v)) → (k+h^v)·dim(g)/(2h^v) | mathematical_audit:A7 |
| H0193 | 3 | FORMULA-FIX | I | chapters/theory/koszul_pair_structure.tex:1433 | Same wrong KM κ formula | mathematical_audit:A7 |
| H0194 | 3 | FORMULA-FIX | I | chapters/examples/free_fields.tex:3452 | Wrong KM κ formula c/(2(k+h^v)) → (k+h^v)·dim(g)/(2h^v) | mathematical_audit:A7 |
| H0195 | 3 | DEF-DRIFT | II | ht_bulk_boundary_line.tex:1804 | A^!_{M2} := Ω(B(A)) is WRONG; should be H*(B(A))^v | CLAUDE.md:pitfall-4-objects |


### Step2-C: Examples Large Files (4 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0196 | 2 | STALE-PROSE | I | chapters/examples/yangians_drinfeld_kohno.tex:987 | Change "MC4 open problem" → "MC4 problem (now closed/proved)" | thm:completed-bar-cobar-strong |
| H0197 | 2 | STATUS-ADD | I | chapters/examples/yangians_drinfeld_kohno.tex:6585 | Add \ClaimStatusProvedHere to lemma [Class-3 ordered BCH coefficient] | missing-tag |
| H0198 | 2 | STATUS-ADD | I | chapters/examples/kac_moody.tex:3800 | Add \ClaimStatusProvedHere to corollary [Bar-complex intertwining] | missing-tag |
| H0199 | 2 | FORMULA-FIX | I | chapters/examples/w_algebras.tex:1438 | Change 500/6 → 250/3 (unsimplified fraction, 2 occurrences) | consistency |

### Step2-F: Appendices + Frame (69 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0200 | 2 | STALE-PROSE | I | appendices/nonlinear_modular_shadows.tex:73 | Rewrite status discipline paragraph: shadow tower PROVED, D²=0 PROVED at both levels | thm:mc2-bar-intrinsic |
| H0201 | 2 | XREF-STALE | I | chapters/frame/heisenberg_frame.tex:1755 | Change ref thm:mc2-full-resolution → thm:mc2-bar-intrinsic (bar-intrinsic is canonical, no Lie symmetry restriction) | thm:mc2-bar-intrinsic |
| H0202 | 2 | XREF-STALE | I | chapters/frame/heisenberg_frame.tex:1796 | Same: thm:mc2-full-resolution → thm:mc2-bar-intrinsic | thm:mc2-bar-intrinsic |
| H0203 | 2 | STATUS-ADD | I | appendices/typeA_baxter_rees_theta.tex:137-1355 | Add ClaimStatus tags to ALL 26 theorem-class environments (17 theorems + 9 props/lemmas/cors) — file has ZERO tags | STRIKE_LIST:B-series |
| H0204 | 2 | STATUS-ADD | I | appendices/casimir_divisor_core_transport.tex:111-1104 | Add ClaimStatus tags to ALL 14 environments (10 theorems + 4 conjectures) — file has ZERO tags | STRIKE_LIST:B-series |
| H0205 | 2 | STRUCTURE | I | appendices/casimir_divisor_core_transport.tex:6 | Add missing \label{} to chapter command | structure |
| H0206 | 2 | STATUS-ADD | I | appendices/dg_shifted_factorization_bridge.tex:113-1179 | Add ClaimStatus tags to ALL 15 theorem-class environments — file has ZERO tags | STRIKE_LIST:B-series |
| H0207 | 2 | MACRO-NORM | I | appendices/shifted_rtt_duality_orthogonal_coideals.tex:82-983 | Replace 23 textual \textup{[proved here]} → \ClaimStatusProvedHere (nonstandard convention) | LaTeX-rules |
| H0208 | 2 | MACRO-NORM | I | appendices/shifted_rtt_duality_orthogonal_coideals.tex:967 | Replace textual \textup{[conjectured]} → \ClaimStatusConjectured | LaTeX-rules |
| H0209 | 2 | STATUS-ADD | I | appendices/ordered_associative_chiral_kd.tex:297-1300 | Add ClaimStatus tags to ALL 14 environments (10 theorems + 4 conjectures) — file has ZERO tags | STRIKE_LIST:B-series |

**Restored file ClaimStatus summary**: 5 restored files have a combined **92 theorem-class environments** missing standard \ClaimStatus tags. This is the single largest cluster of STATUS-ADD items.


### Step2-D: Examples Medium+Small Files (5 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0210 | 2 | FORMULA-FIX | I | chapters/examples/w_algebras_deep.tex:340 | κ(W₃) = c/2 is T-channel only → change to 5c/6 or qualify as "T-channel κ_T" | landscape_census:99 |
| H0211 | 2 | FORMULA-FIX | I | chapters/examples/beta_gamma.tex:6 | "κ_{βγ} = 0 (uncurved)" misleading without qualifier → add "on the weight-changing line"; global κ = 6λ²-6λ+1 = 1 at λ=1 | beta_gamma:1005,2421 |
| H0212 | 2 | FORMULA-FIX | I | chapters/examples/landscape_census.tex:114 | Lattice VOA κ shows "---" → should show rank(Λ) per lattice_foundations.tex proof | lattice_foundations:12 |
| H0213 | 2 | STALE-PROSE | I | chapters/examples/landscape_census.tex:261 | "stage-5 open problem" potentially misleading 2 lines after MC4 closure → change to "stage-5 explicit verification" | MC4:proved |
| H0214 | 2 | STATUS-LEVEL | I | chapters/examples/w_algebras_deep.tex:346 | κ(H_Q)=Q²/2 normalization-dependent → clarify this is per-boson Miura-normalized level | landscape_census:68 |


---

## INTERIM CONSOLIDATION SUMMARY (awaiting 2 final agents)

### Item Counts by Phase

| Phase | Description | Items (main file) | Items (absorbed) | Total |
|-------|-------------|-------------------|------------------|-------|
| 1 | Delta Propagation (Δ1-Δ8) | 113 | — | 113 |
| 2 | File-by-File Audit | 51 | — | 51 |
| 3 | Existing Audit Absorption | 5 | 498 | 503 |
| 5 | Control Plane | 50 | — | 50 |
| **SUBTOTAL** | | **219** | **498** | **717** |

*Awaiting: Step2-A (theory large files, 7 files), Step2-G (Vol II, 44 files)*

### Item Counts by Category

| Category | Count (main file) |
|----------|-------------------|
| STALE-PROSE | 68 |
| STATUS-UP | 5 |
| STATUS-DOWN | 14 |
| STATUS-ADD | 11 (+ ~92 missing tags in restored files) |
| STATUS-LEVEL | 10 |
| FORMULA-FIX | 9 |
| DEF-DRIFT | 12 |
| XREF-STALE | 5 |
| XREF-BROKEN | 5 |
| XVOL-SYNC | 11 |
| MACRO-NORM | 2 |
| SCAFFOLD | 50 |
| REFORGE (absorbed) | 248 |
| STRIKE_LIST (absorbed) | 250 |
| STRUCTURE | 1 |

### Coverage (files with items found)

**Vol I theory/**: introduction, bar_cobar_adjunction_curved, bar_cobar_adjunction_inversion, higher_genus_modular_koszul, chiral_modules, chiral_hochschild_koszul, cobar_construction, koszul_pair_structure, homotopy_transfer ✓
**Vol I examples/**: yangians_computations, yangians_drinfeld_kohno, yangians_foundations, w_algebras, w_algebras_deep, kac_moody, free_fields, lattice_foundations, bar_complex_tables, beta_gamma, landscape_census, genus_expansions, deformation_quantization, deformation_quantization_examples ✓
**Vol I connections/**: concordance, editorial_constitution, genus_complete, bv_brst, feynman_diagrams, feynman_connection, frontier_modular_holography_platonic, semistrict_modular_higher_spin_w3, kontsevich_integral, ym_boundary_theory, ym_instanton_screening ✓
**Vol I appendices/**: nonlinear_modular_shadows, typeA_baxter_rees_theta, casimir_divisor_core_transport, dg_shifted_factorization_bridge, shifted_rtt_duality_orthogonal_coideals, ordered_associative_chiral_kd, coderived_models, nilpotent_completion, existence_criteria, branch_line_reductions, koszul_reference, homotopy_transfer ✓
**Vol I frame/**: heisenberg_frame ✓
**Vol II**: holomorphic_topological, fm3_planted_forest_synthesis, conclusion, spectral-braiding, w-algebras, affine_half_space_bv, log_ht_monodromy, hochschild, pva-descent, examples-worked, examples-complete, ht_bulk_boundary_line ✓
**Control plane**: CLAUDE.md, README.md, MEMORY.md, 16 memory files, 8 notes files, 3 metadata files ✓


### Step2-G: Vol II Full Audit (42 items)

**P0: Mathematical Errors (3 items)**

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0215 | 2 | DEF-DRIFT | II | examples-worked.tex:194 | A^!_{M2} = Ω B(U(g)) is WRONG; Ω B recovers A (bar-cobar inversion), not A^!. Change to A^!_{M2} = H*(B(U(g)))^v ≃ C*(g) | CLAUDE.md:pitfall-4-objects |
| H0216 | 2 | DEF-DRIFT | II | conclusion.tex:226 | Same A^! conflation: Ω B̄(A) recovers A, not A^!. Fix to Verdier dual of bar cohomology | CLAUDE.md:pitfall-4-objects |
| H0217 | 2 | DEF-DRIFT | II | ht_bulk_boundary_line.tex:1804 | Same: A^!_{M2} := Ω B̄(A) → H*(B̄(A))^v | CLAUDE.md:pitfall-4-objects |

**P1: Cross-Volume Sync (12 items)**

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0218 | 2 | XVOL-SYNC | II | concordance.tex:132 | "MC3 (DK extension)" → add "MC3 proved type A; arbitrary type open" | thm:mc3-type-a-resolution |
| H0219 | 2 | XVOL-SYNC | II | concordance.tex:(missing) | Add cross-volume bridge row for MC2 closure (bar-intrinsic Θ_A) | thm:mc2-bar-intrinsic |
| H0220 | 2 | XVOL-SYNC | II | concordance.tex:(missing) | Add cross-volume bridge row for MC4 closure (strong completion towers) | thm:completed-bar-cobar-strong |
| H0221 | 2 | XVOL-SYNC | II | conclusion.tex:86 | "MC3 programme" framed as fully open → note MC3 proved type A | thm:mc3-type-a-resolution |
| H0222 | 2 | XVOL-SYNC | II | w-algebras.tex:1353-1365 | Missing W∞ scalar saturation, weight-4 Gram matrix, c₃₃₄² from Vol I | thm:winfty-scalar, thm:c334 |
| H0223 | 2 | XVOL-SYNC | II | concordance.tex:441 | "Would advance MC3. Status: Open." → note type A proved | thm:mc3-type-a-resolution |
| H0224 | 2 | XVOL-SYNC | II | holomorphic_topological.tex:117 | "Coefficient identities belong to MC4" → MC4 CLOSED | thm:completed-bar-cobar-strong |
| H0225 | 2 | XVOL-SYNC | II | holomorphic_topological.tex:378 | "MC4/MC5" → MC4 CLOSED | thm:completed-bar-cobar-strong |
| H0226 | 2 | XVOL-SYNC | II | holomorphic_topological.tex:781 | "Remaining...belong to MC4" → MC4 CLOSED | thm:completed-bar-cobar-strong |
| H0227 | 2 | XVOL-SYNC | II | physical_origins.tex:73 | "remaining targets belong to MC4/MC5" → MC4 CLOSED | thm:completed-bar-cobar-strong |
| H0228 | 2 | XVOL-SYNC | II | physical_origins.tex:118 | "MC4/MC5 dependency order" → MC4 CLOSED | thm:completed-bar-cobar-strong |
| H0229 | 2 | XVOL-SYNC | II | spectral-braiding.tex:1044 | "full DK ladder (MC3)" → add "proved type A" | thm:mc3-type-a-resolution |

**P2: Dangling Cross-Volume References (14 items — 1 label, 14 occurrences)**

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0230 | 2 | XREF-BROKEN | II | holomorphic_topological.tex:71,117,291,378,394,443,781,826 | 8 bare \ref{conj:master-bv-brst} → use \ref*{} or define label locally (Vol I only) | xref |
| H0231 | 2 | XREF-BROKEN | II | bv_ht_physics.tex:180 | Dangling \ref{conj:master-bv-brst} | xref |
| H0232 | 2 | XREF-BROKEN | II | physical_origins.tex:73,101,118,154,179 | 5 dangling \ref{conj:master-bv-brst} | xref |

**P3: Missing ClaimStatus Tags (78 environments across 7 files)**

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0233 | 2 | STATUS-ADD | II | dg_shifted_factorization_bridge.tex:* | Add ClaimStatus to ALL 26 theorem envs (0% coverage) | STRIKE_LIST:B-series |
| H0234 | 2 | STATUS-ADD | II | ordered_associative_chiral_kd.tex:* | Add ClaimStatus to ALL 28 theorem envs (0% coverage) | STRIKE_LIST:B-series |
| H0235 | 2 | STATUS-ADD | II | fm-proofs.tex:* | Add ClaimStatus to ALL 6 theorem envs | STRIKE_LIST:B-series |
| H0236 | 2 | STATUS-ADD | II | pva-expanded.tex:* | Add ClaimStatus to ALL 7 theorem envs | STRIKE_LIST:B-series |
| H0237 | 2 | STATUS-ADD | II | pva-expanded-repaired.tex:* | Add ClaimStatus to ALL 7 theorem envs | STRIKE_LIST:B-series |
| H0238 | 2 | STATUS-ADD | II | orientations.tex:* | Add ClaimStatus to ALL 3 theorem envs | STRIKE_LIST:B-series |
| H0239 | 2 | STATUS-ADD | II | holomorphic_topological.tex:* | Add ClaimStatus to 1 missing theorem env | STRIKE_LIST:B-series |


### Step2-A: Theory Large Files (6 items)

| ID | PH | CAT | VOL | FILE:LINE | EDIT | SRC |
|----|----|----|-----|-----------|------|-----|
| H0240 | 2 | FORMULA-FIX | I | chapters/theory/higher_genus_modular_koszul.tex:5859-5860 | Cross-ref cites "Theorem D(iv)" for duality constraint → should be "(iii)" (Duality, not Additivity) | thm:modular-characteristic:1886 |
| H0241 | 2 | STALE-PROSE | I | chapters/theory/bar_cobar_adjunction_curved.tex:1882 | Drop "conjecturally" → "controlled by" (conj:winfty-stage4-ward-inheritance now ProvedElsewhere at line 3040) | bar_cobar_adjunction_curved:3040 |
| H0242 | 2 | STALE-PROSE | I | chapters/theory/chiral_modules.tex:1974 | Retitle "H-level open problem" → "H-level comparison conjecture" (MC4 closed) | thm:completed-bar-cobar-strong |

**Verified clean (no issues)**: higher_genus_complementarity.tex, higher_genus_foundations.tex, chiral_hochschild_koszul.tex

---

## FINAL CONSOLIDATION

### All 17 agents completed. Deduplication performed.

**Duplicate items removed** (same FILE:LINE appearing in multiple agents):
- main.tex:632 (Δ1 H0001 + Δ4 H0022): kept H0001
- main.tex:1161 (Δ2 H0011 + Δ3 H0037): kept H0011
- concordance.tex:1072 (Δ4 H0026 + Step2-E H0166 variant): kept H0026
- concordance.tex:1190 (Δ2 H0013): single item
- genus_complete.tex:198 (Δ4 H0024 + Δ5 H0069 + Step2-E H0164): kept H0164 (most specific)
- genus_complete.tex:1131 (Δ1 H0009 + Step2-E H0165): kept H0009
- introduction.tex:1420-1433 (Δ5 H0063-66 + Step2-A + Step2-B): kept H0063-66
- nonlinear_modular_shadows.tex:73 (Δ1 H0002 + Δ4 H0027 + Step2-F H0200): kept H0002
- bar_cobar_adjunction_curved.tex:498 (Δ3 H0041 + Step2-B): kept H0041
- bar_cobar_adjunction_inversion.tex:694 (Δ3 H0045 + Step2-B H0187 variant): kept H0045
- chiral_modules.tex:3792 (Δ3 H0052 + Step2-A H0242 variant): kept H0052
- yangians_drinfeld_kohno.tex:987 (Δ3 H0058 + Step2-C H0196): kept H0058
- holomorphic_topological.tex:117,378,781 (Δ3 + Step2-G): kept Step2-G (more specific)
- Vol II concordance.tex:132,441 (Δ2 + Step2-G): kept Step2-G

**~25 duplicates removed**, leaving **~220 unique items in main file**.

### FINAL ITEM COUNT

| Source | Items |
|--------|-------|
| Main file (H0001–H0242, minus ~25 duplicates) | ~217 |
| Absorbed: REFORGE findings | 248 |
| Absorbed: STRIKE_LIST items | 250 |
| Absorbed: Formula propagation | 5 |
| Bulk STATUS-ADD: Vol I restored files (92 envs) | 92 |
| Bulk STATUS-ADD: Vol II missing tags (78 envs) | 78 |
| **GRAND TOTAL** | **~890** |

### Item Distribution by Category

| Category | Count | Description |
|----------|-------|-------------|
| STALE-PROSE | ~75 | MC2/MC3/MC4 status not propagated, "conjectural" for proved results |
| STATUS-ADD | ~170 | Missing ClaimStatus tags (bulk: 5 restored Vol I files + 7 Vol II files) |
| STATUS-UP | 5 | ClaimStatusConjectured → ProvedHere |
| STATUS-DOWN | 14 | Definitions incorrectly carrying ClaimStatusConjectured |
| STATUS-LEVEL | 10 | Missing convolution/ambient or finite/all-arity qualifier |
| FORMULA-FIX | 12 | Wrong κ formulas, Theorem D misnumbering, unsimplified fractions |
| DEF-DRIFT | 15 | Four-object conflation (A^!≠ΩB(A)), two-level convention missing |
| XREF-BROKEN | 17 | Dangling \ref{conj:master-bv-brst} in Vol II (14), missing \cite{Mok25} |
| XREF-STALE | 5 | Stale labels (conj: → thm:), stale theorem counts |
| XVOL-SYNC | 23 | Vol II not absorbing MC2/MC3/MC4 closures, W∞ results |
| MACRO-NORM | 2 | Nonstandard textual [proved here] instead of \ClaimStatus macros |
| SCAFFOLD | 55 | CLAUDE.md drift, README.md stale counts, memory files stale |
| REFORGE | 248 | Tell-not-show prose (THROAT/ECHO/DEAD/SCOPE) |
| STRIKE_LIST | 250 | Build health, structural integrity, content verification |
| STRUCTURE | 2 | Missing chapter headers, missing labels |
| **TOTAL** | **~903** |

### Coverage Matrix

| Directory | Files Audited | Files with Items | Files Clean |
|-----------|--------------|-----------------|-------------|
| Vol I theory/ (24) | 15 | 12 | 3 (hg_comp, hg_found, chh_koszul) |
| Vol I examples/ (20) | 16 | 14 | 2 (verified clean) |
| Vol I connections/ (15) | 13 | 11 | 2 (concordance, ed_constitution = truth sources) |
| Vol I appendices/ (23) | 17 | 12 | 5 (small/reference) |
| Vol I frame/ (2) | 2 | 2 | 0 |
| Vol II all/ (44) | 20 | 17 | 3 |
| Control plane | 35+ | 30+ | 5 (recent/consistent) |
| **TOTAL** | **~120** | **~100** | **~20** |

### Priority Triage

**P0 — Mathematical errors (fix immediately):**
- H0215-H0217: A^! := Ω B(A) conflation in 3 Vol II files (DEF-DRIFT)
- H0191-H0194: Wrong KM κ formulas in 4 Vol I files (FORMULA-FIX)
- H0189-H0190, H0240: Theorem D part misnumbering (iii)→(iv) in 3 locations
- H0210-H0212: κ(W₃), κ(βγ), κ(lattice) formula issues

**P1 — Status propagation (high-value, systematic):**
- H0001-H0010: MC2 bar-intrinsic not propagated (~10 files)
- H0037-H0062: MC4 closure not propagated (~26 files)
- H0218-H0229: Vol II not absorbing MC2/MC3/MC4 (~12 items)
- H0023, H0025-H0026: Ambient D²=0 proved status not propagated

**P2 — Structural integrity (bulk work):**
- H0203-H0209, H0233-H0239: 170 missing ClaimStatus tags across 12 files
- H0230-H0232: 14 dangling cross-volume \ref{conj:master-bv-brst}
- 248 REFORGE prose items (tell-not-show)
- 250 STRIKE_LIST items (build/structure)

**P3 — Control plane harmonization:**
- H0032-H0036: CLAUDE.md (identification theorem count, appendix clusters, MC4 description)
- H0114-H0127: README.md (20 stale counts/descriptions)
- H0128-H0163: Memory files and notes (stale MC status, old file names)

