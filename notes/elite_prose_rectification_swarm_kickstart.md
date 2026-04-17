# Elite-Prose Rectification Swarm -- Kickstart

Mission: line-by-line elite-prose rectification of the entire three-volume series.

LOSSLESS for mathematics. Aggressive for prose. Single pass; ten parallel agents; full corpus coverage.

## Standard

Russian school + mathematical-physicists. Polyakov-Gelfand-Drinfeld-Kazhdan-Etingof-Beilinson-Bezrukavnikov-Kapranov + Witten-Costello-Gaiotto-Dirac. Simple. Direct. Elegant. Inevitability: every sentence forces the next.

---

## A. Banned tokens (HZ-10 + extensions)

Grep all and contextually rewrite. The word does not survive unless it carries technical content unavailable elsewhere.

### A.1 AI slop / connective filler
moreover, additionally, notably, crucially, remarkably, interestingly, furthermore, indeed, in fact, of course, naturally, certainly, surely, presumably, arguably, seemingly, apparently, basically, essentially (as filler), fundamentally (as filler), just (as filler), simply (as filler), really, very, quite, rather, fairly, somewhat, slightly, kind of, sort of.

### A.2 Stalling phrases
"in some sense", "more or less", "as it were", "so to speak", "if you will", "as we shall see", "as we will see", "in what follows", "as discussed", "as mentioned", "above-mentioned", "aforementioned", "the present work", "this work", "in this paper", "we now turn to", "we now present", "we now describe", "we now discuss", "we begin by", "we conclude by", "we end with", "to summarise", "to sum up", "to wrap up", "to be precise", "more precisely", "strictly speaking", "loosely speaking".

### A.3 Conversational AI tells
"wait", "actually" (as conversational hedge), "that's not quite right", "this is incorrect", "let us now", "we shall now", "let me", "let's", "now we", "next we", "first we", "second we", "third we", "finally we".

### A.4 Throat-clearing
"it is worth noting", "worth mentioning", "it should be noted", "it is important to note", "note that" (as filler), "observe that" (as filler), "we see that" (as filler), "one can see that".

### A.5 Generic-AI prose tics
delve, leverage, tapestry, cornerstone, journey, navigate (non-geometric).

### A.6 Transition tics
"in particular" (as transition), "specifically" (as transition), "more specifically" (as filler), "namely" (when not introducing a name), "hence" + "therefore" + "thus" stacked redundantly.

---

## B. Banned constructions

### B.1 Em dashes
ASCII `---`, en-dash `–`, U+2014 `—`. Replace with hyphen / parens / colon / semicolon / sentence split. Match the semantic weight of the original pause.

### B.2 The "not X but Y" pattern
"X is not Y but Z" -> "X is Z" (drop the negation; if Y was a previously-asserted claim, write "X is Z, not Y" only if the contrast is mathematically informative).
"Not just X but Y" -> "X and Y" or restructure.

### B.3 Pseudo-modesty
"It is well-known that X" -> cite or assert directly.
"It can be shown that X" -> "X (proof: ...)" or cite.
"One can see that X" -> "X."
"It follows from X that Y" -> "By X, Y" or "X gives Y" (with explicit arrow).
"Note that / Observe that / We see that X" -> "X."

### B.4 Hedging in mathematics
arguably, perhaps, presumably, possibly, seems to, appears to, suggests (in math contexts). Strike or replace with `\ClaimStatusConjectured` if the claim is genuinely open.

### B.5 Formulaic enumeration
"First we ..., second we ..., third we ..., finally we ..." -> restructure to direct claims (state the claims; itemize only when listing parallel objects).

### B.6 Narrative scaffolding
"Now that we have established X, we turn to Y" -> "Y. (X is given above.)"
"Having proved X, we will now use it to prove Y" -> "X yields Y as follows."

### B.7 Faux-symmetry
"Conversely, Y implies X" when only the forward direction is proved -> state the forward direction and mark the converse.

### B.8 Throat-clearing openers
"This chapter will ..." / "In this section we ..." / "We begin with ..." -> cut. Open with the result.

---

## C. Elite English standard

State the result. Defer narration to remarks. Each sentence carries its weight.

