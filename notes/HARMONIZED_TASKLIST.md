# HARMONIZED TASK LIST
# Generated 2026-03-17 from three audit artifacts
# Sources: REFORGE_MANIFEST.md (387 findings), STRIKE_LIST_250.md (250 items), mathematical_audit (34 issues)

---

## PART 0: FORMULA-FIX (unpropagated audit fixes)

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| FF-1 | I | chapters/theory/introduction.tex:1257 | FIX kappa formula: `dim(g)/(k+h^v)` → `dim(g)·(k+h^v)/(2h^v)` | AUDIT:A7-UNPROPAGATED |
| FF-2 | I | chapters/theory/koszul_pair_structure.tex:1400 | FIX kappa formula: `k·dim(g)/(2(k+h^v))` → `(k+h^v)·dim(g)/(2h^v)` | AUDIT:A7-UNPROPAGATED |
| FF-3 | I | chapters/theory/koszul_pair_structure.tex:1433 | FIX kappa formula: `k·dim(g)/(2(k+h^v))` → `(k+h^v)·dim(g)/(2h^v)` | AUDIT:A7-UNPROPAGATED |
| FF-4 | I | chapters/examples/free_fields.tex:3452 | FIX kappa formula: `c/(2(k+h^v))` → `(k+h^v)·dim(g)/(2h^v)` | AUDIT:A7-UNPROPAGATED |
| FF-5 | II | chapters/connections/ht_bulk_boundary_line.tex:1804 | FIX Koszul dual conflation: `A^!_{M2} := Omega(B(A))` → `A^!_{M2} := H*(B(A))^v` (Verdier dual) | AUDIT:A8-UNPROPAGATED |

---

## PART 1: REFORGE MANIFEST (tell-not-show prose cleanup)

### TIER 1: CONNECTIONS

#### `chapters/connections/bv_brst.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-1 | I | chapters/connections/bv_brst.tex:4-6 | CUT or SHARPEN governing question remark | REFORGE_MANIFEST:1 |
| R-2 | I | chapters/connections/bv_brst.tex:8-10 | CUT or SHARPEN H/M/S route remark | REFORGE_MANIFEST:2 |
| R-3 | I | chapters/connections/bv_brst.tex:41-47 | CUT or SHARPEN "antifields" physics gloss in proof Step 1 | REFORGE_MANIFEST:3 |
| R-4 | I | chapters/connections/bv_brst.tex:56 | CUT or COMPRESS restates what lines 52-55 showed | REFORGE_MANIFEST:4 |
| R-5 | I | chapters/connections/bv_brst.tex:63-69 | CUT physics interp in proof Step 3 | REFORGE_MANIFEST:5 |
| R-6 | I | chapters/connections/bv_brst.tex:108 | CUT or COMPRESS rephrases algebraic stage | REFORGE_MANIFEST:6 |
| R-7 | I | chapters/connections/bv_brst.tex:149 | CUT or SHARPEN journalistic subsection title | REFORGE_MANIFEST:7 |
| R-8 | I | chapters/connections/bv_brst.tex:211-230 | CUT or COMPRESS rem:genus1-bv echoes Thm genus-universality three ways | REFORGE_MANIFEST:8 |
| R-9 | I | chapters/connections/bv_brst.tex:232-258 | CUT or COMPRESS rem:anomaly-curvature-bv restates anomaly=curvature | REFORGE_MANIFEST:9 |
| R-10 | I | chapters/connections/bv_brst.tex:260-276 | CUT rem:cg-framework pure literature summary | REFORGE_MANIFEST:10 |
| R-11 | I | chapters/connections/bv_brst.tex:316-318 | CUT one-sentence remark adding nothing | REFORGE_MANIFEST:11 |
| R-12 | I | chapters/connections/bv_brst.tex:441-459 | COMPRESS rem:brst-nilpotence-periodicity extended metaphor | REFORGE_MANIFEST:12 |
| R-13 | I | chapters/connections/bv_brst.tex:594-621 | CUT or COMPRESS rem:bv-convergence repeats BV dictionary | REFORGE_MANIFEST:13 |
| R-14 | I | chapters/connections/bv_brst.tex:993-1008 | CUT or COMPRESS rem:master-table-brst re-lists Master Table entries | REFORGE_MANIFEST:14 |
| R-15 | I | chapters/connections/bv_brst.tex:1179-1201 | CUT 22 lines repeating "bar IS semi-infinite" | REFORGE_MANIFEST:15 |

#### `chapters/connections/feynman_diagrams.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-16 | I | chapters/connections/feynman_diagrams.tex:4-8 | CUT or SHARPEN thesis not question | REFORGE_MANIFEST:16 |
| R-17 | I | chapters/connections/feynman_diagrams.tex:10-14 | CUT or SHARPEN H/M/S route | REFORGE_MANIFEST:17 |
| R-18 | I | chapters/connections/feynman_diagrams.tex:19-25 | CUT or COMPRESS restates governing question | REFORGE_MANIFEST:18 |
| R-19 | I | chapters/connections/feynman_diagrams.tex:43 | CUT obvious tree-diagram statement | REFORGE_MANIFEST:19 |
| R-20 | I | chapters/connections/feynman_diagrams.tex:60 | CUT or COMPRESS restates vanishing just computed | REFORGE_MANIFEST:20 |
| R-21 | I | chapters/connections/feynman_diagrams.tex:93-102 | CUT metaphorical commentary in computational section | REFORGE_MANIFEST:21 |
| R-22 | I | chapters/connections/feynman_diagrams.tex:141-143 | CUT unrelated phi^4 example | REFORGE_MANIFEST:22 |
| R-23 | I | chapters/connections/feynman_diagrams.tex:153-158 | CUT or COMPRESS restates expansion formula | REFORGE_MANIFEST:23 |
| R-24 | I | chapters/connections/feynman_diagrams.tex:160-163 | COMPRESS convention comparing kappa to g_s | REFORGE_MANIFEST:24 |
| R-25 | I | chapters/connections/feynman_diagrams.tex:256-273 | COMPRESS string theory perspective, no theorem | REFORGE_MANIFEST:25 |
| R-26 | I | chapters/connections/feynman_diagrams.tex:275-293 | CUT summary table restating g=genus, L=loops | REFORGE_MANIFEST:26 |
| R-27 | I | chapters/connections/feynman_diagrams.tex:295-308 | CUT or SHARPEN ill-defined notation | REFORGE_MANIFEST:27 |
| R-28 | I | chapters/connections/feynman_diagrams.tex:370-406 | COMPRESS conj:bar-cobar-path-integral + 30-line scope | REFORGE_MANIFEST:28 |
| R-29 | I | chapters/connections/feynman_diagrams.tex:408-425 | CUT "Three perspectives on kappa" restates 3 chapters | REFORGE_MANIFEST:29 |

#### `chapters/connections/holomorphic_topological.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-30 | I | chapters/connections/holomorphic_topological.tex:4-6 | CUT or SHARPEN thesis not question | REFORGE_MANIFEST:30 |
| R-31 | I | chapters/connections/holomorphic_topological.tex:8-10 | CUT or SHARPEN H/M/S route | REFORGE_MANIFEST:31 |
| R-32 | I | chapters/connections/holomorphic_topological.tex:71-88 | CUT or SHARPEN evidence sketch: 3 steps all say "requires" | REFORGE_MANIFEST:32 |
| R-33 | I | chapters/connections/holomorphic_topological.tex:90-122 | COMPRESS 32-line frontier-order navigation | REFORGE_MANIFEST:33 |
| R-34 | I | chapters/connections/holomorphic_topological.tex:166-190 | COMPRESS 24-line MC4/MC5 boilerplate | REFORGE_MANIFEST:34 |
| R-35 | I | chapters/connections/holomorphic_topological.tex:268-290 | CUT or SHARPEN physics-heavy proof sketch | REFORGE_MANIFEST:35 |
| R-36 | I | chapters/connections/holomorphic_topological.tex:335-343 | CUT restates preceding construction | REFORGE_MANIFEST:36 |
| R-37 | I | chapters/connections/holomorphic_topological.tex:372-402 | CUT or SHARPEN 30-line physics proof sketch | REFORGE_MANIFEST:37 |
| R-38 | I | chapters/connections/holomorphic_topological.tex:417-431 | COMPRESS "beyond scope" boilerplate | REFORGE_MANIFEST:38 |
| R-39 | I | chapters/connections/holomorphic_topological.tex:515-524 | CUT or SHARPEN "Evidence: Physical picture" | REFORGE_MANIFEST:39 |
| R-40 | I | chapters/connections/holomorphic_topological.tex:526-547 | COMPRESS 21-line MC4/MC5 frontier | REFORGE_MANIFEST:40 |
| R-41 | I | chapters/connections/holomorphic_topological.tex:561-582 | COMPRESS 21-line standard boilerplate | REFORGE_MANIFEST:41 |
| R-42 | I | chapters/connections/holomorphic_topological.tex:584-599 | CUT or SHARPEN example names without computation | REFORGE_MANIFEST:42 |
| R-43 | I | chapters/connections/holomorphic_topological.tex:640-655 | COMPRESS standard "homotopy template" | REFORGE_MANIFEST:43 |
| R-44 | I | chapters/connections/holomorphic_topological.tex:658-695 | CUT or SHARPEN 4 physics steps | REFORGE_MANIFEST:44 |
| R-45 | I | chapters/connections/holomorphic_topological.tex:738-756 | CUT or COMPRESS 18 lines citing theorems already in statement | REFORGE_MANIFEST:45 |
| R-46 | I | chapters/connections/holomorphic_topological.tex:814-828 | CUT or COMPRESS physics interp remark restates hbar=epsilon_1 | REFORGE_MANIFEST:46 |
| R-47 | I | chapters/connections/holomorphic_topological.tex:830-845 | COMPRESS two classical limits -- tangential | REFORGE_MANIFEST:47 |
| R-48 | I | chapters/connections/holomorphic_topological.tex:847-856 | CUT or SHARPEN summary remark | REFORGE_MANIFEST:48 |
| R-49 | I | chapters/connections/holomorphic_topological.tex:903-925 | CUT 5-row vague analogies table | REFORGE_MANIFEST:49 |
| R-50 | I | chapters/connections/holomorphic_topological.tex:1014-1024 | CUT scope restates conjecture | REFORGE_MANIFEST:50 |
| R-51 | I | chapters/connections/holomorphic_topological.tex:1072-1073 | CUT or SHARPEN journalistic section title | REFORGE_MANIFEST:51 |
| R-52 | I | chapters/connections/holomorphic_topological.tex:1075-1114 | CUT or COMPRESS near-duplicate of bv_brst thm | REFORGE_MANIFEST:52 |
| R-53 | I | chapters/connections/holomorphic_topological.tex:1116-1136 | CUT 20 lines restating quantum bar = genus expansion | REFORGE_MANIFEST:53 |
| R-54 | I | chapters/connections/holomorphic_topological.tex:1138-1167 | CUT or COMPRESS re-states earlier theorem | REFORGE_MANIFEST:54 |
| R-55 | I | chapters/connections/holomorphic_topological.tex:1169-1300 | COMPRESS 100-line scope with MC4 detail | REFORGE_MANIFEST:55 |
| R-56 | I | chapters/connections/holomorphic_topological.tex:1302-1312 | CUT restates same AGT reformulation | REFORGE_MANIFEST:56 |
| R-57 | I | chapters/connections/holomorphic_topological.tex:1321-1341 | CUT analogies table | REFORGE_MANIFEST:57 |
| R-58 | I | chapters/connections/holomorphic_topological.tex:1392-1401 | CUT scope restates theorem's own paragraph | REFORGE_MANIFEST:58 |
| R-59 | I | chapters/connections/holomorphic_topological.tex:1403-1418 | CUT or COMPRESS speculative Vassiliev invariants | REFORGE_MANIFEST:59 |
| R-60 | I | chapters/connections/holomorphic_topological.tex:1420-1468 | CUT question blocks -- belongs in concordance | REFORGE_MANIFEST:60 |

