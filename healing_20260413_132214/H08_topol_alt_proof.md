# H08_topol_alt_proof (350s)

Reworked the existing alternative-topologization remark in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3184). The new version now makes the top-down CFG route explicit: local bulk observables carry the `\Ethree^{\mathrm{top}}` structure, global bulk observables come from factorization homology, boundary restriction recovers `\cA`, the bulk-boundary comparison identifies the local bulk algebra with `Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)`, and Sugawara is reframed as the boundary-side perturbative computation of that same bulk structure. It also sharpens the obstruction statement: for non-gauge families the missing input is existence of the `3`d HT bulk theory and its bulk-boundary map, not an internal promotion inside `\mathsf{SC}^{\mathrm{ch,top}}`. The remark cites the existing `CFG25` entry, which is the `arXiv:2602.12412` paper.

I re-read the edited surface and ran a LaTeX verification pass. The build is currently blocked by a pre-existing `\@@BOOKMARK` runaway at `main.tex:590`, plus many unrelated unresolved refs/citations, so there is no clean full-build confirmation from this turn.

## Fortification Report
`thm:topologization`: PRIMARY PROOF: sound. SECONDARY PROOF: written in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3184). TECHNIQUE: Costello-Francis-Gwilliam factorization-algebra / factorization-homology route from a `3`d holomorphic-topological bulk theory. CONDITION STATUS: affine Kac--Moody at non-critical level remains unconditional; the general lane remains conditional on constructing the relevant `3`d HT bulk theory and the bulk-boundary identification. CONFIDENCE: high on the primary affine KM proof; medium-high on the secondary route as a rigorous fortified remark.


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
session id: 019d869f-97ae-7c92-a4fd-ac68ebbd88be
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


TOPOLOGIZATION — ALTERNATIVE APPROACH via factorization homology.

TARGET: chapters/theory/en_koszul_duality.tex (add Remark)

The primary approach uses Sugawara. Write an ALTERNATIVE:

TECHNIQUE: Costello-Francis-Gwilliam factorization homology approach.
1. The 3d HT theory on X x R has factorization algebra structure = E_3 by definition.
2. The boundary restriction to X x {0} gives the chiral algebra A.
3. The bulk observables = factorization homology of the E_3 algebra = Z^{der}_{ch}(A).
4. The E_3 structure on Z^{der}_{ch}(A) is AUTOMATIC from the 3d factorization structure,
   independent of Sugawara.
5. The Sugawara approach is the PERTURBATIVE COMPUTATION of this E_3 structure.

This gives E_3 from the TOP (3d theory) rather than the BOTTOM (Sugawara). The 3d
theory exists for gauge-theoretic families (Costello-Li holomorphic CS). For non-gauge
families: the existence of the 3d theory IS the obstruction.

Write as Remark[Alternative approach via 3d factorization]. Cite CFG arXiv:2602.12412.
mcp startup: no servers
codex
I’m treating this as a local fortification pass on the topologization lane in `chapters/theory/en_koszul_duality.tex`: first I’m reading the required constitutional files, the target section, and the relevant skill instructions so the new remark lands on the live theorem surface without drifting status or conventions.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 102ms:
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

 succeeded in 82ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
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

 succeeded in 55ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3672 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
 exited 1 in 56ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory

thinking
**Locating missing files**

I need to note that the red team file is missing its original path, but my skills suggest it’s in the archive. I should check the archive. The target file might also have relevant sections. I’m thinking I could use an explorer agent to help. Let’s spawn an explorer to locate the topologization section, find the right point for remarks, and check for any existing CFG citations or discussions on factorization-homology.
codex
I’ve loaded the rectification workflow and confirmed the live constitutional surface. Next I’m locating the topologization section, existing citation machinery, and the precise place where an alternative factorization-homology remark can strengthen the theorem without changing its proved status.
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "rg -n \"topologization|SC\\"'^'"\\{ch,top\\}|E_3|Sugawara|factorization\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"2602\\.12412|Costello|Francis|Gwilliam|factorization homology|holomorphic Chern|holomorphic CS|3d factorization\" -g '*.tex' -g '*.bib' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
23:$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
25:$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
27:The topologization proof is made constructive by an explicit
44:factorization on real $n$-manifolds? Then the propagator becomes a
54:factorization with full symmetric-group invariance: Heisenberg,
164:factorization on real $n$-manifolds. The earlier hierarchy
311:This factorization equips $\{\overline{\Conf}_k(\bR^n)\}_{k \geq 0}$
639: where $\int_M$ denotes $\En$-factorization homology and $A^\vee$
724: compute the factorization homology $\int_X \cA$ as a chain
731: is the descent spectral sequence of factorization homology with
737:Part (a): by the fundamental theorem of factorization
763:the descent spectral sequence for the factorization homology
913:$n$ & $(n{-}1)$-form & Totaro & $\En$-factorization homology
1197:factorization}
1201:\index{holomorphic--topological!factorization|textbf}
1275:  topologization theorem
1276:  (Theorem~\textup{\ref{thm:topologization}}).
1349:factorization-coalgebra structure on $\barB^{\Sigma}$ uses the
1529:and topological factorization in different dimensions. The
 succeeded in 51ms:
Total output lines: 735