### C.1 Russian school
Polyakov-Gelfand-Drinfeld-Kazhdan-Etingof-Beilinson-Bezrukavnikov-Kapranov standard: one form, one relation, one object. Economy. Each definition is a tool that already does its job.

### C.2 Mathematical physicists
Witten-Costello-Gaiotto-Dirac-Polyakov standard: physical insight precedes proof. The OPE is the bar differential. Construction is computation.

### C.3 Inevitability (Gelfand)
Every sentence forces the next. The reader cannot diverge.

### C.4 Compression (Kazhdan)
Say it once. Say it right.

### C.5 Falsification (Beilinson)
Every claim false until verified. Status tags everywhere. Conjectures named. Open frontiers honest.

### C.6 Higher structure IS the math (Kapranov)
A_infinity is not a correction. It is the structure.

### C.7 Factorisation as organisational principle (Costello)
The atomic objects organise themselves through factorisation.

### C.8 Dualities compute (Gaiotto)
Specialise, compute, recover.

---

## D. Mathematics fortification

For each weak segment apply first-principles. Strengthen, do not just rewrite.

### D.1 Hedged-but-solid claim
State directly with explicit scope. Drop "perhaps", "arguably", "we suspect"; replace with `\ClaimStatusProvedHere` and the proof.

### D.2 Overscoped claim
Scope sharply. Add the explicit hypotheses; state the locus on which the claim holds.

### D.3 Sketchy proof
Either complete it (if straightforward at this level) or defer to a citation with explicit axioms named.

### D.4 Informal definition
Move to formal definition in body; intuition into a `Remark`.

### D.5 Mentioned but not constructed
Construct it explicitly. "X gives Y" requires the explicit arrow.

### D.6 Meandering exposition
Cut to the precise theorem statement. Defer narrative to a `Remark`.

### D.7 Mid-sentence convention drift
Grep for two-convention clashes (two `hbar`, two r-matrix forms, two kappa subscripts) without explicit bridge identity. AP151 / HZ-1 / HZ-4.

---

## E. First-principles protocol (mandatory per violation)

Step 1 -- INVESTIGATE
For each issue answer all three:
(a) What does the claim get RIGHT (the ghost theorem)?
(b) What does it get WRONG (the precise conflation)?
(c) What is the CORRECT mathematical relationship?

Step 2 -- FIX WITH SUBSTANCE
Every correction must contain actual mathematics. A remark, a factorisation, an adjunction, a construction. NO shallow term swaps.

Step 3 -- WRITE TO CACHE
If a confusion pattern is new, or appears 2+ times, append to:
  `/Users/raeez/chiral-bar-cobar/appendices/first_principles_cache.md`
Format: `| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |`

---

## F. Top-15 cached confusions (check ALL claims)

1. specific/general: toric result applied to all CY (S_N vanishing, Omega-bg, kappa = c/2).
2. label/content: bare kappa (AP113), bare 'ordered' (AP152), bare 'Hochschild' (AP160).
3. native/derived: at d >= 3, A is E_1; E_2 lives on Z(Rep(A)) only.
4. construction/narration: 'X gives Y' needs explicit arrow (AP-CY57).
5. algebra/coalgebra: CoHA != bar complex.
6. CoHA != chiral: CoHA is associative, not a vertex algebra (AP-CY7).
7. Drinfeld center != averaging: center is right adjoint to forgetful (AP-CY54).
8. scope: CY-B d-dependent (AP-CY58); Phi output d-dependent (FM43).
9. AP-CY8: denominator = bar Euler needs BOTH CY-A AND Vol I anchor.
10. CY-C CONJECTURAL; G(X) unconstructed; super-Yangian conjectural.
11. convention: two `hbar` without bridge = disaster (AP151).
12. mechanism: N_{C/Y} -> spectral params needs Omega intermediary (AP-CY20).
13. chain/cohom: class M E_3 bar = 6^g (cohomological), NOT infinite.
14. part/whole: `{b_k, B^{(2)}} = 0` per-k FALSE; only total vanishes.
15. coincidence: `kappa_BKM = kappa_ch + chi(O_fiber)` is N=1 K3 x E COINCIDENCE; FAILS at N >= 2.

