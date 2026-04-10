% Wrong-Formula Blacklist (Wave 12)
% Modular Koszul Duality Programme -- Raeez Lorgat
% Purpose: concrete catalogue of WRONG formula forms repeatedly emitted by
% Opus 4.6 agents across Waves 1-11, paired with the correct form, the
% reason the wrong form is wrong, the wave/agent where it was caught, and
% a regex pattern for automatic hook detection when feasible.
%
% Companion file: opus_46_failure_modes_wave12.md (behavioural failure modes).
% This file: the concrete forbidden text strings.
%
% Entry format:
%   NAME. short label
%   WRONG.    LaTeX as emitted (forbidden)
%   CORRECT.  LaTeX as required
%   WHY.      one-line reason
%   CAUGHT.   wave / agent / AP id
%   REGEX.    pattern for automatic detection (or NONE if manual-only)

# Wrong-Formula Blacklist (Wave 12)

## Part A -- r-matrix and level prefix

### B1. Affine Kac-Moody r-matrix without level prefix
- WRONG:    `r(z) = \Omega/z`
- CORRECT:  `r(z) = k \cdot \Omega/z`
- WHY:      the level k survives d-log absorption; at k=0 the r-matrix must vanish. AP126/AP141.
- CAUGHT:   Waves 7-1, 7-2, 7-3, 7-4, 7-7, 8-1, 8-2, 9-1..9-6 (42+ instances). MOST VIOLATED AP.
- REGEX:    `r\(z\)\s*=\s*\\Omega\s*/\s*z` (fires when level prefix absent)

### B2. Virasoro r-matrix with quartic pole
- WRONG:    `r(z) = (c/2)/z^4`
- CORRECT:  `r(z) = (c/2)/z^3 + 2T/z`
- WHY:      Virasoro OPE has order-4 pole; r-matrix absorbs one d-log -> CUBIC, not quartic. AP19/AP21.
- CAUGHT:   various family chapters, Wave 6 CG sweep.
- REGEX:    `r\(z\)\s*=\s*\(c/2\)/z\^4`

### B3. Vir r-matrix with quadratic collapse
- WRONG:    `r(z) = (c/2)/z^2`
- CORRECT:  `r(z) = (c/2)/z^3 + 2T/z`
- WHY:      visual collapse from pole/weight confusion; the field T has weight 2 but the pole is 3. AP19/AP27.
- CAUGHT:   Wave 8 sweeps.
- REGEX:    `r\(z\)\s*=\s*\(c/2\)/z\^2`

### B4. Level-stripped r-matrix disguised as `\Omega dz/z`
- WRONG:    `r(z)\,dz = \Omega\, d\log z`
- CORRECT:  `r(z)\,dz = k\Omega\,d\log z`
- WHY:      another face of AP126; d-log form still carries the level. AP117/AP126.
- CAUGHT:   Wave 9-3 and Wave 9-6 sweeps.
- REGEX:    `\\Omega\s*\\?,?\s*d\s*\\log\s*z` (no `k` within 10 chars)

## Part B -- central charges and kappa

### B5. Bosonic beta-gamma central charge mislabelled as fermionic
- WRONG:    `c_{bc}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)`
- CORRECT:  `c_{bc}(\lambda) = 1 - 3(2\lambda - 1)^2`; separately `c_{\beta\gamma}(\lambda) = 2(6\lambda^2-6\lambda+1)`
- WHY:      the two partners satisfy c_{bc}+c_{βγ}=0; swapping them flips the sign. AP137.
- CAUGHT:   multiple family chapters; Wave 8 BRST survey.
- REGEX:    `c_\{bc\}\([^)]*\)\s*=\s*2\(6`

### B6. Fermionic bc central charge mislabelled as bosonic
- WRONG:    `c_{\beta\gamma}(\lambda) = 1 - 3(2\lambda - 1)^2`
- CORRECT:  `c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)`
- WHY:      mirror of B5; both errors coexist. AP137.
- CAUGHT:   same chapters as B5.
- REGEX:    `c_\{\\beta\\gamma\}\([^)]*\)\s*=\s*1\s*-\s*3`

