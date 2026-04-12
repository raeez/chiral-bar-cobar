# R02_higher_genus_complementarity (1182s)

Edited [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:458). The C1 surface now separates the genus-$0$ exception from the positive-genus duality claim, Theorem B no longer carries an unproved off-locus clause, and the C2 proof now stays on the correct bar-side objects.

Verification: `./scripts/verify_edit.sh chapters/theory/higher_genus_complementarity.tex` passed. `make fast` did not give a clean regression signal because TeX failed before the document body on a pre-existing corrupted `main.aux` entry (`Runaway argument` at `Proposition~9.7.5`), so I could not use the full build as a trustworthy check.

## Rectification Summary
- [NARROWED] finding 1 — [Theorem B](</Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4130>) is now only the proved Koszul-locus inversion statement; the off-locus coderived continuation was moved to a separate remark at [4189](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4189), explicitly not proved here, which breaks the circular dependence on `prop:coderived-adequacy`.
- [FIXED] finding 2 — [Theorem C](</Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:475>) now states duality/Lagrangian claims only for `g >= 1` and records the genus-$0$ exception `Q_0(\cA)=H^0(...)`, `Q_0(\cA^!)=0`; the same exception is propagated in the summary and the duality corollary at [1221](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1221), and the small-genus check at [1720](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1720) now points back to that exception.
- [FIXED] finding 3 — [C2(i)](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1916) and its proof at [1961](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1961) now use the correct bar-side objects throughout: the adjoint BV map lands in `D_Ran(\barB(\cA))[1] \simeq \barB(\cA^!)[1]`, not `\Omega(\cA^!)`.
- [CONDITIONAL] finding 4 — [C2(iii)](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1947) no longer misapplies the center-side Lagrangian proposition directly to `L_g`; it now requires an explicit paired quasi-isomorphism `\chi_g: L_g \to \mathbf C_g(\cA)` and transports the proved ambient Lagrangian decomposition in the proof at [1998](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1998).


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
session id: 019d83a0-a0ac-7062-8fc6-bae4b2a17fe7
--------
user
<task>
You are a RECTIFICATION agent for a research mathematics manuscript on operadic Koszul duality.
Your mission: fix the specific findings below with the STRONGEST technical choice.
Hierarchy: (1) strengthen proof > (2) add missing lemma > (3) narrow claim to match proof > (4) mark conditional.
NEVER weaken when you can strengthen. NEVER leave a gap unfixed.
</task>

<action_safety>
Only edit the specific file(s) assigned. Do not touch other files.
Make the MINIMUM truthful edit that resolves each finding.
After each edit, re-read surrounding context to verify coherence.
</action_safety>

<verification_loop>
After all edits, re-read the modified sections and verify:
1. Each finding is resolved
2. No new inconsistencies introduced
3. Theorem status tags match the actual proof status
4. All \ref and \label are valid
</verification_loop>

<completeness_contract>
Address EVERY finding listed. Do not stop at the first fix.
For each finding, state: FIXED (how) or CANNOT_FIX (why, what narrower claim survives).
</completeness_contract>

<structured_output_contract>
End with:
## Rectification Summary
- [FIXED] finding — what was done
- [NARROWED] finding — claim narrowed to X
- [CONDITIONAL] finding — marked conditional on Y
- [BLOCKED] finding — cannot fix because Z
</structured_output_contract>


TARGET: chapters/theory/higher_genus_complementarity.tex

FINDINGS TO FIX:

1. [CRITICAL T02] Line ~4123: Theorem B clause (b) — off-locus proof is circular.
   thm:higher-genus-inversion cited by coderived_models.tex:247-270 which itself cites
   thm:higher-genus-inversion. The off-locus argument uses d^2=0 spectral sequence for curved setting.
   FIX: Break the circularity. Either prove clause (b) independently or mark it conditional.
   The strongest choice: separate the off-locus argument from the on-locus, prove each independently.

2. [CRITICAL T04] Line ~455,1701: C1 genus-0 boundary case. Q_0(A)=Z(A) and Q_0(A^!)=0
   contradicts Q_g(A) ≅ Q_g(A^!)^v for all g>=0.
   FIX: Either add hypothesis g>=1, or fix the genus-0 identification. The strongest choice:
   check if Q_0 formula is correct and add the genus-0 exception if needed.

3. [CRITICAL T05] Line ~1940: C2 part (i) switches from D(bar B(A)) to Omega(A^!) mid-proof.
   These are different objects. Nondegeneracy not established.
   FIX: Use the correct object consistently. If the pairing is with bar B(A^!), use that.

4. [CRITICAL T05] Line ~1970: C2 part (iii) cites prop:lagrangian-eigenspaces about center-side
   V = H*(M-bar_g, Z(A)), but applies it to bar-side L_g = bar B^(g)(A)[1]. No lift is given.
   FIX: Either prove the lift from center-level to bar-side, or restructure to work at center level.

Read the file, verify each finding, make the strongest truthful fix.
mcp startup: no servers

thinking
**Planning exploratory task**

Alright, I want to begin with some commentary on the task. I'll update my plan with steps and consider using the explorer based on guidance from the developer regarding exploratory tasks. The explorer should help locate relevant theorems and findings, as well as scan files for cited labels and potential circularity. I also need to open the skill file and execute commands to read it. My first commentary will note using `beilinson-rectify` for this claim-surface repair.
codex
Using `beilinson-rectify` for this claim-surface repair. I’m reading the required constitutional files plus the target theorem surface, then I’ll isolate the four findings against the live proof text before editing.
Plan update
  → Read required repo guidance and the target file context for the four findings
  • Trace each cited dependency/circular reference and decide the strongest truthful fix
  • Patch `chapters/theory/higher_genus_complementarity.tex` only, then re-read modified sections for coherence
  • Verify findings resolved and summarize exact disposition of each
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '380,520p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "higher-genus-inversion|higher genus|complementarity|Q_g|Q_0|lagrangian-eigenspaces" chapters/connections/concordance.tex metadata/theorem_registry.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1880,2055p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4050,4195p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: beilinson-rectify
description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
---

# Beilinson Rectify

This is the heavy rectification workflow. Use it when the task is not just to patch a claim, but to make a chapter or proof lane truer, tighter, and harder to break.

It is also the Codex-side home of the lighter `/rectify` and `/beilinson-rectify` workflows from `CLAUDE.md`.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the full target file
- the directly cited dependencies

 succeeded in 52ms:
$C^{(g)}_X(\cA)\!\mid_\Sigma$ by bar degree, writing
\[
F_p := \bigoplus_{n \leq p} \bar{B}^{(g),n}(\cA).
\]

\emph{Step~2: Identify the associated graded.}
At the associated graded level, the fiberwise curvature
$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes (it lies
in positive filtration degree), so $\operatorname{gr}_F$ sees
only the genus-$0$ collision differential~$\dzero$.
By genus-$0$ Koszulity (axiom~MK1), the associated graded is
the classical Koszul/Ext complex of
$\operatorname{gr}_F \cA$, which has cohomology concentrated
in total degree~$0$.

\emph{Step~3: Total fiber concentration.}\quad
The bar-degree filtration spectral sequence
\[
E_1^{p,q} = H^q\bigl(\operatorname{gr}_p
C^{(g)}_X(\cA)\big|_\Sigma\bigr)
 exited 2 in 51ms:
Total output lines: 536

rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
chapters/theory/higher_genus_complementarity.tex:1:\section{The complementarity theorem}
chapters/theory/higher_genus_complementarity.tex:2:\label{sec:complementarity-theorem}
chapters/theory/higher_genus_complementarity.tex:19:\begin{equation}\label{eq:complementarity-chapter-opening}
chapters/theory/higher_genus_complementarity.tex:22: Q_g(\cA) \;\oplus\; Q_g(\cA^!),
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:58: \begin{equation}\label{eq:complementarity-summary}
chapters/theory/higher_genus_complementarity.tex:61: Q_g(\cA) \;\oplus\; Q_g(\cA^!),
chapters/theory/higher_genus_complementarity.tex:63: where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
chapters/theory/higher_genus_complementarity.tex:64: $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
chapters/theory/higher_genus_complementarity.tex:65: the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
chapters/theory/higher_genus_complementarity.tex:66: Q_g(\cA^!)^\vee$
chapters/theory/higher_genus_complementarity.tex:67: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
chapters/theory/higher_genus_complementarity.tex:126:and obstructions (anomalies). The complementarity theorem gives
chapters/theory/higher_genus_complementarity.tex:139:=Q_g(\cA)\oplus Q_g(\cA^!)$.
chapters/theory/higher_genus_complementarity.tex:145:$F(\cA) \oplus F(\cA^!) = \text{universal}$. The complementarity
chapters/theory/higher_genus_complementarity.tex:162:\label{rem:complementarity-transversality}
chapters/theory/higher_genus_complementarity.tex:163:\index{complementarity!transversality of boundaries}%
 succeeded in 52ms:
\index{shifted symplectic!(-1)-shifted|textbf}
\index{Lagrangian!complementarity!shifted symplectic|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Assume the conditional BV package of
Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
genus-$1$ complementarity
$Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!)
\cong H^*(\overline{\mathcal{M}}_1, Z(\mathcal{H}_\kappa))$ that we
computed in~\S\ref{sec:frame-complementarity} admits the following
bar-side $(-1)$-shifted symplectic refinement.
\index{BV algebra!shifted symplectic structure}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
curve $X$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{BV antibracket is $(-1)$-shifted Poisson.}
 The BV bracket $\{-,-\}_{\mathrm{BV}}$ on
 $\barB^{\mathrm{ch}}(\cA)$
 \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
 succeeded in 52ms:
whose stalks $\mathcal{H}^q(C)_s = H^q(C_s) = 0$ vanish at
every geometric point~$s$.
A constructible sheaf on a connected base whose stalks are all
zero is the zero sheaf
(see~\cite[Expos\'e~IX, Th\'eor\`eme~2.14]{SGA4});
hence $\mathcal{H}^q(C) = 0$ for all~$q$, which means $C$ is
acyclic and $j_g^*\psi_g$ is a quasi-isomorphism on~$U_g$.
\end{proof}

\begin{lemma}[Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g}; \ClaimStatusProvedHere]\label{lem:higher-genus-boundary-qi}
For every boundary stratum $D_\Gamma \subset \partial\overline{\mathcal{M}}_g$
indexed by a stable graph $\Gamma$, the restricted map
\[\psi_g|_{D_\Gamma}: \Omega_g(\bar{B}_g(\mathcal{A}))|_{D_\Gamma}
\longrightarrow \mathcal{A}_g|_{D_\Gamma}\]
is a quasi-isomorphism, provided the higher-genus inversion statement is known for
all genera $< g$.
\end{lemma}

\begin{proof}
By Proposition~\ref{prop:gluing-at-nodes} and
codex
I’ve isolated the theorem surfaces. Next I’m tracing the cited dependencies behind the circularity and the bar-side pairing claims so the patch strengthens where possible and only narrows where the file cannot presently support more.
collab spawn_agent(call_D9ewcMvVq7Ts59TKkdjio32Z, prompt="Inspect `chapters/theory/higher_genus_complementarity.tex` for these four findings only, without editing. Read the local…")
spawn_agent(call_D9ewcMvVq7Ts59TKkdjio32Z, prompt="Inspect `chapters/theory/higher_genus_complementarity.tex` for these four findings only, without editing. Read the local…") pending init:
  agent: 019d83a1-3178-7472-afe0-f448e4832922
mcp startup: no servers

exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N3_e1_primacy.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit_campaign_20260412_230832
audit_campaign_20260412_231034
bibliography
bp_self_duality.pdf
chapters
exec
/bin/zsh -lc "sed -n '1,160p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc "sed -n '1,200p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\section{The complementarity theorem}
\label{sec:complementarity-theorem}

Classical Koszul duality over a point is a discrete correspondence:
$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
Already at genus~$0$ on a curve, the Fulton--MacPherson
compactifications $\overline{C}_n(X)$ and the Arnold forms
$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
that has no counterpart over a point: the collision residues that
define the bar differential, the averaging map
$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
characteristic from the spectral $r$-matrix, and the higher
operations $m_n$ for $n \geq 3$ that determine whether the shadow
tower terminates. At genus~$g \geq 1$, the fiberwise curvature
$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
algebras to interact through the moduli
$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
decomposes into two complementary halves via Verdier duality:
\begin{equation}\label{eq:complementarity-chapter-opening}
 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
exec
/bin/zsh -lc 'rg -n "thm:higher-genus-inversion" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
5231:inversion (Theorem~\ref{thm:higher-genus-inversion}),
thinking
**Inspecting dependencies**

I need to continue reading the dependencies, possibly looking into parallel executions. I might use a tool to locate labels and open the relevant sections since the explorer could take some time. It's a good idea to inspect direct dependencies too. I can use a command to find label names in the repository and explore the surroundings. Also, I should check `coderived_models.tex` around those lines and utilize multi-tool usage for efficiency.
exec
/bin/zsh -lc "sed -n '230,290p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{prop:lagrangian-eigenspaces\\}|label\\{thm:bv-functor\\}|label\\{cor:duality-bar-complexes-complete\\}|label\\{thm:bar-cobar-isomorphism-main\\}|label\\{thm:config-space-bv\\}|label\\{def:complementarity-complexes\\}|label\\{conv:bar-coalgebra-identity\\}|label\\{thm:verdier-bar-cobar\\}|label\\{thm:bar-nilpotency-complete\\}|label\\{thm:chiral-koszul-duality\\}|label\\{thm:bar-cobar-inversion-qi\\}|label\\{def:provisional-coderived\\}|label\\{prop:coderived-adequacy\\}\" chapters/theory/*.tex chapters/appendices/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1760,1845p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '820,890p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,230p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: no matches found: chapters/appendices/*.tex
 succeeded in 51ms:
by~\cite[Proposition~3.5]{Positselski11}.
\end{definition}

\begin{definition}[Provisional coderived category]
\label{def:provisional-coderived}
\index{coderived category!provisional|textbf}
The \emph{provisional coderived category} $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
is the localization of the category of filtered curved factorization
models (Definition~\ref{def:filtered-curved-model}) at the weak
equivalences of Definition~\ref{def:curved-weak-equiv}.
\end{definition}

\begin{proposition}[Adequacy; \ClaimStatusProvedHere]
\label{prop:coderived-adequacy}
The provisional coderived category is adequate for the following
constructions in this monograph:
\begin{enumerate}[label=\textup{(\alph*)}]
\item The curved bar-cobar counit
 $\Omega_X \bar{B}_X(\cA) \to \cA$ of
 Theorem~\textup{\ref{thm:higher-genus-inversion}} is an isomorphism
 succeeded in 50ms:
(Lemma~\ref{lem:verdier-involution-moduli}).
\emph{Second}, Lemma~\ref{lem:involution-splitting}(a) gives
the cochain-level splitting: the projectors
$p^\pm = \tfrac{1}{2}(\mathrm{id} \pm \sigma)$ are cochain maps
whose images provide a quasi-isomorphic direct sum decomposition
$\mathbf{C}_g \simeq \operatorname{im}(p^+) \oplus \operatorname{im}(p^-)$.
\emph{Third}, model independence
(Proposition~\ref{prop:model-independence}) ensures the
decomposition depends only on the Koszul pair $(\cA, \cA^!)$,
not on auxiliary choices.
\end{remark}

\begin{remark}[Geometric substrate (Volume~II)]
\label{rem:theorem-c-lagrangian}
\index{Lagrangian self-intersection!Theorem C}
Volume~II interprets the complementary decomposition as two
Lagrangians $\mathcal{L}$ and $\mathcal{L}^!$ inside a
$(-2)$-shifted symplectic stack $\mathcal{M}$, whose derived
intersection $\mathcal{L} \times_{\mathcal{M}} \mathcal{L}^!$
carries the $(-1)$-shifted symplectic structure that governs the
 succeeded in 50ms:
\emph{(3) Exhaustiveness and bounded-below.}
The genus filtration $F^{\le g}$ is exhaustive
($\bigcup_g F^{\le g} = \bar{B}(\cA)$) and bounded below
($F^{\le -1} = 0$). By conilpotency of $\bar{B}(\cA)$
(Theorem~\ref{thm:conilpotency-bar}), each element has
finite bar degree, hence lives in some $F^{\le g}$.

\emph{Convergence.} By (1)--(3), the spectral sequence
satisfies the hypotheses of the filtered convergence theorem
for bounded-below exhaustive filtrations with constructible
graded pieces
(Grothendieck~\cite[\S II.4.17]{Tohoku}). The $d_r$
differential shifts the genus grading by~$r$ and the
complementary degree by~$-r+1$. Since $E_r^{p,q,g} = 0$
for $p > 6g - 6$ by (1) and for $g < 0$ by (3), every
$d_r$ with $r > 6g - 6 + 1 = 6g - 5$ has either zero source
or zero target. For fixed total degree, $r \le 3g - 2$
suffices: the genus spectral sequence stabilizes
at $E_{3g-2}$.
\end{proof}
 succeeded in 50ms:

\begin{remark}[Computational perspective: Heisenberg at genus~$1$]
For $\mathcal{H}_\kappa$ at genus~$1$
(Convention~\ref{conv:heisenberg-kappa-notation}: level $=$ modular
characteristic $\kappa(\mathcal{H}_\kappa) = \kappa$):
$H^*(\overline{\mathcal{M}}_{1,1})=\mathbb{Q}\oplus\mathbb{Q}\lambda$,
$Q_1(\mathcal{H}_\kappa)=\mathbb{C}\cdot\kappa$ (central extension),
$Q_1(\mathcal{H}_\kappa^!)=\mathbb{C}\cdot\lambda$ (curved structure),
and $Q_1\oplus Q_1^!=H^0\oplus H^2=\mathbb{C}^2$.
\end{remark}

\begin{remark}[Complementarity as transversality of boundary conditions]
\label{rem:complementarity-transversality}
\index{complementarity!transversality of boundaries}%
\index{Dimofte!transversality and complementarity}%
In the holomorphic-topological framework of
Costello--Dimofte--Gaiotto~\cite{CDG2024,CG17}, a $3$d HT theory
on $\bC \times [0,1]$ places boundary conditions $\cA$
and~$\cA^!$ at the two ends of the interval. Complementarity is
the algebraic manifestation of the transversality of these
exec
/bin/zsh -lc "sed -n '4040,4140p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The cone $C = \operatorname{Cone}(j_g^*\psi_g)$ is therefore a complex of
constructible sheaves on~$U_g$ whose stalk cohomology vanishes at every
geometric point (by the fiberwise quasi-isomorphism just established).
Constructibility of~$C$ is inherited from that of the fiber
cohomology sheaves on~$U_g$
(established in the proof of Theorem~\ref{thm:ss-quantum},
Step~2).
The cohomology sheaves $\mathcal{H}^q(C)$ are therefore
constructible sheaves on the smooth connected stack~$U_g$
whose stalks $\mathcal{H}^q(C)_s = H^q(C_s) = 0$ vanish at
every geometric point~$s$.
A constructible sheaf on a connected base whose stalks are all
zero is the zero sheaf
(see~\cite[Expos\'e~IX, Th\'eor\`eme~2.14]{SGA4});
hence $\mathcal{H}^q(C) = 0$ for all~$q$, which means $C$ is
acyclic and $j_g^*\psi_g$ is a quasi-isomorphism on~$U_g$.
\end{proof}

\begin{lemma}[Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g}; \ClaimStatusProvedHere]\label{lem:higher-genus-boundary-qi}

exec
/bin/zsh -lc "sed -n '4140,4380p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{proof}
Induct on $g$.

\emph{Base case ($g=0$).}
The genus-$0$ bar-cobar inversion is proved independently by
Theorem~\ref{thm:bar-nilpotency-complete} ($d^2 = 0$) and
Theorem~\ref{thm:chiral-koszul-duality} (Koszul quasi-isomorphism);
this result is independently summarized in clause~(D2) of Theorem~\ref{thm:bar-cobar-inversion-qi} (which cites the present theorem, creating a cross-reference, not a circular dependency).

\emph{Inductive step.}
Fix $g>0$ and assume the claim for all genera $<g$. Set
$X=\overline{\mathcal{M}}_g$, with $j:U_g\hookrightarrow X$ and
$i:\partial X\hookrightarrow X$.
\begin{enumerate}[label=(\arabic*)]
\item By Lemma~\ref{lem:higher-genus-open-stratum-qi}, $j^*\psi_g$ is a
quasi-isomorphism.
\item By Lemma~\ref{lem:higher-genus-boundary-qi} and the induction hypothesis
on the lower-genus vertices of each stable graph $\Gamma$ indexing a boundary
stratum $D_\Gamma$, $\psi_g|_{D_\Gamma}$ is a quasi-isomorphism for every
$D_\Gamma$. The passage from ``quasi-isomorphism on each~$D_\Gamma$''
thinking
**Searching dependencies**

I need to locate direct dependencies, but it seems like using glob with rg isn't working. I might try using rg in the repo instead. Maybe searching for the labels individually will help, possibly using some alternation and avoiding globbing? I'll try running rg with the -n flag across chapters. It’s important to be thorough, so I’ll make sure to open around those labels when I run the search. Let's see how that goes!
exec
/bin/zsh -lc "sed -n '220,320p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
 strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
 \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
\item The induced map on coacyclic quotients
 $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
 isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
 generated by totalizations of short exact sequences
 (Positselski~\cite{Positselski11}).
\end{enumerate}
The equivalence of (i) and (ii) holds for bounded-below filtrations
by~\cite[Proposition~3.5]{Positselski11}.
\end{definition}

\begin{definition}[Provisional coderived category]
\label{def:provisional-coderived}
\index{coderived category!provisional|textbf}
The \emph{provisional coderived category} $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
is the localization of the category of filtered curved factorization
models (Definition~\ref{def:filtered-curved-model}) at the weak
equivalences of Definition~\ref{def:curved-weak-equiv}.
codex
The file-level picture is clear now: the genus-0 issue is real in the theorem statement itself, and the shifted-symplectic upgrade is mixing H-level and M-level objects. I’m checking whether any existing bar-side theorem can genuinely close those two gaps before I demote or reframe them.
exec
/bin/zsh -lc "sed -n '1200,1245p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2268,2335p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(thm:bv-functor|cor:duality-bar-complexes-complete|thm:bar-cobar-isomorphism-main|thm:config-space-bv|thm:verdier-bar-cobar|conv:bar-coalgebra-identity|thm:bar-cobar-spectral-sequence|lem:higher-genus-open-stratum-qi)\\}\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(E_\infty^{p,q,g})_{\mathcal{A}} \cong ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee
\end{equation}

But $E_\infty^{*,*,g} = \text{gr}^g H^*$ by definition, so:
\begin{equation}
\text{gr}^g H^{p+q}(\bar{B}(\mathcal{A})) \cong (\text{gr}^g H^{p+d-q}(\bar{B}(
\mathcal{A}^!)))^\vee
\end{equation}
\end{proof}

\begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
\label{cor:quantum-dual-complete}
For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
\begin{equation}
Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
\end{equation}
with respect to the Verdier pairing.
\end{corollary}

\begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
 succeeded in 51ms:
\begin{equation}
H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!)
\end{equation}

If $Q_g(\mathcal{A}) = 0$, then $Q_g(\mathcal{A}^!) \cong H^*(\overline{\mathcal{M}}_g, 
Z(\mathcal{A}))$.

\emph{Second statement}: If both vanish, then by exhaustion:
\begin{equation}
0 = \dim Q_g(\mathcal{A}) + \dim Q_g(\mathcal{A}^!) = \dim H^*(\overline{\mathcal{M}}_g, 
Z(\mathcal{A}))
\end{equation}

Thus $H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = 0$.
\end{proof}

\begin{remark}[Examples of vanishing]
At genus~$0$: $Q_0(\cA)=\mathbb{C}$, $Q_0(\cA^!)=0$ (tree-level,
no obstruction).
For TFTs: $Q_g(\cA)=0$ for all~$g$.
 succeeded in 51ms:
chapters/theory/bar_construction.tex:81:\label{conv:bar-coalgebra-identity}
chapters/theory/bar_cobar_adjunction_inversion.tex:2024:\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
chapters/theory/higher_genus_complementarity.tex:1117:\label{cor:duality-bar-complexes-complete}
chapters/theory/higher_genus_complementarity.tex:4010:\begin{lemma}[Open-stratum quasi-isomorphism; \ClaimStatusProvedHere]\label{lem:higher-genus-open-stratum-qi}
chapters/theory/chiral_koszul_pairs.tex:3611:\label{thm:bar-cobar-isomorphism-main}
chapters/theory/cobar_construction.tex:1313:\label{thm:verdier-bar-cobar}
chapters/connections/bv_brst.tex:1303:\label{thm:config-space-bv}
chapters/connections/bv_brst.tex:1359:\label{thm:bv-functor}
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '230,290p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   230	by~\cite[Proposition~3.5]{Positselski11}.
   231	\end{definition}
   232	
   233	\begin{definition}[Provisional coderived category]
   234	\label{def:provisional-coderived}
   235	\index{coderived category!provisional|textbf}
   236	The \emph{provisional coderived category} $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
   237	is the localization of the category of filtered curved factorization
   238	models (Definition~\ref{def:filtered-curved-model}) at the weak
   239	equivalences of Definition~\ref{def:curved-weak-equiv}.
   240	\end{definition}
   241	
   242	\begin{proposition}[Adequacy; \ClaimStatusProvedHere]
   243	\label{prop:coderived-adequacy}
   244	The provisional coderived category is adequate for the following
   245	constructions in this monograph:
   246	\begin{enumerate}[label=\textup{(\alph*)}]
   247	\item The curved bar-cobar counit
   248	 $\Omega_X \bar{B}_X(\cA) \to \cA$ of
   249	 Theorem~\textup{\ref{thm:higher-genus-inversion}} is an isomorphism
exec
/bin/zsh -lc 'rg -n "coderived" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3361: coderived
4132:faithfully in the provisional coderived category
4134:\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
4135:Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
4266:The replacement is the coderived factorization co-contra comparison on
4414:(iii)~the coderived category
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4100,4175p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4100	
  4101	\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
  4102	\index{bar-cobar inversion!higher genus}
  4103	\textup{[}Regime: curved-central on the Koszul locus;
  4104	filtered-complete off it
  4105	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  4106	
  4107	\smallskip\noindent
  4108	The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.
  4109	
  4110	Let $\cA$ be a modular pre-Koszul chiral algebra
  4111	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral}},
  4112	axioms \textup{MK1--MK3)}.
  4113	\begin{enumerate}[label=\textup{(\alph*)}]
  4114	\item \emph{Koszul locus.}
  4115	For each genus $g \geq 0$, the bar-cobar counit is a
  4116	quasi-isomorphism:
  4117	\[\psi_g \colon \Omega_g(\bar{B}_g(\cA))
  4118	\xrightarrow{\;\sim\;} \cA_g,\]
  4119	where $\cA_g$ denotes the genus-$g$ component.
