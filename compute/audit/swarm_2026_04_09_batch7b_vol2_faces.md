# Adversarial Swarm 2026-04-09/10 — Batch 7b: Vol II Seven Faces chapter-level

**Scope.** 10 agents, 10 distinct angles going below the master-theorem level that Batch 5 covered. Sweeps each of Vol II's seven face sections + 6 additional bbl-core chapters + full AP126 compliance + Vol II novelty assessment + honest reformulation writer.

## Master verdict

**Vol II's master theorem is a forwarding restatement of Vol I**; the genuinely new Vol II content lives in separate chapters (3D gravity, DNP line operators, half-space BV, celestial, Kontsevich integral). The master theorem's `\ClaimStatusProvedHere` tag is **locally correct but systematically erases per-face caveats** from Vol I (F3 higher-genus conjectural, F4 W_N normalization, F7 rescaling, F5 DK-4/5 conditional).

**13 AP126 violations found in Vol II** across 8 distinct files, three sharing a level-stripped Sugawara template suggesting copy-paste from a common broken source.

## 10-angle findings

### Angle 1 — Face 1 chapter: Swiss-cheese bar-cobar twisting

**Verdict: FACE-IMPORTED + FACE-SC-PROMOTION-GAP + FACE-AP126-VIOLATED.**

- Lives at `dnp_identification_master.tex:58-74` — NOT a chapter, just a section
- Vol II adds no new proof; imports `V1-thm:collision-residue-twisting`
- **V2-AP86 gap**: SC is two-coloured but F1 treats A as one-colour input. No promotion A → (A,A). "Swiss-cheese setting" is decorative; actual formula is the one-colour Vol I twisting morphism
- **Two AP126 violations in this file**: L48 `r(z) = Ω/((k+h^v)z)` (affine KM) and L415 `r^{sl_3}(z) = Ω/((k+3)z)`. Both bare Ω, no k prefix
- Genus-0 only; higher-genus deferred to `genus1_seven_faces.tex`
- CG17, Costello 2011 EFT not cited in this section

### Angle 2 — Face 2 chapter: Line operators as A^!-modules

**Verdict: FACE-CONDITIONAL.**

- **Real content lives at `line-operators.tex:1674-1710`** (`thm:dnp-bar-cobar-identification`, ProvedHere), NOT in the master file which only summarizes
- Three clauses: (i) monoidal Φ: C_line ≃ A^!_line-mod, (ii) MC identification r(z) = Res^coll, (iii) non-renormalization = E_2 collapse
- Clauses (i)-(ii) ride on prior theorems (Vol I collision residue + Face 5 Yangian recognition); clause (iii) is genuine new content
- **Face 2 depends on Face 5** via `thm:yangian-recognition` — separation directional, not independent
- AP126 violation at `dnp_identification_master.tex:48` propagates to Face 2 via the summary
- `rem:lines-modules-scope:382-385` hedges the full bulk-boundary-line triangle to conjectural outside boundary-linear sector — but this caveat is not in the master theorem statement
- RNW19 bifunctoriality trap avoided implicitly via single-slot hom_α construction; never explicitly addressed
- DNP25 cited with specific theorem numbers (Thm 3.1, Thm 4.1)

### Angle 3 — Face 3 chapter: Khan-Zeng PVA λ-bracket

**Verdict: SCOPE-HIDDEN.**

- Vol II F3 at `dnp_identification_master.tex:102-124` — pointer, not derivation
- Vol II says "at tree level" (L116) — too soft; no explicit genus-0 tag, no `(g=0 only)` qualifier
- **Vol I clause (iv) higher-genus conjectural clause NOT propagated** to Vol II
- Master theorem `thm:seven-face-master-3d-ht` claims `\ClaimStatusProvedHere` while listing F3 — silent inheritance of a conjectural clause
- A Vol II reader cannot recover the g=0 restriction without traversing V1- prefix back to Vol I L1797-1808
- KZ25 (Khan-Zeng, arXiv:2502.13227 "Poisson vertex algebras and 3d gauge theory") cited with double bibitem alias

### Angle 4 — Face 4 chapter: Gaiotto-Zeng Hamiltonians

**Verdict: SCOPE-DRIFT + FACE-IMPORTED.**

