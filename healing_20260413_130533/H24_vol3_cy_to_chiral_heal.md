# H24_vol3_cy_to_chiral_heal (722s)



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
session id: 019d86b9-94cc-7050-ba33-92e1b04a5aa3
--------
user
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.
Your mission is threefold:

1. HEAL: find remaining wounds (gaps, weaknesses, fragilities) and repair them
2. FORTIFY: for every main result, construct an ALTERNATIVE proof path that provides
   REDUNDANCY — if one proof fails, the other stands independently
3. UPGRADE: where a result is conditional, investigate whether the condition can be
   REMOVED by new mathematical insight, alternative technique, or reformulation

You have WRITE access. Make edits. Write new proofs. Add remarks.
The standard is: every theorem that can have two independent proofs MUST have two.
</task>

<action_safety>
Keep edits within assigned scope. After every substantial edit, re-read and verify.
New proofs must be mathematically rigorous — no hand-waving, no "by analogy."
If you cannot complete a proof: write a detailed proof SKETCH with the key steps
identified and the remaining gap precisely named.
</action_safety>

<completeness_contract>
For each theorem in your scope:
1. Verify the PRIMARY proof is now sound (after rectification)
2. Write or sketch a SECONDARY proof via a different technique
3. If conditional: investigate removing the condition
4. State confidence level for each proof path
</completeness_contract>

<structured_output_contract>
End with:
## Fortification Report
For each theorem:
  - PRIMARY PROOF: [sound/repaired/gap-remaining]
  - SECONDARY PROOF: [written/sketched/identified/blocked]
  - TECHNIQUE: [what alternative method]
  - CONDITION STATUS: [unconditional/conditional-on-X/research-programme-Y]
  - CONFIDENCE: [high/medium/low]
</structured_output_contract>


HEAL the CY-to-chiral functor chapter.

TARGET: ~/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex

After the pi_3(BU) correction and kappa_ch domain fix:
1. Verify CY-A stated as proved for d=2 only
2. Verify d=3 claims properly conditioned
3. Verify kappa_ch = chi(S)/2 applied only to local surfaces Tot(K_S -> S)
4. Verify pi_3(BU) = 0 (not Z) in any remaining homotopy arguments
5. Verify the bar-Euler/Borcherds connection doesn't overclaim
6. Add cross-references to the Vol I rectified theorems

Fix any remaining violations.
mcp startup: no servers

thinking
**Fortifying main results**

I'm considering whether I need to strengthen the main results and theorems in this chapter. I should think about adding an alternative proof for the main theorem if that's feasible. It’s important to make all necessary edits and maintain rigor throughout. I believe the main theorem might relate to the CY-to-chiral functor, particularly for dimension d=2, with some conditional remarks for d=3. Time to inspect the chapter more closely.
codex
Using `vol3-beilinson-loop`, `vol3-pre-edit-verification`, and `vol3-cross-volume-propagation` on [chapters/theory/cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex). I’m reading the live chapter, the local dirty surface, and the relevant skill instructions first so I can lock the exact claims and then patch only verified violations.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-cross-volume-propagation/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "git status --short chapters/theory/cy_to_chiral.tex && sed -n '1,260p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
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
 succeeded in 50ms:
---
name: vol3-cross-volume-propagation
description: Use when changing formulas, definitions, theorem statuses, or terminology that may recur across Volumes I, II, and III. Trigger on propagate, cross-volume, grep other volume, update all occurrences, or changes involving kappa, Theta, bar/cobar, CoHA, E_1/E_2, Borcherds products, quantum groups, or center constructions.
---

# Vol III Cross-Volume Propagation

Read `AGENTS.md` first. This skill exists to prevent local fixes from creating global incoherence.

## Sweep

Search all three volumes:

- `~/calabi-yau-quantum-groups`
- `~/chiral-bar-cobar-vol2`
- `~/chiral-bar-cobar`

## Conversion discipline

Before updating a matching statement, verify whether it is actually the same claim in the same convention:
 succeeded in 51ms:
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
 succeeded in 52ms:
\chapter{From CY Categories to Chiral Algebras}
\label{ch:cy-to-chiral}

A Calabi--Yau category has a trace. A chiral algebra has an OPE. The trace is a map $\HH_d(\cC) \to \C$; the OPE is a distribution-valued product on sections over a punctured disc. No formal argument connects them: the trace is finite-dimensional Hochschild data, the OPE is an infinite-dimensional vertex structure on a curve. Volumes~I and~II accept a chiral algebra as given and extract its invariants: bar-cobar adjunction, the modular characteristic $\kappa_{\mathrm{ch}}$, the shadow tower, the five theorems A--D+H. The geometric source of that algebra is left unspecified. Affine Kac--Moody algebras arise from flat connections, Virasoro from reparametrizations; every other chiral algebra in the standard landscape (conifold, Hilbert schemes of K3, resolved $A_n$ singularities, local threefolds with potential) must be supplied by hand. The question is: what functor connects CY categories to chiral algebras, and what structure must it preserve?

The answer requires four constructions, each with a precise structural role. A CY category $\cC$ of dimension $d$ carries a cyclic $\Ainf$-structure, a Connes $B$-operator, and an $\bS^d$-framing on Hochschild homology. None of these are chiral algebras. The Gerstenhaber bracket on $\HH^\bullet(\cC)$ produces a Lie conformal algebra $\mathfrak{L}_\cC$; the factorization envelope on a curve $X$ promotes $\mathfrak{L}_\cC$ to a factorization algebra; the $\bS^d$-framing provides the higher operadic enhancement; and the CY trace determines the quantization. The functor $\Phi \colon \CY_d\text{-}\Cat \to \En\text{-}\mathrm{ChirAlg}$ that results is the central object of this volume. It must preserve three things: the Hochschild data (the bar complex of $\Phi(\cC)$ recovers the cyclic bar complex of $\cC$), the modular characteristic ($\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$), and the operadic level (the $\bS^d$-framing produces an $E_n$-structure, not higher).

At $d = 2$, the functor is unconditional: the $\bS^2$-framing of Kontsevich--Vlassopoulos enhances $\Fact_X(\mathfrak{L}_\cC)$ to an $\Etwo$-chiral algebra, and $\Phi$ is constructed end-to-end. At $d = 3$, a fundamental obstruction intervenes. The native $E_3$-structure on $\HH_\bullet(\cC)$ restricts to \emph{symmetric} braiding under Dunn additivity; the nonsymmetric quantum group braiding that physics demands can only be recovered through the Drinfeld center of the $\Eone$-monoidal representation category. This chapter verifies the $d = 3$ chain end-to-end for $\C^3$, where both sides are independently known (CoHA$(\C^3) \simeq Y^+(\widehat{\fgl}_1)$ on the CY side, $\cW_{1+\infty}$ at $c=1$ on the chiral side), and sets up the quiver-chart gluing that assembles the global $\Eone$-chiral algebra from local CoHA data via the factorization envelope.

% ============================================================
\section{The cyclic-to-chiral passage}
\label{sec:cyclic-to-chiral}
% ============================================================

A CY category $\cC$ of dimension $d$ carries a cyclic $\Ainf$-structure (Chapter~\ref{ch:cyclic-ainf}). The primary invariant is the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ with its $\bS^d$-framing. The passage to chiral algebras decomposes into four steps; each consumes a specific piece of the CY data and produces a specific algebraic structure:

\begin{enumerate}[label=\textbf{Step \arabic*.}]
 \item \textbf{Cyclic $\Ainf \to$ Lie conformal algebra.} The Gerstenhaber bracket on $\HH^\bullet(\cC)$ is a graded Lie bracket of degree $-1$. The CY pairing (the nondegenerate trace $\HH_d(\cC) \to \C$) promotes this to a Lie conformal algebra $\mathfrak{L}_\cC$: the bracket becomes a $\lambda$-bracket, and the pairing becomes the invariant bilinear form. This step consumes the $\Ainf$-structure and the CY trace; it produces the ``current algebra'' of $\cC$.
 \item \textbf{Lie conformal algebra $\to$ factorization envelope.} The factorization envelope construction produces a factorization algebra $\Fact_X(\mathfrak{L}_\cC)$ on any smooth curve $X$. This step consumes the Lie conformal algebra and the curve; it produces a cosheaf on $\Ran(X)$ whose sections are the OPE data.
 \item \textbf{$\bS^d$-framing $\to$ $E_n$ enhancement.} When $d = 2$, the $\bS^2$-framing of $\HH_\bullet(\cC)$ (Kontsevich--Vlassopoulos) provides an $\Etwo$-algebra structure on the factorization algebra. This step consumes the framing; it produces the operadic enhancement that distinguishes a chiral algebra from a commutative factorization algebra.

thinking
**Searching theorems and issues**