### B7. W_N central charge with shifted harmonic number
- WRONG:    `\kappa(W_N) = c \cdot H_{N-1}`
- CORRECT:  `\kappa(W_N) = c \cdot (H_N - 1)` where `H_N = \sum_{j=1}^N 1/j`
- WHY:      `H_{N-1} \neq H_N - 1`; at N=2, the former is 1, the latter is 1/2. AP136.
- CAUGHT:   CLAUDE.md itself; Wave 9-4.
- REGEX:    `\\kappa\(W_N\)\s*=\s*c\s*\\cdot\s*H_\{N-1\}`

### B8. kappa universally equal to c/2
- WRONG:    `\kappa = c/2`  (any family)
- CORRECT:  `\kappa(V_c^{\mathrm{Vir}}) = c/2`  (ONLY Virasoro); KM uses `\kappa(V_k(\fg)) = \dim(\fg)(k+h^\vee)/(2h^\vee)`; Heis uses `\kappa = k`; W_N uses `c(H_N-1)`.
- WHY:      AP39: `\kappa \neq S_2` for non-Virasoro; c/2 is a family coincidence. AP1/AP9/AP39.
- CAUGHT:   holomorphic_topological.tex:41, Wave 10-5; dozens of earlier sweeps.
- REGEX:    `\\kappa\s*=\s*c/2` (not preceded by `^{\\mathrm{Vir}}` within 40 chars)

### B9. kappa + kappa' = 0 unscoped
- WRONG:    `\kappa + \kappa' = 0`  (stated universally)
- CORRECT:  for KM/free-field: `\kappa+\kappa'=0`; for Virasoro self-dual c=13: `\kappa+\kappa'=13`; for W_N: `\kappa+\kappa'=\rho_N K_N`.
- WHY:      complementarity constant depends on family; unscoped form implies a false universality. AP24/AP8.
- CAUGHT:   dozens of chapters; caught consistently in Waves 6, 9, 10.
- REGEX:    `\\kappa\s*\+\s*\\kappa'?\s*=\s*0` (flag for context review)

### B10. kappa = S_2 / 2 (wrong factor)
- WRONG:    `\kappa = S_2/2`   or   `S_2 = \kappa/2`
- CORRECT:  `S_2 = \kappa` (no factor of 2); only Virasoro satisfies `\kappa(V_c) = c/2`.
- WHY:      confusion between the Vir coincidence `c/2` and the generic `S_2=\kappa` shadow identity. AP39.
- CAUGHT:   N6 audit, Wave 11-4.
- REGEX:    `\\kappa\s*=\s*S_2\s*/\s*2|S_2\s*=\s*\\kappa\s*/\s*2`

### B11. Sugawara shift missing in av(r(z)) formula
- WRONG:    `\mathrm{av}(r(z)) = \kappa`  (non-abelian KM)
- CORRECT:  `\mathrm{av}(r(z)) + \dim(\fg)/2 = \kappa(V_k(\fg)) = \dim(\fg)(k+h^\vee)/(2h^\vee)`
- WHY:      av(r(z)) = κ holds for abelian (Heisenberg); non-abelian needs the dim(g)/2 Sugawara shift. AP102 / FM11.
- CAUGHT:   Wave 7-1 preface audit.
- REGEX:    `\\mathrm\{av\}\(r\(z\)\)\s*=\s*\\kappa[^(_^]` (absent a preceding abelian qualifier)

### B12. Bare kappa in Vol III
- WRONG:    `\kappa` (alone) anywhere in `~/calabi-yau-quantum-groups`
- CORRECT:  one of `\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{cat}}`, `\kappa_{\mathrm{BKM}}`, `\kappa_{\mathrm{fiber}}`.
- WHY:      Vol III requires a subscripted spectrum. AP113.
- CAUGHT:   Waves 9-7, 9-8, 9-9, 9-10 (~165 instances).
- REGEX:    `\\kappa(?!_)` restricted to `~/calabi-yau-quantum-groups/**/*.tex`