#### `chapters/connections/physical_origins.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-61 | I | chapters/connections/physical_origins.tex:10-12 | CUT or SHARPEN thesis not question | REFORGE_MANIFEST:61 |
| R-62 | I | chapters/connections/physical_origins.tex:53-55 | CUT or COMPRESS "Status split" | REFORGE_MANIFEST:62 |
| R-63 | I | chapters/connections/physical_origins.tex:78-95 | COMPRESS 17-line "requires input" | REFORGE_MANIFEST:63 |
| R-64 | I | chapters/connections/physical_origins.tex:134-150 | COMPRESS 16-line same pattern | REFORGE_MANIFEST:64 |
| R-65 | I | chapters/connections/physical_origins.tex:155-157 | CUT identical "Status split" | REFORGE_MANIFEST:65 |
| R-66 | I | chapters/connections/physical_origins.tex:180-203 | COMPRESS 23-line boilerplate | REFORGE_MANIFEST:66 |
| R-67 | I | chapters/connections/physical_origins.tex:237-256 | COMPRESS 19-line boilerplate | REFORGE_MANIFEST:67 |
| R-68 | I | chapters/connections/physical_origins.tex:295-311 | COMPRESS 16-line same | REFORGE_MANIFEST:68 |
| R-69 | I | chapters/connections/physical_origins.tex:313-320 | CUT zero math content | REFORGE_MANIFEST:69 |

#### `chapters/connections/feynman_connection.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-70 | I | chapters/connections/feynman_connection.tex:2-4 | CUT or SHARPEN governing question | REFORGE_MANIFEST:70 |
| R-71 | I | chapters/connections/feynman_connection.tex:9-13 | CUT or COMPRESS restates Ch heisenberg-frame | REFORGE_MANIFEST:71 |
| R-72 | I | chapters/connections/feynman_connection.tex:93-102 | CUT DUPLICATE of feynman_diagrams.tex | REFORGE_MANIFEST:72 |
| R-73 | I | chapters/connections/feynman_connection.tex:160-163 | CUT DUPLICATE convention | REFORGE_MANIFEST:73 |
| R-74 | I | chapters/connections/feynman_connection.tex:234-246 | CUT or COMPRESS restates Thm genus-universality | REFORGE_MANIFEST:74 |
| R-75 | I | chapters/connections/feynman_connection.tex:247-254 | CUT or COMPRESS restates Thm explicit-theta | REFORGE_MANIFEST:75 |
| R-76 | I | chapters/connections/feynman_connection.tex:256-273 | COMPRESS string theory perspective | REFORGE_MANIFEST:76 |
| R-77 | I | chapters/connections/feynman_connection.tex:275-293 | CUT DUPLICATE summary table | REFORGE_MANIFEST:77 |
| R-78 | I | chapters/connections/feynman_connection.tex:379-406 | COMPRESS 27-line boilerplate | REFORGE_MANIFEST:78 |
| R-79 | I | chapters/connections/feynman_connection.tex:408-425 | CUT DUPLICATE "Three perspectives on kappa" | REFORGE_MANIFEST:79 |

#### `chapters/connections/genus_complete.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-80 | I | chapters/connections/genus_complete.tex:6-8 | CUT or SHARPEN governing question | REFORGE_MANIFEST:80 |
| R-81 | I | chapters/connections/genus_complete.tex:10-12 | CUT or SHARPEN H/M/S route | REFORGE_MANIFEST:81 |
| R-82 | I | chapters/connections/genus_complete.tex:17-19 | CUT obvious torus statement | REFORGE_MANIFEST:82 |
| R-83 | I | chapters/connections/genus_complete.tex:100-113 | COMPRESS 14-line c=26/c=15 digression | REFORGE_MANIFEST:83 |
| R-84 | I | chapters/connections/genus_complete.tex:116-118 | CUT restates theorem just stated | REFORGE_MANIFEST:84 |
| R-85 | I | chapters/connections/genus_complete.tex:235-239 | CUT or COMPRESS restating Segal/BK | REFORGE_MANIFEST:85 |
| R-86 | I | chapters/connections/genus_complete.tex:317-329 | CUT or COMPRESS 12 lines restating chain-level refines classical | REFORGE_MANIFEST:86 |
| R-87 | I | chapters/connections/genus_complete.tex:566-614 | COMPRESS 48 lines including boilerplate | REFORGE_MANIFEST:87 |
| R-88 | I | chapters/connections/genus_complete.tex:616-623 | CUT vertex=operator, edge=propagator | REFORGE_MANIFEST:88 |
| R-89 | I | chapters/connections/genus_complete.tex:625-672 | COMPRESS AdS/CFT analogies + 23-line scope | REFORGE_MANIFEST:89 |
| R-90 | I | chapters/connections/genus_complete.tex:678-683 | CUT states b_1=2g, dim M_g=3g-3 | REFORGE_MANIFEST:90 |
| R-91 | I | chapters/connections/genus_complete.tex:713-715 | CUT "converse implications largely open" -- vacuous | REFORGE_MANIFEST:91 |

### TIER 2: EXAMPLES (moderate density)

#### `chapters/examples/free_fields.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-92 | I | chapters/examples/free_fields.tex:5-11 | CUT boilerplate remark pair | REFORGE_MANIFEST:92-93 |
| R-93 | I | chapters/examples/free_fields.tex:16-19 | CUT or COMPRESS restates Heisenberg from Ch 1 | REFORGE_MANIFEST:94 |
| R-94 | I | chapters/examples/free_fields.tex:3310-3366 | COMPRESS Weyl group Poisson summation | REFORGE_MANIFEST:95 |
| R-95 | I | chapters/examples/free_fields.tex:3368-3414 | COMPRESS spectral discriminant Plancherel | REFORGE_MANIFEST:96 |
| R-96 | I | chapters/examples/free_fields.tex:3564-3634 | COMPRESS nonlinear Fourier / curved Fourier remarks | REFORGE_MANIFEST:97 |
| R-97 | I | chapters/examples/free_fields.tex:3784-3840 | CUT tikzpicture + echo of duality | REFORGE_MANIFEST:98 |
| R-98 | I | chapters/examples/free_fields.tex:3861-3866 | CUT section "String theory" preamble | REFORGE_MANIFEST:99 |
| R-99 | I | chapters/examples/free_fields.tex:4020-4033 | CUT or SHARPEN bulk-boundary correspondence | REFORGE_MANIFEST:100 |
| R-100 | I | chapters/examples/free_fields.tex:4071-4121 | CUT holographic dictionary table | REFORGE_MANIFEST:101 |
| R-101 | I | chapters/examples/free_fields.tex:4162-4213 | CUT entanglement + loop corrections | REFORGE_MANIFEST:102 |
| R-102 | I | chapters/examples/free_fields.tex:4280-4308 | CUT scope + evidence restating | REFORGE_MANIFEST:103 |
| R-103 | I | chapters/examples/free_fields.tex:4492-4530 | CUT physical motivation + scope | REFORGE_MANIFEST:104 |
| R-104 | I | chapters/examples/free_fields.tex:4692-4734 | CUT fusion rule section duplicating minimal_model_fusion | REFORGE_MANIFEST:105 |

#### `chapters/examples/deformation_examples.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-105 | I | chapters/examples/deformation_examples.tex:9-20 | CUT boilerplate pair + echo | REFORGE_MANIFEST:106-107 |
| R-106 | I | chapters/examples/deformation_examples.tex:80-92 | CUT rehashes coisson distinction | REFORGE_MANIFEST:108 |
| R-107 | I | chapters/examples/deformation_examples.tex:209-218 | CUT or SHARPEN Green-Schwarz in theorem | REFORGE_MANIFEST:109 |
| R-108 | I | chapters/examples/deformation_examples.tex:415-465 | CUT or COMPRESS bar complex interpretation + hierarchy table | REFORGE_MANIFEST:110 |
| R-109 | I | chapters/examples/deformation_examples.tex:569-608 | CUT or COMPRESS symplectic fermion scope + echo | REFORGE_MANIFEST:111 |
| R-110 | I | chapters/examples/deformation_examples.tex:713-743 | CUT or COMPRESS filtered deformation SS description | REFORGE_MANIFEST:112 |

