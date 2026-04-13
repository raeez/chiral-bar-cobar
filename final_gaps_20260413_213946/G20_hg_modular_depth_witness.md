# G20_hg_modular_depth_witness (361s)

FIXED.

In [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:15237), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17061), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17130), and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17935), the AP219 surface now states unambiguously that the `d_{\mathrm{alg}}=2` `\beta\gamma` witness is the standard conformal-weight family `\beta\gamma_\lambda`, not the internal weight-changing line. The `T`-line and weight-changing line are both explicitly excluded as class `\mathbf{C}` witnesses, and the comparison witness at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:19646) was aligned to the same wording.

Verification: I re-read the touched passages and ran fixed-string greps to confirm there is no remaining reversal in this file placing the class `\mathbf{C}` witness on the weight-changing line. I did not run a full TeX build; this was a scoped wording/claim-surface correction only.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d88a1-3982-79e1-b575-756adddf72b4
--------
user
<task>
You are a FINAL GAPS agent. This is the LAST PASS. Every remaining gap must be closed.
832 agents have already run. You fix what they couldn't finish.
Read files on disk — they reflect ALL prior work. Be surgical. Be complete.
</task>
<action_safety>Keep changes scoped. After edits, re-read and verify. Grep for AP violations.</action_safety>
<completeness_contract>Fix EVERY issue in your scope. Report: FIXED or BLOCKED (with reason).</completeness_contract>
<verification_loop>After all edits, verify no new violations introduced.</verification_loop>


Verify depth gap betagamma witness in higher_genus_modular_koszul.tex (AP219).

NARROW SCOPE. Search for 'depth.*gap\|beta.*gamma.*d_alg\|class.*C.*witness' near lines 16400-16430 and 17100-17200.
Verify: the witness is on the STANDARD conformal-weight line (not weight-changing).
If the platonic agent P14 fixed it, verify the fix is correct.
mcp startup: no servers
codex
Using `multi-path-verify` for this pass because the task is a narrow claim verification with independent checks. I’m pulling the live claim surface first: the AP219 references in the repo constitution files, then the exact scope in `higher_genus_modular_koszul.tex`.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP219|depth gap|betagamma witness|class C witness|weight-changing|standard conformal-weight" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

 exited 2 in 52ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
CLAUDE.md:215:alpha_g = 2*rank + 4*dim*h^v (universal Hilbert-series growth, all simple types). d_alg in {0,1,2,inf} (depth gap: 3 impossible, prop:depth-gap-trichotomy). kappa(BP)+kappa(BP^!)=98/3 (self-dual k=-3).
CLAUDE.md:546:| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3. Betagamma d_alg=2 witness on standard conformal-weight line (corrected from weight-changing line where tower vanishes). Impossibility of 3 via MC relation + shadow Lie algebra Jacobi. ALT: representation-theoretic proof (H10). |
CLAUDE.md:1083:**Genuinely new (AP211-AP224):** AP211 (test file absent for compute engine, 219 findings), AP212 (TODO/FIXME unresolved), AP213 (stub chapter false coverage), AP214 (cross-volume bridge outdated after rectification), AP215 (preface/introduction advertising stronger than proved), AP216 (Koszul (vii) genus-0 scope), AP217 (Koszul (viii) ChirHoch freeness overclaim), AP218 (SC-formality proof restricted to families with metric), AP219 (depth-gap d_alg=2 witness on wrong line), AP220 (D^2=0 proof uses wrong geometric space), AP221 (Gerstenhaber bracket single insertion only), AP222 (Theorem H configuration-space collapse unjustified), AP223 (Theorem H bar-coalgebra/Koszul-dual conflation), AP224 (README scope inflation).
CLAUDE.md:1117:**Unconditional (high confidence):** Theorems A (fixed-curve), B (on-locus), C0 (D^co), C1 (g>=1), D (non-circular), H, MC1, MC2, MC4, SC-formality, depth gap, D^2=0, Theta_A existence, ChirHoch^1, 10 Koszul equivs, Verlinde recovery, ker(av), Miura coefficient, critical level jump, E_3 identification (simple g), chiral QG equiv, gl_N chiral QG.
metadata/theorem_registry.md:1007:| `prop:depth-gap-trichotomy` | `proposition` | 17787 | Algebraic depth gap: no $d_{\mathrm{alg}} = 3$ |
metadata/theorem_registry.md:1432:| `cor:betagamma-postnikov-termination` | `corollary` | 2132 | $\beta\gamma$ shadow obstruction tower: degree~$4$ on weight-changing line |
metadata/theorem_registry.md:1480:| `prop:betagamma-weight-line-shadows` | `proposition` | 1155 | $\beta\gamma$ shadow obstruction tower: weight-changing line |
chapters/connections/concordance.tex:5647: Gaussian on weight-changing line),
chapters/connections/concordance.tex:7222: & Algebraic depth gap:
chapters/connections/concordance.tex:9810:& Algebraic depth gap:
exec
/bin/zsh -lc 'rg -n "depth.*gap|beta.*gamma.*d_alg|class.*C.*witness|AP219" higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: higher_genus_modular_koszul.tex: IO error for operation on higher_genus_modular_koszul.tex: No such file or directory (os error 2)

thinking
**Locating file paths**

I need to find a file path, possibly under the chapters. I might need to read the archive for red team if there’s another path. It seems using the explorer agent could help me locate the file and its scope. So, let's go ahead and spawn the explorer to assist with that. I'm hopeful I can find what I need by exploring the right areas!
codex
The repo-level references already show AP219 was previously corrected conceptually: the surviving witness should be on the standard conformal-weight line. I’m locating the exact file path and local theorem surface now, then I’ll check whether the manuscript text and registry still agree.
collab spawn_agent(call_r8mSKarQieM1N4WVKEq44mu0, prompt="Locate the exact path for higher_genus_modular_koszul.tex and summarize the AP219-related local claim surface. Focus on …")
spawn_agent(call_r8mSKarQieM1N4WVKEq44mu0, prompt="Locate the exact path for higher_genus_modular_koszul.tex and summarize the AP219-related local claim surface. Focus on …") pending init:
  agent: 019d88a1-9f0a-7eb2-97df-44ed0b4bc9c2
mcp startup: no servers
exec
/bin/zsh -lc "sed -n '7200,7265p' chapters/connections/concordance.tex
sed -n '9790,9835p' chapters/connections/concordance.tex
sed -n '530,560p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg \"higher_genus_modular_koszul\\.tex"'$|red_team_summary'"\\.md"'$"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\ref{prop:shadow-tower-three-lenses}
 & Three equivalent descriptions of $S_r(\cA)$:
 algebraic (shadow), geometric (formality obstruction),
 holographic (boundary-bulk correction)
 & bar-intrinsic MC $+$ formality identification
 $+$ derived-centre factorization \\
\ref{def:generating-depth}
 & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
 $d_{\mathrm{alg}}$: formal distinction~;
 Virasoro $d_{\mathrm{gen}} = 3$,
 $d_{\mathrm{alg}} = \infty$
 & depth decomposition $+$ class~M tower non-termination \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: structural propositions and depth classification}} \\
\hline
\ref{prop:sc-formal-iff-class-g}
 & SC-formality characterises class~$\mathbf{G}$:
 $\cA$ is Swiss-cheese formal iff class~$\mathbf{G}$
 \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar

thinking
**Considering file inspections**

I need to wait for the explorer to finish. While I'm doing that, it might be a good idea to inspect the exact lines in the file. I plan to use the exec_command function for this task. There's also the thought of doing it in parallel, which could save some time. I'll figure out the best approach to ensure everything runs smoothly!
exec
/bin/zsh -lc "rg --files -g 'higher_genus_modular_koszul.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex
exec
/bin/zsh -lc 'rg -n "AP219" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

codex
The concordance and theorem status surface already say the corrected statement: the `d_alg=2` beta-gamma witness survives on the standard conformal-weight line, while the weight-changing line vanishes. I’m checking the actual chapter text around the cited ranges and the local witness construction now.
exec
/bin/zsh -lc "sed -n '16380,16440p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17080,17220p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item \emph{Quintic bracket and obstruction class.}
 On the primary line, the transferred bracket satisfies
 \begin{equation}\label{eq:ell5-explicit}
 \ell_5^{(0),\mathrm{tr}}
 (\Theta^{\leq 4},\, \Theta^{\leq 4},\,
 \Theta^{\leq 4},\, \Theta^{\leq 4},\,
 \Theta^{\leq 4})
 \;=\; S_5 \cdot e_5,
 \end{equation}
 where $e_5$ is the degree-$5$ basis vector in the
 shadow algebra. The obstruction class is
 \begin{equation}\label{eq:o5-obstruction}
 o_5(\cA)
 \;=\;
 S_5 \cdot e_5
 \;+\;
 \tfrac{1}{2}\ell_2^{(0)}
 (S_3 \cdot e_3,\, S_4 \cdot e_4)
 \;+\;
 (\text{lower-degree cross-terms}),
 succeeded in 52ms:
 \tfrac{10}{c(5c{+}22)}\,x^4$ are both non-vanishing, and
 $o_5(\mathrm{Vir}) = \{\mathfrak{C}, \mathfrak{Q}\}_{H} \neq 0$
 for generic~$c$
 \textup{(}Theorem~\textup{\ref{thm:w-virasoro-quintic-forced}}).
 The tower is infinite by induction on the all-degree master equation.
 For multi-generator algebras $\mathcal{W}_N$ ($N \geq 3$),
 diagonal non-autonomy at degree~$6$ is governed by the
 propagator variance
 \textup{(}Proposition~\textup{\ref{prop:propagator-variance}}):
 it vanishes at isolated curvature-proportionality loci in the
 central charge.
\end{enumerate}
Shadow depth is orthogonal to Koszulness: all archetypes are
chirally Koszul
\textup{(}Theorem~\textup{\ref{thm:modular-koszul-duality-main}}),
yet their shadow depths differ
\textup{(}Figure~\textup{\ref{fig:shadow-archetype-classification})}.
The shadow depth classifies the
complexity of $\Theta_\cA$, not whether the bar complex is acyclic.

exec
/bin/zsh -lc "rg -n \"betagamma|beta.?gamma|depth-gap|d_\\\\mathrm\\{alg\\}|d_{\\\\mathrm\\{alg\\}}|standard conformal-weight|weight-changing|class~\\\\mathbf\\{C\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:betagamma|beta.?gamma|depth-gap|d_\mathrm\{alg\}|d_{\mathrm\{alg\}}|standard conformal-weight|weight-changing|class~\mathbf\{C\})
                                         ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n "AP219" -n' in /Users/raeez/chiral-bar-cobar succeeded in 61ms:
