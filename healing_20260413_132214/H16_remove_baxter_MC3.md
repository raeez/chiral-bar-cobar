# H16_remove_baxter_MC3 (758s)



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
session id: 019d86b7-3568-79a1-83d8-e1bb471dbdcc
--------
user
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.

CRITICAL SESSION CONTEXT (factor this in):
This session deployed 537+ Codex agents across 7 campaigns. The following has ALREADY been done:
- Theorems A-D, H: proof architecture rectified. Verdier convention fixed (Thm A), off-locus
  coderived proven independently (Thm B), curved C0 in D^co unconditional (Thm C0), genus-0
  separated + reflexivity from perfectness (Thm C1), center-to-bar lift proved (Thm C2),
  circularity broken with routing remark (Thm D).
- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
- Topologization: split into cohomological (proved KM) + chain-level (conjectural).
- Koszul equivs (vii)/(viii): scope narrowed to match proofs.
- SC-formality, depth gap, D^2=0, Gerstenhaber: platonic agents running (P11-P20).
- 48 new anti-patterns catalogued (AP186-AP224).
- Wave A: broken refs, hardcoded Parts, duplicate labels, status mismatches, proof-after-conj
  all fixed across Vol I and Vol II.
- New compute engines: critical level (72 tests), Verlinde polynomial (g=0..6),
  genus-2 decomposition, chiral bialgebra, tetrahedron, and 20+ more.
- Vol I ~2,719pp (29 commits this session), Vol II ~1,681pp (15 commits), Vol III ~319pp (19 commits).

READ the current state of files on disk — they reflect ALL the above work.
Your job: HEAL remaining wounds, provide ALTERNATIVE proofs, UPGRADE strength.

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


RESEARCH: Can the Baxter constraint be removed from MC3?

TARGET: chapters/examples/yangians_computations.tex (add Research Remark)

MC3 type-A thick generation is conditional on the Baxter constraint b = a - 1/2.

INVESTIGATE:
1. The Baxter constraint comes from the shifted prefundamental representations.
   Are there OTHER generating representations that don't need this constraint?
2. In the classical (non-shifted) setting: the fundamental representations generate
   without spectral constraints. Can the classical result be DEFORMED?
3. The completion extension is conditional on localising generation. Is this proved
   in the literature for the relevant categories?
4. For types B, C, D: what is the analogue of the Baxter constraint?

Write a Research Remark with the deformation approach and the type-BCD landscape.
mcp startup: no servers


thinking
**Planning for research tasks**

I think we should use an explorer sub-agent to find the target file and relevant theorem contexts. The worker might not be necessary, and I can use the explorer to inspect the codebase. Updating the plan could be helpful, especially if we're doing substantial work, and we should provide a longer plan after gathering sufficient context. 

I'll need to keep commentary frequent and consider using the apply_patch function for edits. Maybe I need to follow the Pre-Edit Verification Protocol for the theorem formula? I'll research to see if we need to touch on the theorem's status. I might need to add remarks with the formula Baxter constraint \(b=a-\frac12\) and verify literature, likely using primary sources. Searching arXiv or papers could help here too!
thinking
**Utilizing the explorer for codebase tasks**

Since the instructions prefer using the explorer for codebase questions, I should ask it precisely and trust the results. However, I still need to read files. For simple tasks, I can use exec_command directly to view files, but it's best to avoid manual searches. To understand the codebase better, I should use the explorer to locate the target file and relevant labels. A commentary update would be useful, so let's consider spawning the explorer for this purpose.
codex
I’m locking scope on `chapters/examples/yangians_computations.tex` and the MC3 Baxter-constraint surface, then I’ll read the required constitutional files and the live theorem context before drafting anything.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3673 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
 succeeded in 52ms:
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

collab spawn_agent(call_4JlVuU5ZM9luczpcyYSO4P9z, prompt="Inspect the codebase for the MC3 Baxter-constraint surface around chapters/examples/yangians_computations.tex. Find the …")
mcp startup: no servers
spawn_agent(call_4JlVuU5ZM9luczpcyYSO4P9z, prompt="Inspect the codebase for the MC3 Baxter-constraint surface around chapters/examples/yangians_computations.tex. Find the …") pending init:
  agent: 019d86b7-9047-7212-b3ab-43b64c84f299
exec
/bin/zsh -lc "sed -n '1,260p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\section{Coulomb branch algebras}
\label{sec:coulomb-branch}
% Regime I: Quadratic, $\Eone$-chiral (Convention~\ref{conv:regime-tags}).

The preceding sections established the Yangian $Y(\fg)$ as an
$\Eone$-chiral algebra and constructed its bar-cobar duality. This
section and those that follow serve as the computational verification
ground: every algebraic claim from the foundations is tested against
explicit calculations with specific rank, specific shift parameters,
and specific representation-theoretic data. The shifted Yangian isomorphisms with
Coulomb branch algebras (Braverman--Finkelberg--Nakajima), the
cohomological Hall algebra structures (Schiffmann--Vasserot,
Kontsevich--Soibelman), and the explicit bar complex computations for
$\mathfrak{sl}_2$ through $\mathfrak{sl}_4$ are the primary evidence
for the MC3 thick generation theorem and the DK ladder beyond the
evaluation locus.

