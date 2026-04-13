# C17_bare_kappa_v3 (203s)

1. PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:569): the conventions paragraph still contained a forbidden bare `\kappa`.
EXACT edit applied: replaced `Bare $\kappa$ without subscript is forbidden in this volume; every occurrence carries an explicit qualifier.` with `Unsubscripted use is forbidden in this volume; every occurrence carries an explicit qualifier.`

2. PROBLEM at [chapters/theory/cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2188): the MacMahon-exponent warning still used a bare `\kappa` token.
EXACT edit applied: replaced `must not be given a $\kappa$ subscript.` with `must not be relabeled as $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{BKM}}$, or $\kappa_{\mathrm{fiber}}$.`

3. PROBLEM at [chapters/theory/en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:410): the Yang `R`-matrix theorem used bare `\kappa` for a coupling that is not one of the sanctioned Vol III modular characteristics.
EXACT edit applied: renamed that coupling throughout the theorem/proof from `\kappa` to `\hbar_{\mathrm{Y}}`, specifically:
`R(z) = (z \cdot \mathrm{Id} + \hbar_{\mathrm{Y}} \cdot P)/(z + \hbar_{\mathrm{Y}})` with `\hbar_{\mathrm{Y}} = h_1 h_2 h_3`,
and updated the follow-on occurrences at [chapters/theory/en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:423), [424](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:424), and [429](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:429) from `O(\kappa^2)`, `\kappa = 0`, and `symbolic expansion in \kappa` to `O(\hbar_{\mathrm{Y}}^2)`, `\hbar_{\mathrm{Y}} = 0`, and `symbolic expansion in \hbar_{\mathrm{Y}}`.

Verification: `grep -rn '\\kappa[^_{}]\\|\\kappa$' chapters/` now returns no matches.


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
session id: 019d87d0-38db-7573-9dfc-48b8c4af0776
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


Fix ALL remaining bare kappa in Vol III (AP113).
Run: grep -rn '\\kappa[^_{}]\|\\kappa$' chapters/ | head -50
Must be kappa_ch, kappa_cat, kappa_BKM, or kappa_fiber. Fix each.
mcp startup: no servers


thinking
**Planning codebase edits**

I need to operate on the codebase and follow instructions closely. This involves auditing and rectifying high-risk formula naming, using vol3-beilinson-loop and possibly cross-volume verification. The user requested that I only edit assigned files, so I'll fix things within that scope. I should start with a commentary update to acknowledge the request and plan my first step. I’ll read the live target, inspect it, and run the appropriate commands to check the files as needed.
thinking
**Preparing for the audit fix**

I should audit and fix all the relevant files. To start, I need to inspect the skill files, possibly using a parallel tool for reading the skill documentation while also checking the git status and using grep. I plan to use multi_tool_use.parallel for commentary calls, but I need to avoid system tools in parallel. Instead, I'll use exec_command in a parallel format and ensure I'm only calling tools defined in the developer messages, starting with an update.
codex
Using `vol3-beilinson-loop` and `vol3-pre-edit-verification` for a scoped AP113 sweep. I’m starting by reading the skill instructions, checking the current dirty surface, and running the exact bare-`\kappa` grep the task specifies so the edit set is evidence-driven.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git status --short' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "grep -rn '\\\\kappa["'^_{}]'"\\|\\\\kappa"'$'"' chapters/ | head -50" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
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
 succeeded in 50ms:
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
 succeeded in 51ms:
 M Makefile
 M README.md
 M calabi_yau_quantum_groups.pdf
 M chapters/connections/cy_holographic_datum_master.tex
 M chapters/connections/geometric_langlands.tex
 M chapters/connections/modular_koszul_bridge.tex
 M chapters/examples/derived_categories_cy.tex
 M chapters/examples/fukaya_categories.tex
 M chapters/examples/k3_times_e.tex
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
 M chapters/theory/en_factorization.tex
 succeeded in 52ms:
chapters/theory/cy_to_chiral.tex:2188: \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
chapters/theory/introduction.tex:569:relevant for fibered CY manifolds). Bare $\kappa$ without
chapters/theory/en_factorization.tex:410:Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
chapters/theory/en_factorization.tex:423: on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\kappa^2)$ and is antisymmetric.
chapters/theory/en_factorization.tex:424: \item At $\kappa = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
chapters/theory/en_factorization.tex:429:Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\kappa^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\kappa$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
codex
I have three target files from the mandated grep: [chapters/theory/cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex), [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex), and [chapters/theory/en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex). Next I’m reading the local context and current diffs there so the fixes stay minimal and don’t trample existing in-flight edits.
exec
/bin/zsh -lc "sed -n '548,582p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '2168,2200p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '392,438p' chapters/theory/en_factorization.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- chapters/theory/cy_to_chiral.tex chapters/theory/introduction.tex chapters/theory/en_factorization.tex' in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
 \item The Koszul dual $\cF^! = D_{\C^3}(B_{E_3}(\cF))$ carries $E_3$-chiral structure with inverted parameters $(h_1, h_2, h_3) \to (-h_1, -h_2, -h_3)$.
 \item On restriction to $\C^2 \subset \C^3$, the $E_3$ Koszul duality reduces to the $\Etwo$-chiral Koszul duality of Conjecture~\ref{conj:e2-koszul}. On further restriction to $C \subset \C^2$, it reduces to the $\Eone$-chiral Koszul duality of Vol~II.
 \item The modular characteristics satisfy $\kappa_{\mathrm{ch}}(\cF|_C) + \kappa_{\mathrm{ch}}(\cF^!|_C) = \rho_K$ (the family-dependent Koszul conductor of Vol~I Theorem~C), consistent with the lower-dimensional Koszul duality statements.
\end{enumerate}
\end{conjecture}

\begin{remark}[$E_3$ Koszul duality and quantum toroidal algebras]
\label{rem:e3-koszul-toroidal}
At the level of quantum toroidal algebras, the $E_3$ Koszul duality of Conjecture~\ref{conj:e3-koszul-duality}(ii) predicts the parameter-inversion symmetry
\[
 U_{q,t}(\widehat{\widehat{\fgl}}_1)^! \;\simeq\; U_{q^{-1}, t^{-1}}(\widehat{\widehat{\fgl}}_1),
\]
which is the conjectural Koszul duality of Chapter~\ref{ch:quantum-groups} (Definition~\ref{def:qgf-four-regimes}, toroidal regime). The $E_3$ framework provides the geometric origin of this parameter inversion: it is the Verdier duality on $\C^3$ factorization coalgebras.
\end{remark}

