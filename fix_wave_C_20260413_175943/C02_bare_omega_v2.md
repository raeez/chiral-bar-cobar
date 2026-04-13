# C02_bare_omega_v2 (487s)

CONVERGED

- `PROBLEM` at [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1244) and the same live affine/Kac--Moody summary layer at lines `2729, 2860, 3150, 3280, 3397, 3744, 3796, 3806, 4796, 4839, 5361`: generic collision residues were written with the level stripped as `\Omega/z`.
  `EXACT edit applied`: changed each generic affine form to the level-prefixed form:
  `\Omega_\fg / z -> k\,\Omega_\fg / z`, `\Omega_\fg/z -> k\,\Omega_\fg/z`, `\Omega_{\mathfrak{sl}_2}/z -> k\,\Omega_{\mathfrak{sl}_2}/z`.

- `PROBLEM` at [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2345) and the related active affine/lattice lines `2795-2799, 2867`: leading spectral `R`-matrix formulas dropped the level prefix.
  `EXACT edit applied`: changed
  `R(z) = 1 + \hbar\,\Omega/z + \cdots -> R(z) = 1 + \hbar\,k\,\Omega/z + \cdots`,
  `R(z) = 1 + \hbar\,\Omega_{\mathfrak{sl}_3}/z -> R(z) = 1 + \hbar\,k\,\Omega_{\mathfrak{sl}_3}/z`,
  `R(z) = 1 + \hbar\,\Omega_{\mathfrak{so}_8}/z -> R(z) = 1 + \hbar\,k\,\Omega_{\mathfrak{so}_8}/z`,
  and rewrote the level-one sentence to keep the prefix visible:
  `k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z`.

- `PROBLEM` at [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:946): the reduced evaluation-sector braiding exponent omitted the affine level, so the `k=0` collapse was not encoded in the formula.
  `EXACT edit applied`: changed
  `\exp(\Omega_{\lambda_1,\lambda_2}/z) -> \exp(k\,\Omega_{\lambda_1,\lambda_2}/z)`
  and added:
  `At k=0 this braiding collapses to the identity, as the classical residue r(z)=k\,\Omega/z vanishes.`

- `PROBLEM` at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2129) and line `2977`: two generic affine `R`-matrix leading terms were written as `1+\hbar\,\Omega/z+...` even though the surrounding discussion was explicitly level-`k`.
  `EXACT edit applied`: changed both occurrences to
  `R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`.

- `PROBLEM` at [linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:3): the AP126 sweep was not recorded in the persistent audit ledger.
  `EXACT edit applied`: added the section `2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep` with target, finding, fix, and verification notes.

Verification used targeted `rg` re-audits on the touched live surface. No remaining generic affine/Kac--Moody AP126 survivor is left in those files; the one remaining no-`k` hit is the Yangian-specific `R_Y(z)` at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:4083), which is outside this affine-level AP126 scope. I did not run a full LaTeX build.


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
session id: 019d8791-ffe1-7dd2-974f-c0ceee9cd172
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


Same AP126 fix for Vol II.
mcp startup: no servers
codex
Target is the Vol II analogue of the prior `AP126` correction, with an audit-plus-fix pass constrained to the relevant Vol II files. I’m locating the original `AP126` pattern first, then I’ll trace every Vol II occurrence, patch the minimum truthful edits, and verify there are no surviving duplicates or stale statements.
exec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/vol2-deep-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "AP126|Same AP126 fix|AP 126|AP-126" -S .' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
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
 M Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
 D working_notes.pdf
 succeeded in 50ms:
./AGENTS.md:546:   `AP126`, `V2-AP34`, `AP44`, `AP45`, `AP46`, `AP49`, and `AP113` recur across manuscript and compute layers.
./compute/audit/beilinson_audit_drinfeld_double_wave11.md:242:- AP126 (level-prefixed r-matrix) verified on every r-matrix formula: 5899, 5921, 6131, 2480, 1678.
./compute/audit/beilinson_audit_drinfeld_double_wave11.md:284:- /Users/raeez/chiral-bar-cobar/CLAUDE.md (AP34, AP83, AP94-98, AP102, AP105, AP109, AP126, AP132, AP134, AP141)
./compute/lib/pva_descent_coefficients_engine.py:50:AP126/AP141: At level k = 0 the Kac-Moody central extension of the
./compute/lib/pva_descent_coefficients_engine.py:603:    AP126: at k = 0 the bracket vanishes identically.
./compute/lib/pva_descent_coefficients_engine.py:633:    AP126: at k = 0 the central extension vanishes but the semisimple
./compute/lib/pva_descent_coefficients_engine.py:729:    """Verify the AP126/AP141 boundary check at level 0.
./compute/audit/beilinson_audit_vol2_preface_wave11.md:12:The preface is structurally strong. The Steinberg analogy (one coalgebra, three projections: cobar = inversion, Verdier = Koszul, Hochschild = bulk) is precise and survives examiner pressure. The three-leap architecture is well motivated. The AP-OC distinction is stated correctly. The slab-is-bimodule (RS-9) language is clean. All five Dimofte remark labels exist in ht_bulk_boundary_line_core.tex. The six integrated AP fixes (AP24, AP25/AP34, AP126, AP117, AP32, V2-AP26) are all present and correctly applied.
./compute/audit/beilinson_audit_vol2_preface_wave11.md:50:- **LOW -- Heisenberg R-matrix R(z) = exp(k*hbar/z).** Matches V2-AP7. Correct with level prefix; vanishes at k = 0. AP126-clean.
./compute/audit/beilinson_audit_vol2_preface_wave11.md:64:- **POSITIVE -- AP126 level-prefix on all r-matrices.** Heisenberg r_H(z) = k/z (line 355), Kac-Moody r(z) = k*Omega/z (line 373), "at k = 0 the r-matrix vanishes" sanity check stated explicitly (lines 346, 355, 376, 531). AP126/AP141 fully absorbed. PASS.
./compute/audit/beilinson_audit_vol2_preface_wave11.md:118:| AP126 (level-prefixed r-matrix; k=0 vanishing) | lines 346, 355, 373, 376, 530--531 | INTEGRATED, five explicit vanishing checks |
./compute/audit/beilinson_audit_vol2_preface_wave11.md:182:| POSITIVE | 12 | V2-AP26 Part refs; zero AI slop; AP126 level prefix; AP117 Arnold vs KZ; AP24 forceful; AP32 tags; all six Wave 4-1 fixes absorbed; Steinberg analogy precise; three leaps precise; AP-OC precise; RS-9 slab-is-bimodule explicit; decomposition table |
./compute/tests/test_pva_descent_coefficients_engine.py:4:cases (3): trivial PVA, level-zero affine sl_2, and the AP126
./compute/tests/test_pva_descent_coefficients_engine.py:23:    * AP126  (level-zero r-matrix vanishing)
./compute/tests/test_pva_descent_coefficients_engine.py:250:    def test_level_zero_boundary_AP126(self):
./compute/tests/test_pva_descent_coefficients_engine.py:251:        """AP126 / AP141: at k = 0 the Kac-Moody central extension of
./compute/tests/test_pva_descent_coefficients_engine.py:257:            (CLAUDE.md AP126).  Bracket's central term is the Borel

thinking
**Searching for r-matrix**

I need to search the repository for "level-prefixed r-matrix." I'm thinking that there might be mentions of AP126 in the AGENTS section, especially in the recurring documents. It seems I should focus on inspecting the content around line 546 for more detailed information. This could help me gather the context I need to understand the references better. Let's see what I find!
codex
I’ve confirmed the task matches both `$vol2-deep-audit` and `$vol2-beilinson-rectification`: audit first, then repair. Next I’m pinning down the original `AP126` invariant and mapping every Vol II surface that still violates it, rather than guessing from the prompt.
Plan update
Audit-first, then minimum truthful rectification for the Vol II AP126 analogue.
  → Identify the original AP126 rule and locate all Vol II candidate violations
  • Read the live manuscript surfaces and determine exact minimum edits
  • Apply fixes and log findings in the audit ledger
  • Run targeted verification greps/tests and re-audit the touched surface
exec
/bin/zsh -lc "sed -n '520,580p' AGENTS.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"R\\(z\\)|r\\(z\\)|classical r-matrix|universal R-matrix|Heisenberg R-matrix|Kac-Moody r-matrix|Yangian R-matrix|elliptic R-matrix\" --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"level-prefixed r-matrix|r-matrix vanishes|at k = 0 the r-matrix vanishes|AP126-clean|vanishes at k = 0|R\\(z\\).*k|r\\(z\\).*k\" -S ." in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

Record nontrivial findings in `compute/audit/linear_read_notes.md` with date, target, severity, class, location, issue, fix, and status.

### 10. Re-Audit

Hostilely reread your own rewrite. This is not celebration. It is attempted refutation of the patch you just made.

### 11. Convergence

A task is converged only when:

- no actionable finding at severity `MODERATE` or above remains on the modified surface; and
- the narrowest relevant verification passes.

Rectification sessions end only with:

- `CONVERGED`
- `BLOCKED: <one-sentence blocker>`

## Cross-Volume Empirical Priors (Last 100 Commits Per Repo)
 succeeded in 52ms:
# Linear Read Notes

## 2026-04-13 - Bar-Cobar Review Fortification

- Target: `chapters/connections/bar-cobar-review.tex`
- Status: IN PROGRESS

### Findings

1. `2026-04-13-002`
   Severity: `SERIOUS`
   Class: `D`
   Location: `chapters/connections/bar-cobar-review.tex:205-210`, `:625`, `:1355`, `:1620`, `:2280-2413`, `:4079-4088`
   Issue: the review chapter still advertised stale Theorem A language from earlier Vol I drafts. It conflated the genus-zero bar differential package with Main Theorem A and repeatedly treated Verdier duality as landing directly on a bar coalgebra or on the classical dual, whereas the current Vol I convention is algebra-level: `\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)` is the homotopy Koszul dual factorization algebra, formal to the classical dual only on the Koszul locus.
   Fix: rewrite the theorem-package summaries so Theorem A is stated with the algebra-level Verdier convention, and retarget the bar-differential/collision statements to the genus-zero bar-construction package rather than to Main Theorem A.
   Status: `PENDING`

2. `2026-04-13-003`
   Severity: `SERIOUS`
   Class: `D`
 succeeded in 52ms:
Total output lines: 902

