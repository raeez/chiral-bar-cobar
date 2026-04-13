# C03_bare_omega_v3 (257s)

1. PROBLEM at [chapters/connections/geometric_langlands.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38): the critical-level paragraph conflated `\kappa_{\mathrm{ch}}(V_{-h^\vee}) = 0` with the affine AP126 `r`-matrix convention, and it contained a broken parenthetical fragment.
EXACT edit applied: replaced the sentence with:
`At the critical level \kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0. In the AP126 trace-form convention the classical r-matrix is still r(z) = k\,\Omega/z, so at k = -h^\vee it is -h^\vee\,\Omega/z, not 0. The critical phenomenon is the vanishing of \kappa_{\mathrm{ch}} and the resulting shadow/center degeneration encoded by \Theta_A, not a level-stripped disappearance of the affine collision residue.`

2. PROBLEM at [chapters/connections/geometric_langlands.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:47): the Koszul-locus remark incorrectly said the critical-point issue comes from needing a nonvanishing `r`-matrix, which contradicts the AP126 trace-form convention.
EXACT edit applied: replaced
`because the standard proof goes through a nonvanishing r-matrix`
with
`because the shadow metric degenerates there even though the AP126 trace-form r-matrix remains nonzero`.

Verification: `pytest compute/tests/test_drinfeld_center_affine_km_engine.py -q -k 'test_ap126_trace_k0_vanishes or test_kz_critical_raises'` passed (`2 passed`), and `pytest compute/tests/test_geometric_langlands_shadow.py -q -k 'test_critical_level_value_sl2 or test_shadow_metric_critical_vanishes or test_verify_all_critical_kappa_zero'` passed (`3 passed`).


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/calabi-yau-quantum-groups
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d8791-fec7-7352-816d-51dba9771131
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


Same AP126 fix for Vol III.
mcp startup: no servers

thinking
**Inspecting surface differences**

I need to inspect the dirty surface's current differences before making any edits for the session entry. It looks like I should use a tool like rg for that. I want to ensure I read the skill file properly, too. I think using commentary updates will guide me as I proceed. Let's see how this goes! I'll take my time with it to make sure everything is accurate.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'pwd && rg -n "AP126|AP 126|AP-?126|same AP126|AP126 fix" .' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git status --short' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
---
name: vol3-beilinson-loop
description: Use when auditing, rectifying, falsifying, converging, or pressure-testing theorem, proof, formula, status, or scope material in the Calabi-Yau Quantum Groups repository. Trigger on audit, rectify, red-team, Beilinson, theorem status, proof gap, convergence, or "is this actually proved?" tasks.
---

# Vol III Beilinson Loop

Read `AGENTS.md` first. This skill is the triggered deep workflow for hostile mathematical review.

## Surface

Work on the live manuscript surface:

- `main.tex`
- currently `\input`-ed files
- the dirty git diff
- relevant build logs
- the narrowest relevant `compute/tests/` slice

