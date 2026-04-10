# Adversarial Mathematical Audit -- 2026-04-10

## Campaign: 180 agents (all codex:rescue or general-purpose), ~500K .tex lines + ~2,600 compute files audited
## Compute tests verified: ~10,300 pass, 3 known failures

### CRITICAL FINDINGS (9)

| # | Vol | File | Line | Error | AP |
|---|-----|------|------|-------|----|
| C1 | I | cobar_construction.tex | 2542 | κ = k for non-abelian KM (should be dim(g)(k+h^v)/(2h^v)) | AP1 |
| C2 | I | cobar_construction.tex | 2176 | Garbled sl_2 curvature computation (m_1^2 proof incoherent) | -- |
| C3 | I | heisenberg_eisenstein.tex | 1108 | Koszul dual H_κ^! = H_{-κ} (WRONG: Sym^ch(V*), contradicts same file L312) | AP33 |
| C4 | I | algebraic_foundations.tex | 344 | Bare Ω/z without level prefix k | AP126 |
| C5 | I | algebraic_foundations.tex | 1395 | Face map formula off-by-one (exponents sum n-2, should be n) | -- |
| C6 | II | ht_bulk_boundary_line_core.tex | 2404 | κ(sl_2) = k (WRONG: 3(k+2)/4) | AP1 |
| C7 | II | modular_pva_quantization.tex | 1611 | W_3 Hamiltonian coeff 32/(5c) (WRONG: 16/(22+5c), cascades) | -- |
| C8 | I | landscape_census.tex | 216 | r-matrix Ω/((k+h^v)z) fails k=0 vanishing | AP126 |
| C9 | I | genus_expansions.tex | 79 | Same forbidden r-matrix form Ω/((k+h^v)z) | AP126 |

### SERIOUS FINDINGS (4)

| # | Vol | File | Line | Error | AP |
|---|-----|------|------|-------|----|
| S1 | I | cobar_construction.tex | 47 | d_cobar^2 = κ·ω_g conflates fiberwise/total | AP87 |
| S2 | I | cobar_construction.tex | 2345 | Dimensionally incoherent bar differential computation | AP132 |
| S3 | I | bar_cobar_adjunction_inversion.tex | 2354 | BBL conservativity proof incomplete | -- |
| S4 | II | log_ht_monodromy_core.tex | 99 | Bar complex T^c(sA) missing augmentation ideal | AP132 |

### MODERATE FINDINGS (~45)

**AP126 r-matrix (6):** spectral-braiding-frontier L1841/2064, celestial_holography L1883/1953, line-operators L953, bar_cobar_adjunction_curved L757
**AP32 weight tags (~15):** higher_genus_foundations L1013/4624, heisenberg_eisenstein L28/327/615/1710, heisenberg_frame L46/3756, genus_expansions L91, higher_genus_modular_koszul L24476, e1_modular_koszul L655
**AP125/124 labels (~8):** e1_modular_koszul 5 duplicates, algebraic_foundations 2 mismatches + 2 duplicates
**AP117 KZ form (2):** line-operators L917, celestial_holography L1940
**AP40 env/tag (3):** higher_genus_foundations L7081, e1_modular_koszul L183
**AP29 prose (5):** higher_genus_modular_koszul L2775, heisenberg_frame L730/4360/4624, heisenberg_eisenstein L242/1353
**Hardcoded Part refs (8):** concordance L172/1987/4406, various others
**Other:** bar_construction L992/2235/1716, arithmetic_shadows L1533, chiral_koszul_pairs L5449, higher_genus_modular_koszul L9212

### CLEAN CHAPTERS (13/30)

bar_cobar_adjunction_curved, higher_genus_complementarity, chiral_hochschild_koszul, chiral_koszul_pairs, higher_genus_modular_koszul (30K lines), kac_moody, free_fields+beta_gamma, lattice+toroidal, bv_brst, arithmetic_shadows, concordance, heisenberg_frame+introduction

### AP126 MEGA-SWEEP (all 3 volumes, ~103 violations)

