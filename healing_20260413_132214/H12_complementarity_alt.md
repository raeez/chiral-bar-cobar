# H12_complementarity_alt (375s)

Rewrote the existing remark at [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3204) instead of adding a duplicate. The new version makes the index-theoretic route explicit: it defines the normalized scalar index `\chi_g^{\mathrm{sh}} = F_g/\lambda_g^{\mathrm{FP}}`, identifies it with `\kappa` via Theorems `thm:modular-characteristic` and `thm:family-index`, promotes `\kappa(\cA)+\kappa(\cA^!)` to the total Verdier-split bar-package index, and then computes `K_{\mathrm{Vir}}=13` from the self-dual fixed point `c=13` without using the termwise identity `c/2 + (26-c)/2 = 13`.

Local text checks passed, and the remark label/title are unique on the live `chapters/` surfaces across Vols I-III. I could not get a clean full build verdict because the repo currently has unrelated TeX blockers: `latexmk` with `/tmp` output cannot open included `.aux` files, and an in-worktree `pdflatex` run fails upstream on a pre-existing broken `main.aux` (`Missing \begin{document}`), plus existing duplicate-label warnings.

## Fortification Report
`prop:complementarity-landscape` scalar complementarity lane
- PRIMARY PROOF: sound
- SECONDARY PROOF: written
- TECHNIQUE: Euler characteristic / GRR family-index normalization, Verdier eigenspace splitting, self-dual fixed-point evaluation
- CONDITION STATUS: unconditional for Virasoro; all genera on the proved uniform-weight lane; genus 1 unconditional for all standard families
- CONFIDENCE: high for the Virasoro fixed-point derivation; medium if read as a genus `g>=2` argument for multi-weight families beyond the existing scalar lane


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
session id: 019d86aa-10af-71a1-8f17-c328e2a9743d
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


COMPLEMENTARITY kappa + kappa' = K — ALTERNATIVE DERIVATION.

TARGET: chapters/theory/higher_genus_complementarity.tex (add Remark)

Write an ALTERNATIVE derivation of the complementarity sum:

TECHNIQUE: Euler characteristic / index theory approach.
1. The bar-cobar adjunction pairs A with A^! in a duality.
2. kappa(A) = Euler characteristic of the shadow tower of A (suitably normalised).
3. K(A) = kappa(A) + kappa(A^!) is the Euler characteristic of the TOTAL bar complex,
   which depends only on the operad (chiral Ass), not on A.
4. For Com (classical Koszul): K = 0. For chiral Ass: K depends on the central charge.
5. The Vir self-duality at c=13 means kappa(Vir_{13}) = K(Vir)/2 = 13/2.
6. This gives K(Vir) = 13 from the SELF-DUALITY FIXED POINT, independent of computation.

Write as Remark[Alternative derivation via index theory].
mcp startup: no servers



thinking
**Reviewing manuscript modifications**

I need to modify the manuscript file by adding remarks and following AGENTS' instructions carefully. Before making any substantive mathematical edits, I’ll read CLAUDE.md and check other supporting documents. It seems necessary to assess the file exactly and determine if I should announce skills related to the edits. I'll also consider using the shell exec for file inspection, and maybe I should ask the explorer agent for any codebase questions before proceeding.
thinking
**Navigating code and files**

I need to avoid re-reading or re-searching the code that's already covered. The developer advises trusting the explorer results without needing verification. It seems I should spawn explorer agents for relevant file contexts and any duplicates while adhering to AGENTS' local reading requirements. However, I can still utilize the `exec_command` to open files for mandatory reads. I’ll focus on searching for the complementarity section, theorem, and potentially where to place remarks for the edits.
thinking
**Examining local context**

I need to read the local context surrounding `higher_genus_complementarity.tex` and verify if the theorem contains a complementarity formula. It’s essential to start with mandatory files first. The developer suggests I can parallelize file reads, so it makes sense to use `multi_tool_use.parallel` with `exec_command` for efficiency. I should also think about updating commentary and avoid web tools since I'm working with the local repo. Running a grep for verification sounds useful, especially when checking for forbidden em-dashes or syntax in LaTeX.
codex
Scope locked on `chapters/theory/higher_genus_complementarity.tex`: I’m reading the mandatory constitutional files plus the live theorem surface before writing a new alternative derivation remark, then I’ll patch the local complementarity lane and verify the surrounding claim/state coherence.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

