# F15_hidden_imports_hg_comp (783s)

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:205](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:205) — PROBLEM: `\sigma` on `\mathbf C_g(\cA)=R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\cA))` is declared to come from `thm:verdier-bar-cobar`, but [chapters/theory/cobar_construction.tex:1313](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1313) is a genus-0 bar/cobar Verdier theorem on configuration-space objects, not a cochain-level involution on the genus-`g` center local system. FIX: Move Definition `def:complementarity-complexes` after `lem:verdier-involution-moduli`, or insert a new proposition before line 205 proving that Verdier duality plus Koszul identification induces `\sigma` on `\mathcal Z(\cA)`; cite that proposition instead of `thm:verdier-bar-cobar`.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:378](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:378) — PROBLEM: C0 assumes only “finite-dimensional fiber cohomology” and then invokes `lem:perfectness-criterion`, but [chapters/theory/higher_genus_complementarity.tex:288](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:288) proves perfectness only for the strict flat comparison family `(\barB^{(g)}(\cA),\Dg{g})` under PBW filterability plus finite-dimensional flat fiber cohomology, not for the curved family `R\pi_{g*}\bar B^{(g)}(\cA)`. FIX: Rewrite the theorem statement to use `R\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\cA)` and state both lemma hypotheses explicitly, or add a separate theorem transferring perfectness from the flat model to the curved one via `prop:gauss-manin-uncurving-chain`.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:407](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:407) — PROBLEM: C0 filters the curved fiber complex with `\dfib^{\,2}=\kappa(\cA)\omega_g`, takes ordinary cohomology of it, and then identifies the surviving `H^0` with `\bigoplus_p(\cA^!)_p` “hence with the center”; this violates the chapter’s own curved/flat distinction and contradicts [chapters/theory/chiral_koszul_pairs.tex:940](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:940), which only identifies bar cohomology with the Koszul dual, not with `Z(\cA)`. FIX: Replace Steps 2-4 by a strict-flat proof on `(\barB^{(g)}(\cA),\Dg{g})`, identify `H^0` first with the Koszul dual object, and add a separate cited step for the passage from that object to the center local system.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:552](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:552) — PROBLEM: the first proof of `thm:quantum-complementarity-main` is only a roadmap and ends at line 562; the actual argument starts later in detached proof environments, so the theorem’s `\ClaimStatusProvedHere` does not sit under one continuous proof block. FIX: Convert lines 552-562 into `\begin{remark}[Proof roadmap]...\end{remark}` and start the actual theorem proof at line 665, or keep the theorem proof environment open until line 1827.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:669](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:669) — PROBLEM: Step I invents a “genus filtration” on a single bar complex by summing contributions from varying genera, then proves a Leray statement using the product `\overline C_n(X)\times\overline{\mathcal M}_g\to\overline{\mathcal M}_g` at lines 755-760, and later justifies genus-exhaustiveness by finite bar degree at lines 897-903; these are three different filtrations/objects. FIX: Delete the genus-filtration package and replace it with the actual Leray spectral sequence for the relative Fulton-MacPherson family `\pi_{g,n}:\overline C_n(\mathcal C_g/\overline{\mathcal M}_g)\to\overline{\mathcal M}_g`, or explicitly define a completed all-genus bar object and prove a genuine genus-support filtration before using it.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:822](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:822) — PROBLEM: Step I asserts `d_{\mathrm{fiber}}^2=0` by the genus-0 Arnold relation, but [chapters/theory/higher_genus_foundations.tex:229](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:229) fixes the higher-genus convention `\dfib^{\,2}=\kappa(\cA)\omega_g`; the proof is using the wrong differential. FIX: Replace `d_{\mathrm{fiber}}` by the strict flat comparison differential and cite `thm:quantum-diff-squares-zero`, or restrict the entire Step I argument to the flat case `\kappa(\cA)=0`.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:920](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:920) — PROBLEM: `Q_g(\mathcal A)` is redefined here as `E_\infty^{*,*,g}=\operatorname{gr}^gH^*(\bar B(\mathcal A))`, but Definition `def:complementarity-complexes` already defined `Q_g` as the `\pm1`-eigenspace cohomology of `\sigma`; the lemma explicitly says this is only “anticipating Theorem C”, so the identification is circular. FIX: Rename the spectral-sequence object to `\operatorname{gr}^g H^*(\bar B^{\mathrm{full}}(\mathcal A))` and add a later comparison theorem if you want to identify it with `Q_g`.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:986](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:986) — PROBLEM: `lem:fiber-cohomology-center` fixes one curve `\Sigma_g`, computes with the curved differential `d=d_{\mathrm{coll}}+d_{\mathrm{curv}}`, and then upgrades the result to a sheaf over moduli by saying the OPE is local; no family-over-moduli hypothesis is stated, and ordinary cohomology of the curved complex is again used at lines 1052-1097. FIX: Add the missing family hypothesis on `(\mathcal A,\mathcal A^!)` over the universal curve and rewrite the lemma for the strict flat family `R^0\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\mathcal A)`; if only a pointwise statement is available, downgrade the lemma to a fixed-curve result.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1172](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1172) — PROBLEM: Step II treats `\Omega^*_{\log}` as Verdier self-dual and pairs it with another copy of `\Omega^*_{\log}`, but the repo’s own Verdier surface is [chapters/theory/poincare_duality.tex:170](/Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality.tex:170) plus [chapters/theory/cobar_construction.tex:353](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:353), which pair logarithmic forms with the `j_!`/distributional compact-support dual, not with themselves. FIX: Replace `thm:verdier-duality-config-complete` and `cor:duality-bar-complexes-complete` by citations to `thm:verdier-config` and `lem:verdier-extension-exchange`, and rewrite the bar pairing as `j_*` bar data against the `j_!`/distributional dual.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:1287](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1287) — PROBLEM: `cor:quantum-dual-complete` cites `thm:quantum-complementarity-main` for the genus-0 exception while it is still inside the proof lane of that theorem. FIX: Replace the citation with the explicit genus-0 calculation already written at lines 1785-1789, or cite an earlier genus-0 theorem outside this proof.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1329](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1329) — PROBLEM: `thm:kodaira-spencer-chiral-complete` starts with a fixed chiral algebra on a curve `X`, then silently upgrades to the universal curve `\pi:\mathcal C_g\to\overline{\mathcal M}_g` and `R^q\pi_*^{\mathrm{ch}}\mathcal A` as if `\mathcal A` were already a family over all genus-`g` curves; it also cites `cor:quantum-dual-complete` as if it gave `H^*(\bar B^{(g)}(\mathcal A))\cong H^*(\bar B^{(g)}(\mathcal A^!))^\vee`, which it does not. FIX: Add the missing family-over-moduli hypothesis and restate the theorem entirely in terms of the object actually produced by C0, or cite the corrected Step II duality theorem that genuinely acts on the same complex.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:1553](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1553) — PROBLEM: `lem:center-isomorphism` begins with “Since every `E_\infty`-chiral algebra...”, but the lemma assumes only a chiral Koszul pair; the cited module-duality theorem is [chapters/theory/chiral_koszul_pairs.tex:5287](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:5287), an `E_1` theorem with completeness/conilpotence hypotheses. FIX: Delete the `E_\infty` sentence and apply `thm:e1-module-koszul-duality` directly to the underlying `E_1`-chiral Koszul pair, stating its hypotheses explicitly.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:1913](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1913) — PROBLEM: `prop:lagrangian-eigenspaces` defines `\sigma=\mathbb D\circ\mathrm{KS}`, but `thm:kodaira-spencer-chiral-complete` never constructs a named isomorphism `\mathrm{KS}`; Part (i) also cites “Theorem~C, Step~7” at line 1907 instead of the actual named `lem:center-isomorphism`. FIX: Define `\sigma` via `lem:verdier-involution-moduli`, and replace the proof-step citation with `lem:center-isomorphism`; if a Kodaira-Spencer isomorphism is intended, state and prove it separately before using it.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:1976](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1976) — PROBLEM: `lem:bar-chart-lagrangian-lift` transports the ambient polarization through `R\Gamma(\overline{\mathcal M}_g,R\pi_{g*}\barB^{(g)}(\cA))` and `L_g:=\barB^{(g)}(\cA)[1]`, but C0 only has a plausible strict-flat statement, not one on the curved family. FIX: Replace every occurrence of `\barB^{(g)}(\cA)` in the transport square by the strict flat model `\barB^{(g)}_{\mathrm{flat}}(\cA)` and use `prop:gauss-manin-uncurving-chain` only as the comparison from curved to flat.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:2074](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2074) — PROBLEM: C2 treats `L_g:=\barB^{(g)}(\cA)[1]` as a dg Lie algebra and feeds it to the Kontsevich-Pridham machine, but elsewhere the same higher-genus bar object is curved when `\kappa(\cA)\neq0`; only the strict flat model is an honest dg object. FIX: Redefine `L_g` as `(\barB^{(g)}(\cA),\Dg{g})[1]`, or add an explicit flatness hypothesis `\kappa(\cA)=0` before any dg-Lie or formal-moduli claim.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:200](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:200) — PROBLEM: the chapter states everything over `\overline{\mathcal M}_g` for all `g\ge0`, but the proof later uses `\overline{\mathcal M}_{1,1}` at line 1791 and the DM-stack dimension formula `3g-3` at lines 869-872; the low-genus base is not fixed consistently. FIX: Choose one stable convention and propagate it everywhere: either restrict the unmarked theory to `g\ge2` and add separate low-genus propositions, or replace the low-genus ambient spaces by stable marked stacks and correct the degree shifts.

## Summary
Checked: 10 | Findings: 15 | Verdict: FAIL


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
session id: 019d8648-99fd-7d42-81c1-030593c26725
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

Same: hidden imports for C0/C1/C2 proofs.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers


thinking
**Exploring file dependencies**

I'm thinking we should spawn explorers to gather file dependencies in parallel. However, we still might need to read some files ourselves later. I want to rely on the explorers first for efficiency and not re-search code they cover. The user asks about ground claims in file contents, which makes me rethink: if the explorer reads, is it our actual reading? It feels like using explorers for context and then reading specific files ourselves could be the best approach!
thinking
**Updating and auditing files**

I need to make commentary updates frequently, focusing on auditing the higher_genus_complementarity.tex file. My goal is to inspect it thoroughly and locate any proofs like C0/C1/C2, as well as find hidden imports and unresolved references. There might be unjustified steps too. I want to produce exhaustive findings and exact fixes. It could be a lot to tackle! Maybe I should use subagents or spawn multiple explorers to analyze the dependencies and list any referenced labels or lemmas.
codex
Audit surface is `chapters/theory/higher_genus_complementarity.tex`, with emphasis on the C0/C1/C2 proof lane and any hidden imports, missing definitions, or unjustified steps. I’m loading the repo’s required mathematical context first, then I’ll read the target file and trace every cited dependency before I write findings.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
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
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
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
 succeeded in 52ms:
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
**Planning file reading**

I need to read the target file and might consider using explorer for a dependency map, but shell rg could be better. Since there's no delegated task unless the user explicitly asks, I won’t use subagents, so a straightforward plan seems necessary.

I think I need to update my approach since the context is still developing. I’ll use rg to locate C0/C1/C2 and check the line count and labels in the full file since it may be lengthy.
codex
I’ve loaded the constitutional surfaces and the audit skill. Next I’m reading the target chapter end to end, locating the C0/C1/C2 lane, and tracing every explicit dependency it imports so the findings are pinned to exact lines instead of paraphrase.
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"C0|C1|C2|complementarity|quantum-complementarity-main|ClaimStatus|begin\\{theorem\\}|begin\\{proposition\\}|begin\\{lemma\\}|begin\\{corollary\\}|begin\\{remark\\}|begin\\{definition\\}|\\\\label\\{\" chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    6238 chapters/theory/higher_genus_complementarity.tex
 exited 2 in 52ms:
rg: regex parse error:
    (?:C0|C1|C2|complementarity|quantum-complementarity-main|ClaimStatus|begin\{theorem\}|begin\{proposition\}|begin\{lemma\}|begin\{corollary\}|begin\{remark\}|begin\{definition\}|\label\{)
                                                                                                                                                                                     ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '521,820p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\smallskip\noindent
\textbf{S-level \textup{(}cohomological shadow\textup{)}.}
Setting $\mathcal{H}_g(\cA) := H^*(\overline{\mathcal{M}}_g,
\mathcal{Z}(\cA))$, Lemma~\textup{\ref{lem:involution-splitting}(b)}
gives:
\begin{equation}\label{eq:verdier-symplectic-pairing}
\mathcal{H}_g(\cA) \;=\;
Q_g(\cA) \;\oplus\; Q_g(\cA^!),
\end{equation}
where the cohomological shadows
$Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
\textup{(}Definition~\textup{\ref{def:complementarity-complexes}}\textup{)}
are the $\pm 1$ eigenspaces of~$\sigma$.
For $g \geq 1$, they are Lagrangians for the induced pairing
on~$\mathcal{H}_g$, and
\begin{equation}\label{eq:quantum-duality}
Q_g(\cA) \cong Q_g(\cA^!)^\vee.
\end{equation}
At genus $0$, the unique point class is $\sigma$-fixed, so
exec
/bin/zsh -lc "sed -n '261,520p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 52ms:
\hookrightarrow V$ is a quasi-isomorphism by direct-sum decomposition,
and $\operatorname{im}(p^\pm) \simeq \operatorname{fib}(\sigma \mp \mathrm{id})$
via the standard cone identification.
Part~(b) follows by applying $H^*$ to~(a).
Part~(c): for $x, y \in V^+$ we have $\sigma x = x$, $\sigma y = y$,
so $\langle x, y \rangle = \langle \sigma x, \sigma y \rangle
= -\langle x, y \rangle$, hence $\langle x, y \rangle = 0$.
Maximality is immediate from the direct-sum decomposition.
\end{proof}

\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
\index{bar complex!relative fiber|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
\[
\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
\overline{\mathcal{M}}_g
\]
be the family of genus-$g$ compactified configuration spaces
carrying the relative bar complex $\bar{B}^{(g)}(\cA)$.
Its stalk at $[\Sigma] \in \overline{\mathcal{M}}_g$ is the
codex
The chapter is large and the first 800 lines already expose a structural problem: the proof lane mixes a local C0 theorem with a second “proof” architecture that appears to restart the chapter from first principles. I’m mapping the label graph now so I can separate foundational defects from mere exposition noise.
exec
/bin/zsh -lc 'rg -n "thm:fiber-center-identification|thm:quantum-complementarity-main|thm:shifted-symplectic-complementarity|thm:ss-quantum|lem:quantum-ss-convergence|lem:genus-filtration|prop:gauss-manin-uncurving-chain|thm:verdier-duality-config-complete|thm:kodaira-spencer-chiral-complete|prop:model-independence|prop:ptvv-lagrangian|thm:verdier-bar-cobar|cor:bar-cohomology-koszul-dual|thm:chiral-koszul-duality|thm:ambient-d-squared-zero|thm:mc2-bar-intrinsic|thm:arnold-three|def:geometric-bar|conv:higher-genus-differentials|def:modular-koszul-chiral|conv:regime-tags|conv:proof-architecture|conv:hms-levels" chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
39:(Theorem~\ref{thm:quantum-complementarity-main}).
50: \textup{(}Proposition~\textup{\ref{prop:gauss-manin-uncurving-chain}}\textup{)}.
57: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
78: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
207:(Theorem~\ref{thm:verdier-bar-cobar}).
224:\begin{remark}[H/M/S layers; Convention~\ref{conv:hms-levels}]
285:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
295:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
303:Convention~\textup{\ref{conv:higher-genus-differentials}}.
313: Definition~\textup{\ref{def:modular-koszul-chiral})}.
372:\label{thm:fiber-center-identification}
375:\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
379:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
437:(Corollary~\ref{cor:bar-cohomology-koszul-dual}).
456:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
459:(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
477:\label{thm:quantum-complementarity-main}
482:\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
487:its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
555:Step~I (\S\ref{lem:genus-filtration}ff.) constructs the spectral
exec
/bin/zsh -lc "rg -n \"begin\\{theorem\\}|begin\\{lemma\\}|begin\\{proposition\\}|begin\\{proof\\}|end\\{proof\\}|ClaimStatus\" chapters/theory/higher_genus_complementarity.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
234:\begin{lemma}[Involution splitting in characteristic~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
256:\begin{proof}
269:\end{proof}
288:\begin{lemma}[Perfectness criterion for the strict flat relative bar family;
289:\ClaimStatusProvedHere]
327:\begin{proof}
369:\end{proof}
371:\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
396:\begin{proof}
450:\end{proof}
476:\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
552:\begin{proof}
562:\end{proof}
665:\begin{proof}[Step I: Steps 1-4]
669:\begin{lemma}[Genus filtration; \ClaimStatusProvedHere]
683:\begin{proof}[Proof of Lemma~\ref{lem:genus-filtration}]
711:\end{proof}
724:\begin{theorem}[Spectral sequence for quantum corrections; \ClaimStatusProvedHere]
748:\begin{proof}[Proof of Theorem~\ref{thm:ss-quantum}]
806:\end{proof}

thinking
**Addressing proof structure**

I’m noticing the issue here is that the proof isn't self-contained, which means I need to ensure everything is properly referred to. I could either keep the theorem proof open until it's fully complete or change line 552 to a "Proof roadmap," which would downgrade the theorem status until the proof is finished and can reference completed internal theorems. This feels like a significant review finding that needs careful attention.
codex
I’ve isolated the first hard failure: C0 invokes a perfectness lemma on the wrong object and with missing hypotheses. I’m checking the higher-genus differential convention and the uncurving proposition now, because if the curved/flat comparison is only coderived, several later “ordinary derived” statements collapse with it.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '360,460p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"conv:higher-genus-differentials|prop:gauss-manin-uncurving-chain|dfib|Dg\\{g\\}|flat comparison|coderived\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   360	cohomology sheaves
   361	$\mathcal{H}^q(R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA))$ vanish for
   362	$q \neq 0$ uniformly over the base, and the surviving $R^0$ has
   363	finite-dimensional fibers by hypothesis~(ii). The standard
   364	cohomology and base change theorem
   365	(EGA~III, Th\'eor\`eme~7.7.5)
   366	then gives that $R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA)$ is a perfect
   367	complex (bounded, with coherent cohomology sheaves) on
   368	$\overline{\mathcal{M}}_g$.
   369	\end{proof}
   370	
   371	\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
   372	\label{thm:fiber-center-identification}
   373	\index{fiber--center identification|textbf}
   374	\textup{[}Regime: curved-central
   375	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   376	
   377	\smallskip\noindent
   378	Assume $\cA$ carries a modular pre-Koszul datum
   379	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
 succeeded in 50ms:
Total output lines: 263

chapters/theory/higher_genus_complementarity.tex:44: \textup{(}unconditional in coderived form on the Koszul locus\textup{)}.}\;
chapters/theory/higher_genus_complementarity.tex:47: $(\barB^{(g)}(\cA),\dfib)$ determines a well-defined coderived
chapters/theory/higher_genus_complementarity.tex:48: object and is read through its strict flat comparison model
chapters/theory/higher_genus_complementarity.tex:49: $(\barB^{(g)}(\cA),\Dg{g})$
chapters/theory/higher_genus_complementarity.tex:50: \textup{(}Proposition~\textup{\ref{prop:gauss-manin-uncurving-chain}}\textup{)}.
chapters/theory/higher_genus_complementarity.tex:105:coderived form on the Koszul locus, and its ordinary-derived
chapters/theory/higher_genus_complementarity.tex:227:$(\bar{B}^{(g)}(\cA), \Dg{g})$ are M-level models; the kernel
chapters/theory/higher_genus_complementarity.tex:284:differential~$\dfib$
chapters/theory/higher_genus_complementarity.tex:285:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
chapters/theory/higher_genus_complementarity.tex:300:\bigl(\barB^{(g)}(\cA), \Dg{g}\bigr)
chapters/theory/higher_genus_complementarity.tex:302:for the strict flat comparison family of
chapters/theory/higher_genus_complementarity.tex:303:Convention~\textup{\ref{conv:higher-genus-differentials}}.
chapters/theory/higher_genus_complementarity.tex:335:$\Dg{g}$ sit in positive filtration degree, so
chapters/theory/higher_genus_complementarity.tex:408:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes (it lies
chapters/theory/higher_genus_complementarity.tex:2894:\item Compute the total corrected differential $\Dg{g}$ on $\bar{B}^{(g)}(\mathcal{A})$
chapters/theory/higher_genus_complementarity.tex:2897:This differential satisfies $\Dg{g}^{\,2} = 0$ (Convention~\ref{conv:higher-genus-differentials}).
chapters/theory/higher_genus_complementarity.tex:2898:\item Compute the fiberwise collision differential $\dfib$ and verify
chapters/theory/higher_genus_complementarity.tex:2899:that $\dfib^{\,2} = \kappa \cdot \omega_g \in Z(\mathcal{A}) \otimes H^2(\overline{\mathcal{M}}_g)$;
exec
/bin/zsh -lc "for f in chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/theory/bar_cobar_adjunction_curved.tex; do if rg -q \"label\\{conv:higher-genus-differentials\\}|label\\{prop:gauss-manin-uncurving-chain\\}\" \""'$f"; then echo "FILE $f"; nl -ba "$f" | sed -n '"'1,260p'; fi; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
FILE chapters/theory/higher_genus_foundations.tex
     1	\chapter{Higher genus}
     2	\label{chap:higher-genus}
     3	
     4	\index{higher genus!bar complex|textbf}
     5	\index{quantum corrections|textbf}
     6	
     7	Everything up to this point takes place at genus zero; but
     8	genus zero on a curve is not the same as ``over a point.''
     9	The bar differential $\dfib$ is constructed from collision
    10	residues on the Fulton--MacPherson compactification
    11	$\overline{C}_n(X)$, its nilpotency $\dfib^{\,2} = 0$ uses
    12	the Arnold relations among the forms
    13	$\eta_{ij} = d\log(z_i - z_j)$ on the diagonal complement,
    14	and the higher $A_\infty$ operations $m_n$ for $n \geq 3$ are
    15	transferred along a retract whose source is
    16	$C_*(\overline{\mathcal{M}}_{0,n+1})$, the chain complex of the
    17	Stasheff associahedron. The formal-disk restriction that recovers
    18	classical Koszul duality over a point is a homotopy retract: it is
    19	additional data, not a tautology.

thinking
**Exploring convention lines**

I'm considering the need for convention lines, particularly focusing on uncurving chain lines around 900 in higher genus foundations. It seems essential to target an excerpt related to this proposition, as I want to ensure I'm accurately addressing it. I wonder what specific details or elements would make this excerpt most effective. Exploring these aspects will help in making a solid proposal!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '900,980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4570,4655p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   900	boundary cancellation.
   901	
   902	Level~(ii): the positive-energy axiom gives
   903	$\cA = \bigoplus_{n \geq 0} \cA_n$ with $\dim \cA_n < \infty$.
   904	The weight-by-weight SDR
   905	(Cliff~\cite[Proposition~8.1]{Cliff19})
   906	applies at each genus to produce the transferred structure
   907	in $D^{\mathrm{co}}$; the key input is that the homotopy
   908	transfer theorem requires only finite-dimensional weight
   909	spaces, not Koszulness.
   910	
   911	Level~(iii): MK1 (PBW collapse at $E_2$) implies diagonal Ext
   912	vanishing, which is the hypothesis of
   913	Theorem~\ref{thm:higher-genus-inversion}. On the Koszul locus,
   914	the curved bar complex $(\barBch(\cA), \dfib)$ and the flat model
   915	$(\barBch(\cA), \Dg{g})$ are linked by the coderived-to-derived
   916	comparison
   917	(Proposition~\ref{prop:gauss-manin-uncurving-chain}),
   918	and the counit is a quasi-isomorphism in the ordinary
   919	derived category. The passage from coderived to derived is
 succeeded in 51ms:
  4570	\bar{B}^{(g)}_{\mathrm{flat}}(\mathcal{A})
  4571	\;:=\;
  4572	\bigl(\bar{B}^{(g)}(\mathcal{A}), \Dg{g}\bigr)
  4573	\]
  4574	be the strict genus-$g$ bar complex
  4575	\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}}\textup{)}.
  4576	Write
  4577	\[
  4578	\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A})
  4579	\;:=\;
  4580	\mathcal{E}nd\!\bigl(\bar{B}^{(g)}_{\mathrm{flat}}(\mathcal{A})\bigr),
  4581	\qquad
  4582	\mathcal{Z}(\mathcal{A})
  4583	\;:=\;
  4584	\mathcal{H}^0\!\bigl(\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A})\bigr).
  4585	\]
  4586	Then the obstruction to extending the genus-$(g{-}1)$ flat data to
  4587	genus~$g$ is a transgression class
  4588	\begin{equation}
  4589	\operatorname{Obs}^{(g)}(\mathcal{A})
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '550,640p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   550	A candidate Koszul dual chiral algebra $\cA^!$ on~$X$ with
   551	universal twisting morphism
   552	$\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
   553	$\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
   554	\emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
   555	not an input; $\bar{B}_X(\cA)$ itself is the Koszul dual \emph{coalgebra}.
   556	
   557	\item\label{D:genus-tower}
   558	A genus tower $\{\bar{B}^{(g)}_X(\cA)\}_{g \geq 0}$ extending the
   559	genus-$0$ bar construction to all genera via propagators on
   560	$\overline{C}_n(\Sigma_g)$
   561	(Theorem~\ref{thm:prism-higher-genus}).
   562	Each genus-$g$ piece carries a degree-$1$ \emph{fiberwise
   563	differential}~$\dfib$ with
   564	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \operatorname{id}$
   565	(Convention~\ref{conv:higher-genus-differentials}).
   566	The completed total bar object
   567	$\bar{B}^{\mathrm{full}}_X(\cA) :=
   568	\prod_{g \geq 0} \hbar^g \bar{B}^{(g)}_X(\cA)$
   569	carries a strict total differential $\Dg{} \colon
