# D15_e1_einf_v2 (445s)

1. PROBLEM at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1589) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1729): `E_\infty` was stated as if it meant `commutative chiral algebra`. EXACT edit applied: changed `An $E_\infty$-algebra (commutative chiral algebra) has` to `An $E_\infty$-chiral algebra has`, and added `The pole-free BD-commutative subclass is a special case.`

2. PROBLEM at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1998) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1893): the ordered/unordered comparison said the two coincide for `E_\infty`-chiral algebras as such, collapsing `E_\infty` to the pole-free subclass. EXACT edit applied: replaced `For $E_\infty$-chiral algebras (commutative chiral algebras), the two are equivalent.` with `For $E_\infty$-chiral algebras in the pole-free BD-commutative subclass, the two are equivalent. For local vertex algebras with OPE poles, the comparison is still $E_\infty$-chiral but requires the OPE-derived $R$-matrix twist.`

3. PROBLEM at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2351), [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2383), [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2719), [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2025), and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2052): the descent/`R`-matrix clauses used `For $E_\infty$-algebras...` or `For pole-free $E_\infty$-algebras...` in a way that made pole-freeness sound definitional. EXACT edit applied: rewrote each clause to `For the pole-free BD-commutative subclass of $E_\infty$-chiral algebras, ...`; in the core file I also changed `For $E_\infty$-algebras with OPE poles` to `For local vertex algebras in the $E_\infty$ regime with OPE poles`.

4. PROBLEM at [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:111): `E_\infty` was glossed as `i.e. has only simple poles`. EXACT edit applied: changed `which is $E_\infty$-chiral, i.e.\ has only simple poles` to `which remains $E_\infty$-chiral and, by construction of the commutator filtration, has only first-order OPE singularities`.

5. PROBLEM at [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:3044): the three-tier summary treated class `L` as the `E_\infty` poleful tier and left class `M` outside that local `E_\infty` regime. EXACT edit applied: changed the tier labels to `Tier~(i) (pole-free BD-commutative $E_\infty$ subclass)`, `Tier~(ii) (local $E_\infty$ with OPE poles, class~L)`, and `Tier~(iii) (still local $E_\infty$, class~M)`.

6. PROBLEM at [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:15913) and [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:15978): the duality summary still used `pole-free $E_\infty$-chiral` phrasing that invited the same false identification. EXACT edit applied: changed those clauses to `the pole-free BD-commutative subclass of $E_\infty$-chiral algebras` and `lies in the pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.

Verification: I re-grepped the scope for the exact bad equivalences (`E_\infty = commutative/pole-free`, `E_\infty = simple-pole`, and the old tier label), and those hits are now gone. I did not run a LaTeX build.


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
session id: 019d87cd-dddd-7b03-a6c6-ef5341d67273
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


Fix E_1/E_inf terminology violations in Vol II (V2-AP1-AP24).
Search for 'E_inf' near 'no poles' or 'not E_inf' near 'vertex algebra'.
All VAs are E_inf. OPE poles don't break E_inf. Fix violations.
mcp startup: no servers
codex
Target is Vol II terminology drift around `E_1` versus `E_inf`; I’m checking the live surface first, then I’ll patch only the violating files. Using `vol2-deep-audit` for the findings pass and `vol2-beilinson-rectification` for the minimal fixes.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-deep-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
---
name: vol2-beilinson-rectification
description: Use when the user asks to audit, rectify, fortify, fix, tighten, or converge a Vol II chapter, theorem, proof, introduction, appendix, or the live manuscript surface. Do not use for purely local copyedits with no mathematical or structural truth conditions.
---

# Vol II Beilinson Rectification

Run the full local rectification loop on the live surface.

## Inputs

- exact target file or theorem if given
- otherwise the smallest live surface implied by the user prompt

## Mandatory loop

1. Start with a short progress update naming the target and first verification step.
2. Register a nontrivial task in `update_plan`.
3. Read before editing:
   - target file
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
**Evaluating input needs**

I need to work with the active input graph from main.tex and look for target patterns. Maybe I could use `rg` for analyzing E_inf near no poles or if it isn't near the vertex algebra. I should read the context and check relevant files too. Using `rg` with context over the repo sounds like a solid plan. Additionally, I might need to check the `\input` lines in main.tex to know which files are active. Let’s update the plan now!
codex
I’ve confirmed the tree is already dirty in many manuscript files, so I’m treating this as a surgical pass inside the user’s stated scope and avoiding unrelated surfaces. Next I’m locating every active and superseded Vol II phrasing that ties `E_inf` to pole-freeness or claims a vertex algebra is “not `E_inf`.”
Plan update
Audit and repair Vol II `E_1`/`E_inf` terminology violations around vertex algebras and OPE poles, then verify the corrected surface and record the findings.
  → Inspect active Vol II input graph and grep for `E_inf`/`vertex algebra`/`no poles` violation patterns
  • Read the exact contexts, classify actionable terminology violations, and record them in the audit ledger
  • Apply minimal truthful edits only in violating files
  • Re-grep the scope to verify the violations are removed and summarize exact fixes
exec
/bin/zsh -lc "rg -n \"\\\\input\\{|\\\\include\\{\" main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -C 3 \"E_inf|E\\\\\\\\infty|not E_inf|not E\\\\\\\\infty|vertex algebra|no poles|pole-free|poles\" chapters working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:\input\{|\include\{)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
Total output lines: 7086

working_notes.tex-158-cooperad, the operadic fingerprint
working_notes.tex-159-of a $3$d holomorphic-topological field theory
working_notes.tex-160-on~$\mathbb{C} \times \mathbb{R}$:
working_notes.tex:161:$(-1)$-shifted Poisson vertex algebra on cohomology,
working_notes.tex-162-the bulk-boundary-line triangle, dg-shifted Yangians on the line,
working_notes.tex-163-and curved Swiss-cheese at genus~$g \ge 1$ where
working_notes.tex-164-$d_{\mathrm{fib}}^{\,2} = \kappa \cdot \omega_g$ couples the
--
working_notes.tex-454-% =================================================================
working_notes.tex-455-
working_notes.tex-456-The holomorphic Swiss-cheese algebra, projected to cohomology,
working_notes.tex:457:produces a Poisson vertex algebra (PVA).  The descent is
working_notes.tex-458-controlled by six axioms D1--D6, each proved by a geometric
working_notes.tex-459-argument on $\FM_k(\C)$.
working_notes.tex-460-
--
working_notes.tex-603-\subsection*{Gravity}
working_notes.tex-604-

thinking
**Refining search patterns**

I see that my initial approach with `rg` is too broad, so I need to target specific patterns better. I'll focus on fixing only the assigned files and inspect the `main.tex` inputs. Maybe I can simplify my grep command to search for lines starting with `\input`. I think using `rg -n '^\\(input|include)\{' could work, or maybe even using escaped regex. The user has requested specific searches, like finding 'E_inf' near 'no poles', so I’ll run those targeted searches.
codex
The first broad grep confirms this drift lives in the manuscript surface, but it’s too noisy for a safe patch. I’m narrowing to exact violation shapes now so I only touch places that actually assert the wrong criterion.
exec
/bin/zsh -lc "rg -n '"'^'"\\\\(input|include)\\{' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -C 3 \"no poles|pole-free|not E_\\\\infty|not E_inf|vertex algebra\" chapters README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -C 4 \"E_\\\\infty|E_inf|not E_\\\\infty|not E_inf|vertex algebra\" chapters README.md working_notes.tex | rg -n \"no poles|pole-free|poles|not E_|vertex algebra\"" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:
rg: regex parse error:
    (?:E_\infty|E_inf|not E_\infty|not E_inf|vertex algebra)
         ^^
error: unrecognized escape sequence
 exited 2 in 52ms:
rg: regex parse error:
    (?:no poles|pole-free|not E_\infty|not E_inf|vertex algebra)
                                ^^
error: unrecognized escape sequence
 succeeded in 52ms:
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
1297:\input{chapters/connections/bar-cobar-review}
1298:\input{chapters/connections/line-operators}
1299:\input{chapters/connections/ordered_associative_chiral_kd_core}
1300:\input{chapters/connections/dg_shifted_factorization_bridge}
1301:\input{chapters/connections/thqg_gravitational_yangian}

thinking
**Fixing escape patterns**