\begin{theorem}[The Zamolodchikov tetrahedron equation fails for the Yang $R$-matrix]
\label{thm:zte-failure}
\ClaimStatusProvedHere{}
Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
\[
 succeeded in 52ms:
This volume inherits the conventions of Volumes~I and~II; we record here the points where the CY setting introduces additional notation or where conventions differ across the literature. A comprehensive conventions appendix is Appendix~\ref{app:conventions}.

\emph{Grading.} All grading is cohomological: differentials have degree $+1$. The bar construction uses desuspension $s^{-1}$, with $|s^{-1}v| = |v| - 1$ (matching Volume~I; see signs\_and\_shifts.tex therein). The CY dimension~$d$ enters as a cohomological shift: the CY trace $\mathrm{Tr} \colon \HH_\bullet(\cC) \to k[-d]$ is a map of degree $-d$.

\emph{$E_n$ notation.} We write $E_n$ for the little $n$-disks operad (Boardman--Vogt) and $E_\infty$ for the commutative operad. Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra (Definition~\ref{def:e2-chiral-algebra}) factorizes along two holomorphic directions; its representation category is braided monoidal (Theorem~\ref{thm:lurie-e2-braided}). We write $\mathrm{FM}_k(\mathbb{C})$ for the Fulton--MacPherson compactification of $\mathrm{Conf}_k(\mathbb{C})$; this is a blowup along diagonals, not the complement of the diagonal.

\emph{Divided powers and the $\lambda$-bracket.} The translation between OPE modes $a_{(n)}b$ and the $\lambda$-bracket uses the divided-power convention $\lambda^{(n)} = \lambda^n / n!$, so $\{a_\lambda b\} = \sum_n \lambda^{(n)} a_{(n)}b$. The $\lambda$-bracket coefficient at order~$n$ is $a_{(n)}b / n!$, not $a_{(n)}b$ (Volume~I). This convention is consistent with Volumes~I and~II; when consulting references that use the Borel transform $B(K)(\lambda) = \sum \lambda^{(n)} c_n$, the $1/n!$ is already absorbed into $\lambda^{(n)}$.

\emph{CY categories.} We write $\CY_d$-$\Cat$ for the $\infty$-category of smooth $d$-dimensional CY categories. Tensor products of dg categories are derived unless stated otherwise. ``Equivalence'' means quasi-equivalence of dg categories (equivalence of associated $\infty$-categories). The Hochschild--Kostant--Rosenberg isomorphism $\HH_\bullet(D^b(\mathrm{Coh}(X))) \simeq H^*(X, \Omega^\bullet_X)$ is used freely for smooth projective varieties.

\emph{The $\kappa_\bullet$-spectrum.}
A single CY manifold admits multiple modular characteristics,
each measuring a different face of the geometry. This volume uses
subscripted $\kappa_\bullet$ throughout:
$\kappa_{\mathrm{ch}}$ (the chiral algebra modular characteristic
of Volume~I, defined as the degree-$2$ projection of $\Theta_A$),
$\kappa_{\mathrm{cat}}$ (the holomorphic Euler characteristic
$\chi(\cO_X)$, a categorical invariant),
$\kappa_{\mathrm{BKM}}$ (the half-weight of the Borcherds
automorphic form, an automorphic invariant), and
 succeeded in 51ms:
\]
At $t = 0$ (critical level): $\kappa_{\mathrm{ch}} = 0$, commutative ($\Einf$). At $t = 1$ (balanced): $\kappa_{\mathrm{ch}} = -\dim(\frakg)/2$. At $t = \infty$ (dual critical): $\kappa_{\mathrm{ch}} \to \infty$. Complementarity on the KM/free-field lane: $\kappa_{\mathrm{ch}}(A_t) + \kappa_{\mathrm{ch}}(A_t^!) = \dim(\frakg)/2$ for all~$t$ and all gauge groups.

\noindent\textit{Verification}: 137 tests in \texttt{kw\_twisted\_n4\_chiral.py}.
\end{proposition}

\begin{remark}[The BCOV constant-map formula vs the shadow formula]
\label{rem:bcov-vs-shadow}
%: structural identification correct, quantitative instantiation fails at g >= 2.
The identification BCOV $=$ shadow is \emph{structural}: the holomorphic anomaly equation IS the genus spectral sequence of an MC equation in the Costello--Li dgLa. However, the \emph{quantitative} formula $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}$ fails for compact CY$_3$ at $g \geq 2$. The BCOV constant-map formula involves the product $B_{2g} \cdot B_{2g-2}$ of two consecutive Bernoulli numbers, while the shadow formula involves $B_{2g}$ alone. Since $B_{2g-2}/B_{2g}$ varies with~$g$, no single~$\kappa_{\mathrm{ch}}$ reconciles the two at all genera. For the quintic: the effective $\kappa_{\mathrm{ch}}$ matching $F_g^{\mathrm{CM}}$ oscillates ($200, -28.6, -4.3, 2.8, -3.8$ for $g = 1, \ldots, 5$). The shadow formula applies to the \emph{uniform-weight lane} (free fields, toric CY$_3$); for compact CY$_3$, the full shadow tower $\Theta_A$ (all degrees) is needed.

\noindent\textit{Verification}: 130 tests in \texttt{bcov\_e1\_shadow\_engine.py}, including 10 tests quantifying the genus-dependent disagreement.
\end{remark}

\begin{remark}[The $\kappa_{\mathrm{ch}}$ polysemy]
\label{rem:cy3-kappa-polysemy}
The symbol~$\kappa_{\mathrm{ch}}$ appears in at least four distinct roles across the programme:
\begin{enumerate}[label=(\roman*)]
 \item $\kappa_{\mathrm{ch}}(A)$: the modular characteristic (Vol~I Theorem~D), from $F_1 = \kappa_{\mathrm{ch}} \cdot \lambda_1^{\mathrm{FP}}$.
 \item $\kappa_{\mathrm{BCOV}} = \chi_{\mathrm{top}}(X)/24$: the BCOV anomaly coefficient. Equals~$\kappa_{\mathrm{ch}}(A_X)$ for rigid compact CICYs with $h^{1,0} = 0$, but not in general.
 succeeded in 51ms:
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index 030fed4..b995783 100644
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -618,8 +618,8 @@ is the inclusion of cohomology and $p$ is the projection. The contracting
 homotopy is purely algebraic: it acts by
 $s(f_{i_0 \cdots i_q}) = f_{0 i_0 \cdots i_q}$ on \v{C}ech cochains and
 involves no PDE solving. The SDR data $(i, p, s)$ interfaces directly
-with the homotopy transfer theorem
-\textup{(}HTT, Theorem~\textup{\ref{thm:htt-general}}\textup{)},
+with the standard homotopy transfer theorem
+\textup{(}HTT\textup{)},
 transferring the $\Ainf$-structure from $\check{C}^\bullet(\cE nd(\cE))$
 to its cohomology $\Ext^\bullet(\cE, \cE)$.
 \end{theorem}