exec
/bin/zsh -lc "rg -n \"label\\{prop:gauss-manin-uncurving-chain\\}|gauss-manin-uncurving-chain\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2920,3015p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2920	
  2921	Now compute $\mathcal{A}_3^{(1)}$. The pure holomorphic terms $\sum_{\mathrm{cyc}} h_{ij}h_{jk}\,(dz_i - dz_j)\wedge(dz_j - dz_k)$ vanish: expanding, the coefficient functions satisfy the identity
  2922	\begin{equation}
  2923	\zeta(u)\zeta(v) + \zeta(v)\zeta(w) + \zeta(w)\zeta(u) = \tfrac{1}{2}\bigl[\wp(u) + \wp(v) + \wp(w)\bigr]
  2924	\end{equation}
  2925	for $u+v+w = 0$ (where $u = z_{12}$, $v = z_{23}$, $w = z_{31}$). Since $\wp$ is an even function and $dz_i \wedge dz_j$ is antisymmetric, symmetry kills the right-hand side when wedged with the form factors.
  2926	
  2927	The surviving cross-terms are $\sum_{\mathrm{cyc}} (h_{ij} a_{jk} + a_{ij} h_{jk})\,(dz_i - dz_j) \wedge (dz_j - dz_k)$. These are $(1,1)$-forms because $a_{jk}$ contributes a $d\bar{z}$-dependence through $\bar{z}_{jk}$. Using $\bar\partial a_{jk} = \frac{\pi}{2i\,\mathrm{Im}(\tau)}\,d\bar{z}_j$ and summing over cyclic permutations:
  2928	\begin{equation}
  2929	\mathcal{A}_3^{(1)} = \frac{2\pi i}{2i\,\mathrm{Im}(\tau)} \, dz \wedge d\bar{z} = 2\pi i \cdot \omega_\tau
  2930	\end{equation}
  2931	where $\omega_\tau = \frac{i}{2\,\mathrm{Im}(\tau)}\,dz \wedge d\bar{z}$ is the normalized volume form on $E_\tau$.
  2932	\end{proof}
  2933	
  2934	\begin{proof}[Genus $2$ case]
  2935	Fix a genus-$2$ surface $\Sigma_2$ with canonical homology basis
  2936	$(A_1, A_2, B_1, B_2)$, period matrix $\Omega \in \mathfrak{H}_2$,
  2937	and normalized abelian differentials $\omega_1, \omega_2$.
  2938	The single-valued propagator on $\Sigma_2$ is
  2939	(Definition~\ref{def:higher-genus-log-forms}):
 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:50: \textup{(}Proposition~\textup{\ref{prop:gauss-manin-uncurving-chain}}\textup{)}.
chapters/theory/higher_genus_foundations.tex:345:\label{prop:gauss-manin-uncurving-chain}
chapters/theory/higher_genus_foundations.tex:917:(Proposition~\ref{prop:gauss-manin-uncurving-chain}),
chapters/theory/higher_genus_foundations.tex:4613:By Proposition~\ref{prop:gauss-manin-uncurving-chain} and
chapters/theory/higher_genus_foundations.tex:4643:Finally, Proposition~\ref{prop:gauss-manin-uncurving-chain}(ii)
chapters/theory/higher_genus_foundations.tex:345:\label{prop:gauss-manin-uncurving-chain}
chapters/theory/higher_genus_foundations.tex:917:(Proposition~\ref{prop:gauss-manin-uncurving-chain}),
chapters/theory/higher_genus_foundations.tex:4613:By Proposition~\ref{prop:gauss-manin-uncurving-chain} and
chapters/theory/higher_genus_foundations.tex:4643:Finally, Proposition~\ref{prop:gauss-manin-uncurving-chain}(ii)
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '320,390p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   320	$d$ for the genus-$0$ bar differential are using $\dzero$.
   321	\end{convention}
   322	
   323	\begin{remark}[Curvature as infinitesimal monodromy: the chiral Riemann--Hilbert correspondence]
   324	\label{rem:curvature-riemann-hilbert}
   325	\index{Riemann--Hilbert correspondence!chiral|textbf}
   326	\index{curvature!as infinitesimal monodromy}
   327	The genus-$g$ propagator $\eta_{ij}^{(g)}=d\log E(z_i,z_j)+\cdots$
   328	acquires monodromy $2\pi i$ around $B$-cycles; the Arakelov
   329	normalization transfers this into the Arnold defect, giving
   330	$\dfib^{\,2}=\kappa(\cA)\cdot\omega_g$.
   331	Thus $\kappa(\cA)$ is the infinitesimal monodromy of the logarithmic
   332	propagator. The corrected differential $\Dg{g}$ absorbs the curvature
   333	into quantum corrections, restoring $\Dg{g}^{\,2}=0$; this is the chiral
   334	analogue of the Riemann--Hilbert correspondence ($\dfib$ is the curved
   335	connection, $\Dg{g}$ the flat one).
   336	The three differentials $\dzero$, $\dfib$, $\Dg{g}$ correspond to:
   337	genus-$0$ (single-valued), genus-$g$ with monodromy (curved),
   338	and the full logarithm on the universal cover (flat).
   339	See Volume~II, Remark~\ref*{rem:three-models} for the full
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '390,460p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   390	 $\{\dfib, \nabla^{\mathrm{GM}}\}
   391	 = -\kappa(\cA) \cdot \omega_g^{\mathrm{Ar}}$
   392	 \textup{(}the Lagrangian property of the $A$-cycle subspace
   393	 cancels the Arakelov form against the period correction\textup{)},
   394	 and $(\nabla^{\mathrm{GM}})^2 = 0$ \textup{(}flatness\textup{)}.
   395	
   396	\item \emph{The uncurving is not a gauge equivalence.}\;
   397	 The passage $\dfib \leadsto \Dg{g}$ is \emph{not} a gauge
   398	 transformation of the curved bar complex: there is no element
   399	 $\alpha$ with $\Dg{g} = e^{\alpha}\,\dfib\,e^{-\alpha}$.
   400	 Rather, $\nabla^{\mathrm{GM}}$ is an independent geometric datum
   401	 (the connection on the base $\overline{\cM}_g$), and the
   402	 uncurving identity~\eqref{eq:chain-uncurving} expresses the
   403	 interplay between fiber curvature and base flatness.
   404	 The resulting flat complex $(\barB^{(g)}(\cA), \Dg{g})$ lives in
   405	 the derived category; the curved complex
   406	 $(\barB^{(g)}(\cA), \dfib)$ lives in the coderived category
   407	 $D^{\mathrm{co}}$~(Appendix~\ref{app:coderived-models}).
   408	 These categories are \emph{inequivalent} in general: the
   409	 coderived category has strictly more objects (the coacyclic

thinking
**Considering definitions for D**

I’m trying to figure out what D means in this context, which is said to equal dfib + GM. But I wonder if convention lines define D in another way? I think it’s a good idea to check the continuation lines starting from 258 to see if there’s additional context or clarification there. It feels important to verify this so I can get it right!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '229,290p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   229	\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
   230	\index{bar differential!higher-genus notation|textbf}
   231	The Feynman transform differential
   232	$d_{\mathrm{FT}} = d_{\mathrm{tree}} + d_{\mathrm{loop}}$
   233	\textup{(}Proposition~\textup{\ref{prop:loop-filtration-compatible})} is
   234	the single canonical differential on the genus-$g$ bar complex. For
   235	computational purposes, three projections of this differential are
   236	used throughout the manuscript.
   237	\begin{enumerate}
   238	\item[\textup{(i)}] \textbf{Fiberwise curved differential} $\dfib$.
   239	 On a fixed curve $\Sigma_g$, the collision-residue differential built
   240	 from the genus-$g$ propagator. This differential is \emph{curved}:
   241	 \[
   242	 \dfib^{\,2} = \kappa(\cA)\cdot\omega_g\cdot\mathrm{id},
   243	 \]
   244	 where $\omega_g$ is the Arakelov $(1,1)$-form
   245	 (Theorem~\ref{thm:quantum-arnold-relations}) and
   246	 $\kappa(\cA)$ is the leading OPE anomaly coefficient.
   247	 At chain level, this equation is an operator identity on
   248	 $\barB^{(g)}(\cA)|_{[\Sigma_g]}$: the endomorphism $\dfib^{\,2}$


thinking
**Reviewing theorem proofs**

I’m focusing on steps I-III to see if they justify the theorem, which involves reading sections around lines 665-1780. I need to identify any missing definitions, hidden imports, unresolved references, and unjustified steps. The user mentioned doing a thorough audit, so I might find many issues — possibly 10 to 20 findings. I’ll consider using tools like `texcheck` or command-line searches to find unresolved labels or undefined references. I need to determine the best approach without unnecessary complexity!
thinking
**Identifying unresolved references**

If there are unresolved references in the file, a build could reveal them. However, the user specifically wants to focus on missing definitions, hidden imports, and unresolved references. I could use grep to search for labels referenced in the proof. It might be helpful to script something that extracts references within a specific line range and checks their existence using regex. As the user wants an exhaustive search for hidden imports, I may need to systematically identify all references in lines 1-2104.
codex
I’m checking the proof lane mechanically now: every `\ref` in the C0/C1/C2 block against actual label definitions. That catches hard unresolved imports quickly and separates them from the deeper logical failures in the proofs themselves.
exec
/bin/zsh -lc "perl -ne 'if("'$.<=2104){ while(/'"\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){ print \""'$.:$1'"\\n\" } }' chapters/theory/higher_genus_complementarity.tex | while IFS=: read -r line label; do hits="'$(rg -n "label'"\\\\{"'$label'"\\\\}\" chapters appendices metadata 2>/dev/null | wc -l | tr -d ' '); if [ \""'$hits" = "0" ]; then printf '"'%s:%s\\n' \""'$line" "$label"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 1.63s:
1805:part:characteristic-datum

thinking
**Investigating unresolved labels**

I’ve come across an unresolved label `part:characteristic-datum` at line 1805 in the file. I need to inspect that area closely. It might be insightful, but I should consider other labels defined in the volumes since I only searched the chapters, appendices, and metadata within the repository. There could be more unresolved references later on, so I might check all lines. I should also extract references to non-existent local definitions or external ones. I'm focusing on lines around 1787 to 1810.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1788,1812p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1788	$1 + 0 = 1$. This is the genus-$0$ exception to the duality clause in
  1789	Theorem~\ref{thm:quantum-complementarity-main}.
  1790	
  1791	\emph{Genus $1$}: $\dim H^*(\overline{\mathcal{M}}_{1,1}) = 2$ ($H^0 \oplus H^2$).
  1792	For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
  1793	(central extension, eigenvalue $+1$) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C}
  1794	\cdot \lambda$ (curvature, eigenvalue $-1$). Dimension check: $1 + 1 = 2$.
  1795	
  1796	\emph{Genus $2$}: $\dim H^*(\overline{\mathcal{M}}_2) = 8$
  1797	(Poincar\'e polynomial $1 + 3t^2 + 3t^4 + t^6$).
  1798	The involution $\sigma$ splits $H^*$ into $\pm 1$-eigenspaces whose
  1799	dimensions depend on the chiral algebra through the $j_*/j_!$ extension
  1800	data. For Koszul self-dual algebras (e.g., $\mathrm{Vir}_{13}$),
  1801	Corollary~\ref{cor:virasoro-quantum-dim} gives
  1802	$\dim V^+ = \dim V^- = 4$. For all Koszul chiral algebras
  1803	$\cA$ with trivial center, $\dim Q_2(\cA) + \dim Q_2(\cA^!) = 8$.
  1804	Detailed genus-$2$ complementarity dimensions are verified in
  1805	Part~\ref{part:characteristic-datum} (\S\ref{subsec:genus2-complementarity-verification}).
  1806	\end{proof}
  1807	

thinking
**Inspecting theorem proof**

I think I need to look into whether this is related to a proof of a theorem. Maybe I'm at the end of a stray proof? I'm considering inspecting the years around 1760 to 1810 for relevant insights or context. There's something intriguing about this period—it could hold clues that lead to a better understanding of what I'm trying to prove. Let's explore this further!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1740,1825p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1740	\emph{Step 9: Intersection vanishes (direct sum).}
  1741	
  1742	\begin{lemma}[Trivial intersection; \ClaimStatusProvedHere]
  1743	\label{lem:trivial-intersection-complete}
  1744	The quantum correction spaces intersect trivially:
  1745	\begin{equation}
  1746	Q_g(\mathcal{A}) \cap Q_g(\mathcal{A}^!) = 0
  1747	\end{equation}
  1748	\end{lemma}
  1749	
  1750	\begin{proof}[Proof of Lemma~\ref{lem:trivial-intersection-complete}]
  1751	By Lemma~\ref{lem:eigenspace-decomposition-complete}, $Q_g(\mathcal{A}) = V^+$ and
  1752	$Q_g(\mathcal{A}^!) = V^-$ are the $+1$ and $-1$ eigenspaces of the involution
  1753	$\sigma$. Since $+1 \neq -1$ (we work over $\mathbb{C}$, characteristic $\neq 2$),
  1754	eigenspaces for distinct eigenvalues of any linear operator intersect trivially:
  1755	\[
  1756	V^+ \cap V^- = 0. \qedhere
  1757	\]
  1758	\end{proof}
  1759	

thinking
**Inspecting theorem proof**

I'm noticing something intriguing about the theorem proof. It's marked as "completed," but I see there's no `\begin{proof}` at line 1825. Hmm, that definitely raises some questions. I should look closely around lines 1820 to 1890 to dig deeper into what’s going on there. It could be essential to ensure everything is in the right structure! Let’s see what I can find.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1818,1905p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1818	
  1819	Therefore:
  1820	\begin{equation}
  1821	Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) \cong H^*(\overline{\mathcal{M}}_g,
  1822	Z(\mathcal{A}))
  1823	\end{equation}
  1824	
  1825	This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere
  1826	
  1827	\end{proof}
  1828	
  1829	\begin{remark}[Proof architecture summary for Theorem~C]
  1830	\label{rem:h-level-proof-summary}
  1831	\index{Theorem C!proof architecture summary}
  1832	The distributed proof above establishes both the
  1833	S-level (cohomological) and H-level (homotopy) claims of
  1834	Theorem~\ref{thm:quantum-complementarity-main} via three steps.
  1835	\emph{First}, the Verdier involution~$\sigma$ is a
  1836	\emph{cochain-level} involution on
  1837	$\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$:



thinking
**Evaluating proof structure**

It looks like there are nested proofs here. The earlier theorem proof ends at 552, and then we have Step I starting at 665. The theorem C1 seems to have two proof environments; one is a short roadmap and the other a distributed proof. While it's syntactically allowed to have multiple proof environments, the initial proof indicates the theorem is "proved" before entering Step I. This might cause a broken proof block from an audit perspective. I’d prefer to convert the first proof to a remark or keep it open.
thinking
**Identifying proof issues**

I see that the theorem is already closed. The distributed proof labeled as Step I isn't formally tied to the theorem in LaTeX, so that could be a problem. It finishes at 1827, and although it compiles fine, the initial proof didn’t actually prove the theorem, creating an issue. I need to keep reading through the crucial proofs and find more potential issues. For instance, in Step I regarding the spectral sequence, the genus filtration seems incorrect, as it mixes contributions across genera, when it should focus on fixed genus contributions only.
thinking
**Exploring genus filtration**

It seems that the filtration on the total bar complex by genus isn’t defined in this chapter, which could indicate a hidden importance tied to some full genus tower. I need to verify if the expression `bar B(A)=\bigcup_{g=0}^\infty ...` is defined elsewhere, possibly as the total sum across all genera. I should search for definitions like `\bar{B}^{\mathrm{full}}` in higher_genus_modular_koszul. Meanwhile, in theorem C1 at a fixed genus g, Step I claims that this genus filtration leads to the spectral sequence.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '808,870p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   808	\overline{\mathcal{M}}_g
   809	\end{tikzcd}
   810	\end{equation}
   811	
   812	\emph{$E_1$~page.}
   813	By definition, $E_1^{p,q,g}$ is the cohomology
   814	of the fiber complex.
   815	The fiber over
   816	$[(\Sigma_g;\allowbreak p_1, \ldots, p_n)]$ is:
   817	\begin{equation}
   818	\bar{B}^p_{\text{fiber}} = \Gamma(\overline{C}_p(\Sigma_g), \mathcal{A}^{\boxtimes p} 
   819	\otimes \Omega^*_{\log})
   820	\end{equation}
   821	
   822	The differential
   823	\[
   824	d_{\mathrm{fiber}} = \!\!\!\!\sum_{D \,\subset\, \partial \overline{C}_p(\Sigma_g)}
   825	\!\!\!\!\operatorname{Res}_D
   826	\]
   827	computes residues along boundary divisors. By Theorem~\ref{thm:arnold-three},
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '866,925p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   866	\begin{proof}
   867	Three conditions must be verified.
   868	
   869	\emph{(1) Finite cohomological dimension of the base.}
   870	The Deligne--Mumford--Knudsen stack
   871	$\overline{\mathcal{M}}_g$ is a smooth proper
   872	Deligne--Mumford stack of dimension $3g - 3$. For any
   873	constructible sheaf $\mathcal{F}$ on
   874	$\overline{\mathcal{M}}_g$,
   875	$H^i(\overline{\mathcal{M}}_g, \mathcal{F}) = 0$ for
   876	$i > 2(3g-3) = 6g - 6$
   877	(Artin vanishing for proper DM stacks,
   878	\cite[\S4.1]{Olsson16}).
   879	
   880	\emph{(2) Constructibility of the fiber sheaves.}
   881	The fiber cohomology sheaf
   882	$\mathcal{H}^q_{\mathrm{fiber}}(\cA)$ on
   883	$\overline{\mathcal{M}}_g$ is constructible with respect to
   884	the stratification by topological type of stable curve.
   885	On the smooth locus $\mathcal{M}_g$, it is a local system

thinking
**Reviewing fiber cohomology**

I need to check the fiber-cohomology center and see if it involves fiber-center identification. There might be some circularity happening, so let’s take a closer look at the specific lines from 924 to 1064. I’ll inspect those lines carefully to clarify any potential confusion or overlap. It’s important to ensure I fully understand the concepts before moving on! Let's dig into the details and assess what’s going on there.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '920,1066p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   920	\begin{lemma}[Quantum corrections as spectral sequence limit; \ClaimStatusProvedHere]
   921	\label{lem:quantum-from-ss}
   922	The genus-$g$ quantum correction space is:
   923	\begin{equation}
   924	Q_g(\mathcal{A}) = E_\infty^{*,*,g} = \bigoplus_{p+q=*} \text{gr}^g H^{p+q}(
   925	\bar{B}(\mathcal{A}))
   926	\end{equation}
   927	where $\text{gr}^g$ denotes the $g$-th graded piece of the genus filtration.
   928	\end{lemma}
   929	
   930	\begin{proof}[Proof of Lemma~\ref{lem:quantum-from-ss}]
   931	By definition of spectral sequences, $E_\infty$ is the associated graded of the 
   932	filtered cohomology:
   933	\begin{equation}
   934	E_\infty^{p,q,g} \cong \frac{F^g H^{p+q}(\bar{B}(\mathcal{A}))}{F^{g-1} H^{p+q}(
   935	\bar{B}(\mathcal{A}))}
   936	\end{equation}
   937	
   938	The genus-$g$ quantum corrections are precisely those cohomology classes that arise 
   939	from genus-$g$ contributions but not from lower genus. Thus:
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1064,1070p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1064	This is an exhaustive, bounded-below ($F_{-1}=0$) filtration, so the
  1065	associated spectral sequence converges to
  1066	$H^*(\bar{B}^*_{\Sigma_g}(\mathcal{A}))$.
  1067	
  1068	On the associated graded $\operatorname{gr}^p_F$, the curvature
  1069	corrections~$d_{\mathrm{curv}}$ vanish because they raise bar degree
  1070	(hence filtration level). The surviving differential~$d_0$ is the
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1068,1110p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1068	On the associated graded $\operatorname{gr}^p_F$, the curvature
  1069	corrections~$d_{\mathrm{curv}}$ vanish because they raise bar degree
  1070	(hence filtration level). The surviving differential~$d_0$ is the
  1071	genus-$0$ collision differential alone. By
  1072	Theorem~\ref{thm:geometric-equals-operadic-bar}, the complex
  1073	$(\operatorname{gr}^p_F, d_0)$ is identified with the operadic bar
  1074	complex of~$\operatorname{gr}\mathcal{A}$.
  1075	
  1076	Since $\mathcal{A}$ is Koszul
  1077	(Definition~\ref{def:chiral-koszul-pair}), the bar concentration
  1078	theorem (Theorem~\ref{thm:bar-concentration}) gives
  1079	\[
  1080	E_1^{p,q}
  1081	= H^q\bigl(\operatorname{gr}^p_F
  1082	 \bar{B}^*_{\Sigma_g}(\mathcal{A}),\, d_0\bigr)
  1083	= 0
  1084	\qquad\text{for } q \neq 0.
  1085	\]
  1086	Because the $E_1$ page is concentrated on the line $q=0$, every
  1087	differential


