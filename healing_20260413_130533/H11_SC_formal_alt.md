# H11_SC_formal_alt (709s)

I repaired the converse of `prop:sc-formal-iff-class-g` and added the requested `Remark[Operadic alternative proof]` in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2823) and [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2863). The key correction is that I did not use the requested `B_{SC}` / `Δ=0 \Rightarrow` class `G` converse, because that is not true on the manuscript’s own classification surface: class `L` still has `\Delta=0`. The new converse instead uses the full operadic vanishing pattern `S_r=0` for all `r\ge 3`, via the genus-0 transfer tree and the averaging map `\operatorname{av}(\Theta^{E_1}_\cA)=\Theta_\cA`.

Verification: I ran `make fast`. The build failed outside this edit, on pre-existing undefined-control-sequence errors in [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3513), so there is no clean full-manuscript build verdict from this turn.

## Fortification Report
- `prop:sc-formal-iff-class-g` in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2823): PRIMARY PROOF: repaired; SECONDARY PROOF: written; TECHNIQUE: genus-0 operadic transfer plus the shadow/formality dictionary and `E_1` averaging; CONDITION STATUS: unconditional; CONFIDENCE: high.

Pending collision surface: `../calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py` still appears to advertise a stale SC-formality classification, but I did not edit it because this turn’s write scope was the target manuscript file.


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
session id: 019d869e-5398-7780-9a28-224297e91290
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


SC-FORMALITY — ALTERNATIVE PROOF of iff class G.

TARGET: chapters/theory/chiral_koszul_pairs.tex (add Remark)

Write a PURELY OPERADIC alternative proof of both directions:

FORWARD (class G => SC-formal):
1. Class G means Delta = 8*kappa*S_4 = 0 and the shadow tower truncates at degree 2.
2. The SC operations m_k^{SC} at order k >= 3 are controlled by S_{k-1} in the shadow tower.
3. S_r = 0 for r >= 3 (class G) implies m_k^{SC} = 0 for k >= 3. QED.

CONVERSE (SC-formal => class G):
1. SC-formality means the SC bar complex B_{SC}(A) is formal.
2. Formality of the bar implies its cohomology is a FORMAL dg-object.
3. The shadow tower is the WEIGHT-GRADED PIECE of this cohomology.
4. A formal dg-object with nonzero S_3 would produce a non-formal Massey product in B_{SC}.
5. So SC-formal implies S_3 = 0, which forces Delta = 0, which forces class G.

This avoids the bilinear-form argument. Write as Remark[Operadic alternative proof].
mcp startup: no servers


thinking
**Analyzing codebase proof**

I think the requested proof might conflict with certain repository invariants—like SC^{ch,top} not being on B(A). It's possible that SC-formality relates to whether G is about A being SC-formal, but I'm unsure about the complexity here. I need to inspect the exact theorem and context first. For this codebase question, my developer suggests using explorer agents instead of manual searches. I should probably start with the explorer to find relevant files and theorem references efficiently.
thinking
**Using explorer agents effectively**

I think I should spawn one or more explorer agents. One could summarize the relevant context in the target file and theorem while another might locate the necessary files and references about SC-formality. The task seems to align with "beilinson-rectify" and possibly "cross-volume-propagation" after some edits. I also need to consider "claim-surface-sync" if the theorem status is relevant. Since the instructions suggest using explorers first, that's definitely my plan to comply!
codex
Scope is `chapters/theory/chiral_koszul_pairs.tex`, specifically the SC-formality surface and whether the requested operadic alternative proof is compatible with the repo’s current SC/bar conventions. I’m loading the required constitutional files plus the local theorem context first, and I’ll only write once the proof path is consistent with those invariants.
collab spawn_agent(call_POzydudGkCEvaRhFgBtKqhW8, prompt="Read and summarize only the parts needed for an edit to chapters/theory/chiral_koszul_pairs.tex about SC-formality. Requ…")
spawn_agent(call_POzydudGkCEvaRhFgBtKqhW8, prompt="Read and summarize only the parts needed for an edit to chapters/theory/chiral_koszul_pairs.tex about SC-formality. Requ…") pending init:
  agent: 019d869e-a72b-77a1-906f-b4f28761d20e
mcp startup: no servers
collab spawn_agent(call_Q1cdk9lAT2m9ZBgflkuuN5f2, prompt="Search Vol I/II/III for 'SC-formal', 'class G', 'shadow tower', 'Delta = 8', 'S_3', 'B_{SC}', 'Swiss-cheese formality'. …")
mcp startup: no servers
spawn_agent(call_Q1cdk9lAT2m9ZBgflkuuN5f2, prompt="Search Vol I/II/III for 'SC-formal', 'class G', 'shadow tower', 'Delta = 8', 'S_3', 'B_{SC}', 'Swiss-cheese formality'. …") pending init:
  agent: 019d869e-a82e-7092-852b-81571524b78a
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC-formal" -n' in /Users/raeez/chiral-bar-cobar succeeded in 171ms:
healing_20260413_132214/H04_thm_D_alt_proof.md:43:- SC-formality, depth gap, D^2=0, Gerstenhaber: platonic agents running (P11-P20).
healing_20260413_132214/H02_thm_B_alt_proof.md:43:- SC-formality, depth gap, D^2=0, Gerstenhaber: platonic agents running (P11-P20).
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:5:I then re-read the other flagged surfaces in the same file and verified they are already repaired on the live surface: the bar-side filtered comparison lemma exists and is cited, `(vii)` is only genus-`0` unconditionally with the all-genera version restricted to the uniform-weight lane, `(viii)` is only a one-way Hochschild consequence, and the SC-formality/class-`G` discussion now covers Heisenberg, lattice VOA, and free fermion without the invalid `\kappa`-trilinear argument. I did not run a full TeX build; verification was by local reread and grep, and I did not change any labels.
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:13:- [FIXED] finding 6 — verified the converse SC-formality proof no longer uses the invalid `\kappa(x,[y,z])` construction and instead runs through shadow-tower truncation/classification.
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:96:6. [CRITICAL T15] Line ~2539: SC-formality converse proof uses bilinear form C(x,y,z)=kappa(x,[y,z])
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:110:I’m thinking about the guidelines around edits in hot zones, and it seems there’s a specific protocol to follow. It looks like we might be dealing with some findings related to kappa, potentially class G and SC-formality. I need to check whether we should provide PE-10 for scope quantifier modification when changing theorem statements and maybe PE-4 for writing adjustments to bar complex formulas under theorem A. There's a lot to navigate!
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:340:/bin/zsh -lc 'rg -n "filtered-comparison|Verdier|SC-formality|class G|lattice|Koszul equiv|Theorem A|bar-cobar-isomorphism-main|thm:verdier-bar-cobar|thm:shadow-formality-identification" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:559:relationship between SC-formality and the classification is
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:567:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:570:\index{class G@class~$G$!characterised by SC-formality}
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:602:  2646	relationship between SC-formality and the classification is
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:610:  2654	\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:613:  2657	\index{class G@class~$G$!characterised by SC-formality}
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:1051:Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:1058:precisely class~$G$. Hence an SC-formal algebra must belong
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:2380:I then re-read the other flagged surfaces in the same file and verified they are already repaired on the live surface: the bar-side filtered comparison lemma exists and is cited, `(vii)` is only genus-`0` unconditionally with the all-genera version restricted to the uniform-weight lane, `(viii)` is only a one-way Hochschild consequence, and the SC-formality/class-`G` discussion now covers Heisenberg, lattice VOA, and free fermion without the invalid `\kappa`-trilinear argument. I did not run a full TeX build; verification was by local reread and grep, and I did not change any labels.
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:2388:- [FIXED] finding 6 — verified the converse SC-formality proof no longer uses the invalid `\kappa(x,[y,z])` construction and instead runs through shadow-tower truncation/classification.
healing_20260413_132214/H01_thm_A_alt_proof.md:43:- SC-formality, depth gap, D^2=0, Gerstenhaber: platonic agents running (P11-P20).
healing_20260413_132214/H03_thm_C_alt_proof.md:43:- SC-formality, depth gap, D^2=0, Gerstenhaber: platonic agents running (P11-P20).
CLAUDE.md:512:| SC-formal | PROVED | SC-formal iff class G (prop:sc-formal-iff-class-g) |
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
bibliography
bp_self_duality.pdf

exec
/bin/zsh -lc "sed -n '1,160p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

thinking
**Considering task updates**

I’m thinking I might need to update my plan since the task seems substantial. It’s important to assess everything properly. Maybe I should take a moment to wait and gather more information before diving in. I want to make sure I have a clear approach. It’s crucial to consider all aspects before proceeding, so I’ll take my time with this decision. Let’s see how I can best move forward!
exec
/bin/zsh -lc 'rg -n "SC-formality" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarcodex
I’m checking two things in parallel: the local SC-formality theorem lane and the cross-volume collision surface. The critical point is whether the requested converse proof uses forbidden SC-on-bar language; if it does, I’ll rewrite it to the nearest truthful operadic statement rather than insert a false argument.
 succeeded in 51ms:
7197: & SC-formality characterises class~$\mathbf{G}$:
9782:& SC-formality $\iff$ class~$\mathbf{G}$
exec
/bin/zsh -lc "pwd && sed -n '1,220p' .agents/skills/beillington-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
/Users/raeez/chiral-bar-cobar
sed: .agents/skills/beillington-rectify/SKILL.md: No such file or directory
 succeeded in 51ms:
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

exec
/bin/zsh -lc "sed -n '7150,7225p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 & shadow trace formula RTF $= 0$ \\
Vol.~II, rank-$1$ DR string equation
 & CohFT string equation at rank $1$ & DR cycle forgetful $+$ Buryak DR/DZ \\
\ref{thm:pixton-from-mc-semisimple}
 & Pixton ideal from MC for semisimple cases
 & FSZ $+$ PPZ $+$ Givental--Teleman \\
\ref{thm:operadic-complexity}
 & $r_{\max} = d_\infty = f_\infty$
 \textup{(}operadic complexity identification\textup{)}
 & induction on degree $+$ HPL tree formula \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: theorem architecture rewrites (A1--A6~+~G7)}} \\
\hline
\ref{lem:chirhoch-descent}
 & Chiral Hochschild descent:
 $\ChirHoch^{\bullet}(\cA)
 \cong (\mathbb{D}_{\Ran}\barB(\cA))_{\Sigma}$
 on the Koszul locus
 & Theorem~A Verdier intertwining $+$ coinvariant descent \\

exec
/bin/zsh -lc "sed -n '9750,9825p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarthinking
**Organizing targeted multi-volume search**

I’m planning a focused search across multiple volume directories for key terms like ‘SC-formal’ and ‘class G’ to gather canonical statements with file references. I want to identify duplicates and note cross-volume overlap risks while summarizing relevant proof outlines, using precise ripgrep commands to manage the large output effectively.
 succeeded in 50ms:
 uniform-weight modular Koszul algebras at all genera
 \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\
& Swiss-cheese theorem
 \textup{(}Theorem~\ref{thm:thqg-swiss-cheese}\textup{)} \\
& Chiral derived center as universal bulk \\
& Annulus trace
 \textup{(}Theorem~\ref{thm:thqg-annulus-trace}\textup{)} \\
& Heisenberg and lattice sewing
 \textup{(}Theorems~\ref{thm:heisenberg-sewing},
 \ref{thm:lattice-sewing}\textup{)} \\
& HS-sewing for the entire standard landscape (universal algebras)
 \textup{(}Theorem~\ref{thm:general-hs-sewing}\textup{)} \\
& All-degree inverse limit
 $\Theta_\cA = \varprojlim \Theta_\cA^{\le r}$
 \textup{(}Theorem~\ref{thm:recursive-existence}\textup{)} \\
& Algebraic-family rigidity
 \textup{(}Theorem~\ref{thm:algebraic-family-rigidity}\textup{)} \\
& DS primitivity of the gravitational coproduct
 (Vol~II, Theorem~\textup{thm:ds-hpl-transfer}) \\
