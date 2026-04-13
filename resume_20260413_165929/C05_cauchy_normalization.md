# C05_cauchy_normalization (539s)

**Result**
I audited all three volumes for AP120. Volume I and the checked Volume III surfaces have no live Cauchy-normalization fixes: their `1/(2\pi)` hits are real-angle `d\arg` kernels, scalar Green functions, asymptotics, or period integrals, not holomorphic contour normalizations. Every live AP120 defect is in Volume II.

No edits were applied because this session cannot write to sibling repos outside `/Users/raeez/chiral-bar-cobar`. I tested `apply_patch` on Volume II and it was rejected with: `writing outside of the project; rejected by user approval settings`.

**Blocked Fixes**
- PROBLEM at [examples-complete.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:54), [examples-complete-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex:36), [examples-complete-proved.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:36): HT free propagator uses `\frac{1}{2\pi}`. EXACT edit blocked: `\frac{1}{2\pi}` -> `\frac{1}{2\pi i}`.
- PROBLEM at [examples-complete.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:527), [examples-complete-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:66): non-abelian HT propagator uses `\frac{\delta^{ab}}{2\pi}`. EXACT edit blocked: `\frac{\delta^{ab}}{2\pi}` -> `\frac{\delta^{ab}}{2\pi i}`.
- PROBLEM at [examples-computing.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:81), [examples-computing.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:99): kernel/bracket uses `2\pi` instead of `2\pi i`. EXACT edit blocked: `\frac{1}{2\pi}\frac{\Theta(t-t')}{z-z'}` -> `\frac{1}{2\pi i}\frac{\Theta(t-t')}{z-z'}` and `\frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}` -> `\frac{\Theta(t_1-t_2)}{2\pi i (z_1-z_2)}`.
- PROBLEM at [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:509), [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:555), [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:571), [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:575): mixed HT kernel and derived residue terms use `1/(2\pi)`. EXACT edit blocked: `\frac{1}{2\pi}` -> `\frac{1}{2\pi i}`, `\frac{\Theta(t-t')}{2\pi}` -> `\frac{\Theta(t-t')}{2\pi i}`, `\frac{\kappa}{2\pi}` -> `\frac{\kappa}{2\pi i}`.
- PROBLEM at [thqg_bv_construction_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:135), [thqg_bv_construction_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:140), [thqg_bv_construction_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:156), [thqg_bv_construction_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:769): retarded `\bar\partial` kernel and contour formula omit `i`. EXACT edit blocked: `\frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}` -> `\frac{\Theta(t_1-t_2)}{2\pi i (z_1-z_2)}`, `1/(2\pi(z_1-z_2))` -> `1/(2\pi i (z_1-z_2))`, `\frac{dz}{2\pi(z-w)}` -> `\frac{dz}{2\pi i (z-w)}`.
- PROBLEM at [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:445), [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:660), [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:864), [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:866), [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:870): all HT propagator formulas use `2\pi` instead of `2\pi i`. EXACT edit blocked: add `i` in each denominator, including `K(z,t)=\Theta(t)/(2\pi z)` -> `K(z,t)=\Theta(t)/(2\pi i z)`.
- PROBLEM at [fm-proofs.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:481): `G(z_{v_i}, z_{v_j}) = \frac{1}{2\pi(z_{v_i} - z_{v_j})}`. EXACT edit blocked: `\frac{1}{2\pi(z_{v_i} - z_{v_j})}` -> `\frac{1}{2\pi i (z_{v_i} - z_{v_j})}`.
- PROBLEM at [raviolo.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:558): `K = \delta(t_1 - t_2)/(2\pi(z_1 - z_2))`. EXACT edit blocked: `/(2\pi(z_1-z_2))` -> `/(2\pi i (z_1-z_2))`.
- PROBLEM at [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:139), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:168), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:659), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:660): HT propagators/contractions use `2\pi(z_1-z_2)`. EXACT edit blocked: add `i` in every denominator on those lines.
- PROBLEM at [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:129), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:158), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:757), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:758), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1057): same AP120 drift. EXACT edit blocked: add `i` to each `2\pi(z_1-z_2)` denominator.
- PROBLEM at [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:61), [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:62), [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1063): same AP120 drift. EXACT edit blocked: add `i` to each `2\pi(z_1-z_2)` denominator.
- PROBLEM at [w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:125), [w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:157): same AP120 drift. EXACT edit blocked: add `i` to each `2\pi(z_1-z_2)` denominator.
- PROBLEM at [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1686), [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1690), [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1691): direct and reflected HT propagators use `2\pi(z-z')` and `2\pi(z-\bar z')`. EXACT edit blocked: replace with `2\pi i (z-z')` and `2\pi i (z-\bar z')`.

If you want the fixes actually applied, rerun with `/Users/raeez/chiral-bar-cobar-vol2` added to the writable roots; I already have the exact patch surface isolated.


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
session id: 019d87e8-04a5-72a1-ad66-6b0dba56c1a4
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


Fix Cauchy integral normalization (AP120).
Search ALL volumes for '\\oint' or '\\frac{1}{2\\pi}'.
Must be 1/(2*pi*i), NOT 1/(2*pi). Fix each instance.
mcp startup: no servers



thinking
**Inspecting codebase for updates**

I need to act as a coding agent and start by inspecting the codebase. I should read through the required files, particularly since there's a substantial mathematical edit involved. User wants me to search all volumes for specific terms like '\\oint' and '\\frac{1}{2\\pi}', and fix each instance. This means I might need to employ skills for cross-volume propagation and multi-path verification. First, I should provide an update before substantial work begins.
thinking
**Searching the codebase efficiently**

I’m considering using an explorer sub-agent for the codebase search, but since I’m already in the repo, I might first employ shell rg. The instructions say to prefer explorer agents over manual searching, especially for codebase questions. I could have one explorer locate problematic normalization instances across three volumes and another one summarize required reads. However, I think I still need to read certain files myself before making any substantial mathematical edits, like checking CLAUDE.
thinking
**Using explorers for efficient reading**

I could ask the explorer to summarize relevant AP120 information, but I might also need to read directly due to hierarchy requirements. The instructions emphasize that explorers are faster and more authoritative, so I should definitely prefer them for searching and reading. However, I can’t re-read or re-search the code they cover. It seems I should delegate the required reads to the explorer while ensuring I gather the exact edits and line references needed for my tasks.
codex
Scope is AP120 across all three volumes: I’m checking the canonical sources first, then I’ll enumerate every `\oint` / `\frac{1}{2\pi}` hit, classify the true normalization errors, and patch only those files.
collab spawn_agent(call_vc5OmQXtpS916bdTzhRRPq0N, prompt="Read the required repo-constitution files for a mathematical edit in /Users/raeez/chiral-bar-cobar and summarize only th…")
spawn_agent(call_vc5OmQXtpS916bdTzhRRPq0N, prompt="Read the required repo-constitution files for a mathematical edit in /Users/raeez/chiral-bar-cobar and summarize only th…") pending init:
  agent: 019d87e8-48fd-7712-8172-c763f4249d82
mcp startup: no servers
collab spawn_agent(call_FKAATdKEEDCHc2v0NSZ6F2MB, prompt="Search across the three volumes for all TeX-source occurrences relevant to AP120 normalization drift. Roots: /Users/raee…")
spawn_agent(call_FKAATdKEEDCHc2v0NSZ6F2MB, prompt="Search across the three volumes for all TeX-source occurrences relevant to AP120 normalization drift. Roots: /Users/raee…") pending init:
  agent: 019d87e8-4ad3-7002-83b4-52d0e1a16ca1
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n --glob '*.{tex,sty,cls,md}' '\\\\oint|\\\\frac{1}{2\\\\pi'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\oint|\\frac{1}{2\\pi)
                       ^^
error: unclosed counted repetition
codex
I’m using `cross-volume-propagation` first to sweep the collision surface, then `multi-path-verify` on each candidate normalization before editing. After that I’ll run a narrow verification pass for stale `1/(2\pi)` residues.
exec
/bin/zsh -lc 'rg -n "AP120" -n CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
267:**C24. Cauchy integral normalization.** `[z^{n-1}] f(z) = (1/(2*pi*i)) * contour_integral f(z) dz/z^n`. Wrong: 1/(2*pi) (missing i gives zero for real integrands, AP120). Sanity: F_1 = kappa/24.
347:- B38. `\frac{1}{2\pi}\oint` (missing i). CORRECT: `\frac{1}{2\pi i}\oint`. AP120.
863:AP120: Cauchy integral normalization is 1/(2*pi*i), NOT 1/(2*pi). Missing i gives zero for real coefficients. Always verify F_1=kappa/24 as sanity check.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n --glob '*.{tex,sty,cls,md}' '\\\\oint'" in /Users/raeez/chiral-bar-cobar succeeded in 58ms:
wave2_audit_20260413_001942/S01_bar_to_cobar.md:1210:chapters/theory/bar_cobar_adjunction_inversion.tex:3936:Period matrix $\tau_{ij} = \oint_{B_j} \omega_i$ &
fix_wave_E_20260413_182434/E15_build_warnings.md:1198:   223	where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:2231: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:2395: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:2566: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:2757: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:3014: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:3301: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:3611: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:4188: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:4734: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:5293: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:5847: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:6394: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:6942: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:7488: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:8034: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:8580: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:9141: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
fix_wave_E_20260413_182434/E15_build_warnings.md:9735: where $E(z,w)$ is the prime form (Appendix~\ref{app:theta}), $\omega_1, \ldots, \omega_g$ are the normalized holomorphic differentials ($\oint_{A_j}\omega_k = \delta_{jk}$), and $\Omega$ is the period matrix. The second term subtracts the zero-mode contribution, ensuring $G_g$ is well-defined on~$\Sigma_g$ (which admits no global Green's function without this regularization).
Plan update
Cross-volume AP120 audit and fix with minimum truthful edits.
  → Read constitutional sources relevant to AP120 and scope constraints
  • Enumerate all cross-volume normalization candidates and classify true errors
  • Patch only definite AP120 errors in assigned files
  • Re-scan all volumes to verify no incorrect `1/(2\pi)` contour normalizations remain
exec
/bin/zsh -lc "sed -n '240,310p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).

**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.

**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).

**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).

**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).

**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.

**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).

**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).

**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).

**C20. Bershadsky-Polyakov Koszul conductor.** `K_BP = c(k) + c(-k-6) = 196`. Self-dual level k=-3. Wrong: K_BP=76 (corrected in Wave 7); K_BP=2 (AP140, confusing with ghost constant C_{(2,1)}=2).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n --glob '*.{tex,sty,cls,md}' '\\\\frac\\{1/2\\\\pi'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "Cauchy" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n --glob '*.{tex,sty,cls,md}' --fixed-strings '\\frac{1}{2\\pi'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 226

