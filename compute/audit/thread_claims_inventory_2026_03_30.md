# Complete Inventory of Mathematical Claims from Thread
## Beilinson self-audit, 2026-03-30

### A. Claims that are PROVED (backed by theorem in manuscript)

| # | Claim | Theorem | Volume | Status |
|---|-------|---------|--------|--------|
| A1 | Chiral Hochschild cochains carry brace dg algebra structure | thm:thqg-brace-dg-algebra | I | ProvedHere |
| A2 | Operadic center of SC^{ch,top} is C_ch^•(A,A) | thm:operadic-center-hochschild | I | ProvedHere |
| A3 | Center is geometrically inevitable via half-space factorization | thm:center-geometric-inevitability | I | ProvedHere |
| A4 | W(SC^{ch,top})-algebras = HT prefactorization algebras | thm:recognition (Vol II) | II | ProvedHere |
| A5 | A∞-chiral algebra from boundary vacuum | thm:boundary-algebra-from-vacuum | II | ProvedHere |
| A6 | Bulk = derived center Z_der(C) ≃ C_ch^•(A_b,A_b) | cor:bulk-derived-center-categorical | II | ProvedHere |
| A7 | Factorization homology ∫_{S^1} C ≃ HH_•(A_b) | thm:vol2-annulus-trace | II | ProvedHere |
| A8 | PVA descent from A∞-chiral cohomology | thm:cohomology-PVA-main | II | ProvedHere |
| A9 | Boundary-linear LG: Z_der(A_F) ≃ O(dCrit(W)) | thm:boundary-linear-bulk-boundary | II | ProvedHere |
| A10 | Exact pointed line algebra K = Ω(J_{F,p}) | thm:exact-line | II | ProvedHere |
| A11 | Kuranishi elimination to minimal line algebra | thm:boundary-kuranishi | II | ProvedHere |
| A12 | Fortified local bulk/boundary/line triangle | thm:fortified-local-triangle | II | ProvedHere |
| A13 | Gravitational Koszul triangle Vir_c / Vir_{26-c}-mod / C[[c]] | thm:gravity-koszul-triangle | II | ProvedHere |
| A14 | Universal modular MC element Θ_A via bar-intrinsic | thm:mc2-bar-intrinsic | I | ProvedHere |
| A15 | Genus obstruction tower as Postnikov system | prop:genus-tower-postnikov | II | ProvedHere |
| A16 | Open/closed MC element Θ^oc satisfies MC equation | thm:vol2-oc-mc-equation | II | ProvedHere |
| A17 | Q^contact_Vir = 10/[c(5c+22)] | thm:nms-virasoro-quartic-explicit | I | ProvedHere |
| A18 | Q(c=6k) = 5/[6k(15k+11)] at Brown-Henneaux | comp:gravity-quartic-correction | II | ProvedHere |
| A19 | Complementarity Q(c) + Q(26-c) | comp:gravity-quartic-correction | II | ProvedHere |
| A20 | q_4(A_F) = 0 in boundary-linear sector | prop:quartic-contact-vanishes-BL | II | ProvedHere |

### B. Claims that are PRECISELY CONJECTURAL (stated as formal conjectures)

| # | Claim | Label | Volume | Obstruction |
|---|-------|-------|--------|-------------|
| B1 | Global factorization descent theorem | sec:global | II | Gluing local open categories across curve |
| B2 | C_line ≃ A!-mod globally | conj:geometric-steinberg | II | Steinberg presentation |
| B3 | Full open-sector modular twisting morphism | princ:modular-trace (iv) | II | Global bordered log-modular cooperad |
| B4 | S-duality = Koszul duality | conj:ht-s-duality-koszul | I | Extension beyond affine KM |
| B5 | HT deformation quantization functor | conj:ht-deformation-quantization | I | 3d Poisson sigma-model realization |
| B6 | Cardy formula from MC moduli | prop:cardy-mc | II | Rigorous saddle-point on MC moduli |
| B7 | Khan-Zeng gauge theory = operadic center observables | rem:chiral-deligne-tamarkin-dimensional-jump | I | Comparison functor |

### C. Claims that are HEURISTIC (organizing principles, not theorems)

| # | Claim | Where | Issue |
|---|-------|-------|-------|
| C1 | Cyclic/traced/ribbon/modular as four-fold hierarchy | princ:modular-trace table | Ribbon row not formalized |
| C2 | "Extra dimension is universal normal-collar direction" | rem:chiral-deligne-tamarkin-dimensional-jump | Geometric language, not a theorem |
| C3 | Shadow obstruction tower = open-sector trace expansion | princ:modular-trace final sentence | True but identity is structural, not a new theorem |

### D. Claims that were FALSE (found and fixed by self-audit)

| # | Original claim | Error | Fix |
|---|----------------|-------|-----|
| D1 | Khan-Zeng "Proposition 3.1" | Paper has no numbered theorems | Fixed to §2.2 |
| D2 | Khan-Zeng "Theorem 5.2" | Paper has no numbered theorems | Fixed to §4.3 |
| D3 | Q(c=6k) = 5/[3k(15k+11)] | Off by factor 2 | Fixed to 5/[6k(15k+11)] |
| D4 | δ_H(c=6k) = 10/[3k²(15k+11)] | Off by factor 2 | Fixed to 5/[3k²(15k+11)] |
| D5 | ∫_{M̄_2} ψ_1² = 1/240 | ψ_1 undefined on M̄_{2,0} | Removed entirely |
| D6 | F_2^contact = Q · ∫ψ_1² | Unjustified formula | Removed entirely |
| D7 | thm:quartic-contact-shadow | Label doesn't exist | Fixed to thm:nms-virasoro-quartic-explicit |
| D8 | "Established independently" for Khan-Zeng | Misleading | Fixed to "independent construction corroborating" |
| D9 | Operadic center = perturbative observables (as fact) | Unproved | Fixed to "we expect" |
| D10 | ∫_{S^1} C ≃ HH_• "not yet proved" | Already proved in same file! | Fixed to cite thm:vol2-annulus-trace |
| D11 | Principle with no ClaimStatus | Missing epistemic tag | Fixed: now has status column in table |

### E. Items NOT in manuscript (discussed in thread only, not installed)

| # | Idea | Status | Why not installed |
|---|------|--------|-------------------|
| E1 | Chiral brace operations from FM trees | Already in def:chiral-braces (Vol I) | Pre-existing |
| E2 | Free polarization theorem | Already in cor:free-polarization (Vol II) | Pre-existing |
| E3 | One-step Jacobi coalgebra explicit formulas | Already in cor:explicit-line (Vol II) | Pre-existing |
| E4 | Propagator factorization P(t,z) ~ Θ(t)/z | Not proved as standalone theorem | Needs more work |
| E5 | Conv^{mod,≤4} formal definition | Referenced but not defined | Needs Vol I infrastructure |
