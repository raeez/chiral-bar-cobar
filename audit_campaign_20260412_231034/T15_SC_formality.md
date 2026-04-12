# T15_SC_formality (651s, gpt-5.4)

- [CRITICAL] [chapters/theory/chiral_koszul_pairs.tex:2539](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2539) — The converse proof is not valid on its stated domain. Here `SC-formal` means `m_k^{\mathrm{SC}}=0` for all `k>=3` ([chiral_koszul_pairs.tex:2525](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2525)), but the proof then treats every standard-landscape algebra as having a current-algebra bracket and an invariant bilinear form `C(x,y,z)=\kappa(x,[y,z])`, and cites `thm:modular-characteristic` for nondegeneracy. That theorem only defines the scalar `\kappa(\cA)\in\mathbb C` ([higher_genus_modular_koszul.tex:2627](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2627)), not a bilinear form; meanwhile the same manuscript says `\beta\gamma` has “no metric, no Sugawara construction, no Casimir tensor” ([preface.tex:2932](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2932)). The step `S_3=0 => [y,z]=0` is therefore unsupported and object-conflating.

- [CRITICAL] [chapters/theory/chiral_koszul_pairs.tex:2532](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2532) — The forward implication is outsourced to `prop:swiss-cheese-nonformality-by-class`, but that dependency only proves the Heisenberg case and conflicts with the manuscript’s own class data. Its table puts only Heisenberg in class `G` and even places “lattice VOA” in class `L` ([chiral_koszul_pairs.tex:2434](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2434)), while the shadow-archetype theorem puts lattice VOAs and free fermions in class `G` ([higher_genus_modular_koszul.tex:16402](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16402)); see also [lattice_foundations.tex:1677](/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1677) and [free_fields.tex:209](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:209). As written, `class G => SC-formal` is not proved for the full class-`G` surface being claimed.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:16653](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16653) — A nearby remark says vanishing of `m_3^{\mathrm{SC}}` separates class `G` from `{L,C,M}`, but the very next classification table says class `C` has `m_3^{\mathrm{SC}}=0` and `m_4^{\mathrm{SC}}\neq0` ([higher_genus_modular_koszul.tex:16702](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16702)); the local table in [chiral_koszul_pairs.tex:2444](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2444) says the same. So the manuscript itself supplies a counterexample (`\beta\gamma`) to the claim that cubic vanishing isolates class `G`.

- [HIGH] [chapters/theory/en_koszul_duality.tex:3170](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3170) — Downstream propagation is contradictory. This chapter states “For class `G` and `L` algebras (SC-formal: `m_k^{\mathrm{SC}}=0` for `k>=3`)...”, which directly contradicts the audited proposition ([chiral_koszul_pairs.tex:2525](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2525)) and the concordance summary ([concordance.tex:7073](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7073), [concordance.tex:9647](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:9647)). The claim surface is not stable across the volume.

- [MEDIUM] [chapters/theory/chiral_koszul_pairs.tex:2525](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2525) — The scope term “standard landscape” is not locked. One definition uses Heisenberg, affine KM at non-critical level, `\mathcal W` at generic central charge, and `\beta\gamma/bc` ([higher_genus_foundations.tex:896](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:896)); the preface class table includes free fermion in class `G` ([preface.tex:2556](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2556)); and the perfectness corollary adds the extra qualifier “non-critical, non-degenerate levels” ([bar_cobar_adjunction_inversion.tex:3029](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3029)). The theorem relies on these hidden qualifications but does not state them.

## Summary
Instances checked: 16 | Violations found: 5 | Verdict: FAIL


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
session id: 019d8388-3466-7663-9a49-21c66d619944
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


MISSION: FALSIFY the proof of SC-formality: A is SC-formal iff class G. Check: (a) is this an iff? (b) is the proof complete in both directions? (c) what exactly is SC-formality?

Search the chapters/ directory for the theorem. Read the full statement AND proof.
For EACH step of the proof:
1. Does this step follow logically from previous steps?
2. Are all cited lemmas/propositions actually proved?
3. Is the scope correct (genus, level, type, family)?
4. Are there hidden assumptions?
5. Could a counterexample exist at boundary values?

Look for: circular reasoning, scope inflation, missing hypotheses, conflation of distinct objects, convention errors, status inflation.
mcp startup: no servers
codex
Using `deep-beilinson-audit` for this turn. I’m locating the SC-formality claim surface first, then I’ll read the exact theorem statement, proof, and cited dependencies before judging whether the `iff` is actually supported.
Plan update
  → Read audit workflow and repo-wide claim-status context relevant to SC-formality
  • Locate the SC-formality theorem, definition, and proof surface in chapters/
  • Trace every cited dependency and verify each proof step, scope, and boundary case
  • Re-verify findings against file contents and produce severity-ordered report
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 succeeded in 51ms:
Total output lines: 220

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
**Searching for the theorem**