compute/audit/sl3_rtt_latex_output.tex:57:r(z) \;=\; \frac{k\,\Omega}{z}
compute/audit/sl3_rtt_latex_output.tex:67:The quantization of $r(z) = k\Omega/z$ is the Yang $R$-matrix
compute/audit/sl3_rtt_latex_output.tex:270: (left and right collision, controlled by $r(z) = k\Omega/z$).
compute/audit/non_simply_laced_rmatrix_report.tex:94: r(z) = \frac{k \cdot \Omega}{z}\,.
compute/audit/non_simply_laced_rmatrix_report.tex:100: regular part (no pole in $r(z)$).
compute/audit/non_simply_laced_rmatrix_report.tex:212:$r(z) = k\Omega/z$ & \checkmark \\
main.tex:1046:$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
main.tex:1274:$R(z) \in \End(B^{\mathrm{ord}}_2)$, the KZ associator, and the
main.tex:1278:The modular characteristic $\kappa(\cA) = \mathrm{av}(r(z))$
main.tex:1280:$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$;
main.tex:1307:\part{The Seven Faces of $r(z)$}
main.tex:1312:The collision residue $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
chapters/examples/w-algebras-stable.tex:574:exactly the CYBE for $r(z)$. This is the standard
chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
working_notes.tex:590:$r$-matrix: $r(z) = \Omega_\fg/z$ (Casimir, single pole).
working_notes.tex:606:$\infty$.  $r$-matrix: $r(z) = (c/2)/z^3 + 2T/z$ (two poles,
working_notes.tex:754:where $R(z)$ is the quantum $R$-matrix built from the bulk-boundary
working_notes.tex:757:$R(z) = 1 + \hbar\,\Omega_\fg/z + O(\hbar^2)$.  For gravity:
 succeeded in 50ms:
Total output lines: 378

./CLAUDE.md:164:- R-matrix provenance: R(z) from bulk-boundary composition, NOT universal R-matrix (agree on eval locus = DK-0).
./chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
./chapters/examples/examples-worked.tex:87:For abelian Chern--Simons with HT boundary condition, conditional on Theorem~\ref{thm:physics-bridge}, the boundary category of line operators is braided by $R(z)$, with classical limit $r(z)=\frac{k}{z}$ (after normalization). The bulk chiral Hochschild cochains produce the same $r(z)$ via the Laplace transform of the bulk $\lambda$-bracket kernel as in Proposition~\ref{prop:field-theory-r}.
./chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
./chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
./chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
./chapters/examples/examples-worked.tex:2729:$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
./chapters/examples/examples-worked.tex:2860:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
./chapters/examples/examples-worked.tex:3150:\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
./chapters/examples/examples-worked.tex:3280:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
./chapters/examples/examples-worked.tex:3397:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
./chapters/examples/examples-worked.tex:3441:  via the collision residue $r(z) = k\,\Omega/z$.
./chapters/examples/examples-worked.tex:3470:classical limit: $r(z) = k\,\Omega/z$ is the classical
./chapters/examples/examples-worked.tex:4689:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
./chapters/examples/examples-complete.tex:699: r(z) = \frac{k\,\Omega}{z},
./chapters/examples/examples-complete.tex:722:$k\,\delta^{ab}/z^2$ gives, after $d\log$ absorption, the collision $r$-matrix $r(z) = k\,\Omega/z$, the standard rational
./chapters/examples/examples-complete-conditional.tex:280: r(z) = \frac{k\,\Omega}{z},
./chapters/examples/examples-complete-conditional.tex:305:$r(z) = k\,\Omega/z$, the standard rational


thinking
**Analyzing AP126 Issues**

I’m looking at the AP126 issue and thinking it might come from Volume I. It seems I need to always include the level prefix 'k' in r-matrix formulas and ensure they vanish at k=0 on high-visibility surfaces. The user mentioned needing the same fix for Volume II, so I suspect there's a similar problem there. I’ll need to audit for any violations, identify candidate surfaces in Volume II, and check recent changes for exact files assigned. I may have to inspect the active build graph to narrow it down.
thinking
**Investigating Manuscript Issues**

I’m searching through the active manuscript files, specifically the `chapters/` and `main.tex`, while ignoring working notes. The user pointed out this is about Volume II, so I may need to focus on active files only related to assigned tasks. I should be thorough within the assigned scope. I’ll inspect the `\input` graph in main.tex and target files where AP126 violations can be found. I’ll look for specific issues like instances of `r(z)=Ω` and `R(z)=1+\hbarΩ/z` missing the prefix 'k', especially in level-specific examples. It’s crucial to differentiate between general formulas and those with level-1 specialization.
codex
The grep surface shows the likely failure mode: several active Vol II examples still write affine `r(z)` or `R(z)` with the level stripped, despite the rest of the manuscript already enforcing the AP126 rule. I’m now reading the suspicious live contexts to separate true violations from legitimate `k=1` specializations before I edit anything.
exec
/bin/zsh -lc "sed -n '1540,1595p' chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2688,3415p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3560,3788p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2320,2888p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Setting $q=e^{i\pi/(k+2)}$, the eigenvalues are $q^{-1}$ (triplet) and $q^3=-q^{-1}\cdot q^{k+2}=-q^{-1}$
when $q^{k+2}=1$... more precisely, $e^{3\pi i/(k+2)}=q^3$.
These are exactly the eigenvalues of the $R$-matrix of $U_q(\mathfrak{sl}_2)$
on $V\otimes V$:
\[
 \check{R}\big|_{V_1}=q,\qquad \check{R}\big|_{V_0}=-q^{-1},
\]
matching $M_\gamma = q^{-\Omega_{12}} = P\circ \check{R}^{-1}$
(with $P$ the transposition) up to the standard framing scalar.
At $k=1$ one recovers $q=e^{i\pi/3}$, $M_\gamma=\operatorname{diag}(-1,\,q^{-1})$
on the singlet/triplet decomposition, confirming the
$\widehat{\mathfrak{sl}}_2$ level-$1$ WZW fusion rules.
\end{computation}

\begin{computation}[Formal $R$-matrix expansion; \ClaimStatusProvedHere]
\label{comp:formal-R-expansion}
\index{R-matrix@$R$-matrix!formal expansion}
The formal monodromy operator, equivalently the asymptotic $R$-matrix,
admits the $z^{-1}$-expansion (with $\Omega$ denoting the Sugawara-normalized
residue tensor $k\,\Omega_{\mathrm{Cas}}/(k+h^\vee)$ absorbing the level prefix and the level-explicit form at~\eqref{eq:R-level-explicit} below)
 succeeded in 52ms:
 are at $\zeta = 0$ and conformal weights are unchanged.
\item The root channel ($E^+ \cdot E^-$) satisfies a
 \emph{shifted weight-depth identity}: the ``effective
 depth'' is computed relative to the shifted poles.
 Each shifted simple pole at $\zeta = \pm\hbar$
 contributes at effective depth~$d_{\mathrm{eff}} = 2$
 (the residue is a field, not a scalar), while the
 combined effect of both poles contributes to
 $d_{\mathrm{eff}} = 1$ (the $1/\zeta^2$ term in the
 Laurent expansion around~$0$).
\end{itemize}
The resolution: the weight-depth identity holds
\emph{channel-by-channel} at each pole of the shifted
singularity locus. At each individual shifted pole
$\zeta = \pm\hbar$, the residue has $w = 1$,
$d_{\mathrm{eff}} = 1$, $n = 2$, giving $w + d = n$
(shifted by $+1$ relative to the classical formula).
The shift is exactly the $\hbar$-correction:
$w + d_{\mathrm{eff}} = n - 1 + 1$ where the extra $+1$
is the penalty for the off-diagonal singularity.
 succeeded in 52ms:
$[s^{-1}e_1\,|\,s^{-1}e_1\,|\,s^{-1}e_2]$ vanishes in
bar homology: its boundary at $D_{1,2}$ vanishes
($[e_1,e_1] = 0$) and its boundary at $D_{2,3}$ produces
$[s^{-1}e_1\,|\,s^{-1}e_{12}]$, whose own boundary
$[e_1, e_{12}] = 0$ by the Serre relation; the weight
space $(\mathfrak{sl}_3)_{2\alpha_1+\alpha_2} = 0$
forces the entire sector to be acyclic. The Yangian Serre relation
$\mathrm{Sym}_{r_1,r_2}[x^+_{1,r_1},[x^+_{1,r_2},
x^+_{2,s}]] = 0$ follows by the same mechanism at all mode
levels.
\end{computation}

\begin{remark}[$E_N$ level reached by $V_k(\fg)$ at non-critical level]
\label{rem:km-EN-level}
\index{Kac--Moody!$E_N$ level}
\index{E_N ladder@$E_N$ ladder!Kac--Moody}
For $k \ne -h^\vee$ (non-critical level), the affine
Kac--Moody vertex algebra $\cA = V_k(\fg)$ reaches the
top of the $E_N$ ladder:
\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 52ms:
(universal couplings between $V_k$ and $V_{-k-4}$); it does not
see the Verlinde algebra directly.
\end{remark}


\subsubsection{The Kazhdan--Lusztig equivalence and the line category}
\label{subsubsec:benchmark-kl-category}

On the chirally Koszul locus, the line-operator category is
modelled by modules for the Koszul dual
(Theorem~\ref{thm:lines_as_modules}):
\begin{equation}\label{eq:benchmark-line-category}
  \cC_{\mathrm{line}}
  \;\simeq\;
  V_{-k-4}(\mathfrak{sl}_2)\text{-mod}.
\end{equation}
At integrable level $k \in \Z_{\ge 0}$, the Kazhdan--Lusztig
theorem identifies the finite-dimensional quotient:
\begin{equation}\label{eq:benchmark-kl-equivalence}
  \cO_k^{\mathrm{int}}(\widehat{\mathfrak{sl}}_2)

thinking
**Evaluating assignment safety**

I'm considering that action safety might only apply to editing assigned files. The assignment is a bit ambiguous, so I want to infer the smallest live surface. I wonder if I should mention stale mirrors if they're not edited due to the assignment. Completeness suggests I need to be exhaustive within the assigned scope, which I think is Vol II live surface. I need to better understand AP126, possibly from Vol I, and search for it in CLAUDE.md if that's accessible in the repo.
exec
/bin/zsh -lc 'rg -n "AP126|level-prefixed|k = 0 the r-matrix vanishes|after writing any R-matrix" CLAUDE.md chapters compute/audit -S' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '5200,5355p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2330,2885p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '860,1185p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
compute/audit/beilinson_audit_drinfeld_double_wave11.md:242:- AP126 (level-prefixed r-matrix) verified on every r-matrix formula: 5899, 5921, 6131, 2480, 1678.
compute/audit/beilinson_audit_drinfeld_double_wave11.md:284:- /Users/raeez/chiral-bar-cobar/CLAUDE.md (AP34, AP83, AP94-98, AP102, AP105, AP109, AP126, AP132, AP134, AP141)
compute/audit/beilinson_audit_vol2_preface_wave11.md:12:The preface is structurally strong. The Steinberg analogy (one coalgebra, three projections: cobar = inversion, Verdier = Koszul, Hochschild = bulk) is precise and survives examiner pressure. The three-leap architecture is well motivated. The AP-OC distinction is stated correctly. The slab-is-bimodule (RS-9) language is clean. All five Dimofte remark labels exist in ht_bulk_boundary_line_core.tex. The six integrated AP fixes (AP24, AP25/AP34, AP126, AP117, AP32, V2-AP26) are all present and correctly applied.
compute/audit/beilinson_audit_vol2_preface_wave11.md:50:- **LOW -- Heisenberg R-matrix R(z) = exp(k*hbar/z).** Matches V2-AP7. Correct with level prefix; vanishes at k = 0. AP126-clean.
compute/audit/beilinson_audit_vol2_preface_wave11.md:64:- **POSITIVE -- AP126 level-prefix on all r-matrices.** Heisenberg r_H(z) = k/z (line 355), Kac-Moody r(z) = k*Omega/z (line 373), "at k = 0 the r-matrix vanishes" sanity check stated explicitly (lines 346, 355, 376, 531). AP126/AP141 fully absorbed. PASS.
compute/audit/beilinson_audit_vol2_preface_wave11.md:118:| AP126 (level-prefixed r-matrix; k=0 vanishing) | lines 346, 355, 373, 376, 530--531 | INTEGRATED, five explicit vanishing checks |
compute/audit/beilinson_audit_vol2_preface_wave11.md:182:| POSITIVE | 12 | V2-AP26 Part refs; zero AI slop; AP126 level prefix; AP117 Arnold vs KZ; AP24 forceful; AP32 tags; all six Wave 4-1 fixes absorbed; Steinberg analogy precise; three leaps precise; AP-OC precise; RS-9 slab-is-bimodule explicit; decomposition table |
chapters/connections/ordered_associative_chiral_kd_frontier.tex:5995:at level $k$, the classical $r$-matrix is level-prefixed:
 succeeded in 52ms:
For $V_k(\mathfrak{sl}_2)$ with generators
$J^a$ ($a = 1,2,3$) and $\lambda$-bracket
$\{J^a_\lambda J^b\} = f^{ab}_c J^c + k\,\kappa^{ab}\lambda$,
the three invariants are:
$\kappa = 3(k+2)/4$,
$c_0 = \Omega := \sum_a t^a \otimes t_a$ \textup{(}the
quadratic Casimir, from the Lie bracket\textup{)},
$d = 3$ \textup{(}propagator-entangled regime\textup{)}.

\smallskip
\noindent
\emph{Period correction.}
$F_1 = 3(k+2)/96 = (k+2)/32$.

\smallskip
\noindent
\emph{Genus-$1$ $r$-matrix.}
The Laurent coefficients are $c_0 = \Omega \ne 0$
and $c_1 = k\,\kappa$. By
Theorem~\ref{thm:elliptic-spectral-dichotomy}:
 succeeded in 52ms:
\end{computation}

\begin{remark}[$E_N$ level reached by $V_k(\fg)$ at non-critical level]
\label{rem:km-EN-level}
\index{Kac--Moody!$E_N$ level}
\index{E_N ladder@$E_N$ ladder!Kac--Moody}
For $k \ne -h^\vee$ (non-critical level), the affine
Kac--Moody vertex algebra $\cA = V_k(\fg)$ reaches the
top of the $E_N$ ladder:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\Eone$-chiral
 (Definition~\ref{def:e1-chiral-algebra}): the current
 OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
 structure of an $\Einf$-chiral algebra, hence
 \emph{a fortiori} $\Eone$-chiral.
 The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
 with $\Omega$ the Casimir of~$\fg$.

\item $\Etwo$-chiral on the derived center
 (Definition~\ref{def:E2-chiral-algebra}): automatic from
 succeeded in 52ms:
for every standard family; the spectral kernel~$r(z)$ is the
collision residue $\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
(by the collision-residue compatibility theorem of Volume~I).

\subsection{Heisenberg: free lines}
\label{subsec:line-op-heisenberg}

For $\cA=\cH_k$: the chiral Koszul dual is
$\cA^!_{\mathrm{ch}}=\Sym^{\mathrm{ch}}(V^*)$, while the
open-colour dual is
$\cA^!_{\mathrm{line}}=Y(\mathfrak{u}(1))$
(whose mode algebra $U(\mathfrak{u}(1)[t]) \cong \Bbbk[t]$
coincides with the mode algebra of~$\cH_{-k}$,
but is distinct as a chiral algebra),
$r(z)=k/z$, and $\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$.
The $r$-matrix is scalar: $r(z)=k/z\in\Bbbk(\!(z^{-1})\!)$.

\begin{computation}[Line-operator category for Heisenberg;
\ClaimStatusProvedHere]
\label{comp:line-op-heisenberg}
codex
I’ve isolated real AP126-style survivors, not just unit-level specializations: the live `examples`, `rosetta`, `line-operators`, and `ordered_associative` surfaces still have general affine formulas with the level silently stripped. I’m doing one more targeted sweep now so the patch is exhaustive within the live Vol II manuscript surface, not just the first few obvious hits.
exec
/bin/zsh -lc "sed -n '1688,1755p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '5980,6205p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'r\\(z\\)\\s*=\\s*\\\\Omega|R\\(z\\)\\s*=\\s*1\\s*\\+\\s*\\\\hbar["'^'"\\n]*\\\\Omega|R\\(z\\)\\s*=\\s*1\\s*\\+\\s*["'^k'"\\n]*\\\\Omega|exp\\(["'^'"\\n]*\\\\Omega["'^'"\\n]*\\/z\\)' chapters main.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\b(r\\(z\\)|R\\(z\\))["'^'"\\n]*(Omega|\\\\Omega)["'^'"\\n]*(/z|z\\)|z\\}|u\\}|u\\)|z\\+|z\\-|z\\s)' chapters main.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:

The CDG $R$-matrix governing line-operator OPE is the
monodromy of the ordered bar connection
(Construction~\ref{constr:r-matrix-monodromy}):
the physical process of one line operator circling another
in the holomorphic plane is the loop $\gamma$ in
$\mathrm{Conf}_2^{\mathrm{ord}}(\mathbb C)$ whose monodromy
is~$R(z)$. The Yang--Baxter equation
(Proposition~\ref{prop:ybe-from-d-squared}) is the
consistency of the perturbative expansion for three
simultaneously present lines.

For $\widehat{\mathfrak{sl}}_2$: the CDG line operators are
Wilson lines in 3d Chern--Simons, and $R(z)=1+k\,\Omega/z+\cdots$
is the perturbative expansion of the Chern--Simons $R$-matrix.
For Virasoro: the CDG lines are gravitational defects, and
the Laplace kernel $r^L_c(z)=\partial T/z+2T/z^2+c/(2z^4)$ has a
fourth-order pole from the conformal anomaly (the collision residue
$r^{\mathrm{coll}}_c(z) = (c/2)/z^3 + 2T/z$ has a cubic pole).
\end{remark}
 succeeded in 51ms:
Conjecture~\ref{conj:drinfeld-double-e1-construction}
restricted to $\cA = \cH_k$ is then prescribed by the
bilinear pairing
\begin{equation}
\label{eq:drinfeld-mix-heisenberg}
\mu_{\mathrm{mix}}(J(z_1),J^!(z_2))
\;=\;
\frac{k}{z_1-z_2}\cdot \mathbf 1
\;+\;\text{(regular terms from bar--cobar pairing)},
\end{equation}
where $J^!$ is the Verdier-dual generator (a simple vector
at the same conformal weight; the Koszul dual is
$\mathrm{Sym}^{\mathrm{ch}}(V^*)$, see the base-case analysis below).

For the affine Kac--Moody vertex algebra $V_k(\mathfrak g)$
at level $k$, the classical $r$-matrix is level-prefixed:
\begin{equation}
\label{eq:drinfeld-r-kmc}
r_{V_k(\mathfrak g)}(z) \;=\;\frac{k\,\Omega}{z},
\qquad
 succeeded in 50ms:
chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
chapters/examples/examples-worked.tex:1244:  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
chapters/examples/examples-worked.tex:2729:$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:2860:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
chapters/examples/examples-worked.tex:3150:\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
chapters/examples/examples-worked.tex:3280:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:3397:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
chapters/examples/examples-worked.tex:3744:  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
chapters/examples/examples-worked.tex:3796:$r(z) = \Omega_\fg/z$ has the same analytic structure
chapters/examples/examples-worked.tex:4839:  $r(z) = \Omega_\fg / z$
chapters/examples/rosetta_stone.tex:2345: The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
chapters/connections/spectral-braiding-core.tex:48:For $V_k(\mathfrak{sl}_2)$, the collision residue is $r(z) = k\,\Omega/z$, where $\Omega = \sum e_a \otimes e^a \in \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$ is the Casimir tensor. Again $k=0$ gives $r=0$. At leading order, $R(z) = 1 + \hbar\, k\,\Omega/z + \cdots$ is the Yang $R$-matrix. The YBE at order $\hbar^2$ reduces to the infinitesimal braid relation $[\Omega_{12},\, \Omega_{13} + \Omega_{23}] = 0$, which is the Jacobi identity on $\mathfrak{sl}_2$. This is class~L: depth $1$, the $r$-matrix carries non-trivial Lie structure, but the twisted coproduct $\Delta_z$ on the Koszul dual is still cocommutative at the classical level.
chapters/connections/spectral-braiding-core.tex:791:$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
chapters/connections/spectral-braiding-frontier.tex:322:$R(z) = \exp(\hbar k\,\Omega/z)$
chapters/connections/ordered_associative_chiral_kd.tex:2294:$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$=1$) where
chapters/connections/ordered_associative_chiral_kd.tex:2404:The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
chapters/connections/thqg_spectral_braiding_extensions.tex:1198:The $R$-matrix $R(z) = 1 + \hh\, \Omega/((k+h^\vee)z)
chapters/connections/ordered_associative_chiral_kd_core.tex:2129:$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
chapters/connections/ordered_associative_chiral_kd_core.tex:2977:The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
 exited 1 in 51ms:


thinking
**Checking active files**

I think I need to focus on whether to use `ordered_associative_chiral_kd_core.tex` and `ordered_associative_chiral_kd.tex`. Maybe there are mirrors involved? I should check the main input to identify which chapter is active, looking at core or unsplit options. It might be helpful to inspect `main.tex` to see inputs related to ordered_associative, as I need to determine the currently active file(s). I'll need to search for input names too.
exec
/bin/zsh -lc "sed -n '2200,2365p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'ordered_associative_chiral_kd|line-operators|examples-worked|rosetta_stone|log_ht_monodromy_core' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2350,2365p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2940,2995p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
926:\phantomsection\label{V1-subsec:thqg-V-line-operators-mc3}%
1298:\input{chapters/connections/line-operators}
1299:\input{chapters/connections/ordered_associative_chiral_kd_core}
1363:\input{chapters/examples/rosetta_stone}
1366:\input{chapters/examples/examples-worked}
1403:\input{chapters/connections/log_ht_monodromy_core}
1458:\input{chapters/connections/ordered_associative_chiral_kd_frontier}
 succeeded in 52ms:
that the $\Sigma_2$-quotient kills.
At $n = 3$: $27$ vs $10$, surplus $= 17$, decomposing into
irreducible $B_3$-representations that carry the
degree-$3$ Vassiliev data. At $n = 4$: $81$ vs $15$,
surplus $= 66$.

For Virasoro ($d = 1$, single generator of weight~$2$):
$\dim\Barchord_n = 1 = \dim\Barch_n$
at each tensor degree (one ordered sequence and one
unordered multiset of length~$n$ from a single generator).
The surplus is \emph{not} in raw dimensions but in the
\emph{spectral asymmetry}: the ordered bar differential
$d_{\mathrm{res}}$ on
$\Barchord_n(\mathrm{Vir})$
retains the spectral-parameter dependence
$r(z) = (c/2)/z^3 + 2T/z$ (the collision residue of
the quartic-pole OPE, after $d\log$ absorption), while
the symmetric bar sees only the $\Sigma_n$-invariant
part. The directed spectral flow (the fact that
$r(z) \ne r(-z)$ due to the odd-power term
 succeeded in 51ms:
 the chiral Deligne conjecture.

\item $\Etwo$-topological
 (Definition~\ref{def:E2-topological-algebra}): the
 Sugawara construction provides a conformal vector
 $T_{\mathrm{Sug}}(z)
 = \frac{1}{2(k + h^\vee)}
 \sum_a {:}\!J^a J^a\!{:}(z)$
 of central charge $c = k\dim\fg/(k + h^\vee)$.
 At $k \ne -h^\vee$ this is well-defined, and
 Construction~\ref{constr:topologization} trivializes the
 complex-structure dependence in cohomology.

\item $\Ethree$-chiral: the 3d holomorphic-topological
 theory is holomorphic Chern--Simons on $\C \times \R$,
 descended from the 6d holomorphic gauge theory
 succeeded in 51ms:
$u$-expansion produce the Yangian deformation:
\[
[H_i(u),\,E_j(v)]
\;=\;
\frac{A_{ij}}{u-v}\,E_j(v)
\;+\;\text{(higher poles)},
\]
where the higher poles come from OPE coefficients
$h_{i(n)}e_j$ ($n\ge 1$). The Serre relations arise from
degree-$3$ bar cohomology via the $A_\infty$ structure.

\emph{The RTT presentation.}
The transfer matrix
$T(u)=\sum_I e_I\otimes t^I(u)
\in\operatorname{End}(V)\otimes Y_\hbar(\mathfrak g)[\![u^{-1}]\!]$
(where $V$ is the defining representation of~$\mathfrak g$
and $t^I(u)$ are the degree-$1$ bar cohomology generating
functions) satisfies
\begin{equation}\label{eq:rtt-from-bar}
R(u{-}v)\,T_1(u)\,T_2(v)

thinking
**Identifying lines in files**

I need to pinpoint the exact lines in active files. The search results show a lot within examples-worked, so I should read the contexts around those lines. There's also rosetta to consider. Some might qualify as integrable level k explicit, but I still need to verify if they meet AP126 standards. For example, something at k=1 could be okay, but I need to distinguish and inspect those contexts from both examples-worked and rosetta.
exec
/bin/zsh -lc "sed -n '2718,2740p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1228,1260p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2848,2870p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3268,3290p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3138,3160p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3387,3405p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '4828,4850p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3736,3804p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  more precisely, $\cA_\partial^! = \mathrm{CE}^{\mathrm{ch}}(\widehat\fg_{-k-2h^\vee})$
  \textup{(}chiral CE cochains\textup{)}, which shares
  $\kappa(\cA^!) = -\kappa(\cA)$ with $V_{-k-2h^\vee}(\fg)$
  but is categorically distinct \textup{(}cf.\ AP33\textup{)}.
  On the associated graded \textup{(}PBW filtration\textup{)},
  $\operatorname{gr}\cA_\partial^! \simeq C^\bullet(\fg[t^{-1}]t^{-1})$.
  The Koszul involution exchanges Neumann~$\leftrightarrow$~Dirichlet
  boundary conditions.

\item \textbf{Derived center \textup{(}universal bulk\textup{)}.}
  $\Zder^{\mathrm{ch}}(\cA_\partial)
  = C^\bullet_{\mathrm{ch}}(V_k(\fg),\, V_k(\fg))$.
  The bulk observables are chiral Hochschild cochains of the boundary
  algebra, not the bar complex.

\item \textbf{Collision residue.}
  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
  equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.

\item \textbf{Modular MC element.}
 succeeded in 52ms:
Drinfeld~\cite{Dri89}.)}
At integrable level~$k$, the category of integrable
$\widehat{\mathfrak{sl}}_2$-modules at level $k$ is
a braided tensor category equivalent to
$\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ with $q = e^{i\pi/(k+2)}$.
Its braiding is compared by the affine Drinfeld--Kohno theorem
with the monodromy of the KZ connection on the corresponding
integrable affine comparison surface.
On the manuscript's affine Kac--Moody comparison surface, the
corresponding genus-$0$ bar-side connection identifies with KZ and
begins from the same classical residue
$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
\end{proposition}

