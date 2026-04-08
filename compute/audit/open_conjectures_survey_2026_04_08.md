# Open Conjectures Survey — 2026-04-08

## Aggregate Counts

| Volume | ClaimStatusConjectured occurrences | Unique conj: labels | Files with conjectures |
|--------|-------------------------------------|----------------------|------------------------|
| Vol I  | 263 (chapters+appendices)           | 309                  | 52                     |
| Vol II | 189                                 | 73                   | 43                     |
| Vol III| 45                                  | 80                   | 12                     |
| **Total** | **497**                          | **462**              | **107**                |

Note: 21 conj: labels in Vol I have been upgraded to theorems (ProvedHere) but retain
backward-compatible conj: labels (e.g., conj:pixton-from-shadows, conj:operadic-complexity-detailed,
conj:platonic-completion, conj:tropical-koszulness, conj:differential-square-zero, etc.).
These are NOT open conjectures despite the conj: prefix.

## Top 10 Most Load-Bearing Open Conjectures

Ranked by downstream dependency (cross-reference count across all three volumes)
and mathematical centrality. Only genuinely open conjectures included.

### 1. conj:master-bv-brst
- **File**: chapters/connections/editorial_constitution.tex (line 434)
- **Summary**: BV/BRST complex coincides with bar complex of the associated chiral algebra at all genera. The genus-0 identification is proved; what remains is the all-genera physics-mathematics bridge.
- **This session**: No progress. This is a mathematical-physics bridge conjecture, logically downstream of the purely algebraic core.

### 2. conj:master-dk-kl
- **File**: chapters/connections/editorial_constitution.tex (line 250)
- **Summary**: The proved DK comparison on the evaluation-generated core extends to a full equivalence on the derived category, completing the Kazhdan-Lusztig conjecture via bar-cobar technology.
- **This session**: No progress. Depends on DK-4/5 (extension beyond evaluation modules).

### 3. conj:master-infinite-generator
- **File**: chapters/connections/editorial_constitution.tex (line 317)
- **Summary**: The structural completion framework (MC4) is proved; what remains is H-level target identification for specific infinite-generator families (construct explicit completed bar-cobar data for W_{1+infinity}, affine Yangians, etc.).
- **This session**: No progress. Example-specific coefficient stabilization task.

### 4. conj:w-orbit-duality
- **File**: chapters/examples/w_algebras.tex (line 472)
- **Summary**: W-algebra Koszul duality for general nilpotent: W^k(g,f)^! = W^{k'}(g,f^D) where f^D is the Barbasch-Vogan dual. Proved for principal (Feigin-Frenkel) and hook-type in type A; open for general nilpotent.
- **This session**: No progress. Active research direction (Direction 4).

### 5. conj:full-derived-dk (DK-3)
- **File**: chapters/examples/yangians_drinfeld_kohno.tex (line 542)
- **Summary**: The factorization-categorical DK/KL bridge extends from evaluation-generated core to the full E1-factorization category Fact_{E1}(Y(g)) = KL_k(g-hat).
- **This session**: No progress. Downstream of MC3 (which is proved for all simple types).

### 6. conj:ds-kd-arbitrary-nilpotent
- **File**: chapters/examples/w_algebras_deep.tex (line 1969)
- **Summary**: DS-KD intertwining for arbitrary nilpotent: the natural comparison map bar(W^k(g,f)) -> DS_f(bar(V_k(g))) is a quasi-isomorphism at generic level for every nilpotent f.
- **This session**: No progress. Proved for principal and hook-type; general case open.

### 7. conj:analytic-realization
- **File**: chapters/connections/genus_complete.tex (line 1720)
- **Summary**: Analytic realization criterion: a unitary full VOA satisfying conformal OS axioms and HS-sewing admits IndHilb-valued factorization homology recovering its partition functions at all genera.
- **This session**: No progress. Part of the analytic sewing programme (Direction 2).

### 8. conj:scalar-saturation-universality
- **File**: chapters/theory/higher_genus_modular_koszul.tex (line 8772)
- **Summary**: The effective Gamma-quadruple reduction extends to ALL modular Koszul chiral algebras at non-critical levels (not just algebraic families with rational OPE coefficients).
- **This session**: No progress. Residual universality conjecture restricted to non-algebraic-family constructions.

### 9. conj:type-a-transport-to-transpose
- **File**: chapters/connections/subregular_hook_frontier.tex (line 298)
- **Summary**: In type A, the transport-closure of hook vertices covers all of Par(N), and Koszul duality intertwines all proved reduction edges. Consequently W_k(sl_N, f_lambda)^! = W_{k^v}(sl_N, f_{lambda^t}).
- **This session**: No progress. Active frontier (Direction 4).

### 10. conj:d-module-purity-koszulness
- **File**: chapters/theory/bar_cobar_adjunction_inversion.tex (line 2494)
- **Summary**: D-module purity criterion for Koszulness: the converse direction (Koszulness implies D-module purity via PBW filtration = Saito weight filtration from MHM on FM_n(X)). Forward direction proved; converse open. Proved for affine KM via chiral localization + Hitchin.
- **This session**: No progress. 13th Koszulness characterization, one-directional.

## Notable Upgraded Conjectures (no longer open)

These conj: labels retain backward-compatible names but are now proved theorems:

| Label | Status | Key result |
|-------|--------|------------|
| conj:pixton-from-shadows | ProvedHere | Pixton ideal from shadow obstruction tower |
| conj:operadic-complexity-detailed | ProvedHere | r_max(A) = A-infinity-depth = L-infinity-formality level |
| conj:platonic-completion | ProvedHere | Every positive-energy chiral algebra has finite resonance rank |
| conj:tropical-koszulness | ProvedHere | Tropical Koszulness equivalence |
| conj:differential-square-zero | ProvedHere | D^2 = 0 at ambient level |
| conj:shadow-depth-invariant | ProvedHere | Shadow depth is an invariant |
| conj:ext-diagonal-vanishing | ProvedHere | Ext diagonal vanishing criterion |
| conj:lagrangian-koszulness | Conditional | Lagrangian criterion (pending perfectness) |
| conj:mc3-arbitrary-type | ProvedHere | MC3 for all simple types |
| conj:FG-shadow | ProvedHere | Francis-Gaitsgory shadow identification |

## Files with Highest Conjecture Density

| File | Count |
|------|-------|
| concordance.tex | 24 |
| arithmetic_shadows.tex | 15 |
| nonlinear_modular_shadows.tex | 15 |
| toroidal_elliptic.tex | 14 |
| koszul_pair_structure.tex | 13 |
| chiral_hochschild_koszul.tex | 13 |
| frontier_modular_holography_platonic.tex | 13 |
| yangians_drinfeld_kohno.tex | 12 |
| ht_physical_origins.tex (Vol II) | 19 |
| celestial_holography_frontier.tex (Vol II) | 12 |
| spectral-braiding-frontier.tex (Vol II) | 12 |
| holomorphic_topological.tex (Vol II) | 11 |
| ht_bulk_boundary_line_frontier.tex (Vol II) | 11 |

## Session Assessment

None of the top 10 open conjectures were advanced in this session. The session was diagnostic
(survey + build + test), not substantive. The three master conjectures (BV/BRST, DK/KL,
infinite-generator) are physics-bridge and extension problems downstream of the proved algebraic
core. The most tractable open conjectures for near-term progress are:

- **conj:type-a-transport-to-transpose** (transport-closure in type A is computable)
- **conj:d-module-purity-koszulness** (converse direction, reduced to PBW = Saito weight)
- **conj:ds-kd-arbitrary-nilpotent** (hook-type corridor proved, extension to more orbits)