I’ve loaded the initial readings, and now I need to locate the theorem. I’m considering using an explorer tool to help with that. I already read some parts, but I want to dig into codebase questions specifically regarding SC-formality. I think it would be useful to spawn an explorer to search for chapters with terms like "SC-formal," "class G," and specific theorem labels. I need to focus on reading without making any edits.
codex
I’ve loaded the repo-wide claim-status context. Next I’m fixing the exact audit surface: the definition of `SC-formality`, the theorem that states `SC-formal iff class G`, and every dependency actually used in its proof.
collab spawn_agent(call_LpFTdqco6JAXSJYZWIV6ztOz, prompt="Locate the exact claim surface in /Users/raeez/chiral-bar-cobar for the statement 'A is SC-formal iff class G' or equiva…")
mcp startup: no servers
spawn_agent(call_LpFTdqco6JAXSJYZWIV6ztOz, prompt="Locate the exact claim surface in /Users/raeez/chiral-bar-cobar for the statement 'A is SC-formal iff class G' or equiva…") pending init:
  agent: 019d8388-9549-7651-a4af-427231f754d7
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "SC-formal" -n "class G" chapters -n' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: class G: No such file or directory (os error 2)
chapters/connections/concordance.tex:7074: & SC-formality characterises class~$\mathbf{G}$:
chapters/connections/concordance.tex:9647:& SC-formality $\iff$ class~$\mathbf{G}$
chapters/frame/preface.tex:2606:a chiral algebra in the standard landscape is SC-formal if and
chapters/frame/heisenberg_frame.tex:110:shadow depth~$2$, tower terminates, SC-formal. The bar construction
chapters/theory/e1_modular_koszul.tex:1195:\item \emph{SC-formality.} The Swiss-cheese type
chapters/theory/en_koszul_duality.tex:3171:and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
chapters/theory/chiral_koszul_pairs.tex:86:(Heisenberg and its relatives) is SC-formal
chapters/theory/chiral_koszul_pairs.tex:2511:relationship between SC-formality and the classification is
chapters/theory/chiral_koszul_pairs.tex:2515:algebra outside class~$G$ can be SC-formal. The answer
chapters/theory/chiral_koszul_pairs.tex:2521:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:2524:\index{class G@class~$G$!characterised by SC-formality}
chapters/theory/chiral_koszul_pairs.tex:2533:SC-formal\textup{)} is established in
chapters/theory/chiral_koszul_pairs.tex:2539:For the converse, suppose~$\cA$ is SC-formal.
chapters/theory/chiral_koszul_pairs.tex:2548: \text{SC-formal}
chapters/theory/chiral_koszul_pairs.tex:2571:brackets; SC-formality is incompatible with each. The only

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Swiss-cheese" -n "class G" chapters' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: class G: No such file or directory (os error 2)
chapters/examples/yangians_foundations.tex:989:closest existing work is the Swiss-cheese operad
chapters/examples/kac_moody.tex:5200:\index{Swiss-cheese!critical level deformation}
chapters/examples/kac_moody.tex:5203:governing the chiral Swiss-cheese pair
chapters/examples/toroidal_elliptic.tex:4426:interacting CFT, has non-formal Swiss-cheese structure
chapters/examples/w_algebras.tex:7036:Swiss-cheese operations, but
chapters/frame/preface_sections10_13_draft.tex:14:The Swiss-cheese operad $\SCchtop$ encodes the interaction of these two
chapters/frame/preface_sections10_13_draft.tex:74:the holomorphic-topological operad to the classical Swiss-cheese operad,
chapters/frame/preface_sections10_13_draft.tex:100:For the Heisenberg algebra $\mathcal H_k$ in Swiss-cheese coordinates:
chapters/frame/preface_sections10_13_draft.tex:166:complexity of the Swiss-cheese operations.
chapters/frame/preface_sections10_13_draft.tex:196:The Swiss-cheese structure at genus~$0$ produces a Poisson vertex
chapters/frame/preface_sections10_13_draft.tex:588:Volume~II identifies the local composition law (the Swiss-cheese
chapters/theory/ordered_associative_chiral_kd.tex:1709:The two-coloured Swiss-cheese operad
chapters/theory/ordered_associative_chiral_kd.tex:2040:\item The Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$
chapters/frame/preface_sections2_4_draft.tex:1182:Swiss-cheese colour decomposition
chapters/frame/preface.tex:32:Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$. Each operad
chapters/frame/preface.tex:2108:Swiss-cheese colour decomposition
chapters/frame/preface.tex:2570:A chirally Koszul algebra is Swiss-cheese formal if and only if
chapters/frame/preface.tex:2573:of all Swiss-cheese higher operations $m_k^{\mathrm{SC}}$ for
chapters/frame/preface.tex:2604:The Swiss-cheese formality condition ($m_k^{\mathrm{SC}}=0$ for
thinking
**Waiting for results**

While I can run rg myself, it seems smart to wait for the explorer's results first to avoid overlaps. The instructions say to ask explorers first and not re-read or re-search what they cover, so I'll refrain from doing that. I wonder if I should inspect the theorem_registry with rg, but that might overlap with what the explorer covers too. For now, waiting seems to be the best plan.
collab wait(call_x9871YkSQ99g2DKGcMZuMKDN)
  receivers: 019d8388-9549-7651-a4af-427231f754d7
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2500,2595p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
sharper than the table suggests. The forward direction is
clear: class~$G$ algebras have a central bracket, so all
higher SC-operations vanish. The question is whether any
algebra outside class~$G$ can be SC-formal. The answer
is no, and the proof is a three-line forced march: the
nondegeneracy of the invariant form turns vanishing of the
cubic shadow into vanishing of the bracket itself. Of the
four classes, only Heisenberg survives.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '60,130p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
equivalent characterisations of chiral Koszulness. Ten are
unconditional: $E_2$-collapse of the bar spectral sequence,
vanishing of transferred $A_\infty$ operations $m_k$ for
$k \geq 3$, acyclicity of the twisted tensor product
$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
$\Theta_\cA^{\leq r}$, and six others. One (the Lagrangian
eigenspace decomposition) is conditional on perfectness of the
bar-cobar normal complex. One (D-module purity) is a
one-directional implication. The count is exact: $10 + 1 + 1$.

Two distinctions require emphasis. First, the four complexity
classes G/L/C/M, with shadow depths
$\{2, 3, 4, \infty\}$
(Theorem~\ref{thm:shadow-archetype-classification}), record the
degree at which the shadow obstruction tower first becomes
nontrivial; they do \emph{not} record failure of Koszulness.
Every standard chiral algebra is chirally Koszul. The classes
separate algebras by the complexity of their higher-genus
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '70,130p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    70	one-directional implication. The count is exact: $10 + 1 + 1$.
    71	
    72	Two distinctions require emphasis. First, the four complexity
    73	classes G/L/C/M, with shadow depths
    74	$\{2, 3, 4, \infty\}$
    75	(Theorem~\ref{thm:shadow-archetype-classification}), record the
    76	degree at which the shadow obstruction tower first becomes
    77	nontrivial; they do \emph{not} record failure of Koszulness.
    78	Every standard chiral algebra is chirally Koszul. The classes
    79	separate algebras by the complexity of their higher-genus
    80	behaviour, not by the validity of the duality. Second,
    81	Koszulness and SC formality are logically independent properties.
    82	Koszulness is the condition that bar cohomology is concentrated
    83	in degree one; SC formality is the condition
    84	$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
    85	bar complex. All standard families are Koszul; only class~$G$
    86	(Heisenberg and its relatives) is SC-formal
    87	(Proposition~\ref{prop:sc-formal-iff-class-g}).
    88	Confusing the two misidentifies what the shadow tower measures.
    89	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2480,2585p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2480	\end{proposition}
  2481	
  2482	\begin{proof}
  2483	Class~$G$: centrality of the Heisenberg bracket kills all nested
  2484	compositions; $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
  2485	Class~$L$: the cubic shadow
  2486	$S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
  2487	ratio (the structure constant divided by the level); the quartic
  2488	and higher shadows vanish because the Jacobi identity and rank
  2489	constraints eliminate all $\overline{\cM}_{0,r+1}$ tree sums for
  2490	$r \geq 4$ when the OPE has at most double poles.
  2491	Class~$C$: the cubic shadow vanishes by the parity obstruction on
  2492	the weight-$0$ generator~$\gamma$; the quartic contact invariant
  2493	$Q^{\mathrm{contact}}$ is nonzero by the explicit
  2494	$\beta\gamma\beta\gamma$ channel computation; termination at
  2495	depth~$4$ follows from rank-one rigidity
  2496	(Theorem~\ref{thm:riccati-algebraicity}).
  2497	Class~$M$:
  2498	$S_3 = (\text{scalar projection of } T_{(1)}T)/T_{(3)}T
  2499	= 2\kappa/\kappa = 2$, independent of~$c$;
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/connections/concordance.tex | sed -n '9600,9665p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  9600	 $+$ $1$ one-directional (D-module purity)
  9601	 \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
  9602	& Shadow obstruction tower algebraicity:
  9603	 $H(t)^2 = t^4 Q_L(t)$, tower determined by
  9604	 $(\kappa, \alpha, S_4)$
  9605	 \textup{(}Theorem~\ref{thm:riccati-algebraicity}\textup{)};
  9606	 cubic coefficient $\alpha = S_3/\kappa$ universal per family:
  9607	 $\alpha = 0$ \textup{(}Heis\textup{)},
  9608	 $\alpha = 2$ \textup{(}Vir\textup{)},
  9609	 family-specific for $\Walg_N$ and affine KM \\
  9610	& $\kappa$ formula universality: $\kappa(\cH_k) = k$,
  9611	 $\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$,
  9612	 $\kappa(\mathrm{Vir}_c) = c/2$,
  9613	 $\kappa(\Walg_N) = c(H_N{-}1)$ \\
  9614	& $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for
  9615	 uniform-weight modular Koszul algebras at all genera
  9616	 \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\
  9617	& Swiss-cheese theorem
  9618	 \textup{(}Theorem~\ref{thm:thqg-swiss-cheese}\textup{)} \\
  9619	& Chiral derived center as universal bulk \\
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/connections/concordance.tex | sed -n '7060,7085p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7060	 holographic (boundary-bulk correction)
  7061	 & bar-intrinsic MC $+$ formality identification
  7062	 $+$ derived-centre factorization \\
  7063	\ref{def:generating-depth}
  7064	 & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
  7065	 $d_{\mathrm{alg}}$: formal distinction~;
  7066	 Virasoro $d_{\mathrm{gen}} = 3$,
  7067	 $d_{\mathrm{alg}} = \infty$
  7068	 & depth decomposition $+$ class~M tower non-termination \\
  7069	\hline
  7070	\multicolumn{3}{l}{\textit{%
  7071	 April 2026 session: structural propositions and depth classification}} \\
  7072	\hline
  7073	\ref{prop:sc-formal-iff-class-g}
  7074	 & SC-formality characterises class~$\mathbf{G}$:
  7075	 $\cA$ is Swiss-cheese formal iff class~$\mathbf{G}$
  7076	 \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
  7077	 & abelian bracket $+$ nondegeneracy of~$\kappa$ \\
  7078	\ref{prop:depth-gap-trichotomy}
  7079	 & Algebraic depth gap:

thinking
**Summarizing theorem and proof locations**

I'll prepare a clear bullet list highlighting the precise file paths, line ranges, and short descriptions for the definition of SC-formality, the full theorem statement, and proof locations, as well as relevant cross-references in other files per the instructions.
codex
- `chapters/theory/chiral_koszul_pairs.tex:72-87` — SC-formality is defined as the vanishing of all higher Swiss-cheese operations ($m_k^{\mathrm{SC}}=0$ for $k\geq 3$) in the Swiss-cheese bar complex and immediately contrasted with Koszulness; the paragraph also points ahead to `prop:sc-formal-iff-class-g` as the only SC-formal family in the standard landscape.  
- `chapters/theory/chiral_koszul_pairs.tex:2521-2573` (`prop:sc-formal-iff-class-g`) — full proposition statement (“$\cA$ is Swiss-cheese formal iff $\cA$ belongs to class $G$”) lives in lines 2521‑2528, followed by the proof (lines 2531‑2573) that first recalls the class $G$ direction and then shows SC-formality forces the bracket to vanish via the cubic shadow and nondegeneracy of the invariant form.  
- `chapters/connections/concordance.tex:7073-7077` — the April 2026 structural table entry for `prop:sc-formal-iff-class-g`, describing the proposition and noting the abelian bracket/nondegenerate $\kappa$ rationale.  
- `chapters/connections/concordance.tex:9647-9648` — the concordance checklist entry reiterating “SC-formality $\iff$ class $\mathbf{G}$” and linking to the same proposition for the scanned claim surface.
wait(call_x9871YkSQ99g2DKGcMZuMKDN) 1 agents complete:
  019d8388-9549-7651-a4af-427231f754d7 completed: "- `chapters/theory/chiral_koszul_pairs.tex:72-87` — SC-formality is defined as the vanishing of all higher Swiss-cheese …"
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '40,110p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2480,2595p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7050,7090p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '9638,9652p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    40	Koszul: it does not see the genus corrections in the bar
    41	complex, and it does not detect the shadow obstruction tower
    42	whose depth varies from two to infinity across the standard
    43	families.
    44	
    45	The bar-cobar adjunction of Theorem~A
    46	(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
    47	functorial pair that resolves all three obstructions. It is the
    48	unique adjunction that (a)~inverts on the Koszul locus, producing
    49	$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
    50	(Theorem~\ref{thm:bar-cobar-inversion-qi}); (b)~intertwines
    51	Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with
    52	$\barB_X(\cA^!)$; (c)~produces Lagrangian complementarity
    53	$Q_g(\cA) \oplus Q_g(\cA^!) \simeq
    54	H^*(\overline{\mathcal{M}}_g, Z(\cA))$
    55	(Theorem~\ref{thm:quantum-complementarity-main}).
    56	No other functorial construction achieves all three: the operadic
    57	adjunction achieves (a) but not (b) or (c); Verdier duality alone
    58	achieves (b) but has no bar-cobar content; complementarity (c)
    59	requires both (a) and (b) as input.
 succeeded in 51ms:
  7050	 & three pre-existing fragments consolidated;
  7051	 quotients excluded \\
  7052	\ref{prop:d-module-purity-km-equivalence}
  7053	 & Kac--Moody equivalence via Saito--Kashiwara weight
  7054	 filtration: PBW strictness~(ii) $\iff$
  7055	 $\cD$-module purity~(xii)
  7056	 & chiral localization $+$ Hitchin VHS $+$ Saito \\
  7057	\ref{prop:shadow-tower-three-lenses}
  7058	 & Three equivalent descriptions of $S_r(\cA)$:
  7059	 algebraic (shadow), geometric (formality obstruction),
  7060	 holographic (boundary-bulk correction)
  7061	 & bar-intrinsic MC $+$ formality identification
  7062	 $+$ derived-centre factorization \\
  7063	\ref{def:generating-depth}
  7064	 & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
  7065	 $d_{\mathrm{alg}}$: formal distinction~;
  7066	 Virasoro $d_{\mathrm{gen}} = 3$,
  7067	 $d_{\mathrm{alg}} = \infty$
  7068	 & depth decomposition $+$ class~M tower non-termination \\
  7069	\hline
 succeeded in 51ms:
  2480	\end{proposition}
  2481	
  2482	\begin{proof}
  2483	Class~$G$: centrality of the Heisenberg bracket kills all nested
  2484	compositions; $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
  2485	Class~$L$: the cubic shadow
  2486	$S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
  2487	ratio (the structure constant divided by the level); the quartic
  2488	and higher shadows vanish because the Jacobi identity and rank
  2489	constraints eliminate all $\overline{\cM}_{0,r+1}$ tree sums for
  2490	$r \geq 4$ when the OPE has at most double poles.
  2491	Class~$C$: the cubic shadow vanishes by the parity obstruction on
  2492	the weight-$0$ generator~$\gamma$; the quartic contact invariant
  2493	$Q^{\mathrm{contact}}$ is nonzero by the explicit
  2494	$\beta\gamma\beta\gamma$ channel computation; termination at
  2495	depth~$4$ follows from rank-one rigidity
  2496	(Theorem~\ref{thm:riccati-algebraicity}).
  2497	Class~$M$:
  2498	$S_3 = (\text{scalar projection of } T_{(1)}T)/T_{(3)}T
  2499	= 2\kappa/\kappa = 2$, independent of~$c$;
 succeeded in 52ms:
  9638	 imaginary quadratic for class~$\mathbf{M}$;
  9639	 trivial for class~$\mathbf{G}/\mathbf{L}$
  9640	 \textup{(}Remark~\ref{rem:shadow-field}\textup{)} \\
  9641	& Descent fan: three independent projections of
  9642	 $\Theta_\cA$ (categorical, spectral, modular)
  9643	 \textup{(}Proposition~\ref{prop:descent-fan}\textup{)} \\
  9644	& Lattice fan closure: all three projections
  9645	 compatible for lattice VOAs
  9646	 \textup{(}\S\ref{subsec:concordance-descent-fan}\textup{)} \\
  9647	& SC-formality $\iff$ class~$\mathbf{G}$
  9648	 \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)} \\
  9649	& Algebraic depth gap:
  9650	 $d_{\mathrm{alg}} \in \{0,1,2,\infty\}$
  9651	 \textup{(}Proposition~\ref{prop:depth-gap-trichotomy}\textup{)} \\
  9652	& $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level

thinking
**Investigating definitions and assumptions**

I need to look into hidden assumptions and boundary values for SC-formality. I've got a local definition at lines 81-87, but I wonder if a more formal definition exists elsewhere. Maybe I should search for "m_k^{\\mathrm{SC}}" or "Swiss-cheese formal." It might help to use an explorer tool for the dependency map. I’m considering if I should use the same explorer or spawn a new one to find labels and definitions that connect various propositions.
codex
The theorem surface is now fixed. I’m tracing the proof dependencies next, because the forward implication is outsourced and the converse leans on two fragile points: `m_3^{SC}=0 => S_3=0` and the claim that `\kappa` is nondegenerate on the whole standard landscape.
collab send_input(call_QkxKILmQLB7iWFK1p9LWsHb4, prompt="Find the precise dependency surface used by `prop:sc-formal-iff-class-g` in `chapters/theory/chiral_koszul_pairs.tex`. I…")
  receiver: 019d8388-9549-7651-a4af-427231f754d7
send_input(call_QkxKILmQLB7iWFK1p9LWsHb4, prompt="Find the precise dependency surface used by `prop:sc-formal-iff-class-g` in `chapters/theory/chiral_koszul_pairs.tex`. I…") completed: "- `chapters/theory/chiral_koszul_pairs.tex:72-87` — SC-formality is defined as the vanishing of all higher Swiss-cheese …":
  receiver: 019d8388-9549-7651-a4af-427231f754d7
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:swiss-cheese-nonformality-by-class" -n "S_3" -n "thm:modular-characteristic" -n "standard landscape" -n "shadow-archetype-classification" -n "class G" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: S_3: No such file or directory (os error 2)
rg: thm:modular-characteristic: No such file or directory (os error 2)
rg: standard landscape: No such file or directory (os error 2)
rg: shadow-archetype-classification: No such file or directory (os error 2)
rg: class G: No such file or directory (os error 2)
chapters/theory/chiral_koszul_pairs.tex:2415:\label{prop:swiss-cheese-nonformality-by-class}
chapters/theory/chiral_koszul_pairs.tex:2534:Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
chapters/theory/chiral_koszul_pairs.tex:2773:(Proposition~\ref{prop:swiss-cheese-nonformality-by-class})

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2380,2445p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2380	The W-algebra construction $\cW^k(\fg, f)$ via Drinfeld--Sokolov
  2381	reduction is the principal example where the quotient \emph{does}
  2382	preserve Koszulness, and this is a substantive theorem of the chapter
  2383	(Theorem~\ref{thm:w-algebra-koszul}), not a corollary of closure.
  2384	\end{remark}
  2385	
  2386	\begin{remark}[$A_\infty$ formality and Gaiotto--Kulp--Wu]
  2387	\label{rem:ainfty-formality-gkw}
  2388	\index{Gaiotto--Kulp--Wu!formality characterization}
  2389	The $A_\infty$ formality characterization
  2390	(item~(iii) of Theorem~\ref{thm:koszul-equivalences-meta})
  2391	is the bar-complex statement of the formality theorem of
  2392	Gaiotto--Kulp--Wu~\cite{GKW2025}: the transferred operations
  2393	$m_k = 0$ for $k \geq 3$ on bar cohomology if and only if
  2394	$\cA$ is chirally Koszul. The shadow depth classification
  2395	$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
  2396	(Remark~\ref{rem:shadow-depth-gkw-refinement}) refines their
  2397	binary formal/non-formal dichotomy into a four-class stratification
  2398	governed by the discriminant $\Delta = 8\kappa S_4$.
  2399	\end{remark}
thinking
**Considering code inspection**

I'm thinking about manually inspecting with rg if there's no overlap. Right now, the Explorer is doing a dependency search. I should check the local file context around a specific property, but I remember the instructions say not to re-read or re-search code they cover. So, it's probably best to wait for the results. Once Explorer identifies things, we will still need to look at the actual lines ourselves to ground our claims. I guess we’ll figure it out step by step!
collab wait(call_Ln0sXYWdcqQz3oBVC1f30E2U)
  receivers: 019d8388-9549-7651-a4af-427231f754d7
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2445,2505p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2445	& $\beta\gamma$
  2446	& $= 0$
  2447	& $\neq 0$
  2448	& $= 0$ \\
  2449	$M$ \textup{(}$r_{\max}=\infty$\textup{)}
  2450	& Virasoro, $\cW_N$
  2451	& $\neq 0$
  2452	& $\neq 0$
  2453	& $\neq 0\;\forall\, k$ \\
  2454	\bottomrule
  2455	\end{tabular}
  2456	\end{center}
  2457	
  2458	\medskip\noindent
  2459	\emph{Mechanism.}
  2460	For class~$G$\textup{:} the bracket $[a_m, a_n] = km\,\delta_{m+n,0}$
  2461	is central, so nested brackets
  2462	$[[a_m, a_n], a_p] = 0$ and all higher tree sums vanish.
  2463	For class~$L$\textup{:} the OPE has at most a double pole; the
  2464	three-channel tree sum over $\overline{\cM}_{0,4}$ is nonzero
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "S_3" -n "Shadow" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: Shadow: No such file or directory (os error 2)
chapters/theory/chiral_koszul_pairs.tex:2465:\textup{(}$S_3 = 2h^\vee/(k+h^\vee) \neq 0$\textup{)} but the
chapters/theory/chiral_koszul_pairs.tex:2476:\textup{(}$T_{(3)}T = c/2$\textup{)} produces $S_3 = 2$
chapters/theory/chiral_koszul_pairs.tex:2486:$S_3 = 2h^\vee/(k + h^\vee)$ is computed from the OPE coefficient
chapters/theory/chiral_koszul_pairs.tex:2498:$S_3 = (\text{scalar projection of } T_{(1)}T)/T_{(3)}T
chapters/theory/chiral_koszul_pairs.tex:2505:(three independent methods for $S_3$,
chapters/theory/chiral_koszul_pairs.tex:2540:The cubic shadow $S_3$ is the normalized projection of the
chapters/theory/chiral_koszul_pairs.tex:2552: S_3 = 0
chapters/theory/chiral_koszul_pairs.tex:2569:shadows ($S_3 = 0$) into a structural condition on the bracket
chapters/theory/chiral_koszul_pairs.tex:3346:(iii) Class~$G$: $S_3 = S_4 = 0$, so the crossing
chapters/theory/chiral_koszul_pairs.tex:3348:Class~$L$: $S_3 \neq 0$, $S_4 = 0$; one cubic crossing
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3300,3385p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3300	\index{conformal bootstrap!from Koszulness|textbf}
  3301	\index{Koszul property!bootstrap closure|textbf}
  3302	Let $\cA$ be a chirally Koszul chiral algebra. Then:
  3303	\begin{enumerate}[label=\textup{(\roman*)}]
  3304	\item The Maurer--Cartan moduli $\MC(\gAmod)$ is discrete
  3305	 \textup{(}zero-dimensional\textup{)}: the MC element
  3306	 $\Theta_\cA$ is the unique solution, determined by the
  3307	 genus-$0$ OPE data.
  3308	\item The shadow depth $r_{\max}(\cA)$ equals the bootstrap
  3309	 closure order: the number of OPE channels at which the
  3310	 crossing equation
  3311	 $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at degree
  3312	 $n = 4$ is satisfied.
  3313	\item The shadow depth classification corresponds to bootstrap
  3314	 complexity:
  3315	 class~$G$ has no OPE corrections beyond leading order,
  3316	 class~$L$ has one cubic correction
  3317	 \textup{(}the pentagon identity\textup{)},
  3318	 class~$C$ terminates at the quartic,
  3319	 class~$M$ requires the infinite tower.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"thm:modular-characteristic\" -n \"modular-characteristic\" -n \"\\label{thm:modular-characteristic}\" -n \"modular characteristic\" -n \"nondegenerate\" chapters/theory -n" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: modular-characteristic: No such file or directory (os error 2)
rg: \label{thm:modular-characteristic}: No such file or directory (os error 2)
rg: modular characteristic: No such file or directory (os error 2)
rg: nondegenerate: No such file or directory (os error 2)
chapters/theory/higher_genus_modular_koszul.tex:411:$\cW$-algebras, Theorem~\ref{thm:modular-characteristic}(iii))
chapters/theory/higher_genus_modular_koszul.tex:1442:(Theorem~\ref{thm:modular-characteristic}).
chapters/theory/higher_genus_modular_koszul.tex:1592:(Theorem~\ref{thm:modular-characteristic}).
chapters/theory/higher_genus_modular_koszul.tex:1653:(Theorem~\ref{thm:modular-characteristic}).
chapters/theory/higher_genus_modular_koszul.tex:2597:(1)~scalar: $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic}),
chapters/theory/higher_genus_modular_koszul.tex:2628:\label{thm:modular-characteristic}
chapters/theory/higher_genus_modular_koszul.tex:2864:Theorem~\ref{thm:modular-characteristic}(ii) is the exact
chapters/theory/higher_genus_modular_koszul.tex:2874:Theorem~\ref{thm:modular-characteristic}(iv) is the
chapters/theory/higher_genus_modular_koszul.tex:2888:consequence of Theorem~\ref{thm:modular-characteristic} and
chapters/theory/higher_genus_modular_koszul.tex:2897:term-by-term from Theorem~\ref{thm:modular-characteristic}.
chapters/theory/higher_genus_modular_koszul.tex:2971:(Theorem~\ref{thm:modular-characteristic}, applied to the
chapters/theory/higher_genus_modular_koszul.tex:3006:Theorem~\ref{thm:modular-characteristic}(iii). At $N = 2$
chapters/theory/higher_genus_modular_koszul.tex:3043:Theorem~\ref{thm:modular-characteristic}(iv), applied to the
chapters/theory/higher_genus_modular_koszul.tex:3739:(Theorem~\ref{thm:modular-characteristic}(iii),
chapters/theory/higher_genus_modular_koszul.tex:4482:(Theorem~\ref{thm:modular-characteristic}(iii)) for KM, and from
chapters/theory/higher_genus_modular_koszul.tex:4555:(i)~the scalar shadow $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic});
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2600,2665p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2600	(Theorem~\ref{thm:spectral-characteristic}),
  2601	exponential $=$ periodicity profile~$\Pi_{\cA}$;
  2602	(3)~shadow obstruction tower / full MC: $\Theta_{\cA}^{\leq r}$, $\Defcyc(\cA)$
  2603	(Definition~\ref{def:shadow-postnikov-tower};
  2604	Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
  2605	at scalar level),
  2606	exponential $=$ modular automorphy.
  2607	See Table~\ref{tab:master-invariants}.
  2608	\end{remark}
  2609	
  2610	\medskip
  2611	Via the Feynman transform of the Getzler--Kapranov modular operad
  2612	$\{\overline{\mathcal{M}}_{g,n}\}_{g,n}$, the genus tower
  2613	assembles into a chain-level modular functor
  2614	(Theorem~\ref{thm:chain-modular-functor}): to each surface~$\Sigma_{g,n}$ a
  2615	cochain complex $V_{g,n} = \barB^{(g)}_n(\cA)$, to each boundary
  2616	degeneration a chain map, to each consistency relation a chain
  2617	homotopy. Passing to cohomology recovers the classical
  2618	modular-functor package; for $\widehat{\fg}_k$ at integrable level, $H^0(V_{g,n})$ is the
  2619	Tsuchiya--Ueno--Yamada space of conformal blocks
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "nondeg" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
724:with modular operad operations. This depends on Theorem~A, not on Shapovalov nondegeneracy
5425:$\sigma$-stable Verdier-nondegenerate plane.
5461:$\sigma$-stable Verdier-nondegenerate plane
5784:seed-pairing matrix is chain-level nondegenerate.
21521:pairing $\eta = \langle{-},{-}\rangle|_V$ is nondegenerate.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2665,2735p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2665	 At genus~$1$ this holds unconditionally for all families;
  2666	 at genus $g \geq 2$ with multi-weight algebras, the scalar
  2667	 formula fails and a cross-channel correction
  2668	 $\delta F_g^{\mathrm{cross}}$ is required
  2669	 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
  2670	\item \emph{Duality.}
  2671	 Under Koszul duality, $\kappa$ satisfies a duality constraint:
  2672	 $\kappa(\cA) + \kappa(\cA^!) = 0$ for affine Kac--Moody and
  2673	 free-field algebras. For the principal $\mathcal{W}$-algebra
  2674	 $\mathcal{W}^k(\mathfrak{g})$ under Drinfeld--Sokolov reduction,
  2675	 $\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'}) =
  2676	 K_\fg \cdot \varrho(\fg)$
  2677	 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
  2678	 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
  2679	 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
  2680	 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
  2681	 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
  2682	 $m_1, \ldots, m_r$ the exponents;
  2683	 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
  2684	 In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '80,140p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    80	behaviour, not by the validity of the duality. Second,
    81	Koszulness and SC formality are logically independent properties.
    82	Koszulness is the condition that bar cohomology is concentrated
    83	in degree one; SC formality is the condition
    84	$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
    85	bar complex. All standard families are Koszul; only class~$G$
    86	(Heisenberg and its relatives) is SC-formal
    87	(Proposition~\ref{prop:sc-formal-iff-class-g}).
    88	Confusing the two misidentifies what the shadow tower measures.
    89	
    90	On a point, the bar complex
    91	$\barB(A) = T^c(s^{-1}\bar{A})$ is built from tensor powers of
    92	the augmentation ideal; a classical twisting morphism
    93	$\tau \colon \barB(A) \to A^!$ is a degree-$+1$ element in the
    94	convolution dg~Lie algebra satisfying $d\tau + \tau \star \tau = 0$.
    95	On a curve~$X$, the chiral twisting morphism
    96	(Definition~\ref{def:chiral-twisting-datum}) lives in the chiral
    97	convolution algebra, where the star product is mediated by the
    98	integration kernel on $X^2 \setminus \Delta$. The acyclicity of
    99	the twisted tensor product $K_\tau^L(\cA, \cC)$, the defining
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bilinear" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
315:$\mathrm{MCG}$-invariant bilinear form), and integration
4935:over~$\mathbb{C}$ with non-degenerate invariant bilinear form
6073:seed spaces $E_g$ and $E_g^!$ using the bilinear simple-pole bracket
8836:bilinear form on~$\fg$. For simple~$\fg$, Schur's lemma
23508: $2 \cdot 2^2 + 2^2 - 12 = 0$, and the bilinear coupling
25635:the Hirota bilinear residual is nonvanishing. The KdV reduction
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "def:modular-koszul-chiral" -n "modular Koszul" -n "modular Koszul chiral" -n "modular Koszul" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: modular Koszul: No such file or directory (os error 2)
rg: modular Koszul chiral: No such file or directory (os error 2)
rg: modular Koszul: No such file or directory (os error 2)
chapters/theory/higher_genus_modular_koszul.tex:426:version; Definition~\ref{def:modular-koszul-chiral} gives the concrete
chapters/theory/higher_genus_modular_koszul.tex:530:chosen model. Definition~\ref{def:modular-koszul-chiral} provides
chapters/theory/higher_genus_modular_koszul.tex:535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
chapters/theory/higher_genus_modular_koszul.tex:693:\textup{MK1--MK3} of Definition~\textup{\ref{def:modular-koszul-chiral}}.
chapters/theory/higher_genus_modular_koszul.tex:796:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
chapters/theory/higher_genus_modular_koszul.tex:924:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
chapters/theory/higher_genus_modular_koszul.tex:1222:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
chapters/theory/higher_genus_modular_koszul.tex:1399:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_modular_koszul.tex:1467:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
chapters/theory/higher_genus_modular_koszul.tex:1550:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_modular_koszul.tex:1602:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_modular_koszul.tex:1882:Definition~\textup{\ref{def:modular-koszul-chiral})} and
chapters/theory/higher_genus_modular_koszul.tex:2000:Definition~\ref{def:modular-koszul-chiral}
chapters/theory/higher_genus_modular_koszul.tex:2398:(Definition~\ref{def:modular-koszul-chiral}). The
chapters/theory/higher_genus_modular_koszul.tex:2579:Definition~\ref{def:modular-koszul-chiral} and
chapters/theory/higher_genus_modular_koszul.tex:2635:(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
chapters/theory/higher_genus_modular_koszul.tex:2846:(Definition~\ref{def:modular-koszul-chiral}) realized as the
wait(call_Ln0sXYWdcqQz3oBVC1f30E2U) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '520,620p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   520	$Q_g(\cA^!) := H^*(\mathbf{Q}_g(\cA^!))$ recover the
   521	deformation and obstruction spaces of
   522	Theorem~\ref{thm:quantum-complementarity-main}.
   523	\end{definition}
   524	
   525	\begin{remark}[Model independence]\label{rem:model-independence}
   526	Any two admissible dg presentations of the same factorization
   527	object are connected by a contractible space of quasi-isomorphisms,
   528	so the homotopy axioms \ref{MK:koszul-htpy}--\ref{MK:modular-htpy}
   529	are invariants of the factorization algebra, not of a
   530	chosen model. Definition~\ref{def:modular-koszul-chiral} provides
   531	the dg model used throughout.
   532	\end{remark}
   533	
   534	\begin{definition}[Modular pre-Koszul chiral algebra: dg model of
   535	 Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
   536	Let $X$ be a smooth projective curve over $\mathbb{C}$.
   537	A \emph{modular pre-Koszul chiral algebra} on $X$ is an augmented chiral
   538	algebra $(\cA, \varepsilon\colon \cA \to \mathcal{O}_X)$ equipped with
   539	the following data and satisfying the following axioms.
collab wait(call_1mdFiSaruaDcWeCwTttmKBhZ)
  receivers: 019d8388-9549-7651-a4af-427231f754d7
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "label{thm:quantum-complementarity-main" -n "quantum complementarity" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label{thm:quantum-complementarity-main)
             ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "quantum-complementarity-main" -n "complementarity" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: complementarity: No such file or directory (os error 2)
chapters/theory/chiral_koszul_pairs.tex:55:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/chiral_koszul_pairs.tex:110:(Theorem~\ref{thm:quantum-complementarity-main});
chapters/theory/chiral_koszul_pairs.tex:5368:(Theorem~\ref{thm:quantum-complementarity-main}) admits a
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "standard landscape" -n "Standard landscape" -n "standard families" -n "standard chiral" -n "standard chiral algebra" chapters' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: Standard landscape: No such file or directory (os error 2)
rg: standard families: No such file or directory (os error 2)
rg: standard chiral: No such file or directory (os error 2)
rg: standard chiral algebra: No such file or directory (os error 2)
chapters/examples/beta_gamma.tex:241:largest in the standard landscape at every fixed $p_{\max}$.
chapters/examples/y_algebras.tex:3:Every chiral algebra in the standard landscape inhabits a single
chapters/examples/w3_holographic_datum.tex:17:or scalar. The first algebra in the standard landscape that
chapters/examples/moonshine.tex:308:This is the only instance in the standard landscape where
chapters/examples/genus_expansions.tex:2747:full standard landscape. At genus~$1$, the formula
chapters/examples/n2_superconformal.tex:4:witness in the standard landscape that chiral Koszulness and
chapters/examples/n2_superconformal.tex:319:in the standard landscape that CE Koszulness (vanishing of
chapters/examples/bar_complex_tables.tex:3143:standard landscape. The rule ``OPE pole $z^{-n} \to$
chapters/frame/preface_sections10_13_draft.tex:345:bridge theorem, so the entire standard landscape enters through two
chapters/frame/preface_sections10_13_draft.tex:537:the standard landscape for all seven families, and the genus-$2$ and
chapters/frame/preface_sections5_9_draft.tex:350:The standard landscape partitions into four classes
chapters/frame/preface_sections5_9_draft.tex:500:Every algebra in the standard landscape is either primitive
chapters/frame/preface_sections5_9_draft.tex:510:\section*{7.\quad The standard landscape}
chapters/frame/preface_sections5_9_draft.tex:840:point). Scope: every family in the standard landscape at all
chapters/frame/preface.tex:319:(the entire standard landscape), the two theories agree; for
chapters/frame/preface.tex:1098:classifies the standard landscape into four shadow-depth classes
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "standard landscape" chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1922:give the architecture; the standard landscape (Part~\ref{part:standard-landscape},
2046:The twelve characterisations K1--K12 of Koszulness (Theorem~\ref{thm:koszul-equivalences-meta}) comprise ten unconditional equivalences, one conditional (the Lagrangian criterion, conditional on perfectness; unconditional for the standard landscape), and one one-directional ($\mathcal{D}$-module purity, with only the forward direction proved). The bifunctor decomposition theorem is a further proved consequence outside the twelve numbered items.
2088:\noindent\textbf{MC4} ($\mathcal{W}_\infty$ closure and completed bar-cobar): The completed bar-cobar problem asks whether finite-stage Koszul duality passes to inverse limits. Two complementary mechanisms cover the entire standard landscape:
2111:for the standard landscape (Theorem~\ref{thm:general-hs-sewing}):
2141:The standard landscape of Part~\ref{part:standard-landscape} is summarized in a single table recording $\kappa$, $c$, $K = c + c'$, $\Delta$, and the shadow archetype for each family.
2424: standard landscape.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
connections
examples
frame
theory
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
algebraic_foundations.aux
algebraic_foundations.tex
bar_cobar_adjunction.aux
bar_cobar_adjunction.tex
bar_cobar_adjunction_curved.tex
bar_cobar_adjunction_inversion.tex
bar_construction.aux
bar_construction.tex
chiral_center_theorem.tex
chiral_hochschild_koszul.aux
chiral_hochschild_koszul.tex
chiral_koszul_pairs.aux
chiral_koszul_pairs.tex
chiral_modules.aux
chiral_modules.tex
cobar_construction.aux
cobar_construction.tex
coderived_models.tex
computational_methods.tex
configuration_spaces.aux
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "standard landscape" chapters/theory/three_invariants.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
18:classification of the standard landscape into the four
96:pole order among that minimal set. For the standard landscape
181:For every chiral algebra $\cA$ in the standard landscape:
300:The value $k_{\max} = 2$ is absent from the standard landscape
314:For every chiral algebra $\cA$ in the standard landscape,
327:chiral algebras in the standard landscape, and $k_{\max} = p_{\max}-1$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/three_invariants.tex | sed -n '1,140p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\chapter{The three invariants of a chiral algebra}
     2	\label{ch:three-invariants}
     3	
     4	\begin{abstract}
     5	Three distinct numerical invariants of a chiral algebra~$\cA$
     6	(the \emph{generator OPE pole order}~$p_{\max}(\cA)$, the
     7	\emph{collision depth}~$k_{\max}(\cA)$, and the
     8	\emph{shadow depth}~$r_{\max}(\cA)$) measure three different
     9	structural features and need not coincide. This chapter formalizes
    10	the distinction, states the relation
    11	$k_{\max} = p_{\max} - 1$ that always holds
    12	(a consequence of the $\mathrm{d}\log$ absorption of the bar
    13	propagator, AP\textup{19}), and proves that $r_{\max}$ is independent
    14	of $p_{\max}$. The $\beta\gamma$ system is the archetypal witness:
    15	$p_{\max} = 1$, $k_{\max} = 0$, $r_{\max} = 4$.
    16	This distinction is load-bearing for the operator-order trichotomy
    17	of Theorem~\ref{thm:shadow-depth-operator-order} and for the
    18	classification of the standard landscape into the four
    19	classes~$G,L,C,M$.
    20	\end{abstract}
wait(call_1mdFiSaruaDcWeCwTttmKBhZ) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"m_3\\"'^{'"\\\\mathrm{SC}}\" -n \"m_3"'^{SC}" -n "m_3''^{'"\\mathrm{SC}}\" -n \"m_3"'^{'"\\mathrm{SC}}\" chapters -n" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:m_3\^{\mathrm{SC}})
             ^
error: repetition quantifier expects a valid decimal
collab wait(call_z43QqPKweym9tOAGr72JjSK6)
  receivers: 019d8388-9549-7651-a4af-427231f754d7
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "m_3" chapters/theory/chiral_koszul_pairs.tex | grep -n "SC"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3:2430:& $m_3^{\mathrm{SC}}$
4:2550: m_3^{\mathrm{SC}} = 0
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "m_3''^{'"\\\\mathrm\" chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:m_3^{\mathrm)
            ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -nF "m_3''^{SC}" -nF "m_3''^{'"\\mathrm{SC}}\" chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: m_3^{\mathrm{SC}}: No such file or directory (os error 2)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -nF 'm_3"'^{'"\\mathrm{SC}}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:16655:it detects whether the cubic Swiss-cheese operation $m_3^{\mathrm{SC}}$
chapters/theory/higher_genus_modular_koszul.tex:16701: $m_3^{\mathrm{SC}}{\neq}0$, $m_k^{\mathrm{SC}}{=}0$ for $k \geq 4$ & Jacobi cubic; quartic killed \\
chapters/theory/higher_genus_modular_koszul.tex:16703: $m_3^{\mathrm{SC}}{=}0$, $m_4^{\mathrm{SC}}{\neq}0$ &
chapters/theory/higher_genus_modular_koszul.tex:16736:For class~$\mathbf{L}$ (affine KM), $m_3^{\mathrm{SC}} \neq 0$
chapters/theory/higher_genus_modular_koszul.tex:16742:($\beta\gamma$), $m_3^{\mathrm{SC}} = 0$ on the neutral
chapters/theory/chiral_koszul_pairs.tex:2430:& $m_3^{\mathrm{SC}}$
chapters/theory/chiral_koszul_pairs.tex:2550: m_3^{\mathrm{SC}} = 0
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16620,16780p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 16620	\begin{enumerate}[label=\textup{(\roman*)}]
 16621	\item Class~$\mathbf{G}$ is formal \emph{even at}
 16622	 $d' = 1$: the OPE is abelian, so all transferred
 16623	 $A_\infty$-operations $m_k^{\mathrm{SC}} = 0$ for
 16624	 $k \geq 3$ (Heisenberg, lattice VOAs).
 16625	 This class is strictly larger than the GKW formal locus.
 16626	\item Class~$\mathbf{L}$: $m_3 \neq 0$ from the Lie bracket,
 16627	 $m_k = 0$ for $k \geq 4$ (Jacobi identity kills the
 16628	 quartic obstruction).
 16629	\item Class~$\mathbf{C}$: $m_3 = 0$ on the neutral stratum,
 16630	 $m_4 \neq 0$ from the contact quartic, $m_k = 0$ for
 16631	 $k \geq 5$ (rank-one rigidity).
 16632	\item Class~$\mathbf{M}$: $m_k \neq 0$ for all $k \geq 3$
 16633	 (the all-degree master equation forces an infinite tower).
 16634	\end{enumerate}
 16635	The map $\varphi\colon
 16636	\{\mathbf{G},\mathbf{L},\mathbf{C},\mathbf{M}\}
 16637	\to \{\text{formal}, \text{non-formal}\}$
 16638	sending $\mathbf{G} \mapsto \text{formal}$ and
 16639	$\{\mathbf{L},\mathbf{C},\mathbf{M}\} \mapsto \text{non-formal}$
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "invariant bilinear form" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
315:$\mathrm{MCG}$-invariant bilinear form), and integration
4935:over~$\mathbb{C}$ with non-degenerate invariant bilinear form
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4910,4955p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4910	($G^0 = \widehat{L}_W$), separated ($\bigcap_m G^m = 0$), and
  4911	respected by the brackets:
  4912	$\hat{l}_n(G^{m_1}, \ldots, G^{m_n}) \subseteq
  4913	G^{m_1 + \cdots + m_n}$.
  4914	
  4915	(b)\enspace The composition constraint
  4916	$g_1 + \cdots + g_n = g$ with $g_i \geq 0$ admits
  4917	$\binom{g + n - 1}{n - 1}$ solutions. For fixed~$g$, only
  4918	degrees $n \leq g + 1$ contribute when $\theta_0 = 0$; in
  4919	general the series is controlled by the bar-length filtration
  4920	of~$L$.
  4921	
  4922	(c)\enspace Rearranging: $l_1(\theta_g) = -O_g(\theta_{<g})$,
  4923	where $O_g$ depends only on $\theta_h$ with $h < g$. A
  4924	solution~$\theta_g$ exists if and only if $[O_g] = 0$ in
  4925	$H^2(L, l_1)$. By K\"unneth (since $W_g$ is
  4926	finite-dimensional),
  4927	$H^*(L \otimes W_g) \cong H^*(L) \otimes W_g$, placing the
  4928	obstruction in $H^2(L, l_1) \otimes W_g$.
  4929	\end{proof}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "shadow-archetype-classification" -n "shadow depth class" -n "riic" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: shadow depth class: No such file or directory (os error 2)
