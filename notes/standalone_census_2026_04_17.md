# Standalone Programme Census (2026-04-17)

Cross-volume inventory of all standalone `.tex` documents across the three
volumes of the modular Koszul duality programme. Produced under S10
reconstitution (no commit, no build).

Legend:
- P0 = ship-ready (title matches claim; reflects current theorem status).
- P1 = minor sync needed (small updates to scope qualifiers, label
  prefixes, or retraction notices).
- P2 = substantial rewrite (claim advertised stronger than current status;
  needs scope qualifiers or new proof paths inscribed).
- P3 = obsolete candidate for retirement (superseded by a versioned successor
  or covered by a chapter-internal file).
- CL = cover letter (not a theorem document).

All authors: Raeez Lorgat.

## Part A. Volume I standalones (54 files)

Directory `/Users/raeez/chiral-bar-cobar/standalone/`.

| # | File | LC | Last hash / date | Primary advertisement | Status of primary thm (per CLAUDE.md table) | Self-cont. | Canonical chapter counterpart | Tier | Supersession / notes |
|---|------|----|-----------------|----------------------|-----------|-----|-----|-----|-----|
| 1 | `analytic_sewing.tex` | 3315 | 98f1f767 2026-04-13 | Analytic sewing / HS-sewing unconditional | MC5 analytic PROVED | Y | `chapters/theory/analytic_sewing.tex` | P1 | MC5 chain-level class M healed 2026-04-16 in weight-completed cat; needs addendum. |
| 2 | `arithmetic_shadows.tex` | 1296 | 072e55b1 2026-04-13 | Kummer-Bernoulli arithmetic of Z_g, S_r | CONJECTURAL duality; primes {691, 3617} PROVED through r=11 | Y | `z_g_kummer_bernoulli_platonic.tex` / `shadow_tower_higher_coefficients.tex` | P2 | Needs Beilinson-rectification of B88, B92 retractions (1423, 3067, 23, 43, 419 retracted to Riccati-arithmetic). |
| 3 | `bp_self_duality.tex` | 857 | f87cca83 2026-04-17 | BP Koszul conductor K = 196 (Arakawa convention) | PROVED (polynomial identity) | Y | `chapters/examples/bershadsky_polyakov.tex` | P0 | Arakawa convention caveat inscribed; Vol II FL-convention cross-check noted. |
| 4 | `chiral_chern_weil.tex` | 2101 | f87cca83 2026-04-17 | Chiral Chern--Weil + BRST ghost identity | CHAPTER-QUALITY (wave14 reconstitute) | Y | `chiral_chern_weil_brst_conductor.tex` (chapter target) | P1 | Target chapter exists; needs final inscription pass. |
| 5 | `classification.tex` | 1442 | 557bbc06 2026-04-17 | G/L/C/M shadow tables | PROVED | Y | `chapters/theory/classification.tex` | P0 | |
| 6 | `classification_trichotomy.tex` | 756 | 557bbc06 2026-04-17 | Three invariants / four shadow classes | PROVED | Y | `chapters/theory/classification.tex` | P0 | Complementary to #5; decide which is canonical. |
| 7 | `computations.tex` | 853 | 07c7b9f0 2026-04-13 | Genus-2 W_3 free energy / gravitational coproduct | δF_2(W_3) = (c+204)/(16c) PROVED (2026-04-16) | Y | `multi_weight_genus_expansion.tex` | P1 | Updated formula (`prop:delta-f-cross-w3-g2`) not yet reflected. |
| 8 | `cover_letter_garland_lepowsky.tex` | 58 | 5052fa65 2026-04-12 | (cover letter) | CL | N | — | CL | |
| 9 | `cover_letter_seven_faces.tex` | 70 | a0f29d9d 2026-04-13 | (cover letter) | CL | N | — | CL | |
| 10 | `cover_letter_shadow_towers.tex` | 57 | a0f29d9d 2026-04-13 | (cover letter) | CL | N | — | CL | |
| 11 | `cover_letter_virasoro_r_matrix.tex` | 62 | 857dfa33 2026-04-12 | (cover letter) | CL | N | — | CL | |
| 12 | `cy_quantum_groups_6d_hcs.tex` | 1134 | f87cca83 2026-04-17 | CY quantum groups + 6d hCS | PROVED (leading) | Y | Vol III `chapters/examples/cy3_6d_hcs.tex` | P1 | Should migrate to Vol III standalone dir (see scaffold). |
| 13 | `cy_to_chiral_functor.tex` | 1008 | c754a913 2026-04-14 | CY → chiral Φ functor | PROVED | Y | Vol III `chapters/theory/cy_to_chiral_functor.tex` | P1 | Vol III standalone mirror proposed. |
| 14 | `drinfeld_kohno_bridge.tex` | 1819 | f87cca83 2026-04-17 | DK bridge for chiral algebras | PROVED on Koszul locus (MC3 via five-family) | Y | `chapters/theory/mc3_five_family_platonic.tex` | P0 | Baxter retraction + five-family install complete. |
| 15 | `e1_primacy_ordered_bar.tex` | 2522 | f87cca83 2026-04-17 | Ordered bar B^ord + E_1 primacy | PROVED | Y | `chapters/theory/e1_primacy_ordered.tex` | P0 | |
| 16 | `editorial.tex` | 48 | eb521e03 2026-04-13 | (editorial cover) | CL | N | — | CL | |
| 17 | `en_chiral_operadic_circle.tex` | 3882 | f87cca83 2026-04-17 | E_n operadic circle + SC^{ch,top} | PROVED (heptagon in Vol II; SC^{ch,top} here) | Y | `chapters/theory/en_koszul_duality.tex` | P0 | Flagship survey. |
| 18 | `five_theorems_modular_koszul.tex` | 3108 | 99b3fb22 2026-04-17 | Five theorems A-D+H | PROVED (with scope qualifiers per CLAUDE.md) | Y | Introduction + Part I | P0 | |
| 19 | `garland_lepowsky.tex` | 1462 | f87cca83 2026-04-17 | Garland--Lepowsky chiral | PROVED | Y | `chapters/examples/garland_lepowsky.tex` | P0 | |
| 20 | `gaudin_from_collision.tex` | 784 | 557bbc06 2026-04-17 | Gaudin Hamiltonians from collision residue | PROVED (Face 7) | Y | `chapters/seven_faces/gaudin.tex` | P0 | |
| 21 | `genus1_seven_faces.tex` | 973 | e74693fc 2026-04-13 | Elliptic collision residues + KZB | PROVED leading ℏ for sl_2 | Y | `chapters/seven_faces/genus1.tex` | P1 | |
| 22 | `holographic_datum.tex` | 1412 | 557bbc06 2026-04-17 | Holographic modular Koszul datum | PROVED | Y | `chapters/theory/holographic_datum.tex` | P0 | |
| 23 | `introduction_full_survey.tex` | 5441 | 072e55b1 2026-04-13 | Full introduction survey | meta-document | Y | `chapters/frame/introduction.tex` | P2 | Pre-2026-04-16 wave; needs refresh of open-frontier list + retractions B86-B92. |
| 24 | `koszulness_fourteen_characterizations.tex` | 2610 | f87cca83 2026-04-17 | 14 Koszulness characterisations | PROVED (10 unconditional + 4 conditional) | Y | `chapters/theory/koszulness.tex` | P0 | |
| 25 | `multi_weight_cross_channel.tex` | 1385 | 98f1f767 2026-04-13 | Multi-weight genus + δF_g^cross | PROVED | Y | `multi_weight_genus_expansion.tex` | P1 | Needs δF_2(W_3) = (c+204)/(16c) inscription. |
| 26 | `N1_koszul_meta.tex` | 1103 | f87cca83 2026-04-17 | Koszulness moduli meta-level | PROVED | Y | — | P0 | N-series (note-series); keep as standalone. |
| 27 | `N2_mc3_all_types.tex` | 1181 | 5052fa65 2026-04-12 | DK thick generation all types | PROVED via five-family (supersedes Baxter) | Y | `mc3_five_family_platonic.tex` | P1 | Baxter retraction needs inscription; five-family replacement. |
| 28 | `N3_e1_primacy.tex` | 1038 | 557bbc06 2026-04-17 | E_1 primacy | PROVED | Y | `chapters/theory/e1_primacy_ordered.tex` | P0 | |
| 29 | `N4_mc4_completion.tex` | 915 | eb521e03 2026-04-13 | Strong completion tower | MC4^+ unconditional; MC4^0 NON-PRINCIPAL HOOK-TYPE partial (subregular W_n^{(2)} via PBW-Slodowy + Bell recursion). MC4^0 global landscape unconditional status RETRACTED 2026-04-17 per audit agent a44f + AP269 (no Wakimoto one-step SDR in manuscript; Feigin-Frenkel screening not chiral-coproduct-compatible per prop:ff-screening-coproduct-obstruction). | Y | — | P1 | Wakimoto / Feigin-Frenkel SDR claim DROPPED. MC4^0 scope: G/L via harmonic + standard-filtration inputs; C (βγ) conditional on support-property comparison; M (Vir/W_N) pro/J-adic/weight-completed ambient via MC5. Subregular inscribed; principal W_N hook-type (r ≤ N-3) CONJECTURAL via KRW03/Arakawa07 parabolic screenings. |
| 30 | `N5_mc5_theorem.tex` | 277 | f87cca83 2026-04-17 | MC5 theorem draft | PROVED in weight-completed cat | Y | `mc5_*` theorems | P0 | Recent (2026-04-16); wave14 reconstitute. |
| 31 | `N5b_analytic_sewing.tex` | 897 | 557bbc06 2026-04-17 | Analytic sewing companion | PROVED | Y | `chapters/theory/analytic_sewing.tex` | P1 | Overlap with #1; decide canonical. |
| 32 | `N6_shadow_formality.tex` | 704 | 5052fa65 2026-04-12 | Shadow tower = formality tower | PROVED (SC-formal iff class G) | Y | — | P0 | |
| 33 | `notation_index.tex` | 230 | eb521e03 2026-04-13 | Notation index | auto-generated | Y | — | P1 | Regenerate after 2026-04-17 macro additions. |
| 34 | `ordered_chiral_homology.tex` | 7699 | f87cca83 2026-04-17 | Chiral Yangians / ordered chiral homology | PROVED | Y | `chapters/theory/ordered_chiral_homology.tex` | P0 | Largest standalone. |
| 35 | `programme_summary.tex` | 2790 | f87cca83 2026-04-17 | Programme summary | meta-document | Y | — | P1 | Needs 2026-04-16/17 frontier updates. |
| 36 | `programme_summary_section1.tex` | 690 | f87cca83 2026-04-17 | § 1 only | derived from #35 | Y | — | P3 | Retire in favour of #35 or inline into chapter 0. |
| 37 | `programme_summary_sections2_4.tex` | 807 | 02336ae5 2026-04-13 | §§ 2-4 | derived from #35 | Y | — | P3 | Retire. |
| 38 | `programme_summary_sections5_8.tex` | 798 | 02336ae5 2026-04-13 | §§ 5-8 | derived from #35 | Y | — | P3 | Retire. |
| 39 | `programme_summary_sections9_14.tex` | 823 | f87cca83 2026-04-17 | §§ 9-14 | derived from #35 | Y | — | P3 | Retire. |
| 40 | `riccati.tex` | 773 | 02feda65 2026-04-13 | Riccati algebraicity + depth classification | PROVED | Y | `chapters/theory/riccati.tex` | P0 | |
| 41 | `sc_chtop_pva_descent.tex` | 1594 | 98f1f767 2026-04-13 | SC^{ch,top} + PVA descent | PROVED (topologization affine KM; conj. general) | Y | `chapters/theory/en_koszul_duality.tex` | P1 | Needs AP-TOPOLOGIZATION scope qualifiers. |
| 42 | `seven_faces.tex` | 1557 | f87cca83 2026-04-17 | Seven faces flagship | PROVED all seven | Y | Part V | P0 | |
| 43 | `shadow_towers.tex` | 2347 | 07c7b9f0 2026-04-13 | Shadow obstruction towers | PROVED | Y | `shadow_tower_higher_coefficients.tex` | P3 | SUPERSEDED by `shadow_towers_v3.tex`. Retire. |
| 44 | `shadow_towers_v2.tex` | 795 | 07c7b9f0 2026-04-13 | Shadow tower + modular Koszul duality (compressed) | PROVED | Y | idem | P3 | SUPERSEDED by v3. Retire. |
| 45 | `shadow_towers_v3.tex` | 4718 | f87cca83 2026-04-17 | Shadow obstruction tower (canonical) | PROVED | Y | `shadow_tower_higher_coefficients.tex` | P0 | Canonical shadow-tower standalone. |
| 46 | `survey_modular_koszul_duality.tex` | 8595 | 02336ae5 2026-04-13 | MKD survey | meta | Y | — | P3 | SUPERSEDED by `survey_modular_koszul_duality_v2.tex`. Retire after 2026-04-17 cross-check. |
| 47 | `survey_modular_koszul_duality_v2.tex` | 8530 | 557bbc06 2026-04-17 | MKD survey (canonical v2) | meta | Y | — | P1 | Needs Beilinson-rectified 2026-04-17 open-frontier update. |
| 48 | `survey_track_a_compressed.tex` | 2463 | 02336ae5 2026-04-13 | Compressed track A | meta | Y | — | P2 | Pre-2026-04-16 wave. |
| 49 | `survey_track_b_compressed.tex` | 2394 | 02336ae5 2026-04-13 | Compressed track B | meta | Y | — | P2 | Pre-2026-04-16 wave. |
| 50 | `theorem_index.tex` | 2347 | f87cca83 2026-04-17 | Auto-generated theorem index | meta | Y | — | P1 | Regenerate post-wave14/15. |
| 51 | `three_dimensional_quantum_gravity.tex` | 2851 | 650a5ce3 2026-04-14 | 3D quantum gravity (Vol II climax shadow) | PROVED (Vol II thm:programme-climax with scope caveats) | Y | Vol II Part VI | P2 | Needs 2026-04-17 W(p) tempering retraction + non-tempered-stratum scope fix. |
| 52 | `three_parameter_hbar.tex` | 608 | f87cca83 2026-04-17 | 3-parameter ℏ identification | PROVED | Y | — | P0 | |
| 53 | `virasoro_r_matrix.tex` | 490 | f87cca83 2026-04-17 | Virasoro spectral R-matrix | PROVED (closed form + non-formality) | Y | `chapters/seven_faces/virasoro_r_matrix.tex` | P0 | Vol II `rpt_convergence_shapovalov.tex` is an independent verification. |
| 54 | `w3_holographic_datum.tex` | 596 | 07c7b9f0 2026-04-13 | First rank-2 holographic datum H(W_3) | PROVED | Y | `chapters/theory/holographic_datum.tex` | P0 | |