./working_notes_frontier_2026_04.tex:82:\simeq B^{(0)}(\cA)$ is a theorem of Costello--Gwilliam. At
./working_notes_frontier_2026_04.tex:142:In the Costello--Li framework, the bulk theory on
./working_notes_frontier_2026_04.tex:351:category requires the Francis--Gaitsgory pro-nilpotent
./main.tex:790:restriction recovers the Costello--Francis--Gwilliam
./main.tex:1143:% Totaro relations, connection to Ayala--Francis, the n=2 case.
./main.tex:1870:\index{Ayala--Francis|see{Poincar\'e duality, non-abelian}}
./appendices/homotopy_transfer.tex:507:The bar construction is functorial for $\Ainf$-morphisms \cite{LV12}: an $\Ainf$-quasi-isomorphism $f: A \xrightarrow{\sim} B$ induces a quasi-isomorphism $\Bbar(f): \Bbar(A) \xrightarrow{\sim} \Bbar(B)$ of bar complexes. (The functoriality of $\barB$ for $A_\infty$-morphisms is the bar-cobar adjunction as a quantum $L_\infty$ functor.) Since the SDR maps $(\iota, p)$ extend to $\Ainf$-quasi-isomorphisms by Theorem~\ref{thm:htt}, the bar complexes $\Bbar(\cA)$ and $\Bbar(H, \{\tilde{m}_n\})$ are quasi-isomorphic. The geometric realization is compatible because $\Bbar^{\mathrm{geom}}$ is computed as the factorization homology of $\Bbar$, and factorization homology preserves quasi-isomorphisms between factorization algebras on $X$.
./appendices/nonlinear_modular_shadows.tex:64:$H^*(\barB^{(g)}(\cA), \Dg{g})$ (the factorization homology
./chapters/examples/deformation_quantization.tex:208:(\ClaimStatusProvedElsewhere, Francis--Gaitsgory~\cite{FG12}), the $L_\infty$~algebra
./chapters/examples/deformation_quantization.tex:261:Francis--Gaitsgory). The explicit integral formula and the
./chapters/examples/deformation_quantization.tex:585:This follows from the formality of the $E_2$-operad (Kontsevich, Tamarkin \cite{Tamarkin00}) via the factorization algebra formalism of Francis--Gaitsgory. See also Dolgushev--Tamarkin--Tsygan \cite{DTT09} for a systematic treatment of formality for Hochschild complexes.
./chapters/examples/deformation_quantization.tex:636:Francis--Gaitsgory \cite{FG12}) combined with the Maurer--Cartan formalism: the
./chapters/examples/deformation_quantization.tex:784:The factorization algebra framework of Costello--Gwilliam provides a rigorous formulation in which the Kontsevich star product arises as the local-to-global assembly map.
./chapters/examples/deformation_quantization.tex:790:\subsection{Connection to Ayala--Francis}
./chapters/examples/deformation_quantization.tex:792:Ayala--Francis \cite{AF15} develop factorization homology. The bar-cobar perspective:
./chapters/examples/deformation_quantization.tex:813:that the bar-cobar adjunction, restricted to the formal disk at genus~$0$, recovers classical Koszul duality, in agreement with the Francis--Gaitsgory formality
./appendices/_sl2_yangian_insert.tex:598:The closed-colour (symmetric, Francis--Gaitsgory) Koszul dual of
./tmp_standalone_audit/survey_v2_xr.tex:564:Its Koszul dual $\cA^!_{\mathrm{ch}}$ is the Francis--Gaitsgory
codex
The target section already contains a `Remark[Alternative approach via 3d factorization]`, so this is a fortification edit rather than a fresh insertion. I’m reading that live text now, along with the bibliography surface, to decide whether it needs tightening, status fencing, or a more exact CFG-based route.
exec
/bin/zsh -lc "sed -n '3136,3224p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
dimensional ladder: the $n = 2$ (chiral) and $n = 3$
(Chern--Simons) rows are connected not by an automatic
operadic promotion, but by the physical data of a stress
tensor.
\end{remark}

\begin{remark}[Scope: which algebras admit topologization]
\label{rem:topologization-scope}
\index{topologization theorem!scope}
Theorem~\ref{thm:topologization} is proved for affine
Kac--Moody $V_k(\fg)$ at non-critical level
$k \neq -h^\vee$, where the Sugawara element provides
an explicit inner conformal vector and the $3$d
holomorphic--topological theory is Chern--Simons.
For affine Kac--Moody, the strongest proved statement is now
split into three layers: the cohomological
$\Ethree^{\mathrm{top}}$ on BRST cohomology is proved, the
cohomology complex itself gives an unconditional chain-level
$\Ethree^{\mathrm{top}}$ model on a quasi-isomorphic
complex, and the lift to the original cochain complex is
exec
/bin/zsh -lc "rg -n \"CFG26|2602\\.12412|Costello--Francis--Gwilliam|CFG25\" -g '*.bib' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./main.tex:790:restriction recovers the Costello--Francis--Gwilliam
./chapters/connections/kontsevich_integral.tex:516:Costello--Francis--Gwilliam~\cite{CFG25} extract knot
./chapters/connections/holomorphic_topological.tex:948:collaborators~\cite{CG17,CWY18,CostelloGaiotto2020,CL16,Costello2111,CostelloP2201,Costello2302,CPS2208,CPS2306,FernandezCostelloP24,BittlestonCostelloZeng24,BittlestonCostello25,CFG25}
./chapters/theory/en_koszul_duality.tex:3192:Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
./chapters/theory/en_koszul_duality.tex:3882:  \textup{(}Costello--Francis--Gwilliam\textup{)}.
./chapters/theory/en_koszul_duality.tex:3892:\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG25}]
./chapters/theory/en_koszul_duality.tex:3910:\item \textup{(Theorem~1.4 of \cite{CFG25}.)} Canonical
./chapters/theory/en_koszul_duality.tex:4008:Costello--Francis--Gwilliam algebra $\cA^\lambda$ from
./chapters/theory/en_koszul_duality.tex:4131:(Costello--Francis--Gwilliam~\cite{CFG25}, Theorem~1.4
./standalone/ordered_chiral_homology.tex:197:classifies the Costello--Francis--Gwilliam perturbative
./standalone/ordered_chiral_homology.tex:491:  Costello--Francis--Gwilliam package are both governed by
./standalone/ordered_chiral_homology.tex:498:  Costello--Francis--Gwilliam~\cite{CFG26} identify
./standalone/ordered_chiral_homology.tex:1722:  theory (Costello--Francis--Gwilliam~\cite{CFG26}).
./standalone/ordered_chiral_homology.tex:5905:\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG26}]
./standalone/ordered_chiral_homology.tex:5929:\item \textup{(Theorem~1.4 of \cite{CFG26}.)} Canonical
./standalone/ordered_chiral_homology.tex:6024:Costello--Francis--Gwilliam~\cite{CFG26},
./standalone/ordered_chiral_homology.tex:10771:(Costello's $4$d Chern--Simons~\cite{CWY1,CWY2,CFG26,CG17}),
./standalone/ordered_chiral_homology.tex:10839:refinement of the Costello--Francis--Gwilliam perturbative
./standalone/ordered_chiral_homology.tex:11128:\bibitem{CFG26}
./standalone/ordered_chiral_homology.tex:11132:arXiv:2602.12412, 2026.
exec
/bin/zsh -lc "sed -n '3876,3938p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '352,366p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \textup{(Comparison with CFG.)}
  The same space classifies perturbative CS quantisations,
  filtered $\Ethree$-algebras deforming $C^*(\fg)$,
  braided monoidal deformations of
  $\mathrm{Rep}_{\mathrm{fin}}(\fg)$, and
  quasi-triangular quasi-Hopf deformations of $U(\fg)$
  \textup{(}Costello--Francis--Gwilliam\textup{)}.
\item \textup{(Topological enhancement.)}
  The Sugawara Virasoro element at non-critical level
  upgrades the holomorphic $\Etwo$ to topological $\Etwo$;
  Dunn additivity gives $\Ethree^{\mathrm{top}}$
  \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}.
  At $k = -h^\vee$, the enhancement fails.
\end{enumerate}
\end{theorem}

\begin{theorem}[Costello--Francis--Gwilliam~\cite{CFG25}]
\label{thm:cfg}
\ClaimStatusProvedElsewhere
Let $\fg$ be a simple finite-dimensional Lie algebra.
 succeeded in 52ms:

\bibitem{FernandezCostelloP24}
N. Fernandez, K. Costello, and N. M. Paquette, \emph{Koszul duality in quantum field theory}, arXiv:2412.17168, 2024.

\bibitem{BittlestonCostello25}
L. Bittleston and K. Costello, \emph{Twisted eleven-dimensional supergravity}, arXiv:2510.26764, 2025.

\bibitem{CFG25}
K. Costello, J. Francis, and O. Gwilliam, \emph{Chern--Simons factorization algebras and knot polynomials}, arXiv:2602.12412, 2026.

