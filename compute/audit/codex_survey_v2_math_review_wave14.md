# Codex Survey v2 Mathematical Correctness Review — Wave 14

## Per-Section Finding Counts
| Section | CRITICAL | MODERATE | MINOR |
|---------|----------|----------|-------|
| 1 | 0 | 2 | 0 |
| 2 | 0 | 1 | 1 |
| 3 | 0 | 1 | 0 |
| 4 | 0 | 0 | 0 |
| 5 | 0 | 1 | 0 |
| 6 | 0 | 0 | 1 |
| 7 | 1 | 1 | 0 |
| 8 | 0 | 0 | 0 |
| 9 | 1 | 1 | 0 |
| 10 | 1 | 0 | 0 |
| 11 | 0 | 0 | 0 |
| 12 | 1 | 1 | 0 |
| 13 | 1 | 1 | 0 |

## Findings by Section
### Section 1: The bar construction on algebraic curves
#### [MODERATE] Genus-zero coordinate formula is stated as if it were global on an arbitrary curve (line 255)
- Claim as written: the survey places points on a general curve `X` and assigns `\eta_{ij}=d\log(z_i-z_j)`.
- Why it's wrong/imprecise/overclaimed: `z_i-z_j` is not globally defined on a general algebraic curve. This formula is literally valid only on an affine chart / comparison surface such as `\mathbb A^1` or `\mathbb P^1` with chosen local coordinates. On higher-genus curves the survey itself later replaces it by the prime-form propagator.
- Independent verification: Section 2 switches to the prime form `E(z_1,z_2)` and the propagator `d\log E(z_1,z_2)+...` at lines 546-552. So the Section 1 formula cannot be a global formula on arbitrary `X`.
- Suggested fix: either scope Section 1.3 explicitly to genus `0` / local collision coordinates, or replace `d\log(z_i-z_j)` by the appropriate local logarithmic form on configuration space.

#### [MODERATE] The affine double-pole contribution is incorrectly written as `d\eta_{12}` (line 493)
- Claim as written: `\mu^{\mathrm{ch}}= f^{ab}{}_c J^c\cdot\eta_{12} + k\kappa^{ab}\cdot\mathbf 1\cdot d\eta_{12}`.
- Why it's wrong/imprecise/overclaimed: `\eta_{12}=d\log(z_1-z_2)` is closed away from the collision divisor, so a literal `d\eta_{12}` term is zero on the configuration space and cannot represent the affine central term in the bar differential. This confuses the de Rham differential with the second-order OPE contribution.
- Independent verification: `chapters/theory/configuration_spaces.tex:3086-3099` states `d\eta_{ij}=0` away from higher codimension strata. `chapters/theory/quantum_corrections.tex:115-122` likewise notes that `d(d\log(z_1-z_2))=0`.
- Suggested fix: say that the double pole contributes the scalar/curvature part of the residue operator, not a literal `d\eta_{12}` term.

### Section 2: Curvature and the genus tower
#### [MODERATE] `d_{z_1}\log E(z_1,z_2)` is misidentified as a differential of the second kind (line 546)
- Claim as written: `\omega(z_1,z_2):=d_{z_1}\log E(z_1,z_2)` is “the fundamental meromorphic differential of the second kind.”
- Why it's wrong/imprecise/overclaimed: `d_{z_1}\log E(z_1,z_2)` has a simple pole along the diagonal; the normalized bidifferential of the second kind is obtained from `d_{z_1}d_{z_2}\log E(z_1,z_2)` (up to conventional sign), not from a single logarithmic derivative.
- Independent verification: the prime form has a simple zero on the diagonal, so one `z_1`-derivative produces a simple pole, not a symmetric double-pole bidifferential.
- Suggested fix: replace the sentence by “`d_{z_1}\log E(z_1,z_2)` is the logarithmic derivative of the prime form; the bidifferential of the second kind is `d_{z_1}d_{z_2}\log E(z_1,z_2)`.”

#### [MINOR] The curvature formula is missing the explicit `g\ge 1` scope the section promises (line 567)
- Claim as written: `d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_g`.
- Why it's wrong/imprecise/overclaimed: the user-requested scope issue is real here. The surrounding discussion is about the higher-genus propagator and the failure of genus-zero nilpotence, but the displayed equation itself is not fenced by `g\ge 1`.
- Independent verification: the survey immediately contrasts this with genus `0` flatness at lines 599-607, and `chapters/theory/en_koszul_duality.tex:1393-1397` states the curved formula explicitly “at genus `g\ge 1`.”
- Suggested fix: write “for `g\ge 1`, the fibrewise differential satisfies ...”.

