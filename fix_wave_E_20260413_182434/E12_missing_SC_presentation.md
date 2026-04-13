# E12_missing_SC_presentation (410s)

`SC^{ch,top}` was not presented as a full generators-and-relations operad. In the live Vol I surfaces, it was only given as an operation-space model.

- `PROBLEM` at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1220): the canonical definition gave operation spaces and componentwise composition, but no codimension-1 generators or codimension-2 relations. `EXACT edit applied`: inserted the new remark at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247) listing closed collision faces `\partial_S\FM_k(\bC)`, open interval-splitting faces in a Stasheff compactification of `E_1(m)`, mixed product faces in `\FM_k(\bC)\times E_1(m)`, and stating the codimension-2 relation families: Arnold--Orlik--Solomon, Stasheff, and mixed commuting squares. The remark also states explicitly that the full minimal presentation is still not written out there.

- `PROBLEM` at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1840): the proof of the operadic-center theorem called the `SC^{ch,top}` input the “explicit form,” which overstated the presentation. `EXACT edit applied`: changed that phrase to “the operation-space description of `\mathsf{SC}^{\mathrm{ch,top}}`.”

- `PROBLEM` at [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:1792): the duplicate live construction also gave only operation spaces, with no generator list, and could be read as if the ordered bar complex already carried the full Swiss-cheese structure. `EXACT edit applied`: inserted the new remark at [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:1832) stating that this is only an operation-space model, not a minimal generators-and-relations presentation and not by itself a full Swiss-cheese algebra structure on the ordered bar complex, then listing the same codimension-1 generator families and codimension-2 relation families.

- `PROBLEM` at [appendices/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:1697): the appendix duplicate had the same omission. `EXACT edit applied`: inserted the matching remark at [appendices/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:1737) with the same generator list and codimension-2 relation summary.

Verification was a targeted grep and line check. I did not run a full TeX build.


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
session id: 019d87c7-5771-7de3-a6b5-962d70a16416
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


Search for SC^{ch,top} generators-and-relations.
Is the operadic presentation explicit? With generators (codim-1 boundary strata) and
relations (codim-2)? If missing: add at least a remark listing the generators.
mcp startup: no servers
codex
I’m auditing the `SC^{ch,top}` presentation surface, starting with the required repo-wide constitutional files and then tracing every live mention of “generators”, “relations”, and boundary strata before I edit anything.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{Concordance with primary literature}
\label{chap:concordance}

\index{concordance|textbf}

This chapter is the constitution of the monograph. When chapters
disagree, this chapter governs. It records the five main theorems
with their precise status and locates every result against the
prior literature: what is proved, what is conditional, what
remains conjectural.

The governing principle is falsification: every claim in these three
volumes is presumed false until it appears below with an explicit
status tag and a proof reference or independent verification trail.
A theorem that contradicts the concordance is not a theorem; it is an
error in the chapter that states it. Omission from this chapter is
itself a verdict: what is not recorded here has not survived scrutiny.
The concordance does not summarize the monograph; the monograph
approximates the concordance.

 succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 51ms:
# Red-Team Summary of Vol1/Vol2 Claim Audit
## Scope
- Formal tagged claims catalogued: **4866**
- Volume I formal claims: **2841**
- Volume II formal claims: **2025**
- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.

## Status profile
- ProvedHere: **3801**
- Conjectured: **327**
- Heuristic: **35**
- ProvedElsewhere: **513**
- Conditional: **116**
- Open: **74**

## Risk profile
- medium: **1999**
- low: **1913**
- high: **807**
 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |

thinking
**Searching for relevant files**

I need to search for relevant files, probably looking at chapters like en_koszul_duality.tex or others with SC presentation. I'll specifically search for terms like SC^{ch,top}, generators, relations, and boundary strata. It seems using explorer would be a good idea. I also want to think about skills like deep-beilinson-audit and possibly cross-volume-propagation later. First, I should spawn the explorer to help locate those files and check the status.
codex
I’m using `deep-beilinson-audit` first to locate the explicit Swiss-cheese claim surface, then `cross-volume-propagation` only if the same presentation recurs outside the target file.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: cross-volume-propagation
description: Use after any mathematical wording, status, label, terminology, or formula change that may recur across Volumes I, II, and III, compute layers, tests, notes, or superseded files. This is the Codex-native equivalent of `/propagate` from `CLAUDE.md`.
---

# Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Sweep

Search all live surfaces that may still advertise the old claim:

- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`
- `~/calabi-yau-quantum-groups`
- `compute/`
- `compute/tests/`
- relevant notes, standalones, or superseded files if they still mislead future audits


thinking
**Searching and editing files**

I'm looking to search for relevant information and potentially edit one specific file. It seems like I can only make minimal edits to the targeted file. I'll run a search for terms like "SC^{ch,top}," "swiss-cheese," "codim-1," and "boundary strata," and consider using parallel executions for efficiency. Overall, it's about being precise and keeping my edits truthful and minimal while working within the scope.
codex
I’ve loaded the constitutional surface. Next I’m pinning the exact file and label where `SC^{ch,top}` is introduced, then I’ll test whether the text actually states generators and codimension-two relations or only gestures at them.
exec
/bin/zsh -lc "rg -n \"thm:bar-swiss-cheese|princ:sc-two-incarnations|topologization|SC\\"'^!|Lie'"\\"'^c, Ass'"\\"'^c|shuffle-mixed|derived center|bulk, boundary" chapters appendices frontmatter -g '"'*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"SC\\"'^'"\\{ch,top\\}|SC\\"'^'"\\{ch\\}|Swiss[- ]cheese|swiss[- ]cheese|two-colou|two-colou?r|boundary strata|codim-1|codimension-1|codim-2|codimension-2|generators and relations|generator|relation\" chapters appendices frontmatter -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: frontmatter: No such file or directory (os error 2)
chapters/examples/deformation_quantization.tex:722:(boundary deformation data); the \emph{derived center}
chapters/examples/deformation_quantization.tex:2124:chiral algebra of a Landau--Ginzburg B-model, the derived center
appendices/nonlinear_modular_shadows.tex:1012:In the chiral derived center $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k)$
appendices/nonlinear_modular_shadows.tex:1122:In the chiral derived center, the cubic shadow
appendices/nonlinear_modular_shadows.tex:1255:In the chiral derived center, the contact archetype exhibits a
appendices/nonlinear_modular_shadows.tex:1432:The mixed archetype is the first where the derived center carries
appendices/ordered_associative_chiral_kd.tex:4164:derived center, as the pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)$
chapters/examples/kac_moody.tex:25:PBW filtrations, and the derived center of
chapters/connections/thqg_open_closed_realization.tex:2:% The open/closed realization: chiral derived center as universal bulk
chapters/connections/thqg_open_closed_realization.tex:8:% algebra? The derived center Z^der_ch(A) resolves this by realizing
chapters/connections/thqg_open_closed_realization.tex:13:\section{The open/closed realization: chiral derived center as universal bulk}
chapters/connections/thqg_open_closed_realization.tex:15:\index{derived center!chiral|textbf}
chapters/connections/thqg_open_closed_realization.tex:41:\subsection{The chiral endomorphism operad and the algebraic derived center}
chapters/connections/thqg_open_closed_realization.tex:289:\begin{definition}[Chiral derived center]
chapters/connections/thqg_open_closed_realization.tex:291:\index{derived center!chiral|textbf}
chapters/connections/thqg_open_closed_realization.tex:292:The \emph{chiral derived center} of $\cA$ is the cohomology
chapters/connections/thqg_open_closed_realization.tex:302:for $n \notin \{0, 1, 2\}$, so the derived center is a
chapters/connections/thqg_open_closed_realization.tex:318:\begin{definition}[Genus-$g$ chiral derived center]
chapters/connections/thqg_open_closed_realization.tex:320:\index{derived center!genus $g$|textbf}
 exited 2 in 50ms:
Total output lines: 4599

rg: frontmatter: No such file or directory (os error 2)
appendices/general_relations.tex:17:Jacobi identity & Arnold--Orlik--Solomon relations \\
appendices/general_relations.tex:67:\chapter{\texorpdfstring{Arnold relations for small $n$}{Arnold relations for small n}}
appendices/general_relations.tex:68:\label{app:arnold-relations-small-n}
appendices/general_relations.tex:70:Arnold relations for logarithmic forms:
appendices/general_relations.tex:77:\emph{$n = 4$ (four 3-term Arnold relations, one for each triple $\{i,j,k\} \subset \{1,2,3,4\}$).}
appendices/general_relations.tex:84:These four relations (each involving forms that share an index) reduce $\binom{6}{2} = 15$ naive products to $\dim H^2(C_4(\mathbb{C})) = 11$ independent classes. Products of disjoint pairs such as $\eta_{12} \wedge \eta_{34}$ are \emph{not} constrained by Arnold relations and remain independent.
appendices/general_relations.tex:86:\emph{$n = 5$ ($\binom{5}{3} = 10$ independent quadratic relations).}
appendices/general_relations.tex:87:These are the ten three-term Arnold relations $\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0$, one for each triple $\{i,j,k\} \subset \{1,2,3,4,5\}$. All higher-degree relations (such as the degree-3 relations in $H^3(C_5(\mathbb{C}))$) are consequences of these quadratic relations, by the Orlik--Solomon theorem.
appendices/general_relations.tex:91:by the ideal generated by $\binom{n}{3}$ quadratic Arnold relations (one for each triple $i < j < k$).
appendices/general_relations.tex:97:\chapter{\texorpdfstring{Curved $A_\infty$ relations: complete formulas}{Curved A infty relations: complete formulas}}
appendices/general_relations.tex:100:For reference, we collect the complete curved $A_\infty$ relations. An $A_\infty$ algebra 
appendices/general_relations.tex:125:If $\mu_0 \in Z(\mathcal{A})$ (i.e., $m_2(\mu_0 \otimes a) = m_2(a \otimes \mu_0)$ for all $a$), then the $n=1$ relation gives:
appendices/homotopy_transfer.tex:102:\emph{Verification of $\Ainf$-relations.}
appendices/homotopy_transfer.tex:103:The $\Ainf$-relation at degree~$n$ for $\{\tilde{m}_k\}$ requires:
appendices/homotopy_transfer.tex:104:\begin{equation}\label{eq:ainfty-relation}
appendices/homotopy_transfer.tex:111:\item a term $\id_V$, which together with the $\Ainf$-relations for $\{m_k\}$
appendices/homotopy_transfer.tex:117:relation for } \{m_k\}) \circ \iota^{\otimes n} = 0$, while the terms

thinking
**Inspecting sections for editing**

I need to check a large output and find the relevant section around line 1196. It looks like I should focus on editing the en_koszul_duality.tex section, specifically looking at definitions and theorem surfaces. I might also want to search for "generated by codim-1" to find any remarks that aren't explicit. I’ll need to review the text from sections 1196 to 1310 and possibly later around 6280 to see if there are any comments about generators and relations. I’ll use sed to help with this.
codex
The main live surface is `chapters/theory/en_koszul_duality.tex`. I’m reading the Swiss-cheese section itself now, plus the later remarks that may already admit the presentation is only schematic.
exec
/bin/zsh -lc "sed -n '1520,1825p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1196,1328p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6288,6336p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6748,6795p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Proposition~\ref{prop:en-formality};
see also Remark~\ref{rem:en-scope}).
The \emph{ordered} bar complex
$\barB^{\mathrm{ord}}(\cA)=T^c(s^{-1}\bar\cA)$ is a
single-coloured $\Eone$-chiral dg coalgebra: the differential
comes from holomorphic collision residues on $\FM_k(\bC)$ and
the deconcatenation coproduct comes from ordered interval
splitting on $\Conf_k(\bR)$
(Theorem~\ref{thm:bar-swiss-cheese}). The actual
$\mathsf{SC}^{\mathrm{ch,top}}$ datum appears only on the
derived center pair
$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$; the symmetric bar
$\barB^{\Sigma}(\cA)$ of Theorem~A is recovered by $R$-twisted
$\Sigma_n$-coinvariants and uses the coshuffle coproduct
instead. At higher genus the fibrewise differential
$\dfib$ is curved with $\dfib^{\,2}=\kappa(\cA)\cdot\omega_g$
but is \emph{not} a coderivation; flatness and the coderivation
property are restored only by the period-corrected differential
$\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
(Remark~\ref{rem:sc-higher-genus}).
 succeeded in 51ms:
\section{The Swiss-cheese case: holomorphic--topological
factorization}
\label{sec:swiss-cheese}
\index{Swiss-cheese operad|textbf}
\index{bar complex!$\Eone$-chiral coassociative coalgebra|textbf}
\index{holomorphic--topological!factorization|textbf}

The dimensional ladder has so far been one-dimensional: $n = 1$
(associative), $n = 2$ (chiral), $n = 3$ (Chern--Simons). But the
ordered bar complex $\barB^{\mathrm{ord}}(\cA)$ of this monograph
already carries a \emph{mixed}
structure that does not fit on this line. The differential
$d_{\barB}$ lives on $\FM_k(\bC)$ (the $n = 2$ slot); the
coassociative coproduct~$\Delta$ lives on $\Conf_k(\bR)$ (the
$n = 1$ slot). Together, a bar element of degree~$k$ is
parametrized by
\begin{equation}\label{eq:bar-product-space}
\FM_k(\bC) \times \Conf_k(\bR),
\end{equation}
the product of holomorphic and topological configuration spaces.
 succeeded in 51ms:
\end{remark}

\begin{remark}[Position in the dimensional ladder]
\label{rem:sc-dimensional-ladder}
The Swiss-cheese operad $\mathsf{SC}^{\mathrm{ch,top}}$ is the
$(n_{\mathrm{hol}}, n_{\mathrm{top}}) = (2, 1)$ entry in a
two-parameter family of mixed operads. The one-parameter diagonal
$n_{\mathrm{hol}} = n$, $n_{\mathrm{top}} = 0$ recovers the $\En$
ladder of this chapter. The off-diagonal entries mix holomorphic
and topological factorization in different dimensions. The
classical Swiss-cheese of Voronov~\cite{Voronov99} is the
$(n, n-1)$ case; ours is the holomorphic refinement at $(2, 1)$.
\end{remark}


%================================================================
% SECTION: THE CHIRAL CENTER THEOREM VIA THE OPERADIC ROUTE
%================================================================

\section{The chiral center theorem: operadic proof}
 succeeded in 52ms:
$\ChirHoch^1(V_k(\fsl_2)) \cong \fsl_2$, see
Proposition~\ref{prop:gerstenhaber-sl2-bracket}.

\textbf{Part~(ii).}
An $\mathsf{E}_3$ structure on a chain complex $C$ requires an
action of $\Conf_k(\bR^3)$ on $C^{\otimes k}$ for all~$k$,
compatible with the $\mathsf{FM}_3$ operad structure. The bar
complex $\barB^{\Sigma}(\cA)$ is built from
$\Conf_k(\bC) = \Conf_k(\bR^2)$;
no embedding $\bR^3 \hookrightarrow \bC$ exists
that would provide the additional topological data.
The Swiss-cheese operad $\SCchtop$ has
$\Etwo$ acting on the closed holomorphic sector (points in $\bC$)
and $\Eone$ acting on the open topological sector (points in $\bR$);
these are \emph{different colors} of a colored operad.
Dunn additivity ($\mathsf{E}_m \otimes \mathsf{E}_n
\simeq \mathsf{E}_{m+n}$, \cite{Dunn88})
applies to the tensor product of operads acting on the
\emph{same} underlying object, not to different colors of a
colored operad.

thinking
**Searching boundary strata**

I need to search for "codimension-1 boundary strata" in the SC section, specifically looking around line 2342. I wonder what insights I can find there! It seems like a focused task, so I'll try to gather the appropriate context and details for better understanding. I should be ready to explore the outcomes and see how they connect to my analysis. Let's see what I can uncover!
exec
/bin/zsh -lc "sed -n '2618,2705p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2320,2398p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1218,1278p' chapters/theory/en_koszul_duality.tex | nl -ba -v1218" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6288,6310p' chapters/theory/en_koszul_duality.tex | nl -ba -v6288" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
To summarize the difficulties identified in
Remark~\ref{rem:chiral-spectral-parameter-difficulty} at the level
of the complete proof:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Steps 1--2} (algebraic/chain-level) are parallel to the
 topological case, with Arnold relations replacing smooth Stokes.
 The key input is the FM compactification of $\Conf_k(X)$, which
 provides the same combinatorial structure as $\FM_k(\bR^2)$ but
 with holomorphic forms.
\item \emph{Step 3} (geometric realization) requires the recognition
 theorem (F4/F5), which itself requires homotopy-Koszulity of
 $\mathsf{SC}^{\mathrm{ch,top}}$. The proof of
 homotopy-Koszulity uses Kontsevich formality, which is the single
 deepest input. In the topological case, Koszulity of the
 classical Swiss-cheese operad suffices.
\item \emph{Step 4} (comparison) requires that the $\Etwo$-structure
 from the operadic center and the $\Etwo$-structure from braces
 agree. In the topological case, this is part of the Deligne
 conjecture proof. In the chiral case, the comparison
 also requires that the configuration-space forms are compatible with the
 succeeded in 52ms:
\;:=\;
\sum_{\substack{S_1 \sqcup \cdots \sqcup S_k \sqcup T \\
= \{z_1, \ldots, z_N\}}}
\pm\;
\operatorname{Res}_{\substack{w_1 \to z_{S_1} \\
\vdots \\ w_k \to z_{S_k}}}
f(w_1, \ldots, w_k, z_T)
\prod_{j=1}^{k} g_j(z_{S_j}),
\end{equation}
where the sum is over ordered partitions of the input set, the
residue is at the collision loci $w_j \to z_{S_j}$ in
$\FM_k(\bC) \subset \overline{C}_{k+N}(X)$, and the sign $\pm$
follows the Koszul convention for the desuspended tensor product.
\end{definition}

\begin{proposition}[Brace operations from the operadic center;
\ClaimStatusProvedHere]
\label{prop:braces-from-center}
\index{brace operations!from operadic center}
The brace operations of
 succeeded in 51ms:
  6288	Proposition~\ref{prop:en-formality};
  6289	see also Remark~\ref{rem:en-scope}).
  6290	The \emph{ordered} bar complex
  6291	$\barB^{\mathrm{ord}}(\cA)=T^c(s^{-1}\bar\cA)$ is a
  6292	single-coloured $\Eone$-chiral dg coalgebra: the differential
  6293	comes from holomorphic collision residues on $\FM_k(\bC)$ and
  6294	the deconcatenation coproduct comes from ordered interval
  6295	splitting on $\Conf_k(\bR)$
  6296	(Theorem~\ref{thm:bar-swiss-cheese}). The actual
  6297	$\mathsf{SC}^{\mathrm{ch,top}}$ datum appears only on the
  6298	derived center pair
  6299	$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$; the symmetric bar
  6300	$\barB^{\Sigma}(\cA)$ of Theorem~A is recovered by $R$-twisted
  6301	$\Sigma_n$-coinvariants and uses the coshuffle coproduct
  6302	instead. At higher genus the fibrewise differential
  6303	$\dfib$ is curved with $\dfib^{\,2}=\kappa(\cA)\cdot\omega_g$
  6304	but is \emph{not} a coderivation; flatness and the coderivation
  6305	property are restored only by the period-corrected differential
  6306	$\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
  6307	(Remark~\ref{rem:sc-higher-genus}).
 succeeded in 51ms:
  1218	$\mathsf{SC}^{\mathrm{ch,top}}$.
  1219	
  1220	\begin{definition}[Holomorphic--topological Swiss-cheese operad]
  1221	\label{def:SC}
  1222	\index{Swiss-cheese operad!definition}
  1223	Define the two-colored topological operad $\mathsf{SC}^{\mathrm{ch,top}}$
  1224	with colors $\{\mathsf{ch}, \mathsf{top}\}$ (closed/holomorphic
  1225	and open/topological) by:
  1226	\begin{enumerate}[label=\textup{(\roman*)}]
  1227	\item \emph{Closed output, closed inputs only:}
  1228	 $\mathsf{SC}^{\mathrm{ch,top}}
  1229	 ((\mathsf{ch},\ldots,\mathsf{ch});\, \mathsf{ch})
  1230	 := \FM_k(\bC)$.
  1231	\item \emph{Open output, mixed inputs:}
  1232	 $\mathsf{SC}^{\mathrm{ch,top}}
  1233	 ((\underbrace{\mathsf{ch},\ldots}_{k},
  1234	 \underbrace{\mathsf{top},\ldots}_{m});\, \mathsf{top})
  1235	 := \FM_k(\bC) \times E_1(m)$.
  1236	\item \emph{No open-to-closed:}
  1237	 $\mathsf{SC}^{\mathrm{ch,top}}

thinking
**Investigating codimension definitions**

I need to check for any explicit mentions of codim-1 generators in the document. I'll search specifically within the file for terms like "codimension-1," "codimension-2," and "boundary strata." This way, I can ensure I'm gathering all relevant information related to those definitions. It's important to be thorough so that I don't miss anything significant! Let’s see what I can find.
exec
/bin/zsh -lc "rg -n \"codimension-1|codim-1|codimension-2|codim-2|boundary strata|generator|relation\" chapters/theory/en_koszul_duality.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"SC\\"'^'"\\{ch,top\\}|SCchtop|Swiss-cheese operad\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1199:\index{Swiss-cheese operad|textbf}
1217:\emph{two-colored} operad: the Swiss-cheese operad
1220:\begin{definition}[Holomorphic--topological Swiss-cheese operad]
1222:\index{Swiss-cheese operad!definition}
1250:\index{Swiss-cheese operad!on derived center, NOT on bar}
1416:\index{Swiss-cheese operad!promotion from chiral algebra}
1469:\index{Swiss-cheese operad!curved|textbf}
1524:The Swiss-cheese operad $\mathsf{SC}^{\mathrm{ch,top}}$ is the
1543:\index{Swiss-cheese operad!center theorem}
1549:center} of an open-color algebra~$\cA$ in the Swiss-cheese operad
1554:classical Swiss-cheese operad. The chiral version requires the
1591:The Swiss-cheese operad $\mathsf{SC}^{\mathrm{ch,top}}$
1599:\index{Swiss-cheese operad!Koszul dual cooperad|textbf}
1799:of the holomorphic--topological Swiss-cheese operad, with
2441:\textup{(1)}~the classical Swiss-cheese operad is Koszul
2632: classical Swiss-cheese operad suffices.
2805:formality of the Swiss-cheese operad
2912:% TOPOLOGIZATION: SC^{ch,top} + SUGAWARA = E_3
6685: Swiss-cheese operad $\SCchtop$, which governs the
6693: $\SCchtop \not\simeq \mathsf{E}_3$.
 succeeded in 51ms:
9:relations with the Totaro relations, and chiral Koszul duality with
40:singularities are controlled by Arnold relations, and the bar-cobar
46:\emph{Totaro relations}, and the bar-cobar adjunction governs
80: closed $(n{-}1)$-form and collision relations governed by the Totaro
120:the Arnold generators on $\Conf_k(\bC)$ are the Totaro generators
190:generators-and-relations presentation due to Arnold ($n = 2$, i.e., $\bR^n = \bC$) and
197:\index{Arnold relations!presentation}
200:$1 \leq i < j \leq k$, subject to the \emph{Arnold relations}:
214:\index{Totaro relations|textbf}
219:$1 \leq i \neq j \leq k$, subject to the relations:
223:\item \textup{(Totaro relations)}\quad
233:oriented generator of $H^1(\Conf_2(\bR^2))$, one recovers Arnold's
234:three-term relation on $\Conf_k(\bC)$. By contrast, $n = 1$ is the
245:relations among these pullbacks are generated by the three-term
246:relation (ii).
251:\index{Arnold relations!as Totaro specialization}
253:The classical Arnold generators on $\Conf_k(\bC)$ are Totaro
254:generators at $n = 2$; our chiral bar complex uses $n = 2$:
291:corners whose boundary strata are indexed by nested partitions
299:\index{Fulton--MacPherson!boundary strata}
exec
/bin/zsh -lc "sed -n '1938,1988p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(d_{\mathrm{fact}}\phi)(z_1, \ldots, z_{k-1})
= \sum_{1 \leq i < j \leq k}
(-1)^{\epsilon(i,j)}\,
\operatorname{Res}_{z_i = z_j}
\bigl[\phi(\ldots, z_i, \ldots, z_j, \ldots)
\cdot \mu(a_i, a_j)\bigr],
\]
where $\epsilon(i,j)$ is the Koszul sign from permuting $a_i$ past
$a_{i+1}, \ldots, a_{j-1}$. This is the factorization component
$d_{\mathrm{fact}}$ from
Theorem~\ref{thm:chiral-hochschild-differential}: the
residue extraction at collision divisors $D_{ij} \subset
\partial\FM_k(\bC)$ using the chiral product. The signs agree
because both are determined by the codimension-1 boundary
orientation of $\FM_k(\bC)$ and the Koszul convention for
graded-symmetric tensor products.

\emph{(c.3) Configuration-space differential.}
The de~Rham differential $d_{\mathrm{dR}}$ on $\FM_k(\bC)$ acts
on the logarithmic form factor~$\omega$ in

thinking
**Inspecting generators and geometry**

I need to take a closer look at the definitions or remarks related to listing generators from codim-1 boundary strata. I could possibly refer to FM boundary strata and interval splitting. It's essential I have an accurate list of generators of SC^{ch,top} and understand the geometry involved. I might need to check around 291 on FM codim-1 boundary strata, focusing on the earlier section regarding general FM stratification to ensure proper terminology.
exec
/bin/zsh -lc "sed -n '286,336p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\times \prod_{|S| \geq 2} [0, \infty]
\]
recording positions, relative directions
$\theta_{ij} = (x_i - x_j)/|x_i - x_j| \in S^{n-1}$,
and relative distances. The result is a smooth manifold with
corners whose boundary strata are indexed by nested partitions
of $\{1, \ldots, k\}$, the same combinatorial data as the
Stasheff associahedron ($n = 1$) or the FM operad ($n \geq 2$).
\end{definition}

\begin{proposition}[Boundary strata and operadic structure;
\ClaimStatusProvedElsewhere{} \cite{FM94}]
\label{prop:fm-boundary-strata}
\index{Fulton--MacPherson!boundary strata}
The codimension-$1$ boundary strata of
$\overline{\Conf}_k(\bR^n)$ are indexed by subsets
$S \subset \{1, \ldots, k\}$ with $|S| \geq 2$, and are
diffeomorphic to
\[
\partial_S \overline{\Conf}_k(\bR^n)

thinking
**Searching definitions for E1**

I'm considering how to approach using topological E1 codim-1 strata and their relation to consecutive interval splittings in ordered configuration spaces. I think it would be useful to look up definitions of E1, perhaps in a specific file or another resource. It seems like I need a solid understanding of this concept to proceed effectively. Let’s find the information to clarify my next steps!
exec
/bin/zsh -lc "sed -n '1,140p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"consecutive splitting|ordered interval splitting|E_1\\(m\\)|associahedron|boundary strata.*E_1|Stasheff\" chapters/theory/en_koszul_duality.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/frame/heisenberg_frame.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% Ordered Associative Chiral Koszul Duality
% Integration-ready chapter file (stripped from standalone amsart draft).
% Uses only \providecommand for macros that may not be in main.tex preamble.

\providecommand{\Assch}{\mathrm{Ass}^{\mathrm{ch}}}
\providecommand{\Barch}{\overline{B}^{\mathrm{ch}}}
\providecommand{\Cobar}{\Omega^{\mathrm{ch}}}
\providecommand{\coHoch}{\operatorname{coHH}}
\providecommand{\Cotor}{\operatorname{Cotor}}
\providecommand{\Coext}{\operatorname{Coext}}
\providecommand{\RHom}{R\!\operatorname{Hom}}
\providecommand{\Tot}{\operatorname{Tot}}
\providecommand{\KK}{\mathbb{K}}
\providecommand{\Dpbw}{D^{\mathrm{pbw}}}
\providecommand{\Dco}{D^{\mathrm{co}}}
\providecommand{\chotimes}{\mathbin{\otimes^{\mathrm{ch}}}}
\providecommand{\wt}{\widetilde}
\providecommand{\eps}{\varepsilon}
\providecommand{\susp}{s}
\providecommand{\coeq}{\operatorname{coeq}}
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:293:Stasheff associahedron ($n = 1$) or the FM operad ($n \geq 2$).
chapters/theory/en_koszul_duality.tex:322:Stasheff's theorem for $n = 1$.
chapters/theory/en_koszul_duality.tex:910:$1$ & $\operatorname{sgn}(t_1 - t_2)$ & Stasheff polytopes & Hochschild cohomology \\
chapters/theory/en_koszul_duality.tex:1235: := \FM_k(\bC) \times E_1(m)$.
chapters/theory/en_koszul_duality.tex:1322: & $\Conf_k(\bR)$: consecutive splitting \\[2pt]
chapters/theory/en_koszul_duality.tex:1635:$\operatorname{FM}_k(\mathbb{C}) \times E_1(m)$
chapters/theory/en_koszul_duality.tex:1824:= \FM_k(\bC) \times E_1(m)$.
chapters/theory/en_koszul_duality.tex:1828:\FM_k(\bC) \times E_1(m)
chapters/theory/en_koszul_duality.tex:1833:$\Sigma_m$-action on $E_1(m)$.
chapters/theory/en_koszul_duality.tex:1839:For general~$m$, the $E_1(m)$-factor provides the ``$m$ open inputs''
chapters/theory/en_koszul_duality.tex:1863:= \FM_1(\bC) \times E_1(m) \cong \mathrm{pt} \times E_1(m)$
chapters/theory/en_koszul_duality.tex:1865:$\prod_m \operatorname{Hom}_{\Sigma_m}(E_1(m),
chapters/theory/en_koszul_duality.tex:1877:$E_1(m) \times E_1(j) \to E_1(m + j - 1)$.
chapters/theory/en_koszul_duality.tex:2187:open-sector operations, indexed by $E_1(m)$ (configurations of
chapters/theory/en_koszul_duality.tex:2510:\FM_k(\bC) \times E_1(m),\,
chapters/theory/en_koszul_duality.tex:2836:\emph{all} $k \geq 3$: the Stasheff cascade
chapters/theory/en_koszul_duality.tex:2863:functor~$U$. The obstruction is the Stasheff cascade: any chiral
chapters/theory/en_koszul_duality.tex:3370:the Stasheff coherence equations for an
chapters/theory/ordered_associative_chiral_kd.tex:1797:\FM_k(\mathbb C)\times E_1(m),
chapters/theory/ordered_associative_chiral_kd.tex:1801:(the chiral, holomorphic factor) and $E_1(m)$ is

thinking
**Exploring search options**

I'm considering the possibility of using ordered associative chiral KD, but it seems like I might have mentioned it before. The user is looking to search for SC generators and relations. I think I might need a cross-volume search to explore if ordered associative chiral KD involves SC theorem too. I should probably check around line 1797 and inspect any potential duplicate sections to ensure clarity. Let's see what I can find!
exec
/bin/zsh -lc "sed -n '1788,1888p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"SC\\"'^'"\\{ch,top\\}|Swiss-cheese|codimension-1|codim-1|codimension-2|codim-2|boundary strata|generator|relation\" chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{construction}[The SC$^{\mathrm{ch,top}}$ operation space;
\ClaimStatusProvedHere]
\label{constr:sc-operation-space}
The two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch,top}}$ has operation spaces
\[
\mathrm{SC}^{\mathrm{ch,top}}(k,m)
\;=\;
\FM_k(\mathbb C)\times E_1(m),
\]
where $\FM_k(\mathbb C)$ is the Fulton--MacPherson
compactification of $\mathrm{Conf}_k(\mathbb C)$
(the chiral, holomorphic factor) and $E_1(m)$ is
the little-intervals operad (the coassociative, topological factor).
Concretely, $E_1(m)\simeq \mathrm{Conf}_m^{<}(\mathbb R)$
up to translation and scaling, which is contractible.

For the ordered bar complex of an $E_1$-chiral algebra,
the relevant spaces at tensor degree~$k$ are
 succeeded in 51ms:
472:impose the three-term relation on triple collisions.
498:has standard generators $\gamma_{ij}$ ($i<j$, the loop in which $z_i$
506:The braid relation $\gamma_{ij}\gamma_{ik}\gamma_{jk}
560:Define the \emph{$R$-twisted action} on generators by
570:of the braid group, provided the braid relation holds (verified below).
572:we must also verify the Coxeter relations.
592:The braid relation
781:generators in odd degrees~$\geq 3$, one for each odd
1463:subject to the sewing relations induced from the algebra side.
1492:Finally, every ordered genus-zero sewing relation on the coalgebra side is the image under the
1493:equivalence $\KK_A^{\mathrm{bi}}$ of the corresponding relation on the algebra side.
1792:The two-coloured Swiss-cheese operad
1877:The boundary strata of $\overline{\FM}_k^{\mathrm{ord}}(\mathbb C)$
1906:In the unordered FM compactification, boundary strata are
1959:to the boundary strata of
1965:\textup{(}i.e.~the $E_1$-operad relation on the zeroth-mode
2123:\item The Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$
2139:generator of $\pi_1=\mathbb Z$.
2197:a \emph{single} generator
2250:Heisenberg has the single generator~$J$ and the unique
exec
/bin/zsh -lc "sed -n '1790,1885p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{theorem}[The operadic center of
$\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex;
\ClaimStatusProvedHere]
\label{thm:operadic-center-hochschild}
\index{Hochschild cohomology!as operadic center|textbf}
Let $\cA$ be a logarithmic chiral algebra
\textup{(}an algebra over the closed sector
$(\mathsf{SC}^{\mathrm{ch,top}})^{\mathsf{c}} = \{\FM_k(\bC)\}$
of the holomorphic--topological Swiss-cheese operad, with
operations extending to the log compactification of
$\Conf_k(\bC)$\textup{)}, and
let $A = \cA|_{\{z_0\}}$ denote the fiber at a basepoint
\textup{(}an $E_1$-algebra via the open sector\textup{)}. There is
a quasi-isomorphism of $\Etwo$-algebras
\begin{equation}\label{eq:center-hochschild-qi}
Z_{\mathsf{SC}}(A)
\;\simeq\;
C^{\bullet}_{\mathrm{ch}}(\cA, \cA),
\end{equation}
codex
I’ve found the gap: the Swiss-cheese section gives an operation-space model and componentwise composition, but it never spells out a codimension-one generating set or a codimension-two relation set. I’m checking whether any nearby wording overstates that as an explicit presentation before I patch it.
exec
/bin/zsh -lc 'rg -n "explicit (form|presentation)|generators-and-relations|codimension-1 boundary strata|codimension-2" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"SC\\"'^'"\\{ch,top\\}|Swiss-cheese\" ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
190:generators-and-relations presentation due to Arnold ($n = 2$, i.e., $\bR^n = \bC$) and
994:graph expansion providing the explicit formulas.
1817:Definition~\ref{def:operadic-center} and the explicit form of
 succeeded in 51ms:
Total output lines: 638

/Users/raeez/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex:84:We develop the BV-BRST interpretation of the bar complex of a quantum chiral algebra arising from a Calabi--Yau category. The $\Ainf$-operations of the CY category define an open string field theory in the Batalin--Vilkovisky formalism; the CY pairing provides the BV bracket; the quantum master equation is identified with the Maurer--Cartan equation for $\Theta_A$ from Volume~I. The bar complex $B(A)$ is the BV-BRST complex, with the bar differential equal to $Q_{\BRST}$. We explain how the genus-$g$ curvature $d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$ is the BRST anomaly, and how anomaly cancellation ($\kappa_{\mathrm{ch}} = 0$) corresponds to an ``untwisted'' BKM algebra. The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra (deconcatenation coproduct, bar differential); the Swiss-cheese structure $\SC^{\mathrm{ch,top}}$ of Volume~II emerges on the open-closed \emph{pair} $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, where the chiral Hochschild cochain complex $C^\bullet_{\mathrm{ch}}(A,A)$ (the bulk/closed sector) acts on $A$ (the boundary/open sector). For CY3 manifolds $X$, the full BV-BRST complex of the topological B-model is the bar complex of the quantum vertex chiral group $G(X)$.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex:379:\section{The Swiss-cheese structure and open-closed string field theory}
/Users/raeez/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex:383:\subsection{The Swiss-cheese operad}
/Users/raeez/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex:386:The open-closed string field theory requires both open and closed string sectors. The algebraic structure governing their interaction is the \emph{Swiss-cheese operad} $\SC^{\mathrm{ch,top}}$ from Volume~II: a 2-colored operad with a ``chiral'' color (closed strings, bulk) and a ``topological'' color (open strings, boundary).
/Users/raeez/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex:401:  % AP158: SC^{ch,top} != E_3. Dunn additivity does not apply.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex:407:The bar complex $B(A)$ is an $E_1$ dg coassociative coalgebra. It is \emph{not} an $\SC^{\mathrm{ch,top}}$-algebra: the Swiss-cheese operad is two-coloured, requiring both an open (boundary) and a closed (bulk) sector. The $\SC^{\mathrm{ch,top}}$ structure emerges on the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on $B(A)$ alone.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex:563: \item \textbf{Swiss-cheese = open-closed BV.} The $\SC^{\mathrm{ch,top}}$ structure on the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ is the BV structure on the combined open-closed string field theory. The bar complex $B(A)$ is the $E_1$ dg coassociative coalgebra (the open sector); the chiral derived center $C^\bullet_{\mathrm{ch}}(A,A)$ is the closed sector.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex:586: \item \textbf{The closed string field theory and $\mathcal{W}$-algebras.} For CY3, the closed string sector is controlled by the BCOV theory, whose algebraic structure is a $\mathcal{W}$-algebra (the vertex algebra of polyvector fields with Schouten bracket and $\partial$ operator). The full open-closed BV-BRST complex should be the Swiss-cheese bar complex $B_{\SC}(A_\cC)$, combining the $\mathcal{W}$-algebra (bulk) with $G(X)$ (boundary) via the open-closed coupling.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_coha_e1_sector.tex:373:\subsection{The Swiss-cheese interpretation}
/Users/raeez/calabi-yau-quantum-groups/notes/theory_coha_e1_sector.tex:376:The $E_1$-structure on the CoHA is the shadow of the Swiss-cheese algebra from
/Users/raeez/calabi-yau-quantum-groups/notes/theory_coha_e1_sector.tex:377:Volume~II. The Swiss-cheese operad $\mathrm{SC}$ governs the
/Users/raeez/calabi-yau-quantum-groups/notes/theory_coha_e1_sector.tex:384: \textbf{Swiss-cheese sector} & \textbf{Operadic structure} & \textbf{CY3 realization} \\
/Users/raeez/calabi-yau-quantum-groups/notes/theory_coha_e1_sector.tex:393:The Swiss-cheese picture makes manifest why the CoHA is $E_1$: it lives on the
/Users/raeez/calabi-yau-quantum-groups/notes/physics_sduality_langlands.tex:820: where the interval gives the Swiss-cheese structure).
/Users/raeez/calabi-yau-quantum-groups/notes/theory_6d_hcs_chiral_qg.tex:49:% E_inf-chiral (BD sense), E_1-ordered refinement (Vol II Swiss-cheese).
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1078:$A_\infty$~chiral algebra, bar complex, Swiss-cheese operad,
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1094:\item $\SCchtop$ is the holomorphic--topological Swiss-cheese operad (Definition~\ref{def:SC}).
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1110: algebra over the Swiss-cheese operad

thinking
**Investigating local notation**

I need to look into whether there's a local notation referred to as `K_m`. This could be important for understanding the context better. I'll search for it to see what I can find and clarify its meaning or usage. It feels like this could be a straightforward inspection, but I want to make sure I'm thorough in my search to ensure I capture all necessary details! Let's see what I can uncover!
exec
/bin/zsh -lc "rg -n \"K_m|K_n|associahedron|Stasheff model\" chapters/theory/en_koszul_duality.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
293:Stasheff associahedron ($n = 1$) or the FM operad ($n \geq 2$).

thinking
**Considering notation for K_m**

I don't seem to have a local `K_m`, but perhaps I can introduce it as a standard. It's important to be careful with notation, so maybe I should say "in the Stasheff compactification of $E_1(m)$." I might be able to avoid creating new notation altogether. I think it would be wise to check if there is a model for `E_1` in the earlier file. I'll look into that!
exec
/bin/zsh -lc "rg -n \"little intervals|E_1\\(m\\)|ordered interval|Conf_m\\"'^<'"\\(\\\\bR\\)|Associa\" chapters/theory/en_koszul_duality.tex | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1235: := \FM_k(\bC) \times E_1(m)$.
1635:$\operatorname{FM}_k(\mathbb{C}) \times E_1(m)$
1824:= \FM_k(\bC) \times E_1(m)$.
1828:\FM_k(\bC) \times E_1(m)
1833:$\Sigma_m$-action on $E_1(m)$.
1839:For general~$m$, the $E_1(m)$-factor provides the ``$m$ open inputs''
1863:= \FM_1(\bC) \times E_1(m) \cong \mathrm{pt} \times E_1(m)$
1865:$\prod_m \operatorname{Hom}_{\Sigma_m}(E_1(m),
1877:$E_1(m) \times E_1(j) \to E_1(m + j - 1)$.
2187:open-sector operations, indexed by $E_1(m)$ (configurations of
2510:\FM_k(\bC) \times E_1(m),\,
5382:\item \textup{(Associated graded.)}
5883:\item \textup{(Associated graded.)}
6294:the deconcatenation coproduct comes from ordered interval


thinking
**Considering file edits**

I’m thinking about whether I should edit both files since it might still fall within scope. However, the AGENTS guideline mentions minimum truthful edits. I wonder if using a canonical file along with a duplicate construction in the ordered_associative_chiral_kd setup would provide a more comprehensive approach. I need to check if the duplicate is live or already included in the main file since it seems to be an active file.
thinking
**Investigating document duplication**

I'm thinking there might be a duplicate in my appendix related to `appendices/ordered_associative_chiral_kd.tex`. It seems mirrored, but I'm not sure if it's currently active. I could search to see if that section appears in both places. The theorem registry indicates `appendices/ordered_associative_chiral_kd.tex` is active, which is puzzling if they're duplicated. I'll investigate further by searching for `The SC^ch,top operation space` in the appendices to clarify the situation.
codex
I found a second live surface in `chapters/theory/ordered_associative_chiral_kd.tex` that also defines `SC^{ch,top}` only by operation spaces. I’m checking whether that duplicate is active enough to warrant the same minimal clarification, to avoid the canonical file and the ordered chapter drifting apart.
exec
/bin/zsh -lc "rg -n \"The SC\\"'$'"\\"'^'"\\{\\\\mathrm\\{ch,top\\}\\}\\"'$ operation space|SC'"\\"'^'"\\{\\\\mathrm\\{ch,top\\}\\}.*operation spaces|Swiss-cheese operad.*operation spaces\" chapters appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"explicit form of.*SC|operation spaces.*SC\\"'^'"\\{\\\\mathrm\\{ch,top\\}\\}|The two-coloured Swiss-cheese operad\" chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:The SC$\^\{\mathrm\{ch,top\}\}$ operation space|SC\^\{\mathrm\{ch,top\}\}.*operation spaces|Swiss-cheese operad.*operation spaces)
                  ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
rg: regex parse error:
    (?:explicit form of.*SC|operation spaces.*SC\^\{\mathrm\{ch,top\}\}|The two-coloured Swiss-cheese operad)
                                                    ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F \"The two-coloured Swiss-cheese operad\" chapters appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"explicit form of\" chapters appendices -g '*.tex' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"has operation spaces\" chapters appendices -g '*.tex' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/ordered_associative_chiral_kd.tex:1697:The two-coloured Swiss-cheese operad
chapters/theory/ordered_associative_chiral_kd.tex:1792:The two-coloured Swiss-cheese operad
 succeeded in 51ms:
appendices/ordered_associative_chiral_kd.tex:1698:$\mathrm{SC}^{\mathrm{ch,top}}$ has operation spaces
chapters/theory/ordered_associative_chiral_kd.tex:1793:$\mathrm{SC}^{\mathrm{ch,top}}$ has operation spaces
 succeeded in 51ms:
appendices/homotopy_transfer.tex:51: formula for $m_n^{\mathrm{tr}}$ is the explicit form of the
chapters/examples/w_algebras.tex:2669:Part~(iii) follows from the explicit form of the
chapters/theory/en_koszul_duality.tex:1817:Definition~\ref{def:operadic-center} and the explicit form of
exec
/bin/zsh -lc "sed -n '1788,1888p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1688,1788p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the full braid group.
\end{definition}

\subsection{The product space and its operadic role}
\label{subsec:product-space}

\begin{construction}[The SC$^{\mathrm{ch,top}}$ operation space;
\ClaimStatusProvedHere]
\label{constr:sc-operation-space}
The two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch,top}}$ has operation spaces
\[
\mathrm{SC}^{\mathrm{ch,top}}(k,m)
\;=\;
\FM_k(\mathbb C)\times E_1(m),
\]
where $\FM_k(\mathbb C)$ is the Fulton--MacPherson
compactification of $\mathrm{Conf}_k(\mathbb C)$
(the closed/holomorphic colour) and $E_1(m)$ is
the little-intervals operad (the open/topological colour).
 succeeded in 51ms:

\begin{construction}[The SC$^{\mathrm{ch,top}}$ operation space;
\ClaimStatusProvedHere]
\label{constr:sc-operation-space}
The two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch,top}}$ has operation spaces
\[
\mathrm{SC}^{\mathrm{ch,top}}(k,m)
\;=\;
\FM_k(\mathbb C)\times E_1(m),
\]
where $\FM_k(\mathbb C)$ is the Fulton--MacPherson
compactification of $\mathrm{Conf}_k(\mathbb C)$
(the chiral, holomorphic factor) and $E_1(m)$ is
the little-intervals operad (the coassociative, topological factor).
Concretely, $E_1(m)\simeq \mathrm{Conf}_m^{<}(\mathbb R)$
up to translation and scaling, which is contractible.

For the ordered bar complex of an $E_1$-chiral algebra,
the relevant spaces at tensor degree~$k$ are
Plan update
Canonical SC^{ch,top} surfaces give an operation-space model but not a codim-1/codim-2 presentation. I’m patching the canonical Vol I definition plus the duplicated ordered-associative surfaces, then I’ll grep the repo for drift and verify the new wording is scoped correctly.
  ✓ Audit the live SC^{ch,top} definition surfaces and identify overclaims about explicit presentation
  → Add minimal remarks listing codim-1 generators and codim-2 relation families, and soften any overclaiming wording
  • Run targeted grep checks for the new remark and unresolved explicit-presentation claims, then summarize findings with exact edits
codex
```text
surface: chapters/theory/en_koszul_duality.tex + ordered_associative_chiral_kd chapter/appendix SC^{ch,top} definitions
object lock: SC^{ch,top} acts on the derived-center pair, not on the bar complex [Y]
current presentation: operation-space model only; no codimension-1/codimension-2 generators-relations list [Y]
planned edit: add unlabelled remarks listing codimension-1 generator families and codimension-2 relation families; replace one “explicit form” phrase with “operation-space description” [Y]
mixed-face check: in FM_k(C) x E_1(m), a codimension-1 generator comes from one factor hitting a codimension-1 face while the other stays interior; simultaneous closed+open degeneration is codimension-2 [Y]
scope check: genus [0], arities [(k,m) all], no theorem status or labels changed [Y]
verdict: ACCEPT
```


thinking
**Considering SC generators**

I'm thinking this might be interpreted as the bar complex carrying both colors, which contradicts AGENTS where the bar complex is E1 only. Contextually, it's about the degree k product space, not necessarily the full SC algebra. However, the user asked specifically about SC generators-and-relations. So, perhaps I should minimally edit by adding a remark that clarifies it's a geometric mnemonic and not an SC-algebra structure. It might prevent any misleading interpretations. But I have to ensure not to overdo it!
thinking
**Clarifying structures**

I'm considering that the canonical en_koszul already has a principle of clarification, but the ordered_associative_chiral_kd might not. I could add a remark stating that this product-space description doesn't equip the bar complex with an SC-algebra structure since the codimension-one faces record only the geometric generators. This could address both aspects. If I add the same clarification to the appendix, that might be okay. I should also check if the ordered chapter makes any explicit claims, but it seems like just adding a remark might suffice.
codex
I’ve pinned the exact edits. I’m patching the canonical definition plus the duplicated ordered-associative surfaces now, with one wording downgrade where the file currently overstates the presentation as “explicit.”
file update
M /Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex
@@ -1736,2 +1736,26 @@
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
M /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex
@@ -1831,2 +1831,26 @@
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -1246,2 +1246,25 @@
 
+\begin{remark}[Generator surface of
+\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
+The definition above gives an operation-space model, not yet a
+minimal generators-and-relations presentation. On compactified
+models the codimension-$1$ generator families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
+ faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
+ $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
+ \textup{(}ii\textup{)}, supplying the bulk-to-boundary generators.
+\end{enumerate}
+The codimension-$2$ relations come from pairwise intersections of
+these codimension-$1$ faces: Arnold--Orlik--Solomon in the closed
+factor, Stasheff associativity in the open factor, and commuting
+mixed squares comparing a closed collision with an open split.
+Later arguments use this boundary-stratum description; the full
+minimal presentation is not written out here.
+\end{remark}
+
 \begin{principle}[The bar complex is $\Eone$-chiral coassociative;
@@ -1816,3 +1839,3 @@
 We compute the center using
-Definition~\ref{def:operadic-center} and the explicit form of
+Definition~\ref{def:operadic-center} and the operation-space description of
 $\mathsf{SC}^{\mathrm{ch,top}}$
apply_patch(auto_approved=true) exited 0 in 36ms:
Success. Updated the following files:
M chapters/theory/en_koszul_duality.tex
M chapters/theory/ordered_associative_chiral_kd.tex
M appendices/ordered_associative_chiral_kd.tex
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index bced5562f5f45921b80a2fa6aef6292c25185f9b..780ea6fc37e282635a05ba72b278dde1c48d9f8e
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1734,6 +1734,30 @@
 open (topological) colour.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ee8a9e416789579ba37cd1f8c6251b5e6e3688f..85d1853ca9828b12c3a1146de29311f585a14953
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -1244,6 +1244,29 @@
 from the open color.
 \end{definition}
 
+\begin{remark}[Generator surface of
+\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
+The definition above gives an operation-space model, not yet a
+minimal generators-and-relations presentation. On compactified
+models the codimension-$1$ generator families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
+ faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
+ $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
+ \textup{(}ii\textup{)}, supplying the bulk-to-boundary generators.
+\end{enumerate}
+The codimension-$2$ relations come from pairwise intersections of
+these codimension-$1$ faces: Arnold--Orlik--Solomon in the closed
+factor, Stasheff associativity in the open factor, and commuting
+mixed squares comparing a closed collision with an open split.
+Later arguments use this boundary-stratum description; the full
+minimal presentation is not written out here.
+\end{remark}
+
 \begin{principle}[The bar complex is $\Eone$-chiral coassociative;
 $\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
 \label{princ:sc-two-incarnations}
@@ -1814,7 +1837,7 @@
 
 \begin{proof}
 We compute the center using
-Definition~\ref{def:operadic-center} and the explicit form of
+Definition~\ref{def:operadic-center} and the operation-space description of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 (Definition~\ref{def:SC}).
 
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index b39c61f3763a21a717b6d65de5388ff9c9a9a966..28f349f273d1747b2027c58acf9ae54f3181e053
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -1829,6 +1829,30 @@
 coassociative (topological) component.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 

file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index bced5562f5f45921b80a2fa6aef6292c25185f9b..780ea6fc37e282635a05ba72b278dde1c48d9f8e
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1734,6 +1734,30 @@
 open (topological) colour.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ee8a9e416789579ba37cd1f8c6251b5e6e3688f..85d1853ca9828b12c3a1146de29311f585a14953
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -1244,6 +1244,29 @@
 from the open color.
 \end{definition}
 
+\begin{remark}[Generator surface of
+\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
+The definition above gives an operation-space model, not yet a
+minimal generators-and-relations presentation. On compactified
+models the codimension-$1$ generator families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
+ faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
+ $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
+ \textup{(}ii\textup{)}, supplying the bulk-to-boundary generators.
+\end{enumerate}
+The codimension-$2$ relations come from pairwise intersections of
+these codimension-$1$ faces: Arnold--Orlik--Solomon in the closed
+factor, Stasheff associativity in the open factor, and commuting
+mixed squares comparing a closed collision with an open split.
+Later arguments use this boundary-stratum description; the full
+minimal presentation is not written out here.
+\end{remark}
+
 \begin{principle}[The bar complex is $\Eone$-chiral coassociative;
 $\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
 \label{princ:sc-two-incarnations}
@@ -1814,7 +1837,7 @@
 
 \begin{proof}
 We compute the center using
-Definition~\ref{def:operadic-center} and the explicit form of
+Definition~\ref{def:operadic-center} and the operation-space description of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 (Definition~\ref{def:SC}).
 
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index b39c61f3763a21a717b6d65de5388ff9c9a9a966..28f349f273d1747b2027c58acf9ae54f3181e053
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -1829,6 +1829,30 @@
 coassociative (topological) component.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 

codex
The edits are in place. I’m doing a narrow verification pass now: line-level diff, grep for the downgraded overclaim, and a duplicate sweep to see whether any untouched live surface in this repo still defines `SC^{ch,top}` without the new generator note.
exec
/bin/zsh -lc 'git diff -- chapters/theory/en_koszul_duality.tex chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Codimension-one generators for\" chapters appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"explicit form of\" chapters appendices -g '*.tex' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"The two-coloured Swiss-cheese operad\" chapters appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index 15cdbf4..780ea6f 100644
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -433,10 +433,10 @@ $\bar A^{\otimes n}$:
 d
 \;-\;
 \sum_{1\leq i<j\leq n}
-r_{ij}(z_i-z_j)\,d\log(z_i-z_j).
+r_{ij}(z_i-z_j)\,d(z_i-z_j).
 \end{equation}
 Here $r_{ij}$ acts in the $(i,j)$ tensor slots of~$\bar A^{\otimes n}$
-and $d\log(z_i-z_j)=dz_{ij}/(z_i-z_j)$ is the logarithmic form
+and $r_{ij}(z_{ij})\,dz_{ij}$ is the connection $1$-form
 on $\mathrm{Conf}_n^{\mathrm{ord}}(\mathbb{C})$.
 
 \emph{Flatness.}
@@ -479,7 +479,7 @@ R(z)
 \operatorname{Mon}_\gamma(\nabla)
 \;=\;
 succeeded in 51ms:
appendices/homotopy_transfer.tex:51: formula for $m_n^{\mathrm{tr}}$ is the explicit form of the
chapters/examples/w_algebras.tex:2669:Part~(iii) follows from the explicit form of the
 succeeded in 51ms:
appendices/ordered_associative_chiral_kd.tex:1737:\begin{remark}[Codimension-one generators for
chapters/theory/ordered_associative_chiral_kd.tex:1832:\begin{remark}[Codimension-one generators for
 succeeded in 51ms:
appendices/ordered_associative_chiral_kd.tex:1697:The two-coloured Swiss-cheese operad
chapters/theory/ordered_associative_chiral_kd.tex:1792:The two-coloured Swiss-cheese operad
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index bced5562f5f45921b80a2fa6aef6292c25185f9b..780ea6fc37e282635a05ba72b278dde1c48d9f8e
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1734,6 +1734,30 @@
 open (topological) colour.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ee8a9e416789579ba37cd1f8c6251b5e6e3688f..85d1853ca9828b12c3a1146de29311f585a14953
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -1244,6 +1244,29 @@
 from the open color.
 \end{definition}
 
+\begin{remark}[Generator surface of
+\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
+The definition above gives an operation-space model, not yet a
+minimal generators-and-relations presentation. On compactified
+models the codimension-$1$ generator families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
+ faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
+ $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
+ \textup{(}ii\textup{)}, supplying the bulk-to-boundary generators.
+\end{enumerate}
+The codimension-$2$ relations come from pairwise intersections of
+these codimension-$1$ faces: Arnold--Orlik--Solomon in the closed
+factor, Stasheff associativity in the open factor, and commuting
+mixed squares comparing a closed collision with an open split.
+Later arguments use this boundary-stratum description; the full
+minimal presentation is not written out here.
+\end{remark}
+
 \begin{principle}[The bar complex is $\Eone$-chiral coassociative;
 $\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
 \label{princ:sc-two-incarnations}
@@ -1814,7 +1837,7 @@
 
 \begin{proof}
 We compute the center using
-Definition~\ref{def:operadic-center} and the explicit form of
+Definition~\ref{def:operadic-center} and the operation-space description of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 (Definition~\ref{def:SC}).
 
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index b39c61f3763a21a717b6d65de5388ff9c9a9a966..28f349f273d1747b2027c58acf9ae54f3181e053
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -1829,6 +1829,30 @@
 coassociative (topological) component.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 




thinking
**Evaluating git diff issues**

I'm noticing that the `git diff` is huge because there are other modifications in the same files that aren't mine. I need to focus on our specific changes and might consider using tools like `rg` or `nl`. It's also important to note any unexpected modifications in files we touched that were already there. Since the workspace is dirty, I might be cautious to ensure I only mention our edits. I could check `git status`, although it might not be necessary.
thinking
**Finalizing edits and checks**

I need to ensure that I'm only mentioning our edits and that nothing was inadvertently overridden, especially since `apply_patch` only added sections and one phrase. I might check with `grep` for line numbers and use `nl -ba` around the inserted sections. I should also search for "Generator surface of" using `rg`. Interestingly, my remark in `en_koszul` isn't found due to different search terms, which could be fine. I might also check for duplicates within the repo related to "The two-coloured Swiss-cheese operad" to ensure everything is patched correctly.
thinking
**Searching for definitions and duplicates**

I’m thinking about searching for `\begin{definition}[Holomorphic--topological Swiss-cheese operad]` specifically in `en_koszul`. I also need to check for potential duplicates around "operation spaces." It might be worth adding a note about the untouched cross-volume surfaces. I found references in volumes outside the current repo, particularly in the main introduction, but they reference `Definition\ref{def:SC}`. I can clarify that these weren't edited since they aren't exact theorem surfaces and are outside our current scope.
codex
The repo is dirty in those files already, so `git diff` shows unrelated preexisting edits too. I’m narrowing to line-anchored reads of only the hunks I added or rewrote, so the final report doesn’t attribute other changes to this pass.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1814,1824p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1240,1278p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '1826,1856p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/ordered_associative_chiral_kd.tex | sed -n '1731,1761p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Generator surface of" chapters/theory/en_koszul_duality.tex && rg -n -F "Codimension-one generators for" chapters/theory/ordered_associative_chiral_kd.tex appendices/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1814	\begin{theorem}[The operadic center of
  1815	$\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex;
  1816	\ClaimStatusProvedHere]
  1817	\label{thm:operadic-center-hochschild}
  1818	\index{Hochschild cohomology!as operadic center|textbf}
  1819	Let $\cA$ be a logarithmic chiral algebra
  1820	\textup{(}an algebra over the closed sector
  1821	$(\mathsf{SC}^{\mathrm{ch,top}})^{\mathsf{c}} = \{\FM_k(\bC)\}$
  1822	of the holomorphic--topological Swiss-cheese operad, with
  1823	operations extending to the log compactification of
  1824	$\Conf_k(\bC)$\textup{)}, and
 succeeded in 51ms:
  1240	\end{enumerate}
  1241	Composition is componentwise: FM insertion in~$\bC$, interval
  1242	insertion in~$E_1$. The no-open-to-closed rule ensures that
  1243	the closed color is an operadic retract: it receives no information
  1244	from the open color.
  1245	\end{definition}
  1246	
  1247	\begin{remark}[Generator surface of
  1248	\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
  1249	The definition above gives an operation-space model, not yet a
  1250	minimal generators-and-relations presentation. On compactified
  1251	models the codimension-$1$ generator families are:
  1252	\begin{enumerate}[label=\textup{(\roman*)}]
  1253	\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
  1254	\item open interval-splitting faces in a Stasheff compactification
  1255	 of $E_1(m)$, equivalently cuts of the ordered open inputs into
  1256	 consecutive blocks;
  1257	\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
  1258	 faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
  1259	 $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
 succeeded in 51ms:
  1826	observables factorise holomorphically in~$z$ and
  1827	associatively in~$t$. The bar differential is the
  1828	chiral (holomorphic) component. The bar coproduct is the
  1829	coassociative (topological) component.
  1830	\end{remark}
  1831	
  1832	\begin{remark}[Codimension-one generators for
  1833	\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
  1834	The construction above gives the operation space, not yet a minimal
  1835	generators-and-relations presentation, and by itself it does not
  1836	equip the ordered bar complex with a full Swiss-cheese algebra
  1837	structure. On compactified models the codimension-$1$ generator
  1838	families are:
  1839	\begin{enumerate}[label=\textup{(\roman*)}]
  1840	\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
  1841	 $|S|\ge 2$;
  1842	\item open interval-splitting faces in a Stasheff compactification
  1843	 of $E_1(m)$, equivalently cuts of the ordered open inputs into
  1844	 consecutive blocks;
  1845	\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
 succeeded in 51ms:
  1731	observables factorise holomorphically in~$z$ and
  1732	associatively in~$t$. The bar differential is the
  1733	closed (holomorphic) colour. The bar coproduct is the
  1734	open (topological) colour.
  1735	\end{remark}
  1736	
  1737	\begin{remark}[Codimension-one generators for
  1738	\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
  1739	The construction above gives the operation space, not yet a minimal
  1740	generators-and-relations presentation, and by itself it does not
  1741	equip the ordered bar complex with a full Swiss-cheese algebra
  1742	structure. On compactified models the codimension-$1$ generator
  1743	families are:
  1744	\begin{enumerate}[label=\textup{(\roman*)}]
  1745	\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
  1746	 $|S|\ge 2$;
  1747	\item open interval-splitting faces in a Stasheff compactification
  1748	 of $E_1(m)$, equivalently cuts of the ordered open inputs into
  1749	 consecutive blocks;
  1750	\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
 succeeded in 52ms:
1247:\begin{remark}[Generator surface of
appendices/ordered_associative_chiral_kd.tex:1737:\begin{remark}[Codimension-one generators for
chapters/theory/ordered_associative_chiral_kd.tex:1832:\begin{remark}[Codimension-one generators for
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index bced5562f5f45921b80a2fa6aef6292c25185f9b..780ea6fc37e282635a05ba72b278dde1c48d9f8e
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1734,6 +1734,30 @@
 open (topological) colour.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ee8a9e416789579ba37cd1f8c6251b5e6e3688f..85d1853ca9828b12c3a1146de29311f585a14953
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -1244,6 +1244,29 @@
 from the open color.
 \end{definition}
 
+\begin{remark}[Generator surface of
+\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
+The definition above gives an operation-space model, not yet a
+minimal generators-and-relations presentation. On compactified
+models the codimension-$1$ generator families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
+ faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
+ $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
+ \textup{(}ii\textup{)}, supplying the bulk-to-boundary generators.
+\end{enumerate}
+The codimension-$2$ relations come from pairwise intersections of
+these codimension-$1$ faces: Arnold--Orlik--Solomon in the closed
+factor, Stasheff associativity in the open factor, and commuting
+mixed squares comparing a closed collision with an open split.
+Later arguments use this boundary-stratum description; the full
+minimal presentation is not written out here.
+\end{remark}
+
 \begin{principle}[The bar complex is $\Eone$-chiral coassociative;
 $\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
 \label{princ:sc-two-incarnations}
@@ -1814,7 +1837,7 @@
 
 \begin{proof}
 We compute the center using
-Definition~\ref{def:operadic-center} and the explicit form of
+Definition~\ref{def:operadic-center} and the operation-space description of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 (Definition~\ref{def:SC}).
 
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index b39c61f3763a21a717b6d65de5388ff9c9a9a966..28f349f273d1747b2027c58acf9ae54f3181e053
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -1829,6 +1829,30 @@
 coassociative (topological) component.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 

exec
/bin/zsh -lc 'rg -n -F "operation-space description of" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1840:Definition~\ref{def:operadic-center} and the operation-space description of
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index bced5562f5f45921b80a2fa6aef6292c25185f9b..780ea6fc37e282635a05ba72b278dde1c48d9f8e
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1734,6 +1734,30 @@
 open (topological) colour.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ee8a9e416789579ba37cd1f8c6251b5e6e3688f..85d1853ca9828b12c3a1146de29311f585a14953
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -1244,6 +1244,29 @@
 from the open color.
 \end{definition}
 
+\begin{remark}[Generator surface of
+\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
+The definition above gives an operation-space model, not yet a
+minimal generators-and-relations presentation. On compactified
+models the codimension-$1$ generator families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
+ faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
+ $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
+ \textup{(}ii\textup{)}, supplying the bulk-to-boundary generators.
+\end{enumerate}
+The codimension-$2$ relations come from pairwise intersections of
+these codimension-$1$ faces: Arnold--Orlik--Solomon in the closed
+factor, Stasheff associativity in the open factor, and commuting
+mixed squares comparing a closed collision with an open split.
+Later arguments use this boundary-stratum description; the full
+minimal presentation is not written out here.
+\end{remark}
+
 \begin{principle}[The bar complex is $\Eone$-chiral coassociative;
 $\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
 \label{princ:sc-two-incarnations}
@@ -1814,7 +1837,7 @@
 
 \begin{proof}
 We compute the center using
-Definition~\ref{def:operadic-center} and the explicit form of
+Definition~\ref{def:operadic-center} and the operation-space description of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 (Definition~\ref{def:SC}).
 
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index b39c61f3763a21a717b6d65de5388ff9c9a9a966..28f349f273d1747b2027c58acf9ae54f3181e053
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -1829,6 +1829,30 @@
 coassociative (topological) component.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 


thinking
**Considering file edits**

I think I need to note that a full build might not be necessary right now. Maybe I should run a targeted grep search for "operation-space model." That feels okay. I could also quickly use `sed -n` to check around lines 1836-1842 to find that specific phrase, but it doesn't seem essential. Ultimately, I need to finalize my plan to ensure everything's updated after verification.
Plan update
Inserted codimension-one/codimension-two generator remarks on all live Vol I SC^{ch,top} definition surfaces I found, and downgraded the one overclaim that called the presentation “explicit.” Verification was by line-anchored reads plus grep for the new remarks and the old phrase.
  ✓ Audit the live SC^{ch,top} definition surfaces and identify overclaims about explicit presentation
  ✓ Add minimal remarks listing codim-1 generators and codim-2 relation families, and soften any overclaiming wording
  ✓ Run targeted grep checks for the new remark and unresolved explicit-presentation claims, then summarize findings with exact edits
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index bced5562f5f45921b80a2fa6aef6292c25185f9b..780ea6fc37e282635a05ba72b278dde1c48d9f8e
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1734,6 +1734,30 @@
 open (topological) colour.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ee8a9e416789579ba37cd1f8c6251b5e6e3688f..85d1853ca9828b12c3a1146de29311f585a14953
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -1244,6 +1244,29 @@
 from the open color.
 \end{definition}
 
+\begin{remark}[Generator surface of
+\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
+The definition above gives an operation-space model, not yet a
+minimal generators-and-relations presentation. On compactified
+models the codimension-$1$ generator families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
+ faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
+ $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
+ \textup{(}ii\textup{)}, supplying the bulk-to-boundary generators.
+\end{enumerate}
+The codimension-$2$ relations come from pairwise intersections of
+these codimension-$1$ faces: Arnold--Orlik--Solomon in the closed
+factor, Stasheff associativity in the open factor, and commuting
+mixed squares comparing a closed collision with an open split.
+Later arguments use this boundary-stratum description; the full
+minimal presentation is not written out here.
+\end{remark}
+
 \begin{principle}[The bar complex is $\Eone$-chiral coassociative;
 $\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
 \label{princ:sc-two-incarnations}
@@ -1814,7 +1837,7 @@
 
 \begin{proof}
 We compute the center using
-Definition~\ref{def:operadic-center} and the explicit form of
+Definition~\ref{def:operadic-center} and the operation-space description of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 (Definition~\ref{def:SC}).
 
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index b39c61f3763a21a717b6d65de5388ff9c9a9a966..28f349f273d1747b2027c58acf9ae54f3181e053
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -1829,6 +1829,30 @@
 coassociative (topological) component.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 

codex
Cross-volume note: the Vol II/III sweep turned up references and note-level restatements of `SC^{ch,top}`, but within the current task I only patched the live Vol I definition surfaces. I did not touch external-note duplicates in the sibling volumes.

thinking
**Identifying findings clearly**

I'm considering organizing my findings into a bullet list for clarity. One of the potential findings highlights a problem in the document at chapters/theory/en_koszul_duality.tex:1220. It seems that the definition provided only mentions operation spaces, but it lacks explicit codimension-1 generators and codimension-2 relations. This suggests that there are significant gaps that need to be addressed for a more complete understanding. I'll make sure to emphasize these points in my analysis.
codex
`SC^{ch,top}` was not presented as a full generators-and-relations operad. In the live Vol I surfaces, it was only given as an operation-space model.

- `PROBLEM` at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1220): the canonical definition gave operation spaces and componentwise composition, but no codimension-1 generators or codimension-2 relations. `EXACT edit applied`: inserted the new remark at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247) listing closed collision faces `\partial_S\FM_k(\bC)`, open interval-splitting faces in a Stasheff compactification of `E_1(m)`, mixed product faces in `\FM_k(\bC)\times E_1(m)`, and stating the codimension-2 relation families: Arnold--Orlik--Solomon, Stasheff, and mixed commuting squares. The remark also states explicitly that the full minimal presentation is still not written out there.

- `PROBLEM` at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1840): the proof of the operadic-center theorem called the `SC^{ch,top}` input the “explicit form,” which overstated the presentation. `EXACT edit applied`: changed that phrase to “the operation-space description of `\mathsf{SC}^{\mathrm{ch,top}}`.”

- `PROBLEM` at [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:1792): the duplicate live construction also gave only operation spaces, with no generator list, and could be read as if the ordered bar complex already carried the full Swiss-cheese structure. `EXACT edit applied`: inserted the new remark at [chapters/theory/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:1832) stating that this is only an operation-space model, not a minimal generators-and-relations presentation and not by itself a full Swiss-cheese algebra structure on the ordered bar complex, then listing the same codimension-1 generator families and codimension-2 relation families.

- `PROBLEM` at [appendices/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:1697): the appendix duplicate had the same omission. `EXACT edit applied`: inserted the matching remark at [appendices/ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:1737) with the same generator list and codimension-2 relation summary.

Verification was a targeted grep and line check. I did not run a full TeX build.
file update:
diff --git a/appendices/ordered_associative_chiral_kd.tex b/appendices/ordered_associative_chiral_kd.tex
index bced5562f5f45921b80a2fa6aef6292c25185f9b..780ea6fc37e282635a05ba72b278dde1c48d9f8e
--- a/appendices/ordered_associative_chiral_kd.tex
+++ b/appendices/ordered_associative_chiral_kd.tex
@@ -1734,6 +1734,30 @@
 open (topological) colour.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 1ee8a9e416789579ba37cd1f8c6251b5e6e3688f..85d1853ca9828b12c3a1146de29311f585a14953
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -1244,6 +1244,29 @@
 from the open color.
 \end{definition}
 
+\begin{remark}[Generator surface of
+\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}]
+The definition above gives an operation-space model, not yet a
+minimal generators-and-relations presentation. On compactified
+models the codimension-$1$ generator families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\bC)$ with $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\bC)\times E_1(m)$, the product
+ faces $\partial_S\FM_k(\bC)\times E_1(m)$ and
+ $\FM_k(\bC)\times F$, with $F$ an interval-splitting face as in
+ \textup{(}ii\textup{)}, supplying the bulk-to-boundary generators.
+\end{enumerate}
+The codimension-$2$ relations come from pairwise intersections of
+these codimension-$1$ faces: Arnold--Orlik--Solomon in the closed
+factor, Stasheff associativity in the open factor, and commuting
+mixed squares comparing a closed collision with an open split.
+Later arguments use this boundary-stratum description; the full
+minimal presentation is not written out here.
+\end{remark}
+
 \begin{principle}[The bar complex is $\Eone$-chiral coassociative;
 $\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
 \label{princ:sc-two-incarnations}
@@ -1814,7 +1837,7 @@
 
 \begin{proof}
 We compute the center using
-Definition~\ref{def:operadic-center} and the explicit form of
+Definition~\ref{def:operadic-center} and the operation-space description of
 $\mathsf{SC}^{\mathrm{ch,top}}$
 (Definition~\ref{def:SC}).
 
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index b39c61f3763a21a717b6d65de5388ff9c9a9a966..28f349f273d1747b2027c58acf9ae54f3181e053
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -1829,6 +1829,30 @@
 coassociative (topological) component.
 \end{remark}
 
+\begin{remark}[Codimension-one generators for
+\texorpdfstring{$\mathrm{SC}^{\mathrm{ch,top}}$}{SC}]
+The construction above gives the operation space, not yet a minimal
+generators-and-relations presentation, and by itself it does not
+equip the ordered bar complex with a full Swiss-cheese algebra
+structure. On compactified models the codimension-$1$ generator
+families are:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item closed collision faces $\partial_S\FM_k(\mathbb C)$ with
+ $|S|\ge 2$;
+\item open interval-splitting faces in a Stasheff compactification
+ of $E_1(m)$, equivalently cuts of the ordered open inputs into
+ consecutive blocks;
+\item in the mixed space $\FM_k(\mathbb C)\times E_1(m)$, the
+ product faces $\partial_S\FM_k(\mathbb C)\times E_1(m)$ and
+ $\FM_k(\mathbb C)\times F$, with $F$ an interval-splitting face
+ as in \textup{(}ii\textup{)}.
+\end{enumerate}
+The codimension-$2$ relations are the intersections of these faces:
+Arnold--Orlik--Solomon in the closed factor, Stasheff associativity
+in the open factor, and mixed commuting squares comparing a closed
+collision with an open split.
+\end{remark}
+
 \subsection{The ordered FM compactification}
 \label{subsec:ordered-fm-compact}
 

tokens used
138,575
