# C16_lambda_bracket_v2 (590s)

**Findings**
- PROBLEM at [w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:134), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:138), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:148): the Virasoro lambda-bracket was advertised as `\sum a_n/\lambda^n`, which is an OPE-kernel presentation, not the Vol II divided-power lambda-bracket. EXACT edit applied: replaced that with `a_1 + a_2 \lambda + a_3 \lambda^3` and added the convention lock `a_3 = T_{(3)}T/3! = c/12`.
- PROBLEM at [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1067), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1165), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1175), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:419), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:517), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:527), [w-algebras-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:46), [w-algebras-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:134), [w-algebras-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:142): several lambda-brackets were still written with inverse powers of `\lambda`. EXACT edit applied: converted them to the divided-power polynomial forms
  `{T_\lambda T} = \partial T + 2T\lambda + (c/12)\lambda^3`,
  `{T_\lambda W} = \partial W + 3\lambda W`,
  `{W_\lambda W} = (c/360)\lambda^5 + (1/3)T\lambda^3 + (1/2)(\partial T)\lambda^2 + \cdots`.
- PROBLEM at [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1380), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1420), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:724), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:764): the sample Mathematica code encoded the same inverse-power convention. EXACT edit applied: rewrote `VirLambdaBracket` and `W3LambdaBracket` to polynomial lambda-brackets and changed the expansion from `Series[..., {lambda, Infinity, -n}]` to `Series[..., {lambda, 0, n}]`.
- PROBLEM at [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:6325) and [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:6615): the Ising and `c=1` specializations used the OPE coefficient instead of the divided-power lambda-bracket coefficient. EXACT edit applied: changed `(1/4)\lambda^3` to `(1/24)\lambda^3` for `c=1/2`, and `\tfrac{1}{2}\lambda^3` to `\tfrac{1}{12}\lambda^3` for `c=1`.
- PROBLEM at [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:2847) and [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3022): the BP Virasoro subalgebra still used `c_{\mathrm{BP}}/2` on the `\lambda^3` term and the surrounding prose matched that wrong convention. EXACT edit applied: changed the bracket to `\tfrac{c_{\mathrm{BP}}}{12}\lambda^3 + 2T\lambda + \partial T` and rewrote the prose to say the quartic OPE pole is equivalent to the divided-power term `(c_{\mathrm{BP}}/12)\lambda^3` in `\{T_\lambda T\}`.

**Verification**
- Grep sweep: no remaining old lambda-bracket spellings of the bad forms; the remaining `1/\lambda^3` and `1/\lambda^5` hits are `r`-matrix formulas, not lambda-brackets.
- `pytest -q compute/tests/test_pva_axioms.py`: `36 passed`.
- `pytest -q compute/tests/test_pva_descent_coefficients_engine.py -k 'Virasoro or virasoro or AP34'`: `2 passed`.
- `pytest -q compute/tests/test_examples.py -k 'virasoro or lambda'`: `12 passed`.
- `pytest -q compute/tests/test_pva_descent_coefficients_engine.py` still has an unrelated preexisting failure in `TestHeisenberg::test_heisenberg_D3_D5_skew_and_leibniz` (`assert 2*k*lam == 0`). I did not change that surface.
- I did not run a TeX build.


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
session id: 019d8809-5b90-7100-b639-4463e09b7a41
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
codex
Target is the Vol II lambda-bracket convention surface, specifically any Virasoro or related `\{\,_\lambda\,\}` formulas that still use non-divided-power coefficients. I’m checking the live manuscript and diff first, then I’ll patch only the files that actually contain the wrong convention and verify the remaining surface is coherent.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-formula-verification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-deep-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
 M Makefile
 M README.md
 M chapters/connections/3d_gravity.tex
 M chapters/connections/conclusion.tex
 M chapters/connections/concordance.tex
 M chapters/connections/hochschild.tex
 M chapters/connections/ht_bulk_boundary_line_frontier.tex
 M chapters/connections/line-operators.tex
 M chapters/connections/log_ht_monodromy_core.tex
 M chapters/connections/ordered_associative_chiral_kd.tex
 M chapters/connections/ordered_associative_chiral_kd_core.tex
 M chapters/connections/ordered_associative_chiral_kd_frontier.tex
 M chapters/connections/relative_feynman_transform.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/connections/thqg_3d_gravity_movements_vi_x.tex
 M chapters/connections/thqg_gravitational_complexity.tex
 M chapters/connections/thqg_holographic_reconstruction.tex
 M chapters/connections/thqg_line_operators_extensions.tex
 M chapters/connections/thqg_perturbative_finiteness.tex
 M chapters/connections/ym_synthesis.tex
 succeeded in 51ms:
---
name: vol2-deep-audit
description: Use when the user asks to audit, review, red-team, falsify, pressure-test, or run a findings-first mathematical pass on a Vol II theorem, chapter, proof, or live surface. Do not use for straightforward fix-only requests where the rectification skill is the better fit.
---

# Vol II Deep Audit

This is the findings-first counterpart to rectification.

## Inputs

- exact target file, theorem, definition, or live surface if given
- otherwise the smallest live surface implied by the prompt

## Audit posture

- Read before editing.
- Default output is prioritized findings, not prose reassurance.
- Treat every strong claim as false until a local proof, citation, or computation survives hostile checking.
- If the user asks for both audit and repair, start with the audit pass, then hand off to `$vol2-beilinson-rectification` for fixes.

thinking
**Updating skills and plans**

I need to utilize my skills effectively, likely focusing on formula verification and cross-volume propagation. Given that the user mentioned an adversarial auditor and fixer, I might consider a deep audit as well. I'll update my plan and search for lambda brackets in live surfaces. It could be worthwhile to inspect the inputs in main.tex, and I’ll run a targeted search for lambda bracket formulas throughout the repository. Using rg might help here too. Let’s proceed with commentary updates on skills and my approach.
codex
I’m using `$vol2-deep-audit` first to locate every live mis-normalized lambda-bracket, then `$vol2-formula-verification` and `$vol2-cross-volume-propagation` to repair and sweep copies of the same formula in manuscript and compute surfaces. Next step is a repo-wide search for `\lambda`-bracket patterns, `c/2`, and Virasoro convention notes so I can narrow the actual edit set.
Plan update
Audit-and-fix pass for the Vol II lambda-bracket divided-power convention surface.
  → Search the active Vol II manuscript and compute surfaces for lambda-bracket formulas, Virasoro central-term conventions, and V2-AP34 references.
  • Read the local context for each suspect occurrence, determine whether the divided-power convention is wrong, and identify the minimum truthful edits.
  • Apply exact fixes only where needed, then verify the remaining search surface and summarize each finding with file:line plus the exact edit applied.
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\{["'^'"\\n]*_\\\\lambda["'^'"\\n]*\\\\}|lambda-bracket|lambda bracket|V2-AP34|c/2|c\\\\/2|c/12|c\\\\/12|T_\\\\lambda T|T\\\\}_\\\\lambda T|\\{T_\\\\lambda T\\}|\\\\lambda\\"'^3'"' ." in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:\\{[^\n]*_\\lambda[^\n]*\\}|lambda-bracket|lambda bracket|V2-AP34|c/2|c\\/2|c/12|c\\/12|T_\\lambda T|T\\}_\\lambda T|\{T_\\lambda T\}|\\lambda\^3)
          ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n '"'^'"\\\\input|"'^'"\\\\include' main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
1212:\input{chapters/frame/preface}
1214:\input{chapters/theory/introduction}
1250:\input{chapters/theory/foundations}
1251:\input{chapters/theory/locality}
1252:\input{chapters/theory/axioms}
1253:\input{chapters/theory/equivalence}
1254:\input{chapters/theory/bv-construction}
1255:\input{chapters/theory/factorization_swiss_cheese}
1256:\input{chapters/theory/raviolo}
1257:\input{chapters/theory/raviolo-restriction}
1258:\input{chapters/theory/fm-calculus}
1259:\input{chapters/theory/orientations}
1260:\input{chapters/theory/fm-proofs}
1261:\input{chapters/theory/pva-descent-repaired}
1262:\input{chapters/theory/pva-expanded-repaired}
1299:\input{chapters/connections/bar-cobar-review}
1300:\input{chapters/connections/line-operators}
1301:\input{chapters/connections/ordered_associative_chiral_kd_core}
1302:\input{chapters/connections/dg_shifted_factorization_bridge}
1303:\input{chapters/connections/thqg_gravitational_yangian}
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' 'V2-AP34|divided powers|Vol II lambda-brackets use divided powers' ." in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
./CLAUDE.md:216:V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
./chapters/theory/pva-descent.tex:126:recording the same OPE coefficients $a_{(n)}b$ via divided powers $\lambda^{(n)} = \lambda^n/n!$.
./.git/logs/refs/heads/main:387:638bf84ab6d669221921bc4c80432fcb1ba372f5 d5ef5f04b42574681fd2715870c1055272225977 Raeez Lorgat <raeez@momentum.inc> 1775473014 +0200	commit: Vol II theory: AP44 divided powers, terminology, degree formula, foundations audit
./compute/tests/test_pva_descent_coefficients_engine.py:21:    * V2-AP34 (divided-power lambda-bracket c/12 * lam^3)
./compute/tests/test_pva_descent_coefficients_engine.py:161:    """Virasoro at central charge c; V2-AP34 divided-power convention."""
./compute/tests/test_pva_descent_coefficients_engine.py:168:        Path B: Divided-power form of OPE (V2-AP34).  The c/2 mode
./compute/tests/test_pva_descent_coefficients_engine.py:176:        # Explicit V2-AP34 guardrail: refuse the wrong c/2 * lam^3 form.
./.claude/commands/propagate.md:11:**AP49 Convention Alert**: Vol II uses lambda-brackets (divided powers). Vol I uses OPE modes. The coefficient at order n differs by 1/n!. When grepping for a Vol II formula in Vol I, apply the conversion BEFORE comparing.
./.git/logs/HEAD:443:638bf84ab6d669221921bc4c80432fcb1ba372f5 d5ef5f04b42574681fd2715870c1055272225977 Raeez Lorgat <raeez@momentum.inc> 1775473014 +0200	commit: Vol II theory: AP44 divided powers, terminology, degree formula, foundations audit
./.agents/skills/vol2-formula-verification/SKILL.md:28:- Vol II lambda-brackets use divided powers: the order-`n` coefficient is `a_(n)b / n!`.
./compute/lib/pva_descent_coefficients_engine.py:35:divided-power central term, V2-AP34).
./compute/lib/pva_descent_coefficients_engine.py:45:V2-AP34: Virasoro lambda-bracket uses divided-power central term
./compute/lib/pva_descent_coefficients_engine.py:673:    so the polynomial lambda-bracket (divided-power / V2-AP34) is
./compute/lib/pva_descent_coefficients_engine.py:678:    the divided-power convention at V2-AP34 in the Vol II CLAUDE.md.
./.agents/skills/vol2-compute-engine/SKILL.md:40:- `V2-AP34`: lambda-bracket coefficients use divided powers.
./.agents/skills/vol2-cross-volume-propagation/SKILL.md:38:- Vol II uses lambda-brackets with divided powers.
./AGENTS.md:546:   `AP126`, `V2-AP34`, `AP44`, `AP45`, `AP46`, `AP49`, and `AP113` recur across manuscript and compute layers.
./AGENTS.md:602:- Vol II lambda-brackets use divided powers;
./AGENTS.md:746:- Vol II uses lambda-brackets with divided powers;


thinking
**Searching for formulas**

I’ve run into a search failure due to regex issues, so I need to refine my approach. I should look for all lambda bracket formulas, possibly in both TeX and code, and consider using simpler patterns. I'll need to inspect compute tests and code for any guardrails and search for terms like `lambda^3`, `T_\lambda T`, and `W_\lambda W`. I should ensure I'm following the correct conventions, particularly regarding divided powers for Virasoro.
thinking
**Searching for wrong coefficients**