## Passes
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups
./AGENTS.md:289:- Volume I is dominated by rectification, build-noise cleanup, formula/convention repair, compute/test synchronization, and repeated AP126/AP141, AP124/AP125, AP136, AP137, AP140, AP29, and AP128 failures. The SC^{ch,top} critical correction (AP165) and associated AP166-AP175 represent a major structural fix wave.
./AGENTS.md:779:- `AP19`, `AP44`, `V2-AP34`, `AP117`, `AP126`, `AP141`.
./chapters/theory/quantum_chiral_algebras.tex:405:where the coefficient $\Psi = -\sigma_2 = -(h_1 h_2 + h_1 h_3 + h_2 h_3)$ arises from the equivariant normalization of the propagator: the Omega-background twists the inner product on $\fgl_1$ by $-\sigma_2$ (which is the Kac--Moody level of the 5d theory on $\C^2 \times \R$, as in Costello~2013). In mode language: $J_{(1)} J = \Psi$, all other modes vanish. The classical $r$-matrix is $r^{\mathrm{Heis}}(z) = \Psi/z$ (C10; level prefix $\Psi$ mandatory, AP126). At $\Psi = 0$: the $r$-matrix vanishes (AP141).
./chapters/theory/quantum_chiral_algebras.tex:444: \item \emph{AP compliance} (4 tests): AP126 level prefix, AP141 vanishing at zero level, AP19 pole absorption, AP44 divided powers.
./compute/lib/drinfeld_center_heisenberg_bulk.py:106:  r-matrix: r^{Heis}(z) = k/z (AP126/C10: level prefix mandatory)
./compute/lib/drinfeld_center_heisenberg_bulk.py:318:    AP126 check: r(z)|_{k=0} = 0/z = 0.  PASS.
./compute/lib/drinfeld_center_heisenberg_bulk.py:639:    """AP126: r-matrix must vanish at k=0 (trace-form convention)."""
./compute/lib/drinfeld_center_affine_km_engine.py:106:    r-matrix trace-form: r(z) = k*Omega/z (AP126: level prefix mandatory)
./compute/lib/drinfeld_center_affine_km_engine.py:370:        AP126 check: r(z)|_{k=0} = 0. PASS.
./compute/lib/drinfeld_center_affine_km_engine.py:760:    r"""AP126: r-matrix has level prefix and vanishes at k=0 (trace-form)."""
./compute/lib/hcs_codim2_defect_ope.py:193:        (AP126, C10), the classical r-matrix is r(z) = Psi/z.
./compute/lib/hcs_codim2_defect_ope.py:245:    AP126 check: Psi = 0 => J(z)J(w) = 0 (degenerate).
./compute/tests/test_hcs_codim2_defect_ope.py:212:        AP126: level-stripped r-matrix FORBIDDEN.
./compute/tests/test_hcs_codim2_defect_ope.py:215:        # VERIFIED [DC] [LT] AP126/C10
./compute/tests/test_hcs_codim2_defect_ope.py:496:    def test_AP126_level_prefix(self):
./compute/tests/test_hcs_codim2_defect_ope.py:497:        """AP126: r-matrix has level prefix.
./compute/tests/test_drinfeld_center_affine_km_engine.py:11:    (7) r-matrix: trace-form k*Omega/z, KZ Omega/((k+2)z) (C9/AP126/AP148).
./compute/tests/test_drinfeld_center_affine_km_engine.py:315:        """AP126: r(z)|_{k=0} = 0 in trace-form convention."""
./compute/tests/test_drinfeld_center_affine_km_engine.py:606:        """AP126: trace-form r-matrix vanishes at k=0."""
 succeeded in 52ms:
 M calabi_yau_quantum_groups.pdf
 M chapters/connections/cy_holographic_datum_master.tex
 M chapters/connections/modular_koszul_bridge.tex
 M chapters/examples/fukaya_categories.tex
 M chapters/examples/quantum_group_reps.tex
 M chapters/examples/toric_cy3_coha.tex
 M chapters/examples/toroidal_elliptic.tex
 M chapters/frame/preface.tex
 M chapters/theory/braided_factorization.tex
 M chapters/theory/cy_categories.tex
 M chapters/theory/cy_to_chiral.tex
 M chapters/theory/drinfeld_center.tex
 M chapters/theory/e1_chiral_algebras.tex
 M chapters/theory/e2_chiral_algebras.tex
 M chapters/theory/introduction.tex
 M main.log
 M out/calabi_yau_quantum_groups.pdf
 M out/working_notes.pdf
 M working_notes.pdf



thinking
**Evaluating skill usage and fixes**

I need to announce my skill usage and the reasoning behind it. It's essential to provide a commentary update too. Since user mentioned the same AP126 fix for Vol III, I’ll apply this mandatory fix across those files. I need to audit within the assigned scope and inspect potentially problematic files. The search indicates only one manuscript file mentions AP126, so I should check for any missing fixes in the dirty files. I might also look for patterns related to r-matrix formulas in Vol III.
thinking
**Exploring AP126 fixes in Vol III**

The task mentions applying the same AP126 fix for Vol III, which could mimic fixes from Vol I or II. I should search for suspicious "Omega/z" without the k or "1/z" to check for missing levels. Since the safety action says to limit edits to assigned files, I'll consider all Vol III files that need AP126. I want minimal truthful edits, so I need to inspect the current diff or utilize git diff. I'll read relevant passages and search for specific formulas to understand any missing lines.
thinking
**Searching for missing formulas**

I need to search for any candidate missing formulas in the dirty files and the compute area. It sounds like using rg will be the best way to do this. I'll look for specific formulas that might be absent and make sure I'm thorough in my search. It’s important to ensure I don’t overlook anything that could be significant. I’ll keep focusing on those details to help the user effectively!
codex
Using `vol3-beilinson-loop` for a red-team pass on the Vol III AP126 surface. I’m locating every Vol III `r`-matrix/OPE statement that could still be level-stripped, then I’ll patch only the files that actually fail that check.
exec
/bin/zsh -lc "sed -n '360,470p' chapters/theory/quantum_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"r-matrix|r\\"'^'"\\{|r\\(z\\)|Omega/z|\\\\Omega/z|1/z|Psi/z|k\\\\*|level prefix|AP126\" chapters compute/tests compute/lib main.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/theory/quantum_chiral_algebras.tex compute/lib/drinfeld_center_heisenberg_bulk.py compute/lib/drinfeld_center_affine_km_engine.py compute/lib/hcs_codim2_defect_ope.py compute/tests/test_hcs_codim2_defect_ope.py compute/tests/test_drinfeld_center_affine_km_engine.py compute/tests/test_drinfeld_center_heisenberg_bulk.py' in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:

\begin{proof}
\emph{Step~1: restriction to the tubular neighborhood.}
The tubular neighborhood $U = \C_{z_1} \times D^2$ of $C$ in $Y = \C^3$ inherits the holomorphic $3$-form $\Omega|_U = dz_1 \wedge dz_2 \wedge dz_3$. The 6d holomorphic Chern--Simons action on $Y$ with gauge algebra $\fgl_1$:
\[
 S \;=\; \frac{1}{2}\int_Y \Omega \wedge \bigl(A \wedge \bar{\partial} A + \tfrac{2}{3}A \wedge A \wedge A\bigr)
\]
restricts to a free theory on $U$ because the cubic term vanishes for abelian $\fgl_1$.

\emph{Step~2: mode expansion in the normal directions.}
Expand the gauge field in modes of the normal bundle:
\[
 A(z_1, z_2, z_3, \bar{z}) \;=\; \sum_{m, n \geq 0} A^{(m,n)}(z_1, \bar{z}_1)\, z_2^m z_3^n.
\]
Each mode $A^{(m,n)}$ is a $(0,1)$-form on $C$ valued in $\fgl_1$. The Omega-background assigns equivariant weight $m \cdot h_2 + n \cdot h_3$ to $A^{(m,n)}$ under the torus $T^2 = \C^*_{z_2} \times \C^*_{z_3}$.

\emph{Step~3: integration over the normal fiber.}
Inserting the mode expansion into $S|_U$ and integrating the holomorphic $2$-form $dz_2 \wedge dz_3$ over the formal bidisk $D^2$ (extracting the $(0,0)$ Fourier coefficient of the product of normal modes), the action becomes:
\[
 S|_U \;=\; \sum_{m,n \geq 0} \int_C dz_1 \wedge A^{(m,n)} \bar{\partial} A^{(m,n)} \;+\; \text{(equivariant-weight terms from } \boldsymbol{h}\text{)}.
 exited 2 in 51ms:
rg: regex parse error:
    (?:r-matrix|r\^\{|r\(z\)|Omega/z|\Omega/z|1/z|Psi/z|k\*|level prefix|AP126)
                                     ^^
error: unrecognized escape sequence
 succeeded in 51ms:


thinking
**Rerunning search queries**

It seems like my previous search failed due to regex escaping issues, so I need to rerun some simpler queries. I should inspect AP126 and maybe see if other files are missing a prefix. It'd be helpful to compare this with previous fixes in other volumes and check the commit messages. I think I’ll try using “rg 'Omega/z'” in the chapters compute to make it more targeted and efficient.
codex
I’ve confirmed one Vol III manuscript surface already advertises the AP126 fix. Next I’m checking for the remaining level-stripped variants, especially bare `1/z` or `Omega/z` formulas that were not annotated or tested yet.
exec
/bin/zsh -lc "rg -n 'AP126|level prefix|vanishes at k=0|vanishes at Psi=0|trace-form' chapters compute/tests compute/lib" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Omega/z|\\\\Omega/z|= *1/z|= *\\\\frac\\{1\\}\\{z\\}|r\\(z\\) *=|r\\"'^'"\\{["'^}]+'"\\}\\(z\\) *=|classical \\\\"'$r'"\\\\"'$-matrix|level prefix'"' chapters compute/tests compute/lib" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/theory/introduction.tex chapters/theory/drinfeld_center.tex chapters/theory/e1_chiral_algebras.tex chapters/theory/e2_chiral_algebras.tex chapters/theory/braided_factorization.tex chapters/theory/cy_to_chiral.tex chapters/connections/cy_holographic_datum_master.tex chapters/connections/modular_koszul_bridge.tex chapters/examples/toroidal_elliptic.tex chapters/examples/quantum_group_reps.tex chapters/examples/toric_cy3_coha.tex chapters/examples/fukaya_categories.tex chapters/frame/preface.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/examples/quantum_group_reps.tex:127:Casimir $\Omega \in \frakg \otimes \frakg$ and level prefix $k$
chapters/examples/toroidal_elliptic.tex:2759:$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
chapters/theory/quantum_groups_foundations.tex:109:Passing from $U_q(\frakg)$ (finite type) to the affine quantum group $U_q(\hat{\frakg})$ at level $k$, Proposition~\ref{prop:qgf-classical-limit-r} acquires a level prefix: the classical limit produces
chapters/theory/quantum_chiral_algebras.tex:405:where the coefficient $\Psi = -\sigma_2 = -(h_1 h_2 + h_1 h_3 + h_2 h_3)$ arises from the equivariant normalization of the propagator: the Omega-background twists the inner product on $\fgl_1$ by $-\sigma_2$ (which is the Kac--Moody level of the 5d theory on $\C^2 \times \R$, as in Costello~2013). In mode language: $J_{(1)} J = \Psi$, all other modes vanish. The classical $r$-matrix is $r^{\mathrm{Heis}}(z) = \Psi/z$ (C10; level prefix $\Psi$ mandatory, AP126). At $\Psi = 0$: the $r$-matrix vanishes (AP141).
chapters/theory/quantum_chiral_algebras.tex:444: \item \emph{AP compliance} (4 tests): AP126 level prefix, AP141 vanishing at zero level, AP19 pole absorption, AP44 divided powers.
compute/lib/drinfeld_center_heisenberg_bulk.py:106:  r-matrix: r^{Heis}(z) = k/z (AP126/C10: level prefix mandatory)
compute/lib/drinfeld_center_heisenberg_bulk.py:318:    AP126 check: r(z)|_{k=0} = 0/z = 0.  PASS.
compute/lib/drinfeld_center_heisenberg_bulk.py:319:    AP141 check: no bare 1/z without level prefix.
compute/lib/drinfeld_center_heisenberg_bulk.py:331:        "convention": "trace-form",
compute/lib/drinfeld_center_heisenberg_bulk.py:639:    """AP126: r-matrix must vanish at k=0 (trace-form convention)."""
compute/lib/drinfeld_center_affine_km_engine.py:106:    r-matrix trace-form: r(z) = k*Omega/z (AP126: level prefix mandatory)
compute/lib/drinfeld_center_affine_km_engine.py:339:    For non-abelian KM (trace-form): av(r(z)) = k*dim(g)/(2h^v) = kappa_dp.
compute/lib/drinfeld_center_affine_km_engine.py:370:        AP126 check: r(z)|_{k=0} = 0. PASS.
compute/lib/drinfeld_center_affine_km_engine.py:386:            "convention": "trace-form",
compute/lib/drinfeld_center_affine_km_engine.py:760:    r"""AP126: r-matrix has level prefix and vanishes at k=0 (trace-form)."""
compute/lib/drinfeld_center_affine_km_engine.py:764:        "convention": "trace-form",
compute/lib/hcs_codim2_defect_ope.py:192:        of the W_{1+inf} defect algebra. In the trace-form convention
compute/lib/hcs_codim2_defect_ope.py:193:        (AP126, C10), the classical r-matrix is r(z) = Psi/z.
compute/lib/hcs_codim2_defect_ope.py:245:    AP126 check: Psi = 0 => J(z)J(w) = 0 (degenerate).
compute/tests/test_hcs_codim2_defect_ope.py:210:        """The r-matrix r^Heis(z) = Psi/z has the level prefix Psi.
 succeeded in 52ms:
chapters/examples/quantum_group_reps.tex:122: r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_{V_k(\frakg)})
chapters/examples/quantum_group_reps.tex:126:where $r(z) = \frac{k\,\Omega}{z} + O(1)$ is the classical $r$-matrix with
chapters/examples/quantum_group_reps.tex:127:Casimir $\Omega \in \frakg \otimes \frakg$ and level prefix $k$
chapters/examples/quantum_group_reps.tex:132:%: affine KM r-matrix at level k is k*Omega/z, not Omega/z.
chapters/examples/quantum_group_reps.tex:142: \item $r(z) = \frac{k\,\Omega}{z}$: the classical $r$-matrix at level $k$
chapters/examples/quantum_group_reps.tex:267:$r(z) = \frac{k\,\Omega}{z}$
chapters/examples/quantum_group_reps.tex:553:$R(z) = 1 + r(z) + O(r^2)$ where $r(z) = \frac{k\,\Omega}{z}$:
chapters/examples/quantum_group_reps.tex:560: $r(z) = \frac{k\,\Omega}{z} \mapsto \kappa_{\mathrm{cat}}$: the full
chapters/examples/toric_cy3_coha.tex:314:The collision residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
chapters/examples/toric_cy3_coha.tex:523:  $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{A_X})$,
chapters/examples/toric_cy3_coha.tex:584:$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
chapters/examples/toric_cy3_coha.tex:740:  $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}
chapters/examples/toric_cy3_coha.tex:762:$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{A_X})$
chapters/examples/toroidal_elliptic.tex:2759:$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
chapters/examples/toroidal_elliptic.tex:6051:The rational $r$-matrix $r(z) = k\,\Omega/z$ and the trigonometric
chapters/examples/toroidal_elliptic.tex:6052:$r$-matrix $r(z) = k\,\Omega \cdot \cot(z)$ both admit a single
chapters/examples/k3_times_e.tex:1059: residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$
compute/lib/affine_yangian_e1_cy3.py:75:       r(z) = Res^{coll}_{0,2}(Theta^{E_1}_{W_{1+inf}})
compute/lib/affine_yangian_e1_cy3.py:90:       r(z) = phi_3 / z^3 + phi_5 / z^5 + ... (odd poles only)
compute/lib/affine_yangian_e1_cy3.py:164:   Its arity-2 projection is the classical r-matrix r(z) = r_{12}(z1-z2).
 succeeded in 50ms:
diff --git a/chapters/connections/cy_holographic_datum_master.tex b/chapters/connections/cy_holographic_datum_master.tex
index 2a66e8a..b0ef346 100644
--- a/chapters/connections/cy_holographic_datum_master.tex
+++ b/chapters/connections/cy_holographic_datum_master.tex
@@ -943,7 +943,7 @@ Calabi--Yau chiral algebra, in seven CY-specific languages: CY
 bar-cobar, CoHA / perverse coherent sheaves, classical CY Poisson
 coisson, MO stable envelope, affine super Yangian for toric CY$_3$,
 elliptic Sklyanin for toroidal CY, Gaudin from CY$_3$
-(Theorem~\ref{thm:cy-seven-face-master} above).
+(Conjecture~\ref{conj:cy-seven-face-master} above).
 \end{enumerate}
 The three master theorems are mutually compatible: under the CY-to-chiral
 functor $\Phi$, face~$i$ of Vol~III maps to a specialization of face~$i$