I need to work on fixing the escaping issues. I'll consider using the "-F" option for literal searches and focus on identifying all occurrences of specific strings like "E_\infty", "E_inf", "vertex algebra", "no poles", and "pole-free." It might be helpful to use `rg` with "-F" and multiple "-e" options or PCRE with escaped backslashes. I plan to execute precise searches using `rg` to inspect contexts and narrow the scope to specific chapters and files. Storing the output could be useful too!
codex
I have the active `\input` map now. The next pass is literal matching, not regex guessing, so I can separate real theorem-language violations from harmless mentions of poles or vertex algebras.
exec
/bin/zsh -lc "rg -n -C 3 -F -e 'not E_\\infty' -e 'not E_inf' -e 'no poles' -e 'pole-free' chapters README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -C 3 -F -e 'E_\\infty' -e 'E_inf' -e 'no poles' -e 'pole-free' -e 'vertex algebra' chapters README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -C 4 -F -e 'vertex algebra' chapters README.md working_notes.tex | rg -n -F -e 'not E' -e 'E_\\infty' -e 'E_inf' -e 'no poles' -e 'pole-free'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
working_notes.tex-3041-
working_notes.tex-3042-The three-tier picture (AP51) maps precisely:
working_notes.tex-3043-\begin{itemize}[nosep]
working_notes.tex:3044:\item Tier~(i) (pole-free): forgetful functor to
working_notes.tex-3045-  $\mathrm{Vect}$, commutative Hopf algebra.
working_notes.tex-3046-\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
working_notes.tex-3047-  exists, compact quantum group.
--
working_notes.tex-15910-The descent from ordered to unordered is $R$-twisted:
working_notes.tex-15911-$B^{\mathrm{ch}}(\cA)_n \simeq
working_notes.tex-15912-(\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
working_notes.tex:15913:For pole-free $E_\infty$-chiral algebras (the
working_notes.tex-15914-BD-commutative subclass: no OPE singularities):
working_notes.tex-15915-$R(z) = \tau$ (the flip), descent is trivial, both
working_notes.tex-15916-duals carry equivalent information.  For
--
working_notes.tex-15975-differential remains the sole gap.
working_notes.tex-15976-
working_notes.tex-15977-\medskip\noindent\textbf{When do the two duals agree?}\enspace
working_notes.tex:15978:When $\cA$ is pole-free $E_\infty$-chiral (the
 succeeded in 50ms:
Total output lines: 4569

working_notes.tex-158-cooperad, the operadic fingerprint
working_notes.tex-159-of a $3$d holomorphic-topological field theory
working_notes.tex-160-on~$\mathbb{C} \times \mathbb{R}$:
working_notes.tex:161:$(-1)$-shifted Poisson vertex algebra on cohomology,
working_notes.tex-162-the bulk-boundary-line triangle, dg-shifted Yangians on the line,
working_notes.tex-163-and curved Swiss-cheese at genus~$g \ge 1$ where
working_notes.tex-164-$d_{\mathrm{fib}}^{\,2} = \kappa \cdot \omega_g$ couples the
--
working_notes.tex-454-% =================================================================
working_notes.tex-455-
working_notes.tex-456-The holomorphic Swiss-cheese algebra, projected to cohomology,
working_notes.tex:457:produces a Poisson vertex algebra (PVA).  The descent is
working_notes.tex-458-controlled by six axioms D1--D6, each proved by a geometric
working_notes.tex-459-argument on $\FM_k(\C)$.
working_notes.tex-460-
--
working_notes.tex-1314-of Volume~I (built from a Lie conformal algebra $L$) and the
working_notes.tex-1315-eight-fold $\Pi^{\mathrm{oc}}_X(\cA)$ (built from a chiral
 succeeded in 50ms:
200:working_notes.tex-15917-$E_\infty$-chiral algebras with OPE poles
201:working_notes.tex-15918-(Heisenberg, affine KM, Virasoro --- still $E_\infty$,
202:working_notes.tex:15919:since all vertex algebras are $E_\infty$-chiral):
211:working_notes.tex-15983-When $\cA$ is $E_\infty$-chiral with OPE poles (all
213:working_notes.tex-15985-Virasoro --- these are still $E_\infty$, since all
214:working_notes.tex:15986:vertex algebras are $E_\infty$-chiral): $R(z)$
1298:chapters/connections/spectral-braiding-core.tex:508:coherence datum.  For $E_\infty$-chiral algebras (vertex algebras),
2009:chapters/frame/preface_trimmed.tex-209-differential~$D_\cA$. For $E_\infty$-chiral algebras (all
2173:chapters/frame/preface.tex-502-$E_\infty$: locality is compatible with arbitrary pole order. The
2180:chapters/frame/preface.tex:509:$E_\infty$-chiral algebras (all vertex algebras), the $R$-matrix is
2950:chapters/connections/hochschild.tex-1769-For the pole-free sub-class (BD commutative chiral
3048:chapters/connections/bar-cobar-review.tex-1639- $E_\infty$-chiral algebras with OPE poles (all interesting
3052:chapters/connections/bar-cobar-review.tex-1643- (Proposition~\ref{prop:r-matrix-descent}). For the pole-free
3169:chapters/connections/ordered_associative_chiral_kd_core.tex:1970:$E_\infty$-chiral (it is a local vertex algebra), so its
3177:chapters/connections/ordered_associative_chiral_kd_core.tex-2405-for $E_\infty$-chiral algebras (including those with OPE
3185:chapters/connections/ordered_associative_chiral_kd_core.tex-2712-$E_\infty$-chiral algebras (commutative chiral algebras)
3186:chapters/connections/ordered_associative_chiral_kd_core.tex-2713-whose OPE is pole-free, $R(z) = \tau$ and both
3188:chapters/connections/ordered_associative_chiral_kd_core.tex-2715-$E_\infty$-chiral algebras with OPE poles
3199:chapters/connections/ordered_associative_chiral_kd_core.tex:4734:For $E_\infty$-chiral algebras (vertex algebras in the sense
3209:chapters/connections/ordered_associative_chiral_kd_core.tex:4773:For $E_\infty$-chiral algebras (vertex algebras), the $n$-th


thinking
**Considering audit ledger updates**

I might need to update the audit ledger with an entry since the user requested the final format. It seems necessary to document this in the compute/audit/linear_read_notes.md file. I should add the entry there after inspecting the contexts in active files like preface.tex and others. I’ll look for the phrase "not E_inf" with a search tool and check if "pole-free E_inf-chiral" is acceptable referring to a commutative subclass. The user's input highlights key points to clarify.
thinking
**Examining terminology clarity**

I need to check if there's a differentiation between tier(i) pole-free commutative algebras and tier(ii) E_inf algebras with poles. It's important to ensure that the terminology doesn't imply that the pole-free case is entirely separate from E_inf. I want to identify any actual violations of terminology here to avoid any potential misunderstandings. I’ll gather more context on these distinctions to clarify further.
exec
/bin/zsh -lc "rg -n -F -e 'not E_\\infty' -e 'not E_inf' -e 'not "'$E_'"\\infty"'$'"' -e 'not "'$E_1$'"' chapters README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F -e 'vertex algebras are "'$E_'"\\infty"'$-chiral'"' -e 'all vertex algebras' -e '"'$E_'"\\infty"'$-chiral (it is a local vertex algebra)'"' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/connections/spectral-braiding-core.tex chapters/connections/bar-cobar-review.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/line-operators.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'no poles' -e 'pole-free' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/connections/spectral-braiding-core.tex chapters/connections/bar-cobar-review.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/line-operators.tex chapters/examples/rosetta_stone.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/line-operators.tex:602:pole-free commutative algebras have $R(z) = \tau$: the flat
chapters/connections/line-operators.tex:611:are invisible in the pole-free commutative limit and
chapters/examples/rosetta_stone.tex:1910:\item $\chirCom$: pole-free commutative chiral algebras.
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3434: & no poles
chapters/connections/ordered_associative_chiral_kd_frontier.tex:6146:quotient works only for pole-free algebras. For
chapters/connections/bar-cobar-review.tex:1643: (Proposition~\ref{prop:r-matrix-descent}). For the pole-free
chapters/connections/ordered_associative_chiral_kd_core.tex:2347:For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
chapters/connections/ordered_associative_chiral_kd_core.tex:2377:For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
chapters/connections/ordered_associative_chiral_kd_core.tex:2713:whose OPE is pole-free, $R(z) = \tau$ and both
chapters/connections/ordered_associative_chiral_kd_core.tex:2744: ($\mathbf{G}$ = pole-free,
working_notes.tex:3044:\item Tier~(i) (pole-free): forgetful functor to
working_notes.tex:15913:For pole-free $E_\infty$-chiral algebras (the
working_notes.tex:15978:When $\cA$ is pole-free $E_\infty$-chiral (the
 succeeded in 52ms:
chapters/frame/preface.tex:505:$E_\infty$-chiral algebras (all vertex algebras), the $R$-matrix is
working_notes.tex:15919:since all vertex algebras are $E_\infty$-chiral):
working_notes.tex:15986:vertex algebras are $E_\infty$-chiral): $R(z)$
chapters/connections/ordered_associative_chiral_kd_core.tex:1970:$E_\infty$-chiral (it is a local vertex algebra), so its

thinking
**Searching for algebra patterns**

I'm exploring the idea that "vertex algebra is not E_inf." I want to look for patterns in phrasing, maybe things like "not E∞ because of poles." To dig deeper, I should search for "local vertex algebra" combined with "not." I’ll also look for lines that mention E1/Einf in relation to vertex algebra or poles. Maybe I can use regex for patterns like `vertex algebra.*E_1` or `E_1.*vertex algebra` and examine those results.
codex
I’m not seeing the literal `not E_\infty` string yet; the drift is more subtle: phrases that split “pole-free” off from `E_\infty` as if poles force a drop to `E_1`. I’m checking those exact comparison passages before editing.
exec
/bin/zsh -lc "sed -n '1958,1990p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '490,520p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -C 3 -F -e 'vertex algebra' -e '"'$E_1$'"' -e '"'$E_'"\\infty"'$'"' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/connections/spectral-braiding-core.tex chapters/connections/bar-cobar-review.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/line-operators.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
(classes~$\mathbf{L}$, $\mathbf{C}$), and $\Delta \neq 0$
with infinite depth (class~$\mathbf{M}$: gravitational) is the
gauge-gravity dichotomy: the discriminant decides whether the 3d
theory has a gravitational sector.

\smallskip
\noindent\textbf{(3) Local to nonlocal.}\enspace
All standard vertex algebras, including those with OPE poles, are
$E_\infty$: locality is compatible with arbitrary pole order. The
genuinely $E_1$ layer is where the spectral $R$-matrix is an
independent input, not derived from the local OPE, and the
line-side dual $\cA^!_{\mathrm{line}}$ is a dg-shifted Yangian.
The ordered bar $B^{\mathrm{ord}}$ is the primitive; the symmetric
bar $B^{\Sigma}$ is its $R$-matrix-twisted $\Sigma_n$-coinvariant
projection. The distinction is provenance, not pole order. For
$E_\infty$-chiral algebras (all vertex algebras), the $R$-matrix is
derived from the OPE: the collision residue at degree~$2$ gives
$r(z) = k/z$ (Heisenberg) or $r(z) = k\,\Omega/z$ (Kac--Moody,
trace-form convention, vanishing at $k = 0$). For genuinely $E_1$
algebras (Yangians, Etingof--Kazhdan quantum vertex algebras), the
 succeeded in 52ms:
d^2\ne 0\colon & [e|f|h],\;[e|h|f],\;[f|e|h],\;
 [f|h|e],\;[h|e|f],\;[h|f|e], \\
 & [e|f|e],\;[e|f|f],\;[f|e|e],\;
 [f|e|f],\;[e|h|e],\;[f|h|f]. \\[4pt]
d^2=0\colon & [e|e|e],\;[f|f|f],\;[h|h|h], \\
 & [e|e|f],\;[e|e|h],\;[f|f|e],\;
 [f|f|h],\;[h|h|e],\;[h|h|f], \\
 & [e|h|h],\;[f|h|h],\;[h|e|e],\;
 [h|f|f],\;[h|e|h],\;[h|f|h].
\end{array}
\]
This is expected: $V_k(\mathfrak{sl}_2)$ is
$E_\infty$-chiral (it is a local vertex algebra), so its
operations are defined on unordered configurations. The
ordered-all-pair differential conflates the ordered and
unordered structures without the $R$-matrix twist
needed for descent
(Proposition~\ref{prop:r-matrix-descent}), and the
resulting inconsistency manifests as $d^2\ne 0$.

 succeeded in 51ms:
Total output lines: 2720

chapters/connections/line-operators.tex-9-$\mathcal{A}^!_{\mathrm{line}}$, and spectral $R$-matrices
chapters/connections/line-operators.tex-10-controlling their OPE emerge from the bar-cobar adjunction.
chapters/connections/line-operators.tex-11-
chapters/connections/line-operators.tex:12:\begin{remark}[$E_1$ primacy of line operators]
chapters/connections/line-operators.tex-13-\label{rem:line-operators-e1-primacy}
chapters/connections/line-operators.tex:14:Line operators are natively $E_1$ data: they are modules over the
chapters/connections/line-operators.tex-15-\emph{ordered} (open-colour) Koszul dual
chapters/connections/line-operators.tex-16-$\cA^!_{\mathrm{line}}$, and their composition is governed by
chapters/connections/line-operators.tex-17-the deconcatenation coproduct on the ordered bar coalgebra,
chapters/connections/line-operators.tex-18-not its symmetric-coinvariant quotient.
chapters/connections/line-operators.tex-19-The spectral $R$-matrix $R(z)$ controlling line-operator OPE is
chapters/connections/line-operators.tex:20:the degree-$2$ $E_1$ MC datum; the modular characteristic
chapters/connections/line-operators.tex-21-$\kappa(\cA) = \mathrm{av}(r(z))$ is its
chapters/connections/line-operators.tex-22-$\Sigma_2$-coinvariant projection.
chapters/connections/line-operators.tex-23-See Volume~I, \S\textup{E$_1$ as primitive}
--
chapters/connections/line-operators.tex-78-\begin{proof}
chapters/connections/line-operators.tex-79-\textbf{Step 1: The classical Swiss--cheese operad is homotopy--Koszul.}

thinking
**Inspecting potential violations**

I need to take a closer look at the context surrounding potential violations in the documents. The `preface.tex` seems fine, but maybe the user is referring to all VAs being E_inf. Some files mention `pole-free E_inf-algebras`, which might be acceptable if it simply refers to a pole-free subclass. However, there could be bigger issues, like the reference to `associated graded gr_com A` suggesting it has only simple poles. That's incorrect, as E_inf doesn’t imply simple poles. I’ll search for `E_\infty` combined with terms like “simple poles” or “pole-free.”
exec
/bin/zsh -lc "sed -n '2708,2722p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2338,2390p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -C 3 -F -e 'E_\\infty' -e 'only simple poles' -e 'simple poles' -e 'pole-free' -e 'no poles' chapters/frame/preface.tex chapters/frame/preface_trimmed.tex chapters/connections/spectral-braiding-core.tex chapters/connections/bar-cobar-review.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/line-operators.tex chapters/examples/rosetta_stone.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
The $R$-matrix is the cross-colour datum:
$\Barch(\cA)_n \simeq
(\Barchord(\cA)_n)^{R\text{-}\Sigma_n}$
(Proposition~\ref{prop:r-matrix-descent}). For
$E_\infty$-chiral algebras (commutative chiral algebras)
whose OPE is pole-free, $R(z) = \tau$ and both
projections carry equivalent information. For
$E_\infty$-chiral algebras with OPE poles
(all interesting vertex algebras: affine Kac--Moody,
Virasoro, Heisenberg),
$R(z)$ carries nontrivial spectral dependence
(derived from the local OPE via analytic
continuation), and $\cA^!_{\mathrm{line}}$ carries
strictly more structure than $\cA^!_{\mathrm{ch}}$:
the spectral parameter~$u$ is the fingerprint of the
 succeeded in 51ms:
of zeroth products (Lie brackets).

The $R$-matrix intertwines the two orderings:
\[
R(z)\colon
{\Barch}_2^{\mathrm{ord}}(a\otimes b;\,z_1,z_2)
\;\xrightarrow{\;\sim\;}
{\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
\]
For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
and unordered complexes are identified. For $E_\infty$-algebras
with OPE poles, $R(z)\ne\tau$ but is derived from the local OPE.
For genuine $E_1$-algebras, $R(z)$ carries nontrivial spectral
dependence as independent input and is the fundamental new datum.
\end{construction}

\begin{proposition}[Descent identification;
\ClaimStatusProvedHere]
\label{prop:r-matrix-descent}
\index{descent!R-matrix!ordered to unordered}
 succeeded in 52ms:
chapters/connections/line-operators.tex-598-The forgetful functor from factorization modules~(ii)
chapters/connections/line-operators.tex-599-to fibers~(i) forgets the flat spectral connection. The
chapters/connections/line-operators.tex-600-$R$-matrix is the holonomy datum that reconstructs the family
chapters/connections/line-operators.tex:601:from its fibers. Within the $E_\infty$-chiral class, the
chapters/connections/line-operators.tex:602:pole-free commutative algebras have $R(z) = \tau$: the flat
chapters/connections/line-operators.tex-603-connection is trivial and the two module categories collapse.
chapters/connections/line-operators.tex:604:For $E_\infty$-chiral algebras with OPE poles (vertex
chapters/connections/line-operators.tex-605-algebras such as $\widehat{\fg}_k$ or $\mathrm{Vir}_c$),
chapters/connections/line-operators.tex-606-$R(z) \neq \tau$ but is derived from the local OPE, so the
chapters/connections/line-operators.tex-607-two categories are related by an explicit twist. For genuine
chapters/connections/line-operators.tex-608-$E_1$-chiral algebras, the $R$-matrix is independent input
chapters/connections/line-operators.tex-609-the nontrivial datum distinguishing the two categories.
chapters/connections/line-operators.tex-610-This is why the spectral parameter and quantum group structure
chapters/connections/line-operators.tex:611:are invisible in the pole-free commutative limit and
chapters/connections/line-operators.tex-612-progressively more visible as one moves through the three
chapters/connections/line-operators.tex-613-tiers.
chapters/connections/line-operators.tex-614-\end{remark}
--
chapters/examples/rosetta_stone.tex-1907-\index{algebraic hierarchy!five levels}
chapters/examples/rosetta_stone.tex-1908-The five levels are:
exec
/bin/zsh -lc "rg -n -F 'E_\\infty"'$-chiral algebras (commutative chiral algebras)'"' chapters working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'E_\\infty"'$-chiral algebras (all vertex algebras)'"' -e 'all vertex algebras' chapters working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'E_\\infty"'$-chiral,'"' -e 'E_\\infty"'$ with poles'"' -e 'pole-free "'$E_'"\\infty"'$'"' -e 'E_\\infty"'$-algebras with OPE poles'"' -e 'E_\\infty"'$-algebras, $R(z)=1$'"' chapters working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/ordered_associative_chiral_kd.tex:1893:$E_\infty$-chiral algebras (commutative chiral algebras),
chapters/connections/ordered_associative_chiral_kd_core.tex:1998:$E_\infty$-chiral algebras (commutative chiral algebras),
chapters/connections/ordered_associative_chiral_kd_core.tex:2712:$E_\infty$-chiral algebras (commutative chiral algebras)
 succeeded in 51ms:
working_notes.tex:15919:since all vertex algebras are $E_\infty$-chiral):
chapters/frame/preface.tex:507:$E_\infty$-chiral algebras (all vertex algebras), the $R$-matrix is
chapters/examples/rosetta_stone.tex:1921:\item $\Einf$-chiral: all vertex algebras with local OPE.
 succeeded in 50ms:
working_notes.tex:3046:\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
working_notes.tex:15913:For pole-free $E_\infty$-chiral algebras (the
working_notes.tex:15978:When $\cA$ is pole-free $E_\infty$-chiral (the
chapters/connections/ordered_associative_chiral_kd.tex:2047:For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
chapters/connections/ordered_associative_chiral_kd_core.tex:2347:For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
chapters/connections/ordered_associative_chiral_kd_core.tex:2377:For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
chapters/connections/ordered_associative_chiral_kd_core.tex:2379:$E_\infty$-algebras with OPE poles, the descent is
chapters/connections/ordered_associative_chiral_kd_frontier.tex:111:For the associated graded $\gr_{\mathrm{com}}A$ (which is $E_\infty$-chiral,
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3750:of the three-tier picture ($E_\infty$ with poles, $R$-matrix
codex
I’ve isolated a real class of violations now: places where `E_\infty` is being identified with the pole-free or simple-pole subclass, not just compared against it. I’m reading those exact blocks in the active chapter and its superseded split file before patching.
exec
/bin/zsh -lc "sed -n '100,116p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1884,1902p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1988,2010p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\begin{remark}[Ordered vs.\ unordered]
% label removed: rem:ordered-vs-unordered
\index{bar complex!ordered vs unordered}
The unordered bar complex
$\Barch(\cA)={\Barch}^{\mathrm{ord}}(\cA)_{\Sigma_n}$
is the $\Sigma_n$-coinvariants of the ordered complex.
The comparison map
${\Barch}^{\mathrm{ord}}(\cA)\to\Barch(\cA)$
is the quotient by the symmetric group action. For
$E_\infty$-chiral algebras (commutative chiral algebras),
the two are equivalent. For genuinely $E_1$-chiral
algebras (Yangians, quantum groups), the ordered complex
carries strictly more information: the $R$-matrix is the
data needed to descend from ordered to unordered.
\end{remark}

\subsection{The $R$-matrix as ordered-to-unordered descent}
% label removed: subsec:r-matrix-monodromy

 succeeded in 52ms:

\begin{remark}[Ordered vs.\ unordered]
\label{rem:ordered-vs-unordered}
\index{bar complex!ordered vs unordered}
The unordered bar complex
$\Barch(\cA)=\Barchord(\cA)_{\Sigma_n}$
is the $\Sigma_n$-coinvariants of the ordered complex.
The comparison map
$\Barchord(\cA)\to\Barch(\cA)$
is the quotient by the symmetric group action. For
$E_\infty$-chiral algebras (commutative chiral algebras),
the two are equivalent. For genuinely $E_1$-chiral
algebras (Yangians, quantum groups), the ordered complex
carries strictly more information: the $R$-matrix is the
data needed to descend from ordered to unordered.

Geometrically, the descent datum is non-trivial because
$\mathrm{Conf}_n^{\mathrm{ord}}(\mathbb R)$ is discrete:
its connected components are the $n!$~chambers cut out by
the total order, while
 succeeded in 52ms:
S_p
\;:=\;
\bigl\{
(z_1,\dotsc,z_k;\,t_1<\cdots<t_k)
\in \FM_k(\mathbb{C})\times\Conf_k(\mathbb{R})
\;\big|\;
\text{commutator depth of the zeroth-product tree} \le p
\bigr\}.
\]
Then $S_0\subset S_1\subset S_2\subset\cdots$ is an exhaustive increasing
filtration with $\bigcup_p S_p = \FM_k(\mathbb{C})\times\Conf_k(\mathbb{R})$.
For the associated graded $\gr_{\mathrm{com}}A$ (which is $E_\infty$-chiral,
i.e.\ has only simple poles), only the stratum $S_1$ contributes to the bar
differential: all OPE singularities are at worst first-order.
\end{construction}

\begin{proposition}[\ClaimStatusProvedHere]
exec
/bin/zsh -lc "sed -n '2038,2052p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '15910,15922p' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1636,1646p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\bigl({\Barch}^{\mathrm{ord}}(\cA)_n\bigr)^{R\text{-}\Sigma_n},
\end{equation}
where $\Sigma_n$ acts by $\sigma_i\cdot(a_1\otimes\cdots\otimes a_n)
=(\tau_{i,i+1}\circ R_{i,i+1}(z_i{-}z_{i+1}))\,
(a_1\otimes\cdots\otimes a_n)$
on the adjacent transposition $(i,\,i{+}1)$. The
$\Sigma_n$-action is well-defined if and only if the
$R$-matrix satisfies the Yang--Baxter
equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
ordinary $\Sigma_n$-coinvariants.
\end{proposition}

\begin{proof}
The covering $\pi_n$ presents $\mathrm{Conf}_n(X)$ as the
 succeeded in 51ms:
The descent from ordered to unordered is $R$-twisted:
$B^{\mathrm{ch}}(\cA)_n \simeq
(\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
For pole-free $E_\infty$-chiral algebras (the
BD-commutative subclass: no OPE singularities):
$R(z) = \tau$ (the flip), descent is trivial, both
duals carry equivalent information.  For
$E_\infty$-chiral algebras with OPE poles
(Heisenberg, affine KM, Virasoro --- still $E_\infty$,
since all vertex algebras are $E_\infty$-chiral):
$R(z) \neq \tau$ (derived from the local OPE via
analytic continuation), and $\cA^!_{\mathrm{line}}$
carries strictly more structure than
 succeeded in 51ms:
\item \emph{Ordered-to-symmetric descent.} Taking
 $\Sigma_n$-coinvariants gives a map
 $\barB^{\mathrm{ord}}(\cA) \to \barBch(\cA)$, but for
 $E_\infty$-chiral algebras with OPE poles (all interesting
 vertex algebras), this descent is $R$-matrix twisted:
 $\barBch(\cA)_n \simeq
 (\barB^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$
 (Proposition~\ref{prop:r-matrix-descent}). For the pole-free
 subclass, $R(z) = \tau$ and the descent is the naive
 $\Sigma_n$-quotient.


thinking
**Searching picture files**

I’m looking into the “three-tier picture” in my active files. I think there might be proper language in the preface. I’ll need to search for terms like "pole-free" and "E_inf with poles" to get more details about the tiers. It's a bit tricky, but I want to ensure I have all the right information before proceeding! Let’s keep the focus sharp!
exec
/bin/zsh -lc "sed -n '3038,3050p' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'Tier~(ii) ("'$E_'"\\infty"'$ with poles'"' -e '"'$E_'"\\infty"'$ with poles'"' -e 'Factorisation type & "'$E_'"\\infty"'$ (local)'"' -e 'three-tier picture' chapters working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'which is "'$E_'"\\infty"'$-chiral,'"' -e 'i.e.\\ has only simple poles' -e 'For "'$E_'"\\infty"'$-algebras, $R(z)=1$'"' -e 'For "'$E_'"\\infty"'$-chiral algebras (commutative chiral algebras)'"' chapters working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\cdot\,)$ is a positive functional (the Haar state), and the
GNS Hilbert space is the state space on
$S^1 \times D^2$.

The three-tier picture (AP51) maps precisely:
\begin{itemize}[nosep]
\item Tier~(i) (pole-free): forgetful functor to
  $\mathrm{Vect}$, commutative Hopf algebra.
\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
  exists, compact quantum group.
\item Tier~(iii) (class~M): \textbf{no} fibre functor to
  $\mathrm{Hilb}$ can make the braiding unitary---the
  $A_\infty$ tower prevents it
 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd_frontier.tex:111:For the associated graded $\gr_{\mathrm{com}}A$ (which is $E_\infty$-chiral,
chapters/connections/ordered_associative_chiral_kd_frontier.tex:112:i.e.\ has only simple poles), only the stratum $S_1$ contributes to the bar
chapters/connections/ordered_associative_chiral_kd.tex:2047:For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
 succeeded in 51ms:
working_notes.tex:3042:The three-tier picture (AP51) maps precisely:
working_notes.tex:3046:\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
chapters/examples/rosetta_stone.tex:1208:three-tier picture
chapters/connections/spectral-braiding-core.tex:510:(cf.\ the three-tier picture of
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3703:Factorisation type & $E_\infty$ (local)
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3750:of the three-tier picture ($E_\infty$ with poles, $R$-matrix

thinking
**Searching for Rosetta file**

I’m considering searching for a three-tier picture with active files related to Rosetta, possibly 1208. I want to inspect the surroundings of this Rosetta reference. It seems like a specific task, and I'll need to explore that area thoroughly. I wonder if there are any related documents or images that can give me more context. It should help me understand what I’m looking for better!
exec
/bin/zsh -lc "sed -n '1198,1224p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '500,514p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3698,3754p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
and the monodromy is $\exp(-2\pi i k)$.
The spectral $R$-matrix on modules is
\begin{equation}\label{eq:heisenberg-hydrogen-R}
R(z) \;=\; e^{k\hbar/z},
\end{equation}
confirming
Corollary~\ref{cor:rosetta-heisenberg-projections}(iii).
The Yang--Baxter equation is trivially satisfied
($R$ is scalar). The braiding is nontrivial
but derived from the local OPE: tier~(ii) of the
three-tier picture
(Section~\ref{subsec:ordered-three-tier}).

\smallskip
\noindent
\emph{Genus-$1$ $r$-matrix.}
On $E_\tau$, the rational propagator $1/z$ is replaced by
$\zeta(z|\tau)$. Since $c_0 = J_{(0)}J = 0$
(no simple pole), the quasi-periodic part of
$\zeta(z|\tau)$ drops out of the $r$-matrix:
 succeeded in 52ms:
dependence is genuine and the $E_2$-chiral algebra cannot be
promoted to $E_2$-topological.
\end{definition}

\begin{remark}[The $E_1$-to-$E_2$ step and the locus of the $E_2$ structure]
\label{rem:E1-to-E2-locus}
\index{E2 structure@$E_2$ structure!locus}
The passage from $E_1$ to $E_2$ requires the $R$-matrix $R(z)$ as
coherence datum.  For $E_\infty$-chiral algebras (vertex algebras),
the $R$-matrix is canonical: it is determined by the local OPE data
(cf.\ the three-tier picture of
Section~\textup{\ref{sec:bulk-boundary-R}}).
For genuinely $E_1$-chiral algebras, $R(z)$ is independent
structure, not derivable from local data.

 succeeded in 51ms:
 & $q$-\emph{stable} \\
$m_4$ & $0$ & $0$
 & $q$-\emph{stable} \\
Poincar\'{e} series & $1 + 3t$ & $1 + 3t$
 & $q$-\emph{stable} \\
Factorisation type & $E_\infty$ (local)
 & $E_1$ (nonlocal)
 & \textbf{changes} \\
$m_2(E^+,E^-)$ & $\alpha\cdot J$ (Lie bracket)
 & $[K^+,K^-]_q$ (braided)
 & \textbf{changes} \\
Collision residue & $\Omega/\zeta$ (one pole)
 & $r_q(\zeta)$ (three poles)
 & \textbf{changes} \\
$R$-matrix type & rational ($1 + \Omega/u$)
 & trigonometric~\eqref{eq:qlattice-R}
 & \textbf{changes} \\
$R$-matrix provenance & derived from OPE (tier~(ii))
 & independent input (tier~(iii))
 & \textbf{changes} \\




thinking
**Searching for classifications**

I'm considering the Frontier 3750 "E_infty with poles" compared to E1. I realize the current notes are misleading because the class M omitted E_inf. I might want to search active files for "three-tier picture" to see if there's a classification error. I'll look into `preface.tex` or core files and check sections around `ordered_associative_chiral_kd_core`. The user is specifically searching for `'E_inf'` near 'no poles' or 'not E_inf' near 'vertex algebra', so I’ll focus on those sections.
thinking
**Identifying necessary patches**

I need to patch some inconsistencies. For instance, the `ordered_associative_chiral_kd_core.tex` claims that E_inf-chiral algebras are equivalent to commutative or pole-free types. Meanwhile, frontier lines show E_inf with simple poles. The working notes suggest that only class L has E_inf poles, which indicates a potential issue. However, the frontier mistakenly states that poles at ζ=0 and ±hbar are absent in all E_inf-chiral examples, while local vertex algebras can have these poles. So overall, I think I'm figuring out what's okay and what needs fixing!
thinking
**Searching for OPE singularities**

I think I need to search for "no OPE singularities" in the context of E∞ and inspect it closely. Some phrasing about explicit subclasses might be acceptable, but I want to ensure I meet the user's expectations. They might be looking for something exhaustive and minimal, so I should clarify what that means. I want to make sure I'm delivering precisely what the user is looking for without any extra fluff or confusion.
thinking
**Clarifying edits and formatting**

I'm thinking about how to add clarity to all those suspicious spots. I need to determine the exact edits that were applied and ensure the final report reflects those changes. It seems like I should audit the ledger entry for accuracy, and perhaps inspect the format to make sure everything aligns correctly. I might also consider using the tail command to assist with this.
codex
I’ve reduced the patch set to the actual false claims, not every mention of poles. The live violations are: `E_\infty = commutative/pole-free`, `E_\infty = simple-pole`, and one tier summary that drops class `M` vertex algebras out of `E_\infty`.
exec
/bin/zsh -lc 'tail -n 80 compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1916,1926p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '15972,15988p' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\item $\PVA$: Poisson vertex algebras. A PVA carries a
 $\lambda$-bracket on cohomology (the classical shadow) but
 no quantum corrections; it is the semiclassical limit of a
 vertex algebra.

\item $\Einf$-chiral: all vertex algebras with local OPE.
 This is the standard setting of Beilinson--Drinfeld~\cite{BD04}
 and Frenkel--Ben-Zvi~\cite{FBZ04}. Every standard vertex
 algebra (Heisenberg, affine Kac--Moody, Virasoro,
 $\mathcal{W}$-algebras, lattice VOAs, $\beta\gamma$,
 $bc_\lambda$, free fermions) belongs to this level: the OPE
 succeeded in 51ms:
The stratification spectral sequence ($E_1$ page $=$ FG bar
complex, convergence proved) provides the controlled
interpolation.  The filtration compatibility of the bar
differential remains the sole gap.

\medskip\noindent\textbf{When do the two duals agree?}\enspace
When $\cA$ is pole-free $E_\infty$-chiral (the
BD-commutative subclass): $R(z) = \tau$, descent is
trivial, both duals carry equivalent information.

\noindent\textbf{When do they disagree?}\enspace
When $\cA$ is $E_\infty$-chiral with OPE poles (all
interesting vertex algebras: Heisenberg, affine KM,
Virasoro --- these are still $E_\infty$, since all
vertex algebras are $E_\infty$-chiral): $R(z)$
carries nontrivial spectral dependence derived from
the local OPE, and $\cA^!_{\mathrm{line}}$ (the
 succeeded in 52ms:
640. `2026-04-13-640`
   Severity: `MODERATE`
   Class: `W/D`
   Location: `AGENTS.md:612`, `AGENTS.md:769`, `CLAUDE.md:215`, `chapters/theory/introduction.tex:1572`, `compute/audit/linear_read_notes.md:99`
   Issue: the repo prescribes a zero-tolerance grep for the rectification-debt marker, but these files themselves still contain the literal token. This poisons the enforcement surface: a naive repo-wide grep reports debt even when no unresolved marker remains in the manuscript.
   Fix: either (a) reword these lines to avoid the literal token after resolution and in policy prose, or (b) standardize the enforcement command to scope the grep to the live manuscript/program surface (`chapters`, `compute/lib`, `compute/tests`, `standalone`, `scripts`, `main.tex`) and keep governance/audit files out of the zero-tolerance query.
   Status: `OPEN`

641. `2026-04-13-641`
   Severity: `MODERATE`
   Class: `P/C`
   Location: `chapters/connections/conclusion.tex:1036-1107`
   Issue: the frontier-status table had drifted from the live theorem surface. The free-PVA `\Ethree` case was missing; the general `\Ethree` row still read as unrestricted rather than narrowed beyond the free-PVA case; the curved-Dunn row omitted the three-level refinement; the modular-operad row did not make the genus split explicit; the chiral-coproduct row omitted the folding route; and the global-triangle row lagged the active `G/L/C` theorem versus class-`M` gap split.
   Fix: retitled the subsection to a neutral frontier heading, inserted the missing free-PVA row, narrowed the general `\Ethree` row, updated the curved-Dunn/modular-operad/chiral-coproduct/global-triangle statuses to match the active labels, and confirmed that all ten Part VII frontier chapter references listed in `conclusion.tex` resolve to active chapter files in `main.tex`.
   Status: `FIXED`

## 2026-04-13 - Chapter-Wide Slop Removal Audit

### Summary

exec
/bin/zsh -lc "rg -n -F -e 'E_\\infty' -e 'pole-free' -e 'commutative chiral algebras' -e 'simple poles' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'E_\\infty' -e 'pole-free' -e 'simple poles' working_notes.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'E_\\infty' -e 'pole-free' -e 'commutative chiral algebras' -e 'simple poles' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
398:The theorem is genuinely associative. In a commutative or $E_\infty$ setting many of the shuffle
1303:\begin{remark}[$E_1$ vs $E_\infty$]
1305:\index{five main theorems!E1 vs E-infty comparison@$E_1$ vs $E_\infty$ comparison}
1310:& \emph{$E_\infty$} & \emph{$E_1$} \\
1330:The $E_\infty$ theorem is the $\Sigma_n$-coinvariant of the $E_1$ theorem.
1344:\item $\gr_{\mathrm{com}}A$ is $E_\infty$-chiral;
1729:An $E_\infty$-algebra (commutative chiral algebra) has
1877:$E_1$ axiom. (For commutative chiral algebras, the
1893:$E_\infty$-chiral algebras (commutative chiral algebras),
1951:For an $E_\infty$-chiral algebra, the equivariant structure
2021:For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
2047:For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
 succeeded in 51ms:
431:The theorem is genuinely associative. In a commutative or $E_\infty$ setting many of the shuffle
1274:Volume~I establishes five main theorems for $E_\infty$-chiral algebras: bar-cobar adjunction, Koszul inversion, complementarity, leading coefficient, and the Hochschild ring. Each has an $E_1$-chiral counterpart, obtained by replacing symmetric coinvariants with the ordered bar complex and its braid-group equivariance. The five $E_1$ theorems at genus zero are formal consequences of the master theorem (Theorem~\ref{thm:master}) together with the explicit constructions of Appendix~\ref{sec:ordered-bar-explicit}; they are collected here to make the parallel with Vol~I explicit.
1361:\begin{remark}[$E_1$ vs $E_\infty$]
1363:\index{five main theorems!E1 vs E-infty comparison@$E_1$ vs $E_\infty$ comparison}
1368:& \emph{$E_\infty$} & \emph{$E_1$} \\
1388:The $E_\infty$ theorem is the $\Sigma_n$-coinvariant of the $E_1$ theorem.
1589:An $E_\infty$-algebra (commutative chiral algebra) has
1737:$E_1$ axiom. (For commutative chiral algebras, the
1939:and the Arnold relation. For $E_\infty$-chiral algebras
1970:$E_\infty$-chiral (it is a local vertex algebra), so its
1998:$E_\infty$-chiral algebras (commutative chiral algebras),
2151:\begin{computation}[$E_1$ vs $E_\infty$ dimension surplus;
2277:For an $E_\infty$-chiral algebra, the equivariant structure
2347:For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
2348:and unordered complexes are identified. For $E_\infty$-algebras
2377:For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
2379:$E_\infty$-algebras with OPE poles, the descent is
2405:for $E_\infty$-chiral algebras (including those with OPE
2636:The $R$-matrix governs descent from ordered to unordered; the Yang--Baxter equation is $d^2=0$. The $E_\infty$-chiral Koszul dual $\cA^!_{\mathrm{ch}}$ is another chiral algebra on the same curve. The ordered ($E_1$) Koszul dual is an associative algebra with spectral parameter, living on the affine line of spectral parameters rather than on the curve. For affine Kac--Moody input, this algebra is the Yangian.
2712:$E_\infty$-chiral algebras (commutative chiral algebras)
 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd_frontier.tex:50:\item $\gr_{\mathrm{com}}A$ is $E_\infty$-chiral;
chapters/connections/ordered_associative_chiral_kd_frontier.tex:111:For the associated graded $\gr_{\mathrm{com}}A$ (which is $E_\infty$-chiral,
chapters/connections/ordered_associative_chiral_kd_frontier.tex:112:i.e.\ has only simple poles), only the stratum $S_1$ contributes to the bar
chapters/connections/ordered_associative_chiral_kd_frontier.tex:588:unordered within each cluster (the $E_\infty$ or holomorphic
chapters/connections/ordered_associative_chiral_kd_frontier.tex:2974:OPEs are simple poles ($\pm G^\pm$, no $\lambda$-dependence).
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3288:The preceding examples are all $E_\infty$-chiral (local vertex
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3354:the simple poles.
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3458:$E_\infty$-chiral examples: poles at $\zeta = 0$ \emph{and}
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3488:two simple poles separated by $2\hbar$: their Laurent
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3535:$\zeta = 0$) & $\kappa_q$: two simple poles at
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3703:Factorisation type & $E_\infty$ (local)
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3744:The instability of the factorisation type ($E_\infty \to E_1$)
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3750:of the three-tier picture ($E_\infty$ with poles, $R$-matrix
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3798:$E_\infty$-chiral algebras:
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3812: the $E_\infty$ setting.
chapters/connections/ordered_associative_chiral_kd_frontier.tex:5469:with simple poles (the structure constants of
chapters/connections/ordered_associative_chiral_kd_frontier.tex:5873:The $E_\infty$-chiral remarks of the core chapter
chapters/connections/ordered_associative_chiral_kd_frontier.tex:5956:descent. The $E_\infty$-chiral analogue, where the product
chapters/connections/ordered_associative_chiral_kd_frontier.tex:6110:the $E_\infty$ side (BD \cite{BD04}) but not developed
chapters/connections/ordered_associative_chiral_kd_frontier.tex:6144:to an $E_\infty$-chiral analogue by $\Sigma_n$-coinvariants.
exec
/bin/zsh -lc "sed -n '1582,1594p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1724,1734p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
 ordered bar differential.
\end{enumerate}
\end{proposition}

\begin{remark}[Why ordered spaces for $E_1$-algebras]
\label{rem:why-ordered}
\index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
An $E_\infty$-algebra (commutative chiral algebra) has
$\Sigma_n$-equivariant operations, so its bar complex
uses the unordered space $\mathrm{Conf}_n(X)$.
An $E_1$-algebra (associative chiral algebra) has
operations indexed by \emph{ordered} compositions, so its
bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
exec
/bin/zsh -lc "sed -n '1584,1594p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\end{proposition}

\begin{remark}[Why ordered spaces for $E_1$-algebras]
% label removed: rem:why-ordered
\index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
An $E_\infty$-algebra (commutative chiral algebra) has
$\Sigma_n$-equivariant operations, so its bar complex
uses the unordered space $\mathrm{Conf}_n(X)$.
An $E_1$-algebra (associative chiral algebra) has
operations indexed by \emph{ordered} compositions, so its
bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
 succeeded in 51ms:
% label removed: sec:integration

For direct integration into a research repository, the following replacements are recommended.

\begin{enumerate}[label=(\arabic*)]
\item Replace the abstract hypotheses in \S\ref{sec:setup} by the precise labels of the repository's
existing bar--cobar and module/comodule theorems.

\item Replace the shorthand notation $\widehat\otimes$ and $\chotimes$ by the repository's preferred
completed tensor notation and chiral monoidal symbol.

exec
/bin/zsh -lc "sed -n '2016,2028p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2038,2050p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3038,3049p' working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
R(z)\colon
{\Barch}_2^{\mathrm{ord}}(a\otimes b;\,z_1,z_2)
\;\xrightarrow{\;\sim\;}
{\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
\]
For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
and unordered complexes are identified. For genuine
$E_1$-algebras, $R(z)$ carries nontrivial spectral dependence
and is the fundamental new datum.
\end{construction}

\begin{proposition}[Descent identification;
\ClaimStatusProvedHere]
 succeeded in 51ms:
\bigl({\Barch}^{\mathrm{ord}}(\cA)_n\bigr)^{R\text{-}\Sigma_n},
\end{equation}
where $\Sigma_n$ acts by $\sigma_i\cdot(a_1\otimes\cdots\otimes a_n)
=(\tau_{i,i+1}\circ R_{i,i+1}(z_i{-}z_{i+1}))\,
(a_1\otimes\cdots\otimes a_n)$
on the adjacent transposition $(i,\,i{+}1)$. The
$\Sigma_n$-action is well-defined if and only if the
$R$-matrix satisfies the Yang--Baxter
equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
ordinary $\Sigma_n$-coinvariants.
\end{proposition}

 succeeded in 52ms:
\cdot\,)$ is a positive functional (the Haar state), and the
GNS Hilbert space is the state space on
$S^1 \times D^2$.

The three-tier picture (AP51) maps precisely:
\begin{itemize}[nosep]
\item Tier~(i) (pole-free): forgetful functor to
  $\mathrm{Vect}$, commutative Hopf algebra.
\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
  exists, compact quantum group.
\item Tier~(iii) (class~M): \textbf{no} fibre functor to
  $\mathrm{Hilb}$ can make the braiding unitary---the

thinking
**Searching for AP51 discrepancies**

I need to search the active file for the AP51 three-tier picture. I want to find the same incorrect statement. I’ll try searching for “AP51” or maybe “Tier(ii)” to locate that specific info. It seems like digging into those keywords will help me pinpoint any errors in the document or resources. Let's see what I can uncover!
exec
/bin/zsh -lc "rg -n -F -e 'Tier~(ii)' -e 'AP51' -e 'three-tier picture' chapters README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'For "'$E_'"\\infty"'$-algebras, $R(z)='"\\tau"'$'"' -e 'For "'$E_'"\\infty"'$-algebras, $R(z)=1$'"' -e 'For pole-free "'$E_'"\\infty"'$-algebras'"' chapters README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F -e 'An "'$E_'"\\infty"'$-algebra (commutative chiral algebra)'"' -e '"'$E_'"\\infty"'$-chiral algebras (commutative chiral algebras),'"' -e '"'$E_'"\\infty"'$-chiral algebras (commutative chiral algebras)'"' chapters README.md working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/examples/rosetta_stone.tex:1208:three-tier picture
chapters/connections/spectral-braiding-core.tex:510:(cf.\ the three-tier picture of
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3750:of the three-tier picture ($E_\infty$ with poles, $R$-matrix
 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd.tex:1729:An $E_\infty$-algebra (commutative chiral algebra) has
chapters/connections/ordered_associative_chiral_kd.tex:1893:$E_\infty$-chiral algebras (commutative chiral algebras),
chapters/connections/ordered_associative_chiral_kd_core.tex:1589:An $E_\infty$-algebra (commutative chiral algebra) has
chapters/connections/ordered_associative_chiral_kd_core.tex:1998:$E_\infty$-chiral algebras (commutative chiral algebras),
chapters/connections/ordered_associative_chiral_kd_core.tex:2712:$E_\infty$-chiral algebras (commutative chiral algebras)
 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd.tex:2021:For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
chapters/connections/ordered_associative_chiral_kd.tex:2047:For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
chapters/connections/ordered_associative_chiral_kd_core.tex:2347:For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
chapters/connections/ordered_associative_chiral_kd_core.tex:2377:For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
exec
/bin/zsh -lc "sed -n '1188,1220p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

\smallskip
\noindent
\emph{$R$-matrix.}
The collision residue is $r^{\mathrm{coll}}(z) = k/z$
(the $d\log$ kernel absorbs one power from the
double-pole OPE: $k/(z-w)^2 \cdot d\log(z-w)
\leadsto k/z$).
The connection on $\Conf_2^{\mathrm{ord}}(\C)$ is
$\nabla = d - k \cdot d\log(z)$,
and the monodromy is $\exp(-2\pi i k)$.
The spectral $R$-matrix on modules is
\begin{equation}\label{eq:heisenberg-hydrogen-R}
R(z) \;=\; e^{k\hbar/z},
\end{equation}
confirming
Corollary~\ref{cor:rosetta-heisenberg-projections}(iii).
The Yang--Baxter equation is trivially satisfied
($R$ is scalar). The braiding is nontrivial
but derived from the local OPE: tier~(ii) of the
codex
I’m about to edit the live chapter, its superseded split file, and the local notes surface. The patch will do three things only: remove `E_\infty = commutative/pole-free`, remove `E_\infty = simple-pole`, and rewrite the one tier summary that was excluding class `M` vertex algebras from the local `E_\infty` regime.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1728,5 +1728,6 @@
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
@@ -1892,4 +1893,7 @@
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
@@ -2020,3 +2024,4 @@
 \]
-For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
 and unordered complexes are identified. For genuine
@@ -2046,3 +2051,4 @@
 equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
-For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent reduces to
 ordinary $\Sigma_n$-coinvariants.
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -110,4 +110,5 @@
 filtration with $\bigcup_p S_p = \FM_k(\mathbb{C})\times\Conf_k(\mathbb{R})$.
-For the associated graded $\gr_{\mathrm{com}}A$ (which is $E_\infty$-chiral,
-i.e.\ has only simple poles), only the stratum $S_1$ contributes to the bar
+For the associated graded $\gr_{\mathrm{com}}A$ (which remains
+$E_\infty$-chiral and, by construction of the commutator filtration,
+has only first-order OPE singularities), only the stratum $S_1$ contributes to the bar
 differential: all OPE singularities are at worst first-order.
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -14424 +14424,17 @@
    Status: `FIXED`
+
+648. `2026-04-13-648`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:1589-1593`, `chapters/connections/ordered_associative_chiral_kd_core.tex:1998-2005`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2347-2350`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2377-2380`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2712-2718`, `chapters/connections/ordered_associative_chiral_kd.tex:1729-1733`, `chapters/connections/ordered_associative_chiral_kd.tex:1893-1900`, `chapters/connections/ordered_associative_chiral_kd.tex:2021-2024`, `chapters/connections/ordered_associative_chiral_kd.tex:2047-2049`
+   Issue: these ordered/unordered comparison passages identified `$E_\infty$` with the pole-free commutative subclass, which contradicts the repo convention that all local vertex algebras remain `$E_\infty$` even when OPE poles are present.
+   Fix: rewrote the affected sentences to distinguish the pole-free BD-commutative subclass from general `$E_\infty$`-chiral vertex algebras with OPE poles, and kept the genuinely `$E_1$` case reserved for independent `$R$`-matrix input.
+   Status: `FIXED`
+
+649. `2026-04-13-649`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:111-113`, `working_notes.tex:3044-3048`, `working_notes.tex:15913-15919`, `working_notes.tex:15978-15986`
+   Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
+   Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
+   Status: `FIXED`
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -1588,5 +1588,6 @@
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
@@ -1997,4 +1998,7 @@
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
@@ -2346,5 +2350,7 @@
 \]
-For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
-and unordered complexes are identified. For $E_\infty$-algebras
-with OPE poles, $R(z)\ne\tau$ but is derived from the local OPE.
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
+and unordered complexes are identified. For local
+vertex algebras in the $E_\infty$ regime with OPE poles,
+$R(z)\ne\tau$ but is derived from the local OPE.
 For genuine $E_1$-algebras, $R(z)$ carries nontrivial spectral
@@ -2376,5 +2382,6 @@
 $R_{12}(z)\,R_{21}(-z)=\id$.
-For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
-reduces to ordinary $\Sigma_n$-coinvariants; for
-$E_\infty$-algebras with OPE poles, the descent is
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent
+reduces to ordinary $\Sigma_n$-coinvariants; for local
+vertex algebras in the $E_\infty$ regime with OPE poles, the descent is
 $R$-twisted (nontrivially, though $R(z)$ is derived from
@@ -2711,4 +2718,4 @@
 (Proposition~\ref{prop:r-matrix-descent}). For
-$E_\infty$-chiral algebras (commutative chiral algebras)
-whose OPE is pole-free, $R(z) = \tau$ and both
+the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z) = \tau$ and both
 projections carry equivalent information. For
M /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex
@@ -3043,7 +3043,7 @@
 \begin{itemize}[nosep]
-\item Tier~(i) (pole-free): forgetful functor to
+\item Tier~(i) (pole-free BD-commutative $E_\infty$ subclass): forgetful functor to
   $\mathrm{Vect}$, commutative Hopf algebra.
-\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
+\item Tier~(ii) (local $E_\infty$ with OPE poles, class~L): $\omega_{\mathrm{BPZ}}$
   exists, compact quantum group.
-\item Tier~(iii) (class~M): \textbf{no} fibre functor to
+\item Tier~(iii) (still local $E_\infty$, class~M): \textbf{no} fibre functor to
   $\mathrm{Hilb}$ can make the braiding unitary---the
@@ -15912,4 +15912,4 @@
 (\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
-For pole-free $E_\infty$-chiral algebras (the
-BD-commutative subclass: no OPE singularities):
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras (no OPE singularities):
 $R(z) = \tau$ (the flip), descent is trivial, both
@@ -15977,4 +15977,4 @@
 \medskip\noindent\textbf{When do the two duals agree?}\enspace
-When $\cA$ is pole-free $E_\infty$-chiral (the
-BD-commutative subclass): $R(z) = \tau$, descent is
+When $\cA$ lies in the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras: $R(z) = \tau$, descent is
 trivial, both duals carry equivalent information.
apply_patch(auto_approved=true) exited 0 in 59ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
M /Users/raeez/chiral-bar-cobar-vol2/working_notes.tex
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 40fe4da0989385b75cd4642d4b1a2eab94133f84..9228dbe201ab55af25fa03100b0e6b698c79438e
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1726,9 +1726,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 % label removed: rem:why-ordered
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1890,8 +1891,11 @@
 The comparison map
 ${\Barch}^{\mathrm{ord}}(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2018,7 +2022,8 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
 and unordered complexes are identified. For genuine
 $E_1$-algebras, $R(z)$ carries nontrivial spectral dependence
 and is the fundamental new datum.
@@ -2044,7 +2049,8 @@
 $\Sigma_n$-action is well-defined if and only if the
 $R$-matrix satisfies the Yang--Baxter
 equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
-For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent reduces to
 ordinary $\Sigma_n$-coinvariants.
 \end{proposition}
 
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e..1f83cc97f58577b74f72a2b202f651aeb6a24295
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -1586,9 +1586,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 \label{rem:why-ordered}
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1995,8 +1996,11 @@
 The comparison map
 $\Barchord(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2344,9 +2348,11 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
-and unordered complexes are identified. For $E_\infty$-algebras
-with OPE poles, $R(z)\ne\tau$ but is derived from the local OPE.
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
+and unordered complexes are identified. For local
+vertex algebras in the $E_\infty$ regime with OPE poles,
+$R(z)\ne\tau$ but is derived from the local OPE.
 For genuine $E_1$-algebras, $R(z)$ carries nontrivial spectral
 dependence as independent input and is the fundamental new datum.
 \end{construction}
@@ -2374,9 +2380,10 @@
 it factors through $\Sigma_n$ if and only if~$R$
 satisfies \emph{strong unitarity}
 $R_{12}(z)\,R_{21}(-z)=\id$.
-For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
-reduces to ordinary $\Sigma_n$-coinvariants; for
-$E_\infty$-algebras with OPE poles, the descent is
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent
+reduces to ordinary $\Sigma_n$-coinvariants; for local
+vertex algebras in the $E_\infty$ regime with OPE poles, the descent is
 $R$-twisted (nontrivially, though $R(z)$ is derived from
 the local OPE).
 \end{proposition}
@@ -2709,8 +2716,8 @@
 $\Barch(\cA)_n \simeq
 (\Barchord(\cA)_n)^{R\text{-}\Sigma_n}$
 (Proposition~\ref{prop:r-matrix-descent}). For
-$E_\infty$-chiral algebras (commutative chiral algebras)
-whose OPE is pole-free, $R(z) = \tau$ and both
+the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z) = \tau$ and both
 projections carry equivalent information. For
 $E_\infty$-chiral algebras with OPE poles
 (all interesting vertex algebras: affine Kac--Moody,
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 6fce089e098fc34bcf219498799daa5ec0e5dcfe..77df257ed240cb9a38f75b9952ce20448768bd97
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -108,8 +108,9 @@
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
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 54dd69e23a585e854d9495a5039d99a6002966df..f946f54cbb93fcef4a840934cfa6eb561cabdff7
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14422,3 +14422,19 @@
    Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
    Fix: replaced each comment-line em dash `—` with ASCII `--`.
    Status: `FIXED`
+
+648. `2026-04-13-648`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:1589-1593`, `chapters/connections/ordered_associative_chiral_kd_core.tex:1998-2005`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2347-2350`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2377-2380`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2712-2718`, `chapters/connections/ordered_associative_chiral_kd.tex:1729-1733`, `chapters/connections/ordered_associative_chiral_kd.tex:1893-1900`, `chapters/connections/ordered_associative_chiral_kd.tex:2021-2024`, `chapters/connections/ordered_associative_chiral_kd.tex:2047-2049`
+   Issue: these ordered/unordered comparison passages identified `$E_\infty$` with the pole-free commutative subclass, which contradicts the repo convention that all local vertex algebras remain `$E_\infty$` even when OPE poles are present.
+   Fix: rewrote the affected sentences to distinguish the pole-free BD-commutative subclass from general `$E_\infty$`-chiral vertex algebras with OPE poles, and kept the genuinely `$E_1$` case reserved for independent `$R$`-matrix input.
+   Status: `FIXED`
+
+649. `2026-04-13-649`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:111-113`, `working_notes.tex:3044-3048`, `working_notes.tex:15913-15919`, `working_notes.tex:15978-15986`
+   Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
+   Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
+   Status: `FIXED`
diff --git a/working_notes.tex b/working_notes.tex
index f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde..bd037eaa21e69666e0e378f12f0c3fa2a45b3e04
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -3041,11 +3041,11 @@
 
 The three-tier picture (AP51) maps precisely:
 \begin{itemize}[nosep]
-\item Tier~(i) (pole-free): forgetful functor to
+\item Tier~(i) (pole-free BD-commutative $E_\infty$ subclass): forgetful functor to
   $\mathrm{Vect}$, commutative Hopf algebra.
-\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
+\item Tier~(ii) (local $E_\infty$ with OPE poles, class~L): $\omega_{\mathrm{BPZ}}$
   exists, compact quantum group.
-\item Tier~(iii) (class~M): \textbf{no} fibre functor to
+\item Tier~(iii) (still local $E_\infty$, class~M): \textbf{no} fibre functor to
   $\mathrm{Hilb}$ can make the braiding unitary---the
   $A_\infty$ tower prevents it
   (Remark~\ref{rem:virasoro-qg-unitarity}).
@@ -15910,8 +15910,8 @@
 The descent from ordered to unordered is $R$-twisted:
 $B^{\mathrm{ch}}(\cA)_n \simeq
 (\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
-For pole-free $E_\infty$-chiral algebras (the
-BD-commutative subclass: no OPE singularities):
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras (no OPE singularities):
 $R(z) = \tau$ (the flip), descent is trivial, both
 duals carry equivalent information.  For
 $E_\infty$-chiral algebras with OPE poles
@@ -15975,8 +15975,8 @@
 differential remains the sole gap.
 
 \medskip\noindent\textbf{When do the two duals agree?}\enspace
-When $\cA$ is pole-free $E_\infty$-chiral (the
-BD-commutative subclass): $R(z) = \tau$, descent is
+When $\cA$ lies in the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras: $R(z) = \tau$, descent is
 trivial, both duals carry equivalent information.
 
 \noindent\textbf{When do they disagree?}\enspace

file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 40fe4da0989385b75cd4642d4b1a2eab94133f84..9228dbe201ab55af25fa03100b0e6b698c79438e
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1726,9 +1726,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 % label removed: rem:why-ordered
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1890,8 +1891,11 @@
 The comparison map
 ${\Barch}^{\mathrm{ord}}(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2018,7 +2022,8 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
 and unordered complexes are identified. For genuine
 $E_1$-algebras, $R(z)$ carries nontrivial spectral dependence
 and is the fundamental new datum.
@@ -2044,7 +2049,8 @@
 $\Sigma_n$-action is well-defined if and only if the
 $R$-matrix satisfies the Yang--Baxter
 equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
-For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent reduces to
 ordinary $\Sigma_n$-coinvariants.
 \end{proposition}
 
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e..1f83cc97f58577b74f72a2b202f651aeb6a24295
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -1586,9 +1586,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 \label{rem:why-ordered}
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1995,8 +1996,11 @@
 The comparison map
 $\Barchord(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2344,9 +2348,11 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
-and unordered complexes are identified. For $E_\infty$-algebras
-with OPE poles, $R(z)\ne\tau$ but is derived from the local OPE.
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
+and unordered complexes are identified. For local
+vertex algebras in the $E_\infty$ regime with OPE poles,
+$R(z)\ne\tau$ but is derived from the local OPE.
 For genuine $E_1$-algebras, $R(z)$ carries nontrivial spectral
 dependence as independent input and is the fundamental new datum.
 \end{construction}
@@ -2374,9 +2380,10 @@
 it factors through $\Sigma_n$ if and only if~$R$
 satisfies \emph{strong unitarity}
 $R_{12}(z)\,R_{21}(-z)=\id$.
-For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
-reduces to ordinary $\Sigma_n$-coinvariants; for
-$E_\infty$-algebras with OPE poles, the descent is
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent
+reduces to ordinary $\Sigma_n$-coinvariants; for local
+vertex algebras in the $E_\infty$ regime with OPE poles, the descent is
 $R$-twisted (nontrivially, though $R(z)$ is derived from
 the local OPE).
 \end{proposition}
@@ -2709,8 +2716,8 @@
 $\Barch(\cA)_n \simeq
 (\Barchord(\cA)_n)^{R\text{-}\Sigma_n}$
 (Proposition~\ref{prop:r-matrix-descent}). For
-$E_\infty$-chiral algebras (commutative chiral algebras)
-whose OPE is pole-free, $R(z) = \tau$ and both
+the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z) = \tau$ and both
 projections carry equivalent information. For
 $E_\infty$-chiral algebras with OPE poles
 (all interesting vertex algebras: affine Kac--Moody,
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 6fce089e098fc34bcf219498799daa5ec0e5dcfe..77df257ed240cb9a38f75b9952ce20448768bd97
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -108,8 +108,9 @@
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
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 54dd69e23a585e854d9495a5039d99a6002966df..f946f54cbb93fcef4a840934cfa6eb561cabdff7
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14422,3 +14422,19 @@
    Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
    Fix: replaced each comment-line em dash `—` with ASCII `--`.
    Status: `FIXED`
+
+648. `2026-04-13-648`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:1589-1593`, `chapters/connections/ordered_associative_chiral_kd_core.tex:1998-2005`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2347-2350`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2377-2380`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2712-2718`, `chapters/connections/ordered_associative_chiral_kd.tex:1729-1733`, `chapters/connections/ordered_associative_chiral_kd.tex:1893-1900`, `chapters/connections/ordered_associative_chiral_kd.tex:2021-2024`, `chapters/connections/ordered_associative_chiral_kd.tex:2047-2049`
+   Issue: these ordered/unordered comparison passages identified `$E_\infty$` with the pole-free commutative subclass, which contradicts the repo convention that all local vertex algebras remain `$E_\infty$` even when OPE poles are present.
+   Fix: rewrote the affected sentences to distinguish the pole-free BD-commutative subclass from general `$E_\infty$`-chiral vertex algebras with OPE poles, and kept the genuinely `$E_1$` case reserved for independent `$R$`-matrix input.
+   Status: `FIXED`
+
+649. `2026-04-13-649`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:111-113`, `working_notes.tex:3044-3048`, `working_notes.tex:15913-15919`, `working_notes.tex:15978-15986`
+   Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
+   Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
+   Status: `FIXED`
diff --git a/working_notes.tex b/working_notes.tex
index f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde..bd037eaa21e69666e0e378f12f0c3fa2a45b3e04
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -3041,11 +3041,11 @@
 
 The three-tier picture (AP51) maps precisely:
 \begin{itemize}[nosep]
-\item Tier~(i) (pole-free): forgetful functor to
+\item Tier~(i) (pole-free BD-commutative $E_\infty$ subclass): forgetful functor to
   $\mathrm{Vect}$, commutative Hopf algebra.
-\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
+\item Tier~(ii) (local $E_\infty$ with OPE poles, class~L): $\omega_{\mathrm{BPZ}}$
   exists, compact quantum group.
-\item Tier~(iii) (class~M): \textbf{no} fibre functor to
+\item Tier~(iii) (still local $E_\infty$, class~M): \textbf{no} fibre functor to
   $\mathrm{Hilb}$ can make the braiding unitary---the
   $A_\infty$ tower prevents it
   (Remark~\ref{rem:virasoro-qg-unitarity}).
@@ -15910,8 +15910,8 @@
 The descent from ordered to unordered is $R$-twisted:
 $B^{\mathrm{ch}}(\cA)_n \simeq
 (\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
-For pole-free $E_\infty$-chiral algebras (the
-BD-commutative subclass: no OPE singularities):
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras (no OPE singularities):
 $R(z) = \tau$ (the flip), descent is trivial, both
 duals carry equivalent information.  For
 $E_\infty$-chiral algebras with OPE poles
@@ -15975,8 +15975,8 @@
 differential remains the sole gap.
 
 \medskip\noindent\textbf{When do the two duals agree?}\enspace
-When $\cA$ is pole-free $E_\infty$-chiral (the
-BD-commutative subclass): $R(z) = \tau$, descent is
+When $\cA$ lies in the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras: $R(z) = \tau$, descent is
 trivial, both duals carry equivalent information.
 
 \noindent\textbf{When do they disagree?}\enspace

codex
The edits are in. I’m re-grepping the exact bad equivalences now and then I’ll do one final diff pass so the report can name each problem site and the exact repair, not just the file list.
exec
/bin/zsh -lc "rg -n -F -e 'An "'$E_'"\\infty"'$-algebra (commutative chiral algebra)'"' -e '"'$E_'"\\infty"'$-chiral algebras (commutative chiral algebras),'"' -e '"'$E_'"\\infty"'$-chiral algebras (commutative chiral algebras)'"' -e 'i.e.\\ has only simple poles' -e 'For "'$E_'"\\infty"'$-algebras, $R(z)='"\\tau"'$'"' -e 'For "'$E_'"\\infty"'$-algebras, $R(z)=1$'"' -e 'For pole-free "'$E_'"\\infty"'$-algebras'"' -e '"'$E_'"\\infty"'$ with poles, class~L'"' chapters working_notes.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '1588,1595p;1998,2007p;2347,2353p;2377,2383p;2712,2719p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex working_notes.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
  1588	\index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
  1589	An $E_\infty$-chiral algebra has
  1590	$\Sigma_n$-equivariant operations, so its bar complex
  1591	uses the unordered space $\mathrm{Conf}_n(X)$.
  1592	The pole-free BD-commutative subclass is a special case.
  1593	An $E_1$-algebra (associative chiral algebra) has
  1594	operations indexed by \emph{ordered} compositions, so its
  1595	bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
  1998	is the quotient by the symmetric group action. For
  1999	$E_\infty$-chiral algebras in the pole-free
  2000	BD-commutative subclass, the two are equivalent. For local
  2001	vertex algebras with OPE poles, the comparison is still
  2002	$E_\infty$-chiral but requires the OPE-derived
  2003	$R$-matrix twist. For genuinely $E_1$-chiral
  2004	algebras (Yangians, quantum groups), the ordered complex
  2005	carries strictly more information: the $R$-matrix is the
  2006	data needed to descend from ordered to unordered.
  2007	
  2347	{\Barch}_2^{\mathrm{ord}}(a\otimes b;\,z_1,z_2)
  2348	\;\xrightarrow{\;\sim\;}
 succeeded in 52ms:
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 9ffafff..9228dbe 100644
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1500,7 +1500,7 @@ The $E_1$-chiral MC element $\Theta^{E_1}_\cA \in \mathrm{MC}(\mathfrak{g}^{E_1}
  Drinfeld--Kohno hierarchy lies on the additional Yangian/spectral
  surface.
 \end{enumerate}
-The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
+The $E_1$ five main theorems (Vol~I, $E_1$-Modular Koszul chapter) are the ordered analogues of Theorems~A--D and~H, with the associative bar replacing the commutative bar and planar forests replacing stable graphs.
 \end{construction}
 
 \subsection{BRST and Drinfeld--Sokolov compatibility}
@@ -1726,9 +1726,10 @@ $\mathrm{Conf}_n(X)
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 % label removed: rem:why-ordered
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 40fe4da0989385b75cd4642d4b1a2eab94133f84..9228dbe201ab55af25fa03100b0e6b698c79438e
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1726,9 +1726,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 % label removed: rem:why-ordered
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1890,8 +1891,11 @@
 The comparison map
 ${\Barch}^{\mathrm{ord}}(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2018,7 +2022,8 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
 and unordered complexes are identified. For genuine
 $E_1$-algebras, $R(z)$ carries nontrivial spectral dependence
 and is the fundamental new datum.
@@ -2044,7 +2049,8 @@
 $\Sigma_n$-action is well-defined if and only if the
 $R$-matrix satisfies the Yang--Baxter
 equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
-For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent reduces to
 ordinary $\Sigma_n$-coinvariants.
 \end{proposition}
 
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e..1f83cc97f58577b74f72a2b202f651aeb6a24295
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -1586,9 +1586,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 \label{rem:why-ordered}
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1995,8 +1996,11 @@
 The comparison map
 $\Barchord(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2344,9 +2348,11 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
-and unordered complexes are identified. For $E_\infty$-algebras
-with OPE poles, $R(z)\ne\tau$ but is derived from the local OPE.
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
+and unordered complexes are identified. For local
+vertex algebras in the $E_\infty$ regime with OPE poles,
+$R(z)\ne\tau$ but is derived from the local OPE.
 For genuine $E_1$-algebras, $R(z)$ carries nontrivial spectral
 dependence as independent input and is the fundamental new datum.
 \end{construction}
@@ -2374,9 +2380,10 @@
 it factors through $\Sigma_n$ if and only if~$R$
 satisfies \emph{strong unitarity}
 $R_{12}(z)\,R_{21}(-z)=\id$.
-For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
-reduces to ordinary $\Sigma_n$-coinvariants; for
-$E_\infty$-algebras with OPE poles, the descent is
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent
+reduces to ordinary $\Sigma_n$-coinvariants; for local
+vertex algebras in the $E_\infty$ regime with OPE poles, the descent is
 $R$-twisted (nontrivially, though $R(z)$ is derived from
 the local OPE).
 \end{proposition}
@@ -2709,8 +2716,8 @@
 $\Barch(\cA)_n \simeq
 (\Barchord(\cA)_n)^{R\text{-}\Sigma_n}$
 (Proposition~\ref{prop:r-matrix-descent}). For
-$E_\infty$-chiral algebras (commutative chiral algebras)
-whose OPE is pole-free, $R(z) = \tau$ and both
+the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z) = \tau$ and both
 projections carry equivalent information. For
 $E_\infty$-chiral algebras with OPE poles
 (all interesting vertex algebras: affine Kac--Moody,
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 6fce089e098fc34bcf219498799daa5ec0e5dcfe..77df257ed240cb9a38f75b9952ce20448768bd97
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -108,8 +108,9 @@
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
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 54dd69e23a585e854d9495a5039d99a6002966df..f946f54cbb93fcef4a840934cfa6eb561cabdff7
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14422,3 +14422,19 @@
    Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
    Fix: replaced each comment-line em dash `—` with ASCII `--`.
    Status: `FIXED`
+
+648. `2026-04-13-648`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:1589-1593`, `chapters/connections/ordered_associative_chiral_kd_core.tex:1998-2005`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2347-2350`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2377-2380`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2712-2718`, `chapters/connections/ordered_associative_chiral_kd.tex:1729-1733`, `chapters/connections/ordered_associative_chiral_kd.tex:1893-1900`, `chapters/connections/ordered_associative_chiral_kd.tex:2021-2024`, `chapters/connections/ordered_associative_chiral_kd.tex:2047-2049`
+   Issue: these ordered/unordered comparison passages identified `$E_\infty$` with the pole-free commutative subclass, which contradicts the repo convention that all local vertex algebras remain `$E_\infty$` even when OPE poles are present.
+   Fix: rewrote the affected sentences to distinguish the pole-free BD-commutative subclass from general `$E_\infty$`-chiral vertex algebras with OPE poles, and kept the genuinely `$E_1$` case reserved for independent `$R$`-matrix input.
+   Status: `FIXED`
+
+649. `2026-04-13-649`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:111-113`, `working_notes.tex:3044-3048`, `working_notes.tex:15913-15919`, `working_notes.tex:15978-15986`
+   Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
+   Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
+   Status: `FIXED`
diff --git a/working_notes.tex b/working_notes.tex
index f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde..bd037eaa21e69666e0e378f12f0c3fa2a45b3e04
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -3041,11 +3041,11 @@
 
 The three-tier picture (AP51) maps precisely:
 \begin{itemize}[nosep]
-\item Tier~(i) (pole-free): forgetful functor to
+\item Tier~(i) (pole-free BD-commutative $E_\infty$ subclass): forgetful functor to
   $\mathrm{Vect}$, commutative Hopf algebra.
-\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
+\item Tier~(ii) (local $E_\infty$ with OPE poles, class~L): $\omega_{\mathrm{BPZ}}$
   exists, compact quantum group.
-\item Tier~(iii) (class~M): \textbf{no} fibre functor to
+\item Tier~(iii) (still local $E_\infty$, class~M): \textbf{no} fibre functor to
   $\mathrm{Hilb}$ can make the braiding unitary---the
   $A_\infty$ tower prevents it
   (Remark~\ref{rem:virasoro-qg-unitarity}).
@@ -15910,8 +15910,8 @@
 The descent from ordered to unordered is $R$-twisted:
 $B^{\mathrm{ch}}(\cA)_n \simeq
 (\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
-For pole-free $E_\infty$-chiral algebras (the
-BD-commutative subclass: no OPE singularities):
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras (no OPE singularities):
 $R(z) = \tau$ (the flip), descent is trivial, both
 duals carry equivalent information.  For
 $E_\infty$-chiral algebras with OPE poles
@@ -15975,8 +15975,8 @@
 differential remains the sole gap.
 
 \medskip\noindent\textbf{When do the two duals agree?}\enspace
-When $\cA$ is pole-free $E_\infty$-chiral (the
-BD-commutative subclass): $R(z) = \tau$, descent is
+When $\cA$ lies in the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras: $R(z) = \tau$, descent is
 trivial, both duals carry equivalent information.
 
 \noindent\textbf{When do they disagree?}\enspace



thinking
**Evaluating findings and edits**

I think I need to use `nl -ba` for the full file and my working notes. I noticed that the `compute/audit/linear_read_notes.md` has some duplicates because of previous user changes. It’s fine, but I’m unsure if I should mention the audit file in my findings or focus on the issues asked by the user. I should probably just stick to listing those issues and see if any suspicious phrases remain in the repo.
thinking
**Searching for patterns**

I think there might be other incorrect patterns that I haven't searched for yet. It could be helpful to broaden my search using `E_\infty.*commutative chiral algebra` or `E_\infty.*simple poles` in those files. I’m considering employing `rg` to run a more comprehensive search. It seems like a good idea to make sure I cover all bases and identify any potential issues that could be lurking around.
codex
The direct bad patterns are gone. I’m doing one last broad scan for weaker survivors like `E_\infty ... commutative chiral algebra` or `E_\infty ... simple poles` so I don’t leave a nearby variant behind.
exec
/bin/zsh -lc "rg -n 'E_\\\\infty.{0,80}commutative chiral algebra|commutative chiral algebra.{0,80}E_\\\\infty|E_\\\\infty.{0,80}simple pole|simple pole.{0,80}E_\\\\infty' chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex working_notes.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd.tex | sed -n '1728,1736p;1892,1902p;2022,2027p;2048,2053p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '110,115p' && nl -ba working_notes.tex | sed -n '3043,3048p;15913,15920p;15978,15986p'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 52ms:

 succeeded in 50ms:
  1728	\index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
  1729	An $E_\infty$-chiral algebra has
  1730	$\Sigma_n$-equivariant operations, so its bar complex
  1731	uses the unordered space $\mathrm{Conf}_n(X)$.
  1732	The pole-free BD-commutative subclass is a special case.
  1733	An $E_1$-algebra (associative chiral algebra) has
  1734	operations indexed by \emph{ordered} compositions, so its
  1735	bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
  1736	The ordering records the topological direction: in
  1892	${\Barch}^{\mathrm{ord}}(\cA)\to\Barch(\cA)$
  1893	is the quotient by the symmetric group action. For
  1894	$E_\infty$-chiral algebras in the pole-free
  1895	BD-commutative subclass, the two are equivalent. For local
  1896	vertex algebras with OPE poles, the comparison is still
  1897	$E_\infty$-chiral but requires the OPE-derived
  1898	$R$-matrix twist. For genuinely $E_1$-chiral
  1899	algebras (Yangians, quantum groups), the ordered complex
  1900	carries strictly more information: the $R$-matrix is the
  1901	data needed to descend from ordered to unordered.
  1902	\end{remark}
 succeeded in 51ms:
   110	filtration with $\bigcup_p S_p = \FM_k(\mathbb{C})\times\Conf_k(\mathbb{R})$.
   111	For the associated graded $\gr_{\mathrm{com}}A$ (which remains
   112	$E_\infty$-chiral and, by construction of the commutator filtration,
   113	has only first-order OPE singularities), only the stratum $S_1$ contributes to the bar
   114	differential: all OPE singularities are at worst first-order.
   115	\end{construction}
  3043	\begin{itemize}[nosep]
  3044	\item Tier~(i) (pole-free BD-commutative $E_\infty$ subclass): forgetful functor to
  3045	  $\mathrm{Vect}$, commutative Hopf algebra.
  3046	\item Tier~(ii) (local $E_\infty$ with OPE poles, class~L): $\omega_{\mathrm{BPZ}}$
  3047	  exists, compact quantum group.
  3048	\item Tier~(iii) (still local $E_\infty$, class~M): \textbf{no} fibre functor to
 15913	For the pole-free BD-commutative subclass of
 15914	$E_\infty$-chiral algebras (no OPE singularities):
 15915	$R(z) = \tau$ (the flip), descent is trivial, both
 15916	duals carry equivalent information.  For
 15917	$E_\infty$-chiral algebras with OPE poles
 15918	(Heisenberg, affine KM, Virasoro --- still $E_\infty$,
 15919	since all vertex algebras are $E_\infty$-chiral):
 15920	$R(z) \neq \tau$ (derived from the local OPE via
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 40fe4da0989385b75cd4642d4b1a2eab94133f84..9228dbe201ab55af25fa03100b0e6b698c79438e
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1726,9 +1726,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 % label removed: rem:why-ordered
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1890,8 +1891,11 @@
 The comparison map
 ${\Barch}^{\mathrm{ord}}(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2018,7 +2022,8 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
 and unordered complexes are identified. For genuine
 $E_1$-algebras, $R(z)$ carries nontrivial spectral dependence
 and is the fundamental new datum.
@@ -2044,7 +2049,8 @@
 $\Sigma_n$-action is well-defined if and only if the
 $R$-matrix satisfies the Yang--Baxter
 equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
-For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent reduces to
 ordinary $\Sigma_n$-coinvariants.
 \end{proposition}
 
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e..1f83cc97f58577b74f72a2b202f651aeb6a24295
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -1586,9 +1586,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 \label{rem:why-ordered}
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1995,8 +1996,11 @@
 The comparison map
 $\Barchord(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2344,9 +2348,11 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
-and unordered complexes are identified. For $E_\infty$-algebras
-with OPE poles, $R(z)\ne\tau$ but is derived from the local OPE.
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
+and unordered complexes are identified. For local
+vertex algebras in the $E_\infty$ regime with OPE poles,
+$R(z)\ne\tau$ but is derived from the local OPE.
 For genuine $E_1$-algebras, $R(z)$ carries nontrivial spectral
 dependence as independent input and is the fundamental new datum.
 \end{construction}
@@ -2374,9 +2380,10 @@
 it factors through $\Sigma_n$ if and only if~$R$
 satisfies \emph{strong unitarity}
 $R_{12}(z)\,R_{21}(-z)=\id$.
-For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
-reduces to ordinary $\Sigma_n$-coinvariants; for
-$E_\infty$-algebras with OPE poles, the descent is
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent
+reduces to ordinary $\Sigma_n$-coinvariants; for local
+vertex algebras in the $E_\infty$ regime with OPE poles, the descent is
 $R$-twisted (nontrivially, though $R(z)$ is derived from
 the local OPE).
 \end{proposition}
@@ -2709,8 +2716,8 @@
 $\Barch(\cA)_n \simeq
 (\Barchord(\cA)_n)^{R\text{-}\Sigma_n}$
 (Proposition~\ref{prop:r-matrix-descent}). For
-$E_\infty$-chiral algebras (commutative chiral algebras)
-whose OPE is pole-free, $R(z) = \tau$ and both
+the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z) = \tau$ and both
 projections carry equivalent information. For
 $E_\infty$-chiral algebras with OPE poles
 (all interesting vertex algebras: affine Kac--Moody,
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 6fce089e098fc34bcf219498799daa5ec0e5dcfe..77df257ed240cb9a38f75b9952ce20448768bd97
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -108,8 +108,9 @@
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
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 54dd69e23a585e854d9495a5039d99a6002966df..f946f54cbb93fcef4a840934cfa6eb561cabdff7
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14422,3 +14422,19 @@
    Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
    Fix: replaced each comment-line em dash `—` with ASCII `--`.
    Status: `FIXED`
+
+648. `2026-04-13-648`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:1589-1593`, `chapters/connections/ordered_associative_chiral_kd_core.tex:1998-2005`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2347-2350`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2377-2380`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2712-2718`, `chapters/connections/ordered_associative_chiral_kd.tex:1729-1733`, `chapters/connections/ordered_associative_chiral_kd.tex:1893-1900`, `chapters/connections/ordered_associative_chiral_kd.tex:2021-2024`, `chapters/connections/ordered_associative_chiral_kd.tex:2047-2049`
+   Issue: these ordered/unordered comparison passages identified `$E_\infty$` with the pole-free commutative subclass, which contradicts the repo convention that all local vertex algebras remain `$E_\infty$` even when OPE poles are present.
+   Fix: rewrote the affected sentences to distinguish the pole-free BD-commutative subclass from general `$E_\infty$`-chiral vertex algebras with OPE poles, and kept the genuinely `$E_1$` case reserved for independent `$R$`-matrix input.
+   Status: `FIXED`
+
+649. `2026-04-13-649`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:111-113`, `working_notes.tex:3044-3048`, `working_notes.tex:15913-15919`, `working_notes.tex:15978-15986`
+   Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
+   Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
+   Status: `FIXED`
diff --git a/working_notes.tex b/working_notes.tex
index f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde..bd037eaa21e69666e0e378f12f0c3fa2a45b3e04
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -3041,11 +3041,11 @@
 
 The three-tier picture (AP51) maps precisely:
 \begin{itemize}[nosep]
-\item Tier~(i) (pole-free): forgetful functor to
+\item Tier~(i) (pole-free BD-commutative $E_\infty$ subclass): forgetful functor to
   $\mathrm{Vect}$, commutative Hopf algebra.
-\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
+\item Tier~(ii) (local $E_\infty$ with OPE poles, class~L): $\omega_{\mathrm{BPZ}}$
   exists, compact quantum group.
-\item Tier~(iii) (class~M): \textbf{no} fibre functor to
+\item Tier~(iii) (still local $E_\infty$, class~M): \textbf{no} fibre functor to
   $\mathrm{Hilb}$ can make the braiding unitary---the
   $A_\infty$ tower prevents it
   (Remark~\ref{rem:virasoro-qg-unitarity}).
@@ -15910,8 +15910,8 @@
 The descent from ordered to unordered is $R$-twisted:
 $B^{\mathrm{ch}}(\cA)_n \simeq
 (\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
-For pole-free $E_\infty$-chiral algebras (the
-BD-commutative subclass: no OPE singularities):
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras (no OPE singularities):
 $R(z) = \tau$ (the flip), descent is trivial, both
 duals carry equivalent information.  For
 $E_\infty$-chiral algebras with OPE poles
@@ -15975,8 +15975,8 @@
 differential remains the sole gap.
 
 \medskip\noindent\textbf{When do the two duals agree?}\enspace
-When $\cA$ is pole-free $E_\infty$-chiral (the
-BD-commutative subclass): $R(z) = \tau$, descent is
+When $\cA$ lies in the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras: $R(z) = \tau$, descent is
 trivial, both duals carry equivalent information.
 
 \noindent\textbf{When do they disagree?}\enspace


thinking
**Updating plan status**

I’m considering using `nl -ba` to focus on all the changed lines, and it seems we already have some. I might need the full set including line 2351 and updating `working_notes` line numbers. I’m also unsure if I need to include `nl` for the compute ledger, and maybe it’s not necessary. I think I’ll skip a final mention in my report and ensure the plan status is marked as completed.
Plan update
Patched the terminology violations, logged them in the audit ledger, and re-grepped the scope to confirm the bad `E_\infty`/pole-order equivalences are gone.
  ✓ Inspect active Vol II input graph and grep for `E_inf`/`vertex algebra`/`no poles` violation patterns
  ✓ Read the exact contexts, classify actionable terminology violations, and record them in the audit ledger
  ✓ Apply minimal truthful edits only in violating files
  ✓ Re-grep the scope to verify the violations are removed and summarize exact fixes
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 40fe4da0989385b75cd4642d4b1a2eab94133f84..9228dbe201ab55af25fa03100b0e6b698c79438e
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1726,9 +1726,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 % label removed: rem:why-ordered
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1890,8 +1891,11 @@
 The comparison map
 ${\Barch}^{\mathrm{ord}}(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2018,7 +2022,8 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
 and unordered complexes are identified. For genuine
 $E_1$-algebras, $R(z)$ carries nontrivial spectral dependence
 and is the fundamental new datum.
@@ -2044,7 +2049,8 @@
 $\Sigma_n$-action is well-defined if and only if the
 $R$-matrix satisfies the Yang--Baxter
 equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
-For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent reduces to
 ordinary $\Sigma_n$-coinvariants.
 \end{proposition}
 
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e..1f83cc97f58577b74f72a2b202f651aeb6a24295
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -1586,9 +1586,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 \label{rem:why-ordered}
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1995,8 +1996,11 @@
 The comparison map
 $\Barchord(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2344,9 +2348,11 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
-and unordered complexes are identified. For $E_\infty$-algebras
-with OPE poles, $R(z)\ne\tau$ but is derived from the local OPE.
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
+and unordered complexes are identified. For local
+vertex algebras in the $E_\infty$ regime with OPE poles,
+$R(z)\ne\tau$ but is derived from the local OPE.
 For genuine $E_1$-algebras, $R(z)$ carries nontrivial spectral
 dependence as independent input and is the fundamental new datum.
 \end{construction}
@@ -2374,9 +2380,10 @@
 it factors through $\Sigma_n$ if and only if~$R$
 satisfies \emph{strong unitarity}
 $R_{12}(z)\,R_{21}(-z)=\id$.
-For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
-reduces to ordinary $\Sigma_n$-coinvariants; for
-$E_\infty$-algebras with OPE poles, the descent is
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent
+reduces to ordinary $\Sigma_n$-coinvariants; for local
+vertex algebras in the $E_\infty$ regime with OPE poles, the descent is
 $R$-twisted (nontrivially, though $R(z)$ is derived from
 the local OPE).
 \end{proposition}
@@ -2709,8 +2716,8 @@
 $\Barch(\cA)_n \simeq
 (\Barchord(\cA)_n)^{R\text{-}\Sigma_n}$
 (Proposition~\ref{prop:r-matrix-descent}). For
-$E_\infty$-chiral algebras (commutative chiral algebras)
-whose OPE is pole-free, $R(z) = \tau$ and both
+the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z) = \tau$ and both
 projections carry equivalent information. For
 $E_\infty$-chiral algebras with OPE poles
 (all interesting vertex algebras: affine Kac--Moody,
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 6fce089e098fc34bcf219498799daa5ec0e5dcfe..77df257ed240cb9a38f75b9952ce20448768bd97
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -108,8 +108,9 @@
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
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 54dd69e23a585e854d9495a5039d99a6002966df..f946f54cbb93fcef4a840934cfa6eb561cabdff7
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14422,3 +14422,19 @@
    Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
    Fix: replaced each comment-line em dash `—` with ASCII `--`.
    Status: `FIXED`
+
+648. `2026-04-13-648`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:1589-1593`, `chapters/connections/ordered_associative_chiral_kd_core.tex:1998-2005`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2347-2350`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2377-2380`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2712-2718`, `chapters/connections/ordered_associative_chiral_kd.tex:1729-1733`, `chapters/connections/ordered_associative_chiral_kd.tex:1893-1900`, `chapters/connections/ordered_associative_chiral_kd.tex:2021-2024`, `chapters/connections/ordered_associative_chiral_kd.tex:2047-2049`
+   Issue: these ordered/unordered comparison passages identified `$E_\infty$` with the pole-free commutative subclass, which contradicts the repo convention that all local vertex algebras remain `$E_\infty$` even when OPE poles are present.
+   Fix: rewrote the affected sentences to distinguish the pole-free BD-commutative subclass from general `$E_\infty$`-chiral vertex algebras with OPE poles, and kept the genuinely `$E_1$` case reserved for independent `$R$`-matrix input.
+   Status: `FIXED`
+
+649. `2026-04-13-649`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:111-113`, `working_notes.tex:3044-3048`, `working_notes.tex:15913-15919`, `working_notes.tex:15978-15986`
+   Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
+   Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
+   Status: `FIXED`
diff --git a/working_notes.tex b/working_notes.tex
index f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde..bd037eaa21e69666e0e378f12f0c3fa2a45b3e04
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -3041,11 +3041,11 @@
 
 The three-tier picture (AP51) maps precisely:
 \begin{itemize}[nosep]
-\item Tier~(i) (pole-free): forgetful functor to
+\item Tier~(i) (pole-free BD-commutative $E_\infty$ subclass): forgetful functor to
   $\mathrm{Vect}$, commutative Hopf algebra.
-\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
+\item Tier~(ii) (local $E_\infty$ with OPE poles, class~L): $\omega_{\mathrm{BPZ}}$
   exists, compact quantum group.
-\item Tier~(iii) (class~M): \textbf{no} fibre functor to
+\item Tier~(iii) (still local $E_\infty$, class~M): \textbf{no} fibre functor to
   $\mathrm{Hilb}$ can make the braiding unitary---the
   $A_\infty$ tower prevents it
   (Remark~\ref{rem:virasoro-qg-unitarity}).
@@ -15910,8 +15910,8 @@
 The descent from ordered to unordered is $R$-twisted:
 $B^{\mathrm{ch}}(\cA)_n \simeq
 (\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
-For pole-free $E_\infty$-chiral algebras (the
-BD-commutative subclass: no OPE singularities):
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras (no OPE singularities):
 $R(z) = \tau$ (the flip), descent is trivial, both
 duals carry equivalent information.  For
 $E_\infty$-chiral algebras with OPE poles
@@ -15975,8 +15975,8 @@
 differential remains the sole gap.
 
 \medskip\noindent\textbf{When do the two duals agree?}\enspace
-When $\cA$ is pole-free $E_\infty$-chiral (the
-BD-commutative subclass): $R(z) = \tau$, descent is
+When $\cA$ lies in the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras: $R(z) = \tau$, descent is
 trivial, both duals carry equivalent information.
 
 \noindent\textbf{When do they disagree?}\enspace



thinking
**Summarizing findings**

I’m considering mentioning about six findings. First, there's the core 1589 and the superseded 1729. Next up, core 1999 and the superseded 1894. Then, I'll touch on core 2351, 2383, and 2719 along with their superseded numbers 2025 and 2052. Additionally, I’d include frontier 111, working notes 3044-3048, and finally working notes 15913 and 15978. Alright, maybe that’s enough information to cover.
thinking
**Producing concise records**

I realize that skill development requires documentation, but I don't think I need to go into great detail. I might just note that I've logged this in linear_read_notes.md without needing an extra line. It's important to keep the explanation straightforward and not overly verbose. My goal here is to produce something concise while ensuring I include all the necessary details.
codex
1. PROBLEM at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1589) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1729): `E_\infty` was stated as if it meant `commutative chiral algebra`. EXACT edit applied: changed `An $E_\infty$-algebra (commutative chiral algebra) has` to `An $E_\infty$-chiral algebra has`, and added `The pole-free BD-commutative subclass is a special case.`

2. PROBLEM at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1998) and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1893): the ordered/unordered comparison said the two coincide for `E_\infty`-chiral algebras as such, collapsing `E_\infty` to the pole-free subclass. EXACT edit applied: replaced `For $E_\infty$-chiral algebras (commutative chiral algebras), the two are equivalent.` with `For $E_\infty$-chiral algebras in the pole-free BD-commutative subclass, the two are equivalent. For local vertex algebras with OPE poles, the comparison is still $E_\infty$-chiral but requires the OPE-derived $R$-matrix twist.`

3. PROBLEM at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2351), [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2383), [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2719), [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2025), and [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2052): the descent/`R`-matrix clauses used `For $E_\infty$-algebras...` or `For pole-free $E_\infty$-algebras...` in a way that made pole-freeness sound definitional. EXACT edit applied: rewrote each clause to `For the pole-free BD-commutative subclass of $E_\infty$-chiral algebras, ...`; in the core file I also changed `For $E_\infty$-algebras with OPE poles` to `For local vertex algebras in the $E_\infty$ regime with OPE poles`.

4. PROBLEM at [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:111): `E_\infty` was glossed as `i.e. has only simple poles`. EXACT edit applied: changed `which is $E_\infty$-chiral, i.e.\ has only simple poles` to `which remains $E_\infty$-chiral and, by construction of the commutator filtration, has only first-order OPE singularities`.

5. PROBLEM at [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:3044): the three-tier summary treated class `L` as the `E_\infty` poleful tier and left class `M` outside that local `E_\infty` regime. EXACT edit applied: changed the tier labels to `Tier~(i) (pole-free BD-commutative $E_\infty$ subclass)`, `Tier~(ii) (local $E_\infty$ with OPE poles, class~L)`, and `Tier~(iii) (still local $E_\infty$, class~M)`.

6. PROBLEM at [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:15913) and [working_notes.tex](/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:15978): the duality summary still used `pole-free $E_\infty$-chiral` phrasing that invited the same false identification. EXACT edit applied: changed those clauses to `the pole-free BD-commutative subclass of $E_\infty$-chiral algebras` and `lies in the pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.

Verification: I re-grepped the scope for the exact bad equivalences (`E_\infty = commutative/pole-free`, `E_\infty = simple-pole`, and the old tier label), and those hits are now gone. I did not run a LaTeX build.
file update:
diff --git a/chapters/connections/ordered_associative_chiral_kd.tex b/chapters/connections/ordered_associative_chiral_kd.tex
index 40fe4da0989385b75cd4642d4b1a2eab94133f84..9228dbe201ab55af25fa03100b0e6b698c79438e
--- a/chapters/connections/ordered_associative_chiral_kd.tex
+++ b/chapters/connections/ordered_associative_chiral_kd.tex
@@ -1726,9 +1726,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 % label removed: rem:why-ordered
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1890,8 +1891,11 @@
 The comparison map
 ${\Barch}^{\mathrm{ord}}(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2018,7 +2022,8 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
 and unordered complexes are identified. For genuine
 $E_1$-algebras, $R(z)$ carries nontrivial spectral dependence
 and is the fundamental new datum.
@@ -2044,7 +2049,8 @@
 $\Sigma_n$-action is well-defined if and only if the
 $R$-matrix satisfies the Yang--Baxter
 equation~\textup{(Proposition~\ref{prop:ybe-from-d-squared})}.
-For $E_\infty$-algebras, $R(z)=1$ and the descent reduces to
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent reduces to
 ordinary $\Sigma_n$-coinvariants.
 \end{proposition}
 
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e..1f83cc97f58577b74f72a2b202f651aeb6a24295
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -1586,9 +1586,10 @@
 \begin{remark}[Why ordered spaces for $E_1$-algebras]
 \label{rem:why-ordered}
 \index{E1 algebra@$E_1$-algebra!ordered configuration spaces}
-An $E_\infty$-algebra (commutative chiral algebra) has
+An $E_\infty$-chiral algebra has
 $\Sigma_n$-equivariant operations, so its bar complex
 uses the unordered space $\mathrm{Conf}_n(X)$.
+The pole-free BD-commutative subclass is a special case.
 An $E_1$-algebra (associative chiral algebra) has
 operations indexed by \emph{ordered} compositions, so its
 bar complex uses $\mathrm{Conf}_n^{\mathrm{ord}}(X)$.
@@ -1995,8 +1996,11 @@
 The comparison map
 $\Barchord(\cA)\to\Barch(\cA)$
 is the quotient by the symmetric group action. For
-$E_\infty$-chiral algebras (commutative chiral algebras),
-the two are equivalent. For genuinely $E_1$-chiral
+$E_\infty$-chiral algebras in the pole-free
+BD-commutative subclass, the two are equivalent. For local
+vertex algebras with OPE poles, the comparison is still
+$E_\infty$-chiral but requires the OPE-derived
+$R$-matrix twist. For genuinely $E_1$-chiral
 algebras (Yangians, quantum groups), the ordered complex
 carries strictly more information: the $R$-matrix is the
 data needed to descend from ordered to unordered.
@@ -2344,9 +2348,11 @@
 \;\xrightarrow{\;\sim\;}
 {\Barch}_2^{\mathrm{ord}}(b\otimes a;\,z_2,z_1).
 \]
-For pole-free $E_\infty$-algebras, $R(z)=\tau$ (the flip): ordered
-and unordered complexes are identified. For $E_\infty$-algebras
-with OPE poles, $R(z)\ne\tau$ but is derived from the local OPE.
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=\tau$ (the flip): ordered
+and unordered complexes are identified. For local
+vertex algebras in the $E_\infty$ regime with OPE poles,
+$R(z)\ne\tau$ but is derived from the local OPE.
 For genuine $E_1$-algebras, $R(z)$ carries nontrivial spectral
 dependence as independent input and is the fundamental new datum.
 \end{construction}
@@ -2374,9 +2380,10 @@
 it factors through $\Sigma_n$ if and only if~$R$
 satisfies \emph{strong unitarity}
 $R_{12}(z)\,R_{21}(-z)=\id$.
-For pole-free $E_\infty$-algebras, $R(z)=1$ and the descent
-reduces to ordinary $\Sigma_n$-coinvariants; for
-$E_\infty$-algebras with OPE poles, the descent is
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z)=1$ and the descent
+reduces to ordinary $\Sigma_n$-coinvariants; for local
+vertex algebras in the $E_\infty$ regime with OPE poles, the descent is
 $R$-twisted (nontrivially, though $R(z)$ is derived from
 the local OPE).
 \end{proposition}
@@ -2709,8 +2716,8 @@
 $\Barch(\cA)_n \simeq
 (\Barchord(\cA)_n)^{R\text{-}\Sigma_n}$
 (Proposition~\ref{prop:r-matrix-descent}). For
-$E_\infty$-chiral algebras (commutative chiral algebras)
-whose OPE is pole-free, $R(z) = \tau$ and both
+the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras, $R(z) = \tau$ and both
 projections carry equivalent information. For
 $E_\infty$-chiral algebras with OPE poles
 (all interesting vertex algebras: affine Kac--Moody,
diff --git a/chapters/connections/ordered_associative_chiral_kd_frontier.tex b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
index 6fce089e098fc34bcf219498799daa5ec0e5dcfe..77df257ed240cb9a38f75b9952ce20448768bd97
--- a/chapters/connections/ordered_associative_chiral_kd_frontier.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_frontier.tex
@@ -108,8 +108,9 @@
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
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 54dd69e23a585e854d9495a5039d99a6002966df..f946f54cbb93fcef4a840934cfa6eb561cabdff7
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -14422,3 +14422,19 @@
    Issue: chapter comment headers still contained Unicode em dashes, which violated the repo's chapter-level slop grep surface even though the prose body was clean.
    Fix: replaced each comment-line em dash `—` with ASCII `--`.
    Status: `FIXED`
+
+648. `2026-04-13-648`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_core.tex:1589-1593`, `chapters/connections/ordered_associative_chiral_kd_core.tex:1998-2005`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2347-2350`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2377-2380`, `chapters/connections/ordered_associative_chiral_kd_core.tex:2712-2718`, `chapters/connections/ordered_associative_chiral_kd.tex:1729-1733`, `chapters/connections/ordered_associative_chiral_kd.tex:1893-1900`, `chapters/connections/ordered_associative_chiral_kd.tex:2021-2024`, `chapters/connections/ordered_associative_chiral_kd.tex:2047-2049`
+   Issue: these ordered/unordered comparison passages identified `$E_\infty$` with the pole-free commutative subclass, which contradicts the repo convention that all local vertex algebras remain `$E_\infty$` even when OPE poles are present.
+   Fix: rewrote the affected sentences to distinguish the pole-free BD-commutative subclass from general `$E_\infty$`-chiral vertex algebras with OPE poles, and kept the genuinely `$E_1$` case reserved for independent `$R$`-matrix input.
+   Status: `FIXED`
+
+649. `2026-04-13-649`
+   Severity: `MODERATE`
+   Class: `W/C`
+   Location: `chapters/connections/ordered_associative_chiral_kd_frontier.tex:111-113`, `working_notes.tex:3044-3048`, `working_notes.tex:15913-15919`, `working_notes.tex:15978-15986`
+   Issue: the frontier stratification note and working-notes summaries tied `$E_\infty$` to simple-pole or pole-free behavior, and one tier summary excluded class-`M` local vertex algebras from the `$E_\infty$` regime.
+   Fix: changed the stratification sentence so the first-order pole statement is attributed to the commutator filtration rather than to `$E_\infty$`, rewrote the tier summary so classes `L` and `M` are both local `$E_\infty$` regimes, and rewrote the pole-free clauses in the duality summary to say `pole-free BD-commutative subclass of $E_\infty$-chiral algebras`.
+   Status: `FIXED`
diff --git a/working_notes.tex b/working_notes.tex
index f385356d4cb8e2c08fc29c8a99cda6eba4ec0dde..bd037eaa21e69666e0e378f12f0c3fa2a45b3e04
--- a/working_notes.tex
+++ b/working_notes.tex
@@ -3041,11 +3041,11 @@
 
 The three-tier picture (AP51) maps precisely:
 \begin{itemize}[nosep]
-\item Tier~(i) (pole-free): forgetful functor to
+\item Tier~(i) (pole-free BD-commutative $E_\infty$ subclass): forgetful functor to
   $\mathrm{Vect}$, commutative Hopf algebra.
-\item Tier~(ii) ($E_\infty$ with poles, class~L): $\omega_{\mathrm{BPZ}}$
+\item Tier~(ii) (local $E_\infty$ with OPE poles, class~L): $\omega_{\mathrm{BPZ}}$
   exists, compact quantum group.
-\item Tier~(iii) (class~M): \textbf{no} fibre functor to
+\item Tier~(iii) (still local $E_\infty$, class~M): \textbf{no} fibre functor to
   $\mathrm{Hilb}$ can make the braiding unitary---the
   $A_\infty$ tower prevents it
   (Remark~\ref{rem:virasoro-qg-unitarity}).
@@ -15910,8 +15910,8 @@
 The descent from ordered to unordered is $R$-twisted:
 $B^{\mathrm{ch}}(\cA)_n \simeq
 (\bar{B}^{\mathrm{ord}}(\cA)_n)^{R\text{-}\Sigma_n}$.
-For pole-free $E_\infty$-chiral algebras (the
-BD-commutative subclass: no OPE singularities):
+For the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras (no OPE singularities):
 $R(z) = \tau$ (the flip), descent is trivial, both
 duals carry equivalent information.  For
 $E_\infty$-chiral algebras with OPE poles
@@ -15975,8 +15975,8 @@
 differential remains the sole gap.
 
 \medskip\noindent\textbf{When do the two duals agree?}\enspace
-When $\cA$ is pole-free $E_\infty$-chiral (the
-BD-commutative subclass): $R(z) = \tau$, descent is
+When $\cA$ lies in the pole-free BD-commutative subclass of
+$E_\infty$-chiral algebras: $R(z) = \tau$, descent is
 trivial, both duals carry equivalent information.
 
 \noindent\textbf{When do they disagree?}\enspace

tokens used
127,930