I need to look for theorem labels and issues while inspecting the chapter structure and all theorem-like environments. The user mentioned "fortification agent," but I'll focus on the specific chapter scope. I probably don't need every theorem, just the main results, like those around CY-A. The final Fortification Report says to consider "each theorem in your scope," so I’ll decide which statements are relevant. I'll also check for specific theorem labels and references to concepts like pi_3(BU) and Borcherds as I go.
codex
The chapter is larger than the initial surface around CY-A, so I’m mapping the theorem-like statements and grepping the five failure families directly: `d=2/d=3` status drift, `kappa_ch` domain leakage, `pi_3(BU)`, and any Borcherds/bar-Euler overclaim.
exec
/bin/zsh -lc "sed -n '260,520p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"\\\\begin\\{(theorem|proposition|lemma|corollary|conjecture|remark)\\}|pi_3\\(BU\\)|kappa_\\{\\\\mathrm\\{ch\\}\\}|Borcherds|bar-Euler|chi\\(S\\)/2|Tot\\(|local surfaces|d = 3|CY-A\" chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 51ms:
rg: regex parse error:
    (?:\begin\{(theorem|proposition|lemma|corollary|conjecture|remark)\}|pi_3\(BU\)|kappa_\{\mathrm\{ch\}\}|Borcherds|bar-Euler|chi\(S\)/2|Tot\(|local surfaces|d = 3|CY-A)
                                                                                            ^^
error: unrecognized escape sequence
 succeeded in 51ms:
nonabelian sector equals $4 \times \tfrac{1}{2} = 2$ (each $\mathfrak{so}_4
\cong \mathfrak{su}_2 \oplus \mathfrak{su}_2$ at level~$1$ contributes
$\kappa_{\mathrm{ch}} = 1/2$).
\end{proposition}

\begin{proof}
Step~1 is the Ayala--Francis K\"unneth theorem for factorization homology:
$\int_{(S^1)^n} \cF \simeq \cF \otimes H^*((S^1)^n)$ for an $\Einf$-algebra
$\cF$, applied with $n = 4$ and $\cF = \cH_1$.
Step~2 is elementary representation theory of $\bZ_2$ acting on exterior
powers: $\iota^*(\alpha_i) = -\alpha_i$ for each degree-$1$ generator
$\alpha_i \in H^1(T^4)$, so $\iota^*|_{H^k} = (-1)^k$ and the invariant
subspace is $H^{\mathrm{even}}(T^4) = \bC^8$.
Step~3 is classical orbifold VOA theory (Dixon--Harvey--Vafa--Witten):
the $\bZ_2$-twisted ground state of a free boson on $\bC$ has conformal
weight $h = 1/16$ per real boson, hence $h = 1/4$ per complex dimension
and $h = 1/2$ for the two complex tangent directions at each $A_1$ fixed
point.  The twisted-sector characters are standard.
Step~4 assembles untwisted and twisted sectors via the orbifold VOA
construction.  The character follows by direct computation.  The value
exec
/bin/zsh -lc 'git diff -- chapters/theory/cy_to_chiral.tex && git status --short' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
 M compute/lib/chiral_coproduct_spin2_engine.py
 M compute/lib/chiral_coproduct_universal_engine.py
 M compute/lib/conifold_e1_full_chain.py
 M compute/lib/sl2_serre_engine.py
 M compute/tests/test_chiral_coproduct_universal.py
 M compute/tests/test_sl2_serre_engine.py
 M main.log
 M out/calabi_yau_quantum_groups.pdf
 M out/working_notes.pdf
?? compute/tests/test_conifold_e1_factored_transfer.py

thinking
**Continuing file analysis**

I need to continue working on the file and search for patterns that might include pi_3(BU) and local surfaces related to kappa. Using the proper regex with fixed strings or escaped characters feels crucial. I could consider using `rg -n` with multiple patterns for simplicity. It's also important to inspect specific segments around pi_3(BU). I should keep in mind that the current dirty surface isn't relevant and plan for updates once I've gathered enough context. Let's push through to the end and do that search.
codex
The working tree is dirty in unrelated compute/build files, so I’ll leave those untouched. Next I’m finishing the chapter scan and locating the exact lines where `pi_3(BU)`, `kappa_ch` on local surfaces, and Borcherds/bar-Euler language still appear.
exec
/bin/zsh -lc "sed -n '520,1040p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\end{proof}

\begin{remark}[Smooth vs singular: locality of the quantization]
\label{rem:smooth-singular-locality}
The distinction between smooth and singular CY$_3$ is categorical:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{lll}
 \toprule
 \textbf{CY$_3$} & \textbf{Quantization} & \textbf{Algebraic type} \\
 \midrule
 Smooth ($\C^3$, quintic, $K3 \times E$) & Vertex algebra (local) & $\Eone$-chiral ($\Etwo$ via Drinfeld center) \\
 Singular (conifold) & Associative algebra (nonlocal) & $\Eone$-chiral \\
 \bottomrule
\end{tabular}
\end{center}
Smoothness is not a matter of convention: the factorization envelope requires local data (the polyvector fields form a cosheaf whose sections over small discs control the OPE), and singularities obstruct the local-to-global passage. At a singularity, the category $\mathrm{Perf}(X)$ acquires compact objects that do not extend to a neighbourhood, and the factorization structure degenerates from $\Etwo$ to $\Eone$.

\noindent\textit{Verification}: 71 tests in \texttt{cy3\_hochschild.py} (testing smooth vs singular HH data).
\end{remark}
exec
/bin/zsh -lc 'rg -n -F "pi_3(BU)" chapters/theory/cy_to_chiral.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -e 'kappa_\\\\{\\\\mathrm\\\\{ch\\\\}\\\\}' -e 'Borcherds' -e 'bar-Euler' -e 'chi\\(S\\)/2' -e 'Tot\\(' -e 'local surface' -e 'd = 3' -e 'CY-A' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 52ms:
rg: regex parse error:
    (?:kappa_\\{\\mathrm\\{ch\\}\\})|(?:Borcherds)|(?:bar-Euler)|(?:chi\(S\)/2)|(?:Tot\()|(?:local surface)|(?:d = 3)|(?:CY-A)
                ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
556: \item \emph{Bott periodicity path.} The complex structure gives a reduction $\mathrm{GL}(n, \C) \to U(n)$. By Bott periodicity, $\pi_3(BU) = 0$ (the homotopy groups of $BU$ are $\pi_{2k}(BU) = \Z$, $\pi_{2k+1}(BU) = 0$). Since $\pi_3$ is odd, the obstruction vanishes.
578:For the Bott periodicity path: the Bott periodicity theorem gives $\pi_k(BU) \cong \pi_k(BU(n))$ for $n$ large, with $\pi_{2k}(BU) = \Z$ and $\pi_{2k+1}(BU) = 0$. Since $3$ is odd, $\pi_3(BU) = 0$.
952:The topological $\bS^3$-framing obstruction vanishes: $\pi_3(B\Sp(2m)) = \pi_2(\Sp(2m)) = 0$ for all $m \geq 1$ (the CY$_3$ pairing reduces the structure group to $\Sp(2m)$, and all compact simply-connected simple Lie groups have vanishing $\pi_2$; independently, $\pi_3(BU) = 0$ by Bott periodicity, since $3$ is odd).
1476: \item \textbf{Topological obstruction} $\cO_2^{\mathrm{top}} \in \pi_3(BU)$. For CY$_3$: $\pi_3(BU) = 0$ (Bott periodicity), so $\cO_2^{\mathrm{top}} = 0$ \emph{universally}. The obstruction to $\Etwo$ is not topological. (Contrast: for CY$_2$, $\pi_2(BU) = \Z$ \emph{provides} the braiding parameter.)
1487:The topological component follows from Bott periodicity: $\pi_k(BU) = \Z$ for $k$ even, $0$ for $k$ odd, giving $\pi_3(BU) = 0$. The structural component is the rank of the antisymmetric part of the Euler form matrix $(\chi(\gamma_i, \gamma_j))_{i,j}$; for a CY$_3$ quiver with potential $(Q, W)$, this equals $\rk(B^{\mathrm{anti}})$ where $B^{\mathrm{anti}}_{ij} = \dim \Ext^1(S_i, S_j) - \dim \Ext^1(S_j, S_i)$ (the difference of arrow counts, which is nonzero precisely because CY$_3$ Serre duality $\Ext^k(S_i, S_j) \cong \Ext^{3-k}(S_j, S_i)^*$ is \emph{antisymmetric} for $d = 3$ odd). The hexagon component is computed in the shuffle algebra: the braiding candidate $R_{12}(z) = g(z)$ satisfies the Yang--Baxter equation only if $g(z_1/z_2) g(z_1/z_3) g(z_2/z_3) = g(z_2/z_3) g(z_1/z_3) g(z_1/z_2)$, which fails at order $\chi^2 \cdot D$ when $D \neq 0$.
1843:$\pi_3(B\Sp(2m)) = 0$ for all $m \geq 1$ (symplectic path); independently, $\pi_3(BU) = 0$ (Bott periodicity). The topological component of the obstruction is zero universally (Theorem~\textup{\ref{thm:s3-framing-vanishes}}). This removes condition~(a) of hypothesis~\ref{hyp:framing}; only the chain-level BV-compatible trivialization remains.
1905: $\bS^3$-framing obstruction & \textbf{Topol.\ trivial} & $\pi_3(B\Sp) = \pi_3(BU) = 0$ (Thm.~\ref{thm:s3-framing-vanishes}) \\

thinking
**Planning theorem updates**

I need to focus on rectifying Volume I theorems related to bar-cobar and shadow tower. I'll search in the current repository for cross references to Volume I theorems, utilizing labels. I could also explore other volume repositories if they're accessible. It's important to inspect relevant labels in the current file too. Let’s draft a plan and use the update_plan tool to outline the necessary steps for this process.
Plan update
Locked the target file and initial risk surface. Next I’m auditing the chapter against the six requested invariants, then patching only verified violations, then running the narrowest build/grep checks.
  → Audit cy_to_chiral.tex for d=2/d=3 status honesty, kappa_ch domain discipline, pi_3(BU), and Borcherds/bar-Euler overclaiming
  • Identify and verify relevant Vol I theorem labels for explicit cross-references needed in this chapter
  • Write scoped manuscript fixes, including fortifying proofs/remarks where the chapter currently overclaims or lacks redundancy
  • Run targeted verification on the edited chapter and re-audit the modified surface

thinking
**Continuing the audit**

I need to continue the audit by searching for kappa local surfaces and Borcherds. Maybe I should use `rg -n -F` separately for that. I think it’s also important to inspect lines around 1450, so I’ll keep an eye out for that as well. Alright, time to run the search and see what I can find! Let’s see how it goes.
codex
I’ve got the first pass findings: the chapter already uses `pi_3(BU)=0` in several places, but there are still later sections that need rereading because they repackage the same obstruction story and can drift semantically. I’m now checking the lower theorem/proposition surfaces and the `kappa_ch` local-surface statements, since that’s where domain leakage typically hides.
exec
/bin/zsh -lc "rg -n -F 'kappa_{\\mathrm{ch}}' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1820,1920p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1440,1510p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\subsubsection{The punchline: why $d = 3$ gives $\Eone$}
\label{subsubsec:punchline-d3}

We can now state the precise sense in which the CY dimension $d = 3$ forces the $\Eone$ structure.

The CY$_3$ cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ carries an $\bS^3$-framing (Chapter~\ref{ch:cyclic-ainf}). The homotopy type of $\bS^3$ determines the $E_n$-level of the resulting chiral algebra through the configuration space $\Conf_2(\R^{d-2})$:
\begin{itemize}
 \item The framing gives an action of $\SO(d-2)$ on $\mathrm{CC}_\bullet(\cC)$, and the $E_{d-2}$-structure is extracted from the little $(d-2)$-cubes operad.
 \item For $d = 3$: $d - 2 = 1$, $\Conf_2(\R^1) = \{(x_1, x_2) \in \R^2 : x_1 \neq x_2\}$ has two connected components (ordered: $x_1 < x_2$ or $x_1 > x_2$) and is homotopy equivalent to $\bS^0 = \{+, -\}$. This is the $\Eone$ operad: the choice of a connected component is the choice of an ordering, giving an \emph{associative} multiplication. There is no braiding because $\pi_1(\Conf_2(\R^1)) = 0$ (the two components are contractible).
 \item For $d = 2$: $d - 2 = 0$ gives $E_0$, but the correct interpretation uses the $\bS^2$-framing directly: the framed little $2$-discs give $\Etwo$, and $\pi_1(\Conf_2(\R^2)) = \Z$ provides the braiding.
 \item For $d = 4$: $d - 2 = 2$, $\pi_1(\Conf_2(\R^2)) = \Z$, and the CY$_4$ algebra should carry an $\Etwo$ braiding.
\end{itemize}

The descent theorem (Theorem~\ref{thm:e1-descent-degeneration}) translates this homotopy-theoretic fact into a concrete computational advantage: the quiver-chart atlas of a CY$_3$ category glues via a \emph{single system of transition maps} (the wall-crossing automorphisms $K_\gamma$), with no higher coherence data. The global $\Eone$-chiral algebra
\[
 A_\cC \;=\; \operatorname{hocolim}_{\Stab} \CoHA(Q_\alpha, W_\alpha)
\]
is assembled cleanly from pairwise gluing data, and the hocolim works precisely because $\Eone$ descent is unobstructed.

This is the reason the hocolim construction succeeds for CY$_3$ but cannot directly produce an $\Etwo$-algebra: the chart gluing is $1$-categorical, and the braiding lives in the \emph{Drinfeld center} of the representation category, not in the algebra itself (Conjecture~\ref{conj:e1-chart-gluing}).
 succeeded in 52ms:
\begin{itemize}
 \item Smooth proper CY$_3$ categories $D^b(\Coh(X))$ for smooth projective CY$_3$ varieties $X$ (quintic, $K3 \times E$, complete intersections).
 \item Toric CY$_3$ categories with $T^3$-equivariant $\Omega$-deformation ($\C^3$, resolved conifold, local $\bP^2$, local $\bP^1 \times \bP^1$); for these, the CoHA construction replaces the factorization envelope, and hypothesis~\ref{hyp:framing} is satisfied by holomorphic Chern--Simons.
 \item Ginzburg dg algebras $\mathrm{Gin}(Q, W)$ for quivers with CY$_3$ potential; each such algebra provides a single quiver chart (Definition~\textup{\ref{def:quiver-chart}}).
 \item Generalized CY$_3$ inputs with torsion canonical bundle (Enriques $\times E$), provided the orbifold extension of $\Phi$ is available (Conjecture~\textup{\ref{conj:phi-enriques-z2-orbifold}}).
\end{itemize}
The conjecture does NOT apply to singular CY$_3$ categories (smoothness is essential for the factorization-envelope step) or to non-proper inputs (properness controls the finiteness of the generating space).
\end{conjecture}


\begin{remark}[Evidence and obstacle catalogue for Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}]
\label{rem:cy-to-chiral-d3-evidence}

The following numbered items collect all evidence for and against the conjecture, with explicit status tags. Evidence items are labelled \textbf{E1}--\textbf{E10}; obstacle items are labelled \textbf{O1}--\textbf{O5}.

\medskip\noindent\textbf{Evidence.}

\begin{enumerate}[label=\textbf{E\arabic*.}, leftmargin=3em]

\item \textbf{$\C^3$ end-to-end verification.} \textsc{[Proved]}
 succeeded in 52ms:
4:A Calabi--Yau category has a trace. A chiral algebra has an OPE. The trace is a map $\HH_d(\cC) \to \C$; the OPE is a distribution-valued product on sections over a punctured disc. No formal argument connects them: the trace is finite-dimensional Hochschild data, the OPE is an infinite-dimensional vertex structure on a curve. Volumes~I and~II accept a chiral algebra as given and extract its invariants: bar-cobar adjunction, the modular characteristic $\kappa_{\mathrm{ch}}$, the shadow tower, the five theorems A--D+H. The geometric source of that algebra is left unspecified. Affine Kac--Moody algebras arise from flat connections, Virasoro from reparametrizations; every other chiral algebra in the standard landscape (conifold, Hilbert schemes of K3, resolved $A_n$ singularities, local threefolds with potential) must be supplied by hand. The question is: what functor connects CY categories to chiral algebras, and what structure must it preserve?
6:The answer requires four constructions, each with a precise structural role. A CY category $\cC$ of dimension $d$ carries a cyclic $\Ainf$-structure, a Connes $B$-operator, and an $\bS^d$-framing on Hochschild homology. None of these are chiral algebras. The Gerstenhaber bracket on $\HH^\bullet(\cC)$ produces a Lie conformal algebra $\mathfrak{L}_\cC$; the factorization envelope on a curve $X$ promotes $\mathfrak{L}_\cC$ to a factorization algebra; the $\bS^d$-framing provides the higher operadic enhancement; and the CY trace determines the quantization. The functor $\Phi \colon \CY_d\text{-}\Cat \to \En\text{-}\mathrm{ChirAlg}$ that results is the central object of this volume. It must preserve three things: the Hochschild data (the bar complex of $\Phi(\cC)$ recovers the cyclic bar complex of $\cC$), the modular characteristic ($\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$), and the operadic level (the $\bS^d$-framing produces an $E_n$-structure, not higher).
57: \kappa_{\mathrm{ch}}(A_\cC) \;=\; \chi^{\CY}(\cC) \;\stackrel{\mathrm{def}}{=}\; \sum_{i} (-1)^i \dim \HH_i(\cC).
62:The generating space of $A_\cC$ is $\HH^{\bullet+1}(\cC)$, and $\kappa_{\mathrm{ch}}$ equals the supertrace of the identity on this generating space, which is $\chi^{\CY}(\cC)$. The quantization step in the construction of $\Phi$ (CY-A, Step~4) preserves $\kappa_{\mathrm{ch}}$ at $d = 2$: the Serre duality $\mathbb{S}_\cC \simeq [2]$ forces the holomorphic anomaly to vanish, so no quantum correction shifts the supertrace. This is verified computationally for K3 surfaces ($\kappa_{\mathrm{ch}} = 2 = \chi(\cO_{\mathrm{K3}})$) and abelian surfaces ($\kappa_{\mathrm{ch}} = 0 = \chi(\cO_A)$).
70: \kappa_{\mathrm{ch}}(A_\cC) \;=\; \chi^{\CY}(\cC).
76:At $d = 2$, the identification is proved (Proposition~\textup{\ref{prop:cy-kappa-d2}}). At $d = 3$, the conjecture is verified for $\C^3$ where both sides are independently computable ($\kappa_{\mathrm{ch}} = \kappa_{\mathrm{cat}} = 1$; see Proposition~\textup{\ref{prop:categorical-euler}}). The obstruction to extending the $d = 2$ proof is that the $d = 3$ quantization step may introduce corrections: Serre duality $\mathbb{S}_\cC \simeq [3]$ no longer kills the one-loop anomaly by parity. The $d = 3$ functor itself is conjectural beyond $\C^3$.
82:An Enriques surface $S$ is not a strict $\CY_2$ input in the sense of Theorem~\textup{\ref{thm:cy-to-chiral}}, because $\omega_S$ is nontrivial $2$-torsion and the Serre functor on $D^b(\Coh(S))$ is $(-)\otimes \omega_S[2]$, not $[2]$. It is still the first orbifold test case next to the K3 example of Remark~\textup{\ref{rem:cy-kappa-evidence}}. Let $\pi \colon X \to S$ be the universal cover, where $X$ is a K3 surface and the deck involution acts freely. Then $\chi(\cO_X) = 2$ and $\chi(\cO_S) = 1$, so the K3 value $\kappa_{\mathrm{ch}} = 2$ suggests the orbifold value $\kappa_{\mathrm{ch}} = 1$ if $\Phi$ extends to this torsion-canonical quotient surface.
90: \kappa_{\mathrm{ch}}(A^G) \,=\, \frac{\kappa_{\mathrm{ch}}(A)}{|G|},
134: \item $\kappa_{\mathrm{ch}}(S) = 1 = \chi(\cO_S)$, half the K3 value $\kappa_{\mathrm{ch}}(X) = 2$.
136: \item $\kappa_{\mathrm{cat}}(S \times E) = \chi^{\CY}(D^b(\Coh(S \times E)))$, the categorical Euler characteristic. By additivity (Proposition~\textup{\ref{prop:categorical-euler}}), $\kappa_{\mathrm{cat}}(S \times E) = \kappa_{\mathrm{ch}}(S) + \kappa_{\mathrm{ch}}(E) = 1 + 1 = 2$.
212:and $\kappa_{\mathrm{ch}}(\cH_8) = 0$ (abelian torus, $\chi(\cO_{T^4}) = 0$;
248:characteristic is $\kappa_{\mathrm{ch}}(\cA^{\mathrm{orb}}) = 2$, already matching
256:$\kappa_{\mathrm{ch}}$ from the torus value $0$ to the K3 value $2$: specifically,
259:Section~\ref{sec:k3e-five-routes}), and $\kappa_{\mathrm{ch}}$ of this
262:$\kappa_{\mathrm{ch}} = 1/2$).
280:$\kappa_{\mathrm{ch}}(\cA^{\mathrm{orb}}) = 2$ is computed as the supertrace on
330:$\prod_{n \geq 1}(1 - q^n)^{-24}$ and $\kappa_{\mathrm{ch}} = 2 = \chi(\cO_{K3})$.
398:At $d = 2$, the functor $\Phi$ is now in hand (Theorem~\ref{thm:cy-to-chiral}), and $\kappa_{\mathrm{ch}}(\Phi(\cC)) = \chi^{\CY}(\cC)$ is proved (Proposition~\ref{prop:cy-kappa-d2}; the Serre duality argument kills the one-loop correction). At $d = 3$, Step~3 of the cyclic-to-chiral passage breaks: the $\bS^3$-framing produces symmetric braiding under Dunn restriction, and symmetry is the wrong answer. Physics demands nonsymmetric braiding (the Yang $R$-matrix, the Yangian coproduct), and the only known route to it passes through the Drinfeld center of the $\Eone$-monoidal representation category. The remainder of this chapter develops the $d = 3$ programme, beginning with the one case where both sides are independently known.
558:The chain-level BV obstruction $\kappa_{\mathrm{ch}} \cdot [\Omega_3]$ is trivializable via holomorphic Chern--Simons (Witten~1992, Costello--Li~2016): the functional $\mathrm{CS}(\bar{\partial} + A) = \int_X \Omega \wedge \mathrm{tr}(A \wedge \bar{\partial}A + \tfrac{2}{3} A \wedge A \wedge A)$ provides the contracting homotopy.
587:Assuming Conjecture~\textup{\ref{conj:cy-to-chiral-d3}} is formulated with symplectic structure group (i.e., the $d = 3$ CY-to-chiral functor targets a CY$_3$ chiral algebra whose obstruction theory sits in $\pi_3(B\Sp(2m))$), the topological component of that obstruction vanishes. The remaining chain-level construction of the trivialization of $\kappa_{\mathrm{ch}} \cdot [\Omega_3]$ is known to exist by holomorphic Chern--Simons, but its compatibility with the full $\Ainf$-structure is part of CY-A$_3$ itself and remains conjectural. For the toric CY$_3$ verified in compute ($\C^3$, conifold, local $\bP^2$, local $\bP^1 \times \bP^1$, $K3 \times E$), the $\Eone \to \Etwo$ enhancement obstruction vanishes at the level of the explicit CoHA construction.
exec
/bin/zsh -lc "rg -n -F 'Borcherds' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'bar-Euler' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'chi(S)/2' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'local surface' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Tot(' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 succeeded in 51ms:
92:the chiral shadow of the classical formula $\chi(\cO_S) = \chi(\cO_X)/|G|$ for a free finite quotient. In the Vol~I Igusa normalization, this same orbifold picture suggests replacing the K3 lift $\Phi_{10}$ by a $\mathbb{Z}/2$-twisted lift of weight $5$ on the quotient side. That weight drop gives heuristic evidence for $\kappa_{\mathrm{BKM}}$ halving on the Borcherds side, even though the precise Enriques automorphic normalization is a separate question.
94:Turning this into a theorem requires an orbifold extension of the functor $\Phi$, equivariant descent for factorization envelopes, and the twisted Borcherds-lift technology needed to compare the quotient with its K3 cover.
135: \item $\kappa_{\mathrm{BKM}}(S \times E) = 4$, the weight of the Allcock Borcherds product on $O(2, 10)$. This is verified computationally by \texttt{enriques\_shadow.py} (72 tests; see Remark~\textup{\ref{rem:enriques-kappa-anomaly}} in the bar-cobar bridge chapter).
138:The ratio $\kappa_{\mathrm{BKM}}(X \times E) / \kappa_{\mathrm{BKM}}(S \times E) = 5/4$ (not $2$) reflects the fact that $\kappa_{\mathrm{BKM}}$ is the automorphic weight, which is sensitive to the full BPS spectrum across the fiber and not simply the $|G|$-fold quotient of the scalar invariant. The discrepancy $5/4 \neq 2$ is the \emph{Enriques $\kappa_{\mathrm{BKM}}$-anomaly}: the BKM weight does not halve under the $\bZ/2$ quotient because the Borcherds product on $O(2, 10)$ is not the restriction of the Igusa cusp form on $O(2, 18)$ but rather an independent automorphic form (the Allcock product) whose weight is determined by the Enriques lattice.
146: \item The K3 lattice is $\Lambda_{\mathrm{K3}} = U^3 \oplus E_8(-1)^2$, of rank $22$ and signature $(3, 19)$. The BKM algebra for $\mathrm{K3} \times E$ is constructed via the Borcherds lift on $O(2, 18)$ (the orthogonal complement of a hyperbolic plane in $\Lambda_{\mathrm{K3}} \oplus U$), and $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$.
147: \item The Enriques lattice is $\Lambda_{\mathrm{Enr}} = U \oplus E_8(-1)$, of rank $10$ and signature $(1, 9)$. The involution $\iota$ acts on $H^2(X, \bZ)$ with invariant sublattice $U(2) \oplus E_8(-2)$ (the $\iota$-invariant part of $\Lambda_{\mathrm{K3}}$, rescaled by the index-$2$ inclusion). The BKM algebra for $\mathrm{Enr} \times E$ is constructed via the Borcherds lift on $O(2, 10)$ (from $\Lambda_{\mathrm{Enr}} \oplus U$), and $\kappa_{\mathrm{BKM}} = 4$ (the Allcock product weight).
159: \item The \emph{Allcock Borcherds product} is an automorphic form of weight $4$ on $O(2, 10)$ with known divisor (the Heegner divisors of norm $-2$ vectors in $\Lambda_{\mathrm{Enr}} \oplus U$). Its square root (a form of weight $2$ on a double cover) is related to the Enriques period map.
160: \item Gritsenko and Nikulin constructed a ``Enriques modular form'' of weight $4$ on $O(2, 10)$ using a quasi-pullback of the Borcherds form $\Phi_{12}$ on $O(2, 26)$. This is the same object as the Allcock product, identified through different techniques.
1723:The CY-to-chiral functor at $d = 3$ is not yet constructed for $K3 \times E$ (Conjecture~\ref{conj:cy-to-chiral-d3}). The shadow data is read from two sources: $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$; Proposition~\ref{prop:categorical-euler}), and $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)/1$ from the Borcherds lift weight formula. The genus-$1$ shadow $F_1 = \kappa_{\mathrm{BKM}}/24 = 5/24$ matches the DT genus-$1$ free energy. The full DT partition function $Z_{\DT}(K3 \times E) = C/\Delta_5^2$ involves the Igusa cusp form, whose Borcherds product formula $\Delta_5 = p \prod (1-p^n q^l r^m)^{f(4nm - l^2)}$ is a three-variable generalisation of the bar Euler product (Chapter~\ref{ch:k3-times-e}). The passage from the scalar shadow to the full $\Delta_5$ requires the BKM root system, which encodes all BPS states across all charge lattice directions.
1770:\noindent Three remarks on the table entries. First, $K3 \times E$ does not have a quiver atlas in the strict sense of Definition~\ref{def:quiver-chart-atlas}: the derived category $D^b(\Coh(K3 \times E))$ does not admit a single tilting generator, and the fibration structure requires a different gluing mechanism (the relative Fourier--Mukai, see Chapter~\ref{ch:k3-times-e}). The table records $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$, Proposition~\ref{prop:categorical-euler}); the distinct Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$. Second, the quintic has $|I| = 2$ charts: one at large volume (a quiver chart from the Beilinson collection restricted to $X$) and one at the Gepner point (a matrix factorization category $\MF(W_{\mathrm{Fermat}})$, which is NOT a quiver chart; see Remark~\ref{rem:gepner-lv-dichotomy}). Third, the shadow class and depth $r_{\mathrm{max}}$ refer to the Heisenberg truncation ($s = 1$ channel). At the full spin tower, the classification may differ (Remark~\ref{rem:c3-per-channel}).
1977:$^\dagger$The $K3 \times E$ entry records $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\ref{prop:categorical-euler}: $\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1$). The Borcherds automorphic weight is $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, a distinct invariant.}
1995:For K3-fibered CY$_3$, the infinite tower of BPS bound states across fibers contributes additional genus-$1$ data beyond the one-loop determinant. For $K3 \times E$: the $24$ free bosons from the K3 fiber give $\kappa_{\mathrm{fiber}} = 24$, but the sewing along $E$ via the DMVV formula introduces imaginary root contributions that produce $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$ (the weight of the Igusa cusp form). The ``lost'' $19$ units ($24 - 5 = 19$) are absorbed by the Borcherds product structure.
2005:The categorical Euler characteristic accounts for the full BPS spectrum (all charges), not just the massless modes that contribute to $\chi_{\mathrm{top}}$. For K3-fibered CY$_3$, the infinite tower of bound states across fibers contributes to $\chi^{\CY}$ via the Borcherds denominator weight.
2010: \item DMVV exponent: the Borcherds lift weight formula gives $c(0)/2 = 10/2 = 5$.
2103: \item For K3-fibered CY$_3$: $\kappa_{\mathrm{ch}} \neq \chi_{\mathrm{top}}/24$ (Theorem~\ref{thm:chi-neq-kappa}), and the shadow connection carries fiber-global mixing data beyond the BCOV framework. The discrepancy $\kappa_{\mathrm{ch}} - \chi_{\mathrm{top}}/24$ measures the BPS bound-state contribution from the K3 fiber, absorbed by the Borcherds product structure.
2116:where the BKM root system (for K3-fibered CY$_3$) supplies the root lattice structure and the Borcherds denominator formula controls the bar Euler product.
 exited 1 in 51ms:

 succeeded in 51ms:
2133:\begin{theorem}[Curved chiral algebra from non-CY local surfaces]
 exited 1 in 51ms:

codex
I’ve isolated one concrete leakage already: the chapter still has a local-surface theorem in the lower section, which is where `\chi_{\mathrm{top}}(S)/2` and `\mathrm{Tot}(K_S)` discipline has to be stated explicitly. I’m reading that block and the nearby Borcherds/shadow language now, because those are the likeliest remaining overclaims.
exec
/bin/zsh -lc "sed -n '2128,2205p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1708,1735p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\begin{definition}[CY defect]
\label{def:cy-defect}
For $E \to C$ a rank-$2$ bundle, the \emph{CY defect} is $\delta := \deg(\det E) - \deg(K_C) = \deg(\det E) - (2g - 2)$. The CY condition is $\delta = 0$.
\end{definition}

\begin{theorem}[Curved chiral algebra from non-CY local surfaces]
\label{thm:curved-chiral-non-cy}
\ClaimStatusProvedHere{}
When $\delta \neq 0$, the chiral algebra $A_E$ is curved: the curvature element $m_0 = \delta \cdot \omega_C$ is nonzero, the bar complex satisfies $d^2 = [m_0, -]$, and the shadow obstruction tower satisfies the inhomogeneous MC equation
\[
 D \cdot \Theta + \tfrac{1}{2}[\Theta, \Theta] = m_0.
\]
The curved modular characteristic is
\begin{equation}
\label{eq:kappa-curved}
 \kappa_{\mathrm{ch}}^{\mathrm{crv}} = \kappa_{\mathrm{ch}} + \frac{\delta^2 \, \chi(C)}{24},
\end{equation}
where $\kappa_{\mathrm{ch}}$ is the uncurved value at $\delta = 0$. The correction is quadratic in~$\delta$, linear in~$\chi(C)$, and vanishes identically on the torus ($g = 1$, $\chi = 0$).

\noindent\textit{Verification}: 119 tests in \texttt{curved\_shadow\_non\_cy.py}; 130 tests in \texttt{rank2\_bundle\_chiral.py}.
 succeeded in 52ms:
\end{table}

\begin{remark}[Detailed evidence for Conjecture~\textup{\ref{conj:shadow-bps-dt}}]
\label{rem:shadow-bps-evidence-detail}
The four cases in Table~\ref{tab:shadow-bps-evidence} have different logical dependencies.

