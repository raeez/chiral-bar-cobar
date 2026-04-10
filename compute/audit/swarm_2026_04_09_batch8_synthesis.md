# Adversarial Swarm 2026-04-09/10 — Batch 8: 5-segment parallel attack

**Scope.** 10 agents across 5 segments: CFG25 emergency triage (3 angles), compute engine AP10/AP128 (2 angles), Part II Shadow Tower (2 angles), cross-volume preface/intro consistency (2 angles), standalone papers (1 angle).

## Master verdict

Two major corrections to prior batch findings:

1. **F55 (CFG25 fabricated) is WRONG.** WebFetch on arXiv:2602.12412 returns a real paper: "Chern-Simons factorization algebras and knot polynomials" by Costello-Francis-Gwilliam, submitted Feb 12, 2026. The BIBITEM TITLE is wrong ("Chiral Koszul duality" — that string is Francis-Gaitsgory 2012), but the arXiv ID and authors match. Fix is title correction + per-cite content review, NOT deletion.

2. **F52 (Felder 1994 absent from Vol II) is WRONG.** Batch 7b flagged Felder 1994 missing; Batch 7c confirmed; Batch 8 finds `Fel94` IS present in Vol II bibliography. Remove Felder94 from the missing-references list.

Beyond these corrections, Batch 8 found:
- **New r-matrix AP128 sub-epidemic** in 8 compute engines (bare Omega/z)
- **6 shadow classes, not 4** (G/L/C/M + M* + W)
- **10 families lack any shadow class row** in the landscape census (most serious: BP_k)
- **AP131 d_gen symbol ABSENT** from all chapters (only d_alg exists)
- **κ_BPS violation in Vol III intro L238-241** (new HZ-7 violation)
- **standalone N5 owns the CORRECT Huang05 title** — source of truth for monograph fix
- **10 MC5 hedge sites all consistent** in standalones (MC5 reconciliation propagated cleanly)

## Segment 1: CFG25 emergency triage (3 agents)

### Angle 1 — CFG25 full grep sweep

**13 substantive hits (non-audit) across 9 files in 3 volumes**:

Vol I:
- `bibliography/references.tex:340-341` — BIBITEM definition
- `chapters/theory/chiral_koszul_pairs.tex:78` — `\cite{CFG25}` prose "general chiral Koszul duality framework"
- `chapters/connections/kontsevich_integral.tex:516` — `\cite{CFG25}` same prose
- `chapters/connections/holomorphic_topological.tex:947` — `\cite{CFG25}` in 12-key Costello cluster
- `chapters/connections/holomorphic_topological.tex:1089` — table row "Chiral Koszul duality (general)"
- `chapters/connections/holomorphic_topological.tex:1179` — prose "Costello-Francis-Gwilliam develop the general framework"

Vol II (mirror files):
- `main.tex:2074-2075` — BIBITEM
- `chapters/connections/kontsevich_integral.tex:515` — mirror of Vol I 516
- `chapters/connections/holomorphic_topological.tex:943` — mirror of Vol I 947
- `chapters/connections/holomorphic_topological.tex:1087` — mirror table row
- `chapters/connections/holomorphic_topological.tex:1180` — mirror prose

Vol III:
- Zero .tex hits (no bibliography)

**METADATA DISCOVERY**: `/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:18` and `/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md:18` BOTH contain:
```
Cliff-Gannon-Frenkel [CFG25]: universal chiral algebras and genus extension
```
**TWO distinct fabricated identities share the `CFG25` key**:
- BIBITEM identity: "Costello-Francis-Gwilliam, Chiral Koszul duality" (wrong title, real arXiv)
- FRONTIER identity: "Cliff-Gannon-Frenkel, universal chiral algebras and genus extension" (different authors, different title, no arXiv)

The FRONTIER metadata version was not flagged in Batch 7c. This is a second fabrication layer.

### Angle 2 — CFG25 replacement analysis (FG12 hypothesis — now superseded by Angle 3)