CLAUDE.md:347:- B38. `\frac{1}{2\pi}\oint` (missing i). CORRECT: `\frac{1}{2\pi i}\oint`. AP120.
appendices/signs_and_shifts.tex:1463:\omega_K(z, w) = \frac{1}{2\pi i} d\arg(z - w)
appendices/signs_and_shifts.tex:1464: = \frac{1}{2\pi i} \frac{d\bar{z} - d\bar{w}}{z - w}.
appendices/signs_and_shifts.tex:1483:$w_\Gamma = \int_{C_2(\mathbb{R}^2)} \omega_K(z_1, z_2) = \frac{1}{2\pi i}
appendices/signs_and_shifts.tex:1573:Propagator & implicit in $j_*j^*$ & $P_\epsilon$ (regularized) & $\frac{1}{2\pi i}d\arg$ & $d\log(z-w)$ \\
chapters/examples/yangians_drinfeld_kohno.tex:7294: - \frac{1}{2\pi i(k + h^\vee)}\,
audit_campaign_20260412_231034/AP13_hardcoded_part.md:157:- B38. `\frac{1}{2\pi}\oint` (missing i). CORRECT: `\frac{1}{2\pi i}\oint`. AP120.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:5:- `PROBLEM` at [examples-complete.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:54), [examples-complete-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex:36), [examples-complete-proved.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:36), [examples-complete-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:66): HT propagators use `1/(2\pi)` or `\delta^{ab}/(2\pi)`. `EXACT edit needed`: `\frac{1}{2\pi}` -> `\frac{1}{2\pi i}` and `\frac{\delta^{ab}}{2\pi}` -> `\frac{\delta^{ab}}{2\pi i}`.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:7:- `PROBLEM` at [examples-computing.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:81): `K(t-t',z-z') = \frac{1}{2\pi}\frac{\Theta(t-t')}{z-z'}`. `EXACT edit needed`: `\frac{1}{2\pi}` -> `\frac{1}{2\pi i}`.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:67:Using `cross-volume-propagation` and `multi-path-verify` because this is a shared formula correction that needs a repo-wide audit, a minimal patch, and a verification pass. I’m reading the required repo constitution files first, then I’ll grep all three volumes for `\oint` and `\frac{1}{2\pi}` to isolate every AP120 surface before editing.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:215:/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:54:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:221:/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:231:The user asked me to search all volumes for specific instances of `\oint` or `\frac{1}{2\pi}` and to fix them to `1/(2*pi*i)`, not `1/(2*pi)`. I need to clarify that not every instance of `\oint` requires the 1/2πi prefactor; it seems to pertain mainly to Cauchy integral normalization. I want to find occurrences where contour integrals are misusing this normalization, particularly focusing on contexts like `dz/(2\pi(z-w))` found within the .tex files.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:235:I’m considering how to restrict my search to live `.tex` files in the main repositories, while possibly including notes. The user mentioned “all volumes,” which might mean everything in these repos, but I want to stick to “only edit assigned files” and make minimum edits. I need to patch the live source files, not audit artifacts. If a note references `\oint` with certain integrals, like in Vol III, I should find those candidates using a previous artifact, F16_cauchy. I’ll also search for patterns like `\frac{1}{2\pi}` and `2\pi(` to identify issues.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:264:I should think about inspecting myself in parallel. I might want to use rg on a live .tex file to check for specific patterns. It seems I could apply multiple commands at once to look for things like `\frac{1}{2\pi}`, `2\pi(`, and maybe even `dz}{2\\pi`. It feels like we should just get started on this task! Let's see what results I can uncover with those patterns.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:280:/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:281:/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:81:K(t-t',z-z') = \frac{1}{2\pi} \frac{\Theta(t-t')}{z-z'},
fix_wave_C_20260413_175943/C05_cauchy_normalization.md:282:/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
exec
/bin/zsh -lc 'rg -n "AP120" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

collab wait(call_ZrgijjZGFDwUZOQ4yTrPw4JG)
  receivers: 019d87e8-48fd-7712-8172-c763f4249d82, 019d87e8-4ad3-7002-83b4-52d0e1a16ca1
exec
/bin/zsh -lc 'rg -n "kappa/24" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4098:$F_1 = \kappa/24$;
4386:$\ell_2^{(1)} = S_3\kappa/24 - S_3^2$ (exact from MC; Beilinson audit
exec
/bin/zsh -lc "sed -n '4070,4110p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
carry CohFT structure on
$R^*(\overline{\mathcal{M}}_{g,n+1})$
(Theorem~\ref{thm:shadow-cohft});
the CohFT axioms (equivariance, splitting) are formal consequences of $D_\cA^2 = 0$ on the modular bar complex. The flat identity holds conditionally when the vacuum lies in~$V$ (Theorem~\ref{thm:shadow-cohft}).
The MC factorization
$\xi^*\Theta_\cA = \Theta_\cA \star \Theta_\cA$
descends to tautological relations via
Theorem~\ref{thm:mc-tautological-descent}.
At genus~$0$: WDVV equations = Jacobi identity of the MC bracket
(Proposition~\ref{prop:wdvv-from-mc}).
At degree~$2$: Mumford $\lambda$-class relations from the MC equation
(Proposition~\ref{prop:mumford-from-mc}).
Reconstruction:
the Givental $R$-matrix equals the complementarity propagator
$P_\cA$
(Theorem~\ref{thm:cohft-reconstruction}).
The dressed propagator coefficient
$P^R(D_+,D_-)$ from the edge integral
$\int R(\psi_+)\,R(\psi_-)/(\psi_+ + \psi_-)$
satisfies $P^R(D_+,D_-)=P^R(D_-,D_+)$

thinking
**Planning extensive TeX symbol search**

I'm figuring out how to search all three volumes for `\oint` and `\frac{1}{2\pi}` occurrences in TeX and related files, aiming to classify each by AP120 normalization relevance—especially noting missing `i` factors that indicate errors. Since the volume of results might be huge, I plan to filter and highlight only the lines that show definite AP120 errors or need context, while also gathering absolute paths, line numbers, line text, and classifications to produce a clear, useful summary.
exec
/bin/zsh -lc "rg -n \"2\\\\pi\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:2\pi)
        ^^^
error: Unicode property not found
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n --glob '*.{tex,sty,cls,md}' '\\\\oint'" in /Users/raeez/chiral-bar-cobar succeeded in 238ms:
chapters/examples/w-algebras-stable.tex:614:= \oint \oint
chapters/examples/examples-complete.tex:65:m_2(\phi(z_1), \psi(z_2)) = \oint_{|z_1 - z_2| = \varepsilon} \langle \phi(z_1) \psi(z_2) \rangle \, \frac{dz_1}{z_1 - z_2}.
chapters/examples/examples-complete.tex:212:m_3(\phi, \phi, \phi) = 2 \oint_{\Gamma_2} \frac{dz_1 \wedge dz_2}{(z_1 - z_2)(z_2 - z_3)(z_3 - z_1)},
chapters/examples/examples-complete.tex:231:m_3(\phi, \phi, \phi) = 2 \oint_{\Gamma_2} \frac{dz_1 \wedge dz_2}{(z_1 - z_2)(z_2 - z_3)(z_3 - z_1)}.
chapters/examples/examples-complete.tex:849: \QBRST \;=\; \oint\!\Bigl(
chapters/examples/examples-complete.tex:912: \oint [da]_{N}\;
chapters/examples/w-algebras-virasoro.tex:527:= \oint \oint
chapters/examples/examples-complete-proved.tex:47:m_2(\phi(z_1), \psi(z_2)) = \oint_{|z_1 - z_2| = \varepsilon} \langle \phi(z_1) \psi(z_2) \rangle \, \frac{dz_1}{z_1 - z_2}.
chapters/examples/examples-complete-proved.tex:503: \QBRST \;=\; \oint\!\Bigl(
chapters/examples/examples-complete-proved.tex:566: \oint [da]_{N}\;
chapters/examples/examples-complete-core.tex:47:m_2(\phi(z_1), \psi(z_2)) = \oint_{|z_1 - z_2| = \varepsilon} \langle \phi(z_1) \psi(z_2) \rangle \, \frac{dz_1}{z_1 - z_2}.
chapters/examples/examples-complete-core.tex:194:m_3(\phi, \phi, \phi) = 2 \oint_{\Gamma_2} \frac{dz_1 \wedge dz_2}{(z_1 - z_2)(z_2 - z_3)(z_3 - z_1)},
chapters/examples/examples-complete-core.tex:213:m_3(\phi, \phi, \phi) = 2 \oint_{\Gamma_2} \frac{dz_1 \wedge dz_2}{(z_1 - z_2)(z_2 - z_3)(z_3 - z_1)}.
chapters/examples/examples-complete-core.tex:544: \QBRST \;=\; \oint\!\Bigl(
chapters/examples/examples-complete-core.tex:607: \oint [da]_{N}\;
chapters/examples/examples-worked.tex:250:  Q \;=\; \oint\!\bigl(\operatorname{Tr}(c\,Z_1 Z_2)
chapters/examples/examples-worked.tex:463:  \oint\oint
chapters/examples/examples-worked.tex:502:$J^a_n = \oint z^n J^a(z)\,dz$ are likewise $Q$-closed.
chapters/examples/examples-worked.tex:585:  \oint\oint
chapters/examples/examples-worked.tex:947:  Q_W = \oint\!\bigl(YZ\,\partial_X + XZ\,\partial_Y + XY\,\partial_Z\bigr).
exec
/bin/zsh -lc "rg -n \"2\\\\pi\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:2\pi)
        ^^^
error: Unicode property not found
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n --glob '*.{tex,sty,cls,md}' --fixed-strings '\\frac{1}{2\\pi'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/examples-complete-proved.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
working_notes.tex:13983:$\frac{1}{2\pi i}\int d\log(z_1 - z_2)$ around the
chapters/examples/examples-computing.tex:81:K(t-t',z-z') = \frac{1}{2\pi} \frac{\Theta(t-t')}{z-z'},
chapters/theory/modular_swiss_cheese_operad.tex:1943: := \frac{1}{2\pi i}\, d_{z_i} \log E(z_i, z_j),
chapters/theory/fm-proofs.tex:481:G(z_{v_i}, z_{v_j}) = \frac{1}{2\pi(z_{v_i} - z_{v_j})}.
chapters/theory/fm-calculus.tex:870:\int_{\R^2} G(z_1, z_2; t_1, t_2)\, dt_1\, dt_2 = \frac{1}{2\pi(z_1 - z_2)}.
chapters/theory/fm-calculus.tex:936:(the integral is understood in the distributional sense: the propagator $G(z_i, z_v) = \bar\partial^{-1}\delta(z_i - z_v) = \frac{1}{2\pi i} \cdot \frac{1}{z_i - z_v}$ is the $\bar\partial$-propagator (the Green's function for $\bar\partial$ on~$\C$), and the area integral is computed using the distributional identity $\bar\partial\bigl(\frac{1}{z-w}\bigr) = \pi\,\delta^2(z-w)$ (this is Cauchy's integral formula in distributional form; see H\"ormander~\cite[Theorem~1.4.1]{Hormander90} for the precise statement in the tempered distribution setting): each factor $G(z_j, z_v)$ contributes a pole in $z_v$, and integrating $\int d^2z_v$ against the product of poles reduces, via a chain of distributional pairings (successive applications of $\bar\partial \cdot \frac{1}{z-w} = \pi\delta^2$), to the claimed rational function; see e.g.\ \cite{CG17} \S5.4), the result is
chapters/theory/raviolo.tex:427:\emph{Claim}: $G = K_\C \otimes H_\R$, where $K_\C(z) = \frac{1}{2\pi z}$ and $H_\R(t) = \Theta(t)$ (or $\delta(t)$, depending on the bi-degree component).
chapters/theory/raviolo.tex:442: K_\C(z) = \frac{1}{2\pi z}, \quad H_\R(t) = \Theta(t) \text{ or } \delta(t),
standalone/stokes_gap_kzb_regularity.tex:170:  + \delta_{\alpha,g}\delta_{\beta,g} \cdot \frac{1}{2\pi i}\log(t_e)
chapters/theory/factorization_swiss_cheese.tex:2810:dz \wedge d\bar z \cdot \frac{1}{2\pi i} \cdot 2\pi i =
chapters/examples/examples-complete.tex:54:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
chapters/examples/examples-complete-core.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
chapters/connections/spectral-braiding-core.tex:2472:\frac{1}{2\pi i}
chapters/connections/relative_feynman_transform.tex:509:K(z,t) \;=\; \frac{1}{2\pi}\,\frac{\Theta(t)}{z},
chapters/connections/relative_feynman_transform.tex:575:\frac{1}{2\pi}\,
chapters/connections/kontsevich_integral.tex:199:\frac{1}{2\pi}\, d\arg(e^{i\theta_i} - e^{i\theta_j})
chapters/connections/kontsevich_integral.tex:211:where $\eta^K_{ij} = \frac{1}{2\pi}\, d\arg(t_i - t_j)$ is
chapters/connections/kontsevich_integral.tex:239:of $\frac{1}{2\pi}\,d\arg$ from $\Re(\eta_{ij})|_{S^1}$
exec
/bin/zsh -lc 'rg -n "AP120" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n --glob '*.{tex,sty,cls,md}' '\\\\oint'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
notes/physics_4d_n2_hitchin.tex:137: z^I(u) = \oint_{A^I} \Omega_u, \qquad \cF_J(u) = \oint_{B_J} \Omega_u.
notes/physics_4d_n2_hitchin.tex:163: M_\gamma(u) = |Z_\gamma(u)| = \left| \oint_\gamma \Omega_u \right|,
notes/physics_4d_n2_hitchin.tex:192:$Z_\gamma(u) = \oint_\gamma \Omega_u$ is exactly the central charge function of the Bridgeland
notes/physics_4d_n2_hitchin.tex:298: a_I = \oint_{\alpha_I} \lambda_{\SW}, \qquad a_{D,J} = \oint_{\beta_J} \lambda_{\SW} = \frac{\partial \cF}{\partial a_J};
exec
/bin/zsh -lc 'rg -n "AP120" raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: IO error for operation on raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n --glob '*.{tex,sty,cls,md}' --fixed-strings '\\frac{1}{2\\pi'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'ls raeeznotes' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
ls: raeeznotes: No such file or directory
exec
/bin/zsh -lc "find . -path '*raeeznotes100*' -print" in /Users/raeez/chiral-bar-cobar succeeded in 2.19s:
./archive/raeeznotes/raeeznotes100
./archive/raeeznotes/raeeznotes100/red_team_summary.md
./archive/raeeznotes/raeeznotes100/suspicious_proved_claim_dependencies.csv
./archive/raeeznotes/raeeznotes100/label_status_conflicts.csv
./archive/raeeznotes/raeeznotes100/informal_claim_harvest.csv
./archive/raeeznotes/raeeznotes100/provisionally_dismissed_claims.csv
./archive/raeeznotes/raeeznotes100/master_claim_ledger_filtered.csv
exec
/bin/zsh -lc 'rg -n "AP120" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "Cauchy" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "Cauchy" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 499

metadata/dependency_graph.dot:2510:  cor_shadow_cauchy_schwarz [label="cor:shadow-cauchy-schwarz\ncorollary [Pr]\nShadow Cauchy--Schwarz inequality", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:994:| `cor:shadow-cauchy-schwarz` | `corollary` | 14686 | Shadow Cauchy--Schwarz inequality |
metadata/claims.jsonl:2413:{"label": "cor:shadow-cauchy-schwarz", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 14686, "title": "Shadow Cauchy--Schwarz inequality", "labels_in_block": ["cor:shadow-cauchy-schwarz", "eq:shadow-cs"]}
scripts/elite_rescue_40.py:320:Cauchy 1/(2*pi*i), K(Vir)=13, K(BP)=196.
CLAUDE.md:267:**C24. Cauchy integral normalization.** `[z^{n-1}] f(z) = (1/(2*pi*i)) * contour_integral f(z) dz/z^n`. Wrong: 1/(2*pi) (missing i gives zero for real integrands, AP120). Sanity: F_1 = kappa/24.
CLAUDE.md:402:- B74. Cauchy's theorem on formal power series. R(z) in End(V tensor V)((z)) is FORMAL. Cauchy requires CONVERGENT. Correct argument for radius-independence of monodromy: FLATNESS of connection + HOMOTOPY INVARIANCE (topological, not analytic). Applies to ANY formal-series-near-analytic-argument across all volumes.
CLAUDE.md:863:AP120: Cauchy integral normalization is 1/(2*pi*i), NOT 1/(2*pi). Missing i gives zero for real coefficients. Always verify F_1=kappa/24 as sanity check.
scripts/fix_campaign_100.py:421:agent("C", "C05_cauchy_normalization", """Fix Cauchy integral normalization (AP120).
AGENTS.md:188:F_1 = kappa/24                                         # sanity check for Cauchy normalization
AGENTS.md:191:Cauchy: [z^{n-1}]f(z) = 1/(2*pi*i) * oint f(z)dz/z^n  # NOT 1/(2*pi) — missing i
scripts/adversarial_campaign.py:183:    ("F16_cauchy", "Cauchy: 1/(2*pi*i)", "Cauchy integral normalization", "grep -rn '2.*pi.*oint\\|1.*2.*pi' chapters/ | head -30", "WRONG: 1/(2*pi) missing i (AP120)"),
tmp_standalone_audit/survey_v2_xr.tex:802:$F_1=\kappa/24$ as sanity check (Cauchy normalization
wave2_audit_20260413_001942/C07_higher_genus_foundations.md:226:AP120: Cauchy integral normalization is 1/(2*pi*i), NOT 1/(2*pi). Missing i gives zero for real coefficients. Always verify F_1=kappa/24 as sanity check.
bibliography/references.tex:1116:D. Quillen, \emph{Determinants of Cauchy--Riemann operators over a Riemann surface}, Funktsional. Anal. i Prilozhen. \textbf{19} (1985), no.~1, 37--41.
audit_campaign_20260412_230832/F16_cauchy.md:52:MISSION: Verify every instance of Cauchy integral normalization across all .tex files.
audit_campaign_20260412_230832/F16_cauchy.md:54:CANONICAL: Cauchy: 1/(2*pi*i)
audit_campaign_20260412_231034/F16_cauchy.md:5:- [CRITICAL] `chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:427` — Claims `K_\C(z)=1/(2\pi z)` is the Cauchy kernel / tempered fundamental solution of `\dbar`; the same false normalization is repeated at `:438`, `:442`, `:500`, and `:558`. This is not a notation variant; it is the AP120 missing-`i` error.
audit_campaign_20260412_231034/F16_cauchy.md:19:- [LOW] `chapters/examples/landscape_census.tex:3292` — `landscape_census.tex` does not contain the canonical Cauchy-integral normalization. Its only `Cauchy` hit is `Cauchy--Hadamard`, so it cannot serve as the requested source; the live canonical statement is in `CLAUDE.md:267,347,789`.
wait(call_ZrgijjZGFDwUZOQ4yTrPw4JG) timed out:
codex
I’ve started the cross-volume sweep. While the explorers finish, I’m holding edits until I can distinguish actual contour-normalization errors from nearby already-correct formulas or non-Cauchy uses.
exec
/bin/zsh -lc "sed -n '170,205p' AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r^Vir(z) = (c/2)/z^3 + 2T/z                           # cubic+simple, NOT quartic. d-log absorbs one

# Bridge: k*Omega_tr = Omega/(k+h^v) at generic k
# Averaging (C13): av(r(z)) = kappa for abelian; av(r(z)) + dim(g)/2 = kappa for non-abelian KM

# Central charges (C5-C7)
c_bc(lambda) = 1 - 3(2*lambda-1)^2                    # fermionic; lambda=1/2→1, lambda=2→-26
c_bg(lambda) = 2(6*lambda^2-6*lambda+1)               # bosonic; lambda=1/2→-1, lambda=2→+26
c_bc + c_bg = 0                                        # pointwise; verify at lambda=1: 2+(-2)=0

# Bar complex (C14-C15)
B(A) = T^c(s^{-1} A-bar), A-bar = ker(epsilon)        # AP132: augmentation ideal, NOT bare A
|s^{-1}v| = |v| - 1                                    # desuspension LOWERS; mnemonic: bar=down=s^{-1}
d_bar^2 = 0 ALWAYS; d_fib^2 = kappa*omega_g            # fiberwise only, at g>=1

# Structural constants
MC: d*Theta + (1/2)[Theta,Theta] = 0
QME: hbar*Delta*S + (1/2){S,S} = 0
F_1 = kappa/24                                         # sanity check for Cauchy normalization
F_2 = 7*kappa/5760                                     # NOT 7/2880, NOT 1/5760
collab wait(call_QANpFQX0Wn2pe818W0jSSR0c)
  receivers: 019d87e8-48fd-7712-8172-c763f4249d82, 019d87e8-4ad3-7002-83b4-52d0e1a16ca1
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '40,70p' chapters/examples/examples-complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\{\phi(x), \psi(y)\}_{\mathrm{BV}} = \delta^{(3)}(x-y).
\end{equation}
The BV-BRST differential $Q = \{S_{\text{HT}}, \cdot\}_{\mathrm{BV}}$ acts on local observables $\A_{\text{free}} = \C[\phi_n, \psi_n \mid n \geq 0]$ by:
\begin{align}
Q \cdot \phi_n &= \psi_n, % label removed: eq:Q_free_phi \\
Q \cdot \psi_n &= 0. % label removed: eq:Q_free_psi
\end{align}
One verifies $Q^2 = 0$ directly: $Q^2\phi_n = Q(\psi_n) = 0$.

Here $\phi_n = \frac{1}{n!} \partial_z^n \phi$ denotes the $n$th holomorphic derivative.
\subsubsection{Propagator and Two-Point Function}
The free propagator in HT gauge is the Green's function for the kinetic operator $d_t + \dbar$:
\begin{equation}
% label removed: eq:free_propagator
\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
\end{equation}
In the holomorphic direction, this becomes:
\begin{equation}
% label removed: eq:free_propagator_holo
\langle \phi(z_1) \psi(z_2) \rangle_{\text{holo}} = \frac{1}{z_1 - z_2}.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '20,60p' chapters/examples/examples-complete-core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
In the BV formalism, the field $\phi$ (degree~$0$) is paired with the antifield $\psi$ (degree~$1$) via the BV bracket:
\begin{equation}
\{\phi(x), \psi(y)\}_{\mathrm{BV}} = \delta^{(3)}(x-y).
\end{equation}
The BV-BRST differential $Q = \{S_{\text{HT}}, \cdot\}_{\mathrm{BV}}$ acts on local observables $\A_{\text{free}} = \C[\phi_n, \psi_n \mid n \geq 0]$ by:
\begin{align}
Q \cdot \phi_n &= \psi_n, % label removed: eq:Q_free_phi \\
Q \cdot \psi_n &= 0. % label removed: eq:Q_free_psi
\end{align}
One verifies $Q^2 = 0$ directly: $Q^2\phi_n = Q(\psi_n) = 0$.

Here $\phi_n = \frac{1}{n!} \partial_z^n \phi$ denotes the $n$th holomorphic derivative.
\subsubsection{Propagator and Two-Point Function}
The free propagator in HT gauge is the Green's function for the kinetic operator $d_t + \dbar$:
\begin{equation}
% label removed: eq:free_propagator
\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
\end{equation}
In the holomorphic direction, this becomes:
\begin{equation}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '60,110p' chapters/examples/examples-computing.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Q\phi = \frac{\delta S_{\text{free}}}{\delta \psi} = (d_t + \bar{\partial}_z)\phi.
\]
Passing to holomorphic modes $\phi_n = \frac{1}{n!}\partial_z^n\phi$ gives $Q\phi_n = \psi_n$. Since $\psi$ is the BV antifield (of top cohomological degree in the two-term complex), $Q\psi_n = 0$. One verifies directly that
\[
Q^2\phi_n = Q(\psi_n) = 0,
\]
confirming that $(\A_{\text{free}}, Q)$ is a cochain complex. The Leibniz rule follows from the derivation property of the BV bracket.
\end{proof}

\begin{remark}[Free $\neq$ Trivial Differential]
Even though the theory is \emph{free} (no interaction vertices), the differential $Q$ is not zero. It encodes the classical equations of motion via the BV antifield pairing. ``Free theory'' therefore means $m_{k\ge 3}=0$, not $Q=0$.
\end{remark}

\subsubsection{The $\lambda$-Bracket $m_2$}

The binary operation $m_2$ is governed by the free propagator.

\begin{construction}[Free propagator on $\R \times \C$]
\label{const:free_propagator_detailed}
The Green's function for $(d_t + \bar{\partial}_z)$ is
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '840,910p' chapters/theory/fm-calculus.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
sed: chapters/theory/fm-calculus.tex: No such file or directory
codex
**Cauchy Constraints**
- `CLAUDE.md:267` (C24) fixes the canonical residue extraction: `[z^{n-1}]f(z) = (1/(2πi)) ∮ f(z)\,dz/z^n` and flags “1/(2π)” without the `i` as AP120’s fatal normalization slip (it kills real-coefficient integrals); the adjacent B38 warning (`CLAUDE.md:347`) echoes the same “missing i” prohibition, and `CLAUDE.md:863` re-states the AP120 mantra plus the F₁ = κ/24 sanity check.
- `AGENTS.md:188-195` captures the governance summary: `F₁ = κ/24` is the diagnostic witness for correct Cauchy normalization, and the canonical contour formula is `[z^{n-1}]f(z) = 1/(2πi) ∮ f(z)\,dz/z^n`, explicitly forbidding the “1/(2π)” variant that drops the `i`.
- `chapters/connections/concordance.tex:4098` records that the genus‑1 uniform-weight specialization equals `F₁ = κ/24`, reinforcing that any genus‑1 contour computation must pass the AP120 normalization check before the shadow free energy is trusted.
wait(call_QANpFQX0Wn2pe818W0jSSR0c) 1 agents complete:
  019d87e8-48fd-7712-8172-c763f4249d82 completed: "**Cauchy Constraints**
- `CLAUDE.md:267` (C24) fixes the canonical residue extraction: `[z^{n-1}]f(z) = (1/(2πi)) ∮ f(z)…"
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls chapters/theory | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
algebraic_foundations.aux
algebraic_foundations.tex
bar_cobar_adjunction.aux
bar_cobar_adjunction.tex
bar_cobar_adjunction_curved.tex
bar_cobar_adjunction_inversion.tex
bar_construction.aux
bar_construction.tex
chiral_center_theorem.tex
chiral_hochschild_koszul.aux
collab wait(call_G2IzqfWueGzYU5SW72D4Sdk3)
  receivers: 019d87e8-4ad3-7002-83b4-52d0e1a16ca1
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg --files -g 'fm-*'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "find /Users/raeez/chiral-bar-cobar -name 'fm-calculus.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 2.20s:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '840,910p' chapters/theory/fm-calculus.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
where:
\begin{enumerate}[label=(\roman*)]
\item $\Gamma_2 \subset \FM_2(\R \times \C)$ is a 2-dimensional chain (after integrating over topological directions);
\item The weight form $\omega_2$ is
\[
\omega_2(a,b) = G(z_1 - z_2, t_1 - t_2) \cdot a(z_1, t_1) \cdot b(z_2, t_2) \cdot dt_1 dt_2 d^2z_1 d^2z_2,
\]
with $G$ the HT propagator; for physical realizations this is the propagator produced by Theorem~\ref{thm:physics-bridge};
\item After integrating over $t_1, t_2$ (using the delta-function support of $G$ in the topological direction), we obtain
\[
m_2(a,b) = \Res_{z_1 = z_2} \left[ \frac{a(z_1) b(z_2)}{z_1 - z_2} d^2z_1 d^2z_2 \right].
\]
\end{enumerate}
Setting $\lambda := z_1 - z_2$, the binary operation takes values in formal Laurent series:
\[
m_2(a,b) = \sum_{n \in \Z} \frac{a_{(n)} b}{\lambda^{n+1}} \in \A((\lambda)),
\]
where $a_{(n)} b$ are the mode expansions familiar from vertex algebra theory.
\end{proposition}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n '1/2\\\\pi i' chapters/theory/fm-calculus.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n '1/2\\\\pi' chapters/theory/fm-calculus.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '900,970p' chapters/theory/fm-calculus.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\frac{a(z_1)\, b(z_2)}{z_1 - z_2} = \sum_{n \in \Z} \frac{a_{(n)} b(u)}{\lambda^{n+1}},
\]
where $a_{(n)} b$ are the OPE mode coefficients. The singular terms ($n \geq 0$, poles in $\lambda$) correspond to $d\log\varepsilon_{12}$ and higher-order logarithmic terms in the FM decomposition. The residue at $D_{\{1,2\}}$ picks out the leading singular coefficient:
\[
\Res_{D_{\{1,2\}}}(\omega_2) = \oint_{\theta_{12}} \frac{a(z_1)\, b(z_2)}{z_1 - z_2}\bigg|_{\varepsilon_{12} = 0} d\theta_{12},
\]
which via the Cauchy residue theorem ($\oint e^{-i(n+1)\theta}\, d\theta = 2\pi\, \delta_{n,0}$) extracts the $n$-th mode $a_{(n)} b$.

\textbf{Step 5: Regular vs.\ singular decomposition.}
The Laurent series $m_2(a,b) = \sum_n a_{(n)} b / \lambda^{n+1}$ decomposes as
\begin{align*}
m_2^{\mathrm{sing}}(a,b) &= \sum_{n \geq 0} \frac{a_{(n)} b}{\lambda^{n+1}} \in \lambda^{-1}\A[[\lambda^{-1}]], \\
m_2^{\mathrm{reg}}(a,b) &= \sum_{n < 0} \frac{a_{(n)} b}{\lambda^{n+1}} \in \A[[\lambda]].
\end{align*}
The singular part $m_2^{\mathrm{sing}}$ arises entirely from the residue at $D_{\{1,2\}}$ (the OPE poles), while the regular part $m_2^{\mathrm{reg}}$ comes from the smooth (non-polar) part of the weight form. On cohomology, $m_2^{\mathrm{reg}}$ descends to the commutative product and $m_2^{\mathrm{sing}}$ descends to the $\lambda$-bracket, as in the PVA descent (Theorem~\ref{thm:cohomology_PVA}).

For sign conventions and Koszul factors in the graded setting, see~\cite[Section 4]{CDG20}.
\end{proof}
\subsubsection{The Ternary Operation $m_3$}
\begin{proposition}[Explicit Formula for $m_3$; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '460,520p' chapters/theory/fm-proofs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{itemize}
\item Number of internal edges (propagators): $E = V - 1$ (tree has $V$ vertices and $V-1$ edges);
\item Total half-edges: $3V$ (three per vertex);
\item Half-edges accounted for: $k$ external legs $+$ $2E$ from internal edges;
\item Therefore: $3V = k + 2E = k + 2(V-1)$, giving $V = k - 2$.
\end{itemize}
So a tree diagram contributing to $m_k$ has exactly $V = k-2$ internal vertices and $E = k-3$ internal edges (propagators).

\textbf{Step 2: Integration domain.}
After integrating over the topological ($\R$) directions using the
delta-function support of the standard holomorphic-topological
propagator for the cubic LG realisation, the operation $m_k$ reduces to
an integral over the positions of the $V = k-2$ internal vertices
$z_{v_1}, \ldots, z_{v_{k-2}} \in \C$, with the external points
$z_1, \ldots, z_k$ held fixed (as sources of the spectral parameters).
The integration domain is a subset of $\C^{k-2}$, which has real
dimension $2(k-2)$.

\textbf{Step 3: Form-degree count.}
Each propagator connecting vertex $v_i$ to vertex $v_j$ (or to an external point $z_\ell$) contributes the meromorphic $1$-form
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '500,540p' chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
sed: chapters/connections/relative_feynman_transform.tex: No such file or directory
exec
/bin/zsh -lc "find /Users/raeez/chiral-bar-cobar -name 'relative_feynman_transform.tex'" in /Users/raeez/chiral-bar-cobarwait(call_G2IzqfWueGzYU5SW72D4Sdk3) timed out:
 succeeded in 2.36s:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '480,540p' chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Koszul sign for the symmetry isomorphism
$s\,V \otimes s\,V \xrightarrow{\tau} s\,V \otimes s\,V$
in the category of graded vector spaces.
\end{remark}


\subsection{Mixed-sector computation: bulk-boundary interaction}
\label{subsec:rft-mixed-sector}

The two preceding examples compute the relative Feynman
transform on the closed color alone. The factorization
Swiss-cheese structure has a mixed sector,
$\cE^{\mathrm{mix}}(g, I, J)$ with both closed inputs $I$
(bulk) and open inputs $J$ (boundary), but no worked
example of a mixed-sector computation has appeared in any of
the three chapters (factorization, operadic, algebraic). The
following example gives an explicit computation for the
Heisenberg algebra on $\C \times \R$.

\begin{example}[Mixed-sector relative Feynman transform;

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n '1/2\\\\pi i' chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '400,460p' chapters/theory/raviolo.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item Part~(a) (logarithmic forms and pole orders): Proposition~\ref{prop:orientation_formula}.
\item Part~(b) (factorisation at boundary divisors): Theorem~\ref{thm:AOS_forms}, which establishes the Arnold--Orlik--Solomon relations governing restrictions to boundary strata of $\FM_k(\C)$.
\item Part~(c) (Arnold relations at codimension-$2$ corners): Proposition~\ref{prop:k3_identity}, verified explicitly at $k = 3$ and extended to general $k$ by the same mechanism.
\item Part~(d) (Stokes exactness and corner cancellation): Theorem~\ref{thm:LG_truncation_full}, which demonstrates the full Stokes argument with corner cancellations via Arnold relations.
\end{itemize}
\end{proof}

\begin{theorem}[Bridge from physics to algebra; \ClaimStatusProvedHere]
\label{thm:physics-bridge}
Let $\mathcal{T}$ be a 3d holomorphic--topological quantum field theory on $\R_t \times \C_z$ with:
\begin{enumerate}[label=(\alph*)]
\item \textbf{BV data and HT gauge fixing}: A $(-1)$-symplectic graded field space $\mathcal{F}$ with local action $S \in \mathcal{O}(\mathcal{F})$ satisfying $\{S,S\}_{\mathrm{BV}} = 0$, gauge-fixed in HT gauge with $Q_{\mathrm{BRST}}^2 = 0$.

\item \textbf{One-loop finiteness}: In the holomorphic--topological gauge, one-loop Feynman integrals converge without UV divergences (the Gwilliam--Rabinovich--Williams mechanism~\cite{GRW21} for $d' = 1$).

\item \textbf{Polynomial interactions}: The interaction vertices are polynomial in the fields.
\end{enumerate}
Then the BV--BRST complex $\Obs_{\mathrm{bulk}}$ of $\mathcal{T}$, equipped with configuration-space $A_\infty$ operations, is a logarithmic $\SCchtop$-algebra in the sense of Definition~\ref{def:log-SC-algebra}.
\end{theorem}



thinking
**Exploring search options**

I’m considering whether I could use the shell with `rg` for searching since the explorer might still be running. The instructions suggest using explorers first, but it's been 60 seconds without a return, so a manual search may be necessary. I should check the file types and see if I can access other volumes outside my current working directory. It seems I might have read access in sibling repos, but I can't edit outside writable roots without approval.
thinking
**Assessing search and edit options**

I have a problem: the user wants to search and fix instances across all volumes, but those outside writable roots, like `vol2` and `vol3`, can't be edited. I understand that my writable roots are limited to my current directory, `/tmp`, and `/var/tmp`, so I can't make any changes without approval, which is impossible here. I could search and report any blockers based on what I find. However, since the user only wants to edit assigned files, I'll focus on fixing what I can in `vol1` and documenting the blocked instances elsewhere.
thinking
**Considering truthful edits**

I’m thinking about how to handle the user's request for minimum truthful edits in the assigned files. However, the lack of explicit listings means I might need to consider all volumes, even though my environment restricts me from editing them. It’s important to state any blockers clearly, but there might not be any hits in the other volumes. I could still search them, so using `exec_command` to run `rg` across all volumes could be a way forward.
codex
The constitutional read confirms the exact invariant: any contour coefficient formula must use `1/(2\pi i)`, with `F_1=\kappa/24` as the quick falsifier. I’m running the global grep now and will patch only definite AP120 errors; if sibling volumes are outside the writable sandbox, I’ll still enumerate the blocked hits precisely.
exec
/bin/zsh -lc "sed -n '250,360p' /Users/raeez/chiral-bar-cobar/CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4080,4115p' /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.{tex,sty,cls,md}' '\\\\oint|\\\\frac\\{1\\}\\{2\\\\pi\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.

**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).

**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).

**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).

**C20. Bershadsky-Polyakov Koszul conductor.** `K_BP = c(k) + c(-k-6) = 196`. Self-dual level k=-3. Wrong: K_BP=76 (corrected in Wave 7); K_BP=2 (AP140, confusing with ghost constant C_{(2,1)}=2).

**C21. Igusa cusp form / BKM kappa.** `wt(Phi_10) = 10 = 2*kappa_BKM(K3xE)`, so `kappa_BKM(K3xE) = 5`. Phi_10 = Delta_5^2. Wrong: kappa_BKM = 10 (identifies kappa with full weight); kappa_BKM = 2.

**C22. Dedekind eta.** `eta(tau) = q^{1/24} * prod_{n>=1}(1-q^n)`. Prefactor q^{1/24} ESSENTIAL for modular weight 1/2 transformation. Wrong: dropping q^{1/24}; q^{1/12} prefactor.

**C23. Bicoloured partitions.** `1/eta^2 = q^{-1/12} sum p_{-2}(n) q^n`, coefficients `(1, 2, 5, 10, 20, ...)` (OEIS A002513). Wrong: triangular (1,3,6,10,...) (AP135); ordinary partitions (1,1,2,3,5,...).

**C24. Cauchy integral normalization.** `[z^{n-1}] f(z) = (1/(2*pi*i)) * contour_integral f(z) dz/z^n`. Wrong: 1/(2*pi) (missing i gives zero for real integrands, AP120). Sanity: F_1 = kappa/24.

**C25. MC equation.** `d*Theta + (1/2)[Theta, Theta] = 0`. QME: `hbar*Delta*S + (1/2){S,S} = 0`. Wrong: drop the 1/2 (except odd parity); sign flip.
 succeeded in 51ms:
At degree~$2$: Mumford $\lambda$-class relations from the MC equation
(Proposition~\ref{prop:mumford-from-mc}).
Reconstruction:
the Givental $R$-matrix equals the complementarity propagator
$P_\cA$
(Theorem~\ref{thm:cohft-reconstruction}).
The dressed propagator coefficient
$P^R(D_+,D_-)$ from the edge integral
$\int R(\psi_+)\,R(\psi_-)/(\psi_+ + \psi_-)$
satisfies $P^R(D_+,D_-)=P^R(D_-,D_+)$
(algebraic proof from the symplectic condition
$R(-z)R(z)=1$;
Proposition~\ref{prop:dressed-propagator-resolution}).
For uniform-weight algebras, the shadow obstruction tower free energy
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
is the Hodge-lambda integral
$\int_{\overline{\mathcal{M}}_{g,1}}\lambda_g\psi^{2g-2}$
(Theorem~D). The universal genus-$1$ specialization is the identity
$F_1 = \kappa/24$;
the $\psi$-class CohFT graph sum at $(g,0)$
 succeeded in 51ms:
Total output lines: 795

/Users/raeez/calabi-yau-quantum-groups/notes/physics_4d_n2_hitchin.tex:137: z^I(u) = \oint_{A^I} \Omega_u, \qquad \cF_J(u) = \oint_{B_J} \Omega_u.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_4d_n2_hitchin.tex:163: M_\gamma(u) = |Z_\gamma(u)| = \left| \oint_\gamma \Omega_u \right|,
/Users/raeez/calabi-yau-quantum-groups/notes/physics_4d_n2_hitchin.tex:192:$Z_\gamma(u) = \oint_\gamma \Omega_u$ is exactly the central charge function of the Bridgeland
/Users/raeez/calabi-yau-quantum-groups/notes/physics_4d_n2_hitchin.tex:298: a_I = \oint_{\alpha_I} \lambda_{\SW}, \qquad a_{D,J} = \oint_{\beta_J} \lambda_{\SW} = \frac{\partial \cF}{\partial a_J};
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P06_thm_D_circularity_upgrade.md:591:normalize: $\oint_{A_l} \omega_k = \delta_{kl}$. The period matrix
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P06_thm_D_circularity_upgrade.md:592:$\tau_{kl} = \oint_{B_l} \omega_k \in \mathfrak{H}_g$ determines
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P06_thm_D_circularity_upgrade.md:933: t_k \;=\; \oint_{A_k}\omega_k,
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections2_4_draft.tex:63:($\Omega_{jk}=\oint_{B_k}\omega_j$) and
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections2_4_draft.tex:65:normalised by $\oint_{A_j}\omega_k=\delta_{jk}$. The
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:197:S_{\alpha} = \oint_{\gamma_\alpha} V_\alpha(z) \, dz
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:367:charges $S_i = \oint e^{\alpha_i \cdot \phi/Q}$ dualize to
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:368:$S_i' = \oint e^{-\alpha_i \cdot \phi/Q}$.
/Users/raeez/chiral-bar-cobar/working_notes.tex:333:$A$-period parameters $t_k = \oint_{A_k}\omega_k$.
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1094:($\Omega_{jk}=\oint_{B_k}\omega_j$) and
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1096:normalised by $\oint_{A_j}\omega_k=\delta_{jk}$. The
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:376:= \oint \! c(z)\Bigl(T_{\cA}(z) + \tfrac{1}{2}\,T_{\mathrm{gh}}(z)\Bigr)\,dz
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 775350)
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:2969:The screening operators $Q_i = \oint E_{\alpha_i}(z)\,dz$

thinking
**Searching targeted patterns**

I think it might be helpful to search for more specific patterns in all volumes, particularly looking for instances of `\oint` close to `2\pi` or `dz/(2\pi`. I’ll need to run a more robust search, to make sure I’m capturing the right context and details. It seems like refining my approach could yield better results, so I'll focus on that moving forward.

thinking
**Summarizing AP120 normalization issues**

I’m gathering detailed notes on various instances where the factor `1/(2π)` appears without the expected imaginary unit `i`, which is standard in the Cauchy kernel normalization per complex analysis and residue theory. I plan to highlight definite errors, cases needing context, and likely harmless references, referencing both problematic lines and nearby correct uses of `1/(2π i)` in the repo for clarity. This will include absolute file paths with line numbers, classifications, and notes on surrounding context to show consistency or drift from the normalization convention. I’ll also mention patterns like replicated lines across related files, provide examples from different chapters, and comment on search results related to `\oint` usage to document normalization practices and point toward next steps.
codex
The raw `\oint` sweep is noisy, as expected: most hits are periods, screening operators, BRST charges, or real-angle integrals, not Cauchy normalization. I’m narrowing to contour/residue patterns that can actually violate AP120, so the edits stay mathematically truthful.
exec
/bin/zsh -lc "rg -n --glob '*.{tex,sty,cls,md}' '(\\\\frac\\{1\\}\\{2\\\\pi\\}["'^i]|[''^a-zA-Z]1/'"\\(2\\\\pi\\)["'^i]|[''^a-zA-Z]1/'"\\(2\\\\pi["'^i)]|'"\\\\oint["'^'"\\n]{0,120}(2\\\\pi(?"'! i)|2'"\\\\pi\\\\)|2\\\\pi\\\\,|2\\\\pi\\\\;|2\\\\pi\\\\])|2\\\\pi(?"'! i)[''^'"\\n]{0,120}\\\\oint|\\\\frac\\{d[a-zA-Z]+\\}\\{2\\\\pi["'^i}]|'"\\\\frac\\{1\\}\\{2\\\\pi\\s*\\\\?\\}') /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.{tex,sty,cls,md}' '\\\\frac\\{1\\}\\{2\\\\pi\\}|\\\\oint["'^'"\\n]{0,80}\\\\frac\\{d[a-zA-Z]+\\}\\{2\\\\pi|\\\\oint["'^'"\\n]{0,80}/\\(2\\\\pi|2\\\\pi["'^'"\\n]{0,80}\\\\oint' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: parse error near `)'
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1021:\oint \frac{da}{2\pi i\,a}\;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:54:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:81:K(t-t',z-z') = \frac{1}{2\pi} \frac{\Theta(t-t')}{z-z'},
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:201:m_3(O_1, O_2, O_3) = \frac{\lambda_3}{(2\pi i)} \oint_{|w-z_1| < \varepsilon} \frac{dw}{(w-z_1)(w-z_2)(w-z_3)} \times (\text{contractions}),
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R18_cobar_construction.md:166:\[G(z,w) = -\frac{1}{2\pi} \log|z - w|^2\]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:509:K(z,t) \;=\; \frac{1}{2\pi}\,\frac{\Theta(t)}{z},
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:575:\frac{1}{2\pi}\,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:769:= \oint_{\gamma} \frac{dz}{2\pi(z - w)}\bigg|_{w \to z}
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1799: Kontsevich propagator $\eta_{ij}^K = \frac{1}{2\pi} d\arg(t_i - t_j)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1005:The pair-of-pants amplitude for the Heisenberg is the second quantization $\Gamma(R)$ of the one-particle Bergman restriction $R \colon A^2(D_{\mathrm{out}}) \to A^2(D_{\mathrm{in},1}) \otimes A^2(D_{\mathrm{in},2})$ (Theorem~\ref{V1-thm:heisenberg-one-particle-sewing}). The one-particle restriction has matrix entries $R_{n,m} = \frac{k}{2\pi i} \oint\oint z^{-n-1}w^{-m-1}G_{\mathrm{pants}}(z,w)\,dz\,dw$, satisfying $|R_{n,m}| \leq C\,q^{(n+m)/2}$ from the collar length $t = -\log q$. Hence $R$ is Hilbert--Schmidt and $\Gamma(R)$ is trace class.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:199:\frac{1}{2\pi}\, d\arg(e^{i\theta_i} - e^{i\theta_j})
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:211:where $\eta^K_{ij} = \frac{1}{2\pi}\, d\arg(t_i - t_j)$ is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:239:of $\frac{1}{2\pi}\,d\arg$ from $\Re(\eta_{ij})|_{S^1}$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1503:$R_{n,m} = \frac{k}{2\pi i}\oint\oint z^{-n-1}w^{-m-1}
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32679:$G^g(z_i, z_j) = -\frac{1}{2\pi}\log|z_i - z_j|^2 + h_{ij}^g$
/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1276:\[G(z,w) = -\frac{1}{2\pi} \log|z - w|^2\]
/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1285:\[\langle \phi(z_1) \phi(z_2) \rangle = G(z_1, z_2) = -\frac{1}{2\pi} \log|z_1 - z_2|^2\]
/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1430:&= \frac{1}{2\pi i} \oint_{|u|=1} \frac{du}{u} \quad \text{(by residue theorem)} \\
codex
**AP120 Normalization Survey**

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:54` — “\langle \phi\psi\rangle = \frac{1}{2\pi}\cdot\frac{\Theta(t_1-t_2)}{z_1-z_2}.” Definite AP120 error: the HT propagator is written with a bare `1/(2\pi)` instead of the expected `1/(2\pi i)` that feeds into every Cauchy residue used later. (Compare the canonical normalization in Volume I’s `/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1430`, where `\frac{1}{2\pi i}\oint du/u` is the residue datum that AP120 enforces.) The same bad normalization is duplicated verbatim in `examples-complete-core.tex:36`, `examples-complete-proved.tex:36`, and `examples-complete-conditional.tex:66`; all three should be corrected in the same way.

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:81` — “K(t-t',z-z') = \frac{1}{2\pi}\frac{\Theta(t-t')}{z-z'}.” Definite AP120 error: the holomorphic kernel lacks the `i` factor required for contour integrals (so residues computed from this propagator will be off by `i`). Nearby (same volume) `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:936` already records the corrected propagator `\frac{1}{2\pi i}\cdot\frac{1}{z_i - z_v}`; that contrast makes the missing `i` here even clearer.

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:481` — “G(z_{v_i}, z_{v_j}) = \frac{1}{2\pi(z_{v_i}-z_{v_j})}.” Definite AP120 error: the propagator that builds every `m_k` uses the wrong normalization. Again, the same file (and the adjacent `fm-calculus` discussion) already uses `1/(2\pi i)` in the distributional integrals, so the factor here should be updated to match.

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:870` — “\int_{\R^2} G(...) = \frac{1}{2\pi(z_1-z_2)}.” Definite AP120 error: the time-integrated kernel is missing the `i`, yet Step 3 immediately after introduces `G(z_i,z_v) = \frac{1}{2\pi i}\cdot\frac{1}{z_i-z_v}` (line 936). That juxtaposition proves the expected normalization, so the earlier equality should be `1/(2\pi i)` as well.

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:509` — “K(z,t) = \frac{1}{2\pi}\frac{\Theta(t)}{z}.” Definite AP120 error in the mixed-sector propagator (and again at line 575, where the same `1/(2\pi)` multiplies a boundary residue). The standard `1/(2\pi i)` appears elsewhere in Volume II (e.g., the `\bar\partial` propagator in `chapters/theory/fm-calculus.tex:936`), so these mixed-sector formulae should use that normalization too.

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:427` and `:442` — the proof’s Cauchy kernel is stated as `K_\C(z)=\frac{1}{2\pi z}`. Definite AP120 error: the holomorphic Green’s function is missing the crucial `i` from the Cauchy kernel. (Volume I’s `fm-calculus` file again supplies `1/(2\pi i)` for the same object, showing that the “i” is not optional.)

- `/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1276` — “G(z,w) = -\frac{1}{2\pi}\log|z-w|^2.” Needs context: this is the real Green function for the Laplacian/log, not a contour integral, so the missing `i` is not obviously AP120-critical. Still, the surrounding section contains the correctly normalized residue `(1/2\pi i)\oint` (line 1430), so the deviation should be documented as a conscious “real/imaginary” choice rather than a hidden normalization drift.

- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32679` — “G^g(z_i,z_j) = -\frac{1}{2\pi}\log|z_i-z_j|^2 + h_{ij}^g.” Needs context: similar to the previous bullet, the Green function here is a real logarithm, but AP120 is primarily about residue normalizations—so flag this as “needs context/justification.” For comparison, the later section at `:33444` and `:33467` uses `1/(2\pi i)` for the genus expansion coefficients, demonstrating the canonical normalization elsewhere in the chapter.

- `/Users/raeez/chiral-bar-cobar/chapters/connections/kontsevich_integral.tex:199-239` — all the Kontsevich propagator references read `\frac{1}{2\pi}\,d\arg(...)`. Likely harmless reference/example: those are real 1-form normalizations on the circle; no `i` is expected, and changing them would break the conventional interpretation of `d\arg`. (Still worth keeping an eye on if later sections try to reinterpret them as genuine complex contour integrals.)

- `/Users/raeez/calabi-yau-quantum-groups/notes/physics_4d_n2_hitchin.tex:137-298` — various `\oint_{A/B}` period integrals of the holomorphic 3-form. Likely harmless reference/example: these are genuine period integrals in Hitchin geometry (not Cauchy kernels), so AP120 does not apply.

**Notes**

- I ran `rg` across `/Users/raeez/chiral-bar-cobar`, `/Users/raeez/chiral-bar-cobar-vol2`, and `/Users/raeez/calabi-yau-quantum-groups` to collect every `\oint` and `\frac{1}{2\pi}` occurrence in `.tex/.sty/.cls/.md` files; the hits above are the ones that violate the AP120 normalization or require explicit justification. Thousands of other `\oint` uses (periods, screening operators, etc.) remain untouched because they either carry no `1/(2\pi)` prefactor or already use the correct `1/(2\pi i)` normalization (e.g., `/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1430` and `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:936`).

- Next steps: align each definite-AP120 line with the `1/(2\pi i)` normalization (and propagate the same fix to the duplicate copies), and add a short remark for the “needs context” Green functions explaining why their real-valued normalization is intentional.

thinking
**Inspecting files and searching patterns**

I have a candidate list and I need to check vol2 files to confirm specific lines. I think searching around relative_feynman_transform and thqg_bv_construction_extensions might help. There could also be examples in complete-conditional that my exact search missed, especially with the delta superscript. I want to look at vol3 for direct patterns for `2\pi`, as the user requested all volumes for `\oint` or `\frac{1}{2\pi}`. I'll need to check the git status to see if there are any dirty changes since I don't want to overwrite anything.
exec
/bin/zsh -lc "sed -n '500,585p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex
sed -n '128,170p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex
sed -n '760,776p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '45,75p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex
sed -n '28,45p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex
sed -n '28,45p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex
sed -n '58,78p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex
sed -n '74,90p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short /Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex /Users/raeez/chiral-bar-cobar/CLAUDE.md /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\ClaimStatusProvedHere]
\label{ex:rft-mixed-sector}
\index{Heisenberg algebra!mixed-sector computation|textbf}
\index{mixed-sector computation|textbf}
\index{bulk-boundary interaction!worked example|textbf}
Let $H_\kappa$ be the rank-one Heisenberg algebra of
\S\ref{subsec:rft-heisenberg}, now viewed as a logarithmic
$\SCchtop$-algebra on $\C_z \times \R_t$. The HT propagator is
\begin{equation}\label{eq:mixed-propagator}
K(z,t) \;=\; \frac{1}{2\pi}\,\frac{\Theta(t)}{z},
\end{equation}
with $\Theta(t)$ the Heaviside step function
(Construction~\ref{const:free_propagator_detailed}). We work
at genus~$0$ throughout.

\smallskip\noindent
\textbf{Step 1: fields and colors.}
The closed (bulk) field is $a(z,t) := b(z,t)$, the fundamental
Heisenberg generator, living in the interior
$\C \times \R$.
 succeeded in 51ms:
Q \cdot \psi_n &= 0. % label removed: eq:Q_free_psi
\end{align}
One verifies $Q^2 = 0$ directly: $Q^2\phi_n = Q(\psi_n) = 0$.

Here $\phi_n = \frac{1}{n!} \partial_z^n \phi$ denotes the $n$th holomorphic derivative.
\subsubsection{Propagator and Two-Point Function}
The free propagator in HT gauge is the Green's function for the kinetic operator $d_t + \dbar$:
\begin{equation}
% label removed: eq:free_propagator
\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
\end{equation}
In the holomorphic direction, this becomes:
\begin{equation}
% label removed: eq:free_propagator_holo
\langle \phi(z_1) \psi(z_2) \rangle_{\text{holo}} = \frac{1}{z_1 - z_2}.
\end{equation}

\subsubsection{Computing $m_2$: The $\lambda$-Bracket}
The binary operation $m_2$ is computed using the two-point function. For observables $O_1 = \phi$ and $O_2 = \psi$:
\begin{equation}
 exited 128 in 51ms:
fatal: /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex: '/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex' is outside repository at '/Users/raeez/chiral-bar-cobar'


thinking
**Analyzing sed command issues**

It seems the sed command caused some odd concatenation with multiple files, but it’s enough for now. I’m also wondering if line 66 in examples-complete-conditional is missing due to maximum output limits. I should check the lines in Vol II to ensure they have the correct normalization. Some variants like `\frac{\delta^{ab}}{2\pi}` might not be captured, so I'll search for patterns in live .tex files in Vol II. I anticipate many more issues as I go through.
thinking
**Clarifying search parameters**

In reviewing the thqg_bv file, I noticed line 135 doesn't have `\oint` or `\frac{1}{2\pi}`, although line 769 does. There's also the AP120 issue. I’m considering if we should include this, since it relates to the Cauchy normalization that the user requested. To make sure we catch any missed variations, I should perform an exhaustive search. Using the audit artifact fix_wave_C might help outline the problems. I’ll focus on searching Vol II for all instances of `2\pi(` and `/2\pi` in the chapters directly.
codex
I’ve isolated the live AP120 surface. Volume I’s `\frac{1}{2\pi}` hits are all real-angle or scalar Green-function formulas, not contour normalization failures; the live defects are in Volume II’s HT/holomorphic kernels, plus one explicit `\oint dz/(2\pi(z-w))` residue formula.
exec
/bin/zsh -lc "sed -n '60,75p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex
sed -n '132,160p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex
sed -n '565,580p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '2\\\\pi\\(|/2\\\\pi|\\\\delta\\"'^'"\\{ab\\}\\}/\\{2\\\\pi|\\\\frac\\{\\\\delta\\"'^'"\\{ab\\}\\}\\{2\\\\pi|\\\\oint["'^'"\\n]{0,120}2\\\\pi\\(' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$Q$ now has a \emph{quadratic} term from the gauge
self-interaction.

The HT propagator is the same as for abelian CS:
\begin{equation}\label{eq:su2-propagator}
\langle A_z^a(t_1,z_1)\, A_{\bar z}^b(t_2,z_2) \rangle
= \frac{\delta^{ab}}{2\pi} \cdot
 \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
\end{equation}
The Killing form $\delta^{ab}$ (normalized to
$\operatorname{tr}(t^a t^b) = \frac{1}{2}\delta^{ab}$
in the fundamental representation) couples the color indices.

\subsubsection{Binary operation $m_2$ and $\lambda$-bracket}

The binary operation $m_2$ is computed from the propagator
% label removed: eq:thqg-bv-ext-prop
G(z_1, z_2;\, t_1, t_2)
\;=\;
\frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)},
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:481:G(z_{v_i}, z_{v_j}) = \frac{1}{2\pi(z_{v_i} - z_{v_j})}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:99:\{\phi(z_1)\,{}_\lambda\,\psi(z_2)\} = \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1686:$K(z,t;\,z',t')=\Theta(t-t')/(2\pi(z-z'))$. The reflected
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1690:=\frac{\Theta(t-t')}{2\pi(z-z')}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1691:+\frac{\Theta(t+t')}{2\pi(z-\bar z')}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:129:\langle T(z_1) \mu(z_2) \rangle = \frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:158:&= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)} \left( T(z_2) \partial_2 \mu(z_2) + \frac{c}{24} \partial_2^3 \mu(z_2) \right).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:757:\langle T(z_1) \mu(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)},\\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:758:\langle W(z_1) \chi(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1057:$\langle T(z_1)\,\mu(z_2) \rangle = \Theta(t_1-t_2)/(2\pi(z_1-z_2))$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:61:\langle T(z_1) \mu(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)},\\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:62:\langle W(z_1) \chi(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1063:$\langle T(z_1)\,\mu(z_2) \rangle = \Theta(t_1-t_2)/(2\pi(z_1-z_2))$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:2015:conical singularity with deficit angle $2\pi(1 - \sqrt{1 - 24h/c})$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:139:\langle T(z_1) \mu(z_2) \rangle = \frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:168:&= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)} \left( T(z_2) \partial_2 \mu(z_2) + \frac{c}{24} \partial_2^3 \mu(z_2) \right).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:659:\langle T(z_1) \mu(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)},\\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:660:\langle W(z_1) \chi(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:445:The weight forms $\omega_n$ are constructed from time-ordered propagators (Convention~\ref{const:regularized_mk}). Each propagator $G(z_p, z_q; t_p, t_q) = \Theta(t_p - t_q)/(2\pi(z_p - z_q))$ connects points $p$ and $q$ with the time-ordering constraint $t_p > t_q$ enforced by the Heaviside function $\Theta(t_p - t_q)$. The integration chain $\Gamma_n$ is supported on the simplex $\{t_1 > t_2 > \cdots > t_n\} \subset \FM_n(\R)$ (the associahedron chamber).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:660:G(z_i, z_j; t_i, t_j) \sim \frac{\delta(t_i - t_j)}{2\pi(z_i - z_j)} + \text{regular terms}.
exec
/bin/zsh -lc "python - <<'PY'
import os
for p in [
'/Users/raeez/chiral-bar-cobar-vol2',
'/Users/raeez/calabi-yau-quantum-groups']:
    print(p, 'exists=', os.path.exists(p), 'islink=', os.path.islink(p))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "python3 - <<'PY'
import os
for p in [
'/Users/raeez/chiral-bar-cobar-vol2',
'/Users/raeez/calabi-yau-quantum-groups']:
    print(p, 'exists=', os.path.exists(p), 'islink=', os.path.islink(p), 'realpath=', os.path.realpath(p))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2 exists= True islink= False realpath= /Users/raeez/chiral-bar-cobar-vol2
/Users/raeez/calabi-yau-quantum-groups exists= True islink= False realpath= /Users/raeez/calabi-yau-quantum-groups

thinking
**Testing file permissions**

I need to test if apply_patch can work outside the root directory. I think it likely won't patch there, but I'm not completely sure. It might be best to hold off until I'm more confident. I could try using the shell command `touch` to check permissions outside, but that could be destructive. Alternatively, I can use `test -w` to see if the file is writable with `[[ -w file ]]`. Let’s figure this out carefully!
exec
/bin/zsh -lc 'for f in /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex /Users/raeez/calabi-yau-quantum-groups/notes/physics_4d_n2_hitchin.tex; do if [ -w "$f" ]; then echo "writable $f"; else echo "not-writable $f"; fi; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git -C /Users/raeez/chiral-bar-cobar-vol2 status --short -- chapters/examples/examples-complete.tex chapters/examples/examples-complete-core.tex chapters/examples/examples-complete-proved.tex chapters/examples/examples-complete-conditional.tex chapters/examples/examples-computing.tex chapters/examples/w-algebras.tex chapters/examples/w-algebras-stable.tex chapters/examples/w-algebras-virasoro.tex chapters/examples/w-algebras-w3.tex chapters/examples/rosetta_stone.tex chapters/connections/relative_feynman_transform.tex chapters/connections/thqg_bv_construction_extensions.tex chapters/theory/fm-calculus.tex chapters/theory/fm-proofs.tex chapters/theory/raviolo.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git -C /Users/raeez/chiral-bar-cobar status --short' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
not-writable /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex
not-writable /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex
not-writable /Users/raeez/calabi-yau-quantum-groups/notes/physics_4d_n2_hitchin.tex
 succeeded in 51ms:
 M chapters/connections/relative_feynman_transform.tex
 M chapters/examples/rosetta_stone.tex
 succeeded in 51ms:
Total output lines: 408

 M AGENTS.md
 M CLAUDE.md
 M Makefile
 M README.md
 M appendices/_sl2_yangian_insert.tex
 M appendices/nonlinear_modular_shadows.tex
 M appendices/ordered_associative_chiral_kd.tex
 M appendices/signs_and_shifts.tex
 M appendices/spectral_higher_genus.tex
 M bibliography/references.tex
 M chapters/connections/arithmetic_shadows.tex
 M chapters/connections/bv_brst.tex
 D chapters/connections/casimir_divisor_core_transport.tex
 M chapters/connections/concordance.tex
 D chapters/connections/dg_shifted_factorization_bridge.tex
 M chapters/connections/editorial_constitution.tex
 M chapters/connections/entanglement_modular_koszul.tex
 M chapters/connections/feynman_connection.tex
codex
The writable surface isn’t just `chapters/`; there are live `standalone/*.tex` duplicates inside Volume I. I’m checking those now so I don’t miss an editable AP120 copy while the sibling-volume files remain sandbox-blocked.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\frac\\{1\\}\\{2\\\\pi\\}|/\\(2\\\\pi|2\\\\pi\\(' /Users/raeez/chiral-bar-cobar/standalone /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:958:$1/(2\pi)^6$ before normalization.
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:970:to $\zeta(3)/(2\pi i)^3$.
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:927:$(2g)!/(2\pi)^{2g}$.
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:2640:\frac{1}{2\pi}\,
/Users/raeez/chiral-bar-cobar/appendices/signs_and_shifts.tex:1475:$1/(2\pi i)$ in Kontsevich accounts for the residue normalization;
/Users/raeez/chiral-bar-cobar/appendices/combinatorial_frontier.tex:369:$\lambda_g^{FP} \sim 2/(2\pi)^{2g}$, super-exponential decay. This guarantees convergence of the genus expansion $\sum_g F_g(\cA)\,x^{2g}$ for all finite~$\kappa$ (Proposition~\ref{prop:bivariate-gf}).
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:1314:Large $g$ & $\sim 2d/(2\pi)^{2g}$ &
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:3929:The quasi-modularity of $E_2$ (it transforms as $E_2(-1/\tau) = \tau^2 E_2(\tau) + 12\tau/(2\pi i)$) reflects the holomorphic anomaly: the genus-1 partition function is \emph{not} modular, and the failure of modularity is controlled by $(k+2) = k + h^\vee$, i.e., by the same curvature $\mcurv{1}$ that obstructs $\dfib^{\,2} = 0$ (Convention~\ref{conv:higher-genus-differentials}).
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:549:In each case, $F_g$ is a linear function of~$k$, reflecting the factored form $F_g = \frac{3}{4}(k+2) \cdot \lambda_g^{FP}$. At critical level $k = -2$, every entry vanishes: $F_g(\widehat{\mathfrak{sl}}_{2,-2}) = 0$ for all~$g$. The super-exponential decay $\lambda_g^{FP} \sim 2/(2\pi)^{2g}$ (cf.\ Proposition~\ref{prop:fp-coefficients}) ensures that the genus expansion $\sum_g F_g$ converges for all $k \neq -2$.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1836:so the series converges geometrically with ratio $1/(2\pi)^2 \approx 0.025$.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1854:In particular, $|F_{g+1}/F_g| \to 1/(2\pi)^2 \approx 0.025$, giving geometric convergence.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1867:\item \emph{Convergence.} $\sum_{g=1}^\infty |F_g(\mathcal{A})| < \infty$, with geometric ratio $|F_{g+1}/F_g| \to 1/(2\pi)^2$.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1869:\item \emph{Contrast with string theory.} String amplitudes $A_g^{\mathrm{string}} \sim C^g (2g)!$ diverge, while $F_g \sim 2\kappa/(2\pi)^{2g}$ decays geometrically. The distinction is structural: $F_g$ extracts the single tautological intersection number $\int \psi^{2g-2}\lambda_g$, whose Bernoulli decay overwhelms the $(2g)!$ growth of $|B_{2g}|$.
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2506:$1/(2\pi)^2 \approx 0.02533$ from above
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:3414:formula $|B_{2g}| \sim 2(2g)!/(2\pi)^{2g}$
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:3437:$1/(2\pi)^2 \approx 0.02533$:
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:3445:\lambda_g^{\mathrm{FP}}$ & $\text{ratio} - 1/(2\pi)^2$ \\
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:3471:Our genus expansion converges geometrically ($|F_g| \sim 2|\kappa|/(2\pi)^{2g}$), in sharp contrast with string amplitudes which grow as $(2g)!$ and diverge (Remark~\ref{rem:convergence-vs-string}). The distinction: $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ extracts a \emph{single} tautological intersection number, while string amplitudes integrate over all of $\overline{\mathcal{M}}_g$ with all $\lambda$-classes. The factored form shows the algebra contributes only through~$\kappa$, with the decay rate universal (Theorem~\ref{thm:genus-universality}).
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:3588:ratio $F_{g+1}/F_g \to 1/(2\pi)^2$ is $\kappa$-independent).
/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:3615:$\lambda_g \sim 2/(2\pi)^{2g}$ decreases super-exponentially.
exec
/bin/zsh -lc "sed -n '2628,2650p' /Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex
sed -n '1170,1185p' /Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex
sed -n '383,400p' /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The BV propagator~$P_g$ differs from the bar
propagator~$d\log E(z,w)$ by this harmonic term:
\[
P_g(z,w)
\;=\;
d\log E(z,w)
\;+\;
h_g(z,w),
\qquad
h_g
\;=\;
\frac{1}{2\pi}\,
(\operatorname{Im}\Omega)^{-1}_{ab}\,
d\bar z_a \wedge dz_b.
\]
Each insertion of~$h_g$ into a Feynman graph vertex produces
a harmonic correction to the BV amplitude.  At the quartic
level ($r = 4$), the correction is
\begin{equation}\label{eq:quartic-obstruction}
exec
/bin/zsh -lc "sed -n '1788,1805p' /Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex
sed -n '1498,1508p' /Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{Kontsevich integral!bar complex}
For $\cA = \widehat{\fg}_k$, the Feynman transform identification
$\barB^{\mathrm{full}}(\cA) \simeq \mathrm{FT}_{\mathcal{M}\mathrm{od}}(\cA)$
\textup{(}Theorem~\textup{\ref{thm:prism-higher-genus}(ii))}
produces universal Vassiliev invariants when specialized to
configuration spaces of circles:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The restriction
 $\overline{C}_n(X) \rightsquigarrow C_n(S^1)$
 \textup{(}from complex curve to real circle\textup{)} sends the
 holomorphic propagator $\eta_{ij} = d\log(z_i - z_j)$ to the
 Kontsevich propagator $\eta_{ij}^K = \frac{1}{2\pi} d\arg(t_i - t_j)$.
\item Under this restriction, the bar complex weight systems
 $W_\Gamma\colon \fg^{\otimes n} \to \mathbb{C}$ match the
 classical weight systems of Vassiliev theory, with the
 Lie algebra $\fg$ providing the weight system as in
 Bar-Natan~\cite{BarNatan95}.
\item The genus expansion
\end{theorem}

codex
I’ve narrowed the live defect set to explicit holomorphic/HT kernels of the form `1/(2\pi(z-w))`, `\Theta/(2\pi(z-w))`, `\delta^{ab}/(2\pi)·1/(z-w)`, and one contour `dz/(2\pi(z-w))`. I’m collecting exact line numbers now so the final report is concrete even where the sandbox blocks the patch.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex | sed -n '50,60p;523,531p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex | sed -n '132,160p;766,772p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex | sed -n '78,101p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex | sed -n '507,579p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex | sed -n '32,40p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex | sed -n '32,40p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex | sed -n '62,70p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex | sed -n '442,447p;657,661p;863,871p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex | sed -n '478,484p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex | sed -n '554,560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex | sed -n '136,170p;656,662p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex | sed -n '126,160p;754,760p;1054,1059p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex | sed -n '58,63p;1060,1065p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex | sed -n '122,158p'
nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '1684,1692p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    50	\subsubsection{Propagator and Two-Point Function}
    51	The free propagator in HT gauge is the Green's function for the kinetic operator $d_t + \dbar$:
    52	\begin{equation}
    53	% label removed: eq:free_propagator
    54	\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
    55	\end{equation}
    56	In the holomorphic direction, this becomes:
    57	\begin{equation}
    58	% label removed: eq:free_propagator_holo
    59	\langle \phi(z_1) \psi(z_2) \rangle_{\text{holo}} = \frac{1}{z_1 - z_2}.
    60	\end{equation}
   523	
   524	The HT propagator is the same as for abelian CS:
   525	\begin{equation}% label removed: eq:su2-propagator
   526	\langle A_z^a(t_1,z_1)\, A_{\bar z}^b(t_2,z_2) \rangle
   527	= \frac{\delta^{ab}}{2\pi} \cdot
   528	 \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
   529	\end{equation}
   530	The Killing form $\delta^{ab}$ (normalized to
   531	$\operatorname{tr}(t^a t^b) = \frac{1}{2}\delta^{ab}$
 succeeded in 51ms:
   132	% label removed: eq:thqg-bv-ext-prop
   133	G(z_1, z_2;\, t_1, t_2)
   134	\;=\;
   135	\frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)},
   136	\end{equation}
   137	where $\Theta$ is the Heaviside step function. This is the
   138	\emph{retarded} Green function for $\bar\partial$ on
   139	$\bC \times \bR_+$: the holomorphic factor
   140	$1/(2\pi(z_1 - z_2))$ is the $\bar\partial$-Green kernel on
   141	$\bC$, and the topological factor $\Theta(t_1 - t_2)$ enforces
   142	causal (time-)ordering. In the distributional sense,
   143	\[
   144	\bar\partial_{z_1} G(z_1, z_2;\, t_1, t_2)
   145	= \delta^{(2)}(z_1 - z_2)\,\Theta(t_1 - t_2),
   146	\]
   147	so $G$ inverts $\bar\partial_{z_1}$ on the causal half-space
   148	$\{t_1 > t_2\}$, not on all of $\bC \times \bR$. The retarded
   149	boundary condition (vanishing for $t_1 < t_2$) is the HT analogue
   150	of the Feynman $i\epsilon$ prescription.
   151	\end{definition}
 succeeded in 51ms:
   507	$\SCchtop$-algebra on $\C_z \times \R_t$. The HT propagator is
   508	\begin{equation}\label{eq:mixed-propagator}
   509	K(z,t) \;=\; \frac{1}{2\pi}\,\frac{\Theta(t)}{z},
   510	\end{equation}
   511	with $\Theta(t)$ the Heaviside step function
   512	(Construction~\ref{const:free_propagator_detailed}). We work
   513	at genus~$0$ throughout.
   514	
   515	\smallskip\noindent
   516	\textbf{Step 1: fields and colors.}
   517	The closed (bulk) field is $a(z,t) := b(z,t)$, the fundamental
   518	Heisenberg generator, living in the interior
   519	$\C \times \R$.
   520	The open (boundary) field is $\beta(t') := b(0,t')$, the
   521	restriction of the Heisenberg generator to the boundary
   522	$\{z = 0\} \times \R \simeq \R$. In the two-colored bar
   523	complex, the bulk field carries the closed color and the boundary
   524	field carries the open color. The mixed bar element
   525	\[
   526	\xi_{\mathrm{mix}}
 succeeded in 51ms:
    78	\label{const:free_propagator_detailed}
    79	The Green's function for $(d_t + \bar{\partial}_z)$ is
    80	\[
    81	K(t-t',z-z') = \frac{1}{2\pi} \frac{\Theta(t-t')}{z-z'},
    82	\]
    83	with $\Theta$ the Heaviside step function. It produces the unique distributional solution of $(d_t+\bar{\partial}_z)K = \delta(t-t')\delta^{(2)}(z-z')$.
    84	\end{construction}
    85	
    86	\begin{proposition}[Explicit $\lambda$-brackets; \ClaimStatusProvedHere]
    87	\label{prop:free_lambda_brackets_detailed}
    88	The only nonvanishing $\lambda$-bracket is
    89	\begin{align}
    90	\label{eq:free_lambda_phi_psi}
    91	\{\phi_n \,{}_\lambda\, \psi_m\} &= \binom{n+m}{n} (-1)^n \lambda^{n+m},
    92	\end{align}
    93	with all others obtained from sesquilinearity and the $Q$-derivation property.
    94	\end{proposition}
    95	
    96	\begin{proof}
    97	Contracting with the propagator yields
 succeeded in 50ms:
    32	\subsubsection{Propagator and Two-Point Function}
    33	The free propagator in HT gauge is the Green's function for the kinetic operator $d_t + \dbar$:
    34	\begin{equation}
    35	% label removed: eq:free_propagator
    36	\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
    37	\end{equation}
    38	In the holomorphic direction, this becomes:
    39	\begin{equation}
    40	% label removed: eq:free_propagator_holo
    32	\subsubsection{Propagator and Two-Point Function}
    33	The free propagator in HT gauge is the Green's function for the kinetic operator $d_t + \dbar$:
    34	\begin{equation}
    35	\label{eq:free_propagator}
    36	\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
    37	\end{equation}
    38	In the holomorphic direction, this becomes:
    39	\begin{equation}
    40	\label{eq:free_propagator_holo}
    62	
    63	The HT propagator is the same as for abelian CS:
 succeeded in 50ms:
   442	\textbf{Step 5 (Non-consecutive subsets contribute zero).}
   443	Let $S \subseteq \{1,\ldots,n\}$ with $|S| \geq 2$ be non-consecutive, i.e., there exist $p, q \in S$ with $p < r < q$ for some $r \notin S$. We show that $\int_{\Gamma_n \cap D_S} \Res_{D_S}(\omega_n) = 0$.
   444	
   445	The weight forms $\omega_n$ are constructed from time-ordered propagators (Convention~\ref{const:regularized_mk}). Each propagator $G(z_p, z_q; t_p, t_q) = \Theta(t_p - t_q)/(2\pi(z_p - z_q))$ connects points $p$ and $q$ with the time-ordering constraint $t_p > t_q$ enforced by the Heaviside function $\Theta(t_p - t_q)$. The integration chain $\Gamma_n$ is supported on the simplex $\{t_1 > t_2 > \cdots > t_n\} \subset \FM_n(\R)$ (the associahedron chamber).
   446	
   447	On the boundary divisor $D_S$ where points indexed by $S$ collide holomorphically, the time-ordering constraint requires the internal propagators within the cluster $S$ to respect the planar order. If $S$ is non-consecutive (say $S = \{p, q\}$ with $p < r < q$ and $r \notin S$), then the collision $z_p \to z_q$ occurs while point $r$ (with $t_p > t_r > t_q$) remains at finite distance. The factorization of the weight form on $D_S$ requires a propagator connecting $z_p$ and $z_q$ \emph{internally} within the cluster, but the time-ordering forces the path to pass through the intermediate time $t_r$. Since $r \notin S$, point $r$ is at a macroscopic distance from the cluster center, and the internal propagator $G(z_p, z_q)$ does not factor through the operadic decomposition $D_S \cong \FM_r(\C) \times \FM_{|S|}^{\mathrm{red}}(\C)$: the time-ordered propagator kernel has $\Theta(t_p - t_q) = \Theta(t_p - t_r)\Theta(t_r - t_q)$, so the $t_r$-integral couples the inner and outer operations in a way that prevents factorization.
   657	
   658	For the physical realizations covered by Theorem~\ref{thm:physics-bridge}, the propagator $G(z_i, z_j; t_i, t_j)$ has a singularity of the form
   659	\[
   660	G(z_i, z_j; t_i, t_j) \sim \frac{\delta(t_i - t_j)}{2\pi(z_i - z_j)} + \text{regular terms}.
   661	\]
   863	\textbf{Step 1: Propagator in HT gauge.}
   864	The propagator $K(z,t) = \Theta(t)/(2\pi z)$ has a simple pole at $z = 0$ in the holomorphic direction and distributional support (the Heaviside function $\Theta(t)$) in the topological direction. The full two-point propagator is
   865	\[
   866	G(z_1, z_2; t_1, t_2) = K(z_1 - z_2,\, t_1 - t_2) = \frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)}.
   867	\]
   868	In the distributional sense (integrating over the topological direction $t = t_1 - t_2$ against test functions supported near $t = 0$), $\Theta(t)$ acts as a half-delta: $\int_\R \Theta(t)\, f(t)\, dt = \int_0^\infty f(t)\, dt$. For the HT theory, the relevant limit is the time-ordered contraction, which after integrating out $t_1, t_2$ with the time-ordering constraint gives
   869	\[
   870	\int_{\R^2} G(z_1, z_2; t_1, t_2)\, dt_1\, dt_2 = \frac{1}{2\pi(z_1 - z_2)}.
   871	\]
 succeeded in 51ms:
   136	The free propagator for the pair $(T, \mu)$ is determined by inverting the kinetic operator. For operators at holomorphic points $(t_1, z_1)$ and $(t_2, z_2)$:
   137	\begin{equation}
   138	% label removed: eq:vir-propagator
   139	\langle T(z_1) \mu(z_2) \rangle = \frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)}.
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
   155	a_1 &= \partial T. & \text{(derivative term)}




thinking
**Organizing output findings**

I notice that the output includes several files, but there might be even more not covered due to the maximum output limit. I could try to gather candidate line numbers using a search tool, which might simplify things. However, since the user specifically wants exact edits, I’ll need to mention each file and the exact replacements made.

I guess it might be easier to group findings by files if they share the same edit, but I'll be careful to follow the user's instructions closely.
thinking
**Assessing file modifications**

I see that many findings may exceed 20 lines, but the user has requested an exhaustive list. I’ll need to check for any AP120 errors in volume 1 and volume 3. It looks like volume 3 only contains period integrals and not certain contour kernels, so I'll focus on volume 2. I need to verify if some lines in volume 2 have already been modified, but my git status only shows two files as modified. 

It seems that I can't patch since the files are not writable. There could be a permission issue, potentially due to running from a different working directory or because of sandbox restrictions. It might be helpful to mention this as a possible blocker.
thinking
**Exploring patch options**

I’m considering whether I can still patch with apply_patch. It might bypass OS permissions since this tool isn’t shell-based, but it likely still follows sandbox restrictions. If there’s a possibility for a no-op patch, I should check that, but it seems apply_patch doesn’t allow for that. 

I could attempt to modify a copy of the file outside the root, but that feels destructive. Since the user wants a fix, perhaps I could use exec_command with `perl -0pi`, but that feels too intrusive, so I think I'll hold off on that for now.
thinking
**Verifying patterns in repo**

I'm thinking about whether I need to spawn a worker. Instead, I should maybe verify there are no AP120 violations in the live sources using targeted regex searches. I can search the current repo's .tex files for patterns related to missing 'i' with contour integrals. I’ll use regex expressions to check for specific forms and run a targeted verification for patterns like `\oint.*2\pi(` and `\frac{1}{2\pi}\oint`.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\frac\\{1\\}\\{2\\\\pi\\}\\\\oint|\\\\oint["'^'"\\n]{0,80}\\\\frac\\{d[a-zA-Z]+\\}\\{2\\\\pi\\(|\\\\oint["'^'"\\n]{0,80}/\\(2\\\\pi\\(|\\\\Theta\\(["'^'"\\n]*\\)/(2\\\\pi\\(|\\\\Theta\\(["'^'"\\n]*\\)/\\(2\\\\pi\\(|\\\\frac\\{\\\\Theta\\(["'^}]+'"\\)\\}\\{2\\\\pi\\(|\\\\frac\\{\\\\delta\\"'^'"\\{ab\\}\\}\\{2\\\\pi\\}' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\frac\\{1\\}\\{2\\\\pi\\}\\\\oint|\\\\oint["'^'"\\n]{0,80}\\\\frac\\{d[a-zA-Z]+\\}\\{2\\\\pi\\(|\\\\oint["'^'"\\n]{0,80}/\\(2\\\\pi\\(|\\\\Theta\\(["'^'"\\n]*\\)/(2\\\\pi\\(|\\\\Theta\\(["'^'"\\n]*\\)/\\(2\\\\pi\\(|\\\\frac\\{\\\\Theta\\(["'^}]+'"\\)\\}\\{2\\\\pi\\(|\\\\frac\\{\\\\delta\\"'^'"\\{ab\\}\\}\\{2\\\\pi\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:\\frac\{1\}\{2\\pi\}\\oint|\\oint[^\n]{0,80}\\frac\{d[a-zA-Z]+\}\{2\\pi\(|\\oint[^\n]{0,80}/\(2\\pi\(|\\Theta\([^\n]*\)/(2\\pi\(|\\Theta\([^\n]*\)/\(2\\pi\(|\\frac\{\\Theta\([^}]+\)\}\{2\\pi\(|\\frac\{\\delta\^\{ab\}\}\{2\\pi\})
    ^
error: unclosed group
 exited 2 in 52ms:
rg: regex parse error:
    (?:\\frac\{1\}\{2\\pi\}\\oint|\\oint[^\n]{0,80}\\frac\{d[a-zA-Z]+\}\{2\\pi\(|\\oint[^\n]{0,80}/\(2\\pi\(|\\Theta\([^\n]*\)/(2\\pi\(|\\Theta\([^\n]*\)/\(2\\pi\(|\\frac\{\\Theta\([^}]+\)\}\{2\\pi\(|\\frac\{\\delta\^\{ab\}\}\{2\\pi\})
    ^
error: unclosed group

thinking
**Considering regex issues**

I'm looking into some regex issues, and I think there might be a simpler approach. Instead of using complex regular expressions, using multiple fixed strings could be much more straightforward. This seems like a more efficient way to handle the situation. It makes me wonder if I might have overcomplicated things in the past. Sometimes simplicity really is key, right? I'll definitely prioritize clarity and ease of use going forward!
codex
The current repo scan came back clean on the AP120-specific patterns I care about. I’m doing one last fixed-string verification pass rather than a broad regex, since the broad pattern hit ripgrep parsing limits and I don’t want false positives from real-angle `d\arg` formulas.
exec
/bin/zsh -lc "rg -n --glob '*.tex' -e '\\\\frac{1}{2\\\\pi}\\\\oint' -e '\\\\oint' -e '\\\\frac{\\\\delta"'^{ab}}{2'"\\\\pi}' -e '2\\\\pi(z' -e '/(2\\\\pi(z' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/standalone" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\frac{1}{2\\pi}\\oint)|(?:\\oint)|(?:\\frac{\\delta^{ab}}{2\\pi})|(?:2\\pi(z)|(?:/(2\\pi(z)
                ^^
error: unclosed counted repetition
exec
/bin/zsh -lc "rg -n --glob '*.tex' -e '\\\\frac{1}{2\\\\pi}\\\\oint' -e '\\\\frac{\\\\delta"'^{ab}}{2'"\\\\pi}' -e '2\\\\pi(z' -e '/(2\\\\pi(z' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\\frac{1}{2\\pi}\\oint)|(?:\\frac{\\delta^{ab}}{2\\pi})|(?:2\\pi(z)|(?:/(2\\pi(z)
                ^^
error: unclosed counted repetition

thinking
**Considering regex commands**

I’m thinking about how `rg` uses regex and how braces are interpreted. I need to make sure I use `-F` for fixed strings, but there might be something tricky here. Should I use multiple commands in the shell? The instructions suggest avoiding chaining commands, so maybe it’s better to run separate executions in parallel. I want to keep everything simple and straightforward as I work through this process!
exec
/bin/zsh -lc "rg -n -F --glob '*.tex' '\\frac{1}{2\\pi}\\oint' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob '*.tex' '/(2\\pi(z' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob '*.tex' '2\\pi(z' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob '*.tex' '\\frac{\\delta"'^{ab}}{2'"\\pi}' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/standalone" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 52ms:


thinking
**Searching for patterns**

I'm looking into the current repository and noticing there's no direct AP120 patterns. I think I might need to search through volume 2 for similar fixed strings to identify candidate lines. I already have some fixed strings like `2\pi(z` and `\frac{\delta^{ab}}{2\pi}` in mind. It could also be a good idea to search for `/(2\pi(z` in volume 3 to confirm there aren't any, so searching in both volumes separately makes sense.
exec
/bin/zsh -lc "rg -n -F --glob '*.tex' '\\frac{\\delta"'^{ab}}{2'"\\pi}' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob '*.tex' '2\\pi(z' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob '*.tex' '/(2\\pi(z' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F --glob '*.tex' '\\frac{1}{2\\pi}\\oint' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:527:= \frac{\delta^{ab}}{2\pi} \cdot
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:66:= \frac{\delta^{ab}}{2\pi} \cdot
 exited 1 in 51ms:

 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1057:$\langle T(z_1)\,\mu(z_2) \rangle = \Theta(t_1-t_2)/(2\pi(z_1-z_2))$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1063:$\langle T(z_1)\,\mu(z_2) \rangle = \Theta(t_1-t_2)/(2\pi(z_1-z_2))$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1686:$K(z,t;\,z',t')=\Theta(t-t')/(2\pi(z-z'))$. The reflected
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:445:The weight forms $\omega_n$ are constructed from time-ordered propagators (Convention~\ref{const:regularized_mk}). Each propagator $G(z_p, z_q; t_p, t_q) = \Theta(t_p - t_q)/(2\pi(z_p - z_q))$ connects points $p$ and $q$ with the time-ordering constraint $t_p > t_q$ enforced by the Heaviside function $\Theta(t_p - t_q)$. The integration chain $\Gamma_n$ is supported on the simplex $\{t_1 > t_2 > \cdots > t_n\} \subset \FM_n(\R)$ (the associahedron chamber).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:140:$1/(2\pi(z_1 - z_2))$ is the $\bar\partial$-Green kernel on
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:156:with $G^{\mathrm{hol}}(z_1,z_2) = 1/(2\pi(z_1 - z_2))$ and
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:129:\langle T(z_1) \mu(z_2) \rangle = \frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:158:&= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)} \left( T(z_2) \partial_2 \mu(z_2) + \frac{c}{24} \partial_2^3 \mu(z_2) \right).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:757:\langle T(z_1) \mu(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)},\\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:758:\langle W(z_1) \chi(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1057:$\langle T(z_1)\,\mu(z_2) \rangle = \Theta(t_1-t_2)/(2\pi(z_1-z_2))$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:61:\langle T(z_1) \mu(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)},\\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:62:\langle W(z_1) \chi(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1063:$\langle T(z_1)\,\mu(z_2) \rangle = \Theta(t_1-t_2)/(2\pi(z_1-z_2))$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:139:\langle T(z_1) \mu(z_2) \rangle = \frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:168:&= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)} \left( T(z_2) \partial_2 \mu(z_2) + \frac{c}{24} \partial_2^3 \mu(z_2) \right).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:659:\langle T(z_1) \mu(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)},\\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:660:\langle W(z_1) \chi(z_2) \rangle &= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:125:\langle T(z_1) \mu(z_2) \rangle = \frac{\Theta(t_1 - t_2)}{2\pi(z_1 - z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:157:&= \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)} \left( T(z_2) \partial_2 \mu(z_2) + \frac{c}{24} \partial_2^3 \mu(z_2) \right).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1686:$K(z,t;\,z',t')=\Theta(t-t')/(2\pi(z-z'))$. The reflected
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1690:=\frac{\Theta(t-t')}{2\pi(z-z')}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1691:+\frac{\Theta(t+t')}{2\pi(z-\bar z')}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:99:\{\phi(z_1)\,{}_\lambda\,\psi(z_2)\} = \frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:481:G(z_{v_i}, z_{v_j}) = \frac{1}{2\pi(z_{v_i} - z_{v_j})}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:558:the propagator $K = \delta(t_1 - t_2) / (2\pi(z_1 - z_2))$ solves $(\partial_t + \bar{\partial}) K = \delta^{(3)}$. This exhibits the product decomposition: meromorphic in $z$ with a simple pole, distributional $\delta(t)$ in the topological direction, and translation-invariant.

thinking
**Searching for fixed strings**

I need to clarify a calculation involving `\frac{1}{2π}` and potentially search in volume 2 for the fixed string `\frac{1}{2\pi}`. It's crucial for capturing cases that don't involve `2\pi(z` or delta. I want to ensure accuracy in this process, so I'm focusing on the right string formats. Let’s explore these variations to catch all necessary instances. I'll keep this in mind as I proceed!
exec
/bin/zsh -lc "rg -n -F --glob '*.tex' '\\frac{1}{2\\pi}' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:54:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:36:\langle \phi(t_1, z_1) \psi(t_2, z_2) \rangle = \frac{1}{2\pi} \cdot \frac{\Theta(t_1 - t_2)}{z_1 - z_2}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:81:K(t-t',z-z') = \frac{1}{2\pi} \frac{\Theta(t-t')}{z-z'},
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:199:\frac{1}{2\pi}\, d\arg(e^{i\theta_i} - e^{i\theta_j})
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:211:where $\eta^K_{ij} = \frac{1}{2\pi}\, d\arg(t_i - t_j)$ is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/kontsevich_integral.tex:239:of $\frac{1}{2\pi}\,d\arg$ from $\Re(\eta_{ij})|_{S^1}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:509:K(z,t) \;=\; \frac{1}{2\pi}\,\frac{\Theta(t)}{z},
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:575:\frac{1}{2\pi}\,


thinking
**Evaluating patching options**

I'm considering a candidate list for what to patch and need to search for `\delta(t)/(2\pi(z-z'))`. I might try using apply_patch, though I'm uncertain if that can edit non-writable files. Maybe I can patch an external file without causing harm. If it fails, I can try a minimal patch on one file to see if it works. The user asked for a fix, so I'll choose one file to start with. I'll focus on a specific file path and see how it goes!
thinking
**Exploring limitations in commands**

I'm considering the sandbox and writable roots, and I think shell commands might be limited. It seems that apply_patch could also be restricted to the workspace. I should probably run a test to see how things work out. Before I make any edits, it’s definitely important to provide commentary for clarification. I want to ensure I'm taking the right approach and documenting it properly! Let’s see how the testing goes!
codex
I’ve reached the edit boundary. The only live AP120 defects are in Volume II, which the shell reports as non-writable from this session; I’m testing whether `apply_patch` can still reach that sibling repo. If it cannot, I’ll stop cleanly and report the exact blocked edits instead of pretending they were applied.

thinking
**Updating steps**

I’m considering whether to use request_user_input, but I’m not sure it's necessary since I’m not in plan mode. I think I might need to update my plan instead. I can enumerate what I’ve completed so far, but I have to address a sandbox block. Also, I should verify that my current repo is clean. It looks like updating is essential to keep everything on track!
Plan update
Enumeration is complete. Live AP120 defects are all in Volume II, but sibling-repo writes are blocked by the current writable-root policy; Volume I and the checked Volume III surfaces have no live AP120 edit to apply.
  ✓ Read constitutional sources relevant to AP120 and scope constraints
  ✓ Enumerate all cross-volume normalization candidates and classify true errors
  ✓ Patch only definite AP120 errors in assigned files
  ✓ Re-scan all volumes to verify no incorrect `1/(2\pi)` contour normalizations remain


thinking
**Considering file linking and edits**

I’m thinking about how to reference multiple lines in the same file. Maybe I could simply link to the first line and mention the others plainly or include multiple links to the same file. I don’t want to overdo it, so I could keep it simple with line text in backticks. The ideal method might be clickable file links like `[examples-complete.tex](...</Users/...:54>)` for reference. For edits, listing multiple replacements could work too.
thinking
**Structuring the output**

I’m thinking about creating my response with two clear sections: a **Result** paragraph and a list of **Blocked Fixes**. Since the task specifically asks for “each finding,” organizing the information in bullet points makes sense. I want to ensure everything is clear and concise to help the user easily understand my suggestions. Let’s get this organized and make it straightforward for them!
codex
**Result**
I audited all three volumes for AP120. Volume I and the checked Volume III surfaces have no live Cauchy-normalization fixes: their `1/(2\pi)` hits are real-angle `d\arg` kernels, scalar Green functions, asymptotics, or period integrals, not holomorphic contour normalizations. Every live AP120 defect is in Volume II.

No edits were applied because this session cannot write to sibling repos outside `/Users/raeez/chiral-bar-cobar`. I tested `apply_patch` on Volume II and it was rejected with: `writing outside of the project; rejected by user approval settings`.

**Blocked Fixes**
- PROBLEM at [examples-complete.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:54), [examples-complete-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex:36), [examples-complete-proved.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:36): HT free propagator uses `\frac{1}{2\pi}`. EXACT edit blocked: `\frac{1}{2\pi}` -> `\frac{1}{2\pi i}`.
- PROBLEM at [examples-complete.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:527), [examples-complete-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:66): non-abelian HT propagator uses `\frac{\delta^{ab}}{2\pi}`. EXACT edit blocked: `\frac{\delta^{ab}}{2\pi}` -> `\frac{\delta^{ab}}{2\pi i}`.
- PROBLEM at [examples-computing.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:81), [examples-computing.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex:99): kernel/bracket uses `2\pi` instead of `2\pi i`. EXACT edit blocked: `\frac{1}{2\pi}\frac{\Theta(t-t')}{z-z'}` -> `\frac{1}{2\pi i}\frac{\Theta(t-t')}{z-z'}` and `\frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}` -> `\frac{\Theta(t_1-t_2)}{2\pi i (z_1-z_2)}`.
- PROBLEM at [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:509), [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:555), [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:571), [relative_feynman_transform.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:575): mixed HT kernel and derived residue terms use `1/(2\pi)`. EXACT edit blocked: `\frac{1}{2\pi}` -> `\frac{1}{2\pi i}`, `\frac{\Theta(t-t')}{2\pi}` -> `\frac{\Theta(t-t')}{2\pi i}`, `\frac{\kappa}{2\pi}` -> `\frac{\kappa}{2\pi i}`.
- PROBLEM at [thqg_bv_construction_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:135), [thqg_bv_construction_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:140), [thqg_bv_construction_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:156), [thqg_bv_construction_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_construction_extensions.tex:769): retarded `\bar\partial` kernel and contour formula omit `i`. EXACT edit blocked: `\frac{\Theta(t_1-t_2)}{2\pi(z_1-z_2)}` -> `\frac{\Theta(t_1-t_2)}{2\pi i (z_1-z_2)}`, `1/(2\pi(z_1-z_2))` -> `1/(2\pi i (z_1-z_2))`, `\frac{dz}{2\pi(z-w)}` -> `\frac{dz}{2\pi i (z-w)}`.
- PROBLEM at [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:445), [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:660), [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:864), [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:866), [fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:870): all HT propagator formulas use `2\pi` instead of `2\pi i`. EXACT edit blocked: add `i` in each denominator, including `K(z,t)=\Theta(t)/(2\pi z)` -> `K(z,t)=\Theta(t)/(2\pi i z)`.
- PROBLEM at [fm-proofs.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:481): `G(z_{v_i}, z_{v_j}) = \frac{1}{2\pi(z_{v_i} - z_{v_j})}`. EXACT edit blocked: `\frac{1}{2\pi(z_{v_i} - z_{v_j})}` -> `\frac{1}{2\pi i (z_{v_i} - z_{v_j})}`.
- PROBLEM at [raviolo.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:558): `K = \delta(t_1 - t_2)/(2\pi(z_1 - z_2))`. EXACT edit blocked: `/(2\pi(z_1-z_2))` -> `/(2\pi i (z_1-z_2))`.
- PROBLEM at [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:139), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:168), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:659), [w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:660): HT propagators/contractions use `2\pi(z_1-z_2)`. EXACT edit blocked: add `i` in every denominator on those lines.
- PROBLEM at [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:129), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:158), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:757), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:758), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1057): same AP120 drift. EXACT edit blocked: add `i` to each `2\pi(z_1-z_2)` denominator.
- PROBLEM at [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:61), [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:62), [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1063): same AP120 drift. EXACT edit blocked: add `i` to each `2\pi(z_1-z_2)` denominator.
- PROBLEM at [w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:125), [w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:157): same AP120 drift. EXACT edit blocked: add `i` to each `2\pi(z_1-z_2)` denominator.
- PROBLEM at [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1686), [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1690), [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1691): direct and reflected HT propagators use `2\pi(z-z')` and `2\pi(z-\bar z')`. EXACT edit blocked: replace with `2\pi i (z-z')` and `2\pi i (z-\bar z')`.

If you want the fixes actually applied, rerun with `/Users/raeez/chiral-bar-cobar-vol2` added to the writable roots; I already have the exact patch surface isolated.
tokens used
108,506