Key facts:
- `kappa_cat(K3 x E) = 0` (total space), NOT 2 (fiber).
- `CoHA(C^3) = Y^+` (positive half), NOT W_{1+infty} (full Yangian).
- Six routes to G(K3 x E) are six DIFFERENT constructions WITNESSING same `Phi_3`-output.
- `Phi` gives ONE output per category. Different `kappa`s come from DIFFERENT constructions.

---

## G. Lossless invariant

PRESERVE every label, theorem environment, proof, citation, formula, ClaimStatus tag, cross-volume reference.

Restating, rearrangement, repackaging is allowed.

Mathematical content removal is FORBIDDEN. If displaced, insert a `\ref{}` to the chapter that retains it.

Wave-14 anchor cross-references in particular must be preserved:
- Vol I: `chap:climax-platonic`, `chap:universal-conductor`, `chap:shadow-quadrichotomy-platonic`, `thm:koszul-reflection`, `chap:mc5-g0g1-wall-platonic`, `app:q-convention-bridge`.
- Vol II: `thm:universal-holography-master`, `cor:rung-{heisenberg, affine-km, virasoro, w-N, w-infty}`, `conj:universal-trace-identity-volii-bridge`, `ch:programme-climax-platonic`, `thm:chd-ds-hochschild`, `thm:curved-dunn-H2-vanishing-all-genera`, `thm:iterated-sugawara-construction`, `thm:e-infinity-topologization-ladder`.
- Vol III: `chap:cy-to-chiral` (or `thm:cy-to-chiral`, `thm:cy-to-chiral-d3`), `thm:kappa-stratification-by-d`, `prop:bkm-weight-universal`, `rem:bkm-decomposition-adversarial`.

---

## H. Bundle assignments (10 agents, all background)

Each agent processes ONE bundle. Read every line of every file. Apply A-G. Report at the end.

### E1 -- Vol I frame + overture

REPO: `/Users/raeez/chiral-bar-cobar`

Files:
- `chapters/frame/preface.tex`
- `chapters/theory/introduction.tex`
- `main.tex` (abstract section)
- `chapters/frame/heisenberg_frame.tex`
- `chapters/frame/fourier_seed.tex` (if present)

### E2 -- Vol I wave-14 anchors + bar/cobar foundational

REPO: `/Users/raeez/chiral-bar-cobar`

Files:
- `chapters/theory/chiral_climax_platonic.tex`
- `chapters/theory/universal_conductor_K_platonic.tex`
- `chapters/theory/shadow_tower_quadrichotomy_platonic.tex`
- `chapters/theory/theorem_A_infinity_2.tex`
- `chapters/theory/algebraic_foundations.tex`
- `chapters/theory/configuration_spaces.tex`
- `chapters/theory/three_invariants.tex`
- `chapters/theory/bar_construction.tex`
- `chapters/theory/cobar_construction.tex`
- `chapters/theory/bar_cobar_adjunction.tex` (and `_curved.tex`, `_inversion.tex` variants)
- `chapters/theory/mc5_class_m_chain_level_platonic.tex`
- `chapters/theory/mc5_genus0_genus1_wall_platonic.tex`

### E3 -- Vol I higher-genus + Koszul programme

REPO: `/Users/raeez/chiral-bar-cobar`

Files:
- `chapters/theory/higher_genus.tex` (if present)
- `chapters/theory/higher_genus_foundations.tex`
- `chapters/theory/higher_genus_complementarity.tex`
- `chapters/theory/higher_genus_modular_koszul.tex`
- `chapters/theory/clutching_uniqueness_platonic.tex`
- `chapters/theory/conformal_anomaly_rigidity_platonic.tex`
- `chapters/theory/chern_weil_level_shift_platonic.tex`
- `chapters/theory/chiral_koszul_pairs.tex`
- `chapters/theory/koszul_pair_structure.tex`
- `chapters/theory/koszulness_moduli_scheme.tex`
- `chapters/theory/chiral_hochschild_koszul.tex`
- `chapters/theory/poincare_duality.tex`
- `chapters/theory/poincare_duality_quantum.tex`
- `chapters/theory/quantum_corrections.tex`
- `chapters/theory/filtered_curved.tex`
- `chapters/theory/hochschild_cohomology.tex`

