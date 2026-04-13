# C18_bv_brst (533s)

- [HIGH] `chapters/connections/bv_brst.tex:44` — PROBLEM: the file repeatedly wraps ordinary parentheses as `\textup{(}...\textup{)}`; this is typographically noisy and recurs across the chapter (`44, 49, 81-82, 108, 137, 265, 322, 492-494, 643-651, 692-721, 745-848, 930, 1039-1065, 1173-1225, 1349-1396, 1470-1505, 1537-1647, 1661-1711, 1849-1865, 2051-2169, 2200-2317`). FIX: replace every such wrapper with plain text parentheses; e.g. line 44 should read `(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).`, line 1470 should read `\emph{Step~1 (Quillen anomaly).}`, and line 1864 should read `harmonic decoupling (Remark~\ref{rem:bv-bar-class-c-proof}) \\`.
- [HIGH] `chapters/connections/bv_brst.tex:1257` — PROBLEM: `\section{Holomorphic-topological field theories}` is a stub that only punts content to Volume II, and lines `1266-1270` leave four “cross-reference compatibility” labels that are not referenced by any real source file in the repo. FIX: delete lines `1257-1270` and replace them with a single bridge sentence before `\section{The BV algebra structure}`: `Holomorphic-topological boundary theories enter this chapter only through the bar-side BV package; their physical construction belongs to Volume~II, so the next section isolates the configuration-space BV structure.`
- [MEDIUM] `chapters/connections/bv_brst.tex:30` — PROBLEM: `are expected to behave better` hedges a status boundary instead of stating what is proved and what is still only candidate behavior. FIX: replace lines `30-34` with `What this chapter proves is narrower: the genus-$0$ BV/bar comparison and the all-genera scalar Heisenberg identity. The obstruction analysis isolates the unresolved locus: class~$\mathsf{M}$ carries the higher-genus harmonic discrepancy, while classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$ remain candidate extensions rather than proved chain-level comparisons.`
- [MEDIUM] `chapters/connections/bv_brst.tex:314` — PROBLEM: `expected physics reading` is passive hedging inside a remark that already knows it is heuristic. FIX: replace lines `314-317` with `This displayed pairing is a heuristic physics interpretation of the configuration-space forms. The chapter does not prove an identification between the physical integration pairing and the Euler characteristic of the genus-$0$ bar complex.`
- [MEDIUM] `chapters/connections/bv_brst.tex:860` — PROBLEM: `The chain map \Phi should extend` states an unproved target as a modal wish instead of an open construction problem. FIX: replace lines `860-864` with `The higher-genus target is a genus-graded extension of $\Phi$ whose genus-$g$ component incorporates Costello's counterterm expansion. This chapter does not construct that map; it records the problem as Programme~VI-a in \S\ref{sec:modular-koszul-programme}.`
- [MEDIUM] `chapters/connections/bv_brst.tex:1333` — PROBLEM: `should be solved by the bar-cobar pairing` hedges instead of marking the statement as conjectural. FIX: replace lines `1333-1337` with `The chapter does not prove a BV/bar quantum master equation. A natural conjectural target is that the bar-cobar pairing produce a solution of \[\hbar \Delta S + \tfrac12\{S,S\}=0,\] equivalently $\Delta e^{S/\hbar}=0$.`
- [MEDIUM] `chapters/connections/bv_brst.tex:1342` — PROBLEM: `should be equivalent` presents a non-proved comparison without explicit conjectural notation. FIX: replace lines `1342-1345` with `A conjectural comparison would identify the BV quantization of a chiral algebra $\mathcal{A}$ with a bar-side homology theory: \[H^*_{\mathrm{BV}}(\mathcal{A}) \stackrel{?}{\cong} H^*(\bar B(\mathcal{A}), \Omega(\mathcal{A}^!)).\] Here $\mathcal{A}^!$ denotes the Koszul dual.`
- [MEDIUM] `chapters/connections/bv_brst.tex:613` — PROBLEM: notation drifts from family-specific `\kappa(\cdot)` to bare `\kappa` in generic prose (`613, 993, 1096-1105, 1119, 2021`), so the reader cannot tell whether `\kappa` means a level, an anomaly coefficient, or a curvature scalar. FIX: restore the object in every generic occurrence: line 613 `\dfib^{\,2} = \kappa(\cA)\cdot\omega_1` and `\kappa(\cA)=0`; line 993 `m_0 = \kappa(\widehat{\fg}_k)\cdot\mathbf{1}`; lines `1096-1105` `\kappa(\widehat{\fg}_k)=\frac{(k+h^\vee)\dim\fg}{2h^\vee}` and `negates \kappa(\widehat{\fg}_k)`; line 1119 `\kappa(\widehat{\fg}_k)` is the semi-infinite anomaly coefficient; line 2021 `d_{\mathrm{BV}}^2 = \kappa(\cA)\cdot\omega_g`.
- [LOW] `chapters/connections/bv_brst.tex:283` — PROBLEM: lines `283-286` merely restate lines `271-281` without adding new content. FIX: delete lines `283-286` entirely.
- [LOW] `chapters/connections/bv_brst.tex:223` — PROBLEM: theorem-part references are typeset awkwardly as `Theorem~\ref{...}(3)` and similarly at `1051, 1055`; this reads badly and trips TeX hygiene checks. FIX: change line 223 to `Theorem~\ref{thm:FM}, item~(3):`, line 1051 to `Theorem~\ref{thm:genus-universality}(i) equals`, and line 1055 to `Theorem~\ref{thm:genus-universality}(ii) is the`.
- [LOW] `chapters/connections/bv_brst.tex:182` — PROBLEM: theorem/lemma headings at `182, 354, 463` omit the non-breaking space before citations. FIX: change them to `\ClaimStatusProvedElsewhere{}~\cite{CG17}` at lines 182 and 354, and `\ClaimStatusProvedElsewhere{}~\cite{FGZ86}` at line 463.
- [LOW] `chapters/connections/bv_brst.tex:782` — PROBLEM: the sentence runs directly into a display with `... + 1)$ \[`; the display opening is malformed stylistically. FIX: replace lines `781-789` with `$\beta\gamma$ system sits at $\lambda = 3/2$. Using \[\n c_{\beta\gamma}\!\left(\tfrac{3}{2}\right)=2\bigl(6\cdot\tfrac{9}{4}-6\cdot\tfrac{3}{2}+1\bigr)=11,\n\]`.
- [LOW] `chapters/connections/bv_brst.tex:2154` — PROBLEM: the conjecture still uses weak modal prose (`should match`, `is expected to be`) at `2154-2156` and `2165-2169`. FIX: replace lines `2154-2156` with `$\kappa(\mathrm{dP}_k)=k+1$. The characteristic-lattice count therefore predicts the endpoint values $\kappa(\mathbb{P}^2)=1$ and $\kappa(\mathrm{dP}_8)=9$.` Replace lines `2165-2169` with `The conjecture further asserts that the shadow class is $\mathsf{C}$ on the generic locus (four-pair $\beta\gamma$ structure) and degenerates to $\mathsf{M}$ along the stress-tensor line, in direct analogy with the Burns space (Remark~\ref{rem:burns-shadow-class}).`
- [LOW] `chapters/connections/bv_brst.tex:2182` — PROBLEM: there is a stray space before the period in `Theorem~D .`. FIX: change it to `Theorem~D.`

## Summary
Checked: 2339 | Findings: 14 | Verdict: FAIL


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
session id: 019d83fd-f588-74c3-a493-884fbf5a8c34
--------
user
<task>
You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
Tear apart every weakness. Accept NOTHING at face value.
For EVERY finding, you MUST provide the EXACT FIX — not just the diagnosis.
Format: [SEVERITY] file:line — PROBLEM: ... FIX: ...
</task>

<grounding_rules>
Ground every claim in file contents you actually read. No guesses. No inferences presented as facts.
</grounding_rules>

<completeness_contract>
Exhaust the audit surface. After the first finding, dig deeper for second-order failures.
After the obvious issues, hunt for the SUBTLE ones that survive surface-level review.
</completeness_contract>

<verification_loop>
Re-verify each finding against actual file contents. Remove false positives.
</verification_loop>

<structured_output_contract>
Return findings as:
- [CRITICAL] file:line — PROBLEM: ... FIX: ...
- [HIGH] file:line — PROBLEM: ... FIX: ...
- [MEDIUM] file:line — PROBLEM: ... FIX: ...
- [LOW] file:line — PROBLEM: ... FIX: ...

End with:
## Summary
Checked: N | Findings: N | Verdict: PASS/FAIL
</structured_output_contract>


MISSION: COSMETIC & AESTHETIC AUDIT of chapters/connections/bv_brst.tex

Read the entire file. Audit for:

1. **AI slop vocabulary** (AP29): moreover, additionally, notably, crucially, remarkably,
   interestingly, furthermore, delve, leverage, tapestry, cornerstone, "it is worth noting".
   FIX: rewrite each occurrence without the slop word.

2. **Em dashes** (---  or U+2014): FORBIDDEN.
   FIX: replace with colon, semicolon, or separate sentence.

3. **Markdown in LaTeX** (AP121): backtick numerals, **bold**, _italic_.
   FIX: use $...$, \textbf, \emph.

4. **Chapter opening quality**: Does the chapter open with the PROBLEM (CG deficiency opening)?
   Or does it open with "In this chapter we..." (AP106/AP109)?
   FIX: rewrite the opening to state the deficiency/problem first.

5. **Passive voice hedging** in mathematical statements: "it can be shown", "one might expect",
   "it seems reasonable". If the math is clear, STATE it. If not, mark conjecture.
   FIX: active voice or explicit conjecture.

6. **Notation consistency**: Are macros used consistently? Any bare \kappa without family?
   Any bare \Omega/z without level k? Any undefined macros?
   FIX: add family superscript, level prefix, or macro definition.

7. **Dead code**: commented-out sections >10 lines, unused labels, TODOs/FIXMEs.
   FIX: delete dead code or resolve TODOs.

8. **Redundancy**: Same theorem stated in multiple places with different wording.
   FIX: state once, cite elsewhere.

9. **Transition quality**: Does each section force the next? Or do transitions use
   "We now turn to..." signpost language (AP109)?
   FIX: mathematical necessity transitions.

10. **Typography**: double spaces, inconsistent spacing around operators, broken LaTeX
    environments, mismatched braces.
    FIX: fix each instance.