- Vol II F4 at `dnp_identification_master.tex:126-146` — section only, delegates to Vol I
- **W_N conjectural qualifier ABSENT in Vol II**. `rem:gz26-wn-comparison-conjectural` from Vol I NOT transported
- Master theorem lists F4 in ProvedHere master without remark transport
- GZ26 (arXiv:2603.08783, **dated to 2026** — forward-dated) cited
- **Calogero-Moser literature baseline absent**: no Calogero 1975, Moser 1975, Etingof-Felder-Ma 2009, Olshanski 2002 in Vol II bibliography
- Commutativity imported, not derived
- W_N verification exists only via 105 compute tests

### Angle 5 — Face 5 chapter: dg-shifted Yangian

**Verdict: FACE-PROVED + DK-CONDITIONAL + scope-gap + missing-citation.**

- Vol II F5 is the DNP dg-shifted Yangian (distinct from Vol I F5 which is classical Drinfeld Yangian)
- Same "F5" label in both volumes but **different objects** — Batch 5 Angle 9 caught this
- **Finkelberg-Tsymbaliuk 2017** (arXiv:1708.01795 "Shifted quantum affine algebras") — ABSENT from Vol II bibliography, despite being the canonical reference for shifted Yangians
- AP126 in the F5 chapter body: CLEAN (Vol II F5 chapter uses `R(z) = 1 + k·Ω/z + ...` correctly)
- **Critical level k=-h^v gap**: zero matches for "critical level", "k=-h^v", "generic level" in the F5 chapter. Parameter dictionary ℏ = 1/(k+h^v) breaks at critical level; not addressed
- DK-4/5 conditional status via implicit "chirally Koszul locus" restriction, not explicit in theorem statement

### Angle 6 — Face 6 chapter: Sklyanin Poisson bracket

**Verdict: FACE-DUPLICATES-VOL-I + FACE-BIBLIOGRAPHY-GAP.**

- Vol II F6 at `dnp_identification_master.tex:168-183` — verbatim duplicate of Vol I F6 in scope (rational STS83)
- Supporting derivation at `spectral-braiding-core.tex:1932-1992` via FRT (classical limit ℏ→0), not via chiral Li filtration
- **Same bibliography gap as Vol I**: Sklyanin 1982 (arXiv-era), Felder 1994 (KZB), Etingof-Varchenko 1998 (E_{τ,η}(sl_2)) all MISSING
- Elliptic case deferred to Vol III as "future work" (forward-pointer at L453-454)
- Terminology mismatch continues: "Sklyanin Poisson bracket" naming the STS83 construction, not Sklyanin's 1982 elliptic R-matrix

### Angle 7 — Face 7 chapter: Gaudin Hamiltonians

**Verdict: FACE-RESCALING + FACE-CRITICAL-LIMIT-GAP.**

- Vol II F7 at `dnp_identification_master.tex:185-204`
- **Literal rescaling**: H_i^GZ = (1/(k+h^v)) · H_i^Gaudin (L193-202, verbatim)
- Singular at k = -h^v, exactly where FFR94's theorem has content
- FFR94 cited but the critical-level mechanism (Sugawara = Feigin-Frenkel center) never mentioned
- **Talalaev 2006 and Rybnikov 2006** (canonical higher-Hamiltonian/Bethe-algebra references) ABSENT from Vol II bibliography
- Minor new Vol II addition: one sentence (L203-204) gestures at "higher Gaudin Hamiltonians (collision residues at depth k≥2) extend this to the full A_∞ Yangian structure" — no proof, no engine, no precise meaning
- W_3 Gaudin construction in `examples/w-algebras-w3.tex:2152-2216` not cross-referenced from Face 7

### Angle 8 — Additional bbl-core chapters (6 chapters)

**Verdict: 6-CHAPTERS-SUPPORT-FACES** (with carve-outs).