\begin{enumerate}[label=\textup{(\alph*)}]

\item \textbf{$\C^3$: proved at the motivic level.}
The CY-to-chiral functor produces $A_{\C^3} = \cW_{1+\infty} = H_1$ (at the self-dual point). The bar Euler product is $1/M(q) = \prod (1-q^n)^n$ (Proposition~\ref{prop:c3-bar-euler}), inverting the MacMahon function. The bar cohomology gives $\Omega(n) = n = \Omega_{\DT}(n)$ at all degrees ($115$ tests). The motivic comparison holds: $B^{\Eone}(H_1)$ as a graded $\Eone$-coalgebra matches the motivic DT coalgebra of $\C^3$ via the Schiffmann--Vasserot identification $\CoHA(\C^3) = Y^+(\widehat{\fgl}_1)$.

\item \textbf{Toric CY$_3$: proved via the CoHA.}
For any smooth toric CY$_3$ $X_\Sigma$ with McKay quiver atlas $(Q_\alpha, W_\alpha)_{\alpha \in I}$, the toric chart gluing theorem (Theorem~\ref{thm:toric-chart-gluing}) assembles the global $\Eone$-chiral algebra $A_{X_\Sigma}$. The $\CoHA$ of $(Q_\alpha, W_\alpha)$ is the positive half of the quantum vertex chiral group $G(Q_\alpha, W_\alpha)$ (Kontsevich--Soibelman, Schiffmann--Vasserot, Davison). The bar complex of $A_{X_\Sigma}$ recovers the DT moduli via the CoHA-bar identification. The correspondence holds at the motivic level because the CoHA multiplication IS the bar differential, and the CoHA Hilbert series IS the bar Euler characteristic.

\item \textbf{$K3 \times E$: observational at genus~$1$, motivic level requires $\Phi_3$.}
The CY-to-chiral functor at $d = 3$ is not yet constructed for $K3 \times E$ (Conjecture~\ref{conj:cy-to-chiral-d3}). The shadow data is read from two sources: $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$; Proposition~\ref{prop:categorical-euler}), and $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)/1$ from the Borcherds lift weight formula. The genus-$1$ shadow $F_1 = \kappa_{\mathrm{BKM}}/24 = 5/24$ matches the DT genus-$1$ free energy. The full DT partition function $Z_{\DT}(K3 \times E) = C/\Delta_5^2$ involves the Igusa cusp form, whose Borcherds product formula $\Delta_5 = p \prod (1-p^n q^l r^m)^{f(4nm - l^2)}$ is a three-variable generalisation of the bar Euler product (Chapter~\ref{ch:k3-times-e}). The passage from the scalar shadow to the full $\Delta_5$ requires the BKM root system, which encodes all BPS states across all charge lattice directions.

\item \textbf{Quintic: conditional on $\Phi_3$.}
The quintic has $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}/24 = -25/3$ (this is one of the cases where $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}/24$ holds; Theorem~\ref{thm:chi-neq-kappa}). The genus-$1$ DT free energy $F_1 = -25/72$ matches. The BCOV holomorphic anomaly equation (Theorem~\ref{thm:hae-mc-structural}) provides the higher-genus comparison, but the existence of $A_X$ as an $\Eone$-chiral algebra for the quintic depends on the CY-to-chiral functor at $d = 3$.

exec
/bin/zsh -lc "sed -n '2100,2122p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
Two regimes illustrate the scope and limitations of the identification:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item For CY$_3$ with $h^{1,0} = 0$ (rigid CICYs): $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}/24$, and the BCOV propagator is the genus-$1$ shadow. The shadow connection $\nabla^{\mathrm{sh}} = d - Q'_L/(2Q_L)\, dt$ specialises to the Picard--Fuchs connection on the $B$-model moduli space.
 \item For K3-fibered CY$_3$: $\kappa_{\mathrm{ch}} \neq \chi_{\mathrm{top}}/24$ (Theorem~\ref{thm:chi-neq-kappa}), and the shadow connection carries fiber-global mixing data beyond the BCOV framework. The discrepancy $\kappa_{\mathrm{ch}} - \chi_{\mathrm{top}}/24$ measures the BPS bound-state contribution from the K3 fiber, absorbed by the Borcherds product structure.
\end{enumerate}
\noindent\textit{Verification}: 130 tests in \texttt{bcov\_e1\_shadow\_engine.py}, including 10 tests quantifying the K3-fibered discrepancy.
\end{remark}


\subsection{The completed modular Koszul datum for CY$_3$}
\label{subsec:cross-vol-mkd}

The eight-fold completed modular Koszul datum $\Pi^{\mathrm{oc}}_X(A)$ of Vol~I specializes to the CY$_3$ setting as:
\[
 \Pi^{\mathrm{oc}}_{X}(A_{X_3}) = \bigl(\cF_X(A), \overline{B}_X(A), \Theta_A, L_A, (V^{\mathrm{br}}, T^{\mathrm{br}}), R^{\mathrm{mod}}_4, \cZ^{\mathrm{der}}_{\mathrm{ch}}(A), \Tr_A\bigr),
\]
where the BKM root system (for K3-fibered CY$_3$) supplies the root lattice structure and the Borcherds denominator formula controls the bar Euler product.

\noindent\textit{Verification}: 124 tests in \texttt{cross\_volume\_shadow\_bridge.py}.

codex
The chapter has broader `d=3` advertising beyond the opening CY-A section, and some of it likely crosses the repo’s status boundary by treating global CY3 chiral algebras as constructed objects. I’m mapping the theorem/proposition surface now so I can downgrade only the exact overclaimed nodes instead of patching prose blindly.
exec
/bin/zsh -lc "rg -n -P '"'^'"\\\\begin\\{(theorem|proposition|corollary|conjecture)\\}' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
32:\begin{theorem}[CY-to-chiral functor: Theorem CY-A$_2$, $d = 2$]
47:\begin{proposition}[CY modular characteristic at $d = 2$: Theorem CY-A$_2$(iii)]
65:\begin{conjecture}[CY modular characteristic at $d \geq 3$]
98:\begin{conjecture}[$\Phi$ respects $\bZ/2$-orbifold structure for Enriques]
129:\begin{conjecture}[Enriques $\kappa_{\mathrm{BKM}}$-spectrum]
167:\begin{proposition}[Kummer orbifold chiral algebra: Steps 1--4]
290:\begin{conjecture}[The Kummer route, Step~5: resolution recovers $\cH_{\mathrm{Muk}}$]
433:\begin{theorem}[The $d = 3$ functor chain is verified for $\C^3$]
458:\begin{theorem}[Abelianity of the classical bracket]
481:\begin{theorem}[Hochschild cohomology and unique deformation]
506:\begin{proposition}[Necessity of $\Omega$-deformation for noncompact CY$_3$]
550:\begin{theorem}[Vanishing of the $\bS^3$-framing obstruction for CY$_3$ categories]
584:\begin{corollary}[Topological vanishing of the CY-A$_3$ obstruction]
602:\begin{theorem}[\v{C}ech contracting homotopy for compact CY$_3$;
773:\begin{theorem}[Drinfeld center identification for $\C^3$]
813:\begin{corollary}[$\Eone \to \Etwo$ obstruction is trivial]
836:\begin{proposition}[Bar-complex Euler product for $\C^3$]
849:\begin{proposition}[Crystal melting = $\Eone$ bar cohomology]
867:\begin{proposition}[Topological vertex = degree-$3$ $\Eone$ bar amplitude]
885:\begin{theorem}[Modular characteristic of $\C^3$: five-path verification]
exec
/bin/zsh -lc "rg -n -F 'unconditional Costello--Li comparison' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'global \\Eone-chiral algebra' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'A_{X_\\Sigma}' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -P '"'^'"\\\\ClaimStatus(ProvedHere|Conditional|Conjectured|Heuristic|ProvedElsewhere|Open)\\{\\}' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
34:\ClaimStatusProvedHere{}
49:\ClaimStatusProvedHere{}
67:\ClaimStatusConjectured{}
81:\ClaimStatusHeuristic{}
100:\ClaimStatusConjectured{}
119:\ClaimStatusHeuristic{}
131:\ClaimStatusConjectured{}
143:\ClaimStatusHeuristic{}
156:\ClaimStatusHeuristic{}
169:\ClaimStatusProvedHere{}
292:\ClaimStatusConjectured{}
351:\ClaimStatusHeuristic{}
380:\ClaimStatusHeuristic{}
435:\ClaimStatusProvedHere{}
460:\ClaimStatusProvedHere{}
483:\ClaimStatusProvedHere{}
508:\ClaimStatusProvedHere{}
552:\ClaimStatusProvedHere{}
586:\ClaimStatusConditional{}
775:\ClaimStatusProvedHere{}
 succeeded in 52ms:
1918:\noindent The dividing line is precise. At $d = 2$, the functor $\Phi$ is constructed unconditionally (Theorem~\ref{thm:cy-to-chiral}): the $\bS^2$-framing provides native $\Etwo$ structure, and no Drinfeld center passage is needed. At $d = 3$, the functor chain is verified end-to-end for $\C^3$ and the resolved conifold (where both sides are independently known), and the quiver-chart gluing construction is a theorem for all smooth toric CY$_3$ varieties (Theorem~\ref{thm:toric-chart-gluing}): the McKay atlas, mutation $\Eone$-equivalences, and $\Eone$ descent degeneration combine to produce a global $\Eone$-chiral algebra with an unconditional Costello--Li comparison. The topological $\bS^3$-framing obstruction vanishes universally, but the chain-level $\Ainf$-compatible trivialization for compact non-toric CY$_3$ and the global hocolim assembly for non-toric geometries (Conjecture~\ref{conj:e1-chart-gluing}) remain conjectural. Every formal statement in this chapter carries the appropriate status tag: \verb|\ClaimStatusProvedHere| for the $d = 2$ functor, the toric CY$_3$ gluing theorem, and the $\C^3$ verification, \verb|\ClaimStatusConjectured| for the general $d = 3$ programme and its downstream consequences, and \verb|\ClaimStatusConditional| for results that chain through CY-A$_3$.
 exited 1 in 52ms:

 succeeded in 52ms:
1130:  A_{X_\Sigma} \;:=\; \operatorname{hocolim}_{\Sigma(3)} \CoHA(Q_\alpha, W_\alpha)
1135:  \Psi \colon A_{X_\Sigma}^{\mathrm{hocolim}} \;\xrightarrow{\;\simeq_{E_1}\;}\; A_{X_\Sigma}^{\mathrm{CL}} \;=\; U^{\mathrm{ch}}(\mathfrak{L}_{X_\Sigma}),
1137: where $A_{X_\Sigma}^{\mathrm{CL}}$ is the boundary algebra of $5$d holomorphic Chern--Simons on $X_\Sigma \times \R^2$ \textup{(}Costello--Li\textup{)} and $\mathfrak{L}_{X_\Sigma} = \mathrm{PV}^*(X_\Sigma)$ is the polyvector-field Lie conformal algebra. The comparison map is the composite
1139:  A_{X_\Sigma}^{\mathrm{hocolim}} = \operatorname{hocolim} U^{\mathrm{ch}}(\mathfrak{L}_{Q_\alpha}) = U^{\mathrm{ch}}(\operatorname{hocolim} \mathfrak{L}_{Q_\alpha}) = U^{\mathrm{ch}}(\mathfrak{L}_{X_\Sigma}) = A_{X_\Sigma}^{\mathrm{CL}},
1142: \item \textbf{Invariants.} The modular characteristic $\kappa_{\mathrm{ch}}(A_{X_\Sigma})$ is well-defined and independent of the atlas, since flops preserve $\kappa_{\mathrm{ch}}$ \textup{(}Proposition~\textup{\ref{prop:flop-koszul-duality}(iii))}.
1155:Part~(v) follows from Proposition~\ref{prop:flop-koszul-duality}(iii): flops are derived equivalences and $\kappa_{\mathrm{ch}}$ is a derived invariant. Since any two atlases of $X_\Sigma$ are related by a sequence of refinements and flop relabellings, $\kappa_{\mathrm{ch}}(A_{X_\Sigma})$ is atlas-independent.
1720:For any smooth toric CY$_3$ $X_\Sigma$ with McKay quiver atlas $(Q_\alpha, W_\alpha)_{\alpha \in I}$, the toric chart gluing theorem (Theorem~\ref{thm:toric-chart-gluing}) assembles the global $\Eone$-chiral algebra $A_{X_\Sigma}$. The $\CoHA$ of $(Q_\alpha, W_\alpha)$ is the positive half of the quantum vertex chiral group $G(Q_\alpha, W_\alpha)$ (Kontsevich--Soibelman, Schiffmann--Vasserot, Davison). The bar complex of $A_{X_\Sigma}$ recovers the DT moduli via the CoHA-bar identification. The correspondence holds at the motivic level because the CoHA multiplication IS the bar differential, and the CoHA Hilbert series IS the bar Euler characteristic.
1777:The atlas data table records the $\kappa_{\mathrm{ch}}$ values that would result from the quiver-chart gluing construction. For toric CY$_3$ varieties ($\C^3$, resolved conifold, local $\bP^2$, local $\bP^1 \times \bP^1$, and all toric crepant resolutions), the global chiral algebra $A_{X_\Sigma}$ is a proved object: Theorem~\ref{thm:toric-chart-gluing} assembles the hocolim from the McKay quiver atlas and establishes the Costello--Li comparison. For non-toric geometries ($K3 \times E$, the quintic), the hocolim assembly is conditional on Conjecture~\ref{conj:e1-chart-gluing}, which chains back to CY-A$_3$. The following section collects the full $d = 3$ programme statement and its current status.


thinking
**Fixing improper conditioning**

I think I need to fix the d=3 improper conditioning related to CY-A and global objects. It seems I don't have to address every d=3 computational theorem, just the ones that lead to d=3 chiral algebra objects or functor claims. Still, to ensure everything is "properly conditioned" throughout the chapter, I may need to consider a broader approach. There’s a lot to navigate here!
thinking
**Exploring E1-chiral algebra**

I’m considering the E1-chiral algebra and how it relates to associative factorization in CxR. It feels like local CoHA models might provide insight into E1, but I wonder if labeling it as chiral algebra might be an overreach. I want to ensure I'm not over-claiming its implications or settling on definitions too hastily. It’s a complex area, so I need to tread carefully as I think this through!
codex
I’ve now found the main structural wound: the toric CY3 gluing block still advertises a proved global `A_X` object, which crosses the repo’s hard status boundary. I’m reading that theorem cluster and the later Borcherds/bar-Euler passages together so I can downgrade the construction precisely and keep the independent compute-backed pieces intact.
exec
/bin/zsh -lc "sed -n '1090,1265p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:

\noindent\textit{Verification}: the Gepner data ($W = \sum x_i^5$, orbifold group $\Z_5^4 = \Z_5^5/\Z_5^{\mathrm{diag}}$, $625$ fractional branes) is recorded in \texttt{tilting\_chart\_cy3.py}.
\end{remark}


\subsection{The $\Eone$-chiral hocolim}
\label{subsec:e1-hocolim}

Given a quiver-chart atlas $\cA$, each chart $(Q_\alpha, W_\alpha)$ determines a critical CoHA $\cH(Q_\alpha, W_\alpha)$ (Definition~\ref{def:critical-coha}), which is an associative ($\Eone$) algebra with the Schiffmann--Vasserot--Yang--Zhao Hall product; by the $d = 3$ functor chain (Theorem~\ref{thm:e1-universality-cy3}), the factorization envelope of the associated Lie conformal algebra carries a canonical $\Eone$-chiral algebra structure.

\begin{conjecture}[$\Eone$ chart gluing]
\label{conj:e1-chart-gluing}
\ClaimStatusConjectured{}
Given a quiver-chart atlas $\cA = \{(Q_\alpha, W_\alpha, \Psi_\alpha)\}_{\alpha \in I}$ for a CY$_3$ category $\cC$, the \emph{global $\Eone$-chiral algebra} is the homotopy colimit
\begin{equation}
\label{eq:global-e1-chiral}
 A_\cC \;:=\; \operatorname{hocolim}_{I} \CoHA(Q_\alpha, W_\alpha)
\end{equation}
taken in the $\infty$-category of $\Eone$-chiral algebras, where the diagram $I \to \Eone\text{-}\mathrm{ChirAlg}$ is determined by the transition mutations $\mu_{\alpha\beta}$.

exec
/bin/zsh -lc "sed -n '1988,2012p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1538,1580p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:

\noindent\textit{Verification}: 119 tests in \texttt{cy3\_grand\_atlas.py}.
\end{theorem}

\begin{proof}
The BCOV formula $F_1 = -\tfrac{1}{2} \log \det(\bar{\partial}^\dagger \bar{\partial})$ on a compact CY$_3$ $X$ gives $F_1 = \chi_{\mathrm{top}}(X)/24$ when $h^{1,0}(X) = 0$. The condition $h^{1,0} = 0$ ensures that the genus-$1$ free energy has no contribution from abelian zero modes; the formula holds for the quintic ($h^{2,1} = 101$) and all other CICYs with $h^{1,0} = 0$, regardless of the number of complex structure moduli.

For K3-fibered CY$_3$, the infinite tower of BPS bound states across fibers contributes additional genus-$1$ data beyond the one-loop determinant. For $K3 \times E$: the $24$ free bosons from the K3 fiber give $\kappa_{\mathrm{fiber}} = 24$, but the sewing along $E$ via the DMVV formula introduces imaginary root contributions that produce $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$ (the weight of the Igusa cusp form). The ``lost'' $19$ units ($24 - 5 = 19$) are absorbed by the Borcherds product structure.

For the resolved conifold: $\chi_{\mathrm{top}} = 2$ (the total space deformation retracts onto $\bP^1$) gives $\chi_{\mathrm{top}}/24 = 1/12$, but the DT computation gives $\kappa_{\mathrm{ch}} = 1$ (the conifold has a single BPS state contributing at genus~$1$).
\end{proof}

\begin{proposition}[The categorical Euler characteristic resolves the discrepancy]
\label{prop:categorical-euler}
\ClaimStatusProvedHere{}
The invariant controlling the BKM modular characteristic is the \emph{categorical} Euler characteristic $\chi^{\CY}$, not the topological one. For $K3 \times E$: $\chi_{\mathrm{top}} = 0$ but $\chi^{\CY} = 5 = \kappa_{\mathrm{BKM}}$; the chiral modular characteristic $\kappa_{\mathrm{ch}} = 3$ arises from additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$).