thinking
**Analyzing chiral algebra details**

I’m considering the implications of varying curves and how they influence the underlying chiral algebra \(\mathcal{A}\) on \(X\). There's no universal definition of \(\mathcal{A}\) across all curves, which could pose an issue. The chapter treats \(\mathcal{A}\) on a fixed curve, but later discusses fibers over moduli of curves as if the same algebra applies to each. I need to check the statement of theorem C1, especially regarding how a fixed \(X\) relates to arbitrary genus curves. It’s quite confusing!
thinking
**Investigating bar complex on curves**

I'm pondering whether the bar complex applies to any genus-g curve. It seems like there’s a missing family structure in the definitions. I need to check if they define a genus-g bar family over the moduli for a fixed \(A\) and curve \(X\). It's essential to investigate the initial definition concerning the relative bar fiber to clarify this aspect. I really want to get this right, so I’ll take a closer look!
codex
The next layer is worse than a missing label: Step I repeatedly takes ordinary cohomology of the curved fiber complex, even though the repo’s own higher-genus convention says that object only lives in the coderived category when `\kappa \neq 0`. I’m reading Steps II and III now to see whether the same derived/coderived slippage and circularity continue there.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1070,1268p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1070	(hence filtration level). The surviving differential~$d_0$ is the
  1071	genus-$0$ collision differential alone. By
  1072	Theorem~\ref{thm:geometric-equals-operadic-bar}, the complex
  1073	$(\operatorname{gr}^p_F, d_0)$ is identified with the operadic bar
  1074	complex of~$\operatorname{gr}\mathcal{A}$.
  1075	
  1076	Since $\mathcal{A}$ is Koszul
  1077	(Definition~\ref{def:chiral-koszul-pair}), the bar concentration
  1078	theorem (Theorem~\ref{thm:bar-concentration}) gives
  1079	\[
  1080	E_1^{p,q}
  1081	= H^q\bigl(\operatorname{gr}^p_F
  1082	 \bar{B}^*_{\Sigma_g}(\mathcal{A}),\, d_0\bigr)
  1083	= 0
  1084	\qquad\text{for } q \neq 0.
  1085	\]
  1086	Because the $E_1$ page is concentrated on the line $q=0$, every
  1087	differential
  1088	$d_r\colon E_r^{p,q} \to E_r^{p+r,\,q-r+1}$
  1089	with $r \geq 2$ has target in the row $q' = q - r + 1 \leq -1$,
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1270,1552p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1550,1828p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1550	isomorphism $Z(\mathcal{A}) \cong Z(\mathcal{A}^!)$.
  1551	\end{lemma}
  1552	
  1553	\begin{proof}[Proof of Sublemma]
  1554	Since every $E_\infty$-chiral algebra is in particular an $E_1$-chiral algebra, and the Koszul property at the $E_\infty$ level implies Koszulity at the $E_1$ level (the forgetful functor is exact on bar complexes), we may apply the module Koszul duality equivalence
  1555	(Theorem~\ref{thm:e1-module-koszul-duality}), which gives:
  1556	\begin{equation}
  1557	\Phi: D^b(\mathrm{Mod}^{\Eone}_{\mathcal{A}}) \xrightarrow{\;\sim\;}
  1558	D^b(\mathrm{Mod}^{\Eone}_{\mathcal{A}^!})
  1559	\end{equation}
  1560	Under~$\Phi$, the unit module $\mathcal{A}$ (viewed as a module over itself)
  1561	maps to $\bar{B}^{\mathrm{ch}}(\mathcal{A}) = \mathcal{A}^!$ (viewed as a
  1562	module over~$\mathcal{A}^!$). Since equivalences of categories preserve
  1563	endomorphism algebras:
  1564	\begin{equation}
  1565	Z(\mathcal{A}) = \mathrm{End}_{D(\mathrm{Mod}_{\mathcal{A}})}(\mathcal{A})
  1566	\;\xrightarrow[\Phi]{\;\sim\;}\;
  1567	\mathrm{End}_{D(\mathrm{Mod}_{\mathcal{A}^!})}(\mathcal{A}^!)
  1568	= Z(\mathcal{A}^!)
  1569	\end{equation}
 succeeded in 52ms:
  1270	\begin{equation}
  1271	(E_{r+1})_{\mathcal{A}} = H(E_r, d_r)_{\mathcal{A}} \cong (H(E_r, d_r)_{\mathcal{A}^!})^\vee 
  1272	= ((E_{r+1})_{\mathcal{A}^!})^\vee
  1273	\end{equation}
  1274	
  1275	\emph{$E_\infty$ page}: Taking the limit $r \to \infty$:
  1276	\begin{equation}
  1277	(E_\infty^{p,q,g})_{\mathcal{A}} \cong ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee
  1278	\end{equation}
  1279	
  1280	But $E_\infty^{*,*,g} = \text{gr}^g H^*$ by definition, so:
  1281	\begin{equation}
  1282	\text{gr}^g H^{p+q}(\bar{B}(\mathcal{A})) \cong (\text{gr}^g H^{p+d-q}(\bar{B}(
  1283	\mathcal{A}^!)))^\vee
  1284	\end{equation}
  1285	\end{proof}
  1286	
  1287	\begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
  1288	\label{cor:quantum-dual-complete}
  1289	For each genus $g \geq 1$ and every Koszul dual chiral pair

thinking
**Inspecting theorems**

I see there's a lot to consider, particularly around the C2 theorem, specifically lines 1985 to 2104. It's important for me to dig into those lines to fully understand any issues that might arise. I’m making a mental note to focus on those areas, as it seems they could hold significant insights relevant to the problem at hand. Let’s clarify what those lines say and how they might impact my understanding!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1910,2108p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1910	stack $\overline{\mathcal{M}}_g$.
  1911	
  1912	\emph{Part (ii).}
  1913	The Verdier involution $\sigma$ is defined by
  1914	$\sigma = \mathbb{D} \circ \mathrm{KS}$, where $\mathrm{KS}$ is
  1915	the Kodaira--Spencer isomorphism
  1916	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}) and
  1917	$\mathbb{D}$ is Verdier duality. Since $\mathbb{D}^2 = \mathrm{id}$
  1918	on constructible sheaves and the Kodaira--Spencer map satisfies
  1919	the anti-commutativity
  1920	$\mathbb{D} \circ \nabla_{\kappa(v)}^z =
  1921	-\nabla_{\kappa(v)}^z \circ \mathbb{D}$
  1922	(Step~7 of the proof of
  1923	Theorem~\ref{thm:quantum-complementarity-main}), the involution
  1924	$\sigma$ reverses the sign of the pairing:
  1925	$\langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}}
  1926	= \langle \mathbb{D}v, \mathbb{D}w \rangle_{\mathbb{D}}
  1927	= -\langle v, w \rangle_{\mathbb{D}}$,
  1928	where the last step uses the anti-commutativity property.
  1929	
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2108,2140p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2108	\mathbb{D}_{\operatorname{Ran}}(\barB^{\mathrm{ch}}(\cA))
  2109	\xrightarrow{\;\sim\;}
  2110	\cA^!_\infty
  2111	\]
  2112	on the Koszul locus. By the compatibility clause in
  2113	Theorem~\ref{thm:bv-functor}, the adjoint map
  2114	$x \mapsto \{x,-\}_{\mathrm{BV}}$ is exactly this Verdier comparison,
  2115	shifted by~$[1]$. Since the comparison is a quasi-isomorphism, the
  2116	BV Poisson structure is non-degenerate. When one passes to the
  2117	underlying complex of~$\cA^!_\infty$, this recovers the equivalent
  2118	description in terms of $\barB^{\mathrm{ch}}(\cA^!)$.
  2119	
  2120	\emph{Part (ii).}
  2121	Shifting $\barB^{(g)}(\cA)$ by $[1]$ converts the degree~$+1$ BV
  2122	bracket to a degree~$0$ Lie bracket on $L_g$; the dg Lie algebra
  2123	axioms are inherited from the BV algebra axioms. The BV pairing on
  2124	$\barB^{(g)}(\cA)$ produced in Part~(i) restricts to a degree-$+1$
  2125	Verdier pairing. Evaluating against the canonical Verdier pairing on
  2126	the dual object and then shifting by~$[1]$ on both inputs produces a
  2127	bilinear form
exec
/bin/zsh -lc "rg -n \"label\\{lem:verdier-extension-exchange\\}|lem:verdier-extension-exchange\" chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/lattice_foundations.tex:3824:(Lemma~\ref{lem:verdier-extension-exchange}). On the lattice bar
chapters/theory/poincare_duality.tex:225:$j_!$ and $j_*$ extensions (Lemma~\ref{lem:verdier-extension-exchange}).
chapters/theory/cobar_construction.tex:37:(Lemma~\ref{lem:verdier-extension-exchange}) identifies the
chapters/theory/cobar_construction.tex:289:(Lemma~\ref{lem:verdier-extension-exchange}).
chapters/theory/cobar_construction.tex:354:\label{lem:verdier-extension-exchange}
chapters/theory/cobar_construction.tex:423:By Lemma~\ref{lem:verdier-extension-exchange},
chapters/theory/higher_genus_complementarity.tex:1415:exchanges $j_*$ and $j_!$ extensions (Lemma~\ref{lem:verdier-extension-exchange}):
chapters/theory/higher_genus_complementarity.tex:1633:(Lemma~\ref{lem:verdier-extension-exchange}).
chapters/theory/higher_genus_complementarity.tex:1648:(Lemma~\ref{lem:verdier-extension-exchange}).
chapters/theory/higher_genus_complementarity.tex:1688:(Lemma~\ref{lem:verdier-extension-exchange}), hence exchanges
exec
/bin/zsh -lc "rg -n \"label\\{cor:virasoro-quantum-dim\\}|cor:virasoro-quantum-dim|label\\{subsec:genus2-complementarity-verification\\}\" chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/genus_expansions.tex:1676:\subsection{Genus-2 complementarity verification}\label{subsec:genus2-complementarity-verification}
chapters/examples/genus_expansions.tex:1711:$\mathrm{Vir}_{13}$ (Corollary~\ref{cor:virasoro-quantum-dim};
chapters/theory/higher_genus_complementarity.tex:1802:Corollary~\ref{cor:virasoro-quantum-dim} gives
chapters/theory/higher_genus_complementarity.tex:2546:\label{cor:virasoro-quantum-dim}
chapters/theory/higher_genus_complementarity.tex:3184:see Corollary~\ref{cor:virasoro-quantum-dim}).
exec
/bin/zsh -lc "rg -n \"label\\{part:characteristic-datum\\}\" ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:742:/bin/zsh -lc "rg -n --fixed-strings '\\\\label{part:characteristic-datum}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:769:main.tex:1073:\label{part:characteristic-datum}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:311:/Users/raeez/chiral-bar-cobar/main.tex:1073:\label{part:characteristic-datum}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1360:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:742:/bin/zsh -lc "rg -n --fixed-strings '\\\\label{part:characteristic-datum}' chapters appendices" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1363:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:769:main.tex:1073:\label{part:characteristic-datum}
./wave2_audit_20260413_001942/F04_definitions_complementarity.md:1089:main.tex:1073:\label{part:characteristic-datum}
./wave2_audit_20260413_001942/U13_dead_labels.md:279:main.tex:1073:\label{part:characteristic-datum}
./wave2_audit_20260413_001942/C19_chiral_hochschild_koszul.md:1033:main.tex:1073:\label{part:characteristic-datum}
./audit_campaign_20260412_231034/F14_averaging.md:762:  1045	\label{part:characteristic-datum}
./main.tex:1073:\label{part:characteristic-datum}
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:73:1073:\label{part:characteristic-datum}
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:1338:1073:\label{part:characteristic-datum}
./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:686:main.tex:1073:\label{part:characteristic-datum}
./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:740:main.tex:1073:\label{part:characteristic-datum}
./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2002:/bin/zsh -lc "grep -n 'label{app:nonlinear-modular-shadows}\\|label{app:signs}\\|label{app:sign-conventions}\\|label{part:characteristic-datum}\\|label{thm:chiral-htt}\\|label{thm:bar-cobar-htt}\\|label{thm:nms-archetype-trichotomy}\\|label{thm:nms-finite-termination}\\|label{def:chiral-coproduct}' appendices/*.tex main.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:2046:main.tex:1073:\label{part:characteristic-datum}
./audit_campaign_20260412_231034/XV12_part_refs.md:320:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F14_averaging.md:762:  1045	\label{part:characteristic-datum}
./audit_campaign_20260412_231034/XV12_part_refs.md:322:/Users/raeez/chiral-bar-cobar/main.tex:1045:\label{part:characteristic-datum}
exec
/bin/zsh -lc "perl -ne 'if("'$.<=2104){ while(/'"\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){ print \""'$.:$1'"\\n\" } }' chapters/theory/higher_genus_complementarity.tex | while IFS=: read -r line label; do hits="'$(rg -n "label'"\\\\{"'$label'"\\\\}\" . 2>/dev/null | wc -l | tr -d ' '); if [ \""'$hits" = "0" ]; then printf '"'%s:%s\\n' \""'$line" "$label"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 6.81s:

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1894,1940p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1894	\end{proposition}
  1895	
  1896	\begin{proof}
  1897	\emph{Part (i).}
  1898	The center local system $\mathcal{Z}(\cA)$ on
  1899	$\overline{\mathcal{M}}_g$ is a constructible sheaf, and Verdier
  1900	duality gives a perfect pairing
  1901	$H^k(\overline{\mathcal{M}}_g, \mathcal{Z}) \otimes
  1902	H^{(3g-3)-k}(\overline{\mathcal{M}}_g, \mathbb{D}\mathcal{Z})
  1903	\to \mathbb{C}$.
  1904	The Koszul pairing identifies $\mathbb{D}\mathcal{Z}(\cA) \cong
  1905	\mathcal{Z}(\cA^!) \cong \mathcal{Z}(\cA)$
  1906	(the last isomorphism by
  1907	Theorem~\ref{thm:quantum-complementarity-main}, Step~7), so the
  1908	pairing lands on $V \otimes V$. Non-degeneracy follows from Verdier
  1909	duality for constructible sheaves on the smooth Deligne--Mumford
  1910	stack $\overline{\mathcal{M}}_g$.
  1911	
  1912	\emph{Part (ii).}
  1913	The Verdier involution $\sigma$ is defined by