| Chapter | Lines | Thms/Props | Main claim | Face mapping |
|---|---|---|---|---|
| `spectral-braiding-core.tex` | 4606 | 34 (44 ProvedHere) | Spectral R(z) from bulk-boundary line composition; YBE from W-coherence on FM_3(C); dg-shifted Yangian | Face 2/5 expansion |
| `ht_bulk_boundary_line_core.tex` | 3032 | 35 (40 ProvedHere, 1 Conjectured) | A_bulk ≃ Z^der(B_bound) ≃ Z^der(C_line) ≃ HH*_ch(A^!_line) Koszul triangle | Face 7 expansion |
| `celestial_boundary_transfer_core.tex` | 1454 | 37 (37 ProvedHere) | KK transfer of A_∞/L_∞ to H_b^{0,*}(S^3); nonlinear obstruction towers Ob_r; Airy-Witt normal form | Face 5 expansion — **substantive new content**, not just metaphorical |
| `affine_half_space_bv.tex` | 1768 | 31 (33 ProvedHere) | Half-space BV quantization of KZ affine PVA sigma model on C × R_≥0; one-loop exact; K_eff = k + ℏδ_g | **NEW**: BV-BRST = bar on half-space, not a face |
| `fm3_planted_forest_synthesis.tex` | 481 | 6 (6 ProvedHere) | Coderivation MC envelope; local residue splitting; planted-forest small model for FM_3 | Technical substrate for arity-3 Θ^oc |
| `kontsevich_integral.tex` | 622 | 7 (6 ProvedHere, 3 ProvedElsewhere, 2 Conjectured) | Bar propagator restricts to Kontsevich propagator on C_n(S^1); bar weight systems = Lie algebra weight systems; 4T from Arnold | Bridge to knot theory |

**Key observations**:
- The master `dnp_identification_master.tex` is only 464 lines; the heavy content lives in these 6 chapters
- `celestial_boundary_transfer_core.tex` has substantive obstruction theory — **upgrades Batch 5 Angle 6's "FACE-METAPHORICAL" verdict**: at the chapter level, celestial is mathematically substantive (Airy-Witt normal form, obstruction towers)
- `affine_half_space_bv.tex` IS the BV-BRST = bar chapter, fulfilling Batch 7a Angle 1's promise at the half-space level
- 4 chapters (celestial, half-space BV, planted forest, kontsevich) have ZERO conjectures / ZERO ProvedElsewhere — density of ProvedHere claims invites AP40 audit

### Angle 9 — Vol II AP126 deep sweep: 13 VIOLATIONS

| # | File | Line | Formula | Severity |
|---|---|---|---|---|
| V1 | `dnp_identification_master.tex` | 48 | `r(z) = Ω/((k+h^v)z)` | Sugawara level strip |
| V2 | `ht_bulk_boundary_line_core.tex` | 2376 | `r(z) = Ω/z` (sl_2 worked example) | Bare, internal contradiction with same file L3025 |
| V3 | `celestial_holography.tex` | 1953 | `R_cel(z) = 1 + Ω/z + ...` | Yangian deformation ℏ dropped |
| V4 | `thqg_gravitational_yangian.tex` | 1128 | `r_ij(z) = Ω_ij/z` "universal" | Universal claim with level stripped |
| V5 | `thqg_gravitational_yangian.tex` | 1191 | Same formula in IBR proof | Bare |
| V6 | `thqg_gravitational_yangian.tex` | 1709 | `T^(0) = Ω/(k+h^v)` transfer matrix | Sugawara level strip |
| V7 | `ordered_associative_chiral_kd.tex` | 2254 | `R(z) = 1 + Ω/z + O(z^-2)` (sl_2) | Bare |
| V8 | `ordered_associative_chiral_kd.tex` | 2364 | Same formula, ℏ = 1/(k+2) in surrounding text | Displayed eq drops prefactor |
| V9 | `ordered_associative_chiral_kd_frontier.tex` | 3512 | `r_cl(ζ) = Ω/ζ` (q-lattice classical limit) | Bare |
| V10 | `ordered_associative_chiral_kd_frontier.tex` | 3661 | `r(u) = Ω/u` CYBE | Bare |
| V11 | `thqg_spectral_braiding_extensions.tex` | 1502 | `r_0(z) = Ω/((k+h^v)z) + kκ/z²` | Sugawara level strip (same as V1) |
| V12 | `thqg_ht_bbl_extensions.tex` | 1100 | `Ω/z` of gl_K (M2 / double-loop) | Borderline, ℏ convention |
| V13 | `line-operators.tex` | 907 | `R_{λ_1,λ_2}(z) = exp(Ω_{λ_1,λ_2}/z)` | R-matrix exponent drops k |

**Three sites share the level-stripped Sugawara form** (V1, V11, plus the Batch 5 Vol I finding at `holographic_datum_master.tex:448-456`) — propagated from a common broken template. The remaining 10 are independent instances.