Two organizational principles govern the exposition. First, every
computation is placed in the four-level hierarchy: gauge-theoretic
origin (level~C), algebraic/RTT presentation (level~A),
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
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "MC3" -n chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
15:for the MC3 thick generation theorem and the DK ladder beyond the
2094:MC3 packets for \emph{all types} simultaneously, since the root
2634:\begin{conjecture}[Sectorwise DK extension to the completed/coderived MC3 domain for all types;
2649:MC3 packets at all simple types, bypassing ordinary thick generation
2934:The generic-parameter condition suffices for the MC3 generation
3062:categorical lift together with the compact/completed MC3 comparison
3239:\index{MC3!Lemma L}
3276:component of the MC3 split
3310:\begin{remark}[Research remark: removing the Baxter constraint from MC3]
3312:\index{MC3!Baxter constraint!removal programme}
3368:MC3 is still part of the open packet rather than an imported theorem.
3475: recursive self-similarity connecting MC3 to classical partition theory.
3615:arguments in the MC3 programme, since compact generation requires
3758:packages~(i)--(iii) of the old MC3 list are resolved, but
3779:\begin{remark}[Computational evidence for the MC3 critical path]
3781:\index{MC3!computational evidence}
3797: $\dim(L^-_a)_{-2k} = p(k)$ connect MC3 to partition theory.
3842:\begin{remark}[Corrected MC3 open problem]
3844:\index{MC3!corrected open problem}
3928: former MC3 packages reduce to a single remaining
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3200,3385p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Under Koszul duality, $R(u) \mapsto R(u)^{-1}$
($E_1$~inversion,
Remark~\ref{rem:yangian-e1-inversion}).

\smallskip
Since every standard object of
$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$ lies in
$\widehat{D}(\operatorname{thick}\langle
\mathcal{G}_{\mathrm{Bax}}\rangle)$ by Steps~2--3, and every
object of~$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$ has a finite
filtration by standards (BGG), the image of
$D^b(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$ in the separated
completion is contained in the localizing subcategory generated by
$\mathcal{G}_{\mathrm{Bax}}$.

\smallskip\noindent\textit{Conditional completion extension.}
Assume now that $\mathcal{D}^{\mathrm{comp}}$ is a presentable stable
completed enhancement whose compact objects are the thick
idempotent-complete closure of the image of
$D^b(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$. Then the compact part of
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3385,3585p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
target: it attacks the spectral-normalization question and the
completion question at the same time.
\end{remark}

\begin{remark}[Genericity of prefundamental irreducibility at higher rank]
\label{rem:prefundamental-genericity-higher-rank}
\index{prefundamental module!genericity condition}
For $Y(\mathfrak{sl}_2)$, the negative prefundamental~$L^-(a)$
is irreducible for \emph{all} spectral parameters $a \in \mathbb{C}$
(Hern'andez--Jimbo~\cite{HJZ25}, Theorem~3.8).
For $Y(\mathfrak{sl}_N)$ with $N \ge 3$, irreducibility holds
for \emph{generic}~$a$, outside a countable, discrete subset
of~$\mathbb{C}$ where the Drinfeld polynomial of~$L^-_{i,a}$
satisfies special divisibility relations. The simple-root
$\lambda = 0$ Baxter calculation occurs on the hyperplane
$b = a - 1/2$, and the generic exact triangles used in the
type-$A$ generation argument are supplied on a cofinal family of
spectral parameters by
Remark~\ref{rem:baxter-exact-triangles-typeA}. The
Clebsch--Gordan decomposition holds for generic~$a, b$, regardless
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"MC3\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/lattice_foundations.tex:3961:(MC3 categorical CG closure and the generated-core DK comparison are
chapters/examples/lattice_foundations.tex:3997:(Conjecture~\ref{conj:master-dk-kl}); the underlying all-types MC3 core
chapters/examples/lattice_foundations.tex:4590:factorization DK (MC3, beyond the type~A evaluation-generated core which is now proved) to
chapters/examples/lattice_foundations.tex:4632:full DK/KL categorical equivalence (MC3 CG decomposition is proved on the evaluation-generated core for all
chapters/examples/yangians_drinfeld_kohno.tex:325:is the MC3 extension problem; the prefundamental Clebsch--Gordan
chapters/examples/yangians_drinfeld_kohno.tex:1002:\index{MC3!four-conjecture package!interaction with H-level}
chapters/examples/yangians_drinfeld_kohno.tex:1420:\textup{(}MC3, thick generation, DK-2/3\textup{)} converge.
chapters/examples/yangians_drinfeld_kohno.tex:1618:\emph{correct categorical context} for the remaining off-Koszul MC3
chapters/examples/yangians_drinfeld_kohno.tex:1741:unified $\infty$-categorical formulation of the four MC3
chapters/examples/yangians_drinfeld_kohno.tex:1746:\begin{conjecture}[Formal moduli reformulation of MC3;
chapters/examples/yangians_drinfeld_kohno.tex:1749:\index{MC3!formal moduli reformulation}
chapters/examples/yangians_drinfeld_kohno.tex:1750:\index{formal moduli problem!MC3}
chapters/examples/yangians_drinfeld_kohno.tex:1751:The four MC3 components (with the all-types categorical CG and
chapters/examples/yangians_drinfeld_kohno.tex:1814:\index{tangent Lie algebra!role in MC3 extension}
chapters/examples/yangians_drinfeld_kohno.tex:1819:conjectures beyond the proved MC3 evaluation-generated core can be organized over a common structural background,
chapters/examples/yangians_drinfeld_kohno.tex:1834:remaining MC3 packets. What it does \emph{not} by itself prove is
chapters/examples/yangians_drinfeld_kohno.tex:1842:separately identify how each remaining MC3 packet is encoded in
chapters/examples/yangians_drinfeld_kohno.tex:2181:also clarifies the bar-side setting for the remaining MC3 extension
chapters/examples/yangians_drinfeld_kohno.tex:2655:\item \emph{What MC3 gives.}
chapters/examples/yangians_drinfeld_kohno.tex:4746:Type~$A$ does not close MC3 here:
codex
I’ve loaded the constitutional surface and the target file. Next I’m isolating the MC3 locus, reading the research-synthesis workflow, and checking whether the Baxter discussion already propagates elsewhere.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/frontier-research/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "MC3|Baxter|prefundamental|thick generation|localising generation|localizing generation|type A|type B|type C|type D" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/connections/editorial_constitution.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: frontier-research
description: Use for new theorem architecture, research synthesis, or frontier programme design. Keep work local by default. Delegate or swarm only when the user explicitly authorizes it. This is the Codex-native equivalent of the frontier and research-swarm workflows from `CLAUDE.md`.
---

# Frontier Research

Frontier work is allowed only after the proved core, the conditional bridge, and the conjectural extension are separated sharply.

## Workflow

1. Partition the topic into:
   proved core,
   compute-backed evidence,
   conditional bridge,
   conjectural extension,
   heuristic picture.
2. Read the live theorem surface before synthesizing new structure.
3. Name the exact blocker for every missing implication.
4. Prefer the strongest narrower programme statement that survives hostile rereading.
 succeeded in 51ms:
Total output lines: 488

chapters/examples/yangians_foundations.tex:117:\fi constrains the MC3 categorical lift:
chapters/examples/yangians_foundations.tex:118:the all-types MC3 core is proved
chapters/examples/yangians_foundations.tex:120:prefundamental Clebsch--Gordan closure via multiplicity-free
chapters/examples/yangians_foundations.tex:176:The \emph{RTT presentation} (Yang--Baxter presentation) of
chapters/examples/yangians_foundations.tex:269:In all four cases, the Yang--Baxter equation
chapters/examples/yangians_foundations.tex:297:The Yang--Baxter equation is verified by expanding
chapters/examples/yangians_foundations.tex:380:is $R$-matrix-valued, with simple poles. The $R$-matrix $R(u) = 1 + \hbar r/u + O(u^{-2})$ provides the braiding: $\sigma_{12} \circ \mu = R_{12} \cdot \mu \circ \sigma_{12}$, which is the $\Eone$-locality axiom. Associativity follows from the Yang--Baxter equation $R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12}$.
chapters/examples/yangians_foundations.tex:558:The RTT algebra for $R^{-1}(u)$ is isomorphic to the RTT algebra for $R(u)$ with $\hbar \to -\hbar$. To see this, note that $R^{-1}(u; \hbar) = 1 + \hbar P/u + O(u^{-2})$ agrees with $R(u; -\hbar) = 1 + \hbar P/u$ at leading order in $1/u$; the higher-order terms $\hbar^{2k}/u^{2k}$ and $\hbar^{2k+1}P/u^{2k+1}$ in $R^{-1}$ do \emph{not} appear in $R(u;-\hbar)$, but they are irrelevant: the mode expansion~\eqref{eq:rtt-modes} extracts only the leading-order data, and the higher-order terms are automatic consequences of the quadratic RTT relation via the Yang--Baxter equation. Therefore $Y(\mathfrak{sl}_2)^! \cong Y(\mathfrak{sl}_2)^{\hbar \to -\hbar}$: the Koszul dual is the same algebra with reversed deformation parameter. For simply-laced~$\fg$, this is conjecturally isomorphic to $Y(\fg)$ after a spectral parameter shift $u \mapsto u + 1$ \textup{(}Conjecture~\textup{\ref{conj:yangian-spectral-selfdual}}\textup{)}.
chapters/examples/yangians_foundations.tex:791:\label{rem:prefundamental-koszul-extension}
chapters/examples/yangians_foundations.tex:792:\index{prefundamental module!Koszul dual}
chapters/examples/yangians_foundations.tex:795:prefundamental~$L^-(b)$
chapters/examples/yangians_foundations.tex:798:Koszul dual is the positive prefundamental~$L^+(b')$ with Drinfeld
chapters/examples/yangians_foundations.tex:800:pole~$1/(u - b)$ of~$L^-$). The prefundamental Clebsch--Gordan
chapters/examples/yangians_foundations.tex:802:(Theorem~\ref{thm:shifted-prefundamental-generation},
chapters/examples/yangians_foundations.tex:804:preserves the prefundamental class, so any eventual Koszul-duality
chapters/examples/yangians_foundations.tex:807:prefundamental-duality statement.
chapters/examples/yangians_foundations.tex:812:\index{tensor ideal!prefundamental}%
chapters/examples/yangians_foundations.tex:814:The prefundamental Clebsch--Gordan
exec
/bin/zsh -lc "sed -n '520,860p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '260,520p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
commutation relation:
\begin{align}
d\bigl([t_{ij}^{(r)} | t_{kl}^{(s)}] \otimes \eta_{12}\bigr)
&= \Res_{u = v}\left[
\frac{R_{12}(u-v)_{ij,kl} - \delta_{ij}\delta_{kl}}{u-v}
\right]_{r,s} \label{eq:yangian-bar-d2}
\end{align}
The $R$-matrix $R(u) = 1 - P/u$ gives:
\[
\frac{R(u)_{ij,kl} - \delta_{ij}\delta_{kl}}{u}
= -\frac{\delta_{il}\delta_{kj}}{u^2}
\quad (\text{the permutation term})
\]
The residue at $u = v$ extracts the $1/(u-v)$ coefficient:
\begin{align}
d([t_{ij}^{(r)} | t_{kl}^{(s)}]) &=
-t_{il}^{(r+s-1)} \delta_{kj} + t_{kj}^{(r+s-1)} \delta_{il}
\label{eq:yangian-d2-explicit}
\end{align}
(the RTT relation at the level of generating functions).
 succeeded in 51ms:
The degree-2 cohomology satisfies $\dim H^2 = 3 \dim H^2(\mathfrak{sl}_2)$
at each filtration level, reflecting the rank-2 structure.
\end{computation}

\begin{proposition}[Rank dependence of Yangian bar complex; \ClaimStatusProvedHere]
\label{prop:yangian-rank-dependence}
\index{Yangian!bar complex!rank dependence}

For the Yangian $Y(\mathfrak{sl}_N)$ at filtration degree $\leq 1$:
\begin{enumerate}
\item $\dim \bar{B}^1 = N^2 - 1$ (the dimension of $\mathfrak{sl}_N$,
after removing the trace condition $\sum_i t_{ii}^{(r)} = 0$).
\item $\dim \bar{B}^2 = (N^2-1)^2$ (all pairs of generators).
\item $\dim H^2 = \dim \mathfrak{sl}_N \otimes \mathfrak{sl}_N / \mathrm{Im}(d_2)
= (N^2-1)^2 - \binom{N^2-1}{2} + \dim(\mathrm{Serre})$,
where $\mathrm{Serre}$ denotes the Serre relation space.
\item The growth rate is polynomial in $N$: $\dim \bar{B}^n = O(N^{2n})$.
\end{enumerate}
\end{proposition}


thinking
**Collecting MC3 Baxter constraint references**

I'm gathering key theorem and remark labels near line 3310 in yangians_computations.tex related to the MC3 Baxter-constraint surface, focusing on terms like thick generation and shifted prefundamental representations. I'll identify concise cross-references and duplicates across volumes I–III, summarizing relevant file paths, label names, and context snippets that mention thick generation, prefundamental generation, and Baxter constraint removal. I'll also search broadly for occurrences of "shifted-prefundamental" to find repeated discussions elsewhere in the codebase.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "shifted-prefundamental" -n' in /Users/raeez/chiral-bar-cobar succeeded in 84ms:
compute/tests/test_shifted_prefundamental_sl2.py:3:Fills the computational gap for conj:shifted-prefundamental-generation.
compute/tests/test_prefundamental_cg_closure.py:4:the MC3 critical path (conj:shifted-prefundamental-generation).

codex
The MC3 locus is larger than a single theorem: the file already separates the evaluation-core proof from the shifted-prefundamental completion packet. I’m reading the exact open-problem lane now so the new remark lands next to the real blocker, not the historical one.
thinking
**Identifying cross references across volumes**

I’m focusing on finding and highlighting cross references and duplicate mentions like “thick generation,” “shifted prefund,” and the “Baxter constraint” across multiple volumes. I’ll check specific files and line ranges to collect these references and prepare a final summary that points to their contexts.
exec
/bin/zsh -lc "sed -n '1360,1710p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2280,2685p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2820,3665p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Remark~\ref{rem:yangian-status}. Extending to
the \emph{full} Yangian category~$\mathcal{O}$ (which
includes infinite-dimensional highest-weight modules,
Verma modules $M(\lambda, a)$, and their subquotients) requires
the Koszulness conjecture
\textup{(}Remark~\ref{rem:yangian-collapse-conj}\textup{)}.
Even if $Y(\mathfrak{g})$ is Koszul, however, one still needs a
separate ambient extension theorem realizing the larger bar-comodule
comparison on the $Y_{-\hbar}$ module surface and respecting the
highest-weight structures of category~$\mathcal{O}$. The remaining
step is therefore not a new local computation on evaluation modules,
but it is more than generation alone.
\end{remark}

\begin{proposition}[DK-2 reduction to thick generation, conditional on an ambient exact extension;
\ClaimStatusProvedHere]
\label{prop:yangian-dk2-thick-generation}
Let
\[
\mathcal{D}_{\hbar}^{\mathrm{eval}}
 succeeded in 52ms:
$P(\lambda) \in \mathcal{C}_{\mathrm{eval}}$. Since $\mathcal{O}$
has finite global dimension, every object $M \in \mathcal{O}$ admits
a finite projective resolution. Each projective term lies in
$\mathcal{C}_{\mathrm{eval}}$, so $M \in
\mathcal{C}_{\mathrm{eval}}$ by iterated cones. Every object of
$D^b(\mathcal{O})$ is a bounded complex of objects of
$\mathcal{O}$, hence lies in $\mathcal{C}_{\mathrm{eval}}$.
\end{proof}

\begin{remark}[Kazhdan--Lusztig input for Yangian
category~\texorpdfstring{$\mathcal{O}$}{O}]
\label{rem:kl-input-yangian}
\index{Kazhdan--Lusztig!Yangian thick generation}
For $Y_\hbar(\mathfrak{sl}_N)$,
Proposition~\ref{prop:thick-gen-projective} reduces thick generation
to two inputs:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Finite global dimension.}
 For truncated shifted Yangians, this follows from the
 Brundan--Kleshchev equivalence \cite{BrunKlesh06} with parabolic
 succeeded in 52ms:
\eqref{eq:eval-core} identifies $D^b(\operatorname{Rep}_{\mathrm{fd}})$
with the thick closure of that subcategory, the same exactness and
thick-closure argument extends the equivalence to all of
$D^b(\operatorname{Rep}_{\mathrm{fd}})$. Strong monoidality then
extends from the evaluation-generated subcategory to the full thick
closure by Lemma~\ref{lem:monoidal-thick-extension}.
\end{proof}

\subsubsection*{Beyond finite dimensions: the shifted-prefundamental package}

\begin{theorem}[Baxter exact triangles on
\texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly};
\ClaimStatusProvedHere]
\label{thm:baxter-exact-triangles-opoly}
\index{Baxter relation!exact triangle lift|textbf}
\index{shifted Yangian!Baxter exact triangles}
For $\fg = \mathfrak{sl}_2$ and generic spectral parameters,
the three-term TQ relations of Zhang~\cite{Zhang24} lift from
$K_0(\mathcal{O})$ to
$Y(\mathfrak{sl}_2)$-equivariant short exact sequences
exec
/bin/zsh -lc "sed -n '3740,4315p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Baxter constraint"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
shifted-prefundamental generation and completion input beyond the
type-$A$ surface.
\end{remark}

\begin{conjecture}[DK on compacts and completion extension; \ClaimStatusConjectured]
\label{conj:dk-compacts-completion}
\index{Drinfeld--Kohno!derived!compact extension}
\index{Francis--Gaitsgory!pro-nilpotent completion}
The bar-cobar Koszul duality equivalence
$\Phi$~\eqref{eq:dk-eval-core} extends from the finite-dimensional
evaluation core to the full completed shifted-prefundamental core
$\mathcal{G}_{\mathrm{shift}}$, and then by pro-nilpotent completion
in the sense of Francis--Gaitsgory to the completed Yangian category.
\end{conjecture}

\begin{remark}[Type-A status of DK on compacts]
\label{rem:dk-compacts-completion-typeA}
In type~$A$ ($\mathfrak{sl}_N$ for all $N \geq 2$),
packages~(i)--(iii) of the old MC3 list are resolved, but
Conjecture~\ref{conj:dk-compacts-completion} remains the final
 succeeded in 51ms:
Total output lines: 292

healing_20260413_132214/H06_MC2_alt_proof.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H09_koszul_equivs_alt.md:34:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
scripts/healing_fortification_40.py:40:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
scripts/healing_fortification_40.py:408:agent("H16_remove_baxter_MC3", """RESEARCH: Can the Baxter constraint be removed from MC3?
scripts/healing_fortification_40.py:412:MC3 type-A thick generation is conditional on the Baxter constraint b = a - 1/2.
scripts/healing_fortification_40.py:415:1. The Baxter constraint comes from the shifted prefundamental representations.
scripts/healing_fortification_40.py:421:4. For types B, C, D: what is the analogue of the Baxter constraint?
healing_20260413_132214/H05_thm_H_alt_proof.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H05_thm_H_alt_proof.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 176848)
healing_20260413_132214/H14_remove_koszul_locus.md:40:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H03_thm_C_alt_proof.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H10_depth_gap_alt.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H01_thm_A_alt_proof.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H07_MC5_alt_approach.md:46:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H15_remove_chain_level_topol.md:40:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H02_thm_B_alt_proof.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H04_thm_D_alt_proof.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H08_topol_alt_proof.md:34:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2090,2185p' chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item specializing $z = q^h$ for a quantum parameter~$q$ and
 conformal weight~$h$ (the Kazhdan--Lusztig approach,
 Theorem~\ref{thm:kazhdan-lusztig-equivalence}); or
\item taking the monodromy representation of the KZ connection
 around the singularity (the Drinfeld--Kohno approach,
 Theorem~\ref{thm:derived-dk-affine}).
\end{enumerate}
On those affine comparison surfaces, both approaches produce the same
genuine braided tensor category on the corresponding comparison core,
identified with the appropriate quantum-group side by the
Kazhdan--Lusztig / Drinfeld--Kohno package.
\end{remark}


\subsubsection{Thick generation and MC3}

\begin{theorem}[Type-$A$ MC3 reduction via the gravitational Yangian;
\ClaimStatusProvedHere]
\label{thm:thqg-V-mc3-thick-generation}
\index{MC3!thick generation!gravitational Yangian}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2008,2035p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The monograph is organized in three concentric rings.

\subsection*{Ring~1: The proved modular Koszul core}
Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
\textup{(}analytic HS-sewing at all genera, genus-$0$ algebraic
BRST/bar, $D^{\mathrm{co}}$-level BV=bar for all shadow classes;
chain-level BV/BRST/bar conjectural\textup{)},
MC3 \textup{(}evaluation core all types unconditional; categorical
CG all types unconditional; type-$A$ post-core reduction proved on the
Baxter-locus seed, with residual compact-completion DK-4/5 downstream
of the Baxter constraint and Conjecture~\ref{conj:dk-compacts-completion}\textup{)},
DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
and the Koszulness characterization programme
(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
factorization-homology criterion; 1 proved consequence,
1 conditional, 1 one-directional;
Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
appendices touches it except to cross-reference from it.


exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "rem:mc3-baxter-constraint-removal" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/yangians_computations.tex:3311:\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:22:For the Baxter-constraint removal programme recorded in `rem:mc3-baxter-constraint-removal`:
healing_20260413_130533/H16_remove_baxter_MC3.md:1187:/bin/zsh -lc "rg -n \"label\\{rem:mc3-baxter-constraint-removal\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 67ms:
healing_20260413_130533/H16_remove_baxter_MC3.md:1193:label: \label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1220:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1313:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1406:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1498:/bin/zsh -lc "rg -n \"label\\{rem:mc3-baxter-constraint-removal\\}|Research remark: removing the Baxter constraint from MC3|likely|present evidence|landscape|notably|additionally|moreover|furthermore|remarkably|interestingly|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate\" chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_130533/H16_remove_baxter_MC3.md:1521:3311:\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1526:/bin/zsh -lc "rg -n \"label\\{rem:mc3-baxter-constraint-removal\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
healing_20260413_130533/H16_remove_baxter_MC3.md:1527:/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3311:\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1538:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1661:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1753:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1851:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:1948:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:2066:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:2169:\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:2197:+\label{rem:mc3-baxter-constraint-removal}
healing_20260413_130533/H16_remove_baxter_MC3.md:2218:+\label{rem:mc3-baxter-constraint-removal}

thinking
**Reviewing research remarks**

It looks like we've already made a remark about removing the Baxter constraint from MC3. The user is asking for a research remark that includes the deformation approach and type-BCD landscape, which makes me double-check if we fully addressed their request. I need to confirm that our current work on the disk reflects these points. It might be necessary to enhance it with literature references and more precise claims, especially regarding category \(O\) and the asymptotic modules. I'll explore the current literature to see if we can strengthen the remark.
thinking
**Exploring literature on Yangians**

I should take a closer look at the theorem `thm:yangian-generic-boundary-fibers` later on. First, I need to find relevant primary sources, like those related to shifted prefundamental representations. HJZ25 might refer to the publication by Hernandez, Jimbo, and Zhang, so I should track down the actual paper. Additionally, I need to investigate the Baxter–Rees family and gather specific literature about shifted Yangians, asymptotic modules, and category \(O\). I plan to search both online and in local bibliographies for references to Zhang24 and others, and I might find useful notes in the current repository.
collab wait(call_NUcfCHzHPS0LLscrwao8BzSM)
  receivers: 019d86b7-9047-7212-b3ab-43b64c84f299
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "conj:dk-compacts-completion" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 669

metadata/dependency_graph.dot:1837:  conj_dk_compacts_completion [label="conj:dk-compacts-completion\nconjecture [Co]\nDK on compacts and completion extension", style=filled, fillcolor="#fff9c4"];
metadata/label_index.json:2310:  "conj:dk-compacts-completion": {
metadata/claims.jsonl:758:{"label": "thm:thqg-V-mc3-thick-generation", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/thqg_gravitational_yangian.tex", "line": 2108, "title": "Type-$A$ MC3 reduction via the gravitational Yangian", "labels_in_block": ["thm:thqg-V-mc3-thick-generation", "eq:thqg-V-mc3-generation"], "refs_in_block": ["cor:dk23-all-types", "thm:mc3-type-a-resolution", "conj:dk-compacts-completion"]}
metadata/claims.jsonl:759:{"label": "cor:thqg-V-dk5-type-a", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/thqg_gravitational_yangian.tex", "line": 2147, "title": "Type-$A$ DK-5 reduction to the compact-completion packet", "refs_in_block": ["conj:dk-compacts-completion"]}
metadata/claims.jsonl:1772:{"label": "conj:dk-compacts-completion", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/yangians_computations.tex", "line": 3666, "title": "DK on compacts and completion extension", "refs_in_block": ["eq:dk-eval-core"]}
metadata/claims.jsonl:1773:{"label": "thm:mc3-type-a-resolution", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/yangians_computations.tex", "line": 3894, "title": "Type-$A$ MC3 reduction to the compact-completion packet", "refs_in_block": ["prop:prefundamental-clebsch-gordan", "thm:shifted-prefundamental-generation", "conj:dk-compacts-completion"]}
metadata/claims.jsonl:1808:{"label": "conj:mc3-formal-moduli-reformulation", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 1748, "title": "Formal moduli reformulation of MC3", "refs_in_block": ["thm:baxter-exact-triangles", "thm:shifted-prefundamental-generation", "thm:pro-weyl-recovery", "conj:dk-compacts-completion"]}
audit_campaign_20260412_231034/T12_MC5_BV_bar.md:171:archive/raeeznotes/raeeznotes100/red_team_summary.md:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
relaunch_20260413_111534/R19_coderived_models.md:492:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
wave2_audit_20260413_001942/F20_status_audit.md:1255:Conjecture~\ref{conj:dk-compacts-completion}) is downstream of MC3.
wave2_audit_20260413_001942/F20_status_audit.md:1589:chapters/connections/thqg_gravitational_yangian.tex|2108|theorem|thm:thqg-V-mc3-thick-generation|conj:dk-compacts-completion|Conjectured
wave2_audit_20260413_001942/F20_status_audit.md:1590:chapters/connections/thqg_gravitational_yangian.tex|2147|corollary|cor:thqg-V-dk5-type-a|conj:dk-compacts-completion|Conjectured
wave2_audit_20260413_001942/F20_status_audit.md:1592:chapters/examples/yangians_computations.tex|3761|theorem|thm:mc3-type-a-resolution|conj:dk-compacts-completion|Conjectured
audit_campaign_20260412_231034/T07_thm_H.md:161:archive/raeeznotes/raeeznotes100/red_team_summary.md:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
audit_campaign_20260412_231034/T08_MC1_PBW.md:360:Conjecture~\ref{conj:dk-compacts-completion}) is
audit_campaign_20260412_231034/T08_MC1_PBW.md:590:Conjecture~\ref{conj:dk-compacts-completion}) is
audit_campaign_20260412_231034/T08_MC1_PBW.md:650:   169	Conjecture~\ref{conj:dk-compacts-completion}) is
audit_campaign_20260412_231034/T10_MC3_thickgen.md:1022:  1015	(Conjecture~\ref{conj:dk-compacts-completion}))
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "conj:dk-compacts-completion" chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
169:Conjecture~\ref{conj:dk-compacts-completion}) is
520:Conjecture~\ref{conj:dk-compacts-completion}) is downstream of MC3.
808: (Conj.~\ref{conj:dk-compacts-completion}).
849:extension, Conjecture~\ref{conj:dk-compacts-completion}) is
1062:$\to$\ref{conj:dk-compacts-completion})
1111: is Conjecture~\ref{conj:dk-compacts-completion}: extending the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '780,840p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$Q(\cA)$, the primitive generating series $G_\cA(t)$, the
completion Hilbert series $H_\cA(t)$, and the completion entropy
$h_K(\cA)$) provide numerical invariants of the completed theory
that are independent of curvature and OPE data
(\S\ref{subsec:completion-kinematics-programme} of the concordance).
\end{remark}

\begin{remark}[Local conjecture dependencies]\label{rem:conjecture-dependencies}
\index{conjectures!dependency map}
The individual conjectures in earlier chapters reduce to the
master package. Each local conjecture carries a parenthetical
annotation identifying its master parent.
\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{@{}llp{6.8cm}@{}}
\toprule
\textbf{MC} & \textbf{Status} & \textbf{Scope} \\
\midrule
MC1 & \textbf{Proved} (Thm~\ref{thm:master-pbw})
 & PBW concentration for KM, Vir, principal $\mathcal{W}_N$. \\
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Lemma~L" -n' in /Users/raeez/chiral-bar-cobar succeeded in 86ms:
Total output lines: 402

metadata/dependency_graph.dot:1831:  conj_rank_independence_step2 [label="conj:rank-independence-step2\nconjecture [Co]\nLift-and-lower \textup{(}Lemma~L\textup{...", style=filled, fillcolor="#fff9c4"];
rectification_20260412_233715/R07_yangians_computations.md:267:  3146	\begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:1050:  4009	 \textup{(}Lemma~L, lift-and-lower\textup{)} for all other simple
rectification_20260412_233715/R07_yangians_computations.md:1056:  4015	Lemma~L outside type~$A$\textup{)}, pro-Weyl recovery, and the
rectification_20260412_233715/R07_yangians_computations.md:1207:  3185	in the derived shifted category. Pending Lemma~L, the layer~3
rectification_20260412_233715/R07_yangians_computations.md:1513: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:1652: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:1673:in the derived shifted category. Pending Lemma~L, the layer~3
rectification_20260412_233715/R07_yangians_computations.md:1902: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:2064: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:2221: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:2237:in the derived shifted category. Pending Lemma~L, the layer~3
rectification_20260412_233715/R07_yangians_computations.md:2455: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:2597: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:2749: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:2893: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:3051: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:3216: \begin{conjecture}[Lift-and-lower \textup{(}Lemma~L\textup{)};
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "three-layer split" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Summarizing cross references and key statements**

I'm gathering main references from the `yangians_computations.tex` file with line ranges and key theorems, then linking these to related statements in `thqg_gravitational_yangian.tex`, `editorial_constitution.tex`, and `concordance.tex`. I’ll note research remarks like the Baxter constraint removal and clarify which volumes include these discussions to give a clear, concise bullet list for the user.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1865,1905p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 obstruction tower) are the constructive content.
 MC1 (PBW concentration) holds unconditionally for universal
 algebras $V_k(\fg)$, $\mathrm{Vir}_c$, $\mathcal{W}^k(\fg)$
 (Proposition~\ref{prop:pbw-universality}). For simple quotients
 $L_k(\fg)$ at admissible levels, PBW concentration fails at
 $\mathrm{rk}(\fg) \geq 2$ with denominator $q \geq 3$: the
 abelian Cartan subalgebra contributes $\mathrm{rk}(\fg)$ classes
 to $H^2(\barB)$
 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}).
\item \emph{MC3}: MC3 is \textbf{proved} for all simple types on the
evaluation-generated core. The categorical CG decomposition is proved via
multiplicity-free $\ell$-weights
\textup{(}Theorem~\ref{thm:categorical-cg-all-types}\textup{)}, and
the DK comparison on the
evaluation-generated core is proved
\textup{(}Corollary~\ref{cor:dk23-all-types}\textup{)}. Type~$A$
further reduces the old four-packet post-core problem to the single
compact-completion packet
\textup{(}Theorem~\ref{thm:mc3-type-a-resolution}\textup{)}:
shifted-prefundamental generation and pro-Weyl recovery are proved on
wait(call_NUcfCHzHPS0LLscrwao8BzSM) timed out:

thinking
**Summarizing MC3 Baxter references**

I'll organize the key theorem and remark labels around thick generation, shifted prefundamental representations, and Baxter constraints found in multiple files, clearly citing line ranges and cross-references to keep the context tight and highlight relevant duplicated discussions across Volumes I–III.

thinking
**Checking references and options**

I’m thinking the explorer tool timed out, and it might still be running, so I’ll poll later. In the meantime, I'll consider using a web search. I also need to inspect local references in the bibliography for the cited works. I’ll search the bibliography entries for things like HJZ25, Zhang24, GTL17, HerNeg24, and Hernandez05. Using rg could help with that!
codex
**MC3 Baxter surface**
- `chapters/examples/yangians_computations.tex:3068-3335` — `thm:shifted-prefundamental-generation` proves that every standard of `\mathcal{O}^{\mathrm{sh}}_{\leq 0}` lies in the thick idempotent-complete closure of the Baxter seed `\{V_{\omega_i}(a)\}\cup\{L^-_{i,a-\frac{1}{2}}\}`; Step 2 keeps the Baxter hyperplane `b=a-\tfrac{1}{2}` plus prefundamental Clebsch–Gordan input intact, so the shifted prefundamental family generates the shifted envelope and, by compact-generation hypotheses, the desired completed Yangian subcategory. `conj:rank-independence-step2` and `rem:lemma-L-status` immediately afterward explain that the only remaining obstacle to propagating this shifted-prefundamental generation beyond type A is the lift-and-lower (Lemma L) filtration needed to upgrade the `\ell`-weight multiplicity‑free decomposition to the derived shifted category. `rem:shifted-prefundamental-generation-typeA` emphasizes the bijective reparametrization `a \mapsto a-\tfrac{1}{2}` on the Baxter locus, and `rem:prefundamental-genericity-higher-rank` records the genericity needed for the prefundamental irreducibility input.
- `chapters/examples/yangians_computations.tex:3310-3477` — `rem:mc3-baxter-constraint-removal` is the research remark the user asked to inspect: it isolates the Baxter locus as a `b=a-\tfrac{1}{2}` constraint, spells out why neither the proof mechanism nor the current asymptotic/Baxter–Rees deformation supplies a replacement for the Baxter singular vector off that hyperplane, and outlines the envisioned deformation route (generic asymptotic fibers specializing to negative prefundamentals) plus the remaining compact/localizing hypotheses (`conj:dk-compacts-completion`) that keep the completion packet open.

**Cross references / duplicate cases**
- `chapters/connections/thqg_gravitational_yangian.tex:2106-2173` — `thm:thqg-V-mc3-thick-generation` reuses `thm:mc3-type-a-resolution` to assert that the gravitational Yangian’s evaluation-generated core is thick‑generated by evaluation modules, that shifted prefundamental generation and pro-Weyl recovery reduce the MC3 chain to the single compact/completion packet, and that only `conj:dk-compacts-completion` remains unresolved. The adjoining `cor:thqg-V-dk5-type-a` records the same DK-5 reduction, and `rem:thqg-V-mc3-arbitrary-type` reiterates the all‑types CG core plus the conditional lift of the post-core packets (the same Lemma L story).
- `chapters/connections/concordance.tex:1865-1903` — the concordance recapitulates MC3 as “proved for all simple types on the evaluation-generated core (prefundamental CG + DK-2/3)”, notes that type A reduces the old four MC3 packets to the Baxter-locus shifted-prefundamental generation and pro-Weyl recovery (`thm:mc3-type-a-resolution`), highlights the spectral constraint supplied by `prop:baxter-yangian-equivariance`, and flags `conj:dk-compacts-completion` as the downstream DK-4/5 extension/completion. This is the same thick-generation/shifted-prefundamental narrative as the target section.
- `chapters/connections/editorial_constitution.tex:806-828` — the constitutional remark list restates MC3’s status (evaluation core proved, type A post-core reduction proved on the Baxter seed, compact/completed extension still open) and explicitly points to `conj:dk-compacts-completion` as the remaining type‑A packet, thereby duplicating the Baxter-constrained story at the high-level editorial summary.
codex
I found that the file already contains a first-pass research remark on this exact question. I’m treating that as a draft, not as solved: now I’m checking it against the literature points you asked for and tightening the claims to what the sources actually support.
exec
/bin/zsh -lc "sed -n '4620,4915p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"@.*\\{(HJZ25|Zhang24|HerNeg24|GTL17|Hernandez05|ChariMoura06|FrenkelMukhin01|Nakajima04|KKKO18|BrunKlesh06|BLPW16)\" -g\"*.bib\" ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "yangian-generic-boundary-fibers|Baxter--Rees|asymptotic modules|negative prefundamental|compact-completion|localizing generation|Francis--Gaitsgory" chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\section{The type-$A$ Baxter--Rees compactification}
\label{sec:typeA-baxter-rees}
\index{Baxter--Rees compactification}
\index{Yangian!Baxter--Rees family}
\index{weightwise MC4}

The representation theory of $Y_\hbar(\fsl_N)$ admits a natural
compactification that unifies three apparently different regimes
into a single algebraic family. Consider the chain of
Kirillov--Reshetikhin modules
\begin{equation}\label{eq:KR-chain-baxter-rees}
 W_0 \xhookrightarrow{F_{1,0}} W_1 \xhookrightarrow{F_{2,1}}
 W_2 \xhookrightarrow{} \cdots
\end{equation}
for a simple node $i \in \{1,\dots,N-1\}$. Write
$W_\infty := \varinjlim_l W_l$ for the inductive limit. Define
$\mathcal{E}_i := W_\infty \otimes_{\CC} \CC[q]$ and, for every
generator~$t$ of the Cartan-doubled Yangian
$Y_\infty(\fsl_N)$, set
 succeeded in 51ms:
./standalone/references.bib:136:@article{ChariMoura06,
 succeeded in 51ms:
chapters/connections/editorial_constitution.tex:270:subcategory requires either localizing generation in a completed
chapters/connections/editorial_constitution.tex:294:\item Francis--Gaitsgory pro-nilpotent completion changes the ambient
chapters/connections/editorial_constitution.tex:302: superpolynomial, forcing localizing generation in place of thick
chapters/connections/editorial_constitution.tex:811: Francis--Gaitsgory completion supplies only the ambient
chapters/connections/editorial_constitution.tex:862:Francis--Gaitsgory completion formalism
chapters/connections/editorial_constitution.tex:1114: desired Francis--Gaitsgory/pro-nilpotent completion.
chapters/connections/editorial_constitution.tex:2073:\item The Francis--Gaitsgory factorization framework~\cite{FG12}
chapters/connections/editorial_constitution.tex:2617:correct framework is localizing generation in a completed/coderived
chapters/examples/yangians_computations.tex:1972: prefundamental or asymptotic modules.
chapters/examples/yangians_computations.tex:2363:The negative prefundamental $L^-(b)$ has weight multiplicities
chapters/examples/yangians_computations.tex:2590:\begin{corollary}[Sectorwise localizing generation; \ClaimStatusProvedHere]
chapters/examples/yangians_computations.tex:2593:\index{truncation sector!localizing generation}
chapters/examples/yangians_computations.tex:3087:and $L^-_{i,a}$ are the negative prefundamental modules of
chapters/examples/yangians_computations.tex:3167:is a bijection, so every negative prefundamental $L^-_{i}(b)$ occurs on
chapters/examples/yangians_computations.tex:3319:bijection, every negative prefundamental $L^-_{i,b}$ already appears
chapters/examples/yangians_computations.tex:3331:Kirillov--Reshetikhin chain and the Baxter--Rees family
chapters/examples/yangians_computations.tex:3333:Theorem~\ref{thm:yangian-generic-boundary-fibers} identifies its
chapters/examples/yangians_computations.tex:3334:generic fibers with Cartan-renormalized asymptotic modules and its
chapters/examples/yangians_computations.tex:3335:boundary fiber with the negative prefundamental module. If one proves
chapters/examples/yangians_computations.tex:3351:boundary. The Baxter--Rees family supplies exactly such an

thinking
**Investigating bib entries**

I noticed that my search in the bib via regex only found one entry, which makes me think there might be an issue with the pattern or the local bib file not containing all entries. I need to inspect the relevant bib entries more closely. Maybe I could use regex to search for specific citation keys, but they might not all be formatted as @article. I'll need to try and refine my search strategy.
exec
/bin/zsh -lc "sed -n '260,520p' standalone/references.bib" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' standalone/references.bib" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "HJZ25|Zhang24|HerNeg24|GTL17|Hernandez05|FG12|ChariMoura06|FrenkelMukhin01|Nakajima04|KKKO18|BrunKlesh06" standalone/references.bib' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% Shared bibliography for standalone papers
% Modular Koszul Duality programme — R. Lorgat

% ============================================================
%  A
% ============================================================

@article{AbouzaidGeneration,
  author  = {Abouzaid, Mohammed},
  title   = {A geometric criterion for generating the Fukaya category},
  note    = {Preprint and related published versions},
}

@article{ADKMV,
  author  = {Aganagic, Mina and Dijkgraaf, Robbert and Klemm, Albrecht
             and Mari\~no, Marcos and Vafa, Cumrun},
  title   = {Topological strings and integrable hierarchies},
  journal = {Comm. Math. Phys.},
  volume  = {261},
  year    = {2006},
 succeeded in 51ms:
             and {G}elfand--{D}ikii algebras},
  journal = {Internat. J. Modern Phys. A},
  volume  = {7},
  number  = {Suppl. 1A},
  year    = {1992},
  pages   = {197--215},
}

@article{FL,
  crossref = {FF92},
}

@article{FFR1994,
  author  = {Feigin, Boris and Frenkel, Edward and Reshetikhin, Nicolai},
  title   = {Gaudin model, {B}ethe ansatz and critical level},
  journal = {Comm. Math. Phys.},
  volume  = {166},
  year    = {1994},
  pages   = {27--62},
}
 succeeded in 50ms:
136:@article{ChariMoura06,
289:@article{FG12,
300:  crossref = {FG12},

thinking
**Searching literature on representations**

I’m noticing that my bibliography is incomplete, and I’m wondering if I have the necessary keys or citations. I need to search online literature regarding several questions I have about Baxter constraints and representations. For instance, do classical settings allow for fundamental representations without spectral constraints, and can these results be deformed? I also want to check on localizing generation and specific analogues of Baxter constraints. I'll carefully look for primary sources and relevant works by prominent researchers.
🌐 Searching the web...
🌐 Searched: site:arxiv.org Yangian asymptotic representations Hernandez Zhang prefundamental Yangians

thinking
**Searching for better resources**

I’m realizing that my search results are poor. I might need to be more directed or consider a general web search using specific terms, perhaps even beyond just arxiv. It seems like I need to broaden my search to find better resources. Exploring other domains could help me locate the information I'm looking for. Let's see how this approach works out for me!
🌐 Searching the web...
🌐 Searched: Hernandez Jimbo Zhang Yangians asymptotic modules prefundamental

thinking
**Searching for research papers**

I'm thinking I should search for prefundamental or asymptotic modules related to Yangians. The HZ 2024 paper might be sufficient, so I’ll check that out first. Also, the Zhang24 work might be useful, especially if it covers exact triangles or TQ. I’ll look for this information on arXiv, which seems like a good place to find those types of papers. It’s quite a bit to explore, but I'm curious about the results!
🌐 Searching the web...
🌐 Searched: Huafeng Zhang Baxter TQ shifted Yangians arXiv


thinking
**Searching primary sources**

The search results look promising, so I think I should open up some primary sources, like the HJZ paper on shifted Yangians and polynomial R-matrices. I'll also consider Zhang Yangians and Baxter's relations, and maybe look into Gautam-Toledano Laredo's work too. I need to verify if there’s literature on completion and localizing generation, particularly around the conditions for completion extensions in relevant categories. It might be necessary to check arXiv for derived categories related to this topic and find supporting evidence.
thinking
**Verifying categories in literature**

I’m considering if the relevant categories refer to the shifted envelope or completed shifted Yangian category, but it seems these might not be standard in the literature. I could state, “I did not find a theorem” based on this review. To be sure, I need to browse more carefully and conduct a focused search to verify the existence of any relevant theorems or discussions in this area. Targeting my search will be crucial!
🌐 Searching the web...
🌐 Searched: "Yangians and Baxter's relations" pdf

thinking
**Searching for article sources**

I need to find the primary source likely titled "Yangians and Baxter's relations." I think searching for an open summary might be a good idea, and I might use the Springer page to look for an abstract. It could be a great starting point. Let’s explore this together and see what I find! It’s all about gathering the right information!
🌐 Searching the web...
🌐 Searched: site:link.springer.com "Yangians and Baxter's relations"

thinking
**Investigating cyclic structures**

It looks like I need to look into HZ papers regarding cyclic and cocyclic parameters, especially focusing on Jordan-Hölder stability over finite lengths. There's something about tensor products of prefundamental components being cyclic for all spectral parameters, which could suggest alternative generators that don't require the Baxter constraint. I should check the HZ paper for anything related to asymptotics, though I’m not sure if that will help. Perhaps searching the text within the PDF could yield better results.
🌐 Searching the web...
🌐 Searched: 'finite representation length' in https://ems.press/content/serial-article-files/48672
🌐 Searching the web...
🌐 Searched: "Asymptotic representations and Drinfeld rational fractions" Yangian quantum affine

thinking
**Searching for relations**

I need to conduct a better search for information about the relationships between Yangians and Baxter's relations. I'm thinking that I might find something useful in a PDF, possibly from Springer. It seems like accessing the abstract could give me enough information to determine if it's worth delving deeper into the study. I'll aim to refine my search to see if I can find relevant papers or articles on this topic.
🌐 Searching the web...
🌐 Searched: "Yangians and Baxter's relations" Springer abstract
🌐 Searching the web...
🌐 Searched: https://arxiv.org/abs/1808.02294
🌐 Searching the web...
🌐 Searched: site:arxiv.org shifted Yangian derived category compact generation
🌐 Searching the web...
🌐 Searched: "shifted Yangian" "category O" "Jordan-Holder" "finite length"

thinking
**Planning edits to remarks**

I need to inspect the exact lines of the current remark to determine where to make changes. I could use tools like `nl -ba` or `sed -n` for that. Before I start editing, it’s essential to provide an update explaining the edits I plan to make. It might also be helpful to update the plan with clear steps I’ll follow. So, I'll focus on creating that plan now since it feels substantial.
codex
Plan for the remaining work:

1. Lock the live theorem surface around `thm:shifted-prefundamental-generation`, `conj:dk-compacts-completion`, and the existing research remark.
2. Cross-check the four research questions against primary sources: Zhang on Baxter relations, Hernandez–Zhang on shifted Yangians, Gautam–Toledano Laredo on the Yangian/quantum-loop bridge, and the local Baxter–Rees section.
3. Rewrite the research remark so it sharply separates:
   proved core,
   deformation route,
   completion/localizing gap,
   type `B/C/D` landscape.
4. Re-read the edited block in context and run narrow hygiene checks on the touched surface.
Plan update
Fortifying the existing MC3 Baxter-constraint research remark with literature-backed statements and a sharper separation of proved versus conjectural mechanisms.
  ✓ Audit the existing MC3 Baxter-constraint remark and nearby theorems in yangians_computations.tex
  → Cross-check the four requested research points against primary sources and local source context
  • Edit the research remark in chapters/examples/yangians_computations.tex
  • Re-read the edited block and run targeted verification/hygiene checks

thinking
**Searching for web results**

I need actual web results, and the previous search queries didn’t show what I needed. I think I could use a search with the author or title to narrow it down. Domains like arxiv.org, aims, ems, or springer might be useful. Perhaps I could also try Google? Although that might not be available. Anyway, I'll aim for a more targeted search this time. Let’s see what I can find!
🌐 Searching the web...
🌐 Searched: "Yangians and Baxter's relations" "Huafeng Zhang"

thinking
**Searching for specific terms**

I think I need to find specific lines, possibly by looking for open source pages. I should search within the results for terms like "finite representation length" and "cyclic or cocyclic." It seems like I can get abstract ideas, but I'll focus on searching within the open results to narrow it down further. This should help me find the most relevant information!
🌐 Searching the web...
🌐 Searched: https://ems.press/journals/prims/articles/14298177
🌐 Searching the web...
🌐 Searched: "Yangians and Baxter's relations" "Huafeng Zhang" site:springer.com
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: "10.1007/s11005-020-01285-x" abstract
🌐 Searching the web...
🌐 Searched: "Asymptotic representations and Drinfeld rational fractions" Hernandez Jimbo all finite type

thinking
**Searching PDF sources**

I need to find the primary source, which might be hidden within the lines of a paper. I'll consider using a PDF search if I can access an open PDF. It sounds like a good idea to open the PDF text and perform a search. Let's give that a try and see what I can uncover!
🌐 Searching the web...
🌐 Searched the web

thinking
**Exploring PDF access**

I’m considering whether it’s possible to open a PDF directly from the URL I found. There’s a URL available: `https://ems.press/content/serial-article-files/48672?nt=1`. I wonder if I can use this link to access the PDF directly. It seems like a straightforward approach, but I need to confirm if it will lead me to the right content when I try to open it. Let’s see if that works!
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: "finite representation length" "shifted Yangians"

thinking
**Searching for article text**

I noticed the seminar abstract says that "the class of finite representation length is stable under tensor product." While I could use this as supporting information, referring to the abstract feels a bit weak. It seems better to actually find the article text through a web search. I'll look up that exact phrase, hoping to find a snippet or access a PDF from a site like Oberwolfach. That sounds like a solid plan!
🌐 Searching the web...
🌐 Searched: "finite representation length" "tensor product" "shifted Yangians" "Hernandez"
🌐 Searching the web...
🌐 Searched: orthogonal symplectic Yangians Yang-Baxter R-operators spectral parameter shift

thinking
**Investigating R-matrix details**

I’m considering the orthogonal R-matrix, which has an extra \(K\)-term and \(\kappa\)-shift. This means that in type D, the companion hyperplane could differ from the \(A\)-type formula unless I’m using Drinfeld generators instead of RTT normalization. It feels a bit subtle and potentially important, so I should look into it further. I’ll search my local repository or other sources for information about the type D Baxter constraint—maybe I can find something useful!
codex
The non-simply-laced part is subtler than the first-pass remark suggests. I’m checking whether type `D` really behaves like `A` at the relevant local singular-vector step, or whether the orthogonal/symplectic Yangian normalization already shifts the companion hyperplane.
exec
/bin/zsh -lc "sed -n '3290,3395p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"type D|type~D|orthogonal|symplectic|root-length|half-shift|a - \\\\frac\\{1\\}\\{2\\}|Baxter constraint|non-simply-laced|folding\" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1088,1148p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
separated completion, and hence the image of
$D^b(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$ is generated there by
this set. Since $a \mapsto a - \tfrac{1}{2}$ is bijective, this is
equivalent to generation by the full prefundamental family. If a chosen
completed enhancement is compactly generated with compact part given by
the shifted envelope, the same Baxter seed generates that enhancement
as a localizing subcategory. The compact-object identification for the
intended Yangian completion is the separate remaining packet
\textup{(}Conjecture~\textup{\ref{conj:dk-compacts-completion}}\textup{)}.
The proof uses the Baxter singular vector
(Proposition~\ref{prop:baxter-yangian-equivariance},
rank-independent) and the prefundamental Clebsch--Gordan closure
(Proposition~\ref{prop:prefundamental-clebsch-gordan}).
The prefundamental Clebsch--Gordan closure
(Proposition~\ref{prop:prefundamental-clebsch-gordan}) holds for
all simple~$\mathfrak{g}$ at the character level. Extension to
arbitrary type thus reduces to the categorical lift: upgrading the
$K_0$-level identity to a module decomposition in~$\mathcal{O}^{\mathrm{sh}}$.
\end{remark}

 succeeded in 51ms:
chapters/examples/yangians_foundations.tex:253: where $K_{(ab),(cd)} = -J_{ab}J_{cd}$ is the symplectic contraction,
chapters/examples/yangians_foundations.tex:255: is the symplectic form, and $K$ satisfies $K^2 = -2n\,K$ and
chapters/examples/yangians_foundations.tex:257: symplectic-type sign, distinguishing type~$C$ from types~$B$ and~$D$.
chapters/examples/yangians_foundations.tex:291:For type $C$, the symplectic contraction $K$ satisfies $K^2 = -NK$
chapters/examples/yangians_foundations.tex:292:and $PK = KP = -K$: the sign difference from the orthogonal case
chapters/examples/yangians_foundations.tex:481:This is the quadratic dual of the RTT relation~\eqref{eq:rtt-modes}: the bar differential encodes the orthogonal complement of the relations under the chiral pairing.
chapters/examples/yangians_foundations.tex:493:\item $\bar{B}^2 = R^\perp \subset V^* \otimes V^*$ (orthogonal complement of relations on $\overline{C}_3(X)$).
chapters/examples/yangians_foundations.tex:535:and relations~$R^\perp$, the orthogonal complement
chapters/examples/yangians_foundations.tex:546:The orthogonal complement $R^\perp$ consists of quadratic expressions $Q(T^*, T^*)$ that pair to zero with all elements of $R$. For $\mathfrak{sl}_2$ (where $V = \mathbb{C}^2$ and $P$ is the $4 \times 4$ permutation matrix), $R^\perp$ is computed by direct matrix calculation. The RTT relation at fixed spectral parameters defines a linear map $\Phi_R\colon \mathrm{End}(V)^{\otimes 2} \to \mathrm{End}(V)^{\otimes 2}$ by $X \mapsto R_{12} X - \sigma(X) R_{12}$ where $\sigma$ is the flip; its image is the space of relations~$R$. Writing out the $16 \times 16$ matrix of $\Phi_R$ in the standard basis of $\mathrm{End}(\mathbb{C}^2)^{\otimes 2}$ and computing its orthogonal complement with respect to the trace pairing, $R^\perp$ coincides with the image of $\Phi_{R^{-1}}$, i.e., the space of $R^{-1}$-RTT relations (verified by explicit $16\times 16$ matrix computation; see \texttt{test\_koszul\_dual\_dims.py}).
chapters/examples/yangians_foundations.tex:566:At $\hbar = 0$ (the classical limit), $R(u) = R^{-1}(u) = 1$, and the RTT algebra becomes commutative: $[T_{ij}^{(r)}, T_{kl}^{(s)}] = 0$, i.e., $\mathrm{Sym}(V)$ where $V = \bigoplus_{r \geq 0} \mathfrak{gl}_2^{(r)}$. The Koszul dual of the symmetric algebra is the exterior algebra: $\mathrm{Sym}(V)^! = \bigwedge(V^*)$. Since $R^{-1}(u;0) = R(u;0) = 1$, the defining relations of $\mathrm{Sym}(V)$ are the antisymmetric tensors $v \otimes w - w \otimes v$, and the orthogonal complement $R^\perp$ consists of the symmetric tensors $v \otimes w + w \otimes v$, which are the defining relations of $\bigwedge(V^*)$. (In the Drinfeld presentation, the classical limit is the noncommutative algebra $U(\mathfrak{g}[t])$; the two presentations yield different classical limits.)
chapters/examples/yangians_foundations.tex:584:$Y(\fg^\vee)$ for non-simply-laced~$\fg$, realizing Langlands
chapters/examples/yangians_foundations.tex:2768:with the canonical shifted-symplectic pairing\textup{)}.
chapters/examples/yangians_foundations.tex:2834:\section{Shifted RTT duality and orthogonal coideals}
chapters/examples/yangians_foundations.tex:2835:\label{sec:shifted-rtt-duality-orthogonal-coideals}
chapters/examples/yangians_foundations.tex:2837:\index{orthogonal coideal}
chapters/examples/yangians_foundations.tex:2855:orthogonal coideal of the $\mathfrak{sl}_2$ Casimir quotient is a
chapters/examples/yangians_foundations.tex:3049:$(-1)$-shifted symplectic structure is the tangent-level shadow of
chapters/examples/yangians_foundations.tex:3050:the shifted-symplectic geometry that controls the Yangian deformation
chapters/examples/yangians_foundations.tex:3133:\index{shifted-symplectic!Lagrangian envelope}
chapters/examples/yangians_foundations.tex:3138:$(-1)$-shifted symplectic pairing
 succeeded in 51ms:
\item \emph{Multiplicity-free $\ell$-weights.}
 For any simple~$\fg$ and any fundamental weight~$\omega_i$, the
 evaluation module $V_{\omega_i}(a) = \mathrm{ev}_a^*(V_{\omega_i})$
 of $Y(\fg)$ has the property that its $q$-character
 $\chi_q(V_{\omega_i}(a))$ is a sum of distinct $\ell$-weight
 monomials: no $\ell$-weight has multiplicity $> 1$. This is the
 fundamental result of Chari--Moura~\cite{ChariMoura06}.
 The multiplicity-free property ensures that the tensor product
 $V_{\omega_i}(a) \otimes V_{\omega_j}(b)$
 has a composition series whose successive quotients are
 $\ell$-weight-separated at generic spectral parameters, enabling
 the categorical Clebsch--Gordan decomposition
 \textup{(}Theorem~\textup{\ref{thm:categorical-cg-all-types}}\textup{)}.

\item \emph{MC3 categorical closure.}
 The multiplicity-free $\ell$-weight property, combined with the
 Francis--Gaitsgory pro-nilpotent completion and the DK comparison
 on compacts, yields:
 \begin{enumerate}[label=\textup{(\alph*)}]
 \item Prefundamental representations $L_i^\pm(a)$ exist as
🌐 Searching the web...
🌐 Searched the web

thinking
**Evaluating search stability**

I'm realizing that search result IDs from different calls aren't stable; each call seems to reset the numbering. Perhaps I should try to search and open results in one call, or utilize the current response IDs instead. It sounds like a focused search with relevant queries could help streamline this process and improve the outcomes. I’m getting curious about how to approach it to get more reliable results!
🌐 Searching the web...
🌐 Searched: "Shifted Yangians and Polynomial R-Matrices" EMS Press

thinking
**Searching for relations**

I didn't find any information about Yangians and Baxter's relations in my recent search. It seems like I might need to be more specific, especially by targeting a source like the Cambridge website. Okay, I’ll refine my search terms or directly look into academic databases that are likely to have detailed information on this topic. Let’s try again and see if I can get better results this time!
🌐 Searching the web...
🌐 Searched: "Yangians and Baxter's relations" "Huafeng Zhang" "Lett Math Phys"
🌐 Searching the web...
🌐 Searched: https://ems.press/journals/prims/articles/14298177
🌐 Searching the web...
🌐 Searched: "Yangians, quantum loop algebras, and abelian difference equations" arxiv
🌐 Searching the web...
🌐 Searched: 'finite representation length' in https://ems.press/content/serial-article-files/48672
🌐 Searching the web...
🌐 Searched: https://ems.press/content/serial-article-files/48672
🌐 Searching the web...
🌐 Searched: https://ems.press/content/serial-article-files/48672

thinking
**Exploring cyclicity and generation**

This gives more nuance since shifted cases show cyclicity and cocyclicity with positive and negative modules, unlike non-shifted cases. There are polynomial R-matrices for prefundamental with arbitrary irreducible. I could consider using positive prefundamental and arbitrary irreducible modules, but positive modules might not be helpful since they are one-dimensional. Example 5.11 shows an exact sequence. I could check `Theorem 6.4` for factorization in the sl2-case and look into localizing generation literature as well.
🌐 Searching the web...
🌐 Searched: Yangian category O compactly generated derived localizing generation


thinking
**Clarifying the theorem details**

I should probably explain that the localizing subcategory generated by evaluation modules contains generic asymptotic modules and is closed under flat specialization, particularly as \(q\) approaches 0. This simplifies things by removing direct singular vector dependence. Also, I need to highlight that the completion extension depends on localizing generation. It seems important to structure this clearly to ensure understanding.
thinking
**Clarifying definitions**

I'm thinking about Example 5.11, which uses \(d_{ij}\) instead of \(d_i\). I should probably define \(d_{ij}\) more clearly. It seems that in the HZ paper, around line p7, there might be a definitional context for it. I'll search for the term `dij :=` to find the exact formula. Ensuring that definitions are clear is really important for understanding this concept fully!
🌐 Searching the web...
🌐 Searched: 'dij :=' in https://ems.press/content/serial-article-files/48672
codex
The literature check changed one important point: there is already an all-type Baxter pattern on the shifted-Yangian side. It is not a blind `1/2` shift, but the generalized-simple-root shift by the symmetrized Cartan data `d_{ij}`. That means the remark should say “type `D` keeps the half-shift, types `B/C` become root-length dependent,” not leave both as equally open.
exec
/bin/zsh -lc "sed -n '3728,3768p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"HJZ25|GTL17|Hernandez.?Zhang|Yangians and Baxter|Baxter's relations and spectra of quantum integrable models|Frenkel.?Hernandez\" ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\{W_m = W(\Psi_{\leq m})\}_{m \geq 0}$ satisfies the
Mittag--Leffler condition: the transition maps
$W_{m+1} \twoheadrightarrow W_m$ are surjective at each weight,
whence $R^1\varprojlim = 0$ and the ordinary standard is recovered as
$M(\Psi) \simeq R\varprojlim_m W_m$ inside the separated completion
$\widehat{\mathcal{O}}$.
The argument is rank-independent (it depends only on the weight
filtration, not on the Dynkin type), and the finite-dimensionality of
each~$W_m$ is guaranteed by the proved evaluation core
(Theorem~\ref{thm:eval-core-identification}).
Extension to arbitrary type remains part of the unresolved
post-core extension/completion packet: one still needs the
shifted-prefundamental generation and completion input beyond the
type-$A$ surface.
\end{remark}

\begin{conjecture}[DK on compacts and completion extension; \ClaimStatusConjectured]
\label{conj:dk-compacts-completion}
\index{Drinfeld--Kohno!derived!compact extension}
\index{Francis--Gaitsgory!pro-nilpotent completion}
 succeeded in 87ms:
./compute/tests/test_hjz_prefundamental.py:17:  - Hernandez-Jimbo-Zhang (2025) [HJZ25]
exec
/bin/zsh -lc "sed -n '4248,4315p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Conjecture~\ref{conj:dk-compacts-completion}.
\end{proof}

\begin{remark}[Francis--Gaitsgory completion mechanism]\label{rem:francis-gaitsgory-mc3}
Once one has an equivalence on the relevant compact core and a
compatible Francis--Gaitsgory-style completion formalism, the passage
to the corresponding cocompletion is categorical and does not depend
on Lie type. What this mechanism does \emph{not} prove by itself is
that the required compact-core equivalence or the needed completion
comparison holds uniformly in every type.
\end{remark}

\subsection{Landscape of the MC3 extension}
\label{sec:mc3-extension-landscape}

\begin{conjecture}[Type-independence of the remaining MC3 completion mechanisms;
 \ClaimStatusConjectured]
\label{conj:mc3-automatic-generalization}
\label{conj:mc3-proof-step-analysis}% backward compatibility (renamed from prop:)
Let~$\mathfrak{g}$ be simple. Assume that, beyond the all-types

thinking
**Inspecting bibliography entry**

I need to take a closer look at the bibliography entry for HJZ25 and check its actual content. It might be worth mentioning that HJZ25 is key for backward compatibility, specifically referencing Hernandez–Jimbo from 2012. I'll focus on examining the lines surrounding that bibliography entry to see what insights or details can be gleaned. This helps ensure everything is accurate and reflects the right information.
codex
I also checked the repo’s bibliography layer: `HJZ25` is being used as the standing key for the Hernandez–Jimbo prefundamental/Baxter package, and `GTL17` is already wired in. I can tighten the remark without introducing new bib debt.
exec
/bin/zsh -lc "sed -n '680,725p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
D. Hernandez and B. Leclerc, \emph{Cluster algebras and quantum affine algebras}, Duke Math. J. \textbf{154} (2010), no.~2, 265--341.

\bibitem{HerNeg24}
D. Hernandez and A. Negu\c{t}, \emph{Shifted quantum groups and matter multiplets}, Comm. Math. Phys. \textbf{379} (2020), no.~1, 189--215.

\bibitem{HJZ25}% key retained for backward compat; actual: Hernandez--Jimbo 2012
D.~Hern\'andez and M.~Jimbo, \emph{Asymptotic representations and Drinfeld rational fractions}, Compos. Math. \textbf{148} (2012), no.~5, 1593--1623, arXiv:1104.1891.

\bibitem{Hormander}
L. H\"ormander, \emph{The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis}, Classics in Mathematics, Springer, 2003.

\bibitem{Hornfeck93}
K. Hornfeck, \emph{$W$-algebras with set of primary fields of dimensions $(3,4,5)$ and $(3,4,5,6)$}, Nucl. Phys. B \textbf{407} (1993), 237--246.

\bibitem{HS87}
V. Hinich and V. Schechtman, \emph{On homotopy limit of homotopy algebras}, in \emph{$K$-theory, Arithmetic and Geometry} (Yu.~I.~Manin, ed.), Lecture Notes in Mathematics \textbf{1289}, Springer, 1987, 240--264.

\bibitem{HS93}
V. Hinich and V. Schechtman, \emph{Homotopy Lie algebras}, in \emph{I.\,M.\,Gelfand Seminar}, Adv. Sov. Math. \textbf{16}, Part~2 (1993), 1--28.

exec
/bin/zsh -lc "sed -n '1,220p' compute/lib/mc3_frontier.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1398,1425p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
"""Unified MC3 frontier: Ext obstructions, tilting, chromatic filtration, YBE.

Consolidates mc3_ext_computation, mc3_tilting_probe, mc3_chromatic_strategy
into a single module with no doc-only functions and no duplicated utilities.

KEY RESULTS:
  1. Hom(L^-, V_n) = n/2+1 for n even, 0 for n odd (weight parity).
  2. Euler characteristic chi(L^-, V_n) = sum_{k=0}^{n/2} p(k) for n even.
  3. Resolution obstruction delta(k) = p(k) - 1 grows sub-exponentially.
  4. Hardy-Ramanujan: log(p(k))/sqrt(k) -> pi*sqrt(2/3).
  5. Tilting complex from Baxter SES with self-orthogonality for odd spin.
  6. E_1 page: partitions of loop_degree into odd parts >= 3.
  7. Capture ratio R(n) -> 0: naive truncation fails.
  8. Yang-Baxter equation verified symbolically (8x8 matrix computation).
  9. Chebyshev recurrence [V_n] = [V_1]*[V_{n-1}] - [V_{n-2}] at character level.

References:
  - yangians_computations.tex, MC3 frontier
  - concordance.tex, MC3 architecture
"""
 succeeded in 50ms:
E.~Frenkel and E.~Mukhin, \emph{Combinatorics of $q$-characters of finite-dimensional representations of quantum affine algebras}, Comm. Math. Phys. \textbf{216} (2001), no.~1, 23--57, arXiv:math/9911112.

\bibitem{FR99}
E.~Frenkel and N.~Reshetikhin, \emph{The $q$-characters of representations of quantum affine algebras and deformations of $\mathcal{W}$-algebras}, in: Recent developments in quantum affine algebras and related topics (Raleigh, NC, 1998), Contemp. Math. \textbf{248}, Amer. Math. Soc., 1999, 163--205, arXiv:math/9810055.

\bibitem{GTL17}
S.~Gautam and V.~Toledano Laredo, \emph{Yangians, quantum loop algebras, and abelian difference equations}, J. Amer. Math. Soc. \textbf{29} (2016), no.~3, 775--824, arXiv:1310.7318.

\bibitem{GTL-catO}
S.~Gautam and V.~Toledano Laredo, \emph{Meromorphic tensor equivalence for Yangians and quantum loop algebras}, Publ. Math. Inst. Hautes \'Etudes Sci. \textbf{125} (2017), 267--337, arXiv:1403.5251.

\bibitem{Hernandez06KR}
D.~Hern\'andez, \emph{The Kirillov--Reshetikhin conjecture and solutions of $T$-systems}, J. Reine Angew. Math. \textbf{596} (2006), 63--87, arXiv:math/0501202.

\bibitem{Hernandez07}
D.~Hern\'andez, \emph{On minimal affinizations of representations of quantum groups}, Comm. Math. Phys. \textbf{276} (2007), no.~1, 221--259, arXiv:math/0607527.

\bibitem{Nakajima04}
H.~Nakajima, \emph{$t$-Analogs of $q$-characters of Kirillov--Reshetikhin modules of quantum affine algebras}, Represent. Theory \textbf{7} (2003), 259--274, arXiv:math/0204185.

exec
/bin/zsh -lc 'rg -n "d_ij|dij|type D|type B|type C|localizing generation|Baxter constraint|asymptotic modules|Baxter--Rees|removing the Baxter constraint" healing_20260413_130533/H16_remove_baxter_MC3.md platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md compute/lib/prefundamental_cg_universal.py compute/lib/baxter_derived_lift.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 288

healing_20260413_130533/H16_remove_baxter_MC3.md:3:Added a new research remark at [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3310) that separates three issues cleanly: the proved type-$A$ Baxter-locus theorem, a conjectural deformation route through the Baxter--Rees/asymptotic family, and the non-simply-laced type-$B/C/D$ normalization problem. The remark answers your four prompts directly: it identifies asymptotic/Baxter--Rees objects as the real alternative generators, frames the classical generation result as deforming through KR/asymptotic families rather than through off-hyperplane singular vectors, records that the compact/localizing extension is still exactly the open packet `conj:dk-compacts-completion`, and splits the type-$B/C/D$ picture into the simply-laced type-$D$ lift-and-lower issue versus the type-$B/C$ root-length normalization issue.
healing_20260413_130533/H16_remove_baxter_MC3.md:11:- TECHNIQUE: deform from the evaluation core through the Baxter--Rees family; specialize asymptotic fibers to the prefundamental boundary via specialization-stable localizing generation
healing_20260413_130533/H16_remove_baxter_MC3.md:25:- TECHNIQUE: asymptotic/Baxter--Rees deformation plus specialization-stable localizing generation; type-$D$ via lift-and-lower, type-$B/C$ via rootwise normalization test
healing_20260413_130533/H16_remove_baxter_MC3.md:85:RESEARCH: Can the Baxter constraint be removed from MC3?
healing_20260413_130533/H16_remove_baxter_MC3.md:89:MC3 type-A thick generation is conditional on the Baxter constraint b = a - 1/2.
healing_20260413_130533/H16_remove_baxter_MC3.md:92:1. The Baxter constraint comes from the shifted prefundamental representations.
healing_20260413_130533/H16_remove_baxter_MC3.md:98:4. For types B, C, D: what is the analogue of the Baxter constraint?
healing_20260413_130533/H16_remove_baxter_MC3.md:116:The user wants a research remark related to the removal of the Baxter constraint, so I should consider if there’s a need for a proof edit. I might add a remark, and I’ll ensure to communicate my confidence in the final report.
healing_20260413_130533/H16_remove_baxter_MC3.md:124:Task scope is `chapters/examples/yangians_computations.tex`, centered on MC3 and the Baxter constraint. I’m first loading the required constitutional files and locating the exact MC3 surface, then I’ll assess whether this is a proof repair, a research-programme remark, or both.
healing_20260413_130533/H16_remove_baxter_MC3.md:219:I’ve loaded the governing files. Next I’m mapping the exact MC3 claim surface, nearby dependencies, and any existing discussion of Baxter constraints or type-BCD analogues before I draft or edit anything.
healing_20260413_130533/H16_remove_baxter_MC3.md:242:collab spawn_agent(call_kB4m6pBRhGPALbk3m59POlSC, prompt="Inspect the Yangian chapter surfaces relevant to MC3 and the Baxter constraint. Identify the exact labels, status tags, …")
healing_20260413_130533/H16_remove_baxter_MC3.md:243:spawn_agent(call_kB4m6pBRhGPALbk3m59POlSC, prompt="Inspect the Yangian chapter surfaces relevant to MC3 and the Baxter constraint. Identify the exact labels, status tags, …") pending init:
healing_20260413_130533/H16_remove_baxter_MC3.md:247:/bin/zsh -lc 'rg -n "MC3|Baxter|prefundamental|type-A thick generation|localising generation|thick generation|shifted prefundamental|BCD|type B|type C|type D" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/connections/concordance.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
healing_20260413_130533/H16_remove_baxter_MC3.md:261:metadata/theorem_registry.md:2037:| `thm:yangian-baxter-rees-algebraicity` | `theorem` | 4762 | Algebraicity of the Baxter--Rees family |
healing_20260413_130533/H16_remove_baxter_MC3.md:262:metadata/theorem_registry.md:2039:| `prop:baxter-rees-derived-realization` | `proposition` | 4814 | Derived realization of the Baxter--Rees family |
healing_20260413_130533/H16_remove_baxter_MC3.md:266:metadata/theorem_registry.md:3143:| `thm:algebraicity-baxter-rees-family` | `theorem` | 849 | Algebraicity of the Baxter--Rees family |
healing_20260413_130533/H16_remove_baxter_MC3.md:267:metadata/theorem_registry.md:3145:| `thm:derived-realization-baxter-rees-family` | `theorem` | 924 | Derived realization of the Baxter--Rees family |
healing_20260413_130533/H16_remove_baxter_MC3.md:452:/bin/zsh -lc 'rg -n "Baxter constraint" -n "Baxter" -n "Baxter TQ"' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
exec
/bin/zsh -lc "sed -n '260,520p' healing_20260413_130533/H16_remove_baxter_MC3.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' healing_20260413_130533/H16_remove_baxter_MC3.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/theorem_registry.md:2030:| `cor:mc3-all-types` | `corollary` | 4131 | Three-layer MC3 status after categorical CG closure |
metadata/theorem_registry.md:2037:| `thm:yangian-baxter-rees-algebraicity` | `theorem` | 4762 | Algebraicity of the Baxter--Rees family |
metadata/theorem_registry.md:2039:| `prop:baxter-rees-derived-realization` | `proposition` | 4814 | Derived realization of the Baxter--Rees family |
metadata/theorem_registry.md:2925:| `thm:thqg-V-mc3-thick-generation` | `theorem` | 2108 | Type-$A$ MC3 reduction via the gravitational Yangian |
metadata/theorem_registry.md:3141:| `thm:derived-realization-negative-prefundamental` | `theorem` | 743 | Derived realization of negative prefundamentals |
metadata/theorem_registry.md:3142:| `thm:baxter-envelope-criterion` | `theorem` | 789 | Baxter-envelope criterion |
metadata/theorem_registry.md:3143:| `thm:algebraicity-baxter-rees-family` | `theorem` | 849 | Algebraicity of the Baxter--Rees family |
metadata/theorem_registry.md:3145:| `thm:derived-realization-baxter-rees-family` | `theorem` | 924 | Derived realization of the Baxter--Rees family |
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
 succeeded in 51ms:
# H16_remove_baxter_MC3 (464s)

Added a new research remark at [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3310) that separates three issues cleanly: the proved type-$A$ Baxter-locus theorem, a conjectural deformation route through the Baxter--Rees/asymptotic family, and the non-simply-laced type-$B/C/D$ normalization problem. The remark answers your four prompts directly: it identifies asymptotic/Baxter--Rees objects as the real alternative generators, frames the classical generation result as deforming through KR/asymptotic families rather than through off-hyperplane singular vectors, records that the compact/localizing extension is still exactly the open packet `conj:dk-compacts-completion`, and splits the type-$B/C/D$ picture into the simply-laced type-$D$ lift-and-lower issue versus the type-$B/C$ root-length normalization issue.

Verification: label uniqueness passed. A full `latexmk` run parsed through the edited Yangian section and then failed later, outside this edit, at [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:677) on an existing undefined control sequence `B^{\ord}`.

## Fortification Report
For `thm:shifted-prefundamental-generation`:
- PRIMARY PROOF: sound
- SECONDARY PROOF: sketched
- TECHNIQUE: deform from the evaluation core through the Baxter--Rees family; specialize asymptotic fibers to the prefundamental boundary via specialization-stable localizing generation
- CONDITION STATUS: unconditional on the Baxter-locus seed inside the shifted envelope; conditional on compact/localizing hypotheses for the intended completion
- CONFIDENCE: medium

For `thm:mc3-type-a-resolution`:
- PRIMARY PROOF: sound
- SECONDARY PROOF: identified
- TECHNIQUE: replace the Baxter-hyperplane companion argument by a deformation/specialization argument, then invoke the existing pro-Weyl and completion formalism
- CONDITION STATUS: unconditional type-$A$ reduction to the compact-completion packet; remaining completion step conditional on `conj:dk-compacts-completion`
- CONFIDENCE: medium

thinking
**Evaluating healing notes**

The previous healing notes indicate that the same task was done earlier, so I'll add my current remarks. It looks like we might improve on this. The note mentions using local sources only, but now we have web literature that can strengthen our findings. I need to inspect the explorer to see if it's necessary, or maybe it isn't. I might check with the existing agent to see if this has already been completed.
collab wait(call_t27MVyPTPT83ujNt264DBV5C)
  receivers: 019d86b7-9047-7212-b3ab-43b64c84f299
wait(call_t27MVyPTPT83ujNt264DBV5C) 1 agents complete:
  019d86b7-9047-7212-b3ab-43b64c84f299 completed: "**MC3 Baxter surface**
- `chapters/examples/yangians_computations.tex:3068-3335` — `thm:shifted-prefundamental-generatio…"
🌐 Searching the web...
🌐 Searched: 'Example 5.11' in https://ems.press/content/serial-article-files/48672
🌐 Searching the web...
🌐 Searched: "Baxter's relations and spectra of quantum integrable models" arXiv 2015
exec
/bin/zsh -lc "rg -n \"Frenkel.*Hernandez|FH15|Baxter's Relations and Spectra of Quantum Integrable Models|1308.3444\" bibliography/references.tex standalone/references.bib" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:




thinking
**Structuring the remark**

I'm thinking about avoiding bib entries, but I might still cite HJZ25 and GTL17 without needing new references. I want to inspect lines around my current remark to see how I can patch things up. Keeping it concise is key as I answer four prompts. I could include phrases like "Research route" and "Literature boundary" and maybe mention concepts like "What is proved" and "What remains conjectural." I’ll aim for clear sentences instead of bullet points as I draft this improved remark.
thinking
**Structuring the content**

I need to make sure I include a few key points. First is the proved core, focusing on the type A generation theorem related to the Baxter-locus seed, where the bijection shows that coverage isn't an issue. Next, I should mention other generators, such as asymptotic/KR modules and the Baxter-Rees family. Lastly, I'll cover the deformation approach to demonstrate that generic asymptotic fibers fit within the localizing subcategory, utilizing modular evaluations and flat family specialization to establish boundary negative prefundamental modules.
thinking
**Discussing deformation and extensions**

I'm thinking about how this deforms the classical fundamental-generation theorem without needing off-hyperplane singular vectors. For the completion extension, I need the sectorwise localizing formalism and FG/Lurie, but only after confirming compact generation. It seems there isn’t a Yangian-specific theorem in the current literature that proves the completed shifted Yangian category meets the necessary hypotheses, which is exactly what remains conjectured in the dk-compacts-completion. 

Also, the B/C/D analogue is regarding HJZ25's all-type Baxter relations, which are dependent on generalized simple roots, leading to a root-datum-dependent spectral shift rather than a universal scalar.
exec
/bin/zsh -lc "rg -n \"Shifted Yangians and Polynomial R-Matrices|Yangians and Baxter's relations|Huafeng Zhang|shifted Yangians and polynomial R-matrices\" bibliography/references.tex standalone/references.bib" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"A_\\{i,a\\}|A_\\{i, a\\}|generalized simple root|d_\\{ij\\}|\\Psi_\\{j,a-d_\\{ij\\}\\}\" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/connections/concordance.tex standalone/N2_mc3_all_types.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:




thinking
**Considering citation needs**

I’m thinking about how to present a formula in my remark without needing a citation, but I wonder if I should include one since the user asks for research. It could be essential to properly cite the literature. I may have to add an entry to my bibliography for citations, and I need to consider where to place it alphabetically. Although I could simplify by just making a statement about the Baxter package without citations, I feel the claim might need more support.
thinking
**Organizing complex ideas**

I’m reflecting on how to present the shifted category and the role of generalized simple roots. It seems that the analogy I'm using is dependent on the root datum. I need to be careful about punctuation, like avoiding em-dashes and using semicolons instead. The term "landscape" isn't ideal as a metaphor, especially since the user specifically asked for a "type-BCD landscape." Instead, I could phrase it as a "type-B/C/D picture." Also, I want to be cautious about stating available theorems unless verified.
thinking
**Considering hedging in research**

I’m thinking about the role of hedging in my research remarks. It seems that it might be acceptable to hedge when discussing the absence of literature. This way, I can express uncertainty while remaining accurate about the information I'm presenting. I just want to ensure that my phrasing conveys the right amount of caution without sounding overly vague. It’s a fine balance to strike, but I think I can manage it!
codex
I have enough evidence to rewrite the remark. The main change is conceptual: I’m replacing the speculative `B/C` discussion with the stronger statement that the all-type analogue is governed by generalized-simple-root shifts, while keeping the completion packet explicitly open.

thinking
**Searching for citations**

I'm considering how to verify details accurately. If I can’t confirm everything, it might be best to use a note to highlight that. I want to avoid making mistakes, so I think I should look for the title lines on the search page text. For an exact citation, it seems like getting information directly from the PRIMS page summary, including the author and year, would be the way to go.
🌐 Searching the web...
🌐 Searched: https://ems.press/journals/prims/articles/14298177

thinking
**Searching for bibliography entries**

I’m thinking about adding a bibliography entry if it’s necessary. If the paper already has a bibliography, I might not need to add another line. I could search in `standalone/N2_mc3_all_types.tex` to find any existing bibliography items. That might make it easier to borrow something instead of creating a new entry. I can explore HZ24 and use regex to look within the standalone file for items.
exec
/bin/zsh -lc 'rg -n "Shifted Yangians and Polynomial R-Matrices|PRIMS|Hernandez, Huafeng Zhang|10.4171/PRIMS/60-1-1|HZ24" standalone/N2_mc3_all_types.tex bibliography/references.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bibliography/references.tex:1295:\bibitem{HZ24}
exec
/bin/zsh -lc "sed -n '1288,1305p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\bibitem{Tohoku}
A. Grothendieck, \emph{Sur quelques points d'alg\`ebre homologique}, T\^ohoku Math.~J.\ (2) \textbf{9} (1957), 119--221.

\bibitem{WW27}
E.~T. Whittaker and G.~N. Watson, \emph{A Course of Modern Analysis}, 4th ed., Cambridge Univ.\ Press, 1927.

\bibitem{HZ24}
D. Hernandez and H. Zhang, \emph{Shifted Yangians and Polynomial $R$-Matrices}, Publ. Res. Inst. Math. Sci. \textbf{60} (2024), no.~1, 1--69.

\bibitem{ZhangTheta24}
H. Zhang, \emph{Theta series for quantum loop algebras and Yangians}, Comm. Math. Phys. \textbf{405} (2024), no.~10, Paper No.~231.

\bibitem{FeiginSemikhatov}
B.~L. Feigin and A.~M. Semikhatov, \emph{$\mathcal W_n^{(2)}$ algebras}, Nuclear Phys.~B \textbf{698} (2004), 409--449.

\bibitem{FehilyHook}
Z.~Fehily, \emph{Inverse reduction and hook-type $W$-algebras}, J.~Pure Appl.\ Algebra \textbf{228} (2024), no.~7, Paper No.~107006.

thinking
**Searching for citation**

I’m thinking about citing HZ24, but first, I need to check if Zhang24 is a key that exists in my bibliography. I need to search through the relevant materials to make sure I have the right references. It’s essential to ensure that I’m accurately confirming citations and not missing anything important. Let’s see what I can find to solidify this citation!
exec
/bin/zsh -lc "rg -n \"Yangians and Baxter|Zhang24|Zhang.*Baxter|Baxter's relations|FrenkelHernandez|FH15\" bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1254:\bibitem{Zhang24}
1255:H. Zhang, \emph{Baxter operators and asymptotic representations}, Selecta Math. (N.S.) \textbf{26} (2020), no.~2, Paper No.~23.

thinking
**Structuring remarks for clarity**

I’m thinking about how to align the document with clear and simple sentences. Using explicit phrases within paragraphs could enhance clarity. I might structure it into mini-paragraphs like "Proved core," "Alternative generators," and so on. LaTeX seems great for this, using `\smallskip\noindent\emph{Proved core.}` as a format. I’d want to avoid nested bullets but feel fine about using separate mini-paragraphs within the manuscript. It looks like a solid plan!
codex
I’m editing only the existing research-remark block. The goal is to replace the weaker speculative discussion with four sharper pieces: proved core, alternative generators, completion boundary, and the all-type root-data analogue.
Reconnecting... 1/5 (stream disconnected before completion: Transport error: network error: error decoding response body)
exec
/bin/zsh -lc 'rg -n "HZ24|Zhang24" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/yangians_computations.tex:2837:the three-term TQ relations of Zhang~\cite{Zhang24} lift from
chapters/examples/yangians_computations.tex:2889:whose $K_0$-class recovers the formula of Zhang~\cite{Zhang24},
chapters/examples/yangians_computations.tex:3892: the decategorified TQ relations of Zhang~\cite{Zhang24}
chapters/examples/yangians_computations.tex:5060:theory of Hernandez--Zhang~\cite{HZ24} and Zhang~\cite{ZhangTheta24}),
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
@@ -3313,4 +3313,5 @@
 \index{Baxter constraint!removal programme}
+\smallskip\noindent\emph{Proved core.}
 Theorem~\ref{thm:shifted-prefundamental-generation} proves the
-type-$A$ generation statement on the Baxter-locus seed
+type-$A$ statement on the Baxter-locus seed
 $\{V_{\omega_i}(a)\}\cup\{L^-_{i,a-\frac{1}{2}}\}$.
@@ -3320,68 +3321,77 @@
 on that seed. The issue is the proof mechanism. Step~2 uses the
-simple-root singular vector on the hyperplane $b=a-\tfrac{1}{2}$; away
-from that hyperplane, the present manuscript has no module-level
-replacement for the Baxter companion.
+rank-$1$ singular vector on the hyperplane
+\eqref{eq:baxter-spectral-constraint}; away from that hyperplane, the
+present manuscript has no module-level replacement for the Baxter
+companion.
 
-There is a second route that would remove the hyperplane from the
-generation argument itself. The natural alternative generators are not
-new finite-dimensional modules, since
+\smallskip\noindent\emph{Alternative generators and the deformation
+route.}
+The natural replacements are not new finite-dimensional modules, since
 Corollary~\ref{cor:dk2-thick-generation-all-types} already shows that
-fundamental evaluation modules generate only the evaluation core. The
-new candidates are the asymptotic objects attached to the
-Kirillov--Reshetikhin chain and the Baxter--Rees family
-$\mathcal{E}_i$ constructed later in this chapter:
+fundamental evaluations generate only the evaluation core. The real
+candidates are the asymptotic modules of the Kirillov--Reshetikhin
+tower in the sense of \cite{HJZ25,Zhang24} and the Baxter--Rees family
+$\mathcal{E}_i$ constructed later in this chapter.
 Theorem~\ref{thm:yangian-generic-boundary-fibers} identifies its
 generic fibers with Cartan-renormalized asymptotic modules and its
-boundary fiber with the negative prefundamental module. If one proves
-that the generic asymptotic fibers already lie in the localizing
-subcategory generated by evaluation modules in the completed category,
-and that this localizing subcategory is closed under specialization in
-the flat family $\mathcal{E}_i \to \mathbb{A}^1_q$, then the boundary
-module $L^-_{i,b}$ follows by degeneration, with no appeal to the
-explicit Baxter singular vector. In that form the Baxter hyperplane is
-only one visible rank-$1$ chart of a broader deformation argument.
+boundary fiber with the negative prefundamental module. A genuine
+removal of the Baxter constraint should therefore proceed by
+deformation: first show that the generic asymptotic fibers already lie
+in the localizing subcategory generated by the evaluation core inside
+the chosen completion, then prove that this localizing subcategory is
+stable under specialization along the flat family
+$\mathcal{E}_i \to \mathbb{A}^1_q$. The boundary module $L^-_{i,b}$
+would then follow by degeneration, so the explicit Baxter singular
+vector becomes only one rank-$1$ chart of the argument rather than the
+engine of the proof.
 
-This is the correct deformation of the classical generation theorem.
+\smallskip\noindent\emph{Why this is the correct deformation of the
+classical theorem.}
 In the non-shifted finite-dimensional theory, ordered tensor products
-of fundamental evaluation modules generate without spectral
-constraints. The conjectural deformation is not to perturb the singular
-vector away from $b=a-\tfrac{1}{2}$, but to pass from the
-finite-dimensional evaluation core to the asymptotic chart of the
-Kirillov--Reshetikhin tower and then specialize to the prefundamental
-boundary. The Baxter--Rees family supplies exactly such an
-interpolation; what is missing is a theorem that localizing generation
-survives along that family.
+of fundamental evaluation modules generate without any spectral
+constraint. The shifted problem should not be attacked by perturbing
+the singular vector off the hyperplane
+\eqref{eq:baxter-spectral-constraint}. The sharper deformation is to
+move from the finite-dimensional evaluation core to the asymptotic
+chart of the Kirillov--Reshetikhin tower and then specialize to the
+prefundamental boundary. The Baxter--Rees family supplies exactly that
+interpolation.
 
+\smallskip\noindent\emph{Completion boundary.}
 The completion step remains separate. Theorem~\ref{thm:shifted-prefundamental-generation}
-proves localizing generation for any presentable stable completed
-enhancement whose compact objects are the thick idempotent-complete
-closure of the shifted envelope. Corollary~\ref{cor:sectorwise-localizing-generation}
-gives a sectorwise version, and
-Remark~\ref{rem:francis-gaitsgory-mc3} records the formal
-Francis--Gaitsgory/Lurie passage from compact-core equivalences to
-cocompletions once those hypotheses are known. What is not proved on
-the live source surface is that the intended completed shifted Yangian
-category satisfies those compact/localizing hypotheses. In the present
-chapter that is exactly
-Conjecture~\ref{conj:dk-compacts-completion}. So the abstract
-formalism exists, but the Yangian-specific identification needed for
-MC3 is still part of the open packet rather than an imported theorem.
+and Corollary~\ref{cor:sectorwise-localizing-generation} show that,
+once a presentable stable completion is compactly generated by the
+shifted envelope, the localizing extension is formal; see also
+Remark~\ref{rem:francis-gaitsgory-mc3}. The shifted-Yangian inputs
+imported from \cite{HZ24,GTL17,HJZ25} control tensor products, blocks,
+and convention transfer, but they do not identify the intended
+completed shifted Yangian category as such a compactly generated
+localizing completion. In the present chapter that missing Yangian-side
+identification is exactly Conjecture~\ref{conj:dk-compacts-completion}.
 
-For types $B$, $C$, and $D$, the all-types categorical
-Clebsch--Gordan theorem removes the old minuscule obstruction, so the
-remaining issue is the Layer~3 shifted-envelope step. Type~$D$ is
-simply-laced, so no separate root-length renormalization is visible on
-the live source surface; the missing input is the lift-and-lower categorical
-statement of Conjecture~\ref{conj:rank-independence-step2}. Types
-$B$ and $C$ are different: the old folding heuristics explain why one
-expects a type-$A$ shadow, but they do not determine the spectral
-normalization of the non-simply-laced Yangian. On the live source surface
-there are two honest possibilities. Either the local rank-$1$
-constraint remains $b=a-\tfrac{1}{2}$ after the chosen normalization
-of the simple-root Yangian, or the correct hyperplane is renormalized
-rootwise by the short/long-root conventions of the Drinfeld data. The
-manuscript proves neither alternative. This is why the deformation
-route through asymptotic and Baxter--Rees objects is the cleaner
-target: it attacks the spectral-normalization question and the
-completion question at the same time.
+\smallskip\noindent\emph{Type \texorpdfstring{$B/C/D$}{B/C/D}.}
+The honest all-type analogue of the type-$A$ Baxter hyperplane is not
+a blind reuse of $b = a-\tfrac{1}{2}$. In the shifted-Yangian Baxter
+package of \cite{HZ24}, the spectral data is organized by the
+generalized simple roots
+\[
+ A_{i,a}
+ \;=\;
+ \prod_{j:\,c_{ij}\neq 0}
+ \frac{\Psi_{j,a-d_{ij}}}{\Psi_{j,a+d_{ij}}},
+ \qquad
+ d_{ij} := \frac{(\alpha_i,\alpha_j)}{2},
+\]
+so the relevant shift is root-datum dependent. After converting
+conventions, simply-laced type~$D$ has the same uniform local shift
+pattern as type~$A$; the remaining obstruction there is still the
+lift-and-lower categorical step of
+Conjecture~\ref{conj:rank-independence-step2}. Types~$B$ and~$C$ are
+different: the short/long-root asymmetry forces rootwise spectral
+renormalization, so one should expect mixed shifts rather than a single
+universal half-step. The manuscript does not yet prove a
+negative-prefundamental companion theorem with those renormalized
+shifts. This is why the asymptotic/Baxter--Rees deformation route is
+the sharper target: it attacks the spectral-normalization question and
+the completion question at the same time.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 23ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fa334b4fe68c1718688424c3d80253ef2878fbc2..fe8dc8bb648eaf33cecfebeb0313aab2c702f496
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -3311,79 +3311,89 @@
 \label{rem:mc3-baxter-constraint-removal}
 \index{MC3!Baxter constraint!removal programme}
 \index{Baxter constraint!removal programme}
+\smallskip\noindent\emph{Proved core.}
 Theorem~\ref{thm:shifted-prefundamental-generation} proves the
-type-$A$ generation statement on the Baxter-locus seed
+type-$A$ statement on the Baxter-locus seed
 $\{V_{\omega_i}(a)\}\cup\{L^-_{i,a-\frac{1}{2}}\}$.
 The issue is therefore not set-theoretic coverage of the
 prefundamental family: because $a \mapsto a-\tfrac{1}{2}$ is a
 bijection, every negative prefundamental $L^-_{i,b}$ already appears
 on that seed. The issue is the proof mechanism. Step~2 uses the
-simple-root singular vector on the hyperplane $b=a-\tfrac{1}{2}$; away
-from that hyperplane, the present manuscript has no module-level
-replacement for the Baxter companion.
+rank-$1$ singular vector on the hyperplane
+\eqref{eq:baxter-spectral-constraint}; away from that hyperplane, the
+present manuscript has no module-level replacement for the Baxter
+companion.
 
-There is a second route that would remove the hyperplane from the
-generation argument itself. The natural alternative generators are not
-new finite-dimensional modules, since
+\smallskip\noindent\emph{Alternative generators and the deformation
+route.}
+The natural replacements are not new finite-dimensional modules, since
 Corollary~\ref{cor:dk2-thick-generation-all-types} already shows that
-fundamental evaluation modules generate only the evaluation core. The
-new candidates are the asymptotic objects attached to the
-Kirillov--Reshetikhin chain and the Baxter--Rees family
-$\mathcal{E}_i$ constructed later in this chapter:
+fundamental evaluations generate only the evaluation core. The real
+candidates are the asymptotic modules of the Kirillov--Reshetikhin
+tower in the sense of \cite{HJZ25,Zhang24} and the Baxter--Rees family
+$\mathcal{E}_i$ constructed later in this chapter.
 Theorem~\ref{thm:yangian-generic-boundary-fibers} identifies its
 generic fibers with Cartan-renormalized asymptotic modules and its
-boundary fiber with the negative prefundamental module. If one proves
-that the generic asymptotic fibers already lie in the localizing
-subcategory generated by evaluation modules in the completed category,
-and that this localizing subcategory is closed under specialization in
-the flat family $\mathcal{E}_i \to \mathbb{A}^1_q$, then the boundary
-module $L^-_{i,b}$ follows by degeneration, with no appeal to the
-explicit Baxter singular vector. In that form the Baxter hyperplane is
-only one visible rank-$1$ chart of a broader deformation argument.
+boundary fiber with the negative prefundamental module. A genuine
+removal of the Baxter constraint should therefore proceed by
+deformation: first show that the generic asymptotic fibers already lie
+in the localizing subcategory generated by the evaluation core inside
+the chosen completion, then prove that this localizing subcategory is
+stable under specialization along the flat family
+$\mathcal{E}_i \to \mathbb{A}^1_q$. The boundary module $L^-_{i,b}$
+would then follow by degeneration, so the explicit Baxter singular
+vector becomes only one rank-$1$ chart of the argument rather than the
+engine of the proof.
 
-This is the correct deformation of the classical generation theorem.
+\smallskip\noindent\emph{Why this is the correct deformation of the
+classical theorem.}
 In the non-shifted finite-dimensional theory, ordered tensor products
-of fundamental evaluation modules generate without spectral
-constraints. The conjectural deformation is not to perturb the singular
-vector away from $b=a-\tfrac{1}{2}$, but to pass from the
-finite-dimensional evaluation core to the asymptotic chart of the
-Kirillov--Reshetikhin tower and then specialize to the prefundamental
-boundary. The Baxter--Rees family supplies exactly such an
-interpolation; what is missing is a theorem that localizing generation
-survives along that family.
+of fundamental evaluation modules generate without any spectral
+constraint. The shifted problem should not be attacked by perturbing
+the singular vector off the hyperplane
+\eqref{eq:baxter-spectral-constraint}. The sharper deformation is to
+move from the finite-dimensional evaluation core to the asymptotic
+chart of the Kirillov--Reshetikhin tower and then specialize to the
+prefundamental boundary. The Baxter--Rees family supplies exactly that
+interpolation.
 
+\smallskip\noindent\emph{Completion boundary.}
 The completion step remains separate. Theorem~\ref{thm:shifted-prefundamental-generation}
-proves localizing generation for any presentable stable completed
-enhancement whose compact objects are the thick idempotent-complete
-closure of the shifted envelope. Corollary~\ref{cor:sectorwise-localizing-generation}
-gives a sectorwise version, and
-Remark~\ref{rem:francis-gaitsgory-mc3} records the formal
-Francis--Gaitsgory/Lurie passage from compact-core equivalences to
-cocompletions once those hypotheses are known. What is not proved on
-the live source surface is that the intended completed shifted Yangian
-category satisfies those compact/localizing hypotheses. In the present
-chapter that is exactly
-Conjecture~\ref{conj:dk-compacts-completion}. So the abstract
-formalism exists, but the Yangian-specific identification needed for
-MC3 is still part of the open packet rather than an imported theorem.
+and Corollary~\ref{cor:sectorwise-localizing-generation} show that,
+once a presentable stable completion is compactly generated by the
+shifted envelope, the localizing extension is formal; see also
+Remark~\ref{rem:francis-gaitsgory-mc3}. The shifted-Yangian inputs
+imported from \cite{HZ24,GTL17,HJZ25} control tensor products, blocks,
+and convention transfer, but they do not identify the intended
+completed shifted Yangian category as such a compactly generated
+localizing completion. In the present chapter that missing Yangian-side
+identification is exactly Conjecture~\ref{conj:dk-compacts-completion}.
 
-For types $B$, $C$, and $D$, the all-types categorical
-Clebsch--Gordan theorem removes the old minuscule obstruction, so the
-remaining issue is the Layer~3 shifted-envelope step. Type~$D$ is
-simply-laced, so no separate root-length renormalization is visible on
-the live source surface; the missing input is the lift-and-lower categorical
-statement of Conjecture~\ref{conj:rank-independence-step2}. Types
-$B$ and $C$ are different: the old folding heuristics explain why one
-expects a type-$A$ shadow, but they do not determine the spectral
-normalization of the non-simply-laced Yangian. On the live source surface
-there are two honest possibilities. Either the local rank-$1$
-constraint remains $b=a-\tfrac{1}{2}$ after the chosen normalization
-of the simple-root Yangian, or the correct hyperplane is renormalized
-rootwise by the short/long-root conventions of the Drinfeld data. The
-manuscript proves neither alternative. This is why the deformation
-route through asymptotic and Baxter--Rees objects is the cleaner
-target: it attacks the spectral-normalization question and the
-completion question at the same time.
+\smallskip\noindent\emph{Type \texorpdfstring{$B/C/D$}{B/C/D}.}
+The honest all-type analogue of the type-$A$ Baxter hyperplane is not
+a blind reuse of $b = a-\tfrac{1}{2}$. In the shifted-Yangian Baxter
+package of \cite{HZ24}, the spectral data is organized by the
+generalized simple roots
+\[
+ A_{i,a}
+ \;=\;
+ \prod_{j:\,c_{ij}\neq 0}
+ \frac{\Psi_{j,a-d_{ij}}}{\Psi_{j,a+d_{ij}}},
+ \qquad
+ d_{ij} := \frac{(\alpha_i,\alpha_j)}{2},
+\]
+so the relevant shift is root-datum dependent. After converting
+conventions, simply-laced type~$D$ has the same uniform local shift
+pattern as type~$A$; the remaining obstruction there is still the
+lift-and-lower categorical step of
+Conjecture~\ref{conj:rank-independence-step2}. Types~$B$ and~$C$ are
+different: the short/long-root asymmetry forces rootwise spectral
+renormalization, so one should expect mixed shifts rather than a single
+universal half-step. The manuscript does not yet prove a
+negative-prefundamental companion theorem with those renormalized
+shifts. This is why the asymptotic/Baxter--Rees deformation route is
+the sharper target: it attacks the spectral-normalization question and
+the completion question at the same time.
 \end{remark}
 
 \begin{remark}[Genericity of prefundamental irreducibility at higher rank]

file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fa334b4fe68c1718688424c3d80253ef2878fbc2..fe8dc8bb648eaf33cecfebeb0313aab2c702f496
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -3311,79 +3311,89 @@
 \label{rem:mc3-baxter-constraint-removal}
 \index{MC3!Baxter constraint!removal programme}
 \index{Baxter constraint!removal programme}
+\smallskip\noindent\emph{Proved core.}
 Theorem~\ref{thm:shifted-prefundamental-generation} proves the
-type-$A$ generation statement on the Baxter-locus seed
+type-$A$ statement on the Baxter-locus seed
 $\{V_{\omega_i}(a)\}\cup\{L^-_{i,a-\frac{1}{2}}\}$.
 The issue is therefore not set-theoretic coverage of the
 prefundamental family: because $a \mapsto a-\tfrac{1}{2}$ is a
 bijection, every negative prefundamental $L^-_{i,b}$ already appears
 on that seed. The issue is the proof mechanism. Step~2 uses the
-simple-root singular vector on the hyperplane $b=a-\tfrac{1}{2}$; away
-from that hyperplane, the present manuscript has no module-level
-replacement for the Baxter companion.
+rank-$1$ singular vector on the hyperplane
+\eqref{eq:baxter-spectral-constraint}; away from that hyperplane, the
+present manuscript has no module-level replacement for the Baxter
+companion.
 
-There is a second route that would remove the hyperplane from the
-generation argument itself. The natural alternative generators are not
-new finite-dimensional modules, since
+\smallskip\noindent\emph{Alternative generators and the deformation
+route.}
+The natural replacements are not new finite-dimensional modules, since
 Corollary~\ref{cor:dk2-thick-generation-all-types} already shows that
-fundamental evaluation modules generate only the evaluation core. The
-new candidates are the asymptotic objects attached to the
-Kirillov--Reshetikhin chain and the Baxter--Rees family
-$\mathcal{E}_i$ constructed later in this chapter:
+fundamental evaluations generate only the evaluation core. The real
+candidates are the asymptotic modules of the Kirillov--Reshetikhin
+tower in the sense of \cite{HJZ25,Zhang24} and the Baxter--Rees family
+$\mathcal{E}_i$ constructed later in this chapter.
 Theorem~\ref{thm:yangian-generic-boundary-fibers} identifies its
 generic fibers with Cartan-renormalized asymptotic modules and its
-boundary fiber with the negative prefundamental module. If one proves
-that the generic asymptotic fibers already lie in the localizing
-subcategory generated by evaluation modules in the completed category,
-and that this localizing subcategory is closed under specialization in
-the flat family $\mathcal{E}_i \to \mathbb{A}^1_q$, then the boundary
-module $L^-_{i,b}$ follows by degeneration, with no appeal to the
-explicit Baxter singular vector. In that form the Baxter hyperplane is
-only one visible rank-$1$ chart of a broader deformation argument.
+boundary fiber with the negative prefundamental module. A genuine
+removal of the Baxter constraint should therefore proceed by
+deformation: first show that the generic asymptotic fibers already lie
+in the localizing subcategory generated by the evaluation core inside
+the chosen completion, then prove that this localizing subcategory is
+stable under specialization along the flat family
+$\mathcal{E}_i \to \mathbb{A}^1_q$. The boundary module $L^-_{i,b}$
+would then follow by degeneration, so the explicit Baxter singular
+vector becomes only one rank-$1$ chart of the argument rather than the
+engine of the proof.
 
-This is the correct deformation of the classical generation theorem.
+\smallskip\noindent\emph{Why this is the correct deformation of the
+classical theorem.}
 In the non-shifted finite-dimensional theory, ordered tensor products
-of fundamental evaluation modules generate without spectral
-constraints. The conjectural deformation is not to perturb the singular
-vector away from $b=a-\tfrac{1}{2}$, but to pass from the
-finite-dimensional evaluation core to the asymptotic chart of the
-Kirillov--Reshetikhin tower and then specialize to the prefundamental
-boundary. The Baxter--Rees family supplies exactly such an
-interpolation; what is missing is a theorem that localizing generation
-survives along that family.
+of fundamental evaluation modules generate without any spectral
+constraint. The shifted problem should not be attacked by perturbing
+the singular vector off the hyperplane
+\eqref{eq:baxter-spectral-constraint}. The sharper deformation is to
+move from the finite-dimensional evaluation core to the asymptotic
+chart of the Kirillov--Reshetikhin tower and then specialize to the
+prefundamental boundary. The Baxter--Rees family supplies exactly that
+interpolation.
 
+\smallskip\noindent\emph{Completion boundary.}
 The completion step remains separate. Theorem~\ref{thm:shifted-prefundamental-generation}
-proves localizing generation for any presentable stable completed
-enhancement whose compact objects are the thick idempotent-complete
-closure of the shifted envelope. Corollary~\ref{cor:sectorwise-localizing-generation}
-gives a sectorwise version, and
-Remark~\ref{rem:francis-gaitsgory-mc3} records the formal
-Francis--Gaitsgory/Lurie passage from compact-core equivalences to
-cocompletions once those hypotheses are known. What is not proved on
-the live source surface is that the intended completed shifted Yangian
-category satisfies those compact/localizing hypotheses. In the present
-chapter that is exactly
-Conjecture~\ref{conj:dk-compacts-completion}. So the abstract
-formalism exists, but the Yangian-specific identification needed for
-MC3 is still part of the open packet rather than an imported theorem.
+and Corollary~\ref{cor:sectorwise-localizing-generation} show that,
+once a presentable stable completion is compactly generated by the
+shifted envelope, the localizing extension is formal; see also
+Remark~\ref{rem:francis-gaitsgory-mc3}. The shifted-Yangian inputs
+imported from \cite{HZ24,GTL17,HJZ25} control tensor products, blocks,
+and convention transfer, but they do not identify the intended
+completed shifted Yangian category as such a compactly generated
+localizing completion. In the present chapter that missing Yangian-side
+identification is exactly Conjecture~\ref{conj:dk-compacts-completion}.
 
-For types $B$, $C$, and $D$, the all-types categorical
-Clebsch--Gordan theorem removes the old minuscule obstruction, so the
-remaining issue is the Layer~3 shifted-envelope step. Type~$D$ is
-simply-laced, so no separate root-length renormalization is visible on
-the live source surface; the missing input is the lift-and-lower categorical
-statement of Conjecture~\ref{conj:rank-independence-step2}. Types
-$B$ and $C$ are different: the old folding heuristics explain why one
-expects a type-$A$ shadow, but they do not determine the spectral
-normalization of the non-simply-laced Yangian. On the live source surface
-there are two honest possibilities. Either the local rank-$1$
-constraint remains $b=a-\tfrac{1}{2}$ after the chosen normalization
-of the simple-root Yangian, or the correct hyperplane is renormalized
-rootwise by the short/long-root conventions of the Drinfeld data. The
-manuscript proves neither alternative. This is why the deformation
-route through asymptotic and Baxter--Rees objects is the cleaner
-target: it attacks the spectral-normalization question and the
-completion question at the same time.
+\smallskip\noindent\emph{Type \texorpdfstring{$B/C/D$}{B/C/D}.}
+The honest all-type analogue of the type-$A$ Baxter hyperplane is not
+a blind reuse of $b = a-\tfrac{1}{2}$. In the shifted-Yangian Baxter
+package of \cite{HZ24}, the spectral data is organized by the
+generalized simple roots
+\[
+ A_{i,a}
+ \;=\;
+ \prod_{j:\,c_{ij}\neq 0}
+ \frac{\Psi_{j,a-d_{ij}}}{\Psi_{j,a+d_{ij}}},
+ \qquad
+ d_{ij} := \frac{(\alpha_i,\alpha_j)}{2},
+\]
+so the relevant shift is root-datum dependent. After converting
+conventions, simply-laced type~$D$ has the same uniform local shift
+pattern as type~$A$; the remaining obstruction there is still the
+lift-and-lower categorical step of
+Conjecture~\ref{conj:rank-independence-step2}. Types~$B$ and~$C$ are
+different: the short/long-root asymmetry forces rootwise spectral
+renormalization, so one should expect mixed shifts rather than a single
+universal half-step. The manuscript does not yet prove a
+negative-prefundamental companion theorem with those renormalized
+shifts. This is why the asymptotic/Baxter--Rees deformation route is
+the sharper target: it attacks the spectral-normalization question and
+the completion question at the same time.
 \end{remark}
 
 \begin{remark}[Genericity of prefundamental irreducibility at higher rank]

ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 4:15 PM.
tokens used
317,193