### B13. Non-approved kappa subscripts in Vol III
- WRONG:    `\kappa_{\mathrm{global}}`, `\kappa_{\mathrm{BPS}}`, `\kappa_{\mathrm{eff}}`
- CORRECT:  approved set only: `{ch, cat, BKM, fiber}`.
- WHY:      the spectrum is finite; new subscripts drift the theory. AP113/AP-CY1.
- CAUGHT:   Wave 9-8.
- REGEX:    `\\kappa_\{\\mathrm\{(global|BPS|eff|total|naive)\}\}`

## Part C -- bar complex, suspension, augmentation

### B14. Bar complex missing augmentation ideal
- WRONG:    `T^c(s^{-1} A)`
- CORRECT:  `T^c(s^{-1} \bar{A})` where `\bar{A} = \ker(\epsilon)`
- WHY:      the bar complex is built on the augmentation ideal; using A includes the unit and breaks the construction. AP132.
- CAUGHT:   recurring in shadow-tower and Koszul chapters; Wave 10 CG sweep.
- REGEX:    `T\^c\(\s*s\^\{-1\}\s*A\s*\)` (no `\bar` within the argument)

### B15. Bar complex with bare s (suspension) instead of s^{-1}
- WRONG:    `T^c(s A)`   or   `T^c(s\bar{A})`
- CORRECT:  `T^c(s^{-1} \bar{A})`
- WHY:      desuspension lowers degree; bar uses `s^{-1}`, NOT `s`. AP22/AP45.
- CAUGHT:   N6 audit, Wave 11-4.
- REGEX:    `T\^c\(\s*s\s+` (bare `s` followed by space, no `^{-1}`)

### B16. Desuspension sign inversion
- WRONG:    `|s^{-1} v| = |v| + 1`
- CORRECT:  `|s^{-1} v| = |v| - 1`
- WHY:      s^{-1} LOWERS degree; suspension raises it. AP22/AP45.
- CAUGHT:   multiple chapter prefaces.
- REGEX:    `\|s\^\{-1\}\s*v\|\s*=\s*\|v\|\s*\+\s*1`

### B17. eta(q) missing q^{1/24} prefactor
- WRONG:    `\eta(q) = \prod_{n\ge 1}(1-q^n)`
- CORRECT:  `\eta(q) = q^{1/24}\prod_{n\ge 1}(1-q^n)`
- WHY:      Dedekind eta includes the `q^{1/24}` modular weight shift. AP22/FM13.
- CAUGHT:   recurrent in modular/genus-1 prose.
- REGEX:    `\\eta\(q\)\s*=\s*\\prod`

## Part D -- summation boundaries and indices

### B18. W_N generator weight set off-by-one (top end)
- WRONG:    W_N strong generators at weights `{2, 3, \ldots, N+1}` (total N)
- CORRECT:  W_N strong generators at weights `{2, 3, \ldots, N}` (total N-1, including Virasoro T at weight 2)
- WHY:      W_N has N-1 strong generators, not N. AP79 analogue.
- CAUGHT:   N4 audit, Wave 11-2.
- REGEX:    `W_N[^$]*weights[^$]*\\\{2[^}]*N\s*\+\s*1\\\}`

### B19. Harmonic sum starting at j=1 then subtracting
- WRONG:    `H_N = \sum_{j=1}^{N-1} 1/j`
- CORRECT:  `H_N = \sum_{j=1}^{N} 1/j`
- WHY:      boundary error; evaluation at N=2 immediately catches this. AP116.
- CAUGHT:   recurrent in W_N chapter drafts.
- REGEX:    `H_N\s*=\s*\\sum_\{j=1\}\^\{N-1\}`