exec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
codex
Using `beilinson-rectify` for the local theorem lane and `cross-volume-propagation` after the edit if the new derivation advertises a shared formula. I’ve finished the mandatory first reads and I’m now locating the complementarity surface, the existing `K` discussion, and the safest insertion point for the alternative proof remark.
exec
/bin/zsh -lc "rg -n \"complementarity|kappa\\+|K\\(|self-dual|index theory|Euler characteristic\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,360p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"K\\(Vir|kappa\\(Vir|complementarity|self-dual at c=13|c=13\" chapters examples appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1:\section{The complementarity theorem}
2:\label{sec:complementarity-theorem}
19:\begin{equation}\label{eq:complementarity-chapter-opening}
39:(Theorem~\ref{thm:quantum-complementarity-main}).
66: \begin{equation}\label{eq:complementarity-summary}
78: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
139:and obstructions (anomalies). The complementarity theorem gives
158:$F(\cA) \oplus F(\cA^!) = \text{universal}$. The complementarity
175:\label{rem:complementarity-transversality}
176:\index{complementarity!transversality of boundaries}%
177:\index{Dimofte!transversality and complementarity}%
197:\label{def:complementarity-complexes}
209:\begin{equation}\label{eq:complementarity-fiber}
225:The homotopy fibers~\eqref{eq:complementarity-fiber} are the
504:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
507:(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
511:the complementarity formulas below are consequences of the
516:$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
517:Table~\ref{tab:complementarity-landscape}).
520:The Heisenberg complementarity
 succeeded in 55ms:
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
 exited 2 in 50ms:
Total output lines: 1758

rg: examples: No such file or directory (os error 2)
chapters/examples/deformation_quantization.tex:817:and~\ref{thm:quantum-complementarity-main}) address the
chapters/examples/w_algebras_deep.tex:356:(Theorem~\ref{thm:quantum-complementarity-main}; this is nonzero, since the full MC elements do \emph{not} sum to zero for $\mathcal{W}$-algebras). The Miura embedding
chapters/examples/w_algebras_deep.tex:595:\index{DS complementarity defect}
chapters/examples/w_algebras_deep.tex:618:The complementarity constant for the \emph{Koszul pair}
chapters/examples/w_algebras_deep.tex:1550:The curvature complementarity
chapters/examples/w_algebras_deep.tex:1557:a complementarity formula in general: for $\mathfrak{sl}_N$
chapters/examples/w_algebras_deep.tex:1562:complementarity is instead a purely \emph{algebraic} consequence
chapters/examples/w_algebras_deep.tex:2294:\begin{proposition}[Kappa deficit and Koszul complementarity for non-principal DS]
chapters/examples/w_algebras_deep.tex:2295:\label{prop:partition-dependent-complementarity}
chapters/examples/w_algebras_deep.tex:2297:\index{complementarity!partition-dependent constant}
chapters/examples/w_algebras_deep.tex:2341:\item The \emph{Koszul complementarity sum}
chapters/examples/w_algebras_deep.tex:2346: Koszul conductor (Theorem~\textup{\ref{thm:quantum-complementarity-main}}).
chapters/examples/w_algebras_deep.tex:2355:Koszul complementarity values $\varrho_\lambda \cdot K_\lambda$.
chapters/examples/w_algebras_deep.tex:2381:(Theorem~\ref{thm:central-charge-complementarity}). For principal
chapters/examples/w_algebras_deep.tex:2413:Theorem~\ref{thm:central-charge-complementarity}: at $N = 3$ one
chapters/examples/w_algebras_deep.tex:2423:(Proposition~\ref{prop:partition-dependent-complementarity},
chapters/examples/w_algebras_deep.tex:2428:and the complementarity sum
exec
/bin/zsh -lc "rg -n \"landscape_census|Complementarity|K\\(Vir|self-dual\" chapters/theory/higher_genus_complementarity.tex chapters/connections/concordance.tex chapters examples appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"kappa\\(Vir|K\\(Vir|self-dual c=13|self-dual at c=13|K\\(BP|kappa\\+kappa'\" CLAUDE.md chapters examples appendices metadata" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: examples: No such file or directory (os error 2)
CLAUDE.md:91:- Vir: `kappa(Vir_c) = c/2`; c=13 -> 13/2 (self-dual)
CLAUDE.md:214:kappa(KM)=dim(g)(k+h^v)/(2h^v). kappa(Vir)=c/2. kappa(Heis)=k. kappa(W_N)=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j. Vir^!=Vir_{26-c}. Self-dual at c=13. kappa+kappa'=0 (KM/free), 13 (Vir). QME: hbar*Delta*S+(1/2){S,S}=0. sl_2 bar H^2=5 (not 6). Desuspension: |s^{-1}v|=|v|-1, NOT +1. eta(q)=q^{1/24}*prod(1-q^n). Bar propagator d log E(z,w): ALWAYS weight 1. Prime form: section of K^{-1/2} boxtimes K^{-1/2}. FM_n(X): blowup along diagonals, NOT complement. Grading: COHOMOLOGICAL (|d|=+1). Curved A-inf: m_1^2(a)=[m_0,a]. Bar d^2=0 always; curvature appears as m_1^2 != 0.
CLAUDE.md:223:**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).
CLAUDE.md:235:**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).
CLAUDE.md:541:**kappa** (AP1, AP9, AP20, AP24, AP48, AP136): DISTINCT per family, NEVER copy. KM=dim(g)(k+h^v)/(2h^v), Vir=c/2, W_N=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j (AP136: NOT c*H_{N-1}), Heis=k. Always qualify: kappa^{KM}, kappa^{Vir}. Complementarity: kappa+kappa'=0 (KM/free), 13 (Vir), NOT universal. State WHICH algebra: intrinsic vs kappa_eff=kappa(matter)+kappa(ghost) vs kappa(B) where B=A^!. **AP1 operational mandate**: before writing ANY kappa formula, (a) read landscape_census.tex for that family, (b) evaluate at k=0 and k=-h^v, (c) cross-check compute/. Writing kappa from memory is FORBIDDEN.
CLAUDE.md:563:AP8: NEVER "self-dual" unqualified. Specify which duality, which c. Virasoro self-dual at c=13.
CLAUDE.md:581:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
CLAUDE.md:658:  NOT kappa(Vir) = c       NOT kappa(W_N) = c*H_{N-1}
chapters/theory/higher_genus_modular_koszul.tex:20090:%: kappa(Vir_c) = c/2 from landscape_census.tex:620; c=0 -> 0, c=13 -> 13/2 verified.
chapters/theory/higher_genus_modular_koszul.tex:20247:%: kappa(Vir_c) = c/2 from landscape_census.tex:620; c=0 -> 0, c=13 -> 13/2 verified.
chapters/connections/arithmetic_shadows.tex:6:%: kappa(Heis) = k, kappa(Vir) = c/2, kappa(KM) = dim(g)(k+h^v)/(2h^v)
chapters/connections/arithmetic_shadows.tex:29:%: kappa(Vir) = c/2 from landscape_census.tex; c=0 -> 0, c=13 -> 13/2 verified.
 exited 2 in 52ms:
Total output lines: 899

rg: examples: No such file or directory (os error 2)
chapters/connections/concordance.tex:47:\textbf{C} & Complementarity
chapters/connections/concordance.tex:202:\item \textbf{Complementarity}
chapters/connections/concordance.tex:520:FG establish $\chirCom$-$\chirLie$ duality. We show this is derived from the more fundamental $\chirAss$-$\chirAss$ self-duality via the deformation Pois → Ass.
chapters/connections/concordance.tex:550:\begin{theorem}[FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality; \ClaimStatusProvedHere]\label{thm:fg-from-assch}
chapters/connections/concordance.tex:551:The Francis--Gaitsgory $\chirCom$-$\chirLie$ duality is the associated graded of the $\chirAss$ self-duality under the PBW filtration. Precisely: for a quadratic $\Einf$-chiral algebra $\cA$, the $\chirAss$ bar complex $\bar{B}_{\chirAss}(\cA)$ carries a filtration $F_\bullet$ (induced by the symmetrization degree of the $\Sigma$-action on $C_n(X)$) such that:
chapters/connections/concordance.tex:2076: critical locus governing simultaneous self-dual deformations,
chapters/connections/concordance.tex:2756:the shadow growth rate is self-dual ($\rho \approx 0.467$).
chapters/connections/concordance.tex:3067:\item \emph{Critical level}: $V_{-h^\vee}(\fg)$ is uncurved ($\kappa=0$), self-dual under the Feigin--Frenkel involution ($k=-h^\vee$ is a fixed point of $k \mapsto -k-2h^\vee$), center~$= \mathfrak{z}(\widehat{\fg})$ (Theorem~\ref{thm:critical-level-cohomology}).
chapters/connections/concordance.tex:5939: (the spectral discriminant is self-dual);
chapters/connections/concordance.tex:6003:the spectral discriminant is self-dual. For
chapters/connections/concordance.tex:6670:\begin{remark}[The self-dual central charge $c = 13$]
chapters/connections/concordance.tex:6672:\index{Virasoro algebra!self-duality at $c=13$!concordance}%
chapters/connections/concordance.tex:6673:\index{holographic modular Koszul datum!self-dual point}%
chapters/connections/concordance.tex:6685: family is self-dual under Koszul duality.
chapters/connections/concordance.tex:6687:\item \emph{Full tower self-duality}
chapters/connections/concordance.tex:6688: \textup{(}Proposition~\textup{\ref{prop:c13-full-self-duality}}\textup{)}.
chapters/connections/concordance.tex:6721:The self-dual point $c = 13$ must be distinguished from the

thinking
**Inspecting target file remarks**

I find it interesting that the target file has a remark labeled "Alternative derivation via index theory" around line 3204. I'll need to check if this matches the user's request and possibly consider editing the current remark instead of just adding a new one. It's important to read the surrounding lines to see if the existing remark is incomplete or lacks rigor. I should also look into the complementarity-landscape context and use specific lines for further inspection.
codex
The target surface already contains a remark with the requested title, so I’m checking whether it actually satisfies the requested Euler-characteristic derivation or whether it needs replacement. Next step is a tight read of the landscape proposition and the existing index-theory remark around that insertion point.
exec
/bin/zsh -lc "sed -n '3038,3275p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1260,1325p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 69ms:

\begin{proof}
Combine $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) with $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}(ii)).
\end{proof}

\begin{remark}[Reading the table]\label{rem:reading-master-table}
Three structural features are visible from the table:
\begin{enumerate}
\item \emph{Complementarity.}
 Every $c + c'$ entry is independent of the level~$k$: it depends
 only on the root datum of~$\fg$.
 This is the content of Theorem~\ref{thm:central-charge-complementarity}.
\item \emph{Critical level.}
 Setting $\kappa(\cA) = 0$ (i.e., $t = k + h^\vee = 0$)
 simultaneously forces $\operatorname{obs}_g = 0$
 for all genera: the bar complex becomes \emph{uncurved}, and
 the Feigin--Frenkel center $\mathfrak{z}(\widehat{\fg}_{-h^\vee})$
 emerges as the degree-zero cohomology.