### E4 -- Vol I E_1/E_n + characteristic datum + shadow tower

REPO: `/Users/raeez/chiral-bar-cobar`

Files:
- `chapters/theory/e1_modular_koszul.tex`
- `chapters/theory/ordered_associative_chiral_kd.tex`
- `chapters/theory/en_koszul_duality.tex`
- `chapters/theory/topologization_chain_level_platonic.tex`
- `chapters/theory/e3_identification_chain_level_platonic.tex`
- `chapters/theory/genus_2_ddybe_platonic.tex`
- `chapters/theory/computational_methods.tex`
- `chapters/theory/shadow_tower_higher_coefficients.tex`
- `chapters/theory/shadow_tower_sub_subleading_platonic.tex`
- `chapters/theory/shadow_tower_other_class_M_platonic.tex`
- All `chapters/theory/motivic_shadow_*.tex`
- `chapters/theory/shadow_L_function_platonic.tex`
- `chapters/theory/z_g_kummer_bernoulli_platonic.tex`
- `chapters/theory/higher_kummer_arithmetic_duality_platonic.tex`
- `chapters/theory/all_tier_generating_function_platonic.tex`
- `chapters/theory/virasoro_motivic_purity_all_r_platonic.tex`
- `chapters/theory/periodic_cdg_admissible.tex`
- `chapters/theory/ftm_seven_fold_tfae_platonic.tex`
- `chapters/theory/mc3_five_family_platonic.tex`

### E5 -- Vol I Standard Landscape + Connections + Appendices

REPO: `/Users/raeez/chiral-bar-cobar`

Files (examples):
- `chapters/examples/heisenberg_eisenstein.tex`
- `chapters/examples/kac_moody.tex`
- `chapters/examples/w_algebras.tex`
- `chapters/examples/w3_composite_fields.tex`
- `chapters/examples/minimal_model_fusion.tex`
- `chapters/examples/minimal_model_examples.tex`
- `chapters/examples/w_algebras_deep.tex`
- `chapters/examples/w3_holographic_datum.tex`
- `chapters/examples/beta_gamma.tex`
- `chapters/examples/free_fields.tex`
- `chapters/examples/lattice_foundations.tex`
- `chapters/examples/lattice_vertex_algebras.tex` (if present)
- `chapters/examples/n2_superconformal.tex`
- `chapters/examples/bershadsky_polyakov.tex`
- `chapters/examples/yangians_foundations.tex`
- `chapters/examples/yangians_computations.tex`
- `chapters/examples/yangians_drinfeld_kohno.tex`
- `chapters/examples/moonshine.tex`
- `chapters/examples/level1_bridge.tex`
- `chapters/examples/landscape_census.tex`

Files (connections):
- `chapters/connections/feynman_diagrams.tex`
- `chapters/connections/feynman_connection.tex`
- `chapters/connections/bv_brst.tex`
- `chapters/connections/holographic_datum_master.tex`
- `chapters/connections/genus1_seven_faces.tex`
- `chapters/connections/holomorphic_topological.tex` (Vol I)
- `chapters/connections/kontsevich_integral.tex` (if present)
- `chapters/connections/physical_origins.tex` (if present)
- `chapters/connections/arithmetic_shadows.tex`
- `chapters/theory/derived_langlands.tex`
- `chapters/theory/thqg_open_closed_realization.tex`

Appendices:
- `appendices/q_convention_bridge_appendix.tex`
- DO NOT touch `appendices/first_principles_cache.md` (this is the cache target).

### E6 -- Vol II frame + Part I (open primitive)

REPO: `/Users/raeez/chiral-bar-cobar-vol2`

