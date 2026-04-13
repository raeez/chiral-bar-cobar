# E11_missing_genus2 (220s)

Explicit genus-2 content was already present, so I did not add a new remark: explicit genus-2 graph-sum computation at [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5816), the seven-graph genus-2 catalogue at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:22941), and the `2x2` period matrix definition at [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:4250).

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:23863): the proof said “At genus~$2$ there are six stable graphs,” contradicting the file’s own genus-2 catalogue of seven total stable graphs.
  EXACT edit applied: replaced that sentence with “At genus~$2$ there are seven stable graphs in total (Computation~\ref{comp:genus2-multichannel-catalogue}); the smooth graph has no edges, so the boundary graph sum for the cross-channel correction runs over the remaining six.”

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:24080): a second proof again collapsed the total genus-2 count to six without explaining that this was only the boundary part of the graph sum.
  EXACT edit applied: replaced that sentence with “Again the genus-$2$ computation starts from the seven stable graphs of (Computation~\ref{comp:genus2-multichannel-catalogue}); the smooth graph has no edges, so the boundary graph sum reduces to the remaining six.”

Narrow verification passed: no remaining `six stable graphs` claims in the assigned files. I did not run a full TeX build.


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
session id: 019d87c7-5771-7562-824e-a2f70b474456
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


Search for genus-2 content.
Is there explicit genus-2 computation? 7 stable graphs enumerated? Period matrix 2x2?
If missing: add a remark in higher_genus_foundations.tex or higher_genus_modular_koszul.tex.
mcp startup: no servers

thinking
**Updating exploration plans**

I’m thinking about how I can use exec commands in parallel, which could help me search across the codebase more quickly. It seems like I should send a commentary update before I dive into any substantial work. Maybe I need to revise the plan, but I'm not sure if that's necessary. I definitely want to send a brief commentary about understanding the first steps first, and then I can move on to skill reading and the explorer.
codex
Using `deep-beilinson-audit` plus `beilinson-rectify` in that order: first I’ll locate the genus-2 claim surface and check whether the repo already contains an explicit computation, the `7` stable-graph enumeration, and a `2x2` period-matrix discussion, then I’ll patch the assigned higher-genus file only if the surface is missing or underspecified.
collab spawn_agent(call_t7hebn0jjTnsHEjKAFMqPg8k, prompt="Search the repository for genus-2 content relevant to higher-genus chapters. Identify whether there is explicit genus-2 …")
spawn_agent(call_t7hebn0jjTnsHEjKAFMqPg8k, prompt="Search the repository for genus-2 content relevant to higher-genus chapters. Identify whether there is explicit genus-2 …") pending init:
  agent: 019d87c7-a025-77f0-b166-3fcdf7f4aa5c