**Compliant chapters** (cross-check): `line-operators.tex:835-1050` (correct `k·Ω/z` multiple times), `spectral-braiding-core.tex:40, 507, 521, 539, 543, 650, 1147, ...` (all compliant), `ht_bulk_boundary_line_core.tex:3015-3032` (correct, cites AP126 explicitly), `ordered_associative_chiral_kd_core.tex:2095-2114` (correct with explicit AP126 footnote), `log_ht_monodromy_core.tex` (many correct sites with (AP126) annotations), `holomorphic_topological.tex` (compliant), `affine_half_space_bv.tex` / `fm3_planted_forest_synthesis.tex` / `kontsevich_integral.tex` (N/A — no r-matrix formulas).

**Pattern**: the violations cluster in "frontier" / "extensions" files and master summary files; the "core" files are largely compliant. This suggests a wave-based development where core files got AP126 rectified but the frontier/extension/summary files lagged.

### Angle 10 — Vol II Seven Faces novelty synthesis

**Verdict: VOL-II-HAS-NEW-MATH** (but the seven-face master is NOT the new math).

**Master theorem comparison**:
- Vol I `thm:seven-faces-master` at `holographic_datum_master.tex:136-164` (1144 lines in chapter)
- Vol II `thm:seven-face-master-3d-ht` at `dnp_identification_master.tex:209-239` (464 lines in chapter, master is 30 lines)
- **Identical statement content**. Vol II's "proof" at L241-250 is a 4-line citation chain — 5 of 7 faces forwarded to Vol I theorems.

**Category theoretical distinction**: Vol II works with SC^{ch,top}-algebras vs "modular Koszul chiral algebras on X" — a realization layer on top of identical algebraic content, not a theoretically distinct category.

**The DK-four-path theorem** at L259-295: genuine content beyond Vol I (4 independent paths, 63 compute tests verifying DK-0 for spins j ∈ {1/2, 1, 3/2, 2} and levels k = 1..20). But still a VERIFICATION of an existing Vol I claim, not a new theorem.

**Where Vol II earns its ~1500 pages**:

| Chapter | Lines | Content |
|---|---|---|
| `3d_gravity.tex` | 7790 | **The actual climax** — 27+ theorems: Brown-Henneaux, gravitational Koszul triangle, gap migration, period-2 Catalan factorisation, graviton resolvent closed form, MSS bound, OTOC from R-matrix, Stasheff cancellation, infinite soft graviton tower |
| `line-operators.tex` | 1818 | **Genuine keystone**: DNP bar-cobar identification, lines as modules |
| `affine_half_space_bv.tex` | 1768 | Half-space BV programme (Vol I has no analog) |
| `celestial_holography_core.tex` | 1117 | Celestial OPE, modular obstruction tower, helicity splitting |
| `kontsevich_integral.tex` | 622 | Kontsevich integral bridge |
| `thqg_holographic_reconstruction.tex` | 2745 | |
| `thqg_modular_bootstrap.tex` | 2928 | |

**Honest assessment**: Vol II = Vol I + 3D gravity application (Part VI, ~half of Vol II by length) + DNP line operators + half-space BV + celestial + Kontsevich. Strip the gravity climax and the DNP/celestial/half-space chapters, and the remainder overlaps substantially with Vol I + SC^{ch,top} reformatting.

**Caveat**: Batch 7a Angle 5 flagged Part VI as CLIMAX-CONDITIONAL. Of 27+ gravity theorems, Cardy formula and BTZ entropy are explicit `conj:`, Brown-Henneaux is explicitly imported, Virasoro line identification is conjectural. The new math is real, but with substantial conditional pockets.

## Vol II Seven Faces honest reformulation (Angle 10 deliverable)

**Complete LaTeX** produced at Angle 10 report for `thm:seven-faces-honest-v2` replacing `thm:seven-face-master-3d-ht` at `dnp_identification_master.tex:209-239`. Key features:
- Per-face status tags explicit: F1 unconditional, F2/F5 DK-4/5 conditional, F3 g=0 only + higher-genus conjectural, F4 KM+Vir only + W_N conditional, F7 rescaling
- Genericity hypothesis k ≠ -h^v in opening
- Cross-volume cite to `V1-thm:seven-faces-honest-v1` (itself part of Batch 5 deliverable pipeline)
- Companion `rem:seven-faces-honest-v2-cite` for AP5 propagation hook
- AP126/AP141 compliant: no bare Ω/z; only Sugawara-prefixed forms
- AP125/AP124 verified: prefix matches environment, v2 suffix unique across all three volumes