& Epstein zeta of the shadow metric: functional equation
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC-formality characterises class" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:567:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:610:  2654	\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
relaunch_20260413_111534/S14_standalone_to_main.md:2244:chapters/connections/concordance.tex:7097: & SC-formality characterises class~$\mathbf{G}$:
relaunch_20260413_111534/S14_standalone_to_main.md:2341:  2574	\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
rectification_20260412_233715/R18_cobar_construction.md:606:| `prop:sc-formal-iff-class-g` | `proposition` | 2455 | SC-formality characterises class~$G$ |
chapters/connections/concordance.tex:7197: & SC-formality characterises class~$\mathbf{G}$:
rectification_20260412_233715/R09_en_koszul_duality.md:611:chapters/theory/chiral_koszul_pairs.tex:2521:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
standalone/survey_modular_koszul_duality.tex:6238:\noindent\textbf{SC-formality characterises class~$\mathbf{G}$.}\enspace
standalone/classification.tex:799:\subsection{SC-formality characterises class G}
chapters/theory/chiral_koszul_pairs.tex:2786:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
metadata/dependency_graph.dot:2427:  prop_sc_formal_iff_class_g [label="prop:sc-formal-iff-class-g\nproposition [Pr]\nSC-formality characterises class~$G$", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:416:| `prop:sc-formal-iff-class-g` | `proposition` | 2682 | SC-formality characterises class~$G$ |
wave2_audit_20260413_001942/S03_koszul_to_shadow.md:562:chapters/theory/chiral_koszul_pairs.tex:2572:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
metadata/claims.jsonl:2328:{"label": "prop:sc-formal-iff-class-g", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 2682, "title": "SC-formality characterises class~$G$"}
audit_campaign_20260412_231034/T16_depth_gap.md:1485:  7074	 & SC-formality characterises class~$\mathbf{G}$:
audit_campaign_20260412_231034/T15_SC_formality.md:207:chapters/connections/concordance.tex:7074: & SC-formality characterises class~$\mathbf{G}$:
audit_campaign_20260412_231034/T15_SC_formality.md:216:chapters/theory/chiral_koszul_pairs.tex:2521:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
audit_campaign_20260412_231034/T15_SC_formality.md:377:  7074	 & SC-formality characterises class~$\mathbf{G}$:
audit_campaign_20260412_231034/T15_SC_formality.md:1135:metadata/dependency_graph.dot:2411:  prop_sc_formal_iff_class_g [label="prop:sc-formal-iff-class-g\nproposition [Pr]\nSC-formality characterises class~$G$", style=filled, fillcolor="#c8e6c9"];
audit_campaign_20260412_231034/T15_SC_formality.md:1136:metadata/theorem_registry.md:412:| `prop:sc-formal-iff-class-g` | `proposition` | 2455 | SC-formality characterises class~$G$ |
exec
/bin/zsh -lc 'rg -n "SC-form" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
416:| `prop:sc-formal-iff-class-g` | `proposition` | 2682 | SC-formality characterises class~$G$ |
exec
/bin/zsh -lc 'cd /Users/raeez && rg -n "SC-formal" chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chiral-bar-cobar-vol2/compute/depth_spectrum_c_dependence.py:363:    print("  kappa(Vir_c) = c - 26. At c=26: kappa=0 (SC-formal, shadow truncates).")
chiral-bar-cobar-vol2/compute/audit/beilinson_audit_vol2_preface_wave11.md:52:- **MODERATE -- "Heisenberg class G, formal" (line 349).** The "formal" tag is correct (G is formal by definition), but a hostile reader will ask: "formal" in which sense -- SC-formal (m_k^SC = 0 for k >= 3), or dg-algebra formal (H*(A) quasi-iso to A)? AP14 explicitly distinguishes: "Koszulness != SC formality." In the Heisenberg case both hold, but the preface does not say which it means. For a preface this is LOW.
chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:852: & SC-formality \\[2pt]
chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1186:The Swiss-cheese structure is SC-formal: the higher
chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1642: & $0$ (Koszul and SC-formal) \\[2pt]
chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3304: obstructs SC-formality
chiral-bar-cobar-vol2/working_notes.tex:10604:  \emph{SC-formal}
chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:489:\index{SC-formality!characterisation}%
chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:497: $\cA$ is SC-formal \textup{(}$m_k^{\mathrm{SC}} = 0$
chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:520:Part~\eqref{item:fdd-sc-formal}: SC-formality requires
chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:525:$m_k = 0$ for $k \ge 3$ and SC-formality holds.
chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:561:is the equivalence between SC-formality, finite shadow
exec
/bin/zsh -lc "sed -n '380,430p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
| `thm:geometric-depth-smooth` | `theorem` | 4349 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 4647 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 4778 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 4825 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 5023 | $bc$/$\beta\gamma$ Koszul duality |
| `thm:gerstenhaber-structure` | `theorem` | 5047 | Chiral Gerstenhaber structure on $\ChirHoch^*$ |
| `prop:hochschild-cech-ss` | `proposition` | 5374 | Hochschild--\v{C}ech spectral sequence |
| `prop:envelope-shadow` | `proposition` | 5812 | Factorization envelope shadow functor |

#### `chapters/theory/chiral_koszul_pairs.tex` (49)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 286 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 313 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 333 | Filtered comparison |
| `lem:filtered-comparison-unit` | `lemma` | 361 | Bar-side filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 412 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 488 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 767 | PBW criterion for chiral Koszulness |
exec
/bin/zsh -lc 'cd /Users/raeez && rg -n "SC-formal" calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
calabi-yau-quantum-groups/AGENTS.md:224:- shadow class or SC-formality claims;
calabi-yau-quantum-groups/AGENTS.md:763:If editing shadow depth, class, or SC-formality claims, check:
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:58:  SC-formal (m_k^{SC} = 0 for k >= 3): Heisenberg, lattice (class G only)
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:62:  CRITICAL: SC-formality is DIFFERENT from chirally Koszul.
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:63:  ALL standard families are chirally Koszul.  Only class G is SC-formal.
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:291:    SC-formal means m_k^{SC} = 0 for k >= 3.  Only class G (Heisenberg)
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:292:    is SC-formal.  Class L has m_3^{SC} != 0, class C has m_4^{SC} != 0,
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:295:    CRITICAL (AP14): SC-formality is DIFFERENT from chirally Koszul.
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:296:    ALL standard families are chirally Koszul.  Only class G is SC-formal.
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:305:    For SC-formal families (class G only): returns float('inf').
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:311:    for k >= 3 are nonzero.  Only class G is SC-formal.
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:315:        return float("inf")  # SC-formal
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:482:# 7. VOL II BRIDGE -- SC-formality data
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:628:    SC-formality, complementarity, and cross-check status.
calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:639:    # SC-formality
calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:62:   Vol I proves: class G/L are SC-formal (m_k^{SC} = 0 for k >= 3).
calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:458:        sc_formal=False,  # class M is NOT SC-formal
calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:468:            "Class M (infinite depth), r_max=infinity. NOT SC-formal. "
calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:993:            obstruction_source="Class L: m_3^{SC} != 0 (Lie bracket, NOT SC-formal).",
calabi-yau-quantum-groups/compute/tests/test_swiss_cheese_cy3_e1.py:373:        """Local P^2: class M, NOT SC-formal (AP-CY12)."""
exec
/bin/zsh -lc "sed -n '1,200p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory
codex
I’m using `beilinson-rectify` for the proof-surface repair and `cross-volume-propagation` after the local edit if the wording changes a shared claim. Before editing, I’m reading the exact SC-formality lane in the target file and the constitutional sources that outrank prior prose.
exec
/bin/zsh -lc 'rg -n "SC-formal|SC formality|class G|shadow tower|Swiss-cheese|Delta = 8|S_3|S_4" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "SC-formal|class G|shadow tower|Delta = 8|S_3|S_4|Swiss-cheese" chapters/connections/concordance.tex metadata/theorem_registry.md CLAUDE.md archive/raeeznotes/raeeznotes100/red_team_summary.md raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
66:$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
84:Koszulness and SC formality are logically independent properties.
86:in degree one; SC formality is the condition
87:$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
89:(Heisenberg and its relatives) is SC-formal
91:Confusing the two misidentifies what the shadow tower measures.
114:and the critical discriminant $\Delta = 8\kappa S_4$, whose
2485:This reaches \textup{(x)} without passing through the shadow tower.
2635:governed by the discriminant $\Delta = 8\kappa S_4$.
2648:This ordering refines the Koszulness programme: all four classes are chirally Koszul (bar $E_2$-collapse), but they differ in Swiss-cheese formality depth.
2651:\begin{proposition}[Swiss-cheese non-formality by shadow class; \ClaimStatusProvedHere]
2653:\index{Swiss-cheese operad!non-formality by shadow class|textbf}
2654:\index{shadow depth!Swiss-cheese formality}
2656:The Swiss-cheese operations $m_k^{\mathrm{SC}}$ on~$\cA$ itself
2702:Equivalently, the shadow tower truncates at degree~$2$:
2709:the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
2714:\textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
2725:\textup{(}$T_{(3)}T = c/2$\textup{)} produces $S_3 = 2$
2727:$\Delta = 8\kappa S_4 \neq 0$ forces all higher operations to be
2737:shadow tower with its weight-$2$ truncation. For the free fermion,
 exited 2 in 52ms:
archive/raeeznotes/raeeznotes100/red_team_summary.md:112:- Volume II foundations around Swiss-cheese recognition, PVA descent, FM/AOS cancellation, and bar-cobar rectification look substantially healthier than the speculative connection chapters.
CLAUDE.md:11:**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:202:4. DERIVE the symmetric result (kappa = av(r(z)), obs_g = kappa*lambda_g, the shadow tower).
CLAUDE.md:204:NEVER state a symmetric-bar result (kappa, obs_g, shadow tower) without first showing the E1 object it projects from. NEVER frame the five theorems as "concerning the symmetric bar" — they EXTRACT the Sigma_n-invariant content of the ordered bar. The symmetric bar is the shadow; the ordered bar generates.
CLAUDE.md:279:**C30. Delta discriminant.** `Delta = 8*kappa*S_4`. Finite tower iff Delta=0; for kappa!=0 iff S_4=0. LINEAR in kappa (NOT quadratic, AP21). Heis: S_4=0, Delta=0, class G. Vir: S_4!=0, Delta!=0, class M.
CLAUDE.md:375:- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
CLAUDE.md:388:- B63. `S_4 \sim 2/(5c^2)` at large c. CORRECT: `S_4 \sim 2/c^2`. The 10/(5c^2) = 2/c^2, not 2/(5c^2). AP178.
CLAUDE.md:512:| SC-formal | PROVED | SC-formal iff class G (prop:sc-formal-iff-class-g) |
CLAUDE.md:564:AP14: Koszulness != SC formality. Koszul = bar H* in degree 1. SC formal = m_k^{SC}=0 for k>=3. All standard families Koszul; only class G SC-formal.
CLAUDE.md:838:AP129: Reciprocal formula. When a formula involves a ratio a/b, the most common transcription error is b/a or -b/a. Both "look right" because they contain the same symbols. S_4(Vir) = 10/[c(5c+22)] was written as -(5c+22)/(10c) (the negative reciprocal). VERIFY: substitute a known value (e.g. c=1) and check the NUMBER before trusting the symbolic form.
CLAUDE.md:858:AP143: DS ghost charge background shift omission. DS reduction from sl_N to W_{N,f} requires subtracting the full ghost central charge c_ghost(N,f,k) = c(sl_N,k) - c(W_{N,f},k), which includes the background charge contribution from the DS BRST complex. The simplified formula c_ghost(N,k=0) = N*(N-1) OMITS this background charge; the correct formula gives (N-1)*((N^2-1)*(N-1)-1). At N=7: 1722 vs 42. This error caused a cascade across W6/W7 shadow tower engines where engine and test were synchronized to the same wrong value (AP128 variant). VERIFY: at N=2, ghost_c = 1*((4*1)-1) = 3 = c(sl_2,0) - c(Vir,0) = 3 - 0. Before writing ANY DS ghost formula for N>=3, compute c(sl_N,k) - c(W_{N,f},k) directly from the Fateev-Lukyanov formula.
CLAUDE.md:874:AP158: SC^{ch,top} != E_3. The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply to coloured operads. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, T(z) = {Q,G(z)}) = E_3-TOPOLOGICAL (NOT E_3-chiral). The conformal vector KILLS the chiral direction at the cohomological level: C-translations become Q-exact, the complex structure on C becomes irrelevant in cohomology, the two SC colors collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct). At critical level k=-h^v: Sugawara undefined, topologization fails. NEVER write "E_3-chiral" for the topologized bulk; it is E_3-topological. Vol II MUST construct the E_3-topological structure on Z^{der}_{ch}(A) explicitly at chain level — define it, prove it, verify on examples, and characterize the obstruction when conformal vector is absent.
CLAUDE.md:881:AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).
CLAUDE.md:889:AP171: Associator dependence dichotomy. The chiral QG equivalence (R-matrix <-> A_inf <-> coproduct) holds "up to choice of Drinfeld associator Phi." COHOMOLOGICAL derived center = ASSOCIATOR-INDEPENDENT (proved for sl_2: GRT_1 shifts P_3 by coboundaries). COCHAIN-LEVEL derived center = ASSOCIATOR-DEPENDENT (the cochain-level E_3 carries the quantum group structure). Bar-side invariants (kappa, shadow tower) are associator-FREE. Cobar-side and coproduct-side depend on Phi. Analogous to deformation quantization: gauge-equivalent star products.
CLAUDE.md:898:AP178: S_4 large-c asymptotic off by factor 5 (Vol II, 3d_gravity.tex line 7763). The manuscript writes "S_4 = 10/[c(5c+22)] ~ 2/(5c^2) at large c." WRONG. 10/[c(5c+22)] = 10/(5c^2 + 22c) ~ 10/(5c^2) = 2/c^2 at large c. The correct asymptotic is 2/c^2, NOT 2/(5c^2). Off by factor 5. The error: the denominator 5c^2 was retained inside the fraction instead of being cancelled against the numerator 10. COUNTER: after writing ANY asymptotic, substitute c=100 and verify: 10/[100*522] = 10/52200 ≈ 1.916e-4; 2/c^2 = 2/10000 = 2e-4 (matches); 2/(5c^2) = 2/50000 = 4e-5 (off by 5x).
CLAUDE.md:920:RS-9: The slab is a bimodule, NOT a Swiss-cheese disk. Two boundary components.
CLAUDE.md:949:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
CLAUDE.md:959:**Vol I**: Introduction + Overture (Heisenberg CG opening, unnumbered) + Part I (Bar Complex: Thms A-D+H, 12 Koszul equivs) + Part II (Characteristic Datum: shadow tower, G/L/C/M/M*/W, higher-genus, E_1 modular) + Part III (Standard Landscape: all families, census) + Part IV (Physics Bridges: E_n, factorization envelopes, derived Langlands) + Part V (Seven Faces of r(z): F1 bar-cobar twisting, F2 DNP25 line-operator, F3 Khan-Zeng PVA, F4 Gaiotto-Zeng sphere Hamiltonians, F5 Drinfeld Yangian, F6 Sklyanin/STS83, F7 FFR94 Gaudin) + Part VI (Frontier) + Appendices.
metadata/theorem_registry.md:415:| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 2547 | Swiss-cheese non-formality by shadow class |
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{Chiral Koszul duality}
\label{chap:koszul-pairs}

\index{chiral Koszul duality|textbf}
\index{twisting morphism!chiral|textbf}
\index{Francis--Gaitsgory|textbf}