#### `chapters/examples/deformation_quantization.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-111 | I | chapters/examples/deformation_quantization.tex:5-11 | CUT boilerplate pair | REFORGE_MANIFEST:113-114 |
| R-112 | I | chapters/examples/deformation_quantization.tex:14-23 | CUT or COMPRESS DQ reverses the question | REFORGE_MANIFEST:115 |
| R-113 | I | chapters/examples/deformation_quantization.tex:1113-1134 | CUT or COMPRESS quantization obstructions restates | REFORGE_MANIFEST:116 |
| R-114 | I | chapters/examples/deformation_quantization.tex:1137-1150 | CUT open questions -- bare list | REFORGE_MANIFEST:117 |

#### `chapters/examples/toroidal_elliptic.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-115 | I | chapters/examples/toroidal_elliptic.tex:9-14 | CUT boilerplate pair | REFORGE_MANIFEST:118-119 |
| R-116 | I | chapters/examples/toroidal_elliptic.tex:16-32 | CUT or COMPRESS "All examples so far live on a single curve" | REFORGE_MANIFEST:120 |
| R-117 | I | chapters/examples/toroidal_elliptic.tex:1305-1390 | CUT or COMPRESS shuffle algebra echo + remark | REFORGE_MANIFEST:121 |
| R-118 | I | chapters/examples/toroidal_elliptic.tex:1466-1504 | CUT or COMPRESS degeneration limits restates table | REFORGE_MANIFEST:122 |

#### `chapters/examples/minimal_model_examples.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-119 | I | chapters/examples/minimal_model_examples.tex:3-9 | CUT boilerplate pair | REFORGE_MANIFEST:123-124 |
| R-120 | I | chapters/examples/minimal_model_examples.tex:47-53 | CUT orphan 2-liner duplicated | REFORGE_MANIFEST:125 |
| R-121 | I | chapters/examples/minimal_model_examples.tex:469-494 | CUT or SHARPEN Ising bar interp: no computation | REFORGE_MANIFEST:126 |
| R-122 | I | chapters/examples/minimal_model_examples.tex:319-467 | COMPRESS multiple speculative scope remarks | REFORGE_MANIFEST:127 |

#### `chapters/examples/minimal_model_fusion.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-123 | I | chapters/examples/minimal_model_fusion.tex:3-9 | CUT boilerplate pair | REFORGE_MANIFEST:128-129 |
| R-124 | I | chapters/examples/minimal_model_fusion.tex:139-140 | CUT admits absence of computation | REFORGE_MANIFEST:130 |
| R-125 | I | chapters/examples/minimal_model_fusion.tex:265-272 | CUT or COMPRESS Virasoro vs W_3 fusion restates | REFORGE_MANIFEST:131 |
| R-126 | I | chapters/examples/minimal_model_fusion.tex:342-347 | CUT DUPLICATE subsection from minimal_model_examples | REFORGE_MANIFEST:132 |
| R-127 | I | chapters/examples/minimal_model_fusion.tex:791-821 | CUT or SHARPEN MTC speculative remarks | REFORGE_MANIFEST:133 |

### TIER 3: THEORY STRUCTURE

#### `chapters/theory/algebraic_foundations.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-128 | I | chapters/theory/algebraic_foundations.tex:5-11 | CUT boilerplate pair | REFORGE_MANIFEST:134-135 |
| R-129 | I | chapters/theory/algebraic_foundations.tex:12-16 | CUT or COMPRESS restates what Ch heisenberg-frame did | REFORGE_MANIFEST:136 |
| R-130 | I | chapters/theory/algebraic_foundations.tex:289-295 | CUT or COMPRESS excision restated three ways | REFORGE_MANIFEST:137 |
| R-131 | I | chapters/theory/algebraic_foundations.tex:412-419 | CUT panorama of higher_genus chapter | REFORGE_MANIFEST:138 |
| R-132 | I | chapters/theory/algebraic_foundations.tex:582-609 | COMPRESS textbook physics + factorization without computation | REFORGE_MANIFEST:139 |
| R-133 | I | chapters/theory/algebraic_foundations.tex:611-627 | CUT forward ref + universal property restatement | REFORGE_MANIFEST:140 |
| R-134 | I | chapters/theory/algebraic_foundations.tex:715-717 | CUT paraphrases axiom names | REFORGE_MANIFEST:141 |
| R-135 | I | chapters/theory/algebraic_foundations.tex:829-838 | CUT or COMPRESS restates why Weiss covers exist | REFORGE_MANIFEST:142 |
| R-136 | I | chapters/theory/algebraic_foundations.tex:870-882 | CUT or SHARPEN "Coming attractions" closing | REFORGE_MANIFEST:143 |

#### `chapters/theory/configuration_spaces.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-137 | I | chapters/theory/configuration_spaces.tex:5-14 | CUT boilerplate pair + echo | REFORGE_MANIFEST:144-145 |
| R-138 | I | chapters/theory/configuration_spaces.tex:2033-2072 | COMPRESS Arnold proof I excessive setup | REFORGE_MANIFEST:146 |
| R-139 | I | chapters/theory/configuration_spaces.tex:2160-2268 | COMPRESS Arnold proof II (Stokes) 108 lines for textbook fact | REFORGE_MANIFEST:147 |
| R-140 | I | chapters/theory/configuration_spaces.tex:2270-2272 | CUT historical context one-liner | REFORGE_MANIFEST:148 |
| R-141 | I | chapters/theory/configuration_spaces.tex:2284-2387 | COMPRESS Arnold proof III 103 lines, third proof | REFORGE_MANIFEST:149 |
| R-142 | I | chapters/theory/configuration_spaces.tex:2390-2401 | CUT Brieskorn tangent | REFORGE_MANIFEST:150 |
| R-143 | I | chapters/theory/configuration_spaces.tex:2403-2466 | CUT equivalence of three Arnold formulations | REFORGE_MANIFEST:151 |
| R-144 | I | chapters/theory/configuration_spaces.tex:2468-2483 | CUT dictionary between perspectives -- trivial | REFORGE_MANIFEST:152 |
| R-145 | I | chapters/theory/configuration_spaces.tex:2488-2499 | CUT n=2 trivial case | REFORGE_MANIFEST:153 |

#### `chapters/theory/chiral_koszul_pairs.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-146 | I | chapters/theory/chiral_koszul_pairs.tex:10-19 | CUT boilerplate pair | REFORGE_MANIFEST:154-155 |
| R-147 | I | chapters/theory/chiral_koszul_pairs.tex:352-401 | CUT three remarks restating Theorem A | REFORGE_MANIFEST:156 |
| R-148 | I | chapters/theory/chiral_koszul_pairs.tex:465-486 | CUT marketing bullet list + difficulties list | REFORGE_MANIFEST:157 |
| R-149 | I | chapters/theory/chiral_koszul_pairs.tex:569-584 | CUT or COMPRESS restates proof just given | REFORGE_MANIFEST:158 |
| R-150 | I | chapters/theory/chiral_koszul_pairs.tex:825-854 | CUT or COMPRESS restates Step 4 correction | REFORGE_MANIFEST:159 |
| R-151 | I | chapters/theory/chiral_koszul_pairs.tex:918-933 | CUT restates concentration theorem | REFORGE_MANIFEST:160 |

#### `chapters/theory/koszul_pair_structure.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-152 | I | chapters/theory/koszul_pair_structure.tex:8-14 | CUT boilerplate pair | REFORGE_MANIFEST:161-162 |
| R-153 | I | chapters/theory/koszul_pair_structure.tex:1000-1049 | CUT or SHARPEN prose-heavy proof outline | REFORGE_MANIFEST:163 |

#### `chapters/theory/deformation_theory.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-154 | I | chapters/theory/deformation_theory.tex:5-11 | CUT boilerplate pair | REFORGE_MANIFEST:164-165 |
| R-155 | I | chapters/theory/deformation_theory.tex:2089-2108 | CUT or COMPRESS non-scalar landscape restates | REFORGE_MANIFEST:166 |
| R-156 | I | chapters/theory/deformation_theory.tex:2128-2157 | COMPRESS periodicity as exponential metaphor | REFORGE_MANIFEST:167 |
| R-157 | I | chapters/theory/deformation_theory.tex:2246-2296 | CUT or COMPRESS 50-line gap documentation | REFORGE_MANIFEST:168 |
| R-158 | I | chapters/theory/deformation_theory.tex:2336-2393 | CUT or COMPRESS modular periodicity conj + echo remark | REFORGE_MANIFEST:169 |
| R-159 | I | chapters/theory/deformation_theory.tex:2397-2418 | CUT or COMPRESS trivial substitution examples | REFORGE_MANIFEST:170 |

#### `chapters/theory/poincare_duality_quantum.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-160 | I | chapters/theory/poincare_duality_quantum.tex:2-8 | CUT boilerplate pair | REFORGE_MANIFEST:171-172 |
| R-161 | I | chapters/theory/poincare_duality_quantum.tex:19-30 | CUT or SHARPEN Costello-Li holographic conjecture | REFORGE_MANIFEST:173 |
| R-162 | I | chapters/theory/poincare_duality_quantum.tex:32-41 | CUT or SHARPEN genus-graded Koszul duality remark | REFORGE_MANIFEST:174 |
| R-163 | I | chapters/theory/poincare_duality_quantum.tex:64-74 | CUT heuristic motivation (not formal proof) | REFORGE_MANIFEST:175 |
| R-164 | I | chapters/theory/poincare_duality_quantum.tex:90-108 | CUT or SHARPEN M2 branes: names not computations | REFORGE_MANIFEST:176 |
| R-165 | I | chapters/theory/poincare_duality_quantum.tex:127-142 | CUT imported-proof provenance | REFORGE_MANIFEST:177 |
| R-166 | I | chapters/theory/poincare_duality_quantum.tex:144-178 | CUT diagrammatic OPE technique: tikzpicture only | REFORGE_MANIFEST:178 |
| R-167 | I | chapters/theory/poincare_duality_quantum.tex:180-188 | CUT computing Koszul dual OPEs remark | REFORGE_MANIFEST:179 |
| R-168 | I | chapters/theory/poincare_duality_quantum.tex:190-215 | CUT or SHARPEN AdS_3 x S^3 holography | REFORGE_MANIFEST:180 |
| R-169 | I | chapters/theory/poincare_duality_quantum.tex:217-263 | COMPRESS backreaction conjecture + remarks | REFORGE_MANIFEST:181 |
| R-170 | I | chapters/theory/poincare_duality_quantum.tex:265-303 | CUT open-closed string duality tikzpicture | REFORGE_MANIFEST:182 |
| R-171 | I | chapters/theory/poincare_duality_quantum.tex:377-395 | CUT applications list | REFORGE_MANIFEST:183 |
| R-172 | I | chapters/theory/poincare_duality_quantum.tex:463-495 | CUT or SHARPEN Evidence [Kontsevich] + spectral decomp + Lurie remark | REFORGE_MANIFEST:184 |
| R-173 | I | chapters/theory/poincare_duality_quantum.tex:497-531 | CUT Lurie + Gaitsgory insight remarks | REFORGE_MANIFEST:185 |

