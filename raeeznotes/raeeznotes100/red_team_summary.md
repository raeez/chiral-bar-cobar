# Red-Team Summary of Vol1/Vol2 Claim Audit
## Scope
- Formal tagged claims catalogued: **4866**
- Volume I formal claims: **2841**
- Volume II formal claims: **2025**
- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.

## Status profile
- ProvedHere: **3801**
- Conjectured: **327**
- Heuristic: **35**
- ProvedElsewhere: **513**
- Conditional: **116**
- Open: **74**

## Risk profile
- medium: **1999**
- low: **1913**
- high: **807**
- critical: **147**

## What I would dismiss immediately
- **All heuristic claims** as evidence. They may be useful motivations, but they cannot support downstream theorems.
- **All conjectured claims** as established mathematics. They should be treated only as targets.
- **All open claims** as unresolved.
- **All conditional claims** whenever their hypotheses are not explicitly imported at the point of use.

## Strongest concrete failure modes found
- **47 proved-here claims** cite at least one non-proved / conditional / conjectural / heuristic / unknown-status label in their local block. These are the first places to try dismissal.
- **9 label-status conflicts** exist across files/volumes. This is claim drift: the same label is not stably assigned a single epistemic status.
- There are many duplicated theorem clusters across split core/frontier/stable files. Duplication is not itself falsehood, but it is a major error surface: status drift, proof drift, and unstated hypothesis drift.

## Highest-risk proved-here clusters
- V1 `chapters/examples/free_fields.tex`: **36** high/critical-risk claims
- V1 `chapters/examples/kac_moody.tex`: **27** high/critical-risk claims
- V2 `chapters/connections/ht_physical_origins.tex`: **26** high/critical-risk claims
- V1 `chapters/examples/w_algebras.tex`: **24** high/critical-risk claims
- V1 `chapters/examples/yangians_drinfeld_kohno.tex`: **21** high/critical-risk claims
- V1 `chapters/connections/genus_complete.tex`: **20** high/critical-risk claims
- V2 `chapters/connections/modular_pva_quantization.tex`: **18** high/critical-risk claims
- V2 `chapters/connections/thqg_modular_pva_extensions.tex`: **17** high/critical-risk claims
- V2 `chapters/connections/twisted_holography_quantum_gravity.tex`: **17** high/critical-risk claims
- V2 `chapters/connections/ht_bulk_boundary_line_frontier.tex`: **16** high/critical-risk claims
- V2 `chapters/connections/thqg_3d_gravity_movements_vi_x.tex`: **16** high/critical-risk claims
- V2 `chapters/connections/thqg_symplectic_polarization.tex`: **15** high/critical-risk claims
- V1 `chapters/connections/editorial_constitution.tex`: **14** high/critical-risk claims
- V1 `chapters/connections/arithmetic_shadows.tex`: **13** high/critical-risk claims
- V1 `chapters/connections/thqg_gravitational_complexity.tex`: **13** high/critical-risk claims

## Highest-density frontier clusters
- V2 `chapters/connections/ht_physical_origins.tex`: **38** conjectural / conditional / heuristic / open claims
- V1 `chapters/theory/koszul_pair_structure.tex`: **14** conjectural / conditional / heuristic / open claims
- V1 `chapters/theory/chiral_hochschild_koszul.tex`: **13** conjectural / conditional / heuristic / open claims
- V2 `chapters/examples/w-algebras.tex`: **13** conjectural / conditional / heuristic / open claims
- V2 `chapters/connections/holomorphic_topological.tex`: **12** conjectural / conditional / heuristic / open claims
- V2 `chapters/connections/ht_bulk_boundary_line_frontier.tex`: **12** conjectural / conditional / heuristic / open claims
- V2 `chapters/connections/thqg_symplectic_polarization.tex`: **12** conjectural / conditional / heuristic / open claims
- V1 `chapters/connections/editorial_constitution.tex`: **10** conjectural / conditional / heuristic / open claims
- V1 `chapters/connections/genus_complete.tex`: **10** conjectural / conditional / heuristic / open claims
- V1 `chapters/examples/kac_moody.tex`: **10** conjectural / conditional / heuristic / open claims
- V1 `chapters/examples/yangians_computations.tex`: **10** conjectural / conditional / heuristic / open claims
- V2 `chapters/connections/bar-cobar-review.tex`: **10** conjectural / conditional / heuristic / open claims
- V2 `chapters/connections/celestial_holography.tex`: **10** conjectural / conditional / heuristic / open claims
- V2 `chapters/connections/celestial_holography_frontier.tex`: **10** conjectural / conditional / heuristic / open claims
- V1 `chapters/connections/concordance.tex`: **9** conjectural / conditional / heuristic / open claims