**Ordering constraint**: Batch 5's v1 theorem must land before Batch 7b's v2 to avoid dangling cross-reference.

## New findings (F43-F51)

**F43 — 13 AP126 violations in Vol II** across 8 files, many in thqg_gravitational_yangian and frontier files. Pattern: "core" files compliant, "frontier/extensions/master-summary" files lag.

**F44 — Three-site level-stripped Sugawara template**: `dnp_identification_master.tex:48`, `thqg_spectral_braiding_extensions.tex:1502`, `holographic_datum_master.tex:448` all share the same broken form — common parent template.

**F45 — Vol II Face 3 (Khan-Zeng) silently erases the Vol I higher-genus conjectural clause**. Master-theorem `ProvedHere` tag propagates a stronger statement than the underlying Vol I theorem supports.

**F46 — Vol II Face 4 (Gaiotto-Zeng) silently erases the Vol I W_N conjectural qualifier** via the same master-theorem propagation mechanism.

**F47 — Vol II Face 5 missing Finkelberg-Tsymbaliuk 2017** (arXiv:1708.01795, canonical shifted-Yangian reference). Added to bibliography gap list.

**F48 — Vol II Face 6 missing Sklyanin 1982, Felder 1994, Etingof-Varchenko 1998** (same gap as Vol I). Terminology mismatch persists: "Sklyanin Poisson bracket" names the 1983 STS construction, not Sklyanin's eponymous 1982 paper.

**F49 — Vol II Face 7 missing Talalaev 2006 and Rybnikov 2006** (canonical higher-Hamiltonian/Bethe-algebra references). Also silent on critical-level mechanism that FFR94 actually addresses.

**F50 — Vol II Face 4 missing Calogero-Moser literature baseline**: Calogero 1975, Moser 1975, Etingof-Felder-Ma 2009, Olshanski 2002. Integrable systems context undercited.

**F51 — Vol II master theorem is a forwarding restatement**: 464-line chapter, 30-line master theorem, 4-line "proof" delegating to Vol I. The real Vol II math is in 3D gravity + DNP + BV half-space + celestial + Kontsevich chapters, not in the Seven Faces master.

**F52 — 4 bbl-core chapters with ZERO conjectures** (celestial, half-space BV, planted forest, kontsevich_integral): density of ProvedHere claims invites AP40 audit — are all claims actually proved, or are some "prove-by-assertion"?

**F53 — Vol II Face 2 has only ONE conjecture across 6 bbl-core chapters in 11,963 lines** (`ht_bulk_boundary_line_core.tex`). Low conjecture density could indicate either genuine completeness or hidden conjectural content.

## Batch 7b deliverable inventory (10 items ready to apply)

1. Vol II `thm:seven-faces-honest-v2` rewrite (complete LaTeX at Angle 10)
2. AP126 fix plan for 13 violations (specific before→after text per site)
3. Transport `rem:gz26-wn-comparison-conjectural` from Vol I to Vol II Face 4
4. Propagate higher-genus conjectural clause to Vol II Face 3 via explicit `(g=0 only)` tag
5. Add Finkelberg-Tsymbaliuk 2017 bibitem (Face 5)
6. Add Sklyanin 1982, Felder 1994, Etingof-Varchenko 1998 bibitems (Face 6)
7. Add Talalaev 2006, Rybnikov 2006 bibitems (Face 7)
8. Add Calogero 1975, Moser 1975, Etingof-Felder-Ma 2009, Olshanski 2002 bibitems (Face 4)
9. Critical-level scope sentence for Face 5 (k ≠ -h^v)
10. SC two-colour promotion fix for Face 1 (`A → (A, A)` per V2-AP86)

## Open items for Batch 7c+

- Full bibliography audit across all three volumes (Batch 7c launching now)
- Vol II Face 1 SC promotion architectural fix (requires rewriting the F1 section not just the master)
- Vol II `thm:dnp-bar-cobar-identification` standalone verification (is DNP25 itself a reliable reference?)
- Vol II `thm:seven-face-master-3d-ht` `ProvedHere` tag — should it be `Conditional` given the conjectural clauses it silently erases?
- `celestial_boundary_transfer_core.tex` chapter-level deep audit (37 ProvedHere claims across 1454 lines, zero conjectures)
