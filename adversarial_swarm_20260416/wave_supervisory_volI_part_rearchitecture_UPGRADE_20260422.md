# Wave Supervisory — Vol I Part Re-architecture, Cross-Volume Upgrade (2026-04-22)

**Date.** 2026-04-22. **Author.** Raeez Lorgat. **Mode.** Lossless upgrade; the 2026-04-16 document (`wave_supervisory_volI_part_rearchitecture.md`, 576 lines, §§1--11) stays verbatim. This file extends it with §§12--16, recording the cross-volume sharpening imposed on the four Vol I pillars by the 2026-04-22 Vol III two-stage factorisation, the two-scope $\kappa$ split, the positive-geometry grammar, and the three-factor Universal Trace Identity.

**Scope.** Every change is a *sharpening*: each pillar gains a structural lens that refines but does not displace its 2026-04-16 statement. The four pillars of Vol I remain the four interior Parts of the Option C spine. The cross-volume bridges listed below are the content of the new Part VI centrepiece.

---

## §12. Pillar 1 (Koszul Reflection) — now Stage 1 of a two-stage factorisation

The Vol III 2026-04-22 synthesis factors the CY-to-chiral functor $\Phi: \mathrm{CY}\text{-cat}_d \to \mathrm{ChirAlg}$ through an intermediate Koszul reflection: $\Phi = \Phi_2 \circ \Phi_1$, with $\Phi_1$ the stage that sends a CY datum to its Koszul-self-dual chiral image on $\mathrm{Kosz}(X)$, and $\Phi_2$ the stage that assembles the $E_n$-chiral output at the correct dimensional scope. The Vol I Koszul Reflection $K = \overline{B}_X$ *is* Stage 1 at the internal Vol I level: on $\mathrm{Kosz}(X)$, $K^2 \simeq \id$ defines the involutive invariant of the Koszul-self-dual subcategory, and Stage 1 of $\Phi$ is precisely $\Phi_1(\mathcal{C}) = K(\mathcal{A}_{\mathcal{C}})$ with $\mathcal{A}_{\mathcal{C}}$ the chiral algebra image of $\mathcal{C}$.

The cross-volume refinement this installs on Part II of Vol I is structural, not content-bearing: the Part-opener theorem `thm:koszul-reflection` gains a final clause naming Stage 1 as the Vol I shadow of Vol III's factorisation. The four named morphisms (twisting unit $\eta$, twisting counit $\varepsilon$, reflection $K$, genus-completed counit $\psi(\hbar)$) remain the internal architecture. The bridge $K = \Phi_1|_{\text{Vol I internal}}$ is the cross-volume structural identification.

Migration impact. Step 2 of the §9 checklist (create `chapters/theory/koszul_reflection_platonic.tex`) gains a fifth clause in the master theorem statement. No other file moves. The V19 chiral Hochschild Trinity remains the cohomological shadow of $K^2 \simeq \id$.

---

## §13. Pillar 2 ($\kappa$-Conductor) — two-scope split mirrored from Vol III

Vol III has four never-conflated $\kappa$-invariants: $\kappa_{\mathrm{ch}}$ (chiral-side), $\kappa_{\mathrm{cat}}$ (categorical Euler), $\kappa_{\mathrm{BKM}}$ (Borcherds/BKM weight $c_N(0)/2$), $\kappa_{\mathrm{fiber}}$ (fibre correction). The 2026-04-22 synthesis isolates two structurally distinct scopes at which $\kappa$ acts: a **denominator-scope** reading (restricted to the Koszul-self-dual subcategory, where Theorem A forces the bar-denominator identity and $\kappa$ is the leading logarithm coefficient), and a **ghost-scope** reading (the universal Borcherds-weight reading, where $\kappa$ is the BRST ghost charge or equivalently the Borcherds singular weight, defined wherever a BRST resolution exists).