The categorical Euler characteristic accounts for the full BPS spectrum (all charges), not just the massless modes that contribute to $\chi_{\mathrm{top}}$. For K3-fibered CY$_3$, the infinite tower of bound states across fibers contributes to $\chi^{\CY}$ via the Borcherds denominator weight.

Five independent verifications of $\kappa_{\mathrm{BKM}}(K3 \times E) = 5$:
 succeeded in 51ms:
\noindent\textit{Verification}: $76$ tests in \texttt{drinfeld\_center\_hocolim.py} and $85$ tests in \texttt{swiss\_cheese\_chart\_gluing.py}. The obstruction grows with geometric complexity: $\C^3$ ($0$) $<$ conifold ($2$) $<$ local~$\bP^2$ (nonzero) $<$ $K3 \times E$ (massive, controlled by the full BKM superalgebra).

\medskip

\subsection{Bar-hocolim commutation}
\label{subsec:bar-hocolim}

The bar construction commutes with homotopy colimits. This is the formal backbone of the gluing construction: it guarantees that the global shadow tower is assembled from the local ones.

\begin{theorem}[Bar-hocolim commutation]
\label{thm:bar-hocolim}
\ClaimStatusProvedHere{}
For any diagram $D \colon I \to \Eone\text{-}\mathrm{ChirAlg}$ indexed by a finite poset $I$, there is a natural equivalence of $\Eone$-factorization coalgebras
\begin{equation}
\label{eq:bar-hocolim}
 B^{\Eone}\!\bigl(\operatorname{hocolim}_I D\bigr) \;\simeq\; \operatorname{hocolim}_I B^{\Eone}(D).
\end{equation}
\end{theorem}

\begin{proof}
codex
I’ve confirmed the main overclaiming zone is the toric `E_1` hocolim block plus a few downstream advertisements that treat the candidate CY3 output as constructed. Before editing I’m pulling the exact Vol I labels I’ll cite, so the fortification cross-references point to the live rectified theorem surfaces rather than generic “Theorem A/D” prose.
exec
/bin/zsh -lc "rg -n -F 'Theorem~A' /Users/raeez/chiral-bar-cobar -g '*.tex'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -P '"'^'"\\\\label\\{.*\\}' /Users/raeez/chiral-bar-cobar -g '*.tex' | rg 'thm:.*(bar|cobar|kappa|modular|shadow|uniform|hocolim|theorem-a|theorem-d|theorem-h|MC|shadow)'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:803:The chiral Kontsevich formula realizes Theorem~A
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:1243:($\operatorname{Ran}_1(X) \cong X$) follows from Theorem~A +
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1940:\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:444:\item \emph{Theorem~A} (Geometric Bar-Cobar Duality, Theorem~\ref{thm:bar-cobar-isomorphism-main}; this is Theorem~$\mathrm{A}_2$ in the $\mathrm{A}_0/\mathrm{A}_1/\mathrm{A}_2$ decomposition of Remark~\ref{rem:theorem-A-decomposition}):
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex:1279:Theorem~A. The lift exists because $\mathcal{C}_{\mathrm{op}}$
/Users/raeez/chiral-bar-cobar/chapters/connections/poincare_computations.tex:7:Theorem~A, an adjunction between factorization homology and
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1767:Theorem~A$_2$).
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:877:\emph{Theorem~A (Geometric Bar-Cobar Duality).}
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:3935:The three main theorems are verified at genus~$1$ for $\widehat{\mathfrak{sl}}_{2,k}$: Theorem~A via the bar complex on $E_\tau$ with propagator $K^{(1)} = \theta_1'/\theta_1$ (Theorem~\ref{thm:km-higher-genus-corrections}); Theorem~B via $E_2$-collapse for generic $k$ (Theorem~\ref{thm:sl2-genus1-inversion}); and Theorem~C via
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:5877:BRST variations above. This is Theorem~A (the bar-cobar
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:5958:\textup{(Theorem~A, Chapter~\ref{chap:bar-cobar-adjunction})} intertwining
/Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:281:\emph{Theorem~A}: $\bar{B}^{\mathrm{ell}}(U_{q,t})$ computes the Koszul dual coalgebra (nilpotency via Proposition~\ref{prop:fay-implies-d-squared}).
/Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:2116:The Verdier intertwining \textup{(}Theorem~A,
/Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:3062:the Koszul locus (Theorem~A intertwining). The
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_fusion.tex:10:bar-cobar adjunction (Theorem~A) transports between the
/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:1456:Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}) produces the
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:833:Theorem~A\textsubscript{2}
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:8022:inverse; the full content is Verdier intertwining (Theorem~A).
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:8067: \textup{(}Theorem~A\textup{)} identifies
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:8139:(Theorem~A\textsubscript{2}).
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/appendices/homotopy_transfer.tex:524:\label{thm:bar-cobar-htt}
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:395:\label{thm:nms-shadow-tower-mc}%
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:772:\label{thm:nms-shadow-master-equations}
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:873:\label{thm:nms-shadow-cocycle-characterization}
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:1316:\label{thm:nms-virasoro-mixed-shadow}
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:1472:\label{thm:nms-w3-mixed-shadow-normal-form}
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:1823:\label{thm:nms-clutching-law-modular-resonance}
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:1897:\label{thm:nms-first-nonlinear-shadow-theta}
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:3753:\label{thm:ds-shadow-depth-increase}%
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:3958:\label{thm:shadow-subalgebra-autonomy}%
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:4063:\label{thm:nms-shadow-mc-potential}%
/Users/raeez/chiral-bar-cobar/appendices/spectral_higher_genus.tex:156:\label{thm:bar-spectral-sequence-config}
/Users/raeez/chiral-bar-cobar/appendices/dual_methodology.tex:25:\label{thm:abstract-bar-cobar}
/Users/raeez/chiral-bar-cobar/appendices/dual_methodology.tex:48:\label{thm:concrete-bar-cobar}
/Users/raeez/chiral-bar-cobar/appendices/signs_and_shifts.tex:469:\label{thm:det-bar-cobar-signs}
/Users/raeez/chiral-bar-cobar/appendices/arnold_relations.tex:92:\label{thm:bar-d-squared-arnold}
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex:399:\label{thm:bar-computes-deformation}
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2052:\label{thm:heisenberg-ordered-bar}
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2401:\label{thm:bg-ordered-bar}
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2404:\label{thm:bc-ordered-bar}
exec
/bin/zsh -lc "rg -n -F 'Theorem~H' /Users/raeez/chiral-bar-cobar -g '*.tex'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Theorem~D' /Users/raeez/chiral-bar-cobar -g '*.tex'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:1504:adds $\delta F_g^{\mathrm{cross}}$). Theorem~H identifies the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:3482:\subsection*{9.5.\enspace Chiral Hochschild cohomology (Theorem~H)}
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:3908:the Kodaira--Spencer class; Theorem~H (Hochschild polynomial
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:4836:Theorems~A--D and Theorem~H are proved projections at the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1252:the Kodaira--Spencer class; Theorem~H (Hochschild polynomial
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:2180:Theorems~A--D and Theorem~H are proved projections at the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed.tex:1252:the Kodaira--Spencer class; Theorem~H (Hochschild polynomial
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed.tex:2180:Theorems~A--D and Theorem~H are proved projections at the
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1012:ring (Theorem~H). Their $\Eone$ formulations require the following
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex:299:Gerstenhaber algebra. On the Koszul locus, Theorem~H
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1644: (Theorem~H, Chapter~\ref{chap:deformation-theory}).
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:136: modular Koszul algebras (Theorem~H).
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:414: Theorem~H does not apply there, and the oper/Feigin--Frenkel package
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3304:bar-cobar inversion via Theorem~H, polynomial growth, and
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4396:in the proof of Theorem~H: the chiral Hochschild complex
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4402:the original Theorem~H proof; the lemma makes it citable
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4658:This recovers Theorem~H
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4815:$H$ & Generic-level Theorem~H package: concentration in & \textbf{Proved} on the Koszul locus & Thms~\ref{thm:main-koszul-hoch}, \\
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6884: by Theorem~H.
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7322: \textbf{Critical level: Theorem~H does NOT apply.}
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:1502:\textsc{(uniform-weight)}). Theorem~D extracts the scalar $\kappa$
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:3907:carries a $(-1)$-shifted symplectic structure; Theorem~D is
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:4:The modular characteristic $\kappa(\cA)$ (Theorem~D) and the spectral
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:425:Item~(i) is Theorem~D specialized to genus~$1$; items~(ii)--(iv)
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1251:carries a $(-1)$-shifted symplectic structure; Theorem~D is
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3583:Theorem~D) or Kac--Moody-type ($\kappa + \kappa' = 0$).
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5193:under cosets (Theorem~D):
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:3302:By Vol~I Theorem~D, $\kappa(\mathrm{Vir}_c) = c/2$. The Koszul
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:7337: (Vol~I, Theorem~D).
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed.tex:1251:carries a $(-1)$-shifted symplectic structure; Theorem~D is
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:681:Theorem~D sees a single scalar:
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:763:(Theorem~D; ) is the first Chern class of the Verlinde bundle;
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:2691:complementarity structure of Theorem~D controlling the
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:3495:\textup{(}Theorem~D\textup{)}: for a single-generator $\mathcal{W}$-algebra with
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:7162:genus-$1$ obstruction class coefficient (Theorem~D). The
/Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex:661:(Theorem~D), so $c' = 26 - 1/2 = 51/2$ and
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex:937:By Theorem~D (Theorem~\ref{thm:modular-characteristic}),
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex:1119: Theorem~D\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex:1486:characteristic $\kappa(\cA)$ and its duality constraint (Theorem~D)
/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:1989:Theorem~D (Theorem~\ref{thm:modular-characteristic})

thinking
**Searching theorem labels**

I need to gather specific theorem labels like `thm:bar-cobar-isomorphism-main`, `thm:modular-characteristic`, and perhaps `thm:main-koszul-hoch`. I should check if theorem A's label is used in the current file by searching for `thm:bar-cobar-isomorphism-main` or `thm:modular-characteristic`, though I'm not sure if they are. It might be necessary to utilize the xrefs mechanism for referencing labels across volumes. I'll search the current repository using `rg` for `thm:bar-cobar-isomorphism-main`.
exec
/bin/zsh -lc "rg -n -F 'thm:bar-cobar-isomorphism-main' ." in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'thm:modular-characteristic' ." in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'thm:main-koszul-hoch' ." in /Users/raeez/calabi-yau-quantum-groups exited 1 in 51ms:

 succeeded in 52ms:
./chapters/examples/toroidal_elliptic.tex:39:\phantomsection\label{thm:modular-characteristic}%
./chapters/examples/toroidal_elliptic.tex:4353:Theorem~\textup{\ref{thm:modular-characteristic})}, in the
./chapters/examples/toroidal_elliptic.tex:4385:(Theorem~\ref{thm:modular-characteristic})
 exited 1 in 52ms:


thinking
**Inspecting local imports**

I find it interesting to consider whether these labels imported locally have any connection to phantom labels from external theorems. It seems worth checking the top of the chapters or the examples, particularly around the file "toroidal_elliptic.tex" near line 39. I want to ensure I’m not missing any important details there. Let’s see what insights I can gather from that section!
codex
The Vol I labels are live and cross-volume referencing is already being done in this repo, so I’m checking the local alias pattern before I insert any new refs. That lets me cite the rectified theorem labels directly without breaking the build.
exec
/bin/zsh -lc "sed -n '1,70p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CHAPTER: TOROIDAL AND ELLIPTIC ALGEBRAS
% Migrated from Vol I (Chapter 66) with K3 x E content merged from k3_times_e.tex.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Cross-volume label stubs: these labels are defined in Vol I and
%% referenced in this chapter. The stubs prevent undefined-reference
%% errors; the actual content lives in Vol I.
\phantomsection\label{conj:master-infinite-generator}%
\phantomsection\label{constr:platonic-package}%
\phantomsection\label{conv:bar-coalgebra-identity}%
\phantomsection\label{conv:hms-levels}%
\phantomsection\label{conv:regime-tags}%
\phantomsection\label{cor:bar-is-dgcoalg}%
\phantomsection\label{cor:shadow-extraction}%
\phantomsection\label{def:chiral-ass-operad}%
\phantomsection\label{def:cyclically-admissible}%
\phantomsection\label{def:shadow-depth-classification}%
\phantomsection\label{def:shadow-postnikov-tower}%
\phantomsection\label{prop:independent-sum-factorization}%
exec
/bin/zsh -lc "rg -n -F '\\externaldocument' main.tex chapters -g '*.tex'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'phantomsection\\label{thm:modular-characteristic}' -g '*.tex' ." in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 succeeded in 51ms:
./chapters/examples/toroidal_elliptic.tex:39:\phantomsection\label{thm:modular-characteristic}%




thinking
**Considering cross-references for theorems**

The user asked about adding cross-references to rectified theorems, and I’m thinking A and D might be sufficient, or maybe H? The opening says theorems A-D+H. I should look for references to A, D, and H and see if H is accessible. I could also search for `main-koszul-hoch` in the current repo. There's a consideration to simplify things by just referencing `Theorem\ref{thm:modular-characteristic}` and `Theorem\ref{thm:bar-cobar-adjunction}`.
thinking
**Crafting rigorous proofs**

I’m realizing I need immediate proof for my theorem, but it seems I don’t have one. The user wants me to strengthen the main results and explore alternative proofs. So, I definitely need to add the proof for CY-A2 and maybe an alternative remark too. This is serious! I should look into the context or other chapters; a proof sketch could be helpful. But it’s important to be rigorous and ground it in existing constructions, step by step.
thinking
**Considering proof paths**

I see that I have proof already, but maybe I should think about strengthening it with a second proof path. I could add a secondary verification remark using some specific theorems. But then again, is that really necessary? The user asked for every theorem in scope, so should I limit it just to certain theorems or include the proposition too since it’s a key result? In the final report, I can clarify the scope based on the relevant surfaces.
thinking
**Evaluating kappa values**

I’m considering the values related to `chiCY = 5` and kappa_BKM in the context of K3×E. I'm questioning if `chiCY = 5` is accurate, especially since kappa_ch is 3, and kappa_BKM is claimed to be 5. It seems there might be some distinct differences between them. The statement about the categorical Euler characteristic accounting for the full BPS spectrum might be a stretch. I need to review the proof to check if it uses bar Euler or BKM in its calculations.
exec
/bin/zsh -lc "sed -n '2000,2035p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\begin{proposition}[The categorical Euler characteristic resolves the discrepancy]
\label{prop:categorical-euler}
\ClaimStatusProvedHere{}
The invariant controlling the BKM modular characteristic is the \emph{categorical} Euler characteristic $\chi^{\CY}$, not the topological one. For $K3 \times E$: $\chi_{\mathrm{top}} = 0$ but $\chi^{\CY} = 5 = \kappa_{\mathrm{BKM}}$; the chiral modular characteristic $\kappa_{\mathrm{ch}} = 3$ arises from additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$).