### B20. Catalan-number index shift
- WRONG:    `C_n` counts binary trees with n leaves
- CORRECT:  `C_n` counts binary trees with n+1 leaves (equivalently n internal nodes); `C_3 = 5` has 4 leaves.
- WHY:      the most common combinatorial off-by-one on A_infinity trees. AP133.
- CAUGHT:   multiple Stasheff discussions.
- REGEX:    `C_n[^$]*trees[^$]*with\s+n\s+leaves`

## Part E -- finite-dimensional data

### B21. E_8 fundamental dimension 779247 (not in the irreducible list)
- WRONG:    `779247` claimed as an E_8 fundamental dimension
- CORRECT:  `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`
- WHY:      `779247` is not any E_8 irreducible. FM5.
- CAUGHT:   N2 audit, Wave 10-8.
- REGEX:    `E_8[^$]*779247|779247[^$]*E_8`

### B22. sl_2 bar H^2 dimension stated as 6
- WRONG:    `\dim H^2(B(sl_2)) = 6`
- CORRECT:  `\dim H^2(B(sl_2)) = 5`
- WHY:      Aomoto/Orlik-Solomon count; explicit in CLAUDE.md constants list.
- CAUGHT:   recurrent; Wave 8 Koszul audit.
- REGEX:    `H\^2\([^)]*sl_2[^)]*\)\s*=\s*6`

### B23. Genus-2 stable graphs count stated as 6
- WRONG:    `6` stable boundary graphs at g=2
- CORRECT:  `7`
- WHY:      hand enumeration misses one. AP123.
- CAUGHT:   Wave 10 CohFT audit.
- REGEX:    `g\s*=\s*2[^$]*stable[^$]*graphs[^$]*=\s*6`

### B24. Bicoloured partition numbers replaced by triangular numbers
- WRONG:    coefficients of `1/\eta(q)^2` listed as `(1,3,6,10,\ldots)` (triangular)
- CORRECT:  `(1,2,5,10,20,\ldots)` (bicoloured partitions, OEIS A000712)
- WHY:      `1/\eta^r` coefficients are r-coloured partition numbers p_{-r}(n). AP135.
- CAUGHT:   Wave 10 modular audit.
- REGEX:    `1/\\eta\(q\)\^2[^$]*\(\s*1\s*,\s*3\s*,\s*6`

### B25. Koszul conductor K_BP = 2
- WRONG:    `K_{\mathrm{BP}} = 2`
- CORRECT:  `K_{\mathrm{BP}} = 196`
- WHY:      conflation with ghost constant `C_{(2,1)} = 2`. AP140.
- CAUGHT:   extremal W-algebra chapter.
- REGEX:    `K_\{\\mathrm\{BP\}\}\s*=\s*2\b`

## Part F -- scope, quantifier, and duality drift

### B26. Theorem D for all genera without uniform-weight tag
- WRONG:    `obs_g = \kappa \cdot \lambda_g`  (no tag, for all g)
- CORRECT:  `obs_g = \kappa \cdot \lambda_g`  `(UNIFORM-WEIGHT)` or `(ALL-WEIGHT, + \delta F_g^{\mathrm{cross}})`.
- WHY:      at g>=2 with multi-weight, the scalar formula fails by the cross-channel correction. AP32/FM8.
- CAUGHT:   Wave 11 overture audit, F1-C1 panel L176-179.
- REGEX:    `obs_g\s*=\s*\\kappa\s*\\cdot\s*\\lambda_g` (no UNIFORM-WEIGHT within 3 lines)

### B27. iff/biconditional in Koszul equivalents where only forward is proved
- WRONG:    `A \iff B`  (theorem statement, converse not proved)
- CORRECT:  `A \implies B`  with a subsequent Remark that the converse is conjectural.
- WHY:      AP36. Forward-direction drift into biconditional.
- CAUGHT:   Koszul 10+1+1 list; Wave 9 sweep.
- REGEX:    `\\iff|\\Leftrightarrow|\\Longleftrightarrow` (flag for manual review in theorems only)

