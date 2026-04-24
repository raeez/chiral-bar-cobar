# Vol I Audit Infrastructure Queue - 2026-04-24

## Live Snapshot

Commands run:

- `make audit`
- `make verify-independence`
- `compute/.venv/bin/python -m pytest -q compute/tests/test_generate_metadata_parser.py compute/tests/test_beilinson_auditor.py`

The worktree was active during this lane: theorem-surface status edits
landed concurrently and changed the audit counts. The final Worker 6
snapshot is the one below.

Proof-chain audit:

- Claims: 3817.
- Statement edges: 5019.
- Proof edges: 3452.
- Proofs extracted: 2861.
- Genuine proof cycles: 0.
- Forward-reference cycles: 22.
- Critical findings: 0.
- Serious findings: 20.
- Warnings: 206.
- Info findings: 474.
- Warning split: AP11 = 170, AP5 = 36.
- Claims with compute tests: 760.
- `ProvedHere` total in the proof auditor: 1861.
- `ProvedHere` without tests in the proof auditor: 1469.

No critical proof-integrity item survives in the final `make audit`
snapshot.

Independent-verification audit:

- Raw-scanned `ProvedHere` labels: 2017.
- Labels with independent verification: 133.
- Coverage gap: 1884.
- Tautological registry entries: 0.
- Orphan registry entries: 0.

Structured metadata:

- Tagged claims: 3919.
- PH = 1951; PE = 456; CJ = 369; H = 29; CD = 1111; O = 3.

## Infrastructure Changes

`compute/lib/beilinson_auditor.py` now reports the break edges for every
AP13-FWD cycle in `make audit`. A forward-reference cycle is still
nonfatal only when at least one edge is statement-only or proof-editorial;
the report now prints those break edges explicitly instead of only giving
a count.

Regression coverage was added in `compute/tests/test_beilinson_auditor.py`
for a synthetic two-node cycle with one statement-only edge and one proof
edge. The test asserts that the cycle is nonfatal and that the report
prints the statement-only break edge. Existing metadata-parser tests still
cover comment stripping for commented theorem/status/label/ref surfaces.

## Warning Triage

AP4 proof-level findings are no longer warning-level in the final
snapshot. The remaining AP4 surfaces are classified as lower-severity
conditional/statement surfaces by the auditor, except for any future case
where a `ProvedHere` proof again cites conjectural material.

AP5 warnings remain propagation warnings only. They are not proof
failures; they say that any mathematical change to a high-fanout label
requires a cross-file sweep.

AP11 warnings remain independent-verification priorities. They flag
`ProvedHere` claims with one external citation and few internal
dependencies. They should be attacked by adding direct computation,
a second primary-source derivation, or a disjoint internal proof route.

AP4-STMT findings are now INFO in the final snapshot. They are
statement-only references and should stay visible as forward-reference
cleanup, not proof-failure evidence.

## Forward-Reference Cycle Queue

`make audit` now prints AP13-FWD break-edge summaries directly.
The final snapshot heads are:

1. `thm:genus-universality`
2. `thm:bar-cobar-inversion-qi`
3. `thm:mc2-full-resolution`
4. `cor:hochschild-averaging-symmetric`
5. `comp:sl2-ce-verification`
6. `comp:y-special-cases-c`
7. `conj:full-dk-bridge`
8. `thm:derived-dk-yangian`
9. `thm:ds-koszul-intertwine`
10. `cor:universal-koszul`
11. `cor:effective-quadruple`
12. `prop:winfty-factorization-package`
13. `cor:branch-points-instantons`
14. `cor:e3-solvable-unconditional`
15. `thm:hgmk-abar5-bar-cobar-scope`
16. `prop:winfty-mc4-frontier-package`
17. `prop:dg-shifted-rtt-seed-normalized-coefficient`
18. `cor:winfty-standard-mc4-package`
19. `cor:yangian-standard-mc4-package`
20. `prop:betagamma-weight-line-shadows`
21. `prop:full-brace-chiral`
22. `thm:heisenberg-all-genus`

Their current edge summaries are available in the `make audit` output and
are not hidden behind aggregate counts.

## HZ-IV Bottleneck Queue

There are 20 uncovered bottleneck nodes in the final snapshot. Decorators
on `ProvedHere` nodes reduce the HZ-IV gap; decorators on `ProvedElsewhere`
or `Conditional` nodes are still valid verification work but do not reduce
the `ProvedHere` coverage gap.

Priority 0:

| deps | status | label | file:line |
|---:|---|---|---|
| 7 | PH | `thm:nms-all-degree-master-equation` | `appendices/nonlinear_modular_shadows.tex:2110` |

Priority 1:

| deps | status | label | file:line |
|---:|---|---|---|
| 6 | PH | `thm:ent-scalar-entropy` | `chapters/connections/entanglement_modular_koszul.tex:160` |
| 6 | CD | `thm:sphere-reconstruction` | `chapters/connections/frontier_modular_holography_platonic.tex:1636` |
| 6 | PH | `v1-thm:kms-moduli` | `chapters/theory/koszulness_moduli_scheme.tex:169` |
| 6 | PE | `prop:fg-ambient-properties` | `chapters/theory/theorem_A_infinity_2.tex:861` |

Priority 2:

| deps | status | label | file:line |
|---:|---|---|---|
| 5 | CD | `thm:bv-bar-coderived` | `chapters/connections/bv_brst.tex:2200` |
| 5 | PH | `thm:frontier-protected-bulk-antiinvolution` | `chapters/connections/frontier_modular_holography_platonic.tex:140` |
| 5 | CD | `thm:hdm-seven-way-master` | `chapters/connections/holographic_datum_master.tex:912` |
| 5 | CD | `prop:hdm-upgrade-theta` | `chapters/connections/holographic_datum_master.tex:1668` |
| 5 | PE | `prop:universal-twisting-adjunction` | `chapters/theory/algebraic_foundations.tex:771` |
| 5 | CD | `prop:winfty-stage5-block-34` | `chapters/theory/bar_cobar_adjunction_curved.tex:5135` |
| 5 | CD | `prop:derived-center-explicit` | `chapters/theory/chiral_center_theorem.tex:1967` |
| 5 | PH | `prop:conformal-blocks-bar` | `chapters/theory/chiral_modules.tex:544` |
| 5 | PH | `thm:cobar-free` | `chapters/theory/cobar_construction.tex:1928` |
| 5 | PH | `prop:twisting-morphism-propagator` | `chapters/theory/configuration_spaces.tex:1203` |
| 5 | PH | `thm:e1-mc-element` | `chapters/theory/e1_modular_koszul.tex:347` |
| 5 | PH | `prop:e1-nonsplitting-obstruction` | `chapters/theory/e1_modular_koszul.tex:432` |
| 5 | PE | `lem:sl2-admissible-splitting` | `chapters/theory/mc5_class_m_chain_level_platonic.tex:1555` |
| 5 | PH | `thm:codim3-heegner-transversality` | `chapters/theory/mc5_class_m_chain_level_platonic.tex:1986` |
| 5 | PH | `thm:strict-chain-level-across-humbert-walls` | `chapters/theory/theorem_B_scope_platonic.tex:1697` |

## Worker F AP5 Propagation Triage

Source surface:

- `compute/audit/vol1_full_audit_2026_04_24/auditor_findings.csv`
  reports 36 AP5 rows.
- AP5 means high fanout: the claim is referenced from many files, so
  any mathematical correction must propagate. AP5 by itself is not a
  proof failure.
- Cross-volume read-only sweep covered
  `~/chiral-bar-cobar-vol2` and `~/calabi-yau-quantum-groups`.

### Classification

Genuine cross-volume mathematical drift or scope-drift risk:

| label | risk | anchor |
|---|---|---|
| `thm:w-algebra-koszul-main` | Principal W-duality is already a validated serious surface in the catalogue; downstream W references must distinguish characteristic transport from an actual same-family Koszul dual. | `chapters/examples/w_algebras.tex:373` |
| `thm:wn-obstruction` | Vol II imports the W obstruction coefficient without a `V1-` namespace and without restating the conditional DS/bar transport hypothesis. | `~/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:1468`, `:1500` |
| `thm:central-charge-complementarity` | Vol II's W-anomaly corollary cites the central-charge theorem through an unprefixed label while combining it with the conditional W obstruction surface. | `~/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:1501` |
| `thm:multi-weight-genus-expansion` | High-risk cross-channel formula surface. Vol II W-algebra and HT passages must use the multi-weight statement, not the older scalar-saturation slogan. | `~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:919`, `:946`; `~/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:164` |
| `thm:bar-cobar-inversion-qi` | Cross-volume consumers must preserve the exact scope: strict on the Koszul locus, coderived/completed off it. Vol III has a compute docstring import and audit note references. | `~/calabi-yau-quantum-groups/compute/lib/bar_hocolim_commutation.py:78` |
| `thm:main-koszul-hoch` | Theorem H identity/concentration label split remains propagation-sensitive; Vol II has live uses and legacy notes recording the overload. | `~/chiral-bar-cobar-vol2/chapters/connections/ym_boundary_theory.tex:285` |
| `thm:hochschild-polynomial-growth` | Same Theorem H split: growth/concentration clauses must not be cited as the Koszul-duality identity. | `chapters/theory/chiral_hochschild_koszul.tex:1972` |
| `prop:pbw-universality` | Frontier summaries in Vol II/III mention universal PBW and admissible quotients; keep the distinction between universal `V_k(g)` and simple quotient `L_k(g)`. | `~/chiral-bar-cobar-vol2/FRONTIER.md:237`; `~/calabi-yau-quantum-groups/FRONTIER.md:357` |
| `thm:general-hs-sewing` | Vol II/III frontier summaries say "entire standard landscape"; this is safe only with the exact HS-sewing hypotheses retained. | `~/chiral-bar-cobar-vol2/FRONTIER.md:289`; `~/calabi-yau-quantum-groups/FRONTIER.md:409` |