\bibitem{BRvR14-6d}
C. Beem, L. Rastelli, and B. C. van Rees, \emph{$\mathcal{W}$-symmetry in six dimensions}, J.\ High Energy Phys.\ (2015), no.~5, Paper No.~017, arXiv:1404.1079.

\bibitem{HS98}
M. Henningson and K. Skenderis, \emph{The holographic Weyl anomaly}, J.\ High Energy Phys.\ (1998), no.~7, Paper No.~023, arXiv:hep-th/9806087.

thinking
**Inspecting topology theorems**

I'm thinking about inspecting the theorem of topologization itself. There’s a lot to consider in how topological structures are formed and the implications they have in mathematics. I want to dig deeper into the principles that underlie these theorems. Getting a solid grasp on them will help clarify their significance, and I might even uncover some interesting relationships or applications! Let’s explore this further together!
exec
/bin/zsh -lc "sed -n '2960,3058p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the Sugawara element
$T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
\sum_a {:}J^a J_a{:}$
provides the inner conformal vector. For the
Virasoro algebra, $T(z)$ is the stress tensor itself.
\end{definition}

\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
\label{thm:topologization}
\ClaimStatusProvedHere
\index{topologization theorem!statement}
Let $\fg$ be a finite-dimensional simple Lie algebra
and let $\cA = V_k(\fg)$ be the universal affine
vertex algebra at non-critical level $k \neq -h^\vee$.
The Sugawara element
$T_{\mathrm{Sug}} = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a J_a{:}$
provides an inner conformal vector
\textup{(}Definition~\textup{\ref{def:inner-conformal-vector}}\textup{)}.
The chiral
center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, which carries
exec
/bin/zsh -lc "sed -n '3058,3118p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\bR$-direction (the open color of
$\mathsf{SC}^{\mathrm{ch,top}}$), Dunn additivity gives
$\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}}
= \Ethree^{\mathrm{top}}$ on
$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$.

\emph{Part~\textup{(ii)}.}
The cohomology complex
$M_k = H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
is already a chain complex, with zero differential, and
part~\textup{(i)} equips it with a chain-level
$\Ethree^{\mathrm{top}}$-structure. Over~$\CC$, choose a
splitting of cycles and boundaries in
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$; this gives a strong
deformation retract of chain complexes onto~$M_k$.
Hence $M_k$ is quasi-isomorphic as a chain complex to the
original derived center. The homotopy transfer theorem for
operadic algebras
\textup{(}Theorem~\textup{\ref{thm:htt-operadic}}\textup{)}
controls the dependence on the chosen retract, so the
codex
The live remark is already on the right lane, but it compresses two distinct objects: local bulk observables, which carry the `E_3` structure, and global observables, which come from factorization homology. I’m checking the surrounding `CFG` theorem surface now so the rewrite keeps that distinction exact while still delivering the top-down route the user asked for.
exec
/bin/zsh -lc "sed -n '3800,3860p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

% ================================================================
% Alternative E_3 via Dunn additivity (bypasses HDC)
% ================================================================

\begin{proposition}[$\Ethree^{\mathrm{top}}$ via Dunn additivity, bypassing the
Higher Deligne Conjecture]
\label{prop:e3-via-dunn}%
\index{E3 algebra@$\Ethree$ algebra!via Dunn additivity|textbf}%
\index{Dunn additivity!alternative $\Ethree$ construction|textbf}%
\index{topologization theorem!Dunn route to $\Ethree$}%
\ClaimStatusProvedHere
Let $\fg$ be a finite-dimensional simple Lie algebra and
$\cA = V_k(\fg)$ the universal affine vertex algebra at
non-critical level $k \neq -h^\vee$.  The BRST cohomology of
the derived chiral centre
$H_Q^\bullet\!\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\bigr)$
carries an $\Ethree^{\mathrm{top}}$-algebra structure by a route
that does not invoke the Higher Deligne Conjecture.

exec
/bin/zsh -lc 'rg -n "derived chiral center|bulk observables|boundary algebra|bulk-boundary|local observables|factorization algebra" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3996,4146p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  The space of $\Ethree$-deformations is
  non-canonically isomorphic to
  $(k+h^\vee) H^3(\fg)[[k+h^\vee]]$. For simple~$\fg$,
  $H^3(\fg)$ is one-dimensional.
\item \textup{(Comparison with CFG.)}
  The same space classifies perturbative CS quantisations,
  filtered $\Ethree$-algebras deforming $C^*(\fg)$,
  braided monoidal deformations of
  $\mathrm{Rep}_{\mathrm{fin}}(\fg)$, and
  quasi-triangular quasi-Hopf deformations of $U(\fg)$
  \textup{(}Costello--Francis--Gwilliam\textup{)}.
\item \textup{(Topological enhancement.)}
  The Sugawara Virasoro element at non-critical level
  upgrades the holomorphic $\Etwo$ to topological $\Etwo$;
  Dunn additivity gives $\Ethree^{\mathrm{top}}$
  \textup{(}Theorem~\textup{\ref{thm:topologization}}\textup{)}.
  At $k = -h^\vee$, the enhancement fails.
\end{enumerate}
\end{theorem}

 succeeded in 52ms:
1263:the \emph{derived chiral center}
1267:The derived center is the algebra of bulk observables of
1333:derived chiral center $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
1401:theory on $\bC_z \times \bR_t$ produces local observables that
1665:\textup{(}Proposition~\textup{\ref{prop:mixed-sector-bulk-boundary}}\textup{)}.
2147:$\cF_\cA$ denote the corresponding prefactorization algebra on
2157:\item \emph{Closed color $=$ bulk observables.} The closed-sector
2167:\item \emph{Center $=$ interior bulk observables.} The
2182:$X \times \{0\}$) supports local observables of~$\cA$ that multiply
2273:holomorphic-topological prefactorization algebras on
2599: interior bulk observables in the half-space
2608:the bulk-boundary correspondence in 2d TFT, and Keller's
2956:of bulk observables up to a $Q$-boundary: there exists
3052:cohomology of the factorization algebra on the
3054:locally constant factorization algebra on
3098:$\partial_z$ is not $Q$-exact, and the factorization algebra
3110:factorization algebras on $\bR^n$ and $\En$-algebras
3112:that converts local constancy of the factorization algebra
3188:algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
3191:factorization algebra in the sense of

thinking
**Inspecting bulk observables**

I think I need to take a closer look at around line 1263 to possibly understand the definitions related to the derived center as they pertain to bulk observables. There's likely something crucial in there that could clarify my understanding. So, I'll dive into that section and see what insights I can gather. Let's see what I can find in those definitions!
exec
/bin/zsh -lc "sed -n '1256,1288p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2148,2190p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$(\operatorname{Ass}^{\mathrm{ch}})^{\scriptstyle !}$.
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
 succeeded in 51ms:
$X \times \bR$ obtained from the
$\mathsf{SC}^{\mathrm{ch,top}}$-algebra structure
\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese})}.
Under the recognition theorem identifying
$\mathsf{SC}^{\mathrm{ch,top}}$-algebras with prefactorization
algebras on $D \times \bR$
\textup{(}Volume~II, items F4--F5\textup{)}, the following
identifications hold:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Closed color $=$ bulk observables.} The closed-sector
 algebra
 $\cO_{\mathrm{bulk}} := \cF_\cA(\mathrm{disks\ in\ } X)$
 is the chiral algebra~$\cA$ itself.