Row totals: 54 files. CL = 5 (#8, 9, 10, 11, 16).

## Part B. Volume II standalones (9 files)

Directory `/Users/raeez/chiral-bar-cobar-vol2/standalone/`.

| # | File | LC | Last hash / date | Primary advertisement | Status | Self-cont. | Canonical chapter | Tier | Notes |
|---|------|----|----------------|----------------------|--------|-----|-----|-----|-----|
| V2-1 | `bar_chain_models_chiral_quantum_groups.tex` | 875 | 80196c8 2026-04-16 | E_1-chiral quantum groups + E_N ladder | PROVED on Koszul locus | Y | Part II | P0 | Most recent. |
| V2-2 | `bcfg_chiral_coproduct_folding.tex` | 215 | ba54eea 2026-04-13 | BCFG non-simply-laced coproduct | CONJECTURAL | Y | `unified_chiral_quantum_group.tex` | P1 | Unified Q_g^{k,f,μ} inscription 2026-04-16 may supersede. |
| V2-3 | `class_m_global_triangle.tex` | 206 | ba54eea 2026-04-13 | Class M global triangle | conj/partial | Y | `class_m_global_triangle.tex` (chapter) | P1 | Weight-completed closure (MC5) not yet reflected. |
| V2-4 | `curved_dunn_two_complex_bridge.tex` | 177 | 80196c8 2026-04-16 | Curved-Dunn two-complex bridge | PROVED all g (2026-04-16) | Y | `curved_dunn_higher_genus.tex` | P0 | Fresh inscription. |
| V2-5 | `monster_voa_orbifold_e3.tex` | 190 | ba54eea 2026-04-13 | E_3-top for Monster VOA orbifold | CONJECTURAL | Y | — | P1 | |
| V2-6 | `preface_full_survey.tex` | 1759 | edc3ac2 2026-04-12 | Full Vol II preface | meta | Y | `chapters/frame/preface.tex` | P2 | Pre-wave14. Needs refresh. |
| V2-7 | `rpt_convergence_shapovalov.tex` | 185 | ba54eea 2026-04-13 | Virasoro spectral R = Shapovalov | PROVED | Y | — | P0 | Cross-volume partner of Vol I #53. |
| V2-8 | `stokes_gap_kzb_regularity.tex` | 248 | ba54eea 2026-04-13 | Stokes gap / KZB regularity | PROVED (Jimbo-Miwa, 2026-04-16) | Y | `curved_dunn_higher_genus.tex` | P1 | Update to cite `thm:irregular-singular-kzb-regularity`. |

Row total: 9 files.

## Part C. Volume III standalones

Directory `/Users/raeez/calabi-yau-quantum-groups/standalone/` — **does not exist**. Row total: 0.

See Part E for scaffold proposal.

## Part D. Breakdown by tier

- **P0 (ship-ready):** 22 (Vol I #3, 5, 6, 14, 15, 17, 18, 19, 20, 22, 24, 26, 28, 30, 32, 34, 40, 42, 45, 52, 53, 54; Vol II V2-1, V2-4, V2-7) — net 25.
- **P1 (minor sync):** 17 (Vol I #1, 4, 7, 12, 13, 21, 25, 27, 29, 31, 33, 35, 41, 47, 50; Vol II V2-2, V2-3, V2-5, V2-8) — net 19.
- **P2 (substantial rewrite):** 7 (Vol I #2, 23, 48, 49, 51; Vol II V2-6; also Vol I #3 for FL-convention caveat counted under P0 with caveat inscribed).
- **P3 (retire):** 6 (Vol I #36, 37, 38, 39, 43, 44, 46).
- **CL (cover letter):** 5 (Vol I #8, 9, 10, 11, 16).

## Part E. Coverage gap — wave 14 / 15 Platonic results without a standalone

Each row: wave-14/15 theorem → does any existing standalone advertise it → proposed filename.

| Result | Label | Chapter host | Existing standalone? | Proposed new standalone filename | Proposed location |
|--------|-------|--------------|----------------------|----------------------------------|-------------------|
| Universal conductor K | `chap:universal-conductor` / `thm:platonic-conductor` | Vol I `chiral_chern_weil_brst_conductor.tex` | Partial (#4 chiral_chern_weil.tex) | `standalone/universal_conductor.tex` | Vol I |
| Iterated Sugawara ladder / E_∞-topologization | `thm:iterated-sugawara-construction`, `thm:e-infinity-topologization-ladder` | Vol II `e_infinity_topologization.tex` | NO | `standalone/e_infinity_topologization_ladder.tex` | Vol II |
| Chiral higher Deligne | `thm:chiral-higher-deligne` | Vol II `chiral_higher_deligne.tex` | NO | `standalone/chiral_higher_deligne.tex` | Vol II |
| Theorem A^{∞,2} properad | `thm:A-infinity-2` | Vol I `theorem_A_infinity_2.tex` | NO | `standalone/theorem_A_infinity_2_properad.tex` | Vol I |
| Admissible-KL periodic CDG | `thm:periodic-cdg-is-koszul-compatible` | Vol I `periodic_cdg_admissible.tex` | NO | `standalone/periodic_cdg_admissible_kl.tex` | Vol I |
| Universal celestial holography | `thm:uch-main` | Vol II `universal_celestial_holography.tex` | NO | `standalone/universal_celestial_holography.tex` | Vol II |
| CY-D κ stratification | `thm:kappa-stratification-by-d`, `thm:kappa-hodge-supertrace-identification` | Vol III `cy_d_kappa_stratification.tex` | NO (Vol III has none) | `standalone/cy_d_kappa_stratification_vol3.tex` | Vol III (see Part F) |
| FTM seven-fold TFAE at g=0 | `thm:ftm-seven-fold-tfae-via-hub-spoke` | Vol I `ftm_seven_fold_tfae_platonic.tex` | NO | `standalone/ftm_seven_fold_tfae_g0.tex` | Vol I |
| MC3 five-family mechanism | `chapters/theory/mc3_five_family_platonic.tex` | — | Partial (#14 drinfeld_kohno, #27 N2_mc3_all_types) | `standalone/mc3_five_family.tex` (optional consolidation) | Vol I |
| sl_3 Sugawara c = -83/20 admissible (iter 52) | iter breakthrough | — | NO | `standalone/sl3_sugawara_admissible.tex` | Vol I (optional) |

Coverage-gap count: 8 of 8 advertised wave-14/15 results lack a dedicated standalone; Vol I's `chiral_chern_weil.tex` partially covers the universal conductor but pre-dates wave-14 inscription.

## Part F. Duplicate-standalone retirement recommendations

Retire (move to `standalone/archive/` or delete after AP149 propagation sweep):

1. `shadow_towers.tex` → superseded by `shadow_towers_v3.tex` (canonical).
2. `shadow_towers_v2.tex` → superseded by `shadow_towers_v3.tex`.
3. `survey_modular_koszul_duality.tex` → superseded by `survey_modular_koszul_duality_v2.tex`.
4. `programme_summary_section1.tex` → derivable from `programme_summary.tex`.
5. `programme_summary_sections2_4.tex` → derivable from `programme_summary.tex`.
6. `programme_summary_sections5_8.tex` → derivable from `programme_summary.tex`.
7. `programme_summary_sections9_14.tex` → derivable from `programme_summary.tex`.

Keep canonical: `shadow_towers_v3.tex`, `survey_modular_koszul_duality_v2.tex`, `programme_summary.tex`.

Near-duplicates requiring a canonical-vs-companion decision (do NOT retire without review):

- `classification.tex` vs `classification_trichotomy.tex`: #5 is the shadow-tables reference; #6 is the trichotomy axis. Keep both; add cross-references.
- `analytic_sewing.tex` vs `N5b_analytic_sewing.tex`: #1 is the long-form treatment; #31 is the note-series companion. Keep both; add explicit companion pointer.
- `survey_track_a_compressed.tex` vs `survey_track_b_compressed.tex`: two audiences (Track A = algebraic-geometry, Track B = physics). Keep both; mark P2 pending 2026-04-17 refresh.
- `cy_to_chiral_functor.tex` (Vol I) vs proposed `standalone/cy_to_chiral_functor_vol3.tex` (Vol III): Vol I version is the Platonic-statement draft; Vol III mirror will be the implementation-level with κ stratification tables. Keep both.

## Part G. Status matrix for the 8 wave-14 / 15 advertisements

| Advertisement | Vol I chapter | Vol II chapter | Vol III chapter | Standalone status |
|---------------|---------------|----------------|-----------------|-------------------|
| Universal conductor K (`chap:universal-conductor`) | EXISTS (chiral_chern_weil_brst_conductor.tex) | cross-referenced | cross-referenced | **needs creation** (partial coverage in Vol I #4) |
| Iterated Sugawara ladder (`thm:e-infinity-topologization-ladder`) | cross-referenced | EXISTS (e_infinity_topologization.tex) | cross-referenced | **needs creation** |
| Chiral higher Deligne (`thm:chiral-higher-deligne`) | cross-referenced | EXISTS (chiral_higher_deligne.tex) | cross-referenced | **needs creation** |
| Theorem A^{∞,2} properad (`thm:A-infinity-2`) | EXISTS (theorem_A_infinity_2.tex) | bridge I.3.2 | Φ dependency | **needs creation** |
| Admissible-KL periodic CDG (`thm:periodic-cdg-is-koszul-compatible`) | EXISTS (periodic_cdg_admissible.tex) | — | — | **needs creation** |
| Universal celestial holography (`thm:uch-main`) | — | EXISTS (universal_celestial_holography.tex) | — | **needs creation** |
| CY-D κ stratification (`thm:kappa-stratification-by-d`) | — | — | EXISTS (cy_d_kappa_stratification.tex) | **needs creation** (Vol III scaffold proposed) |
| FTM seven-fold TFAE g=0 (`thm:ftm-seven-fold-tfae-via-hub-spoke`) | EXISTS (ftm_seven_fold_tfae_platonic.tex) | — | — | **needs creation** |

All 8 advertisements are in the **needs creation** state for standalone coverage. `#4 chiral_chern_weil.tex` is the closest partial pre-wave-14 coverage; it does not yet advertise K as universal conductor identity at the closure-wave level.

## Appendix. Vol III scaffold plan (see separate files under `/Users/raeez/calabi-yau-quantum-groups/standalone/`)

Six scaffold `.tex` files drafted 2026-04-17 (title + abstract stub + `\input` pointers + bibliography only; NOT full content):

1. `cy_to_chiral_functor_vol3.tex`
2. `cy_d_kappa_stratification_vol3.tex`
3. `k3e_cy3_programme_vol3.tex`
4. `cy3_6d_hcs_w1inf_vol3.tex`
5. `m3_b2_saga_vol3.tex`
6. `super_riccati_shadow_tower_vol3.tex`

See Part E for wave-14/15 advertised results covered.

— End of census.
