# Kickstart Prompt — Relaunch 100+ Agent Swarm

## How to Use

Copy the text between === markers as your first message in a fresh Claude Code session.

## ===BEGIN PROMPT===

Read compute/audit/session_state_2026_04_01_final.md for the complete state. That file has everything: 20 manuscript fixes, 2506+ new tests across 25 compute modules, 30+ new quantities computed for 20+ algebras, 10 key mathematical discoveries.

The previous session's 25 compute agents ALL completed successfully. The 101-agent adversarial swarm produced 8 agents with full results and ~60 that hit rate limits before finishing. The mathematical fixes are applied. The compute layer is comprehensive.

**What remains and needs 100+ agents:**

TIER 1 — MANUSCRIPT INTEGRATION (20 agents):
Launch agents to integrate ALL computed quantities into the manuscript LaTeX. Each agent takes one compute module's results and writes them into the corresponding .tex chapter:
1. Virasoro S₅-S₁₀ → landscape_census.tex + w_algebras.tex (table + formulas)
2. W₃ shadow S₃-S₈ → w_algebras_deep.tex (T-line and W-line tables)
3. F₁/F₂/F₃ for 15 families → genus_expansions.tex (master genus table)
4. F₂(W₃) = (c+120)/(16c) cross-channel → w_algebras_deep.tex + genus_expansions.tex (NEW RESULT)
5. r-matrices for 8 families → landscape_census.tex (r-matrix column in master table)
6. Discriminant atlas → higher_genus_modular_koszul.tex (discriminant table)
7. Shadow radius landscape → higher_genus_modular_koszul.tex (convergence table)
8. Depth classification 20 algebras → landscape_census.tex (depth column)
9. DS cascade N=2..6 → w_algebras_deep.tex (DS section)
10. Shadow connection → higher_genus_modular_koszul.tex (connection section)
11. Non-simply-laced B₂/C₂/G₂/F₄ → kac_moody.tex (non-simply-laced section)
12. Exceptional E₆/E₇/E₈ → kac_moody.tex (exceptional section)
13. W₄/W₅ shadows → w_algebras_deep.tex (higher W section)
14. βγ full tower → free_fields.tex (βγ section)
15. Complementarity landscape → higher_genus_complementarity.tex (complementarity table)
16. Koszulness 15 algebras → chiral_koszul_pairs.tex (Koszulness table)
17. Propagator variance 6 families → higher_genus_modular_koszul.tex (variance section)
18. Ghost constant k-dependent → w_algebras_deep.tex (already partially done, verify)
19. Genus-2 planted-forest → higher_genus_modular_koszul.tex (planted-forest section)
20. Genus-3 planted-forest → higher_genus_modular_koszul.tex (genus-3 section)

TIER 2 — ADVERSARIAL RE-AUDIT (20 agents):
The first swarm's adversarial agents mostly hit rate limits. Relaunch the most critical ones:
1. Deep Beilinson: Vol I introduction (verify Five Facets, MC3 status, κ formulas)
2. Deep Beilinson: Vol I higher genus (verify Theorem D fix, shadow tower)
3. Deep Beilinson: Vol I bar-cobar adjunction (Theorems A, B)
4. Deep Beilinson: Vol I Koszul pairs (verify circularity fix)
5. Deep Beilinson: Vol II foundations (Swiss-cheese, derived center)
6. Deep Beilinson: Vol II 3d gravity (DS-HPL transfer theorem)
7. Deep Beilinson: Vol II spectral braiding (r-matrix, YBE)
8. Deep Beilinson: concordance (constitutional consistency)
9. Deep Beilinson: landscape census (master table correctness)
10. Adversarial: Mok25 dependency (single-preprint vulnerability)
11. Adversarial: status tag sweep (ProvedHere vs Conjectured consistency)
12. Adversarial: AP5 propagation sweep (all fixes propagated?)
13. Adversarial: perturbative scope (remaining "exact" language?)
14. Adversarial: cross-volume label consistency
15. Adversarial: Teleman reconstruction (flat identity hypothesis)
16. Adversarial: analytic sewing claims (MC5)
17. Adversarial: BV/BRST = bar (genus 0 proved, higher genus conjectural)
18. Adversarial: formality chain (Kontsevich formality correctly used?)
19. Adversarial: quantum group claims (DK bridge)
20. Adversarial: non-principal W-duality (hook-type scope)

TIER 3 — PROSE CLEANUP (15 agents):
The prose agents mostly hit limits. Relaunch systematically:
1. Vol I preface (7300 lines, highest priority)
2. Vol I introduction
3. Vol I theory chapters (bar, cobar, adjunction, inversion, Koszul pairs, Hochschild)
4. Vol I higher genus chapters (foundations, complementarity, modular Koszul)
5. Vol I example chapters (Heisenberg, KM, W-algebras, free fields, genus expansions)
6. Vol I connections (Feynman, BV/BRST, YM, E_n, Langlands, concordance)
7. Vol I appendices (signs, nonlinear shadows, homotopy transfer, dual methodology)
8. Vol II introduction + preface
9. Vol II foundations + locality + axioms
10. Vol II spectral braiding + line operators + brace
11. Vol II 3d gravity + gravity chapters (8 files)
12. Vol II descent + PVA chapters
13. Vol II examples (rosetta, computing, worked, complete-proved)
14. Vol II frontier chapters (all *_frontier.tex files)
15. Vol II ordered sector + factorization bridge + Yangian