exec
/bin/zsh -lc "sed -n '1080,1145p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3590,3655p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2000,2060p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1290,1365p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1288,1388p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Since $\overline{C}_n(X)$ is a smooth proper variety over~$\mathbb{C}$, the algebraic and analytic canonical bundles coincide by~GAGA.

The duality pairing is given by integration:
\begin{equation}
\langle \alpha, \beta \rangle = \int_{\overline{C}_n(X)} \alpha \wedge \beta
\end{equation}
for $\alpha \in H^k(\overline{C}_n(X))$ and $\beta \in H^{2n-k}(\overline{C}_n(X))$.

\emph{Perfect pairing}: By Poincaré duality for compact oriented manifolds:
\begin{equation}
H^k(\overline{C}_n(X)) \times H^{2n-k}(\overline{C}_n(X)) \xrightarrow{\wedge} 
H^{2n}(\overline{C}_n(X)) \xrightarrow{\int} \mathbb{C}
\end{equation}
is a perfect pairing. This is the geometric incarnation of Verdier duality.

\emph{Logarithmic forms}: When we include logarithmic forms $\Omega^*_{\log}(
\overline{C}_n(X))$ (forms with logarithmic poles along $\partial \overline{C}_n(X)$), 
the duality becomes:
\begin{equation}
\Omega^k_{\log}(\overline{C}_n(X)) \times \Omega^{2n-k}_{\log}(\overline{C}_n(X)) 
 succeeded in 52ms:
so $\Delta^{\mathrm{prim}}_\cA = 0$ identically. The
Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
of weight~$2$ and $g_r = p(r+1) - p(r)$ for all $r \geq 1$,
giving primitive defect $\Delta^{\mathrm{prim}}_{\mathrm{Vir}}(t)
= G_{\mathrm{Vir}}(t) - t$, which is nonzero starting at
$t^3$. This nonvanishing defect is the kinematic signature of
nonquadraticity and feeds directly into the MC4 completion
programme
(\S\textup{\ref{subsec:shadow-postnikov-tower}}).
\end{remark}

\subsection{Geometric bar-cobar duality (Theorem~A)}
\label{sec:theorem-a-statement}

The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
is unconditionally a factorization algebra
(Chapter~\ref{chap:NAP-koszul-derivation}).
Theorem~A identifies the conditions under which $\cA^!_\infty$ is
\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.

 succeeded in 52ms:
\begin{enumerate}
\item $F^0 \supseteq F^1 \supseteq F^2 \supseteq \cdots$
\item $\bigcap_{p=0}^\infty F^p = 0$ (completeness)
\item The differential respects filtration: $d(F^p) \subseteq F^p$
\item The natural map factors through the filtration
\end{enumerate}
\end{definition}

\begin{lemma}[Associated graded; \ClaimStatusProvedHere]\label{lem:bar-cobar-associated-graded}
The associated graded of the bar-cobar filtration is:
\[\text{Gr}^p\Omega(\bar{B}(\mathcal{A})) = \Omega^p(\bar{B}^p(\mathcal{A}))\]

The induced differential on $\text{Gr}^\bullet$ is the \emph{bar complex differential} $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ (i.e., the full differential on $\bar{B}(\mathcal{A})$, lifted to each cobar tensor factor).
\end{lemma}

\begin{proof}
By definition of associated graded:
\[\text{Gr}^p = F^p / F^{p+1} = \Omega^p(\bar{B}^p(\mathcal{A}))\]

The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
 succeeded in 51ms:
 - (-1)^{|a|} a\,\Delta(b)\bigr]
 \]
 (the failure of $\Delta$ to be a graded derivation) satisfies the
 graded Leibniz rule in each slot:
 \begin{gather*}
 \{a, bc\} = \{a, b\}\,c + (-1)^{(|a|+1)|b|} b\,\{a, c\},\\
 \{a, b\} = -(-1)^{(|a|+1)(|b|+1)}\{b, a\}.
 \end{gather*}
\end{enumerate}
The bracket automatically satisfies the graded Jacobi identity.
\end{definition}

\subsection{BV structure from configuration spaces}

\begin{theorem}[Conditional configuration-space BV package; \ClaimStatusConditional]
\label{thm:config-space-bv}
Assume that the diagonal-residue operator on the logarithmic bar
complex extends to a degree-$+1$ second-order operator
\[
\Delta\colon \bar{B}^{\mathrm{ch}}(\mathcal{A})
 succeeded in 51ms:

\begin{remark}[CFT vertex operators from cobar]\label{rem:vertex-operators-cobar}
In conformal field theory, vertex operators $V_\alpha(z)$ create states $|\alpha\rangle$ 
at position $z$. These correspond to cobar elements:
\[V_\alpha \leftrightarrow K_\alpha \in \Omega^1(\mathcal{C})\]

The OPE of vertex operators:
\[V_\alpha(z) V_\beta(w) \sim \sum_\gamma \frac{C_{\alpha\beta}^\gamma}{(z-w)^{h_\gamma - h_\alpha - h_\beta}} V_\gamma(w)\]

corresponds to the cobar product:
\[n_2(K_\alpha, K_\beta) = \sum_\gamma C_{\alpha\beta}^\gamma K_\gamma\]

The structure constants $C_{\alpha\beta}^\gamma$ are precisely the cobar $A_\infty$ 
structure constants.

The cobar construction thus provides a geometric derivation
of the OPE algebra in CFT.
\end{remark}

\subsection{Verdier duality on bar and cobar}
exec
/bin/zsh -lc 'rg -n "thm:quantum-complementarity-main" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
39:(Theorem~\ref{thm:quantum-complementarity-main}).
67: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
435:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
456:\label{thm:quantum-complementarity-main}
867:anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
1740:This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere
1749:Theorem~\ref{thm:quantum-complementarity-main} via three steps.
1821:Theorem~\ref{thm:quantum-complementarity-main}, Step~7), so the
1837:Theorem~\ref{thm:quantum-complementarity-main}), the involution
1858:Theorem~\ref{thm:quantum-complementarity-main} is a Lagrangian
2048: (Theorem~\ref{thm:quantum-complementarity-main}), we have
2183:The conjecture asserts that quantum complementarity (Theorem~\ref{thm:quantum-complementarity-main}) reproduces established physics identifications (central charge duality, marginal-obstruction exchange, electric-magnetic splitting) when applied to specific CFT Koszul pairs.
2203:complementarity decomposition is functorial (property 3 of Theorem~\ref{thm:quantum-complementarity-main}), it commutes with the modular action.
2321:(Theorem~\ref{thm:quantum-complementarity-main}):
2390:(Theorem~\ref{thm:quantum-complementarity-main}) with
2428:The mathematical content is that Theorem~\ref{thm:quantum-complementarity-main}
2682:By Theorem~\ref{thm:quantum-complementarity-main},
2708:(Theorem~\ref{thm:quantum-complementarity-main}),
5140:\mathbf{Q}_g(\cA^!)$ of Theorem~\ref{thm:quantum-complementarity-main}
5256:By Theorem~\ref{thm:quantum-complementarity-main},
exec
/bin/zsh -lc "sed -n '420,520p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\pi_g\colon \mathcal{C}_g(\cA) \to \overline{\mathcal{M}}_g$.
The fiber-level concentration from Step~3 gives
$R^q\pi_{g*}\bar{B}^{(g)}(\cA) = 0$ for $q \neq 0$.
Perfectness of $R\pi_{g*}\bar{B}^{(g)}(\cA)$
(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
uniformly over $\overline{\mathcal{M}}_g$.
The surviving $R^0\pi_{g*}$ is identified with
$\mathcal{Z}_{\cA}$ by the fiber-level identification
from Step~3, which holds uniformly over the base.
\end{proof}

\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
\index{Theorem C!decomposition}
Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
identification, this theorem) produces the ambient complex;
$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
gives the Verdier eigenspace decomposition and its Lagrangian
splitting; $\mathrm{C}_2$
(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
conditional bar-side BV / shifted-symplectic upgrade.
exec
/bin/zsh -lc "rg -n \"Q_g\\(\" -n chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
22: Q_g(\cA) \;\oplus\; Q_g(\cA^!),
61: Q_g(\cA) \;\oplus\; Q_g(\cA^!),
63: where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
64: $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
65: the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
66: Q_g(\cA^!)^\vee$
139:=Q_g(\cA)\oplus Q_g(\cA^!)$.
204:Q_g(\cA) &:= H^*(\mathbf{Q}_g(\cA))
206:Q_g(\cA^!) &:= H^*(\mathbf{Q}_g(\cA^!))
507:Q_g(\cA) \;\oplus\; Q_g(\cA^!),
510:$Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
511:$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
515:Q_g(\cA) \cong Q_g(\cA^!)^\vee.
565:$\mathcal{H}_g=Q_g(\cA)\oplus Q_g(\cA^!)$; model independence
608:& Establish perfect pairing between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$\\
847:Q_g(\mathcal{A}) = E_\infty^{*,*,g} = \bigoplus_{p+q=*} \text{gr}^g H^{p+q}(
864:Q_g(\mathcal{A}) := \text{gr}^g H^*(\bar{B}(\mathcal{A})) = E_\infty^{*,*,g}
866:We use the same notation $Q_g(\mathcal{A})$ for this graded piece,
882:\emph{Explicit description.} An element of $Q_g(\mathcal{A})$ is represented by a closed form $\omega \in \bar{B}^{(g)}(\mathcal{A})$ (i.e., $d\omega = 0$) that is not exact modulo lower genus contributions.
1033:sequence, and the identification of $Q_g(\mathcal{A})$ with $E_\infty$
exec
/bin/zsh -lc "sed -n '820,980p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\emph{(3) Exhaustiveness and bounded-below.}
The genus filtration $F^{\le g}$ is exhaustive
($\bigcup_g F^{\le g} = \bar{B}(\cA)$) and bounded below
($F^{\le -1} = 0$). By conilpotency of $\bar{B}(\cA)$
(Theorem~\ref{thm:conilpotency-bar}), each element has
finite bar degree, hence lives in some $F^{\le g}$.

\emph{Convergence.} By (1)--(3), the spectral sequence
satisfies the hypotheses of the filtered convergence theorem
for bounded-below exhaustive filtrations with constructible
graded pieces
(Grothendieck~\cite[\S II.4.17]{Tohoku}). The $d_r$
differential shifts the genus grading by~$r$ and the
complementary degree by~$-r+1$. Since $E_r^{p,q,g} = 0$
for $p > 6g - 6$ by (1) and for $g < 0$ by (3), every
$d_r$ with $r > 6g - 6 + 1 = 6g - 5$ has either zero source
or zero target. For fixed total degree, $r \le 3g - 2$
suffices: the genus spectral sequence stabilizes
at $E_{3g-2}$.
\end{proof}
exec
/bin/zsh -lc 'rg -n "prop:lagrangian-eigenspaces" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1780:Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
1784:\label{prop:lagrangian-eigenspaces}
1869:Proposition~\ref{prop:lagrangian-eigenspaces} establishes the
1978:Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
2027:(Proposition~\ref{prop:lagrangian-eigenspaces}(i)) is a
2044: Proposition~\ref{prop:lagrangian-eigenspaces}(iii):
exec
/bin/zsh -lc "sed -n '2024,2145p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
\label{thm:koszul-spectral-sequence}
The filtration from Definition~\ref{def:bar-cobar-filtration} induces a spectral 
sequence:
\[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.

\emph{Explicit description of pages.}
\begin{align*}
E_0^{p,q} &= \left(F^p\Omega^{p+q}(\bar{B}(\mathcal{A})) \big/ F^{p+1}\Omega^{p+q}(\bar{B}(\mathcal{A}))\right) \quad \text{(associated graded)} \\
E_1^{p,q} &= H^{p+q}\!\left(E_0^{p,\bullet},\, d_{\bar{B}}\right)
 \quad \text{(bar cohomology at fixed cobar degree $p$)} \\
E_2^{p,q} &= H^p\!\left(E_1^{\bullet,q},\, d_{\text{cobar}}\right)
 \quad \text{(cohomology w.r.t.\ comultiplication-induced differential)} \\
E_\infty^{p,q} &= \mathrm{Gr}^p H^{p+q}(\Omega(\bar{B}(\mathcal{A}))) \quad \text{(limiting page)}
\end{align*}
\end{theorem}

\begin{proof}
This is a standard spectral sequence associated to a filtered complex (Weibel~\cite{Weibel94}, Chapter~5). We verify the key properties:
exec
/bin/zsh -lc "sed -n '1740,2100p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere

\end{proof}

\begin{remark}[Proof architecture summary for Theorem~C]
\label{rem:h-level-proof-summary}
\index{Theorem C!proof architecture summary}
The distributed proof above establishes both the
S-level (cohomological) and H-level (homotopy) claims of
Theorem~\ref{thm:quantum-complementarity-main} via three steps.
\emph{First}, the Verdier involution~$\sigma$ is a
\emph{cochain-level} involution on
$\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$:
it is induced by the composition of Verdier duality~$\mathbb{D}$
(an exact functor on $D^b_{\mathrm{hol}}(\mathcal{D})$) with the
Koszul identification
$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$
(Theorem~\ref{thm:kodaira-spencer-chiral-complete}, Step~7).
Since~$\sigma$ is induced by exact functors, it commutes with
differentials at every page of the spectral sequence
exec
/bin/zsh -lc "rg -n \"Proof of Theorem~\\\\ref\\{thm:quantum-complementarity-main\\}\" -n chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


exec
/bin/zsh -lc "sed -n '1000,1300p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(Definition~\ref{def:chiral-koszul-pair}), the bar concentration
theorem (Theorem~\ref{thm:bar-concentration}) gives
\[
E_1^{p,q}
= H^q\bigl(\operatorname{gr}^p_F
 \bar{B}^*_{\Sigma_g}(\mathcal{A}),\, d_0\bigr)
= 0
\qquad\text{for } q \neq 0.
\]
Because the $E_1$ page is concentrated on the line $q=0$, every
differential
$d_r\colon E_r^{p,q} \to E_r^{p+r,\,q-r+1}$
with $r \geq 2$ has target in the row $q' = q - r + 1 \leq -1$,
which is zero (bar degree is non-negative).
The $d_1$ differential maps within the $q = 0$ row and need not
vanish, but after passing to $E_2 = H(E_1, d_1)$ the page remains
concentrated on $q = 0$. The spectral sequence therefore collapses
at~$E_2$: $E_\infty = E_2$.

Convergence of the spectral sequence now gives
thinking
**Investigating weak equivalence**

I'm thinking about how this theorem could reference a definition and demonstrate that the counit represents weak equivalence in the specific category. By definition, weak equivalence is linked to graded quasi-isomorphisms or E1-page quasi-isomorphisms. I realize I need to check the definitions, like `def:curved-weak-equiv`, and then search for relevant materials. Let's get insights on this to clarify my understanding further and ensure I'm on the right track!
exec
/bin/zsh -lc "sed -n '160,235p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{def:curved-weak-equiv\\}|label\\{def:filtered-curved-model\\}\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
194:\label{def:filtered-curved-model}
214:\label{def:curved-weak-equiv}
 succeeded in 51ms:
At genus $g \geq 1$ with $\kappa(\cA) \neq 0$, the bar complex
is genuinely curved, and the underlying bar complex is acyclic on
the ordinary cochain-complex surface
\textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)}.
Bar-cobar inversion therefore becomes a statement in the
coderived category
$D^{\mathrm{co}}(\bar{B}^{(g)}\text{-}\mathrm{comod})$.
The Koszul duality equivalence
$D^{\mathrm{co}}(\barB^{(g)}(\cA)\text{-}\mathrm{comod})
\simeq D^{\mathrm{ctr}}(\barB^{(g)}(\cA)\text{-}\mathrm{contra})$
\textup{(}Theorem~\ref{thm:positselski-chiral-proved}\textup{)} is the chiral
incarnation of the comodule-contramodule correspondence
\eqref{eq:co-contra-equivalence}.
\end{remark}

%%% ---------------------------------------------------------------
%%% Relative curved models adequate for the present monograph
%%% ---------------------------------------------------------------

\subsection{Relative curved models}
exec
/bin/zsh -lc 'rg -n "curvature|associated graded|positive filtration degree|strict complexes|weak equivalence|off the Koszul locus" chapters/theory/higher_genus_complementarity.tex chapters/theory/coderived_models.tex chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:48:with central curvature), filtered-complete (requiring $I$-adic completion),
chapters/theory/bar_cobar_adjunction_inversion.tex:104:The double pole produces a \emph{curved} quadratic structure: the relation $J \otimes J \sim k \cdot \mathbf{1}$ is inhomogeneous (the right side is degree~0, not degree~2), so the bar complex has curvature $m_0 \propto k \cdot \mathbf{1} \neq 0$ for $k \neq 0$ (the curvature element is proportional to the vacuum, which is central). In the language of Definition~\ref{def:quadratic-chiral}, the Heisenberg is ``quadratic'' in the sense that the OPE involves at most two generators on the left side, but it is \emph{not} strictly quadratic (i.e., $m_0 \neq 0$).
chapters/theory/bar_cobar_adjunction_inversion.tex:107:\[\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*) \quad \text{(commutative chiral algebra on the dual space, with curvature)}\]
chapters/theory/bar_cobar_adjunction_inversion.tex:109:Since $\mathfrak{h}$ is abelian, the chiral Koszul dual is $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ with $d = 0$ and curvature $m_0 \propto -k \cdot \mathbf{1}$ (the level negates under Koszul duality; $h^\vee = 0$ for the abelian Lie algebra). This is a \emph{commutative} chiral algebra with curvature, not the Heisenberg at negated level \neq \mathcal{H}_{-k}$). The bar differential vanishes (Example~\ref{ex:ope-to-residue}), so $H^*(\bar{B}(\mathcal{H}_k)) \simeq \bar{B}(\mathcal{H}_k)$ with CE cooperad structure.
chapters/theory/bar_cobar_adjunction_inversion.tex:123:No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
chapters/theory/bar_cobar_adjunction_inversion.tex:153:\item There exists a \emph{central curvature element} $\mu_0 \in Z(\mathcal{A})^2$
chapters/theory/bar_cobar_adjunction_inversion.tex:154:\item The curvature satisfies the MC equation: 
chapters/theory/bar_cobar_adjunction_inversion.tex:170:The algebra is curved because the central charge $c$ is a curvature
chapters/theory/bar_cobar_adjunction_inversion.tex:199:The \emph{associated graded} is:
chapters/theory/bar_cobar_adjunction_inversion.tex:337:The $E_1$ page reduces to the associated graded computation of Step~1.
chapters/theory/bar_cobar_adjunction_inversion.tex:353:\item The associated graded $\mathrm{gr}(\mathcal{A})$ is generated by $\mathrm{gr}^1(\mathcal{A})$
chapters/theory/bar_cobar_adjunction_inversion.tex:354:\item All higher relations are \emph{consequences} of lower ones plus curvature
chapters/theory/bar_cobar_adjunction_inversion.tex:365:The filtered algebra $\mathcal{A}$ deforms $\mathrm{gr}(\mathcal{A})$. By condition~(3), the deformation is controlled by a single curvature element: choose generators $a_1, \ldots, a_r$ lifting $\mathrm{gr}^1(\mathcal{A})$ to $F_1\mathcal{A}$. The product $\mu(a_i, a_j)$ in $\mathcal{A}$ differs from the product in $\mathrm{gr}(\mathcal{A})$ by an element in $F_2\mathcal{A}$:
chapters/theory/bar_cobar_adjunction_inversion.tex:386:\emph{Option 2 - Curved.} Generator $V = \mathbb{C} \cdot T$, curvature $\mu_0 = c \cdot \mathbf{1}$, and higher operations $m_3(T \otimes T \otimes T)$ from the Schwarzian.
chapters/theory/bar_cobar_adjunction_inversion.tex:392:The curvature $\mu_0 = c$ captures the failure of $T$ to be a quadratic generator.
chapters/theory/bar_cobar_adjunction_inversion.tex:430:Since $J_{(0)}J = 0$ (no simple pole), only the curvature
chapters/theory/bar_cobar_adjunction_inversion.tex:431:component~$d_{\mathrm{curvature}}$ contributes
chapters/theory/bar_cobar_adjunction_inversion.tex:433:bar degrees, the output of $d_{\mathrm{curvature}}$ is the
chapters/theory/bar_cobar_adjunction_inversion.tex:473:\item Its Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ is the commutative chiral algebra on $V^*$, with curvature $m_0 \propto -k \cdot \mathbf{1}$
chapters/theory/bar_cobar_adjunction_inversion.tex:507:The curvature $c$ ensures $\widehat{d}^2 = 0$ on the completed complex.
exec
/bin/zsh -lc "sed -n '4200,4245p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
abstract homotopy equivalence $\mathrm{FT}^2 \simeq \mathrm{id}$
descends to a concrete quasi-isomorphism on each stratum of
$\overline{\mathcal{M}}_g$.
\end{remark}