rg: riic: No such file or directory (os error 2)
chapters/theory/chiral_koszul_pairs.tex:75:(Theorem~\ref{thm:shadow-archetype-classification}), record the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:shadow-archetype-classification\" -n \"shadow-archetype\" -n \"shadow depth\" chapters/theory -n" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: shadow-archetype: No such file or directory (os error 2)
rg: shadow depth: No such file or directory (os error 2)
chapters/theory/higher_genus_modular_koszul.tex:16390:\label{thm:shadow-archetype-classification}
wait(call_z43QqPKweym9tOAGr72JjSK6) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16360,16435p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 16360	 \S\ref{sec:betagamma-quartic-birth} \\[3pt]
 16361	$\mathrm{Vir}_c$ &
 16362	 $\mathbf{M}$ & $\infty$ & $\infty$
 16363	 & $\frac{40}{5c{+}22}$ &
 16364	 Thm~\ref{thm:w-virasoro-quintic-forced} \\
 16365	$\mathcal{W}_N$ &
 16366	 $\mathbf{M}$ & $\infty$ & $\infty$
 16367	 & $\neq 0$ &
 16368	 \S\ref{sec:mixed-cubic-quartic-shadows} \\[6pt]
 16369	\multicolumn{6}{l}{\emph{Higher-rank lattice VOAs
 16370	 (\S\ref{sec:higher-depths}; class by $d_{\mathrm{alg}}$, cf.\
 16371	 Theorem~\ref{thm:depth-decomposition}):}} \\
 16372	$V_{\mathrm{Leech}}$ &
 16373	 $\mathbf{G}$ & $4$ & $0$ & $0$ &
 16374	 Prop~\ref{prop:leech-epstein} \\
 16375	Rank-$48$ &
 16376	 $\mathbf{G}$ & $5$ & $0$ & $0$ &
 16377	 \S\ref{sec:higher-depths} \\
 16378	Rank-$72$ &
 16379	 $\mathbf{G}$ & $6$ & $0$ & $0$ &