TIER 4 — NEW CONTENT FROM RAEEZNOTES (15 agents):
1-5. WP5 worked examples (CS, 3d gravity, twisted holography, M2, M5) — canonical Θ^oc template
6-9. WP6 example chapter restructure (Heisenberg, KM, W-algebras, free fields)
10. WP7: open problems restated as Θ^oc questions
11. Four-test boundary of control (rn116 Item 13)
12. Two orthogonal axes (rn116 Item 14)
13. DS as functor on primitive triples (rn115 Item 21)
14. Restricted DK-5 conjecture (rn116 Item 12)
15. r(z) = KD inverse named theorem (precise categorical statement)

TIER 5 — COMPUTE VERIFICATION + EXTENSION (15 agents):
1. Run ALL 2506+ new tests and verify they pass
2. Fix ds_kappa_from_affine() in hook_type_w_duality.py (uses wrong ghost subtraction formula)
3. Genus-4 F₄ for 10 families
4. Genus-5 F₅ for 10 families
5. Shadow towers through arity 12 for Virasoro
6. Multi-channel genus-2 graph sum for W₄
7. Δ_z^grav first nonlinear correction (explicit formula)
8. Cross-verify F₂(W₃) = (c+120)/(16c) by independent method
9. W₃ genus-2 with R-matrix dressing (test universality)
10. Compute S₃ for ALL non-simply-laced + exceptional via Lie bracket
11. Lattice VOA shadow data (D₄, E₈, Leech, Niemeier)
12. Minimal model bar complex (verify NOT Koszul)
13. Admissible-level Koszulness tests
14. Shadow connection monodromy numerical verification
15. Planted-forest genus-4 formula

TIER 6 — THE GRAVITATIONAL COPRODUCT IS PRIMITIVE (3 agents):
The most important new discovery of this session. The transferred coproduct Δ_z^Vir is STRICTLY PRIMITIVE at all arities (ghost-number obstruction kills every HPL tree correction). This means: gravity doesn't produce particles, it only braids them. The quartic pole (c/2)/z³ and double pole 2T/z in the r-matrix are the COMPLETE content of gravitational dynamics.

1. **Writer**: Write a full detailed exposition in Vol II 3d_gravity.tex as a new subsection "The gravitational coproduct is primitive" after the DS-HPL transfer theorem. The exposition must cover:
   - The setup: Virasoro Yangian from DS-HPL, coproduct Δ_z, what primitivity means
   - The computation: ghost-number obstruction (h has ghost degree -1, p kills ghost ≠ 0, so ALL HPL tree corrections vanish)
   - The physical meaning: two channels of nonlinearity (coproduct vs r-matrix twist), gravity uses only channel 2
   - Comparison with gauge theory: affine KM Yangian HAS nontrivial coproduct (gluons split), DS reduction kills production vertices while preserving scattering
   - Why this is deep: no local gravitational degrees of freedom in 3d, no propagating gravitons, only topological effects + braiding
   - The formula: Δ_z^Vir(T) = τ_z(T)⊗1 + 1⊗T, and the compatibility condition reduces the entire Yangian to one field + one r-matrix
   - Connection to BTZ: conical deficits and black holes are topological, encoded in monodromy of the r-matrix braiding, not in coproduct vertices
   Read the existing prop:coproduct-arity2-vanishing in 3d_gravity.tex and EXPAND it into a full 3-4 page exposition at the Chriss-Ginzburg standard. This should be one of the most memorable passages in the monograph.

2. **Adversarial**: Try to BREAK the primitivity result. Check: does the ghost-number argument really work at ALL arities? What about the perturbation δ — does it preserve ghost number? What if the BRST differential has ghost-number-violating terms? What about the A∞ morphism condition — does primitivity of Δ_z force any constraints on the transferred products m_k^Vir? Could the argument fail for W_N (N≥3) where the DS reduction is more complex?

3. **Compute**: Write ~/chiral-bar-cobar/compute/lib/gravitational_coproduct.py verifying the primitivity by explicit computation. Implement the SDR (i,p,h) for sl_2 DS, compute the first 3 HPL tree corrections to Δ_{z,2}(T,T) numerically at k=1,2,3, and verify they vanish to machine precision. Also check Δ_{z,3}(T,T,T) vanishes. Write 40+ tests.

TIER 7 — STANDALONE PAPER (5 agents):
1. Write abstract + introduction (from compute/audit/standalone_paper_plan.md)
2. Write §3-4 (Riccati algebraicity theorem + proof)
3. Write §5-6 (G/L/C/M classification + shadow tables)
4. Write §7 (F₂(W₃) computation)
5. Adversarial review of the draft

Standing directives: Do NOT build LaTeX or run pre-existing tests unless you wrote them. Focus on mathematical writing and new computation. Beilinson Principle. Chriss-Ginzburg standard. Kac/Etingof/Serre prose. No AI slop. No em dashes. No hedging.

## ===END PROMPT===