\begin{lemma}[\texorpdfstring{$E_2$}{E2} collapse at higher genus;
\ClaimStatusProvedHere]\label{lem:e2-collapse-higher-genus}
\index{spectral sequence!E2 collapse@$E_2$ collapse!higher genus}
For a Koszul chiral algebra~$\cA$ on a genus-$g$ curve, the PBW
spectral sequence
$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g \bar{B}_g(\cA))$
degenerates at~$E_2$.
\end{lemma}

\begin{proof}
The PBW filtration is a filtration by chiral algebras, and the
Koszulness hypothesis ensures that the associated graded is a
Koszul complex in the classical sense. The $d_r$ differential
for $r \geq 2$ maps between PBW-graded components separated
by~$r$ steps, and the Koszul concentration (all bar cohomology

thinking
**Inspecting mathematical remarks**

It seems there's a need to adjust the theorem based on the existing remarks about a certain category. I might want to inspect those later for clarity. I'm looking into whether the theorem currently states "for each g ≥ 0" regarding homotopy and S-level. There's a details about Q0 being given later, which could influence my checks. I should check the Q0 formula for correctness and possibly add a genus-0 exception. I’ll review the context around line 1701.
exec
/bin/zsh -lc "sed -n '1678,1715p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{lemma}[Exhaustion property; \ClaimStatusProvedHere]
\label{lem:exhaustion-complete}
The quantum correction spaces exhaust the moduli space cohomology:
\begin{equation}
\dim Q_g(\mathcal{A}) + \dim Q_g(\mathcal{A}^!) = \dim H^*(\overline{\mathcal{M}}_g,
Z(\mathcal{A}))
\end{equation}
\end{lemma}

\begin{proof}[Proof of Lemma~\ref{lem:exhaustion-complete}]
Since $\sigma^2 = \mathrm{id}$ on the finite-dimensional vector space
$V = H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$, the minimal polynomial of
$\sigma$ divides $t^2 - 1 = (t-1)(t+1)$. Over $\mathbb{C}$, every vector decomposes
uniquely into $\pm 1$ eigenvectors via the projectors
$\pi^+ = \frac{1}{2}(\mathrm{id} + \sigma)$ and
$\pi^- = \frac{1}{2}(\mathrm{id} - \sigma)$. Therefore:
\begin{equation}
V = V^+ \oplus V^- = Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!)
\end{equation}
and in particular $\dim V^+ + \dim V^- = \dim V$.

thinking
**Verifying theorem details**

I'm checking if the formula for Q0 is correct, and it seems likely, based on the definition. The theorem should state that for g ≥ 1, it discusses decomposition, and for g = 0, \(Q_0(A)=H^0(...)\) and \(Q_0(A^!)=0\). I also need to adjust any later references to "eq:quantum-duality" for all g values. I'll search within the target for the references to “eq:quantum-duality.”
exec
/bin/zsh -lc "rg -n \"eq:quantum-duality|Q_0\\(|g >= 0|for each genus g \\\\geq 0|for all g \\\\geq 0|3g-3|Lagrangian polarization|Q_g\\(\\\\cA\\) \\\\cong Q_g\\(\\\\cA\\"'^!'"\\)\\"'^'"\\\\vee\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:eq:quantum-duality|Q_0\(|g >= 0|for each genus g \geq 0|for all g \geq 0|3g-3|Lagrangian polarization|Q_g\(\cA\) \cong Q_g\(\cA\^!\)\^\vee)
                                                        ^^
error: unrecognized escape sequence


thinking
**Clarifying genus moduli definitions and dimensionality**

I’m analyzing how the moduli of genus g curves is defined, especially for g=0 and g=1 where automorphism groups are infinite, making stable moduli stacks not well-defined without markings. The dimension formula 3g-3 and Verdier duality used in proofs only hold for g≥2, so genus-0 cases need exceptions or separate treatment. I’ll also explore whether the user’s question on conditional results in C2(i) can be answered by checking if referenced theorems like `thm:config-space-bv` stand unconditionally or remain conditional.
exec
/bin/zsh -lc 'rg -n "thm:config-space-bv" -n -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1886:Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
1899: \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
1933:has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
thinking
**Considering search strategies**

I’m thinking about using simpler search methods, perhaps by separating fixed strings. This approach might make it easier to target the information I need. It feels a bit uncertain, though. I wonder if this will provide better results or if it might overcomplicate things. I just want to ensure I'm getting accurate and relevant information in the most straightforward way possible. Let’s see how this method works out!
exec
/bin/zsh -lc 'rg -n -F "for each genus $g '"\\geq 0"'$" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "eq:quantum-duality" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Q_0(" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "3g{-}3" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
514:\begin{equation}\label{eq:quantum-duality}
2053: by~\eqref{eq:quantum-duality}.
 succeeded in 51ms:
1703:giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
2285:At genus~$0$: $Q_0(\cA)=\mathbb{C}$, $Q_0(\cA^!)=0$ (tree-level,
 succeeded in 51ms:
77: $\mathbf{C}_g(\cA)$ carries a $({-}(3g{-}3))$-shifted symplectic
82: \mathbf{Q}_g(\cA^!)^\vee[-(3g{-}3)]$.
478: of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
491: $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
492: so $\mathbf{Q}_g(\cA) \simeq \mathbf{Q}_g(\cA^!)^\vee[-(3g{-}3)]$.
583:\mathcal{Z}(\cA))$ carries a $-(3g{-}3)$-shifted symplectic structure
2008:carries a $(-(3g{-}3))$-shifted symplectic structure in the sense of
2028:non-degenerate symmetric pairing of degree $-(3g{-}3)$, so $C_g$
2029:carries a $(-(3g{-}3))$-shifted symplectic structure.
2050: $Q_g(\cA) \to Q_g(\cA^!)^{\vee}[-(3g{-}3)]$ is a
2052: $Q_g(\cA) \otimes Q_g(\cA^!)$ is perfect of degree $-(3g{-}3)$
2062:($(-(3g{-}3))$-shifted,
5153:$(-(3g{-}3))$-shifted symplectic form.
exec
/bin/zsh -lc 'rg -n "config-space-bv" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/dependency_graph.dot:183:  thm_config_space_bv [label="thm:config-space-bv\ntheorem [Co]\nConditional configuration-space BV packa...", style=filled, fillcolor="#e1bee7"];
metadata/label_index.json:46250:  "thm:config-space-bv": {
metadata/claims.jsonl:157:{"label": "rem:qme-bar-cobar", "env_type": "remark", "status": "Heuristic", "file": "chapters/connections/bv_brst.tex", "line": 256, "title": "Heuristic QME/MC comparison", "refs_in_block": ["thm:bv-bar-geometric", "thm:config-space-bv", "thm:bv-functor"]}
metadata/claims.jsonl:173:{"label": "thm:config-space-bv", "env_type": "theorem", "status": "Conditional", "file": "chapters/connections/bv_brst.tex", "line": 1294, "title": "Conditional configuration-space BV package"}
metadata/claims.jsonl:176:{"label": "thm:bv-functor", "env_type": "theorem", "status": "Conditional", "file": "chapters/connections/bv_brst.tex", "line": 1350, "title": "Conditional BV functor package", "refs_in_block": ["thm:config-space-bv", "thm:verdier-bar-cobar"]}
metadata/claims.jsonl:914:{"label": "thm:thqg-III-bv-lagrangian", "env_type": "theorem", "status": "Conditional", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 901, "title": "Conditional BV Lagrangian polarization", "refs_in_block": ["thm:config-space-bv", "thm:bv-functor"]}
metadata/claims.jsonl:2662:{"label": "thm:shifted-symplectic-complementarity", "env_type": "theorem", "status": "Conditional", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 1858, "title": "Conditional bar-side BV upgrade of complementarity", "refs_in_block": ["conv:regime-tags", "thm:config-space-bv", "thm:bv-functor", "sec:frame-complementarity", "cor:duality-bar-complexes-complete", "thm:verdier-bar-cobar", "conv:bar-coalgebra-identity", "prop:modular-deformation-truncation", "thm:modular-homotopy-convolution"], "cites_in_block": ["Pridham17"]}
audit_campaign_20260412_231034/T05_thm_C2.md:386:  1886	Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
audit_campaign_20260412_231034/T05_thm_C2.md:399:  1899	 \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
audit_campaign_20260412_231034/T05_thm_C2.md:788:/bin/zsh -lc 'rg -n "thm:deformation-obstruction|deformation-obstruction|quantum-complementarity-main|shifted-symplectic-complementarity|perfectness-criterion|prop:lagrangian-eigenspaces|thm:fiber-center-identification|thm:verdier-bar-cobar|thm:bv-functor|thm:config-space-bv" chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex metadata/claims.jsonl' in /Users/raeez/chiral-bar-cobarexec
audit_campaign_20260412_231034/T05_thm_C2.md:1525:Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
audit_campaign_20260412_231034/T05_thm_C2.md:1542:Theorem~\ref{thm:config-space-bv} and a Verdier-duality comparison
audit_campaign_20260412_231034/T05_thm_C2.md:2258:I need to check if part (ii) of theorem C2 uses pairing from the bar-cobar construction for invariant pairing on L_g. It's a bit tricky since the invariance deduced comes from the BV Leibniz rule, and I’m not sure if it’s conditionally valid. I'll also verify if `Theorem\ref{thm:config-space-bv}` provides proof of bracket degree. I should look for a possible "scalar BV pairing" theorem elsewhere. It turns out that the requested theorem C2 might be conditional, which is important.
audit_campaign_20260412_231034/T05_thm_C2.md:2336:  1899	 \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
audit_campaign_20260412_231034/T05_thm_C2.md:2356:  1362	Theorem~\ref{thm:config-space-bv} and a Verdier-duality comparison
chapters/theory/higher_genus_complementarity.tex:1886:Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
chapters/theory/higher_genus_complementarity.tex:1899: \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
chapters/theory/higher_genus_complementarity.tex:1933:has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
chapters/connections/bv_brst.tex:263:\textup{(}Theorem~\ref{thm:config-space-bv}\textup{)}.
chapters/connections/bv_brst.tex:278:Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. That

thinking
**Checking theorem summaries**

I'm thinking about searching for a summary of theorems mentioned, especially around lines 77. I need to adjust the chapter opening accordingly since the user just asked for the findings. However, I notice that the theorem summaries at lines 63-66 and 77-82 might conflict if the theorem changed. I guess I'll need to inspect the top lines, particularly from 50 to 90, to see what's going on there.
exec
/bin/zsh -lc "sed -n '52,88p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

\item \emph{Eigenspace decomposition \textup{(}unconditional on the
 Koszul locus\textup{)}.}\;
 For every chiral Koszul pair $(\cA, \cA^!)$ on a smooth projective
 curve~$X$ and every genus $g \geq 0$, the cohomology of the ambient
 complex splits as
 \begin{equation}\label{eq:complementarity-summary}
 H^*(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA))
 \;=\;
 Q_g(\cA) \;\oplus\; Q_g(\cA^!),
 \end{equation}
 where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
 the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
 Q_g(\cA^!)^\vee$
 \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.

\item \emph{Shifted-symplectic Lagrangian upgrade
 \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
 When the relative bar family
exec
/bin/zsh -lc "sed -n '1260,1420p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
from configuration-space geometry is in
\S\ref{sec:complete-bv-structure}.

% Labels preserved for cross-reference compatibility.
\label{rem:ht-from-n4-sym}%
\label{rem:boundary-chiral-algebra-bv}%
\label{rem:bar-cobar-ht-boundary}%
% conj:holographic-bar-cobar defined in genus_complete.tex
\label{rem:w-algebra-bar-cobar}%


\section{The BV algebra structure}
\label{sec:complete-bv-structure}

\subsection{BV algebra definition}

\begin{definition}[BV algebra]
\label{def:bv-algebra-complete}
\index{BV algebra|textbf}
A \emph{Batalin--Vilkovisky algebra} is a graded commutative algebra
exec
/bin/zsh -lc "rg -n -F \"Q_g(\\cA) \\cong Q_g(\\cA"'^!)''^'"\\vee\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
515:Q_g(\cA) \cong Q_g(\cA^!)^\vee.

thinking
**Searching for fixed strings**

I'm considering a scenario involving a fixed string and some shifts in other areas. I need to search for this specific expression: `Q_g(\\mathcal{A}) \\cong Q_g(\\mathcal{A}^!)^\\vee`. It's important to make sure I'm gathering the right context for this search so I can understand its implications fully. The notation seems technical, and I want to capture all relevant meanings. Let's dive into that!
exec
/bin/zsh -lc "rg -n \"Q_g\\((\\\\cA|\\\\mathcal\\{A\\})\\)\\s*\\\\cong\\s*Q_g\\((\\\\cA\\"'^!|'"\\\\mathcal\\{A\\}\\"'^!)'"\\)\\"'^'"\\\\vee\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Q_g\((\cA|\mathcal\{A\})\)\s*\cong\s*Q_g\((\cA\^!|\mathcal\{A\}\^!)\)\^\vee)
             ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F \"Q_g(\\mathcal{A}"'^!)''^'"\\vee\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Q_g(\\cA"'^!)''^'"\\vee\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1214:Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
1224:\bigoplus_{p+q=n} ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee = Q_g(\mathcal{A}^!)^\vee
1541:$Q_g(\mathcal{A}^!)^\vee$. Under the identification with moduli cohomology,
 succeeded in 51ms:
66: Q_g(\cA^!)^\vee$
515:Q_g(\cA) \cong Q_g(\cA^!)^\vee.

thinking
**Inspecting theorem details**

I want to look at the corollary around 1214 that suggests "all g maybe." I'll need to see if this needs to be fixed too since it seems independent from the main theorem. Also, I’d like to search for context regarding topics from 1180 to 1230 because getting a broader understanding could help clarify things. It's interesting how these details connect!
exec
/bin/zsh -lc "sed -n '1178,1232p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is perfect. Thus $(E_1^{p,q,g})_{\mathcal{A}} \cong ((E_1^{p,d-q,g})_{\mathcal{A}^!})^\vee$.

\emph{Differential $d_1$}: The differential $d_1: E_1^{p,q,g} \to E_1^{p+1,q,g}$ is 
induced by the moduli space differential. Under Verdier duality:
\begin{equation}
\mathbb{D} \circ d_1 = (-1)^{p+q} d_1^\vee \circ \mathbb{D}
\end{equation}
where $d_1^\vee$ is the dual differential.

This sign is precisely the Koszul sign convention (see Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}). 
Thus the differential on $(E_1)_{\mathcal{A}}$ is dual to the differential on 
$(E_1)_{\mathcal{A}^!}$, up to the appropriate sign.

\emph{Higher pages}: By induction, if $(E_r)_{\mathcal{A}} \cong ((E_r)_{\mathcal{A}^!})^\vee$, 
then taking cohomology with respect to $d_r$ preserves this duality:
\begin{equation}
(E_{r+1})_{\mathcal{A}} = H(E_r, d_r)_{\mathcal{A}} \cong (H(E_r, d_r)_{\mathcal{A}^!})^\vee 
= ((E_{r+1})_{\mathcal{A}^!})^\vee
\end{equation}





thinking
**Analyzing conditional theorem dependencies**

I'm working through four key points regarding conditionality in the theorems, especially how C2(i) and C2(iii) depend on conditional BV structures. I've noted that C2(i) remains conditional due to reliance on unproven diagonal residue operators, while C2(iii) can be rephrased at the center level using unconditional Verdier pairing results. I’m also examining genus restrictions in the moduli space statements and circular references between propositions and theorems to suggest precise file references and potential local edits that avoid circularity, all while carefully documenting line numbers and dependencies for clarity.
thinking
**Recommending targeted theorem and statement edits**

I’m proposing specific local edits to avoid circular references by removing the Proposition citation from Theorem clause (b), restricting genus-related statements to g≥2 for moduli validity, maintaining conditional status on BV-dependent parts due to missing unconditional diagonal operators, and rephrasing the Lagrangian claim in C2(iii) to center-level results where unconditional proofs exist—all with precise line references and usage of multipath verification to support these recommendations.
codex
Used the **multi-path-verify** workflow to trace the relevant proofs/lemmas in `higher_genus_complementarity.tex` and the cited dependencies.

- **Circularity in Theorem `thm:higher-genus-inversion` clause (b)**: Clause (b) currently asserts that the curved counit represents $\cA$ in the provisional coderived category “(Definition…; Proposition~\ref{prop:coderived-adequacy}(a))”. Proposition \ref{prop:coderived-adequacy}(a) is proved in `chapters/theory/coderived_models.tex:242-271` by appealing to the same Theorem~\ref{thm:higher-genus-inversion}, so the citation is circular. Recommend removing the reference to Proposition (a) from clause (b) (or rephrasing it so the theorem only states the existence of the curved object in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$) and leaving the argument that it is an equivalence to the later proposition (which should be reworked to stand independently of this theorem). (`chapters/theory/higher_genus_complementarity.tex:4123-4136`, `chapters/theory/coderived_models.tex:242-271`)

- **Genus-0 statement in `thm:quantum-complementarity-main`**: The decomposition, Verdier pairing and shift $\dim_{\mathbb C}\overline{\mathcal{M}}_g=3g-3$ are proved in Proposition~\ref{prop:lagrangian-eigenspaces} only for a smooth proper DM stack, which only exists in the unmarked case for $g\geq 2$ (the $g<2$ cases either have no stable moduli or infinite automorphisms). The current “for each genus $g\geq 0$” claim therefore cannot be sustained; the strongest truthful version is to restrict to the regime where $\overline{\mathcal{M}}_g$ is a finite-type stack (i.e., $g\geq 2$) and to mention separately that the genus-0 data is captured by the earlier Heisenberg/frame complementarity arguments. Update the theorem statement at `chapters/theory/higher_genus_complementarity.tex:456-514` to begin “For each genus $g\geq 2$ …”. (`chapters/theory/higher_genus_complementarity.tex:456-514`, `chapters/theory/higher_genus_complementarity.tex:1778-1838`)

- **C2(i) (bar-side Poisson/BV upgrade)**: This bullet is already flagged “conditional”, and for good reason: the diagonal residue operator and BV functor needed in Theorem~\ref{thm:shifted-symplectic-complementarity} depend on the conditional package of Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}, both of which are still unproved (see `chapters/connections/bv_brst.tex:1303-1377`). The existing pairing `\langle-,-\rangle` from Corollary~\ref{cor:duality-bar-complexes-complete} alone does not give the missing degree-1 Laplacian/bracket data. Keep C2(i) conditional until those hypotheses can be resolved; no stronger bar-side statement is justified by the current supply of objects. (`chapters/theory/higher_genus_complementarity.tex:1886-1905`, `chapters/connections/bv_brst.tex:1303-1377`)

