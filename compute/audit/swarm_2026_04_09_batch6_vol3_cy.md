# Adversarial Swarm 2026-04-09/10 — Batch 6: Vol III CY Programme

**Scope.** 10 agents, 10 distinct angles on Vol III (`/Users/raeez/calabi-yau-quantum-groups`) — the Calabi-Yau / Quantum Groups / BPS Algebras volume. First adversarial pass over this volume. Coordination via `reconciliation_learnings.md`.

## Master verdict

**Vol III is epistemically the most honest of the three volumes** (everything conditional-by-default per AP-CY14), BUT suffers from three classes of problems:
1. **Critical citation gaps** — the three most-adjacent literature precursors (Kapranov 2015, Kapustin-Rozansky-Saulina 2009, Costello-Gaiotto 2018/2019) are NOT cited in Vol III
2. **Inverted stub status** — 5 chapters flagged as stubs in CLAUDE.md are actually developed (152-229 lines with real theorems) but commented out in main.tex, EXCLUDING ~705 lines of content from the build
3. **κ-spectrum promise not delivered** — Part II "CY Character Datum" fails to define κ_fiber or give a formal definition of κ_BKM; the κ-spectrum lives in Part III

## 10-angle findings

### Angle 1 — CY → chiral functor Φ

**Verdict: UNDERSPECIFIED.**

- Definition at `cy_to_chiral.tex:32-46` (`thm:cy-to-chiral`, ProvedHere at d=2, PROGRAMME at d=3)
- **Φ is defined only on OBJECTS, not morphisms.** No `\Phi(f)` anywhere. Functoriality asserted, never exhibited.
- Four-step construction (cyclic A∞ → Lie conformal → factorization envelope → E_2 framing → quantization) has a **hidden circularity in Step 1** flagged in Vol III's own `notes/audit_red3_cy_to_chiral.md:19-57` ("λ-bracket simultaneously defined by and verified from Jacobi"); proposed fix (Kac affinization) not yet done.
- **Φ(D^b Coh(K3×E)) is explicitly NOT constructed.** `quantum_chiral_algebras.tex:32` admits: "κ_BKM = 5 is an observation matching the Borcherds lift weight, NOT a computation from Vol I's definition of κ_ch."
- **CRITICAL CITATION GAPS**: Kapranov 2015 "Chiral algebras from Calabi-Yau manifolds" (the direct precursor to Φ) — **ZERO hits** in Vol III. Kapustin-Rozansky-Saulina 2009, Costello-Creutzig-Gaiotto 2019, Oh-Yu 2023 — **ZERO hits each**. Without these citations the novelty claim is unverifiable.
- **AP128 trap**: `test_cy_to_chiral_functor.py:420-425` asserts "Φ(K3): κ=24" with docstring "kappa = 24 (lattice VOA rank 24)"; this is κ_fiber, but the function name and prose conflicts with `fukaya_categories.tex:143` "κ_cat(Φ(K3)) = 2". Reconcilable only via κ-spectrum convention but creates a test/prose mislabeling risk.

### Angle 2 — AP113 κ-spectrum compliance

**Verdict: PARTIAL COMPLIANCE with localized FAILURE in `toroidal_elliptic.tex`.**

- Approved subscripts: 695 hits (`\kappa_{ch}`=495, `\kappa_{cat}`=103, `\kappa_{BKM}`=72, `\kappa_{fiber}`=25)
- **60 FORBIDDEN subscript hits across 6 files**:
  - **`toroidal_elliptic.tex`: 23 instances** of `\kappa_{BPS}`, `\kappa_{global}`, `\kappa_{eff}` (lines 2270, 3063, 3099, 3111, 3129, 3399, 3403, 3407, 3453, 3459, 3875, 4393, 4394, 4396, 4446, 4897, 4930, 4935, 4979, 5030, 5032, 5429, 5431) — should be `\kappa_{BKM}`
  - `cy_holographic_datum_master.tex:482, 979, 983` (3 forbidden)
  - `introduction.tex:238, 240` (2 `\kappa_{BPS}`)
  - `working_notes.tex`: 18
  - `notes/physics_anomaly_cancellation.tex`: 13
  - `notes/theory_qvcg_koszul.tex`: 1