CLAUDE.md:1083:**Genuinely new (AP211-AP224):** AP211 (test file absent for compute engine, 219 findings), AP212 (TODO/FIXME unresolved), AP213 (stub chapter false coverage), AP214 (cross-volume bridge outdated after rectification), AP215 (preface/introduction advertising stronger than proved), AP216 (Koszul (vii) genus-0 scope), AP217 (Koszul (viii) ChirHoch freeness overclaim), AP218 (SC-formality proof restricted to families with metric), AP219 (depth-gap d_alg=2 witness on wrong line), AP220 (D^2=0 proof uses wrong geometric space), AP221 (Gerstenhaber bracket single insertion only), AP222 (Theorem H configuration-space collapse unjustified), AP223 (Theorem H bar-coalgebra/Koszul-dual conflation), AP224 (README scope inflation).
mega_rescue_20260413_141327/M07_higher_genus_modular.md:54:Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g.
mega_rescue_20260413_141327/M19_free_fields.md:54:bc/bg: c_bc+c_bg=0. Verify signs (AP137). Verify betagamma depth gap witness (AP219). Cross-check with Friedan-Martinec-Shenker.
opus_audit_20260413_224154/OA4_depth_gap.md:622:f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
opus_audit_20260413_224154/OA4_depth_gap.md:642:f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
opus_audit_20260413_224154/OA4_depth_gap.md:650:    Depth gap impossibility of 3: two independent proofs (AP219 tightened)
resume_20260413_192632/M19_free_fields.md:54:bc/bg: c_bc+c_bg=0. Verify signs (AP137). Verify betagamma depth gap witness (AP219). Cross-check with Friedan-Martinec-Shenker.
resume_20260413_192632/M07_higher_genus_modular.md:54:Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g.
compute/audit/new_antipatterns_wave12_campaign.md:212:### AP219: Depth-gap d_alg=2 witness on wrong parameter line.
resume_20260413_165929/M07_higher_genus_modular.md:54:Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g.
resume_20260413_165929/M19_free_fields.md:54:bc/bg: c_bc+c_bg=0. Verify signs (AP137). Verify betagamma depth gap witness (AP219). Cross-check with Friedan-Martinec-Shenker.
elite_rescue_20260413_221642/L08_Livernet_comparison.md:95:f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
scripts/final_gaps_campaign.py:256:agent("G20_hg_modular_depth_witness", """Verify depth gap betagamma witness in higher_genus_modular_koszul.tex (AP219).
elite_rescue_20260413_221642/L07_KS_comparison.md:172:f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
elite_rescue_20260413_221642/L07_KS_comparison.md:1810:scripts/final_gaps_campaign.py:256:agent("G20_hg_modular_depth_witness", """Verify depth gap betagamma witness in higher_genus_modular_koszul.tex (AP219).
elite_rescue_20260413_221642/L07_KS_comparison.md:1813:scripts/mega_rescue_100.py:98:    ("M07_higher_genus_modular", "chapters/theory/higher_genus_modular_koszul.tex", "Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g."),
scripts/mega_rescue_100.py:98:    ("M07_higher_genus_modular", "chapters/theory/higher_genus_modular_koszul.tex", "Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g."),
scripts/mega_rescue_100.py:110:    ("M19_free_fields", "chapters/examples/free_fields.tex", "bc/bg: c_bc+c_bg=0. Verify signs (AP137). Verify betagamma depth gap witness (AP219). Cross-check with Friedan-Martinec-Shenker."),
elite_rescue_20260413_221642/L09_CFG_E3_comparison.md:90:f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
elite_rescue_20260413_221642/L10_GR_comparison.md:90:f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
exec
/bin/zsh -lc 'rg -n "depth.*gap" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
146: No other depths occur (Proposition~\ref{prop:depth-gap-trichotomy}):
17771:\index{depth gap!degree-4 MC obstruction}
17848:\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
17849:\label{prop:depth-gap-trichotomy}
17851:\index{algebraic depth!gap theorem|textbf}
17853:\index{depth classification!algebraic depth gap}
17856:\begin{equation}\label{eq:depth-gap}
17957:\begin{remark}[Structural content of the depth gap]
17958:\label{rem:depth-gap-shadow-lie-alternative}
17959:\index{shadow algebra!depth gap alternative proof}
17979:The depth gap is the shadow tower's sharpest structural
17987:\begin{remark}[Fine structure of the depth gap]
17988:\label{rem:depth-gap-fine-structure}
exec
/bin/zsh -lc "sed -n '17830,17930p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
so the degree-$6$ weight space is populated.
Applying $D_{\mathfrak{Q}}$ again:
$D_{\mathfrak{Q}}(x^6) = 24\,P\,S_4\,x^8 \neq 0$; then
$D_{\mathfrak{Q}}(x^{2m}) = 4 \cdot 2m \cdot P\,S_4\,x^{2m+2} \neq 0$
for all $m \geq 2$.
By induction, $S_4 \neq 0$ forces nonzero shadows at
all even degrees $\geq 6$.
In particular, the tower cannot terminate at any finite degree
$\geq 5$: once the quartic shadow survives, infinitely many successors
are forced.

The two arguments identify the same structural constraint:
$d_{\mathrm{alg}} \in \{0, 1\}$ (finite tower, $S_4 = 0$) or
$d_{\mathrm{alg}} = \infty$ ($S_4 \neq 0$, infinite tower) on any
$\kappa \neq 0$ primary line. The value $d_{\mathrm{alg}} = 3$
falls in neither class.
\end{proof}

\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
\label{prop:depth-gap-trichotomy}
collab wait(call_4b2UNMVyBWR1Z5VQ9xYGSsNb)
  receivers: 019d88a1-9f0a-7eb2-97df-44ed0b4bc9c2
exec
/bin/zsh -lc 'rg -n "standard conformal-weight" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "weight-changing" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
15240:The $T$-line is class~$\mathbf{M}$, while the weight-changing
15286:weight-changing line has zero shadow tower, so the
17060: The class-$\mathbf{C}$ witness is not the weight-changing line and
17127:(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
17933:one-dimensional internal slices. On the weight-changing line,
19299:${}^*$\,Stratum separation (Remark~\ref{rem:contact-stratum-separation}): $\kappa = 0$ on the weight-changing line; shadow metric not applicable.\\
exec
/bin/zsh -lc 'rg -n "class.*C.*witness" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
15242:class-$\mathbf{C}$ witness by itself.}
15287:class-$\mathbf{C}$ witness is the full family rather than either
17020: discriminant is not the class-$\mathbf{C}$ witness.}
17060: The class-$\mathbf{C}$ witness is not the weight-changing line and
17128:the class-$\mathbf{C}$ witness: its shadow tower vanishes and
17131:The $T$-line is also not the class-$\mathbf{C}$ witness:
17134:The class-$\mathbf{C}$ witness is the global conformal-weight family:
17939:The class-$\mathbf{C}$ witness is the full family:
exec
/bin/zsh -lc "sed -n '15180,15360p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
permanently feeds higher degrees
(Theorem~\ref{thm:w-virasoro-quintic-forced}).
\end{construction}

\begin{example}[Annals calibration table for the shadow obstruction tower]
\label{ex:shadow-calibration-table}
\index{shadow obstruction tower!calibration table|textbf}
\index{shadow archetype!calibration data}
The finite-order shadow data for the primitive archetypes and
extension families is collected in two tables: the shadow
projections~(A) and the termination mechanisms~(B).

\smallskip
\noindent
\textbf{Table~(A).\enspace Shadow obstruction tower projections.}
\nopagebreak
\begin{center}
\small
\renewcommand{\arraystretch}{1.35}
\begin{tabular}{@{}llcll@{}}
exec
/bin/zsh -lc "sed -n '16960,17240p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
to the Yangian coproduct that cannot be removed by gauge
transformation.
\end{remark}