Classical Koszul duality, in the sense of
Priddy~\cite{Priddy70} and
Beilinson--Ginzburg--Soergel~\cite{BGS96}, works for graded
algebras over a field: the bar complex is a tensor coalgebra on a
finite-dimensional vector space, the cobar functor inverts it
when bar cohomology is concentrated in degree one, and the
duality exchanges quadratic algebras with quadratic coalgebras.
Three features of chiral algebras on algebraic curves defeat
this framework simultaneously. First, chiral algebras are
\emph{curved}: the bar differential on the genus expansion
satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
rather than $d^2 = 0$, so the classical bar-cobar adjunction,
which requires strict nilpotence, does not apply beyond genus
exec
/bin/zsh -lc 'rg -n "shadow tower" -n' in /Users/raeez/chiral-bar-cobar succeeded in 102ms:
versality -> family index`.
relaunch_20260413_111534/R14_concordance.md:955:+\text{shadow tower construction}
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:6:- [FIXED] T06 circularity in Theorem D — added an explicit routing remark making the proof chain non-circular: bar-intrinsic shadow tower (`thm:mc2-bar-intrinsic`) → genus universality (`thm:genus-universality`) → downstream GRR/family-index identification (`thm:family-index`).
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:74:   The proof chain should be: shadow tower construction (independent) → genus universality
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:75:   (from shadow tower) → family index identification (from universality). Make this explicit.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:96:6. [CRITICAL T16] Line ~16414: Class-C witness contradicted. betagamma shadow tower vanishes
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:99:   verify the shadow tower is nonzero there. Update the witness.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:160:**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:172:/bin/zsh -lc "rg -n \"thm:family-index|thm:mc2-bar-intrinsic|Theta_A|Defcyc|depth gap|betagamma|D\\"'^2=0|log FM|Whitehead|PBW|truncated current algebra|shadow tower|genus universality|family index" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:715:I need to focus on the idea of non-circular anchors in shadow tower construction. It seems like genus universality leads us to family index identification, so the family index is actually downstream of universality and not parallel. If I claim the family index is independent, it might create confusion. I should take a closer look at the theorem `thm:family-index` to understand how it's used and perhaps conduct a search around the label for additional insights.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:717:I found the Theorem D routing surface. It still presents `thm:family-index` as a parallel computation, while your required proof architecture makes it downstream of the bar-intrinsic shadow tower and genus universality. I’m checking `thm:family-index` citations now so I can rewrite that route without creating a new contradiction elsewhere in this file.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1027:  2895	shadow tower. Theorem~\ref{thm:genus-universality} identifies its
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1204:-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1210:+The non-circular anchor is the bar-intrinsic shadow tower.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1245: The bar-intrinsic shadow tower is the common source.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1387:-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1393:+The non-circular anchor is the bar-intrinsic shadow tower.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1418: \Theta_\cA \text{ and its shadow tower}
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1432: The bar-intrinsic shadow tower is the common source.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:1607:-shadow tower. Theorem~\ref{thm:genus-universality} identifies its
exec
/bin/zsh -lc "sed -n '1,200p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
/bin/zsh -lc 'rg -n "SC-formal" -n archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

thinking
**Summarizing key references on shadow tower**

I'll focus on extracting and highlighting canonical statements about the "shadow tower" mainly from `AGENTS`, `CLAUDE`, and the theory chapters, noting duplicates and how these statements appear across multiple volumes. I'll also consider conflicts with the requested proof outlines and related verification notes about avoiding certain formality assumptions, aiming to provide a clear, consolidated summary with cross-references.
exec
/bin/zsh -lc 'rg -n "Delta = 8" -n' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 1379

CLAUDE.md:279:**C30. Delta discriminant.** `Delta = 8*kappa*S_4`. Finite tower iff Delta=0; for kappa!=0 iff S_4=0. LINEAR in kappa (NOT quadratic, AP21). Heis: S_4=0, Delta=0, class G. Vir: S_4!=0, Delta!=0, class M.
wave2_audit_20260413_001942/D15_hardcoded_parts.md:848:$\Delta = 8\kappa S_4$ to vanish, and the algebraicity theorem of
wave2_audit_20260413_001942/S11_bv_brst_to_body.md:129:CLAUDE.md:279:**C30. Delta discriminant.** `Delta = 8*kappa*S_4`. Finite tower iff Delta=0; for kappa!=0 iff S_4=0. LINEAR in kappa (NOT quadratic, AP21). Heis: S_4=0, Delta=0, class G. Vir: S_4!=0, Delta!=0, class M.
wave2_audit_20260413_001942/C15_free_fields.md:271:   326	where $\alpha = S_3$ and $\Delta = 8\kappa S_4$. With
wave2_audit_20260413_001942/C15_free_fields.md:534:326:where $\alpha = S_3$ and $\Delta = 8\kappa S_4$. With
wave2_audit_20260413_001942/C15_free_fields.md:727:326:where $\alpha = S_3$ and $\Delta = 8\kappa S_4$. With
wave2_audit_20260413_001942/S06_intro_to_body.md:1022:AGENTS.md:153:Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.
wave2_audit_20260413_001942/D04_kappa_drift.md:356:16:and the critical discriminant $\Delta = 8\kappa S_4$. The
wave2_audit_20260413_001942/S04_shadow_to_examples.md:233:chapters/examples/landscape_census.tex:16:and the critical discriminant $\Delta = 8\kappa S_4$. The
wave2_audit_20260413_001942/S04_shadow_to_examples.md:325:    16	and the critical discriminant $\Delta = 8\kappa S_4$. The
wave2_audit_20260413_001942/S04_shadow_to_examples.md:404:/bin/zsh -lc "rg -n -S \"Heisenberg|beta\\\\gamma|betagamma|Virasoro|W_N|W_3|affine Kac|Kac--Moody|class~\\\\mathbf\\{G\\}|class~\\\\mathbf\\{L\\}|class~\\\\mathbf\\{C\\}|class~\\\\mathbf\\{M\\}|r_max|kappa\\(|k\\\\Omega|c/2|H_N|H_{N-1}|Delta = 8|8\\\\kappa\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/S04_shadow_to_examples.md:405:/bin/zsh -lc "rg -n -S \"Heisenberg|beta\\\\gamma|betagamma|Virasoro|W_N|W_3|affine Kac|Kac--Moody|class G|class L|class C|class M|r_max|kappa\\(|k\\\\Omega|c/2|H_N|H_{N-1}|Delta = 8|8\\\\kappa\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
wave2_audit_20260413_001942/S04_shadow_to_examples.md:407:    (?:Heisenberg|beta\gamma|betagamma|Virasoro|W_N|W_3|affine Kac|Kac--Moody|class~\mathbf\{G\}|class~\mathbf\{L\}|class~\mathbf\{C\}|class~\mathbf\{M\}|r_max|kappa\(|k\Omega|c/2|H_N|H_{N-1}|Delta = 8|8\kappa)
wave2_audit_20260413_001942/S04_shadow_to_examples.md:412:    (?:Heisenberg|beta\gamma|betagamma|Virasoro|W_N|W_3|affine Kac|Kac--Moody|class G|class L|class C|class M|r_max|kappa\(|k\Omega|c/2|H_N|H_{N-1}|Delta = 8|8\kappa)
wave2_audit_20260413_001942/S04_shadow_to_examples.md:427:16:and the critical discriminant $\Delta = 8\kappa S_4$. The
wave2_audit_20260413_001942/S04_shadow_to_examples.md:664:   685	 & $\boldsymbol{\Delta = 8\kappa S_4}$
wave2_audit_20260413_001942/S04_shadow_to_examples.md:931:29545:where $Q_L(t) = (2\kappa + 3\alpha t)^2 + 2\Delta\,t^2$ is the shadow metric \textup{(}Theorem~\textup{\ref{thm:riccati-algebraicity})}. In the Polyakov regime ($t \to 0$, degree-$2$ dominance): $H_L(t) \sim \kappa\,t^2$, recovering the Polyakov free energy $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ as the Taylor coefficients of $H_L$. The shadow metric $Q_L$ encodes the full nonlinear completion: its critical discriminant $\Delta = 8\kappa S_4$ determines whether the tower terminates ($\Delta = 0$: classes G, L) or persists ($\Delta \neq 0$: classes C, M). The Polyakov formula is the leading-order ($\Delta = 0$) specialization.
wave2_audit_20260413_001942/S04_shadow_to_examples.md:933:    16	and the critical discriminant $\Delta = 8\kappa S_4$. The
exec
/bin/zsh -lc "sed -n '500,528p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2640,2838p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7178,7212p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
| Thm | Status | Key result |
|-----|--------|------------|
| A | PROVED | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
| B | PROVED | Bar-cobar inversion: Omega(B(A)) -> A qi on Koszul locus |
| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
| H | PROVED | ChirHoch*(A) polynomial Hilbert series, concentrated in cohomological degrees {0,1,2} |
| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
| Koszul | 10+1+1 | 10 unconditional + Lagrangian (conditional) + D-mod purity (one-dir) |
| D^2=0 | PROVED | Convolution (M-bar_{g,n}) + ambient (Mok25 log FM) |
| Theta_A | PROVED | Bar-intrinsic; all-degree inverse limit (thm:recursive-existence) |
| SC-formal | PROVED | SC-formal iff class G (prop:sc-formal-iff-class-g) |
| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy) |
| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
| Topologization | PROVED (affine KM); CONJECTURAL (general) | SC^{ch,top} + Sugawara = E_3 for V_k(g) at k != -h^v (thm:topologization). General chiral algebras with conformal vector: conj:topologization-general. Proof cohomological; class M chain-level open. |
| E_3 identification | PROVED (simple g) | Z^der_ch(V_k(g)) ≅ A^lambda as E_3-families over lambda*H^3(g)[[lambda]] (thm:e3-identification). Proof: E_3 formality (Kontsevich) + 1-dim of H^3(g) forces order-by-order uniqueness. For non-simple g: open (H^3 may be higher-dimensional). |
| Chiral QG equiv | PROVED | Three structures (R-matrix, A_inf, coproduct) determine each other on Koszul locus (thm:chiral-qg-equiv). Independent proof via CoHA (rem:independent-proof-coha). |
| gl_N chiral QG | PROVED (all N >= 1) | W_N carries chiral quantum group datum with Yang R-matrix, Drinfeld coproduct, non-trivial RTT for N >= 2 (thm:glN-chiral-qg). N=1 = thm:w-infty-chiral-qg. OPE compatibility by coderivation + JKL. |
| Verlinde recovery | PROVED | Verlinde Z_g = sum S_{0j}^{2-2g} recovered from ordered chiral homology at integer level (prop:verlinde-from-ordered). Handle attachment and separating factorization verified. |
 succeeded in 50ms:
\index{shadow depth!loop-exactness ordering}
The four shadow-depth classes are ordered by the number of loop corrections needed to determine the full $A_\infty$ structure on~$\cA^!_{\mathrm{line}}$:
\begin{itemize}
\item Class~$G$ (Gaussian, $r_{\max}=2$): tree-level exact.
\item Class~$L$ (Lie/tree, $r_{\max}=3$): one-loop exact (DNP non-renormalization, Theorem~\ref{thm:dnp-bar-cobar-identification}(iii)).
\item Class~$C$ (Contact, $r_{\max}=4$): two-loop exact.
\item Class~$M$ (Mixed, $r_{\max}=\infty$): requires all-loop resummation.
\end{itemize}
This ordering refines the Koszulness programme: all four classes are chirally Koszul (bar $E_2$-collapse), but they differ in Swiss-cheese formality depth.
\end{remark}

\begin{proposition}[Swiss-cheese non-formality by shadow class; \ClaimStatusProvedHere]
\label{prop:swiss-cheese-nonformality-by-class}
\index{Swiss-cheese operad!non-formality by shadow class|textbf}
\index{shadow depth!Swiss-cheese formality}
\index{Ainfty@$A_\infty$!non-formality for class M}
The Swiss-cheese operations $m_k^{\mathrm{SC}}$ on~$\cA$ itself
\textup{(}not on the bar cohomology $H^*(\barB(\cA))$, which is
always $A_\infty$-formal for Koszul algebras by
Theorem~\textup{\ref{thm:koszul-equivalences-meta}(iii)}\textup{)}
 succeeded in 52ms:
 $\cD$-module purity~(xii)
 & chiral localization $+$ Hitchin VHS $+$ Saito \\
\ref{prop:shadow-tower-three-lenses}
 & Three equivalent descriptions of $S_r(\cA)$:
 algebraic (shadow), geometric (formality obstruction),
 holographic (boundary-bulk correction)
 & bar-intrinsic MC $+$ formality identification
 $+$ derived-centre factorization \\
\ref{def:generating-depth}
 & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
 $d_{\mathrm{alg}}$: formal distinction~;
 Virasoro $d_{\mathrm{gen}} = 3$,
 $d_{\mathrm{alg}} = \infty$
 & depth decomposition $+$ class~M tower non-termination \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: structural propositions and depth classification}} \\
\hline
\ref{prop:sc-formal-iff-class-g}
 & SC-formality characterises class~$\mathbf{G}$:
exec
/bin/zsh -lc 'rg -n "Swiss" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
112:- Volume II foundations around Swiss-cheese recognition, PVA descent, FM/AOS cancellation, and bar-cobar rectification look substantially healthier than the speculative connection chapters.
exec
/bin/zsh -lc 'rg -n "S_3" -n' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
Total output lines: 9147

wave2_audit_20260413_001942/D13_genus_1_vs_all.md:433:/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:609:share $\kappa(V_\Lambda) = r$, class~G shadow depth $r_{\max} = 2$, and genus expansion $F_g(V_\Lambda) = r \cdot \lambda_g^{\mathrm{FP}}$ at every genus. For the $24$ Niemeier lattices ($r = 24$), the scalar invariants $(\kappa, S_3, S_4, \ldots) = (24, 0, 0,
wave2_audit_20260413_001942/C13_virasoro.md:386:chapters/examples/free_fields.tex:1101:of~$c$, with $S_3 = 2$ (the universal Virasoro cubic shadow) and
wave2_audit_20260413_001942/C13_virasoro.md:388:chapters/examples/free_fields.tex:1138:$S_3 = 2$ from the universal Virasoro cubic (the coefficient of
wave2_audit_20260413_001942/C13_virasoro.md:762:chapters/examples/lattice_foundations.tex:877:The $S_3$-action on $H_*(\barBgeom(\Vlat_{D_4}))$ is the representation-theoretic manifestation of the triality symmetry: the three fundamental representations of $\mathfrak{so}_8$ (vector, spinor, conjugate spinor) are permuted by outer automorphisms, and this permutation lifts to the bar complex level.
wave2_audit_20260413_001942/S11_bv_brst_to_body.md:996:25827:For class~$\mathsf{M}$ $($Virasoro$)$: $S_3 = 2$, $\kappa = c/2$,
wave2_audit_20260413_001942/S10_examples_to_wn.md:252:standalone/virasoro_r_matrix.tex:66:shadow coefficient $S_3(\Vir_c) = 2$ is independent of the central
wave2_audit_20260413_001942/S10_examples_to_wn.md:770:  9606	 cubic coefficient $\alpha = S_3/\kappa$ universal per family:
wave2_audit_20260413_001942/F19_dangling_refs_v3.md:1166:  4768	The fundamental polyhedron $\mathcal{P}_{II}$ has $\mathrm{Aut}(\mathcal{P}_{II}) \simeq S_3$, and
wave2_audit_20260413_001942/F19_dangling_refs_v3.md:1188:    81	The fundamental polyhedron $\mathcal{P}_{II}$ has $\mathrm{Aut}(\mathcal{P}_{II}) \simeq S_3$, and
wave2_audit_20260413_001942/F19_dangling_refs_v3.md:1485:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:444:The Verdier duality functor $D_{\C^3}$ on conilpotent $E_3$-coalgebras acts by linear duality on the underlying graded space and inverts the $\C^3$-equivariant parameters: $(h_1, h_2, h_3) \mapsto (-h_1, -h_2, -h_3)$. At the self-dual point $(1, 0, -1)$, this gives $(-1, 0, 1)$. Since $h_2 = 0$ is preserved, the inversion is the relabeling $z_1 \leftrightarrow z_3$, under which $H_1 \simeq H_1$ by the $S_3$-symmetry of the Omega-background (the Heisenberg is insensitive to the ordering of the $\C$ factors). The Shapovalov form at level $k = 1$ provides the explicit isomorphism $H_1 \xrightarrow{\sim} H_1^*$.
wave2_audit_20260413_001942/F19_dangling_refs_v3.md:1486:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:471:The holomorphic refinement replaces the $\SO(3)$-action on $E_3$ by the action of the algebraic torus $T = (\C^*)^3/\C^*_{\mathrm{diag}}$ on $\C^3$, where $\C^*_{\mathrm{diag}}$ acts by the CY constraint $q_1 q_2 q_3 = 1$. The Omega-background parameters $(h_1, h_2, h_3)$ with $h_1 + h_2 + h_3 = 0$ are the Lie algebra coordinates on $\mathrm{Lie}(T)$, and the multiplicative parameters $q_i = e^{h_i}$ are the characters. The Weyl group of $T$ in $\GL_3(\C)$ is precisely $S_3$ acting by coordinate permutation. Hence $S_3$ persists from the topological $\SO(3)$-action on $E_3$ to the holomorphic torus action on $\C^3$:
wave2_audit_20260413_001942/F19_dangling_refs_v3.md:1487:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:492:\subsubsection{Rational degeneration and $S_3$-breaking}
wave2_audit_20260413_001942/F19_dangling_refs_v3.md:1489:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:495:The affine Yangian $Y(\widehat{\fgl}_1)$ is the rational limit $q_i \to 1$, equivalently $h_i \to 0$ with ratios $\epsilon_i = h_i/\hbar$ fixed. In this limit, the torus $T = (\C^*)^2$ degenerates to the additive group $\C^2$, and the $S_3$-action on $(\epsilon_1, \epsilon_2, \epsilon_3)$ persists as a \emph{parameter symmetry} but ceases to lift to an algebra automorphism. The $E_3$-operadic explanation is:
wave2_audit_20260413_001942/C15_free_fields.md:271:   326	where $\alpha = S_3$ and $\Delta = 8\kappa S_4$. With
wave2_audit_20260413_001942/C15_free_fields.md:272:   327	$S_3 = 0$ and $S_4 = 0$:
wave2_audit_20260413_001942/C15_free_fields.md:372:  1283	$\lambda$ & $c$ & $\kappa$ & $S_3$ & $S_4$ & $\Delta$ & $\rho$
wave2_audit_20260413_001942/C15_free_fields.md:386:  1297	Here $S_3$ and $S_4$ are the T-line shadow invariants,
wave2_audit_20260413_001942/C15_free_fields.md:534:326:where $\alpha = S_3$ and $\Delta = 8\kappa S_4$. With
exec
/bin/zsh -lc "sed -n '2400,2800p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
trivial: $E_\infty = E_2$ as bigraded objects, not merely as
filtered objects. Hence $E_2$-collapse, hence~(i).

\medskip
\textsc{Lagrangian criterion}
\textup{(i)}$\Leftrightarrow$\textup{(xi)}
\emph{(unconditional for the standard landscape by
Proposition~\textup{\ref{prop:lagrangian-perfectness}}; conditional
on perfectness in general)}:

\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(xi)}:
On the Koszul locus, the bar-cobar adjunction provides a free
resolution, and the complementarity splitting
$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
\simeq H^*(\overline{\cM}_g, \cZ_\cA)$
(Theorem~C) identifies $\cM_\cA$ and $\cM_{\cA^!}$ as
complementary subspaces of $\cM_{\mathrm{comp}}$. The
shifted-symplectic structure
(Theorem~\ref{thm:ambient-complementarity-fmp})
collab wait(call_ftkeqtQErQdsiTsGt2YyuMVq)
  receivers: 019d869e-a72b-77a1-906f-b4f28761d20e, 019d869e-a82e-7092-852b-81571524b78a
exec
/bin/zsh -lc "sed -n '2800,3100p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the class-$G$ row consists of the Gaussian families Heisenberg,
lattice VOA, and free fermion, and in each case the genus-$0$
mixed tree formulas stop at arity~$2$, so
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.

For the converse, suppose~$\cA$ is SC-formal.
Then the mixed sector of the Swiss-cheese bar complex is formal:
every higher arity tree operation vanishes. The tower-bar
correspondence is operadic: the arity-$r$ mixed tree and the
degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
formula, with the same propagator on internal edges; the only
difference is the output colour, and passage to the symmetric
closed sector applies the averaging morphism
$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
there is no higher mixed tree whose closed projection could survive.
By Theorem~\ref{thm:shadow-formality-identification} and
Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
the statement that the shadow/formality tower truncates at

thinking
**Collecting canonical references and discrepancies**

I’m gathering precise references on the canonical SC-formal statements across volumes, focusing on locating exact line numbers in key files like `chiral_koszul_pairs.tex` and `swiss_cheese_cy3_e1.py`. I want to highlight cross-volume discrepancies—especially the conflicting claims about class G/L SC-formality—and include detailed file paths and line ranges for accurate user reference.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2480,2555p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the K\"unneth spectral sequence yields
\[
H^k\bigl(i_{S_T}^!\,\barB_n(\cA)\bigr)=0
\qquad (k \neq 0).
\]
This reaches \textup{(x)} without passing through the shadow tower.

The same bookkeeping exposes further direct links already implicit
in the proof:
\[
\textup{(iv)} \Rightarrow \textup{(ii)},\qquad
\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
\textup{(ix)} \Rightarrow \textup{(ii)},\qquad
\textup{(x)} \Rightarrow \textup{(ii)},\qquad
\textup{(v)} \Longleftrightarrow \textup{(vi)}.
\]
Accordingly the unconditional core
\[
\{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
\textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
exec
/bin/zsh -lc 'rg -n "operadic" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
38:Koszul duality of the Lie--Com pair at the operadic level, but
56:No other functorial construction achieves all three: the operadic
260: is quadratic/Koszul in the ordinary operadic sense;
2808:correspondence is operadic: the arity-$r$ mixed tree and the
5264:\emph{Step 1: Reduction to the classical operadic statement.}
5281:By Lemma~\ref{lem:operadic-koszul-transfer} below
5286:chiral tensor category: the operadic bar complex
5318:\label{lem:operadic-koszul-transfer}
5325:the operadic bar construction\/
5339:\emph{Step~1: The Koszul complex is built from operadic composition.}
5348:of planar trees indexing operadic compositions
5382:Lemma~\ref{lem:operadic-koszul-transfer} with
5399:\textup{(}Lemma~\textup{\ref{lem:operadic-koszul-transfer}},
5473:counterpart, operating within the single operadic type $\chirAss$.
5486:land in the same operadic type) but has not been treated in the
5827: The chiral bar-cobar adjunction is the operadic skeleton
5857:mechanism at the operadic level, with the
5872:category) with the operadic datum of a twisting morphism
6038:The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC-formality" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2778:relationship between SC-formality and the classification is
2784:between SC-formality and truncation of the shadow tower at degree~$2$.
2786:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
2789:\index{class G@class~$G$!characterised by SC-formality}
2815:Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
exec
/bin/zsh -lc "sed -n '5200,5405p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[Convergence role of pro-nilpotence]\label{rem:convergence-pro-nil}
\label{rem:convergence-pronilpotent}
Pro-nilpotence ensures the cobar differential
$d_\Omega: \Omega(\mathcal{C})_n \to \Omega(\mathcal{C})_{n-1}$
is well-defined: the formula involves a sum over all ways to
decompose a tensor factor via the coproduct, which in general is an
infinite series. Conilpotence ensures this sum is finite in each
degree. On the algebra side, pro-nilpotence ensures the bar
construction is degree-wise finite-dimensional.
See Appendix~\ref{app:nilpotent-completion} for the completion
theory.
\end{remark}

\subsection{\texorpdfstring{The bar-cobar equivalence for $\chirAss$}{The bar-cobar equivalence for Ass ch}}

\begin{theorem}[\texorpdfstring{$\Eone$}{E1}-chiral Koszul duality; \ClaimStatusProvedHere]
\label{thm:e1-chiral-koszul-duality}
\index{E1-Koszul duality@$\mathbb{E}_1$-Koszul duality|textbf}
\textup{[Regime: quadratic on the Koszul locus;
filtered-complete via PBW degeneration
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2760,2825p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$Q^{\mathrm{contact}}$ is nonzero by the explicit
$\beta\gamma\beta\gamma$ channel computation; termination at
depth~$4$ follows from rank-one rigidity
(Theorem~\ref{thm:riccati-algebraicity}).
Class~$M$:
$S_3 = (\text{scalar projection of } T_{(1)}T)/T_{(3)}T
= 2\kappa/\kappa = 2$, independent of~$c$;
$S_4 = 10/[c(5c{+}22)]$ and $\Delta = 8\kappa S_4 = 40/(5c{+}22) \neq 0$
for generic~$c$, so the Riccati algebraicity theorem
forces the tower to be infinite.
Computational verification:
\texttt{theorem\_ainfty\_nonformality\_class\_m\_engine.py}
(three independent methods for $S_3$,
quartic shadow $S_4$ and $Q^{\mathrm{contact}}$, quintic
shadow $S_5 = -48/(c^2(5c+22))$, all four classes verified).
\end{proof}

The four classes exhaust the standard landscape, but the
relationship between SC-formality and the classification is
sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
exec
/bin/zsh -lc 'rg -n "alternative proof" -n chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '140,180p' AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
**SC^{ch,top} is NOT on B(A) (AP165).** B(A) is E_1 coassociative coalgebra. SC^{ch,top} lives on the pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) is a coalgebra over SC^{ch,top}"; "the bar differential is the closed color"; "the bar coproduct is the open color."

**SC^{ch,top} is NOT Koszul self-dual (AP166).** SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!. SC = (Com, Ass) with closed dim = 1. The duality FUNCTOR is involutive ((P^!)^! ~ P); the OPERAD is not self-dual (P^! ≇ P).

**A^! is an SC^!-algebra (AP172)** = (Lie, Ass)-algebra (closed = Sklyanin bracket, open = Yangian product). NOT an SC-algebra.

## X. The Four Shadow Classes

- **G**: r=2, Heisenberg. Delta=0, d_alg=0. SC-formal.
- **L**: r=3, affine KM. Delta!=0, d_alg=1.
- **C**: r=4, betagamma. Delta!=0, d_alg=2.
- **M**: r=inf, Vir/W_N. Delta!=0, d_alg=inf.

Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.

## XI. Canonical Formulas

Verify against these AND `landscape_census.tex` before writing. NEVER write kappa from memory (AP1).

```text
exec
/bin/zsh -lc 'rg -n "B_{SC}" -n' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:B_{SC})
          ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n \"B_\\{SC\\}\" -n" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2500,2890p'" in /Users/raeez/chiral-bar-cobar succeeded in 65ms:
compute/tests/test_two_colored_bar_engine.py:10:  4. Two-coloured SC bar construction B_{SC}
compute/tests/test_two_colored_bar_engine.py:342:        """d^2 = 0 on closed-output elements of B_{SC}."""
compute/tests/test_two_colored_bar_engine.py:363:        """Closed sector of B_{SC} should equal B_{Com}."""
compute/tests/test_two_colored_bar_engine.py:384:        """Pure-open sector of B_{SC} should equal B_{Ass}."""
compute/tests/test_two_colored_bar_engine.py:520:        """B_{SC}(k[x]/(x^3), k[x]/(x^3)) explicit structure."""
compute/tests/test_two_colored_bar_engine.py:720:        """d^2 = 0 for B_{SC}(C, C) for all commutative test algebras."""
 succeeded in 51ms:
  2500	\textup{(x)}\}
  2501	\]
  2502	forms a web rather than a chain.
  2503	
  2504	\begin{center}
  2505	\begin{tikzcd}[column sep=3em,row sep=2.8em]
  2506	\textup{(iv)} \arrow[r] \arrow[dr] &
  2507	\textup{(ii)} \arrow[d, shift left=.5ex] \arrow[r, shift left=.5ex] &
  2508	\textup{(v)} \arrow[l, shift left=.5ex] \arrow[dl] \arrow[dr] &
  2509	\\
  2510	\textup{(vii)} \arrow[r, shift left=.5ex] \arrow[ur] &
  2511	\textup{(i)} \arrow[l, shift left=.5ex] \arrow[r, shift left=.5ex] \arrow[d, shift left=.5ex] \arrow[dr] \arrow[rr, bend left=12] &
  2512	\textup{(iii)} \arrow[l, shift left=.5ex] \arrow[dl] &
  2513	\textup{(vi)} \arrow[ll, bend left=12]
  2514	\\
  2515	\textup{(ix)} \arrow[uur, bend left=16] \arrow[r] &
  2516	\textup{(x)} \arrow[u, shift left=.5ex] \arrow[ur] &
  2517	\textup{(viii)} &
  2518	\end{tikzcd}
  2519	\end{center}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '680,730p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\hline