@@ -652,7 +652,7 @@ non-perturbative convergence of the resulting chiral operations
 (whether the formal series in the OPE coefficients converges to
 define honest holomorphic functions) requires separate input from
 the analytic completion programme (MC5,
-\S\ref{sec:analytic-sewing} of Vol~I). Specifically: the HTT
codex
The convention-only hits are straightforward. The `en_factorization.tex` hit is substantive: there `\kappa` is being used as a Yang `R`-matrix coupling, which is not one of the sanctioned Vol III modular characteristics, so I’m checking nearby usage before deciding whether it should be renamed away from `\kappa` entirely or mapped to an approved subscript.
exec
/bin/zsh -lc "rg -n \"\\\\kappa_\\{\\\\mathrm\\{fiber\\}\\}|\\\\kappa_\\{\\\\mathrm\\{cat\\}\\}|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}|\\\\kappa_\\{\\\\mathrm\\{BKM\\}\\}\" chapters/theory/en_factorization.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"h_1 h_2 h_3|Zamolodchikov tetrahedron|Yang \\\\R|O\\\\(\\\\kappa\\"'^2'"\\\\)|\\\\kappa = h_1 h_2 h_3|R\\(z\\) = \\(z \\\\cdot \\\\mathrm\\{Id\\}\" chapters/theory/en_factorization.tex chapters -g '"'!*.pdf'"'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "zamolodchikov_tetrahedron_engine|tetrahedron" compute/lib compute/tests' in /Users/raeez/calabi-yau-quantum-groups exited 2 in 51ms:
rg: regex parse error:
    (?:\kappa_\{\mathrm\{fiber\}\}|\kappa_\{\mathrm\{cat\}\}|\kappa_\{\mathrm\{ch\}\}|\kappa_\{\mathrm\{BKM\}\})
       ^^
error: unrecognized escape sequence
 exited 2 in 50ms:
rg: regex parse error:
    (?:h_1 h_2 h_3|Zamolodchikov tetrahedron|Yang \R|O\(\kappa\^2\)|\kappa = h_1 h_2 h_3|R\(z\) = \(z \cdot \mathrm\{Id\})
                                                  ^^
error: unrecognized escape sequence
 succeeded in 50ms:
compute/lib/e1_descent_theory.py:1531:        "tetrahedron_boundary",
compute/lib/e1_descent_theory.py:1545:        "tetrahedron_filled",
compute/tests/test_e3_two_parameter_rmatrix.py:6:        conj:parametric-tetrahedron: E_3 consistency via Zamolodchikov
compute/tests/test_e3_two_parameter_rmatrix.py:33:    Parametric tetrahedron: automatically satisfied at charge 1 (scalars commute).
compute/tests/test_e3_two_parameter_rmatrix.py:44:    parametric_tetrahedron_constraint,
compute/tests/test_e3_two_parameter_rmatrix.py:54:    verify_tetrahedron_charge1,
compute/tests/test_e3_two_parameter_rmatrix.py:324:        VERIFIED [DC] numerical check [LT] Zamolodchikov tetrahedron theory.
compute/tests/test_e3_two_parameter_rmatrix.py:381:    """Test the parametric tetrahedron equation (E_3 consistency)."""
compute/tests/test_e3_two_parameter_rmatrix.py:386:        VERIFIED [DC] parameter counting [LT] Zamolodchikov tetrahedron theory.
compute/tests/test_e3_two_parameter_rmatrix.py:388:        result = parametric_tetrahedron_constraint(1.0, 0.5, 0.7, 0.3)
compute/tests/test_e3_two_parameter_rmatrix.py:394:        VERIFIED [DC] algebraic check [LT] tetrahedron constraint equations.
compute/tests/test_e3_two_parameter_rmatrix.py:397:        result = parametric_tetrahedron_constraint(u1, v1, u2, v2)
compute/tests/test_e3_two_parameter_rmatrix.py:407:        result = parametric_tetrahedron_constraint(u1, v1, u2, v2)
compute/tests/test_e3_two_parameter_rmatrix.py:410:    def test_tetrahedron_charge1_trivial(self):
compute/tests/test_e3_two_parameter_rmatrix.py:415:        passes, max_res = verify_tetrahedron_charge1(Q1, Q2, Q3)
compute/tests/test_e3_two_parameter_rmatrix.py:418:    def test_tetrahedron_charge1_SV(self):
compute/tests/test_e3_two_parameter_rmatrix.py:426:        passes, max_res = verify_tetrahedron_charge1(q1_sv, q2_sv, q3_sv)
compute/tests/test_e3_two_parameter_rmatrix.py:427:        assert passes, f"SV tetrahedron failed: max_res = {max_res}"
compute/lib/e3_two_parameter_rmatrix.py:53:    R(u,v) = sum over vertices of a tetrahedron.
compute/lib/e3_two_parameter_rmatrix.py:92:At charge 1 (all R scalars), the tetrahedron equation reduces to a

thinking
**Investigating regex errors**

I’m looking into errors with rg that seem to stem from regex escaping in the shell. I think using fixed strings or proper quoting might help. I also need to check the engine documentation for parameter naming. It might be useful to search for "kappa" in the engine and en_factorization. I’ll consider using rg -n '\\bkappa\\b', possibly with plain. Let’s inspect the relevant lines in the engine to sort this out!
codex
I didn’t need the failed regex queries; the compute surface already identifies the tetrahedron engine as the backing witness. I’m now checking how that engine names the coupling so the manuscript edit matches executable language rather than inventing a fresh notation.
exec
/bin/zsh -lc "sed -n '230,340p' compute/tests/test_zamolodchikov_tetrahedron.py" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' compute/lib/zamolodchikov_tetrahedron_engine.py" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"kappa|coupling|h1\\*h2\\*h3|h_1 h_2 h_3|Yang R-matrix\" compute/lib/zamolodchikov_tetrahedron_engine.py compute/tests/test_zamolodchikov_tetrahedron_engine.py compute/tests/test_zamolodchikov_tetrahedron.py" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
            "S_{012} (forward) != S_{012} (reverse by YBE)"

    def test_s_at_kappa0_is_permutation(self):
        """At kappa=0, S_{012} is a permutation matrix (product of transpositions)."""
        kappa = 1e-15  # near-zero
        S = s_operator_numpy(0.0, 1.0, 3.0, kappa, 0, 1, 2, 3)
        # Should be close to a permutation (product of 3 permutations)
        # Each row and column should have exactly one entry close to 1
        for row in range(8):
            sorted_abs = np.sort(np.abs(S[row, :]))[::-1]
            assert abs(sorted_abs[0] - 1.0) < 1e-8, \
                f"S at kappa~0: row {row} max entry = {sorted_abs[0]}"


# ---------------------------------------------------------------------------
# Zamolodchikov tetrahedron equation: the main result
# ---------------------------------------------------------------------------

class TestZamolodchikovTetrahedron:
    """ZTE (3-simplex): the Yang R-matrix does NOT satisfy it."""
 succeeded in 52ms:
"""Zamolodchikov tetrahedron equation for the Yang R-matrix.

MATHEMATICAL FRAMEWORK:

The Zamolodchikov tetrahedron equation (ZTE) is the 3-dimensional analogue
of the Yang-Baxter equation (YBE). While YBE governs consistency of
2-particle scattering in 1+1 dimensions (2-simplex), ZTE governs consistency
of 3-particle scattering in 2+1 dimensions (3-simplex / tetrahedron).

SETUP:
    V = C^2 = span{|0>, |1>} (the charge-2 Fock space, with basis
    elements corresponding to partitions (2) and (1,1)).

    R-matrix: R(z) = (z*Id + kappa*P) / (z + kappa)  on  V tensor V
    where P is the permutation (flip) operator and kappa = h1*h2*h3.

    This is the rational Yang R-matrix, the simplest solution of YBE.

FACE S-OPERATOR (3-SIMPLEX OPERATOR):
    For each triangular face (i,j,k) of the tetrahedron with spectral
 succeeded in 52ms:
compute/tests/test_zamolodchikov_tetrahedron.py:3:Verifies the complete 3-simplex analysis for the Yang R-matrix
compute/tests/test_zamolodchikov_tetrahedron.py:4:R(z) = (z*Id + kappa*P)/(z+kappa) on V = C^2.
compute/tests/test_zamolodchikov_tetrahedron.py:10:  4. Obstruction is O(kappa^2), antisymmetric, rank 4 on charge-2.
compute/tests/test_zamolodchikov_tetrahedron.py:11:  5. At kappa=0, ZTE IS satisfied (Kapranov-Voevodsky permutation limit).
compute/tests/test_zamolodchikov_tetrahedron.py:14:The Yang R-matrix is intrinsically 2-dimensional: it solves the 2-simplex
compute/tests/test_zamolodchikov_tetrahedron.py:21:[SC] Scaling analysis: obstruction ~ kappa^2 from log-log fit.
compute/tests/test_zamolodchikov_tetrahedron.py:50:    """Basic properties of the Yang R-matrix."""
compute/tests/test_zamolodchikov_tetrahedron.py:54:        kappa = -6.0
compute/tests/test_zamolodchikov_tetrahedron.py:56:            R_z = _yang_r_numpy(z, kappa)
compute/tests/test_zamolodchikov_tetrahedron.py:57:            R_neg = _yang_r_numpy(-z, kappa)
compute/tests/test_zamolodchikov_tetrahedron.py:60:                f"R(z)*R(-z) != Id at z={z}, kappa={kappa}"
compute/tests/test_zamolodchikov_tetrahedron.py:64:        kappa = -6.0
compute/tests/test_zamolodchikov_tetrahedron.py:65:        R0 = _yang_r_numpy(0.0, kappa)
compute/tests/test_zamolodchikov_tetrahedron.py:74:        kappa = -6.0
compute/tests/test_zamolodchikov_tetrahedron.py:75:        R_big = _yang_r_numpy(1e10, kappa)
compute/tests/test_zamolodchikov_tetrahedron.py:81:        kappa = -6.0
compute/tests/test_zamolodchikov_tetrahedron.py:83:        R = _yang_r_numpy(z, kappa)
compute/tests/test_zamolodchikov_tetrahedron.py:98:        kappa = Rational(-6)
compute/tests/test_zamolodchikov_tetrahedron.py:100:        R_sym = yang_r_matrix_4x4(z, kappa)
compute/tests/test_zamolodchikov_tetrahedron.py:112:    """YBE: the 2-simplex equation that the Yang R-matrix satisfies."""

thinking
**Investigating notation choices**

I’m considering the directive related to actual kappa invariants. It seems the theorem's application might be rogue and needs reassessment. I should really decide how to proceed. I'll take a closer look to see if there’s existing notation in en_factorization or anywhere else that uses `\hbar_{\mathrm{Y}}` or another parameter for the Yang R-matrix. Maybe a search for `\hbar` could yield some useful insights.
codex
The tetrahedron engine itself still uses plain `kappa` internally, but the user constrained edits to the chapter files. I’m checking the surrounding manuscript notation so I can make the chapter truthful without broadening scope into the compute layer.
exec
/bin/zsh -lc "rg -n \"\\\\hbar|\\\\varkappa|Yangian parameter|Planck constant|deformation parameter\" chapters/theory/en_factorization.tex chapters/theory chapters/examples -g '"'!*.pdf'"'" in /Users/raeez/calabi-yau-quantum-groups exited 2 in 52ms:
rg: regex parse error:
    (?:\hbar|\varkappa|Yangian parameter|Planck constant|deformation parameter)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '1128,1185p' compute/lib/zamolodchikov_tetrahedron_engine.py" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"kappa_{\\\\mathrm\\{Y\\}}|kappa_Y|kappa parameter\" chapters -g '"'!*.pdf'"'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
        """Embed R_{ii,jj}(z) on charge-1 sector of V^{otimes 3} (3x3)."""
        M = eye(3)
        for col_idx, s in enumerate(states_c1):
            bi, bj = s[ii], s[jj]
            if bi == bj:
                continue
            partner = list(s)
            partner[ii], partner[jj] = partner[jj], partner[ii]
            partner_idx = index_c1[tuple(partner)]
            M[col_idx, col_idx] = z / (z + kap)
            M[partner_idx, col_idx] = kap / (z + kap)
        return M

    R01 = r_embed_c1_3(u - v, 0, 1)
    R02 = r_embed_c1_3(u, 0, 2)
    R12 = r_embed_c1_3(v, 1, 2)

    lhs = R01 * R02 * R12
    rhs = R12 * R02 * R01
    diff = (lhs - rhs).applyfunc(lambda x: cancel(expand(x)))
 exited 2 in 52ms:
rg: regex parse error:
    (?:kappa_{\mathrm\{Y\}}|kappa_Y|kappa parameter)
              ^
error: repetition quantifier expects a valid decimal

thinking
**Configuring rg command**

I need to use the `rg` command with fixed strings or handle escaped backslashes properly. Specifically, I should run it like this: `rg -n -F "\\hbar" chapters/...`. I’ll make sure everything is set up correctly for my search. It’s essential to get these details right so that I can find what I'm looking for without any issues! Let’s go ahead and execute this command now.
exec
/bin/zsh -lc "rg -n -F '\\\\varkappa' chapters/theory/en_factorization.tex chapters/theory chapters/examples" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F '\\\\hbar' chapters/theory/en_factorization.tex chapters/theory chapters/examples" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Planck constant' chapters/theory chapters/examples" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -F 'Yangian parameter' chapters/theory chapters/examples" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 exited 1 in 51ms:

 exited 1 in 52ms:

 succeeded in 52ms:
chapters/theory/quantum_chiral_algebras.tex:428: \item $\Etwo$ on $\C^2$: one spectral parameter $z_2$ (the Yangian parameter $u$);




thinking
**Considering mathematical notation changes**

I’m looking to rename elements like \hbar or \varkappa since they don’t exist. Maybe I could use `\eta_{\mathrm{Y}}` or `\mu`, but kappa names must be approved. In the theorem, I could denote something like `\kappa_{\mathrm{fiber}} = h_1 h_2 h_3`, but that doesn't accurately represent the lattice rank. I think the most truthful approach is to rewrite the theorem without a Greek letter by using `\lambda := h_1 h_2 h_3`. This way, I avoid using bare `\kappa` and remain truthful.
thinking
**Verifying notation consistency**

I need to run a grep after making edits to ensure no unwanted letters remain. Since line numbers could shift, I'll verify and look for new instances across files. Including a pre-edit block in my commentary is crucial because editing kappa is risky. I should detail the exact object and formula used, ensuring boundary checks are done. 

For renaming, I might consider using `\lambda_{\mathrm{Y}}`, but I have to think some more. Alternatively, `\eta_{\mathrm{Y}}` looks like a minimal option.
thinking
**Considering notation for clarity**

I’m wondering if `\hbar_{\mathrm{Y}}` might be a better choice since the documentation refers to it as the Planck constant. This could make the notation more semantically appropriate. It's essential to clarify my choices to ensure they fit within the context and don’t cause confusion. I need to weigh my options carefully to pick the most suitable notation that communicates the intended meaning clearly. I'll keep this in mind as I move forward!
thinking
**Checking edits and line numbers**

I think I need to check the line numbers and exact edits with `apply_patch`. But before jumping into editing, I should comment on the update and include a PRE-EDIT block. I'll also need to inspect specific lines, particularly around the intro and `cy_to_chiral` line numbers, using `nl -ba`. Additionally, I ought to figure out the exact line numbers in `en_factorization`. So, I'll gather those line numbers first.
codex
```text
## PRE-EDIT: kappa
object:
1. Vol III convention paragraph in introduction.tex governing allowed kappa symbols.
2. CY3 kappa-polysemy remark in cy_to_chiral.tex, specifically the MacMahon-exponent warning.
3. Yang R-matrix theorem in en_factorization.tex where bare \kappa is currently a coupling, not a modular characteristic.

approved subscript:
Only \kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}} are allowed for actual Vol III modular-characteristic symbols. Non-modular couplings must be renamed away from \kappa.

formula:
1. Convention prose should refer only to subscripted forms or to “unsubscripted use”.
2. MacMahon exponent warning should name the approved kappa-symbol family explicitly, without a bare \kappa token.
3. Yang R-matrix coupling will be rewritten as \hbar_{\mathrm{Y}} = h_1 h_2 h_3, with every O(\kappa^2) / \kappa=0 occurrence updated consistently.

source:
Live manuscript context in chapters/theory/introduction.tex, chapters/theory/cy_to_chiral.tex, chapters/theory/en_factorization.tex; compute witness naming checked in compute/lib/zamolodchikov_tetrahedron_engine.py.

boundary checks:
- Do not relabel the MacMahon exponent as any modular characteristic.
- Do not assign \kappa_{\mathrm{fiber}}/\kappa_{\mathrm{cat}}/\kappa_{\mathrm{ch}}/\kappa_{\mathrm{BKM}} to the Yang R-matrix coupling, because that would be false.
- Keep edits scoped to the three chapter files named by the grep.
- Post-edit grep over chapters/ must return no bare \kappa hits.

wrong variants avoided:
- Leaving policy prose with a literal bare \kappa token.
- Reusing an approved modular-characteristic subscript for the Yang R-matrix coupling.
- Expanding scope into compute/tests despite the file constraint.

verdict: ACCEPT
```
exec
/bin/zsh -lc "nl -ba chapters/theory/cy_to_chiral.tex | sed -n '2180,2195p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
  2180	\end{remark}
  2181	
  2182	\begin{remark}[The $\kappa_{\mathrm{ch}}$ polysemy]
  2183	\label{rem:cy3-kappa-polysemy}
  2184	The symbol~$\kappa_{\mathrm{ch}}$ appears in at least four distinct roles across the programme:
  2185	\begin{enumerate}[label=(\roman*)]
  2186	 \item $\kappa_{\mathrm{ch}}(A)$: the modular characteristic (Vol~I Theorem~D), from $F_1 = \kappa_{\mathrm{ch}} \cdot \lambda_1^{\mathrm{FP}}$.
  2187	 \item $\kappa_{\mathrm{BCOV}} = \chi_{\mathrm{top}}(X)/24$: the BCOV anomaly coefficient. Equals~$\kappa_{\mathrm{ch}}(A_X)$ for rigid compact CICYs with $h^{1,0} = 0$, but not in general.
  2188	 \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
  2189	 \item $\kappa_{\mathrm{BKM}}$: the weight of the BKM automorphic form. For $K3 \times E$: $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$.
  2190	\end{enumerate}
  2191	These coincide for Heisenberg ($\kappa_{\mathrm{ch}} = k$) and Virasoro ($\kappa_{\mathrm{ch}} = c/2$) but diverge for general CY$_3$. The quintic alone admits three values: $-25/3$, $-100$, $200$.
  2192	\end{remark}
  2193	
  2194	
  2195	\begin{proposition}[CoHA of non-CY threefolds]
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '564,574p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/en_factorization.tex | sed -n '408,430p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
   564	$\kappa_{\mathrm{cat}}$ (the holomorphic Euler characteristic
   565	$\chi(\cO_X)$, a categorical invariant),
   566	$\kappa_{\mathrm{BKM}}$ (the half-weight of the Borcherds
   567	automorphic form, an automorphic invariant), and
   568	$\kappa_{\mathrm{fiber}}$ (the lattice rank of the fiber,
   569	relevant for fibered CY manifolds). Bare $\kappa$ without
   570	subscript is forbidden in this volume; every occurrence carries
   571	an explicit qualifier.
   572	
   573	\emph{Operadic terminology.}
   574	Following Volume~I, the word ``degree'' is used universally
 succeeded in 52ms:
   408	\label{thm:zte-failure}
   409	\ClaimStatusProvedHere{}
   410	Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
   411	\[
   412	 S_{ijk}(u_i, u_j, u_k) \;=\; R_{ij}(u_i - u_j) \, R_{ik}(u_i - u_k) \, R_{jk}(u_j - u_k)
   413	\]
   414	acting on $(\C^2)^{\otimes 3}$. Then:
   415	\begin{enumerate}[label=\textup{(\roman*)}]
   416	 \item The Yang--Baxter equation $R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}$ is satisfied (positive control).
   417	 \item The Zamolodchikov tetrahedron equation
   418	 \[
   419	  S_{012} \, S_{013} \, S_{023} \, S_{123}
   420	  \;=\;
   421	  S_{123} \, S_{023} \, S_{013} \, S_{012}
   422	 \]
   423	 on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\kappa^2)$ and is antisymmetric.
   424	 \item At $\kappa = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
   425	\end{enumerate}
   426	\end{theorem}
   427	

thinking
**Planning patch edits**

I need to edit some specific lines, and I wonder if I can do them all in one patch. It seems like I should preserve only the files that are assigned. To do this, I plan to use the apply_patch function. Before I make any edits, I want to provide an update to explain what changes I'm making. It's all about being clear and organized for the user!
codex
I’ve locked the three exact edit sites. The patch will do three things only: remove the literal bare-`\kappa` warning token in the conventions paragraph, make the MacMahon warning name the approved kappa-family explicitly, and rename the Yang `R`-matrix coupling away from `\kappa` so it no longer masquerades as a modular characteristic.
file update
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex
@@ -2187,3 +2187,3 @@
  \item $\kappa_{\mathrm{BCOV}} = \chi_{\mathrm{top}}(X)/24$: the BCOV anomaly coefficient. Equals~$\kappa_{\mathrm{ch}}(A_X)$ for rigid compact CICYs with $h^{1,0} = 0$, but not in general.
- \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
+ \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be relabeled as $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{BKM}}$, or $\kappa_{\mathrm{fiber}}$.
  \item $\kappa_{\mathrm{BKM}}$: the weight of the BKM automorphic form. For $K3 \times E$: $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$.
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex
@@ -409,3 +409,3 @@
 \ClaimStatusProvedHere{}
-Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
+Let $R(z) = (z \cdot \mathrm{Id} + \hbar_{\mathrm{Y}} \cdot P)/(z + \hbar_{\mathrm{Y}})$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\hbar_{\mathrm{Y}} = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
 \[
@@ -422,4 +422,4 @@
  \]
- on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\kappa^2)$ and is antisymmetric.
- \item At $\kappa = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
+ on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\hbar_{\mathrm{Y}}^2)$ and is antisymmetric.
+ \item At $\hbar_{\mathrm{Y}} = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
 \end{enumerate}
@@ -428,3 +428,3 @@
 \begin{proof}
-Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\kappa^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\kappa$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
+Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\hbar_{\mathrm{Y}}^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\hbar_{\mathrm{Y}}$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
 \end{proof}
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
@@ -568,5 +568,5 @@
 $\kappa_{\mathrm{fiber}}$ (the lattice rank of the fiber,
-relevant for fibered CY manifolds). Bare $\kappa$ without
-subscript is forbidden in this volume; every occurrence carries
-an explicit qualifier.
+relevant for fibered CY manifolds). Unsubscripted use is
+forbidden in this volume; every occurrence carries an explicit
+qualifier.
 
apply_patch(auto_approved=true) exited 0 in 31ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex
M /Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex
file update:
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index b9957838e3d27b442afd949c2bd3b8c375e03292..0bc4612a3d656df75158e3068cd130f62961ca50
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -2185,7 +2185,7 @@
 \begin{enumerate}[label=(\roman*)]
  \item $\kappa_{\mathrm{ch}}(A)$: the modular characteristic (Vol~I Theorem~D), from $F_1 = \kappa_{\mathrm{ch}} \cdot \lambda_1^{\mathrm{FP}}$.
  \item $\kappa_{\mathrm{BCOV}} = \chi_{\mathrm{top}}(X)/24$: the BCOV anomaly coefficient. Equals~$\kappa_{\mathrm{ch}}(A_X)$ for rigid compact CICYs with $h^{1,0} = 0$, but not in general.
- \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
+ \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be relabeled as $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{BKM}}$, or $\kappa_{\mathrm{fiber}}$.
  \item $\kappa_{\mathrm{BKM}}$: the weight of the BKM automorphic form. For $K3 \times E$: $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$.
 \end{enumerate}
 These coincide for Heisenberg ($\kappa_{\mathrm{ch}} = k$) and Virasoro ($\kappa_{\mathrm{ch}} = c/2$) but diverge for general CY$_3$. The quintic alone admits three values: $-25/3$, $-100$, $200$.
diff --git a/chapters/theory/en_factorization.tex b/chapters/theory/en_factorization.tex
index 451cd4827448c498e95874300cd3576d00d3016f..c753f65a2518fff0639e77908925919845ac3641
--- a/chapters/theory/en_factorization.tex
+++ b/chapters/theory/en_factorization.tex
@@ -407,7 +407,7 @@
 \begin{theorem}[The Zamolodchikov tetrahedron equation fails for the Yang $R$-matrix]
 \label{thm:zte-failure}
 \ClaimStatusProvedHere{}
-Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
+Let $R(z) = (z \cdot \mathrm{Id} + \hbar_{\mathrm{Y}} \cdot P)/(z + \hbar_{\mathrm{Y}})$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\hbar_{\mathrm{Y}} = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
 \[
  S_{ijk}(u_i, u_j, u_k) \;=\; R_{ij}(u_i - u_j) \, R_{ik}(u_i - u_k) \, R_{jk}(u_j - u_k)
 \]
@@ -420,13 +420,13 @@
   \;=\;
   S_{123} \, S_{023} \, S_{013} \, S_{012}
  \]
- on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\kappa^2)$ and is antisymmetric.
- \item At $\kappa = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
+ on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\hbar_{\mathrm{Y}}^2)$ and is antisymmetric.
+ \item At $\hbar_{\mathrm{Y}} = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\kappa^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\kappa$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
+Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\hbar_{\mathrm{Y}}^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\hbar_{\mathrm{Y}}$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
 \end{proof}
 
 \begin{remark}[Consequence for $E_3$-chiral structure]
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index be80ef202059e41717186f92909e8a4a60c6d3f9..9987e7852909b14f7237b8226056f9c1ce16c4a3
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -566,9 +566,9 @@
 $\kappa_{\mathrm{BKM}}$ (the half-weight of the Borcherds
 automorphic form, an automorphic invariant), and
 $\kappa_{\mathrm{fiber}}$ (the lattice rank of the fiber,
-relevant for fibered CY manifolds). Bare $\kappa$ without
-subscript is forbidden in this volume; every occurrence carries
-an explicit qualifier.
+relevant for fibered CY manifolds). Unsubscripted use is
+forbidden in this volume; every occurrence carries an explicit
+qualifier.
 
 \emph{Operadic terminology.}
 Following Volume~I, the word ``degree'' is used universally

file update:
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index b9957838e3d27b442afd949c2bd3b8c375e03292..0bc4612a3d656df75158e3068cd130f62961ca50
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -2185,7 +2185,7 @@
 \begin{enumerate}[label=(\roman*)]
  \item $\kappa_{\mathrm{ch}}(A)$: the modular characteristic (Vol~I Theorem~D), from $F_1 = \kappa_{\mathrm{ch}} \cdot \lambda_1^{\mathrm{FP}}$.
  \item $\kappa_{\mathrm{BCOV}} = \chi_{\mathrm{top}}(X)/24$: the BCOV anomaly coefficient. Equals~$\kappa_{\mathrm{ch}}(A_X)$ for rigid compact CICYs with $h^{1,0} = 0$, but not in general.
- \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
+ \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be relabeled as $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{BKM}}$, or $\kappa_{\mathrm{fiber}}$.
  \item $\kappa_{\mathrm{BKM}}$: the weight of the BKM automorphic form. For $K3 \times E$: $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$.
 \end{enumerate}
 These coincide for Heisenberg ($\kappa_{\mathrm{ch}} = k$) and Virasoro ($\kappa_{\mathrm{ch}} = c/2$) but diverge for general CY$_3$. The quintic alone admits three values: $-25/3$, $-100$, $200$.
diff --git a/chapters/theory/en_factorization.tex b/chapters/theory/en_factorization.tex
index 451cd4827448c498e95874300cd3576d00d3016f..c753f65a2518fff0639e77908925919845ac3641
--- a/chapters/theory/en_factorization.tex
+++ b/chapters/theory/en_factorization.tex
@@ -407,7 +407,7 @@
 \begin{theorem}[The Zamolodchikov tetrahedron equation fails for the Yang $R$-matrix]
 \label{thm:zte-failure}
 \ClaimStatusProvedHere{}
-Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
+Let $R(z) = (z \cdot \mathrm{Id} + \hbar_{\mathrm{Y}} \cdot P)/(z + \hbar_{\mathrm{Y}})$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\hbar_{\mathrm{Y}} = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
 \[
  S_{ijk}(u_i, u_j, u_k) \;=\; R_{ij}(u_i - u_j) \, R_{ik}(u_i - u_k) \, R_{jk}(u_j - u_k)
 \]
@@ -420,13 +420,13 @@
   \;=\;
   S_{123} \, S_{023} \, S_{013} \, S_{012}
  \]
- on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\kappa^2)$ and is antisymmetric.
- \item At $\kappa = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
+ on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\hbar_{\mathrm{Y}}^2)$ and is antisymmetric.
+ \item At $\hbar_{\mathrm{Y}} = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\kappa^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\kappa$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
+Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\hbar_{\mathrm{Y}}^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\hbar_{\mathrm{Y}}$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
 \end{proof}
 
 \begin{remark}[Consequence for $E_3$-chiral structure]
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index be80ef202059e41717186f92909e8a4a60c6d3f9..9987e7852909b14f7237b8226056f9c1ce16c4a3
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -566,9 +566,9 @@
 $\kappa_{\mathrm{BKM}}$ (the half-weight of the Borcherds
 automorphic form, an automorphic invariant), and
 $\kappa_{\mathrm{fiber}}$ (the lattice rank of the fiber,
-relevant for fibered CY manifolds). Bare $\kappa$ without
-subscript is forbidden in this volume; every occurrence carries
-an explicit qualifier.
+relevant for fibered CY manifolds). Unsubscripted use is
+forbidden in this volume; every occurrence carries an explicit
+qualifier.
 
 \emph{Operadic terminology.}
 Following Volume~I, the word ``degree'' is used universally

codex
The patch is in. I’m running the mandated grep again, plus a full bare-`\kappa` sweep over `chapters/`, so the stop condition is evidence rather than assumption.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '566,572p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/en_factorization.tex | sed -n '410,430p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/cy_to_chiral.tex | sed -n '2186,2190p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "grep -rn '\\\\kappa["'^_{}]'"\\|\\\\kappa"'$'"' chapters/ | head -50" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "grep -rn '\\\\kappa["'^_{}]'"\\|\\\\kappa"'$'"' chapters/" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
   566	$\kappa_{\mathrm{BKM}}$ (the half-weight of the Borcherds
   567	automorphic form, an automorphic invariant), and
   568	$\kappa_{\mathrm{fiber}}$ (the lattice rank of the fiber,
   569	relevant for fibered CY manifolds). Unsubscripted use is
   570	forbidden in this volume; every occurrence carries an explicit
   571	qualifier.
   572	
 succeeded in 51ms:
   410	Let $R(z) = (z \cdot \mathrm{Id} + \hbar_{\mathrm{Y}} \cdot P)/(z + \hbar_{\mathrm{Y}})$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\hbar_{\mathrm{Y}} = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
   411	\[
   412	 S_{ijk}(u_i, u_j, u_k) \;=\; R_{ij}(u_i - u_j) \, R_{ik}(u_i - u_k) \, R_{jk}(u_j - u_k)
   413	\]
   414	acting on $(\C^2)^{\otimes 3}$. Then:
   415	\begin{enumerate}[label=\textup{(\roman*)}]
   416	 \item The Yang--Baxter equation $R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}$ is satisfied (positive control).
   417	 \item The Zamolodchikov tetrahedron equation
   418	 \[
   419	  S_{012} \, S_{013} \, S_{023} \, S_{123}
   420	  \;=\;
   421	  S_{123} \, S_{023} \, S_{013} \, S_{012}
   422	 \]
   423	 on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\hbar_{\mathrm{Y}}^2)$ and is antisymmetric.
   424	 \item At $\hbar_{\mathrm{Y}} = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
   425	\end{enumerate}
   426	\end{theorem}
   427	
   428	\begin{proof}
   429	Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\hbar_{\mathrm{Y}}^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\hbar_{\mathrm{Y}}$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
 succeeded in 51ms:
  2186	 \item $\kappa_{\mathrm{ch}}(A)$: the modular characteristic (Vol~I Theorem~D), from $F_1 = \kappa_{\mathrm{ch}} \cdot \lambda_1^{\mathrm{FP}}$.
  2187	 \item $\kappa_{\mathrm{BCOV}} = \chi_{\mathrm{top}}(X)/24$: the BCOV anomaly coefficient. Equals~$\kappa_{\mathrm{ch}}(A_X)$ for rigid compact CICYs with $h^{1,0} = 0$, but not in general.
  2188	 \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be relabeled as $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{BKM}}$, or $\kappa_{\mathrm{fiber}}$.
  2189	 \item $\kappa_{\mathrm{BKM}}$: the weight of the BKM automorphic form. For $K3 \times E$: $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$.
  2190	\end{enumerate}
 succeeded in 51ms:

 exited 1 in 51ms:

file update:
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index b9957838e3d27b442afd949c2bd3b8c375e03292..0bc4612a3d656df75158e3068cd130f62961ca50
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -2185,7 +2185,7 @@
 \begin{enumerate}[label=(\roman*)]
  \item $\kappa_{\mathrm{ch}}(A)$: the modular characteristic (Vol~I Theorem~D), from $F_1 = \kappa_{\mathrm{ch}} \cdot \lambda_1^{\mathrm{FP}}$.
  \item $\kappa_{\mathrm{BCOV}} = \chi_{\mathrm{top}}(X)/24$: the BCOV anomaly coefficient. Equals~$\kappa_{\mathrm{ch}}(A_X)$ for rigid compact CICYs with $h^{1,0} = 0$, but not in general.
- \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
+ \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be relabeled as $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{BKM}}$, or $\kappa_{\mathrm{fiber}}$.
  \item $\kappa_{\mathrm{BKM}}$: the weight of the BKM automorphic form. For $K3 \times E$: $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$.
 \end{enumerate}
 These coincide for Heisenberg ($\kappa_{\mathrm{ch}} = k$) and Virasoro ($\kappa_{\mathrm{ch}} = c/2$) but diverge for general CY$_3$. The quintic alone admits three values: $-25/3$, $-100$, $200$.
diff --git a/chapters/theory/en_factorization.tex b/chapters/theory/en_factorization.tex
index 451cd4827448c498e95874300cd3576d00d3016f..c753f65a2518fff0639e77908925919845ac3641
--- a/chapters/theory/en_factorization.tex
+++ b/chapters/theory/en_factorization.tex
@@ -407,7 +407,7 @@
 \begin{theorem}[The Zamolodchikov tetrahedron equation fails for the Yang $R$-matrix]
 \label{thm:zte-failure}
 \ClaimStatusProvedHere{}
-Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
+Let $R(z) = (z \cdot \mathrm{Id} + \hbar_{\mathrm{Y}} \cdot P)/(z + \hbar_{\mathrm{Y}})$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\hbar_{\mathrm{Y}} = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
 \[
  S_{ijk}(u_i, u_j, u_k) \;=\; R_{ij}(u_i - u_j) \, R_{ik}(u_i - u_k) \, R_{jk}(u_j - u_k)
 \]
@@ -420,13 +420,13 @@
   \;=\;
   S_{123} \, S_{023} \, S_{013} \, S_{012}
  \]
- on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\kappa^2)$ and is antisymmetric.
- \item At $\kappa = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
+ on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\hbar_{\mathrm{Y}}^2)$ and is antisymmetric.
+ \item At $\hbar_{\mathrm{Y}} = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\kappa^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\kappa$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
+Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\hbar_{\mathrm{Y}}^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\hbar_{\mathrm{Y}}$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
 \end{proof}
 
 \begin{remark}[Consequence for $E_3$-chiral structure]
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index be80ef202059e41717186f92909e8a4a60c6d3f9..9987e7852909b14f7237b8226056f9c1ce16c4a3
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -566,9 +566,9 @@
 $\kappa_{\mathrm{BKM}}$ (the half-weight of the Borcherds
 automorphic form, an automorphic invariant), and
 $\kappa_{\mathrm{fiber}}$ (the lattice rank of the fiber,
-relevant for fibered CY manifolds). Bare $\kappa$ without
-subscript is forbidden in this volume; every occurrence carries
-an explicit qualifier.
+relevant for fibered CY manifolds). Unsubscripted use is
+forbidden in this volume; every occurrence carries an explicit
+qualifier.
 
 \emph{Operadic terminology.}
 Following Volume~I, the word ``degree'' is used universally




thinking
**Inspecting changes and verifications**

I need to check for expected changes and consider verification. Running a line-specific grep might be enough to catch any issues, but I need to ensure there aren’t any bare \kappa in the chapters. The grep command returning an exit code of 1 indicates no output, which is good for my search. I wonder if there could be occurrences in comments that need attention. Overall, I should enumerate problems with exact edits as requested by the user.
thinking
**Identifying problems with edits**

I need to provide a concise yet explicit report on the issues found. 

1. PROBLEM at [introduction.tex](...:569): The conventions paragraph still contained a forbidden bare `\kappa`. I changed it from “Bare $\kappa$ without subscript is forbidden…” to “Unsubscripted use is forbidden…” 

2. PROBLEM at [cy_to_chiral.tex](...:2188): There's a warning using a bare `\kappa`. I revised it from “must not be given a $\kappa$ subscript” to more specific labeling.

3. PROBLEM at multiple lines in [en_factorization.tex]: The Yang `R`-matrix theorem improperly used bare `\kappa`.
thinking
**Considering verification findings**

I need to note that the verification attempt using `grep -rn ...` didn't return any matches. I think I should keep things straightforward, maybe avoiding nested bullet points. A numbered list of my findings could work well, along with a brief summary afterward. I'm also thinking about making sure I include clickable links for easy access. Let’s craft this in a way that’s as concise as possible while ensuring everything is clear and precise!
codex
1. PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:569): the conventions paragraph still contained a forbidden bare `\kappa`.
EXACT edit applied: replaced `Bare $\kappa$ without subscript is forbidden in this volume; every occurrence carries an explicit qualifier.` with `Unsubscripted use is forbidden in this volume; every occurrence carries an explicit qualifier.`

2. PROBLEM at [chapters/theory/cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2188): the MacMahon-exponent warning still used a bare `\kappa` token.
EXACT edit applied: replaced `must not be given a $\kappa$ subscript.` with `must not be relabeled as $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{BKM}}$, or $\kappa_{\mathrm{fiber}}$.`

3. PROBLEM at [chapters/theory/en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:410): the Yang `R`-matrix theorem used bare `\kappa` for a coupling that is not one of the sanctioned Vol III modular characteristics.
EXACT edit applied: renamed that coupling throughout the theorem/proof from `\kappa` to `\hbar_{\mathrm{Y}}`, specifically:
`R(z) = (z \cdot \mathrm{Id} + \hbar_{\mathrm{Y}} \cdot P)/(z + \hbar_{\mathrm{Y}})` with `\hbar_{\mathrm{Y}} = h_1 h_2 h_3`,
and updated the follow-on occurrences at [chapters/theory/en_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:423), [424](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:424), and [429](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:429) from `O(\kappa^2)`, `\kappa = 0`, and `symbolic expansion in \kappa` to `O(\hbar_{\mathrm{Y}}^2)`, `\hbar_{\mathrm{Y}} = 0`, and `symbolic expansion in \hbar_{\mathrm{Y}}`.

Verification: `grep -rn '\\kappa[^_{}]\\|\\kappa$' chapters/` now returns no matches.
file update:
diff --git a/chapters/theory/cy_to_chiral.tex b/chapters/theory/cy_to_chiral.tex
index b9957838e3d27b442afd949c2bd3b8c375e03292..0bc4612a3d656df75158e3068cd130f62961ca50
--- a/chapters/theory/cy_to_chiral.tex
+++ b/chapters/theory/cy_to_chiral.tex
@@ -2185,7 +2185,7 @@
 \begin{enumerate}[label=(\roman*)]
  \item $\kappa_{\mathrm{ch}}(A)$: the modular characteristic (Vol~I Theorem~D), from $F_1 = \kappa_{\mathrm{ch}} \cdot \lambda_1^{\mathrm{FP}}$.
  \item $\kappa_{\mathrm{BCOV}} = \chi_{\mathrm{top}}(X)/24$: the BCOV anomaly coefficient. Equals~$\kappa_{\mathrm{ch}}(A_X)$ for rigid compact CICYs with $h^{1,0} = 0$, but not in general.
- \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
+ \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be relabeled as $\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{BKM}}$, or $\kappa_{\mathrm{fiber}}$.
  \item $\kappa_{\mathrm{BKM}}$: the weight of the BKM automorphic form. For $K3 \times E$: $\kappa_{\mathrm{BKM}} = \mathrm{wt}(\Delta_5) = 5$.
 \end{enumerate}
 These coincide for Heisenberg ($\kappa_{\mathrm{ch}} = k$) and Virasoro ($\kappa_{\mathrm{ch}} = c/2$) but diverge for general CY$_3$. The quintic alone admits three values: $-25/3$, $-100$, $200$.
diff --git a/chapters/theory/en_factorization.tex b/chapters/theory/en_factorization.tex
index 451cd4827448c498e95874300cd3576d00d3016f..c753f65a2518fff0639e77908925919845ac3641
--- a/chapters/theory/en_factorization.tex
+++ b/chapters/theory/en_factorization.tex
@@ -407,7 +407,7 @@
 \begin{theorem}[The Zamolodchikov tetrahedron equation fails for the Yang $R$-matrix]
 \label{thm:zte-failure}
 \ClaimStatusProvedHere{}
-Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
+Let $R(z) = (z \cdot \mathrm{Id} + \hbar_{\mathrm{Y}} \cdot P)/(z + \hbar_{\mathrm{Y}})$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\hbar_{\mathrm{Y}} = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
 \[
  S_{ijk}(u_i, u_j, u_k) \;=\; R_{ij}(u_i - u_j) \, R_{ik}(u_i - u_k) \, R_{jk}(u_j - u_k)
 \]
@@ -420,13 +420,13 @@
   \;=\;
   S_{123} \, S_{023} \, S_{013} \, S_{012}
  \]
- on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\kappa^2)$ and is antisymmetric.
- \item At $\kappa = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
+ on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\hbar_{\mathrm{Y}}^2)$ and is antisymmetric.
+ \item At $\hbar_{\mathrm{Y}} = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
 \end{enumerate}
 \end{theorem}
 
 \begin{proof}
-Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\kappa^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\kappa$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
+Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\hbar_{\mathrm{Y}}^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\hbar_{\mathrm{Y}}$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
 \end{proof}
 
 \begin{remark}[Consequence for $E_3$-chiral structure]
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index be80ef202059e41717186f92909e8a4a60c6d3f9..9987e7852909b14f7237b8226056f9c1ce16c4a3
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -566,9 +566,9 @@
 $\kappa_{\mathrm{BKM}}$ (the half-weight of the Borcherds
 automorphic form, an automorphic invariant), and
 $\kappa_{\mathrm{fiber}}$ (the lattice rank of the fiber,
-relevant for fibered CY manifolds). Bare $\kappa$ without
-subscript is forbidden in this volume; every occurrence carries
-an explicit qualifier.
+relevant for fibered CY manifolds). Unsubscripted use is
+forbidden in this volume; every occurrence carries an explicit
+qualifier.
 
 \emph{Operadic terminology.}
 Following Volume~I, the word ``degree'' is used universally

tokens used
62,729