mcp startup: no servers
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
audit_campaign_20260413_163450
exec
/bin/zsh -lc 'rg -n "genus-2"' in /Users/raeez/chiral-bar-cobar succeeded in 72ms:
compute/tests/test_a2_polynomial_combinatorics_engine.py:3:Multi-path verification of the genus-2 cross-channel polynomial
compute/tests/test_a2_polynomial_combinatorics_engine.py:411:    W_3 multi-weight genus-2 free-energy correction.
compute/lib/betagamma_genus2_cross_channel_engine.py:1:r"""Betagamma genus-2 cross-channel engine: Mumford vanishing theorem.
compute/lib/betagamma_genus2_cross_channel_engine.py:348:    # The 7 genus-2 stable graphs:
compute/lib/betagamma_genus2_cross_channel_engine.py:569:    print("Betagamma genus-2 cross-channel engine")
compute/lib/bps_entropy_shadow.py:48:      (the genus-2 Siegel space, reflecting the 2 electric + 2 magnetic charges).
compute/lib/bps_entropy_shadow.py:316:    Siegel genus-2 forms. For weight 10: nu = 10 - 3/2 = 17/2.
compute/lib/bps_entropy_shadow.py:715:      - For genus-2 (H_2, dim_moduli=3): nu = k - 3/2
compute/lib/seiberg_witten_shadow.py:1121:    The curve is genus-2 generically, with 6 branch points.
compute/lib/seiberg_witten_shadow.py:1155:    The genus-2 curve has 4 independent periods: a_1, a_2, a_{D,1}, a_{D,2}.
compute/lib/seiberg_witten_shadow.py:1157:    over the 4 independent cycles of the genus-2 surface.
compute/lib/seiberg_witten_shadow.py:1187:        'description': 'SU(3) genus-2 periods (branch points computed)',
compute/tests/test_shadow_cohft_tautological.py:65:    # Section 8: genus-2 graphs
compute/tests/test_shadow_cohft_tautological.py:519:        """Smooth genus-2 term: F_2 = kappa * 7/5760."""
compute/lib/betagamma_determinant.py:529:    characteristics) appears as the genus-2 analog of eta^{24}.
compute/lib/logarithmic_voa_shadow_engine.py:1120:    3. GENUS-2 ANOMALY: The genus-2 shadow delta_pf detects
compute/lib/logarithmic_voa_shadow_engine.py:1495:         (c) The genus-2 amplitude receives nilpotent corrections
compute/tests/test_pixton_shadow_bridge.py:207:    """Test Hodge integral computation for genus-2 graphs."""
compute/tests/test_pixton_shadow_bridge.py:752:        assert pf == 0  # S_3=0 kills all genus-2 pf
compute/lib/theorem_delta_f2_intersection_engine.py:7:2, 3, ..., N, the genus-2 cross-channel correction has the form:
exec
/bin/zsh -lc 'ls chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
connections
examples
frame
theory
exec
/bin/zsh -lc 'rg --files | grep higher' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/C07_higher_genus_foundations.md
wave2_audit_20260413_001942/S02_bar_to_higher_genus.md
wave2_audit_20260413_001942/C08_higher_genus_modular_koszul.md
wave2_audit_20260413_001942/G07_higher_genus_modular_koszul.md
wave2_audit_20260413_001942/G06_higher_genus_foundations.md
wave2_audit_20260413_001942/G08_higher_genus_complementarity.md
wave2_audit_20260413_001942/C09_higher_genus_complementarity.md
staging/for_higher_genus__genus2.tex
staging/for_higher_genus__verlinde.tex
resume_20260413_165929/R04_higher_genus_modular_koszul.md
staging/combined_for_higher_genus.tex
rectification_20260412_233715/R04_higher_genus_modular_koszul.md
rectification_20260412_233715/R03_higher_genus_foundations.md
rectification_20260412_233715/R02_higher_genus_complementarity.md
chapters/connections/semistrict_modular_higher_spin_w3.tex
chapters/theory/higher_genus_complementarity.tex
chapters/theory/higher_genus.tex
chapters/theory/higher_genus_foundations.tex
chapters/theory/higher_genus_modular_koszul.tex
appendices/spectral_higher_genus.tex
codex
I’m reading the required constitutional files and the two candidate chapter files now, while a codebase explorer maps the existing genus-2 surface so I don’t patch the wrong location.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc 'rg -n "genus-2" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2541:\item Assign the genus-2 propagator $G_{\Sigma_2}(z_i, z_j)$ to each internal line.
4215:\label{sec:genus-2-complete}
4250:\begin{definition}[Period matrix: genus-2 case]
4252:Let $\Sigma_2$ be a genus-2 Riemann surface with canonical homology basis:
4458:For genus~2: $\Sigma_2$ is parameterized by the period matrix $\Omega = (\Omega_{ij})_{1 \leq i,j \leq 2} \in \mathbb{H}_2$ (the Siegel upper half-space of symmetric $2 \times 2$ matrices with positive-definite imaginary part), a $3$-complex-dimensional space. The genus-2 propagator $\eta_{12}^{(2)} = d\log E(z_1, z_2 | \Omega)$ (where $E$ is the prime form on $\Sigma_2$) depends on $\Omega$ through the theta function, so $E_1^{*,*,2}$ carries a $\mathbb{C}[\Omega_{ij}, \bar{\Omega}_{ij}]$-module structure. The computation is otherwise parallel to genus~1: internal cohomology is computed on a fixed $\Sigma_2$ using the genus-2 Arnold--Orlik--Solomon relations (which hold with the same combinatorial structure but with genus-2 propagators), and the moduli dependence enters through the propagator's dependence on~$\Omega$.
4702:\label{ex:genus-2-obstruction}
exec
/bin/zsh -lc "sed -n '4190,4285p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{center}
In every case, complementarity $\kappa(\cA) + \kappa(\cA^!) = \mathrm{const}$
holds at genus~$1$, consistent with the genus-$0$ statement of
Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
\end{theorem}

\begin{proof}
The Heisenberg case is Theorem~\ref{thm:genus1-d-squared}.
For a general Koszul chiral algebra $\cA$, the argument is identical:
the Arnold defect at genus~$1$ is the universal $(1,1)$-form
proportional to $E_2(\tau)$ (Theorem~\ref{thm:arnold-genus1}),
and the coefficient of the defect when contracted with the OPE data
of $\cA$ is exactly the modular characteristic $\kappa(\cA)$,
by the same highest-pole extraction that defines $\kappa(\cA)$ in
Theorem~\ref{thm:universal-generating-function}.
The total differential $\Dg{1}$ absorbs the curvature via the
period correction $F_1(\cA) = \kappa(\cA)/24$
\textup{(g=1 only; all-weight at g=1 is unconditional)}, because the
integral $\int_{\overline{\cM}_{1,1}} \psi \cdot \lambda_1 = \lambda_1^{FP} = 1/24$
normalizes the genus-$1$ term in the universal generating function.

exec
/bin/zsh -lc 'rg -n "stable graph" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
46:irreducible stable graph
53:through the Feynman transform, summing over stable graphs
54:weighted by handles. The passage from trees to stable graphs
63:\emph{connected stable graph}~$\Gamma$ with a genus label~$g(v)$
73:The passage from trees to stable graphs corresponds to the passage from
75:operations are indexed by all stable graphs, not just trees, and
86:the unique stable graph $\Gamma_{\mathrm{irr}}$ with one vertex of
482:one-loop stable graph \textup{(}the tadpole\textup{)} evaluated
5820:stable graphs at $(g{=}2, n{=}0)$, depends linearly on the
6427:that every edge of every stable graph carries the same weight-$1$
6530:\section{Quantum chiral homology from stable graph topology}
6533:\index{stable graph!topology|textbf}
6539:direction: starting from the combinatorics of stable graphs alone,
6549:\subsection{The stable graph complex}
6551:\index{stable graph!complex|textbf}
6554:A \emph{stable graph} of type $(g,n)$ is a connected graph
6574:classes of stable graphs of type $(g,n)$.
6580:The \emph{loop order} of a stable graph~$\Gamma$ is its first Betti
6588:For a stable graph of type $(g,n)$:
6617:\begin{definition}[Edge contraction and the stable graph differential]%
thinking
**Exploring skill documents**

I'm considering opening the skill documentation for better insight. It looks like I'll need specific files, too. I might want to search through the genus-2 content using regex or `rg`. Doing this with parallel execution could be beneficial, and perhaps checking explorer results would help. At this point, I think I should read the higher_genus files. Let’s go ahead and use `rg` across the repo for a thorough search!
exec
/bin/zsh -lc "sed -n '5805,5865p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Part~(c): scalar saturation gives
$\Theta^{\min} = \eta\otimes\Omega$ for some
$\Omega \in \widehat{\Gmod}$; the Kuranishi map vanishes by
parity (Proposition~\ref{prop:saturation-equivalence}), so the
MC equation does not constrain~$\Omega$. The identification
$\Omega_g = \lambda_g$
\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
requires the bar construction to produce
$\lambda_g$ at genus~$g$ for multi-weight algebras.
\end{proof}

\begin{proposition}[Genus-$2$ quartic dependence; \ClaimStatusProvedHere]%
\label{prop:f2-quartic-dependence}%
\index{multi-generator obstruction!quartic dependence}%
The genus-$2$ free energy, computed as a graph sum over the seven
stable graphs at $(g{=}2, n{=}0)$, depends linearly on the
quartic shadow coefficient~$S_4$ \textup{(LOCAL)}:
\begin{equation}\label{eq:f2-quartic-dep}
 \frac{\partial F_2}{\partial S_4} \;=\; \frac{1}{8\kappa^2} \;\neq\; 0.
\end{equation}
codex
I’ve loaded the required repo-wide sources. Next I’m auditing the actual genus-2 surface in the higher-genus chapters and nearby files to see whether the three requested ingredients already exist or are only implicit.
exec
/bin/zsh -lc "rg -n \"genus-2|genus 2|stable graphs|period matrix|Siegel|\\bOmega\\b|\\b\\tau\\b|2x2|2\\\\times 2|seven stable graphs|7 stable graphs\" chapters/theory chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,320p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1668

chapters/frame/preface_sections10_13_draft.tex:354:$r(z)=k\Omega/z$ (Yang's solution of the CYBE),
chapters/connections/thqg_open_closed_realization.tex:331:\Omega^{\bullet}_{\overline{\mathcal{M}}_g}(\log D),
chapters/frame/preface_sections2_4_draft.tex:62:where $\Omega=(\Omega_{jk})$ is the period matrix of~$X$
chapters/frame/preface_sections2_4_draft.tex:79:(\mathrm{Im}\,\Omega)^{-1}_{jk}\,
chapters/frame/preface_sections2_4_draft.tex:83:The period correction $(\mathrm{Im}\,\Omega)^{-1}_{jk}$
chapters/frame/preface_sections2_4_draft.tex:90:matrix~$\Omega$.
chapters/frame/preface_sections2_4_draft.tex:372:operations indexed by connected stable graphs of arbitrary genus,
chapters/frame/preface_sections2_4_draft.tex:387:by \emph{connected stable graphs}. A connected
chapters/frame/preface_sections2_4_draft.tex:416:the operadic bar construction, replaces trees by stable graphs:
chapters/frame/preface_sections2_4_draft.tex:452:a chain complex spanned by stable graphs, graded by edge number,
chapters/frame/preface_sections2_4_draft.tex:862:obtained by summing over all stable graphs of fixed type:
chapters/frame/preface_sections2_4_draft.tex:1165: & inversion $\Omega(\barB(\cA))\xrightarrow{\sim}\cA$
chapters/frame/guide_to_main_results.tex:360:$\barB$: bar functor. $\Omega$: cobar functor.
chapters/connections/editorial_constitution.tex:1641: determined by a Green's form $G \in \Omega^{n-1}(M \times M
chapters/connections/editorial_constitution.tex:2027:\item Bar-cobar inversion $\Omega(\barB(\cA)) \simeq \cA$
chapters/connections/editorial_constitution.tex:2318:$\barB(\cA) \dashv \Omega(\barB(\cA))$ models the
chapters/connections/feynman_connection.tex:26:differential terms and tree-level stable graphs: the Feynman
chapters/connections/genus_complete.tex:62:\[\bar{B}^{(1),n}_{\text{geom}}(\mathcal{A}) = \Gamma\left(\overline{C}_{n+1}^{(1)}(E_\tau), j_*j^*\mathcal{A}^{\boxtimes(n+1)} \otimes \Omega^n_{ell}(\log D)\right)\]
 succeeded in 50ms:
\chapter{Higher genus}
\label{chap:higher-genus}

\index{higher genus!bar complex|textbf}
\index{quantum corrections|textbf}

Everything up to this point takes place at genus zero; but
genus zero on a curve is not the same as ``over a point.''
The bar differential $\dfib$ is constructed from collision
residues on the Fulton--MacPherson compactification
$\overline{C}_n(X)$, its nilpotency $\dfib^{\,2} = 0$ uses
the Arnold relations among the forms
$\eta_{ij} = d\log(z_i - z_j)$ on the diagonal complement,
and the higher $A_\infty$ operations $m_n$ for $n \geq 3$ are
transferred along a retract whose source is
$C_*(\overline{\mathcal{M}}_{0,n+1})$, the chain complex of the
Stasheff associahedron. The formal-disk restriction that recovers
classical Koszul duality over a point is a homotopy retract: it is
additional data, not a tautology.

 succeeded in 50ms:
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

 succeeded in 51ms:
\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.

Bar-cobar inversion (Theorem~B) proves that
$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
The proof uses one fact: the bar differential squares to zero.
At genus~$g \geq 1$, this fact fails fiberwise.
The bar complex $\barB^{(g)}(\cA)$ acquires curvature
\[
 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
\]
%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
where $\omega_g = c_1(\lambda)$ is the Hodge class on
$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
The fiberwise differential no longer squares to zero; cobar inversion,
as stated, does not extend.

exec
/bin/zsh -lc 'rg -n "genus-2" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
22943:\index{stable graphs!genus-2 multi-channel catalogue}
23101:\index{$\cW_3$!genus-2 graph-by-graph calculation|textbf}
23430:\index{$\cW_3$!genus-2 arithmetic verification|textbf}%
23509:\index{stable graphs!genus-2 intersection decomposition}%
25148:% A: Smooth genus-2:
25873:\index{$\cW_3$!genus-2 cross-channel correction}
25874:\index{cross-channel correction!genus-2}
26548:\index{Pixton ideal!genus-2 MC bridge|textbf}
26549:\index{genus-2 amplitude!MC decomposition}
32456:% genus-0 loop + bridge to genus-2
32694:% Verlinde formula recovery, genus-2 ordered chiral homology
33611:% PE-1: r-matrix. Family: affine KM sl_2 on genus-2 curve.
exec
/bin/zsh -lc 'rg -n "seven stable graphs" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
22351: \textup{(}among the seven stable graphs of\/
22708: seven stable graphs; and
22944:The seven stable graphs of $\overline{\mathcal{M}}_{2,0}$
23511:The seven stable graphs $\Gamma_0, \ldots, \Gamma_6$ of
25230:\caption{The seven stable graphs of
exec
/bin/zsh -lc "sed -n '22290,22370p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
vacuum vector of~$\cA$ lies in~$V$ and $\ell_2^{(0)}$
restricts to a unital multiplication on~$V$ (satisfied for
all standard families).
\end{proof}

\begin{theorem}[Multi-weight genus expansion; \ClaimStatusProvedHere]
\label{thm:multi-weight-genus-expansion}
\label{thm:multi-generator-universality}
\index{multi-generator obstruction!genus expansion|textbf}%
\index{multi-weight genus expansion|textbf}%
\index{cross-channel correction|textbf}%
\index{Faber--Pandharipande formula!multi-weight decomposition}%
\index{genus expansion!multi-channel graph sum}%
Let\/ $\cA$ be a modular Koszul chiral algebra with
strong generators $\varphi_1, \ldots, \varphi_r$ of conformal
weights $h_1, \ldots, h_r$, per-channel modular characteristics
$\kappa_1, \ldots, \kappa_r$
\textup{(}Theorem~\textup{\ref{thm:shadow-channel-decomposition})},
and total modular characteristic\/
$\kappa(\cA) = \sum_{i=1}^r \kappa_i$.
exec
/bin/zsh -lc 'rg -n "period matrix" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
10012:with $\Omega$ the period matrix, giving
23002:Writing the genus-$2$ period matrix in full form as
27009:For a genus-$g$ tropical curve with period matrix
27022:period matrix. The tropical degeneration $\tau \to t\Omega$,
33245:theta function; (ii)~the period matrix
33262:with Siegel period matrix
33738:period matrix $\Omega \in \HHH_2$, and satisfies a
33843:generic off-diagonal period matrix $\Omega$ to relative
34325:In the non-separating degeneration, the period matrix
34510:(i)~At $\Omega_{12} = 0$, the period matrix is
exec
/bin/zsh -lc "sed -n '22980,23040p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{remark}[Evidence for a motivic genus ladder in the averaging kernel]
\label{rem:motivic-evidence-genus2-averaging-kernel}
\index{averaging kernel!motivic evidence}
Remark~\ref{rem:five-theorems-as-av-images} isolates the ordered
$E_1$ data discarded by the coinvariant projection
$\operatorname{av}$. The low-genus evidence suggests that
$\ker(\operatorname{av})$ carries a genus-sensitive period theory.

At genus~$0$, the ordered boundary integrals on configuration spaces
are controlled by mixed Tate periods. At genus~$1$, the elliptic
propagator introduces the quasi-modular sector generated by
$E_2^*, E_4, E_6$, and the genus-$1$ averaging kernel enlarges
accordingly. At genus~$2$,
Computation~\ref{comp:genus2-multichannel-catalogue} shows that the
stable-graph sum is already a seven-term object. The seven graphs are
organized by three outer topological templates: the smooth irreducible
genus-$2$ graph~A; the non-separating shell $B,D,E$ obtained from a
genus-$1$ component with a self-loop and its deeper degenerations; and
the separating shell $C,F,G$ obtained from two genus-$1$ vertices

thinking
**Clarifying tool usage**

I realize I might have used a subagent even though the user didn’t explicitly ask for it. The developer mentioned using the explorer for all codebase questions, but the AGENTS skill suggests using subagents only if requested. This feels a bit conflicting! However, the developer's guidance to always prefer explorers seems to take precedence. I might also need to consider opening the beilinson-rectify skill. It's a bit tricky to navigate!
codex
The higher-genus foundations file already has a large genus-2 surface. I’m now checking whether it actually contains the two concrete items you asked for, or whether genus-2 is described only abstractly and still needs a scoped repair remark.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4208,4290p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2288,2460p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"7 stable graphs|seven stable graphs|stable graphs at \\(g\\{=}2, n\\{=}0\\)|genus-2 stable graphs|g=2, n=0|stable graph\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
integral $\int_{\overline{\cM}_{1,1}} \psi \cdot \lambda_1 = \lambda_1^{FP} = 1/24$
normalizes the genus-$1$ term in the universal generating function.
The complementarity column follows from Theorem~\ref{thm:quantum-complementarity-main}
evaluated at $g=1$.
\end{proof}

\section{\texorpdfstring{Genus $2$}{Genus 2}}
\label{sec:genus-2-complete}

\subsection{The genus 2 case}

\begin{remark}[Genus 2 vs higher genus]
\label{rem:genus2-special}
Genus~$2$ is the first case with period matrices, spin structures
(16 characteristics), hyperelliptic involution, and the Schottky
problem. For $g\geq 3$, the full Teichm\"uller theory is needed.
\end{remark}

\subsection{\texorpdfstring{The moduli space $\mathcal{M}_2$}{The moduli space M-2}}

 succeeded in 52ms:
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

\section{Genus 2 OPE contributions: A concrete example in full detail}
\label{sec:genus_2_ope_example}

\subsection{Setting: genus 2 Riemann surfaces}

\subsubsection{\texorpdfstring{Moduli space $\mathcal{M}_2$}{Moduli space M-2}}

A genus 2 Riemann surface can be represented as:
\[\Sigma_2 = \mathbb{H}/\Gamma\]
where $\mathbb{H}$ is the upper half-plane and $\Gamma \subset \operatorname{PSL}(2,\mathbb{R})$
is a Fuchsian group.

The moduli space $\mathcal{M}_2$ has complex dimension $3g-3 = 3$, with coordinates given by period matrices $\Omega \in \mathbb{H}_2$ (Siegel upper half-space) and volume form $d\mu_{\text{WP}}$ (Weil--Petersson).

\subsubsection{The period matrix}

Explicitly, choose a symplectic basis $\{a_1, a_2, b_1, b_2\}$ of $H_1(\Sigma_2, \mathbb{Z})$
with intersection form:
\[a_i \cdot b_j = \delta_{ij}, \quad a_i \cdot a_j = b_i \cdot b_j = 0\]
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:46:irreducible stable graph
chapters/theory/higher_genus_foundations.tex:53:through the Feynman transform, summing over stable graphs
chapters/theory/higher_genus_foundations.tex:54:weighted by handles. The passage from trees to stable graphs
chapters/theory/higher_genus_foundations.tex:63:\emph{connected stable graph}~$\Gamma$ with a genus label~$g(v)$
chapters/theory/higher_genus_foundations.tex:73:The passage from trees to stable graphs corresponds to the passage from
chapters/theory/higher_genus_foundations.tex:75:operations are indexed by all stable graphs, not just trees, and
chapters/theory/higher_genus_foundations.tex:86:the unique stable graph $\Gamma_{\mathrm{irr}}$ with one vertex of
chapters/theory/higher_genus_foundations.tex:482:one-loop stable graph \textup{(}the tadpole\textup{)} evaluated
chapters/theory/higher_genus_foundations.tex:5820:stable graphs at $(g{=}2, n{=}0)$, depends linearly on the
chapters/theory/higher_genus_foundations.tex:6427:that every edge of every stable graph carries the same weight-$1$
chapters/theory/higher_genus_foundations.tex:6530:\section{Quantum chiral homology from stable graph topology}
chapters/theory/higher_genus_foundations.tex:6533:\index{stable graph!topology|textbf}
chapters/theory/higher_genus_foundations.tex:6539:direction: starting from the combinatorics of stable graphs alone,
chapters/theory/higher_genus_foundations.tex:6549:\subsection{The stable graph complex}
chapters/theory/higher_genus_foundations.tex:6551:\index{stable graph!complex|textbf}
chapters/theory/higher_genus_foundations.tex:6554:A \emph{stable graph} of type $(g,n)$ is a connected graph
chapters/theory/higher_genus_foundations.tex:6574:classes of stable graphs of type $(g,n)$.
chapters/theory/higher_genus_foundations.tex:6580:The \emph{loop order} of a stable graph~$\Gamma$ is its first Betti
chapters/theory/higher_genus_foundations.tex:6588:For a stable graph of type $(g,n)$:
chapters/theory/higher_genus_foundations.tex:6617:\begin{definition}[Edge contraction and the stable graph differential]%

thinking
**Summarizing genus-2 content and editing guidance**

I'll gather evidence on explicit genus-2 computations, the enumeration of 7 stable graphs, and the 2x2 period matrix from the specified files with line references. Then I'll clarify which file—`higher_genus_foundations.tex` or `higher_genus_modular_koszul.tex`—is most appropriate for adding missing content based on their general scope and focus. I'll produce a concise bullet-list summary with file paths and line anchors referencing the key points.
codex
- **Explicit genus‑2 computation is already present.** Proposition “Genus‑2 quartic dependence” in `chapters/theory/higher_genus_foundations.tex:5820-5854` spells out the graph sum over the seven stable graphs at $(g{=}2,n{=}0)$, isolates the banana graph, and records the resulting nonzero derivative $\frac{\partial F_2}{\partial S_4}=1/(8\kappa^2)$, so the higher‑genus foundations file already houses the concrete computation you asked about.

- **Seven stable graphs have been enumerated.** `chapters/theory/higher_genus_modular_koszul.tex:22351-22960` (see the multi‑weight genus expansion theorem and the surrounding figure captions) explicitly refers to “the seven stable graphs of $\overline{\mathcal{M}}_{2,0}$” and describes the sunset/theta/bridge slices that contribute to $\delta F_2^{\mathrm{cross}}(\cA)$; the figure referenced there (`fig:genus2-stable-graphs`) fixes the catalogue.

- **The genus‑2 $2\times 2$ period matrix is defined.** `chapters/theory/higher_genus_foundations.tex:4252-4267` gives “Definition [Period matrix: genus-2 case]”, writing $\Omega=\begin{pmatrix}\oint_{B_i}\omega_j\end{pmatrix}\in\mathbb{H}_2$ with the canonical basis, so the foundational file already covers the Siegel matrix you mentioned.

- **Editing guidance.** For missing or expanded general moduli/period-matrix context (propagators, theta functions, stable-graph machinery) keep the work in `higher_genus_foundations.tex`; for missing genus-2 graph sums, multi-channel cross-channel formulas, or modular-Koszul consequences, update `higher_genus_modular_koszul.tex` (it already hosts the detailed genus-2 enumeration and cross-channel corrections).


thinking
**Assessing computational issues**

I think I can confirm that explicit computation, enumeration, and the 2x2 period matrix are valid in their respective areas. However, since the user explicitly wants to address potential issues, I need to investigate if there are problems, like contradictory counts or missing cross-links within the assigned scope. I can certainly correct any contradictions I find and possibly add a remark linking the stable graph catalogue to the explicit computation to enhance the search surface.
thinking
**Waiting for results**

I'm thinking about whether I should include some commentary on the evidence while I wait for the explorer results. I guess it might help set the stage for whatever findings come up. It's kind of like preparing myself and being ready to connect the dots once the information is available. This approach feels like a good way to stay productive even if I can't move forward just yet.
collab wait(call_VWC81HHgWfXDbhMocwQL6VR0)
  receivers: 019d87c7-a025-77f0-b166-3fcdf7f4aa5c
wait(call_VWC81HHgWfXDbhMocwQL6VR0) 1 agents complete:
  019d87c7-a025-77f0-b166-3fcdf7f4aa5c completed: "- **Explicit genus‑2 computation is already present.** Proposition “Genus‑2 quartic dependence” in `chapters/theory/high…"

thinking
**Investigating computation issues**

I need to confirm the calculations and specifically look into the lines mentioning "six stable graphs." That could be where the main problem lies. I wonder if I should open and examine those areas more closely. It’s possible that focusing on this aspect might clear up any confusion or errors we're facing. Let's dive into that and see what we find!
codex
The repo already contains all three requested ingredients, but I found an internal contradiction inside `higher_genus_modular_koszul.tex`: two later passages still say genus~2 has six stable graphs even though the file’s own catalogue and figure use the canonical count `7`. I’m verifying those exact locations before patching.
exec
/bin/zsh -lc "sed -n '22930,23020p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '22330,22410p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '23840,23910p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '24055,24105p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 mixed-channel boundary graphs of\/ $\overline{\mathcal{M}}_{g,0}$
 \textup{(}Construction~\textup{\ref{constr:cross-channel-graph-sum}}).

\item \emph{Genus-$1$ universality.}
 $\delta F_1^{\mathrm{cross}} = 0$ for all\/~$\cA$.

\item \emph{Uniform-weight universality.}
 If\/ $h_1 = h_2 = \cdots = h_r$, then\/
 $\delta F_g^{\mathrm{cross}} = 0$ for all\/ $g \geq 1$
 \textup{(}Theorem~\textup{\ref{thm:algebraic-family-rigidity})}.

\item \emph{$R$-matrix independence.}
 The cross-channel correction $\delta F_g^{\mathrm{cross}}$
 is independent of the Givental $R$-matrix:
 genus-$0$ boundary vertices receive no $R$-contribution,
 and genus-$1$ vertices on\/ $\overline{\mathcal{M}}_{1,1}$
 have vanishing $R$-correction for degree reasons.

\item \emph{Genus-$2$ explicit formula.}
 At genus~$2$, the cross-channel correction sums over
 succeeded in 51ms:
The propagator variance $\delta_{\mathrm{mix}}$
(Proposition~\ref{prop:propagator-variance}) is the degree-$4$
projection of the cross-channel non-autonomy: it measures the
failure of the quartic gradient to be curvature-proportional.
The genus-$2$ correction
$\delta F_2^{\mathrm{cross}}$ involves graph amplitudes at
degree~$\leq 6$ (the theta graph has valence $3 + 3 = 6$),
controlled by $\delta_{\mathrm{mix}}$ at leading order.
\end{remark}

\begin{computation}[Genus-$2$ stable graph catalogue:
multi-channel data]
\label{comp:genus2-multichannel-catalogue}
\index{stable graphs!genus-2 multi-channel catalogue}
The seven stable graphs of $\overline{\mathcal{M}}_{2,0}$
(Figure~\ref{fig:genus2-stable-graphs}), with their
cross-channel contributions for a rank-$2$ algebra with
channels $\{1, 2\}$:
\begin{center}
\small
 succeeded in 50ms:
$\delta F_2^{\mathrm{HS}} := \delta F_2^{\mathrm{full}}
- \delta F_2^{\mathrm{grav}}$ is $3$--$30\%$ of the
gravitational part depending on~$c$:
at $c = 1$, $\delta F_2^{\mathrm{HS}} / \delta F_2^{\mathrm{grav}}
\approx 3\%$; at $c = 100$, $\approx 27\%$; at $c \to \infty$,
$\delta F_2^{\mathrm{HS}} / \delta F_2^{\mathrm{grav}}
\to (3\sqrt{10})/(3\sqrt{10} + 28) \approx 25\%$.
As $c \to \infty$:
\begin{equation}\label{eq:w4-large-c}
\delta F_2^{\mathrm{full}}(\cW_4)
\;\xrightarrow{\;c \to \infty\;}
\frac{3\sqrt{10} + 28}{192}
\;\approx\; 0.195.
\end{equation}

\textup{(}\texttt{test\_theorem\_w4\_full\_ope\_delta\_f2\_engine.py};
$7$~independent verification paths including direct per-graph
symbolic computation, float graph sum, gravitational limit recovery,
large-$c$ asymptotics, Koszul duality check, and comparison
with~$\cW_3$.\textup{)}
 succeeded in 51ms:
Dumbbell & $0$ & single edge \\
Theta
 & $9g_{334}^2/(16c) + 6g_{345}^2/(5c) + g_{455}^2/c + 25/c$
 & rational \\
Lollipop & $g_{334}/64 + g_{455}/48 + 1/4$ & irrational \\
Barbell
 & $9g_{334}^2/(32c) + 3g_{334}g_{444}/(4c)
 + 3g_{334}g_{455}/(4c)$ & \\
 & ${}+ g_{444}g_{455}/c + g_{455}^2/(2c) + 48/c$
 & rational $+$ irrational \\
\hline
\end{tabular}
\end{center}

\textup{(}\texttt{test\_w5\_full\_ope\_delta\_f2\_engine.py};
$8$~independent verification paths including direct per-graph
symbolic computation, float graph sum, gravitational limit
recovery, large-$c$ asymptotics, Koszul duality check,
comparison with~$\cW_3$ and~$\cW_4$, and Galois rank
verification.\textup{)}


thinking
**Clarifying stable graphs**

I'm looking at the concept of stable graphs. It seems that there are mentions of seven stable graphs, but perhaps it reduces to six boundary stable graphs if we exclude the smooth irreducible graph. I should inspect the surrounding computations and statements regarding W4/W5 to understand the contributions more clearly. The six graphs are likely the figure-eight, dumbbell, banana, theta, lollipop, and barbell, but I need to clarify the exact enumeration to avoid confusion. I’ll search for earlier lists or figures to verify this.
thinking
**Searching for computation statements**

I need to find relevant computation statements related to W4 and W5. There might be a table listing the six graphs within those computations. I should look at the earlier sections around these computations to gather enough information. It might be possible to patch the proof if I can identify enough details. I could also search for the term "banana" to see if it leads me to useful references regarding the graphs.
codex
I found the contradiction source. The file is mixing two different counts without saying so: `7` total stable graphs of `\overline{\mathcal{M}}_{2,0}`, but only `6` boundary graphs after excluding the smooth interior stratum. I’m patching those proofs to state that distinction explicitly instead of leaving the wrong raw count.

thinking
**Inspecting files for updates**

I need to check in on the latest updates before I dive into editing. I've wrapped up that first part and now I'm considering examining the specific line numbers. I think I’ll also look into another area. To do this, I’ll use the command `rg` to search for "six stable graphs" in the two files. That should help me locate everything I need efficiently!
exec
/bin/zsh -lc "rg -n \"six stable graphs|6 stable graphs|reduces to the six stable graphs|At genus~\\\\\\"'$2'"\\\\\\"'$ there are six stable graphs" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:23863:At genus~$2$ there are six stable graphs.
chapters/theory/higher_genus_modular_koszul.tex:24078:Again the genus-$2$ computation reduces to the six stable graphs.

thinking
**Inspecting line numbering**

I think I need to look more closely at the lines with exact numbering, and using a command like "nl -ba" might help. That could allow me to see line numbers clearly, but I'm also pondering if there are other methods I should consider. It's important to make sure I get this right, so using the best tool for the job will be key to ensure accurate inspection. Let's see how it goes!
codex
I’ve narrowed the write scope to two proof sentences in `higher_genus_modular_koszul.tex`. The edit is minimal: preserve the computation, fix the count, and make the boundary-vs-total distinction explicit so the file agrees with its own genus-2 catalogue.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '23856,24086p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 23856	$7$~independent verification paths including direct per-graph
 23857	symbolic computation, float graph sum, gravitational limit recovery,
 23858	large-$c$ asymptotics, Koszul duality check, and comparison
 23859	with~$\cW_3$.\textup{)}
 23860	\end{computation}
 23861	
 23862	\begin{proof}
 23863	At genus~$2$ there are six stable graphs.
 23864	The figure-eight and dumbbell graphs vanish by the same single-edge
 23865	channel-purity mechanism as in the $\cW_3$ computation, so only the
 23866	banana, theta, lollipop, and barbell graphs contribute.
 23867	Substituting the Hornfeck couplings
 23868	\eqref{eq:hornfeck-couplings} into those four graph amplitudes and
 23869	summing them gives the master formula \eqref{eq:w4-master-formula}.
 23870	Separating the even powers of the couplings from the odd powers yields
 23871	the decomposition into the rational part $R(c)$ and the two irrational
 23872	terms $I_1(c)$ and $I_2(c)$.
 23873	The large-$c$ limit and the comparison with the gravitational lower
 23874	bound are then obtained by expanding those closed forms asymptotically.
 23875	\end{proof}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5810,5858p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4248,4272p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"fig:genus2-stable-graphs|seven stable graphs of \\\\overline\\{\\\\cM\\}_\\{2,0\\}|seven stable graphs of \\\\overline\\{\\\\mathcal\\{M\\}\\}_\\{2,0\\}|\\"'$7'"\\"'$ stable graphs of '"\\"'$'"\\\\overline\\{\\\\cM\\}_\\{2,0\\}\\"'$" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5810	$\Omega_g = \lambda_g$
  5811	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
  5812	requires the bar construction to produce
  5813	$\lambda_g$ at genus~$g$ for multi-weight algebras.
  5814	\end{proof}
  5815	
  5816	\begin{proposition}[Genus-$2$ quartic dependence; \ClaimStatusProvedHere]%
  5817	\label{prop:f2-quartic-dependence}%
  5818	\index{multi-generator obstruction!quartic dependence}%
  5819	The genus-$2$ free energy, computed as a graph sum over the seven
  5820	stable graphs at $(g{=}2, n{=}0)$, depends linearly on the
  5821	quartic shadow coefficient~$S_4$ \textup{(LOCAL)}:
  5822	\begin{equation}\label{eq:f2-quartic-dep}
  5823	 \frac{\partial F_2}{\partial S_4} \;=\; \frac{1}{8\kappa^2} \;\neq\; 0.
  5824	\end{equation}
  5825	The $S_4$-dependence enters through the banana graph
  5826	\textup{(}one genus-$0$ vertex with two self-loops, $|\operatorname{Aut}| = 8$\textup{)},
  5827	which has amplitude $(S_4 / \kappa^2) / 8$.
  5828	No other graph at $(2,0)$ involves~$S_4$.
  5829	\end{proposition}
 succeeded in 52ms:
  4248	\end{definition}
  4249	
  4250	\begin{definition}[Period matrix: genus-2 case]
  4251	\label{def:period-matrix-g2}
  4252	Let $\Sigma_2$ be a genus-2 Riemann surface with canonical homology basis:
  4253	\begin{equation}
  4254	\{A_1, A_2, B_1, B_2\} \quad \text{with} \quad A_i \cap B_j = \delta_{ij}, \quad A_i \cap A_j = B_i \cap B_j = 0
  4255	\end{equation}
  4256	
  4257	Let $\{\omega_1, \omega_2\}$ be the normalized holomorphic 1-forms satisfying:
  4258	\begin{equation}
  4259	\oint_{A_j} \omega_i = \delta_{ij}
  4260	\end{equation}
  4261	
  4262	The period matrix is:
  4263	\begin{equation}
  4264	\Omega = \begin{pmatrix} 
  4265	\oint_{B_1} \omega_1 & \oint_{B_2} \omega_1 \\
  4266	\oint_{B_1} \omega_2 & \oint_{B_2} \omega_2
  4267	\end{pmatrix}
 exited 2 in 51ms:
rg: regex parse error:
    (?:fig:genus2-stable-graphs|seven stable graphs of \overline\{\cM\}_\{2,0\}|seven stable graphs of \overline\{\mathcal\{M\}\}_\{2,0\}|$7$ stable graphs of $\overline\{\cM\}_\{2,0\}$)
                                                       ^^
error: unrecognized escape sequence




thinking
**Considering audit summary details**

I need to produce a concise audit summary that highlights problem lines and specific edits. I should check for any references to "six stable graphs" and verify if they exist after the patch. The user's request as an adversarial auditor suggests I focus on fixing contradictions. There's possibly no mention of the period matrix in "modular_koszul," but it appears in "foundations." I might want to add a remark in "modular_koszul" that references this connection. I’ll also check for contradictions in "higher_genus_foundations" and any potential inaccuracies in genus-2 content.
thinking
**Investigating graph references**

I’m looking to search for "seven stable graphs" and "six stable graphs" in "modular_koszul." I’m wondering if "six boundary stable graphs" could be missing. There's also an issue with Theorem lines 23863/24078 mentioning graphs like "banana, theta, lollipop, and barbell," while the earlier catalogue refers to different names like "sunset" and "bridge-loop." They might be synonyms, but I need to check for alignment with figure labels. To ensure exhaustiveness, I should look for any counting mismatches or missing remarks. I'll also inspect any mention of genus-2 stable graphs to confirm there are no contradictions.
thinking
**Checking theorems and computations**

I’m considering whether there’s a line in a theorem that mentions "among the seven stable graphs" and if other references regarding "sum over all stable graphs at genus g and degree n" are consistent. I might need to look around line 25230 for anything relevant, like figure captions, but it might not be crucial. I could also search for "six stable graphs" throughout the entire repository. The user specifically asked about genus-2 content and any explicit computations related to it, like the enumeration of seven stable graphs or a 2x2 period matrix. If something is missing, I should note that a remark should be added.
thinking
**Clarifying graph details**

I want to include cross-references for clarity while avoiding unnecessary punctuation like em dashes. Instead, I’ll use semicolons or separate sentences. For instance: "At genus 2, there are seven stable graphs in total (Computation \ref{comp:genus2-multichannel-catalogue}); the smooth graph has no edges, so the boundary graph sum for the cross-channel correction runs over the remaining six." I’ll check line lengths too, ensuring there’s no AI sloppiness. Finally, I need to ensure I use apply_patch only.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -23862,3 +23862,6 @@
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
@@ -24077,3 +24080,6 @@
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
apply_patch(auto_approved=true) exited 0 in 29ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3ff1c57fb9b3774c5507cd94a08f8abb3aabce64..3d909c63678258706d014a202ad2c66dc68acc02
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -23860,7 +23860,10 @@
 \end{computation}
 
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
 channel-purity mechanism as in the $\cW_3$ computation, so only the
 banana, theta, lollipop, and barbell graphs contribute.
@@ -24075,7 +24078,10 @@
 \end{computation}
 
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
 and the figure-eight and dumbbell graphs remain zero by single-edge
 channel purity.

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3ff1c57fb9b3774c5507cd94a08f8abb3aabce64..3d909c63678258706d014a202ad2c66dc68acc02
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -23860,7 +23860,10 @@
 \end{computation}
 
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
 channel-purity mechanism as in the $\cW_3$ computation, so only the
 banana, theta, lollipop, and barbell graphs contribute.
@@ -24075,7 +24078,10 @@
 \end{computation}
 
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
 and the figure-eight and dumbbell graphs remain zero by single-edge
 channel purity.

codex
The patch is in. I’m running a narrow verification now: no residual `six stable graphs` claims in the assigned files, and the revised proof sentences still read cleanly against the existing genus-2 catalogue and figure reference.
exec
/bin/zsh -lc "rg -n \"seven stable graphs|Period matrix: genus-2 case|genus-2 quartic dependence|\\\\mathbb\\{H\\}_2|comp:genus2-multichannel-catalogue|fig:genus2-stable-graphs\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "six stable graphs|6 stable graphs" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '23860,24086p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:seven stable graphs|Period matrix: genus-2 case|genus-2 quartic dependence|\mathbb\{H\}_2|comp:genus2-multichannel-catalogue|fig:genus2-stable-graphs)
                                                                                  ^^
error: unrecognized escape sequence
 exited 1 in 51ms:

 succeeded in 50ms:
 23860	\end{computation}
 23861	
 23862	\begin{proof}
 23863	At genus~$2$ there are seven stable graphs in total
 23864	\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
 23865	the smooth graph has no edges, so the boundary graph sum for the
 23866	cross-channel correction runs over the remaining six.
 23867	The figure-eight and dumbbell graphs vanish by the same single-edge
 23868	channel-purity mechanism as in the $\cW_3$ computation, so only the
 23869	banana, theta, lollipop, and barbell graphs contribute.
 23870	Substituting the Hornfeck couplings
 23871	\eqref{eq:hornfeck-couplings} into those four graph amplitudes and
 23872	summing them gives the master formula \eqref{eq:w4-master-formula}.
 23873	Separating the even powers of the couplings from the odd powers yields
 23874	the decomposition into the rational part $R(c)$ and the two irrational
 23875	terms $I_1(c)$ and $I_2(c)$.
 23876	The large-$c$ limit and the comparison with the gravitational lower
 23877	bound are then obtained by expanding those closed forms asymptotically.
 23878	\end{proof}
 23879	
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3ff1c57fb9b3774c5507cd94a08f8abb3aabce64..3d909c63678258706d014a202ad2c66dc68acc02
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -23860,7 +23860,10 @@
 \end{computation}
 
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
 channel-purity mechanism as in the $\cW_3$ computation, so only the
 banana, theta, lollipop, and barbell graphs contribute.
@@ -24075,7 +24078,10 @@
 \end{computation}
 
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
 and the figure-eight and dumbbell graphs remain zero by single-edge
 channel purity.

codex
The wording fix is consistent, and the old bad count is gone. I’m doing one last evidence pass so the closeout can state exactly where the three requested genus-2 ingredients already live in the source.
exec
/bin/zsh -lc 'rg -n -F "The genus-2 free energy, computed as a graph sum over the seven" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Period matrix: genus-2 case" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"The seven stable graphs of \\overline{\\mathcal{M}}_{2,0}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
4250:\begin{definition}[Period matrix: genus-2 case]
 exited 1 in 52ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3ff1c57fb9b3774c5507cd94a08f8abb3aabce64..3d909c63678258706d014a202ad2c66dc68acc02
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -23860,7 +23860,10 @@
 \end{computation}
 
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
 channel-purity mechanism as in the $\cW_3$ computation, so only the
 banana, theta, lollipop, and barbell graphs contribute.
@@ -24075,7 +24078,10 @@
 \end{computation}
 
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
 and the figure-eight and dumbbell graphs remain zero by single-edge
 channel purity.


thinking
**Troubleshooting string search**

It seems like the fixed string search failed, possibly due to needing a simpler pattern or dealing with escape characters. For the phrase "The genus-$2$ free energy, computed as a graph sum over the seven," I could try escaping the dollar sign since it's in the shell. Maybe using single quotes will help. I’m thinking I might just run a direct search instead to see if that resolves the issue!
exec
/bin/zsh -lc "rg -n -F 'The genus-"'$2$ free energy, computed as a graph sum over the seven'"' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'The seven stable graphs of "'$'"\\overline{\\mathcal{M}}_{2,0}"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5819:The genus-$2$ free energy, computed as a graph sum over the seven
 succeeded in 51ms:
22945:The seven stable graphs of $\overline{\mathcal{M}}_{2,0}$
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3ff1c57fb9b3774c5507cd94a08f8abb3aabce64..3efa2bd0b2c95be618e4acf0d594ff413dcf09f0
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -552,7 +552,8 @@
 $\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
 $\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
 \emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
-not an input; $\bar{B}_X(\cA)$ itself is the Koszul dual \emph{coalgebra}.
+not an input; $\bar{B}_X(\cA)$ is the bar coalgebra computing the dual
+coalgebra.
 
 \item\label{D:genus-tower}
 A genus tower $\{\bar{B}^{(g)}_X(\cA)\}_{g \geq 0}$ extending the
@@ -23860,7 +23861,10 @@
 \end{computation}
 
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
 channel-purity mechanism as in the $\cW_3$ computation, so only the
 banana, theta, lollipop, and barbell graphs contribute.
@@ -24075,7 +24079,10 @@
 \end{computation}
 
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
 and the figure-eight and dumbbell graphs remain zero by single-edge
 channel purity.


thinking
**Considering code verification**

I think it’s important to verify my final answer, even if I don’t need to build or run anything. Running a `git diff` on the file might not be strictly necessary, but it could be really helpful to see the exact edits made. I'm considering using the command to get those details, which would help clarify what changes were implemented. This way, I can feel more confident about the final output!
exec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1176

diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index ccd33b0..3efa2bd 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -552,7 +552,8 @@ universal twisting morphism
 $\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
 $\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
 \emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
-not an input; $\bar{B}_X(\cA)$ itself is the Koszul dual \emph{coalgebra}.
+not an input; $\bar{B}_X(\cA)$ is the bar coalgebra computing the dual
+coalgebra.
 
 \item\label{D:genus-tower}
 A genus tower $\{\bar{B}^{(g)}_X(\cA)\}_{g \geq 0}$ extending the
@@ -3842,24 +3843,24 @@ therefore incorrect; the ordered theorem is
 Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3ff1c57fb9b3774c5507cd94a08f8abb3aabce64..3efa2bd0b2c95be618e4acf0d594ff413dcf09f0
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -552,7 +552,8 @@
 $\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
 $\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
 \emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
-not an input; $\bar{B}_X(\cA)$ itself is the Koszul dual \emph{coalgebra}.
+not an input; $\bar{B}_X(\cA)$ is the bar coalgebra computing the dual
+coalgebra.
 
 \item\label{D:genus-tower}
 A genus tower $\{\bar{B}^{(g)}_X(\cA)\}_{g \geq 0}$ extending the
@@ -23860,7 +23861,10 @@
 \end{computation}
 
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
 channel-purity mechanism as in the $\cW_3$ computation, so only the
 banana, theta, lollipop, and barbell graphs contribute.
@@ -24075,7 +24079,10 @@
 \end{computation}
 
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
 and the figure-eight and dumbbell graphs remain zero by single-edge
 channel purity.



thinking
**Considering git diff challenges**

I noticed that the git diff is huge because our file is dirty, so I should only mention the exact edits we made without reverting anything else. To clarify our changes, I might use `git diff -U0 -- ... | rg`, but the user might not need command output. I need to verify if any other uncommitted changes exist since we only touched two lines. It’s important to note that verification is limited due to the dirty worktree.
thinking
**Clarifying findings and remarks**

I should note that no remark was added since there wasn’t anything missing. However, the user mentioned that if something were missing, I should add a remark. Since everything is present, I didn’t add anything extra. It’s important to order findings by severity, but since there’s only one finding, that simplifies things. I might point out specific line references for the explicit genus-2 computation and the enumerated stable graphs to ensure clarity on those details.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '22940,22962p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5816,5828p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4250,4269p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 22940	
 22941	\begin{computation}[Genus-$2$ stable graph catalogue:
 22942	multi-channel data]
 22943	\label{comp:genus2-multichannel-catalogue}
 22944	\index{stable graphs!genus-2 multi-channel catalogue}
 22945	The seven stable graphs of $\overline{\mathcal{M}}_{2,0}$
 22946	(Figure~\ref{fig:genus2-stable-graphs}), with their
 22947	cross-channel contributions for a rank-$2$ algebra with
 22948	channels $\{1, 2\}$:
 22949	\begin{center}
 22950	\small
 22951	\renewcommand{\arraystretch}{1.35}
 22952	\begin{tabular}{llcccl}
 22953	\toprule
 22954	Label & Name & $|E|$ & $|\mathrm{Aut}|$
 22955	 & Assign.\ & Cross status \\
 22956	\midrule
 22957	A & smooth & $0$ & $1$ & $1$ & none (no edges) \\
 22958	B & figure-eight & $1$ & $2$ & $r$ & pure only \\
 22959	C & separating & $1$ & $2$ & $r$ & genus-$1$ universal \\
 succeeded in 52ms:
  5816	\begin{proposition}[Genus-$2$ quartic dependence; \ClaimStatusProvedHere]%
  5817	\label{prop:f2-quartic-dependence}%
  5818	\index{multi-generator obstruction!quartic dependence}%
  5819	The genus-$2$ free energy, computed as a graph sum over the seven
  5820	stable graphs at $(g{=}2, n{=}0)$, depends linearly on the
  5821	quartic shadow coefficient~$S_4$ \textup{(LOCAL)}:
  5822	\begin{equation}\label{eq:f2-quartic-dep}
  5823	 \frac{\partial F_2}{\partial S_4} \;=\; \frac{1}{8\kappa^2} \;\neq\; 0.
  5824	\end{equation}
  5825	The $S_4$-dependence enters through the banana graph
  5826	\textup{(}one genus-$0$ vertex with two self-loops, $|\operatorname{Aut}| = 8$\textup{)},
  5827	which has amplitude $(S_4 / \kappa^2) / 8$.
  5828	No other graph at $(2,0)$ involves~$S_4$.
 succeeded in 51ms:
  4250	\begin{definition}[Period matrix: genus-2 case]
  4251	\label{def:period-matrix-g2}
  4252	Let $\Sigma_2$ be a genus-2 Riemann surface with canonical homology basis:
  4253	\begin{equation}
  4254	\{A_1, A_2, B_1, B_2\} \quad \text{with} \quad A_i \cap B_j = \delta_{ij}, \quad A_i \cap A_j = B_i \cap B_j = 0
  4255	\end{equation}
  4256	
  4257	Let $\{\omega_1, \omega_2\}$ be the normalized holomorphic 1-forms satisfying:
  4258	\begin{equation}
  4259	\oint_{A_j} \omega_i = \delta_{ij}
  4260	\end{equation}
  4261	
  4262	The period matrix is:
  4263	\begin{equation}
  4264	\Omega = \begin{pmatrix} 
  4265	\oint_{B_1} \omega_1 & \oint_{B_2} \omega_1 \\
  4266	\oint_{B_1} \omega_2 & \oint_{B_2} \omega_2
  4267	\end{pmatrix}
  4268	\in \mathbb{H}_2
  4269	\end{equation}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3ff1c57fb9b3774c5507cd94a08f8abb3aabce64..26f63c806b3edb8706d3963dde3b14f93c9d0f8b
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -552,7 +552,8 @@
 $\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
 $\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
 \emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
-not an input; $\bar{B}_X(\cA)$ itself is the Koszul dual \emph{coalgebra}.
+not an input; $\bar{B}_X(\cA)$ is the bar coalgebra computing the dual
+coalgebra.
 
 \item\label{D:genus-tower}
 A genus tower $\{\bar{B}^{(g)}_X(\cA)\}_{g \geq 0}$ extending the
@@ -3842,9 +3843,9 @@
 Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 % BAR-INTRINSIC CONSTRUCTION DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1.3cm, y=1.2cm]
@@ -10296,9 +10297,9 @@
 the operad composition.
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 % FIVE-COMPONENT DIFFERENTIAL DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=2.4cm, y=1.0cm]
@@ -12382,9 +12383,9 @@
 their holographic reconstruction saturates.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 % SHADOW POSTNIKOV TOWER DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1.2cm, y=1.35cm]
@@ -13338,9 +13339,9 @@
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
 \end{proof}
 
-%% --------------------------------------------------------:
+%% ========================================================
 %% PRIMITIVE KERNEL COMPRESSION
-%% --------------------------------------------------------:
+%% ========================================================
 
 \subsection{The primitive logarithmic modular kernel}
 \label{subsec:primitive-kernel-compression}
@@ -14099,9 +14100,9 @@
 \end{enumerate}
 \end{remark}
 
-%% --------------------------------------------------------:
+%% ========================================================
 %% THE PRIMITIVE FLAT CONNECTION
-%% --------------------------------------------------------:
+%% ========================================================
 
 \subsection{The primitive flat connection and conformal block
 reconstruction}
@@ -14537,9 +14538,9 @@
 on $L_\cA^{1/2}$.
 \end{conjecture}
 
-%% --------------------------------------------------------:
+%% ========================================================
 %% END OF PRIMITIVE FLAT CONNECTION
-%% --------------------------------------------------------:
+%% ========================================================
 
 \begin{theorem}[Ran-coherent bar-cobar equivalence]
 \label{thm:ran-coherent-bar-cobar}
@@ -16993,9 +16994,9 @@
 Heisenberg, lattice, and $\beta\gamma$.
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 % SHADOW ARCHETYPE CLASSIFICATION DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=2.8cm, y=0.85cm]
@@ -21382,9 +21383,9 @@
 where $Q_{\mathrm{aut}}$ is the autonomous shadow metric (from the effective single-line data $\kappa_v = \sum\kappa_i$, $\alpha_v = \sum \alpha_i$, $S_4^v$) and $R(t)$ is a correction series. The autonomous approximation is exact through~$t^3$ (the coefficient $\tilde{q}_3 = 0$). For $\mathcal{W}_3$: $P(c) = 25c^2 + 100c - 428$ and the first correction appears at~$t^4$.
 \end{remark}
 
-%%% -------------------------------------------------------:
+%%% =======================================================
 %%% HAMILTON--JACOBI STRUCTURE AND FINITE DETERMINATION
-%%% -------------------------------------------------------:
+%%% =======================================================
 
 \begin{theorem}[Hamilton--Jacobi master equation on deformation spaces]
 \label{thm:hamilton-jacobi-shadow}
@@ -21805,9 +21806,9 @@
 at each vertex.
 \end{definition}
 
-% --------------------------------------------------------:
+% ========================================================
 % GRAPH AMPLITUDE / TAUTOLOGICAL EVALUATION DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1cm, y=1cm]
@@ -22056,9 +22057,9 @@
 \end{proof}
 
 
-% --------------------------------------------------------:
+% ========================================================
 % The Chriss--Ginzburg tautological programme
-% --------------------------------------------------------:
+% ========================================================
 
 \subsubsection{The Chriss--Ginzburg tautological programme}
 \label{subsubsec:chriss-ginzburg-tautological-programme}
@@ -23860,7 +23861,10 @@
 \end{computation}
 
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
 channel-purity mechanism as in the $\cW_3$ computation, so only the
 banana, theta, lollipop, and barbell graphs contribute.
@@ -24075,7 +24079,10 @@
 \end{computation}
 
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
 and the figure-eight and dumbbell graphs remain zero by single-edge
 channel purity.
@@ -25029,9 +25036,9 @@
 boundary-stratum pushforwards and $\psi$-class monomials.
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 % MC RELATION AT (2,0) AS VISUAL EQUATION
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1.0cm, y=1.0cm]
@@ -25242,9 +25249,9 @@
 \label{fig:genus2-stable-graphs}
 \end{figure}
 
-% --------------------------------------------------------:
+% ========================================================
 % BOUNDARY POSET OF M-BAR_{2,0}
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=2.0cm, y=1.4cm,
@@ -27047,9 +27054,9 @@
 
 
 
-% --------------------------------------------------------:
+% ========================================================
 % Non-perturbative shadow partition function
-% --------------------------------------------------------:
+% ========================================================
 
 \subsubsection{Non-perturbative shadow partition function}
 \label{subsubsec:shadow-double-convergence}
@@ -27194,9 +27201,9 @@
 \end{remark}
 
 
-% --------------------------------------------------------:
+% ========================================================
 % Analytic structure and resurgence of the shadow partition function
-% --------------------------------------------------------:
+% ========================================================
 
 \subsubsection{Analytic structure of the scalar genus series}
 \label{subsubsec:shadow-analytic-structure}
@@ -28410,9 +28417,9 @@
 \end{remark}
 
 
-% --------------------------------------------------------:
+% ========================================================
 % The envelope-shadow functor: from invariant to functor
-% --------------------------------------------------------:
+% ========================================================
 %
 % The shadow obstruction tower was constructed above as an invariant
 % of a fixed chiral algebra A. When A arises as the enveloping
@@ -28423,7 +28430,7 @@
 % dependence, and Gaussian collapse. The input data is a
 % cyclically admissible Lie conformal algebra in the sense of
 % Nishinaka [Nish26].
-% --------------------------------------------------------:
+% ========================================================
 
 \subsubsection{Cyclically admissible input and the envelope-shadow functor}
 \label{subsubsec:envelope-shadow-functor}
@@ -32422,9 +32429,9 @@
 produces corrections at all degree levels, and all $42$ graphs
 contribute beyond the scalar sector.
 
-% --------------------------------------------------------:
+% ========================================================
 % GENUS-3 STABLE GRAPH VISUAL CENSUS
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1.4cm, y=1.1cm, every node/.style={font=\scriptsize}]
@@ -33253,7 +33260,7 @@
 by $\pi_1(\Sigma_2)^n \cong (\ZZ^4)^n$ with four generators
 per point (two $A$-cycles, two $B$-cycles).
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Setup: the genus-$2$ ordered chiral chain
 complex}
 \label{subsec:genus2-setup}
@@ -33381,7 +33388,7 @@
 \omega_2 \cdot [\text{Hodge correction}]$ restores
 $(D^{(2)})^2 = 0$ at the total level.
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{The genus-$2$ KZB connection}
 \label{subsec:g2-kzb}
 
@@ -33473,7 +33480,7 @@
 parameter.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degree $0$: the center}
 \label{subsec:g2-degree0}
 
@@ -33504,7 +33511,7 @@
 $\cA$, not on the base curve.
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degree $1$: de~Rham cohomology of
 $\Sigma_2$ with Yangian coefficients}
 \label{subsec:g2-degree1}
@@ -33578,7 +33585,7 @@
 extra $1$-cycles on $\Sigma_g$.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degree $2$: the genus-$2$ KZB local system}
 \label{subsec:g2-degree2}
 
@@ -34068,7 +34075,7 @@
 the dominance of $H^1$ over $H^0$ and $H^2$.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degree $n$: genus-$2$ surface braid group
 monodromy}
 \label{subsec:g2-degree-n}
@@ -34163,7 +34170,7 @@
 product is non-vanishing for all~$n$.)
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Summary: genus $0$ vs.\ genus $1$ vs.\
 genus $2$}
 \label{subsec:genus-comparison-table}
@@ -34304,7 +34311,7 @@
 alternating sum is a useful invariant at every degree.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degenerations and genuinely genus-$2$ content}
 \label{subsec:g2-degenerations}
 


thinking
**Addressing proof discrepancies**

I’m noticing two specific problems with findings linked to proofs in graphs. The first issue is at link 23863, where it claims six stable graphs but contradicts the canonical seven-graph catalogue found at link 22941. Then, at link 24080, the proof again refers to a total genus-2 count of six, but it fails to differentiate between boundary graphs and the smooth stratum. In both cases, I've replaced the sentences to fix the issues.
codex
Explicit genus-2 content was already present, so I did not add a new remark: explicit genus-2 graph-sum computation at [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5816), the seven-graph genus-2 catalogue at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:22941), and the `2x2` period matrix definition at [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:4250).

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:23863): the proof said “At genus~$2$ there are six stable graphs,” contradicting the file’s own genus-2 catalogue of seven total stable graphs.
  EXACT edit applied: replaced that sentence with “At genus~$2$ there are seven stable graphs in total (Computation~\ref{comp:genus2-multichannel-catalogue}); the smooth graph has no edges, so the boundary graph sum for the cross-channel correction runs over the remaining six.”

- PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:24080): a second proof again collapsed the total genus-2 count to six without explaining that this was only the boundary part of the graph sum.
  EXACT edit applied: replaced that sentence with “Again the genus-$2$ computation starts from the seven stable graphs of (Computation~\ref{comp:genus2-multichannel-catalogue}); the smooth graph has no edges, so the boundary graph sum reduces to the remaining six.”

Narrow verification passed: no remaining `six stable graphs` claims in the assigned files. I did not run a full TeX build.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3ff1c57fb9b3774c5507cd94a08f8abb3aabce64..26f63c806b3edb8706d3963dde3b14f93c9d0f8b
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -552,7 +552,8 @@
 $\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
 $\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
 \emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
-not an input; $\bar{B}_X(\cA)$ itself is the Koszul dual \emph{coalgebra}.
+not an input; $\bar{B}_X(\cA)$ is the bar coalgebra computing the dual
+coalgebra.
 
 \item\label{D:genus-tower}
 A genus tower $\{\bar{B}^{(g)}_X(\cA)\}_{g \geq 0}$ extending the
@@ -3842,9 +3843,9 @@
 Theorem~\ref{thm:e1-mc-element}.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 % BAR-INTRINSIC CONSTRUCTION DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1.3cm, y=1.2cm]
@@ -10296,9 +10297,9 @@
 the operad composition.
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 % FIVE-COMPONENT DIFFERENTIAL DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=2.4cm, y=1.0cm]
@@ -12382,9 +12383,9 @@
 their holographic reconstruction saturates.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 % SHADOW POSTNIKOV TOWER DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1.2cm, y=1.35cm]
@@ -13338,9 +13339,9 @@
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
 \end{proof}
 
-%% --------------------------------------------------------:
+%% ========================================================
 %% PRIMITIVE KERNEL COMPRESSION
-%% --------------------------------------------------------:
+%% ========================================================
 
 \subsection{The primitive logarithmic modular kernel}
 \label{subsec:primitive-kernel-compression}
@@ -14099,9 +14100,9 @@
 \end{enumerate}
 \end{remark}
 
-%% --------------------------------------------------------:
+%% ========================================================
 %% THE PRIMITIVE FLAT CONNECTION
-%% --------------------------------------------------------:
+%% ========================================================
 
 \subsection{The primitive flat connection and conformal block
 reconstruction}
@@ -14537,9 +14538,9 @@
 on $L_\cA^{1/2}$.
 \end{conjecture}
 
-%% --------------------------------------------------------:
+%% ========================================================
 %% END OF PRIMITIVE FLAT CONNECTION
-%% --------------------------------------------------------:
+%% ========================================================
 
 \begin{theorem}[Ran-coherent bar-cobar equivalence]
 \label{thm:ran-coherent-bar-cobar}
@@ -16993,9 +16994,9 @@
 Heisenberg, lattice, and $\beta\gamma$.
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 % SHADOW ARCHETYPE CLASSIFICATION DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=2.8cm, y=0.85cm]
@@ -21382,9 +21383,9 @@
 where $Q_{\mathrm{aut}}$ is the autonomous shadow metric (from the effective single-line data $\kappa_v = \sum\kappa_i$, $\alpha_v = \sum \alpha_i$, $S_4^v$) and $R(t)$ is a correction series. The autonomous approximation is exact through~$t^3$ (the coefficient $\tilde{q}_3 = 0$). For $\mathcal{W}_3$: $P(c) = 25c^2 + 100c - 428$ and the first correction appears at~$t^4$.
 \end{remark}
 
-%%% -------------------------------------------------------:
+%%% =======================================================
 %%% HAMILTON--JACOBI STRUCTURE AND FINITE DETERMINATION
-%%% -------------------------------------------------------:
+%%% =======================================================
 
 \begin{theorem}[Hamilton--Jacobi master equation on deformation spaces]
 \label{thm:hamilton-jacobi-shadow}
@@ -21805,9 +21806,9 @@
 at each vertex.
 \end{definition}
 
-% --------------------------------------------------------:
+% ========================================================
 % GRAPH AMPLITUDE / TAUTOLOGICAL EVALUATION DIAGRAM
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1cm, y=1cm]
@@ -22056,9 +22057,9 @@
 \end{proof}
 
 
-% --------------------------------------------------------:
+% ========================================================
 % The Chriss--Ginzburg tautological programme
-% --------------------------------------------------------:
+% ========================================================
 
 \subsubsection{The Chriss--Ginzburg tautological programme}
 \label{subsubsec:chriss-ginzburg-tautological-programme}
@@ -23860,7 +23861,10 @@
 \end{computation}
 
 \begin{proof}
-At genus~$2$ there are six stable graphs.
+At genus~$2$ there are seven stable graphs in total
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum for the
+cross-channel correction runs over the remaining six.
 The figure-eight and dumbbell graphs vanish by the same single-edge
 channel-purity mechanism as in the $\cW_3$ computation, so only the
 banana, theta, lollipop, and barbell graphs contribute.
@@ -24075,7 +24079,10 @@
 \end{computation}
 
 \begin{proof}
-Again the genus-$2$ computation reduces to the six stable graphs.
+Again the genus-$2$ computation starts from the seven stable graphs of
+\textup{(}Computation~\textup{\ref{comp:genus2-multichannel-catalogue}}\textup{)};
+the smooth graph has no edges, so the boundary graph sum reduces to the
+remaining six.
 Parity eliminates the forbidden odd channels listed in the statement,
 and the figure-eight and dumbbell graphs remain zero by single-edge
 channel purity.
@@ -25029,9 +25036,9 @@
 boundary-stratum pushforwards and $\psi$-class monomials.
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 % MC RELATION AT (2,0) AS VISUAL EQUATION
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1.0cm, y=1.0cm]
@@ -25242,9 +25249,9 @@
 \label{fig:genus2-stable-graphs}
 \end{figure}
 
-% --------------------------------------------------------:
+% ========================================================
 % BOUNDARY POSET OF M-BAR_{2,0}
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=2.0cm, y=1.4cm,
@@ -27047,9 +27054,9 @@
 
 
 
-% --------------------------------------------------------:
+% ========================================================
 % Non-perturbative shadow partition function
-% --------------------------------------------------------:
+% ========================================================
 
 \subsubsection{Non-perturbative shadow partition function}
 \label{subsubsec:shadow-double-convergence}
@@ -27194,9 +27201,9 @@
 \end{remark}
 
 
-% --------------------------------------------------------:
+% ========================================================
 % Analytic structure and resurgence of the shadow partition function
-% --------------------------------------------------------:
+% ========================================================
 
 \subsubsection{Analytic structure of the scalar genus series}
 \label{subsubsec:shadow-analytic-structure}
@@ -28410,9 +28417,9 @@
 \end{remark}
 
 
-% --------------------------------------------------------:
+% ========================================================
 % The envelope-shadow functor: from invariant to functor
-% --------------------------------------------------------:
+% ========================================================
 %
 % The shadow obstruction tower was constructed above as an invariant
 % of a fixed chiral algebra A. When A arises as the enveloping
@@ -28423,7 +28430,7 @@
 % dependence, and Gaussian collapse. The input data is a
 % cyclically admissible Lie conformal algebra in the sense of
 % Nishinaka [Nish26].
-% --------------------------------------------------------:
+% ========================================================
 
 \subsubsection{Cyclically admissible input and the envelope-shadow functor}
 \label{subsubsec:envelope-shadow-functor}
@@ -32422,9 +32429,9 @@
 produces corrections at all degree levels, and all $42$ graphs
 contribute beyond the scalar sector.
 
-% --------------------------------------------------------:
+% ========================================================
 % GENUS-3 STABLE GRAPH VISUAL CENSUS
-% --------------------------------------------------------:
+% ========================================================
 \begin{figure}[ht]
 \centering
 \begin{tikzpicture}[x=1.4cm, y=1.1cm, every node/.style={font=\scriptsize}]
@@ -33253,7 +33260,7 @@
 by $\pi_1(\Sigma_2)^n \cong (\ZZ^4)^n$ with four generators
 per point (two $A$-cycles, two $B$-cycles).
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Setup: the genus-$2$ ordered chiral chain
 complex}
 \label{subsec:genus2-setup}
@@ -33381,7 +33388,7 @@
 \omega_2 \cdot [\text{Hodge correction}]$ restores
 $(D^{(2)})^2 = 0$ at the total level.
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{The genus-$2$ KZB connection}
 \label{subsec:g2-kzb}
 
@@ -33473,7 +33480,7 @@
 parameter.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degree $0$: the center}
 \label{subsec:g2-degree0}
 
@@ -33504,7 +33511,7 @@
 $\cA$, not on the base curve.
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degree $1$: de~Rham cohomology of
 $\Sigma_2$ with Yangian coefficients}
 \label{subsec:g2-degree1}
@@ -33578,7 +33585,7 @@
 extra $1$-cycles on $\Sigma_g$.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degree $2$: the genus-$2$ KZB local system}
 \label{subsec:g2-degree2}
 
@@ -34068,7 +34075,7 @@
 the dominance of $H^1$ over $H^0$ and $H^2$.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degree $n$: genus-$2$ surface braid group
 monodromy}
 \label{subsec:g2-degree-n}
@@ -34163,7 +34170,7 @@
 product is non-vanishing for all~$n$.)
 \end{proof}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Summary: genus $0$ vs.\ genus $1$ vs.\
 genus $2$}
 \label{subsec:genus-comparison-table}
@@ -34304,7 +34311,7 @@
 alternating sum is a useful invariant at every degree.
 \end{remark}
 
-% --------------------------------------------------------:
+% ========================================================
 \subsection{Degenerations and genuinely genus-$2$ content}
 \label{subsec:g2-degenerations}
 

tokens used
127,250