I might need to check W3 if I find anything incorrect. I should search for those coefficients, specifically `c/2*lambda^3` and `c/3*lambda^5`, within active and compute surfaces. I'll use `rg` with fixed strings and general patterns like `lambda^`. Additionally, I should inspect the relevant pva files. After the search, maybe I’ll consider updating the plan statuses. For now, I will run `rg` with multiple patterns in parallel to maximize efficiency.
codex
The first pass confirms the repo already encodes `V2-AP34`, but I still need the live occurrence sweep because several manuscript files are dirty and the wrong coefficient can hide in examples, frontier text, or compute comments. I’m now grepping the concrete formula variants directly rather than relying on one broad regex.
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' -F 'lambda"'^3'"' chapters compute working_notes.tex README.md CLAUDE.md AGENTS.md .agents .claude" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' -F '{T_\\lambda T}' chapters compute working_notes.tex README.md CLAUDE.md AGENTS.md .agents .claude" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' -F 'lambda-bracket' chapters compute working_notes.tex README.md CLAUDE.md AGENTS.md .agents .claude" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' -F 'c/2' chapters compute working_notes.tex README.md CLAUDE.md AGENTS.md .agents .claude" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
AGENTS.md:188:3. the convention bridge: grading, shifts, OPE modes versus lambda-brackets, open/closed colors, genus and degree scope, Vol I versus Vol II versus Vol III normalization;
AGENTS.md:232:- Vol II `CLAUDE.md`: `V2-AP1` through `V2-AP39` + `FM58`-`FM68` for the local `E_1/E_infinity` hierarchy, lambda-bracket, standalone, and session-specific hazards.
AGENTS.md:437:- lambda-bracket versus OPE-mode conventions;
AGENTS.md:602:- Vol II lambda-brackets use divided powers;
AGENTS.md:608:- Vol I uses OPE modes, Vol II uses lambda-brackets, Vol III may use motivic or categorical normalizations;
AGENTS.md:746:- Vol II uses lambda-brackets with divided powers;
AGENTS.md:785:- if an `r`-matrix or lambda-bracket changed, did you perform the level-prefix or divided-power check;
CLAUDE.md:163:- PVA is (-1)-shifted: lambda-bracket on H*(A,Q) has shifted parity.
CLAUDE.md:216:V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
README.md:35:- **VI. Three-Dimensional Quantum Gravity**: The climax; Virasoro lambda-bracket generates the full gravitational theory; critical string dichotomy c=26 vs c!=26
working_notes.tex:7893:  computation (the lambda-bracket sesquilinearity propagated
.claude/hooks/beilinson-gate.sh:129:    PROPAGATION="AP5/AP49: Formula edit. Grep ALL THREE volumes. Convention: Vol I=OPE modes, Vol II=lambda-brackets (1/n! factor)."
.agents/skills/vol2-formula-verification/SKILL.md:28:- Vol II lambda-brackets use divided powers: the order-`n` coefficient is `a_(n)b / n!`.
.agents/skills/vol2-formula-verification/SKILL.md:46:- If the formula differs across volumes, explicitly perform the OPE-mode versus lambda-bracket conversion before comparing.
.agents/skills/vol2-compute-engine/SKILL.md:21:   - OPE mode versus lambda-bracket
.agents/skills/vol2-compute-engine/SKILL.md:40:- `V2-AP34`: lambda-bracket coefficients use divided powers.
.agents/skills/vol2-cross-volume-propagation/SKILL.md:38:- Vol II uses lambda-brackets with divided powers.
.claude/commands/rectify.md:30:- **AP44**: lambda-bracket coefficient = a_{(n)}b/n!, NOT a_{(n)}b.
.claude/commands/rectify.md:39:Convention check (AP49): Vol I uses OPE modes. Vol II uses lambda-brackets. The coefficient at order n differs by 1/n!.
.claude/commands/verify.md:16:- **Convention bridge**: Verify the same formula in Vol I OPE-mode convention (AP49: divide lambda-bracket coefficients by n!)
 succeeded in 52ms:
CLAUDE.md:216:V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
working_notes.tex:1333:\partial T + 2T\lambda + \frac{c}{12}\,\lambda^3
working_notes.tex:1337:quartic pole ($\frac{c}{12}\lambda^3$, the central charge).
working_notes.tex:7840:\partial T + 2T\lambda + \frac{c}{12}\,\lambda^3
working_notes.tex:7843:pole ($\lambda^3$ in the $\lambda$-bracket) forces
working_notes.tex:8018:  + 14\lambda^3\, T
working_notes.tex:8184:  - 84\lambda^3\,\partial T
working_notes.tex:8215:  & $\frac{c}{12}\lambda^3$ \\[3pt]
working_notes.tex:8300:pole persists at $c = 0$ (the $\lambda^3$ term is purely
working_notes.tex:8544:$\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$.
working_notes.tex:9065:$\{T {}_\lambda T\} = (\partial + 2\lambda)\, T + \tfrac{c}{12}\,\lambda^3$
working_notes.tex:9332:\partial T + 2T\lambda + \frac{c}{12}\,\lambda^3.
working_notes.tex:9388:\int_0^\infty e^{-\lambda z}\,\frac{c}{12}\lambda^3\,d\lambda
working_notes.tex:9453:+ \tfrac{c}{12}\lambda^3(\lambda + 2\mu)$.
working_notes.tex:9472:&\tfrac{c}{12}\bigl[\lambda^4 + 2\lambda^3\mu - \mu^4 - 2\mu^3\lambda\bigr]
working_notes.tex:11413:\partial T + 2T\lambda + \frac{c}{12}\lambda^3.
working_notes.tex:11645:The entire infinite tower traces to the quartic pole in the Virasoro OPE --- equivalently, to the $\lambda^3$ term in the $\lambda$-bracket.  For affine Kac--Moody algebras (where the maximal OPE pole is double, $\lambda^1$), the $\Ainf$ structure truncates at $m_2$ and the soft hierarchy terminates at the subleading level.  For the Virasoro algebra, the quartic pole forces $m_3 \ne 0$, which cascades through the Stasheff identities to produce $m_k \ne 0$ for all $k$, and hence $S^{(k)} \ne 0$ for all $k$.  The statement ``infinitely many soft graviton theorems'' is the same statement as ``the Virasoro $\Ainf$ structure does not truncate,'' which is the same statement as ``the quartic pole in the stress-tensor OPE forces infinite shadow depth.''
working_notes.tex:12594:+ \frac{c_{\mathrm{DS}}}{12}\,\lambda^3.
working_notes.tex:12644:+ \frac{c_{\mathrm{DS}}}{12}\,\lambda^3\Bigr).
working_notes.tex:12665:$T^{\mathrm{DS}}$ has a $\lambda^3$ term (quartic pole)
 succeeded in 51ms:
Total output lines: 1155

CLAUDE.md:216:V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
working_notes.tex:567:$r$-matrix & $\Omega_\fg/z$ & $(c/2)/z^3 + 2T/z$ \\[3pt]
working_notes.tex:576:$r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$.  The coproduct carries
working_notes.tex:606:$\infty$.  $r$-matrix: $r(z) = (c/2)/z^3 + 2T/z$ (two poles,
working_notes.tex:608:$\kappa = c/2$; $\kappa^! = (26-c)/2$;
working_notes.tex:699:$\chi_j(\tau) = \mathrm{tr}_{L_j}(q^{L_0 - c/24})$
working_notes.tex:758:$R(z) = 1 + \hbar\,((c/2)/z^3 + 2T/z) + O(\hbar^2)$.
working_notes.tex:1348:r(z) \;=\; (c/2)/z^3 + 2T/z.
working_notes.tex:1367:  with $\kappa = \kappa(\mathrm{Vir}_c) = c/2$.
working_notes.tex:1598:The $r$-matrix $r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$ carries
working_notes.tex:1777:$r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$ controls BTZ
working_notes.tex:1778:thermodynamics.  The leading coefficient $c/2 = \kappa$ is the
working_notes.tex:1818:  & $c/2$ & $\dim(\fg)\frac{k+h^\vee}{2h^\vee}$
working_notes.tex:1913:$\dfib^{\,2} = (c/2) \cdot \omega_1 \neq 0$.
working_notes.tex:1914:The bar complex is curved.  The curvature $c/2$ is the modular
working_notes.tex:1934:S_2 &= c/2, \\
working_notes.tex:1953:corrections to quantum gravity: $\kappa = c/2$, $\alpha = 2$ (the
working_notes.tex:2006:derives from $\kappa = c/2$, the leading coefficient of

thinking
**Searching for specific patterns**

I have a lot of results, but I need to focus specifically on incorrect conventions. Some entries show inverse powers like `1/\lambda^3`, which seem suspicious. I should search for `c/2.*lambda^3` specifically, but it looks like my previous search got truncated due to being too large. I'll try using targeted regex patterns within the right context. I might also look for `c/3.*lambda^5` and check candidate files across the repository.
codex
The broad scan shows most live surfaces already use `c/12`, but there are still a few suspect forms: direct `c/2 ... lambda^3` matches, and some example/frontier files are writing the lambda-bracket with inverse powers of `\lambda`, which is a different kernel and likely a notation leak. I’m isolating those now and reading the surrounding context before patching.
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' 'c\\s*/\\s*3["'^'"\\n]{0,120}lambda\\"'^5|lambda'"\\"'^5[''^'"\\n]{0,120}c\\s*/\\s*3' chapters compute working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\{T["'^'"\\n]*_\\\\lambda["'^'"\\n]*T["'^'"\\n]*\\\\}.*lambda\\"'^3|lambda'"\\"'^3.*'"\\\\{T["'^'"\\n]*_\\\\lambda["'^'"\\n]*T["'^'"\\n]*\\\\}' chapters compute working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' 'c\\s*/\\s*2["'^'"\\n]{0,120}lambda\\"'^3|lambda'"\\"'^3[''^'"\\n]{0,120}c\\s*/\\s*2' chapters compute working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '/lambda\\"'^3|/lambda'"\\"'^5|'"\\\\lambda\\"'^3'"\\}|\\\\lambda\\"'^5'"\\}' chapters" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:\\{T[^\n]*_\\lambda[^\n]*T[^\n]*\\}.*lambda\^3|lambda\^3.*\\{T[^\n]*_\\lambda[^\n]*T[^\n]*\\})
          ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