thinking
**Adjusting structure for clarity**

I’m focusing on structural changes, aiming for a medium to high-level fix. I need to be precise: I’ll convert lines 552-562 to use the format `\begin{remark}[Proof roadmap] ... \end{remark}`. Then, I should also update line 665 to clearly indicate the start of the actual theorem proof with Step I. Getting these details right is essential for improving the overall clarity and organization!
exec
/bin/zsh -lc "rg -n \"label\\{thm:lagrangian-complementarity\\}|thm:lagrangian-complementarity\" chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_gravitational_s_duality.tex:2425:(Theorem~\ref{thm:lagrangian-complementarity}): the
chapters/connections/outlook.tex:666:\phantomsection\label{thm:lagrangian-complementarity}
chapters/connections/concordance.tex:4973:\ClaimStatusProvedHere]\label{thm:lagrangian-complementarity}
chapters/theory/higher_genus_complementarity.tex:1948:sense (Theorem~\ref{thm:lagrangian-complementarity}).
chapters/theory/higher_genus_foundations.tex:7219:(Theorem~\ref{thm:lagrangian-complementarity}),
codex
Plan for the rest of the audit:

1. Finish the C0/C1/C2 proof graph.
2. For each imported theorem or lemma that materially carries a proof step, check whether the target file uses the right object, the right hypotheses, and the right categorical setting.
3. Separate failures into:
   - false or circular proof steps,
   - hidden hypothesis / object mismatches,
   - missing definitions or unresolved structural references.
4. Re-verify every surviving finding against exact line ranges before I write the final review, so the output is only hard failures with concrete fixes.
exec
/bin/zsh -lc "nl -ba chapters/theory/poincare_duality.tex | sed -n '200,250p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '340,390p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:verdier-bar-cobar\\}|label\\{thm:e1-module-koszul-duality\\}|label\\{thm:chiral-koszul-duality\\}|label\\{thm:bar-concentration\\}|label\\{thm:geometric-equals-operadic-bar\\}|label\\{thm:conilpotency-bar\\}|label\\{thm:config-space-bv\\}|label\\{thm:bv-functor\\}\" chapters/theory chapters/examples appendices" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   340	The internal differential $d_{\mathrm{internal}}$ is induced by the
   341	chiral algebra structure, which is a $\mathcal{D}_X$-module morphism
   342	by definition.
   343	The form differential $d_{\mathrm{form}}$ is the de~Rham differential
   344	on $\Omega^*_{\log}(D)$, which is a $\mathcal{D}$-module morphism.
   345	The residue differential $d_{\mathrm{residue}} = \sum_D \operatorname{Res}_D$
   346	is the composition of restriction to a boundary divisor~$D$ followed
   347	by the trace map, both of which are morphisms of
   348	$\mathcal{D}$-modules \cite[Chapter~4]{KS90}.
   349	Hence $d_{\mathrm{bar}}$ is a morphism of holonomic
   350	$\mathcal{D}$-modules.
   351	\end{proof}
   352	
   353	\begin{lemma}[Verdier duality exchanges extensions; \ClaimStatusProvedHere]%
   354	\label{lem:verdier-extension-exchange}
   355	Let $Y$ be a smooth variety, $U \xhookrightarrow{j} Y$ an open inclusion
   356	with complement a normal crossings divisor, and $\mathcal{M}$ a holonomic
   357	$\mathcal{D}_U$-module. Then there is a canonical isomorphism in the
   358	derived category of holonomic $\mathcal{D}_Y$-modules:
   359	\[
 succeeded in 52ms:
   200	\emph{Step 3.}
   201	Taking hypercohomology with respect to the de Rham complex:
   202	\begin{align*}
   203	\mathbb{H}^*(\overline{C}_k(X), \Omega^*_{\log}) &= H^*_{\text{dR}}(\overline{C}_k(X), \log D)\\
   204	\mathbb{H}^*_{C_k(X)}(\Omega^*_{\text{dist}}) &= H^*_{c,\text{dR}}(C_k(X))
   205	\end{align*}
   206	
   207	The Verdier duality pairing descends to the de Rham pairing.
   208	
   209	\emph{Step 4.}
   210	The explicit pairing is computed by residues:
   211	\[\langle \omega_{\text{log}}, K_{\text{dist}} \rangle = \sum_{\text{strata } S} \int_S \text{Res}_S(\omega_{\text{log}}) \wedge K_{\text{dist}}|_S\]
   212	
   213	Verdier duality for constructible complexes on smooth varieties~\cite{KS90} gives perfectness.
   214	\end{proof}
   215	
   216	\begin{remark}[Algebraic vs.\ analytic Verdier duality]\label{rem:verdier-bridge}
   217	\index{Verdier duality!algebraic vs.\ analytic}
   218	Theorem~\ref{thm:verdier-config} uses ``Verdier duality'' in two senses that
   219	must be carefully distinguished:
 succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_curved.tex:581:\label{thm:conilpotency-bar}
chapters/theory/cobar_construction.tex:1314:\label{thm:verdier-bar-cobar}
chapters/theory/bar_construction.tex:2065:\label{thm:geometric-equals-operadic-bar}
chapters/theory/chiral_koszul_pairs.tex:1129:\label{thm:bar-concentration}
chapters/theory/chiral_koszul_pairs.tex:4251:\label{thm:chiral-koszul-duality}
chapters/theory/chiral_koszul_pairs.tex:5289:\label{thm:e1-module-koszul-duality}

thinking
**Evaluating step II fix**

I think this points to a fix for Step II: instead of using self-pairing log forms, I should use the Poincaré duality theorem distributional current pairing. I might need to inspect the `thm:verdier-config` lines around 180 to find the exact fix. I should definitely look into that to clarify things.
exec
/bin/zsh -lc "rg -n \"label\\{thm:verdier-config\\}\" chapters/theory/poincare_duality.tex && nl -ba chapters/theory/poincare_duality.tex | sed -n '150,215p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
170:\begin{theorem}[Verdier duality for configuration spaces; \ClaimStatusProvedElsewhere{} \cite{KS90}]\label{thm:verdier-config}
   150	\begin{example}[Three points and the Arnold relation]
   151	For $k = 3$, the three boundary divisors $D_{12}$, $D_{23}$,
   152	$D_{31}$ of $\overline{C}_3(\mathbb{P}^1)$ satisfy
   153	$\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31}
   154	+ \eta_{31} \wedge \eta_{12} = 0$
   155	(Theorem~\ref{thm:arnold-three}). The pairing with the
   156	distributional currents $\delta_{12} \wedge \delta_{23}$, etc.,
   157	gives the associativity constraint: the signed sum of iterated
   158	residues vanishes.
   159	\end{example}
   160	
   161	\section{Verdier duality on configuration spaces}
   162	
   163	\begin{setup}[Configuration space duality]\label{setup:config-verdier}
   164	Let $X$ be a smooth curve (or more generally, an $n$-dimensional manifold). The configuration space of $k$ points is:
   165	\[C_k(X) = \{(z_1, \ldots, z_k) \in X^k : z_i \neq z_j \text{ for } i \neq j\}\]
   166	
   167	Its Fulton--MacPherson compactification $\overline{C}_k(X)$ is a smooth manifold with corners, with boundary divisors parametrizing collision patterns.
   168	\end{setup}
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5280,5355p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5280	Any extension of that package to arbitrary chiral Koszul pairs would
  5281	require extra hypotheses and a module-level comparison theorem beyond
  5282	what is currently established here.
  5283	\end{remark}
  5284	
  5285	\subsection{\texorpdfstring{$\Eone$-chiral module category Koszul duality}{E1-chiral module category Koszul duality}}
  5286	
  5287	\begin{theorem}[\texorpdfstring{$\Eone$}{E1}-module category Koszul duality;
  5288	\ClaimStatusProvedHere]
  5289	\label{thm:e1-module-koszul-duality}
  5290	\index{module Koszul duality|textbf}
  5291	Let $\mathcal{A}$ be a Koszul $\Eone$-chiral algebra with Koszul
  5292	dual bar coalgebra
  5293	$C_{\mathcal{A}} := \bar{B}^{\mathrm{ch}}(\mathcal{A})$
  5294	\textup{(}Theorem~\ref{thm:e1-chiral-koszul-duality},
  5295	Corollary~\ref{cor:e1-self-duality}\textup{)}. When the finite-type
  5296	graded dual exists, we write $\mathcal{A}^! := C_{\mathcal{A}}^\vee$
  5297	for the corresponding dual algebra. Then the bar-cobar adjunction
  5298	restricts to an equivalence of derived categories between
  5299	\emph{complete} (pro-nilpotent) $\mathcal{A}$-modules and
