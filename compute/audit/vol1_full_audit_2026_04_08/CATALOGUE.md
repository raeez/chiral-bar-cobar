# Volume I Full Mathematical Fault Catalogue

Generated on 2026-04-08 from the live Volume I repo plus the archived red-team ledgers.

This catalogue excludes pure exposition/style backlog and focuses on rigor, correctness, claim-surface integrity, proof dependencies, hypothesis discipline, and duplication/drift risks.

## Snapshot

- Tagged claims in current Volume I metadata: **3463**
- Current `ProvedHere` claims: **2711**
- Current proof-auditor findings: **742**
- Current proof-level critical findings: **8**
- Current proof-level serious findings: **30**
- Current `ProvedHere` claims without compute-test references: **2171**
- Archived red-team V1 high/critical-risk claims: **428**
- Archived red-team V1 frontier claims: **229**
- Archived suspicious proved-here local dependency violations in V1: **28**
- Cross-volume label-status conflicts touching V1: **8**
- Local duplicate labels inside Volume I: **102**
- Duplicate title clusters across files: **191**

## Source-Validated Critical / Serious Findings

1. **[CRITICAL] Principal W-duality surface is internally contradictory**
   The main principal-duality theorem states an actual equivalence (W^k)^! ≃ W^{k'}, while the later 'precise statement' says the dual is not W^{k'} itself, only a chiral CE algebra with the same kappa. This is a foundational inversion-vs-dual conflation.
   Evidence:
   - `chapters/examples/w_algebras.tex:316` `thm:w-algebra-koszul-main`
   - `chapters/examples/w_algebras.tex:1201` `thm:w-koszul-precise`
   - `chapters/examples/w_algebras.tex:1218` `thm:w-koszul-precise`
   - `chapters/connections/concordance.tex:28` `thm:higher-genus-inversion`

2. **[CRITICAL] W precise statement leaves its general-level claim unproved**
   The proof of thm:w-koszul-precise proves the critical-level package and skips Part B. The theorem still asserts a general-level statement, so the claim surface currently outruns the written proof.
   Evidence:
   - `chapters/examples/w_algebras.tex:1214` `thm:w-koszul-precise`
   - `chapters/examples/w_algebras.tex:1228` `thm:w-koszul-precise`

3. **[CRITICAL] Explicit theta theorem overclaims beyond the proved scalar lane**
   thm:explicit-theta asserts the full kappa·eta⊗Lambda formula under a one-channel hypothesis, but later results and concordance explicitly restrict that formula to the proved uniform-weight lane and record failure of tautological purity in multi-weight settings.
   Evidence:
   - `chapters/theory/higher_genus_modular_koszul.tex:3777` `thm:explicit-theta`
   - `chapters/theory/higher_genus_modular_koszul.tex:7404` `cor:scalar-saturation`
   - `chapters/theory/higher_genus_modular_koszul.tex:13735` `thm:theta-direct-derivation`
   - `chapters/connections/concordance.tex:9394` `concordance-multi-weight-diagnosis`

4. **[SERIOUS] Sub-exponential growth is not automatic from positive energy alone**
   prop:subexponential-growth-automatic assumes only positive energy and finite-dimensional graded pieces, then imports Hardy-Ramanujan-Rademacher/effective-central-charge asymptotics. Those asymptotics need much stronger modularity/character-control input, so the proposition is overstated.
   Evidence:
   - `chapters/theory/bar_cobar_adjunction_inversion.tex:3781` `prop:subexponential-growth-automatic`
   - `chapters/theory/bar_cobar_adjunction_inversion.tex:3811` `prop:subexponential-growth-automatic`
   - `chapters/connections/concordance.tex:6702` `concordance-factorization-finiteness-reduction`

5. **[SERIOUS] Yangian duality proof only controls leading-order / low-rank data**
   thm:yangian-koszul-dual is stated as an exact RTT duality theorem, but the proof leans on a 16x16 sl2 orthogonal-complement computation and then declares higher R^{-1} coefficients irrelevant because the mode expansion sees only leading-order data. That does not justify the full algebra-level identification.
   Evidence:
   - `chapters/examples/yangians_foundations.tex:501` `thm:yangian-koszul-dual`
   - `chapters/examples/yangians_foundations.tex:545` `thm:yangian-koszul-dual`
   - `chapters/examples/yangians_foundations.tex:557` `thm:yangian-koszul-dual`