### B28. Critical-level / abelian-limit conflation for affine KM
- WRONG:    `at k=0 the r-matrix vanishes and the algebra fails Koszulness`
- CORRECT:  `at k=0 the r-matrix vanishes and the algebra remains Koszul (abelian limit); at k=-h^\vee the centre jumps and Koszulness fails`
- WHY:      two distinct limits conflated. FM4.
- CAUGHT:   N1 audit, Wave 10-7, L818-821.
- REGEX:    `k\s*=\s*0[^.]*fail[^.]*Koszul` (manual review)

### B29. Variable n unbound in Theorem C^{E1}
- WRONG:    `\mathrm{obs}_g = \kappa \cdot \lambda_g + \delta^{\mathrm{cross}}_n`  (LHS has g, RHS has n free)
- CORRECT:  fully quantify n: `\forall n` with `2g-2+n > 0`.
- WHY:      free variable makes the theorem ill-formed. AP139.
- CAUGHT:   Theorem C^{E1} statement.
- REGEX:    manual (structural)

## Part G -- macros, labels, environments

### B30. `\end{definition>` LaTeX structural typo
- WRONG:    `\end{definition>`
- CORRECT:  `\end{definition}`
- WHY:      `>` instead of `}`; survives visual inspection, fails at compile. FM7.
- CAUGHT:   N2 audit, Wave 10-8 (Vol I overture).
- REGEX:    `\\end\{[^}]*>`

### B31. `\begin{...>` variant of the same typo
- WRONG:    `\begin{theorem>`
- CORRECT:  `\begin{theorem}`
- WHY:      same as B30 but on the opening brace.
- CAUGHT:   inferred from B30; occasional co-occurrence.
- REGEX:    `\\begin\{[^}]*>`

### B32. Undefined `\cW` in standalone extractions
- WRONG:    `\cW` used in a standalone `.tex` whose preamble lacks the macro
- CORRECT:  add `\providecommand{\cW}{\mathcal{W}}` to the standalone preamble.
- WHY:      monograph macros not inherited by arXiv extractions. FM6.
- CAUGHT:   N6 audit, Wave 11-4.
- REGEX:    grep `\\cW` in standalone, cross-check preamble for `providecommand{\\cW}`.

### B33. Hardcoded `Part~IV` or `Chapter~12`
- WRONG:    `Part~IV`, `Chapter~12`
- CORRECT:  `\ref{part:examples}`, `\ref{chap:foo}`
- WHY:      hardcoded numerals break silently on reorganisation. V2-AP26/FM10.
- CAUGHT:   Vol II Part VI reorg; multiple chapter prefaces.
- REGEX:    `Part~[IVX]+|Chapter~[0-9]+`

### B34. Duplicate `conj:kappa-bps-universality` across Vol I and Vol III
- WRONG:    `\label{conj:kappa-bps-universality}` in both Vol I and Vol III
- CORRECT:  volume suffix, e.g. `conj:kappa-bps-universality-v3`.
- WHY:      cross-volume duplicate labels silently misdirect refs. AP124/FM15.
- CAUGHT:   Wave 9-7.
- REGEX:    cross-volume grep for identical `\label{...}`

### B35. Label prefix `thm:` on a `\begin{conjecture}` environment
- WRONG:    `\begin{conjecture} \label{thm:foo} ... \end{conjecture}`
- CORRECT:  `\begin{conjecture} \label{conj:foo} ... \end{conjecture}`
- WHY:      status/prefix mismatch after downgrade. AP125/FM14.
- CAUGHT:   rectify-all sweep.
- REGEX:    `\\begin\{conjecture\}[^$]*\\label\{thm:` (multiline, within 5 lines of the begin)

### B36. Bibliography item `\cite{GeK98}` without bibitem
- WRONG:    `\cite{GeK98}` in Survey v2 with no `\bibitem{GeK98}` present
- CORRECT:  add Getzler-Kapranov 1998 bibitem to the bibliography.
- WHY:      dangling `\cite` emits `[?]` at compile. AP28-style.
- CAUGHT:   Survey v2 audit, Wave 11-5.
- REGEX:    grep `\\cite\{([^}]+)\}` cross-check against `\\bibitem\{...\}`.