Report EVERY finding with exact line number and exact fix.
mcp startup: no servers
codex
I’m auditing `chapters/connections/bv_brst.tex` as a hostile surface review. I’ll read the full file first, then sweep for the specific AP29/AP109/AP121 and notation failures, and only report findings I can anchor to exact lines.
exec
/bin/zsh -lc "wc -l chapters/connections/bv_brst.tex && nl -ba chapters/connections/bv_brst.tex | sed -n '1,220p' && printf '\\n<<CHUNK_BREAK>>\\n' && nl -ba chapters/connections/bv_brst.tex | sed -n '221,440p' && printf '\\n<<CHUNK_BREAK>>\\n' && nl -ba chapters/connections/bv_brst.tex | sed -n '441,660p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    2339 chapters/connections/bv_brst.tex
     1	\chapter{BV-BRST formalism and Gaiotto's perspective}
     2	\label{ch:bv-brst}
     3	\index{Batalin--Vilkovisky|see{BV algebra}}
     4	
     5	The physicist's BRST cohomology and the algebraist's bar resolution
     6	are not analogous: they are the same computation. The BV formalism
     7	is a machine for computing derived functors; the bar complex is a
     8	machine for computing derived functors; at genus~$0$, they are the
     9	same machine applied to the same input. Costello's formulation of
    10	perturbative QFT as the theory of derived moduli problems makes the
    11	identification inevitable: the BRST operator computes the derived
    12	space of gauge-equivalence classes, which is what the bar differential
    13	computes on the algebraic side. What requires proof is not the
    14	coincidence but the precise scope of the agreement.
    15	
    16	The BV Laplacian and the sewing operator agree at genus~$0$. The
    17	quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
    18	the BV formalism coincides on $\mathbb{P}^1$ with the bar
    19	differential $d_{\mathrm{bar}}$ of the chiral algebra: the
codex
I’ve read the opening third. The file is long, so I’m continuing line-by-line through the rest and separately indexing likely failure classes: signpost prose, hedging, notation drift, dead code, and line-level typography defects.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '661,920p' && printf '\\n<<CHUNK_BREAK>>\\n' && nl -ba chapters/connections/bv_brst.tex | sed -n '921,1180p' && printf '\\n<<CHUNK_BREAK>>\\n' && nl -ba chapters/connections/bv_brst.tex | sed -n '1181,1460p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   661	Theorem~\ref{thm:brst-bar-genus0} constructs $\Phi$ under
   662	the hypothesis $c = 26$, giving a quasi-isomorphism that
   663	identifies $H^*(Q_{\mathrm{BRST}}) \cong H^*(d_{\mathrm{bar}})$.
   664	If $c \neq 26$, the BRST side has $Q^2 = \frac{c-26}{12}\,c_0 \neq 0$
   665	and the bar side has $\dfib^{\,2} = \kappa_{\mathrm{tot}} \cdot \omega_1
   666	\cdot \mathrm{id} \neq 0$: neither is a cochain complex,
   667	and both obstructions are controlled by the same numerical invariant
   668	$c - 26$. The dictionary
   669	\[
   670	\kappa_{\mathrm{tot}}
   671	= \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})
   672	= \tfrac{c}{2} + \tfrac{-26}{2}
   673	= \tfrac{c-26}{2}
   674	\]
   675	(Computation~\ref{comp:virasoro-curvature} for $\kappa(\mathrm{Vir}_c) = c/2$;
   676	$\kappa(\text{$bc$-ghost}, \lambda{=}2) = c_{\mathrm{gh}}/2 = -13$)
   677	converts the BRST obstruction $Q^2 \propto (c-26)$ into
   678	the bar obstruction $\dfib^{\,2} \propto \kappa_{\mathrm{tot}}$.
   679	\end{proof}
   680	
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1461,1760p' && printf '\\n<<CHUNK_BREAK>>\\n' && nl -ba chapters/connections/bv_brst.tex | sed -n '1761,2060p' && printf '\\n<<CHUNK_BREAK>>\\n' && nl -ba chapters/connections/bv_brst.tex | sed -n '2061,2339p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1461	= \bigl(\det\nolimits'_\zeta \bar\partial_{\Sigma_g}\bigr)^{-\kappa},
  1462	\end{equation}
  1463	where $\det'_\zeta$ denotes the zeta-regularized determinant
  1464	with the zero modes removed.
  1465	Apply GRR to the universal curve
  1466	$\pi\colon \overline{\mathcal{C}}_g
  1467	\to \overline{\mathcal{M}}_g$
  1468	for the structure sheaf~$\mathcal{O}$.
  1469	
  1470	\emph{Step~1} \textup{(}Quillen anomaly\textup{)}.
  1471	The Quillen metric $h_Q$ on the determinant line bundle
  1472	$\det(R\pi_*\mathcal{O})$ over
  1473	$\overline{\mathcal{M}}_g$ has curvature
  1474	\[
  1475	\operatorname{curv}(h_Q)
  1476	= -2\pi i\, c_1(\mathbb{E}),
  1477	\]
  1478	where $\mathbb{E} = R^0\pi_*\omega_{\mathcal{C}/\mathcal{M}_g}$
  1479	is the Hodge bundle of rank~$g$ \cite{Quillen85}.
  1480	
codex
This is a `deep-beilinson-audit` turn. I’m loading only the audit workflow and then I’m cross-checking the raw file with targeted searches so the findings stay anchored and false positives stay out.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

collab spawn_agent(call_mWxTPrFwcruTcE4nkmM5Plxf, prompt="In /Users/raeez/chiral-bar-cobar, find whether labels defined in chapters/connections/bv_brst.tex are referenced elsewhe…")
spawn_agent(call_mWxTPrFwcruTcE4nkmM5Plxf, prompt="In /Users/raeez/chiral-bar-cobar, find whether labels defined in chapters/connections/bv_brst.tex are referenced elsewhe…") pending init:
  agent: 019d83fe-8d66-70e2-8e9a-dbe01560b35b
mcp startup: no servers
collab spawn_agent(call_dJYfT3xHP5XkJtfQ5WMrWYEj, prompt="Inspect chapters/connections/bv_brst.tex for the user-specified cosmetic/aesthetic audit surface only. Read the whole fi…")
mcp startup: no servers
spawn_agent(call_dJYfT3xHP5XkJtfQ5WMrWYEj, prompt="Inspect chapters/connections/bv_brst.tex for the user-specified cosmetic/aesthetic audit surface only. Read the whole fi…") pending init:
  agent: 019d83fe-8d6b-7281-bf56-6a2f62e315b3
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
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
chiral_chern_weil.pdf
exec
/bin/zsh -lc "sed -n '1240,1295p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
finite-type $\mathcal{W}$-algebra,
$\kappa(\mathcal{W}^k(\fg)) = c(\mathcal{W}^k(\fg))\cdot\varrho(\fg)$.
Part~(b) then follows from the quantum complementarity theorem.
Part~(c): specialize to $\fg = \mathfrak{sl}_2$ with $h^\vee = 2$,
for which $c + c' = 26$ and $\varrho(\mathfrak{sl}_2)=1/2$.
\end{proof}

\begin{remark}[Conditional semi-infinite interpretation]
\label{rem:w-semi-infinite-conditional}
If Theorem~\ref{thm:bar-semi-infinite-w} holds, then
Corollary~\ref{cor:anomaly-duality-w} acquires the intended
semi-infinite anomaly interpretation for principal
$\mathcal{W}$-algebra pairs. On the current record, that
interpretation remains conditional on explicit DS/bar
compatibility.
\end{remark}

\section{Holomorphic-topological field theories}

The physical content (Gaiotto's framework, boundary chiral
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
chiral_chern_weil.pdf
exec
/bin/zsh -lc "sed -n '1,200p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{BV-BRST formalism and Gaiotto's perspective}
\label{ch:bv-brst}
\index{Batalin--Vilkovisky|see{BV algebra}}

The physicist's BRST cohomology and the algebraist's bar resolution
are not analogous: they are the same computation. The BV formalism
is a machine for computing derived functors; the bar complex is a
machine for computing derived functors; at genus~$0$, they are the
same machine applied to the same input. Costello's formulation of
perturbative QFT as the theory of derived moduli problems makes the
identification inevitable: the BRST operator computes the derived
space of gauge-equivalence classes, which is what the bar differential
computes on the algebraic side. What requires proof is not the
coincidence but the precise scope of the agreement.

The BV Laplacian and the sewing operator agree at genus~$0$. The
quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
the BV formalism coincides on $\mathbb{P}^1$ with the bar
differential $d_{\mathrm{bar}}$ of the chiral algebra: the
BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
exec
/bin/zsh -lc "rg -n \"\\\\label\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '200,400p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The degree-$n$ bar complex is:
\[\bar{B}^n(\mathcal{A}) = \Omega^*(\overline{C}_{n+1}(X), \mathcal{A}^{\boxtimes (n+1)})\]

The generators are operator insertions $\phi_i \in \mathcal{A}$ at marked points, paired with logarithmic $1$-forms $\eta_{ij} = d\log(z_i - z_j)$ dual to the collision divisors.

\emph{Step~2: BV Bracket.}

The BV bracket is a residue operation on the log-de~Rham complex
of~$\overline{C}_{n+1}(X)$. In local coordinates near the divisor
$D_{ij} = \{z_i = z_j\}$, with $\epsilon = z_i - z_j$:
\[\{\phi(z_i), \eta_{jk}\}
= \delta_{ij}\,\Res_{\epsilon = 0}
\Bigl[\frac{\partial\phi}{\partial z_i}\,
\frac{d\epsilon}{\epsilon(z_i - z_k)}\Bigr]
+ \delta_{ik}\,\Res_{\epsilon = 0}
\Bigl[\frac{\partial\phi}{\partial z_i}\,
\frac{d\epsilon}{\epsilon(z_i - z_j)}\Bigr].\]
Both terms are Poincar\'e residues of logarithmic forms along
normal-crossing divisors of the smooth
variety~$\overline{C}_{n+1}(X)$: the residue map
exec
/bin/zsh -lc "rg -n '\\\\label' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2:\label{ch:bv-brst}
57:\label{rem:brst-anomaly-gkw}
74:\label{rem:bv-bar-bridge}
103:\label{rem:modular-qme-bv}
111:\begin{equation}\label{eq:modular-qme-bv}
155:\label{rem:sft-bar-identification}
169:\label{def:bv-data-chiral}
183:\label{thm:bv-bar-geometric}
248:\label{def:bv-laplacian}
269:\label{rem:qme-bar-cobar}
289:\label{subsec:bv-bar-identification}
293:\ClaimStatusHeuristic]\label{rem:genus0-amplitude-bar}
320:\begin{remark}[Genus-$1$ partition function]\label{rem:genus1-bv}
326:\begin{remark}[Anomaly = curvature]\label{rem:anomaly-curvature-bv}
336:\label{def:brst-operator}
355:\label{thm:brst-physical-states}
384:\label{thm:log-form-ghost-law}
429:\label{conj:bar-topological-brst}
441:\label{sec:brst-bar-chain-map}
452:\begin{equation}\label{eq:brst-differential}
exec
/bin/zsh -lc "sed -n '400,800p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
+ \eta_{ki} \wedge \eta_{ij} = 0$
in the Orlik--Solomon algebra provide the quadratic
structure shared by the BRST ghost algebra
($Q_{\mathrm{BRST}}(c) = c\,\partial c$).
\end{theorem}

\begin{proof}
Direct computation: $\eta_{ij} = d\log(z_i - z_j)$
maps to $d\log(w(z_i) - w(z_j))$ under $z \to w(z)$.
Factoring:
\[
d\log(w(z_i) - w(z_j)) = d\log(z_i - z_j)
+ d\log\!\left(\frac{w(z_i) - w(z_j)}{z_i - z_j}\right)
\]
and near the diagonal, L'H\^opital gives
$(w(z_i) - w(z_j))/(z_i - z_j) \to w'(z_i)$, so
the correction approaches $d\log w'(z_i)$. This is
the BRST ghost 1-cocycle for the Lie algebra
$\mathrm{Vect}(X)$: if $c(z)$ is the ghost field for
$v(z)\partial_z \in \mathrm{Vect}(X)$, then the
exec
/bin/zsh -lc "rg -n 'rem:ht-from-n4-sym' -g'*'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '800,1200p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Superstring BRST anomaly cancellation requires
$\kappa_{\mathrm{tot}} = \kappa_{\mathrm{matter}}
+ \kappa_{\mathrm{ghost}}^{\mathrm{super}} = 0$,
hence $\kappa_{\mathrm{matter}} = 15/2$, equivalently
$c_{\mathrm{matter}} = 15$. For the $N = 1$ superconformal
matter of $d$ flat spacetime dimensions
($d$ free scalars contributing $d$ to $c$, plus $d$ free
Majorana fermions contributing $d/2$), this gives
$c_{\mathrm{matter}} = d + d/2 = 3d/2 = 15$, hence
$d = 10$: the critical dimension of the superstring. The
complementarity sum for the superghost is
\[
 \kappa_{\mathrm{ghost}}^{\mathrm{super}}
 + (\kappa_{\mathrm{ghost}}^{\mathrm{super}})'
 \;=\; -\tfrac{15}{2} + \tfrac{15}{2}
 \;=\; 0,
\]
confirming that the superstring BRST anomaly cancellation
\textup{(}at $d = 10$\textup{)} is preserved by the matching
Koszul involution of Proposition~\ref{prop:koszul-brst-anomaly-preservation}.
exec
/bin/zsh -lc "sed -n '1200,1600p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\item The curvature coefficients satisfy the same
level-independent complementarity law as the central-charge
package. For principal finite-type $\mathcal{W}$-algebras,
\[
\kappa(\mathcal{W}^k(\fg)) + \kappa(\mathcal{W}^{k'}(\fg))
= \bigl(c(\mathcal{W}^k(\fg)) + c(\mathcal{W}^{k'}(\fg))\bigr)
\varrho(\fg),
\]
where $\varrho(\fg) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly
ratio from Theorem~\ref{thm:wn-obstruction}. Thus the sum is a
level-independent constant: $13$ for Virasoro and $250/3$ for
$\mathcal{W}_3$.

\item The quantum complementarity theorem
\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
applied to the W-algebra Koszul pair
\textup{(}Theorem~\textup{\ref{thm:w-algebra-koszul-main})} gives:
\[
Q_g(\mathcal{W}^k) \oplus Q_g(\mathcal{W}^{-k-2h^\vee})
= H^*(\overline{\mathcal{M}}_g,\, Z(\mathcal{W}^k)).
 succeeded in 3.33s:
rectification_20260412_233715/R02_higher_genus_complementarity.md:1046:\label{rem:ht-from-n4-sym}%
chapters/connections/bv_brst.tex:1266:\label{rem:ht-from-n4-sym}%
metadata/label_index.json:32678:  "rem:ht-from-n4-sym": {
compute/audit/ap5_cross_volume_report_wave6.md:131:2. **Line 1276-1277:** `\begin{theorem}[HT theory from 4d N=4 SYM; \ClaimStatusProvedElsewhere]` / `\label{rem:ht-from-n4-sym}`
exec
/bin/zsh -lc "sed -n '1600,2000p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\noindent\textbf{Path \textup{(d)}: numerical verification.}
\index{multi-path verification!Heisenberg BV/bar}
At each genus $g = 1, \ldots, 15$, three independent
implementations produce the same rational number $\lambda_g^{\mathrm{FP}}$:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item the Bernoulli formula
 $\lambda_g^{\mathrm{FP}}
 = \frac{(2^{2g-1}-1)\,|B_{2g}|}{2^{2g-1}\,(2g)!}$;
\item the Taylor extraction of the $\hat{A}$-series
 $(\hbar/2)/\sin(\hbar/2) - 1
 = \sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\,\hbar^{2g}$;
\item a direct computation of the Faber--Pandharipande
 intersection integral on $\overline{\mathcal{M}}_{g,1}$
 via the string/dilaton equation and Witten's conjecture.
\end{enumerate}
All three agree at every genus tested. Sample values:
$\lambda_1^{\mathrm{FP}} = 1/24$,
$\lambda_2^{\mathrm{FP}} = 7/5760$,
$\lambda_3^{\mathrm{FP}} = 31/967680$.
\textup{(}Verified in the compute layer:
exec
/bin/zsh -lc "rg -n 'ht-from-n4-sym'" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
metadata/label_index.json:32678:  "rem:ht-from-n4-sym": {
rectification_20260412_233715/R02_higher_genus_complementarity.md:1046:\label{rem:ht-from-n4-sym}%
chapters/connections/bv_brst.tex:1266:\label{rem:ht-from-n4-sym}%
compute/audit/ap5_cross_volume_report_wave6.md:131:2. **Line 1276-1277:** `\begin{theorem}[HT theory from 4d N=4 SYM; \ClaimStatusProvedElsewhere]` / `\label{rem:ht-from-n4-sym}`
compute/audit/ap5_cross_volume_report_wave6.md:132:   — theorem with `rem:` prefix; should be `thm:ht-from-n4-sym`
compute/audit/ap5_post_wave7_verification.md:113:- Line 1276-1277: `\begin{theorem}[HT theory from 4d N=4 SYM; ClaimStatusProvedElsewhere]` / `\label{thm:ht-from-n4-sym}` — CORRECT
exec
/bin/zsh -lc "sed -n '2000,2400p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
In the Costello--Li framework of twisted supergravity, the bulk
theory on $\mathrm{AdS}_{d+1}$ is computed by Witten diagrams
using the bulk propagator, while the boundary theory is computed
by the bar complex using the boundary OPE. The mismatch between
bulk and boundary propagators at one loop ($g = 1$) is the
holographic anomaly: the Weyl anomaly coefficient
$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
correction to the BV/bar comparison. The coderived formalism
packages this anomaly as curvature data rather than forcing a
strict differential. The missing mathematical step is still to
show that the comparison map becomes an isomorphism after
localizing at coacyclic objects.

\emph{The categorical viewpoint.}
The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
home for curved dg~algebras: it is the homotopy category of
dg~comodules over the bar coalgebra $B(\cA)$ in which
$d^2 = m_0 \cdot \mathrm{id}$ is permitted. The bar complex
$B(\cA)$ always satisfies $D_B^2 = 0$ (the total bar differential
squares to zero regardless of curvature), so $B(\cA)$ lives
exec
/bin/zsh -lc "rg -n 'boundary-chiral-algebra-bv'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/audit/ap5_post_wave7_verification.md:114:- Line 1326-1327: `\begin{theorem}[Boundary chiral algebra; ClaimStatusProvedElsewhere]` / `\label{thm:boundary-chiral-algebra-bv}` — CORRECT
metadata/label_index.json:29470:  "rem:boundary-chiral-algebra-bv": {
compute/audit/ap5_cross_volume_report_wave6.md:134:3. **Line 1326-1327:** `\begin{theorem}[Boundary chiral algebra; \ClaimStatusProvedElsewhere ...]` / `\label{rem:boundary-chiral-algebra-bv}`
compute/audit/ap5_cross_volume_report_wave6.md:135:   — theorem with `rem:` prefix; should be `thm:boundary-chiral-algebra-bv`
chapters/connections/bv_brst.tex:1267:\label{rem:boundary-chiral-algebra-bv}%
rectification_20260412_233715/R19_coderived_models.md:374:chapters/connections/bv_brst.tex:1267:\label{rem:boundary-chiral-algebra-bv}%
rectification_20260412_233715/R02_higher_genus_complementarity.md:1047:\label{rem:boundary-chiral-algebra-bv}%
exec
/bin/zsh -lc 'rg -n "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|We now turn to|we now turn to|In this chapter we|one might expect|it can be shown|it seems reasonable|TODO|FIXME|```|'"\\*\\*|_[A-Za-z]|---|—|  +"'$|  [A-Za-z'"\\\\"'$]" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
p=Path('chapters/connections/bv_brst.tex')
for i,line in enumerate(p.read_text().splitlines(),1):
    if '  ' in line:
        print(f\"{i}:{line}\")
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP29|AP109|AP121|bv_brst|BV-BRST|ch:bv-brst" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: unmatched "
 exited 127 in 52ms:
zsh:1: command not found: python
 succeeded in 52ms:
CLAUDE.md:170:### HZ-10. AP29/V2-AP29 (AI slop) -- 4 waves, 40+ instances over 3 zero-tolerance commits
CLAUDE.md:352:- B40. Markdown in LaTeX: backtick numerals, **bold**, _italic_. CORRECT: $...$, \textbf, \emph. AP121.
CLAUDE.md:519:**duality** (AP33, AP29, AP31): H_k^! = Sym^ch(V*) != H_{-k}. Same kappa, different algebras. delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (cancellation, vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-degree components independent. F_1=0 does NOT imply F_g=0.
CLAUDE.md:552:AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
CLAUDE.md:790:AP121: Modality hygiene. In LaTeX, NEVER use Markdown: no backtick numerals (`29` -> $29$), no **bold** -> \textbf, no _italic_ -> \emph. Grep for backticks after every .tex write.
metadata/theorem_registry.md:2302:#### `chapters/connections/bv_brst.tex` (11)
chapters/connections/concordance.tex:693:\item \emph{BV-BRST.}
chapters/connections/concordance.tex:695: Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
exec
/bin/zsh -lc "sed -n '2400,2800p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

exec
/bin/zsh -lc "rg -n 'ref\\{rem:boundary-chiral-algebra-bv'" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


exec
/bin/zsh -lc "sed -n '360,390p' rectification_20260412_233715/R19_coderived_models.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
Let $C=\operatorname{Cone}(f)$. It suffices to prove $C$ is acyclic.
From $j^*f$ and $i^*f$ quasi-isomorphisms, $j^*C$ and $i^*C$ are acyclic.
Apply the localization triangle
\[j_!j^*C \longrightarrow C \longrightarrow i_*i^*C \xrightarrow{+1}.\]
Both outer terms are acyclic, hence $C$ is acyclic. Therefore $f$ is a
quasi-isomorphism.
\end{proof}

 succeeded in 51ms:
chapters/connections/bv_brst.tex:29:the bar differential collects OPE residues along FM boundary strata.
chapters/connections/bv_brst.tex:65:iterated residues on FM boundary strata
chapters/connections/bv_brst.tex:1259:The physical content (Gaiotto's framework, boundary chiral
chapters/connections/bv_brst.tex:1260:algebras, HT boundary conditions, W-algebras from Higgs branches)
chapters/connections/bv_brst.tex:1267:\label{rem:boundary-chiral-algebra-bv}%
chapters/connections/bv_brst.tex:1268:\label{rem:bar-cobar-ht-boundary}%
chapters/connections/bv_brst.tex:1844:non-separating boundary divisor
chapters/connections/bv_brst.tex:1872:\kappa / \operatorname{Im}(\tau)$ is not a coboundary
chapters/connections/bv_brst.tex:2002:using the bulk propagator, while the boundary theory is computed
chapters/connections/bv_brst.tex:2003:by the bar complex using the boundary OPE. The mismatch between
thinking
**Running commands effectively**

I might need to use Python 3 since the first rg command failed due to some quotes. I’m planning to rerun it with more targeted settings. I also need to open a concordance around relevant lines and make sure there's a theorem registry for bv_brst. It could be useful to utilize rg for patterns, or even perl or Python 3 if necessary. I’ll get started on this and check back later.
exec
/bin/zsh -lc 'rg -n "notably|crucially" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '1020,1070p' rectification_20260412_233715/R02_higher_genus_complementarity.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

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
/bin/zsh -lc 'rg -n "—" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

codex
The first grep sweep surfaced the policy anchors, but one pattern command failed on shell quoting. I’m rerunning the scans in a safer form and then I’ll reconcile them against the raw line reads so the final list only contains verified defects.
exec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|we now turn to|in this chapter we|one might expect|it can be shown|it seems reasonable|todo|fixme|---|—|\\*\\*|"'`'"' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2288,2335p' metadata/theorem_registry.md && printf '\\n<<CONCORDANCE>>\\n' && sed -n '688,708p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
p=Path('chapters/connections/bv_brst.tex')
for i,line in enumerate(p.read_text().splitlines(),1):
    if '  ' in line:
        print(f\"{i}:{line}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
887:power: the ``Dirac sea'' vacuum is the semi-infinite form
892:with a ``charge anomaly'' correction term that ensures
906:unconditionally. The ghosts are ``built in'' to the semi-infinite
2026:forces a choice of ``strictification'' (lifting the curvature
 succeeded in 51ms:
| `rem:arithmetic-comparison-sharpening` | `remark` | 11267 | Sharpening of the arithmetic comparison conjecture |
| `prop:miura-packet-splitting` | `proposition` | 11341 | — |
| `prop:genus2-non-diagonal` | `proposition` | 11707 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | 11751 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | 11883 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | 11915 | B\"ocherer bridge |
| `rem:genus2-definitive-scope` | `remark` | 12040 | Definitive scope of genus-$2$ arithmetic access |
| `rem:leech-all-sk` | `remark` | 12095 | Leech: all genus-$2$ cusp forms are Saito--Kurokawa lifts |
| `thm:leech-chi12-projection` | `theorem` | 12116 | Leech $\chi_{12}$-projection and Waldspurger consequence |
| `prop:prime-locality-proved-cases` | `proposition` | 12332 | Settled cases |
| `thm:prime-locality-obstructions` | `theorem` | 12373 | Precise obstructions to prime-locality; {} where indicated |
| `thm:riccati-determinacy-assessment` | `theorem` | 12575 | Riccati determinacy |
| `prop:shadow-not-selberg` | `proposition` | 12618 | The shadow zeta is not in the Selberg class |

#### `chapters/connections/bv_brst.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:log-form-ghost-law` | `theorem` | 371 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 476 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
 succeeded in 53ms:

exec
/bin/zsh -lc 'rg -n "`" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:
zsh:1: unmatched "
exec
/bin/zsh -lc "sed -n '1030,1060p' rectification_20260412_233715/R02_higher_genus_complementarity.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
exec
/bin/zsh -lc "rg -n '\\"'`'"' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
887:power: the ``Dirac sea'' vacuum is the semi-infinite form
892:with a ``charge anomaly'' correction term that ensures
906:unconditionally. The ghosts are ``built in'' to the semi-infinite
2026:forces a choice of ``strictification'' (lifting the curvature

exec
/bin/zsh -lc "rg -n 'bar-cobar-ht-boundary' -n" in /Users/raeez/chiral-bar-cobar succeeded in 77ms:
metadata/label_index.json:29106:  "rem:bar-cobar-ht-boundary": {
chapters/connections/bv_brst.tex:1268:\label{rem:bar-cobar-ht-boundary}%
compute/audit/ap5_cross_volume_report_wave6.md:137:4. **Line 1363-1364:** `\begin{conjecture}[Bar-cobar from HT boundary; \ClaimStatusHeuristic]` / `\label{rem:bar-cobar-ht-boundary}`
compute/audit/ap5_cross_volume_report_wave6.md:138:   — conjecture with `rem:` prefix; should be `conj:bar-cobar-ht-boundary`
compute/audit/ap5_post_wave7_verification.md:115:- Line 1363-1364: `\begin{conjecture}[Bar-cobar from HT boundary; ClaimStatusHeuristic]` / `\label{conj:bar-cobar-ht-boundary}` — CORRECT
rectification_20260412_233715/R19_coderived_models.md:375:chapters/connections/bv_brst.tex:1268:\label{rem:bar-cobar-ht-boundary}%
rectification_20260412_233715/R02_higher_genus_complementarity.md:1048:\label{rem:bar-cobar-ht-boundary}%
exec
/bin/zsh -lc "rg -n '\\*\\*' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "In this chapter we" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "sed -n '120,140p' compute/audit/ap5_cross_volume_report_wave6.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
None are in theorem environments; all are in prose or tables. CLAUDE.md AP32 says "every occurrence in a theorem MUST carry explicit tag" so these are below the strict threshold but still represent AP32 drift. Recommendation: add a `(UNIFORM-WEIGHT)` parenthetical to table captions and to each table row/column header describing `F_g`.

### W2. AP125 label-environment mismatches (Vol II)

**File:** `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex`

Four environments carrying mismatched `rem:` labels:

1. **Line 1031:** `\begin{conjecture}[W-algebra bar-cobar duality; \ClaimStatusConjectured]\label{rem:w-algebra-bar-cobar}`
   — conjecture with `rem:` prefix; should be `conj:w-algebra-bar-cobar`

2. **Line 1276-1277:** `\begin{theorem}[HT theory from 4d N=4 SYM; \ClaimStatusProvedElsewhere]` / `\label{rem:ht-from-n4-sym}`
   — theorem with `rem:` prefix; should be `thm:ht-from-n4-sym`

3. **Line 1326-1327:** `\begin{theorem}[Boundary chiral algebra; \ClaimStatusProvedElsewhere ...]` / `\label{rem:boundary-chiral-algebra-bv}`
   — theorem with `rem:` prefix; should be `thm:boundary-chiral-algebra-bv`

4. **Line 1363-1364:** `\begin{conjecture}[Bar-cobar from HT boundary; \ClaimStatusHeuristic]` / `\label{rem:bar-cobar-ht-boundary}`
   — conjecture with `rem:` prefix; should be `conj:bar-cobar-ht-boundary`

exec
/bin/zsh -lc 'rg -n "we now" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobarthinking
**Searching for backticks and comments**

I’m realizing that I only found quotes instead of backticks, which could just be a false positive due to grave accents. It seems like double backticks in LaTeX could be acceptable for quotes. I’ll need to actually find the backticks. I think looking for double spaces might not be necessary. I should consider using rg to locate comment lines and TODOs as well. I’ll also check labels for external references. Let’s search more carefully for signpost phrases!
 exited 1 in 53ms:

exec
/bin/zsh -lc "rg -n '"'^'"\\s*%|TODO|FIXME|XXX|TBD' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'We now|we now|We turn|we turn|It remains|The argument extends|The proof uses|The proof parallels|Under the stated|This is|There is|There exists|should be|would require|remains heuristic|is expected|is inevitable' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\kappa(\\(|\\b\\\\kappa\\b)|\\\\Omega/z|\\\\Omega\\\\/z|\\\\Omega\\\\,d\\\\log z|bare \\\\kappa|\\\\Omega/z|k\\\\,\\\\Omega/z|r\\"'^'"\\{\\\\mathrm\\{KM\\}\\}\\(z\\)' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1265:% Labels preserved for cross-reference compatibility.
1269:% conj:holographic-bar-cobar defined in genus_complete.tex
2203:%: from landscape_census.tex; k=0 -> r=0 verified
2209:%: from landscape_census.tex; k=0 -> dim(g)/2; k=-h^v -> 0
 succeeded in 53ms:
261:delta-function along $D_{ij}$. This is the loop-insertion operator in the bar
279:complex would require the conditional BV package recorded in
416:the correction approaches $d\log w'(z_i)$. This is
494:$\kappa_{\mathrm{tot}} = 0$\textup{)}. There exists a chain map
506:The proof uses a PBW filtration on both complexes, reducing the
557:to all degrees. This is a classical result in homological algebra
630: configuration space. This is the ghost--propagator identification.
848:\textup{(}which would require $\kappa + \kappa' = 13$\textup{)}:
921:$k \neq -h^\vee$. There is a quasi-isomorphism of filtered cochain
940:The proof parallels that of
1076:the full moduli space cohomology. This is the mathematical
1155:Under the stated transport hypotheses, begin with the affine
1221:This is the genus-$g$ complementarity statement for the principal
1323:Under the stated assumptions, the product is graded commutative by the
1336:should be solved by the bar-cobar pairing. This is a heuristic
1342:The BV quantization of a chiral algebra $\mathcal{A}$ should be
1354:The identification remains heuristic for general chiral algebras,
1406:for the Heisenberg family. The proof uses four independent
1450:at every genus $g \geq 1$. It remains to show that the BV free
1972:\begin{remark}[Why the coderived category is inevitable]
 succeeded in 53ms:
47:one-loop anomaly coefficient $\kappa(\cA)$, and its projection
48:onto $H^2(\overline{\mathcal{M}}_{g,n})$ gives $F_g = \kappa(\cA) \cdot \lambda_g$
87: $\kappa(\cA)$, the one-loop anomaly
123: \qquad\text{(one-loop anomaly $=$ $\kappa(\cA)\cdot\omega_1$)}, \\
136:$F_g = \kappa(\cA)\lambda_g$
321:At genus~$1$, the $\hat{A}$-genus gives $F_1 = \kappa(\cA)/24$
323:$\kappa(\mathrm{Vir}_c) = c/2$: $F_1 = c/48$.
328:By Theorem~\ref{thm:anomaly-koszul}, $d_{\mathrm{bar}}^2 = 0$ for $\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$ if and only if $\kappa_{\mathrm{tot}} = 0$ (equivalently, $c = 26$ for the bosonic string). When $\kappa_{\mathrm{tot}} \neq 0$, the scalar projection of the universal MC class is $\Theta_\cA^{\min} = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Theorem~\ref{thm:explicit-theta}), curving the bar complex at every genus.
671:= \kappa(\cA_{\mathrm{matter}}) + \kappa(\cA_{\mathrm{ghost}})
675:(Computation~\ref{comp:virasoro-curvature} for $\kappa(\mathrm{Vir}_c) = c/2$;
676:$\kappa(\text{$bc$-ghost}, \lambda{=}2) = c_{\mathrm{gh}}/2 = -13$)
687:$\kappa_{\mathrm{tot}} = \kappa(\cA_{\mathrm{matter}}) +
688:\kappa(\cA_{\mathrm{ghost}}) = 0$ at the classical level. Assume the matter
690:family, so that the complementarity sum $\kappa(\cA_{\mathrm{matter}})
691:+ \kappa(\cA_{\mathrm{matter}}^!) = 0$ holds
697:$\kappa(\widetilde{\cA}_{\mathrm{ghost}}) = -\kappa(\cA_{\mathrm{ghost}})$.
705: \kappa(\cA_{\mathrm{tot}}^{\vee})
706: \;=\; \kappa(\cA_{\mathrm{matter}}^!)
707: + \kappa(\widetilde{\cA}_{\mathrm{ghost}})
708: \;=\; -\kappa(\cA_{\mathrm{matter}})
exec
/bin/zsh -lc 'rg -n "TODO|FIXME|xxx" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1800,1900p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1800	 in the fundamental fields, it factors through the
  1801	 genus-$1$ trace of the underlying free-field sector,
  1802	 whose scalar anomaly is already resolved.
  1803	 For class~M (Virasoro, $\cW_N$), the stress tensor $T$ is
  1804	 itself a fundamental generator with its own propagator channel;
  1805	 the quartic vertex involves $T$ coupling to $T$, and the
  1806	 harmonic correction does not factor through a free subsystem.
  1807	\end{enumerate}
  1808	The three mechanisms combine to show that the quartic
  1809	harmonic-propagator correction vanishes for the $\beta\gamma$
  1810	system at genus~$1$, despite the nonzero quartic shadow
  1811	$Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
  1812	resolved obstructions~(1) and~(2), this establishes
  1813	Conjecture~\ref{conj:master-bv-brst} at the scalar level for
  1814	class~C at genus~$1$. What it does not yet supply is a global
  1815	all-genera BV/bar quasi-isomorphism. For class~$\mathsf{M}$, the
  1816	quartic harmonic discrepancy
  1817	$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
  1818	\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
  1819	identity, and the missing higher-genus step is to prove that the full

exec
/bin/zsh -lc "rg -n \"\\bshould\\b\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
860:(Chapter~\ref{chap:higher-genus}). The chain map $\Phi$ should
1336:should be solved by the bar-cobar pairing. This is a heuristic
1342:The BV quantization of a chiral algebra $\mathcal{A}$ should be
2156: $\kappa = 9$\textup{)} the numerics should match the
thinking
**Summarizing external references of bv_brst.tex labels**

I’m examining whether labels defined in `bv_brst.tex`, especially the compatibility ones near lines 1265-1270, are referenced outside that file. From searches, these labels mainly appear in metadata and cross-volume audit reports under `compute/audit/`, where they’re discussed in mismatch contexts but not actually referenced via `\ref` in other `.tex` files. For each key label like `rem:ht-from-n4-sym`, `rem:boundary-chiral-algebra-bv`, `rem:bar-cobar-ht-boundary`, and `rem:w-algebra-bar-cobar`, there’s no external referencing through LaTeX commands, just reporting or mention in audit and rectify-related files. This suggests these labels serve internal or compatibility tracking roles without active cross-file referencing.
exec
/bin/zsh -lc "rg -n 'w-algebra-bar-cobar'" in /Users/raeez/chiral-bar-cobar succeeded in 83ms:
audit_campaign_20260412_231034/XV11_claim_status_sync.md:752:/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:1031:\begin{conjecture}[\texorpdfstring{$\mathcal{W}$}{W}-algebra bar-cobar duality; \ClaimStatusConjectured]\label{conj:w-algebra-bar-cobar}
audit_campaign_20260412_231034/XV11_claim_status_sync.md:1073:\begin{conjecture}[\texorpdfstring{$\mathcal{W}$}{W}-algebra bar-cobar duality; \ClaimStatusConjectured]\label{conj:w-algebra-bar-cobar}
audit_campaign_20260412_231034/XV11_claim_status_sync.md:1117:  1031	\begin{conjecture}[\texorpdfstring{$\mathcal{W}$}{W}-algebra bar-cobar duality; \ClaimStatusConjectured]\label{conj:w-algebra-bar-cobar}
metadata/label_index.json:37114:  "rem:w-algebra-bar-cobar": {
rectification_20260412_233715/R02_higher_genus_complementarity.md:1050:\label{rem:w-algebra-bar-cobar}%
chapters/connections/bv_brst.tex:1270:\label{rem:w-algebra-bar-cobar}%
compute/audit/ap5_cross_volume_report_wave6.md:128:1. **Line 1031:** `\begin{conjecture}[W-algebra bar-cobar duality; \ClaimStatusConjectured]\label{rem:w-algebra-bar-cobar}`
compute/audit/ap5_cross_volume_report_wave6.md:129:   — conjecture with `rem:` prefix; should be `conj:w-algebra-bar-cobar`
compute/audit/ap5_post_wave7_verification.md:112:- Line 1031: `\begin{conjecture}[W-algebra bar-cobar duality; ClaimStatusConjectured]\label{conj:w-algebra-bar-cobar}` — CORRECT

exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '820,870p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   820	\end{computation}
   821	
   822	\begin{remark}[The ghost--superghost Koszul involution;
   823	\ClaimStatusProvedElsewhere]
   824	\label{rem:ghost-superghost-koszul}
   825	\index{ghost!Koszul involution}
   826	\index{superghost!Koszul involution}
   827	The preceding computation identifies the ghost characteristic in
   828	each of the two string backgrounds:
   829	\begin{itemize}[nosep]
   830	\item bosonic string: ghost $= bc$ at $\lambda = 2$, with
   831	 $\kappa = -13$;
   832	\item superstring: ghost $= bc$ at $\lambda = 2$ plus $\beta\gamma$
   833	 at $\lambda = 3/2$, with total $\kappa = -15/2$.
   834	\end{itemize}
   835	In each case, the Koszul dual is obtained by a single involution
   836	that reverses the sign of the ghost characteristic while preserving
   837	the bilinear pairing. For the $bc$ system, the involution is
   838	the one identified by Friedan--Martinec--Shenker~\cite{FMS86}
   839	relating the $bc$ and $\beta\gamma$ systems at bosonised level;

exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1310,1350p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1310	\longrightarrow
  1311	\bar{B}^{\mathrm{ch}}(\mathcal{A})[1]
  1312	\]
  1313	with $\Delta^2 = 0$, that the induced failure-of-derivation bracket is
  1314	the configuration-space residue pairing, and that these structures are
  1315	functorial in morphisms of chiral algebras. Then
  1316	$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ carries a BV algebra structure
  1317	whose product is wedge product of logarithmic forms, whose bracket is
  1318	the residue pairing, and whose Laplacian is the diagonal-residue
  1319	operator.
  1320	\end{theorem}
  1321	
  1322	\begin{proof}
  1323	Under the stated assumptions, the product is graded commutative by the
  1324	wedge-product sign rule, the bracket is generated from $\Delta$ by the
  1325	BV second-order identity, and the remaining BV axioms are exactly the
  1326	assumed nilpotence, Jacobi, and functorial compatibility conditions.
  1327	\end{proof}
  1328	
  1329	\subsection{Quantum master equation}

thinking
**Evaluating kappa notation issues**

I need to evaluate the issue with bare kappa notation since the user asked if any bare \kappa can exist without a family. While it seems that some uses, like \kappa(\cA), might be acceptable, I'm aware that per AGENTS, bare kappa is forbidden in certain contexts. The user wants consistency, so I should also check specific lines where kappa appears, like line 1439. It could be too complicated to check for undefined macros, but I'll explore possibilities to address the user’s needs efficiently.
thinking
**Auditing latex for undefined macros**

I need to check for any suspicious undefined macros like \barB that might be defined globally. Compiling the entire chapter might be too complicated and heavy, so I'll consider targeted builds. I could use commands like `latexmk -pdf -interaction=nonstopmode main.tex`, but they might yield too much information. Since the user wants an exhaustive audit, I'll focus on the strongest relevant verifications. Running `latexmk -pdf -interaction=nonstopmode -halt-on-error` could be a solid option for the file to ensure accuracy without overloading myself with unnecessary details.
thinking
**Determining root content issues**

I need to figure out the root of the problem. I could try using `rg --files '*.tex' | head`, but that might be a bit resource-intensive. The user specifically asked for grounding every claim in the actual contents of the file, which means I don't necessarily have to rely only on compile errors. I should be on the lookout for broken LaTeX environments and mismatched braces, which I might identify through text analysis instead.
thinking
**Searching for unused labels**

I need to check for any undefined references or labels. The user is specifically asking about unused labels, which means I should look into the compatibility labels around 1265. I might utilize tools like grep or rg for this. There are a few labels related to 1265, including one that seems to be an orphan. I should search globally across the repository and maybe note that there are only 11 theorem-like environments listed. I could script this process to extract label names and reference counts effectively.

exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2140,2170p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2140	\index{Enriques surface!Koszul datum}
  2141	The boundary VOAs of twisted supergravity on the non-Calabi--Yau
  2142	local surfaces listed in Table~\textup{\ref{tab:non-cy-local-surfaces}}
  2143	have the Koszul data shown there. Concretely:
  2144	\begin{enumerate}[label=\textup{(\roman*)},nosep]
  2145	\item \emph{Hirzebruch $\mathbb{F}_n$:} the characteristic lattice
  2146	 $H^{2}(\mathbb{F}_n, \mathbb{Z})$ has rank~$2$, so the boundary
  2147	 VOA decomposes into $n$ isomorphic $\beta\gamma$ pairs
  2148	 \textup{(}one pair per self-intersection unit along the fibre
  2149	 direction\textup{)}, giving
  2150	 $\kappa(\mathbb{F}_n) = n$ linearly in the Hirzebruch parameter.
  2151	\item \emph{del Pezzo $\mathrm{dP}_k$:} the dimension
  2152	 $\dim H^{2}(\mathrm{dP}_k, \mathbb{R}) = k + 1$ controls the
  2153	 number of $\beta\gamma$ pairs in the boundary VOA, giving
  2154	 $\kappa(\mathrm{dP}_k) = k + 1$. At $k = 0$ \textup{(}$\mathbb{P}^2$,
  2155	 $\kappa = 1$\textup{)} and $k = 8$ \textup{(}maximal blow-up,
  2156	 $\kappa = 9$\textup{)} the numerics should match the
  2157	 characteristic-lattice dimension prediction.
  2158	\item \emph{Enriques surface:} a $\mathbb{Z}/2$ quotient of a K3 surface,
  2159	 and the K3 boundary VOA carries $\kappa(\mathrm{K3}) = 24$
thinking
**Analyzing unused and cross-volume label references**

I'm reviewing label references in `bv_brst.tex` and cross-volume files, focusing on compatibility labels around lines 1265-1270 and other potentially unused ones. I’ll note that many such labels like `rem:w-algebra-bar-cobar` and `rem:ht-from-n4-sym` are only referenced internally or in audit/rectification logs, with no external `\ref` calls elsewhere. I'll summarize the findings with specific file paths and contexts to clarify where these labels appear and confirm their limited external usage.
exec
/bin/zsh -lc "rg -n 'rem:w-semi-infinite-conditional'" in /Users/raeez/chiral-bar-cobar succeeded in 72ms:
wave2_audit_20260413_001942/S11_bv_brst_to_body.md:1246:1248:\label{rem:w-semi-infinite-conditional}
metadata/label_index.json:37214:  "rem:w-semi-infinite-conditional": {
chapters/connections/bv_brst.tex:1248:\label{rem:w-semi-infinite-conditional}
exec
/bin/zsh -lc 'rg -n "Now we" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

codex
I’ve moved past the first-pass pattern scan. Next I’m checking reference hygiene and local structure, because this file has several compatibility labels and long heuristic stretches where aesthetic defects often hide second-order drift.
exec
/bin/zsh -lc "rg -n 'Theorem~D gives|Theorem~D\\b|We give four independent proofs|The proof uses four independent|The argument extends|The proof parallels|It remains to show|This is the' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
text=Path('chapters/connections/bv_brst.tex').read_text().splitlines()
for i,line in enumerate(text,1):
    if '\\\\label{' in line and ('\\\\section' not in line and '\\\\subsection' not in line and '\\\\begin{' not in line):
        print(f'{i}:{line}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
49:on the uniform-weight lane \textup{(}Theorem~D\textup{)}. The
137:\textup{(}Theorem~D, on the uniform-weight lane\textup{)}. At the
261:delta-function along $D_{ij}$. This is the loop-insertion operator in the bar
322:\textup{(}Theorem~D\textup{)}. For $\cA = \mathrm{Vir}_c$ with
630: configuration space. This is the ghost--propagator identification.
719:By Theorem~D \textup{(}$\kappa$-additivity under tensor product of chirally
940:The proof parallels that of
1076:the full moduli space cohomology. This is the mathematical
1221:This is the genus-$g$ complementarity statement for the principal
1406:for the Heisenberg family. The proof uses four independent
1429:We give four independent proofs, each arriving at the same
1435:Theorem~D gives $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
1450:at every genus $g \geq 1$. It remains to show that the BV free
1635:\textup{(}Theorem~D for uniform-weight algebras;
2182:pattern $F_g = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ of Theorem~D .
2254:The argument extends
2325:This is the same numerical contribution carried by the odd
 succeeded in 51ms:
2:\label{ch:bv-brst}
57:\label{rem:brst-anomaly-gkw}
74:\label{rem:bv-bar-bridge}
103:\label{rem:modular-qme-bv}
155:\label{rem:sft-bar-identification}
169:\label{def:bv-data-chiral}
183:\label{thm:bv-bar-geometric}
248:\label{def:bv-laplacian}
269:\label{rem:qme-bar-cobar}
289:\label{subsec:bv-bar-identification}
293:\ClaimStatusHeuristic]\label{rem:genus0-amplitude-bar}
336:\label{def:brst-operator}
355:\label{thm:brst-physical-states}
384:\label{thm:log-form-ghost-law}
429:\label{conj:bar-topological-brst}
441:\label{sec:brst-bar-chain-map}
464:\label{lem:brst-nilpotence}
475:\label{rem:brst-nilpotence-periodicity}
489:\label{thm:brst-bar-genus0}
611:\label{rem:bv-convergence}
exec
/bin/zsh -lc "python3 - <<'PY'
import re, subprocess, pathlib
p=pathlib.Path('chapters/connections/bv_brst.tex')
text=p.read_text()
labels=re.findall(r'\\\\label\\{(["'^}]+)'"\\}', text)
for lab in labels:
    rg = subprocess.run(['rg','-n',re.escape(lab),'.'],capture_output=True,text=True)
    lines=[ln for ln in rg.stdout.splitlines() if 'chapters/connections/bv_brst.tex' not in ln]
    print(lab)
    if lines:
        for ln in lines[:8]:
            print('  ',ln)
        if len(lines)>8:
            print('   ...', len(lines)-8, 'more')
    else:
        print('   NO_EXTERNAL_MATCH')
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\texttt\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

codex
- `rem:w-semi-infinite-conditional` (defined `chapters/connections/bv_brst.tex:1248`) is *not* referenced by any other `.tex` or `.md` in the repo; the only other occurrence is the audit note `wave2_audit_20260413_001942/S11_bv_brst_to_body.md:1246-1248`, which simply repeats the label for inspection purposes and does not generate a `\ref`/`\autoref`. No external document links to it.

- Compatibility labels added after the “Holomorphic-topological field theories” paragraph are likewise unreferenced elsewhere:
  * `rem:ht-from-n4-sym` (`bv_brst.tex:1266`) appears only in the same file, metadata (`metadata/label_index.json`), and the audit notes `compute/audit/ap5_cross_volume_report_wave6.md:131-134` and `compute/audit/ap5_post_wave7_verification.md:113`. None of those are cross-volume `\ref` calls, so nothing outside `bv_brst.tex` actually points at the label.
  * `rem:boundary-chiral-algebra-bv` (`bv_brst.tex:1267`) likewise only shows up in metadata and audit reports (same two files plus `rectification_20260412_233715/R02_higher_genus_complementarity.md:1047`, which just quotes the label).
  * `rem:bar-cobar-ht-boundary` (`bv_brst.tex:1268`) appears only in audit/rectification notes (`compute/audit/...`, `rectification_20260412_233715/R02_higher_genus_complementarity.md:1048`, etc.) and not in any other chapter reference.
  * `rem:w-algebra-bar-cobar` (`bv_brst.tex:1270`) again occurs only in metadata and audit reports (plus `rectification_20260412_233715/R02_higher_genus_complementarity.md:1050`); the only real `\label`/`\ref` pair in the repo lives in `chapters/connections/ht_physical_origins.tex` under the correctly prefixed `conj:w-algebra-bar-cobar`, so `rem:w-algebra-bar-cobar` itself never gets referenced outside `bv_brst.tex`.

Summary: the compatibility labels you flagged are defined solely in `bv_brst.tex`; apart from metadata/audit notes, no other source file in the repo ever refers to them.
exec
/bin/zsh -lc 'rg -n "compute layer" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1619:\textup{(}Verified in the compute layer:
2178:and the six-path $F_2$ verification in the compute layer. The
 succeeded in 2.38s:
ch:bv-brst
   ./wave2_audit_20260413_001942/F04_definitions_complementarity.md:1055:ch:bv-brst
   ./wave2_audit_20260413_001942/S07_preface_to_intro.md:565:  2230	BV-BRST (Ch.~\ref{ch:bv-brst}) &
   ./main.tex:1381:(Chapter~\ref{ch:bv-brst}); its genus tower is the string
   ./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:3:- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:24845 — PROBLEM: the main-theorem seam collapses MC5 into an undifferentiated “outside” conjectural region. Lines 24845-24846 say the four tests “exhaust the proved output,” and lines 24882-24885 list higher-genus `BV/BRST = bar` as simply outside, but `bv_brst.tex:30-40` and `1881-1969` explicitly split that surface into: proved genus-0 algebraic BRST/bar, proved Heisenberg scalar all-genus equality, and only a conditional coderived higher-genus lift, with class `\mathsf{M}` the obstruction locus. FIX: change line 24845 to `Four independent bar-side tests exhaust the proved output internal to the modular Koszul machine.` Replace lines 24878-24885 with: `Three regions lie outside these four bar-side tests: multi-weight universality at $g \geq 2$ (Open Problem~\ref{op:multi-generator-universality}, resolved negatively); the \emph{chain-level} higher-genus identity $\mathrm{BV}/\mathrm{BRST}=\mathrm{bar}$ (Conjecture~\ref{conj:master-bv-brst}); Chapter~\ref{ch:bv-brst} proves the genus-$0$ algebraic BRST/bar comparison (Theorem~\ref{thm:algebraic-string-dictionary}), proves the Heisenberg scalar equality at all genera (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and records the coderived lift only conditionally (Theorem~\ref{thm:bv-bar-coderived}); class~$\mathsf{M}$ is the chain-level obstruction locus; and non-perturbative completion.`
   ./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:219:     2	\label{ch:bv-brst}
   ./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:1583:/bin/zsh -lc 'rg -n -F "ch:bv-brst" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
   ./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:1669:- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:24845 — PROBLEM: the main-theorem seam collapses MC5 into an undifferentiated “outside” conjectural region. Lines 24845-24846 say the four tests “exhaust the proved output,” and lines 24882-24885 list higher-genus `BV/BRST = bar` as simply outside, but `bv_brst.tex:30-40` and `1881-1969` explicitly split that surface into: proved genus-0 algebraic BRST/bar, proved Heisenberg scalar all-genus equality, and only a conditional coderived higher-genus lift, with class `\mathsf{M}` the obstruction locus. FIX: change line 24845 to `Four independent bar-side tests exhaust the proved output internal to the modular Koszul machine.` Replace lines 24878-24885 with: `Three regions lie outside these four bar-side tests: multi-weight universality at $g \geq 2$ (Open Problem~\ref{op:multi-generator-universality}, resolved negatively); the \emph{chain-level} higher-genus identity $\mathrm{BV}/\mathrm{BRST}=\mathrm{bar}$ (Conjecture~\ref{conj:master-bv-brst}); Chapter~\ref{ch:bv-brst} proves the genus-$0$ algebraic BRST/bar comparison (Theorem~\ref{thm:algebraic-string-dictionary}), proves the Heisenberg scalar equality at all genera (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and records the coderived lift only conditionally (Theorem~\ref{thm:bv-bar-coderived}); class~$\mathsf{M}$ is the chain-level obstruction locus; and non-perturbative completion.`
   ./audit_campaign_20260412_231034/T12_MC5_BV_bar.md:180:chapters/connections/concordance.tex:695: Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
   ... 22 more
rem:brst-anomaly-gkw
   ./metadata/label_index.json:29578:  "rem:brst-anomaly-gkw": {
   ./audit_campaign_20260412_231034/BC06_genus_0.md:1159:\label{rem:brst-anomaly-gkw}
rem:bv-bar-bridge
   ./metadata/dependency_graph.dot:165:  rem_bv_bar_bridge [label="rem:bv-bar-bridge\nremark [He]\nBV/bar dictionary", style=filled, fillcolor="#ffccbc"];
   ./metadata/label_index.json:29614:  "rem:bv-bar-bridge": {
   ./chapters/connections/physical_origins.tex:15:\textup{(}Remark~\ref{rem:bv-bar-bridge}\textup{)}, the
   ./chapters/connections/thqg_critical_string_dichotomy.tex:2169:Remark~\ref{rem:bv-bar-bridge}? The quantum master
rem:modular-qme-bv
   ./metadata/label_index.json:33746:  "rem:modular-qme-bv": {
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1600,1650p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1600	\noindent\textbf{Path \textup{(d)}: numerical verification.}
  1601	\index{multi-path verification!Heisenberg BV/bar}
  1602	At each genus $g = 1, \ldots, 15$, three independent
  1603	implementations produce the same rational number $\lambda_g^{\mathrm{FP}}$:
  1604	\begin{enumerate}[label=\textup{(\roman*)},nosep]
  1605	\item the Bernoulli formula
  1606	 $\lambda_g^{\mathrm{FP}}
  1607	 = \frac{(2^{2g-1}-1)\,|B_{2g}|}{2^{2g-1}\,(2g)!}$;
  1608	\item the Taylor extraction of the $\hat{A}$-series
  1609	 $(\hbar/2)/\sin(\hbar/2) - 1
  1610	 = \sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\,\hbar^{2g}$;
  1611	\item a direct computation of the Faber--Pandharipande
  1612	 intersection integral on $\overline{\mathcal{M}}_{g,1}$
  1613	 via the string/dilaton equation and Witten's conjecture.
  1614	\end{enumerate}
  1615	All three agree at every genus tested. Sample values:
  1616	$\lambda_1^{\mathrm{FP}} = 1/24$,
  1617	$\lambda_2^{\mathrm{FP}} = 7/5760$,
  1618	$\lambda_3^{\mathrm{FP}} = 31/967680$.
  1619	\textup{(}Verified in the compute layer:
exec
/bin/zsh -lc 'rg -n "basically|obviously|crucially|really|clearly|plainly|literally" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'rg -n "should " chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1336:should be solved by the bar-cobar pairing. This is a heuristic
1342:The BV quantization of a chiral algebra $\mathcal{A}$ should be
2156: $\kappa = 9$\textup{)} the numerics should match the
codex
I’ve isolated the likely label-hygiene surface. A few labels have no external hits at all, so I’m distinguishing “compatibility anchor kept deliberately” from genuinely unreferenced labels before I include anything in the findings.
exec
/bin/zsh -lc "sed -n '1,120p' chapters/connections/bv_brst.tex | nl -ba -v1 && printf '\\n<<MID1>>\\n' && sed -n '1248,1275p' chapters/connections/bv_brst.tex | nl -ba -v1248 && printf '\\n<<MID2>>\\n' && sed -n '2170,2215p' chapters/connections/bv_brst.tex | nl -ba -v2170" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for lab in prop:wzw-brst-bar-genus0 eq:wzw-r-matrix-brst eq:wzw-kappa-brst rem:wzw-brst-bar-generic-level; do echo "LABEL:$lab"; rg -n "ref'"\\{"'$lab'"\\}|eqref\\{"'$lab'"\\}|autoref\\{"'$lab'"\\}|cref\\{"'$lab'"\\}|Cref\\{"'$lab'"\\}\" .; done" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	\chapter{BV-BRST formalism and Gaiotto's perspective}
     2	\label{ch:bv-brst}
     3	\index{Batalin--Vilkovisky|see{BV algebra}}
     4	
     5	The physicist's BRST cohomology and the algebraist's bar resolution
     6	are not analogous: they are the same computation. The BV formalism
     7	is a machine for computing derived functors; the bar complex is a
     8	machine for computing derived functors; at genus~$0$, they are the
     9	same machine applied to the same input. Costello's formulation of
    10	perturbative QFT as the theory of derived moduli problems makes the
    11	identification inevitable: the BRST operator computes the derived
    12	space of gauge-equivalence classes, which is what the bar differential
    13	computes on the algebraic side. What requires proof is not the
    14	coincidence but the precise scope of the agreement.
    15	
    16	The BV Laplacian and the sewing operator agree at genus~$0$. The
    17	quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
    18	the BV formalism coincides on $\mathbb{P}^1$ with the bar
    19	differential $d_{\mathrm{bar}}$ of the chiral algebra: the
    20	BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
 exited 1 in 77ms:
LABEL:prop:wzw-brst-bar-genus0
./chapters/connections/bv_brst.tex:2300:Proposition~\ref{prop:wzw-brst-bar-genus0}; the remaining content is
./chapters/connections/bv_brst.tex:2308:Proposition~\ref{prop:wzw-brst-bar-genus0} uses the chirally Koszul
LABEL:eq:wzw-r-matrix-brst
LABEL:eq:wzw-kappa-brst
LABEL:rem:wzw-brst-bar-generic-level
collab wait(call_D6M9sa3XpQcCL7CByvLRIImb)
  receivers: 019d83fe-8d6b-7281-bf56-6a2f62e315b3, 019d83fe-8d66-70e2-8e9a-dbe01560b35b
wait(call_D6M9sa3XpQcCL7CByvLRIImb) 1 agents complete:
  019d83fe-8d66-70e2-8e9a-dbe01560b35b completed: "- `rem:w-semi-infinite-conditional` (defined `chapters/connections/bv_brst.tex:1248`) is *not* referenced by any other `…"
exec
/bin/zsh -lc 'rg -n "expected" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
33:$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
314:The displayed comparison is the expected physics reading of these
2165:In all three cases, the shadow class is expected to be
collab wait(call_safApNn6xbqnoVF0fJ4lkgTP)
  receivers: 019d83fe-8d6b-7281-bf56-6a2f62e315b3
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '20,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    20	BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
    21	classical master equation is $d_{\mathrm{bar}}^2 = 0$, and anomaly
    22	cancellation ($c = 26$) is the condition $\kappa_{\mathrm{tot}} = 0$
    23	on the total Virasoro central charge of matter plus ghosts. Do
    24	they agree at all genera?
    25	
    26	A natural obstruction sits in the way. At higher genus, the BV
    27	Laplacian receives contributions from handle-gluing amplitudes that
    28	involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
    29	the bar differential collects OPE residues along FM boundary strata.
    30	What is proved in this chapter is the genus-$0$ BV/bar comparison
    31	and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
    32	the obstruction analysis isolates why classes~$\mathsf{G}$,
    33	$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
    34	class~$\mathsf{M}$, but it does not by itself produce a global
    35	chain-level quasi-isomorphism. The higher-genus coderived upgrade is
    36	therefore recorded only as the conditional criterion of
    37	Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
    38	filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
    39	the missing input is precisely a proof that the harmonic discrepancy
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '290,330p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   290	\index{BV algebra!bar complex identification}
   291	
   292	\begin{remark}[Heuristic genus-\texorpdfstring{$0$}{0} amplitude/bar comparison;
   293	\ClaimStatusHeuristic]\label{rem:genus0-amplitude-bar}
   294	\index{string amplitude!bar complex}
   295	Let $\cA$ be a chiral algebra on $\mathbb{P}^1$, and let
   296	$\omega_1, \ldots, \omega_n$ be cocycles in
   297	$\bar{B}^1(\cA)$. The heuristic genus-$0$ string-amplitude pairing
   298	\[
   299	\mathcal{A}_0(\omega_1, \ldots, \omega_n)
   300	\;=\;
   301	\int_{\overline{\mathcal{M}}_{0,n}}
   302	 \omega_1 \wedge \cdots \wedge \omega_n
   303	\]
   304	parallels the bar-complex Euler characteristic
   305	$\chi(\bar{B}^n_0(\cA))$, where $\bar{B}^n_0$ denotes the
   306	genus-$0$ component of the degree-$n$ bar complex. The exact
   307	identification between these two quantities is not proved in the
   308	manuscript.
   309	The bar complex is realized on
codex
- **AI-slop vocabulary**: none of the classic trigger words (e.g., *notably*, *crucially*, *obviously*) appear in this chapter.

- **Em dashes**: no em dashes (`—`) are present.

- **Markdown in LaTeX**: no backtick-delimited code spans or `**bold**` markdown snippets occur; the nearest quotes use proper TeX conventions.

- **“In this chapter we” / weak opening**: the chapter avoids the canonical weak opener and there are no “we now turn to”/“now we” signposts.

- **Passive hedging phrases** (exact line references and quoted snippets):
  - line 33: “the obstruction analysis isolates why classes \(\mathsf{G}\), \(\mathsf{L}\), and \(\mathsf{C}\) are expected to behave better than class \(\mathsf{M}\)…”.
  - line 314: “The displayed comparison is the expected physics reading of these configuration-space forms, but the chapter does not prove…”.
  - line 860: “The chain map \(\Phi\) should extend to a map of genus-graded complexes…”.
  - line 1336: “\(\Delta e^{S/\hbar} = 0\) should be solved by the bar-cobar pairing…”.
  - line 1342: “The BV quantization of a chiral algebra \(\mathcal{A}\) should be equivalent to computing the bar-cobar homology…”.
  - line 2156: “\(\kappa = 9\) the numerics should match the characteristic-lattice dimension prediction.”
  - line 2165: “In all three cases, the shadow class is expected to be \(\mathsf{C}\) on the generic locus…”

- **Signpost transitions (“we now turn to” etc.)**: none detected.

- **Dead code / TODO / comment blocks**: no TODO/FIXME-style markers or commented-out material remain in this file.

- **Typographic defects (double spaces, malformed displays, awkward spacing)**: no systematic defects stood out; spacing around displays and punctuation is consistent.

- **Local redundancy / transition issues**: the flow doesn’t introduce redundant “this chapter does X’/’also X” phrasing beyond the normal mathematical scaffolding.
wait(call_safApNn6xbqnoVF0fJ4lkgTP) 1 agents complete:
  019d83fe-8d6b-7281-bf56-6a2f62e315b3 completed: "- **AI-slop vocabulary**: none of the classic trigger words (e.g., *notably*, *crucially*, *obviously*) appear in this c…"

thinking
**Analyzing code compatibility**

I noticed the Explorer says there's no dead code or TODOs, but we found some potential compatibility labels. The user specified dead code includes commented-out sections over 10 lines, unused labels, and TODOs, so I'm thinking compatibility labels might count as unused labels. 

I need to decide if I should search for exact references, especially for `rem:w-semi-infinite-conditional`. I'll check the whole repository, as there could be more unused labels. Next, I'll look into how to compile a list of labels with zero references. Let's get started!
codex
I’ve got one likely dead-surface cluster already: compatibility labels that nothing actually references. I’m running a full label-use pass across the file now so I can separate that real dead surface from labels that merely lack external references but are still used locally.
exec
/bin/zsh -lc "rg -n 'Theorem~D\\.|Theorem~D gives|the current record|this chapter does not prove|remains heuristic|should extend|should be equivalent|is expected to be|are expected to behave' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
33:$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
1252:$\mathcal{W}$-algebra pairs. On the current record, that
1354:The identification remains heuristic for general chiral algebras,
1435:Theorem~D gives $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
2165:In all three cases, the shadow class is expected to be
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
text=Path('chapters/connections/bv_brst.tex').read_text().splitlines()
for i,line in enumerate(text,1):
    if 'Theorem~D .' in line or 'Theorem~D .' in line.replace('~',' '):
        print(i, line)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, subprocess
text = pathlib.Path('chapters/connections/bv_brst.tex').read_text()
labels = re.findall(r'\\\\label\\{(["'^}]+)'"\\}', text)
for lab in labels:
    pat = rf'(?:eqref|ref|autoref|cref|Cref)\\{{{re.escape(lab)}\\}}'
    rg = subprocess.run(['rg','-n',pat,'.'],capture_output=True,text=True)
    refs = [ln for ln in rg.stdout.splitlines() if True]
    if not refs:
        print(f'UNUSED:{lab}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2182 pattern $F_g = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ of Theorem~D .
 succeeded in 3.73s:
UNUSED:rem:brst-anomaly-gkw
UNUSED:rem:modular-qme-bv
UNUSED:rem:sft-bar-identification
UNUSED:def:bv-data-chiral
UNUSED:def:bv-laplacian
UNUSED:rem:qme-bar-cobar
UNUSED:subsec:bv-bar-identification
UNUSED:rem:genus0-amplitude-bar
UNUSED:rem:genus1-bv
UNUSED:rem:anomaly-curvature-bv
UNUSED:def:brst-operator
UNUSED:thm:brst-physical-states
UNUSED:conj:bar-topological-brst
UNUSED:eq:brst-differential
UNUSED:rem:brst-nilpotence-periodicity
UNUSED:rem:bv-convergence
UNUSED:comp:superstring-ghost-koszul
UNUSED:rem:brst-bar-higher-genus
UNUSED:sec:semi-infinite-bar
UNUSED:def:semi-infinite-cohomology




thinking
**Deciding on label reporting**

I'm contemplating how to approach label reporting in the script. It catches explicit references, but many labels could be established through metadata, not just text. The user has asked for a report on unused labels, but providing all might be overwhelming. It's essential to focus on dead labels, particularly those clearly unrelated or low severity ones. The user wants every finding, but I need to decide the best way to summarize without exceeding the line limit while addressing them comprehensively.
thinking
**Clarifying reporting structure**

The user has requested every finding with exact lines and fixes. I think grouping contiguous lines or multiple labels with the same fix into one bullet point could work well. The format is clear: [SEVERITY] file:line — PROBLEM: ... FIX: ... It seems like citing multiple line numbers for a single issue should be okay, perhaps just the first one. Grouping problems spanning multiple lines might make sense too. However, only focusing on compatibility labels could be a better approach since other unused labels might not be dead code after all.
thinking
**Determining label statuses**

I’m considering the status of labels used solely as anchors for future references. They might not be dead, especially if the file comments say they're preserved for cross-reference compatibility, but with no actual cross-references found, that seems contradictory. For other labels, I can’t confirm explicit references, but they could still be used by tooling through metadata. Since the user wants to know about dead code, it might be best to be cautious and not label all unused ones as dead without clearer evidence.
thinking
**Exploring build options**

Building might take a while, but I could consider using `texfot` or `lualatex` and check if the root tex file like `main.tex` exists. Since the repo is large, the build could be heavy, but if it’s just for a cosmetic audit, I might not need to build everything. I should inspect for broken LaTeX environments and mismatched braces, possibly using a quick parser or a basic script for matching begin/end counts. Let's see if `chktex -q -n8` is available.
codex
The cosmetic surface is mostly prose, but I still need to rule out hidden TeX breakage before I finalize. I’m doing a lightweight structural check on the file now: environment balance and obvious formatting hazards, without widening into a full build unless the file itself looks unstable.
exec
/bin/zsh -lc "rg -n '\\\\texttt\\{|\\\\verb|\\\\begin\\{proof\\}\\[|\\bTODO\\b|\\bFIXME\\b|\\\\emph\\{Step~|\\\\noindent\\\\textbf\\{|Theorem~D \\.|\\"'$'"\\"'$'"' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
text=Path('chapters/connections/bv_brst.tex').read_text()
# strip comments
lines=[]
for line in text.splitlines():
    if '%' in line:
        i=0
        out=''
        while i < len(line):
            if line[i]=='%' and (i==0 or line[i-1] "'!= '"'\\\\'):
                break
            out += line[i]
            i += 1
        lines.append(out)
    else:
        lines.append(line)
text='\\n'.join(lines)
# begin/end balance
stack=[]
for m in re.finditer(r'\\\\(begin|end)\\{(["'^}]+)'"\\}', text):
    kind, env = m.group(1), m.group(2)
    line = text.count('\\n', 0, m.start()) + 1
    if kind=='begin':
        stack.append((env,line))
    else:
        if not stack or stack[-1][0]"'!=env:
            print(f'"'MISMATCH end {env} at line {line}, stack top {stack[-1] if stack else None}')
            break
        stack.pop()
else:
    if stack:
        print('UNMATCHED begins:', stack[-10:])
    else:
        print('ENV_OK')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
197:\begin{proof}[Geometric construction supporting \textup{Theorem~\ref{thm:bv-bar-geometric}}]
198:\emph{Step~1: Bar generators.}
205:\emph{Step~2: BV Bracket.}
238:\emph{Step~3: Master Equation.}
510:\emph{Step~1: Conformal weight filtration.}
532:\emph{Step~2: Associated graded.}
562:\emph{Step~3: Spectral sequence comparison.}
586:\emph{Step~4: Lifting to a chain map.}
945:\emph{Step~1: Conformal weight filtration.}
958:\emph{Step~2: Associated graded.}
977:\emph{Step~3: Spectral sequence comparison.}
988:\emph{Step~4: No anomaly obstruction.}
1434:\noindent\textbf{Preliminary: the bar side.}
1454:\noindent\textbf{Path \textup{(a)}: Quillen anomaly + GRR.}
1470:\emph{Step~1} \textup{(}Quillen anomaly\textup{)}.
1481:\emph{Step~2} \textup{(}Scaling\textup{)}.
1487:\emph{Step~3} \textup{(}GRR + family index\textup{)}.
1505:\emph{Step~4} \textup{(}Faber--Pandharipande\textup{)}.
1522:\noindent\textbf{Path \textup{(b)}: Selberg zeta function.}
1561:\noindent\textbf{Path \textup{(c)}: direct family index.}
exec
/bin/zsh -lc 'command -v chktex >/dev/null && chktex -q -n22 -n30 -n8 chapters/connections/bv_brst.tex || echo CHKTEX_UNAVAILABLE' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
ENV_OK
 succeeded in 58ms:
Warning 24 in chapters/connections/bv_brst.tex line 2: Delete this space to maintain correct pagereferences.
\label{ch:bv-brst}  
^
Warning 24 in chapters/connections/bv_brst.tex line 3: Delete this space to maintain correct pagereferences.
\index{Batalin--Vilkovisky|see{BV algebra}}  
^
Warning 9 in chapters/connections/bv_brst.tex line 44: `)' expected, found `}'.
\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.  
         ^
Warning 9 in chapters/connections/bv_brst.tex line 44: `}' expected, found `)'.
\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.  
                                                                ^
Warning 9 in chapters/connections/bv_brst.tex line 49: `)' expected, found `}'.
on the uniform-weight lane \textup{(}Theorem~D\textup{)}. The  
                                    ^
Warning 9 in chapters/connections/bv_brst.tex line 49: `}' expected, found `)'.
on the uniform-weight lane \textup{(}Theorem~D\textup{)}. The  
                                                      ^
Warning 24 in chapters/connections/bv_brst.tex line 57: Delete this space to maintain correct pagereferences.
\label{rem:brst-anomaly-gkw}  





thinking
**Processing typographic issues**

I need to go through the chktex output, which has many warnings, specifically Warning 24 about labels having trailing spaces. That might be due to extra spaces added in the command output. Also, there's Warning 9 related to the misuse of `\textup{(}` for parentheses, which could be a style issue since the user is focused on typography. The best solution would be to replace these with standard parentheses or to use `\textup{(...)}.` I might want to group issues by severity rather than listing each one individually.
thinking
**Identifying typographic issues**

I can point out a specific problem in the file where parentheses are repeatedly wrapped as `\textup{(}...\textup{)}`. This is causing chktex warnings and affecting readability. The fix would involve replacing instances like `(Theorem\ref{thm:heisenberg-bv-bar-all-genera})` and doing so for similar cases in the file, such as on lines 49, 81-82, and others. The user asked for exact line numbers for every finding, so I'll need to keep track of each one, even if it makes the report lengthy. It's important to be thorough.
thinking
**Evaluating opening quality**

I'm assessing the opening quality of the text. It seems line 30 says, "What is proved in this chapter is..." which doesn't really serve as a strong opening since it implies a deficiency. I think I need to clarify that an opening statement should be engaging rather than reflecting a problem. So for this line, there aren’t any significant findings to report, but I need to note how passive language is used in several lines.
thinking
**Inspecting typography errors**

I’ve noticed an extra space before a period on line 2182. There might be an issue with line 782, where display math starts with "By the formula" without proper punctuation, which looks like a syntactic break. Upon inspection, I see the inline math is immediately followed by a display without punctuation, so it would help to end the sentence with a comma. I should also flag a couple of warnings about parentheses in inline math and check for typographical defects noted by `chktex`.
thinking
**Gathering context for revisions**

I need to ground my findings in the lines I've read and cite the `chktex` verification to support my claims. I shouldn't mention the categories without issues explicitly; a concise summary will do. It’s essential to check if the line numbers have changed in the file. Since I have the original line numbers, that's good. I should inspect specific hedging lines and propose exact rewrite suggestions for each finding, gathering context around each. Using `sed` for text replacements might be helpful.
codex
The structural check is useful: the file is environment-balanced, but `chktex` confirms a recurring typographic pathology the raw read already suggested. I’m narrowing that into exact, line-level fixes rather than dumping linter noise.
exec
/bin/zsh -lc "sed -n '1249,1271p;2174,2184p;2198,2213p;777,790p' chapters/connections/bv_brst.tex | nl -ba -v777" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '40,50p;718,726p;1038,1062p;1428,1450p;1600,1621p' chapters/connections/bv_brst.tex | nl -ba -v40" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '24,38p;308,318p;852,864p;1331,1346p;2150,2169p' chapters/connections/bv_brst.tex | nl -ba -v24" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
    40	factors through the curvature. The Heisenberg case is resolved at the
    41	scalar level at all genera:
    42	$F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
    43	= \kappa \cdot \lambda_g^{\mathrm{FP}}$
    44	\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
    45	For general algebras what survives at every genus is the scalar
    46	anomaly package: the universal MC class $\Theta_\cA$ encodes the
    47	one-loop anomaly coefficient $\kappa(\cA)$, and its projection
    48	onto $H^2(\overline{\mathcal{M}}_{g,n})$ gives $F_g = \kappa(\cA) \cdot \lambda_g$
    49	on the uniform-weight lane \textup{(}Theorem~D\textup{)}. The
    50	multi-weight correction $\delta F_g^{\mathrm{cross}}$ is where the
    51	\begin{proof}
    52	By Theorem~D \textup{(}$\kappa$-additivity under tensor product of chirally
    53	Koszul algebras, uniform-weight lane; see
    54	Theorem~\ref{thm:explicit-theta}\textup{)},
    55	$\kappa(\cA_{\mathrm{matter}}^! \otimes \widetilde{\cA}_{\mathrm{ghost}})
    56	= \kappa(\cA_{\mathrm{matter}}^!) + \kappa(\widetilde{\cA}_{\mathrm{ghost}})$.
    57	The free\slash Kac--Moody complementarity sum gives
    58	$\kappa(\cA_{\mathrm{matter}}^!) = -\kappa(\cA_{\mathrm{matter}})$,
    59	and the matching involution hypothesis gives
 succeeded in 50ms:
    24	they agree at all genera?
    25	
    26	A natural obstruction sits in the way. At higher genus, the BV
    27	Laplacian receives contributions from handle-gluing amplitudes that
    28	involve the full moduli space $\overline{\mathcal{M}}_{g,n}$, while
    29	the bar differential collects OPE residues along FM boundary strata.
    30	What is proved in this chapter is the genus-$0$ BV/bar comparison
    31	and the all-genera scalar Heisenberg identity. Beyond genus~$0$,
    32	the obstruction analysis isolates why classes~$\mathsf{G}$,
    33	$\mathsf{L}$, and~$\mathsf{C}$ are expected to behave better than
    34	class~$\mathsf{M}$, but it does not by itself produce a global
    35	chain-level quasi-isomorphism. The higher-genus coderived upgrade is
    36	therefore recorded only as the conditional criterion of
    37	Theorem~\ref{thm:bv-bar-coderived}: one needs a comparison map of
    38	filtered curved models whose cone is coacyclic, and in class~$\mathsf{M}$
    39	manuscript.
    40	The bar complex is realized on
    41	$\overline{C}_n(\mathbb{P}^1) = \overline{\mathcal{M}}_{0,n+1}$
    42	(Theorem~\ref{thm:bar-cobar-isomorphism-main}),
    43	with the bar differential given by residues of the FM propagator
 succeeded in 50ms:
   777	the bilinear pairing but reverses the total $\kappa$.
   778	
   779	For the superstring, the ghost sector enlarges to
   780	$(bc) \otimes (\beta\gamma)$, where the superghost
   781	$\beta\gamma$ system sits at $\lambda = 3/2$. By the
   782	formula $c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)$ \[
   783	 c_{\beta\gamma}(\tfrac{3}{2})
   784	 \;=\; 2\bigl(6 \cdot \tfrac{9}{4}
   785	 - 6 \cdot \tfrac{3}{2} + 1\bigr)
   786	 \;=\; 2\bigl(\tfrac{27}{2} - 9 + 1\bigr)
   787	 \;=\; 2 \cdot \tfrac{11}{2}
   788	 \;=\; 11,
   789	\]
   790	hence $\kappa_{\beta\gamma} = c_{\beta\gamma}/2 = 11/2$, and the
   791	If Theorem~\ref{thm:bar-semi-infinite-w} holds, then
   792	Corollary~\ref{cor:anomaly-duality-w} acquires the intended
   793	semi-infinite anomaly interpretation for principal
   794	$\mathcal{W}$-algebra pairs. On the current record, that
   795	interpretation remains conditional on explicit DS/bar
   796	compatibility.

thinking
**Reviewing the theorem details**

I'm trying to determine if there's conflicting wording around a certain theorem in the file. For instance, line 915 mentions a bar complex equating to a semi-infinite complex, while line 2193 brings up an affine bar complex. That seems different. I might need to check lines 1259-1263 for any abrupt transitions that aren't mathematically warranted. The main concern is the dead labels; overall, the cosmetic audit may categorize issues as mostly LOW/MEDIUM, except for a HIGH concern due to broken displays.
exec
/bin/zsh -lc "rg -n '\\\\textup\\{\\(\\}|\\\\textup\\{\\)\\}' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
44:\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
49:on the uniform-weight lane \textup{(}Theorem~D\textup{)}. The
81: \textup{(}Theorem~\textup{\ref{thm:bv-bar-geometric}}, proved
82: elsewhere\textup{)};
108:\textup{(}Theorem~\ref{thm:mc2-bar-intrinsic}\textup{)}.
137:\textup{(}Theorem~D, on the uniform-weight lane\textup{)}. At the
265:\textup{(}Theorem~\ref{thm:config-space-bv}\textup{)}.
322:\textup{(}Theorem~D\textup{)}. For $\cA = \mathrm{Vir}_c$ with
492:$c(\cA) = 26$ \textup{(}so that
494:$\kappa_{\mathrm{tot}} = 0$\textup{)}. There exists a chain map
643:\textup{(}Theorem~\textup{\ref{thm:anomaly-koszul})} is equivalent,
648: if and only if $c(\cA) = 26$ \textup{(}Lemma~\textup{\ref{lem:brst-nilpotence})}.
651: \textup{(}Theorem~\textup{\ref{thm:anomaly-koszul})}.
692:\textup{(}Theorem~\ref{thm:quantum-complementarity-main}, free\slash Kac--Moody
693:branch\textup{)}. Let $\widetilde{\cA}_{\mathrm{ghost}}$ be a ghost sector
719:By Theorem~D \textup{(}$\kappa$-additivity under tensor product of chirally
721:Theorem~\ref{thm:explicit-theta}\textup{)},
745:\textup{(}complementarity for the free\slash Heisenberg family,
749:the Virasoro branch where $\kappa + \kappa' = 13$\textup{)}.
758:\textup{(}Remark~\textup{\ref{rem:ghost-superghost-koszul})}.

thinking
**Analyzing code comments and formatting**

I'm looking at some local repetitions of "current record." They could be aesthetic but might not relate directly to a theorem, so I could skip those for now. I'm considering whether comments on lines 2203 and 2209 are adding value or just creating noise. Lines like 1051 and 1055 seem malformed with nested `\textup`, which might be a minor issue to flag. Also, I'm noticing a warning about spacing before parentheses in line 223, which is definitely a typography concern.
exec
/bin/zsh -lc "rg -n '\\\\ClaimStatus["'^]]*'"\\}\\s+\\\\cite|\\\\cite\\{["'^}]+'"\\};|\\\\ref\\{["'^}]+'"\\}\\([0-9ivx]+' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
182:\begin{theorem}[BV complex $=$ geometric bar complex; \ClaimStatusProvedElsewhere{} \cite{CG17}]
193:\cite{CG17}; the following geometric construction explains the
223:the transverse divisor $D_{ik}$ (Theorem~\ref{thm:FM}(3):
354:\begin{theorem}[BRST cohomology = physical states; \ClaimStatusProvedElsewhere{} \cite{CG17}]
463:\begin{lemma}[BRST nilpotence; \ClaimStatusProvedElsewhere{} \cite{FGZ86}]
589:(Eilenberg--Moore~\cite{EM66}; see also
982:(\cite{EM66}; cf.\ \cite[Theorem~5.2.12]{Weibel94}), $\Phi_0$ lifts
1051:\textup{(}Theorem~\textup{\ref{thm:genus-universality}(i))} equals
1055:of Theorem~\textup{\ref{thm:genus-universality}(ii)} is the
1084:by Theorem~\ref{thm:genus-universality}(ii).

thinking
**Checking citation formatting**

I think the citation formatting around line 589/982 looks fine! I should look for terms that start with `Part\ref{...} \textup{(` to ensure everything’s consistent. I might want to verify if there are any unnecessary AI-related words, but maybe that’s not necessary. Also, I need to watch for any double spaces or trailing spaces. The "chktex" warnings seem to suggest I should delete some spaces at the ends of label or index lines, so I’ll check for that.
exec
/bin/zsh -lc "sed -n '1,5p;55,60p;1248,1270p;1950,1975p' chapters/connections/bv_brst.tex | cat -vet" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\chapter{BV-BRST formalism and Gaiotto's perspective}$
\label{ch:bv-brst}$
\index{Batalin--Vilkovisky|see{BV algebra}}$
$
The physicist's BRST cohomology and the algebraist's bar resolution$
$
\begin{remark}[BRST anomaly brackets and transferred SC operations]$
\label{rem:brst-anomaly-gkw}$
\index{Gaiotto--Kulp--Wu!BRST anomaly brackets}$
\index{BRST operator!GKW higher operations}$
The BRST-anomaly brackets of Gaiotto--Kulp--Wu~\cite{GKW2025}$
\label{rem:w-semi-infinite-conditional}$
If Theorem~\ref{thm:bar-semi-infinite-w} holds, then$
Corollary~\ref{cor:anomaly-duality-w} acquires the intended$
semi-infinite anomaly interpretation for principal$
$\mathcal{W}$-algebra pairs. On the current record, that$
interpretation remains conditional on explicit DS/bar$
compatibility.$
\end{remark}$
$
exec
/bin/zsh -lc "rg -n '\\\\Omega/z|\\\\Omega\\\\,d\\\\log z|r\\"'^'"\\{["'^}]+'"\\}\\(z\\) = \\\\Omega/z|r\\(z\\) = \\\\Omega/z|("'^|[''^A-Za-z])'"\\\\kappa(["'^_'"\\(A-Za-z]|"'$)'"' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
42:$F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
43:= \kappa \cdot \lambda_g^{\mathrm{FP}}$
613:Theorem~\ref{thm:brst-bar-genus0} realizes the parallel-track identifications of Remarks~\ref{rem:bv-parallel-track} and~\ref{rem:anomaly-parallel-track}: in~\eqref{eq:master-square}, $\barB_X(\cA)$ is the BV complex, $\barB_X(\cA^!)$ the ghost complex, $\mathbb{D}_{\mathrm{Ran}}$ the field--antifield exchange, and $\dfib^{\,2} = \kappa \cdot \omega_1$ the conformal anomaly. The square commutes precisely when $\kappa = 0$.
719:By Theorem~D \textup{(}$\kappa$-additivity under tensor product of chirally
739:contributes $\kappa = 1/2$, so the total is $13$);
746:$\kappa(\mathcal{H}_\kappa) + \kappa(\mathcal{H}_\kappa^!) = 0$;
749:the Virasoro branch where $\kappa + \kappa' = 13$\textup{)}.
771:$\kappa + \kappa' = -26 \neq 13$ shows that the $bc$ system is
774:$\kappa + \kappa' = 13$\textup{)}: the $bc$ ghost is self-dual
777:the bilinear pairing but reverses the total $\kappa$.
791:Koszul dual satisfies $\kappa'_{\beta\gamma} = -11/2$.
831: $\kappa = -13$;
833: at $\lambda = 3/2$, with total $\kappa = -15/2$.
848:\textup{(}which would require $\kappa + \kappa' = 13$\textup{)}:
993:$m_0 = \kappa \cdot \mathbf{1}$ contributes to the $A_\infty$
1096:curvature $m_0 = \kappa \cdot \mathbf{1}$ in the bar complex
1104:$\kappa = (k+h^\vee)\dim\fg/(2h^\vee)$: replacing $k$ by
1105:$-k - 2h^\vee$ negates~$\kappa$.
1119:Via Corollary~\ref{cor:anomaly-duality-km}, every entry in the Master Table (Table~\ref{tab:master-invariants}) is a semi-infinite anomaly coefficient: $\kappa$ is the semi-infinite anomaly, $c + c' = 2\dim\fg$ the total Feigin--Frenkel anomaly, and $F_g$ the genus-$g$ WZW free energy.
1414:For the Heisenberg vertex algebra $\cH_\kappa$ at level

thinking
**Considering notation issues**

I need to decide if bare kappa lines are issues in my context. For instance, line 613 has `\dfib^{2}=\kappa\cdot\omega_1`, which is definitely a bare kappa without a family. I could fix it to `\dfib^{\,2} = \kappa(\cA)\cdot\omega_1`. Lines 993, 1096, and 2021 also use bare kappa generically, presenting a consistency issue. I should inspect the context around several lines to find the exact fixes needed. I'll use sed for this.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '608,615p;988,999p;1093,1106p;1116,1120p;2014,2023p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   608	\end{proof}
   609	
   610	\begin{remark}[BV/BRST reading of the master square]
   611	\label{rem:bv-convergence}
   612	\index{BV complex!convergence with bar complex}
   613	Theorem~\ref{thm:brst-bar-genus0} realizes the parallel-track identifications of Remarks~\ref{rem:bv-parallel-track} and~\ref{rem:anomaly-parallel-track}: in~\eqref{eq:master-square}, $\barB_X(\cA)$ is the BV complex, $\barB_X(\cA^!)$ the ghost complex, $\mathbb{D}_{\mathrm{Ran}}$ the field--antifield exchange, and $\dfib^{\,2} = \kappa \cdot \omega_1$ the conformal anomaly. The square commutes precisely when $\kappa = 0$.
   614	\end{remark}
   615	
   988	\emph{Step~4: No anomaly obstruction.}
   989	Unlike Theorem~\ref{thm:brst-bar-genus0}, no central charge
   990	condition is needed. On the bar side, $d_{\mathrm{bar}}^2 = 0$
   991	by the Arnold relations
   992	(Theorem~\ref{thm:arnold-three}); the curvature
   993	$m_0 = \kappa \cdot \mathbf{1}$ contributes to the $A_\infty$
   994	structure but does not obstruct the bar differential. On the
   995	semi-infinite side, $Q_{\mathrm{si}}^2 = 0$ by
   996	construction~\cite{FGZ86}: the semi-infinite wedge product
   997	absorbs the charge anomaly that would otherwise require
   998	$c = 26$. Both differentials square to zero at every level
   999	$k \neq -h^\vee$, and the spectral sequence comparison





thinking
**Reviewing kappa clusters**

I’m flagging some lines in the text that need adjustments, particularly those with bare kappa clusters. I have specific replacements for lines 613, 993, 1096-1105, 1119, and 2021 to ensure clarity around the notation. I'm considering that some kappa mentions in the Heisenberg theorem summary might also need noting, especially lines 42-43 and 1417-1419, since there are some ambiguities. It seems like this could improve the overall accuracy of the document.
thinking
**Considering kappa notation**

It seems that using bare `\kappa` might not be essential since it acts as a level parameter. I should probably skip it for now. I need to ensure that the formula doesn't use bare `\Omega/z` without a corresponding `k` found, as that could lead to issues. I don't think any undefined macro problems showed up during structural checks. I might want to look over line 44 for the `\textup{(}` pattern and possibly reference relevant line numbers as well.
thinking
**Analyzing text issues**

I’m considering potential fixes for a text cluster with various compatibility and typographic labels. Some lines have high or medium compatibility issues, and I might need to rewrite hedging lines individually for better clarity. Additionally, I've spotted extra spaces, broken displays, and missing citation spacing. Grouping related typographic issues could help streamline revisions. I also need to assess the transition quality in certain sections and address possible redundancy issues. There’s a lot to tackle!
thinking
**Evaluating section transition issues**

I'm reviewing the section on "topological field theories" from lines 1257-1270. It seems to mainly indicate that the content is elsewhere, with dead labels, which doesn't help transition smoothly. To address this, I could either merge it into a bridge sentence at the end of the previous section or replace it with a necessary mathematical bridge. The suggested fix is clear: remove the section heading and compatibility labels, simplify with a one-sentence bridge, and then continue with the following section. This seems to enhance clarity and address dead code effectively.
thinking
**Inspecting redundancy and transitions**

I'm considering the section starting at lines 166-167, and whether it flows smoothly from the previous remark. The file structure seems mostly okay. However, I think there might be some unnecessary redundancy in lines 90-99 after the BV/bar dictionary. It lists three items, labeling them as theorems, which feels more like a status clarification than redundancy. There's another instance from lines 283-286 that restates the previous paragraph (271-280). I should inspect those lines closely to determine if the redundancy is truly needed.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '268,287p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   268	\begin{remark}[Heuristic QME/MC comparison; \ClaimStatusHeuristic]
   269	\label{rem:qme-bar-cobar}
   270	\index{quantum master equation|textbf}
   271	At genus~$0$, the classical part of the BV master equation matches the
   272	square-zero bar differential after transporting through the external
   273	comparison of Theorem~\ref{thm:bv-bar-geometric}. Extending this to a
   274	full identification of the quantum master equation
   275	\[
   276	\hbar\,\Delta_{\mathrm{BV}}S + \tfrac{1}{2}\{S,S\}=0
   277	\]
   278	with a Maurer--Cartan equation in a BV-enhanced bar/cobar deformation
   279	complex would require the conditional BV package recorded in
   280	Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. That
   281	full comparison is not proved here.
   282	
   283	The classical genus-$0$ comparison combines the external BV/bar
   284	identification with the square-zero bar differential on the
   285	uncurved locus. The quantum, Laplacian, and functorial parts are
   286	isolated as conditional content later in this chapter.
   287	\end{remark}

thinking
**Identifying redundancies in text**

I’ve noticed that the second paragraph is redundant. Specifically, lines 283-286 repeat lines 271-281 without adding any new content, so I should just delete those lines. That's a good catch! I wonder if there’s another redundancy around lines 94-99, following the dictionary items. I should probably take a closer look to confirm that. Let's keep inspecting to ensure the text is clear and concise!
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '73,100p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    73	\begin{remark}[BV/bar dictionary; \ClaimStatusHeuristic]
    74	\label{rem:bv-bar-bridge}
    75	\index{BV algebra!bar complex bridge|textbf}
    76	Let $\cA$ be a chiral algebra on a smooth curve~$X$. The BV and
    77	bar-cobar formalisms are related by the following dictionary:
    78	\begin{enumerate}[label=\textup{(\roman*)}]
    79	\item the geometric BV complex and the geometric bar complex are
    80	 identified at genus~$0$
    81	 \textup{(}Theorem~\textup{\ref{thm:bv-bar-geometric}}, proved
    82	 elsewhere\textup{)};
    83	\item the classical master equation corresponds to the
    84	 genus-$0$ square-zero condition for the bar differential after
    85	 transporting through that external comparison;
    86	\item the scalar genus-$1$ obstruction is the modular characteristic
    87	 $\kappa(\cA)$, the one-loop anomaly
    88	 coefficient.
    89	\end{enumerate}
    90	The chain-level identifications (antifields versus
    91	cogenerators, the BV Laplacian, the full quantum master equation,
    92	BRST versus bar cohomology) remain heuristic in this manuscript.

thinking
**Clarifying status details**

I'm considering whether the line 1450, which states, "It remains to show that the BV free," needs more context. I want to make sure there's enough information for clarity. It’s important to inspect the next line too. I'll focus on ensuring that redundancy isn’t an issue here, but rather a way to clarify the status of the discussion. Let’s take it step by step and ensure everything is clear!
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1448,1458p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1448	Therefore
  1449	$F_g^{\mathrm{bar}}(\cH_\kappa) = \kappa \cdot \lambda_g^{\mathrm{FP}}$
  1450	at every genus $g \geq 1$. It remains to show that the BV free
  1451	energy agrees.
  1452	
  1453	\medskip
  1454	\noindent\textbf{Path \textup{(a)}: Quillen anomaly + GRR.}
  1455	\index{Quillen metric!BV/bar proof|(}
  1456	The BV partition function of $\kappa$ free bosons on a compact
  1457	Riemann surface~$\Sigma_g$ of genus~$g$ is the Gaussian functional
  1458	integral





thinking
**Rephrasing terminology**

I can rephrase the statement by replacing `$\kappa$ is the semi-infinite anomaly` with `$\kappa(\widehat{\fg}_k)$ is the semi-infinite anomaly coefficient`. This change clarifies the expression and makes it more precise. I find that expressing complex ideas in clearer terms is always beneficial for better understanding. Let’s make sure the notation is consistent and aligns with the context so that it conveys the intended meaning effectively!
thinking
**Inspecting formatting issues**

I need to check for an extra space before a period at line 2182 and identify lines 782-789, which have a malformed display due to missing punctuation. I think the issues are low to medium priority. 

For example, I could clarify line 223 and make a small adjustment. I also see some missing non-breaking spaces before citations at lines 182, 354, and 463. The user mentioned wanting to focus on aesthetics, so I should note these citation issues, and I might list the specific lines for clarity.
thinking
**Identifying findings and weaknesses**

Okay, I'm reflecting on whether "every finding" should be included. The user wants a thorough exploration, but I'm unsure if we need all findings given the many other important issues at stake. 

Since the user explicitly asked for an exhaustive analysis, I think providing around 12-15 robust findings is a reasonable target. I’ll highlight key issues, such as the misuse of parentheses, dead compatibility labels, and hedged statuses. It seems important to balance completeness with clarity for the user.
thinking
**Considering LaTeX adjustments**

I could suggest removing lines 1257-1270 completely since the next section title already sets the context. But the user asked for a specific fix, so an option is to say, "Delete lines 1257-1270 entirely." However, I'd miss mentioning that the physical content belongs to Volume II. Instead, I could propose something like, "Holomorphic-topological boundary theories enter the present chapter only through the bar-side BV package; their physical construction belongs to Volume II, so I’ll continue with the configuration-space operator \Delta." That feels more complete!
thinking
**Refining the signpost**

I’m thinking about how to effectively highlight the transition, possibly saying, "...so the next section isolates the bar-side BV structure from configuration-space geometry." That feels clearer! Now, for lines 1333-1337, I want to ensure I communicate the fix accurately. I could suggest to simply replace those lines with: "The chapter does not prove a BV/bar quantum master equation." That keeps it straightforward and addresses the user’s request directly. I’m feeling good about this!
collab close_agent(call_b2S7BHcDfEoTwMZU9eD5eqUp)
  receiver: 019d83fe-8d66-70e2-8e9a-dbe01560b35b
close_agent(call_b2S7BHcDfEoTwMZU9eD5eqUp) completed: "- `rem:w-semi-infinite-conditional` (defined `chapters/connections/bv_brst.tex:1248`) is *not* referenced by any other `…":
  receiver: 019d83fe-8d66-70e2-8e9a-dbe01560b35b
collab close_agent(call_qddgWMBuv1EI3BQXo3JAyYvg)
  receiver: 019d83fe-8d6b-7281-bf56-6a2f62e315b3
close_agent(call_qddgWMBuv1EI3BQXo3JAyYvg) completed: "- **AI-slop vocabulary**: none of the classic trigger words (e.g., *notably*, *crucially*, *obviously*) appear in this c…":
  receiver: 019d83fe-8d6b-7281-bf56-6a2f62e315b3





thinking
**Organizing the revisions**

I need to focus on whether there's really only one instance of line 44, even though the problem mentions it's repeated. For item 2, I should fix the stub section and the dead compatibility labels, removing them and adding a bridge sentence instead. I'll also rewrite items with hedged language to make them more direct and explicit, like for the heuristic phrasing. Lastly, I need to revise the QME remark and BV quantization remark for accuracy and clarity.
thinking
**Reviewing document issues**

I need to check line 782 for an introductory display. There's a potential stray space at line 2182. I see a possible issue at line 1119, where "Master Table, revisited" references `Table\ref{tab:master-invariants}` and uses `\kappa` and `F_g` without a family, which might not be right. At line 1434, the path headings with `\noindent\textbf{Path \textup{(a)}: ...}` might be okay. Also, line 1404 mentions "the free-field case," which could be good.
thinking
**Drafting concise solutions**

I think I shouldn’t overcomplicate things, especially if there aren’t any findings to share. I need to make sure the wording is minimal and direct. Keeping each bullet in the same format will help maintain clarity. I’ll focus on drafting each point by clearly stating the problem and then offering a concise fix for it. This should make everything easier to digest for the user!
thinking
**Organizing findings by severity**

I'm thinking I should order the findings by severity: high, medium, and low. For high severity, I've got 44 systemic parentheses and 1,257 dead section labels. Medium severity includes items like 30, 314, and 860 bare kappa. The low severity category features things like redundancy, theorem spacing, and extra space. Hm, also considering if the line 44 might be medium. I want to mention that there was no AI slop or specific markdown issues. The summary could say, “Checked: 2339 | Findings: 13 | Verdict: FAIL,” but I need to decide if it’s 13 or 14 findings.
thinking
**Counting findings and organizing details**

I'm adding together findings: 223, 182, 782, 2154, 2182, and 283. It looks like that gives me 14 findings. I’m considering whether I actually need the “HIGH” severity—there are only 2 high, 6 medium, and 6 low. I might want each bullet pointed out on a single line to keep things tidy, aiming for under 70 lines total. The line references need to be exact, and I should mention the repeated cluster on line 44 without overquoting more than 25 words from the source.
codex
- [HIGH] `chapters/connections/bv_brst.tex:44` — PROBLEM: the file repeatedly wraps ordinary parentheses as `\textup{(}...\textup{)}`; this is typographically noisy and recurs across the chapter (`44, 49, 81-82, 108, 137, 265, 322, 492-494, 643-651, 692-721, 745-848, 930, 1039-1065, 1173-1225, 1349-1396, 1470-1505, 1537-1647, 1661-1711, 1849-1865, 2051-2169, 2200-2317`). FIX: replace every such wrapper with plain text parentheses; e.g. line 44 should read `(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).`, line 1470 should read `\emph{Step~1 (Quillen anomaly).}`, and line 1864 should read `harmonic decoupling (Remark~\ref{rem:bv-bar-class-c-proof}) \\`.
- [HIGH] `chapters/connections/bv_brst.tex:1257` — PROBLEM: `\section{Holomorphic-topological field theories}` is a stub that only punts content to Volume II, and lines `1266-1270` leave four “cross-reference compatibility” labels that are not referenced by any real source file in the repo. FIX: delete lines `1257-1270` and replace them with a single bridge sentence before `\section{The BV algebra structure}`: `Holomorphic-topological boundary theories enter this chapter only through the bar-side BV package; their physical construction belongs to Volume~II, so the next section isolates the configuration-space BV structure.`
- [MEDIUM] `chapters/connections/bv_brst.tex:30` — PROBLEM: `are expected to behave better` hedges a status boundary instead of stating what is proved and what is still only candidate behavior. FIX: replace lines `30-34` with `What this chapter proves is narrower: the genus-$0$ BV/bar comparison and the all-genera scalar Heisenberg identity. The obstruction analysis isolates the unresolved locus: class~$\mathsf{M}$ carries the higher-genus harmonic discrepancy, while classes~$\mathsf{G}$, $\mathsf{L}$, and~$\mathsf{C}$ remain candidate extensions rather than proved chain-level comparisons.`
- [MEDIUM] `chapters/connections/bv_brst.tex:314` — PROBLEM: `expected physics reading` is passive hedging inside a remark that already knows it is heuristic. FIX: replace lines `314-317` with `This displayed pairing is a heuristic physics interpretation of the configuration-space forms. The chapter does not prove an identification between the physical integration pairing and the Euler characteristic of the genus-$0$ bar complex.`
- [MEDIUM] `chapters/connections/bv_brst.tex:860` — PROBLEM: `The chain map \Phi should extend` states an unproved target as a modal wish instead of an open construction problem. FIX: replace lines `860-864` with `The higher-genus target is a genus-graded extension of $\Phi$ whose genus-$g$ component incorporates Costello's counterterm expansion. This chapter does not construct that map; it records the problem as Programme~VI-a in \S\ref{sec:modular-koszul-programme}.`
- [MEDIUM] `chapters/connections/bv_brst.tex:1333` — PROBLEM: `should be solved by the bar-cobar pairing` hedges instead of marking the statement as conjectural. FIX: replace lines `1333-1337` with `The chapter does not prove a BV/bar quantum master equation. A natural conjectural target is that the bar-cobar pairing produce a solution of \[\hbar \Delta S + \tfrac12\{S,S\}=0,\] equivalently $\Delta e^{S/\hbar}=0$.`
- [MEDIUM] `chapters/connections/bv_brst.tex:1342` — PROBLEM: `should be equivalent` presents a non-proved comparison without explicit conjectural notation. FIX: replace lines `1342-1345` with `A conjectural comparison would identify the BV quantization of a chiral algebra $\mathcal{A}$ with a bar-side homology theory: \[H^*_{\mathrm{BV}}(\mathcal{A}) \stackrel{?}{\cong} H^*(\bar B(\mathcal{A}), \Omega(\mathcal{A}^!)).\] Here $\mathcal{A}^!$ denotes the Koszul dual.`
- [MEDIUM] `chapters/connections/bv_brst.tex:613` — PROBLEM: notation drifts from family-specific `\kappa(\cdot)` to bare `\kappa` in generic prose (`613, 993, 1096-1105, 1119, 2021`), so the reader cannot tell whether `\kappa` means a level, an anomaly coefficient, or a curvature scalar. FIX: restore the object in every generic occurrence: line 613 `\dfib^{\,2} = \kappa(\cA)\cdot\omega_1` and `\kappa(\cA)=0`; line 993 `m_0 = \kappa(\widehat{\fg}_k)\cdot\mathbf{1}`; lines `1096-1105` `\kappa(\widehat{\fg}_k)=\frac{(k+h^\vee)\dim\fg}{2h^\vee}` and `negates \kappa(\widehat{\fg}_k)`; line 1119 `\kappa(\widehat{\fg}_k)` is the semi-infinite anomaly coefficient; line 2021 `d_{\mathrm{BV}}^2 = \kappa(\cA)\cdot\omega_g`.
- [LOW] `chapters/connections/bv_brst.tex:283` — PROBLEM: lines `283-286` merely restate lines `271-281` without adding new content. FIX: delete lines `283-286` entirely.
- [LOW] `chapters/connections/bv_brst.tex:223` — PROBLEM: theorem-part references are typeset awkwardly as `Theorem~\ref{...}(3)` and similarly at `1051, 1055`; this reads badly and trips TeX hygiene checks. FIX: change line 223 to `Theorem~\ref{thm:FM}, item~(3):`, line 1051 to `Theorem~\ref{thm:genus-universality}(i) equals`, and line 1055 to `Theorem~\ref{thm:genus-universality}(ii) is the`.
- [LOW] `chapters/connections/bv_brst.tex:182` — PROBLEM: theorem/lemma headings at `182, 354, 463` omit the non-breaking space before citations. FIX: change them to `\ClaimStatusProvedElsewhere{}~\cite{CG17}` at lines 182 and 354, and `\ClaimStatusProvedElsewhere{}~\cite{FGZ86}` at line 463.
- [LOW] `chapters/connections/bv_brst.tex:782` — PROBLEM: the sentence runs directly into a display with `... + 1)$ \[`; the display opening is malformed stylistically. FIX: replace lines `781-789` with `$\beta\gamma$ system sits at $\lambda = 3/2$. Using \[\n c_{\beta\gamma}\!\left(\tfrac{3}{2}\right)=2\bigl(6\cdot\tfrac{9}{4}-6\cdot\tfrac{3}{2}+1\bigr)=11,\n\]`.
- [LOW] `chapters/connections/bv_brst.tex:2154` — PROBLEM: the conjecture still uses weak modal prose (`should match`, `is expected to be`) at `2154-2156` and `2165-2169`. FIX: replace lines `2154-2156` with `$\kappa(\mathrm{dP}_k)=k+1$. The characteristic-lattice count therefore predicts the endpoint values $\kappa(\mathbb{P}^2)=1$ and $\kappa(\mathrm{dP}_8)=9$.` Replace lines `2165-2169` with `The conjecture further asserts that the shadow class is $\mathsf{C}$ on the generic locus (four-pair $\beta\gamma$ structure) and degenerates to $\mathsf{M}$ along the stress-tensor line, in direct analogy with the Burns space (Remark~\ref{rem:burns-shadow-class}).`
- [LOW] `chapters/connections/bv_brst.tex:2182` — PROBLEM: there is a stray space before the period in `Theorem~D .`. FIX: change it to `Theorem~D.`

## Summary
Checked: 2339 | Findings: 14 | Verdict: FAIL
tokens used
143,590