\item \emph{Free fields.}
 The exact Koszul dualities ($\psi \leftrightarrow \gamma$,
 succeeded in 85ms:
\index{complementarity!landscape|textbf}
\index{Koszul conductor|textbf}
\index{anomaly ratio|textbf}

The complementarity sum $\kappa(\cA) + \kappa(\cA^!)$ is a
level-independent invariant for every standard family
(Theorem~\ref{thm:complementarity-root-datum}). We collect the
full data here.

\begin{proposition}[Complementarity landscape; \ClaimStatusProvedHere]
\label{prop:complementarity-landscape}
\index{complementarity!landscape}
Let $(\cA, \cA^!)$ be a chiral Koszul pair from the standard
landscape. The complementarity sum
$\kappa(\cA) + \kappa(\cA^!)$ is determined as follows.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Free fields.}\;
 For the Heisenberg~$\cH_k$, the free fermion, the
 $\beta\gamma$~system at conformal weight~$\lambda$, and
 lattice vertex algebras~$V_\Lambda$:
exec
/bin/zsh -lc "sed -n '1660,1715p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3718,3755p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \textit{Class $\mathbf{L}$: Epstein zeta degenerate
 ($\Delta = 0$, $\operatorname{disc} = 0$)}} \\
\hline
$\widehat{\fg}_k$ (generic)
 & $\mathbf{L}$ & $0$ & $\bQ$ & --- & $\zeta(s)$ \\
\hline
$\widehat{\mathfrak{sl}}_2$ at $k = 1$
 & $\mathbf{L}$ & $0$ & $\bQ$ & --- & $\zeta(s)$ \\
\hline
\multicolumn{6}{|c|}{%
 \textit{Class $\mathbf{C}$: stratum separation
 ($\kappa = 0$ on charged stratum)}} \\
\hline
$\beta\gamma$
 & $\mathbf{C}$ & \textsuperscript{$\ast$}
 & --- & --- & --- \\
\hline
\multicolumn{6}{|c|}{%
 \textit{Class $\mathbf{M}$: genuine imaginary quadratic field
 ($\Delta \neq 0$)}} \\
 succeeded in 51ms:
}
\end{table}