### Section 3: Modular homotopy theory
#### [MODERATE] The displayed Feynman-transform formula omits the orientation/determinant twist needed for the stated sign rule (line 799)
- Claim as written: `F\cO(g,n)=\bigoplus_\Gamma \hbar^{g(\Gamma)} |\Aut(\Gamma)|^{-1}\otimes_{v}\cO(g(v),\In(v))`, followed by a differential whose sign comes from `\det(E(\Gamma))`.
- Why it's wrong/imprecise/overclaimed: as written, the formula does not contain the determinant/orientation line that the next paragraph uses to define the contraction signs. The displayed formula is therefore not the full Feynman transform data needed for the sign convention being advertised.
- Independent verification: the survey itself appeals to the edge-ordering determinant at lines 806-809, but that determinant twist is absent from line 799. The same omission persists in the `\Com` specialization, where `\det(E(\Gamma))` suddenly appears at line 818.
- Suggested fix: include the determinant/orientation twist directly in the Feynman-transform formula, or explicitly say the display is schematic and suppresses the standard sign twist.

### Section 4: The universal Maurer--Cartan element
No mathematical findings. The sign in the MC equation at lines 1178-1182 is consistent with expanding `(d_0+\Theta_\cA)^2=0`.

### Section 5: The modular tangent complex and Chern--Weil theory
#### [MODERATE] `\kappa(\cA)` is treated as the first Chern class itself, rather than the scalar coefficient of that class (line 1441)
- Claim as written: “This is the first Chern class of the modular bar bundle.”
- Why it's wrong/imprecise/overclaimed: the displayed formula at line 1439 gives `\kappa(\cA)\in\Bbbk`, a scalar. The actual cohomology class is `c_1(\mathcal L_\cA)=\kappa(\cA)\lambda` or, genuswise, `\operatorname{obs}_g(\cA)=\kappa(\cA)\lambda_g`. Chain level, scalar level, and cohomology level are being conflated.
- Independent verification: `chapters/theory/higher_genus_modular_koszul.tex:9023-9025` states `c_1(\mathcal L_\cA)=\kappa(\cA)\cdot\lambda`; `chapters/theory/higher_genus_modular_koszul.tex:9048-9062` identifies `\kappa` with the scalar trace / first-Chern-number slot.
- Suggested fix: say “`\kappa(\cA)` is the scalar Chern--Weil coefficient (or first Chern number), while the corresponding class is `\kappa(\cA)\lambda`.”

### Section 6: The shadow obstruction tower
#### [MINOR] The survey does not distinguish the global quartic contact shadow from its weight-line projection in the `\beta\gamma` case (line 1972)
- Claim as written: “the quartic contact invariant `\mu_{\beta\gamma}=0`,” while later the section says `Q^{\mathrm{contact}}_{\beta\gamma}\neq 0`.
- Why it's wrong/imprecise/overclaimed: the local chapters distinguish two different objects: the full quartic contact shadow `Q^{\mathrm{contact}}_{\beta\gamma}`, which is nonzero, and the weight-changing-line projection `\mu_{\beta\gamma}`, which vanishes by rank-one abelian rigidity. The survey collapses these into one name at line 1972.
- Independent verification: `chapters/examples/free_fields.tex:1197-1205` explicitly separates nontrivial `Q^{\mathrm{contact}}_{\beta\gamma}` from the vanishing slice projection `\mu_{\beta\gamma}`; `chapters/examples/beta_gamma.tex:2522-2530` proves the vanishing only on the weight-changing line.
- Suggested fix: rewrite line 1972 as “the weight-changing-line quartic projection `\mu_{\beta\gamma}` vanishes,” reserving `Q^{\mathrm{contact}}_{\beta\gamma}` for the full quartic class.

### Section 7: The standard landscape
#### [CRITICAL] Heisenberg `r`-matrix is misprinted as degree zero instead of `1/z` (line 2209)
- Claim as written: `r(z)=k/z^0`.
- Why it's wrong/imprecise/overclaimed: this is simply false. The Heisenberg binary shadow is proportional to `1/z`, not to a degree-zero central constant.
- Independent verification: the same survey states `r(z)=k/z` at line 460, and `chapters/examples/landscape_census.tex:376` records the Heisenberg `r`-matrix as `k/z`.
- Suggested fix: replace `k/z^0` by `k/z`.