Files:
- `chapters/frame/preface.tex`
- `chapters/theory/introduction.tex`
- `main.tex` (abstract section)
- `chapters/theory/foundations.tex`
- `chapters/theory/locality.tex`
- `chapters/theory/axioms.tex`
- `chapters/theory/equivalence.tex`
- `chapters/theory/factorization_swiss_cheese.tex`
- `chapters/theory/raviolo.tex`
- `chapters/theory/raviolo-restriction.tex`
- `chapters/theory/fm_calculus.tex` (if present)
- `chapters/theory/orientations.tex` (if present)
- `chapters/theory/fm_proofs.tex` (if present)
- `chapters/theory/bv-construction.tex`
- `chapters/theory/pva-descent-repaired.tex`
- `chapters/theory/pva-expanded-repaired.tex`
- `chapters/theory/sc_chtop_heptagon.tex`

### E7 -- Vol II Part II + III + IV (E_1 core, GRT torsor, characteristic datum + modularity)

REPO: `/Users/raeez/chiral-bar-cobar-vol2`

Files (theory):
- `chapters/theory/bar_cobar_review.tex`
- `chapters/theory/line_operators.tex`
- `chapters/theory/ordered_associative_chiral_kd_core.tex`
- `chapters/theory/dg_shifted_factorization_bridge.tex`
- `chapters/theory/gravitational_yangian.tex`
- `chapters/theory/typeA_baxter_rees_theta.tex`
- `chapters/theory/shifted_rtt_orthogonal_coideals.tex` (or `shifted_rtt_duality_orthogonal_coideals.tex`)
- `chapters/theory/casimir_divisor_transport.tex`
- `chapters/theory/unified_chiral_quantum_group.tex`
- `chapters/theory/super_chiral_yangian.tex`
- `chapters/theory/modular_swiss_cheese_operad.tex`
- `chapters/theory/beta_N_closed_form_all_platonic.tex`
- `chapters/theory/wn_tempered_closure_platonic.tex`
- `chapters/theory/irrational_cosets_tempered_platonic.tex`
- `chapters/theory/logarithmic_wp_tempered_analysis_platonic.tex`
- `chapters/theory/tempered_stratum_characterization_platonic.tex`
- `chapters/theory/bp_chain_level_strict_platonic.tex`
- `chapters/theory/curved_dunn_higher_genus.tex`
- `chapters/theory/chiral_higher_deligne.tex`

Files (connections):
- `chapters/connections/dnp_identification_master.tex`
- `chapters/connections/grt_parametrized_seven_faces.tex`
- `chapters/connections/spectral_braiding_core.tex`
- `chapters/connections/ht_bulk_boundary_line_core.tex`
- `chapters/connections/celestial_boundary_transfer_core.tex`
- `chapters/connections/hochschild.tex`
- `chapters/connections/brace.tex`
- `chapters/connections/relative_feynman_transform.tex`
- `chapters/connections/modular_pva_quantization_core.tex`
- `chapters/connections/modular_pva_quantization.tex`
- `chapters/connections/modular_pva_quantization_frontier.tex`
- `chapters/connections/fm81_fractional_ghost_platonic.tex`

### E8 -- Vol II Part V + VI + VII + VIII (HT landscape, climax, frontier)

REPO: `/Users/raeez/chiral-bar-cobar-vol2`

Files:
- `chapters/theory/ht_physical_origins.tex` (if present)
- `chapters/connections/ym_boundary_theory.tex`
- `chapters/connections/ym_higher_body_couplings.tex`
- `chapters/connections/ym_instanton_screening.tex`
- `chapters/connections/celestial_holography_core.tex`
- `chapters/connections/log_ht_monodromy.tex`
- `chapters/connections/anomaly_completed.tex`
- `chapters/connections/holomorphic_topological.tex` (Vol II)
- `chapters/connections/holographic_reconstruction.tex`
- `chapters/connections/modular_bootstrap.tex`
- `chapters/connections/programme_climax_platonic.tex`
- `chapters/connections/e_infinity_topologization.tex`
- `chapters/connections/3d_gravity*.tex`
- `chapters/connections/critical_string_dichotomy.tex` (if present)
- `chapters/connections/perturbative_finiteness.tex` (if present)
- `chapters/connections/soft_graviton_theorems.tex` (if present)
- `chapters/connections/symplectic_polarization.tex` (if present)
- `chapters/connections/universal_holography_functor.tex`
- `chapters/connections/universal_celestial_holography.tex`
- `chapters/connections/celestial_moonshine_bridge.tex` (if present)
- `chapters/connections/soft_graviton_mellin_shadow.tex` (if present)
- `chapters/connections/monster_chain_level_e3_top_platonic.tex`
- `chapters/connections/schellekens_71_alpha_classification_platonic.tex`
- `chapters/theory/koszulness_moduli_M_kosz.tex`
- `chapters/theory/infinite_fingerprint_classification.tex`
- `chapters/connections/ordered_associative_chiral_kd_frontier.tex`
- `chapters/examples/w-algebras-frontier.tex` (if present)
- All other Part VII frontier chapters via `Glob` of `*frontier*.tex`.