- **C2(iii) (bar-side Lagrangian eigenspaces)**: Without the conditional BV package there is no established bar-level symplectic form on $L_g=\barB^{(g)}(\cA)[1]$. However, Proposition~\ref{prop:lagrangian-eigenspaces} and Proposition~\ref{prop:ptvv-lagrangian} already prove that the Verdier pairing on the ambient complex $\mathbf{C}_g(\cA)$ produces complementary Lagrangians $Q_g(\cA)$, $Q_g(\cA^!)$ (respectively in the classical and PTVV senses) unconditionally (`chapters/theory/higher_genus_complementarity.tex:1774-2080`). Either keep C2(iii) as a conditional “bar-side” statement or rephrase it so that the Lagrangian property is asserted for the center complex (where it has been proven). Without the BV hypothesis, we cannot assert the bar-side version. (`chapters/theory/higher_genus_complementarity.tex:1774-2080`)
thinking
**Resolving mathematical conflicts**

I'm wondering if the corollary is also false at g=0 unless Q0(A^!) is not 0. The theorem suggests 0, but since the user pointed to specific lines for a fix, we might need to address the conflicting corollary and step II as well. This is all within the same file, and minimizing edits is key. To avoid inconsistencies, we should consider restricting the corollary to g≥1 or adding an exception. I need to check if the proof really is just for g≥1 due to the moduli dimension formula.
thinking
**Aligning mathematical findings**

Given the theorem statement and the remark on Q0, it seems safest to restrict duality claims to g≥1 and note an exception for genus 0. However, if the corollary proof relates to spectral sequence limits, it might apply to all g. The theorem identifies Q_g with the eigenspace, suggesting genus-0 could be an exception. Notably, the finding points to a contradiction for Q0(A^!) being zero. The search at line 1214 might also clarify if it should restrict to g≥1. I’ll need to consider the broader context, especially with the object switch mid-proof.
codex
I’ve confirmed the shifted-symplectic proof cannot currently reuse the center-side Lagrangian proposition verbatim: that proposition is about `RΓ( M̄_g , Z(A))`, not `\bar B^{(g)}(A)[1]`. I’m checking whether there is already a bar-side involution/pairing result to salvage the claim; if not, I’ll keep the strongest center-level statement and fence the bar-side lift as conditional.
exec
/bin/zsh -lc "sed -n '1145,1185p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1365,1415p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"L_g\\"'^'"\\+|L_g\\"'^-|bar-side eigenspaces|Verdier involution induces an involution on.*bar|BV pairing on '"\\\\barB|isotropic|Lagrangian subspaces|bar-side\" chapters/theory/higher_genus_complementarity.tex chapters/connections/bv_brst.tex chapters/theory/cobar_construction.tex chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{equation}
\langle s, t \rangle = \int_{\overline{C}_n(X)} (s \otimes t) \wedge (-)
\end{equation}
for $s \in \bar{B}^n(\mathcal{A})$ and $t \in \bar{B}^n(\mathcal{A}^!)$.

This pairing is perfect because both the Koszul pairing and the Verdier pairing are 
perfect.
\end{proof}

\emph{Step 6: Duality interchanges spectral sequences.}

\begin{lemma}[Spectral sequence duality; \ClaimStatusProvedHere]
\label{lem:ss-duality-complete}
The Verdier duality of Theorem~\ref{thm:verdier-duality-config-complete} induces an isomorphism 
of spectral sequences:
\begin{equation}
(E_r^{p,q,g})_{\mathcal{A}} \cong ((E_r^{p,d-q,g})_{\mathcal{A}^!})^\vee
\end{equation}
for all $r \geq 1$, where $d = \dim_{\mathbb{R}} \overline{C}_n(X) = 2n$.
\end{lemma}
 succeeded in 52ms:
differential. Then the assignment
\[\mathrm{BV}: \mathrm{ChirAlg}_X \longrightarrow \mathrm{BV\text{-}Alg}\]
is a lax monoidal functor, and the Verdier dual
$\mathbb{D}_{\operatorname{Ran}}(\bar{B}(\mathcal{A}))$ identifies
with a factorization algebra $\cA^!_\infty$ whose underlying complex
is equivalent to $\bar{B}(\mathcal{A}^!)$
\textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}.
On the Koszul locus, $\cA^!_\infty \simeq \cA^!$.
\end{theorem}

\begin{proof}
Functoriality of the underlying bar construction is standard. The
extra BV functoriality and lax monoidal statements are exactly the
assumed functorial and tensor-compatibility properties of the
conditional BV package, while the Verdier-duality comparison is part
of the additional hypothesis in the theorem statement.
\end{proof}

\begin{remark}[Shifted symplectic structure from BV]\label{rem:bv-shifted-symplectic}
\index{shifted symplectic!from BV}
 succeeded in 50ms:
chapters/connections/bv_brst.tex:1387:$\barB^{\mathrm{ch}}(\cA)$ would provide a bar-side
chapters/theory/higher_genus_complementarity.tex:80: $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
chapters/theory/higher_genus_complementarity.tex:238: $V^-$ are isotropic for $\langle -,- \rangle$; if the pairing is
chapters/theory/higher_genus_complementarity.tex:439:conditional bar-side BV / shifted-symplectic upgrade.
chapters/theory/higher_genus_complementarity.tex:1852:isotropic, i.e., Lagrangian.
chapters/theory/higher_genus_complementarity.tex:1873:direct bar-side realization of a $(-1)$-shifted symplectic chart on
chapters/theory/higher_genus_complementarity.tex:1875:Chapter~\ref{ch:bv-brst}. The following theorem records that bar-side
chapters/theory/higher_genus_complementarity.tex:1878:\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
chapters/theory/higher_genus_complementarity.tex:1891:bar-side $(-1)$-shifted symplectic refinement.
chapters/theory/higher_genus_complementarity.tex:1923: eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
chapters/theory/higher_genus_complementarity.tex:1924: complementary Lagrangian subspaces, with $L_g^+$ controlling
chapters/theory/higher_genus_complementarity.tex:1925: deformations of~$\cA$ and $L_g^-$ controlling deformations
chapters/theory/higher_genus_complementarity.tex:1979:$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
chapters/theory/higher_genus_complementarity.tex:1980:$(-1)$-shifted symplectic form. They are maximal isotropic (hence
chapters/theory/higher_genus_complementarity.tex:1981:Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
chapters/theory/higher_genus_complementarity.tex:2068:there is also a direct bar-side $(-1)$-shifted strict chart on
chapters/theory/higher_genus_complementarity.tex:3417:isotropicity $\gamma_k \cdot \gamma_l = 0$
chapters/theory/higher_genus_complementarity.tex:4531:$(-1)$-shifted symplectic form and isotropicity of each side.
chapters/theory/higher_genus_complementarity.tex:4533:isotropicity is \emph{equivariant} under the modular operad
chapters/theory/higher_genus_complementarity.tex:4608:are isotropic inside $T_{\mathrm{comp}}(\cA)$;
exec
/bin/zsh -lc "rg -n \"\\\\barB\\"'^'"\\{\\(g\\)\\}|genus-\\"'$g'"\\"'$ bar|pairing on.*bar|Verdier.*bar.*genus|L_g := '"\\\\barB\\"'^'"\\{\\(g\\)\\}\" chapters/theory/higher_genus_complementarity.tex chapters/connections/bv_brst.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_modules.tex:38:A module over a factorization algebra is itself a factorization algebra on a pointed space: the marked point carries the module data, the remaining points carry algebra data (Voronov~\cite{Voronov99}, Costello--Gwilliam~\cite{CG17}, Ayala--Francis~\cite{AF15}). The bar complex $\bar{B}(\cA, M)$ lives on such pointed configuration spaces, and its Verdier dual is a comodule over $\bar{B}(\cA)$. On the proved quadratic genus-$0$ $\Eone$ surface, this leads to the complete/conilpotent module comparison of Theorem~\ref{thm:e1-module-koszul-duality}. More generally, the module bar construction provides the intrinsic coalgebra-side object, while broader representation-category equivalences require additional hypotheses and are treated only on the specific lanes where they are established.
chapters/theory/higher_genus_complementarity.tex:4001:With Verdier duality and Ayala--Francis compatibility established, the bar-cobar adjunction at higher genus can be inverted on the Koszul locus.
chapters/theory/higher_genus_complementarity.tex:4001:With Verdier duality and Ayala--Francis compatibility established, the bar-cobar adjunction at higher genus can be inverted on the Koszul locus.

thinking
**Clarifying the approach**

I'm considering whether the task I'm tackling is about finding something by not misusing property, which could be seen as 'conditional' rather than restructured. The task emphasizes finding the strongest truthful fix. Since the theorem is already conditional, I think it could work to add the exact missing lift as a hypothesis—unless it needs proof, in which case, I'd need to rethink it! It’s a little tricky to navigate, but I’ll figure it out.
collab wait(call_l5G5gLmo75LtAJEnNjJhYUD3)
  receivers: 019d83a1-3178-7472-afe0-f448e4832922
wait(call_l5G5gLmo75LtAJEnNjJhYUD3) 1 agents complete:
  019d83a1-3178-7472-afe0-f448e4832922 completed: "Used the **multi-path-verify** workflow to trace the relevant proofs/lemmas in `higher_genus_complementarity.tex` and th…"



thinking
**Analyzing mathematical consistency**

I'm examining a claim about stronger restrictions needing a genus of at least 2 due to stability of moduli. However, the earlier file refers to genus 1 with \(\overline{\mathcal M}_{1,1}\), while the theorem mentions \(\overline{\mathcal M}_g\). This inconsistency raises questions for me. The theorem's statement uses \(\overline{\mathcal M}_g\) and involves a shift for genus 1, which might be okay if it’s addressing dimension—but I need to be cautious not to overreach. It feels contradictory.
thinking
**Defining minimal adjustments**

I believe the strongest, most truthful fix might involve just adding a genus-0 exception instead of a broader g≥2 restriction. I want to avoid making any major scope changes since the user suggested checking the Q_0 formula and adding the exception. I also need to carefully parse the proof of theorem B and possibly include an independent off-locus argument. Exploring local proofs from definitions could be necessary, while also ensuring we clearly demonstrate that \(\operatorname{gr}\psi\) becomes an isomorphism.
thinking
**Considering associated graded curvature**

I'm examining arguments suggesting that the associated graded curvature vanishes, and how genus-0 Koszulity aligns with the classical Koszul complex. Hm, this might support off-locus situations. I need to take a closer look at the earlier section from around 260 to 420 to gather more context and better understand these connections. There's definitely a lot to unpack here!
exec
/bin/zsh -lc "sed -n '260,420p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
\[
\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
\overline{\mathcal{M}}_g
\]
be the family of genus-$g$ compactified configuration spaces
carrying the relative bar complex $\bar{B}^{(g)}(\cA)$.
Its stalk at $[\Sigma] \in \overline{\mathcal{M}}_g$ is the
\emph{genus-$g$ fiber bar complex}
$C^{(g)}_X(\cA)\!\mid_\Sigma$, i.e.\ the bar complex of~$\cA$
on the fixed curve~$\Sigma$ with the fiberwise curved
differential~$\dfib$
\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
\end{definition}

\begin{lemma}[Perfectness criterion for the relative bar family;
\ClaimStatusProvedHere]
\label{lem:perfectness-criterion}
\index{perfectness criterion|textbf}
\index{bar complex!relative perfectness|textbf}
exec
/bin/zsh -lc "rg -n \"label\\{thm:bar-cobar-inversion-qi\\}|Higher genus inversion|curved equivalence|associated graded map|counit\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:4020:the bar-cobar counit
chapters/theory/higher_genus_complementarity.tex:4038:spectral sequence collapses at~$E_2$, and the counit~$\psi_s$
chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
chapters/theory/higher_genus_complementarity.tex:4115:For each genus $g \geq 0$, the bar-cobar counit is a
chapters/theory/higher_genus_complementarity.tex:4232:The counit $\psi_g\colon\Omega_g(\bar{B}_g(\cA))\xrightarrow{\sim}\cA_g$
chapters/theory/higher_genus_complementarity.tex:4263:route, and the bar-cobar counit is therefore not promoted here as a
chapters/theory/bar_cobar_adjunction_inversion.tex:15:whether the counit $\psi \colon \Omegach(\barBch(\cA)) \to \cA$
chapters/theory/bar_cobar_adjunction_inversion.tex:23:(Definition~\ref{def:koszul-locus}), the counit~$\psi$ is a
chapters/theory/bar_cobar_adjunction_inversion.tex:691:the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
chapters/theory/bar_cobar_adjunction_inversion.tex:743: a counit $\varepsilon\colon C \to \omega_X$, coassociativity,
chapters/theory/bar_cobar_adjunction_inversion.tex:744: and the counit axioms.
chapters/theory/bar_cobar_adjunction_inversion.tex:750: (the counit annihilates $d$ except possibly in the lowest degree).
chapters/theory/bar_cobar_adjunction_inversion.tex:812:and counit axioms) endowed with a homogeneous endomorphism
chapters/theory/bar_cobar_adjunction_inversion.tex:1284:where the last step uses the counit of the adjunction
chapters/theory/bar_cobar_adjunction_inversion.tex:1364:To see this, observe that the unit and counit natural transformations
chapters/theory/bar_cobar_adjunction_inversion.tex:1604:\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
chapters/theory/bar_cobar_adjunction_inversion.tex:1619:counit
chapters/theory/bar_cobar_adjunction_inversion.tex:1660:the counit $\psi$ is a quasi-isomorphism there
chapters/theory/bar_cobar_adjunction_inversion.tex:1713:The counit
chapters/theory/bar_cobar_adjunction_inversion.tex:1775:The map $\psi$ is the counit of the bar-cobar adjunction
exec
/bin/zsh -lc "sed -n '1604,1718p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
\textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
on the Koszul locus; filtered-complete off it
\textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}

The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.

Let $\mathcal{A}$ be a \emph{Koszul} chiral algebra on a Riemann surface $X$
(Definition~\ref{def:koszul-chiral-algebra};
equivalently, $\cA \in \operatorname{Kosz}(X)$;
this excludes simple admissible-level quotients and minimal-model
central charges; see Scope below), with
$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ conilpotent or $\mathcal{A}$ complete
with respect to its augmentation ideal
\textup{(}\S\ref{sec:i-adic-completion}\textup{)}. Then the genus-$0$
counit
\[
\psi_0: \Omega_0(\bar{B}_0(\mathcal{A})) \longrightarrow \mathcal{A}
\]
is a quasi-isomorphism of chiral algebras.

thinking
**Considering mathematical implications**

I’m looking at the bar-cobar inversion theorem, and it seems like the off-locus needs to relate to completed or coderived correspondence. But it doesn’t actually prove anything. For higher genus inversion, I think the off-locus clause could be conditional or marked with a remark, which might be the simplest approach. Also, it could be helpful to make an open remark around 4263 to clarify this for others who might be reading.
exec
/bin/zsh -lc "sed -n '4245,4275p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\emph{Step~B} (M-level): induction on genus via open-stratum QI
(Lemma~\ref{lem:higher-genus-open-stratum-qi}), boundary QI
(Lemma~\ref{lem:higher-genus-boundary-qi}), and extension
(Lemma~\ref{lem:extension-across-boundary-qi}).
\emph{B$\to$A}: lifts to H-level by factorization-homology excision
(Remark~\ref{rem:homotopy-native-b}) and model independence.
\emph{Step~C}: PBW spectral sequence collapses at $E_2$
(Lemma~\ref{lem:e2-collapse-higher-genus}), yielding Riordan/Motzkin
generating functions.
\end{remark}