\item \emph{Open color $=$ boundary observables.} The open-sector
 algebra
 $\cO_{\mathrm{bdy}} := \cF_\cA(\mathrm{half\text{-}disks\ touching\ }
 X \times \{0\})$
 is the $E_1$-algebra $A = \cA|_{\{z_0\}}$, the fiber of~$\cA$
 at a point, equipped with its associative multiplication.
\item \emph{Center $=$ interior bulk observables.} The



thinking
**Interpreting algebraic structures**

I’m considering the algebra as \( Z^{der}_{ch}(A) \) in relation to the manuscript. It mentions that the derived center is the algebra of bulk observables, so I can clarify that in the manuscript's bulk-boundary dictionary, the derived center corresponds to the bulk observable algebra. This helps clear up the local/global confusion. I'll simplify bullet 3 by stating the CFG formalism packages the bulk into a locally constant factorization algebra. This can connect local observables and global ones nicely.
thinking
**Clarifying algebraic relationships**

I want to reference the user's phrase about bulk observables being related to the factorization homology of the E3 algebra equating to \( Z^{der} \). It's possible they see this specific route. I'll mention that, through non-abelian Poincaré duality, local observables as the E3 algebra \( O_{bulk} \) mean the factorization algebra relates to its homology with coefficients in \( O_{bulk} \). On the manifold \( X \times R \), we get global observables, but there's ambiguity in the definition of the derived center as either local or algebra of bulk observables.
thinking
**Enhancing clarity in definitions**

I think the phrase "Under the usual bulk-boundary dictionary, the local bulk observable algebra is identified with \( Z^{der}_{ch}(\cA)\); integrating it over \( X \times \R \) recovers global bulk observables" could be helpful. It maintains a clear distinction while possibly improving clarity. This way, the connection between local and global observables remains precise, making it easier for readers to follow. I'll need to ensure it's set in the right context to maximize understanding for the user.
exec
/bin/zsh -lc 'rg -n "Costello--Li|CL20|CL16|holomorphic Chern--Simons|holomorphic--topological Chern--Simons|Chern--Simons" bibliography/references.tex chapters/theory/en_koszul_duality.tex chapters/connections/holomorphic_topological.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '932,980p' chapters/connections/holomorphic_topological.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
bibliography/references.tex:109:S. Axelrod and I. M. Singer, \emph{Chern--Simons perturbation theory.~II}, J. Differential Geom. \textbf{39} (1994), no.~1, 173--213.
bibliography/references.tex:225:C. Braun and A. Lazarev, \emph{Unimodular homotopy algebras and Chern--Simons theory}, J. Pure Appl. Algebra \textbf{219} (2015), no.~11, 5158--5194.
bibliography/references.tex:264:A. S. Cattaneo and P. Mnev, \emph{Remarks on Chern--Simons invariants}, Comm. Math. Phys. \textbf{293} (2010), no.~3, 803--836, arXiv:0811.2045.
bibliography/references.tex:308:\bibitem{CL16}
bibliography/references.tex:311:\bibitem{CL20}
bibliography/references.tex:360:K. Costello, J. Francis, and O. Gwilliam, \emph{Chern--Simons factorization algebras and knot polynomials}, arXiv:2602.12412, 2026.
chapters/theory/en_koszul_duality.tex:14:recovering the chiral bar complex) to $n = 3$ (Chern--Simons,
chapters/theory/en_koszul_duality.tex:30:in the $3$d holomorphic Chern--Simons BV complex
chapters/theory/en_koszul_duality.tex:64:interfaces with Chern--Simons theory and Vassiliev invariants
chapters/theory/en_koszul_duality.tex:261:$n = 3$ & $3$-manifold & Chern--Simons bar \\
chapters/theory/en_koszul_duality.tex:403:\begin{example}[\texorpdfstring{$n = 3$}{n = 3}: the Chern--Simons propagator]
chapters/theory/en_koszul_duality.tex:405:\index{Chern--Simons!propagator}
chapters/theory/en_koszul_duality.tex:415:Chern--Simons theory~\cite{Kon94}, this propagator appears as the
chapters/theory/en_koszul_duality.tex:1145:\section{\texorpdfstring{The $n = 3$ case: Chern--Simons theory}{The n = 3 case: Chern--Simons theory}}
chapters/theory/en_koszul_duality.tex:1147:\index{Chern--Simons!$\mathsf{E}_3$ bar complex}
chapters/theory/en_koszul_duality.tex:1150:perturbative Chern--Simons theory and the Kontsevich integral
chapters/theory/en_koszul_duality.tex:1153:\begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
chapters/theory/en_koszul_duality.tex:1156:\index{Chern--Simons!perturbative expansion}
chapters/theory/en_koszul_duality.tex:1160:Chern--Simons invariants of $3$-manifolds:
chapters/theory/en_koszul_duality.tex:1162:\item The propagator is the Chern--Simons propagator of
 succeeded in 51ms:
binary trees with leaves in cyclic order. The resulting
expression is the Parke--Taylor formula by direct computation.
Computational verification:
\texttt{compute/lib/celestial\_ope\_shadow\_projections\_engine.py}
(73~tests).
\end{proof}

The wedge construction, obstruction tower, exact ladder theorems,
and Airy--Witt realization are in Volume~II\@.

\section{Systematic comparison with Costello's programme}
\label{sec:costello-comparison}
\index{Costello!programme comparison|textbf}
\index{holomorphic Chern--Simons!modular Koszul comparison}

The body of work initiated by Costello and
collaborators~\cite{CG17,CWY18,CostelloGaiotto2020,CL16,Costello2111,CostelloP2201,Costello2302,CPS2208,CPS2306,FernandezCostelloP24,BittlestonCostelloZeng24,BittlestonCostello25,CFG25}
constitutes the most sustained programme connecting perturbative
gauge theory to the algebraic structures studied in this monograph.
The precise relationship is recorded below, organized by the four
exec
/bin/zsh -lc "sed -n '3284,3302p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3588,3618p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For affine Kac--Moody, the question
``can the correction be removed by gauge transformation on the
original complex?'' is equivalent to the coherence equation
$[m,G]=\partial_z$ of
Remark~\ref{rem:topologization-chain-vs-cohomology}. For
general chiral algebras, the obstruction to extending
Theorem~\ref{thm:topologization} to
Conjecture~\ref{conj:topologization-general} is twofold:
first construct the $3$d HT BRST complex for the relevant
bulk theory (Chern--Simons for gauge algebras, $3$d gravity
for Virasoro, higher-spin gravity for $\cW_N$), and then
verify the corresponding $A_\infty$-coherent null-homotopy of
holomorphic translation.
For affine Kac--Moody, the bulk theory is holomorphic
Chern--Simons and the BRST complex is standard. For
$3$d gravity, this is the subject of Volume~II
\textup{(}Three-Dimensional Quantum Gravity\textup{)}.
\end{remark}

 succeeded in 51ms:
\index{E3 algebra@$\Ethree$ algebra!coderived}%
Let $\cA$ be a chirally Koszul algebra with inner conformal vector
at non-critical level.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Coderived local constancy.)}
  The chiral factorization algebra $\cF_\cA$ on a curve~$X$,
  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
  is locally constant. Precisely: the
  $m_0$-curvature obstruction to local constancy at
  step~\textup{(iv)} of
  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}
  lies in $\operatorname{Im}(d)$ in $D^{\mathrm{co}}$, by the
  same mechanism that absorbs $\delta_4$ in
  Theorem~\textup{\ref{thm:bv-bar-coderived}}.