Pillar 2 acquires the same split. The BRST Ghost Identity $K(A) = -c_{\mathrm{ghost}}(\mathrm{BRST}(A))$ is the **ghost-scope** reading: it holds universally where the quasi-free BRST resolution exists, across Heisenberg, free fermion, $bc(\lambda)$, $\beta\gamma(\lambda)$, affine KM, Vir, $W_N$, BP. The trinity $K_E = K_c = K_g$ is the **denominator-scope** reading: it holds on the Koszul-self-dual subcategory, and asserts that the Euler, conductor, and genus versions of $K$ coincide there. Outside $\mathrm{Kosz}(X)$, the three readings can differ — this is exactly the Vol III observation that $\kappa_{\mathrm{BKM}} \ne \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ on arithmetic examples, restated in Vol I vocabulary.

The Part III opener (§5 above) gains a second display that separates the two scopes. The first display (universal $K(A) = -c_{\mathrm{ghost}}$) remains as stated; a second display `K_E = K_c = K_g \text{ on } \mathrm{Kosz}(X)$` records the denominator-scope trinity. The standard landscape chapters (Heisenberg, KM, Vir, $W_N$, BP, $\beta\gamma$, lattice, Yangian) each compute both scopes where both apply, and record the discrepancy where they differ. Lattice and Heisenberg belong to Koszul-self-dual, so both scopes agree. Generic $\beta\gamma(\lambda)$ and $bc(\lambda)$ lie outside Koszul-self-duality except at special $\lambda$; the discrepancy is the $\lambda$-dependent ghost correction.

Migration impact. Step 2 creates `chapters/koszul/chiral_chern_weil_brst_conductor.tex` with two master-theorem displays. The per-family numerical corollaries (B1--B6 of the wave 14 $\kappa$-conductor report) are split into denominator-scope witnesses and ghost-scope witnesses; the inconsistencies dissolve once the scope is named.

---

## §14. Pillar 3 (Climax) — alongside the universal positive-geometry grammar

The Vol III 2026-04-22 synthesis adopts a universal grammar for the cohomological-Hall-algebra output of $\Phi$: for each CY target $X$, one writes $Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$, the equivariant vanishing-cycle cohomology of the moduli of effective objects, with $W$ the Calabi--Yau potential. This is a *positive-geometry* grammar: every output of $\Phi$ on compact CY_d fits this template, with the positivity matching the effective-cone and the grading matching the vanishing-cycle weight filtration.

Pillar 3 sits alongside this grammar rather than above or below it. The Climax `d_bar = KZ^*(∇_Arnold)` classifies the four classical theorems (DK, Verlinde, Borcherds, Arnold) as KZ-pullback specialisations on Vol I's chiral side. The positive-geometry grammar classifies the CoHA-valued outputs of $\Phi$ on the CY side. The cross-volume content is that the pullback of $\nabla_{\mathrm{Arnold}}$ along the Vol III structure functor (factorising through Stage 1 of §12) lands *inside* $Y^+(X)$: the chiral bar differential and the vanishing-cycle differential are two presentations of the same universal connection, on two presentations of the same universal moduli space. The Schiffmann--Vasserot cohomological-Hall-algebra description of $Y^+$ for $X = \mathbb{C}^3$ is the first worked example; K3 is the next.

Part IV gains a new chapter at its tail named `chapters/connections/positive_geometry_bridge.tex` which states the identification $\mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})|_{\Phi_1(\mathcal{C})} = \nabla_{\mathrm{vanishing}}|_{Y^+(X_{\mathcal{C}})}$ as a structural lemma. The four existing Climax chapters (Drinfeld--Kohno, Verlinde, Borcherds, Arnold) are unchanged; the positive-geometry chapter is the bridge to Vol III.

Migration impact. Step 2 adds one file to Part IV. The MC5 sewing theorem (V12) remains the genus-0-to-genus-1 corner closure; the positive-geometry bridge is the CY-side corner closure.

---

## §15. Universal Trace Identity — now three-factor

The 2026-04-16 document (§5 Part VI opener and §9 Step 2) installed a *two-factor* Universal Trace Identity:
$$\mathrm{tr}_{Z(\mathcal{C})}(K_{\mathcal{C}}) = \begin{cases} -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C}))) & \text{Vol I (Koszul)} \\ c_N(0)/2 & \text{Vol III (Borcherds)} \end{cases}$$