6. **[SERIOUS] Derived W3 duality theorem inherits the contradictory W-duality surface**
   thm:w3-koszul-dual imports the principal W-duality theorem as if it proved (W_3^k)^! ≃ W_3^{k'}. Since the parent theorem surface is internally contradictory, the specialized W3 theorem is downstream-fragile as written.
   Evidence:
   - `chapters/examples/w_algebras.tex:1869` `thm:w3-koszul-dual`
   - `chapters/examples/w_algebras.tex:1897` `thm:w3-koszul-dual`
   - `chapters/examples/w_algebras.tex:1218` `thm:w-koszul-precise`

## Raw Exports

- Full proof-auditor findings: [auditor_findings.csv](./auditor_findings.csv)
- Bottleneck claims and test coverage gaps: [auditor_bottlenecks.csv](./auditor_bottlenecks.csv)
- All `ProvedHere` claims without compute-test references: [auditor_uncovered_provedhere.csv](./auditor_uncovered_provedhere.csv)
- Archived V1 high/critical-risk claims: [archive_v1_high_critical_claims.csv](./archive_v1_high_critical_claims.csv)
- Archived V1 frontier claims: [archive_v1_frontier_claims.csv](./archive_v1_frontier_claims.csv)
- Archived suspicious proved-here dependencies: [archive_v1_suspicious_proved_dependencies.csv](./archive_v1_suspicious_proved_dependencies.csv)
- Cross-volume label-status conflicts touching V1: [archive_label_status_conflicts_touching_v1.csv](./archive_label_status_conflicts_touching_v1.csv)
- Local duplicate labels: [local_duplicate_labels.csv](./local_duplicate_labels.csv)
- Duplicate title clusters: [duplicate_title_clusters.csv](./duplicate_title_clusters.csv)
- QC math-surface drift export: [qc_math_surfaces.json](./qc_math_surfaces.json)
- Manual validated findings as JSON: [manual_findings.json](./manual_findings.json)
- Aggregate counts: [counts.json](./counts.json)

## Current Machine-Detected Math Surfaces

### Auditor

- `CRITICAL`: 8
- `SERIOUS`: 30
- `WARNING`: 84
- `INFO`: 620

- `AP11`: 61
- `AP13-FWD`: 17
- `AP4`: 137
- `AP4-STMT`: 70
- `AP5`: 10
- `AP6`: 36
- `BOTTLENECK`: 21
- `TRANSITIVE`: 390

### QC / Doctrine Drift

- `ambiguous_status`: 25
- `duplicate_paragraph_clusters`: 246
- `infinite_generator_drift`: 1
- `kl_scope_drift`: 1
- `periodicity_overclaim_drift`: 1
- `prior_version`: 1
- `untagged`: 11
- `virasoro_shadow_drift`: 1

## Archive-Derived Highest-Risk File Clusters (V1)

- `chapters/examples/free_fields.tex`: 36 archived high/critical claims
- `chapters/examples/kac_moody.tex`: 27 archived high/critical claims
- `chapters/examples/w_algebras.tex`: 24 archived high/critical claims
- `chapters/examples/yangians_drinfeld_kohno.tex`: 21 archived high/critical claims
- `chapters/connections/genus_complete.tex`: 20 archived high/critical claims
- `chapters/connections/editorial_constitution.tex`: 14 archived high/critical claims
- `chapters/connections/arithmetic_shadows.tex`: 13 archived high/critical claims
- `chapters/connections/thqg_gravitational_complexity.tex`: 13 archived high/critical claims
- `chapters/examples/lattice_foundations.tex`: 13 archived high/critical claims
- `chapters/examples/yangians_foundations.tex`: 13 archived high/critical claims
- `chapters/connections/concordance.tex`: 12 archived high/critical claims
- `chapters/connections/frontier_modular_holography_platonic.tex`: 11 archived high/critical claims
- `chapters/examples/genus_expansions.tex`: 10 archived high/critical claims
- `chapters/examples/yangians_computations.tex`: 10 archived high/critical claims
- `chapters/theory/chiral_hochschild_koszul.tex`: 10 archived high/critical claims
- `chapters/connections/bv_brst.tex`: 9 archived high/critical claims
- `chapters/connections/thqg_gravitational_s_duality.tex`: 9 archived high/critical claims
- `chapters/theory/koszul_pair_structure.tex`: 9 archived high/critical claims
- `chapters/connections/feynman_diagrams.tex`: 8 archived high/critical claims
- `chapters/connections/thqg_symplectic_polarization.tex`: 8 archived high/critical claims

## Honesty Clause

This directory is the fullest current catalogue grounded in the repo’s own claim metadata, proof-chain extraction, archive ledgers, QC drift rules, and direct source reads. It is still not logically absolute completeness: untagged or subtly wrong proofs can exist outside these detection surfaces.