\begin{remark}[Scope boundary at admissible levels]
\label{rem:admissible-scope-boundary}
\index{admissible level!scope boundary}
\index{bar-cobar inversion!failure at admissible levels}
Theorem~B requires Koszulity (MK1). For simple admissible affine
quotients $L_k(\fg)$ at levels $k=-h^\vee+p/q$, that hypothesis is
not currently verified: null vectors obstruct the PBW/Shapovalov
route, and the bar-cobar counit is therefore not promoted here as a
derived equivalence. The obstruction is expected to be carried by




thinking
**Evaluating theorem adjustments**

The remark indicates that theorem B requires Koszulity and isn't promoted at admissible levels, which contradicts clause (b). I think the theorem needs narrowing or a conditional off-locus statement. It might make sense to treat clause (b) as conditional and separate it, pointing to a provisional coderived category. Since the user requested a distinction between on-locus and off-locus arguments, I need to ensure it's marked conditional if it can't be independently proven.
thinking
**Refining theorem clarity**

I think the statement should be narrowed to focus solely on the Koszul locus. After the theorem, I might add a remark explaining that off the Koszul locus, the filtered curved object persists, representing \(\cA\) in a provisional coderived category. However, I need to address clause (b) specifically, as the user requested. Maintaining the theorem with two subparts could work: (a) Koszul locus [proved]; and (b) a conditional statement for off the Koszul locus, ensuring clarity on the theorem's status.
thinking
**Adjusting theorem structure**

I’m considering changing the theorem status to mixed, but I’m not sure if that’s best since it needs to match the actual proof status. I might have to split it into a theorem and a remark. It feels safer to state that the Higher Genus Inversion theorem is only proved for clause (a). After the proof, I could add a conditional remark about off-locus continuation, which may require updating the theorem header text as well.
thinking
**Searching theorem references**

It seems like there might be a remark related to homotopy that's possibly off-locus. I'm thinking if I narrow down the theorem, the references might still be valid for on-locus inversion. However, the summary table of the theorem might include mentions of off-locus. I should search the file for terms like "off the Koszul locus" and "Theoremref{thm:higher-genus-inversion}". I wonder if I need to adjust anything if nothing is directly false. Alright, let's search!
codex
I’ve resolved the strategy choices. `thm:higher-genus-inversion` cannot honestly keep an off-locus proved clause in this file, so I’m narrowing the theorem to the independently proved Koszul-locus statement and moving the coderived continuation out of the proved theorem surface. I’m also rewriting the C2 proof so it stays on the correct bar-side objects and explicitly marks the missing lift in part (iii).
exec
/bin/zsh -lc 'rg -n -F "thm:higher-genus-inversion" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Theorem~\\ref{thm:higher-genus-inversion}\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "off the Koszul locus" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
5231:inversion (Theorem~\ref{thm:higher-genus-inversion}),
 succeeded in 51ms:
5231:inversion (Theorem~\ref{thm:higher-genus-inversion}),
 exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '5210,5245p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\ClaimStatusProvedHere]
\label{thm:holo-comp-bulk-reconstruction}
\index{dual transform!protected|textbf}
Let $\cA$ be a modular Koszul chiral algebra on~$X$. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Dual transform.}\;
 $\mathbb{H}_X(\cA) \simeq \cA^!$.
\item \emph{Anti-involution.}\;
 $\mathbb{H}_X^2(\cA) \simeq \cA$.
\item \emph{Cofiber identification.}\;
 For every $g \geq 0$,
 $\mathbf{H}^{\mathrm{hol}}_g(\cA) \simeq \mathbf{Q}_g(\cA^!)$.
\end{enumerate}
In particular, the protected transform $\mathbb{H}_X$ identifies
canonically with the Koszul-dual branch and is a contravariant
involution.
\end{theorem}

\begin{proof}
By Verdier intertwining

thinking
**Reviewing the C2 theorem**

I don't see an issue here. I might need to search for references to the C2 theorem or the quantum dual equation later, though I'm not entirely sure if it's necessary. I think it’d be useful to inspect line 1870 and the surrounding context before the C2 theorem to make any adjustments to the introductory text. I want to ensure everything is accurate and well-integrated!
exec
/bin/zsh -lc "sed -n '1868,1995p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

Proposition~\ref{prop:lagrangian-eigenspaces} establishes the
Lagrangian polarization at the level of cohomology, and
Proposition~\ref{prop:ptvv-lagrangian} upgrades the Verdier side to a
proved shifted-symplectic statement on the ambient complex~$C_g$. The
direct bar-side realization of a $(-1)$-shifted symplectic chart on
$L_g = \barB^{(g)}(\cA)[1]$ would require the additional BV package of
Chapter~\ref{ch:bv-brst}. The following theorem records that bar-side
upgrade conditionally.

\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
\label{thm:shifted-symplectic-complementarity}
\index{shifted symplectic!(-1)-shifted|textbf}
\index{Lagrangian!complementarity!shifted symplectic|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Assume the conditional BV package of
Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
genus-$1$ complementarity
exec
/bin/zsh -lc "sed -n '2058,2085p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[Two shifted symplectic structures]\label{rem:ptvv-relation}
\index{Pantev--To\"en--Vaqui\'e--Vezzosi}
Complementarity carries two shifted symplectic structures:
(i)~Verdier on the ambient complex
($(-(3g{-}3))$-shifted,
Proposition~\ref{prop:ptvv-lagrangian});
(ii)~ambient cyclic deformation theory
($(-1)$-shifted,
Theorem~\ref{thm:ambient-complementarity-fmp}).
Conditional on Theorem~\ref{thm:shifted-symplectic-complementarity},
there is also a direct bar-side $(-1)$-shifted strict chart on
$L_g = \barB^{(g)}(\cA)[1]$. In each proved incarnation,
$Q_g(\cA)$ and $Q_g(\cA^!)$ are complementary Lagrangians; the
different realizations are compatible via the spectral sequence
$E_2^{p,q,g}\Rightarrow H^{p+q}_{\mathrm{chiral}}$.
\end{remark}

\begin{theorem}[Spectral sequence as genus stratification; \ClaimStatusProvedHere]\label{thm:ss-genus-stratification}
\textup{[Regime: curved-central; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}




thinking
**Evaluating theorem adjustments**

This remark seems fine as long as the theorem stays conditional—no changes needed. I might need to check line 4531 later, perhaps relating to isotropicity in ambient complementarity tangent. There might be a better fix for theorem B off-locus than simply removing the clause. I should check references from theorem B to ensure they don't affect other files, even though the user said to only edit the specific assigned file. Leaving a note about off-locus might be helpful.
thinking
**Considering theorem adjustments**

The user has explicitly stated to only work on specific files, so I need to find a way to keep references intact. If I can shift the off-locus to a conditional remark within the same file while retaining the same theorem label, that might work. I wonder if keeping clause (b) labeled as conditional within the theorem could satisfy requirements. I need to check if that’s acceptable, especially to align theorem status with the actual proof. A mixed status might cause confusion.
thinking
**Examining theorem labeling**

It looks like the environment label may not support mixed statements. I could change the theorem title to something like "Higher genus inversion on the Koszul locus; \ClaimStatusProvedHere" and then add a remark or proposition as a conditional off-locus without a label. This way, while the other file's citation would be semantically incorrect, my edited file would stay accurate. 

Alternatively, I might keep clause (b) and prove it independently using definitions, but I need to analyze if that gives enough support. I have to confirm that the off-locus object accurately represents A in the provisional coderived category.
thinking
**Inspecting consistency**

I see that everything is in the same file, which is good for avoiding inconsistencies. I'll need to check the chapter summary bullet and the theorem statement as well. It might be necessary to inspect line 1541 to see how duality is used in the proof of identification. I'm thinking I'll search through the context around lines 1526-1560 to gather more details. This sounds like a plan!
exec
/bin/zsh -lc "sed -n '1528,1562p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{align}
\end{lemma}

\begin{proof}[Proof of Lemma~\ref{lem:eigenspace-decomposition-complete}]
Since $\sigma^2 = \mathrm{id}$ on the finite-dimensional vector space $V :=
H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$, the eigenvalues of $\sigma$ are
$\pm 1$, and $V = V^+ \oplus V^-$ (standard linear algebra over $\mathbb{C}$;
the projectors are $\pi^\pm = \frac{1}{2}(\mathrm{id} \pm \sigma)$).

\emph{Identification of $V^+$ with $Q_g(\mathcal{A})$.}
By construction, $\sigma$ acts on $E_\infty^{*,*,g}$ by exchanging the contributions
from $\mathcal{A}$ and $\mathcal{A}^!$. A class $\alpha \in Q_g(\mathcal{A}) =
\mathrm{gr}^g H^*(\bar{B}(\mathcal{A}))$ maps under $\mathbb{D}$ to a class in
$Q_g(\mathcal{A}^!)^\vee$. Under the identification with moduli cohomology,
$\alpha$ contributes to $V^+$ because:
\begin{enumerate}
\item The bar complex of $\mathcal{A}$ uses $j_*$-extension.
\item The cobar complex of $\mathcal{A}$ (equivalently, the bar of $\mathcal{A}^!$)
uses $j_!$-extension.
\item Verdier duality exchanges $j_*$ and $j_!$

thinking
**Adjusting approach**

I’m thinking I should adjust my approach since the user asked for specific findings rather than a comprehensive review of the entire file. It seems like focusing on the key points will be more helpful for them. This way, I can provide a clear and succinct summary that meets their needs without overwhelming them with unnecessary details. It’s all about delivering the right information in the most effective way!
exec
/bin/zsh -lc 'rg -n -F "cor:quantum-dual-complete" chapters/theory/higher_genus_complementarity.tex chapters/**/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_symplectic_polarization.tex:640:(Corollary~\ref{cor:quantum-dual-complete}).
chapters/theory/higher_genus_complementarity.tex:1211:\label{cor:quantum-dual-complete}
chapters/theory/higher_genus_complementarity.tex:1219:\begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
chapters/theory/higher_genus_complementarity.tex:1254:\mathcal{A}^!))^\vee$ be the Verdier isomorphism of Corollary~\ref{cor:quantum-dual-complete}.
chapters/theory/higher_genus_complementarity.tex:2240:By Verdier duality (Corollary~\ref{cor:quantum-dual-complete}):
chapters/theory/higher_genus_complementarity.tex:1211:\label{cor:quantum-dual-complete}
chapters/theory/higher_genus_complementarity.tex:1219:\begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
chapters/theory/higher_genus_complementarity.tex:1254:\mathcal{A}^!))^\vee$ be the Verdier isomorphism of Corollary~\ref{cor:quantum-dual-complete}.
chapters/theory/higher_genus_complementarity.tex:2240:By Verdier duality (Corollary~\ref{cor:quantum-dual-complete}):

thinking
**Inspecting file references**

I notice that another file is using certain references, but I can’t edit that. It might be acceptable if I restrict g to be greater than or equal to 1, which could affect those references, but maybe it's fine as is. I think I should inspect the local references at 1254 and 2240 to ensure g constraints are being met. I’ll also need to search around lines 2235 and 1250 for additional context.
exec
/bin/zsh -lc "sed -n '1244,1265p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2232,2246p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
\to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
\begin{equation}
\rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
\end{equation}
constructed from the Gauss--Manin connection on the chiral homology sheaf.

This action interacts with Verdier duality via anti-commutativity: let
$\mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A})) \xrightarrow{\sim} H^*(\bar{B}^{(g)}(
\mathcal{A}^!))^\vee$ be the Verdier isomorphism of Corollary~\ref{cor:quantum-dual-complete}.
Then for every $z \in Z(\mathcal{A})$ and $v \in T_{[\Sigma_g]}\overline{\mathcal{M}}_g$:
\begin{equation}\label{eq:verdier-ks-anticommute}
\mathbb{D} \circ \nabla_{\kappa(v)}^z = -\nabla_{\kappa(v)}^z \circ \mathbb{D}
\end{equation}
where $\kappa(v)$ is the Kodaira--Spencer class associated to $v$ and $\nabla^z$
denotes the action of $z$ via the Gauss--Manin connection.
\end{theorem}

\begin{proof}[Proof of Theorem~\ref{thm:kodaira-spencer-chiral-complete}]
 succeeded in 52ms:
\end{equation}

Thus:
\begin{equation}
Q_g(\mathcal{A}^!) = H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(\mathcal{A})
\end{equation}
as vector spaces.

By Verdier duality (Corollary~\ref{cor:quantum-dual-complete}):
\begin{equation}
Q_g(\mathcal{A}^!) \cong Q_g(\mathcal{A})^\vee
\end{equation}

Combining these gives the stated formula.


thinking
**Searching references and context**

I’m thinking about making this assumption for \( g \ge 1 \) and patching local uses with necessary notes. I need to search for where these references occur and see if the context already uses \( g \ge 1 \). I'll specifically look for mentions of "for every \( g \)" in the section around 2232 and also check between 2210 and 2245 to gather more context. This should help clarify things!
exec
/bin/zsh -lc "sed -n '2208,2245p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\mathbb{Z})$)
\item Elliptic genera (combinations of characters transforming as modular forms)
\item Quantum corrections at genus $g \geq 1$ (parametrized by modular forms)
\end{itemize}
\end{proof}

\begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
\label{cor:uniqueness-quantum}
Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
\begin{equation}
Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
\mathcal{A})\right)^\vee
\end{equation}
where the dual is taken with respect to Verdier duality.

This identification is constructive.
\end{corollary}

\begin{proof}[Proof of Corollary~\ref{cor:uniqueness-quantum}]
codex
```text
PE-10 scope quantifier
surface: thm:quantum-complementarity-main, cor:quantum-dual-complete, thm:higher-genus-inversion, thm:shifted-symplectic-complementarity
genus: theorem C duality/pairing -> g>=1; genus-0 handled separately; theorem B proved surface -> Koszul locus only
degree: theorem C uses ambient cohomology / eigenspaces; no free genus variable left implicit
AP32 weight tag: NA
AP139 free-var audit: all revised genus restrictions explicit in each clause
AP36: no iff claims introduced
verdict: ACCEPT
```

I’m patching the target file now. The edits are confined to four local surfaces: theorem C summary/statement plus the genus-0 duality exception, theorem B’s off-locus clause, and the two broken arguments inside the conditional BV upgrade.
exec
/bin/zsh -lc "rg -n -F \"Proof of Theorem~\\ref{thm:quantum-complementarity-main}\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "rg -n -F \"This completes the proof of Theorem~\\ref{thm:quantum-complementarity-main}\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1740:This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere
exec
/bin/zsh -lc "sed -n '1435,1742p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{equation}
satisfying $\sigma^2 = \mathrm{id}$.
\end{lemma}

\begin{proof}[Proof of Lemma~\ref{lem:verdier-involution-moduli}]
\emph{Construction.}
By Corollary~\ref{cor:duality-bar-complexes-complete}, the Verdier-Koszul pairing
identifies:
\begin{equation}
\mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A})) \xrightarrow{\sim}
H^*(\bar{B}^{(g)}(\mathcal{A}^!))^\vee
\end{equation}
Since $(\mathcal{A}^!)^! \simeq \mathcal{A}$ (Koszul involutivity,
Theorem~\ref{thm:chiral-koszul-duality}), we also have:
\begin{equation}
\mathbb{D}': H^*(\bar{B}^{(g)}(\mathcal{A}^!)) \xrightarrow{\sim}
H^*(\bar{B}^{(g)}(\mathcal{A}))^\vee
\end{equation}
The composition $(\mathbb{D}')^\vee \circ \mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A}))
\to H^*(\bar{B}^{(g)}(\mathcal{A}))$ is the identity (by involutivity of Verdier









thinking
**Analyzing proof adjustments**

The proof doesn't itself demonstrate duality; that's covered earlier in the corollary. Step 8 might not need adjustments without restrictions on g. I think the theorem should summarize the corollary, but there could be inconsistencies if it uses g=0. The only spot in the proof mentioning this seems to be line 1541, which is more general. The user states that Q_0 contradicts Q_g duality, so I’m contemplating incorporating a genus-0 exception while still considering any contradictions.
thinking
**Considering adjustments for corollaries**

The explicit finding from "Theorem B clause (b)" points toward limitations with the C1 genus-0 boundary case. I'd like to adjust the corollary to specify `g≥1` and perhaps add remarks around lines 1211 and 2240. However, I need to be cautious about cross-references to corollaries in other files, especially since the user said not to touch those. The theorem at line 1254 uses a corollary without restrictions on g, so further inspection is needed. Maybe a patch for `For each g≥1` could work.
thinking
**Adjusting the corollary context**

I see that the corollary is in a section on "genus g quantum corrections." It might make sense to set it as, "Given genus-g corrections," and include a note specifying for `g≥1`. This seems like a minimal and effective adjustment to clarify the context without disrupting the overall structure. Keeping it simple could help ensure that the user easily understands the intended application while adhering to the relevant restrictions.
thinking
**Clarifying proof language**

I’m working on part (iii) of the proof, where I’m comparing the map and Lagrangian eigenspaces on the ambient complex. Since the theorem is already conditional, adding another condition in part (iii) seems fine. However, I realize that I can't just state that "bar-side eigenspaces are Lagrangian" without some important caveats. So, I need to choose my wording more carefully to make sure it reflects the nuance.
thinking
**Exploring theorem adjustments**

I think I need a clearer opening for the theorem, like something that states it "extends to all genera at the scalar level." That sounds better. Also, I'm considering how to adjust the wording of "Let \cA be a modular pre-Koszul chiral algebra" and include the definition and axioms, MK1 to MK3. I feel like these tweaks will help clarify my ideas!
thinking
**Evaluating theorem adjustments**

I'm considering that the theorem and remark might still conflict with the earlier corollary. Maybe I can do a minimal patch to corollary and also line 1254/2240? If I change the corollary to "For each g ≥ 1," then the theorem `thm:kodaira-spencer-chiral-complete` should be fine since Kodaira-Spencer makes sense for g ≥ 1, right? However, the theorem statement is lacking details. Maybe I should keep the corollary's current wording but clarify that at genus 0 the bar-side duality doesn’t match the Verdier eigenspace splitting. This acknowledges some complexities but could address the user's request regarding genus-0 exceptions without causing further issues. So, I think I should focus on patching the theorem summary instead of adjusting the corollary to avoid a cascading effect.
thinking
**Clarifying the theorem statement**

I'm thinking about mentioning in the theorem statement or remark that the "duality clause refers to the S-level eigenspaces," while noting that the genus-0 bar-side spectral-sequence shadow is handled separately in Step II. However, I wonder if that explanation fully resolves the issue. There might be lingering concerns that I need to address. It’s important for me to ensure clarity while not getting too complex or convoluted in my explanation!
thinking
**Considering mathematical theorems**

I'm pondering whether to add that there might be no change, but it seems like the theorem could involve the tangent space of moduli. For g=0, the tangent is 0, which could still hold true, but there might be a logical issue if it references a corollary with g≥1 without clarification. Still, the theorem uses `\overline{\mathcal M}_g`, so g might encompass all cases. Maybe it's alright to ignore g=0 and leave it at that.
thinking
**Strengthening coherence in proof**

I’m thinking it might be a good idea to keep the collapse statement because the later lemma in the same section actually proves it. In the theorem proof, I can say something like, "The E_2 collapse is proved separately in Lemma\ref{lem:e2-collapse-higher-genus}." I should add one sentence at the end of the proof to enhance coherence. It sounds like a solid plan to ensure everything ties together nicely.

thinking
**Evaluating patching strategy**

I think the patch might have failed due to spaces or because the earlier line context was too broad. I should consider applying smaller patches with a more precise context. It seems like using `sed` around specific sections could be a way to address this issue. I need to inspect the exact snippets to ensure everything works correctly. That's probably the most efficient approach to take.
codex
The first patch failed on context matching, so I’m re-reading the exact local chunks and applying the edits in smaller hunks. No scope change.
exec
/bin/zsh -lc "sed -n '454,520p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4101,4160p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1206,1224p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2214,2232p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '56,84p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1698,1710p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
\index{bar-cobar inversion!higher genus}
\textup{[}Regime: curved-central on the Koszul locus;
filtered-complete off it
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

\smallskip\noindent
The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.

Let $\cA$ be a modular pre-Koszul chiral algebra
\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral}},
axioms \textup{MK1--MK3)}.
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Koszul locus.}
For each genus $g \geq 0$, the bar-cobar counit is a
quasi-isomorphism:
\[\psi_g \colon \Omega_g(\bar{B}_g(\cA))
\xrightarrow{\;\sim\;} \cA_g,\]
where $\cA_g$ denotes the genus-$g$ component.
The spectral sequence $E_1^{p,q}(g) \Rightarrow
 succeeded in 52ms:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}