- Chapter files have effectively zero bare `\kappa` (only metacommentary references to AP113 itself)
- **Fix**: global rename `\kappa_{BPS} → \kappa_{BKM}` in `toroidal_elliptic.tex`; fix `\kappa_{eff}`, `\kappa_{tot}` to approved subscripts elsewhere

### Angle 3 — κ_{BKM}(K3×E) = 5 verification

**Verdict: CORRECT-BUT-DEFINITIONAL.**

Arithmetic chain verified:
- wt(Φ_10) = 10 (Igusa 1962) ✓
- Φ_10 = const·(Δ_5)² (Gritsenko-Nikulin 1997) ✓
- wt(Δ_5) = c(0)/2 = 5 (Borcherds 1995 weight formula) ✓
- κ_BKM(K3×E) := wt(Δ_5) = 5 ✓

**BUT**: this is a **definition by convention**, not a derivation from a chiral-algebra modular characteristic. The operative definition is "κ_{BKM}(X) := ½·wt(Borcherds automorphic form controlling the BKM denominator of X)". There is no axiomatic Vol I object κ_{BKM} that one then computes to be 5.

Vol III is explicit: `k3_times_e.tex:167`: "an observation matching the Borcherds lift weight formula, **not a computation from the Volume I definition of κ_ch**". Also `modular_trace.tex:60`: "conjectural as a modular characteristic".

**Vol I CLAUDE.md C21** ("κ_{BKM}(K3×E) = 5") conceals this definitional status. Recommend parenthetical "(definition; A_{K3×E} not constructed, see Vol III k3_times_e.tex:167)".

### Angle 4 — BPS gap audit

**Verdict: HONESTLY-FLAGGED in 5 locations.**

- The string "BPS gap" does NOT appear in any Vol III .tex — it's memory-file shorthand
- Content exists under different names:
  - `thm:shadow-siegel-gap` at `toroidal_elliptic.tex:4365-4456` (ProvedHere) — **proves the gap EXISTS via four obstructions O1-O4** (categorical, kappa-mismatch, second-quantization, Schottky). This is a **genuinely new NEGATIVE result**.
  - `rem:second-quantization-gap` at `toroidal_elliptic.tex:3080-3090`
  - `conj:kappa-bps-universality-vol3` at `toroidal_elliptic.tex:3446` (Conjectured)
  - `introduction.tex:208`: "observation, not a theorem"
  - `modular_trace.tex:46`: "conjectural as a modular characteristic"
  - CLAUDE.md AP-CY8: explicit warning
- Gap classification: (b) between chiral algebras and DT/BPS counts, mediated by missing A_{K3×E} and missing second-quantization functor
- **Literature gap**: Kontsevich-Soibelman 2008 NOT cited anywhere in Vol III. Joyce-Song 2011 NOT cited. Davison 2017 cited ONCE as "Davison-Meinhardt PBW filtration" without engaging the integrality conjecture.
- **Closure status**: FUNDAMENTALLY OPEN. CY-A_3 prerequisite is conjectural.
- Does κ_BKM(K3×E)=5 depend on the gap closing? **YES.** The value 5 is computed from Borcherds lift weight, not from a chiral algebra computation. The identification IS the gap.

### Angle 5 — Stub chapter detection

**Verdict: STUBS-HIDDEN (INVERTED variant).**

- **Zero stubs by AP114 criteria** in the actual .tex files
- Smallest chapter: `modular_trace.tex` at 150 lines with 4 formal environments
- CLAUDE.md line 11 lists "5 genuine stubs": `quantum_groups_foundations` (24 lines), `derived_categories_cy` (27), `geometric_langlands` (28), `matrix_factorizations` (29), `modular_koszul_bridge` (13)
- **All 5 line counts are stale**: actual current lengths are 229, 153, 175, 152, 225 — 5x to 17x larger
- **The chapters were DEVELOPED in waves 1-9 but never re-`\input{}`-ed in `main.tex`**
- `main.tex:451-493` has STUB-AUDIT 2026-04-08 comment-outs citing the stale line counts
- **~705 lines of developed content are SILENTLY EXCLUDED from the build**
- **Broken forward reference**: `fukaya_categories.tex:500` writes `Chapter~\ref{ch:derived-cy}` pointing to the commented-out chapter → emits `[?]` in build
- **Fix**: re-enable the 5 chapters in main.tex; update CLAUDE.md to reflect current line counts
- This is the OPPOSITE of stub inflation — it's **stub DEFLATION**: Vol III CLAUDE.md misrepresents its own coverage by ~14-15 pages