### TIER 4: MAIN THEORY

#### `chapters/theory/introduction.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-174 | I | chapters/theory/introduction.tex:6-14 | CUT governing question remark | REFORGE_MANIFEST:186 |
| R-175 | I | chapters/theory/introduction.tex:19-36 | CUT or COMPRESS synthetic viewpoint remark | REFORGE_MANIFEST:187 |

#### `chapters/theory/bar_cobar_construction.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-176 | I | chapters/theory/bar_cobar_construction.tex:6-12 | CUT boilerplate pair | REFORGE_MANIFEST:188-189 |
| R-177 | I | chapters/theory/bar_cobar_construction.tex:16-31 | CUT or COMPRESS logarithmic 1-form planted metaphor | REFORGE_MANIFEST:190 |
| R-178 | I | chapters/theory/bar_cobar_construction.tex:22-31 | CUT or SHARPEN "categorical logarithm" before definition | REFORGE_MANIFEST:191 |
| R-179 | I | chapters/theory/bar_cobar_construction.tex:5030-5047 | CUT or COMPRESS rem:positselski-acyclicity | REFORGE_MANIFEST:192 |
| R-180 | I | chapters/theory/bar_cobar_construction.tex:5232-5329 | CUT or COMPRESS Virasoro Koszul dual + MC4 frontier | REFORGE_MANIFEST:193 |
| R-181 | I | chapters/theory/bar_cobar_construction.tex:5421-5440 | CUT rem:mc4-concrete-checklist | REFORGE_MANIFEST:194 |
| R-182 | I | chapters/theory/bar_cobar_construction.tex:5566-5992 | CUT or COMPRESS multiple propositions restating MC4 criteria | REFORGE_MANIFEST:195 |
| R-183 | I | chapters/theory/bar_cobar_construction.tex:6026-6272 | CUT or COMPRESS remarks restating reduction propositions | REFORGE_MANIFEST:196 |
| R-184 | I | chapters/theory/bar_cobar_construction.tex:6324-6695 | CUT or COMPRESS DS stage-growth pipeline | REFORGE_MANIFEST:197 |
| R-185 | I | chapters/theory/bar_cobar_construction.tex:6896-7203 | CUT or COMPRESS stage-4 residual-packet chain | REFORGE_MANIFEST:198 |
| R-186 | I | chapters/theory/bar_cobar_construction.tex:7737-7952 | CUT or COMPRESS MC4 frontier package + closure criteria | REFORGE_MANIFEST:199 |
| R-187 | I | chapters/theory/bar_cobar_construction.tex:8043-8533 | CUT or COMPRESS stage-4 pairing reductions | REFORGE_MANIFEST:200 |
| R-188 | I | chapters/theory/bar_cobar_construction.tex:8628-8800 | CUT or COMPRESS stage-4 local attack order + contraction | REFORGE_MANIFEST:201 |
| R-189 | I | chapters/theory/bar_cobar_construction.tex:9058-15051 | MEGA-COMPRESS ~6000 lines of stage-5 mechanical decomposition. Collapse to 3 results. | REFORGE_MANIFEST:202 |

#### `chapters/theory/higher_genus.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-190 | I | chapters/theory/higher_genus.tex:5-11 | CUT boilerplate pair | REFORGE_MANIFEST:203-204 |

#### `chapters/theory/chiral_modules.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-191 | I | chapters/theory/chiral_modules.tex:5-13 | CUT boilerplate pair | REFORGE_MANIFEST:205-206 |
| R-192 | I | chapters/theory/chiral_modules.tex:15-19 | CUT or COMPRESS restates bar-cobar machinery | REFORGE_MANIFEST:207 |

#### `chapters/frame/heisenberg_frame.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-193 | I | chapters/frame/heisenberg_frame.tex:4-10 | CUT boilerplate pair | REFORGE_MANIFEST:208-209 |
| R-194 | I | chapters/frame/heisenberg_frame.tex:11-21 | CUT or COMPRESS "The first example" remark | REFORGE_MANIFEST:210 |

### TIER 5: EXAMPLES (computational, mostly clean) -- boilerplate pairs

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-195 | I | chapters/examples/kac_moody.tex:5-11 | CUT boilerplate pair | REFORGE_MANIFEST:211-212 |
| R-196 | I | chapters/examples/w_algebras.tex:6-16 | CUT boilerplate pair | REFORGE_MANIFEST:213-214 |
| R-197 | I | chapters/examples/w3_composite_fields.tex:3-9 | CUT boilerplate pair + echo line 15 | REFORGE_MANIFEST:215-216 |
| R-198 | I | chapters/examples/w_algebras_deep.tex:2-9 | CUT boilerplate pair | REFORGE_MANIFEST:217-218 |
| R-199 | I | chapters/examples/beta_gamma.tex:4-10 | CUT boilerplate pair + echo line 11 | REFORGE_MANIFEST:219-220 |
| R-200 | I | chapters/examples/heisenberg_eisenstein.tex:2-8 | CUT boilerplate pair | REFORGE_MANIFEST:221-222 |
| R-201 | I | chapters/examples/lattice_foundations.tex:9-15 | CUT boilerplate pair | REFORGE_MANIFEST:223-224 |
| R-202 | I | chapters/examples/landscape_census.tex:3-9 | CUT boilerplate pair | REFORGE_MANIFEST:225-226 |
| R-203 | I | chapters/examples/bar_complex_tables.tex:5-11 | CUT boilerplate pair | REFORGE_MANIFEST:227-228 |
| R-204 | I | chapters/examples/genus_expansions.tex:4-10 | CUT boilerplate pair | REFORGE_MANIFEST:229 |

### TIER 5: Additional findings in computational example files

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-205 | I | chapters/examples/kac_moody.tex:2537-2552 | CUT terminal echo paragraph | REFORGE_MANIFEST:230 |
| R-206 | I | chapters/examples/kac_moody.tex:3149-3153 | CUT or COMPRESS chapter-end echo | REFORGE_MANIFEST:231 |
| R-207 | I | chapters/examples/w_algebras.tex:2054-2095 | COMPRESS AGT conjecture + scope | REFORGE_MANIFEST:232 |
| R-208 | I | chapters/examples/w_algebras.tex:2097-2148 | CUT holographic interpretation subsection | REFORGE_MANIFEST:233 |
| R-209 | I | chapters/examples/w_algebras.tex:2150-2214 | CUT or COMPRESS 65-line re-summary of Theorems A/B/C | REFORGE_MANIFEST:234 |
| R-210 | I | chapters/examples/w_algebras.tex:2512-2536 | CUT or COMPRESS generic open questions | REFORGE_MANIFEST:235 |

#### `chapters/examples/yangians.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-211 | I | chapters/examples/yangians.tex:6-12 | CUT boilerplate pair | REFORGE_MANIFEST:236-237 |
| R-212 | I | chapters/examples/yangians.tex:1429-1550 | COMPRESS 120-line remark table-of-contents | REFORGE_MANIFEST:238 |
| R-213 | I | chapters/examples/yangians.tex:3345-3399 | CUT 30+20 line restating + trivial normalization | REFORGE_MANIFEST:239 |
| R-214 | I | chapters/examples/yangians.tex:3610-3700 | CUT or SHARPEN CoHA definitions without bar computation | REFORGE_MANIFEST:240 |
| R-215 | I | chapters/examples/yangians.tex:3661-3747 | COMPRESS two scope remarks | REFORGE_MANIFEST:241 |
| R-216 | I | chapters/examples/yangians.tex:3988-3996 | CUT central charge doesn't apply | REFORGE_MANIFEST:242 |
| R-217 | I | chapters/examples/yangians.tex:5016-5051 | CUT or COMPRESS DK ladder re-summary | REFORGE_MANIFEST:243 |
| R-218 | I | chapters/examples/yangians.tex:5727-5900 | COMPRESS 170-line strategy assessment | REFORGE_MANIFEST:244 |
| R-219 | I | chapters/examples/yangians.tex:5963-5968 | CUT meta-commentary | REFORGE_MANIFEST:245 |
| R-220 | I | chapters/examples/yangians.tex:8204-8217 | CUT preamble explaining definitions | REFORGE_MANIFEST:246 |
| R-221 | I | chapters/examples/yangians.tex:8806-10800 | MEGA-COMPRESS ~2000 lines, ~15 props/cors: DK-5 formal categorical extension. Collapse to 3 results. | REFORGE_MANIFEST:247 |

### TIER 6: CONCORDANCE + CONNECTIONS

#### `chapters/connections/concordance.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-222 | I | chapters/connections/concordance.tex:4-10 | CUT boilerplate pair | REFORGE_MANIFEST:248-249 |
| R-223 | I | chapters/connections/concordance.tex:2000-2035 | CUT or COMPRESS MC4 coefficient identity narrative | REFORGE_MANIFEST:250 |

#### `chapters/connections/kontsevich_integral.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-224 | I | chapters/connections/kontsevich_integral.tex:4-10 | CUT boilerplate pair | REFORGE_MANIFEST:251-252 |
| R-225 | I | chapters/connections/kontsevich_integral.tex:358-375 | CUT or SHARPEN "This is not an analogy" emphatic physics | REFORGE_MANIFEST:253 |

#### `chapters/connections/poincare_computations.tex`

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-226 | I | chapters/connections/poincare_computations.tex:4-10 | CUT boilerplate pair | REFORGE_MANIFEST:254-255 |
| R-227 | I | chapters/connections/poincare_computations.tex:292-298 | CUT tautological summary + laundry list | REFORGE_MANIFEST:256-257 |