\item \textup{(Coderived $\Ethree$.)}
  The locally-constant recognition principle
  \textup{(}Lurie~\cite{HA}\textup{)}, adapted to the
  coderived setting, equips the derived chiral center
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ with an
  $\Etwo^{\mathrm{top}}$-structure in $D^{\mathrm{co}}$.
exec
/bin/zsh -lc "sed -n '304,318p' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\bibitem{CG97}
N. Chriss and V. Ginzburg, \emph{Representation Theory and Complex Geometry}, Birkh\"auser, 1997.

\bibitem{CL16}
K. Costello and S. Li, \emph{Twisted supergravity and its quantization}, arXiv:1606.00365, 2016.

\bibitem{CL20}
K. Costello and S. Li, \emph{Anomaly cancellation in the topological string}, arXiv:1905.09269, 2019.

\bibitem{Costello-1705.02500v1}
K. Costello, \emph{Holography and Koszul duality: the example of the M2 brane}, arXiv:1705.02500, 2017.

\bibitem{costello-gaiotto}
K. Costello and D. Gaiotto, \emph{Twisted holography}, J.\ High Energy Phys.\ (2022), no.~3, Paper No.~087, arXiv:1812.09257.
exec
/bin/zsh -lc 'rg -n "holomorphic--topological theory|boundary algebra|Costello--Li|CL16|CL20" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2951:of a holomorphic--topological theory~$T$ on
3149:holomorphic--topological theory is Chern--Simons.
3163:stress tensor $T(z)$. The holomorphic--topological theory
3188:algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
3189:the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory

thinking
**Considering edits and bibliography**

I’m thinking about renaming the text to "Costello--Francis--Gwilliam\cite{CFG25}" and including arXiv in the bibliography. That sounds good! Should I verify any anti-patterns? It seems like no, I don’t need to do that. Before making any edits, I should provide an update and include a pre-edit verification block to ensure everything's in order. That way, I can feel confident moving forward with the changes!
codex
```text
topologization surface: chapters/theory/en_koszul_duality.tex, Remark[Alternative approach via 3d factorization] adjacent to thm:topologization
status boundary: theorem stays proved only for affine KM at non-critical level; remark must not upgrade conj:topologization-general
object distinction: local bulk observables carry E_3; global bulk observables are their factorization homology; the remark will state both explicitly
boundary identification: boundary restriction recovers the chiral algebra A; bulk-boundary comparison identifies the local bulk algebra with Z^{der}_{ch}(A)
Sugawara role: perturbative boundary computation of the same E_3 structure, not the source of existence in the top-down route
scope split: gauge-theoretic families have a genuine 3d HT bulk theory; for non-gauge families, existence of that bulk theory is the obstruction
citation surface: use existing key CFG25 = arXiv:2602.12412 in bibliography/references.tex
verdict: ACCEPT
```
codex
I’ve isolated the change to the existing 3d-factorization remark. The edit will make the local-vs-global bulk distinction explicit, tie the argument directly to the `CFG` factorization-algebra formalism, and recast Sugawara as the boundary-side perturbative computation rather than the source of `E_3`.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -3185,35 +3185,46 @@
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 69ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]

codex
The remark is patched. I’m re-reading the edited block now for theorem-surface accuracy, then I’ll run a narrow hygiene pass on the touched text so the fortification doesn’t introduce wording drift or TeX issues.
exec
/bin/zsh -lc "sed -n '3178,3228p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|landscape|journey|navigate|---|—" chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Algebras without conformal vector (Heisenberg at $k = 0$,
certain coset constructions, genuinely $\Eone$-chiral
algebras without inner Virasoro): topologization fails.
The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
\end{remark}

\begin{remark}[Alternative approach via 3d factorization]
\index{topologization theorem!alternative 3d factorization route}
There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
the bulk theory rather than from the conformal vector. Suppose a
chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
algebra on the slice $X \times \{0\}$ of a $3$d
holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The $3$d theory is the primary object. If the topological shadow
  of $\cF_{T_\cA}$ is locally constant on the underlying real
  $3$-manifold, its local bulk observables form an
  $\Ethree^{\mathrm{top}}$-algebra by the
 succeeded in 51ms:
2755:\item \emph{Standard landscape.}
2756: For every family in the standard landscape (Heisenberg, affine
4526:% ----------------------------------------------------------------
4937:% ----------------------------------------------------------------
5218:% ----------------------------------------------------------------
5647:% ----------------------------------------------------------------
5733:% ----------------------------------------------------------------
5941:% ----------------------------------------------------------------
6062:% ----------------------------------------------------------------
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]


thinking
**Exploring grep results**

I'm looking through the grep results and noticed that "landscape" appeared elsewhere, not in my edit. I think I should read the full remark to understand better since it seems sed might have truncated something. I need to check a few more lines to see if that helps me get a clearer picture of the context. Let's dig a bit deeper; there might be important information I’m missing!
exec
/bin/zsh -lc "sed -n '3228,3242p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
statement for the bulk theory, while the Sugawara mechanism is the
boundary perturbative realization when such a bulk theory is known.
\end{remark}

\begin{conjecture}[Chain-level topologization for general chiral algebras]
\label{conj:topologization-general}
\ClaimStatusConjectured
\index{topologization theorem!general conjecture}
Let $\cA$ be a chiral algebra with conformal vector
$T(z)$ at non-critical parameters, and suppose the
corresponding $3$d holomorphic--topological bulk theory
admits a BRST complex in which holomorphic translations are
$Q$-exact by an antighost contraction. Then the analogue of
Theorem~\ref{thm:topologization} holds:
\begin{enumerate}[label=\textup{(\roman*)}]
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]


thinking
**Considering compilation options**

I'm thinking about how to compile something, specifically focusing on contracts and theorem scope. Running the command `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` seems like a solid option for working within the time constraints. Alternatively, I could compile just one file or check for existing build instructions. I’m also considering if the repo has scripts available. I’ll need to ensure a commentary update is done before building—so many details to keep track of!
codex
The text is clean on reread. I’m running a narrow LaTeX verification pass next; this is just to catch syntax or citation fallout from the remark rewrite, not to re-litigate the larger theorem package.
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]

 exited 12 in 2.09s:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  chapters/frame/heisenberg_frame.aux
  main.aux
  main.ind
  main.out

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -halt-on-error -file-line-error -recorder  "main.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode

thinking
**Polling build status**