codex
I’ve got the main proposition and proof. I’m still chasing the dependency chain rather than trusting the prose summary, because the likely failure mode here is a proof step leaning on a theorem that does not actually supply the needed hypothesis.
collab wait(call_7fQfdFS3BdUcTUqVu3goISN8)
  receivers: 019d8388-9549-7651-a4af-427231f754d7
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/frame/preface.tex | sed -n '2520,2765p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2520	\in \{0, 1, 2, \infty\}$
  2521	(Proposition~\ref{prop:depth-gap-trichotomy}). No standard
  2522	family realises $d_{\mathrm{alg}} = 3$; the gap is forced by the
  2523	degree-$2$ algebraicity of the generating function, which
  2524	constrains the branching pattern of $\sqrt{Q_L}$ to at most
  2525	quadratic order.
  2526	
  2527	\subsection*{6.5.\enspace The four depth classes}
  2528	
  2529	The \emph{shadow depth} $r_{\max}(\cA)$ is the largest degree at
  2530	which the shadow obstruction tower carries a nontrivial
  2531	invariant, or $\infty$ if the tower never terminates. Three
  2532	numerical invariants must be distinguished:
  2533	\begin{itemize}[nosep]
  2534	\item $p_{\max}(\cA)$: generator OPE pole order,
  2535	\item $k_{\max}(\cA)=p_{\max}-1$: collision depth
  2536	 (logarithmic absorption),
  2537	\item $r_{\max}(\cA)$: shadow depth (independent of
  2538	 $p_{\max}$).
  2539	\end{itemize}

thinking
**Summarizing source references with line numbers**

I'll gather precise file paths, labels, and line ranges to answer each question: (1) swiss-cheese nonformality proposition, (2) relation between \(m_3^{SC}\) and cubic shadow \(S_3\) with two key references, (3) modular characteristic theorem’s content about bilinear form nondegeneracy, (4) definition of the standard landscape including its table, and (5) the theorem classifying the four landscape classes. I'll provide brief descriptions alongside each reference for clarity.
codex
- 1. `chapters/theory/chiral_koszul_pairs.tex:2414-2480` (`prop:swiss-cheese-nonformality-by-class`) — the table there stratifies the Swiss-cheese operations by shadow depth for classes G/L/C/M, then the “Mechanism” paragraph (lines 2458‑2480) explains how each class enforces the corresponding vanishing/non-vanishing pattern of $m_k^{\mathrm{SC}}$ (in particular $m_3=0$ only for class G) and justifies the classification via OPE pole orders, parity obstructions, and contact/quartic invariants.

- 2. `chapters/theory/chiral_koszul_pairs.tex:2521-2555` (`prop:sc-formal-iff-class-g` proof) plus `chapters/theory/higher_genus_modular_koszul.tex:16655-16669` (Remark on the GKW dichotomy) — the proposition’s converse argument spells out the chain “SC-formal ⇒ $m_3^{\mathrm{SC}}=0$ ⇒ cubic shadow $S_3=0$ ⇒ $C(x,y,z)=\kappa(x,[y,z])=0$,” and the higher-genus remark immediately before `prop:sc-formality-by-class` says that the cubic SC operation vanishing is exactly what detects the $S_3$ obstruction, so these passages together anchor the $m_3^{\mathrm{SC}}$–$S_3$ relation.

- 3. `chapters/theory/higher_genus_modular_koszul.tex:2628-2690` (`thm:modular-characteristic`) — the theorem only describes the scalar modular characteristic $\kappa(\cA)$, its genus‑$g$ factorization $\mathrm{obs}_g=\kappa\cdot\lambda_g$, its generating function, duality/additivity properties, and the resulting homomorphism; it nowhere asserts anything about an invariant bilinear form being nondegenerate, so the “nondegeneracy of the invariant form” used in the SC-formality argument must come from another place (e.g., the complementarity theorems referenced nearby).

- 4. `chapters/frame/preface.tex:2541-2565` (Section “The standard landscape” and the preceding 6.5 subsection) — this passage spells out the “standard landscape” as the finite list of universal families (Heisenberg, affine Kac–Moody, $\beta\gamma$, $bc$ ghosts, Virasoro, $\mathcal W_N$, lattice VOAs, free fermion, etc.), states that it is partitioned into the four shadow-depth classes, and provides the table that pairs each class (G/L/C/M) with the relevant examples and the vanishing pattern of the cubic/quartic shadows, so this is the precise definition of the landscape the SC-formality proposition refers to.