Angle 2 worked under the Batch 7c hypothesis that CFG25 is fully fabricated. It found that a SINGLE replacement (`FG12`) suffices for all 5 unique call sites — every call site supports "the general chiral Koszul duality framework" which is exactly the FG12 title. Per-site fix plan produced.

**But Angle 3 then found the arXiv ID 2602.12412 IS real, with matching authors.** So the correct fix is:
- The BIBITEM title "Chiral Koszul duality" is wrong — should be "Chern-Simons factorization algebras and knot polynomials"
- The CITATION CALLS were inserted under the wrong assumption that the paper is about chiral Koszul duality
- Per-cite review needed: each `\cite{CFG25}` site was placed assuming "chiral Koszul duality framework" content. The actual paper (Chern-Simons knot polynomials) is about RESHETIKHIN-TURAEV / E_3 quantization / factorization homology trace — a related but distinct topic.
- For each call site, decide: (a) replace with `\cite{FG12}` (if the context is specifically about chiral Koszul duality), or (b) keep `\cite{CFG25}` with corrected title (if the context is about Costello-Gwilliam factorization-algebra knot invariants)

### Angle 3 — Other forward-dated entries + WebFetch verification

**Seven Vol I 2026 bibitems probed via WebFetch**:

| Key | arXiv | Page exists? | Title matches? | Verdict |
|-----|-------|--------------|----------------|---------|
| **CFG25** | 2602.12412 | YES | **NO — title is wrong** | **TITLE-FIX, NOT DELETE** |
| Moriwaki26a | 2602.08729 | YES | YES | LIKELY REAL |
| Moriwaki26b | 2603.06491 | YES | YES | LIKELY REAL |
| Nafcha26 | 2603.30037 | YES | YES | LIKELY REAL (serial unusual but real) |
| CDN26 | 2603.04667 | YES | YES | LIKELY REAL |
| LQ26 | 2601.12017 | YES | YES | LIKELY REAL |
| GZ26 | 2603.08783 | YES | YES | LIKELY REAL |
| Nish26 | 2512.xxxxx | N/A (placeholder) | n/a | CONFIRMED BROKEN |

**Cross-volume cite counts**:
- CFG25: 5 Vol I + 4 Vol II + 0 Vol III
- Moriwaki26a/b: 22 Vol I + 3 Vol II + 1 Vol III
- Nafcha26: **0 everywhere** — ORPHAN, safe to delete
- CDN26: 1 Vol I, 0 others
- LQ26: 1 Vol I, 0 others
- GZ26: 28 Vol I (heavy) + 0 others
- Nish26: 21 Vol I + 1 Vol II + 0 Vol III — 22 dangling cites

**New fix plan for Batch 7c / F55 correction**:
- CFG25: **TITLE FIX** (change to "Chern-Simons factorization algebras and knot polynomials") + per-cite content audit
- Nafcha26: **DELETE** (0 cites)
- Nish26: **STILL BROKEN** (placeholder arXiv ID)
- 5 others: **KEEP** (WebFetch-verified real papers)

## Segment 2: Compute engine AP10/AP128 (2 agents)

### Angle 4 — AP10 hostile sweep

**1 CRITICAL (FM5 live)**: `compute/lib/bc_exceptional_categorical_zeta_engine.py:750` contains `779247` in `_E8_SMALL_DIMS` lookup table. This is NOT an E_8 irreducible dimension (FM5 prohibition). `_KNOWN_FUND_DIMS['E8']` at L130 is correct; only `_E8_SMALL_DIMS` is poisoned. Served by `e8_first_dims()`. No test catches it because tests only check positions 0-4 of the list (248, 3875, 27000, 30380) and 779247 is at position 5+.

