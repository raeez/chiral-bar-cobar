# AP13_hardcoded_part (484s, gpt-5.4)

- [HIGH] [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5970) — hardcoded cross-volume part reference: `Volume~II, Part~VI`.
- [HIGH] [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7549) — hardcoded part reference: `Part~VII`.
- [HIGH] [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7752) — hardcoded cross-volume part reference: `Volume~II, Part~VII`.
- [HIGH] [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3796) — hardcoded cross-volume part reference: `Volume~II's Part~VII`.
- [HIGH] [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1788) — hardcoded cross-volume part reference: `Vol~II, Part~IV`.
- [HIGH] [thqg_introduction_supplement_body.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1620) — hardcoded frontier part in a list otherwise using `Part~\ref{...}`: `(Part~VII)`.
- [HIGH] [thqg_preface_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2017) — mixed compliant/hardcoded range: `Parts~\ref{part:seven-faces}--VII`.
- [HIGH] [thqg_preface_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2055) — hardcoded part reference: `Part~VII pushes`.
- [HIGH] [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:987) — hardcoded part in section title: `The Part~VII frontier chapters`.
- [HIGH] [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:990) — hardcoded part references in prose: `Part~VII extends the proved core of Parts~I--VI`.
- [HIGH] [dnp_identification_master.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:540) — sibling chapter-reference defect found in context scan: literal label name `Chapter~\texttt{ch:genus1-seven-faces}` instead of a chapter `\ref`.
- [HIGH] [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34) — hardcoded cross-volume part reference: `Volume~II, Part~III`.
- [HIGH] [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:157) — hardcoded cross-volume part reference: `Volume~I, Part~II`.
- [HIGH] [braided_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:89) — hardcoded cross-volume chapter reference: `Volume~II, Chapter~11`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:922) — hardcoded cross-volume part references: `Vol~I Part~III and Vol~II Part~III`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:931) — hardcoded cross-volume part reference: `Vol~I, Part~III`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:936) — hardcoded cross-volume part reference: `Vol~II, Part~III`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1006) — sibling chapter-reference defect found in context scan: literal label name `Chapter~\texttt{ch:genus1-seven-faces}`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1009) — hardcoded local part reference: `Part~V`.
- [HIGH] [k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:966) — hardcoded chapter number in cross-volume reference: `Chapter~66`.
- [HIGH] [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94) — hardcoded cross-volume part reference: `Vol~I, Part~I`.
- [HIGH] [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5492) — hardcoded chapter number in cross-volume reference: `Chapter~66`.
- [HIGH] [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342) — hardcoded cross-volume part reference: `Volume~II, Part~III`.
- [HIGH] [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:546) — hardcoded cross-volume part reference: `Volume~I, Part~II`.

Excluded as false positives after context read: external bibliography chapter citations such as `\cite[Chapter~3]{BD04}` and non-live `.bak` artifact files under `chapters/`.

## Summary
Instances checked: 76 | Violations found: 24 | Verdict: FAIL


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
session id: 019d83aa-aad1-7253-aff6-4a5540f1a356
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: Sweep for FM10/B33: hardcoded Part numbers across all three volumes.

Run: grep -rn 'Part~[IVXL]\|Chapter~[0-9]' chapters/ | head -30

Expected: Use \ref{part:...}

For EACH hit:
1. Read surrounding context to determine if it's a genuine violation
2. Distinguish false positives from real violations
3. Report file:line and the exact violating text
4. Assess severity (CRITICAL if mathematical, HIGH if structural, MEDIUM if prose)
mcp startup: no servers
codex
Using `deep-beilinson-audit` for this sweep because the task is an adversarial repository audit with verification and false-positive control. I’ll start by reading that skill briefly, then run the requested search and inspect each hit in context before reporting only genuine violations.
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

Plan update
Adversarial sweep for FM10/B33 across all three volumes, with context reads, per-hit verification, false-positive filtering, and downstream propagation checks.
  → Load the required audit context files and confirm the target pattern/rule for hardcoded Part or Chapter references
  • Run the requested search on each volume and collect candidate hits
  • Read surrounding context for every candidate, classify genuine violations vs false positives, and check for drift across duplicate surfaces
  • Re-verify surviving findings and produce the severity-ordered report with counts and verdict