### E9 -- Vol III frame + theory + examples (first batch)

REPO: `/Users/raeez/calabi-yau-quantum-groups`

Files:
- `chapters/frame/preface.tex`
- `chapters/theory/introduction.tex`
- `main.tex` (abstract section)
- `chapters/theory/cy_categories.tex`
- `chapters/theory/cyclic_ainf.tex`
- `chapters/theory/hochschild_calculus.tex`
- `chapters/theory/e1_chiral_algebras.tex`
- `chapters/theory/e2_chiral_algebras.tex`
- `chapters/theory/en_factorization.tex`
- `chapters/theory/drinfeld_center.tex`
- `chapters/theory/braided_factorization.tex`
- `chapters/theory/modular_trace.tex`
- `chapters/theory/quantum_chiral_algebras.tex`
- `chapters/theory/m3_b2_saga.tex`
- `chapters/theory/cy_to_chiral.tex`
- `chapters/theory/quantum_groups_foundations.tex`
- `chapters/examples/k3_chiral_algebra.tex`
- `chapters/examples/k3_yangian_chapter.tex`
- `chapters/examples/k3_quantum_toroidal_chapter.tex`

### E10 -- Vol III examples (second batch) + connections + frontier

REPO: `/Users/raeez/calabi-yau-quantum-groups`

Files:
- `chapters/examples/cy_d_kappa_stratification.tex`
- `chapters/examples/toric_cy3_coha.tex`
- `chapters/examples/toroidal_elliptic.tex`
- `chapters/examples/derived_categories_cy.tex`
- `chapters/examples/fukaya_categories.tex`
- `chapters/examples/matrix_factorizations.tex`
- `chapters/examples/quantum_group_reps.tex`
- `chapters/examples/super_riccati_shadow_tower_platonic.tex`
- `chapters/examples/k3e_cy3_programme.tex`
- `chapters/examples/cy_c_six_routes_convergence.tex`
- `chapters/examples/cy_c_six_routes_generator_level_platonic.tex` (if present)
- `chapters/examples/coha_wall_crossing.tex`
- `chapters/connections/bar_cobar_bridge.tex`
- `chapters/connections/cy_holographic_datum_master.tex`
- `chapters/connections/modular_koszul_bridge.tex`
- `chapters/connections/geometric_langlands.tex`

---

## I. Per-agent prompt template

Use the following template per agent. Replace `{{BUNDLE_NAME}}`, `{{REPO}}`, and `{{FILES}}` with the bundle data above. Launch in background (`run_in_background: true`).