\textbf{Algebra $\cA$}
 & \textbf{Class}
 & $\boldsymbol{S_3}$
 & $\boldsymbol{S_4}$
 & $\boldsymbol{\Delta = 8\kappa S_4}$
 & $\boldsymbol{\rho}$
 & $\boldsymbol{\kappa{+}\kappa'}$ \\
\hline
$\mathcal{H}_k$ & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
\hline
Free fermion & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
\hline
$bc$ ($\lambda$) & C & $0$ & $\neq 0$ & $0^\dagger$ & $0^\dagger$ & $0$ \\
\hline
$V_\Lambda$ (rank $d$) & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
\hline
$\widehat{\fg}_k$ & L & $\neq 0$ & $0$ & $0$ & $0$ & $0$ \\
\hline
$\beta\gamma_\lambda$ & C & $0$ & $\neq 0$ & $0^\dagger$ & $0^\dagger$ & $0$ \\
exec
/bin/zsh -lc "nl -ba CLAUDE.md | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
     1	# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)
     2	
     3	## Identity
     4	
     5	E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
     6	
     7	**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
     8	
     9	Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.
    10	
    11	**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.
    12	
    13	**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
    14	
    15	**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
    16	
    17	**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.
    18	
    19	**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.
    20	
wait(call_ftkeqtQErQdsiTsGt2YyuMVq) timed out:

codex
The target proposition is already proved locally, but the current converse proof still talks about the “Swiss-cheese bar complex.” That collides with the repo’s AP165 rule, so I’m verifying whether the requested new remark can be salvaged by shifting the converse to the actual SC datum on the derived-center pair rather than inserting false bar language.
collab wait(call_O1Vny4GnXKHYtb4I3X7rL5SC)
  receivers: 019d869e-a72b-77a1-906f-b4f28761d20e, 019d869e-a82e-7092-852b-81571524b78a
thinking
**Summarizing operadic proof remarks and references**

I'm collecting key points for the final summary about the operadic alternative proof remark's legitimacy, referencing SC formality on the derived center versus bar from CLAUDE lines 5-7 and related sections. I plan to highlight the current proof strategy based on the coupling of SC operations and the shadow tower, referencing lines 2651-2823 in `chapters/theory/chiral_koszul_pairs.tex`. I will also note SC formality classification details from `chapters/connections/concordance.tex` around lines 7160 and 9782, the `metadata/theorem_registry.md` entry near line 416, and cautionary notes from the archived red team summary. The summary will truthfully assess whether adding an operadic alternative proof remark is consistent with existing mentions of “operadic” structures in lines 2797-2824 and 2808-2813. I'll follow developer instructions by including bullet points with inline code file references and line numbers to keep the summary clear and precise.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7165,7205p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7165	 & Chiral Hochschild descent:
  7166	 $\ChirHoch^{\bullet}(\cA)
  7167	 \cong (\mathbb{D}_{\Ran}\barB(\cA))_{\Sigma}$
  7168	 on the Koszul locus
  7169	 & Theorem~A Verdier intertwining $+$ coinvariant descent \\
  7170	\ref{prop:koszul-closure-properties}
  7171	 & Closure of chiral Koszulness under tensor product,
  7172	 Koszul dualization, and base change
  7173	 & three pre-existing fragments consolidated;
  7174	 quotients excluded \\
  7175	\ref{prop:d-module-purity-km-equivalence}
  7176	 & Kac--Moody equivalence via Saito--Kashiwara weight
  7177	 filtration: PBW strictness~(ii) $\iff$
  7178	 $\cD$-module purity~(xii)
  7179	 & chiral localization $+$ Hitchin VHS $+$ Saito \\
  7180	\ref{prop:shadow-tower-three-lenses}
  7181	 & Three equivalent descriptions of $S_r(\cA)$:
  7182	 algebraic (shadow), geometric (formality obstruction),
  7183	 holographic (boundary-bulk correction)
  7184	 & bar-intrinsic MC $+$ formality identification
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '9750,9815p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  9750	 uniform-weight modular Koszul algebras at all genera
  9751	 \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\
  9752	& Swiss-cheese theorem
  9753	 \textup{(}Theorem~\ref{thm:thqg-swiss-cheese}\textup{)} \\
  9754	& Chiral derived center as universal bulk \\
  9755	& Annulus trace
  9756	 \textup{(}Theorem~\ref{thm:thqg-annulus-trace}\textup{)} \\
  9757	& Heisenberg and lattice sewing
  9758	 \textup{(}Theorems~\ref{thm:heisenberg-sewing},
  9759	 \ref{thm:lattice-sewing}\textup{)} \\
  9760	& HS-sewing for the entire standard landscape (universal algebras)
  9761	 \textup{(}Theorem~\ref{thm:general-hs-sewing}\textup{)} \\
  9762	& All-degree inverse limit
  9763	 $\Theta_\cA = \varprojlim \Theta_\cA^{\le r}$
  9764	 \textup{(}Theorem~\ref{thm:recursive-existence}\textup{)} \\
  9765	& Algebraic-family rigidity
  9766	 \textup{(}Theorem~\ref{thm:algebraic-family-rigidity}\textup{)} \\
  9767	& DS primitivity of the gravitational coproduct
  9768	 (Vol~II, Theorem~\textup{thm:ds-hpl-transfer}) \\
  9769	& Epstein zeta of the shadow metric: functional equation

thinking
**Summarizing canonical references and cross-volume risks**

I'll organize a detailed bullet list covering key canonical statements like Swiss-cheese formality, shadow tower, Delta and S3 formulas, and B_SC rules with precise file and line references. I'll highlight conflicts including cross-volume duplications and propagation risks by pointing to examples in CLAUDE, AGENTS, standalone chapters, and compute libraries to frame the requested proof outline and classification collisions clearly.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '40,90p' compute/lib/swiss_cheese_cy3_e1.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   at each bar degree k >= 2 (Vol II, AP37, AP38).

   Consequence: the E_1 shadow obstruction tower has MORE terms at
   each arity, but the R-matrix descent B^{ord} -> B^{Sigma} (twisted
   by R) produces the same scalar shadow on the symmetric quotient.

3. SHADOW DEPTH FOR CY3 ALGEBRAS.
   The shadow depth classification (G/L/C/M) depends on the OPE
   structure of the chiral algebra, not on the E_1/E_inf distinction.

   For CY3-derived algebras:
     C^3 -> W_{1+inf}: class M (infinite tower). Each spin-s
       channel contributes independently. Spin 1 (Heisenberg) = G.
       Spin 2 (Virasoro at c=1) = M. Total: M.
     Resolved conifold -> H_1 (Heisenberg from compact cycle): class G.
     Local P^2 -> McKay quiver CoHA: class M (AP-CY12: infinite depth;
       leading-order OPE is Lie-type from shuffle product, but
       higher-degree BPS states generate an infinite tower).
     Quintic -> class M (infinite GW invariants drive infinite tower).
     K3 x E -> class M (BKM superalgebra, infinite Borcherds product).
exec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '400,430p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   400	| `thm:km-chiral-koszul` | `theorem` | 845 | Affine Kac--Moody algebras are chiral Koszul |
   401	| `thm:virasoro-chiral-koszul` | `theorem` | 900 | Virasoro chiral Koszulness |
   402	| `cor:bar-cohomology-koszul-dual` | `corollary` | 944 | Bar cohomology computes Koszul dual |
   403	| `thm:bar-concentration` | `theorem` | 1132 | Bar concentration for Koszul pairs |
   404	| `prop:ainfty-formality-implies-koszul` | `proposition` | 1245 | Formality implies chiral Koszulness |
   405	| `thm:ainfty-koszul-characterization` | `theorem` | 1279 | Converse: chiral Koszulness implies formality |
   406	| `thm:ext-diagonal-vanishing` | `theorem` | 1349 | Ext diagonal vanishing criterion |
   407	| `prop:pbw-universality` | `proposition` | 1386 | PBW universality |
   408	| `cor:universal-koszul` | `corollary` | 1412 | Universal vertex algebras are chirally Koszul |
   409	| `thm:kac-shapovalov-koszulness` | `theorem` | 1478 | Kac--Shapovalov criterion for simple quotients |
   410	| `prop:li-bar-poisson-differential` | `proposition` | 1729 | Poisson differential on the Li--bar $E_1$ page |
   411	| `thm:associated-variety-koszulness` | `theorem` | 1800 | Associated-variety criterion for Koszulness |
   412	| `prop:large-orbit-obstruction` | `proposition` | 1902 | Nilradical obstruction at degenerate admissible levels |
   413	| `thm:koszul-equivalences-meta` | `theorem` | 2036 | Equivalences and consequences of chiral Koszulness |
   414	| `prop:koszul-closure-properties` | `proposition` | 2447 | Closure of chiral Koszulness under tensor, dualization, and base change |
   415	| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 2547 | Swiss-cheese non-formality by shadow class |
   416	| `prop:sc-formal-iff-class-g` | `proposition` | 2682 | SC-formality characterises class~$G$ |
   417	| `prop:d-module-purity-km` | `proposition` | 2785 | $\cD$-module purity for affine Kac--Moody algebras |
   418	| `prop:d-module-purity-km-equivalence` | `proposition` | 2807 | Kac--Moody equivalence via Saito--Kashiwara weight filtration |
   419	| `prop:koszulness-formality-equivalence` | `proposition` | 3121 | Koszulness as formality of the convolution algebra |
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '40,110p' compute/lib/cross_volume_shadow_bridge.py" in /Users/raeez/chiral-bar-cobar succeeded in 64ms:
  From landscape_census.tex: kappa(V_{E_8 lattice}) = rank = 8 for
  pure lattice VOAs, or kappa = 248*(1+30)/(2*30) for affine E_8_1.

  We will use the authoritative Vol I formulas and let the tests catch
  any discrepancies.

SHADOW DEPTH CLASSIFICATION (G/L/C/M, from Vol I):
  G (Gaussian, r_max = 2):   Heisenberg, pure lattice VOAs
  L (Lie/tree, r_max = 3):   affine Kac-Moody at all types
  C (contact/quartic, r_max = 4): beta-gamma, bc ghosts
  M (mixed, r_max = infinity):    Virasoro, W_N

COMPLEMENTARITY (Theorem C, AP24):
  kappa(A) + kappa(A!) = 0         for KM / free fields / lattice
  kappa(A) + kappa(A!) = 13        for Virasoro (c + (26-c))/2 = 13
  kappa(A) + kappa(A!) = 250/3     for W_3 (5c/6 + 5(100-c)/6)

SWISS-CHEESE FORMALITY (Vol II, AP14):
  SC-formal (m_k^{SC} = 0 for k >= 3): Heisenberg, lattice (class G only)
  SC-non-formal: affine KM (class L, m_3^{SC} != 0), beta-gamma (class C, m_4^{SC} != 0),
exec
/bin/zsh -lc "nl -ba archive/raeeznotes/raeeznotes100/red_team_summary.md | sed -n '100,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   100	- `thm:thqg-contact-termination` has statuses **ProvedElsewhere,ProvedHere** across instances: V1:ProvedHere:chapters/connections/thqg_gravitational_complexity.tex:549:Contact termination || V2:ProvedElsewhere:chapters/connections/thqg_gravitational_complexity.tex:551:Contact termination...
   101	- `lem:thqg-VII-genus-shifts` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_modular_bootstrap.tex:203:Genus shifts of the differential components || V2:Unknown:chapters/connections/thqg_line_operators_extensions.tex:2124:Planted-forest differential and genus shifts || V2...
   102	- `cor:thqg-I-genus-g-partition` has statuses **ProvedHere,Unknown** across instances: V1:ProvedHere:chapters/connections/thqg_perturbative_finiteness.tex:369:Genus-$g$ partition function || V2:Unknown:chapters/connections/thqg_perturbative_finiteness.tex:368:Genus-$g$ partition function...
   103	- `prop:thqg-III-kontsevich-pridham` has statuses **ProvedElsewhere,Unknown** across instances: V1:ProvedElsewhere:chapters/connections/thqg_symplectic_polarization.tex:857:{Kontsevich--Pridham correspondence; ;
   104	\cite{Pridham17}} || V2:Unknown:chapters/connections/thqg_symplectic_polarization.tex:855:...
   105	- `thm:grand-synthesis-principle` has statuses **Conditional,ProvedHere** across instances: V1:ProvedHere:chapters/connections/ym_boundary_theory.tex:128:Grand synthesis principle || V2:Conditional:chapters/connections/ym_synthesis.tex:36:Grand synthesis principle; \ClaimStatusConditional || V2:Conditional:chapters/connections/ym_...
   106	- `thm:conditional-mass-gap-transfer` has statuses **Conditional,Conjectured** across instances: V1:Conjectured:chapters/connections/ym_instanton_screening.tex:499:Conditional mass-gap transfer via screening domination || V2:Conditional:chapters/connections/ym_synthesis.tex:1616:Conditional mass-gap transfer via screening domination; \...
   107	- `conj:modular` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1278:Associative modular Maurer--Cartan class || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1396: || V2:ProvedHere:chapters/connections/ordered_associativ...
   108	- `conj:DS` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1309:Reduction commutes with associative chiral duality || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1457: || V2:ProvedHere:chapters/connections/ordered_...
   109	- `lem:PVA2_proof` has statuses **ProvedHere,Unknown** across instances: V2:Unknown:chapters/theory/pva-descent.tex:149:Alternative derivation of PVA2 via vertex algebra modes || V2:ProvedHere:chapters/theory/pva-descent-repaired.tex:375:Chain-level exchange homotopies; \ClaimStatusProvedHere...
   110	
   111	## Zones that currently survive the red-team pass better than the rest
   112	- Volume II foundations around Swiss-cheese recognition, PVA descent, FM/AOS cancellation, and bar-cobar rectification look substantially healthier than the speculative connection chapters.
   113	- Volume I core theory and the explicitly tagged examples are safer than the high-energy connection/frontier material, but still need local proof verification claim by claim.
   114	
   115	## Files produced
   116	- `master_claim_ledger_filtered.csv`: all filtered formal claims with attack swarms and dismissal stances.
   117	- `suspicious_proved_claim_dependencies.csv`: proved-here claims that locally depend on non-proved or unstable references.
   118	- `label_status_conflicts.csv`: same label with multiple statuses across files/volumes.
   119	- `informal_claim_harvest.csv`: harvested sentence-level explicit informal/meta claims.

thinking
**Summarizing SC formality references and remarks**

I'll organize key points about SC-formality invariants and proofs into a clear bullet list referencing relevant files and line ranges: highlighting CLAUDE invariants about SC placement, concordance classification with metadata verification, the proposition’s operadic proof and averaging remarks, plus the red team’s note on Volume I stability. I’ll also confirm that mentioning an operadic alternative proof viewpoint is consistent with existing reasoning and clarify SC bar versus derived center distinctions. This sets up a precise, friendly summary focusing on the user’s interest in repo invariants around SC-formality.
codex
**SC Formality Context**  
- `CLAUDE.md:5-16` insists the ordered bar `B^{\mathrm{ord}}(A)=T^c(s^{-1}A\textbar\))` is only an E₁ chiral coassociative coalgebra and never carries `SC^{\mathrm{ch,top}}`; the latter emerges on the derived center `Z^{\mathrm{der}}_{\mathrm{ch}}(A)=\ChirHoch^{\ast}(A,A)` via the bar resolution, so any reference to SC structure must live in the derived-center/averaging layer rather than on the bar itself.  
- `chapters/connections/concordance.tex:7196-7203` and `9782-9786` reframe SC-formality as equivalent to class G and part of the depth/classification slate, a statement whose provenance is catalogued in `metadata/theorem_registry.md:400-430` (see `prop:sc-formal-iff-class-g` at line 2682).

**Proof strategy & operadic remark potential**  
- `chapters/theory/chiral_koszul_pairs.tex:2651-2823` shows the Swiss-cheese table isolates the first nonzero mixed operation per shadow class, and the forward/backward directions both reduce to comparing mixed-sector tree sums with the shadow tower. The proof concludes by pointing out that the same genus‑0 tree-transfer formula (with identical propagators) produces both the mixed SC operations and the closed shadow invariants, differing only by output color and the averaging map `\operatorname{av}(\Theta^{\Eone})=\Theta` (`chapters/theory/chiral_koszul_pairs.tex:2805-2813`). That operadic correspondence already underpins the equivalence, so a remark describing an “operadic alternative proof” as the comparison of these tree-level operadic formulas (with the averaging map encoding the color change) would be accurate and consistent with the existing argument.

**Repository stability note**  
- `archive/raeeznotes/raeeznotes100/red_team_summary.md:111-113` flags Volume I core theory (where `prop:sc-formal-iff-class-g` lives) as one of the safer zones, but still notes that each formal claim needs a local verification pass; keep that in mind if you introduce new remarks or tightening.
wait(call_O1Vny4GnXKHYtb4I3X7rL5SC) 1 agents complete:
  019d869e-a72b-77a1-906f-b4f28761d20e completed: "**SC Formality Context**  
- `CLAUDE.md:5-16` insists the ordered bar `B^{\mathrm{ord}}(A)=T^c(s^{-1}A\textbar\))` is on…"

thinking
**Summarizing cross-volume conflicts and references**

I’m organizing a detailed summary highlighting conflicting statements about SC-formality across multiple volumes and files, noting discrepancies between claims like class G only versus class G/L being SC-formal. I’ll include cross-volume risks, key file references with line numbers, and group related points into clear bullets covering SC-formality, shadow tower concepts, B_{SC} usage, and collision/propagation risks for coherent verification.
collab wait(call_hXLyPucKMBxk35abpnNY5TIN)
  receivers: 019d869e-a82e-7092-852b-81571524b78a
codex
- **SC-formality = class G**  
  The canonical proof is in Vol I: the “SC-formality characterises class G” proposition (ch. theory `chiral_koszul_pairs`, lines 2786‑2818) shows SC-formality ⇔ the shadow tower truncates at degree 2 and therefore only the Gaussian families (Heisenberg/lattice/free fermion) survive. That statement is echoed in the constitutional summaries (`AGENTS.md:148‑158` and `chapters/connections/concordance.tex:7097‑7099`), and it is used to populate the landscape census table (`chapters/examples/landscape_census.tex:681‑708`, `standalone/classification.tex:22‑26`).  
  **Proof-outline collision:** Vol III’s Swiss‑cheese engine still writes “Vol I proves class G/L are SC-formal” (`calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py:62‑74`), which conflicts directly with the above proposition and would undo the requested outline if left unchecked. Any tweak to the proposition therefore has to reread the same classification surfaces in `AGENTS`, `CLAUDE`, `concordance`, the standalone summaries, and the compute layers.

- **Shadow tower + Δ = 8 κ S₄ + S₃ data**  
  The programme identity in `CLAUDE.md:11`/`AGENTS.md:65` declares the shadow tower the characteristic-class data produced by the bar/cobar constructions, and the discriminant formula `Δ = 8·κ·S₄` (CLAUDE C30, `CLAUDE.md:279`, `AGENTS.md:153`) governs whether the tower terminates (Δ=0 ⇔ classes G/L) or not. The cubic/quartic invariants (`S₃, S₄`) appear in both the depth tables (`chapters/examples/landscape_census.tex:681‑708`) and the arithmetic classification (`standalone/shadow_towers.tex`, `standalone/classification.tex:22‑26`), with S₃ distinguishing class L (S₃≠0) and class G/C (S₃=0). Changing any of those numerical claims should therefore propagate to the census, concordance, and all cross‑volume metadata that record the same triplet (κ, S₃, Δ).

- **B_{SC} / Swiss‑cheese structure rules**  
  The forbidden formula list keeps `B_{SC}(A)` off the single‑colour bar: SC is intrinsically two‑coloured and must be introduced via the promotion `A → (A,A)` so closed = Com, open = Ass, with a mixed sector (`CLAUDE.md:372`, `AGENTS.md:284`). Several “SC/promotion” audits (e.g., `wave2_audit_…/D13…`) re‑quote that line because treating `B_{SC}` as a one‑colour object leads to contradictory formulas. Any future edits touching Swiss‑cheese formality or bar constructions therefore need to re‑verify this rule (including the compute tests like `compute/tests/test_two_colored_bar_engine.py`).

- **Cross‑volume duplication and propagation risk**  
  Beyond the main proof surface, the same picture is repeated across the repo: `metadata/theorem_registry.md:416` records the proposition, `standalone/programme_summary.tex:1246,1783` and `standalone/preface_full_survey.tex:85` narrate the same classification, and Vol II chapters/compute scripts (`calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:58‑70`) restate SC-formality data. Conversely, Vol III’s `swiss_cheese_cy3_e1.py:62‑74` still carries the older “class G/L SC-formal” claim, which is the collision mentioned above. Any update to the SC-formality proof (or to Δ/S₃ data) therefore has to be mirrored in the concordance, metadata, standalone summaries, Vol II prefaces/bridges, and the Vol III compute libraries to avoid a split between the proof outline and these propagated descriptions.
wait(call_hXLyPucKMBxk35abpnNY5TIN) 1 agents complete:
  019d869e-a82e-7092-852b-81571524b78a completed: "- **SC-formality = class G**  
  The canonical proof is in Vol I: the “SC-formality characterises class G” proposition (…"

thinking
**Analyzing proof adjustments**

Okay, I need to analyze the user's request to add a Remark Operadic alternative proof with a specific outline. I think I should correct the current proof's incorrect mention of the Swiss-cheese bar complex. So, I'll aim to repair the proof and add that remark. I also need to look into the relevant theorems around shadow-formality-identification and shadow-tower-three-lenses for grounding the alternative proof. It seems reviewing those relevant lines and searching for the theorem makes sense too.
codex
The explorers confirmed the local proposition can support an operadic alternative proof, but they also surfaced a real wound: the existing converse currently says “Swiss-cheese bar complex,” which violates AP165. I’m now reading the exact dependency theorems that relate mixed SC trees to shadows so I can repair that proof and then add the new remark in a form that stays inside the repo’s SC conventions.
exec
/bin/zsh -lc "rg -n \"shadow-formality-identification|shadow-tower-three-lenses|e1-primacy|SC-formal|mixed-sector|averaging morphism|Theta_\\\\cA\" chapters/theory/chiral_koszul_pairs.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2440,2595p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:shadow-formality-identification|shadow-tower-three-lenses|e1-primacy|SC-formal|mixed-sector|averaging morphism|Theta_\cA)
                                                                                                                            ^^
error: unrecognized escape sequence
 succeeded in 54ms:

The shortest loop is
\[
\textup{(v)} \Longleftrightarrow \textup{(i)}.
\]
The backward implication is the repaired step in the proof:
for the universal twisting morphism
$\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
condition~\textup{(v)} is the quasi-isomorphism of the counit
$\varepsilon_{\tau_{\mathrm{univ}}}$, and
Theorem~\ref{thm:fundamental-twisting-morphisms}
identifies that directly with
$\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
This route uses the universal bar twisting datum and the bar
filtration, not the chain through \textup{(ii)} or \textup{(iii)}.

Condition~\textup{(i)} also implies condition~\textup{(viii)}
directly.
Theorem~\ref{thm:main-koszul-hoch},
Theorem~\ref{thm:hochschild-polynomial-growth}, and
exec
/bin/zsh -lc "sed -n '2360,2445p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Non-degeneracy $\det G_h \neq 0$ in the bar-relevant range
means the PBW-to-bar comparison map
$\iota \colon \operatorname{Sym}^{\mathrm{ch}}(V)_h \to
\barB_h(\cA)$ is injective at every bar-relevant weight~$h$.
Suppose $d_r \neq 0$ for some $r \geq 2$. Then there exists
$x \in E_r^{p,q}$ with $d_r(x) \neq 0$, represented by
$\tilde{x} \in F^p\barB$ with $d_{\mathrm{bar}}(\tilde{x})
\in F^{p+r}\barB$. If $\tilde{x} \in \operatorname{im}(\iota)$,
it represents a nonzero class in
$\operatorname{gr}^p(\barB) \cong \operatorname{Sym}^p(V)$,
and $d_r(\tilde{x})$ represents a nonzero class in
$\operatorname{gr}^{p+r}$. By PBW strictness (injectivity
of~$\iota$ at all bar-relevant weights), this contradicts the
acyclicity of $\operatorname{Sym}(V)$ as a Koszul complex.
Hence $d_r = 0$, giving~(ii) and hence~(i).

\medskip
\textsc{Ext diagonal vanishing}
\textup{(i)}$\Leftrightarrow$\textup{(iv)}:


thinking
**Finding theorem references**

I need to locate the exact theorem references and maybe some context surrounding them. It seems important to rerun the search correctly to ensure I gather the right information. I want to approach this methodically to avoid missing anything crucial. It feels like the details are key here, so I’ll focus on getting the right connections in my search. Alright, let’s get started and see what I can uncover!
exec
/bin/zsh -lc "rg -n 'shadow-formality-identification|shadow-tower-three-lenses|e1-primacy|mixed-sector|averaging morphism|Theta_\\\\cA|S_r\\\\(\\\\cA\\\\)' chapters/theory/chiral_koszul_pairs.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2240,2365p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1936

chapters/theory/chiral_koszul_pairs.tex:67:$\Theta_\cA^{\leq r}$, and five others. One (Hochschild
chapters/theory/chiral_koszul_pairs.tex:130:of the universal MC element $\Theta_\cA$
chapters/theory/chiral_koszul_pairs.tex:1210:The MC element $\Theta_\cA \in \MC(\mathfrak{g}_\cA^{\mathrm{mod}})$
chapters/theory/chiral_koszul_pairs.tex:1213:it says the genus-$0$ component $\Theta_\cA^{(0)}$ is
chapters/theory/chiral_koszul_pairs.tex:1222:reading~$\Theta_\cA^{(0)}$ through a different invariant
chapters/theory/chiral_koszul_pairs.tex:1304:shadow obstruction tower $\Theta_\cA^{\leq 3}, \Theta_\cA^{\leq 4},
chapters/theory/chiral_koszul_pairs.tex:1307:$\Theta_\cA^{\leq r}$ measure it at all genera.
chapters/theory/chiral_koszul_pairs.tex:1655:shadow triple $(\Theta_\cA, M_\cA, h_\cA)$: the propagator
chapters/theory/chiral_koszul_pairs.tex:2707:$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
chapters/theory/chiral_koszul_pairs.tex:2708:\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
chapters/theory/chiral_koszul_pairs.tex:2711:all higher mixed-sector operations vanish.
chapters/theory/chiral_koszul_pairs.tex:2744:$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
chapters/theory/chiral_koszul_pairs.tex:2745:\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
chapters/theory/chiral_koszul_pairs.tex:2747:the mixed-sector operations vanish:
chapters/theory/chiral_koszul_pairs.tex:2782:mixed-sector tree formulas with the degree-by-degree shadow tower
chapters/theory/chiral_koszul_pairs.tex:2812:closed sector applies the averaging morphism
chapters/theory/chiral_koszul_pairs.tex:2813:$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
chapters/theory/chiral_koszul_pairs.tex:2814:\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 succeeded in 51ms:
Because no mixed-weight channels exist on that lane, the
cross-channel correction $\delta F_g^{\mathrm{cross}}$ is absent,
so no positive-degree cohomology reappears. Hence
$H^k(\int_{\Sigma_g}\cA)=0$ for $k \neq 0$ for all $g \geq 0$ on
the uniform-weight lane.

\smallskip\noindent
\textup{(vii)}$\Rightarrow$\textup{(i)}:
Suppose $H^k(\int_{\mathbb{P}^1} \cA) = 0$ for $k \neq 0$ at $g = 0$
\textup{(}this genus-$0$ clause is the only input needed for the
converse\textup{)}. The factorization
homology $\int_{\mathbb{P}^1}\cA$ is computed by the bar complex:
$\int_{\mathbb{P}^1}\cA \simeq |\barBgeom(\cA)|$, the geometric
realization. Concentration in degree~$0$ means the bar spectral
sequence computing $H^*(\int_{\mathbb{P}^1}\cA)$ collapses, which
by Theorem~\ref{thm:pbw-koszulness-criterion} is Koszulness.

\begin{remark}[Scope of factorization-homology concentration]
\label{rem:fh-vii-uniform-weight-scope}
Condition~\textup{(vii)} has two layers. The genus-$0$ clause is
exec
/bin/zsh -lc "rg -n 'shadow-formality-identification|shadow-tower-three-lenses|e1-primacy' chapters/theory/chiral_koszul_pairs.tex chapters/frame/preface.tex chapters/connections/concordance.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:shadow-formality-identification|prop:shadow-tower-three-lenses|thm:e1-primacy)\\}' chapters/theory/chiral_koszul_pairs.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:15453:\label{thm:shadow-formality-identification}
chapters/theory/higher_genus_modular_koszul.tex:15727:\label{prop:shadow-tower-three-lenses}
chapters/theory/introduction.tex:1303:\label{thm:e1-primacy}
 succeeded in 51ms:
chapters/connections/concordance.tex:194: (Theorem~\ref{thm:shadow-formality-identification}).
chapters/connections/concordance.tex:2586:Theorem~\ref{thm:shadow-formality-identification}:
chapters/connections/concordance.tex:3842:\label{subsec:concordance-e1-primacy}
chapters/connections/concordance.tex:3850:Theorem~\ref{thm:e1-primacy}
chapters/connections/concordance.tex:4427:Proposition~\ref{prop:shadow-tower-three-lenses} identifies
chapters/connections/concordance.tex:7185:\ref{prop:shadow-tower-three-lenses}
chapters/frame/preface.tex:2634:(Theorem~\ref{thm:shadow-formality-identification}). The four
chapters/frame/preface.tex:3413:(Theorem~\ref{thm:shadow-formality-identification})
chapters/theory/chiral_koszul_pairs.tex:2708:\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
chapters/theory/chiral_koszul_pairs.tex:2745:\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
chapters/theory/chiral_koszul_pairs.tex:2814:\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
chapters/theory/chiral_koszul_pairs.tex:2817:By Theorem~\ref{thm:shadow-formality-identification} and
chapters/theory/chiral_koszul_pairs.tex:2818:Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
exec
/bin/zsh -lc "sed -n '15420,15540p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1290,1345p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '15700,15815p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the three binary trees with $3$ leaves, contracted
with the homotopy propagator $h \circ P_\cA$.
On cohomology, $[\ell_3^{(0)}] = 0$ because
$H^1(\overline{\mathcal{M}}_{0,4}) =
H^1(\mathbb{P}^1) = 0$. At chain level,
$\ell_3^{(0)}$ is exact but nonzero, and the
homotopy transfer formula gives
\[
\mathfrak{C}(\cA)
= -h\bigl(\ell_3^{(0)}(\Theta^{\leq 2},\,
\Theta^{\leq 2},\, \Theta^{\leq 2})\bigr).
\]
This is exactly the cubic shadow as computed in
Appendix~\ref{app:nonlinear-modular-shadows}:
the three-channel graph sum at degree~$3$ coincides
with the three-tree sum because each binary tree
with $3$ leaves corresponds to one of the $s$-, $t$-,
$u$-channel stable graphs.

\emph{Part~(iii).}
 succeeded in 52ms:
realization of~$\kappa$ as the holographic central charge: the
$r$-matrix encodes the boundary coupling, the shift encodes the
bulk renormalization, and the sum is the one-loop coefficient that
enters Theorem~D. The
shadow obstruction tower
$(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
degree-by-degree image of
$(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
(Proposition~\ref{prop:e1-shadow-r-matrix}). The $\Eone$ side
contains the matrix-valued meromorphic function; the $\Einf$ side
contains its $\Sigma_n$-symmetrized scalar.

\begin{theorem}[$\Eone$ primacy; \ClaimStatusProvedHere]
\label{thm:e1-primacy}
\index{primacy thesis!E1@$\Eone$|textbf}
\index{averaging map!information loss}
\index{Reynolds operator!as averaging map}
Let\/ $\cA$ be a cyclic chiral algebra on\/~$X$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Surjectivity.)}
 succeeded in 51ms:
\textbf{M} (mixed, $r_{\max} = \infty$): &
 $\mathfrak{h}$ is \emph{intrinsically non-formal}:
 no finite truncation of the $L_\infty$ structure is
 quasi-isomorphic to a dg~Lie algebra.
\end{tabular}
\end{center}
This is a homotopy-invariant classification:
$L_\infty$-formality of the minimal model does not depend on
the choice of strict model, contracting homotopy, or
representative of the quasi-isomorphism class. The shadow
depth is therefore an invariant of the modular homotopy type
(Definition~\ref{def:modular-homotopy-type}), not of any
particular presentation of the deformation complex.

The genus-$g$ corrections (BV operators $\ell_1^{(g)}$,
higher-genus Feynman amplitudes $\ell_n^{(g)}$) form a
separate, quantum layer on top of the genus-$0$ formality
tower. They contribute to the \emph{quantum} shadow
invariants $\operatorname{Sh}_{r,g}$ for $g \geq 1$ but do
not affect the genus-$0$ formality classification.
exec
/bin/zsh -lc "rg -n 'Swiss-cheese bar complex|mixed sector of the Swiss-cheese bar complex|SC-formal iff class G|Swiss-cheese formal iff class\\\\~\\\\"'$G'"\\\\"'$|m_k'"\\\\"'^'"\\\\{\\\\mathrm\\\\{SC\\\\}\\\\} = 0 for all \\\\Q?\\\\? k >= 3' . ../chiral-bar-cobar-vol2 ../calabi-yau-quantum-groups -g '*.tex' -g '*.md' -g '*.py'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Swiss-cheese bar complex|mixed sector of the Swiss-cheese bar complex|SC-formal iff class G|Swiss-cheese formal iff class\\~\\$G\\$|m_k\\^\\{\\mathrm\\{SC\\}\\} = 0 for all \\Q?\\? k >= 3)
                                                                                                                                                    ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n 'class G/L are SC-formal|class G.*SC-formal|class L.*SC-formal|SC-formal' ../calabi-yau-quantum-groups/compute ../chiral-bar-cobar-vol2/compute compute -g '*.py'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:58:  SC-formal (m_k^{SC} = 0 for k >= 3): Heisenberg, lattice (class G only)
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:62:  CRITICAL: SC-formality is DIFFERENT from chirally Koszul.
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:63:  ALL standard families are chirally Koszul.  Only class G is SC-formal.
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:291:    SC-formal means m_k^{SC} = 0 for k >= 3.  Only class G (Heisenberg)
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:292:    is SC-formal.  Class L has m_3^{SC} != 0, class C has m_4^{SC} != 0,
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:295:    CRITICAL (AP14): SC-formality is DIFFERENT from chirally Koszul.
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:296:    ALL standard families are chirally Koszul.  Only class G is SC-formal.
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:305:    For SC-formal families (class G only): returns float('inf').
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:311:    for k >= 3 are nonzero.  Only class G is SC-formal.
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:315:        return float("inf")  # SC-formal
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:482:# 7. VOL II BRIDGE -- SC-formality data
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:628:    SC-formality, complementarity, and cross-check status.
../calabi-yau-quantum-groups/compute/lib/cross_volume_shadow_bridge.py:639:    # SC-formality
compute/tests/test_gaiotto_3d_ht_comparison_engine.py:84:        """Class G families: r_max = 2, SC-formal."""
compute/tests/test_gaiotto_3d_ht_comparison_engine.py:90:            assert sd.sc_formal is True, f"{name} should be SC-formal"
compute/tests/test_gaiotto_3d_ht_comparison_engine.py:94:        """Class L families: r_max = 3, not SC-formal."""
compute/tests/test_gaiotto_3d_ht_comparison_engine.py:104:        """Class C families: r_max = 4, not SC-formal."""
compute/tests/test_gaiotto_3d_ht_comparison_engine.py:113:        """Class M families: r_max = infinity, not SC-formal."""
compute/tests/test_gaiotto_3d_ht_comparison_engine.py:327:        """Heisenberg is SC-formal even at d'=1 (GKW would say 'non-formal')."""
compute/tests/test_gaiotto_3d_ht_comparison_engine.py:754:        """SC-formality holds if and only if class G (multi-path check)."""

thinking
**Inspecting file details**

I need to take a close look at the current file since there might be an inaccurate statement about the "mixed sector of the Swiss-cheese bar complex." I think it should possibly say "mixed sector of the Swiss-cheese structure on the pair (Z^{der}_{ch}(\cA),\cA)" or something similar. I should also read through the concordance around SC and search for the exact statement regarding the SC structure pair.
exec
/bin/zsh -lc "sed -n '438,452p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3828,3858p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6878,6892p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \emph{Chiral center theorem
 (Theorems~\textup{\ref{thm:operadic-center-hochschild}}
 and~\textup{\ref{thm:chiral-deligne-tamarkin}}).}
 The chiral Hochschild cochain complex
 $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the operadic center of a
 logarithmic chiral algebra~$\cA$ in the holomorphic--topological
 Swiss-cheese operad $\mathsf{SC}^{\mathrm{ch,top}}$. The pair
 $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$ is terminal in the
 category of local chiral Swiss-cheese pairs over~$\cA$: for every
 such pair $(B, \cA, \mu)$, there exists a unique morphism
 $\Phi \colon B \to C^\bullet_{\mathrm{ch}}(\cA,\cA)$
 intertwining the brace structures and the mixed operations.
 Two independent proofs: (i)~operadic, via the recognition theorem
 and homotopy-Koszulity of~$\mathsf{SC}^{\mathrm{ch,top}}$
 (\S\ref{sec:operadic-center-theorem}); (ii)~direct, via the
 succeeded in 55ms:
(Definition~\ref{def:modular-convolution-dg-lie}) uses the
symmetric bar~$B^\Sigma$. The
Swiss-cheese two-colour structure $\SCchtop$ of Volume~II uses
the ordered bar~$B^{\mathrm{ord}}$ for the open colour and
$B^\Sigma$ for the closed colour. The Harrison
bar~$B^{\mathrm{Lie}}$ appears as the primitives of~$B^\Sigma$
and controls the Francis--Gaitsgory chiral Lie Koszul duality.
The three bar complexes produce three
different Koszul duals: $B^{\mathrm{Lie}}$ gives the chiral Lie
dual, $B^\Sigma$ gives $\cA^!_{\mathrm{ch}}$ (Volume~I,
Theorem~A), and $B^{\mathrm{ord}}$ gives the ordered/line-side
dual $\cA^!_{\mathrm{line}}$.

\subsection{$E_1$ primacy}
\label{subsec:concordance-e1-primacy}
\index{E1 primacy@$E_1$ primacy|textbf}
\index{averaging map|textbf}

The $E_1$/ordered story is the natural primitive of the
modular Koszul duality.
 succeeded in 52ms:
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
/bin/zsh -lc "rg -n 'Operadic alternative proof|alternative proof' chapters/theory/chiral_koszul_pairs.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3031:\index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
chapters/theory/higher_genus_modular_koszul.tex:3032:\index{Hodge bundle!alternative proof of Theorem D}
chapters/theory/higher_genus_modular_koszul.tex:4228:installed, it furnishes an alternative proof path to MC2.
chapters/theory/higher_genus_modular_koszul.tex:17721:\index{shadow algebra!depth gap alternative proof}



thinking
**Adjusting proof complexities**

I’m working on refining my current proof, particularly focusing on fixing the false bar complex. There’s an alternative approach that might involve citing the theorem about shadow-formality identification and properties of shadow tower three lenses as part of a fully operadic framework. However, I should avoid making claims about the B_SC formal dg-object and Massey products, since that seems not rigorous and conflicts with the established structures. Time to adjust!
thinking
**Clarifying an operadic proof**

I’m noticing that for `S_r=0` when `r>=3`, it leads to class G, which is purely operadic. However, the user specifically asked for a "purely operadic alternative proof of both directions" and mentioned avoiding the bilinear-form argument. There’s a lot to consider here as I think about how to respond appropriately to their request while ensuring clarity and relevance. It's interesting to navigate between these different aspects!
thinking
**Examining tree decomposition**

I'm considering that in class G, every connected tree with `r>=3` decomposes into binary pairings. This results in the mixed operation and its closed projection vanishing, which helps avoid unsafe projection-only implications. I think I might not need to oversell the formula. Instead, I could phrase it like, “Once `S_r=0` is determined, that indicates the absence of a primitive degree-r tree in the Gaussian case," for clarity.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:shadow-archetype-classification\\}|class~\\\\"'$G'"\\\\"'$|truncates at degree~'"\\\\"'$2'"\\\\"'$|S_r'"\\\\(\\\\cA\\\\)=0 for \\\\w* r \\\\geq 3' chapters/theory/chiral_koszul_pairs.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:16843:\label{thm:shadow-archetype-classification}
exec
/bin/zsh -lc "sed -n '17230,17340p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc "sed -n '16843,16990p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{thm:shadow-archetype-classification}
\ClaimStatusProvedHere
\index{shadow depth!classification theorem|textbf}
\index{shadow archetype classification|textbf}
Every chirally Koszul algebra in the standard landscape has algebraic
shadow depth
\[
 d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
\]
Equivalently, it belongs to exactly one of the shadow depth classes
$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
The class is determined by the vanishing pattern of obstruction
classes at degrees~$3$, $4$, $5$, and the assignments for the
primitive archetypes are as follows:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Gaussian \textup{(}$\mathbf{G}$,
$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}
 Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
 All higher obstruction classes vanish:
codex
I’ve pinned the exact logical gap. The requested converse path “`S_3=0 ⇒ Δ=0 ⇒ class G`” is not valid in this repo’s classification, because `Δ=0` still allows class `L`. I’m rewriting the proof lane around the actual invariant that characterises class `G`, namely full truncation `S_r=0` for every `r≥3`, and I’ll keep the new remark purely operadic without `B_{SC}` language.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`

thinking
**Planning the structure**

I might need to use build-surface later. That seems good. I should also inspect the style of the remark and decide where to insert it. It feels natural to add a proposition proof before the next remark. I’ll likely need to adjust the proof and add a new remark afterward. I think I should use apply_patch too. Before editing, I need the PE-10 commentary block, and I might mention the AP165 check for no SC bar. Let's prepare the commentary with a fenced block.
codex
```text
PE-10
genus: all
degree: all higher arities k >= 3
AP32 weight tag: NA  tagged? Y
AP139 free-var audit: LHS vars:{A,k} RHS vars:{A,k,S_r,class G}  LHS⊇RHS? Y
AP36: implies/iff  if iff, converse proved same thm? Y

AP165 check
SC datum used in converse: pair (C^\bullet_ch(A,A), A) / mixed-tree formulas, not B(A) as an SC coalgebra
forbidden "Swiss-cheese bar complex" language after edit: must be absent

verdict: ACCEPT
```

thinking
**Clarifying classification theorems**

I need to verify that Theorem refers to class G as precisely the Gaussian locus, specifically mentioning the shadow tower truncation at degree 2. It's essential to clarify that the converse applies full vanishing \( S_r=0 \) for all \( r \geq 3 \), not just \( \Delta=0 \). Class L still holds \( \Delta=0 \) but has \( S_3 \neq 0 \). It's crucial to avoid misconceptions about the converse. Since the user mentioned delta, I’ll point out that the discriminant only covers the quartic stage. I'll ensure the remark is titled "Operadic alternative proof."
codex
I’ve got the exact edit shape. I’m patching two things in the target file: first, repairing the existing converse so it no longer attributes SC structure to a bar complex; second, adding the new `Remark[Operadic alternative proof]` with a fully operadic `iff` argument based on genus-zero tree transfer and the averaging map.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2805,9 +2805,11 @@
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure on the universal
+open/closed pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2825,2 +2827,40 @@
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure on
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
apply_patch(auto_approved=true) exited 0 in 41ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..7f30f1f9f8b40e4a028997079ef7b709413d83ba
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,15 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure on the universal
+open/closed pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2825,44 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure on
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..7f30f1f9f8b40e4a028997079ef7b709413d83ba
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,15 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure on the universal
+open/closed pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2825,44 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure on
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}


thinking
**Verifying content for editing**

I need to verify the content I’m working on and check if the `C^\bullet_{\mathrm{ch}}` macro is acceptable, especially since the same file uses `\ChirHoch`. I’ll take a moment to re-read everything to ensure clarity and consistency. It’s important to get this right, so I’ll double-check my understanding of the contents. Let’s make sure everything aligns well with the formatting guidelines!
codex
The proof surface is patched. I’m re-reading the edited block now for two specific failure modes: any residual forbidden `SC`-on-bar phrasing, and any converse step that accidentally reduces class `G` to `Δ=0` instead of full shadow truncation.
exec
/bin/zsh -lc "sed -n '2792,2865p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Swiss-cheese bar complex|B_\\{SC\\}|B\\(A\\).*SC|SC.*bar complex|class~\\\\"'$L'"\\\\ also has \\\\Delta = 0|Delta = 8\\\\kappa S_4' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
if and only if~$\cA$ belongs to class~$G$.
\end{proposition}

\begin{proof}
The forward direction \textup{(}class~$G$ $\Longrightarrow$
SC-formal\textup{)} is established in
Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
the class-$G$ row consists of the Gaussian families Heisenberg,
lattice VOA, and free fermion, and in each case the genus-$0$
mixed tree formulas stop at arity~$2$, so
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.

For the converse, suppose~$\cA$ is SC-formal.
Then every mixed Swiss-cheese operation of arity~$r \geq 3$
vanishes in the Swiss-cheese structure on the universal
open/closed pair
$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
The tree-shadow correspondence is operadic: the arity-$r$ mixed
tree and the degree-$r$ shadow are produced by the same genus-$0$
 succeeded in 50ms:
114:and the critical discriminant $\Delta = 8\kappa S_4$, whose
2635:governed by the discriminant $\Delta = 8\kappa S_4$.
2727:$\Delta = 8\kappa S_4 \neq 0$ forces all higher operations to be
2767:$S_4 = 10/[c(5c{+}22)]$ and $\Delta = 8\kappa S_4 = 40/(5c{+}22) \neq 0$
2856:$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..7f30f1f9f8b40e4a028997079ef7b709413d83ba
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,15 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure on the universal
+open/closed pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2825,44 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure on
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}



thinking
**Considering theorem citations**

I’m realizing I need a more rigorous approach. Instead of just referencing certain theorems, I might consider citing specific propositions to maintain independence from existing proof paths. That can make the argument stronger. Also, while I could mention the structural facts about the Gaussian families, I want to ensure that I'm not mixing family-specific computation with theorems. Making sure my references align well is important for clarity in this context. I need to think this through a bit more!
thinking
**Citing theorems and propositions**

I'm thinking it might be necessary to maintain rigor by citing relevant corollaries or theorems concerning lattices. I'll need to search for suitable references. I could look into the proposition related to nonformality by class, but that might be too close for comfort. Maybe, in my remark, I could succinctly clarify that "the forward direction is the operadic part of the class-G mechanism, already isolated in the earlier proposition," while noting the ordered bar data on the Gaussian locus.
exec
/bin/zsh -lc "rg -n 'C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA,\\\\cA\\)|universal open/closed pair|C\\\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}|ChirHoch\\"'^'"\\*\\(\\\\cA,\\\\cA\\)' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2809:$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
2847:$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..7f30f1f9f8b40e4a028997079ef7b709413d83ba
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,15 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure on the universal
+open/closed pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2825,44 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure on
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

exec
/bin/zsh -lc "rg -n 'derived center|ChirHoch|Hochschild' chapters/theory/chiral_koszul_pairs.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
67:$\Theta_\cA^{\leq r}$, and five others. One (Hochschild
1219:Hochschild consequence on the Koszul locus, one conditional on
2047:them on the Koszul locus: it yields Hochschild duality,
2096:\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
2098:\item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
2101: \ChirHoch^n(\cA)
2102: \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X
2104: with Hochschild--Hilbert series
2106: P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\cdot t
2109: and $\ChirHoch^*(\cA)$ is formal as an $\Etwo$-algebra;
2167:\textsc{Hochschild consequence}
2173:bar-cobar resolution with the chiral Hochschild complex. On the
2182:braces and Massey products on $\ChirHoch^*(\cA)$ are
2277:\begin{remark}[The strongest proved Hochschild consequence]
2281:$\ChirHoch^*(\cA)$ is free. At generic central charge,
2284:\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2].
2287:$\ChirHoch^4(\mathrm{Vir}_c)=0$, whereas a free
2462:$\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
3114:The nine unconditional equivalences and the Hochschild
3412:and the Hochschild consequence~\textup{(viii)} no longer follows.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..7f30f1f9f8b40e4a028997079ef7b709413d83ba
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,15 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure on the universal
+open/closed pair
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2825,44 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure on
+$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}


thinking
**Considering Gaussian locus**

I’m thinking about how to describe the Gaussian locus, where the ordered bar data is generated by the binary two-point kernel. I wonder if I should reference the class-G mechanism in a previous proposition, but maybe it's not necessary since it's an alternative proof remark. I need to ensure that the alternative proof path is clear, independent of the bilinear-form argument. I’ll adjust the sentence for clarity and remove any unnecessary citations. Let's clarify the tree-shadow correspondence in the proof.
codex
The local reread exposed one style issue, not a logical one: I introduced the explicit pair `\((C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)\)` without any local setup in this chapter. I’m tightening that phrasing now so the proof stays precise about SC operations without adding undeclared notation to this lane.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2806,5 +2806,3 @@
 Then every mixed Swiss-cheese operation of arity~$r \geq 3$
-vanishes in the Swiss-cheese structure on the universal
-open/closed pair
-$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
 The tree-shadow correspondence is operadic: the arity-$r$ mixed
@@ -2845,4 +2843,3 @@
 genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
-structure on
-$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$.
+structure with open colour~$\cA$.
 By Theorem~\ref{thm:shadow-formality-identification},
apply_patch(auto_approved=true) exited 0 in 38ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..16d52c924b508b356e4d6be35a75a72360e73084
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2823,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..16d52c924b508b356e4d6be35a75a72360e73084
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2823,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

exec
/bin/zsh -lc "sed -n '2800,2862p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Swiss-cheese bar complex|B_\\{SC\\}|C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA,\\\\cA\\\\)' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the class-$G$ row consists of the Gaussian families Heisenberg,
lattice VOA, and free fermion, and in each case the genus-$0$
mixed tree formulas stop at arity~$2$, so
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.

For the converse, suppose~$\cA$ is SC-formal.
Then every mixed Swiss-cheese operation of arity~$r \geq 3$
vanishes in the Swiss-cheese structure with open colour~$\cA$.
The tree-shadow correspondence is operadic: the arity-$r$ mixed
tree and the degree-$r$ shadow are produced by the same genus-$0$
tree-transfer formula, with the same propagator on internal edges;
the only difference is the output colour, and passage to the
symmetric closed sector applies the averaging morphism
$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
there is no higher mixed tree whose closed projection could survive.
By Theorem~\ref{thm:shadow-formality-identification} and
Proposition~\ref{prop:shadow-tower-three-lenses}, this is exactly
the statement that the shadow/formality tower truncates at
 exited 2 in 52ms:
rg: regex parse error:
    (?:Swiss-cheese bar complex|B_\{SC\}|C\^\\bullet_\{\\mathrm\{ch\}\}\(\\cA,\\cA\\))
                                                                                     ^
error: unopened group
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..16d52c924b508b356e4d6be35a75a72360e73084
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2823,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

exec
/bin/zsh -lc "rg -n -F 'Swiss-cheese bar complex' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'B_{SC}' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -F 'C"'^'"\\bullet_{\\mathrm{ch}}(\\cA,\\cA)' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..16d52c924b508b356e4d6be35a75a72360e73084
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2823,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}


thinking
**Evaluating build options**

I need to run a build and test, possibly using the build-surface skill. It seems I should choose the narrowest option. I'm considering using `make fast` or `latexmk`. I'll need to inspect the Makefile to see what make targets are available. There's a bit of decision-making to do, but I'm sure I can figure it out! I'll make it work. Let's take it one step at a time!
codex
The text is clean on the two targeted invariants: no residual `SC`-on-bar phrase and no reintroduction of the false `Δ=0 ⇒ class G` converse. I’m doing one narrow verification step now: a local LaTeX build check on the manuscript surface to catch any syntax or reference damage from the insertion.
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'^([A-Za-z0-9_-]+:|'"\\.PHONY)' Makefile makefile GNUmakefile" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
bibliography
bp_self_duality.pdf
 exited 2 in 51ms:
rg: GNUmakefile: No such file or directory (os error 2)
makefile:81:.PHONY: all fast watch clean veryclean count check draft integrity phase0-index metadata verify census test editorial standalone annals archive dist release help working-notes publish icloud
makefile:84:icloud: main.pdf
makefile:93:all: $(STAMP) working-notes publish
makefile:114:fast:
makefile:121:working-notes: $(OUT_WN)
makefile:138:publish:
makefile:144:release:
makefile:220:watch:
makefile:226:check:
makefile:238:integrity:
makefile:242:phase0-index:
makefile:246:draft:
makefile:260:clean:
makefile:271:veryclean: clean
makefile:277:count:
makefile:293:metadata:
makefile:298:census: metadata
makefile:302:audit: metadata
makefile:306:verify:
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..16d52c924b508b356e4d6be35a75a72360e73084
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2823,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}


thinking
**Considering output options**

I’m thinking that "fast" might be too narrow as a target. I might need to inspect what I’m aiming for or consider using "make fast" instead. It could help clarify the output. I wonder if running it with maximum output would provide enough details. It's essential to find the right balance here to ensure I get the information right and useful for what I need to accomplish!
exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..16d52c924b508b356e4d6be35a75a72360e73084
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2823,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..16d52c924b508b356e4d6be35a75a72360e73084
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2823,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..16d52c924b508b356e4d6be35a75a72360e73084
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2803,13 +2803,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2823,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

codex
The build is still running, so I’m waiting rather than guessing at the result. Once it settles I’ll inspect the log specifically for the edited proposition/remark surface, not just the top-level pass banner.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}


thinking
**Inspecting build process**

I'm considering how to handle a long build process. Maybe I should inspect it further? Possibly using another session to tail the logs could help. Since the build is ongoing, it might make sense to use an exec command to view the main log or check running processes. But maybe it's okay as it is. I think doing both in parallel could be useful—like using `ps` and tailing the log at the same time!
exec
/bin/zsh -lc 'tail -n 60 main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
undefined on input line 147.


LaTeX Warning: Reference `rem:unifying-principle' on page 1836 undefined on inp
ut line 152.


LaTeX Warning: Reference `sec:concordance-three-pillars' on page 1836 undefined
 on input line 159.


LaTeX Warning: Reference `cor:nms-betagamma-mu-vanishing' on page 1836 undefine
d on input line 164.


LaTeX Warning: Reference `const:vol1-genus-two-shells' on page 1836 undefined o
n input line 182.


LaTeX Warning: Reference `cor:nms-betagamma-mu-vanishing' on page 1836 undefine
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}



thinking
**Considering build issues**

It looks like the build might still be running, but it’s unclear if it’s stable. I could check the logs to find new errors, but the user probably doesn’t need the complete build just yet. If it's taking too long, I should mention that it hasn’t finished. I might also run a command to see if there are undefined references. Overall, I’m thinking it might be best to stop waiting and report that the build didn't complete within the available time.
thinking
**Evaluating the build process**

I’m considering whether our change is just text and if I could run `python3 scripts/check_tex_refs.py` to check for references. I’m not entirely sure if that’s the right move, but I think the build should be enough if it eventually completes. I can still monitor the build process, but it might be silent until it’s finished. I should give it another 30 seconds or so to see if anything changes.
codex
The manuscript build hasn’t returned control yet, and the log tail only shows pre-existing undefined references far from this theorem lane. I’m giving it one more interval; if it still doesn’t settle, I’ll close on the verified local text checks and report the build as inconclusive rather than pretending it passed.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}