### TIER 7: APPENDICES -- boilerplate pairs

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-228 | I | appendices/coderived_models.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:258-259 |
| R-229 | I | appendices/combinatorial_frontier.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:260-261 |
| R-230 | I | appendices/signs_and_shifts.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:262-263 |
| R-231 | I | appendices/computational_tables.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:264-265 |
| R-232 | I | appendices/dual_methodology.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:266-267 |
| R-233 | I | appendices/general_relations.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:268-269 |
| R-234 | I | appendices/koszul_reference.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:270-271 |
| R-235 | I | appendices/nilpotent_completion.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:272-273 |
| R-236 | I | appendices/notation_index.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:274-275 |
| R-237 | I | appendices/sign_conventions.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:276-277 |
| R-238 | I | appendices/spectral_higher_genus.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:278-279 |
| R-239 | I | appendices/spectral_sequences.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:280-281 |
| R-240 | I | appendices/theta_functions.tex:boilerplate | CUT boilerplate pair | REFORGE_MANIFEST:282-283 |

### TIER 7: Additional appendix findings

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| R-241 | I | appendices/arnold_relations.tex:29-53 | CUT 25-line "Novel contributions" | REFORGE_MANIFEST:284 |
| R-242 | I | appendices/arnold_relations.tex:96-102 | CUT "Topological heuristic" | REFORGE_MANIFEST:285 |
| R-243 | I | appendices/arnold_relations.tex:162-265 | COMPRESS three proofs of Arnold -- one suffices | REFORGE_MANIFEST:286 |
| R-244 | I | appendices/arnold_relations.tex:285-361 | COMPRESS 75-line attribution history | REFORGE_MANIFEST:287 |
| R-245 | I | appendices/homotopy_transfer.tex:17-60 | CUT 45-line history + physics origins | REFORGE_MANIFEST:288 |
| R-246 | I | appendices/existence_criteria.tex:31-73 | CUT comparison meta-remark + obvious consequences | REFORGE_MANIFEST:289 |
| R-247 | I | appendices/existence_criteria.tex:299-318 | CUT or COMPRESS textbook-style "Problem 1, 2, 3, Solution" | REFORGE_MANIFEST:290 |
| R-248 | I | appendices/combinatorial_frontier.tex:382-411 | CUT speculative sqrt(13) and rationality admissions | REFORGE_MANIFEST:291 |

---

## PART 2: STRIKE LIST (items NOT marked done)

### A. BUILD HEALTH

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-A1 | I | chapters/connections/holomorphic_topological.tex:19 | FIX remove duplicate label `conj:agt-w-algebra` | STRIKE_LIST:A1 |
| S-A2 | I | chapters/connections/bv_brst.tex:1016 | FIX remove duplicate label `conj:holographic-bar-cobar` | STRIKE_LIST:A2 |
| S-A3 | I | chapters/theory/deformation_theory.tex:4063 | FIX undefined ref `def:cyclic-l-infinity-deformation` | STRIKE_LIST:A3 |
| S-A4 | II | chapters/connections/ym_synthesis.tex:280,543 | FIX deduplicate 10 multiply-defined labels | STRIKE_LIST:A4 |
| S-A5 | II | chapters/connections/log_ht_monodromy.tex:103 | FIX rename `\label{sec:foundations}` to `\label{sec:log-ht-foundations}` | STRIKE_LIST:A5 |
| S-A6 | II | main.tex preamble | FIX add `\providecommand` for `\Defmod`, `\Coder`, `\Bmod`, `\orline`, `\StGraph` | STRIKE_LIST:A6 |
| S-A7 | II | chapters/connections/anomaly_completed_topological_holography.tex:1099,1101 | FIX `\text{\rm -mod}` to `\mathrm{-mod}` | STRIKE_LIST:A7 |
| S-A8 | II | multiple files | FIX map 38 undefined citation keys to correct Vol II equivalents | STRIKE_LIST:A8 |
| S-A9 | I | chapters/frame/heisenberg_frame.tex:710,754,1216 | FIX 3 critical overfull boxes | STRIKE_LIST:A9 |
| S-A10 | II | line 63, line 99 | FIX 2 critical overfull boxes | STRIKE_LIST:A10 |

### B. MISSING CLAIM STATUS

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-B1 | I | chapters/connections/bv_brst.tex:148,183,220,... | ADD ClaimStatus to 30+ theorem-class environments | STRIKE_LIST:B1 |
| S-B2 | II | chapters/connections/anomaly_completed_topological_holography.tex:152,190,... | ADD ClaimStatus to 35 environments | STRIKE_LIST:B2 |
| S-B3 | II | chapters/theory/bv-construction.tex | ADD ClaimStatus to 10 environments | STRIKE_LIST:B3 |
| S-B4 | II | chapters/examples/examples-computing.tex | ADD ClaimStatus to 9 environments | STRIKE_LIST:B4 |
| S-B5 | II | chapters/theory/pva-descent.tex | ADD ClaimStatus to 11 environments | STRIKE_LIST:B5 |
| S-B6 | II | chapters/theory/axioms.tex | ADD ClaimStatus to 6 environments | STRIKE_LIST:B6 |
| S-B7 | II | chapters/connections/bar-cobar-review.tex:52,110,170,209,315 | ADD ClaimStatus to 5 environments | STRIKE_LIST:B7 |
| S-B8 | II | chapters/connections/spectral-braiding.tex | ADD ClaimStatus to 5 environments | STRIKE_LIST:B8 |
| S-B9 | II | chapters/connections/brace.tex:51,69,90,153 | ADD ClaimStatus to 4 environments | STRIKE_LIST:B9 |
| S-B10 | II | chapters/connections/celestial_holography.tex:143,191,256 | ADD ClaimStatus to 3 environments | STRIKE_LIST:B10 |

### C. STRUCTURAL INTEGRITY

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-C1 | I | appendices/ordered_associative_chiral_kd.tex:1 | ADD `\chapter{...}` before `\label{chap:ordered-associative-kd}` | STRIKE_LIST:C1 |
| S-C2 | I | appendices/chiral_koszul_casimir_transgression.tex:1 | ADD `\chapter{...}` before `\label{chap:...}` | STRIKE_LIST:C2 |
| S-C3 | I | appendices/modular_dg_shifted_yangian.tex | ADD chapter header (starts with `\providecommand`) | STRIKE_LIST:C3 |
| S-C4 | II | affine_half_space_bv.tex | VERIFY compiles correctly as `\chapter` under memoir with `\input` | STRIKE_LIST:C4 |
| S-C5 | I | holomorphic_topological.tex, physical_origins.tex | VERIFY stub chapters don't produce blank pages | STRIKE_LIST:C5 |
| S-C6 | II | Part II | EVALUATE moving `ht_bulk_boundary_line.tex` and `celestial_boundary_transfer.tex` to Part V | STRIKE_LIST:C6 |
| S-C7 | I | concordance.tex section three-rings | VERIFY refs `\ref{app:nonlinear-modular-shadows}`, `\ref{app:branch-line-reductions}`, `\ref{app:subregular-hook-frontier}` resolve | STRIKE_LIST:C7 |
| S-C8 | I | chapters/connections/semistrict_modular_higher_spin_w3.tex | VERIFY appears in correct Part | STRIKE_LIST:C8 |
| S-C9 | II | celestial_boundary_transfer.tex | VERIFY uses `\providecommand` (not `\newcommand`) | STRIKE_LIST:C9 |
| S-C10 | I | appendices/fm3_planted_forest_residue.tex | VERIFY `\chapter` header renders in appendix environment | STRIKE_LIST:C10 |

### D. FOUR-OBJECT DISTINCTION SWEEP

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-D1 | I | chapters/examples/free_fields.tex:2325 | VERIFY "three dualities" uses "Koszul duality" not "bar-cobar Koszul duality" | STRIKE_LIST:D1 |
| S-D2 | I | appendices/existence_criteria.tex | VERIFY "Koszul dual?" / "Bar-cobar inversion?" labels intact | STRIKE_LIST:D2 |
| S-D3 | I | chapters/examples/genus_expansions.tex | VERIFY sl_2 Theorem A uses "bar construction and Verdier duality" | STRIKE_LIST:D3 |
| S-D4 | I | chapters/examples/kac_moody.tex:153 | VERIFY "For Koszul duality" not "For bar-cobar duality" | STRIKE_LIST:D4 |
| S-D5 | I | chapters/theory/bar_cobar_construction.tex:2858 | VERIFY "bar-cobar inversion" not "bar-cobar duality" | STRIKE_LIST:D5 |
| S-D6 | I | chapters/connections/bv_brst.tex:94 | VERIFY title "QME as Maurer-Cartan equation" | STRIKE_LIST:D6 |
| S-D7 | I | chapters/theory/chiral_modules.tex:2368 | VERIFY remark title "...and the bar complex" | STRIKE_LIST:D7 |
| S-D8 | I | chapters/examples/yangians.tex:6087 | VERIFY "module Koszul duality functor" | STRIKE_LIST:D8 |
| S-D9 | II | chapters/connections/bar-cobar-review.tex | VERIFY genus tower distinguishes curved R-factorization | STRIKE_LIST:D9 |
| S-D10 | I | chapters/theory/bar_cobar_construction.tex:112 | VERIFY four-object table and convolution Lie algebra intact | STRIKE_LIST:D10 |

### E. CROSS-VOLUME COHERENCE

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-E1 | I | chapters/theory/en_koszul_duality.tex | VERIFY `thm:bar-swiss-cheese` compiles and cross-refs resolve | STRIKE_LIST:E1 |
| S-E2 | II | abstract | VERIFY references Vol I's bar complex and Swiss-cheese identification | STRIKE_LIST:E2 |
| S-E3 | I | concordance.tex "Bridges to Volume II" | UPDATE 5 bridge conjectures to reference Vol II Parts IV/V | STRIKE_LIST:E3 |
| S-E4 | II | Part I intro | VERIFY "bar complex presents Swiss-cheese" and Convention 112 ref | STRIKE_LIST:E4 |
| S-E5 | II | Part IV intro | VERIFY `\ref*{rem:fake-complementarity}` from Vol I | STRIKE_LIST:E5 |
| S-E6 | II | Part V intro | VERIFY transgression algebra B_Theta and secondary anomaly u=eta^2 | STRIKE_LIST:E6 |
| S-E7 | I | deformation_theory.tex | VERIFY `thm:ambient-complementarity` has 5 parts and genus shadow cross-refs Thm C | STRIKE_LIST:E7 |
| S-E8 | II | bar-cobar-review.tex | VERIFY `prop:curved-R-factorization` cross-refs Vol I theorems | STRIKE_LIST:E8 |
| S-E9 | I | heisenberg_frame.tex Theorem A summary | VERIFY convolution Lie algebra and Convention 112 cross-ref | STRIKE_LIST:E9 |
| S-E10 | II | bibliography | VERIFY 27 entries from Vol I present without duplicates | STRIKE_LIST:E10 |

