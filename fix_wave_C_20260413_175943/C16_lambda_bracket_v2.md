# C16_lambda_bracket_v2 (575s)

**Findings**
- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1849): the Virasoro paragraph mixed the correct Vol II formula `\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3` with the alternate display `(c/2)\lambda^{(3)}`, which reintroduces the OPE coefficient into the lambda-bracket surface. EXACT edit applied: replaced that clause with `the OPE mode T_{(3)}T = c/2 therefore contributes (c/2)/3! = c/12 to the cubic \lambda-term`.

- PROBLEM at [compute/lib/genus2_ordered_bar.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_ordered_bar.py:22): the module described `c_n` as lambda-bracket coefficients, then later used `c_3 = c/2` as an OPE mode, so the convention was internally inconsistent. EXACT edit applied: changed the generic convention to `a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!`, rewrote the Virasoro display at line 633 to `{T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3`, and relabeled the stored data strings at lines 661-663 as `T_(0)T`, `T_(1)T`, `T_(3)T` OPE modes.

- PROBLEM at [compute/genus_tower_catalan.py](/Users/raeez/chiral-bar-cobar-vol2/compute/genus_tower_catalan.py:187): the note explicitly stated the wrong Virasoro lambda-bracket `{T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3`, then corrected itself later, leaving the convention surface contradictory. EXACT edit applied: replaced that block with the single consistent statement `{T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3`, followed by the OPE-mode explanation `T_{(3)}T = c/2` and the divided-power expansion `sum_n T_{(n)}T * lambda^n / n!`; also fixed the later generic comment at line 634 from `sum_n c_n * lambda^n` to `sum_n c_n * lambda^n / n!`.

- PROBLEM at [compute/lib/examples/virasoro.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/examples/virasoro.py:234): the explanatory lambda-bracket line still displayed the intermediate mixed form `(c/2)*lam^3/6`. EXACT edit applied: collapsed it to the Vol II form `= dT + 2T*lam + (c/12)*lam^3`, keeping the next sentence as the OPE-to-bracket conversion explanation.

- PROBLEM at [compute/tests/test_spectral_braiding.py](/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_spectral_braiding.py:390): the test docstring advertised the lambda-bracket as `... + (c/2)*lam^3/3!`, which is mathematically equivalent but not the repo’s declared Vol II convention. EXACT edit applied: changed it to `lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3` and kept the conversion note on the next line: `because (c/2)/3! = c/12`.

**Verification**
- `rg` found no remaining `'(c/2)*lambda^3'`, `'(c/2)*lam^3'`, or `'lambda^{(3)}'` spellings on the checked Vol II manuscript/compute surface.
- `python3 -m py_compile` passed for the touched Python files.
- Remaining `c_3 = c/2` hits are OPE-mode conversion comments in tests, not lambda-bracket formulas.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar-vol2
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d87d0-38dd-7bc3-87b6-2d630ce4504c
--------
user
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>


Fix lambda-bracket divided-power convention in Vol II (V2-AP34).
Search for lambda-bracket formulas. Must use divided powers: c/12 (not c/2) for Virasoro.
{T_lambda T} = (c/12)*lambda^3. Fix any incorrect conventions.
mcp startup: no servers

thinking
**Planning updates**

I think I need to use an update plan. It's worth doing a commentary update as well, since I might want to clarify or adjust my approach. There’s a lot to keep in mind, and planning may help streamline my thoughts and actions. I wonder if I'm on the right track with this! I want to ensure everything is organized and clear moving forward.
codex
Target is the Vol II lambda-bracket convention surface, specifically V2-AP34 and any live formulas using `{T_\lambda T}`. I’m reading the formula-verification and propagation workflows, then I’ll grep the manuscript for lambda-bracket formulas and patch only the incorrect convention instances.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-formula-verification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
---
name: vol2-cross-volume-propagation
description: Use after any mathematical wording, status, or formula change that may appear elsewhere in Vol II, Vol I, Vol III, superseded split files, notes, or compute layers. Do not use for isolated edits that cannot plausibly propagate.
---

# Vol II Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Search surface

After a load-bearing change, inspect:

- active Vol II chapter files
- active Vol II appendices
- superseded split files that still advertise the same claim
- `~/chiral-bar-cobar`
- `~/calabi-yau-quantum-groups` when the bridge is genuinely cross-volume
- `compute/` and `compute/tests/`

 succeeded in 51ms:
---
name: vol2-formula-verification
description: Use when verifying or repairing a formula, coefficient, invariant, table entry, generating function, spectral sequence page, test oracle, or convention bridge in Vol II. Do not use for purely prose edits with no mathematical payload.
---

# Vol II Formula Verification

Every load-bearing formula should survive at least three independent attacks.

## Verification paths

Use at least three when feasible:

1. direct computation from the definition
2. alternative but equivalent formula
3. limiting or special case
4. symmetry, duality, or reduction
5. cross-family or functorial consistency
6. literature comparison with normalization check
7. degree, weight, sign, or units analysis
 succeeded in 51ms:
 M Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
 M Makefile
 M README.md
 M chapters/connections/conclusion.tex
 M chapters/connections/concordance.tex
 M chapters/connections/hochschild.tex
 M chapters/connections/line-operators.tex
 M chapters/connections/ordered_associative_chiral_kd.tex
 M chapters/connections/ordered_associative_chiral_kd_core.tex
 M chapters/connections/ordered_associative_chiral_kd_frontier.tex
 M chapters/connections/relative_feynman_transform.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/connections/thqg_line_operators_extensions.tex
 M chapters/connections/ym_synthesis.tex
 M chapters/connections/ym_synthesis_core.tex
 M chapters/examples/examples-worked.tex
 M chapters/examples/rosetta_stone.tex
 M chapters/frame/preface.tex
 M chapters/frame/preface_trimmed.tex
 M chapters/theory/equivalence.tex

thinking
**Assessing file modifications**

I need to be careful about the dirty worktree and only edit the files I've been assigned. It seems like I need to identify the scope as it likely involves multiple files. I should check for any existing modifications in the files I may edit to avoid overwriting anything. Maybe I can use a search tool like `rg` across the repository, looking for specific formulas. I should read the relevant target files and any existing diffs and then use an update plan with clear steps. Let's get a plan together!
codex
I have the verification and propagation rules loaded. Next I’m searching the live Vol II surface for lambda-bracket variants and central-term normalizations, with extra care on already-dirty files so I only make minimal truthful edits.
Plan update
Adversarial audit + fix pass for the Vol II divided-power lambda-bracket convention.
  → Search the active Vol II surface for lambda-bracket formulas and central-term variants involving Virasoro/T lambda T.
  • Inspect each hit in context, distinguish correct divided-power usage from OPE-mode formulas, and identify only genuine Vol II convention violations.
  • Apply minimal edits to incorrect live instances and verify no contradictory copies remain in scope.
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.toc'"' --glob '"'!*.out'"' --glob '"'!*.bbl'"' --glob '"'!*.blg'"' '\\\\{T_\\\\lambda T\\\\}|T_\\\\lambda T|lambda-bracket|lambda bracket|\\\\lambda\\\\"'^3|c/2|c/12'"' ." in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.toc'"' --glob '"'!*.out'"' --glob '"'!*.bbl'"' --glob '"'!*.blg'"' 'V2-AP34|divided powers|a_\\(n\\)b / n"'!|a_'"\\{\\(n\\)\\}b|\\\\{L_\\\\lambda L\\\\}|\\\\{T_\\\\lambda T\\\\}' AGENTS.md CLAUDE.md chapters working_notes.tex README.md compute .agents" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:\\{T_\\lambda T\\}|T_\\lambda T|lambda-bracket|lambda bracket|\\lambda\\^3|c/2|c/12)
          ^
error: repetition quantifier expects a valid decimal
 exited 2 in 51ms:
rg: regex parse error:
    (?:V2-AP34|divided powers|a_\(n\)b / n!|a_\{\(n\)\}b|\\{L_\\lambda L\\}|\\{T_\\lambda T\\})
                                                            ^
error: repetition quantifier expects a valid decimal

thinking
**Considering regex patterns**

I'm thinking about whether I need a fixed string or perhaps multiple regex patterns. Using `-F` or escaping characters might be an option. It could make sense to create separate patterns with the `-e` flag. That might help me clarify the different matches I want to achieve. I just need to ensure I'm organizing my thought process correctly here to avoid unnecessary confusion. Let's figure this out step by step!
codex
The first grep tripped on TeX braces in the regex, so I’m rerunning with fixed-string searches and narrower symbolic variants. After that I’ll inspect each hit in-file before editing.
exec
/bin/zsh -lc "rg -n -F --hidden --glob '"'!*.pdf'"' --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.toc'"' --glob '"'!*.out'"' --glob '"'!*.bbl'"' --glob '"'!*.blg'"' -e 'V2-AP34' -e 'divided powers' -e 'a_(n)b / n"'!'"' -e '{L_\\lambda L}' -e '{T_\\lambda T}' AGENTS.md CLAUDE.md chapters working_notes.tex README.md compute .agents" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F --hidden --glob '"'!*.pdf'"' --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.toc'"' --glob '"'!*.out'"' --glob '"'!*.bbl'"' --glob '"'!*.blg'"' -e '{T_\\lambda T}' -e 'T_\\lambda T' -e 'lambda-bracket' -e 'lambda bracket' -e '\\lambda"'^3'"' -e 'c/2' -e 'c/12' ." in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
AGENTS.md:546:   `AP126`, `V2-AP34`, `AP44`, `AP45`, `AP46`, `AP49`, and `AP113` recur across manuscript and compute layers.
AGENTS.md:602:- Vol II lambda-brackets use divided powers;
AGENTS.md:746:- Vol II uses lambda-brackets with divided powers;
CLAUDE.md:216:V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
.agents/skills/vol2-formula-verification/SKILL.md:28:- Vol II lambda-brackets use divided powers: the order-`n` coefficient is `a_(n)b / n!`.
.agents/skills/vol2-compute-engine/SKILL.md:40:- `V2-AP34`: lambda-bracket coefficients use divided powers.
.agents/skills/vol2-cross-volume-propagation/SKILL.md:38:- Vol II uses lambda-brackets with divided powers.
compute/lib/pva_descent_coefficients_engine.py:35:divided-power central term, V2-AP34).
compute/lib/pva_descent_coefficients_engine.py:45:V2-AP34: Virasoro lambda-bracket uses divided-power central term
compute/lib/pva_descent_coefficients_engine.py:673:    so the polynomial lambda-bracket (divided-power / V2-AP34) is
compute/lib/pva_descent_coefficients_engine.py:678:    the divided-power convention at V2-AP34 in the Vol II CLAUDE.md.
compute/tests/test_pva_descent_coefficients_engine.py:21:    * V2-AP34 (divided-power lambda-bracket c/12 * lam^3)
compute/tests/test_pva_descent_coefficients_engine.py:161:    """Virasoro at central charge c; V2-AP34 divided-power convention."""
compute/tests/test_pva_descent_coefficients_engine.py:168:        Path B: Divided-power form of OPE (V2-AP34).  The c/2 mode
compute/tests/test_pva_descent_coefficients_engine.py:176:        # Explicit V2-AP34 guardrail: refuse the wrong c/2 * lam^3 form.
chapters/theory/pva-descent.tex:126:recording the same OPE coefficients $a_{(n)}b$ via divided powers $\lambda^{(n)} = \lambda^n/n!$.
 succeeded in 51ms:
Total output lines: 1900