thinking
**Evaluating progress**

I'm thinking about my current progress. The build is on track, and I'm considering if I should finalize everything after the second pass. Maybe it would make sense to stop now? But, I wonder if a final exit is still needed. I'm also contemplating whether I might need a shorter poll to gather any last feedback. It feels like there are a few decisions to weigh here.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

 exited 2 in 3m 50s:
  ── Fast build (up to 4 passes) ──
Building main.tex (up to 4 passes)
── Pass 1 / 4 ──
   2696pp, 2000 undef citations, 7743 undef references, 2 rerun requests, 164 overfull, 281 underfull
── Pass 2 / 4 ──
   2714pp, 2639 undef citations, 6465 undef references, 1 rerun requests, 205 overfull, 446 underfull
✗ Build failed.
  Logs: .build_logs/tex-build.stdout.log and main.log
./chapters/theory/en_koszul_duality.tex:3513: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4183: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4186: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4497: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4499: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4499: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4505: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4508: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4508: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4571: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4571: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4572: Undefined control sequence.

thinking
**Investigating build errors**

It looks like the build failed due to unrelated errors in `en_koszul_duality` and `main.aux`, which might have been there before. I need to inspect the file to see if there were any new errors added. I should also check the log for `chiral_koszul_pairs` around those lines, although it seems like there might not be any. Maybe using `grep` could help narrow things down. Let’s sort this out!
exec
/bin/zsh -lc "rg -n 'chiral_koszul_pairs|prop:sc-formal-iff-class-g|Operadic alternative proof|Undefined control sequence|Fatal error' main.log .build_logs/tex-build.stdout.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.log: binary file matches (found "\0" byte around offset 54221)
 succeeded in 51ms:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}