I see that the build is still running, and I want to make sure I’m keeping track of its progress. It seems like checking in or polling to get updates on the build status is the next step I should take. I’ll stay tuned for any notifications or changes. Let’s see how this goes!
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]


thinking
**Investigating build failure**

I'm looking into why the build failed, possibly due to pre-existing bookmarks or refs that are unrelated to my current changes. I might need to check if my changes introduced an issue. It seems okay at line 590 in main.tex, but it could be due to stale auxiliary files. I wonder if it would help to compile a standalone file, or perhaps run `kpsewhich`. I could also inspect my changes using `git diff`. Let's see what I find!
codex
The local build did not complete, but the failure is not on the edited remark. `pdflatex` stopped immediately at a pre-existing `\@@BOOKMARK` runaway in `main.tex:590`, with many unrelated unresolved refs/citations already present in the tree. I’m doing one final diff check on the touched file, then I’ll close with the exact fortification outcome and the verification limit.
exec
/bin/zsh -lc 'git diff -- chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 115ms:

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]


thinking
**Exploring git details**

I’m curious about why the git diff is empty. Perhaps there’s a filter affecting my repository? I should check the git status to gather more information. This step might help me troubleshoot what’s going on, as I want to understand if there's something unusual happening with the files. Let’s see what status reveals, and hopefully, it will clarify why there’s no diff to review!
exec
/bin/zsh -lc 'git status --short chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]

exec
/bin/zsh -lc 'git ls-files chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]



thinking
**Exploring Git File Changes**

I'm considering whether the file is identical to HEAD because the same change might already exist. I noticed our remarks changed from previous text, which could mean the index was updated externally. If `git diff` is empty, then the current file is the same as HEAD, but before, the patch file differed. I'm questioning if there's anything reverting the changes or if the original file is already the same. I might be missing something regarding the workspace or branching situation.
thinking
**Analyzing Patch Application**

I'm trying to figure out why applying the patch didn't show any changes. It could be that the file content was normalized through smudge or clean, but checking for Git LFS shows it isn't there. I wonder if line endings were converted, preventing any diffs. Maybe the patch was applied, but a watcher reverted it? The content might have already existed in HEAD, though my earlier output suggested old content. I'm considering if the repo is not tracking modifications due to a new file system and will check the hashes in HEAD versus the working tree.
exec
/bin/zsh -lc "git show HEAD:chapters/theory/en_koszul_duality.tex | sed -n '3178,3228p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Algebras without conformal vector (Heisenberg at $k = 0$,
certain coset constructions, genuinely $\Eone$-chiral
algebras without inner Virasoro): topologization fails.
The center remains $\Etwo^{\mathrm{hol}}$, not $\Ethree$.
\end{remark}

\begin{remark}[Alternative approach via 3d factorization]
\index{topologization theorem!alternative 3d factorization route}
There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
the bulk theory rather than from the conformal vector. Suppose a
chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
algebra on the slice $X \times \{0\}$ of a $3$d
holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The $3$d theory is the primary object. If the topological shadow
  of $\cF_{T_\cA}$ is locally constant on the underlying real
  $3$-manifold, its local bulk observables form an
  $\Ethree^{\mathrm{top}}$-algebra by the
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..e659efb73dd053593a1a1314468e24fdeb1c44b0
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]

exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3182,3236p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3182	\end{remark}
  3183	
  3184	\begin{remark}[Alternative approach via 3d factorization]
  3185	\index{topologization theorem!alternative 3d factorization route}
  3186	There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
  3187	the bulk theory rather than from the conformal vector. Suppose a
  3188	chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
  3189	algebra on the slice $X \times \{0\}$ of a $3$d
  3190	holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
  3191	$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
  3192	Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
  3193	\begin{enumerate}[label=\textup{(\roman*)}]
  3194	\item The $3$d theory is the primary object. If the topological shadow
  3195	  of $\cF_{T_\cA}$ is locally constant on the underlying real
  3196	  $3$-manifold, its local bulk observables form an
  3197	  $\Ethree^{\mathrm{top}}$-algebra by the
  3198	  Costello--Francis--Gwilliam/Lurie recognition theorem.
  3199	\item Restriction to the boundary slice $X \times \{0\}$ recovers the
  3200	  boundary chiral algebra~$\cA$.
  3201	\item The bulk--boundary comparison identifies the local bulk
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..1e19adf52e9e0207a8d29cc610355786e931eab2
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]
@@ -3377,6 +3388,99 @@
 is the expected endpoint.
 \end{remark}
 
+\begin{remark}[Research direction: chain-level topologization]
+\label{rem:research-chain-level-topologization}
+\index{topologization theorem!chain-level research direction}%
+\index{Sugawara construction!gauge rectification programme}%
+Theorem~\ref{thm:topologization} separates the problem into a proved
+homotopy-invariant lane and an unproved original-complex lane. The
+status sharpens as follows.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \emph{What the homotopy transfer theorem already gives.}
+  Part~\textup{(ii)} of Theorem~\ref{thm:topologization}, together
+  with Theorem~\ref{thm:htt-operadic}, gives a chain-level
+  $\Ethree^{\mathrm{top}}$-algebra on the zero-differential
+  cohomology complex
+  $H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$,
+  quasi-isomorphic as a chain complex to the original derived center.
+  This is sufficient for applications that depend only on the
+  $\infty$-quasi-isomorphism class of the bulk algebra: existence of
+  an $\Ethree^{\mathrm{top}}$ enhancement, factorization homology up
+  to equivalence, deformation functors of the bulk algebra, and
+  homotopy-invariant module-category constructions.
+
+\item \emph{What still needs the original complex.}
+  A transferred model does not by itself control statements written
+  on the chosen BRST complex. The original-complex lift is needed for
+  rigid chain-level comparisons: compatibility with the explicit
+  action of the pair
+  $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)$, comparison with the
+  concrete brace and BV operators before passing to cohomology,
+  locality and renormalization arguments on a fixed complex, and
+  filtered perturbative constructions in which the chosen
+  representatives of $Q$, $T$, and the higher operations matter.
+
+\item \emph{Relation to class~M and MC5.}
+  The class~M failure in MC5 does not literally equal the
+  topologization obstruction. MC5 studies the BV/bar comparison cone,
+  while Theorem~\ref{thm:topologization}\textup{(iii)} studies the
+  cocycle $\partial_z$ in the brace deformation complex. The ambient
+  complexes are different. The mechanism is adjacent: in both cases
+  the infinite shadow tower produces genuine higher chain-level terms
+  that disappear on cohomology, or after coderived passage, but do
+  not vanish on the ordinary complex. Thus MC5 is not the same
+  obstruction, but it is strong evidence that class~M should not
+  admit a naive original-complex $\Ethree$ lift without extra
+  completion or coderived input.
+
+\item \emph{Affine Kac--Moody: an explicit gauge-rectification
+  programme.}
+  For $V_k(\fg)$ at non-critical level
+  $k \neq -h^\vee$, Construction~\ref{constr:sugawara-antighost}
+  gives an explicit unary contraction $G_1$. Acting on observables,
+  the Sugawara field is the holomorphic-translation operator, so the
+  operator identity
+  $[Q,G_1] = T_{\mathrm{Sug}} + (\text{$Q$-exact})$
+  translates at arity~$1$ into
+  \[
+    [m_1, G_1]
+    \;=\;
+    \partial_z + [m_1,h_1]
+  \]
+  for a degree-$(-1)$ correction $h_1$. Replacing $G_1$ by
+  $G_1-h_1$ kills the unary defect. The remaining error then starts
+  in arity at least~$2$:
+  \[
+    D^{(1)}
+    \;:=\;
+    [m, G_1-h_1] - \partial_z.
+  \]
+  A concrete route to
+  Theorem~\ref{thm:topologization}\textup{(iii)} is to solve
+  recursively for degree-$0$ gauge parameters
+  $u_2,u_3,\ldots$ and set
+  \[
+    m^{(r+1)} := \exp(\operatorname{ad}_{u_r})\,m^{(r)},
+    \qquad
+    G^{(r+1)} := \exp(\operatorname{ad}_{u_r})\,G^{(r)},
+  \]
+  choosing $u_r$ so that the lowest-arity piece of
+  $D^{(r)} := [m^{(r)},G^{(r)}]-\partial_z$ becomes
+  $d_{m^{(r)}}$-exact and is removed at the next step. This is a
+  research programme, not a proof. Its appeal on the affine lane is
+  that every input is explicit: the Sugawara field is explicit,
+  affine Kac--Moody is class~L with shadow depth
+  $r_{\max}=3$ on the present surface, and the harmonic cubic
+  correction is killed by the Jacobi identity
+  \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
+  These facts suggest that only finitely many arities should need
+  correction in the affine case. The remaining gap is precise: one
+  must identify the higher-arity defect in the brace deformation
+  complex with the Jacobi-controlled harmonic terms strongly enough to
+  prove that the recursive gauge equations close.
+\end{enumerate}
+\end{remark}
+
 \begin{construction}[The Sugawara antighost contraction for affine
 Kac--Moody]
 \label{constr:sugawara-antighost}%




