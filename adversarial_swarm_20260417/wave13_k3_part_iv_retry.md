# Wave 13 (retry): Vol III Part IV K3 Yangian audit

Date: 2026-04-17. Target: Vol III Part IV. File skip: `k3_yangian_chapter.tex` (Wave-7 healed).

## Audit verdicts

| Item | Verdict | Evidence |
|------|---------|----------|
| Y_osp(4|20) NOT Y(gl(4|20)) | PASS | main.tex:890 "Envelope: $Y_{\osp(4 \mid 20)}$, conjectural (orthosymplectic super-Yangian of the Mukai form, signature $(4, 20)$; symmetric indefinite, not super-graded)". No `gl(4|20)` hit anywhere in Part IV. |
| Mukai rank 24 (not 22) | PASS | main.tex:873 "rank $24$, signature $(4, 20)$"; k3_chiral_algebra.tex:479 `$\kappa_{\mathrm{fiber}}$ & $\mathrm{rank}(\Lambda_{\mathrm{Mukai}})$ ... $24$`; :514 "codimension of ... sub-lattice $\Lambda^{3,2}$ (rank~$5$) inside the Mukai lattice (rank~$24$)". No `rank 22` hits in Part IV. |
| AP247 `{Φ_d}` family notation | PASS | Used correctly as `\{\Phi_d\}` in k3_quantum_toroidal_chapter.tex:523,527,540,809; `\Phi_d` in cy_d_kappa_stratification.tex:77-206 and coha_wall_crossing_platonic.tex. Specialisations `\Phi_2`, `\Phi_3` used correctly at main.tex:867,922. |
| HZ-7 bare κ in Vol III Part IV | PASS | Zero bare `\kappa` without subscript in k3_chiral_algebra, k3e_cy3_programme, k3e_bkm_chapter, k3_quantum_toroidal_chapter, toroidal_elliptic, cy_c_six_routes_*, cy_c_pentagon_hypothesis_closures_platonic, derived_categories_cy. All occurrences carry {ch, cat, BKM, fiber}. |
| Phantom `mock_modular_k3_proof.tex` | NOT PRESENT | Grep across all `.tex` in Vol III returns zero `\input{...mock_modular...}` references. Mock K3 is inscribed in-place as `\begin{remark}[Mock modular form from K3]\label{rem:mock-modular-k3}` at k3e_cy3_programme.tex:509-549 with explicit Zwegers decomposition (eq:mock-modular-decomposition), polar coefficient identification $-2 = -\kappa_{\mathrm{ch}}(\cA_{K3})$, and machine-precision verification $5.7\times 10^{-16}$. |
| κ_BKM(K3) = 5 via Gritsenko Δ_5 | PASS | main.tex:904 `\underbrace{\kappa_{\mathrm{BKM}} = 5}_{\mathrm{wt}(\Delta_5),\ \text{Borcherds lift}}`; k3_chiral_algebra.tex:355 "Borcherds additive lift $\phi_{0,1} \mapsto \Delta_5$ ... weight formula $\mathrm{wt}(\Delta_5) = c(0)/2 = 10/2 = 5$"; :492 `$\kappa_{\mathrm{BKM}}$ & $\mathrm{wt}(\Delta_5) = c_f(0)/2$ (Borcherds lift) ... $5$`; :26 credits Gritsenko--Nikulin for the generalized root datum. |

## Architecture assessment

Part IV preface (main.tex:862-967) is structurally sound. The κ-spectrum
`Spec_{κ_\bullet}(K3 × E) = {κ_cat=2, κ_ch=3, κ_BKM=5, κ_fiber=24}`
(main.tex:899-906) correctly separates manifold invariants (κ_cat, κ_fiber)
from construction-dependent invariants (κ_ch, κ_BKM). The deficit identity
`κ_fiber − κ_BKM = 24 − 5 = 19 = codim(Λ^{3,2}⊂Λ_Muk)` is stated with
explicit ramification to imaginary root families (k3_chiral_algebra.tex:514).

## Residual concerns (out-of-scope, for next wave)

1. k3_yangian_chapter.tex:2764 states "shadow depth remains $r_{\max}=3$ (class~L)"
   then in the SAME paragraph says "stays at depth~$2$" then "increase to depth~$3$". Class/depth labelling drifts
   within 4 lines. FILE IS WAVE-7 SKIP; flag for follow-up.
2. CY-C six-route convergence (main.tex:914-928) remains CONJECTURAL — correctly
   tagged. Route (4) via Φ_3 is the only proved branch (consistent with 2026-04-17
   Beilinson rectification that healed the pentagon stratification from κ_ch to
   generator rank ρ^{R_i}).
3. `Y_osp(4|20)` is tagged "conjectural" at main.tex:890; no attempt in Part IV
   to promote to theorem-status, which is correct given that the Mukai form is
   symmetric indefinite (not super-graded), so the super-Yangian envelope is
   analogy not derivation.

## Surgical edits

None. All six audit points pass. Part IV K3 Yangian architecture is coherent
post Wave-7 healing of k3_yangian_chapter.tex.

verdict: ACCEPT (0 edits required)