## Part H -- numerical coefficients

### B37. F_2 value 1/5760 or 7/2880 (wrong prefactor)
- WRONG:    `F_2 = 1/5760`  or  `F_2 = 7/2880`
- CORRECT:  `F_2 = 7/5760`
- WHY:      dimensional-reconstruction without source lookup. FM21.
- CAUGHT:   Wave 11 overture audit.
- REGEX:    `F_2\s*=\s*(1/5760|7/2880)`

### B38. Cauchy integral normalisation missing i
- WRONG:    `\frac{1}{2\pi}\oint \cdots dz`
- CORRECT:  `\frac{1}{2\pi i}\oint \cdots dz`
- WHY:      missing i gives zero for real coefficients; sanity check F_1 = kappa/24. AP120.
- CAUGHT:   recurring in genus-1 prose.
- REGEX:    `\\frac\{1\}\{2\\pi\}\\oint`

### B39. r-matrix k=0 non-vanishing check failed
- WRONG:    `r(z)` formula that does not vanish at k=0 for affine KM
- CORRECT:  every KM r-matrix must satisfy `r(z)|_{k=0} = 0`.
- WHY:      the level k=0 limit is abelian; the KM r-matrix must reduce to 0. AP126/AP141.
- CAUGHT:   every AP126 instance.
- REGEX:    manual (semantic); protocol is to substitute k=0 after every r-matrix.

## Part I -- modality and LaTeX hygiene