### Angle 6 — AP-CY1 through AP-CY8 compliance

**Verdict: CY1-CY5, CY8 COMPLIANT; CY6/CY14 VIOLATED (2 confirmed); CY7 VIOLATED (prose conflation).**

Per `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:39-48`:
| # | Summary | Status |
|---|---|---|
| CY1 | CY dimension d ≠ complex dim n | COMPLIANT |
| CY2 | CY trace lives in HC^-_d, not HH_d→k | COMPLIANT |
| CY3 | E_2 ≠ commutative (braiding non-symmetric) | COMPLIANT |
| CY4 | Drinfeld center Z(C) ≠ chiral derived center Z^der_ch(A) | COMPLIANT (116 hits, dedicated chapter) |
| CY5 | Kazhdan-Lusztig requires root of unity | COMPLIANT |
| **CY6/CY14** | **A_X for CY3 does NOT exist; result depending on A_X at d=3 MUST be Conditional + name CY-A_3** | **2 VIOLATIONS** |
| **CY7** | **CoHA ≠ E_1-chiral algebra** | **Prose violation** |
| CY8 | Borcherds denominator ≠ bar Euler product; K3×E is observation, not theorem | COMPLIANT |

**AP-CY6 violations found**:
1. `quantum_chiral_algebras.tex:161-174` — `\begin{theorem}[MO/chiral R-matrix comparison]` with `\ClaimStatusProvedHere` references A_X for CY threefold. Should be `\begin{conjecture}` + `\ClaimStatusConditional` + name CY-A_3.
2. `toric_cy3_coha.tex:257-267` — `thm:wall-crossing-mc` ProvedHere uses Θ_ζ ∈ MC(g^mod_{A_X}) for toric CY3. Same violation.

**AP-CY7 violations**:
- `toric_cy3_coha.tex:67,74` — "the toric fan is the root datum of the quantum vertex chiral group G(X)" / "CoHA = positive half of G(X) = E_1-chiral sector"

**Proposed Vol III HOT ZONE (HZ3-1 through HZ3-10)** — full 10-rule Vol III analog of Vol I HZ-1..10, ranked by recurrence + blast radius. HZ3-1 = AP-CY6 (unconstructed object in theorem); HZ3-2 = AP113 bare κ; HZ3-3 = AP-CY7 CoHA conflation; HZ3-4 = AP-CY11 conditional transitivity; HZ3-5 = AP-CY8 Borcherds denominator framing; HZ3-6 = AP-CY3 E_2≠E_∞; HZ3-7 = AP-CY10 flop ≠ Koszul dual; HZ3-8 = AP-CY13 cross-volume Part-number staleness; HZ3-9 = AP-CY17 MF(W) dimension; HZ3-10 = AP-CY12 shadow class.

### Angle 7 — Seven Faces of r_CY (Part IV)

**Verdict: PARALLEL-TO-VOLS-I-II + CY-SPECIFIC-NEW-FACES + MASTER-IS-CONJECTURE.**

- Part IV exists at `main.tex:468-480` (`part:connections`); developed, not a stub
- Master: `conj:cy-seven-face-master` at `cy_holographic_datum_master.tex:829` — **\begin{conjecture}**, NOT theorem (contra Vol I/II which have theorems)
- **Seven faces are DIFFERENT from Vol I/II**:

| # | Vol III face | Status |
|---|---|---|
| F1 | CY bar-cobar twisting | ProvedHere (d=2); conj (d=3) — parallel to Vol I F1 |
| F2 | **CoHA / perverse coherent sheaves** | Conjectured generally; SV proved for C^3 — **genuinely new** |
| F3 | Classical CY Poisson coisson | ProvedHere (d=2); conj (d=3) — parallel to Vol I F3 |
| F4 | **Maulik-Okounkov R-matrix for K3×E** | Conjectured — **genuinely new** |
| F5 | Affine super Yangian for toric CY3 | ProvedElsewhere (RSYZ) — CY-specialized |
| F6 | Elliptic Sklyanin/Felder E_{q,p}(sl_2) | ProvedHere (sl_2 only); conj (general) — CY-elliptic |
| F7 | **CY_3 Gaudin from collision residues with DT/PT Bethe roots** | ProvedHere (C^3 only); conj (general) — **genuinely new** |