#### [MODERATE] The affine Kac--Moody “Koszul dual” is overstated as the shifted-level affine algebra itself (line 2267)
- Claim as written: `\widehat\fg_k^! = \widehat\fg_{-k-2h^\vee}`.
- Why it's wrong/imprecise/overclaimed: in the repo’s own mathematical discipline this confuses a same-family shadow object with the genuine strict dual target. The strict chiral Koszul dual is the chiral Chevalley--Eilenberg algebra at the shifted level, not the shifted-level affine algebra itself.
- Independent verification: `chapters/examples/landscape_census.tex:78-79` gives the Koszul dual as `\mathrm{CE}^{\mathrm{ch}}(\widehat{\fg}_{-k-2h^\vee})`; `chapters/examples/kac_moody.tex:488` and `chapters/examples/kac_moody.tex:1172` make the same distinction explicitly.
- Suggested fix: write that the strict dual is `\mathrm{CE}^{\mathrm{ch}}(\widehat{\fg}_{-k-2h^\vee})`, and that the shifted-level affine family is the same-family comparison object sharing the relevant `\kappa`.

### Section 8: Arithmetic of the shadow obstruction tower
No mathematical findings. The shadow-Eisenstein identity is correctly scoped as exact only at arity `2`, and the `s=0` continuation check gives `-24\kappa\,\zeta(0)\zeta(-1)=-\kappa`, matching `chapters/connections/arithmetic_shadows.tex:3458-3489`.

### Section 9: Scalar saturation and the Koszulness programme
#### [CRITICAL] The survey replaces “polynomial algebra generated in degrees `{0,1,2}`” by outright vanishing outside `{0,1,2}` (line 3031)
- Claim as written: `\operatorname{ChirHoch}^*(\cA)` vanishes outside degrees `{0,1,2}`.
- Why it's wrong/imprecise/overclaimed: this is stronger than, and incompatible with, the actual theorem. A polynomial algebra generated in degrees `{0,1,2}` typically has classes in arbitrarily high total degree.
- Independent verification: `chapters/theory/chiral_koszul_pairs.tex:1937-1940` states item (viii) as “`\mathrm{ChirHoch}^*(\cA)` is a polynomial algebra with generators concentrated in degrees `{0,1,2}`.”
- Suggested fix: replace line 3031 by the theorem’s actual statement.

#### [MODERATE] The Barr--Beck--Lurie item drops the crucial fiber qualifier (line 3029)
- Claim as written: “The Barr--Beck--Lurie comparison for `\barB\dashv\Omega` is an equivalence.”
- Why it's wrong/imprecise/overclaimed: the proved theorem only gives equivalence on the fiber over `\barBgeom(\cA)`; the survey’s wording sounds like an unconditional global equivalence.
- Independent verification: `chapters/theory/chiral_koszul_pairs.tex:1931-1933` states item (vi) as equivalence “on the fiber over `\barBgeom(\cA)`.”
- Suggested fix: restore the fiber/Koszul-locus qualifier.

### Section 10: The open/closed world (Volume II)
#### [CRITICAL] The bar complex is called an `\mathsf{SC}^{\mathrm{ch,top}}`-algebra when the proved local statement is an ordered `E_1` coalgebra (line 3424)
- Claim as written: “The bar complex with both structures is a `\SCchtop`-algebra.”
- Why it's wrong/imprecise/overclaimed: this flips the operadic variance on the bar side. The bar construction carries differential plus deconcatenation coproduct and is formulated locally as a single-coloured ordered `E_1` coalgebra, not as an algebra over the operad.
- Independent verification: `chapters/theory/en_koszul_duality.tex` now states “Bar complex as `E_1`-chiral coassociative coalgebra” and identifies `\barB^{\mathrm{ord}}(\cA)` as a dg coalgebra with deconcatenation coproduct, with `\mathsf{SC}^{\mathrm{ch,top}}` moved to the derived-center pair.
- Suggested fix: replace “algebra” by “coalgebra” here and in the surrounding discussion.

### Section 11: Modular PVA quantization
No mathematical findings. Read as obstruction theory, the one-edge decomposition and genus-1 obstruction package are internally coherent with the local modular-bar formalism.