chapters/examples/w-algebras-w3.tex:522:$P_5\,\lambda^5 = (c/360)\lambda^5$ is a scalar multiple
chapters/examples/w-algebras-w3.tex:817:r^{WW}(\lambda,\mu) &= \frac{c/360}{\lambda^5 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{3\lambda^3 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{2\lambda^2 \mu} \\
chapters/examples/w-algebras-w3.tex:1934:$1/z^5$ & $c/360$ (from $\lambda^5$)
chapters/examples/w-algebras.tex:831:r^{WW}(\lambda,\mu) &= \frac{c/360}{\lambda^5 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{3\lambda^3 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{2\lambda^2 \mu} \\
chapters/examples/w-algebras.tex:1176:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras.tex:1422: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
chapters/examples/w-algebras-frontier.tex:142:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-frontier.tex:559:r^{W_3 W_3}(\lambda) &= \frac{c/360}{\lambda^5}
chapters/examples/w-algebras-conditional.tex:184:r^{WW}(\lambda,\mu) &= \frac{c/360}{\lambda^5 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{3\lambda^3 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{2\lambda^2 \mu} \\
chapters/examples/w-algebras-conditional.tex:528:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-conditional.tex:766: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
compute/lib/cross_volume_deep_bridge.py:226:    {W_lambda W} = ... (c/360)*lambda^5 + lower order (nonlinear)
compute/lib/cross_volume_deep_bridge.py:241:            ('W', 'W'): {5: c / 360},  # leading: (c/3*5!)*lambda^5
compute/lib/cross_volume_deep_bridge.py:379:    """Verify leading WW bracket: {W_lambda W} has (c/360)*lambda^5 term.
chapters/connections/thqg_fm_calculus_extensions.tex:1354: to $\lambda^5/5!$; multiplying by the OPE coefficient $c/3$
 succeeded in 51ms:
compute/lib/examples/virasoro.py:21:packages this as (c/2) * lambda^3 / 3! = (c/12) * lambda^3.
chapters/connections/thqg_fm_calculus_extensions.tex:937: to $\lambda^3/3!$; multiplying by the OPE coefficient $c/2$
chapters/connections/celestial_holography_core.tex:983:The holomorphic-topological twist of $3$d gravity on $\mathbb{C} \times \mathbb{R}_{\ge 0}$ produces a boundary Virasoro algebra $\mathrm{Vir}_c$. The positive-helicity graviton maps to the stress tensor~$T(z)$. The Virasoro $\lambda$-bracket $\{T{}_\lambda T\} = (\partial + 2\lambda)\,T + \frac{c}{12}\,\lambda^3$ Laplace-transforms to $r^{\mathrm{Lap}}(z) = \partial T/z + 2T/z^2 + (c/2)/z^4$. After $d\log$ absorption, the $\partial T$ term drops, producing the two-pole collision $r$-matrix:
compute/tests/test_pva_axioms.py:424:        Factor: c/2 * lambda^3 / 3! = c/2 * lambda^3 / 6 = c/12 * lambda^3.
compute/tests/test_cross_volume_deep_bridge.py:110:        """The lambda^3 term gives c/2 at z^{-4}."""
 succeeded in 51ms:
chapters/examples/w-algebras.tex:1069:\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
chapters/examples/w-algebras.tex:1070:&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
chapters/examples/w-algebras.tex:1176:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-frontier.tex:48:\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
chapters/examples/w-algebras-frontier.tex:142:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-frontier.tex:556:r^{TT}(\lambda) &= \frac{c/12}{\lambda^3}
chapters/examples/w-algebras-frontier.tex:559:r^{W_3 W_3}(\lambda) &= \frac{c/360}{\lambda^5}
chapters/examples/w-algebras-frontier.tex:560: + \frac{T/3}{\lambda^3}
chapters/examples/w-algebras-frontier.tex:565: + \frac{T_4}{\lambda^5}
chapters/examples/w-algebras-conditional.tex:421:\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
chapters/examples/w-algebras-conditional.tex:422:&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
chapters/examples/w-algebras-conditional.tex:528:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/connections/thqg_fm_calculus_extensions.tex:934: $\frac{c}{2} \cdot \frac{\lambda^3}{3!}
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3984:\frac{\{T^{(i)}_\lambda T^{(j)}\}}{\lambda^3},
exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-conditional.tex | sed -n '412,438p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/rosetta_stone.tex | sed -n '6318,6630p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras.tex | sed -n '1060,1080p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-frontier.tex | sed -n '36,70p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  1060	m_k(a_1, \ldots, a_k) = \sum_{n_1, \ldots, n_{k-1} \in \Z} \frac{C_{n_1, \ldots, n_{k-1}}(a_1, \ldots, a_k)}{\lambda_1^{n_1+1} \cdots \lambda_{k-1}^{n_{k-1}+1}}.
  1061	\end{equation}
  1062	
  1063	\subsection{Virasoro: Explicit Formulas}
  1064	
  1065	\subsubsection{The Binary Operation $m_2(T,T)$}
  1066	
  1067	\textbf{Singular Part ($\lambda$-bracket):}
  1068	\begin{align}
  1069	\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
  1070	&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
  1071	\end{align}
  1072	
  1073	\textbf{In Mode Expansion:}
  1074	\begin{align}
  1075	\{T_m {}_\lambda T_n\} &= \sum_{k=0}^{m} \binom{m}{k} (-\lambda)^k (k-m-1) T_{m+n-k}\\
  1076	&\quad + \frac{c}{12} \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m-2)(k-m-1)(k-m) \delta_{m+n-k,0}.
  1077	\end{align}
  1078	
  1079	\textbf{Regular Part:}
 succeeded in 51ms:
   412	m_k(a_1, \ldots, a_k) = \sum_{n_1, \ldots, n_{k-1} \in \Z} \frac{C_{n_1, \ldots, n_{k-1}}(a_1, \ldots, a_k)}{\lambda_1^{n_1+1} \cdots \lambda_{k-1}^{n_{k-1}+1}}.
   413	\end{equation}
   414	
   415	\subsection{Virasoro: Explicit Formulas}
   416	
   417	\subsubsection{The Binary Operation $m_2(T,T)$}
   418	
   419	\textbf{Singular Part ($\lambda$-bracket):}
   420	\begin{align}
   421	\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
   422	&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
   423	\end{align}
   424	
   425	\textbf{In Mode Expansion:}
   426	\begin{align}
   427	\{T_m {}_\lambda T_n\} &= \sum_{k=0}^{m} \binom{m}{k} (-\lambda)^k (k-m-1) T_{m+n-k}\\
   428	&\quad + \frac{c}{12} \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m-2)(k-m-1)(k-m) \delta_{m+n-k,0}.
   429	\end{align}
   430	
   431	\textbf{Regular Part:}
 succeeded in 51ms:
    36	
    37	The operation $m_k$ is a Laurent series in $\lambda_1, \ldots, \lambda_{k-1}$:
    38	\begin{equation}
    39	m_k(a_1, \ldots, a_k) = \sum_{n_1, \ldots, n_{k-1} \in \Z} \frac{C_{n_1, \ldots, n_{k-1}}(a_1, \ldots, a_k)}{\lambda_1^{n_1+1} \cdots \lambda_{k-1}^{n_{k-1}+1}}.
    40	\end{equation}
    41	
    42	\subsection{Virasoro: Explicit Formulas}
    43	
    44	\subsubsection{The Binary Operation $m_2(T,T)$}
    45	
    46	The singular part (the $\lambda$-bracket) is
    47	\begin{align}
    48	\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
    49	\end{align}
    50	In modes,
    51	\begin{align}
    52	\{T_m {}_\lambda T_n\} &= \sum_{k=0}^{m} \binom{m}{k} (-\lambda)^k (k-m-1) T_{m+n-k}\\
    53	&\quad + \frac{c}{12} \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m-2)(k-m-1)(k-m) \delta_{m+n-k,0}.
    54	\end{align}
    55	The regular part gives the normally ordered product:
 succeeded in 51ms:
  6318	algebra, and bar of a subalgebra is a sub-coalgebra.
  6319	
  6320	\smallskip
  6321	\noindent
  6322	\emph{Binary operation.}
  6323	At $k = 2$ (Ising model, $c = 1/2$), the single generator
  6324	is $T$ and the binary operation is
  6325	$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
  6326	+ \partial T$.
  6327	This is the standard Virasoro $m_2$ at $c = 1/2$.
  6328	For $k = 2$, the GKO bar complex is isomorphic to
  6329	$\bar{B}^{\mathrm{ch,ord}}(\mathrm{Vir}_{1/2})$, already
  6330	in the landscape as a specialisation of the Virasoro
  6331	row at $c = 1/2$.
  6332	
  6333	\smallskip
  6334	\noindent
  6335	\emph{$r$-matrix.}
  6336	The coset $r$-matrix is the restriction of the tensor
  6337	product $r$-matrix to the $V_k$-singlet sector.



thinking
**Searching for coefficients**

I'm noticing that the Rosetta stone lines have incorrect coefficients for c=1/2 and c=1. Specifically, c/12 at c=1/2 should be 1/24, not 1/4. This needs a fix! There are more issues, so I’ll search for explicit numeric values like 1/4 or 1/2 lambda^3 in m2 formulas. I'll focus on searching patterns around these terms to identify any discrepancies. I'll also inspect the ordered_associative_chiral_kd_frontier lines and w-algebras-frontier for further context.
thinking
**Searching lambda patterns**

I'm considering the best approach to search for `lambda^3` in the chapters. I think using generic `rg` might not work out too well, so I need to focus on specific patterns like `1/2`, `/2`, or `c_BP`. I'll search for `\lambda^3` that comes right after these coefficients, but I also need to keep in mind the correct formulas, such as `c/12` and `1/3 T λ^3` for W3. I should be particular about targeting `m_2(T, T)` and `T_\lambda T`, especially in their proper contexts.
thinking
**Searching for occurrences**

I definitely need to fix this. I should search for all occurrences of `m_2(T, T;` because that might help reveal more information. It's interesting to think about how something that seems simple could lead to greater insights once I dig deeper. So, I'll need to go through my data systematically to uncover all instances and see what else they might reveal. This could be crucial!
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' 'm_2\\(T, ?T;["'^'"\\n]*lambda\\)|m_2\\(T,T;["'^'"\\n]*lambda\\)|\\{T_\\\\lambda T\\}|\\{T\\{\\}_\\\\lambda T\\}|\\{T\\(z_1\\) \\{\\}_\\\\lambda T\\(z_2\\)\\}' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\frac\\{c\\}\\{2\\}\\\\lambda\\"'^3|'"\\\\tfrac\\{c\\}\\{2\\}\\\\lambda\\"'^3|c/2'"\\\\,?\\\\lambda\\"'^3|c'"\\s*\\\\lambda\\"'^3/2'"' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\frac\\{["'^}]*'"\\}\\{2\\}\\\\lambda\\"'^3|'"\\\\tfrac\\{["'^}]*'"\\}\\{2\\}\\\\lambda\\"'^3|'"\\(1/2\\)\\\\lambda\\"'^3|'"\\(1/4\\)\\\\lambda\\"'^3|c_'"\\{["'^}]*'"\\}/2\\\\,\\\\lambda\\"'^3|c_'"\\{["'^}]*'"\\}/2\\\\lambda\\"'^3|c_'"\\{["'^}]*'"\\}\\\\lambda\\"'^3/2'"' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\frac\\{c\\}\\{3\\}\\\\lambda\\"'^5|'"\\\\tfrac\\{c\\}\\{3\\}\\\\lambda\\"'^5|c/3'"\\\\,?\\\\lambda\\"'^5|c'"\\s*\\\\lambda\\"'^5/3'"' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
working_notes.tex:7842:defines $m_2(T,T;\lambda) = \{T{}_\lambda T\}$.  The quartic OPE
working_notes.tex:8212:$m_2(T,T;\lambda)$
working_notes.tex:11476:m_2(T, T;\, \lambda)\big|_{\lambda = 0}
working_notes.tex:11503:m_2(T, T;\, \lambda)\big|_{O(\lambda)}
working_notes.tex:15029:m_2(T,T;\,\lambda)
working_notes.tex:15327:\item the binary operation $m_2(T,T;\lambda)
chapters/frame/preface_trimmed.tex:474:infinite: $m_2(T,T;\lambda)
compute/genus_tower_catalan.py:193:      m_2(T,T; lambda) = sum_n T_{(n)}T * lambda^n / n!
compute/genus_tower_catalan.py:634:    # The m_2(T,T;lambda) = sum_n c_n * lambda^n / n! is already the
compute/genus_tower_catalan.py:648:    # The m_2 operation is m_2(T,T;lambda) where lambda is the
compute/m_even_symmetric_vanishing.py:4:  m_2: NOT zero (just m_2(T,T;lambda) = dT + 2*lambda*T + c/12*lambda^3)
chapters/frame/preface.tex:1288:m_2(T,T;\lambda) \;=\; \frac{c}{12}\lambda^3 + 2T\lambda + \partial T
chapters/connections/thqg_fm_calculus_extensions.tex:900:m_2(T, T;\, \lambda)
chapters/connections/thqg_fm_calculus_extensions.tex:964: = -\lambda\, m_2(T,T;\,\lambda)$
chapters/connections/thqg_fm_calculus_extensions.tex:967: = (\lambda + \partial)\, m_2(T,T;\,\lambda)$
chapters/connections/3d_gravity.tex:614:m_2(T, T;\, \lambda)
chapters/connections/3d_gravity.tex:1421:h\bigl(m_2(T, T;\, \lambda)\bigr)
chapters/connections/3d_gravity.tex:1657:\item the binary operation $m_2(T,T;\lambda)
chapters/examples/rosetta_stone.tex:6325:$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
chapters/examples/rosetta_stone.tex:6615:$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
 exited 1 in 51ms:

 exited 1 in 51ms:

 succeeded in 51ms:
chapters/examples/rosetta_stone.tex:6325:$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
chapters/examples/rosetta_stone.tex:6615:$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3

thinking
**Inspecting suspicious files**

I need to examine some suspicious files related to inverse powers and maybe c_BP/2. I'll search for specific patterns like `lambda^3`, and also consider `c_BP` or `BP`. There's a chance that the frontier file is incorrectly using c_BP/2 in the bracket of BP algebra. So, it looks like I need to dig deeper into these files to find out what's going on! Let's see what patterns I can uncover.
exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '3014,3030p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-frontier.tex | sed -n '548,566p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-frontier.tex | sed -n '136,150p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '2838,2856p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   548	
   549	\begin{computation}[$\mathcal{W}_4$ spectral $r$-matrix;
   550	\ClaimStatusConditional]
   551	\label{comp:w4-r-matrix}
   552	\index{W4@$\mathcal{W}_4$!r-matrix}%
   553	The $\mathcal{W}_4$ $r$-matrix is a $3 \times 3$ matrix in the
   554	$\{T, W_3, W_4\}$ basis. The diagonal components are:
   555	\begin{align}
   556	r^{TT}(\lambda) &= \frac{c/12}{\lambda^3}
   557	 + \frac{2T}{\lambda} + \frac{\partial T}{\lambda^0},
   558	 \\
   559	r^{W_3 W_3}(\lambda) &= \frac{c/360}{\lambda^5}
   560	 + \frac{T/3}{\lambda^3}
   561	 + \frac{\partial T/2}{\lambda^2}
   562	 + \frac{(32/(5c+22))\Lambda}{\lambda}
   563	 + \cdots, \\
   564	r^{W_4 W_4}(\lambda) &= \frac{c_4}{\lambda^7}
   565	 + \frac{T_4}{\lambda^5}
   566	 + \cdots
 succeeded in 51ms:
  2838	\end{equation}
  2839	where $|a|$ denotes the parity ($0$ for bosonic, $1$ for
  2840	fermionic). The remaining $11$ independent $\lambda$-brackets
  2841	(from which the collision residues and bar differential are
  2842	extracted) are:
  2843	
  2844	\begin{align}
  2845	\{T_\lambda\, T\}
  2846	&\;=\;
  2847	\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
  2848	+ 2T\lambda + \partial T,
  2849	\label{eq:bp-TT}
  2850	\\[4pt]
  2851	\{T_\lambda\, \Gp\}
  2852	&\;=\;
  2853	\tfrac{3}{2}\,\Gp\lambda + \partial\Gp,
  2854	\label{eq:bp-TGp}
  2855	\\[4pt]
  2856	\{T_\lambda\, \Gm\}
 succeeded in 51ms:
   136	and in modes,
   137	$\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
   138	The self-bracket $\{W_\lambda W\}$
   139	(cf.\ equation~\eqref{eq:m2WW-recap} for the compact
   140	polynomial form) is
   141	\begin{align}
   142	\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
   143	&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
   144	\end{align}
   145	
   146	\subsubsection{The Ternary Operations}
   147	
   148	The pure-$T$ operation $m_3(T,T,T)$ agrees with Virasoro.
   149	The mixed operation $m_3(T,T,W)$ is
   150	\begin{equation}
 succeeded in 51ms:
  3014	(Computation~\texttt{comp:virasoro-m3} of the examples chapter),
  3015	with $c$ specialised to $c_{\mathrm{BP}}(k')=(k'-15)/(k'+3)$.
  3016	The $T$-sector shadow obstruction tower is therefore the Virasoro shadow
  3017	tower at the BP central charge: infinite depth,
  3018	class~$\mathbf{M}$.
  3019	
  3020	\emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
  3021	into the matter sector.}
  3022	The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
  3023	$T$--$T$ OPE generates a depth-$3$ collision residue.
  3024	However, when one of the three inputs is a fermionic
  3025	generator $\Gp$ (or $\Gm$), the transferred product
  3026	$m_3(T,T,\Gp)$ receives contributions only from the
  3027	$T$--$\Gp$ collision (which has a double pole,
  3028	depth~$1$) and from the composite
  3029	$m_2(m_2(T,T),\Gp) - m_2(T,m_2(T,\Gp))$ (the
  3030	$\Ainf$-relation). The quartic pole in the $T$--$T$

thinking
**Inspecting results**

I’ve got results listed in d439, and I need to examine those related to `c/12` — so far, everything seems good. But there are some variants that use different central symbols, like `c_BP`. I need to search for `T_\lambda` along with specific line numbers. It might help to look across chapters. Alright, let’s compile that list and see what I find!
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\{T\\(["'^'"\\n]*\\{\\}_\\\\lambda T\\(["'^'"\\n]*\\)' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' 'm_2\\(T, ?T;["'^'"\\n]*\\)|m_2\\(T,T;["'^'"\\n]*\\)' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' -F '{T_\\lambda T}' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' -F '{T{}_\\lambda T}' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:\\{T\([^\n]*\{\}_\\lambda T\([^\n]*\))
          ^
error: repetition quantifier expects a valid decimal
 exited 1 in 52ms:

 exited 1 in 52ms:

 succeeded in 52ms:
working_notes.tex:7842:defines $m_2(T,T;\lambda) = \{T{}_\lambda T\}$.  The quartic OPE
working_notes.tex:7918:\underbrace{m_3(m_2(T,T;\lambda_{12}),\, T,\, T;\,
working_notes.tex:7921:\underbrace{m_3(T,\, m_2(T,T;\lambda_{23}),\, T;\,
working_notes.tex:7925:\underbrace{m_3(T,\, T,\, m_2(T,T;\lambda_{34});\,
working_notes.tex:7937:handle the substitution of $m_2(T,T;\lambda_{12})
working_notes.tex:8212:$m_2(T,T;\lambda)$
working_notes.tex:11476:m_2(T, T;\, \lambda)\big|_{\lambda = 0}
working_notes.tex:11503:m_2(T, T;\, \lambda)\big|_{O(\lambda)}
working_notes.tex:15029:m_2(T,T;\,\lambda)
working_notes.tex:15070:S_1 &= +m_3\bigl(m_2(T,T;\lambda_1),\, T,\, T;\;
working_notes.tex:15072:S_2 &= -m_3\bigl(T,\, m_2(T,T;\lambda_2),\, T;\;
working_notes.tex:15074:S_3 &= +m_3\bigl(T,\, T,\, m_2(T,T;\lambda_3);\;
working_notes.tex:15327:\item the binary operation $m_2(T,T;\lambda)
working_notes.tex:17800:  $m_2(T,T;\,0) = \partial T$,
chapters/frame/preface_trimmed.tex:474:infinite: $m_2(T,T;\lambda)
compute/symmetric_point_catalan.py:39:        # m_2(T,T; 1) = dT + 2T*1 + (c/12)*1 => T-coeff = 2
compute/symmetric_point_catalan.py:57:        # m_2(T,T;1) has scalar = c/12 * 1^3 = c/12. P_2 = scalar/(c/12) = 1
chapters/frame/preface.tex:1288:m_2(T,T;\lambda) \;=\; \frac{c}{12}\lambda^3 + 2T\lambda + \partial T
compute/m_even_symmetric_vanishing.py:4:  m_2: NOT zero (just m_2(T,T;lambda) = dT + 2*lambda*T + c/12*lambda^3)
chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1425:$m_3(m_2(T,T),T,T)$, where $m_2(T,T;\lambda_{23})







thinking
**Inspecting candidate files**

I need to take a closer look at more candidate files like w-algebras.tex, inverse powers, and conditional/frontier. I want to check if they’re active. The main.tex includes files like w-algebras-virasoro.tex and w-algebras-w3.tex, but not those two. The user asked about Vol II, possibly regarding active and stale surfaces. I’ll determine the minimal edits needed while ensuring they’re truthful, focusing only on the files within the assigned scope. It might be necessary to document my findings as well.
thinking
**Deciding on audit notes**

So, the task hints that assigned files might not include the audit ledger, but AGENTS suggests I should record actionable findings in linear_read_notes.md. Since this task is substantial, I’m considering appending an entry. However, the user specifically requested a fix in Vol II. I realize that the audit ledger might not be part of the assigned files. To respect the user’s request for minimal edits, I might skip updating the ledger unless absolutely necessary, treating AGENTS as guidance.
thinking
**Inspecting findings for fixes**

I’m considering that as an "adversarial auditor + fixer," I should focus on outputting findings without modifying the audit ledger unless absolutely necessary. I need to inspect both active and stale surfaces and search for any suspect inverse-power lambda-bracket formulas throughout the repo. I should check files like w-algebras.tex, conditional, frontier, and ensure stable elements are correct. Also, I wonder if there are more inverse power formulas for T or W in other files, but my initial search didn’t reveal much.
thinking
**Evaluating consistent definitions**

I'm realizing the intention is to define `m_k` as Laurent series, but they interchangeably use "lambda-bracket" and "singular part," which feels inconsistent. I might want to correct this by shifting to polynomial lambda-bracket formulas and mentioning how coefficients relate to the Laurent kernel. I need to examine those sections more closely, as it seems some files might be outdated duplicates while others could need an update to avoid misleading future audits. There are four files that show the same bug, so I should probably patch them all similarly.
thinking
**Addressing notation issues**

I'm noticing a similar problem with inverse powers and the c/360 notation. They mentioned looking into lambda-bracket formulas to fix incorrect conventions, so if inverse powers are misused, I’ll need to convert them to divided-power polynomials. Looking at `r^{TT}(\lambda)`, it might not be a lambda-bracket but rather an r-matrix, which I don't need to fix. Also, I find the naming of `r^{TT}(\lambda)` a bit odd since it depends on the spectral parameter, not lambda. I should search for symbols like `c_BP/2 λ^3` and adjust the notation using targeted regex searches for lines containing `{T_\lambda` while avoiding certain formats in bash.
thinking
**Considering command options**

I’m pondering whether I could still use pipes, but maybe avoiding separators is safer. They mentioned not to chain with separators like echo, which makes sense. Piping might work fine, but just to play it safe, I could opt for using `rg` and perhaps even incorporate `perl`. It seems simpler and could maintain clarity in my commands. I want to ensure I’m following best practices while keeping everything efficient!
thinking
**Searching for lambda equations**

I'm considering searching for `lambda^3` plus `1/4` to narrow my results. I could also look for variations like `1/4).*lambda^3` or `1/2.*lambda^3`, but maybe I should focus on just the Rosetta database. I think checking `/2 λ^3` with a custom symbol might help, especially with BP. I'll also try `c_{\mathrm{.*}}/2 λ^3`, ensuring I avoid `c_` as `12`. Let's move forward with that targeted search and inspect the findings!
codex
I’ve confirmed three real bug classes, not one: a live frontier chapter with `c_BP/2` instead of divided-power `c_BP/12`, a duplicated W-algebra derivation that writes lambda-brackets as inverse-power Laurent kernels, and two concrete Rosetta examples whose specialized Virasoro coefficients are off by a factor of `6`. I’m checking for any remaining T-T specializations before I patch.
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\{T_\\\\lambda\\\\, T\\\\}|\\\\{T_\\\\lambda T\\\\}|\\\\{T\\\\{\\\\}_\\\\lambda T\\\\}|\\\\{T\\\\(z_1\\\\) \\\\{\\\\}_\\\\lambda T\\\\(z_2\\\\)\\\\}|m_2\\(T, T;\\\\, \\\\lambda\\)|m_2\\(T,T;\\\\lambda\\)' chapters working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\lambda\\"'^3'"' chapters/examples/rosetta_stone.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/examples/w-algebras*.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '/lambda\\"'^3|/lambda'"\\"'^5'"' chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' 'c_\\{["'^}]+'"\\}.*lambda\\"'^3|lambda'"\\"'^3.*c_'"\\{["'^}]+'"\\}|\\\\lambda\\"'^3.*central|central.*'"\\\\lambda\\"'^3'"' chapters working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:\\{T_\\lambda\\, T\\}|\\{T_\\lambda T\\}|\\{T\\{\\}_\\lambda T\\}|\\{T\\(z_1\\) \\{\\}_\\lambda T\\(z_2\\)\\}|m_2\(T, T;\\, \\lambda\)|m_2\(T,T;\\lambda\))
          ^
error: repetition quantifier expects a valid decimal
 exited 1 in 51ms:

 succeeded in 52ms:
chapters/examples/w-algebras-virasoro.tex:71:\{T_\lambda T\} = \partial T + 2T\lambda + \frac{c}{12}\lambda^3.
chapters/examples/w-algebras-virasoro.tex:76:The $\lambda^3$ term arises from the Schwarzian derivative in the transformation law
chapters/examples/w-algebras-virasoro.tex:111:We verify $Q^2 = 0$ on each generator. The inputs are the Virasoro $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2\lambda T + \frac{c}{12}\lambda^3$ and the ghost OPE $\{(c_{\mathrm{gh}})_\lambda c_{\mathrm{gh}}\} = 0$, $\{(c_{\mathrm{gh}})_\lambda \mu\} = -1$.
chapters/examples/w-algebras-virasoro.tex:271:On cohomology, with $m_2(T,T;\lambda) = \{T_\lambda T\} = \partial T + 2T\lambda + \tfrac{c}{12}\lambda^3$, the left-hand side is the \emph{PVA associator}. By the PVA Jacobi identity, this associator equals $-\{T_{\lambda_2}\{T_{\lambda_1} T\}\}$: it is nonzero but determined by the bracket. The chain-level $m_3$ lives in the full BV-BRST complex (involving the ghost field $\mu$); its projection to cohomology is the transferred operation $m_3^H$.
chapters/examples/w-algebras-w3.tex:17:\{T_\lambda T\} &= \partial T + 2T\lambda + \frac{c}{12}\lambda^3,\\
chapters/examples/w-algebras-w3.tex:21:\{W_\lambda W\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T\lambda^3 + \frac{1}{2}(\partial T)\lambda^2 + \biggl(\frac{32}{5c + 22}\Lambda + \frac{3}{10}\partial^2 T\biggr)\lambda + \frac{16}{5c + 22}\partial\Lambda + \frac{1}{15}\partial^3 T,
chapters/examples/w-algebras-w3.tex:79:The proof is analogous to Proposition \ref{prop:vir-m2}, using Wick contractions with the two propagators. The $\{W_\lambda W\}$ bracket requires contracting $W$ fields with $\chi$ in the interaction terms involving $T$, $W$, $\chi$. For instance, the $\lambda^3$ term in $\{W_\lambda W\}$ proportional to $T$ comes from:
chapters/examples/w-algebras-w3.tex:173: + \frac{1}{3}T\,\lambda^3
chapters/examples/w-algebras-w3.tex:630:inserting $m_2(W,W;\lambda)|_{P_3} = \tfrac{1}{3}T\lambda^3$
chapters/examples/w-algebras-w3.tex:815:r^{TT}(\lambda,\mu) &= \frac{c/12}{\lambda^3 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{\lambda^2 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{\lambda \mu},\\
chapters/examples/w-algebras-w3.tex:817:r^{WW}(\lambda,\mu) &= \frac{c/360}{\lambda^5 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{3\lambda^3 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{2\lambda^2 \mu} \\
chapters/examples/w-algebras-w3.tex:842:\emph{Triple $(T,T,W)$:} Using $\{T_\lambda W\} = \partial W + 3\lambda W + \ldots$ (the primary OPE with $W$ of spin 3), the LHS involves $\{T_\lambda \{T_\mu W\}\}$ and $\{T_\mu \{T_\lambda W\}\}$. By sesquilinearity, $\{T_\lambda \{T_\mu W\}\} = \{T_\lambda (\partial W + 3\mu W + \cdots)\} = (\partial + 3\mu)(\partial W + 2\lambda W + \cdots) + \cdots$, and the RHS $\{\{T_\lambda T\}_{\lambda+\mu} W\} = \{(\partial T + 2\lambda T + \frac{c}{12}\lambda^3)_{\lambda+\mu} W\}$. Expanding both sides in powers of $\lambda, \mu$ and using the explicit $\{T_\lambda W\}$ bracket, all terms cancel.
chapters/examples/w-algebras-w3.tex:1435:$(T,T)$ & $\partial T + 2T\lambda + \tfrac{c}{12}\lambda^3$
chapters/examples/w-algebras-w3.tex:1441:$(W,W)$ & $\tfrac{c}{360}\lambda^5 + \tfrac{1}{3}T\lambda^3
chapters/examples/w-algebras-w3.tex:1811:\frac{c}{12}\lambda^3$, and the $W_3$ generator acquires a
chapters/examples/w-algebras-w3.tex:1938:$1/z^3$ & $T/3$ (from $\lambda^3$)
chapters/examples/w-algebras-stable.tex:75:\{T_\lambda T\} = \partial T + 2T\lambda + \frac{c}{12}\lambda^3.
chapters/examples/w-algebras-stable.tex:80:The $\lambda^3$ term arises from the Schwarzian derivative in the transformation law
chapters/examples/w-algebras-stable.tex:115:We verify $Q^2 = 0$ on each generator. The inputs are the Virasoro $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2\lambda T + \frac{c}{12}\lambda^3$ and the ghost OPE $\{(c_{\mathrm{gh}})_\lambda c_{\mathrm{gh}}\} = 0$, $\{(c_{\mathrm{gh}})_\lambda \mu\} = -1$.
chapters/examples/w-algebras-stable.tex:363:$m_2(T,T;\lambda) = \{T_\lambda T\} = \partial T + 2T\lambda + \tfrac{c}{12}\lambda^3$.
 succeeded in 51ms:
working_notes.tex:1337:quartic pole ($\frac{c}{12}\lambda^3$, the central charge).
working_notes.tex:12594:+ \frac{c_{\mathrm{DS}}}{12}\,\lambda^3.
working_notes.tex:12644:+ \frac{c_{\mathrm{DS}}}{12}\,\lambda^3\Bigr).
chapters/examples/w-algebras-stable.tex:115:We verify $Q^2 = 0$ on each generator. The inputs are the Virasoro $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2\lambda T + \frac{c}{12}\lambda^3$ and the ghost OPE $\{(c_{\mathrm{gh}})_\lambda c_{\mathrm{gh}}\} = 0$, $\{(c_{\mathrm{gh}})_\lambda \mu\} = -1$.
chapters/examples/w-algebras.tex:125:We verify $Q^2 = 0$ on each generator. The inputs are the Virasoro $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2\lambda T + \frac{c}{12}\lambda^3$ and the ghost OPE $\{(c_{\mathrm{gh}})_\lambda c_{\mathrm{gh}}\} = 0$, $\{(c_{\mathrm{gh}})_\lambda \mu\} = -1$.
chapters/examples/w-algebras-virasoro.tex:111:We verify $Q^2 = 0$ on each generator. The inputs are the Virasoro $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2\lambda T + \frac{c}{12}\lambda^3$ and the ghost OPE $\{(c_{\mathrm{gh}})_\lambda c_{\mathrm{gh}}\} = 0$, $\{(c_{\mathrm{gh}})_\lambda \mu\} = -1$.
chapters/connections/modular_pva_quantization.tex:1192:\{T_\lambda T\} = \partial T + 2T\lambda + \frac{c_{\mathrm{cl}}}{12}\lambda^3,
chapters/connections/modular_pva_quantization.tex:1305:L_X P_c = -x\Big(\frac{c_{\mathrm{cl}}}{6}\lambda^3 + 2T\lambda + \partial T\Big).
chapters/connections/modular_pva_quantization_frontier.tex:19:\{T_\lambda T\} = \partial T + 2T\lambda + \frac{c_{\mathrm{cl}}}{12}\lambda^3,
chapters/connections/modular_pva_quantization_frontier.tex:132:L_X P_c = -x\Big(\frac{c_{\mathrm{cl}}}{6}\lambda^3 + 2T\lambda + \partial T\Big).
chapters/connections/ordered_associative_chiral_kd_frontier.tex:2847:\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3022:The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the

thinking
**Inspecting candidate files**

I’m concluding that we have enough candidate files and need a closer look at the `w-algebras.tex` section to address some issues. I should search for any duplicates with similar patterns and aim for minimal edits. The plan involves replacing the inverse-power lambda-bracket displays in the specific files with the correct polynomial forms, possibly as they relate to Laurent series. User just wanted fixes for lambda-bracket formulas, so maybe I only need to change the displays and adjust the description slightly. I'll check the surrounding context to ensure everything fits smoothly.
exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras.tex | sed -n '36,58p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras.tex | sed -n '1168,1184p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-conditional.tex | sed -n '417,534p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-frontier.tex | sed -n '44,148p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
    36	% label removed: eq:KZ-action
    37	S = \int_{\R \times \C} \eta_i (d_t + \bar{\partial})\Phi^i + \frac{1}{2} \eta_i \Pi^{ij}(\partial_z) \eta_j,
    38	\end{equation}
    39	where $\Pi^{ij}(\partial) = \sum_n \Pi^{ij}_n \partial^n$ is the differential operator encoding the $\lambda$-bracket.
    40	
    41	The gauge transformations are
    42	\begin{align}
    43	\delta \Phi^i &= \Pi^{ij}(\partial) \epsilon_j,\\
    44	\delta \eta_i &= -(d_t + \bar{\partial})\epsilon_i - \eta_j \frac{\partial \Pi^{jk}}{\partial \Phi^i}(\partial) \epsilon_k,
    45	\end{align}
    46	where $\epsilon_i$ are gauge parameters of spin $1-s_i$.
    47	\end{construction}
    48	
    49	\begin{remark}[Higher-Spin Gravity]
    50	When $\mathcal{V}$ is a W-algebra, the resulting 3D theory is a form of higher-spin gravity in the sense of Henneaux--Teitelboim and Vasiliev. The gauge symmetry extends diffeomorphisms to include higher-spin transformations.
    51	\end{remark}
    52	
    53	\subsubsection{BV Quantization and $A_\infty$ Operations}
    54	
    55	\begin{remark}[Analytic hypotheses for W-algebra examples]
 succeeded in 51ms:
  1168	
  1169	\textbf{In Mode Expansion:}
  1170	\begin{equation}
  1171	\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}.
  1172	\end{equation}
  1173	
  1174	\textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
  1175	\begin{align}
  1176	\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
  1177	&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
  1178	\end{align}
  1179	
  1180	\subsubsection{The Ternary Operations}
  1181	
  1182	\textbf{$m_3(T,T,T)$:} Same as Virasoro.
  1183	
  1184	\textbf{$m_3(T,T,W)$:}
 succeeded in 51ms:
   417	\subsubsection{The Binary Operation $m_2(T,T)$}
   418	
   419	\textbf{Singular Part ($\lambda$-bracket):}
   420	\begin{align}
   421	\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
   422	&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
   423	\end{align}
   424	
   425	\textbf{In Mode Expansion:}
   426	\begin{align}
   427	\{T_m {}_\lambda T_n\} &= \sum_{k=0}^{m} \binom{m}{k} (-\lambda)^k (k-m-1) T_{m+n-k}\\
   428	&\quad + \frac{c}{12} \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m-2)(k-m-1)(k-m) \delta_{m+n-k,0}.
   429	\end{align}
   430	
   431	\textbf{Regular Part:}
   432	\begin{equation}
   433	m_2(T,T)_{\text{reg}} = \sum_{n=0}^\infty \frac{(\lambda_1 + \lambda_2)^n}{n!} \partial^n(T_1 \cdot T_2),
   434	\end{equation}
   435	where $T_1 \cdot T_2$ is the pointwise product (becomes normal ordered product in quantum theory).
   436	
 succeeded in 52ms:
    44	\subsubsection{The Binary Operation $m_2(T,T)$}
    45	
    46	The singular part (the $\lambda$-bracket) is
    47	\begin{align}
    48	\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
    49	\end{align}
    50	In modes,
    51	\begin{align}
    52	\{T_m {}_\lambda T_n\} &= \sum_{k=0}^{m} \binom{m}{k} (-\lambda)^k (k-m-1) T_{m+n-k}\\
    53	&\quad + \frac{c}{12} \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m-2)(k-m-1)(k-m) \delta_{m+n-k,0}.
    54	\end{align}
    55	The regular part gives the normally ordered product:
    56	$m_2(T,T)_{\text{reg}} = {:}T_1 T_2{:}$.
    57	
    58	\subsubsection{The Ternary Operation $m_3(T,T,T)$}
    59	
    60	The ternary operation comes from the Y-diagram integral. In modes:
    61	\begin{equation}
    62	\label{eq:vir-m3-modes}
    63	m_3(T_m, T_n, T_p) = \sum_{\substack{a,b,c \geq 0 \\ a+b+c = m+n+p-2}} \mathcal{A}_{m,n,p}^{a,b,c} \frac{\partial^a T \cdot \partial^b T \cdot \partial^c T}{\lambda_1^{a+2} \lambda_2^{b+2}},



thinking
**Inspecting lambda-brackets**

I see I need to address the patch for w-algebras-conditional and frontier to ensure they align properly. The w-algebras.tex and conditional duplicates aren’t active and need fixing. I also spotted an issue with the mixed lambda-bracket; it should be `∂W + 3W λ`, not the inverse power `3W/λ^2`. That oversight appears to affect all sections—T-T and W-W included. I'll also need to check T-W and similar sections to ensure everything is accurate.
thinking
**Adjusting polynomial forms**

I’m noticing that these sections have m_k defined as Laurent series in lambda, which isn’t standard for mode expansion. I think I should patch only the explicit bracket formulas to polynomial forms and possibly the mixed bracket formulas. The mode expansion lines, which use `\sum \binom{m}{k} (-\lambda)^k`, might seem odd, but they could work. My minimal fix will involve changing the explicitly labeled lambda-bracketing to polynomial divided-power form and adjusting the text to reflect this. I might also remove some nonsensical derivative expansion lines that become irrelevant.
thinking
**Patching brackets and frontier**

I think I need to patch the T-W bracket line, ensuring it's consistent with the other adjustments I’ve made. It seems like the frontier file might also need similar attention. I wonder if the changes in the bracket lines will maintain clarity and ensure everything is aligned properly across these files. I want to make sure that all sections follow the same structure to avoid confusion and maintain consistency throughout the work.
codex
Before editing, I’m tightening the patch scope to the actual bad formulas inside the duplicated W-algebra sections: the text displays, the mixed `T–W` bracket, and the Mathematica snippets all share the same inverse-power leak. I’m reading those exact blocks now so the fixes stay local and don’t disturb unrelated derivations.
exec
/bin/zsh -lc "rg -n '/lambda\\"'^|/ lambda'"\\"'^|'"\\\\lambda\\"'^[-]?'"' chapters/examples/w-algebras.tex chapters/examples/w-algebras-conditional.tex chapters/examples/w-algebras-frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-conditional.tex | sed -n '718,772p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras.tex | sed -n '1374,1428p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-frontier.tex | sed -n '200,216p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/w-algebras-frontier.tex:48:\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
chapters/examples/w-algebras-frontier.tex:134:\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
chapters/examples/w-algebras-frontier.tex:142:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-frontier.tex:210:\frac{\partial \mathcal{F}_{\text{Vir}}}{\partial T} = \left( \partial + 2\lambda + \frac{c}{12}\lambda^3 \partial^3 \right) \mathcal{F}_{\text{Vir}} + \frac{1}{2} \{\mathcal{F}_{\text{Vir}}, \mathcal{F}_{\text{Vir}}\}_\lambda.
chapters/examples/w-algebras-frontier.tex:252:r^{\text{Vir}}(\lambda, \mu) = \sum_{m,n \in \Z} r_{m,n} T_m \otimes T_n \cdot \lambda^{-m-2} \mu^{-n-2}.
chapters/examples/w-algebras-frontier.tex:269:\sum r^{TT}_{m,n; i,j} T_m T_n \lambda^{-i} \mu^{-j} & \sum r^{TW}_{m,n; i,j} T_m W_n \lambda^{-i} \mu^{-j}\\
chapters/examples/w-algebras-frontier.tex:270:\sum r^{WT}_{m,n; i,j} W_m T_n \lambda^{-i} \mu^{-j} & \sum r^{WW}_{m,n; i,j} W_m W_n \lambda^{-i} \mu^{-j}
chapters/examples/w-algebras-frontier.tex:293: \binom{n+k-1}{k} \lambda^{-n-k} \partial^k;
chapters/examples/w-algebras-frontier.tex:497:terms up to $\lambda^7$ (pole order $8$ minus $1$ from bar
chapters/examples/w-algebras-frontier.tex:556:r^{TT}(\lambda) &= \frac{c/12}{\lambda^3}
chapters/examples/w-algebras-frontier.tex:557: + \frac{2T}{\lambda} + \frac{\partial T}{\lambda^0},
chapters/examples/w-algebras-frontier.tex:559:r^{W_3 W_3}(\lambda) &= \frac{c/360}{\lambda^5}
chapters/examples/w-algebras-frontier.tex:560: + \frac{T/3}{\lambda^3}
chapters/examples/w-algebras-frontier.tex:561: + \frac{\partial T/2}{\lambda^2}
chapters/examples/w-algebras-frontier.tex:564:r^{W_4 W_4}(\lambda) &= \frac{c_4}{\lambda^7}
chapters/examples/w-algebras-frontier.tex:565: + \frac{T_4}{\lambda^5}
chapters/examples/w-algebras-frontier.tex:578:$\lambda^{-7}$ (from the $z^{-8}$ OPE pole).
chapters/examples/w-algebras-frontier.tex:689:weight-$1$ lacuna (the $\lambda^{s+s'-2}$ coefficient in
chapters/examples/w-algebras-frontier.tex:702:The $\lambda^6$ coefficient in $\{W_{4\,\lambda} W_4\}$
chapters/examples/w-algebras-frontier.tex:707:A $\lambda^6$ term would contribute a field of conformal
 succeeded in 51ms:
   200	\begin{equation}
   201	\mathcal{F}_{\text{Vir}}(T; \lambda) = \sum_{k=1}^\infty \frac{1}{k!} m_k(T, \ldots, T)(\lambda_1, \ldots, \lambda_{k-1}).
   202	\end{equation}
   203	
   204	\begin{theorem}[Virasoro Generating Function; \ClaimStatusConditional]
   205	\label{thm:vir-gen-func-explicit}
   206	Let\/ $\cA$ be a logarithmic\/ $\SCchtop$-algebra.
   207	The generating function satisfies the differential equation:
   208	\begin{equation}
   209	\label{eq:vir-diff-eq}
   210	\frac{\partial \mathcal{F}_{\text{Vir}}}{\partial T} = \left( \partial + 2\lambda + \frac{c}{12}\lambda^3 \partial^3 \right) \mathcal{F}_{\text{Vir}} + \frac{1}{2} \{\mathcal{F}_{\text{Vir}}, \mathcal{F}_{\text{Vir}}\}_\lambda.
   211	\end{equation}
   212	\end{theorem}
   213	
   214	\noindent Equation~\eqref{eq:vir-diff-eq} yields the recursion
   215	\begin{align}
   216	m_{k+1}(T^{\otimes (k+1)}) &= \frac{1}{k+1} \Bigg[ Q_{\text{BRST}} \cdot m_k(T^{\otimes k})\\
 succeeded in 51ms:
  1374	
  1375	\subsection{Sample Mathematica Code}
  1376	
  1377	\subsubsection{Virasoro $m_2$ Computation}
  1378	
  1379	\begin{verbatim}
  1380	(* Define Virasoro lambda-bracket *)
  1381	VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
  1382	
  1383	(* Expand in spectral parameter *)
  1384	ExpandLambdaBracket[expr_, lambda_, n_] := 
  1385	 Series[expr, {lambda, Infinity, -n}] // Normal;
  1386	
  1387	(* Compute singular part of m_2 *)
  1388	m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
  1389	
  1390	(* Output *)
  1391	Print["m_2(T,T)_sing = ", m2Sing];
  1392	\end{verbatim}
  1393	
 succeeded in 51ms:
   718	
   719	\subsection{Sample Mathematica Code}
   720	
   721	\subsubsection{Virasoro $m_2$ Computation}
   722	
   723	\begin{verbatim}
   724	(* Define Virasoro lambda-bracket *)
   725	VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
   726	
   727	(* Expand in spectral parameter *)
   728	 ExpandLambdaBracket[expr_, lambda_, n_] :=
   729	 Series[expr, {lambda, Infinity, -n}] // Normal;
   730	
   731	(* Compute singular part of m_2 *)
   732	m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
   733	
   734	(* Output *)
   735	Print["m_2(T,T)_sing = ", m2Sing];
   736	\end{verbatim}
   737	
exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras.tex | sed -n '140,154p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-conditional.tex | sed -n '512,532p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-frontier.tex | sed -n '36,52p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-frontier.tex | sed -n '128,146p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   140	\end{equation}
   141	
   142	\begin{proposition}[Virasoro $\lambda$-bracket from Propagator; \ClaimStatusConditional]
   143	% label removed: prop:vir-m2
   144	Assume the Khan--Zeng Virasoro realization satisfies
   145	Theorem~\ref{thm:physics-bridge}.
   146	The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
   147	\begin{equation}
   148	m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
   149	 \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
   150	\end{equation}
   151	where
   152	\begin{align}
   153	a_3 &= \frac{c}{12}, & \text{(Schwarzian term)}\\
   154	a_2 &= 2T, & \text{(primary transformation)}\\
 succeeded in 51ms:
   512	\subsubsection{The Binary Operations}
   513	
   514	\textbf{$m_2(T,T)$:} Identical to Virasoro.
   515	
   516	\textbf{$m_2(T,W)$:} The mixed bracket is
   517	\begin{equation}
   518	\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
   519	\end{equation}
   520	
   521	\textbf{In Mode Expansion:}
   522	\begin{equation}
   523	\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}.
   524	\end{equation}
   525	
   526	\textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
   527	\begin{align}
   528	\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
   529	&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
   530	\end{align}
   531	
 succeeded in 51ms:
    36	
    37	The operation $m_k$ is a Laurent series in $\lambda_1, \ldots, \lambda_{k-1}$:
    38	\begin{equation}
    39	m_k(a_1, \ldots, a_k) = \sum_{n_1, \ldots, n_{k-1} \in \Z} \frac{C_{n_1, \ldots, n_{k-1}}(a_1, \ldots, a_k)}{\lambda_1^{n_1+1} \cdots \lambda_{k-1}^{n_{k-1}+1}}.
    40	\end{equation}
    41	
    42	\subsection{Virasoro: Explicit Formulas}
    43	
    44	\subsubsection{The Binary Operation $m_2(T,T)$}
    45	
    46	The singular part (the $\lambda$-bracket) is
    47	\begin{align}
    48	\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
    49	\end{align}
    50	In modes,
    51	\begin{align}
    52	\{T_m {}_\lambda T_n\} &= \sum_{k=0}^{m} \binom{m}{k} (-\lambda)^k (k-m-1) T_{m+n-k}\\
 succeeded in 51ms:
   128	
   129	\subsubsection{The Binary Operations}
   130	
   131	The binary operation $m_2(T,T)$ is identical to Virasoro.
   132	The mixed bracket is
   133	\[
   134	\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
   135	\]
   136	and in modes,
   137	$\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
   138	The self-bracket $\{W_\lambda W\}$
   139	(cf.\ equation~\eqref{eq:m2WW-recap} for the compact
   140	polynomial form) is
   141	\begin{align}
   142	\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
   143	&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
   144	\end{align}
   145	
   146	\subsubsection{The Ternary Operations}



thinking
**Evaluating polynomial form**

It seems like the original snippet isn’t following the correct W3 bracket conventions. If I convert it to polynomial form, it might still lead to inconsistencies. To ensure accuracy, I’m thinking it’s better to align it with the correct full polynomial in line 528. Actually, just setting it equal to the formula in line 619 should fix the denominator too. The conditional snippet diverged, but upon inspection, the original file does have the correct denominator, so I should ensure it matches.
thinking
**Patching formulas and adjusting text**

I should patch the full formula for accuracy. It might be a good idea to search other files for inverse-power formulas, especially in non-active areas. The w-algebras-frontier file doesn’t have sample code but does provide explicit formulas, like those related to `r^{TT}(\lambda)`, so no need to focus on those. I’ll look at specific lines, like 134, needing a patch. Adjusting text to refer to "divided-power polynomial form" instead of "λ-bracket" seems necessary, while I'll leave the general `m_k` line since it can actually be a Laurent series.
thinking
**Identifying and patching errors**

I noticed that the phrasing "The singular part (the λ-bracket) is" regarding inverse powers is incorrect. I should patch those specific lines only. In w-algebras.tex, particularly proposition line 148, I might need to make the equation more explicit in polynomial form. It makes sense to search for similar bugs in the conditional/frontier files at equivalent proposition lines. I’ll specifically look for references like "OPE convention" using rg to ensure consistency across the documents.
exec
/bin/zsh -lc "rg -n '\\\\{T_\\\\lambda W\\\\}|\\\\{T\\(z_1\\) \\{\\}_\\\\lambda W\\(z_2\\)\\}|\\\\{W\\(z_1\\) \\{\\}_\\\\lambda W\\(z_2\\)\\}' chapters/examples/w-algebras.tex chapters/examples/w-algebras-conditional.tex chapters/examples/w-algebras-frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'OPE convention|1/\\\\lambda\\"'^n|'"\\\\frac\\{a_n\\}\\{\\\\lambda\\"'^n'"\\}|sum_\\{n=1\\}\\"'^3 '"\\\\frac\\{a_n\\}\\{\\\\lambda\\"'^n'"\\}' chapters/examples/w-algebras.tex chapters/examples/w-algebras-conditional.tex chapters/examples/w-algebras-frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'c_\\{\\\\mathrm\\{BP\\}\\}.*lambda\\"'^3|lambda'"\\"'^3/2|'"\\\\tfrac\\{c_\\{\\\\mathrm\\{BP\\}\\}\\}\\{2\\}\\\\,\\\\lambda\\"'^3'"' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'VirLambdaBracket|W3LambdaBracket' chapters/examples/w-algebras.tex chapters/examples/w-algebras-conditional.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:\\{T_\\lambda W\\}|\\{T\(z_1\) \{\}_\\lambda W\(z_2\)\}|\\{W\(z_1\) \{\}_\\lambda W\(z_2\)\})
          ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
chapters/examples/w-algebras.tex:148:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras.tex:149: \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
 succeeded in 51ms:
chapters/examples/w-algebras.tex:1381:VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
chapters/examples/w-algebras.tex:1388:m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
chapters/examples/w-algebras.tex:1421:W3LambdaBracket[c_, lambda_] :=
chapters/examples/w-algebras.tex:1427:m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
chapters/examples/w-algebras-conditional.tex:725:VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
chapters/examples/w-algebras-conditional.tex:732:m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
chapters/examples/w-algebras-conditional.tex:765:W3LambdaBracket[c_, lambda_] :=
chapters/examples/w-algebras-conditional.tex:771:m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
 succeeded in 51ms:
2847:\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
3022:The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
exec
/bin/zsh -lc "rg -n 'm_2\\(T, T\\)_\\\\text\\{sing\\}|m_2\\(T,T\\)_\\\\text\\{sing\\}' chapters/examples/w-algebras*.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '1/\\\\lambda\\"'^|/ lambda'"\\"'^'"' chapters/examples/w-algebras*.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/w-algebras-virasoro.tex:134:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras.tex:148:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras-stable.tex:138:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
 succeeded in 51ms:
chapters/examples/w-algebras.tex:1381:VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
chapters/examples/w-algebras.tex:1422: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
chapters/examples/w-algebras-conditional.tex:725:VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
chapters/examples/w-algebras-conditional.tex:766: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
codex
A second pass found one more live inconsistency in the active Virasoro example chapter: even where the coefficient is `c/12`, one proposition still defines the lambda-bracket as `\sum a_n/\lambda^n`, which is an OPE-kernel presentation, not the divided-power bracket itself. I’m patching that together with the confirmed `c_BP/2`, inverse-power W-algebra displays, and the two bad Rosetta specializations.
exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-stable.tex | sed -n '132,142p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-virasoro.tex | sed -n '66,74p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-virasoro.tex | sed -n '128,142p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '4336,4344p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
    66	\subsubsection{Classical Structure}
    67	
    68	The Virasoro Poisson vertex algebra is generated by a single field $T$ of spin 2 (the stress tensor) with $\lambda$-bracket
    69	\begin{equation}
    70	\label{eq:vir-lambda-bracket}
    71	\{T_\lambda T\} = \partial T + 2T\lambda + \frac{c}{12}\lambda^3.
    72	\end{equation}
    73	Here $c \in \C$ is the \emph{classical central charge}, measuring the conformal anomaly.
    74	
 succeeded in 51ms:
   128	\begin{proposition}[Virasoro $\lambda$-bracket from Propagator; \ClaimStatusConditional]
   129	\label{prop:vir-m2}
   130	Assume the Khan--Zeng Virasoro realization satisfies
   131	Theorem~\ref{thm:physics-bridge}.
   132	The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
   133	\begin{equation}
   134	m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
   135	 \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
   136	\end{equation}
   137	(We use $\zeta = z_1 - z_2$ for the position-space variable and
   138	$\lambda$ for the PVA spectral parameter; the Borel transform
   139	(Definition~\ref{def:borel-transform-pva}) converts between them.)
   140	Here
   141	\begin{align}
   142	a_3 &= \frac{c}{12}, & \text{(Schwarzian term)}\\
 succeeded in 51ms:
   132	\begin{proposition}[Virasoro $\lambda$-bracket from Propagator; \ClaimStatusProvedHere]
   133	% label removed: prop:vir-m2
   134	Let\/ $\cA$ be a logarithmic\/ $\SCchtop$-algebra
   135	\textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
   136	The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
   137	\begin{equation}
   138	m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
   139	 \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
   140	\end{equation}
   141	where
   142	\begin{align}
 succeeded in 51ms:
  4336	\noindent\emph{(vi) Vanishing OPEs.}
  4337	$\{G^\pm_\alpha{}_\lambda\, G^\pm_\beta\} = 0$.
  4338	
  4339	\smallskip
  4340	\noindent\emph{(vii) Virasoro subalgebra.}
  4341	$\{T_\lambda T\} = \frac{c}{12}\lambda^3 + 2T\lambda
  4342	+ \partial T$,
  4343	with the central charge
  4344	$c = c(\mathfrak{sl}_4, f_{(2,1,1)}, k)$ given by the
exec
/bin/zsh -lc "rg -n 'sum_\\{n=1\\}\\"'^3 '"\\\\frac\\{a_n\\}\\{\\\\lambda\\"'^n'"\\}|sum_\\{n=1\\}\\"'^5 '"\\\\frac\\{["'^}]+'"\\}\\{\\\\lambda\\"'^n'"\\}|\\\\frac\\{["'^}]+'"\\}\\{\\\\lambda\\"'^5'"\\}' chapters/examples/w-algebras*.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'c/12 / lambda\\"'^3|c/360 / lambda'"\\"'^5|3W / lambda'"\\"'^2|D'"\\[T, z\\] / lambda|D\\[W, z\\] / lambda' chapters/examples/w-algebras*.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/w-algebras.tex:148:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras.tex:1176:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-virasoro.tex:134:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras-frontier.tex:142:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-frontier.tex:559:r^{W_3 W_3}(\lambda) &= \frac{c/360}{\lambda^5}
chapters/examples/w-algebras-frontier.tex:565: + \frac{T_4}{\lambda^5}
chapters/examples/w-algebras-conditional.tex:528:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-stable.tex:138:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
 succeeded in 51ms:
chapters/examples/w-algebras.tex:1381:VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
chapters/examples/w-algebras.tex:1422: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
chapters/examples/w-algebras-conditional.tex:725:VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
chapters/examples/w-algebras-conditional.tex:766: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
exec
/bin/zsh -lc "rg -n '/lambda\\"'^3|/lambda'"\\"'^5|/ lambda'"\\"'^3|/ lambda'"\\"'^5|sum_'"\\{n=1\\}\\"'^3 '"\\\\frac\\{a_n\\}\\{\\\\lambda\\"'^n'"\\}|\\\\{T_\\\\lambda T\\\\} = \\\\sum' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'c_\\{\\\\mathrm\\{["'^}]+'"\\}\\}/2\\\\,\\\\lambda\\"'^3|lambda'"\\"'^3/2|'"\\\\tfrac\\{c_\\{\\\\mathrm\\{["'^}]+'"\\}\\}\\}\\{2\\}\\\\,\\\\lambda\\"'^3'"' chapters working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:/lambda\^3|/lambda\^5|/ lambda\^3|/ lambda\^5|sum_\{n=1\}\^3 \\frac\{a_n\}\{\\lambda\^n\}|\\{T_\\lambda T\\} = \\sum)
                                                                                                    ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd_frontier.tex:2847:\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3022:The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
exec
/bin/zsh -lc "rg -n -F '/lambda"'^5'"' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F '/lambda"'^3'"' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'sum_{n=1}"'^3 '"\\frac{a_n}{\\lambda"'^n}'"' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n '\\(1/4\\)\\\\lambda\\"'^3|'"\\\\tfrac\\{1\\}\\{2\\}\\\\lambda\\"'^3|'"\\(1/2\\)\\\\lambda\\"'^3|'"\\\\frac\\{1\\}\\{2\\}\\\\lambda\\"'^3|'"\\\\frac\\{1\\}\\{4\\}\\\\lambda\\"'^3|'"\\\\tfrac\\{1\\}\\{4\\}\\\\lambda\\"'^3'"' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'c/2 \\* lambda\\"'^3|'"\\(c/2\\) \\* lambda\\"'^3|c/2'"\\s*\\*\\s*lam\\"'^3'"' compute chapters working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/rosetta_stone.tex:6325:$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
chapters/examples/rosetta_stone.tex:6615:$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
 succeeded in 51ms:
compute/lib/pva_descent_chain_level.py:174:    c/2 * lam^3/3! = c/12 * lam^3.
compute/lib/pva_descent_coefficients_engine.py:46:c/12 * lam^3, NOT c/2 * lam^3.  Sesquilinearity of the mode relation
compute/lib/examples/virasoro.py:21:packages this as (c/2) * lambda^3 / 3! = (c/12) * lambda^3.
compute/tests/test_pva_axioms.py:424:        Factor: c/2 * lambda^3 / 3! = c/2 * lambda^3 / 6 = c/12 * lambda^3.
compute/tests/test_pva_descent_coefficients_engine.py:176:        # Explicit V2-AP34 guardrail: refuse the wrong c/2 * lam^3 form.

thinking
**Searching for formulas**

I need to search for `3W / lambda^2` in the frontier and conditional sections of the TeX files. I've already identified something, and I think I might have to patch both `w-algebras.tex` and the `conditional/frontier` files. I also want to check if `active w3.tex` correctly utilizes `\partial W + 3\lambda W`. It seems I also need to search for `\frac{3W}{\lambda^2}` across the entire repository.
exec
/bin/zsh -lc "rg -n '3W\\s*/\\s*lambda\\"'^2|'"\\\\frac\\{3W\\}\\{\\\\lambda\\"'^2'"\\}|\\\\frac\\{3W\\(z_2\\)\\}\\{\\\\lambda\\"'^2'"\\}|\\\\frac\\{3W\\}\\{\\\\lambda\\"'^2'"\\}' chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/w-algebras.tex:1166:\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
chapters/examples/w-algebras-frontier.tex:134:\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
chapters/examples/w-algebras-conditional.tex:518:\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
exec
/bin/zsh -lc "rg -n 'c/360 / lambda\\"'^5|'"\\\\frac\\{c/360\\}\\{\\\\lambda\\"'^5'"\\}|T\\(z_2\\)/3\\}\\{\\\\lambda\\"'^3'"\\}|D\\[T, z\\]/2 / lambda\\"'^2'"' chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/w-algebras.tex:1176:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras.tex:1422: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
chapters/examples/w-algebras-frontier.tex:142:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-frontier.tex:559:r^{W_3 W_3}(\lambda) &= \frac{c/360}{\lambda^5}
chapters/examples/w-algebras-conditional.tex:528:\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
chapters/examples/w-algebras-conditional.tex:766: c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2

thinking
**Patching algebras**

I need to evaluate the w-algebras-frontier since it's included in the main file. Both w-algebras.tex and conditional/stable seem to be outdated, so I should consider updating those too, especially because of a proposition. There's a chance that w-algebras-virasoro might be active, which makes patching it a priority. I think I should search for the term `\{T_\lambda T\} = \sum` throughout the repository to find relevant sections to patch.
exec
/bin/zsh -lc "rg -n '\\\\{T_\\\\lambda T\\\\} = \\\\sum|\\\\{T_\\\\lambda T\\\\} = \\\\frac|\\\\{T\\(z_1\\) \\{\\}_\\\\lambda T\\(z_2\\)\\} = \\\\frac' chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\{T_\\\\lambda W\\\\} = \\\\frac|\\\\{W\\(z_1\\) \\{\\}_\\\\lambda W\\(z_2\\)\\} = \\\\frac|\\\\{T\\(z_1\\) \\{\\}_\\\\lambda W\\(z_2\\)\\} = \\\\frac' chapters" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:\\{T_\\lambda W\\} = \\frac|\\{W\(z_1\) \{\}_\\lambda W\(z_2\)\} = \\frac|\\{T\(z_1\) \{\}_\\lambda W\(z_2\)\} = \\frac)
          ^
error: repetition quantifier expects a valid decimal
 exited 2 in 51ms:
rg: regex parse error:
    (?:\\{T_\\lambda T\\} = \\sum|\\{T_\\lambda T\\} = \\frac|\\{T\(z_1\) \{\}_\\lambda T\(z_2\)\} = \\frac)
          ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-virasoro.tex | sed -n '140,156p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras.tex | sed -n '148,158p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-stable.tex | sed -n '140,150p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
   140	Here
   141	\begin{align}
   142	a_3 &= \frac{c}{12}, & \text{(Schwarzian term)}\\
   143	a_2 &= 2T, & \text{(primary transformation)}\\
   144	a_1 &= \partial T. & \text{(derivative term)}
   145	\end{align}
   146	The regular part gives the commutative product: $m_2(T,T)_\text{reg} = :TT:$ (normal ordered).
   147	\end{proposition}
   148	
   149	\begin{proof}
   150	By Wick's theorem, contracting $T(z_1)$ with $\mu$ in the interaction term $\int T\mu\partial\mu + \frac{c}{24}\mu\partial^3\mu$ at $z_2$ gives
   151	\[
   152	\langle T(z_1) : T\mu\partial\mu + \frac{c}{24}\mu\partial^3\mu :(z_2) \rangle.
   153	\]
   154	Evaluating the Wick contraction:
   155	\begin{align*}
   156	\langle T(z_1) \mu(z_2) \rangle &\cdot \left( T(z_2) \partial_2 \mu(z_2) + \frac{c}{24} \partial_2^3 \mu(z_2) \right)\\
 succeeded in 51ms:
   148	m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
   149	 \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
   150	\end{equation}
   151	where
   152	\begin{align}
   153	a_3 &= \frac{c}{12}, & \text{(Schwarzian term)}\\
   154	a_2 &= 2T, & \text{(primary transformation)}\\
   155	a_1 &= \partial T. & \text{(derivative term)}
   156	\end{align}
   157	The regular part gives the commutative product: $m_2(T,T)_\text{reg} = :TT:$ (normal ordered).
   158	\end{proposition}
 succeeded in 52ms:
   140	\end{equation}
   141	where
   142	\begin{align}
   143	a_3 &= \frac{c}{12}, & \text{(Schwarzian term)}\\
   144	a_2 &= 2T, & \text{(primary transformation)}\\
   145	a_1 &= \partial T. & \text{(derivative term)}
   146	\end{align}
   147	The regular part gives the commutative product: $m_2(T,T)_\text{reg} = :TT:$ (normal ordered).
   148	\end{proposition}
   149	
   150	\begin{proof}



thinking
**Considering mathematical patches**

I'm exploring the possibility of patching to polynomial form using coefficients from the provided document. It looks like I have some equations involving \(T\) and \(W\) functions. I need to focus on specific lines to make sure the formulas are adjusted accurately. Lines 48, 134, and 142 from "w-algebras-frontier" look important, as do some lines from "w-algebras-conditional." I'm identifying code snippets that could also need adjustments. It's a detailed process, but I’ll keep track of the necessary patches!
thinking
**Analyzing formulas in context**

I'm searching for the `1/λ` pattern in `w-algebras.tex`, focusing on code and explicit formulas while avoiding other `r` formulas. Great, we've identified some elements there. I might need to patch the `w-algebras-frontier` at line 134 due to a mixed bracket. I also want to check line 48 for `z_1, z_2` arguments. There's a possibility to address the `ordered_associative_chiral_kd_frontier.tex` with `c_BP/12` as well. It seems like the references to quartic OPE poles could be conflated too!
thinking
**Considering proof conventions**

I'm pondering whether the proof could employ the OPE convention or perhaps use `\lambda^{-n}` later on. I think it might be useful to check in the file w-algebras-virasoro.tex for any occurrences of `/lambda`. It might lead me to the answers I need, so searching feels like the right next step! Let's explore what we find in that document. I'm curious to see if it will point me in the right direction!
exec
/bin/zsh -lc "rg -n '/lambda\\"'^|sum_'"\\{n=1\\}\\"'^3 '"\\\\frac\\{a_n\\}\\{\\\\lambda\\"'^n'"\\}' chapters/examples/w-algebras-virasoro.tex chapters/examples/w-algebras-stable.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'The singular part \\(the \\\\"'$'"\\\\lambda\\\\"'$-bracket'"\\) is|The mixed bracket is|self-bracket \\"'$'"\\\\{W_\\\\lambda W\\\\}\\"'$'"' chapters/examples/w-algebras.tex chapters/examples/w-algebras-conditional.tex chapters/examples/w-algebras-frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/w-algebras-virasoro.tex:134:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras-stable.tex:138:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
 exited 2 in 51ms:
rg: regex parse error:
    (?:The singular part \(the \\$\\lambda\\$-bracket\) is|The mixed bracket is|self-bracket \$\\{W_\\lambda W\\}\$)
                                                                                                  ^
error: repetition quantifier expects a valid decimal

thinking
**Planning updates before patching**

I think I need to update my plan before applying the patch. It seems I'm still at step 2, and I'm unsure if I'm actually progressing. Maybe I should focus on adding some commentary before making any file edits, as per the instructions. It’s essential to clearly mention the specific edits I’ll be making so that everything is organized for the next steps. Let's ensure everything is in order before proceeding!
codex
I’ve isolated the exact edit set: seven files, all within the lambda-bracket convention surface. I’m now applying local fixes only: convert stray inverse-power “lambda-brackets” back to divided-power polynomials, correct the BP Virasoro coefficient from `c/2` to `c/12`, and fix the two specialized Rosetta coefficients to `1/24` and `1/12`.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex
@@ -137,4 +137,4 @@
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex
@@ -133,4 +133,4 @@
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex
@@ -418,6 +418,5 @@
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
@@ -517,3 +516,3 @@
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
@@ -527,4 +526,4 @@
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
@@ -724,3 +723,3 @@
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
@@ -728,3 +727,3 @@
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
@@ -765,5 +764,5 @@
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
@@ -6324,3 +6324,3 @@
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
@@ -6614,3 +6614,3 @@
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex
@@ -45,5 +45,5 @@
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
@@ -133,3 +133,3 @@
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
@@ -141,4 +141,4 @@
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
@@ -1219,2 +1219 @@
 \end{remark}
-
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2846,3 +2846,3 @@
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
@@ -3021,4 +3021,5 @@
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex
@@ -147,4 +147,4 @@
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
@@ -1066,6 +1066,5 @@
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
@@ -1165,3 +1164,3 @@
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
@@ -1175,4 +1174,4 @@
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
@@ -1380,3 +1379,3 @@
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
@@ -1384,3 +1383,3 @@
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
@@ -1421,5 +1420,5 @@
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
apply_patch(auto_approved=true) exited 0 in 55ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];


thinking
**Verifying search parameters**

I need to check the search surface involving expressions like `c_BP/2 λ^3` and the inverse-power lambda-brackets, as well as the sum of coefficients `a_n/λ^n`. I'm considering running a regex search and maybe compiling, but since this task is for the manuscript, tests might not be necessary. I'll also ensure the `Lambda` symbol in the code block is correct and check for any syntax issues in the text. Time to search!
codex
The edits are in. I’m running the narrow falsifier sweep now: re-grepping the exact bad patterns (`c/2`-style cubic terms, inverse-power “lambda-brackets,” and the wrong specialized Virasoro numerics) to make sure the convention surface is clean without touching unrelated `r`-matrix formulas.
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' '\\\\{T_\\\\lambda T\\\\} = \\\\sum|\\\\{T\\(z_1\\) \\{\\}_\\\\lambda T\\(z_2\\)\\} &= \\\\frac\\{c/12\\}\\{\\\\lambda\\"'^3'"\\}|\\\\{T_\\\\lambda W\\\\} = \\\\frac|\\\\{T\\(z_1\\) \\{\\}_\\\\lambda W\\(z_2\\)\\} = \\\\frac|\\\\{W\\(z_1\\) \\{\\}_\\\\lambda W\\(z_2\\)\\} &= \\\\frac\\{c/360\\}\\{\\\\lambda\\"'^5'"\\}' chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'sum_\\{n=1\\}\\"'^3 '"\\\\frac\\{a_n\\}\\{\\\\lambda\\"'^n'"\\}|c_\\{\\\\mathrm\\{BP\\}\\}\\\\lambda\\"'^3/2|'"\\\\tfrac\\{c_\\{\\\\mathrm\\{BP\\}\\}\\}\\{2\\}\\\\,\\\\lambda\\"'^3|'"\\(1/4\\)\\\\lambda\\"'^3|'"\\\\tfrac\\{1\\}\\{2\\}\\\\lambda\\"'^3|c/12 / lambda'"\\"'^3|c/360 / lambda'"\\"'^5|3W / lambda'"\\"'^2|'"\\\\frac\\{3W\\}\\{\\\\lambda\\"'^2'"\\}|\\\\frac\\{c/12\\}\\{\\\\lambda\\"'^3'"\\}|\\\\frac\\{c/360\\}\\{\\\\lambda\\"'^5'"\\}' chapters compute working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/examples/w-algebras-virasoro.tex chapters/examples/w-algebras-stable.tex chapters/examples/w-algebras.tex chapters/examples/w-algebras-conditional.tex chapters/examples/w-algebras-frontier.tex chapters/examples/rosetta_stone.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 52ms:
rg: regex parse error:
    (?:\\{T_\\lambda T\\} = \\sum|\\{T\(z_1\) \{\}_\\lambda T\(z_2\)\} &= \\frac\{c/12\}\{\\lambda\^3\}|\\{T_\\lambda W\\} = \\frac|\\{T\(z_1\) \{\}_\\lambda W\(z_2\)\} = \\frac|\\{W\(z_1\) \{\}_\\lambda W\(z_2\)\} &= \\frac\{c/360\}\{\\lambda\^5\})
          ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
chapters/examples/w-algebras-frontier.tex:556:r^{TT}(\lambda) &= \frac{c/12}{\lambda^3}
chapters/examples/w-algebras-frontier.tex:559:r^{W_3 W_3}(\lambda) &= \frac{c/360}{\lambda^5}
 succeeded in 50ms:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 23c8dd3..aeee300 100644
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -108,8 +108,9 @@ S_p
 \]
 Then $S_0\subset S_1\subset S_2\subset\cdots$ is an exhaustive increasing
 filtration with $\bigcup_p S_p = \FM_k(\mathbb{C})\times\Conf_k(\mathbb{R})$.
-For the associated graded $\gr_{\mathrm{com}}A$ (which is $E_\infty$-chiral,
-i.e.\ has only simple poles), only the stratum $S_1$ contributes to the bar
+For the associated graded $\gr_{\mathrm{com}}A$ (which remains
+$E_\infty$-chiral and, by construction of the commutator filtration,
+has only first-order OPE singularities), only the stratum $S_1$ contributes to the bar
 differential: all OPE singularities are at worst first-order.
 \end{construction}
 
@@ -169,7 +170,8 @@ $\gr_{\mathrm{com}}(A^!)\simeq(\gr_{\mathrm{com}}A)^!_{FG}$.
 Strong convergence of the filtration (hypothesis~(c)) gives convergence of
 the spectral sequence. The $E_1$~identification is
 Proposition~\ref{prop:stratification-E1}. On the Koszul locus, the
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];



thinking
**Analyzing Git Changes**

It looks like the `git diff` output is showing some unrelated changes in the rosetta and ordered_associative files, which shouldn't be included in our edits. I need to focus on isolating our specific changes, so maybe I should use `git diff -U0`. However, it might still show unrelated modifications. I'll inspect the current line numbers and possibly use `git blame` to keep track of our edits. Lastly, I should check for any untouched files and ensure everything is neat.
thinking
**Searching for Inverse-Power Patterns**

The initial regex search only returned the r-matrix inverse power forms, which is a good start. Now, I need to focus on finding the remaining inverse-power lambda-bracket patterns in those files. It might be helpful to search using fixed string patterns, one by one, since there were regex errors due to braces. Maybe I should use the `-F` flag for exact matching of the old lines as I search for the remaining patterns.
codex
The remaining `1/\lambda^3` and `1/\lambda^5` hits are now only `r`-matrix formulas, which are allowed. I’m doing one last fixed-string check on the exact old lambda-bracket spellings so I can close with precise file:line findings instead of a vague summary.
exec
/bin/zsh -lc "rg -n -F '{T(z_1) {}_\\lambda T(z_2)} &= \\frac{c/12}{\\lambda"'^3}'"' chapters/examples" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F '{T_\\lambda W} = \\frac{3W}{\\lambda"'^2} + '"\\frac{\\partial W}{\\lambda}' chapters/examples" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F '{T(z_1) {}_\\lambda W(z_2)} = \\frac{3W(z_2)}{\\lambda"'^2} + '"\\frac{\\partial W(z_2)}{\\lambda}.' chapters/examples" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F '\\tfrac{c_{\\mathrm{BP}}}{2}\\,\\lambda"'^3'"' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 52ms:

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];

exec
/bin/zsh -lc "rg -n -F '(1/4)\\lambda"'^3'"' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'sum_{n=1}"'^3 '"\\frac{a_n}{\\lambda"'^n}'"' chapters/examples" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F '\\tfrac{1}{2}\\lambda"'^3'"' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F 'VirLambdaBracket[c_, lambda_] := c/12 / lambda"'^3 + 2 T / lambda''^2 + D[T, z] / lambda;'"' chapters/examples" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 exited 1 in 50ms:

 exited 1 in 51ms:

 exited 1 in 50ms:

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];


thinking
**Gathering line numbers for edits**

I need to get exact line numbers after patching to reference in the final report. Using `nl -ba` on the changed files around the edits should help. I’ll gather the necessary line numbers. It seems I might need to group the findings since the user asked for a specific format: "PROBLEM at file:line" followed by the exact edit applied. The final report should organize findings into 4-6 groups. So, I'll be collecting those line numbers from the edited spots.
exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-virasoro.tex | sed -n '131,136p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras.tex | sed -n '145,150p;1067,1078p;1163,1178p;1380,1425p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-conditional.tex | sed -n '419,429p;516,530p;723,769p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-stable.tex | sed -n '136,140p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   136	The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
   137	\begin{equation}
   138	m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
   139	 \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
   140	\end{equation}
 succeeded in 51ms:
   145	Theorem~\ref{thm:physics-bridge}.
   146	The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
   147	\begin{equation}
   148	m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
   149	 \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
   150	\end{equation}
  1067	\textbf{Singular Part (divided-power $\lambda$-bracket):}
  1068	\begin{align}
  1069	\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
  1070	\end{align}
  1071	
  1072	\textbf{In Mode Expansion:}
  1073	\begin{align}
  1074	\{T_m {}_\lambda T_n\} &= \sum_{k=0}^{m} \binom{m}{k} (-\lambda)^k (k-m-1) T_{m+n-k}\\
  1075	&\quad + \frac{c}{12} \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m-2)(k-m-1)(k-m) \delta_{m+n-k,0}.
  1076	\end{align}
  1077	
  1078	\textbf{Regular Part:}
  1163	\textbf{$m_2(T,W)$:} The mixed bracket is
  1164	\begin{equation}
 succeeded in 51ms:
   131	Theorem~\ref{thm:physics-bridge}.
   132	The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
   133	\begin{equation}
   134	m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
   135	 \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
   136	\end{equation}
 succeeded in 51ms:
   419	\textbf{Singular Part (divided-power $\lambda$-bracket):}
   420	\begin{align}
   421	\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
   422	\end{align}
   423	
   424	\textbf{In Mode Expansion:}
   425	\begin{align}
   426	\{T_m {}_\lambda T_n\} &= \sum_{k=0}^{m} \binom{m}{k} (-\lambda)^k (k-m-1) T_{m+n-k}\\
   427	&\quad + \frac{c}{12} \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m-2)(k-m-1)(k-m) \delta_{m+n-k,0}.
   428	\end{align}
   429	
   516	\begin{equation}
   517	\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
   518	\end{equation}
   519	
   520	\textbf{In Mode Expansion:}
   521	\begin{equation}
   522	\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}.
   523	\end{equation}
   524	
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];

exec
/bin/zsh -lc "nl -ba chapters/examples/rosetta_stone.tex | sed -n '6322,6327p;6613,6617p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/w-algebras-frontier.tex | sed -n '46,49p;133,144p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '2844,2849p;3020,3024p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  2844	\begin{align}
  2845	\{T_\lambda\, T\}
  2846	&\;=\;
  2847	\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
  2848	+ 2T\lambda + \partial T,
  2849	\label{eq:bp-TT}
  3020	\emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
  3021	into the matter sector.}
  3022	The quartic $T$--$T$ OPE pole, equivalently the divided-power
  3023	term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
  3024	generates a depth-$3$ collision residue.
 succeeded in 52ms:
  6322	\emph{Binary operation.}
  6323	At $k = 2$ (Ising model, $c = 1/2$), the single generator
  6324	is $T$ and the binary operation is
  6325	$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
  6326	+ \partial T$.
  6327	This is the standard Virasoro $m_2$ at $c = 1/2$.
  6613	On the Virasoro field $T$, the binary operation is
  6614	the standard Virasoro $m_2$ at $c = 1$:
  6615	$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
  6616	+ 2T\lambda + \partial T$.
  6617	
 succeeded in 52ms:
    46	The singular part (the divided-power $\lambda$-bracket) is
    47	\begin{align}
    48	\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
    49	\end{align}
   133	\[
   134	\{T_\lambda W\} = \partial W + 3\lambda W,
   135	\]
   136	and in modes,
   137	$\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
   138	The self-bracket $\{W_\lambda W\}$
   139	(cf.\ equation~\eqref{eq:m2WW-recap} for the compact
   140	polynomial form) is
   141	\begin{align}
   142	\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
   143	&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
   144	\end{align}
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];

codex
The search surface is clean. I’m adding one executable check now against the existing PVA guardrails so the manuscript edits are backed by the compute layer, not just by grep.
exec
/bin/zsh -lc 'pytest -q compute/tests/test_pva_axioms.py' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'pytest -q compute/tests/test_pva_descent_coefficients_engine.py' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 459ms:
....................................                                     [100%]
36 passed in 0.20s
 exited 1 in 462ms:
..F.......                                                               [100%]
=================================== FAILURES ===================================
____________ TestHeisenberg.test_heisenberg_D3_D5_skew_and_leibniz _____________

self = <tests.test_pva_descent_coefficients_engine.TestHeisenberg object at 0x10ce5e2c0>

    def test_heisenberg_D3_D5_skew_and_leibniz(self):
        """D_3 and D_5 simultaneously: Heisenberg is central.
    
        Path A: compute_D3(J,J) should vanish because {J_lam J} = k*lam
            and -{J_{-lam-d} J} = -k*(-lam - 0) = k*lam; matches.
        Path B: {J_lam (J*J)} by Leibniz = 2 k lam * J; the engine D_5
            residue must vanish on (J, J, J).  Independent check:
            direct Leibniz expansion from the chapter example lines
            1301--1305: {J_lam(J*J)} = 2k lam J.
        """
        spec = heisenberg_pva(k)
        d3 = compute_D3(spec, "J", "J", lam)
        d5 = compute_D5(spec, "J", "J", "J", lam)
>       assert d3 == 0
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];


thinking
**Evaluating test failures**

I noticed a test failed, but it's unrelated to our changes, so I need to mention that. I might not need to fix it if it's a preexisting issue. To be thorough, I could verify our specific issue with tests that passed. It might be a good idea to run targeted tests in the second file related to Virasoro to ensure relevance. I can use a command to run those specific tests and possibly update the commentary afterward.
codex
One broader engine test file has a preexisting Heisenberg failure unrelated to the Virasoro convention surface, so I’m narrowing the executable check to the Virasoro/AP34 cases inside that file. That will separate a real regression from an unrelated red test already present in the repo.
exec
/bin/zsh -lc "pytest -q compute/tests/test_pva_descent_coefficients_engine.py -k 'Virasoro or virasoro or AP34'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "pytest -q compute/tests/test_examples.py -k 'virasoro or lambda'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 673ms:
............                                                             [100%]
12 passed, 34 deselected in 0.24s
 succeeded in 725ms:
..                                                                       [100%]
2 passed, 8 deselected in 0.27s
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];

Plan update
  ✓ Search the active Vol II manuscript and compute surfaces for lambda-bracket formulas, Virasoro central-term conventions, and V2-AP34 references.
  ✓ Read the local context for each suspect occurrence, determine whether the divided-power convention is wrong, and identify the minimum truthful edits.
  ✓ Apply exact fixes only where needed, then verify the remaining search surface and summarize each finding with file:line plus the exact edit applied.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];

codex
**Findings**
- PROBLEM at [w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:134), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:138), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:148): the Virasoro lambda-bracket was advertised as `\sum a_n/\lambda^n`, which is an OPE-kernel presentation, not the Vol II divided-power lambda-bracket. EXACT edit applied: replaced that with `a_1 + a_2 \lambda + a_3 \lambda^3` and added the convention lock `a_3 = T_{(3)}T/3! = c/12`.
- PROBLEM at [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1067), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1165), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1175), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:419), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:517), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:527), [w-algebras-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:46), [w-algebras-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:134), [w-algebras-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:142): several lambda-brackets were still written with inverse powers of `\lambda`. EXACT edit applied: converted them to the divided-power polynomial forms
  `{T_\lambda T} = \partial T + 2T\lambda + (c/12)\lambda^3`,
  `{T_\lambda W} = \partial W + 3\lambda W`,
  `{W_\lambda W} = (c/360)\lambda^5 + (1/3)T\lambda^3 + (1/2)(\partial T)\lambda^2 + \cdots`.
- PROBLEM at [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1380), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:1420), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:724), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:764): the sample Mathematica code encoded the same inverse-power convention. EXACT edit applied: rewrote `VirLambdaBracket` and `W3LambdaBracket` to polynomial lambda-brackets and changed the expansion from `Series[..., {lambda, Infinity, -n}]` to `Series[..., {lambda, 0, n}]`.
- PROBLEM at [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:6325) and [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:6615): the Ising and `c=1` specializations used the OPE coefficient instead of the divided-power lambda-bracket coefficient. EXACT edit applied: changed `(1/4)\lambda^3` to `(1/24)\lambda^3` for `c=1/2`, and `\tfrac{1}{2}\lambda^3` to `\tfrac{1}{12}\lambda^3` for `c=1`.
- PROBLEM at [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:2847) and [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:3022): the BP Virasoro subalgebra still used `c_{\mathrm{BP}}/2` on the `\lambda^3` term and the surrounding prose matched that wrong convention. EXACT edit applied: changed the bracket to `\tfrac{c_{\mathrm{BP}}}{12}\lambda^3 + 2T\lambda + \partial T` and rewrote the prose to say the quartic OPE pole is equivalent to the divided-power term `(c_{\mathrm{BP}}/12)\lambda^3` in `\{T_\lambda T\}`.

**Verification**
- Grep sweep: no remaining old lambda-bracket spellings of the bad forms; the remaining `1/\lambda^3` and `1/\lambda^5` hits are `r`-matrix formulas, not lambda-brackets.
- `pytest -q compute/tests/test_pva_axioms.py`: `36 passed`.
- `pytest -q compute/tests/test_pva_descent_coefficients_engine.py -k 'Virasoro or virasoro or AP34'`: `2 passed`.
- `pytest -q compute/tests/test_examples.py -k 'virasoro or lambda'`: `12 passed`.
- `pytest -q compute/tests/test_pva_descent_coefficients_engine.py` still has an unrelated preexisting failure in `TestHeisenberg::test_heisenberg_D3_D5_skew_and_leibniz` (`assert 2*k*lam == 0`). I did not change that surface.
- I did not run a TeX build.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 5175e461354fe393ca4a4b3147d9358e86719a5f..aeee300c7a18488058cab861d0172bdcb511796a
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -2844,7 +2844,7 @@
 \begin{align}
 \{T_\lambda\, T\}
 &\;=\;
-\tfrac{c_{\mathrm{BP}}}{2}\,\lambda^3
+\tfrac{c_{\mathrm{BP}}}{12}\,\lambda^3
 + 2T\lambda + \partial T,
 \label{eq:bp-TT}
 \\[4pt]
@@ -3019,8 +3019,9 @@
 
 \emph{(b) $m_3(T,T,\Gp)$: quartic shadow does not propagate
 into the matter sector.}
-The quartic pole $c_{\mathrm{BP}}\lambda^3/2$ in the
-$T$--$T$ OPE generates a depth-$3$ collision residue.
+The quartic $T$--$T$ OPE pole, equivalently the divided-power
+term $(c_{\mathrm{BP}}/12)\lambda^3$ in $\{T_\lambda T\}$,
+generates a depth-$3$ collision residue.
 However, when one of the three inputs is a fermionic
 generator $\Gp$ (or $\Gm$), the transferred product
 $m_3(T,T,\Gp)$ receives contributions only from the
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 3bd261fe91bf6e13581564bb77aa6dfed82ece93..56c406abff7b73e78179a21bfa35b907f79cf3cb
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -6322,7 +6322,7 @@
 \emph{Binary operation.}
 At $k = 2$ (Ising model, $c = 1/2$), the single generator
 is $T$ and the binary operation is
-$m_2(T, T;\, \lambda) = (1/4)\lambda^3 + 2T\lambda
+$m_2(T, T;\, \lambda) = (1/24)\lambda^3 + 2T\lambda
 + \partial T$.
 This is the standard Virasoro $m_2$ at $c = 1/2$.
 For $k = 2$, the GKO bar complex is isomorphic to
@@ -6612,7 +6612,7 @@
 the invariant sector because $J$ is $\sigma$-odd.
 On the Virasoro field $T$, the binary operation is
 the standard Virasoro $m_2$ at $c = 1$:
-$m_2(T, T;\, \lambda) = \tfrac{1}{2}\lambda^3
+$m_2(T, T;\, \lambda) = \tfrac{1}{12}\lambda^3
 + 2T\lambda + \partial T$.
 
 \smallskip
diff --git a/chapters/examples/w-algebras-conditional.tex b/chapters/examples/w-algebras-conditional.tex
index 18d3df994db755e1b87286101d3ac9699e4edfbe..70814726d623e97693123c59632e0d6dd4994c31
--- a/chapters/examples/w-algebras-conditional.tex
+++ b/chapters/examples/w-algebras-conditional.tex
@@ -416,10 +416,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -515,7 +514,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -525,8 +524,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -722,11 +721,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
  ExpandLambdaBracket[expr_, lambda_, n_] :=
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -763,9 +762,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c)) / lambda
- + 1/15 * D[T, {z, 3}] + 32/(5*c) * T * D[T, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];
diff --git a/chapters/examples/w-algebras-frontier.tex b/chapters/examples/w-algebras-frontier.tex
index f845ebfe252450961a4e18f5b207210f3fe591fe..9c349f23d48a9d7941c8bf16e27f179980837a2d
--- a/chapters/examples/w-algebras-frontier.tex
+++ b/chapters/examples/w-algebras-frontier.tex
@@ -43,9 +43,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-The singular part (the $\lambda$-bracket) is
+The singular part (the divided-power $\lambda$-bracket) is
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\,.
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 In modes,
 \begin{align}
@@ -131,7 +131,7 @@
 The binary operation $m_2(T,T)$ is identical to Virasoro.
 The mixed bracket is
 \[
-\{T_\lambda W\} = \frac{3W}{\lambda^2} + \frac{\partial W}{\lambda},
+\{T_\lambda W\} = \partial W + 3\lambda W,
 \]
 and in modes,
 $\{T_m {}_\lambda W_n\} = \sum_{k=0}^m \binom{m}{k} (-\lambda)^k (k-m) W_{m+n-k} + \frac{1}{k!} \partial^k W_{m+n-k}$.
@@ -139,8 +139,8 @@
 (cf.\ equation~\eqref{eq:m2WW-recap} for the compact
 polynomial form) is
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1217,4 +1217,3 @@
 class~$\mathbf{M}$ with one generator to class~$\mathbf{M}$
 with $N - 1$ generators.
 \end{remark}
-
diff --git a/chapters/examples/w-algebras-stable.tex b/chapters/examples/w-algebras-stable.tex
index d428ecb5ae05708302999cf0be885653eea63ed5..770d988f5084dc8ea78220e13c181a7d94493e80
--- a/chapters/examples/w-algebras-stable.tex
+++ b/chapters/examples/w-algebras-stable.tex
@@ -135,8 +135,8 @@
 \textup{(}Definition~\textup{\ref{def:log-SC-algebra})}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
diff --git a/chapters/examples/w-algebras-virasoro.tex b/chapters/examples/w-algebras-virasoro.tex
index 86a620f695d4c0d9fa3fcd20a500be3156202a32..43b263d94c36ef6aaa1aa477910055a46196d033
--- a/chapters/examples/w-algebras-virasoro.tex
+++ b/chapters/examples/w-algebras-virasoro.tex
@@ -131,8 +131,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 (We use $\zeta = z_1 - z_2$ for the position-space variable and
 $\lambda$ for the PVA spectral parameter; the Borel transform
diff --git a/chapters/examples/w-algebras.tex b/chapters/examples/w-algebras.tex
index b37933c91b3fab5344ae4197187d9aee3b9c52d9..a768576afc49a17621bee3b521e90cd8da242f73
--- a/chapters/examples/w-algebras.tex
+++ b/chapters/examples/w-algebras.tex
@@ -145,8 +145,8 @@
 Theorem~\ref{thm:physics-bridge}.
 The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
 \begin{equation}
-m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
- \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
+m_2(T, T)_\text{sing} = \{T_\lambda T\} = a_1 + a_2 \lambda + a_3 \lambda^3,
+ \qquad\text{(divided-power convention: $a_3 = T_{(3)}T/3! = c/12$)}
 \end{equation}
 where
 \begin{align}
@@ -1064,10 +1064,9 @@
 
 \subsubsection{The Binary Operation $m_2(T,T)$}
 
-\textbf{Singular Part ($\lambda$-bracket):}
+\textbf{Singular Part (divided-power $\lambda$-bracket):}
 \begin{align}
-\{T(z_1) {}_\lambda T(z_2)\} &= \frac{c/12}{\lambda^3} + \frac{2T(z_2)}{\lambda^2} + \frac{\partial T(z_2)}{\lambda}\\
-&= \sum_{n=0}^\infty \frac{1}{n!} \partial^n \left( \frac{c/12}{\lambda^3} + \frac{2T}{\lambda^2} + \frac{\partial T}{\lambda} \right).
+\{T(z_1) {}_\lambda T(z_2)\} &= \partial T(z_2) + 2\lambda\,T(z_2) + \frac{c}{12}\lambda^3.
 \end{align}
 
 \textbf{In Mode Expansion:}
@@ -1163,7 +1162,7 @@
 
 \textbf{$m_2(T,W)$:} The mixed bracket is
 \begin{equation}
-\{T(z_1) {}_\lambda W(z_2)\} = \frac{3W(z_2)}{\lambda^2} + \frac{\partial W(z_2)}{\lambda}.
+\{T(z_1) {}_\lambda W(z_2)\} = \partial W(z_2) + 3\lambda\,W(z_2).
 \end{equation}
 
 \textbf{In Mode Expansion:}
@@ -1173,8 +1172,8 @@
 
 \textbf{$m_2(W,W)$:} The self-bracket for $W$ is the most complex:
 \begin{align}
-\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c/360}{\lambda^5} + \frac{T(z_2)/3}{\lambda^3} + \frac{\partial T(z_2)/2}{\lambda^2}\\
-&\quad + \frac{(3/10)\partial^2 T(z_2) + (32/(5c+22))\Lambda}{\lambda} + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
+\{W(z_1) {}_\lambda W(z_2)\} &= \frac{c}{360}\lambda^5 + \frac{1}{3}T(z_2)\lambda^3 + \frac{1}{2}(\partial T(z_2))\lambda^2\\
+&\quad + \left(\frac{3}{10}\partial^2 T(z_2) + \frac{32}{5c+22}\Lambda\right)\lambda + \frac{1}{15}\partial^3 T + \frac{16}{5c+22}\partial\Lambda.
 \end{align}
 
 \subsubsection{The Ternary Operations}
@@ -1378,11 +1377,11 @@
 
 \begin{verbatim}
 (* Define Virasoro lambda-bracket *)
-VirLambdaBracket[c_, lambda_] := c/12 / lambda^3 + 2 T / lambda^2 + D[T, z] / lambda;
+VirLambdaBracket[c_, lambda_] := D[T, z] + 2 T lambda + (c/12) lambda^3;
 
 (* Expand in spectral parameter *)
 ExpandLambdaBracket[expr_, lambda_, n_] := 
- Series[expr, {lambda, Infinity, -n}] // Normal;
+ Series[expr, {lambda, 0, n}] // Normal;
 
 (* Compute singular part of m_2 *)
 m2Sing = ExpandLambdaBracket[VirLambdaBracket[c, lambda], lambda, 5];
@@ -1419,9 +1418,9 @@
 \begin{verbatim}
 (* Define W_3 W-W lambda-bracket *)
 W3LambdaBracket[c_, lambda_] :=
- c/360 / lambda^5 + T/3 / lambda^3 + D[T, z]/2 / lambda^2
- + (3/10 * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) / lambda
- + 1/15 * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
+ (c/360) lambda^5 + (T/3) lambda^3 + (D[T, z]/2) lambda^2
+ + ((3/10) * D[T, {z, 2}] + 32/(5*c + 22) * Lambda) lambda
+ + (1/15) * D[T, {z, 3}] + 16/(5*c + 22) * D[Lambda, z];
 
 (* Expand *)
 m2WWsing = ExpandLambdaBracket[W3LambdaBracket[c, lambda], lambda, 7];

tokens used
139,855
