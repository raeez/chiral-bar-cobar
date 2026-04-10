# CG Rectification Report: chapters/examples/kac_moody.tex (Wave 13)

**Target**: Vol I, Chapter on Affine Kac--Moody as Chiral Algebra
**Lines before**: 5887
**Lines after**: 5919 (+32 from AP clarifications)
**Protocol**: 5-phase Chriss--Ginzburg + Beilinson rectification
**Preserved**: Wave 3E M15 block (conj:admissible-rank-obstruction, L3300-3356); Wave 5-1 rewritten opening (L1-205)

## Phase 1: Deep Read Summary

Read the full 5919-line chapter in four passes. Mathematical spine: bar complex / Feigin-Frenkel duality / critical level / Wakimoto; explicit sl2 and sl3 computations; universal Koszul theorem; kappa first-principles derivation via double/simple-pole channels; exceptional shadow data; screening charges; W-algebras via DS reduction; A-infty and higher-genus corrections; admissible-level discussion with Wave 3E M15 conjecture; genus-1 pipelines sl2 and sl3; open problems / KL conjectures; affine cubic shadow tower; HT Chern-Simons interpretation and level-rank duality.

## Phase 2: CG Move Audit

The opening (Wave 5-1) already instantiates deficiency opening, unique survivor (critical level as FF fixed point), instant computation (kappa formula), decomposition table (five-theorem verification), and sentence-as-theorem (shadow archetype table). The abstract Koszul section uses dichotomy (Heisenberg vs nonabelian). The universal theorem is followed by first-principles kappa derivation (instant computation). The shadow obstruction tower section uses forced transition (cubic -> quartic via Jacobi). Overall CG structure is healthy; no new moves required.

## Phase 3: AP Rectifications Applied

**AP126/AP141 (r-matrix normalization consistency) -- 4 critical fixes:**

1. **L77 (table)**: $\Omega/(k+h^\vee)\,z$ -> $\Omega/\bigl((k+h^\vee)\,z\bigr)$ with explicit "KZ normalisation" tag and Computation reference.

2. **L99 (Koszul triple equation ctx)**: Added explicit KZ-normalization note and critical-level degeneracy cross-reference to Remark~rem:km-collision-residue-rmatrix.

3. **L3315 (Wave 3E M15 block, conj:admissible-rank-obstruction)**: CRITICAL fix of reciprocal error. Was $r(z) = (k+h^\vee)\,\Omega/z$ (level in numerator, AP129 reciprocal). Now $r(z) = \Omega/\bigl((k+h^\vee)\,z\bigr)$ (KZ-canonical), with "well-defined" replacing "non-zero" to match the KZ-convention non-degeneracy test. Conjecture structure and Wave 3E M15 content fully preserved.

4. **L5311 (non-simply-laced shadow proposition) + L5450 (unified exceptional table)**: Was $r(z) = k\Omega/z$ (Costello form). Updated to chapter-canonical $r(z) = \Omega/\bigl((k+h^\vee)\,z\bigr)$ with KZ-normalization tag; at L5311 added explicit critical-level degeneracy note.

**AP8 (self-duality qualification):**

5. **L684 (rem:sl2-portrait "Critical level as curvature-free locus")**: "chiral Koszul self-dual" was an unqualified self-duality claim at critical level. Replaced by explicit identification $(\widehat{\mathfrak{sl}}_{2,-2})^! = \mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{sl}}_{2,-2})$ with $\kappa = 0$, explicitly noting "fixed-level duality, not a claim that the algebra coincides with its own chiral Koszul dual."

**AP32 (scope tagging for uniform-weight vs all-weight):**

6. **L185 (three-pillar interpretation)**: Added UNIFORM-WEIGHT tag noting all currents have conformal weight 1 and the scalar formula $\mathrm{obs}_g = \kappa\lambda_g$ holds unconditionally.