The categorical Euler characteristic accounts for the full BPS spectrum (all charges), not just the massless modes that contribute to $\chi_{\mathrm{top}}$. For K3-fibered CY$_3$, the infinite tower of bound states across fibers contributes to $\chi^{\CY}$ via the Borcherds denominator weight.

Five independent verifications of $\kappa_{\mathrm{BKM}}(K3 \times E) = 5$:
\begin{enumerate}[label=\textup{(\alph*)}]
 \item Weight of the Igusa cusp form: $\mathrm{wt}(\Delta_5) = 5$.
 \item DMVV exponent: the Borcherds lift weight formula gives $c(0)/2 = 10/2 = 5$.
 \item Bar Euler product: the genus-$1$ coefficient of $\log Z_{\DT}$ gives $F_1 = 5/24$.
 \item Relative DT: fiber-by-fiber computation via K3 fibers sewed along $E$.
 \item Anomaly cancellation: the worldsheet anomaly for the $K3 \times E$ sigma model.
\end{enumerate}

\noindent\textit{Verification}: 78 tests in \texttt{k3e\_relative\_shadow.py}; 119 tests in \texttt{cy3\_grand\_atlas.py}.
\end{proposition}



thinking
**Searching for Euler products**

I'm considering searching for terms like "controls the bar Euler product" and "three-variable generalization." I might start by looking up "bar Euler" results since I already found something in line 1723, 2009, possibly related to the "Bar Euler product." To refine my search, I think I should run a simpler command with regex, focusing on "bar Euler" and variations with Borcherds. Let's see what I can find!
codex
I’ve got the exact passages to soften on the Borcherds side: one explicit “three-variable generalisation of the bar Euler product,” one “denominator formula controls the bar Euler product,” and one “Bar Euler product” verification bullet that really only uses the genus-one coefficient. Those will be rewritten as analogies/evidence, not identifications.
exec
/bin/zsh -lc "rg -n -e 'bar Euler' -e 'bar-Euler' -e 'controls the bar Euler product' -e 'generalisation of the bar Euler product' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -e 'Borcherds.*bar' -e 'bar.*Borcherds' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
135: \item $\kappa_{\mathrm{BKM}}(S \times E) = 4$, the weight of the Allcock Borcherds product on $O(2, 10)$. This is verified computationally by \texttt{enriques\_shadow.py} (72 tests; see Remark~\textup{\ref{rem:enriques-kappa-anomaly}} in the bar-cobar bridge chapter).
1723:The CY-to-chiral functor at $d = 3$ is not yet constructed for $K3 \times E$ (Conjecture~\ref{conj:cy-to-chiral-d3}). The shadow data is read from two sources: $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$; Proposition~\ref{prop:categorical-euler}), and $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)/1$ from the Borcherds lift weight formula. The genus-$1$ shadow $F_1 = \kappa_{\mathrm{BKM}}/24 = 5/24$ matches the DT genus-$1$ free energy. The full DT partition function $Z_{\DT}(K3 \times E) = C/\Delta_5^2$ involves the Igusa cusp form, whose Borcherds product formula $\Delta_5 = p \prod (1-p^n q^l r^m)^{f(4nm - l^2)}$ is a three-variable generalisation of the bar Euler product (Chapter~\ref{ch:k3-times-e}). The passage from the scalar shadow to the full $\Delta_5$ requires the BKM root system, which encodes all BPS states across all charge lattice directions.
2116:where the BKM root system (for K3-fibered CY$_3$) supplies the root lattice structure and the Borcherds denominator formula controls the bar Euler product.
 succeeded in 52ms:
854: \item The MacMahon function $M(q) = \prod_{n \geq 1}(1-q^n)^{-n}$ is the bar Euler characteristic of the positive half of the affine Yangian: $M(q) = \sum_{k \geq 0} \mathrm{ch}(H^k(B(Y^+(\widehat{\fgl}_1))))$.
856: \item The bar Euler characteristic inverts the MacMahon function: $\sum_{k \geq 0}(-1)^k (M(q)-1)^k = 1/M(q) = \prod_{n \geq 1}(1-q^n)^n$. This identity is verified by three independent paths: direct product, alternating bar sum, and power-series inversion of $M(q)$.
863:The crystal melting model of Okounkov--Reshetikhin--Vafa, counting three-dimensional partitions weighted by $q^{|\pi|}$, is the degree filtration of the $\Eone$ bar complex of $\cW_{1+\infty}$: the bar degree-$n$ component $\barB^n(\cW_{1+\infty})$ counts configurations of $n$ atoms in the crystal. The MacMahon function $M(q) = \prod_{n \ge 1}(1-q^n)^{-n}$ is the bar Poincar\'e series (Proposition~\ref{prop:c3-bar-euler}). Concretely, the degree filtration $F^{\bullet} \barB(\cW_{1+\infty})$ has associated graded whose Hilbert series at degree~$n$ counts plane partitions of size~$n$, with the bar differential encoding the crystal growth rules (addition and removal of atoms at admissible sites). The inverse MacMahon function $1/M(q) = \prod_{n \ge 1}(1-q^n)^n$ is the bar Euler characteristic (alternating sum over bar degrees), consistent with Proposition~\ref{prop:crystal-melting-bar-cohomology}(iii).
1597:The following conjecture refines Conjecture~\ref{conj:dt-hocolim-shadow} by stratifying the identification into three levels of precision and giving the explicit bar Euler product formula. It is the central enumerative prediction of the CY-to-chiral programme.
1717:The CY-to-chiral functor produces $A_{\C^3} = \cW_{1+\infty} = H_1$ (at the self-dual point). The bar Euler product is $1/M(q) = \prod (1-q^n)^n$ (Proposition~\ref{prop:c3-bar-euler}), inverting the MacMahon function. The bar cohomology gives $\Omega(n) = n = \Omega_{\DT}(n)$ at all degrees ($115$ tests). The motivic comparison holds: $B^{\Eone}(H_1)$ as a graded $\Eone$-coalgebra matches the motivic DT coalgebra of $\C^3$ via the Schiffmann--Vasserot identification $\CoHA(\C^3) = Y^+(\widehat{\fgl}_1)$.
1720:For any smooth toric CY$_3$ $X_\Sigma$ with McKay quiver atlas $(Q_\alpha, W_\alpha)_{\alpha \in I}$, the toric chart gluing theorem (Theorem~\ref{thm:toric-chart-gluing}) assembles the global $\Eone$-chiral algebra $A_{X_\Sigma}$. The $\CoHA$ of $(Q_\alpha, W_\alpha)$ is the positive half of the quantum vertex chiral group $G(Q_\alpha, W_\alpha)$ (Kontsevich--Soibelman, Schiffmann--Vasserot, Davison). The bar complex of $A_{X_\Sigma}$ recovers the DT moduli via the CoHA-bar identification. The correspondence holds at the motivic level because the CoHA multiplication IS the bar differential, and the CoHA Hilbert series IS the bar Euler characteristic.
1723:The CY-to-chiral functor at $d = 3$ is not yet constructed for $K3 \times E$ (Conjecture~\ref{conj:cy-to-chiral-d3}). The shadow data is read from two sources: $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$; Proposition~\ref{prop:categorical-euler}), and $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)/1$ from the Borcherds lift weight formula. The genus-$1$ shadow $F_1 = \kappa_{\mathrm{BKM}}/24 = 5/24$ matches the DT genus-$1$ free energy. The full DT partition function $Z_{\DT}(K3 \times E) = C/\Delta_5^2$ involves the Igusa cusp form, whose Borcherds product formula $\Delta_5 = p \prod (1-p^n q^l r^m)^{f(4nm - l^2)}$ is a three-variable generalisation of the bar Euler product (Chapter~\ref{ch:k3-times-e}). The passage from the scalar shadow to the full $\Delta_5$ requires the BKM root system, which encodes all BPS states across all charge lattice directions.
1855:Theorem~\textup{\ref{thm:kappa-c3}} establishes $\kappa_{\mathrm{ch}}(\C^3) = \kappa_{\mathrm{ch}}(H_1) = 1$ by five independent paths (Heisenberg level, MacMahon leading order, bar Euler product, DT genus-$1$ free energy, categorical Euler characteristic).
2116:where the BKM root system (for K3-fibered CY$_3$) supplies the root lattice structure and the Borcherds denominator formula controls the bar Euler product.
exec
/bin/zsh -lc "rg -n -F '\\mathrm{Tot}(K_S)' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'chi_{\\mathrm{top}}(S)/2' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
2188: \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
 succeeded in 50ms:
2188: \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.



thinking
**Reviewing proof options**

I'm considering using an alternative approach that involves applying Vol I Theorem D to the bar complex and the Euler characteristic of indecomposables. While it may be distinct from the quantization correction argument due to bar invariance, it could serve as a valid secondary proof path. I think I should add a remark indicating this, clarifying that it might not be fully proven but provides a concise sketch for the user who prefers rigor.
thinking
**Considering final report details**

I'm thinking about how to present everything clearly in the final confidence medium. Maybe I don't need to edit the original proposition. Instead, I could just summarize that a secondary proof has been identified or sketched in the final report. This way, I'm conveying the essential information without overcomplicating things. It’s about striking the right balance to ensure clarity for the user while still being thorough.
thinking
**Adjusting theorems and proofs**

I need to consider adjusting some lines, like 1720, 1777, and 1918. That feels manageable. However, when it comes to the theorem proof, it seems to only hold under certain assumptions. I should clarify which parts are unconditional and which assumptions apply. It’s essential to ensure that the proof is thorough and accurately reflects these distinctions. Let’s make sure to do this right!
exec
/bin/zsh -lc "sed -n '924,980p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
% ============================================================

The preceding sections have established the $d = 3$ functor chain and the Drinfeld center passage from $\Eone$ to $\Etwo$. The following theorem shows that the $\Eone$ structure is \emph{universal}: every CY$_3$ chiral algebra with $\Omega$-deformation is natively $\Eone$, not $\Etwo$. The proof has four independent pillars.


\begin{theorem}[$\Eone$ universality for CY$_3$ chiral algebras]
\label{thm:e1-universality-cy3}
\ClaimStatusProvedHere{}
For any toric CY$_3$ category $\cC$ with $T^3$-equivariant $\Omega$-deformation ($\sigma_3 = h_1 h_2 h_3 \neq 0$, subject to $h_1 + h_2 + h_3 = 0$), the chiral algebra $A_\cC = \Phi(\cC)$ is natively $\Eone$. For compact CY$_3$ without a global torus action, the $\Eone$ nature is expected but requires a different argument; see Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}.

Concretely: the $\bS^3$-framing obstruction vanishes topologically ($\pi_3(B\Sp(2m)) = 0$), but the chain-level BV trivialization via holomorphic CS is NOT $\Etwo$-equivariant. The $\Etwo$-braided structure is recovered \emph{only} through the Drinfeld center of the $\Eone$-monoidal representation category (Theorem~\textup{\ref{thm:c3-drinfeld-center}}).
\end{theorem}

\begin{proof}
Four independent pillars, each sufficient to establish the $\Eone$ nature.

\medskip
\noindent\textbf{Pillar (a): Abelianity of the classical bracket.}
By Theorem~\ref{thm:c3-abelian-bracket}, the $\GL(3)$-invariant Schouten--Nijenhuis brackets on $\PV^*(\C^3)$ all vanish. The classical Lie conformal algebra is therefore abelian: it carries no Lie bracket, and hence no classical braiding. The entire noncommutative structure of $A_\cC$ arises from quantization in the factorization envelope, not from a pre-existing bracket. This quantization introduces associativity ($\Eone$) through the extension correspondence (the CoHA multiplication), which is ordered: short exact sequences $0 \to V' \to V \to V'' \to 0$ have a preferred direction (sub before quotient). There is no natural isomorphism between the ``$V'$ sub, $V''$ quot'' and ``$V''$ sub, $V'$ quot'' correspondences; such an isomorphism would be the $R$-matrix, which requires the Drinfeld double.

exec
/bin/zsh -lc "rg -n -e 'CY-to-chiral functor produces' -e 'construction is a theorem' -e 'proved object' -e 'unconditional Costello--Li comparison' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -e 'toric chart gluing theorem' -e 'global \\\\Eone-chiral algebra' -e 'global chiral algebra \\\\A_' -e 'A_\\{X_\\\\Sigma\\}' -e 'Theorem~\\\\ref\\{thm:toric-chart-gluing\\}' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
876: \item \emph{Algebra identification.} By Schiffmann--Vasserot, $\CoHA(\C^3) = Y^+(\widehat{\fgl}_1)$; by Proch\'azka--Rap\v{c}\'ak, $Y(\widehat{\fgl}_1) = \cW_{1+\infty}$. The CY-to-chiral functor produces $A_{\C^3} = \cW_{1+\infty}$ as an $\Eone$-chiral algebra.
1118:For general CY$_3$ categories, the conjecture chains through the Bridgeland finiteness conjecture (Conjecture~\ref{conj:tilting-chart-cover}). For toric CY$_3$ varieties, all ingredients are unconditional, and the construction is a theorem.
1717:The CY-to-chiral functor produces $A_{\C^3} = \cW_{1+\infty} = H_1$ (at the self-dual point). The bar Euler product is $1/M(q) = \prod (1-q^n)^n$ (Proposition~\ref{prop:c3-bar-euler}), inverting the MacMahon function. The bar cohomology gives $\Omega(n) = n = \Omega_{\DT}(n)$ at all degrees ($115$ tests). The motivic comparison holds: $B^{\Eone}(H_1)$ as a graded $\Eone$-coalgebra matches the motivic DT coalgebra of $\C^3$ via the Schiffmann--Vasserot identification $\CoHA(\C^3) = Y^+(\widehat{\fgl}_1)$.
1777:The atlas data table records the $\kappa_{\mathrm{ch}}$ values that would result from the quiver-chart gluing construction. For toric CY$_3$ varieties ($\C^3$, resolved conifold, local $\bP^2$, local $\bP^1 \times \bP^1$, and all toric crepant resolutions), the global chiral algebra $A_{X_\Sigma}$ is a proved object: Theorem~\ref{thm:toric-chart-gluing} assembles the hocolim from the McKay quiver atlas and establishes the Costello--Li comparison. For non-toric geometries ($K3 \times E$, the quintic), the hocolim assembly is conditional on Conjecture~\ref{conj:e1-chart-gluing}, which chains back to CY-A$_3$. The following section collects the full $d = 3$ programme statement and its current status.
1918:\noindent The dividing line is precise. At $d = 2$, the functor $\Phi$ is constructed unconditionally (Theorem~\ref{thm:cy-to-chiral}): the $\bS^2$-framing provides native $\Etwo$ structure, and no Drinfeld center passage is needed. At $d = 3$, the functor chain is verified end-to-end for $\C^3$ and the resolved conifold (where both sides are independently known), and the quiver-chart gluing construction is a theorem for all smooth toric CY$_3$ varieties (Theorem~\ref{thm:toric-chart-gluing}): the McKay atlas, mutation $\Eone$-equivalences, and $\Eone$ descent degeneration combine to produce a global $\Eone$-chiral algebra with an unconditional Costello--Li comparison. The topological $\bS^3$-framing obstruction vanishes universally, but the chain-level $\Ainf$-compatible trivialization for compact non-toric CY$_3$ and the global hocolim assembly for non-toric geometries (Conjecture~\ref{conj:e1-chart-gluing}) remain conjectural. Every formal statement in this chapter carries the appropriate status tag: \verb|\ClaimStatusProvedHere| for the $d = 2$ functor, the toric CY$_3$ gluing theorem, and the $\C^3$ verification, \verb|\ClaimStatusConjectured| for the general $d = 3$ programme and its downstream consequences, and \verb|\ClaimStatusConditional| for results that chain through CY-A$_3$.
 succeeded in 52ms:
1130:  A_{X_\Sigma} \;:=\; \operatorname{hocolim}_{\Sigma(3)} \CoHA(Q_\alpha, W_\alpha)
1135:  \Psi \colon A_{X_\Sigma}^{\mathrm{hocolim}} \;\xrightarrow{\;\simeq_{E_1}\;}\; A_{X_\Sigma}^{\mathrm{CL}} \;=\; U^{\mathrm{ch}}(\mathfrak{L}_{X_\Sigma}),
1137: where $A_{X_\Sigma}^{\mathrm{CL}}$ is the boundary algebra of $5$d holomorphic Chern--Simons on $X_\Sigma \times \R^2$ \textup{(}Costello--Li\textup{)} and $\mathfrak{L}_{X_\Sigma} = \mathrm{PV}^*(X_\Sigma)$ is the polyvector-field Lie conformal algebra. The comparison map is the composite
1139:  A_{X_\Sigma}^{\mathrm{hocolim}} = \operatorname{hocolim} U^{\mathrm{ch}}(\mathfrak{L}_{Q_\alpha}) = U^{\mathrm{ch}}(\operatorname{hocolim} \mathfrak{L}_{Q_\alpha}) = U^{\mathrm{ch}}(\mathfrak{L}_{X_\Sigma}) = A_{X_\Sigma}^{\mathrm{CL}},
1142: \item \textbf{Invariants.} The modular characteristic $\kappa_{\mathrm{ch}}(A_{X_\Sigma})$ is well-defined and independent of the atlas, since flops preserve $\kappa_{\mathrm{ch}}$ \textup{(}Proposition~\textup{\ref{prop:flop-koszul-duality}(iii))}.
1155:Part~(v) follows from Proposition~\ref{prop:flop-koszul-duality}(iii): flops are derived equivalences and $\kappa_{\mathrm{ch}}$ is a derived invariant. Since any two atlases of $X_\Sigma$ are related by a sequence of refinements and flop relabellings, $\kappa_{\mathrm{ch}}(A_{X_\Sigma})$ is atlas-independent.
1720:For any smooth toric CY$_3$ $X_\Sigma$ with McKay quiver atlas $(Q_\alpha, W_\alpha)_{\alpha \in I}$, the toric chart gluing theorem (Theorem~\ref{thm:toric-chart-gluing}) assembles the global $\Eone$-chiral algebra $A_{X_\Sigma}$. The $\CoHA$ of $(Q_\alpha, W_\alpha)$ is the positive half of the quantum vertex chiral group $G(Q_\alpha, W_\alpha)$ (Kontsevich--Soibelman, Schiffmann--Vasserot, Davison). The bar complex of $A_{X_\Sigma}$ recovers the DT moduli via the CoHA-bar identification. The correspondence holds at the motivic level because the CoHA multiplication IS the bar differential, and the CoHA Hilbert series IS the bar Euler characteristic.
1777:The atlas data table records the $\kappa_{\mathrm{ch}}$ values that would result from the quiver-chart gluing construction. For toric CY$_3$ varieties ($\C^3$, resolved conifold, local $\bP^2$, local $\bP^1 \times \bP^1$, and all toric crepant resolutions), the global chiral algebra $A_{X_\Sigma}$ is a proved object: Theorem~\ref{thm:toric-chart-gluing} assembles the hocolim from the McKay quiver atlas and establishes the Costello--Li comparison. For non-toric geometries ($K3 \times E$, the quintic), the hocolim assembly is conditional on Conjecture~\ref{conj:e1-chart-gluing}, which chains back to CY-A$_3$. The following section collects the full $d = 3$ programme statement and its current status.
1918:\noindent The dividing line is precise. At $d = 2$, the functor $\Phi$ is constructed unconditionally (Theorem~\ref{thm:cy-to-chiral}): the $\bS^2$-framing provides native $\Etwo$ structure, and no Drinfeld center passage is needed. At $d = 3$, the functor chain is verified end-to-end for $\C^3$ and the resolved conifold (where both sides are independently known), and the quiver-chart gluing construction is a theorem for all smooth toric CY$_3$ varieties (Theorem~\ref{thm:toric-chart-gluing}): the McKay atlas, mutation $\Eone$-equivalences, and $\Eone$ descent degeneration combine to produce a global $\Eone$-chiral algebra with an unconditional Costello--Li comparison. The topological $\bS^3$-framing obstruction vanishes universally, but the chain-level $\Ainf$-compatible trivialization for compact non-toric CY$_3$ and the global hocolim assembly for non-toric geometries (Conjecture~\ref{conj:e1-chart-gluing}) remain conjectural. Every formal statement in this chapter carries the appropriate status tag: \verb|\ClaimStatusProvedHere| for the $d = 2$ functor, the toric CY$_3$ gluing theorem, and the $\C^3$ verification, \verb|\ClaimStatusConjectured| for the general $d = 3$ programme and its downstream consequences, and \verb|\ClaimStatusConditional| for results that chain through CY-A$_3$.

thinking
**Evaluating mathematical proofs**

I’m thinking about how to refine my explanation of the functor chain regarding d=3 and its relation to the CY3 chiral algebra with Omega-deformation. Perhaps I should clarify that every explicit toric CY3 model discussed here fits into this framework. It feels necessary to establish proof for CY-A2, and it seems like a secondary proof might also be needed. This sounds like a solid approach to ensure clarity and understanding!
codex
```text
## PRE-EDIT: d=3 status
statement:
- CY-A is proved only for d=2 in this chapter.
- Toric CY3 hocolim/gluing language must not advertise a constructed global chiral algebra object A_X as unconditional.
- For C^3, the manuscript may verify the functor chain against independently known target-side chiral data, but not claim a general d=3 functor construction.
depends on unconstructed object?:
Yes. Any global d=3 object A_X, Phi_3(C), or G(X) depends on the unconstructed CY-A_3 output.
environment:
- thm:cy-to-chiral
- thm:e1-universality-cy3
- thm:toric-chart-gluing
- downstream evidence/status-summary prose in cy_to_chiral.tex
claim status:
- thm:cy-to-chiral stays ProvedHere at d=2 only
- d=3 global-object/gluing claims must be Conditional or recast as candidate/model statements
dependency chain:
AGENTS.md hard boundary -> live chapter statements at lines 876, 1118, 1120ff, 1717, 1720, 1777, 1918 -> conditional CY-A_3 conjecture at conj:cy-to-chiral-d3
verdict: ACCEPT
```