thinking
**Preparing Fortification Report**

I need to compile a final answer with a fortification report regarding the theorem and the topologization target. The report should have sections like a change summary and verification. I should mention the high/medium confidence status regarding the techniques and the existence problem. Plus, I need to clarify that the build failed due to a pre-existing problem in the main file. Finally, I'll note that I fortified the alternative remark in the specified file link. Keeping it concise is essential!
thinking
**Finalizing Observables and Report**

I’m separating local bulk E3 observables from global factorization homology. This involves making boundary restrictions and identifying bulk-boundary explicitly. I’ll cite Costello–Francis–Gwilliam and reframe Sugawara in the context of E3 structure computations. Additionally, I’ll sharpen the obstruction statement about family existence concerning bulk theory. 

For verification, I’ve re-read the touched surface and ran `latexmk`, but the build is blocked due to a pre-existing issue in the main file. Finally, I’ll prepare the fortification report with a clear bullet point layout for the theorem.
thinking
**Drafting Fortification Report**

I’m structuring the fortification report, focusing on `thm:topologization`. For the primary proof, I’ll state it is sound. Then I'll reference the secondary proof, which will be documented as an alternative approach using 3D factorization. I need to ensure the format is clear and straightforward so the user can easily understand the report. Keeping it concise and to the point is key here; I will include just what's necessary!
codex
Reworked the existing alternative-topologization remark in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3184). The new version now makes the top-down CFG route explicit: local bulk observables carry the `\Ethree^{\mathrm{top}}` structure, global bulk observables come from factorization homology, boundary restriction recovers `\cA`, the bulk-boundary comparison identifies the local bulk algebra with `Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)`, and Sugawara is reframed as the boundary-side perturbative computation of that same bulk structure. It also sharpens the obstruction statement: for non-gauge families the missing input is existence of the `3`d HT bulk theory and its bulk-boundary map, not an internal promotion inside `\mathsf{SC}^{\mathrm{ch,top}}`. The remark cites the existing `CFG25` entry, which is the `arXiv:2602.12412` paper.

I re-read the edited surface and ran a LaTeX verification pass. The build is currently blocked by a pre-existing `\@@BOOKMARK` runaway at `main.tex:590`, plus many unrelated unresolved refs/citations, so there is no clean full-build confirmation from this turn.

## Fortification Report
`thm:topologization`: PRIMARY PROOF: sound. SECONDARY PROOF: written in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3184). TECHNIQUE: Costello-Francis-Gwilliam factorization-algebra / factorization-homology route from a `3`d holomorphic-topological bulk theory. CONDITION STATUS: affine Kac--Moody at non-critical level remains unconditional; the general lane remains conditional on constructing the relevant `3`d HT bulk theory and the bulk-boundary identification. CONFIDENCE: high on the primary affine KM proof; medium-high on the secondary route as a rigorous fortified remark.
file update:
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 88d9099149576269be75f6280db290200f71cea2..f5e7f0e0d32e1a40a1c3d60a03775e92a513ddf3
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3183,39 +3183,50 @@
 
 \begin{remark}[Alternative approach via 3d factorization]
 \index{topologization theorem!alternative 3d factorization route}
-There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from the
-bulk theory rather than from the conformal vector. Suppose a chiral
-algebra $\cA$ on a curve~$X$ is realized as the boundary algebra on
-the slice $X \times \{0\}$ of a $3$d holomorphic--topological theory
-$T_\cA$ on $X \times \bR$, and let $\cF_{T_\cA}$ be its bulk
-factorization algebra in the sense of
-Costello--Francis--Gwilliam~\cite{CFG25}. If the topological shadow of
-$\cF_{T_\cA}$ is locally constant on the underlying real
-$3$-manifold, then its local observables are automatically an
-$\Ethree^{\mathrm{top}}$-algebra, and its factorization homology
-computes the global bulk observables:
-\[
-  \int_{X \times \bR} \cF_{T_\cA}.
-\]
-When the bulk--boundary comparison identifies this complex with the
-derived chiral center
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the
-$\Ethree^{\mathrm{top}}$ structure on
-$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is inherited from the
-$3$d factorization structure itself, without a separate Sugawara
-construction.
+There is a top-down route to $\Ethree^{\mathrm{top}}$ that starts from
+the bulk theory rather than from the conformal vector. Suppose a
+chiral algebra $\cA$ on a curve~$X$ is realized as the boundary
+algebra on the slice $X \times \{0\}$ of a $3$d
+holomorphic--topological theory $T_\cA$ on $X \times \bR$, and let
+$\cF_{T_\cA}$ be its bulk factorization algebra in the sense of
+Costello--Francis--Gwilliam~\cite{CFG25}. Then the argument is:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item The $3$d theory is the primary object. If the topological shadow
+  of $\cF_{T_\cA}$ is locally constant on the underlying real
+  $3$-manifold, its local bulk observables form an
+  $\Ethree^{\mathrm{top}}$-algebra by the
+  Costello--Francis--Gwilliam/Lurie recognition theorem.
+\item Restriction to the boundary slice $X \times \{0\}$ recovers the
+  boundary chiral algebra~$\cA$.
+\item The bulk--boundary comparison identifies the local bulk
+  observable algebra with the derived chiral center
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. Integrating this
+  $\Ethree^{\mathrm{top}}$ object over $X \times \bR$ gives the
+  global bulk observables:
+  \[
+    \int_{X \times \bR} \cF_{T_\cA}.
+  \]
+\item Hence the $\Ethree^{\mathrm{top}}$ structure on
+  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is automatic from the $3$d
+  factorization structure itself. No separate Sugawara argument is
+  needed to produce it.
+\item The Sugawara route of Theorem~\ref{thm:topologization} is then
+  the boundary-side perturbative computation of this same
+  $\Ethree^{\mathrm{top}}$ structure: for affine Kac--Moody,
+  holomorphic Chern--Simons provides the bulk theory, and the
+  Sugawara contraction shows on the boundary BRST complex that
+  holomorphic translations are $Q$-exact.
+\end{enumerate}
 