exec
/bin/zsh -lc "rg -n \"label\\{cor:bar-cohomology-koszul-dual\\}|cor:bar-cohomology-koszul-dual\" chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/combinatorial_frontier.tex:30:For a Koszul chiral algebra~$\cA$, the bar cohomology dimensions $\dim H^n(\barBgeom(\cA))$ coincide with the Hilbert function of the Koszul dual $\cA^!$ (Corollary~\ref{cor:bar-cohomology-koszul-dual}). These dimensions are the central enumerative invariants of the theory. Their generating functions encode, in compact form, the full structure of the bar complex: growth rates, analytic singularities, and (conjecturally) the spectral data of a finite-rank transfer operator.
appendices/combinatorial_frontier.tex:213:(Corollary~\ref{cor:bar-cohomology-koszul-dual},
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
chapters/examples/bar_complex_tables.tex:1960:(Corollary~\ref{cor:bar-cohomology-koszul-dual}, Step~4),
chapters/theory/higher_genus_complementarity.tex:4442:Corollary~\ref{cor:bar-cohomology-koszul-dual}, Step~4, applied
chapters/theory/chiral_koszul_pairs.tex:941:\label{cor:bar-cohomology-koszul-dual}
chapters/theory/chiral_koszul_pairs.tex:1167:Corollary~\ref{cor:bar-cohomology-koszul-dual} then gives
chapters/theory/chiral_koszul_pairs.tex:1228:(Corollary~\ref{cor:bar-cohomology-koszul-dual}) admits a sharp
chapters/theory/chiral_koszul_pairs.tex:3918:(Corollary~\ref{cor:bar-cohomology-koszul-dual}, Step~4),
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '920,970p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   920	\emph{Hypothesis~\ref{item:pbw-classical-koszul}.}
   921	$\operatorname{gr}_F \mathrm{Vir}_c
   922	\cong \operatorname{Sym}(V)$
   923	is a polynomial algebra (the OPE reduces to a commutative
   924	product on the associated graded: the non-linear terms
   925	$T_{(0)}T = \partial T$, $T_{(1)}T = 2T$ are lower-order in the
   926	PBW filtration, and the quartic pole $T_{(3)}T = c/2$ is a
   927	scalar that contributes to the curvature, not the
   928	associated graded bracket).
   929	By Priddy's theorem, $\operatorname{Sym}(V)$ is Koszul.
   930	
   931	\emph{Hypothesis~\ref{item:pbw-bounded}.}
   932	Same argument as the Kac--Moody case: the number of
   933	partitions of weight~$h$ into at most $n$ parts (each $\geq 2$)
   934	is finite.
   935	
   936	By Theorem~\ref{thm:pbw-koszulness-criterion},
   937	$\mathrm{Vir}_c$ is chiral Koszul.
   938	\end{proof}
   939	
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1300,1365p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1300	corresponds to the cobar product:
  1301	\[n_2(K_\alpha, K_\beta) = \sum_\gamma C_{\alpha\beta}^\gamma K_\gamma\]
  1302	
  1303	The structure constants $C_{\alpha\beta}^\gamma$ are precisely the cobar $A_\infty$ 
  1304	structure constants.
  1305	
  1306	The cobar construction thus provides a geometric derivation
  1307	of the OPE algebra in CFT.
  1308	\end{remark}
  1309	
  1310	\subsection{Verdier duality on bar and cobar}
  1311	
  1312	
  1313	\begin{theorem}[Bar-cobar Verdier; \ClaimStatusProvedHere]\label{thm:bar-cobar-verdier}
  1314	\label{thm:verdier-bar-cobar}
  1315	\index{Verdier duality!bar-cobar|textbf}
  1316	\textup{[Regime: quadratic, genus-$0$
  1317	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1318	
  1319	Let $\mathcal{A}$ be on the Koszul locus and write $\mathcal{A}^!$ for its
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '196,222p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   196	\begin{definition}[Deformation-obstruction complexes: H-level]
   197	\label{def:complementarity-complexes}
   198	\index{deformation-obstruction complexes|textbf}
   199	Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$.
   200	The \emph{ambient complex} at genus~$g$ is
   201	\[
   202	\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
   203	\]
   204	where $\mathcal{Z}(\cA)$ is the center local system.
   205	The Verdier involution $\sigma$ acts on $\mathbf{C}_g(\cA)$ as a
   206	cochain-level endomorphism with $\sigma^2 = \mathrm{id}$
   207	(Theorem~\ref{thm:verdier-bar-cobar}).
   208	Define the \emph{deformation-obstruction complexes} as homotopy eigenspaces:
   209	\begin{equation}\label{eq:complementarity-fiber}
   210	\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \mathrm{id}\colon
   211	\mathbf{C}_g \to \mathbf{C}_g), \qquad
   212	\mathbf{Q}_g(\cA^!) := \operatorname{fib}(\sigma + \mathrm{id}\colon
   213	\mathbf{C}_g \to \mathbf{C}_g).
   214	\end{equation}
   215	The \emph{cohomological shadows} (S-level) are defined by:

thinking
**Evaluating mathematical definitions**

I see there's a strong hidden import mismatch, so I need to inspect the exact theorem involving `thm:bar-cobar-verdier`. It mentions regime quadratic and genus-0, which may not support the moduli cochain-level sigma. This seems critical since definitions depend on an unsupported theorem. The fix could be to cite `lem:verdier-involution-moduli` and adjust definitions accordingly. I might also want to check if `def:center local system` exists, as the target file may use it without defining. I'll search for that.
exec
/bin/zsh -lc "rg -n \"label\\{.*center.*local.*\\}|center local system|\\\\mathcal\\{Z\\}\\(\\\\cA\\)\" chapters/theory/higher_genus_complementarity.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label\{.*center.*local.*\}|center local system|\mathcal\{Z\}\(\cA\))
                                                      ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"center local system|mathcal\\{Z\\}|Z\\(\\\\cA\\)\" chapters/theory/higher_genus_complementarity.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:center local system|mathcal\{Z\}|Z\(\cA\))
                                           ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n --fixed-strings "center local system" chapters/theory/higher_genus_complementarity.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:204:where $\mathcal{Z}(\cA)$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:416: $\mathcal{Z}_{\cA}$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:481:degree-$0$ sheaf with the center local system~$\mathcal{Z}_{\cA}$.
chapters/theory/higher_genus_complementarity.tex:1876:\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
chapters/theory/higher_genus_complementarity.tex:1898:The center local system $\mathcal{Z}(\cA)$ on
chapters/theory/introduction.tex:583: The \emph{center local system} $\mathcal{Z}_\cA$ is the
chapters/theory/higher_genus_complementarity.tex:204:where $\mathcal{Z}(\cA)$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:416: $\mathcal{Z}_{\cA}$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:481:degree-$0$ sheaf with the center local system~$\mathcal{Z}_{\cA}$.
chapters/theory/higher_genus_complementarity.tex:1876:\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
chapters/theory/higher_genus_complementarity.tex:1898:The center local system $\mathcal{Z}(\cA)$ on
chapters/theory/cobar_construction.tex:3262:(Theorem~\ref{thm:chiral-koszul-duality}), the center local system
chapters/theory/cobar_construction.tex:3289:on the center local system $\mathcal{Z}(\mathcal{A})$
chapters/theory/cobar_construction.tex:3332:The Verdier involution $\sigma$ on the center local system
chapters/theory/algebraic_foundations.tex:265:complementarity decomposes the center local system into
chapters/theory/higher_genus_foundations.tex:4633:with the chiral product. Their sheaf is the center local system
chapters/theory/higher_genus_modular_koszul.tex:454:A \emph{center local system}
chapters/theory/higher_genus_modular_koszul.tex:575:A center local system $\mathcal{Z}_{\cA}$ on
chapters/theory/higher_genus_modular_koszul.tex:28997:center local system $\mathcal{Z}_\cA$ on
exec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:quantum-complementarity-main\\}|thm:quantum-complementarity-main\" chapters/theory/higher_genus_complementarity.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
39:(Theorem~\ref{thm:quantum-complementarity-main}).
78: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
504:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
525:\label{thm:quantum-complementarity-main}
944:anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
1298:\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
1314:Theorem~\ref{thm:quantum-complementarity-main}.
1790:Theorem~\ref{thm:quantum-complementarity-main}.
1826:This completes the proof of Theorem~\ref{thm:quantum-complementarity-main}. \qedhere
1835:Theorem~\ref{thm:quantum-complementarity-main} via three steps.
1907:Theorem~\ref{thm:quantum-complementarity-main}, Step~7), so the
1923:Theorem~\ref{thm:quantum-complementarity-main}), the involution
1944:Theorem~\ref{thm:quantum-complementarity-main} is a Lagrangian
2262: (Theorem~\ref{thm:quantum-complementarity-main}), we have
2397:The conjecture asserts that quantum complementarity (Theorem~\ref{thm:quantum-complementarity-main}) reproduces established physics identifications (central charge duality, marginal-obstruction exchange, electric-magnetic splitting) when applied to specific CFT Koszul pairs.
2417:complementarity decomposition is functorial (property 3 of Theorem~\ref{thm:quantum-complementarity-main}), it commutes with the modular action.
2536:(Theorem~\ref{thm:quantum-complementarity-main}):
2605:(Theorem~\ref{thm:quantum-complementarity-main}) with
2643:The mathematical content is that Theorem~\ref{thm:quantum-complementarity-main}
2897:By Theorem~\ref{thm:quantum-complementarity-main},

thinking
**Evaluating DM-stack claims**

I need to decide whether to restrict the DM-stack claims and theorems to `g ≥ 2`, or if I should use `\overline{\mathcal M}_{g,1}` instead of `\overline{\mathcal M}_g` for low genus. I notice that the chapter currently combines `\overline{\mathcal M}_0=pt`, `\overline{\mathcal M}_{1,1}`, and `\overline{\mathcal M}_g` as if they belong to the same family, which is misleading. This impacts several lines, particularly around the Step I convergence lemma and the theorem statement that I should examine closely.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '486,550p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   486	The fiber-level concentration from Step~3 gives
   487	$\mathcal{H}^q(R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA)) = 0$
   488	for $q \neq 0$.
   489	Perfectness of $R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA)$
   490	(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
   491	uniformly over $\overline{\mathcal{M}}_g$.
   492	The surviving $\mathcal{H}^0$ is identified with
   493	$\mathcal{Z}_{\cA}$ by the fiber-level identification
   494	from Step~3, which holds uniformly over the base.
   495	If $\kappa(\cA)=0$, then $\dfib^{\,2}=0$ and the curved model is
   496	already an ordinary complex; the same conclusion can therefore be
   497	read directly on $\barB^{(g)}_{\mathrm{curv}}(\cA)$.
   498	\end{proof}
   499	
   500	\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
   501	\index{Theorem C!decomposition}
   502	Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
   503	identification, this theorem) produces the ambient complex;
   504	$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
   505	gives the Verdier eigenspace decomposition and its Lagrangian



thinking
**Identifying theorem discrepancies**

I’m noticing a potential issue in the theorem about "quantum corrections as spectral sequence limit." On lines 923-924, it states that `Q_g = E_\infty^{*,*,g}`, but previously, I defined `Q_g` as an eigenspace. I should probably reference lines 920-927 to clarify this inconsistency. It’s important to make sure everything aligns correctly!
thinking
**Exploring summary options**

I think the user might want me to check issues in N, possibly choosing 10 files, since I've read 10 of them. It seems I should consider producing links to these files. My final answer formatting suggests that I should use clickable markdown links for local files. But I wonder if I could alternatively present them in a plain format like file:line. There are a few options to consider for clarity!
thinking
**Analyzing DM stacks**

