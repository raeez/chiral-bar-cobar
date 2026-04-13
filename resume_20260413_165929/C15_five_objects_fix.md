# C15_five_objects_fix (643s)

**Findings**
- PROBLEM at [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:4950): the conjecture identified the Koszul dual `\cA^!` with the bulk package. EXACT edit applied: `between \cA and a candidate holographic package: the derived center \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) supplies the bulk observable algebra, the Koszul dual \cA^! supplies the line/defect sector, and the bar-cobar filtration degree maps to the radial coordinate.`

- PROBLEM at [chapters/connections/editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:2014): the AdS/CFT conjecture said `\cA^!` models bulk field content while also naming the derived centre as the bulk observables. EXACT edit applied: changed `\cA^!$ models the bulk field content` to `\cA^!$ models the line/defect sector`.

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:483): the ordered bar was described as the boundary-to-bulk map, and bulk reconstruction was framed as an upgrade of bar-cobar inversion. EXACT edit applied: replaced that passage with `\barB^{\mathrm{ord}}(\cA)` as `the boundary-side coalgebraic resolution feeding the boundary-to-bulk story`, then stated that the derived centre `is computed from Hochschild cochains using that resolution` and that Volume II adds `the separate bulk reconstruction through the derived centre`.

- PROBLEM at [chapters/examples/beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1881): the slogan `bar-cobar duality and holographic duality coincide` erased the boundary/defect/bulk distinction. EXACT edit applied: replaced it with `the boundary algebra, the Koszul-dual defect sector, and the derived-center bulk are all explicitly computable.`

- PROBLEM at [chapters/connections/thqg_introduction_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement.tex:117): the strict Koszul dual was described as coming from `Verdier/linear duality`, blurring `\cA^!` with `\cA^!_\infty`. EXACT edit applied: `\cA^! = (H^*(\barB_X(\cA)))^\vee` is now the `strict Koszul dual chiral algebra`, built from `bar cohomology and then linear duality`, and the next sentence now separately says `\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)` is the `homotopy Koszul-dual factorization algebra`.

- PROBLEM at [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:2810): the Heisenberg summary used the same `Verdier/linear duality` collapse. EXACT edit applied: replaced it with `The second arrow is linear duality on that coalgebra, producing the strict Koszul dual algebra... The separate Verdier image \mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) is the homotopy Koszul-dual factorization algebra.`

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2213): the roadmap line equated strict `\cA^!` with the Verdier image of `\barB(\cA)`. EXACT edit applied: replaced it with `\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality`.

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2670): the warning box listed only four objects and again merged linear duality with Verdier duality. EXACT edit applied: changed `Four objects.` to `Five objects.`, added `\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)` as the derived center, changed `\cA^!` to the `strict Koszul dual algebra`, and replaced `Verdier/linear duality` with `linear duality on bar cohomology, while \mathbb{D}_{\operatorname{Ran}}\barB(\cA) gives the homotopy Koszul-dual factorization algebra`.

Verification: repo-wide grep for the old bad phrases on `chapters/*.tex` came back clean after these edits. I did not run a TeX build.


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
session id: 019d8809-5b8c-7c40-bb42-a55e53daf4b0
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


Fix five-object conflation (D09 findings).
Search Vol I for paragraphs mentioning both 'bar' and 'Koszul dual' or 'derived center'.
Verify all five objects (A, B(A), A^i, A^!, Z^der) correctly distinguished.
Fix any conflation language.
mcp startup: no servers

thinking
**Interpreting assigned files**

I'm thinking it might be that the assigned files are the ones in Volume I. If so, we can only edit the files we've identified as being in scope, so I want to be thorough in my search within that scope. I'll need to find all paragraphs that match my search criteria and verify them. After that, I should fix any conflations and output my findings with specific file and line references. I might also need to produce PE protocols if there's a hot zone triggered.
codex
Using `deep-beilinson-audit` for an adversarial pass on Vol I wording, then a minimal fix pass on the exact files that conflate `A`, `B(A)`, `A^i`, `A^!`, and `Z^{der}_{ch}(A)`. I’m reading the required constitutional files first, then I’ll grep the live Vol I surface for paragraphs that mention `bar` together with `Koszul dual` or `derived center`.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
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

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

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

thinking
**Searching for relevant paragraphs**

I need to search for paragraphs using specific patterns related to bar and Koszul dual or derived center. It seems like using an explorer agent might be the best approach since this involves codebase questions. I’ll spawn the explorer to locate candidate files and paragraphs. I want to search through Vol I .tex for those terms and return file:line snippets with possible conflations. After that, I should mention the results in my commentary.
codex
I have the constitutional constraints loaded. Next I’m extracting the exact Vol I paragraphs in scope and checking each against the five-object template before touching any text.

thinking
**Considering item mention requirements**

I need to think about whether mentioning the item name is optional. It seems like it said that the display name might not be required, but it could be necessary. I need to ensure that I'm sending the information properly. Maybe I should double-check how the mention feature works to avoid any confusion. It’s important to get this right!
collab spawn_agent(call_hhhcT3FV1GEr4BPoxFiFWHRU, prompt="<task>In /Users/raeez/chiral-bar-cobar, search only Vol I .tex source for paragraphs that mention both 'bar' and either …")
mcp startup: no servers
spawn_agent(call_hhhcT3FV1GEr4BPoxFiFWHRU, prompt="<task>In /Users/raeez/chiral-bar-cobar, search only Vol I .tex source for paragraphs that mention both 'bar' and either …") pending init:
  agent: 019d8809-f986-7b60-add9-5da9ecb4205d
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar" chapters -g"*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 9003

chapters/examples/deformation_quantization.tex:18:\item \emph{Curvature.} At genus~$g > 0$, the bar complex carries
chapters/examples/deformation_quantization.tex:22: in~$\hbar$; the $\hbar$-adic filtration corresponds to the weight
chapters/examples/deformation_quantization.tex:25: quantization from order~$\hbar^n$ to~$\hbar^{n+1}$ lives in
chapters/examples/deformation_quantization.tex:27: Theorem~\ref{thm:hochschild-bar-cobar}.
chapters/examples/deformation_quantization.tex:29:Kontsevich's star product formula and the chiral bar differential are
chapters/examples/deformation_quantization.tex:41:Let $(M, \pi)$ be a Poisson manifold with Poisson bivector $\pi \in \Gamma(\wedge^2 TM)$. There exists a star product $\star: C^\infty(M)[[\hbar]] \otimes C^\infty(M)[[\hbar]] \to C^\infty(M)[[\hbar]]$ such that:
chapters/examples/deformation_quantization.tex:43:\item $f \star g = fg + \frac{\hbar}{2}\{f,g\} + O(\hbar^2)$
chapters/examples/deformation_quantization.tex:46:\[f \star g = \sum_{\Gamma} \frac{\hbar^{|\Gamma|}}{|\text{Aut}(\Gamma)|} w_\Gamma \cdot B_\Gamma(f,g)\]
chapters/examples/deformation_quantization.tex:53:The configuration spaces here are the same ones that defined the Heisenberg bar differential (\S\ref{sec:frame-bar-deg2}), now with marked boundary points replacing interior points.
chapters/examples/deformation_quantization.tex:66:At order $\hbar$, the unique admissible graph has one internal vertex in $\mathbb{H}$ with edges to the two boundary points $f, g$ on $\mathbb{R}$:
chapters/examples/deformation_quantization.tex:80:\[f \star g = fg + \frac{\hbar}{2}\{f,g\} + O(\hbar^2)\]
chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/examples/deformation_quantization.tex:147:For coisson algebras, the classical Kontsevich formality theorem ensures the vanishing of all higher obstructions at the operadic level: the $E_2$-operad (governing Poisson structures) is formal, so the deformation problem is unobstructed. Theorem~\ref{thm:geometric-equals-operadic-bar} lifts this to the curve $X$: the same object as the operadic bar construction is computed via the geometric bar complex, so formality propagates from the classical to the chiral setting. Gauge equivalence follows from the standard deformation-theoretic argument: different choices of Maurer--Cartan element in the same gauge orbit give isomorphic deformations.
chapters/examples/deformation_quantization.tex:189:Let $\mathcal{A}_{\text{cl}}$ be a coisson algebra on $X$. Its quantization $\mathcal{A}_\hbar$ has structure constants:
chapters/examples/deformation_quantization.tex:190:\[(a \star b)(w) = \sum_{\Gamma \in \mathcal{G}_n} \frac{\hbar^{n}}{|\text{Aut}(\Gamma)|} \int_{\overline{C}_n^{\text{ch}}(X)} B_\Gamma(a,b) \wedge \omega_\Gamma\]
chapters/examples/deformation_quantization.tex:240:resulting identity is precisely the $\hbar^n$ term of
chapters/examples/deformation_quantization.tex:250:The star product is $a \star b = m \circ \exp(\hbar \mathcal{F}(\pi))(a \otimes b)$
chapters/examples/deformation_quantization.tex:251:where $\pi$ is the Poisson bivector of the coisson structure. The $\hbar^0$ term is the

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Koszul dual" chapters -g"*.tex"' in /Users/raeez/chiral-bar-cobarthinking
**Updating extraction plans**

I need to think about running parallel tasks instead of just waiting around. Using regular expressions with patterns could help with candidate extraction, and maybe I should use exec_command for that. But then again, do I need to create a distinct plan for it? Updating the plan might be a good move since it's a substantial change. Let's visualize how this all ties together and decide on the next steps.
 succeeded in 50ms:
Total output lines: 1932