thinking
**Investigating git diff output**

I'm thinking about why I'm not seeing any output from git diff. It might be that no changes are tracked, or perhaps the repository isn't a git repo at all. I wonder if I should check the git status first. There’s also a chance that the diff output is suppressed because of a pager. Maybe trying `git diff --stat` could help shed some light on the situation.
thinking
**Considering git commands**

I think I need to check my Git command and maybe use `git diff --word-diff=plain --...`. I'm trying to figure out the best way to compare changes. This option seems like it could help highlight the differences more clearly. I’ll take a closer look and see if it gives me the formatted output that I’m looking for. If I need to adjust it, I can also explore other options.
codex
The build failure is not on the edited file. `make fast` died inside unrelated `en_koszul_duality.tex` undefined-control-sequence errors, so I’m treating build verification as blocked by pre-existing breakage and doing a final diff/readback check on the actual theorem surface instead.
exec
/bin/zsh -lc 'git status --short -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --unified=3 --no-ext-diff -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 51ms:

exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
p=Path('chapters/theory/chiral_koszul_pairs.tex')
text=p.read_text()
start=text.index('\\\\begin{proposition}[SC-formality characterises class~"'$G$; '"\\\\ClaimStatusProvedHere]')
end=text.index('\\\\begin{remark}[D-module purity: reduction to a single gap]')
print(text[start:end])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
\label{prop:sc-formal-iff-class-g}
\index{Swiss-cheese operad!formality characterisation}
\index{class G@class~$G$!characterised by SC-formality}
Let~$\cA$ be a chiral algebra in the standard landscape.
Then~$\cA$ is Swiss-cheese formal
\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
if and only if~$\cA$ belongs to class~$G$.
\end{proposition}

\begin{proof}
The forward direction \textup{(}class~$G$ $\Longrightarrow$
SC-formal\textup{)} is established in
Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
the class-$G$ row consists of the Gaussian families Heisenberg,
lattice VOA, and free fermion, and in each case the genus-$0$
mixed tree formulas stop at arity~$2$, so
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.

For the converse, suppose~$\cA$ is SC-formal.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}


thinking
**Checking file status and line numbers**