- F2, F4, F7 are genuinely new face content unique to Vol III
- **Vol III is more honest than Vol I/II**: individual faces carry split per-d / per-example status tags consistent with AP-CY14; master is explicitly conjectural
- **AP126 violations**: L508 and L779 write bare `Ω/z` Yangian r-matrices without level prefix
- **Stale "Vol I Part III" reference** at L935 (should be Part V)
- **Phantom-stub cross-volume label inconsistency**: L17-18 reference `thm:vol1-seven-face-master` but the actual Vol I label is `thm:seven-faces-master`
- Zero AP125 violations within the chapter

### Angle 8 — CY Character Datum (Part II)

**Verdict: UNDERDEFINED.**

Specific failures:
1. **κ_fiber is UNDEFINED anywhere in Vol III** — zero matches across `chapters/theory/`. CLAUDE.md advertises it; manuscript ships `kappa_BPS` (forbidden) instead, only for K3×E
2. **κ_BKM has no formal definition**, only example values and a "weight of Siegel form" gloss
3. **kappa-spectrum definition is exiled to Part III** (`toroidal_elliptic.tex:3021`), not Part II where it belongs
4. **No meta-theorem relating the four kappas**
5. **Three sections of `modular_trace.tex:143-150` are EMPTY section headers**: `sec:genus-gw`, `sec:cy-shadow-tower`, `sec:cy-complementarity`
6. **No CY Theorem C analog** — the section that would house it is one of the empty headers
7. **Spectrum table inconsistency**: abstract claims {κ_ch, κ_cat, κ_BKM, κ_fiber} = {3, 2, 5, 24}; actual `toroidal_elliptic.tex:3050-3054` table writes all four as `kappa_ch` with different algebras (plus `kappa_BPS` for the fourth)
8. **MNOP 2006 NOT cited**; **Okounkov-Reshetikhin 2003 NOT cited**

**Definitions found**:
- `kappa_ch` at `modular_trace.tex:14` (`thm:cy-modular-characteristic`) — integer/rational, equals χ^CY
- `kappa_cat` at `braided_factorization.tex:256-269` (`def:braided-kappa`) — av(R_A(z)), integer
- `kappa_BKM` — no `\def`, only example values
- `kappa_fiber` — absent

### Angle 9 — CY Landscape (Part III)

**Verdict: PARTIAL-HIDDEN.**

- **No `landscape_census_cy.tex` analog exists.** Vol I has 4022-line `landscape_census.tex`; Vol III has nothing equivalent
- 4 active example chapters: `toroidal_elliptic.tex` (5811 lines), `toric_cy3_coha.tex` (393), `fukaya_categories.tex` (565), `quantum_group_reps.tex` (585)
- K3 is the Vol III CG opening (six independent κ paths, most-developed family)
- K3×E is the climax (where κ_BKM=5 lives)

**Families COVERED**: K3, T^4, elliptic curve, toric CY3 (C^3, conifold, local P^2, local P^1×P^1), K3×E (conditional)

**Families ABSENT**:
- **Quintic X_5 ⊂ P^4** — the paradigmatic compact CY3 — gets **18 lines** as a Fukaya example in Part III; substantive treatment exiled to Part IV `bar_cobar_bridge.tex:308-345`
- Enriques × E (mentioned only)
- ADE surfaces (no own chapter)
- K3 × K3, CY4, fourfolds — entirely absent
- Ginzburg algebras / noncommutative CY — absent
- Symplectic resolutions / quiver varieties — absent
- MF(W) Landau-Ginzburg — stub commented out

**Landscape gaps where Φ is DEFINED but not COMPUTED**:
1. Quintic — Phi defined via Fuk(X_5), kappa predicted, only 18 lines
2. General toric CY3 with compact 4-cycles — excluded by RSYZ hypothesis
3. Wrapped Fukaya / non-compact CY — flagged but not executed
4. ALL d=3 families — conditional on CY-A_3