### Section 12: Holographic modular Koszul duality
#### [CRITICAL] The KZ comparison formula is algebraically inconsistent as written, and it also violates the survey’s own level-full `r`-matrix discipline (line 3918)
- Claim as written: `\sum_{i<j} r_{ij}(z_i-z_j)\,d\log(z_i-z_j)=\frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}`, with `r_{ij}=\Omega_{ij}/(h^\vee+k)`.
- Why it's wrong/imprecise/overclaimed: if `r(z)=\Omega/((k+h^\vee)z)`, then `r(z)\,d\log z` gives `\Omega\,dz/((k+h^\vee)z^2)`, not the `1/z` KZ form displayed on the next line. In addition, the formula suppresses the survey’s own level-full binary-shadow normalization from Section 7, where the affine `r`-matrix vanishes at `k=0`.
- Independent verification: the algebraic mismatch is immediate from substituting `d\log z=dz/z`. The survey’s own Section 7 gives the affine binary shadow as `k\Omega/z` at lines 2264-2265, explicitly vanishing at `k=0`.
- Suggested fix: either write the connection as `\sum r_{ij}(z_{ij})\,dz_{ij}` with the chosen `r(z)`, or switch consistently to the KZ normalization `\Omega/((k+h^\vee)z)` without multiplying by `d\log`.

#### [MODERATE] Section 12 promotes the dg-shifted Yangian package from a proved affine-lineage statement to an “every 3d HT system” theorem (line 3852)
- Claim as written: every 3d HT system `T` is controlled by `\cH(T)=(\cA,\cA^!,\cC,r(z),\Theta_\cA,\nabla^{\hol})`, with `\cA^!` holographically a dg-shifted Yangian.
- Why it's wrong/imprecise/overclaimed: the survey itself previously states that the dg-shifted Yangian is proved only for the affine lineage and that extension to non-standard families is still programme. Section 12.1 suppresses that scope restriction.
- Independent verification: `standalone/survey_modular_koszul_duality_v2.tex:3654-3655` says “dg-shifted Yangian is proved for affine lineage only, extension to non-standard families is programme.” Section 12.4 then lists the full derived Yangian-shadow target as conjectural at lines 3943-3945.
- Suggested fix: restrict the Section 12.1 package to the proved affine/standard lane, or explicitly tag the all-HT-system statement as programme/conjectural.

### Section 13: Completion and the frontier
#### [CRITICAL] The survey falsely reports MC5 as proved (line 4197)
- Claim as written: “all five master conjectures MC1--MC5 are proved.”
- Why it's wrong/imprecise/overclaimed: this contradicts the repository’s constitutional status surface. MC5 is only partially proved: the analytic HS-sewing lane is proved, but the full genuswise BV/BRST/bar identification remains open.
- Independent verification: `chapters/connections/editorial_constitution.tex:149-150` marks MC5 “Partially proved”; `chapters/connections/editorial_constitution.tex:179-185` explains that the genuswise BV/BRST/bar comparison is still conjectural; `chapters/connections/concordance.tex:1863-1871` says “MC5 (analytic part proved).”
- Suggested fix: replace the status line by “MC1--MC4 are proved; MC5 is analytically proved in its HS-sewing lane, but the full BV/BRST/bar identification remains open.”

#### [MODERATE] The four-test summary collapses the corrected all-genus differential back to “the bar differential” (line 4528)
- Claim as written: “`D_\cA^2=0`: the bar differential squares to zero at all genera and arities.”
- Why it's wrong/imprecise/overclaimed: the raw higher-genus fibrewise bar differential does not square to zero; it satisfies `d_{\mathrm{fib}}^2=\kappa\omega_g`. Nilpotence is restored only after passing to the corrected total differential.
- Independent verification: `chapters/theory/en_koszul_duality.tex:1402-1428` explicitly distinguishes the non-flat fibrewise differential from the corrected flat coderivation `\D_g`.
- Suggested fix: write “the corrected total differential squares to zero at all genera and arities,” not “the bar differential.”

## Summary
- Strongest sections (mathematically): Sections 4, 8, and 11. I found no definite mathematical correctness failures there. Section 8 in particular survives the requested `s=0` arithmetic check.
- Sections needing rectification: Sections 7, 9, 12, and 13 need the most urgent repair. Section 1 also needs cleanup because the general-curve bar formulas are too loose and one affine Kac--Moody display is genuinely wrong.
- Overall math-correctness grade: C. The survey contains several real mathematical errors, plus multiple structural overclaims about status and scope. The core architecture is often recognizable and many family-specific `\kappa` values are correct, but the current claim surface is not yet reliable enough for an A/B-grade survey.