codex
I’ve loaded the audit skill. Next I’m grounding the rule from the repo’s canonical surfaces so the sweep is judged against local policy rather than memory.
exec
/bin/zsh -lc "rg -n \"B33|FM10|hardcoded Part|Chapter~\\\\[0-9]|Part~\\\\[IVXL]|use \\\\ref\\{part:\" metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"B33|FM10|hardcoded Part|Chapter~\\\\[0-9]|Part~\\\\[IVXL]|use \\\\ref\\{part:\" CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"B33|FM10|hardcoded Part|Chapter~\\\\[0-9]|Part~\\\\[IVXL]|use \\\\ref\\{part:\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"B33|FM10|hardcoded Part|Chapter~\\\\[0-9]|Part~\\\\[IVXL]|use \\\\ref\\{part:\" archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
339:- B33. `Part~IV`, `Chapter~12` hardcoded. CORRECT: `\ref{part:...}`. V2-AP26/FM10.
418:**FM10. Hardcoded part number drift (`Part~IV` vs `\ref{part:...}`).** Cross-volume references as hardcoded roman numerals break silently on reorganisation. Counter: after any Edit, grep `Part~[IVX]+|Chapter~[0-9]+` in the file and replace with `\ref{part:...}`.
 exited 1 in 51ms:

 exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '330,425p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
- B27. `A \iff B` in theorem where only forward proved. CORRECT: `\implies` + Remark on converse. AP36.
- B28. "k=0 r-matrix vanishes and algebra fails Koszulness" for affine KM. CORRECT: k=0 is abelian limit, still Koszul; k=-h^v is critical, Koszulness fails. FM4.
- B29. Theorem C^{E1} with `n` free on RHS but only `g` on LHS. CORRECT: fully quantify n with `2g-2+n > 0`. AP139.

**macros / labels / LaTeX**

- B30. `\end{definition>` (> instead of }). Regex: `\\end\{[^}]*>`. FM7.
- B31. `\begin{theorem>`. Symmetric.
- B32. `\cW` in standalone without `\providecommand`. FM6.
- B33. `Part~IV`, `Chapter~12` hardcoded. CORRECT: `\ref{part:...}`. V2-AP26/FM10.
- B34. Duplicate `conj:kappa-bps-universality` across Vol I and Vol III. AP124/FM15.
- B35. `\begin{conjecture} \label{thm:foo}` prefix mismatch. AP125/FM14.
- B36. `\cite{GeK98}` without bibitem. Emits [?]. AP28.

**numerical coefficients**

- B37. `F_2 = 1/5760` or `7/2880`. CORRECT: `7/5760`. FM21.
- B38. `\frac{1}{2\pi}\oint` (missing i). CORRECT: `\frac{1}{2\pi i}\oint`. AP120.
- B39. KM r-matrix not vanishing at k=0. AP126/AP141.



thinking
**Planning grep command execution**

I need to run the grep command across three volumes as the user specified. The command is `grep -rn ... chapters/ | head -30`, which means I want to check the first 30 hits. Since I’ll sweep all volumes, I should use the command in each directory. I might need to use `multi_tool_use.parallel` to speed things up. If there are more than 30 hits overall, I can consider running without `head`. Let's proceed step by step!
thinking
**Executing grep command**

I need to use grep, and I want to run the exact command across each volume. This ensures I'm checking everything thoroughly. By doing this, I can ensure I cover all the bases and find any relevant hits. I’ll treat each volume individually to make sure nothing is missed. It's all about being methodical here! Let’s get started and see what the results reveal!
codex
The rule is confirmed locally: `CLAUDE.md` flags `Part~IV` / `Chapter~12` hardcoding as `B33` / `FM10`, with the canonical replacement `\ref{part:...}`. I’m running the exact sweep on all three `chapters/` trees now, then I’ll read every candidate in context.
exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/ | head -30" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/theory/quantum_groups_foundations.tex:84:Drinfeld, ``Quantum groups'' (ICM Berkeley 1986), Theorem~2; see also Chari--Pressley, \emph{A Guide to Quantum Groups}, Chapter~4.2. The proof is a direct consequence of quasi-triangularity and the coassociativity of $\Delta$.
chapters/theory/introduction.tex:34: \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
chapters/theory/introduction.tex:157:(Volume~I, Part~II) organizes the resulting landscape:
chapters/theory/braided_factorization.tex:89:fewer pole order than the OPE). See Volume~II, Chapter~11 for the
chapters/connections/cy_holographic_datum_master.tex:922:This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
chapters/connections/cy_holographic_datum_master.tex:931:\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
chapters/connections/cy_holographic_datum_master.tex:936:\item \emph{Vol~II, Part~III:} the binary collision residue of a
chapters/connections/cy_holographic_datum_master.tex:1009:Vol~III. Subsequent chapters in Part~V record the geometric Langlands
chapters/examples/k3_times_e.tex:966:of Chapter~66) and apply to the $K3 \times E$ tower.
chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
chapters/examples/toroidal_elliptic.tex:5492:of Chapter~66) and apply to the $K3 \times E$ tower.
chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~III), the BPS algebra
chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~II) acquires categorical meaning through the
exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/ | head -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/ | head -30" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/theory/locality.tex:284:Costello--Gwilliam~\cite[Chapter~5, \S5.4]{CG17} prove that a
chapters/theory/foundations_recast_draft.tex:721:\cite{BD04}, Chapter~3.
chapters/theory/foundations_recast_draft.tex:732:Chapter~4).
chapters/theory/raviolo.tex:498:\emph{Absolute convergence.} Item~(b) asserts one-loop finiteness: all one-loop Feynman integrals converge in the HT gauge. For theories with $d' = 1$ topological direction, the power-counting of~\cite{GRW21} shows that this implies finiteness at \emph{all} loop orders: the superficial degree of divergence of an $L$-loop graph is $\delta = (1 - d')L = 0$ for $L = 0$ and $\delta < 0$ for $L \ge 2$, so the only potential divergences are at one loop, and these are finite by hypothesis. This power-counting bound applies to theories with propagator of type $(0,1)$ in the holomorphic direction and distributional in the topological direction. For such theories, the loop superficial degree of divergence is $\delta = (1-d')L$ where $d' = \dim_\C$ of the holomorphic factor; at $d' = 1$ this gives $\delta = 0$ for all $L$, so only logarithmic divergences can appear and these are removed by the one-loop renormalization hypothesis. See \cite[Chapter~9]{CG17} and \cite[Theorem~3.1]{GRW21} for the precise class of theories. After FM compactification of the holomorphic factor, the integrand acquires at worst logarithmic singularities along boundary divisors. Concretely:
chapters/theory/factorization_swiss_cheese.tex:2148:Lurie \cite{HA}, Chapter~5.5, with two strata: the open stratum
chapters/connections/relative_feynman_transform.tex:846:\cite{LV12}, Chapter~13.
chapters/connections/relative_feynman_transform.tex:1452:(Chriss--Ginzburg~\cite{CG97}, Chapter~8): the convolution
chapters/connections/spectral-braiding.tex:969:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
chapters/connections/conclusion.tex:987:\subsection{The Part~VII frontier chapters}
chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
chapters/connections/bar-cobar-review.tex:465:The convolution dg Lie algebra $\mathrm{Conv}(\cC, \cA)$ arises in two equivalent ways: (i)~when $\cC = \barB(\cA)$ is the bar construction, the cooperad structure on $\barB(\cA)$ and the operad structure on $\mathrm{End}_\cA$ give an $L_\infty$-algebra via the operadic convolution of \cite{LV12}, Chapter~6; (ii)~for a general conilpotent coalgebra $\cC$ and algebra $\cA$, the associative convolution product $f \star g = \mu_\cA \circ (f \otimes g) \circ \Delta_\cC$ on $\mathrm{Hom}(\cC, \cA)$ yields a dg Lie algebra by taking graded commutators. When $\cC = \barB(\cA)$, the two constructions agree because the cooperad structure on $\barB(\cA)$ is determined by the coalgebra structure via the cofree property. In the representability theorems above, we use convention~(ii) for general $\cC$ and convention~(i) when $\cC = \barB(\cA)$.
chapters/connections/ordered_associative_chiral_kd_frontier.tex:83:In Chriss--Ginzburg \cite{chriss-ginzburg} Chapter~3, the orbit stratification
chapters/connections/hochschild.tex:913:\cite[Chapter~6]{CG17}:
chapters/connections/hochschild.tex:1079:theorem~\cite[Chapter~6]{CG17}, a locally constant factorization
chapters/connections/spectral-braiding-core.tex:3469:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
 succeeded in 187ms:
chapters/theory/higher_genus_complementarity.tex:582:Beilinson--Drinfeld~\cite[Chapter~4]{BD04} proved the $g=0$ case;
chapters/theory/higher_genus_complementarity.tex:2154:Costello--Gwilliam~\cite{CG17}, Volume~2, Chapter~5).
chapters/theory/ordered_associative_chiral_kd.tex:5970:hierarchy of Volume~II, Part~VI\@. The correspondence is:
chapters/theory/ordered_associative_chiral_kd.tex:7549:of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
chapters/theory/ordered_associative_chiral_kd.tex:7752:non-formality (Volume~II, Part~VII).
chapters/theory/configuration_spaces.tex:1212:the Beilinson--Drinfeld framework \cite[Chapter~3]{BD04}.
chapters/theory/configuration_spaces.tex:3525:% (see Beilinson--Drinfeld~\cite[Chapter~3]{BD04}).
chapters/theory/configuration_spaces.tex:4838:chiral/Ran-space correspondence is developed in \cite[Chapter~3]{BD04}; the
chapters/theory/configuration_spaces.tex:4857:formalism \cite[Chapter~3]{BD04} together with factorization-homology
chapters/theory/algebraic_foundations.tex:1293:\textup{(Beilinson--Drinfeld \cite[Chapter~3]{BD04})}
chapters/theory/koszul_pair_structure.tex:441:\emph{Step 4}: By Stokes' theorem, $\int_{\overline{C}_n} d(\cdots) = \int_{\partial\overline{C}_n}(\cdots)$. Each codimension-$1$ boundary stratum $\overline{C}_i \times \overline{C}_j$ (with $i + j = n + 1$) contributes a composition $m_i \circ_k m_j$ (with $k$ indexing the insertion point). The sign $(-1)^{rs+t}$ in the $A_\infty$ relation arises from the Koszul sign rule applied to the desuspended generators $s^{-1}f_i$: the desuspended map $b_s$ has degree~$+1$, so permuting $s^{-1}f_1, \ldots, s^{-1}f_r$ past $b_s$ contributes $(-1)^r$; inserting $b_s$ into position $(r{+}1)$ among the desuspended outputs and accounting for the $s$ inputs with their signs gives the total sign $(-1)^{rs+t}$ (see~\cite{LV12}, \S9.2.8 for the complete sign derivation). The sum over all boundary strata exhausts all compositions, and $\partial^2 = 0$ on $\overline{C}_n$ ensures the total contribution vanishes. See~\cite{LV12}, Chapter~9 for the complete operadic argument. \qedhere
chapters/theory/bar_construction.tex:1972:(Reutenauer \cite[Chapter~9]{Reutenauer93};
chapters/theory/hochschild_cohomology.tex:433:This identification is classical for associative algebras \cite{Loday98}; the chiral extension follows from the factorization structure of the loop space \cite[Chapter~5]{CG17}.
chapters/theory/hochschild_cohomology.tex:1128:Costello--Gwilliam~\cite[Chapter~5]{CG17}.
chapters/theory/hochschild_cohomology.tex:1454:parallel result appears in Costello--Gwilliam~\cite[Chapter~5]{CG17}.
chapters/theory/cobar_construction.tex:347:$\mathcal{D}$-modules \cite[Chapter~4]{KS90}.
chapters/theory/cobar_construction.tex:1374:At the level of $\mathcal{D}$-modules on $\overline{C}_n(X)$, the bar and cobar differentials are flat connections (the bar complex is a complex of holonomic $\mathcal{D}$-modules by Lemma~\ref{lem:bar-holonomicity}). Verdier duality is an exact contravariant involution on $D^b_{\mathrm{hol}}(\mathcal{D}_{\overline{C}_n(X)})$ that sends a flat connection $\nabla$ to the adjoint connection $\nabla^\dagger$ (see~\cite{KS90}, Chapter~4).
chapters/theory/introduction.tex.bak:1083:flat finite-type completed-dual loci singled out later in Part~I.
chapters/theory/introduction.tex.bak:1282:the outlook (Part~VI, Chapter~\ref{chap:concordance}) records
chapters/theory/introduction.tex.bak:1465:\multicolumn{2}{@{}l}{\textbf{Part~I: The Bar Complex} \emph{(proved core; Thms A--D+H)}} \\[3pt]





thinking
**Evaluating candidate hits**

I need to assess candidate hits; many look like bibliography citations or references that might not be valid. The user has hardcoded part numbers and chapter numbers in multiple volumes. There's a concern that hardcoded references can cause issues when reorganizing the content. I think I'll have to inspect each hit to determine if they’re legitimate internal references or false positives. I suppose only internal hardcoded references should be counted as violations, but questions remain about using labels across volumes.
thinking
**Assessing chapter references**

I need to determine if "Volume II, Chapter 11" is a hardcoded reference within another volume, which could be a violation. I think "Volume II, Part III" might also be hardcoded. There are mentions of local parts in "Part VII frontier chapters," and I need to evaluate their severity. The user asked for a command with head -30, but I wonder if I should check all hits since there could be 54 total. I’ll need to read the context around each candidate hit to get clarity.
thinking
**Classifying citation hits**

I could categorize obvious false positives without delving into the wider context if the hit is a clear citation, like `\cite[Chapter4]{BD04}`, since that indicates an external reference. However, the user stressed the importance of reading surrounding context to assess genuine violations. I might need to use a script to gather the context for each hit effectively. I should particularly focus on lines with hardcoded references like "Volume II, Part VI," while noting that some chapter numbers with external citations might be false positives. Should I only report genuine violations?
thinking
**Revisiting command counts**

I’m checking the task requirements and wondering if I should count all hits, focusing on genuine entries. The mission directs me to sweep for FM10/B33 part numbers across all volumes, and I wonder if there are more than 30 in Volume I. If yes, I need to check beyond the initial 30 hits. Although the user asked for a command with head -30, I think I must verify the total count for a complete resolution.
thinking
**Analyzing grep command instructions**

The user specifies "Run: grep -rn ... chapters/ | head -30," which might be to sample the output. However, the phrase "For EACH hit" suggests I should inspect every returned line. To ensure completeness, I think I should follow the user's command precisely while also checking for additional candidate hits beyond the first 30. The completeness contract indicates I shouldn't stop early, so I might also count total hits using grep -rn without head and categorize them per volume.
codex
The first pass returns many citation-style `Chapter~...` matches, which are likely false positives. I’m counting the full candidate surface now so the audit doesn’t silently stop at the first 30-line window.
exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/ | wc -l" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
      13
exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/ | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/ | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 89ms:
      15
 succeeded in 275ms:
      45

thinking
**Evaluating search results**

I see I have 73 hits to inspect, which seems quite overwhelming. However, I realize that many might be false positives that could be classified using simple patterns. I should separate Part hits from Chapter hits since all Part hits could be genuine internal references, while Chapter hits are often citations. It sounds like listing all lines and using grep on each volume would help. Following the user’s instructions, I’ll carefully examine the context around candidates that aren’t clearly external. Let's find a balanced approach that doesn’t take too much time.
exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
chapters/theory/quantum_groups_foundations.tex:84:Drinfeld, ``Quantum groups'' (ICM Berkeley 1986), Theorem~2; see also Chari--Pressley, \emph{A Guide to Quantum Groups}, Chapter~4.2. The proof is a direct consequence of quasi-triangularity and the coassociativity of $\Delta$.
chapters/theory/introduction.tex:34: \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
chapters/theory/introduction.tex:157:(Volume~I, Part~II) organizes the resulting landscape:
chapters/theory/braided_factorization.tex:89:fewer pole order than the OPE). See Volume~II, Chapter~11 for the
chapters/connections/cy_holographic_datum_master.tex:922:This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
chapters/connections/cy_holographic_datum_master.tex:931:\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
chapters/connections/cy_holographic_datum_master.tex:936:\item \emph{Vol~II, Part~III:} the binary collision residue of a
chapters/connections/cy_holographic_datum_master.tex:1009:Vol~III. Subsequent chapters in Part~V record the geometric Langlands
chapters/examples/k3_times_e.tex:966:of Chapter~66) and apply to the $K3 \times E$ tower.
chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
chapters/examples/toroidal_elliptic.tex:5492:of Chapter~66) and apply to the $K3 \times E$ tower.
chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~III), the BPS algebra
chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~II) acquires categorical meaning through the
exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 71ms:
chapters/theory/locality.tex:284:Costello--Gwilliam~\cite[Chapter~5, \S5.4]{CG17} prove that a
chapters/theory/foundations_recast_draft.tex:721:\cite{BD04}, Chapter~3.
chapters/theory/foundations_recast_draft.tex:732:Chapter~4).
chapters/theory/raviolo.tex:498:\emph{Absolute convergence.} Item~(b) asserts one-loop finiteness: all one-loop Feynman integrals converge in the HT gauge. For theories with $d' = 1$ topological direction, the power-counting of~\cite{GRW21} shows that this implies finiteness at \emph{all} loop orders: the superficial degree of divergence of an $L$-loop graph is $\delta = (1 - d')L = 0$ for $L = 0$ and $\delta < 0$ for $L \ge 2$, so the only potential divergences are at one loop, and these are finite by hypothesis. This power-counting bound applies to theories with propagator of type $(0,1)$ in the holomorphic direction and distributional in the topological direction. For such theories, the loop superficial degree of divergence is $\delta = (1-d')L$ where $d' = \dim_\C$ of the holomorphic factor; at $d' = 1$ this gives $\delta = 0$ for all $L$, so only logarithmic divergences can appear and these are removed by the one-loop renormalization hypothesis. See \cite[Chapter~9]{CG17} and \cite[Theorem~3.1]{GRW21} for the precise class of theories. After FM compactification of the holomorphic factor, the integrand acquires at worst logarithmic singularities along boundary divisors. Concretely:
chapters/theory/factorization_swiss_cheese.tex:2148:Lurie \cite{HA}, Chapter~5.5, with two strata: the open stratum
chapters/connections/relative_feynman_transform.tex:846:\cite{LV12}, Chapter~13.
chapters/connections/relative_feynman_transform.tex:1452:(Chriss--Ginzburg~\cite{CG97}, Chapter~8): the convolution
chapters/connections/spectral-braiding.tex:969:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
chapters/connections/conclusion.tex:987:\subsection{The Part~VII frontier chapters}
chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
chapters/connections/bar-cobar-review.tex:465:The convolution dg Lie algebra $\mathrm{Conv}(\cC, \cA)$ arises in two equivalent ways: (i)~when $\cC = \barB(\cA)$ is the bar construction, the cooperad structure on $\barB(\cA)$ and the operad structure on $\mathrm{End}_\cA$ give an $L_\infty$-algebra via the operadic convolution of \cite{LV12}, Chapter~6; (ii)~for a general conilpotent coalgebra $\cC$ and algebra $\cA$, the associative convolution product $f \star g = \mu_\cA \circ (f \otimes g) \circ \Delta_\cC$ on $\mathrm{Hom}(\cC, \cA)$ yields a dg Lie algebra by taking graded commutators. When $\cC = \barB(\cA)$, the two constructions agree because the cooperad structure on $\barB(\cA)$ is determined by the coalgebra structure via the cofree property. In the representability theorems above, we use convention~(ii) for general $\cC$ and convention~(i) when $\cC = \barB(\cA)$.
chapters/connections/ordered_associative_chiral_kd_frontier.tex:83:In Chriss--Ginzburg \cite{chriss-ginzburg} Chapter~3, the orbit stratification
chapters/connections/hochschild.tex:913:\cite[Chapter~6]{CG17}:
chapters/connections/hochschild.tex:1079:theorem~\cite[Chapter~6]{CG17}, a locally constant factorization
chapters/connections/spectral-braiding-core.tex:3469:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
 succeeded in 302ms:
chapters/theory/higher_genus_complementarity.tex:582:Beilinson--Drinfeld~\cite[Chapter~4]{BD04} proved the $g=0$ case;
chapters/theory/higher_genus_complementarity.tex:2162:Costello--Gwilliam~\cite{CG17}, Volume~2, Chapter~5).
chapters/theory/ordered_associative_chiral_kd.tex:5970:hierarchy of Volume~II, Part~VI\@. The correspondence is:
chapters/theory/ordered_associative_chiral_kd.tex:7549:of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
chapters/theory/ordered_associative_chiral_kd.tex:7752:non-formality (Volume~II, Part~VII).
chapters/theory/configuration_spaces.tex:1212:the Beilinson--Drinfeld framework \cite[Chapter~3]{BD04}.
chapters/theory/configuration_spaces.tex:3525:% (see Beilinson--Drinfeld~\cite[Chapter~3]{BD04}).
chapters/theory/configuration_spaces.tex:4838:chiral/Ran-space correspondence is developed in \cite[Chapter~3]{BD04}; the
chapters/theory/configuration_spaces.tex:4857:formalism \cite[Chapter~3]{BD04} together with factorization-homology
chapters/theory/algebraic_foundations.tex:1293:\textup{(Beilinson--Drinfeld \cite[Chapter~3]{BD04})}
chapters/theory/koszul_pair_structure.tex:441:\emph{Step 4}: By Stokes' theorem, $\int_{\overline{C}_n} d(\cdots) = \int_{\partial\overline{C}_n}(\cdots)$. Each codimension-$1$ boundary stratum $\overline{C}_i \times \overline{C}_j$ (with $i + j = n + 1$) contributes a composition $m_i \circ_k m_j$ (with $k$ indexing the insertion point). The sign $(-1)^{rs+t}$ in the $A_\infty$ relation arises from the Koszul sign rule applied to the desuspended generators $s^{-1}f_i$: the desuspended map $b_s$ has degree~$+1$, so permuting $s^{-1}f_1, \ldots, s^{-1}f_r$ past $b_s$ contributes $(-1)^r$; inserting $b_s$ into position $(r{+}1)$ among the desuspended outputs and accounting for the $s$ inputs with their signs gives the total sign $(-1)^{rs+t}$ (see~\cite{LV12}, \S9.2.8 for the complete sign derivation). The sum over all boundary strata exhausts all compositions, and $\partial^2 = 0$ on $\overline{C}_n$ ensures the total contribution vanishes. See~\cite{LV12}, Chapter~9 for the complete operadic argument. \qedhere
chapters/theory/bar_construction.tex:1972:(Reutenauer \cite[Chapter~9]{Reutenauer93};
chapters/theory/hochschild_cohomology.tex:433:This identification is classical for associative algebras \cite{Loday98}; the chiral extension follows from the factorization structure of the loop space \cite[Chapter~5]{CG17}.
chapters/theory/hochschild_cohomology.tex:1128:Costello--Gwilliam~\cite[Chapter~5]{CG17}.
chapters/theory/hochschild_cohomology.tex:1454:parallel result appears in Costello--Gwilliam~\cite[Chapter~5]{CG17}.
chapters/theory/cobar_construction.tex:347:$\mathcal{D}$-modules \cite[Chapter~4]{KS90}.
chapters/theory/cobar_construction.tex:1374:At the level of $\mathcal{D}$-modules on $\overline{C}_n(X)$, the bar and cobar differentials are flat connections (the bar complex is a complex of holonomic $\mathcal{D}$-modules by Lemma~\ref{lem:bar-holonomicity}). Verdier duality is an exact contravariant involution on $D^b_{\mathrm{hol}}(\mathcal{D}_{\overline{C}_n(X)})$ that sends a flat connection $\nabla$ to the adjoint connection $\nabla^\dagger$ (see~\cite{KS90}, Chapter~4).
chapters/theory/introduction.tex.bak:1083:flat finite-type completed-dual loci singled out later in Part~I.
chapters/theory/introduction.tex.bak:1282:the outlook (Part~VI, Chapter~\ref{chap:concordance}) records
chapters/theory/introduction.tex.bak:1465:\multicolumn{2}{@{}l}{\textbf{Part~I: The Bar Complex} \emph{(proved core; Thms A--D+H)}} \\[3pt]
codex
I’ve separated the surface into two classes: most `Chapter~...` hits are external bibliography citations, while nearly all potential FM10 violations are internal `Part~...` / cross-volume chapter mentions. I’m reading those internal candidates in context now, plus the two hardcoded chapter-number cases that are not obvious citations.
exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "grep -rn 'Part~[IVXL]' chapters/" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/theory/introduction.tex:34: \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
chapters/theory/introduction.tex:157:(Volume~I, Part~II) organizes the resulting landscape:
chapters/connections/cy_holographic_datum_master.tex:922:This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
chapters/connections/cy_holographic_datum_master.tex:931:\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
chapters/connections/cy_holographic_datum_master.tex:936:\item \emph{Vol~II, Part~III:} the binary collision residue of a
chapters/connections/cy_holographic_datum_master.tex:1009:Vol~III. Subsequent chapters in Part~V record the geometric Langlands
chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~III), the BPS algebra
chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~II) acquires categorical meaning through the
exec
/bin/zsh -lc "grep -rn 'Part~[IVXL]' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/conclusion.tex:987:\subsection{The Part~VII frontier chapters}
chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
 succeeded in 52ms:
chapters/theory/ordered_associative_chiral_kd.tex:5970:hierarchy of Volume~II, Part~VI\@. The correspondence is:
chapters/theory/ordered_associative_chiral_kd.tex:7549:of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
chapters/theory/ordered_associative_chiral_kd.tex:7752:non-formality (Volume~II, Part~VII).
chapters/theory/introduction.tex.bak:1083:flat finite-type completed-dual loci singled out later in Part~I.
chapters/theory/introduction.tex.bak:1282:the outlook (Part~VI, Chapter~\ref{chap:concordance}) records
chapters/theory/introduction.tex.bak:1465:\multicolumn{2}{@{}l}{\textbf{Part~I: The Bar Complex} \emph{(proved core; Thms A--D+H)}} \\[3pt]
chapters/theory/introduction.tex.bak:1487:\multicolumn{2}{@{}l}{\textbf{Part~II: The Characteristic Datum} \emph{(shadow obstruction tower; $E_1$ wing; $E_n$ Koszul duality)}} \\[3pt]
chapters/theory/introduction.tex.bak:1497:\multicolumn{2}{@{}l}{\textbf{Part~III: The Standard Landscape} \emph{(complete portrait of each family)}} \\[3pt]
chapters/theory/introduction.tex.bak:1518:\multicolumn{2}{@{}l}{\textbf{Part~IV: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
chapters/theory/introduction.tex.bak:1534:\multicolumn{2}{@{}l}{\textbf{Part~V: The Seven Faces of the Collision Residue} \emph{(archive-only)}} \\[3pt]
chapters/theory/introduction.tex.bak:1540:\multicolumn{2}{@{}l}{\textbf{Part~VI: The Frontier} \emph{(archive-only)}} \\[3pt]
chapters/theory/introduction.tex.bak:1778:The standard landscape of Part~III is summarized in a single table recording $\kappa$, $c$, $K = c + c'$, $\Delta$, and the shadow archetype for each family.
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:22:Part~I is instantiated here before it is stated in generality.  A
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:116:  complementarity of quantum corrections.  Every theorem of Part~I is
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3737:Part~I develops the categorical logarithm in full generality,
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3738:Part~II extracts its nonlinear content through the shadow obstruction tower,
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3739:Part~III develops the ordered ($E_1$) refinement,
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3740:Part~IV carries the engine out for every major family, and Part~V
chapters/connections/concordance.tex:3796:shadow. Volume~II's Part~VII (ordered
chapters/connections/frontier_modular_holography_platonic.tex:1788:associated classical shadow \textup{(}cf.\ Vol~II, Part~IV\textup{)}.

thinking
**Inspecting ambiguous chapter hits**

I need to look into the ambiguous chapter hits to confirm any false positives. Similar cases like bar_cobar_adjunction_inversion and en_koszul_duality might need external citations, but not all will. I should check other ambiguous external candidates too, such as higher_genus_complementarity and foundations_recast_draft. It might be worthwhile to inspect with context. Perhaps it's sufficient to classify everything based on what I find, so I'll gather contexts through parallel commands, maybe up to 10 at once!
exec
/bin/zsh -lc "nl -ba chapters/connections/conclusion.tex | sed -n '983,993p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '30,36p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '5964,5974p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '153,160p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '7544,7554p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_preface_supplement.tex | sed -n '2051,2059p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '7747,7757p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1784,1792p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3792,3800p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement_body.tex | sed -n '1616,1624p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   983	 Thm~\ref{thm:doubling-rwi} \\
   984	\end{tabular}
   985	\end{center}
   986	
   987	\subsection{The Part~VII frontier chapters}
   988	\label{subsec:frontier-chapters}
   989	
   990	Part~VII extends the proved core of Parts~I--VI into conditional,
   991	conjectural, and frontier territory. Its ten chapters are:
   992	
   993	\begin{enumerate}[label=\textup{(\arabic*)}]
 succeeded in 51ms:
    30	
    31	Three levels of chiral structure organize the theory:
    32	
    33	\begin{itemize}
    34	 \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
    35	 \item $E_2$-chiral algebras (this work): braided factorization on $\mathbb{C} \times \mathbb{C}$, encoding the holomorphic-holomorphic sector. Representation categories are braided monoidal: the natural habitat of quantum groups.
    36	 \item The passage $E_1 \to E_2$ via Dunn additivity: $E_2 \simeq E_1 \otimes E_1$. An $E_2$-chiral algebra is an $E_1$-algebra in $E_1$-algebras.
 succeeded in 50ms:
   153	\begin{remark}[Shadow depth classification of the CY landscape]
   154	\label{rem:v3-cy-glcm-shadow-classification}
   155	The CY-to-chiral functor $\Phi$ assigns to each CY geometry a
   156	chiral algebra $A_\cC$ whose shadow class
   157	(Volume~I, Part~II) organizes the resulting landscape:
   158	\begin{itemize}
   159	\item $\C^3$ (toric, abelian): class~$\mathbf{G}$ (shadow depth~$2$,
   160	 $\kappa_{\mathrm{ch}} = 1$). The Heisenberg truncation at spin~$1$.
 succeeded in 50ms:
  5964	
  5965	\begin{remark}[Physical meaning: the soft graviton hierarchy]
  5966	\label{rem:tridegree-physical}
  5967	\index{soft graviton!and ordered tridegree}
  5968	\index{obstruction cascade!depth-3 origin}
  5969	The ordered tridegree $(g,n,d)^{E_1}$ organises the soft graviton
  5970	hierarchy of Volume~II, Part~VI\@. The correspondence is:
  5971	soft order $p$ of a graviton theorem corresponds to degree
  5972	$r = p + 2$ in the bar complex. The depth~$d$ records
  5973	\emph{which OPE pole is responsible}: a soft theorem at order~$p$
  5974	receives contributions from all poles whose depth
 succeeded in 52ms:
  7544	factorization structure). The ordered bar complex
  7545	$\Barch(A)$ retains the ordering as auxiliary bookkeeping;
  7546	the descent to the symmetric bar $B^\Sigma(A)$ is the
  7547	$R$-matrix-twisted quotient of Proposition~\ref*{sec:r-matrix-descent}.
  7548	None of the families below is $\mathsf{E}_1$-chiral in the sense
  7549	of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
  7550	(nonlocal, ordered configurations as primitive data) are the
  7551	Etingof--Kazhdan quantum vertex algebras, which lie outside
  7552	the Beilinson--Drinfeld framework.
  7553	
  7554	\begin{theorem}[$\mathsf{E}_1$ ordered bar landscape;
 succeeded in 50ms:
  2051	
  2052	\medskip\noindent
  2053	The constructions of Parts~\ref{part:bar-complex}--\ref{part:standard-landscape} provide the MC element, the
  2054	shadow obstruction tower, the Koszul dual, and the genus expansion. Part~\ref{part:seven-faces}
  2055	interprets these in the gravitational context. Part~VII pushes
  2056	to the frontier. Volume~II descends to three dimensions.
 succeeded in 51ms:
  7747	the Yangian $Y_\hbar(\mathfrak{g})$
  7748	(Volume~II, Theorem~\ref*{thm:Koszul_dual_Yangian}).
  7749	For Virasoro and $\mathcal{W}_N$: the ordered Koszul dual is the
  7750	dg-shifted Yangian $Y^{\mathrm{dg}}$, a dg algebra with
  7751	infinitely many cohomological generators reflecting
  7752	non-formality (Volume~II, Part~VII).
  7753	For $\beta\gamma$/$bc$: the Koszul duality exchanges
  7754	statistics ($bc^! = \beta\gamma$, $\beta\gamma^! = bc$),
  7755	so the line-side algebra is the dual free-field system.
  7756	
  7757	All entries are chirally Koszul (bar cohomology concentrated),
 succeeded in 51ms:
  1784	Let\/ $\cP$ be a freely generated Poisson vertex algebra with
  1785	$\lambda$-bracket $\{a_\lambda b\}=\sum_{n\geq 0}\lambda^{(n)}c_n$
  1786	satisfying the $\lambda$-Jacobi identity. Let $\cA$ be a modular
  1787	Koszul chiral algebra with $\cP\cong H^*(\cA,Q)/(\hbar)$ as
  1788	associated classical shadow \textup{(}cf.\ Vol~II, Part~IV\textup{)}.
  1789	\begin{enumerate}[label=\textup{(\roman*)}]
  1790	\item \textup{(Genus-$0$ seed.)} The $\lambda$-bracket determines the
  1791	 genus-$0$ component of the bar differential. Quadratic duality
  1792	 \textup{(}\cite{GLZ22}\textup{)} produces a classical $r$-matrix
 succeeded in 52ms:
  3792	\paragraph{The thesis.}
  3793	The $E_1$ MC element $\Theta^{E_1}_\cA$ is the primary
  3794	algebraic invariant. The modular MC element
  3795	$\Theta_\cA = \operatorname{av}(\Theta^{E_1}_\cA)$ is its
  3796	shadow. Volume~II's Part~VII (ordered
  3797	associative chiral Koszul duality, dg-shifted factorization
  3798	bridge, gravitational Yangian) develops the $E_1$ layer;
  3799	Parts~\ref{part:bar-complex}--\ref{part:v1-frontier} describe the modular/symmetric framework that is the
  3800	$\operatorname{av}$-image. Line operators, spectral $R$-matrices,
 succeeded in 51ms:
  1616	each building on the categorical logarithm of Part~\ref{part:bar-complex},
  1617	the nonlinear engine of Part~\ref{part:characteristic-datum}, and the $E_1$ wing of Part~\ref{part:standard-landscape},
  1618	then extending outward through the standard landscape (Part~\ref{part:physics-bridges}),
  1619	the bridges to mathematical physics (Part~\ref{part:seven-faces}), and the frontier
  1620	(Part~VII). The
  1621	holographic datum $\mathcal{H}(\cA)$ of
  1622	\S\ref{subsec:holographic-datum-sixfold} provides the unifying thread:
  1623	each result is a projection or extraction from the single MC
  1624	element~$\Theta_\cA$.

thinking
**Seeking more context**

I see I'm looking for more context for Volume III and also trying to clarify what the ambiguous chapter hits are. It feels like I need more details to better understand these elements and how they intertwine. Let’s dig a little deeper into this, so I can gather enough information and thoughts to really make sense of it! Understanding those ambiguities will definitely help clarify my perspective.
exec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '918,940p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/braided_factorization.tex | sed -n '84,92p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '1005,1013p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/quantum_group_reps.tex | sed -n '338,346p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/k3_times_e.tex | sed -n '960,970p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '88,96p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/foundations_recast_draft.tex | sed -n '717,735p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '5488,5496p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/quantum_group_reps.tex | sed -n '542,548p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
   918	
   919	\section{Cross-volume bridge}
   920	\label{sec:cy-cross-volume-bridge}
   921	
   922	This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
   923	common skeleton is the seven-face programme; the variation is in which
   924	face is most concrete.
   925	
   926	\begin{remark}[The three seven-face masters]
   927	\label{rem:three-seven-face-masters}
   928	The three volumes each devote a part to the seven-face programme, with
   929	the same architecture but different ground objects:
   930	\begin{enumerate}[label=(\arabic*)]
   931	\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
   932	algebra on a curve, in seven languages: bar-cobar twisting, primitive
   933	generator, classical $r$-matrix, KZ connection, Gaudin model, Bethe
   934	ansatz, dg-shifted Yangian (cf.\ Vol~I,
   935	Theorem~\ref{thm:vol1-seven-face-master}).
   936	\item \emph{Vol~II, Part~III:} the binary collision residue of a
   937	holomorphic-topological quantum group, in seven languages: open-string
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2158,2166p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1005	elliptic $r$-matrix on the torus~$E_\tau$, is proved for affine KM
  1006	in Vol~I, Chapter~\texttt{ch:genus1-seven-faces}.
  1007	
  1008	\noindent\textit{This chapter closes the seven-face programme for
  1009	Vol~III. Subsequent chapters in Part~V record the geometric Langlands
  1010	implications and the bridges to Vols~I--II at the level of theorem
  1011	statements; the present chapter is the algebraic engine that makes the
  1012	bridges possible.}
 succeeded in 50ms:
    84	coincide on degree-$3$ elements; the $R$-matrix arises from the bar
    85	differential restricted to degree $(1,1)$. Coassociativity at degree $3$
    86	gives $\cR_{12}\cR_{13}\cR_{23} = \cR_{23}\cR_{13}\cR_{12}$, which is
    87	the Yang--Baxter equation. The spectral parameters arise from the
    88	$z$-dependence of the collision residue (so the $R$-matrix has one
    89	fewer pole order than the OPE). See Volume~II, Chapter~11 for the
    90	full derivation.
    91	\end{proof}
    92	
 succeeded in 52ms:
   338	
   339	\begin{remark}[Slab as bimodule]
   340	\label{rem:bps-slab}
   341	% RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.
   342	In the Dimofte framework (Volume~II, Part~III), the BPS algebra
   343	arises from the 3d holomorphic-topological theory on the slab
   344	$X \times [0,1]$. The slab has \emph{two} boundary components
   345	($X \times \{0\}$ and $X \times \{1\}$), making the algebra of
   346	operators on the slab a bimodule for the two boundary algebras.
 succeeded in 52ms:
    88	track~(a) is developed here; track~(b) is a completion target.
    89	\end{remark}
    90	
    91	\begin{remark}[The generalization principle: Arnold to Fay]
    92	\label{rem:arnold-fay-generalization}
    93	\index{Arnold relation!Fay generalization}
    94	The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
    95	\end{remark}
    96	
 succeeded in 52ms:
   960	
   961	\section{Cross-volume structural results}
   962	\label{sec:k3e-cross-volume}
   963	
   964	The following results are proved in Volume~I
   965	(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
   966	of Chapter~66) and apply to the $K3 \times E$ tower.
   967	We record them here for cross-reference; conventions
   968	follow Volume~I throughout.
   969	
   970	\begin{enumerate}[label=\textup{(K3-\arabic*)}]
 succeeded in 51ms:
   717	Stages~$0$--$2$ are classical; see Loday--Vallette \cite{LV12},
   718	Chapters~2, 9, and~11.
   719	Stage~$3$: the BD chiral operad structure on $\FM_k(\C)$ and
   720	its relation to OPE residues is Beilinson--Drinfeld
   721	\cite{BD04}, Chapter~3.
   722	Stage~$4$: the identification of $\barB(A)$ as an $\Eone$
   723	dg coassociative coalgebra over $(\mathrm{ChirAss})^!$ is
   724	Proposition~\ref{prop:bar-from-open}(iii).
   725	Stage~$5$: the $\SCchtop$ structure on the pair
   726	$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(A), A)$ is
   727	Theorem~\ref{thm:universal-bulk}(ii).
   728	Stage~$6$: the chiral endomorphism operad is
   729	Definition~\ref{def:chiral-endomorphism-operad-v2}; the
   730	$\Aut(\cO)$-equivariance is the coordinate-independence of
   731	vertex algebra axioms (Frenkel--Ben-Zvi \cite{FBZ04},
   732	Chapter~4).
   733	Stage~$7$: the modular extension and curvature identity are
   734	Volume~I, Theorem~D.
   735	Stage~$8$: the $\Etwo$-chiral Gerstenhaber structure on
 succeeded in 50ms:
  5488	\label{sec:k3e-cross-volume}
  5489	
  5490	The following results are proved in Volume~I
  5491	(\S\ref{sec:k3-sigma-model}--\S\ref{sec:grand-synthesis-k3xe}
  5492	of Chapter~66) and apply to the $K3 \times E$ tower.
  5493	We record them here for cross-reference; conventions
  5494	follow Volume~I throughout.
  5495	
  5496	\begin{enumerate}[label=\textup{(K3-\arabic*)}]
 succeeded in 52ms:
   542	\section{Shadow obstruction tower for quantum group categories}
   543	\label{sec:shadow-tower-qg}
   544	
   545	The shadow obstruction tower $\Theta_{A_\cC}$
   546	(Volume~I, Part~II) acquires categorical meaning through the
   547	quantum group lens.
   548	
 succeeded in 51ms:
  2158	derived-functor differential, not a pushforward integral.
  2159	Convergence is controlled by the finite cohomological dimension
  2160	of $\overline{\mathcal{M}}_g$
  2161	(Lemma~\ref{lem:quantum-ss-convergence}; compare
  2162	Costello--Gwilliam~\cite{CG17}, Volume~2, Chapter~5).
  2163	\end{remark}
  2164	
  2165	\subsection{Corollaries and physical interpretation}
  2166	