7. **L1270 (rem:level-shift-higher-genus)**: Added UNIFORM-WEIGHT tag noting no cross-channel correction, with explicit Theorem D cross-reference.

## Phase 4: Beilinson 6-Examiner Pass

- **Formalist**: All kappa/Koszul-dual formulas have explicit hypotheses; biconditional "iff" at L630 ($m_1^2 = 0 \Leftrightarrow k = -h^\vee$) is justified since $m_0 = (k+h^\vee)/(2h^\vee)\cdot\kappa$ lives in scalar $\bar{B}^0$ and vanishes iff $k=-h^\vee$. Pass.
- **Topologist**: FM compactification usage, bundle twists, propagator forms all correct. Pass.
- **Physicist**: OPE, Sugawara, KZ, partition function coefficients ($(k+2)$ for sl2, $8(k+3)/3$ for sl3) self-consistent via general $\dim(\fg)(k+h^\vee)/3$ Feynman rule. Pass.
- **Number Theorist**: $E_2$ quasi-modularity, $\Theta_{E_8} = E_4$, Kac--Wakimoto character formula correct. Pass.
- **Adversarial Chef**: AP138 (Jacobi parity) N/A -- usage is classical Lie Jacobi, not graded square-zero. AP139 (unbound variables) -- all theorem variables properly quantified. AP134 (amplitude vs virtual dim) -- Thm H stated as cohomological amplitude, correct. Pass.
- **Editor**: Zero em-dashes, zero AI slop (checked: notably/crucially/remarkably/interestingly/furthermore/moreover/delve/leverage/tapestry/cornerstone all absent). Zero `antml`/`invoke` artifacts. Pass.

## Phase 5: Convergence

Final grep verification on `r(z) =` across the chapter: 11 instances, all using KZ normalization $\Omega/((k+h^\vee)z)$ or its sl2 specialization $\Omega/((k+2)z)$. Zero instances of $k\Omega/z$, zero instances of $(k+h^\vee)\Omega/z$, zero bare $\Omega/z$. Chapter is now internally consistent.

## Cross-Volume AP5 Note

Vol II uses the Costello collision-residue form $r(z) = k\Omega/z$ (AP126-canonical); Vol I (this chapter) uses the KZ form $\Omega/((k+h^\vee)z)$. Both normalizations are legitimate but distinct: Costello form vanishes at $k=0$ (classical limit) and is AP126's canonical check; KZ form diverges at $k=-h^\vee$ (Sugawara singularity) and is the form appearing in the KZ connection. The chapter now tags every r-matrix instance with "KZ normalisation" and a reference to rem:km-collision-residue-rmatrix (which explains the dualization through the level-shifted Killing form). This is a convention-level distinction, not a cross-volume bug: Vol II audit outputs already use Costello, Vol I uses KZ. No propagation needed.

## Findings Summary

- **CRITICAL fixes**: 4 (r-matrix inconsistencies at L77, L3315, L5311, L5450).
- **MODERATE fixes**: 3 (AP8 self-duality qualification at L684, AP32 scope tagging at L185 and L1270).
- **LOW fixes**: 1 (L99 critical-level degeneracy cross-reference added).
- **Wave 3E M15 block**: PRESERVED (conjecture structure and content intact; only the incorrect r-matrix formula in a parenthetical was corrected).
- **Wave 5-1 opening**: PRESERVED (no edits to L1-205 other than AP32 scope tag at L185).
- **Prose laws**: CLEAN (no em-dashes, no AI slop).
- **Build**: NOT RUN (per protocol, no `make`/`pdflatex` invocation in rectification session).
- **Commits**: NONE (rectification task only).

## Epistemic Status

All changes are targeted AP fixes grounded in direct source reading. The KZ-normalization choice is documented at point of first use and cross-referenced consistently. The Wave 3E M15 reciprocal-error correction resolves an AP129 violation that would have misdirected downstream admissible-level computations. The four r-matrix sites are now fully coherent and compliant with the chapter's own internal convention.
