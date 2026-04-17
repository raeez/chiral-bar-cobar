# Wave 11 — Vol III Part II (CY-to-Chiral Functor): Attack & Heal

Target: Vol III Part II comprising three chapters:
- `chapters/theory/cy_to_chiral.tex` (5188 lines)
- `chapters/theory/m3_b2_saga.tex` (1261 lines)
- `chapters/theory/quantum_chiral_algebras.tex` (2713 lines)

Part frame: `main.tex:663-735` (`\part{The CY-to-Chiral Functor}`, `\label{part:bridge}`).

## Phase 1 — Adversarial audit

### (i) CG deficiency opening
`cy_to_chiral.tex:4` opens with a genuine CG deficiency: "A Calabi--Yau category has a trace. A chiral algebra has an OPE. The trace is a map $\HH_d(\cC) \to \C$; the OPE is a distribution-valued product on sections over a punctured disc. No formal argument connects them." Forced question: "what functor connects CY categories to chiral algebras, and what structure must it preserve?" No AP106 narration block. PASS.

### (ii) AP247 `{Φ_d}` propagation
Part II is AP247-aware at the structural level. The opening of §sec:cy-chiral-functor (`cy_to_chiral.tex:41`) explicitly states:
> "The correspondence programme $\{\Phi_d\}_{d \geq 1}$ is not a single functor; it is a $d$-indexed family of constructions ... the collection $\{\Phi_d\}$ does not assemble into a functor in the standard category-theoretic sense: there is no single target category in which the image sits."

The Platonic theorem `thm:phi-platonic` uses `\Phi_d` consistently. Universal properties (U1)-(U4) use bare `\Phi` with explicit scope `Fix $d \geq 1$` in force — acceptable scoped form.

Residual AP247 drift sites found:
- `cy_to_chiral.tex:14`: `\kappa_{\mathrm{ch}}(\Phi(\cC))` at explicit $d=2$ context → should be `\Phi_2`.
- `cy_to_chiral.tex:143`: Theorem CY-A$_2$ displays `\Phi : \CY_2 \to \Etwo\text{-}\ChirAlg` (plus (i)–(ii) uses `\Phi(\cC)`) at explicit $d=2$ → should be `\Phi_2`.
- `quantum_chiral_algebras.tex:57`: Construction of CY $R$-matrix at "dimension $2$" uses `A_\cC = \Phi(\cC)` → should be `\Phi_2`.
- `m3_b2_saga.tex:61`: Programme-level prose "construction of $\Phi$ from Chapter~\ref{ch:cy-to-chiral}" → should be `\{\Phi_d\}_{d \geq 1}`.

### (iii) Φ_d per-d targets — honesty of scope
- d=1 (elliptic curve): `cy_to_chiral.tex:134` records $\Phi(\Coh(E)) = $ elliptic lattice VOA, natively $E_\infty$, $\kappa_{\mathrm{ch}}=1$. PASS.
- d=2 (K3, Enriques): unconditional $\Phi_2$, `thm:phi-k3-explicit` explicit evaluation to Mukai–Heisenberg of rank 24. PASS.
- d=3 (quintic, local $\bP^2$, $\C^3$): remark `rem:phi3-quintic-local-p2` at `cy_to_chiral.tex:4369` makes honest scoping — quintic via CoHA Gepner chart, local $\bP^2$ via SV/Nakajima, both explicit. Non-K3-fibered CY$_3$ admit BCOV/Göttsche substitutes, not Borcherds lift. PASS.
- d=4 (CY$_4$ p$_1$-twisted): theorem status table says "K3×K3: N(X)=0, unobstructed E$_4$"; `quantum_chiral_algebras.tex` covers via hCS. Scope honest.
- d=5: generic CY$_5$ has $\kappa_{\mathrm{ch}}=0$ via Hodge supertrace (Vol III `cy_d_kappa_stratification.tex`). No overclaim in Part II. PASS.

### (iv) Universal trace identity
`phi_universal_trace_platonic.tex` is included at `main.tex:1154` (Part VII frontiers, Ch 23a). `bar_cobar_bridge.tex` at Ch 23. Part II chapters themselves do not cross-cite the UTI — opportunity for forward pointer (non-critical; UTI is post-Part-II material).