**Smoking gun**: the most famous CY3 (quintic) has no Part III chapter, and the gap is not acknowledged at Part III level.

**AP-CY6 violation in landscape**: `prop:fukaya-phi-status` uses `\ClaimStatusProvedHere` instead of Conditional for a d=3 statement.

### Angle 10 — Novelty vs literature

**Verdict: MIXED (GENUINELY-NEW-PROGRAMME ∧ UNCITED-OVERLAP).**

- ~30% genuinely new
- ~50% repackaging existing CY-to-VOA literature
- ~20% UNCITED OVERLAP

**Vol III's most distinctive contributions**:
1. **The κ-spectrum {κ_ch, κ_BKM, κ_cat, κ_fiber}** — the recognition that "kappa" splits into four distinct invariants for one CY is not in any baseline
2. **Shadow-Siegel gap theorem** — the shadow tower of K3×E does NOT produce Φ_10, with four explicit obstructions O1-O4. This is a **genuinely new NEGATIVE result** that deserves headline status
3. **Bar-cobar lens on CoHA** — new framing

**UNCITED OVERLAP (serious)**:
1. **Kapustin-Rozansky-Saulina 2009** (arXiv:0810.5415) — NOT cited. Vol III's Conjecture CY-C is **literally the KRS conjecture from 2009** with A_C in place of KRS's 3D TQFT. Most problematic non-citation.
2. **Costello-Gaiotto 2018** (arXiv:1804.06460, "VOAs and 3d N=4 gauge theories") — NOT cited. **This is the foundational paper for Vol III's Φ functor applied to Higgs branches.** MOST SERIOUS citation gap.
3. **Davison 2017** (arXiv:1602.02110, integrality conjecture) — NOT cited.
4. **Kapranov 2015** "Chiral algebras from Calabi-Yau manifolds" — NOT cited. Direct precursor to Φ.
5. **Borcherds 1995** product-formula paper — under-cited (only 1992 Monstrous Moonshine is in bib)
6. **MNOP 2006** (Maulik-Nekrasov-Okounkov-Pandharipande GW/DT correspondence) — NOT cited
7. **Okounkov-Reshetikhin 2003** — NOT cited

**CITES-FAITHFULLY**:
- Schiffmann-Vasserot 2013/2020 (CoHA → Yangian) — proper bibitem and attribution
- Maulik-Okounkov 2019 stable envelopes — proper bibitem
- Kontsevich-Soibelman 2008/2009 (motivic DT) — loose attribution (no specific bibitem)

## Critical cross-batch findings

### F27 — Vol III κ-spectrum promise undelivered

The CLAUDE.md κ-spectrum table {ch, cat, BKM, fiber} is promised in Part II but the manuscript delivers only {ch, cat}. `κ_fiber` is UNDEFINED (0 hits) and `κ_BKM` has no formal definition. The "four kappa split" idea — the genuinely-new Vol III contribution — is architecturally undercooked at the definitional level.

### F28 — Vol III stub status inverted

MEMORY.md "12 stubs" and CLAUDE.md "5 genuine stubs" are stale. The 5 flagged "stubs" are actually 152-229-line developed chapters with theorems. They're commented out in main.tex with stale STUB-AUDIT banners. **~705 lines of substantive content excluded from the build.** `fukaya_categories.tex:500` has broken `\ref{ch:derived-cy}` pointing to a commented chapter.

### F29 — Costello-Gaiotto 2018 uncited

The Costello-Gaiotto VOA construction `arXiv:1804.06460` is the direct analog of Vol III's Φ functor applied to Higgs branches. **Not cited anywhere in Vol III.** This is a novelty overclaim: the "boundary VOA from CY" identification is headline CG19 content that Vol III presents as its own.

### F30 — Conjecture CY-C is Kapustin-Rozansky-Saulina 2009

Vol III's Conjecture CY-C ("Rep_q(g) ≃ Rep^{E_2}(A_C)") is literally the KRS conjecture from 2009 with A_C in place of KRS's 3D TQFT. **KRS 2009 is not cited.** Novelty overclaim.