The 2026-04-22 synthesis establishes a **third factor**: the Pentagon trace from the Vol II single-colour Pentagon (V19 chiral Hochschild Trinity). The unified identity reads
$$\mathrm{tr}_{\mathrm{ghost}}(\mathcal{C}) \;=\; \mathrm{tr}_{\mathrm{Pentagon}}(\mathcal{C}) \;=\; \mathrm{wt}_{\mathrm{Borcherds}}(\Phi(\mathcal{C})),$$
with the ghost trace $= -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))$ (Vol I denominator reading), the Pentagon trace the single-colour coherence-cycle of the chiral Hochschild Trinity (Vol II), and the Borcherds weight $c_N(0)/2$ evaluated on the Gritsenko lift of $\Phi(\mathcal{C})$ (Vol III). The three factors agree on the Koszul-self-dual subcategory with BRST resolution and CY target supporting a Borcherds product.

This three-factor identity is the cross-volume centrepiece of Part VI. The master theorem in `chapters/connections/universal_trace_identity.tex` is now a three-factor display, not a two-factor case split. The Vol III lift — $\Phi$ factoring through Stage 1 (§12) — is what makes the middle term well-defined: the Pentagon trace lives on $\Phi_1(\mathcal{C}) \in \mathrm{Kosz}(X)$, not on $\mathcal{C}$ itself.

The numerical witness closes: on the $K3 \times E$ Mukai-enhanced Heisenberg witness, all three factors take the value $8$, realising the $\mathsf{B}$-row $K^\kappa = 8$ of derived-centre complementarity. At $N = 1$ (Gritsenko $\Delta_5$), all three factors equal $5$. The three-factor identity is checked at five lattice points $N \in \{1, 2, 3, 4, 6\}$ plus the Mukai-enhanced point.

Migration impact. Step 2 retargets the Universal Trace Identity chapter from two-factor to three-factor. The Part VI opener prose (§5 above) gains one line stating the three-factor identity. The V11 §8.5 reference is updated to §8.5-three-factor.

---

## §16. Vol I migration checklist — status under the cross-volume sharpening

Restating the §9 fourteen-step checklist with each step's status after the 2026-04-22 sharpening:

| # | Step | Status |
|---|------|--------|
| 1 | Pre-flight inventory | unchanged; runs verbatim |
| 2 | Create four new pillar chapter files | **sharpened**: Pillar 1 gets Stage 1 clause; Pillar 2 gets two-scope split; Pillar 3 gets positive-geometry bridge chapter |
| 3 | Create supporting supervisory files | **sharpened**: `universal_trace_identity.tex` now three-factor |
| 4 | Restructure `main.tex` Part declarations | unchanged; six-Part spine holds |
| 5 | Insert six Part-opener prose blocks | **sharpened**: Part II opener adds Stage 1 line; Part III opener adds denominator-scope display; Part IV opener adds positive-geometry bridge line; Part VI opener adopts three-factor identity |
| 6 | Reading-paths block | unchanged |
| 7 | Theorem-index generator | unchanged |
| 8 | Phantom-label audit | unchanged |
| 9 | Cross-volume `\ref` audit | **sharpened**: Vol III's `\ref` to Vol I Part VI now targets the three-factor identity |
| 10 | Build verification | unchanged |
| 11 | HU-W11g.5 verification | unchanged; closure confirmed |
| 12 | HU-W11g.6 verification | unchanged; closure confirmed |
| 13 | CLAUDE.md update | **sharpened**: each of Vol I / Vol II / Vol III CLAUDE.md records the three-factor identity and the two-scope $\kappa$ split as programme-level facts |
| 14 | Commit | **sharpened**: commit message names the cross-volume sharpening in a second paragraph |

Six of the fourteen steps acquire sharpening content; the other eight execute verbatim. No step is removed, replaced, or re-ordered. The migration remains a single commit.

The four interior pillars (II--V) of the Option C spine remain the architecture. The cross-volume sharpening is additive: Stage 1 on Pillar 1, two-scope split on Pillar 2, positive-geometry alongside on Pillar 3, three-factor Trace on Frontier. Pillar 4 (Shadow Quadrichotomy) carries no §§12--15 sharpening in this wave; its cross-volume upgrade is scheduled separately once the Vol III mock-modular K3 theorem `thm:mock-modular-k3-d2` propagates to Vol I's class M chapter.

— Raeez Lorgat, 2026-04-22