I’m encountering a problem with the chapter's statement that everything is over `\overline{\mathcal M}_g` for all `g ≥ 0`. It proves convergence using `\overline{\mathcal M}_g` as a proper DM stack of dimension `3g - 3`, but then it checks genus 1 on `\overline{\mathcal M}_{1,1}` and genus 0 on `\overline{\mathcal M}_0 = pt`. I notice that the low-genus base isn't being fixed consistently, which is a bit confusing.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '446,460p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   446	$\Defcyc(\cA)$
   447	(Definition~\ref{def:cyclic-deformation-bar}),
   448	and (when constructed)
   449	a genus-completed Maurer--Cartan datum~$\Theta_{\cA}$
   450	\textup{(}Theorem~\textup{\ref{thm:universal-MC}} for the
   451	non-scalar part\textup{)}.
   452	
   453	\item\label{D:center-htpy}
   454	A \emph{center local system}
   455	$\mathcal{Z}_{\cA}$ on $\overline{\mathcal{M}}_{g,\bullet}$
   456	\textup{(}or the appropriate modular parameter stack\textup{)},
   457	whose global sections house the obstruction classes.
   458	
   459	\item\label{D:discriminant-htpy}
   460	A \emph{spectral discriminant}



thinking
**Finalizing findings overview**

I’ve got the foundation text ready, but I think it’s better to use clickable items for the main sections. I want to ensure the problem texts are precise, grounded in the file content, without making guesses. For instance, I noted that the Step 7 family-over-moduli is an inference from the theorem text. Maybe I should include a summary line that states, "Checked: 10 files | Findings: 14 | Verdict: FAIL." 

Now, let's finalize the findings list!
thinking
**Clarifying findings and inconsistencies**

I need to ensure that the findings are clear and concise. I’ve identified several critical issues: for example, the fiber-cohomology-center lemma is missing a family hypothesis, and there are problems with the Verdier duality object in Step II. I also noted that the Step 7 curve switch misquotes a corollary about quantum-dual-complete.

In total, I have fourteen findings but I think it’s worth including a fifteenth finding about low-genus moduli inconsistency because it’s subtly significant. So, let’s summarize all fifteen findings now!
thinking
**Adjusting stable convention**

I need to fix the stable convention and check that my final line count isn’t too long. I’m thinking of having 15 bullet points, ideally with each being one concise sentence. If each bullet ends up being about two lines, that could lead to around 30 lines total, which might be manageable.

I want to ensure everything stays organized and clear, so this should work out fine! I’ll keep track of the length as I finalize it.
codex
- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:205](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:205) — PROBLEM: `\sigma` on `\mathbf C_g(\cA)=R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\cA))` is declared to come from `thm:verdier-bar-cobar`, but [chapters/theory/cobar_construction.tex:1313](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1313) is a genus-0 bar/cobar Verdier theorem on configuration-space objects, not a cochain-level involution on the genus-`g` center local system. FIX: Move Definition `def:complementarity-complexes` after `lem:verdier-involution-moduli`, or insert a new proposition before line 205 proving that Verdier duality plus Koszul identification induces `\sigma` on `\mathcal Z(\cA)`; cite that proposition instead of `thm:verdier-bar-cobar`.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:378](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:378) — PROBLEM: C0 assumes only “finite-dimensional fiber cohomology” and then invokes `lem:perfectness-criterion`, but [chapters/theory/higher_genus_complementarity.tex:288](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:288) proves perfectness only for the strict flat comparison family `(\barB^{(g)}(\cA),\Dg{g})` under PBW filterability plus finite-dimensional flat fiber cohomology, not for the curved family `R\pi_{g*}\bar B^{(g)}(\cA)`. FIX: Rewrite the theorem statement to use `R\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\cA)` and state both lemma hypotheses explicitly, or add a separate theorem transferring perfectness from the flat model to the curved one via `prop:gauss-manin-uncurving-chain`.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:407](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:407) — PROBLEM: C0 filters the curved fiber complex with `\dfib^{\,2}=\kappa(\cA)\omega_g`, takes ordinary cohomology of it, and then identifies the surviving `H^0` with `\bigoplus_p(\cA^!)_p` “hence with the center”; this violates the chapter’s own curved/flat distinction and contradicts [chapters/theory/chiral_koszul_pairs.tex:940](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:940), which only identifies bar cohomology with the Koszul dual, not with `Z(\cA)`. FIX: Replace Steps 2-4 by a strict-flat proof on `(\barB^{(g)}(\cA),\Dg{g})`, identify `H^0` first with the Koszul dual object, and add a separate cited step for the passage from that object to the center local system.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:552](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:552) — PROBLEM: the first proof of `thm:quantum-complementarity-main` is only a roadmap and ends at line 562; the actual argument starts later in detached proof environments, so the theorem’s `\ClaimStatusProvedHere` does not sit under one continuous proof block. FIX: Convert lines 552-562 into `\begin{remark}[Proof roadmap]...\end{remark}` and start the actual theorem proof at line 665, or keep the theorem proof environment open until line 1827.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:669](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:669) — PROBLEM: Step I invents a “genus filtration” on a single bar complex by summing contributions from varying genera, then proves a Leray statement using the product `\overline C_n(X)\times\overline{\mathcal M}_g\to\overline{\mathcal M}_g` at lines 755-760, and later justifies genus-exhaustiveness by finite bar degree at lines 897-903; these are three different filtrations/objects. FIX: Delete the genus-filtration package and replace it with the actual Leray spectral sequence for the relative Fulton-MacPherson family `\pi_{g,n}:\overline C_n(\mathcal C_g/\overline{\mathcal M}_g)\to\overline{\mathcal M}_g`, or explicitly define a completed all-genus bar object and prove a genuine genus-support filtration before using it.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:822](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:822) — PROBLEM: Step I asserts `d_{\mathrm{fiber}}^2=0` by the genus-0 Arnold relation, but [chapters/theory/higher_genus_foundations.tex:229](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:229) fixes the higher-genus convention `\dfib^{\,2}=\kappa(\cA)\omega_g`; the proof is using the wrong differential. FIX: Replace `d_{\mathrm{fiber}}` by the strict flat comparison differential and cite `thm:quantum-diff-squares-zero`, or restrict the entire Step I argument to the flat case `\kappa(\cA)=0`.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:920](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:920) — PROBLEM: `Q_g(\mathcal A)` is redefined here as `E_\infty^{*,*,g}=\operatorname{gr}^gH^*(\bar B(\mathcal A))`, but Definition `def:complementarity-complexes` already defined `Q_g` as the `\pm1`-eigenspace cohomology of `\sigma`; the lemma explicitly says this is only “anticipating Theorem C”, so the identification is circular. FIX: Rename the spectral-sequence object to `\operatorname{gr}^g H^*(\bar B^{\mathrm{full}}(\mathcal A))` and add a later comparison theorem if you want to identify it with `Q_g`.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:986](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:986) — PROBLEM: `lem:fiber-cohomology-center` fixes one curve `\Sigma_g`, computes with the curved differential `d=d_{\mathrm{coll}}+d_{\mathrm{curv}}`, and then upgrades the result to a sheaf over moduli by saying the OPE is local; no family-over-moduli hypothesis is stated, and ordinary cohomology of the curved complex is again used at lines 1052-1097. FIX: Add the missing family hypothesis on `(\mathcal A,\mathcal A^!)` over the universal curve and rewrite the lemma for the strict flat family `R^0\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\mathcal A)`; if only a pointwise statement is available, downgrade the lemma to a fixed-curve result.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1172](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1172) — PROBLEM: Step II treats `\Omega^*_{\log}` as Verdier self-dual and pairs it with another copy of `\Omega^*_{\log}`, but the repo’s own Verdier surface is [chapters/theory/poincare_duality.tex:170](/Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality.tex:170) plus [chapters/theory/cobar_construction.tex:353](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:353), which pair logarithmic forms with the `j_!`/distributional compact-support dual, not with themselves. FIX: Replace `thm:verdier-duality-config-complete` and `cor:duality-bar-complexes-complete` by citations to `thm:verdier-config` and `lem:verdier-extension-exchange`, and rewrite the bar pairing as `j_*` bar data against the `j_!`/distributional dual.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:1287](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1287) — PROBLEM: `cor:quantum-dual-complete` cites `thm:quantum-complementarity-main` for the genus-0 exception while it is still inside the proof lane of that theorem. FIX: Replace the citation with the explicit genus-0 calculation already written at lines 1785-1789, or cite an earlier genus-0 theorem outside this proof.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1329](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1329) — PROBLEM: `thm:kodaira-spencer-chiral-complete` starts with a fixed chiral algebra on a curve `X`, then silently upgrades to the universal curve `\pi:\mathcal C_g\to\overline{\mathcal M}_g` and `R^q\pi_*^{\mathrm{ch}}\mathcal A` as if `\mathcal A` were already a family over all genus-`g` curves; it also cites `cor:quantum-dual-complete` as if it gave `H^*(\bar B^{(g)}(\mathcal A))\cong H^*(\bar B^{(g)}(\mathcal A^!))^\vee`, which it does not. FIX: Add the missing family-over-moduli hypothesis and restate the theorem entirely in terms of the object actually produced by C0, or cite the corrected Step II duality theorem that genuinely acts on the same complex.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:1553](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1553) — PROBLEM: `lem:center-isomorphism` begins with “Since every `E_\infty`-chiral algebra...”, but the lemma assumes only a chiral Koszul pair; the cited module-duality theorem is [chapters/theory/chiral_koszul_pairs.tex:5287](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:5287), an `E_1` theorem with completeness/conilpotence hypotheses. FIX: Delete the `E_\infty` sentence and apply `thm:e1-module-koszul-duality` directly to the underlying `E_1`-chiral Koszul pair, stating its hypotheses explicitly.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:1913](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1913) — PROBLEM: `prop:lagrangian-eigenspaces` defines `\sigma=\mathbb D\circ\mathrm{KS}`, but `thm:kodaira-spencer-chiral-complete` never constructs a named isomorphism `\mathrm{KS}`; Part (i) also cites “Theorem~C, Step~7” at line 1907 instead of the actual named `lem:center-isomorphism`. FIX: Define `\sigma` via `lem:verdier-involution-moduli`, and replace the proof-step citation with `lem:center-isomorphism`; if a Kodaira-Spencer isomorphism is intended, state and prove it separately before using it.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:1976](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1976) — PROBLEM: `lem:bar-chart-lagrangian-lift` transports the ambient polarization through `R\Gamma(\overline{\mathcal M}_g,R\pi_{g*}\barB^{(g)}(\cA))` and `L_g:=\barB^{(g)}(\cA)[1]`, but C0 only has a plausible strict-flat statement, not one on the curved family. FIX: Replace every occurrence of `\barB^{(g)}(\cA)` in the transport square by the strict flat model `\barB^{(g)}_{\mathrm{flat}}(\cA)` and use `prop:gauss-manin-uncurving-chain` only as the comparison from curved to flat.

- [HIGH] [chapters/theory/higher_genus_complementarity.tex:2074](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2074) — PROBLEM: C2 treats `L_g:=\barB^{(g)}(\cA)[1]` as a dg Lie algebra and feeds it to the Kontsevich-Pridham machine, but elsewhere the same higher-genus bar object is curved when `\kappa(\cA)\neq0`; only the strict flat model is an honest dg object. FIX: Redefine `L_g` as `(\barB^{(g)}(\cA),\Dg{g})[1]`, or add an explicit flatness hypothesis `\kappa(\cA)=0` before any dg-Lie or formal-moduli claim.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:200](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:200) — PROBLEM: the chapter states everything over `\overline{\mathcal M}_g` for all `g\ge0`, but the proof later uses `\overline{\mathcal M}_{1,1}` at line 1791 and the DM-stack dimension formula `3g-3` at lines 869-872; the low-genus base is not fixed consistently. FIX: Choose one stable convention and propagate it everywhere: either restrict the unmarked theory to `g\ge2` and add separate low-genus propositions, or replace the low-genus ambient spaces by stable marked stacks and correct the degree shifts.

## Summary
Checked: 10 | Findings: 15 | Verdict: FAIL
tokens used
285,588