chapters/examples/deformation_quantization.tex:496:The $\beta\gamma$ system is Koszul dual to the $bc$ ghost system: $(\beta\gamma)^! \cong \mathcal{F}_{bc}$. This is a bosonic-to-fermionic ghost system duality realized through chiral Koszul duality (distinct from the standard boson-fermion correspondence/bosonization). The duality is visible at the level of configuration space integrals:
chapters/examples/deformation_quantization.tex:788:The paper on quadratic duality for chiral algebras \cite{GLZ22} focuses on Koszul duality for quadratic operads. The deformation quantization framework of this monograph generalizes from quadratic to arbitrary (non-quadratic via curvature), geometrizes the duality via bar-cobar configuration spaces, and provides explicit formulas for dualizing.
chapters/examples/deformation_quantization.tex:813:that the bar-cobar adjunction, restricted to the formal disk at genus~$0$, recovers classical Koszul duality, in agreement with the Francis--Gaitsgory formality
chapters/examples/w_algebras_deep.tex:354:Koszul duality $k \mapsto -k-6$ sends $Q \mapsto -Q$, implementing
chapters/examples/w_algebras_deep.tex:361:\emph{Koszul duality via Miura.}
chapters/examples/w_algebras_deep.tex:364:Under Koszul duality, the background charge transforms as
chapters/examples/w_algebras_deep.tex:428:$c = 0$ (the uncurved locus). The Koszul duality
chapters/examples/w_algebras_deep.tex:515:The bar-complex dimensions across the simple types (Table~\ref{comp:w-bar-dims}) display a uniform pattern: at each bar degree the chain spaces are infinite-dimensional but graded-finite under the conformal weight grading, and the growth rates are governed by a single discriminant $\Delta(x)$ that is invariant under both DS reduction and Koszul duality. This uniformity persists in the large-$N$ limit, made precise below.
chapters/examples/w_algebras_deep.tex:579:the bar spectral sequence to collapse at~$E_2$, and the Koszul dual to
chapters/examples/w_algebras_deep.tex:613:the Koszul dual of $\mathcal{W}_N^k$ is $\mathcal{W}_N^{k'}$
chapters/examples/w_algebras_deep.tex:803:Under Koszul duality $c \mapsto 100 - c$, the channel
chapters/examples/w_algebras_deep.tex:869:are conjectured to be Koszul dual to $\mathcal{W}_N$ at
chapters/examples/w_algebras_deep.tex:894:The conjecture posits the existence of the bar complex of $\mathcal{W}_{1+\infty}$ as a completed inverse limit, with Koszul dual determined by the 't~Hooft coupling involution $\lambda \mapsto 1 - \lambda$.
chapters/examples/w_algebras_deep.tex:973:generators does not obstruct Koszul duality because the
chapters/examples/w_algebras_deep.tex:983:%% Factorization Koszul dual of W_infty
chapters/examples/w_algebras_deep.tex:987:The factorization Koszul dual of the $\mathcal{W}_\infty$
chapters/examples/w_algebras_deep.tex:993:\subsubsection*{Warm-up: the Koszul dual of $\mathcal{W}_3$}
chapters/examples/w_algebras_deep.tex:1059:\emph{Step~2: the principal theorem identifies the Koszul dual.}
Plan update
Auditing the exact Vol I prose surface first, then applying only minimum truthful edits on files that actually conflate the five objects.
  → Search Vol I for in-scope paragraphs mentioning bar with Koszul dual or derived center
  • Read each candidate in context and classify clean vs conflated using the five-object template
  • Patch only conflated paragraphs with minimal truthful wording fixes
  • Run targeted grep verification for forbidden conflations on edited files
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "derived center" -g"*.tex" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/deformation_quantization.tex:722:(boundary deformation data); the \emph{derived center}
chapters/examples/deformation_quantization.tex:2124:chiral algebra of a Landau--Ginzburg B-model, the derived center
chapters/examples/kac_moody.tex:25:PBW filtrations, and the derived center of
chapters/examples/yangians_drinfeld_kohno.tex:6239: to the derived center;
chapters/examples/yangians_drinfeld_kohno.tex:6623: from the bulk algebra to the derived center of the boundary
chapters/frame/preface_sections10_13_draft.tex:35:\item the \emph{chiral derived center}
chapters/frame/preface_sections10_13_draft.tex:124:the bulk; the derived center classifies bulk operators acting on the
chapters/frame/preface_sections10_13_draft.tex:154:\emph{Stage~1} (local one-colour theorem: derived center is universal
chapters/frame/preface_sections10_13_draft.tex:176: $\mathcal C$ and its derived center are intrinsic.
chapters/frame/heisenberg_frame.tex:2008:physically realised by this derived center is abelian
chapters/frame/heisenberg_frame.tex:3283:with interval amplitudes (thesis item~(4), derived center); and
chapters/frame/heisenberg_frame.tex:3735:of the boundary algebra and its derived center. The cascade
chapters/frame/heisenberg_frame.tex:4819:structure on the derived center pair
chapters/frame/preface.tex:3776:operadic: the derived center is $E_2$, and only topologization raises
chapters/frame/preface.tex:3793:E_3^{\mathrm{top}}(\text{derived center}).
chapters/frame/preface.tex:3886:Each notion carries its own derived center; the five derived
chapters/frame/preface.tex:3954:derived center are defined as $E_3^{\mathrm{top}}$-algebras. Then
chapters/frame/preface.tex:4013:center, and the derived center, each recovering the next.
chapters/frame/preface.tex:4026:ideal. The Swiss-cheese operad $\SCchtop$ governs the derived center
chapters/frame/preface.tex:4046:\item the \emph{chiral derived center}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '700,760p' chapters/examples/deformation_quantization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\subsection{AdS/CFT and holography}

The bar-cobar duality admits a conjectural holographic interpretation:

\begin{conjecture}[Holographic duality; \ClaimStatusConjectured]\label{conj:deformation-holographic}
\[\text{Bulk theory on } AdS_3 \longleftrightarrow \text{Boundary chiral algebra on } S^1\]

The boundary genus expansion should model the bulk theory:
\[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
where $F_g$ are free energies computed via configuration space integrals.
(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
\end{conjecture}

\begin{remark}[Scope and the bar/center distinction]
The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.

\emph{Clarification on bar vs.\ center.}
The genus expansion $F_g$ is a projection of the universal MC
element $\Theta_\cA \in \MC(\gAmod)$, which lives in the
exec
/bin/zsh -lc "rg -l -i --glob '*.tex' 'bar' chapters appendices preface main.tex | xargs rg -l -i 'Koszul dual|derived center'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: preface: No such file or directory (os error 2)
chapters/examples/w_algebras_deep.tex
appendices/general_relations.tex
chapters/examples/deformation_quantization.tex
appendices/homotopy_transfer.tex
chapters/examples/logarithmic_w_algebras.tex
appendices/dual_methodology.tex
chapters/examples/w3_holographic_datum.tex
chapters/examples/w_algebras.tex
appendices/signs_and_shifts.tex
main.tex
appendices/nonlinear_modular_shadows.tex
chapters/examples/y_algebras.tex
appendices/_sl2_yangian_insert.tex
appendices/notation_index.tex
chapters/examples/bar_complex_tables.tex
chapters/examples/beta_gamma.tex
chapters/examples/symmetric_orbifolds.tex
appendices/spectral_higher_genus.tex
chapters/examples/lattice_foundations.tex
exec
/bin/zsh -lc "rg -n -i --glob '*.tex' 'bar.{0,120}(Koszul dual|derived center)|(Koszul dual|derived center).{0,120}bar' chapters appendices preface" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
Total output lines: 234

rg: preface: No such file or directory (os error 2)
chapters/examples/deformation_quantization.tex:813:that the bar-cobar adjunction, restricted to the formal disk at genus~$0$, recovers classical Koszul duality, in agreement with the Francis--Gaitsgory formality
appendices/_sl2_yangian_insert.tex:8:$Y_\hbar(\mathfrak{sl}_2)$ as the open-colour Koszul dual. This is
appendices/_sl2_yangian_insert.tex:602:Koszul dual is the \emph{finite-type} Yangian $Y_\hbar(\mathfrak{sl}_2)$.
appendices/_sl2_yangian_insert.tex:625:$E_1$-chiral Koszul duality functor) extracts the ordered bar
appendices/_sl2_yangian_insert.tex:637:$m_k=0$ for $k\ge 3$, and the open-colour Koszul dual $Y_\hbar(\mathfrak{sl}_2)$
appendices/koszul_reference.tex:462:as chiral coalgebras. Since $\bar{B}(\mathcal{A})$ is the Koszul dual
appendices/dual_methodology.tex:207:produces the Koszul dual bar coalgebra (Verdier duality, Theorem~A).
appendices/signs_and_shifts.tex:252:These are consistent: when $\cA$ is Koszul, $H^*(\bar{B}(\cA))$ concentrates in bar degree~$1$, and the desuspension-then-suspension cancels, recovering the Koszul dual generators in their natural degree.
appendices/signs_and_shifts.tex:837:\item Bar-cobar construction and Koszul duality instead of BV
chapters/examples/w_algebras_deep.tex:579:the bar spectral sequence to collapse at~$E_2$, and the Koszul dual to
chapters/examples/w_algebras_deep.tex:894:The conjecture posits the existence of the bar complex of $\mathcal{W}_{1+\infty}$ as a completed inverse limit, with Koszul dual determined by the 't~Hooft coupling involution $\lambda \mapsto 1 - \lambda$.
chapters/examples/w_algebras_deep.tex:2081:bar--cobar/Koszul duality commutes with Drinfeld--Sokolov reduction
chapters/examples/w_algebras_deep.tex:2086:proving that bar--cobar/Koszul duality commutes with
chapters/connections/thqg_open_closed_realization.tex:1565:$\cA^!$ & Koszul dual (line-operator algebra) & bar + Verdier \\
chapters/examples/landscape_census.tex:1380:bar construction $\bar{B}(bc) = \Lambda^c(V^*)$, Koszul dual
chapters/examples/landscape_census.tex:1759:Table~\ref{tab:bar-dimensions} records the Koszul dual Hilbert
chapters/examples/landscape_census.tex:2080:Among the Koszul chiral algebras in Table~\textup{\ref{tab:bar-dimensions}}, the Koszul dual Hilbert function $\dim (\cA^!)_n$ grows sub-exponentially if and only if $\cA$ is a free field (Heisenberg or free fermion) or affine $\widehat{\mathfrak{sl}}_2$ (which has linear growth $2n{+}1$). All other interacting algebras (higher-rank Kac--Moody, Virasoro, $\mathcal{W}_3$, $bc$, $\beta\gamma$, Yangian) have exponential growth.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar.*derived center" chapters -g"*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/connections/thqg_introduction_supplement_body.tex:69:$\barB_X(\cA)$ itself but on the derived center pair
chapters/theory/introduction.tex:2279: $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
chapters/theory/en_koszul_duality.tex:1306:The passage from bar complex to derived center is
chapters/theory/en_koszul_duality.tex:6673:(where $\barB^{\Sigma}(\cA)$ exists), the \emph{derived center}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1440,1525p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
ordered. Three-dimensional holomorphic-topological theories
have line operators along the topological direction $\R_t$
(Costello--Gaiotto~\cite{CostelloGaiotto2020}); these line operators
form the ordered convolution algebra ${\gAmod}^{\Eone}$ on
$\C_z \times \R_t$, and their fusion is the
$\Eone$-multiplication. Open-string field theory and
factorization on bordered curves carry intrinsic boundary
orderings. Integrable lattice models have $R$-matrices that
satisfy the (ordered) Yang--Baxter equation, not its symmetric
projection. In every physical setting where the bar complex
appears, the line/boundary direction is ordered before any
$\Sigma_n$-symmetrization is taken.

\textsc{Categorical primacy.} The categorical objects of
representation theory are ordered. Quantum groups, Yangians, and
braided tensor categories are the natural framework for chiral
algebras coupled to a spectral parameter; their structure
constants are matrix-valued and obey ordered identities (CYBE,
pentagon, hexagon, mixed Yang--Baxter). Symmetric monoidal
categories are obtained from braided ones by the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1280,1335p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
It has a differential (from OPE collision residues) and a
coassociative deconcatenation coproduct. These are the two
structures of a dg coalgebra. The bar complex does \emph{not}
carry $\mathsf{SC}^{\mathrm{ch,top}}$ structure.

The $\mathsf{SC}^{\mathrm{ch,top}}$ structure emerges on
the \emph{derived chiral center}
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
= C^{\bullet}_{\mathrm{ch}}(\cA, \cA)$,
computed \emph{using} the bar complex as a resolution.
The derived center is the algebra of bulk observables of
the 3d HT theory on $X \times \bR$:
\begin{itemize}
\item It carries $\Etwo$ structure from
  $\FM_k(\bC)$ (the operadic center theorem,
  Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
\item With an inner conformal vector at non-critical level,
  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
  topologization theorem
  (Theorem~\textup{\ref{thm:topologization}}).

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6650,6715p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
These formulas enter the bar complex dimensions via
$\dim B_{\En}(A)_k = P_k^{(n)}(1) \cdot \dim(A^{\otimes k})$
at the level of total Betti numbers.
\end{remark}


%================================================================
% SECTION: E_3 BAR ALGEBRA STRUCTURE
%================================================================

\section{\texorpdfstring{$\Etwo$ structure on the symmetric bar and the $\mathsf{E}_3$ obstruction}{E2 structure on the symmetric bar and the E3 obstruction}}
\label{sec:e3-bar-structure}
\index{bar complex!E2 structure@$\Etwo$ structure|textbf}
\index{E3 obstruction@$\mathsf{E}_3$ obstruction|textbf}

The symmetric chiral bar complex $\barB^{\Sigma}(\cA)$ of a chiral
algebra on a curve carries a natural $\Etwo$ structure from the local
configuration spaces $\Conf_k(\bC)$. It is obtained from the
ordered primitive $\barB^{\mathrm{ord}}(\cA)$ by the lossy
$R$-twisted $\Sigma_n$-coinvariant passage. It does \emph{not}

thinking
**Exploring search options**

I’m considering using ripgrep with --multiline, but a Perl one-liner could be even easier for handling each file. I think Perl can work well, maybe with `perl -0ne`. I need to generate a manageable list, focusing only on chapters and appendices. Using `find` or `rg` to grab `.tex` files from those sections sounds good. I might craft a shell loop to output matched snippets along with line numbers, then refine how to identify file sections.
thinking
**Considering manual search methods**

I’m thinking about using explorer results for pinpointing suspicious candidates, but to be thorough, I might need a manual approach. A simpler option could be to use a temporary script with Perl. I think I can create that by just using `exec_command`. It seems like a good balance between automation and keeping things comprehensive, so let's see how that approach plays out!
codex
The raw hit surface is large, so I’m collapsing it to paragraph-level matches now. After that I’ll read only the suspicious paragraphs in context and patch the ones that actually blur `bar`, `dual coalgebra`, `dual algebra`, or `derived center`.
exec
/bin/zsh -lc "perl -0ne 'while(/(?:"'^|'"\\n\\s*\\n)(.*?)(?=\\n\\s*\\n|\\z)/sg){"'$p=$1; if($p =~ /bar/i && $p =~ /(Koszul dual|derived center)/i){($s=$p)=~s/'"\\s+/ /g; "'$s=substr($s,0,240); print qq{$ARGV:$.:$s'"\\n};}}' "'$(rg --files chapters appendices | rg '"'\\.tex"'$'"')" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '930,995p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
F_p = \operatorname{span}\{L_{-n_1} \cdots L_{-n_r}
|0\rangle : r \leq p,\; n_i \geq 2\}.
\]

\emph{Hypothesis~\ref{item:pbw-flat}.}
Each $F_p/F_{p-1} \cong S^p(V)$ where
$V = \bigoplus_{n \geq 2} \bC \cdot L_{-n}$
(the Virasoro generators modulo vacuum), which is
free of finite rank in each conformal weight.

\emph{Hypothesis~\ref{item:pbw-classical-koszul}.}
$\operatorname{gr}_F \mathrm{Vir}_c
\cong \operatorname{Sym}(V)$
is a polynomial algebra (the OPE reduces to a commutative
product on the associated graded: the non-linear terms
$T_{(0)}T = \partial T$, $T_{(1)}T = 2T$ are lower-order in the
PBW filtration, and the quartic pole $T_{(3)}T = c/2$ is a
scalar that contributes to the curvature, not the
associated graded bracket).
By Priddy's theorem, $\operatorname{Sym}(V)$ is Koszul.
 succeeded in 310ms:
gin{remark}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar dimensions: conventions]\label{rem:betagamma-conventions} \index{betagamma@$\beta\gamma$ system!bar dimension conventions} The $\beta\gamma$ bar complex is infinite-dimensional i
chapters/examples/landscape_census.tex:40:\begin{remark}[Locating the computations]\label{rem:cross-ref-guide} Each row of the Master Table~\textup{\ref{tab:master-invariants}} is computed in the following locations. \begin{enumerate} \item \emph{Free fermion}: bar complex (Theorem
chapters/examples/landscape_census.tex:40:\noindent The computations of Part~\ref{part:physics-bridges} are complete. Part~\ref{part:seven-faces} connects the bar-cobar framework to adjacent programs (Feynman diagrams, BV-BRST, holomorphic-topological field theories, the 4d/2d corr
chapters/examples/yangians_drinfeld_kohno.tex:42:\begin{theorem}[Derived Drinfeld--Kohno on the evaluation-generated subcategory; \ClaimStatusProvedHere]\label{thm:derived-dk-yangian} \index{Drinfeld--Kohno!derived!Yangian} % \textup{[Category: the evaluation-generated subcategory of $\op
chapters/examples/yangians_drinfeld_kohno.tex:42:\begin{theorem}[\texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence; \ClaimStatusProvedHere] \label{thm:h-level-factorization-kd} \index{Koszul duality!factorization!sectorwise|textbf} \in
chapters/examples/yangians_drinfeld_kohno.tex:42:\begin{remark}[The DK ladder as successive approximation to \texorpdfstring{$\infty$}{infinity}-categorical Koszul duality] \label{rem:unified-dk-hierarchy} \index{Drinfeld--Kohno!unified hierarchy} The five DK levels are successive approxi
chapters/examples/yangians_drinfeld_kohno.tex:42:The deeper unity is organizational rather than eliminative: \emph{the RTT presentation supplies the common algebraic source}, while PBW shows that the quadratic extraction is faithful and the root grading makes the factorization descent con
chapters/examples/yangians_drinfeld_kohno.tex:42:\emph{Step~3: Surjectivity on $E_1$.} For the commutative algebra $\operatorname{Sym}(V_{\leq N})$, the Koszul dual is $\bigwedge(V_{\leq N}^*)$, and bar cohomology in degree~$n$ is $\bigwedge^n(V_{\leq N}^*)$. The truncation $\operatorname
chapters/examples/yangians_drinfeld_kohno.tex:42:\emph{Rational DK} \textup{(}Theorem~\textup{\ref{thm:derived-dk-yangian})}. The Yangian $R$-matrix $R(u) = 1 - \hbar P/u$ is rational in the additive spectral parameter $u$. Koszul duality sends $\hbar \to -\hbar$, i.e., $R(u) \to R^{-1}(u
chapters/examples/yangians_drinfeld_kohno.tex:42:\emph{Trigonometric DK} \textup{(}Remark~\textup{\ref{rem:yangian-quantum-group})}. The quantum loop algebra $U_q(\widehat{\mathfrak{g}})$ has trigonometric $R$-matrix $R(u/v)$ in the multiplicative parameter. Koszul duality sends $q \to q^
chapters/examples/yangians_drinfeld_kohno.tex:42:The Yangian chapter reveals the $\Eone$-chiral face of the theory. The chain-level / evaluation-locus derived Drinfeld--Kohno theorem (Theorems~\ref{thm:derived-dk-affine} and~\ref{thm:derived-dk-yangian}) proves that bar-cobar duality \emp
chapters/examples/yangians_drinfeld_kohno.tex:42:Principal Drinfeld--Sokolov reduction defines a functor on primitive triples: \begin{equation}\label{eq:ds-functor-primitive-triple} \mathrm{DS}_{\mathrm{prin}} \colon \bigl(\widehat{\fg}_{k'},\; \Delta_z^{\mathrm{KM}},\; r^{\mathrm{KM}}(z)
chapters/examples/yangians_drinfeld_kohno.tex:42:The preceding subsection computed the collision residue $r_\cA(z) = \tau|_{\deg 2}$ for the standard families. The following state the categorical content of this identification: the collision residue is the binary inverse of the bar functo
chapters/examples/yangians_drinfeld_kohno.tex:42:\begin{theorem}[Collision residue as binary Koszul inverse; \ClaimStatusProvedHere] \label{thm:rmatrix-koszul-inverse} \index{r-matrix@$r$-matrix!binary Koszul inverse|textbf} \index{Koszul duality!binary inverse via collision residue} \ind
chapters/examples/yangians_drinfeld_kohno.tex:42:\item \emph{RTT self-encoding.} For a Yangian $Y(\fg)$, the RTT relation $R_{12}(u{-}v)\, T_1(u)\, T_2(v) = T_2(v)\, T_1(u)\, R_{12}(u{-}v)$ is the binary component of the bar codifferential: the quadratic relations defining $Y(\fg)$ are ex
chapters/examples/yangians_drinfeld_kohno.tex:42:Part~(iii): for the Yangian $Y(\fg)$ with RTT presentation, the quadratic relations $\{R_{12}T_1T_2 - T_2T_1R_{12} = 0\}$ are the bar relations at degree~$2$. The orthogonal complement under the Koszul duality pairing gives the relations of
chapters/examples/yangians_drinfeld_kohno.tex:42:\begin{remark}[The binary inverse as leading term] \label{rem:rmatrix-koszul-inverse-leading} \index{Koszul duality!binary inverse as leading term} Theorem~\ref{thm:rmatrix-koszul-inverse} is a genus-zero, degree-$2$ statement. The full inv
chapters/examples/yangians_drinfeld_kohno.tex:42:\begin{theorem}[The $r$-matrix as Koszul-dual inverse; \ClaimStatusProvedHere] \label{thm:r-matrix-koszul-dual-inverse} \index{r-matrix@$r$-matrix!Koszul-dual inverse|textbf} \index{twisting morphism!Koszul-dual inverse} \index{Koszul duali
chapters/examples/yangians_drinfeld_kohno.tex:42:\begin{proof} Part~(i) is Theorem~\ref{thm:thqg-V-collision-twisting}: the genus-zero binary collision residue of~$\Theta_\cA$ is the universal twisting morphism $\pi_\cA \in \Tw(\barBch(\cA), \cA)$, and $\tau_r$ is its projection to the Ko
chapters/examples/yangians_drinfeld_kohno.tex:42:Part~(iii): the first composition factors through the bar-cobar counit $\varepsilon \colon \Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$ (Theorem~\ref{thm:higher-genus-inversion} on the Koszul locus), which is a quasi-isomorphism by Theore

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "derived center.*bar" -g"*.tex" chapters' in /Users/raeez/chiral-bar-cobarthinking
**Narrowing down suspicious paragraphs**

I need to focus on targeted suspicious results. The explorer might help with that. At the same time, I can identify possible conflations from the search results, specifically looking at the five-object conflation from the D09 findings. I should search for paragraphs that mention both "bar" and either "Koszul dual" or "derived center." It seems like we might only need to fix actual conflating language in a handful of cases, but I want to be thorough. I’ll wait for the explorer to assist.
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:1273:\index{Swiss-cheese operad!on derived center, NOT on bar}
chapters/theory/en_koszul_duality.tex:6734: the derived center, not the symmetric bar.
chapters/theory/chiral_modules.tex:4619:derived center, equivalently on the bar resolution of the diagonal
chapters/connections/concordance.tex:7269: derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
chapters/theory/introduction.tex:1470:derived center, not on the bar complex. The closed sector of any
collab wait(call_MtSClESJTWCXj2WJ2dRGeG5I)
  receivers: 019d8809-f986-7b60-add9-5da9ecb4205d
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4595,4625p' chapters/theory/chiral_modules.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \[
 E_1^{p,q}
 \;=\;
 H^q_{\mathrm{DS}}\!\bigl(C^p_{\mathrm{ch}}(A,A)\bigr).
 \]
 If one proves the degreewise comparison map
 \[
 H^0_{\mathrm{DS}}\!\bigl(C^p_{\mathrm{ch}}(A,A)\bigr)
 \longrightarrow
 C^p_{\mathrm{ch}}(W,W)
 \]
 is a quasi-isomorphism and that
 $H^q_{\mathrm{DS}}(C^p_{\mathrm{ch}}(A,A)) = 0$ for
 $q > 0$, then the spectral sequence collapses at~$E_1$ and yields
 \[
 H^0_{\mathrm{DS}}\!\bigl(C^\bullet_{\mathrm{ch}}(A,A)\bigr)
 \;\simeq\;
 C^\bullet_{\mathrm{ch}}(W,W),
 \]
 hence~\eqref{eq:ds-derived-center-commute} as an isomorphism of
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar complex.*derived center" -g"*.tex" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:1306:The passage from bar complex to derived center is
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '770,830p' chapters/examples/deformation_quantization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{center}
\begin{tabular}{|l|l|}
\hline
\textbf{Beilinson--Drinfeld} & \textbf{Bar-Cobar Approach} \\
\hline
Abstract $\mathcal{D}$-modules & Concrete configuration spaces \\
Factorization axioms & Geometric integrals \\
Local-to-global principles & Explicit bar-cobar formulas \\
Existence proofs & Constructive algorithms \\
\hline
\end{tabular}
\end{center}

The factorization algebra framework of Costello--Gwilliam provides a rigorous formulation in which the Kontsevich star product arises as the local-to-global assembly map.

\subsection{Relation to quadratic duality paper}

The paper on quadratic duality for chiral algebras \cite{GLZ22} focuses on Koszul duality for quadratic operads. The deformation quantization framework of this monograph generalizes from quadratic to arbitrary (non-quadratic via curvature), geometrizes the duality via bar-cobar configuration spaces, and provides explicit formulas for dualizing.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '40,95p' chapters/connections/thqg_introduction_supplement_body.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compactification $\overline{C}_n(\Sigma)$ fibers over the ordered
configuration space $\operatorname{Conf}_n(\mathbb{R})$, and the bar
differential decomposes as
\begin{equation}\label{eq:thqg-intro-swiss-cheese-decomposition}
d_{\barB,\Sigma}
\;=\;
d_C + d_R,
\end{equation}
where $d_C$ acts in the $X$-direction (extracting OPE residues along
holomorphic collision divisors) and $d_R$ acts in the $\mathbb{R}$-direction
(extracting residues along the topological ordering). The identity
$d_{\barB,\Sigma}^2 = 0$ decomposes as
\begin{equation}\label{eq:thqg-intro-swiss-cheese-squares}
d_C^2 = 0, \qquad d_R^2 = 0, \qquad \{d_C, d_R\} = 0.
\end{equation}
The first equation is the bar nilpotence of~$\cA$ on~$X$. The second
is the coassociativity of the bar coproduct. The third is the
compatibility of the OPE with the ordered product.

\begin{definition}[$\Eone$-chiral coassociative structure on the bar complex]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6880,6950p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item The \emph{brace dg algebra structure} on chiral Hochschild cochains
 $\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA)$
 (Theorem~\ref{thm:thqg-brace-dg-algebra}). \textbf{Proved}:
 the same tree-combinatorial argument as Gerstenhaber--Voronov,
 with block-substitution replacing simple reindexing.
\item The \emph{chiral derived center}
 $\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 := H^*(\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA), \delta)$
 (Definition~\ref{def:thqg-chiral-derived-center}).
 On the Koszul locus this is a three-term chiral Gerstenhaber algebra
 $\mathcal{Z}^0 \oplus \mathcal{Z}^1 \oplus \mathcal{Z}^2$
 by Theorem~H.
\item The \emph{universal open/closed pair}
 $\mathcal{U}(\cA)
 = (\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA),\, \cA,\, \mathrm{id})$
 (Theorem~\ref{thm:thqg-swiss-cheese}). \textbf{Proved}: the chiral
 Swiss-cheese theorem, asserting that the derived center is the
 universal bulk with open color~$\cA$.
\item The \emph{local-global bridge}
 (Theorem~\ref{thm:thqg-local-global-bridge}): restriction of the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/deformation_quantization.tex | sed -n '700,740p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   700	
   701	\subsection{AdS/CFT and holography}
   702	
   703	The bar-cobar duality admits a conjectural holographic interpretation:
   704	
   705	\begin{conjecture}[Holographic duality; \ClaimStatusConjectured]\label{conj:deformation-holographic}
   706	\[\text{Bulk theory on } AdS_3 \longleftrightarrow \text{Boundary chiral algebra on } S^1\]
   707	
   708	The boundary genus expansion should model the bulk theory:
   709	\[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
   710	where $F_g$ are free energies computed via configuration space integrals.
   711	(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
   712	\end{conjecture}
   713	
   714	\begin{remark}[Scope and the bar/center distinction]
   715	The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.
   716	
   717	\emph{Clarification on bar vs.\ center.}
   718	The genus expansion $F_g$ is a projection of the universal MC
   719	element $\Theta_\cA \in \MC(\gAmod)$, which lives in the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/introduction.tex | sed -n '1440,1505p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1440	ordered. Three-dimensional holomorphic-topological theories
  1441	have line operators along the topological direction $\R_t$
  1442	(Costello--Gaiotto~\cite{CostelloGaiotto2020}); these line operators
  1443	form the ordered convolution algebra ${\gAmod}^{\Eone}$ on
  1444	$\C_z \times \R_t$, and their fusion is the
  1445	$\Eone$-multiplication. Open-string field theory and
  1446	factorization on bordered curves carry intrinsic boundary
  1447	orderings. Integrable lattice models have $R$-matrices that
  1448	satisfy the (ordered) Yang--Baxter equation, not its symmetric
  1449	projection. In every physical setting where the bar complex
  1450	appears, the line/boundary direction is ordered before any
  1451	$\Sigma_n$-symmetrization is taken.
  1452	
  1453	\textsc{Categorical primacy.} The categorical objects of
  1454	representation theory are ordered. Quantum groups, Yangians, and
  1455	braided tensor categories are the natural framework for chiral
  1456	algebras coupled to a spectral parameter; their structure
  1457	constants are matrix-valued and obey ordered identities (CYBE,
  1458	pentagon, hexagon, mixed Yang--Baxter). Symmetric monoidal
  1459	categories are obtained from braided ones by the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1265,1325p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1265	mixed squares comparing a closed collision with an open split.
  1266	Later arguments use this boundary-stratum description; the full
  1267	minimal presentation is not written out here.
  1268	\end{remark}
  1269	
  1270	\begin{principle}[The bar complex is $\Eone$-chiral coassociative;
  1271	$\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
  1272	\label{princ:sc-two-incarnations}
  1273	\index{Swiss-cheese operad!on derived center, NOT on bar}
  1274	\index{bar complex!is E1 coassociative, NOT SC}
  1275	The ordered bar complex
  1276	$\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$
  1277	is an $\Eone$-chiral coassociative coalgebra: a coalgebra
  1278	over the Koszul dual cooperad
  1279	$(\operatorname{Ass}^{\mathrm{ch}})^{\scriptstyle !}$.
  1280	It has a differential (from OPE collision residues) and a
  1281	coassociative deconcatenation coproduct. These are the two
  1282	structures of a dg coalgebra. The bar complex does \emph{not}
  1283	carry $\mathsf{SC}^{\mathrm{ch,top}}$ structure.
  1284	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '940,1010p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   940	\emph{Hypothesis~\ref{item:pbw-classical-koszul}.}
   941	$\operatorname{gr}_F \mathrm{Vir}_c
   942	\cong \operatorname{Sym}(V)$
   943	is a polynomial algebra (the OPE reduces to a commutative
   944	product on the associated graded: the non-linear terms
   945	$T_{(0)}T = \partial T$, $T_{(1)}T = 2T$ are lower-order in the
   946	PBW filtration, and the quartic pole $T_{(3)}T = c/2$ is a
   947	scalar that contributes to the curvature, not the
   948	associated graded bracket).
   949	By Priddy's theorem, $\operatorname{Sym}(V)$ is Koszul.
   950	
   951	\emph{Hypothesis~\ref{item:pbw-bounded}.}
   952	Same argument as the Kac--Moody case: the number of
   953	partitions of weight~$h$ into at most $n$ parts (each $\geq 2$)
   954	is finite.
   955	
   956	By Theorem~\ref{thm:pbw-koszulness-criterion},
   957	$\mathrm{Vir}_c$ is chiral Koszul.
   958	\end{proof}
   959	
codex
- `chapters/examples/deformation_quantization.tex:714-729` — “The bar complex \barB(A) classifies twisting morphisms (boundary deformation data); the derived center Z_{\mathrm{der}}(A) \simeq C^\bullet_{\mathrm{ch}}(A,A) is the bulk observable algebra … the genus expansion … should be compared with bulk amplitudes via the center, not directly via the bar complex.” Verdict: clean — the paragraph explicitly keeps B(A)’s deformation role separate from Z^{der}_{ch}(A) and warns against conflating the two.

- `chapters/theory/introduction.tex:1464-1474` — “The Swiss-cheese operad … governs the open/closed derived center pair …; the bar complex itself is a single-coloured E₁-coassociative coalgebra … the SC structure emerges on the derived center, not on the bar complex.” Verdict: clean — it asserts Z^{der}_{ch}(A) carries the closed sector while the ordered bar remains the E₁ engine, so none of the five objects are merged.

- `chapters/theory/en_koszul_duality.tex:1270-1313` — “The bar complex … is an E₁ coassociative coalgebra … The SC^{ch,top} structure emerges on the derived chiral center … computed using the bar complex as a resolution … the passage from bar complex to derived center is where the SC structure is produced.” Verdict: clean — the text consistently treats B(A) as an E₁ computational engine and Z^{der}_{ch}(A) as the superior output, avoiding any conflation of those objects.

- `chapters/theory/chiral_koszul_pairs.tex:960-984` — “Bar cohomology computes Koszul dual … dim Hⁿ(B(𝐀)) = dim (𝐀^!)ₙ … the Koszul dual … is the linear dual of the bar coalgebra, not the affine algebra at the dual level.” Verdict: clean — it uses the bar coalgebra to compute A^! but clearly distinguishes the dual algebra from the bar/B(A) and derived-center objects.
wait(call_MtSClESJTWCXj2WJ2dRGeG5I) 1 agents complete:
  019d8809-f986-7b60-add9-5da9ecb4205d completed: "- `chapters/examples/deformation_quantization.tex:714-729` — “The bar complex \barB(A) classifies twisting morphisms (bo…"

thinking
**Searching for findings**

It seems the explorer only found a few results, which might not be exhaustive due to limited search terms. I’m thinking we might need to run more searches ourselves. Perhaps I could use the explorer again to flag suspicious items from a broader search surface. I'll consider asking about specific candidate files that are suspicious. It might be easier to inspect the main files from the search results where there's likely some conflation. I should also search for actual D09 findings or existing notes.
codex
The first pass shows many in-scope paragraphs are already clean. I’m now querying the specific surfaces most likely to be wrong: places that explicitly say the bar “is” the Koszul dual, that the bar-cobar route “produces” bulk, or that identify the bar directly with the dual algebra.
exec
/bin/zsh -lc "rg -n -i --glob '*.tex' 'bar["'^.]{0,120}(derived center|bulk)|derived center[''^.]{0,120}bar|bar[''^.]{0,120}Koszul dual|Koszul dual[''^.]{0,120}bar'"' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'D09|five-object conflation|bar-cobar produces bulk|the Koszul dual equals the bar complex|Omega\\(B\\(A\\)\\) is the Koszul dual|D09 findings' -S ." in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/deformation_quantization.tex:813:that the bar-cobar adjunction, restricted to the formal disk at genus~$0$, recovers classical Koszul duality, in agreement with the Francis--Gaitsgory formality
appendices/_sl2_yangian_insert.tex:8:$Y_\hbar(\mathfrak{sl}_2)$ as the open-colour Koszul dual. This is
appendices/_sl2_yangian_insert.tex:602:Koszul dual is the \emph{finite-type} Yangian $Y_\hbar(\mathfrak{sl}_2)$.
appendices/_sl2_yangian_insert.tex:625:$E_1$-chiral Koszul duality functor) extracts the ordered bar
appendices/_sl2_yangian_insert.tex:637:$m_k=0$ for $k\ge 3$, and the open-colour Koszul dual $Y_\hbar(\mathfrak{sl}_2)$
chapters/examples/w_algebras_deep.tex:579:the bar spectral sequence to collapse at~$E_2$, and the Koszul dual to
chapters/examples/w_algebras_deep.tex:894:The conjecture posits the existence of the bar complex of $\mathcal{W}_{1+\infty}$ as a completed inverse limit, with Koszul dual determined by the 't~Hooft coupling involution $\lambda \mapsto 1 - \lambda$.
chapters/examples/w_algebras_deep.tex:2081:bar--cobar/Koszul duality commutes with Drinfeld--Sokolov reduction
chapters/examples/w_algebras_deep.tex:2086:proving that bar--cobar/Koszul duality commutes with
appendices/dual_methodology.tex:207:produces the Koszul dual bar coalgebra (Verdier duality, Theorem~A).
chapters/examples/lattice_foundations.tex:17:The bar complex acquires a cocycle twist; the Koszul dual
chapters/examples/lattice_foundations.tex:1437:\textbf{Operation} & \textbf{Vertex algebra} & \textbf{Bar complex} & \textbf{Koszul dual} \\
chapters/examples/lattice_foundations.tex:1984:\caption{Lattice Koszul dual pairs and genus-1 bar complex data.}
chapters/examples/lattice_foundations.tex:3588:\noindent{\footnotesize $^*$For simply-laced $\fg$: $Y(\fg)^! \cong Y(\fg^!)$ and $\fg \cong \fg^!$, so the Koszul dual is isomorphic to the original as an abstract algebra but with $\hbar \to -\hbar$; this is ``almost'' self-dual (Remark~\ref{rem:yangian-langlands}). PH = proved here; CJ = conjectured.}
appendices/signs_and_shifts.tex:252:These are consistent: when $\cA$ is Koszul, $H^*(\bar{B}(\cA))$ concentrates in bar degree~$1$, and the desuspension-then-suspension cancels, recovering the Koszul dual generators in their natural degree.
appendices/signs_and_shifts.tex:837:\item Bar-cobar construction and Koszul duality instead of BV
appendices/koszul_reference.tex:462:as chiral coalgebras. Since $\bar{B}(\mathcal{A})$ is the Koszul dual
chapters/examples/beta_gamma.tex:514:The symmetric coalgebra structure arises because $\mathcal{F}$ is a Clifford-type (exterior/anticommutative) algebra. By Koszul duality, $\Lambda^! = \mathrm{Sym}$, so the bar complex of an exterior algebra is a symmetric coalgebra. This is the chiral analog of $\bar{B}(\Lambda(V)) \cong \mathrm{Sym}^c(V^*)$.
chapters/examples/beta_gamma.tex:537:\subsubsection{\texorpdfstring{Koszul dual algebra: $\mathcal{F}^! = \bar{B}(\mathcal{F})^\vee \cong \beta\gamma$}{Koszul dual algebra: F! = B(F)v = beta-gamma}}
chapters/examples/beta_gamma.tex:586:\subsubsection{\texorpdfstring{Koszul dual: $(\beta\gamma)^! = \bar{B}(\beta\gamma)^\vee \cong \mathcal{F}$}{Koszul dual: (bg)! = F}}
 succeeded in 52ms:
Total output lines: 88

./healing_20260413_132214/H03_thm_C_alt_proof.md:600:forbidden drift: no claim that bar-cobar produces bulk; no claim that the shifted-symplectic perspective replaces the primary proof; no upgrade from perspective to unconditional proof
./CLAUDE.md:165:- "bar-cobar produces bulk" (wrong: bar-cobar inverts to A; bulk is Hochschild)
./CLAUDE.md:166:- "Omega(B(A)) is the Koszul dual" (wrong: that is INVERSION)
./CLAUDE.md:167:- "the Koszul dual equals the bar complex" (wrong: bar is coalgebra, dual is algebra)
./CLAUDE.md:613:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
./CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
./scripts/adversarial_wave2.py:303:    ("D09_five_objects_discipline", "Search for paragraphs that mention both 'bar' and 'Koszul dual' or 'derived center'. For each: are all five objects (A, B(A), A^i, A^!, Z^der) correctly distinguished? Any conflation?"),
./rectification_20260412_233715/R18_cobar_construction.md:183:CLAUDE.md:539:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
./rectification_20260412_233715/R18_cobar_construction.md:463:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
./scripts/fix_campaign_100.py:468:agent("C", "C15_five_objects_fix", """Fix five-object conflation (D09 findings).
./scripts/fix_campaign_100.py:521:agent("D", "D09_markdown_in_latex", """Fix markdown in LaTeX across ALL volumes (AP121/B40).
./platonic_rectification_20260413_114523/P01_thm_A_verdier_upgrade.md:825:wave2_audit_20260413_001942/D09_five_objects_discipline.md:31:- [HIGH] chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:409 — PROBLEM: the line Koszul dual is built from `\overline B^{\mathrm{ord}}(\mathcal A_{\mathrm{bulk}})`, contradicting the corrected triangle in the same volume, where line operators come from the open-color Koszul dual of the boundary, not from the bar of the bulk. FIX: replace `\overline B^{\mathrm{ord}}(\mathcal A_{\mathrm{bulk}})` by `\overline B^{\mathrm{ord}}(\mathcal A_{\partial})` and define `\mathcal A^!_{\mathrm{line}} := H^\bullet(\overline B^{\mathrm{ord}}(\mathcal A_{\partial}))^\vee`; keep the bulk action separate via the Swiss-cheese action map.
./platonic_rectification_20260413_114523/P01_thm_A_verdier_upgrade.md:826:wave2_audit_20260413_001942/D09_five_objects_discipline.md:471:/bin/zsh -lc "sed -n '1700,1710p;404,412p;2688,2700p;30,36p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./platonic_rectification_20260413_114523/P01_thm_A_verdier_upgrade.md:827:wave2_audit_20260413_001942/D09_five_objects_discipline.md:651:/bin/zsh -lc "sed -n '400,414p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobarexec
./platonic_rectification_20260413_114523/P01_thm_A_verdier_upgrade.md:828:wave2_audit_20260413_001942/D09_five_objects_discipline.md:788:/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex | sed -n '407,410p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex | sed -n '2694,2699p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex | sed -n '32,35p'" in /Users/raeez/chiral-bar-cobarexec
./platonic_rectification_20260413_114523/P01_thm_A_verdier_upgrade.md:829:wave2_audit_20260413_001942/D09_five_objects_discipline.md:1117:I see that there's definitely a conflict in line-operators 409. I should inspect `ht_bulk_boundary_line_core` for conflicts with earlier definitions—it's likely okay to report. I'll check if the same file mentions that bulk is derived from the center, not computed by the bar, which it probably does. I also need to look at `celestial_holography` for potential conflicts. Additionally, the `spectral-braiding-frontier` shows an anti-pattern related to Verdier duality on bar cohomology. Lastly, there's a mistake in `examples-worked` theorem 779 that we can report.
./platonic_rectification_20260413_114523/P01_thm_A_verdier_upgrade.md:830:wave2_audit_20260413_001942/D09_five_objects_discipline.md:1359:- [HIGH] chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:409 — PROBLEM: the line Koszul dual is built from `\overline B^{\mathrm{ord}}(\mathcal A_{\mathrm{bulk}})`, contradicting the corrected triangle in the same volume, where line operators come from the open-color Koszul dual of the boundary, not from the bar of the bulk. FIX: replace `\overline B^{\mathrm{ord}}(\mathcal A_{\mathrm{bulk}})` by `\overline B^{\mathrm{ord}}(\mathcal A_{\partial})` and define `\mathcal A^!_{\mathrm{line}} := H^\bullet(\overline B^{\mathrm{ord}}(\mathcal A_{\partial}))^\vee`; keep the bulk action separate via the Swiss-cheese action map.
./resume_20260413_163457/S14_standalone_to_main.md:1052:/bin/zsh -lc "rg -n -C 2 'B\\(A\\) is a coalgebra over SC|bar differential is the closed color|bar coproduct is the open color|SC\\"'^'"\\{ch,top\\} is Koszul self-dual|E_3-chiral|Topologization proved for all|A\\"'^! is an SC-algebra|bar-cobar produces bulk|Omega'"\\(B\\(A\\)\\) is the Koszul dual|the Koszul dual equals the bar complex|D_Ran\\(B\\(A\\)\\) is the cobar complex|the bar complex carrying both structures' standalone/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Inspecting audit findings**

I need to check the existing D09 audit for specific findings in Volume I. I can use the local audit file `wave2_audit_20260413_001942/D09_five_objects_discipline.md`, since it’s in the repository and I can access the findings directly. This might save me some time. I’ll search the D09 file with the command line tool `rg` in the specified directory to read the relevant lines. It’ll be important to verify the information locally!
codex
I found the old D09 audit log in the workspace. I’m using it only as a lead list, then re-checking each cited paragraph in live `.tex` before editing.
exec
/bin/zsh -lc "rg -n '/Users/raeez/chiral-bar-cobar/' wave2_audit_20260413_001942/D09_five_objects_discipline.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
245:/bin/zsh -lc "perl -0ne 'while(/(.*?)(\\n\\s*\\n|\\z)/sg){"'$p=$1; $start=1+(()=substr($_,0,$-[0])=~/'"\\n/g); if("'$p =~ /bar/i && $p =~ /Koszul dual/i){ $one=$p; $one =~ s/'"\\n/ /g; "'$one =~ s/'"\\s+/ /g; print \"KOSZUL\\t"'$ARGV'"\\t"'$start'"\\t"'$one'"\\n\"; } if("'$p =~ /bar/i && $p =~ /derived center/i){ $one=$p; $one =~ s/'"\\n/ /g; "'$one =~ s/'"\\s+/ /g; print \"CENTER\\t"'$ARGV'"\\t"'$start'"\\t"'$one'"\\n\"; }}' "'$(rg --files /Users/raeez/chiral-bar-cobar/chapters -g '"'*.tex')" in /Users/raeez/chiral-bar-cobarexec
291:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	2063	Under the bar construction, this monodromy becomes a $\langle\alpha,\gamma\rangle$-twist in the differential on $\overline{C}_{n+1}(X)$. The Verdier involution (which underlies Koszul duality) reverses the monodromy: $z^{\langle\alpha,\gamma\rangle} \mapsto z^{-\langle\alpha,\gamma\rangle}$, mapping $\gamma$ to $-\gamma$ in the discriminant group. Since $\gamma \mapsto -\gamma$ is an involution of the finite abelian group $D(\Lambda)$, it permutes the twisted sectors without changing their number. \end{proof}
292:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	2442	The $\Eone$ bar complex computation in complete constructive detail for three explicit deformations producing strictly $\Eone$-chiral algebras. Each example is computed end-to-end: cocycle values, OPE phases, bar differential, ordering cycles, bar cohomology, Koszul dual identification, and braiding torsion. All numerical values are verified by the computational suite (\texttt{compute/lib/e1\_lattice\_bar.py}, 45 tests passing).
293:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	2981	\begin{remark}[Pattern across examples] \label{rem:lattice:e1-pattern} The three computations exhibit a universal structure: \begin{enumerate}[label=(\roman*)] \item In each adjacent-pair sector $\gamma = \alpha_i + \alpha_j$, the $\Eone$ bar complex $0 \to \C^2 \xrightarrow{d} \C \to 0$ has $\dim\ker(d) = 1$, producing exactly one ordering cycle. \item The ordering cycle coefficient is always $\zeta_N^{-1}$, regardless of the specific value of $q$ on that edge \textup{(}only the normalization and overall phase depend on~$q$\textup{)}. \item The number of ordering cycles equals the number of edges in the Dynkin diagram: $1$ for $A_2$, $3$ for $D_4$. These are \emph{not} the number of positive roots (which is $3$ for $A_2$, $12$ for $D_4$), but rather the number of adjacent simple root pairs. At higher bar degrees, the remaining positive roots contribute to the bar cohomology through longer chains of collisions. \item The $\Einf$ bar complex has $H^2 = 0$ in every sector considered above: all ordering cycles are strictly $\Eone$ classes that vanish under symmetrization. \item Koszul duality inverts the deformation parameter: $q \to -q$, with the dual braiding being the transpose of the original. \end{enumerate} \end{remark}
294:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	3215	\begin{proof} The abstract statement follows from the $\Eone$-chiral Koszul duality (Theorem~\ref{thm:e1-chiral-koszul-duality}) and the self-duality of $\chirAss$: the bar construction on an $\Eone$-chiral algebra $\cA$ produces a coalgebra over ${\chirAss}^! \cong \chirAss \otimes \mathrm{sgn}$, which is again an associative coalgebra but with the sign-twisted structure. This sign twist is realized in each instance as: \begin{itemize} \item For lattice algebras: the bar differential carries the cocycle value $\varepsilon(\alpha,\beta)$, and the sign twist inverts it to $\varepsilon(\alpha,\beta)^{-1}$. \item For Yangians: the bar differential encodes the RTT relation via the $R$-matrix, and the sign twist inverts $R(u) \to R^{-1}(u)$, equivalently $\hbar \to -\hbar$ for the Yang $R$-matrix. \item For quantum lattice algebras: the deformation datum $\zeta^{q(\alpha,\beta)}$ is inverted to $\zeta^{-q(\alpha,\beta)}$. \end{itemize} In each case, the geometric mechanism is that the Verdier involution on ordered configurations $\overline{C}^{\mathrm{ord}}_n(X)$ reverses the ordering, which transposes the defining relation and hence inverts the non-commutativity data. \end{proof}
295:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	3253	The parallel extends to the classical limit: the Feigin--Frenkel shift has a classical limit $k \to \infty$ in which the duality becomes trivial; the $\Eone$ inversion has a classical limit $\hbar \to 0$ (for Yangians) or $N \to \infty$ (for quantum lattice algebras) in which the datum becomes the identity and the duality becomes the $\Einf$ Koszul duality of $\mathrm{Sym} \leftrightarrow \bigwedge$ (Corollary~\ref{cor:yangian-classical-self-dual}). \end{remark}
296:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	3524	\begin{table}[ht] \centering \caption{$\Eone$-chiral algebras and their Koszul duals.} \label{tab:lattice:e1-catalog} \index{E1-chiral algebra@$\Eone$-chiral algebra!master table} \renewcommand{\arraystretch}{1.4} {\small \begin{tabular}{l l l c l} \textbf{$\Eone$ algebra} & \textbf{Datum $\delta$} & \textbf{Koszul dual} & \textbf{Self-dual?} & \textbf{Status} \\ \hline \multicolumn{5}{l}{\textit{Lattice cocycle deformations \textup{(}this section\textup{)}}} \\ \hline $\Vlat_{A_2}^{N,q}$ ($N \geq 3$) & $\zeta_N^{q(\alpha_i,\alpha_j)}$ & $\Vlat_{A_2}^{N,-q}$ & No & PH \\ $\Vlat_{D_4}^{N,q}$ & $\zeta_N^{q(\alpha_i,\alpha_j)}$ & $\Vlat_{D_4}^{N,-q}$ & No & PH \\ $\Vlat_{E_8}^{N,q}$ & $\zeta_N^{q(\alpha_i,\alpha_j)}$ & $\Vlat_{E_8}^{N,-q}$ & No & PH \\ $\Vlat_\Lambda^{N,q}$ (general) & $\zeta_N^{q(\alpha,\beta)}$ & $\Vlat_\Lambda^{N,-q}$ & No & PH \\ \hline \multicolumn{5}{l}{\textit{RTT/Yangian constructions \textup{(}Chapter~\ref{chap:yangians}\textup{)}}} \\ \hline $Y(\fg)^{\mathrm{ch}}$ & $R(u)$ & $Y_{R^{-1}}(\fg)^{\mathrm{ch}}$ & No$^*$ & PH \\ $Y(\fg)^{\mathrm{ch}}|_{\hbar=0}$ & $R = 1$ & $\mathrm{Sym}^! = \bigwedge$ & No & PH \\ \hline \multicolumn{5}{l}{\textit{Elliptic/toroidal \textup{(}Chapter~\ref{chap:toroidal-elliptic}\textup{)}}} \\ \hline $U_{q,t}(\hat{\hat{\fg}})^{\mathrm{ch}}$ & $R^{\mathrm{ell}}(u,\tau)$ & $U_{q^{-1},t^{-1}}(\hat{\hat{\fg}})^{\mathrm{ch}}$ & No & CJ \\ \end{tabular} } \smallskip
297:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	3580	\noindent{\footnotesize $^*$For simply-laced $\fg$: $Y(\fg)^! \cong Y(\fg^!)$ and $\fg \cong \fg^!$, so the Koszul dual is isomorphic to the original as an abstract algebra but with $\hbar \to -\hbar$; this is ``almost'' self-dual (Remark~\ref{rem:yangian-langlands}). PH = proved here; CJ = conjectured.} \end{table}
298:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	3711	\begin{theorem}[Lattice factorization Koszul pair; \ClaimStatusProvedHere] \label{thm:lattice:factorization-koszul} \index{Koszul pair!lattice factorization|textbf} Let $\Lambda$ be an even positive-definite lattice with cocycle $\varepsilon$ \textup{(}symmetric or not\textup{)}. The lattice vertex algebra $\Vlat_\Lambda^\varepsilon$ and its Koszul dual $(\Vlat_\Lambda^{\varepsilon^{-1}})^c$ \textup{(}Theorem~\textup{\ref{thm:lattice:koszul-dual})} form a chiral Koszul pair \textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})} in the factorization sense: \begin{enumerate}[label=(\roman*)] \item \textup{(}Factorization bar-cobar equivalence\textup{).} The bar construction $\barB^{\mathrm{ch}}(\Vlat_\Lambda^\varepsilon)$ is a conilpotent factorization coalgebra on $\Ran(X)$, and the cobar-bar counit is a quasi-isomorphism of factorization algebras: \begin{equation}\label{eq:lattice:fact-bar-cobar} \Omega^{\mathrm{ch}}(\barB^{\mathrm{ch}}(\Vlat_\Lambda^\varepsilon)) \xrightarrow{\;\sim\;} \Vlat_\Lambda^\varepsilon. \end{equation} \item \textup{(}Verdier intertwining on $\Ran(X)$\textup{).} Verdier duality sends the bar coalgebra to the homotopy Koszul dual algebra: \begin{equation}\label{eq:lattice:verdier-ran} \mathbb{D}_{\Ran}\, \barB^{\mathrm{ch}}(\Vlat_\Lambda^\varepsilon) \simeq (\Vlat_\Lambda^{\varepsilon^{-1}})^!_\infty \qquad \bigl(\text{underlying complex } \simeq \barB^{\mathrm{ch}}(\Vlat_\Lambda^{\varepsilon^{-1}})\bigr). \end{equation} \item \textup{(}Functoriality over $\overline{\mathcal{M}}_{g,n}$\textup{).} Both equivalences hold in families over moduli: for $\pi\colon \mathcal{X} \to \overline{\mathcal{M}}_{g,n}$ the universal curve, the relative bar construction $\barB^{\mathrm{ch}}_{\mathcal{X}/\overline{\mathcal{M}}_{g,n}} (\Vlat_\Lambda^\varepsilon)$ is a factorization coalgebra on $\Ran(\mathcal{X}/\overline{\mathcal{M}}_{g,n})$, and the counit and Verdier equivalences hold fiberwise by proper base change. \end{enumerate} \end{theorem}
299:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	3852	\begin{remark}[Why thick generation is unnecessary] \label{rem:lattice:no-thick-generation} \index{thick generation!unnecessary for lattice} The proof of Theorem~\ref{thm:lattice:factorization-koszul} does not use any thick-generation argument. Compare with the Yangian DK ladder (Chapter~\ref{chap:yangians}): \begin{itemize} \item DK-2 (Proposition~\ref{prop:yangian-dk2-thick-generation}) requires showing that evaluation modules thickly generate the finite-dimensional representation category. For lattice algebras, the lattice sectors replace thick generation: the direct sum decomposition~\eqref{eq:lattice:fact-decomposition} is \emph{exact}, not a thick-closure approximation. \item DK-3 (Proposition~\ref{prop:yangian-dk3-generated-core}) requires lifting the Kazhdan--Lusztig equivalence to factorization categories. For lattice algebras, both sides of the Koszul duality live in the same lattice-VOA family (cocycle $\varepsilon$ vs.\ $\varepsilon^{-1}$), so no external bridge is needed. \end{itemize} The lattice setting thus provides the first \emph{unconditional} (Tier~T1) factorization bar-cobar equivalence in the monograph. \end{remark}
300:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	4423	\begin{theorem}[Quantum lattice factorization DK; \ClaimStatusProvedHere] \label{thm:lattice:quantum-factorization-dk} \index{Drinfeld--Kohno!quantum lattice|textbf} \index{quantum lattice algebra!factorization DK} For $\fg$ simply-laced, $N \geq 3$, and $q \colon \Lambda_\fg \times \Lambda_\fg \to \Z/N\Z$ a non-zero antisymmetric bilinear form, the quantum lattice algebra $\Vlat_{\Lambda_\fg}^{N,q}$ \textup{(}Definition~\textup{\ref{def:quantum-lattice})} satisfies: \begin{enumerate}[label=(\roman*)] \item \emph{$\Eone$-factorization bar-cobar}: \[ \Omega^{\Eone,\mathrm{ch}}( \barB^{\Eone,\mathrm{ch}}(\Vlat_{\Lambda_\fg}^{N,q})) \xrightarrow{\;\sim\;} \Vlat_{\Lambda_\fg}^{N,q} \] as an equivalence of $\Eone$-factorization algebras on $\Ran(X)$. \item \emph{Homotopy-level equivalence}: the $\Eone$-factorization $\infty$-category equivalence \begin{equation}\label{eq:lattice:quantum-fact-dk} \Factord(X; \Vlat_{\Lambda_\fg}^{N,q}) \;\simeq\; \Factord(X; \Vlat_{\Lambda_\fg}^{N,-q})^{\mathrm{rev}}. \end{equation} \item \emph{$\Eone$ inversion}: the equivalence realizes the $\Eone$ inversion principle \textup{(}Theorem~\textup{\ref{thm:e1-inversion-principle})} at the factorization-categorical level: the Koszul dual $(\Vlat_{\Lambda_\fg}^{N,q})^! \cong (\Vlat_{\Lambda_\fg}^{N,-q})^c$ \textup{(}Proposition~\textup{\ref{prop:lattice:deformation-properties}(iv))} governs the Verdier dual factorization category. \end{enumerate} \end{theorem}
301:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	4475	(iii) The Verdier identification $\mathbb{D}_{\Ran}\, \barB^{\Eone}(\Vlat^{N,q}) \simeq (\Vlat^{N,-q})^!_\infty$ (Corollary~\ref{cor:lattice:factorization-dk-level1}(iii)) identifies the Verdier dual bar complex with the bar complex of the Koszul dual. At the $\infty$-categorical level, this says that the Verdier dual of $\Factord(X; \Vlat^{N,q})$ is governed by the Koszul dual $(\Vlat^{N,q})^! = (\Vlat^{N,-q})^c$, which is the factorization-categorical realization of the $\Eone$ inversion principle. \end{proof}
302:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	424	\begin{proof} By the Koszul duality $(\beta\gamma)^! \cong \mathcal{F}$ (Theorem~\ref{thm:betagamma-fermion-koszul}) and the bar-cobar adjunction (Theorem~\ref{thm:bar-cobar-isomorphism-main}), the bar complex $\bar{B}(\beta\gamma)$ is quasi-isomorphic to the Chevalley coalgebra of the free fermion system. Since the $\beta\gamma$--fermion pair is Koszul (the underlying operadic duality is $\chirCom$--$\chirLie$, which is Koszul by Theorem~\ref{thm:chiral-koszul-duality}), acyclicity follows from the general inversion theorem (Theorem~\ref{thm:higher-genus-inversion}).
303:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	514	The symmetric coalgebra structure arises because $\mathcal{F}$ is a Clifford-type (exterior/anticommutative) algebra. By Koszul duality, $\Lambda^! = \mathrm{Sym}$, so the bar complex of an exterior algebra is a symmetric coalgebra. This is the chiral analog of $\bar{B}(\Lambda(V)) \cong \mathrm{Sym}^c(V^*)$. \end{proposition}
304:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	537	\subsubsection{\texorpdfstring{Koszul dual algebra: $\mathcal{F}^! = \bar{B}(\mathcal{F})^\vee \cong \beta\gamma$}{Koszul dual algebra: F! = B(F)v = beta-gamma}}
305:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	539	\begin{theorem}[Koszul dual of the free fermion; \ClaimStatusProvedHere] \label{thm:cobar-betagamma} The Koszul dual algebra of the free fermion is the $\beta\gamma$ system: \[\mathcal{F}^! = \bar{B}(\mathcal{F})^\vee \cong \text{Chiral algebra}(\beta, \gamma \mid [\beta,\gamma] = 1).\] (Bar-cobar inversion gives $\Omega(\bar{B}(\mathcal{F})) \cong \mathcal{F}$, recovering the fermion itself.) \end{theorem}
306:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	586	\subsubsection{\texorpdfstring{Koszul dual: $(\beta\gamma)^! = \bar{B}(\beta\gamma)^\vee \cong \mathcal{F}$}{Koszul dual: (bg)! = F}}
307:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	588	\begin{theorem}[Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma}; \ClaimStatusProvedHere] \label{thm:cobar-fermions} The Koszul dual algebra of the $\beta\gamma$ system is the free fermion ($bc$ ghost system): \[(\beta\gamma)^! = \bar{B}(\beta\gamma)^\vee \cong \text{Chiral algebra}(b, c \mid b^2 = 0,\; c^2 = 0,\; b(z)c(w) \sim \tfrac{1}{z-w}).\] (Bar-cobar inversion gives $\Omega(\bar{B}(\beta\gamma)) \cong \beta\gamma$, recovering $\beta\gamma$ itself.) \end{theorem}
308:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	663	This is \emph{different} from Koszul duality: bosonization equates correlation functions, while Koszul duality is an algebraic relationship between chiral algebras via bar-cobar (Remark~\ref{rem:bosonization-not-koszul}). \end{theorem}
309:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	1153	\emph{Step~2: Curvature from the bar differential.} The genus-$1$ bar differential on $\bar{B}^2(\beta\gamma)$ has the form $d^{(1)} = d^{(0)} + \delta^{(1)}$, where $d^{(0)}$ is the genus-$0$ differential (residues of the rational propagator $1/u$) and $\delta^{(1)}$ encodes the genus-$1$ correction. The curvature $m_0^{(1)}$ measures the failure of $d^{(1)}$ to square to zero on the cobar side; equivalently, it is the obstruction to extending the genus-$0$ bar complex to genus~$1$. This obstruction is the genus-$1$ component $\theta_1$ of the universal MC class (Theorem~\ref{thm:explicit-theta}): for $\beta\gamma$, $\theta_1 = \kappa(\beta\gamma) \cdot \mu \otimes \lambda_1$, with $\kappa(\beta\gamma) = 6\lambda^2 - 6\lambda + 1$. The Koszul duality $\beta\gamma \leftrightarrow bc$ reverses the sign of $\Theta$: $\kappa(\beta\gamma) + \kappa(bc) = 0$.

thinking
**Inspecting audit findings**

I notice the D09 audit file has candidate lines, but I don't see any findings yet. I’m thinking I’ll need to scroll through it later to find high severity findings. It might be helpful to search for “[HIGH]” or check the severity levels in the D09 file and Volume I paths to be more specific. I should inspect those later lines to gather all necessary information.
exec
/bin/zsh -lc "rg -n '\\[(CRITICAL|HIGH|MEDIUM|LOW)\\].*/Users/raeez/chiral-bar-cobar/' wave2_audit_20260413_001942/D09_five_objects_discipline.md" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'PROBLEM:.*chiral-bar-cobar|FIX:.*chiral-bar-cobar|KOSZUL\\t/Users/raeez/chiral-bar-cobar.*(is the|coincide|bulk|derived center)' wave2_audit_20260413_001942/D09_five_objects_discipline.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
272:KOSZUL	/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex	4502	\begin{example}[The ADHM Coulomb branch: from geometry to shadow class] \label{ex:adhm-coulomb} \index{ADHM quiver!Coulomb branch} The ADHM quiver with gauge group $G = \mathrm{GL}_n$ and $N$ fundamental hypermultiplets produces a Coulomb branch whose VOA is the $\mathcal{W}$-algebra $\mathcal{W}_n$ at a level determined by $N$. This provides the sharpest illustration of the non-Lagrangian passage: the Coulomb branch is defined as an algebraic variety $\mathcal{M}_C = \Spec(\C[\mathcal{M}_H]^G)$ (the categorical quotient of the Higgs branch), but the associated VOA is the DS reduction $\mathcal{W}_n = H^0_{\mathrm{DS}}(V_k(\mathfrak{gl}_n))$. The bar complex of $\mathcal{W}_n$ inherits the shadow data: class~$\mathbf{M}$ for $n \ge 2$ (the Virasoro quartic pole is unavoidable once the DS reduction creates a stress tensor). The passage from the geometric data (moduli space, quiver, hyperk\"ahler metric) to the algebraic data (shadow class, Koszul dual, $r$-matrix) is mediated entirely by the VOA functor. \end{example}
274:KOSZUL	/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex	58	The Heisenberg algebra~$\cH_k$ has shadow depth $r_{\max} = 2$ (class~G), so $\Theta^{\mathrm{oc}}$ terminates at degree~2. Every projection is computed in closed form: curvature $\kappa = k$, spectral $R$-matrix $R(z) = e^{k\hbar/z}$, genus tower $F_g = k\,\lambda_g^{\mathrm{FP}}$. The line category is $\cC_{\mathrm{line}} \simeq \cH_{-k}\text{-mod}$ (via $Y(\mathfrak{u}(1)) \simeq \cH_{-k}$); the derived center is the free boson bulk; the complementarity involution $k \mapsto -k$ closes the triangle (note: the Koszul dual $\cH_k^! = \Sym^{\mathrm{ch}}(V^*)$ is not $\cH_{-k}$).
278:KOSZUL	/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex	895	\begin{remark}[$bc$--$\beta\gamma$ Koszul duality and the statistics exchange] \label{rem:rosetta-bc-betagamma-koszul} \index{Koszul duality!bc-betagamma@$bc$--$\beta\gamma$}% \index{complementarity!free fields}% The Heisenberg complementarity $K(\cH_k) = 0$ is the first instance of a universal pattern for all free-field chiral algebras. The $bc$ ghost system of conformal weights $(\lambda, 1-\lambda)$ and the $\beta\gamma$ system of the same weights are Koszul dual to each other: \[ bc_\lambda^! \;=\; \beta\gamma_\lambda, \qquad \beta\gamma_\lambda^! \;=\; bc_\lambda. \] The mechanism is the chiral incarnation of classical $\mathrm{Ext}/\mathrm{Sym}$ duality: $bc_\lambda$ is the chiral exterior algebra $\bigwedge^{\mathrm{ch}}(V)$ on $V = \bC b \oplus \bC c$ (fermionic), and its Koszul dual is the chiral symmetric algebra $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ (bosonic), which is precisely the $\beta\gamma$ system. The bar complex has $m_2$ only (simple-pole OPE), confirming that both systems are Koszul. Koszul duality exchanges statistics while preserving conformal weights; it does \emph{not} exchange spins $\lambda \mapsto 1 - \lambda$ (that is a relabelling, not a dualisation).
279:KOSZUL	/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex	1013	The Heisenberg bar complex is a single coalgebra that unifies Koszul duality with holomorphic--topological factorization (Theorem~\ref{thm:steinberg-presentation}). The Rosetta Stone is the dictionary that makes this analogy precise. \end{remark}
284:KOSZUL	/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex	2031	\noindent\textbf{Koszul dual: explicit generators and relations.} \label{par:cs-koszul-dual-explicit}% \index{Chern--Simons!Koszul dual!explicit generators|textbf}% \index{Yangian!dg-shifted!Chern--Simons}% The Koszul dual $A^! = Y_\hbar^{\mathrm{dg}}(\fg)$ is the dg-shifted Yangian constructed from the bar complex of $V_k(\fg)$ (Volume~I, Theorem~\ref*{thm:Koszul_dual_Yangian}; \cite{DNP25}). We give the explicit presentation in modes and generating functions, first for general~$\fg$ and then for $\fg = \mathfrak{sl}_2$.
286:KOSZUL	/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex	2482	\smallskip \noindent \emph{Cobar compatibility and Koszul dual.} Applying $\Omega^{\mathrm{ch}}$ to both sides of \eqref{eq:wakimoto-bar-map}, the cobar functor commutes with the embedding: \[ \Omega^{\mathrm{ch}}(\barBch(\iota_W)) \;\colon\; V_k(\mathfrak{sl}_2) \;\xrightarrow{\;\sim\;} \Omega^{\mathrm{ch}}\bigl( \barBch(V_k(\mathfrak{sl}_2))\bigr) \;\longrightarrow\; \cH_k \otimes \beta\gamma\,. \] At the level of Koszul duals, the map induces \begin{equation}\label{eq:wakimoto-koszul} Y_\hbar(\mathfrak{sl}_2) \;=\; V_k(\mathfrak{sl}_2)^! \;\longrightarrow\; (\cH_k)^! \otimes (bc) \;=\; \mathrm{Sym}^{\mathrm{ch}}(V^*) \otimes bc\,, \end{equation} embedding the Yangian into a tensor product of the Heisenberg Koszul dual and the $bc$ system. This is the Koszul-dual shadow of the Wakimoto embedding: the Yangian inherits a free-field presentation from the free-field realisation of the original affine algebra.
301:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex	4475	(iii) The Verdier identification $\mathbb{D}_{\Ran}\, \barB^{\Eone}(\Vlat^{N,q}) \simeq (\Vlat^{N,-q})^!_\infty$ (Corollary~\ref{cor:lattice:factorization-dk-level1}(iii)) identifies the Verdier dual bar complex with the bar complex of the Koszul dual. At the $\infty$-categorical level, this says that the Verdier dual of $\Factord(X; \Vlat^{N,q})$ is governed by the Koszul dual $(\Vlat^{N,q})^! = (\Vlat^{N,-q})^c$, which is the factorization-categorical realization of the $\Eone$ inversion principle. \end{proof}
303:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	514	The symmetric coalgebra structure arises because $\mathcal{F}$ is a Clifford-type (exterior/anticommutative) algebra. By Koszul duality, $\Lambda^! = \mathrm{Sym}$, so the bar complex of an exterior algebra is a symmetric coalgebra. This is the chiral analog of $\bar{B}(\Lambda(V)) \cong \mathrm{Sym}^c(V^*)$. \end{proposition}
305:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	539	\begin{theorem}[Koszul dual of the free fermion; \ClaimStatusProvedHere] \label{thm:cobar-betagamma} The Koszul dual algebra of the free fermion is the $\beta\gamma$ system: \[\mathcal{F}^! = \bar{B}(\mathcal{F})^\vee \cong \text{Chiral algebra}(\beta, \gamma \mid [\beta,\gamma] = 1).\] (Bar-cobar inversion gives $\Omega(\bar{B}(\mathcal{F})) \cong \mathcal{F}$, recovering the fermion itself.) \end{theorem}
307:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	588	\begin{theorem}[Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma}; \ClaimStatusProvedHere] \label{thm:cobar-fermions} The Koszul dual algebra of the $\beta\gamma$ system is the free fermion ($bc$ ghost system): \[(\beta\gamma)^! = \bar{B}(\beta\gamma)^\vee \cong \text{Chiral algebra}(b, c \mid b^2 = 0,\; c^2 = 0,\; b(z)c(w) \sim \tfrac{1}{z-w}).\] (Bar-cobar inversion gives $\Omega(\bar{B}(\beta\gamma)) \cong \beta\gamma$, recovering $\beta\gamma$ itself.) \end{theorem}
309:KOSZUL	/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex	1153	\emph{Step~2: Curvature from the bar differential.} The genus-$1$ bar differential on $\bar{B}^2(\beta\gamma)$ has the form $d^{(1)} = d^{(0)} + \delta^{(1)}$, where $d^{(0)}$ is the genus-$0$ differential (residues of the rational propagator $1/u$) and $\delta^{(1)}$ encodes the genus-$1$ correction. The curvature $m_0^{(1)}$ measures the failure of $d^{(1)}$ to square to zero on the cobar side; equivalently, it is the obstruction to extending the genus-$0$ bar complex to genus~$1$. This obstruction is the genus-$1$ component $\theta_1$ of the universal MC class (Theorem~\ref{thm:explicit-theta}): for $\beta\gamma$, $\theta_1 = \kappa(\beta\gamma) \cdot \mu \otimes \lambda_1$, with $\kappa(\beta\gamma) = 6\lambda^2 - 6\lambda + 1$. The Koszul duality $\beta\gamma \leftrightarrow bc$ reverses the sign of $\Theta$: $\kappa(\beta\gamma) + \kappa(bc) = 0$.

thinking
**Analyzing log classifications**

I’m looking at the D09 log, and it doesn’t seem to classify entries as problems, just lists them. I think I need more information, maybe there are bullet findings toward the end that could help. My plan is to search for specific lines around number 1300, and I might use sed to format certain later sections. It feels like there might be useful details hiding in there!
exec
/bin/zsh -lc "sed -n '1320,1410p' wave2_audit_20260413_001942/D09_five_objects_discipline.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
thinking
**Counting final bullets**

I need to figure out if I should include vol3 5562 separately since it’s the same as 5753 but earlier. To keep the count at 18, I think I might skip 5562 and 4476. I also want to include vol1 free_fields or beta_gamma. 

Now, counting the final bullets, I have 20 items total, which seems fine!
thinking
**Drafting summary findings**

I'm considering how to summarize findings regarding the theorem. I should ensure bullet points reflect exact fixes, particularly for line 299. Maybe using absolute paths or repo names as prefixes will help. I need to check the relevant paragraphs and state a verdict. Also, I have to be cautious about the overall length—I want about 20 bullet points, each around two lines. User’s formatting includes em dashes, so I’ll include them, but I’ll skip the markdown section except for the summary heading.
codex
- [CRITICAL] chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:4548 — PROBLEM: `\Omega\B(\cA^{\mathrm{cl}}_{\mathrm{M2}})` is identified with the bulk `L_\infty` algebra, collapsing bar-cobar inversion into bulk. FIX: rewrite the sentence and equation as `\Omega\B(\cA^{\mathrm{cl}}_{\mathrm{M2}}) \simeq \cA^{\mathrm{cl}}_{\mathrm{M2}}`; if the intended object is the defect/Koszul-dual algebra, rename it to `\cA^{!,\mathrm{cl}}_{\mathrm{M2}} := H^\bullet(B(\cA^{\mathrm{cl}}_{\mathrm{M2}}))^\vee \simeq C^\bullet(\fg_{\mathrm{dbl}})`.

- [CRITICAL] chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:4632 — PROBLEM: the conjecture defines “Koszul duality” by `\cA_{\mathrm{bulk}} = \Omega\B(\cA_{\mathrm{M2}})`, again identifying bulk with inversion back to `A`. FIX: replace `\cA_{\mathrm{bulk}} = \Omega\B(\cA_{\mathrm{M2}})` with either `\cA^!_{\mathrm{M2}} = H^\bullet(B(\cA_{\mathrm{M2}}))^\vee` if the defect algebra is meant, or `\beta_{\mathrm{der}}\colon \cA_{\mathrm{bulk}} \to Z^{\mathrm{der}}_{\mathrm{ch}}(\cA_{\mathrm{M2}})` if the bulk is meant.

- [CRITICAL] calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5634 — PROBLEM: the same false equation reappears in Vol III: the bar construction is said to “yield the bulk `L_\infty` algebra.” FIX: make the proposition about the classical defect/Koszul-dual algebra, not the bulk, and replace `\cA^{\mathrm{cl}}_{\mathrm{bulk}}` by `\cA^{!,\mathrm{cl}}_{\mathrm{M2}} := H^\bullet(B(\cA^{\mathrm{cl}}_{\mathrm{M2}}))^\vee`.

- [CRITICAL] calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5718 — PROBLEM: Vol III repeats the inversion/bulk conflation with `\cA_{\mathrm{bulk}}=\Omega\B(\cA_{\mathrm{M2}})`. FIX: replace that display by a derived-center comparison for bulk, and keep Koszul duality on the defect side as `\cA^!_{\mathrm{M2}} = H^\bullet(B(\cA_{\mathrm{M2}}))^\vee`.

- [CRITICAL] chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:299 — PROBLEM: the M2 paragraph says the boundary algebra is Koszul dual to the bulk algebra and that this is “bar-cobar duality as holographic duality,” conflating `A^!` with `Z^{\mathrm{der}}`. FIX: replace lines 298-300 by a three-object sentence: boundary algebra `\cA_\partial`, defect/Koszul-dual algebra `\cA^!_\partial`, and bulk algebra `Z^{\mathrm{der}}_{\mathrm{ch}}(\cA_\partial)` are distinct; holography uses the derived center, not bar-cobar inversion.

thinking
**Inspecting critical findings**

I need to ensure I'm thorough within my assigned scope. I could refer to the D09 bullet list from earlier as a starting point with items like thqg_modular_bootstrap.tex and free_fields.tex. I'm examining whether the toroidal_elliptic.tex is present since search results suggest otherwise. I need to fix the five-object conflation issue and possibly check other Volume I problems that weren’t summarized. I can rerun targeted searches for specific phrases from the D09 list across chapters.
codex
I have a concrete lead list from the prior audit. I’m re-reading those exact live paragraphs now to see which findings still exist and to avoid “fixing” text that has already been repaired.
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '4908,4922p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '1878,1886p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4908	$H^0$ is the space of coinvariants $=$ conformal blocks
  4909	(Zhu \cite{Zhu96}).
  4910	\end{proof}
  4911	
  4912	\begin{conjecture}[String amplitude correspondence,
  4913	\texorpdfstring{$g \geq 1$}{g 1}; \ClaimStatusConjectured]
  4914	\label{conj:string-amplitude-higher-genus}
  4915	The chiral homology class of
  4916	Theorem~\ref{thm:genus-g-chiral-homology}, integrated
  4917	over $\overline{\mathcal{M}}_{g,n}$, computes the
  4918	$g$-loop string amplitude:
  4919	\[
  4920	\mathcal{A}_{g,n}^{\mathrm{string}}
  4921	= \int_{\overline{\mathcal{M}}_{g,n}}
  4922	\langle \barB^{(g)}_n
exec
/bin/zsh -lc "nl -ba chapters/connections/ym_boundary_theory.tex | sed -n '60,76p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1878	\index{holomorphic-topological!beta-gamma atom@$\beta\gamma$ atom}
  1879	Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
  1880	into the global geometry of curves, so factorization homology alone
  1881	controls the genus expansion. The $\beta\gamma$ system is therefore the
  1882	simplest object in which bar-cobar duality and holographic duality coincide.
  1883	\end{remark}
  1884	
  1885	\section{From 3d \texorpdfstring{$\mathcal{N}=2$}{N=2} to the full chiral algebra}
  1886	
 succeeded in 51ms:
nl: chapters/connections/ym_boundary_theory.tex: No such file or directory
exec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '4544,4560p;4628,4638p;4668,4678p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_modular_bootstrap.tex | sed -n '1248,1256p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
nl: chapters/connections/thqg_modular_bootstrap.tex: No such file or directory
 succeeded in 52ms:
nl: chapters/examples/toroidal_elliptic.tex: No such file or directory
codex
Some old D09 leads now point to paths that no longer exist in the live tree. I’m resolving current file locations first and only patching live paragraphs.
exec
/bin/zsh -lc "rg --files chapters | rg 'ym_boundary_theory|thqg_modular_bootstrap|toroidal_elliptic'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'bar-cobar duality and holographic duality coincide|bulk field content; the Koszul dual|Verdier duality on bar cohomology|obtained by Verdier duality on bar cohomology|the Koszul dual .* supplies the bulk|holographic duality is.*Koszul duality|bulk .* derived center|bar-cobar duality admits a conjectural holographic interpretation' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 succeeded in 51ms:
chapters/examples/deformation_quantization.tex:703:The bar-cobar duality admits a conjectural holographic interpretation:
chapters/examples/beta_gamma.tex:1882:simplest object in which bar-cobar duality and holographic duality coincide.
chapters/examples/yangians_drinfeld_kohno.tex:6623: from the bulk algebra to the derived center of the boundary
chapters/connections/concordance.tex:4653:The bulk algebra of the 3d theory is the derived center
chapters/connections/concordance.tex:7024: The bulk observables are the chiral derived center
chapters/connections/concordance.tex:9841: bulk reconstruction from the derived center \\
chapters/connections/genus_complete.tex:777:cohomology of the chiral category). The bulk is the derived center
chapters/connections/thqg_introduction_supplement.tex:52:The \emph{bulk algebra} is the derived center of~$\cA$. Define the
chapters/theory/chiral_center_theorem.tex:46:Every bulk action factors uniquely through the derived center.
chapters/connections/semistrict_modular_higher_spin_w3.tex:715:Let $\Bdy(W_3)$ be the completed boundary model of Definition~\ref{def:completed-boundary-model-chapter}. Then the physical Dirichlet boundary chiral algebra of the semistrict $W_3$ bulk is quasi-isomorphic to a chiral enhancement of $\Bdy(W_3)$, and its derived center recovers the classical $W_3$ Poisson vertex algebra.

thinking
**Searching for suspicious phrases**

I think I might have some issues that need attention. I’ll search the current live tree for any suspicious phrases, possibly using D09 patterns. I want to look through all paragraphs for combinations like 'bar' with 'derived center' or 'Koszul dual.' I should also include phrases that seem suspicious, such as "coincide," "obtained via Verdier duality on bar cohomology," and "bar = bulk." I’ll search across chapters to catch any false patterns.
exec
/bin/zsh -lc "rg -n -i 'bar-cobar.*bulk|bulk.*bar-cobar|bar.*bulk|bulk.*bar' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'A\\"'^!.*D_'"\\\\Ran\\(B|D_\\\\Ran.*A\\"'^!|Verdier duality on bar cohomology|bar cohomology.*is the Koszul dual|H'"\\"'^'"\\*\\(\\\\barB.*\\).*is the Koszul dual|the bar construction .* computes .* derived center|derived center .* bar complex|bar complex .* derived center|coincide.*holographic duality|holographic duality.*Koszul duality' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_introduction_supplement.tex:117:Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
chapters/theory/introduction.tex:2671:$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
chapters/theory/en_koszul_duality.tex:1306:The passage from bar complex to derived center is
 succeeded in 52ms:
chapters/examples/deformation_quantization.tex:709:\[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
chapters/examples/deformation_quantization.tex:715:The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.
chapters/frame/preface_sections10_13_draft.tex:59:condition~$b$; $\barB$ forgets the bulk; $\Theta_\cA$ is the
chapters/frame/preface_sections10_13_draft.tex:170:\item \emph{Bar $\neq$ bulk.}
chapters/connections/editorial_constitution.tex:2042:relating boundary and bulk. The bar--semi-infinite identification
chapters/examples/free_fields.tex:4950:supplies the bulk field content, and the bar-cobar filtration degree
chapters/connections/genus_complete.tex:703:Bar-cobar duality supplies an algebraic template for AdS/CFT: $\cA \leftrightarrow \barB(\cA)$, OPE coefficients $\leftrightarrow$ vertices, conformal blocks $\leftrightarrow$ Witten diagrams, $c \leftrightarrow R_{\mathrm{AdS}}$, $1/N \leftrightarrow$ genus. The conjectural comparison $Z_{\mathrm{CFT}}[\mathcal{J}] = Z_{\mathrm{gravity}}[\phi_0 = \mathcal{J}]$ identifies the genus expansion with the $1/N$ expansion ($g \mapsto N^{-(2g-2)}$). Requires bulk CS reconstruction~\cite{Wit89} and Witten diagram matching beyond this monograph; contributing to Conjecture~\ref{conj:master-bv-brst} (MC5;
chapters/connections/genus_complete.tex:831:refinement of the large-$N$ boundary/bulk duality, with $\hbar$
chapters/connections/holographic_datum_master.tex:73: all-degree boundary-bulk coupling produced by the bar-intrinsic
chapters/frame/preface.tex:80:bar's two factors, is conjectured to be the universal boundary-bulk
chapters/frame/preface.tex:484:$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
chapters/frame/preface.tex:489:proves bar-cobar inversion; Volume~II would upgrade it to bulk
chapters/frame/preface.tex:4070:condition~$b$; $\barB$ forgets the bulk; $\Theta_\cA$ is the
chapters/frame/preface.tex:4191:\item \emph{Bar $\neq$ bulk.}
chapters/connections/thqg_introduction_supplement_body.tex:20:bar complex into a bulk direction and a boundary direction; the
chapters/connections/thqg_introduction_supplement_body.tex:137:\item \emph{Boundary $\to$ Bulk} (the bar map).
chapters/examples/kac_moody.tex:2068:The mathematical content is Theorem~\ref{thm:universal-kac-moody-koszul} ($\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$); the conjectural step is the downstream MC5 dictionary comparing bar-cobar data with holographic boundary/bulk physics.
chapters/theory/poincare_duality_quantum.tex:88:For $K$ M2 branes at an $A_{N-1}$ singularity \cite{Costello-1705.02500v1}: the boundary algebra is $\mathcal{A}_{\mathrm{M2}} = \mathrm{Yangian}(\mathfrak{gl}_N)$ (twisted ABJM at $K \to \infty$), and the bulk algebra is $\mathcal{A}_{\mathrm{bulk}} = U_{\hbar,c}(\mathrm{Diff}(\mathbb{C}) \otimes \mathfrak{gl}_N)$. These are conjecturally related by curved Koszul duality with deformation parameter $c$.
chapters/theory/poincare_duality_quantum.tex:1221: suitable bulk data (via the bar-cobar adjunction as a
chapters/theory/poincare_duality_quantum.tex:1233: (the bar complex provides the coalgebraic input, but the bulk


thinking
**Evaluating mathematical context**

I see that Beta_gamma line 1882 discusses bar-cobar and holographic duality but doesn’t mention Koszul dual or derived center, which is part of what the user is asking for. D09 has found the latter concepts, but it’s unclear if that qualifies under the user’s specific request for paragraphs that include both 'bar' and 'Koszul dual' or 'derived center'. I’ll need to check broader context and possibly automate paragraph-level matches for a more thorough inspection.
thinking
**Searching for candidate paragraphs**

I'm planning to search for candidate paragraphs that mention both bar and Koszul dual or derived center, especially focusing on any risky phrasing. I'll likely use a tool like rg to locate lines that contain "derived center" alongside "bar." This way, I can quickly filter through relevant content to find the best matches that meet the user’s request while keeping an eye on potential issues in phrasing. Let's see what I can find!
codex
I’m reading the few remaining risky paragraphs now. Most of the live `bar`/`derived center` mentions are already clean, so the patch set should stay small if the wording still fails the five-object test.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement_body.tex | sed -n '14,24p;132,142p;166,180p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement.tex | sed -n '46,60p;112,122p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '4944,4956p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4944	
  4945	\begin{conjecture}[Bulk-boundary correspondence; \ClaimStatusConjectured]
  4946	\label{conj:bulk-boundary-correspondence}
  4947	For a boundary chiral algebra $\cA$, the bar-cobar adjunction
  4948	$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
  4949	between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
  4950	supplies the bulk field content, and the bar-cobar filtration degree
  4951	maps to the radial coordinate.
  4952	(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
  4953	\end{conjecture}
  4954	
  4955	
  4956	\subsection{Complete classification of extensions}
 succeeded in 51ms:
    46	
    47	\subsection{Vertex 2: the bulk algebra (derived center)}
    48	\label{subsec:vertex-bulk}
    49	\index{bulk algebra|textbf}
    50	\index{derived center|textbf}
    51	
    52	The \emph{bulk algebra} is the derived center of~$\cA$. Define the
    53	center local system on the universal curve
    54	$\pi \colon \mathcal{C}_g \to \overline{\mathcal{M}}_g$ by
    55	\begin{equation}\label{eq:supp-center-local-system-def}
    56	\mathcal{Z}(\cA) \;:=\;
    57	R\mathcal{H}om_{\cA\text{-bimod}}(\cA,\, \cA),
    58	\end{equation}
    59	where the bimodule structure uses left and right chiral actions.
    60	On a fixed smooth curve~$\Sigma_g$ of genus~$g$, the fiber of the
   112	The \emph{line-operator category} is the derived module category
   113	of the Koszul dual algebra:
   114	\begin{equation}\label{eq:supp-line-category-def}
   115	\mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
   116	\end{equation}
 succeeded in 51ms:
    14	
    15	The holographic triangle of \S\ref{sec:holographic-triangle} was
    16	presented as a diagram of three vertices and three edges. The following
    17	constructs it from the bar complex alone, by progressively extracting
    18	structure from the identity $D_\cA^2 = 0$. The extraction proceeds
    19	in four stages: the Swiss-cheese factorization that separates the
    20	bar complex into a bulk direction and a boundary direction; the
    21	bulk-boundary-line triangle that identifies each vertex categorically;
    22	the holographic datum that packages the triangle into a single
    23	Maurer--Cartan element; and the reconstruction theorems that recover
    24	the triangle from the datum.
   132	\index{holographic triangle!edges}
   133	
   134	The three edges connecting the vertices are:
   135	
   136	\begin{enumerate}[label=\textup{(\roman*)}]
   137	\item \emph{Boundary $\to$ Bulk} (the bar map).
   138	 The bar construction $\barB_X \colon \cA \mapsto \barB_X(\cA)$
   139	 maps the boundary algebra to the bar coalgebra. The trace
   140	 map~\eqref{eq:thqg-intro-bar-to-ambient} projects the bar
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '6618,6628p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6618	\item the \emph{line-boundary functor}
  6619	 $F_b \colon \mathcal{C}_T \to V_b\text{-}\mathrm{mod}$
  6620	 comparing the algebraic line-operator model to boundary modules;
  6621	\item the \emph{bulk-boundary map}
  6622	 $\beta_{\mathrm{der}} \colon V \to Z(V_b)_{\mathrm{der}}$
  6623	 from the bulk algebra to the derived center of the boundary
  6624	 algebra; and
  6625	\item the \emph{boundary $R$-matrix}
  6626	 $R_b(z) \in \operatorname{End}(V_b \otimes V_b)(z^{-1})$
  6627	 encoding the OPE/fusion on $V_b$-mod.
  6628	\end{enumerate}
exec
/bin/zsh -lc "nl -ba chapters/theory/poincare_duality_quantum.tex | sed -n '80,92p;1218,1264p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1752,1760p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1752	\langle d_{\bar{B}}(\omega), K \rangle = \langle \omega, d_\Omega(K) \rangle
  1753	\]
  1754	by the adjointness of residue and distribution (integration by parts on~$\overline{C}_n(X)$).
  1755	
  1756	\emph{Row 3: $\overline{C}_n \leftrightarrow C_n$.}
  1757	The bar complex lives on the compactification~$\overline{C}_n(X)$ (logarithmic forms extend to the boundary), while its Verdier dual lives on the open configuration space~$C_n(X)$ (distributions are supported away from diagonals). Verdier duality exchanges sheaves on~$\overline{C}_n$ with cosheaves on~$C_n$: the boundary strata of~$\overline{C}_n$ (where points collide) encode the bar differential, while the bulk of~$C_n$ (where points are separated) carries the dual algebra structure of~$\cA^!_\infty$.
  1758	
  1759	\emph{Row 4: $m_2 \leftrightarrow \Delta_2$.}
  1760	The binary product $m_2(a \otimes b) = \mathrm{Res}_{z_1=z_2}[a(z_1) b(z_2) \cdot \eta_{12}]$ is dual to the binary coproduct $\Delta_2(c) = c(z_1) \cdot \delta(z_1 - z_2)$ via:
 succeeded in 52ms:
    80	locus is the content of Theorem~A
    81	(Convention~\ref{conv:bar-coalgebra-identity}), not a tautology \emph{Caution}: the cobar construction $\Omega(\bar{B}(\mathcal{A}))$
    82	recovers $\mathcal{A}$ itself \textup{(}bar-cobar inversion, Theorem~B\textup{)}, \emph{not} $\mathcal{A}^!$. The Koszul dual is obtained via Verdier duality, not cobar.
    83	\end{theorem}
    84	
    85	\subsection{The M2 brane example: quantum Yangian as Koszul dual}
    86	
    87	\begin{example}[M2 branes at \texorpdfstring{$A_{N-1}$}{A_N-1} singularity]\label{ex:M2-brane}
    88	For $K$ M2 branes at an $A_{N-1}$ singularity \cite{Costello-1705.02500v1}: the boundary algebra is $\mathcal{A}_{\mathrm{M2}} = \mathrm{Yangian}(\mathfrak{gl}_N)$ (twisted ABJM at $K \to \infty$), and the bulk algebra is $\mathcal{A}_{\mathrm{bulk}} = U_{\hbar,c}(\mathrm{Diff}(\mathbb{C}) \otimes \mathfrak{gl}_N)$. These are conjecturally related by curved Koszul duality with deformation parameter $c$.
    89	\end{example}
    90	
    91	\begin{theorem}[Curved Koszul duality (algebraic form) {\cite{Positselski11, GLZ22}}; \ClaimStatusProvedElsewhere]\label{thm:curved-koszul}
    92	Let $\mathcal{A}$ be a complete filtered chiral algebra satisfying the finite-type
  1218	\item Residues at collision divisors should model bulk interactions
  1219	 (via the brace operations on Hochschild cochains)
  1220	\item The cobar construction should recover the boundary package from
  1221	 suitable bulk data (via the bar-cobar adjunction as a
  1222	 representability theorem for deformations)
  1223	\item The bar-cobar adjunction is conjecturally interpreted as the
  1224	 algebraic shadow of holographic duality: bar classifies couplings,



thinking
**Examining candidates for Koszul duality**

I need to inspect other candidates from my current search list related to the bar and Koszul dual/derived center. For some of the lines I found in the supplementary material, there's a potential conflation regarding the explanation of "Verdier/linear duality." I could clarify this by emphasizing that the construction involves linear duality followed by the separate Verdier image. It seems that while another line regarding A^! is acceptable as is, another section may need some cleaning up regarding terminology about dual algebra structures.
thinking
**Clarifying potential ambiguities**

I think this could be okay, but there’s some ambiguity here. The user's task involves a five-object conflation, and there's a risk that "bulk" might be misinterpreted as bulk algebra. The discussion references both bar and dual algebra structures rather than the derived center, which might cause further confusion. It's essential to ensure that terminology is clear to avoid any misinterpretations. I should consider how to clarify that in my response!
thinking
**Refining search approach**

I think I should take a more refined approach for my search. Maybe I’ll look within chapters for paragraphs that contain both terms along with key phrases like "Verdier/linear duality," "bulk," "coincide," "supplies," "constructs," or "is the." It seems like I can also rely on the audit summary and the current RG for help. This structured method might lead me to the information I need more effectively!
exec
/bin/zsh -lc "rg -n 'Verdier/linear duality|Verdier duality on bar cohomology|constructed by first taking bar cohomology|obtained via Verdier duality on bar cohomology|bar cohomology, then Verdier|bar cohomology.*Verdier' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'supplies the bulk field content|bar-cobar duality and holographic duality coincide|candidate bulk package: the Koszul dual|boundary-to-bulk map: the' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'The passage from bar complex to derived center|derived center.*bar complex|bar complex.*derived center|bar.*Koszul dual.*bulk|Koszul dual.*bulk.*bar' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/beta_gamma.tex:1882:simplest object in which bar-cobar duality and holographic duality coincide.
chapters/examples/free_fields.tex:4949:between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
chapters/examples/free_fields.tex:4950:supplies the bulk field content, and the bar-cobar filtration degree
chapters/frame/preface.tex:484:$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
 succeeded in 51ms:
chapters/examples/free_fields.tex:2810: second arrow is Verdier/linear duality, producing the Koszul dual
chapters/connections/thqg_introduction_supplement.tex:118:algebra, constructed by first taking bar cohomology, then Verdier/linear
chapters/theory/introduction.tex:2671:$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
 succeeded in 51ms:
chapters/theory/introduction.tex:1470:derived center, not on the bar complex. The closed sector of any
chapters/theory/en_koszul_duality.tex:1306:The passage from bar complex to derived center is

thinking
**Inspecting components**

I need to take a closer look at free_fields 2810 and introduction 2671, as there might be an issue related to Verdier/linear duality. I'll also check free_fields 2806 and the introduction around 2671 to get more context. Additionally, I think line 484 might mention something about the bar boundary-to-bulk. It's important to inspect these elements thoroughly to ensure everything lines up correctly and there's no oversight in the analysis.
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '2804,2814p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2804	\item \emph{Koszul duality} (algebra $\to$ dual coalgebra $\to$ dual algebra).
  2805	 \[\mathcal{H}_k \xrightarrow{\;\bar{B}\;} \bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \xrightarrow{\;(-)^\vee\;} \mathrm{Sym}^{\mathrm{ch}}(V^*)\]
  2806	 The first arrow is the bar construction: extraction of OPE residues
  2807	 along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  2808	 dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  2809	 conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
  2810	 second arrow is Verdier/linear duality, producing the Koszul dual
  2811	 \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
  2812	 construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  2813	 \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  2814	 (Theorem~\ref{thm:bar-cobar-inversion-qi}).
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2666,2674p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '478,490p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '701,717p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   478	$S_r(\cA)\in H^*(\overline{\cM}_{0,r})$ is the obstruction to
   479	extending the inversion one step further. The tower
   480	$\{S_r\}_{r\ge 2}$ terminates when the obstruction
   481	hierarchy collapses to finitely many terms.
   482	
   483	The conjectural extension (Volume~II) identifies
   484	$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
   485	derived centre
   486	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
   487	R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
   488	reassembles the bulk from the coalgebraic shadow. Volume~I
   489	proves bar-cobar inversion; Volume~II would upgrade it to bulk
   490	reconstruction.
 succeeded in 52ms:
  2666	\index{critical pitfalls|textbf}
  2667	
  2668	The following distinctions are the most common sources of error:
  2669	
  2670	\smallskip\noindent\textbf{Four objects.}
  2671	$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
  2672	
  2673	\smallskip\noindent\textbf{Grading.}
  2674	Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.
 succeeded in 51ms:
   701	\subsection{AdS/CFT and holography}
   702	
   703	The bar-cobar duality admits a conjectural holographic interpretation:
   704	
   705	\begin{conjecture}[Holographic duality; \ClaimStatusConjectured]\label{conj:deformation-holographic}
   706	\[\text{Bulk theory on } AdS_3 \longleftrightarrow \text{Boundary chiral algebra on } S^1\]
   707	
   708	The boundary genus expansion should model the bulk theory:
   709	\[Z_{\text{bulk}}[AdS_3] = \exp\left(\sum_{g=0}^\infty \hbar^{2g-2} F_g\right)\]
   710	where $F_g$ are free energies computed via configuration space integrals.
   711	(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
   712	\end{conjecture}
   713	
   714	\begin{remark}[Scope and the bar/center distinction]
   715	The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.
   716	
   717	\emph{Clarification on bar vs.\ center.}
exec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '714,730p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   714	\begin{remark}[Scope and the bar/center distinction]
   715	The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.
   716	
   717	\emph{Clarification on bar vs.\ center.}
   718	The genus expansion $F_g$ is a projection of the universal MC
   719	element $\Theta_\cA \in \MC(\gAmod)$, which lives in the
   720	\emph{modular convolution algebra}, not in the bar complex itself.
   721	The bar complex $\barB(\cA)$ classifies twisting morphisms
   722	(boundary deformation data); the \emph{derived center}
   723	$Z_{\mathrm{der}}(\cA) \simeq C^\bullet_{\mathrm{ch}}(\cA,\cA)$
   724	is the bulk observable algebra
   725	(Theorem~\ref{thm:operadic-center-hochschild}).
   726	The genus expansion records the scalar projections of $\Theta_\cA$
   727	and should be compared with bulk amplitudes via the center, not
   728	directly via the bar complex.
   729	
   730	\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '72,88p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'boundary-to-bulk map|Verdier/linear duality|bulk package: the Koszul dual|derived centre.*bar|bar.*derived centre|bar.*derived center|derived center.*bar' chapters/frame/preface.tex chapters/examples/free_fields.tex chapters/connections/thqg_introduction_supplement.tex chapters/theory/introduction.tex --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    72	Feigin--Frenkel centre makes the cohomology unbounded.
    73	
    74	The five theorems are the $\Sigma_n$-invariant skeleton. The full
    75	$E_1$ structure (the $r$-matrix, the Yangian, the spectral
    76	braiding) is developed in this volume; Volume~II adds the
    77	open/closed holomorphic-topological lift through
    78	$\SCchtop$ and the topologized bulk. The Drinfeld double
    79	$U_\cA := \cA \bowtie \cA^{!}_\infty$, assembled from the ordered
    80	bar's two factors, is conjectured to be the universal boundary-bulk
    81	reconstructor.
    82	
    83	\section*{1.\quad The ordered bar construction on algebraic curves}
    84	% ====================================================================
    85	
    86	\medskip
    87	
    88	\noindent
 succeeded in 52ms:
chapters/frame/preface.tex:484:$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
chapters/theory/introduction.tex:1470:derived center, not on the bar complex. The closed sector of any
chapters/theory/introduction.tex:2279: $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
chapters/theory/introduction.tex:2671:$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
chapters/examples/free_fields.tex:2810: second arrow is Verdier/linear duality, producing the Koszul dual
chapters/examples/free_fields.tex:4949:between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$





thinking
**Analyzing mathematical concepts**

I think mentioning bar and Koszul dual without addressing derived center could work—but it might be wiser to include derived center as the fifth object for clarity. The user is asking for a search on paragraphs featuring both bar and Koszul dual or derived center. This paragraph summarizes potential pitfalls, which might well include Z^{der}_{ch}(\cA). AGENTS suggests listing all five objects, so revising the introduction accordingly seems helpful. I’ll consider separating linear and Verdier duality in free_fields and thqg_intro_supplement while updating the introduction too.
thinking
**Refining mathematical patches**

I notice that both free_fields and thqg_intro fall within the user's request and mix linear and Verdier duality, which needs to be fixed. It might be a good idea to search for "Verdier/linear duality" throughout the chapters so I can clearly separate strict from homotopy duality—there are three occurrences to patch. I’ll consider revising the preface too, as "bar's two factors" might not be necessary and could conflate bar as a boundary-to-bulk map.
thinking
**Considering editing scope**

I'm thinking about whether I should fix issues in the document as I encounter them. The task clearly states to search for specific paragraphs mentioning both items and verify all five objects, so maybe that should be my focus. But if I encounter clear conflation in the same file, I might need to address it. I should keep the edits minimal, but since it seems relevant, it could be acceptable to fix within the same document.
thinking
**Focusing on issues in files**

I want to concentrate on files that show actual problems and consider including related issues if they're significant. Some potential files to check include chapters/examples/free_fields.tex, which has two issues related to wording and conflation, and chapters/theory/introduction.tex, where there’s a missing derived center. I’m also looking at chapters/frame/preface.tex for boundary-to-bulk map conflation, as well as chapters/connections with mixing issues. I may need to run a script that identifies specific keywords across documents.
thinking
**Searching for specific paragraphs**

I could look for paragraphs that mention both "bar" and either "derived center" or "Koszul dual," along with the word "bulk." I might want to use a targeted paragraph search for this. To narrow it down, I could create a `perl` command that matches those keywords and patterns. After running this, hopefully, I'll find additional relevant results that highlight the issues I’m addressing. Let’s see what insights I can uncover!
exec
/bin/zsh -lc "perl -0ne 'while(/(?:"'^|'"\\n\\s*\\n)(.*?)(?=\\n\\s*\\n|\\z)/sg){"'$p=$1; next unless $p =~ /bar/i && $p =~ /(Koszul dual|derived center)/i; next unless $p =~ /(bulk|Verdier'"\\/linear|boundary-to-bulk|supplies|coincide|reassembles|constructs it from the bar complex alone|constructs the triangle from the bar complex alone)/i; ("'$s=$p)=~s/'"\\s+/ /g; print qq{"'$ARGV:$.:$s'"\\n};}}' "'$(rg --files chapters | rg '"'\\.tex"'$'"')" in /Users/raeez/chiral-bar-cobar exited 255 in 51ms:
Unmatched right curly bracket at -e line 1, at end of line
syntax error at -e line 1, near ";}"
Execution of -e aborted due to compilation errors.

thinking
**Fixing syntax issues**

I need to sort out the escape or Perl syntax. It might help to use simpler quoting, like using `cat << 'EOF'` for command strings. I'm also considering Ruby as an option, since it could be easier. However, I want to make sure that I use Perl correctly too. Balancing between the two may give me a better solution while avoiding potential pitfalls. Plus, I really want to make this work smoothly!
exec
/bin/zsh -lc "perl -0ne 'while(/(?:"'^|'"\\n\\s*\\n)(.*?)(?=\\n\\s*\\n|\\z)/sg){"'$p=$1; next unless $p =~ /bar/i && $p =~ /(Koszul dual|derived center)/i; next unless $p =~ /(bulk|Verdier'"\\/linear|boundary-to-bulk|supplies|coincide|reassembles|constructs it from the bar complex alone)/i; ("'$s=$p)=~s/'"\\s+/ /g; print qq{"'$ARGV:$.:$s'"\\n}; }' "'$(rg --files chapters | rg '"'\\.tex"'$'"')" in /Users/raeez/chiral-bar-cobar succeeded in 317ms:
rived-center} \\ $\Theta^{\mathrm{oc}}_\cA$ & open/closed MC element & Constr.~\ref{constr:thqg-oc-mc-element} \\ $r(z)$ & collision residue (classical $r$-matrix) & Def.~\ref{def:thqg-holographic-datum}(c) \\ $\nabla^{\mathrm{hol}}$ & modular shadow connection & Def.~\ref{def:thqg-holographic-datum}(e) \\ $\operatorname{Tr}_\cA$ & annulus trace ($=HH_*$) & Thm.~\ref{thm:thqg-annulus-trace} \\ $\mathfrak{R}^{\mathrm{oc}}_\bullet(\cA)$ & nonlinear resonance tower & Constr.~\ref{constr:thqg-oc-quartic-resonance} \end{tabular} \end{center} The datum extends the holographic modular Koszul datum $\mathcal{H}(\cA)$ (Definition~\ref{def:thqg-holographic-datum}) by adding the derived center (universal bulk), the annulus trace (open modular shadow), and the nonlinear resonance tower (quartic and higher obstructions in the derived center). \end{definition}
chapters/connections/editorial_constitution.tex:29:\begin{conjecture}[Holographic duality from bar-cobar; \ClaimStatusConjectured]\label{conj:ads-cft-bar} The curved bar complex of a boundary chiral algebra $\cA$ provides an algebraic model for the bulk theory on AdS$_3$: \begin{enumerate}[label=\textup{(\roman*)}] \item The bar complex $\barB(\cA)$ classifies twisting morphisms (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual} $\cA^!$ models the bulk field content \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk \emph{observable} algebra is the derived centre $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$ itself. \item The curvature $m_0 = \kappa \cdot \mathbf{1}$ encodes the cosmological constant $\Lambda \sim -1/R_{\mathrm{AdS}}^2$, with $\kappa \sim c/2 \sim R_{\mathrm{AdS}}^2/\ell_P^2$. \item The genus expansion $\sum_g g_s^{2g-2} \barB^{(g)}$ is the $1/N$ expansion of the dual gauge theory, with $g_s \sim 1/N$. \item Bar-cobar inversion $\Omega(\barB(\cA)) \simeq \cA$ recovers the boundary algebra~(Theorem~B). The boundary-to-bulk map is the chiral centre construction $\cA \mapsto C^\bullet_{\mathrm{ch}}(\cA, \cA)$. \end{enumerate} \end{conjecture}
chapters/connections/editorial_constitution.tex:29:\begin{remark}[Scope]\label{rem:ads-scope} Costello--Paquette \cite{CP2020} conjecture (footnote~8) that curved Koszul duality controls twisted supergravity on AdS$_3$. Our framework provides the mathematical structure they require: the curved $A_\infty$ bar complex (Theorem~\ref{thm:bar-ainfty-complete}), the genus expansion (Theorem~\ref{thm:genus-universality}), and the complementarity theorem (Theorem~\ref{thm:quantum-complementarity-main}) relating boundary and bulk. The bar--semi-infinite identification for affine Kac--Moody algebras \textup{(}Theorem~\ref{thm:bar-semi-infinite-km}\textup{)} is proved, and the principal W-algebra extension remains conditional on Theorem~\ref{thm:bar-semi-infinite-w}. Thus the theorematic boundary algebraic package is fully in place on the Kac--Moody side and only conditionally in place on the principal W side. The open problem is the bulk side of the dictionary: a filtered H-level bulk target, if required, belongs upstream to MC4, and the comparison with twisted supergravity is the downstream MC5 step. Concretely, the remaining gap is the identification of the \emph{bulk} observables with the twisted supergravity theory, which requires input from 3d gauge theory (Chern--Simons formulation of gravity on AdS$_3$, $\mathfrak{sl}_2 \oplus \mathfrak{sl}_2$ gauge group).
chapters/connections/editorial_constitution.tex:29:The anomaly cancellation programme (\S\ref{subsec:anomaly-koszul}) is the physical interpretation of the curvature theory: $\kappa_{\mathrm{tot}} = 0$ is both the mathematical condition $d_{\mathrm{bar}}^2 = 0$ and the physical condition for consistent quantization (Theorem~\ref{thm:anomaly-koszul}). This feeds directly into the AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where the curvature $m_0 = \kappa \cdot \mathbf{1}$ plays the role of the cosmological constant: the bar-cobar adjunction $\barB(\cA) \dashv \Omega(\barB(\cA))$ models the boundary-to-bulk and bulk-to-boundary maps of holographic duality. The $3$d mirror symmetry programme (\S\ref{subsec:3d-mirror}) extends this physical circle from $2$d to $3$d, with $\Eone$-chiral Koszul duality (Theorem~\ref{thm:e1-chiral-koszul-duality}) replacing the $\Etwo$-chiral theory and Coulomb--Higgs exchange replacing bar-cobar inversion.
chapters/connections/thqg_introduction_supplement_body.tex:34:Volume~II applies the engine to the full bulk/boundary/line triangle in~$3$d holomorphic-topological QFT\@. The bar complex's differential is $\mathbb{C}$-direction factorization; its deconcatenation coproduct is $\mathbb{R}$-direction factorization; together they make $\barB_X(\cA)$ an $\Eone$-chiral coassociative coalgebra on $\mathrm{FM}_k(\mathbb{C}) \times \operatorname{Conf}_k(\mathbb{R})$. The $\mathrm{SC}^{\mathrm{ch,top}}$ structure emerges on the derived center pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$; the recognition theorem, homotopy-Koszulity, PVA descent, and the derived conformal-block line-operator identification are proved in Volume~II. The PVA quantization bridge and holographic applications complete the programme.
chapters/connections/holographic_datum_master.tex:35:\begin{proposition}[Recovery of $\mathcal{H}(T)$ from $U_\cA$; \ClaimStatusHeuristic] \label{prop:hdm-u-a-recoverability} \index{Drinfeld double!boundary-bulk recoverability|textbf} \index{holographic modular Koszul datum!recovery from $U_\cA$|textbf} Let $\cA$ be a modular Koszul chiral algebra on a smooth projective curve~$\cC$, and let $U_\cA := \cA \bowtie \cA^{!}_\infty$ be the Drinfeld double of~$\cA$ and its Verdier-dual factorization companion. The six components of the holographic modular Koszul datum $\mathcal{H}(T) = (\cA, \cA^!, \cC, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$ (Definition~\ref{def:holographic-modular-koszul-datum}) are projections of~$U_\cA$ as follows. \begin{enumerate}[label=\textup{(R\arabic*)}] \item \emph{Boundary factor.} The first tensor factor of~$U_\cA$ is the boundary chiral algebra~$\cA$. \item \emph{Dual factor.} The second tensor factor of~$U_\cA$ is the Verdier-dual factorization companion~$\cA^{!}_\infty$; its linear cohomological shadow is the chiral Koszul dual~$\cA^!$. \item \emph{Factorization base.} The curve~$\cC$ on which~$U_\cA$ carries its factorization structure recovers the base of $\mathcal{H}(T)$. \item \emph{Quasitriangular $R$-matrix.} The spectral $R$-matrix of the quasitriangular structure on~$U_\cA$ equals the collision residue~$r_\cA(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ by the seven-way master theorem (Theorem~\ref{thm:hdm-seven-way-master}). \item \emph{Universal MC element.} The bar-intrinsic differential on the convolution dg~Lie algebra $\mathfrak{g}_\cA^{\mathrm{mod}}$ associated to~$U_\cA$ produces the universal Maurer--Cartan element~$\Theta_\cA$ by $\Theta_\cA = D_\cA - d_0$ (Theorem~\ref{thm:mc2-bar-intrinsic}). \item \emph{Shadow connection.} The modular shadow connection $\nabla^{\mathrm{hol}}_{g,n} = d - \operatorname{Sh}_{g,n}(\Theta_\cA)$ is the flat connection produced by projecting~$\Theta_\cA$ to the $(g,n)$-sector, and therefore depends only on~$U_\cA$. \end{enumerate} Consequently, $\mathcal{H}(T)$ is recoverable from~$U_\cA$ alone: the six slots carry no information beyond the Drinfeld double, and the six-tuple is an invariant of~$U_\cA$ rather than independent data. \end{proposition}
chapters/connections/holographic_datum_master.tex:35:\begin{remark}[Status and scope] \label{rem:hdm-u-a-recoverability-scope} Items~(R1), (R3), (R4) are unconditional for modular Koszul~$\cA$: the factor structure of~$U_\cA$ and the seven-way master theorem supply them directly. Item~(R5) is unconditional (Theorem~\ref{thm:mc2-bar-intrinsic}), although the identification of the convolution algebra~$\mathfrak{g}_\cA^{\mathrm{mod}}$ with a structure intrinsic to~$U_\cA$ uses the bar-cobar adjunction of Theorem~A. Item~(R6) is a direct corollary of (R5). Item~(R2) requires the analytic passage from the Verdier-dual factorization companion~$\cA^{!}_\infty$ to the strict Koszul dual~$\cA^!$, which is controlled by the bar-cobar inversion of Theorem~B on the Koszul locus; beyond the Koszul locus, the passage is conjectural and the proposition is heuristic. The overall recoverability statement is therefore tagged \ClaimStatusHeuristic: the individual projections are proved where the structural machinery is available, and the global assembly into a single invariant of~$U_\cA$ is the content of the boundary-bulk reconstruction thesis of Remark~\ref{rem:five-facets-boundary-bulk} and Section~\ref{sec:hdm-thesis}. \end{remark}
chapters/connections/holographic_datum_master.tex:35:\begin{remark}[Four consistency conditions for the six-slot thesis] \label{rem:hdm-four-consistency-conditions} \index{Drinfeld double!four consistency conditions|textbf} The six-slot recovery of $\mathcal{H}(T)$ from~$U_\cA$ is not tautological: for the thesis to hold, the Drinfeld double and the six projections must satisfy four compatibility conditions. Each condition was flagged as an open problem in the frontier audit of the Drinfeld double programme (Section~\ref{sec:frontier-modular-holography-platonic}, parts~(a)--(d)); the reading of Proposition~\ref{prop:hdm-u-a-recoverability} converts the four open problems into four consistency laws that the six-tuple must obey. \begin{enumerate}[label=\textup{(C\arabic*)}] \item \emph{Quasitriangular compatibility.} The spectral $R$-matrix of~$U_\cA$ must satisfy the classical Yang--Baxter equation on the nose, not merely up to homotopy. This is the collision-depth-$2$ projection of the MC equation (Theorem~\ref{thm:collision-depth-2-ybe}) and is verified in slot~(R4) by the seven-way master theorem. \item \emph{Factorization compatibility.} The factorization structure of~$U_\cA$ over~$\cC$ must be compatible with the Ran-space factorization of the underlying chiral algebra~$\cA$, so that the curve slot~$\cC$ carries a single well-defined factorization algebra. This is the content of the Verdier-intertwining part of Theorem~A and is unconditional on the Koszul locus. \item \emph{Shadow compatibility.} The modular shadow connection $\nabla^{\mathrm{hol}}$ produced from slot~(R5) by projection~(R6) must agree with the independent genus-expansion definition of the shadow connection on every $(g,n)$ stratum. This is the flatness $(\nabla^{\mathrm{hol}}_{g,n})^2 = 0$, a consequence of the MC equation, verified on the sphere by Theorem~\ref{thm:sphere-reconstruction}; at higher genus it is the content of the analytic sewing programme (conditional beyond genus~$1$). \item \emph{Duality compatibility.} The second tensor factor of $U_\cA$ must agree with the chiral Koszul dual~$\cA^!$ of~$\cA$ on cohomology, with the passage $\cA^{!}_\infty \to \cA^!$ controlled by bar-cobar inversion on the Koszul locus. This is Theorem~B; beyond the Koszul locus the identification is conjectural and the proposition is heuristic. \end{enumerate} Conditions~(C1)--(C3) are proved in the stated scopes; condition~(C4) is the conditional input that makes Proposition~\ref{prop:hdm-u-a-recoverability} heuristic rather than unconditional. Together, the four conditions are the four structural requirements that the Drinfeld double programme must satisfy for the boundary-bulk reconstruction thesis to hold, and each one is a falsification target in the sense of Principle~\ref{princ:hdm-falsification}. \end{remark}
chapters/connections/frontier_modular_holography_platonic.tex:36:\begin{remark}[Reduction of boundary--defect realization] \label{rem:boundary-defect-reduction} At genus~$0$ and the level of derived categories, the identification $\cA^!_{\mathrm{univ}} \simeq \Omega(\barBch(\cA^!))$ is bar-cobar inversion (Theorem~B) applied to~$\cA^!$: Theorem~\ref{thm:bar-cobar-isomorphism-main} recovers the boundary algebra from its bar coalgebra. The protected dual-transform theorem \textup{(}Theorem~\textup{\ref{thm:frontier-protected-bulk-antiinvolution})} then gives $\mathbb{H}_X(\cA) \simeq \cA^!$. What remains conjectural is the identification of the \emph{geometric} KK-reduced boundary algebra (produced by dimensional reduction of the 3d HT bulk) with the \emph{algebraic} Koszul dual, at the level of the modular category carrying $\Theta_\cA$. This requires a 3d geometric input: constructing the bulk factorization algebra on $X \times \mathbb{R}_{\geq 0}$ whose boundary restriction is~$\cA^!$. \end{remark}
chapters/connections/frontier_modular_holography_platonic.tex:36:\begin{evidence} The hook-type corridor supplies the proved seed family. The 2023--2025 inverse Hamiltonian reduction results in type~$A$ make the edge set of~$\Gamma_N$ dense enough that every partition is reachable from a hook vertex. The remaining content is the edge-compatibility hypothesis: that Koszul duality commutes with each proved reduction functor. This is the correct intermediate conjecture, sharper than the old ``arbitrary Barbasch--Vogan duality'' slogan but still large enough for the frontier label. \end{evidence}
chapters/connections/frontier_modular_holography_platonic.tex:36:\item \emph{Exclusion of physical candidates.} For $N \geq 3$, the dual $\mathrm{M5}_N^!$ does not coincide with any known physical theory: \begin{itemize} \item \emph{Not a $6$d $(1,0)$ theory}: the $(1,0)$ anomaly coefficient $a_{(1,0)}$ is always positive \textup{(}Ohmori--Shimizu--Tachikawa--Yonekura~\cite{OSTY14}\textup{)}, but $\kappa^! < 0$. The sign mismatch is absolute. \item \emph{Not the S-dual}: Koszul duality $\lambda \mapsto 2 - \lambda$ is a homological operation on the bar complex, not a duality of the physical theory. In every compactification dimension ($6$d, $5$d on~$S^1$, $4$d on~$T^2$, $3$d on~$T^3$), the Koszul involution differs from the physical duality (S-duality, T-duality, $3$d mirror symmetry). \end{itemize} \end{enumerate} \end{proposition}
chapters/connections/entanglement_modular_koszul.tex:37:\begin{remark}[Island formula as Koszul dual dominance] \label{rem:ent-island-koszul} \index{island formula!Koszul interpretation} In the language of Penington~\cite{Penington19} and Almheiri--Engelhardt--Marolf--Maxfield~\cite{AEMM19}, the \emph{island} is the region of the bulk where the Koszul dual bar complex $B(\cA^!)$ dominates the matter bar complex $B(\cA)$. The transition from the Hawking phase to the island phase is the exchange of dominant saddle in the complementarity sum $\mathbf{C}_g(\cA) = \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$ (Theorem~\ref{thm:quantum-complementarity-main}). The physical content of the Page curve is that entanglement growth is controlled by $\kappa(\cA)$ at early times and by $\kappa(\cA^!)$ at late times; the complementarity constant $\kappa + \kappa' = 13$ determines the crossover. \end{remark}
chapters/connections/master_concordance.tex:39:\begin{center} \renewcommand{\arraystretch}{1.3} \begin{tabular}{|l|l|l|} \hline \textbf{Label} & \textbf{Source chapter} & \textbf{Content} \\ \hline\hline \texttt{prop:five-facets-collision-residue} & \texttt{introduction.tex} & Five facets of $r(z)$ as collision residue \\ \hline \texttt{prop:bc-general-spin-class-c} & \texttt{free\_fields.tex} & $bc$ system has class $C$ shadow depth for all $\lambda$ \\ \hline \texttt{prop:koszul-brst-anomaly-preservation} & \texttt{bv\_brst.tex} & Koszul duality preserves BRST anomaly cancellation \\ \hline \texttt{prop:calogero-shadow-dictionary} & \texttt{arithmetic\_shadows.tex} & Calogero--Moser integrals coincide with shadow tower \\ \hline \texttt{prop:bar-sym-n-synthesis} & \texttt{toroidal\_elliptic.tex} & $\mathrm{Sym}^N$ synthesis for bar complex \\ \hline \texttt{prop:d-module-purity-km-equivalence} & \texttt{chiral\_koszul\_pairs.tex} & D-module purity equivalent to PBW on Kac--Moody locus \\ \hline \texttt{prop:universal-instanton-action} & \texttt{higher\_genus\_modular\_koszul.tex} & Universal instanton action $A=(2\pi)^2$ \\ \hline \texttt{prop:c13-full-self-duality} & \texttt{higher\_genus\_modular\_koszul.tex} & Full higher-genus tower self-duality of Virasoro at $c=13$ \\ \hline \end{tabular} \end{center}
chapters/connections/thqg_introduction_supplement.tex:41:The \emph{line-operator category} is the derived module category of the Koszul dual algebra: \begin{equation}\label{eq:supp-line-category-def} \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}. \end{equation} Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral algebra, constructed by first taking bar cohomology, then Verdier/linear duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms are chain maps.
chapters/connections/thqg_introduction_supplement.tex:41:The three vertices assemble into a commutative triangle of categories and functors: \begin{equation}\label{eq:supp-holographic-triangle-diagram} \begin{tikzcd}[row sep=huge, column sep=huge] & \text{Bulk: } \mathbf{C}_g(\cA) \arrow[dl, "\text{restrict}"'] \arrow[dr, "\text{cofiber}"] & \\ \text{Boundary: } \cA \arrow[rr, "\text{Koszul dual}"'] \arrow[ur, "\barB_X"] & & \text{Lines: } \cA^!\text{-}\mathsf{mod} \end{tikzcd} \end{equation} The left edge is the bar construction $\barB_X$, which maps the boundary algebra to the bar coalgebra (a factorization coalgebra contributing to the ambient complex). The right edge is the holographic cofiber: $\mathbf{H}_g^{\mathrm{hol}}(\cA) = \operatorname{cofib}(\mathbf{Q}_g(\cA) \to \mathbf{C}_g(\cA)) \simeq \mathbf{Q}_g(\cA^!)$ (Theorem~\ref{thm:frontier-protected-bulk-antiinvolution}(iii)). The bottom edge is Koszul duality: $\cA \mapsto \cA^!$ by the bar-then-dualize construction, with the module category $\cA^!\text{-}\mathsf{mod}$ as the categorical output.
chapters/connections/concordance.tex:44:\subsection*{Ring~3: The physics-facing extension problems} Three axes, each with its own appendix chain: \begin{enumerate} \item \emph{The $\mathcal{W}$-algebra axis.} Completed Koszulity is ubiquitous (every affine $\mathcal{W}$-algebra at generic level); strict Koszulity is exceptional. The subregular family $\mathcal{W}_n^{(2)}$ exhibits unbounded canonical homotopy degree. \item \emph{The Yangian/RTT axis and the Bridge Theorem.} Three layers: local RTT kernel, completed envelope, boundary quotient. The shift belongs to the boundary quotient, not the local kernel. The rank-one test case produces the quantized Kleinian surface. The \emph{Bridge Theorem project} (Remark~\ref{rem:bridge-theorem-programme}; Theorem~\ref{thm:bridge-criterion}) is now the central remaining target: the full triple equivalence $\mathrm{Fact}^{\Eone}_{\mathrm{ord}} \simeq \mathrm{Mod}^{\mathrm{comp}}(\Ydg_\cA) \simeq \mathrm{Rep}^{\mathrm{spec}}(\QGspec(R_\cA))^{\mathrm{op}}$ decomposes into four sub-targets~B1--B4 with a proved criterion theorem (B1$+$B2$+$B4 $\Rightarrow$ full bridge). \item \emph{The holographic/celestial axis.} Protected transform calculus (dual transform, transposition, Weyl sewing, metaplectic anomaly) built directly from the proved core. Volume~II develops the bulk--boundary--line Koszul triangle $A_{\mathrm{bulk}} \simeq Z_{\mathrm{der}}(\text{boundary}) \simeq \mathrm{HH}^\bullet(\cA^!)$. The \emph{holographic modular Koszul datum} $\mathcal{H}(T) = (\cA, \cA^!, \mathcal{C}, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$ (Definition~\ref{def:holographic-modular-koszul-datum}) extends the \emph{modular Koszul triple} $(\cA, \cA^!, r(z))$ (Definition~\ref{def:modular-koszul-triple}) to the full HT holographic system in a single modular MC problem: the dg-shifted Yangian $r(z)$ is the binary genus-zero collision residue of~$\Theta_\cA$, and the 2026 exact sphere-correlator matching~\cite{GZ26} is the genus-zero matrix-element shadow of this datum. Five theorem targets decompose the programme: boundary--defect realization (Conjecture~\ref{conj:boundary-defect-realization}), Yangian-shadow (Theorem~\ref{thm:yangian-shadow-theorem}; \textbf{proved}), sphere reconstruction on established comparison surfaces (Theorem~\ref{thm:sphere-reconstruction}; \textbf{proved}), quartic resonance obstruction (Theorem~\ref{thm:quartic-resonance-obstruction}; \textbf{proved}), and singular-fiber descent (Conjecture~\ref{conj:singular-fiber-descent}). The factorisation quantum-group envelope~\cite{Latyntsev23} supplies the categorical home beyond the meromorphic line category, and the HT deformation-quantization functor (Conjecture~\ref{conj:ht-deformation-quantization}) bridges classical PVA data to the quantum modular Koszul package. The landscape of worked physics examples now includes: free chiral vortex lines with explicit $r$-matrix (\S\ref{sec:betagamma-vortex-lines}), affine PVA $\to$ Chern--Simons action (\S\ref{sec:affine-ht-chern-simons}), SQED--XYZ mirror symmetry as bar-cobar equivalence, non-renormalization of tree-level operations (\S\ref{sec:non-renormalization-tree}), superpotential $A_\infty$ truncation (\S\ref{sec:superpotential-ainfty-truncation}), Virasoro phase space as Teichm\"uller geometry (\S\ref{subsec:virasoro-teichmuller-phase-space}), level-rank-type Chern--Simons analogy for Koszul duality, monopole operators via affine Grassmannian modifications, Costello's M2-brane double-loop model (developed in Volume~III, Chapter~\ref{chap:toroidal-elliptic}), SuperVirasoro $\to$ 3d supergravity, SQCD boundary algebra, Witten diagrams in twisted holography, $N=4$ global symmetry matching, the deformed conifold, and $\mathcal{W}_N \to$ higher-spin gauge theory. \end{enumerate}
chapters/connections/concordance.tex:44:The open/closed realization (\S\ref{sec:thqg-open-closed-realization}) constructs the algebraic bridge between the local chiral Hochschild theory and the global bordered FM geometry. The central results: \begin{enumerate}[label=\textup{(\alph*)}] \item The \emph{chiral endomorphism operad} $\mathcal{E}\!nd^{\mathrm{ch}}_A$ with consecutive block-substitution (Definition~\ref{def:thqg-chiral-endomorphism-operad}). This is the nonsymmetric operad governing $A_\infty$-chiral algebras. \item The \emph{brace dg algebra structure} on chiral Hochschild cochains $\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA)$ (Theorem~\ref{thm:thqg-brace-dg-algebra}). \textbf{Proved}: the same tree-combinatorial argument as Gerstenhaber--Voronov, with block-substitution replacing simple reindexing. \item The \emph{chiral derived center} $\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA) := H^*(\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA), \delta)$ (Definition~\ref{def:thqg-chiral-derived-center}). On the Koszul locus this is a three-term chiral Gerstenhaber algebra $\mathcal{Z}^0 \oplus \mathcal{Z}^1 \oplus \mathcal{Z}^2$ by Theorem~H. \item The \emph{universal open/closed pair} $\mathcal{U}(\cA) = (\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA),\, \cA,\, \mathrm{id})$ (Theorem~\ref{thm:thqg-swiss-cheese}). \textbf{Proved}: the chiral Swiss-cheese theorem, asserting that the derived center is the universal bulk with open color~$\cA$. \item The \emph{local-global bridge} (Theorem~\ref{thm:thqg-local-global-bridge}): restriction of the bordered FM convolution to the formal disk identifies with $\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA)$. \textbf{Proved}: Morita invariance of the derived center. \item The \emph{annulus trace theorem} (Theorem~\ref{thm:thqg-annulus-trace}): $\int_{S^1_p} \mathcal{M} \simeq HH_*(\mathcal{M})$. \textbf{Proved}: by Ayala--Francis $\otimes$-excision on the standard Weiss cover of $S^1_p$, reducing to the two-sided bar complex $A_b \otimes^{\mathbf{L}}_{A_b^e} A_b = HH_*(A_b)$. The annulus degeneration proposition (Proposition~\ref{prop:thqg-annulus-degeneration-kappa}) connects this to the genus-$1$ curvature: $\Delta_{\mathrm{ns}}(\operatorname{Tr}_\cA) = \kappa(\cA) \cdot \lambda_1$. \item The \emph{open/closed MC element} $\Theta^{\mathrm{oc}}_\cA = \Theta_\cA + \sum_j \mu^{\mathcal{M}_j}$ (Construction~\ref{constr:thqg-oc-mc-element}, Theorem~\ref{thm:thqg-oc-mc-equation}). \textbf{Proved}: satisfies the MC equation in $\mathfrak{g}^{\mathrm{oc}}_{\cA, \vec{\mathcal{M}}}$ by Stokes' theorem on the bordered FM compactification. \item The \emph{open/closed quartic resonance class} $\mathfrak{R}^{\mathrm{oc}}_4(\cA) \in \mathcal{Z}^2$ (Construction~\ref{constr:thqg-oc-quartic-resonance}). Vanishes for G-type, tree-only for L-type, both terms nonzero for M-type. $\mathfrak{R}^{\mathrm{oc}}_4(\mathrm{Vir}_c)$ has poles at $c = 0$ and $c = -22/5$. \item The \emph{completed modular Koszul datum} $\Pi^{\mathrm{oc}}_X(\cA)$ (Definition~\ref{def:thqg-completed-platonic-datum}): eight-fold datum extending $\mathcal{H}(\cA)$ by the derived center, annulus trace, and nonlinear resonance tower. \end{enumerate} \noindent\emph{Key distinction.} Bar/cobar classifies \emph{twisting morphisms} (universal couplings between $\cA$ and $\cA^!$). The derived center classifies \emph{bulk operators acting on the boundary}. These are complementary: the bar complex is the coalgebraic shadow of the boundary, while the derived center is the universal bulk. The open/closed MC element $\Theta^{\mathrm{oc}}_\cA$ packages both into a single object, with the closed projection recovering $\Theta_\cA$ and the mixed projection recovering the bulk-to-boundary coupling.
chapters/connections/concordance.tex:44:\paragraph{Five negative principles (permanent).} \label{par:concordance-five-negative-principles} \begin{enumerate}[label=\textup{(N\arabic*)}] \item \emph{Bar $\neq$ bulk.} The bar complex classifies twisting morphisms (couplings between $\cA$ and $\cA^!$). The bulk observables are the chiral derived center $\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. These are different objects solving different problems. \item \emph{Boundary algebra $=$ chart.} The boundary algebra $A_b = \operatorname{End}(b)$ depends on the choice of compact generator~$b$. The Morita-invariant primitive is the boundary dg-category $\mathcal{C}_{\mathrm{op}}$. \item \emph{Tangential log geometry.} The correct global stage is a tangential log curve $(X, D, \tau)$, not a punctured curve $(X \setminus D)$. The real-oriented blowup at punctures produces the boundary intervals and circles on which the open sector lives. \item \emph{Modularity $=$ trace $+$ clutching.} The bar-intrinsic MC element $\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$ satisfies the clutching factorization at all genera (Theorem~\ref{thm:mc2-bar-intrinsic}(iii)). The open/closed MC equation $D^{\mathrm{oc}}\Theta^{\mathrm{oc}} + \tfrac{1}{2}[\Theta^{\mathrm{oc}}, \Theta^{\mathrm{oc}}] + \hbar\Delta_{\mathrm{clutch}}(\Theta^{\mathrm{oc}}) = 0$ is proved at all genera (Theorem~\ref{thm:thqg-oc-mc-equation}). Its closed projection recovers $\Theta_\cA$ with the genus tower $F_g = \kappa \cdot \lambda_g$ on the uniform-weight lane (Theorem~\ref{thm:thqg-oc-projection}(i), Theorem~D). Its open projection at genus~$1$ is the annulus trace (Theorem~\ref{thm:thqg-annulus-trace}). Because all sectors are projections of the \emph{same} MC element $\Theta^{\mathrm{oc}}_\cA$, the MC equation forces open-closed consistency at every genus (Theorem~\ref{thm:thqg-mc-forced-consistency}): the genus-$g$ closed-sector amplitude and the genus-$g$ open-sector amplitude are jointly constrained by a single identity, and no additional consistency check is required. Two distinct questions: (a)~the scalar formula $F_g = \kappa \cdot \lambda_g$ \emph{fails} for multi-weight algebras at $g \geq 2$: the full free energy includes a cross-channel correction (\textbf{op:multi-generator-universality}, resolved negatively; Theorem~\ref{thm:multi-weight-genus-expansion}); (b)~the independent open-sector derivation of genus-$g$ amplitudes from iterated clutching on $\mathcal{C}_{\mathrm{op}}$ without using the bar-intrinsic construction. \item \emph{Honest scope.} The dg-shifted Yangian is proved for the affine lineage (Vol~II, Theorem~\textup{thm:Koszul\_dual\_Yangian}). The general perturbative 3d~HT Yangian structure is conjectural. The BV/BRST~$=$~bar identification at higher genus is resolved in the coderived category $D^{\mathrm{co}}$ for all shadow classes (Theorem~\ref{thm:bv-bar-coderived}); at chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M fails. The Heisenberg scalar level is proved at the chain level (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}). \end{enumerate}
chapters/connections/concordance.tex:44:\begin{center} \renewcommand{\arraystretch}{1.25} \begin{tabular}{lp{8cm}l} \textbf{Former label} & \textbf{Result} & \textbf{Mechanism} \\ \hline \ref{thm:lattice-sewing} & Lattice sewing envelope (Theorem~\ref{thm:lattice-sewing}, promoted) & HS-sewing $+$ Fock factorization $+$ Siegel $\Theta$-convergence \\ \ref{thm:nms-full-resonance-tower} & Full resonance tower (Theorem~\ref{thm:nms-full-resonance-tower}) & $\Theta_\cA$ bar-intrinsic \\ \ref{thm:nms-all-degree-resonance-boundary} & All-degree clutching law (Theorem~\ref{thm:nms-all-degree-resonance-boundary}) & Mok degeneration $+$ boundary filtration \\ \ref{thm:nms-bipartite-vanishing} & Bipartite vanishing & Lagrangian isotropy: $P^{++} = P^{--} = 0$ \\ \ref{thm:bifunctor-obstruction-decomposition} & Bifunctor obstruction & One-slot Koszul factorization \\ \ref{thm:convolution-formality-one-channel} & Scalar-orbit formality & scalar $\Theta_\cA$ $\Rightarrow$ formal scalar MC orbit \\ \ref{conj:EO-recursion}\textup{(b)} & MC-shadow recursion in the Koszul case \textup{(}Cor.~\ref{cor:topological-recursion-mc-shadow}\textup{)}; full EO identification remains conditional on Conj.~\ref{conj:v1-bar-worldline} & MC tautological relation $+$ Chern--Weil transform \\ \hline \multicolumn{3}{l}{\textit{% April 2026 session: arithmetic, purity, and CohFT}} \\ \hline \ref{thm:shadow-eisenstein} & Genus-$1$ amplitude Mellin transform is Eisenstein: $D_2(\cA,s) = -24\kappa \cdot \zeta(s)\,\zeta(s{-}1)$ & $\sigma_1$ Dirichlet convolution $+$ $E_2^*$ Fourier expansion \\ \ref{rem:categorical-zeta-riemann} & $\zeta^{\mathrm{DK}}_{\mathfrak{sl}_2}(s) = \zeta(s) - 1$: Riemann zeta from $\mathfrak{sl}_2$ irreps & dimension counting $+$ analytic continuation \\ \ref{prop:d-module-purity-km} & $\cD$-module purity for affine KM \textup{(}converse of~(xii)\textup{)} & chiral localization $+$ Hitchin VHS $+$ Saito \\ \ref{prop:universal-instanton-action} & Universal instanton action $A = (2\pi)^2$, Stokes constant $S_1 = -4\pi^2\kappa i$ & Borel singularities $=$ $Q_L$ branch points \\ \ref{prop:c13-full-self-duality} & Entire tower self-dual at $c = 13$ \textup{(}not just~$\kappa$\textup{)} & shadow trace formula RTF $= 0$ \\ Vol.~II, rank-$1$ DR string equation & CohFT string equation at rank $1$ & DR cycle forgetful $+$ Buryak DR/DZ \\ \ref{thm:pixton-from-mc-semisimple} & Pixton ideal from MC for semisimple cases & FSZ $+$ PPZ $+$ Givental--Teleman \\ \ref{thm:operadic-complexity} & $r_{\max} = d_\infty = f_\infty$ \textup{(}operadic complexity identification\textup{)} & induction on degree $+$ HPL tree formula \\ \hline \multicolumn{3}{l}{\textit{% April 2026 session: theorem architecture rewrites (A1--A6~+~G7)}} \\ \hline \ref{lem:chirhoch-descent} & Chiral Hochschild descent: $\ChirHoch^{\bullet}(\cA) \cong (\mathbb{D}_{\Ran}\barB(\cA))_{\Sigma}$ on the Koszul locus & Theorem~A Verdier intertwining $+$ coinvariant descent \\ \ref{prop:koszul-closure-properties} & Closure of chiral Koszulness under tensor product, Koszul dualization, and base change & three pre-existing fragments consolidated; quotients excluded \\ \ref{prop:d-module-purity-km-equivalence} & Kac--Moody equivalence via Saito--Kashiwara weight filtration: PBW strictness~(ii) $\iff$ $\cD$-module purity~(xii) & chiral localization $+$ Hitchin VHS $+$ Saito \\ \ref{prop:shadow-tower-three-lenses} & Three equivalent descriptions of $S_r(\cA)$: algebraic (shadow), geometric (formality obstruction), holographic (boundary-bulk correction) & bar-intrinsic MC $+$ formality identification $+$ derived-centre factorization \\ \ref{def:generating-depth} & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth $d_{\mathrm{alg}}$: formal distinction~; Virasoro $d_{\mathrm{gen}} = 3$, $d_{\mathrm{alg}} = \infty$ & depth decomposition $+$ class~M tower non-termination \\ \hline \multicolumn{3}{l}{\textit{% April 2026 session: structural propositions and depth classification}} \\ \hline \ref{prop:sc-formal-iff-class-g} & SC-formality characterises class~$\mathbf{G}$: $\cA$ is Swiss-cheese formal iff class~$\mathbf{G}$ \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)} & abelian bracket $+$ nondegeneracy of~$\kappa$ \\ \ref{prop:depth-gap-trichotomy} & Algebraic depth gap: $d_{\mathrm{alg}}(\cA) \in \{0,\,1,\,2,\,\infty\}$, no finite $d_{\mathrm{alg}} \geq 3$ realized \textup{(}Proposition~\ref{prop:depth-gap-trichotomy}\textup{)} & Riccati algebraicity $+$ $\Delta$-dichotomy \\ \ref{prop:chirhoch1-affine-km} & $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)} & Koszul resolution $+$ adjoint cochain \\ \ref{prop:e1-nonsplitting-genus1} & $E_1$ non-splitting at genus~$1$: quasi-modular $E_2$ obstruction \textup{(}Proposition~\ref{prop:e1-nonsplitting-genus1}\textup{)} & genus-$0$ persistence $+$ $E_2$ anomaly \\ \ref{prop:free-field-scalar-exact} & Free-field exactness: $\delta F_g^{\mathrm{cross}}(\cA) = 0$ for all free-field families at all genera \textup{(}all-weight; Proposition~\ref{prop:free-field-scalar-exact}\textup{)} & quadratic OPE $\Rightarrow$ no mixed channels \\ \ref{prop:virasoro-shadow-ratio-riccati} & Virasoro shadow growth rate: $|S_{r+1}/S_r| \to \rho^{-1}$ from Riccati root asymptotics \textup{(}Proposition~\ref{prop:virasoro-shadow-ratio-riccati}\textup{)} & explicit $Q_L^{\mathrm{Vir}}(t)$ $+$ Darboux \\ \hline \multicolumn{3}{l}{\textit{% April 2026 session: operadic corrections, falsification, and new structural results}} \\ \hline \ref{prop:gerstenhaber-sl2-bracket} & Gerstenhaber bracket on $\ChirHoch^*(\widehat{\fsl}_2)$: explicit $\fsl_2$-equivariant computation \textup{(}Proposition~\ref{prop:gerstenhaber-sl2-bracket}\textup{)} & Koszul resolution $+$ chiral endomorphism calculus \\ \ref{prop:ds-chirhoch-compatibility} & DS--ChirHoch compatibility: DS reduction commutes with chiral Hochschild \textup{(}Proposition~\ref{prop:ds-chirhoch-compatibility}\textup{)} & BRST complex $+$ HPL transfer \\ \ref{prop:ker-av-schur-weyl} & Kernel of averaging: $\dim\ker(\mathrm{av}_n) = n! - \binom{n+d-1}{n}$ closed formula via Schur--Weyl \textup{(}Proposition~\ref{prop:ker-av-schur-weyl}\textup{)} & Schur--Weyl duality $+$ symmetric group characters \\ Vol.~III & $E_1$-obstruction is categorical: $E_1 \not\to E_2$ promotion obstructed by non-trivial Drinfeld associator \textup{(}Volume~III proposition on the categorical $E_2$-obstruction for CY$_3$\textup{)} & associator $+$ monodromy \\ Ordered-center conjecture & Ordered chiral center of the Yangian: derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$ as $E_2$-chiral algebra \textup{(}Conjecture\textup{)} & standalone paper; cf.\ Theorem~\ref{thm:yangian-e1} \\ \ref{conj:coderived-e3} & Coderived $E_3$: $D^{\mathrm{co}}$-level $E_3$ on $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ without conformal vector \textup{(}Conjecture\textup{)} & \S\ref{sec:en-koszul-duality} \\ \ref{conj:center-essential-surjectivity} & Center essential surjectivity: every $E_2$-chiral algebra arises as a derived center \textup{(}Conjecture\textup{)} & \S\ref{sec:en-koszul-duality} \\ \ref{constr:sugawara-antighost} & Sugawara antighost construction: conformal vector at non-critical level yields antighost field for topologization & \S\ref{sec:en-koszul-duality} \\ \hline \multicolumn{3}{l}{\textit{% April 2026 session: AP165 bar-complex operadic correction}} \\ \hline \multicolumn{3}{p{13cm}}{% \textbf{AP165 correction (constitutional).} The bar complex $\barB(\cA)$ is an $E_1$ coassociative coalgebra over $(\mathrm{ChirAss})^!$, the Koszul dual cooperad of the chiral associative operad. It is \emph{not} an $\SCchtop$-coalgebra. The $\SCchtop$ structure emerges on the derived chiral center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\; \cA)$: bulk acts on boundary. See Vol~II CLAUDE.md, AP165/B54--B56.} \\ \hline \multicolumn{3}{p{13cm}}{% \textbf{SC self-duality retracted.} $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\, \text{shuffle-mixed})$: the closed dimensions are $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not} Koszul self-dual. The duality \emph{functor} is an involution; the \emph{operad} is not self-dual. See AP166/B57.} \\ \hline \multicolumn{3}{p{13cm}}{% \textbf{Topologization scoped.} The cohomological topologization theorem (Theorem~\ref{thm:topologization}: $\SCchtop + \text{inner conformal vector} \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology) is proved for affine Kac--Moody at non-critical level. The same theorem gives an unconditional chain-level $E_3^{\mathrm{top}}$ model on the zero-differential cohomology complex, which is quasi-isomorphic as a chain complex to the original derived center. The lift to the original cochain complex is conditional on the $A_\infty$-coherence equation $[m,G]=\partial_z$; beyond affine Kac--Moody, the full package remains conjectural (Conjecture~\ref{conj:topologization-general}).} \\ \hline \multicolumn{3}{p{13cm}}{% \textbf{Critical level: Theorem~H does NOT apply.} At the critical level $k = -h^\vee$ for affine KM, $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional (Feigin--Frenkel center). Theorem~H (polynomial Hilbert series, cohomological degrees $\{0,1,2\}$) requires generic level. For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is unbounded and $4$-periodic.} \\ \end{tabular} \end{center}
chapters/connections/concordance.tex:44:\begin{center} \renewcommand{\arraystretch}{1.25} \small \begin{tabular}{cp{10.5cm}} \textbf{Status} & \textbf{Result} \\ \hline \multicolumn{2}{l}{\textsc{Green} \textup{(proved local algebra)}} \\[2pt] & Theorems A--H (bar-cobar adjunction, inversion, complementarity, modular characteristic, chiral Hochschild) \\ & MC1, MC2, MC4, and the analytic/coderived lanes of MC5 (PBW, bar-intrinsic MC, strong completion towers, HS-sewing, coderived BV$=$bar) \\ & MC3 proved for all simple types on the evaluation-generated core; DK-4/5 (extension beyond evaluation modules) downstream \\ & Koszulness programme: $9$ unconditional equivalences \textup{(}with factorization homology at genus~$0$\textup{)} $+$ $1$ proved consequence \textup{(}chiral Hochschild on the Koszul locus\textup{)} $+$ $1$ conditional (Lagrangian) $+$ $1$ one-directional (D-module purity) \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\ & Shadow obstruction tower algebraicity: $H(t)^2 = t^4 Q_L(t)$, tower determined by $(\kappa, \alpha, S_4)$ \textup{(}Theorem~\ref{thm:riccati-algebraicity}\textup{)}; cubic coefficient $\alpha = S_3/\kappa$ universal per family: $\alpha = 0$ \textup{(}Heis\textup{)}, $\alpha = 2$ \textup{(}Vir\textup{)}, family-specific for $\Walg_N$ and affine KM \\ & $\kappa$ formula universality: $\kappa(\cH_k) = k$, $\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$, $\kappa(\mathrm{Vir}_c) = c/2$, $\kappa(\Walg_N) = c(H_N{-}1)$ \\ & $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for uniform-weight modular Koszul algebras at all genera \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\ & Swiss-cheese theorem \textup{(}Theorem~\ref{thm:thqg-swiss-cheese}\textup{)} \\ & Chiral derived center as universal bulk \\ & Annulus trace \textup{(}Theorem~\ref{thm:thqg-annulus-trace}\textup{)} \\ & Heisenberg and lattice sewing \textup{(}Theorems~\ref{thm:heisenberg-sewing}, \ref{thm:lattice-sewing}\textup{)} \\ & HS-sewing for the entire standard landscape (universal algebras) \textup{(}Theorem~\ref{thm:general-hs-sewing}\textup{)} \\ & All-degree inverse limit $\Theta_\cA = \varprojlim \Theta_\cA^{\le r}$ \textup{(}Theorem~\ref{thm:recursive-existence}\textup{)} \\ & Algebraic-family rigidity \textup{(}Theorem~\ref{thm:algebraic-family-rigidity}\textup{)} \\ & DS primitivity of the gravitational coproduct (Vol~II, Theorem~\textup{thm:ds-hpl-transfer}) \\ & Epstein zeta of the shadow metric: functional equation for class~$\mathbf{M}$ at rational~$c$ \textup{(}Theorem~\ref{thm:shadow-epstein-zeta}\textup{)} \\ & Shadow field $K_L = \bQ(\sqrt{\operatorname{disc}(Q_L)})$: imaginary quadratic for class~$\mathbf{M}$; trivial for class~$\mathbf{G}/\mathbf{L}$ \textup{(}Remark~\ref{rem:shadow-field}\textup{)} \\ & Descent fan: three independent projections of $\Theta_\cA$ (categorical, spectral, modular) \textup{(}Proposition~\ref{prop:descent-fan}\textup{)} \\ & Lattice fan closure: all three projections compatible for lattice VOAs \textup{(}\S\ref{subsec:concordance-descent-fan}\textup{)} \\ & SC-formality $\iff$ class~$\mathbf{G}$ \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)} \\ & Algebraic depth gap: $d_{\mathrm{alg}} \in \{0,1,2,\infty\}$ \textup{(}Proposition~\ref{prop:depth-gap-trichotomy}\textup{)} \\ & $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)} \\ & $E_1$ non-splitting at genus~$1$ \textup{(}Proposition~\ref{prop:e1-nonsplitting-genus1}\textup{)} \\ & Free-field exactness: $\delta F_g^{\mathrm{cross}} = 0$ for all free-field families \textup{(}Proposition~\ref{prop:free-field-scalar-exact}\textup{)} \\ & Virasoro shadow growth rate from Riccati \textup{(}Proposition~\ref{prop:virasoro-shadow-ratio-riccati}\textup{)} \\ & Gerstenhaber bracket on $\ChirHoch^*(\widehat{\fsl}_2)$ \textup{(}Proposition~\ref{prop:gerstenhaber-sl2-bracket}\textup{)} \\ & DS--ChirHoch compatibility \textup{(}Proposition~\ref{prop:ds-chirhoch-compatibility}\textup{)} \\ & Kernel of averaging: $\dim\ker(\mathrm{av}_n) = n! - \binom{n{+}d{-}1}{n}$ \textup{(}Proposition~\ref{prop:ker-av-schur-weyl}\textup{)} \\ & $E_1$-obstruction categorical \textup{(}Vol.~III, categorical $E_2$-obstruction proposition\textup{)} \\ & Toric chart gluing \textup{(}Vol.~III toric chart gluing theorem, promoted from conjecture\textup{)} \\[4pt] \multicolumn{2}{l}{\textsc{Amber} \textup{(externally supported, conditional, or physically interpreted)}} \\[2pt] & Shadow CohFT \textup{(}Theorem~\ref{thm:shadow-cohft}; equivariance and splitting proved; flat identity conditional on $|0\rangle \in V$, see\textup{)} \\ & Gravitational interpretation of $\kappa$ as central charge of the boundary graviton \\ & BTZ black hole entropy from the binary $r$-matrix \\ & Entanglement entropy $S_{\mathrm{EE}} = (c/3)\log(L/\epsilon)$ from $\kappa$-level complementarity \\ & Holographic dictionary: bulk reconstruction from the derived center \\ & BV/BRST $=$ bar at higher genus: resolved in $D^{\mathrm{co}}$ for all shadow classes \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)}; chain-level proved for classes~G/L, conditional for class~C on harmonic decoupling, false for class~M; Heisenberg scalar level proved at chain level \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\ & Shadow--chromatic correspondence \textup{(}Remark~\ref{rem:chromatic-shadow-correspondence}\textup{)} \\[4pt] \multicolumn{2}{l}{\textsc{Red} \textup{(unproved global modular descent)}} \\[2pt] & Multi-generator universality at $g \geq 2$: scalar formula \emph{fails}; cross-channel correction nonzero \textup{(}Open Problem~\ref{op:multi-generator-universality}, resolved negatively\textup{)} \\ & Modular cooperad completion: full modular cooperad structure on the open factorization category $\mathcal{C}_{\mathrm{op}}$ \\ & Global open sector on tangential log curves \textup{(}modest globalisation over $(X,D,\tau)$\textup{)} \\ & Pixton ideal generation from class-M shadows \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)} \\ & Arithmetic Langlands bridge: arithmetic descent from function field to number field \textup{(}Remark~\ref{rem:langlands-gap-b}\textup{)} \\ & Modular periodicity for simple quotients at admissible levels \textup{(}Conjecture~\ref{conj:modular-periodicity-minimal}\textup{)} \\ & D-module purity: converse direction \textup{(}item~(xii) of Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\ & Shadow principal class: whether $Q_L$ always represents the principal ideal class \textup{(}Conjecture~\ref{conj:shadow-principal-class}\textup{)} \\ & Non-lattice $L$-function descent: sewing lift $\to$ $L$-function content for non-lattice algebras \textup{(}\S\ref{subsec:concordance-descent-fan}\textup{)} \\ & DS shadow depth monotonicity: every non-trivial DS reduction escalates $\mathbf{L} \to \mathbf{M}$ \textup{(}Conjecture~\ref{conj:ds-shadow-depth-monotonicity}\textup{)} \\ & Resurgent shadow classification: G/L/C/M governs transseries and Stokes structure \textup{(}Conjecture~\ref{conj:resurgent-shadow-classification}\textup{)} \\ & $E_1$ non-splitting at genus~$2$: seven stable-graph obstruction classes \textup{(}Conjecture~\ref{conj:e1-nonsplitting-genus2}\textup{)} \\ & Koszul boundary as swampland boundary: complement of Koszul locus $=$ algebraic swampland \textup{(}Conjecture~\ref{conj:koszul-swampland}\textup{)} \\ & Shadow $s{=}1$ pole, quantum modularity, and volume growth \textup{(}Conjecture~\ref{conj:shadow-s1-quantum-volume}\textup{)} \\ & Page curve from Koszul complementarity \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\ & Ordered chiral center of the Yangian \textup{(}standalone conjecture\textup{)} \\ & Coderived $E_3$ without conformal vector \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\ & Center essential surjectivity \textup{(}Conjecture~\ref{conj:center-essential-surjectivity}\textup{)} \end{tabular} \end{center}

thinking
**Searching for terms**

I’m thinking about searching for current suspicious terms related to "models the bulk field content" and possibly focusing on "free_fields." It seems important to search for the phrase "bulk field content" across different chapters to gather more context. I want to be thorough in my approach and find any relevant information that could help clarify these terms. Let’s see what insights I can uncover with this search!
exec
/bin/zsh -lc "rg -n 'bulk field content|models the bulk field content|supplies the bulk field content' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '24,36p;2038,2048p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:4950:supplies the bulk field content, and the bar-cobar filtration degree
chapters/connections/editorial_constitution.tex:2016: $\cA^!$ models the bulk field content
chapters/theory/poincare_duality_quantum.tex:1247:bar construction with bulk field content, and of the cobar construction
 succeeded in 52ms:
    24	(Theorems~\ref{thm:master-pbw},
    25	\ref{thm:pbw-allgenera-km},
    26	\ref{thm:pbw-allgenera-virasoro},
    27	\ref{thm:pbw-allgenera-principal-w}).
    28	Scalar saturation for all algebraic families
    29	(Theorem~\ref{thm:algebraic-family-rigidity}).
    30	Ambient $D^2 = 0$ at both levels
    31	(Theorem~\ref{thm:ambient-d-squared-zero}).
    32	
    33	\smallskip\noindent
    34	\emph{Finite-order engine.}\enspace
    35	Shadow obstruction tower $\Theta_\cA^{\leq r}$ with
    36	obstruction classes, quartic resonance class with clutching law,
  2038	the curved $A_\infty$ bar complex
  2039	(Theorem~\ref{thm:bar-ainfty-complete}), the genus expansion
  2040	(Theorem~\ref{thm:genus-universality}), and the
  2041	complementarity theorem (Theorem~\ref{thm:quantum-complementarity-main})
  2042	relating boundary and bulk. The bar--semi-infinite identification
  2043	for affine Kac--Moody algebras
  2044	\textup{(}Theorem~\ref{thm:bar-semi-infinite-km}\textup{)}
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '2012,2018p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2012	an algebraic model for the bulk theory on AdS$_3$:
  2013	\begin{enumerate}[label=\textup{(\roman*)}]
  2014	\item The bar complex $\barB(\cA)$ classifies twisting morphisms
  2015	 (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
  2016	 $\cA^!$ models the bulk field content
  2017	 \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  2018	 \emph{observable} algebra is the derived centre
exec
/bin/zsh -lc "nl -ba chapters/theory/poincare_duality_quantum.tex | sed -n '1242,1250p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1242	\begin{remark}[Physical evidence and scope]
  1243	This conjecture is supported by matching of partition functions,
  1244	three-point functions, and conformal blocks between boundary W-algebras
  1245	and bulk Vasiliev theory \cite{GG11}. It is labeled
  1246	\ClaimStatusConjectured{} because the holographic identification of the
  1247	bar construction with bulk field content, and of the cobar construction
  1248	with boundary reconstruction, requires physical input from the
  1249	AdS$_3$/CFT$_2$ correspondence that lies outside the algebraic framework
  1250	of this monograph. The mathematical content is the structural parallel

thinking
**Evaluating editing conditions**

This paragraph doesn't bring up the Koszul dual or derived center, but it could still be a clear issue, though it’s not applicable in the search condition. Maybe I should skip it unless I'm already editing the same file. Hmm, I might need to inspect `chapters/connections/editorial_constitution.tex` early on. It could make sense to apply a patch there. Let's make sure I read enough before deciding.
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '2012,2024p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2012	an algebraic model for the bulk theory on AdS$_3$:
  2013	\begin{enumerate}[label=\textup{(\roman*)}]
  2014	\item The bar complex $\barB(\cA)$ classifies twisting morphisms
  2015	 (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
  2016	 $\cA^!$ models the bulk field content
  2017	 \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  2018	 \emph{observable} algebra is the derived centre
  2019	 $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
  2020	 itself.
  2021	\item The curvature $m_0 = \kappa \cdot \mathbf{1}$ encodes
  2022	 the cosmological constant $\Lambda \sim -1/R_{\mathrm{AdS}}^2$,
  2023	 with $\kappa \sim c/2 \sim R_{\mathrm{AdS}}^2/\ell_P^2$.
  2024	\item The genus expansion $\sum_g g_s^{2g-2} \barB^{(g)}$

thinking
**Clarifying terminology issues**

I think there's a misunderstanding here: Volume II shouldn’t upgrade bar-cobar inversion to bulk reconstruction. Bulk reconstruction is actually based on derived center or Swiss-cheese models. So, it seems like I need to patch this up. Maybe I should search for similar phrases in the repository. I could look for “upgrade it to bulk reconstruction” and “boundary-to-bulk map” to see what's currently in use. That might provide clarity!
exec
/bin/zsh -lc "rg -n 'boundary-to-bulk map|upgrade it to bulk reconstruction|reassembles the bulk from the coalgebraic shadow|boundary algebra to the bar coalgebra' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'bar.*derived center|derived center.*bar' chapters/frame chapters/connections chapters/theory chapters/examples --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/editorial_constitution.tex:2029: boundary-to-bulk map is the chiral centre construction
chapters/frame/preface.tex:484:$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
chapters/frame/preface.tex:488:reassembles the bulk from the coalgebraic shadow. Volume~I
chapters/connections/thqg_introduction_supplement.tex:168:boundary algebra to the bar coalgebra (a factorization coalgebra
chapters/theory/poincare_duality_quantum.tex:1214: algebra (the boundary-to-bulk map is the center map, not the
chapters/connections/thqg_introduction_supplement_body.tex:139: maps the boundary algebra to the bar coalgebra. The trace
 succeeded in 51ms:
chapters/connections/thqg_introduction_supplement_body.tex:69:$\barB_X(\cA)$ itself but on the derived center pair
chapters/theory/en_koszul_duality.tex:1273:\index{Swiss-cheese operad!on derived center, NOT on bar}
chapters/theory/en_koszul_duality.tex:1306:The passage from bar complex to derived center is
chapters/theory/en_koszul_duality.tex:6673:(where $\barB^{\Sigma}(\cA)$ exists), the \emph{derived center}
chapters/theory/en_koszul_duality.tex:6734: the derived center, not the symmetric bar.
chapters/connections/concordance.tex:7269: derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
chapters/theory/introduction.tex:1470:derived center, not on the bar complex. The closed sector of any
chapters/theory/introduction.tex:2279: $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
chapters/theory/chiral_modules.tex:4619:derived center, equivalently on the bar resolution of the diagonal
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement.tex | sed -n '160,172p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   160	& \\
   161	\text{Boundary: } \cA
   162	 \arrow[rr, "\text{Koszul dual}"']
   163	 \arrow[ur, "\barB_X"]
   164	& & \text{Lines: } \cA^!\text{-}\mathsf{mod}
   165	\end{tikzcd}
   166	\end{equation}
   167	The left edge is the bar construction $\barB_X$, which maps the
   168	boundary algebra to the bar coalgebra (a factorization coalgebra
   169	contributing to the ambient complex). The right edge is the
   170	holographic cofiber: $\mathbf{H}_g^{\mathrm{hol}}(\cA) =
   171	\operatorname{cofib}(\mathbf{Q}_g(\cA) \to \mathbf{C}_g(\cA))
   172	\simeq \mathbf{Q}_g(\cA^!)$

thinking
**Analyzing diagram context**

I'm trying to understand the left edge of the diagram, thinking it might relate boundary to bulk. I feel like I need more context from lines 154 and possibly a triangle diagram. Line 167 mentions how bar construction maps boundary algebra to bar coalgebra, which seems promising. I should take a closer look at preface and line 484. Also, I think I'll inspect connections from line 69 and open sections around lines 64-72 for clarity.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement_body.tex | sed -n '64,72p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    64	The differential $d_C$ is $\Einf$-chiral (factorization on~$X$);
    65	the coproduct $d_R$ is $\Eone$-topological (deconcatenation on
    66	ordered configurations of~$\mathbb{R}$)
    67	(Theorem~\ref{thm:bar-swiss-cheese}).
    68	The $\mathrm{SC}^{\mathrm{ch,top}}$ two-colour datum emerges not on
    69	$\barB_X(\cA)$ itself but on the derived center pair
    70	$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$; see Volume~II\@.
    71	\end{definition}
    72	

thinking
**Inspecting the theorem label**

I need to check if the theorem label is outdated, but the sentence seems correct, so there’s no issue there. I might inspect chapters around the theory of Koszul duality, particularly around 1306, to clean up any mixed phrasing. I've noticed three occurrences in the introduction, free fields, and supplement chapters. It might be best to rephrase to clarify the distinctions in duality. I also want to update a summary and consider renaming a section from "Four objects" to "Five objects." It’s crucial to keep edits minimal and truthful.
exec
/bin/zsh -lc "rg -n '\\\\textbf\\{Four objects\\}|Four objects\\.' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/introduction.tex:2670:\smallskip\noindent\textbf{Four objects.}
exec
/bin/zsh -lc "rg -n 'Z\\"'^'"\\{.*der|derived center|derived centre|C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
424:(the chiral derived center
665: The deficiency is coefficient blow-up: the bulk derived center could
770:bulk via the chiral derived centre
771:$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the modular
842: $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \ChirHoch^*(\cA)$
1466:open/closed derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
1470:derived center, not on the bar complex. The closed sector of any
1547: $(\mathrm{ChirAss})^!$; the SC structure emerges on the derived center.
2279: $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
2503: $\SCchtop$ on the derived center pair; curved at
exec
/bin/zsh -lc "rg -n 'Koszul dual.*bulk|bulk.*Koszul dual|derived center.*bulk|bulk.*derived center' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:4949:between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
chapters/connections/thqg_open_closed_realization.tex:2:% The open/closed realization: chiral derived center as universal bulk
chapters/connections/thqg_open_closed_realization.tex:13:\section{The open/closed realization: chiral derived center as universal bulk}
chapters/connections/thqg_open_closed_realization.tex:1567: & derived center (universal bulk) & Def.~\ref{def:thqg-chiral-derived-center} \\
chapters/connections/thqg_open_closed_realization.tex:1582:by adding the derived center (universal bulk), the annulus trace
chapters/connections/genus_complete.tex:768:\index{bulk-boundary correspondence!derived center}
chapters/connections/genus_complete.tex:777:cohomology of the chiral category). The bulk is the derived center
chapters/examples/yangians_drinfeld_kohno.tex:6623: from the bulk algebra to the derived center of the boundary
chapters/theory/introduction.tex:665: The deficiency is coefficient blow-up: the bulk derived center could
chapters/theory/introduction.tex:2279: $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
chapters/theory/koszul_pair_structure.tex:1644:The AdS$_3$/CFT$_2$ interpretation requires: (a)~3d gravity as $SL(2,\mathbb{R})^2$ CS (Witten \cite{Wit89}); (b)~boundary WZW identification (Beilinson--Drinfeld \cite{BD04}); (c)~a holographic dictionary for ``Koszul duality exchanges bulk and boundary.'' The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.
chapters/connections/frontier_modular_holography_platonic.tex:1393:bulk) with the \emph{algebraic} Koszul dual, at the level of the
chapters/theory/poincare_duality_quantum.tex:48:For $N$ D-branes, the genus-graded boundary operator algebra (at $N \to \infty$) and the twisted supergravity bulk algebra are conjecturally related by genus-graded Koszul duality~\cite{CostelloGaiotto2020,FernandezCostelloP24}.
chapters/theory/poincare_duality_quantum.tex:88:For $K$ M2 branes at an $A_{N-1}$ singularity \cite{Costello-1705.02500v1}: the boundary algebra is $\mathcal{A}_{\mathrm{M2}} = \mathrm{Yangian}(\mathfrak{gl}_N)$ (twisted ABJM at $K \to \infty$), and the bulk algebra is $\mathcal{A}_{\mathrm{bulk}} = U_{\hbar,c}(\mathrm{Diff}(\mathbb{C}) \otimes \mathfrak{gl}_N)$. These are conjecturally related by curved Koszul duality with deformation parameter $c$.
chapters/theory/chiral_center_theorem.tex:46:Every bulk action factors uniquely through the derived center.
chapters/connections/thqg_introduction_supplement.tex:47:\subsection{Vertex 2: the bulk algebra (derived center)}
chapters/connections/thqg_introduction_supplement.tex:52:The \emph{bulk algebra} is the derived center of~$\cA$. Define the
chapters/theory/en_koszul_duality.tex:1290:The derived center is the algebra of bulk observables of
chapters/theory/en_koszul_duality.tex:3439:  bulk-boundary identification of the derived center.
chapters/frame/preface_sections10_13_draft.tex:124:the bulk; the derived center classifies bulk operators acting on the



thinking
**Reviewing file issues**

I’m looking into the current suspicious file related to Koszul duality, specifically line 1644 that mentions a holographic dictionary but no applicable bar. There’s another file where similar issues appear. Given the user’s task, I can look to patch certain files, focusing on active ones. However, drafts seem less relevant since the user specified Volume I. I'll verify which files are active before proceeding with any edits while ensuring to stick to the assigned files.
thinking
**Clarifying Pre-Edit Protocol**

The guidelines state that pre-edit verification is mandatory in hot zones, particularly regarding object and convention conflation. I’m considering which Pre-Edit (PE) protocol applies—maybe PE-4 would work, though there's no exact template. I’ll likely include a fenced block in my commentary to clarify object distinctions and end with a verdict of ACCEPT. PE-10 could be relevant as a scope quantifier, but I’m unsure if it fits perfectly for this task. I'll need to verify the specifics before proceeding.
thinking
**Planning commentary structure**

To comply with the guidelines, I’ll create a fenced block for commentary that summarizes object identities and includes a verdict of ACCEPT. Since there isn't an exact template, I’ll specify the scope. I’m thinking it might work well to use a custom scope lock alongside an object identity block. The AGENTS say I should fill this in as a fenced block for the hot zone, so I’ll ensure to provide this before proceeding with any edits.
codex
Scope lock and object check before edits:

```text
scope: five-object conflation audit on live Vol I prose in chapters/frame/preface.tex, chapters/theory/introduction.tex, chapters/examples/free_fields.tex, chapters/connections/thqg_introduction_supplement.tex, chapters/connections/editorial_constitution.tex
A: boundary/input chiral algebra
B(A): bar coalgebra / resolution
A^i = H^*(B(A)): dual coalgebra
A^!: strict Koszul dual algebra = (A^i)^vee
A^!_infty: Verdier image D_Ran(B(A)), homotopy Koszul-dual factorization algebra
Z^der_ch(A): derived center / bulk observable algebra
forbidden collapses checked: A^! != Z^der_ch(A); Omega(B(A)) != A^!; D_Ran(B(A)) != A^! unless explicitly marked homotopy/compatibility; bar != bulk
verdict: ACCEPT
```
exec
/bin/zsh -lc "rg -n '\\\\mathbb\\{D\\}_\\{\\\\Ran\\}|\\\\mathbb\\{D\\}_\\{\\\\operatorname\\{Ran\\}\\}' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
343:$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ with a chiral algebra.
460:$\mathbb{D}_{\Ran}\,\barB(\cH_k) \simeq (\cH_k^!)_\infty$.
556: $\mathbb{D}_{\operatorname{Ran}}\bar{B}_X(\cA)$ has no proved
564: \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1) \simeq \cA_2,
1129: \arrow[d, "\mathbb{D}_{\operatorname{Ran}}"]
1773: $\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA) \simeq
codex
I have the live edit set. I’m patching only the paragraphs that still collapse `A^!` into bulk, blur linear duality with Verdier duality, or treat the bar complex itself as the boundary-to-bulk map.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -2809,4 +2809,7 @@
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
@@ -4948,5 +4951,6 @@
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
M /Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex
@@ -2015,3 +2015,3 @@
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex
@@ -482,4 +482,5 @@
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
@@ -487,5 +488,6 @@
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -2669,4 +2669,4 @@
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement.tex
@@ -116,5 +116,8 @@
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
apply_patch(auto_approved=true) exited 0 in 46ms:
Success. Updated the following files:
M chapters/examples/free_fields.tex
M chapters/connections/thqg_introduction_supplement.tex
M chapters/theory/introduction.tex
M chapters/frame/preface.tex
M chapters/connections/editorial_constitution.tex
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..28d70579e59451516c33745effd18137616cc959
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..28d70579e59451516c33745effd18137616cc959
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.


thinking
**Verifying edits and searches**

I need to verify with grep and maybe run targeted searches for removed phrases while checking the context. There could still be issues with things like beta_gamma or parts on line 80. I should search through edited files for any remaining suspicious phrases and possibly rerun a paragraph scan.

Then, I might want to fix any compile problems that arise from the \cZ macro or lengthy lines. I'll also run rg in edited files for specific patterns, like `Verdier/linear duality`, and check paragraph clarity.
codex
The edits are in. I’m running a narrow falsification pass now: grep for the old bad phrases on the touched files, then re-read each patched paragraph in place.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement.tex | sed -n '114,123p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2668,2673p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '2804,2816p;4945,4953p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Verdier/linear duality|supplies the bulk field content|models the bulk field content|boundary-to-bulk map:|bar-cobar duality and holographic duality coincide|candidate bulk package: the Koszul dual' chapters/examples/free_fields.tex chapters/connections/thqg_introduction_supplement.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '2014,2020p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '483,491p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   114	\begin{equation}\label{eq:supp-line-category-def}
   115	\mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
   116	\end{equation}
   117	Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
   118	algebra, constructed by first taking bar cohomology and then linear
   119	duality. Separately,
   120	$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
   121	Koszul-dual factorization algebra. The module category
   122	$\cA^!\text{-}\mathsf{mod}$ is a
   123	$\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 succeeded in 50ms:
  2804	\item \emph{Koszul duality} (algebra $\to$ dual coalgebra $\to$ dual algebra).
  2805	 \[\mathcal{H}_k \xrightarrow{\;\bar{B}\;} \bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \xrightarrow{\;(-)^\vee\;} \mathrm{Sym}^{\mathrm{ch}}(V^*)\]
  2806	 The first arrow is the bar construction: extraction of OPE residues
  2807	 along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  2808	 dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  2809	 conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
  2810	 second arrow is linear duality on that coalgebra, producing the
  2811	 strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
  2812	 The separate Verdier image
  2813	 $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
  2814	 is the homotopy Koszul-dual factorization algebra. The cobar
  2815	 construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  2816	 \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  4945	
  4946	\subsubsection{Holographic duality via bar-cobar}
  4947	
  4948	\begin{conjecture}[Bulk-boundary correspondence; \ClaimStatusConjectured]
  4949	\label{conj:bulk-boundary-correspondence}
  4950	For a boundary chiral algebra $\cA$, the bar-cobar adjunction
  4951	$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
 succeeded in 50ms:
  2668	The following distinctions are the most common sources of error:
  2669	
  2670	\smallskip\noindent\textbf{Five objects.}
  2671	$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
  2672	
  2673	\smallskip\noindent\textbf{Grading.}
 exited 1 in 50ms:

 succeeded in 51ms:
  2014	\item The bar complex $\barB(\cA)$ classifies twisting morphisms
  2015	 (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
  2016	 $\cA^!$ models the line/defect sector
  2017	 \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  2018	 \emph{observable} algebra is the derived centre
  2019	 $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
  2020	 itself.
 succeeded in 51ms:
   483	The conjectural extension (Volume~II) uses
   484	$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
   485	resolution feeding the boundary-to-bulk story: the
   486	derived centre
   487	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
   488	R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
   489	is computed from Hochschild cochains using that resolution.
   490	Volume~I proves bar-cobar inversion and the bar-side input;
   491	Volume~II would add the separate bulk reconstruction through the
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..28d70579e59451516c33745effd18137616cc959
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.

exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '4950,4956p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4950	For a boundary chiral algebra $\cA$, the bar-cobar adjunction
  4951	$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
  4952	between $\cA$ and a candidate holographic package: the derived center
  4953	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
  4954	algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
  4955	the bar-cobar filtration degree maps to the radial coordinate.
  4956	(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..28d70579e59451516c33745effd18137616cc959
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.



thinking
**Clarifying the document editing process**

I need to ensure consistency in language, like fixing `derived centre` vs `center` in the file. I might run a search for suspicious patterns, perhaps just focusing on `beta_gamma`. Currently, I'm working on a task to search for paragraphs that mention both 'bar' and 'Koszul dual' or 'derived center'. I want to verify that I've accurately distinguished all five objects and eliminate any conflating language. I'll also need systematic verification to catch any remaining suspicious phrases.
thinking
**Searching for risky expressions**

The user has asked for an exhaustive search within certain chapters to find potentially risky expressions. I should consider employing a tool like "rg" to help with this task. I want to ensure I'm thorough in my search to meet the user's needs, so I’ll focus on searching the entire content specified while keeping my approach as efficient as possible. It’s important to be diligent about this!
codex
The local bad phrases in the patched files are gone. I’m doing one last repo-wide grep for the same five-object failure modes to check whether there are any remaining live hits inside the requested Vol I scope.
exec
/bin/zsh -lc "rg -n 'Verdier/linear duality|supplies the bulk field content|models the bulk field content|candidate bulk package: the Koszul dual|boundary-to-bulk map: the|bar-cobar duality and holographic duality coincide|obtained via Verdier duality on bar cohomology|Verdier duality on bar cohomology' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/beta_gamma.tex:1882:simplest object in which bar-cobar duality and holographic duality coincide.
exec
/bin/zsh -lc "rg -n 'bar.*(Koszul dual|derived center)|((Koszul dual|derived center).*)bar' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/deformation_quantization.tex:788:The paper on quadratic duality for chiral algebras \cite{GLZ22} focuses on Koszul duality for quadratic operads. The deformation quantization framework of this monograph generalizes from quadratic to arbitrary (non-quadratic via curvature), geometrizes the duality via bar-cobar configuration spaces, and provides explicit formulas for dualizing.
chapters/examples/deformation_quantization.tex:813:that the bar-cobar adjunction, restricted to the formal disk at genus~$0$, recovers classical Koszul duality, in agreement with the Francis--Gaitsgory formality
chapters/examples/w_algebras_deep.tex:515:The bar-complex dimensions across the simple types (Table~\ref{comp:w-bar-dims}) display a uniform pattern: at each bar degree the chain spaces are infinite-dimensional but graded-finite under the conformal weight grading, and the growth rates are governed by a single discriminant $\Delta(x)$ that is invariant under both DS reduction and Koszul duality. This uniformity persists in the large-$N$ limit, made precise below.
chapters/examples/w_algebras_deep.tex:579:the bar spectral sequence to collapse at~$E_2$, and the Koszul dual to
chapters/examples/w_algebras_deep.tex:894:The conjecture posits the existence of the bar complex of $\mathcal{W}_{1+\infty}$ as a completed inverse limit, with Koszul dual determined by the 't~Hooft coupling involution $\lambda \mapsto 1 - \lambda$.
chapters/examples/w_algebras_deep.tex:2081:bar--cobar/Koszul duality commutes with Drinfeld--Sokolov reduction
chapters/examples/w_algebras_deep.tex:2086:proving that bar--cobar/Koszul duality commutes with
chapters/examples/free_fields.tex:164:(Theorem~\ref{thm:mc2-bar-intrinsic}). The bar complex, Koszul dual, genus tower, and shadow invariants computed below are all \emph{outputs} of that single MC element, projected to the relevant degree and genus. For free-field archetypes, the projection is maximally simple: the Gaussian archetype (free fermion) has $\Theta_\cA = \Theta_\cA^{\leq 2}$, and the contact/quartic archetype ($\beta\gamma$, $bc$) terminates at $\Theta_\cA^{\leq 4}$.
chapters/examples/free_fields.tex:728:The $\beta\gamma$ system combines a bosonic weight-$1$ field $\beta$ and a bosonic weight-$0$ field $\gamma$. Its bar complex shares the discriminant $\Delta(x) = (1-3x)(1+x)$ with $\widehat{\mathfrak{sl}}_2$ and the Virasoro algebra. The Koszul dual is the $bc$ ghost system (\S\ref{sec:fermion-boson-koszul}).
chapters/examples/free_fields.tex:1674:Having computed the bar complexes, the Koszul duals are extracted next.
chapters/examples/free_fields.tex:1856:The residue pairing matrix of Step~3 is rank 3 (matching the 3 generators $\psi^{(-1)}, \psi^{(0)}, \psi^{(1)}$ paired against the 4 generators $\beta, \gamma, b, c$ of the derived $\beta\gamma$-$bc$ system). The pairing $\langle \psi^{(i)}, - \rangle: \mathcal{B}^{\bullet} \to \mathbb{C}$ identifies $\mathcal{F}^{\bullet}$ with the linear dual of the cogenerators of $\bar{B}(\mathcal{B}^{\bullet})$: the bar complex of the derived $\beta\gamma$-$bc$ system has cogenerators in bar degree 1 dual to $\psi^{(0)}, \psi^{(\pm 1)}$, with the bar differential $d_{\bar{B}}$ encoding the BRST differential $Q$ of Step~4. The $A_\infty$ structure on $\mathcal{F}^{\bullet}$ is then recovered from the Verdier dual $\mathbb{D}_{\mathrm{Ran}}(\bar{B}(\mathcal{B}^{\bullet}))$, which is the homotopy Koszul-dual factorization algebra computed from the bar resolution (Theorem~\ref{thm:bar-cobar-isomorphism-main}). This identifies $\mathcal{F}^{\bullet}$ as the homotopy Koszul dual $(\mathcal{B}^{\bullet})^!_\infty$. Note: the cobar functor $\Omega(\bar{B}(\mathcal{B}^{\bullet})) \simeq \mathcal{B}^{\bullet}$ (bar-cobar inversion, Theorem~B) recovers $\mathcal{B}^{\bullet}$ itself, not its Koszul dual.
chapters/examples/free_fields.tex:2021:The level $k$ determines the curvature of the Koszul dual: $m_0 = -k \cdot \omega \in \mathrm{Sym}^2(V^*)$. The bar differential satisfies $d^2 = 0$ (as it always does); the curvature manifests instead in the $A_\infty$ relation $m_1^2(a) = [m_0, a]_{m_2}$ on the cobar side.
chapters/examples/free_fields.tex:2025:Two distinct phenomena must be distinguished. \emph{Koszul duality}: the bar coalgebra $\bar{B}(\mathcal{H}_k)$, dualized, gives $\mathcal{H}_k^! = \mathrm{Sym}(V^*)$ (relating different algebras). \emph{Level-shifting}: $\mathrm{Rep}(\mathcal{H}_k) \simeq \mathrm{Rep}(\mathcal{H}_{-k})$ (an equivalence of representation categories). The former is algebraic; the latter is representation-theoretic.
chapters/examples/free_fields.tex:2484:$\sigma^!$ of the Koszul dual via the bar-cobar functor. Since the bar
chapters/examples/free_fields.tex:2749:\subsubsection{Computing the Koszul dual via bar-cobar}
chapters/examples/free_fields.tex:2771:The Koszul dual $\mathcal{H}_k^! \simeq \mathrm{Sym}^{\mathrm{ch}}(V^*)$ was computed in Theorem~\ref{thm:heisenberg-koszul-dual-early}; see Chapter~\ref{ch:heisenberg-frame}\index{Heisenberg algebra|textbf}\index{Fock space} for conventions. The bar complex $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) \simeq \mathrm{coLie}^{\mathrm{ch}}(V^*)$ is cocommutative because the double-pole OPE produces symmetric coproducts.
chapters/examples/free_fields.tex:2795:By Theorem~\ref{thm:heisenberg-bar}, the bar complex $\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$ has cocommutative coproduct: the Heisenberg OPE $\alpha(z)\alpha(w) \sim k(z-w)^{-2}$ produces only the double-pole term, whose residue gives a symmetric (primitive) coproduct $\Delta(\alpha) = \alpha \otimes 1 + 1 \otimes \alpha$. Cocommutative coalgebras are Koszul dual to commutative algebras ($\mathrm{Com}^! = \mathrm{Lie}$, see \cite{LV12}, Theorem~7.6.5), so $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$. This is commutative with regular OPE, while $\mathcal{H}_k$ is non-commutative with singular OPE, so $\mathcal{H}_k \not\cong \mathcal{H}_k^!$.
chapters/examples/free_fields.tex:3149:Chiral Koszul duality is a higher-dimensional Fourier transform: the bar construction
chapters/examples/free_fields.tex:3157:For $\cH_k$ on $\Sigma_g$, this reduction is literal: bar cohomology computes $H^*(\mathrm{Jac}(\Sigma_g), \mathcal{L}_k)$, the Koszul duality map acts via $\Omega \mapsto -\Omega^{-1}$, and Poisson summation on $\mathbb{Z}^g$ gives Fourier inversion. At genus~$1$: $\tau \mapsto -1/\tau$ and $\theta_3(-1/\tau) = (-i\tau)^{1/2}\,\theta_3(\tau)$. At genus~$g$: $\Theta(-\Omega^{-1}, \Omega^{-1}z) = (\det(-i\Omega))^{1/2}\, e^{i\pi z^T \Omega^{-1} z}\, \Theta(\Omega, z)$.
chapters/examples/free_fields.tex:4442:Koszul duality is a bar-cobar adjunction exchanging $\cA$
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..28d70579e59451516c33745effd18137616cc959
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.




thinking
**Evaluating potential issues**

I notice that a search shows the remaining issue is in `beta_gamma.tex` related to bad phrases, which could still present a problem. There might be other mismatches not identified. Since the user asked for fixes regarding D09 findings, I’m considering whether to patch the beta_gamma file. Even though it wasn't a strict match, it clearly addresses an ongoing problem. It seems like patching is necessary given that it falls within scope. I'll check the context further to decide on the patch.
thinking
**Deciding on patches**

I think it might be necessary to rewrite to clarify terms like boundary, defect, and bulk as explicit, which aligns with the D09 fix suggestion. I see no issues with action safety, so I’m considering patching `beta_gamma.tex` at line 1882. There's also `introduction.tex` to consider, but it seems less problematic. Since the user requested an exhaustive review, it’s prudent to use audit leads and search for patterns across chapters. I’ll patch `beta_gamma` and then look for any additional patterns afterward, just in case.
thinking
**Searching for paragraphs**

I'm focusing on finding paragraphs that mention both bar and Koszul dual or derived center. The table row I came across states `\cA^! as Verdier dual of \barB(\cA); resolves circularity...`, which seems to conflate strict A^! with homotopy Verdier image. I think this needs a patch as well. I'll search line 2214 in the introduction table since it looks promising. It feels important to inspect the context more closely before making any final decisions.
codex
One clear five-object slogan is still live in `beta_gamma.tex`, so I’m cleaning that as well. I’m also checking whether the introduction’s chapter-roadmap still overstates `\cA^!` as a Verdier image rather than the strict dual.
exec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '1878,1884p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1878	\index{holomorphic-topological!beta-gamma atom@$\beta\gamma$ atom}
  1879	Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
  1880	into the global geometry of curves, so factorization homology alone
  1881	controls the genus expansion. The $\beta\gamma$ system is therefore the
  1882	simplest object in which bar-cobar duality and holographic duality coincide.
  1883	\end{remark}
  1884	
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2208,2218p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2208	 $\barB_X(\cA)$ via residue extraction; \textbf{Theorem~A} (adjunction + Verdier intertwining); $d^2=0$ \\
  2209	Geometric cobar complex (Ch.~\ref{chap:cobar-construction}) &
  2210	 $\Omega_X$ as left adjoint; $d^2_{\mathrm{cobar}}=0$ via Verdier duality \\
  2211	Bar-cobar adjunction (Ch.~\ref{chap:bar-cobar-adjunction}) &
  2212	 \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
  2213	Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
  2214	 $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
  2215	Higher genus (Ch.~\ref{chap:higher-genus}) &
  2216	 Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
  2217	Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
  2218	 Chiral Koszul pairs; chiral modules; \textbf{Theorem~H} ($\ChirHoch^*$ polynomial, Koszul-functorial) \\
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..28d70579e59451516c33745effd18137616cc959
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.


thinking
**Considering patch updates**

I need to make some adjustments. The introduction table row should say `\cA^!_\infty as Verdier image of \barB(\cA)` and highlight that strict $\cA^!$ comes from bar cohomology duality, resolving circularity. I should keep it concise. I could simplify it to just `$\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar cohomology duality; resolves circularity...`. I’ll check if there are other instances of "as Verdier dual of \barB(\cA)" in the intro for potential patches.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -2213,3 +2213,3 @@
 Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
- $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
+ $\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality; resolves circularity in defining the Koszul dual \\
 Higher genus (Ch.~\ref{chap:higher-genus}) &
M /Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex
@@ -1881,3 +1881,4 @@
 controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which bar-cobar duality and holographic duality coincide.
+simplest object in which the boundary algebra, the Koszul-dual defect
+sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 73ms:
Success. Updated the following files:
M chapters/examples/beta_gamma.tex
M chapters/theory/introduction.tex
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index 179b335ff6db32ae029d5905213ff6b8b013f161..32f68d6b6583630d06ac1ccb670a3436706c04df
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -1879,7 +1879,8 @@
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
 controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which bar-cobar duality and holographic duality coincide.
+simplest object in which the boundary algebra, the Koszul-dual defect
+sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
 
 \section{From 3d \texorpdfstring{$\mathcal{N}=2$}{N=2} to the full chiral algebra}
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..789ce9acf5b68f150a665afd1b7486e6b1256a16
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2211,7 +2211,7 @@
 Bar-cobar adjunction (Ch.~\ref{chap:bar-cobar-adjunction}) &
  \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
 Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
- $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
+ $\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality; resolves circularity in defining the Koszul dual \\
 Higher genus (Ch.~\ref{chap:higher-genus}) &
  Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
 Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index 179b335ff6db32ae029d5905213ff6b8b013f161..32f68d6b6583630d06ac1ccb670a3436706c04df
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -1879,7 +1879,8 @@
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
 controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which bar-cobar duality and holographic duality coincide.
+simplest object in which the boundary algebra, the Koszul-dual defect
+sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
 
 \section{From 3d \texorpdfstring{$\mathcal{N}=2$}{N=2} to the full chiral algebra}
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..789ce9acf5b68f150a665afd1b7486e6b1256a16
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2211,7 +2211,7 @@
 Bar-cobar adjunction (Ch.~\ref{chap:bar-cobar-adjunction}) &
  \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
 Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
- $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
+ $\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality; resolves circularity in defining the Koszul dual \\
 Higher genus (Ch.~\ref{chap:higher-genus}) &
  Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
 Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.


thinking
**Reverifying phrases**

I need to go back and recheck the bad phrases again. There could be new issues that I need to be aware of. I'll also search for “as Verdier dual of \barB” to see what comes up related to that. It seems important to ensure I’m thorough in addressing any potential problems. Let’s explore those details closely to avoid missing anything crucial!
codex
The last two live overstatements are patched. I’m doing a final grep for those exact phrases plus a quick readback on the two new edits.
exec
/bin/zsh -lc "rg -n 'bar-cobar duality and holographic duality coincide|\\"'$'"\\\\cA\\"'^!'"\\"'$ as Verdier dual of '"\\\\barB\\(\\\\cA\\)|Verdier/linear duality|supplies the bulk field content|models the bulk field content|candidate bulk package: the Koszul dual' chapters --glob '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '1879,1883p'; nl -ba chapters/theory/introduction.tex | sed -n '2212,2215p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1879	Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
  1880	into the global geometry of curves, so factorization homology alone
  1881	controls the genus expansion. The $\beta\gamma$ system is therefore the
  1882	simplest object in which the boundary algebra, the Koszul-dual defect
  1883	sector, and the derived-center bulk are all explicitly computable.
  2212	 \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
  2213	Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
  2214	 $\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality; resolves circularity in defining the Koszul dual \\
  2215	Higher genus (Ch.~\ref{chap:higher-genus}) &
 exited 1 in 60ms:

file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index 179b335ff6db32ae029d5905213ff6b8b013f161..32f68d6b6583630d06ac1ccb670a3436706c04df
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -1879,7 +1879,8 @@
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
 controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which bar-cobar duality and holographic duality coincide.
+simplest object in which the boundary algebra, the Koszul-dual defect
+sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
 
 \section{From 3d \texorpdfstring{$\mathcal{N}=2$}{N=2} to the full chiral algebra}
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..789ce9acf5b68f150a665afd1b7486e6b1256a16
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2211,7 +2211,7 @@
 Bar-cobar adjunction (Ch.~\ref{chap:bar-cobar-adjunction}) &
  \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
 Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
- $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
+ $\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality; resolves circularity in defining the Koszul dual \\
 Higher genus (Ch.~\ref{chap:higher-genus}) &
  Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
 Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.

exec
/bin/zsh -lc 'git diff -- chapters/examples/free_fields.tex chapters/connections/thqg_introduction_supplement.tex chapters/theory/introduction.tex chapters/frame/preface.tex chapters/connections/editorial_constitution.tex chapters/examples/beta_gamma.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1068

diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10..4c68d02 100644
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@ at all genera.
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@ within the strong completion-tower framework
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index 179b335ff6db32ae029d5905213ff6b8b013f161..32f68d6b6583630d06ac1ccb670a3436706c04df
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -1879,7 +1879,8 @@
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
 controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which bar-cobar duality and holographic duality coincide.
+simplest object in which the boundary algebra, the Koszul-dual defect
+sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
 
 \section{From 3d \texorpdfstring{$\mathcal{N}=2$}{N=2} to the full chiral algebra}
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..789ce9acf5b68f150a665afd1b7486e6b1256a16
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2211,7 +2211,7 @@
 Bar-cobar adjunction (Ch.~\ref{chap:bar-cobar-adjunction}) &
  \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
 Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
- $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
+ $\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality; resolves circularity in defining the Koszul dual \\
 Higher genus (Ch.~\ref{chap:higher-genus}) &
  Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
 Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.




thinking
**Counting findings and edits**

I need to compute final line numbers for my findings, possibly using nl for relevant lines. I also want to include beta_gamma in my calculations. It might help to mention any problems in the preface and introduction. 

I can count up to eight findings:
1. free_fields.tex:2810
2. free_fields.tex:4950
3. thqg_introduction_supplement.tex:117
4. introduction.tex:2214
5. introduction.tex:2670 or 2671
6. preface.tex:483
7. editorial_constitution.tex:2014
8. beta_gamma.tex:1881/1882

I need to ensure the exact edits apply and gather precise line references too.
thinking
**Considering file links**

I think I need to decide if I should use file links in the final version. The developer wants clickable file links, so I’ll explore using markdown links with absolute paths and line numbers. This could enhance accessibility and make it easier for users to navigate. It seems like a good opportunity to improve the overall usability of the document. I'll have to ensure that the links are correctly formatted for clarity.
thinking
**Updating verification process**

I need to list the problem and exact edit clearly as the user explicitly requested a file with line numbers. It might be helpful to use bullet points. I should also consider mentioning that I removed bad phrases with grep, and clarify that I won't run the TeX build unless necessary. Some verification with grep seems essential, so I'll definitely include that. I'll also update the plan to reflect that this has been completed.
Plan update
The live in-scope conflations were patched and the old bad phrases were re-grepped out of the edited surface.
  ✓ Search Vol I for in-scope paragraphs mentioning bar with Koszul dual or derived center
  ✓ Read each candidate in context and classify clean vs conflated using the five-object template
  ✓ Patch only conflated paragraphs with minimal truthful wording fixes
  ✓ Run targeted grep verification for forbidden conflations on edited files
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index 179b335ff6db32ae029d5905213ff6b8b013f161..32f68d6b6583630d06ac1ccb670a3436706c04df
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -1879,7 +1879,8 @@
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
 controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which bar-cobar duality and holographic duality coincide.
+simplest object in which the boundary algebra, the Koszul-dual defect
+sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
 
 \section{From 3d \texorpdfstring{$\mathcal{N}=2$}{N=2} to the full chiral algebra}
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..789ce9acf5b68f150a665afd1b7486e6b1256a16
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2211,7 +2211,7 @@
 Bar-cobar adjunction (Ch.~\ref{chap:bar-cobar-adjunction}) &
  \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
 Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
- $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
+ $\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality; resolves circularity in defining the Koszul dual \\
 Higher genus (Ch.~\ref{chap:higher-genus}) &
  Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
 Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.


thinking
**Ensuring final clarity**

I need to make sure my final output is between 50 to 70 lines, which seems manageable. I think having 8 bullet points plus a short verification section would work nicely. It might be a good idea to order my findings by severity, which could help highlight the most critical issues. I'm curious how to best present this information for maximum clarity and impact. Let's keep refining this until it's just right!
codex
**Findings**
- PROBLEM at [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:4950): the conjecture identified the Koszul dual `\cA^!` with the bulk package. EXACT edit applied: `between \cA and a candidate holographic package: the derived center \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) supplies the bulk observable algebra, the Koszul dual \cA^! supplies the line/defect sector, and the bar-cobar filtration degree maps to the radial coordinate.`

- PROBLEM at [chapters/connections/editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:2014): the AdS/CFT conjecture said `\cA^!` models bulk field content while also naming the derived centre as the bulk observables. EXACT edit applied: changed `\cA^!$ models the bulk field content` to `\cA^!$ models the line/defect sector`.

- PROBLEM at [chapters/frame/preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:483): the ordered bar was described as the boundary-to-bulk map, and bulk reconstruction was framed as an upgrade of bar-cobar inversion. EXACT edit applied: replaced that passage with `\barB^{\mathrm{ord}}(\cA)` as `the boundary-side coalgebraic resolution feeding the boundary-to-bulk story`, then stated that the derived centre `is computed from Hochschild cochains using that resolution` and that Volume II adds `the separate bulk reconstruction through the derived centre`.

- PROBLEM at [chapters/examples/beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1881): the slogan `bar-cobar duality and holographic duality coincide` erased the boundary/defect/bulk distinction. EXACT edit applied: replaced it with `the boundary algebra, the Koszul-dual defect sector, and the derived-center bulk are all explicitly computable.`

- PROBLEM at [chapters/connections/thqg_introduction_supplement.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement.tex:117): the strict Koszul dual was described as coming from `Verdier/linear duality`, blurring `\cA^!` with `\cA^!_\infty`. EXACT edit applied: `\cA^! = (H^*(\barB_X(\cA)))^\vee` is now the `strict Koszul dual chiral algebra`, built from `bar cohomology and then linear duality`, and the next sentence now separately says `\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)` is the `homotopy Koszul-dual factorization algebra`.

- PROBLEM at [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:2810): the Heisenberg summary used the same `Verdier/linear duality` collapse. EXACT edit applied: replaced it with `The second arrow is linear duality on that coalgebra, producing the strict Koszul dual algebra... The separate Verdier image \mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) is the homotopy Koszul-dual factorization algebra.`

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2213): the roadmap line equated strict `\cA^!` with the Verdier image of `\barB(\cA)`. EXACT edit applied: replaced it with `\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality`.

- PROBLEM at [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2670): the warning box listed only four objects and again merged linear duality with Verdier duality. EXACT edit applied: changed `Four objects.` to `Five objects.`, added `\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)` as the derived center, changed `\cA^!` to the `strict Koszul dual algebra`, and replaced `Verdier/linear duality` with `linear duality on bar cohomology, while \mathbb{D}_{\operatorname{Ran}}\barB(\cA) gives the homotopy Koszul-dual factorization algebra`.

Verification: repo-wide grep for the old bad phrases on `chapters/*.tex` came back clean after these edits. I did not run a TeX build.
file update:
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 28be34ce0ec049c6ac212afae3a1c1e2dce3577e..4c68d029f09375bdc6fed4039ed78930be26877d
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -2013,7 +2013,7 @@
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item The bar complex $\barB(\cA)$ classifies twisting morphisms
  (couplings between $\cA$ and $\cA^!$); the \emph{Koszul dual}
- $\cA^!$ models the bulk field content
+ $\cA^!$ models the line/defect sector
  \textup{(}Costello--Paquette \cite{CP2020}\textup{)}. The bulk
  \emph{observable} algebra is the derived centre
  $C^\bullet_{\mathrm{ch}}(\cA, \cA)$, not $\barB(\cA)$
diff --git a/chapters/connections/thqg_introduction_supplement.tex b/chapters/connections/thqg_introduction_supplement.tex
index aa8909d5368bb4f76f1ab7145652ce7f9e4990f1..cdeb45ac181312a95b1e46dd52c2b6d718674824
--- a/chapters/connections/thqg_introduction_supplement.tex
+++ b/chapters/connections/thqg_introduction_supplement.tex
@@ -114,9 +114,12 @@
 \begin{equation}\label{eq:supp-line-category-def}
 \mathcal{C}(\cA) \;:=\; \cA^!\text{-}\mathsf{mod}.
 \end{equation}
-Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the Koszul dual chiral
-algebra, constructed by first taking bar cohomology, then Verdier/linear
-duality. The module category $\cA^!\text{-}\mathsf{mod}$ is a
+Here $\cA^! = (H^*(\barB_X(\cA)))^\vee$ is the strict Koszul dual chiral
+algebra, constructed by first taking bar cohomology and then linear
+duality. Separately,
+$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$ is the homotopy
+Koszul-dual factorization algebra. The module category
+$\cA^!\text{-}\mathsf{mod}$ is a
 $\mathbb{C}$-linear dg category whose objects are $\cA^!$-modules
 (factorization modules on $\operatorname{Ran}(X)$) and whose morphisms
 are chain maps.
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index 179b335ff6db32ae029d5905213ff6b8b013f161..32f68d6b6583630d06ac1ccb670a3436706c04df
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -1879,7 +1879,8 @@
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
 controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which bar-cobar duality and holographic duality coincide.
+simplest object in which the boundary algebra, the Koszul-dual defect
+sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
 
 \section{From 3d \texorpdfstring{$\mathcal{N}=2$}{N=2} to the full chiral algebra}
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fff6dfc8ccf41749541667200469db0f6660c30b..a4d4d1d9f2650b81b850aad00e336484a4b101c6
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2807,8 +2807,11 @@
  along collision divisors in~$\overline{C}_n(X)$ produces the Koszul
  dual \emph{coalgebra}~$\mathrm{coLie}^{\mathrm{ch}}(V^*)$, a
  conilpotent factorization coalgebra on~$\mathrm{Ran}(X)$. The
- second arrow is Verdier/linear duality, producing the Koszul dual
- \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$. The cobar
+ second arrow is linear duality on that coalgebra, producing the
+ strict Koszul dual \emph{algebra}~$\mathrm{Sym}^{\mathrm{ch}}(V^*)$.
+ The separate Verdier image
+ $\mathbb{D}_{\operatorname{Ran}}\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)$
+ is the homotopy Koszul-dual factorization algebra. The cobar
  construction is \emph{not involved}: $\Omega(\bar{B}(\mathcal{H}_k))
  \simeq \mathcal{H}_k$ recovers the original algebra, not its dual
  (Theorem~\ref{thm:bar-cobar-inversion-qi}).
@@ -4946,9 +4949,10 @@
 \label{conj:bulk-boundary-correspondence}
 For a boundary chiral algebra $\cA$, the bar-cobar adjunction
 $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to a correspondence
-between $\cA$ and a candidate bulk package: the Koszul dual $\cA^!$
-supplies the bulk field content, and the bar-cobar filtration degree
-maps to the radial coordinate.
+between $\cA$ and a candidate holographic package: the derived center
+$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ supplies the bulk observable
+algebra, the Koszul dual $\cA^!$ supplies the line/defect sector, and
+the bar-cobar filtration degree maps to the radial coordinate.
 (Contributing to Conjecture~\ref{conj:master-bv-brst}.)
 \end{conjecture}
 
diff --git a/chapters/frame/preface.tex b/chapters/frame/preface.tex
index ce9870b68b86ef4855065a9a2d2d49ec59fb1d48..7a00ab59b8dd5b8f2bf6e89d5da2f0ca3248e280
--- a/chapters/frame/preface.tex
+++ b/chapters/frame/preface.tex
@@ -480,14 +480,16 @@
 $\{S_r\}_{r\ge 2}$ terminates when the obstruction
 hierarchy collapses to finitely many terms.
 
-The conjectural extension (Volume~II) identifies
-$\barB^{\mathrm{ord}}(\cA)$ as the boundary-to-bulk map: the
+The conjectural extension (Volume~II) uses
+$\barB^{\mathrm{ord}}(\cA)$ as the boundary-side coalgebraic
+resolution feeding the boundary-to-bulk story: the
 derived centre
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) =
 R\!\operatorname{Hom}_{\cA\otimes\cA^{\mathrm{op}}}(\cA,\cA)$
-reassembles the bulk from the coalgebraic shadow. Volume~I
-proves bar-cobar inversion; Volume~II would upgrade it to bulk
-reconstruction.
+is computed from Hochschild cochains using that resolution.
+Volume~I proves bar-cobar inversion and the bar-side input;
+Volume~II would add the separate bulk reconstruction through the
+derived centre.
 
 When~$\cA$ is chirally Koszul, $H^*(B(\cA))$ concentrates in bar
 degree~$1$, the bar-to-cobar spectral sequence collapses at~$E_2$,
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index ecdddd52306f01f8362552357f8d7bbf556f384a..789ce9acf5b68f150a665afd1b7486e6b1256a16
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -2211,7 +2211,7 @@
 Bar-cobar adjunction (Ch.~\ref{chap:bar-cobar-adjunction}) &
  \textbf{Theorem~B} (inversion on Koszul locus); curved $A_\infty$; coderived continuation \\
 Non-abelian Poincar\'e duality (Ch.~\ref{chap:NAP-koszul-derivation}) &
- $\cA^!$ as Verdier dual of $\barB(\cA)$; resolves circularity in defining Koszul dual \\
+ $\cA^!_\infty$ as Verdier image of $\barB(\cA)$; strict $\cA^!$ from bar-cohomology duality; resolves circularity in defining the Koszul dual \\
 Higher genus (Ch.~\ref{chap:higher-genus}) &
  Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
 Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
@@ -2667,8 +2667,8 @@
 
 The following distinctions are the most common sources of error:
 
-\smallskip\noindent\textbf{Four objects.}
-$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
+\smallskip\noindent\textbf{Five objects.}
+$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !\textasciigrave}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee$ is the strict Koszul dual algebra. $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the derived center. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by linear duality on bar cohomology, while $\mathbb{D}_{\operatorname{Ran}}\barB(\cA)$ gives the homotopy Koszul-dual factorization algebra.
 
 \smallskip\noindent\textbf{Grading.}
 Cohomological ($|d| = +1$) throughout. The bar complex uses desuspension: $s^{-1}$ lowers degree by~$1$.

tokens used
206,774