- 5. `chapters/theory/higher_genus_modular_koszul.tex:16389-16429` (`thm:shadow-archetype-classification`) — the theorem states that every chirally Koszul algebra in the standard landscape lies in exactly one of the shadow-depth classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$, then enumerates the primitive examples and the defining obstruction pattern for each class (e.g., only $\mathbf{L}$ has the unique nonzero cubic shadow $\kappa(x,[y,z])$, only $\mathbf{C}$ has the quartic contact invariant, $\mathbf{M}$ has both and an infinite tower), so it is the formal source of the G/L/C/M identification.
wait(call_7fQfdFS3BdUcTUqVu3goISN8) 1 agents complete:
  019d8388-9549-7651-a4af-427231f754d7 completed: "- 1. `chapters/theory/chiral_koszul_pairs.tex:2414-2480` (`prop:swiss-cheese-nonformality-by-class`) — the table there s…"
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2390,2485p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2620,2705p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2390	(item~(iii) of Theorem~\ref{thm:koszul-equivalences-meta})
  2391	is the bar-complex statement of the formality theorem of
  2392	Gaiotto--Kulp--Wu~\cite{GKW2025}: the transferred operations
  2393	$m_k = 0$ for $k \geq 3$ on bar cohomology if and only if
  2394	$\cA$ is chirally Koszul. The shadow depth classification
  2395	$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
  2396	(Remark~\ref{rem:shadow-depth-gkw-refinement}) refines their
  2397	binary formal/non-formal dichotomy into a four-class stratification
  2398	governed by the discriminant $\Delta = 8\kappa S_4$.
  2399	\end{remark}
  2400	
  2401	\begin{remark}[Loop-exactness ordering $G < L < C < M$]
  2402	\label{rem:loop-exactness-ordering}
  2403	\index{shadow depth!loop-exactness ordering}
  2404	The four shadow-depth classes are ordered by the number of loop corrections needed to determine the full $A_\infty$ structure on~$\cA^!_{\mathrm{line}}$:
  2405	\begin{itemize}
  2406	\item Class~$G$ (Gaussian, $r_{\max}=2$): tree-level exact.
  2407	\item Class~$L$ (Lie/tree, $r_{\max}=3$): one-loop exact (DNP non-renormalization, Theorem~\ref{thm:dnp-bar-cobar-identification}(iii)).
  2408	\item Class~$C$ (Contact, $r_{\max}=4$): two-loop exact.
  2409	\item Class~$M$ (Mixed, $r_{\max}=\infty$): requires all-loop resummation.
 succeeded in 52ms:
  2620	(Remark~\ref{rem:chain-vs-classical-mf}). The degree-$2$ projection
  2621	of $\Theta_\cA$ is the scalar $\kappa(\cA)$ that controls the
  2622	entire genus tower (the spectral discriminant~$\Delta_\cA$,
  2623	periodicity profile~$\Pi_\cA$, and full MC
  2624	class~$\Theta_\cA$ require data beyond~$\kappa$;
  2625	see Definition~\ref{def:full-modular-package}).
  2626	
  2627	\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
  2628	\label{thm:modular-characteristic}
  2629	\index{modular characteristic theorem|textbf}
  2630	\index{kappa@$\kappa$!as first characteristic number|textbf}
  2631	\textup{[}Regime: curved-central
  2632	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  2633	
  2634	Let $\cA$ be a modular Koszul chiral algebra
  2635	(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
  2636	characteristic package
  2637	(Definition~\ref{def:scalar-modular-package}) is controlled by one
  2638	number, the genus-$1$ curvature coefficient
  2639	$\kappa(\cA) \in \mathbb{C}$. More precisely:
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2528,2575p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16380,16445p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16635,16690p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2528	
  2529	The \emph{shadow depth} $r_{\max}(\cA)$ is the largest degree at
  2530	which the shadow obstruction tower carries a nontrivial
  2531	invariant, or $\infty$ if the tower never terminates. Three
  2532	numerical invariants must be distinguished:
  2533	\begin{itemize}[nosep]
  2534	\item $p_{\max}(\cA)$: generator OPE pole order,
  2535	\item $k_{\max}(\cA)=p_{\max}-1$: collision depth
  2536	 (logarithmic absorption),
  2537	\item $r_{\max}(\cA)$: shadow depth (independent of
  2538	 $p_{\max}$).
  2539	\end{itemize}
  2540	
  2541	The standard landscape partitions into four classes
  2542	by the cubic shadow $\mathfrak C$ (the degree-$3$ obstruction)
  2543	and the quartic contact invariant $\mathfrak Q$ (the
  2544	canonical degree-$4$ class of \S6.3). The single-line
  2545	dichotomy (Theorem~\ref{thm:single-line-dichotomy}):
  2546	$\Delta = 0$ forces tower termination; $\Delta \neq 0$
  2547	forces an infinite tower.
 succeeded in 50ms:
 16380	 \S\ref{sec:higher-depths} \\
 16381	\bottomrule
 16382	\multicolumn{6}{l}{\textsuperscript{$\ast$}%
 16383	 Stratum separation: $\Delta \neq 0$ on charged stratum,
 16384	 $\dim\Defcyc^{(2q)} = 0$.}
 16385	\end{tabular}
 16386	\end{center}
 16387	\end{example}
 16388	
 16389	\begin{theorem}[Shadow archetype classification]
 16390	\label{thm:shadow-archetype-classification}
 16391	\ClaimStatusProvedHere
 16392	\index{shadow depth!classification theorem|textbf}
 16393	\index{shadow archetype classification|textbf}
 16394	Every chirally Koszul algebra in the standard landscape belongs to
 16395	exactly one of the shadow depth classes $\mathbf{F}_2$, $\mathbf{F}_3$,
 16396	$\mathbf{F}_4$, or $\mathbf{M}$
 16397	\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 16398	The class is determined by the vanishing pattern of obstruction
 16399	classes at degrees~$3$, $4$, $5$, and the assignments for the
 succeeded in 50ms:
 16635	The map $\varphi\colon
 16636	\{\mathbf{G},\mathbf{L},\mathbf{C},\mathbf{M}\}
 16637	\to \{\text{formal}, \text{non-formal}\}$
 16638	sending $\mathbf{G} \mapsto \text{formal}$ and
 16639	$\{\mathbf{L},\mathbf{C},\mathbf{M}\} \mapsto \text{non-formal}$
 16640	is surjective but not injective: three classes collapse
 16641	to one in the GKW picture.
 16642	The shadow metric discriminant
 16643	$\Delta = 8\kappa S_4$
 16644	(Definition~\ref{def:shadow-metric})
 16645	is the quantitative invariant that GKW's binary
 16646	classification does not capture:
 16647	$\Delta = 0$ separates finite shadow depth
 16648	($\mathbf{G}$/$\mathbf{L}$) from infinite shadow depth
 16649	($\mathbf{M}$), while the vanishing pattern of
 16650	$\alpha$ and $S_4$ individually distinguishes
 16651	$\mathbf{G}$ from $\mathbf{L}$ and $\mathbf{C}$
 16652	from~$\mathbf{M}$.
 16653	The GKW formality/non-formality dichotomy is the genus-$0$,
 16654	degree-$3$ projection of the shadow depth classification:

thinking
**Checking class consistency**

I need to see if the property about the swiss-cheese nonformality by class classification conflicts with the canonical class theorem. The proof currently relies solely on class G=Heisenberg, which could lead to a serious inconsistency. So, I should verify the details to ensure everything aligns properly. It’s essential to double-check and make sure there aren't any contradictions before moving forward!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16670,16840p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 16670	\begin{proposition}[Swiss-cheese formality classification by shadow class;
 16671	\ClaimStatusProvedHere]
 16672	\label{prop:sc-formality-by-class}
 16673	\index{Swiss-cheese!formality classification|textbf}
 16674	\index{shadow depth!Swiss-cheese formality}
 16675	Three distinct formality properties are governed by the
 16676	shadow depth class. Let $\cA$ be a modular Koszul chiral
 16677	algebra.
 16678	\begin{enumerate}[label=\textup{(\roman*)}]
 16679	\item \emph{$A_\infty$-formality of bar cohomology}
 16680	 \textup{(}operations on $H^*(\Barch(\cA))$\textup{)}:
 16681	 the transferred $A_\infty$ operations $m_k = 0$ for
 16682	 $k \geq 3$. This holds for \emph{all} Koszul algebras in
 16683	 \emph{all} four classes $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
 16684	 \textup{(}Theorem~\textup{\ref{thm:koszul-equivalences-meta}},
 16685	 item~\textup{(iii))}.
 16686	\item \emph{Swiss-cheese operations $m_k^{\mathrm{SC}}$ on
 16687	 $\cA$ itself} \textup{(}encoded by the
 16688	 $\mathrm{SC}^{\mathrm{ch,top}}$ operad\textup{)}:
 16689	 \begin{center}
exec
/bin/zsh -lc "rg -n \"prop:sc-formal-iff-class-g|SC-formality|Swiss-cheese formal iff|class~\\\\mathbf\\{G\\}\" chapters metadata appendices | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:prop:sc-formal-iff-class-g|SC-formality|Swiss-cheese formal iff|class~\mathbf\{G\})
                                                                             ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F \"prop:sc-formal-iff-class-g\" chapters metadata appendices && rg -n \"SC-formality|Swiss-cheese formal\" chapters metadata appendices | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/dependency_graph.dot:2411:  prop_sc_formal_iff_class_g [label="prop:sc-formal-iff-class-g\nproposition [Pr]\nSC-formality characterises class~$G$", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:412:| `prop:sc-formal-iff-class-g` | `proposition` | 2455 | SC-formality characterises class~$G$ |
metadata/label_index.json:26938:  "prop:sc-formal-iff-class-g": {
metadata/claims.jsonl:2312:{"label": "prop:sc-formal-iff-class-g", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 2455, "title": "SC-formality characterises class~$G$"}
chapters/connections/concordance.tex:7073:\ref{prop:sc-formal-iff-class-g}
chapters/connections/concordance.tex:7076: \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
chapters/connections/concordance.tex:9648: \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)} \\
chapters/theory/e1_modular_koszul.tex:1194:  (Proposition~\ref{prop:sc-formal-iff-class-g}).
chapters/theory/introduction.tex:91:(Proposition~\ref{prop:sc-formal-iff-class-g}).
chapters/theory/chiral_koszul_pairs.tex:87:(Proposition~\ref{prop:sc-formal-iff-class-g}).
chapters/theory/chiral_koszul_pairs.tex:2522:\label{prop:sc-formal-iff-class-g}
chapters/theory/en_koszul_duality.tex:2891:(Proposition~\ref{prop:sc-formal-iff-class-g}), so
chapters/frame/preface.tex:2572:(Proposition~\ref{prop:sc-formal-iff-class-g}): the vanishing
chapters/frame/preface.tex:2608:(Proposition~\ref{prop:sc-formal-iff-class-g}).
metadata/theorem_registry.md:412:| `prop:sc-formal-iff-class-g` | `proposition` | 2455 | SC-formality characterises class~$G$ |
metadata/theorem_registry.md:980:| `prop:sc-formality-by-class` | `proposition` | 16289 | Swiss-cheese formality classification by shadow class |
metadata/dependency_graph.dot:2411:  prop_sc_formal_iff_class_g [label="prop:sc-formal-iff-class-g\nproposition [Pr]\nSC-formality characterises class~$G$", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:3053:  prop_sc_formality_by_class [label="prop:sc-formality-by-class\nproposition [Pr]\nSwiss-cheese formality classification by...", style=filled, fillcolor="#c8e6c9"];
metadata/claims.jsonl:2312:{"label": "prop:sc-formal-iff-class-g", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 2455, "title": "SC-formality characterises class~$G$"}
metadata/claims.jsonl:2941:{"label": "prop:sc-formality-by-class", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 16289, "title": "Swiss-cheese formality classification by shadow class", "refs_in_block": ["thm:koszul-equivalences-meta"]}
exec
/bin/zsh -lc "rg -n \"nondegenerate invariant bilinear form|invariant bilinear form.*nondegenerate|perfect pairing|nondegeneracy of the invariant\" chapters/theory chapters/frame chapters/examples chapters/connections | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"self-duality|Lagrangian complementarity\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/examples | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_symplectic_polarization.tex:176:The Koszul pairing restricts to a perfect pairing on centers
chapters/connections/thqg_symplectic_polarization.tex:403:and Serre duality on the stack gives a perfect pairing on
chapters/examples/yangians_foundations.tex:3040:The next result shows that a finite bar-duality datum (perfect pairings
chapters/examples/yangians_foundations.tex:3053:\item perfect pairings
chapters/examples/yangians_foundations.tex:3056:\item induced perfect pairings on reduced bar slices
chapters/theory/poincare_duality.tex:129:perfect pairing
chapters/theory/poincare_duality.tex:172:There exists a canonical perfect pairing:
chapters/connections/thqg_fredholm_partition_functions.tex:2701:$\cZ(\cA)$ carries the perfect pairing from
chapters/connections/holographic_codes_koszul.tex:193:is a perfect pairing
chapters/connections/holographic_codes_koszul.tex:252: $\cC \times \mathbf{Q}_g(\cA^!)$ is a perfect pairing
chapters/theory/higher_genus_foundations.tex:1423:Applied to the sheaf $j_!\mathbb{C}_{C_n(X)}$ where $j: C_n(X) \hookrightarrow \overline{C}_n(X)$ is the open inclusion, this exchanges $j_!$ and $Rj_*$ (Theorem~\ref{thm:verdier-config}), identifying logarithmic forms on the compactification with distributional forms on the open configuration space. The perfect pairing $\langle \eta_{ij}, \delta(z_i - z_j) \rangle = 1$ realizes the NAP isomorphism at the level of differential forms, since residues (bar operations) and delta functions (cobar operations) are Verdier duals.
chapters/theory/chiral_koszul_pairs.tex:2517:nondegeneracy of the invariant form turns vanishing of the
chapters/theory/chiral_koszul_pairs.tex:2561:$\kappa$ is a perfect pairing: if $C(x,y,z) = \kappa(x,[y,z]) = 0$
chapters/theory/higher_genus_complementarity.tex:104:(a nondegenerate invariant bilinear form), then
chapters/theory/higher_genus_complementarity.tex:608:& Establish perfect pairing between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$\\
chapters/theory/higher_genus_complementarity.tex:1093:is a perfect pairing. This is the geometric incarnation of Verdier duality.
chapters/theory/higher_genus_complementarity.tex:1118:The Verdier duality on $\overline{C}_n(X)$ induces a perfect pairing:
chapters/theory/higher_genus_complementarity.tex:1229:induces a duality of spectral sequences and a perfect pairing
chapters/theory/higher_genus_complementarity.tex:1353:to a perfect pairing on centers $Z(\mathcal{A}) \otimes Z(\mathcal{A}^!) \to \mathbb{C}$:
chapters/theory/higher_genus_complementarity.tex:1814:duality gives a perfect pairing
 succeeded in 50ms:
chapters/theory/chiral_koszul_pairs.tex:52:$\barB_X(\cA^!)$; (c)~produces Lagrangian complementarity
chapters/theory/chiral_koszul_pairs.tex:109:Lagrangian complementarity between $\cA$ and $\cA^!$
chapters/theory/chiral_koszul_pairs.tex:2558:form~$\kappa$ (this is a consequence of the self-duality or
chapters/theory/chiral_koszul_pairs.tex:2559:Lagrangian complementarity of the landscape; see
chapters/theory/chiral_koszul_pairs.tex:3776:\section{Yangians and affine Yangians: self-duality and Koszul theory}
chapters/theory/chiral_koszul_pairs.tex:3780:provide examples where Koszul duality manifests as self-duality.
chapters/theory/chiral_koszul_pairs.tex:5011:\label{cor:e1-self-duality}
chapters/theory/chiral_koszul_pairs.tex:5029:of the classical self-duality $\operatorname{Ass}^! \cong
chapters/theory/chiral_koszul_pairs.tex:5141:Corollary~\ref{cor:e1-self-duality}\textup{)}. When the finite-type
chapters/theory/higher_genus_complementarity.tex:2312:The self-duality isomorphism $f\colon \cA \xrightarrow{\sim} \cA^!$ induces,
chapters/theory/higher_genus_complementarity.tex:2974:phenomena: $c = 13$ is self-duality of the Koszul pair, $c = 26$
chapters/theory/higher_genus_complementarity.tex:5269:\item \emph{Self-holographic self-duality.}\;
chapters/theory/higher_genus_complementarity.tex:5836:The numerator $6960 = 2^4 \cdot 3 \cdot 5 \cdot 29 = 40 \cdot 174$ in the discriminant complementarity formula $\Delta + \Delta' = 6960/[(5c{+}22)(152{-}5c)]$ is a \emph{universal constant}: it depends on neither $c$ nor the specific algebra within the Virasoro family. The factor $40$ is the $c$-independent numerator of $\Delta(c) = 40/(5c{+}22)$, which arises from $8\kappa(c) Q^{\mathrm{contact}}(c) = 8 \cdot (c/2) \cdot 10/[c(5c{+}22)] = 40/(5c{+}22)$. At self-duality $c = 13$ this gives $\Delta(13) = 40/87$, and $174 = (5c{+}22 + 152{-}5c)|_{c=13} = 87 + 87$ is the sum of the two Lee--Yang denominators at self-duality.
chapters/theory/higher_genus_modular_koszul.tex:505:\emph{(Lagrangian complementarity; Theorem~\textup{\ref{thm:quantum-complementarity-main}}.)}
chapters/theory/higher_genus_modular_koszul.tex:2982:(Proposition~\ref{prop:c13-full-self-duality}) is the
chapters/theory/higher_genus_modular_koszul.tex:9433:and duality reflects Verdier self-duality
chapters/theory/higher_genus_modular_koszul.tex:26738:self-duality $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$
chapters/theory/higher_genus_modular_koszul.tex:26907:\begin{proposition}[Full tower self-duality at $c = 13$;
chapters/theory/higher_genus_modular_koszul.tex:26909:\label{prop:c13-full-self-duality}
chapters/theory/higher_genus_modular_koszul.tex:26910:\index{Virasoro algebra!self-duality at $c=13$|textbf}

thinking
**Investigating the theorem**

I need to look closely at the higher_genus_complementarity at line 104, specifically the definition of "quadratic," since it involves a nondegenerate invariant bilinear form. The proof cites the modular characteristic theorem, so I'm curious if there's a theorem that shows standard landscape families carry these nondegenerate invariant bilinear forms. My plan is to search for "standard landscape carries a nondegenerate invariant bilinear form" and check the relevant hits around that line.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '90,130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1340,1365p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2298,2338p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    90	nondegeneracy of the Verdier pairing is a hypothesis verified
    91	family by family
    92	(Proposition~\ref{prop:standard-examples-modular-koszul}).
    93	The fiber--center identification~(C0) and the
    94	S-level decomposition~(C1) hold unconditionally on the
    95	Koszul locus; the H-level Lagrangian upgrade~(C2) is the
    96	geometric content of the nonlinear theory.
    97	
    98	\begin{remark}[Calabi--Yau exchange and the perfectness hypothesis]
    99	\label{rem:hr24-cy-interchange}
   100	Holstein--Rivera~\cite{HR24} prove that Koszul duality
   101	between dg categories and pointed curved coalgebras exchanges
   102	smooth and proper Calabi--Yau structures. Applied to our
   103	setting: if $\cA$ carries a smooth $\mathrm{CY}_1$ structure
   104	(a nondegenerate invariant bilinear form), then
   105	$\barB(\cA)$ carries a proper $\mathrm{CY}_1$ structure
   106	(finite-dimensional bar cohomology at each weight). In particular, hypothesis~(P2) (nondegeneracy) implies
   107	fiber-level perfectness of the bar complex, and makes
   108	hypothesis~(P3) (dual regularity: $\cA^!$ also satisfies
   109	(P1)--(P2)) redundant on the Koszul locus via Verdier
 succeeded in 50ms:
  2298	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  2299	
  2300	Let $(\cA, \cA^!)$ be a Koszul chiral pair
  2301	(Definition~\ref{def:chiral-koszul-pair}) with $\cA \cong \cA^!$
  2302	as chiral algebras. Then for all $g \geq 1$:
  2303	\begin{equation}\label{eq:self-dual-halving}
  2304	\dim Q_g(\cA) \;=\; \dim Q_g(\cA^!)
  2305	\;=\; \tfrac{1}{2}\,\dim H^*(\overline{\mathcal{M}}_g, Z(\cA))
  2306	\end{equation}
  2307	In particular, $\dim H^*(\overline{\mathcal{M}}_g, Z(\cA))$ is even
  2308	for every $g \geq 1$.
  2309	\end{theorem}
  2310	
  2311	\begin{proof}
  2312	The self-duality isomorphism $f\colon \cA \xrightarrow{\sim} \cA^!$ induces,
  2313	by functoriality of the bar construction
  2314	(Theorem~\ref{thm:geometric-equals-operadic-bar}), an isomorphism on
  2315	genus-$g$ bar complexes $\bar{B}^{(g)}(f)\colon \bar{B}^{(g)}(\cA)
  2316	\xrightarrow{\sim} \bar{B}^{(g)}(\cA^!)$. Passing to cohomology gives
  2317	\begin{equation}\label{eq:self-dual-qg-iso}
 succeeded in 50ms:
  1340	$\mathbb{D}(\mathcal{F})$ carries the contragredient action
  1341	$\rho^\vee = -\rho^t$, which reverses signs):
  1342	\begin{equation}\label{eq:verdier-lie-anticommute}
  1343	\mathbb{D} \circ \mathcal{L}_{\tilde{v}} = -\mathcal{L}_{\tilde{v}} \circ \mathbb{D}
  1344	\end{equation}
  1345	
  1346	Concretely, $\mathbb{D}$ reverses the orientation of the fibers of the FM
  1347	compactification, and the Lie derivative reverses sign under orientation reversal.
  1348	
  1349	\emph{Ingredient 2: Verdier duality intertwines center actions via the Koszul pairing.}
  1350	For $z \in Z(\mathcal{A})$, the action $\rho(z)$ on the bar complex
  1351	$\bar{B}^{(g)}(\mathcal{A})$ is a $\mathcal{D}$-module endomorphism (since $z$ is
  1352	central). The Koszul pairing $\mathcal{A} \otimes \mathcal{A}^! \to \omega_X$ restricts
  1353	to a perfect pairing on centers $Z(\mathcal{A}) \otimes Z(\mathcal{A}^!) \to \mathbb{C}$:
  1354	the module Koszul duality equivalence $\Phi$ of
  1355	Sublemma~\ref{lem:center-isomorphism} identifies
  1356	$Z(\mathcal{A}) = \mathrm{End}_{\mathrm{Mod}_{\mathcal{A}}}(\mathcal{A})$ with
  1357	$Z(\mathcal{A}^!) = \mathrm{End}_{\mathrm{Mod}_{\mathcal{A}^!}}(\mathcal{A}^!)$,
  1358	and $\Phi$ intertwines the Koszul pairing
  1359	(Corollary~\ref{cor:duality-bar-complexes-complete}) with the
exec
/bin/zsh -lc "rg -n \"prop:standard-examples-modular-koszul|nondegeneracy of the Verdier pairing|P2\\)|nondegenerate invariant bilinear form\" chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:90:nondegeneracy of the Verdier pairing is a hypothesis verified
chapters/theory/higher_genus_complementarity.tex:92:(Proposition~\ref{prop:standard-examples-modular-koszul}).
chapters/theory/higher_genus_complementarity.tex:104:(a nondegenerate invariant bilinear form), then
chapters/theory/higher_genus_complementarity.tex:106:(finite-dimensional bar cohomology at each weight). In particular, hypothesis~(P2) (nondegeneracy) implies
chapters/theory/higher_genus_complementarity.tex:109:(P1)--(P2)) redundant on the Koszul locus via Verdier
chapters/theory/higher_genus_modular_koszul.tex:199:Proposition~\ref{prop:standard-examples-modular-koszul} suffices.
chapters/theory/higher_genus_modular_koszul.tex:687:\label{prop:standard-examples-modular-koszul}
chapters/theory/higher_genus_modular_koszul.tex:3718:see Proposition~\textup{\ref{prop:standard-examples-modular-koszul}}.\textup{)}
chapters/examples/w3_holographic_datum.tex:223:(P2)~the channel sum $\kappa_T + \kappa_W = c/2 + c/3$;
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '640,760p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   640	\emph{modular Koszul chiral algebra}.
   641	\end{definition}
   642	
   643	\begin{remark}[Axioms versus consequences]\label{rem:mk-axioms-vs-consequences}
   644	Only MK1--MK3 are axioms; MK4 and MK5 are
   645	consequences proved (Theorems~\ref{thm:higher-genus-inversion} and
   646	\ref{thm:quantum-complementarity-main}) and are not axioms. For
   647	modular Koszul chiral algebras with simple Lie symmetry, MK6 and MK7
   648	are further theorematic consequences of the universal MC package
   649	(Lemma~\ref{lem:mk67-from-mc2}). MK8 is the remaining
   650	ordered-factorization open problem.
   651	\end{remark}
   652	
   653	\begin{remark}[Logical structure]\label{rem:mk-axiom-relations}
   654	The definition separates \emph{hypotheses} (MK1--MK3) from
   655	\emph{consequences} (MK4--MK5). The hypotheses are checkable; the consequences are theorems: MK4 (inversion) is proved by Theorem~\ref{thm:higher-genus-inversion} and MK5 (complementarity) by Theorem~\ref{thm:quantum-complementarity-main}, both from MK1--MK3.
   656	There is no circularity. The dg axioms MK1--MK3 present the homotopy axioms
   657	\ref{MK:koszul-htpy}, \ref{MK:verdier-htpy},
   658	and~\ref{MK:modular-htpy} of
   659	Definition~\ref{def:modular-koszul-homotopy}. For simple Lie

thinking
**Clarifying audit details**

I'm thinking that there might be some confusion regarding what m3/S3 is detecting, and this could undermine the audit. I need to cite actual lines in the documentation more accurately. I'll inspect the exact definition of cubic shadow because I suspect that S3 refers to the normalized projection of C(x,y,z). To get more clarity, I'll search within the chiral_koszul_pairs and the higher genus modular koszul materials.
codex
The dependency pass is exposing drift inside the proof’s own neighborhood. I’m now checking whether the cubic step is even stable across the manuscript, because one nearby remark already appears to contradict the local class-`C` table on whether `m_3^{SC}` vanishes.
exec
/bin/zsh -lc "rg -n \"S_3|cubic shadow|m_3\\"'^'"\\{\\\\mathrm\\{SC\\}\\}|normalized projection|kappa\\(x, \\[y,z\\]\\)|\\mathfrak C\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/frame/preface.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16648,16660p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:S_3|cubic shadow|m_3\^\{\mathrm\{SC\}\}|normalized projection|kappa\(x, \[y,z\]\)|\mathfrak C)
                               ^^
error: unrecognized escape sequence
 succeeded in 51ms:
 16648	($\mathbf{G}$/$\mathbf{L}$) from infinite shadow depth
 16649	($\mathbf{M}$), while the vanishing pattern of
 16650	$\alpha$ and $S_4$ individually distinguishes
 16651	$\mathbf{G}$ from $\mathbf{L}$ and $\mathbf{C}$
 16652	from~$\mathbf{M}$.
 16653	The GKW formality/non-formality dichotomy is the genus-$0$,
 16654	degree-$3$ projection of the shadow depth classification:
 16655	it detects whether the cubic Swiss-cheese operation $m_3^{\mathrm{SC}}$
 16656	vanishes, which separates class~$\mathbf{G}$ from
 16657	$\{\mathbf{L}, \mathbf{C}, \mathbf{M}\}$.
 16658	The shadow obstruction tower extends this to all genera and degrees:
 16659	the quartic discriminant $\Delta$ distinguishes $\mathbf{C}$
 16660	from~$\mathbf{M}$, and the all-genera MC equation