### F. MATHEMATICAL CONTENT VERIFICATION

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-F1 | I | prop:formal-legendre | VERIFY tagged `\ClaimStatusConjectured` | STRIKE_LIST:F1 |
| S-F2 | I | ambient complementarity theorem | VERIFY conditional on "cyclic deformation complexes exist as filtered cyclic L-inf algebras" | STRIKE_LIST:F2 |
| S-F3 | I | nonlinear_modular_shadows.tex | VERIFY quartic shadow computed for all 5 frame families | STRIKE_LIST:F3 |
| S-F4 | I | branch_line_reductions.tex | VERIFY genus-3 constant 7 is theorem with proof | STRIKE_LIST:F4 |
| S-F5 | I | typeA_baxter_rees_theta.tex | VERIFY weightwise MC4 distinguished from unweighted | STRIKE_LIST:F5 |
| S-F6 | I | ordered_associative_chiral_kd.tex | VERIFY "new results" appendix tagged ProvedHere | STRIKE_LIST:F6 |
| S-F7 | I | subregular_hook_frontier.tex | VERIFY Bershadsky-Polyakov is first non-principal example | STRIKE_LIST:F7 |
| S-F8 | I | shifted_rtt_duality_orthogonal_coideals.tex | VERIFY three-layer separation is theorem | STRIKE_LIST:F8 |
| S-F9 | I | celestial_bf_frontier_synthesis.tex | VERIFY first Jacobi equation stated precisely | STRIKE_LIST:F9 |
| S-F10 | I | categorical_logarithm_frontier.tex | VERIFY four theorems connected to four logarithm properties | STRIKE_LIST:F10 |
| S-F11 | II | modular_pva_quantization.tex | VERIFY W_3 H^1-sector has exact dimensions | STRIKE_LIST:F11 |
| S-F12 | II | affine_half_space_bv.tex | VERIFY one-loop exactness qualified under H1-H4 | STRIKE_LIST:F12 |
| S-F13 | II | log_ht_monodromy.tex | VERIFY HT associator conditional on quasi-linear class | STRIKE_LIST:F13 |
| S-F14 | II | anomaly_completed_topological_holography.tex | VERIFY genus-Clifford dichotomy stated precisely | STRIKE_LIST:F14 |
| S-F15 | II | ht_bulk_boundary_line.tex | VERIFY corrected triangle A_bulk ~ Z_der ~ HH(A^!) is theorem with hypotheses | STRIKE_LIST:F15 |

### G. TYPOGRAPHIC AND FORMATTING

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-G1 | I | main.tex | VERIFY garamondthm/garamonddef use `4pt plus 1pt minus 1pt` | STRIKE_LIST:G1 |
| S-G2 | II | main.tex | UPDATE theorem spacing to match Vol I | STRIKE_LIST:G2 |
| S-G3 | I | proposition "Universal twisting morphisms" | VERIFY title short enough | STRIKE_LIST:G3 |
| S-G4 | I | Virasoro example title | VERIFY "Virasoro Koszul dual" intact | STRIKE_LIST:G4 |
| S-G5 | I | full build | RUN 2-pass build, report definitive overfull count | STRIKE_LIST:G5 |
| S-G6 | II | full build | RUN 2-pass build, report definitive overfull count | STRIKE_LIST:G6 |
| S-G7 | I | main.tex | VERIFY `\setlength{\abovedisplayskip}{8pt plus 2pt minus 4pt}` | STRIKE_LIST:G7 |
| S-G8 | II | main.tex | ADD matching display math spacing | STRIKE_LIST:G8 |
| S-G9 | I | chapters/ appendices/ | FIX any `\newcommand` in chapter files to `\providecommand` | STRIKE_LIST:G9 |
| S-G10 | II | chapter files | FIX any `\newcommand` in chapter files to `\providecommand` | STRIKE_LIST:G10 |

### H. BIBLIOGRAPHY AND CITATIONS

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-H1 | I | bibliography/references.tex | VERIFY FeiginSemikhatov, FehilyHook, GenraStages, ButsonNair present | STRIKE_LIST:H1 |
| S-H2 | I | bibliography/references.tex | VERIFY HZ24, ZhangTheta24 present | STRIKE_LIST:H2 |
| S-H3 | I | bibliography/references.tex | VERIFY GZ26 present | STRIKE_LIST:H3 |
| S-H4 | I | main.log | FIX `grep 'Citation.*undefined'` -- fix any remaining | STRIKE_LIST:H4 |
| S-H5 | II | all files | FIX all 38 undefined citation keys | STRIKE_LIST:H5 |
| S-H6 | II | bibliography | VERIFY `\bibitem{CF00}` present | STRIKE_LIST:H6 |
| S-H7 | I | bibliography/references.tex | FIX duplicate `\bibitem` entries | STRIKE_LIST:H7 |
| S-H8 | II | inline bibliography | FIX duplicate bib entries | STRIKE_LIST:H8 |
| S-H9 | I | Swiss-cheese section | VERIFY `\cite{Voronov99}` (not `\cite{Vor99}`) | STRIKE_LIST:H9 |
| S-H10 | II | moved chapters | VERIFY all use Vol II citation keys | STRIKE_LIST:H10 |

### I. COMPUTE/TEST INTEGRITY

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-I1 | I | test suite | RUN `make test` -- verify 0 failures | STRIKE_LIST:I1 |
| S-I2 | I | scripts | RUN `python3 scripts/generate_metadata.py` -- verify census | STRIKE_LIST:I2 |
| S-I3 | I | metadata/census.json | VERIFY `Open: 0` | STRIKE_LIST:I3 |
| S-I4 | I | test suite | VERIFY sl_2 bar H^2=5 test in fast suite | STRIKE_LIST:I4 |
| S-I5 | I | test suite | VERIFY d_bracket^2 != 0 test in fast suite | STRIKE_LIST:I5 |

### J. FRONTIER RESEARCH

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-J1 | I | Heisenberg | COMPUTE cubic term of S_A (first genuine-vs-fake discriminant) | STRIKE_LIST:J1 |
| S-J2 | I | sl_2-hat | COMPUTE cubic term of S_A (first non-abelian cubic shadow) | STRIKE_LIST:J2 |
| S-J3 | I | W_3 | VERIFY quartic resonance class R^mod_{4,g,n} against semistrict W_3 chapter | STRIKE_LIST:J3 |
| S-J4 | I | Bershadsky-Polyakov | PROVE/DISPROVE W_3^(2) strictly Koszul at any admissible level | STRIKE_LIST:J4 |
| S-J5 | I | MC4 | EXTEND weightwise MC4 to non-principal case | STRIKE_LIST:J5 |
| S-J6 | I | free fermion | COMPUTE complementarity potential S_A (should match Heisenberg by Lie-Com duality) | STRIKE_LIST:J6 |
| S-J7 | I | filtered trace | PROVE filtered trace-detecting uniqueness unconditionally | STRIKE_LIST:J7 |
| S-J8 | I | sl_2 | VERIFY shifted RTT boundary quotient produces quantized Kleinian surface | STRIKE_LIST:J8 |
| S-J9 | I | FM_4 | EXTEND FM_3 planted-forest L-inf model to FM_4 | STRIKE_LIST:J9 |
| S-J10 | I | test suite | WRITE test verifying universal genus-3 constant 7 | STRIKE_LIST:J10 |

### K. PROOF FORTIFICATION

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-K1 | I | chapters/theory/higher_genus.tex:~9137 | DECOMPOSE 242-line proof into 3-4 named lemmas | STRIKE_LIST:K1 |
| S-K2 | I | chapters/theory/bar_cobar_construction.tex:~2338 | EXTRACT "coderivation Leibniz" as standalone lemma | STRIKE_LIST:K2 |
| S-K3 | I | chapters/theory/chiral_koszul_pairs.tex | VERIFY Theorem A proof A0/A1/A2 steps have forward refs | STRIKE_LIST:K3 |
| S-K4 | I | chapters/theory/deformation_theory.tex | CONVERT "cyclic minimal-model transfer" into lemma | STRIKE_LIST:K4 |
| S-K5 | I | chapters/theory/higher_genus.tex | VERIFY Theorem B coderived part (b) clearly marked conditional | STRIKE_LIST:K5 |
| S-K6 | I | chapters/theory/poincare_duality.tex | VERIFY intrinsic A^! definition (Construction 248) complete | STRIKE_LIST:K6 |
| S-K7 | I | chapters/theory/en_koszul_duality.tex | STRENGTHEN Swiss-cheese proof: collision residues commute with interval splitting sign computation | STRIKE_LIST:K7 |
| S-K8 | I | chapters/theory/bar_cobar_construction.tex | VERIFY Berger-Fresse citation correct theorem number | STRIKE_LIST:K8 |
| S-K9 | I | appendices/nonlinear_modular_shadows.tex | VERIFY every clutching identity has explicit proof | STRIKE_LIST:K9 |
| S-K10 | I | appendices/branch_line_reductions.tex | VERIFY genus-2 transparency proof self-contained (no Ring 3 dependency) | STRIKE_LIST:K10 |
| S-K11 | I | appendices/typeA_baxter_rees_theta.tex | VERIFY Schur-envelope formula proof complete | STRIKE_LIST:K11 |
| S-K12 | I | appendices/ordered_associative_chiral_kd.tex | VERIFY Calabi-Yau transport is proved consequence | STRIKE_LIST:K12 |
| S-K13 | I | appendices/casimir_divisor_core_transport.tex | VERIFY "single Casimir separates spectrum" for all simple types | STRIKE_LIST:K13 |
| S-K14 | II | chapters/connections/affine_half_space_bv.tex | VERIFY one-loop exactness cites Gwilliam-Williams | STRIKE_LIST:K14 |
| S-K15 | II | chapters/connections/anomaly_completed_topological_holography.tex | VERIFY Morita-triviality has complete proof | STRIKE_LIST:K15 |