diff --git a/chapters/connections/modular_koszul_bridge.tex b/chapters/connections/modular_koszul_bridge.tex
index 1199c5a..a423d35 100644
--- a/chapters/connections/modular_koszul_bridge.tex
+++ b/chapters/connections/modular_koszul_bridge.tex
@@ -234,7 +234,7 @@ Let $X = K3 \times E$, with chiral algebra $\cA_{K3} \otimes H_1$ (chiral de Rha
 \end{theorem}
 

thinking
**Searching formulas**

I need to search for all instances of `Omega/z` or `1/z` formulas in the manuscript. I've noticed that most of them have a kappa/k prefix, so I'll focus on those. I should also look for the compute code to see if there are any wrong comments related to it. Additionally, I want to search for `Omega/z` specifically without the prefix to ensure I capture everything needed. Let's get to it!
codex
The broad scan turned up one clearly suspicious Vol III sentence in `geometric_langlands.tex` that still mixes “critical level” with a malformed AP126 remark. I’m now reading that surface and nearby AP126-adjacent formulas to confirm whether it’s the only remaining truthful edit.
exec
/bin/zsh -lc "sed -n '1,120p' chapters/connections/geometric_langlands.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Omega/z|k\\\\,\\\\Omega/z|k\\\\*Omega/z|1/z|level-stripped|critical level|k\\+h|k \\+ h|AP148|AP126' chapters/connections chapters/theory chapters/examples | sed -n '1,220p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Omega/z|1/z|level-stripped|AP126|critical level' compute/lib compute/tests | sed -n '1,260p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\chapter{Geometric Langlands and CY Quantum Groups}
\label{ch:geometric-langlands}

The functor $\Phi$ of \ref{part:bridge} sends a Calabi--Yau category to an $\Etwo$-chiral algebra; the bar complex of the output (Volume~I, Theorem~A) is the factorization invariant on which geometric Langlands is ultimately a statement. This chapter traces the thread. At the critical level the Feigin--Frenkel theorem identifies the chiral center with the algebra of $G^L$-opers; the Verdier intertwining of Volume~I Theorem~A then relates local geometric Langlands to the four-functor picture (bar, cobar, Verdier, derived center). For Calabi--Yau input, the analogue is conjectural: a Langlands dual of a CY $d$-category should realize the mirror of its $\Phi$-image. The chapter is entirely FRONTIER material. Every formal statement uses \texttt{\textbackslash{}begin\{conjecture\}} unless it is a literal citation of Feigin--Frenkel (1992) or Frenkel--Gaitsgory (2006), in which case it is tagged \ClaimStatusProvedElsewhere.


% ============================================================
\section{The Feigin--Frenkel center at the critical level}
\label{sec:feigin-frenkel}
% ============================================================

Let $\frakg$ be a simple finite-dimensional complex Lie algebra and $\hat{\frakg}_k$ its affine Kac--Moody algebra at level $k$. The vacuum vertex algebra $V_k(\frakg)$ is the universal chiral algebra generated by the currents $J^a(z)$ with the Kac--Moody OPE. The \emph{critical level} is $k_c = -h^\vee$, where $h^\vee$ is the dual Coxeter number.

\begin{theorem}[Feigin--Frenkel, 1992]
\label{thm:feigin-frenkel-center}
\ClaimStatusProvedElsewhere{}
At the critical level $k = -h^\vee$, the center of the vacuum vertex algebra is canonically isomorphic to the algebra of functions on the space of $G^L$-opers on the formal disk:
\[
 \mathfrak{z}(\hat{\frakg}) \;:=\; Z(V_{-h^\vee}(\frakg)) \;\xrightarrow{\ \sim\ }\; \mathrm{Fun}\bigl(\mathrm{Op}_{G^L}(D)\bigr).
\]
 succeeded in 51ms:
chapters/examples/quantum_group_reps.tex:54: \item \emph{Root of unity $q = e^{\pi i/(k+h^\vee)}$} with
chapters/examples/quantum_group_reps.tex:118:$q = e^{\pi i/(k+h^\vee)}$, the degree-$(1,1)$ component of the
chapters/examples/quantum_group_reps.tex:132:%: affine KM r-matrix at level k is k*Omega/z, not Omega/z.
chapters/examples/quantum_group_reps.tex:164:$q = e^{\pi i/(k+h^\vee)}$, there is an equivalence of braided
chapters/examples/quantum_group_reps.tex:212:For a simple Lie algebra $\frakg$ and $q = e^{\pi i/(k+h^\vee)}$
chapters/examples/quantum_group_reps.tex:221: = \dim(\frakg) \cdot (k + h^\vee)/(2h^\vee)$, recovering the
chapters/examples/quantum_group_reps.tex:283: algebras; at the critical level $k = -h^\vee$, this produces
chapters/examples/quantum_group_reps.tex:465:$q = e^{\pi i/(k + h^\vee)}$, the modular characteristic of
chapters/examples/quantum_group_reps.tex:470: = \dim(\frakg) \cdot \frac{k + h^\vee}{2h^\vee}
chapters/examples/quantum_group_reps.tex:490:%: each formula recomputed from dim(g)(k+h^v)/(2h^v).
chapters/examples/quantum_group_reps.tex:525:where $q' = e^{\pi i/(k' + h^\vee)} = e^{-\pi i/(k + h^\vee)}$.
chapters/examples/quantum_group_reps.tex:537:= -\dim(\frakg)(k + h^\vee)/(2h^\vee)
chapters/connections/geometric_langlands.tex:4:The functor $\Phi$ of \ref{part:bridge} sends a Calabi--Yau category to an $\Etwo$-chiral algebra; the bar complex of the output (Volume~I, Theorem~A) is the factorization invariant on which geometric Langlands is ultimately a statement. This chapter traces the thread. At the critical level the Feigin--Frenkel theorem identifies the chiral center with the algebra of $G^L$-opers; the Verdier intertwining of Volume~I Theorem~A then relates local geometric Langlands to the four-functor picture (bar, cobar, Verdier, derived center). For Calabi--Yau input, the analogue is conjectural: a Langlands dual of a CY $d$-category should realize the mirror of its $\Phi$-image. The chapter is entirely FRONTIER material. Every formal statement uses \texttt{\textbackslash{}begin\{conjecture\}} unless it is a literal citation of Feigin--Frenkel (1992) or Frenkel--Gaitsgory (2006), in which case it is tagged \ClaimStatusProvedElsewhere.
chapters/connections/geometric_langlands.tex:8:\section{The Feigin--Frenkel center at the critical level}
chapters/connections/geometric_langlands.tex:12:Let $\frakg$ be a simple finite-dimensional complex Lie algebra and $\hat{\frakg}_k$ its affine Kac--Moody algebra at level $k$. The vacuum vertex algebra $V_k(\frakg)$ is the universal chiral algebra generated by the currents $J^a(z)$ with the Kac--Moody OPE. The \emph{critical level} is $k_c = -h^\vee$, where $h^\vee$ is the dual Coxeter number.
chapters/connections/geometric_langlands.tex:17:At the critical level $k = -h^\vee$, the center of the vacuum vertex algebra is canonically isomorphic to the algebra of functions on the space of $G^L$-opers on the formal disk:
chapters/connections/geometric_langlands.tex:24:The isomorphism is the content of Feigin--Frenkel (1992), with the full exposition in Frenkel's book \emph{Langlands Correspondence for Loop Groups} (2007). Off the critical level the center is trivial; at $k = -h^\vee$ it becomes a commutative vertex subalgebra of maximal size, and the resulting ind-scheme is $\mathrm{Op}_{G^L}(D)$.
chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
chapters/connections/geometric_langlands.tex:42:Let $A = V_{-h^\vee}(\frakg)$ and write $A^!$ for the Verdier-dual chiral algebra $D_{\mathrm{Ran}}(B(A))$ of Volume~I Theorem~A. At the critical level the chiral-algebra inclusion $\mathfrak{z}(\hat{\frakg}) \hookrightarrow A$, combined with the Feigin--Frenkel isomorphism of Theorem~\ref{thm:feigin-frenkel-center}, implies (does not iff) the existence of a factorization-coalgebra map $\mathrm{Fun}(\mathrm{Op}_{G^L}(D)) \to B(A^!)$ on $\mathrm{Ran}(X)$. The conjecture is that this map is a quasi-isomorphism on the Volume~I Koszul locus. This is a statement about the Verdier leg of the four-functor picture, not about the inversion leg $\Omega \circ B$.
chapters/connections/geometric_langlands.tex:47:\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 succeeded in 51ms:
compute/lib/k3_yangian.py:709:    # r_{ii} = -2 * h_i  (coefficient of 1/z in (z-h)/(z+h))
compute/lib/e2_bar_complex.py:421:        """Classical r-matrix r(z) = Omega/(k+h^v) * 1/z.
compute/lib/e2_bar_complex.py:432:        return ("Omega/z", 1 / kh)
compute/tests/test_coha_non_cy_threefold.py:725:        The CY3 symmetry zeta_{ij}(z)*zeta_{ji}(1/z)=1 requires the
compute/tests/test_coha_non_cy_threefold.py:732:        i=j and the kernel is trivially symmetric: zeta_{00}*zeta_{00}(1/z)
compute/tests/test_coha_non_cy_threefold.py:744:        # Single vertex: zeta_{00}(z)*zeta_{00}(1/z) involves same exponent
compute/lib/e2_koszul_heisenberg.py:57:  R-matrix: R^{E_2}(z) = k*Omega/z + O(1)
compute/lib/e2_koszul_heisenberg.py:149:    (3) Koszul dual has R^{E_2,!}(z) = -k*Omega/z = braiding reversal.
compute/lib/e2_koszul_heisenberg.py:256:        Since the R-matrix is R = 1 + k*Omega/z + ..., inverting k
compute/lib/e2_koszul_heisenberg.py:257:        gives R^{-1} = 1 - k*Omega/z + ..., which is exactly the
compute/tests/test_drinfeld_center_heisenberg_bulk.py:18:    [LC] k=0: r-matrix vanishes (AP126), kappa=0 (C1), bracket degenerates
compute/tests/test_drinfeld_center_heisenberg_bulk.py:231:        """AP126: r(z) vanishes at k=0 (trace-form convention)."""
compute/tests/test_drinfeld_center_heisenberg_bulk.py:454:        """AP126: r-matrix vanishes at k=0 (trace-form convention)."""
compute/tests/test_geometric_langlands_shadow.py:8:  - Shadow connection degeneration at critical level
compute/tests/test_geometric_langlands_shadow.py:216:    """Verify kappa vanishing at critical level k = -h^v."""
compute/tests/test_geometric_langlands_shadow.py:271:        """Sugawara c is None at critical level for sl_2."""
compute/tests/test_geometric_langlands_shadow.py:276:        """Sugawara c is None at critical level for sl_3."""
compute/tests/test_geometric_langlands_shadow.py:364:            assert k_dual == k_crit, f"{t}{r}: critical level not fixed by FF"
compute/tests/test_geometric_langlands_shadow.py:483:    """Shadow connection degeneration at critical level."""
compute/tests/test_geometric_langlands_shadow.py:493:        """Shadow metric vanishes at critical level (kappa = 0)."""
codex
The critical-level surface is worse than a typo: it currently leaves the AP126 convention ambiguous exactly where Vol III distinguishes `κ_ch = 0` from the affine trace-form `r(z)`. I’m checking the compute witness for that chapter so the manuscript edit matches the live convention instead of papering over it.
exec
/bin/zsh -lc "sed -n '880,980p' compute/tests/test_geometric_langlands_shadow.py" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/geometric_langlands_shadow.py" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
        for key, val in results.items():
            if key.startswith('kappa_critical_'):
                assert val['is_zero'], f"{key}: kappa = {val['kappa']}"

    def test_verify_all_ff_antisymmetric(self):
        """All FF entries in verify_all are antisymmetric."""
        results = verify_all()
        for key, val in results.items():
            if key.startswith('ff_'):
                assert val['antisymmetric'], f"{key} failed"

    def test_full_computation_runs(self):
        """full_computation() runs without error."""
        result = full_computation()
        assert 'verification' in result
        assert 'critical_tower_sl2' in result
        assert 'opers_sl2_g2' in result
        assert 'so5_sp4' in result
        assert 'kw_sl2' in result
        assert 'hitchin_sl2_g2' in result
 succeeded in 52ms:
r"""Geometric Langlands programme from shadow obstruction towers.

The geometric Langlands correspondence relates:
  - D-modules on Bun_G(X) (moduli of G-bundles on a curve X)
  - Quasi-coherent sheaves on LocSys_{G^v}(X) (local systems for Langlands dual)

The bar-cobar framework of Vol I produces this structure via the shadow
tower of the affine algebra g_hat_k at and near the CRITICAL LEVEL k = -h^v.

CRITICAL LEVEL ANALYSIS
========================

The modular characteristic for affine Kac-Moody is:

    kappa(g_hat_k) = dim(g) * (k + h^v) / (2 * h^v)

At the critical level k = -h^v:
    kappa(g_hat_{-h^v}) = dim(g) * 0 / (2 * h^v) = 0.