Duplicate-label / namespace propagation risk:

| labels | risk |
|---|---|
| `thm:bar-modular-operad`, `thm:bar-nilpotency-complete`, `thm:geometric-equals-operadic-bar`, `thm:bar-cobar-isomorphism-main`, `thm:prism-higher-genus` | Vol II contains both unprefixed phantom stubs and `V1-` stubs for Vol I bar-cobar anchors. Consumers should prefer `V1-...` when the result is imported from Vol I. |
| `thm:pbw-koszulness-criterion`, `thm:koszul-equivalences-meta`, `thm:e1-module-koszul-duality`, `thm:ds-koszul-intertwine` | Vol II consumers mix `V1-...` and unprefixed labels. This is mostly a cross-reference hygiene risk, but it becomes mathematical if a Vol II theorem with the same label is later introduced. |
| `thm:arnold-relations`, `thm:genus-universality`, `thm:modular-characteristic`, `thm:mc2-bar-intrinsic`, `thm:recursive-existence`, `thm:shadow-archetype-classification`, `thm:riccati-algebraicity`, `thm:single-line-dichotomy`, `thm:shadow-connection` | Vol II and/or Vol III contain unprefixed Vol I stubs or references. The mathematical risk is accidental local self-citation instead of explicit Vol I import. |
| `thm:quantum-complementarity-main` | Vol II mostly healed this by using `V1-thm:quantum-complementarity-main`; remaining unprefixed mentions are comments or local compatibility stubs. Keep the `V1-` discipline. |

False-positive / local high-fanout only in this lane:

| labels | reason |
|---|---|
| `thm:heisenberg-koszul-dual-early`, `thm:genus-induction-strict`, `thm:completed-bar-cobar-strong`, `thm:bar-cobar-verdier`, `thm:geom-unit`, `thm:quantum-diff-squares-zero`, `thm:higher-genus-inversion`, `prop:depth-gap-trichotomy` | No direct cross-volume mathematical drift was found in the read-only sweep. They remain high-fanout labels, so future theorem edits still require propagation. |

### Top Actionable Queue

1. Vol II W-anomaly retarget:
   `~/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:1468`,
   `:1500`, `:1501`.
   Closed by Worker F. The W obstruction, central-charge
   complementarity, and completed bar-cobar references now use `V1-`
   labels, with `V1-thm:wn-obstruction` added to the Vol II stub bank.
   The DS/bar transport hypothesis was already present in the corollary
   statement and was not broadened.
2. Vol II phantom-stub cleanup:
   `~/chiral-bar-cobar-vol2/main.tex:630-647`, `:698-710`,
   `:859-889`.
   Decide whether unprefixed Vol I aliases stay as compatibility stubs
   or whether live consumers should all move to `V1-...`.
3. Vol III toroidal stub cleanup:
   `~/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:21-36`.
   The bank of unprefixed Vol I labels should be namespaced or commented
   as import stubs.
4. Vol III K3 x E modular-characteristic references:
   `~/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex:3369-3625`.
   Verify every use of `thm:genus-universality`,
   `thm:modular-characteristic`, `thm:general-hs-sewing`,
   `thm:riccati-algebraicity`, and `thm:shadow-connection` against the
   current Vol I Heisenberg-shadow vs total-space `\kappa_{\mathrm{ch}}`
   distinction.
5. Vol II multi-weight consumers:
   `~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:919`,
   `:946`; `~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:382`;
   `~/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:164`,
   `:1409`.
   Check that every formula is multi-weight/cross-channel, not the older
   scalar lane.
6. Vol II/III frontier PBW wording:
   `~/chiral-bar-cobar-vol2/FRONTIER.md:237`,
   `~/calabi-yau-quantum-groups/FRONTIER.md:357`.
   Preserve `V_k(\mathfrak g)` universal PBW all levels separately from
   simple quotient `L_k(\mathfrak g)` admissible-level claims.
7. Vol II/III HS-sewing summaries:
   `~/chiral-bar-cobar-vol2/FRONTIER.md:289`,
   `~/calabi-yau-quantum-groups/FRONTIER.md:409`.
   If the phrase "entire standard landscape" remains, attach the exact
   HS-sewing hypotheses or a Vol I reference with the hypotheses visible.