\begin{example}[Shadow depth of all computed families]
\label{ex:shadow-depth-all-families}
\index{shadow depth!computed families}
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{llcccl}
\toprule
\emph{Family} &
\emph{Class} &
$d$ &
$d_{\mathrm{alg}}$ &
$\Delta$ &
\emph{Reference} \\
\midrule
Heisenberg $\cH_k$ &
exec
/bin/zsh -lc 'rg -n "conformal-weight line" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "conformal-weight" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
822:is the conformal-weight-$h$ piece of the augmentation ideal.
842:Therefore, relative to the ascending conformal-weight filtration on
874:Any class in a fixed bidegree has finite conformal-weight support by
1666:is the conformal-weight-$h$ piece of the Virasoro augmentation ideal.
12226:conformal-weight filtration within each fixed genus to compute bar
12262: spectral sequence) arises from the conformal-weight filtration
15237:{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
15281:For $\beta\gamma_\lambda$ on the global conformal-weight family,
17058: the conformal-weight family $\beta\gamma_\lambda$
17134:The class-$\mathbf{C}$ witness is the global conformal-weight family:
17864: conformal-weight family $\beta\gamma_\lambda$
17932:conformal-weight family $\beta\gamma_\lambda$, not by either of its
17944:vanishes on the conformal-weight family; and the charged quartic
18008: & conformal-weight family:\; charged quartic survives,\;
19587: on the conformal-weight family line;\;
19642:$r = 4$: on the global conformal-weight family,
21641:\textup{(}conformal-weight eigenvalue\textup{)}.
21809: \textup{(}$\mathbb{Z}_2$ parity, conformal-weight
22698:respect to the conformal-weight grading: if generators $\phi_a$
22739:refines Mechanism~2 by replacing the conformal-weight grading
wait(call_4b2UNMVyBWR1Z5VQ9xYGSsNb) timed out:

thinking
**Organizing pattern hit summary and references**

I'm gathering relevant file paths and line numbers for each regex pattern hit, aiming to summarize key claims about witnesses, depth gaps, and conformal-weight lines, while clarifying whether the text explicitly states that the class-C witness lies on the standard conformal-weight line. I'll structure the final response with bullet points referencing lines and file paths, noting interpretations about the “global conformal-weight family” and its relation to the standard conformal-weight line.
codex
The chapter proof already looks materially corrected: it explicitly rejects the weight-changing line and places the class `C` witness on the global conformal-weight family. I’m checking the supporting propositions around that claim so the surviving witness is really the standard line and not just renamed prose.
exec
/bin/zsh -lc 'rg -n -F "global conformal-weight family" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "weight-changing line" chapters/theory/higher_genus_modular_koszul.tex CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "standard conformal-weight" chapters/theory/higher_genus_modular_koszul.tex CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
15281:For $\beta\gamma_\lambda$ on the global conformal-weight family,
17134:The class-$\mathbf{C}$ witness is the global conformal-weight family:
19642:$r = 4$: on the global conformal-weight family,
 succeeded in 52ms:
CLAUDE.md:546:| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3. Betagamma d_alg=2 witness on standard conformal-weight line (corrected from weight-changing line where tower vanishes). Impossibility of 3 via MC relation + shadow Lie algebra Jacobi. ALT: representation-theoretic proof (H10). |
 succeeded in 52ms:
CLAUDE.md:546:| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3. Betagamma d_alg=2 witness on standard conformal-weight line (corrected from weight-changing line where tower vanishes). Impossibility of 3 via MC relation + shadow Lie algebra Jacobi. ALT: representation-theoretic proof (H10). |
metadata/theorem_registry.md:1432:| `cor:betagamma-postnikov-termination` | `corollary` | 2132 | $\beta\gamma$ shadow obstruction tower: degree~$4$ on weight-changing line |
metadata/theorem_registry.md:1480:| `prop:betagamma-weight-line-shadows` | `proposition` | 1155 | $\beta\gamma$ shadow obstruction tower: weight-changing line |
chapters/connections/concordance.tex:5647: Gaussian on weight-changing line),
chapters/theory/higher_genus_modular_koszul.tex:15286:weight-changing line has zero shadow tower, so the
chapters/theory/higher_genus_modular_koszul.tex:17060: The class-$\mathbf{C}$ witness is not the weight-changing line and
chapters/theory/higher_genus_modular_koszul.tex:17127:(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
chapters/theory/higher_genus_modular_koszul.tex:17933:one-dimensional internal slices. On the weight-changing line,
chapters/theory/higher_genus_modular_koszul.tex:19299:${}^*$\,Stratum separation (Remark~\ref{rem:contact-stratum-separation}): $\kappa = 0$ on the weight-changing line; shadow metric not applicable.\\
codex
**File:** `chapters/theory/higher_genus_modular_koszul.tex`

- **Depth-gap claim (AP219 surface)** — `:17848-17905`. Proposition \ref{prop:depth-gap-trichotomy} reiterates AP219: algebraic depth can only be \(0,1,2,\infty\) and the single-line Riccati argument plus global contact witness rule out \(d_{\mathrm{alg}}=3\) or higher on any primary line. The subsequent remarks/definition chain (e.g., Remark \ref{rem:depth-gap-fine-structure} at `:17957-17990`) frame the same constraint in terms of disallowed shadow depth values.

- **\(\beta\gamma\) and \(d_{\mathrm{alg}}=2\)** — `:17024-17085` and the earlier table footnote `:15234-15290`. Both the main text and the calibration table footnote stress that the full \(\beta\gamma_\lambda\) family is the unique \(d_{\mathrm{alg}}=2\) witness: the global conformal-weight family has \(S_2=6\lambda^2-6\lambda+1\), \(S_3=0\), \(S_4=-5/12\) and no higher shadows, so the quartic contact class is the last nonzero obstruction. The weight-changing slice and the \(T\)-line each fail to produce the correct \(S_r\), so they are expressly ruled out.

- **Class \(\mathbf{C}\) witness** — `:15240-15290`, `:17020-17140`, `:17933-17945`. The narrative repeatedly says that the class-\(\mathbf{C}\) witness is not any one-dimensional slice (neither \(T\)-line nor weight-changing line) but the entire global conformal-weight family (and its \(bc\) dual), with the charged quartic surviving while higher obstructions vanish by rank-one rigidity and stratum separation.

- **Standard conformal-weight line witness statement** — `:15237-15287`, `:17058-17078`. Yes: the local text already declares that the class-\(\mathbf{C}\) witness sits on the global conformal-weight family/line. That line is singled out as the “global conformal-weight family” (the standard conformal-weight line for \(\beta\gamma_\lambda\)), so no further relocation is needed.

- **Weight-changing line** — `:15240-15290`, `:17056-17140`. The weight-changing line’s shadow tower vanishes (\(\mu=0\)), so the text explicitly disqualifies it as the depth-gap witness; the global conformal-weight family remains the only valid \(d_{\mathrm{alg}}=2\) locus.

In short, the file gives the precise AP219 surface: depth-gap trichotomy plus the \(\beta\gamma\) family as the class‑\(\mathbf{C}\) witness, explicitly placing that witness on the standard/global conformal-weight line and excluding both the \(T\)-line and the weight-changing line.
exec
/bin/zsh -lc "sed -n '17040,17095p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '15240,15320p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
The $T$-line is class~$\mathbf{M}$, while the weight-changing
line has zero shadow tower, so neither one-dimensional slice is the
class-$\mathbf{C}$ witness by itself.}

\smallskip
\noindent
\textbf{Table~(B).\enspace Termination mechanisms.}
\nopagebreak
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{@{}clll@{}}
\toprule
\emph{Class} & $r_{\max}$
 & \emph{Termination identity}
 & \emph{Algebraic origin} \\
\midrule
$\mathbf{G}$ & $2$
 & $\ell_k^{\mathrm{tr}} = 0$,\; $k \geq 2$
 & strict coassociativity \\
 succeeded in 50ms:
primitive archetypes are as follows:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Gaussian \textup{(}$\mathbf{G}$,
$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
 Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
 All higher obstruction classes vanish:
 $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
 exactly quadratic.

\item \emph{Lie \textup{(}$\mathbf{L}$,
$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
 Affine Kac--Moody $V_k(\fg)$ at generic level.
 The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
 \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
 quartic obstruction $o_4 = 0$ by the Jacobi identity.

\item \emph{Contact \textup{(}$\mathbf{C}$,
$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
 the conformal-weight family $\beta\gamma_\lambda$
 \textup{(}and its $bc$ dual\textup{)}.
exec
/bin/zsh -lc "sed -n '17910,17970p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '19620,19670p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
$2\Delta\,t^2$ prevents $\sqrt{Q_L}$ from being polynomial.
The Taylor expansion of $\sqrt{Q_L(t)}$ about $t = 0$ has
infinitely many nonzero coefficients (the binomial series for
$(1 + u)^{1/2}$ with $u = (6\alpha\,t + (9\alpha^2 +
2\Delta)\,t^2)/(4\kappa^2)$ does not terminate when the
coefficient of~$t^2$ in~$u$ is nonzero).
Therefore $S_r \neq 0$ for infinitely many~$r$, and
$d_{\mathrm{alg}} = \infty$ (class~$\mathbf{M}$).

Thus no single primary line with $\kappa \neq 0$ can realize
$d_{\mathrm{alg}} = 2$ or~$3$.

The impossibility of $d_{\mathrm{alg}} = 3$ (and any finite
$d_{\mathrm{alg}} \geq 3$) on a $\kappa \neq 0$ line is
Lemma~\ref{lem:depth-three-impossible}: if $S_4 \neq 0$,
the MC recursion at degrees $5$ and $6$ forces a nonzero tail
regardless of whether $\alpha = 0$ or $\alpha \neq 0$, and the
closed form $H(t) = t^2\sqrt{Q_L(t)}$ with $\Delta \neq 0$ makes
the infinite extent manifest.

 succeeded in 52ms:
 is determined by finitely many shadow vanishings.
\end{enumerate}
\end{theorem}

\begin{proof}
(i)~Completeness follows from the recursive existence theorem
(Theorem~\ref{thm:recursive-existence}): the inverse limit
$\Theta_\cA = \varprojlim \Theta_\cA^{\leq r}$ exists in the
weight-completion $\widehat{\gAmod}$ and satisfies the full
Maurer--Cartan equation. Gauge equivalence propagates to the
completion by the Mittag-Leffler property of the weight
filtration: the transition maps
$F^r \gAmod \twoheadrightarrow F^{r-1} \gAmod$
are surjective (Lemma~\ref{lem:degree-cutoff}).

(ii)~$r = 3$: $\kappa(\cH_1) = 1 = \kappa(\mathrm{Vir}_2)$
by \S\ref{sec:heisenberg-shadow-gaussianity} and
\S\ref{sec:mixed-cubic-quartic-shadows}; but
$\mathfrak{C}_{\cH_1} = 0$
(class~$\mathbf{G}$, strict coassociativity) while

thinking
**Inspecting theorem details**

I need to look into the theorem about beta-gamma global depth and also check the proposition concerning the T-line and weight-changing line. I’ll want to search for relevant labels that might help clarify these concepts. There's a lot going on here, so I want to ensure I'm thorough in my examination to fully understand it. Let's see what I can find!
exec
/bin/zsh -lc 'rg -n -F "prop:betagamma-T-line-shadows" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:betagamma-global-depth" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
17133:\textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
17937:On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 succeeded in 52ms:
15289:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
16993: Thm~\ref{thm:betagamma-global-depth} \\[3pt]
17071: \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
17136:$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
17940:Theorem~\ref{thm:betagamma-global-depth} gives
19647:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
exec
/bin/zsh -lc 'rg -n -F "rem:contact-stratum-separation" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "cor:nms-betagamma-mu-vanishing" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
17073: Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
18256:(Remark~\ref{rem:contact-stratum-separation}).
19299:${}^*$\,Stratum separation (Remark~\ref{rem:contact-stratum-separation}): $\kappa = 0$ on the weight-changing line; shadow metric not applicable.\\
19403:\label{rem:contact-stratum-separation}
20603:(Remark~\textup{\ref{rem:contact-stratum-separation}}).
35473:Remark~\ref{rem:contact-stratum-separation}, and
 succeeded in 51ms:
14006:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}), but the quartic rigid
15290: Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
17072: Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
17130:\textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
17936:\textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
exec
/bin/zsh -lc "sed -n '16970,17030p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '13970,14020p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '19390,19425p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{tabular}{llcccl}
\toprule
\emph{Family} &
\emph{Class} &
$d$ &
$d_{\mathrm{alg}}$ &
$\Delta$ &
\emph{Reference} \\
\midrule
Heisenberg $\cH_k$ &
 $\mathbf{G}$ & $2$ & $0$ & $0$ &
 \S\ref{sec:heisenberg-shadow-gaussianity} \\
Lattice VOA $V_\Lambda$ &
 $\mathbf{G}$ & $2$ & $0$ & $0$ &
 Thm~\ref{thm:lattice:curvature-braiding-orthogonal} \\
Free fermion &
 $\mathbf{G}$ & $2$ & $0$ & $0$ &
 \S\ref{sec:heisenberg-shadow-gaussianity} \\[3pt]
$\hat{\fg}_k$ (generic) &
 $\mathbf{L}$ & $3$ & $1$ & $0$ &
 succeeded in 52ms:
\begin{equation}
\label{eq:primitive-shell-g3}
R_3(\mathfrak{K}_\cA)
\;=\;
\Delta_{\mathrm{ns}}(K_2)
\;+\;
[K_1, K_2]
\;+\;
\tfrac{1}{3!}\ell_3(K_1, K_1, K_1)
\;+\;
\sum_{\rho \in \operatorname{Rig}_2}
R_\rho^\cA(K_1)
\;+\;
\sum_{\rho \in \operatorname{Rig}_3}
R_\rho^\cA(K_{0,2}^\cA).
\end{equation}
\end{enumerate}
These formulas stratify by the primitive kernel regime:
\begin{center}
\begin{tabular}{lccc}
 succeeded in 50ms:
= 512/[3(5c{+}22)^2]$.
(v)~Immediate from the Gaussian
decomposition~\eqref{eq:gaussian-decomposition}
and Theorem~\ref{thm:single-line-dichotomy}.
\end{proof}

\begin{remark}[Affine shadow metric]
\label{rem:affine-shadow-metric}
\index{shadow metric!affine Kac--Moody}
For affine Kac--Moody $\hat{\fg}_k$: the quartic obstruction $o_4 = \frac{1}{2}\{\mathfrak{C},\mathfrak{C}\}_H$ vanishes by the Jacobi identity (Theorem~\ref{thm:shadow-archetype-classification}(ii)), giving $S_4 = 0$ and $\Delta = 0$. The shadow metric $Q_L = (2\kappa + 3\alpha t)^2$ is a \emph{perfect square}: $\sqrt{Q_L}$ is polynomial and the tower terminates at $r_{\max} = 3$. The shadow connection is trivial ($\omega = Q'/(2Q) = 3\alpha/(2\kappa+3\alpha t)$, regular everywhere), consistent with the finite depth.
\end{remark}

\begin{remark}[Stratum separation and the depth decomposition]
\label{rem:contact-stratum-separation}
\index{contact class!stratum separation}
\index{stratum separation|textbf}
\index{rank-one abelian rigidity!stratum separation}
The single-line dichotomy governs
$r_{\max}|_L \in \{2,3,\infty\}$. The value
$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full

thinking
**Searching for a theorem**

I need to locate the theorem called betagamma-global-depth. It might not be in the extracted lines I've reviewed so far, so I’ll try searching for it by starting with "begin theorem." I wonder if there's a specific source or document where I can find this theorem. Let’s see what I can uncover!
exec
/bin/zsh -lc "rg -n \"begin\\{theorem\\}.*betagamma-global-depth|label\\{thm:betagamma-global-depth\\}|global-depth|conformal-weight family\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
15281:For $\beta\gamma_\lambda$ on the global conformal-weight family,
15289:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
16993: Thm~\ref{thm:betagamma-global-depth} \\[3pt]
17058: the conformal-weight family $\beta\gamma_\lambda$
17071: \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
17134:The class-$\mathbf{C}$ witness is the global conformal-weight family:
17136:$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
17864: conformal-weight family $\beta\gamma_\lambda$
17932:conformal-weight family $\beta\gamma_\lambda$, not by either of its
17940:Theorem~\ref{thm:betagamma-global-depth} gives
17944:vanishes on the conformal-weight family; and the charged quartic
18008: & conformal-weight family:\; charged quartic survives,\;
19587: on the conformal-weight family line;\;
19642:$r = 4$: on the global conformal-weight family,
19647:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
exec
/bin/zsh -lc "sed -n '20540,20620p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\noindent
$\arg(t_0)/\pi \to 1$ as
$c \to \infty$ (semiclassical near-alternation).
At the Lee--Yang singularity $c = -22/5$: $\rho \to \infty$
and the branch points collide at $t = 0$.
The convergent regime $c > c_\star$ contains the
string-theoretic value $c = 26$; the divergent regime
$c < c_\star$ contains all unitary minimal models
($c < 1 \ll c_\star$).

For $\cW_3$ (two primary lines: $L_T$ at weight~$2$, $L_W$
at weight~$3$; see Example~\ref{ex:w3-two-line-shadow}),
the channel hierarchy is:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{rcccc}
\toprule
$c$ & $\rho_T$ & $\rho_W^{\mathrm{aut}}$
 & $\rho_T/\rho_W^{\mathrm{aut}}$ & T conv? \\
\midrule

thinking
**Inspecting theorem locations**

I need to check for the theorem or proof between 17850 and 18008. It could be somewhere in that range. I’m curious if I’ll find something interesting or important there. I should take a closer look at those areas to make sure I'm not missing anything valuable. Alright, let's explore those references and see what pops up!
exec
/bin/zsh -lc "sed -n '17840,18030p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '19570,19610p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Two chirally Koszul algebras with isomorphic shadow obstruction towers
 at all finite orders have gauge-equivalent universal MC
 classes.

\item \emph{Strict refinement.}
 At degrees $r = 3$ and $r = 4$, there exist chirally
 Koszul algebras $\cA$, $\cB$ with
 $[\Theta_\cA^{\leq r-1}] = [\Theta_\cB^{\leq r-1}]$
 but $[\Theta_\cA^{\leq r}] \neq [\Theta_\cB^{\leq r}]$.
 \begin{itemize}
 \item $r = 3$:
 $\kappa(\cH_1) = \kappa(\mathrm{Vir}_2) = 1$,\;
 $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
 \mathfrak{C}_{\mathrm{Vir}}$.
 \item $r = 4$:
 $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
 $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
 on the conformal-weight family line;\;
 $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
 = \mathfrak{Q}_{\beta\gamma_1}$.
 succeeded in 52ms:

The two arguments identify the same structural constraint:
$d_{\mathrm{alg}} \in \{0, 1\}$ (finite tower, $S_4 = 0$) or
$d_{\mathrm{alg}} = \infty$ ($S_4 \neq 0$, infinite tower) on any
$\kappa \neq 0$ primary line. The value $d_{\mathrm{alg}} = 3$
falls in neither class.
\end{proof}

\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
\label{prop:depth-gap-trichotomy}
\ClaimStatusProvedHere
\index{algebraic depth!gap theorem|textbf}
\index{shadow depth!forbidden values}
\index{depth classification!algebraic depth gap}
Let $\cA$ be a chirally Koszul algebra in the standard landscape.
Then the algebraic depth satisfies
\begin{equation}\label{eq:depth-gap}
 d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
\end{equation}
More precisely:

thinking
**Verifying depth gaps**

It seems my depth gap proposition is on the right track. I need to check for any local inconsistencies near target lines 16400-16430 and 17100-17200. I might want to search around line 16400, especially regarding witness statements. 

It’s possible that lines around 16400 aren't displaying due to insufficient sedation. The user mentioned this specific range, so I’ll need to inspect for local statements or references in the theorem or table. Continuing with lines 16400-16435 will be essential.
exec
/bin/zsh -lc "sed -n '16400,16440p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \end{equation}
 and the MC equation at degree~$5$ reads
 $o_5(\cA) = 0$ in $\cA^{\mathrm{sh}}$, which
 on the primary line is equivalent to the recursion
 $a_3 = -a_1 a_2/a_0$
 \textup{(}equation~\eqref{eq:convolution-higher-recursion}\textup{)}.
 The homotopy transfer theorem computes the bracket
 $\ell_5^{(0),\mathrm{tr}}$ via
 $C_4 = 14$ planar binary trees with $5$ leaves
 \textup{(}HPL route\textup{)}, equivalently via
 $C_5 = 42$ binary trees with $6$ leaves
 \textup{(}Feynman transform route\textup{)}, or via
 $(2 \cdot 6 - 5)!! = 105$ trivalent trees with $6$
 legs \textup{(}stable-graph route\textup{)}.

\item \emph{Sextic bracket and obstruction class.}
 Similarly,
 \begin{equation}\label{eq:ell6-explicit}
 \ell_6^{(0),\mathrm{tr}}
 (\Theta^{\leq 5}, \dotsc, \Theta^{\leq 5})
exec
/bin/zsh -lc "sed -n '16440,16490p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \midrule
 $\mathbf{G}$ \textup{(}Heisenberg\textup{)} &
 $0$ & $0$ &
 tower terminates at degree $2$ \\
 $\mathbf{L}$ \textup{(}affine KM\textup{)} &
 $0$ & $0$ &
 Jacobi kills degree $\geq 4$ \\
 $\mathbf{C}$ \textup{(}$\beta\gamma$\textup{)} &
 $0$ & $0$ &
 stratum separation at degree $5$ \\
 $\mathbf{M}$ \textup{(}Virasoro\textup{)} &
 $\neq 0$ & $\neq 0$ &
 $\Delta \neq 0$ forces $a_n \neq 0$ for all $n$ \\
 \bottomrule
 \end{tabular}
 \end{center}
 For Virasoro: the numerical values
 $S_5 = -48/(c^2(5c{+}22))$ and
 $S_6 = 80(45c{+}193)/(3\,c^3(5c{+}22)^2)$
 are both nonzero for all $c > 0$,

thinking
**Searching for theorems**

I'm looking at this table that uses beta gamma class C with a degree of stratum separation of 5. While it seems okay, it doesn't specify which line to check. I think I should verify if it's not changing the weight. I might need to search for specific labels and theorems related to global depth, possibly around line 17864. Maybe also looking into the "betagamma depth theorem" could help, so I'm considering inspecting lines near 13850 instead.
exec
/bin/zsh -lc 'rg -n -F "betagamma global" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n -F "global depth" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '13680,14120p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
The Euler characteristic filtration on the modular convolution algebra,
\begin{equation}
\label{eq:pronilpotent-filtration}
F^p \mathfrak{g}^{\mathrm{mod,log}}_\cA
\;:=\;
\prod_{2g - 2 + n \geq p}
\mathfrak{g}^{\mathrm{mod,log}}_\cA(g,n),
\end{equation}
is pronilpotent: $F^1$ is a pronilpotent Lie ideal, each quotient
$\mathfrak{g}^{\mathrm{mod,log}}_\cA / F^{p+1}$ is nilpotent,
and the inverse limit
$\mathfrak{g}^{\mathrm{mod,log}}_\cA =
\varprojlim_p\, \mathfrak{g}^{\mathrm{mod,log}}_\cA / F^{p+1}$
is a completed filtered dg Lie algebra. For fixed~$(g,n)$, the
stable-graph contribution to the Feynman transform is finite:
\begin{equation}
\label{eq:graph-finiteness}
|\{\Gamma \in \operatorname{StGr}(g,n)\}| < \infty,
\qquad
|V(\Gamma)| \leq 2g - 2 + n,

thinking
**Searching for theorem label**

I’m trying to locate the theorem `thm:betagamma-global-depth`, but it looks like I can’t find it. I wonder if the label isn't exactly right. Should I try searching for the label with some escape characters? I could also use a command like `rg -n "thm:betagamma-global-depth"` to check if it's just references that are missing. Maybe the theorem registry has the missing label? I should also look into the metadata for more clues.
exec
/bin/zsh -lc 'rg -n -F "thm:betagamma-global-depth" metadata/theorem_registry.md chapters/connections/concordance.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/theorem_registry.md:1481:| `thm:betagamma-global-depth` | `theorem` | 1182 | $\beta\gamma$ global shadow depth |
chapters/theory/higher_genus_modular_koszul.tex:15289:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
chapters/theory/higher_genus_modular_koszul.tex:16993: Thm~\ref{thm:betagamma-global-depth} \\[3pt]
chapters/theory/higher_genus_modular_koszul.tex:17071: \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
chapters/theory/higher_genus_modular_koszul.tex:17136:$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
chapters/theory/higher_genus_modular_koszul.tex:17940:Theorem~\ref{thm:betagamma-global-depth} gives
chapters/theory/higher_genus_modular_koszul.tex:19647:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.

thinking
**Searching for label locations**

I’m wondering why there’s no label location visible. Maybe the theorem is in an included file or the label is concealed by comments? I think I should try using `rg -F` to find the label too. There’s also a possibility that the label is located in a different file. It looks like I need to run `rg` across the entire repository to track it down. Let's keep exploring that option!
exec
/bin/zsh -lc "rg -n -F \"label{thm:betagamma-global-depth}\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:1182:\label{thm:betagamma-global-depth}

thinking
**Inspecting theorems and definitions**

I need to look into the theorem and definitions related to lines first. It seems important to verify if the class C witness is indeed on the standard conformal-weight line. The user has specifically requested this, while the text might mention a global conformal-weight family. Maybe the theorem refers to a global family that uses a standard parameter. I also want to check the free_fields theorem to see if it connects to higher genus.
codex
I found the actual witness theorem surface: `thm:betagamma-global-depth` lives in `chapters/examples/free_fields.tex`, not in the higher-genus chapter. I’m checking that source now, because the local chapter is only correct if the underlying theorem really proves the witness on the standard conformal-weight family rather than a weight-changing slice.
exec
/bin/zsh -lc "sed -n '1120,1235p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{prop:betagamma-T-line-shadows}
\index{beta-gamma system@$\beta\gamma$ system!T-line shadow data}
On the stress tensor line, the shadow obstruction tower of $\beta\gamma$ at
weight~$\lambda$ is
\begin{alignat}{2}
 S_2 &= \kappa(\beta\gamma) &&= 6\lambda^2 - 6\lambda + 1,
 \label{eq:bg-S2-Tline} \\
 S_3 &= \alpha &&= 2
 \quad \textup{(independent of~$\lambda$)},
 \label{eq:bg-S3-Tline} \\
 S_4 &= \frac{10}{c(5c+22)}
 &&= \frac{10}{2(6\lambda^2{-}6\lambda{+}1)
 \bigl(10(6\lambda^2{-}6\lambda{+}1)+22\bigr)},
 \label{eq:bg-S4-Tline}
\end{alignat}
and $S_r \neq 0$ for all $r \geq 2$.
The restriction to the T-line has infinite shadow depth
\textup{(}class~M on the one-dimensional slice\textup{)}.
\end{proposition}

exec
/bin/zsh -lc 'rg -n -F "weight-changing line" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "standard conformal-weight" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "conformal-weight family" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
82:weight-changing line (the global modular characteristic
712:is nonzero at generic $\lambda$, but on the weight-changing line
759:weight-changing line (cubic vanishes by rank-one abelian rigidity).
1089:\item \emph{The weight-changing line}: the deformation that shifts the
1153:\begin{proposition}[$\beta\gamma$ shadow obstruction tower: weight-changing line;
1156:\index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
1157:On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
1170:The weight-changing line satisfies the hypothesis of rank-one abelian
1191:The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
1211:weight-changing line because the Maurer--Cartan equation is linear there
5600:Shadow obstruction tower: on the one-dimensional weight-changing line all
 exited 1 in 51ms:

codex
There’s a live tension now: the higher-genus chapter says the surviving class `C` witness is the conformal-weight family, but the source theorem in `free_fields.tex` still describes a mixed charged stratum in the full two-channel space. I’m tracing the definition of the “standard conformal-weight line” to decide whether this is genuine inconsistency or just a naming mismatch.
exec
/bin/zsh -lc "rg -n -F \"standard conformal-weight line\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "conformal-weight line|conformal-weight family|weight-changing direction|mixed charged stratum|two-channel deformation space|standard line" chapters/examples/free_fields.tex chapters/theory/higher_genus_modular_koszul.tex chapters/geometry/beta_gamma*.tex chapters/**/beta* chapters/**/free*' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1210,1265p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1060,1115p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: no matches found: chapters/geometry/beta_gamma*.tex
 succeeded in 50ms:
\end{remark}

\subsection{\texorpdfstring{Shadow obstruction tower of the $\beta\gamma$ system}{Shadow obstruction tower of the beta-gamma system}}
\label{sec:betagamma-shadow-tower-free}
\index{shadow obstruction tower!beta-gamma@$\beta\gamma$!full tower}

The $\beta\gamma$ system is the unique free-field archetype outside the
Gaussian class. The full shadow obstruction tower is controlled by the
interaction between two primary directions in the modular cyclic
deformation complex (Definition~\ref{def:modular-cyclic-deformation-complex}),
and terminates at degree~$4$ by a stratum separation mechanism that has
no analogue for single-generator algebras.

\subsubsection{Multi-channel structure}
\label{sec:betagamma-multi-channel}

\begin{proposition}[$\beta\gamma$ deformation complex;
\ClaimStatusProvedHere]
\label{prop:betagamma-deformation-channels}
\index{beta-gamma system@$\beta\gamma$ system!deformation channels}
 succeeded in 50ms:
The cubic shadow $\mathfrak{C}_{\beta\gamma}$ vanishes on the
weight-changing line because the Maurer--Cartan equation is linear there
(Theorem~\ref{thm:betagamma-quartic-birth}).
On the T-line, $S_3 = 2 \neq 0$; the cubic is supported only on the
stress tensor direction.

\emph{Degree~$4$.}
The quartic contact shadow $Q^{\mathrm{contact}}_{\beta\gamma}$
is nontrivial on the charged stratum that mixes the T-line and
weight-changing directions
(Chapter~\ref{chap:beta-gamma},
Theorem~\ref{thm:betagamma-quartic-birth}).
The weight-changing-line projection
$\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
vanishes by rank-one abelian rigidity
(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
Hence the nonzero quartic class is genuinely mixed: it is invisible on
both isolated one-dimensional slices and appears only on the charged
stratum. The quartic contact class is the \emph{last} nontrivial global
shadow component.


thinking
**Searching for patterns**

I’m trying to figure out why my search command with globs failed due to shell expansion. Instead, I could use `rg` to look across the repo with simpler patterns. Maybe searching all `.tex` files for "standard conformal-weight line" will help, though it seems the user’s term might not match any exact phrases in the repo. I need to clarify what "standard conformal-weight line" means. It could refer to the "global conformal-weight family" or the variation within a one-dimensional family. It feels a bit complex!
thinking
**Reviewing the theorem proof**

I’m going through the proof where for degree 2, S2 equals kappa and is generally nonzero. For degree 3, the cubic shadow disappears on the weight-changing line, while on the T-line, S3 is 2, which is not zero. Moving to degree 4, the quartic exists on a charged stratum. For degree 5, the global bracket is zero. But can I conclude that global S3 equals 0? It seems like it may still exist on the T-line direction, which raises questions. I need to check if the higher genus statement holds.
codex
I found the key structural point in `free_fields.tex`: the source theorem still phrases the witness as a mixed charged stratum in the full two-channel deformation space. To validate the higher-genus wording, I need one more check: whether the global cubic is actually gauge-trivial, so the surviving class `C` witness can legitimately be summarized as the conformal-weight family with `S_3 = 0`, `S_4 ≠ 0`.
exec
/bin/zsh -lc 'rg -n -F "thm:cubic-gauge-triviality" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/free_fields.tex chapters/**/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:9373:(Theorem~\textup{\ref{thm:cubic-gauge-triviality}})
chapters/examples/free_fields.tex:284:(Theorem~\ref{thm:cubic-gauge-triviality}).
chapters/theory/higher_genus_modular_koszul.tex:14001:\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
chapters/theory/higher_genus_modular_koszul.tex:19655:Theorem~\ref{thm:cubic-gauge-triviality});
chapters/theory/higher_genus_modular_koszul.tex:21828:\textup{(}Theorem~\ref{thm:cubic-gauge-triviality}
chapters/theory/higher_genus_modular_koszul.tex:28892:\label{thm:cubic-gauge-triviality}
chapters/theory/higher_genus_modular_koszul.tex:28948:Theorem~\ref{thm:cubic-gauge-triviality} is the abstract
chapters/theory/higher_genus_modular_koszul.tex:30106: \textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality})}.
chapters/theory/higher_genus_modular_koszul.tex:30133:Part~(iii): by Theorem~\ref{thm:cubic-gauge-triviality},
chapters/theory/higher_genus_modular_koszul.tex:30550: produced by Theorem~\ref{thm:cubic-gauge-triviality}
chapters/examples/free_fields.tex:284:(Theorem~\ref{thm:cubic-gauge-triviality}).
chapters/theory/higher_genus_modular_koszul.tex:14001:\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
chapters/theory/higher_genus_modular_koszul.tex:19655:Theorem~\ref{thm:cubic-gauge-triviality});
chapters/theory/higher_genus_modular_koszul.tex:21828:\textup{(}Theorem~\ref{thm:cubic-gauge-triviality}
chapters/theory/higher_genus_modular_koszul.tex:28892:\label{thm:cubic-gauge-triviality}
chapters/theory/higher_genus_modular_koszul.tex:28948:Theorem~\ref{thm:cubic-gauge-triviality} is the abstract
chapters/theory/higher_genus_modular_koszul.tex:30106: \textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality})}.
chapters/theory/higher_genus_modular_koszul.tex:30133:Part~(iii): by Theorem~\ref{thm:cubic-gauge-triviality},
chapters/theory/higher_genus_modular_koszul.tex:30550: produced by Theorem~\ref{thm:cubic-gauge-triviality}
exec
/bin/zsh -lc "sed -n '700,820p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "cubic shadow.*vanish|cubic.*gauge-trivial|S_3 = 0|global cubic|charged quartic" chapters/examples/free_fields.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\subsection{\texorpdfstring{The $\beta\gamma$ system}{The beta-gamma system}}
\index{beta-gamma system|textbf}

\begin{remark}[Shadow archetype: contact/quartic]
\label{rem:betagamma-shadow-archetype-free}
\index{beta-gamma system@$\beta\gamma$ system!shadow archetype}
Shadow depth $r_{\max} = 4$ (class~C).
Modular characteristic $\kappa(\beta\gamma) = c/2 = 6\lambda^2 - 6\lambda + 1$,
where $\lambda$ is the conformal weight of $\gamma$.
Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
is nonzero at generic $\lambda$, but on the weight-changing line
$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
weight-changing slice tower vanishes. On the T-line, by contrast, the
recomputed one-dimensional tower is the Virasoro tower and has infinite
depth. The class~C witness on the full deformation space is the quartic
contact term on the mixed charged stratum:
$Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
Tower terminates at exactly $r = 4$ by
 succeeded in 52ms:
chapters/examples/free_fields.tex:214:shadow in a bosonic algebra, but fermionic statistics force $S_3 = 0$
chapters/examples/free_fields.tex:238: \textup{(}Consequence of $S_3 = 0$: no quartic contact term survives in the
chapters/examples/free_fields.tex:277:With $S_3 = 0$, the quartic contact invariant
chapters/examples/free_fields.tex:282:$S_3 = 0$ the obstruction class $o_4 = 0$
chapters/examples/free_fields.tex:284:(Theorem~\ref{thm:cubic-gauge-triviality}).
chapters/examples/free_fields.tex:290:implies $r_{\max} \leq 3$. With $S_3 = 0$, the tower terminates
chapters/examples/free_fields.tex:327:$S_3 = 0$ and $S_4 = 0$:
chapters/examples/free_fields.tex:1210:The cubic shadow $\mathfrak{C}_{\beta\gamma}$ vanishes on the
chapters/theory/higher_genus_modular_koszul.tex:3610:$\cW_3$ $\mathbb{Z}_2$-parity ($S_3 = 0$ kills
chapters/theory/higher_genus_modular_koszul.tex:14000:For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
chapters/theory/higher_genus_modular_koszul.tex:14001:\textup{(}Theorem~\textup{\ref{thm:cubic-gauge-triviality}}\textup{)},
chapters/theory/higher_genus_modular_koszul.tex:15220: & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
chapters/theory/higher_genus_modular_koszul.tex:15238:family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
chapters/theory/higher_genus_modular_koszul.tex:15282:the cubic shadow vanishes while the charged quartic survives:
chapters/theory/higher_genus_modular_koszul.tex:15283:$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
chapters/theory/higher_genus_modular_koszul.tex:17017: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
chapters/theory/higher_genus_modular_koszul.tex:17019: The charged quartic lies off the $T$-line, so the single-line
chapters/theory/higher_genus_modular_koszul.tex:17064:  S_3 = 0,\qquad
chapters/theory/higher_genus_modular_koszul.tex:17068: Thus the charged quartic contact class is nonzero and is the last
chapters/theory/higher_genus_modular_koszul.tex:17135:there the cubic shadow vanishes, the charged quartic survives with
exec
/bin/zsh -lc "rg -n \"conformal-weight line|standard conformal-weight|mixed charged stratum|charged stratum|quartic birth|weight-changing direction\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2860,2945p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"thm:betagamma-quartic-birth\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/beta_gamma.tex:2002:\section{The \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth and rank-one rigidity}
chapters/examples/beta_gamma.tex:2004:\index{beta-gamma system@$\beta\gamma$ system!quartic birth}
chapters/examples/beta_gamma.tex:2094:\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth;
chapters/examples/beta_gamma.tex:2097:\index{quartic birth!beta-gamma@$\beta\gamma$}
chapters/examples/beta_gamma.tex:2474:restricted to the weight-changing direction takes the form
chapters/examples/beta_gamma.tex:2710:$\mathfrak{Q}_{\beta\gamma}$ lives on the charged stratum
chapters/examples/beta_gamma.tex:2724:with the same composite Sugawara structure, but no charged stratum:
chapters/examples/y_algebras.tex:613:+ \partial J(w)(z-w)^{-1}$ is the standard conformal-weight-$1$
chapters/examples/free_fields.tex:80:contact shadow nontrivial on the charged stratum), even though
chapters/examples/free_fields.tex:717:contact term on the mixed charged stratum:
chapters/examples/free_fields.tex:760:The quartic contact shadow lives on the charged stratum mixing the
chapters/examples/free_fields.tex:1189:stratum coupling the T-line to the weight-changing direction; neither
chapters/examples/free_fields.tex:1218:is nontrivial on the charged stratum that mixes the T-line and
chapters/examples/free_fields.tex:1219:weight-changing directions
chapters/examples/free_fields.tex:1234:The quartic contact class lives on the charged stratum, while the cubic
chapters/examples/free_fields.tex:1239:The quartic contact class lives on a charged stratum whose
chapters/examples/free_fields.tex:1254:T-direction, the quartic contact lives on the charged stratum, and
chapters/examples/free_fields.tex:5607:the quartic contact class lives on a charged stratum whose
chapters/examples/landscape_census.tex:723:$\mathfrak{Q}^{\mathrm{contact}} \neq 0$ lives on a charged stratum.
chapters/examples/landscape_census.tex:1674: ($\kappa = 0$ on charged stratum)}} \\
 succeeded in 50ms:
chapters/examples/free_fields.tex:1212:(Theorem~\ref{thm:betagamma-quartic-birth}).
chapters/examples/free_fields.tex:1221:Theorem~\ref{thm:betagamma-quartic-birth}).
chapters/theory/higher_genus_modular_koszul.tex:17403:(Theorem~\ref{thm:betagamma-quartic-birth}).
chapters/examples/beta_gamma.tex:2076:Theorem~\ref{thm:betagamma-quartic-birth} and
chapters/examples/beta_gamma.tex:2096:\label{thm:betagamma-quartic-birth}
chapters/examples/beta_gamma.tex:2153:Combine Theorem~\ref{thm:betagamma-quartic-birth}
chapters/examples/beta_gamma.tex:2286:Theorem~\ref{thm:betagamma-quartic-birth} and the vanishing of the
chapters/examples/beta_gamma.tex:2701:$($Theorem~\textup{\ref{thm:betagamma-quartic-birth}}$)$.
chapters/examples/beta_gamma.tex:2734:Part~(ii) is Theorem~\ref{thm:betagamma-quartic-birth}: the
chapters/connections/arithmetic_shadows.tex:1860:(Theorem~\ref{thm:betagamma-quartic-birth}):
 succeeded in 50ms:
$\kappa(\cA) \in \mathbb{C}$. More precisely:

\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Universality.}
 \begin{enumerate}[label=\textup{(\alph*)}]
 \item \emph{Cohomological\textup{:}} The genus-$g$ obstruction class
 factors as
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 \textup{(}UNIFORM-WEIGHT\textup{}) in $H^{2g}(\overline{\mathcal{M}}_g)$ for all $g \geq 1$
 \textup{(}UNIFORM-WEIGHT; unconditional at $g = 1$\textup{)}.
 \end{enumerate}
 For multi-generator algebras \textup{(}$\mathcal{W}_N$ with
 $N \geq 3$\textup{)}, the genus-$1$ factorization is unconditional,
 while the higher-genus extension remains conditional on the
 strong scalar ansatz
 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
\item \emph{Generating function.}
 The genus free energies
 assemble as
 \begin{equation}\label{eq:modular-char-gf}
exec
/bin/zsh -lc "sed -n '2088,2148p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2460,2495p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2688,2738p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
to the moduli of deformations spanned by the class $\eta$ that shifts
conformal weight $\lambda \mapsto \lambda + \epsilon$.
\end{definition}

\subsection{Quartic birth}

\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth;
\ClaimStatusProvedHere]
\label{thm:betagamma-quartic-birth}
\index{quartic birth!beta-gamma@$\beta\gamma$}
On the weight/contact slice
(Definition~\textup{\ref{def:betagamma-weight-contact-slice}}), one has
\[
 \mathfrak{C}_{\beta\gamma} = 0,
 \qquad
 \mathfrak{o}_{\beta\gamma}^{(4)} = 0,
 \qquad
 \mathfrak{Q}_{\beta\gamma} = \operatorname{cyc}(m_3).
\]
Equivalently, the first nonlinear local shadow is quartic rather than
 succeeded in 52ms:
$\beta\gamma$~system has \emph{trivial quartic secondary Borcherds
operations}: $j'_{(p,q,r)} = 0$ for all $(p,q,r)$ on the
weight-changing line. Together with the nonvanishing cubic
($\ell_2^{\mathrm{tr}} \neq 0$ generically), the
$\beta\gamma$~system is a contact/quartic archetype: secondary Borcherds
operations are nonzero at degree~$3$ but vanish at degree~$4$, and the
shadow obstruction tower terminates at weight~$4$.
\end{proof}

\subsubsection{The complementarity potential on the weight line}
\label{sssec:betagamma-potential-weight-line}
\index{complementarity potential!beta-gamma weight line@$\beta\gamma$ weight line}

Assembling the preceding computations, the complementarity potential
restricted to the weight-changing direction takes the form
\begin{equation}\label{eq:betagamma-potential-weight-line}
 \mathfrak{S}_{\beta\gamma}(x)
 \;=\;
 \tfrac{1}{2}\,\langle \eta,\eta \rangle\, x^2
 \;+\;
 succeeded in 51ms:
$r_{\max} = \infty$ in class~$\mathsf{M}$ is absent.

\item[\textup{(ii)}]
\textbf{The Sugawara composite produces a nonzero quartic contact.}
The stress tensor
$T_\lambda = (1{-}\lambda)\normord{\beta\,\partial\gamma}
- \lambda\,\normord{(\partial\beta)\,\gamma}$
is a \emph{composite} field: it is not a generator of the vertex algebra
but a quadratic expression in the generators.
The $TT$ OPE has a quartic pole with coefficient
$c_{\beta\gamma}(\lambda)/2 = 6\lambda^2 - 6\lambda + 1$,
and the transferred operation $m_3$ inherits a nontrivial
quartic contact corolla $\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
$($Theorem~\textup{\ref{thm:betagamma-quartic-birth}}$)$.
This composite interaction is invisible at the generator level
but creates genuine shadow depth beyond degree~$3$.