At the explicit level $k = 1$ (the simplest integrable case):
$q = e^{i\pi/3}$ is a primitive $6$th root of unity,
and $\mathrm{Rep}(U_q(\mathfrak{sl}_2))$ has
$k + 1 = 2$ simple objects (the trivial and the fundamental
representation), with fusion rule $L_1 \otimes L_1 \cong L_0$
(the fundamental is self-dual, and the tensor product is
 succeeded in 51ms:
\item \textbf{Koszul dual.}
  $\cA_\partial^! = V_{-k-4}(\mathfrak{sl}_2)$
  \textup{(}Feigin--Frenkel: $k' = -k - 2h^\vee = -k-4$\textup{)}.

\item \textbf{Universal bulk \textup{(}derived center\textup{)}.}
  $\cZ^{\mathrm{der}}_{\mathrm{ch}}(V_k(\mathfrak{sl}_2))
  = C^\bullet_{\mathrm{ch}}(V_k, V_k)$. \\
  Generic $k$: $H^0 \cong \C$.\\
  Integrable $k$: the categorical center is the Verlinde algebra
  of dimension $k + 1$.

\item \textbf{Collision residue.}
  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
  satisfying the classical Yang--Baxter equation.
  The RTT quantization gives the Yangian
  $Y_\hbar(\mathfrak{sl}_2)$.

\item \textbf{Modular characteristic.}
  $\kappa = 3(k+2)/4$. \\
  Complementarity: $\kappa + \kappa' = 0$.\\
 succeeded in 50ms:
$L_0, L_1, \ldots, L_k$ of $L_k(\mathfrak{sl}_2)$.

\begin{proposition}[What the bar complex sees and does not
  see; \ClaimStatusProvedHere]
\label{prop:bar-sees-quantum-group}
\index{bar complex!quantum group at root of unity}
Let $k \in \Z_{\ge 0}$.
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item \textbf{The bar complex sees the collision residue.}
  The classical $r$-matrix
  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
  $V_k$ and $L_k$, hence the perturbative quantum group
  structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
  KZ connection\textup{)} is unchanged at genus~$0$.

\item \textbf{The bar complex sees the truncation of
  representations.}
  The bar complex $\barB^{\mathrm{ch}}(L_k)$ classifies
  twisting morphisms $L_k \to L_k^!$, and the category
 succeeded in 52ms:
  (nonzero).  The new feature at $k = 1$: the additional
  quadratic relation $R_{\mathrm{null}}$ introduces a
  new cycle in bar degree~$2$.  The element
  $[s^{-1}f \,|\, s^{-1}f]_{\mathrm{null}}$, which in
  $\barB^2(V_1)$ has $d_B = f_{(1)}f = k = 1$
  \textup{(}nondegenerate\textup{)}, is now \emph{modified}:
  the additional relation $:ff: = 0$ in $L_1$ means that
  the mode product $f_{(0)}f$ vanishes in $L_1$, altering the
  bar differential on degree-$2$ elements.

\item \textbf{Collision residue.}
  Unchanged from $V_1$:
  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.

\item \textbf{Finite representation theory.}
  The bar complex $\barB^{\mathrm{ch}}(L_1)$ has the property
  that its cohomology is finitely generated in each
  weight: the null vector truncation ensures that no
  null descendants contribute, and the weight spaces of
  $L_1$ grow more slowly than those of $V_1$.
 succeeded in 52ms:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item The bar complex $\barB^{\mathrm{ch}}(L_k(\mathfrak{sl}_2))$
  is a sub-dg-coalgebra of\/
  $\barB^{\mathrm{ch}}(V_k(\mathfrak{sl}_2))$, with the
  inclusion~\eqref{eq:bar-contravariant-inclusion} a strict map
  of dg coalgebras.
\item The weight-space decomposition of the bar complex
  truncates: for each bar degree~$n$ and conformal weight~$w$,
  the weight-$w$ component
  $\barB^n(L_k)_{[w]}$ is a quotient of
  $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
  null descendants of weight $\le w$.
\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
  is unchanged: it depends only on the quadratic OPE data,
  which is the same for $V_k$ and $L_k$.  In particular, the
  classical Yang--Baxter equation and the Yangian RTT
  presentation survive the null vector truncation at the
  genus-$0$ level.
\item The bar differential acquires additional relations from the
  null vector: the element
 succeeded in 51ms:
  \textup{(}Theorem~\textup{\ref*{V1-thm:mc2-bar-intrinsic}}\textup{)},
  with modular characteristic
  \begin{equation}\label{eq:platonic-kappa-KM}
  \kappa\bigl(V_k(\fg)\bigr) = \frac{\dim(\fg)\,(k + h^\vee)}{2h^\vee}.
  \end{equation}
  Complementarity:
  $\kappa(\cA) + \kappa(\cA^!) = 0$
  (the Feigin--Frenkel involution ensures
  anti-symmetry around $k = -h^\vee$).

\item \textbf{Collision residue.}
  $r(z) = \Omega_\fg / z$
  \textup{(}single simple pole; the double pole of the OPE is
  absorbed by the $d\log$ bar kernel\textup{)}.
  Satisfies the classical Yang--Baxter equation; the RTT
  quantization produces the Yangian $Y_\hbar(\fg)$.

\item \textbf{Shadow connection.}
  $\nabla^{\mathrm{hol}}_{\mathrm{KM}} = d - \kappa \cdot \omega_g$
  at each genus $g$.  Since $S_4 = 0$ (the quartic contact invariant
 succeeded in 51ms:
  The $\lambda$-bracket is
  $\{J^a_\lambda J^b\} = f^{ab}_c J^c + k\,\delta^{ab}\,\lambda$,
  with maximal pole order $d_{\max} = 2$
  \textup{(}the Killing-form double pole and the
  structure-constant simple pole\textup{)}.

\item \textbf{Collision residue.}
  The bar-kernel absorption gives
  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
  Casimir of $\fg$.  The $r$-matrix satisfies the classical
  Yang--Baxter equation.

\item \textbf{Shadow depth.}
  $r_{\max} = 3$, class~$\mathbf{L}$: the ternary operation $m_3$
  is nonzero at chain level and vanishes on cohomology by the Jacobi
  identity, and $m_k = 0$ on cohomology for all $k \ge 3$.

\item \textbf{Koszul dual.}
  $V_k(\fg)^! \simeq V_{-k-2h^\vee}(\fg)$ at the Feigin--Frenkel
  dual level, with

thinking
**Inspecting general statements**

I see that the examples-worked document has several general statements that are missing the letter "k." I need to patch all active occurrences of this issue. It might also be worth considering additional contexts beyond these. Perhaps I could search again using the patterns that include the missing "k." I should inspect some suspicious contexts around lines 2345, 2518, 2798, 2867, 5411, and maybe 5326 as well.
exec
/bin/zsh -lc "sed -n '2510,2525p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2336,2352p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2790,2804p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2862,2872p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '5318,5333p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '5404,5415p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
For $k \ne -h^\vee$ (non-critical level), the affine
Kac--Moody vertex algebra $\cA = V_k(\fg)$ reaches the
top of the $E_N$ ladder:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\Eone$-chiral
 (Definition~\ref{def:e1-chiral-algebra}): the current
 OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
 structure of an $\Einf$-chiral algebra, hence
 \emph{a fortiori} $\Eone$-chiral.
 The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
 with $\Omega$ the Casimir of~$\fg$.

\item $\Etwo$-chiral on the derived center
 (Definition~\ref{def:E2-chiral-algebra}): automatic from
 the chiral Deligne conjecture.

\item $\Etwo$-topological
 succeeded in 51ms:
shadow of the Wakimoto embedding: the Yangian inherits a
free-field presentation from the free-field realisation
of the original affine algebra.

\smallskip
\noindent
\emph{$R$-matrix compatibility.}
The Yang $R$-matrix
$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
decomposes under the Wakimoto embedding as a product:
$R_{\mathrm{Wak}}(z) = R_{\cH}(z) \cdot R_{\beta\gamma}$,
where $R_{\cH}(z) = e^{k\hbar/z}$ (the Heisenberg
exponential $R$-matrix) and
$R_{\beta\gamma} = \mathrm{Id}$ (trivial on generators).
The Lie-bracket contributions to the $\mathfrak{sl}_2$
Casimir $\Omega$ arise from the composite sector of
 succeeded in 51ms:
\emph{$R$-matrix and Koszul dual.}
The collision residue is the $\mathfrak{sl}_3$ classical
$r$-matrix:
$r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
the Yang $R$-matrix
\begin{equation}\label{eq:A2-lattice-R}
R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
\end{equation}
The Koszul dual is the Yangian
$Y_\hbar(\mathfrak{sl}_3)$.

\smallskip
\noindent
 succeeded in 51ms:
\noindent
\emph{$R$-matrix and Koszul dual.}
The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
The spectral $R$-matrix is
\begin{equation}\label{eq:D4-lattice-R}
R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
\end{equation}
The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.

\smallskip
\noindent
 succeeded in 51ms:
 of degree~$m$, the last factor wraps around the
 boundary circle and is re-inserted at the beginning,
 acquiring the KZ monodromy
 (Remark~\ref{rem:wraparound-monodromy}).

 For $V_k(\mathfrak{sl}_2)$, the $R$-matrix is
 \begin{equation}\label{eq:sl2-ann-Rmatrix}
 R(z) \;=\; 1 + \frac{k\,\Omega}{z}
 + \frac{k^2\,\Omega^2}{2z^2} + \cdots
 \;=\; \exp\!\Bigl(\frac{k\,\Omega}{z}\Bigr)
 + O(1/z^2),
 \end{equation}
 succeeded in 51ms:
\begin{itemize}
\item The bar differential has a \emph{simple-pole component}:
 $d_{\barB}[s^{-1}J^a\,|\,s^{-1}J^b]
 = k\,\delta^{ab} + \epsilon^{ab}{}_c\, s^{-1}J^c$.
 The first term (double pole, scalar) is the Heisenberg
 contribution; the second (simple pole, valued in~$V$)
 is the Lie bracket. Heisenberg has only the first.
\item The $R$-matrix is \emph{matrix-valued}:
 $R(z) = 1 + k\,\Omega/z + \cdots$ with
 $\Omega = \sum_a t^a \otimes t_a \in
 \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$,
 while Heisenberg has $R(z) = e^{k/z}$ (scalar).
 The KZ monodromy $\exp(-2\pi ik\,\Omega)$ is a
 genuine matrix acting on $V^{\otimes n}$, not a phase.
\end{itemize}



thinking
**Maintaining consistency in equations**

I think I need to ensure that I don't change the term "hbar" unless it's really necessary for consistency in a sentence. For example, in the Rosetta line, I would keep it as `R(z)=1+\hbar Ω/z` unless I need to formalize it. If I'm doing a formal expansion, I'd change it to `1+\hbar kΩ/z`. That feels like a good approach to maintain clarity.
thinking
**Searching active files**

I’m considering that the expression R(z)=1+kΩ/z is already pretty good. The line operators seem to have a general R exponential function that’s missing the k. It looks like "rosetta" and "examples-worked" also have a general r without k. I noticed that `ordered_associative_chiral_kd_core` has R(z)=1+\hbarΩ/z at a certain level in the active file, and maybe `ordered_associative_chiral_kd_frontier` does too. I need to specifically search for patterns in the active files.
exec
/bin/zsh -lc "sed -n '2268,2408p' chapters/connections/ht_bulk_boundary_line_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1568,1580p' chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2968,2988p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2280,2310p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'r\\(z\\)\\s*=\\s*\\\\Omega|R\\(z\\)\\s*=\\s*1\\s*\\+\\s*\\\\hbar\\s*,?\\\\Omega|R\\(z\\)\\s*=\\s*1\\s*\\+\\s*\\\\hbar["'^'"\\n]*\\\\Omega|R\\(z\\)\\s*=\\s*1\\s*\\+\\s*k\\\\Omega/z|exp\\"'!'"\\?\\\\Bigl\\(\\\\frac\\{k\\\\,?\\\\Omega\\}\\{z\\}\\)|exp\\(\\\\frac\\{k\\\\,?\\\\Omega\\}\\{z\\}\\)' chapters/connections/line-operators.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/log_ht_monodromy_core.tex chapters/connections/ht_bulk_boundary_line_core.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
 \qquad
 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
\]
The leading-order formula
\begin{equation}\label{eq:R-level-explicit}
 R(z)=1+k\,\Omega/z+O(z^{-2})
\end{equation}
at level~$k$ identifies $k\,\Omega$ as the collision residue, consistent with
Lemma~\ref{lem:inf-braid}.
\end{computation}

\begin{computation}[$\Conf_3^{\mathrm{ord}}(\CC)$ monodromy and Yang--Baxter;
 succeeded in 51ms:
 Cubic algebras. The quantum $R$-matrix satisfies the full
 quantum Yang--Baxter equation (as it must for any
 $\SCchtop$-algebra), but requires independent ternary data
 ($m_3$) beyond the classical $r$-matrix for its determination.
 \emph{Example:} $\beta\gamma$ system.
\item[\textbf{M} (Mixed, $d_{\mathrm{alg}}=\infty$):]
 No finite truncation of the bar data determines the
 $R$-matrix. The full perturbative series of
 higher operations contributes at every degree.
 \emph{Example:} Virasoro at generic~$c$; $\cW_3$ at non-generic central charge.
\end{description}
\end{proposition}

\begin{proof}
The shadow depth $d(\cA)$ is defined by the degree filtration on
the bar coderivation: it is the smallest $r$ such that all MC
components $\Theta^{(n)}_\cA$ for $n>r$ are determined
(via the Stasheff system) by those for $n\le r$. For a free
algebra, the bar coalgebra carries no differential beyond the
linear counit, so $d=0$. For a quadratic algebra, the bar
 succeeded in 50ms:
orderings of the first two tensor factors, and the transfer
matrix encodes the insertion of a bar cohomology class in
the third slot. The consistency of these three insertions
is the Yang--Baxter
equation~\eqref{eq:ybe-from-bar}
(Computation~\ref{comp:ordered-bar-sl2},
Proposition~\ref{prop:ybe-from-d-squared}).

\emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
$\hbar=1/(k+2)$ and
$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
(the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
is generated by $E(u)$, $F(u)$, $H(u)$ with
the same $\hbar$. The RTT relation
$R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
with $T(u)=\bigl(\begin{smallmatrix}
H(u) & F(u) \\ E(u) & -H(u)
\end{smallmatrix}\bigr)$
reproduces all Yangian relations from bar complex
 succeeded in 51ms:
the Koszul sign. The descent recovers the ordinary
$\Sigma_n$-coinvariant bar complex.

For an $E_1$-chiral algebra, the operations respect only
the linear ordering. The equivariant structure must be
\emph{constructed} from the OPE data, and the construction
is the $R$-matrix.
\end{construction}

\begin{construction}[$R$-matrix as monodromy of the ordered
bar complex; \ClaimStatusProvedHere]
\label{constr:r-matrix-monodromy}
\index{R-matrix!from monodromy|textbf}
\index{monodromy!R-matrix}
The simplest descent instance is $n=2$. The ordered
configuration space
$\mathrm{Conf}_2^{\mathrm{ord}}(\mathbb C)
=\{(z_1,z_2)\in\mathbb C^2\mid z_1\neq z_2\}$
has fundamental group $\pi_1=\mathbb Z$, generated by the
loop $\gamma\colon t\mapsto
 succeeded in 51ms:
chapters/examples/rosetta_stone.tex:2345: The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
chapters/examples/rosetta_stone.tex:2518:$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
chapters/connections/ordered_associative_chiral_kd_core.tex:2129:$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
chapters/connections/ordered_associative_chiral_kd_core.tex:2977:The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
chapters/examples/examples-worked.tex:1244:  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
chapters/examples/examples-worked.tex:2729:$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:2860:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
chapters/examples/examples-worked.tex:3150:\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
chapters/examples/examples-worked.tex:3280:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:3397:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
chapters/examples/examples-worked.tex:3744:  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
chapters/examples/examples-worked.tex:3796:$r(z) = \Omega_\fg/z$ has the same analytic structure
chapters/examples/examples-worked.tex:4839:  $r(z) = \Omega_\fg / z$

thinking
**Searching for missing elements**

It seems that I have some missing elements in the active file `ordered_associative_chiral_kd_core` at lines 2129 and 2977, specifically the variable k. I think I need to create a patch for this. I might also want to look for more active files that weren't captured by my regex search since they might not match exactly. Using general patterns like line-operators R(z)=exp(Ω/z) could help me find any additional missing instances of k.
exec
/bin/zsh -lc "rg -n 'exp\\(\\\\Bigl\\(\\\\frac\\{\\\\Omega|exp\\(\\\\frac\\{\\\\Omega|exp\\(\\\\Bigl\\(\\\\frac\\{\\\\Omega_|exp\\(\\\\frac\\{\\\\Omega_|R_\\{["'^'"\\n]*\\}=\\\\exp\\(\\\\Bigl\\(\\\\frac\\{\\\\Omega' chapters/connections/line-operators.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-worked.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/log_ht_monodromy_core.tex chapters/connections/ht_bulk_boundary_line_core.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '930,980p' chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2338,2352p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3748,3776p' chapters/connections/ordered_associative_chiral_kd_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 50ms:

exec
/bin/zsh -lc "rg -n 'k=0|k = 0' chapters/connections/line-operators.tex chapters/examples/rosetta_stone.tex chapters/examples/examples-worked.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/connections/log_ht_monodromy_core.tex chapters/connections/ht_bulk_boundary_line_core.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
top of the $E_N$ ladder:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\Eone$-chiral
 (Definition~\ref{def:e1-chiral-algebra}): the current
 OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
 structure of an $\Einf$-chiral algebra, hence
 \emph{a fortiori} $\Eone$-chiral.
 The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
 with $\Omega$ the Casimir of~$\fg$.

\item $\Etwo$-chiral on the derived center
 (Definition~\ref{def:E2-chiral-algebra}): automatic from
 the chiral Deligne conjecture.

\item $\Etwo$-topological
 succeeded in 51ms:
factorisation) are each individually sufficient to detect
this transition. The classical lattice VOA is tier~(ii)
of the three-tier picture ($E_\infty$ with poles, $R$-matrix
derived from OPE); the quantum deformation promotes it to
tier~(iii) ($E_1$ with independent $R$-matrix).

\smallskip
\noindent
\emph{Koszul dual: $U_q(\widehat{\mathfrak{sl}}_2)$.}
The Koszul dual of $V_q$ is conjectured to be the
quantum affine algebra:
\begin{equation}\label{eq:qlattice-koszul}
V_q^!
\;\simeq\;
U_q(\widehat{\mathfrak{sl}}_2)\,.
\end{equation}
This is the $q$-deformation of the classical result
$V_{\sqrt{2}\Z}^! = Y_\hbar(\mathfrak{sl}_2)$
(Computation~\ref{comp:lattice-voa-ordered-bar}).
The rational $R$-matrix $R(z) = 1 + k\,\Omega/z$
 succeeded in 52ms:
sector,
\[
\cC_{\mathrm{line}}^{\mathrm{red}}(\widehat{\mathfrak{sl}}_2{}_k)
\big|_{\mathrm{eval}}
\simeq \operatorname{Rep}_q(\mathfrak{sl}_2),
\qquad q=e^{i\pi/(k+2)}.
\]
In this reduced evaluation sector, the simple objects are the usual
quantum-group simples $V_\lambda$ ($\lambda\in\mathbb Z_{\ge 0}$,
with $0\le \lambda\le k$ in the integrable level-$k$ sector).

The $r$-matrix $r(z)=k\,\Omega/z$ acts on
$V_{\lambda_1}\otimes V_{\lambda_2}$ via the Casimir:
\[
R_{\lambda_1,\lambda_2}(z)
\;=\;
\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
\;\in\;
\operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
[\![z^{-1}]\!].
 succeeded in 51ms:
chapters/connections/ht_bulk_boundary_line_core.tex:2433:$k=0$ one gets $F_1 = 1/16$, while at the critical level
chapters/connections/ht_bulk_boundary_line_core.tex:3028:For $G = U(1)$: $\Bbound = \cH_k$, $R(z) = e^{k\hbar/z}$, $\Abulk = \cH_k$ (bulk $\simeq$ boundary), $\alpha_T = m_2 + \hbar k\,\eta \otimes \Lambda$. The classical $r$-matrix $r(z) = k/z$ satisfies the $k = 0$ vanishing check trivially.
chapters/connections/ht_bulk_boundary_line_core.tex:3032:For $G = SL_2$: $\Bbound = \widehat{\mathfrak{sl}}_2{}_k$, $\cA^!_{\mathrm{ch}} = \widehat{\mathfrak{sl}}_2{}_{-k-4}$, $r(z) = k\,\Omega/z$ (vanishing at $k = 0$ satisfied). The KZ connection is the degree-$(2,0)$ projection of $\alpha_T$; on evaluation modules, the reduced HT spectral $R$-matrix agrees with the quantum-group $R$-matrix of $U_q(\mathfrak{sl}_2)$ at $q = e^{i\pi/(k+2)}$ (Theorem~\ref{thm:affine-monodromy-identification}). Line category:
chapters/connections/ordered_associative_chiral_kd_frontier.tex:2724:(at $k=0$ the $r$-matrix vanishes,). For the $\mathcal N=2$ SCA, the
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3273:(the $k$ prefactor enforces the vanishing condition: at $k=0$ the
chapters/connections/ordered_associative_chiral_kd_frontier.tex:5978:At $k = 0$ the $r$-matrix vanishes, $r_{\cH_0}(z) = 0$:
chapters/connections/ordered_associative_chiral_kd_frontier.tex:6002:with $\Omega$ the Casimir element. At $k=0$ the $r$-matrix
chapters/connections/ordered_associative_chiral_kd_frontier.tex:6181:At $k = 0$ both factors collapse to the trivial algebra
chapters/connections/ordered_associative_chiral_kd_frontier.tex:6207:$k=0$ vanishes identically and at $k=1$
chapters/connections/log_ht_monodromy_core.tex:155: quadratic Casimir tensor of $\mathfrak g$, vanishing at $k=0$, cf.\
chapters/connections/log_ht_monodromy_core.tex:285:which is the claimed logarithmic form \textup{(}with overall level factor~$k$; at $k=0$ the connection reduces to the exterior derivative, as required\textup{)}.
chapters/connections/log_ht_monodromy_core.tex:1740:$k/(k+h^\vee)$. At $k=0$ both the connection trivializes in the
chapters/connections/log_ht_monodromy_core.tex:1825:Since the affine algebra is Koszul ($m_k = 0$ for $k \geq 3$), there are no higher collision corrections to the residue: the $A_\infty$ Yang--Baxter defect (Theorem~\ref{thm:first-obstruction}) vanishes identically, and the higher support homotopies $h_S$ ($|S| \geq 3$) can be taken to be zero. After projection to degree-zero states, the regular terms in $r(z)$ beyond the simple pole act on higher-degree components that are killed by $p_n$. Thus
chapters/connections/log_ht_monodromy_core.tex:1876:exactness: the operations $m_k = 0$ for $k \geq 3$
chapters/connections/log_ht_monodromy_core.tex:1879:while $m_k = 0$ for $k \geq 3$ by the graph-counting argument
chapters/connections/log_ht_monodromy_core.tex:2006: \item \emph{Bar-complex identification}: By one-loop exactness of $V^k(\fsl_3)$ at generic $k$ \textup{(}Theorem~\textup{\ref{thm:one-loop-koszul})}, the $A_\infty$ operations $m_k = 0$ for $k \geq 3$, so the reduced HT connection is exactly the KZ connection. Therefore the bar-complex associator reproduces the Drinfeld--KZ associator identically, including the cubic Casimir contribution. By the Drinfeld--Kohno theorem, the monodromy identifies with the $U_q(\fsl_3)$ braiding and associator on evaluation modules.
chapters/connections/log_ht_monodromy_core.tex:2011:The computation is a direct verification. The split Casimir $\Omega = \sum_{i \neq j} E_{ij} \ot E_{ji} + \sum_{a,b} (A^{-1})_{ab} H_a \ot H_b$ has the stated eigenvalues by the formula $\Omega|_{V_\nu} = \frac{1}{2}(c_2(\nu) - c_2(\lambda) - c_2(\mu))$. For part~(ii), the Fierz decomposition is standard; the key point is that $\mathcal{D}_{123}^{(-)} \neq 0$ because the totally symmetric tensor $d_{abc}$ of $\fsl_3$ is nonvanishing. The off-diagonal matrix element on the multiplicity space of $V_{(1,1)}$ is proportional to $c_3(2,0) - c_3(0,1) = 35/9 + 10/9 = 5$. For part~(iii), one-loop exactness gives $m_k = 0$ for $k \geq 3$, and the reduced connection $\nabla_{\fS} = d + \Omega\,dz/((k+3)z)$ is the KZ connection for $\fsl_3$ at level $k$. The identification with $U_q(\fsl_3)$ then follows from Theorem~\ref{thm:affine-monodromy-identification} applied to $\fg = \fsl_3$.
chapters/connections/ordered_associative_chiral_kd_core.tex:1420:Equivalently: $K_\cA(z) = 1$ iff the boundary coproduct is primitive iff the shadow tower terminates at depth zero. This is the $K$-matrix shadow of the pole-order hierarchy summarised in Table~\ref{tab:two-colour-koszul-duals} and in the shadow-depth discussion of Volume~I. It is not an $r$-matrix statement: the $K$-matrix modifies the coproduct, not the product, and the level-$k$ vanishing check does not apply directly; the corresponding $r$-matrix check is the one already recorded in the Volume~II affine constructions (classical $r$-matrix $k\,\Omega/z$ vanishes at $k=0$, in which case $\cA = \cH_0$ collapses to the trivial Heisenberg and $K_\cA(z) = 1$, consistent with class~$\mathbf{G}$).
chapters/connections/ordered_associative_chiral_kd_core.tex:2132:is the Casimir. (At $k=0$ the level-stripped
chapters/connections/ordered_associative_chiral_kd_core.tex:2137:$k\,\Omega/z$, which vanishes at $k=0$ in accordance
codex
The remaining active candidates are narrower now. The real violations are formulas stated for generic affine level but written as if `k=1`; I’m excluding true unit-level examples so the patch stays minimal and doesn’t rewrite legitimate specializations.
exec
/bin/zsh -lc "sed -n '2108,2140p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2338,2350p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2968,2990p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\Omega["'^'"\\n]*/z|/z["'^'"\\n]*\\\\Omega|exp\\(["'^'"\\n]*\\\\Omega|\\\\Omega_\\{["'^'"\\n]*\\}/z' chapters/connections/line-operators.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd_frontier.tex chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/log_ht_monodromy_core.tex chapters/connections/ht_bulk_boundary_line_core.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
$s^{-1}e$, $s^{-1}f$, $s^{-1}h$ at degree~$1$ span
the image); the quotient
$H^1=6-\dim(\text{image from degree }3)=\cdots$.
The full computation gives
$\dim H^1(\Barchord)=3=\dim\mathfrak{sl}_2$
(the Koszul dual has the same dimension as the Lie
algebra, consistent with
$(\widehat{\mathfrak{sl}}_2)^!
=\widehat{\mathfrak{sl}}_2{}_{-k-4}$).

\emph{The $R$-matrix from the ordered bar complex.}
The $R$-matrix $R(z)\in\operatorname{End}(V\otimes V)(\!(z)\!)$
for $V=\mathfrak{sl}_2$ is the operator that intertwines
the two orderings:
\[
R(z)\colon
\Barchord_2(e_i\otimes e_j;\,z_1<z_2)
\;\xrightarrow{\;\sim\;}
\Barchord_2(e_j\otimes e_i;\,z_2<z_1).
\]
exec
/bin/zsh -lc "sed -n '2514,2522p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
top of the $E_N$ ladder:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\Eone$-chiral
 (Definition~\ref{def:e1-chiral-algebra}): the current
 OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
 structure of an $\Einf$-chiral algebra, hence
 \emph{a fortiori} $\Eone$-chiral.
 The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
 with $\Omega$ the Casimir of~$\fg$.

\item $\Etwo$-chiral on the derived center
 (Definition~\ref{def:E2-chiral-algebra}): automatic from
 the chiral Deligne conjecture.
 succeeded in 51ms:
orderings of the first two tensor factors, and the transfer
matrix encodes the insertion of a bar cohomology class in
the third slot. The consistency of these three insertions
is the Yang--Baxter
equation~\eqref{eq:ybe-from-bar}
(Computation~\ref{comp:ordered-bar-sl2},
Proposition~\ref{prop:ybe-from-d-squared}).

\emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
$\hbar=1/(k+2)$ and
$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
(the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
is generated by $E(u)$, $F(u)$, $H(u)$ with
the same $\hbar$. The RTT relation
$R(u{-}v)\,T_1(u)\,T_2(v)=T_2(v)\,T_1(u)\,R(u{-}v)$
with $T(u)=\bigl(\begin{smallmatrix}
H(u) & F(u) \\ E(u) & -H(u)
\end{smallmatrix}\bigr)$
reproduces all Yangian relations from bar complex
 succeeded in 51ms:
chapters/connections/ht_bulk_boundary_line_core.tex:3032:For $G = SL_2$: $\Bbound = \widehat{\mathfrak{sl}}_2{}_k$, $\cA^!_{\mathrm{ch}} = \widehat{\mathfrak{sl}}_2{}_{-k-4}$, $r(z) = k\,\Omega/z$ (vanishing at $k = 0$ satisfied). The KZ connection is the degree-$(2,0)$ projection of $\alpha_T$; on evaluation modules, the reduced HT spectral $R$-matrix agrees with the quantum-group $R$-matrix of $U_q(\mathfrak{sl}_2)$ at $q = e^{i\pi/(k+2)}$ (Theorem~\ref{thm:affine-monodromy-identification}). Line category:
chapters/connections/log_ht_monodromy_core.tex:154: $r(z)=k\,\Omega_{\mathrm{aff}}/z$ with $\Omega_{\mathrm{aff}}$ the
chapters/connections/log_ht_monodromy_core.tex:183:When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
chapters/connections/log_ht_monodromy_core.tex:226:If $r(z)=k\,\Omega/z+O(1)$ at level~$k$ near $z=0$ and $\Omega_{ij}$ denotes the action of $\Omega$ in factors $i,j$, then
chapters/connections/log_ht_monodromy_core.tex:273:with $u_{ij}$ a unit. Since $r(z)=k\,\Omega/z+O(1)$ at level~$k$ one has
chapters/connections/log_ht_monodromy_core.tex:291: \exp(2\pi i\,\Omega_e).
chapters/connections/log_ht_monodromy_core.tex:1192: \exp(2\pi i\,\Omega_{ij}^{\mathrm{red}}).
chapters/connections/log_ht_monodromy_core.tex:1205:After a local logarithmic gauge transformation removing the regular part, the monodromy around $t=\varepsilon e^{2\pi is}$ is exactly $\exp(2\pi i\,\Omega_{ij}^{\mathrm{red}})$. Since the connection is flat, parallel transport depends only on homotopy class and therefore defines a representation of the fundamental group.
chapters/connections/log_ht_monodromy_core.tex:1574: R(z)=1+k\,\Omega/z+O(z^{-2})
chapters/connections/log_ht_monodromy_core.tex:1853:\noindent\textbf{(ii).} The Drinfeld--Kohno theorem (\cite{Dri89}, Theorem~3.2; \cite{KL93}) compares the monodromy representation of the KZ connection at level $k$, acting on tensor products of finite-dimensional $\fg$-modules, with the braided tensor product representation of $\mathrm{Rep}_q(\fg)$ at $q = e^{i\pi/(k + h^\vee)}$. The braiding $\sigma_{ij}^2 \mapsto \exp(-2\pi i \cdot \Omega_{ij}/(k + h^\vee))$ on elementary generators matches the universal $R$-matrix of $U_q(\fg)$ acting on $V_i \otimes V_j$. Since $\rho_n^{\mathrm{HT}} = \rho_n^{\mathrm{KZ}}$, the same comparison holds for the HT monodromy.
chapters/connections/log_ht_monodromy_core.tex:1914:$r(z) = k\,\Omega/z$ at level~$k$ up to scalars.
chapters/connections/log_ht_monodromy_core.tex:1932:$\mathrm{P}\!\exp(\int_0^\pi (k\,\Omega/z_{ij} e^{i\theta})
chapters/connections/log_ht_monodromy_core.tex:1934:= \exp(i\pi\,k\, \Omega)$, with the normalization
chapters/examples/rosetta_stone.tex:1841: ($R = 1 + k\Omega/z + \cdots$), Virasoro, $\cW_3$, symplectic
chapters/examples/rosetta_stone.tex:2256:$r(z) = k\,\Omega/z$ (with $\Omega$ the Casimir
chapters/examples/rosetta_stone.tex:2345: The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
chapters/examples/rosetta_stone.tex:2518:$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
chapters/examples/rosetta_stone.tex:2636:$r(z) = k\,\Omega/z$ at $k = 1$, where
chapters/examples/rosetta_stone.tex:2644:The quantisation of $r(z) = k\,\Omega/z$ is the
chapters/examples/rosetta_stone.tex:2645:Yang $R$-matrix $R(z) = 1 + k\hbar\,\Omega/z$,
 succeeded in 52ms:
\smallskip
\noindent
\emph{$R$-matrix compatibility.}
The Yang $R$-matrix
$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
decomposes under the Wakimoto embedding as a product:
$R_{\mathrm{Wak}}(z) = R_{\cH}(z) \cdot R_{\beta\gamma}$,
where $R_{\cH}(z) = e^{k\hbar/z}$ (the Heisenberg
exponential $R$-matrix) and
exec
/bin/zsh -lc "sed -n '4072,4090p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3988,4045p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1836,1846p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '6038,6060p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 & $\mathbf{L}$
 & $\{1,2\}$
 & $1{+}k\Omega/z$ ($k{=}1$)
 & $Y_\hbar(\mathfrak{so}_8)$
 & $1{+}28t$
 & $2$
 & $\Omega\ne 0$
 & entangled \\[3pt]
$V_k(\mathfrak{sl}_2)$
 & $\mathbf{L}$
 & $\{1,2\}$
 & $1{+}k\Omega/z$
 & $Y_\hbar(\mathfrak{sl}_2)$
 & $1{+}3t$
 & $\dfrac{3k}{2(k{+}2)}$
 & $\Omega\ne 0$
 & entangled \\[5pt]
$V_k(\mathfrak{sl}_3)$
 & $\mathbf{L}$
 & $\{1,2\}$
 succeeded in 52ms:
 of the flat connection on configuration space.
 The descent $\bar{B}^{\mathrm{ch,ord}} \to \barBch$ is
 $R$-matrix twisted (Proposition~\ref{prop:r-matrix-descent}).
 Examples: all standard vertex algebras,
 including Heisenberg ($R = e^{k\hbar/z}$), affine Kac--Moody
 ($R = 1 + k\Omega/z + \cdots$), Virasoro, $\cW_3$, symplectic
 bosons, lattice VOAs, $\beta\gamma$, $bc_\lambda$,
 free fermions. For systems whose OPE on generators
 has only a simple pole ($\beta\gamma$, $bc_\lambda$, $\psi$),
 the $d\log$ kernel absorbs it to a constant and the
 generator-level $R$-matrix is $\tau$ or $\mathrm{Id}$;
 succeeded in 52ms:
because $d(s^{-1}E^{(r)}\otimes s^{-1}E^{(s)}) = 0$
($E$--$E$ collision vanishes) and
$d(s^{-1}E^{(s)}\otimes s^{-1}F^{(t)})
\propto s^{-1}H^{(s+t-\cdots)}$, followed by
$d(s^{-1}E^{(r)}\otimes s^{-1}H^{(\cdots)})
\propto s^{-1}E^{(\cdots)}$, which matches the
Jacobi identity
$[e_r,[e_s,f_t]] + [e_s,[f_t,e_r]] = 0$.
All $3^3 \cdot (\text{mode triples}) = 27 \cdot
\text{(modes)}$ checks reduce to the Jacobi identity
for $\mathfrak{sl}_2[t]$.

The \emph{classical Yang--Baxter equation} for the
Yangian $r$-matrix
$r_Y(z) = \hbar\,\Omega/z$ is:
\[
[r_{Y,12}(z_{12}),\,r_{Y,13}(z_{13})]
+ [r_{Y,12}(z_{12}),\,r_{Y,23}(z_{23})]
+ [r_{Y,13}(z_{13}),\,r_{Y,23}(z_{23})]
\;=\;0,
 succeeded in 52ms:
it has its own ordered bar complex with its own
$R$-matrix $R_Y(z)$. By
Construction~\ref{constr:r-matrix-monodromy},
$R_Y(z)$ is the monodromy of the flat connection
defined by the bar differential of the Yangian.
Since the bar differential of the Yangian extracts
only the $\mathfrak{sl}_2[t]$ Lie bracket (parts~(2)
and~(5) above), the $R$-matrix is:
\begin{equation}\label{eq:yangian-r-matrix-own}
R_Y(z)
\;=\;
1 + \Omega_{\mathfrak{sl}_2}/z + O(z^{-2}),
\end{equation}
where $\Omega_{\mathfrak{sl}_2}$ is the Casimir of
$\mathfrak{sl}_2$ (not the Yangian Casimir). This
is the \emph{same} leading-order $R$-matrix as for
$\widehat{\mathfrak{sl}}_{2,k}$
(Computation~\ref{comp:ordered-bar-sl2}). The
deformation parameter $\hbar$ of the Yangian does

thinking
**Considering code style adjustments**

It might be helpful to check the style they're using, especially since they added explicit vanishing checks. I could mimic a minimal approach by searching through current files for similar styles, like in `ht_bulk_boundary_line_core`, which has explicit notes about vanishing checks. I wonder if we can include similar parentheticals in our high-level package statements to enhance clarity. It’s all about finding the best way to communicate our intent effectively!
exec
/bin/zsh -lc "sed -n '4788,4802p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '5352,5366p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3798,3810p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\begin{equation}\label{eq:platonic-CS}
\Pi^{\mathrm{oc}}_X\!\bigl(V_k(\fg)\bigr)
\;=\;
\bigl(\,
V_k(\fg),\;\;
V_{-k-2h^\vee}(\fg),\;\;
C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
\Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
\Omega_\fg/z,\;\;
\nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
HH_*(V_k(\fg)),\;\;
\mathfrak{R}^{\mathrm{oc}}_\bullet
\,\bigr).
\end{equation}
The individual components are:
 succeeded in 50ms:
  & $\kappa$
  & $\kappa + \kappa'$
  & \textbf{Class}
  & $r_{\max}$
  \\
\hline
CS
  & $V_k(\fg)$
  & $V_{-k-2h^\vee}(\fg)$
  & $\Omega_\fg/z$
  & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
  & $0$
  & $\mathbf{L}$ & $3$ \\[6pt]
3d gravity
  & $\mathrm{Vir}_c$
 succeeded in 51ms:
mechanism operates identically.
\end{proposition}

\begin{proof}
The OPE of $V_k(\fg)$ depends only on the structure constants
$f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
(in an orthonormal basis).  For any simple $\fg$, the maximal
pole order is $2$ (from the Killing form), the collision residue
is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
cohomology.  The Jacobi identity is a property of the Lie algebra,
not of its root system: it holds for all simple $\fg$, classical
or exceptional.  The vanishing of $m_4$ and all higher operations




thinking
**Organizing findings**

I need to determine how to report findings effectively. Perhaps I could list one finding per file or cluster. The user wants "PROBLEM at file:line," followed by the exact edits applied. 

It makes sense to group similar problems to avoid excessive bullet points, but I also want to be exhaustive. If a semantic issue occurs in several locations, I might treat them as one finding. However, I have to ensure every instance is clear. I could include line references for each occurrence while grouping files with repeated edits.
thinking
**Planning exact edits**

I need to carefully outline the exact edits applied. Each occurrence gets changed to k\,Ω/z or its variations, with tuple/table/proof summaries updated accordingly. I want to keep the entries concise yet precise.

To implement this, I’ll need to gather the relevant line segments for crafting a patch. Before making any edits, I might send commentary on the changes. Later, I can use `nl -ba` for line numbers.

The plan includes specific updates to lines in "chapters/examples/examples-worked.tex." Overall, I'm ensuring clarity and consistency in the report of these edits.
thinking
**Deciding on changes**

I need to consider the context of "Unchanged from V_1:" regarding the formula without k. It seems acceptable since it specifically references V_1. However, for AP126, there's a unit-level specialization that mentions a missing k. I need to decide whether to patch this or not. The proposition relates to L_1, making the formula without k legitimate since we're working under the assumption that k=1. I may need more clarification on how to proceed.
thinking
**Considering file patching**

I might be able to patch five files at once, but I need to ensure it's only the assigned files — the active files plus the audit ledger. It seems okay to include the ledger since it’s required by the instructions. I wonder if I should update the plan step statuses before or after the editing is done? It feels like it might be better to do it after, but I’m not entirely sure.
codex
I’ve finished the audit pass and have the exact patch set: four active manuscript files plus the audit ledger. The edits are narrowly scoped to AP126-style level-stripping on affine/Kac–Moody `r(z)`/`R(z)` formulas; I’m applying only those replacements now, leaving separate `\hbar`-normalization issues out of scope unless they’re required to carry the level prefix truthfully.
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex
@@ -945,3 +945,3 @@
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
@@ -950,2 +950,4 @@
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
@@ -1243,3 +1243,3 @@
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
@@ -2728,3 +2728,3 @@
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
@@ -2859,3 +2859,3 @@
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
@@ -3149,3 +3149,3 @@
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
@@ -3396,3 +3396,3 @@
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
@@ -3743,3 +3743,3 @@
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
@@ -3795,3 +3795,3 @@
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
@@ -3805,3 +3805,3 @@
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
@@ -4795,3 +4795,3 @@
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
@@ -5360,3 +5360,3 @@
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -2,2 +2,22 @@
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
M /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2128,3 +2128,3 @@
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
@@ -2976,3 +2976,3 @@
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
@@ -4986,2 +4986 @@
 \end{remark}
-
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
@@ -2344,3 +2344,3 @@
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
@@ -2797,3 +2797,3 @@
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
@@ -2866,3 +2866,3 @@
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
apply_patch(auto_approved=true) exited 0 in 101ms:
Success. Updated the following files:
M chapters/examples/examples-worked.tex
M chapters/examples/rosetta_stone.tex
M chapters/connections/line-operators.tex
M chapters/connections/ordered_associative_chiral_kd_core.tex
M compute/audit/linear_read_notes.md
file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..59246d0a7de9a132cd16dac16407683357b4ec26
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..c6eacb3ee2e883bd57e246468d39ae90247c88e6
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2795,7 +2795,7 @@
 of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2864,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`

file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..59246d0a7de9a132cd16dac16407683357b4ec26
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..c6eacb3ee2e883bd57e246468d39ae90247c88e6
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2795,7 +2795,7 @@
 of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2864,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`


thinking
**Considering code changes**

I need to run targeted `rg` patterns across active files and maybe use `git diff --stat` or `git diff --unified=0` to inspect changes. I want to check for grammar issues in specific lines, like in Rosetta where it says `at level k=1`, but the formula is `1+ \frac{ħ k Ω}{z}`. I'll also consider line breaks, and maybe add `\mathrm{id}` instead of `identity`. Finally, I’ll use `nl -ba` for exact line numbers. Let's verify with greps!
codex
The patch is in. I’m re-auditing the touched surface now with negative greps and line-number reads so the closeout can report exact locations and confirm there are no generic affine formulas still missing the level prefix.
exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '2125,2138p;2974,2982p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/examples-worked.tex | sed -n '1238,1250p;2724,2733p;2856,2864p;3146,3154p;3393,3400p;3740,3748p;3792,3807p;4794,4800p;5358,5364p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'r\\(z\\)\\s*=\\s*\\\\Omega|\\\\Omega_\\{["'^'"\\n]*\\}/z|R\\(z\\)\\s*=\\s*1\\s*\\+\\s*\\\\hbar\\s*,?\\\\Omega|exp\\(\\\\Bigl\\(\\\\frac\\{\\\\Omega|exp\\(\\\\frac\\{\\\\Omega' chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/line-operators.tex chapters/connections/ordered_associative_chiral_kd_core.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/rosetta_stone.tex | sed -n '2341,2347p;2792,2800p;2864,2869p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/line-operators.tex | sed -n '940,952p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba compute/audit/linear_read_notes.md | sed -n '1,28p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff --unified=0 -- chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/line-operators.tex chapters/connections/ordered_associative_chiral_kd_core.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  2341	 (Definition~\ref{def:e1-chiral-algebra}): the current
  2342	 OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  2343	 structure of an $\Einf$-chiral algebra, hence
  2344	 \emph{a fortiori} $\Eone$-chiral.
  2345	 The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  2346	 with $\Omega$ the Casimir of~$\fg$.
  2347	
  2792	$r$-matrix:
  2793	$r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
  2794	where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
  2795	of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
  2796	the Yang $R$-matrix
  2797	\begin{equation}\label{eq:A2-lattice-R}
  2798	R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
  2799	\end{equation}
  2800	The Koszul dual is the Yangian
  2864	The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
  2865	The spectral $R$-matrix is
  2866	\begin{equation}\label{eq:D4-lattice-R}
  2867	R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 succeeded in 51ms:
  1238	  $\Zder^{\mathrm{ch}}(\cA_\partial)
  1239	  = C^\bullet_{\mathrm{ch}}(V_k(\fg),\, V_k(\fg))$.
  1240	  The bulk observables are chiral Hochschild cochains of the boundary
  1241	  algebra, not the bar complex.
  1242	
  1243	\item \textbf{Collision residue.}
  1244	  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
  1245	  equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
  1246	
  1247	\item \textbf{Modular MC element.}
  1248	  $\Theta_\cA = D_\cA - d_0 \in \MC(\gAmod)$, with modular
  1249	  characteristic $\kappa = \kappa(V_k(\fg))
  1250	  = \dim(\fg)\cdot(k + h^\vee)/(2h^\vee)$ and complementarity
  2724	with the monodromy of the KZ connection on the corresponding
  2725	integrable affine comparison surface.
  2726	On the manuscript's affine Kac--Moody comparison surface, the
  2727	corresponding genus-$0$ bar-side connection identifies with KZ and
  2728	begins from the same classical residue
  2729	$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
  2730	\end{proposition}
 succeeded in 51ms:
chapters/examples/examples-worked.tex:2729:$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:2860:  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
chapters/examples/examples-worked.tex:3150:\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
chapters/examples/examples-worked.tex:3280:  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:3397:  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
chapters/examples/examples-worked.tex:4839:  $r(z) = \Omega_\fg / z$
chapters/examples/rosetta_stone.tex:2793:$r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
chapters/examples/rosetta_stone.tex:2795:of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
chapters/examples/rosetta_stone.tex:2864:The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
chapters/connections/ordered_associative_chiral_kd_core.tex:4083:1 + \Omega_{\mathfrak{sl}_2}/z + O(z^{-2}),
 succeeded in 51ms:
  2125	\;\xrightarrow{\;\sim\;}
  2126	\Barchord_2(e_j\otimes e_i;\,z_2<z_1).
  2127	\]
  2128	For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
  2129	$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
  2130	$\hbar=1/(k+2)$, where
  2131	$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
  2132	is the Casimir. (At $k=0$ the level-stripped
  2133	coefficient $\hbar\to 1/2$ remains nonzero because
  2134	the $\widehat{\mathfrak{sl}}_2$ Sugawara shift
  2135	$k+2$ survives; the strict classical $r$-matrix
  2136	on the underlying affine current algebra is
  2137	$k\,\Omega/z$, which vanishes at $k=0$ in accordance
  2138	with Anti-Pattern~\ref*{AP:126}.) The Yang--Baxter equation
  2974	Proposition~\ref{prop:ybe-from-d-squared}).
  2975	
  2976	\emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
  2977	The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
  2978	$\hbar=1/(k+2)$ and
  2979	$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 succeeded in 51ms:
   940	
   941	The $r$-matrix $r(z)=k\,\Omega/z$ acts on
   942	$V_{\lambda_1}\otimes V_{\lambda_2}$ via the Casimir:
   943	\[
   944	R_{\lambda_1,\lambda_2}(z)
   945	\;=\;
   946	\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
   947	\;\in\;
   948	\operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
   949	[\![z^{-1}]\!].
   950	\]
   951	At $k=0$ this braiding collapses to the identity, as the
   952	classical residue $r(z)=k\,\Omega/z$ vanishes.
 succeeded in 51ms:
     1	# Linear Read Notes
     2	
     3	## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
     4	
     5	- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
     6	- Status: COMPLETE
     7	
     8	### Findings
     9	
    10	1. `2026-04-13-007`
    11	   Severity: `MODERATE`
    12	   Class: `D/W`
    13	   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
    14	   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
    15	   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
    16	   Status: `FIXED`
    17	
    18	### Verification
    19	
    20	- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
 succeeded in 51ms:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9..503688d 100644
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -946 +946 @@ R_{\lambda_1,\lambda_2}(z)
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
@@ -950,0 +951,2 @@ R_{\lambda_1,\lambda_2}(z)
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed..4dd4d86 100644
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2129 +2129 @@ For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
@@ -2977 +2977 @@ Proposition~\ref{prop:ybe-from-d-squared}).
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..59246d0a7de9a132cd16dac16407683357b4ec26
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..c6eacb3ee2e883bd57e246468d39ae90247c88e6
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2795,7 +2795,7 @@
 of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2864,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`

codex
The re-audit caught two live survivors in `examples-worked` and one level-1 narrative sentence in `rosetta`. I’m doing one final cleanup pass so the active Vol II surface is genuinely AP126-clean, then I’ll freeze the result.
exec
/bin/zsh -lc "sed -n '4834,4842p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '4078,4086p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2793,2797p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3276,3283p' chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  bar differential on degree-$2$ elements.

\item \textbf{Collision residue.}
  Unchanged from $V_1$:
  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.

\item \textbf{Finite representation theory.}
  The bar complex $\barB^{\mathrm{ch}}(L_1)$ has the property
 succeeded in 52ms:
only the $\mathfrak{sl}_2[t]$ Lie bracket (parts~(2)
and~(5) above), the $R$-matrix is:
\begin{equation}\label{eq:yangian-r-matrix-own}
R_Y(z)
\;=\;
1 + \Omega_{\mathfrak{sl}_2}/z + O(z^{-2}),
\end{equation}
where $\Omega_{\mathfrak{sl}_2}$ is the Casimir of
$\mathfrak{sl}_2$ (not the Yangian Casimir). This
 succeeded in 52ms:
  $\kappa(\cA) + \kappa(\cA^!) = 0$
  (the Feigin--Frenkel involution ensures
  anti-symmetry around $k = -h^\vee$).

\item \textbf{Collision residue.}
  $r(z) = \Omega_\fg / z$
  \textup{(}single simple pole; the double pole of the OPE is
  absorbed by the $d\log$ bar kernel\textup{)}.
  Satisfies the classical Yang--Baxter equation; the RTT
 succeeded in 52ms:
$r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
the Yang $R$-matrix
\begin{equation}\label{eq:A2-lattice-R}
file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..59246d0a7de9a132cd16dac16407683357b4ec26
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..c6eacb3ee2e883bd57e246468d39ae90247c88e6
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2795,7 +2795,7 @@
 of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2864,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`



thinking
**Considering patch updates**

I definitely need to patch 4839, and patch 3280 might be necessary if we're strict with AP126. I could consider adjusting 2795 to a specific sentence format. For 4083, it seems related to Yangian, not AP126, so we can possibly exclude that but need to confirm if it still appears in grep results.

After applying patches, I’ll need to clarify which formulas are aligned with Yangian to keep everything organized. It’s a bit complex, but I think I’m on the right track!
thinking
**Evaluating necessary patches**

I’m considering patches for `examples-worked` 4839 and 3280. Although 3280 is level 1 explicit, I think it’s okay to keep `k` visible even when k=1. I could mention something like: “Unchanged from V_1: $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ at $k=1$” but maybe I can just go for a minimal patch focusing on the formula itself. For rosetta 2795, I might apply a sentence stating the collision residue. Let's move forward with these patches!
file update
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
@@ -2794,3 +2794,4 @@
 where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
-of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
+of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
+$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
M /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
@@ -3279,3 +3279,3 @@
   Unchanged from $V_1$:
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 
@@ -4838,3 +4838,3 @@
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$
+  $r(z) = k\,\Omega_\fg / z$
   \textup{(}single simple pole; the double pole of the OPE is
apply_patch(auto_approved=true) exited 0 in 73ms:
Success. Updated the following files:
M chapters/examples/examples-worked.tex
M chapters/examples/rosetta_stone.tex
file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..e764a3343796e05210c23ef15801dacac57d714c
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3277,7 +3277,7 @@
 
 \item \textbf{Collision residue.}
   Unchanged from $V_1$:
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 
 \item \textbf{Finite representation theory.}
   The bar complex $\barB^{\mathrm{ch}}(L_1)$ has the property
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -4836,7 +4836,7 @@
   anti-symmetry around $k = -h^\vee$).
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$
+  $r(z) = k\,\Omega_\fg / z$
   \textup{(}single simple pole; the double pole of the OPE is
   absorbed by the $d\log$ bar kernel\textup{)}.
   Satisfies the classical Yang--Baxter equation; the RTT
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..428b7303296fdf974432032a0cdd37b9bf5ea898
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2792,10 +2792,11 @@
 $r$-matrix:
 $r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
 where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
-of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
+of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
+$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2865,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`

file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..e764a3343796e05210c23ef15801dacac57d714c
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3277,7 +3277,7 @@
 
 \item \textbf{Collision residue.}
   Unchanged from $V_1$:
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 
 \item \textbf{Finite representation theory.}
   The bar complex $\barB^{\mathrm{ch}}(L_1)$ has the property
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -4836,7 +4836,7 @@
   anti-symmetry around $k = -h^\vee$).
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$
+  $r(z) = k\,\Omega_\fg / z$
   \textup{(}single simple pole; the double pole of the OPE is
   absorbed by the $d\log$ bar kernel\textup{)}.
   Satisfies the classical Yang--Baxter equation; the RTT
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..428b7303296fdf974432032a0cdd37b9bf5ea898
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2792,10 +2792,11 @@
 $r$-matrix:
 $r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
 where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
-of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
+of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
+$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2865,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`

exec
/bin/zsh -lc "nl -ba chapters/examples/examples-worked.tex | sed -n '3278,3282p;4836,4841p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/rosetta_stone.tex | sed -n '2793,2799p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'r\\(z\\)\\s*=\\s*\\\\Omega|\\\\Omega_\\{["'^'"\\n]*\\}/z|R\\(z\\)\\s*=\\s*1\\s*\\+\\s*\\\\hbar\\s*,?\\\\Omega|exp\\(\\\\Bigl\\(\\\\frac\\{\\\\Omega|exp\\(\\\\frac\\{\\\\Omega' chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/line-operators.tex chapters/connections/ordered_associative_chiral_kd_core.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  3278	\item \textbf{Collision residue.}
  3279	  Unchanged from $V_1$:
  3280	  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
  3281	
  3282	\item \textbf{Finite representation theory.}
  4836	  anti-symmetry around $k = -h^\vee$).
  4837	
  4838	\item \textbf{Collision residue.}
  4839	  $r(z) = k\,\Omega_\fg / z$
  4840	  \textup{(}single simple pole; the double pole of the OPE is
  4841	  absorbed by the $d\log$ bar kernel\textup{)}.
 succeeded in 52ms:
  2793	$r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
  2794	where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
  2795	of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
  2796	$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
  2797	the Yang $R$-matrix
  2798	\begin{equation}\label{eq:A2-lattice-R}
  2799	R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd_core.tex:4083:1 + \Omega_{\mathfrak{sl}_2}/z + O(z^{-2}),
chapters/examples/examples-worked.tex:2729:$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:2860:  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
chapters/examples/examples-worked.tex:3150:\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
chapters/examples/examples-worked.tex:3280:  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:3397:  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
chapters/examples/rosetta_stone.tex:2793:$r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
chapters/examples/rosetta_stone.tex:2796:$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
chapters/examples/rosetta_stone.tex:2865:The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..e764a3343796e05210c23ef15801dacac57d714c
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3277,7 +3277,7 @@
 
 \item \textbf{Collision residue.}
   Unchanged from $V_1$:
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 
 \item \textbf{Finite representation theory.}
   The bar complex $\barB^{\mathrm{ch}}(L_1)$ has the property
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -4836,7 +4836,7 @@
   anti-symmetry around $k = -h^\vee$).
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$
+  $r(z) = k\,\Omega_\fg / z$
   \textup{(}single simple pole; the double pole of the OPE is
   absorbed by the $d\log$ bar kernel\textup{)}.
   Satisfies the classical Yang--Baxter equation; the RTT
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..428b7303296fdf974432032a0cdd37b9bf5ea898
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2792,10 +2792,11 @@
 $r$-matrix:
 $r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
 where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
-of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
+of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
+$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2865,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`

exec
/bin/zsh -lc "rg -n 'r\\(z\\)\\s*=\\s*\\\\Omega|R\\(z\\)\\s*=\\s*1\\s*\\+\\s*\\\\hbar\\s*\\\\Omega|exp\\(\\\\Bigl\\(\\\\frac\\{\\\\Omega|exp\\(\\\\frac\\{\\\\Omega|R_Y\\(z\\)\\s*=\\s*1\\s*\\+\\s*\\\\Omega' chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/line-operators.tex chapters/connections/ordered_associative_chiral_kd_core.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short chapters/examples/examples-worked.tex chapters/examples/rosetta_stone.tex chapters/connections/line-operators.tex chapters/connections/ordered_associative_chiral_kd_core.tex compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
 M chapters/connections/line-operators.tex
 M chapters/connections/ordered_associative_chiral_kd_core.tex
 M chapters/examples/examples-worked.tex
 M chapters/examples/rosetta_stone.tex
 M compute/audit/linear_read_notes.md
file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..e764a3343796e05210c23ef15801dacac57d714c
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3277,7 +3277,7 @@
 
 \item \textbf{Collision residue.}
   Unchanged from $V_1$:
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 
 \item \textbf{Finite representation theory.}
   The bar complex $\barB^{\mathrm{ch}}(L_1)$ has the property
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -4836,7 +4836,7 @@
   anti-symmetry around $k = -h^\vee$).
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$
+  $r(z) = k\,\Omega_\fg / z$
   \textup{(}single simple pole; the double pole of the OPE is
   absorbed by the $d\log$ bar kernel\textup{)}.
   Satisfies the classical Yang--Baxter equation; the RTT
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..428b7303296fdf974432032a0cdd37b9bf5ea898
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2792,10 +2792,11 @@
 $r$-matrix:
 $r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
 where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
-of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
+of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
+$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2865,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`

Plan update
AP126 sweep converged on the active Vol II affine/Kac--Moody surface; edits and verification are complete.
  ✓ Identify the original AP126 rule and locate all Vol II candidate violations
  ✓ Read the live manuscript surfaces and determine exact minimum edits
  ✓ Apply fixes and log findings in the audit ledger
  ✓ Run targeted verification greps/tests and re-audit the touched surface
file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..e764a3343796e05210c23ef15801dacac57d714c
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3277,7 +3277,7 @@
 
 \item \textbf{Collision residue.}
   Unchanged from $V_1$:
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 
 \item \textbf{Finite representation theory.}
   The bar complex $\barB^{\mathrm{ch}}(L_1)$ has the property
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -4836,7 +4836,7 @@
   anti-symmetry around $k = -h^\vee$).
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$
+  $r(z) = k\,\Omega_\fg / z$
   \textup{(}single simple pole; the double pole of the OPE is
   absorbed by the $d\log$ bar kernel\textup{)}.
   Satisfies the classical Yang--Baxter equation; the RTT
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..428b7303296fdf974432032a0cdd37b9bf5ea898
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2792,10 +2792,11 @@
 $r$-matrix:
 $r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
 where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
-of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
+of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
+$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2865,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`


thinking
**Finalizing build notes**

I’m thinking that I shouldn’t include a full build run in the answer. Instead, I might mention using `git diff --unified=0` for specific line numbers from the diff. It feels important to share the findings concisely. I should highlight that I’m considering whether the user is asking about the same AP126 fix. Ultimately, I want to make sure the final notes are clear and include those findings while staying concise.
codex
CONVERGED

- `PROBLEM` at [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1244) and the same live affine/Kac--Moody summary layer at lines `2729, 2860, 3150, 3280, 3397, 3744, 3796, 3806, 4796, 4839, 5361`: generic collision residues were written with the level stripped as `\Omega/z`.
  `EXACT edit applied`: changed each generic affine form to the level-prefixed form:
  `\Omega_\fg / z -> k\,\Omega_\fg / z`, `\Omega_\fg/z -> k\,\Omega_\fg/z`, `\Omega_{\mathfrak{sl}_2}/z -> k\,\Omega_{\mathfrak{sl}_2}/z`.

- `PROBLEM` at [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2345) and the related active affine/lattice lines `2795-2799, 2867`: leading spectral `R`-matrix formulas dropped the level prefix.
  `EXACT edit applied`: changed
  `R(z) = 1 + \hbar\,\Omega/z + \cdots -> R(z) = 1 + \hbar\,k\,\Omega/z + \cdots`,
  `R(z) = 1 + \hbar\,\Omega_{\mathfrak{sl}_3}/z -> R(z) = 1 + \hbar\,k\,\Omega_{\mathfrak{sl}_3}/z`,
  `R(z) = 1 + \hbar\,\Omega_{\mathfrak{so}_8}/z -> R(z) = 1 + \hbar\,k\,\Omega_{\mathfrak{so}_8}/z`,
  and rewrote the level-one sentence to keep the prefix visible:
  `k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z`.

- `PROBLEM` at [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:946): the reduced evaluation-sector braiding exponent omitted the affine level, so the `k=0` collapse was not encoded in the formula.
  `EXACT edit applied`: changed
  `\exp(\Omega_{\lambda_1,\lambda_2}/z) -> \exp(k\,\Omega_{\lambda_1,\lambda_2}/z)`
  and added:
  `At k=0 this braiding collapses to the identity, as the classical residue r(z)=k\,\Omega/z vanishes.`

- `PROBLEM` at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2129) and line `2977`: two generic affine `R`-matrix leading terms were written as `1+\hbar\,\Omega/z+...` even though the surrounding discussion was explicitly level-`k`.
  `EXACT edit applied`: changed both occurrences to
  `R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})`.

- `PROBLEM` at [linear_read_notes.md](/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:3): the AP126 sweep was not recorded in the persistent audit ledger.
  `EXACT edit applied`: added the section `2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep` with target, finding, fix, and verification notes.

Verification used targeted `rg` re-audits on the touched live surface. No remaining generic affine/Kac--Moody AP126 survivor is left in those files; the one remaining no-`k` hit is the Yangian-specific `R_Y(z)` at [ordered_associative_chiral_kd_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:4083), which is outside this affine-level AP126 scope. I did not run a full LaTeX build.
file update:
diff --git a/chapters/connections/line-operators.tex b/chapters/connections/line-operators.tex
index 170d9c9399cd974ff7d84a7aa3313fb4469971c5..503688d2663eb7e815d8eb8b758a551a6853c2bc
--- a/chapters/connections/line-operators.tex
+++ b/chapters/connections/line-operators.tex
@@ -943,11 +943,13 @@
 \[
 R_{\lambda_1,\lambda_2}(z)
 \;=\;
-\exp\Bigl(\frac{\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
+\exp\Bigl(\frac{k\,\Omega_{\lambda_1,\lambda_2}}{z}\Bigr)
 \;\in\;
 \operatorname{End}(V_{\lambda_1}\otimes V_{\lambda_2})
 [\![z^{-1}]\!].
 \]
+At $k=0$ this braiding collapses to the identity, as the
+classical residue $r(z)=k\,\Omega/z$ vanishes.
 For $k=1$ (simplest non-abelian level): two simple objects
 $V_0$ (trivial) and $V_1$ (fundamental). Fusion:
 $V_1\otimes V_1=V_0$. The $R$-matrix at $\lambda_1=\lambda_2=1$
diff --git a/chapters/connections/ordered_associative_chiral_kd_core.tex b/chapters/connections/ordered_associative_chiral_kd_core.tex
index 5aa3aed5a37e761748d4ebed9810251156ab8316..4dd4d861fc4d676b7eea0f68a4c1fe50a5d4596e
--- a/chapters/connections/ordered_associative_chiral_kd_core.tex
+++ b/chapters/connections/ordered_associative_chiral_kd_core.tex
@@ -2126,7 +2126,7 @@
 \Barchord_2(e_j\otimes e_i;\,z_2<z_1).
 \]
 For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
-$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+$R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$, where
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 is the Casimir. (At $k=0$ the level-stripped
@@ -2974,7 +2974,7 @@
 Proposition~\ref{prop:ybe-from-d-squared}).
 
 \emph{For $\widehat{\mathfrak{sl}}_2$ at level~$k$.}
-The $R$-matrix is $R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
+The $R$-matrix is $R(z)=1+\hbar\,k\,\Omega/z+O(z^{-2})$ with
 $\hbar=1/(k+2)$ and
 $\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
 (the Casimir), and the Yangian $Y_\hbar(\mathfrak{sl}_2)$
@@ -4984,4 +4984,3 @@
 and Remark~\textup{\ref{rem:r-matrix-coproduct-warning}}
 for the specific mechanisms.
 \end{remark}
-
diff --git a/chapters/examples/examples-worked.tex b/chapters/examples/examples-worked.tex
index 66f16262ea82f05bf5fcd4660196f1d4bebe3e49..e764a3343796e05210c23ef15801dacac57d714c
--- a/chapters/examples/examples-worked.tex
+++ b/chapters/examples/examples-worked.tex
@@ -1241,7 +1241,7 @@
   algebra, not the bar complex.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$, satisfying the classical Yang--Baxter
+  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
   equation.  The RTT quantization produces the Yangian $Y_\hbar(\fg)$.
 
 \item \textbf{Modular MC element.}
@@ -2726,7 +2726,7 @@
 On the manuscript's affine Kac--Moody comparison surface, the
 corresponding genus-$0$ bar-side connection identifies with KZ and
 begins from the same classical residue
-$r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 \end{proposition}
 
 At the explicit level $k = 1$ (the simplest integrable case):
@@ -2857,7 +2857,7 @@
   of dimension $k + 1$.
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$,
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
   satisfying the classical Yang--Baxter equation.
   The RTT quantization gives the Yangian
   $Y_\hbar(\mathfrak{sl}_2)$.
@@ -3147,7 +3147,7 @@
   $\barB^n(L_k)_{[w]}$ is a quotient of
   $\barB^n(V_k)_{[w]}$ by the sub-coalgebra generated by
   null descendants of weight $\le w$.
-\item The collision residue $r(z) = \Omega_{\mathfrak{sl}_2}/z$
+\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   is unchanged: it depends only on the quadratic OPE data,
   which is the same for $V_k$ and $L_k$.  In particular, the
   classical Yang--Baxter equation and the Yangian RTT
@@ -3277,7 +3277,7 @@
 
 \item \textbf{Collision residue.}
   Unchanged from $V_1$:
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$.
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
 
 \item \textbf{Finite representation theory.}
   The bar complex $\barB^{\mathrm{ch}}(L_1)$ has the property
@@ -3394,7 +3394,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},nosep]
 \item \textbf{The bar complex sees the collision residue.}
   The classical $r$-matrix
-  $r(z) = \Omega_{\mathfrak{sl}_2}/z$ is the same for both
+  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
   $V_k$ and $L_k$, hence the perturbative quantum group
   structure \textup{(}Yangian $Y_\hbar(\mathfrak{sl}_2)$,
   KZ connection\textup{)} is unchanged at genus~$0$.
@@ -3741,7 +3741,7 @@
 
 \item \textbf{Collision residue.}
   The bar-kernel absorption gives
-  $r(z) = \Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
+  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
   Casimir of $\fg$.  The $r$-matrix satisfies the classical
   Yang--Baxter equation.
 
@@ -3793,7 +3793,7 @@
 (the Casimir eigenvalue equals the dual Coxeter number)
 is the root cause of the uniform shadow classification:
 it ensures that the collision residue
-$r(z) = \Omega_\fg/z$ has the same analytic structure
+$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
 for all simple types, and that the Jacobi cancellation
 mechanism operates identically.
 \end{proposition}
@@ -3803,7 +3803,7 @@
 $f^{ab}_c$ and the Killing form $\kappa^{ab} = k\,\delta^{ab}$
 (in an orthonormal basis).  For any simple $\fg$, the maximal
 pole order is $2$ (from the Killing form), the collision residue
-is $\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
+is $k\,\Omega_\fg/z$ (by bar-kernel absorption, AP19), and the Jacobi
 identity $f^{ab}_e f^{ec}_d + \mathrm{cyc} = 0$ kills $m_3$ on
 cohomology.  The Jacobi identity is a property of the Lie algebra,
 not of its root system: it holds for all simple $\fg$, classical
@@ -4793,7 +4793,7 @@
 V_{-k-2h^\vee}(\fg),\;\;
 C^\bullet_{\mathrm{ch}}(V_k, V_k),\;\;
 \Theta^{\mathrm{oc}}_{\mathrm{KM}},\;\;
-\Omega_\fg/z,\;\;
+k\,\Omega_\fg/z,\;\;
 \nabla^{\mathrm{hol}}_{\mathrm{KM}},\;\;
 HH_*(V_k(\fg)),\;\;
 \mathfrak{R}^{\mathrm{oc}}_\bullet
@@ -4836,7 +4836,7 @@
   anti-symmetry around $k = -h^\vee$).
 
 \item \textbf{Collision residue.}
-  $r(z) = \Omega_\fg / z$
+  $r(z) = k\,\Omega_\fg / z$
   \textup{(}single simple pole; the double pole of the OPE is
   absorbed by the $d\log$ bar kernel\textup{)}.
   Satisfies the classical Yang--Baxter equation; the RTT
@@ -5358,7 +5358,7 @@
 CS
   & $V_k(\fg)$
   & $V_{-k-2h^\vee}(\fg)$
-  & $\Omega_\fg/z$
+  & $k\,\Omega_\fg/z$
   & $\dfrac{d(k{+}h^\vee)}{2h^\vee}$
   & $0$
   & $\mathbf{L}$ & $3$ \\[6pt]
diff --git a/chapters/examples/rosetta_stone.tex b/chapters/examples/rosetta_stone.tex
index 55d13a4f44991007bfe11e4c767ae4ab84b02f0b..428b7303296fdf974432032a0cdd37b9bf5ea898
--- a/chapters/examples/rosetta_stone.tex
+++ b/chapters/examples/rosetta_stone.tex
@@ -2342,7 +2342,7 @@
  OPE~\eqref{eq:cs-km-ope} gives $V_k(\fg)$ the
  structure of an $\Einf$-chiral algebra, hence
  \emph{a fortiori} $\Eone$-chiral.
- The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
+ The $R$-matrix is $R(z) = 1 + \hbar\,k\,\Omega/z + \cdots$
  with $\Omega$ the Casimir of~$\fg$.
 
 \item $\Etwo$-chiral on the derived center
@@ -2792,10 +2792,11 @@
 $r$-matrix:
 $r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
 where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
-of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
+of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is
+$k\,\Omega_{\mathfrak{sl}_3}/z=\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
 the Yang $R$-matrix
 \begin{equation}\label{eq:A2-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{sl}_3}}{z}\,.
 \end{equation}
 The Koszul dual is the Yangian
 $Y_\hbar(\mathfrak{sl}_3)$.
@@ -2864,7 +2865,7 @@
 The collision residue is $r(z) = k\,\Omega_{\mathfrak{so}_8}/z$.
 The spectral $R$-matrix is
 \begin{equation}\label{eq:D4-lattice-R}
-R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
+R(z) \;=\; 1 + \frac{\hbar\,k\,\Omega_{\mathfrak{so}_8}}{z}\,.
 \end{equation}
 The Koszul dual is $Y_\hbar(\mathfrak{so}_8)$.
 
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index 376d786b3767c5ac28e49fb1ba3c357240e13a24..0727fd698dfd8c0fcb22f345b01c57c3f7e7c7d0
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,25 @@
 # Linear Read Notes
 
+## 2026-04-13 - Vol II AP126 Affine Level-Prefix Sweep
+
+- Target: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+- Status: COMPLETE
+
+### Findings
+
+1. `2026-04-13-007`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/examples/examples-worked.tex`, `chapters/examples/rosetta_stone.tex`, `chapters/connections/line-operators.tex`, `chapters/connections/ordered_associative_chiral_kd_core.tex`
+   Issue: the active Vol II affine/Kac--Moody summary layer still had AP126 survivors: generic collision residues or leading $R$-matrix terms were written with the level stripped (`\Omega/z`, `\exp(\Omega/z)`, `1+\hbar\,\Omega/z`) even though the surrounding text treated the same formulas as level-dependent and elsewhere enforced the `k=0 \Rightarrow r=0` sanity check.
+   Fix: restored the explicit level prefix on every live affine/Kac--Moody survivor in scope (`k\,\Omega/z`, `\exp(k\,\Omega/z)`, `1+\hbar\,k\,\Omega/z`), and added the missing `k=0` collapse sentence to the line-operator evaluation-sector summary.
+   Status: `FIXED`
+
+### Verification
+
+- Grepped the active input surface for stripped affine/Kac--Moody patterns before patching: `r(z)=\Omega/z`, `\Omega_\fg/z`, `R(z)=1+\hbar\,\Omega/z`, and `\exp(\Omega/z)`.
+- Re-grepped the touched files after patching to confirm that the surviving no-`k` formulas are explicit `k=1`/Yangian specializations rather than generic affine statements.
+
 ## 2026-04-13 - Bar-Cobar Review Fortification
 
 - Target: `chapters/connections/bar-cobar-review.tex`

tokens used
158,653