8. Theorem H split in Vol II:
   `~/chiral-bar-cobar-vol2/chapters/connections/ym_boundary_theory.tex:285`
   and any `V1-thm:main-koszul-hoch` consumers.
   Partly closed by Worker F for the generic-level Yang--Mills boundary
   lane: `ym_boundary_theory.tex` now uses `V1-thm:main-koszul-hoch`,
   and `V1-thm:main-koszul-hoch` has been added to the Vol II stub bank.
   The mathematical split between the Koszul-duality identity and the
   polynomial-growth/concentration clause remains a theorem-owner audit
   item for non-YM consumers.

### Cross-Volume Label-Status Conflicts

The catalogue still reports eight label/status conflicts touching Vol I.
They are not AP5 rows, but they are the active cross-volume status queue:

| label | conflict |
|---|---|
| `thm:thqg-contact-termination` | V1 `ProvedHere`; V2 `ProvedElsewhere`. |
| `lem:thqg-VII-genus-shifts` | V1 `ProvedElsewhere`; V2 mixed `Unknown`/`ProvedElsewhere`. |
| `cor:thqg-I-genus-g-partition` | V1 `ProvedHere`; V2 `Unknown`. |
| `prop:thqg-III-kontsevich-pridham` | V1 `ProvedElsewhere`; V2 `Unknown`. |
| `thm:grand-synthesis-principle` | V1 `ProvedHere`; V2 `Conditional`. |
| `thm:conditional-mass-gap-transfer` | V1 `Conjectured`; V2 `Conditional`. |
| `conj:modular` | V1 `Conjectured`; V2 `ProvedHere`. |
| `conj:DS` | V1 `Conjectured`; V2 `ProvedHere`. |

Worker F did not edit cross-volume theorem files. The queue above is
intended for the integration owner or a dedicated cross-volume sync lane.

### Worker F Minimal Sync Patch

Files changed outside Vol I:

- `~/chiral-bar-cobar-vol2/main.tex`: added
  `V1-thm:wn-obstruction`, `V1-thm:pbw-koszulness-criterion`, and
  `V1-thm:main-koszul-hoch` to the existing Vol I stub bank.
- `~/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex`:
  retargeted the W-anomaly corollary's imports from unprefixed
  `thm:wn-obstruction`, `thm:central-charge-complementarity`, and
  `thm:completed-bar-cobar-strong` to the explicit `V1-` labels.
- `~/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex`:
  retargeted Vol I PBW and DS-Koszul references to
  `V1-thm:pbw-koszulness-criterion` and
  `V1-thm:ds-koszul-intertwine`.
- `~/chiral-bar-cobar-vol2/chapters/connections/ym_boundary_theory.tex`:
  retargeted the generic-level Theorem H imports to
  `V1-thm:main-koszul-hoch`.

Targeted verification:

- `rg "\\ref\\{thm:wn-obstruction\\}|\\ref\\{thm:central-charge-complementarity\\}|\\ref\\{thm:completed-bar-cobar-strong\\}" ~/chiral-bar-cobar-vol2/chapters ~/chiral-bar-cobar-vol2/standalone`
  returns no unprefixed live theorem references.
- The remaining occurrences in `~/chiral-bar-cobar-vol2/main.tex` and
  `~/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex` are
  `V1-` imports.
- A targeted residual sweep over `bv_brst.tex`,
  `chiral_higher_deligne.tex`, `ym_boundary_theory.tex`, and
  `ym_synthesis.tex` found zero explicitly-Vol-I AP5 references still
  using unprefixed labels.

Clean residual sweep, excluding `metadata/`, `compute/`, `notes/`,
`archive/`, and `.claude/` worktrees:

- Vol II live residuals: 20 explicitly-Vol-I AP5 references still use
  unprefixed labels. The dominant cluster is
  `thm:general-hs-sewing` in THQG/HT connection files; smaller residues
  are `thm:completed-bar-cobar-strong`,
  `prop:depth-gap-trichotomy`, and comment-only
  `thm:ds-koszul-intertwine`.
- Vol III live residuals: 19 explicitly-Vol-I AP5 references still use
  unprefixed labels. The dominant clusters are the
  `toroidal_elliptic.tex` Vol I stub bank and the
  `k3e_cy3_programme.tex` shadow/recursion references.

These residuals were not patched in Worker F because they require either
large mechanical namespace propagation or a theorem-owner check of the
HS-sewing / K3 x E `\kappa_{\mathrm{ch}}` scope. The safe namespace
patches in the W, PBW/DS, and generic Theorem H lanes did converge.