The bar complex becomes UNCURVED (d^2 = 0 on the nose). This is the algebraic
exec
/bin/zsh -lc "sed -n '100,140p' chapters/theory/quantum_groups_foundations.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
at order $\hbar^2$.
\end{proposition}

\begin{proof}[Attribution]
Drinfeld, ``Hamiltonian structures on Lie groups, Lie bialgebras and the geometric meaning of classical Yang--Baxter equations'' (Soviet Math.\ Dokl.\ 1983); Drinfeld (1986), Theorem~3.
\end{proof}

\begin{remark}[cross-volume check: level-stripped $r$-matrix]
\label{rem:qgf-ap126-level-check}
Passing from $U_q(\frakg)$ (finite type) to the affine quantum group $U_q(\hat{\frakg})$ at level $k$, Proposition~\ref{prop:qgf-classical-limit-r} acquires a level prefix: the classical limit produces
\begin{equation}
 r(z) = k \cdot \frac{\Omega_{\frakg}}{z} + O(\hbar, z^0),
 \label{eq:qgf-r-level-k}
\end{equation}
matching the Vol~I and Vol~II convention. Two sanity checks, mandatory after writing any $r$-matrix formula:
\begin{enumerate}[label=(\alph*)]
 \item At $k = 0$: the level-zero limit collapses the affine algebra to a loop algebra whose invariant form is identically zero, the classical $r$-matrix vanishes ($r(z) = 0$), and the universal $R$-matrix reduces to the identity $\cR(z) = 1$. This matches $\kappa_{\mathrm{ch}}^{\mathrm{KM}} = \dim(\frakg)(k + h^\vee)/(2 h^\vee) |_{k=0} = \dim(\frakg)/2$ reflected through the residue at $k = 0$ of the coefficient.
 \item At $k = -h^\vee$ (the critical level): $\kappa_{\mathrm{ch}}^{\mathrm{KM}}$ vanishes, the $R$-matrix degenerates, and the quantum group collapses to the classical enveloping algebra of the loop algebra. This is the Feigin--Frenkel regime.
\end{enumerate}
This principle caught repeated level-stripped affine pole terms; both (a) and (b) must be verified whenever an affine $r$-matrix is written.

thinking
**Investigating propagation of fixes**

I need to check if the "same AP126 fix" should apply to all instances like quantum_groups_foundations.tex and geometric_langlands.tex, and possibly others, including compute docs. I'll search for statements that claim r vanishes or degenerates in trace form. My initial findings show that in quantum_groups_foundations, there's a remark about the R-matrix degenerating at critical levels. I should look for more files containing "At k = -h^v: r(z) = ..." and refine my search around "critical level.*r-matrix." Let's focus on that.
codex
The compute witness confirms the key distinction: `κ_ch` vanishes at the critical level, but AP126 is still about the affine trace-form `r(z)=kΩ/z`, not a level-stripped pole. I’m doing one more pass for other Vol III sentences that still incorrectly collapse those two facts together before I edit.
exec
/bin/zsh -lc "sed -n '100,140p' chapters/examples/quantum_group_reps.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '260,300p' chapters/examples/quantum_group_reps.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'critical level.*r-matrix|r-matrix.*critical level|level-stripped|R-matrix degenerates|r\\(z\\) = 0|vanishes at k = -h|vanishes at the critical level|critical level.*Omega/z|critical level.*k\\\\,\\\\Omega/z' chapters compute/lib compute/tests" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
\[
 Y(\frakg) = \langle r^{\mathrm{coll}}(z) \rangle_{\mathrm{RTT}}
\]
where the RTT relation is the degree-$(1,1,1)$ bar differential.
This is the content of Volume~II, MC3: the ordered bar complex
$B^{\mathrm{ord}}(V_k(\frakg))$ produces the Yangian as the
universal algebra generated by the modes of
$r(z) = \frac{k\,\Omega}{z}$
.
\end{proposition}

\begin{remark}[Three distinct operations]
\label{rem:three-operations}
% restated for clarity.
The following three operations on quantum groups must never be
conflated:
\begin{enumerate}[label=(\alph*)]
 \item \emph{Koszul duality}:
 $V_k(\frakg) \mapsto V_k(\frakg)^!$, the Koszul dual vertex
 algebra involving the dual level
 succeeded in 51ms:
= (k+2)/(2\sin^2(\pi/(k+2)))$.
The $S$-matrix entries are
$S_{mn} = \sqrt{2/(k+2)} \, \sin(\pi(m+1)(n+1)/(k+2))$.
This is a modular tensor category: the Reshetikhin--Turaev functor
produces the $SU(2)$ Chern--Simons invariants of 3-manifolds.
\end{example}


\section{The $R$-matrix as categorical $r(z)$}
\label{sec:r-matrix-categorical}

The $R$-matrix of $\Uq(\frakg)$ is the categorical incarnation of
the collision residue $r(z)$ from the Volume~I bar complex.

\begin{proposition}[$R$-matrix from bar degree $(1,1)$]
\label{prop:r-matrix-bar}
\ClaimStatusProvedElsewhere
For the affine vertex algebra $V_k(\frakg)$ at level $k$ with
$q = e^{\pi i/(k+h^\vee)}$, the degree-$(1,1)$ component of the
ordered bar complex $B^{\mathrm{ord}}(V_k(\frakg))$ recovers the
 succeeded in 51ms:
chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
chapters/theory/quantum_groups_foundations.tex:107:\begin{remark}[cross-volume check: level-stripped $r$-matrix]
chapters/theory/quantum_groups_foundations.tex:116: \item At $k = 0$: the level-zero limit collapses the affine algebra to a loop algebra whose invariant form is identically zero, the classical $r$-matrix vanishes ($r(z) = 0$), and the universal $R$-matrix reduces to the identity $\cR(z) = 1$. This matches $\kappa_{\mathrm{ch}}^{\mathrm{KM}} = \dim(\frakg)(k + h^\vee)/(2 h^\vee) |_{k=0} = \dim(\frakg)/2$ reflected through the residue at $k = 0$ of the coefficient.
chapters/theory/quantum_groups_foundations.tex:119:This principle caught repeated level-stripped affine pole terms; both (a) and (b) must be verified whenever an affine $r$-matrix is written.
compute/lib/twisted_holography_cy3_engine.py:784:    At the self-dual point (h2 = 0): r(z) = 0 (Heisenberg), so the
compute/tests/test_hcs_codim2_defect_ope.py:212:        AP126: level-stripped r-matrix FORBIDDEN.
compute/lib/drinfeld_center_affine_km_engine.py:783:    Trace-form at k=0: r(z) = 0 (vanishes).
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
---
name: vol3-pre-edit-verification
description: Use before editing any high-risk Vol III formula, theorem status, d=3 existence claim, compute oracle, or cross-volume convention bridge. This is the Codex-native analogue of the Claude-side pre-edit verification templates.
---

# Vol III Pre-Edit Verification

Before editing a high-risk surface, fill in a fenced `PRE-EDIT` block in commentary and end with `verdict: ACCEPT` or `verdict: REJECT`.

If a required source is blank or any boundary check fails, do not edit yet.

## Triggers

- `r`-matrix or OPE/lambda-bracket edit
- `kappa` or modular-characteristic edit
- bar/cobar/desuspension formula
- theorem environment or claim-status edit touching d=3 objects
- shadow-class or SC-formality edit
- `MF(W)` CY-dimension edit
- cross-volume Part reference or copied formula

thinking
**Editing geometric Langlands**

I can see there are a couple of edits needed in the geometric_langlands.tex. First, I'll fix the malformed AP126 sentence. Then, I need to adjust the wording from "the standard proof goes through a nonvanishing r-matrix" to something like "through nonzero modular characteristic/away from critical level." I want to ensure clarity and accuracy, so making these edits is important. Let's get to it!
codex
I’ve isolated the likely manuscript bug, but I want the repair to match the prior AP126 cleanup rather than improvise a new phrasing. I’m checking the sibling volumes for the already-accepted wording pattern and then I’ll patch the Vol III analogue.
exec
/bin/zsh -lc "rg -n 'critical level.*nonvanishing r-matrix|standard proof goes through a nonvanishing r-matrix|surviving structure is not the collision r-matrix|Theta_A' chapters/connections/geometric_langlands.tex chapters/theory/quantum_groups_foundations.tex compute/lib/geometric_langlands_shadow.py" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
chapters/connections/geometric_langlands.tex:197:From Volume~I: the bar functor $B$ and the Verdier leg $D_{\mathrm{Ran}} \circ B$ of Theorem~A (four-functor picture), the shadow tower $\Theta_A$ and its G/L/C/M classification (Theorem~D), the Koszul locus definition, and the Kac--Moody chiral modular characteristic $\kappa_{\mathrm{ch}}(V_k(\frakg)) = \dim(\frakg)(k + h^\vee)/(2 h^\vee)$.
exec
/bin/zsh -lc "rg -n 'AP126|level-stripped|critical level.*r-matrix|k\\\\,\\\\Omega/z|vanishes at k=0|trace-form' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
Total output lines: 2306