\item[\textup{(iii)}]
\textbf{Stratum separation kills the quintic pump.}
The cyclic deformation complex decomposes by charge:

thinking
**Verifying statements**

I need to ensure I'm using evidence for my claims and possibly focus on a strong, truthful statement. It’s important to verify independent paths to reach a conclusion about whether the higher genus text is correct or if it should be adjusted. I might need to read the explorer summary as well, but I could also pause and wait before making any final decisions. Let's take a moment to reevaluate!
collab wait(call_Yvz731KyLA39ZESrkT5V83fY)
  receivers: 019d88a1-9f0a-7eb2-97df-44ed0b4bc9c2
wait(call_Yvz731KyLA39ZESrkT5V83fY) 1 agents complete:
  019d88a1-9f0a-7eb2-97df-44ed0b4bc9c2 completed: "**File:** `chapters/theory/higher_genus_modular_koszul.tex`

- **Depth-gap claim (AP219 surface)** — `:17848-17905`. Pro…"




thinking
**Clarifying terminology**

I need to ensure the text around lines 17100-17200 clearly states what's necessary. I’m also searching for the footnote around line 17017, which might be sufficient. But there's this distinction between "full family" and "line." If the user wants to verify the standard line without altering weights, I think the text should probably say "standard conformal-weight line" instead of "global conformal-weight family" for clarity. If I edit this, I must be cautious about mathematical correctness.
thinking
**Considering editing protocols**