**20 AP10 violations ranked by severity**. Top 5:
1. **779247 in E8 dims** — FM5 live (described above)
2. **`test_bar_cohomology_sl2_explicit_engine.py:177`** — `H^3_6 = 7` with comment "(new computation from this engine)" — **literal AP128 textbook case**
3. **`test_bar_cohomology_sl2_explicit_engine.py:188`** — `H^4_{10} = 9` with same "(new computation)" comment
4. **`test_genus2_shadow_strata.py:188`** — 10 stable graphs at M̄_{2,2}, no derivation cited (AP123 pitfall territory)
5. **`bp_shadow_tower.py:98-99`** — `tower[3]=2`, `tower[4]=10/(c(5c+22))` with no derivation comment

**Cluster A (bar-cohomology "new computation" cluster)**: tests explicitly assert "new computation from this engine" — engine's own output frozen as expected. Sister engines (sl_3, w_3, w_4, lattice) likely propagate same anti-pattern.

**Cluster B (Vir shadow tower seeds)**: `bp_shadow_tower.py:98-99` hardcodes seeds with no derivation, and tests at `test_genus2_shadow_strata.py:102-114` re-hardcode evaluations at c=10, c=1, c=26 — circular AP128.

**Cluster C (`_E8_SMALL_DIMS` poisoning)**: single live FM5, latent because not actively tested.

### Angle 5 — AP128 hostile sweep (r-matrix sub-epidemic)

**DOMINANT PATTERN: r-matrix level-prefix AP128 sub-epidemic in 8+ engines.** The bare Omega/z AP126 violation that Batch 5+7b found in `.tex` files has a MIRROR in the compute layer that was never swept.

**Top 10 AP128-risk pairs**:

1. `theorem_seven_face_categorification_engine.py` + test — `_r_matrix_affine_sl2` returns `Fraction(1, k+2)` (docstring says "Omega/((k+2)z)"); test hardcodes `Fraction(1,3)` for k=1; at k=0 engine returns 1/2 (should be 0); at k=-2 ZeroDivisionError
2. `theorem_three_way_r_matrix_engine.py` + test — FOUR perspectives (RMatrixFromBar/PVA/DNP/GZ26.affine_sl2) all return `1/(k+2)`; tests hardcode matching values; "four-way agreement" is circular on the wrong scalar
3. `quantum_rmatrix_barcomplex.py:316-340` `classical_r_matrix_fundamental` returns `Omega/z` (no k); test asserts bare form
4. `theorem_genus1_seven_faces_engine.py` (6 sites) — uses `1/(k+h^v)` scalar everywhere; tests parametrise k over {1,2,5,10}, never k=0 or k=-h^v
5. `elliptic_rmatrix_shadow.py:716-777` kzb_connection_sl2 returns `Omega/(2πi(k+h^v))` without k prefix
6. `homfly_shadow_yangian_engine.py:551-577` `shadow_classical_r_matrix(N)` returns just `Omega`
7. `theorem_bethe_mc_engine.py` — 4 sites with `r(z) = Omega/z`
8. `theorem_cs_knot_invariant_engine.py` — bare form in CS knot invariant chain
9. `theorem_open_closed_rectification_engine.py` — `"r_matrix": "Omega/z"` string literal
10. `twisted_holography_engine.py` + `bethe_ansatz_shadow.py` — bare form in holographic/Bethe layers

**These are NOT caught by 119K passing tests because none parametrise k=0 on the r-matrix.**

**Verified CLEAN (NOT AP128)**:
- `kappa_cross_verification.py` + test — gold standard, 5 methods × 11 families, critical-level checks
- `rmatrix_landscape.py` + test — both engine and test use correct `r(z) = k*Omega/z`
- `theorem_pva_classical_r_matrix_engine.py` + test — AP19 d-log absorption verified
- `theorem_kappa_en_invariance_engine.py` — three-proof framework with independent computation

**Vol III test file** `test_cy_to_chiral_functor.py:420-425` asserting κ(K3)=24 is NOT AP128 — the rank-24 Niemeier-lattice argument is a literature-derived independent anchor.