### F31 — 2 AP-CY6 theorem-environment violations

`quantum_chiral_algebras.tex:161-174` (`thm:mo-chiral-rmatrix`) and `toric_cy3_coha.tex:257-267` (`thm:wall-crossing-mc`) are both marked `\ClaimStatusProvedHere` but reference A_X for CY3 without `\ClaimStatusConditional` or naming the CY-A_3 dependency.

### F32 — Vol III own internal red-team flagged Φ Step 1 circularity

`notes/audit_red3_cy_to_chiral.md:19-57` flags a hidden circularity in Step 1 of Φ construction (λ-bracket simultaneously defined by and verified from Jacobi). Vol III's own audit identifies this; the fix (Kac affinization) is proposed but not yet applied.

### F33 — Shadow-Siegel gap theorem deserves headline status

`thm:shadow-siegel-gap` at `toroidal_elliptic.tex:4365-4456` is a genuinely new NEGATIVE result: proves that the shadow obstruction tower of K3×E does NOT produce the Igusa cusp form Φ_10, with four explicit obstructions O1-O4. This is the kind of "false bridge falsified" output that no existing literature provides. Currently buried in Part III as a sub-result; should be promoted to a headline theorem of Vol III.

### F34 — 23 `\kappa_{BPS}` violations in toroidal_elliptic.tex

Heavy concentration of AP113 violations in a single file. Should be mass-renamed `\kappa_{BPS} → \kappa_{BKM}` (or if BPS semantics differ, formally add `BPS` to the approved subscript set with justification).

## Batch 6 deliverable inventory

All 10 angles produced actionable findings:

| # | Target | Deliverable | Ready? |
|---|---|---|---|
| 1 | Φ functor underspecified | 5 concrete fixes (morphism def, Step 1 citation, 4 missing bibitems, AP113 test label) | ✅ |
| 2 | AP113 sweep (23 `\kappa_{BPS}` + 37 others) | Rename plan | ✅ |
| 3 | κ_BKM(K3×E)=5 definitional status | Vol I C21 parenthetical fix | ✅ |
| 4 | BPS gap honestly flagged | 3 missing KS/Joyce-Song/Davison bibitems | ✅ |
| 5 | Stub status inverted | Re-enable 5 chapters in main.tex + fix `\ref{ch:derived-cy}` + update CLAUDE.md | ✅ |
| 6 | AP-CY6 2 violations + HOT ZONE proposal | 2 theorem→conjecture rewrites + HZ3-1..10 | ✅ |
| 7 | Part IV Seven Faces: 2 AP126 + stale Part III ref + phantom labels | 4 fixes | ✅ |
| 8 | Part II κ-spectrum undelivered | Write `def:kappa-fiber`, formal `def:kappa-BKM`, move `def:kappa-spectrum` to Part II, fill 3 empty sections, write CY Theorem C analog | ✅ |
| 9 | Part III landscape partial-hidden | Create `landscape_census_cy.tex`, promote quintic to own chapter, add Part III "out of scope" preamble | ✅ |
| 10 | Novelty overclaim + 7 missing citations | Add KRS09, CG18, Davison17, Kapranov15, Borcherds95, MNOP06, Okounkov-Reshetikhin03 bibitems + comparison remarks | ✅ |

## Open items for Batch 7+

- **Conjecture CY-C vs KRS 2009 structural comparison** — write out the exact correspondence and decide whether CY-C is a restatement or a genuine extension
- **Shadow-Siegel gap promotion** — how to elevate the genuinely-new negative result to headline status
- **Vol III κ-spectrum definitional audit** — write formal definitions for κ_fiber, κ_BKM that make Part II actually deliver its κ-spectrum promise
- **CY Theorem C analog** — construct the CY version of Koszul complementarity (currently an empty section)
- **Quintic CY3 chapter** — promote from Fukaya example to own chapter; compute Φ(D^b Fuk(X_5)) explicitly or flag CY-A_3 dependency
- **CY4 coverage** — decide if Vol III scope includes CY4 or explicitly excludes it
- **Φ Step 1 Kac affinization repair** — execute the fix proposed in `notes/audit_red3_cy_to_chiral.md`