thinking
**Investigating cross-volume references**

I need to look more into the conclusion, especially regarding Part VII and its section heading. It seems crucial to check for any labels across volumes that could help, like `part:seven-faces`. I wonder if using hardcoded parts in cross-volume references violates the expected use of `\ref{part:...}`. If cross-repo references are not defined, it could cause issues since the guidelines say to use `\ref`. I’ll need to inspect compliant examples and search for patterns.
codex
I’ve confirmed the main live candidates. Before freezing the findings, I’m checking how the manuscript itself writes compliant part cross-references, so I don’t mislabel intentional patterns as violations.
exec
/bin/zsh -lc "rg -n \"Volume~II, Part~\\\\ref|Vol~II, Part~\\\\ref|Volume~I, Part~\\\\ref|Vol~I, Part~\\\\ref|Parts~\\\\ref|Part~\\\\ref\\{part:\" chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Volume~II, Part~\\\\ref|Vol~II, Part~\\\\ref|Volume~I, Part~\\\\ref|Vol~I, Part~\\\\ref|Parts~\\\\ref|Part~\\\\ref\\{part:\" chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"Volume~II, Part~\\\\ref|Vol~II, Part~\\\\ref|Volume~I, Part~\\\\ref|Vol~I, Part~\\\\ref|Parts~\\\\ref|Part~\\\\ref\\{part:\" chapters/" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 50ms:

exec
/bin/zsh -lc "rg -n \"part:[A-Za-z0-9:-]+|Part~\\\\ref|Parts~\\\\ref\" chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"part:[A-Za-z0-9:-]+|Part~\\\\ref|Parts~\\\\ref\" chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"part:[A-Za-z0-9:-]+|Part~\\\\ref|Parts~\\\\ref\" chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/rosetta_stone.tex:1881:Part~\ref{part:e1-core}\@.
chapters/examples/rosetta_stone.tex:5718: & (Part~\ref{part:e1-core})
chapters/examples/rosetta_stone.tex:5720: & (Part~\ref{part:e1-core})
chapters/examples/rosetta_stone.tex:5722: & (Part~\ref{part:e1-core}) \\
chapters/examples/rosetta_stone.tex:5773:the full treatment is in Part~\ref{part:e1-core}\@.
chapters/frame/preface_trimmed.tex:435:Part~\ref{part:examples}.
chapters/frame/preface_trimmed.tex:627:(Part~\ref{part:swiss-cheese}).}\enspace
chapters/frame/preface_trimmed.tex:634:(Part~\ref{part:e1-core}).}\enspace
chapters/frame/preface_trimmed.tex:641:(Part~\ref{part:bbl-core}).}\enspace
chapters/frame/preface_trimmed.tex:652:(Part~\ref{part:examples}).}\enspace
chapters/frame/preface_trimmed.tex:659:(Part~\ref{part:holography}).}\enspace
chapters/frame/preface_trimmed.tex:666:(Part~\ref{part:gravity}).}\enspace
chapters/frame/preface_trimmed.tex:678:(Part~\ref{part:frontier}).}\enspace
chapters/frame/preface.tex:56:  \ref{part:swiss-cheese} \\[2pt]
chapters/frame/preface.tex:61:  \ref{part:swiss-cheese} \\[2pt]
chapters/frame/preface.tex:66:  \ref{part:e1-core} \\[2pt]
chapters/frame/preface.tex:72:  \ref{part:bbl-core} \\[2pt]
chapters/frame/preface.tex:78:  \ref{part:bbl-core} \\[2pt]
chapters/frame/preface.tex:84:  \ref{part:holography} \\[2pt]
chapters/frame/preface.tex:90:  \ref{part:examples} \\[2pt]
 succeeded in 51ms:
Total output lines: 109

chapters/examples/lattice_foundations.tex:65:Every example in Part~\ref{part:physics-bridges} descends from a single algebraic seed.
chapters/examples/lattice_foundations.tex:1475:of Part~\ref{part:bar-complex} applies throughout.
chapters/examples/lattice_foundations.tex:1653:quantum corrections studied in Part~\ref{part:bar-complex}.
chapters/examples/lattice_foundations.tex:1936:main theorems of Part~\ref{part:bar-complex}. Each verification reveals structure invisible
chapters/examples/lattice_foundations.tex:3958:bar-cobar framework of Part~\ref{part:bar-complex}.
chapters/examples/yangians_foundations.tex:457: (the $\Einf$-chiral story of Part~\ref{part:bar-complex}). With ordering, it
chapters/examples/toroidal_elliptic.tex:54:The Arnold relation (Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex of Part~\ref{part:bar-complex} (Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
chapters/examples/bar_complex_tables.tex:1989:Parts~\ref{part:bar-complex}--\ref{part:standard-landscape} (configuration space integrals, FM
chapters/examples/bar_complex_tables.tex:1991:of Part~\ref{part:physics-bridges} (OPE residues, screening operators,
chapters/examples/landscape_census.tex:29:Koszul chiral algebra treated in Part~\ref{part:physics-bridges}. Read horizontally, each row
chapters/examples/landscape_census.tex:37:\noindent\emph{The Master Table below collects the invariants computed throughout Part~\ref{part:physics-bridges}. For the Heisenberg algebra, these invariants were derived in Chapter~\ref{ch:heisenberg-frame}; for each subsequent algebra, the corresponding chapter provides the complete computation.}
chapters/examples/landscape_census.tex:1772:presentations of the bar complex given in Part~\ref{part:physics-bridges};
chapters/examples/landscape_census.tex:4048:The computations of Part~\ref{part:physics-bridges} are complete. Part~\ref{part:seven-faces} connects the bar-cobar framework to adjacent programs (Feynman diagrams, BV-BRST, holomorphic-topological field theories, the 4d/2d correspondence) and concludes with the concordance and the project toward modular Koszul duality (\S\ref{sec:modular-koszul-programme}).
chapters/connections/thqg_symplectic_polarization.tex:86:The five main theorems (A--D+H) of Part~\ref{part:bar-complex} supply the following
chapters/theory/koszul_pair_structure.tex:2774:The Koszul pair structure developed in this chapter (the quadratic condition, the periodicity phenomena, the level-shifting involution) provides the algebraic skeleton on which the examples of Part~\ref{part:characteristic-datum} are built. Every explicit computation there begins by verifying the Koszul condition and identifying the dual; the reward is that the three main theorems then deliver bar cohomology, spectral collapse, and complementarity without further work. The periodicity theorems, in particular, constrain the genus tower: the Hochschild cohomology ring $\mathrm{CH}^*(\cA)$ controls deformations of the bar complex at every genus, and Koszul duality exchanges the periodicity generators of $\cA$ and $\cA^!$ with a sign (Corollary~\ref{cor:hochschild-cup-exchange}).
chapters/connections/thqg_preface_supplement.tex:2017:chapters of Parts~\ref{part:seven-faces}--VII of this monograph:
chapters/connections/thqg_preface_supplement.tex:2053:The constructions of Parts~\ref{part:bar-complex}--\ref{part:standard-landscape} provide the MC element, the
chapters/connections/thqg_preface_supplement.tex:2054:shadow obstruction tower, the Koszul dual, and the genus expansion. Part~\ref{part:seven-faces}
 succeeded in 51ms:
chapters/examples/fukaya_categories.tex:560:Part~\ref{part:cy-categories}), the primitive object is the full open-sector factorization
chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
chapters/connections/geometric_langlands.tex:4:The functor $\Phi$ of \ref{part:bridge} sends a Calabi--Yau category to an $\Etwo$-chiral algebra; the bar complex of the output (Volume~I, Theorem~A) is the factorization invariant on which geometric Langlands is ultimately a statement. This chapter traces the thread. At the critical level the Feigin--Frenkel theorem identifies the chiral center with the algebra of $G^L$-opers; the Verdier intertwining of Volume~I Theorem~A then relates local geometric Langlands to the four-functor picture (bar, cobar, Verdier, derived center). For Calabi--Yau input, the analogue is conjectural: a Langlands dual of a CY $d$-category should realize the mirror of its $\Phi$-image. The chapter is entirely FRONTIER material. Every formal statement uses \texttt{\textbackslash{}begin\{conjecture\}} unless it is a literal citation of Feigin--Frenkel (1992) or Frenkel--Gaitsgory (2006), in which case it is tagged \ClaimStatusProvedElsewhere.
chapters/frame/preface.tex:350:Part~\ref{part:cy-categories} establishes the categorical
chapters/frame/preface.tex:354:obstruction tower. Part~\ref{part:bridge} constructs the
chapters/frame/preface.tex:359:Part~\ref{part:bridge} is the Drinfeld center chapter: the
chapters/frame/preface.tex:364:Part~\ref{part:examples} works through the standard CY
chapters/frame/preface.tex:367:Part~\ref{part:connections} develops the seven faces of
chapters/frame/preface.tex:370:Part~\ref{part:frontier} connects to the geometric Langlands
chapters/theory/cyclic_ainf.tex:4:A Calabi--Yau category enters this volume through a single structural datum: a cyclic $\Ainf$-algebra of dimension $d$. Everything that follows, the functor $\Phi$ to chiral algebras, the modular characteristic $\kappa_{\mathrm{cat}}$, the four subscripted kappas of the CY kappa-spectrum, depends on this input. This chapter fixes the definitions, records the standard examples (elliptic curve, K3, quintic), and states the bridge to \ref{part:bridge} precisely. The content is classical (Stasheff, Kontsevich, Keller, Costello); the Vol~III role is the specific identification of $d$ with the CY dimension appearing in Theorem~CY-A.
chapters/theory/cyclic_ainf.tex:85:The cyclic pairing enters the bar complex $B(A) = T^c(s^{-1}\bar A)$ through the cyclic quotient $\mathrm{CC}_\bullet(A) = B(A)/(1 - t)$ where $t$ is the signed cyclic rotation. The factor $s^{-1}$ desuspends: $|s^{-1}v| = |v| - 1$. The augmentation ideal $\bar A = \ker(\varepsilon)$ is used rather than $A$ itself. The cyclic bar complex is the primary invariant of $(A, \mu_n, \langle-,-\rangle)$ and is what \ref{part:bridge} promotes to a factorization coalgebra on curves.
chapters/theory/cyclic_ainf.tex:200:Four source threads feed the construction used here. Stasheff~\cite{Stasheff1963} introduced the associahedra and the higher homotopies $\mu_n$. Kontsevich~\cite{Kontsevich1995} identified cyclic $\Ainf$-algebras with algebras over the operad of ribbon graphs, providing the link to moduli of curves with boundary. Costello~\cite{Costello2005TCFT,Costello2007Ainfty} proved that cyclic $\Ainf$-categories are equivalent to open topological conformal field theories and supplied the first rigorous construction of the associated chain-level trace. Kontsevich--Soibelman~\cite{KontsevichSoibelman2009} axiomatized the CY structure in terms of the negative cyclic class and gave the formalism used in Part~\ref{part:cy-categories}. Keller~\cite{Keller2001Ainfty} surveys the homological-algebra side. For explicit computations on projective varieties, Polishchuk~\cite{Polishchuk2011} computed the cyclic $\Ainf$-structure on elliptic curves and on their products, and Caldararu~\cite{Caldararu2005} set up the Hochschild calculus for smooth proper CY categories. The Vol~III role is the specific mapping of this input through the functor $\Phi$, producing chiral algebras whose modular characteristic can be computed and compared across the four kappas of the spectrum.
chapters/theory/e2_chiral_algebras.tex:174:duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
chapters/theory/e1_chiral_algebras.tex:145:The proof unfolds in Chapter~\ref{ch:cy-chiral-functor}. For $\cC = D^b(\Coh(K3))$ the output is the positive half of the BKM superalgebra studied in \ref{part:examples}: the Borcherds denominator arises as the Euler character of $B^{\mathrm{ord}}(A_{K3})$, and $\kappa_{\mathrm{BKM}} = 5$ is distinct from $\kappa_{\mathrm{ch}} = 3$.
chapters/theory/e1_chiral_algebras.tex:152:The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:cha-yangian}.
chapters/theory/e1_chiral_algebras.tex:184:The CY-to-chiral functor $\Phi$ of \ref{part:cy-categories} factors as $\Phi = \Phi^{\mathrm{Vol\ II}}_{E_1} \circ \Phi^{\mathrm{Vol\ III}}_{\mathrm{cyc}}$, where $\Phi^{\mathrm{Vol\ III}}_{\mathrm{cyc}}$ takes a CY$_d$ category to its cyclic $A_\infty$ algebra and $\Phi^{\mathrm{Vol\ II}}_{E_1}$ takes a cyclic $A_\infty$ algebra to an $E_1$-chiral algebra via the Swiss-cheese promotion.
chapters/theory/e1_chiral_algebras.tex:615:The remaining parts use these facts directly. \ref{part:bridge} computes the modular trace $\kappa_{\mathrm{ch}}$ for each CY family, using the ordered bar as the computational model. \ref{part:examples} catalogues the families $K3$, $K3 \times E$, toric CY$_3$, Fukaya, and quantum-group, and identifies the corresponding point in the kappa-spectrum. \ref{part:connections} reads the seven faces of $r_{\mathrm{CY}}(z)$ from the $E_1$ structure of Proposition~\ref{prop:e1-sector-d2}. \ref{part:frontier} collects the open problems, most of them variants of Conjecture~\ref{conj:e1-sector-d3} or its downstream consequences. Throughout, the ordered bar is the primitive, and the averaging map, Drinfeld center, and modular characteristic are all computed on the $E_1$ side before any symmetric or braided image is taken.
chapters/theory/introduction.tex:295: \item All physics conjectures in Part~\ref{part:frontier}.
chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
chapters/theory/hochschild_calculus.tex:372:Under the CY-to-chiral functor $\Phi$ (Part~\ref{part:bridge}), the categorical




thinking
**Analyzing reference formats**

I see that the output got quite large and truncated. There are examples of compliant `Part\ref`, which is good because it confirms what I expected. I might need to check Volume III for `Chapter\ref` or current chapter references. It could make sense to inspect contexts for live references. I wonder if these cross-volume references should use labels or citations, especially since FM10 says hardcoded references can break silently during reorganization. So, should I find all live Part references across volumes? The grep output showed all `Part` hits, including backups.
thinking
**Identifying live references**

I need to determine which references are live. There might be more internal ones that weren't captured by grep since `Part\ref` isn't relevant right now. I’m focusing on identifying genuine part violations, which include several files across Volumes I, II, and III. For instance, in Volume I, I see specific lines in `ordered_associative_chiral_kd.tex` and other files that need attention. Also, I noticed some files in Volume III that hardcode previous references to Volume I. This could impact citation consistency.
thinking
**Considering backup file classifications**

I’m thinking about how to classify backup file hits. Maybe I could assign a MEDIUM severity to them when reporting. I might also want to categorize low-severity backups as LOW, since the user asked about each hit, not just the live ones. Hmm, I should inspect the contexts of these backup files to see if they need to be classified as low or as false positives since grep includes `.bak` files under chapters.
thinking
**Inspecting backup findings**

I'm considering how to evaluate the findings for stale backup artifacts, which may not be reported as genuine. The final output should list findings ordered by severity, so I might include low findings for these artifacts even if they're non-live. They still match the sweep and could cause drift. I'll quickly inspect the minimal context around backup files, like introduction.tex.bak and Heisenberg backup, to verify their relevance. Let’s see what those lines reveal!
codex
I’ve verified the live violations. I’m doing one last pass over the backup/draft hits to decide whether they’re genuine low-risk artifact debt or just noise that should be excluded from the final report.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex.bak | sed -n '1278,1284p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex.bak | sed -n '1079,1085p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1079	measures the failure of strict commutativity.  Vanishing of the
  1080	scalar curvature term $\kappa(\cA)$ removes one obstruction, but the
  1081	manuscript's reduction from the intrinsic coderived/contraderived
  1082	comparison to ordinary derived categories is proved only on the
  1083	flat finite-type completed-dual loci singled out later in Part~I.
  1084	
  1085	Off the Koszul locus, the coderived category
 succeeded in 52ms:
  1278	and the DK ladder
  1279	through step~3 on the evaluation-generated core at all simple Lie
  1280	types.
  1281	This ring is closed: every claim is proved in the text, and
  1282	the outlook (Part~VI, Chapter~\ref{chap:concordance}) records
  1283	its boundary precisely.
  1284	
exec
/bin/zsh -lc 'ls chapters/theory/introduction.tex chapters/theory/introduction.tex.bak chapters/frame/heisenberg_frame.tex chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix | sed -n '18,24p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex.bak | sed -n '1774,1780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix | sed -n '3735,3742p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix | sed -n '112,118p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex.bak | sed -n '1462,1542p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/heisenberg_frame.tex
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
chapters/theory/introduction.tex
chapters/theory/introduction.tex.bak
 succeeded in 51ms:
    18	where the MC element has no nonlinear obstructions and the genus
    19	expansion closes in one step.
    20	
    21	The strategy: example first, theory after.  Every theorem proved in
    22	Part~I is instantiated here before it is stated in generality.  A
    23	reader who writes out the Arnold relation for three points,
    24	differentiates the bar complex at degree~$2$, and checks that the
 succeeded in 51ms:
  1774	\section{The master invariant table}
  1775	\label{sec:master-invariant-table-intro}
  1776	\index{master invariant table}
  1777	
  1778	The standard landscape of Part~III is summarized in a single table recording $\kappa$, $c$, $K = c + c'$, $\Delta$, and the shadow archetype for each family.
  1779	
  1780	\begin{center}
 succeeded in 50ms:
   112	  (\S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-complementarity})
   113	  carries the full vertical structure: the bar complex at genus~$0$,
   114	  the Arnold relation, the Koszul dual, bar-cobar inversion, genus-$1$
   115	  curvature, the $\hat{A}$-genus generating function, and the
   116	  complementarity of quantum corrections.  Every theorem of Part~I is
   117	  instantiated here.
   118	
 succeeded in 51ms:
  1462	{\small
  1463	\renewcommand{\arraystretch}{1.25}
  1464	\begin{longtable}{@{}p{0.32\textwidth}p{0.62\textwidth}@{}}
  1465	\multicolumn{2}{@{}l}{\textbf{Part~I: The Bar Complex} \emph{(proved core; Thms A--D+H)}} \\[3pt]
  1466	\hline
  1467	Fourier seed (Ch.~\ref{ch:fourier-seed}) &
  1468	  Bar construction as transform; product-formula GF; inversion as Fourier inversion \\
  1469	Algebraic foundations (Ch.~\ref{ch:algebraic-foundations}) &
  1470	  Classical Koszul duality; twisting morphisms; operadic bar-cobar; HTT ($A_\infty$/$L_\infty$ transfer) \\
  1471	Configuration spaces (Ch.~\ref{chap:config-spaces}) &
  1472	  FM compactification $\overline{C}_n(X)$; Arnold relations; residue calculus; cooperadic boundary strata \\
  1473	Geometric bar complex (Ch.~\ref{chap:bar-cobar}) &
  1474	  $\barB_X(\cA)$ via residue extraction; \textbf{Theorem~A} (adjunction + Verdier intertwining); $d^2=0$ \\
  1475	Geometric cobar complex (Ch.~\ref{chap:cobar-construction}) &
  1476	  $\Omega_X$ as left adjoint; $d^2_{\mathrm{cobar}}=0$ via Verdier duality \\
  1477	Bar-cobar adjunction (Ch.~\ref{chap:bar-cobar-adjunction}) &
  1478	  \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
  1479	Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
  1480	  $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
  1481	Higher genus (Ch.~\ref{chap:higher-genus}) &
 succeeded in 60ms:
  3735	preserving everything already established.
  3736	
  3737	Part~I develops the categorical logarithm in full generality,
  3738	Part~II extracts its nonlinear content through the shadow obstruction tower,
  3739	Part~III develops the ordered ($E_1$) refinement,
  3740	Part~IV carries the engine out for every major family, and Part~V
  3741	connects them to BV-BRST quantization, Feynman integrals, and
  3742	holomorphic-topological field theory.




thinking
**Deciding on backup artifacts**

I need to figure out whether backup artifacts should count in my report. There are files under chapters, but live siblings exist, so they likely don't violate any genuine manuscript rules. The user asked for specific file:line entries for violations. I think reporting only genuine discrepancies makes sense, but backups could clutter the results. I could summarize some findings, but I want to keep the final answer concise, maybe around 50-70 lines. There are about 18 live and possibly 5 low backup hits.
thinking
**Investigating ambiguous chapter hits**

I’m inspecting potential false positives in my chapter hits that aren’t citations. For example, lines like `ordered_associative_chiral_kd_frontier.tex:83` and others contain clear external citations. However, I’m also seeing some lines that might indicate hardcoded chapters, like in `k3_times_e` and `toroidal_elliptic`. They appear to have nearly identical text, which raises concerns about possible duplication. I need to check for any live candidates with "Part" labels nearby, as this could strengthen the findings and perhaps report both instances as high severity.
thinking
**Evaluating second-order failures**

I'm thinking about inspecting line 1006 in cy_holographic_datum_master since it mentions a broken label that isn't showing up in the grep results. Even though the user's mission focuses on FM10/B33, this seems like a second-order failure worth mentioning, as it aligns with the same failure class.

Completeness means I should check for similar patterns, but I wonder if that tight scope limits my findings. I might run a targeted search for similar chapter labels across the volumes, just in case.
thinking
**Considering expansion limits**

I’m realizing we shouldn’t aim for endless expansion in this project. Instead, it might be more effective to simply note any discovered adjacency if there are only a few instances. Keeping it focused could help maintain clarity and prevent overwhelming complexity in the findings. It's essential to balance thoroughness with practicality, so I want to ensure that I don't overextend our scope unnecessarily while still capturing valuable insights.
codex
A second-order check turned up one adjacent pattern worth testing: chapter references written as literal label names rather than `\ref`. I’m scanning just that narrow variant now so the final report doesn’t miss an obvious sibling defect.
exec
/bin/zsh -lc "rg -n 'Chapter~\\\\texttt|Volume~[IVX]+, Chapter~\\\\texttt|Vol~[IVX]+, Chapter~\\\\texttt|Chapter~[A-Za-z]' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:5015:presentable by \cite[Chapter~I.3]{GR17}; see also
chapters/theory/chiral_koszul_pairs.tex:5023:\cite[Chapter~IV.5]{GR17}.
chapters/theory/higher_genus_foundations.tex:3115:(cf.~\cite{Fay73}, Chapter~III, and \cite{dH89}).
chapters/theory/higher_genus_foundations.tex:3303:(\cite{Fay73}, Chapter~II) give
chapters/theory/computational_methods.tex:369:(Flajolet--Sedgewick, Chapter~VI) gives
exec
/bin/zsh -lc "rg -n 'Chapter~\\\\texttt|Volume~[IVX]+, Chapter~\\\\texttt|Vol~[IVX]+, Chapter~\\\\texttt|Chapter~[A-Za-z]' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Chapter~\\\\texttt|Volume~[IVX]+, Chapter~\\\\texttt|Vol~[IVX]+, Chapter~\\\\texttt|Chapter~[A-Za-z]' chapters/" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
chapters/connections/cy_holographic_datum_master.tex:1006:in Vol~I, Chapter~\texttt{ch:genus1-seven-faces}.
chapters/theory/quantum_groups_foundations.tex:154:Reshetikhin--Turaev, ``Ribbon graphs and their invariants derived from quantum groups'' (Comm.\ Math.\ Phys.\ 1990); Turaev, \emph{Quantum Invariants of Knots and $3$-Manifolds}, Chapter~XI.
 succeeded in 50ms:
chapters/theory/factorization_swiss_cheese.tex:2067:$X \times X$ (Fay \cite{Fay73}, Chapter~II). Its logarithmic
chapters/connections/dnp_identification_master.tex:540:Chapter~\texttt{ch:genus1-seven-faces}.

thinking
**Considering chapter references**

I'm noticing second-order hits in the documents for Vol II and Vol III, both sharing the same label text. The user is focused on hardcoded part numbers, but it seems the grep also pulls chapter numbers. I should consider including these as a structural note, but it needs to fit the output contract of file:line severity. Perhaps I could provide a note about their discovery during context checking. I should also inspect specific lines in the dnp_identification_master for possible insights.
exec
/bin/zsh -lc "nl -ba chapters/connections/dnp_identification_master.tex | sed -n '536,542p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/cy_holographic_datum_master.tex | sed -n '1004,1007p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
   536	
   537	The genus-$1$ extension of the seven-face programme, proving the
   538	identification of the KZB connection with the elliptic $r$-matrix
   539	and the elliptic Gaudin model for affine KM, is in Vol~I,
   540	Chapter~\texttt{ch:genus1-seven-faces}.
 succeeded in 51ms:
  1004	The genus-$1$ extension, identifying the KZB connection with the
  1005	elliptic $r$-matrix on the torus~$E_\tau$, is proved for affine KM
  1006	in Vol~I, Chapter~\texttt{ch:genus1-seven-faces}.
  1007	

thinking
**Searching document references**

I’m considering searching for all instances of `PartVII` and `Chapterdigits` in the live version while excluding backups or drafts like `.bak` and `_draft.tex`. I noticed `foundations_recast_draft.tex` included citations, which seems fine, but it’s better to focus only on chapters. I'll need to look for hardcoded internal references, such as `VolumeI, Chapter\ref` or `Chapter66`, and confirm cross-volume labels in Volume III. I wonder how Volume III can reference parts that aren't in the same repository.
exec
/bin/zsh -lc "rg -n 'part:e1-core|part:swiss-cheese|part:bbl-core|part:gravity|part:frontier' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'part:bar-complex|part:characteristic-datum|part:standard-landscape|part:seven-faces|part:v1-frontier' chapters/" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:

 succeeded in 52ms:
chapters/frame/preface.tex:370:Part~\ref{part:frontier} connects to the geometric Langlands
chapters/theory/introduction.tex:295: \item All physics conjectures in Part~\ref{part:frontier}.
chapters/theory/introduction.tex:398:Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
chapters/theory/e2_chiral_algebras.tex:174:duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
chapters/theory/e1_chiral_algebras.tex:615:The remaining parts use these facts directly. \ref{part:bridge} computes the modular trace $\kappa_{\mathrm{ch}}$ for each CY family, using the ordered bar as the computational model. \ref{part:examples} catalogues the families $K3$, $K3 \times E$, toric CY$_3$, Fukaya, and quantum-group, and identifies the corresponding point in the kappa-spectrum. \ref{part:connections} reads the seven faces of $r_{\mathrm{CY}}(z)$ from the $E_1$ structure of Proposition~\ref{prop:e1-sector-d2}. \ref{part:frontier} collects the open problems, most of them variants of Conjecture~\ref{conj:e1-sector-d3} or its downstream consequences. Throughout, the ordered bar is the primitive, and the averaging map, Drinfeld center, and modular characteristic are all computed on the $E_1$ side before any symmetric or braided image is taken.

thinking
**Investigating cross-volume references**

I noticed there's no "Volume I" label in Volume III. However, I found references to Volume II in `e2_chiral_algebras.tex`, like `\ref{part:e1-core} of \cite{VolII}`, which suggests compliant cross-volume citations. This raises the question of whether hardcoded references in Volume III violate the rules since at least one file uses the appropriate notation. It might be beneficial to check if similar compliant references exist in Volumes I or II as well.
exec
/bin/zsh -lc "nl -ba chapters/theory/e2_chiral_algebras.tex | sed -n '170,176p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
   170	\section{Connection to Volume~II: the Drinfeld center}
   171	\label{sec:drinfeld-center-bridge}
   172	
   173	Volume~II constructs $\Phi_{E_1}$ and proves $E_1$-chiral Koszul
   174	duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
   175	$Z\colon E_1\text{-}\Cat \xrightarrow{\sim} E_2\text{-}\Cat$
   176	(under dualizability) is the categorical passage from ordered
exec
/bin/zsh -lc "rg -n '\\\\ref\\{part:["'^}]+'"\\} of \\\\cite\\{VolI\\}|\\\\ref\\{part:["'^}]+'"\\} of \\\\cite\\{VolII\\}' chapters/" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/theory/e2_chiral_algebras.tex:174:duality (see \ref{part:e1-core} of \cite{VolII}). The Drinfeld center
exec
/bin/zsh -lc "rg -n '\\\\ref\\{part:["'^}]+'"\\} of \\\\cite\\{VolI\\}|\\\\ref\\{part:["'^}]+'"\\} of \\\\cite\\{VolIII\\}|\\\\ref\\{part:["'^}]+'"\\} of \\\\cite\\{VolII\\}' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\ref\\{part:["'^}]+'"\\} of \\\\cite\\{VolII\\}|\\\\ref\\{part:["'^}]+'"\\} of \\\\cite\\{VolIII\\}|\\\\ref\\{part:["'^}]+'"\\} of \\\\cite\\{VolI\\}' chapters/" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 52ms:










thinking
**Deciding instance counts**

I’ve got one explicit example that might not need to be included in the final output. I should check if Volume II makes local references in the conclusion—there are many hits. I think I can set the instance count as 75, including the 73 grep hits plus a couple of adjacent chapter-label variants. However, I should probably just state the 73 from the grep initially, noting the extras for clarity. I'll finalize the output format soon!
thinking
**Counting violations for summary**

I might be able to say, "Instances checked: 75," noting it includes 73 grep hits plus 2 adjacent sibling patterns. But the contract feels rigid, so maybe I'd just state, "Instances checked: 75 | Violations found: 22 | Verdict: FAIL." I need to determine the exact violation count. I'll tally genuine live violations, low artifacts, and second-order ones. I can list some candidates and check that backup hit situation too. This will help finalize things!
thinking
**Considering report structure**

I think providing 15 extra lines is still manageable, so that gives me about 38 lines in total, plus a summary. That fits within the 50-70 line range. However, I wonder if the user is looking for a more concise audit report rather than all the backup details that might obscure current issues. It might be better to focus on lower priority items, like detailed notes on specific sections that could get too noisy.
thinking
**Evaluating violation reports**

I’m thinking about how to handle explicit instructions regarding genuine violations versus false positives. Ideally, for real violations, I should clearly list each hit. However, backup hits might be classified as false positives since they come from non-live backups, not the actual compiled manuscript. I'm debating whether a `.bak` file counts as a false positive, especially since it’s not part of the active manuscript. Given the context, I feel it's reasonable to exclude `.bak` hits from the report.
thinking
**Finalizing the report**

I'm considering how to structure the final report regarding the items not counted—should I mention them under summary or residual risks? Since the output contract only requires findings, I wonder if it’s needed at all. It might be useful to note that backup artifacts were excluded and perhaps include counts, like 75 instances checked with 13 citation false positives. I also need to verify second-order findings, which may indicate structural failures, and clarify what exact details to include in the summary.
thinking
**Verifying file classifications**

I’m thinking about verifying file classifications using commands like `file` or `ls`, but maybe it’s not necessary. I should inspect files like `introduction.tex.bak` to confirm they are indeed backups and should count as false positives. The `ls` command already shows these `.bak` files and their live counterparts, which is helpful. I may look into line 987 of the conclusion section for "The Part VII frontier chapters," since it addresses a structural aspect. Lastly, I should check if `VolumeII, PartIII` in Vol III is acceptable, given absent references.
thinking
**Evaluating severity of violations**

I think we should mention the "hardcoded part number" instead of "missing \ref" because the cross-volume fix style looks like `\ref{part:...} of \cite{VolII}`. The user did ask for the exact violating text, so we'll report that description with the text included. Now, should I classify `toroidal_elliptic.tex:94` as high or medium severity? It's structural, so I might lean towards HIGH. Similarly for `ordered_associative_chiral_kd.tex:7549`, all live violations seem structural rather than mathematical, which suggests HIGH as well.
thinking
**Organizing findings by severity**

It might be okay to note that there are no CRITICAL/MEDIUM/LOW issues if none exist. I could just list all 23 as HIGH; it might be long, but that's alright. I could group them by volume within severity, though the contract specifies findings ordered by severity. 

If I include second-order findings not from the original grep, I might mention them after the direct hits. I also need to address false positives, which seem to be 52 out of 73 hits, primarily from external citations. In total, I could say there are 23 violations found, with a summary stating 75 instances checked and a verdict of FAIL.
thinking
**Clarifying counts of violations**

I think the user might only expect the grep hits. I could say there were 73 checks and 21 direct violations. However, if I include the two second-order cases, I could run into a count mismatch. 

A summary like `Instances checked: 73 grep hits + 2 adjacent sibling cases | Violations found: 23 | Verdict: FAIL` could work, but the contract specifies otherwise. Maybe saying `Instances checked: 75` could still be acceptable, as long as it’s clear. I need to confirm there are exactly 21 live direct violations from those 73 hits.
codex
One sibling pattern fell outside the original grep: mixed plural references like `Parts~\ref{...}--VII` or `Parts~I--VI`. I’m checking that narrow surface once so the audit is actually complete.
exec
/bin/zsh -lc "rg -n 'Parts~I|Parts~V|Parts~X|Parts~\\\\ref\\{["'^}]+'"\\}--[IVXL]+' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'Parts~I|Parts~V|Parts~X|Parts~\\\\ref\\{["'^}]+'"\\}--[IVXL]+' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Parts~I|Parts~V|Parts~X|Parts~\\\\ref\\{["'^}]+'"\\}--[IVXL]+' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
 exited 1 in 51ms:

 succeeded in 51ms:
chapters/connections/thqg_preface_supplement.tex:2017:chapters of Parts~\ref{part:seven-faces}--VII of this monograph:
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_preface_supplement.tex | sed -n '2013,2019p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2013	
  2014	\bigskip
  2015	
  2016	The eight subsections of this section correspond to eight
  2017	chapters of Parts~\ref{part:seven-faces}--VII of this monograph:
  2018	
  2019	\begin{center}


thinking
**Searching for patterns**

I’m thinking about the strengths of the findings and whether similar patterns show up in other volumes. I might want to check if there are plural references in the conclusions, like “Parts I–VI.” It could be useful to search for specific formats across all volumes, such as “--VII,” “--VI,” or “Parts I–.” 

I wonder if it would help to inspect if multiple parts appear on the same line, especially in current files. This might not be necessary for the report, but it could make justifications stronger later on.
thinking
**Identifying mixed references**

I’m noticing that line 2017 might use a mix of a proper reference and a hardcoded “VII” in the format “Parts\ref{part:seven-faces}--VII.” This seems especially clear. I wonder if there are other mixed ranges that haven’t been captured yet due to the singular format, like “Partref--VII.” 

I think it would be a good idea to search specifically for “Part\\ref{” followed by a Roman numeral. I’ll run a search query across the volumes to see what comes up!
exec
/bin/zsh -lc "rg -n 'Part~\\\\ref\\{["'^}]+'"\\}--[IVXL]+' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Part~\\\\ref\\{["'^}]+'"\\}--[IVXL]+' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'Part~\\\\ref\\{["'^}]+'"\\}--[IVXL]+' chapters/" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 52ms:

codex
The live surface is narrow now. I’m doing one final non-backup scan so the report isn’t distorted by `.bak` noise and doesn’t miss a live hit hidden past the first-window grep.
exec
/bin/zsh -lc "find chapters -name '*.tex' "'! -name '"'*.bak' "'! -name '"'*.bak.*' -print0 | xargs -0 grep -n 'Part~[IVXL]\\|Chapter~[0-9]'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find chapters -name '*.tex' "'! -name '"'*.bak' "'! -name '"'*.bak.*' -print0 | xargs -0 grep -n 'Part~[IVXL]\\|Chapter~[0-9]'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find chapters -name '*.tex' "'! -name '"'*.bak' "'! -name '"'*.bak.*' -print0 | xargs -0 grep -n 'Part~[IVXL]\\|Chapter~[0-9]'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/theory/quantum_groups_foundations.tex:84:Drinfeld, ``Quantum groups'' (ICM Berkeley 1986), Theorem~2; see also Chari--Pressley, \emph{A Guide to Quantum Groups}, Chapter~4.2. The proof is a direct consequence of quasi-triangularity and the coassociativity of $\Delta$.
chapters/theory/introduction.tex:34: \item $E_1$-chiral algebras (Volume~II, Part~III): associative factorization on $\mathbb{C} \times \mathbb{R}$, encoding the ordered/topological sector. Representation categories are monoidal.
chapters/theory/introduction.tex:157:(Volume~I, Part~II) organizes the resulting landscape:
chapters/theory/braided_factorization.tex:89:fewer pole order than the OPE). See Volume~II, Chapter~11 for the
chapters/connections/cy_holographic_datum_master.tex:922:This part of Vol~III mirrors Vol~I Part~III and Vol~II Part~III. The
chapters/connections/cy_holographic_datum_master.tex:931:\item \emph{Vol~I, Part~III:} the binary collision residue of a chiral
chapters/connections/cy_holographic_datum_master.tex:936:\item \emph{Vol~II, Part~III:} the binary collision residue of a
chapters/connections/cy_holographic_datum_master.tex:1009:Vol~III. Subsequent chapters in Part~V record the geometric Langlands
chapters/examples/k3_times_e.tex:966:of Chapter~66) and apply to the $K3 \times E$ tower.
chapters/examples/toroidal_elliptic.tex:94:The Arnold relation (Vol~I, Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Vol~I, Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex developed in Vol~I, Part~I (Vol~I, Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
chapters/examples/toroidal_elliptic.tex:5492:of Chapter~66) and apply to the $K3 \times E$ tower.
chapters/examples/quantum_group_reps.tex:342:In the Dimofte framework (Volume~II, Part~III), the BPS algebra
chapters/examples/quantum_group_reps.tex:546:(Volume~I, Part~II) acquires categorical meaning through the
 succeeded in 98ms:
chapters/theory/locality.tex:284:Costello--Gwilliam~\cite[Chapter~5, \S5.4]{CG17} prove that a
chapters/theory/foundations_recast_draft.tex:721:\cite{BD04}, Chapter~3.
chapters/theory/foundations_recast_draft.tex:732:Chapter~4).
chapters/theory/raviolo.tex:498:\emph{Absolute convergence.} Item~(b) asserts one-loop finiteness: all one-loop Feynman integrals converge in the HT gauge. For theories with $d' = 1$ topological direction, the power-counting of~\cite{GRW21} shows that this implies finiteness at \emph{all} loop orders: the superficial degree of divergence of an $L$-loop graph is $\delta = (1 - d')L = 0$ for $L = 0$ and $\delta < 0$ for $L \ge 2$, so the only potential divergences are at one loop, and these are finite by hypothesis. This power-counting bound applies to theories with propagator of type $(0,1)$ in the holomorphic direction and distributional in the topological direction. For such theories, the loop superficial degree of divergence is $\delta = (1-d')L$ where $d' = \dim_\C$ of the holomorphic factor; at $d' = 1$ this gives $\delta = 0$ for all $L$, so only logarithmic divergences can appear and these are removed by the one-loop renormalization hypothesis. See \cite[Chapter~9]{CG17} and \cite[Theorem~3.1]{GRW21} for the precise class of theories. After FM compactification of the holomorphic factor, the integrand acquires at worst logarithmic singularities along boundary divisors. Concretely:
chapters/theory/factorization_swiss_cheese.tex:2148:Lurie \cite{HA}, Chapter~5.5, with two strata: the open stratum
chapters/connections/relative_feynman_transform.tex:846:\cite{LV12}, Chapter~13.
chapters/connections/relative_feynman_transform.tex:1452:(Chriss--Ginzburg~\cite{CG97}, Chapter~8): the convolution
chapters/connections/spectral-braiding.tex:969:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
chapters/connections/conclusion.tex:987:\subsection{The Part~VII frontier chapters}
chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
chapters/connections/bar-cobar-review.tex:465:The convolution dg Lie algebra $\mathrm{Conv}(\cC, \cA)$ arises in two equivalent ways: (i)~when $\cC = \barB(\cA)$ is the bar construction, the cooperad structure on $\barB(\cA)$ and the operad structure on $\mathrm{End}_\cA$ give an $L_\infty$-algebra via the operadic convolution of \cite{LV12}, Chapter~6; (ii)~for a general conilpotent coalgebra $\cC$ and algebra $\cA$, the associative convolution product $f \star g = \mu_\cA \circ (f \otimes g) \circ \Delta_\cC$ on $\mathrm{Hom}(\cC, \cA)$ yields a dg Lie algebra by taking graded commutators. When $\cC = \barB(\cA)$, the two constructions agree because the cooperad structure on $\barB(\cA)$ is determined by the coalgebra structure via the cofree property. In the representability theorems above, we use convention~(ii) for general $\cC$ and convention~(i) when $\cC = \barB(\cA)$.
chapters/connections/ordered_associative_chiral_kd_frontier.tex:83:In Chriss--Ginzburg \cite{chriss-ginzburg} Chapter~3, the orbit stratification
chapters/connections/hochschild.tex:913:\cite[Chapter~6]{CG17}:
chapters/connections/hochschild.tex:1079:theorem~\cite[Chapter~6]{CG17}, a locally constant factorization
chapters/connections/spectral-braiding-core.tex:3469:operads (Loday--Vallette \cite{LV12}, Chapter~10; generalized
 succeeded in 206ms:
chapters/theory/higher_genus_complementarity.tex:582:Beilinson--Drinfeld~\cite[Chapter~4]{BD04} proved the $g=0$ case;
chapters/theory/higher_genus_complementarity.tex:2165:Costello--Gwilliam~\cite{CG17}, Volume~2, Chapter~5).
chapters/theory/ordered_associative_chiral_kd.tex:5970:hierarchy of Volume~II, Part~VI\@. The correspondence is:
chapters/theory/ordered_associative_chiral_kd.tex:7549:of Part~VII\@: genuinely $\mathsf{E}_1$-chiral algebras
chapters/theory/ordered_associative_chiral_kd.tex:7752:non-formality (Volume~II, Part~VII).
chapters/theory/configuration_spaces.tex:1212:the Beilinson--Drinfeld framework \cite[Chapter~3]{BD04}.
chapters/theory/configuration_spaces.tex:3525:% (see Beilinson--Drinfeld~\cite[Chapter~3]{BD04}).
chapters/theory/configuration_spaces.tex:4838:chiral/Ran-space correspondence is developed in \cite[Chapter~3]{BD04}; the
chapters/theory/configuration_spaces.tex:4857:formalism \cite[Chapter~3]{BD04} together with factorization-homology
chapters/theory/algebraic_foundations.tex:1293:\textup{(Beilinson--Drinfeld \cite[Chapter~3]{BD04})}
chapters/theory/koszul_pair_structure.tex:441:\emph{Step 4}: By Stokes' theorem, $\int_{\overline{C}_n} d(\cdots) = \int_{\partial\overline{C}_n}(\cdots)$. Each codimension-$1$ boundary stratum $\overline{C}_i \times \overline{C}_j$ (with $i + j = n + 1$) contributes a composition $m_i \circ_k m_j$ (with $k$ indexing the insertion point). The sign $(-1)^{rs+t}$ in the $A_\infty$ relation arises from the Koszul sign rule applied to the desuspended generators $s^{-1}f_i$: the desuspended map $b_s$ has degree~$+1$, so permuting $s^{-1}f_1, \ldots, s^{-1}f_r$ past $b_s$ contributes $(-1)^r$; inserting $b_s$ into position $(r{+}1)$ among the desuspended outputs and accounting for the $s$ inputs with their signs gives the total sign $(-1)^{rs+t}$ (see~\cite{LV12}, \S9.2.8 for the complete sign derivation). The sum over all boundary strata exhausts all compositions, and $\partial^2 = 0$ on $\overline{C}_n$ ensures the total contribution vanishes. See~\cite{LV12}, Chapter~9 for the complete operadic argument. \qedhere
chapters/theory/bar_construction.tex:1972:(Reutenauer \cite[Chapter~9]{Reutenauer93};
chapters/theory/hochschild_cohomology.tex:433:This identification is classical for associative algebras \cite{Loday98}; the chiral extension follows from the factorization structure of the loop space \cite[Chapter~5]{CG17}.
chapters/theory/hochschild_cohomology.tex:1128:Costello--Gwilliam~\cite[Chapter~5]{CG17}.
chapters/theory/hochschild_cohomology.tex:1454:parallel result appears in Costello--Gwilliam~\cite[Chapter~5]{CG17}.
chapters/theory/cobar_construction.tex:347:$\mathcal{D}$-modules \cite[Chapter~4]{KS90}.
chapters/theory/cobar_construction.tex:1374:At the level of $\mathcal{D}$-modules on $\overline{C}_n(X)$, the bar and cobar differentials are flat connections (the bar complex is a complex of holonomic $\mathcal{D}$-modules by Lemma~\ref{lem:bar-holonomicity}). Verdier duality is an exact contravariant involution on $D^b_{\mathrm{hol}}(\mathcal{D}_{\overline{C}_n(X)})$ that sends a flat connection $\nabla$ to the adjoint connection $\nabla^\dagger$ (see~\cite{KS90}, Chapter~4).
chapters/theory/higher_genus_foundations.tex:1769:(see \cite[Chapter~7]{LV12} for the operadic framework):
chapters/theory/higher_genus_foundations.tex:2641:(Lurie~\cite[Chapter~5]{HA}, Ayala--Francis~\cite{AF15}).
chapters/theory/bar_cobar_adjunction_inversion.tex:2043:This is a standard spectral sequence associated to a filtered complex (Weibel~\cite{Weibel94}, Chapter~5). We verify the key properties:

thinking
**Investigating surface matches**

I'm checking if the `higher_genus_complementarity` line changed from 2162 to 2165 due to line number drift. It's important that we only care about this change. Now, I want to search for `Parts\ref...--VII` in the non-bak live files and I found one instance. Then, I searched for `Chapter\texttt` and found two. I also want to check for any additional `PartVII` references, and I'll search for `Parts[IVXL]` across all live files to ensure there are no unflagged items. Let's keep this quick.
exec
/bin/zsh -lc "find chapters -name '*.tex' "'! -name '"'*.bak' "'! -name '"'*.bak.*' -print0 | xargs -0 rg -n 'Parts~[IVXL]'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find chapters -name '*.tex' "'! -name '"'*.bak' "'! -name '"'*.bak.*' -print0 | xargs -0 rg -n 'Parts~[IVXL]'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "find chapters -name '*.tex' "'! -name '"'*.bak' "'! -name '"'*.bak.*' -print0 | xargs -0 rg -n 'Parts~[IVXL]'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 53ms:
chapters/connections/conclusion.tex:990:Part~VII extends the proved core of Parts~I--VI into conditional,
 exited 1 in 51ms:






thinking
**Analyzing instances and violations**

I'm considering the user's request to count only live instances checked while excluding false positives marked as `.bak`. They mentioned 76 total instances checked, so that’s what I should go with. I’ll compute that there are 24 violations found, leading to a result of FAIL. I think I’ll present the summary like this: "Instances checked: 76 | Violations found: 24 | Verdict: FAIL." I’ll also need to make sure to label the severity correctly for certain lines as HIGH or MEDIUM.
thinking
**Considering file naming and references**

I’m thinking about using short file names, and it seems the clickable label could be `ordered_associative_chiral_kd.tex`, which sounds good. I also need to make sure to note the exact text for `Volume II's Part VII`. Additionally, I should mention the reference for the line marked as `[HIGH] [thqg_preface_supplement.tex](...:2017)` concerning the mixed compliant/hardcoded range: `Parts\ref{part:seven-faces}--VII`. Lastly, I’ll ensure that line 2055 is treated separately.
thinking
**Classifying document sections**

I’m considering whether to classify `conclusion.tex:987` as HIGH or MEDIUM. It seems like it would depend on the section heading, right? I think it’s probably more structural, so maybe that leans toward a certain classification. But then again, I want to make sure I'm being consistent and careful about how I categorize it. It's a bit tricky to find that balance. Let’s see what makes the most sense!
thinking
**Ensuring clickable link syntax**

I need to mention "hardcoded chapter label text" as sibling defects, which are still significant. Let’s ensure that the clickable link syntax is correct and includes the absolute path followed by a line after the colon. An example would be `[ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5970)`. This looks good!
thinking
**Finalizing the format**

I don’t think I need to create separate sections; a simple list and summary will work. I might title it something like `- [HIGH] ...`. I need to keep it concise, ensuring it doesn't exceed 70 lines. Given my math, 24 bullets, plus one note and two summary lines would total 27 lines, which is fine. I’ll focus on producing a concise final version!
codex
- [HIGH] [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5970) — hardcoded cross-volume part reference: `Volume~II, Part~VI`.
- [HIGH] [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7549) — hardcoded part reference: `Part~VII`.
- [HIGH] [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:7752) — hardcoded cross-volume part reference: `Volume~II, Part~VII`.
- [HIGH] [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3796) — hardcoded cross-volume part reference: `Volume~II's Part~VII`.
- [HIGH] [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1788) — hardcoded cross-volume part reference: `Vol~II, Part~IV`.
- [HIGH] [thqg_introduction_supplement_body.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1620) — hardcoded frontier part in a list otherwise using `Part~\ref{...}`: `(Part~VII)`.
- [HIGH] [thqg_preface_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2017) — mixed compliant/hardcoded range: `Parts~\ref{part:seven-faces}--VII`.
- [HIGH] [thqg_preface_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:2055) — hardcoded part reference: `Part~VII pushes`.
- [HIGH] [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:987) — hardcoded part in section title: `The Part~VII frontier chapters`.
- [HIGH] [conclusion.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex:990) — hardcoded part references in prose: `Part~VII extends the proved core of Parts~I--VI`.
- [HIGH] [dnp_identification_master.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:540) — sibling chapter-reference defect found in context scan: literal label name `Chapter~\texttt{ch:genus1-seven-faces}` instead of a chapter `\ref`.
- [HIGH] [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:34) — hardcoded cross-volume part reference: `Volume~II, Part~III`.
- [HIGH] [introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:157) — hardcoded cross-volume part reference: `Volume~I, Part~II`.
- [HIGH] [braided_factorization.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:89) — hardcoded cross-volume chapter reference: `Volume~II, Chapter~11`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:922) — hardcoded cross-volume part references: `Vol~I Part~III and Vol~II Part~III`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:931) — hardcoded cross-volume part reference: `Vol~I, Part~III`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:936) — hardcoded cross-volume part reference: `Vol~II, Part~III`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1006) — sibling chapter-reference defect found in context scan: literal label name `Chapter~\texttt{ch:genus1-seven-faces}`.
- [HIGH] [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1009) — hardcoded local part reference: `Part~V`.
- [HIGH] [k3_times_e.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:966) — hardcoded chapter number in cross-volume reference: `Chapter~66`.
- [HIGH] [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:94) — hardcoded cross-volume part reference: `Vol~I, Part~I`.
- [HIGH] [toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5492) — hardcoded chapter number in cross-volume reference: `Chapter~66`.
- [HIGH] [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:342) — hardcoded cross-volume part reference: `Volume~II, Part~III`.
- [HIGH] [quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:546) — hardcoded cross-volume part reference: `Volume~I, Part~II`.

Excluded as false positives after context read: external bibliography chapter citations such as `\cite[Chapter~3]{BD04}` and non-live `.bak` artifact files under `chapters/`.

## Summary
Instances checked: 76 | Violations found: 24 | Verdict: FAIL
tokens used
83,100