### L. CROSS-REFERENCE DENSITY

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-L1 | I | appendices/categorical_logarithm_frontier.tex | ADD `\ref` to four theorems it characterizes | STRIKE_LIST:L1 |
| S-L2 | I | appendices/nonlinear_modular_shadows.tex | ADD backward ref to ambient complementarity in deformation_theory.tex | STRIKE_LIST:L2 |
| S-L3 | I | appendices/lifted_spectral_defect_calculus.tex | ADD ref to `branch_line_reductions.tex` | STRIKE_LIST:L3 |
| S-L4 | I | appendices/celestial_bf_frontier_synthesis.tex | ADD ref to Vol II anomaly_completed chapter | STRIKE_LIST:L4 |
| S-L5 | I | concordance.tex section three-rings | SYSTEMATIZE all appendix refs as `\ref` (not text) | STRIKE_LIST:L5 |
| S-L6 | I | appendices/subregular_hook_frontier.tex | ADD ref to `w_algebras_framework.tex` and `w_algebras_deep.tex` | STRIKE_LIST:L6 |
| S-L7 | I | appendices/shifted_rtt_duality_orthogonal_coideals.tex | ADD ref to yangians DK ladder and typeA weightwise MC4 | STRIKE_LIST:L7 |
| S-L8 | II | Part IV intro | ADD `\ref*` to `rem:fake-complementarity` and `def:complementarity-potential` | STRIKE_LIST:L8 |
| S-L9 | II | Part V intro | ADD `\ref*` to `thm:ambient-complementarity` and `conv:bar-coalgebra-identity` | STRIKE_LIST:L9 |
| S-L10 | I | appendices/dg_shifted_factorization_bridge.tex | ADD ref to `modular_dg_shifted_yangian.tex` | STRIKE_LIST:L10 |

### M. INDEX COMPLETION

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-M1 | I | chapters/theory/en_koszul_duality.tex | ADD `\index{Swiss-cheese operad}` beyond the definition | STRIKE_LIST:M1 |
| S-M2 | I | chapters/theory/deformation_theory.tex | ADD `\index{complementarity potential}` | STRIKE_LIST:M2 |
| S-M3 | I | concordance.tex | VERIFY `\index{three concentric rings}` renders | STRIKE_LIST:M3 |
| S-M4 | I | appendices/categorical_logarithm_frontier.tex | ADD `\index{categorical logarithm|textbf}` | STRIKE_LIST:M4 |
| S-M5 | I | appendices/fm3_planted_forest_residue.tex | ADD `\index{planted-forest $L_\infty$-algebra}` | STRIKE_LIST:M5 |
| S-M6 | I | appendices/casimir_divisor_core_transport.tex | ADD `\index{Casimir recurrence module}` | STRIKE_LIST:M6 |
| S-M7 | I | appendices/typeA_baxter_rees_theta.tex | ADD `\index{weightwise stabilization}` | STRIKE_LIST:M7 |
| S-M8 | I | appendices/shifted_rtt_duality_orthogonal_coideals.tex | ADD `\index{orthogonal coideal}` | STRIKE_LIST:M8 |
| S-M9 | I | appendices/nonlinear_modular_shadows.tex | ADD `\index{quartic resonance class}` | STRIKE_LIST:M9 |
| S-M10 | I | appendices/branch_line_reductions.tex | ADD `\index{branch-line reduction}` | STRIKE_LIST:M10 |

### N. NOTATION CONSISTENCY

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-N1 | I | global | STANDARDIZE `\mathfrak{g}` vs `\fg` | STRIKE_LIST:N1 |
| S-N2 | I | global | STANDARDIZE `\bar{B}` vs `\barB` | STRIKE_LIST:N2 |
| S-N3 | I | global | USE `\Conf` macro everywhere (not inline `C_n(X)`) | STRIKE_LIST:N3 |
| S-N4 | I | global | USE `\ChirHoch` everywhere (not inline `CH^*`) | STRIKE_LIST:N4 |
| S-N5 | II | global | USE `\Ainf` everywhere (not inline `A_\infty`) | STRIKE_LIST:N5 |
| S-N6 | I | global | VERIFY `\kappa` for modular characteristic throughout | STRIKE_LIST:N6 |
| S-N7 | I | global | VERIFY `\omega_g` for Arakelov form throughout | STRIKE_LIST:N7 |
| S-N8 | I | frontier appendices | VERIFY `\dzero`, `\dfib`, `\Dg{g}` used consistently | STRIKE_LIST:N8 |
| S-N9 | II | global | USE `\SCchtop` everywhere (not inline `\mathsf{SC}^{\mathrm{ch,top}}`) | STRIKE_LIST:N9 |
| S-N10 | I | global | VERIFY only `\ClaimStatusProvedHere` (no variants) for proved-here claims | STRIKE_LIST:N10 |

### O. COMPUTATIONAL VERIFICATION

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-O1 | I | test suite | WRITE test: quartic shadow vanishes for Heisenberg | STRIKE_LIST:O1 |
| S-O2 | I | test suite | WRITE test: cubic shadow proportional to Casimir for sl_2-hat | STRIKE_LIST:O2 |
| S-O3 | I | test suite | WRITE test: genus-2 transparency quotient trivial for rank-two | STRIKE_LIST:O3 |
| S-O4 | I | test suite | WRITE test: Feigin-Semikhatov Bell-recursive OPE for W_3^(2) | STRIKE_LIST:O4 |
| S-O5 | I | test suite | WRITE test: spectral discriminant Delta_A for Virasoro | STRIKE_LIST:O5 |
| S-O6 | I | test suite | WRITE test: common two-sheet sl_2-hat / Virasoro | STRIKE_LIST:O6 |
| S-O7 | I | test suite | WRITE test: weightwise bar tower stabilization Y(sl_2) weights 0-4 | STRIKE_LIST:O7 |
| S-O8 | I | test suite | WRITE test: planted-forest cubic bracket on FM_3 non-zero for sl_2 | STRIKE_LIST:O8 |
| S-O9 | I | test suite | WRITE test: seed propagation formula matches additive spectral kernel | STRIKE_LIST:O9 |
| S-O10 | I | test suite | WRITE test: orthogonal coideal at Kleinian point for sl_2 | STRIKE_LIST:O10 |

### P. EXPOSITION UPGRADES

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-P1 | I | chapters/theory/introduction.tex | ADD paragraph on Swiss-cheese and R-direction factorization | STRIKE_LIST:P1 |
| S-P2 | I | chapters/theory/introduction.tex | ADD three-ring summary subsection | STRIKE_LIST:P2 |
| S-P3 | I | chapters/frame/heisenberg_frame.tex | ADD remark connecting to Swiss-cheese | STRIKE_LIST:P3 |
| S-P4 | I | concordance.tex | UPDATE census numbers (~1,700 claims, ~1,960 pages) | STRIKE_LIST:P4 |
| S-P5 | I | concordance.tex | UPDATE DK ladder for shifted RTT boundary quotient | STRIKE_LIST:P5 |
| S-P6 | I | concordance.tex | UPDATE MC4 for weightwise stabilization | STRIKE_LIST:P6 |
| S-P7 | I | concordance.tex | ADD entry for modular dg-shifted Yangian | STRIKE_LIST:P7 |
| S-P8 | II | abstract | UPDATE page/chapter counts | STRIKE_LIST:P8 |
| S-P9 | II | conclusion.tex | EXPAND to reference Parts IV/V | STRIKE_LIST:P9 |
| S-P10 | II | concordance.tex | EXPAND from 147 lines to proper constitution | STRIKE_LIST:P10 |
| S-P11 | I | chapters/examples/landscape_census.tex | ADD Bershadsky-Polyakov row | STRIKE_LIST:P11 |
| S-P12 | I | chapters/examples/w_algebras.tex | ADD forward ref to subregular hook appendix | STRIKE_LIST:P12 |
| S-P13 | I | chapters/examples/yangians.tex | ADD forward ref to typeA_baxter_rees_theta | STRIKE_LIST:P13 |
| S-P14 | I | chapters/examples/yangians.tex | ADD forward ref to shifted_rtt_duality | STRIKE_LIST:P14 |
| S-P15 | I | chapters/examples/yangians.tex | ADD forward ref to dg_shifted_factorization_bridge | STRIKE_LIST:P15 |

### Q. VOL II CHAPTER QUALITY

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-Q1 | II | chapters/connections/ym_synthesis.tex:280,543 | DEDUPLICATE content | STRIKE_LIST:Q1 |
| S-Q2 | II | chapters/connections/modular_pva_quantization.tex | ADD `\providecommand` for 5 undefined macros | STRIKE_LIST:Q2 |
| S-Q3 | II | chapters/connections/log_ht_monodromy.tex | RENAME `\label{sec:foundations}` to avoid conflict | STRIKE_LIST:Q3 |
| S-Q4 | II | chapters/connections/anomaly_completed_topological_holography.tex | FIX `\rm` to `\mathrm` | STRIKE_LIST:Q4 |
| S-Q5 | II | chapters/connections/ht_bulk_boundary_line.tex | VERIFY no `\newcommand` remains | STRIKE_LIST:Q5 |
| S-Q6 | II | chapters/connections/celestial_holography.tex | ADD ClaimStatus to 3 untagged environments | STRIKE_LIST:Q6 |
| S-Q7 | II | chapters/connections/fm3_planted_forest_synthesis.tex | MOVE `\providecommand` to main.tex | STRIKE_LIST:Q7 |
| S-Q8 | II | chapters/connections/affine_half_space_bv.tex | VERIFY `\chapter` works with `\input` | STRIKE_LIST:Q8 |
| S-Q9 | II | Part II | EVALUATE moving `ht_bulk_boundary_line` and `celestial_boundary_transfer` to Part V | STRIKE_LIST:Q9 |
| S-Q10 | II | equivalence.tex | VERIFY included or absorbed | STRIKE_LIST:Q10 |
| S-Q11 | II | pva-preview.tex | VERIFY included or absorbed | STRIKE_LIST:Q11 |
| S-Q12 | II | chapters/examples/w-algebras.tex | ADD cross-volume DS reduction remarks | STRIKE_LIST:Q12 |
| S-Q13 | II | chapters/examples/examples-worked.tex | EXPAND or absorb into `examples-complete.tex` | STRIKE_LIST:Q13 |
| S-Q14 | II | chapters/connections/conclusion.tex | EXPAND to summarize five-part architecture | STRIKE_LIST:Q14 |
| S-Q15 | II | chapters/connections/concordance.tex | EXPAND from 147 lines to proper constitution | STRIKE_LIST:Q15 |