**Priority 1 fix**: add `pytest -k "k_zero"` mandatory boundary tests for every r-matrix engine. `assert r_matrix(k=0) == zero`. This single test pattern catches the entire sub-epidemic.

## Segment 3: Part II Shadow Tower (2 agents)

### Angle 6 — Shadow Tower hostile attack

**Verdict: CLASSIFICATION-WELL-DEFINED with ONE localized AP-VIOLATION.**

**Definitions verified**:
- `def:shadow-postnikov-tower` (`higher_genus_modular_koszul.tex:11589-11642`): explicit inverse limit construction
- `def:shadow-algebra:11825`: `A^sh = H_•(Def^cyc_mod(A))`
- `def:shadow-depth-classification:15713-15788`: 4-class G/L/C/M table

**`thm:mc2-bar-intrinsic` VERIFIED ALL-ARITY** (L3303-3357). Batch 1 Angle 7 concern resolved: the all-arity limit IS proved via inverse limit of finite truncations; uniform-weight tag is present in clause (ii) for the scalar trace claim.

**Δ = 8·κ·S_4 VERIFIED LINEAR in κ** at 19+ usage sites across `lattice_foundations`, `free_fields`, `kac_moody`, `w_algebras_deep`, `bershadsky_polyakov`, `landscape_census`, `preface`. AP21 clean. Δ=0 ⇔ finite tower confirmed.

**AP59 VERIFIED ENFORCED** in dedicated chapter `chapters/theory/three_invariants.tex`. βγ archetype (p=1, k=0, r=4) documented verbatim.

**AP131 VIOLATION (localized)**: the symbol `d_gen` (generating depth) is **ABSENT from all chapter files**. Only `d_alg` exists. Vol I CLAUDE.md AP131 mandates distinguishing d_gen (arity at which m_k determined recursively) from d_alg (tower termination). The conceptual distinction is upheld in prose (Vir → class M with infinite tower), but the symbolic marker `d_gen` is not instantiated. **Definitional gap** — any agent grepping for "d_gen" will find nothing.

**Class W**: defined via `rem:wild-quiver-boundary:15790-15819` with Kronecker K_{m≥3}, DT invariant replacement, 89-test compute backing. Honestly disclosed.

**Heisenberg G-class vs physics atom role**: CONSISTENT. G-class means r_max=2 (tower terminates at κ alone). This IS the Brown-Henneaux regime stated at L11716-11719. The "atom" status is precisely why Heisenberg sits at G.

### Angle 7 — G/L/C/M classification verification

**Classification table**: 14 families verified against census `tab:shadow-tower-census` (L236-295) and `tab:shadow-invariants-landscape` (L630-676).

**Two new classes discovered beyond CLAUDE.md G/L/C/M**:
- **M\***: W_∞ limit with 1-dim cyclic line (L280) — not in CLAUDE.md
- **W**: wild (Kronecker K_{m≥3}) — not in CLAUDE.md, introduced in census

CLAUDE.md update needed: mention M* and W.

**10 families lack any shadow-class row** (census gaps):
1. **BP_k (Bershadsky-Polyakov)** — in Master Table L142-145 but ABSENT from `tab:shadow-tower-census` — **MOST SERIOUS**
2. Critical-level KM V_{-h^v}(g) — discussed in remark but not tabulated
3. Virasoro minimal models c_{p,q} — never appears
4. Vir at c=13 self-dual — no row
5. W_N at degenerate c — no rows
6. SVir / N=1 / N=2 super-Virasoro — never appears
7. Symplectic fermion — parenthetical only
8. Triplet W(p) logarithmic — flagged but not classified
9. Quantum lattice V_Λ^{N,q} — no class
10. Admissible-level KM L_{p/q-2}(g) — status "open", no class

**AP131 check**: census uses ONLY r_max (= d_alg). Zero hits for `d_gen`, `generating depth` across the census. Confirms Angle 6's AP131 violation.