/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:546:   `AP126`, `V2-AP34`, `AP44`, `AP45`, `AP46`, `AP49`, and `AP113` recur across manuscript and compute layers.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2125:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2135: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2821: r^{\mathrm{KM}}(z) = k\,\Omega/z
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2867: The simple-pole KM $r$-matrix $k\,\Omega/z$ acquires
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3441:  via the collision residue $r(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3470:classical limit: $r(z) = k\,\Omega/z$ is the classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3687:Collision residue & $k\,\Omega/z$ & $k\,\Omega/z$ (same) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4689:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:513:r-matrix is $r(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:520:k\,\Omega/z$ is the Lie-algebra Jacobi identity for $\fg$: the
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1140:$r(z) = k\,\Omega/z$ as classical limit.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1261:$r(z) = k\,\Omega/z$. The KZ connection is the degree-$(2,0)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:722:$k\,\delta^{ab}/z^2$ gives, after $d\log$ absorption, the collision $r$-matrix $r(z) = k\,\Omega/z$, the standard rational
/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:227:% Convention: trace-form normalisation. In the KZ normalisation

thinking
**Investigating volume theorem proof**

I need to look into Volume I of the theorem. It seems the membership proof relies on nonzero κ_ch or genericity away from critical points. To clarify, I might rewrite it to say that a separate argument is needed because the generic-volume proof does not apply at the critical point where κ_ch vanishes, though the trace-form remains finite. I should verify there are no exact label references and look for computation tests in the repository regarding critical level trace-form.
codex
The cross-volume archaeology confirms this is a regression on a previously clean Vol III AP126 surface. I’m checking one live engine/test pair for the exact critical-level wording, because the manuscript currently suggests the wrong object vanishes.
exec
/bin/zsh -lc "sed -n '360,390p' compute/lib/drinfeld_center_affine_km_engine.py" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '300,335p' compute/tests/test_drinfeld_center_affine_km_engine.py" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
# 3. R-matrix data
# =========================================================================

def r_matrix_sl2(k: F, convention: str = "trace") -> Dict[str, Any]:
    r"""Classical r-matrix for V_k(sl_2).

    Two conventions (C9/AP148):

    (i) Trace-form: r(z) = k * Omega / z
        where Omega = e tensor f + f tensor e + (1/2) h tensor h.
        AP126 check: r(z)|_{k=0} = 0. PASS.
        At k = -h^v = -2: r(z) = -2*Omega/z (finite, non-degenerate).

    (ii) KZ normalisation: r(z) = Omega / ((k + h^v) * z) = Omega / ((k+2)*z)
        At k=0: r(z) = Omega/(2z) != 0 (Lie bracket persists for non-abelian).
        At k=-h^v=-2: DIVERGES (Sugawara singularity).

    Bridge: k * Omega_{trace} = Omega / (k + h^v) at generic k (C9).

    OPE pole order: 2 (J^a(z) J^b(w) ~ k*(a,b)/(z-w)^2 + [a,b]/(z-w)).
 succeeded in 51ms:
# =========================================================================
# Section 4: R-matrix
# =========================================================================

class TestRMatrix:
    """Classical r-matrix for V_k(sl_2)."""

    def test_trace_form_coefficient(self):
        """Trace-form: r-matrix coefficient = k."""
        # VERIFIED: [DC] C9: r(z) = k*Omega/z.
        for k_val in [F(1), F(-1), F(1, 2)]:
            r = r_matrix_sl2(k_val, "trace")
            assert r["coefficient"] == k_val

    def test_ap126_trace_k0_vanishes(self):
        """AP126: r(z)|_{k=0} = 0 in trace-form convention."""
        # VERIFIED: [LC] trace-form r = 0*Omega/z = 0.
        r = r_matrix_sl2(F(0), "trace")
        assert r["k_equals_0_vanishes"]

exec
/bin/zsh -lc "git log --oneline -- chapters/connections/geometric_langlands.tex | sed -n '1,20p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
74ca0f9 CY-to-chiral deepening, toric CY3 landscape expansion, and cross-volume terminological normalisation
8423dd1 CY-to-chiral programme: alert patterns, Hochschild separation, kappa-spectrum fortification
b456b98 Vol III content: AP113 kappa subscript enforcement, AP40/AP125 theorem-status hygiene, BCH coefficient correction, stub chapter restoration across 37 files
ffb3ea8 Vol III build artifacts + prior-wave chapter edits
605ab15 Build artifacts
6f91b88 Connective tissue: 7 chapter openings + 5 Part reference fixes
af55879 AP25/AP33/AP40/AP43 rectification, MF(W) CY dimension n-2 correction, A-infinity relations displayed, bar-Koszul conventions appendix, and BV-BRST conjecture downgrade
146e415 Initial scaffold: Calabi-Yau Quantum Groups (Volume III)

thinking
**Reviewing file history**

I should take a look at the previous version of the file before any recent changes. I can use the `git show` command to pull up the version from a commit that was made before the current changes. I need to focus on searching around line 38 to see what was altered. This could help me figure out what has changed and why. It's always good to verify before moving forward!
exec
/bin/zsh -lc "git show 8423dd1:chapters/connections/geometric_langlands.tex | sed -n '30,55p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\begin{enumerate}[label=(\alph*)]
 \item The bar functor $B$, producing a factorization coalgebra.
 \item Verdier duality $D_{\mathrm{Ran}}$ applied to the bar, producing the linear-dual algebra denoted $A^!$.
 \item Inversion, returning the original algebra up to quasi-isomorphism on the Koszul locus.
 \item The derived chiral center $Z^{\mathrm{der}}_{\mathrm{ch}}$, computed as chiral Hochschild cochains; this is the bulk.
\end{enumerate}
Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.

At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.

\begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
\label{conj:critical-self-dual}
Let $A = V_{-h^\vee}(\frakg)$ and write $A^!$ for the Verdier-dual chiral algebra $D_{\mathrm{Ran}}(B(A))$ of Volume~I Theorem~A. At the critical level the chiral-algebra inclusion $\mathfrak{z}(\hat{\frakg}) \hookrightarrow A$, combined with the Feigin--Frenkel isomorphism of Theorem~\ref{thm:feigin-frenkel-center}, implies (does not iff) the existence of a factorization-coalgebra map $\mathrm{Fun}(\mathrm{Op}_{G^L}(D)) \to B(A^!)$ on $\mathrm{Ran}(X)$. The conjecture is that this map is a quasi-isomorphism on the Volume~I Koszul locus. This is a statement about the Verdier leg of the four-functor picture, not about the inversion leg $\Omega \circ B$.
\end{conjecture}

The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.

\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.

\paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.



thinking
**Evaluating regression fixes**

I see there's a regression in the commit concerning line 35. The audit suggests it’s correct, but I wonder if they only checked basic aspects. I need to address this and possibly adjust nearby remarks. Could I check the current file from another repository, or need to identify whether I'm allowed to edit this file? The task specifies the same AP126 fix, but safety limits edits to assigned files without a clear list. 

It seems like I could make minimal edits to the manuscript and maybe update tests if necessary, but I need to be cautious about whether it’s within scope. I might run a verification test afterwards, likely involving a targeted grep.
thinking
**Considering targeted tests**

I’m considering running targeted pytest commands for existing tests, like `test_drinfeld_center_affine_km_engine.py -q` and `test_geometric_langlands_shadow.py`. Since the changes involve the manuscript, these might help verify that everything is in order. Following that, I could use grep to confirm there are no malformed phrases remaining.

Even though no code changes were made, running one or two focused tests could provide some assurance. I might look at tests specifically related to AP126 and trace-form critical distinctions, though this is more about maintaining consistency than verifying edits.
thinking
**Exploring test possibilities**

I might need to open `test_geometric_langlands_shadow.py` to check if there's a test related to critical levels. I'll search through it to see if there's something that verifies when kappa vanishes at critical points. It could be helpful to run this specific test to ensure everything aligns well. If I can find precise names, it will help narrow down what I need to look for. It’s all about ensuring accuracy in my review!
codex
The live evidence is consistent now: the engine/test layer already distinguishes `k=0` vanishing from `k=-h∨` critical behavior. I’m preparing a two-line manuscript patch and will keep it scoped to the geometric Langlands chapter unless the pre-edit check rejects it.

thinking
**Evaluating clarification for AP126**

I need to preserve the tone without introducing unsupported claims like "KZ-normalised coefficient singular," especially if it’s not covered in the chapter. The user's request regarding AP126 makes critical-level clarification seem necessary. I might skip mentioning KZ if conventions haven't been discussed yet, but for resolution, it could be relevant. I can provide a succinct explanation about the AP126 trace-form convention, which should address the issue effectively without unnecessary details. This could resolve the bug.
codex
```text
## PRE-EDIT: r-matrix
family: affine Kac--Moody / Feigin--Frenkel critical-level discussion in chapters/connections/geometric_langlands.tex
formula: trace-form collision residue r(z) = k\,\Omega/z; at k = -h^\vee this is -h^\vee\,\Omega/z, while AP126 boundary check is k = 0 => r(z) = 0
level parameter: k
k=0 check: r(z)|_{k=0} = 0
source: chapters/theory/quantum_groups_foundations.tex (rem:qgf-ap126-level-check); compute/lib/drinfeld_center_affine_km_engine.py `r_matrix_sl2`; compute/tests/test_drinfeld_center_affine_km_engine.py `test_ap126_trace_k0_vanishes`, `test_kz_critical_raises`
wrong variants avoided: bare \Omega/z; conflating \kappa_{\mathrm{ch}} = 0 at k = -h^\vee with trace-form r(z) = 0; silently importing KZ critical singularity into trace-form prose
verdict: ACCEPT

## PRE-EDIT: kappa
object: affine KM critical-level paragraph in chapters/connections/geometric_langlands.tex
approved subscript: \kappa_{\mathrm{ch}}
formula: \kappa_{\mathrm{ch}}(V_k(\frakg)) = \dim(\frakg)(k + h^\vee)/(2 h^\vee), hence 0 at k = -h^\vee
source: chapters/connections/geometric_langlands.tex; compute/lib/geometric_langlands_shadow.py `kappa_affine`
boundary checks: k = -h^\vee => 0; keep distinct from the AP126 trace-form r-matrix, which remains nonzero there
wrong variants avoided: using vanishing \kappa_{\mathrm{ch}} to imply vanishing affine collision residue; claiming the critical-point proof depends on a nonvanishing r-matrix
verdict: ACCEPT
```
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex
@@ -37,3 +37,3 @@
 
-At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
+At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
 
@@ -46,3 +46,3 @@
 
-\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
+\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 
apply_patch(auto_approved=true) exited 0 in 18ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex
file update:
diff --git a/chapters/connections/geometric_langlands.tex b/chapters/connections/geometric_langlands.tex
index cb00fe2b10931458bb6610802aa6e6b67b214698..0dcf81afcb20c2cb35966c27f0667d33dbebb433
--- a/chapters/connections/geometric_langlands.tex
+++ b/chapters/connections/geometric_langlands.tex
@@ -35,7 +35,7 @@
 \end{enumerate}
 Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
 
-At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
+At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
 
 \begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
 \label{conj:critical-self-dual}
@@ -44,7 +44,7 @@
 
 The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.
 
-\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
+\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 
 \paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.
 

file update:
diff --git a/chapters/connections/geometric_langlands.tex b/chapters/connections/geometric_langlands.tex
index cb00fe2b10931458bb6610802aa6e6b67b214698..0dcf81afcb20c2cb35966c27f0667d33dbebb433
--- a/chapters/connections/geometric_langlands.tex
+++ b/chapters/connections/geometric_langlands.tex
@@ -35,7 +35,7 @@
 \end{enumerate}
 Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
 
-At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
+At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
 
 \begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
 \label{conj:critical-self-dual}
@@ -44,7 +44,7 @@
 
 The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.
 
-\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
+\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 
 \paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.
 

codex
The patch is in. I’m running the narrowest falsifiers now: one AP126 engine test slice for the affine trace-form convention, and one critical-level shadow slice for the `κ_ch = 0` side of the manuscript sentence.
exec
/bin/zsh -lc "rg -n 'level-stripped|nonvanishing \\"'$r'"\\"'$-matrix|shadow metric degenerates|not a level-stripped disappearance|AP126 trace-form'"' chapters/connections/geometric_langlands.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'test_.*kappa.*critical|test_.*critical.*kappa|test_.*shadow.*critical|test_.*critical.*shadow|test_.*critical.*level' compute/tests/test_geometric_langlands_shadow.py" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/connections/geometric_langlands.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
47:\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 succeeded in 51ms:
260:    def test_critical_level_value_sl2(self):
265:    def test_critical_level_value_g2(self):
492:    def test_shadow_metric_critical_vanishes(self):
738:    def test_kappa_near_critical_exact(self):
877:    def test_verify_all_critical_kappa_zero(self):
943:    def test_kappa_slope_matches_kappa_near_critical(self):
1126:    def test_so5_sp4_critical_level_same(self):
 succeeded in 50ms:
diff --git a/chapters/connections/geometric_langlands.tex b/chapters/connections/geometric_langlands.tex
index cb00fe2..0dcf81a 100644
--- a/chapters/connections/geometric_langlands.tex
+++ b/chapters/connections/geometric_langlands.tex
@@ -35,7 +35,7 @@ The proof of the Feigin--Frenkel isomorphism proceeds via the Wakimoto realizati
 \end{enumerate}
 Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
 
-At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
+At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
 
 \begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
 \label{conj:critical-self-dual}
@@ -44,7 +44,7 @@ Let $A = V_{-h^\vee}(\frakg)$ and write $A^!$ for the Verdier-dual chiral algebr
 
 The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.
 
-\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
+\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 
file update:
diff --git a/chapters/connections/geometric_langlands.tex b/chapters/connections/geometric_langlands.tex
index cb00fe2b10931458bb6610802aa6e6b67b214698..0dcf81afcb20c2cb35966c27f0667d33dbebb433
--- a/chapters/connections/geometric_langlands.tex
+++ b/chapters/connections/geometric_langlands.tex
@@ -35,7 +35,7 @@
 \end{enumerate}
 Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
 
-At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
+At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
 
 \begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
 \label{conj:critical-self-dual}
@@ -44,7 +44,7 @@
 
 The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.
 
-\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
+\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 
 \paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.
 

exec
/bin/zsh -lc "pytest compute/tests/test_drinfeld_center_affine_km_engine.py -q -k 'test_ap126_trace_k0_vanishes or test_kz_critical_raises'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "pytest compute/tests/test_geometric_langlands_shadow.py -q -k 'test_critical_level_value_sl2 or test_shadow_metric_critical_vanishes or test_verify_all_critical_kappa_zero'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 381ms:
..                                                                       [100%]
2 passed, 91 deselected in 0.05s
 succeeded in 456ms:
...                                                                      [100%]
3 passed, 155 deselected in 0.14s
file update:
diff --git a/chapters/connections/geometric_langlands.tex b/chapters/connections/geometric_langlands.tex
index cb00fe2b10931458bb6610802aa6e6b67b214698..0dcf81afcb20c2cb35966c27f0667d33dbebb433
--- a/chapters/connections/geometric_langlands.tex
+++ b/chapters/connections/geometric_langlands.tex
@@ -35,7 +35,7 @@
 \end{enumerate}
 Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
 
-At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
+At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
 
 \begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
 \label{conj:critical-self-dual}
@@ -44,7 +44,7 @@
 
 The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.
 
-\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
+\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 
 \paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.
 


thinking
**Reviewing update plans**

I’m considering whether I need to update my plan, but part of me thinks it might not be necessary. I should probably inspect the line numbers after the patch for a final reference. I'll need to use the new line numbering to ensure everything is correct and meets the requirements. It's essential that I’m thorough in this step to avoid any potential issues down the line!
codex
The AP126-specific checks passed, and the critical-level shadow checks passed too. I’m pulling exact line numbers from the edited chapter so the final report can list each problem and the precise edit applied.
exec
/bin/zsh -lc "nl -ba chapters/connections/geometric_langlands.tex | sed -n '34,49p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
    34	 \item The derived chiral center $Z^{\mathrm{der}}_{\mathrm{ch}}$, computed as chiral Hochschild cochains; this is the bulk.
    35	\end{enumerate}
    36	Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
    37	
    38	At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
    39	
    40	\begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
    41	\label{conj:critical-self-dual}
    42	Let $A = V_{-h^\vee}(\frakg)$ and write $A^!$ for the Verdier-dual chiral algebra $D_{\mathrm{Ran}}(B(A))$ of Volume~I Theorem~A. At the critical level the chiral-algebra inclusion $\mathfrak{z}(\hat{\frakg}) \hookrightarrow A$, combined with the Feigin--Frenkel isomorphism of Theorem~\ref{thm:feigin-frenkel-center}, implies (does not iff) the existence of a factorization-coalgebra map $\mathrm{Fun}(\mathrm{Op}_{G^L}(D)) \to B(A^!)$ on $\mathrm{Ran}(X)$. The conjecture is that this map is a quasi-isomorphism on the Volume~I Koszul locus. This is a statement about the Verdier leg of the four-functor picture, not about the inversion leg $\Omega \circ B$.
    43	\end{conjecture}
    44	
    45	The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.
    46	
    47	\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
    48	
    49	\paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.
file update:
diff --git a/chapters/connections/geometric_langlands.tex b/chapters/connections/geometric_langlands.tex
index cb00fe2b10931458bb6610802aa6e6b67b214698..0dcf81afcb20c2cb35966c27f0667d33dbebb433
--- a/chapters/connections/geometric_langlands.tex
+++ b/chapters/connections/geometric_langlands.tex
@@ -35,7 +35,7 @@
 \end{enumerate}
 Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
 
-At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
+At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
 
 \begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
 \label{conj:critical-self-dual}
@@ -44,7 +44,7 @@
 
 The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.
 
-\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
+\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 
 \paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.
 





thinking
**Structuring findings report**

I need to ensure I'm editing only the necessary file, and I should mention tests. It's also important to indicate that there are no other actionable AP126 findings within the scope. It might be useful to search all Volume III chapters for `Omega/z` to confirm it's clean. The audit found just one file with two AP126-related regressions. To be thorough, we should note that the scan revealed no more AP126 issues in the active chapters. Finally, I need to present the findings clearly.
thinking
**Formatting findings with links**

I need to include clickable file links, using the format `[chapters/connections/geometric_langlands.tex](/Users/...:38)` with one link per line. Including file paths and line numbers might make it clearer. I must say `PROBLEM at file:line` and use markdown links for clarity. For example: `PROBLEM at [file](/path:line): ...` followed by `EXACT edit applied: ...`. 

I also need line 47 referenced and verification added. The tests show two passing for the first command and three for the second. It's important to note that only this manuscript file had actionable AP126 regressions, and no other live Vol III patterns were found.
thinking
**Describing edits and tests**

I found one live file with two actionable regressions. I need to mention the exact edits applied, specifically the text changes, possibly quoting the exact sentences. This shouldn't pose a copyright issue since it's our local file. For each edit, I could show the change, like: "EXACT edit applied: replaced `...(level-stripped r-matrix)...` with `In the AP126 trace-form convention...`.” Then I'll include verification that "Narrow falsifiers passed: 2 AP126 affine-engine tests and 3 critical-level shadow tests." That should be clear and concise.
thinking
**Summarizing findings and edits**

I'll avoid mentioning commentary or pre-edit details to keep it concise. Here’s how I can format it:

**Findings**  
1. **PROBLEM** at [chapters/connections/geometric_langlands.tex](...:38): The critical-level paragraph conflated `κ_ch(V_{-h^\vee})=0` with the affine trace-form `r`-matrix, and had a malformed parenthetical. The **EXACT edit applied**: replaced the sentence with `At the critical level ... In the AP126 trace-form convention ... -h^\vee\,\Omega/z, not 0...`.  
2. **PROBLEM** at [chapters/connections/geometric_langlands.tex](...:47): The remark incorrectly linked critical-point difficulty to a nonvanishing `r`-matrix. The **EXACT edit applied**: replaced `because the standard proof goes through a nonvanishing r-matrix` with `because the shadow metric degenerates there ...`. Verification confirms AP126/critical-level slices passed: `test_drinfeld_center_affine_km_engine` (2 tests) and `test_geometric_langlands_shadow` (3 tests).
codex
1. PROBLEM at [chapters/connections/geometric_langlands.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38): the critical-level paragraph conflated `\kappa_{\mathrm{ch}}(V_{-h^\vee}) = 0` with the affine AP126 `r`-matrix convention, and it contained a broken parenthetical fragment.
EXACT edit applied: replaced the sentence with:
`At the critical level \kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0. In the AP126 trace-form convention the classical r-matrix is still r(z) = k\,\Omega/z, so at k = -h^\vee it is -h^\vee\,\Omega/z, not 0. The critical phenomenon is the vanishing of \kappa_{\mathrm{ch}} and the resulting shadow/center degeneration encoded by \Theta_A, not a level-stripped disappearance of the affine collision residue.`

2. PROBLEM at [chapters/connections/geometric_langlands.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:47): the Koszul-locus remark incorrectly said the critical-point issue comes from needing a nonvanishing `r`-matrix, which contradicts the AP126 trace-form convention.
EXACT edit applied: replaced
`because the standard proof goes through a nonvanishing r-matrix`
with
`because the shadow metric degenerates there even though the AP126 trace-form r-matrix remains nonzero`.

Verification: `pytest compute/tests/test_drinfeld_center_affine_km_engine.py -q -k 'test_ap126_trace_k0_vanishes or test_kz_critical_raises'` passed (`2 passed`), and `pytest compute/tests/test_geometric_langlands_shadow.py -q -k 'test_critical_level_value_sl2 or test_shadow_metric_critical_vanishes or test_verify_all_critical_kappa_zero'` passed (`3 passed`).
file update:
diff --git a/chapters/connections/geometric_langlands.tex b/chapters/connections/geometric_langlands.tex
index cb00fe2b10931458bb6610802aa6e6b67b214698..0dcf81afcb20c2cb35966c27f0667d33dbebb433
--- a/chapters/connections/geometric_langlands.tex
+++ b/chapters/connections/geometric_langlands.tex
@@ -35,7 +35,7 @@
 \end{enumerate}
 Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
 
-At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
+At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
 
 \begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
 \label{conj:critical-self-dual}
@@ -44,7 +44,7 @@
 
 The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.
 
-\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the standard proof goes through a nonvanishing $r$-matrix. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
+\paragraph{Remark on the Koszul locus.} Volume~I defines the Koszul locus as the set of chiral algebras $A$ for which the inversion map $\Omega(B(A)) \to A$ is a quasi-isomorphism. For $V_k(\frakg)$ with $\frakg$ simple and $k$ generic, membership in the Koszul locus is a theorem of Volume~I (the Kac--Moody family is class L, shadow depth $r = 3$). At the critical level $k = -h^\vee$ the chiral modular characteristic $\kappa_{\mathrm{ch}}$ vanishes, and membership requires a separate argument because the shadow metric degenerates there even though the AP126 trace-form $r$-matrix remains nonzero. The status of $V_{-h^\vee}(\frakg)$ on the Koszul locus is therefore itself conjectural and feeds into Conjecture~\ref{conj:critical-self-dual}.
 
 \paragraph{Remark on the opposite level.} Vol~I records that the Koszul conductor for the Kac--Moody family is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ where $\kappa_{\mathrm{ch}}' = \kappa_{\mathrm{ch}}(V_{k'}(\frakg))$ with $k' = -k - 2 h^\vee$ (the Feigin--Frenkel reflection). The two critical-level points $k = -h^\vee$ and $k' = -h^\vee$ coincide: the critical level is the fixed point of the Feigin--Frenkel reflection. This is the algebraic reason the critical level is distinguished, and the source of the self-duality language that must not be transposed to universal form.
 

tokens used
100,338
