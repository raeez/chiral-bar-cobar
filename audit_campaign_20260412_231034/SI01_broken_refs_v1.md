# SI01_broken_refs_v1 (729s, gpt-5.4)

First-100 scan: `grep -rn '\\ref{' chapters/ | head -100` produced 101 `\ref` occurrences (52 unique targets); all 52 have matching live `\label`s. All surviving failures below come from the current `main.log` undefined-reference surface (163 warning instances, 76 unique unresolved targets).

- [HIGH] chapters/theory/introduction.tex:2016 — `thm:ds-hpl-transfer` has no matching live `\label`.
- [HIGH] chapters/frame/heisenberg_frame.tex:3467; chapters/frame/heisenberg_frame.tex:3537 — `sec:bar-complex-introduction` has no matching live `\label`.
- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:1980 — `sec:complementarity` has no matching live `\label`.
- [HIGH] chapters/theory/higher_genus_foundations.tex:4754 — `rem:feynman_genus_g` has no matching live `\label`.
- [HIGH] chapters/theory/e1_modular_koszul.tex:694; chapters/theory/higher_genus_modular_koszul.tex:20508 — `sec:landscape-census` has no matching live `\label`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:26890; chapters/connections/arithmetic_shadows.tex:2405 — `def:glcm-classification` has no matching live `\label`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:31912; chapters/theory/higher_genus_modular_koszul.tex:31987; chapters/theory/higher_genus_modular_koszul.tex:32432 — `prop:ell-degree0` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8413`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32152 — `prop:ell-degree2` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8677`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32153 — `thm:ell-ordered-ch` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8876`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32173 — `sec:elliptic-ordered` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8294`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32323; chapters/theory/higher_genus_modular_koszul.tex:32561 — `eq:kzb-ell` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8366`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32367 — `eq:kzb-tau` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8597`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32471; chapters/theory/higher_genus_modular_koszul.tex:32496 — `eq:bar-degree1-yangian` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8486`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32857 — `subsec:ell-degree2` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8528`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32866 — `comp:sl2-kappa` has no matching live `\label`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32890 — `eq:ell-braid` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8763`.
- [HIGH] appendices/ordered_associative_chiral_kd.tex:5170; chapters/theory/ordered_associative_chiral_kd.tex:5481 — `thm:affine-half-space-bv` has no matching live `\label`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6047; chapters/theory/ordered_associative_chiral_kd.tex:6166; chapters/theory/ordered_associative_chiral_kd.tex:8107; chapters/theory/ordered_associative_chiral_kd.tex:8132; chapters/theory/ordered_associative_chiral_kd.tex:8168 — `ex:yangian` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:608`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6048; chapters/theory/ordered_associative_chiral_kd.tex:6146; chapters/theory/ordered_associative_chiral_kd.tex:6159; chapters/connections/concordance.tex:7131; chapters/connections/concordance.tex:9746 — `conj:yangian-ordered-center` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1158`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6167; chapters/theory/ordered_associative_chiral_kd.tex:8173 — `eq:yangian-ker-av2` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:917`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8106 — `eq:yangian-qybe` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:657`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8177 — `eq:sl2-kappa` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7558`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8198 — `eq:ek-s-locality` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3458`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8384 — `eq:yangian-drinfeld-coprod` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:754`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8385 — `ex:yangian-coproduct` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3205`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8577 — `def:chiral-coproduct` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2492`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8731 — `def:e1-chiral-rmatrix` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2402`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8732 — `eq:equiv-triangle` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2595`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8738 — `eq:mk-from-ope` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2626`.
- [HIGH] chapters/theory/en_koszul_duality.tex:3584; chapters/theory/en_koszul_duality.tex:3789; chapters/theory/en_koszul_duality.tex:3799; chapters/theory/en_koszul_duality.tex:4598 — `prop:e3-structure` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:5263`.
- [HIGH] chapters/theory/en_koszul_duality.tex:3801 — `ex:km` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7541`.
- [HIGH] chapters/theory/en_koszul_duality.tex:4067 — `eq:kz-sl2-degree2` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7574`.
- [HIGH] chapters/theory/en_koszul_duality.tex:4201; chapters/theory/en_koszul_duality.tex:4266 — `ex:ek-qvoa` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3238`.
- [HIGH] chapters/theory/en_koszul_duality.tex:4245 — `eq:ek-vertex-rmatrix` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3405`.
- [HIGH] chapters/theory/en_koszul_duality.tex:4537; chapters/theory/en_koszul_duality.tex:4821; chapters/theory/en_koszul_duality.tex:5258 — `warn:e1-vs-e2-source` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1632`.
- [HIGH] chapters/connections/thqg_open_closed_realization.tex:662; chapters/connections/thqg_open_closed_realization.tex:707 — `def:oc-factorization-category` has no matching live `\label`.
- [HIGH] chapters/examples/y_algebras.tex:340 — `prop:heisenberg-kappa` has no matching live `\label`.
- [HIGH] chapters/examples/yangians_computations.tex:1150; chapters/examples/yangians_foundations.tex:1228 — `thm:rtt-all-types` has no matching live `\label`.
- [HIGH] chapters/connections/editorial_constitution.tex:1059; chapters/examples/yangians_computations.tex:2895; chapters/examples/yangians_computations.tex:3031; chapters/examples/yangians_computations.tex:3602; chapters/examples/yangians_computations.tex:3708; chapters/examples/yangians_drinfeld_kohno.tex:1010; chapters/examples/yangians_drinfeld_kohno.tex:1731; chapters/examples/yangians_drinfeld_kohno.tex:1759 — `thm:baxter-exact-triangles` has no matching live `\label`.
- [HIGH] chapters/connections/concordance.tex:1859; chapters/connections/editorial_constitution.tex:167; chapters/connections/editorial_constitution.tex:1061; chapters/examples/yangians_computations.tex:3550; chapters/examples/yangians_computations.tex:3592; chapters/examples/yangians_computations.tex:3720; chapters/examples/yangians_drinfeld_kohno.tex:1013; chapters/examples/yangians_drinfeld_kohno.tex:1717; chapters/examples/yangians_drinfeld_kohno.tex:1783; chapters/examples/yangians_drinfeld_kohno.tex:2186; chapters/examples/yangians_drinfeld_kohno.tex:2188 — `thm:pro-weyl-recovery` has no matching live `\label`.
- [MEDIUM] chapters/frame/preface.tex:3664 — `conv:three-hochschild` is undefined in `main.log`; live `\label` at chapters/connections/concordance.tex:100, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/introduction.tex:860; chapters/theory/introduction.tex:1119; chapters/theory/introduction.tex:2238; chapters/theory/introduction.tex:2439; chapters/examples/kac_moody.tex:4399; chapters/examples/kac_moody.tex:4439 — `ch:derived-langlands` is undefined in `main.log`; live `\label` at chapters/theory/derived_langlands.tex:6, but it never reaches the current aux surface.
- [MEDIUM] main.tex:1486; chapters/theory/introduction.tex:933; chapters/theory/introduction.tex:974; chapters/theory/introduction.tex:1684; chapters/theory/introduction.tex:2242; chapters/theory/introduction.tex:2450; chapters/frame/heisenberg_frame.tex:4802; chapters/connections/thqg_introduction_supplement_body.tex:1619; chapters/connections/thqg_introduction_supplement_body.tex:1752; chapters/connections/thqg_preface_supplement.tex:2017; chapters/connections/thqg_preface_supplement.tex:2054; chapters/examples/landscape_census.tex:4048 — `part:seven-faces` is undefined in `main.log`; live `\label` at main.tex:1450, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/cobar_construction.tex:2042; chapters/theory/introduction.tex:934; chapters/theory/introduction.tex:975; chapters/theory/introduction.tex:2244; chapters/theory/introduction.tex:2453 — `ch:holographic-datum-master` is undefined in `main.log`; live `\label` at chapters/connections/holographic_datum_master.tex:2, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/introduction.tex:1179; chapters/connections/subregular_hook_frontier.tex:966 — `comp:bp-kappa-three-paths` is undefined in `main.log`; live `\label` at chapters/connections/subregular_hook_frontier.tex:905, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/introduction.tex:1180; chapters/connections/subregular_hook_frontier.tex:1674 — `prop:nilpotent-transport-typeA` is undefined in `main.log`; live `\label` at chapters/connections/subregular_hook_frontier.tex:1519, but it never reaches the current aux surface.
- [MEDIUM] main.tex:1488; chapters/theory/introduction.tex:1941; chapters/theory/introduction.tex:2248; chapters/theory/introduction.tex:2468; chapters/connections/concordance.tex:3799 — `part:v1-frontier` is undefined in `main.log`; live `\label` at main.tex:1483, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/introduction.tex:2246; chapters/theory/introduction.tex:2462; chapters/connections/concordance.tex:6510 — `ch:genus1-seven-faces` is undefined in `main.log`; live `\label` at chapters/connections/genus1_seven_faces.tex:2, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/three_invariants.tex:234; chapters/connections/genus1_seven_faces.tex:1040; chapters/connections/holomorphic_topological.tex:43 — `ch:landscape-census` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:2, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/chiral_koszul_pairs.tex:1424; chapters/connections/arithmetic_shadows.tex:105; chapters/connections/arithmetic_shadows.tex:11156 — `thm:langlands-bar-bridge` is undefined in `main.log`; live `\label` at chapters/theory/derived_langlands.tex:95, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/higher_genus_foundations.tex:194; chapters/theory/higher_genus_foundations.tex:633; chapters/theory/higher_genus_foundations.tex:1074; chapters/theory/higher_genus_foundations.tex:5405; chapters/theory/higher_genus_foundations.tex:6388; chapters/theory/higher_genus_foundations.tex:6789; chapters/theory/higher_genus_foundations.tex:6827; chapters/theory/higher_genus_foundations.tex:6897; chapters/theory/higher_genus_modular_koszul.tex:2730; chapters/theory/higher_genus_modular_koszul.tex:2806; chapters/theory/higher_genus_modular_koszul.tex:2816; chapters/theory/higher_genus_modular_koszul.tex:4407; chapters/theory/higher_genus_modular_koszul.tex:4457; chapters/theory/higher_genus_modular_koszul.tex:9507; chapters/theory/higher_genus_modular_koszul.tex:13934; chapters/frame/heisenberg_frame.tex:1616; chapters/frame/heisenberg_frame.tex:1718; chapters/frame/heisenberg_frame.tex:4642; chapters/connections/concordance.tex:4712; chapters/connections/concordance.tex:6227; chapters/connections/bv_brst.tex:1502; chapters/connections/thqg_fredholm_partition_functions.tex:1449; chapters/connections/editorial_constitution.tex:2579; chapters/connections/editorial_constitution.tex:2668; chapters/examples/genus_expansions.tex:169; chapters/examples/genus_expansions.tex:1904; chapters/examples/heisenberg_eisenstein.tex:1738 — `thm:family-index` is undefined in `main.log`; live `\label` at chapters/connections/outlook.tex:660; chapters/connections/concordance.tex:5928, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:32123 — `prop:bar-verlinde-asymptotics` is undefined in `main.log`; live `\label` at chapters/examples/genus_expansions.tex:1987, but it never reaches the current aux surface.
- [MEDIUM] appendices/combinatorial_frontier.tex:226; appendices/combinatorial_frontier.tex:238; chapters/theory/derived_langlands.tex:1056; chapters/theory/higher_genus_modular_koszul.tex:33808; chapters/examples/landscape_census.tex:1843; chapters/examples/landscape_census.tex:1851; chapters/examples/landscape_census.tex:2016; chapters/examples/landscape_census.tex:2084; chapters/examples/landscape_census.tex:2101; chapters/examples/landscape_census.tex:2138; chapters/examples/landscape_census.tex:2163; chapters/examples/landscape_census.tex:2178; chapters/examples/landscape_census.tex:2483; chapters/examples/landscape_census.tex:2631; chapters/examples/landscape_census.tex:2819; chapters/examples/landscape_census.tex:2876; chapters/examples/kac_moody.tex:1060; chapters/examples/kac_moody.tex:1080 — `rem:garland-lepowsky-sl2` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:2035, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:33872 — `rem:rank-plus-one` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:2445, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/computational_methods.tex:1025; chapters/examples/landscape_census.tex:1627 — `tab:shadow-l-functions` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:1633, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/ordered_associative_chiral_kd.tex:9826; chapters/theory/ordered_associative_chiral_kd.tex:9848; chapters/theory/ordered_associative_chiral_kd.tex:9904; chapters/theory/ordered_associative_chiral_kd.tex:10013; chapters/theory/ordered_associative_chiral_kd.tex:10040; chapters/theory/coderived_models.tex:298; chapters/theory/coderived_models.tex:900; chapters/connections/concordance.tex:4940; chapters/connections/editorial_constitution.tex:1410 — `thm:off-koszul-ran-inversion` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:825, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/ordered_associative_chiral_kd.tex:10047; chapters/theory/coderived_models.tex:156; chapters/theory/coderived_models.tex:563; chapters/theory/coderived_models.tex:935 — `thm:conilpotent-reduction` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:125, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/chiral_center_theorem.tex:2516 — `rem:cdr-k3` is undefined in `main.log`; live `\label` at chapters/examples/toroidal_elliptic.tex:2080, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/chiral_center_theorem.tex:2551; chapters/theory/chiral_center_theorem.tex:2572 — `def:complementarity-asymmetry` is undefined in `main.log`; live `\label` at chapters/connections/thqg_critical_string_dichotomy.tex:964, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/thqg_fredholm_partition_functions.tex:777; chapters/connections/thqg_fredholm_partition_functions.tex:1152; chapters/connections/thqg_fredholm_partition_functions.tex:1714; chapters/examples/heisenberg_eisenstein.tex:2190 — `lem:thqg-X-composition-decay` is undefined in `main.log`; live `\label` at chapters/connections/thqg_fredholm_partition_functions.tex:447, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/thqg_fredholm_partition_functions.tex:864; chapters/connections/thqg_fredholm_partition_functions.tex:904; chapters/connections/thqg_fredholm_partition_functions.tex:1195; chapters/examples/heisenberg_eisenstein.tex:2414 — `eq:thqg-X-polyakov` is undefined in `main.log`; live `\label` at chapters/connections/thqg_fredholm_partition_functions.tex:822, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/heisenberg_eisenstein.tex:2420 — `rem:thqg-X-pants-independence` is undefined in `main.log`; live `\label` at chapters/connections/thqg_fredholm_partition_functions.tex:408, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/kac_moody.tex:764 — `tab:rmatrix-census` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:397, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/derived_langlands.tex:42; chapters/theory/derived_langlands.tex:720; chapters/theory/derived_langlands.tex:861; chapters/theory/derived_langlands.tex:890; chapters/theory/derived_langlands.tex:918; chapters/theory/derived_langlands.tex:1344; chapters/theory/derived_langlands.tex:1365; chapters/theory/derived_langlands.tex:1560; chapters/examples/kac_moody.tex:4372 — `thm:oper-bar-dl` is undefined in `main.log`; live `\label` at chapters/theory/derived_langlands.tex:648, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/landscape_census.tex:286; chapters/examples/bar_complex_tables.tex:2257; chapters/examples/bar_complex_tables.tex:2578; chapters/examples/kac_moody.tex:4507; chapters/examples/kac_moody.tex:5588 — `sec:B2-details` is undefined in `main.log`; live `\label` at chapters/examples/bar_complex_tables.tex:1207, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/landscape_census.tex:286; chapters/examples/kac_moody.tex:4507; chapters/examples/kac_moody.tex:5588 — `sec:G2-details` is undefined in `main.log`; live `\label` at chapters/examples/bar_complex_tables.tex:2253, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/y_algebras.tex:630 — `subsec:concordance-e1-primacy` is undefined in `main.log`; live `\label` at chapters/connections/concordance.tex:3752, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/w3_holographic_datum.tex:215 — `cor:anomaly-ratio-ds` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:1238, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/landscape_census.tex:506; chapters/examples/w3_holographic_datum.tex:387 — `rem:ww-even-poles-census` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:568, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/thqg_gravitational_yangian.tex:1033; chapters/connections/thqg_gravitational_yangian.tex:1474; chapters/connections/thqg_gravitational_yangian.tex:2005; chapters/connections/thqg_gravitational_yangian.tex:2242; chapters/examples/yangians_drinfeld_kohno.tex:8056; chapters/examples/yangians_drinfeld_kohno.tex:8099 — `thm:thqg-V-collision-twisting` is undefined in `main.log`; live `\label` at chapters/connections/thqg_gravitational_yangian.tex:579, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/bv_brst.tex:1546 — `cor:thqg-I-heisenberg-selberg` is undefined in `main.log`; live `\label` at chapters/connections/thqg_perturbative_finiteness.tex:1997, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/concordance.tex:4929; chapters/connections/bv_brst.tex:1878; chapters/connections/bv_brst.tex:1964; chapters/connections/bv_brst.tex:2030 — `def:coacyclic-fact` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:518, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/coderived_models.tex:239; chapters/theory/coderived_models.tex:267; chapters/theory/coderived_models.tex:674; chapters/connections/bv_brst.tex:1878; chapters/connections/bv_brst.tex:1907; chapters/connections/bv_brst.tex:1931; chapters/connections/bv_brst.tex:1965 — `def:curved-weak-equiv` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:214, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/coderived_models.tex:292; chapters/connections/concordance.tex:4935; chapters/connections/bv_brst.tex:1936; chapters/connections/editorial_constitution.tex:1404 — `prop:provisional-embedding` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:654, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/bv_brst.tex:2030 — `def:coderived-fact` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:546, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/arithmetic_shadows.tex:2883; chapters/connections/concordance.tex:2251; chapters/connections/concordance.tex:6529; chapters/connections/frontier_modular_holography_platonic.tex:1656 — `thm:yangian-shadow-theorem` is undefined in `main.log`; live `\label` at chapters/connections/frontier_modular_holography_platonic.tex:1400, but it never reaches the current aux surface.

## Summary
Instances checked: 264 | Violations found: 76 | Verdict: FAIL


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d83cb-0f56-7fd3-a1e5-567b8d0535d0
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


Find broken \ref in Vol I. Run: grep -rn '\\ref{' chapters/ | head -100. For each ref, check the corresponding \label exists. Also check compile log for undefined references.

Report every finding with file:line.
mcp startup: no servers
codex
Using `deep-beilinson-audit` and `build-surface`: I’m treating the ref graph as hostile until each target label is verified locally. First step is to read the relevant skill instructions, then enumerate the first 100 `\ref{...}` occurrences in `chapters/`, resolve each label against the live source, and cross-check the build logs for undefined references.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
 succeeded in 51ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

codex
I’ve loaded the audit and build workflows. Next I’m reading the required repo-level constitutional files just enough to anchor the audit surface, then I’ll enumerate the reference targets and the current log warnings.
exec
/bin/zsh -lc "sed -n '1,160p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

exec
/bin/zsh -lc "sed -n '1,160p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,160p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,160p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2809 |
| Total tagged claims | 3615 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2809 |
 succeeded in 51ms:
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
 succeeded in 51ms:
\chapter{Concordance with primary literature}
\label{chap:concordance}

\index{concordance|textbf}

This chapter is the constitution of the monograph. When chapters
disagree, this chapter governs. It records the five main theorems
with their precise status and locates every result against the
prior literature: what is proved, what is conditional, what
remains conjectural.

The governing principle is falsification: every claim in these three
volumes is presumed false until it appears below with an explicit
status tag and a proof reference or independent verification trail.
A theorem that contradicts the concordance is not a theorem; it is an
error in the chapter that states it. Omission from this chapter is
itself a verdict: what is not recorded here has not survived scrutiny.
The concordance does not summarize the monograph; the monograph
approximates the concordance.


thinking
**Compiling log detection**

I need to compile log detection, focusing on "undefined references" in logs. I might use an exploration agent for a quicker search, but using a manual shell could work too. I wonder if I need to provide a PE, but that seems unnecessary since it's just for pre-edit. I'll run the grep command to locate logs in parallel and ensure commentary updates are frequent. Let's get started!
codex
I’ve finished the required repository reads. Now I’m fixing the exact audit surface: the first 100 `\ref{...}` occurrences under `chapters/`, plus whatever the current LaTeX logs say about undefined references.
exec
/bin/zsh -lc "grep -rn '\\\\ref{' chapters/ | head -100" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files -g '*.log' -g '*.blg' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"undefined references|Reference .* undefined|There were undefined references|LaTeX Warning: Reference .* undefined\" -S . --glob '*.log' --glob '*.blg'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
chapters/theory/higher_genus_complementarity.tex:70: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
chapters/theory/higher_genus_complementarity.tex:76: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
chapters/theory/higher_genus_complementarity.tex:88: \textup{(}Appendix~\textup{\ref{app:nonlinear-modular-shadows})}.
chapters/theory/higher_genus_complementarity.tex:92:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
chapters/theory/higher_genus_complementarity.tex:95:(Proposition~\ref{prop:standard-examples-modular-koszul}).
chapters/theory/higher_genus_complementarity.tex:116:base change (Lemma~\ref{lem:perfectness-criterion}).
chapters/theory/higher_genus_complementarity.tex:156:(Convention~\ref{conv:heisenberg-kappa-notation}: level $=$ modular
chapters/theory/higher_genus_complementarity.tex:197:(Theorem~\ref{thm:verdier-bar-cobar}).
chapters/theory/higher_genus_complementarity.tex:214:\begin{remark}[H/M/S layers; Convention~\ref{conv:hms-levels}]
chapters/theory/higher_genus_complementarity.tex:220:(Lemma~\ref{lem:involution-splitting}) makes the passage automatic
chapters/theory/higher_genus_complementarity.tex:275:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
chapters/theory/higher_genus_complementarity.tex:285:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_complementarity.tex:295: Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_complementarity.tex:357:\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
chapters/theory/higher_genus_complementarity.tex:361:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
chapters/theory/higher_genus_complementarity.tex:365:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
chapters/theory/higher_genus_complementarity.tex:419:(Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/theory/higher_genus_complementarity.tex:427:(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
 succeeded in 50ms:
./main.log
 succeeded in 52ms:
./main.log:2205:LaTeX Warning: Reference `conv:three-hochschild' on page 95 undefined on input 
./main.log:2315:LaTeX Warning: Reference `ch:derived-langlands' on page 118 undefined on input 
./main.log:2364:LaTeX Warning: Reference `part:seven-faces' on page 119 undefined on input line
./main.log:2368:LaTeX Warning: Reference `ch:holographic-datum-master' on page 119 undefined on
./main.log:2372:LaTeX Warning: Reference `part:seven-faces' on page 119 undefined on input line
./main.log:2376:LaTeX Warning: Reference `ch:holographic-datum-master' on page 119 undefined on
./main.log:2383:LaTeX Warning: Reference `ch:derived-langlands' on page 120 undefined on input 
./main.log:2390:LaTeX Warning: Reference `comp:bp-kappa-three-paths' on page 121 undefined on i
./main.log:2394:LaTeX Warning: Reference `prop:nilpotent-transport-typeA' on page 121 undefined
./main.log:2424:LaTeX Warning: Reference `part:seven-faces' on page 126 undefined on input line
./main.log:2437:LaTeX Warning: Reference `part:v1-frontier' on page 128 undefined on input line
./main.log:2451:LaTeX Warning: Reference `thm:ds-hpl-transfer' on page 129 undefined on input l
./main.log:2497:LaTeX Warning: Reference `ch:derived-langlands' on page 132 undefined on input 
./main.log:2501:LaTeX Warning: Reference `part:seven-faces' on page 132 undefined on input line
./main.log:2505:LaTeX Warning: Reference `ch:holographic-datum-master' on page 132 undefined on
./main.log:2509:LaTeX Warning: Reference `ch:genus1-seven-faces' on page 132 undefined on input
./main.log:2513:LaTeX Warning: Reference `part:v1-frontier' on page 132 undefined on input line
./main.log:2535:LaTeX Warning: Reference `ch:derived-langlands' on page 136 undefined on input 
./main.log:2539:LaTeX Warning: Reference `part:seven-faces' on page 136 undefined on input line
./main.log:2543:LaTeX Warning: Reference `ch:holographic-datum-master' on page 136 undefined on





thinking
**Checking label existence**

I need to verify that the corresponding labels exist, and they probably do. Automating this might be helpful given that the first 100 results from grep are from higher_genus_complementarity.tex. I could write a shell script to extract unique labels and search for `\label{...}`. I should report any missing ones. Although the first 100 may resolve, the compile log shows some undefined references later, so I need to map those to source files and line numbers. I'll also check where `\ref{label}` is used in the log.
thinking
**Finding broken references**

Okay, I need to check for broken `\ref` commands in Volume I, as the user asked. I should report the source occurrence with file and line number. The compile log might have references outside the first 100, so I need to include all undefined references with their source. This could be around 180 lines! I might need to deduplicate repeated occurrences too. The contract says to report every finding, but I could focus on just the broken references in the chapters for Volume I, since the compile warnings are already quite a few.
thinking
**Evaluating label status**

I need to check if a corresponding `\label{label}` exists in the repository or within the chapters. I want to distinguish between a broken label due to it being absent versus one that might be unstable. The log indicates persistent undefined status on the current build. I should verify the label's absence using `rg` for `\label{label}`. It's possible some labels are in appendices or the preamble, not in the chapters. If the label is truly absent, I'll report it as missing. If it exists but has a compile warning, that's a different kind of bug.
thinking
**Investigating unresolved references**

I could report the description as "reference unresolved in build; no matching \label found anywhere," or "reference unresolved despite matching label in file X, suggesting an excluded file or stale AUX." I need to check this. Maybe I'll use a script to extract all labels from the log and search the repository for label definitions and reference occurrences, focusing on Volume I. Python might be effective because of the many labels, but shell and Perl could work too. I should ensure I'm not reading or writing files unnecessarily. I'll run a small Python one-liner for efficiency and might use `rg` for speed as well.
thinking
**Structuring the label search**

I’m considering a Python script that uses commands like `rg -n '\\label{...}'` to find labels, but since the developer prefers `rg`, I might lean toward that. Since we need actual commands for reporting, a manual script works fine for now. I’ll check if the first 100 references include any missing labels using either Python or `awk`. I should process any undefined references from `main.log` too. I need to focus on the exact scope of the first 100 `\ref` occurrences under chapters and determine if there are multiple labels per line to check effectively.
codex
The first 100 `\ref` hits are concentrated in [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:39). I’m now resolving them mechanically against live `\label{...}` definitions so I can separate actual missing targets from refs that only fail on the build surface.

thinking
**Considering planning options**

I’m thinking that I might need a longer plan for this task, but it’s not necessarily required. If the work is substantial, then a longer plan could be helpful. I could do a commentary with a brief plan after I establish sufficient context. Maybe I should use the update_plan tool since the developer allows for it. It could be beneficial even though the user won’t see it. Let’s consider issuing the update_plan for my own benefit.
Plan update
Audit surface fixed to the first 100 `\ref` occurrences under `chapters/` plus all undefined-reference warnings in `main.log`. No file edits.
  → Parse the first 100 `\ref` occurrences and verify whether each target label exists anywhere in Vol I.
  • Extract undefined labels from `main.log`, map each to source `\ref` locations, and check whether a matching `\label` exists.
  • Re-verify surviving discrepancies and produce a severity-ordered findings report with exact file:line references.

thinking
**Considering output parsing**

I could use regular expressions, but it might be simpler to parse the output I have. I'll run a script using `subprocess.check_output` to execute the command in the shell. This command will search through the chapters to find occurrences of "\\ref{", and I can limit it to the first 100 lines. After that, I’ll use regex to parse each line and produce a list of occurrences with their labels. Let's get started on that!
exec
/bin/zsh -lc "python3 - <<'PY'
import re, subprocess, pathlib, json
root = pathlib.Path('/Users/raeez/chiral-bar-cobar')
cmd = r\"grep -rn '\\\\ref{' chapters/ | head -100\"
out = subprocess.check_output(cmd, shell=True, cwd=root, text=True)
entries = []
for line in out.splitlines():
    m = re.match(r'(["'^:]+):('"\\d+):(.*)', line)
    if not m:
        continue
    path, lineno, text = m.groups()
    labels = re.findall(r'\\\\ref\\{(["'^}]+)'"\\}', text)
    for label in labels:
        entries.append((path, int(lineno), label, text.strip()))
# collect labels from all tex files in repo
label_map = {}
for tex in root.rglob('*.tex'):
    try:
        content = tex.read_text()
    except Exception:
        continue
    for i, line in enumerate(content.splitlines(), start=1):
        for label in re.findall(r'\\\\label\\{(["'^}]+)'"\\}', line):
            label_map.setdefault(label, []).append((str(tex.relative_to(root)), i))
missing = [e for e in entries if e[2] not in label_map]
print(json.dumps({
    'total_ref_occurrences': len(entries),
    'unique_labels': len({e[2] for e in entries}),
    'missing_count': len(missing),
    'missing': missing,
}, indent=2))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 15.75s:
{
  "total_ref_occurrences": 101,
  "unique_labels": 52,
  "missing_count": 0,
  "missing": []
}






thinking
**Analyzing reference issues**

I see that the structured output suggests reporting every finding, which could include unresolved references. Since the task specifies "broken \ref," I should likely focus on those. The compile log might include undefined references that aren't clear in warnings. I wonder if we should also check for unresolved references in chapters by looking for `\ref{label}`. However, if a label is only used with `\eqref`, it may not be relevant. The user mentioned checking the compile log for all undefined references, so I’ll need to report the broken references comprehensively.
thinking
**Searching for unresolved references**

I think I need to filter for occurrences of `\ref{label}` specifically because that’s what the command search is targeting. I want to check the compile log for undefined labels and look for actual `\ref{label}` occurrences in chapters. Some labels might only be referenced with `\Cref` or `\eqref`. I’ll need a script to scan through the repository and inspect all `.tex` files, including chapters and appendices, although the user specified Volume I. I'll consider the entire repo since the main log includes all parts.
thinking
**Evaluating unresolved labels**

I think it’s a good idea to use a Python script to extract unresolved labels from main.log and check for occurrences of `\ref`, `\eqref`, `\autoref`, and similar commands in all `.tex` files under the repo. The user mentioned broken references, and the compile log shows undefined references, so I should definitely report any unresolved labels even if they're in `\eqref` or `\autoref`. I'll categorize their severity—perhaps anything causing an active undefined cross-reference should be considered high.
thinking
**Determining severity of unresolved refs**

I’m considering the severity levels for unresolved references. Maybe I’d assign MEDIUM if a matching label exists, but the build shows unresolved issues due to inactive or excluded files. CRITICAL might be reserved for cases where the first 100 references are missing a label, but that seems iffy. I think undefined references with no matching labels should be HIGH, while those with existing but inactive labels could be MEDIUM. I need to create a Python script to extract and count these labels.
thinking
**Considering report findings**

I’m exploring how to report source occurrences that match undefined warnings. It seems like the main.log might have many repeating warnings, so grouping duplicates could help. The user wants every finding with file:line, which means listing all broken occurrences, but that could result in over 162 warnings. I must balance clarity and conciseness to avoid going over 70 lines while still complying with the user’s request. Grouping by label could be a solution, but I need to keep it clear.
thinking
**Exploring reporting options**

I still need to report all file:lines while keeping things organized. A flat list could work, with each unresolved label having semicolon-separated locations. I think severity ordering is important, and if there are around 70 unique missing labels, I might still end up with 70 lines. That feels manageable to me. However, if there are multiple source occurrences per label, grouping them could help streamline the report even further.
codex
The first-100 scan came back clean: 101 `\ref` occurrences there, 52 unique targets, and every target has a matching `\label` somewhere in the Vol I tree. The remaining work is the real failure surface: labels that `main.log` still marks undefined.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
root = pathlib.Path('/Users/raeez/chiral-bar-cobar')
log = (root / 'main.log').read_text(errors='ignore')
undefs = re.findall(r\"LaTeX Warning: Reference "'`([''^'"']+)' .* undefined\", log)
# preserve order unique
seen = set(); labels=[]
for lab in undefs:
    if lab not in seen:
        seen.add(lab); labels.append(lab)