I see that there's a Pre-Edit Verification Protocol required before making edits in hot zones. While AP219 isn't in the top 10 hot zones, it might still be relevant for scope quantification. Since it’s not a hot zone, the protocol may not be obligatory, but I should still consider using a PE-10 scope quantifier if I modify any propositions. It seems prudent to provide an update on any edits. Even though it’s just a local prose clarification, a verification note might be beneficial.
thinking
**Evaluating local edits**

I think I need to verify local duplicates after making edits, so I should locate all candidate lines in the file. Some mentions are around key points, such as "global conformal-weight family" and "conformal-weight family βγ_λ." I’m considering updating all mentions to "standard conformal-weight family" and clearly contrasting with internal weight-changing lines in a couple of main propositions. Since the user requested specific lines but there are duplicates, it makes sense to ensure consistency across the whole file if I’m touching those sections.
thinking
**Searching for repeated phrases**

I need to search for all occurrences of "global conformal-weight family" and "conformal-weight family βγ_λ" to patch any repeated phrases. It's important to ensure that I don’t have any awkward phrasing or excessive punctuation, like em dashes, that might confuse the reader. I want to keep the language clear and straightforward without over-editing the formulas. Simplifying the prose will help maintain clarity throughout the document.
codex
The local manuscript surface is substantively correct, but it is still ambiguous about which “conformal-weight” locus is meant. I’m making a surgical wording pass in `higher_genus_modular_koszul.tex` to spell out that the `d_alg=2` witness is the standard `\lambda`-family, not the internal weight-changing line.
exec
/bin/zsh -lc "sed -n '15210,15245p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '17052,17076p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '17130,17142p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '17928,17947p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '19638,19650p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 & $\mathbf{G}$ & $2$
 & $\operatorname{rank}\Lambda$
 & none \\[4pt]
Affine $\hat{\fg}_k$
 & $\mathbf{L}$ & $3$
 & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
 & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
 & $\mathbf{C}$ & $4$
 & $6\lambda^2 - 6\lambda + 1$
 & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
$\mathrm{Vir}_c$
 & $\mathbf{M}$ & $\infty$
 & $c/2$
 & $\mathfrak{C} = 2x^3$,\;
 $\mathfrak{Q}^{\mathrm{ct}}
 = \dfrac{10}{c(5c{+}22)}\,x^4$ \\[6pt]
$\mathcal{W}_N$ ($N \geq 3$)
 & $\mathbf{M}$ & $\infty$
 & $\kappa_{\mathcal{W}_N}\!(k)$
codex
I’m editing only the duplicated witness sentences in `higher_genus_modular_koszul.tex`. The formulas stay unchanged; the change is just to disambiguate that the surviving `d_alg=2` witness is the standard `\lambda`-family and explicitly not the internal weight-changing slice.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -15236,4 +15236,7 @@
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
@@ -17057,6 +17060,6 @@
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
@@ -17133,3 +17136,4 @@
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
@@ -17931,3 +17935,3 @@
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
@@ -17938,3 +17942,3 @@
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
@@ -17943,3 +17947,3 @@
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
@@ -19641,3 +19645,3 @@
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
apply_patch(auto_approved=true) exited 0 in 33ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..2991283e94a8dfdc8a43ea18fcb24dfdd68e9a84
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..2991283e94a8dfdc8a43ea18fcb24dfdd68e9a84
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and