### (v) Mock K3 path
No citation of `mock_modular_k3_proof.tex` (phantom path) or of `k3_yangian_chapter.tex:2767-2783` in Part II. Mock modular only appears in `cy_to_chiral.tex:2241, 4347` as a class $\mathbf M$ deformation descriptor, not a citation; no stale path.

### (vi) HZ-7 bare κ
`grep '\\kappa(?!_|\\_)'` on all three Part II chapters: zero hits. PASS. The `$\kappa^{(4)}$` occurrences at `cy_to_chiral.tex:4569-4624` are tensor indices (4-index object $\kappa^{(4)}_{ijkl}$), not bare $\kappa$.

### (vii) κ_BKM(Φ_d) values
- d=1: $\kappa_{\mathrm{ch}}(\text{lattice VOA on }E)=1$; no BKM context.
- d=2: K3 → $\kappa_{\mathrm{ch}}=2$ (Hodge supertrace), $\kappa_{\mathrm{BKM}}=5$ via Gritsenko $\Delta_5$ (AP238/245 verified Wave-4 #20, Wave-7 #38). Part II at `cy_to_chiral.tex:71` and `:334` matches.
- d=3 (K3×E): `cy_to_chiral.tex:334`: $\kappa_{\mathrm{ch}} = 2 + 1 = 3$. $\kappa_{\mathrm{BKM}}(\Phi_{10}) = 5$ elsewhere in programme. Consistent.
- Quintic (`rem:phi3-quintic-local-p2`): $\kappa_{\mathrm{BKM}}$ undefined (no even unimodular Mukai), BCOV substitute. Honestly scoped.
No factor-13 UTI residue (Wave-7 #38 retraction fully propagated into Part II).

### (viii) AP-CY62 geometric vs algebraic
`cy_to_chiral.tex:57-60` (universal property U1): `B^{\mathrm{ord}}(\Phi(\cC)) \simeq \mathrm{CC}_\bullet(\cC) \text{ in } \mathrm{ChirCoAlg}^{\mathrm{conil}}_{\cM_d}` — algebraic (bar/operadic) side explicit. `quantum_chiral_algebras.tex` uses $\RHom(\Omega B(A), A)$ at :925 for derived centre — algebraic. No bare "$\End^{\mathrm{ch}}$ on $\FM_k(\C)$" attribution. PASS.

## Phase 2 — Heal

Four surgical edits applied:

1. `cy_to_chiral.tex:14`: `\kappa_{\mathrm{ch}}(\Phi(\cC))` → `\kappa_{\mathrm{ch}}(\Phi_2(\cC))`.
2. `cy_to_chiral.tex:141-148`: Theorem CY-A$_2$ display and properties (i)/(ii): three `\Phi` → `\Phi_2`.
3. `quantum_chiral_algebras.tex:57`: `A_\cC = \Phi(\cC)` → `A_\cC = \Phi_2(\cC)` (construction context is explicit dimension-2).
4. `m3_b2_saga.tex:61`: "construction of $\Phi$" → "construction of $\{\Phi_d\}_{d \geq 1}$" (programme-level prose).

All edits tighten AP247 discipline without touching mathematical content.

## Residuals (deferred)

- Bare `\Phi(` at `cy_to_chiral.tex:57, 59, 63, 65, 67, 68, 70-76, 147-148, 155, 334, 349, 353, 365, 377, 380, 399, 601, 606, 609, 844, 849, 1255-1256, 1265, 1270, 191` etc.: these occur INSIDE scoped contexts (Theorem `thm:phi-platonic` with `Fix $d \geq 1$`, universal properties at fixed $d$, or $d$-specific remarks such as Enriques descent at $d=2$). AP247 admits bare `\Phi` under fixed-$d$ scope. No violation.
- Universal Trace Identity cross-reference: UTI lives in Part VII (Ch 23a); forward reference from Part II would invert dependency order. Defer.

## Verdict

Vol III Part II is AP247-healthy at the architectural level (§sec:cy-chiral-functor unambiguously frames `{Φ_d}` as a correspondence programme, not a functor). Four residual drift sites are surgically corrected. HZ-7 clean, mock K3 path citations absent (no phantom), κ_BKM values consistent with Wave-4/7 healings, AP-CY62 discipline observed.