# collect label definitions and ref-like usages
tex_files = list(root.rglob('*.tex'))
label_defs = {}
ref_uses = {lab: [] for lab in labels}
for tex in tex_files:
    rel = str(tex.relative_to(root))
    try:
        lines = tex.read_text(errors='ignore').splitlines()
    except Exception:
        continue
    for i, line in enumerate(lines, start=1):
        for lab in re.findall(r'\\\\label\\{(["'^}]+)'"\\}', line):
            label_defs.setdefault(lab, []).append((rel, i))
        for lab in labels:
            if lab in line:
                # capture ref-like commands using this label on the line
                if re.search(r'\\\\[A-Za-z]*ref\\{' + re.escape(lab) + r'\\}', line):
                    ref_uses[lab].append((rel, i, line.strip()))
# summarize
summary = []
for lab in labels:
    summary.append({
        'label': lab,
        'warnings': undefs.count(lab),
        'defs': label_defs.get(lab, []),
        'uses': ref_uses.get(lab, []),
    })
print(json.dumps({
    'unique_undefined_labels': len(labels),
    'total_warnings': len(undefs),
    'labels': summary,
}, indent=2))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
root = pathlib.Path('/Users/raeez/chiral-bar-cobar')
log = (root / 'main.log').read_text(errors='ignore')
undefs = re.findall(r\"LaTeX Warning: Reference "'`([''^'"']+)' .* undefined\", log)
labels = []
seen = set()
for lab in undefs:
    if lab not in seen:
        seen.add(lab)
        labels.append(lab)
label_set = set(labels)
label_defs = {}
ref_uses = {lab: [] for lab in labels}
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\([A-Za-z]*ref)\\{(["'^}]+)'"\\}')
for tex in root.rglob('*.tex'):
    rel = str(tex.relative_to(root))
    try:
        lines = tex.read_text(errors='ignore').splitlines()
    except Exception:
        continue
    for i, line in enumerate(lines, start=1):
        for lab in label_re.findall(line):
            label_defs.setdefault(lab, []).append((rel, i))
        for cmd, lab in ref_re.findall(line):
            if lab in label_set:
                ref_uses[lab].append((rel, i, cmd, line.strip()))
summary = []
for lab in labels:
    summary.append({
        'label': lab,
        'warnings': undefs.count(lab),
        'defs': label_defs.get(lab, []),
        'uses': ref_uses.get(lab, []),
    })
print(json.dumps({
    'unique_undefined_labels': len(labels),
    'total_warnings': len(undefs),
    'labels': summary,
}, indent=2))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 9.94s:
{
  "unique_undefined_labels": 77,
  "total_warnings": 165,
  "labels": [
    {
      "label": "conv:three-hochschild",
      "warnings": 1,
      "defs": [
        [
          "chapters/connections/concordance.tex",
          100
        ]
      ],
      "uses": [
        [
          "chapters/frame/preface.tex",
          3664,
          "ref",
          "Convention~\\ref{conv:three-hochschild})."
        ]
codex
I’m validating the log failures by scanning the entire TeX tree once for both `\label{...}` definitions and ref-like uses. That separates three cases cleanly: no label anywhere, label exists but the built manuscript never sees it, and false positives that disappear on reread.

thinking
**Generating reports**

I see that there are no modifications needed to the repo root, but the /tmp directory is fine. I could write a report there, but maybe it’s simpler to produce counts to stdout so we can inspect specific sets. A final report is needed, so I’ll generate a concise TSV of labels with definition counts using locations under the live tree. I can either write to /tmp or print directly, and I’m leaning towards creating /tmp/undefined_refs_live.json or .tsv.
codex
The first log pass was noisy because the repo contains nested `.claude` worktrees with their own TeX trees. I’m re-running the check against the live manuscript surface only, excluding those shadow copies, so the remaining findings correspond to the actual Vol I build.
 succeeded in 1m 19s:
{
  "unique_undefined_labels": 77,
  "total_warnings": 165,
  "labels": [
    {
      "label": "conv:three-hochschild",
      "warnings": 1,
      "defs": [
        [
          "chapters/connections/concordance.tex",
          100
        ]
      ],
      "uses": [
        [
          "chapters/frame/preface.tex",
          3664,
          "Convention~\\ref{conv:three-hochschild})."
        ]
      ]
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
root = pathlib.Path('/Users/raeez/chiral-bar-cobar')
log = (root / 'main.log').read_text(errors='ignore')
undefs = re.findall(r\"LaTeX Warning: Reference "'`([''^'"']+)' .* undefined\", log)
labels = []
seen = set()
for lab in undefs:
    if lab not in seen:
        seen.add(lab)
        labels.append(lab)
label_set = set(labels)
label_defs = {}
ref_uses = {lab: [] for lab in labels}
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\([A-Za-z]*ref)\\{(["'^}]+)'"\\}')
for tex in root.rglob('*.tex'):
    rel = tex.relative_to(root)
    rels = str(rel)
    if rels.startswith('.claude/') or rels.startswith('standalone/') or rels.startswith('archive/'):
        continue
    try:
        lines = tex.read_text(errors='ignore').splitlines()
    except Exception:
        continue
    for i, line in enumerate(lines, start=1):
        for lab in label_re.findall(line):
            label_defs.setdefault(lab, []).append((rels, i))
        for cmd, lab in ref_re.findall(line):
            if lab in label_set:
                ref_uses[lab].append((rels, i, cmd))
summary = []
for lab in labels:
    summary.append({
        'label': lab,
        'warnings': undefs.count(lab),
        'defs': label_defs.get(lab, []),
        'uses': ref_uses.get(lab, []),
    })
outpath = pathlib.Path('/tmp/undefined_refs_live.json')
outpath.write_text(json.dumps(summary, indent=2))
print(f'wrote {outpath}')
print(f'unique_labels={len(labels)} total_warnings={len(undefs)}')
print('no_defs=', sum(1 for x in summary if not x['defs']))
print('defs_present=', sum(1 for x in summary if x['defs']))
print('no_use_found=', sum(1 for x in summary if not x['uses']))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.91s:
wrote /tmp/undefined_refs_live.json
unique_labels=77 total_warnings=165
no_defs= 13
defs_present= 64
no_use_found= 2

thinking
**Inspecting the summary**

I’m thinking I need to inspect the summary carefully. Maybe I can use jq or Python to list no_defs and defs_present along with their uses. I'll query that and see what I find. It feels like a good way to understand the data better! I want to ensure that I'm on the right track with how I examine this. Let’s see what the results tell me when I run the query!
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
p=Path('/tmp/undefined_refs_live.json')
data=json.loads(p.read_text())
for x in data:
    if not x['uses']:
        defs='; '.join(f\"{d[0]}:{d[1]}\" for d in x['defs'])
        print(f\"NO USE FOUND: {x['label']} | warnings={x['warnings']} | defs={defs}\")
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
p=Path('/tmp/undefined_refs_live.json')
data=json.loads(p.read_text())
print('NO LABEL DEFINITIONS')
for x in data:
    if not x['defs']:
        uses='; '.join(f\"{u[0]}:{u[1]} ({u[2]})\" for u in x['uses'])
        print(f\"{x['label']} | warnings={x['warnings']} | uses={uses}\")
print('\\nLABEL EXISTS BUT LOG SAYS UNDEFINED')
for x in data:
    if x['defs']:
        defs='; '.join(f\"{d[0]}:{d[1]}\" for d in x['defs'])
        uses='; '.join(f\"{u[0]}:{u[1]} ({u[2]})\" for u in x['uses'])
        print(f\"{x['label']} | warnings={x['warnings']} | defs={defs} | uses={uses}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
NO LABEL DEFINITIONS
thm:ds-hpl-transfer | warnings=1 | uses=chapters/theory/introduction.tex:2016 (ref)
sec:bar-complex-introduction | warnings=2 | uses=chapters/frame/heisenberg_frame.tex:3467 (ref); chapters/frame/heisenberg_frame.tex:3537 (ref)
sec:complementarity | warnings=1 | uses=chapters/theory/bar_cobar_adjunction_inversion.tex:1980 (ref)
rem:feynman_genus_g | warnings=1 | uses=chapters/theory/higher_genus_foundations.tex:4754 (ref)
sec:landscape-census | warnings=2 | uses=chapters/theory/e1_modular_koszul.tex:694 (ref); chapters/theory/higher_genus_modular_koszul.tex:20508 (ref)
def:glcm-classification | warnings=2 | uses=chapters/theory/higher_genus_modular_koszul.tex:26890 (ref); chapters/connections/arithmetic_shadows.tex:2405 (ref)
comp:sl2-kappa | warnings=1 | uses=staging/for_higher_genus__genus2.tex:582 (eqref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9810 (eqref); staging/combined_for_higher_genus.tex:793 (eqref); chapters/theory/higher_genus_modular_koszul.tex:32866 (eqref)
thm:affine-half-space-bv | warnings=1 | uses=
def:oc-factorization-category | warnings=2 | uses=
prop:heisenberg-kappa | warnings=1 | uses=chapters/examples/y_algebras.tex:340 (ref)
thm:rtt-all-types | warnings=2 | uses=chapters/examples/yangians_computations.tex:1150 (ref); chapters/examples/yangians_foundations.tex:1222 (ref)
thm:baxter-exact-triangles | warnings=7 | uses=chapters/connections/editorial_constitution.tex:1059 (ref); chapters/examples/yangians_computations.tex:2895 (ref); chapters/examples/yangians_computations.tex:3031 (ref); chapters/examples/yangians_computations.tex:3602 (ref); chapters/examples/yangians_computations.tex:3708 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1010 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1731 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1759 (ref)
thm:pro-weyl-recovery | warnings=8 | uses=chapters/connections/concordance.tex:1859 (ref); chapters/connections/editorial_constitution.tex:167 (ref); chapters/connections/editorial_constitution.tex:1061 (ref); chapters/examples/yangians_computations.tex:3550 (ref); chapters/examples/yangians_computations.tex:3592 (ref); chapters/examples/yangians_computations.tex:3720 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1013 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1717 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1783 (ref); chapters/examples/yangians_drinfeld_kohno.tex:2186 (ref); chapters/examples/yangians_drinfeld_kohno.tex:2188 (ref)

LABEL EXISTS BUT LOG SAYS UNDEFINED
conv:three-hochschild | warnings=1 | defs=chapters/connections/concordance.tex:100 | uses=chapters/frame/preface.tex:3664 (ref)
ch:derived-langlands | warnings=6 | defs=chapters/theory/derived_langlands.tex:6 | uses=chapters/theory/introduction.tex:860 (ref); chapters/theory/introduction.tex:1119 (ref); chapters/theory/introduction.tex:2238 (ref); chapters/theory/introduction.tex:2439 (ref); chapters/examples/kac_moody.tex:4399 (ref); chapters/examples/kac_moody.tex:4439 (ref)
part:seven-faces | warnings=8 | defs=main.tex:1450 | uses=main.tex:1486 (ref); chapters/theory/introduction.tex:933 (ref); chapters/theory/introduction.tex:974 (ref); chapters/theory/introduction.tex:1684 (ref); chapters/theory/introduction.tex:2242 (ref); chapters/theory/introduction.tex:2450 (ref); chapters/frame/heisenberg_frame.tex:4802 (ref); chapters/connections/thqg_introduction_supplement_body.tex:1619 (ref); chapters/connections/thqg_introduction_supplement_body.tex:1752 (ref); chapters/connections/thqg_preface_supplement.tex:2017 (ref); chapters/connections/thqg_preface_supplement.tex:2054 (ref); chapters/examples/landscape_census.tex:4048 (ref)
ch:holographic-datum-master | warnings=5 | defs=chapters/connections/holographic_datum_master.tex:2 | uses=chapters/theory/cobar_construction.tex:2042 (ref); chapters/theory/introduction.tex:934 (ref); chapters/theory/introduction.tex:975 (ref); chapters/theory/introduction.tex:2244 (ref); chapters/theory/introduction.tex:2453 (ref)
 succeeded in 52ms:
NO USE FOUND: thm:affine-half-space-bv | warnings=1 | defs=
NO USE FOUND: def:oc-factorization-category | warnings=2 | defs=
exec
/bin/zsh -lc "rg -n \"\\\\\\w*ref\\{(thm:affine-half-space-bv|def:oc-factorization-category)\\}\" chapters appendices *.tex -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:affine-half-space-bv|def:oc-factorization-category" chapters appendices main.tex frontmatter.tex preamble.tex -S' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 2 in 52ms:
rg: frontmatter.tex: No such file or directory (os error 2)
rg: preamble.tex: No such file or directory (os error 2)
appendices/ordered_associative_chiral_kd.tex:5170:the BV-BRST differential (Theorem~\ref*{thm:affine-half-space-bv} of
chapters/connections/thqg_open_closed_realization.tex:662:Definition~\ref*{def:oc-factorization-category}). The same
chapters/connections/thqg_open_closed_realization.tex:707:of Definition~\ref*{def:oc-factorization-category}),
chapters/theory/ordered_associative_chiral_kd.tex:5481:the BV-BRST differential (Theorem~\ref*{thm:affine-half-space-bv} of
codex
I found an audit blind spot: some unresolved targets are referenced with starred forms like `\ref*{...}`, which my first pass didn’t capture. I’m re-running the live-tree scan with starred ref commands included so the file:line mapping is exact.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
root = pathlib.Path('/Users/raeez/chiral-bar-cobar')
log = (root / 'main.log').read_text(errors='ignore')
undefs = re.findall(r\"LaTeX Warning: Reference "'`([''^'"']+)' .* undefined\", log)
labels = []
seen = set()
for lab in undefs:
    if lab not in seen:
        seen.add(lab)
        labels.append(lab)
label_set = set(labels)
label_defs = {}
ref_uses = {lab: [] for lab in labels}
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\([A-Za-z]*ref\\*?)\\{(["'^}]+)'"\\}')
for tex in root.rglob('*.tex'):
    rel = tex.relative_to(root)
    rels = str(rel)
    if rels.startswith('.claude/') or rels.startswith('standalone/') or rels.startswith('archive/'):
        continue
    try:
        lines = tex.read_text(errors='ignore').splitlines()
    except Exception:
        continue
    for i, line in enumerate(lines, start=1):
        for lab in label_re.findall(line):
            label_defs.setdefault(lab, []).append((rels, i))
        for cmd, lab in ref_re.findall(line):
            if lab in label_set:
                ref_uses[lab].append((rels, i, cmd))
summary = []
for lab in labels:
    summary.append({
        'label': lab,
        'warnings': undefs.count(lab),
        'defs': label_defs.get(lab, []),
        'uses': ref_uses.get(lab, []),
    })
outpath = pathlib.Path('/tmp/undefined_refs_live.json')
outpath.write_text(json.dumps(summary, indent=2))
print(f'wrote {outpath}')
print(f'unique_labels={len(labels)} total_warnings={len(undefs)}')
print('no_defs=', sum(1 for x in summary if not x['defs']))
print('defs_present=', sum(1 for x in summary if x['defs']))
print('no_use_found=', sum(1 for x in summary if not x['uses']))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.41s:
wrote /tmp/undefined_refs_live.json
unique_labels=77 total_warnings=165
no_defs= 13
defs_present= 64
no_use_found= 0





thinking
**Categorizing label issues**

I need to sort out some labels. There are 13 labels without any definitions in the live tree, which means they're completely missing. Then, I’ve got 64 labels that have definitions but appear undefined in the log. Some of these definitions are only in staging, not the active build. I should separate those with definitions only in staging from those in the main chapters because that’s causing issues. It seems some labels might have forward references that aren’t compiled yet.
thinking
**Investigating label definitions**

I have a situation where labels are defined in the active chapters but still show as undefined in the log. This might indicate a medium or high issue related to cross-build or inactive inclusions. I need to inspect the `main.aux` or `main.fls` files to see if those definitions are present. If a label exists in an included file but isn’t resolved, it could be due to a commented-out `\input` or an aborted build. I'll check if the chapter is included in `main.tex` to clarify the whole picture.
thinking
**Analyzing LaTeX warnings**

LaTeX warnings at the end show labels not found in the auxiliary files after a full run. If the file containing the label definition isn't included, there won’t be a `\newlabel`. To check, I could search the `*.aux` files for `\newlabel{label}`; if I find none, then it’s not included in the build. However, this doesn’t solve the issue but merely replicates the warning. I might need to classify definitions that are in the active source but missing from the aux due to an inactive include or conditional exclusion.
thinking
**Exploring label definitions**

I am considering whether definitions are based in `main.tex` or relevant files, which might be a bit much. However, I can classify them better: if the defs path starts with `staging/`, it means they exist only outside the build surface, so references are dangling. If the path is in `chapters/` or `main.tex`, it suggests the label is in live source but not resolved in the build. I could confirm this by checking `main.fls` or `main.log` to see which files were read.
thinking
**Analyzing label inclusion**

I’m wondering if the label is in an included file but not written to aux, possibly because it’s inside a dead conditional. If the file appears in `main.fls`, then it must have been input. However, there might still be issues like the label being in a comment or a false condition. If the label definition exists, it should have written to aux unless TeX encountered a fatal error earlier. I need to check for fatal errors in `main.log` to ensure accuracy.
exec
/bin/zsh -lc 'ls main.fls main.aux 2>/dev/null' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
p=Path('/tmp/undefined_refs_live.json')
data=json.loads(p.read_text())
print('NO LABEL DEFINITIONS')
for x in data:
    if not x['defs']:
        uses='; '.join(f\"{u[0]}:{u[1]} ({u[2]})\" for u in x['uses'])
        print(f\"{x['label']} | warnings={x['warnings']} | uses={uses}\")
print('\\nSTAGING-ONLY LABEL DEFINITIONS')
for x in data:
    if x['defs'] and all(d[0].startswith('staging/') for d in x['defs']):
        defs='; '.join(f\"{d[0]}:{d[1]}\" for d in x['defs'])
        uses='; '.join(f\"{u[0]}:{u[1]} ({u[2]})\" for u in x['uses'])
        print(f\"{x['label']} | warnings={x['warnings']} | defs={defs} | uses={uses}\")
print('\\nLIVE-TREE LABEL DEFINITIONS')
for x in data:
    if x['defs'] and any(not d[0].startswith('staging/') for d in x['defs']):
        defs='; '.join(f\"{d[0]}:{d[1]}\" for d in x['defs'])
        uses='; '.join(f\"{u[0]}:{u[1]} ({u[2]})\" for u in x['uses'])
        print(f\"{x['label']} | warnings={x['warnings']} | defs={defs} | uses={uses}\")
PY" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
main.aux
 succeeded in 52ms:
NO LABEL DEFINITIONS
thm:ds-hpl-transfer | warnings=1 | uses=chapters/theory/introduction.tex:2016 (ref)
sec:bar-complex-introduction | warnings=2 | uses=chapters/frame/heisenberg_frame.tex:3467 (ref); chapters/frame/heisenberg_frame.tex:3537 (ref)
sec:complementarity | warnings=1 | uses=chapters/theory/bar_cobar_adjunction_inversion.tex:1980 (ref)
rem:feynman_genus_g | warnings=1 | uses=chapters/theory/higher_genus_foundations.tex:4754 (ref)
sec:landscape-census | warnings=2 | uses=chapters/theory/e1_modular_koszul.tex:694 (ref); chapters/theory/higher_genus_modular_koszul.tex:20508 (ref)
def:glcm-classification | warnings=2 | uses=chapters/theory/higher_genus_modular_koszul.tex:26890 (ref); chapters/connections/arithmetic_shadows.tex:2405 (ref)
comp:sl2-kappa | warnings=1 | uses=staging/for_higher_genus__genus2.tex:582 (eqref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9810 (eqref); staging/combined_for_higher_genus.tex:793 (eqref); chapters/theory/higher_genus_modular_koszul.tex:32866 (eqref)
thm:affine-half-space-bv | warnings=1 | uses=appendices/ordered_associative_chiral_kd.tex:5170 (ref*); chapters/theory/ordered_associative_chiral_kd.tex:5481 (ref*)
def:oc-factorization-category | warnings=2 | uses=chapters/connections/thqg_open_closed_realization.tex:662 (ref*); chapters/connections/thqg_open_closed_realization.tex:707 (ref*)
prop:heisenberg-kappa | warnings=1 | uses=chapters/examples/y_algebras.tex:340 (ref)
thm:rtt-all-types | warnings=2 | uses=chapters/examples/yangians_computations.tex:1150 (ref); chapters/examples/yangians_foundations.tex:1228 (ref)
thm:baxter-exact-triangles | warnings=7 | uses=chapters/connections/editorial_constitution.tex:1059 (ref); chapters/examples/yangians_computations.tex:2895 (ref); chapters/examples/yangians_computations.tex:3031 (ref); chapters/examples/yangians_computations.tex:3602 (ref); chapters/examples/yangians_computations.tex:3708 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1010 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1731 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1759 (ref)
thm:pro-weyl-recovery | warnings=8 | uses=chapters/connections/concordance.tex:1859 (ref); chapters/connections/editorial_constitution.tex:167 (ref); chapters/connections/editorial_constitution.tex:1061 (ref); chapters/examples/yangians_computations.tex:3550 (ref); chapters/examples/yangians_computations.tex:3592 (ref); chapters/examples/yangians_computations.tex:3720 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1013 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1717 (ref); chapters/examples/yangians_drinfeld_kohno.tex:1783 (ref); chapters/examples/yangians_drinfeld_kohno.tex:2186 (ref); chapters/examples/yangians_drinfeld_kohno.tex:2188 (ref)

STAGING-ONLY LABEL DEFINITIONS
prop:ell-degree0 | warnings=3 | defs=staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8413 | uses=staging/for_higher_genus__genus2.tex:265 (ref); staging/for_higher_genus__verlinde.tex:41 (ref); staging/for_higher_genus__verlinde.tex:116 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9070 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9145 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9493 (ref); staging/combined_for_higher_genus.tex:48 (ref); staging/combined_for_higher_genus.tex:123 (ref); staging/combined_for_higher_genus.tex:476 (ref); chapters/theory/higher_genus_modular_koszul.tex:31912 (ref); chapters/theory/higher_genus_modular_koszul.tex:31987 (ref); chapters/theory/higher_genus_modular_koszul.tex:32432 (ref)
prop:ell-degree2 | warnings=1 | defs=staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8677 | uses=staging/for_higher_genus__verlinde.tex:190 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8831 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9219 (ref); staging/combined_for_higher_genus.tex:197 (ref); chapters/theory/higher_genus_modular_koszul.tex:32152 (ref)
thm:ell-ordered-ch | warnings=1 | defs=staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8876 | uses=staging/for_higher_genus__verlinde.tex:191 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9220 (ref); staging/combined_for_higher_genus.tex:198 (ref); chapters/theory/higher_genus_modular_koszul.tex:32153 (ref)
sec:elliptic-ordered | warnings=2 | defs=staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8294 | uses=staging/for_higher_genus__genus2.tex:7 (ref); staging/for_higher_genus__genus2.tex:831 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:558 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9235 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:10059 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:10246 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:10346 (ref); staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:10370 (ref); staging/combined_for_higher_genus.tex:218 (ref); staging/combined_for_higher_genus.tex:1042 (ref); chapters/theory/higher_genus_modular_koszul.tex:32173 (ref)
codex
The live-tree unresolved labels now split cleanly into two families. One family is hard failure: no matching `\label` at all, or the only label lives in `staging/`. The other family is subtler: the source does contain a matching live `\label`, but the current build still leaves it unresolved, so I’m checking the aux surface to see whether those labels ever make it into the compiled manuscript.
exec
/bin/zsh -lc "rg --files -g '*.aux'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import json, re
from pathlib import Path
root=Path('/Users/raeez/chiral-bar-cobar')
aux_files=list(root.rglob('*.aux'))
aux_files=[p for p in aux_files if '.claude/' not in str(p) and 'archive/' not in str(p)]
aux_text='\\n'.join(p.read_text(errors='ignore') for p in aux_files)
data=json.loads(Path('/tmp/undefined_refs_live.json').read_text())
# Only live-tree labels (not staging-only) with defs present
for x in data:
    if x['defs'] and any(not d[0].startswith('staging/') for d in x['defs']):
        present = bool(re.search(r'\\\\newlabel\\{' + re.escape(x['label']) + r'\\}', aux_text))
        print(f\"{x['label']}|aux={'Y' if present else 'N'}|defs={' ; '.join(f'{d[0]}:{d[1]}' for d in x['defs'])}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
main.aux
chapters/frame/heisenberg_frame.aux
chapters/frame/preface.aux
chapters/theory/koszul_pair_structure.aux
chapters/theory/higher_genus.aux
chapters/theory/algebraic_foundations.aux
chapters/theory/configuration_spaces.aux
chapters/theory/poincare_duality.aux
chapters/theory/bar_cobar_adjunction.aux
chapters/theory/chiral_koszul_pairs.aux
chapters/theory/introduction.aux
chapters/theory/cobar_construction.aux
chapters/theory/bar_construction.aux
chapters/theory/three_invariants.aux
 succeeded in 401ms:
conv:three-hochschild|aux=N|defs=chapters/connections/concordance.tex:100
ch:derived-langlands|aux=N|defs=chapters/theory/derived_langlands.tex:6
part:seven-faces|aux=N|defs=main.tex:1450
ch:holographic-datum-master|aux=N|defs=chapters/connections/holographic_datum_master.tex:2
comp:bp-kappa-three-paths|aux=N|defs=chapters/connections/subregular_hook_frontier.tex:905
prop:nilpotent-transport-typeA|aux=N|defs=chapters/connections/subregular_hook_frontier.tex:1519
part:v1-frontier|aux=N|defs=main.tex:1483
ch:genus1-seven-faces|aux=N|defs=chapters/connections/genus1_seven_faces.tex:2
ch:landscape-census|aux=N|defs=chapters/examples/landscape_census.tex:2
thm:langlands-bar-bridge|aux=N|defs=chapters/theory/derived_langlands.tex:95
thm:family-index|aux=N|defs=chapters/connections/outlook.tex:660 ; chapters/connections/concordance.tex:5928
prop:bar-verlinde-asymptotics|aux=N|defs=chapters/examples/genus_expansions.tex:1987
rem:garland-lepowsky-sl2|aux=N|defs=chapters/examples/landscape_census.tex:2035
rem:rank-plus-one|aux=N|defs=chapters/examples/landscape_census.tex:2445
tab:shadow-l-functions|aux=N|defs=chapters/examples/landscape_census.tex:1633
thm:off-koszul-ran-inversion|aux=N|defs=chapters/theory/coderived_models.tex:825
thm:conilpotent-reduction|aux=N|defs=chapters/theory/coderived_models.tex:125
rem:cdr-k3|aux=N|defs=chapters/examples/toroidal_elliptic.tex:2080
def:complementarity-asymmetry|aux=N|defs=chapters/connections/thqg_critical_string_dichotomy.tex:964
lem:thqg-X-composition-decay|aux=N|defs=chapters/connections/thqg_fredholm_partition_functions.tex:447




thinking
**Considering reference counts**

I need to gather source line numbers for the first 100 references, but there's a possibility I won't report them if there are no findings. I could mention that the first 100 references had none. I need to count the instances checked, like 101 reference occurrences found and 165 log warnings. However, these might overlap since the user asked about "Instances checked: N." I think 266 total instances is a reasonable summary, combining unique references and warnings.
thinking
**Deciding on label counts**

I need to determine the counts for different label categories. It looks like we might have 13 labels without definitions and 23 staging-only labels, plus maybe 35 unresolved labels from the live tree. The unique label count is 77, but I'm unsure about the exact breakdown—perhaps 13 with no definitions and 29 staging-only? Oh, and the total number of broken source occurrences might be 165 from log warnings, but these warnings could include more than just `\ref` mentions.
thinking
**Analyzing violation reports**

I think I need to start with the total of 165 violations found, but I realize that the compile log includes duplicates and staging references. I should group the report by labels since it might be too overwhelming to list all 165 lines. There could be 77 unique unresolved labels, and I should mention that. So, after checking 266 instances, the clear verdict seems to lean towards FAIL with 77 unique broken targets noted.
thinking
**Computing failure counts**

I should clarify that the first 100 scans were clean, meaning all failures are coming from the compile log. That seems useful. Now, I need to break down the counts for staging-only, no-defs, and live-tree definitions. It looks like I might have 13 no-defs, along with staging-only and live-tree counts. The total is 77, which breaks down to 13 no-defs, potentially 28 staging-only, and 36 live-tree definitions. I need to get these exact numbers.
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
p=Path('/tmp/undefined_refs_live.json')
data=json.loads(p.read_text())
no_defs=sum(1 for x in data if not x['defs'])
staging_only=sum(1 for x in data if x['defs'] and all(d[0].startswith('staging/') for d in x['defs']))
live_defs=sum(1 for x in data if x['defs'] and any(not d[0].startswith('staging/') for d in x['defs']))
print(no_defs, staging_only, live_defs, no_defs+staging_only+live_defs)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
13 28 36 77

thinking
**Evaluating build configurations**

I need to consider the live-tree definitions, possibly labeling them as MEDIUM, while staging or no-def might be HIGH since the build can't resolve those. Maybe we can categorize some as LOW if they're self-referencing within the same inactive file, but the compile log still shows them as undefined, so that could still be MEDIUM. I suspect verifying whether the 36 live-tree definitions are absent from the aux might help. If they are included later but not built, this might clarify the unresolved references. I’ll also inspect the `main.aux` includes for `@input{...}` lines.
exec
/bin/zsh -lc "sed -n '1,120p' main.aux" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\relax 
\providecommand*{\memsetcounter}[2]{}
\providecommand\hyper@newdestlabel[2]{}
\providecommand\HyField@AuxAddToFields[1]{}
\providecommand\HyField@AuxAddToCoFields[2]{}
\@writefile{toc}{\contentsline {chapter}{Contents}{2}{section*.1}\protected@file@percent }
\@input{chapters/frame/preface.aux}
\gdef \LT@i {\LT@entry 
    {3}{110.87878pt}\LT@entry 
    {1}{253.84842pt}\LT@entry 
    {3}{68.55722pt}}
\@writefile{toc}{\contentsline {chapter}{Guide to main results}{103}{chapter*.80}\protected@file@percent }
\newlabel{ch:guide}{{}{103}{Guide to main results}{chapter*.80}{}}
\citation{MS24}
\citation{RNW19}
\citation{Val16}
\citation{RNW19}
\citation{Mok25}
\newlabel{sec:guide-three-pillars}{{}{105}{Three-pillar foundational architecture}{section*.84}{}}
\@@wrindexm@m{main}{three-pillar architecture|textbf}{105}
exec
/bin/zsh -lc "grep -n '@input' main.aux | tail -20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
47:\@input{chapters/theory/bar_construction.aux}
48:\@input{chapters/theory/cobar_construction.aux}
49:\@input{chapters/theory/bar_cobar_adjunction.aux}
168:\@input{chapters/theory/poincare_duality.aux}
169:\@input{chapters/theory/chiral_koszul_pairs.aux}
170:\@input{chapters/theory/koszul_pair_structure.aux}
171:\@input{chapters/theory/higher_genus.aux}
172:\@input{chapters/theory/chiral_hochschild_koszul.aux}
173:\@input{chapters/theory/chiral_modules.aux}
174:\@input{chapters/theory/poincare_duality_quantum.aux}
175:\@input{chapters/theory/quantum_corrections.aux}
3789:\@input{chapters/examples/lattice_foundations.aux}
3790:\@input{chapters/examples/moonshine.aux}
3791:\@input{chapters/examples/level1_bridge.aux}
3792:\@input{chapters/examples/free_fields.aux}
3793:\@input{chapters/examples/beta_gamma.aux}
4095:\@input{chapters/examples/kac_moody.aux}
4096:\@input{chapters/examples/w_algebras.aux}
5365:\@input{chapters/examples/w3_holographic_datum.aux}
5366:\@input{chapters/examples/deformation_quantization.aux}


thinking
**Organizing findings by labels**

The user wants me to report every finding with file:line, so I might group them by label to keep it concise. Since I could manage about 77 lines, that should be acceptable, but I need to consider how to handle multiple live use locations by listing them separated by `;`. It could get long, but grouping by label and listing occurrences in the description seems better than overwhelming with 165 lines. I'll try to focus on live uses only, skipping staging ones if possible.
thinking
**Creating markdown by severity**

I might need to produce markdown that organizes findings by severity. For example, I could format it like this: 

[HIGH] [chapters/theory/introduction.tex:2016](...) — `\ref{thm:ds-hpl-transfer}` has no corresponding `\label{thm:ds-hpl-transfer}` in the live tree. 

Establishing clear sections for different severity levels could help present the information more effectively. It’s all about making things easier to navigate while ensuring details are clear and logically structured for the user.
codex
I have the final classification. The remaining unresolved labels all fall into evidence-backed buckets: 13 have no live `\label` anywhere, 28 are only labeled inside `staging/` snapshots, and 36 do have live source labels but those labels never enter the current aux surface, so the build still leaves them undefined.
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
root=Path('/Users/raeez/chiral-bar-cobar')
data=json.loads(Path('/tmp/undefined_refs_live.json').read_text())

def link(rel, line):
    return f\"[{rel}]({root / rel}:{line})\"

high=[]
medium=[]
for x in data:
    live_uses=[u for u in x['uses'] if not u[0].startswith('staging/')]
    if not live_uses:
        continue
    uses='; '.join(f\"{u[0]}:{u[1]}\" for u in live_uses)
    use_links='; '.join(link(u[0], u[1]) for u in live_uses)
    live_defs=[d for d in x['defs'] if not d[0].startswith('staging/')]
    staging_defs=[d for d in x['defs'] if d[0].startswith('staging/')]
    if not x['defs']:
        high.append(f\"[HIGH] {use_links} — "'`{x['"'label']}"'` is referenced here but no matching `'"\\\\label{{{x['label']}}}"'` exists anywhere in the live tree.")
    elif live_defs:
        defs='"'; '.join(link(d[0], d[1]) for d in live_defs)
        medium.append(f\"[MEDIUM] {use_links} — "'`{x['"'label']}"'` is still undefined in `main.log` even though a live `'"\\\\label"'` exists at {defs}; no `'"\\\\newlabel{{{x['label']}}}"'` appears in the current aux surface.")
    elif staging_defs:
        defs='"'; '.join(link(d[0], d[1]) for d in staging_defs)
        high.append(f\"[HIGH] {use_links} — "'`{x['"'label']}"'` only has matching `'"\\\\label"'` definitions in `staging/` ({defs}), so the active manuscript references an uncompiled target.")
out='"'\\n'.join(high + medium)
Path('/tmp/ref_audit_report.md').write_text(out)
print(f\"high={len(high)} medium={len(medium)} total={len(high)+len(medium)}\")
print('wrote /tmp/ref_audit_report.md')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
high=40 medium=36 total=76
wrote /tmp/ref_audit_report.md
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
p=Path('/tmp/undefined_refs_live.json')
data=json.loads(p.read_text())
for x in data:
    live=[u for u in x['uses'] if not u[0].startswith('staging/')]
    if not live:
        print(x['label'], x['warnings'], x['defs'])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rem:dynamical-parameter 1 [['staging/ordered_chiral_homology_BACKUP_20260412_225116.tex', 8652]]

thinking
**Exploring log warnings**

I'm noticing an interesting compile log warning regarding `rem:dynamical-parameter`, but it seems like this is only used in staging. It’s curious because the `main.log` shouldn't originate from staging. Maybe the chapter file was copied from staging, and the usage is inside a line that isn’t captured? I wonder if our live uses list points back to staging because in the live chapters, there are references at specific lines. I should search directly for the log line within the included file.
exec
/bin/zsh -lc 'rg -n "rem:dynamical-parameter" chapters appendices main.tex -S' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:



thinking
**Evaluating compile log warnings**

Hmm, it looks like there's a warning about an undefined reference, possibly from an old, stale auxiliary file. Since the user is asking about the compile log, I wonder if we should exclude it since it's not linked to a current source file. The log mentions a specific line with an issue, but without the corresponding source file, I can't pinpoint it. Maybe I should mention it as a log-only warning? But it complicates the structured output. I'll need to double-check the repository to see if this label string is there.
thinking
**Assessing unresolved labels**

Since I can’t provide a specific file:line reference, it might be best to exclude it from the findings and note it in the summary as an unresolved log-only label at `main.log line 7409`. But the contract states I should report every finding with a file:line. I could use `main.log:7409` as a reference for the unresolved label, noting its absence in the live source. I’ll consider marking its severity as LOW or MEDIUM, given it’s only in the compile log. I need to check for any other similar labels as well.
exec
/bin/zsh -lc "sed -n '1,120p' /tmp/ref_audit_report.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
[HIGH] [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2016) — `thm:ds-hpl-transfer` is referenced here but no matching `\label{thm:ds-hpl-transfer}` exists anywhere in the live tree.
[HIGH] [chapters/frame/heisenberg_frame.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:3467); [chapters/frame/heisenberg_frame.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:3537) — `sec:bar-complex-introduction` is referenced here but no matching `\label{sec:bar-complex-introduction}` exists anywhere in the live tree.
[HIGH] [chapters/theory/bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1980) — `sec:complementarity` is referenced here but no matching `\label{sec:complementarity}` exists anywhere in the live tree.
[HIGH] [chapters/theory/higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:4754) — `rem:feynman_genus_g` is referenced here but no matching `\label{rem:feynman_genus_g}` exists anywhere in the live tree.
[HIGH] [chapters/theory/e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:694); [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:20508) — `sec:landscape-census` is referenced here but no matching `\label{sec:landscape-census}` exists anywhere in the live tree.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:26890); [chapters/connections/arithmetic_shadows.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2405) — `def:glcm-classification` is referenced here but no matching `\label{def:glcm-classification}` exists anywhere in the live tree.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:31912); [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:31987); [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32432) — `prop:ell-degree0` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8413)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32152) — `prop:ell-degree2` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8677)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32153) — `thm:ell-ordered-ch` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8876)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32173) — `sec:elliptic-ordered` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8294)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32323); [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32561) — `eq:kzb-ell` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8366)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32367) — `eq:kzb-tau` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8597)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32471); [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32496) — `eq:bar-degree1-yangian` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8486)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32857) — `subsec:ell-degree2` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8528)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32866) — `comp:sl2-kappa` is referenced here but no matching `\label{comp:sl2-kappa}` exists anywhere in the live tree.
[HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32890) — `eq:ell-braid` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8763)), so the active manuscript references an uncompiled target.
[HIGH] [appendices/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:5170); [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5481) — `thm:affine-half-space-bv` is referenced here but no matching `\label{thm:affine-half-space-bv}` exists anywhere in the live tree.
[HIGH] [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:6047); [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:6166); [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8107); [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8132); [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8168) — `ex:yangian` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:608)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:6048); [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:6146); [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:6159); [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7131); [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:9746) — `conj:yangian-ordered-center` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1158)), so the active manuscript references an uncompiled target.
[HIGH] [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:6167); [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8173) — `eq:yangian-ker-av2` only has matching `\label` definitions in `staging/` ([staging/ordered_chiral_homology_BACKUP_20260412_225116.tex](/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:917)), so the active manuscript references an uncompiled target.

thinking
**Formatting findings for report**

I need to prepare the findings with a simpler format, focusing on severity, so maybe ordering them by HIGH and MEDIUM. The user wants to see every finding, even if it exceeds 70 lines. I could mention at the top that the first 100 scans are clean, but I wonder if it’s better to place that before or after the findings? Also, I'll need to include a [LOW] finding for the `main.log:7409` as it wasn’t reported previously. Let’s see if I can get that in there too.
exec
/bin/zsh -lc "sed -n '7398,7415p' main.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

[1191]

[1192]

[1193]

[1194]

[1195]

[1196]

[1197]

[1198]

[1199]

thinking
**Clarifying sed usage**

I’m thinking the warning could stem from how I'm using line numbers with sed versus log line numbers. Actually, the log file isn’t numbered by line, so when I use sed, it's referencing the file's actual line positions, which might not match up due to wrapping. I’ll need to use the command `nl -ba main.log | sed -n '7400,7415p'` to correctly reference the lines I want.
exec
/bin/zsh -lc "nl -ba main.log | sed -n '7400,7415p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7400	
  7401	[1192]
  7402	
  7403	[1193]
  7404	
  7405	[1194]
  7406	
  7407	[1195]
  7408	
  7409	[1196]
  7410	
  7411	[1197]
  7412	
  7413	[1198]
  7414	
  7415	[1199]
exec
/bin/zsh -lc 'rg -n "rem:dynamical-parameter" main.log' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Investigating log updates**

I'm noticing that the label might not be present due to recent log updates. I remember that earlier it printed correctly, so I'm wondering if the log has changed in some way. There might be some strange line breaks causing issues. I think it would be helpful to search for the partial term "dynamical" to see if that reveals anything useful. Let's see what I can find!
exec
/bin/zsh -lc 'grep -n "dynamical" main.log | head' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc 'rg -n "conv:three-hochschild|rem:dynamical-parameter|There were undefined references" main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2199:LaTeX Warning: Reference `conv:three-hochschild' on page 95 undefined on input 
16341:LaTeX Warning: There were undefined references.

thinking
**Verifying log findings**

I'm wondering if the main.log could have been modified by a concurrent background build after running the script. It's unclear, so I need to avoid any false positives and re-verify my findings. I'll rerun the extraction of undefined labels and compare it. The user asked for this re-verification, so I should check the current list to see if the counts or any labels have changed since the last extraction. Final verification is essential!
codex
I hit one moving-target case in `main.log`, so I’m re-reading the current log and rebuilding the undefined-label set from scratch before finalizing. That should eliminate any stale warnings or transient false positives.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('/Users/raeez/chiral-bar-cobar')
log=(root/'main.log').read_text(errors='ignore')
labels=[]
seen=set()
for lab in re.findall(r\"LaTeX Warning: Reference "'`([''^'"']+)' .* undefined\", log):
    if lab not in seen:
        seen.add(lab)
        labels.append(lab)
print('unique', len(labels))
for lab in labels:
    print(lab)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
unique 76
conv:three-hochschild
ch:derived-langlands
part:seven-faces
ch:holographic-datum-master
comp:bp-kappa-three-paths
prop:nilpotent-transport-typeA
part:v1-frontier
thm:ds-hpl-transfer
ch:genus1-seven-faces
sec:bar-complex-introduction
ch:landscape-census
sec:complementarity
thm:langlands-bar-bridge
thm:family-index
rem:feynman_genus_g
sec:landscape-census
def:glcm-classification
prop:ell-degree0
prop:bar-verlinde-asymptotics
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
root=pathlib.Path('/Users/raeez/chiral-bar-cobar')
log=(root/'main.log').read_text(errors='ignore')
warns=re.findall(r\"LaTeX Warning: Reference "'`([''^'"']+)' .* undefined\", log)
print('total_warnings', len(warns))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
total_warnings 163
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
root = pathlib.Path('/Users/raeez/chiral-bar-cobar')
log = (root / 'main.log').read_text(errors='ignore')
undefs = re.findall(r\"LaTeX Warning: Reference "'`([''^'"']+)' .* undefined\", log)
labels = []
seen = set()
for lab in undefs:
    if lab not in seen:
        seen.add(lab)
        labels.append(lab)
label_set = set(labels)
label_defs = {}
ref_uses = {lab: [] for lab in labels}
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\([A-Za-z]*ref\\*?)\\{(["'^}]+)'"\\}')
for tex in root.rglob('*.tex'):
    rel = tex.relative_to(root)
    rels = str(rel)
    if rels.startswith('.claude/') or rels.startswith('standalone/') or rels.startswith('archive/'):
        continue
    try:
        lines = tex.read_text(errors='ignore').splitlines()
    except Exception:
        continue
    for i, line in enumerate(lines, start=1):
        for lab in label_re.findall(line):
            label_defs.setdefault(lab, []).append((rels, i))
        for cmd, lab in ref_re.findall(line):
            if lab in label_set:
                ref_uses[lab].append((rels, i, cmd))
summary=[]
for lab in labels:
    summary.append({'label':lab,'warnings':undefs.count(lab),'defs':label_defs.get(lab,[]),'uses':ref_uses.get(lab,[])})
Path('/tmp/undefined_refs_live.json').write_text(json.dumps(summary, indent=2))
print('wrote /tmp/undefined_refs_live.json')
print('unique', len(labels), 'warnings', len(undefs))
print('no_defs', sum(1 for x in summary if not x['defs']))
print('staging_only', sum(1 for x in summary if x['defs'] and all(d[0].startswith('staging/') for d in x['defs'])))
print('live_defs', sum(1 for x in summary if x['defs'] and any(not d[0].startswith('staging/') for d in x['defs'])))
PY" in /Users/raeez/chiral-bar-cobar exited 1 in 509ms:
Traceback (most recent call last):
  File "<stdin>", line 34, in <module>
NameError: name 'Path' is not defined
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
root = pathlib.Path('/Users/raeez/chiral-bar-cobar')
log = (root / 'main.log').read_text(errors='ignore')
undefs = re.findall(r\"LaTeX Warning: Reference "'`([''^'"']+)' .* undefined\", log)
labels = []
seen = set()
for lab in undefs:
    if lab not in seen:
        seen.add(lab)
        labels.append(lab)
label_set = set(labels)
label_defs = {}
ref_uses = {lab: [] for lab in labels}
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\([A-Za-z]*ref\\*?)\\{(["'^}]+)'"\\}')
for tex in root.rglob('*.tex'):
    rel = tex.relative_to(root)
    rels = str(rel)
    if rels.startswith('.claude/') or rels.startswith('standalone/') or rels.startswith('archive/'):
        continue
    try:
        lines = tex.read_text(errors='ignore').splitlines()
    except Exception:
        continue
    for i, line in enumerate(lines, start=1):
        for lab in label_re.findall(line):
            label_defs.setdefault(lab, []).append((rels, i))
        for cmd, lab in ref_re.findall(line):
            if lab in label_set:
                ref_uses[lab].append((rels, i, cmd))
summary=[]
for lab in labels:
    summary.append({'label':lab,'warnings':undefs.count(lab),'defs':label_defs.get(lab,[]),'uses':ref_uses.get(lab,[])})
(root.parent / 'tmp_placeholder').parent
(pathlib.Path('/tmp') / 'undefined_refs_live.json').write_text(json.dumps(summary, indent=2))
print('wrote /tmp/undefined_refs_live.json')
print('unique', len(labels), 'warnings', len(undefs))
print('no_defs', sum(1 for x in summary if not x['defs']))
print('staging_only', sum(1 for x in summary if x['defs'] and all(d[0].startswith('staging/') for d in x['defs'])))
print('live_defs', sum(1 for x in summary if x['defs'] and any(not d[0].startswith('staging/') for d in x['defs'])))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 496ms:
wrote /tmp/undefined_refs_live.json
unique 76 warnings 163
no_defs 13
staging_only 27
live_defs 36
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
root=Path('/Users/raeez/chiral-bar-cobar')
data=json.loads(Path('/tmp/undefined_refs_live.json').read_text())

def link(rel, line):
    return f\"[{rel}]({root / rel}:{line})\"

high=[]
medium=[]
for x in data:
    live_uses=[u for u in x['uses'] if not u[0].startswith('staging/')]
    if not live_uses:
        continue
    use_links='; '.join(link(u[0], u[1]) for u in live_uses)
    live_defs=[d for d in x['defs'] if not d[0].startswith('staging/')]
    staging_defs=[d for d in x['defs'] if d[0].startswith('staging/')]
    if not x['defs']:
        high.append(f\"[HIGH] {use_links} — "'`{x['"'label']}"'` is referenced here but no matching `'"\\\\label{{{x['label']}}}"'` exists anywhere in the live tree.")
    elif live_defs:
        defs='"'; '.join(link(d[0], d[1]) for d in live_defs)
        medium.append(f\"[MEDIUM] {use_links} — "'`{x['"'label']}"'` is still undefined in `main.log` even though a live `'"\\\\label"'` exists at {defs}; no `'"\\\\newlabel{{{x['label']}}}"'` appears in the current aux surface.")
    elif staging_defs:
        defs='"'; '.join(link(d[0], d[1]) for d in staging_defs)
        high.append(f\"[HIGH] {use_links} — "'`{x['"'label']}"'` only has matching `'"\\\\label"'` definitions in `staging/` ({defs}), so the active manuscript references an uncompiled target.")
Path('"'/tmp/ref_audit_report.md').write_text('\\n'.join(high + medium))
print('high', len(high), 'medium', len(medium), 'total', len(high)+len(medium))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
high 40 medium 36 total 76

thinking
**Clarifying reporting findings**

I think I need to include a note about having no findings in the first 100 references scanned. It might make sense to place this note either before or after the findings section. The user asked for a report on every finding, so a brief mention of the first 100 being clean could be helpful. I also want to summarize the instances checked, which total 264 (101 references plus 163 warnings). I should verify that the first 100 count is still accurate.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess
root=pathlib.Path('/Users/raeez/chiral-bar-cobar')
out=subprocess.check_output(r\"grep -rn '\\\\ref{' chapters/ | head -100\", shell=True, cwd=root, text=True)
entries=[]
label_map={}
for tex in root.rglob('*.tex'):
    rel=str(tex.relative_to(root))
    if rel.startswith('.claude/') or rel.startswith('standalone/') or rel.startswith('archive/'):
        continue
    for i, line in enumerate(tex.read_text(errors='ignore').splitlines(), start=1):
        for lab in re.findall(r'\\\\label\\{(["'^}]+)'"\\}', line):
            label_map.setdefault(lab, []).append((rel,i))
for line in out.splitlines():
    m=re.match(r'(["'^:]+):('"\\d+):(.*)', line)
    if not m:
        continue
    path, lineno, text=m.groups()
    for lab in re.findall(r'\\\\ref\\{(["'^}]+)'"\\}', text):
        entries.append((path,int(lineno),lab))
missing=[e for e in entries if e[2] not in label_map]
print('occurrences', len(entries), 'unique_labels', len({e[2] for e in entries}), 'missing', len(missing))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 510ms:
occurrences 101 unique_labels 52 missing 0


thinking
**Considering file reference options**

I'm thinking about how to handle 76 findings, especially regarding clickable links. They make the lines really long, so maybe using plain relative file:line references would be better. This could satisfy the user without cluttering the format. However, the developer prefers clickable local file links, so I’m weighing my options. For this large audit, I believe plain file:line references are more practical. I might also consider including some clickable links while keeping the overall format tidy.
thinking
**Considering file paths for reports**

I'm thinking that using multiple clickable absolute file paths creates a lot of noise, so maybe plain relative paths would be better. I should also probably mention the first 100 scans as clean. It seems like my findings should be grouped and condensed. I think generating a report that shows plain file:line references grouped by label could be really helpful. I guess I could use a script for that. Let's go ahead and do it!
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path

data=json.loads(Path('/tmp/undefined_refs_live.json').read_text())

def fmt_locs(locs):
    return '; '.join(f\"{p}:{ln}\" for p,ln,*_ in locs if not p.startswith('staging/'))

def fmt_defs(defs):
    return '; '.join(f\"{p}:{ln}\" for p,ln in defs)

high=[]
medium=[]
for x in data:
    live_uses=[u for u in x['uses'] if not u[0].startswith('staging/')]
    if not live_uses:
        continue
    live_defs=[d for d in x['defs'] if not d[0].startswith('staging/')]
    staging_defs=[d for d in x['defs'] if d[0].startswith('staging/')]
    if not x['defs']:
        high.append(f\"[HIGH] {fmt_locs(live_uses)} — "'`{x['"'label']}"'` is referenced here but no matching `'"\\\\label{{{x['label']}}}"'` exists anywhere in the live tree.")
    elif live_defs:
        medium.append(f"[MEDIUM] {fmt_locs(live_uses)} — `{x['"'label']}"'` is still undefined in `main.log` even though a live `'"\\\\label"'` exists at {fmt_defs(live_defs)}; no `'"\\\\newlabel{{{x['label']}}}"'` appears in the current aux surface.")
    elif staging_defs:
        high.append(f"[HIGH] {fmt_locs(live_uses)} — `{x['"'label']}"'` only has matching `'"\\\\label"'` definitions in `staging/` ({fmt_defs(staging_defs)}), so the active manuscript references an uncompiled target.")
Path('"'/tmp/ref_audit_report_plain.md').write_text('\\n'.join(high + medium))
print('wrote /tmp/ref_audit_report_plain.md')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
wrote /tmp/ref_audit_report_plain.md
exec
/bin/zsh -lc "wc -l /tmp/ref_audit_report_plain.md && sed -n '1,120p' /tmp/ref_audit_report_plain.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
      75 /tmp/ref_audit_report_plain.md
[HIGH] chapters/theory/introduction.tex:2016 — `thm:ds-hpl-transfer` is referenced here but no matching `\label{thm:ds-hpl-transfer}` exists anywhere in the live tree.
[HIGH] chapters/frame/heisenberg_frame.tex:3467; chapters/frame/heisenberg_frame.tex:3537 — `sec:bar-complex-introduction` is referenced here but no matching `\label{sec:bar-complex-introduction}` exists anywhere in the live tree.
[HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:1980 — `sec:complementarity` is referenced here but no matching `\label{sec:complementarity}` exists anywhere in the live tree.
[HIGH] chapters/theory/higher_genus_foundations.tex:4754 — `rem:feynman_genus_g` is referenced here but no matching `\label{rem:feynman_genus_g}` exists anywhere in the live tree.
[HIGH] chapters/theory/e1_modular_koszul.tex:694; chapters/theory/higher_genus_modular_koszul.tex:20508 — `sec:landscape-census` is referenced here but no matching `\label{sec:landscape-census}` exists anywhere in the live tree.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:26890; chapters/connections/arithmetic_shadows.tex:2405 — `def:glcm-classification` is referenced here but no matching `\label{def:glcm-classification}` exists anywhere in the live tree.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:31912; chapters/theory/higher_genus_modular_koszul.tex:31987; chapters/theory/higher_genus_modular_koszul.tex:32432 — `prop:ell-degree0` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8413), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32152 — `prop:ell-degree2` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8677), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32153 — `thm:ell-ordered-ch` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8876), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32173 — `sec:elliptic-ordered` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8294), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32323; chapters/theory/higher_genus_modular_koszul.tex:32561 — `eq:kzb-ell` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8366), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32367 — `eq:kzb-tau` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8597), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32471; chapters/theory/higher_genus_modular_koszul.tex:32496 — `eq:bar-degree1-yangian` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8486), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32857 — `subsec:ell-degree2` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8528), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32866 — `comp:sl2-kappa` is referenced here but no matching `\label{comp:sl2-kappa}` exists anywhere in the live tree.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32890 — `eq:ell-braid` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8763), so the active manuscript references an uncompiled target.
[HIGH] appendices/ordered_associative_chiral_kd.tex:5170; chapters/theory/ordered_associative_chiral_kd.tex:5481 — `thm:affine-half-space-bv` is referenced here but no matching `\label{thm:affine-half-space-bv}` exists anywhere in the live tree.
[HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6047; chapters/theory/ordered_associative_chiral_kd.tex:6166; chapters/theory/ordered_associative_chiral_kd.tex:8107; chapters/theory/ordered_associative_chiral_kd.tex:8132; chapters/theory/ordered_associative_chiral_kd.tex:8168 — `ex:yangian` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:608), so the active manuscript references an uncompiled target.
[HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6048; chapters/theory/ordered_associative_chiral_kd.tex:6146; chapters/theory/ordered_associative_chiral_kd.tex:6159; chapters/connections/concordance.tex:7131; chapters/connections/concordance.tex:9746 — `conj:yangian-ordered-center` only has matching `\label` definitions in `staging/` (staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1158), so the active manuscript references an uncompiled target.




thinking
**Evaluating report findings**

I found 76 unique broken targets or 163 warnings. For the final report, the summary could say, "Violations found: 76." I think I should mention the "163 warning instances in main.log collapsed to 76 unique broken targets" too. But since the contract specifies a summary with number N, I might just go with 76. I wonder if I should include a parenthetical; maybe not. The user did ask for a report with "file:line" details.
thinking
**Organizing scan results**

I’m considering how to structure my findings from the scan. I think it might be best to summarize first, highlighting that the first 100 scans are clean. I want to mention that all remaining violations arise from the current compile log. 

I might format it like this: “First-100 scan: 101 \ref occurrences from \`grep...; 0 missing labels.” Then, I'll list the findings ordered. I should keep it simple, avoiding nested bullets while considering headers.
thinking
**Streamlining report**

I want to use the markdown section `## Summary` without any conversational openers, which is good. I need to think about the final length of the report since it should be around 80 lines, but I may not include all 75 lines if it gets too lengthy. 

It could help to introduce a note about MEDIUM entries mentioning that they have a live label but no newlabel in aux. For instance, I could shorten entries like `[MEDIUM] chapters/... — \`conv:three-hochschild\`` to make them more concise. Reducing repetitive phrases will also help!
thinking
**Generating concise lines**

I’m thinking about how to rephrase "only has matching \label definitions in staging/" to "label exists only in staging at...". This change could make the lines more concise and easier to read. I want to focus on generating straightforward lines for clarity, as it seems like a simple adjustment that will streamline the content. Keeping things concise can help the user better understand the report without getting bogged down in longer phrases.
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path

data=json.loads(Path('/tmp/undefined_refs_live.json').read_text())

def fmt_locs(locs):
    return '; '.join(f\"{p}:{ln}\" for p,ln,*_ in locs if not p.startswith('staging/'))

def fmt_defs(defs):
    return '; '.join(f\"{p}:{ln}\" for p,ln in defs)

lines=[]
for x in data:
    live_uses=[u for u in x['uses'] if not u[0].startswith('staging/')]
    if not live_uses:
        continue
    live_defs=[d for d in x['defs'] if not d[0].startswith('staging/')]
    staging_defs=[d for d in x['defs'] if d[0].startswith('staging/')]
    if not x['defs']:
        lines.append(f\"[HIGH] {fmt_locs(live_uses)} — "'`{x['"'label']}"'` has no matching live `'"\\\\label"'`." )
    elif live_defs:
        lines.append(f"[MEDIUM] {fmt_locs(live_uses)} — `{x['"'label']}"'` is undefined in `main.log`; live `'"\\\\label"'` at {fmt_defs(live_defs)}, but it never reaches the current aux surface.")
    elif staging_defs:
        lines.append(f"[HIGH] {fmt_locs(live_uses)} — `{x['"'label']}"'` is defined only in `staging/` at {fmt_defs(staging_defs)}.")
Path('"'/tmp/ref_audit_report_concise.md').write_text('\\n'.join(lines))
print('wrote /tmp/ref_audit_report_concise.md')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
wrote /tmp/ref_audit_report_concise.md
exec
/bin/zsh -lc "wc -l /tmp/ref_audit_report_concise.md && sed -n '1,120p' /tmp/ref_audit_report_concise.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
      75 /tmp/ref_audit_report_concise.md
[MEDIUM] chapters/frame/preface.tex:3664 — `conv:three-hochschild` is undefined in `main.log`; live `\label` at chapters/connections/concordance.tex:100, but it never reaches the current aux surface.
[MEDIUM] chapters/theory/introduction.tex:860; chapters/theory/introduction.tex:1119; chapters/theory/introduction.tex:2238; chapters/theory/introduction.tex:2439; chapters/examples/kac_moody.tex:4399; chapters/examples/kac_moody.tex:4439 — `ch:derived-langlands` is undefined in `main.log`; live `\label` at chapters/theory/derived_langlands.tex:6, but it never reaches the current aux surface.
[MEDIUM] main.tex:1486; chapters/theory/introduction.tex:933; chapters/theory/introduction.tex:974; chapters/theory/introduction.tex:1684; chapters/theory/introduction.tex:2242; chapters/theory/introduction.tex:2450; chapters/frame/heisenberg_frame.tex:4802; chapters/connections/thqg_introduction_supplement_body.tex:1619; chapters/connections/thqg_introduction_supplement_body.tex:1752; chapters/connections/thqg_preface_supplement.tex:2017; chapters/connections/thqg_preface_supplement.tex:2054; chapters/examples/landscape_census.tex:4048 — `part:seven-faces` is undefined in `main.log`; live `\label` at main.tex:1450, but it never reaches the current aux surface.
[MEDIUM] chapters/theory/cobar_construction.tex:2042; chapters/theory/introduction.tex:934; chapters/theory/introduction.tex:975; chapters/theory/introduction.tex:2244; chapters/theory/introduction.tex:2453 — `ch:holographic-datum-master` is undefined in `main.log`; live `\label` at chapters/connections/holographic_datum_master.tex:2, but it never reaches the current aux surface.
[MEDIUM] chapters/theory/introduction.tex:1179; chapters/connections/subregular_hook_frontier.tex:966 — `comp:bp-kappa-three-paths` is undefined in `main.log`; live `\label` at chapters/connections/subregular_hook_frontier.tex:905, but it never reaches the current aux surface.
[MEDIUM] chapters/theory/introduction.tex:1180; chapters/connections/subregular_hook_frontier.tex:1674 — `prop:nilpotent-transport-typeA` is undefined in `main.log`; live `\label` at chapters/connections/subregular_hook_frontier.tex:1519, but it never reaches the current aux surface.
[MEDIUM] main.tex:1488; chapters/theory/introduction.tex:1941; chapters/theory/introduction.tex:2248; chapters/theory/introduction.tex:2468; chapters/connections/concordance.tex:3799 — `part:v1-frontier` is undefined in `main.log`; live `\label` at main.tex:1483, but it never reaches the current aux surface.
[HIGH] chapters/theory/introduction.tex:2016 — `thm:ds-hpl-transfer` has no matching live `\label`.
[MEDIUM] chapters/theory/introduction.tex:2246; chapters/theory/introduction.tex:2462; chapters/connections/concordance.tex:6510 — `ch:genus1-seven-faces` is undefined in `main.log`; live `\label` at chapters/connections/genus1_seven_faces.tex:2, but it never reaches the current aux surface.
[HIGH] chapters/frame/heisenberg_frame.tex:3467; chapters/frame/heisenberg_frame.tex:3537 — `sec:bar-complex-introduction` has no matching live `\label`.
[MEDIUM] chapters/theory/three_invariants.tex:234; chapters/connections/genus1_seven_faces.tex:1040; chapters/connections/holomorphic_topological.tex:43 — `ch:landscape-census` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:2, but it never reaches the current aux surface.
[HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:1980 — `sec:complementarity` has no matching live `\label`.
[MEDIUM] chapters/theory/chiral_koszul_pairs.tex:1424; chapters/connections/arithmetic_shadows.tex:105; chapters/connections/arithmetic_shadows.tex:11156 — `thm:langlands-bar-bridge` is undefined in `main.log`; live `\label` at chapters/theory/derived_langlands.tex:95, but it never reaches the current aux surface.
[MEDIUM] chapters/theory/higher_genus_foundations.tex:194; chapters/theory/higher_genus_foundations.tex:633; chapters/theory/higher_genus_foundations.tex:1074; chapters/theory/higher_genus_foundations.tex:5405; chapters/theory/higher_genus_foundations.tex:6388; chapters/theory/higher_genus_foundations.tex:6789; chapters/theory/higher_genus_foundations.tex:6827; chapters/theory/higher_genus_foundations.tex:6897; chapters/theory/higher_genus_modular_koszul.tex:2730; chapters/theory/higher_genus_modular_koszul.tex:2806; chapters/theory/higher_genus_modular_koszul.tex:2816; chapters/theory/higher_genus_modular_koszul.tex:4407; chapters/theory/higher_genus_modular_koszul.tex:4457; chapters/theory/higher_genus_modular_koszul.tex:9507; chapters/theory/higher_genus_modular_koszul.tex:13934; chapters/frame/heisenberg_frame.tex:1616; chapters/frame/heisenberg_frame.tex:1718; chapters/frame/heisenberg_frame.tex:4642; chapters/connections/concordance.tex:4712; chapters/connections/concordance.tex:6227; chapters/connections/bv_brst.tex:1502; chapters/connections/thqg_fredholm_partition_functions.tex:1449; chapters/connections/editorial_constitution.tex:2579; chapters/connections/editorial_constitution.tex:2668; chapters/examples/genus_expansions.tex:169; chapters/examples/genus_expansions.tex:1904; chapters/examples/heisenberg_eisenstein.tex:1738 — `thm:family-index` is undefined in `main.log`; live `\label` at chapters/connections/outlook.tex:660; chapters/connections/concordance.tex:5928, but it never reaches the current aux surface.
[HIGH] chapters/theory/higher_genus_foundations.tex:4754 — `rem:feynman_genus_g` has no matching live `\label`.
[HIGH] chapters/theory/e1_modular_koszul.tex:694; chapters/theory/higher_genus_modular_koszul.tex:20508 — `sec:landscape-census` has no matching live `\label`.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:26890; chapters/connections/arithmetic_shadows.tex:2405 — `def:glcm-classification` has no matching live `\label`.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:31912; chapters/theory/higher_genus_modular_koszul.tex:31987; chapters/theory/higher_genus_modular_koszul.tex:32432 — `prop:ell-degree0` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8413.
[MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:32123 — `prop:bar-verlinde-asymptotics` is undefined in `main.log`; live `\label` at chapters/examples/genus_expansions.tex:1987, but it never reaches the current aux surface.

thinking
**Reordering the report**

I see that the report is currently ordered by a JSON structure. I think it's important to reorder it by severity instead. Maybe I won’t need to do this manually if I can generate the final lines sorted by severity. So, I'll focus on generating the sections for high severity first, then move on to medium severity. This way, I ensure that the most critical information is highlighted appropriately.
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path

data=json.loads(Path('/tmp/undefined_refs_live.json').read_text())

def fmt_locs(locs):
    return '; '.join(f\"{p}:{ln}\" for p,ln,*_ in locs if not p.startswith('staging/'))

def fmt_defs(defs):
    return '; '.join(f\"{p}:{ln}\" for p,ln in defs)

high=[]
medium=[]
for x in data:
    live_uses=[u for u in x['uses'] if not u[0].startswith('staging/')]
    if not live_uses:
        continue
    live_defs=[d for d in x['defs'] if not d[0].startswith('staging/')]
    staging_defs=[d for d in x['defs'] if d[0].startswith('staging/')]
    if not x['defs']:
        high.append(f\"[HIGH] {fmt_locs(live_uses)} — "'`{x['"'label']}"'` has no matching live `'"\\\\label"'`.")
    elif live_defs:
        medium.append(f"[MEDIUM] {fmt_locs(live_uses)} — `{x['"'label']}"'` is undefined in `main.log`; live `'"\\\\label"'` at {fmt_defs(live_defs)}, but it never reaches the current aux surface.")
    elif staging_defs:
        high.append(f"[HIGH] {fmt_locs(live_uses)} — `{x['"'label']}"'` is defined only in `staging/` at {fmt_defs(staging_defs)}.")
Path('"'/tmp/ref_audit_report_concise_sorted.md').write_text('\\n'.join(high + medium))
print('wrote /tmp/ref_audit_report_concise_sorted.md')
print(len(high), len(medium))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
wrote /tmp/ref_audit_report_concise_sorted.md
40 36
exec
/bin/zsh -lc "sed -n '1,20p' /tmp/ref_audit_report_concise_sorted.md && printf '\\n---\\n' && tail -20 /tmp/ref_audit_report_concise_sorted.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
[HIGH] chapters/theory/introduction.tex:2016 — `thm:ds-hpl-transfer` has no matching live `\label`.
[HIGH] chapters/frame/heisenberg_frame.tex:3467; chapters/frame/heisenberg_frame.tex:3537 — `sec:bar-complex-introduction` has no matching live `\label`.
[HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:1980 — `sec:complementarity` has no matching live `\label`.
[HIGH] chapters/theory/higher_genus_foundations.tex:4754 — `rem:feynman_genus_g` has no matching live `\label`.
[HIGH] chapters/theory/e1_modular_koszul.tex:694; chapters/theory/higher_genus_modular_koszul.tex:20508 — `sec:landscape-census` has no matching live `\label`.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:26890; chapters/connections/arithmetic_shadows.tex:2405 — `def:glcm-classification` has no matching live `\label`.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:31912; chapters/theory/higher_genus_modular_koszul.tex:31987; chapters/theory/higher_genus_modular_koszul.tex:32432 — `prop:ell-degree0` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8413.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32152 — `prop:ell-degree2` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8677.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32153 — `thm:ell-ordered-ch` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8876.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32173 — `sec:elliptic-ordered` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8294.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32323; chapters/theory/higher_genus_modular_koszul.tex:32561 — `eq:kzb-ell` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8366.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32367 — `eq:kzb-tau` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8597.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32471; chapters/theory/higher_genus_modular_koszul.tex:32496 — `eq:bar-degree1-yangian` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8486.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32857 — `subsec:ell-degree2` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8528.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32866 — `comp:sl2-kappa` has no matching live `\label`.
[HIGH] chapters/theory/higher_genus_modular_koszul.tex:32890 — `eq:ell-braid` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8763.
[HIGH] appendices/ordered_associative_chiral_kd.tex:5170; chapters/theory/ordered_associative_chiral_kd.tex:5481 — `thm:affine-half-space-bv` has no matching live `\label`.
[HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6047; chapters/theory/ordered_associative_chiral_kd.tex:6166; chapters/theory/ordered_associative_chiral_kd.tex:8107; chapters/theory/ordered_associative_chiral_kd.tex:8132; chapters/theory/ordered_associative_chiral_kd.tex:8168 — `ex:yangian` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:608.
[HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6048; chapters/theory/ordered_associative_chiral_kd.tex:6146; chapters/theory/ordered_associative_chiral_kd.tex:6159; chapters/connections/concordance.tex:7131; chapters/connections/concordance.tex:9746 — `conj:yangian-ordered-center` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1158.
[HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6167; chapters/theory/ordered_associative_chiral_kd.tex:8173 — `eq:yangian-ker-av2` is defined only in `staging/` at staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:917.


thinking
**Refining report details**

I’m considering whether to include "First 100 scan clean" and the summary along with 76 lines. I think it might be best to not rearrange the medium group logically but keep the original order. I could mention `main.log`, which has evidence of 163 warnings, 76 of which are unique. The user asked for a full report, and I need to include the lines about instances checked and violations found while keeping the report manageable.
thinking
**Organizing report structure**

I think I should note the first 101 occurrences and 163 log warnings. It’s good to clarify that the "first 100 scan clean" isn't counted as a violation. Mentioning that `grep -rn '\\ref{' chapters/ | head -100` produced 101 references is useful since there were two lines with multiple refs. I'm considering using a **Findings** header, but maybe it's optional. I could start the report with the summary of references and unique targets, then list the findings. It’s essential to keep the length reasonable, aiming for around 80 lines.
Plan update
Completed the first-100 `\ref` scan, rebuilt the current undefined-label set from `main.log`, mapped each unresolved target back to live source occurrences, and re-verified label presence against the live tree and aux surface.
  ✓ Parse the first 100 `\ref` occurrences and verify whether each target label exists anywhere in Vol I.
  ✓ Extract undefined labels from `main.log`, map each to source `\ref` locations, and check whether a matching `\label` exists.
  ✓ Re-verify surviving discrepancies and produce a severity-ordered findings report with exact file:line references.

thinking
**Reviewing findings for compression**

I’m thinking about whether to remove some of the long `thm:family-index` line, but the user asked for every finding, so I’ll keep it as is. The file has 76 items, and I confirmed that by counting the newlines. While I could compress findings with semicolons, I want to provide everything clearly. I’ll make sure the summary aligns with earlier notes and draft carefully without using clickable links to save space.
codex
First-100 scan: `grep -rn '\\ref{' chapters/ | head -100` produced 101 `\ref` occurrences (52 unique targets); all 52 have matching live `\label`s. All surviving failures below come from the current `main.log` undefined-reference surface (163 warning instances, 76 unique unresolved targets).

- [HIGH] chapters/theory/introduction.tex:2016 — `thm:ds-hpl-transfer` has no matching live `\label`.
- [HIGH] chapters/frame/heisenberg_frame.tex:3467; chapters/frame/heisenberg_frame.tex:3537 — `sec:bar-complex-introduction` has no matching live `\label`.
- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:1980 — `sec:complementarity` has no matching live `\label`.
- [HIGH] chapters/theory/higher_genus_foundations.tex:4754 — `rem:feynman_genus_g` has no matching live `\label`.
- [HIGH] chapters/theory/e1_modular_koszul.tex:694; chapters/theory/higher_genus_modular_koszul.tex:20508 — `sec:landscape-census` has no matching live `\label`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:26890; chapters/connections/arithmetic_shadows.tex:2405 — `def:glcm-classification` has no matching live `\label`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:31912; chapters/theory/higher_genus_modular_koszul.tex:31987; chapters/theory/higher_genus_modular_koszul.tex:32432 — `prop:ell-degree0` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8413`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32152 — `prop:ell-degree2` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8677`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32153 — `thm:ell-ordered-ch` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8876`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32173 — `sec:elliptic-ordered` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8294`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32323; chapters/theory/higher_genus_modular_koszul.tex:32561 — `eq:kzb-ell` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8366`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32367 — `eq:kzb-tau` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8597`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32471; chapters/theory/higher_genus_modular_koszul.tex:32496 — `eq:bar-degree1-yangian` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8486`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32857 — `subsec:ell-degree2` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8528`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32866 — `comp:sl2-kappa` has no matching live `\label`.
- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32890 — `eq:ell-braid` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8763`.
- [HIGH] appendices/ordered_associative_chiral_kd.tex:5170; chapters/theory/ordered_associative_chiral_kd.tex:5481 — `thm:affine-half-space-bv` has no matching live `\label`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6047; chapters/theory/ordered_associative_chiral_kd.tex:6166; chapters/theory/ordered_associative_chiral_kd.tex:8107; chapters/theory/ordered_associative_chiral_kd.tex:8132; chapters/theory/ordered_associative_chiral_kd.tex:8168 — `ex:yangian` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:608`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6048; chapters/theory/ordered_associative_chiral_kd.tex:6146; chapters/theory/ordered_associative_chiral_kd.tex:6159; chapters/connections/concordance.tex:7131; chapters/connections/concordance.tex:9746 — `conj:yangian-ordered-center` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1158`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:6167; chapters/theory/ordered_associative_chiral_kd.tex:8173 — `eq:yangian-ker-av2` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:917`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8106 — `eq:yangian-qybe` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:657`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8177 — `eq:sl2-kappa` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7558`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8198 — `eq:ek-s-locality` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3458`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8384 — `eq:yangian-drinfeld-coprod` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:754`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8385 — `ex:yangian-coproduct` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3205`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8577 — `def:chiral-coproduct` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2492`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8731 — `def:e1-chiral-rmatrix` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2402`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8732 — `eq:equiv-triangle` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2595`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:8738 — `eq:mk-from-ope` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2626`.
- [HIGH] chapters/theory/en_koszul_duality.tex:3584; chapters/theory/en_koszul_duality.tex:3789; chapters/theory/en_koszul_duality.tex:3799; chapters/theory/en_koszul_duality.tex:4598 — `prop:e3-structure` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:5263`.
- [HIGH] chapters/theory/en_koszul_duality.tex:3801 — `ex:km` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7541`.
- [HIGH] chapters/theory/en_koszul_duality.tex:4067 — `eq:kz-sl2-degree2` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7574`.
- [HIGH] chapters/theory/en_koszul_duality.tex:4201; chapters/theory/en_koszul_duality.tex:4266 — `ex:ek-qvoa` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3238`.
- [HIGH] chapters/theory/en_koszul_duality.tex:4245 — `eq:ek-vertex-rmatrix` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:3405`.
- [HIGH] chapters/theory/en_koszul_duality.tex:4537; chapters/theory/en_koszul_duality.tex:4821; chapters/theory/en_koszul_duality.tex:5258 — `warn:e1-vs-e2-source` is defined only in `staging/` at `staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1632`.
- [HIGH] chapters/connections/thqg_open_closed_realization.tex:662; chapters/connections/thqg_open_closed_realization.tex:707 — `def:oc-factorization-category` has no matching live `\label`.
- [HIGH] chapters/examples/y_algebras.tex:340 — `prop:heisenberg-kappa` has no matching live `\label`.
- [HIGH] chapters/examples/yangians_computations.tex:1150; chapters/examples/yangians_foundations.tex:1228 — `thm:rtt-all-types` has no matching live `\label`.
- [HIGH] chapters/connections/editorial_constitution.tex:1059; chapters/examples/yangians_computations.tex:2895; chapters/examples/yangians_computations.tex:3031; chapters/examples/yangians_computations.tex:3602; chapters/examples/yangians_computations.tex:3708; chapters/examples/yangians_drinfeld_kohno.tex:1010; chapters/examples/yangians_drinfeld_kohno.tex:1731; chapters/examples/yangians_drinfeld_kohno.tex:1759 — `thm:baxter-exact-triangles` has no matching live `\label`.
- [HIGH] chapters/connections/concordance.tex:1859; chapters/connections/editorial_constitution.tex:167; chapters/connections/editorial_constitution.tex:1061; chapters/examples/yangians_computations.tex:3550; chapters/examples/yangians_computations.tex:3592; chapters/examples/yangians_computations.tex:3720; chapters/examples/yangians_drinfeld_kohno.tex:1013; chapters/examples/yangians_drinfeld_kohno.tex:1717; chapters/examples/yangians_drinfeld_kohno.tex:1783; chapters/examples/yangians_drinfeld_kohno.tex:2186; chapters/examples/yangians_drinfeld_kohno.tex:2188 — `thm:pro-weyl-recovery` has no matching live `\label`.
- [MEDIUM] chapters/frame/preface.tex:3664 — `conv:three-hochschild` is undefined in `main.log`; live `\label` at chapters/connections/concordance.tex:100, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/introduction.tex:860; chapters/theory/introduction.tex:1119; chapters/theory/introduction.tex:2238; chapters/theory/introduction.tex:2439; chapters/examples/kac_moody.tex:4399; chapters/examples/kac_moody.tex:4439 — `ch:derived-langlands` is undefined in `main.log`; live `\label` at chapters/theory/derived_langlands.tex:6, but it never reaches the current aux surface.
- [MEDIUM] main.tex:1486; chapters/theory/introduction.tex:933; chapters/theory/introduction.tex:974; chapters/theory/introduction.tex:1684; chapters/theory/introduction.tex:2242; chapters/theory/introduction.tex:2450; chapters/frame/heisenberg_frame.tex:4802; chapters/connections/thqg_introduction_supplement_body.tex:1619; chapters/connections/thqg_introduction_supplement_body.tex:1752; chapters/connections/thqg_preface_supplement.tex:2017; chapters/connections/thqg_preface_supplement.tex:2054; chapters/examples/landscape_census.tex:4048 — `part:seven-faces` is undefined in `main.log`; live `\label` at main.tex:1450, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/cobar_construction.tex:2042; chapters/theory/introduction.tex:934; chapters/theory/introduction.tex:975; chapters/theory/introduction.tex:2244; chapters/theory/introduction.tex:2453 — `ch:holographic-datum-master` is undefined in `main.log`; live `\label` at chapters/connections/holographic_datum_master.tex:2, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/introduction.tex:1179; chapters/connections/subregular_hook_frontier.tex:966 — `comp:bp-kappa-three-paths` is undefined in `main.log`; live `\label` at chapters/connections/subregular_hook_frontier.tex:905, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/introduction.tex:1180; chapters/connections/subregular_hook_frontier.tex:1674 — `prop:nilpotent-transport-typeA` is undefined in `main.log`; live `\label` at chapters/connections/subregular_hook_frontier.tex:1519, but it never reaches the current aux surface.
- [MEDIUM] main.tex:1488; chapters/theory/introduction.tex:1941; chapters/theory/introduction.tex:2248; chapters/theory/introduction.tex:2468; chapters/connections/concordance.tex:3799 — `part:v1-frontier` is undefined in `main.log`; live `\label` at main.tex:1483, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/introduction.tex:2246; chapters/theory/introduction.tex:2462; chapters/connections/concordance.tex:6510 — `ch:genus1-seven-faces` is undefined in `main.log`; live `\label` at chapters/connections/genus1_seven_faces.tex:2, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/three_invariants.tex:234; chapters/connections/genus1_seven_faces.tex:1040; chapters/connections/holomorphic_topological.tex:43 — `ch:landscape-census` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:2, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/chiral_koszul_pairs.tex:1424; chapters/connections/arithmetic_shadows.tex:105; chapters/connections/arithmetic_shadows.tex:11156 — `thm:langlands-bar-bridge` is undefined in `main.log`; live `\label` at chapters/theory/derived_langlands.tex:95, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/higher_genus_foundations.tex:194; chapters/theory/higher_genus_foundations.tex:633; chapters/theory/higher_genus_foundations.tex:1074; chapters/theory/higher_genus_foundations.tex:5405; chapters/theory/higher_genus_foundations.tex:6388; chapters/theory/higher_genus_foundations.tex:6789; chapters/theory/higher_genus_foundations.tex:6827; chapters/theory/higher_genus_foundations.tex:6897; chapters/theory/higher_genus_modular_koszul.tex:2730; chapters/theory/higher_genus_modular_koszul.tex:2806; chapters/theory/higher_genus_modular_koszul.tex:2816; chapters/theory/higher_genus_modular_koszul.tex:4407; chapters/theory/higher_genus_modular_koszul.tex:4457; chapters/theory/higher_genus_modular_koszul.tex:9507; chapters/theory/higher_genus_modular_koszul.tex:13934; chapters/frame/heisenberg_frame.tex:1616; chapters/frame/heisenberg_frame.tex:1718; chapters/frame/heisenberg_frame.tex:4642; chapters/connections/concordance.tex:4712; chapters/connections/concordance.tex:6227; chapters/connections/bv_brst.tex:1502; chapters/connections/thqg_fredholm_partition_functions.tex:1449; chapters/connections/editorial_constitution.tex:2579; chapters/connections/editorial_constitution.tex:2668; chapters/examples/genus_expansions.tex:169; chapters/examples/genus_expansions.tex:1904; chapters/examples/heisenberg_eisenstein.tex:1738 — `thm:family-index` is undefined in `main.log`; live `\label` at chapters/connections/outlook.tex:660; chapters/connections/concordance.tex:5928, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:32123 — `prop:bar-verlinde-asymptotics` is undefined in `main.log`; live `\label` at chapters/examples/genus_expansions.tex:1987, but it never reaches the current aux surface.
- [MEDIUM] appendices/combinatorial_frontier.tex:226; appendices/combinatorial_frontier.tex:238; chapters/theory/derived_langlands.tex:1056; chapters/theory/higher_genus_modular_koszul.tex:33808; chapters/examples/landscape_census.tex:1843; chapters/examples/landscape_census.tex:1851; chapters/examples/landscape_census.tex:2016; chapters/examples/landscape_census.tex:2084; chapters/examples/landscape_census.tex:2101; chapters/examples/landscape_census.tex:2138; chapters/examples/landscape_census.tex:2163; chapters/examples/landscape_census.tex:2178; chapters/examples/landscape_census.tex:2483; chapters/examples/landscape_census.tex:2631; chapters/examples/landscape_census.tex:2819; chapters/examples/landscape_census.tex:2876; chapters/examples/kac_moody.tex:1060; chapters/examples/kac_moody.tex:1080 — `rem:garland-lepowsky-sl2` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:2035, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:33872 — `rem:rank-plus-one` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:2445, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/computational_methods.tex:1025; chapters/examples/landscape_census.tex:1627 — `tab:shadow-l-functions` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:1633, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/ordered_associative_chiral_kd.tex:9826; chapters/theory/ordered_associative_chiral_kd.tex:9848; chapters/theory/ordered_associative_chiral_kd.tex:9904; chapters/theory/ordered_associative_chiral_kd.tex:10013; chapters/theory/ordered_associative_chiral_kd.tex:10040; chapters/theory/coderived_models.tex:298; chapters/theory/coderived_models.tex:900; chapters/connections/concordance.tex:4940; chapters/connections/editorial_constitution.tex:1410 — `thm:off-koszul-ran-inversion` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:825, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/ordered_associative_chiral_kd.tex:10047; chapters/theory/coderived_models.tex:156; chapters/theory/coderived_models.tex:563; chapters/theory/coderived_models.tex:935 — `thm:conilpotent-reduction` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:125, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/chiral_center_theorem.tex:2516 — `rem:cdr-k3` is undefined in `main.log`; live `\label` at chapters/examples/toroidal_elliptic.tex:2080, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/chiral_center_theorem.tex:2551; chapters/theory/chiral_center_theorem.tex:2572 — `def:complementarity-asymmetry` is undefined in `main.log`; live `\label` at chapters/connections/thqg_critical_string_dichotomy.tex:964, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/thqg_fredholm_partition_functions.tex:777; chapters/connections/thqg_fredholm_partition_functions.tex:1152; chapters/connections/thqg_fredholm_partition_functions.tex:1714; chapters/examples/heisenberg_eisenstein.tex:2190 — `lem:thqg-X-composition-decay` is undefined in `main.log`; live `\label` at chapters/connections/thqg_fredholm_partition_functions.tex:447, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/thqg_fredholm_partition_functions.tex:864; chapters/connections/thqg_fredholm_partition_functions.tex:904; chapters/connections/thqg_fredholm_partition_functions.tex:1195; chapters/examples/heisenberg_eisenstein.tex:2414 — `eq:thqg-X-polyakov` is undefined in `main.log`; live `\label` at chapters/connections/thqg_fredholm_partition_functions.tex:822, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/heisenberg_eisenstein.tex:2420 — `rem:thqg-X-pants-independence` is undefined in `main.log`; live `\label` at chapters/connections/thqg_fredholm_partition_functions.tex:408, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/kac_moody.tex:764 — `tab:rmatrix-census` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:397, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/derived_langlands.tex:42; chapters/theory/derived_langlands.tex:720; chapters/theory/derived_langlands.tex:861; chapters/theory/derived_langlands.tex:890; chapters/theory/derived_langlands.tex:918; chapters/theory/derived_langlands.tex:1344; chapters/theory/derived_langlands.tex:1365; chapters/theory/derived_langlands.tex:1560; chapters/examples/kac_moody.tex:4372 — `thm:oper-bar-dl` is undefined in `main.log`; live `\label` at chapters/theory/derived_langlands.tex:648, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/landscape_census.tex:286; chapters/examples/bar_complex_tables.tex:2257; chapters/examples/bar_complex_tables.tex:2578; chapters/examples/kac_moody.tex:4507; chapters/examples/kac_moody.tex:5588 — `sec:B2-details` is undefined in `main.log`; live `\label` at chapters/examples/bar_complex_tables.tex:1207, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/landscape_census.tex:286; chapters/examples/kac_moody.tex:4507; chapters/examples/kac_moody.tex:5588 — `sec:G2-details` is undefined in `main.log`; live `\label` at chapters/examples/bar_complex_tables.tex:2253, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/y_algebras.tex:630 — `subsec:concordance-e1-primacy` is undefined in `main.log`; live `\label` at chapters/connections/concordance.tex:3752, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/w3_holographic_datum.tex:215 — `cor:anomaly-ratio-ds` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:1238, but it never reaches the current aux surface.
- [MEDIUM] chapters/examples/landscape_census.tex:506; chapters/examples/w3_holographic_datum.tex:387 — `rem:ww-even-poles-census` is undefined in `main.log`; live `\label` at chapters/examples/landscape_census.tex:568, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/thqg_gravitational_yangian.tex:1033; chapters/connections/thqg_gravitational_yangian.tex:1474; chapters/connections/thqg_gravitational_yangian.tex:2005; chapters/connections/thqg_gravitational_yangian.tex:2242; chapters/examples/yangians_drinfeld_kohno.tex:8056; chapters/examples/yangians_drinfeld_kohno.tex:8099 — `thm:thqg-V-collision-twisting` is undefined in `main.log`; live `\label` at chapters/connections/thqg_gravitational_yangian.tex:579, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/bv_brst.tex:1546 — `cor:thqg-I-heisenberg-selberg` is undefined in `main.log`; live `\label` at chapters/connections/thqg_perturbative_finiteness.tex:1997, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/concordance.tex:4929; chapters/connections/bv_brst.tex:1878; chapters/connections/bv_brst.tex:1964; chapters/connections/bv_brst.tex:2030 — `def:coacyclic-fact` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:518, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/coderived_models.tex:239; chapters/theory/coderived_models.tex:267; chapters/theory/coderived_models.tex:674; chapters/connections/bv_brst.tex:1878; chapters/connections/bv_brst.tex:1907; chapters/connections/bv_brst.tex:1931; chapters/connections/bv_brst.tex:1965 — `def:curved-weak-equiv` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:214, but it never reaches the current aux surface.
- [MEDIUM] chapters/theory/coderived_models.tex:292; chapters/connections/concordance.tex:4935; chapters/connections/bv_brst.tex:1936; chapters/connections/editorial_constitution.tex:1404 — `prop:provisional-embedding` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:654, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/bv_brst.tex:2030 — `def:coderived-fact` is undefined in `main.log`; live `\label` at chapters/theory/coderived_models.tex:546, but it never reaches the current aux surface.
- [MEDIUM] chapters/connections/arithmetic_shadows.tex:2883; chapters/connections/concordance.tex:2251; chapters/connections/concordance.tex:6529; chapters/connections/frontier_modular_holography_platonic.tex:1656 — `thm:yangian-shadow-theorem` is undefined in `main.log`; live `\label` at chapters/connections/frontier_modular_holography_platonic.tex:1400, but it never reaches the current aux surface.

## Summary
Instances checked: 264 | Violations found: 76 | Verdict: FAIL
tokens used
149,073