codex
The edit is in place. I’m re-reading the touched passages and grepping the file for remaining AP219-style ambiguity so the witness language is consistent everywhere in this chapter.
exec
/bin/zsh -lc "rg -n -F \"global conformal-weight family\" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F \"standard conformal-weight family\" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F \"weight-changing line\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '15230,15295p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '17056,17080p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '17126,17142p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '17928,17947p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '19640,19649p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
15284:For $\beta\gamma_\lambda$ on the global conformal-weight family,
17061: the standard conformal-weight family $\beta\gamma_\lambda$
17137:The class-$\mathbf{C}$ witness is the standard conformal-weight family
17936:standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
19646:$r = 4$: on the standard conformal-weight family,
15240:weight-changing line in the deformation complex.
15289:weight-changing line has zero shadow tower, so the
17130:(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
17937:one-dimensional internal slices. On the weight-changing line,
19303:${}^*$\,Stratum separation (Remark~\ref{rem:contact-stratum-separation}): $\kappa = 0$ on the weight-changing line; shadow metric not applicable.\\
 succeeded in 51ms:
 & mixed cubic--quartic \\
\bottomrule
\end{tabular}
\end{center}

\smallskip
\noindent
{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
family $\beta\gamma_\lambda$:
this is the usual $\lambda$-family in the landscape, not the internal
weight-changing line in the deformation complex.
$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
The $T$-line is class~$\mathbf{M}$, while the weight-changing
line has zero shadow tower, so neither one-dimensional slice is the
class-$\mathbf{C}$ witness by itself.}

\smallskip
\noindent
\textbf{Table~(B).\enspace Termination mechanisms.}
exec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index b0aa08e..2991283 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3910,105 +3910,6 @@ argument. The universal MC element on the coinvariant modular
 convolution algebra is therefore proved in full generality.
 \end{theorem}
 
-\begin{remark}[Scope of MC2 in this chapter]
-\index{MC2!coinvariant scope}
-Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
-statement: its target dg~Lie algebra is
-$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
-The ordered lift
-$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
-\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
-Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
-Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
-therefore incorrect; the ordered theorem is
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..2991283e94a8dfdc8a43ea18fcb24dfdd68e9a84
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and

codex
One stale phrase is still left in the earlier summary paragraph. I’m aligning that last duplicate, then I’ll rerun the grep so the witness wording is uniform across the chapter.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -15283,3 +15283,3 @@
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma_\lambda$ on the global conformal-weight family,
+For $\beta\gamma_\lambda$ on the standard conformal-weight family,
 the cubic shadow vanishes while the charged quartic survives:
@@ -15289,3 +15289,3 @@
 weight-changing line has zero shadow tower, so the
-class-$\mathbf{C}$ witness is the full family rather than either
+class-$\mathbf{C}$ witness is the full standard $\lambda$-family rather than either
 one-dimensional slice
apply_patch(auto_approved=true) exited 0 in 32ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..dbb162fddd11e676ffac7779fc476884dcc6f76d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -15278,13 +15281,13 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma_\lambda$ on the global conformal-weight family,
+For $\beta\gamma_\lambda$ on the standard conformal-weight family,
 the cubic shadow vanishes while the charged quartic survives:
 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line restriction has an infinite tail, and the
 weight-changing line has zero shadow tower, so the
-class-$\mathbf{C}$ witness is the full family rather than either
+class-$\mathbf{C}$ witness is the full standard $\lambda$-family rather than either
 one-dimensional slice
 \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..dbb162fddd11e676ffac7779fc476884dcc6f76d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -15278,13 +15281,13 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma_\lambda$ on the global conformal-weight family,
+For $\beta\gamma_\lambda$ on the standard conformal-weight family,
 the cubic shadow vanishes while the charged quartic survives:
 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line restriction has an infinite tail, and the
 weight-changing line has zero shadow tower, so the
-class-$\mathbf{C}$ witness is the full family rather than either
+class-$\mathbf{C}$ witness is the full standard $\lambda$-family rather than either
 one-dimensional slice
 \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and

exec
/bin/zsh -lc "rg -n -F \"global conformal-weight family\" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F \"standard conformal-weight family\" chapters/theory/higher_genus_modular_koszul.tex
rg -n \"class-\\\\mathbf\\{C\\} witness.*weight-changing|weight-changing line.*class-\\\\mathbf\\{C\\} witness\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '15278,15291p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '17130,17140p' chapters/theory/higher_genus_modular_koszul.tex
sed -n '17934,17946p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
15284:For $\beta\gamma_\lambda$ on the standard conformal-weight family,
17061: the standard conformal-weight family $\beta\gamma_\lambda$
17137:The class-$\mathbf{C}$ witness is the standard conformal-weight family
17936:standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
19646:$r = 4$: on the standard conformal-weight family,
rg: regex parse error:
    (?:class-\mathbf\{C\} witness.*weight-changing|weight-changing line.*class-\mathbf\{C\} witness)
             ^^
error: unrecognized escape sequence
 succeeded in 51ms:
$\Theta_{\cH} = \kappa \cdot x^2$ (exactly quadratic).
For affine algebras, the cubic shadow
$\mathfrak{C}_{\mathrm{aff}} = \kappa(x,[y,z])$ is the
Lie bracket transported through the bar complex;
the Jacobi identity forces
$o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
For $\beta\gamma_\lambda$ on the standard conformal-weight family,
the cubic shadow vanishes while the charged quartic survives:
$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
The $T$-line restriction has an infinite tail, and the
weight-changing line has zero shadow tower, so the
class-$\mathbf{C}$ witness is the full standard $\lambda$-family rather than either
one-dimensional slice
(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
the class-$\mathbf{C}$ witness: its shadow tower vanishes and
$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
\textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
The $T$-line is also not the class-$\mathbf{C}$ witness:
it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..dbb162fddd11e676ffac7779fc476884dcc6f76d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -15278,13 +15281,13 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma_\lambda$ on the global conformal-weight family,
+For $\beta\gamma_\lambda$ on the standard conformal-weight family,
 the cubic shadow vanishes while the charged quartic survives:
 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line restriction has an infinite tail, and the
 weight-changing line has zero shadow tower, so the
-class-$\mathbf{C}$ witness is the full family rather than either
+class-$\mathbf{C}$ witness is the full standard $\lambda$-family rather than either
 one-dimensional slice
 \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and

codex
The chapter now reads consistently in all the repeated witness summaries. I’m doing one last fixed-string grep for the exact bad reversal so I can close this as verified rather than just edited.
exec
/bin/zsh -lc 'rg -n -F "class-$'"\\\\mathbf{C}"'$ witness is the weight-changing line" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F "class-$'"\\\\mathbf{C}"'$ witness is the global conformal-weight family" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff --unified=0 -- chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index b0aa08e..dbb162f 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3913,99 +3912,0 @@ convolution algebra is therefore proved in full generality.
-\begin{remark}[Scope of MC2 in this chapter]
-\index{MC2!coinvariant scope}
-Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
-statement: its target dg~Lie algebra is
-$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
-The ordered lift
-$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
-\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
-Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
-Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
-therefore incorrect; the ordered theorem is
-Theorem~\ref{thm:e1-mc-element}.
-\end{remark}
-
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..dbb162fddd11e676ffac7779fc476884dcc6f76d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -15278,13 +15281,13 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma_\lambda$ on the global conformal-weight family,
+For $\beta\gamma_\lambda$ on the standard conformal-weight family,
 the cubic shadow vanishes while the charged quartic survives:
 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line restriction has an infinite tail, and the
 weight-changing line has zero shadow tower, so the
-class-$\mathbf{C}$ witness is the full family rather than either
+class-$\mathbf{C}$ witness is the full standard $\lambda$-family rather than either
 one-dimensional slice
 \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and


thinking
**Confirming changes for diff command**

The diff command shows unrelated changes due to a dirty worktree—got it. I should focus on our specific changes in the final answer and not discuss unrelated diff details. It might be helpful to confirm the line numbers of our edits. I could use `nl -ba` to reference the touched lines and possibly use exec_command. I can include a file link without exact lines but will need to gather the precise line numbers after the patch.
codex
The exact bad reversal is gone. I’m grabbing final line references for the touched witness statements so the close-out is precise and confined to the scope you asked about.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15234,15292p'
nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17056,17140p'
nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17934,17946p'
nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '19642,19648p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 15234	
 15235	\smallskip
 15236	\noindent
 15237	{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
 15238	family $\beta\gamma_\lambda$:
 15239	this is the usual $\lambda$-family in the landscape, not the internal
 15240	weight-changing line in the deformation complex.
 15241	$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 15242	$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 15243	The $T$-line is class~$\mathbf{M}$, while the weight-changing
 15244	line has zero shadow tower, so neither one-dimensional slice is the
 15245	class-$\mathbf{C}$ witness by itself.}
 15246	
 15247	\smallskip
 15248	\noindent
 15249	\textbf{Table~(B).\enspace Termination mechanisms.}
 15250	\nopagebreak
 15251	\begin{center}
 15252	\small
 15253	\renewcommand{\arraystretch}{1.15}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..dbb162fddd11e676ffac7779fc476884dcc6f76d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -15278,13 +15281,13 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma_\lambda$ on the global conformal-weight family,
+For $\beta\gamma_\lambda$ on the standard conformal-weight family,
 the cubic shadow vanishes while the charged quartic survives:
 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line restriction has an infinite tail, and the
 weight-changing line has zero shadow tower, so the
-class-$\mathbf{C}$ witness is the full family rather than either
+class-$\mathbf{C}$ witness is the full standard $\lambda$-family rather than either
 one-dimensional slice
 \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and




thinking
**Verifying the theorem's consistency**

I want to mention that I've checked the underlying theorem in the chapter summary, and it's consistent regarding the vanishing weight-changing slice and the surviving quartic witness being the standard \(\lambda\)-family. I'll also note that the higher-genus chapter treats the C witness as part of the full standard \(\lambda\)-family and explicitly excludes the one-dimensional slices. Since the user asked about the witness verification, I can confirm it's on the standard \(\lambda\)-family and not the weight-changing slice. It might help to include the file link too.
thinking
**Creating clickable links**

I think it would be helpful to use clickable links with absolute paths and specific line numbers, maybe one or two links. If I include multiple links, I could refer to the same file with representative lines, like 17061, 17137, and 17935. This way, the user can easily navigate to those specific points in the document. I might include two or three links to make everything clearer. I’ll finalize that with a note saying "FIXED."
thinking
**Fixing the summary**

I checked the supporting theorem surface in `chapters/examples/free_fields.tex`, and now the higher-genus summary is clear about the locus in this chapter. I'm wondering if mentioning that is safe or if it might complicate things. Maybe I should omit it? I want to make sure I don’t start with "Done" but instead with "FIXED." It’s crucial that I keep my explanations concise, so I’m balancing clarity with brevity here.
codex
FIXED.

In [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:15237), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17061), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17130), and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17935), the AP219 surface now states unambiguously that the `d_{\mathrm{alg}}=2` `\beta\gamma` witness is the standard conformal-weight family `\beta\gamma_\lambda`, not the internal weight-changing line. The `T`-line and weight-changing line are both explicitly excluded as class `\mathbf{C}` witnesses, and the comparison witness at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:19646) was aligned to the same wording.

Verification: I re-read the touched passages and ran fixed-string greps to confirm there is no remaining reversal in this file placing the class `\mathbf{C}` witness on the weight-changing line. I did not run a full TeX build; this was a scoped wording/claim-surface correction only.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 12a3043fc07ed4ba0f7510f046154f2552f7bf19..dbb162fddd11e676ffac7779fc476884dcc6f76d
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15234,8 +15234,11 @@
 
 \smallskip
 \noindent
-{\footnotesize \textsuperscript{$\dagger$}Global conformal-weight
-family: $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
+{\footnotesize \textsuperscript{$\dagger$}Standard conformal-weight
+family $\beta\gamma_\lambda$:
+this is the usual $\lambda$-family in the landscape, not the internal
+weight-changing line in the deformation complex.
+$S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line is class~$\mathbf{M}$, while the weight-changing
 line has zero shadow tower, so neither one-dimensional slice is the
@@ -15278,13 +15281,13 @@
 Lie bracket transported through the bar complex;
 the Jacobi identity forces
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H = 0$.
-For $\beta\gamma_\lambda$ on the global conformal-weight family,
+For $\beta\gamma_\lambda$ on the standard conformal-weight family,
 the cubic shadow vanishes while the charged quartic survives:
 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
 The $T$-line restriction has an infinite tail, and the
 weight-changing line has zero shadow tower, so the
-class-$\mathbf{C}$ witness is the full family rather than either
+class-$\mathbf{C}$ witness is the full standard $\lambda$-family rather than either
 one-dimensional slice
 \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
  Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
@@ -17055,10 +17058,10 @@
 
 \item \emph{Contact \textup{(}$\mathbf{C}$,
 $d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
- the conformal-weight family $\beta\gamma_\lambda$
+ the standard conformal-weight family $\beta\gamma_\lambda$
  \textup{(}and its $bc$ dual\textup{)}.
- The class-$\mathbf{C}$ witness is not the weight-changing line and
- not the $T$-line: on the full family one has
+ The class-$\mathbf{C}$ witness is not the internal weight-changing
+ line and not the $T$-line: on the standard $\lambda$-family one has
  \[
   S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
   S_3 = 0,\qquad
@@ -17131,7 +17134,8 @@
 The $T$-line is also not the class-$\mathbf{C}$ witness:
 it has $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and infinite shadow depth
 \textup{(}Proposition~\textup{\ref{prop:betagamma-T-line-shadows}}\textup{)}.
-The class-$\mathbf{C}$ witness is the global conformal-weight family:
+The class-$\mathbf{C}$ witness is the standard conformal-weight family
+$\beta\gamma_\lambda$:
 there the cubic shadow vanishes, the charged quartic survives with
 $S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
 $S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
@@ -17929,19 +17933,19 @@
 
 \emph{Global contact witness.}
 The value $d_{\mathrm{alg}} = 2$ is realized by the
-conformal-weight family $\beta\gamma_\lambda$, not by either of its
+standard conformal-weight family $\beta\gamma_\lambda$, not by either of its
 one-dimensional internal slices. On the weight-changing line,
 all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian
 rigidity
 \textup{(}Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}}\textup{)}.
 On the $T$-line, Proposition~\ref{prop:betagamma-T-line-shadows}
 gives $S_3 = 2$, $S_4 = 10/[c(5c{+}22)]$, and an infinite tail.
-The class-$\mathbf{C}$ witness is the full family:
+The class-$\mathbf{C}$ witness is the full standard $\lambda$-family:
 Theorem~\ref{thm:betagamma-global-depth} gives
 $r_{\max} = 4$, hence $S_r = 0$ for $r \geq 5$;
 the degree-$2$ coefficient is
 $S_2 = 6\lambda^2 - 6\lambda + 1$; the cubic coefficient
-vanishes on the conformal-weight family; and the charged quartic
+vanishes on the standard $\lambda$-family; and the charged quartic
 is the nonzero constant $S_4 = -5/12$.
 Thus $d_{\mathrm{alg}}(\beta\gamma_\lambda) = 2$.
 The same statement holds for $bc_\lambda$ by the same
@@ -19639,7 +19643,7 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the global conformal-weight family,
+$r = 4$: on the standard conformal-weight family,
 $\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
 $\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
 while $\mathfrak{Q}_{\cH_1} = 0$ and

tokens used
93,511