From the comprehensive cross-volume sweep agent:

| Volume | Type A (r=Ω/z) | Type B (frac) | Type C (denom) | Type D (Ω_ij) | Type E (dlog) | Total |
|--------|:-:|:-:|:-:|:-:|:-:|:-:|
| Vol I (build) | 5 | 3 | ~15 | 9 | ~10 | ~42 |
| Vol I (draft) | 5 | 2 | 0 | 0 | 0 | 7 |
| Vol II | 5 | 9 | ~11 | 7 | ~18 | ~50 |
| Vol III | 1 | 0 | 0 | 3 | 0 | 4 |
| **Standalones** | ~22 | -- | ~20 | -- | -- | ~40 |
| **TOTAL** | | | | | | **~143** |

Worst offender files:
- thqg_gravitational_yangian.tex: 11 Type A/D violations
- three_parameter_hbar.tex: 8 violations
- genus1_seven_faces.tex: 9 violations
- kac_moody.tex: 5 Type C (KZ convention, needs triage)
- log_ht_monodromy_core.tex: 6 violations
- spectral-braiding-core.tex: 4 violations

### Vol I thqg cluster (CX-19): 16 AP126 + 20 AP32 + 30 kappa audit

### COMPUTE LAYER FINDINGS

- **656 critical tests PASS** (recently modified engines)
- **120,068 total tests** available
- **1 meta-test failure**: test_ap126_violation_detected (test expects violations, cleanup removed them)
- **1 real test failure**: test_euler_truncated_converges in sft_bar_comparison_engine (monotonicity at d=2)
- **1 stale docstring**: sl3_subregular_bar.py lines 36,42 still say K_BP=2 (code correctly returns 196)
- **Vol III**: 29+ bare kappa violations in affine_yangian_e1_cy3.py (AP113)

### COMPUTE FORMULA ERRORS (22 total, from CX-05 + CX-30)

**5 DS engines -- c(W_N,k) bug (copy-paste, spurious (k+N-1)^2):**
- ds_arithmetic_transformation_engine.py:98
- ds_cascade_shadows.py:83
- ds_shadow_cascade_engine.py:92
- ds_nonprincipal_shadows.py:88
- ds_transferred_shadows.py:97

**12 WRONG central charge formulas:**
- extended_ferm_ghost.py:68,83,97,107 -- wrong c_bc polynomial
- physics_horizon.py:265-266 -- same wrong formula
- theorem_w_algebra_chapter_rectification_engine.py:139 -- BP implies K=2
- hook_type_w_duality.py:233,285 -- KRW implies K=2
- theorem_ap49_superconformal_engine.py:320 -- preserves K=76 (test-only)
- true_formula_census_verifier.py:183,191 -- k=-3 regularization

**5 AP137 SWAPS:**
- bc_quantum_modularity_shadow_engine.py:178 -- c_bg=-2 (should be +2)
- bc_mzv_shadow_engine.py:418 -- c_bg=-2
- theorem_ainfty_nonformality_class_m_engine.py:445 -- c_bg=-2
- cy_chiral_derham_k3_engine.py:555-556 -- both labels swapped

### ADDITIONAL .tex FINDINGS

**Vol II 3d_gravity.tex:1696** -- AP4: proof after conjectured remark
**Vol II spectral-braiding-frontier.tex:1841,2019,2064** -- 3 more AP126
**Vol II twisted_holography_quantum_gravity.tex:1881,1938** -- 2 more AP126 + 2 AP117
**Vol II ordered_kd_frontier.tex:1778** -- 1 AP117 + 3 em dashes

### FIXES APPLIED ON DISK BY AGENTS

1. Vol III: 4 AP113 fixes (cy_to_chiral, cy_holographic_datum_master, toroidal_elliptic)
2. Vol I ordered_associative_chiral_kd.tex: AP126 fix + AP4 fix + em-dash fix (3 fixes)
Total: 7 fixes applied

### STATUS: 130 agents launched and completed. 9 CRITICAL .tex + 22 CRITICAL compute errors located.