## Highest-density suspicious proved-here dependency clusters
- V1 `chapters/connections/editorial_constitution.tex`: **4** proved-here claims with suspicious dependencies
- V1 `chapters/examples/yangians_drinfeld_kohno.tex`: **4** proved-here claims with suspicious dependencies
- V1 `chapters/theory/higher_genus_modular_koszul.tex`: **4** proved-here claims with suspicious dependencies
- V1 `chapters/connections/feynman_diagrams.tex`: **2** proved-here claims with suspicious dependencies
- V1 `chapters/connections/thqg_symplectic_polarization.tex`: **2** proved-here claims with suspicious dependencies
- V1 `chapters/examples/yangians_computations.tex`: **2** proved-here claims with suspicious dependencies
- V2 `chapters/connections/bar-cobar-review.tex`: **2** proved-here claims with suspicious dependencies
- V2 `chapters/connections/thqg_symplectic_polarization.tex`: **2** proved-here claims with suspicious dependencies
- V1 `chapters/connections/thqg_critical_string_dichotomy.tex`: **1** proved-here claims with suspicious dependencies
- V1 `chapters/connections/ym_boundary_theory.tex`: **1** proved-here claims with suspicious dependencies
- V1 `chapters/connections/ym_instanton_screening.tex`: **1** proved-here claims with suspicious dependencies
- V1 `chapters/examples/w_algebras.tex`: **1** proved-here claims with suspicious dependencies
- V1 `chapters/examples/w_algebras_deep.tex`: **1** proved-here claims with suspicious dependencies
- V1 `chapters/examples/yangians_foundations.tex`: **1** proved-here claims with suspicious dependencies
- V1 `chapters/theory/bar_cobar_adjunction_inversion.tex`: **1** proved-here claims with suspicious dependencies

## Specific red flags worth reading first
- `prop:standard-tower-mc5-reduction` (V1 `chapters/connections/editorial_constitution.tex:533`): proved here, but cites `conj:master-dk-kl:Conjectured`.
- `cor:standard-tower-mc5-closure` (V1 `chapters/connections/editorial_constitution.tex:621`): proved here, but cites `conj:master-dk-kl:Conjectured`.
- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
- `prop:constitution-status-updates` (V1 `chapters/connections/editorial_constitution.tex:2607`): proved here, but cites `prop:mc3-type-b-folding:Conjectured`.
- `prop:disk-local-binary-ternary-reduction` (V1 `chapters/connections/feynman_diagrams.tex:323`): proved here, but cites `conj:disk-local-perturbative-fm:Conjectured`.
- `prop:compactified-ternary-two-channel` (V1 `chapters/connections/feynman_diagrams.tex:389`): proved here, but cites `conj:disk-local-perturbative-fm:Conjectured`.
- `cor:g9-comparison-universal` (V1 `chapters/connections/thqg_critical_string_dichotomy.tex:1936`): proved here, but cites `rem:g9-mc-relation:Unknown`.
- `prop:thqg-III-compatibility` (V1 `chapters/connections/thqg_symplectic_polarization.tex:1148`): proved here, but cites `thm:thqg-III-lagrangian-polarization:Conditional`.
- `thm:thqg-III-landscape-census` (V1 `chapters/connections/thqg_symplectic_polarization.tex:1764`): proved here, but cites `thm:thqg-III-lagrangian-polarization:Conditional`.
- `thm:ym-bar-bridge` (V1 `chapters/connections/ym_boundary_theory.tex:58`): proved here, but cites `thm:conditional-mass-gap-transfer:Conditional,Conjectured`.
- `cor:stable-untwisting-bounded-error` (V1 `chapters/connections/ym_instanton_screening.tex:526`): proved here, but cites `thm:conditional-mass-gap-transfer:Conditional,Conjectured`.
- `thm:w-algebra-koszul-main` (V1 `chapters/examples/w_algebras.tex:250`): proved here, but cites `conj:w-orbit-duality:Conjectured`.