**D-flags (drift)**:
- D1: CLAUDE.md HZ is incomplete on C-class (census extends to bc ghosts)
- D2: M* subclass exists in census but not CLAUDE.md
- D3: W class exists in census but not CLAUDE.md
- D4: BP_k appears in Master Table with data but is absent from shadow tower table
- D5: No critical-level KM row

## Segment 4: Cross-volume preface + intro consistency (2 agents)

### Angle 8 — Cross-volume 6-file × 8-dimension matrix

**Files read**: Vol I preface (3619 lines, post-F7), Vol I intro (2447), Vol II preface (793), Vol II intro (2358), Vol III preface (304), Vol III intro (328).

**Classification of inconsistencies**:

**CONTRADICTION-1 (boundary-bulk thesis hedging)**: Vol I preface is hedged (post-F7); Vol I intro AND Vol II preface contain IDENTICAL unhedged thesis paragraphs. F7 propagation lag confirmed.

**CONTRADICTION-2 (Theorem H scope)**: Vol I preface (L68-71) states "at generic level" + critical-level caveat; Vol II preface (L302-308) asserts H bound as "the bulk algebra Z^der_ch(Vir_c) itself" without generic-level qualifier.

**CONTRADICTION-3 (`\begin{principle}` environment)**: Vol I intro `princ:boundary-bulk-thesis` (L645-743) still uses `\begin{principle}` for conjectural content (AP40 violation). F13 unfixed.

**DRIFT-1 (Heisenberg framing)**: THREE DIFFERENT framings across 6 texts:
- Vol I preface: "atom" (unconditional verification case)
- Vol I intro `rem:two-strata` (L26-34): "commutative extreme" (paired with "Yangian as ordered extreme")
- Vol II preface: class G with κ = k
The Vol I intro framing COLLIDES with CLAUDE.md AP108 ("Heisenberg = CG opening, NOT the atom").

**DRIFT-2 (Seven Faces count)**:
- Vol I intro `rem:five-facets-seven-faces` (L847-859): introduces **5-facet vs 7-face** distinction
- Vol I preface: 6 names listed implicitly
- Vol II preface (L657-666): 7 explicit names (different list from Vol I!)
- Vol I and Vol II 7-face lists do NOT name-match each other

**DRIFT-3 (genus-0 tautology refs)**: Vol I intro L261-264 and L685-687 still contain the F14 tautology references.

**PROPAGATION LAG-1**: F7 preface weakening incomplete — Vol I intro, Vol II preface, Vol III preface ALL still carry the unhedged thesis.

**PROPAGATION LAG-2 (κ subscript)**: **NEW κ_MacMahon subscript** in Vol III intro L122 — `κ_{MacMahon} = χ/2 = -100`. This subscript is NOT in the approved AP113 set `{ch, cat, BKM, fiber}`. New leak.

**Vol III preface L271-279 CONFIRMED as most egregious overclaim**: "Volumes I and II prove... reconstructs gravity" with four "proves" + "is incarnated" + "is the universal reconstruction functor", all referring to the conjectural part. Direct contradiction with Vol I preface L51-74.

### Angle 9 — Within-volume consistency

**Vol I: MAJOR MISMATCH** (preface hedged, intro unhedged). Specific mismatches:
- F13 still open: `\begin{principle}[boundary-bulk thesis]` in intro
- F14 still open: L261-264 and L685-687 tautology refs
- Boundary-bulk thesis: preface "conjectured to be", intro "IS"
- Seven Faces: preface omits, intro has 7 in Part V
- Heisenberg: preface "atom", intro "commutative extreme"

**Vol II: REVERSE MISMATCH** (preface unhedged, intro silent on thesis). F15 confirmed at 4 sites (L29-45, L255-257, L279-281, L295-299). Intro correctly hedges MC5 at L1569-1571 but preface is silent on MC5 entirely. Drinfeld double notation inconsistent across preface (`A ⋈ A^!`, `A ⋈ A^!_line`, `A ⋈ A^!_∞`).