```text
## PRE-EDIT: kappa
object:
- kappa_ch in CY-A_2 theorem/proposition
- MacMahon/topological exponent remark in cy3-kappa-polysemy
approved subscript:
kappa_ch only for modular characteristic of a genuine or candidate chiral algebra; no kappa-subscript for the MNOP/MacMahon topological exponent
formula:
- d=2: kappa_ch(Phi(C)) = chi^CY(C)
- local-surface topological exponent: chi_top(S)/2 only for Tot(K_S -> S)
source:
- prop:cy-kappa-d2 and surrounding remarks in cy_to_chiral.tex
- local-surface domain note at rem:cy3-kappa-polysemy
boundary checks:
- do not state chi(S)/2 outside Tot(K_S -> S)
- do not conflate kappa_ch with kappa_BKM or with the MacMahon exponent
wrong variants avoided:
- bare "kappa" for topological DT exponent
- extending chi_top(S)/2 to arbitrary CY3s or non-local-surface settings
verdict: ACCEPT
```

thinking
**Editing and patching sections**

I need to edit by applying a patch, and it’s crucial to do this carefully across multiple sections. First, I should identify the specific changes needed. Reading a bit more around theorem 32 will help me insert the proof and remarks properly. I’ll gather line contexts for a well-structured patch, focusing on sections from 32 to 76, and I might need to review the start of the theorem for accuracy in my edits.
codex
I’ve locked the status and kappa boundaries. Next edit is the core fortification pass: adding an actual proof and secondary proof route for CY-A$_2$, then downgrading the toric/d=3 advertising to candidate or conditional language, and then softening the Borcherds/bar-Euler statements to the evidence level the manuscript can currently support.
exec
/bin/zsh -lc "sed -n '1,120p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\chapter{From CY Categories to Chiral Algebras}
\label{ch:cy-to-chiral}

A Calabi--Yau category has a trace. A chiral algebra has an OPE. The trace is a map $\HH_d(\cC) \to \C$; the OPE is a distribution-valued product on sections over a punctured disc. No formal argument connects them: the trace is finite-dimensional Hochschild data, the OPE is an infinite-dimensional vertex structure on a curve. Volumes~I and~II accept a chiral algebra as given and extract its invariants: bar-cobar adjunction, the modular characteristic $\kappa_{\mathrm{ch}}$, the shadow tower, the five theorems A--D+H. The geometric source of that algebra is left unspecified. Affine Kac--Moody algebras arise from flat connections, Virasoro from reparametrizations; every other chiral algebra in the standard landscape (conifold, Hilbert schemes of K3, resolved $A_n$ singularities, local threefolds with potential) must be supplied by hand. The question is: what functor connects CY categories to chiral algebras, and what structure must it preserve?

The answer requires four constructions, each with a precise structural role. A CY category $\cC$ of dimension $d$ carries a cyclic $\Ainf$-structure, a Connes $B$-operator, and an $\bS^d$-framing on Hochschild homology. None of these are chiral algebras. The Gerstenhaber bracket on $\HH^\bullet(\cC)$ produces a Lie conformal algebra $\mathfrak{L}_\cC$; the factorization envelope on a curve $X$ promotes $\mathfrak{L}_\cC$ to a factorization algebra; the $\bS^d$-framing provides the higher operadic enhancement; and the CY trace determines the quantization. The functor $\Phi \colon \CY_d\text{-}\Cat \to \En\text{-}\mathrm{ChirAlg}$ that results is the central object of this volume. It must preserve three things: the Hochschild data (the bar complex of $\Phi(\cC)$ recovers the cyclic bar complex of $\cC$), the modular characteristic ($\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$), and the operadic level (the $\bS^d$-framing produces an $E_n$-structure, not higher).

At $d = 2$, the functor is unconditional: the $\bS^2$-framing of Kontsevich--Vlassopoulos enhances $\Fact_X(\mathfrak{L}_\cC)$ to an $\Etwo$-chiral algebra, and $\Phi$ is constructed end-to-end. At $d = 3$, a fundamental obstruction intervenes. The native $E_3$-structure on $\HH_\bullet(\cC)$ restricts to \emph{symmetric} braiding under Dunn additivity; the nonsymmetric quantum group braiding that physics demands can only be recovered through the Drinfeld center of the $\Eone$-monoidal representation category. This chapter verifies the $d = 3$ chain end-to-end for $\C^3$, where both sides are independently known (CoHA$(\C^3) \simeq Y^+(\widehat{\fgl}_1)$ on the CY side, $\cW_{1+\infty}$ at $c=1$ on the chiral side), and sets up the quiver-chart gluing that assembles the global $\Eone$-chiral algebra from local CoHA data via the factorization envelope.

% ============================================================
\section{The cyclic-to-chiral passage}
\label{sec:cyclic-to-chiral}
% ============================================================

A CY category $\cC$ of dimension $d$ carries a cyclic $\Ainf$-structure (Chapter~\ref{ch:cyclic-ainf}). The primary invariant is the cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ with its $\bS^d$-framing. The passage to chiral algebras decomposes into four steps; each consumes a specific piece of the CY data and produces a specific algebraic structure:

\begin{enumerate}[label=\textbf{Step \arabic*.}]
 \item \textbf{Cyclic $\Ainf \to$ Lie conformal algebra.} The Gerstenhaber bracket on $\HH^\bullet(\cC)$ is a graded Lie bracket of degree $-1$. The CY pairing (the nondegenerate trace $\HH_d(\cC) \to \C$) promotes this to a Lie conformal algebra $\mathfrak{L}_\cC$: the bracket becomes a $\lambda$-bracket, and the pairing becomes the invariant bilinear form. This step consumes the $\Ainf$-structure and the CY trace; it produces the ``current algebra'' of $\cC$.
 \item \textbf{Lie conformal algebra $\to$ factorization envelope.} The factorization envelope construction produces a factorization algebra $\Fact_X(\mathfrak{L}_\cC)$ on any smooth curve $X$. This step consumes the Lie conformal algebra and the curve; it produces a cosheaf on $\Ran(X)$ whose sections are the OPE data.
 \item \textbf{$\bS^d$-framing $\to$ $E_n$ enhancement.} When $d = 2$, the $\bS^2$-framing of $\HH_\bullet(\cC)$ (Kontsevich--Vlassopoulos) provides an $\Etwo$-algebra structure on the factorization algebra. This step consumes the framing; it produces the operadic enhancement that distinguishes a chiral algebra from a commutative factorization algebra.
exec
/bin/zsh -lc "sed -n '860,900p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1845,1925p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
\item \textbf{$\Eone$ universality for toric CY$_3$.} \textsc{[Proved]}
Theorem~\textup{\ref{thm:e1-universality-cy3}} establishes, by four independent pillars (abelianity of the classical bracket, one-dimensional deformation space, BV-to-$\Eone$ breaking, $R$-matrix unitarity), that toric CY$_3$ chiral algebras with $\Omega$-deformation are natively $\Eone$. Verified for $\C^3$, resolved conifold, local~$\bP^2$, and the quintic (89 tests).

\item \textbf{$\Eone \to \Etwo$ enhancement obstruction trivial.} \textsc{[Proved for tested cases]}
Corollary~\textup{\ref{cor:e1-e2-trivial}}: the enhancement obstruction vanishes for $\C^3$, the resolved conifold, and $K3 \times E$. The CY condition $g(z)g(-z) = 1$ forces the $R$-matrix unitarity that controls the obstruction (217 tests across two compute modules).

\item \textbf{Quiver-chart gluing for toric CY$_3$.} \textsc{[Proved for toric; conjectural in general]}
Wall-crossing mutations induce $\Eone$-algebra equivalences (Proposition~\textup{\ref{prop:transition-e1-equiv}}), verified for the resolved conifold and local~$\bP^2$. The bar-hocolim commutation theorem (Theorem~\textup{\ref{thm:bar-hocolim}}) guarantees $\kappa_{\mathrm{ch}}$-invariance of the global algebra. The general tilting-chart cover (Conjecture~\textup{\ref{conj:tilting-chart-cover}}) and the full $\Eone$ chart gluing (Conjecture~\textup{\ref{conj:e1-chart-gluing}}) remain conjectural.

\item \textbf{$\kappa_{\mathrm{ch}}(\C^3) = 1$: five-path verification.} \textsc{[Proved]}
Theorem~\textup{\ref{thm:kappa-c3}} establishes $\kappa_{\mathrm{ch}}(\C^3) = \kappa_{\mathrm{ch}}(H_1) = 1$ by five independent paths (Heisenberg level, MacMahon leading order, bar Euler product, DT genus-$1$ free energy, categorical Euler characteristic).

\item \textbf{$\kappa_{\mathrm{ch}}$ formula verified for fibered CY$_3$.} \textsc{[Partial]}
For $K3 \times E$: $\kappa_{\mathrm{ch}} = 3$ by additivity (Proposition~\textup{\ref{prop:categorical-euler}}). For Enriques~$\times E$: $\kappa_{\mathrm{ch}} = 2$ (72 tests via \texttt{enriques\_shadow.py}). The general formula $\kappa_{\mathrm{ch}} = \chi^{\CY}(\cC)$ for arbitrary compact CY$_3$ is conditional on the functor itself.

\item \textbf{DT/shadow correspondence at genus~$1$.} \textsc{[Verified for $\C^3$ and $K3 \times E$]}
Conjecture~\textup{\ref{conj:dt-hocolim-shadow}} predicts $F_1^{\DT}(X) = \kappa_{\mathrm{ch}}(A_X)/24$. For $\C^3$: $\kappa_{\mathrm{ch}} = 1$ gives $F_1 = 1/24$, matching the MacMahon function (Theorem~\textup{\ref{thm:kappa-c3}}). For $K3 \times E$: $\kappa_{\mathrm{BKM}} = 5$ and the genus-$1$ shadow matches.

\item \textbf{Drinfeld center identification for $\C^3$.} \textsc{[Proved]}
$\cZ(\Rep^{\Eone}(Y^+(\widehat{\fgl}_1))) \simeq \Rep^{\Etwo}(Y(\widehat{\fgl}_1)) \simeq \Rep^{\Etwo}(\cW_{1+\infty})$ (Theorem~\textup{\ref{thm:c3-drinfeld-center}}). This is the mechanism by which the non-symmetric braiding arises from the $\Eone$ structure without native $\Etwo$.
 succeeded in 52ms:

\begin{remark}[Crystal melting as bar filtration]
\label{rem:crystal-melting-bar}
The crystal melting model of Okounkov--Reshetikhin--Vafa, counting three-dimensional partitions weighted by $q^{|\pi|}$, is the degree filtration of the $\Eone$ bar complex of $\cW_{1+\infty}$: the bar degree-$n$ component $\barB^n(\cW_{1+\infty})$ counts configurations of $n$ atoms in the crystal. The MacMahon function $M(q) = \prod_{n \ge 1}(1-q^n)^{-n}$ is the bar Poincar\'e series (Proposition~\ref{prop:c3-bar-euler}). Concretely, the degree filtration $F^{\bullet} \barB(\cW_{1+\infty})$ has associated graded whose Hilbert series at degree~$n$ counts plane partitions of size~$n$, with the bar differential encoding the crystal growth rules (addition and removal of atoms at admissible sites). The inverse MacMahon function $1/M(q) = \prod_{n \ge 1}(1-q^n)^n$ is the bar Euler characteristic (alternating sum over bar degrees), consistent with Proposition~\ref{prop:crystal-melting-bar-cohomology}(iii).
\end{remark}


\begin{proposition}[Topological vertex = degree-$3$ $\Eone$ bar amplitude]
\label{prop:topological-vertex-e1-amplitude}
\ClaimStatusProvedHere{}
The topological vertex $C_{\lambda\mu\nu}(q)$ of Aganagic--Klemm--Mari\~{n}o--Vafa is the degree-$3$ $\Eone$ bar amplitude of $A_{\C^3} = \cW_{1+\infty}$, evaluated on Fock-space states $|\lambda\rangle, |\mu\rangle, |\nu\rangle$:
\[
 C_{\lambda\mu\nu}(q) \;=\; \bigl\langle \lambda,\mu,\nu \bigm| B^{\Eone}_{0,3}(A_{\C^3}) \bigr\rangle.
\]
Four independent components establish this identification.
\begin{enumerate}[label=\textup{(\alph*)}]
 \item \emph{Algebra identification.} By Schiffmann--Vasserot, $\CoHA(\C^3) = Y^+(\widehat{\fgl}_1)$; by Proch\'azka--Rap\v{c}\'ak, $Y(\widehat{\fgl}_1) = \cW_{1+\infty}$. The CY-to-chiral functor produces $A_{\C^3} = \cW_{1+\infty}$ as an $\Eone$-chiral algebra.
 \item \emph{Vertex as $3$-point amplitude.} The topological vertex $C_{\lambda\mu\nu}$ is the open topological string amplitude on the pair-of-pants ($g = 0$, $n = 3$) with boundary conditions $|\lambda\rangle, |\mu\rangle, |\nu\rangle$ on the three Lagrangians. In chiral algebra language this is the genus-$0$ degree-$3$ factorization homology amplitude $B_{0,3}(A_{\C^3})$; the $\Eone$ structure (not $\Etwo$) is used because $A_{\C^3}$ is natively $\Eone$ (Theorem~\ref{thm:e1-universality-cy3}).
 \item \emph{Gluing = sewing.} The toric diagram gluing rules (one vertex factor $C_{\lambda\mu\nu}$ per trivalent node, one propagator $(-q)^{|\lambda|}/z_\lambda$ per internal edge, sum over internal partitions) are the $\Eone$ sewing rules (Vol~I, MC5 analytic HS-sewing lane). The edge propagator $(-q)^{|\lambda|}/z_\lambda$ is the $\Eone$ bar complex pairing on $H^1(B^1)$.
 \item \emph{Refined vertex.} The refined vertex $C_{\lambda\mu\nu}(q,t)$ (Iqbal--Kozcaz--Vafa) incorporates the two independent $\Omega$-background parameters $(q,t) = (e^{-h_1}, e^{-h_2})$ of the $\Eone$ bar complex with equivariant data.
ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 4:15 PM.
tokens used
300,921