\begin{remark}[Complementarity at each genus]\label{rem:genus-complementarity}
\index{complementarity!genus-g}
By Theorem~\ref{thm:quantum-complementarity-main},
$\operatorname{obs}_g(\cA) + \operatorname{obs}_g(\cA^!)
 = \lambda_g \cdot (\kappa + \kappa')$.
For affine Kac--Moody algebras,
$\kappa(\widehat{\fg}_k) + \kappa(\widehat{\fg}_{-k-2h^\vee}) = 0$
(the shifted level $t = k + h^\vee$ maps to $-t$, and
$\kappa = td/(2h^\vee)$ is linear in~$t$).
Hence $\operatorname{obs}_g(\widehat{\fg}_k)
 + \operatorname{obs}_g(\widehat{\fg}_{k'}) = 0$.
For $\widehat{\mathfrak{sl}}_2$:
$3(k{+}2)/96 + 3(-k{-}2)/96 = 0$.
At the critical level $k = -h^\vee$, both $\kappa = 0$ and $\kappa' = 0$,
so $\operatorname{obs}_g = \operatorname{obs}_g' = 0$.

For $\mathcal{W}$-algebras, $\kappa + \kappa' \neq 0$ in general:



thinking
**Considering code commentary**

I'm thinking about including commentary in the PE-8 after sharing the formula. I should find the line related to the landscape census, particularly for the Vir c formula and possibly complementarity. There's a specific line, like 1689, that might be relevant here. I need to ensure I provide clear guidance and context in the template to assist users in understanding this better. I'll keep that in mind as I proceed!
thinking
**Evaluating mathematical remarks**

I'm reviewing how to search for line numbers in the landscape census regarding Vir row and possibly K_N. I could use nl -ba for this. Maybe I should check for duplicates across versions, but with the mathematical wording about complementarity, I might not need propagation since the formula hasn't changed. Since the user's specific about the file, I shouldn't overcomplicate things. It looks like a local proof is all that's needed for now!
thinking
**Refining existing remarks**

I’m considering whether the existing remark should be replaced with a stronger derivation, possibly editing it to align better. Maybe I can reference "Remark[Alternative derivation via index theory]" directly. I should read the existing proof for any weaknesses. The user might want to clarify the "ALTERNATIVE DERIVATION" of the complementarity sum in this remark. I may need to strengthen the content by incorporating operad-dependence and clearer references to Vir's fixed point. Plus, perhaps I should check for cross-references with the self-dual complementarity and mention relevant theorems.
codex
I have the insertion block: the file already carries an index-theory remark, but it stops short of the operad-level interpretation you asked for. I’m now verifying the exact supporting labels for the normalized Euler-characteristic argument, then I’ll rewrite that remark rather than add a duplicate.
exec
/bin/zsh -lc "rg -n \"label\\{thm:chiral-koszul-duality\\}|label\\{thm:verdier-bar-cobar\\}|Verdier bar-cobar|chiral-koszul-duality\" chapters/theory chapters/examples appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}|family index|normalized genus-\\"'$g'"\\"'$ index|F_g'"\\(\\cA\\)|lambda_g\" chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/koszul_reference.tex:90:duality (Theorem~\ref{thm:e1-chiral-koszul-duality}) genus by genus, with
chapters/examples/lattice_foundations.tex:2140:construction of Theorem~\ref{thm:e1-chiral-koszul-duality}, indexed by
chapters/examples/lattice_foundations.tex:3168:(Theorem~\ref{thm:e1-chiral-koszul-duality}).
chapters/examples/lattice_foundations.tex:3217:(Theorem~\ref{thm:e1-chiral-koszul-duality}) and the self-duality of
chapters/examples/lattice_foundations.tex:3944:Theorem~\ref{thm:e1-chiral-koszul-duality}). The Verdier
chapters/examples/beta_gamma.tex:431:which is Koszul by Theorem~\ref{thm:chiral-koszul-duality}), acyclicity
chapters/examples/landscape_census.tex:1059: \textup{(}Theorems~\ref{thm:e1-chiral-koszul-duality},
chapters/examples/landscape_census.tex:1460:Theorem~\ref{thm:e1-chiral-koszul-duality});
chapters/examples/w_algebras.tex:397:For $k \neq -h^\vee$, the W-algebra has non-trivial curvature $m_0 \neq 0$ (Theorem~\ref{thm:w-bar-curvature}). The bar-cobar adjunction of Theorem~\ref{thm:e1-chiral-koszul-duality} gives a curved $A_\infty$ quasi-isomorphism:
chapters/examples/yangians_drinfeld_kohno.tex:664:\textbf{DK-0/1}: chain-level braided bar-cobar (Theorems~\ref{thm:e1-chiral-koszul-duality}--\ref{thm:derived-dk-yangian}) and evaluation-locus factorization DK (Theorem~\ref{thm:factorization-dk-eval}), proved. \textbf{DK-2/3}: the type-$A$ thick-generation input is proved, but the promotion beyond generators is only conditional on the ambient extension/comparison package of Theorem~\ref{conj:dk-fd-typeA}; a separate sectorwise-convergence route exists at the H-level for all types (Corollary~\ref{cor:dk23-all-types}). Category-$\mathcal{O}$ extension remains conjectural (Conjecture~\ref{conj:full-derived-dk}; see Corollary~\ref{cor:dk-partial-conj}). \textbf{DK-4}: structural framework proved (MC4 closed, Theorem~\ref{thm:completed-bar-cobar-strong}); algebraic identification $\varprojlim \mathfrak{g}_N \cong Y^{\mathrm{dg}}_\cA$ remains open (Conjecture~\ref{conj:dk4-inverse-limit}). \textbf{DK-5}: conjectural (Conjecture~\ref{conj:full-dk-bridge}; see Remark~\ref{rem:yangian-dk23-inputs} for exact inputs). \ifannalsedition\else
chapters/examples/yangians_drinfeld_kohno.tex:903:Theorem~\ref{thm:e1-chiral-koszul-duality} gives the
chapters/theory/bar_cobar_adjunction_inversion.tex:1814:Theorem~\ref{thm:chiral-koszul-duality};
chapters/theory/bar_cobar_adjunction_inversion.tex:1914:\textup{(}equivalently, Theorem~\textup{\ref{thm:chiral-koszul-duality}}
chapters/examples/yangians_computations.tex:1720:\textup{(}Theorem~\textup{\ref{thm:e1-chiral-koszul-duality})}.
chapters/examples/yangians_foundations.tex:697:Theorem~\ref{thm:e1-chiral-koszul-duality} then applies:
chapters/examples/yangians_foundations.tex:891:equivalence by Theorem~\ref{thm:e1-chiral-koszul-duality}, and the
chapters/examples/toroidal_elliptic.tex:243:(Theorem~\ref{thm:e1-chiral-koszul-duality}) applies to the
chapters/examples/toroidal_elliptic.tex:266:\item \emph{RTT presentation.} By $\Eone$-chiral Koszul duality (Theorem~\ref{thm:e1-chiral-koszul-duality}), the dual has $R$-matrix $R(u;q,t)^{-1} = R(u;q^{-1},t^{-1})$ (Ding--Iohara inversion; cf.\ Theorem~\ref{thm:yangian-koszul-dual}).
chapters/theory/higher_genus_foundations.tex:1963:Theorem~\ref{thm:chiral-koszul-duality}. Then:
chapters/theory/higher_genus_foundations.tex:2050:This filtration satisfies the hypotheses of Theorem~\ref{thm:convergence-filtered}: it is complete and separated (conformal weight is bounded below), compatible with chiral operations ($\mu(F_i \otimes F_j) \subset F_{i+j}$), and has associated graded $\mathrm{gr}\,W_N \cong$ free field algebra (Koszul by Theorem~\ref{thm:chiral-koszul-duality}).
 exited 2 in 50ms:
rg: regex parse error:
    (?:label\{thm:family-index\}|family index|normalized genus-$g$ index|F_g\(\cA\)|lambda_g)
                                                                              ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3200,3270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '615,635p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   615	$\widehat{\mathfrak{sl}}_2$ & $\tfrac{9}{4}$ & $\tfrac{3}{32}$ & $\tfrac{7}{2560}$ & scalar \\
   616	\hline
   617	$\widehat{\mathfrak{sl}}_3$ & $\tfrac{16}{3}$ & $\tfrac{2}{9}$ & $\tfrac{7}{1080}$ & scalar \\
   618	\hline
   619	$\widehat{\mathfrak{so}}_{5}$ (type $B_2$) & $\tfrac{20}{3}$ & $\tfrac{5}{18}$ & $\tfrac{7}{864}$ & scalar \\
   620	\hline
   621	$\widehat{\mathfrak{sp}}_{4}$ (type $C_2$) & $\tfrac{20}{3}$ & $\tfrac{5}{18}$ & $\tfrac{7}{864}$ & scalar \\
   622	\hline
   623	$\widehat{\mathfrak{so}}_{8}$ (type $D_4$) & $\tfrac{49}{3}$ & $\tfrac{49}{72}$ & $\tfrac{343}{17280}$ & scalar \\
   624	\hline
   625	$\widehat{G}_2$ & $\tfrac{35}{4}$ & $\tfrac{35}{96}$ & $\tfrac{49}{4608}$ & scalar \\
   626	\hline
   627	$\widehat{F}_4$ & $\tfrac{260}{9}$ & $\tfrac{65}{54}$ & $\tfrac{91}{2592}$ & scalar \\
   628	\hline
   629	$\widehat{E}_6$ & $\tfrac{169}{4}$ & $\tfrac{169}{96}$ & $\tfrac{1183}{23040}$ & scalar \\
   630	\hline
   631	$\widehat{E}_7$ & $\tfrac{2527}{36}$ & $\tfrac{2527}{864}$ & $\tfrac{17689}{207360}$ & scalar \\
   632	\hline
   633	$\widehat{E}_8$ & $\tfrac{1922}{15}$ & $\tfrac{961}{180}$ & $\tfrac{6727}{43200}$ & scalar \\
   634	\hline
 succeeded in 52ms:
  3200	\bottomrule
  3201	\end{tabular}
  3202	\end{table}
  3203	
  3204	\begin{remark}[Alternative derivation via index theory]
  3205	\label{rem:complementarity-index-theory}
  3206	\index{complementarity!index-theoretic derivation}
  3207	\index{index theory!complementarity}
  3208	There is a second derivation of the complementarity sum that does not
  3209	add the two explicit $\kappa$-formulas term by term. The bar-cobar
  3210	package
  3211	\textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
  3212	Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
  3213	places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
  3214	$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
  3215	with Verdier eigenspace splitting
  3216	\[
  3217	\mathbf{C}_g(\cA)
  3218	\;\simeq\;
  3219	\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
exec
/bin/zsh -lc "rg -n \"Vir_c|c/2|self-dual point is|K_2 = 26|c_\\* = 13\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '680,745p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
33:and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
79: & $c/2$ & PH \\
142: & $1 - \dfrac{6(k{+}1)^2}{k{+}2}$ & $26$ & $c/2$ & PH \\[4pt]
463: & $(c/2)/z^3 + 2T/z$
468: & $(c/2)/z^3 + 2T/z$
637:$\mathrm{Vir}_{c}$ & $c/2$ & $c/48$ & $7c/11520$ & scalar \\
731:$K_2 = 26$, $K_3 = 100$, $K_4 = 246$, $K_5 = 488$.
737:since $\dim V_1^\natural = 0$ forces $\kappa = c/2 = 12$
844:$\kappa(V^\natural) = c/2 = 12$.
1203:$F_1(\mathcal{H}_1) = 1/24 = c/24$, precisely the conformal anomaly coefficient
1204:$q^{-c/24}$ in the torus partition function $Z(\tau) = q^{-c/24}\sum_h d(h)\,q^h$.
1207:In general, $F_1 = \kappa/24$ differs from the conformal anomaly $c/24$ by the ratio $\kappa/c$, which is~$1$ for the Heisenberg algebra but varies for other algebras.
1221:The anomaly ratio $\varrho(\cA) := \kappa(\cA)/c(\cA)$ measures how much of the conformal anomaly survives from the Lie bracket's cyclic deformation. For the rank-$d$ Heisenberg algebra $\cH_1^{\oplus d}$ at level~$1$, $\varrho = d/d = 1$: the Polyakov formula $F_1 = c/24$ and the shadow formula $F_1 = \kappa/24$ coincide because $\kappa = c = d$. For all other standard families, $\varrho \neq 1$:
1228:$\mathrm{Vir}_c$ & $c$ & $c/2$ & $1/2$ \\
1286: $\kappa(bc) = c/2$ are nonzero (they measure the
1309:The first values are: $K_2 = 26$, $K_3 = 100$, $K_4 = 246$, $K_5 = 488$. In general $K_N = 4N^3 - 2N - 2$ (equivalently $K_N = 2(N-1)(2N^2+2N+1)$).
1413:(\S\ref{sec:virasoro-genus-one-pipeline}, $c + c' = 26$, $\kappa = c/2$)
3412:\item the quartic pole $\frac{c/2}{(z-w)^4}$ (central,
3656: & $c/2$
3702: & $c/2$
 succeeded in 52ms:
   680	\hline
   681	\textbf{Algebra $\cA$}
   682	 & \textbf{Class}
   683	 & $\boldsymbol{S_3}$
   684	 & $\boldsymbol{S_4}$
   685	 & $\boldsymbol{\Delta = 8\kappa S_4}$
   686	 & $\boldsymbol{\rho}$
   687	 & $\boldsymbol{\kappa{+}\kappa'}$ \\
   688	\hline
   689	$\mathcal{H}_k$ & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
   690	\hline
   691	Free fermion & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
   692	\hline
   693	$bc$ ($\lambda$) & C & $0$ & $\neq 0$ & $0^\dagger$ & $0^\dagger$ & $0$ \\
   694	\hline
   695	$V_\Lambda$ (rank $d$) & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
   696	\hline
   697	$\widehat{\fg}_k$ & L & $\neq 0$ & $0$ & $0$ & $0$ & $0$ \\
   698	\hline
   699	$\beta\gamma_\lambda$ & C & $0$ & $\neq 0$ & $0^\dagger$ & $0^\dagger$ & $0$ \\
exec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}|label\\{thm:modular-characteristic\\}|F_g\\(\\cA\\)|lambda_g"'^{'"\\\\mathrm\\{FP\\}}|family-index\" chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label\{thm:family-index\}|label\{thm:modular-characteristic\}|F_g\(\cA\)|lambda_g^{\mathrm\{FP\}}|family-index)
                                                                          ^^
error: unrecognized escape sequence


thinking
**Considering query simplification**

I’m thinking that I might need to make the queries simpler. It looks like using a fixed string multiple might not be easily doable. I could try something like using `rg` with the pattern "thm:family-index|thm:modular-characteristic|thm:family-index" to see if that works better. The goal is to simplify things while still getting the right information, so let’s explore this approach further!
thinking
**Checking theorem labels**

I need to look for the exact label of the theorem. Maybe I should check if I can use regular expressions with fixed strings and avoid backslashes. It might help to search specifically for "thm:family-index" and similar terms to see if I can find what I’m looking for. Let’s see if that approach leads me to the right information!
codex
I’ve confirmed the current remark is the right place and identified the main gap: it mentions a normalized index, but it does not say cleanly enough that the total index is an operadic invariant of the full bar package. I’m checking the exact support for the `F_g/\lambda_g` normalization before patching that remark into the requested fixed-point derivation.
exec
/bin/zsh -lc "rg -n \"thm:family-index|thm:modular-characteristic|lambda_g\\"'^'"\\{\\\\mathrm\\{FP\\}\\}|F_g\\(\" chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:family-index\\}|label\\{thm:family-index\\}|label\\{thm:modular-characteristic\\}\" chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:thm:family-index|thm:modular-characteristic|lambda_g\^\{\mathrm\{FP\}\}|F_g\()
                                                               ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2844:\label{thm:modular-characteristic}
exec
/bin/zsh -lc "sed -n '2520,2615p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = 0
\end{equation}
meaning the center acts trivially on moduli space cohomology.
\end{corollary}

\begin{proof}[Proof of Corollary~\ref{cor:vanishing-quantum}]
\emph{First statement}: By the decomposition theorem:
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


thinking
**Searching for family index theorem**

I need to find the exact location of the family index theorem, and maybe I can start by searching for "thm:family-index." It seems like a good idea to keep the search simpler, so I’ll focus on that. I'll check various resources to pinpoint where I can get the right information! Let’s see what I can dig up on this topic. Finding the exact details will be really helpful!
codex
The label check is enough for the patch: `thm:modular-characteristic` is live, and the self-dual halving block gives the fixed-point support at `c=13`. I’m now preparing the rewrite and will include the pre-edit verification block before touching the file.
exec
/bin/zsh -lc "sed -n '2838,2898p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:family-index' chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/landscape_census.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'F_g\\(|\\\\lambda_g|uniform-weight lane|F_1 = \\\\kappa/24|obs_g\\(\\\\cA\\)=\\\\kappa' chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
entire genus tower (the spectral discriminant~$\Delta_\cA$,
periodicity profile~$\Pi_\cA$, and full MC
class~$\Theta_\cA$ require data beyond~$\kappa$;
see Definition~\ref{def:full-modular-package}).

\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
\label{thm:modular-characteristic}
\index{modular characteristic theorem|textbf}
\index{kappa@$\kappa$!as first characteristic number|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $\cA$ be a modular Koszul chiral algebra
(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
characteristic package
(Definition~\ref{def:scalar-modular-package}) is controlled by one
number, the genus-$1$ curvature coefficient
$\kappa(\cA) \in \mathbb{C}$. More precisely:

\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 50ms:
chapters/connections/concordance.tex:4811: & genus-$1$ unconditional; family-index routed downstream & genus-$1$ universal & \ref{thm:family-index} \\[2pt]
chapters/connections/concordance.tex:6029:\ClaimStatusProvedHere]\label{thm:family-index}
chapters/connections/concordance.tex:6114:\text{Theorem~\ref{thm:family-index}}.
chapters/connections/concordance.tex:6116:Thus Theorem~\ref{thm:family-index} is a downstream
chapters/connections/concordance.tex:6328:\text{Theorem~\ref{thm:family-index}}.
chapters/connections/concordance.tex:6330:Theorem~\ref{thm:family-index} is the downstream GRR
chapters/connections/concordance.tex:6355:Theorem~\ref{thm:family-index} synthesizes the preceding results:
chapters/theory/higher_genus_complementarity.tex:3228:integral of Theorem~\textup{\ref{thm:family-index}}. By the family
chapters/theory/higher_genus_complementarity.tex:3244:Theorem~\textup{\ref{thm:family-index}} can shift the total index,
chapters/theory/higher_genus_modular_koszul.tex:2917:Theorem~\ref{thm:family-index} is downstream again: it is the
chapters/theory/higher_genus_modular_koszul.tex:2931:Theorem~\ref{thm:family-index}.
chapters/theory/higher_genus_modular_koszul.tex:3008:virtual bar family. Theorem~\ref{thm:family-index} is therefore the
chapters/theory/higher_genus_modular_koszul.tex:3024:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:4774: \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:4822:(Theorem~\ref{thm:family-index}) of the scalar series already
chapters/theory/higher_genus_modular_koszul.tex:9873:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:14308:(Theorem~\ref{thm:family-index}).
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:2210:F_g(\cA)
chapters/theory/higher_genus_complementarity.tex:2212:\kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
chapters/theory/higher_genus_complementarity.tex:2218:uniform-weight lane. Therefore the exact scalar condition for the
chapters/theory/higher_genus_complementarity.tex:2220:$\kappa(\cA)\lambda_g^{\mathrm{FP}}$ term is not uniform-weight by
chapters/theory/higher_genus_complementarity.tex:2647:\lambda_g$ At $k = -h^\vee$, the coefficient $k + h^\vee$ vanishes. The
chapters/theory/higher_genus_complementarity.tex:3225:\frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
chapters/theory/higher_genus_complementarity.tex:3227:where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
chapters/theory/higher_genus_complementarity.tex:3229:index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
chapters/theory/higher_genus_complementarity.tex:3808: $\kappa(\cA) \cdot \lambda_g \in H^*(\overline{\mathcal{M}}_g)$
chapters/theory/higher_genus_complementarity.tex:4430:The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.
chapters/theory/higher_genus_complementarity.tex:5963:isomorphism $\lambda_g^{\otimes c/2} \cong
chapters/theory/higher_genus_complementarity.tex:6045:$\mathrm{obs}_g = \kappa \cdot \lambda_g$ is proved , is controlled by the same data.
chapters/theory/higher_genus_complementarity.tex:6340:lifting the uniform-weight scalar shadow $\kappa(\cA)\sum_{g \geq 1}\lambda_g$,
chapters/theory/higher_genus_modular_koszul.tex:488:$\mathrm{obs}_g = \kappa(\cA) \cdot \lambda_g$ for
chapters/theory/higher_genus_modular_koszul.tex:2621:\item The \emph{genus tower} $\{F_g(\cA)\}_{g \geq 1}$, the sequence
chapters/theory/higher_genus_modular_koszul.tex:2714:\index{uniform-weight lane|see{scalar lane}}
chapters/theory/higher_genus_modular_koszul.tex:2716:\emph{uniform-weight lane} (or \emph{scalar lane}) if every
chapters/theory/higher_genus_modular_koszul.tex:2725:On the scalar lane, $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$
chapters/theory/higher_genus_modular_koszul.tex:2781: \sum_{g \geq 1} \kappa(\cA)\lambda_g,
chapters/theory/higher_genus_modular_koszul.tex:2862: $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$


thinking
**Investigating theorem dependencies**

I need to inspect the family-index theorem to see if it's necessary, but it seems like the existing label might be good enough. I could search for more rigorous dependencies on the operad and review the concordance related to the family-index theorem. The user's target points are explicit, so I need to verify the claim that it "depends only on operad (chiral Ass), not A" is safe. I should check the evidence in the repository and search for relevant terms like "operad."
thinking
**Exploring mathematical concepts**

I’m thinking there might be a direct statement within the higher genus modular Koszul framework regarding the virtual bar family and the family index being tied to the chiral bar family. It could be independent but perhaps connected through some trace. I should take a closer look at the specifics between lines 2998 and 3030 to clarify these relationships. Let's investigate this further!
codex
The scalar support is now pinned down: `thm:modular-characteristic` gives `F_g = \kappa \lambda_g^{FP}` on the proved uniform-weight lane, and `thm:self-dual-halving` gives the fixed-point halving at `c=13`. I’m doing one more local read on the family-index discussion to phrase the operad-dependence carefully enough that it stays within the proved surface.
exec
/bin/zsh -lc "sed -n '2988,3035p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6020,6068p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\subsection{The index theorem for genus expansions}

The appearance of the $\hat{A}$-genus in the Heisenberg genus
expansion (Theorem~\ref{thm:universal-generating-function})
and the Bernoulli asymptotics of $F_g(\cA)$ are not coincidental:
they are the output of a Grothendieck--Riemann--Roch computation
on the universal curve.

\begin{theorem}[Family index theorem for genus expansions;
\ClaimStatusProvedHere]\label{thm:family-index}
\index{index theorem!modular deformation|textbf}
\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
\overline{\mathcal{M}}_g$ be the universal curve with relative
dualizing sheaf~$\omega_\pi$, and let
$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
The following holds for uniform-weight modular Koszul algebras
at all genera; the genus-$1$ statements are unconditional for
all families, including multi-generator.
 succeeded in 51ms:
Conjecture~\ref{conj:categorical-modular-kd}).
\end{remark}

\begin{remark}[Proof routing for Theorem~D;
Convention~\ref{conv:proof-architecture}]
\label{rem:theorem-d-model}
\index{modular characteristic theorem!model presentation}
\[
\Theta_\cA \text{ and its shadow tower}
\Longrightarrow
\mathrm{obs}_g=\kappa\cdot\lambda_g
\Longrightarrow
\sum_{g \ge 1} F_g x^{2g}
=
\kappa\cdot(\hat{A}(ix)-1)
\]
The bar-intrinsic shadow tower is the common source.
The first implication is the scalar-trace identification of
Theorem~\ref{thm:genus-universality}; the second is the downstream
GRR/family-index identification of the same scalar series on the
exec
/bin/zsh -lc 'rg -n "depends only on the operad|operad.*index|Verdier-self-dual bar package|total bar complex" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:843:the genus filtration on the total bar complex
chapters/theory/higher_genus_complementarity.tex:3241:characteristic of the total Verdier-self-dual bar package. Over a



thinking
**Clarifying operad dependencies**

The user's point is clear: it depends only on the operad (chiral Ass) and not on A. I might need to phrase it as "the total index is the index of the ambient \chirAss-bar package; equivalently, it is based solely on the \chirAss-duality class and not on any specific member A or A^!". This seems like a safer and more acceptable way to present the information, focusing on the duality class instead of all A.
thinking
**Rewriting theorem remarks**

I’m working on simplifying remarks to match six concise bullet points. First, I’ll state that the bar-cobar and Verdier theorems pair A with A! within a single total complex. Next, I’ll define the normalized index, linking it to the Euler characteristic. Then, I’ll summarize that the total index relates to both parts of the ambient package. Lastly, for curves, I’ll highlight the role of the central charge in the Virasoro context while ensuring clarity in my wording.
thinking
**Clarifying terminology**

I’m pondering the best way to refer to the "suitably normalized Euler characteristic of the shadow tower." Perhaps using "scalar Euler characteristic" would be clearer. I should be careful not to overuse the term "total bar complex," especially if it’s really an ambient complex. But since the user specifically mentions "total bar complex," I want to respect that request while ensuring my language is precise and easily understood. It's all about clarity!
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '633,640p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   633	$\widehat{E}_8$ & $\tfrac{1922}{15}$ & $\tfrac{961}{180}$ & $\tfrac{6727}{43200}$ & scalar \\
   634	\hline
   635	\multicolumn{5}{|c|}{\textit{$\mathcal{W}$-Algebras}} \\
   636	\hline
   637	$\mathrm{Vir}_{c}$ & $c/2$ & $c/48$ & $7c/11520$ & scalar \\
   638	\hline
   639	$\mathcal{W}_{3,c}$ & $5c/6$ & $5c/144$ & $7c/6912$ & multi \\
   640	\hline


thinking
**Exploring modular deformation complex**

I'm looking to define the "modular deformation complex" and wonder if it relates to K-theory classes from the Hodge bundle. It's definitely not an actual bar complex, but I can discuss pushing forward the index of the total bar package via GRR. 

I might phrase it like: "Theorem family-index identifies \(F_g\) with the GRR pushforward of the K-theory class." The normalized index of the scalar shadow is safer. I think I should use "normalized index" instead of "Euler characteristic" in key sentences, while still mentioning "Euler characteristic" early on since the user requested it.
thinking
**Clarifying index terminology**

To clarify, I want to say: "Thus, \(\kappa(\cA)\) is the normalized scalar index of the shadow tower of \(\cA\)." I’ll note that "the total complementarity constant is the normalized index of the Verdier-self-dual total package." 

I think I should mention "Euler characteristic" once for clarity: "equivalently, the scalar Euler characteristic extracted by GRR." Also, I need to introduce the term "chirAss-duality orbit." Finally, I should explicitly state, "For Com classical Koszul: K=0." That will improve understanding!
codex
```text
PE-2: kappa formula write
family: Virasoro
kappa written: \kappa(\mathrm{Vir}_{13}) = 13/2 and K_{\mathrm{Vir}} = 2\kappa(\mathrm{Vir}_{13})
census: chapters/examples/landscape_census.tex:637 = \kappa(\mathrm{Vir}_c)=c/2  match? Y
at c=0: 0 expected 0  at c=13: 13/2 expected 13/2
AP136 (W_N N=2): \varrho_2=H_2-1=1/2, hence \kappa(\mathcal W_2)=c/2 expected c/2
wrong variants avoided: NOT c, NOT H_{N-1}, NOT k/2, NOT c/(2h^v)
verdict: ACCEPT

PE-10: scope quantifier
genus: all on the proved uniform-weight lane; genus 1 unconditional for standard families
degree: all
AP32 weight tag: (UNIFORM) tagged? Y
AP139 free-var audit: LHS vars {g,\cA}  RHS vars {g,\cA}  LHS⊇RHS? Y
AP36: implies; no converse asserted
verdict: ACCEPT
```
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
@@ -3212,5 +3212,7 @@
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
@@ -3220,5 +3222,6 @@
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
@@ -3227,11 +3230,20 @@
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
@@ -3239,8 +3251,10 @@
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
@@ -3249,4 +3263,4 @@
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
@@ -3254,3 +3268,5 @@
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
@@ -3262,5 +3278,5 @@
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 42ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]

file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]



thinking
**Considering LaTeX build options**

I see the task is local, but the user wants to write. Running a full build could take some time, though it might be feasible. Perhaps it’d be easier to use `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. It could take a while, but it might work in the environment. Alternatively, I could run a more targeted approach with that same command, just to check for any syntax errors first.
thinking
**Considering remark titles**

I think it's important to ensure no duplicate remark titles across live surfaces. I should re-read the edited section using sed, and maybe run a local grep for any banned patterns or em-dash issues. I might also use ripgrep (rg) for efficiency. Additionally, there's the possibility of needing to look into line wrapping. It seems like I have a few things to sort out to make everything tidy and organized!
codex
The edit is in place. I’m re-reading the patched block now and then I’ll do the narrowest verification that can still fail this change: local diff plus a grep sweep for the new formulas and basic TeX hygiene on the touched surface.
exec
/bin/zsh -lc "sed -n '3204,3272p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Alternative derivation via index theory]
\label{rem:complementarity-index-theory}
\index{complementarity!index-theoretic derivation}
\index{index theory!complementarity}
There is a second derivation of the complementarity sum that does not
add the two explicit $\kappa$-formulas term by term. The bar-cobar
package
\textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
Koszul pair inside the single ambient complementarity complex
$\mathbf{C}_g(\cA)$ of
Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
eigenspace splitting
\[
\mathbf{C}_g(\cA)
\;\simeq\;
\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
\]
On the proved uniform-weight lane, and at genus~$1$ for every standard
exec
/bin/zsh -lc "rg -n \"chi_g\\"'^'"\\{\\\\mathrm\\{sh\\}\\}|chi_g\\"'^'"\\{\\\\mathrm\\{tot\\}\\}|c/2 \\+ \\(26-c\\)/2 = 13|self-dual fixed point|---|notably|crucially|remarkably|furthermore|additionally|moreover\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:chi_g\^\{\mathrm\{sh\}\}|chi_g\^\{\mathrm\{tot\}\}|c/2 \+ \(26-c\)/2 = 13|self-dual fixed point|---|notably|crucially|remarkably|furthermore|additionally|moreover)
                ^^
error: unrecognized escape sequence
 succeeded in 51ms:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fd..e05ba30 100644
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@ add the two explicit $\kappa$-formulas term by term. The bar-cobar
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]


thinking
**Considering options for execution**

I’m thinking about whether to complete the current task or use polling instead, which seems more robust. I know the repository is huge, but I think the compile may run eventually. If it takes too long, we can always stop it. I’m considering using `tty:false` for plain pipes and running fixed-string greps. Maybe I could parallelize the grep and compile processes since they can run independently. So yeah, let’s go for it!
codex
The prose reads correctly after the patch. I’m doing one stronger verification pass now: fixed-string greps on the touched formulas plus a build attempt, so I can distinguish a verified LaTeX surface from a purely textual patch.
exec
/bin/zsh -lc "rg -n -F 'chi_g"'^{'"\\mathrm{sh}}' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'chi_g"'^{'"\\mathrm{tot}}' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'self-dual fixed point plus index theory' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/codex-hgc main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3226:\chi_g^{\mathrm{sh}}(\cA)
3238:\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
3246:\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
3271:2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 succeeded in 51ms:
3244:\chi_g^{\mathrm{tot}}(\cA)
3264:Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
3269:\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
 succeeded in 51ms:
3280:self-dual fixed point plus index theory, independently of the direct
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]

 exited 12 in 3.13s:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: making output directory '/tmp/codex-hgc'
No existing .aux file, so I'll make a simple one, and require run of *latex.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Category 'other':
  Rerun of 'pdflatex' forced or previously required:
    Reason or flag: 'Initial setup'

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -halt-on-error -file-line-error -recorder -output-directory="/private/tmp/codex-hgc"  "main.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]


thinking
**Running LaTeX build**

Okay, I want to run the command `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex`. It should take just one pass, or maybe even less. I remember that `main.tex` has includes, so I'll need to check the file `chapters/frame/preface.aux` in the workspace. I really want to ensure there are no errors, so I’ll proceed with that. Let's get this going!
codex
The first build attempt failed for an environment reason, not a theorem-surface reason: `latexmk` with `/tmp` output could not open included `.aux` files under `chapters/frame/*`. I’m doing one in-worktree `pdflatex` pass now to separate “output-directory problem” from an actual syntax break in the edited chapter.
exec
/bin/zsh -lc 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]

 exited 1 in 1.59s:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/memoir.cls
Document Class: memoir 2025/03/06 v3.8.3 configurable book, report, article doc
ument class
(/usr/local/texlive/2025/texmf-dist/tex/latex/xpatch/xpatch.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3kernel/expl3.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def))
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3packages/xparse/xparse.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/etoolbox/etoolbox.sty))
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/mem11.clo)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/dcolumn.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/delarray.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/tabularx.sty)
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]

codex
The in-worktree build also failed before reaching a clean theorem-surface verdict, but again not because of this edit: `main.aux` is already broken upstream (`Missing \begin{document}`), with additional pre-existing duplicate-label warnings. I’m doing a final cross-volume sweep on the new remark label and title now, then I’ll close with the local outcome and the unrelated verification blockers.
exec
/bin/zsh -lc "rg -n -F 'rem:complementarity-index-theory' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:31378:  "rem:complementarity-index-theory": {
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1091:candidate label: \label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1097:/bin/zsh -lc "rg -n '\\\\label\\{rem:complementarity-index-theory\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1138:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1215:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1292:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1385:/bin/zsh -lc "rg -n '\\\\label\\{rem:complementarity-index-theory\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1396:/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3205:\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1407:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1507:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1613:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1695:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1772:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1910:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1995:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:2087:  3205	\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:2122:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:2211:+\label{rem:complementarity-index-theory}
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3205:\label{rem:complementarity-index-theory}
exec
/bin/zsh -lc 'git status --short chapters/theory/higher_genus_complementarity.tex main.aux main.log' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Alternative derivation via index theory' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

 succeeded in 61ms:
/Users/raeez/chiral-bar-cobar/scripts/healing_fortification_40.py:346:Write as Remark[Alternative derivation via index theory].""")
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:3:Inserted `Remark [Alternative derivation via index theory]` in [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3204). It recasts the complementarity sum as the normalized Euler characteristic of the Verdier-split ambient bar package, then computes the Virasoro conductor from the self-dual point `c=13`, without using the direct termwise sum `c/2 + (26-c)/2`.
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:81:Write as Remark[Alternative derivation via index theory].
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1100:/bin/zsh -lc "rg -n 'Alternative derivation via index theory|index-theoretic complementarity|self-dual point .*13|Virasoro.*13/2' chapters/theory/higher_genus_complementarity.tex /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 58ms:
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1137:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1214:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1291:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1406:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1506:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1612:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1694:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1771:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1909:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:1994:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:2086:  3204	\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:2121:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:2195:Inserted `Remark [Alternative derivation via index theory]` in [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3204). It recasts the complementarity sum as the normalized Euler characteristic of the Verdier-split ambient bar package, then computes the Virasoro conductor from the self-dual point `c=13`, without using the direct termwise sum `c/2 + (26-c)/2`.
/Users/raeez/chiral-bar-cobar/healing_20260413_130533/H12_complementarity_alt.md:2210:+\begin{remark}[Alternative derivation via index theory]
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3204:\begin{remark}[Alternative derivation via index theory]
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]


thinking
**Confirming labels uniqueness**

I'm thinking that running a direct grep on only the chapters directories across volumes could help me confirm that the labels are unique. I want to make sure I'm being precise with this step. It seems like a solid approach to verifying something important, and doing it directly should save time. So, let’s go ahead with that idea!
codex
The cross-volume sweep is clean on the live TeX surface: the new label/title only exist in this chapter, and the extra hits were in local healing notes and metadata, not in Vol II or Vol III source. I’m making one last precise grep on the live `chapters/` trees only, then I’ll close with the fortification status and the unrelated build blockers.
exec
/bin/zsh -lc "rg -n -F 'Alternative derivation via index theory' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'rem:complementarity-index-theory' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3204:\begin{remark}[Alternative derivation via index theory]
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3205:\label{rem:complementarity-index-theory}
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]


thinking
**Evaluating confidence levels**

I'm feeling confident about the Virasoro lane, but my confidence is more medium when it comes to the broader multi-weight family, especially if we interpret it beyond genus 1. I think it’s important to mention this because the remarks explicitly scope the discussion. It’s interesting to navigate how different interpretations can change the confidence level in these contexts! Let's keep examining this further!
codex
Rewrote the existing remark at [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:3204) instead of adding a duplicate. The new version makes the index-theoretic route explicit: it defines the normalized scalar index `\chi_g^{\mathrm{sh}} = F_g/\lambda_g^{\mathrm{FP}}`, identifies it with `\kappa` via Theorems `thm:modular-characteristic` and `thm:family-index`, promotes `\kappa(\cA)+\kappa(\cA^!)` to the total Verdier-split bar-package index, and then computes `K_{\mathrm{Vir}}=13` from the self-dual fixed point `c=13` without using the termwise identity `c/2 + (26-c)/2 = 13`.

Local text checks passed, and the remark label/title are unique on the live `chapters/` surfaces across Vols I-III. I could not get a clean full build verdict because the repo currently has unrelated TeX blockers: `latexmk` with `/tmp` output cannot open included `.aux` files, and an in-worktree `pdflatex` run fails upstream on a pre-existing broken `main.aux` (`Missing \begin{document}`), plus existing duplicate-label warnings.

## Fortification Report
`prop:complementarity-landscape` scalar complementarity lane
- PRIMARY PROOF: sound
- SECONDARY PROOF: written
- TECHNIQUE: Euler characteristic / GRR family-index normalization, Verdier eigenspace splitting, self-dual fixed-point evaluation
- CONDITION STATUS: unconditional for Virasoro; all genera on the proved uniform-weight lane; genus 1 unconditional for all standard families
- CONFIDENCE: high for the Virasoro fixed-point derivation; medium if read as a genus `g>=2` argument for multi-weight families beyond the existing scalar lane
file update:
diff --git a/chapters/theory/higher_genus_complementarity.tex b/chapters/theory/higher_genus_complementarity.tex
index a9089fdfaac7800404922901ffc79933c9714816..e05ba30537f2536e1eac20ef8999881c73aab0a3
--- a/chapters/theory/higher_genus_complementarity.tex
+++ b/chapters/theory/higher_genus_complementarity.tex
@@ -3210,49 +3210,65 @@
 package
 \textup{(}Theorem~\textup{\ref{thm:chiral-koszul-duality}},
 Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}
-places a Koszul pair $(\cA,\cA^!)$ inside the single ambient complex
-$\mathbf{C}_g(\cA)$ of Theorem~\textup{\ref{thm:quantum-complementarity-main}},
-with Verdier eigenspace splitting
+does not treat $\cA$ and $\cA^!$ as isolated objects. It places the
+Koszul pair inside the single ambient complementarity complex
+$\mathbf{C}_g(\cA)$ of
+Theorem~\textup{\ref{thm:quantum-complementarity-main}}, with Verdier
+eigenspace splitting
 \[
 \mathbf{C}_g(\cA)
 \;\simeq\;
 \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!).
 \]
-On the scalar lane, define the normalized genus-$g$ index by
+On the proved uniform-weight lane, and at genus~$1$ for every standard
+family, define the normalized scalar index
 \[
-I_g(\cA)
+\chi_g^{\mathrm{sh}}(\cA)
 \;:=\;
 \frac{F_g(\cA)}{\lambda_g^{\mathrm{FP}}},
 \]
 where $\lambda_g^{\mathrm{FP}}$ is the universal tautological
-integral of Theorem~\textup{\ref{thm:family-index}}. By the family
-index theorem, $I_g(\cA)=\kappa(\cA)$ on the uniform-weight lane, and
-at genus~$1$ this identification is unconditional for the standard
-families. Additivity of Euler characteristic on the direct sum above
-therefore gives
+integral of Theorem~\textup{\ref{thm:family-index}}. The modular
+characteristic theorem together with the family-index theorem
+\textup{(}Theorems~\textup{\ref{thm:modular-characteristic}}
+and~\textup{\ref{thm:family-index}}\textup{)}
+identify this normalized Euler characteristic with the scalar shadow
+coefficient:
+\[
+\chi_g^{\mathrm{sh}}(\cA) \;=\; \kappa(\cA).
+\]
+Thus $\kappa(\cA)$ is the index-theoretic shadow of the genus tower.
+
+Passing to the total Verdier-self-dual bar package gives
 \[
-I_g(\mathbf{C}_g(\cA))
+\chi_g^{\mathrm{tot}}(\cA)
+\;:=\;
+\chi_g^{\mathrm{sh}}(\cA) + \chi_g^{\mathrm{sh}}(\cA^!)
 \;=\;
-I_g(\cA) + I_g(\cA^!)
+\frac{F_g(\cA) + F_g(\cA^!)}{\lambda_g^{\mathrm{FP}}}
 \;=\;
 \kappa(\cA) + \kappa(\cA^!).
 \]
-The complementarity constant is thus the normalized Euler
-characteristic of the total Verdier-self-dual bar package. Over a
-point this total index is zero, recovering the classical
-antisymmetry $K = 0$; on a curve the universal Hodge term from
-Theorem~\textup{\ref{thm:family-index}} can shift the total index,
-which is why the chiral conductor need not vanish.
+This is the normalized index of the total bar package. Replacing
+$\cA$ by $\cA^!$ only exchanges the two Verdier eigensummands, so the
+total index depends on the underlying $\chirAss$ duality orbit, not on
+the chosen representative. Over a point the Hodge contribution is
+absent, and one recovers the classical commutative Koszul constant
+$K = 0$. On a curve the same index acquires the universal Hodge term,
+so in the chiral associative setting the conductor can be nonzero; in
+the Virasoro family this is the central-charge conductor.
 
 For the Virasoro family the involution is $c \mapsto 26-c$, whose
 fixed point is $c = 13$
 \textup{(}Remark~\textup{\ref{rem:self-dual-complementarity}}\textup{)}.
-Since the total index is constant along a duality orbit, it may be
-computed at the fixed point:
+Since $\chi_g^{\mathrm{tot}}$ is constant along the duality orbit, it
+may be evaluated at the fixed point:
 \[
 K_{\mathrm{Vir}}
 \;=\;
-2\,I_g(\mathrm{Vir}_{13})
+\chi_g^{\mathrm{tot}}(\mathrm{Vir}_{13})
+\;=\;
+2\,\chi_g^{\mathrm{sh}}(\mathrm{Vir}_{13})
 \;=\;
 2\,\kappa(\mathrm{Vir}_{13})
 \;=\;
@@ -3260,9 +3276,9 @@
 \;=\;
 13.
 \]
-This recovers the Virasoro complementarity constant from self-duality
-plus the index theorem, independently of the direct calculation
-$c/2 + (26-c)/2 = 13$.
+This recovers the Virasoro complementarity constant from the
+self-dual fixed point plus index theory, independently of the direct
+identity $c/2 + (26-c)/2 = 13$.
 \end{remark}
 
 \begin{remark}[The Koszul conductor polynomial]

tokens used
280,541