./CLAUDE.md:163:- PVA is (-1)-shifted: lambda-bracket on H*(A,Q) has shifted parity.
./CLAUDE.md:216:V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
./FRONTIER.md:214:The paper that constructed the 3d holomorphic-topological Poisson sigma model from a PVA lambda-bracket. Its gauge invariance condition is the lambda-Jacobi identity, which is d^2_B = 0 via the Arnold relation. Its sigma-model coupling 1/(k+h^v) is the same scalar as the DNP loop parameter and the collision-residue prefactor. The remaining gap: half-space quantization at the chain level.
./FRONTIER.md:338:- **Conformal anomaly = c/2 = kappa**: quantitative obstruction to constant coproduct. At c=0 constant exists; c≠0 forces spectral parameter.
./main.tex:1421:$\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$
./main.tex:1424:involution $c \mapsto 26 - c$, the curvature $\kappa = c/2$, and the
./appendices/pva-expanded.tex:8:\noindent\textbf{Standing notation.} Throughout, $[a],[b],[c]\in H$ denote cohomology classes with representatives $a,b,c\in \A$. The cohomological degree of $a$ is written $\degree{a}$. The product and bracket are defined from the regular/singular decomposition of $m_2$ as in Definition~\ref{def:product} and Definition~\ref{def:lambda-bracket}:
./compute/w3_shadow_coefficients.py:10:  Hessian: kappa = diag(c/2, c/3)
./compute/w3_shadow_coefficients.py:540:    # h_2(a,b) = 2*[(c/2)*a^2 + (c/3)*b^2] = c*a^2 + (2c/3)*b^2
./compute/w3_shadow_coefficients.py:543:    # Sh_2^{Vir} = S_2^{Vir} * x_T^2 = (c/2)*x_T^2.
./compute/e1_arithmetic_complete.py:521:    # chi_h(q) = q^{h - c/24} / prod(1-q^n)
./chapters/examples/w-algebras-stable.tex:74:% label removed: eq:vir-lambda-bracket
./chapters/examples/w-algebras-stable.tex:75:\{T_\lambda T\} = \partial T + 2T\lambda + \frac{c}{12}\lambda^3.
./chapters/examples/w-algebras-stable.tex:80:The $\lambda^3$ term arises from the Schwarzian derivative in the transformation law
./chapters/examples/w-algebras-stable.tex:115:We verify $Q^2 = 0$ on each generator. The inputs are the Virasoro $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2\lambda T + \frac{c}{12}\lambda^3$ and the ghost OPE $\{(c_{\mathrm{gh}})_\lambda c_{\mathrm{gh}}\} = 0$, $\{(c_{\mathrm{gh}})_\lambda \mu\} = -1$.
./chapters/examples/w-algebras-stable.tex:119:\emph{On $T$:} $Q(T) = \partial T \cdot c_{\mathrm{gh}} + 2T\partial c_{\mathrm{gh}} + \frac{c}{12}\partial^3 c_{\mathrm{gh}}$. Computing $Q^2(T)$ requires applying $Q$ to each term and using the Leibniz rule. The result is a polynomial in $T, c_{\mathrm{gh}}, \mu$ and their derivatives. The cancellation follows from the Jacobi identity for the $\lambda$-bracket: the coefficient of each monomial in $Q^2(T)$ is a specific linear combination of structure constants of $\{T_\lambda T\}$, and the Jacobi identity $\{T_\lambda \{T_\mu T\}\} - \{T_\mu \{T_\lambda T\}\} = \{\{T_\lambda T\}_{\lambda+\mu} T\}$ ensures these cancel. This is a standard calculation in BRST cohomology; see~\cite{FMS86}.
./chapters/examples/w-algebras-stable.tex:136:The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
./chapters/examples/w-algebras-stable.tex:138:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
codex
The broad search confirms the convention note is present; now I’m narrowing to actual violations: lines where a lambda-bracket, lambda-polynomial, or its explanatory prose still carries OPE coefficients like `c/2` against `\lambda^3`. Those are the only places I’ll touch.
exec
/bin/zsh -lc "rg -n -F --hidden --glob '"'!*.pdf'"' --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.toc'"' --glob '"'!*.out'"' --glob '"'!*.bbl'"' --glob '"'!*.blg'"' -e '{T_\\lambda T} = ' -e '{T {}_\\lambda T} = ' -e '{T_\\lambda T}\\=' -e 'm_2(T,T; lambda) =' -e 'm_2(T,T;\\lambda) =' chapters compute main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.toc'"' --glob '"'!*.out'"' --glob '"'!*.bbl'"' --glob '"'!*.blg'"' '(c/2["'^'"\\n]{0,120}lambda\\"'^3|lambda'"\\"'^3[''^'"\\n]{0,120}c/2|c/3["'^'"\\n]{0,120}lambda\\"'^5|lambda'"\\"'^5[''^'"\\n]{0,120}c/3)' chapters compute main.tex working_notes.tex README.md CLAUDE.md AGENTS.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
working_notes.tex:7842:defines $m_2(T,T;\lambda) = \{T{}_\lambda T\}$.  The quartic OPE
chapters/examples/w-algebras-stable.tex:363:$m_2(T,T;\lambda) = \{T_\lambda T\} = \partial T + 2T\lambda + \tfrac{c}{12}\lambda^3$.
chapters/examples/w-algebras.tex:275:$m_2(T,T;\lambda) = \{T_\lambda T\} = \partial T + 2T\lambda + \tfrac{c}{12}\lambda^3$.
chapters/examples/w-algebras-virasoro.tex:271:On cohomology, with $m_2(T,T;\lambda) = \{T_\lambda T\} = \partial T + 2T\lambda + \tfrac{c}{12}\lambda^3$, the left-hand side is the \emph{PVA associator}. By the PVA Jacobi identity, this associator equals $-\{T_{\lambda_2}\{T_{\lambda_1} T\}\}$: it is nonzero but determined by the bracket. The chain-level $m_3$ lives in the full BV-BRST complex (involving the ghost field $\mu$); its projection to cohomology is the transferred operation $m_3^H$.
compute/genus_tower_catalan.py:193:      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
compute/genus_tower_catalan.py:198:      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
 succeeded in 51ms:
CLAUDE.md:216:V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
chapters/examples/w-algebras-w3.tex:522:$P_5\,\lambda^5 = (c/360)\lambda^5$ is a scalar multiple
chapters/examples/w-algebras-w3.tex:817:r^{WW}(\lambda,\mu) &= \frac{c/360}{\lambda^5 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{3\lambda^3 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{2\lambda^2 \mu} \\
chapters/examples/w-algebras-w3.tex:1934:$1/z^5$ & $c/360$ (from $\lambda^5$)
chapters/examples/w-algebras-frontier.tex:142:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-frontier.tex:559:r^{W_3 W_3}(\lambda) &= \frac{c/360}{\lambda^5}
chapters/examples/w-algebras-conditional.tex:184:r^{WW}(\lambda,\mu) &= \frac{c/360}{\lambda^5 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{3\lambda^3 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{2\lambda^2 \mu} \\
chapters/examples/w-algebras-conditional.tex:528:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-conditional.tex:766: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
chapters/examples/w-algebras.tex:831:r^{WW}(\lambda,\mu) &= \frac{c/360}{\lambda^5 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{3\lambda^3 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{2\lambda^2 \mu} \\
chapters/examples/w-algebras.tex:1176:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras.tex:1422: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
chapters/theory/introduction.tex:1849:equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
compute/lib/genus2_ordered_bar.py:633:      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
compute/tests/test_cross_volume_deep_bridge.py:110:        """The lambda^3 term gives c/2 at z^{-4}."""
compute/lib/cross_volume_deep_bridge.py:226:    {W_lambda W} = ... (c/360)*lambda^5 + lower order (nonlinear)
compute/lib/cross_volume_deep_bridge.py:241:            ('W', 'W'): {5: c / 360},  # leading: (c/3*5!)*lambda^5
compute/lib/cross_volume_deep_bridge.py:379:    """Verify leading WW bracket: {W_lambda W} has (c/360)*lambda^5 term.
compute/tests/test_pva_axioms.py:424:        Factor: c/2 * lambda^3 / 3! = c/2 * lambda^3 / 6 = c/12 * lambda^3.
chapters/connections/thqg_fm_calculus_extensions.tex:937: to $\lambda^3/3!$; multiplying by the OPE coefficient $c/2$
exec
/bin/zsh -lc "sed -n '930,944p' chapters/connections/thqg_fm_calculus_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1348,1360p' chapters/connections/thqg_fm_calculus_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '620,648p' compute/lib/genus2_ordered_bar.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1818,1860p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '180,206p' compute/genus_tower_catalan.py" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\]
The Borel transform converts each pole
$(z-w)^{-n-1}$ to $\lambda^n/n!$, giving:
\begin{itemize}
\item Sextic pole $c/3 \cdot (z-w)^{-6}$:
 the Borel transform sends $(z{-}w)^{-6} = (z{-}w)^{-(5+1)}$
 to $\lambda^5/5!$; multiplying by the OPE coefficient $c/3$
 gives $c/(3 \cdot 5!) = c/360$ as the $\lambda$-bracket
 coefficient of $\lambda^5$, matching the $m_2$ term
 $\frac{c}{360}\lambda^5$.
\item Quartic pole: the $\beta$-dependent piece
 $\beta \cdot 2T/(z{-}w)^4$ contributes
 $\beta \cdot 2T \cdot \lambda^3/3! = \beta \cdot
 succeeded in 52ms:
The Borel transform $(z-w)^{-n-1} \mapsto \lambda^n/n!$
applied to the OPE poles gives:
\begin{itemize}
\item Quartic pole $c/2 \cdot (z-w)^{-4}$:
 $\frac{c}{2} \cdot \frac{\lambda^3}{3!}
 = \frac{c}{12}\lambda^3$.
 (The Borel transform sends $(z{-}w)^{-4} = (z{-}w)^{-(3+1)}$
 to $\lambda^3/3!$; multiplying by the OPE coefficient $c/2$
 gives $c/12$ as the coefficient of $\lambda^3$,
 matching the
 $\lambda$-bracket~\eqref{eq:virasoro-lambda-bracket-ext}.: the divided-power convention absorbs $1/n!$.)
\item Double pole: $2T\lambda$.
\item Simple pole: $\partial T$.
\end{itemize}

 succeeded in 52ms:

    The genus-0 collision residue for Virasoro (post-d-log absorption, AP19):
      r^{(0)}(z) = (c/2)/z^3 + 2T/z + dT

    The genus-1 collision residue replaces rational poles by Weierstrass:
      r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)

    Wait -- let me be more careful. The Virasoro lambda-bracket is:
      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3

    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.

    The genus-0 m_2 in the bar complex is:
      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
                       = c_0 + c_1*lambda + c_3*lambda^3
    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).

    Wait no: from the code m2_num:
      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3

 succeeded in 52ms:
            'newton_polygon': {
                'ordinary': 'slopes = {0, 0, 1, 1} (ht = dim + dim = 2+2)',
                'supersingular': 'slopes = {1/2, 1/2, 1/2, 1/2} (ht = 2*dim = 4)',
                'generic': 'depends on the isogeny class of J(Sigma_2) over F_p',
            },
        },
    }


def genus2_r_matrix_virasoro(c_val=None) -> Dict[str, Any]:
    r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.

    The Virasoro lambda-bracket:
      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.

    The genus-2 r-matrix:
      r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)

    THREE sectors:
 succeeded in 52ms:
$R$-matrix is the exponential of the classical $r$-matrix. This
is the braided atom, the simplest family with nontrivial spectral
structure.

\subsection*{Affine $\widehat{\fg}_k$: the non-abelian test}

Affine $\widehat{\mathfrak{su}(2)}_k$ tests the full non-abelian
Swiss-cheese machine:
\begin{itemize}
\item $\lambda$-bracket:
 $\{J^a {}_\lambda J^b\} = f^{ab}_c J^c + k \delta^{ab} \lambda$,
 the affine Lie bracket.
\item $m_3 \neq 0$: from the cubic Casimir structure of the Jacobi
 identity. The $n = 3$ $\Ainf$ relation produces a nonvanishing
 $m_3$ whose chain-level existence is the homotopy for the failure
 of strict associativity in the Lie case.
\item Classical $r$-matrix: $r(z) = k\,\Omega / z$, where
 $\Omega = \sum_a J^a \otimes J^a$ is the Casimir element, the
 standard Lie-algebraic $r$-matrix at level~$k$.
\item Quantum $R$-matrix: on the reduced evaluation comparison surface in the affine lineage, the reduced HT monodromy is compared with the quantum-group braid representation and the spectral $R$-matrix agrees with the quantum group $R$-matrix of $U_q(\fg)$ at $q = e^{i\pi/(k+h^\vee)}$ (Theorem~\ref{thm:affine-monodromy-identification}).


thinking
**Searching for lambda-bracket issues**

I’m noticing that the compute documentation might be incorrect. I need to search more specifically for "The Virasoro lambda-bracket" and "c_3 = c/2," looking through all occurrences. It seems I’ll also want to consider the entire Volume II repository since the user asked about fixing the lambda-bracket divided-power convention. I’ll search chapters, compute files, and possibly even outdated split files. My goal is to identify where the lambda-bracket or its coefficients are wrong while avoiding unnecessary fixes to correct explanations.
thinking
**Verifying coefficient documentation**

I’m considering whether I should just adjust comments or docstrings. If the code logic already uses the correct coefficient, maybe only the documentation needs fixing. Yet, I need to confirm there are no issues with the logic itself. I plan to search for functions returning the c/2 coefficient in relation to the lambda bracket. I might use regex to find instances where “lambda-bracket” appears near “c/2,” or where assignments of c_3 = c/2 occur. It's essential to examine suspicious patterns thoroughly.
codex
I’ve isolated real convention drift in the compute/docs layer: a few docstrings and notes still state the Virasoro lambda-bracket with `c/2` and `c_3 = c/2`, even though nearby code uses `c/12`. I’m now scanning for every remaining `c_3 = c/2` or “lambda-bracket … c/2” variant before patching.
exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.toc'"' --glob '"'!*.out'"' --glob '"'!*.bbl'"' --glob '"'!*.blg'"' '(c_3\\s*=\\s*c/2|c_3 = c/2|\\(c/2\\)\\*lambda\\"'^3|'"\\(c/2\\)lambda\\"'^3|c/2'"\\)\\*lambda\\"'^3|c/2'"\\*lambda\\"'^3|c/2'"\\)\\lambda\\"'^3)'"' compute chapters working_notes.tex README.md main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' --glob '"'!*.aux'"' --glob '"'!*.log'"' --glob '"'!*.toc'"' --glob '"'!*.out'"' --glob '"'!*.bbl'"' --glob '"'!*.blg'"' '(lambda-bracket|lambda bracket|\\{T_lambda T\\}|\\{T_\\\\lambda T\\}|m_2\\(T,T; lambda\\)|m_2\\(T,T;\\\\lambda\\)|c_3\\s*=)' compute chapters working_notes.tex README.md main.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: PCRE2: error compiling pattern at offset 103: PCRE2 does not support \F, \L, \l, \N{name}, \U, or \u
 succeeded in 51ms:
README.md:35:- **VI. Three-Dimensional Quantum Gravity**: The climax; Virasoro lambda-bracket generates the full gravitational theory; critical string dichotomy c=26 vs c!=26
chapters/examples/w-algebras-stable.tex:74:% label removed: eq:vir-lambda-bracket
chapters/examples/w-algebras-stable.tex:136:The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
chapters/examples/w-algebras-stable.tex:164:Setting $\lambda = z_1 - z_2$ and extracting singular terms gives \eqref{eq:vir-lambda-bracket}.
chapters/examples/w-algebras-stable.tex:363:$m_2(T,T;\lambda) = \{T_\lambda T\} = \partial T + 2T\lambda + \tfrac{c}{12}\lambda^3$.
chapters/examples/w-algebras-stable.tex:382:using left-sesquilinearity $m_2(\partial T, T;\lambda) = -\lambda\, m_2(T,T;\lambda)$
chapters/examples/w-algebras-stable.tex:395:Using right-sesquilinearity $m_2(T,\partial T;\lambda) = (\lambda+\partial)\,m_2(T,T;\lambda)$:
chapters/examples/examples-complete-conditional.tex:82:\label{prop:su2-lambda-bracket}
chapters/examples/w-algebras-virasoro.tex:70:\label{eq:vir-lambda-bracket}
chapters/examples/w-algebras-virasoro.tex:132:The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
chapters/examples/w-algebras-virasoro.tex:163:Setting $\lambda = z_1 - z_2$ and extracting singular terms gives \eqref{eq:vir-lambda-bracket}.
chapters/examples/w-algebras-virasoro.tex:271:On cohomology, with $m_2(T,T;\lambda) = \{T_\lambda T\} = \partial T + 2T\lambda + \tfrac{c}{12}\lambda^3$, the left-hand side is the \emph{PVA associator}. By the PVA Jacobi identity, this associator equals $-\{T_{\lambda_2}\{T_{\lambda_1} T\}\}$: it is nonzero but determined by the bracket. The chain-level $m_3$ lives in the full BV-BRST complex (involving the ghost field $\mu$); its projection to cohomology is the transferred operation $m_3^H$.
chapters/examples/examples-complete.tex:543:% label removed: prop:su2-lambda-bracket
working_notes.tex:7842:defines $m_2(T,T;\lambda) = \{T{}_\lambda T\}$.  The quartic OPE
working_notes.tex:7893:  computation (the lambda-bracket sesquilinearity propagated
working_notes.tex:8212:$m_2(T,T;\lambda)$
working_notes.tex:8483:$c_3 = -\frac{2\pi^6}{945}E_6$.
working_notes.tex:11885:$\Delta c_3 = c_3(2,0) - c_3(0,1) = 5$.
working_notes.tex:15327:\item the binary operation $m_2(T,T;\lambda)
working_notes.tex:17136:  \Delta c_3 = c_3(2,0) - c_3(0,1)
exec
/bin/zsh -lc "sed -n '7836,7854p' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '15298,15338p' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F --hidden --glob '"'!*.pdf'"' '\\lambda"'^{(3)}'"' chapters working_notes.tex compute main.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$4$ & $c = -22/5$ & Lee--Yang edge singularity
  & $m_k$ for $k \ge 4$ \\
$6$ & $c = -68/7$ & next minimal model locus
  & $m_k$ for $k \ge 6$ \\
$n$ & Kac zeros at level~$n$ & & $m_k$ for $k \ge n$
\end{tabular}
\end{center}

\noindent
The full denominator of $m_k^H$ is the product of Kac
determinant factors at levels $\le k$:
\begin{equation}\label{eq:mk-denominator-wn}
D_k(c) \;=\;
\prod_{n=2}^{k}\;
\prod_{\substack{r,s \ge 1 \\ rs \le n}}
\bigl(h_{r,s}(c)\bigr)^{p(n - rs)}\bigg|_{h=0},
\end{equation}
where $h_{r,s}(c) = [(m(r^2-1) - n(s^2-1))^2 - (m-n)^2]/(4mn)$
with $c = 1 - 6(m-n)^2/(mn)$, and $p(j)$ is the
number of partitions of~$j$.
 succeeded in 51ms:
The Virasoro $\lambda$-bracket
\begin{equation}\label{eq:vir-lambda-wn2}
\{T{}_\lambda T\}
\;=\;
\partial T + 2T\lambda + \frac{c}{12}\,\lambda^3
\end{equation}
defines $m_2(T,T;\lambda) = \{T{}_\lambda T\}$.  The quartic OPE
pole ($\lambda^3$ in the $\lambda$-bracket) forces
non-associativity, compensated by
\[
m_3(T,T,T;\,\lambda_{12},\lambda_{23})
\;=\;
\partial^2 T
+ (2\lambda_{12} + 3\lambda_{23})\,\partial T
+ 2\lambda_{23}(2\lambda_{12} + \lambda_{23})\,T
+ \frac{c}{12}\,\lambda_{23}^3(2\lambda_{12} + \lambda_{23}).
\]
This section computes the next two operations $m_4$ and $m_5$
explicitly, by solving the Stasheff identity at arities $4$ and~$5$.
 succeeded in 51ms:
chapters/theory/introduction.tex:1849:equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
exec
/bin/zsh -lc "sed -n '1648,1670p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

\begin{theorem}[Finite presentation of the gravitational $\Ainf$
structure; \ClaimStatusProvedHere]
\label{thm:gravity-finite-presentation}
\index{finite presentation!gravitational A-infinity@gravitational $\Ainf$|textbf}
\index{resolvent tree formula!gravitational}
The Virasoro $\Ainf$ structure $\{m_k\}_{k \ge 2}$ is finitely
presented: every $m_k$ is uniquely determined by the two data
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item the binary operation $m_2(T,T;\lambda)
 = \partial T + 2T\lambda + (c/12)\lambda^3$
 \textup{(}the Virasoro $\lambda$-bracket\textup{)}, and
\item the BRST contracting homotopy $h$ from the
 Drinfeld--Sokolov reduction of\/ $\widehat{\mathfrak{sl}}_2$ at
 level~$k$.
\end{enumerate}
The determination is by the resolvent tree formula of
Proposition~\ref{prop:finite-presentation-general}:
$m_k$ is the sum over Catalan-many planar binary trees with $k$
leaves, internal edges decorated by~$h$, and internal vertices

thinking
**Adjusting code consistency**

I'm thinking that the actual code might be using `c_val / 12`, and it seems I need to ensure that the docstring reflects this accurately. It’s important for the documentation to match the code’s logic to avoid confusion. I should search within the file for instances of `c/12` to double-check and make any necessary adjustments. This way, everything stays clear and consistent for future reference!
codex
The manuscript search is clean on actual displayed Virasoro brackets except one mixed-notation sentence in the introduction. The remaining drift is in compute-facing documentation, where two modules still spell the lambda-bracket with OPE coefficients. I’m checking whether those are docstrings only or feed logic before I patch them.
exec
/bin/zsh -lc "sed -n '1,120p' compute/lib/genus2_ordered_bar.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'c_3' compute/lib/genus2_ordered_bar.py compute/genus_tower_catalan.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'c/12' compute/lib/genus2_ordered_bar.py compute/genus_tower_catalan.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'c / 12' compute/lib/genus2_ordered_bar.py compute/genus_tower_catalan.py" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
r"""Genus-2 ordered bar complex and r-matrix on Sigma_2.

THE BLEEDING EDGE OF THE GENUS TOWER.

At genus 0, the ordered bar complex lives on FM_k(C) x Conf_k(R), and
the spectral r-matrix is a rational function of the spectral parameter z.

At genus 1, the r-matrix deforms to an elliptic function on E_tau:
  rational 1/z -> Weierstrass zeta(z|tau),
  rational 1/z^2 -> Weierstrass -wp(z|tau), etc.
The modular parameter tau in H_1 (upper half-plane) controls the
geometry. The elliptic quantum group E_{q,p} of Felder is the
genus-1 quantum symmetry.

At genus 2, the curve is Sigma_2 with period matrix Omega in H_2
(Siegel upper half-space of degree 2). The propagator is the
SZEGO KERNEL / prime form on Sigma_2. The r-matrix involves:

  f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
  B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 exited 1 in 51ms:

 succeeded in 51ms:
compute/genus_tower_catalan.py:49:    Quartic (c/2): (c/12) * [wp''(z|tau)/6 - 1/z^4] at z -> 0
compute/genus_tower_catalan.py:50:                  = (c/12) * [G_4 + 10*G_6*z^2 + ...]
compute/genus_tower_catalan.py:58:    delta_m_2 = (c/12) * G_4 + [-dT*G_2 + 2T*3*G_4 + (c/12)*10*G_6 + ...]
compute/genus_tower_catalan.py:185:      r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
compute/genus_tower_catalan.py:193:      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
compute/genus_tower_catalan.py:195:    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
compute/genus_tower_catalan.py:198:      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
compute/genus_tower_catalan.py:201:    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
compute/genus_tower_catalan.py:754:    m_2^{eff}(T,T; λ) = (1 + 2λ + (c/12)λ³)     [genus-0]
compute/lib/genus2_ordered_bar.py:667:            1: '(c/12)*wp\'\'(z|tau) + 2T*wp(z|tau) + partial(T)*zeta(z|tau)',
 succeeded in 51ms:
compute/lib/genus2_ordered_bar.py:634:    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
compute/lib/genus2_ordered_bar.py:642:      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
compute/genus_tower_catalan.py:190:    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
compute/genus_tower_catalan.py:194:                       = c_0 + c_1*lambda + c_3*lambda^3
compute/genus_tower_catalan.py:201:    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
compute/genus_tower_catalan.py:664:    #   r(z) = c_0/z + c_1/z^2 + c_3/z^4  (genus-0 Virasoro r-matrix)
compute/genus_tower_catalan.py:762:      r^{(0)}(z) = c_0/z + c_1/z^2 + c_3/z^4
compute/genus_tower_catalan.py:766:      r^{(1)}(z;tau) = c_0·ζ(z|τ) + c_1·(-℘(z|τ)) + c_3·℘''(z|τ)/6
compute/genus_tower_catalan.py:769:      = c_0·[ζ(z)-1/z] + c_1·[-℘(z)+1/z^2] + c_3·[℘''(z)/6-1/z^4]

thinking
**Inspecting code functionality**

I should take a closer look at the genus2_ordered_bar function in the actual code — maybe it utilizes c_3? I’ll consider searching for the Virasoro lambda bracket function as well. It might help to use sed around the relevant area that's beyond the docstring. I want to ensure that I'm exploring all the right aspects and not missing anything important within the code. Let's inspect this carefully!
exec
/bin/zsh -lc "sed -n '648,684p' compute/lib/genus2_ordered_bar.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '150,190p' compute/lib/pva_descent_chain_level.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '748,776p' compute/genus_tower_catalan.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '384,416p' compute/tests/test_spectral_braiding.py" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
    GRAVITATIONAL INTERPRETATION:
    The genus-2 r-matrix for Virasoro is the perturbative vertex of 3d
    quantum gravity at genus 2. The quartic sector (c/4)*d_z^2 B(z,w)
    represents the graviton-graviton scattering amplitude on Sigma_2.
    The curvature kappa = c/2 enters via the Faber-Pandharipande number:
      F_2 = kappa * 7/5760 = 7c/11520
    """
    c = c_val if c_val is not None else Symbol('c')

    return {
        'algebra': f'Vir_{{{c}}}',
        'kappa': c / 2,
        'c0': 'partial(T) (derivative of stress tensor)',
        'c1': '2T (stress tensor)',
        'c3': 'c/2 (central charge / 2)',
        'regime': 'ENTANGLED (c_0 = partial(T) != 0)',

        'genus_tower': {
            0: '(c/2)/z^4 + 2T/z^2 + partial(T)/z',
            1: '(c/12)*wp\'\'(z|tau) + 2T*wp(z|tau) + partial(T)*zeta(z|tau)',
 succeeded in 52ms:
            source='J', target='J'
        ),
    }

    product = {('J', 'J'): Symbol('JJ')}
    partial = {'J': Symbol('dJ')}

    return PVAData(
        name='Heisenberg',
        generators=['J'],
        brackets=brackets,
        product=product,
        partial=partial,
    )


def virasoro_pva(c_val=None):
    """Virasoro PVA: {T_lam T} = dT + 2T*lam + (c/12)*lam^3.

    One generator T, conformal weight 2.
 succeeded in 52ms:

        Start from OPE coefficients, convert to lambda-bracket, then to r-matrix.
        The result should reproduce the original OPE coefficients.

        Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
        n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
                                   = dT + 2T*lam + (c/12)*lam^3
        r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4

        The roundtrip reproduces the OPE pole structure.
        Tier 3 (cross-check).
        """
        from lib.laplace_bridge import r_matrix_to_lambda_bracket, lambda_bracket_to_r_matrix
        from lib.examples.virasoro import T, dT
        c = Symbol('c')
        z = Symbol('z')

        # Step 1: OPE -> lambda-bracket
        ope_coeffs = {0: dT, 1: 2*T, 3: Rational(1, 2)*c}
 succeeded in 52ms:

    The corrections MODIFY how the bar differential acts on 2-element
    bar chains. This is equivalent to a deformed m_2.

    For the Virasoro case, the deformed m_2 at leading Eisenstein order:

    m_2^{eff}(T,T; λ) = (1 + 2λ + (c/12)λ³)     [genus-0]
                        + G_2·(-λ)                  [E_2 correction, from simple pole]
                        + G_4·(c/2 + 6λ²)          [E_4 correction, quartic+double]
                        + G_6·(5c·λ² + ...)         [E_6 correction]

    Actually, let me re-derive this more carefully.

    The genus-1 Virasoro r-matrix in the PRE-d-log convention:
      r^{(0)}(z) = c_0/z + c_1/z^2 + c_3/z^4
                 = (dT)/z + 2T/z^2 + (c/2)/z^4

    The genus-1 r-matrix:
      r^{(1)}(z;tau) = c_0·ζ(z|τ) + c_1·(-℘(z|τ)) + c_3·℘''(z|τ)/6


thinking
**Exploring genus coefficients**

I need to determine if the genus 2 coefficient should be c/24, c/4, or maybe it’s influenced by the local expansion factor of 6/(z-w)^4. I should compute this. I’m considering the generic genus-g formula from either the introduction or spectral-braiding-core. There’s a possibility that I could find relevant information by searching for `cor:genus-g-curvature-braiding`. Using rg to explore further could be beneficial too!
codex
One suspicious module is deeper than a wording bug: it advertises genus-2 formulas using `c_3 = c/2` as though those were lambda-bracket coefficients, which then inflates the derived Bergman-kernel term. I’m checking that against the repo’s own generic `lambda -> r` conversion before deciding whether this needs a formula patch or just a docstring fix.
exec
/bin/zsh -lc "rg -n -F 'sum_{n>=2}' compute/lib/genus2_ordered_bar.py chapters compute" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'cor:genus-g-curvature-braiding' -g '*.tex' chapters compute ." in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

 succeeded in 52ms:
compute/lib/genus2_ordered_bar.py:27:                     + sum_{n>=2} (-1)^{n-1}/(n-1)! * c_n * d_z^{n-1} B(z,w)
compute/lib/genus2_ordered_bar.py:27:                     + sum_{n>=2} (-1)^{n-1}/(n-1)! * c_n * d_z^{n-1} B(z,w)
exec
/bin/zsh -lc "rg -n -F 'c_0 * f(z,w) + c_1 * B(z,w)' -g '*.py' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
./compute/lib/genus2_ordered_bar.py:26:  r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
exec
/bin/zsh -lc "rg -n -F 'c_3·℘''(z|τ)/6' compute/genus_tower_catalan.py compute/lib/genus2_ordered_bar.py" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:


thinking
**Searching mathematical theorems**

I need to look for relevant theorems, possibly from chapters like spectral-braiding-core or the introduction with a generic formula. It might help to focus on the specific context of these topics. Additionally, I should search for the Bergman derivative coefficient and check for the expression `d_z^2 B`. This should help me gather the necessary information more efficiently. Let's see what I can find!
exec
/bin/zsh -lc "rg -n -F 'd_z"'^2 B'"' chapters compute" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'wp''(z|tau)' chapters compute" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'c/24' chapters compute | head -n 200" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
compute/lib/genus2_ordered_bar.py:637:      r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
compute/lib/genus2_ordered_bar.py:642:      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
compute/lib/genus2_ordered_bar.py:650:    quantum gravity at genus 2. The quartic sector (c/4)*d_z^2 B(z,w)
compute/lib/genus2_ordered_bar.py:668:            2: '(c/4)*d_z^2 B(z,w) + 2T*B(z,w) + partial(T)*f(z,w) on Sigma_2',
compute/lib/genus2_ordered_bar.py:686:                'formula': '(c/4) * d_z^2 B(z,w)',
 succeeded in 51ms:
compute/genus1_e1_ordered_shadow_all_families.py:15:  1/z^2 -> wp(z|tau)             (doubly periodic, no monodromy)
compute/genus1_e1_ordered_shadow_all_families.py:81:    print("\n  wp(z|tau) - 1/z^2:")
compute/genus1_e1_ordered_shadow_all_families.py:229:    print(f"  (1) Genus-1: r^(1)(z;tau) = Omega*zeta(z|tau) + k*kappa*wp(z|tau)")
compute/lib/genus2_ordered_bar.py:10:  rational 1/z^2 -> Weierstrass -wp(z|tau), etc.
compute/lib/genus2_ordered_bar.py:297:    Genus-1: r^{E_tau}(z) = k * wp(z|tau) (pre-d-log convention)
compute/lib/genus2_ordered_bar.py:363:            1: 'wp(z|tau) (elliptic, doubly periodic)',
compute/lib/genus2_ordered_bar.py:386:                'r_matrix': f'{k} * wp(z|tau) + node corrections',
compute/lib/genus2_ordered_bar.py:484:            1: 'Omega*zeta(z|tau) + k*kappa*wp(z|tau)',
compute/lib/genus2_ordered_bar.py:582:                'r_matrix': 'Omega*zeta(z|tau) + k*kappa*wp(z|tau) + Yangian correction',
compute/lib/genus2_ordered_bar.py:667:            1: '(c/12)*wp\'\'(z|tau) + 2T*wp(z|tau) + partial(T)*zeta(z|tau)',
compute/lib/genus2_ordered_bar.py:734:      Genus 1: R^{(1)} = k * [wp(z|tau) - 1/z^2] = k * [3G_4(tau)*z^2 + 5G_6(tau)*z^4 + ...]
compute/lib/genus2_ordered_bar.py:830:    │ c_1 sector   │  k*kappa/z^2         │  k*kappa*wp(z|tau)     │  k*kappa*B(z,w)         │
compute/genus_tower_catalan.py:17:    1/z^2 -> -wp(z|tau)  (note sign: wp = -zeta')
compute/genus_tower_catalan.py:51:    Double (2T):  2T * [wp(z|tau) - 1/z^2]
compute/genus_tower_catalan.py:185:      r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 succeeded in 50ms:
compute/e1_arithmetic_complete.py:521:    # chi_h(q) = q^{h - c/24} / prod(1-q^n)
chapters/examples/examples-worked.tex:2599:  q^{-c/24}\,\bigl(1 + 3q + \cdots\bigr),
chapters/examples/examples-worked.tex:2766:  \mathrm{tr}_{L_j}(q^{L_0 - c/24}).
chapters/examples/examples-complete-proved.tex:929:\operatorname{tr}_{V_k(\fg)} q^{L_0 - c/24}
chapters/examples/examples-complete-proved.tex:931:q^{-c/24} \prod_{n=1}^{\infty} \frac{1}{(1-q^n)^{\dim\fg}}
chapters/examples/examples-complete-proved.tex:963: $\;Z_{\mathrm{ann}} = q^{-c/24}\prod(1-q^n)^{-\dim\fg}$
compute/field_sector_generating_function.py:132:    scalar_{2r+1}(1,...,1) = (c/24) * T_{2r+1}(1,...,1)
compute/field_sector_generating_function.py:195:    At lam = 1: scalar/T = c/24.
compute/field_sector_generating_function.py:405:    # Theorem 2: scalar/T = c/24
compute/field_sector_generating_function.py:406:    print("\n--- Theorem 2: scalar/T = c/24 at symmetric point ---")
compute/field_sector_generating_function.py:414:              f"c/24 = {d['expected']:.8f}, match = {d['match']}")
chapters/examples/rosetta_stone.tex:5632:$\chi_j(\tau) = \mathrm{tr}_{L_j}(q^{L_0 - c/24})$,
compute/lib/genus_one_bridge.py:544:        χ₀(q) = q^{-c/24} · Π_{n≥2}(1/(1-qⁿ))
compute/lib/genus_one_bridge.py:573:        'leading_power': -c / 24,  # q^{-c/24} prefactor
compute/lib/genus_one_bridge.py:575:        'formula': 'χ₀(q) = q^{-c/24} · Π_{n≥2} 1/(1-qⁿ)',
compute/lib/verlinde_bulk_check.py:638:        T_{ij} = delta_{ij} * exp(2*pi*i * (h_i - c/24))
compute/ising_e1_shadow_complete.py:145:      ch_{1,1}(q) = q^{-c/24} * (1 + q^2 + q^3 + 2q^4 + 2q^5 + 3q^6 + ...)
compute/ising_e1_shadow_complete.py:159:    ch_{r,s}(q) = q^{h_{r,s} - c/24} * (1/eta(q)) * sum_{k in Z}
compute/ising_e1_shadow_complete.py:201:    # We need these to be integers after subtracting h - c/24 = 0 - 1/48 = -1/48
compute/ising_e1_shadow_complete.py:204:    # Actually let's work with q^{h-c/24} = q^{0 - 1/48} = q^{-1/48}

thinking
**Searching for computation issues**

I need to conduct a more targeted search for the incorrect computation logic, specifically looking at `c_3 = c/2`. There seems to be inconsistency in the top formula, and it might go beyond just the documentation. I should also search for `c3` within the function, perhaps focusing on string occurrences. It seems like using `sed` after line 684 would be beneficial for addressing this issue effectively.
exec
/bin/zsh -lc "sed -n '684,724p' compute/lib/genus2_ordered_bar.py" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
            'quartic_pole': {
                'name': 'Sector III: c-curvature',
                'formula': '(c/4) * d_z^2 B(z,w)',
                'globally_meromorphic': True,
                'B_monodromies': '0',
                'gravitational': 'genus-2 graviton vertex',
            },
        },

        'F_2': {
            'formula': f'F_2 = kappa * 7/5760 = 7*{c}/11520',
            'kappa': c / 2,
            'lambda_2_FP': Rational(7, 5760),
        },

        'degeneration_limits': {
            'separating': (
                'r -> Virasoro genus-1 r-matrices on each E_{tau_a}. '
                'The quartic sectors from each component are independent.'
            ),


thinking
**Correcting notation issues**

It seems that the existing top docstring is misleading. Instead of stating that the lambda-bracket is `{a_\lambda b} = c_0 + c_1 \lambda + ...`, it should clarify that `a_{(n)}b = c_n` and express the lambda-bracket as the sum of `c_n λ^n/n!`. The lines in genus2_ordered_bar incorrectly present the lambda-bracket. To fix it, we can redefine it with the OPE coefficients explicitly, correcting the value stated in line 633.
thinking
**Searching for functions**

I’m looking into whether the top docstring is incorrect for the whole repository. First, I need to check if there are other functions that are defining a generic bridge similarly. I’ll search for the pattern `lambda-bracket {a_lambda b} = c_0 + c_1*lambda + ...` in other files since there might be several instances. The user might be focusing on lambda-bracket formulas specifically, so I’ll search for that exact pattern.
exec
/bin/zsh -lc "rg -n -F '{T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda"'^3'"' compute chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'lambda-bracket {a_lambda b} = c_0 + c_1*lambda + c_2*lambda"'^2 + ...'"' compute chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'c_3 = c/2.' compute chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F '{T_lambda T} = dT + 2T*lambda + (c/2)*lambda"'^3'"' compute chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
compute/lib/genus2_ordered_bar.py:634:    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
compute/genus_tower_catalan.py:190:    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
 succeeded in 52ms:
compute/lib/genus2_ordered_bar.py:633:      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
 exited 1 in 51ms:

 succeeded in 51ms:
compute/genus_tower_catalan.py:188:      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3

thinking
**Refining formula search**

I am considering if there are potentially incorrect formulas involving `lambda^{(3)}` that could be confusing. I need to search for the term `c/2` near these lambdas, employing regex to catch any lines with `lambda` and `c/2`. It might also bring up `equivalently (c/2)\lambda^{(3)}`. I should clarify the introduction line to align with the user's request and ensure consistency in notation, while also checking for `c/3*5!` and `lambda^{(5)}`.
exec
/bin/zsh -lc "rg -n -F 'lambda"'^{(3)}'"' chapters compute working_notes.tex main.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' '(lambda-bracket|lambda bracket|\\{T_\\\\lambda T\\}|\\{T\\{\\}_\\\\lambda T\\}|\\{T_lambda T\\}|m_2\\(T,T; ?\\\\lambda\\)|m_2\\(T,T; lambda\\)|Virasoro lambda-bracket)["'^'"\\n]{0,160}c/2' chapters compute main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/theory/introduction.tex:1849:equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
 succeeded in 51ms:
compute/lib/genus2_ordered_bar.py:633:      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
compute/genus_tower_catalan.py:188:      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
compute/lib/examples/virasoro.py:14:- The coefficient c/12 (not c/2) in the lambda-bracket vs c/2 in OPE
compute/tests/test_spectral_braiding.py:390:        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!

thinking
**Analyzing documentation patches**

I'm considering updating the introduction line to remove the equivalently c/2 λ^(3) since the user might prefer c/12 instead. I'll search for `{W_\lambda W}` with c/3 λ^{(5)} but might not find anything. It's also possible that I need to search for general claims about lambda-bracket coefficients stored as c_n, making sure there's no confusion with /n! I may need to check other files for patterns stating sum c_n lambda^n without the /n!.
exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' 'sum["'^'"\\n]{0,80}lambda\\"'^n(?!/n!)'"' compute chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' '\\{["'^'"\\n]{0,40}_lam["'^'"\\n]{0,40}\\}["'^'"\\n]{0,80}c/2["'^'"\\n]{0,80}(lambda|lam)' compute chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' '\\{["'^'"\\n]{0,40}_lam["'^'"\\n]{0,40}\\}["'^'"\\n]{0,80}c/3["'^'"\\n]{0,80}(lambda|lam)' compute chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/w-algebras-stable.tex:13:\{\phi^i{}_\lambda \phi^j\} = \sum_{n \geq 0} \Pi^{ij}_n \lambda^n, \quad \Pi^{ij}_n \in \mathcal{V},
chapters/examples/w-algebras-stable.tex:138:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras-w3.tex:178:For compactness, write $\{W_\lambda W\} = \sum_{n=0}^{5} P_n\,\lambda^n$
chapters/examples/w-algebras-w3.tex:400:$\{W_\lambda W\} = \sum_{n=0}^5 P_n\,\lambda^n$ into one slot of
chapters/examples/w-algebras-virasoro.tex:13:\{\phi^i{}_\lambda \phi^j\} = \sum_{n \geq 0} \Pi^{ij}_n \lambda^n, \quad \Pi^{ij}_n \in \mathcal{V},
chapters/examples/w-algebras-virasoro.tex:134:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras-virasoro.tex:434:r^{\text{Vir}}(\lambda, \mu) = \sum_{n=1}^3 \frac{r_n}{\lambda^n} \otimes \frac{1}{\mu},
compute/genus_tower_catalan.py:642:    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
compute/genus_tower_catalan.py:644:    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
chapters/examples/w-algebras-frontier.tex:908:= \sum_{n=0}^{7} P_n^{(4)}\,\lambda^n
chapters/examples/examples-complete-core.tex:415:where $\delta_\lambda = \sum_{n \geq 0} \frac{\lambda^n}{n!} \partial^n \delta(z)$ is the delta-function distribution.
chapters/examples/w-algebras.tex:23:\{\phi^i{}_\lambda \phi^j\} = \sum_{n \geq 0} \Pi^{ij}_n \lambda^n, \quad \Pi^{ij}_n \in \mathcal{V},
chapters/examples/w-algebras.tex:148:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras.tex:420:r^{\text{Vir}}(\lambda, \mu) = \sum_{n=1}^3 \frac{r_n}{\lambda^n} \otimes \frac{1}{\mu},
chapters/examples/examples-worked.tex:114:  \{a_\lambda b\} = \sum_{n \geq 0} c_n^{ab}\, \lambda^n.
chapters/examples/examples-complete.tex:433:where $\delta_\lambda = \sum_{n \geq 0} \frac{\lambda^n}{n!} \partial^n \delta(z)$ is the delta-function distribution.
compute/tests/test_spectral_braiding.py:6:where {a_lambda b} = sum c_n lambda^n is the lambda-bracket.
compute/lib/cross_volume_deep_bridge.py:68:    """Compute r(z) = sum_n c_n * n! / z^{n+1} from {a_lambda b} = sum c_n lambda^n.
compute/lib/cross_volume_deep_bridge.py:97:      {a_lambda b} = sum_{n>=0} c_n * lambda^n / n!
compute/lib/spectral.py:14:    """Truncated Laurent series in one variable: sum_{n >= -N} a_n lambda^n.
 succeeded in 50ms:
compute/lib/cross_volume_deep_bridge.py:226:    {W_lambda W} = ... (c/360)*lambda^5 + lower order (nonlinear)
compute/lib/cross_volume_deep_bridge.py:379:    """Verify leading WW bracket: {W_lambda W} has (c/360)*lambda^5 term.
compute/lib/cross_volume_deep_bridge.py:390:        'bracket': '{W_lam W} has (c/360)*lam^5',
compute/tests/test_w3_pva.py:93:        """Leading term of {W_lam W} is (c/360)*lam^5.
compute/lib/examples/w3_algebra.py:23:  {W_lam W} = (c/360)lam^5 + (T/3)lam^3 + (dT/2)lam^2
compute/lib/examples/w3_algebra.py:187:    {W_lam W} = (c/360)lam^5 + (T/3)lam^3 + (dT/2)lam^2
compute/lib/examples/w3_algebra.py:635:    # the maximum lambda-degree in {W_lam W} is 5 (from c/360*lam^5).
compute/lib/modular_pva_quantization.py:193:            'bracket_type': '{W_lam W} = (c/360)*lam^5 + ... + beta^2*Lambda*lam + ...',
compute/lib/pva_descent_chain_level.py:274:    {W_lam W} = (c/360)*lam^5 + ... (the nonlinear bracket)
 succeeded in 51ms:
compute/genus_tower_catalan.py:188:      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
compute/tests/test_spectral_braiding.py:390:        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
compute/lib/genus2_ordered_bar.py:633:      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3



thinking
**Analyzing lambda-bracket conventions**

I noticed that the search shows some potentially problematic generic formulas that lack the /n! factor. The user is focused on the lambda-bracket divided-power convention and the Virasoro formula c/12. I need to check the files in Volume II to see if they define the general lambda-bracket correctly. Misconceptions might arise if the notation doesn’t include /n! when it should. I could also suggest being explicit about coefficients being divided powers if they're not already.
thinking
**Clarifying formula specifics**

I see that the focus in V2-AP34 is on distinguishing between c/12 and c/2, as well as W3 c/360. I don't think I need to rewrite all the generic notation, but I should clarify that "Search for lambda-bracket formulas" suggests looking for actual formulas, not just definitions. I found a few suspicious hits that might need examination, especially since the user emphasizes using c/12 for Virasoro. The test line may not be wrong since it’s just a comment, but I might want to confirm it aligns with user expectations for exactness.
thinking
**Considering code documentation updates**

I’m thinking about patching comments and docstrings where the lambda-bracket notation is mixed. Specifically, I want to change instances of `c/2*lam^3/3!` to `c/12*lam^3` and keep OPE conversion in a separate sentence. I need to search for patterns like `lam^3/3!` and `lambda^3/3!` to see how widespread the issue is. It looks like there aren't many lines to address, so I need to decide whether to patch them all.
codex
The narrow violation set is now clear. There are three kinds of drift:
1. outright wrong displayed Virasoro brackets using `(c/2)lambda^3`,
2. mixed notation that states the bracket as `(c/2)lambda^{(3)}` or `(c/2)lam^3/3!`, and
3. one generic docstring that mislabeled OPE coefficients as lambda-bracket coefficients.

I’m patching all three so the repo advertises one convention consistently: `{T_λ T} = ∂T + 2Tλ + (c/12)λ^3`, with any `c/2` discussion moved to an OPE-to-bracket conversion sentence.
exec
/bin/zsh -lc "rg -n -F 'lam"'^3/3!'"' compute chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'lambda"'^3/3!'"' compute chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F '(c/2)*lambda"'^3'"' compute chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F '(c/2)*lam"'^3'"' compute chapters README.md main.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/theory/introduction.tex:1849:equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
chapters/connections/thqg_fm_calculus_extensions.tex:937: to $\lambda^3/3!$; multiplying by the OPE coefficient $c/2$
chapters/connections/thqg_fm_calculus_extensions.tex:1360: $\beta \cdot 2T \cdot \lambda^3/3! = \beta \cdot
 succeeded in 51ms:
compute/lib/gravity_3d_engine.py:66:      (z-w)^{-4}: c/2    -> T_{(3)}T = c/2   -> coeff of lam^3/3! = c/12
compute/lib/pva_descent_chain_level.py:174:    c/2 * lam^3/3! = c/12 * lam^3.
compute/tests/test_w3_pva.py:111:        From W_{(3)}W = 2T: (2T)*lam^3/3! = T/3 * lam^3.
compute/tests/test_spectral_braiding.py:390:        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
 succeeded in 50ms:
compute/lib/genus2_ordered_bar.py:633:      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
compute/genus_tower_catalan.py:188:      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
 succeeded in 51ms:
compute/lib/examples/virasoro.py:235:      = dT + 2T*lam + 0 + (c/2)*lam^3/6
compute/tests/test_spectral_braiding.py:390:        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
exec
/bin/zsh -lc "sed -n '384,396p' compute/tests/test_spectral_braiding.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '226,240p' compute/lib/examples/virasoro.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '56,72p' compute/lib/gravity_3d_engine.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '182,176p' compute/lib/gravity_3d_engine.py" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
    """
 succeeded in 52ms:

    {T_lam T} = (c/12) lam^3 + 2T lam + dT

    This encodes the OPE:
      T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)

    via the state-field dictionary: T_{(n)} T corresponds to the
    (n+1)-th pole in the OPE, and {T_lam T} = sum_n T_{(n)}T lam^n/n!.

    Pole dictionary:
      (z-w)^{-4}: c/2    -> T_{(3)}T = c/2   -> coeff of lam^3/3! = c/12
      (z-w)^{-2}: 2T     -> T_{(1)}T = 2T    -> coeff of lam^1/1! = 2T
      (z-w)^{-1}: dT     -> T_{(0)}T = dT    -> coeff of lam^0/0! = dT

    Returns a dict with keys 'lam3', 'lam1_T', 'lam0_dT' for the
    coefficients of lam^3, T*lam, and dT respectively.

 succeeded in 52ms:
    OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)

    n-products (from OPE): T_n T = Res_{z->w} (z-w)^n T(z)T(w)
      T_0 T = dT (coefficient of 1/(z-w))
      T_1 T = 2T (coefficient of 1/(z-w)^2)
      T_2 T = 0
      T_3 T = c/2 (coefficient of 1/(z-w)^4)

    Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
      = dT + 2T*lam + 0 + (c/2)*lam^3/6
      = dT + 2T*lam + (c/12)*lam^3

    So the c/12 coefficient comes from c/2 divided by 3! = 6.
    """
    ope_fourth_pole = Rational(1, 2) * c  # c/2
 succeeded in 52ms:

        Start from OPE coefficients, convert to lambda-bracket, then to r-matrix.
        The result should reproduce the original OPE coefficients.

        Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
        n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
                                   = dT + 2T*lam + (c/12)*lam^3
        r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4

        The roundtrip reproduces the OPE pole structure.
        Tier 3 (cross-check).
        """

thinking
**Analyzing formula consistency**

I want to patch notation lines in examples/virasoro/test_spectral_braiding, focusing on terms like `lam^3/6` and `lam^3/3!` for consistency. I think the user wants uniform formula displays, so I might need to adjust these. I’ll also check the compute/tests/test_cross_volume_deep_bridge for lines involving OPE coeffs and bracket conversion, particularly `c/2)/3!`. If the user requests formulas, I’ll ensure clarity by making changes as needed, especially lines with "lambda-bracket" and related expressions.
exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' '(Lambda-bracket:|lambda-bracket:|The Virasoro lambda-bracket:|\\{T_lam T\\}|\\{T_lambda T\\})["'^'"\\n]{0,120}(lam\\"'^3/6|lam'"\\"'^3/3!|lambda'"\\"'^3/3!|lambda'"\\"'^'"\\{\\(3\\)\\})' compute chapters main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F '{T_lam T} = dT + 2T*lam + (c/12)*lam"'^3'"' compute chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
compute/tests/test_spectral_braiding.py:390:        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
 succeeded in 52ms:
compute/tests/test_pva_descent_chain_level.py:83:        """Virasoro: {T_lam T} = dT + 2T*lam + (c/12)*lam^3."""
compute/tests/test_w3_pva.py:31:        """Verify {T_lam T} = dT + 2T*lam + (c/12)*lam^3.
compute/lib/examples/w3_algebra.py:365:    """Base bracket {T_lam T} = dT + 2T*lam + (c/12)*lam^3."""
compute/lib/examples/w3_algebra.py:479:    # {T_lam T} = dT + 2T*lam + (c/12)*lam^3
compute/tests/test_swiss_cheese_virasoro_wheels.py:243:    """Test m_2(T,T;lam) = {T_lam T} = dT + 2T*lam + (c/12)*lam^3."""
compute/lib/modular_pva_quantization.py:180:            'bracket_type': '{T_lam T} = dT + 2T*lam + (c/12)*lam^3',
compute/lib/modular_pva_quantization.py:746:    The Virasoro PVA: {T_lam T} = dT + 2T*lam + (c/12)*lam^3.
compute/lib/sc_bar_cobar_engine.py:579:    {T_lam T} = dT + 2T*lam + (c/12)*lam^3
compute/tests/test_cross_volume_deep_bridge.py:103:    """Virasoro: {T_lam T} = dT + 2T*lam + (c/12)*lam^3."""
compute/lib/swiss_cheese_virasoro_wheels.py:173:    {T_lam T} = dT + 2T*lam + (c/12)*lam^3
compute/lib/cross_volume_deep_bridge.py:321:        'bracket': '{T_lam T} = dT + 2T*lam + (c/12)*lam^3',
compute/lib/pva_descent_chain_level.py:167:    """Virasoro PVA: {T_lam T} = dT + 2T*lam + (c/12)*lam^3.
compute/lib/pva_descent_chain_level.py:272:    {T_lam T} = dT + 2T*lam + (c/12)*lam^3
compute/lib/pva_descent_chain_level.py:630:    # {T_lam T} = dT + 2T*lam + (c/12)*lam^3
compute/lib/modular_obstruction_engine.py:222:            'description': 'Virasoro PVA: {T_lam T} = dT + 2T*lam + (c/12)*lam^3',
compute/lib/modular_obstruction_engine.py:1387:        {T_lam T} = dT + 2T*lam + (c/12)*lam^3
exec
/bin/zsh -lc "sed -n '636,646p' compute/genus_tower_catalan.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'sum_n c_n * lambda"'^n'"' compute chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'sum c_n lambda"'^n'"' compute chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
    # The z^1 term of R^{(1)} is -dT*G_2. Since G_2 = (pi^2/3)*E_2,
    # the correction proportional to E_2 in the m_2 operation is:
    #   delta_m2(lambda) = -(pi^2/3) * dT * lambda
    #
    # But wait: the r-matrix expansion R^{(1)} is in powers of z,
    # where z is the spectral parameter of the bar complex.
    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
    # RESIDUE, and the genus-1 correction is:
    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
    # where delta(c_n) is the Eisenstein correction to the nth
    # OPE coefficient.
 succeeded in 51ms:
compute/genus_tower_catalan.py:642:    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
 succeeded in 51ms:
compute/lib/cross_volume_deep_bridge.py:68:    """Compute r(z) = sum_n c_n * n! / z^{n+1} from {a_lambda b} = sum c_n lambda^n.
compute/tests/test_spectral_braiding.py:6:where {a_lambda b} = sum c_n lambda^n is the lambda-bracket.
codex
I found a second layer of convention drift: a few compute utilities describe the generic lambda-bracket as `sum c_n lambda^n`, which is the non-divided convention. Those are in the bridge/test code and one genus note. I’m fixing those too so the generic definitions match V2-AP34, not just the Virasoro example.
exec
/bin/zsh -lc "sed -n '1,120p' compute/lib/cross_volume_deep_bridge.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,28p' compute/tests/test_spectral_braiding.py" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' '\\{a_lambda b\\} = sum["'^'"\\n]*lambda\\"'^n(?!'"\\s*/\\s*n"'!)|'"\\{a_lam b\\} = sum["'^'"\\n]*lam\\"'^n(?!'"\\s*/\\s*n"'!)|sum_n c_n '"\\* lambda\\"'^n|sum c_n lambda'"\\"'^n'"' compute chapters main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
"""Cross-volume deep bridge: Laplace, sign conventions, shadow-boundary comparison.

Extends the basic Laplace bridge (laplace_bridge.py) with:

1. **Laplace bridge for all 7 standard families**: Heisenberg, affine sl_2,
   Virasoro, beta-gamma, bc ghosts, W_3, and lattice VOAs.
   r(z) = Res_{lambda=0} e^{-lambda z} {a_lambda b}
   For polynomial lambda-brackets: r(z) = sum c_n * n! / z^{n+1}.

2. **Sign convention check**: Verify the Lian-Zuckerman/Voronov (LV) sign
   convention for A_infinity structures at arities 2, 3, 4.  The A_infinity
   relations m_1^2 = 0, m_1 m_2 = m_2(m_1 x 1 + 1 x m_1), etc. carry
   signs from the Koszul convention.  For curved A_infinity (genus >= 1),
   m_1^2(a) = [m_0, a] with the COMMUTATOR sign.

3. **Shadow-boundary comparison**: Vol I kappa values vs Vol II boundary
   curvature.  The modular curvature kappa(A) from the bar complex in
   Vol I must equal the boundary curvature in the Swiss-cheese setting
   of Vol II.

 succeeded in 51ms:
"""
Tests verifying R-matrix structures and Yang-Baxter equations.

The spectral braiding data arises from the Laplace transform bridge:
  r(z) = sum_{n>=0} c_n * n! / z^{n+1}
where {a_lambda b} = sum c_n lambda^n is the lambda-bracket.

For each example family, we verify:
1. The Laplace transform bridge (BR3) correctly maps brackets to r-matrices
2. The classical Yang-Baxter equation (CYBE) for the r-matrix
3. The quantum Yang-Baxter equation (YBE) for the R-matrix (when applicable)

Paper references: Vol II Section 18 (spectral-braiding.tex), BR3 axiom.

Test tiers:
  Tier 1 (structural): CYBE/YBE are self-certifying identities
  Tier 2 (published): r-matrix forms match Kac, Chari-Pressley
  Tier 3 (cross-check): Laplace bridge agrees with direct OPE computation
"""
import sys
 succeeded in 51ms:
compute/genus_tower_catalan.py:642:    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
compute/tests/test_spectral_braiding.py:6:where {a_lambda b} = sum c_n lambda^n is the lambda-bracket.
compute/lib/cross_volume_deep_bridge.py:68:    """Compute r(z) = sum_n c_n * n! / z^{n+1} from {a_lambda b} = sum c_n lambda^n.


thinking
**Evaluating test needs**

I'm considering whether we need to patch the strings returned by the genus2_ordered_bar function, and if I should import something for that. Running tests might be expected by the user, even if we don't change any logic—though the developer suggests focusing on verifying changes. I could run a specific test, but maybe I don't need to. Since the only change was in the test docstring, perhaps no tests are actually required.
thinking
**Exploring string data edits**

If I edit the string data in genus2_ordered_bar.py, I might consider running a command to verify syntax. I could use `python -c "from compute.lib.genus2_ordered_bar import genus2_r_matrix_virasoro; print(genus2_r_matrix_virasoro()['c3'])"` if the import path isn’t too tricky. That should help confirm everything's working. Additionally, running tests with `python -m pytest compute/tests/test_examples.py -q` might be necessary, depending on whether I need to compile anything first.
exec
/bin/zsh -lc "sed -n '1844,1852p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\subsection*{Virasoro and $\mathcal{W}_3$: the nonlinear tests}

The Virasoro algebra ($\lambda$-bracket
$\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
structures:
\begin{itemize}
exec
/bin/zsh -lc 'git diff -- chapters/theory/introduction.tex compute/lib/genus2_ordered_bar.py compute/genus_tower_catalan.py compute/lib/cross_volume_deep_bridge.py compute/tests/test_spectral_braiding.py compute/lib/examples/virasoro.py' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index a86fcff..d95e263 100644
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1606,8 +1606,7 @@ inductive genus determination
 along with $2$D convergence and the analytic-algebraic comparison;
 the analytic lane of MC5 is proved at all genera; BV=bar in
 the coderived category is proved for all shadow classes
-(Volume~I, Theorem~
-ef*{V1-thm:bv-bar-coderived}); the genuswise
+(Volume~I, Theorem~\ref*{V1-thm:bv-bar-coderived}); the genuswise
 chain-level BV/BRST/bar identification remains conjectural
 (class~M chain-level false).
 
@@ -1882,7 +1881,8 @@ structures:
  $c \mapsto \alpha_N - c$, where
  $\alpha_N = 2(N-1)(2N^2 + 2N + 1)$ is the $\cW_N$
  complementarity constant (recovering $\alpha_2 = 26$ for
- Virasoro). Self-duality occurs at $c^* = \alpha_N/2$. The
+ Virasoro). Self-duality occurs at $c^* = \alpha_N/2$
exec
/bin/zsh -lc "sed -n '180,206p' compute/genus_tower_catalan.py" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

    The genus-0 collision residue for Virasoro (post-d-log absorption, AP19):
      r^{(0)}(z) = (c/2)/z^3 + 2T/z + dT

    The genus-1 collision residue replaces rational poles by Weierstrass:
      r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)

    Wait -- let me be more careful. The Virasoro lambda-bracket is:
      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3

    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.

    The genus-0 m_2 in the bar complex is:
      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
                       = c_0 + c_1*lambda + c_3*lambda^3
    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).

    Wait no: from the code m2_num:
      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3


thinking
**Organizing my thoughts**

I see this section needs a more concise and consistent explanation. I should consider adjusting the comment at line 642, possibly just updating that specific comment. There's also a need to patch areas around lines 185-201 and 642-644. I wonder if I should inspect the file for current changes to ensure everything is in order. I guess it's likely clean, but I’ll use apply_patch just to be sure. I need to look into compute/lib/genus2_ordered_bar around the top and its functions as well.
exec
/bin/zsh -lc "sed -n '18,34p' compute/lib/genus2_ordered_bar.py" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

  f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
  B(z,w) = d_z d_w log E(z,w) (Bergman kernel)

The genus-2 r-matrix for a chiral algebra A with lambda-bracket
{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
(from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):

  r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
                     + sum_{n>=2} (-1)^{n-1}/(n-1)! * c_n * d_z^{n-1} B(z,w)

The B-cycle monodromy has TWO independent components (j = 1, 2):
  delta_{B_j} r^{Sigma_2}(z,w) = -2*pi*i * c_0 * omega_j(z)

where omega_1, omega_2 are the normalized abelian differentials.

THREE DEGENERATION LIMITS of Sigma_2:

thinking
**Clarifying coefficients**

The user noted that I must use divided powers, specifically c/12, for the Virasoro operator. This suggests they want me to display the coefficient as c/12 rather than an intermediate expression. I should also make sure to patch any mixed notation lines accordingly. This seems like an important detail to get right, so I'll keep that in mind as I proceed!
codex
I’ve finished the audit pass and isolated the actual convention defects. The edits are confined to one manuscript sentence and the compute/test doc surfaces that still displayed the Virasoro bracket with an OPE coefficient or mixed notation; I’m patching those now.
file update
M /Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_ordered_bar.py
@@ -21,4 +21,4 @@
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
@@ -632,4 +632,5 @@
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
@@ -641,3 +642,3 @@
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
@@ -659,5 +660,5 @@
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
M /Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_spectral_braiding.py
@@ -389,4 +389,4 @@
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
M /Users/raeez/chiral-bar-cobar-vol2/compute/lib/examples/virasoro.py
@@ -234,3 +234,2 @@
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
M /Users/raeez/chiral-bar-cobar-vol2/compute/genus_tower_catalan.py
@@ -186,19 +186,11 @@
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
@@ -641,5 +633,5 @@
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
M /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
@@ -1848,3 +1848,3 @@
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
apply_patch(auto_approved=true) exited 0 in 49ms:
Success. Updated the following files:
M chapters/theory/introduction.tex
M compute/lib/genus2_ordered_bar.py
M compute/genus_tower_catalan.py
M compute/lib/examples/virasoro.py
M compute/tests/test_spectral_braiding.py
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.

file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.


thinking
**Verifying code patches**

I’m thinking about whether I need to patch `compute/lib/cross_volume_deep_bridge.py`. It seems like a good idea to verify the search results after making the patch. I'll look for targeted patterns like `(c/2)*lambda^3`, `lambda^{(3)}`, or even `c/2)*lam^3/3!`. I want to ensure I’m checking the actual relevant surfaces. I’m also considering if `c_3 = c/2` is still present in `genus2_ordered_bar` since we changed the string, but there could be other contexts still needing attention. I’ll search again!
codex
The patch is in. I’m running the falsifiers now: grep for the old Virasoro cubic-term spellings and a quick syntax check on the touched Python files, so the turn closes on verified state rather than an unverified edit.
exec
/bin/zsh -lc "rg -n -F '(c/2)*lambda"'^3'"' chapters compute main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'lambda"'^{(3)}'"' chapters compute main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -F '(c/2)*lam"'^3'"' chapters compute main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'python -m py_compile compute/lib/genus2_ordered_bar.py compute/genus_tower_catalan.py compute/lib/examples/virasoro.py compute/tests/test_spectral_braiding.py' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 exited 127 in 51ms:
zsh:1: command not found: python
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.


thinking
**Checking Python and code variables**

It seems like Python isn’t found; maybe I should look for Python 3 instead. I believe I might need to rerun something. I want to search for the equation c_3 = c/2. Ah, and maybe I should also include an explanation for the `lambda-bracket` with c/2 to make things clearer. I think using targeted regex could help with this. Let’s see how that goes!
codex
The old bad spellings are gone; the grep checks returned clean. `python` isn’t available in this shell, so I’m rerunning the syntax check with `python3` and doing one more targeted pass for any surviving Virasoro lambda-bracket lines that still mention `c/2`.
exec
/bin/zsh -lc "rg -n -F 'c_3 = c/2' chapters compute main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P --hidden --glob '"'!*.pdf'"' '(Virasoro lambda-bracket|lambda-bracket: \\{T_lam T\\}|\\{T_lambda T\\}|\\{T_\\\\lambda T\\}|\\{T\\{\\}_\\\\lambda T\\}|m_2\\(T,T; ?lambda\\)|m_2\\(T,T; ?\\\\lambda\\))["'^'"\\n]{0,140}c/2' chapters compute main.tex working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'python3 -m py_compile compute/lib/genus2_ordered_bar.py compute/genus_tower_catalan.py compute/lib/examples/virasoro.py compute/tests/test_spectral_braiding.py' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 50ms:

 succeeded in 50ms:
compute/tests/test_infrastructure.py:364:        # Virasoro OPE: c_0 = dT, c_1 = 2T, c_3 = c/2
compute/tests/test_cross_volume_deep_bridge.py:213:        """OPE coeff c_3 = c/2 -> bracket {3: (c/2)/3! = c/12}."""
 succeeded in 51ms:

file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.


thinking
**Searching for patches**

I’m looking for a search with `c_3 = c/2` to find the OPE coefficient comments, but I see I need to be careful about not editing those notes. I’ll do a targeted search for `lambda-bracket` but it looks like that search didn’t yield results. I should check the line numbers after applying the patch for final reporting. I need to gather exact lines changed, perhaps using `nl -ba` or `rg`. My goal is to summarize findings with corresponding file details and editor changes.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1844,1850p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba compute/genus_tower_catalan.py | sed -n '184,200p;640,646p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba compute/lib/genus2_ordered_bar.py | sed -n '22,32p;632,646p;660,671p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba compute/tests/test_spectral_braiding.py | sed -n '386,394p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba compute/lib/examples/virasoro.py | sed -n '232,239p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  1844	\subsection*{Virasoro and $\mathcal{W}_3$: the nonlinear tests}
  1845	
  1846	The Virasoro algebra ($\lambda$-bracket
  1847	$\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
  1848	in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
  1849	the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
  1850	and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 succeeded in 51ms:
   184	    The genus-1 collision residue replaces rational poles by Weierstrass:
   185	      r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
   186	
   187	    The Virasoro lambda-bracket is:
   188	      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
   189	
   190	    Equivalently, the OPE/n-product data are
   191	      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
   192	    so in divided-power form
   193	      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
   194	                       = dT + 2T*lambda + (c/12)*lambda^3.
   195	
   196	    At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
   197	    The correction to the collision residue at genus 1 is:
   198	
   199	    In the manuscript convention (genus1_intersection.py, Virasoro section):
   200	    The genus-1 R-MATRIX CORRECTION R^{(1)} = r^{(1)} - r^{(0)} has:
   640	    # From the three-sector analysis:
   641	    # - The quartic sector gives a z^0 SCALAR correction: (c/2)*G_4
   642	    #   This corrects the SCALAR (weight -1) component, not T.
 succeeded in 51ms:
    22	The genus-2 r-matrix for a chiral algebra A with n-products
    23	a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
    24	(from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
    25	
    26	  r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
    27	                     + sum_{n>=2} (-1)^{n-1}/(n-1)! * c_n * d_z^{n-1} B(z,w)
    28	
    29	The B-cycle monodromy has TWO independent components (j = 1, 2):
    30	  delta_{B_j} r^{Sigma_2}(z,w) = -2*pi*i * c_0 * omega_j(z)
    31	
    32	where omega_1, omega_2 are the normalized abelian differentials.
   632	    The Virasoro lambda-bracket:
   633	      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
   634	    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
   635	    T_{(2)}T = 0, T_{(3)}T = c/2.
   636	
   637	    The genus-2 r-matrix:
   638	      r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
   639	
   640	    THREE sectors:
 succeeded in 52ms:
   386	        The result should reproduce the original OPE coefficients.
   387	
   388	        Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
   389	        n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
   390	        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
   391	                        because (c/2)/3! = c/12
   392	        r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
   393	
   394	        The roundtrip reproduces the OPE pole structure.
 succeeded in 52ms:
   232	      T_3 T = c/2 (coefficient of 1/(z-w)^4)
   233	
   234	    Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
   235	      = dT + 2T*lam + (c/12)*lam^3
   236	
   237	    So the c/12 coefficient comes from c/2 divided by 3! = 6.
   238	    """
   239	    ope_fourth_pole = Rational(1, 2) * c  # c/2
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.


thinking
**Considering line numbers**

I might need to change the line numbers for the compute/genus_tower comment between lines 642-645 since 640-646 doesn’t show what was changed due to selection. Should I report if there's nothing found? But we have patched the comment at line 648, so it might be helpful to get the line numbers. Let’s open lines 646-652 for a closer look. That way, I can clarify what’s happening!
exec
/bin/zsh -lc "nl -ba compute/genus_tower_catalan.py | sed -n '646,652p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   646	    #
   647	    # Wait, the r-matrix correction R^{(1)}(z) is an expansion in z.
   648	    # The m_2 operation is m_2(T,T;lambda) where lambda is the
   649	    # spectral parameter. The r-matrix r(z) is related to m_2 by:
   650	    #   r(z) = sum_n c_n / z^{n+1}  (pre-d-log)
   651	    # After d-log absorption (AP19):
   652	    #   m_2 coefficients at lambda^n = c_n (the OPE coefficients)
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.


thinking
**Evaluating patch adjustments**

Hmm, I'm wondering if our earlier patch to line 642 is relevant for this section. Did we patch that line earlier? It's possible the line numbers have shifted. I think it makes sense to inspect lines 652-660 to get a clearer view on this. I'll need to keep track of the changes we've made and how it all connects.
exec
/bin/zsh -lc "nl -ba compute/genus_tower_catalan.py | sed -n '652,660p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   652	    #   m_2 coefficients at lambda^n = c_n (the OPE coefficients)
   653	    #
   654	    # The correction R^{(1)}(z) adds to the r-matrix in the z-expansion,
   655	    # NOT in the lambda-expansion of m_2. The two are DIFFERENT:
   656	    #   r(z) = c_0/z + c_1/z^2 + c_3/z^4  (genus-0 Virasoro r-matrix)
   657	    #   R^{(1)}(z) = (c/2)*G_4 - dT*G_2*z + ...  (genus-1 correction)
   658	    #
   659	    # The genus-1 r-matrix r^{(1)}(z) = r^{(0)}(z) + R^{(1)}(z).
   660	    # The RESIDUE of r^{(1)} at z=0 is UNCHANGED: the correction
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.


thinking
**Checking patch details**

Hmm, it seems like our earlier patch regarding the comment at line 642 didn’t hold up. I’m seeing the old text, which is puzzling. Maybe there were multiple similar sections, and the patch applied to a different part instead? I need to search for where the patch went and ensure it was applied correctly. Let’s dive into this and figure it out!
exec
/bin/zsh -lc "rg -n -F 'sum_n c_n * lambda"'^n / n!'"' compute/genus_tower_catalan.py" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
634:    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.

exec
/bin/zsh -lc "nl -ba compute/genus_tower_catalan.py | sed -n '630,638p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   630	    #   delta_m2(lambda) = -(pi^2/3) * dT * lambda
   631	    #
   632	    # But wait: the r-matrix expansion R^{(1)} is in powers of z,
   633	    # where z is the spectral parameter of the bar complex.
   634	    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
   635	    # RESIDUE, and the genus-1 correction is:
   636	    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
   637	    # where delta(c_n) is the Eisenstein correction to the nth
   638	    # OPE coefficient.
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.


thinking
**Organizing file references**

I need to get the exact file path for links, using an absolute path and line references. While I could use a plain file:line format, the instructions prefer clickable links. For example, I could format it as `PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1847): ... EXACT edit applied: ...`. I'll also mention verification lines in a concise paragraph, perhaps adding sections like **Findings** and **Verification**, and include line references for specific computations.
codex
**Findings**
- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1849): the Virasoro paragraph mixed the correct Vol II formula `\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3` with the alternate display `(c/2)\lambda^{(3)}`, which reintroduces the OPE coefficient into the lambda-bracket surface. EXACT edit applied: replaced that clause with `the OPE mode T_{(3)}T = c/2 therefore contributes (c/2)/3! = c/12 to the cubic \lambda-term`.

- PROBLEM at [compute/lib/genus2_ordered_bar.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/genus2_ordered_bar.py:22): the module described `c_n` as lambda-bracket coefficients, then later used `c_3 = c/2` as an OPE mode, so the convention was internally inconsistent. EXACT edit applied: changed the generic convention to `a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!`, rewrote the Virasoro display at line 633 to `{T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3`, and relabeled the stored data strings at lines 661-663 as `T_(0)T`, `T_(1)T`, `T_(3)T` OPE modes.

- PROBLEM at [compute/genus_tower_catalan.py](/Users/raeez/chiral-bar-cobar-vol2/compute/genus_tower_catalan.py:187): the note explicitly stated the wrong Virasoro lambda-bracket `{T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3`, then corrected itself later, leaving the convention surface contradictory. EXACT edit applied: replaced that block with the single consistent statement `{T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3`, followed by the OPE-mode explanation `T_{(3)}T = c/2` and the divided-power expansion `sum_n T_{(n)}T * lambda^n / n!`; also fixed the later generic comment at line 634 from `sum_n c_n * lambda^n` to `sum_n c_n * lambda^n / n!`.

- PROBLEM at [compute/lib/examples/virasoro.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/examples/virasoro.py:234): the explanatory lambda-bracket line still displayed the intermediate mixed form `(c/2)*lam^3/6`. EXACT edit applied: collapsed it to the Vol II form `= dT + 2T*lam + (c/12)*lam^3`, keeping the next sentence as the OPE-to-bracket conversion explanation.

- PROBLEM at [compute/tests/test_spectral_braiding.py](/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_spectral_braiding.py:390): the test docstring advertised the lambda-bracket as `... + (c/2)*lam^3/3!`, which is mathematically equivalent but not the repo’s declared Vol II convention. EXACT edit applied: changed it to `lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3` and kept the conversion note on the next line: `because (c/2)/3! = c/12`.

**Verification**
- `rg` found no remaining `'(c/2)*lambda^3'`, `'(c/2)*lam^3'`, or `'lambda^{(3)}'` spellings on the checked Vol II manuscript/compute surface.
- `python3 -m py_compile` passed for the touched Python files.
- Remaining `c_3 = c/2` hits are OPE-mode conversion comments in tests, not lambda-bracket formulas.
file update:
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index e37b9d7e68588acec131bcc7bcc9ed891b9aee8a..2d7d27c9a681d634895881d9160973d9d3b6f04c
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1846,7 +1846,7 @@
 The Virasoro algebra ($\lambda$-bracket
 $\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
 in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
-equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
+the OPE mode $T_{(3)}T = c/2$ therefore contributes $(c/2)/3! = c/12$ to the cubic $\lambda$-term)
 and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
 structures:
 \begin{itemize}
diff --git a/compute/genus_tower_catalan.py b/compute/genus_tower_catalan.py
index 68146462ea9ffb3632cd84a1b06f8259fbcecd32..b12e999d12fc397d6e66264594a02509c048155d
--- a/compute/genus_tower_catalan.py
+++ b/compute/genus_tower_catalan.py
@@ -184,23 +184,15 @@
     The genus-1 collision residue replaces rational poles by Weierstrass:
       r^{(1)}(z;tau) = (c/12)*wp''(z|tau) + 2T*(-wp(z|tau)) + dT*zeta(z|tau)
 
-    Wait -- let me be more careful. The Virasoro lambda-bracket is:
-      {T_lambda T} = dT + 2T*lambda + (c/2)*lambda^3
-
-    so c_0 = dT, c_1 = 2T, c_2 = 0, c_3 = c/2.
+    The Virasoro lambda-bracket is:
+      {T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3
 
-    The genus-0 m_2 in the bar complex is:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-                       = c_0 + c_1*lambda + c_3*lambda^3
-    (note c/12 not c/2 due to the 1/n! normalization in the Koszul sign).
+    Equivalently, the OPE/n-product data are
+      T_{(0)}T = dT, T_{(1)}T = 2T, T_{(2)}T = 0, T_{(3)}T = c/2,
+    so in divided-power form
+      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
+                       = dT + 2T*lambda + (c/12)*lambda^3.
 
-    Wait no: from the code m2_num:
-      m_2(T,T; lambda) = dT + 2T*lambda + (c/12)*lambda^3
-
-    This uses c_0 = dT (as d^1 T), c_1 = 2T (as 2*T coefficient of lambda),
-    c_3 = c/12 (coefficient of lambda^3). The 1/6 factor accounts for the
-    d-log kernel absorption plus combinatorial factors.
-
     At genus 1, the Stasheff m_2 picks up corrections from the torus geometry.
     The correction to the collision residue at genus 1 is:
 
@@ -639,9 +631,9 @@
     #
     # But wait: the r-matrix expansion R^{(1)} is in powers of z,
     # where z is the spectral parameter of the bar complex.
-    # The m_2(T,T;lambda) = sum_n c_n * lambda^n is already the
+    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
     # RESIDUE, and the genus-1 correction is:
-    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n
+    #   delta_m2(T,T;lambda) = sum_n delta(c_n) * lambda^n / n!
     # where delta(c_n) is the Eisenstein correction to the nth
     # OPE coefficient.
     #
diff --git a/compute/lib/examples/virasoro.py b/compute/lib/examples/virasoro.py
index 240e4387e9a9b4f8a7c4d114db89fc1ae92352c0..cd85d2080d651bed915eaa7f1a8c1b0b2954dc35
--- a/compute/lib/examples/virasoro.py
+++ b/compute/lib/examples/virasoro.py
@@ -232,7 +232,6 @@
       T_3 T = c/2 (coefficient of 1/(z-w)^4)
 
     Lambda-bracket: {T_lam T} = sum_{n>=0} (T_n T) * lam^n / n!
-      = dT + 2T*lam + 0 + (c/2)*lam^3/6
       = dT + 2T*lam + (c/12)*lam^3
 
     So the c/12 coefficient comes from c/2 divided by 3! = 6.
diff --git a/compute/lib/genus2_ordered_bar.py b/compute/lib/genus2_ordered_bar.py
index 8279509294ef1dad41dd34d57bbb512da282450f..ec9e8843931a0b9afab366ad18eaced640bfe6f7
--- a/compute/lib/genus2_ordered_bar.py
+++ b/compute/lib/genus2_ordered_bar.py
@@ -19,8 +19,8 @@
   f(z,w) = d_z log E(z,w)    (abelian differential of the third kind)
   B(z,w) = d_z d_w log E(z,w) (Bergman kernel)
 
-The genus-2 r-matrix for a chiral algebra A with lambda-bracket
-{a_lambda b} = c_0 + c_1*lambda + c_2*lambda^2 + ... is
+The genus-2 r-matrix for a chiral algebra A with n-products
+a_{(n)}b = c_n, so that {a_lambda b} = sum_{n>=0} c_n*lambda^n/n!, is
 (from spectral-braiding-core.tex, Cor. cor:genus-g-curvature-braiding):
 
   r^{Sigma_2}(z,w) = c_0 * f(z,w) + c_1 * B(z,w)
@@ -630,8 +630,9 @@
     r"""Genus-2 r-matrix for the Virasoro algebra Vir_c on Sigma_2.
 
     The Virasoro lambda-bracket:
-      {T_lambda T} = partial(T) + 2*T*lambda + (c/2)*lambda^3
-    so c_0 = partial(T), c_1 = 2T, c_2 = 0, c_3 = c/2.
+      {T_lambda T} = partial(T) + 2*T*lambda + (c/12)*lambda^3
+    equivalently T_{(0)}T = partial(T), T_{(1)}T = 2T,
+    T_{(2)}T = 0, T_{(3)}T = c/2.
 
     The genus-2 r-matrix:
       r^{Sigma_2}(z,w) = partial(T) * f(z,w) + 2T * B(z,w) + (c/4) * d_z^2 B(z,w)
@@ -639,7 +640,7 @@
     THREE sectors:
       Sector I (simple pole, from c_0 = partial(T)):   partial(T) * f(z,w)
       Sector II (double pole, from c_1 = 2T):          2T * B(z,w)
-      Sector III (quartic pole, from c_3 = c/2):       (c/4) * d_z^2 B(z,w)
+      Sector III (quartic pole, from T_{(3)}T = c/2):  (c/4) * d_z^2 B(z,w)
 
     KEY: Virasoro has c_0 = partial(T) != 0, so it is in the ENTANGLED regime.
     The B-cycle monodromies are:
@@ -657,9 +658,9 @@
     return {
         'algebra': f'Vir_{{{c}}}',
         'kappa': c / 2,
-        'c0': 'partial(T) (derivative of stress tensor)',
-        'c1': '2T (stress tensor)',
-        'c3': 'c/2 (central charge / 2)',
+        'c0': 'T_(0)T = partial(T)',
+        'c1': 'T_(1)T = 2T',
+        'c3': 'T_(3)T = c/2 (quartic OPE mode)',
         'regime': 'ENTANGLED (c_0 = partial(T) != 0)',
 
         'genus_tower': {
diff --git a/compute/tests/test_spectral_braiding.py b/compute/tests/test_spectral_braiding.py
index b7bedeb8e76547a981051f13ef3e16be09753460..25de73569ff621c817c859644647b47de73d3290
--- a/compute/tests/test_spectral_braiding.py
+++ b/compute/tests/test_spectral_braiding.py
@@ -387,8 +387,8 @@
 
         Virasoro OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)
         n-products: T_0 T = dT, T_1 T = 2T, T_2 T = 0, T_3 T = c/2
-        lambda-bracket: {T_lam T} = dT + 2T*lam + 0 + (c/2)*lam^3/3!
-                                   = dT + 2T*lam + (c/12)*lam^3
+        lambda-bracket: {T_lam T} = dT + 2T*lam + (c/12)*lam^3
+                        because (c/2)/3! = c/12
         r-matrix: r(z) = dT/z + 2T/z^2 + (c/2)/z^4
 
         The roundtrip reproduces the OPE pole structure.

tokens used
162,597