**Vol III: MINOR MISMATCH** (2 specific defects).
- **HZ-7 violation**: intro L238, L240, L241 use `\kappa_{BPS}` (FORBIDDEN subscript)
- Missing κ-spectrum definition in intro (preface L143-154 defines it; intro uses without defining)
- L10-17 inherits the unhedged reconstruction thesis — cross-volume propagation lag

## Segment 5: Standalone papers (1 agent)

### Angle 10 — Standalone audit

**18 standalones audited**.

**KEY DISCOVERY: standalone N5 owns the CORRECT Huang05 bibitem**. `N5_mc5_sewing.tex:865-868` contains:
```
Y.-Z. Huang, "Differential equations, duality and modular invariance",
CCM 7 (2005), 649-706
```
This is the CORRECT title/pagination for arXiv:math/0502533. The monograph `bibliography/references.tex:675-676` has the WRONG form ("Differential equations and intertwining operators, 375-400"). **N5 is the source of truth** — the fix direction is standalone → monograph (reverse propagation).

**4 Mok25 author misattributions in standalones**:
- `programme_summary.tex:2691` — "L. Mok" (wrong)
- `programme_summary_section1.tex:659` — "L. Mok" (wrong)
- `programme_summary_sections9_14.tex:697` — "L. Mok" (wrong)
- `survey_modular_koszul_duality_v2.tex:4838` — "D. Mok" (different wrong form)

**2 standalones have CORRECT "C.-P. Mok"** (propagation references):
- `classification_trichotomy.tex:507`
- `w3_holographic_datum.tex:560`

**N5 AP127 violation**: `\ref{chap:genus-complete}` at L180 — broken (no local phantomsection stub). Becomes `??` in standalone build.

**3 AP126 violations in standalones**:
- `three_parameter_hbar.tex:234` — literal "`r(z) = Omega/z`"
- `genus1_seven_faces.tex:695, 722` — bare Omega/z as q→0 limit

**`introduction_full_survey.tex`** has 8 AP127 hardcoded `Part~I/II/III/IV/V/VI` violations (L1722, L4610, L4792-4867, L5106). Most AP127-violating standalone.

**CFG25 in standalones**: ZERO. Clean. (Good news for the emergency triage — standalone layer is uncontaminated.)

**MC5 propagation verified clean**: 10+ MC5 mention sites in standalones (programme_summary, programme_summary_sections9_14, introduction_full_survey, survey_modular_koszul_duality, survey_modular_koszul_duality_v2, survey_track_a_compressed, survey_track_b_compressed, N5) all use the hedged form matching `editorial_constitution.tex:179`. **MC5 status reconciliation HAS propagated cleanly to standalones.**

**N1 definition-tautology check**: N1_koszul_meta uses its own local `def:chiral-koszul-morphism` (twisted-tensor acyclicity — the F4/F6-safe formulation per Batch 4 Angle 2). N1 is the ARCHITECTURAL CLEAN reference for the canonical definition rewrite.

## New findings F64-F75

**F64** — CFG25 is NOT fabricated (corrects F55). arXiv:2602.12412 is real Costello-Francis-Gwilliam 2026 paper "Chern-Simons factorization algebras and knot polynomials". Only the BIBITEM TITLE is wrong. Fix: title correction + per-cite content audit.

**F65** — Nafcha26 is ORPHAN (0 cites anywhere). Safe delete.

**F66** — Two distinct fabricated identities share CFG25 key: BIBITEM says "Costello-Francis-Gwilliam / Chiral Koszul duality"; Vol II FRONTIER.md:18 AND Vol III FRONTIER.md:18 say "Cliff-Gannon-Frenkel / universal chiral algebras and genus extension". The FRONTIER metadata version was not in Batch 7c.