I think I need to check the git status or diff because the file might be modified but not tracked. That's a bit odd. It’s possible the repository uses something non-git, but I think it's probably okay. It's not crucial right now. I should also check the line numbers for the final file link. Maybe I can use `nl -ba` to show line numbers around the lines. I'll reference the file and use `exec` for that.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2798,2865p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2798	$\beta\gamma\beta\gamma$ channel computation; termination at
  2799	depth~$4$ follows from rank-one rigidity
  2800	(Theorem~\ref{thm:riccati-algebraicity}).
  2801	Class~$M$:
  2802	$S_3 = (\text{scalar projection of } T_{(1)}T)/T_{(3)}T
  2803	= 2\kappa/\kappa = 2$, independent of~$c$;
  2804	$S_4 = 10/[c(5c{+}22)]$ and $\Delta = 8\kappa S_4 = 40/(5c{+}22) \neq 0$
  2805	for generic~$c$, so the Riccati algebraicity theorem
  2806	forces the tower to be infinite.
  2807	Computational verification:
  2808	\texttt{theorem\_ainfty\_nonformality\_class\_m\_engine.py}
  2809	(three independent methods for $S_3$,
  2810	quartic shadow $S_4$ and $Q^{\mathrm{contact}}$, quintic
  2811	shadow $S_5 = -48/(c^2(5c+22))$, all four classes verified).
  2812	\end{proof}
  2813	
  2814	The four classes exhaust the standard landscape, but the
  2815	relationship between SC-formality and the classification is
  2816	sharper than the table suggests. Proposition~\ref{prop:swiss-cheese-nonformality-by-class}
  2817	already isolates the first nonzero Swiss-cheese operation in each
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2863,2908p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2863	\begin{remark}[Operadic alternative proof]
  2864	\index{Swiss-cheese operad!operadic alternative proof}
  2865	Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
  2866	path that stays entirely in the genus-$0$ operadic transfer formalism.
  2867	
  2868	For the forward direction, class~$G$ means that the shadow tower
  2869	truncates at degree~$2$:
  2870	$S_r(\cA) = 0$ for every $r \geq 3$
  2871	\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
  2872	Equivalently, the ordered bar data is generated by the binary
  2873	two-point kernel, so every connected Swiss-cheese tree of arity
  2874	$r \geq 3$ factors through binary pairings and has no primitive
  2875	higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
  2876	from those same genus-$0$ trees, hence
  2877	$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
  2878	
  2879	For the converse, assume~$\cA$ is SC-formal. Then every mixed
  2880	genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
  2881	structure with open colour~$\cA$.
  2882	By Theorem~\ref{thm:shadow-formality-identification},
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..6811a000b216ba6b3eead4ae94d181055b159af1
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+Equivalently, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2871,3 +2871,3 @@
 \textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
-Equivalently, the ordered bar data is generated by the binary
+On this Gaussian locus, the ordered bar data is generated by the binary
 two-point kernel, so every connected Swiss-cheese tree of arity
apply_patch(auto_approved=true) exited 0 in 28ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..389603ff45abad20d877d89eeda5d9cb2b3cf40c
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+On this Gaussian locus, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..389603ff45abad20d877d89eeda5d9cb2b3cf40c
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+On this Gaussian locus, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

exec
/bin/zsh -lc "sed -n '2868,2897p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For the forward direction, class~$G$ means that the shadow tower
truncates at degree~$2$:
$S_r(\cA) = 0$ for every $r \geq 3$
\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
On this Gaussian locus, the ordered bar data is generated by the binary
two-point kernel, so every connected Swiss-cheese tree of arity
$r \geq 3$ factors through binary pairings and has no primitive
higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
from those same genus-$0$ trees, hence
$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.

For the converse, assume~$\cA$ is SC-formal. Then every mixed
genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
structure with open colour~$\cA$.
By Theorem~\ref{thm:shadow-formality-identification},
Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
identity
$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
the degree-$r$ shadow $S_r(\cA)$ is the
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..389603ff45abad20d877d89eeda5d9cb2b3cf40c
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+On this Gaussian locus, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}


thinking
**Checking for build errors**

I need to search and see if there's a build error due to an undefined control sequence. I might grep the `.build_logs/tex-build.stdout.log` for specific lines, but it might not be necessary. I could also consider using `strings` on the main log, although it seems binary. Still, that might be not needed. It might be worth running a command to check for keywords related to errors in the logs and confirm there are no issues.
exec
/bin/zsh -lc "rg -n -a 'chiral_koszul_pairs|Operadic alternative proof|Undefined control sequence|Fatal error' main.log .build_logs/tex-build.stdout.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.log:5071:\openout2 = `chapters/theory/chiral_koszul_pairs.aux'.
main.log:5073:(./chapters/theory/chiral_koszul_pairs.tex
main.log:16146:./chapters/theory/en_koszul_duality.tex:3513: Undefined control sequence.
main.log:16317:./chapters/theory/en_koszul_duality.tex:4183: Undefined control sequence.
main.log:16326:./chapters/theory/en_koszul_duality.tex:4186: Undefined control sequence.
main.log:16384:./chapters/theory/en_koszul_duality.tex:4497: Undefined control sequence.
main.log:16393:./chapters/theory/en_koszul_duality.tex:4499: Undefined control sequence.
main.log:16402:./chapters/theory/en_koszul_duality.tex:4499: Undefined control sequence.
main.log:16411:./chapters/theory/en_koszul_duality.tex:4505: Undefined control sequence.
main.log:16420:./chapters/theory/en_koszul_duality.tex:4508: Undefined control sequence.
main.log:16431:./chapters/theory/en_koszul_duality.tex:4508: Undefined control sequence.
main.log:16440:./chapters/theory/en_koszul_duality.tex:4571: Undefined control sequence.
main.log:16451:./chapters/theory/en_koszul_duality.tex:4571: Undefined control sequence.
main.log:16460:./chapters/theory/en_koszul_duality.tex:4572: Undefined control sequence.
main.log:39206:ory/poincare_duality.aux) (./chapters/theory/chiral_koszul_pairs.aux) (./chapte
main.log:59875:./main.aux:158:  ==> Fatal error occurred, no output PDF file produced!
main.log:68626:./main.aux:158:  ==> Fatal error occurred, no output PDF file produced!
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..389603ff45abad20d877d89eeda5d9cb2b3cf40c
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+On this Gaussian locus, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}



thinking
**Mentioning build errors**

I think I need to note that the build was blocked due to unrelated errors in `chapters/theory/en_koszul_duality.tex`. Also, it seems like the computed surfaces are inconsistent, possibly because they weren't addressed in the current scope. Should I mention that my confidence in the primary proof is high? After all, it's sound and maybe repaired. I also need to ensure the final output is structured as requested with `## Fortification Report`.
thinking
**Structuring theorem proofs**

The user specified, "For each theorem: - PRIMARY PROOF ...". I'm thinking of using short paragraphs for theorem names followed by a flat list. It might make sense to structure it as: `prop:sc-formal-iff-class-g` ([...]): PRIMARY PROOF: repaired; SECONDARY PROOF: written; TECHNIQUE: ...; CONDITION STATUS: unconditional; CONFIDENCE: high. This provides a clear structure. I also want to include a brief mention of the manuscript build status and any pending issues with clickable file links.
codex
I repaired the converse of `prop:sc-formal-iff-class-g` and added the requested `Remark[Operadic alternative proof]` in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2823) and [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2863). The key correction is that I did not use the requested `B_{SC}` / `Δ=0 \Rightarrow` class `G` converse, because that is not true on the manuscript’s own classification surface: class `L` still has `\Delta=0`. The new converse instead uses the full operadic vanishing pattern `S_r=0` for all `r\ge 3`, via the genus-0 transfer tree and the averaging map `\operatorname{av}(\Theta^{E_1}_\cA)=\Theta_\cA`.

Verification: I ran `make fast`. The build failed outside this edit, on pre-existing undefined-control-sequence errors in [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3513), so there is no clean full-manuscript build verdict from this turn.

## Fortification Report
- `prop:sc-formal-iff-class-g` in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2823): PRIMARY PROOF: repaired; SECONDARY PROOF: written; TECHNIQUE: genus-0 operadic transfer plus the shadow/formality dictionary and `E_1` averaging; CONDITION STATUS: unconditional; CONFIDENCE: high.

Pending collision surface: `../calabi-yau-quantum-groups/compute/lib/swiss_cheese_cy3_e1.py` still appears to advertise a stale SC-formality classification, but I did not edit it because this turn’s write scope was the target manuscript file.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0be8f3aa5ecafa9db9ea60376ef554d037de4b9f..389603ff45abad20d877d89eeda5d9cb2b3cf40c
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2435,44 +2435,68 @@
 
 \begin{remark}[Proof web redundancy]
 \label{rem:koszul-proof-web-redundancy}
-The proof above need not be read as a line.
-Several arrows close independently of the PBW-to-shadow route.
-
-The shortest loop is
+The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
+single chain.
+Its unconditional core already has several proof lanes that do not
+route through the same intermediate condition:
 \[
-\textup{(v)} \Longleftrightarrow \textup{(i)}.
+\textup{(i)} \Longleftrightarrow \textup{(v)}
+\quad\text{(universal twisting morphism and bar filtration),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(iii)}
+\quad\text{($A_\infty$ transfer and Keller classicality),}
 \]
-The backward implication is the repaired step in the proof:
-for the universal twisting morphism
+\[
+\textup{(i)} \Longleftrightarrow \textup{(iv)}
+\quad\text{(Ext diagonal vanishing),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(vii)}
+\quad\text{(factorization homology at genus~$0$),}
+\]
+\[
+\textup{(i)} \Longleftrightarrow \textup{(ix)}
+\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
+\textup{(i)} \Longleftrightarrow \textup{(x)}
+\quad\text{(FM boundary acyclicity),}
+\]
+and on the monadic side
+\[
+\textup{(i)} \Longleftrightarrow \textup{(vi)}
+\quad\text{(Barr--Beck--Lurie monadicity).}
+\]
+
+Three direct cross-links are the load-bearing redundancy.
+
+\smallskip\noindent
+\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.
+For the universal twisting morphism
 $\tau_{\mathrm{univ}}\colon \barB_X(\cA)\to \cA$,
 condition~\textup{(v)} is the quasi-isomorphism of the counit
 $\varepsilon_{\tau_{\mathrm{univ}}}$, and
 Theorem~\ref{thm:fundamental-twisting-morphisms}
 identifies that directly with
 $\tau_{\mathrm{univ}}$ being a chiral Koszul morphism.
-This route uses the universal bar twisting datum and the bar
-filtration, not the chain through \textup{(ii)} or \textup{(iii)}.
+This uses the universal bar twisting datum and the bar filtration,
+not the route through \textup{(ii)} or \textup{(iii)}.
 
-Condition~\textup{(i)} also implies condition~\textup{(viii)}
-directly.
+\smallskip\noindent
+\textup{(i)}$\Rightarrow$\textup{(viii)} is also direct.
 Theorem~\ref{thm:main-koszul-hoch},
 Theorem~\ref{thm:hochschild-polynomial-growth}, and
 Proposition~\ref{prop:e2-formality-hochschild}
-start from a Koszul datum and compute
+start from a chiral Koszul datum and compute
 $\ChirHoch^*(\cA)$ by the bar-cobar Hochschild resolution.
-This gives duality, polynomial growth, and $\Etwo$-formality
-without routing through conditions~\textup{(ii)}--\textup{(vii)}
-inside the meta-theorem.
+This yields duality, polynomial Hilbert growth, and
+$\Etwo$-formality without routing through
+\textup{(ii)}--\textup{(vii)} inside the meta-theorem.
 
-Condition~\textup{(iii)} implies condition~\textup{(x)}
-directly on FM strata.
+\smallskip\noindent
+\textup{(iii)}$\Rightarrow$\textup{(x)} is fiberwise and geometric.
 For a boundary stratum $S_T$, the restriction
 $i_{S_T}^!\,\barB_n(\cA)$ decomposes as the tensor product of the
 vertexwise collision complexes, and
 Remark~\ref{rem:iterated-residues-ainfty}
 identifies those iterated residues with the transferred
 $A_\infty$ operations.
-If $m_k=0$ for $k \geq 3$, only the strict binary residue survives
+If $m_k = 0$ for $k \geq 3$, only the strict binary residue survives
 at each vertex.
 Fiberwise Keller classicality, exactly as in
 Theorem~\ref{thm:ainfty-koszul-characterization},
@@ -2484,16 +2508,17 @@
 \]
 This reaches \textup{(x)} without passing through the shadow tower.
 
-The same bookkeeping exposes further direct links already implicit
-in the proof:
+\smallskip\noindent
+The same bookkeeping gives further direct arrows already implicit in
+the proof:
 \[
+\textup{(ii)} \Rightarrow \textup{(vii)},\qquad
+\textup{(vii)} \Rightarrow \textup{(ii)},\qquad
 \textup{(iv)} \Rightarrow \textup{(ii)},\qquad
-\textup{(vii)} \Longleftrightarrow \textup{(ii)},\qquad
 \textup{(ix)} \Rightarrow \textup{(ii)},\qquad
-\textup{(x)} \Rightarrow \textup{(ii)},\qquad
 \textup{(v)} \Longleftrightarrow \textup{(vi)}.
 \]
-Accordingly the unconditional core
+Hence the unconditional core
 \[
 \{\textup{(i)},\textup{(ii)},\textup{(iii)},\textup{(iv)},
 \textup{(v)},\textup{(vi)},\textup{(vii)},\textup{(ix)},
@@ -2520,12 +2545,24 @@
 
 Here \textup{(viii)} is a satellite consequence, not part of the
 equivalence core.
-In the undirected graph underlying the displayed core subweb on
-\textup{(i)--(vii)}, \textup{(ix)}, \textup{(x)},
-deleting any one displayed implication still leaves the core
-connected:
-there is no single proved arrow whose removal disconnects the
-equivalence package.
+Let $G_{\mathrm{core}}$ be the undirected graph obtained from the
+displayed core subweb by forgetting arrow directions and deleting the
+satellite node~\textup{(viii)}.
+Every displayed core edge lies on one of the cycles
+\[
+(\textup{(i)},\textup{(ii)},\textup{(v)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(iv)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(vii)}),
+\]
+\[
+(\textup{(i)},\textup{(iii)},\textup{(x)}),\qquad
+(\textup{(i)},\textup{(v)},\textup{(vi)}),\qquad
+(\textup{(i)},\textup{(ii)},\textup{(ix)},\textup{(x)}).
+\]
+Therefore $G_{\mathrm{core}}$ has no bridges.
+Equivalently, deleting any one displayed implication still leaves the
+unconditional core connected: the proof web has no single point of
+failure.
 \end{remark}
 
 \begin{remark}[Status of the Lagrangian and purity refinements]
@@ -2803,13 +2840,13 @@
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then the mixed sector of the Swiss-cheese bar complex is formal:
-every higher arity tree operation vanishes. The tower-bar
-correspondence is operadic: the arity-$r$ mixed tree and the
-degree-$r$ shadow are produced by the same genus-$0$ tree-transfer
-formula, with the same propagator on internal edges; the only
-difference is the output colour, and passage to the symmetric
-closed sector applies the averaging morphism
+Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+vanishes in the Swiss-cheese structure with open colour~$\cA$.
+The tree-shadow correspondence is operadic: the arity-$r$ mixed
+tree and the degree-$r$ shadow are produced by the same genus-$0$
+tree-transfer formula, with the same propagator on internal edges;
+the only difference is the output colour, and passage to the
+symmetric closed sector applies the averaging morphism
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}.
 Hence SC-formality forces $S_r(\cA) = 0$ for every $r \geq 3$:
@@ -2823,6 +2860,43 @@
 to class~$G$.
 \end{proof}
 
+\begin{remark}[Operadic alternative proof]
+\index{Swiss-cheese operad!operadic alternative proof}
+Proposition~\ref{prop:sc-formal-iff-class-g} admits a second proof
+path that stays entirely in the genus-$0$ operadic transfer formalism.
+
+For the forward direction, class~$G$ means that the shadow tower
+truncates at degree~$2$:
+$S_r(\cA) = 0$ for every $r \geq 3$
+\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
+On this Gaussian locus, the ordered bar data is generated by the binary
+two-point kernel, so every connected Swiss-cheese tree of arity
+$r \geq 3$ factors through binary pairings and has no primitive
+higher vertex. The mixed operations $m_k^{\mathrm{SC}}$ are built
+from those same genus-$0$ trees, hence
+$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
+
+For the converse, assume~$\cA$ is SC-formal. Then every mixed
+genus-$0$ tree of arity~$r \geq 3$ vanishes in the Swiss-cheese
+structure with open colour~$\cA$.
+By Theorem~\ref{thm:shadow-formality-identification},
+Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
+identity
+$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
+\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
+the degree-$r$ shadow $S_r(\cA)$ is the
+$\Sigma_n$-coinvariant closed projection of that same transfer tree.
+Hence $S_r(\cA) = 0$ for every $r \geq 3$; in particular
+$S_4(\cA) = 0$ and $\Delta = 8\kappa S_4 = 0$.
+The classification step, however, uses the full vanishing pattern,
+not the discriminant alone:
+class~$L$ also has $\Delta = 0$ but $S_3 \neq 0$.
+Therefore the relevant criterion is the truncation
+$S_r(\cA) = 0$ for all $r \geq 3$, and
+Theorem~\ref{thm:shadow-archetype-classification} identifies that
+property with class~$G$.
+\end{remark}
+
 \begin{remark}[D-module purity: reduction to a single gap]
 \label{rem:d-module-purity-content}
 \index{D-module purity!reduction to Saito weight}

tokens used
101,430