-For affine Kac--Moody, this is the top-down interpretation of
-Theorem~\ref{thm:topologization}: holomorphic Chern--Simons supplies
-the bulk theory, and the Sugawara contraction computes on the boundary
-BRST complex the same bulk $\Ethree^{\mathrm{top}}$ structure
-perturbatively. For Virasoro and $\cW_N$, the missing step is
-therefore not an operadic promotion inside
-$\mathsf{SC}^{\mathrm{ch,top}}$; it is the construction of the
-relevant $3$d holomorphic--topological bulk theory together with its
-bulk--boundary identification. In that form,
+This shifts the obstruction. For gauge-theoretic families, the issue
+is not whether $\mathsf{SC}^{\mathrm{ch,top}}$ can be promoted
+internally, but whether one has already constructed the relevant $3$d
+holomorphic--topological bulk theory and its bulk--boundary map. For
+Virasoro, $\cW_N$, and other non-gauge families, that existence
+problem is precisely the missing input. In that form,
 Conjecture~\ref{conj:topologization-general} becomes an existence
-statement for the bulk theory.
+statement for the bulk theory, while the Sugawara mechanism is the
+boundary perturbative realization when such a bulk theory is known.
 \end{remark}
 
 \begin{conjecture}[Chain-level topologization for general chiral algebras]
@@ -3377,6 +3388,101 @@
 is the expected endpoint.
 \end{remark}
 
+\begin{remark}[Research direction: chain-level topologization]
+\label{rem:research-chain-level-topologization}
+\index{topologization theorem!chain-level research direction}%
+\index{Sugawara construction!gauge rectification programme}%
+Theorem~\ref{thm:topologization} separates the problem into a proved
+homotopy-invariant lane and an unproved original-complex lane. The
+status sharpens as follows.
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \emph{What the homotopy transfer theorem already gives.}
+  Part~\textup{(ii)} of Theorem~\ref{thm:topologization}, together
+  with Theorem~\ref{thm:htt-operadic}, gives a chain-level
+  $\Ethree^{\mathrm{top}}$-algebra on the zero-differential
+  cohomology complex
+  $H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$,
+  quasi-isomorphic as a chain complex to the original derived center.
+  This is sufficient for applications that depend only on the
+  $\infty$-quasi-isomorphism class of the bulk algebra: existence of
+  an $\Ethree^{\mathrm{top}}$ enhancement, factorization homology up
+  to equivalence, deformation functors of the bulk algebra, and
+  homotopy-invariant module-category constructions.
+
+\item \emph{What still needs the original complex.}
+  A transferred model does not by itself control statements written
+  on the chosen BRST complex. The original-complex lift is needed for
+  rigid chain-level comparisons: compatibility with the explicit
+  action of the pair
+  $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)$, comparison with the
+  concrete brace and BV operators before passing to cohomology,
+  locality and renormalization arguments on a fixed complex, and
+  filtered perturbative constructions in which the chosen
+  representatives of $Q$, $T$, and the higher operations matter.
+
+\item \emph{Relation to class~M and MC5.}
+  The class~M failure in MC5 does not literally equal the
+  topologization obstruction. MC5 studies the BV/bar comparison cone,
+  while Theorem~\ref{thm:topologization}\textup{(iii)} studies the
+  cocycle $\partial_z$ in the brace deformation complex. The ambient
+  complexes are different. The mechanism is adjacent: in both cases
+  the infinite shadow tower produces genuine higher chain-level terms
+  that disappear on cohomology, or after coderived passage, but do
+  not vanish on the ordinary complex. Thus MC5 is not the same
+  obstruction, but it is strong evidence that class~M should not
+  admit a naive original-complex $\Ethree$ lift without extra
+  completion or coderived input.
+
+\item \emph{Affine Kac--Moody: an explicit gauge-rectification
+  programme.}
+  For $V_k(\fg)$ at non-critical level
+  $k \neq -h^\vee$, Construction~\ref{constr:sugawara-antighost}
+  gives an explicit unary contraction $G_1$. Acting on observables,
+  the Sugawara field is the holomorphic-translation operator, so the
+  operator identity
+  $[Q,G_1] = T_{\mathrm{Sug}} + (\text{$Q$-exact})$
+  suggests at arity~$1$ a relation of the form
+  \[
+    [m_1, G_1]
+    \;=\;
+    \partial_z + [m_1,h_1]
+  \]
+  after choosing a degree-$(-1)$ primitive $h_1$ for the
+  $Q$-exact term. Replacing $G_1$ by
+  $G_1-h_1$ kills the unary defect. The remaining error then starts
+  in arity at least~$2$:
+  \[
+    D^{(1)}
+    \;:=\;
+    [m, G_1-h_1] - \partial_z.
+  \]
+  A concrete route to
+  Theorem~\ref{thm:topologization}\textup{(iii)} is to solve
+  recursively for degree-$0$ gauge parameters
+  $u_2,u_3,\ldots$ and, in the arity-completed deformation Lie
+  algebra, try to gauge-conjugate schematically by
+  \[
+    m^{(r+1)} := \exp(\operatorname{ad}_{u_r})\,m^{(r)},
+    \qquad
+    G^{(r+1)} := \exp(\operatorname{ad}_{u_r})\,G^{(r)},
+  \]
+  choosing $u_r$ so that the lowest-arity piece of
+  $D^{(r)} := [m^{(r)},G^{(r)}]-\partial_z$ becomes
+  $d_{m^{(r)}}$-exact and is removed at the next step. This is a
+  research programme, not a proof. Its appeal on the affine lane is
+  that every input is explicit: the Sugawara field is explicit,
+  affine Kac--Moody is class~L with shadow depth
+  $r_{\max}=3$ on the present surface, and the harmonic cubic
+  correction is killed by the Jacobi identity
+  \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
+  These facts suggest that only finitely many arities should need
+  correction in the affine case. The remaining gap is precise: one
+  must identify the higher-arity defect in the brace deformation
+  complex with the Jacobi-controlled harmonic terms strongly enough to
+  prove that the recursive gauge equations close.
+\end{enumerate}
+\end{remark}
+
 \begin{construction}[The Sugawara antighost contraction for affine
 Kac--Moody]
 \label{constr:sugawara-antighost}%

tokens used
150,049