## Status-conflict examples
- `thm:thqg-contact-termination` has statuses **ProvedElsewhere,ProvedHere** across instances: V1:ProvedHere:chapters/connections/thqg_gravitational_complexity.tex:549:Contact termination || V2:ProvedElsewhere:chapters/connections/thqg_gravitational_complexity.tex:551:Contact termination...
- `lem:thqg-VII-genus-shifts` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_modular_bootstrap.tex:203:Genus shifts of the differential components || V2:Unknown:chapters/connections/thqg_line_operators_extensions.tex:2124:Planted-forest differential and genus shifts || V2...
- `cor:thqg-I-genus-g-partition` has statuses **ProvedHere,Unknown** across instances: V1:ProvedHere:chapters/connections/thqg_perturbative_finiteness.tex:369:Genus-$g$ partition function || V2:Unknown:chapters/connections/thqg_perturbative_finiteness.tex:368:Genus-$g$ partition function...
- `prop:thqg-III-kontsevich-pridham` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_symplectic_polarization.tex:857:{Kontsevich--Pridham correspondence; ;
\cite{Pridham17}} || V2:Unknown:chapters/connections/thqg_symplectic_polarization.tex:855:...
- `thm:grand-synthesis-principle` has statuses **Conditional,ProvedHere** across instances: V1:ProvedHere:chapters/connections/ym_boundary_theory.tex:128:Grand synthesis principle || V2:Conditional:chapters/connections/ym_synthesis.tex:36:Grand synthesis principle; \ClaimStatusConditional || V2:Conditional:chapters/connections/ym_...
- `thm:conditional-mass-gap-transfer` has statuses **Conditional,Conjectured** across instances: V1:Conjectured:chapters/connections/ym_instanton_screening.tex:499:Conditional mass-gap transfer via screening domination || V2:Conditional:chapters/connections/ym_synthesis.tex:1616:Conditional mass-gap transfer via screening domination; \...
- `conj:modular` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1278:Associative modular Maurer--Cartan class || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1396: || V2:ProvedHere:chapters/connections/ordered_associativ...
- `conj:DS` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1309:Reduction commutes with associative chiral duality || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1457: || V2:ProvedHere:chapters/connections/ordered_...
- `lem:PVA2_proof` has statuses **ProvedHere,Unknown** across instances: V2:Unknown:chapters/theory/pva-descent.tex:149:Alternative derivation of PVA2 via vertex algebra modes || V2:ProvedHere:chapters/theory/pva-descent-repaired.tex:375:Chain-level exchange homotopies; \ClaimStatusProvedHere...

## Zones that currently survive the red-team pass better than the rest
- Volume II foundations around Swiss-cheese recognition, PVA descent, FM/AOS cancellation, and bar-cobar rectification look substantially healthier than the speculative connection chapters.
- Volume I core theory and the explicitly tagged examples are safer than the high-energy connection/frontier material, but still need local proof verification claim by claim.

## Files produced
- `master_claim_ledger_filtered.csv`: all filtered formal claims with attack swarms and dismissal stances.
- `suspicious_proved_claim_dependencies.csv`: proved-here claims that locally depend on non-proved or unstable references.
- `label_status_conflicts.csv`: same label with multiple statuses across files/volumes.
- `informal_claim_harvest.csv`: harvested sentence-level explicit informal/meta claims.