### R. METADATA AND INFRASTRUCTURE

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-R1 | I | scripts | RUN `python3 scripts/generate_metadata.py` and commit | STRIKE_LIST:R1 |
| S-R2 | I | census | VERIFY census reflects new appendices (~200+ new claims) | STRIKE_LIST:R2 |
| S-R3 | I | notes/autonomous_state.md | UPDATE | STRIKE_LIST:R3 |
| S-R4 | I | .gitignore | VERIFY includes `archive/` | STRIKE_LIST:R4 |
| S-R5 | II | scripts/ | CREATE build script matching Vol I | STRIKE_LIST:R5 |
| S-R6 | II | metadata/ | CREATE census script | STRIKE_LIST:R6 |
| S-R7 | I | test suite | VERIFY `make test` passes after appendix additions | STRIKE_LIST:R7 |
| S-R8 | I | build | RUN 3-pass build, verify convergence | STRIKE_LIST:R8 |
| S-R9 | II | build | RUN 2-pass build, record page/error/overfull counts | STRIKE_LIST:R9 |
| S-R10 | Both | build | VERIFY simultaneous builds don't interfere | STRIKE_LIST:R10 |

### S. DEEP MATHEMATICAL FRONTIER

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-S1 | I | sl_2-hat | PROVE S_A non-quadratic (genuine complementarity != fake) | STRIKE_LIST:S1 |
| S-S2 | I | Heisenberg FM_3 | PROVE planted-forest cubic vanishes (abelian = quadratic) | STRIKE_LIST:S2 |
| S-S3 | I | Bershadsky-Polyakov | COMPUTE spectral discriminant Delta_A for W_3^(2) | STRIKE_LIST:S3 |
| S-S4 | I | Virasoro genus 3 | COMPUTE branch-line reduction quotient -- verify constant 7 | STRIKE_LIST:S4 |
| S-S5 | I | GKO | PROVE diagonal GKO transgression unconditionally | STRIKE_LIST:S5 |
| S-S6 | I | celestial BF | COMPUTE first positive KK shell for sl_3 | STRIKE_LIST:S6 |
| S-S7 | I | filtered trace | PROVE filtered trace-detecting uniqueness at two-channel level | STRIKE_LIST:S7 |
| S-S8 | I | Baxter-Rees | CONSTRUCT boundary Kodaira-Spencer class | STRIKE_LIST:S8 |
| S-S9 | I | sl_2 | VERIFY dg-shifted factorization bridge strictification | STRIKE_LIST:S9 |
| S-S10 | I | sl_2 genus 1 | COMPUTE modular Yang-Baxter class | STRIKE_LIST:S10 |
| S-S11 | I | W_4 | PROVE W-normal form vanishing extends from W_3 to W_4 | STRIKE_LIST:S11 |
| S-S12 | I | W_7^(2) | COMPUTE Miura-Appell symbols | STRIKE_LIST:S12 |
| S-S13 | I | rank 2 | PROVE orthogonal coideal | STRIKE_LIST:S13 |
| S-S14 | I | metaplectic | VERIFY metaplectic anomaly matches Weil representation theory | STRIKE_LIST:S14 |
| S-S15 | I | Heisenberg genus 1 | CONSTRUCT genus-Clifford completion test | STRIKE_LIST:S15 |

### T. AESTHETIC AND STRUCTURAL

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-T1 | I | chapters/theory/introduction.tex | REWRITE opening to lead with categorical logarithm | STRIKE_LIST:T1 |
| S-T2 | I | chapters/frame/heisenberg_frame.tex | ADD road map diagram | STRIKE_LIST:T2 |
| S-T3 | I | concordance.tex | ADD DK ladder as tikz dependency diagram | STRIKE_LIST:T3 |
| S-T4 | I | concordance.tex | ADD three-ring diagram as tikz figure | STRIKE_LIST:T4 |
| S-T5 | II | abstract | REWRITE Swiss-cheese as FIRST sentence | STRIKE_LIST:T5 |
| S-T6 | II | Part IV | ADD "proved/remains" summary table | STRIKE_LIST:T6 |
| S-T7 | II | Part V | ADD "proved/remains" summary table | STRIKE_LIST:T7 |
| S-T8 | I | frontier appendices | ADD "Status and scope" remark first in every appendix | STRIKE_LIST:T8 |
| S-T9 | I | frontier appendices | ADD "What is proved here" summary in every appendix | STRIKE_LIST:T9 |
| S-T10 | I | concordance/appendices | ADD master table of frontier appendices with theorem counts and Ring assignment | STRIKE_LIST:T10 |
| S-T11 | I | chapters/theory/en_koszul_duality.tex | UPDATE section en-summary to include Swiss-cheese as item 6 | STRIKE_LIST:T11 |
| S-T12 | II | conclusion.tex | PROMOTE to genuine synthesis chapter | STRIKE_LIST:T12 |
| S-T13 | Both | notation | CREATE shared notation page includable in both volumes | STRIKE_LIST:T13 |
| S-T14 | I | TOC | VERIFY all frontier appendix titles render | STRIKE_LIST:T14 |
| S-T15 | II | TOC | VERIFY all five Parts show | STRIKE_LIST:T15 |

### U. FINAL INTEGRITY

| # | VOL | FILE:LINE | EDIT | SRC |
|---|-----|-----------|------|-----|
| S-U1 | I | global | GREP for unmatched `\begin{proof}` / `\end{proof}` | STRIKE_LIST:U1 |
| S-U2 | I | global | GREP for unmatched `\begin{theorem}` / `\end{theorem}` | STRIKE_LIST:U2 |
| S-U3 | II | global | SAME unmatched environment check | STRIKE_LIST:U3 |
| S-U4 | I | frontier appendices | VERIFY no `\include` (vs `\input`) | STRIKE_LIST:U4 |
| S-U5 | I | global | CHECK for circular references | STRIKE_LIST:U5 |
| S-U6 | I | global | FIND orphan labels (defined but never referenced) | STRIKE_LIST:U6 |
| S-U7 | II | global | VERIFY no theorem counter resets mid-chapter | STRIKE_LIST:U7 |
| S-U8 | I | main.tex | VERIFY `\makeindex` and `\printindex` present | STRIKE_LIST:U8 |
| S-U9 | Both | main.tex | VERIFY `\setlength{\emergencystretch}{3em}` | STRIKE_LIST:U9 |
| S-U10 | I | main.tex | VERIFY `\hfuzz=1pt` | STRIKE_LIST:U10 |
| S-U11 | I | global | VERIFY no `\providecommand` conflicts with main.tex definitions | STRIKE_LIST:U11 |
| S-U12 | II | global | VERIFY `\providecommand{\Ainf}` doesn't conflict with `\newcommand{\Ainf}` | STRIKE_LIST:U12 |
| S-U13 | I | bibliography | VERIFY alphabetically sorted | STRIKE_LIST:U13 |
| S-U14 | II | bibliography | VERIFY no duplicate bib keys | STRIKE_LIST:U14 |
| S-U15 | I | PDF | CHECK for `??` in compiled PDF | STRIKE_LIST:U15 |
| S-U16 | II | PDF | SAME | STRIKE_LIST:U16 |
| S-U17 | I | scripts/build.sh | VERIFY `buf_size=1000000` | STRIKE_LIST:U17 |
| S-U18 | I | test suite | VERIFY `make test-full` works | STRIKE_LIST:U18 |
| S-U19 | Both | git | VERIFY clean `git status` | STRIKE_LIST:U19 |
| S-U20 | Both | git | VERIFY commit history coherent | STRIKE_LIST:U20 |
| S-U21 | I | Makefile | VERIFY `SOURCES` wildcard includes `appendices/*.tex` | STRIKE_LIST:U21 |
| S-U22 | I | git | TAG `v43-session-complete` | STRIKE_LIST:U22 |
| S-U23 | II | git | TAG `v2-session-complete` | STRIKE_LIST:U23 |
| S-U24 | I | Makefile | VERIFY `make clean` doesn't delete frontier appendices | STRIKE_LIST:U24 |
| S-U25 | Both | PDF | VERIFY file sizes reasonable (Vol I ~8MB, Vol II ~2MB) | STRIKE_LIST:U25 |

---

## SUMMARY COUNTS

| Source | Items |
|--------|-------|
| FORMULA-FIX (unpropagated audit) | 5 |
| REFORGE_MANIFEST (prose cleanup) | 248 |
| STRIKE_LIST (all open) | 250 |
| **TOTAL** | **503** |

### By priority:

| Priority | Count | Sources |
|----------|-------|---------|
| CRITICAL (formula fixes + build health) | 15 | FF-1..5, S-A1..10 |
| HIGH (claim status, structural, four-object, math content, proof, Vol II quality) | 95 | S-B1..10, S-C1..10, S-D1..10, S-F1..15, S-K1..15, S-Q1..15, S-I1..5 |
| MEDIUM (cross-vol, typo, bib, xref, index, notation, expo, metadata, aesthetic, integrity) | 125 | S-E1..10, S-G1..10, S-H1..10, S-L1..10, S-M1..10, S-N1..10, S-P1..15, S-R1..10, S-T1..15, S-U1..25 |
| FRONTIER (research + computational) | 35 | S-J1..10, S-O1..10, S-S1..15 |
| REFORGE (prose) | 248 | R-1..248 |

### MEGA items (highest line savings):

| Item | File | Est. lines recoverable |
|------|------|----------------------|
| R-189 | bar_cobar_construction.tex:9058-15051 | ~7,000-8,000 |
| R-221 | yangians.tex:8806-10800 | ~1,500-1,700 |
| R-55 | holomorphic_topological.tex:1169-1300 | ~130 |
| R-182..188 | bar_cobar_construction.tex:5566-8800 | ~3,200 combined |