### B40. Markdown modality in LaTeX (backticks, asterisks, underscores)
- WRONG:    `` `29` `` (backticks), `**bold**`, `_italic_`
- CORRECT:  `$29$`, `\textbf{bold}`, `\emph{italic}`
- WHY:      LaTeX does not render Markdown; backticks become literal. AP121.
- CAUGHT:   recurring across all prose agents.
- REGEX:    `` `[^`]+` `` in `.tex` files; `\*\*[^*]+\*\*`; `(?<![a-zA-Z])_[^_]+_(?![a-zA-Z])`

### B41. Em-dash in prose
- WRONG:    text `---` text or `—` (Unicode em dash)
- CORRECT:  colon, semicolon, or two sentences.
- WHY:      prose-law violation; em dashes forbidden across the programme.
- CAUGHT:   Wave 8 prose fortification.
- REGEX:    `---|—`

### B42. AI slop vocabulary
- WRONG:    any of `notably, crucially, remarkably, interestingly, furthermore, moreover, delve, leverage, tapestry, cornerstone`
- CORRECT:  rewrite without them.
- WHY:      prose-law violation.
- CAUGHT:   Wave 8 prose fortification.
- REGEX:    `\b(notably|crucially|remarkably|interestingly|furthermore|moreover|delve|leverage|tapestry|cornerstone)\b`

## Part J -- depth/dimension/fiber-base

### B43. d_alg(Vir) stated as finite
- WRONG:    `d_{\mathrm{alg}}(\mathrm{Vir}) = 3`
- CORRECT:  `d_{\mathrm{gen}}(\mathrm{Vir}) = 3`, `d_{\mathrm{alg}}(\mathrm{Vir}) = \infty` (class M).
- WHY:      generating depth vs algebraic depth conflation. AP131/FM18.
- CAUGHT:   G/L/C/M classification discussion.
- REGEX:    `d_\{\\mathrm\{alg\}\}\(\\mathrm\{Vir\}\)\s*=\s*3`

### B44. Bare `d(Vir) = 3` without subscript
- WRONG:    `d(\mathrm{Vir}) = 3`
- CORRECT:  `d_{\mathrm{gen}}(\mathrm{Vir}) = 3`
- WHY:      ambiguous depth type. AP131.
- CAUGHT:   depth classification rewrites.
- REGEX:    `d\(\\mathrm\{Vir\}\)\s*=`

### B45. ChirHoch virtual dimension vs cohomological amplitude
- WRONG:    `\mathrm{vdim}\,\mathrm{ChirHoch}^*(A) = 2`
- CORRECT:  `\mathrm{ChirHoch}^*(A)` has cohomological amplitude `[0,2]` (topological), not virtual dimension 2 (arithmetic).
- WHY:      amplitude != vdim. AP134/FM17.
- CAUGHT:   shadow-tower rectification.
- REGEX:    `vdim\s*\\mathrm\{ChirHoch\}`

### B46. omega_g equated to a form on the fibre
- WRONG:    `\omega_g = d\tau`
- CORRECT:  `\omega_g = c_1(\lambda)` on `\bar{\mathcal{M}}_g`; `d\tau` is a form on the elliptic curve, not a class on moduli.
- WHY:      fiber-base confusion. AP130/FM19.
- CAUGHT:   Wave 11 F1-M3 genus-1 curvature audit.
- REGEX:    `\\omega_g\s*=\s*d\s*\\tau`

## Part K -- degenerate identities and grading

### B47. Degenerate graded Jacobi at even suspended degree
- WRONG:    `[m,[m,f]] = \tfrac12 [[m,m],f]` used at `||m||` even
- CORRECT:  at even `||m||`, `[[m,m],f] = 0` tautologically; the `1/2` trick requires `||m||` odd.
- WHY:      parity-dependent identity. AP138.
- CAUGHT:   curved A-infinity discussion, Wave 10 CG.
- REGEX:    manual (context-dependent).

### B48. Curved A-inf with m_0 treated as non-commuting derivation
- WRONG:    `m_1^2 = 0` asserted universally
- CORRECT:  in curved A-infinity, `m_1^2(a) = [m_0, a]`; the square is non-zero unless `m_0 = 0`.
- WHY:      confuses curved with uncurved. AP46.
- CAUGHT:   Wave 8 curved A-inf chapter.
- REGEX:    `m_1\^2\s*=\s*0`

### B49. Bar d^2 = 0 conflated with d_fib^2 = kappa * omega_g
- WRONG:    `d^2 = \kappa \cdot \omega_g`  stated as the bar differential
- CORRECT:  `d^2_{\mathrm{bar}} = 0` always; `d^2_{\mathrm{fib}} = \kappa \cdot \omega_g` is the FIBERWISE statement at g>=1.
- WHY:      two different differentials. AP46/AP87.
- CAUGHT:   Wave 8 MC3 audit.
- REGEX:    `d\^2\s*=\s*\\kappa\s*\\cdot\s*\\omega_g` (flag for context: is this bar or fiberwise?)

## Part L -- promotion and sector hygiene

### B50. SC mixed-sector dimension formula
- WRONG:    `\dim \mathrm{SC}^{\mathrm{mix}}_{k,m} = (k-1)! \cdot m!`
- CORRECT:  `(k-1)! \cdot \binom{k+m}{m}`
- WHY:      factorial of m is wrong; binomial is correct. AP89.
- CAUGHT:   Vol II SC swarm, Wave 7 SC bar.
- REGEX:    `\\dim[^$]*\\mathrm\{SC\}[^$]*=\s*\(k-1\)!\s*\\cdot\s*m!`

### B51. B_{SC}(A) for one-colour input
- WRONG:    `B_{\mathrm{SC}}(A)` applied to a single-colour algebra
- CORRECT:  SC is two-coloured; use promotion `A \mapsto (A, A)` and write `B_{\mathrm{SC}}(A, A)` with the open/closed structure.
- WHY:      SC requires two colours; one-colour is ill-formed. AP86.
- CAUGHT:   Vol II Part II open-closed chapter.
- REGEX:    manual (structural).

---

# Hook vs manual review

**Candidates for automatic hook (regex-matchable, low false-positive):**

- B1 (r-matrix `\Omega/z`): `r\(z\)\s*=\s*\\Omega\s*/\s*z` -- AP126 enforcement. Highest priority.
- B2, B3 (Vir r-matrix pole): literal patterns, trivial.
- B5, B6 (bc/βγ swap): literal polynomial patterns.
- B7 (W_N H_{N-1}): literal.
- B10 (kappa = S_2/2): literal.
- B12 (bare `\kappa` in Vol III): `\\kappa(?!_)` restricted to Vol III path. Needs allowlist for legitimate display cases.
- B13 (non-approved kappa subscripts): literal set.
- B14 (T^c(s^{-1} A) missing bar): `T\^c\(\s*s\^\{-1\}\s*A\s*\)` (no `\bar`).
- B15 (bare s in T^c): literal.
- B16 (desuspension sign inversion): literal.
- B17 (eta missing q^{1/24}): literal.
- B19 (H_N = sum to N-1): literal.
- B22 (sl_2 bar H^2 = 6): literal.
- B24 (bicoloured vs triangular): literal sequence check.
- B25 (K_BP = 2): literal.
- B30, B31 (LaTeX `{...>`): `\\end\{[^}]*>` / `\\begin\{[^}]*>`. Near-zero false positive.
- B33 (hardcoded Part~IV): `Part~[IVX]+|Chapter~[0-9]+`.
- B37 (F_2 wrong): literal.
- B38 (Cauchy missing i): literal.
- B40 (Markdown in LaTeX): backticks/asterisks/underscores. Already partly enforced as AP121.
- B41 (em dash): trivial.
- B42 (AI slop): word-list grep.
- B44 (bare d(Vir)): literal.
- B45 (vdim ChirHoch): literal.
- B46 (omega_g = dtau): literal.
- B48 (m_1^2 = 0): literal.
- B50 (SC mixed sector): literal.

**Requires manual review (semantic or context-dependent):**

- B4 (d-log r-matrix no-k): regex catches most, manual for edge cases.
- B8 (kappa = c/2 unqualified): needs Virasoro context check.
- B9 (kappa+kappa'=0 unscoped): always scoped in correct writing; regex flags for review.
- B11 (Sugawara shift missing): depends on whether the family is abelian.
- B18 (W_N weight set): regex brittle; manual.
- B20 (Catalan index): prose-level; manual.
- B23 (g=2 stable graphs = 6): literal but rare; manual.
- B26 (obs_g UNIFORM-WEIGHT tag): regex must check "within 3 lines"; harness-dependent.
- B27 (iff drift): always flag all `\iff` in theorems; manual review.
- B28 (k=0 vs k=-h^v): semantic.
- B29 (unbound n): structural; manual.
- B32 (standalone undefined macros): cross-file check; requires preamble parse.
- B34 (cross-volume duplicate labels): cross-volume grep; harness-level.
- B35 (label prefix vs environment): requires multiline match within environment scope.
- B36 (dangling \cite): requires bibitem parse.
- B39 (k=0 substitution): semantic protocol.
- B43 (d_alg(Vir) = 3): literal catches the obvious form; variants are semantic.
- B47 (degenerate Jacobi): parity context; manual.
- B49 (d^2 = kappa * omega_g): needs bar-vs-fiberwise disambiguation.
- B51 (one-colour SC): structural.

---

# Provenance notes

- Entries B1-B51 are drawn from: the Wave-12 failure-modes file (`opus_46_failure_modes_wave12.md`); the AP catalogue AP1-AP141 in `/Users/raeez/chiral-bar-cobar/CLAUDE.md`; Wave 7-11 audit reports in `/Users/raeez/chiral-bar-cobar/compute/audit/`; and the concordance constitution.
- Every entry has an AP number or a wave/agent source; none are speculative.
- Uncertain "correct form" entries (flagged for user review): B9 (the W_N complementarity constant `\rho_N K_N` has multiple conventions; verify against `landscape_census.tex`), B25 (K_BP = 196 assumes the ghost normalisation in Vol I Part V; verify convention).
- Entries B50 and B51 depend on the Vol II SC convention (two-coloured operad with promotion); do not propagate to Vol I without reinterpretation.

# End of blacklist