```
{{BUNDLE_NAME}}: line-by-line elite-prose rectification.

LOSSLESS for mathematics. Aggressive for prose. Single pass.

REPO: {{REPO}}
BUNDLE: {{FILES}}

CONTEXT:
- /Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/platonic_ideal_reconstituted_2026_04_17.md
- /Users/raeez/chiral-bar-cobar/CLAUDE.md (HZ-1..HZ-10; AP catalog)
- /Users/raeez/chiral-bar-cobar/notes/elite_prose_rectification_swarm_kickstart.md (THIS DOC)

PROTOCOL:
For each file in BUNDLE:
1. Read the file in full.
2. Grep banned tokens (Section A) and banned constructions (Section B) of the kickstart doc; for each hit READ surrounding 2-3 lines and CONTEXTUALLY rewrite to the elite-grade form.
3. Identify weak segments (hedged-but-solid claims, overscoped claims, sketchy proofs, informal definitions, mentioned-but-not-constructed objects, meandering exposition); apply Section D fortification.
4. For each violation, apply the Section E first-principles protocol:
   (a) ghost theorem
   (b) precise error
   (c) correct relationship
   then fix with substance.
5. If a confusion pattern is new or appears 2+ times, append entry to /Users/raeez/chiral-bar-cobar/appendices/first_principles_cache.md per the format in Section E.

LOSSLESS INVARIANT (Section G): PRESERVE every label, theorem environment, proof, citation, formula, ClaimStatus tag, cross-volume reference. PRESERVE wave-14 anchors. Mathematical content removal FORBIDDEN.

DISCIPLINE GUARDS (top-15 cached confusions, Section F):
- Apply HZ3-2 zero-bare-kappa for Vol III files.
- Apply HZ-1 r-matrix level prefix for any r-matrix.
- Apply HZ-3 scope tags for any obs_g / F_g / lambda_g.
- Apply HZ-4 family-qualified kappa for Vol I/II.
- Cached confusion #15 (kappa_BKM scope): K3-fibered Class A only.
- Cached confusion #4 (construction-not-narration): explicit arrow for every "X gives Y".
- Cached confusion #3 (native vs derived): at d>=3, A is E_1; E_2 on Z(Rep(A)) only.
- Cached confusion #10 (CY-C conjectural): never claim G(X) constructed.

PROHIBITIONS:
- NO commit (no git add, no git commit).
- NO build (no make, no pdflatex).
- NO touch of /Users/raeez/chiral-bar-cobar/appendices/first_principles_cache.md as content (only append entries).
- NO touch of files outside BUNDLE.
- NO removal of mathematical content.

REPORT (under 300 words):
- Files processed (count + per-file line count change).
- Banned tokens replaced (per-category counts: AI slop / stalling phrases / conversational tells / throat-clearing / generic-AI tics / transition tics).
- Banned constructions fixed (per-construction counts: em dashes / not-X-but-Y / pseudo-modesty / hedging / formulaic enumeration / narrative scaffolding / faux-symmetry / throat-clearing openers).
- Weak-segment rewrites with mathematical fortification (count + 2-3 representative before/after pairs).
- New cached confusions appended (count + entry summary).
- Any segments left FLAGGED for follow-up (count + reason).
- Cross-volume references preserved (Y/N).
```

---

## J. Launch instructions

On the target machine, launch all 10 agents in parallel in background. Recommended cap: 10 concurrent.

The task tool invocation per agent:
```
Agent({
  description: "{{short E1-E10 description}}",
  subagent_type: "general-purpose",
  run_in_background: true,
  prompt: "<the canonical template above with {{BUNDLE_NAME}} and {{FILES}} filled in>"
})
```

Wait for all 10 to complete (notifications will arrive asynchronously). After all 10 return, run:
1. Build all three volumes:
   - Vol I: `cd /Users/raeez/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast`
   - Vol II: `cd /Users/raeez/chiral-bar-cobar-vol2 && make`
   - Vol III: `cd /Users/raeez/calabi-yau-quantum-groups && make fast`
2. Tests: `make test` in each repo.
3. Grep verification across all three repos:
   - `---` ASCII em-dashes (target: 0 outside verbatim/comment blocks).
   - `\\bmoreover\\b|\\badditionally\\b|\\bnotably\\b|\\bcrucially\\b|\\bremarkably\\b|\\binterestingly\\b|\\bfurthermore\\b|\\bof\\s+course\\b|\\bdelve\\b|\\bleverage\\b|\\btapestry\\b|\\bcornerstone\\b` (target: 0 in body text).
   - Bare `\\kappa[^_a-zA-Z\\^\\{(\\)]` in Vol III (target: 0).

Estimated wall-clock per agent: 8-15 minutes depending on bundle size. Total estimated session: 15-20 minutes if all 10 run concurrently without rate limits.

---

## K. Acceptance criteria

The pass is complete when:
- All ten bundles report.
- Build all three volumes succeeds.
- Em-dash grep returns 0 outside verbatim/comment blocks.
- Banned-token grep returns 0 in body text.
- Vol III bare-kappa grep returns 0.
- No mathematical content has been removed.
- All wave-14 cross-references resolve.
- The first-principles cache has been updated with any newly-discovered confusion patterns.