\label{thm:quantum-complementarity}
\index{deformation-obstruction complementarity|textbf}
\index{Lagrangian!complementarity|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
for the ambient complex and homotopy eigenspaces of
Definition~\textup{\ref{def:complementarity-complexes}}.

\smallskip\noindent
\textbf{H-level \textup{(}homotopy\textup{)}.}
For each genus $g \geq 0$:
 succeeded in 52ms:
\mathcal{A}^!)))^\vee
\end{equation}
\end{proof}

\begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
\label{cor:quantum-dual-complete}
For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
\begin{equation}
Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
\end{equation}
with respect to the Verdier pairing.
\end{corollary}

\begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
Immediate from Lemma~\ref{lem:ss-duality-complete} by taking the sum over all $(p,q)$ with 
$p+q = n$ fixed:
\begin{equation}
Q_g(\mathcal{A}) = \bigoplus_{p+q=n} (E_\infty^{p,q,g})_{\mathcal{A}} \cong 
\bigoplus_{p+q=n} ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee = Q_g(\mathcal{A}^!)^\vee
 succeeded in 50ms:

\emph{Verification at small genera.}

\emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
$\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
$1 + 0 = 1$.

\emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
(central extension, eigenvalue $+1$) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C}
\cdot \lambda$ (curvature, eigenvalue $-1$). Dimension check: $1 + 1 = 2$.

 succeeded in 52ms:
\begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
\label{cor:uniqueness-quantum}
Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
\begin{equation}
Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
\mathcal{A})\right)^\vee
\end{equation}
where the dual is taken with respect to Verdier duality.

This identification is constructive.
\end{corollary}

\begin{proof}[Proof of Corollary~\ref{cor:uniqueness-quantum}]
By the direct sum property (Lemma~\ref{lem:trivial-intersection-complete}) and exhaustion 
(Lemma~\ref{lem:exhaustion-complete}), we have:
\begin{equation}
H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!)
\end{equation}
 succeeded in 52ms:
 curve~$X$ and every genus $g \geq 0$, the cohomology of the ambient
 complex splits as
 \begin{equation}\label{eq:complementarity-summary}
 H^*(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA))
 \;=\;
 Q_g(\cA) \;\oplus\; Q_g(\cA^!),
 \end{equation}
 where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
 the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
 Q_g(\cA^!)^\vee$
 \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.

\item \emph{Shifted-symplectic Lagrangian upgrade
 \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
 When the relative bar family
 $R\pi_{g*}\barB^{(g)}(\cA)$ is perfect
 \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
 Verdier pairing $\langle -,- \rangle_{\mathbb{D}}$ on the ambient
 complex $\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g,
exec
/bin/zsh -lc "sed -n '1888,1988p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!)
\cong H^*(\overline{\mathcal{M}}_1, Z(\mathcal{H}_\kappa))$ that we
computed in~\S\ref{sec:frame-complementarity} admits the following
bar-side $(-1)$-shifted symplectic refinement.
\index{BV algebra!shifted symplectic structure}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
curve $X$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{BV antibracket is $(-1)$-shifted Poisson.}
 The BV bracket $\{-,-\}_{\mathrm{BV}}$ on
 $\barB^{\mathrm{ch}}(\cA)$
 \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
 has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
 Non-degeneracy is guaranteed by the Koszul duality pairing
 \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
 and the Verdier intertwining
 $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
 \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
 Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.

exec
/bin/zsh -lc "sed -n '4160,4195p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
to ``quasi-isomorphism on all of~$\partial\overline{\mathcal{M}}_g$''
follows by a Mayer--Vietoris argument on the normal crossing boundary:
the boundary strata form a simple normal crossing divisor, so the
cone of~$i^*\psi_g$ is computed by iterated extensions along the
pairwise intersections $D_\Gamma \cap D_{\Gamma'}$, each of which
is a deeper boundary stratum where the same inductive hypothesis
applies. Hence $i^*\psi_g$ is a quasi-isomorphism.
\item Apply Lemma~\ref{lem:extension-across-boundary-qi} to
$X=U_g\sqcup\partial X$ and $f=\psi_g$. Since $j^*f$ and $i^*f$ are
quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
\end{enumerate}
Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
\end{proof}

\begin{remark}[Geometric substrate (Volume~II)]
\label{rem:theorem-b-lagrangian}
\index{Lagrangian self-intersection!Theorem B}
Volume~II interprets Koszul inversion as the reconstruction
of a Lagrangian from its clean self-intersection: the derived
self-intersection groupoid
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -62,6 +62,9 @@
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
apply_patch(auto_approved=true) exited 0 in 28ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..b0203e023a32e8314c2640b376ff165743552231
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..b0203e023a32e8314c2640b376ff165743552231
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -1214,3 +1214,4 @@
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
@@ -1218,3 +1219,7 @@
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
apply_patch(auto_approved=true) exited 0 in 37ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..9c7a0a4760ab0dc071cfa2e61012060963234f8d
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -1209,11 +1212,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..9c7a0a4760ab0dc071cfa2e61012060963234f8d
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -1209,11 +1212,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -477,7 +477,3 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
@@ -487,6 +483,10 @@
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
@@ -515,3 +515,5 @@
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
@@ -519,2 +521,8 @@
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..1e94141bc6ecff00f18fb3d03238d63420940ae7
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..1e94141bc6ecff00f18fb3d03238d63420940ae7
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -1719,3 +1719,4 @@
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
apply_patch(auto_approved=true) exited 0 in 46ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..4c5be3475787319b090347e4ddd8f60970319234
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..4c5be3475787319b090347e4ddd8f60970319234
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -2232,3 +2232,4 @@
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
apply_patch(auto_approved=true) exited 0 in 37ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..e4f8c87682fa9007f930a2444b9d55d32692cd45
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -2213,7 +2230,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..e4f8c87682fa9007f930a2444b9d55d32692cd45
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -2213,7 +2230,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -1917,8 +1917,14 @@
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
@@ -1937,8 +1943,12 @@
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
@@ -1952,14 +1962,12 @@
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
@@ -1969,6 +1977,8 @@
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
@@ -1976,5 +1986,4 @@
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
@@ -1986,15 +1995,14 @@
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
apply_patch(auto_approved=true) exited 0 in 33ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..60c241ef7ff9784fa60517aeb0681a13d18aa268
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..60c241ef7ff9784fa60517aeb0681a13d18aa268
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -4128,4 +4128,3 @@
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
@@ -4147,17 +4146,2 @@
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
@@ -4197,4 +4181,26 @@
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
apply_patch(auto_approved=true) exited 0 in 32ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..32be7bf4b33d46890918d32e9561de7671e7fd17
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4126,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4144,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4179,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..32be7bf4b33d46890918d32e9561de7671e7fd17
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4126,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4144,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4179,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

codex
The main edits are in place. I’m doing a focused reread on the modified sections and a grep pass for the remaining genus-0/all-genera duality wording so I can catch any local drift before I close.
exec
/bin/zsh -lc "rg -n -F \"Q_0(\\cA"'^!)=0" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Q_g(\\cA) \\cong Q_g(\\cA"'^!)''^'"\\vee\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Q_g(\\mathcal{A}) \\cong Q_g(\\mathcal{A}"'^!)''^'"\\vee\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '56,84p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '454,525p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1698,1710p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1206,1226p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1888,1995p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
69: $Q_0(\cA^!)=0$
526:Q_0(\cA^!)=0.
2311:At genus~$0$: $Q_0(\cA)=\mathbb{C}$, $Q_0(\cA^!)=0$ (tree-level,
 succeeded in 51ms:
66: identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
520:Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 succeeded in 52ms:
1226:Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
exec
/bin/zsh -lc "sed -n '4101,4205p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
= ((E_{r+1})_{\mathcal{A}^!})^\vee
\end{equation}

\emph{$E_\infty$ page}: Taking the limit $r \to \infty$:
\begin{equation}
(E_\infty^{p,q,g})_{\mathcal{A}} \cong ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee
\end{equation}

But $E_\infty^{*,*,g} = \text{gr}^g H^*$ by definition, so:
\begin{equation}
\text{gr}^g H^{p+q}(\bar{B}(\mathcal{A})) \cong (\text{gr}^g H^{p+d-q}(\bar{B}(
\mathcal{A}^!)))^\vee
\end{equation}
\end{proof}

\begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
\label{cor:quantum-dual-complete}
For each genus $g \geq 1$ and every Koszul dual chiral pair
$(\mathcal{A}, \mathcal{A}^!)$:
\begin{equation}
 succeeded in 52ms:
The Heisenberg complementarity
of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
polarization:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}
\label{thm:quantum-complementarity}
\index{deformation-obstruction complementarity|textbf}
\index{Lagrangian!complementarity|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
for the ambient complex and homotopy eigenspaces of
Definition~\textup{\ref{def:complementarity-complexes}}.

 succeeded in 52ms:
\dim Q_g(\mathcal{A}) + \dim Q_g(\mathcal{A}^!) = \dim H^*(\overline{\mathcal{M}}_g,
Z(\mathcal{A}))
\end{equation}
\end{lemma}

\begin{proof}[Proof of Lemma~\ref{lem:exhaustion-complete}]
Since $\sigma^2 = \mathrm{id}$ on the finite-dimensional vector space
$V = H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$, the minimal polynomial of
$\sigma$ divides $t^2 - 1 = (t-1)(t+1)$. Over $\mathbb{C}$, every vector decomposes
uniquely into $\pm 1$ eigenvectors via the projectors
$\pi^+ = \frac{1}{2}(\mathrm{id} + \sigma)$ and
$\pi^- = \frac{1}{2}(\mathrm{id} - \sigma)$. Therefore:
\begin{equation}
 succeeded in 52ms:
 curve~$X$ and every genus $g \geq 0$, the cohomology of the ambient
 complex splits as
 \begin{equation}\label{eq:complementarity-summary}
 H^*(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA))
 \;=\;
 Q_g(\cA) \;\oplus\; Q_g(\cA^!),
 \end{equation}
where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
 the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
 identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
 class is $\sigma$-fixed, so
 $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
 $Q_0(\cA^!)=0$
 \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.

\item \emph{Shifted-symplectic Lagrangian upgrade
 \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
 When the relative bar family
 $R\pi_{g*}\barB^{(g)}(\cA)$ is perfect
 succeeded in 50ms:
Proposition~\ref{prop:ptvv-lagrangian} upgrades the Verdier side to a
proved shifted-symplectic statement on the ambient complex~$C_g$. The
direct bar-side realization of a $(-1)$-shifted symplectic chart on
$L_g = \barB^{(g)}(\cA)[1]$ would require the additional BV package of
Chapter~\ref{ch:bv-brst}. The following theorem records that bar-side
upgrade conditionally.

\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
\label{thm:shifted-symplectic-complementarity}
\index{shifted symplectic!(-1)-shifted|textbf}
\index{Lagrangian!complementarity!shifted symplectic|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Assume the conditional BV package of
Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
genus-$1$ complementarity
$Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!)
\cong H^*(\overline{\mathcal{M}}_1, Z(\mathcal{H}_\kappa))$ that we
computed in~\S\ref{sec:frame-complementarity} admits the following
 succeeded in 52ms:

Every vertex genus in $\Gamma$ is strictly smaller than $g$: in the separating case,
$g=g_1+g_2$ with $g_1,g_2 \geq 0$ and each $g_i < g$ (note: one component may have genus~$0$, which is the base case of the induction); in the non-separating case, the single vertex has genus $g-1 < g$. In either case, the induction hypothesis applies to each vertex. Tensor products of quasi-isomorphisms
are quasi-isomorphisms by the K\"unneth formula for factorization
algebras at nodes: the factorization tensor product at a node is
computed fiberwise over the normalization, reducing to the plain
tensor product of chain complexes over the ground field, which
preserves quasi-isomorphisms by K\"unneth. This yields the claim.
\end{proof}

\begin{lemma}[Extension across boundary; \ClaimStatusProvedHere]\label{lem:extension-across-boundary-qi}
Let $X$ be a stack with open-closed decomposition $X = U \sqcup Z$ (with
$j:U\hookrightarrow X$, $i:Z\hookrightarrow X$). For a morphism of complexes
$f:K\to L$ on $X$, if $j^*f$ and $i^*f$ are quasi-isomorphisms, then $f$ is a
quasi-isomorphism.
\end{lemma}

\begin{proof}
Let $C=\operatorname{Cone}(f)$. It suffices to prove $C$ is acyclic.
From $j^*f$ and $i^*f$ quasi-isomorphisms, $j^*C$ and $i^*C$ are acyclic.
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..32be7bf4b33d46890918d32e9561de7671e7fd17
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4126,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4144,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4179,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc "sed -n '520,532p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Q_g(\cA) \cong Q_g(\cA^!)^\vee.
\end{equation}
At genus $0$, the unique point class is $\sigma$-fixed, so
\[
Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
\qquad
Q_0(\cA^!)=0.
\]
\end{theorem}

\begin{remark}\label{rem:lagrangian-decomp}
What one algebra sees as deformation, its dual sees as obstruction.
\end{remark}
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..32be7bf4b33d46890918d32e9561de7671e7fd17
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4126,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4144,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4179,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc 'rg -n -F "prop:lagrangian-eigenspaces" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\Omega(\\cA"'^!)" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"ClaimStatusProvedHere\" chapters/theory/higher_genus_complementarity.tex | sed -n '1,5p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
1797:Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
1801:\label{prop:lagrangian-eigenspaces}
1886:Proposition~\ref{prop:lagrangian-eigenspaces} establishes the
2052:(Proposition~\ref{prop:lagrangian-eigenspaces}(i)) is a
2069: Proposition~\ref{prop:lagrangian-eigenspaces}(iii):
 succeeded in 51ms:
224:\begin{lemma}[Involution splitting in characteristic~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
279:\ClaimStatusProvedHere]
353:\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
458:\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
651:\begin{lemma}[Genus filtration; \ClaimStatusProvedHere]
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..32be7bf4b33d46890918d32e9561de7671e7fd17
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4126,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4144,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4179,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}


thinking
**Investigating theorem heading**

I’m searching the local line 1254 section to see if the theorem heading includes the term “Regime ... all genera.” This could indicate a potential issue. I’ll take a closer look at this small part to understand better. It’s important to get this right, as understanding theorem headings is key for accurate analysis. Let’s see what I can find and clarify any possible concerns!
codex
I’ve cleared the explicit bad citations and the bar/cobar object switch. There is one remaining consistency check I’m doing: local theorems that cite the now `g>=1` duality corollary without saying `g>=1`, to see whether they need a short scope line or whether their existing hypotheses already force it.
exec
/bin/zsh -lc "sed -n '1244,1268p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2232,2248p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Corollary~\\ref{cor:quantum-dual-complete}\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
This completes Step~II: Verdier duality on configuration spaces
induces a duality of spectral sequences and a perfect pairing
between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
\end{proof}

\subsection{Step III: decomposition and complementarity}

\begin{proof}[Step III: Steps 7-10]

\emph{Step 7: Center action on moduli space cohomology.}

\begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
\label{thm:kodaira-spencer-chiral-complete}
\index{Kodaira--Spencer map|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
\to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
\begin{equation}
 succeeded in 51ms:
1235:\begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
1270:\mathcal{A}^!))^\vee$ be the Verdier isomorphism of Corollary~\ref{cor:quantum-dual-complete}.
2266:By Verdier duality (Corollary~\ref{cor:quantum-dual-complete}):
 succeeded in 51ms:
\item Partition functions of chiral algebras (transformed under $\text{Sp}(2g, 
\mathbb{Z})$)
\item Elliptic genera (combinations of characters transforming as modular forms)
\item Quantum corrections at genus $g \geq 1$ (parametrized by modular forms)
\end{itemize}
\end{proof}

\begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
\label{cor:uniqueness-quantum}
Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
$\mathcal{A}$, the
Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
\begin{equation}
Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
\mathcal{A})\right)^\vee
\end{equation}
where the dual is taken with respect to Verdier duality.
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..32be7bf4b33d46890918d32e9561de7671e7fd17
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4126,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4144,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4179,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc 'rg -n -F "thm:kodaira-spencer-chiral-complete" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
541:Step~III (from Theorem~\ref{thm:kodaira-spencer-chiral-complete})
1256:\label{thm:kodaira-spencer-chiral-complete}
1279:\begin{proof}[Proof of Theorem~\ref{thm:kodaira-spencer-chiral-complete}]
1774:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}, Step~7).
1847:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}) and
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..32be7bf4b33d46890918d32e9561de7671e7fd17
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4126,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4144,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4179,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}


thinking
**Considering theorem adjustments**

I'm thinking about patching the scope of my theorem. The user asked for only four findings, so maybe it's unnecessary. To avoid any inconsistencies from a corollary restriction, I might consider adjusting the theorem scope to g≥1. I’m also wondering if I should also patch the introduction summary line, but that may not be an issue. Let’s take a quick look at the theorem statement to see if it needs any simple updates.
exec
/bin/zsh -lc "sed -n '1252,1284p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\emph{Step 7: Center action on moduli space cohomology.}

\begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
\label{thm:kodaira-spencer-chiral-complete}
\index{Kodaira--Spencer map|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
\to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
\begin{equation}
\rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
\end{equation}
constructed from the Gauss--Manin connection on the chiral homology sheaf.

This action interacts with Verdier duality via anti-commutativity: let
$\mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A})) \xrightarrow{\sim} H^*(\bar{B}^{(g)}(
\mathcal{A}^!))^\vee$ be the Verdier isomorphism of Corollary~\ref{cor:quantum-dual-complete}.
Then for every $z \in Z(\mathcal{A})$ and $v \in T_{[\Sigma_g]}\overline{\mathcal{M}}_g$:
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..32be7bf4b33d46890918d32e9561de7671e7fd17
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1701,7 +1717,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1915,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1941,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1960,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1993,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2238,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4126,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4144,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4179,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -1245,3 +1245,5 @@
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
@@ -1257,6 +1259,7 @@
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
apply_patch(auto_approved=true) exited 0 in 39ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}



thinking
**Considering compilation options**

This task is a bit time-consuming. I think about running `python`, but maybe that won't work. Using `rg` seems better, given the instructions emphasize strong local verification. Since the repo is LaTeX heavy, I should consider the build-surface skill, even though the user didn't mention it. AGENTS suggest utilizing skills when appropriate. Running `latexmk -pdf` might be overkill unless necessary. I wonder if a simpler local syntax check would suffice, but it may be risky without further knowledge.
thinking
**Exploring build options**

I’m considering simpler commands, like running `grep -n "^\\begin{theorem"`, but that might not be efficient. I think about running `tectonic --keep-logs`, but I'm unsure. It might be worth inspecting the repo for the build command in the CLAUDE or Makefile since reading the CLAUDE was required but not mandatory in this case. I could also look for an existing `make` command. Let's see if there’s a Makefile or any useful scripts to help streamline this process.
codex
The proof surfaces now read coherently. I’m doing one verification step beyond reread: checking the repo’s local build entrypoint so I can run the narrowest compile/syntax pass available against this file rather than guess.
exec
/bin/zsh -lc "rg --files -g 'Makefile' -g 'latexmkrc' -g 'Tectonic.toml' -g '*.mk' -g '*.sh' | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"latexmk|tectonic|pdflatex|xelatex|lualatex|make pdf|make chapter|build\" README* CLAUDE.md .github -g '"'!**/*.png'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
scripts/wave2_launcher.sh
scripts/build.sh
scripts/integrity_gate.sh
scripts/verify_edit.sh
Makefile
 exited 2 in 50ms:
rg: .github: No such file or directory (os error 2)
README.md:60:| Standalone papers | 28 building PDFs |
README.md:65:# Kill any competing pdflatex, then build
README.md:66:pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
README.md:73:Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).
README.md:89:  Makefile                  build system
CLAUDE.md:562:AP17: After writing ANY new theorem, IMMEDIATELY audit before building next result.
CLAUDE.md:798:AP127: Cross-refs to migrated chapters. When migrating \input{chapter} between volumes, immediately add \phantomsection\label{} stubs for EVERY label in the migrated file, and grep for all \ref{} pointing to those labels. Never leave a bare \ref to a label that no longer exists in the build.
CLAUDE.md:875:AP112: Never trust stale page counts. Verify against fresh builds.
CLAUDE.md:906:AAP15: Serialize builds or use isolated worktrees. Parallel pdflatex kills.
CLAUDE.md:936:/build                      Build all three volumes, tests, census
CLAUDE.md:955:pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I
CLAUDE.md:963:CAUTION: Watcher spawns competing pdflatex; always kill before builds.
CLAUDE.md:967:1. Read this file. 2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`. 3. Tests: `make test`. 4. `git log --oneline -10`. 5. Read .tex source before any edit (never from memory). 6. After each change: build+test. After each correction: grep ALL THREE volumes (AP5). 7. Never guess a formula: compute or cite. Check landscape_census.tex (AP1). 8. Apply convergent writing loop to all prose. 9. Session end: build all three volumes, run tests, summarize errors by class. 10. Before first Edit, read the HOT ZONE section (HZ-1 through HZ-10) and run the Pre-Edit Verification Protocol mental check: is the pending edit touching an r-matrix, kappa, bar complex, label, Vol III kappa, cross-volume formula, scope quantifier, or differential form? If yes, fill the corresponding PE-1..PE-12 template as a fenced block in the reply BEFORE invoking Edit, ending with `verdict: ACCEPT`.
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

codex
I found the repo’s documented verification path. I’m running the standard Vol I fast build now, using the repo’s own guidance, so I can catch any label or LaTeX regressions introduced by the patch.
exec
/bin/zsh -lc 'pkill -9 -f pdflatex' in /Users/raeez/chiral-bar-cobar exited 3 in 51ms:
sysmon request failed with error: sysmond service not found
pkill: Cannot get process list
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

codex
The build is still running without emitting intermediate output, so I’m letting it continue rather than interrupting it. Once it returns, I’ll do a final reread against the exact changed regions and the build result.
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}


thinking
**Considering output issues**

I’m not getting any output, and I'm wondering if the process is stuck due to a build issue. Should I check the session status by sending a ctrl-c command? But waiting a little longer might be less expensive. After 30 seconds with no output, I think about looking into the processes or build log instead. Maybe a simple `ps` would suffice? I might need to consider waiting a bit longer before taking action.
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

 exited 2 in 2m 44s:
   2650pp, 147 undef citations, 867 undef references, 2 rerun requests, 177 overfull, 387 underfull
── Pass 2 / 4 ──
   2367pp, 20 undef citations, 178 undef references, 1 rerun requests, 148 overfull, 329 underfull
── Pass 3 / 4 ──
./scripts/build.sh: line 64: 39879 Killed: 9               $TEX $TEXFLAGS main.tex > "$RUN_LOG" 2>&1
   ?pp, 0 undef citations, 31 undef references, 0 rerun requests, 29 overfull, 64 underfull
✗ Build failed.
  Logs: .build_logs/tex-build.stdout.log and main.log
make: *** [fast] Error 137

thinking
**Investigating Build Failure**

It seems like the build failed because it was killed, possibly due to an out-of-memory (OOM) issue. I need to check the logs to see if my changes caused the error since it’s not just a LaTeX error. I'll inspect the tail of the logs to look for any relevant messages. I’m thinking I should use exec_command to tail the logs and grep for my specific file or any identified errors. Let's get to the bottom of this!
exec
/bin/zsh -lc 'tail -n 80 .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"higher_genus_complementarity|Undefined control sequence|LaTeX Error|Emergency stop|Runaway argument|Missing \\\\"'$ inserted|Killed" main.log .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
 succeeded in 52ms:
main.log:1475:Runaway argument?
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}


thinking
**Inspecting log file**

I need to take a closer look at the main.log file, specifically around line 1475. I'm wondering if our recent edits might have caused an issue, like a runaway process. It’s probably a good idea to check the lines around this point to see what could have gone wrong. Let’s dig into the log and see if we can figure it out from there!
codex
The fast build ended with the TeX process being killed, but the log now shows a real syntax signal near `main.log:1475`. I’m opening that exact log region before assuming it’s just resource pressure.
exec
/bin/zsh -lc "sed -n '1460,1495p' main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1488,1515p' main.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 3 \"Runaway argument\\?|File: chapters/theory/higher_genus_complementarity.tex|l\\.[0-9]+\" main.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(/usr/local/texlive/2025/texmf-dist/tex/latex/ebgaramond/T1EBGaramond-OsF.fd
File: T1EBGaramond-OsF.fd 2023/03/19 (autoinst) Font definitions for T1/EBGaram
ond-OsF.
)
LaTeX Font Info:    Font shape `T1/EBGaramond-OsF/m/n' will be
(Font)              scaled to size 10.95pt on input line 589.

(./main.aux (./chapters/frame/preface.aux) (./chapters/theory/introduction.aux)
(./chapters/frame/heisenberg_frame.aux)
(./chapters/theory/algebraic_foundations.aux)
(./chapters/theory/three_invariants.aux)
(./chapters/theory/configuration_spaces.aux)
(./chapters/theory/bar_construction.aux)
(./chapters/theory/cobar_construction.aux)
(./chapters/theory/bar_cobar_adjunction.aux))
Runaway argument?
{\contentsline {proposition}{\ifthmt@listswap Proposition~9.7.5\else \ETC.
! File ended while scanning use of \@writefile.
<inserted text> 
                \par 
 succeeded in 51ms:
Here is how much of TeX's memory you used:
 37730 strings out of 473190
 708027 string characters out of 5715801
 1185947 words of memory out of 5000000
 60442 multiletter control sequences out of 15000+600000
 568085 words of font info for 41 fonts, out of 8000000 for 9000
 1141 hyphenation exceptions out of 8191
 116i,1n,121p,461b,233s stack positions out of 10000i,1000n,20000p,200000b,200000s
!  ==> Fatal error occurred, no output PDF file produced!
 succeeded in 52ms:
1472-(./chapters/theory/bar_construction.aux)
1473-(./chapters/theory/cobar_construction.aux)
1474-(./chapters/theory/bar_cobar_adjunction.aux))
1475:Runaway argument?
1476-{\contentsline {proposition}{\ifthmt@listswap Proposition~9.7.5\else \ETC.
1477-! File ended while scanning use of \@writefile.
1478-<inserted text> 
1479-                \par 
1480:l.589 \begin{document}
1481-                      
1482-I suspect you have forgotten a `}', causing me
1483-to read past where you wanted me to stop.
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}


thinking
**Investigating file issues**

I'm looking into a runaway issue from reading the .aux file, which might be unrelated or based on stale data. It could also stem from unmatched braces from a previous run that generated the toc/.aux files. I should check recent changes, especially with theorem or remark titles that might be contributing to the problem. Since the runaway is specifically in the contentsline around proposition 9.7.5, I need to inspect the .aux file for chapter information and use rg for searching.
exec
/bin/zsh -lc "rg -n \"Proposition~9\\.7\\.5|9\\.7\\.5|Runaway|contentsline \\{proposition\\}\" chapters/**/*.aux main.aux *.aux" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Off-locus coderived continuation kept separate|Bar-side eigenspaces lift the ambient Lagrangian polarization|Quantum complementarity as Lagrangian polarization|Higher genus inversion" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 483

chapters/examples/level1_bridge.aux:25:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~D.2.1\else \numberline {D.2.1}Proposition\fi \thmtformatoptarg {Level-$1$ $\kappa $ reduction; }}{1709}{proposition.D.2.1}\protected@file@percent }
chapters/examples/level1_bridge.aux:37:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~D.3.1\else \numberline {D.3.1}Proposition\fi \thmtformatoptarg {Cubic shadow vanishing at level~$1$; }}{1709}{proposition.D.3.1}\protected@file@percent }
chapters/examples/w3_holographic_datum.aux:63:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~L.5.1\else \numberline {L.5.1}Proposition\fi \thmtformatoptarg {Action of $\Lambda _0$ on primaries; }}{2115}{proposition.L.5.1}\protected@file@percent }
chapters/theory/cobar_construction.aux:116:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~7.0.38\else \numberline {7.0.38}Proposition\fi \thmtformatoptarg {Explicit cobar-bar augmentation; }}{390}{proposition.7.0.38}\protected@file@percent }
chapters/theory/cobar_construction.aux:145:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~7.0.46\else \numberline {7.0.46}Proposition\fi \thmtformatoptarg {Cobar as modular shadow carrier}}{393}{proposition.7.0.46}\protected@file@percent }
chapters/theory/cobar_construction.aux:199:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~7.1.11\else \numberline {7.1.11}Proposition\fi \thmtformatoptarg {Curvature of the affine bar complex; }}{400}{proposition.7.1.11}\protected@file@percent }
chapters/examples/moonshine.aux:12:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~C.1.1\else \numberline {C.1.1}Proposition\fi \thmtformatoptarg {$\kappa (V^\natural ) = 12$; }}{1703}{proposition.C.1.1}\protected@file@percent }
main.aux:58:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.0.1\else \numberline {9.0.1}Proposition\fi \thmtformatoptarg {Homotopy transfer as rectification mechanism}}{563}{proposition.9.0.1}\protected@file@percent }
main.aux:89:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.3.5\else \numberline {9.3.5}Proposition\fi \thmtformatoptarg {Sign computation \cite  {LV12}; }}{566}{proposition.9.3.5}\protected@file@percent }
main.aux:116:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.5.2\else \numberline {9.5.2}Proposition\fi \thmtformatoptarg {$\mathsf  {L}_{\infty }$-relations for transferred structure \cite  {LV12}; }}{568}{proposition.9.5.2}\protected@file@percent }
main.aux:136:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.6.3\else \numberline {9.6.3}Proposition\fi \thmtformatoptarg {Transferred structure and bar complex \cite  {LV12}; }}{570}{proposition.9.6.3}\protected@file@percent }
main.aux:149:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.7.3\else \numberline {9.7.3}Proposition\fi \thmtformatoptarg {Trees as boundary strata; }}{572}{proposition.9.7.3}\protected@file@percent }
main.aux:158:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.7.5\else \numberline {9.7.5}Proposi
chapters/examples/lattice_foundations.aux:109:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~B.5.5\else \numberline {B.5.5}Proposition\fi \thmtformatoptarg {$D_4$ bar complex and triality; }}{1659}{proposition.B.5.5}\protected@file@percent }
chapters/examples/lattice_foundations.aux:111:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~B.5.6\else \numberline {B.5.6}Proposition\fi \thmtformatoptarg {$E_8$ bar complex and self-duality; }}{1660}{proposition.B.5.6}\protected@file@percent }
chapters/examples/lattice_foundations.aux:151:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~B.7.3\else \numberline {B.7.3}Proposition\fi \thmtformatoptarg {Sublattice maps; }}{1664}{proposition.B.7.3}\protected@file@percent }
chapters/examples/lattice_foundations.aux:179:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~B.9.1\else \numberline {B.9.1}Proposition\fi \thmtformatoptarg {Genus-1 partition function; }}{1667}{proposition.B.9.1}\protected@file@percent }
chapters/examples/lattice_foundations.aux:195:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~B.9.5\else \numberline {B.9.5}Proposition\fi \thmtformatoptarg {Niemeier theta series decomposition; }}{1669}{proposition.B.9.5}\protected@file@percent }
 succeeded in 53ms:
458:\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
1947:\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
4189:\begin{remark}[Off-locus coderived continuation kept separate]
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

codex
The build failure is coming from a pre-existing corrupted `main.aux` entry before TeX even starts processing the document body, so it’s not a trustworthy signal on this edit surface. I’m checking the repo’s local edit-verification script as a narrower fallback.
exec
/bin/zsh -lc "sed -n '1,220p' scripts/build.sh" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' scripts/verify_edit.sh" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
#!/bin/bash
# Converging build script for the chiral bar-cobar manuscript.
# Runs up to MAX_PASSES of pdflatex, stopping when references stabilize.
# Use this instead of raw pdflatex to avoid oscillation on large documents.

set -euo pipefail
cd "$(dirname "$0")/.."

MAX_PASSES=${1:-7}
TEX="pdflatex"
TEXFLAGS="-interaction=batchmode -file-line-error -synctex=0 -cnf-line=buf_size=1000000 -cnf-line=stack_size=20000"
LOG_DIR=".build_logs"
RUN_LOG="$LOG_DIR/tex-build.stdout.log"
LOCK_DIR="$LOG_DIR/.build.lock"

mkdir -p "$LOG_DIR"

acquire_lock() {
    local announced=0
    while ! mkdir "$LOCK_DIR" 2>/dev/null; do
 succeeded in 51ms:
#!/usr/bin/env bash
# verify_edit.sh — Post-edit verification for the chiral bar-cobar monograph.
#
# Checks recently modified .tex files for known false patterns (anti-patterns)
# that have recurred historically in this repository.
#
# Usage:
#   ./scripts/verify_edit.sh                    # check files modified in last 10 min
#   ./scripts/verify_edit.sh file1.tex file2.tex  # check specific files
#   ./scripts/verify_edit.sh --staged           # check git-staged files
#   ./scripts/verify_edit.sh --all              # check all .tex files
#
# Exit code: 0 if clean, 1 if anti-patterns found.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# ── Determine which files to check ──────────────────────────────────────
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc './scripts/verify_edit.sh chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 569ms:
verify_edit: checking 1 file(s)...

verify_edit: all checks passed.
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --stat -- chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da..660622a 100644
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@ with distinct logical statuses.
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 succeeded in 52ms:
 chapters/theory/higher_genus_complementarity.tex | 195 +++++++++++++----------
 1 file changed, 115 insertions(+), 80 deletions(-)
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc 'chktex -q -n1 -n2 -n8 -n24 -n46 chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 113ms:
Warning 40 in chapters/theory/higher_genus_complementarity.tex line 5: You should put punctuation outside inner math mode.
$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.  
               ^
Warning 40 in chapters/theory/higher_genus_complementarity.tex line 24: You should put punctuation outside inner math mode.
what~$\cA$ sees as obstruction,~$\cA^!$ sees as deformation.  
                                     ^
Warning 9 in chapters/theory/higher_genus_complementarity.tex line 44: `)' expected, found `}'.
 \textup{(}unconditional on the Koszul locus\textup{)}.}\;  
          ^
Warning 9 in chapters/theory/higher_genus_complementarity.tex line 44: `}' expected, found `)'.
 \textup{(}unconditional on the Koszul locus\textup{)}.}\;  
                                                    ^
Warning 9 in chapters/theory/higher_genus_complementarity.tex line 49: `)' expected, found `}'.
 \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.  
          ^
Warning 9 in chapters/theory/higher_genus_complementarity.tex line 49: `}' expected, found `)'.
 \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.  
                                                                ^
Warning 9 in chapters/theory/higher_genus_complementarity.tex line 53: `)' expected, found `}'.
\item \emph{Eigenspace decomposition \textup{(}unconditional on the  
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}


thinking
**Evaluating build issues**

I’m noticing that chktex is noisy and not particularly useful in this context. Instead, I might want to use the verify_edit script and look into why the build is failing due to the stale main.aux file. I should probably check if the math I inserted in the theorem title or remark caused the broken aux. The build error stemmed from an old proposition in main.aux, which is unrelated. I could run `git diff` to see if everything looks good. Now, I might need to close the build session and update plan statuses since we've completed the task.
Plan update
Patched the assigned theorem surfaces, re-read the modified sections, ran the repo’s `verify_edit.sh` on the target file, and attempted the standard fast build. The build is blocked by a pre-existing corrupted `main.aux` entry (`Proposition~9.7.5`) before the document body is processed, so it could not serve as a clean regression signal for this edit.
  ✓ Read required repo guidance and the target file context for the four findings
  ✓ Trace each cited dependency/circular reference and decide the strongest truthful fix
  ✓ Patch `chapters/theory/higher_genus_complementarity.tex` only, then re-read modified sections for coherence
  ✓ Verify findings resolved and summarize exact disposition of each
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..660622aeb70a1a1c34f466d1e713eb483fcb6078
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,30 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\label{rem:higher-genus-inversion-off-locus}
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}



thinking
**Inspecting modifications**

I need to inspect the final modified sections to check for any typos. I might consider opening a diff, but I’ve noticed an indentation issue on line 66 that might need attention, though it might not be necessary to patch the spacing. I also need to check if the new remark label could cause the metadata to go out of sync since it’s unreferenced in the theorem registry. To minimize drift, I’ll decide to remove that unused label. Similarly, I could also consider removing `\index`.
thinking
**Removing unreferenced label**

I’ve decided to patch the document by removing the new remark label to avoid any potential metadata drift. It seems like a sensible move since it keeps things tidy and ensures that everything is synced up correctly. Removing that label should help minimize any confusion down the line regarding references. It’s nice to have clarity in the metadata, so I’m glad I’m addressing this!
codex
One cleanup before I finish: the new off-locus remark doesn’t need a label, and dropping it avoids unnecessary metadata drift since the target file is the only allowed write surface.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -4189,3 +4189,2 @@
 \begin{remark}[Off-locus coderived continuation kept separate]
-\label{rem:higher-genus-inversion-off-locus}
 \index{bar-cobar inversion!off Koszul locus}
apply_patch(auto_approved=true) exited 0 in 39ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..e76a83b2a94fd7d989a352d4e2daaf3989e711fb
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,29 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..e76a83b2a94fd7d989a352d4e2daaf3989e711fb
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,29 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc './scripts/verify_edit.sh chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 67ms:

verify_edit: all checks passed.
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..e76a83b2a94fd7d989a352d4e2daaf3989e711fb
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,29 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '60,72p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '475,528p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1256,1272p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
    60	 \;=\;
    61	 Q_g(\cA) \;\oplus\; Q_g(\cA^!),
    62	 \end{equation}
    63	where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
    64	$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
    65	 the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
    66	 identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
    67	 class is $\sigma$-fixed, so
    68	 $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
    69	 $Q_0(\cA^!)=0$
    70	 \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
    71	
    72	\item \emph{Shifted-symplectic Lagrangian upgrade
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1894,2008p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1220,1248p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1718,1726p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4129,4207p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2240,2269p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   475	\textbf{H-level \textup{(}homotopy\textup{)}.}
   476	For each genus $g \geq 0$:
   477	\begin{enumerate}[label=\textup{(\roman*)}]
   478	\item \emph{Homotopy eigenspace decomposition.}
   479	 By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
   480	 \begin{equation}\label{eq:complementarity-decomp}
   481	 \mathbf{C}_g(\cA) \;\simeq\;
   482	 \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
   483	 \end{equation}
   484	 functorially in~$(\cA,\cA^!)$.
   485	
   486	\item \emph{Perfect duality for $g \geq 1$.}
   487	 For $g \geq 1$, Verdier duality induces a cochain-level pairing
   488	 $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
   489	 of cohomological degree $-(3g{-}3)$, anti-symmetric under the
   490	 Verdier involution~$\sigma$. Under this pairing, each summand in
   491	 \eqref{eq:complementarity-decomp} is Lagrangian, and
   492	 $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
   493	 non-degenerate pairing
   494	 $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
 succeeded in 51ms:
  1256	
  1257	\begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
  1258	\label{thm:kodaira-spencer-chiral-complete}
  1259	\index{Kodaira--Spencer map|textbf}
  1260	\textup{[Regime: curved-central on the Koszul locus; positive genus
  1261	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1262	
  1263	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
  1264	$g \geq 1$, and let $\pi: \mathcal{C}_g
  1265	\to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
  1266	\begin{equation}
  1267	\rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
  1268	\end{equation}
  1269	constructed from the Gauss--Manin connection on the chiral homology sheaf.
  1270	
  1271	This action interacts with Verdier duality via anti-commutativity: let
  1272	$\mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A})) \xrightarrow{\sim} H^*(\bar{B}^{(g)}(
 succeeded in 52ms:
  1894	$L_g = \barB^{(g)}(\cA)[1]$ would require the additional BV package of
  1895	Chapter~\ref{ch:bv-brst}. The following theorem records that bar-side
  1896	upgrade conditionally.
  1897	
  1898	\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
  1899	\label{thm:shifted-symplectic-complementarity}
  1900	\index{shifted symplectic!(-1)-shifted|textbf}
  1901	\index{Lagrangian!complementarity!shifted symplectic|textbf}
  1902	\textup{[Regime: curved-central on the Koszul locus; all genera
  1903	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1904	
  1905	Assume the conditional BV package of
  1906	Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
  1907	genus-$1$ complementarity
  1908	$Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!)
  1909	\cong H^*(\overline{\mathcal{M}}_1, Z(\mathcal{H}_\kappa))$ that we
  1910	computed in~\S\ref{sec:frame-complementarity} admits the following
  1911	bar-side $(-1)$-shifted symplectic refinement.
  1912	\index{BV algebra!shifted symplectic structure}
  1913	Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 succeeded in 52ms:
  1220	
  1221	\begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
  1222	\label{cor:quantum-dual-complete}
  1223	For each genus $g \geq 1$ and every Koszul dual chiral pair
  1224	$(\mathcal{A}, \mathcal{A}^!)$:
  1225	\begin{equation}
  1226	Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
  1227	\end{equation}
  1228	with respect to the Verdier pairing. At genus $0$, the
  1229	cohomological-shadow eigenspaces are instead
  1230	$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
  1231	and $Q_0(\mathcal{A}^!) = 0$
  1232	\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
  1233	\end{corollary}
  1234	
  1235	\begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
  1236	Immediate from Lemma~\ref{lem:ss-duality-complete} by taking the sum over all $(p,q)$ with 
  1237	$p+q = n$ fixed:
  1238	\begin{equation}
  1239	Q_g(\mathcal{A}) = \bigoplus_{p+q=n} (E_\infty^{p,q,g})_{\mathcal{A}} \cong 
 succeeded in 51ms:
  1718	\emph{Verification at small genera.}
  1719	
  1720	\emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
  1721	$\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
  1722	giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
  1723	$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
  1724	Theorem~\ref{thm:quantum-complementarity-main}.
  1725	
  1726	\emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 succeeded in 52ms:
  4129	
  4130	\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
  4131	\index{bar-cobar inversion!higher genus}
  4132	\textup{[}Regime: curved-central on the Koszul locus
  4133	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  4134	
  4135	\smallskip\noindent
  4136	The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.
  4137	
  4138	Let $\cA$ be a modular pre-Koszul chiral algebra
  4139	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral}},
  4140	axioms \textup{MK1--MK3)}.
  4141	\begin{enumerate}[label=\textup{(\alph*)}]
  4142	\item \emph{Koszul locus.}
  4143	For each genus $g \geq 0$, the bar-cobar counit is a
  4144	quasi-isomorphism:
  4145	\[\psi_g \colon \Omega_g(\bar{B}_g(\cA))
  4146	\xrightarrow{\;\sim\;} \cA_g,\]
  4147	where $\cA_g$ denotes the genus-$g$ component.
  4148	The spectral sequence $E_1^{p,q}(g) \Rightarrow
 succeeded in 51ms:
  2240	\end{proof}
  2241	
  2242	\begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
  2243	\label{cor:uniqueness-quantum}
  2244	Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
  2245	$\mathcal{A}$, the
  2246	Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
  2247	\begin{equation}
  2248	Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
  2249	\mathcal{A})\right)^\vee
  2250	\end{equation}
  2251	where the dual is taken with respect to Verdier duality.
  2252	
  2253	This identification is constructive.
  2254	\end{corollary}
  2255	
  2256	\begin{proof}[Proof of Corollary~\ref{cor:uniqueness-quantum}]
  2257	By the direct sum property (Lemma~\ref{lem:trivial-intersection-complete}) and exhaustion 
  2258	(Lemma~\ref{lem:exhaustion-complete}), we have:
  2259	\begin{equation}
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..e76a83b2a94fd7d989a352d4e2daaf3989e711fb
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,29 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}


thinking
**Clarifying theorem tagging**

In my summary of the contract, I've noted tags like `[FIXED]`, `[NARROWED]`, `[CONDITIONAL]`, and `[BLOCKED]`. For one finding, I moved the off-locus clause into a separate remark, leaving it conditional or unproven. I could tag it `[NARROWED]` for clarity since it wasn’t independently proved. The final summary recommends using tags, so for T02, I'll likely go with `[NARROWED]` because the theorem applies only to the Koszul locus. But it may also fit to say `[FIXED]` due to the changes made.
codex
Edited [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:458). The C1 surface now separates the genus-$0$ exception from the positive-genus duality claim, Theorem B no longer carries an unproved off-locus clause, and the C2 proof now stays on the correct bar-side objects.

Verification: `./scripts/verify_edit.sh chapters/theory/higher_genus_complementarity.tex` passed. `make fast` did not give a clean regression signal because TeX failed before the document body on a pre-existing corrupted `main.aux` entry (`Runaway argument` at `Proposition~9.7.5`), so I could not use the full build as a trustworthy check.

## Rectification Summary
- [NARROWED] finding 1 — [Theorem B](</Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4130>) is now only the proved Koszul-locus inversion statement; the off-locus coderived continuation was moved to a separate remark at [4189](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:4189), explicitly not proved here, which breaks the circular dependence on `prop:coderived-adequacy`.
- [FIXED] finding 2 — [Theorem C](</Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:475>) now states duality/Lagrangian claims only for `g >= 1` and records the genus-$0$ exception `Q_0(\cA)=H^0(...)`, `Q_0(\cA^!)=0`; the same exception is propagated in the summary and the duality corollary at [1221](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1221), and the small-genus check at [1720](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1720) now points back to that exception.
- [FIXED] finding 3 — [C2(i)](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1916) and its proof at [1961](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1961) now use the correct bar-side objects throughout: the adjoint BV map lands in `D_Ran(\barB(\cA))[1] \simeq \barB(\cA^!)[1]`, not `\Omega(\cA^!)`.
- [CONDITIONAL] finding 4 — [C2(iii)](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1947) no longer misapplies the center-side Lagrangian proposition directly to `L_g`; it now requires an explicit paired quasi-isomorphism `\chi_g: L_g \to \mathbf C_g(\cA)` and transports the proved ambient Lagrangian decomposition in the proof at [1998](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1998).
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index 12050da6d7989a4dd111a0f18eb0377af2c54927..e76a83b2a94fd7d989a352d4e2daaf3989e711fb
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -60,10 +60,13 @@
  \;=\;
  Q_g(\cA) \;\oplus\; Q_g(\cA^!),
  \end{equation}
- where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
- $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
- the Verdier involution~$\sigma$, and $Q_g(\cA) \cong
- Q_g(\cA^!)^\vee$
+where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
+$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
+ the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
+ identifies $Q_g(\cA) \cong Q_g(\cA^!)^\vee$; at $g=0$, the point
+ class is $\sigma$-fixed, so
+ $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
+ $Q_0(\cA^!)=0$
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
 
 \item \emph{Shifted-symplectic Lagrangian upgrade
@@ -472,20 +475,20 @@
 \textbf{H-level \textup{(}homotopy\textup{)}.}
 For each genus $g \geq 0$:
 \begin{enumerate}[label=\textup{(\roman*)}]
-\item \emph{Homotopy Lagrangian decomposition.}
- Verdier duality induces a cochain-level pairing
- $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
- of cohomological degree $-(3g{-}3) = -\dim_{\mathbb C}\cM_g$,
- anti-symmetric under the Verdier involution~$\sigma$.
+\item \emph{Homotopy eigenspace decomposition.}
  By Lemma~\textup{\ref{lem:involution-splitting}(a,c)},
  \begin{equation}\label{eq:complementarity-decomp}
  \mathbf{C}_g(\cA) \;\simeq\;
  \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
  \end{equation}
- with each summand Lagrangian for
- $\langle -,- \rangle_{\mathbb{D}}$.
+ functorially in~$(\cA,\cA^!)$.
 
-\item \emph{Perfect duality.}
+\item \emph{Perfect duality for $g \geq 1$.}
+ For $g \geq 1$, Verdier duality induces a cochain-level pairing
+ $\langle -,- \rangle_{\mathbb{D}}$ on~$\mathbf{C}_g(\cA)$
+ of cohomological degree $-(3g{-}3)$, anti-symmetric under the
+ Verdier involution~$\sigma$. Under this pairing, each summand in
+ \eqref{eq:complementarity-decomp} is Lagrangian, and
  $\langle -, - \rangle_{\mathbb{D}}$ restricts to a
  non-degenerate pairing
  $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
@@ -510,10 +513,18 @@
 $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
 $Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
 \textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
-are Lagrangians for the induced pairing on~$\mathcal{H}_g$, and
+are the $\pm 1$ eigenspaces of~$\sigma$.
+For $g \geq 1$, they are Lagrangians for the induced pairing
+on~$\mathcal{H}_g$, and
 \begin{equation}\label{eq:quantum-duality}
 Q_g(\cA) \cong Q_g(\cA^!)^\vee.
 \end{equation}
+At genus $0$, the unique point class is $\sigma$-fixed, so
+\[
+Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
+\qquad
+Q_0(\cA^!)=0.
+\]
 \end{theorem}
 
 \begin{remark}\label{rem:lagrangian-decomp}
@@ -1209,11 +1220,16 @@
 
 \begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
 \label{cor:quantum-dual-complete}
-For Koszul dual chiral algebras $(\mathcal{A}, \mathcal{A}^!)$:
+For each genus $g \geq 1$ and every Koszul dual chiral pair
+$(\mathcal{A}, \mathcal{A}^!)$:
 \begin{equation}
 Q_g(\mathcal{A}) \cong Q_g(\mathcal{A}^!)^\vee
 \end{equation}
-with respect to the Verdier pairing.
+with respect to the Verdier pairing. At genus $0$, the
+cohomological-shadow eigenspaces are instead
+$Q_0(\mathcal{A}) = H^0(\overline{\mathcal{M}}_0, Z(\mathcal{A}))$
+and $Q_0(\mathcal{A}^!) = 0$
+\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
 \end{corollary}
 
 \begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
@@ -1227,7 +1243,9 @@
 
 This completes Step~II: Verdier duality on configuration spaces
 induces a duality of spectral sequences and a perfect pairing
-between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$.
+between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
+the genus-$0$ cohomological-shadow exception is recorded in
+Theorem~\ref{thm:quantum-complementarity-main}.
 \end{proof}
 
 \subsection{Step III: decomposition and complementarity}
@@ -1239,10 +1257,11 @@
 \begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 \label{thm:kodaira-spencer-chiral-complete}
 \index{Kodaira--Spencer map|textbf}
-\textup{[Regime: curved-central on the Koszul locus; all genera
+\textup{[Regime: curved-central on the Koszul locus; positive genus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 
-Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair and let $\pi: \mathcal{C}_g
+Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
+$g \geq 1$, and let $\pi: \mathcal{C}_g
 \to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
 \begin{equation}
 \rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
@@ -1701,7 +1720,8 @@
 \emph{Genus $0$}: $\overline{\mathcal{M}}_0 = \mathrm{pt}$, so
 $\dim H^* = 1$. The involution $\sigma$ acts as $+1$ on $H^0$ (identity class),
 giving $Q_0(\mathcal{A}) = \mathbb{C}$, $Q_0(\mathcal{A}^!) = 0$. Dimension check:
-$1 + 0 = 1$.
+$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
+Theorem~\ref{thm:quantum-complementarity-main}.
 
 \emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
 For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
@@ -1898,12 +1918,18 @@
  $\barB^{\mathrm{ch}}(\cA)$
  \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
- Non-degeneracy is guaranteed by the Koszul duality pairing
- \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
- and the Verdier intertwining
- $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
- \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
- Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
+ Under the bracket-compatible Verdier comparison assumed in
+ Theorem~\textup{\ref{thm:bv-functor}}, the adjoint map
+ \[
+ x \longmapsto \{x,-\}_{\mathrm{BV}} \colon
+ \barB^{\mathrm{ch}}(\cA)
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))[1]
+ \simeq
+ \barB^{\mathrm{ch}}(\cA^!)[1]
+ \]
+ is a quasi-isomorphism, so this Poisson structure is
+ non-degenerate.
 
 \item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
@@ -1918,12 +1944,16 @@
  Proposition~\ref{prop:modular-deformation-truncation}) of the
  modular $L_\infty$-deformation object $\Definfmod(\cA)$
  (Theorem~\ref{thm:modular-homotopy-convolution}).
-\item \emph{Bar-side eigenspaces are Lagrangian.}
- The Verdier involution induces an involution on~$L_g$, and the
+\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
+ For $g \geq 1$, assume in addition that there is a quasi-isomorphism
+ of paired complexes
+ \[
+ \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
+ \]
+ intertwining the Verdier involution and the pairings. Then the
  eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
- complementary Lagrangian subspaces, with $L_g^+$ controlling
- deformations of~$\cA$ and $L_g^-$ controlling deformations
- of~$\cA^!$.
+ complementary Lagrangian subspaces, and
+ $H^*(L_g^+) = Q_g(\cA)$, $H^*(L_g^-) = Q_g(\cA^!)$.
 \end{enumerate}
 \end{theorem}
 
@@ -1933,33 +1963,32 @@
 has degree~$+1$ by Theorem~\ref{thm:config-space-bv}. A degree~$+1$
 Lie bracket is by definition a $(-1)$-shifted Poisson structure: the
 associated bivector field on the formal moduli problem has degree~$-1$.
-For non-degeneracy, the map
-$x \mapsto \{x, -\}_{\mathrm{BV}}$
-gives $\barB^{\mathrm{ch}}(\cA) \to
-\barB^{\mathrm{ch}}(\cA)^{\vee}[-1]$.
-The Verdier duality identification
-$\mathbb{D}(\barB(\cA)) \cong \Omega(\cA^!)$
-(Theorem~\ref{thm:bv-functor}) identifies
-$\barB^{\mathrm{ch}}(\cA)^{\vee}$ with $\Omega^{\mathrm{ch}}(\cA^!)$.
-On the Koszul locus, the bar-cobar adjunction
-(Theorem~\ref{thm:bar-cobar-isomorphism-main}) ensures that this
-map induces a quasi-isomorphism on cohomology, verifying
-non-degeneracy.
+Theorem~\ref{thm:config-space-bv} identifies this bracket with the
+configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
+gives a perfect pairing
+$\barB^{\mathrm{ch}}(\cA)\otimes \barB^{\mathrm{ch}}(\cA^!)\to\mathbb{C}$,
+and Theorem~\ref{thm:bv-functor} supplies the bracket-compatible
+Verdier comparison
+$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
+Therefore the adjoint of the BV bracket is identified with the
+Verdier duality map, hence is a quasi-isomorphism. This is precisely
+the required non-degeneracy.
 
 \emph{Part (ii).}
 Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
 bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
 axioms are inherited from the BV algebra axioms. The BV pairing on
-$\barB^{(g)}(\cA)$ (degree~$+1$ from the antibracket; equivalently,
-the non-degenerate pairing from the Koszul--Verdier construction of
-Corollary~\ref{cor:duality-bar-complexes-complete}) shifts to a
-pairing on $L_g$ of degree $+1 - 2 = -1$
+$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a
+quasi-isomorphism
+$\beta_g\colon \barB^{(g)}(\cA)\xrightarrow{\sim}
+(\barB^{(g)}(\cA))^\vee[1]$.
+After shifting by~$[1]$, $\beta_g$ becomes a pairing on $L_g$ of
+degree $+1 - 2 = -1$
 (each of the two inputs shifts by~$[-1]$).
 Invariance of the pairing (the cyclic property
 $\langle [x,y], z \rangle = \langle x, [y,z] \rangle$)
-follows from the BV relation
-$\{a, bc\} = \{a,b\}c \pm b\{a,c\}$ (Leibniz rule) applied to
-the pairing. By the Kontsevich--Pridham correspondence (a
+is exactly the bracket-compatibility built into the conditional BV
+package of Theorem~\ref{thm:bv-functor}. By the Kontsevich--Pridham correspondence (a
 non-degenerate invariant pairing of degree~$n$ on a dg Lie algebra
 $L$ endows $\mathrm{MC}(L)$ with an $n$-shifted symplectic
 structure~\cite{Pridham17}), the formal moduli
@@ -1967,19 +1996,18 @@
 symplectic.
 
 \emph{Part (iii).}
-The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
-anti-commutes with the Lie bracket:
-$\sigma[x,y] = -[\sigma x, \sigma y]$.
-(This follows from the sign reversal under Verdier duality: the
-antibracket involves the symplectic form on configuration space,
-and~$\mathbb{D}$ reverses the orientation of~$\overline{C}_n(X)$,
-hence reverses the sign of the symplectic form.)
-By the eigenspace argument of
-Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
-$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
-$(-1)$-shifted symplectic form. They are maximal isotropic (hence
-Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
-characteristic $\neq 2$.
+Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
+statement exists. Because~$\chi_g$ intertwines the involutions and the
+pairings, it identifies the $\sigma$-eigenspaces $L_g^\pm$ with the
+ambient homotopy eigenspaces
+$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
+then supplies a decomposition of~$\mathbf{C}_g(\cA)$ by complementary
+Lagrangians. Pulling that structure back along~$\chi_g$ shows that
+$L_g^+$ and~$L_g^-$ are isotropic. Since
+$L_g = L_g^+ \oplus L_g^-$ over a field of characteristic $\neq 2$,
+they are maximal isotropic, hence Lagrangian. Passing to cohomology
+gives $H^*(L_g^+) = Q_g(\cA)$ and
+$H^*(L_g^-) = Q_g(\cA^!)$.
 \end{proof}
 
 \begin{remark}[Genus-wise strictification]
@@ -2213,7 +2241,8 @@
 
 \begin{corollary}[Uniqueness of quantum corrections; \ClaimStatusProvedHere]
 \label{cor:uniqueness-quantum}
-Given genus-$g$ corrections $Q_g(\mathcal{A})$ for a chiral algebra $\mathcal{A}$, the 
+Given genus-$g$ corrections with $g \geq 1$ for a chiral algebra
+$\mathcal{A}$, the
 Koszul dual corrections $Q_g(\mathcal{A}^!)$ are \emph{uniquely determined} by:
 \begin{equation}
 Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
@@ -4100,8 +4129,7 @@
 
 \begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 \index{bar-cobar inversion!higher genus}
-\textup{[}Regime: curved-central on the Koszul locus;
-filtered-complete off it
+\textup{[}Regime: curved-central on the Koszul locus
 \textup{(}Convention~\textup{\ref{conv:regime-tags})].}
 
 \smallskip\noindent
@@ -4119,21 +4147,6 @@
 where $\cA_g$ denotes the genus-$g$ component.
 The spectral sequence $E_1^{p,q}(g) \Rightarrow
 H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
-
-\item \emph{Off the Koszul locus.}
-If $\cA$ leaves the Koszul locus \textup{(}admissible affine levels,
-minimal-model central charges\textup{)}, the bar-cobar object
-$\Omega_X \bar{B}_X(\cA)$ persists but becomes curved: $d^2 \neq 0$
-on the underlying complex, and the failure of inversion is
-measured by the shadow obstruction tower $\Theta_{\cA}^{\leq r}$
-(Definition~\ref{def:shadow-postnikov-tower},
-equation~\eqref{eq:universal-MC}).
-In this regime, $\Omega_X \bar{B}_X(\cA)$ represents $\cA$
-faithfully in the provisional coderived category
-$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
-\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
-Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
-not in the ordinary derived category.
 \end{enumerate}
 \end{theorem}
 
@@ -4169,8 +4182,29 @@
 quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.
 \end{enumerate}
 Therefore $\psi_g$ is a quasi-isomorphism on $\overline{\mathcal{M}}_g$.
+The asserted $E_2$-collapse is proved separately in
+Lemma~\ref{lem:e2-collapse-higher-genus}.
 \end{proof}
 
+\begin{remark}[Off-locus coderived continuation kept separate]
+\index{bar-cobar inversion!off Koszul locus}
+Outside the Koszul locus \textup{(}admissible affine levels,
+minimal-model central charges\textup{)}, the filtered curved object
+$\Omega_X \bar{B}_X(\cA)$ still exists and its failure to invert in the
+ordinary derived category is measured by the shadow obstruction tower
+$\Theta_{\cA}^{\leq r}$
+\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower},}
+equation~\eqref{eq:universal-MC}\textup{)}. The present file does not
+prove that the counit becomes an equivalence in the provisional
+coderived category
+$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$; that off-locus upgrade is
+left to the separate coderived-model formalism
+\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
+and is intentionally not folded into
+Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
+Proposition~\ref{prop:coderived-adequacy}(a) remains.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-b-lagrangian}
 \index{Lagrangian self-intersection!Theorem B}

tokens used
190,457