exec
/bin/zsh -lc 'rg -n -F "m_3''^{'"\\mathrm{SC}}\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/frame/preface.tex && rg -n -F \"cubic shadow\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/frame/preface.tex && rg -n -F \"\\kappa(x, [y,z])\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
chapters/theory/chiral_koszul_pairs.tex:2430:& $m_3^{\mathrm{SC}}$
chapters/theory/chiral_koszul_pairs.tex:2550: m_3^{\mathrm{SC}} = 0
chapters/theory/higher_genus_modular_koszul.tex:16655:it detects whether the cubic Swiss-cheese operation $m_3^{\mathrm{SC}}$
chapters/theory/higher_genus_modular_koszul.tex:16701: $m_3^{\mathrm{SC}}{\neq}0$, $m_k^{\mathrm{SC}}{=}0$ for $k \geq 4$ & Jacobi cubic; quartic killed \\
chapters/theory/higher_genus_modular_koszul.tex:16703: $m_3^{\mathrm{SC}}{=}0$, $m_4^{\mathrm{SC}}{\neq}0$ &
chapters/theory/higher_genus_modular_koszul.tex:16736:For class~$\mathbf{L}$ (affine KM), $m_3^{\mathrm{SC}} \neq 0$
chapters/theory/higher_genus_modular_koszul.tex:16742:($\beta\gamma$), $m_3^{\mathrm{SC}} = 0$ on the neutral
chapters/frame/preface.tex:2139:the cubic shadow coefficient is universal because the Cachazo--Strominger
chapters/frame/preface.tex:2542:by the cubic shadow $\mathfrak C$ (the degree-$3$ obstruction)
chapters/frame/preface.tex:2790:The cubic shadow is the Lie bracket itself, and the Jacobi
chapters/frame/preface.tex:2939:The shadow tower terminates at degree~$4$. The cubic shadow
chapters/frame/preface.tex:4255: &&\text{(cubic shadow, Lie structure)},\\
chapters/theory/chiral_koszul_pairs.tex:2468:the cubic shadow vanishes by weight parity of the $\gamma$
chapters/theory/chiral_koszul_pairs.tex:2485:Class~$L$: the cubic shadow
chapters/theory/chiral_koszul_pairs.tex:2491:Class~$C$: the cubic shadow vanishes by the parity obstruction on
chapters/theory/chiral_koszul_pairs.tex:2518:cubic shadow into vanishing of the bracket itself. Of the
chapters/theory/chiral_koszul_pairs.tex:2540:The cubic shadow $S_3$ is the normalized projection of the
chapters/theory/higher_genus_modular_koszul.tex:50:the cubic shadow~$\mathfrak{C}$ at degree~$3$,
chapters/theory/higher_genus_modular_koszul.tex:3439:the cubic shadow $\mathfrak{C}$ at degree~$3$, the quartic
chapters/theory/higher_genus_modular_koszul.tex:10216: cohomology class $[\ell_3^{(0)}]$ is the cubic shadow
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31145,31170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2780,2800p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16460,16476p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14520,14542p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 31145	& \Theta^{(2)}_{\mathrm{pf}}
 31146	& \text{class}
 31147	\\[2pt]\hline
 31148	\rule{0pt}{11pt}
 31149	\mathcal{H}_k & \neq 0 & 0 & 0 & G \\
 31150	V_k(\fg) & \neq 0 & \neq 0 & \neq 0 & L \\
 31151	\beta\gamma & \neq 0 & 0 & \neq 0 & C \\
 31152	\mathrm{Vir}_c & \neq 0 & \neq 0 & \neq 0 & M
 31153	\end{array}
 31154	\]
 31155	The planted-forest shell $\Theta^{(2)}_{\mathrm{pf}}$ depends on
 31156	both cubic and quartic shadow data via the genus-$2$ planted-forest
 31157	graph sum \textup{(}$\delta_{\mathrm{pf}}^{(2,0)} =
 31158	S_3(10S_3 - \kappa)/48$\textup{)}: it vanishes iff
 31159	$S_3 = 0$ \textup{(}equivalently, iff the cubic shadow
 31160	$\mathfrak{C} = 0$\textup{)}, \emph{not} iff
 31161	$S_4 = 0$. For class~$L$ \textup{(}KM\textup{)},
 31162	$S_3 \neq 0$ and $S_4 = 0$, but planted-forest graphs with
 31163	cubic vertices still produce nonzero contributions.
 31164	Classes~$G$ and~$C$ have $S_3 = 0$ \textup{(}$\beta\gamma$
 succeeded in 51ms:
  2780	Lie-algebraic structure that was invisible in the Heisenberg
  2781	scalar. The level prefix $k$ ensures $r(z)$ vanishes in the
  2782	abelian limit; the averaging map collapses $k\,\Omega$ to a
  2783	scalar, and the Sugawara shift by the dual Coxeter number~$h^\vee$
  2784	yields
  2785	$\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$.
  2786	
  2787	The matrix structure builds the Yangian $Y(\fg)$: the quantum
  2788	group that deforms $U(\fg[z])$ arises from the ordered bar's
  2789	deconcatenation coproduct evaluated on $r(z) = k\,\Omega/z$.
  2790	The cubic shadow is the Lie bracket itself, and the Jacobi
  2791	identity kills all higher obstructions: $S_r(\widehat{\fg}_k) = 0$
  2792	for $r \ge 4$. The shadow tower terminates at degree~$3$:
  2793	class~L. The characteristic number $r_{\max} = 3$ coincides with
  2794	the number of terms in the Jacobi identity, the number of boundary
  2795	divisors of $\overline{\cM}_{0,4}$, and the number of channels in
  2796	the classical Yang--Baxter equation.
  2797	
  2798	At the critical level $k = -h^\vee$: $\kappa = 0$, the bar complex
  2799	is flat, and the chiral algebra acquires a large centre
 succeeded in 51ms:
 16460	\begin{proof}
 16461	Each case follows from the established vanishing theorems:
 16462	
 16463	(i)~For Heisenberg and lattice VOAs, the bar complex is strictly
 16464	coassociative ($m_k = 0$ for $k \geq 3$ in the transferred
 16465	$A_\infty$-structure), so all obstruction sources vanish
 16466	(Theorem~\ref{thm:nms-heisenberg-exact-linearity}).
 16467	
 16468	(ii)~For affine algebras, the cubic shadow is the Lie bracket
 16469	transported through the bar complex
 16470	(Theorem~\ref{thm:nms-affine-cubic-normal-form}). The quartic
 16471	obstruction $o_4 = \tfrac{1}{2}\{\mathfrak{C},\mathfrak{C}\}_H$
 16472	vanishes by the Jacobi identity: the cyclic double Lie bracket
 16473	$\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
 16474	
 16475	(iii)~For $\beta\gamma$, the quartic contact shadow is non-zero by
 16476	explicit computation
 succeeded in 51ms:
 14520	\smallskip
 14521	\noindent\textbf{Step~1} (Degree~$2$).
 14522	Solve the Maurer--Cartan equation at weight~$2$.
 14523	The unique solution is $\Theta_{\cA}^{\leq 2} = \kappa(\cA)$, the
 14524	modular characteristic (Theorem~D).
 14525	
 14526	\smallskip
 14527	\noindent\textbf{Step~2} (Degree~$3$).
 14528	Compute the obstruction $o_3(\cA) =
 14529	(D\Theta^{\leq 2} + \tfrac12[\Theta^{\leq 2},\Theta^{\leq 2}])_3$.
 14530	If $[o_3] = 0$ in $H^2(\cA^{\mathrm{sh}}_{3,0})$, the cubic shadow
 14531	$\mathfrak{C}(\cA) = 0$ (Gaussian archetype: Heisenberg).
 14532	If $[o_3] \neq 0$, define
 14533	$\Theta_{\cA}^{\leq 3} = \Theta_{\cA}^{\leq 2}
 14534	+ \mathfrak{C}(\cA)$ where $\mathfrak{C} = -h(o_3)$
 14535	(Lie archetype: affine).
 14536	
 14537	\smallskip
 14538	\noindent\textbf{Step~3} (Degree~$4$).
 14539	Compute $o_4(\cA) =
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2932,2948p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2932	$\beta\gamma$ system at weights $(\lambda, 1{-}\lambda)$ has
  2933	only a simple pole: $\beta(z)\gamma(w) \sim 1/(z{-}w)$. No
  2934	double pole means no metric, no Sugawara construction, no
  2935	Casimir tensor. The collision residue $r(z)$ is a constant
  2936	propagator~$P$, pole order zero after $d\log$-absorption.
  2937	$\kappa(\beta\gamma) = 1$.
  2938	
  2939	The shadow tower terminates at degree~$4$. The cubic shadow
  2940	vanishes (weight mismatch on the diagonal sector prevents a
  2941	cubic invariant from assembling), but the quartic contact
  2942	invariant is nonzero, killed only by rank-one abelian rigidity
  2943	at degree~$5$. The numerical witness:
  2944	$p_{\max} = 1$, $k_{\max} = 0$, $r_{\max} = 4$. Shadow
  2945	depth is independent of OPE pole order: the $\beta\gamma$ system
  2946	has the lowest pole order in the landscape ($p = 1$) and the
  2947	second-highest finite shadow depth ($r = 4$). This is the
  2948	archetypal class~C algebra: contact structure from a non-metric
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2588,2614p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2118,2146p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2588	\[
  2589	r_{\max}(\cA)
  2590	\;=\;
  2591	A_\infty\text{-depth}(\cA)
  2592	\;=\;
  2593	L_\infty\text{-formality level}(\gAmod).
  2594	\]
  2595	The shadow obstruction tower \emph{is} the $L_\infty$-formality
  2596	obstruction tower at all degrees
  2597	(Theorem~\ref{thm:shadow-formality-identification}). The four
  2598	classes G/L/C/M are the four formality types:
  2599	$\mathbf{G}$ = free,
  2600	$\mathbf{L}$ = Lie,
  2601	$\mathbf{C}$ = quadratic non-Lie,
  2602	$\mathbf{M}$ = genuinely nonlinear.
  2603	
  2604	The Swiss-cheese formality condition ($m_k^{\mathrm{SC}}=0$ for
  2605	all $k\ge 3$) selects exactly class~$\mathbf{G}$:
  2606	a chiral algebra in the standard landscape is SC-formal if and
  2607	only if it is Heisenberg
 succeeded in 51ms:
  2118	lives. Bar-cobar inversion proves that~$\Theta_\cA$ is a complete
  2119	invariant: Theorem~B recovers~$\cA$ from~$\Theta_\cA$. Verdier
  2120	duality decomposes~$\Theta_\cA$ into complementary halves: Theorem~C
  2121	splits the genus tower into Lagrangian summands. The leading
  2122	coefficient of~$\Theta_\cA$ is the modular characteristic: Theorem~D
  2123	extracts the scalar $\kappa(\cA)$ with $\hat A$-genus generating
  2124	function. The coefficient ring of~$\Theta_\cA$ is the chiral
  2125	Hochschild complex: Theorem~H identifies the deformation ring.
  2126	
  2127	The finite-order projections form an obstruction tower
  2128	$\Theta_\cA^{\leq 2} \to
  2129	\Theta_\cA^{\leq 3} \to
  2130	\Theta_\cA^{\leq 4} \to \cdots$
  2131	whose generating function is algebraic of degree~$2$: on each
  2132	primary line~$L$, the weighted shadow generating function
  2133	$H(t) = t^2\sqrt{Q_L(t)}$ for a quadratic polynomial~$Q_L$
  2134	determined by three seed invariants $(\kappa, \alpha, S_4)$.
  2135	The cubic seed $\alpha$ is level-independent for each family:
  2136	$\alpha = 2$ on the Virasoro primary line, so $a_3 = 3\alpha = 6$
  2137	is independent of the central charge. This $c$-independence is the
exec
/bin/zsh -lc "rg -n \"def:.*sc|Swiss-cheese formal|SC-formal|formality classification by shadow class|SC\\"'^'"\\{ch,top\\}\" chapters/theory | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2395:\label{def:scalar-modular-package}
chapters/theory/higher_genus_modular_koszul.tex:2453: (Definition~\ref{def:scalar-modular-package}),
chapters/theory/higher_genus_modular_koszul.tex:2495:\label{def:scalar-lane}
chapters/theory/higher_genus_modular_koszul.tex:2635:(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
chapters/theory/higher_genus_modular_koszul.tex:2637:(Definition~\ref{def:scalar-modular-package}) is controlled by one
chapters/theory/higher_genus_modular_koszul.tex:16670:\begin{proposition}[Swiss-cheese formality classification by shadow class;
chapters/theory/higher_genus_modular_koszul.tex:16674:\index{shadow depth!Swiss-cheese formality}
chapters/theory/en_koszul_duality.tex:1809:\textup{(}Definition~\textup{\ref{def:chiral-hochschild})},
chapters/theory/en_koszul_duality.tex:1896:(Definition~\ref{def:chiral-hochschild},
chapters/theory/en_koszul_duality.tex:2910:% TOPOLOGIZATION: SC^{ch,top} + SUGAWARA = E_3
chapters/theory/en_koszul_duality.tex:3171:and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
chapters/theory/coderived_models.tex:611:(Definition~\ref{def:coacyclic-contraacyclic}), and descends to
chapters/theory/bar_cobar_adjunction_inversion.tex:4859:(Definition~\ref{def:shadow-postnikov-tower}). At the scalar level
chapters/theory/koszul_pair_structure.tex:788:\label{def:derived-scalar-period}
chapters/theory/koszul_pair_structure.tex:1301:\textup{(}Definition~\ref{def:chiral-Phi-Psi}\textup{)} descend to
chapters/theory/e1_modular_koszul.tex:1195:\item \emph{SC-formality.} The Swiss-cheese type
chapters/theory/poincare_duality.tex:438:Here $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ is the geometric bar complex (Definition~\ref{def:geometric-bar}) and $\cA^{\scriptstyle \text{\normalfont !`}}$ is the Verdier dual chiral coalgebra (Construction~\ref{const:A-dual-intrinsic}). The Koszul dual \emph{algebra} is $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$.
chapters/theory/chiral_center_theorem.tex:36:(Definition~\ref{def:chiral-hochschild-cochain-brace},
chapters/theory/chiral_center_theorem.tex:299:\label{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:349:Definition~\ref{def:chiral-hochschild-cochain-brace}
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '1188,1200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3165,3175p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '84,94p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1188	  $m_k^{\mathrm{tr}} = 0$ for $k \ge 3$.
  1189	  Holds for class $\mathbf{G}$ (Heisenberg); fails for
  1190	  classes $\mathbf{L}$, $\mathbf{C}$, $\mathbf{M}$.
  1191	\item \emph{Convolution algebra formality.}
  1192	  The $L_\infty$ brackets $\ell_k = 0$ for
  1193	  $k \ge 3$ in~$\gAmod$. Equivalent to class~$\mathbf{G}$
  1194	  (Proposition~\ref{prop:sc-formal-iff-class-g}).
  1195	\item \emph{SC-formality.} The Swiss-cheese type
  1196	  operations $m_k^{\mathrm{SC}} = 0$ for $k \ge 3$.
  1197	  Equivalent to class~$\mathbf{G}$.
  1198	\end{enumerate}
  1199	Level (a) guarantees that ordered and symmetric give the
  1200	same answer \emph{as chain complexes} for $\Einf$-chiral
 succeeded in 52ms:
  3165	  $(\Etwo^{\mathrm{top}} \otimes \Eone^{\mathrm{top}} \simeq \Ethree^{\mathrm{top}})$
  3166	  is proved at the \emph{$\infty$-categorical} level
  3167	  \textup{(}Lurie~\cite{HA}\textup{)}.
  3168	\end{enumerate}
  3169	The chain-level gap is at step~\textup{(iv)}: the locally-constant
  3170	recognition requires passing to $Q$-cohomology.  For class~G
  3171	and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
  3172	$k \geq 3$\textup{)}, the chain-level and cohomological
  3173	$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
  3174	where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
  3175	chain-level $\Ethree$ may differ from the cohomological $\Ethree$.
 succeeded in 52ms:
    84	separation.
    85	The algebraic depth $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$
    86	admits no value~$3$ or any finite value $\geq 3$
    87	(Proposition~\ref{prop:depth-gap-trichotomy}).
    88	Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
    89	$k \geq 3$) holds if and only if the algebra belongs to
    90	class~$\mathbf{G}$
    91	(Proposition~\ref{prop:sc-formal-iff-class-g}).
    92	For free-field algebras, the scalar formula
    93	$F_g = \kappa \cdot \lambda_g$ is exact at all genera
    94	(all-weight): the cross-channel correction
exec
/bin/zsh -lc "rg -n \"SC-formal|SC-formality|Swiss-cheese formal|m_k\\"'^'"\\{SC\\} = 0|m_k\\"'^'"\\{\\\\mathrm\\{SC\\}\\} = 0|class~G and~L|class~\\\\mathbf\\{L\\}.*SC\" chapters/theory chapters/frame chapters/connections | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:SC-formal|SC-formality|Swiss-cheese formal|m_k\^\{SC\} = 0|m_k\^\{\mathrm\{SC\}\} = 0|class~G and~L|class~\mathbf\{L\}.*SC)
                                                                         ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n -F "SC-formal" chapters/theory chapters/frame chapters/connections && rg -n -F "SC-formality" chapters/theory chapters/frame chapters/connections && rg -n -F "class~G and~L" chapters/theory chapters/frame chapters/connections' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:2606:a chiral algebra in the standard landscape is SC-formal if and
chapters/frame/heisenberg_frame.tex:110:shadow depth~$2$, tower terminates, SC-formal. The bar construction
chapters/theory/en_koszul_duality.tex:3171:and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
chapters/theory/e1_modular_koszul.tex:1195:\item \emph{SC-formality.} The Swiss-cheese type
chapters/theory/chiral_koszul_pairs.tex:86:(Heisenberg and its relatives) is SC-formal
chapters/theory/chiral_koszul_pairs.tex:2511:relationship between SC-formality and the classification is
chapters/theory/chiral_koszul_pairs.tex:2515:algebra outside class~$G$ can be SC-formal. The answer
chapters/theory/chiral_koszul_pairs.tex:2521:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:2524:\index{class G@class~$G$!characterised by SC-formality}
chapters/theory/chiral_koszul_pairs.tex:2533:SC-formal\textup{)} is established in
chapters/theory/chiral_koszul_pairs.tex:2539:For the converse, suppose~$\cA$ is SC-formal.
chapters/theory/chiral_koszul_pairs.tex:2548: \text{SC-formal}
chapters/theory/chiral_koszul_pairs.tex:2571:brackets; SC-formality is incompatible with each. The only
chapters/connections/concordance.tex:7074: & SC-formality characterises class~$\mathbf{G}$:
chapters/connections/concordance.tex:9647:& SC-formality $\iff$ class~$\mathbf{G}$
chapters/theory/e1_modular_koszul.tex:1195:\item \emph{SC-formality.} The Swiss-cheese type
chapters/theory/chiral_koszul_pairs.tex:2511:relationship between SC-formality and the classification is
chapters/theory/chiral_koszul_pairs.tex:2521:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:2524:\index{class G@class~$G$!characterised by SC-formality}
chapters/theory/chiral_koszul_pairs.tex:2571:brackets; SC-formality is incompatible with each. The only
exec
/bin/zsh -lc "rg -n -F \"free fermion\" chapters | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 200

chapters/examples/w_algebras_deep.tex:2632:trivial: ghosts are free fermions with
chapters/examples/w_algebras_deep.tex:3766:\item \emph{Gaussian} (Heisenberg, lattice VOA, free fermion):
chapters/examples/w_algebras_deep.tex:5201:$\kappa(\psi\bar\psi) = 1/2$ (complex free fermion),
chapters/examples/lattice_foundations.tex:71:level~$1$ is $V_{Q}$ for the root lattice $Q$; the free fermion
chapters/examples/lattice_foundations.tex:4493:(Heisenberg, lattice, free fermion) where every Koszul pair is
chapters/examples/beta_gamma.tex:429:coalgebra of the free fermion system. Since the $\beta\gamma$--fermion
chapters/examples/beta_gamma.tex:446:\subsection{Main result: Koszul duality with free fermions}
chapters/examples/beta_gamma.tex:450:\index{Koszul duality!beta-gamma vs.\ free fermion@$\beta\gamma$ vs.\ free fermion|textbf}
chapters/examples/beta_gamma.tex:539:\begin{theorem}[Koszul dual of the free fermion; \ClaimStatusProvedHere]
chapters/examples/beta_gamma.tex:541:The Koszul dual algebra of the free fermion is the $\beta\gamma$ system:
chapters/examples/beta_gamma.tex:590:The Koszul dual algebra of the $\beta\gamma$ system is the free fermion ($bc$ ghost system):
chapters/examples/beta_gamma.tex:602:\emph{Step~3.} This defines the $bc$ ghost system (free fermions with two generators).
chapters/examples/beta_gamma.tex:659:There is a physics ``bosonization'' map relating $\beta\gamma$ and free fermions at the level of 
chapters/examples/landscape_census.tex:1777:closed-form generating functions (Heisenberg, free fermion, $bc$,
chapters/examples/landscape_census.tex:1997: The Heisenberg and free fermion Koszul duals grow
chapters/examples/landscape_census.tex:2080:Among the Koszul chiral algebras in Table~\textup{\ref{tab:bar-dimensions}}, the Koszul dual Hilbert function $\dim (\cA^!)_n$ grows sub-exponentially if and only if $\cA$ is a free field (Heisenberg or free fermion) or affine $\widehat{\mathfrak{sl}}_2$ (which has linear growth $2n{+}1$). All other interacting algebras (higher-rank Kac--Moody, Virasoro, $\mathcal{W}_3$, $bc$, $\beta\gamma$, Yangian) have exponential growth.
chapters/examples/landscape_census.tex:2084:The Heisenberg and free fermion dimensions are $p(n-2)$ and $p(n-1)$ respectively, both sub-exponential by Hardy--Ramanujan asymptotics ($p(n) \sim e^{\pi\sqrt{2n/3}}/(4\sqrt{3}\,n)$). The affine $\widehat{\mathfrak{sl}}_2$ has $\dim H^n = 2n+1$, linear in~$n$ (Remark~\ref{rem:garland-lepowsky-sl2}). All other interacting entries in the table grow exponentially: $2^n$ for $bc$, $3^n$ for $\beta\gamma$ and Virasoro (Remark~\ref{rem:bar-growth-koszul}). The Heisenberg and free fermion are the unique free-field (non-interacting) algebras among the computed examples: they have no nontrivial OPE beyond the central term.
chapters/examples/landscape_census.tex:2090:For every interacting algebra in Table~\textup{\ref{tab:bar-dimensions}} with a known closed-form generating function, that function is algebraic over $\mathbb{Q}(x)$. (The free-field algebras, Heisenberg and free fermion, have transcendental partition-graded generating functions $\prod(1-x^k)^{-1}$, though their conformal-weight-graded series are rational.) For interacting algebras, this algebraicity is a consequence of the Koszul property: the bar spectral sequence collapse at $E_2$ (Theorem~\ref{thm:spectral-sequence-collapse}) constrains the generating function to satisfy a polynomial equation.
exec
/bin/zsh -lc "rg -n -F \"SC-formal\" chapters/examples chapters/theory chapters/frame | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"lattice VOA\" chapters | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:2606:a chiral algebra in the standard landscape is SC-formal if and
chapters/frame/heisenberg_frame.tex:110:shadow depth~$2$, tower terminates, SC-formal. The bar construction
chapters/theory/en_koszul_duality.tex:3171:and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
chapters/theory/e1_modular_koszul.tex:1195:\item \emph{SC-formality.} The Swiss-cheese type
chapters/theory/chiral_koszul_pairs.tex:86:(Heisenberg and its relatives) is SC-formal
chapters/theory/chiral_koszul_pairs.tex:2511:relationship between SC-formality and the classification is
chapters/theory/chiral_koszul_pairs.tex:2515:algebra outside class~$G$ can be SC-formal. The answer
chapters/theory/chiral_koszul_pairs.tex:2521:\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:2524:\index{class G@class~$G$!characterised by SC-formality}
chapters/theory/chiral_koszul_pairs.tex:2533:SC-formal\textup{)} is established in
chapters/theory/chiral_koszul_pairs.tex:2539:For the converse, suppose~$\cA$ is SC-formal.
chapters/theory/chiral_koszul_pairs.tex:2548: \text{SC-formal}
chapters/theory/chiral_koszul_pairs.tex:2571:brackets; SC-formality is incompatible with each. The only
 succeeded in 52ms:
Total output lines: 200

chapters/examples/w_algebras_deep.tex:3766:\item \emph{Gaussian} (Heisenberg, lattice VOA, free fermion):
chapters/examples/lattice_foundations.tex:40:\begin{remark}[Three-pillar interpretation: lattice VOAs]
chapters/examples/lattice_foundations.tex:42:\index{lattice VOA!three-pillar interpretation}
chapters/examples/lattice_foundations.tex:72:is a subalgebra of a rank-$1$ lattice VOA; W-algebras arise
chapters/examples/lattice_foundations.tex:75:\begin{remark}[Four-level structure: lattice VOA]
chapters/examples/lattice_foundations.tex:77:The lattice VOA illustrates the four levels of the modular engine:
chapters/examples/lattice_foundations.tex:109:\index{lattice VOA!sewing envelope|textbf}%
chapters/examples/lattice_foundations.tex:114:\item The lattice VOA\/ $V_\Lambda$ satisfies HS-sewing for
chapters/examples/lattice_foundations.tex:482:\index{lattice VOA|textbf}
chapters/examples/lattice_foundations.tex:762:\index{bar complex!lattice VOA}
chapters/examples/lattice_foundations.tex:916:\index{self-dual!lattice VOA}
chapters/examples/lattice_foundations.tex:950:\index{Koszul dual!lattice VOA}
chapters/examples/lattice_foundations.tex:1040:\index{Koszul dual!lattice VOA!kappa landscape}%
chapters/examples/lattice_foundations.tex:1104:\index{Koszul dual!lattice VOA!structural identification}%
chapters/examples/lattice_foundations.tex:1118: The lattice VOA $\Vlat_\bZ = \cH_1$ is
chapters/examples/lattice_foundations.tex:1158: The Leech lattice VOA
chapters/examples/lattice_foundations.tex:1345:\begin{definition}[Twisted module for lattice VOA]\label{def:twisted-module-lattice}
chapters/examples/lattice_foundations.tex:1346:For a coset $\gamma \in \Lambda^*/\Lambda$, the \emph{$\gamma$-twisted module} for the lattice VOA $\Vlat_\Lambda$ is:

thinking
**Inspecting free fermions**

The search results are quite extensive! I think we have enough examples of class G that includes free fermions or lattices elsewhere. It might be helpful to inspect the free_fields lines specifically related to the free fermion class G. I’ll focus on lines around 209-225 to get more context. This should clarify things for me! Let’s see what insights I can uncover from that section.
exec
/bin/zsh -lc "nl -ba chapters/examples/lattice_foundations.tex | sed -n '1670,1698p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '205,235p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2428,2447p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1670	\label{thm:lattice:niemeier-shadow-universality}%
  1671	\index{Niemeier lattice!shadow universality}%
  1672	\index{shadow tower!class G universality}%
  1673	Let $\Lambda$ be any of the twenty-four Niemeier lattices. Then:
  1674	\begin{enumerate}[label=\textup{(\roman*)}]
  1675	\item $\kappa(V_\Lambda) = \operatorname{rank}(\Lambda) = 24$
  1676	for all twenty-four lattices.
  1677	\item $S_r(V_\Lambda) = 0$ for all $r \geq 3$: every Niemeier
  1678	lattice VOA is class~$\mathbf{G}$ with shadow depth~$2$.
  1679	\item The genus-$g$ scalar amplitude is
  1680	$F_g(V_\Lambda) = 24\,\lambda_g^{\mathrm{FP}}$ for all $g \geq 1$,
  1681	identical for all twenty-four lattices. In particular,
  1682	\begin{equation}\label{eq:niemeier-genus-amplitudes}
  1683	F_1 = 1,\qquad
  1684	F_2 = \tfrac{7}{240},\qquad
  1685	F_3 = \tfrac{31}{40320},\qquad
  1686	F_4 = \tfrac{127}{6451200}.
  1687	\end{equation}
  1688	\item The planted-forest correction vanishes:
  1689	$\delta_{\mathrm{pf}}^{(g,0)}(V_\Lambda) = 0$ for all $g \geq 2$,
 succeeded in 51ms:
   205	\subsubsection{Shadow obstruction tower of the free fermion}
   206	\label{sec:fermion-shadow-tower}%
   207	\index{free fermion!shadow obstruction tower}%
   208	
   209	The free fermion is the Gaussian archetype in its purest form. The
   210	Heisenberg algebra achieves class~G through \emph{commutativity}: the
   211	double pole generates only symmetric bar elements, and the absence of
   212	a simple pole kills the cubic shadow. The free fermion achieves class~G
   213	through \emph{antisymmetry}: the simple pole would produce a cubic
   214	shadow in a bosonic algebra, but fermionic statistics force $S_3 = 0$
   215	because cyclic permutations on three-point configuration space forms
   216	act by cube roots of unity (proof:
   217	Theorem~\ref{thm:fermion-bar-complex-genus-0}, degree~$2$). The two
   218	mechanisms are complementary, and both produce the same outcome: the
   219	shadow obstruction tower terminates at degree~$2$.
   220	
   221	\begin{proposition}[Shadow invariants of the free fermion;
   222	\ClaimStatusProvedHere]
   223	\label{prop:fermion-shadow-invariants}
   224	\index{free fermion!shadow invariants}
 succeeded in 51ms:
  2428	\textbf{Class}
  2429	& \textbf{Families}
  2430	& $m_3^{\mathrm{SC}}$
  2431	& $m_4^{\mathrm{SC}}$
  2432	& $m_k^{\mathrm{SC}},\; k \geq 5$ \\
  2433	\midrule
  2434	$G$ \textup{(}$r_{\max}=2$\textup{)}
  2435	& Heisenberg
  2436	& $= 0$
  2437	& $= 0$
  2438	& $= 0$ \\
  2439	$L$ \textup{(}$r_{\max}=3$\textup{)}
  2440	& affine KM, lattice VOA
  2441	& $\neq 0$
  2442	& $= 0$
  2443	& $= 0$ \\
  2444	$C$ \textup{(}$r_{\max}=4$\textup{)}
  2445	& $\beta\gamma$
  2446	& $= 0$
  2447	& $\neq 0$




thinking
**Explaining proof strategies**

I'm considering class C as a boundary or counterexample to proof strategy, but it doesn’t align with the theorem statement. It looks like there’s a hidden assumption failure here. Similarly, class G with free fermions gets S3=0 through antisymmetry, not through an abelian bracket. This is interesting since it highlights the different approaches in these classes and how they tackle proof strategies. I’m wondering how these nuances affect the overall proof context.
thinking
**Evaluating theorem accuracy**

I’m noticing that the citation about "self-duality or Lagrangian complementarity" doesn't actually appear in the theorem. This seems to be a direct false citation, which feels like a critical issue. I wonder if I should check the metadata dependency graphs for context. It might not be necessary, but reviewing the `claims.jsonl` or looking for line number mismatches in the theorem registry could also be helpful.
thinking
**Clarifying chiral algebras**

I see there's a mix-up in my understanding: not every chiral algebra fits the definition of a current algebra with a Lie bracket. The beta-gamma, free fermion, and lattice theories with operator product expansions (OPE) don't always conform to the current algebra bracket model. I need to confirm this with specific examples. For instance, the beta-gamma preface indicates there's no metric and a simple pole, while the free fermion OPE has a simple pole and follows fermionic statistics.
thinking
**Searching for definitions**

I’m noticing that the proposition discusses a standard landscape, but it lacks a precise definition in the file. It seems to imply a hidden hypothesis, and I’m curious about the distinction between generic/non-critical levels and the nonzero Heisenberg level, which aren’t explicitly stated. I think I should search for occurrences of “standard landscape” to find a clearer definition. I might use regex to dive deeper into this.
exec
/bin/zsh -lc "rg -n \"standard landscape\" chapters/theory chapters/frame | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/preface_sections10_13_draft.tex:345:bridge theorem, so the entire standard landscape enters through two
chapters/frame/preface_sections10_13_draft.tex:537:the standard landscape for all seven families, and the genus-$2$ and
chapters/frame/preface.tex:319:(the entire standard landscape), the two theories agree; for
chapters/frame/preface.tex:1098:classifies the standard landscape into four shadow-depth classes
chapters/frame/preface.tex:2541:The standard landscape partitions into four classes
chapters/frame/preface.tex:2606:a chiral algebra in the standard landscape is SC-formal if and
chapters/frame/preface.tex:2615:$d_{\mathrm{alg}}\ge 3$ is realized on the standard landscape
chapters/frame/preface.tex:2732:Every algebra in the standard landscape is either primitive
chapters/frame/preface.tex:2742:\section*{7.\quad The standard landscape}
chapters/frame/preface.tex:3313:point). Scope: every family in the standard landscape at all
chapters/frame/preface.tex:3668:For $\Einf$-chiral algebras (the entire standard landscape:
chapters/frame/preface.tex:4078:bridge theorem, so the entire standard landscape enters through two
chapters/frame/preface_sections5_9_draft.tex:350:The standard landscape partitions into four classes
chapters/frame/preface_sections5_9_draft.tex:500:Every algebra in the standard landscape is either primitive
chapters/frame/preface_sections5_9_draft.tex:510:\section*{7.\quad The standard landscape}
chapters/frame/preface_sections5_9_draft.tex:840:point). Scope: every family in the standard landscape at all
chapters/theory/higher_genus_modular_koszul.tex:720:\ref{MK:verdier} for the standard landscape follows from: (1)~the genus-$0$ bar-cobar Verdier pairing
chapters/theory/higher_genus_modular_koszul.tex:1892:entire CFT-type standard landscape.
chapters/theory/higher_genus_modular_koszul.tex:2001:therefore reduces to a single axiom for the standard landscape:
chapters/theory/higher_genus_modular_koszul.tex:2264:\textup{(}the entire standard landscape except integer-spin $\beta\gamma$, where hypothesis~\textup{(a)} fails\textup{)},

thinking
**Investigating perfectness**

I'm considering the proposition in bar_cobar_adjunction_inversion and its connection to perfectness in the standard landscape. It seems relevant to my proof since there's a claim about a non-degenerate invariant bilinear form, which might be confusing when discussing perfectness of pairing. I think it’s worth examining this in detail to clarify any potential confusion. Let’s take a closer look and see what insights I can find!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2876,3045p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '888,906p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2876	Lagrangian criterion to an unconditional equivalence for the
  2877	standard landscape.
  2878	\end{remark}
  2879	
  2880	\begin{proposition}[Perfectness for the standard landscape]
  2881	\label{prop:lagrangian-perfectness}
  2882	\ClaimStatusProvedHere
  2883	\index{Lagrangian!perfectness verification}
  2884	\index{perfectness!cyclic pairing on complementarity datum}
  2885	Let $\cA$ satisfy the standing hypotheses and the following:
  2886	\begin{enumerate}[label=\textup{(P\arabic*)}]
  2887	\item\label{item:perf-fingen}
  2888	 \textup{(Finite weight spaces)}\quad
  2889	 The conformal weight spaces $\cA_n$ are finite-dimensional for
  2890	 all~$n$, and $\cA_n = 0$ for $n \ll 0$.
  2891	\item\label{item:perf-nondeg}
  2892	 \textup{(Nondegenerate invariant form)}\quad
  2893	 The invariant bilinear form
  2894	 $\langle{-},{-}\rangle \colon \cA \otimes \cA \to \omega_X$
  2895	 restricts to a nondegenerate pairing on each weight space~$\cA_n$.
 succeeded in 51ms:
   888	one of containment: $C_2$-cofinite simple quotients
   889	$L_k(\fg)$ at admissible level satisfy~\textup{(v)} but may
   890	not satisfy~\textup{(iii)}, while Koszul universal algebras
   891	$V^k(\fg)$ at generic level satisfy~\textup{(iii)} but
   892	not~\textup{(v)}.
   893	Every chiral algebra satisfies~\textup{(i)}.
   894	Every positive-energy chiral algebra satisfies
   895	\textup{(i)}--\textup{(ii)}.
   896	The standard landscape \textup{(}Heisenberg, affine
   897	Kac--Moody at non-critical level, $\cW$-algebras at
   898	generic central charge, $\beta\gamma$ and $bc$
   899	systems\textup{)} satisfies levels
   900	\textup{(i)}--\textup{(iv)}; those that are also
   901	$C_2$-cofinite satisfy all five.
   902	\end{theorem}
   903	
   904	\begin{proof}
   905	Level~(i) is Theorem~\ref{thm:mc2-bar-intrinsic}: $D_\cA^2=0$ holds
   906	universally because the bar differential is the Feynman-transform







thinking
**Inspecting theoretical foundations**

I need to take a closer look at the exact line in the preface or in higher_genus_foundations to illustrate the standard landscape difference. I think I have this on hand. Another option I noticed is that en_koszul_duality 3171 states that class G and L are SC-formal, which appears to be a more direct contradiction downstream than landscape scope. I might want to include that as a high point in my analysis.
thinking
**Evaluating invariant bilinear forms**

I'm thinking about the proof under audit, which uses `\kappa(x,[y,z])`, identifying it as an invariant bilinear form, unlike `\langle,\rangle`. There's clearly a mismatch here. To be careful, I shouldn't claim that beta-gamma definitely lacks any invariant bilinear form just because we have "no metric, no Sugawara, no Casimir tensor." It’s important to avoid false positives in this reasoning!
thinking
**Considering evidence and scope**

I’m thinking about the class G coverage issue and whether we might actually have better, stronger evidence already. It seems like it could be related to finding 2 or 4. I wonder if we should inspect the exact lines in higher_genus_foundations to clarify the scope. I've already looked into that, but I’m also concerned about the possibility of circular reasoning creeping in. It’s something to keep in mind as I move forward!
thinking
**Considering proof validity**

I'm thinking about a potential argument that claims there's a nondegenerate invariant form, but it seems like the proof is still using incorrect theorems and symbols. Now, do I need to prove there's no other valid proof? Maybe not, since the user's question is specifically about whether the cited lemmas actually proved what they claim. It’s all a bit tangled, but I'll focus on the user's request!
thinking
**Evaluating potential theorems**

I'm considering whether another theorem could be helpful since the cited theorem doesn't seem to apply. I want to avoid false positives from hidden assumptions, so it’s important to mention that the nondegeneracy hypothesis might exist elsewhere but isn't part of the cited result. I need to check the `prop:swiss-cheese-nonformality-by-class` proof, specifically looking at `thm:riccati-algebraicity` for class C and factors affecting class M. I'm wondering if we need to trace every step or if our main findings already indicate an incomplete direction due to class drift.
thinking
**Analyzing class characteristics**

I've realized that since class C has m3=0, any claim that this vanishing characterizes class G can be challenged with a counterexample. I can frame `beta gamma` as a counterexample to remark 16653-16657, which is a strong position. I'm considering if there's a counterexample to the converse of a theorem, especially since class G involves free fermions and lattices, while the proof only mentions Heisenberg. It’s essential to verify whether the free fermion has SC-formality in class G without an abelian bracket. I need to find an explicit supporting line for this.
thinking
**Searching for free fields**

I think I should search for `free_fields` specifically looking for m_k^{SC}. This might help clarify things or reveal useful insights that relate to my previous thoughts. I’m curious about the potential findings, as they could provide some context or confirmation I need. It’s a little vague, but it could lead to a more detailed understanding of the SC aspect related to free fields. Let’s see what I can uncover!
exec
/bin/zsh -lc 'rg -n -F "m_k''^{'"\\mathrm{SC}}\" chapters/examples/free_fields.tex chapters/examples/lattice_foundations.tex chapters/examples/free_fields.tex chapters/examples/bar_complex_tables.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc "rg -n -F \"SC-formal\" chapters/examples chapters/frame | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface.tex:2606:a chiral algebra in the standard landscape is SC-formal if and
chapters/frame/heisenberg_frame.tex:110:shadow depth~$2$, tower terminates, SC-formal. The bar construction


thinking
**Clarifying SC-formality**

I’m trying to understand what “SC-formality” means, but it looks like I’m only seeing prose examples without a formal definition. That makes me wonder if it’s more of a low or medium level of formality in writing. I’ll need to dig deeper to find more structured explanations or references. There’s definitely something here worth exploring further to get a clearer picture!
thinking
**Analyzing proof requirements**

I’m considering whether it’s acceptable to use SC-formality to signify `m_k^{SC}=0` for k≥3 directly on A, instead of focusing on bar cohomology, as mentioned in those file lines. I think discussing any arising issues from this approach would probably satisfy the requirements. It seems like no low finding is needed here. Now I want to think about how to order the severity of any issues related to this.
codex
I have enough evidence to re-check the surviving findings directly against source before I report. The remaining work is just falsifier verification: exact lines, no extrapolation.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2525,2565p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2434,2446p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16402,16418p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3169,3174p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '896,899p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16653,16705p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2525	Let~$\cA$ be a chiral algebra in the standard landscape.
  2526	Then~$\cA$ is Swiss-cheese formal
  2527	\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
  2528	if and only if~$\cA$ belongs to class~$G$.
  2529	\end{proposition}
  2530	
  2531	\begin{proof}
  2532	The forward direction \textup{(}class~$G$ $\Longrightarrow$
  2533	SC-formal\textup{)} is established in
  2534	Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
  2535	the Heisenberg bracket $[a_m, a_n] = km\,\delta_{m+n,0}$ is
  2536	central, so all nested brackets vanish and
  2537	$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
  2538	
  2539	For the converse, suppose~$\cA$ is SC-formal.
  2540	The cubic shadow $S_3$ is the normalized projection of the
  2541	trilinear form
  2542	\[
  2543	 C(x,y,z) \;=\; \kappa\bigl(x, [y,z]\bigr),
  2544	\]
 succeeded in 52ms:
  2434	$G$ \textup{(}$r_{\max}=2$\textup{)}
  2435	& Heisenberg
  2436	& $= 0$
  2437	& $= 0$
  2438	& $= 0$ \\
  2439	$L$ \textup{(}$r_{\max}=3$\textup{)}
  2440	& affine KM, lattice VOA
  2441	& $\neq 0$
  2442	& $= 0$
  2443	& $= 0$ \\
  2444	$C$ \textup{(}$r_{\max}=4$\textup{)}
  2445	& $\beta\gamma$
  2446	& $= 0$
 succeeded in 51ms:
 16402	\item \emph{Gaussian \textup{(}$\mathbf{G}$, $r_{\max} = 2$\textup{)}:}
 16403	 Heisenberg $\cH_c$, lattice VOA $V_\Lambda$, free fermion.
 16404	 All higher obstruction classes vanish:
 16405	 $o_r(\cA) = 0$ for $r \geq 3$. The complementarity potential is
 16406	 exactly quadratic.
 16407	
 16408	\item \emph{Lie \textup{(}$\mathbf{L}$, $r_{\max} = 3$\textup{)}:}
 16409	 Affine Kac--Moody $V_k(\fg)$ at generic level.
 16410	 The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
 16411	 \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
 16412	 quartic obstruction $o_4 = 0$ by the Jacobi identity.
 16413	
 16414	\item \emph{Contact \textup{(}$\mathbf{C}$, $r_{\max} = 4$\textup{)}:}
 16415	 $\beta\gamma$ system on the weight-changing line.
 16416	 The quartic shadow $\mathfrak{Q}_{\beta\gamma} =
 16417	 \operatorname{cyc}(m_3) \neq 0$, but $o_5 = 0$ by rank-one
 16418	 abelian rigidity
 succeeded in 51ms:
  3169	The chain-level gap is at step~\textup{(iv)}: the locally-constant
  3170	recognition requires passing to $Q$-cohomology.  For class~G
  3171	and~L algebras \textup{(}SC-formal: $m_k^{\mathrm{SC}} = 0$ for
  3172	$k \geq 3$\textup{)}, the chain-level and cohomological
  3173	$\Ethree$ agree.  For class~M \textup{(}Virasoro, $\cW$-algebras\textup{)},
  3174	where SC non-formality means all $m_k^{\mathrm{SC}}$ are nontrivial, the
 succeeded in 50ms:
   896	The standard landscape \textup{(}Heisenberg, affine
   897	Kac--Moody at non-critical level, $\cW$-algebras at
   898	generic central charge, $\beta\gamma$ and $bc$
   899	systems\textup{)} satisfies levels
 succeeded in 51ms:
 16653	The GKW formality/non-formality dichotomy is the genus-$0$,
 16654	degree-$3$ projection of the shadow depth classification:
 16655	it detects whether the cubic Swiss-cheese operation $m_3^{\mathrm{SC}}$
 16656	vanishes, which separates class~$\mathbf{G}$ from
 16657	$\{\mathbf{L}, \mathbf{C}, \mathbf{M}\}$.
 16658	The shadow obstruction tower extends this to all genera and degrees:
 16659	the quartic discriminant $\Delta$ distinguishes $\mathbf{C}$
 16660	from~$\mathbf{M}$, and the all-genera MC equation
 16661	$D \cdot \Theta + \tfrac{1}{2}[\Theta, \Theta] = 0$
 16662	(Theorem~\ref{thm:mc2-bar-intrinsic})
 16663	governs the complete tower from which GKW's consistency
 16664	conditions are the genus-$0$ projections.
 16665	Computational verification:
 16666	\texttt{compute/lib/theorem\_shadow\_depth\_gkw\_engine.py}
 16667	($78$~tests).
 16668	\end{remark}
 16669	
 16670	\begin{proposition}[Swiss-cheese formality classification by shadow class;
 16671	\ClaimStatusProvedHere]
 16672	\label{prop:sc-formality-by-class}
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '2932,2938p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '209,218p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/lattice_foundations.tex | sed -n '1675,1679p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3029,3034p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2627,2640p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2932	$\beta\gamma$ system at weights $(\lambda, 1{-}\lambda)$ has
  2933	only a simple pole: $\beta(z)\gamma(w) \sim 1/(z{-}w)$. No
  2934	double pole means no metric, no Sugawara construction, no
  2935	Casimir tensor. The collision residue $r(z)$ is a constant
  2936	propagator~$P$, pole order zero after $d\log$-absorption.
  2937	$\kappa(\beta\gamma) = 1$.
  2938	
 succeeded in 51ms:
   209	The free fermion is the Gaussian archetype in its purest form. The
   210	Heisenberg algebra achieves class~G through \emph{commutativity}: the
   211	double pole generates only symmetric bar elements, and the absence of
   212	a simple pole kills the cubic shadow. The free fermion achieves class~G
   213	through \emph{antisymmetry}: the simple pole would produce a cubic
   214	shadow in a bosonic algebra, but fermionic statistics force $S_3 = 0$
   215	because cyclic permutations on three-point configuration space forms
   216	act by cube roots of unity (proof:
   217	Theorem~\ref{thm:fermion-bar-complex-genus-0}, degree~$2$). The two
   218	mechanisms are complementary, and both produce the same outcome: the
 succeeded in 51ms:
  1675	\item $\kappa(V_\Lambda) = \operatorname{rank}(\Lambda) = 24$
  1676	for all twenty-four lattices.
  1677	\item $S_r(V_\Lambda) = 0$ for all $r \geq 3$: every Niemeier
  1678	lattice VOA is class~$\mathbf{G}$ with shadow depth~$2$.
  1679	\item The genus-$g$ scalar amplitude is
 succeeded in 51ms:
  3029	In particular, this applies unconditionally to every algebra in the
  3030	standard landscape at non-critical, non-degenerate levels:
  3031	Heisenberg at $k \neq 0$, affine Kac--Moody $V_k(\fg)$ at
  3032	$k \neq -h^\vee$, Virasoro at generic~$c$, principal
  3033	$\mathcal{W}$-algebras at non-critical level, and all free-field
  3034	families $bc$, $\beta\gamma$.
 succeeded in 51ms:
  2627	\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
  2628	\label{thm:modular-characteristic}
  2629	\index{modular characteristic theorem|textbf}
  2630	\index{kappa@$\kappa$!as first characteristic number|textbf}
  2631	\textup{[}Regime: curved-central
  2632	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  2633	
  2634	Let $\cA$ be a modular Koszul chiral algebra
  2635	(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
  2636	characteristic package
  2637	(Definition~\ref{def:scalar-modular-package}) is controlled by one
  2638	number, the genus-$1$ curvature coefficient
  2639	$\kappa(\cA) \in \mathbb{C}$. More precisely:
  2640	


thinking
**Considering report structure**

I’m pondering the inclusion of free fermion or lattice VOA, but it seems like I shouldn’t focus on current algebras. I think it’s good that the proof isn’t within the claimed domain. For the final report, I want it to be concise, highlighting findings first. Maybe I'll present each finding as a single bullet point with a short description. The contract specifies lines, so I need to ensure I include 4-5 findings and prioritize them by severity, while also using file and line references.
thinking
**Clarifying SC-formality**

I need to be more precise about what SC-formality means. According to chiral_koszul_pairs 81-87, SC-formality is defined by the condition m_k^{SC}=0 for k>=3 in the Swiss-cheese bar complex. That's a solid point! I could also cite `higher_genus_modular_koszul 16686-16688`, but keeping the focus on the low cases is fine. I've checked 16 instances and found 6 violations, which results in a FAIL. Before finalizing, I might want to update the completed plan.
Plan update
The theorem surface, dependencies, and downstream duplicates were checked. Surviving findings were re-verified directly against source passages.
  ✓ Read audit workflow and repo-wide claim-status context relevant to SC-formality
  ✓ Locate the SC-formality theorem, definition, and proof surface in chapters/
  ✓ Trace every cited dependency and verify each proof step, scope, and boundary case
  ✓ Re-verify findings against file contents and produce severity-ordered report

thinking
**Considering summary structure**

I’m thinking about how to handle the summaries. There was no direct circularity found, but there were issues with dependencies, and the contract only specifies the exact line. Should I add a short sentence, or maybe append after the summary? The contract says to end with the summary, so maybe not. Checking the line count, I see about 5 bullets with 10 lines each; I need to compress to keep things concise. Let’s aim for 5 findings, each with 2-3 lines.
codex
- [CRITICAL] [chapters/theory/chiral_koszul_pairs.tex:2539](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2539) — The converse proof is not valid on its stated domain. Here `SC-formal` means `m_k^{\mathrm{SC}}=0` for all `k>=3` ([chiral_koszul_pairs.tex:2525](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2525)), but the proof then treats every standard-landscape algebra as having a current-algebra bracket and an invariant bilinear form `C(x,y,z)=\kappa(x,[y,z])`, and cites `thm:modular-characteristic` for nondegeneracy. That theorem only defines the scalar `\kappa(\cA)\in\mathbb C` ([higher_genus_modular_koszul.tex:2627](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2627)), not a bilinear form; meanwhile the same manuscript says `\beta\gamma` has “no metric, no Sugawara construction, no Casimir tensor” ([preface.tex:2932](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2932)). The step `S_3=0 => [y,z]=0` is therefore unsupported and object-conflating.

- [CRITICAL] [chapters/theory/chiral_koszul_pairs.tex:2532](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2532) — The forward implication is outsourced to `prop:swiss-cheese-nonformality-by-class`, but that dependency only proves the Heisenberg case and conflicts with the manuscript’s own class data. Its table puts only Heisenberg in class `G` and even places “lattice VOA” in class `L` ([chiral_koszul_pairs.tex:2434](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2434)), while the shadow-archetype theorem puts lattice VOAs and free fermions in class `G` ([higher_genus_modular_koszul.tex:16402](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16402)); see also [lattice_foundations.tex:1677](/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1677) and [free_fields.tex:209](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:209). As written, `class G => SC-formal` is not proved for the full class-`G` surface being claimed.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:16653](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16653) — A nearby remark says vanishing of `m_3^{\mathrm{SC}}` separates class `G` from `{L,C,M}`, but the very next classification table says class `C` has `m_3^{\mathrm{SC}}=0` and `m_4^{\mathrm{SC}}\neq0` ([higher_genus_modular_koszul.tex:16702](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16702)); the local table in [chiral_koszul_pairs.tex:2444](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2444) says the same. So the manuscript itself supplies a counterexample (`\beta\gamma`) to the claim that cubic vanishing isolates class `G`.

- [HIGH] [chapters/theory/en_koszul_duality.tex:3170](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3170) — Downstream propagation is contradictory. This chapter states “For class `G` and `L` algebras (SC-formal: `m_k^{\mathrm{SC}}=0` for `k>=3`)...”, which directly contradicts the audited proposition ([chiral_koszul_pairs.tex:2525](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2525)) and the concordance summary ([concordance.tex:7073](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7073), [concordance.tex:9647](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:9647)). The claim surface is not stable across the volume.

- [MEDIUM] [chapters/theory/chiral_koszul_pairs.tex:2525](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2525) — The scope term “standard landscape” is not locked. One definition uses Heisenberg, affine KM at non-critical level, `\mathcal W` at generic central charge, and `\beta\gamma/bc` ([higher_genus_foundations.tex:896](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:896)); the preface class table includes free fermion in class `G` ([preface.tex:2556](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2556)); and the perfectness corollary adds the extra qualifier “non-critical, non-degenerate levels” ([bar_cobar_adjunction_inversion.tex:3029](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3029)). The theorem relies on these hidden qualifications but does not state them.

## Summary
Instances checked: 16 | Violations found: 5 | Verdict: FAIL
tokens used
120,624