**F67** — r-matrix AP128 sub-epidemic in 8+ compute engines. Mirror of the AP126 .tex epidemic that was never propagated to compute. `theorem_seven_face_categorification_engine.py`, `theorem_three_way_r_matrix_engine.py` (with 4 "perspective" sub-engines circularly agreeing on the wrong scalar), `quantum_rmatrix_barcomplex.py`, `theorem_genus1_seven_faces_engine.py` (6 sites), `elliptic_rmatrix_shadow.py`, `homfly_shadow_yangian_engine.py`, `theorem_bethe_mc_engine.py`, `theorem_cs_knot_invariant_engine.py`. None caught by 119K passing tests because no test parametrises k=0 on the r-matrix.

**F68** — FM5 live violation at `compute/lib/bc_exceptional_categorical_zeta_engine.py:750` with `779247` in `_E8_SMALL_DIMS` list. Latent (not tested) but in a lookup returned by `e8_first_dims()`.

**F69** — Bar cohomology "new computation" AP128 cluster: tests explicitly frozen as "new computation from this engine" in sl_2 engine; likely propagates to sl_3, w_3, w_4, lattice engines.

**F70** — Six shadow classes, not four: G/L/C/M + M* + W. CLAUDE.md needs update.

**F71** — 10 families lack any shadow class row in landscape census. Most serious: BP_k (in Master Table with data but absent from shadow tower table).

**F72** — AP131 d_gen symbol ABSENT from ALL Vol I chapters. Only d_alg exists. Conceptual distinction upheld in prose (Vir→M) but symbolic marker missing — future agents grepping for "d_gen" will find nothing.

**F73** — Vol III intro L238-241 uses `κ_BPS` which is FORBIDDEN per HZ-7 / AP113. New HZ-7 violation beyond the 23 in `toroidal_elliptic.tex` from Batch 6.

**F74** — `κ_MacMahon` new subscript leak at Vol III intro L122. Not in approved set.

**F75** — Standalone N5 owns CORRECT Huang05 bibitem (L865-868). Source of truth for monograph Huang05 title fix — reverse propagation standalone→monograph.

## Batch 8 deliverable inventory (10 items)

1. **CFG25 title fix + per-cite audit** — change bibitem title to "Chern-Simons factorization algebras and knot polynomials"; review 9 citation sites for content mismatch
2. **Nafcha26 delete** — 0 cites, safe
3. **CFG25 FRONTIER.md metadata correction** — remove or correct "Cliff-Gannon-Frenkel" alias in Vol II + Vol III FRONTIER.md
4. **Strip 779247 from `_E8_SMALL_DIMS`** — regenerate from `weyl_dimension()` with [DC] comment
5. **Bar cohomology AP128 cleanup** — derive expected values independently for sl_2, sl_3, w_3, w_4, lattice engines; update test assertions
6. **r-matrix compute layer AP126 fix** — 8 engines need level prefix; add `k=0 → r=0` boundary tests
7. **AP131 `def:generating-depth`** — add to `three_invariants.tex` with explicit Vir/KM/W_N d_gen values
8. **BP_k + 9 other missing shadow class rows** — extend `tab:shadow-tower-census`; mark class and provide justification
9. **Vol I intro F13 + F14 fix** — rename `\begin{principle}` → `\begin{conjecture}`; replace tautology references
10. **standalone N5 Huang05 → monograph** — reverse-propagate correct title to `bibliography/references.tex:675-676`

## Open items for Batch 9+

- Per-cite content audit for CFG25 (9 sites) — determine whether to keep (with corrected title) or replace with FG12 based on each site's actual context (chiral Koszul duality vs Chern-Simons factorization)
- κ_MacMahon scope: is it intentional (new subscript) or error (should be κ_cat)?
- Heisenberg framing reconciliation: atom vs CG opening vs commutative extreme (3 texts, 3 framings)
- Vol III preface L271-279 atomic hedging (F37)
- Drinfeld double notation harmonization across Vol II preface (3 different forms)
- Compute layer r-matrix sweep priority ordering (8 engines)
- BP_k shadow class determination: census data points to M-class (κ+κ'=196, tower doesn't terminate)
