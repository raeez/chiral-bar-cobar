# F04_definitions_complementarity (676s)

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:466-472` — PROBLEM: `C1` only assumes a “chiral Koszul pair,” but the theorem immediately uses `\mathbf C_g`, `\mathbf Q_g`, and genus-$g$ bar data; the underlying definition of `chiral Koszul pair` in `chapters/theory/chiral_koszul_pairs.tex:625-682` does not provide a genus tower or center local system. FIX: strengthen the hypothesis to “a chiral Koszul pair carrying a modular pre-Koszul datum in the sense of Definition~\ref{def:modular-koszul-chiral},” and propagate that stronger hypothesis to the C0/C1/C2 summary and to `thm:shifted-symplectic-complementarity`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:195-197` — PROBLEM: Definition~\ref{def:complementarity-complexes} claims the Verdier involution `\sigma` acts on `\mathbf C_g(\cA)` by citing `thm:verdier-bar-cobar`, but the cited theorem in `chapters/theory/cobar_construction.tex:1312-1349` is a genus-0 bar/cobar Verdier pairing, not an involution on `R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\cA))`. FIX: remove the claim from this definition and either construct `\sigma` in a new lemma before line 186, or move the definition of `\mathbf Q_g,Q_g` to after a correct construction of `\sigma` and cite that lemma instead.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:738-744` — PROBLEM: the proof of `thm:ss-quantum` applies Leray to the product `\overline C_n(X)\times\overline{\mathcal M}_g\to\overline{\mathcal M}_g`, which is not the relative genus-$g$ configuration-space family; this trivializes the very moduli variation the theorem is supposed to capture. FIX: replace that display by the actual family `\pi_g:\mathcal C_g(\cA)\to\overline{\mathcal M}_g` from Definition~\ref{def:relative-bar-fiber}, and rewrite the spectral sequence as `E_2^{p,q}=H^p(\overline{\mathcal M}_g,R^q\pi_{g*}\bar B^{(g)}(\cA))`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:414-419` — PROBLEM: the C0 proof identifies the surviving fiber cohomology with the center by citing `cor:bar-cohomology-koszul-dual`, but that corollary in `chapters/theory/chiral_koszul_pairs.tex:924-948` only identifies bar cohomology with the Koszul dual coalgebra, not with centers. FIX: move `lem:fiber-cohomology-center` (currently at lines 906-1041) before `thm:fiber-center-identification` and cite that lemma here; delete the bogus appeal to `cor:bar-cohomology-koszul-dual`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:72-98` — PROBLEM: the chapter opening says C2 is conditional only on perfectness and nondegeneracy, but the actual theorem at lines 1898-1956 also assumes the BV package (`thm:config-space-bv`, `thm:bv-functor`) and an extra comparison quasi-isomorphism `\chi_g`; later, Proposition~\ref{prop:ptvv-lagrangian} proves an unconditional ambient PTVV statement. FIX: split C2 into two named pieces: an unconditional ambient PTVV/linear statement and a conditional bar-side BV lift, then rewrite lines 72-98 and 90-99 so the hypotheses match the actual results.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1267` — PROBLEM: the theorem lane repeatedly takes cohomology of `Z(\mathcal A)` instead of the center local system `\mathcal Z(\mathcal A)` (`1267`, `1339-1340`, `1452-1453`, `1538-1546`, `1708`); that is an object-conflation error, not harmless notation. FIX: replace every `H^*(\overline{\mathcal M}_g, Z(\mathcal A))`/`H^*(\overline{\mathcal M}_g, Z(\cA))` on the complementarity surface with `H^*(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))`/`\mathcal Z(\cA)`, and reserve `Z(\mathcal A)` for the fiberwise center only.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:149,194,375` — PROBLEM: the center local system is never actually defined in this file before it is used; the real definition lives elsewhere (`chapters/theory/higher_genus_modular_koszul.tex:575-577`). The theorem surface just says “where `\mathcal Z(\cA)` is the center local system.” FIX: insert a local definition before Definition~\ref{def:complementarity-complexes}: define `\mathcal Z_\cA` as the constructible sheaf on `\overline{\mathcal M}_g` whose restriction to `\mathcal M_g` has fiber `Z(\cA|_\Sigma)` at `[\Sigma]`, set `\mathcal Z(\cA):=\mathcal Z_\cA`, and use that notation consistently.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:374-375` — PROBLEM: C0 concludes “as local systems/sheaves on `\overline{\mathcal M}_g`,” which is category-level evasion; later the file itself says the boundary extension is only constructible (`815-829`). FIX: replace the conclusion by “as constructible sheaves on `\overline{\mathcal M}_g`, and as local systems on the smooth locus `\mathcal M_g`,” and define the intended boundary extension functor (`j_*`, `j_!`, or `j_{!*}`).

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:29-31` — PROBLEM: the scalar complementarity slogan `\kappa(\cA)+\kappa(\cA^!)=K` uses `K` before it is defined; the same defect recurs at `448-450` with `\varrho\cdot K`. The actual family-by-family definition only appears much later (`2812-2868`) and in `chapters/examples/genus_expansions.tex:3087-3104`. FIX: either define `K` immediately at first use as the family-dependent complementarity constant and forward-reference Proposition~\ref{prop:complementarity-landscape}, or remove the symbolic shorthand from the opening prose.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:42-89` — PROBLEM: the C0/C1/C2 summary uses undeclared objects before the chapter has defined them: `\mathcal Z_\cA`, `Q_g(\cA)`, `Q_g(\cA^!)`, `\mathbf C_g(\cA)`, `\mathbf Q_g(\cA)`, `\sigma`, and the Verdier pairing all appear before the notation is stabilized. FIX: either move the repaired notation block before this summary, or rewrite the summary in prose without symbols and introduce the formal objects only afterward.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:875,205-210` — PROBLEM: `Q_g(\mathcal A)` is defined twice with different meanings: first as the genus-graded piece `\operatorname{gr}^g H^*(\bar B(\mathcal A))`, later as `H^*(\mathbf Q_g(\cA))`, the `+1` eigenspace cohomology. The file later wants them equal, but it first makes them ambiguous. FIX: rename the spectral-sequence object to `Q_g^{\mathrm{ss}}(\mathcal A)` or leave it as `\operatorname{gr}^g H^*(\bar B(\mathcal A))`, reserve `Q_g(\cA)` for the eigenspace object, and add an explicit identification lemma.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:458-528` — PROBLEM: “Lagrangian polarization” is used in the theorem title and statement before this file defines what “Lagrangian” means in the linear pairing setting; the first actual definition appears only later at `2059-2068`, and that one is specifically PTVV-flavored. FIX: insert a definition immediately before `thm:quantum-complementarity-main` stating that for a non-degenerate degree-`d` pairing on `V`, a decomposition `V=L\oplus L'` is Lagrangian iff the pairing vanishes on `L` and `L'` and the induced cross-pairing `L\otimes L'→k[d]` is perfect.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:1838-1841` — PROBLEM: `prop:lagrangian-eigenspaces` cites “Theorem~\ref{thm:quantum-complementarity-main}, Step~7” for the isomorphism `\mathcal Z(\cA^!)\cong\mathcal Z(\cA)`, but Step 7 is the Kodaira–Spencer map, not the center-isomorphism argument; the relevant local argument is the sublemma at `1481-1506`. FIX: extract `lem:center-isomorphism` out of the proof into a standalone lemma before Proposition~\ref{prop:lagrangian-eigenspaces}, then change the citation at line 1841 to that lemma.

## Summary
Checked: 14 | Findings: 12 | Verdict: FAIL


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
session id: 019d83d4-c37d-7651-a5a7-17b067ad8135
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


MISSION: FOUNDATION AUDIT of chapters/theory/higher_genus_complementarity.tex

Check: is complementarity (kappa+kappa'=K) defined? Is the center local system Z_A defined? Is the Lagrangian decomposition defined? Are all objects in C0/C1/C2 defined before the theorem statements?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers



thinking
**Planning file audit**

I’m tasked with auditing a specific file, higher_genus_complementarity.tex. I should first check some essential documents like CLAUDE.md and the theorem registry before making any edits. The user is asking for an audit, which suggests a thorough review of the mathematics involved, so I'll need to read those files carefully. Using an exploration tool may help to read the files, but I want to ensure I ground my claims in actual content. I'll also need to provide updates along the way.
thinking
**Preparing for skill audit**

I may need to open a skill file and use a tool to read multiple files simultaneously since my network is restricted. It might be wise to update my plan based on the context I gather, though maybe just providing commentary updates would suffice. It’s essential to do an exhaustive audit and find any subtle issues without making code edits, as the user requested an audit, not edits. I’ll focus on identifying line numbers accurately and checking definitions related to complementarity before theorems.
thinking
**Searching for definitions and references**

I need to look at the surrounding chapter structure to see if there are any definitions or missing imports. I'll search for unresolved references within the file using rg to identify if there are any issues. It might also be useful to check the concordance and theorem registry for the status of any relevant theorems, but I should only mention those if they relate directly to my findings. Importantly, I need to ensure that all claims are grounded in the actual content of the file without guessing or inferring.
codex
I’m running a hostile audit of `chapters/theory/higher_genus_complementarity.tex` against the live source, starting with the repo’s required constitutional reads and the exact theorem surface around `C0/C1/C2`.
exec
/bin/zsh -lc "printf '%s\\n' '--- THEOREM REGISTRY ---' && sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then printf '%s\\n' '--- RED TEAM ---' && sed -n '1,240p' raeeznotes/raeeznotes100/red_team_summary.md; else printf '%s\\n' '--- RED TEAM ARCHIVE ---' && sed -n '1,240p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && printf '\\n--- CLAUDE ---\\n' && sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf '%s\\n' '--- CONCORDANCE ---' && sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- THEOREM REGISTRY ---
# Theorem Registry

Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2809 |
| Total tagged claims | 3615 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
 succeeded in 51ms:
--- RED TEAM ARCHIVE ---
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
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar

--- CLAUDE ---
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.
 succeeded in 51ms:
--- CONCORDANCE ---
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

thinking
**Auditing unresolved references**

I think using an audit could help identify unresolved references, perhaps starting with grep. Given that the user is asking for an exact file audit, I might want to try using `build-surface`, though targeted building could also be needed to detect undefined references in the file. I’m considering whether it’s better to run the targeted main build, especially since the user is looking for unresolved references. A manual check might even be enough, but an exhaustive audit is probably best.
codex
I’ve finished the required constitutional reads. Next I’m loading the audit workflow and the live theorem surface in `higher_genus_complementarity.tex`, then I’ll trace every object used in `C0/C1/C2` back to an actual local definition.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1,360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"C0|C1|C2|quantum-complementarity-main|Z_A|Z\\\\(|center local system|Lagrangian|complementarity\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
     1	\section{The complementarity theorem}
     2	\label{sec:complementarity-theorem}
     3	
     4	Classical Koszul duality over a point is a discrete correspondence:
     5	$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
     6	Already at genus~$0$ on a curve, the Fulton--MacPherson
     7	compactifications $\overline{C}_n(X)$ and the Arnold forms
     8	$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
     9	that has no counterpart over a point: the collision residues that
    10	define the bar differential, the averaging map
    11	$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
    12	characteristic from the spectral $r$-matrix, and the higher
    13	operations $m_n$ for $n \geq 3$ that determine whether the shadow
    14	tower terminates. At genus~$g \geq 1$, the fiberwise curvature
    15	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
    16	algebras to interact through the moduli
    17	$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
    18	decomposes into two complementary halves via Verdier duality:
    19	\begin{equation}\label{eq:complementarity-chapter-opening}
    20	 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
 succeeded in 51ms:
1:\section{The complementarity theorem}
2:\label{sec:complementarity-theorem}
19:\begin{equation}\label{eq:complementarity-chapter-opening}
27:complex, which splits the moduli contribution into two Lagrangian
39:(Theorem~\ref{thm:quantum-complementarity-main}).
50: This produces the ambient complex on which~\textup{(C1)}
51: and~\textup{(C2)} operate.
58: \begin{equation}\label{eq:complementarity-summary}
70: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
72:\item \emph{Shifted-symplectic Lagrangian upgrade
83: $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
90:The conditionality in~(C2) is substantive:
96:The fiber--center identification~(C0) and the
97:S-level decomposition~(C1) hold unconditionally on the
98:Koszul locus; the H-level Lagrangian upgrade~(C2) is the
114:$\overline{\mathcal{M}}_g$ required by~(C2) is a stronger
118:framework for shifted Lagrangian morphisms that provides
119:the natural geometric setting for the~(C2) upgrade.
129:and obstructions (anomalies). The complementarity theorem gives
136:The center $Z(\cA)$ acts on $H^*(\overline{\mathcal{M}}_g)$
codex
I have the theorem surface. The next pass is structural: theorem statements, proof steps, and every imported definition for `\mathcal Z(\cA)`, `Q_g`, `\mathbf Q_g`, the Verdier involution, and the claimed Lagrangian split. I’m also checking whether the file quietly uses objects before it ever defines them.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '820,1085p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '353,620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1238,1775p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"center local system|\\\\mathcal\\{Z\\}_\\{\\\\cA\\}|\\\\mathcal\\{Z\\}\\(\\\\cA\\)|Z\\(\\\\cA\\)|kappa\\(\\\\cA\\) \\+ \\\\kappa\\(\\\\cA\\"'^!'"\\)|Lagrangian decomposition|Lagrangian polarization|Verdier involution|sigma\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   353	\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
   354	\label{thm:fiber-center-identification}
   355	\index{fiber--center identification|textbf}
   356	\textup{[}Regime: curved-central
   357	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   358	
   359	\smallskip\noindent
   360	Assume $\cA$ carries a modular pre-Koszul datum
   361	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
   362	with finite-dimensional fiber cohomology, so that the relative bar
   363	family $R\pi_{g*}\bar{B}^{(g)}(\cA)$ is perfect over
   364	$\overline{\mathcal{M}}_g$
   365	\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
   366	Then:
   367	\begin{equation}\label{eq:fiber-center}
   368	R^q\pi_{g*}\bar{B}^{(g)}(\cA) = 0
   369	\quad\text{for } q \neq 0,
   370	\qquad
   371	R^0\pi_{g*}\bar{B}^{(g)}(\cA)
   372	\;\cong\; \mathcal{Z}_{\cA}
 succeeded in 52ms:
   820	by Lemma~\ref{lem:fiber-cohomology-center} (constancy of
   821	the center $Z(\cA)$ under variation of complex structure).
   822	On each boundary stratum $D_\Gamma$
   823	(indexed by stable graphs~$\Gamma$), the monodromy
   824	is quasi-unipotent: the Picard--Lefschetz formula gives
   825	monodromy operators $T_e = \mathrm{id} + N_e$ where $N_e$
   826	is nilpotent (one Jordan block per node
   827	$e \in E(\Gamma)$). A local system with quasi-unipotent
   828	monodromy along a normal crossing divisor is constructible
   829	(\cite[\S8.1]{KS90}).
   830	
   831	\emph{(3) Exhaustiveness and bounded-below.}
   832	The genus filtration $F^{\le g}$ is exhaustive
   833	($\bigcup_g F^{\le g} = \bar{B}(\cA)$) and bounded below
   834	($F^{\le -1} = 0$). By conilpotency of $\bar{B}(\cA)$
   835	(Theorem~\ref{thm:conilpotency-bar}), each element has
   836	finite bar degree, hence lives in some $F^{\le g}$.
   837	
   838	\emph{Convergence.} By (1)--(3), the spectral sequence
   839	satisfies the hypotheses of the filtered convergence theorem
 succeeded in 51ms:
  1238	\begin{equation}
  1239	Q_g(\mathcal{A}) = \bigoplus_{p+q=n} (E_\infty^{p,q,g})_{\mathcal{A}} \cong 
  1240	\bigoplus_{p+q=n} ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee = Q_g(\mathcal{A}^!)^\vee
  1241	\end{equation}
  1242	\end{proof}
  1243	
  1244	This completes Step~II: Verdier duality on configuration spaces
  1245	induces a duality of spectral sequences and a perfect pairing
  1246	between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
  1247	the genus-$0$ cohomological-shadow exception is recorded in
  1248	Theorem~\ref{thm:quantum-complementarity-main}.
  1249	\end{proof}
  1250	
  1251	\subsection{Step III: decomposition and complementarity}
  1252	
  1253	\begin{proof}[Step III: Steps 7-10]
  1254	
  1255	\emph{Step 7: Center action on moduli space cohomology.}
  1256	
  1257	\begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
 exited 2 in 51ms:
rg: regex parse error:
    (?:center local system|\mathcal\{Z\}_\{\cA\}|\mathcal\{Z\}\(\cA\)|Z\(\cA\)|kappa\(\cA\) \+ \kappa\(\cA\^!\)|Lagrangian decomposition|Lagrangian polarization|Verdier involution|sigma)
                           ^^
error: unrecognized escape sequence

thinking
**Investigating definitions and propositions**

I think I need to consider using fixed strings with -F for better reference. I should read the theorem and possibly add remarks since we have a lot of content. An audit might be necessary, especially checking definitions for the center local system in the file. I’ll need to review specific lines, focusing on the propositions and definitions, particularly around line 1803. I'm curious whether the theorem cites the Lagrangian property correctly and if the center local system is clearly defined.
codex
I’ve isolated the main risk already: the file repeatedly writes “the center local system” as if it had been defined, but the local theorem surface I’ve read so far only labels it, not defines it. I’m now checking whether that definition exists anywhere earlier in the file or only gets improvised later in the proof.
exec
/bin/zsh -lc 'rg -n -F "center local system" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\mathcal{Z}_{\\cA}\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\kappa(\\cA)+\\kappa(\\cA"'^!)" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\mathcal{Z}(\\cA)\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1788,1888p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
194:where $\mathcal{Z}(\cA)$ is the center local system.
375:where $\mathcal{Z}_{\cA}$ is the center local system.
1810:\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
1832:The center local system $\mathcal{Z}(\cA)$ on
 succeeded in 52ms:
48: with $R^0\pi_{g*}\bar{B}^{(g)}(\cA) \cong \mathcal{Z}_{\cA}$
372:\;\cong\; \mathcal{Z}_{\cA}
375:where $\mathcal{Z}_{\cA}$ is the center local system.
417:hence with the center $\mathcal{Z}_{\cA}\!\mid_\Sigma$
430:$\mathcal{Z}_{\cA}$ by the fiber-level identification
 succeeded in 50ms:
448:$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
449:while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
 succeeded in 50ms:
20: H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
59: H^*(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA))
68: $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
79: \mathcal{Z}(\cA))$ is non-degenerate, the complex
174:$H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$ decomposes
192:\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
194:where $\mathcal{Z}(\cA)$ is the center local system.
208:= \ker(\sigma - \mathrm{id} \mid H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))),\\
210:= \ker(\sigma + \mathrm{id} \mid H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))).
506:\mathcal{Z}(\cA))$, Lemma~\textup{\ref{lem:involution-splitting}(b)}
524:Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
572:on $C_g=R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$.
594:\mathcal{Z}(\cA))$ carries a $-(3g{-}3)$-shifted symplectic structure
1772:$\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$:
1776:$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$
1808:$V = H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
1810:\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
1832:The center local system $\mathcal{Z}(\cA)$ on
1838:The Koszul pairing identifies $\mathbb{D}\mathcal{Z}(\cA) \cong
1839:\mathcal{Z}(\cA^!) \cong \mathcal{Z}(\cA)$
 succeeded in 51ms:
  1788	decomposition depends only on the Koszul pair $(\cA, \cA^!)$,
  1789	not on auxiliary choices.
  1790	\end{remark}
  1791	
  1792	\begin{remark}[Geometric substrate (Volume~II)]
  1793	\label{rem:theorem-c-lagrangian}
  1794	\index{Lagrangian self-intersection!Theorem C}
  1795	Volume~II interprets the complementary decomposition as two
  1796	Lagrangians $\mathcal{L}$ and $\mathcal{L}^!$ inside a
  1797	$(-2)$-shifted symplectic stack $\mathcal{M}$, whose derived
  1798	intersection $\mathcal{L} \times_{\mathcal{M}} \mathcal{L}^!$
  1799	carries the $(-1)$-shifted symplectic structure that governs the
  1800	Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
  1801	\end{remark}
  1802	
  1803	\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
  1804	\label{prop:lagrangian-eigenspaces}
  1805	\index{Lagrangian!eigenspaces|textbf}
  1806	\index{Verdier duality!pairing on moduli}
  1807	Let $(\cA, \cA^!)$ be a chiral Koszul pair and let



thinking
**Inspecting theorem circularity**

I need to examine if the prop:lagrangian-eigenspaces uses theorem circularly. Line 1841 cites Theorem quantum complementarity Step 7 to identify Z(A^!) ≅ Z(A), yet the theorem statement claims a Lagrangian property. That could be circular. I should check if the proof in Step 7 relies on its own claim. It's crucial to see if all definitions, like complementarity, the center local system Z_A, and Lagrangian decomposition, are established before the theorem statements. I need to be thorough here!
thinking
**Identifying definition gaps**

I’m realizing our findings are likely missing key definitions and gaps in theorems or proofs. I don't necessarily need to audit the whole file, but I should surface the requested areas. Every hidden import, unresolved reference, or unjustified step counts as a finding, so I could end up identifying many issues. I need to read dependencies for objects and search referenced labels to check their definitions, especially if they appear before their local definition—this could indicate hidden imports. It's crucial to focus on objects in C0/C1/C2.
thinking
**Searching for definitions**

I need to search the repository to see if there’s an actual definition of the center local system. If I find it, I can fix things by adding an explicit citation. Similarly, the complementarity formula kappa + kappa' = K might be defined in another theorem like `thm:complementarity-root-datum`. In this file, there's mention in remarks 448-450, so I should check if the constant K is defined before or after that. It’s time to use the repository search tool across the whole repo!
codex
I’m tracing the hidden imports now. For each undeclared object I’m checking whether the repo defines it elsewhere, because there’s a big difference between “undefined” and “defined elsewhere but never imported into the theorem surface.” Both are audit findings, but the fixes differ.
exec
/bin/zsh -lc 'rg -n -F "center local system" chapters metadata appendices CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"kappa\\(\\\\cA\\)\\+\\\\kappa\\(\\\\cA\\"'^!'"\\)|complementarity sum|\\\\varrho\\\\.K|root-datum|Kac--Moody and free-field pairs|Theorem~\\\\ref\\{thm:complementarity-root-datum\\}\" chapters/theory/higher_genus_complementarity.tex chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"def:.*center|label\\{def:.*center|Z\\(\\\\cA\\).*defined|\\\\mathcal\\{Z\\}\\(\\\\cA\\).*definition|center isomorphism|def:complementarity-complexes|def:ambient-complementarity-datum\" chapters/theory/higher_genus_complementarity.tex chapters/theory chapters/examples appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Lagrangian polarization" chapters/theory/higher_genus_complementarity.tex chapters/theory chapters/connections appendices' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/genus_expansions.tex:1700:(trivial center local system), the complementarity
chapters/theory/higher_genus_complementarity.tex:194:where $\mathcal{Z}(\cA)$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:375:where $\mathcal{Z}_{\cA}$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:1810:\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
chapters/theory/higher_genus_complementarity.tex:1832:The center local system $\mathcal{Z}(\cA)$ on
chapters/theory/higher_genus_foundations.tex:4629:with the chiral product. Their sheaf is the center local system
chapters/theory/higher_genus_modular_koszul.tex:454:A \emph{center local system}
chapters/theory/higher_genus_modular_koszul.tex:575:A center local system $\mathcal{Z}_{\cA}$ on
chapters/theory/higher_genus_modular_koszul.tex:28968:center local system $\mathcal{Z}_\cA$ on
chapters/theory/introduction.tex.bak:798:  The \emph{center local system} $\mathcal{Z}_\cA$ is the
chapters/theory/algebraic_foundations.tex:265:complementarity decomposes the center local system into
chapters/theory/introduction.tex:583: The \emph{center local system} $\mathcal{Z}_\cA$ is the
chapters/connections/thqg_introduction_supplement.tex:53:center local system on the universal curve
chapters/connections/thqg_introduction_supplement.tex:61:center local system is
chapters/connections/thqg_introduction_supplement.tex:74:of the center local system:
chapters/connections/thqg_preface_supplement.tex:949:be the $(-1)$-shifted symplectic form on the center local system
chapters/connections/editorial_constitution.tex:2478: and the center local system~$\mathcal{Z}_{\cA}$, with Verdier
chapters/connections/thqg_introduction_supplement_body.tex:99:is the center local system. The ambient complex receives a map
chapters/frame/preface_sections2_4_draft.tex:269:The genus-$g$ cohomology of the center local system decomposes into
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:1722:is the center local system on~$\overline{\mathcal{M}}_g$.
 exited 2 in 51ms:
rg: regex parse error:
    (?:kappa\(\cA\)\+\kappa\(\cA\^!\)|complementarity sum|\varrho\.K|root-datum|Kac--Moody and free-field pairs|Theorem~\ref\{thm:complementarity-root-datum\})
              ^^
error: unrecognized escape sequence
 exited 2 in 53ms:
rg: regex parse error:
    (?:def:.*center|label\{def:.*center|Z\(\cA\).*defined|\mathcal\{Z\}\(\cA\).*definition|center isomorphism|def:complementarity-complexes|def:ambient-complementarity-datum)
                                           ^^
error: unrecognized escape sequence
 succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:458:\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:1890:Lagrangian polarization at the level of cohomology, and
chapters/theory/higher_genus_complementarity.tex:1947:\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
chapters/theory/higher_genus_complementarity.tex:5176:Lagrangian polarizations: one branch records the deformations visible
chapters/connections/thqg_symplectic_polarization.tex:899:\begin{theorem}[Conditional BV Lagrangian polarization;
chapters/connections/thqg_symplectic_polarization.tex:902:\index{BV algebra!Lagrangian polarization}
chapters/connections/thqg_symplectic_polarization.tex:930:\begin{theorem}[Verdier Lagrangian polarization (C2);
chapters/connections/thqg_symplectic_polarization.tex:1595:factorizes along the Lagrangian polarization.
chapters/connections/thqg_symplectic_polarization.tex:1658:Since the Lagrangian polarization gives a product
chapters/connections/thqg_symplectic_polarization.tex:2087: symplectic Lagrangian polarization
chapters/theory/higher_genus_modular_koszul.tex:4019: the Lagrangian polarization
chapters/theory/higher_genus_modular_koszul.tex:4130:off-diagonal in the Lagrangian polarization, so every internal
chapters/connections/thqg_introduction_supplement_body.tex:925:Lagrangian polarization records the gravitational content of Koszul
chapters/theory/poincare_duality_quantum.tex:20:class $\Theta_\cA$ mediates the Lagrangian polarization of these
chapters/theory/poincare_duality_quantum.tex:52:The universal MC class $\Theta_\cA$ (Theorem~\ref{thm:explicit-theta}) mediates genus-graded Koszul duality: the Verdier involution exchanges the eigenspace contributions of $\Theta_\cA$ and $\Theta_{\cA^!}$, producing the Lagrangian polarization of the quantum corrections across the genus tower. At the scalar level, the complementarity sum is family-dependent (Theorem~C): $\kappa(\cA) + \kappa(\cA^!) = 0$ for Kac--Moody and free-field pairs; for Virasoro (self-dual at $c = 13$), $\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$; and for $\mathcal{W}$-algebras, $\kappa(\cA) + \kappa(\cA^!) = \rho \cdot K$ where $\rho$ is the anomaly ratio and $K$ is the Killing form normalization.
chapters/connections/frontier_modular_holography_platonic.tex:1110:Lagrangian polarizations of that phase space. The Heisenberg and Weyl packages
chapters/theory/higher_genus_foundations.tex:7214:Lagrangian polarization
chapters/connections/holographic_codes_koszul.tex:139: \textup{(}it is the Lagrangian polarization\textup{)},
chapters/connections/holographic_codes_koszul.tex:280:Lagrangian polarization, with the Shapovalov form
chapters/theory/chiral_hochschild_koszul.tex:5344: recovers the proved Lagrangian polarization

thinking
**Looking into reruns and definitions**

I need to rerun with the -F option or make sure everything is escaped properly. I'm particularly focusing on the higher genus modular Koszul definitions in the center local system, especially around line 454. It might also be helpful to check the introduction at line 583. Additionally, I should search for the complementarity sum and make sure to use fixed strings. There’s a lot to consider here!
codex
I found an actual definition of “center local system” in `higher_genus_modular_koszul.tex`, not in the audited file. That means the current theorem surface is relying on a hidden import instead of a local definition or an explicit citation. I’m reading that source now to determine the exact minimal fix.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '560,620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "complementarity sum" chapters/theory/higher_genus_complementarity.tex chapters/theory/poincare_duality_quantum.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples chapters/connections' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:complementarity-root-datum" chapters/theory/higher_genus_complementarity.tex chapters/theory chapters/examples chapters/connections' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "K is the" chapters/theory/higher_genus_complementarity.tex chapters/theory/poincare_duality_quantum.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples chapters/connections' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '430,610p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/poincare_duality_quantum.tex:23:complementarity sum is family-dependent (Theorem~C).
chapters/theory/poincare_duality_quantum.tex:52:The universal MC class $\Theta_\cA$ (Theorem~\ref{thm:explicit-theta}) mediates genus-graded Koszul duality: the Verdier involution exchanges the eigenspace contributions of $\Theta_\cA$ and $\Theta_{\cA^!}$, producing the Lagrangian polarization of the quantum corrections across the genus tower. At the scalar level, the complementarity sum is family-dependent (Theorem~C): $\kappa(\cA) + \kappa(\cA^!) = 0$ for Kac--Moody and free-field pairs; for Virasoro (self-dual at $c = 13$), $\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$; and for $\mathcal{W}$-algebras, $\kappa(\cA) + \kappa(\cA^!) = \rho \cdot K$ where $\rho$ is the anomaly ratio and $K$ is the Killing form normalization.
chapters/theory/higher_genus_complementarity.tex:2318:complementarity sum (Theorem~\ref{thm:fermion-all-genera}), but
chapters/theory/higher_genus_complementarity.tex:2724:The complementarity sum $\dim Q_2 + \dim Q_2^! = 8$ is
chapters/theory/higher_genus_complementarity.tex:2812:The complementarity sum $\kappa(\cA) + \kappa(\cA^!)$ is a
chapters/theory/higher_genus_complementarity.tex:2821:landscape. The complementarity sum
chapters/theory/higher_genus_complementarity.tex:2908:$\kappa + \kappa^!$ records the complementarity sum
chapters/theory/higher_genus_complementarity.tex:2987:\begin{remark}[Self-dual points and the complementarity sum]
chapters/theory/higher_genus_complementarity.tex:3011:complementarity sum $\kappa + \kappa^!$ is independent of
chapters/theory/higher_genus_complementarity.tex:5880:complementarity sum
chapters/theory/higher_genus_complementarity.tex:5943:the complementarity sum
chapters/theory/higher_genus_modular_koszul.tex:4545:\textup{(}complementarity sum, fixed point at $c = 13$\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:9777:discriminants, complementarity sums) are invariants of the modular characteristic
chapters/theory/higher_genus_modular_koszul.tex:16855:complementarity sum vanishes ($\kappa(\cA) + \kappa(\cA^!) = 0$).
chapters/theory/higher_genus_modular_koszul.tex:18679: The complementarity sum is $80/87$,
chapters/theory/higher_genus_modular_koszul.tex:27019:$\{\mathrm{Vir}_c\}_c$:, and with complementarity sum
chapters/theory/higher_genus_modular_koszul.tex:27237:This non-vanishing of the complementarity sum is the signature
chapters/theory/higher_genus_modular_koszul.tex:29746:the complementarity sum. Verdier duality interchanges
chapters/examples/w_algebras_deep.tex:2341:\item The \emph{Koszul complementarity sum}
chapters/examples/w_algebras_deep.tex:2428:and the complementarity sum
 succeeded in 53ms:
   560	 The non-circular anchor for the $(\mathrm{ii}) \Rightarrow (\mathrm{v})$ routing in Theorem~\ref{thm:koszul-equivalences-meta} is the twisted-tensor identification (Remark~\ref{rem:bar-cobar-twisted-tensor-anchor}): the chain runs through Lemma~\ref{lem:twisted-product-cone-counit}, not through bar-cobar inversion.
   561	
   562	\item \emph{Theorem~B} (Bar-cobar inversion,
   563	 Theorem~\ref{thm:higher-genus-inversion}).
   564	 On the Koszul locus, the counit
   565	 $\Omega_X \bar{B}_X(\cA) \xrightarrow{\sim} \cA$
   566	 is an equivalence; the spectral sequence collapses at~$E_2$.
   567	 Off the locus, the bar-cobar object persists but becomes curved;
   568	 the failure is measured by
   569	 $\Theta_\cA := D_\cA - d_\cA^{(0)}$
   570	 (Theorem~\ref{thm:mc2-bar-intrinsic}).
   571	 The BRST resolution is complete.
   572	
   573	 More precisely, there is a spectral sequence with $E_1$ page
   574	 $E_1^{p,q} = H^q(\barB^p_X(\cA))$ converging to $H^{p+q}(\Omega_X \barB_X(\cA))$.
   575	 On the Koszul locus, $E_1^{p,q} = 0$ for $p \neq 1$, so
   576	 $E_2 = E_\infty$, and the comparison map
   577	 $\varepsilon \colon \Omega_X \barB_X(\cA) \to \cA$
   578	 induces an isomorphism on cohomology. This is the categorical
   579	 exponential: $\exp \circ \log = \operatorname{id}$.
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:450:$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
chapters/theory/higher_genus_complementarity.tex:2814:(Theorem~\ref{thm:complementarity-root-datum}). We collect the
chapters/examples/lattice_foundations.tex:1047:(Theorem~\ref{thm:complementarity-root-datum}):
chapters/examples/lattice_foundations.tex:1695:	Theorem~\textup{\ref{thm:complementarity-root-datum}}\textup{)}.
chapters/examples/bar_complex_tables.tex:2486:(Theorem~\ref{thm:complementarity-root-datum}).
chapters/examples/genus_expansions.tex:1420:(Theorem~\ref{thm:complementarity-root-datum}).
chapters/examples/genus_expansions.tex:3088:\label{thm:complementarity-root-datum}
chapters/examples/genus_expansions.tex:3506:The right-hand side depends only on the root datum \textup{(}Theorem~\textup{\ref{thm:complementarity-root-datum})}. For affine Kac--Moody algebras \textup{(}$\kappa + \kappa' = 0$\textup{)}, the complementary genera cancel: $\phi_{\mathcal{A}} = -\phi_{\mathcal{A}^!}$. For Virasoro \textup{(}$\kappa + \kappa' = 13$\textup{)}, the sum is $13 \cdot (x/2)/\sin(x/2)$.
chapters/examples/genus_expansions.tex:3623:\textup{(}Theorem~\textup{\ref{thm:complementarity-root-datum})}.
chapters/theory/higher_genus_complementarity.tex:450:$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
chapters/theory/higher_genus_complementarity.tex:2814:(Theorem~\ref{thm:complementarity-root-datum}). We collect the
 succeeded in 51ms:
chapters/examples/yangians_drinfeld_kohno.tex:90:DK is the genus-$0$ face; modular
 succeeded in 51ms:
   430	\index{modular Koszul chiral algebra!homotopy form}
   431	Let $X$ be a smooth projective curve over~$\mathbb{C}$.
   432	A \emph{modular Koszul object} on~$X$ is an augmented factorization algebra
   433	$\cA \in \operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))$
   434	equipped with:
   435	\begin{enumerate}[label=\textup{(D\arabic*$_\infty$)}]
   436	\item\label{D:bar-htpy}
   437	A bar object
   438	$\mathbf{B}_X(\cA) \in \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))$
   439	in the homotopy category of factorization coalgebras.
   440	
   441	\item\label{D:dual-htpy}
   442	A dual object~$\cA^!$.
   443	
   444	\item\label{D:deformation-htpy}
   445	A filtered cyclic deformation object
   446	$\Defcyc(\cA)$
   447	(Definition~\ref{def:cyclic-deformation-bar}),
   448	and (when constructed)
   449	a genus-completed Maurer--Cartan datum~$\Theta_{\cA}$



thinking
**Analyzing theorems and definitions**

I need to read about the complementarity theorem related to a constant K and explore genus expansions. There may be something with the local system in higher genus foundations. Also, I should examine if the complementarity sum gets defined later. I’m looking into a proposition from 1803 and its connections—it feels complex and possibly circular. The user asks if the Lagrangian decomposition is defined, and I’m wondering if I can establish a definition for it. I'll aim to clarify that before the theorem.
thinking
**Planning the foundation audit**

I need to check for build or label errors, especially unresolved references. Perhaps running scripts could help, specifically using grep for labels without definitions. The user wants a foundation audit of a file, focusing on specific surfaces while mentioning hidden unresolved imports. I wonder if I should check only within relevant theorem surfaces instead of auditing the entire file, which seems too vast. I might parse references from the first 120 lines and consider targeted checks for unresolved labels in the specified areas.
thinking
**Focusing on theorem surfaces**

I want to concentrate on the requested objects and any hidden imports within the theorem surface. The user mentioned that every missing definition, hidden import, unresolved reference, or unjustified step should be noted as a finding. It feels unfeasible to review the entire 6000 lines, but I can focus on the theorem statements and proofs instead. I might count the lines I check and summarize my findings. I could report something like "Checked: 8 surfaces," but I need to ensure clarity on what N represents in this context.
codex
I’ve confirmed that one core object, `\mathcal Z_\cA`, is only defined in another chapter. Now I’m checking the same thing for the scalar complementarity constant `K` and for the phrase “Lagrangian polarization,” because if those are only explained later or elsewhere, the theorem opening is front-loading undefined terminology.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2808,2918p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4618,4642p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '3078,3150p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Lagrangian decomposition" chapters/theory/higher_genus_complementarity.tex chapters/theory chapters/examples chapters/connections' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Lagrangian polarization" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/introduction.tex chapters/frame/heisenberg_frame.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2808	\index{complementarity!landscape|textbf}
  2809	\index{Koszul conductor|textbf}
  2810	\index{anomaly ratio|textbf}
  2811	
  2812	The complementarity sum $\kappa(\cA) + \kappa(\cA^!)$ is a
  2813	level-independent invariant for every standard family
  2814	(Theorem~\ref{thm:complementarity-root-datum}). We collect the
  2815	full data here.
  2816	
  2817	\begin{proposition}[Complementarity landscape; \ClaimStatusProvedHere]
  2818	\label{prop:complementarity-landscape}
  2819	\index{complementarity!landscape}
  2820	Let $(\cA, \cA^!)$ be a chiral Koszul pair from the standard
  2821	landscape. The complementarity sum
  2822	$\kappa(\cA) + \kappa(\cA^!)$ is determined as follows.
  2823	\begin{enumerate}[label=\textup{(\roman*)}]
  2824	\item \emph{Free fields.}\;
  2825	 For the Heisenberg~$\cH_k$, the free fermion, the
  2826	 $\beta\gamma$~system at conformal weight~$\lambda$, and
  2827	 lattice vertex algebras~$V_\Lambda$:
 succeeded in 53ms:
  4618	Its endomorphism sheaf
  4619	$\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A})$
  4620	is therefore also a strict complex, and ordinary hypercohomology
  4621	applies on the flat side.
  4622	
  4623	On the Koszul locus, Theorem~\ref{thm:cobar-resolution-scoped}
  4624	identifies the strict bar complex as a bar resolution of
  4625	$\mathcal{A}$. Hence
  4626	$\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A})$
  4627	computes the derived endomorphism complex of~$\mathcal{A}$, and
  4628	its degree-$0$ cocycles are precisely the endomorphisms commuting
  4629	with the chiral product. Their sheaf is the center local system
  4630	$\mathcal{Z}(\mathcal{A})
  4631	= \mathcal{H}^0(\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A}))$.
  4632	
  4633	The obstruction to lifting genus-$(g{-}1)$ data to genus~$g$ is the
  4634	first transgression of a local degree-$1$ deformation class, so it
  4635	is the image of
  4636	\[
  4637	d_2\colon E_2^{0,1} \longrightarrow E_2^{2,0}
 succeeded in 50ms:
  3078	
  3079	Type~(iii): If $c(\cA) = 0$ and $\cA$ is generated by a
  3080	single field of conformal weight~$2$ (i.e., $\cA$ is a
  3081	Virasoro algebra), then $\kappa(\cA) = c/2 = 0$.
  3082	More generally, for any VOA with $c = 0$, the genus-$1$
  3083	bar curvature vanishes since the Sugawara OPE has $T_{(3)}T = c/2 = 0$,
  3084	so $\kappa = 0$.
  3085	\end{proof}
  3086	
  3087	\begin{theorem}[Complementarity sum as root datum invariant; \ClaimStatusProvedHere]
  3088	\label{thm:complementarity-root-datum}
  3089	\index{complementarity!root datum invariant}
  3090	\index{obstruction coefficient!complementarity sum}
  3091	For any Koszul pair arising from a simple Lie algebra $\mathfrak{g}$ via the constructions of this monograph, the complementarity sum $\kappa(\mathcal{A}) + \kappa(\mathcal{A}^!)$ is a level-independent invariant of the root datum:
  3092	\begin{enumerate}[label=\textup{(\roman*)}]
  3093	\item \emph{Affine Kac--Moody:} $\kappa(\widehat{\mathfrak{g}}_k) + \kappa(\widehat{\mathfrak{g}}_{k'}) = 0$ \textup{(}exact cancellation\textup{)}.
  3094	\item \emph{Principal $\mathcal{W}$-algebra for $\mathfrak{sl}_N$:}
  3095	\begin{equation}\label{eq:wn-kappa-sum-general}
  3096	\kappa(\mathcal{W}_N^k) + \kappa(\mathcal{W}_N^{k'}) = 2(N{-}1)(2N^2{+}2N{+}1) \cdot (H_N - 1)
  3097	\end{equation}
 succeeded in 53ms:
chapters/theory/higher_genus_complementarity.tex:458:\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:1890:Lagrangian polarization at the level of cohomology, and
chapters/theory/higher_genus_complementarity.tex:1947:\item \emph{Bar-side eigenspaces lift the ambient Lagrangian polarization.}
chapters/theory/higher_genus_complementarity.tex:5176:Lagrangian polarizations: one branch records the deformations visible
chapters/theory/higher_genus_modular_koszul.tex:4019: the Lagrangian polarization
chapters/theory/higher_genus_modular_koszul.tex:4130:off-diagonal in the Lagrangian polarization, so every internal
 succeeded in 55ms:
chapters/connections/thqg_symplectic_polarization.tex:953:\textbf{(C2b) Lagrangian decomposition.}\;
chapters/connections/thqg_symplectic_polarization.tex:995:\emph{Part (C2b): Lagrangian decomposition.}
chapters/connections/thqg_preface_supplement.tex:971:of the moduli of flat connections. The Lagrangian decomposition
chapters/connections/concordance.tex:7707:assembles into a Lagrangian decomposition of the shifted-symplectic
chapters/connections/thqg_introduction_supplement_body.tex:1024:Lagrangian decomposition persists but the genus-$1$ obstruction
chapters/theory/higher_genus_modular_koszul.tex:165: a Lagrangian decomposition of moduli-space cohomology.
chapters/theory/higher_genus_modular_koszul.tex:4153:$\ell_r^{(0),\mathrm{tr}}$. The Lagrangian decomposition
chapters/theory/higher_genus_modular_koszul.tex:4196:The Lagrangian decomposition
chapters/theory/higher_genus_modular_koszul.tex:30377:\item \emph{Complementarity}: the Lagrangian decomposition of Theorem~C is the polarization into $\cA$-side and $\cA^!$-side components (under perfectness hypotheses).
chapters/connections/holographic_codes_koszul.tex:203:The Lagrangian decomposition
chapters/connections/holographic_codes_koszul.tex:226:The Lagrangian decomposition
chapters/connections/holographic_codes_koszul.tex:361:\item The Lagrangian decomposition
chapters/connections/thqg_entanglement_programme.tex:104:The Lagrangian decomposition
chapters/connections/thqg_entanglement_programme.tex:138:The Lagrangian decomposition $Q_g \oplus Q_g^!$ provides
chapters/connections/thqg_entanglement_programme.tex:166:Lagrangian decomposition
chapters/connections/frontier_modular_holography_platonic.tex:17:\item the complementary-Lagrangian decomposition
chapters/connections/thqg_gravitational_s_duality.tex:2002:The Lagrangian decomposition follows from
chapters/theory/bar_cobar_adjunction_inversion.tex:3883:The Lagrangian decomposition
chapters/theory/computational_methods.tex:1325:Theorem~C (complementarity): the Lagrangian decomposition
chapters/theory/introduction.tex.bak:101:a Lagrangian decomposition that constrains the Koszul
codex
The scalar constant `K` is not defined where the chapter opening first uses it. The file only explains the complementarity sum much later, around the landscape proposition. I’m checking whether the early prose can be defended by a prior local definition; so far it cannot.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '930,970p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '145,175p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   930	\begin{theorem}[Verdier Lagrangian polarization (C2);
   931	\ClaimStatusConditional]
   932	\label{thm:thqg-III-lagrangian-polarization}
   933	\index{Lagrangian!polarization!holographic}
   934	Let $(\cA, \cA^!)$ be a chiral Koszul pair on $X$.
   935	Assume:
   936	\begin{enumerate}[label=\textup{(H\arabic*)}]
   937	\item \emph{Perfectness:} $R\pi_{g*}\barB^{(g)}(\cA)$ is
   938	 perfect on $\overline{\mathcal{M}}_g$
   939	 \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
   940	\item \emph{Nondegeneracy:} the holographic Verdier pairing
   941	 $\langle -, - \rangle_g$ is nondegenerate
   942	 \textup{(}Lemma~\textup{\ref{lem:thqg-III-nondegeneracy})}.
   943	\end{enumerate}
   944	Then for $g \ge 2$:
   945	
   946	\smallskip\noindent
   947	\textbf{(C2a) Shifted symplectic structure.}\;
   948	$\mathbf{C}_g(\cA)$ carries a $(-(3g-3))$-shifted symplectic
   949	structure in the PTVV sense
 succeeded in 51ms:
   145	
   146	 No other depths occur (Proposition~\ref{prop:depth-gap-trichotomy}):
   147	 $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$, with a gap at~$3$.
   148	
   149	\item \emph{Formality}
   150	 (Theorem~\ref{thm:shadow-formality-identification}). The
   151	 genus-$0$ shadow obstruction tower coincides with the
   152	 $L_\infty$~formality obstruction tower:
   153	 $\kappa$, $\mathfrak{C}$, $\mathfrak{Q}$ are the genus-$0$
   154	 obstructions at degrees $2$, $3$, $4$, and the four-class
   155	 partition $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ is the
   156	 formality classification of the transferred
   157	 $L_\infty$-structure.
   158	 Positive-genus corrections are carried by the quantum layer.
   159	
   160	\item \emph{Complementarity}
   161	 (Theorem~\ref{thm:quantum-complementarity-main}). For a Koszul pair
   162	 $(\cA, \cA^!)$, the quantum corrections decompose as
   163	 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
   164	 H^*(\overline{\mathcal{M}}_g, Z(\cA))$:
exec
/bin/zsh -lc "rg -n -F \"\\label{prop:ptvv-lagrangian}\" chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{thm:verdier-bar-cobar}\" chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{thm:lagrangian-complementarity}\" chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:2030:\label{prop:ptvv-lagrangian}
 succeeded in 51ms:
chapters/theory/cobar_construction.tex:1313:\label{thm:verdier-bar-cobar}
 succeeded in 53ms:
chapters/connections/concordance.tex:4963:\ClaimStatusProvedHere]\label{thm:lagrangian-complementarity}
chapters/connections/outlook.tex:666:\phantomsection\label{thm:lagrangian-complementarity}
codex
I’m stress-testing the theorem’s imported machinery now. The danger is not just missing definitions; it’s that the file claims “the Verdier involution” exists on the ambient complex by citing a theorem that may only give a bar/cobar duality, not the actual involution used in `C1`.
exec
/bin/zsh -lc 'rg -n -F "thm:ss-quantum" chapters/theory/higher_genus_complementarity.tex chapters/theory' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:kodaira-spencer-chiral-complete" chapters/theory/higher_genus_complementarity.tex chapters/theory' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1290,1365p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "cor:duality-bar-complexes-complete" chapters/theory/cobar_construction.tex chapters/theory/higher_genus_complementarity.tex chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:707:\label{thm:ss-quantum}
chapters/theory/higher_genus_complementarity.tex:730:\begin{proof}[Proof of Theorem~\ref{thm:ss-quantum}]
chapters/theory/higher_genus_complementarity.tex:795:Theorem~\textup{\ref{thm:ss-quantum}} converges to
chapters/theory/higher_genus_complementarity.tex:1477:(Theorem~\ref{thm:ss-quantum}) identifies both $Q_g(\mathcal{A})$ and
chapters/theory/higher_genus_complementarity.tex:4075:(established in the proof of Theorem~\ref{thm:ss-quantum},
chapters/theory/chiral_modules.tex:1248: (Theorem~\ref{thm:ss-quantum}).
chapters/theory/higher_genus_complementarity.tex:707:\label{thm:ss-quantum}
chapters/theory/higher_genus_complementarity.tex:730:\begin{proof}[Proof of Theorem~\ref{thm:ss-quantum}]
chapters/theory/higher_genus_complementarity.tex:795:Theorem~\textup{\ref{thm:ss-quantum}} converges to
chapters/theory/higher_genus_complementarity.tex:1477:(Theorem~\ref{thm:ss-quantum}) identifies both $Q_g(\mathcal{A})$ and
chapters/theory/higher_genus_complementarity.tex:4075:(established in the proof of Theorem~\ref{thm:ss-quantum},
 succeeded in 51ms:
  1290	
  1291	\begin{remark}[CFT vertex operators from cobar]\label{rem:vertex-operators-cobar}
  1292	In conformal field theory, vertex operators $V_\alpha(z)$ create states $|\alpha\rangle$ 
  1293	at position $z$. These correspond to cobar elements:
  1294	\[V_\alpha \leftrightarrow K_\alpha \in \Omega^1(\mathcal{C})\]
  1295	
  1296	The OPE of vertex operators:
  1297	\[V_\alpha(z) V_\beta(w) \sim \sum_\gamma \frac{C_{\alpha\beta}^\gamma}{(z-w)^{h_\gamma - h_\alpha - h_\beta}} V_\gamma(w)\]
  1298	
  1299	corresponds to the cobar product:
  1300	\[n_2(K_\alpha, K_\beta) = \sum_\gamma C_{\alpha\beta}^\gamma K_\gamma\]
  1301	
  1302	The structure constants $C_{\alpha\beta}^\gamma$ are precisely the cobar $A_\infty$ 
  1303	structure constants.
  1304	
  1305	The cobar construction thus provides a geometric derivation
  1306	of the OPE algebra in CFT.
  1307	\end{remark}
  1308	
  1309	\subsection{Verdier duality on bar and cobar}
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:511:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
chapters/theory/higher_genus_foundations.tex:1053:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}). The obstruction
chapters/theory/higher_genus_foundations.tex:4947:The sign reversal is consistent with Main~Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}; the Kodaira--Spencer construction of Theorem~\ref{thm:kodaira-spencer-chiral-complete} provides the geometric mechanism):
chapters/theory/hochschild_cohomology.tex:859:class (Theorem~\ref{thm:kodaira-spencer-chiral-complete}). The partner
chapters/theory/hochschild_cohomology.tex:877:The Kodaira--Spencer class $\mathrm{KS}_g(\mathcal{A}) \in H^1(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$ satisfies $\mathrm{KS}_g(\mathcal{A}) = -\mathrm{KS}_g(\mathcal{A}^!)$ under the Verdier involution (Theorem~\ref{thm:kodaira-spencer-chiral-complete}, equation~\eqref{eq:verdier-ks-anticommute}). The periodicity class $\Theta$ arises from the $g = 0$ contribution to the Kodaira--Spencer class via the bar complex on $\overline{\mathcal{M}}_{0,4} \cong \mathbb{P}^1$ (proof of Theorem~\ref{thm:virasoro-periodicity}, Step~1). The Verdier anti-commutativity descends to the periodicity generators: $\Theta$ on the $\mathcal{A}$ side corresponds to $-\Theta'$ on the $\mathcal{A}^!$ side.
chapters/theory/chiral_hochschild_koszul.tex:676:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}) provides a
chapters/theory/chiral_hochschild_koszul.tex:698:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
chapters/theory/chiral_hochschild_koszul.tex:3459:Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
chapters/theory/chiral_hochschild_koszul.tex:4153:The Kodaira--Spencer map (Theorem~\ref{thm:kodaira-spencer-chiral-complete}) provides a ring homomorphism
chapters/theory/chiral_hochschild_koszul.tex:4503:Both $\cA$ and $\cA^!$ live on the same curve $X$. The Hodge bundle contribution from $\overline{\mathcal{M}}_g$ (via the Kodaira--Spencer map, Theorem~\ref{thm:kodaira-spencer-chiral-complete}) depends only on the geometry of~$X$, not on the chiral algebra. Since $\kappa(\lambda)$ is the image of $\lambda = c_1(\mathbb{E})$ under the same ring homomorphism for both $\cA$ and $\cA^!$, the nilpotency index is preserved.
chapters/theory/higher_genus_complementarity.tex:541:Step~III (from Theorem~\ref{thm:kodaira-spencer-chiral-complete})
chapters/theory/higher_genus_complementarity.tex:1258:\label{thm:kodaira-spencer-chiral-complete}
chapters/theory/higher_genus_complementarity.tex:1282:\begin{proof}[Proof of Theorem~\ref{thm:kodaira-spencer-chiral-complete}]
chapters/theory/higher_genus_complementarity.tex:1777:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}, Step~7).
chapters/theory/higher_genus_complementarity.tex:1850:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}) and
chapters/theory/higher_genus_complementarity.tex:541:Step~III (from Theorem~\ref{thm:kodaira-spencer-chiral-complete})
chapters/theory/higher_genus_complementarity.tex:1258:\label{thm:kodaira-spencer-chiral-complete}
chapters/theory/higher_genus_complementarity.tex:1282:\begin{proof}[Proof of Theorem~\ref{thm:kodaira-spencer-chiral-complete}]
chapters/theory/higher_genus_complementarity.tex:1777:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}, Step~7).
chapters/theory/higher_genus_complementarity.tex:1850:(Theorem~\ref{thm:kodaira-spencer-chiral-complete}) and
 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:1128:\label{cor:duality-bar-complexes-complete}
chapters/theory/higher_genus_complementarity.tex:1137:\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
chapters/theory/higher_genus_complementarity.tex:1184:By Corollary~\ref{cor:duality-bar-complexes-complete}, the pairing:
chapters/theory/higher_genus_complementarity.tex:1378:(Corollary~\ref{cor:duality-bar-complexes-complete}) with the
chapters/theory/higher_genus_complementarity.tex:1460:By Corollary~\ref{cor:duality-bar-complexes-complete}, the Verdier-Koszul pairing
chapters/theory/higher_genus_complementarity.tex:1967:configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
chapters/theory/higher_genus_complementarity.tex:1128:\label{cor:duality-bar-complexes-complete}
chapters/theory/higher_genus_complementarity.tex:1137:\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
chapters/theory/higher_genus_complementarity.tex:1184:By Corollary~\ref{cor:duality-bar-complexes-complete}, the pairing:
chapters/theory/higher_genus_complementarity.tex:1378:(Corollary~\ref{cor:duality-bar-complexes-complete}) with the
chapters/theory/higher_genus_complementarity.tex:1460:By Corollary~\ref{cor:duality-bar-complexes-complete}, the Verdier-Koszul pairing
chapters/theory/higher_genus_complementarity.tex:1967:configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}


thinking
**Identifying a theorem issue**

I'm considering whether this is referring to the theorem `thm:verdier-bar-cobar`, which only applies to genus-0 cases. That makes me suspicious since the definition in complementarity-complexes mentions sigma on the ambient complex and refers to an involution, but this theorem doesn't seem to support that. I need to determine how to correct this by either clarifying the definition or adjusting my references in the text. Also, I may need to inspect `thm:ss-quantum` for potential issues with Step 8.
thinking
**Examining definitions and issues**

I see that the earlier Lemma quant from ss defines Q_g(A) as a graded piece of bar cohomology, but later on, the theorem redefines Q_g through eigenspaces. This introduces some issues, particularly regarding stability in objects in C1. The user wants to know if all objects in C0, C1, and C2 are defined before the theorems. It seems there’s a potential finding here, especially since Q_g(A) is introduced in the opening lines before its formal definition later on. It also crops up in equation 19, which complicates things.
codex
I’m now checking the first actual proof jump in `C0`: the file claims the surviving fiber cohomology is “hence” the center by a cited genus-0 corollary. If that corollary only identifies bar cohomology with the Koszul dual coalgebra, the proof is overreaching and needs a bridge lemma, not rhetoric.
exec
/bin/zsh -lc 'rg -n -F "cor:bar-cohomology-koszul-dual" chapters/theory chapters/examples appendices' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:geometric-equals-operadic-bar" chapters/theory chapters/examples appendices' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:e1-module-koszul-duality" chapters/theory chapters/examples appendices' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:bar-concentration" chapters/theory chapters/examples appendices' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/examples/deformation_quantization.tex:147:For coisson algebras, the classical Kontsevich formality theorem ensures the vanishing of all higher obstructions at the operadic level: the $E_2$-operad (governing Poisson structures) is formal, so the deformation problem is unobstructed. Theorem~\ref{thm:geometric-equals-operadic-bar} lifts this to the curve $X$: the same object as the operadic bar construction is computed via the geometric bar complex, so formality propagates from the classical to the chiral setting. Gauge equivalence follows from the standard deformation-theoretic argument: different choices of Maurer--Cartan element in the same gauge orbit give isomorphic deformations.
chapters/examples/deformation_quantization.tex:641:(Theorem~\ref{thm:geometric-equals-operadic-bar}) provides the
chapters/examples/deformation_quantization.tex:811:(Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/theory/higher_genus_modular_koszul.tex:370:(Theorem~\ref{thm:geometric-equals-operadic-bar}) identifies
chapters/theory/bar_construction.tex:2065:\label{thm:geometric-equals-operadic-bar}
chapters/examples/kac_moody.tex:1953:For $\cA = \widehat{\mathfrak{g}}_k$, the geometric realization of the bar complex on $\overline{C}_{n+1}(X)$ (Theorem~\ref{thm:geometric-equals-operadic-bar}) identifies the transferred operations with configuration space integrals: $m_n$ is computed by integrating the product of input forms against the propagator $\Phi_n$ over the compactified configuration space. The $A_\infty$ relations $\sum_{r+s+t=n}(-1)^{rs+t} m_{r+1+t}(\mathrm{id}^{\otimes r} \otimes m_s \otimes \mathrm{id}^{\otimes t}) = 0$ follow from the Stokes theorem on $\overline{C}_n(X)$: the boundary strata of the FM compactification encode exactly the compositions of lower operations.
chapters/examples/bar_complex_tables.tex:1488:Theorem~\ref{thm:geometric-equals-operadic-bar}
chapters/examples/bar_complex_tables.tex:1643:This is Theorem~\ref{thm:geometric-equals-operadic-bar} made
chapters/examples/bar_complex_tables.tex:1974:verify Theorem~\ref{thm:geometric-equals-operadic-bar} for
chapters/theory/chiral_koszul_pairs.tex:5656:The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
chapters/theory/chiral_hochschild_koszul.tex:3570:(Theorem~\ref{thm:geometric-equals-operadic-bar} for genus~$0$;
chapters/examples/w_algebras.tex:1366:$\overline{C}_3(X)$ (Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/theory/configuration_spaces.tex:3658: \emph{(2) Quasi-isomorphism invariance.} This is a standard consequence of the fact that $\bar{B}^{\mathrm{ch}}$ is a derived functor: it preserves quasi-isomorphisms between augmented chiral algebras (see \cite[Theorem~2.2.4]{LV12} for the operadic statement, which applies verbatim in the chiral setting via the chiral operad formalism of Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/theory/higher_genus_complementarity.tex:1006:Theorem~\ref{thm:geometric-equals-operadic-bar}, the complex
chapters/theory/higher_genus_complementarity.tex:2343:(Theorem~\ref{thm:geometric-equals-operadic-bar}), an isomorphism on
appendices/koszul_reference.tex:127:(Theorem~\ref{thm:geometric-equals-operadic-bar}) with the higher-genus
appendices/koszul_reference.tex:445:By Theorem~\ref{thm:geometric-equals-operadic-bar}, the geometric bar
 succeeded in 53ms:
appendices/combinatorial_frontier.tex:30:For a Koszul chiral algebra~$\cA$, the bar cohomology dimensions $\dim H^n(\barBgeom(\cA))$ coincide with the Hilbert function of the Koszul dual $\cA^!$ (Corollary~\ref{cor:bar-cohomology-koszul-dual}). These dimensions are the central enumerative invariants of the theory. Their generating functions encode, in compact form, the full structure of the bar complex: growth rates, analytic singularities, and (conjecturally) the spectral data of a finite-rank transfer operator.
appendices/combinatorial_frontier.tex:213:(Corollary~\ref{cor:bar-cohomology-koszul-dual},
chapters/examples/bar_complex_tables.tex:1960:(Corollary~\ref{cor:bar-cohomology-koszul-dual}, Step~4),
chapters/examples/landscape_census.tex:1761:By the $E_2$ collapse (Corollary~\ref{cor:bar-cohomology-koszul-dual}),
chapters/examples/landscape_census.tex:1806:(Corollary~\ref{cor:bar-cohomology-koszul-dual}) applied to
chapters/examples/landscape_census.tex:1816: from Corollary~\ref{cor:bar-cohomology-koszul-dual}.
chapters/examples/landscape_census.tex:1820: Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/examples/landscape_census.tex:1825: Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/examples/landscape_census.tex:1831: Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/examples/landscape_census.tex:1837: (Corollary~\ref{cor:bar-cohomology-koszul-dual},
chapters/examples/landscape_census.tex:1865: (Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/examples/landscape_census.tex:1969:$E_2$ collapse (Corollary~\ref{cor:bar-cohomology-koszul-dual})
chapters/examples/landscape_census.tex:2173:(Corollary~\ref{cor:bar-cohomology-koszul-dual},
chapters/examples/landscape_census.tex:2825:with Corollary~\ref{cor:bar-cohomology-koszul-dual}
chapters/examples/landscape_census.tex:3196:For a Koszul algebra $\cA$, the Koszul dual Hilbert function $\dim (\cA^!)_n$ equals the conformal-weight-graded bar cohomology dimension at bar degree~$n$ (Corollary~\ref{cor:bar-cohomology-koszul-dual}). The generating function $P_{\cA}(x) = \sum_n \dim (\cA^!)_n\, x^n$ is the Hilbert series of $\cA^!$. In the Kac--Moody case, $P_{\widehat{\mathfrak{g}}_k}(x)$ coincides with the Hilbert series of $\mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{-k-2h^\vee})$ as a graded algebra; this is independent of~$k$ because the Koszul dual has the same graded structure at all generic levels.
chapters/theory/higher_genus_foundations.tex:1663:(Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/theory/chiral_koszul_pairs.tex:925:\label{cor:bar-cohomology-koszul-dual}
chapters/theory/chiral_koszul_pairs.tex:1151:Corollary~\ref{cor:bar-cohomology-koszul-dual} then gives
chapters/theory/chiral_koszul_pairs.tex:1211:(Corollary~\ref{cor:bar-cohomology-koszul-dual}) admits a sharp
chapters/theory/chiral_koszul_pairs.tex:3805:(Corollary~\ref{cor:bar-cohomology-koszul-dual}, Step~4),
 succeeded in 52ms:
appendices/koszul_reference.tex:410:(Theorem~\ref{thm:bar-concentration}):
chapters/theory/chiral_hochschild_koszul.tex:498:\textup{(}Theorem~\textup{\ref{thm:bar-concentration})}
chapters/theory/chiral_hochschild_koszul.tex:524:cohomology. By Theorem~\ref{thm:bar-concentration}, the bar
chapters/theory/chiral_hochschild_koszul.tex:564:degree. On the Koszul locus, Theorem~\ref{thm:bar-concentration}
chapters/theory/chiral_hochschild_koszul.tex:600:\textup{(}Theorem~\textup{\ref{thm:bar-concentration})} forces
chapters/theory/chiral_hochschild_koszul.tex:900:(Theorem~\ref{thm:bar-concentration}) gives
chapters/theory/chiral_hochschild_koszul.tex:1065: (Theorem~\ref{thm:bar-concentration}).
chapters/theory/chiral_hochschild_koszul.tex:1200:(Theorem~\ref{thm:bar-concentration}),
chapters/theory/higher_genus_complementarity.tex:1012:theorem (Theorem~\ref{thm:bar-concentration}) gives
chapters/theory/higher_genus_foundations.tex:2702:(Theorem~\ref{thm:bar-concentration}) forces the only surviving
chapters/theory/hochschild_cohomology.tex:174:Theorem~\ref{thm:bar-concentration}), Theorem~H does not apply
chapters/theory/cobar_construction.tex:2982: (Theorem~\ref{thm:bar-concentration}). The Koszul dual algebra
chapters/theory/chiral_koszul_pairs.tex:548: (Theorem~\ref{thm:bar-concentration}): for a Koszul morphism,
chapters/theory/chiral_koszul_pairs.tex:1113:\label{thm:bar-concentration}
chapters/theory/chiral_koszul_pairs.tex:2101:(Theorem~\ref{thm:bar-concentration}), which is the input for
chapters/theory/chiral_koszul_pairs.tex:5957: (Theorem~\ref{thm:bar-concentration}), used by
chapters/theory/introduction.tex:554: ($\mathrm{A}_1$, Theorem~\ref{thm:bar-concentration}), and
 succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:873:already used in Theorem~\ref{thm:e1-module-koszul-duality}.
chapters/theory/bar_cobar_adjunction_inversion.tex:1474:Theorem~\textup{\ref{thm:e1-module-koszul-duality}}.
chapters/theory/bar_cobar_adjunction_inversion.tex:1524:Theorem~\textup{\ref{thm:e1-module-koszul-duality}}.
chapters/theory/bar_cobar_adjunction_inversion.tex:1548:Theorem~\ref{thm:e1-module-koszul-duality}.
chapters/theory/bar_cobar_adjunction_inversion.tex:1560:Theorem~\ref{thm:e1-module-koszul-duality}.
chapters/theory/bar_cobar_adjunction_inversion.tex:2314:Theorem~\ref{thm:e1-module-koszul-duality} on the quadratic genus-$0$
chapters/theory/bar_cobar_adjunction_inversion.tex:3424:Theorem~\ref{thm:e1-module-koszul-duality}. Off these loci, the
chapters/examples/free_fields.tex:1897:\textup{(}Theorem~\textup{\ref{thm:e1-module-koszul-duality})}
chapters/examples/free_fields.tex:1925:Apply Theorem~\ref{thm:e1-module-koszul-duality} to the
chapters/examples/free_fields.tex:2040:Apply Theorem~\ref{thm:e1-module-koszul-duality} (module Koszul duality) to
chapters/examples/free_fields.tex:2215:Theorem~\ref{thm:e1-module-koszul-duality} to
chapters/examples/free_fields.tex:2464:module Koszul duality (Theorem~\ref{thm:e1-module-koszul-duality}) sends
chapters/examples/kac_moody.tex:4151:and the module-level duality of Theorem~\ref{thm:e1-module-koszul-duality}
chapters/examples/kac_moody.tex:4231:\emph{Proved here}: level-shifting duality (Theorem~\ref{thm:universal-kac-moody-koszul}), module-level bar-cobar (Theorem~\ref{thm:e1-module-koszul-duality}), bar resolution with KL multiplicities (Remark~\ref{rem:bar-complex-kl-polynomials}), $2\mathsf{h}$-periodicity for type $A_1$ (Proposition~\ref{prop:periodicity-same-type}), affine Hecke Koszul duality (Proposition~\ref{prop:affine-hecke-kd}), tensor structure (Theorem~\ref{thm:fusion-bar-cobar}), and weightwise finiteness at non-degenerate admissible level (Corollary~\ref{cor:bar-admissible-finiteness}).
chapters/examples/kac_moody.tex:4451:\textup{(}Theorem~\textup{\ref{thm:e1-module-koszul-duality})}
chapters/examples/kac_moody.tex:4513:duality of Theorem~\ref{thm:e1-module-koszul-duality} to a
chapters/examples/w_algebras.tex:2906:The level shift $k \mapsto k' = -k - 2h^\vee$ (Theorem~\ref{thm:w-algebra-koszul-main}) extends to modules: $H^0_{\mathrm{DS}}(\mathrm{Ind}(M)) \simeq \mathrm{Ind}_W(H^0_{\mathrm{DS}}(M))$ (Theorem~\ref{thm:e1-module-koszul-duality}). At minimal model values $k = -h^\vee + p/q$, $\mathcal{W}^k$ is rational ($X_{\mathcal{W}^k} = \{0\}$, Arakawa~\cite{Arakawa17}), while at the dual level $k' = -h^\vee - p/q$ it is non-rational ($X_{\mathcal{W}^{k'}} \neq \{0\}$).
chapters/examples/bar_complex_tables.tex:4431:Theorem~\textup{\ref{thm:e1-module-koszul-duality}}
chapters/examples/yangians_drinfeld_kohno.tex:170:\textup{(}Theorem~\textup{\ref{thm:e1-module-koszul-duality})}
chapters/examples/yangians_drinfeld_kohno.tex:188:genus-$0$ lane \textup{(}Theorem~\textup{\ref{thm:e1-module-koszul-duality})},

thinking
**Inspecting theorem imports**

I think there might be more issues with the proof steps and how theorems are imported. I need to closely inspect the relevant lines related to bar cohomology and its Koszul dual. It feels a bit scattered right now, but focusing on these specific areas might help clarify any misunderstandings. I want to make sure everything aligns properly, so I’ll take the time to carefully examine those details.
codex
The `C0` proof does look shaky: it cites a genus-0 corollary about bar cohomology and then silently upgrades that to a genus-g center identification. I’m reading the cited corollary directly to see whether that bridge exists or has simply been omitted.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '900,965p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '2055,2095p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5168,5208p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2055	$\mathrm{SC}^{\mathrm{ch,top}}$ on
  2056	$\FM_k(\bC) \times \Conf_n^{<}(\bR)$.
  2057	\end{remark}
  2058	
  2059	\begin{remark}[Conventions for this chapter]\label{rem:three-bar-conventions}
  2060	\index{bar complex!convention in this chapter}
  2061	In this chapter, the unadorned notation $\bar{B}^{\mathrm{geom}}(\mathcal{A})$ denotes the symmetric bar $\mathrm{Sym}^c(s^{-1}\bar{\mathcal{A}})$ (Theorem~\ref{thm:three-bar-complexes}(ii)): the coproduct (Theorems~\ref{thm:bar-coalgebra}--\ref{thm:coassociativity-complete}) is the coshuffle on $\mathrm{Sym}^c$, matching the geometric decomposition of $\overline{C}_{n+1}(X)$ into unordered collision strata. Every theorem in this chapter is $\Sigma_n$-invariant (Remark~\ref{rem:primacy-direction}).
  2062	\end{remark}
  2063	
  2064	\begin{theorem}[Geometric bar \texorpdfstring{$=$}{=} operadic bar; \ClaimStatusProvedHere]
  2065	\label{thm:geometric-equals-operadic-bar}
  2066	\index{geometric equals operadic bar}
  2067	\index{bar construction!algebraic}
  2068	\index{twisting morphism!chiral}
  2069	Let $\mathcal{P}^{\mathrm{ch}}$ be a chiral operad on $X$ (either
  2070	$\chirCom$ or $\chirAss$) and let $\mathcal{A}$ be an augmented
  2071	$\mathcal{P}^{\mathrm{ch}}$-algebra. Then the geometric bar complex
  2072	$\bar{B}_{\mathrm{geom}}(\mathcal{A})$
  2073	(Definition~\ref{def:geometric-bar}) is naturally quasi-isomorphic
  2074	to the operadic bar construction
 succeeded in 52ms:
   900	$V = \bigoplus_{n \geq 2} \bC \cdot L_{-n}$
   901	(the Virasoro generators modulo vacuum), which is
   902	free of finite rank in each conformal weight.
   903	
   904	\emph{Hypothesis~\ref{item:pbw-classical-koszul}.}
   905	$\operatorname{gr}_F \mathrm{Vir}_c
   906	\cong \operatorname{Sym}(V)$
   907	is a polynomial algebra (the OPE reduces to a commutative
   908	product on the associated graded: the non-linear terms
   909	$T_{(0)}T = \partial T$, $T_{(1)}T = 2T$ are lower-order in the
   910	PBW filtration, and the quartic pole $T_{(3)}T = c/2$ is a
   911	scalar that contributes to the curvature, not the
   912	associated graded bracket).
   913	By Priddy's theorem, $\operatorname{Sym}(V)$ is Koszul.
   914	
   915	\emph{Hypothesis~\ref{item:pbw-bounded}.}
   916	Same argument as the Kac--Moody case: the number of
   917	partitions of weight~$h$ into at most $n$ parts (each $\geq 2$)
   918	is finite.
   919	
 succeeded in 53ms:
  5168	require extra hypotheses and a module-level comparison theorem beyond
  5169	what is currently established here.
  5170	\end{remark}
  5171	
  5172	\subsection{\texorpdfstring{$\Eone$-chiral module category Koszul duality}{E1-chiral module category Koszul duality}}
  5173	
  5174	\begin{theorem}[\texorpdfstring{$\Eone$}{E1}-module category Koszul duality;
  5175	\ClaimStatusProvedHere]
  5176	\label{thm:e1-module-koszul-duality}
  5177	\index{module Koszul duality|textbf}
  5178	Let $\mathcal{A}$ be a Koszul $\Eone$-chiral algebra with Koszul
  5179	dual bar coalgebra
  5180	$C_{\mathcal{A}} := \bar{B}^{\mathrm{ch}}(\mathcal{A})$
  5181	\textup{(}Theorem~\ref{thm:e1-chiral-koszul-duality},
  5182	Corollary~\ref{cor:e1-self-duality}\textup{)}. When the finite-type
  5183	graded dual exists, we write $\mathcal{A}^! := C_{\mathcal{A}}^\vee$
  5184	for the corresponding dual algebra. Then the bar-cobar adjunction
  5185	restricts to an equivalence of derived categories between
  5186	\emph{complete} (pro-nilpotent) $\mathcal{A}$-modules and
  5187	\emph{conilpotent} $C_{\mathcal{A}}$-comodules:

thinking
**Investigating quantum lines**

I need to check Step I of the theorem regarding ss-quantum lines, particularly around lines 707 and also 680-720, to determine if "Q_g" is defined correctly. The proof for theorem C1 states that Step I constructs a spectral sequence that identifies `Q_g` with E∞. I'm wondering if there's any notational overload here, so I should carefully inspect the surrounding definitions in `thm:ss-quantum` to clarify the definition of Q_g.
codex
I’m checking the symbol hygiene now. There are at least two layers of `Q_g`: one from the genus-filtration spectral sequence and one from the later `\pm1` eigenspace definition. If those are not separated cleanly, the theorem is not just underdefined, it is genuinely ambiguous.
exec
/bin/zsh -lc "rg -n -F \"Q_g(\\mathcal{A}) :=\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '680,875p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\mathbf{Q}_g(\\cA)\" chapters/theory/higher_genus_complementarity.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Q_g(\\cA) :=\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
875:Q_g(\mathcal{A}) := \text{gr}^g H^*(\bar{B}(\mathcal{A})) = E_\infty^{*,*,g}
 succeeded in 51ms:
82: \cite{PTVV13}\textup{)}, and the summands $\mathbf{Q}_g(\cA)$ and
84: rank, with $\mathbf{Q}_g(\cA) \simeq
200:\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \mathrm{id}\colon
207:Q_g(\cA) &:= H^*(\mathbf{Q}_g(\cA))
470:Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
482: \mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
494: $\mathbf{Q}_g(\cA) \otimes \mathbf{Q}_g(\cA^!) \to \mathbb{C}[-{(3g{-}3)}]$,
495: so $\mathbf{Q}_g(\cA) \simeq \mathbf{Q}_g(\cA^!)^\vee[-(3g{-}3)]$.
570:$\mathbf{Q}_g(\cA)=\operatorname{fib}(\sigma-\mathrm{id})$ is modeled by
596:The decomposition $\mathbf{C}_g\simeq\mathbf{Q}_g(\cA)\oplus
2003:$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$. Theorem~\ref{thm:quantum-complementarity-main}
5173:$\mathbf{C}_g(\cA) \simeq \mathbf{Q}_g(\cA) \oplus
5188:The two complementary branches $\mathbf{Q}_g(\cA)$ and
5238:\cofib\!\bigl(\mathbf{Q}_g(\cA)
5278:gives $\mathbf{C}_g(\cA) \simeq \mathbf{Q}_g(\cA) \oplus
5288:$V_g(\cA) := \mathbf{Q}_g(\cA)$,
5819: $\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
 succeeded in 51ms:
   680	\begin{equation}
   681	\bar{B}^{(h)}(\mathcal{A}) = R\Gamma(\overline{\mathcal{M}}_h, \mathcal{H}^*(\mathcal{
   682	C}_n, \mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log}))
   683	\end{equation}
   684	
   685	The genus filtration $F^{\leq g}$ consists of contributions from curves of genus 
   686	$\leq g$. This is well-defined because:
   687	\begin{enumerate}
   688	\item The differential $d = \sum_{D} \text{Res}_D$ respects the genus filtration 
   689	(residues at divisors do not change genus)
   690	\item The comultiplication $\Delta$ respects the genus filtration (splitting points 
   691	does not change total genus)
   692	\end{enumerate}
   693	\end{proof}
   694	
   695	\begin{remark}[Physical interpretation]
   696	In quantum field theory, the genus expansion is the \emph{loop expansion}:
   697	\begin{equation}
   698	Z = Z^{(0)} + \hbar Z^{(1)} + \hbar^2 Z^{(2)} + \cdots
   699	\end{equation}
 exited 1 in 51ms:



thinking
**Clarifying proof references**

I'm considering that the user is asking about unresolved references and hidden imports. There’s a specific reference in the proof that cites `Sublemma\ref{lem:center-isomorphism}` at line 1374, which is more of an internal label in the proof. While it might be okay to use, it's not the ideal situation. Still, the user hasn't brought this point up directly, so I wonder if it’s something that needs addressing.
thinking
**Running script for references**

I'm thinking about running a script to check for references in lines 1-600 and see if any labels exist. It seems like a straightforward task, and it could help clarify things. I'll need to make sure the script is set up correctly to capture that information. If there are labels present, that might give us valuable insights to work with. Let's see how this goes!
codex
I’m running a direct label existence check now. If the theorem surface cites labels that do not exist anywhere in the repo, that’s a hard failure; if they exist only in distant files without local import, that’s a hidden-dependency failure.
exec
/bin/zsh -lc 'labels=$(perl -ne '"'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/higher_genus_complementarity.tex | sort -u); for label in "'$labels; do if ! rg -n -F "'"\\\\label{"'$label}" chapters appendices metadata >/dev/null; then echo "MISSING $label"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
MISSING MK:modular
app:nonlinear-modular-shadows
app:sign-conventions
app:signs
ch:bv-brst
ch:en-koszul-duality
conj:master-bv-brst
conj:physical-complementarity
conj:string-theory-complementarity-explicit
conv:bar-coalgebra-identity
conv:heisenberg-kappa-notation
conv:higher-genus-differentials
conv:hms-levels
conv:proof-architecture
conv:regime-tags
cor:bar-cohomology-koszul-dual
codex
The first pass on label checks was garbage because the shell mangled the label list. I’m rerunning it properly with a line-safe loop; I’m not going to trust a broken scan.
exec
/bin/zsh -lc "perl -ne 'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/higher_genus_complementarity.tex | sort -u | while IFS= read -r label; do if "'! rg -n -F "'"\\\\label{"'$label}" chapters appendices metadata >/dev/null; then echo "MISSING $label"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 3.67s:
MISSING part:characteristic-datum

thinking
**Verifying characteristics**

I’m wondering if I'm truly missing some parts of the characteristic-datum. It feels a bit uncertain, so I need to double-check that to be sure. I should probably conduct a search to confirm whether that information is actually absent or if I’m just overlooking something. Let's see what I can find to clarify this! It’s always better to double-check and make sure I’m not missing key details.
codex
The reference scan surfaced one genuine missing label so far: `part:characteristic-datum`. I’m checking whether that’s a stale hardcoded part label or just renamed elsewhere.
exec
/bin/zsh -lc 'rg -n -F "subsec:genus2-complementarity-verification" chapters appendices' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\\\part\" main.tex chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "part:characteristic-datum" chapters appendices main.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/genus_expansions.tex:1676:\subsection{Genus-2 complementarity verification}\label{subsec:genus2-complementarity-verification}
chapters/connections/thqg_symplectic_polarization.tex:1916:\S\ref{subsec:genus2-complementarity-verification}
chapters/theory/higher_genus_complementarity.tex:1740:Part~\ref{part:characteristic-datum} (\S\ref{subsec:genus2-complementarity-verification}).
chapters/theory/higher_genus_complementarity.tex:2723:(\S\ref{subsec:genus2-complementarity-verification}).
 succeeded in 52ms:
main.tex:945:Part~\ref{part:characteristic-datum} develops the full nonlinear structure: the
main.tex:1073:\label{part:characteristic-datum}
main.tex:1082:Part~\ref{part:characteristic-datum} develops the full nonlinear
main.tex:1120:The commutative engine of Parts~\ref{part:bar-complex}--\ref{part:characteristic-datum} uses symmetric configurations
main.tex:1173:The constructions of Parts~\ref{part:bar-complex}--\ref{part:characteristic-datum} (the bar complex, the genus tower, the Koszul
appendices/computational_tables.tex:4:This appendix collects numerical data for the bar complexes computed in Part~\ref{part:characteristic-datum}: Kontsevich weights for the deformation quantization star product, OPE structure constants for low-rank Kac--Moody and $\mathcal{W}$-algebras, Arnold relation expansions through $n = 4$, and modular form data at genera~$1$ and~$2$.
chapters/frame/preface.tex:1267:D, H occupy Parts~\ref{part:bar-complex}--\ref{part:characteristic-datum} of the body. Every theorem is a projection
chapters/frame/heisenberg_frame.tex:4800:Part~\ref{part:characteristic-datum} extracts its nonlinear content through the shadow obstruction tower,
chapters/theory/hochschild_cohomology.tex:1711:The modular characteristic~$\kappa(\cA)$ is only the linear leading term of this structure. Part~\ref{part:characteristic-datum} extracts the full nonlinear content: the shadow obstruction tower $\kappa(\cA) \to \Delta \to \mathfrak{C} \to \mathfrak{Q} \to \cdots$, a hierarchy of finite-order invariants whose all-degree limit is the universal class~$\Theta_\cA$.
chapters/theory/koszul_pair_structure.tex:2774:The Koszul pair structure developed in this chapter (the quadratic condition, the periodicity phenomena, the level-shifting involution) provides the algebraic skeleton on which the examples of Part~\ref{part:characteristic-datum} are built. Every explicit computation there begins by verifying the Koszul condition and identifying the dual; the reward is that the three main theorems then deliver bar cohomology, spectral collapse, and complementarity without further work. The periodicity theorems, in particular, constrain the genus tower: the Hochschild cohomology ring $\mathrm{CH}^*(\cA)$ controls deformations of the bar complex at every genus, and Koszul duality exchanges the periodicity generators of $\cA$ and $\cA^!$ with a sign (Corollary~\ref{cor:hochschild-cup-exchange}).
chapters/theory/chiral_modules.tex:1471:(see Part~\ref{part:characteristic-datum} for explicit computations).
chapters/theory/chiral_modules.tex:4030:By the Drinfeld--Sokolov reduction (\cite{FF}; see Part~\ref{part:characteristic-datum}),
chapters/theory/chiral_hochschild_koszul.tex:1309:This is \emph{not} Koszul duality in the operadic sense (Remark~\ref{rem:bosonization-not-koszul}). Koszul duality preserves the dimension of the generating space: if $\mathcal{A}$ has generators in a space $V$, then $\mathcal{A}^!$ has generators in $V^*$, so $\dim V = \dim V^*$. Here $\mathcal{B}$ has one generator ($\alpha$) while $\mathcal{F}$ has two generators ($\psi, \psi^*$). The Heisenberg algebra is \emph{not} Koszul self-dual: $\mathcal{H}_\kappa^! \simeq \mathrm{Sym}^{ch}(V^*)$, a commutative chiral algebra (Part~\ref{part:characteristic-datum}, the characteristic datum). The boson-fermion correspondence is instead a lattice VOA extension: the vertex operators $\psi = {:}e^{i\phi}{:}$ and $\psi^* = {:}e^{-i\phi}{:}$ lie in $V_{\mathbb{Z}}$, not in the Heisenberg subalgebra.
chapters/theory/chiral_hochschild_koszul.tex:1351:This is the divided power coalgebra $\Gamma(V^*)$, which is the Koszul dual \emph{coalgebra}. Its linear dual is the symmetric algebra $\mathrm{Sym}(V)$, and the Koszul dual \emph{algebra} is $\mathcal{H}_\kappa^! \simeq \mathrm{Sym}^{\mathrm{ch}}(V^*)$ (Part~\ref{part:characteristic-datum}, the characteristic datum), confirming that the Heisenberg algebra is Koszul (Theorem~\ref{thm:km-chiral-koszul}) but \emph{not} Koszul self-dual. (The cobar $\Omega(\bar{B}(\mathcal{H}_\kappa))$ recovers $\mathcal{H}_\kappa$ itself.)
chapters/theory/quantum_corrections.tex:367:The $A_\infty$ structure is strict: $m_0 = 0$ (uncurved, so $m_1^2 = 0$), $m_2$ is the standard product, and $m_n = 0$ for $n \geq 3$. The genus-$g$ corrections for $g \geq 1$ enter not through higher $m_n$ but through the curvature $m_0^{(g)} = \kappa(\mathcal{H}_\kappa) \cdot \lambda_g$ and the cohomology of $\overline{\mathcal{M}}_g$ (cf.\ Part~\ref{part:characteristic-datum}).
chapters/theory/quantum_corrections.tex:756:computed in Part~\ref{part:characteristic-datum} via the Laplace transform of the
chapters/theory/quantum_corrections.tex:798: kernel $r(z)$ computed in Part~\ref{part:characteristic-datum} for each standard family is the
chapters/theory/higher_genus_foundations.tex:6034:in the example chapters of Part~\ref{part:characteristic-datum}, extend this table into a
chapters/theory/higher_genus_foundations.tex:6859:propagator analysis in Part~\ref{part:characteristic-datum}.
chapters/theory/poincare_duality_quantum.tex:187:$-k \cdot \omega_X$ (Part~\ref{part:characteristic-datum}). This is \emph{not} the same as
 succeeded in 52ms:
main.tex:866:\part*{Overture}
main.tex:894:\part{The Bar Complex}
main.tex:1072:\part{The Characteristic Datum}
main.tex:1163:\part{The Standard Landscape}
main.tex:1367:\part{Physics Bridges}
main.tex:1373:$\bar\partial$-operator, and the Kontsevich configuration-space
main.tex:1449:\part{The Seven Faces of the Collision Residue}
main.tex:1482:\part{The Frontier}
chapters/examples/deformation_quantization.tex:79:where $\phi_{1f} = \arg(f - z_1)$ and $\phi_{1g} = \arg(g - z_1)$ are the angles from the internal vertex $z_1 \in \mathbb{H}$ to the boundary points. The bidifferential operator is $B_\Gamma(f,g) = \pi^{ij}\partial_i f \cdot \partial_j g = \{f, g\}$, giving:
chapters/examples/deformation_quantization.tex:85:The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
chapters/examples/deformation_quantization.tex:195:\[B_\Gamma(a,b) = \prod_{v \in V(\Gamma)} \left(\pi_v^{i_v j_v} \frac{\partial}{\partial z_i} \frac{\partial}{\partial w_j}\right) (a(z_v) \otimes b(w_v))\]
chapters/examples/deformation_quantization.tex:231:with $|S| \geq 2$; each stratum $\partial_S$ is a product of lower
chapters/examples/deformation_quantization.tex:234:\partial_S \overline{C}_n^{\text{ch}}(X) \;\cong\;
chapters/examples/deformation_quantization.tex:238:= \sum_S \int_{\partial_S} (\cdots)$. Each boundary contribution
chapters/examples/deformation_quantization.tex:239:$\int_{\partial_S}$ factors as a product of lower-order weights, and the
chapters/examples/deformation_quantization.tex:306:\[B_{\Gamma_1}(a,b) = \pi^{ij} \pi^{kl} \frac{\partial^2 a}{\partial x^i \partial x^k} \frac{\partial^2 b}{\partial x^j \partial x^l}\]
chapters/examples/deformation_quantization.tex:320:\[B_{\Gamma_2}(a,b) = \pi^{ij} (\partial_j\pi^{kl})\, \partial_i\partial_k a \cdot \partial_l b\]
chapters/examples/deformation_quantization.tex:326:\[B_{\Gamma_3}(a,b) = \pi^{ij} (\partial_j\pi^{kl})\, \partial_k a \cdot \partial_i\partial_l b\]
chapters/examples/deformation_quantization.tex:333:This matches the standard Kontsevich formula: the $1/8$ coefficient for the double-Poisson graph and $1/12$ for the $\partial\pi$ graphs (cf.\ the explicit second-order computation below).
chapters/examples/deformation_quantization.tex:337:\[a \star b = ab + \frac{\hbar}{2}\{a,b\} + \hbar^2\!\left(\frac{1}{8}\pi^{ij}\pi^{kl}\partial_i\partial_k a\,\partial_j\partial_l b + \frac{1}{12}\pi^{ij}(\partial_j\pi^{kl})(\partial_i\partial_k a\,\partial_l b - \partial_k a\,\partial_i\partial_l b)\right) + O(\hbar^3)\]

thinking
**Reviewing theorem labels**

I noticed there's an interesting label in main.tex, but it only scans chapters, so it’s not an issue to address. I should check if the theorem surface is using any missing labels, maybe just the main label. I’ll inspect theorem `prop:ptvv-lagrangian` at line 2030 since an earlier remark at line 595 cites it. Also, I’ll look closely at lines 1898-2010 for conditional theorem C2 because user wants all objects defined before theorem statements. Time to review C2 specifically!
codex
I’ve covered `C0` and `C1`. I’m reading the actual `C2` theorem now, not just the chapter opening summary, because the conditional upgrade is exactly where undeclared tangent-complex and shifted-symplectic objects tend to leak in.
exec
/bin/zsh -lc "rg -n -F \"\\chi_g\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1896,2068p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Ambient complementarity datum" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"formal moduli problem\" chapters/theory/higher_genus_complementarity.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1951: \chi_g \colon L_g \xrightarrow{\;\sim\;} \mathbf{C}_g(\cA)
1999:Assume $g \geq 1$ and that the comparison map~$\chi_g$ from the
2000:statement exists. Because~$\chi_g$ intertwines the involutions and the
2005:Lagrangians. Pulling that structure back along~$\chi_g$ shows that
 succeeded in 54ms:
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
  1914	curve $X$.
  1915	\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 53ms:
4574:\begin{definition}[Ambient complementarity datum]
 succeeded in 50ms:
1938: \cite{Pridham17}, the formal moduli problem
1965:associated bivector field on the formal moduli problem has degree~$-1$.
2024:$(-1)$-shifted symplectic formal moduli problem $\mathrm{MC}(L_g)$
4678:formal moduli problem $\mathcal{M}_{\mathrm{comp}}(\cA)$ carrying
4704:formal moduli problem $\mathcal{M}_\fg$
4707:the formal moduli problem $\mathcal{M}_{\mathrm{comp}}(\cA)$.
4725:integrate to Lagrangian maps of formal moduli problems.
4967:Assume the ambient complementarity formal moduli problem exists.
5027:Assume the ambient complementarity formal moduli problem exists.





thinking
**Clarifying theorem presentation**

I need to decide whether to move the theorem statement before or after the requisite definitions. In the audit, we can suggest precise fixes, even if they are extensive. I should also check if the C0 theorem statement applies `\mathcal{Z}_{\cA}` and claims local systems/sheaves on \overline M_g. Since local systems exist only on the smooth locus, we need to verify details about constructible sheaves on the compactification. I found that the exact fix involves clarifying the notation used for the object type.
thinking
**Reviewing theorem lines**

I need to check if the theorem in lines 522-526 refers to `\overline{\mathcal M}_0` instead of `\overline{\mathcal M}_{0,0}`. In DM moduli, there isn't a stable genus 0 curve without marks, though people occasionally use points by convention, which could be tricky. I should search for `\overline{\mathcal M}_0 = pt` in line 1720, as that seems mathematically sloppy. It's important to ensure clarity on moduli without conflicting conventions. User wants an audit of higher genus complementarity, so I’ll consider whether to include this in the review.
thinking
**Evaluating theoretical assumptions**

I see a potential issue on line 45 regarding the "modular pre-Koszul datum with finite-dimensional fiber cohomology." The theorem C0 is assuming that the relative bar family's perfectness is guaranteed because of the perfectness stated in Lemma. However, I wonder if that’s truly the case. It's important to ensure that all assumptions are robust so the conclusions drawn from those theorems remain valid. I'll need to double-check this detail.
thinking
**Evaluating theorem assumptions**

I'm noticing that the C0 theorem on line 360 assumes a modular pre-Koszul datum. However, the C1 theorem moves away from that assumption and just references a chiral Koszul pair on a smooth projective curve. This is kind of intriguing because it seems like there's a hidden hypothesis there, which makes me wonder what the implications are for the conclusions drawn in the context of theorems.
thinking
**Searching for definitions**

I'm looking into what a "chiral Koszul pair" entails and whether it relates to a higher-genus tower. It seems like the definition might specifically refer to genus-zero cases only. I need to inspect this briefly and gather more information to clarify what lines define it. Let’s see if I can find a strong, clear explanation to work from!
codex
I found a more structural problem: `C0` assumes a modular pre-Koszul datum, but `C1` appears to drop that and only says “chiral Koszul pair,” even though the proof keeps using genus-g bar families and moduli-space objects. I’m checking the actual definition of `chiral Koszul pair` now to see whether the theorem statement is missing a higher-genus hypothesis.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\label{def:chiral-koszul-pair}\" chapters/theory chapters/examples appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '458,530p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\chapter{Chiral Koszul duality}
     2	\label{chap:koszul-pairs}
     3	
     4	\index{chiral Koszul duality|textbf}
     5	\index{twisting morphism!chiral|textbf}
     6	\index{Francis--Gaitsgory|textbf}
     7	
     8	Classical Koszul duality, in the sense of
     9	Priddy~\cite{Priddy70} and
    10	Beilinson--Ginzburg--Soergel~\cite{BGS96}, works for graded
    11	algebras over a field: the bar complex is a tensor coalgebra on a
    12	finite-dimensional vector space, the cobar functor inverts it
    13	when bar cohomology is concentrated in degree one, and the
    14	duality exchanges quadratic algebras with quadratic coalgebras.
    15	Three features of chiral algebras on algebraic curves defeat
    16	this framework simultaneously. First, chiral algebras are
    17	\emph{curved}: the bar differential on the genus expansion
    18	satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
    19	rather than $d^2 = 0$, so the classical bar-cobar adjunction,
    20	which requires strict nilpotence, does not apply beyond genus
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:625:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
 succeeded in 52ms:
   458	\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
   459	\label{thm:quantum-complementarity-main}
   460	\label{thm:quantum-complementarity}
   461	\index{deformation-obstruction complementarity|textbf}
   462	\index{Lagrangian!complementarity|textbf}
   463	\textup{[}Regime: curved-central
   464	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   465	
   466	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
   467	curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
   468	the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
   469	its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
   470	Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
   471	for the ambient complex and homotopy eigenspaces of
   472	Definition~\textup{\ref{def:complementarity-complexes}}.
   473	
   474	\smallskip\noindent
   475	\textbf{H-level \textup{(}homotopy\textup{)}.}
   476	For each genus $g \geq 0$:
   477	\begin{enumerate}[label=\textup{(\roman*)}]

thinking
**Investigating chiral Koszul pairs**

I'm trying to define chiral Koszul pairs, and I'm thinking they likely belong to a genus-zero classification. I need to inspect around line 625 to confirm whether the definition includes higher-genus cases. It feels important to clarify this point, as it could influence my understanding. Let’s dive in and see what the analysis around that line reveals about the presence of higher-genus aspects!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '625,700p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   625	\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
   626	\index{Koszul pair!chiral|textbf}
   627	A \emph{chiral Koszul pair} on a smooth projective curve~$X$
   628	is a pair of chiral Koszul data
   629	\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
   630	Definition~\textup{\ref{def:chiral-koszul-morphism})}
   631	\[
   632	(\cA_1, \cC_1, \tau_1, F_\bullet), \qquad
   633	(\cA_2, \cC_2, \tau_2, F_\bullet)
   634	\]
   635	equipped with Verdier-compatible factorization-algebra
   636	identifications
   637	\[
   638	\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \Omega_X(\cC_2),
   639	\qquad
   640	\mathbb{D}_{\operatorname{Ran}}(\cC_2) \simeq \Omega_X(\cC_1),
   641	\]
   642	compatible with the twisting morphisms and filtrations.
   643	In this situation we write $\cA_2 \simeq \cA_1^!$ and
   644	$\cA_1 \simeq \cA_2^!$.


thinking
**Evaluating chapter opening clarity**

I see a potential issue: the line mentions "For every chiral algebra A carrying a modular pre-Koszul datum with finite-dimensional fiber cohomology," which seems okay. However, "Z_A" is undefined, which is problematic. Maybe it should say "for every chiral algebra A that carries..." instead. I think I should check for consistency between `Z(\cA)` and `\mathcal Z(\cA)`, as that could clarify some points. There's definitely more to explore here!
thinking
**Fixing theorem notation**

I need to search for all occurrences related to the theorem definitions, focusing particularly on the key lines 136-149 and theorems 1257/1267. The opening may misstate the ambient object, but line 505 does use \mathcal Z(\cA) correctly. I'm thinking about replacing every instance of `H^*(..., Z(\cA))` with `H^*(..., \mathcal Z(\cA))`. If a constant center is intended, I should use `Z(\cA)\otimes H^*(...)` and clarify that. Line 1267 also needs adjustment.
codex
I found an object-conflation bug, not just a notation preference: this file repeatedly takes cohomology of `Z(\mathcal A)` instead of the center local system `\mathcal Z(\mathcal A)`. That makes the theorem lane ill-typed. I’m enumerating all occurrences on the complementarity surface so the fix can be exact, not hand-wavy.
exec
/bin/zsh -lc 'rg -n -F "H''^*('"\\overline{\\mathcal{M}}_g, Z(\\mathcal\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1267:\rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
1339:\rho(z): H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) \to
1340:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))
1452:\sigma: H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) \xrightarrow{\sim}
1453:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))
1538:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) =
1539:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^+ \oplus
1540:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^-
1542:where $H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^\pm = \ker(\sigma \mp
1545:Q_g(\mathcal{A}) &= H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^+\\
1546:Q_g(\mathcal{A}^!) &= H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))^-
1552:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$, the eigenvalues of $\sigma$ are
1708:$V = H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$, the minimal polynomial of
2248:Q_g(\mathcal{A}^!) \cong \left(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(
2260:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!)
2265:Q_g(\mathcal{A}^!) = H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) / Q_g(\mathcal{A})
2276:The algorithm is: compute $H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))$, compute $Q_g(\mathcal{A})$ via the bar spectral sequence, and take the Verdier-orthogonal complement.
2285:Q_g(\mathcal{A}^!) \cong H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))
2290:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = 0
2298:H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!)
exec
/bin/zsh -lc 'rg -n -F "H''^*('"\\overline{\\mathcal{M}}_g, Z(\\cA\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
149:theorem identifies $H^*(\overline{\mathcal{M}}_g, Z(\cA))$ as the
2334:\;=\; \tfrac{1}{2}\,\dim H^*(\overline{\mathcal{M}}_g, Z(\cA))
2336:In particular, $\dim H^*(\overline{\mathcal{M}}_g, Z(\cA))$ is even
2353:= \dim H^*(\overline{\mathcal{M}}_g, Z(\cA))
2356:\dim H^*(\overline{\mathcal{M}}_g, Z(\cA))$.
2381:$H^*(\overline{\mathcal{M}}_g, Z(\cA))
4530:$Q_g(\cA) \oplus Q_g(\cA^!) \cong H^*(\overline{\mathcal{M}}_g, Z(\cA))$.
4549:$H^*(\overline{\mathcal{M}}_g, Z(\cA))








thinking
**Examining object dependencies**

I need to check if any of these references depend on later-defined objects or mislabels. For example, lines 819-821 in quantum-ss-convergence use `Lemma\ref{lem:fiber-cohomology-center}`, which appears later—acceptable because it’s in the same proof. However, `Theorem\ref{thm:ss-quantum}` is stated in Step 8 before Step 4. It raises suspicions due to the proof line's assertion about the fibration. I'll need to examine these details carefully because they’re subtle but significant.
thinking
**Analyzing genus filtration**

In theorem ss-quantum, I'm looking at line 708, which discusses the genus filtration on \bar B(\mathcal A). In lines 731-744, it states that "for each genus g, the Leray spectral sequence for the fibration converges to H^{p+q}(\bar B^{(g)}(\mathcal A))." I find it essential to consider how this genus filtration functions and whether the spectral sequence's convergence makes sense in this context. This seems crucial for understanding the overall theorem, so I'm paying close attention.
thinking
**Analyzing mathematical nuances**

I notice that there's a subtle issue regarding lines 819-821, which uses the lemma about fiber-cohomology-center to conclude something about local systems on a smooth locus and the constancy of the center when varying complex structure. However, that lemma itself proves constancy by asserting that OPE data doesn’t rely on the global complex structure. This leads to a deeper concern about whether we're addressing the chiral algebra on each genus-g curve or a fixed curve X.
thinking
**Examining chiral algebra definitions**

I'm exploring the definition of the relative bar fiber in line 263, which states "Let (\cA,\cA^!) be a chiral Koszul pair on X." It discusses the genus-g configuration spaces and their associated bar complex but raises questions regarding the phrasing "on the fixed curve \Sigma" when \cA is defined on X. This makes me wonder if \cA can be transported across various curves in the moduli, which seems problematic. I need to research whether \cA varies with \Sigma_g or remains fixed. This confusion is critical, especially regarding the user's question about the center local system.
thinking
**Exploring local system definitions**

In lines 576-577 of higher_genus_modular_koszul, the center local system fiber at the smooth curve Σ is described as center Z(ℵ|Σ). However, I’m questioning how ℵ|Σ is defined since ℵ was initially on X. Could X be viewed as the universal curve? That's an interesting thought. It might be a hidden aspect stemming from the factorization algebra tied to the moduli, and I'm curious to dig deeper into that connection.
thinking
**Investigating status mismatch**

I see there’s a status mismatch in the same file, and I need to investigate what's going on. My focus should be on the proposition proof that uses Lagrangian eigenspaces and the PTVV example to understand this better. It's essential to dig into these elements to clarify the situation and confirm whether everything aligns correctly. Let's take a closer look at these details to figure out the issue.
thinking
**Organizing findings**

I’m considering using a line range of `:195-197`. It probably works, although specifying “exact line” might mean I should indicate start and end points. Keeping it as a single range seems simpler. I should probably order the findings by severity, which could help in organizing them effectively. I think I need about 13 findings; it feels like a lot, but I can manage it within 50-70 lines, right?
thinking
**Evaluating findings summary**

Let’s see what I’ve read: I’ve identified 14 files and surfaces with 12 findings. So my potential summary could be, “Checked: 14 | Findings: 12 | Verdict: FAIL.” I think I should clarify that “Checked” means distinct source surfaces read, ensuring it doesn’t exceed 70 lines. If each finding takes one to two lines, then I could aim for a concise summary of about 26 lines. I might also consider merging some findings to keep it succinct.
codex
- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:466-472` — PROBLEM: `C1` only assumes a “chiral Koszul pair,” but the theorem immediately uses `\mathbf C_g`, `\mathbf Q_g`, and genus-$g$ bar data; the underlying definition of `chiral Koszul pair` in `chapters/theory/chiral_koszul_pairs.tex:625-682` does not provide a genus tower or center local system. FIX: strengthen the hypothesis to “a chiral Koszul pair carrying a modular pre-Koszul datum in the sense of Definition~\ref{def:modular-koszul-chiral},” and propagate that stronger hypothesis to the C0/C1/C2 summary and to `thm:shifted-symplectic-complementarity`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:195-197` — PROBLEM: Definition~\ref{def:complementarity-complexes} claims the Verdier involution `\sigma` acts on `\mathbf C_g(\cA)` by citing `thm:verdier-bar-cobar`, but the cited theorem in `chapters/theory/cobar_construction.tex:1312-1349` is a genus-0 bar/cobar Verdier pairing, not an involution on `R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\cA))`. FIX: remove the claim from this definition and either construct `\sigma` in a new lemma before line 186, or move the definition of `\mathbf Q_g,Q_g` to after a correct construction of `\sigma` and cite that lemma instead.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:738-744` — PROBLEM: the proof of `thm:ss-quantum` applies Leray to the product `\overline C_n(X)\times\overline{\mathcal M}_g\to\overline{\mathcal M}_g`, which is not the relative genus-$g$ configuration-space family; this trivializes the very moduli variation the theorem is supposed to capture. FIX: replace that display by the actual family `\pi_g:\mathcal C_g(\cA)\to\overline{\mathcal M}_g` from Definition~\ref{def:relative-bar-fiber}, and rewrite the spectral sequence as `E_2^{p,q}=H^p(\overline{\mathcal M}_g,R^q\pi_{g*}\bar B^{(g)}(\cA))`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:414-419` — PROBLEM: the C0 proof identifies the surviving fiber cohomology with the center by citing `cor:bar-cohomology-koszul-dual`, but that corollary in `chapters/theory/chiral_koszul_pairs.tex:924-948` only identifies bar cohomology with the Koszul dual coalgebra, not with centers. FIX: move `lem:fiber-cohomology-center` (currently at lines 906-1041) before `thm:fiber-center-identification` and cite that lemma here; delete the bogus appeal to `cor:bar-cohomology-koszul-dual`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:72-98` — PROBLEM: the chapter opening says C2 is conditional only on perfectness and nondegeneracy, but the actual theorem at lines 1898-1956 also assumes the BV package (`thm:config-space-bv`, `thm:bv-functor`) and an extra comparison quasi-isomorphism `\chi_g`; later, Proposition~\ref{prop:ptvv-lagrangian} proves an unconditional ambient PTVV statement. FIX: split C2 into two named pieces: an unconditional ambient PTVV/linear statement and a conditional bar-side BV lift, then rewrite lines 72-98 and 90-99 so the hypotheses match the actual results.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1267` — PROBLEM: the theorem lane repeatedly takes cohomology of `Z(\mathcal A)` instead of the center local system `\mathcal Z(\mathcal A)` (`1267`, `1339-1340`, `1452-1453`, `1538-1546`, `1708`); that is an object-conflation error, not harmless notation. FIX: replace every `H^*(\overline{\mathcal M}_g, Z(\mathcal A))`/`H^*(\overline{\mathcal M}_g, Z(\cA))` on the complementarity surface with `H^*(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))`/`\mathcal Z(\cA)`, and reserve `Z(\mathcal A)` for the fiberwise center only.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:149,194,375` — PROBLEM: the center local system is never actually defined in this file before it is used; the real definition lives elsewhere (`chapters/theory/higher_genus_modular_koszul.tex:575-577`). The theorem surface just says “where `\mathcal Z(\cA)` is the center local system.” FIX: insert a local definition before Definition~\ref{def:complementarity-complexes}: define `\mathcal Z_\cA` as the constructible sheaf on `\overline{\mathcal M}_g` whose restriction to `\mathcal M_g` has fiber `Z(\cA|_\Sigma)` at `[\Sigma]`, set `\mathcal Z(\cA):=\mathcal Z_\cA`, and use that notation consistently.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:374-375` — PROBLEM: C0 concludes “as local systems/sheaves on `\overline{\mathcal M}_g`,” which is category-level evasion; later the file itself says the boundary extension is only constructible (`815-829`). FIX: replace the conclusion by “as constructible sheaves on `\overline{\mathcal M}_g`, and as local systems on the smooth locus `\mathcal M_g`,” and define the intended boundary extension functor (`j_*`, `j_!`, or `j_{!*}`).

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:29-31` — PROBLEM: the scalar complementarity slogan `\kappa(\cA)+\kappa(\cA^!)=K` uses `K` before it is defined; the same defect recurs at `448-450` with `\varrho\cdot K`. The actual family-by-family definition only appears much later (`2812-2868`) and in `chapters/examples/genus_expansions.tex:3087-3104`. FIX: either define `K` immediately at first use as the family-dependent complementarity constant and forward-reference Proposition~\ref{prop:complementarity-landscape}, or remove the symbolic shorthand from the opening prose.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:42-89` — PROBLEM: the C0/C1/C2 summary uses undeclared objects before the chapter has defined them: `\mathcal Z_\cA`, `Q_g(\cA)`, `Q_g(\cA^!)`, `\mathbf C_g(\cA)`, `\mathbf Q_g(\cA)`, `\sigma`, and the Verdier pairing all appear before the notation is stabilized. FIX: either move the repaired notation block before this summary, or rewrite the summary in prose without symbols and introduce the formal objects only afterward.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:875,205-210` — PROBLEM: `Q_g(\mathcal A)` is defined twice with different meanings: first as the genus-graded piece `\operatorname{gr}^g H^*(\bar B(\mathcal A))`, later as `H^*(\mathbf Q_g(\cA))`, the `+1` eigenspace cohomology. The file later wants them equal, but it first makes them ambiguous. FIX: rename the spectral-sequence object to `Q_g^{\mathrm{ss}}(\mathcal A)` or leave it as `\operatorname{gr}^g H^*(\bar B(\mathcal A))`, reserve `Q_g(\cA)` for the eigenspace object, and add an explicit identification lemma.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:458-528` — PROBLEM: “Lagrangian polarization” is used in the theorem title and statement before this file defines what “Lagrangian” means in the linear pairing setting; the first actual definition appears only later at `2059-2068`, and that one is specifically PTVV-flavored. FIX: insert a definition immediately before `thm:quantum-complementarity-main` stating that for a non-degenerate degree-`d` pairing on `V`, a decomposition `V=L\oplus L'` is Lagrangian iff the pairing vanishes on `L` and `L'` and the induced cross-pairing `L\otimes L'→k[d]` is perfect.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:1838-1841` — PROBLEM: `prop:lagrangian-eigenspaces` cites “Theorem~\ref{thm:quantum-complementarity-main}, Step~7” for the isomorphism `\mathcal Z(\cA^!)\cong\mathcal Z(\cA)`, but Step 7 is the Kodaira–Spencer map, not the center-isomorphism argument; the relevant local argument is the sublemma at `1481-1506`. FIX: extract `lem:center-isomorphism` out of the proof into a standalone lemma before Proposition~\ref{prop:lagrangian-eigenspaces}, then change the citation at line 1841 to that lemma.

## Summary
Checked: 14 | Findings: 12 | Verdict: FAIL
tokens used
168,126
